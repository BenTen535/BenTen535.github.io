# Design-Prompts fuer Ideogram, Midjourney und Canva

Alle Prompts muessen markenfrei bleiben. Keine Logos, keine Figuren, keine Promis, keine Vereinsfarben in Kombination mit Vereinsbezug, keine Film-/Serien-/Game-Namen.

## Master-Prompt fuer Claim-Ideen

```text
Du bist ein deutscher Print-on-Demand-Nischenstratege fuer Etsy.

Erstelle 30 markenfreie T-Shirt-Ideen fuer diese Nische:
Nische: [NISCHE]
Zielgruppe: [ZIELGRUPPE]
Anlass: [ANLASS]

Regeln:
- Deutschsprachige Zielgruppe
- Keine Marken, Logos, Promis, Filmtitel, Serien, Games, Songtexte, Fussballvereine
- Keine bekannten Zitate
- Kurze Sprueche mit maximal 7 Woertern bevorzugen
- Geschenkfaehig, humorvoll oder emotional
- Zu jeder Idee: Spruch, Zielgruppe, Anlass, visuelles Motiv, Hauptkeyword, Risiko niedrig/mittel/hoch

Gib die Ausgabe als CSV-kompatible Tabelle aus.
```

## Master-Prompt fuer Design-Prompts

```text
Du bist ein POD-Art-Director fuer deutsche Etsy-T-Shirts.

Erstelle fuer den folgenden Spruch 3 Design-Prompts:
Spruch: [SPRUCH]
Nische: [NISCHE]
Zielgruppe: [ZIELGRUPPE]
Anlass: [ANLASS]
Designrichtung: [DESIGNRICHTUNG]

Regeln:
- Transparent background
- Print-ready t-shirt design
- 4500 x 5400 px geeignet
- Maximal 2-4 Farben
- Hoher Kontrast
- Sehr gut lesbare Typografie
- Zentriertes Layout
- Keine Marken, Logos, geschuetzten Figuren, Promis oder bekannten Franchise-Elemente
- Keine Mockup-Darstellung, kein Shirt im Bild, nur das Design

Gib je Prompt eine Version fuer:
1. Ideogram
2. Midjourney
3. Canva
```

## Ideogram Prompt-Formel

```text
T-shirt design, transparent background, German text: "[SPRUCH]", [MOTIV], [STIL], centered composition, bold readable typography, high contrast, limited color palette, print-ready, no shirt mockup, no logos, no brands, no copyrighted characters, no celebrities
```

### Beispiele

```text
T-shirt design, transparent background, German text: "Gassi ist mein Cardio", minimal paw prints and small sneaker icon, clean typography, white and beige colors, centered composition, high contrast, print-ready, no shirt mockup, no logos, no brands, no copyrighted characters, no celebrities
```

```text
T-shirt design, transparent background, German text: "Legende seit 1984", vintage badge layout, distressed cream and orange typography, retro birthday design, centered composition, high contrast, print-ready, no shirt mockup, no logos, no brands, no copyrighted characters
```

```text
T-shirt design, transparent background, German text: "Nur noch eine Runde", generic pixel typography, small abstract controller icon, neon green and white, centered composition, high contrast, print-ready, no game names, no logos, no copyrighted characters
```

## Midjourney Prompt-Formel

```text
German typography t-shirt design saying "[SPRUCH]", [MOTIV], [STIL], bold readable letters, centered layout, limited color palette, screen print style, transparent background feel, no logos, no brands, no copyrighted characters, no celebrities --ar 5:6 --v 6
```

### Beispiele

```text
German typography t-shirt design saying "Papa repariert das schon", vintage workshop style, small wrench illustration, bold readable letters, centered layout, limited color palette, black white beige, screen print style, transparent background feel, no logos, no brands, no characters --ar 5:6 --v 6
```

```text
German typography t-shirt design saying "Erzieherin mit Herz und Nerven aus Stahl", clean teacher appreciation style, small heart icon, warm neutral colors, bold readable letters, centered layout, screen print style, transparent background feel, no logos, no brands --ar 5:6 --v 6
```

## Canva Prompt-Formel

```text
Erstelle ein minimalistisches T-Shirt-Design mit dem Text "[SPRUCH]".
Stil: [STIL]
Motiv: [MOTIV]
Farben: [FARBEN]
Layout: zentriert, klare Hierarchie, sehr gut lesbar.
Wichtig: Keine Marken, keine Logos, keine geschuetzten Figuren, keine Promis, kein Mockup.
Export: transparenter Hintergrund, druckfaehig.
```

### Beispiele

```text
Erstelle ein minimalistisches T-Shirt-Design mit dem Text "Mama braucht Kaffee".
Nutze eine moderne serifenlose Schrift, eine kleine Kaffeetasse als Icon, warme Beige- und Weisstoene, zentriertes Layout und hohe Lesbarkeit.
Keine Marken, keine Logos, keine geschuetzten Figuren, keine Promis, kein Mockup.
```

```text
Erstelle ein Vintage-T-Shirt-Design mit dem Text "Baujahr 1979, laeuft noch".
Nutze ein Werkstatt-Label, dezente Retro-Textur, Creme und Orange, klare fette Schrift.
Keine Marken, keine Logos, keine geschuetzten Figuren, keine Promis, kein Mockup.
```

## Negative Prompt Bausteine

Nutze diese Ausschluesse, wenn das Bildtool sie unterstuetzt:

```text
no brand logo, no trademark, no celebrity, no movie character, no sports team logo, no disney style, no nike style, no football club, no game character, no copyrighted character, no blurry text, no misspelled text, no watermark, no mockup, no shirt photo
```

## Prompt fuer Design-Review

```text
Pruefe dieses T-Shirt-Design vor der Veroeffentlichung.

Bewerte:
1. Lesbarkeit
2. Rechtsrisiko
3. moegliche Marken-/Copyright-Anspielungen
4. Druckbarkeit
5. Zielgruppen-Fit
6. Etsy-Hauptbild-Tauglichkeit
7. Verbesserungen

Spruch: [SPRUCH]
Nische: [NISCHE]
Zielgruppe: [ZIELGRUPPE]
Bildbeschreibung oder Datei: [BESCHREIBUNG]

Gib ein Ergebnis:
- PASS
- PASS MIT AENDERUNGEN
- FAIL
```

