# Roadmap Engine — from department workshops to a confirmed AI integration roadmap

The Roadmap Engine turns per-department discovery material (workshop transcripts,
notes, intake) into two client-facing interactive deliverables:

1. **AS-IS review** — one self-contained HTML file showing the client's business
   processes per department as clickable BPMN diagrams, color-coded by pain
   severity, where every step opens the documentation of how that process runs
   today, what hurts, and the first-look automation potential. Reviewed and
   approved by consultant **and** client before any recommendation is made.
2. **Roadmap proposal** — one self-contained HTML page the client *operates*:
   an opportunity register scored on Value × Feasibility (F3), € figures driven
   by adjustable assumption sliders, a quadrant scatter, wave-based roadmap with
   recomputing ROI/payback totals, and a **select & confirm** flow that exports
   the client's chosen roadmap as JSON.

It operationalizes the frameworks in `01-frameworks/` (F1 maturity, F2 value
pools & business-case discipline, F3 prioritization, F4 Human/Automation/Agent
allocation, F6 governance) with tooling and conventions ported from proven
sibling systems (ERP BPA pipeline & viewer, Holding agent toolkit & validator
pattern, AINativityCoaching generator discipline).

## Moving parts

| Path | What it is |
|---|---|
| `07-roadmap-engine/catalog/departments.json` | Machine-readable index of departments and coded generic business processes — the controlled vocabulary everything maps to |
| `07-roadmap-engine/catalog/departments/NN-*.md` | Authoring source per department: typical process descriptions, value-leak patterns, AI-opportunity patterns |
| `07-roadmap-engine/flows/NN-*.process.json` | Standard AS-IS flow skeletons per department (BPMN, auto-layout, bilingual labels) |
| `07-roadmap-engine/viewer/` | Interactive AS-IS viewer (HTML/CSS/JS), inlined into every build |
| `07-roadmap-engine/proposal/` | Dynamic proposal shell (HTML/CSS/JS), inlined into every build |
| `07-roadmap-engine/baselines/effort-baselines.json` | Conservative effort seeds per initiative type × T-shirt size — calibrated from actuals over time |
| `07-roadmap-engine/tools/build_asis.py` | Compiles a client's department workspaces into the AS-IS review HTML |
| `07-roadmap-engine/tools/build_proposal.py` | Compiles the opportunity register + assumptions into the proposal HTML |
| `07-roadmap-engine/tools/check_engagement.py` | Mechanical validator — zero errors/warnings is the definition of done |
| `07-roadmap-engine/cores/` | Model-agnostic agent cores (wrapped thinly in `.claude/agents/`) |
| `03-clients/_template/` | Per-client engagement workspace template |
| `03-clients/engagements.csv` | Single source of truth for engagement stage |
| `03-clients/_demo-installtech/` | Worked demo: fictional client, end-to-end |

## The pipeline

Each stage gates the next; never skip a gate to save time.

```
intake → discovery (per department) → asis-review [HUMAN GATE: consultant + client approve]
       → diagnosis (value leaks → opportunities, HAA allocation, scoring)
       → proposal [CLIENT GATE: workshop, client adjusts + confirms]
       → confirmed roadmap → delivery (pilot charters, phase 4) → aftercare
```

**Step 0a — Brief.** Before each department workshop, generate a briefing pack in
`departments/NN-<dept>/briefings/`: known facts from intake, hypothesis scope per
catalog process, numbered questions, applicable patterns from
`catalog/departments/NN-*.md` and `06-knowledge/`.

**Step 0 — Collect.** Drop meeting material in `departments/NN-<dept>/inputs/`,
one file per meeting (`YYYY-MM-DD-<topic>-<type>.md`). Text only — transcribe
recordings first. Note source quality in the file header.

**Step 1 — Extract pains.** Distil discrete pain points into the department's
`pains.md` (`## PAIN-x` blocks). Each keeps a literal client quote, a source
citation (`<file> §<n>`), pain type, severity, and volume. Ask the consultant
about contradictions between meetings rather than guessing.

**Step 2 — Document AS-IS.** For every in-scope catalog process, write how it
runs today in `content/NN-<dept>.md` (`## <CODE>` blocks): current way of
working, who, systems, volume & time, linked pains, severity, first-look
automability (F4 HAA). Processes explicitly out of scope get a one-line reason
in `coverage.md`.

**Step 3 — Flows.** The standard flows in `07-roadmap-engine/flows/` are the
default. Copy into `departments/NN-<dept>/flows/` and adapt to the client's real
process (extra channels, missing approval steps, …) — same `domain` number
overrides the standard at build time.

