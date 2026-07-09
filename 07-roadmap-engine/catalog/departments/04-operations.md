# 04 — Operations: planning & production (OPS)

The value-creating core: turning confirmed orders into delivered work — production,
assembly, projects or works. Planning typically lives in one planner's head plus a
whiteboard/Excel; execution data flows back on paper, late or never. Per F4, the
operating work itself is human by design — the opportunity sits in the information
around it. Consultant-side authoring source; adapt per client.

## OPS.010 — Work order intake & preparation
- **Typical AS-IS:** accepted quotes arrive by mail; work prep re-types them into job sheets; drawings/specs chased from sales or the customer.
- **Value leaks:** `retype` (quote → work order duplication), `error` (missing specs surface on the shop floor).
- **Opportunity patterns:** structured handover from SAL.060 (automation); prep-pack agent that assembles specs, history and site info per job (agent-T2). Caveat: fix the sales handover contract first — an agent can't compile what was never captured.

## OPS.020 — Capacity & resource planning
- **Typical AS-IS:** medium-term load known only to the planner; overtime and subcontracting decided reactively when the week explodes.
- **Value leaks:** `skill-bottleneck` (planning knowledge in one head), `no-visibility` (no forward load picture).
- **Opportunity patterns:** load overview auto-derived from open orders × standard times (automation); what-if sparring on scenarios (agent-T1). Caveat: standard times are usually missing or fictional — calibrate them first or the picture misleads.

## OPS.030 — Day & week scheduling
- **Typical AS-IS:** the planner juggles skills, urgencies and absences on a board each morning; changes propagate by shouting or phone.
- **Value leaks:** `skill-bottleneck` (only the planner can schedule), `error` (double-bookings, forgotten constraints), `wait` (crews idle awaiting instructions).
- **Opportunity patterns:** constraint-aware scheduling suggestions inside the existing planning tool (agent-T1 — planner decides); automated change notifications to the floor/field (automation). Caveat: check the sector tool's native planning AI first — an activation beats an integration; full auto-scheduling (T3) is rarely warranted.

## OPS.040 — Execution & production registration
- **Typical AS-IS:** hours, quantities and deviations noted on paper job sheets, keyed in days later; evening paperwork is universally hated.
- **Value leaks:** `retype` (paper → system), `no-visibility` (progress invisible until the job closes).
- **Opportunity patterns:** voice-note/photo registration → structured job data (agent-T1 — the boring-but-gold enabler that unlocks half the downstream list); direct machine/scan feed where equipment allows (automation). Caveat: sequence this first when the maturity scan shows paper processes; everything in FIN.080 and MGT.030 depends on it.

## OPS.050 — Material availability check
- **Typical AS-IS:** planner walks to the warehouse or calls purchasing to check whether a job can start; shortages discovered at start time.
- **Value leaks:** `wait` (jobs blocked on missing material), `error` (started jobs stall halfway).
- **Opportunity patterns:** availability check against inventory + open POs at scheduling time (automation); shortage-alert digest for the planner (agent-T2). Caveat: presumes LOG.020 inventory accuracy — a check against wrong stock data is worse than a phone call.

## OPS.060 — Change & rework management
- **Typical AS-IS:** customer changes arrive by phone to whoever answers; extra work done without a signed change order; rework absorbed silently.
- **Value leaks:** `error` (unbilled extra work, wrong versions built), `chase` (confirmations chased after the fact).
- **Opportunity patterns:** change-order drafting from the call/mail with price impact (agent-T1); mandatory-confirmation workflow before execution (automation). Caveat: this is margin leakage, not efficiency — quantify it from a sample of past jobs to build the case.

## OPS.070 — Quality control
- **Typical AS-IS:** checks depend on the experienced eye; findings noted informally; recurring defects not tracked.
- **Value leaks:** `error` (escapes reach the customer), `skill-bottleneck` (quality = specific persons).
- **Opportunity patterns:** digital checklists with photo evidence (automation); defect-pattern summaries across jobs (agent-T2); photo-based anomaly assist where volume justifies (agent-T1). Caveat: vision QA needs training data volume most SMEs lack — start with checklists and trend reporting.

## OPS.080 — Subcontractor coordination
- **Typical AS-IS:** subcontractors booked by phone, confirmed by nothing; documents (safety, VCA, attestations) chased per project.
- **Value leaks:** `chase` (availability and paperwork chased repeatedly), `wait` (jobs slip on unconfirmed subs).
- **Opportunity patterns:** document-validity register with expiry alerts (automation); briefing-pack generation per sub per job (agent-T1). Caveat: chain-liability rules (Belgian 30bis, A1 documents) make the compliance register the priority, not the convenience features.

## OPS.090 — Progress reporting
- **Typical AS-IS:** "how far is job X?" answered by walking the floor or calling the crew; customer updates improvised.
- **Value leaks:** `retype` (status re-told to each asker), `no-visibility` (management and customer share the same blindness).
- **Opportunity patterns:** progress dashboard from registration data (automation); customer-update drafts per milestone (agent-T1). Caveat: derives entirely from OPS.040 — without live registration there is nothing to report.

## OPS.100 — Equipment maintenance planning
- **Typical AS-IS:** machines and vehicles maintained when they break or when someone remembers; service books on paper.
- **Value leaks:** `no-visibility` (no maintenance calendar), `wait` (unplanned downtime blocks production).
- **Opportunity patterns:** preventive-maintenance calendar with alerts (automation); maintenance-log capture via voice/photo feeding failure history (agent-T1). Caveat: predictive maintenance is oversold at SME scale — a disciplined preventive calendar captures most of the value.
