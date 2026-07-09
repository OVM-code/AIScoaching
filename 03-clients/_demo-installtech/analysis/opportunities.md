# Opportunity register — InstallTech BV

| Client | Status | Laatst gereviewd |
|---|---|---|
| InstallTech BV | draft | 2026-07-09 |

Gegenereerd uit de goedgekeurde pijnpunten (AS-IS approved 2026-06-20/24/26),
de F2-waardepools en de opportunitypatronen uit de catalogus. Scoring per F3
(standaardgewichten: `Value = 0.50*hours + 0.25*quality + 0.25*strategic`,
`Feasibility = 0.40*data + 0.30*technical + 0.30*ownership`, high ≥ 3.5),
allocatie per F4. Alle €-formules op jaarbasis, gedreven door
`assumptions.json`. Eerlijke-ROI-regel: zelfgerapporteerde besparingen tellen
2–3× te hoog — de defaults zijn daarom conservatief gezet en elk cijfer is
richtinggevend tot de pilotmeting. Discards blijven staan, ze worden nooit
verwijderd.

## OPP-1 — Werkbonnen digitaliseren met een 60-seconden-spraaknotitie van de technieker
- **Status:** proposed
- **Afdelingen:** SVC
- **Processen:** SVC.050, SVC.090
- **Pijnpunten:** PAIN-5
- **Allocatie:** agent-T1
- **Value-scores:** hours=5, quality=4, strategic=4
- **Feasibility-scores:** data=4, technical=4, ownership=4
- **Adoptie:** 4
- **Effort:** M
- **Wave:** 1
- **Tooling €/maand:** 200
- **Waardeformule:** jobs_per_week * 46 * 15 / 60 * loaded_hourly_cost
- **Aannames:** jobs_per_week, loaded_hourly_cost
- **Verdict:** quick-win — confidence: high
- **Wat dit zou veranderen:** als de spraakherkenning op werf-Vlaams en vakjargon onder de ±90% bruikbaarheid blijft in de pilot, of de invoertijd per bon boven de 2 minuten uitkomt, zakt adoptie en schuift dit naar een app-met-velden-variant in wave 2.
- **Enablers:** gestructureerd werkbonsjabloon (velden: werk, materiaal, uren, vervolgwerk-vlag); digitale handtekening op de gsm; starten met de meest gemotiveerde technieker (transcript §21), nooit met de scepticus
- **Risico / AI Act:** beperkt risico; technieker keurt elke gegenereerde bon na (T1). Urenregistratie raakt aan monitoringgevoeligheid — vooraf kaderen als facturatienauwkeurigheid, team betrekken (F4 §6)
- **Eerste stap:** 2 weken pilot met 2 techniekers; parallel 20 papieren bonnen naspellen om het niet-aangerekende klein materiaal te becijferen

## OPP-2 — Offertes genereren uit aanvraagmail en werfnotities met een LLM-assistent
- **Status:** proposed
- **Afdelingen:** SAL
- **Processen:** SAL.030, SAL.020
- **Pijnpunten:** PAIN-1, PAIN-2
- **Allocatie:** agent-T1
- **Value-scores:** hours=4, quality=3, strategic=5
- **Feasibility-scores:** data=4, technical=4, ownership=3
- **Adoptie:** 4
- **Effort:** M
- **Wave:** 1
- **Tooling €/maand:** 150
- **Waardeformule:** quotes_per_month * 12 * minutes_saved_per_quote / 60 * loaded_hourly_cost
- **Aannames:** quotes_per_month, minutes_saved_per_quote, loaded_hourly_cost
- **Verdict:** quick-win — confidence: high
- **Wat dit zou veranderen:** als minder dan 60% van de aanvragen bruikbaar gestructureerd blijkt (catalogus-caveat SAL.030), zakt data-feasibility naar 2 en schuift dit naar wave 2 achter een intake-opschoning. De échte prijs is de doorlooptijd (4–5 dagen → ≤2): als de winratio niet meetbaar stijgt, is het uurcijfer alleen te mager.
- **Enablers:** offerte-sjabloon en prijsboek standaardiseren (de "prijzen kloppen nooit"-klacht eerst oplossen); werfnotities digitaal capteren (spraaknotitie verkoper, zelfde patroon als OPP-1)
- **Risico / AI Act:** beperkt risico; binnendienst en zaakvoerder reviewen elke offerte (T1) — prijszetting en eindgoedkeuring blijven menselijk per F4
- **Eerste stap:** 2 weken schaduwdraaien op de laatste 20 offertes; meten: minuten per offerte en doorlooptijd werfbezoek → verstuurd

