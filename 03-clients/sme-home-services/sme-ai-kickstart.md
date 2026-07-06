# SME AI Kickstart — 5-Session Playbook (Home Services)

The compressed engagement for KMO's in home services (HVAC, sanitair, elektro, renovatie, cleaning, tuin…): **5 sessions over ~6 weeks**, same frameworks and prompts as the full flow, lighter deliverables. Priced as a fixed package; optional monthly retainer afterwards.

## Package shape

| Session | With | Length | Between sessions (you + Claude) |
|---|---|---|---|
| S1 Intake & scan | Owner (+office lead) | 90' | Context doc (Prompt 0.1), mini maturity scan (1.2 SME mode), pain inventory (1.3) |
| S2 Choose | Owner + key people | 2h workshop | Pre-scored candidates (2.2a with sector library below); after: portfolio + mini business cases (2.2b, 2.3) |
| S3 Design | Owner + affected staff | 2h | Task decomposition + who-does-what-now (3.1 lite), agent specs (4.2), policy draft (6.1 SME) |
| S4 Build & launch | Doers | half day hands-on | Pilot run kit (4.4); champions = whoever lit up in S4 |
| S5 Review & anchor | Owner + team | 90' | Scorecard (4.5), simple benefits tracker (6.5), next-wave list, handover |

Change management is **woven in**, not a phase: the owner tells the story in S2 (draft it with Prompt 5.1 — 400-word version only), affected staff co-design in S3/S4 (that IS the Desire lever), training happens hands-on in S4 (that's the AI-literacy artifact too — keep the attendance record), reinforcement = S5's anchor decisions (what old way gets switched off).

## Deliverables (the SME set)

1. Client context doc (2 p) 2. Mini maturity scan (6 bars + narrative, 1 p) 3. Pain & process inventory (2 p) 4. Chosen use cases + one-page business case each (payback < 6 months or pick again) 5. Who-does-what-now table (HAA lite + updated task list per person — the SME "organigram": usually role shifts, not new boxes) 6. Agent/automation specs incl. system prompts & 10 golden test cases 7. 2-page AI policy in plain {{NL/FR}} 8. Pilot scorecard 9. Benefits one-pager + next-wave list

Org-design note: below ~25 FTE, skip organigram options A/B/C. Use Prompt 3.1 + the role-card WIIFM paragraphs only; the structural decision is usually singular ("office admin becomes customer-coordinator who owns the agents"). The **AI Lead hat** goes to the owner or office lead; the "builder" is typically you on retainer or a local no-code partner.

## Home-services use-case library (feed into Prompt 2.2a as [SECTOR PATTERN])

**Lead & sales**
- Missed-call/voicemail-to-SMS agent + auto-callback booking (missed calls = missed jobs; often the #1 leak)
- Website/WhatsApp intake agent that asks the triage questions (photos!, location, urgency) and creates a structured lead
- Quote drafting agent: site-visit voice notes + photos → draft quote in the client's price book & tone (T1: owner reviews) — attacks the visit-to-quote delay that kills win rates
- Quote follow-up automation: polite chase sequence at day 3/7/14 with owner-approved wording

**Planning & field**
- Dispatch assistant: constraint-aware day planning suggestions (skills, zones, urgencies) inside their existing planning tool
- Job-prep pack agent: for tomorrow's jobs, auto-compile history, materials, access notes, parking
- Voice-note job reports: technician dictates 60 seconds → structured report + materials used + follow-up flags (kills evening paperwork — the #1 loved win with field staff)
- Photo-based first diagnosis support & spare-part identification (T1, technician judgment stays)

**Back office & cash**
- Job-report → draft invoice automation same day (cuts invoicing delay → cash)
- Payment-reminder sequence with escalation to human at step 3
- Inbox triage agent: classify (new lead / planning change / invoice question / complaint), draft replies (T1→T2)
- Supplier-invoice data extraction into accounting

**Customer & growth**
- Review-request automation post-job + review-response drafting agent
- Maintenance-contract reminder engine (recurring revenue from the install base — a P3 growth case hiding in every service SME)
- FAQ/knowledge agent for the office ("what did we install at Peeters in 2022?") once data is captured

**Boring-but-gold enablers**: getting job data digital via the voice-note pattern usually unlocks half the list — sequence it first when the maturity scan shows paper processes.

## SME-specific coaching notes

- **The owner IS the change program.** If the owner doesn't use the tools visibly, nobody will. Put one owner-personal use case in wave 1 (e.g., quote drafting) — their enthusiasm is the comms plan.
- **One family, one WhatsApp group, no works council** (usually): messaging rules still apply — the fear of "am I being replaced?" hits the office admin hardest; have the role-shift conversation (role card WIIFM) *before* the team announcement.
- **Payback < 6 months** or don't start (F2 rule). Typical winning first pilots: voice-note job reports, quote drafting, missed-call capture.
- **Stack bias**: their existing sector tool (e.g., planning/field-service software) + WhatsApp Business + accounting tool + one LLM workspace + Make/Zapier. Check the sector tool's native AI features FIRST — an activation beats an integration.
- **Belgium**: kmo-portefeuille registration as dienstverlener is pending (see 04-marketing/LAUNCH-CHECKLIST.md A3b) — until it's done, no subsidy claims in any prospect conversation; once registered, it materially improves the pricing conversation and comes back into the copy.
- **Retainer offer at S5**: monthly half-day — quality sampling with the agent owner, one improvement, one new automation; quarterly re-run of the benefits one-pager. This is where the relationship compounds.