**Step 4 — Build AS-IS & review.**
```bash
python3 07-roadmap-engine/tools/build_asis.py 03-clients/<slug>
```
Output: `03-clients/<slug>/asis/output/ASIS-<slug>.html`. Walk it through with
the client; corrections go back into steps 1–3. When consultant and client
agree it is a faithful picture, set `Status: approved` in each department's
content-file header table. **No diagnosis before approval** — recommendations
built on a wrong AS-IS are worthless.

**Step 5 — Diagnose.** Run the F1 maturity scan (`analysis/maturity.md`).
Generate opportunity candidates (verb + object + mechanism) from approved pains,
F2 value pools, and the catalog's opportunity patterns; allocate each per F4
(automation / agent-T1..T3 / hybrid); score per F3 (Value × Feasibility,
adoption tie-break); write `## OPP-x` blocks in `analysis/opportunities.md`.
Every OPP carries a falsifiable verdict with confidence and "what would change
this" — the default posture is skepticism, and discards are recorded, not
deleted. Define the assumption model in `analysis/assumptions.json` (4–8
sliders that every € figure derives from).

**Step 6 — Build proposal & confirm.**
```bash
python3 07-roadmap-engine/tools/build_proposal.py 03-clients/<slug>
```
Output: `03-clients/<slug>/proposal/output/ROADMAP-<slug>.html`. Run the F3
workshop: client challenges scores, adjusts sliders, selects initiatives,
exports the confirmation JSON. Record it in `proposal/decision-log.md`, update
OPP statuses (`confirmed` / `deferred` / `discarded`), set the engagement stage
to `confirmed`.

**After every authoring step:**
```bash
python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
```
Zero errors and warnings is the definition of done.

## Data contracts

### `engagement-config.json` (client workspace root)

```jsonc
{
  "client": "InstallTech BV",
  "slug": "_demo-installtech",
  "language": "nl",              // "nl" | "en" — deliverable language
  "accentColor": "#D9480F",      // optional brand accent
  "sector": "HVAC-installatie",
  "departments": [2, 5, 8],      // catalog department numbers in scope
  "day_rate": 950,               // consulting day rate (EUR) for cost estimates
  "currency": "EUR"
}
```

### `catalog/departments.json`

```jsonc
{
  "version": "1.0",
  "source": "Roadmap Engine department model",
  "departments": [
    { "number": 2, "id": "sales", "prefix": "SAL",
      "title": { "nl": "Verkoop & offertes", "en": "Sales & quoting" },
      "file": "02-sales.md" }
  ],
  "processes": [
    { "code": "SAL.030",
      "title": { "nl": "Offerte opstellen", "en": "Draft quote" },
      "department": 2,
      "leak_patterns": ["retype", "wait"] }   // typical pain types, informative
  ]
}
```

Process codes are `<PREFIX>.<NNN>` (three digits, steps of 10). The catalog is
generic across industries; per-client relevance is decided in `coverage.md`.

### `*.process.json` (flows — identical to the proven ERP format)

```jsonc
{
  "id": "sales",              // unique flow id (used by "goto")
  "domain": 2,                 // catalog department number
  "title": { "nl": "Verkoop", "en": "Sales" },
  "subtitle": { "nl": "Van aanvraag tot betaalde factuur", "en": "…" },
  "lanes": [ { "id": "binnendienst", "label": { "nl": "Binnendienst", "en": "Inside sales" } } ],
  "nodes": [
    // types: start | end | task | subprocess | gateway | gateway-parallel
    { "id": "start", "type": "start", "label": { "nl": "Klantaanvraag", "en": "Customer inquiry" }, "lane": "binnendienst" },
    { "id": "quote", "type": "task", "label": { "nl": "Offerte opstellen", "en": "Draft quote" },
      "lane": "binnendienst", "process": "SAL.030" }   // clickable + color-coded
  ],
  "flows": [ { "from": "start", "to": "quote", "label": { "nl": "ja", "en": "yes" } } ]
}
```

Keep flows at 10–20 nodes; split bigger ones into a `subprocess` + `goto`.
Labels may be plain strings (used for both languages) or `{nl,en}` objects.

### Department workspace (`03-clients/<slug>/departments/NN-<dept>/`)

```
inputs/           YYYY-MM-DD-<topic>-<type>.md   raw material, quality noted in header
briefings/        pre-workshop briefing packs
pains.md          ## PAIN-x blocks
content/NN-<dept>.md   ## <CODE> AS-IS blocks + status header table
coverage.md       scope matrix: | Code | Proces | Scope | Reden |
flows/NN-<dept>.process.json   adapted AS-IS flow (optional; standard is default)
```

