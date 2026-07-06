# F3 — Use-Case Prioritization

Turns the Phase 1 pain-point inventory into a scored, sequenced portfolio. Designed to be run as a **workshop where the client scores** (ownership!) with a Claude-generated pre-scored draft as the starting point.

## Step 1 — Generate candidates

Sources: pain-point inventory (D5), value pools (F2), sector pattern libraries (see phase playbooks and SME playbook), shadow-AI usage discovered in P1 (what people already do privately is a demand signal).

Write each candidate on one line: **verb + object + mechanism** — "Draft quotes from site-visit photos and notes using an LLM assistant", not "AI for sales".

## Step 2 — Score: Value × Feasibility, tie-broken by Adoption

Each axis 1–5. Defaults below; adjust weights per client and say so in the deliverable.

**Value (weighted avg):**
| Criterion | Weight | 5 looks like |
|---|---|---|
| Hours released or revenue impact | 50% | >0.5 FTE equivalent or clear revenue lever |
| Quality/risk reduction | 25% | Eliminates a recurring costly error class |
| Strategic fit | 25% | Directly serves a stated top-3 priority |

**Feasibility (weighted avg):**
| Criterion | Weight | 5 looks like |
|---|---|---|
| Data & system readiness | 40% | Data digital, accessible, decent quality |
| Technical simplicity | 30% | Buy or assemble; no custom build |
| Process stability & ownership | 30% | Explicit process, named owner, low exception rate |

**Adoption ease (tie-breaker, 1–5):** Will the affected people welcome it? Removing hated work scores 5; touching work people identify with scores 1–2.

## Step 3 — Portfolio map

Plot Value × Feasibility into four quadrants:

| | Low feasibility | High feasibility |
|---|---|---|
| **High value** | **BIG BETS** — roadmap wave 2/3; start enablers now | **QUICK WINS** — pilot in wave 1 |
| **Low value** | **DISCARD** — write them down and say no | **FILL-INS** — do only if a champion volunteers to own one |

Portfolio rules:
- Wave 1 = 2–3 quick wins max (SME: 1–2). One must be *widely visible*, one must have *hard € value*. Ideally at least one removes work people hate (adoption energy).
- Every big bet gets its **enabler** (data fix, integration, skill) placed on the roadmap now.
- The discard list is presented explicitly — saying "not this year" out loud is half the value of the exercise.

## Step 4 — Pilot definition (feeds Phase 4)

Each wave-1 use case gets a charter: owner, affected roles, baseline metric, target metric, tool approach (buy/assemble/build), human-in-the-loop design, 60–90 day timeline, kill criteria. Template in Prompt 4.1.

## Workshop format (2.5h)

1. (15') Recap value pools & strategy ambition.
2. (30') Present candidate list; participants add/merge; each candidate gets an owner-of-the-line.
3. (45') Score in small groups (pre-scored Claude draft as challenge baseline — "we scored this 4 on value, convince us otherwise").
4. (30') Plot, debate the top 8, apply portfolio rules.
5. (30') Commit: wave-1 picks, named owners, discard list read aloud.
