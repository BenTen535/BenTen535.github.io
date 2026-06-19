# POD Etsy Starter Kit

Dieses Starter-Kit ist ein praktisches Betriebssystem fuer einen automatisierten deutschen Print-on-Demand-Etsy-Shop. Es ist bewusst auf generische, markenfreie Nischen ausgelegt: Geburtstage, Jahrgaenge, Berufe, Hobbys, Mama/Papa, Hundebesitzer, Fitness, Handwerker und Gaming.

## Grundregel

Kein Design geht live, bevor es den Rechts- und Qualitaetscheck bestanden hat. Keine Marken, keine Logos, keine Promis, keine Film-/Serien-/Game-/Song-Referenzen, keine Fussballvereine, keine geschuetzten Namen.

## Empfohlener Start-Stack

| Bereich | Empfehlung | Alternative guenstig |
|---|---|---|
| Datenzentrale | Google Sheets oder Airtable | Google Sheets |
| Ideen/Text | Claude oder ChatGPT | Claude/ChatGPT Free |
| Recherche | Etsy Suche, Google Trends, Pinterest, eRank/EverBee | Etsy Suche, Google Trends |
| Design | Ideogram, Canva, Kittl | Canva Free, Inkscape, Photopea |
| Vektor/Export | Illustrator, Vectorizer.ai | Inkscape |
| Mockups | Printify Mockups, Placeit, Canva | Printify Mockups |
| POD | Printify oder Printful | Printify |
| Automation | Make.com oder n8n | n8n self-hosted |
| Shop | Etsy | Etsy |

## Ziel-Workflow

```text
Claude
-> Nischenidee
-> Spruch/Claim
-> Marken-/Copyright-Check
-> Design-Prompt
-> Ideogram/Midjourney/Canva
-> PNG/SVG Export
-> Qualitaetscheck
-> Mockup mit Placeit/Canva/Printify
-> Claude erstellt SEO-Titel, Tags, Beschreibung
-> Google Sheet Status = Approved
-> Make.com/n8n erstellt Etsy/Printify Draft
-> Manuelle Endkontrolle
-> Etsy Listing veroeffentlichen
-> Printify produziert erst nach Kauf
-> Ergebnisdaten zurueck ins Sheet
-> Gewinnerdesigns skalieren
```

## Ordnerstruktur

```text
pod-etsy-starter-kit/
  README.md
  docs/
    operating-system.md
    legal-and-quality-control.md
  templates/
    design_tracker.csv
    30_day_plan.csv
    first_100_design_ideas.csv
    etsy_listing_examples.csv
  prompts/
    design_prompts.md
    listing_prompts.md
  automations/
    n8n-pod-etsy-pipeline.json
```

## Erste Schritte

1. `templates/design_tracker.csv` in Google Sheets importieren.
2. `templates/30_day_plan.csv` als Tagesplan verwenden.
3. Jeden Tag eine Nische aus `templates/first_100_design_ideas.csv` waehlen.
4. Claim rechtlich pruefen: DPMAregister, EUIPO/TMview, Google, Etsy.
5. Prompt aus `prompts/design_prompts.md` verwenden.
6. Design als transparentes PNG exportieren: 4500 x 5400 px.
7. Mockups erstellen.
8. Listing-Daten mit `prompts/listing_prompts.md` generieren.
9. Alles mit `docs/legal-and-quality-control.md` pruefen.
10. Erst als Etsy Draft anlegen, danach manuell freigeben.

## Skalierungsprinzip

Starte nicht direkt mit 200 Live-Listings pro Tag. Baue zuerst einen stabilen Qualitaetsprozess:

- Phase 1: 5-10 Listings/Tag, manuell kontrolliert
- Phase 2: 20-50 Listings/Tag, batchweise vorbereitet
- Phase 3: 50-200 Drafts/Tag, aber mit gestaffelter Veroeffentlichung

Der Engpass darf nie die Rechtspruefung sein. Wenn die Kontrolle nicht sauber skaliert, skaliert das Risiko mit.

## Kennzahlen

Tracke mindestens:

- Views
- Favoriten
- Klickrate
- Warenkorb
- Verkaeufe
- Conversion Rate
- Umsatz
- Produktionskosten
- Versandkosten
- Etsy Fees
- Marge
- Rueckgaben/Reklamationen

## Empfohlene Tagesroutine nach Tag 30

1. 30 Minuten Nischen-/Keyword-Recherche
2. 45 Minuten Claims und Prompt-Batches erzeugen
3. 60 Minuten Designproduktion
4. 30 Minuten Mockups
5. 30 Minuten Listings/SEO
6. 30 Minuten QC und Draft-Freigabe
7. 15 Minuten Performance-Auswertung

