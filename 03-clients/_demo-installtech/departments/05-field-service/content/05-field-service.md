| Client | Afdeling | Status | Laatst gereviewd | Goedgekeurd door | Datum |
|---|---|---|---|---|---|
| InstallTech BV | Buitendienst & uitvoering | approved | 2026-06-24 | zaakvoerder + planner (walkthrough) | 2026-06-24 |

Achttien techniekers, één ervaren planner en een papieren werkbonnenstroom. De uitvoering zelf is vakwerk en loopt goed; de waardevernietiging zit in alles errond: de papieren registratie, de ontbrekende installatiehistoriek en de contractopvolging in een verouderde Excel. AS-IS gevalideerd met planner, technieker en zaakvoerder tijdens de walkthrough van 2026-06-24.

## Gate

**Directieven**

- [x] avondwerk werkbonnen (±15 min/bon) expliciet gekwantificeerd in SVC.050 (toegepast 2026-06-24)
- [x] gemiste onderhoudsbeurten (±10/jaar) toegevoegd aan SVC.070 (toegepast 2026-06-23)

## SVC.010 — Intake en triage van servicemeldingen
- **Huidige werkwijze:** Meldingen komen binnen via telefoon naar het onthaal en de mailbox service@; wie opneemt schat de urgentie in. Gevolg: soms een rit voor iets dat kon wachten, terwijl een echt dringend geval tot de middag in de mailbox blijft hangen.
- **Wie:** onthaal/binnendienst, planner (escalatie)
- **Systemen:** telefoon, Outlook (service@)
- **Volume & tijd:** ±40 meldingen/dag in het seizoen; triage op gevoel, niet geregistreerd
- **Severity:** minor
- **Automability:** agent

## SVC.020 — Dispatching en routeplanning
- **Huidige werkwijze:** De planner plant de 18 techniekers op het planbord in de gang en in de gedeelde Outlook-agenda, op basis van jarenlange kennis van skills, zones en klanten. Dit werkt goed maar hangt volledig aan één persoon: bij haar afwezigheid "staat de gsm roodgloeiend".
- **Wie:** planner-dispatcher (1 pers.), backup beperkt
- **Systemen:** fysiek planbord, gedeelde Outlook-agenda
- **Volume & tijd:** dagplanning voor 18 techniekers, ±85 opdrachten/week; dagelijks 1–2 u herschikken
- **Severity:** minor
- **Automability:** human

## SVC.030 — Werkvoorbereiding voor interventies
- **Huidige werkwijze:** Techniekers vertrekken zonder gebundelde historiek: welke ketel er hangt en wat er vorige keer gebeurd is, zit in servermappen en in hoofden. Ze bellen 5–10 keer per dag naar het bureau; af en toe volgt een tweede rit omdat het juiste stuk niet in de camionette lag.
- **Wie:** technieker (vraagt), planner en binnendienst (zoeken op)
- **Systemen:** servermappen per klant, telefoon
- **Volume & tijd:** 5–10 opzoektelefoons/dag; enkele vermijdbare tweede bezoeken/maand
- **Pijn:** PAIN-6
- **Severity:** major
- **Automability:** agent

## SVC.050 — Werkbon en materiaalregistratie
- **Huidige werkwijze:** Papieren drieluikbon, ingevuld en afgetekend op de werf — in het beste geval; vaak pas dagen later van thuis uit, met foto's in de WhatsApp-groep richting administratie, die alles ontcijfert en overtypt. Klein materiaal wordt structureel vergeten en dus nooit aangerekend.
- **Wie:** 18 techniekers (invullen), administratie (overtypen)
- **Systemen:** papieren drieluik, WhatsApp-groep, Excel/Exact (overtypen)
- **Volume & tijd:** ±85 werkbonnen/week; ±15 min avondwerk per bon plus overtypen op kantoor
- **Pijn:** PAIN-5
- **Severity:** critical
- **Automability:** agent

## SVC.060 — Vervolgwerk en tweede bezoeken
- **Huidige werkwijze:** "Ik kom daar nog eens terug voor dat ventiel" leeft in het hoofd van de technieker en nergens anders; als de klant niet zelf belt, komt er van het vervolgwerk niets. Offertes voor vastgesteld meerwerk worden zelden gemaakt.
- **Wie:** technieker (constateert), niemand (capteert)
- **Systemen:** geen — geheugen en losse opmerkingen op de werkbon
- **Volume & tijd:** ±3–4 verloren vervolgwerken/maand, telkens een gemiste offerte
- **Pijn:** PAIN-7
- **Severity:** major
- **Automability:** hybrid

## SVC.070 — Onderhoudscontracten en periodieke bezoeken
- **Huidige werkwijze:** 220 onderhoudscontracten worden opgevolgd in een Excel uit 2019; de planning van de najaarsbeurten gebeurt manueel vanaf die lijst. Vorig jaar zijn zeker tien beurten niet uitgevoerd; van de installatiebasis van de laatste tien jaar heeft ruwweg de helft geen contract.
- **Wie:** planner (planning), zaakvoerder (contracten)
- **Systemen:** Excel (versie 2019), planbord
- **Volume & tijd:** 220 contracten, piek sept–dec; ±10 gemiste beurten/jaar
- **Pijn:** PAIN-8
- **Severity:** major
- **Automability:** automation

## SVC.090 — Tijdsregistratie techniekers
- **Huidige werkwijze:** Uren worden op de papieren werkbon geschreven en op vrijdag door de technieker gereconstrueerd voor het sociaal secretariaat; verplaatsings- en werktijd lopen door elkaar. De loonverwerking en elke poging tot nacalculatie erven die ruis.
- **Wie:** techniekers (schrijven), administratie 2 (verwerkt richting sociaal secretariaat)
- **Systemen:** papieren werkbon, Excel-urenstaat
- **Volume & tijd:** 18 techniekers × wekelijkse reconstructie; foutmarge onbekend maar erkend (§12)
- **Pijn:** PAIN-5
- **Severity:** major
- **Automability:** agent
