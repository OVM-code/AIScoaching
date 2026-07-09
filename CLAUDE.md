# AI Integration Coaching System

This repository IS the product: a reusable system for coaching businesses
through AI integration (frameworks, phase playbooks, client workspaces) plus
the **Roadmap Engine** (`07-roadmap-engine/`), which turns per-department
discovery into two interactive client deliverables — the AS-IS review and the
roadmap proposal.

## Quick orientation

- `00-system/` — how to run the coaching system, master flow, intake questionnaire.
- `01-frameworks/` — F1 maturity · F2 strategy & value pools · F3 prioritization ·
  F4 operating model/HAA · F5 change · F6 governance/EU AI Act. **F1–F6 govern
  the method — cite them by path in every deliverable that applies them.**
- `02-phase-playbooks/` — phase 0–6 playbooks with the exact generation prompts.
- `03-clients/` — one workspace per client; `engagements.csv` is the single
  source of truth for engagement stage.
- `04-marketing/`, `05-website/`, `06-knowledge/` — go-to-market, site, field notes.
- `07-roadmap-engine/` — catalog, flows, viewer/proposal shells, build & check
  tools, and the model-agnostic agent cores (`cores/`).
- `.claude/agents/` — thin wrappers (process-analyst, opportunity-diagnostician,
  proposal-builder); `.claude/skills/` — the chains (`analyze-department`,
  `build-roadmap-proposal`, `run-engagement`).

## Claude-specific notes

- **Read `07-roadmap-engine/README.md` before any engine work** — it is the
  binding spec for the pipeline, data contracts, enums, and gates.
- After EVERY authoring step run
  `python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>` —
  zero errors and warnings is the definition of done.
- **Two human gates, never bypassed by an agent:** (1) AS-IS approval — only
  the consultant sets `Status: approved`, after the client walkthrough;
  (2) roadmap confirmation — only the client's workshop confirmation export
  moves an engagement to `confirmed`. Never skip a stop condition to save
  time; never send anything to the client directly.
- New client: copy `03-clients/_template/` to `03-clients/<slug>/` and fill
  `engagement-config.json` interactively with the consultant.
- Update `03-clients/engagements.csv` whenever an engagement's stage changes —
  agents and humans both read it as pipeline status.
- Deliverables in the client's configured language
  (`engagement-config.json` → `language`; Belgian default `nl`).
- Opportunity verdicts default to skepticism: a use case is a **discard until
  the evidence says otherwise**; verdicts are falsifiable (confidence +
  what-would-change), discards recorded, never deleted. Honest ROI: treat
  self-reported savings as inflated 2–3× and say so
  (`../AINativityCoaching/knowledge-base/09-teams-and-organisations.md` §9.4).
- Pain and AS-IS facts carry literal quotes with source citations
  (`<file> §<n>`) — never invent; ask the consultant on contradictions.
- New agents/skills follow the Holding agent toolkit standard
  (`../Holding/06-agent-toolkit/`): model-agnostic core in
  `07-roadmap-engine/cores/`, thin Claude wrapper, Sonnet by default with the
  escalation condition stated in a `<!-- model: -->` note.
