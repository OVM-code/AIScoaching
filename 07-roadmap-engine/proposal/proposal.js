/* Roadmap proposal engine — vanilla JS, no CDNs, no eval.
   One render path: state (assumptions + filters + selection) -> render functions.
   DATA is injected by build_proposal.py; formulas are pre-compiled static
   arrow functions (compiled in Python from validated Waardeformule tokens). */
(function () {
"use strict";
if (typeof DATA === "undefined" || !DATA) return; // raw template opened directly

/* ---------------- i18n ---------------- */
var lang = DATA.lang === "en" ? "en" : "nl";
var locale = lang === "nl" ? "nl-BE" : "en-GB";
var STR = {
  nl: {
    brand: "Roadmapvoorstel",
    navOverview: "Overzicht", navAssumptions: "Aannames", navMap: "Kansenkaart",
    navRegister: "Register", navRoadmap: "Roadmap", navKeep: "Niet veranderen", navMethod: "Methode",
    eyebrow: "AI-integratie · roadmapvoorstel",
    heroTitle: "De AI-roadmap voor {client} — stel bij, kies, bevestig",
    heroLede: "Elke euro hieronder is een open formule over {n} aannames. Schuif ze naar jullie realiteit en het hele voorstel herrekent — daarna vink je aan wat in de roadmap komt en bevestig je onderaan. Alle bedragen zijn richtinggevend, geen audit.",
    heroStamp: "gebouwd {date} · {sector} · bedragen per jaar, bij de ingestelde aannames",
    stTotal: "Totale jaarwaarde", stTotalNote: "alle voorgestelde kansen, wave 1–3",
    stHours: "Vrijgespeelde uren / jaar", stHoursNote: "afgeleid uit de waardeformules ÷ uurkost",
    stWave1: "Kansen in wave 1", stWave1Note: "quick wins — max. 2–3 bewust",
    stPayback: "Gemiddelde terugverdientijd", stPaybackNote: "jaar-1 kost ÷ maandwaarde, wave 1–3",
    kAssump: "Kalibreer", hAssump: "Aannames — zet ze naar jullie praktijk",
    subAssump: "De standaardwaarden komen uit de intake en de workshops. Elk €-bedrag in dit voorstel is een live formule over deze schuivers; de formule per kans staat in zijn kaart.",
    assumpFootNote: "Elke aanname vermeldt zijn bron en hoe hij in de pilot gemeten wordt.",
    btnReset: "Terug naar standaard", srcLabel: "Bron",
    kMap: "Prioritering (F3)", hMap: "Waarde × haalbaarheid",
    subMap: "Elke kans geplot op de twee F3-assen; de grens 'hoog' ligt op 3,5. Kleur = allocatie (F4). Klik een punt om zijn kaart te openen.",
    axisX: "haalbaarheid →", axisY: "waarde →",
    qQw: "Quick wins", qBb: "Big bets", qFi: "Fill-ins", qDc: "Discard",
    legendHint: "klik een punt voor detail",
    kRegister: "Kansen", hRegister: "Kansenregister",
    subRegister: "Elke kaart toont de scores, de formule achter het bedrag, de kostenraming en het falsifieerbare verdict. Vink aan wat in de roadmap komt; wave 1 staat vooraf aangevinkt.",
    fDept: "Afdeling", fQuadrant: "Kwadrant", fAlloc: "Allocatie", fStatus: "Status", fAll: "alle",
    sortValue: "sorteer: waarde", sortPayback: "sorteer: terugverdientijd",
    noMatch: "Geen kansen voor deze filter.",
    pick: "Opnemen in roadmap",
    hScores: "Scores (F3)", hPains: "Gekoppelde pijnpunten", hFormula: "Waardeformule",
    hCost: "Kostenraming", hPayback: "Terugverdientijd", hVerdict: "Verdict",
    hWouldChange: "Wat dit zou veranderen", hEnablers: "Enablers", hRisk: "Risico / AI Act",
    hFirstStep: "Eerste stap",
    valueW: "Waarde", feasW: "Haalbaarheid", adoption: "Adoptie",
    wHours: "uren", wQuality: "kwaliteit", wStrategic: "strategie",
    wData: "data", wTechnical: "technisch", wOwnership: "eigenaarschap",
    confidence: "vertrouwen", confMap: { high: "hoog", medium: "gemiddeld", low: "laag" },
    perYear: "/jaar", months: "mnd", daysUnit: "d", hoursUnit: "u",
    costLine: "{days} d × {rate} + 12 × {tooling}/mnd = {y1} in jaar 1",
    costLineNoTool: "{days} d × {rate} = {y1} in jaar 1",
    year1: "jaar-1 kost",
    kRoadmap: "Sequentie", hRoadmap: "Roadmap in drie waves",
    subRoadmap: "Totalen per wave rekenen alleen over de aangevinkte kansen en bewegen mee met de aannames. Doorgestreept = niet geselecteerd.",
    wave: "Wave", waveSubs: { 1: "0–3 maanden · quick wins", 2: "3–9 maanden · big bets + enablers", 3: "9–18 maanden · opschalen" },
    waveTotals: "waarde {v}/jaar · jaar-1 kost {c} · terugverdientijd {p}",
    waveSelected: "{n} van {m} geselecteerd", waveEmpty: "Geen kansen in deze wave.",
    kKeep: "Bewust niet", hKeep: "Niet veranderen",
    subKeep: "Wat vandaag goed werkt en wat we bewust met rust laten — nee zeggen is de helft van een roadmap.",
    kMethod: "Methode", hMethod: "Methode & kanttekeningen",
    methodWeights: "Scores volgen F3: Waarde = {vw}; Haalbaarheid = {fw}. “Hoog” = ≥ {hi} op de as; adoptie (1–5) is de tie-breaker. Kosten per kans = implementatiedagen (effort-baseline per allocatie × T-shirtmaat) × dagtarief € {rate}, plus 12 × tooling/maand. Terugverdientijd = jaar-1 kost ÷ maandwaarde.",
    methodNote: "<strong>Richtinggevend, geen audit.</strong> Zelfgerapporteerde tijdsbesparingen overschatten in de praktijk 2–3×; lees elk bedrag als hypothese, niet als belofte. Kalibratiepad: elke aanname hierboven noemt zijn bron; in de eerste pilotweken vervangen metingen de schattingen en wordt dit voorstel met dezelfde formules herrekend. De effort-baselines zijn conservatieve startwaarden en worden na elk traject bijgesteld.",
    cbCount: "{n} geselecteerd", cbValue: "jaarwaarde {v}", cbCost: "jaar-1 kost {c}",
    cbBtn: "Roadmap bevestigen",
    dTitle: "Jullie roadmap-selectie",
    dSub: "Dit is wat bevestigd wordt, bij de huidige stand van de schuivers.",
    dNone: "Nog niets geselecteerd.",
    dTotal: "Totaal: {v}/jaar · jaar-1 kost {c} · terugverdientijd {p}",
    dNote: "Download het JSON-bestand en bezorg het aan de consultant — het wordt vastgelegd in proposal/decision-log.md.",
    dDownload: "Download JSON", dPrint: "Afdrukken", dClose: "Sluiten",
    themeBtn: "◐ thema",
    alloc: { automation: "Automatisering", "agent-T1": "Agent T1", "agent-T2": "Agent T2", "agent-T3": "Agent T3", hybrid: "Hybride" },
    quad: { "quick-win": "Quick win", "big-bet": "Big bet", "fill-in": "Fill-in", discard: "Discard" },
    status: { proposed: "voorgesteld", confirmed: "bevestigd", deferred: "uitgesteld", discarded: "afgevoerd" }
  },
  en: {
    brand: "Roadmap proposal",
    navOverview: "Overview", navAssumptions: "Assumptions", navMap: "Opportunity map",
    navRegister: "Register", navRoadmap: "Roadmap", navKeep: "Not changing", navMethod: "Method",
    eyebrow: "AI integration · roadmap proposal",
    heroTitle: "The AI roadmap for {client} — adjust, select, confirm",
    heroLede: "Every euro below is an open formula over {n} assumptions. Slide them to your reality and the whole proposal recomputes — then tick what goes into the roadmap and confirm at the bottom. All figures are directional, not audited.",
    heroStamp: "built {date} · {sector} · amounts per year, at the assumptions set below",
    stTotal: "Total annual value", stTotalNote: "all proposed opportunities, waves 1–3",
    stHours: "Hours released / year", stHoursNote: "derived from the value formulas ÷ hourly cost",
    stWave1: "Wave-1 opportunities", stWave1Note: "quick wins — deliberately max 2–3",
    stPayback: "Blended payback", stPaybackNote: "year-1 cost ÷ monthly value, waves 1–3",
    kAssump: "Calibrate", hAssump: "Assumptions — set them to your practice",
    subAssump: "Defaults come from the intake and the workshops. Every € figure in this proposal is a live formula over these sliders; each opportunity card shows its formula.",
    assumpFootNote: "Each assumption names its source and how it will be measured in the pilot.",
    btnReset: "Reset to defaults", srcLabel: "Source",
    kMap: "Prioritisation (F3)", hMap: "Value × feasibility",
    subMap: "Every opportunity plotted on the two F3 axes; the “high” threshold sits at 3.5. Colour = allocation (F4). Click a dot to open its card.",
    axisX: "feasibility →", axisY: "value →",
    qQw: "Quick wins", qBb: "Big bets", qFi: "Fill-ins", qDc: "Discard",
    legendHint: "click a dot for detail",
    kRegister: "Opportunities", hRegister: "Opportunity register",
    subRegister: "Each card shows the scores, the formula behind the amount, the cost estimate and the falsifiable verdict. Tick what goes into the roadmap; wave 1 is pre-selected.",
    fDept: "Department", fQuadrant: "Quadrant", fAlloc: "Allocation", fStatus: "Status", fAll: "all",
    sortValue: "sort: value", sortPayback: "sort: payback",
    noMatch: "No opportunities match this filter.",
    pick: "Include in roadmap",
    hScores: "Scores (F3)", hPains: "Linked pain points", hFormula: "Value formula",
    hCost: "Cost estimate", hPayback: "Payback", hVerdict: "Verdict",
    hWouldChange: "What would change this", hEnablers: "Enablers", hRisk: "Risk / AI Act",
    hFirstStep: "First step",
    valueW: "Value", feasW: "Feasibility", adoption: "Adoption",
    wHours: "hours", wQuality: "quality", wStrategic: "strategic",
    wData: "data", wTechnical: "technical", wOwnership: "ownership",
    confidence: "confidence", confMap: { high: "high", medium: "medium", low: "low" },
    perYear: "/yr", months: "mo", daysUnit: "d", hoursUnit: "h",
    costLine: "{days} d × {rate} + 12 × {tooling}/mo = {y1} in year 1",
    costLineNoTool: "{days} d × {rate} = {y1} in year 1",
    year1: "year-1 cost",
    kRoadmap: "Sequence", hRoadmap: "Roadmap in three waves",
    subRoadmap: "Wave totals count only the ticked opportunities and move with the assumptions. Struck through = not selected.",
    wave: "Wave", waveSubs: { 1: "0–3 months · quick wins", 2: "3–9 months · big bets + enablers", 3: "9–18 months · scale up" },
    waveTotals: "value {v}/yr · year-1 cost {c} · payback {p}",
    waveSelected: "{n} of {m} selected", waveEmpty: "No opportunities in this wave.",
    kKeep: "Deliberately not", hKeep: "What NOT to change",
    subKeep: "What works well today and what we deliberately leave alone — saying no is half of a roadmap.",
    kMethod: "Method", hMethod: "Method & caveats",
    methodWeights: "Scores follow F3: Value = {vw}; Feasibility = {fw}. “High” = ≥ {hi} on the axis; adoption (1–5) is the tie-breaker. Cost per opportunity = implementation days (effort baseline per allocation × T-shirt size) × day rate € {rate}, plus 12 × tooling/month. Payback = year-1 cost ÷ monthly value.",
    methodNote: "<strong>Directional, not audited.</strong> Self-reported time savings inflate 2–3× in practice; read every amount as a hypothesis, not a promise. Calibration path: each assumption above names its source; in the first pilot weeks, measurements replace the estimates and this proposal is recomputed with the same formulas. The effort baselines are conservative seeds, recalibrated after every engagement.",
    cbCount: "{n} selected", cbValue: "annual value {v}", cbCost: "year-1 cost {c}",
    cbBtn: "Confirm roadmap",
    dTitle: "Your roadmap selection",
    dSub: "This is what gets confirmed, at the current slider positions.",
    dNone: "Nothing selected yet.",
    dTotal: "Total: {v}/yr · year-1 cost {c} · payback {p}",
    dNote: "Download the JSON file and hand it to the consultant — it is recorded in proposal/decision-log.md.",
    dDownload: "Download JSON", dPrint: "Print", dClose: "Close",
    themeBtn: "◐ theme",
    alloc: { automation: "Automation", "agent-T1": "Agent T1", "agent-T2": "Agent T2", "agent-T3": "Agent T3", hybrid: "Hybrid" },
    quad: { "quick-win": "Quick win", "big-bet": "Big bet", "fill-in": "Fill-in", discard: "Discard" },
    status: { proposed: "proposed", confirmed: "confirmed", deferred: "deferred", discarded: "discarded" }
  }
};
var S = STR[lang];

/* ---------------- helpers ---------------- */
function esc(s) {
  return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
    .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
function L(x) { return typeof x === "string" ? x : (x && (x[lang] || x.nl || x.en)) || ""; }
function T(tpl, vars) {
  return tpl.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] != null ? vars[k] : m; });
}
function fmt(n) {
  if (!isFinite(n)) return "—";
  if (Math.abs(n) >= 1e6) return "€ " + (n / 1e6).toLocaleString(locale, { maximumFractionDigits: 2 }) + " m";
  if (Math.abs(n) >= 10000) return "€ " + Math.round(n / 1000).toLocaleString(locale) + " k";
  return "€ " + Math.round(n).toLocaleString(locale);
}
function fmtFull(n) { return isFinite(n) ? "€ " + Math.round(n).toLocaleString(locale) : "—"; }
function dec(n) { return n.toLocaleString(locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 }); }
function fmtMonths(m) { return (isFinite(m) && m >= 0) ? dec(m) + " " + S.months : "—"; }

