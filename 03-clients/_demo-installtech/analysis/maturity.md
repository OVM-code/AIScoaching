# F1 — AI maturity scan — InstallTech BV

Per `01-frameworks/F1-ai-maturity-scan.md`: 6 dimensions, scored **1–5 to one
decimal**, from interview + evidence, not aspiration. A dimension only reaches
a level when all typical evidence of the level below is present. The profile
shape matters more than the average. Re-run at engagement close to show
progress.

| Scan date | Evidence base | Scored by |
|---|---|---|
| 2026-06-30 | intake + 3 department workshops (transcripts, quality high) + system walk-through (Exact, server folders, planbord) | consultant (O. Vanmalleghem) |

## Scores

| # | Dimension | Score (1–5) | Evidence (2–3 concrete observations) |
|---|---|---|---|
| 1 | Strategy & Leadership | 2.3 | Owner sponsors and articulates priorities crisply ("offerte binnen de twee dagen"); funds a diagnostic; but no written view on where AI creates value, and no owner besides himself |
| 2 | Data & Systems | 1.7 | Paper werkbonnen (±85/week) and hand-reconstructed hours; no CRM — customer history in mailboxes and heads; contracts in a 2019 Excel; only financials (Exact + Peppol) are digital and trusted |
| 3 | Processes | 2.6 | Core flows are stable and were easy to document (workshops confirmed one consistent story per department); but nothing is written down, ownership is implicit, and handoffs (SAL.060) leak |
| 4 | People & Skills | 2.1 | Two shadow-AI users (owner, one binnendienst); techniekers capable but wary after the 2021 planning-app failure; no training done; strong opinion leaders exist (Rita, senior technician) |
| 5 | Technology & Tooling | 2.2 | Office 365 + Exact Online are solid rails; Peppol e-invoicing live since Jan 2026; but no sanctioned AI tools, no integrations/automation platform, SSO absent |
| 6 | Governance & Culture | 1.6 | No AI policy; customer data occasionally pasted into a free ChatGPT account (owner, self-reported); no risk framing; culture pragmatic rather than fearful — a policy would land well |

## Per-dimension: constraint analysis & first moves

### 1. Strategy & Leadership
- Constraint analysis: does not block wave 1 — the owner's clarity of intent substitutes for a written strategy at this size. Becomes a constraint in wave 2+ when priorities compete (growth vs. efficiency cases).
- First moves: one-page AI ambition note signed by the owner; owner personally uses the quote-drafting assistant (OPP-2) — his visible usage is the comms plan.

### 2. Data & Systems
- Constraint analysis: **blocks most of the portfolio.** Job costing (OPP-7), follow-up capture (OPP-6), contract growth (OPP-5) and even same-day invoicing (OPP-3) all consume data that today exists only on paper or not at all. Nothing analytics-shaped is feasible until capture at the source is digital.
- First moves: voice-note werkbon pilot (OPP-1) — the single enabler that unlocks half the register; consolidate the contract Excel and installed-base list into one maintained source.

### 3. Processes
- Constraint analysis: mild. Processes are stable enough to automate; the leaking handoff (SAL.060) needs a process fix alongside any tooling.
- First moves: write the offerte→werkorder handover as a one-page checklist (enabler for OPP-2/OPP-3); name a process owner per department (office-verantwoordelijke, Rita, administratie 1).

### 4. People & Skills
- Constraint analysis: blocks nothing in wave 1 if adoption design respects the 2021 lesson (near-zero-effort capture, pilot with the most open technician first). Becomes binding in wave 2 (agent-T2 cases need confident reviewers).
- First moves: hands-on session with the field team around the voice-note pilot (that IS the training); short prompt-hygiene training for binnendienst and administratie.

### 5. Technology & Tooling
- Constraint analysis: moderate. The Exact/Peppol rails carry the finance cases; absence of a field-service tool means wave-1 tooling must be lightweight (app + automation platform), not an ERP project.
- First moves: pick one sanctioned LLM workspace with data controls (kills the free-ChatGPT risk); stand up one automation platform (Make/Zapier-class) as the integration spine.

### 6. Governance & Culture
- Constraint analysis: does not block wave 1 technically, but the free-tool shadow use is a live GDPR exposure, and time registration (SVC.090) touches monitoring sensitivities — governance must precede that pilot (F4 §6).
- First moves: 2-page AI policy in plain Dutch (sanctioned tools, red lines, data rules); frame voice-note time capture as billing accuracy with the team involved early — explicitly not monitoring.

## Binding constraint

- **Binding constraint:** Data & Systems (1.7) — concretely: **data discipline at the source** (paper werkbonnen, reconstructed hours, unmaintained customer/contract lists).
- **Why:** every workshop independently hit the same wall — invoicing waits on paper (FIN transcript §3), costing has no trustworthy input (§15), follow-up work and contracts live in heads and a 2019 Excel (SVC transcript §13, §16). The evidence chain from all three departments converges on capture-at-source.
- **What raising it unlocks:** OPP-3 (same-day invoicing), OPP-6 (follow-up revenue), OPP-7 (job costing) and the growth case OPP-5 are all capped by it today — which is why OPP-1 (digital werkbon) sequences first in wave 1 and why the fill-ins that don't depend on it (OPP-8, OPP-9) can run in parallel.

## Top-3 gaps constraining value capture

1. **Paper capture at the source** — werkbonnen, hours, materials (Data & Systems 1.7): caps invoicing speed, costing, follow-up and contract growth.
2. **No governance around already-happening AI use** (Governance 1.6): GDPR exposure now, adoption risk later when monitoring-adjacent pilots start.
3. **Single-person dependencies** (Processes/People): Rita's planning and binnendienst 1's quoting knowledge are strengths without backup — the roadmap must assist, not replace, and document as it goes.
