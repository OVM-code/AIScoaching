# Phase 2 — AI Strategy & Business Case (Week 3–5)

**Goal:** choices. A strategy-on-a-page the exec team signs, a scored use-case portfolio with an explicit discard list, business cases for the top picks, and a two-lane roadmap.

**Gate G2:** strategy approved, wave-1 use cases and budget envelope agreed.

**Upload to Project:** `F2-ai-strategy.md`, `F3-use-case-prioritization.md` (keep F1 outputs in the context doc).

## Activities

1. Generate use-case candidates (Prompt 2.2a) → prioritization **workshop** (format in F3) where the client scores.
2. Draft strategy-on-a-page (Prompt 2.1) → pressure-test with sponsor 1:1 before the exec meeting.
3. Business cases for wave-1 picks (Prompt 2.3).
4. Roadmap (Prompt 2.4) and readout (Prompt 2.5) → Gate G2.

## Deliverables: D8 strategy-on-a-page · D9 use-case portfolio · D10 business cases · D11 roadmap · D12 readout deck

---

## PROMPT 2.1 — Strategy-on-a-page (D8)

```
Using client-context.md and framework F2, draft the AI strategy-on-a-page for
this client. Follow F2's six blocks exactly (Ambition / Where to play / How to
win / Capability bets / Targets / Guardrails).

Constraints:
- Ambition must link explicitly to their stated top-3 priorities, in language
  echoing their own words (use the verbatims)
- Where-to-play must include a "NOT this year" list of at least 3 items
- Targets: 3-5, each with baseline from the Phase-1 inventory (or [BASELINE
  NEEDED]) and a 12-month target range
- How-to-win must name their genuinely defensible assets (proprietary data,
  relationships, expertise) — challenge me if you don't see any real ones
- One page. Then a second section "Rationale & alternatives considered" (max
  1 page) I can use to defend it, including the strongest objection you expect
  from this exec team and my counter.

Also give me 3 sharp questions to pressure-test the ambition with the sponsor
before the exec meeting.
```

## PROMPT 2.2a — Use-case candidate generation (pre-workshop)

```
Using client-context.md (especially the pain-point inventory and top-10 list)
and framework F3, generate the use-case candidate long-list for this client.

- 15-25 candidates, each one line: verb + object + mechanism (F3 format), plus
  value pool (P1-P4), affected roles, and the pain point(s) it addresses
- Include: candidates for every top-10 pain; the demand signals from shadow-AI
  usage; 2-3 candidates from what similar companies in their sector typically
  do that they did NOT mention (mark [SECTOR PATTERN]); at least 2 candidates
  in pools P3/P4 (growth/new offerings)
- Exclude and list separately: "AI won't fix this" items (structural issues
  from D5)

Then pre-score every candidate per F3's Value and Feasibility criteria and
weights, with one-line justifications per score, and plot them into the four
quadrants. Mark scores where you lack evidence with "?" — those become
workshop questions. This is a DRAFT for the client to challenge in the
workshop, so make the justifications assertive enough to argue with.
```

## PROMPT 2.2b — Portfolio write-up after the workshop (D9)

```
Below are the scoring decisions from the client prioritization workshop
(including changed scores and their arguments). Produce the final use-case
portfolio document:

1. Quadrant map (list per quadrant, final scores)
2. Wave-1 picks (the chosen 2-3) with: owner, one-paragraph description,
   affected roles, primary metric, why-now
3. Big bets parked for wave 2/3, each with its required enabler
4. The discard list with the one-line reason each ("not this year because…")
5. Changes vs. my pre-scored draft and what the client's arguments reveal
   about their priorities (useful intelligence for me as coach)

WORKSHOP RESULTS: {{PASTE SCORES/DECISIONS/PHOTOS-TRANSCRIBED}}
```

## PROMPT 2.3 — Business case per wave-1 use case (D10)

```
Using client-context.md, framework F2 (business-case discipline section), and
the portfolio (D9), build a one-page business case for use case:
"{{USE CASE NAME}}".

Structure:
1. Baseline: current volume × time × loaded cost, error/leakage costs — use
   the inventory numbers; every number tagged [SOURCE: interview/survey/
   estimate+reasoning]
2. Impact: conservative and expected scenarios, with the mechanism spelled
   out (what stops being done, what gets faster, what improves)
3. Capacity dividend: hours released and the DECISION REQUIRED from the
   sponsor about their destination (offer 2-3 realistic options for this
   client: billable work / growth absorption / reduced hiring / overtime cut)
4. Costs: tools (realistic EU pricing, seats vs usage), integration effort,
   training time, my coaching time, ongoing run cost
5. Payback period, both scenarios; sensitivity: the one assumption that
   changes the answer most
6. Risks & the human-in-the-loop design in one paragraph (autonomy tier)

Numbers in EUR. Ranges over false precision. If payback exceeds 6 months
(SME) / 12 months (enterprise), say prominently that this may be the wrong
first pick and what would change the math.
```

## PROMPT 2.4 — Roadmap (D11)

```
Using the strategy (D8), portfolio (D9) and framework F2's roadmap principles,
draft the 12-18 month roadmap:

- Two swim-lanes minimum: (1) use cases per wave, (2) capability actions
  (data fixes from D6's remediation backlog, training per F5 preview,
  governance milestones). Add a third lane "Org & change" with the Phase 3-5
  milestones.
- Per initiative: owner, start/duration, dependency arrows (text form),
  review date + the metric that decides scale/iterate/kill
- Wave 1 must respect F3's rules (one visible + one hard-euro use case)
- Respect the client's hard deadlines and seasonality from the context doc
- Output as: (a) a quarter-by-quarter table, (b) a Mermaid gantt code block
  I can render

Then a "first 30 days" zoom: week-by-week actions with names.
```

## PROMPT 2.5 — Strategy readout deck (D12, Gate G2)

```
Using D8-D11 (pasted below or in this Project), draft the Gate-G2 exec deck,
max 10 slides, outline + speaker notes:

1. Recap of G1 findings in 3 bullets 2. The strategy-on-a-page 3. The
portfolio map with wave-1 picks 4. Business cases: one summary slide (table:
use case | investment | payback | capacity dividend decision needed) 5-6. The
roadmap + first 30 days 7. What this means for the organization (honest
preview of Phase 3: roles and structure WILL be touched; change principles)
8. Budget ask & governance of the program 9. Risks & how we manage them
10. Decisions asked today (list them explicitly: strategy sign-off, wave-1
approval, budget envelope, capacity-dividend directions)

The deck must force decisions, not admiration. Speaker notes in my coaching
voice, anticipating this exec team's most likely pushback (infer from the
stakeholder map).
```

## Wrap-up

Update `client-context.md`: add approved strategy summary, wave-1 picks + owners, budget, capacity-dividend decisions to the decisions log; phase → 3. Re-upload.