### `pains.md` — `## PAIN-x` block

```markdown
## PAIN-3 — Offertes hertypen vanuit e-mails en werfnotities
- **Processen:** SAL.030
- **Citaat:** "Elke offerte typ ik letterlijk over uit de mail van de klant."
- **Bron:** inputs/2026-06-12-verkoop-transcript.md §14
- **Type:** retype
- **Severity:** major
- **Volume:** 40/maand × ±45 min
- **Waardehypothese:** ±20 u/maand binnendienst vrij te spelen
```

Enums — `Type`: `retype | chase | wait | error | skill-bottleneck | no-visibility`.
`Severity`: `minor | major | critical`.

PAIN ids are numbered **once across the whole engagement** (`PAIN-1…n`), even
though each department keeps its own `pains.md` — OPP blocks reference them
globally, and a reused id across departments is ambiguous.

### `content/NN-<dept>.md` — status header + gate + `## <CODE>` blocks

```markdown
| Client | Afdeling | Status | Laatst gereviewd | Goedgekeurd door | Datum |
|---|---|---|---|---|---|
| InstallTech BV | Verkoop & offertes | approved | 2026-06-20 | zaakvoerder + consultant | 2026-06-20 |

## Gate

**Directieven**

- [ ] doorlooptijd per offerte ook opnemen in SAL.030
- [x] volume gecorrigeerd naar 40/maand (toegepast 2026-06-18)

## SAL.030 — Offerte opstellen
- **Huidige werkwijze:** Binnendienst hertypt aanvraag uit e-mail in Excel-sjabloon, …
- **Wie:** binnendienst (2 pers.)
- **Systemen:** Outlook, Excel, boekhoudpakket
- **Volume & tijd:** 40/maand, ±45 min per offerte
- **Pijn:** PAIN-3, PAIN-4
- **Severity:** major
- **Automability:** agent
```

Enums — content `Status` (header table): `draft | consultant-review | client-review | approved`.
Block `Severity`: `none | minor | major | critical` (drives the flow color).
`Automability` (F4 first look): `human | automation | agent | hybrid`.

The header table **is** the AS-IS approval gate: `Goedgekeurd door` and
`Datum` are filled on approval (until then `—`). The `## Gate` section (before
the first `## <CODE>` block) holds the reviewers' **directives** — change
instructions recorded as a checklist, applied to this file, and ticked off
with the date applied (`- [x] … (toegepast YYYY-MM-DD)`). `Status: approved`
with an open `- [ ]` directive is a checker error.

### `analysis/opportunities.md` — `## OPP-x` block

```markdown
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
```

Enums — `Status`: `proposed | confirmed | deferred | discarded`.
`Allocatie`: `automation | agent-T1 | agent-T2 | agent-T3 | hybrid`.
`Effort`: `S | M | L`. `Wave`: `1 | 2 | 3 | -` (`-` for discards).
`Verdict`: `quick-win | big-bet | fill-in | discard` — must match the computed
quadrant (Value and Feasibility are the F3 weighted averages; "high" = ≥ 3.5).

Score computation (F3 defaults; per-client weight overrides go in the OPP file
and the proposal states them):

```
Value       = 0.50*hours + 0.25*quality + 0.25*strategic          (each 1–5)
Feasibility = 0.40*data  + 0.30*technical + 0.30*ownership        (each 1–5)
```

`Waardeformule` is a plain arithmetic expression over assumption ids, numbers,
`+ - * / ( )`. `build_proposal.py` validates every token against
`assumptions.json` and compiles the formula to a static JS function — no runtime
eval. Every OPP that carries a € value must have a formula; discards may omit it.
`Aannames` lists **bare assumption ids only**, and must equal the set of ids the
formula uses; numeric substantiation or calibration prose goes in an optional
free-form `Cijferbasis` bullet, which the tools ignore.

### `analysis/assumptions.json`

```jsonc
{
  "assumptions": [
    { "id": "quotes_per_month", "label": { "nl": "Offertes per maand", "en": "Quotes per month" },
      "unit": "/maand", "min": 10, "max": 100, "step": 5, "default": 40,
      "source": "intake §3 — te kalibreren in pilotweek 1" }
  ]
}
```

4–8 assumptions; every € figure in the proposal derives from these via stated
one-line formulas. Label everything directional; each assumption names its
calibration path in `source`.

### `baselines/effort-baselines.json`

