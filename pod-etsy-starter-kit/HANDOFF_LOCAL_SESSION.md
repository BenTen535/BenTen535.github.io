# Handoff fuer lokale Cursor-Session

Diese Datei fasst den Stand dieses Chats zusammen, damit du lokal auf deinem PC direkt weitermachen kannst.

## Ziel

Automatisierter deutscher Print-on-Demand-Etsy-Shop mit:

- markenfreien T-Shirt-Designs
- Etsy-Draft-Listings
- Printify/Printful-Anbindung
- Google-Sheets/CSV-Tracker
- rechtlicher QC vor Veroeffentlichung
- spaeterer Skalierung auf groessere Listing-Batches

## Aktueller Branch

```bash
cursor/pod-etsy-starter-kit-3f3d
```

## Lokal holen

Im lokalen Projektordner:

```bash
git fetch origin cursor/pod-etsy-starter-kit-3f3d
git checkout cursor/pod-etsy-starter-kit-3f3d
git pull origin cursor/pod-etsy-starter-kit-3f3d
```

Falls du das Repo noch nicht lokal hast:

```bash
git clone <DEIN_REPO_URL>
cd <REPO_ORDNER>
git checkout cursor/pod-etsy-starter-kit-3f3d
```

## Wichtigste Dateien

```text
pod-etsy-starter-kit/README.md
pod-etsy-starter-kit/docs/operating-system.md
pod-etsy-starter-kit/docs/legal-and-quality-control.md
pod-etsy-starter-kit/docs/etsy-draft-uploader.md
pod-etsy-starter-kit/templates/design_tracker.csv
pod-etsy-starter-kit/templates/30_day_plan.csv
pod-etsy-starter-kit/templates/first_100_design_ideas.csv
pod-etsy-starter-kit/templates/etsy_listing_examples.csv
pod-etsy-starter-kit/production/first-batch/
pod-etsy-starter-kit/scripts/create_etsy_drafts.py
pod-etsy-starter-kit/scripts/etsy.env.example
```

## Was bereits erstellt wurde

### Starter-Kit

- Betriebsanleitung
- Rechts-/QC-Checkliste
- Prompt-Bibliothek fuer Design und Listing-SEO
- Google-Sheets/CSV-Struktur
- n8n-Draft-Pipeline-Skelett

### Erster 5er-Batch

SVG-Designs:

```text
DOG-0001-gassi-ist-mein-cardio.svg
BDAY-0001-legende-seit-1984.svg
PAPA-0001-papa-repariert-das-schon.svg
JOB-0001-erzieherin-herz-nerven-stahl.svg
GAME-0001-nur-noch-eine-runde.svg
```

Listing-Daten:

```text
production/first-batch/listings_ready_for_review.csv
production/first-batch/etsy-drafts/etsy_draft_payloads.json
production/first-batch/etsy-drafts/etsy_manual_copy_paste.csv
```

## Validierter Stand

Geprueft wurde:

- CSV-Dateien parsebar
- konsistente Spaltenzahlen
- n8n-JSON parsebar
- 5 SVG-Dateien XML-valide
- alle SVGs 4500 x 5400
- Etsy-Draft-Payloads enthalten 5 Drafts
- jeder Draft hat 13 Tags
- Etsy-Uploader Dry-Run funktioniert

## Lokal weiterarbeiten mit Cursor

Wenn du Cursor lokal oeffnest, kannst du diesen Prompt in eine neue lokale Session kopieren:

```text
Wir arbeiten am Branch cursor/pod-etsy-starter-kit-3f3d.
Bitte lies zuerst pod-etsy-starter-kit/HANDOFF_LOCAL_SESSION.md.
Ziel: Die vorbereiteten POD-Etsy-Designs lokal weiterverarbeiten.
Naechste Schritte:
1. SVGs aus production/first-batch/designs als transparente PNGs exportieren.
2. Etsy API/OAuth Werte lokal setzen.
3. create_etsy_drafts.py zuerst im Dry-Run, dann fuer DOG-0001 mit --execute testen.
4. Printify/Etsy Drafts pruefen.
5. Keine Listings live schalten, bis DPMA/EUIPO/TMview/Etsy/Google Check erledigt ist.
```

## Etsy API Werte lokal setzen

Kopiere das Beispiel:

```bash
cp pod-etsy-starter-kit/scripts/etsy.env.example .env
```

Dann `.env` ausfuellen:

```bash
ETSY_API_KEY=...
ETSY_ACCESS_TOKEN=...
ETSY_SHOP_ID=...
ETSY_TAXONOMY_ID_TSHIRT=...
ETSY_SHIPPING_PROFILE_ID=...
ETSY_RETURN_POLICY_ID=...
```

Variablen laden:

```bash
set -a
source .env
set +a
```

## Etsy-Drafts testen

Dry-Run fuer ein Design:

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --only DOG-0001
```

Wenn das korrekt aussieht und die Etsy-Werte gesetzt sind:

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --only DOG-0001 --execute
```

Wenn der Einzeltest klappt:

```bash
python3 pod-etsy-starter-kit/scripts/create_etsy_drafts.py --execute
```

## SVG zu PNG exportieren

Empfohlen lokal:

- Canva
- Inkscape
- Kittl
- Illustrator

Export-Einstellungen:

```text
PNG
transparent background
4500 x 5400 px
hoher Kontrast
```

## Nicht ueberspringen

Vor Live-Schaltung jedes Designs:

```text
DPMA geprueft = Ja
EUIPO/TMview geprueft = Ja
Etsy/Google geprueft = Ja
Status = QC Approved
```

Bis dahin bleibt alles:

```text
Design Ready - Legal Check Pending
Draft only
```

