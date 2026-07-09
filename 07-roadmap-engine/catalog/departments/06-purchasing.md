# 06 — Purchasing (PUR)

Buying materials, parts and services: in most SMEs a part-time role spread over the
owner, the planner and the bookkeeper. Nobody owns supplier performance; price lists
age quietly in quotes long after suppliers raised them. Consultant-side authoring
source; adapt per client.

## PUR.010 — Identify purchase need
- **Typical AS-IS:** needs surface ad hoc — a technician notices an empty shelf, a job requires parts; requests reach purchasing by shout, note or WhatsApp.
- **Value leaks:** `wait` (needs discovered at job start), `no-visibility` (no consolidated requirement view, so no bundling discounts).
- **Opportunity patterns:** requirement generation from confirmed orders × BOM (automation); request intake via a structured channel replacing WhatsApp (automation). Caveat: needs bills-of-material or job templates to exist — often a data project first.

## PUR.020 — Supplier selection & RFQ
- **Typical AS-IS:** three-quotes ritual for big buys, habit supplier for the rest; RFQ mails written from scratch each time.
- **Value leaks:** `wait` (RFQ rounds take weeks), `skill-bottleneck` (market knowledge sits with one buyer/owner).
- **Opportunity patterns:** RFQ drafting + response tabulation into a comparison table (agent-T1, compression pattern); alternative-supplier research for critical items (agent-T1 research). Caveat: supplier relationships are commercial judgment — the agent prepares, the human picks.

## PUR.030 — Price comparison & negotiation
- **Typical AS-IS:** offers compared by eyeballing PDFs; unit conversions and delivery terms make comparisons apples-to-oranges; negotiation leverage unused.
- **Value leaks:** `skill-bottleneck` (only the owner negotiates), `retype` (PDF offers re-keyed into comparison sheets).
- **Opportunity patterns:** offer-PDF extraction into a normalised comparison (agent-T1); negotiation-prep brief with price history and volume leverage (agent-T1 sparring). Caveat: extraction errors on unit/packaging conversions are common — keep the human check on the comparison, not just the decision.

## PUR.040 — Create purchase order
- **Typical AS-IS:** orders placed by phone or mail without a formal PO; what was ordered, at what price, exists only in a sent-items folder.
- **Value leaks:** `retype` (need → mail → later reconstruction), `error` (no reference to check deliveries and invoices against).
- **Opportunity patterns:** PO creation from the approved need with supplier/price defaults (automation); mail-to-PO extraction for the transition period (agent-T2). Caveat: the discipline change (always a PO) matters more than the tool — without it PUR.060 stays impossible.

## PUR.050 — Order confirmation & delivery chase
- **Typical AS-IS:** confirmations sometimes arrive, rarely checked against the order; delivery dates chased by phone when a job is already waiting.
- **Value leaks:** `chase` (proactive chasing never happens), `no-visibility` (no open-order list with promised dates).
- **Opportunity patterns:** confirmation-vs-PO comparison with deviation flags (agent-T2); auto-chase sequence before the promised date (automation). Caveat: quantify wasted planner hours + delayed jobs first; the chase automation is trivial, the case is in the delay cost.

## PUR.060 — Receipt & invoice matching (three-way match)
- **Typical AS-IS:** delivery notes land in a tray; the bookkeeper matches invoices to memory; price hikes and short deliveries slip through unnoticed.
- **Value leaks:** `error` (paying for goods not received, at prices never agreed), `retype` (delivery notes keyed in manually).
- **Opportunity patterns:** delivery-note capture via photo/scan (agent-T1 extraction) + automated three-way match with exception queue (automation; hybrid overall). Caveat: only exceptions should reach a human — if the match rate is below ~80%, fix master data before blaming the tool.

## PUR.070 — Supplier data & performance management
- **Typical AS-IS:** supplier records incomplete; delivery reliability and quality issues known anecdotally ("firm X always delivers late") but never measured.
- **Value leaks:** `no-visibility` (no data to negotiate or switch on), `retype` (same supplier data maintained in accounting, mailbox and Excel).
- **Opportunity patterns:** supplier scorecard auto-derived from PO/receipt history (automation); annual supplier-review brief per key supplier (agent-T1). Caveat: scorecards need 6–12 months of clean PO data — schedule this a wave after PUR.040/060.

## PUR.080 — Process supplier price lists
- **Typical AS-IS:** suppliers mail Excel/PDF price lists; someone updates the calculation sheets eventually; quotes meanwhile go out on old prices.
- **Value leaks:** `retype` (manual price-list entry), `error` (quoting on stale prices = silent margin erosion).
- **Opportunity patterns:** price-list extraction + delta report against current prices (agent-T1); auto-update of the price book after human approval of the delta (hybrid). Caveat: one mis-parsed decimal poisons every downstream quote — the delta report is the safety net, never skip it.
