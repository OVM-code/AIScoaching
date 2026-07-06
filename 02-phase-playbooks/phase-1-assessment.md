# Phase 1 — AI Maturity & Opportunity Assessment (Week 1–3)

**Goal:** an evidence-based picture of where the client stands (F1 maturity scan), where the pain and value sit (process inventory), and whether data/systems can carry the likely use cases.

**Gate G1:** leadership validates the maturity picture + top-10 pain points and commits to strategy work.

**Upload to Project for this phase:** `F1-ai-maturity-scan.md`.

## Activities

1. Staff pulse survey (Prompt 1.1 generates it) — anonymous, 10 questions, 5 min.
2. Role interviews: 3–6 (SME) to 10–15 (enterprise, spread over BUs). 45 min each, focused on Parts B–D of the intake questionnaire at team level.
3. System walk-through: screen-share the real ERP/CRM/planning tool on a real transaction.
4. Score the maturity scan (Prompt 1.2), build the inventories (1.3, 1.4).
5. Readout with leadership (deck via Prompt 1.5) → Gate G1.

## Deliverables: D4 maturity scan · D5 process & pain-point inventory · D6 data readiness report · D7 readout deck

---

## PROMPT 1.1 — Pulse survey + interview guides

```
Using client-context.md and framework F1 (both in this Project), create:

A) An anonymous staff pulse survey, max 10 questions, 5 minutes, in
   {{LANGUAGE}}, phrased for this client's workforce profile. Must measure:
   current AI tool usage (official AND private — phrase it so it's safe to
   admit), perceived usefulness, fear level (job security, monitoring),
   appetite to learn, top time-wasters in their own work. Mix multiple choice
   with 2 open questions. Add a 2-sentence intro from leadership that
   guarantees anonymity and explains why we ask.

B) A 45-minute interview guide per function I list below, tailored to what
   each function does in THIS client (use the core-process section of the
   context doc). Each guide: 8-10 questions covering their slice of the
   process, hours per task, error hotspots, systems friction, current AI use,
   and what they'd never want automated. End with the magic-wand question.

Functions to cover: {{LIST FUNCTIONS, e.g., field technicians, planners,
back office, sales, finance}}
```

## PROMPT 1.2 — Maturity scan report (D4)

```
Using framework F1 and client-context.md, score this client's AI maturity.
Below I paste my evidence: interview notes, pulse-survey results, and
system walk-through observations.

Produce the maturity scan report:
1. Score table: 6 dimensions × score (1 decimal) × one-line justification
2. Per dimension (short section each): evidence (2-3 concrete observations,
   quote the survey numbers where relevant) · constraint analysis (which
   likely use-case types this blocks or enables) · 1-2 fastest-rising moves
3. The binding constraint: the ONE dimension capping everything, and why
4. Profile interpretation: what the SHAPE of this profile says (per F1)
5. Data for a spider chart (dimension: score list I can paste into a chart)
6. 5 headline findings written as punchy readout statements, each anchored
   to a number or verbatim

Follow F1's scoring rules strictly (a level requires all evidence of the level
below). Score what IS, not what's planned. Mark inference beyond my evidence
as [INFERRED].

EVIDENCE:
{{PASTE INTERVIEW NOTES / SURVEY RESULTS / OBSERVATIONS}}
```

## PROMPT 1.3 — Process & pain-point inventory (D5)

```
Using client-context.md plus the evidence I pasted in this conversation (or
pasted below), build the process & pain-point inventory.

For each core process (use the context doc's process list; add ones surfaced
in interviews): a table of steps with columns —
Step | Who does it today | Systems touched | Est. volume & time (use my
numbers; [ESTIMATE] with reasoning if extrapolating) | Pain (⚠ to ⚠⚠⚠) |
Pain type (retype/chase/wait/error/skill-bottleneck/no-visibility) |
First-look automability (Human-only / Automation / Agent / Hybrid — per the
HAA logic: rules-based → automation, language & judgment-lite → agent)

Then:
- Top-10 pain points ranked by (hours burned × error cost × strategic
  relevance), each with a one-line value hypothesis ("if fixed → X")
- Quick-win candidates: pains fixable in <30 days with existing tools
- Structural issues: pains that are org/process problems AI won't fix
  (be honest — these go to the org-redesign phase, not the tool list)
```

## PROMPT 1.4 — Data & tooling readiness report (D6)

```
Using client-context.md (systems section) and my walk-through notes below,
write the data & tooling readiness report:

1. Systems map: each system, what data it holds, integration options (native
   API / export only / vendor-locked / unknown-[VERIFY]), and whether the
   client's tier includes API access
2. Data readiness per likely use-case family (drafting & comms, scheduling,
   quoting, invoicing/finance, customer service, analytics): traffic light +
   what's missing
3. The "knowledge in heads" problem: what critical know-how is undocumented,
   and which of it the priority use cases would need captured
4. Security & access baseline: SSO? shared logins? where would an AI tool
   plug in safely? red flags
5. Remediation backlog: fixes ranked by (unblocks-value ÷ effort), each with
   an owner suggestion and rough effort (days)

WALK-THROUGH NOTES: {{PASTE}}
```

## PROMPT 1.5 — Assessment readout deck (D7, Gate G1)

```
Using the maturity scan, inventory, and readiness report generated in this
Project's conversations (I paste the final versions below), draft the Gate-G1
readout deck for leadership. Slide outline with speaker notes, 10 slides max:

1. What we did (evidence base: N interviews, N survey responses, systems seen)
2. Maturity picture — spider chart data + the one-sentence story
3-4. The pain, in their numbers — top-10 pain points with hours/€ and verbatims
5. Where the value likely sits — pain clusters mapped to the 4 value pools (F2
   preview), with rough sizing ranges [ESTIMATE]
6. What's ready and what's not — data/tooling traffic lights + binding constraint
7. What their people said — survey highlights incl. shadow-AI usage and fear
   levels, framed constructively
8. Honest slide — what AI will NOT fix here (structural issues)
9. Recommendation — proceed to strategy phase, scope, focus areas
10. Decision asked + next steps

Rule: every claim traceable to the evidence; hype-free; end with the explicit
G1 decision question.

FINAL DELIVERABLES: {{PASTE D4, D5, D6}}
```

## Wrap-up

Update `client-context.md`: append maturity scores + top-10 pains to §4-6, set phase → 2, log the G1 decision. Re-upload.
