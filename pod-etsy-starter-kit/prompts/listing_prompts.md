# Etsy-Listing-Prompts

Diese Prompts erzeugen SEO-Titel, Tags und Beschreibungen fuer deutsche Etsy-Listings. Sie ersetzen keine Rechtspruefung.

## Master-Prompt fuer Listing-Daten

```text
Du bist ein deutscher Etsy-SEO-Spezialist fuer Print-on-Demand-Shirts.

Erstelle Listing-Daten fuer:
Produkt: [PRODUKT]
Spruch: [SPRUCH]
Nische: [NISCHE]
Subnische: [SUBNISCHE]
Zielgruppe: [ZIELGRUPPE]
Anlass: [ANLASS]
Hauptkeyword: [HAUPTKEYWORD]
Nebenkeywords: [NEBENKEYWORDS]

Regeln:
- Deutsche Zielgruppe
- Kein Keyword-Stuffing
- Keine Marken, Logos, Promis, Film-/Serien-/Game-Namen, Fussballvereine
- Titel natuerlich lesbar
- Etsy-Tags: exakt 13 Tags, jeder Tag maximal 20 Zeichen wenn moeglich
- Beschreibung ehrlich: POD, Produktion nach Bestellung, Material-/Pflegehinweise neutral halten
- Keine falschen Lieferzeitversprechen

Gib aus:
1. SEO-Titel
2. 13 Etsy-Tags als kommagetrennte Liste
3. Kurzbeschreibung
4. Lange Beschreibung
5. Alt-Text fuer Hauptbild
6. Zielgruppen-Notiz
7. Risiko-Hinweis
```

## Titel-Formeln

```text
[Hauptkeyword] [Spruch], [Zielgruppe] Geschenk, [Anlass], [Produkt]
```

```text
[Spruch] [Produkt], Geschenk fuer [Zielgruppe], [Nische] Shirt
```

```text
[Nische] Shirt [Spruch], lustiges [Produkt] fuer [Anlass]
```

## Beschreibungsvorlage

```text
[KURZER EINSTIEG]

Dieses Shirt ist eine schoene Geschenkidee fuer [ZIELGRUPPE] und passt besonders gut zu [ANLASS]. Das Design ist schlicht, gut lesbar und fuer den Alltag gemacht.

Details:
- Print-on-Demand Produkt
- Produktion erst nach Bestellung
- Verschiedene Groessen und Farben je nach Verfuegbarkeit
- Angenehm fuer Alltag, Geschenk, Geburtstag oder besondere Anlaesse

Pflege:
- Auf links waschen
- Nicht direkt ueber den Druck buegeln
- Niedrige Temperatur empfohlen
- Nicht bleichen

Hinweis:
Farben koennen je nach Bildschirm leicht abweichen. Bitte pruefe vor der Bestellung die Groessentabelle und Produktvarianten.
```

## Prompt fuer Tag-Varianten

```text
Erstelle 3 verschiedene Etsy-Tag-Sets fuer folgendes Listing:

Spruch: [SPRUCH]
Nische: [NISCHE]
Hauptkeyword: [HAUPTKEYWORD]
Zielgruppe: [ZIELGRUPPE]
Anlass: [ANLASS]

Set A: stark keyword-orientiert
Set B: stark geschenkorientiert
Set C: stark zielgruppenorientiert

Regeln:
- Je Set exakt 13 Tags
- Keine Marken oder geschuetzten Begriffe
- Deutsch bevorzugt, englische Begriffe nur wenn auf Etsy ueblich
```

## Prompt fuer Listing-Review

```text
Pruefe dieses Etsy-Listing kritisch:

Titel: [TITEL]
Tags: [TAGS]
Beschreibung: [BESCHREIBUNG]
Design-Spruch: [SPRUCH]
Nische: [NISCHE]

Bewerte:
1. SEO-Klarheit
2. Keyword-Stuffing
3. rechtliche Risiken
4. Kundenverstaendlichkeit
5. Conversion-Staerke
6. fehlende Informationen

Gib konkrete Verbesserungen und eine PASS/FAIL-Entscheidung.
```

## Beispiel-Ausgabe

```text
SEO-Titel:
Hundemama Shirt Gassi ist mein Cardio, Geschenk fuer Hundebesitzerin, lustiges Hunde T-Shirt

Tags:
hundemama,hundeliebe,gassi shirt,hunde geschenk,shirt frau,lustiges shirt,hundebesitzer,pfoten shirt,geschenk frau,hunde mama,t shirt hund,haustier shirt,cardio shirt

Kurzbeschreibung:
Lustiges Shirt fuer Hundemamas und Hundebesitzerinnen. Perfekt als Geschenk zum Geburtstag oder fuer den Alltag.

Alt-Text:
T-Shirt Design mit deutschem Spruch Gassi ist mein Cardio und kleinen Pfoten-Elementen fuer Hundebesitzer.
```

