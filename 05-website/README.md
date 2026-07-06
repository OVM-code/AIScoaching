# Website — deploy & lead-tracking guide

Two self-contained pages, no build step, no dependencies:

- `index.html` — Dutch one-pager: the full funnel (credibility → AI-Scan → debrief booking)
- `en/index.html` — English page for corporate/professional visitors (methodology + conversation CTA)
- `leads-tracker-template.csv` — the follow-up tracker (import into Google Sheets)

## 1. Put it live (10 minutes, free)

**Option A — Netlify Drop (fastest):** go to app.netlify.com/drop → drag the `05-website` folder in → site is live on `something.netlify.app` → Site settings → change site name to e.g. `olivia-ai` → live at `olivia-ai.netlify.app`.

**Option B — connect the repo (auto-updates):** Netlify → Add new site → Import from Git → pick this GitHub repo → set *Publish directory* to `05-website` → every push updates the site automatically. Recommended once you're happy with it.

**Custom domain later:** buy `oliviavanmalleghem.be` at any registrar → Netlify → Domain settings → add domain → follow the DNS instructions. Nothing on the site needs rebuilding.

## 2. Replace the placeholders (search each file)

| Placeholder | Replace with | Where it comes from |
|---|---|---|
| `{{TALLY_SCAN_URL}}` | link of the AI-Scan Tally form | §3 below |
| `{{TALLY_CONTACT_URL}}` | link of the short contact form | §3 below |
| `{{CAL_URL}}` | your Cal.com booking link | LAUNCH-CHECKLIST B3 spec |
| `div.photo` (the OV block) | `<img src="olivia.jpg" ...>` — a real photo, warm and professional | you |
| Footer TODO comment | ondernemingsnummer + adres | legally required on a Belgian commercial site once you sell; add at registration |

## 3. Tally setup (the lead capture + tracking engine, ~30 min once)

Create a free account on tally.so, then two forms:

**Form 1 — "AI-Scan voor installatie- en servicebedrijven"** (this IS the lead magnet, interactive):
1. Intro block: the promise + anonymity of nothing, this one asks contact info at the END (finish the scan first = higher completion).
2. The 12 scan questions from `04-marketing/assets/lead-magnet-ai-scan.md`, as multiple choice (nee/soms/ja = 0/1/2), grouped in the 4 blocks.
3. Tally "Calculated field" sums the score.
4. Contact block: naam, bedrijf, sector (dropdown: HVAC/sanitair/elektro/renovatie/cleaning/tuin/andere), e-mail, telefoon (optional).
5. Thank-you page shows the score band (rood/oranje/groen with the honest interpretations from the lead magnet) + button "Boek je gratis debrief" → `{{CAL_URL}}` + note that the full PDF arrives by mail.
6. Settings → notifications: email yourself on every submission.
7. Settings → integrations → **Google Sheets**: connect, so every submission lands as a row.

**Form 2 — "Hou me op de hoogte"** (short contact form): naam, e-mail, bedrijf (optional), vraag/bericht (optional). Same notification + same Google Sheet (second tab).

## 4. The follow-up tracker

1. Import `leads-tracker-template.csv` into Google Sheets as tab "Leads".
2. Tally sync fills tabs "Scan" and "Contact" automatically; copy new entries into "Leads" (or use the sheet's own automation later).
3. Work the **Status** column as your pipeline: `Nieuw → Debrief gepland → Discovery call → Offer → Klant / Geparkeerd`.
4. Friday ritual (part of the M3 scorecard): every lead gets a *Volgende actie* + date. A lead without a next action is a lost lead.
5. Cal.com bookings: add them to the same sheet (Cal.com also emails you each booking).

This sheet IS the M3 funnel math source: count rows per status for the weekly scorecard.

## 5. Optional: visitor stats

Free + privacy-friendly (no cookie banner needed): create an account at goatcounter.com and uncomment the script line at the bottom of both HTML files. Tells you visits, referrers (which LinkedIn post drove traffic), and which page converts.

## 6. Voice & truth notes

- All NL copy is the approved calibrated voice; the credibility section names role & industry, **no employer name** (decided 2026-07-06).
- No testimonials or case numbers exist on the site yet, on purpose. When the first Kickstart scorecard exists, add a case block to `index.html` (before the FAQ) with real numbers and, with consent, the client's name and quote. That upgrade is the single biggest conversion improvement available later.
- The founder-slots line ("eerste drie bedrijven aan founder-voorwaarden, max twee per maand") is true scarcity; keep it current or remove it when it stops being true.
