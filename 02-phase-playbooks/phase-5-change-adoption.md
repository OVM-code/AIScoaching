# Phase 5 — Change Management & Adoption (starts week 5, runs through the engagement)

**Goal:** the people side, run as a workstream in parallel from the moment strategy direction exists. Change story, ADKAR plan per persona, comms, training/AI literacy, champions, resistance handling, and an adoption dashboard.

**Not a gate but a rhythm:** monthly adoption review with the sponsor using the dashboard (F5 measurement section).

**Upload to Project:** `F5-change-management.md` (keep F4 for role-card links).

## Sequence

| When | Do |
|---|---|
| Week 5 (G2 passed) | Change story with leadership (Prompt 5.1, then a 90-min co-creation session); ADKAR baseline (5.2) |
| Week 6 | Comms calendar (5.3) starts; sponsor kicks off broad communication — before rumors outrun you |
| Week 6–8 | Training curriculum built (5.4); champions recruited (5.5) — recruit heavy shadow-AI users |
| Week 8+ (pilots) | Pilot teams trained first; resistance plan live (5.6); monthly dashboard |
| Gate G3/G4 moments | Workforce messaging per F5 §6 and D18 — sequenced, never improvised |

## Deliverables: D23 change story · D24 ADKAR plan · D25 comms calendar · D26 training curriculum · D27 champions network · D28 resistance plan

---

## PROMPT 5.1 — Change story & leadership narrative (D23)

```
Using client-context.md (verbatims!, strategy summary, people section) and F5,
draft the change story for this client:

1. The core narrative (max 400 words, spoken language, in {{LANGUAGE}}):
   why change, why now, where we're going, what stays the same, what it means
   for people, what we commit to. It must: use their own words from the
   verbatims; name the elephant (jobs) directly with the approved people-story
   from D18 (if not yet approved: [BLOCKED - people-story needed first, per
   F5 §6]); contain zero corporate filler or AI hype; be tellable by the
   sponsor in 3 minutes without slides.
2. Three variants of the same story: for managers (adds their role in it),
   for the most affected teams (adds specifics + support), for everyone else
3. The 10 hardest questions with honest answers (Q&A prep for leaders)
4. "Story test": 5 criteria the leadership team should check in the
   co-creation session, and where your draft is weakest.
```

## PROMPT 5.2 — ADKAR-based change plan (D24)

```
Using F5, client-context.md, the stakeholder map (D2), pulse-survey results,
and the org-redesign impact (D18 if available), build the change plan:

1. Persona table for THIS client (adapt F5's default set): persona | size |
   ADKAR state today (with evidence) | biggest barrier | primary lever
2. Per persona, the plan to move them one ADKAR state at a time: actions,
   owner (mostly line managers and sponsor — NOT me/comms), timing, and how
   we'll know it worked
3. The manager enablement kit list: what each people-manager needs (talking
   points, 1:1 conversation guide keyed to the role cards D16, FAQ)
4. Reinforcement design: what gets retired (old ways switched off, with
   dates), what gets rewarded (link to targets/bonus review from F4 step 6),
   monthly rituals
5. Risk heat: the 2-3 personas × moments where this program most likely
   stalls, and the pre-emptive move for each
```

## PROMPT 5.3 — Persona-based comms calendar (D25)

```
Using D23, D24 and the engagement roadmap (D11), create a 3-month rolling
comms calendar: week | audience/persona | message (one line, keyed to their
ADKAR state — awareness msgs for Awareness-stage groups, proof & WIIFM for
Desire, etc.) | channel (use THIS client's real channels from the context
doc: toolbox meetings, WhatsApp groups, intranet, town hall…) | sender (the
right messenger per F5 — sponsor for why, direct manager for what-it-means-
for-you, champions for how-to) | linked event (pilot start, G3 announcement,
training wave…)

Rules: sponsor repeats the core story at least monthly; every pilot
milestone becomes a story; nothing announced to all before affected teams
heard it face-to-face (F5 §6 sequencing); max 2 messages per persona per
week. Then draft the first 3 concrete pieces (e.g., sponsor townhall talking
points, team-meeting script for managers, pilot-kickoff message) in
{{LANGUAGE}}, in the client's tone.
```

## PROMPT 5.4 — Training curriculum & AI literacy program (D26)

```
Using client-context.md (workforce profile, skills gaps from D18), the role
cards (D16), and F5's layered-literacy note, design the training program:

Layers:
A) Everyone — AI literacy (also our EU AI Act Art. 4 artifact, say so):
   what AI is/isn't, the client's policy & sanctioned tools, verification
   habits & failure examples, data rules. 2-3 hours, format fitting THIS
   workforce (e.g., toolbox-talk style for field staff, not e-learning slides)
B) Power users / affected roles — per changed role from D16: hands-on with
   their actual agents and real work samples; includes judging & correcting
   agent output, not just prompting. Half-day + floor support.
C) Agent owners — prompt maintenance, eval-set testing, quality sampling,
   escalation handling (from D20 runbooks). 
D) Leaders — leading human+agent teams, reading the adoption dashboard,
   reinforcement behaviors. 2 hours.

Per layer: objectives, agenda, materials list, who delivers (me / champions /
external), duration, schedule proposal aligned to the pilot/rollout calendar,
and the proficiency check (what they must demonstrate — no attendance-only).
Add: protected practice-time recommendation per F5 Ability, and the training
record format (compliance evidence).
```

## PROMPT 5.5 — Champions network (D27)

```
Using client-context.md, D2 (stakeholder map) and pulse results, design the
champions network:

1. Sizing & placement: 1 per team/site — list the actual teams and the
   profile to recruit in each (name candidates if the context identifies
   power users/opinion leaders, incl. heavy shadow-AI users)
2. The deal: role description (first-line help, feedback channel, story
   collector), time budget (2-4 h/wk), what they get (first access, training
   layer C, visibility, input into tool choices — for THIS client's culture
   suggest the recognition that will actually work)
3. Operating rhythm: bi-weekly champion sync agenda, feedback loop into the
   pilot reviews and my backlog
4. Recruitment approach: how managers nominate + self-nomination, the
   invitation message draft
5. Failure modes to design against (champion = extra unpaid job; champions
   drift into being the only users; manager bypass)
```

## PROMPT 5.6 — Resistance management plan (D28)

```
Using F5's resistance section, D2, D24, and any resistance signals I paste
below, build the resistance plan:

1. Signal inventory: current resistance signals, each diagnosed by source
   (job fear / skill anxiety / autonomy-status / output distrust / change
   fatigue / genuine flaw detection) with evidence
2. Response per signal following F5's escalation ladder — specific: who has
   which conversation, what involvement is offered, what blocker gets fixed
3. The genuine-flaw channel: how skeptics' valid findings enter the pilot
   backlog visibly (name the mechanism)
4. Middle-manager focus: per F5, the specific plan for the managers most
   affected by span/role changes in D15
5. Escalation criteria: when a case goes to the sponsor, and the
   expectation-setting script for the (rare) last-resort conversation

SIGNALS OBSERVED: {{PASTE}}
```

## Monthly adoption dashboard

Reuse Prompt 4.4's metrics structure at program level: usage, proficiency, sentiment pulse, old-way volume, outcomes. Ask Claude monthly: *"Here's this month's adoption data + last month's dashboard — produce the trend dashboard, the 3 attention points, and the one action per attention point."*
