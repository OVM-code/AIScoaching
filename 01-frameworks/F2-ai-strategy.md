# F2 — AI Strategy Framework

How to get from "we should do something with AI" to a one-page strategy the exec team actually signs. The framework forces choices: **where to play, how to win, what to build first, what NOT to do.**

## Core logic: value pools before tools

AI strategy = business strategy, continued by other means. Start from the client's strategic priorities (intake Q6) and margin structure, then locate AI's leverage in four **value pools**:

| Value pool | Question | Typical levers |
|---|---|---|
| **P1 Productivity** | Same output, fewer hours | Drafting, summarizing, data entry elimination, automated admin, agent-handled routine communication |
| **P2 Quality & Risk** | Fewer errors, better decisions | Checklisting, validation agents, anomaly detection, consistent quotes/pricing, compliance checks |
| **P3 Growth** | More revenue from existing capacity | Faster quote turnaround, lead response time, upsell prompts, better win-rate, capacity released to billable work |
| **P4 New offerings** | Revenue that didn't exist before | AI-enhanced services, data products, new pricing models, 24/7 service coverage |

**Sequencing rule:** P1/P2 fund and de-risk P3/P4. Start where value is provable in one quarter (usually P1), but the strategy must name at least one P3/P4 ambition or it degenerates into a cost program — which kills adoption energy (people don't rally around their own efficiency targets).

## The strategy-on-a-page (the deliverable)

One page, six blocks. If it doesn't fit, it isn't a strategy yet.

1. **Ambition** — one sentence linking AI to the business strategy. ("Free 20% of back-office capacity and redeploy it to same-day quoting, supporting the growth-without-hiring goal.")
2. **Where to play** — the 3–5 domains/processes chosen (from the prioritized portfolio, F3), and explicitly **where we will NOT invest this year**.
3. **How to win** — the client's unfair advantage in each domain (proprietary data, customer relationships, domain expertise) and the human+agent operating model principle (F4).
4. **Capability bets** — the 2–3 capabilities to build: data foundation, AI literacy, integration platform, agent ops.
5. **Targets** — 3–5 measurable outcomes with baseline → 12-month target (hours released, quote turnaround, error rate, NPS, revenue/FTE).
6. **Guardrails** — risk appetite, human-in-the-loop rules, budget envelope, EU AI Act posture (F6).

## Build / buy / assemble decision rule

For each priority use case:

- **Buy** (SaaS with AI inside) when the process is generic (accounting, scheduling, transcription) — speed beats control.
- **Assemble** (Claude/LLM + existing tools + automation platform like Make/Zapier/Power Automate) when the process is client-specific but the components are commodity. **Default for SMEs and for 80% of corporate back-office cases.**
- **Build** (custom development) only when the use case is core to competitive advantage AND volume justifies it. Rare below enterprise scale.

## Roadmap principles (12–18 months)

- **Wave 1 (Q1): prove.** 2–3 pilots from P1/P2, one visible to many employees (adoption energy), one with hard € value (sponsor energy).
- **Wave 2 (Q2–3): embed.** Scale winners, redesign the affected roles/processes (F4), start data fixes surfaced in Phase 1.
- **Wave 3 (Q4+): extend.** P3/P4 use cases, agentic processes with wider autonomy, offering innovation.
- Every wave carries **capability actions** (training, data, governance) alongside use cases — the roadmap has two swim-lanes minimum.
- Kill criteria are written **into** the roadmap: every initiative has a review date and a metric that decides scale/iterate/kill.

## Business case discipline

Per top use case, a one-pager: baseline (hours × frequency × loaded cost, error cost, revenue leakage) → expected impact range (conservative/expected) → costs (tools, integration, training, YOUR time) → payback period. Rules:

- Use the client's own numbers from the intake/inventory; ranges, not false precision.
- Count **capacity released**, and force the sponsor to decide what the capacity becomes (billable work, growth, reduced overtime, reduced hiring) — unallocated "savings" never materialize.
- SME sanity check: if payback > 6 months, it's probably the wrong first use case.
