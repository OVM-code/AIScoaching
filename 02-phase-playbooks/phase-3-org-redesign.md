# Phase 3 — Operating Model & Org Redesign (Week 5–8)

**Goal:** redesign processes, roles and the organigram so the strategy's value is structurally captured — tasks allocated across Humans / Automations / Agents, roles recomposed around human strengths, structure and accountability updated, and a workforce transition plan that keeps the change legitimate.

**Gate G3:** exec team approves the target operating model & organigram; works council informed where required. **Phase 5 (change) starts in parallel — do not wait.**

**Upload to Project:** `F4-operating-model-org-design.md`, `F5-change-management.md`.

## Activities

1. Task decomposition of the priority processes (Prompt 3.1) → validate with the people who do the work (30-min walkthroughs — this doubles as involvement/Desire-building).
2. Target operating model + organigram options (Prompts 3.2, 3.3) → **working session with managers** who must own the boxes; revise.
3. Role cards + RACI-A (Prompts 3.4, 3.5).
4. Workforce transition plan with HR (Prompt 3.6). Legal/works-council check per F4 §6.
5. Exec approval session → Gate G3.

## Deliverables: D13 task decomposition · D14 target operating model · D15 organigram · D16 role cards · D17 RACI-A · D18 workforce transition plan

---

## PROMPT 3.1 — Task decomposition & HAA allocation (D13)

```
Using client-context.md, the process inventory (D5) and framework F4 (steps
1), decompose the following priority processes into tasks and allocate each
task to Human / Automation / Agent:

Processes: {{LIST, e.g., quote-to-cash, planning & dispatch, customer service}}

Per process, output a table:
Task | Today: who + time | Target executor (H/A/Agent/Hybrid) | Why (apply
F4's four allocation tests explicitly) | If Agent: autonomy tier T1-T3 at
launch + promotion criterion | Human touchpoint that remains | Value released
(hours/quality)

Rules:
- Follow F4 strictly: legal/physical/trust → Human; fully rule-describable →
  Automation; language/pattern with cheap-wrong-drafts → Agent; doubt → Human.
- Every Agent row starts at T1 unless I gave evidence for higher.
- Flag tasks where the intake shows people LOVE the work — those need the
  change lens (F5 identity threat), note it.
- End with a per-process summary: % of task-hours by target executor, the 3
  biggest capacity releases, and the handoffs that disappear (input for
  structure redesign).
```

## PROMPT 3.2 — Target operating model (D14)

```
Using D13 (pasted or in Project), client-context.md, and F4 steps 2 & 5,
draft the target operating model:

1. Operating principles (5-7) for how this client runs human+agent work —
   specific to them, not generic (e.g., "every agent has a named owner in the
   line, not in IT")
2. The work: per priority process, the target flow in numbered steps showing
   H/A/Agent per step (compact notation)
3. The roles: list of roles that change, disappear into other roles, or are
   new (per F4's role table — AI Lead, agent owners, champions, builder);
   for the AI-capability question, recommend where it sits for THIS client
   (F4 §5: hat / hub-and-spoke / CoE) with reasoning
4. Decision rights: who decides tool adoption, agent promotion T1→T2→T3,
   process changes, exceptions
5. The capacity dividend map: released hours per team → their approved
   destination (from the G2 decisions — if missing, flag [DECISION NEEDED])
6. What we deliberately do NOT change in this wave

Present as a 3-4 page working document for the management working session,
with 5 open questions the managers must answer in that session.
```

## PROMPT 3.3 — Target organigram, options A/B/C (D15)

```
Using D13, D14, client-context.md (current structure in §3) and F4 step 3,
design 2-3 target organigram options:

- Option A "Minimal": current boxes kept; AI hats added (AI Lead, agent
  owners, champions); FTE shifts within teams only
- Option B "Flow redesign": merge fragmented handoff roles into end-to-end
  flow roles where D13 removed the handoffs; adjust spans; middle-layer role
  shifts per F4
- Option C "Front/back rebalance" (only if the strategy's growth ambition
  justifies it): structural FTE migration from back office to customer-facing
  capacity

Per option, output:
1. A Mermaid org chart code block. Per box: role name, FTE today → FTE at
   +12-18 mo, and the agents/automations operating in that box as ⚙ bullet
   items with tier + owner
2. What changes vs. today (bullets: reporting lines, merged/new/removed roles)
3. Transition mechanism per FTE delta (attrition/redeploy/hire/reduce —
   flag any 'reduce' prominently, per F5 §6 this needs the sponsor's people-
   story first)
4. Pros / risks / works-council sensitivity
5. Fit score against the strategy targets

End with your recommendation and the 3 decisive questions for the exec
session. Remember F4's rule: FTE numbers and agents ON the chart — the
organigram must show the operating model, not just boxes.
```

## PROMPT 3.4 — Role cards (D16)

```
Using D13/D14/D15 (chosen option: {{A/B/C}}), write role cards for every NEW
or MATERIALLY CHANGED role. Per card (max 1 page):

Role name & reports-to | Purpose in one sentence | Key responsibilities (5-8,
marking which are new) | Agents & automations this role OWNS (with tier and
quality metric) vs USES | What this role STOPS doing | Skills: current-role
baseline → target (AI literacy level, prompt craft, exception judgment,
customer skills), with the gap and training route | Success metrics (3-4) |
Capacity dividend destination | The WIIFM paragraph: why this role is better
than the old one, written honestly in language for the person, not for HR —
if it ISN'T clearly better, say what compensates or flag the fairness issue
for the transition plan.

Cards should be usable both for HR (job description input) and for the
1:1 conversations managers will have (F5 Desire lever).
```

## PROMPT 3.5 — RACI-A matrix (D17)

```
Using D13 and the chosen organigram, build the RACI-A matrix for each priority
process. Columns: process step | R | A | C | I | AGENT (which agent/automation
participates, its autonomy tier, and its human owner).

Rules (from F4 step 4): an agent may appear as R but NEVER as A — accountability
stays with a named human role. Exactly one A per step. Flag any step where
today's org has unclear accountability [GAP TODAY].

Then list the escalation paths: for each T2/T3 agent, what triggers human
escalation and to whom.
```

## PROMPT 3.6 — Workforce transition plan (D18)

```
Using D15/D16, client-context.md §7, F4 step 6 and F5 (especially §6 messaging
rules), draft the workforce transition plan:

1. Impact summary: per team — task-hours shifting, roles changed/new/merged,
   FTE trajectory and mechanism
2. Skills bridge: aggregate skills matrix (current → target), training routes
   and effort per group (feeds D26)
3. Transition paths per affected group, in F4's priority order (redeploy >
   reskill > attrition > explicit reduction); for each: timeline, support
   offered, decision owner
4. Legal & consultation checklist for {{COUNTRY: BE/FR/NL/...}}: works-council
   information/consultation triggers, any collective-procedure thresholds
   [VERIFY WITH LEGAL — I am not counsel and neither are you], sequencing
   with the comms plan
5. Commitments register: every promise we're making to employees, each with
   an owner and a check-in date (F5: broken promises cost more than the program)
6. The people-story alignment brief for the sponsor: the one version of the
   truth about jobs, in 5 sentences, plus the 5 hardest questions employees
   will ask with honest answers.
```

## Wrap-up

Update `client-context.md`: chosen option, approved model summary, transition decisions → decisions log; phase → 4 (and 5 in parallel). Re-upload.
