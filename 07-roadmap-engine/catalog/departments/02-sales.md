# 02 — Sales & quoting (SAL)

The revenue front-end of a Belgian SME: inquiries by phone/mail, quotes in Excel or
the sector tool, follow-up in someone's head. The two classic leaks are the
visit-to-quote delay (kills win rates) and missed/unfollowed leads. Consultant-side
authoring source; adapt per client.

## SAL.010 — Lead intake & qualification
- **Typical AS-IS:** leads arrive via phone, mail, website form and WhatsApp; whoever answers scribbles details; missed calls after hours simply evaporate.
- **Value leaks:** `wait` (slow first response loses the job to a faster competitor), `no-visibility` (no lead list, no conversion numbers).
- **Opportunity patterns:** missed-call/voicemail-to-SMS capture with auto-callback booking (automation — often the #1 leak in service SMEs); website/WhatsApp intake agent asking triage questions (photos, location, urgency) and creating a structured lead (agent-T2). Caveat: needs a place for leads to land — a minimal CRM or list is a prerequisite.

## SAL.020 — Site visit & needs analysis
- **Typical AS-IS:** owner or rep visits, takes paper/voice notes and photos; half the detail never reaches the quote.
- **Value leaks:** `retype` (notes re-typed, or re-asked to the customer), `skill-bottleneck` (only the visitor can write the quote).
- **Opportunity patterns:** voice-note + photo capture → structured visit report (agent-T1); checklist-driven intake so juniors can do visits (hybrid). Caveat: field adoption stands or falls with a 60-second capture habit — design for the van, not the desk.

## SAL.030 — Draft quote
- **Typical AS-IS:** inside sales re-types the request from mail and site notes into an Excel/Word template; 30–60 min per quote, days of delay when the specialist is busy.
- **Value leaks:** `retype` (literal re-typing from mail), `wait` (visit-to-quote delay), `skill-bottleneck` (pricing knowledge in one head).
- **Opportunity patterns:** quote-drafting agent from request mail + visit notes in the client's price book and tone (agent-T1 — owner reviews every quote; the flagship SME quick win); template + price-book standardisation as enabler (automation). Caveat: if requests are too unstructured (<60% usable), feasibility drops — pilot on the last 20 quotes first.

## SAL.040 — Quote pricing & approval
- **Typical AS-IS:** margins set by feel; big quotes wait for the owner's blessing, which happens in the evening or not at all.
- **Value leaks:** `wait` (quotes queue on one approver), `skill-bottleneck` (nobody else dares to price).
- **Opportunity patterns:** pricing guardrails + auto-approval under thresholds (automation); margin-check assistant that flags outliers vs. historical wins (agent-T2). Caveat: final approval above threshold stays human — € weight puts this at T1/T2 permanently per F4.

## SAL.050 — Quote follow-up
- **Typical AS-IS:** follow-up happens "when there's time", i.e. rarely and unevenly; no one knows which quotes are open.
- **Value leaks:** `chase` (manual, ad-hoc chasing), `no-visibility` (open-quote list doesn't exist).
- **Opportunity patterns:** polite chase sequence at day 3/7/14 with owner-approved wording (automation); reply-handling and objection summaries (agent-T1). Caveat: sequence tone must sound like the owner, not a robot — invest one workshop in the wording.

## SAL.060 — Order confirmation & handover to operations
- **Typical AS-IS:** accepted quote is forwarded by mail; planning re-types it; details (access, materials, promises made) get lost in the handoff.
- **Value leaks:** `retype` (quote → work order duplication), `error` (verbal promises never reach execution).
- **Opportunity patterns:** structured quote-to-work-order conversion (automation); handover-summary agent that extracts commitments from the mail thread (agent-T1). Caveat: classic candidate for merging into an end-to-end flow role (F4 §3) — tooling alone won't fix a broken handoff culture.

## SAL.070 — Contract & price renewals
- **Typical AS-IS:** annual price increases and contract renewals triggered by memory or by the accountant noticing eroded margin.
- **Value leaks:** `chase` (renewals forgotten), `no-visibility` (no renewal calendar).
- **Opportunity patterns:** renewal-reminder engine off contract dates (automation); indexation-letter drafting per customer (agent-T1). Caveat: Belgian B2B indexation clauses have legal constraints — template wording past legal review once, then reuse.

## SAL.080 — CRM data upkeep
- **Typical AS-IS:** if a CRM exists it's half-filled; customer history lives in mailboxes and the owner's memory.
- **Value leaks:** `retype` (double entry mail↔CRM), `no-visibility` (no usable customer history).
- **Opportunity patterns:** auto-logging of mail/calls to the customer record (automation); enrichment agent that summarises the relationship before a visit (agent-T2). Caveat: don't buy a bigger CRM to fix a discipline problem — capture must be near-zero-effort or it won't happen.

## SAL.090 — Pipeline review & sales forecast
- **Typical AS-IS:** "what's coming in?" answered from memory in the Monday meeting; no weighted pipeline.
- **Value leaks:** `no-visibility` (capacity and cash planned on anecdote).
- **Opportunity patterns:** pipeline snapshot auto-built from the quote list with stage ageing (automation); forecast commentary and risk flags (agent-T2). Caveat: only as good as SAL.050/SAL.080 hygiene — sequence those first.

## SAL.100 — Tender & RFP response
- **Typical AS-IS:** public/large tenders answered in panic mode; boilerplate re-written each time; references and certificates hunted down repeatedly.
- **Value leaks:** `skill-bottleneck` (one person can write these), `wait` (deadline crunches), `retype` (same company info re-entered per tender).
- **Opportunity patterns:** answer-library + first-draft generation from past tenders (agent-T1, expansion pattern); compliance-checklist extraction from the tender doc (agent-T1). Caveat: hallucinated capability claims in a tender are a legal risk — human verification of every factual claim, always T1.
