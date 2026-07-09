# Client context — InstallTech BV

Master context document for this engagement — the single source of truth that
personalizes every other asset. Generated from `intake/intake.md` via Prompt 0.1
(`02-phase-playbooks/phase-0-intake-discovery.md`); facts validated by the
sponsor on 2026-06-05. `[VERIFY]` items remain uncertain until confirmed —
never treated as fact. (This is the worked **demo** engagement: InstallTech BV
is fictional; every number below is illustrative.)

---

## 1. Snapshot

InstallTech BV, Aalst (Oost-Vlaanderen) — HVAC & sanitary installer founded
1998, owner-managed (second generation, since 2015). One site, Dutch-speaking
(`nl`). ±35 FTE: 4 binnendienst, 18 techniekers, 3 planning, 4 admin/finance,
remainder management & purchasing. Mix of residential renovation and small B2B
within ±45 km; split ±60/40 particulier/professioneel [VERIFY — owner's
estimate]. Revenue ±€7.5M, stable-to-slightly-growing [VERIFY — 2025 annual
accounts not yet filed]. Ambition: same volume with less friction, plus growth
in recurring maintenance revenue — not headcount growth.

## 2. Strategy

Top-3 priorities in the owner's words: (1) "offerte buiten binnen de twee
dagen", (2) "het papierwerk van de techniekers weg", (3) "de dienst na verkoop
laten groeien" (maintenance contracts). Trigger for the engagement: two jobs
demonstrably lost in May to faster competitors, plus a tense cash position in
December 2025. Success in 12 months: quote lead time ≤2 days, invoices out
within a week of work completed, zero missed contractual maintenance visits.

## 3. Organization

Flat structure: zaakvoerder (Dirk) → office-verantwoordelijke (binnendienst,
also project lead for this engagement), planner-dispatcher (Rita), aankoper,
administratie (4), 18 techniekers in loose teams (installatie vs. dienst na
verkoop). No works council, no union delegation. Culture: family-firm loyalty,
long tenures, healthy scepticism toward tools after a failed planning app in
2021. Opinion leaders: Rita and one senior technician.

## 4. Core processes

1. Aanvraag (mail/telefoon/werf) → 2. werfbezoek met papieren notities ⚠ →
3. offerte hertypen in Excel (±45/maand, ±50 min; 4–5 dagen doorlooptijd ⚠⚠) →
4. goedkeuring >€10k door zaakvoerder (werkt goed) → 5. opvolging "als het stil
is" ⚠ → 6. overdracht naar planning per doorgestuurde mail ⚠ → 7. uitvoering
(planbord; ±85 werkbonnen/week op papier ⚠⚠) → 8. facturatie: bonnen ontcijferen
en hertypen in Exact, ±3 weken na de werken ⚠⚠ → 9. aanmanen op afroep ⚠.
Department detail lives in `departments/NN-<dept>/`.

## 5. Systems & data

Office 365, Exact Online (+ external accountant, quarterly), bank app with card
reader, WhatsApp groups, physical planning board + shared Outlook calendar.
No CRM, no field-service tool; werkbonnen on paper (drieluik). Loved: the
Exact + Peppol invoicing rails (since Jan 2026). Hated: the Excel quote
template with stale prices. Knowledge lives in mailboxes, per-client server
folders and heads. Data trust: low for hours/materials, medium for financials.
No automations beyond bank/Peppol.

## 6. AI today

No official use. Shadow use: owner drafts difficult mails with a free ChatGPT
account; at least one binnendienst employee occasionally drafts quote texts
[VERIFY — pulse survey planned]. No past AI attempts. Sentiment:
curious-pragmatic (management), expected scepticism among techniekers around
anything resembling monitoring. Red lines: no customer data in free tools; no
"second phone administration" for the field; owner keeps approving big quotes.

## 7. People & change

Long-tenured technicians (avg >8 years), low turnover, younger binnendienst.
Change history: Exact migration 2019 fine; 2021 planning app failed on
click-burden — adoption lesson: capture must be near-zero-effort ("60 seconden
of het gebeurt niet"). The owner is the change program: his visible use of
wave-1 tools is the comms plan. Hard adoption constraint from the field
transcript: "het moet simpel zijn — geen twintig velden op een klein schermke."

## 8. Engagement

Sponsor & decision-maker: zaakvoerder. Project lead: office-verantwoordelijke.
Decision process: owner decides, informally consults Rita + senior technician.
Budget: fixed diagnostic package agreed; implementation per business case,
payback <6 months for wave 1. Timeline: June discovery + AS-IS approval before
bouwverlof; F3 roadmap workshop July 2026; no field pilots during the sept–dec
maintenance peak. NDA signed 2026-05-28. Day rate €950 (see
`engagement-config.json`).

## 9. Verbatims

- (zaakvoerder) "Wij verliezen werken omdat onze offerte er vijf dagen over doet."
- (zaakvoerder) "Mijn techniekers zijn goud waard, maar hun papierwerk is een ramp."
- (zaakvoerder) "De planning van Rita, daar blijf je af. Dat werkt."
- (zaakvoerder) "Ik wil geen systeem kopen en dan trekken. Het moet vanzelf gaan of het gaat niet."
- (binnendienst) "Elke offerte typ ik letterlijk over: eerst uit de mail van de klant, dan uit de werfnotities van de verkoper."
- (technieker) "Ik zit op vrijdagavond aan de keukentafel werkbonnen van maandag in te vullen."
- (administratie) "Nu ben ik een typiste van andermans handschrift."
- (administratie) "Aanmanen doe ik als Dirk vraagt hoeveel er openstaat."

## 10. Open questions

1. Exact quote count and win rate per month (server folder telling + Exact) — needed to calibrate `quotes_per_month` and the SAL.030 business case.
2. Real value of unbilled small material on werkbonnen — sample 20 bonnen in pilot week 1 (drives OPP-1 honest ROI).
3. Depth and spread of shadow AI use — anonymous pulse survey (Phase 1).
4. Customer split particulier/professioneel [VERIFY] — affects tone of dunning automation.
5. Installed-base size without maintenance contract — count from server folders; drives the SVC.070 growth case.
6. Bouwverlof 2026 exact dates — pilot scheduling.

## 11. Engagement status

- Phase: 2 (discovery done, AS-IS approved per department 2026-06-20/24/26; diagnosis in progress)
- Decisions log: AS-IS walkthroughs held 2026-06-20 (verkoop), 2026-06-24 (buitendienst), 2026-06-26 (financiën) — all three approved by consultant + client; F3 workshop to be planned (see `proposal/decision-log.md`, status gepland)
- Last updated: 2026-07-09
