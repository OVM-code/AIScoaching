# 11 — IT & data (IT)

In an SME, "IT" is usually an external partner plus the colleague who's handy with
computers. This department is mostly an enabler: data quality, integrations and
access hygiene determine the feasibility scores of every other department's
opportunities (F3). Score it accordingly — fixes here unlock value elsewhere.
Consultant-side authoring source; adapt per client.

## IT.010 — User & access management
- **Typical AS-IS:** accounts created by mailing the IT partner; leavers keep access for months; passwords shared on post-its; no access overview.
- **Value leaks:** `wait` (new hires unproductive for days — ties to HR.030), `error` (orphaned accounts = security and license waste).
- **Opportunity patterns:** joiner/mover/leaver checklist workflow tied to HR events (automation); quarterly access-review report (automation). Caveat: shared logins block per-user AI tooling and audit trails — often a hidden prerequisite for the whole roadmap.

## IT.020 — Helpdesk & incident handling
- **Typical AS-IS:** problems reported to the handy colleague or the external partner's ticket line; recurring issues re-solved from scratch; no ticket history internally.
- **Value leaks:** `wait` (staff blocked on IT issues), `skill-bottleneck` (one internal person absorbs all first-line questions).
- **Opportunity patterns:** first-line self-help agent over an internal how-to base — printer, VPN, ERP how-do-I (agent-T2); ticket summarisation for the external partner (agent-T1). Caveat: the how-to base must exist; start by capturing the handy colleague's ten most-repeated answers.

## IT.030 — Master data quality management
- **Typical AS-IS:** customers, items and prices maintained separately in accounting, the sector tool and Excel; nobody owns "which is master"; every report needs manual cleaning first.
- **Value leaks:** `error` (conflicting records → wrong invoices, wrong stock), `no-visibility` (no one trusts any list).
- **Opportunity patterns:** duplicate/inconsistency detection with cleanup proposals (agent-T1); single-point-of-entry rules + sync (automation, see IT.040). Caveat: designating the master system is an organisational decision no tool makes — one workshop, then tooling; this gates CS.060, LOG.020, FIN.080.

## IT.040 — Integrations & data synchronisation
- **Typical AS-IS:** systems connected by humans re-typing (the swivel-chair integration): orders from the sector tool into accounting, hours into payroll, contacts everywhere.
- **Value leaks:** `retype` (the same record entered 2–4 times), `error` (sync-by-human drifts), `skill-bottleneck` (only one person knows the export-import ritual).
- **Opportunity patterns:** Make/Zapier/API integrations for the top re-typing flows (automation — the workhorse of most SME roadmaps); document/mail extraction as the bridge where no API exists (agent-T1). Caveat: verify API availability and the client's license tier per system first ([VERIFY] per data-readiness report); vendor-locked tools can cap the whole ambition.

## IT.050 — Backup & business continuity
- **Typical AS-IS:** "the partner handles backups" — untested; key business data in personal OneDrives and single Excel files; recovery time unknown.
- **Value leaks:** `no-visibility` (nobody knows what's protected until a crypto-locker asks).
- **Opportunity patterns:** backup-verification and restore-test schedule with reporting (automation); continuity one-pager drafted per critical system (agent-T1). Caveat: not an AI case — it's the insurance policy under every AI case; a roadmap whose data layer can vanish is not feasible, whatever the scores say.

## IT.060 — Security & phishing awareness
- **Typical AS-IS:** no MFA on half the accounts; invoice-fraud mails nearly succeed yearly; awareness = a warning mail after each incident.
- **Value leaks:** `skill-bottleneck` (security judgment unevenly distributed), `error` (one click from CEO-fraud or ransomware).
- **Opportunity patterns:** MFA + mail-filter hardening (automation, do first); suspicious-mail check agent for staff ("is this real?") (agent-T1); periodic awareness drills (automation). Caveat: AI adoption raises the stakes — new tools mean new credentials and data flows; fold AI-tool vetting into the same policy (F6).

## IT.070 — Reporting & BI maintenance
- **Typical AS-IS:** a graveyard of Excel reports each maintained by its creator; one Power BI attempt half-finished; every number requires manual refresh and explanation.
- **Value leaks:** `skill-bottleneck` (report logic in one head), `wait` (management waits on manual refreshes — ties to MGT.010).
- **Opportunity patterns:** consolidate the top 5 reports onto auto-refreshing sources (automation); natural-language explain-this-figure agent over the model (agent-T2, only after the model is trusted). Caveat: kill zombie reports first — automating 30 reports nobody reads is precisely the leanness trap.

## IT.080 — IT vendor & license management
- **Typical AS-IS:** subscriptions accumulated over years; licenses for departed staff still billed; renewal dates unknown; the SaaS list lives in the credit-card statement.
- **Value leaks:** `no-visibility` (spend and renewal exposure unknown), `chase` (contract terms hunted at renewal time).
- **Opportunity patterns:** license inventory auto-built from billing/statement data (agent-T1 extraction) + renewal calendar with alerts (automation). Caveat: quick, visible savings that fund the roadmap's tooling budget — a good wave-1 credibility win, but a one-off, not recurring value; score it honestly.
