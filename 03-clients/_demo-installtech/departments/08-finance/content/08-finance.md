| Client | Afdeling | Status | Laatst gereviewd |
|---|---|---|---|
| InstallTech BV | Financiën & administratie | approved | 2026-06-26 |

Vier personen administratie/finance, boekhouding in Exact Online met een externe accountant op kwartaalritme. De betaalprocessen en het wettelijke luik lopen degelijk; het grote lek is de facturatieketen die stroomopwaarts op papieren werkbonnen wacht — een werkkapitaalprobleem eerder dan een papierprobleem. AS-IS gevalideerd met administratie en zaakvoerder tijdens de walkthrough van 2026-06-26.

## FIN.010 — Verkoopfacturatie
- **Huidige werkwijze:** Administratie verzamelt papieren werkbonnen en WhatsApp-foto's per werf, ontcijfert het handschrift, zoekt materiaalprijzen op en typt alles in Exact. Gemiddeld drie weken tussen einde werken en factuur (tot een maand voor grote werven); sinds januari vertrekt alles via Peppol en dat deel loopt vanzelf.
- **Wie:** administratie 1
- **Systemen:** papieren werkbonnen, WhatsApp, Exact Online, Peppol
- **Volume & tijd:** ±190 verkoopfacturen/maand, ±12 min hertypen per factuur; 3 weken gemiddelde vertraging
- **Pijn:** PAIN-9
- **Severity:** critical
- **Automability:** automation

## FIN.020 — Aankoopfacturen verwerken
- **Huidige werkwijze:** Alle leveranciersfacturen (groothandels, leasing, telefonie) worden één voor één manueel in Exact ingetikt — twee volle dagen op het einde van elke maand. Goedkeuring verloopt mondeling: zonder de krul van de zaakvoerder wordt niet betaald.
- **Wie:** administratie 1, zaakvoerder (goedkeuring)
- **Systemen:** Exact Online, papier/PDF-facturen per mail
- **Volume & tijd:** ±120 aankoopfacturen/maand × ±8 min
- **Pijn:** PAIN-10
- **Severity:** major
- **Automability:** automation

## FIN.030 — Betalingen en bankafstemming
- **Huidige werkwijze:** Wekelijkse betaalrun in de bankapp met de zaakvoerder ernaast; alles wordt met de kaartlezer afgetekend — het vieroogprincipe wordt nooit losgelaten en blijft ook in elke toekomstige oplossing behouden. Afpunten van de uittreksels gebeurt maandags, ±1 u.
- **Wie:** administratie 1 (voorbereiding), zaakvoerder (goedkeuring)
- **Systemen:** bankapp (Isabel-achtig), Exact Online
- **Volume & tijd:** 1 betaalrun/week; ±1 u afpunten per week
- **Severity:** minor
- **Automability:** automation

## FIN.040 — Debiteurenopvolging en aanmaningen
- **Huidige werkwijze:** Aanmanen gebeurt op afroep, wanneer de zaakvoerder vraagt hoeveel er openstaat; dan worden de openstaande posten uit Exact getrokken en volgt een bel- en mailronde. Er is geen ouderdomsoverzicht; ±een kwart van de facturen gaat over de vervaldag. Veel debiteuren zijn twintigjarige relaties, wat de toon delicaat maakt.
- **Wie:** administratie 2, zaakvoerder (delicate gevallen)
- **Systemen:** Exact Online (openstaande posten), telefoon, mail
- **Volume & tijd:** ±25% van 190 facturen/maand over vervaldag; belrondes ad hoc
- **Pijn:** PAIN-11
- **Severity:** major
- **Automability:** hybrid

## FIN.060 — Btw-aangifte en wettelijke verplichtingen
- **Huidige werkwijze:** De externe accountant dient per kwartaal de btw-aangifte en de overige verplichtingen in vanuit Exact; sinds de Peppol-omschakeling van januari 2026 vraagt hij beduidend minder stukken op. Dit proces loopt naar ieders tevredenheid.
- **Wie:** externe accountant, administratie 1 (aanlevering)
- **Systemen:** Exact Online, portaal accountant, Peppol
- **Volume & tijd:** kwartaalritme; aanlevering ±0,5 dag per kwartaal
- **Severity:** none
- **Automability:** human

## FIN.080 — Kostenopvolging en nacalculatie
- **Huidige werkwijze:** Nacalculatie gebeurt alleen voor werven die "echt pijn gedaan hebben" — twee à drie per jaar. De inputs zijn bovendien onbetrouwbaar: uren op de bonnen zijn geschat en klein materiaal ontbreekt, dus marge per werf of per klant is in feite onbekend.
- **Wie:** zaakvoerder + administratie 1, ad hoc
- **Systemen:** Excel (handmatige samenraapsels), Exact Online
- **Volume & tijd:** 2–3 nacalculaties/jaar op ±240 werven
- **Pijn:** PAIN-12
- **Severity:** major
- **Automability:** automation

## FIN.090 — Cashflowprognose
- **Huidige werkwijze:** Het banksaldo plus het buikgevoel van de zaakvoerder; eind december werd het spannend door voorafbetalingen en twee grote werven die pas in januari gefactureerd geraakten. Er is geen rollend overzicht van in- en uitgaande kasstromen; de zaakvoerder legt de prioriteit zelf bij snellere facturatie.
- **Wie:** zaakvoerder
- **Systemen:** bankapp, hoofdrekenen
- **Volume & tijd:** ad hoc, geen vast ritme
- **Severity:** minor
- **Automability:** human
