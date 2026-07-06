# F1 — AI Maturity Scan

A structured assessment of where the client stands today across **6 dimensions**, scored on a **5-level scale**. Output: a spider chart, dimension narratives, and the 3 gaps that most constrain value capture. Used in Phase 1; re-run at the end of the engagement to show progress.

## The 6 dimensions

| # | Dimension | What it measures |
|---|---|---|
| 1 | **Strategy & Leadership** | Is there a view on where AI creates value? Does leadership sponsor, fund, and model usage? |
| 2 | **Data & Systems** | Is the data needed for priority use cases accessible, digital, and trustworthy? Are core systems API-able? |
| 3 | **Processes** | Are core processes explicit and stable enough to automate/augment? Is there process ownership? |
| 4 | **People & Skills** | AI literacy across roles; presence of power users; hiring/training pipeline; psychological safety to experiment. |
| 5 | **Technology & Tooling** | Sanctioned AI tools in place? Integration/automation capability? Security baseline (SSO, access control)? |
| 6 | **Governance & Culture** | Usage policy, risk awareness, GDPR/AI Act posture; experimentation culture vs. shadow AI chaos or blanket bans. |

## The 5 maturity levels

| Level | Label | Typical evidence |
|---|---|---|
| 1 | **Ad hoc** | Individual, private tool use; no policy; leadership unaware or dismissive |
| 2 | **Exploring** | Pockets of experimentation; some paid licenses; talk but no plan; wildly uneven skills |
| 3 | **Structured** | Named owner; policy exists; 1–3 use cases in production; training started; data cleanup underway |
| 4 | **Integrated** | AI embedded in several core processes; roles redesigned around it; benefits measured; governance routine |
| 5 | **Transformative** | AI shapes strategy & offerings; human+agent operating model is the norm; continuous portfolio management |

**Scoring rules:** score each dimension to one decimal (e.g., 2.4) based on interview + evidence, not aspiration. A dimension only reaches a level when *all* typical evidence of the level below is present. Most SMEs land at 1–2; most corporates at 2–3 with high variance between units. **The profile shape matters more than the average** — a client at Strategy 4 / Data 1 has a very different problem than the reverse.

## Evidence collection

- Intake questionnaire (Parts C, D, E)
- 3–6 role interviews (one per major function; for Econocom-scale: per BU)
- System walk-through (screen-share of the real ERP/CRM/planning tool, not the slideware version)
- Anonymous 10-question staff pulse survey (template in Prompt 1.1) — measures actual usage, fear, and appetite; expect the shadow-AI number to surprise leadership

## Interpretation → so-what

For each dimension, the scan report answers three questions:
1. **Score & evidence** — where they are, with 2–3 concrete observations.
2. **Constraint analysis** — does this dimension block the likely priority use cases? (A Data score of 2 kills analytics use cases but not drafting/communication use cases.)
3. **First moves** — the 1–2 actions that raise the score fastest.

The final section names the **binding constraint**: the single dimension that, unless raised, caps everything else. This drives the Phase 2 roadmap sequencing.

## SME shortcut

For SMEs, skip the survey and role interviews; score from the intake interview + one system walk-through, and present as a simple 6-bar chart with a paragraph each. Levels 4–5 language can be dropped — frame as "Ad hoc → Exploring → Structured" journey.