/* ---------------- state — the single render source ---------------- */
var state = { A: {}, filters: { dept: "all", quadrant: "all", alloc: "all", status: "all" }, sort: "value", selected: {} };
DATA.assumptions.forEach(function (a) { state.A[a.id] = a.default; });
DATA.opps.forEach(function (o) { if (o.wave === 1 && o.verdict !== "discard") state.selected[o.id] = true; });

var FORMULAS = DATA.formulas || {};
function oppValue(o) {
  var f = FORMULAS[o.id];
  return f ? f(state.A) : NaN;
}
function oppPayback(o) {
  var v = oppValue(o);
  return (isFinite(v) && v > 0) ? o.year1_cost / (v / 12) : Infinity;
}
function portfolio() { return DATA.opps.filter(function (o) { return o.wave >= 1 && o.verdict !== "discard"; }); }
function selectedOpps() { return DATA.opps.filter(function (o) { return state.selected[o.id]; }); }
function matchesFilters(o) {
  var f = state.filters;
  if (f.dept !== "all" && o.departments.indexOf(f.dept) === -1) return false;
  if (f.quadrant !== "all" && o.quadrant !== f.quadrant) return false;
  if (f.alloc !== "all" && o.allocation !== f.alloc) return false;
  if (f.status !== "all" && o.status !== f.status) return false;
  return true;
}
var ASSUMP_LABEL = {};
DATA.assumptions.forEach(function (a) { ASSUMP_LABEL[a.id] = L(a.label); });
function readableFormula(o) {
  if (!o.formula_text) return "";
  var s = o.formula_text.replace(/[A-Za-z_][A-Za-z0-9_]*/g, function (id) {
    return ASSUMP_LABEL[id] ? "[" + ASSUMP_LABEL[id] + "]" : id;
  });
  return s.replace(/\*/g, "×").replace(/\//g, "÷");
}

/* ---------------- static chrome ---------------- */
function initChrome() {
  document.documentElement.lang = lang;
  document.documentElement.style.setProperty("--accent", DATA.accent);
  document.querySelectorAll("[data-i18n]").forEach(function (el) {
    var v = S[el.getAttribute("data-i18n")];
    if (typeof v === "string") el.textContent = v;
  });
  document.getElementById("hero-title").textContent = T(S.heroTitle, { client: DATA.client });
  document.getElementById("hero-lede").textContent = T(S.heroLede, { n: DATA.assumptions.length });
  document.getElementById("hero-stamp").textContent =
    T(S.heroStamp, { date: DATA.built.slice(0, 10), sector: DATA.sector || DATA.client });
  var w = DATA.weights;
  function wline(spec, names) {
    return Object.keys(spec).map(function (k) {
      return spec[k].toLocaleString(locale, { minimumFractionDigits: 2 }) + "×" + names[k];
    }).join(" + ");
  }
  document.getElementById("method-weights").textContent = T(S.methodWeights, {
    vw: wline(w.value, { hours: S.wHours, quality: S.wQuality, strategic: S.wStrategic }),
    fw: wline(w.feasibility, { data: S.wData, technical: S.wTechnical, ownership: S.wOwnership }),
    hi: dec(w.high), rate: Math.round(DATA.day_rate).toLocaleString(locale)
  });
  document.getElementById("method-note").innerHTML = S.methodNote;
  /* keep.md passthrough — hide section when absent */
  var keep = document.getElementById("keep"), keepNav = document.getElementById("nav-keep");
  if (DATA.keep_html) document.getElementById("keep-body").innerHTML = DATA.keep_html;
  else { keep.style.display = "none"; keepNav.style.display = "none"; }
  document.getElementById("cb-btn").textContent = S.cbBtn;
  if (!DATA.hourly_id) document.getElementById("st-hours-tile").style.display = "none";
}

/* ---------------- theme toggle (data-theme wins over @media) ---------------- */
function initTheme() {
  var btn = document.getElementById("theme-toggle");
  btn.textContent = S.themeBtn;
  function effective() {
    return document.documentElement.getAttribute("data-theme") ||
      (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  }
  btn.addEventListener("click", function () {
    var next = effective() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    btn.setAttribute("aria-pressed", String(next === "dark"));
    renderScatter(); // colors resolve via CSS vars; re-render keeps labels crisp
  });
}

/* ---------------- assumptions ---------------- */
function assumpDisplay(a, v) {
  var num = v.toLocaleString(locale);
  return a.unit ? num + " " + a.unit : num;
}
function initAssumptions() {
  var grid = document.getElementById("assump-grid");
  grid.innerHTML = DATA.assumptions.map(function (a) {
    return '<label><span class="row"><span>' + esc(L(a.label)) + '</span>' +
      '<output id="o-' + esc(a.id) + '">' + esc(assumpDisplay(a, a.default)) + "</output></span>" +
      '<input type="range" id="a-' + esc(a.id) + '" min="' + a.min + '" max="' + a.max +
      '" step="' + a.step + '" value="' + a.default + '" aria-label="' + esc(L(a.label)) + '">' +
      (a.source ? '<span class="src">' + esc(S.srcLabel) + ": " + esc(a.source) + "</span>" : "") +
      "</label>";
  }).join("");
  DATA.assumptions.forEach(function (a) {
    var input = document.getElementById("a-" + a.id), out = document.getElementById("o-" + a.id);
    input.addEventListener("input", function () {
      state.A[a.id] = +input.value;
      out.textContent = assumpDisplay(a, +input.value);
      rerender();
    });
  });
  document.getElementById("assump-reset").addEventListener("click", function () {
    DATA.assumptions.forEach(function (a) {
      state.A[a.id] = a.default;
      document.getElementById("a-" + a.id).value = a.default;
      document.getElementById("o-" + a.id).textContent = assumpDisplay(a, a.default);
    });
    rerender();
  });
}

/* ---------------- headline ---------------- */
function renderHeadline() {
  var port = portfolio(), total = 0, y1 = 0, hourVal = 0;
  port.forEach(function (o) {
    var v = oppValue(o);
    if (isFinite(v)) { total += v; if (o.uses_hourly) hourVal += v; }
    y1 += o.year1_cost;
  });
  document.getElementById("st-total").textContent = fmt(total);
  document.getElementById("st-wave1").textContent = port.filter(function (o) { return o.wave === 1; }).length;
  document.getElementById("st-payback").textContent = total > 0 ? fmtMonths(y1 / (total / 12)) : "—";
  if (DATA.hourly_id) {
    var hc = state.A[DATA.hourly_id];
    document.getElementById("st-hours").textContent =
      hc > 0 ? "≈ " + Math.round(hourVal / hc).toLocaleString(locale) + " " + S.hoursUnit : "—";
  }
}

/* ---------------- filters ---------------- */
function uniq(arr) { return arr.filter(function (v, i) { return arr.indexOf(v) === i; }); }
function renderFilters() {
  var f = document.getElementById("reg-filters");
  var depts = uniq([].concat.apply([], DATA.opps.map(function (o) { return o.departments; }))).sort();
  var allocs = uniq(DATA.opps.map(function (o) { return o.allocation; }));
  var statuses = uniq(DATA.opps.map(function (o) { return o.status; }));
  var quads = ["quick-win", "big-bet", "fill-in", "discard"].filter(function (q) {
    return DATA.opps.some(function (o) { return o.quadrant === q; });
  });
  function group(label, key, values, names) {
    var h = '<span class="glabel">' + esc(label) + "</span>";
    h += '<button data-g="' + key + '" data-v="all"' + (state.filters[key] === "all" ? ' class="on"' : "") + ">" + esc(S.fAll) + "</button>";
    values.forEach(function (v) {
      h += '<button data-g="' + key + '" data-v="' + esc(v) + '"' + (state.filters[key] === v ? ' class="on"' : "") + ">" +
        esc(names ? names[v] || v : v) + "</button>";
    });
    return h;
  }
  var html = group(S.fDept, "dept", depts) + '<span class="sep"></span>' +
    group(S.fQuadrant, "quadrant", quads, S.quad) + '<span class="sep"></span>' +
    group(S.fAlloc, "alloc", allocs, S.alloc) + '<span class="sep"></span>' +
    group(S.fStatus, "status", statuses, S.status) + '<span class="sep"></span>' +
    '<button data-sort="value"' + (state.sort === "value" ? ' class="on"' : "") + ">" + esc(S.sortValue) + "</button>" +
    '<button data-sort="payback"' + (state.sort === "payback" ? ' class="on"' : "") + ">" + esc(S.sortPayback) + "</button>";
  f.innerHTML = html;
  f.querySelectorAll("button").forEach(function (b) {
    b.addEventListener("click", function () {
      if (b.hasAttribute("data-sort")) state.sort = b.getAttribute("data-sort");
      else {
        var g = b.getAttribute("data-g"), v = b.getAttribute("data-v");
        state.filters[g] = (state.filters[g] === v) ? "all" : v;
      }
      renderFilters(); renderRegister(); renderScatter();
    });
  });
}

/* ---------------- register ---------------- */
var QCHIP = { "quick-win": "qw", "big-bet": "bb", "fill-in": "fi", discard: "dc" };
function allocVar(a) { return "var(--c-" + a.toLowerCase() + ")"; }
function scoreLine(o) {
  var w = DATA.weights, s = o.scores;
  var v = "<b>" + S.valueW + " " + dec(o.value) + "</b> = " +
    w.value.hours.toLocaleString(locale) + "×" + s.hours + " " + S.wHours + " + " +
    w.value.quality.toLocaleString(locale) + "×" + s.quality + " " + S.wQuality + " + " +
    w.value.strategic.toLocaleString(locale) + "×" + s.strategic + " " + S.wStrategic;
  var f = "<b>" + S.feasW + " " + dec(o.feasibility) + "</b> = " +
    w.feasibility.data.toLocaleString(locale) + "×" + s.data + " " + S.wData + " + " +
    w.feasibility.technical.toLocaleString(locale) + "×" + s.technical + " " + S.wTechnical + " + " +
    w.feasibility.ownership.toLocaleString(locale) + "×" + s.ownership + " " + S.wOwnership;
  return v + "<br>" + f + "<br><b>" + S.adoption + " " + s.adoption + "/5</b>";
}
function costLine(o) {
  var tpl = o.tooling > 0 ? S.costLine : S.costLineNoTool;
  return T(tpl, {
    days: o.days, rate: fmtFull(DATA.day_rate), tooling: fmtFull(o.tooling), y1: "<strong>" + fmtFull(o.year1_cost) + "</strong>"
  });
}
function renderRegister() {
  var list = DATA.opps.filter(matchesFilters);
  list.sort(state.sort === "value"
    ? function (a, b) { return (isFinite(oppValue(b)) ? oppValue(b) : -1) - (isFinite(oppValue(a)) ? oppValue(a) : -1); }
    : function (a, b) { return oppPayback(a) - oppPayback(b); });
  var open = {};
  document.querySelectorAll("#reg-list details[open]").forEach(function (d) { open[d.id] = true; });
  document.getElementById("reg-list").innerHTML = list.map(function (o) {
    var v = oppValue(o), isDiscard = o.verdict === "discard";
    var conf = S.confMap[(o.confidence || "").toLowerCase()] || o.confidence || "";
    var pains = o.pains.map(function (p) { return '<span class="chip plain">' + esc(p) + "</span>"; }).join(" ");
    var procs = o.processes.map(function (p) { return '<span class="chip plain">' + esc(p) + "</span>"; }).join(" ");
    return '<details class="opp' + (isDiscard ? " discard" : "") + '" id="d-' + o.id + '"' + (open["d-" + o.id] ? " open" : "") + ">" +
      "<summary>" +
      (!isDiscard ? '<input type="checkbox" class="pick" data-id="' + o.id + '"' +
        (state.selected[o.id] ? " checked" : "") + ' aria-label="' + esc(S.pick) + " " + o.id + '">' : "") +
      '<span class="oid">' + o.id + '</span><span class="ot">' + esc(o.title) + "</span>" +
      '<span class="chip plain"><i style="background:' + allocVar(o.allocation) + '"></i>' + esc(S.alloc[o.allocation] || o.allocation) + "</span>" +
      '<span class="chip ' + QCHIP[o.quadrant] + '">' + esc(S.quad[o.quadrant]) + "</span>" +
      '<span class="chip plain">' + (o.wave >= 1 ? S.wave + " " + o.wave : "—") + " · " + esc(o.effort) + "</span>" +
      '<span class="ov">' + (isFinite(v) ? fmt(v) + S.perYear : "—") + "</span>" +
      "</summary>" +
      '<div class="o-body">' +
      "<div><h4>" + S.hScores + '</h4><p class="scoreline">' + scoreLine(o) + "</p></div>" +
      "<div><h4>" + S.hPains + "</h4><p>" + (pains || "—") + (procs ? "<br>" + procs : "") + "</p></div>" +
      (o.formula_text
        ? '<div class="full"><h4>' + S.hFormula + "</h4><p><code>" + esc(readableFormula(o)) + "</code> = <strong>" +
          fmt(v) + S.perYear + "</strong></p></div>" : "") +
      "<div><h4>" + S.hCost + "</h4><p>" + costLine(o) + "</p></div>" +
      "<div><h4>" + S.hPayback + "</h4><p><strong>" + fmtMonths(oppPayback(o)) + "</strong></p></div>" +
      '<div class="full"><h4>' + S.hVerdict + '</h4><p><span class="chip ' + QCHIP[o.verdict] + '">' + esc(S.quad[o.verdict]) + "</span>" +
      (conf ? " · " + S.confidence + ": <strong>" + esc(conf) + "</strong>" : "") +
      (o.would_change ? "<br><em>" + S.hWouldChange + ":</em> " + esc(o.would_change) : "") + "</p></div>" +
      (o.enablers ? "<div><h4>" + S.hEnablers + "</h4><p>" + esc(o.enablers) + "</p></div>" : "") +
      (o.risk ? "<div><h4>" + S.hRisk + "</h4><p>" + esc(o.risk) + "</p></div>" : "") +
      (o.first_step ? '<div class="full"><h4>' + S.hFirstStep + "</h4><p>" + esc(o.first_step) + "</p></div>" : "") +
      "</div></details>";
  }).join("") || '<p class="sub">' + esc(S.noMatch) + "</p>";
  document.querySelectorAll("#reg-list .pick").forEach(function (cb) {
    cb.addEventListener("click", function (e) { e.stopPropagation(); });
    cb.addEventListener("change", function () {
      if (cb.checked) state.selected[cb.getAttribute("data-id")] = true;
      else delete state.selected[cb.getAttribute("data-id")];
      renderRoadmap(); renderConfirmBar();
    });
  });
}
function openCard(id) {
  var el = document.getElementById("d-" + id);
  if (!el) {
    state.filters = { dept: "all", quadrant: "all", alloc: "all", status: "all" };
    renderFilters(); renderRegister(); renderScatter();
    el = document.getElementById("d-" + id);
  }
  if (el) { el.open = true; el.scrollIntoView({ behavior: "smooth", block: "center" }); }
}

/* ---------------- quadrant scatter ---------------- */
function renderLegend() {
  var allocs = uniq(DATA.opps.map(function (o) { return o.allocation; }));
  document.getElementById("viz-legend").innerHTML = allocs.map(function (a) {
    return '<span class="chip plain"><i style="background:' + allocVar(a) + '"></i>' + esc(S.alloc[a] || a) + "</span>";
  }).join("") + '<span style="margin-left:auto;color:var(--ink-3);font-size:11.5px">' + esc(S.legendHint) + "</span>";
}
function renderScatter() {
  var W = 940, H = 470, mL = 56, mR = 30, mT = 26, mB = 46;
  var iw = W - mL - mR, ih = H - mT - mB;
  var lo = 0.8, hiD = 5.2, span = hiD - lo;
  var X = function (s) { return mL + ((s - lo) / span) * iw; };
  var Y = function (s) { return mT + ih - ((s - lo) / span) * ih; };
  var bx = X(DATA.weights.high), by = Y(DATA.weights.high);
  var s = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(S.hMap) + '">';
  /* quadrant shading */
  s += '<rect class="qbg" x="' + bx + '" y="' + mT + '" width="' + (W - mR - bx) + '" height="' + (by - mT) + '" fill="var(--accent)" opacity=".06"/>';
  s += '<rect class="qbg" x="' + mL + '" y="' + by + '" width="' + (bx - mL) + '" height="' + (mT + ih - by) + '" fill="var(--ink)" opacity=".045"/>';
  /* gridlines (pointer-events:none via CSS) */
  for (var g = 1; g <= 5; g++) {
    s += '<line x1="' + X(g) + '" y1="' + mT + '" x2="' + X(g) + '" y2="' + (mT + ih) + '" stroke="var(--grid)" stroke-width="1"/>';
    s += '<line x1="' + mL + '" y1="' + Y(g) + '" x2="' + (W - mR) + '" y2="' + Y(g) + '" stroke="var(--grid)" stroke-width="1"/>';
    s += '<text class="axl" x="' + X(g) + '" y="' + (H - mB + 16) + '" text-anchor="middle">' + g + "</text>";
    s += '<text class="axl" x="' + (mL - 10) + '" y="' + (Y(g) + 4) + '" text-anchor="end">' + g + "</text>";
  }
  /* the 3.5 boundary */
  s += '<line x1="' + bx + '" y1="' + mT + '" x2="' + bx + '" y2="' + (mT + ih) + '" stroke="var(--ink-3)" stroke-dasharray="4 4" stroke-width="1.2"/>';
  s += '<line x1="' + mL + '" y1="' + by + '" x2="' + (W - mR) + '" y2="' + by + '" stroke="var(--ink-3)" stroke-dasharray="4 4" stroke-width="1.2"/>';
  /* quadrant labels */
  s += '<text class="quad" x="' + (W - mR - 8) + '" y="' + (mT + 16) + '" text-anchor="end">' + esc(S.qQw) + "</text>";
  s += '<text class="quad" x="' + (mL + 8) + '" y="' + (mT + 16) + '">' + esc(S.qBb) + "</text>";
  s += '<text class="quad" x="' + (W - mR - 8) + '" y="' + (mT + ih - 10) + '" text-anchor="end">' + esc(S.qFi) + "</text>";
  s += '<text class="quad" x="' + (mL + 8) + '" y="' + (mT + ih - 10) + '">' + esc(S.qDc) + "</text>";
  /* axis titles */
  s += '<text class="axl" x="' + (mL + iw / 2) + '" y="' + (H - 8) + '" text-anchor="middle">' + esc(S.axisX) + "</text>";
  s += '<text class="axl" transform="translate(16 ' + (mT + ih / 2) + ') rotate(-90)" text-anchor="middle">' + esc(S.axisY) + "</text>";
  /* dots — jitter same-position groups ≥52px apart, labels to the right */
  var groups = {};
  DATA.opps.forEach(function (o) {
    var k = o.feasibility.toFixed(2) + "|" + o.value.toFixed(2);
    (groups[k] = groups[k] || []).push(o);
  });
  Object.keys(groups).forEach(function (k) {
    groups[k].forEach(function (o, i) {
      var n = groups[k].length;
      var off = n > 1 ? (i - (n - 1) / 2) * 60 : 0; /* >=52px so dot + label clear the neighbour */
      var cx = Math.max(mL + 12, Math.min(W - mR - 12, X(o.feasibility) + off));
      var cy = Y(o.value);
      var dim = matchesFilters(o) ? "" : " dim";
      s += '<g class="pt' + dim + '" data-opp="' + o.id + '" tabindex="0" style="cursor:pointer" role="button" aria-label="' + o.id + " " + esc(o.title) + '">' +
        '<circle cx="' + cx + '" cy="' + cy + '" r="9" fill="' + allocVar(o.allocation) + '" stroke="var(--card)" stroke-width="2"' +
        (o.verdict === "discard" ? ' fill-opacity=".45"' : "") + "/>" +
        '<text class="dotl" x="' + (cx + 12) + '" y="' + (cy + 4) + '">' + o.id + "</text></g>";
    });
  });
  s += "</svg>";
  document.getElementById("scatter").innerHTML = s;
  var tip = document.getElementById("tip");
  document.querySelectorAll("#scatter .pt").forEach(function (g) {
    var o = DATA.opps.find(function (x) { return x.id === g.getAttribute("data-opp"); });
    function show(ev) {
      var v = oppValue(o);
      tip.innerHTML = "<b>" + o.id + " · " + esc(o.title) + "</b>" +
        '<span class="figure">' + S.valueW + " " + dec(o.value) + " · " + S.feasW + " " + dec(o.feasibility) +
        (isFinite(v) ? " · " + fmt(v) + S.perYear : "") + " · " + fmtMonths(oppPayback(o)) + "</span><br>" +
        '<span class="chip ' + QCHIP[o.quadrant] + '">' + esc(S.quad[o.quadrant]) + "</span>";
      tip.style.display = "block";
      var p = ev.touches ? ev.touches[0] : ev;
      tip.style.left = Math.min(p.clientX + 14, window.innerWidth - 320) + "px";
      tip.style.top = (p.clientY + 14) + "px";
    }
    g.addEventListener("mousemove", show);
    g.addEventListener("mouseleave", function () { tip.style.display = "none"; });
    g.addEventListener("click", function () { tip.style.display = "none"; openCard(o.id); });
    g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openCard(o.id); } });
  });
}