## OPP-3 — Verkoopfacturen dezelfde dag opmaken vanuit de digitale werkbon
- **Status:** proposed
- **Afdelingen:** FIN
- **Processen:** FIN.010
- **Pijnpunten:** PAIN-9
- **Allocatie:** automation
- **Value-scores:** hours=4, quality=4, strategic=4
- **Feasibility-scores:** data=3, technical=4, ownership=4
- **Adoptie:** 5
- **Effort:** M
- **Wave:** 1
- **Tooling €/maand:** 100
- **Waardeformule:** invoices_per_month * 12 * minutes_per_invoice / 60 * loaded_hourly_cost
- **Aannames:** invoices_per_month, minutes_per_invoice, loaded_hourly_cost
- **Verdict:** quick-win — confidence: medium
- **Wat dit zou veranderen:** dit staat of valt met OPP-1 — zonder digitale werkbon is er niets om automatisch te factureren (data=3 is al een voorschot op die afhankelijkheid). De business case wordt gewonnen op werkkapitaal, niet op uren: als de DSO-meting voor/na geen ±2 weken verbetering toont, is de formule hierboven de ondergrens, niet het verhaal.
- **Enablers:** OPP-1 live bij minstens de helft van de ploeg; conceptfactuur-flow in Exact activeren (administratie keurt elke factuur goed vóór Peppol-verzending)
- **Risico / AI Act:** minimaal risico — regelgebaseerde automatisering; factuur vertrekt nooit zonder menselijke vrijgave
- **Eerste stap:** DSO-nulmeting uit Exact (laatste 6 maanden); daarna conceptfacturen genereren voor één week interventies en de correctiegraad meten

## OPP-4 — Betaalherinneringen versturen via een getrapte sequentie met menselijke overname
- **Status:** proposed
- **Afdelingen:** FIN
- **Processen:** FIN.040
- **Pijnpunten:** PAIN-11
- **Allocatie:** hybrid
- **Value-scores:** hours=3, quality=4, strategic=4
- **Feasibility-scores:** data=4, technical=5, ownership=4
- **Adoptie:** 4
- **Effort:** S
- **Wave:** 1
- **Tooling €/maand:** 50
- **Waardeformule:** invoices_per_month * 12 * 0.25 * 10 / 60 * loaded_hourly_cost
- **Aannames:** invoices_per_month, loaded_hourly_cost
- **Verdict:** quick-win — confidence: high
- **Wat dit zou veranderen:** de formule telt alleen de vermeden belrondes (±25% van de facturen, ±10 min); de grotere winst — kortere betaaltermijn — is bewust niet becijferd tot de ouderdomsanalyse er is. Als één geautomatiseerde aanmaning bij een twintigjarige relatie verkeerd valt, gaat de uitzonderingslijst vóór alles (catalogus-caveat FIN.040).
- **Enablers:** ouderdomsrapport uit Exact als wekelijkse trigger; uitzonderingslijst relatiegevoelige klanten (zaakvoerder beslist wie); toonladder in de woorden van de zaakvoerder (agent-T1 ontwerpt de drie brieven éénmalig)
- **Risico / AI Act:** beperkt risico; stap 1–2 automatisch, stap 3 en alle gevoelige accounts altijd menselijk
- **Eerste stap:** ouderdomsanalyse uit Exact; uitzonderingslijst opstellen met de zaakvoerder; sequentie 4 weken draaien op de niet-gevoelige helft