```jsonc
{
  "version": "0.1-seed",     // conservative expert seeds, uncalibrated
  "day_rate_default": 950,
  "implementation_days": {
    "automation": { "S": 3, "M": 8,  "L": 18 },
    "agent-T1":   { "S": 5, "M": 12, "L": 25 },
    "agent-T2":   { "S": 8, "M": 18, "L": 35 },
    "agent-T3":   { "S": 12, "M": 30, "L": 60 },
    "hybrid":     { "S": 5, "M": 12, "L": 25 }
  }
}
```

Cost model per OPP: `implementation = days(allocatie, effort) × day_rate`,
`year-1 cost = implementation + 12 × tooling €/maand`,
`payback (months) = year-1 cost / (annual value / 12)`. Baselines are
recalibrated from actuals at each engagement close — bump `version`.

### `03-clients/engagements.csv`

```
slug,client_name,sector,language,stage,departments_in_scope,next_action,last_updated,notes
```

`stage` enum: `intake | discovery | asis-review | diagnosis | proposal |
confirmed | delivery | aftercare | closed`. One row per engagement, keyed by
slug (= folder name). Update the row on every stage change.

## Gates (enforced by `check_engagement.py`)

The two human gates each live on a **gate carrier** with a `## Gate` block:
a status plus a **Directieven** checklist. Directives are the human's change
instructions given at review: the assistant records them in the block, applies
them to that artifact, and ticks them off with the date applied
(`- [x] … (toegepast YYYY-MM-DD)`).

1. **AS-IS approval, per department** — carrier: the content file's status
   header table (extended with `Goedgekeurd door` + `Datum`; `Status` enum
   unchanged: `draft | consultant-review | client-review | approved`) plus a
   `## Gate` section holding the directives. See the content schema above.
2. **Roadmap confirmation** — carrier: `proposal/decision-log.md`, with a
   `## Gate` block. Its status values are Dutch and stored as such in the
   file: `gepland | in review | bevestigd`, mapping 1:1 to
   `draft | in review | approved` — the checker treats `bevestigd` as the
   approved state.

```markdown
## Gate

| | |
|---|---|
| Status | gepland <!-- gepland / in review / bevestigd --> |
| Goedgekeurd door | — |
| Datum | — |

**Directieven**

- [ ] discard OPP-10 op de workshopagenda zetten
```

Checker rules:

- **No approval with open directives**: `approved` (content file) or
  `bevestigd` (decision log) with any unchecked `- [ ]` in that `## Gate`
  section is an error — apply or withdraw them first.
- **Visibility**: every run prints one `gates:` line with each gate's status
  and open-directive count — that line is the consultant's to-do list.
- `diagnosis` artifacts (`analysis/opportunities.md`) require every in-scope
  department's content `Status: approved`.
- `build_proposal.py` refuses to build when a department is unapproved or the
  opportunity register / assumptions are missing (warnings in `--dry-run`).
- Stage `confirmed` requires `proposal/decision-log.md` and at least one OPP
  with `Status: confirmed`.
- Unknown process codes, dangling PAIN/OPP references, formula tokens not in
  `assumptions.json`, out-of-range scores, and verdict/quadrant mismatches are
  build/check errors.

## Color coding

**AS-IS viewer** — by step `Severity` (Pijn mode, default):

| Severity | Color | Meaning |
|---|---|---|
| `none` | blue | runs fine today |
| `minor` | amber | friction, liveable |
| `major` | orange-red | recurring cost / delay / error |
| `critical` | red | actively bleeding value |
| *(no documentation)* | grey dashed | step in flow but not documented in this version |

**Kansen mode** (toggle, available once opportunities exist) — by `Automability`
/ OPP allocation: `human` grey-blue, `automation` teal, `agent` purple,
`hybrid` indigo.

## Language

Deliverables follow `language` in `engagement-config.json` (`nl`, `en`).
Viewer/proposal chrome and standard flow labels switch automatically; client
content is authored directly in the client's language. Belgian default: `nl`.

## Where the concepts come from

- ERP repo: BPA transcript→codes pipeline, process.json + viewer, build/check
  tooling pattern, effort baselines, dynamic-report deliverable.
- AIScoaching: F1–F6 frameworks, phase playbooks, pain-point inventory schema,
  client-context single source of truth.
- Holding: agent toolkit (cores + thin wrappers, Sonnet-default), forced
  falsifiable verdicts, validator-in-lockstep-with-conventions.
- AINativityCoaching: generator discipline (parameters → outline → self-check),
  honest-ROI framing (self-reported savings inflate 2–3× — say so in proposals).
