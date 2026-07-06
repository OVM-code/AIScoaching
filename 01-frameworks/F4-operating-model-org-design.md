# F4 — Operating Model & Org Design for the Human + AI Organization

The heart of the system: how to redesign **processes, roles, and the organigram** so value from AI, automation and agents is actually captured — instead of evaporating into slack time — while making human capital *more* valuable, not less.

## Principle: redesign around tasks, not jobs

AI rarely replaces a job; it replaces **tasks inside jobs**. So the unit of redesign is the task. The method:

```
Process map ─► Task decomposition ─► HAA allocation ─► Role recomposition ─► Structure (organigram) ─► Governance of agents
```

Structure comes **last**. Clients who start by redrawing boxes get a reorg; clients who start from tasks get a new operating model.

## Step 1 — Task decomposition & HAA allocation

For each priority process, list tasks and allocate each to **H / A / A**:

| Executor | Give it tasks that are… | Examples |
|---|---|---|
| **Human** | Judgment-heavy, relationship-critical, ethically loaded, physically embodied, exception handling, accountability moments | Negotiation, difficult customer conversations, final approval of quotes above threshold, on-site craft work, firing/hiring |
| **Automation** (deterministic: workflows, RPA, integrations) | Rule-based, repetitive, structured data in/out, high volume, zero tolerance for creativity | Invoice creation from job completion, data sync between systems, reminder sequences, scheduling within fixed rules |
| **Agent** (LLM-based, goal-directed, judgment-lite) | Unstructured input, language-heavy, pattern-based judgment, tolerable error with human catchnet | Drafting quotes/emails, triaging inbox, summarizing site reports, first-line customer Q&A, extracting data from documents, research |

Allocation tests, in order:
1. **Must a human do this?** (legal, physical, trust) → Human.
2. **Can rules fully describe it?** → Automation.
3. **Is it language/pattern work where a wrong draft is cheap?** → Agent (with the right autonomy tier, below).
4. Otherwise → Human, revisit in 12 months.

### Agent autonomy tiers (design decision per agent task)

| Tier | Pattern | Use when |
|---|---|---|
| T1 **Draft** | Agent proposes, human sends/decides every item | New agents; customer-facing text; anything with € or legal weight |
| T2 **Act-with-review** | Agent acts, human reviews samples/exceptions/thresholds | Proven agents; internal outputs; low-cost errors |
| T3 **Autonomous** | Agent acts, humans audit metrics | Mature, measured, low-risk, high-volume tasks only |

Every agent starts at T1 and **earns** promotion via measured accuracy. Promotion criteria are written in the agent spec (D20). This tiering is also your EU AI Act human-oversight story (F6).

## Step 2 — Role recomposition

Recompose the remaining human tasks into coherent roles. Design rules:

- **Rebuild roles around what humans are for**: judgment, relationships, exceptions, improvement. A role that is 80% checking agent output is a bad role — split the checking across process owners instead.
- **Push work up, not out**: freed capacity goes to higher-value work named in the strategy (more customer time, faster quotes, new offering). Every role card states its "capacity dividend destination".
- **Every agent gets a human owner** — someone accountable for its outputs, prompts, quality metrics and improvement. Owning agents becomes part of role descriptions ("runs the quoting agent" like "runs the Ghent branch").
- **New/changed roles that typically emerge:**

| Role | Scale | What it does |
|---|---|---|
| AI Lead / AI Product Owner | 1 per org (SME: hat on an existing manager) | Owns portfolio, policy, vendor relationships, benefits tracking |
| Agent Owner / Process+Agent Manager | 1 per major process | Owns the process INCLUDING its agents & automations; tunes prompts; handles escalations |
| AI Champion | 1 per team | Local power user; first-line help; feedback channel (part-time hat) |
| Automation/Integration Builder | 0.5–2 FTE or outsourced | Builds & maintains the Make/Zapier/RPA layer and integrations |
| (Enterprise) CoE roles | see §5 | Enablement, standards, reusable components |

## Step 3 — Structure: redrawing the organigram

Only now touch the boxes. Levers, with when to use them:

1. **Team resizing** — where HAA allocation removed >30% of a team's task volume: shrink via attrition/redeployment, or hold size and raise output (growth strategy decides — F2 §business-case rule).
2. **Merging fragmentation** — automation removes handoffs; roles that existed to pass information between silos (order desk → planning → invoicing chains) merge into end-to-end **flow roles** with wider spans.
3. **Flatter middle** — agents absorb much reporting/coordination work that justified coordination layers; spans of control widen; middle managers shift from information brokers to coaches & exception handlers. Handle with care: middle managers are also your biggest change risk (F5).
4. **New boxes** — AI Lead reporting line (to CEO/COO for the transformation period, possibly to IT/Ops at maturity — never bury it three levels down in IT at the start); CoE where scale justifies (§5).
5. **Front/back rebalance** — capacity migrates from back office toward customer-facing and revenue roles; the target organigram should *show* this shift in FTE numbers per box, not just boxes.

**Present structure as 2–3 options** (e.g., A: minimal change + AI hats; B: flow-team redesign; C: full front/back rebalance) with an explicit recommendation. Execs choose better between options than they approve single proposals.

### The organigram deliverable (D15) must show, per box:
- FTE today → FTE target (12–18 mo), with the transition mechanism (attrition, redeploy, hire)
- Agents & automations operating "in" that box (drawn as ⚙ items with their tier and owner)
- Changed reporting lines and new roles highlighted

Drawing agents ON the organigram is deliberate: it makes the operating model visible and makes clear that agents are managed resources, not magic.

## Step 4 — RACI-A

Extend classic RACI with an **Agent** column per process step: which agent/automation participates, at which autonomy tier, and who (human) is Accountable for it. Rule: an agent can be R (performs the work) but **never** A — accountability stays human. Template in Prompt 3.5.

## Step 5 — Where AI capability sits (CoE question — for Econocom-scale)

| Model | Fit |
|---|---|
| **Centralized CoE** | Early stage; scarce skills; need for standards & speed. Risk: ivory tower |
| **Hub-and-spoke** ✅ default | Central hub (standards, platform, reusable agents, literacy program) + BU spokes (use-case delivery, agent owners). Best for multi-BU firms like Econocom |
| **Fully federated** | Mature orgs only; requires strong platform + governance already in place |

SMEs: no CoE — an **AI Lead hat** (often the owner or operations manager) + one builder (internal or your retainer) + champions per team.

## Step 6 — Workforce transition & human capital plan

The org redesign is only legitimate if the people plan is real:

- **Skills matrix per changed role**: current → target skills (AI literacy, prompt craft, exception judgment, customer skills), gap, training route (D26).
- **Transition paths** for displaced task-hours: redeployment > reskilling > attrition-absorption > (last, explicit, sponsor-owned) reduction. Never let a reduction be discovered via a leaked organigram — sequencing rules in F5 §6.
- **Update the deal**: job descriptions, targets and bonuses must reward the new behavior (using agents well, handling more exceptions, customer time). If the bonus still pays for the old behavior, the old behavior stays.
- **Works council / CAO check** (BE/FR/NL): role changes and monitoring-adjacent tooling can trigger information/consultation duties (BE: CAO 39 collective-dismissal thresholds, "technologie-akkoorden"; FR: CSE consultation). Flag early, involve HR/legal — timing failures here can stall the whole program.