/* ---------------- roadmap waves ---------------- */
function renderRoadmap() {
  var el = document.getElementById("waves");
  el.innerHTML = [1, 2, 3].map(function (w) {
    var items = DATA.opps.filter(function (o) { return o.wave === w; })
      .sort(function (a, b) { return (oppValue(b) || 0) - (oppValue(a) || 0); });
    var sel = items.filter(function (o) { return state.selected[o.id]; });
    var v = 0, c = 0;
    sel.forEach(function (o) { var x = oppValue(o); if (isFinite(x)) v += x; c += o.year1_cost; });
    var pb = v > 0 ? c / (v / 12) : Infinity;
    return '<div class="wave"><div class="w-h"><div class="t">' + S.wave + " " + w + '</div>' +
      '<div class="s">' + esc(S.waveSubs[w]) + " · " + T(S.waveSelected, { n: sel.length, m: items.length }) + "</div>" +
      '<div class="v">' + T(S.waveTotals, { v: fmt(v), c: fmt(c), p: fmtMonths(pb) }) + "</div></div><ul>" +
      (items.length ? items.map(function (o) {
        var x = oppValue(o);
        return '<li class="' + (state.selected[o.id] ? "" : "off") + '">' +
          '<span class="oref" data-opp="' + o.id + '">' + o.id + "</span> · " + esc(o.title) +
          (isFinite(x) ? ' <span class="liv">' + fmt(x) + S.perYear + "</span>" : "") + "</li>";
      }).join("") : "<li>" + esc(S.waveEmpty) + "</li>") +
      "</ul></div>";
  }).join("");
  el.querySelectorAll(".oref").forEach(function (r) {
    r.addEventListener("click", function () { openCard(r.getAttribute("data-opp")); });
  });
}

