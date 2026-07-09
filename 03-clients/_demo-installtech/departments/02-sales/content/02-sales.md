| Client | Afdeling | Status | Laatst gereviewd | Goedgekeurd door | Datum |
|---|---|---|---|---|---|
| InstallTech BV | Verkoop & offertes | approved | 2026-06-20 | zaakvoerder + consultant (walkthrough) | 2026-06-20 |

De verkoop draait op een gedeelde mailbox, een Excel-sjabloon en de ervaring van de zaakvoerder en twee verkopers. Het kernproces — van aanvraag tot getekende offerte — is stabiel maar traag: het hertypen en de doorlooptijd van vier à vijf werkdagen zijn de grootste lekken. AS-IS gevalideerd met zaakvoerder en binnendienst tijdens de walkthrough van 2026-06-20.

## Gate

**Directieven**

- [x] doorlooptijd offerte (4–5 werkdagen) toegevoegd aan SAL.030 (toegepast 2026-06-20)
- [x] WhatsApp als leadkanaal van de techniekers opgenomen bij SAL.010 (toegepast 2026-06-18)

## SAL.010 — Leadontvangst en kwalificatie
- **Huidige werkwijze:** Aanvragen komen binnen via de gedeelde mailbox verkoop@, telefonisch (genoteerd op post-its) en via klanten die een technieker op de werf aanspreken; dat laatste kanaal geraakt soms pas een week later bij de binnendienst. Er bestaat geen leadlijst, dus verloren aanvragen blijven onzichtbaar.
- **Wie:** binnendienst (2 pers.), sporadisch de techniekers als doorgeefluik
- **Systemen:** Outlook (verkoop@), post-its, WhatsApp
- **Volume & tijd:** ±60 aanvragen/maand (schatting — geen registratie), kwalificatie ad hoc
- **Severity:** minor
- **Automability:** automation

## SAL.020 — Plaatsbezoek en behoefteanalyse
- **Huidige werkwijze:** Voor alles boven een ketelvervanging gaat de zaakvoerder of één van de twee verkopers ter plaatse; notities in een papieren boekje, foto's op de eigen gsm. Een deel van de mondelinge afspraken bereikt de offerte nooit, waarna de binnendienst de klant moet terugbellen.
- **Wie:** zaakvoerder + 2 verkopers (bezoek), binnendienst (verwerking)
- **Systemen:** papieren boekje, gsm-foto's, geen gestructureerd bezoekverslag
- **Volume & tijd:** ±25 werfbezoeken/maand; ±20 min herwerk per dossier door ontbrekende info
- **Pijn:** PAIN-2
- **Severity:** major
- **Automability:** hybrid

## SAL.030 — Offerte opstellen
- **Huidige werkwijze:** Binnendienst hertypt de aanvraagmail en de werfnotities in een Excel-sjabloon en zoekt de actuele groothandelsprijzen manueel op omdat het sjabloon veroudert. Tussen werfbezoek en verstuurde offerte zit gemiddeld 4–5 werkdagen; minstens twee dossiers per maand gaan aantoonbaar verloren aan snellere concurrenten.
- **Wie:** binnendienst 1 (opmaak), verkoper (input), zaakvoerder (grote dossiers)
- **Systemen:** Outlook, Excel-sjabloon, prijslijsten groothandel (PDF)
- **Volume & tijd:** ±45 offertes/maand, ±50 min per offerte
- **Pijn:** PAIN-1, PAIN-2
- **Severity:** critical
- **Automability:** agent

## SAL.040 — Prijszetting en offertegoedkeuring
- **Huidige werkwijze:** Alles boven €10.000 passeert bij de zaakvoerder, die 's avonds nakijkt en de dag erna laat vertrekken. Dit werkt naar ieders tevredenheid en de zaakvoerder wil de grote dossiers expliciet blijven zien — bewust te vrijwaren in de roadmap.
- **Wie:** zaakvoerder (goedkeuring), binnendienst (voorbereiding)
- **Systemen:** Excel, mail
- **Volume & tijd:** ±10 offertes/maand boven de drempel, doorlooptijd goedkeuring <1 dag
- **Severity:** none
- **Automability:** human

## SAL.050 — Offerteopvolging
- **Huidige werkwijze:** Opvolging gebeurt "als het stil is", en het is nooit stil: op elk moment staan ±30 offertes open zonder dat iemand ernaar omkijkt. Er is geen statusoverzicht — de laatste versie moet per klant in submappen op de server gezocht worden.
- **Wie:** binnendienst 2, ad hoc
- **Systemen:** mappenstructuur op de server ("Offertes 2026"), Outlook
- **Volume & tijd:** ±30 open offertes op elk moment; opvolging onregelmatig en niet geregistreerd
- **Pijn:** PAIN-3
- **Severity:** major
- **Automability:** automation

## SAL.060 — Orderbevestiging en overdracht naar uitvoering
- **Huidige werkwijze:** Bij akkoord stuurt de binnendienst de offerte per mail door naar de planning; afspraken die alleen in de mailthread staan (toegang, gehuurd materieel, beloofde data) gaan geregeld verloren. Vorige maand stond een ploeg op de werf zonder de beloofde hoogtewerker.
- **Wie:** binnendienst (doorsturen), planning (interpretatie)
- **Systemen:** Outlook (forward), planbord
- **Volume & tijd:** ±20 orders/maand; 1–2 overdrachtincidenten/maand
- **Pijn:** PAIN-4
- **Severity:** major
- **Automability:** automation

## SAL.080 — CRM-gegevensbeheer
- **Huidige werkwijze:** Er is geen CRM; de klantenlijst is een half bijgehouden Excel. Adressen kloppen meestal, maar de installatie- en contacthistoriek zit verspreid over mailboxen en het geheugen van de zaakvoerder.
- **Wie:** binnendienst, zaakvoerder
- **Systemen:** Excel-klantenlijst, Outlook-mailboxen
- **Volume & tijd:** ±1.800 klantrecords; bijwerking sporadisch
- **Severity:** minor
- **Automability:** automation