## OPP-5 — Onderhoudscontracten aanbieden via een reminder-engine over de installatiebasis
- **Status:** proposed
- **Afdelingen:** SVC
- **Processen:** SVC.070
- **Pijnpunten:** PAIN-8
- **Allocatie:** automation
- **Value-scores:** hours=3, quality=3, strategic=5
- **Feasibility-scores:** data=2, technical=4, ownership=3
- **Adoptie:** 3
- **Effort:** L
- **Wave:** 2
- **Tooling €/maand:** 75
- **Waardeformule:** 480 * 0.08 * 340
- **Cijferbasis:** geen slider — telling installatiebasis (±480 installaties zonder contract, schatting §17) × 8% conversie × €340 gemiddelde jaarmarge per contract; alle drie te valideren vóór wave 2 start
- **Verdict:** big-bet — confidence: medium
- **Wat dit zou veranderen:** dit is een groeicase, geen efficiëntiecase (catalogus: score als growth). Als de telling van de installatiebasis onder de ±300 contractloze installaties uitkomt, of de proefmailing onder 4% conversie blijft, halveert de case en wordt het een fill-in. De datafeasibility (2) is het echte werk: de installatiebasis bestaat vandaag alleen als servermappen.
- **Enablers:** installatiebasis reconstrueren uit servermappen + Exact-facturatiehistoriek (het enabler-project); contract-Excel van 2019 vervangen door één onderhouden lijst; gemiste beurten eerst naar nul (contractuele plicht)
- **Risico / AI Act:** minimaal risico — reminder-automatisering; commerciële voorstellen vertrekken pas na menselijke check
- **Eerste stap:** installatiebasis van de laatste 10 jaar tellen (steekproef 3 jaargangen); proefmailing naar 50 contractloze klanten in het najaar

## OPP-6 — Vervolgwerk capteren via werkbon-vlaggen en automatisch offertes klaarzetten
- **Status:** proposed
- **Afdelingen:** SVC, SAL
- **Processen:** SVC.060, SAL.030
- **Pijnpunten:** PAIN-7
- **Allocatie:** hybrid
- **Value-scores:** hours=3, quality=3, strategic=5
- **Feasibility-scores:** data=2, technical=3, ownership=3
- **Adoptie:** 3
- **Effort:** M
- **Wave:** 3
- **Tooling €/maand:** 50
- **Waardeformule:** jobs_per_week * 46 * 0.03 * 250
- **Aannames:** jobs_per_week
- **Cijferbasis:** 3% van de bonnen draagt een vervolgwerk-vlag die vandaag verdampt (±3–4/maand, transcript §13) × €250 gemiddelde marge per gerecupereerde opdracht — beide te staven met de kwartaaltelling
- **Verdict:** big-bet — confidence: low
- **Wat dit zou veranderen:** volledig stroomafwaarts van OPP-1: zonder vervolgwerk-vlag op een digitale bon bestaat de dataketen niet (data=2). Catalogus-caveat SVC.060: eerst het lek meten — als de telling van "kom ik nog eens terug"-vermeldingen vorig kwartaal onder de 5 uitkomt, is dit een fill-in of een discard.
- **Enablers:** vervolgwerk-vlag als verplicht veld in het werkbonsjabloon (OPP-1); wekelijkse takenlijst bij binnendienst 2 (routing); conceptofferte via het OPP-2-patroon
- **Risico / AI Act:** beperkt risico; elke conceptofferte langs de normale menselijke offerteflow (T1)
- **Eerste stap:** telling over het voorbije kwartaal: vermeldingen van vervolgwerk op bonnen/in WhatsApp vs. effectief verstuurde offertes — het cijfer verkoopt (of begraaft) de case

## OPP-7 — Nacalculatie per werf opbouwen met automatische marge-signalering
- **Status:** proposed
- **Afdelingen:** FIN
- **Processen:** FIN.080
- **Pijnpunten:** PAIN-12
- **Allocatie:** agent-T2
- **Value-scores:** hours=3, quality=4, strategic=5
- **Feasibility-scores:** data=1, technical=3, ownership=3
- **Adoptie:** 3
- **Effort:** L
- **Wave:** 3
- **Tooling €/maand:** 100
- **Waardeformule:** jobs_per_week * 46 * 0.02 * 260
- **Aannames:** jobs_per_week
- **Cijferbasis:** hypothese dat ±2% van de opdrachten verlieslatend is en gemiddeld €260 recupereerbaar per gedetecteerd geval (prijszetting of scope bijsturen) — pure hypothese tot de eerste kwartaalroll-up
- **Verdict:** big-bet — confidence: low
- **Wat dit zou veranderen:** data=1 is de F1-bindende beperking in het klein: uren zijn geschat en klein materiaal ontbreekt (transcript §15), dus vandaag automatiseert dit alleen gissingen (catalogus-caveat FIN.080). Pas zinvol na twee kwartalen betrouwbare digitale registratie (OPP-1 + OPP-3). Blijkt de eerste betrouwbare roll-up dat marges overal gezond zijn, dan is dit een rapport, geen agent — en zakt het naar fill-in.
- **Enablers:** OPP-1 (uren + materiaal digitaal) en OPP-3 (facturatie gekoppeld) twee kwartalen live; werfcodes consequent in Exact
- **Risico / AI Act:** beperkt risico; agent-T2 stelt maandcommentaar en uitschieters voor, controller/zaakvoerder interpreteert — geen automatische beslissingen
- **Eerste stap:** niets bouwen; na kwartaal 1 van OPP-1 een handmatige nacalculatie van 10 werven doen als datakwaliteitstest

