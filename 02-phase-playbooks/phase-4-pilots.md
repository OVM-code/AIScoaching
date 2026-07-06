# Phase 4 — Pilot Design & Execution (Week 8–14)

**Goal:** prove value on the wave-1 use cases in 60–90 days, with clean baselines, honest scorecards, and a scale/iterate/kill decision per pilot.

**Gate G4:** per pilot, an explicit decision against pre-agreed criteria.

**Upload to Project:** keep F4; add `F6-governance-risk-eu-ai-act.md` (tool selection + risk checks happen here).

## Activities

1. Pilot charter per use case (Prompt 4.1) — signed by the pilot owner before anything is built.
2. Agent/automation spec (Prompt 4.2) → build (client builder, your retainer, or a no-code session with the team).
3. Tool selection where needed (Prompt 4.3) + F6 §2 deployer checklist per pilot **before** go-live.
4. Run 4–8 weeks with weekly 30-min pilot reviews (Prompt 4.4 generates the review rhythm + dashboard).
5. Scorecard + retro (Prompt 4.5) → G4 decision meeting.

## Deliverables: D19 pilot charters · D20 agent/automation specs · D21 tool selection matrix · D22 scorecards & retros

## Pilot rules (enforce these)

- **Baseline before build.** One week of measurement of the old way if numbers are shaky.
- **Real work, small scope.** One team/branch/customer-segment, production tasks, not lab demos.
- **The affected team co-builds.** Especially prompt-writing — experts teaching the agent converts skeptics (F5 identity lever).
- **Kill criteria are written before the pilot starts** and honored at G4. A killed pilot with a clean retro is a success of the system.

---

## PROMPT 4.1 — Pilot charter (D19)

```
Using client-context.md, the business case (D10) for "{{USE CASE}}", and the
task decomposition (D13), draft the pilot charter, max 2 pages:

1. Objective & hypothesis ("we believe that X will reduce/improve Y by Z%")
2. Scope: team/location/volume in, everything else out
3. Baseline: current metrics + how we measure them this week if missing
4. Success criteria (numbers) AND kill criteria (numbers + date), pre-agreed
5. Design summary: target flow (H/A/Agent per step from D13), autonomy tier,
   human-in-the-loop points
6. Roles: pilot owner (line, not IT), agent owner, builder, my role, exec
   sponsor; time commitment each
7. Timeline: build (wk 1-2) → shakedown (wk 3) → measured run (wk 4-8) →
   scorecard; weekly review slot
8. Risk & compliance quick-check per F6 §2 deployer checklist (prohibited?
   high-risk? disclosure? personal data → GDPR actions?)
9. What we tell the wider organization and when (link to comms calendar D25)
```

## PROMPT 4.2 — Agent / automation spec (D20)

```
Using the pilot charter for "{{USE CASE}}" and F4, write the build spec:

1. Flow diagram (Mermaid) of the target process: triggers, inputs, the
   agent/automation steps, human touchpoints, outputs, exceptions path
2. For each AGENT component:
   - Job statement & autonomy tier, promotion criteria to next tier
   - The full SYSTEM PROMPT draft, personalized from client-context.md:
     role, the client's tone of voice (derive from verbatims/website),
     domain rules, output format, refusal rules ("if X, hand to human"),
     the client's terminology in {{LANGUAGE}}
   - Eval set: 10-15 golden test cases (input → expected output) drawn from
     the real examples I paste below; include 3 adversarial/edge cases
   - Data it may access (minimum necessary — GDPR minimization) and data it
     must never see
3. For each AUTOMATION component: trigger, steps, systems & connection
   method (from D6's systems map), error handling, notification rules
4. Build approach recommendation for THIS client's stack and skills:
   what to build it IN (their existing tools first, then Claude Projects /
   automation platform / native features), estimated build effort
5. Runbook v0: who fixes what when it breaks, quality sampling routine for
   the agent owner, weekly metrics to log

REAL EXAMPLES FOR EVAL SET: {{PASTE 5-10 real inputs, e.g., actual customer
emails / site notes — anonymized}}
```

## PROMPT 4.3 — Tool & vendor selection matrix (D21)

```
Using client-context.md (systems, budget), D6, and F6 §5 scoring dimensions,
compare tool options for "{{CAPABILITY, e.g., LLM workspace / dispatch
software with AI / voice agent}}":

Candidates: {{LIST — or ask me and propose the standard EU-suitable
candidates for this capability and client size}}

Output: scoring matrix per F6 §5 weights with justifications; total cost at
realistic volume for this client (seats vs usage, EUR, year 1 and year 2);
data-protection notes per candidate (DPA, EU processing, no-training terms —
mark [VERIFY CURRENT TERMS], as vendor terms change); integration fit with
their named stack; exit-ability. Recommendation + what would change it.
Default bias per F6: existing paid tools first, specialize only on proven gaps.
```

## PROMPT 4.4 — Pilot run kit (dashboard + weekly review)

```
For pilot "{{USE CASE}}" (charter pasted/in Project), create the run kit:

1. A metrics log template (table) the pilot owner fills weekly: volume through
   new path, old-way volume, time per unit, quality/error samples, user
   sentiment 1-5, incidents; each with its collection method (keep it under
   10 min/week of logging effort)
2. The weekly 30-min review agenda: metrics vs. plan, top friction, agent
   quality sample review (3 outputs together), one improvement to ship this
   week, escalations
3. A mid-pilot pulse: 4 questions for the pilot team
4. Early-warning signs specific to this pilot's design (e.g., secret double
   work, cherry-picking easy cases into the new path — say how each would
   show up in the metrics)
```

## PROMPT 4.5 — Scorecard & retro (D22, Gate G4)

```
Pilot "{{USE CASE}}" measured run is complete. Below: the weekly metrics log,
incidents, and pulse results. Produce:

1. Scorecard: results vs. success AND kill criteria, one page, no spin —
   traffic light per criterion with the number
2. Business-case check: actuals vs. the D10 conservative/expected scenarios;
   updated payback
3. Retro (what worked / what didn't / what surprised), including change &
   adoption observations for F5 (who leaned in, who resisted, why)
4. Recommendation: SCALE (with the scale plan: rollout order, org changes
   from D14/D15 this activates, training needs, run-cost at scale) or
   ITERATE (what changes, new review date) or KILL (what we learned, what
   the pain point needs instead)
5. The G4 decision slide: one slide, decision question, evidence, recommendation

DATA: {{PASTE metrics log, incidents, pulse}}
```

## Wrap-up

Update `client-context.md`: pilot outcomes + G4 decisions → decisions log; phase → 5/6. Re-upload.