/* ---------------- select & confirm ---------------- */
function selectionTotals() {
  var v = 0, c = 0;
  selectedOpps().forEach(function (o) { var x = oppValue(o); if (isFinite(x)) v += x; c += o.year1_cost; });
  return { n: selectedOpps().length, value: v, cost: c, payback: v > 0 ? c / (v / 12) : Infinity };
}
function renderConfirmBar() {
  var t = selectionTotals();
  document.getElementById("cb-count").innerHTML = T(esc(S.cbCount), { n: "<b>" + t.n + "</b>" });
  document.getElementById("cb-value").innerHTML = T(esc(S.cbValue), { v: "<b>" + fmt(t.value) + S.perYear + "</b>" });
  document.getElementById("cb-cost").innerHTML = T(esc(S.cbCost), { c: "<b>" + fmt(t.cost) + "</b>" });
  document.getElementById("cb-btn").disabled = t.n === 0;
}
function buildExport() {
  var sel = { wave1: [], wave2: [], wave3: [] };
  selectedOpps().forEach(function (o) { if (o.wave >= 1) sel["wave" + o.wave].push(o.id); });
  var t = selectionTotals();
  return {
    client: DATA.client, slug: DATA.slug, language: lang,
    date: DATA.built,                       /* build timestamp of this proposal */
    confirmed_at: new Date().toISOString(), /* moment of confirmation */
    selections: sel,
    assumptions: JSON.parse(JSON.stringify(state.A)),
    totals: { annual_value: Math.round(t.value), year1_cost: Math.round(t.cost) }
  };
}
function initConfirm() {
  var dlg = document.getElementById("confirm-dialog");
  document.getElementById("cb-btn").addEventListener("click", function () {
    var body = document.getElementById("d-body"), t = selectionTotals();
    body.innerHTML = [1, 2, 3].map(function (w) {
      var sel = selectedOpps().filter(function (o) { return o.wave === w; });
      if (!sel.length) return "";
      return "<h4>" + S.wave + " " + w + "</h4><ul>" + sel.map(function (o) {
        return '<li><span class="oid">' + o.id + "</span> " + esc(o.title) +
          ' <span class="figure">· ' + fmt(oppValue(o)) + S.perYear + "</span></li>";
      }).join("") + "</ul>";
    }).join("") || "<p>" + esc(S.dNone) + "</p>";
    document.getElementById("d-total").textContent =
      T(S.dTotal, { v: fmt(t.value), c: fmt(t.cost), p: fmtMonths(t.payback) });
    var a = document.getElementById("d-download");
    a.setAttribute("download", "roadmap-" + DATA.slug.replace(/^_+/, "") + "-confirmed.json");
    a.href = "data:application/json;charset=utf-8," + encodeURIComponent(JSON.stringify(buildExport(), null, 2));
    dlg.showModal();
  });
  /* refresh the payload right before download in case sliders moved while open */
  document.getElementById("d-download").addEventListener("click", function () {
    this.href = "data:application/json;charset=utf-8," + encodeURIComponent(JSON.stringify(buildExport(), null, 2));
  });
  document.getElementById("d-print").addEventListener("click", function () { dlg.close(); window.print(); });
  document.getElementById("d-close").addEventListener("click", function () { dlg.close(); });
}

/* ---------------- one render path ---------------- */
function rerender() {
  renderHeadline(); renderRegister(); renderScatter(); renderRoadmap(); renderConfirmBar();
}
initChrome(); initTheme(); initAssumptions(); initConfirm();
renderFilters(); renderLegend(); rerender();
})();
