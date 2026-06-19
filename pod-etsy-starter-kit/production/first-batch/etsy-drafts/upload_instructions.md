# Etsy/Printify Upload Instructions fuer den ersten 5er-Batch

Ich kann aus dieser Umgebung ohne Etsy-OAuth/Login keine Listings in deinem Etsy-Shop anlegen. Dieses Paket bereitet die Anzeigen aber so vor, dass sie als Etsy-Drafts angelegt werden koennen.

## Warum Draft-only?

Die Designs sind markenfrei erstellt, aber noch nicht extern geprueft. Vor Live-Schaltung:

- DPMAregister pruefen
- EUIPO/TMview pruefen
- Etsy-Suche pruefen
- Google-Suche pruefen
- finale Mockups pruefen
- Produktvarianten und Margen pruefen

## Empfohlener Weg: Printify -> Etsy Draft

1. Bei Etsy einloggen.
2. Printify mit Etsy verbinden.
3. In Printify ein Produkt anlegen:
   - Produkt: Unisex T-Shirt
   - Anbieter: nach Lieferzeit/Preis/Qualitaet auswaehlen
   - Farben: Schwarz, Weiss, Navy, Heather Grey nach Design-Kontrast
   - Groessen: S bis 3XL, falls verfuegbar
4. SVG aus `../designs/` in Canva/Inkscape oeffnen.
5. Als PNG exportieren:
   - 4500 x 5400 px
   - transparenter Hintergrund
6. PNG in Printify hochladen.
7. Designposition pruefen:
   - mittig
   - nicht zu klein
   - nicht zu nah am Kragen
8. Printify-Mockups generieren.
9. Listing-Daten aus `etsy_draft_payloads.json` oder `../listings_ready_for_review.csv` uebernehmen.
10. Als Etsy-Draft speichern, nicht live veroeffentlichen.
11. QC-Checkliste aus `../../docs/legal-and-quality-control.md` abarbeiten.
12. Erst nach PASS den Etsy-Draft veroeffentlichen.

## Direkter Etsy API Weg

Wenn du Etsy API-Zugang hast, benoetigst du:

- Etsy App/API Key
- OAuth Access Token
- Shop ID
- Taxonomy ID fuer T-Shirts
- Shipping Profile ID
- Return Policy ID

Die Payloads liegen in:

```text
etsy_draft_payloads.json
```

Platzhalter ersetzen:

```text
ETSY_SHOP_ID
ETSY_TAXONOMY_ID_TSHIRT
ETSY_SHIPPING_PROFILE_ID
ETSY_RETURN_POLICY_ID
```

Automatischer Uploader:

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --only DOG-0001 --execute
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --execute
```

Details stehen in:

```text
pod-etsy-starter-kit/docs/etsy-draft-uploader.md
```

Danach:

1. Listing als Draft erstellen.
2. Mockup-Bilder hochladen.
3. Varianten/Inventory setzen.
4. Vorschau manuell pruefen.
5. Erst nach QC live schalten.

## Bild-Reihenfolge je Listing

1. Hauptmockup frontal
2. Detailansicht Design
3. Lifestyle-Mockup
4. Farbvarianten
5. Groessentabelle
6. Pflegehinweis oder Geschenkbild

## Konservative Produktempfehlung

Startprodukt:

```text
Unisex Jersey T-Shirt
Preis: 24.99 EUR
Status: Draft
Produktion: made_to_order
```

## Finaler Freigabesatz

Ein Listing darf erst live gehen, wenn im Tracker steht:

```text
DPMA geprueft = Ja
EUIPO/TMview geprueft = Ja
Etsy/Google geprueft = Ja
Status = QC Approved
```

