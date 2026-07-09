# 05 — Field service & execution (SVC)

Technicians on the road: interventions, installations, maintenance rounds. The craft
work is human by definition (F4); the leaks sit in intake, dispatch and the paper
trail around each visit. Voice-note job reports are the single most-loved win with
field staff. Consultant-side authoring source; adapt per client.

## SVC.010 — Service request intake & triage
- **Typical AS-IS:** requests arrive by phone/mail/WhatsApp to the office; urgency judged by whoever answers; details incomplete, so technicians drive out half-informed.
- **Value leaks:** `wait` (requests sit in a mailbox), `error` (wrong urgency, missing info → wasted trips).
- **Opportunity patterns:** intake agent asking the triage questions — photos, location, symptom, urgency — and creating a structured ticket (agent-T2); missed-call capture after hours (automation, ties to SAL.010). Caveat: define the escalation rule for genuine emergencies explicitly — a gas leak must never wait on a bot.

## SVC.020 — Dispatch & route planning
- **Typical AS-IS:** dispatcher assigns jobs each morning balancing skills, zones and urgencies from experience; the schedule dies by 10:00 and is repaired by phone.
- **Value leaks:** `skill-bottleneck` (dispatch = one irreplaceable person), `error` (wrong tech/parts sent, criss-cross driving).
- **Opportunity patterns:** constraint-aware day-planning suggestions inside the existing planning tool (agent-T1 — dispatcher decides); automated customer ETA messages (automation). Caveat: check the field-service tool's native optimizer first; keep the dispatcher as owner, this is assist not replace.

## SVC.030 — Job preparation pack
- **Typical AS-IS:** technician discovers on arrival what was installed before; history in the office system, parking/access knowledge in colleagues' heads.
- **Value leaks:** `chase` (calls to the office for history), `wait` (second visit because the right part wasn't on the van).
- **Opportunity patterns:** auto-compiled prep pack for tomorrow's jobs — history, materials, access notes (agent-T2, high adoption); parts-suggestion from symptom + installed-base data (agent-T1). Caveat: depends on installed-base data quality — often the enabler project comes first.

## SVC.040 — On-site execution & diagnosis
- **Typical AS-IS:** the craft itself: diagnose, repair, install. Experienced techs solve fast; juniors call seniors or return with the job unfinished.
- **Value leaks:** `skill-bottleneck` (senior knowledge doesn't scale; first-time-fix rate suffers).
- **Opportunity patterns:** photo-based first-diagnosis support and spare-part identification (agent-T1 — technician judgment stays); searchable knowledge base of past fixes per installation type (agent-T2 Q&A). Caveat: the work is human per F4 — position AI as a junior's senior-in-the-pocket, never as the mechanic.

## SVC.050 — Job report & materials registration
- **Typical AS-IS:** paper work orders signed on site, typed over by the office days later; materials used remembered approximately; evening paperwork resented.
- **Value leaks:** `retype` (paper → system), `wait` (invoicing waits for the report), `error` (forgotten materials never billed).
- **Opportunity patterns:** 60-second voice-note → structured report + materials + follow-up flags (agent-T1 — the flagship field win, feeds FIN.010 same-day invoicing); digital signature capture (automation). Caveat: pilot with the most open technician first; forcing the sceptic in week one kills adoption for everyone.

## SVC.060 — Follow-up work & repeat visits
- **Typical AS-IS:** "needs a new part, I'll come back" lives in the technician's memory; quotes for follow-up work never sent; second visits unplanned.
- **Value leaks:** `chase` (office reconstructs what was promised), `no-visibility` (revenue leaks from unquoted follow-up).
- **Opportunity patterns:** follow-up flags from SVC.050 auto-create tasks + draft quotes (hybrid: automation routes, agent-T1 drafts). Caveat: measure the leak first — count last quarter's "come back later" mentions vs. quotes actually sent; the number sells the case.

## SVC.070 — Maintenance contracts & periodic visits
- **Typical AS-IS:** contract obligations tracked in Excel or memory; visits planned late or missed; the install base is not systematically converted to contracts.
- **Value leaks:** `no-visibility` (which contracts are due, which installs have none), `chase` (customers call before the SME does).
- **Opportunity patterns:** maintenance-reminder engine over the install base (automation — the P3 growth case hiding in every service SME); contract-proposal drafts for uncovered installations (agent-T1). Caveat: recurring-revenue upside usually dwarfs the efficiency gains in this whole file — score it as growth, not cost.

## SVC.080 — Warranty & claims handling
- **Typical AS-IS:** warranty status checked per case against supplier terms; claims filed late or absorbed as goodwill; supplier credits not reconciled.
- **Value leaks:** `error` (claims missed → SME pays for supplier defects), `wait` (customer waits while paperwork crawls).
- **Opportunity patterns:** warranty check at ticket creation from purchase data (automation); claim-dossier assembly — photos, serials, report (agent-T1). Caveat: needs serial/lot registration (LOG.080) to work; otherwise every claim is archaeology.

## SVC.090 — Technician time registration
- **Typical AS-IS:** hours written on the work order or guessed on Friday; travel vs. work time blurred; payroll and job costing both inherit the noise.
- **Value leaks:** `retype` (hours re-keyed into payroll and costing), `error` (memory-based hours distort margins).
- **Opportunity patterns:** time capture merged into the SVC.050 voice-note flow (agent-T1) or app-based clock-in (automation). Caveat: time tracking touches monitoring sensitivities — involve the team early, frame it as billing accuracy, and check CAO/works-council duties (F4 §6).
