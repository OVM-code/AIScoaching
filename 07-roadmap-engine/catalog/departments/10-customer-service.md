# 10 — Customer service (CS)

Rarely a formal department in an SME — it's the office inbox and whoever picks up
the phone. Language-heavy, pattern-based, high volume: structurally the strongest
agent territory in the whole catalog (F4), and equally the fastest way to damage
trust when an agent answers wrong. Consultant-side authoring source; adapt per
client.

## CS.010 — Inbox & call triage
- **Typical AS-IS:** one shared inbox (or worse, personal ones) mixing leads, planning changes, invoice questions and complaints; oldest-first handling; phone interrupts everything.
- **Value leaks:** `wait` (urgent items buried under routine), `skill-bottleneck` (only experienced staff route correctly).
- **Opportunity patterns:** triage agent classifying and routing mail with draft replies (agent-T1 → T2 as accuracy is proven — the canonical inbox case); after-hours voicemail transcription and ticketing (automation). Caveat: measure misroute cost honestly; keep a human sweep of the "low confidence" queue from day one.

## CS.020 — Answer status questions
- **Typical AS-IS:** "where is my order / when is the technician coming?" — the office asks planning, planning asks the field, the customer waits a day for a one-line answer.
- **Value leaks:** `no-visibility` (the answer isn't in any system the front line can see), `wait` (customer and staff both idle in the relay chain).
- **Opportunity patterns:** proactive status notifications at milestones (automation — removes the question); status-lookup agent over planning/track data for the rest (agent-T2). Caveat: proactive beats reactive — if notifications kill 70% of these questions, build those first and the agent case shrinks honestly.

## CS.030 — Complaint intake & resolution
- **Typical AS-IS:** complaints arrive emotionally by phone; noted on a post-it; resolution depends on who took the call; no register, no pattern learning.
- **Value leaks:** `error` (recurring root causes never fixed), `chase` (customer must call twice to get movement), `no-visibility` (management sees no complaint trends).
- **Opportunity patterns:** structured intake + registration from call notes/mail (agent-T1); monthly root-cause pattern report (agent-T2); resolution-deadline watchdog (automation). Caveat: the empathetic conversation and the goodwill decision stay human per F4 — automate the memory, not the apology.

## CS.040 — FAQ & product information
- **Typical AS-IS:** the same twenty questions answered individually, well by veterans and shakily by new staff; knowledge undocumented ("what did we install at Peeters in 2022?").
- **Value leaks:** `skill-bottleneck` (answers depend on tenure), `retype` (same answer composed hundreds of times).
- **Opportunity patterns:** internal knowledge agent over product docs and job history for staff (agent-T2); curated public FAQ + website chat (agent-T1 for outbound). Caveat: the knowledge base must be built and owned first — an agent over tribal knowledge hallucinates; capture is the real project (ties to MGT.070).

## CS.050 — Appointment scheduling & changes
- **Typical AS-IS:** appointments made by phone ping-pong ("does Tuesday work? no? Thursday?"); changes cascade manually into planning; no-shows unmanaged.
- **Value leaks:** `wait` (multi-day ping-pong per appointment), `chase` (confirmation and reminder calls).
- **Opportunity patterns:** self-service booking within planner-approved slots + reminder sequence (automation); rescheduling agent handling change requests conversationally (agent-T2). Caveat: booking rules must encode real constraints (zones, skills, job length) or self-service creates planning chaos — pilot with one appointment type.

## CS.060 — Customer master data changes
- **Typical AS-IS:** address/contact/VAT changes arrive by mail and get applied to one system out of three; invoices bounce months later.
- **Value leaks:** `retype` (same change entered multiple times), `error` (systems drift apart; wrong invoices).
- **Opportunity patterns:** change-request extraction + apply-to-all-systems workflow (hybrid: agent-T1 extraction, automation propagation); periodic VAT-number validation against VIES (automation). Caveat: fix the "which system is master?" question first (IT.030) — propagating into ambiguity multiplies the mess.

## CS.070 — Escalation to experts & other departments
- **Typical AS-IS:** technical or commercial questions forwarded to the busy expert; the thread dies in their inbox; the customer calls back angry; front line can't answer follow-ups.
- **Value leaks:** `wait` (expert bottleneck), `skill-bottleneck` (knowledge never transfers back to the front line).
- **Opportunity patterns:** escalation tracker with SLA nudges (automation); answer-capture loop that turns each expert reply into a reusable knowledge entry (agent-T1, feeds CS.040). Caveat: the capture loop is the compounding win — position the tracker as the vehicle, the knowledge base as the prize.

## CS.080 — Customer satisfaction follow-up
- **Typical AS-IS:** satisfaction assumed from the absence of complaints; no measurement; silent churn discovered when the customer is already gone.
- **Value leaks:** `no-visibility` (churn signals unseen), `chase` (follow-up calls planned, never made).
- **Opportunity patterns:** post-job micro-survey automation (ties to MKT.060 review flow); churn-signal digest — ordering frequency drops, complaint history (agent-T2). Caveat: only measure what someone will act on; an unread NPS dashboard is negative ROI.
