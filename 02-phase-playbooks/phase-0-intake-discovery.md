# Phase 0 — Intake & Discovery (Week 0–1)

**Goal:** know the business, name the sponsor, produce the client-context doc that powers everything, and open the engagement with a kickoff that sets expectations.

**Gate G0:** signed engagement, sponsor named, `client-context.md` complete.

## Activities

1. Send intake questionnaire Part A ahead (`00-system/client-intake-questionnaire.md`).
2. Run the 60–90 min intake interview (Parts B–F). Record or take dense notes.
3. Generate `client-context.md` (Prompt 0.1), have sponsor validate facts.
4. Map stakeholders (Prompt 0.2).
5. Kickoff meeting with leadership (deck via Prompt 0.3).
6. Create the client's Claude Project; upload context + engagement flow.

## Deliverables: D1 client-context.md · D2 stakeholder map · D3 kickoff deck

---

## PROMPT 0.1 — Client context document (D1)

*Inputs: paste your raw intake notes/transcript. Output: the master `client-context.md`.*

> **Came in via the AI Strategy Preview?** (`04-marketing/assets/ai-strategy-preview.md`) Then a seed client-context already exists from Prompt P-C. Paste it below your intake notes and add to the prompt: "Merge with the seed context: keep its [CONFIRMED]/[CORRECTED] facts, resolve its [STILL UNKNOWN] items from my notes, and flag any contradiction between seed and intake." The intake interview then only needs the ⭐ questions still open in the seed.

```
You are helping me, an AI-integration coach, create the master context document
for a new client engagement. Below are my raw intake interview notes following
my standard questionnaire (business basics, operations & pain, systems & data,
AI today, people & change, engagement mechanics).

Produce a file called client-context.md with EXACTLY these sections:

1. Snapshot — name, locations, languages, what they do, for whom, headcount by
   function, revenue range, growth ambition
2. Strategy — top-3 priorities in their own words; what triggered this
   engagement; success definition for 12 months
3. Organization — current structure (describe the organigram in text), key
   leaders, works council yes/no, culture notes
4. Core processes — the end-to-end flow(s) in numbered steps, with pain points
   marked ⚠ and rough volumes/durations where I captured them
5. Systems & data — tool inventory (loved/hated), where knowledge lives, data
   trust level, existing automations
6. AI today — current usage (official + shadow), past attempts, sentiment,
   red lines
7. People & change — workforce profile, opinion leaders, past change history,
   appetite for org change, constraints
8. Engagement — sponsor, project lead, decision process, budget range,
   timeline, hard deadlines, confidentiality rules
9. Verbatims — 5-10 direct quotes (role attribution only, no names)
10. Open questions — what I still need to find out, ranked by importance
11. Engagement status — phase: 0; decisions log: (empty); last updated: {{DATE}}

Rules: only use information from my notes; never invent numbers; mark anything
uncertain with [VERIFY]; keep it under 3 pages; write in English regardless of
the notes' language but keep verbatims in the original language.

MY RAW NOTES:
{{PASTE NOTES}}
```

## PROMPT 0.2 — Stakeholder & power map (D2)

```
Using client-context.md (in this Project), create a stakeholder map for this
AI-integration engagement.

Output a table: Stakeholder (role) | Influence H/M/L | Current attitude toward
AI change (champion / supportive / neutral / skeptical / resistant, with your
evidence from the context doc) | What they win / what they fear | Engagement
strategy (specific: what I should do with this person in the next 30 days).

Then add:
- "Coalition": the 4-6 people who must be actively FOR this by Gate G2, and the
  single most effective move for each.
- "Watch list": people who could quietly kill this, and early-warning signs.
- 3 targeted questions I should ask to fill attitude gaps you're unsure about.

If the context doc lacks named roles, infer the standard roles for a business
of this type/size and mark them [ASSUMED - VERIFY].
```

## PROMPT 0.3 — Kickoff deck (D3)

```
Using client-context.md, draft a kickoff presentation for the leadership team
of this client. Slide-by-slide outline: title, 3-5 bullets, one concrete data
point or client verbatim where available, and speaker notes (2-3 sentences,
conversational, in my voice as their coach).

Slides:
1. Why now — their strategic priorities + what's changed in AI, in THEIR sector
2. What this engagement is (coach-led, their people do the choosing) and is NOT
   (a tool purchase, a headcount program, consultants doing it to them)
3. The journey — 7 phases with their expected calendar, gates where THEY decide
4. What good looks like in 12 months — 3 scenarios grounded in their stated
   success definition
5. How AI changes organizations — humans + automations + agents in one operating
   model, 2-3 sector-relevant examples (mark examples [ILLUSTRATIVE])
6. The people commitment — change principles: transparency, training first,
   involvement in design (align with my F5 framework if uploaded)
7. What I need from them — sponsor time, data access, workshop participation,
   decision speed
8. Next 2 weeks — assessment activities and who I'll talk to

Tone: confident, concrete, zero AI hype. Flag any slide where the context doc
leaves you guessing.
```

## Wrap-up

Update `client-context.md` §11 (phase → 1, log G0 decision) and re-upload to the Project.
