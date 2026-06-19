#!/usr/bin/env python3
"""Create Etsy draft listings from the prepared POD batch payloads.

Default mode is a dry-run. Use --execute only after Etsy OAuth credentials and
the required shop IDs are configured as environment variables.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_PAYLOAD_FILE = (
    Path(__file__).resolve().parents[1]
    / "production"
    / "first-batch"
    / "etsy-drafts"
    / "etsy_draft_payloads.json"
)

ETSY_CREATE_DRAFT_URL = "https://openapi.etsy.com/v3/application/shops/{shop_id}/listings"


class ConfigError(RuntimeError):
    """Raised when required configuration is missing."""


def env_required(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise ConfigError(f"Missing required environment variable: {name}")
    return value


def env_optional(name: str) -> str | None:
    value = os.environ.get(name, "").strip()
    return value or None


def load_payload(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload.get("drafts"), list):
        raise ConfigError("Payload file must contain a 'drafts' array.")
    return payload


def replace_placeholders(defaults: dict[str, Any]) -> dict[str, Any]:
    resolved = dict(defaults)
    resolved["taxonomy_id"] = int(env_required("ETSY_TAXONOMY_ID_TSHIRT"))
    resolved["shipping_profile_id"] = int(env_required("ETSY_SHIPPING_PROFILE_ID"))

    return_policy_id = env_optional("ETSY_RETURN_POLICY_ID")
    if return_policy_id:
        resolved["return_policy_id"] = int(return_policy_id)
    else:
        resolved.pop("return_policy_id", None)

    return resolved


def validate_draft(draft: dict[str, Any]) -> None:
    required = ["design_id", "title", "description", "tags", "price", "qc_status"]
    missing = [field for field in required if not draft.get(field)]
    if missing:
        raise ConfigError(f"{draft.get('design_id', '<unknown>')}: missing {', '.join(missing)}")

    tags = draft["tags"]
    if not isinstance(tags, list) or len(tags) != 13:
        raise ConfigError(f"{draft['design_id']}: Etsy drafts should contain exactly 13 tags.")

    if draft["qc_status"] != "Design Ready - Legal Check Pending":
        raise ConfigError(
            f"{draft['design_id']}: expected conservative QC status, got {draft['qc_status']!r}"
        )

    forbidden_hints = [
        "disney",
        "nike",
        "adidas",
        "star wars",
        "harry potter",
        "pokemon",
        "fifa",
    ]
    haystack = " ".join(
        [
            draft["title"],
            draft["description"],
            " ".join(tags),
        ]
    ).lower()
    matches = [term for term in forbidden_hints if term in haystack]
    if matches:
        raise ConfigError(f"{draft['design_id']}: forbidden brand/franchise hints: {matches}")


def build_etsy_form(defaults: dict[str, Any], draft: dict[str, Any]) -> dict[str, Any]:
    validate_draft(draft)

    form = {
        "quantity": defaults.get("quantity", 999),
        "title": draft["title"],
        "description": draft["description"],
        "price": f"{float(draft['price']):.2f}",
        "who_made": defaults.get("who_made", "i_did"),
        "when_made": defaults.get("when_made", "made_to_order"),
        "is_supply": str(defaults.get("is_supply", False)).lower(),
        "should_auto_renew": str(defaults.get("should_auto_renew", True)).lower(),
        "type": defaults.get("type", "physical"),
        "taxonomy_id": defaults["taxonomy_id"],
        "shipping_profile_id": defaults["shipping_profile_id"],
        "processing_min": defaults.get("processing_min", 2),
        "processing_max": defaults.get("processing_max", 7),
        "tags": draft["tags"],
        "materials": defaults.get("materials", []),
    }

    if "return_policy_id" in defaults:
        form["return_policy_id"] = defaults["return_policy_id"]

    return form


def create_draft(api_key: str, access_token: str, shop_id: str, form: dict[str, Any]) -> dict[str, Any]:
    encoded = urllib.parse.urlencode(form, doseq=True).encode("utf-8")
    request = urllib.request.Request(
        ETSY_CREATE_DRAFT_URL.format(shop_id=shop_id),
        data=encoded,
        method="POST",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/x-www-form-urlencoded",
            "x-api-key": api_key,
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Etsy API error {error.code}: {body}") from error


def compact_preview(form: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": form["title"],
        "price": form["price"],
        "quantity": form["quantity"],
        "taxonomy_id": form["taxonomy_id"],
        "shipping_profile_id": form["shipping_profile_id"],
        "return_policy_id": form.get("return_policy_id"),
        "tags": form["tags"],
        "materials": form["materials"],
        "state": "draft",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create Etsy draft listings from POD payloads.")
    parser.add_argument("--payloads", type=Path, default=DEFAULT_PAYLOAD_FILE)
    parser.add_argument("--only", action="append", help="Only process the given Design-ID. Can be repeated.")
    parser.add_argument("--execute", action="store_true", help="Actually call Etsy. Default is dry-run.")
    args = parser.parse_args()

    payload = load_payload(args.payloads)
    defaults = replace_placeholders(payload.get("defaults", {})) if args.execute else {
        **payload.get("defaults", {}),
        "taxonomy_id": os.environ.get("ETSY_TAXONOMY_ID_TSHIRT", "ETSY_TAXONOMY_ID_TSHIRT"),
        "shipping_profile_id": os.environ.get("ETSY_SHIPPING_PROFILE_ID", "ETSY_SHIPPING_PROFILE_ID"),
        "return_policy_id": os.environ.get("ETSY_RETURN_POLICY_ID", "ETSY_RETURN_POLICY_ID"),
    }

    selected = set(args.only or [])
    drafts = [
        draft for draft in payload["drafts"] if not selected or draft.get("design_id") in selected
    ]
    if selected and len(drafts) != len(selected):
        found = {draft.get("design_id") for draft in drafts}
        missing = sorted(selected - found)
        raise ConfigError(f"Unknown Design-ID(s): {', '.join(missing)}")

    if args.execute:
        api_key = env_required("ETSY_API_KEY")
        access_token = env_required("ETSY_ACCESS_TOKEN")
        shop_id = env_required("ETSY_SHOP_ID")
    else:
        api_key = access_token = shop_id = ""

    results: list[dict[str, Any]] = []
    for draft in drafts:
        form = build_etsy_form(defaults, draft)
        if args.execute:
            response = create_draft(api_key, access_token, shop_id, form)
            listing_id = response.get("listing_id") or response.get("listing", {}).get("listing_id")
            print(f"CREATED_DRAFT {draft['design_id']} listing_id={listing_id}")
            results.append({"design_id": draft["design_id"], "listing_id": listing_id, "response": response})
        else:
            print(f"DRY_RUN {draft['design_id']}")
            print(json.dumps(compact_preview(form), indent=2, ensure_ascii=False))

    if args.execute:
        print(json.dumps({"created": results}, indent=2, ensure_ascii=False))
    else:
        print("Dry-run complete. Set Etsy environment variables and run with --execute to create drafts.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ConfigError as error:
        print(f"Configuration error: {error}", file=sys.stderr)
        raise SystemExit(2)
