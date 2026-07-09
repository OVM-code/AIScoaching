# 01 — Management & reporting (MGT)

How the owner/management team steers a Belgian SME: mostly Excel consolidation, mail
threads, and meetings. The dominant leak is not hours but decision latency — figures
arrive late, so steering happens on gut feel. Consultant-side authoring source; adapt
per client in the engagement workspace.

## MGT.010 — Periodic KPI reporting
- **Typical AS-IS:** office or controller copies figures from accounting package, planning tool and Excel sheets into a monthly management workbook; 0.5–2 days per cycle, often 2–4 weeks after month-end.
- **Value leaks:** `retype` (manual consolidation across systems), `no-visibility` (numbers stale by the time they land; nobody trusts one version).
- **Opportunity patterns:** scheduled export + auto-consolidation into one dashboard (automation); narrative commentary drafted from the figures (agent-T1). Caveat: garbage-in — fix master data and cut-off discipline first, or you automate the wrong numbers faster.

## MGT.020 — Meeting preparation & minutes
- **Typical AS-IS:** owner assembles an agenda from memory and mail; minutes are typed after (or not at all); action points live in heads.
- **Value leaks:** `retype` (notes → minutes → task lists), `wait` (decisions stall because the pre-read never got made).
- **Opportunity patterns:** transcript → minutes + action list (agent-T1, compression pattern); recurring agenda pack auto-compiled from open actions and KPI deltas (hybrid). Caveat: recording meetings needs explicit team consent — Belgian works-council/privacy sensitivities apply.

## MGT.030 — Cash & margin monitoring
- **Typical AS-IS:** owner checks the bank balance in the banking app and "feels" margin; real margin per job/product only appears at year-end from the accountant.
- **Value leaks:** `no-visibility` (margin leaks discovered months late), `wait` (pricing decisions postponed until the accountant reports).
- **Opportunity patterns:** automated weekly cash/margin snapshot from accounting + open orders (automation); anomaly flagging with plain-language explanation (agent-T2 once trusted). Caveat: depends on FIN.080 job costing actually being fed — usually the real project.

## MGT.040 — Budgeting & forecasting
- **Typical AS-IS:** annual budget built once in Excel from last year +X%; rarely reforecast; versions diverge between owner and accountant.
- **Value leaks:** `retype` (rebuilding the workbook each cycle), `error` (broken formulas, stale links discovered mid-presentation).
- **Opportunity patterns:** driver-based template refreshed from actuals (automation); scenario drafting and sanity-check commentary (agent-T1 sparring). Caveat: an LLM must never be the calculator of record — formulas stay in the sheet, the agent explains and challenges.

## MGT.050 — Project & initiative tracking
- **Typical AS-IS:** improvement projects tracked in a slide or nowhere; status collected by asking people in the corridor.
- **Value leaks:** `chase` (owner pings people for status), `no-visibility` (initiatives silently die).
- **Opportunity patterns:** weekly status-digest agent that reads shared task lists and drafts a one-page delta (agent-T2); automated reminders on stale actions (automation). Caveat: only works if actions live in a system — introducing that habit is change management, not tooling.

## MGT.060 — Board & shareholder reporting
- **Typical AS-IS:** quarterly pack assembled by hand from the monthly workbooks; heavy re-formatting; the story is written the night before.
- **Value leaks:** `retype` (same numbers re-keyed into slides), `wait` (board dates slip because the pack isn't ready).
- **Opportunity patterns:** pack skeleton auto-filled from the KPI source (automation) + narrative first draft (agent-T1). Caveat: keep human ownership of the message — a board deck is judgment, the agent only drafts.

## MGT.070 — Policy & procedure maintenance
- **Typical AS-IS:** procedures exist as tribal knowledge or an outdated Word file; only written down when a certification audit forces it.
- **Value leaks:** `skill-bottleneck` (only one person knows how X works), `error` (people improvise divergent ways of working).
- **Opportunity patterns:** interview/voice-note → drafted SOP (agent-T1, structuring pattern); Q&A agent over the procedure base once it exists (agent-T2). Caveat: capture is the bottleneck, not drafting — budget the humans' time to review, or the SOPs will be confidently wrong.

## MGT.080 — Ad-hoc decision analysis
- **Typical AS-IS:** "should we buy that machine / hire / drop that customer?" answered by a weekend of owner-Excel or not analysed at all.
- **Value leaks:** `skill-bottleneck` (analysis capacity = the owner), `wait` (decisions deferred for lack of a business case).
- **Opportunity patterns:** sparring-partner agent for pre-mortems, option comparison and quick business-case skeletons (agent-T1). Caveat: outputs are directional; the honest-ROI rule applies — self-reported savings inflate 2–3×, so the agent's numbers get challenged, not pasted.