## OPP-8 — Aankoopfacturen inlezen met documentherkenning in de boekhouding
- **Status:** proposed
- **Afdelingen:** FIN
- **Processen:** FIN.020
- **Pijnpunten:** PAIN-10
- **Allocatie:** automation
- **Value-scores:** hours=3, quality=4, strategic=2
- **Feasibility-scores:** data=4, technical=5, ownership=4
- **Adoptie:** 5
- **Effort:** S
- **Wave:** 2
- **Tooling €/maand:** 60
- **Waardeformule:** 120 * 12 * 6 / 60 * loaded_hourly_cost
- **Aannames:** loaded_hourly_cost
- **Cijferbasis:** ±120 aankoopfacturen/maand (transcript §7) × ±6 van de ±8 min per factuur geautomatiseerd (conservatief)
- **Verdict:** fill-in — confidence: high
- **Wat dit zou veranderen:** catalogus-caveat FIN.020: dit is het vaakst al-half-opgeloste proces — als de scan-en-herken-module van het accountantsplatform/Exact dit out-of-the-box dekt, is het een activatie van een halve dag en geen project. Dan stijgt het rendement en blijft het een fill-in dat gewoon meteen mag.
- **Enablers:** check welke herkenningsmodule in het bestaande Exact-abonnement of bij de accountant zit (eerst activeren, dan pas kopen); goedkeuringsdrempels afspreken zodat de mondelinge krul een digitale wordt
- **Risico / AI Act:** minimaal risico; boekingsvoorstellen, administratie valideert — vier ogen op betalingen blijft onaangeroerd
- **Eerste stap:** demo van de bestaande Exact/accountant-module op de facturen van vorige maand; foutgraad meten op 50 stuks

## OPP-9 — Klanten verwittigen met automatische ETA-berichten bij elke interventie
- **Status:** proposed
- **Afdelingen:** SVC
- **Processen:** SVC.020, SVC.010
- **Pijnpunten:** PAIN-6
- **Allocatie:** automation
- **Value-scores:** hours=2, quality=4, strategic=3
- **Feasibility-scores:** data=4, technical=4, ownership=4
- **Adoptie:** 4
- **Effort:** S
- **Wave:** 2
- **Tooling €/maand:** 40
- **Waardeformule:** jobs_per_week * 46 * 0.15 * 4 / 60 * loaded_hourly_cost
- **Aannames:** jobs_per_week, loaded_hourly_cost
- **Cijferbasis:** hypothese: bij ±15% van de opdrachten belt de klant "waar blijft hij?" en kost dat ±4 min onthaaltijd — te toetsen met een streepjeslijst aan het onthaal
- **Verdict:** fill-in — confidence: medium
- **Wat dit zou veranderen:** klein in uren, groot in klantperceptie — bewust een fill-in naast de wave-2-enablerprojecten. Als de streepjesmeting onder de 5% "waar blijft hij"-oproepen uitkomt, vervalt de case; Rita blijft eigenaar van de planning, dit verstuurt alleen wat zij beslist (assist, niet replace — catalogus-caveat SVC.020).
- **Enablers:** planning digitaal genoeg (Outlook-agenda volstaat als bron); sms/WhatsApp Business-kanaal met opt-in conform GDPR
- **Risico / AI Act:** minimaal risico — berichtenautomatisering zonder besluitvorming; geen locatietracking van techniekers (rode lijn monitoring)
- **Eerste stap:** één week streepjes turven aan het onthaal ("waar blijft hij"-oproepen); daarna 2 weken proef met de service-ploeg

