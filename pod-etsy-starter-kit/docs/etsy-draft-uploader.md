# Etsy Draft Uploader

Der Uploader erstellt Etsy-Listings als Drafts aus:

```text
production/first-batch/etsy-drafts/etsy_draft_payloads.json
```

Er veroeffentlicht keine Listings live.

## Warum ich nicht direkt in deinen Etsy-Account gehen kann

Diese Cloud-Umgebung hat keinen Zugriff auf deinen lokalen Browser, deine Etsy-Session oder deine 2FA. Fuer echte Account-Aktionen braucht Etsy OAuth-Zugangsdaten. Deshalb liest der Uploader alle sensiblen Werte aus Umgebungsvariablen und speichert keine Tokens im Repository.

## Voraussetzungen

- Etsy Developer App/API Key
- OAuth Access Token mit Listing-Schreibrechten
- Etsy Shop ID
- Etsy Taxonomy ID fuer T-Shirt Kategorie
- Etsy Shipping Profile ID
- optional: Return Policy ID

## Konfiguration

Beispiel:

```bash
export ETSY_API_KEY="dein_etsy_api_key"
export ETSY_ACCESS_TOKEN="dein_oauth_access_token"
export ETSY_SHOP_ID="deine_shop_id"
export ETSY_TAXONOMY_ID_TSHIRT="deine_tshirt_taxonomy_id"
export ETSY_SHIPPING_PROFILE_ID="deine_shipping_profile_id"
export ETSY_RETURN_POLICY_ID="deine_return_policy_id"
```

Oder lokal:

```bash
cp pod-etsy-starter-kit/scripts/etsy.env.example .env
# .env ausfuellen, aber nicht committen
```

## Dry-Run

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py
```

Der Dry-Run prueft die Payloads und zeigt, welche Drafts erstellt wuerden.

## Nur ein Design testen

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --only DOG-0001
```

## Drafts bei Etsy erstellen

Erst ausfuehren, wenn:

- OAuth funktioniert
- Shop-/Shipping-/Taxonomy-IDs korrekt sind
- Rechtscheck fuer die Claims erledigt ist
- du bewusst Etsy-Drafts erzeugen willst

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --execute
```

Nur ein Draft:

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --only DOG-0001 --execute
```

## Nach der Draft-Erstellung

Der Etsy API Draft enthaelt Textdaten. Danach musst du:

1. PNG-Design aus SVG exportieren.
2. Produktbilder/Mockups erstellen.
3. Bilder in Etsy/Printify hochladen.
4. Varianten/Inventory pruefen.
5. Etsy-Vorschau manuell pruefen.
6. Erst nach QC live schalten.

## Sicherheitsregeln

- Kein `--execute`, solange Rechtscheck offen ist.
- Keine echten Tokens committen.
- Keine Listings automatisch live schalten.
- Immer zuerst `--only DOG-0001 --execute` als Einzeltest.

