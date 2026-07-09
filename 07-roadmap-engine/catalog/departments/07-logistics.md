# 07 — Inventory & logistics (LOG)

Stock and goods movement: a warehouse corner, vans, sometimes site containers. The
recurring SME condition is that the system stock (if any) and the physical stock
disagree, so everyone walks over to check. Most opportunities here are classic
automation + discipline; agents play a supporting extraction role. Consultant-side
authoring source; adapt per client.

## LOG.010 — Goods receiving & putaway
- **Typical AS-IS:** deliveries checked (or not) against the delivery note, signed, dropped in a landing zone; system booking happens later or never.
- **Value leaks:** `error` (short/wrong deliveries accepted unnoticed), `retype` (paper notes keyed in at the desk).
- **Opportunity patterns:** scan/photo-based receiving against the open PO (hybrid: agent-T1 extraction + automation booking); deviation alerts to purchasing (automation). Caveat: requires POs to exist (PUR.040) — receiving against nothing verifies nothing.

## LOG.020 — Inventory registration & counts
- **Typical AS-IS:** stock levels in Excel or in heads; the yearly count is a dreaded weekend; interim accuracy decays continuously.
- **Value leaks:** `error` (system ≠ shelf), `no-visibility` (purchasing and planning fly blind).
- **Opportunity patterns:** barcode/QR registration on every movement (automation — the foundational fix); photo-assisted cycle counting with discrepancy summaries (agent-T1). Caveat: this is a discipline project wearing a tooling costume; without movement registration every smarter feature downstream is fiction.

## LOG.030 — Picking & staging
- **Typical AS-IS:** jobs picked from a printed list or from memory; wrong or incomplete picks discovered on site, causing return trips.
- **Value leaks:** `error` (mispicks → wasted trips), `wait` (crews wait while material is hunted).
- **Opportunity patterns:** digital pick lists generated from the work order (automation); completeness check with photo confirmation before departure (hybrid). Caveat: value scales with mispick frequency — count return-trips-for-material for a month before sizing this.

## LOG.040 — Shipping & transport booking
- **Typical AS-IS:** transport booked by mail/phone per shipment; labels and documents typed manually; customer asks "where is it?" and the office asks the carrier.
- **Value leaks:** `retype` (address/shipment data re-keyed into carrier portals), `chase` (tracking questions relayed manually).
- **Opportunity patterns:** carrier integration or portal automation for labels/booking (automation); tracking-status auto-replies to customers (automation, feeds CS.020). Caveat: volume threshold — below a few shipments a day, a template beats an integration.

## LOG.050 — Van & site stock management
- **Typical AS-IS:** every van is a private mini-warehouse; nobody knows what's on board; technicians hoard parts because restocking is unreliable.
- **Value leaks:** `no-visibility` (capital parked in vans), `error` (missing part on site despite five in colleagues' vans).
- **Opportunity patterns:** van stock lists with scan-out on use (automation, piggybacking on SVC.050 registration); replenishment proposals per van per week (automation). Caveat: acceptance hinges on restocking actually working — fix the supply promise before policing the vans.

## LOG.060 — Replenishment & reorder points
- **Typical AS-IS:** reorder when the shelf looks empty; stockouts of fast-movers coexist with years of dead stock.
- **Value leaks:** `no-visibility` (no consumption data), `wait` (jobs delayed on stockouts).
- **Opportunity patterns:** min/max proposals from consumption history (automation); seasonal-pattern and dead-stock review with plain-language rationale (agent-T1). Caveat: needs 6–12 months of movement data from LOG.020; before that, a simple two-bin system beats any algorithm.

## LOG.070 — Returns processing
- **Typical AS-IS:** returns to suppliers and from customers pile up in a corner; credit notes requested late or forgotten; unused job material silently re-shelved without booking.
- **Value leaks:** `error` (credits never claimed, stock counts corrupted), `chase` (supplier credit notes chased for months).
- **Opportunity patterns:** return registration with photo + reason at the moment of return (agent-T1 capture); credit-note tracking with auto-reminders (automation). Caveat: small individually, material in aggregate — sample a quarter of supplier credits to size the leak honestly.

## LOG.080 — Traceability & lot-serial registration
- **Typical AS-IS:** serial/lot numbers written on the delivery note or nowhere; recalls and warranty claims require digging through paper archives.
- **Value leaks:** `retype` (numbers copied by hand at multiple points), `error` (untraceable installs → lost warranty claims, recall panic).
- **Opportunity patterns:** photo-based serial capture at receipt and installation (agent-T1 extraction feeding SVC.080); label scanning where suppliers barcode (automation). Caveat: mandatory in some sectors (food, medical, construction products) — check the regulatory driver first, it changes priority from convenience to compliance.