## OPP-10 — Dagplanning volledig automatiseren met een autonome dispatch-agent
- **Status:** discarded
- **Afdelingen:** SVC
- **Processen:** SVC.020
- **Pijnpunten:** PAIN-6
- **Allocatie:** agent-T3
- **Value-scores:** hours=3, quality=2, strategic=3
- **Feasibility-scores:** data=2, technical=2, ownership=2
- **Adoptie:** 2
- **Effort:** L
- **Wave:** -
- **Verdict:** discard — confidence: high
- **Wat dit zou veranderen:** de planning is vandaag een sterkte, geen pijn ("De planning van Rita, daar blijf je af" — intake; bevestigd in de workshop §22). Skills, zones en klantgevoeligheden zitten in Rita's hoofd, niet in data (data=2), en niemand wil eigenaar zijn van een autonome planner (ownership=2). Heropenen alléén als Rita's opvolging concreet wordt: dan eerst haar kennis vastleggen, en zelfs dan als assistent (T1), nooit autonoom.
- **Enablers:** n.v.t. — bewust niet starten; wel Rita's planningsregels documenteren als continuïteitsmaatregel (zit in keep.md als guardrail)
- **Risico / AI Act:** een autonome dispatch-agent stuurt de facto werkroosters — raakt aan arbeidsorganisatie en monitoringgevoeligheid; dat governancegewicht is voor deze organisatie disproportioneel (F4 §6, F6)
- **Eerste stap:** geen — gedocumenteerd zodat de vraag niet elk kwartaal terugkomt

## OPP-11 — Cashflowprognose genereren uit openstaande posten met een AI-model
- **Status:** proposed
- **Afdelingen:** FIN
- **Processen:** FIN.090
- **Pijnpunten:** PAIN-9, PAIN-11
- **Allocatie:** agent-T1
- **Value-scores:** hours=2, quality=3, strategic=3
- **Feasibility-scores:** data=2, technical=3, ownership=2
- **Adoptie:** 3
- **Effort:** M
- **Wave:** -
- **Verdict:** discard — confidence: medium
- **Wat dit zou veranderen:** de zaakvoerder benoemt het zelf (§18): eerst snellere facturatie, dan is de helft van het cashprobleem weg. Een prognose bovenop een lege orderpijplijn (SAL.090 out of scope) en late facturatie voorspelt vooral de eigen achterstand (catalogus-caveat FIN.090). Herbekijken zodra OPP-3 en OPP-4 twee kwartalen draaien en er wél een ouderdoms- en orderbeeld bestaat — dan als eenvoudig 13-wekenmodel (automation), niet als AI-project.
- **Enablers:** n.v.t. in deze fase — afhankelijkheden eerst (OPP-3, OPP-4, pijplijnzicht)
- **Risico / AI Act:** beperkt risico, maar een schijnzekere prognose is erger dan buikgevoel — richtinggevend labelen is hier geen formaliteit
- **Eerste stap:** niet starten; herevaluatie geagendeerd bij de kwartaalreview na wave 1

## OPP-12 — Offertes onder de drempel automatisch laten goedkeuren door een prijsmodel
- **Status:** proposed
- **Afdelingen:** SAL
- **Processen:** SAL.040
- **Pijnpunten:** PAIN-1
- **Allocatie:** agent-T2
- **Value-scores:** hours=2, quality=2, strategic=3
- **Feasibility-scores:** data=3, technical=3, ownership=1
- **Adoptie:** 2
- **Effort:** M
- **Wave:** -
- **Verdict:** discard — confidence: high
- **Wat dit zou veranderen:** SAL.040 is vandaag géén bottleneck: goedkeuring binnen de dag en de zaakvoerder wil de grote dossiers expliciet blijven zien (§13 — een uitgesproken rode lijn, ownership=1). De doorlooptijdwinst zit in de opmaak (OPP-2), niet in de goedkeuring. Zou pas heropend worden als het offertevolume verdubbelt én de goedkeuring aantoonbaar >1 dag vertraging veroorzaakt — en dan als marge-signalering naast de mens (T2), nooit als autogoedkeuring (accountability moment per F4).
- **Enablers:** n.v.t. — bewust niet starten
- **Risico / AI Act:** prijsbeslissingen met directe €-impact zonder menselijke controle zijn per F4 een accountability moment; bovendien haaks op de expliciete wens van de sponsor
- **Eerste stap:** niet starten; drempel en doorlooptijd goedkeuring jaarlijks even nameten bij de portfolioreview
