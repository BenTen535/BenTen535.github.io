# Betriebsanleitung: Automatisierter POD-Etsy-Shop

Diese Anleitung beschreibt das operative System fuer einen deutschen POD-Shop, bei dem Produkte erst nach Kauf ueber Printify oder Printful produziert werden.

## 1. Nischenrecherche

### Quellen

- Etsy Autocomplete: `geburtstag shirt`, `mama shirt`, `hundemama shirt`, `handwerker shirt`
- Google Trends: saisonale Peaks und Suchinteresse
- Pinterest: visuelle Stilrichtungen und Geschenk-Anlaesse
- eRank/EverBee/Alura: Keyword-Volumen, Konkurrenz, Listing-Analyse
- Amazon Merch: generische Motivtypen, keine Marken kopieren
- TikTok/Reels: Alltagssprache und Humortrends, keine geschuetzten Referenzen uebernehmen

### Bewertungslogik

Eine Nische ist gut, wenn sie:

- einen klaren Kaeufer hat
- einen klaren Anlass hat
- ohne Marken/Promis funktioniert
- viele Varianten erlaubt
- als Geschenk taugt
- mit einfacher Typografie stark genug ist

### Gute Start-Cluster

- Geburtstag + Jahrgang
- Mama/Papa + Rolle
- Hundebesitzer + Alltag
- Beruf + Humor
- Hobby + Identitaet
- Fitness + Disziplin
- Handwerker + Werkzeughumor
- Gaming + generische Gamer-Sprache

## 2. Ideen-Generierung

Pro Nische werden immer mehrere Ebenen erzeugt:

1. Zielgruppe
2. Anlass
3. Emotion
4. Claim
5. visuelles Motiv
6. Listing-Keyword
7. Risiko-Notiz

Beispiel:

```text
Nische: Hundebesitzer
Zielgruppe: Hundemama
Anlass: Geburtstag, Weihnachten, Alltag
Emotion: stolz, liebevoll, humorvoll
Claim: Gassi ist mein Cardio
Motiv: Pfoten, kleine Sneaker, minimalistische Typografie
Keyword: hundemama shirt
Risiko: niedrig, generischer Spruch
```

## 3. Sprueche/Claims

### Claim-Regeln

- kurz und gut lesbar
- keine Markenbegriffe
- keine Zitate aus Songs/Filmen/Serien
- keine Prominamen
- keine Vereinsnamen
- keine bekannten Logos oder Maskottchen
- keine "inspiriert von"-Designs

### Claim-Formeln

```text
[Rolle] braucht [Alltagsding]
Beispiel: Mama braucht Kaffee

[Hobby] ist mein [Therapie/Workout/Luxus]
Beispiel: Angeln ist Therapie

[Rolle] seit [Jahr]
Beispiel: Papa seit 2024

[Eigenschaft] mit [Humorbild]
Beispiel: Nerven aus Stahl, Herz aus Gold

[Alltagssituation] statt [Alternative]
Beispiel: Werkzeug statt Worte
```

## 4. Design-Erstellung

### Druckstandard

- PNG mit transparentem Hintergrund
- 4500 x 5400 px
- 300 DPI oder druckfaehige Pixelgroesse
- hoher Kontrast
- maximal 2-4 Hauptfarben
- Motiv mittig
- Text gross genug
- keine feinen Details, die beim Druck verschwinden

### SVG

SVG ist ideal fuer reine Typografie und einfache Icons. Wenn KI-Bilder genutzt werden, zuerst sauber vektorisieren und Artefakte entfernen.

## 5. Mockup-Erstellung

Pro Listing:

- 1 Hauptmockup frontal
- 1 Detailansicht Design
- 1 Lifestyle-Mockup
- 1 Farbuebersicht
- 1 Groessentabelle
- optional: Geschenk-/Anlass-Mockup

Hauptbild soll sofort zeigen:

- Shirtfarbe
- Design
- Zielgruppe
- Anlass

## 6. Etsy-Listing-Erstellung

### Listing-Bestandteile

- Titel mit Hauptkeyword am Anfang
- 13 Tags
- klare Beschreibung
- Groessenhinweis
- Materialhinweis
- Pflegehinweise
- Produktions-/Versandhinweis
- keine falschen Versprechen

### Titel-Formel

```text
[Hauptkeyword] [Claim], [Zielgruppe] Geschenk, [Anlass], [Produktart]
```

Beispiel:

```text
Hundemama Shirt Gassi ist mein Cardio, Geschenk fuer Hundebesitzerin, lustiges Hunde T-Shirt
```

## 7. SEO

### Keyword-Quellen

- Etsy Autocomplete
- Top-Listings ohne Markenkopien
- eRank/EverBee
- Google Suggest
- Synonyme in Deutsch

### Tag-Regeln

- 13 Tags nutzen
- Tags nicht verschwenden
- verschiedene Suchintentionen abdecken:
  - Produkt: `t shirt`, `shirt damen`
  - Zielgruppe: `hundemama`
  - Anlass: `geburtstag`
  - Stil: `lustiges shirt`
  - Geschenk: `geschenk frau`

## 8. Printify/Printful

### Setup

1. Etsy mit Printify/Printful verbinden.
2. Standardprodukt waehlen, z.B. Unisex Jersey T-Shirt.
3. Druckanbieter nach Qualitaet, Lieferzeit und Kosten auswaehlen.
4. Standardfarben definieren.
5. Versandprofile pruefen.
6. Preisformel anlegen.

### Preislogik

```text
Verkaufspreis - Produktionskosten - Versandkosten - Etsy Fees - Zahlungsgebuehren = Gewinn
```

Keine Produkte live stellen, deren Marge nach Rabatten unklar ist.

## 9. Automatisierung

### Statuslogik im Sheet

```text
Idea
-> Legal Check
-> Prompt Ready
-> Design Ready
-> Mockup Ready
-> Listing Ready
-> QC Review
-> Etsy Draft
-> Live
-> Optimize
```

### Automationsgrenze

Automatisiere Vorbereitung, nicht blindes Veröffentlichen. Der letzte Schritt bleibt manuell, bis der Prozess stabil und rechtlich sicher ist.

## 10. Qualitaetskontrolle

Siehe `legal-and-quality-control.md`. Kein Design darf online, wenn:

- der Claim unklar rechtlich riskant ist
- Textfehler enthalten sind
- KI-Artefakte sichtbar sind
- Mockups irrefuehrend sind
- Produktvarianten nicht geprueft wurden

## 11. Skalierung

### Batch-System

- Batch 1: 50 Claims
- Batch 2: Rechtscheck
- Batch 3: 20-40 Designs
- Batch 4: Mockups
- Batch 5: Listing-Daten
- Batch 6: QC
- Batch 7: Drafts

### Varianten statt Kopien

Gute Varianten:

- anderer Jahrgang
- andere Zielgruppe
- anderes Produkt
- andere Farbkombination
- anderer Anlass
- anderer Stil

Schlechte Varianten:

- praktisch identische Listings
- minimal andere Wortstellung
- Massen-Duplikate ohne Suchintention

