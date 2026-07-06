# Phase 6 — Scale & Governance (Week 14+)

**Goal:** make it permanent. Scale the proven pilots through the approved org design, install right-sized governance (policy, risk register, compliance posture), stand up the AI ownership structure, and hand over a benefits tracker + next-wave plan so the client can run wave 2 without you.

**Gate G6:** governance live, benefits reviewed quarterly, AI ownership operating, close-out accepted.

**Upload to Project:** `F6-governance-risk-eu-ai-act.md`, keep F2/F4.

## Activities

1. Execute the scale plans from G4 decisions (rollout order, training waves per D26, org changes per D15 activate now).
2. Policy + governance stack (Prompts 6.1, 6.2), compliance check (6.3).
3. Stand up the AI ownership structure (Prompt 6.4) and transfer your artifacts (prompt library, eval sets, runbooks) to the client's AI Lead.
4. Benefits tracker (6.5), executive close-out + next wave (6.6).

## Deliverables: D29 AI policy · D30 governance charter & risk register · D31 compliance check · D32 CoE/ownership design · D33 benefits tracker · D34 close-out & next wave

---

## PROMPT 6.1 — AI usage policy (D29)

```
Using client-context.md, F6 §1-3, and the sanctioned tools decided in the
pilots (D21), draft the AI usage policy for this client — sized for them
(SME: 2 pages max; enterprise: policy + annexes).

Contents: purpose & spirit (enable safely, not forbid); sanctioned tools
list + how to request new ones; data rules (what may never enter which tool
class — concrete examples from THEIR business, e.g. customer lists,
personnel data, {{SECTOR-SPECIFIC}}); verification duty before output is
used/sent; disclosure rules (when we tell customers AI was involved; chatbot
disclosure per AI Act); agent-specific rules (autonomy tiers, owner duties,
incident reporting); personal/shadow use (converted, not banned: what's
tolerated on which data); consequences framed proportionally; policy owner
+ review cycle.

Language: {{LANGUAGE}}, plain, no legalese, readable by a field technician in
5 minutes. End with a 10-line summary card for the workshop wall / van
dashboard. Add [LEGAL REVIEW] markers where counsel must confirm.
```

## PROMPT 6.2 — Governance charter & risk register (D30)

```
Using F6 §1 and §4, the operating model (D14) and the live use cases, draft:

1. Governance charter sized for this client: decision rights table (tool
   adoption, agent tier promotion, new use cases, risk acceptance, policy
   changes — who decides, who's consulted); meeting rhythm (SME: quarterly
   AI review in existing management meeting — do NOT invent new meetings;
   enterprise: AI board + CoE cadence per F4 §5); the agent lifecycle
   standard (spec → eval set → T1 → promotion → quarterly review →
   retirement), referencing the D20 runbooks
2. Risk register: start from F6 §4's recurring risks, keep what applies,
   add client-specific risks from the pilots' incidents and retros; per
   risk: owner, mitigation, indicator, review date
3. Incident process: one page — what counts as an AI incident here, first
   response, logging, learning loop
```

## PROMPT 6.3 — EU AI Act & GDPR compliance check (D31)

```
Using F6 §2-3 and the list of live + planned use cases below, run the
deployer checklist per use case:

Per use case: prohibited-practice check | Annex III high-risk check (flag
especially anything touching employment decisions, worker monitoring or
evaluation) | transparency/disclosure duties | GDPR: personal data involved?
legal basis, ROPA update needed, DPIA trigger?, processor terms status |
AI-literacy evidence (training records from D26) | human-oversight evidence
(tiers from D17/D20) | actions needed, owner, deadline.

Output: a compliance status table + action list + a half-page summary for
the sponsor. Add prominently: this is a structured self-assessment by a
coach, not legal advice; items marked [LEGAL REVIEW] go to counsel; AI Act
guidance evolves — recheck dates and current guidance at delivery.

USE CASES: {{LIST or reference D9/D22}}
```

## PROMPT 6.4 — AI ownership / CoE design (D32)

```
Using F4 §5, D14 §3 and the reality of who emerged during pilots (I describe
below), finalize the AI ownership design:

- For SMEs: the AI Lead hat (who, hours/week, responsibilities, direct line
  to owner/CEO), the builder arrangement (internal person / my retainer /
  local partner — compare cost & risk), champions continuation
- For enterprises: hub-and-spoke design — hub roles & FTE, spoke roles per
  BU, funding model, what's mandatory-central (policy, platform, eval
  standards, literacy program) vs BU-free; 90-day stand-up plan
- Both: the handover inventory from me to them (prompt library, eval sets,
  runbooks, this system's frameworks), capability-transfer checklist, and
  the criteria for when they need me vs. handle it themselves

WHO EMERGED: {{notes on standout people from pilots}}
```

## PROMPT 6.5 — Benefits realization tracker (D33)

```
Using the strategy targets (D8 §5), business cases (D10) and pilot actuals
(D22), build the benefits tracker:

1. Benefit register: per benefit — metric, baseline, target, actual-to-date,
   owner, measurement method & frequency, capacity-dividend destination and
   whether the dividend is ACTUALLY being captured there (the honest column)
2. A quarterly one-page review template the AI Lead fills: trend per benefit,
   variance explanation, decisions needed
3. The rules: benefits counted once, capacity only counts when its
   destination is verifiable (billable hours logged, hire avoided & documented,
   overtime reduced in payroll), leading vs lagging indicators marked
4. Year-1 projection vs the G2 business cases, with confidence level
```

## PROMPT 6.6 — Executive close-out & next-wave plan (D34)

```
Using the whole engagement record in client-context.md (decisions log) and
D33, draft the close-out deck, max 8 slides + a 1-page memo version:

1. Where we started (G1 maturity picture) → where we are (re-scored F1 scan —
   ask me for the re-score inputs if missing)
2. What shipped: use cases live, org changes made, people trained, policy &
   governance installed
3. The numbers: benefits vs business case, honestly, incl. what didn't work
   and was killed (and why that's the system working)
4. The organization now: the new organigram as-built, agents in operation
   with owners and tiers
5. What made it work here / what nearly derailed it (retro, in their story)
6. Wave 2 recommendation: the parked big bets (D9 §3) with their now-status,
   enabler progress, and a proposed 6-month plan
7. Continuity: ownership handover status, when to call me
8. Thank-you slide with the 3 best employee verbatims from the journey
```

## Wrap-up

Final `client-context.md` update (phase → done, full decisions log). Archive the Claude Project or keep it live under a retainer arrangement for quarterly reviews.
