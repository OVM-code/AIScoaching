# Opportunity register — [CLIENT NAME]

| Client | Status | Laatst gereviewd |
|---|---|---|
| [CLIENT NAME] | draft | [YYYY-MM-DD] |

One `## OPP-x` block per opportunity (verb + object + mechanism), generated
from **approved** pains, F2 value pools and the catalog's opportunity patterns.
**Gate:** no OPP blocks before every in-scope department's content is
`approved` — the checker errors otherwise. Default posture is skepticism;
discards are recorded (`Status: discarded`), never deleted.

Enums — **Status:** `proposed | confirmed | deferred | discarded`.
**Allocatie** (F4): `automation | agent-T1 | agent-T2 | agent-T3 | hybrid`.
**Effort:** `S | M | L`. **Wave:** `1 | 2 | 3 | -` (`-` for discards).
**Verdict:** `quick-win | big-bet | fill-in | discard` — must match the
computed quadrant (high = ≥ 3.5):
`Value = 0.50*hours + 0.25*quality + 0.25*strategic`,
`Feasibility = 0.40*data + 0.30*technical + 0.30*ownership` (each 1–5;
per-client weight overrides go here and the proposal states them).
`Waardeformule` uses only assumption ids from `assumptions.json`, numbers and
`+ - * / ( )`; every Wave 1–3 OPP must have one.

<!-- Example block — copy, uncomment and renumber:

## OPP-4 — Offertes genereren uit aanvraag-mail en werfnotities met een LLM-assistent
- **Status:** proposed
- **Afdelingen:** SAL
- **Processen:** SAL.030
- **Pijnpunten:** PAIN-3, PAIN-4
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
- **Wat dit zou veranderen:** als de aanvraagdata te ongestructureerd blijkt (<60% bruikbaar), zakt feasibility naar 2 en schuift dit naar wave 2.
- **Enablers:** offerte-sjabloon standaardiseren; e-mail-inbox als gedeelde bron
- **Risico / AI Act:** beperkt risico; menselijke review van elke offerte (T1)
- **Eerste stap:** 2 weken schaduwdraaien op de laatste 20 offertes

-->
