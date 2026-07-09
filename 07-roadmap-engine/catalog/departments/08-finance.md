# 08 — Finance & administration (FIN)

The paper mill: invoicing, bookkeeping (usually with an external accountant),
payments, filings. Highest automation density of any department — much is rule-based
and structured — and the fastest cash impact (invoicing delay is a working-capital
leak, not a paperwork nuisance). Consultant-side authoring source; adapt per client.

## FIN.010 — Sales invoicing
- **Typical AS-IS:** invoices batched weekly or monthly after someone assembles job data; days-to-weeks between delivery and invoice; details missing so invoicing waits.
- **Value leaks:** `wait` (delivery-to-invoice delay strangles cash), `retype` (job data re-keyed into the invoice), `error` (forgotten items and hours never billed).
- **Opportunity patterns:** job-report → draft invoice same day (automation fed by SVC.050/OPS.040 — the classic cash quick win); completeness check flagging unbilled materials (agent-T2). Caveat: measure days-sales-outstanding before/after — this case is won on working capital, not hours.

## FIN.020 — Purchase invoice processing
- **Typical AS-IS:** supplier invoices arrive by mail/PDF/paper; keyed into accounting by the bookkeeper or scanned via the accountant's portal; approvals verbal.
- **Value leaks:** `retype` (manual entry), `error` (duplicates, wrong codings, invoices paid without receipt check).
- **Opportunity patterns:** invoice capture/extraction into accounting (automation — mature tooling exists; activate before building); approval routing with thresholds (automation). Caveat: check what the accountant's platform already includes — this is the most commonly already-half-solved process in the list.

## FIN.030 — Payments & bank reconciliation
- **Typical AS-IS:** payment batches assembled manually in the banking app; bank statements matched to invoices by hand or by the accountant weeks later.
- **Value leaks:** `error` (double/missed payments, fraud exposure in manual beneficiary entry), `retype` (statement lines matched manually).
- **Opportunity patterns:** payment files generated from approved invoices (automation); auto-reconciliation with exception queue (automation). Caveat: payment execution keeps four-eyes human control permanently — this is a fraud surface, per F4 an accountability moment, never T3.

## FIN.040 — Receivables follow-up & dunning
- **Typical AS-IS:** overdue invoices chased when cash feels tight; reminders awkward because the debtor is also a known relation; no escalation path.
- **Value leaks:** `chase` (irregular manual reminding), `no-visibility` (no ageing overview; surprises at quarter-end).
- **Opportunity patterns:** reminder sequence with tone escalation, human takeover at step 3 (automation + agent-T1 drafted wording); weekly ageing digest to the owner (automation). Caveat: relationship-sensitive accounts get flagged out of the sequence — one automated snub to the biggest customer undoes the ROI.

## FIN.050 — Expense & card transaction processing
- **Typical AS-IS:** receipts in glove compartments and wallets; monthly shoebox to the bookkeeper; card statements reconciled by interrogating colleagues.
- **Value leaks:** `retype` (receipt data keyed in), `chase` (missing receipts hunted for weeks).
- **Opportunity patterns:** photo-at-purchase receipt capture with auto-coding (automation with agent-T1 extraction); auto-matching to card statements with a chase-bot for missing items (automation). Caveat: adoption problem more than tech problem — the habit must be easier than the glove compartment.

## FIN.060 — VAT & statutory filings
- **Typical AS-IS:** the external accountant files VAT/intrastat/annual accounts from the books; the SME's job is delivering complete data on time, which it structurally doesn't.
- **Value leaks:** `error` (late/incomplete data → corrections and fines), `skill-bottleneck` (all fiscal knowledge external).
- **Opportunity patterns:** pre-filing completeness checklist automation (missing invoices, unreconciled accounts); plain-language explanation of accountant queries (agent-T1). Caveat: filing responsibility stays with the accountant — the opportunity is the data handover, not replacing fiscal advice; e-invoicing mandates (Belgium 2026) shift this landscape, verify current state.

## FIN.070 — Month-end close
- **Typical AS-IS:** "close" means the accountant's quarterly VAT rhythm; management figures (MGT.010) wait on it; nobody owns an internal close checklist.
- **Value leaks:** `wait` (steering info 4–8 weeks old), `error` (accruals and WIP guessed).
- **Opportunity patterns:** lightweight monthly close checklist with automated recurring bookings (automation); WIP estimate from operational data (hybrid, agent-T2 draft + controller review). Caveat: the goal is a "good-enough monthly picture", not audit-grade — say so explicitly or scope creeps toward a CFO project.

## FIN.080 — Cost tracking & job costing
- **Typical AS-IS:** post-calculation done for the odd painful job; hours and materials incomplete (see OPS.040/SVC.090), so real margin per job/customer is unknown.
- **Value leaks:** `no-visibility` (loss-making jobs and customers undetected), `retype` (costing sheets assembled by hand).
- **Opportunity patterns:** automated job-cost roll-up from registrations + purchases (automation); margin-outlier commentary per month (agent-T2). Caveat: entirely downstream of registration quality — this is why OPS.040/SVC.050 sequence first; without them, costing automates guesses.

## FIN.090 — Cash-flow forecasting
- **Typical AS-IS:** the owner's mental model plus the bank balance; VAT and payroll due dates surprise; investment timing is gut-based.
- **Value leaks:** `no-visibility` (13-week cash picture absent), `skill-bottleneck` (only the owner can even attempt it).
- **Opportunity patterns:** rolling 13-week forecast from open AR/AP + recurring obligations (automation); scenario sparring — "what if customer X pays 30 days late?" (agent-T1). Caveat: label directional; forecast quality is bounded by FIN.040 ageing data and order-book realism, and the honest-ROI rule applies to any promised precision.
