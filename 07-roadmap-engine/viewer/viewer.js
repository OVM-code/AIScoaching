/* Roadmap Engine — AS-IS interactive viewer.
 * Consumes window.ASIS (injected at build time by tools/build_asis.py):
 *   client      {name, title, sector, language, intro_html, labels{}}
 *   meta        {catalog, version, generated}
 *   departments [{number, id, title, intro_html, status, process, processes:[codes]}]
 *   processes   { code: {code,title,department,severity,automability,pains:[uids],fields{},html} }
 *   coverage    [{code,title,department,scope,severity,note}]
 *   pains       [{uid,id,department,title,quote,source,type,severity,volume,value,processes:[],html}]
 * Severity: "none" | "minor" | "major" | "critical"; undocumented steps render "undoc".
 * Automability: "human" | "automation" | "agent" | "hybrid"; absent renders "neutral".
 * Modes: "pijn" (color by severity, default) | "kansen" (color by automability).
 */
(function () {
  "use strict";
  var D = window.ASIS;
  if (!D) { document.getElementById("app").textContent = "Geen AS-IS-data gevonden."; return; }

  // Built-in language packs. Add a language: add a key here (and translate the
  // flow labels); per-client overrides go in engagement-config.json "labels".
  var LANGS = {
    nl: {
      intro: "Inleiding", processes: "Processen", pains: "Pijnpunten",
      search: "Zoek proces of pijnpunt…", inScope: "in scope", outScope: "buiten scope",
      noResults: "Geen resultaten", allProcesses: "Alle processen in deze afdeling",
      gotoProcess: "Ga naar processtroom", linkedPains: "Gekoppelde pijnpunten",
      deptDocOnly: "Voor deze afdeling is geen processtroom gedefinieerd; de processen staan hieronder.",
      scopeCols: ["Code", "Proces", "Afdeling", "Scope", "Severity", "Reden"],
      filterAll: "alle", generated: "opgemaakt", statusLbl: "status",
      modePijn: "Pijn", modeKansen: "Kansen",
      sev: { none: "Loopt goed", minor: "Lichte frictie", major: "Structurele pijn",
             critical: "Kritiek", undoc: "Niet gedocumenteerd" },
      auto: { human: "Mens", automation: "Automatisering", agent: "AI-agent",
              hybrid: "Hybride", neutral: "Nog niet ingeschat" },
      ptype: { retype: "hertypen", chase: "achternalopen", wait: "wachten", error: "fouten",
               "skill-bottleneck": "kennis-bottleneck", "no-visibility": "geen zicht" },
      fields: { werkwijze: "Huidige werkwijze", wie: "Wie", systemen: "Systemen", volume: "Volume & tijd" },
      severityHdr: "severity", typeHdr: "type", volumeLbl: "Volume", valueLbl: "Waardehypothese",
      register: "register",
      exportBtn: "PDF exporteren", exportTitle: "Exporteer als PDF",
      exportHint: "Kies wat het document bevat. Het afdrukvenster opent — kies daar ‘Opslaan als PDF’.",
      exportDepts: "Afdelingen", exportParts: "Onderdelen",
      exportAllNone: "alles / niets", exportGo: "Maak PDF", exportCancel: "Annuleer",
      toc: "Inhoud", coverClient: "Klant", coverSector: "Sector",
      coverVersion: "Versie", coverDate: "Datum", coverCatalog: "Procescatalogus"
    },
    en: {
      intro: "Introduction", processes: "Processes", pains: "Pain points",
      search: "Search process or pain point…", inScope: "in scope", outScope: "out of scope",
      noResults: "No results", allProcesses: "All processes in this department",
      gotoProcess: "Go to process flow", linkedPains: "Linked pain points",
      deptDocOnly: "No process flow is defined for this department; its processes are listed below.",
      scopeCols: ["Code", "Process", "Department", "Scope", "Severity", "Reason"],
      filterAll: "all", generated: "generated", statusLbl: "status",
      modePijn: "Pain", modeKansen: "Opportunities",
      sev: { none: "Runs fine", minor: "Minor friction", major: "Structural pain",
             critical: "Critical", undoc: "Not documented" },
      auto: { human: "Human", automation: "Automation", agent: "AI agent",
              hybrid: "Hybrid", neutral: "Not yet assessed" },
      ptype: { retype: "retype", chase: "chase", wait: "wait", error: "errors",
               "skill-bottleneck": "skill bottleneck", "no-visibility": "no visibility" },
      fields: { werkwijze: "Current way of working", wie: "Who", systemen: "Systems", volume: "Volume & time" },
      severityHdr: "severity", typeHdr: "type", volumeLbl: "Volume", valueLbl: "Value hypothesis",
      register: "register",
      exportBtn: "Export PDF", exportTitle: "Export as PDF",
      exportHint: "Choose what the document contains. The print dialog opens — pick ‘Save as PDF’ there.",
      exportDepts: "Departments", exportParts: "Sections",
      exportAllNone: "all / none", exportGo: "Create PDF", exportCancel: "Cancel",
      toc: "Contents", coverClient: "Client", coverSector: "Sector",
      coverVersion: "Version", coverDate: "Date", coverCatalog: "Process catalog"
    }
  };
  var lang = D.client.language || "nl";
  document.documentElement.lang = lang;
  var L = Object.assign({}, LANGS.nl, LANGS[lang] || {}, D.client.labels || {});
  ["sev", "auto", "ptype", "fields"].forEach(function (k) {
    L[k] = Object.assign({}, LANGS.nl[k], (LANGS[lang] || {})[k] || {}, (D.client.labels || {})[k] || {});
  });

  // Flow labels may be plain strings or {nl: "...", en: "..."} objects.
  function lbl(v) {
    if (v && typeof v === "object") return v[lang] || v.nl || v.en || "";
    return v || "";
  }

  var app = document.getElementById("app");
  var mode = "pijn"; // "pijn" | "kansen"
  var deptByNum = {};
  D.departments.forEach(function (d) { deptByNum[d.number] = d; });
  var painByUid = {};
  D.pains.forEach(function (p) { painByUid[p.uid] = p; });

  /* ---------------- helpers ---------------- */
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function proc(code) { return D.processes[code]; }
  function sevOf(code) {
    var s = proc(code);
    return s ? (s.severity || "none") : "undoc";
  }
  function autoOf(code) {
    var s = proc(code);
    if (!s) return null; // undocumented: stays grey dashed in both modes
    return s.automability || "neutral";
  }
  function sevChip(sev) {
    return '<span class="chip sev-' + esc(sev) + '">' + esc(L.sev[sev] || sev) + "</span>";
  }
  function autoChip(a) {
    return '<span class="chip auto-' + esc(a) + '">' + esc(L.auto[a] || a) + "</span>";
  }
  function wrapText(text, max) {
    var words = String(text).split(/\s+/), lines = [], cur = "";
    words.forEach(function (w) {
      if ((cur + " " + w).trim().length > max && cur) { lines.push(cur); cur = w; }
      else cur = (cur + " " + w).trim();
    });
    if (cur) lines.push(cur);
    return lines;
  }

  /* ---------------- BPMN layout (ported intact from the BPA viewer) ---------------- */
  var NW = 176, NH = 56, GX = 78, ROW = 92, LANE_PAD = 14, CORR = 34, LBL_W = 34, M = 16;

  function shapeHalf(n) {
    if (n.type === "start" || n.type === "end") return { w: 20, h: 20 };
    if (n.type.indexOf("gateway") === 0) return { w: 26, h: 26 };
    return { w: NW / 2, h: NH / 2 };
  }

  function layoutProcess(p) {
    var byId = {}, out = {}, incoming = {};
    p.nodes.forEach(function (n) { byId[n.id] = n; out[n.id] = []; incoming[n.id] = 0; });
    p.flows.forEach(function (f) { out[f.from].push(f.to); });

    // classify back edges with DFS from start nodes (then any unvisited)
    var back = {}, state = {}; // 0 unseen, 1 on stack, 2 done
    function dfs(u) {
      state[u] = 1;
      out[u].forEach(function (v) {
        if (state[v] === 1) back[u + ">" + v] = true;
        else if (!state[v]) dfs(v);
      });
      state[u] = 2;
    }
    p.nodes.filter(function (n) { return n.type === "start"; }).forEach(function (n) { if (!state[n.id]) dfs(n.id); });
    p.nodes.forEach(function (n) { if (!state[n.id]) dfs(n.id); });

    var fwd = p.flows.filter(function (f) { return !back[f.from + ">" + f.to]; });
    fwd.forEach(function (f) { incoming[f.to]++; });

    // longest-path layering (Kahn)
    var layer = {}, q = [];
    p.nodes.forEach(function (n) { layer[n.id] = 0; if (!incoming[n.id]) q.push(n.id); });
    var order = [], deg = Object.assign({}, incoming);
    while (q.length) {
      var u = q.shift(); order.push(u);
      fwd.forEach(function (f) {
        if (f.from !== u) return;
        if (layer[f.to] < layer[u] + 1) layer[f.to] = layer[u] + 1;
        if (--deg[f.to] === 0) q.push(f.to);
      });
    }

    // rows per (lane, layer)
    var laneIdx = {}, laneRows = {};
    p.lanes.forEach(function (l, i) { laneIdx[l.id] = i; laneRows[l.id] = 1; });
    var cellCount = {};
    var rowOf = {};
    p.nodes.forEach(function (n) {
      var key = n.lane + "|" + layer[n.id];
      rowOf[n.id] = cellCount[key] = (cellCount[key] || 0);
      cellCount[key]++;
      if (cellCount[key] > laneRows[n.lane]) laneRows[n.lane] = cellCount[key];
    });

    var lanes = [], y = M;
    p.lanes.forEach(function (l) {
      var h = LANE_PAD * 2 + laneRows[l.id] * ROW + CORR;
      lanes.push({ id: l.id, label: l.label, y: y, h: h });
      y += h;
    });
    var laneBy = {}; lanes.forEach(function (l) { laneBy[l.id] = l; });

    var maxLayer = 0;
    p.nodes.forEach(function (n) { if (layer[n.id] > maxLayer) maxLayer = layer[n.id]; });
    var width = M + LBL_W + (maxLayer + 1) * (NW + GX) - GX + M + 60;
    var height = y + M;

    var pos = {};
    p.nodes.forEach(function (n) {
      var ln = laneBy[n.lane];
      pos[n.id] = {
        node: n,
        cx: M + LBL_W + layer[n.id] * (NW + GX) + NW / 2,
        cy: ln.y + LANE_PAD + rowOf[n.id] * ROW + ROW / 2 - CORR / 4,
        layer: layer[n.id]
      };
    });

    // route edges
    var edges = p.flows.map(function (f) {
      var s = pos[f.from], t = pos[f.to];
      var sh = shapeHalf(s.node), th = shapeHalf(t.node);
      var pts, labelAt;
      var isBack = back[f.from + ">" + f.to] || t.layer <= s.layer;
      if (!isBack && t.layer - s.layer > 1) {
        // long edge: route through the node-free corridor at the bottom of the
        // source lane so it never crosses nodes in the layers it skips
        var lnS = laneBy[s.node.lane];
        var corrY = lnS.y + lnS.h - CORR / 2;
        var xo = s.cx + sh.w, xi = t.cx - th.w;
        pts = [[xo, s.cy], [xo + GX / 2 - 8, s.cy], [xo + GX / 2 - 8, corrY],
               [xi - GX / 2 + 8, corrY], [xi - GX / 2 + 8, t.cy], [xi, t.cy]];
        labelAt = [xo + 8, s.cy - 7];
      } else if (!isBack) {
        var x0 = s.cx + sh.w, x1 = t.cx - th.w;
        if (Math.abs(s.cy - t.cy) < 2) {
          pts = [[x0, s.cy], [x1, t.cy]];
        } else {
          var mx = x1 - GX / 2 + 8;
          pts = [[x0, s.cy], [mx, s.cy], [mx, t.cy], [x1, t.cy]];
        }
        labelAt = [x0 + 8, s.cy - 7];
      } else {
        var ln = laneBy[s.node.lane];
        var cy = ln.y + ln.h - CORR / 2;
        pts = [[s.cx, s.cy + sh.h], [s.cx, cy], [t.cx, cy], [t.cx, t.cy + th.h]];
        labelAt = [Math.min(s.cx, t.cx) + 14, cy - 6];
      }
      return { flow: f, pts: pts, labelAt: labelAt };
    });

    return { lanes: lanes, pos: pos, edges: edges, width: width, height: height };
  }

  /* ---------------- BPMN render ---------------- */
  function svgNode(pos) {
    var n = pos.node, cx = pos.cx, cy = pos.cy;
    var s = proc(n.process);
    var sev = n.process ? sevOf(n.process) : null;
    var auto = n.process ? autoOf(n.process) : null;
    var cls = "node n-" + n.type + (sev ? " sev-" + sev : "") + (auto ? " auto-" + auto : "") +
      (n.process || n.goto ? " clickable" : "");
    var g = '<g class="' + cls + '" data-node="' + esc(n.id) + '"' +
      (n.process ? ' data-process="' + esc(n.process) + '"' : "") +
      (n.goto ? ' data-goto="' + esc(n.goto) + '"' : "") + ">";
    var title = lbl(n.label) || (s ? s.title : n.id);

    if (n.type === "start" || n.type === "end") {
      g += '<circle class="shape" cx="' + cx + '" cy="' + cy + '" r="20"/>';
      wrapText(title, 20).slice(0, 2).forEach(function (ln, i) {
        g += '<text class="evt-label" x="' + cx + '" y="' + (cy + 34 + i * 13) + '" text-anchor="middle">' + esc(ln) + "</text>";
      });
    } else if (n.type.indexOf("gateway") === 0) {
      var h = 26;
      g += '<path class="shape" d="M' + cx + " " + (cy - h) + " L" + (cx + h) + " " + cy +
        " L" + cx + " " + (cy + h) + " L" + (cx - h) + " " + cy + ' Z"/>';
      if (n.type === "gateway-parallel") {
        g += '<path class="gw-mark" d="M' + (cx - 9) + " " + cy + " H" + (cx + 9) + " M" + cx + " " + (cy - 9) + " V" + (cy + 9) + '"/>';
      } else {
        g += '<path class="gw-mark" d="M' + (cx - 7) + " " + (cy - 7) + " L" + (cx + 7) + " " + (cy + 7) +
          " M" + (cx + 7) + " " + (cy - 7) + " L" + (cx - 7) + " " + (cy + 7) + '"/>';
      }
      if (title) {
        var glines = wrapText(title, 18).slice(0, 2);
        var gy = cy - h - 8 - (glines.length - 1) * 13;
        glines.forEach(function (ln, i) {
          g += '<text class="gw-label" x="' + cx + '" y="' + (gy + i * 13) + '" text-anchor="middle">' + esc(ln) + "</text>";
        });
      }
    } else { // task / subprocess
      var x = cx - NW / 2, yy = cy - NH / 2;
      g += '<rect class="shape" x="' + x + '" y="' + yy + '" width="' + NW + '" height="' + NH + '" rx="9" stroke-width="2"/>';
      if (n.process) {
        g += '<text class="code" x="' + (x + 9) + '" y="' + (yy + 14) + '">' + esc(n.process) + "</text>";
      }
      var lines = wrapText(title, 26).slice(0, 2);
      var ty = cy + (n.process ? 6 : 0) - (lines.length - 1) * 7;
      lines.forEach(function (ln, i) {
        g += '<text class="title" x="' + cx + '" y="' + (ty + i * 15) + '" text-anchor="middle">' + esc(ln) + "</text>";
      });
      if (n.type === "subprocess") {
        var bx = cx - 7, by = yy + NH - 15;
        g += '<rect class="sub-mark" x="' + bx + '" y="' + by + '" width="14" height="14" rx="2"/>' +
          '<path class="gw-mark" style="stroke-width:1.6" d="M' + (bx + 3) + " " + (by + 7) + " H" + (bx + 11) +
          " M" + (bx + 7) + " " + (by + 3) + " V" + (by + 11) + '"/>';
      }
    }
    return g + "</g>";
  }

  function renderDiagram(p, selected) {
    var lay = layoutProcess(p);
    var s = '<svg class="bpmn" viewBox="0 0 ' + lay.width + " " + lay.height + '" width="' + lay.width + '" height="' + lay.height + '">';
    s += '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7.5" markerHeight="7.5" orient="auto-start-reverse">' +
      '<path class="arrowhead" d="M0 0 L10 5 L0 10 z"/></marker></defs>';
    // lanes
    lay.lanes.forEach(function (l, i) {
      s += '<rect class="lane-band lane-band-' + (i % 2) + '" x="' + M + '" y="' + l.y + '" width="' + (lay.width - 2 * M) + '" height="' + l.h + '"/>';
      s += '<text class="lane-label" transform="translate(' + (M + 20) + " " + (l.y + l.h / 2) + ') rotate(-90)" text-anchor="middle">' + esc(lbl(l.label)) + "</text>";
    });
    // edges
    lay.edges.forEach(function (e) {
      var d = e.pts.map(function (pt, i) { return (i ? "L" : "M") + pt[0] + " " + pt[1]; }).join(" ");
      s += '<path class="flow" d="' + d + '" marker-end="url(#arr)"/>';
      var flabel = lbl(e.flow.label);
      if (flabel) {
        var w = flabel.length * 6 + 8;
        s += '<rect class="flow-label-bg" x="' + (e.labelAt[0] - 3) + '" y="' + (e.labelAt[1] - 10) + '" width="' + w + '" height="14" rx="3"/>' +
          '<text class="flow-label" x="' + e.labelAt[0] + '" y="' + (e.labelAt[1] + 1) + '">' + esc(flabel) + "</text>";
      }
    });
    // nodes
    p.nodes.forEach(function (n) {
      var g = svgNode(lay.pos[n.id]);
      if (selected && n.process === selected) g = g.replace('class="node', 'class="node selected');
      s += g;
    });
    return s + "</svg>";
  }

  /* ---------------- views ---------------- */
  function chrome(active) {
    var tabs = [["#/intro", esc(L.intro)]];
    D.departments.forEach(function (d) {
      tabs.push(["#/dept/" + d.number, '<span class="n">' + d.number + "</span>" + esc(d.title)]);
    });
    if (D.coverage.length) tabs.push(["#/processen", esc(L.processes)]);
    if (D.pains.length) tabs.push(["#/pains", esc(L.pains)]);
    var nav = tabs.map(function (t) {
      return '<a href="' + t[0] + '"' + (active === t[0] ? ' class="on"' : "") + ">" + t[1] + "</a>";
    }).join("");
    app.className = "mode-" + mode;
    app.innerHTML =
      '<header class="hdr"><div class="brand">' + esc(D.client.title || "AS-IS review") +
      "<small>" + esc(D.client.name) + (D.client.sector ? " · " + esc(D.client.sector) : "") + "</small></div>" +
      "<nav>" + nav + "</nav>" +
      '<div class="search"><input id="q" type="search" placeholder="' + esc(L.search) + '" autocomplete="off">' +
      '<div class="hits" id="hits"></div></div>' +
      '<div class="mode-toggle" id="modetoggle">' +
      '<button data-mode="pijn"' + (mode === "pijn" ? ' class="on"' : "") + ">" + esc(L.modePijn) + "</button>" +
      '<button data-mode="kansen"' + (mode === "kansen" ? ' class="on"' : "") + ">" + esc(L.modeKansen) + "</button></div>" +
      '<button class="export" id="exportbtn" type="button">⤓ ' + esc(L.exportBtn) + "</button>" +
      "</header>" +
      '<section class="content"><div class="inner" id="view"></div></section>' +
      '<div class="panel-wrap" id="panelwrap"><div class="veil"></div><div class="panel" id="panel"></div></div>' +
      '<div class="exp-wrap" id="expwrap"><div class="veil"></div><div class="exp" id="expdlg"></div></div>';

    var q = document.getElementById("q");
    q.addEventListener("input", onSearch);
    q.addEventListener("focus", onSearch);
    document.addEventListener("click", function (ev) {
      if (!ev.target.closest(".hdr .search")) document.getElementById("hits").classList.remove("open");
    });
    document.getElementById("hits").addEventListener("click", function () {
      document.getElementById("hits").classList.remove("open");
    });
    document.querySelectorAll("#modetoggle button").forEach(function (b) {
      b.addEventListener("click", function () { setMode(b.getAttribute("data-mode")); });
    });
    document.querySelector("#panelwrap .veil").addEventListener("click", closePanel);
    document.getElementById("exportbtn").addEventListener("click", openExport);
    document.querySelector("#expwrap .veil").addEventListener("click", closeExport);
  }

  function setMode(m) {
    if (m === mode) return;
    mode = m;
    app.className = "mode-" + mode;
    document.querySelectorAll("#modetoggle button").forEach(function (b) {
      b.classList.toggle("on", b.getAttribute("data-mode") === mode);
    });
    route(); // re-render current view (legend + card accents follow the mode)
  }

  /* ---------------- PDF export (print-CSS) ---------------- */
  function openExport() {
    var dlg = document.getElementById("expdlg");
    var parts = [
      ["intro", L.intro, !!D.client.intro_html],
      ["processen", L.processes, !!D.coverage.length],
      ["pains", L.pains, !!D.pains.length]
    ];
    dlg.innerHTML =
      "<h2>" + esc(L.exportTitle) + '</h2><p class="hint">' + esc(L.exportHint) + "</p>" +
      "<h3>" + esc(L.exportDepts) + ' — <button type="button" class="all" id="exptoggle">' + esc(L.exportAllNone) + "</button></h3>" +
      '<div class="depts">' + D.departments.map(function (d) {
        return '<label><input type="checkbox" class="expdept" value="' + d.number + '" checked>' +
          '<span class="n">' + d.number + "</span><span>" + esc(d.title) + "</span></label>";
      }).join("") + "</div>" +
      "<h3>" + esc(L.exportParts) + "</h3>" +
      parts.map(function (p) {
        return '<label><input type="checkbox" class="exppart" value="' + p[0] + '"' + (p[2] ? " checked" : " disabled") + ">" +
          "<span>" + esc(p[1]) + "</span></label>";
      }).join("") +
      '<div class="row"><span class="sp"></span>' +
      '<button type="button" class="cancel" id="expcancel">' + esc(L.exportCancel) + "</button>" +
      '<button type="button" class="go" id="expgo">' + esc(L.exportGo) + "</button></div>";
    dlg.querySelector("#expcancel").addEventListener("click", closeExport);
    dlg.querySelector("#exptoggle").addEventListener("click", function () {
      var boxes = dlg.querySelectorAll(".expdept");
      var any = Array.prototype.some.call(boxes, function (b) { return b.checked; });
      boxes.forEach(function (b) { b.checked = !any; });
    });
    dlg.querySelector("#expgo").addEventListener("click", function () {
      var depts = [];
      dlg.querySelectorAll(".expdept:checked").forEach(function (b) { depts.push(+b.value); });
      var opts = {};
      dlg.querySelectorAll(".exppart:checked").forEach(function (b) { opts[b.value] = true; });
      if (!depts.length && !Object.keys(opts).length) return;
      closeExport();
      buildPrintDoc(depts, opts);
      document.body.classList.add("printing");
      // let the print DOM paint before the dialog opens
      setTimeout(function () { window.print(); }, 60);
    });
    document.getElementById("expwrap").classList.add("open");
  }

  function closeExport() {
    document.getElementById("expwrap").classList.remove("open");
  }

  window.addEventListener("afterprint", function () {
    document.body.classList.remove("printing");
    document.getElementById("printdoc").innerHTML = "";
  });

  // Print legend: always the severity (Pijn) palette — the printed diagrams
  // are colored by severity regardless of the on-screen mode.
  function printLegend() {
    function item(color, bg, label, dashed) {
      return '<span><i style="border-color:var(' + color + ');background:var(' + bg + ')' +
        (dashed ? ";border-style:dashed" : "") + '"></i>' + esc(label) + "</span>";
    }
    return '<div class="pv-legend">' +
      item("--sev-none", "--sev-none-bg", L.sev.none) +
      item("--sev-minor", "--sev-minor-bg", L.sev.minor) +
      item("--sev-major", "--sev-major-bg", L.sev.major) +
      item("--sev-critical", "--sev-critical-bg", L.sev.critical) +
      item("--sev-undoc", "--sev-undoc-bg", L.sev.undoc, true) + "</div>";
  }

  function printPain(uid) {
    var p = painByUid[uid];
    if (!p) return "";
    return '<div class="pv-pain sev-' + esc(p.severity || "major") + '">' +
      '<h4><code>' + esc(p.id) + "</code> " + esc(p.title) + "</h4>" +
      (p.quote ? "<blockquote>“" + esc(p.quote) + "”</blockquote>" : "") +
      (p.source ? '<div class="src">' + esc(p.source) + "</div>" : "") +
      '<div class="chips">' +
      (p.type ? '<span class="chip plain">' + esc(L.ptype[p.type] || p.type) + "</span> " : "") +
      (p.severity ? sevChip(p.severity) + " " : "") +
      (p.volume ? '<span class="chip plain">' + esc(L.volumeLbl) + ": " + esc(p.volume) + "</span>" : "") +
      "</div></div>";
  }

  function printProc(code) {
    var s = proc(code);
    if (!s) return "";
    var chips = sevChip(sevOf(code)) + (s.automability ? " " + autoChip(s.automability) : "");
    var fields = "";
    ["werkwijze", "wie", "systemen", "volume"].forEach(function (k) {
      if (s.fields && s.fields[k]) {
        fields += "<dt>" + esc(L.fields[k]) + "</dt><dd>" + esc(s.fields[k]) + "</dd>";
      }
    });
    return '<div class="pv-proc"><div class="codes"><code>' + esc(code) + "</code></div>" +
      "<h3>" + esc(s.title) + '</h3><div class="chips">' + chips + "</div>" +
      (fields ? '<dl class="pv-fields">' + fields + "</dl>" : "") +
      (s.html ? '<div class="md">' + s.html + "</div>" : "") +
      ((s.pains || []).length
        ? '<div class="pv-painshdr">' + esc(L.linkedPains) + "</div>" + s.pains.map(printPain).join("") : "") +
      "</div>";
  }

  function buildPrintDoc(deptNums, opts) {
    var sel = {};
    deptNums.forEach(function (n) { sel[n] = true; });
    var depts = D.departments.filter(function (d) { return sel[d.number]; });
    var h = "";

    // cover — vendor-neutral: accent-tinted artwork, no third-party assets
    h += '<div class="pv-cover"><div class="mark"></div>' +
      '<div class="title"><h1>' + esc(D.client.title || "AS-IS review") + "</h1>" +
      '<p class="sub">' + esc(D.client.name) + (D.client.sector ? " · " + esc(D.client.sector) : "") + "</p></div>" +
      '<div class="meta">' +
      "<div><b>" + esc(L.coverClient) + ":</b> " + esc(D.client.name) + "</div>" +
      (D.client.sector ? "<div><b>" + esc(L.coverSector) + ":</b> " + esc(D.client.sector) + "</div>" : "") +
      (D.meta && D.meta.version ? "<div><b>" + esc(L.coverVersion) + ":</b> " + esc(D.meta.version) + "</div>" : "") +
      "<div><b>" + esc(L.coverDate) + ":</b> " + esc((D.meta && D.meta.generated) || "") + "</div>" +
      (D.meta && D.meta.catalog ? "<div><b>" + esc(L.coverCatalog) + ":</b> " + esc(D.meta.catalog) + "</div>" : "") +
      "</div>" +
      '<div class="art"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div></div>';

    // everything after the cover lives in a table whose <thead> the browser
    // repeats at the top of every printed page — the running header
    h += '<table class="pv-doc"><thead><tr><td><div class="pv-run"><span>' +
      esc(D.client.title || "AS-IS review") + " — " + esc(D.client.name) +
      (D.meta && D.meta.version ? " · v" + esc(D.meta.version) : "") +
      '</span><span class="r">' + esc((D.meta && D.meta.generated) || "") +
      '</span></div></td></tr></thead><tbody><tr><td>';

    // table of contents
    var toc = [];
    if (opts.intro) toc.push(["", L.intro]);
    depts.forEach(function (d) { toc.push([d.number + ".", d.title]); });
    if (opts.processen) toc.push(["", L.processes]);
    if (opts.pains) toc.push(["", L.pains]);
    h += '<div class="pv-toc"><h2>' + esc(L.toc) + "</h2><ol>" + toc.map(function (t) {
      return '<li><span class="n">' + esc(t[0]) + "</span><span>" + esc(t[1]) + "</span></li>";
    }).join("") + "</ol></div>";

    if (opts.intro && D.client.intro_html) {
      h += '<div class="pv-section"><h1>' + esc(L.intro) + '</h1><div class="md">' + D.client.intro_html + "</div></div>";
    }

    // departments: intro + flow + full AS-IS process documentation
    depts.forEach(function (d) {
      h += '<div class="pv-section"><h1><span class="n">' + d.number + ".</span> " + esc(d.title) + "</h1>";
      if (d.intro_html) h += '<div class="pv-intro md">' + d.intro_html + "</div>";
      if (d.process) {
        h += '<div class="pv-diagram">' + renderDiagram(d.process, null) + printLegend() + "</div>";
      }
      h += d.processes.map(printProc).join("");
      h += "</div>";
    });

    // coverage matrix (rows limited to the selected departments)
    if (opts.processen) {
      var rows = D.coverage.filter(function (c) { return sel[c.department]; });
      h += '<div class="pv-section"><h1>' + esc(L.processes) + '</h1><table class="pv-table"><thead><tr>' +
        L.scopeCols.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>" +
        rows.map(function (c) {
          var s = proc(c.code);
          var d = deptByNum[c.department];
          return "<tr><td><code>" + esc(c.code) + "</code></td><td>" + esc(c.title) + "</td>" +
            "<td>" + (d ? d.number + ". " + esc(d.title) : esc(c.department)) + "</td>" +
            "<td>" + (c.scope ? esc(L.inScope) : esc(L.outScope)) + "</td>" +
            "<td>" + (c.scope ? sevChip(s ? sevOf(c.code) : "undoc") : "—") + "</td>" +
            "<td>" + esc(c.note || "") + "</td></tr>";
        }).join("") + "</tbody></table></div>";
    }

    // pains register (entries in the selected departments, plus entries
    // without a department — nothing silently dropped)
    if (opts.pains) {
      h += '<div class="pv-section"><h1>' + esc(L.pains) + "</h1>" +
        D.pains.filter(function (p) { return !p.department || sel[p.department]; }).map(function (p) {
          var d = deptByNum[p.department];
          return '<div class="pv-proc"><div class="codes"><code>' + esc(p.id) + "</code>" +
            (d ? " · " + d.number + ". " + esc(d.title) : "") + "</div>" +
            "<h3>" + esc(p.title) + "</h3>" +
            (p.quote ? "<blockquote>“" + esc(p.quote) + "”</blockquote>" : "") +
            (p.source ? '<div class="src">' + esc(p.source) + "</div>" : "") +
            (p.html ? '<div class="md">' + p.html + "</div>" : "") +
            '<div class="chips">' +
            (p.type ? '<span class="chip plain">' + esc(L.ptype[p.type] || p.type) + "</span> " : "") +
            (p.severity ? sevChip(p.severity) + " " : "") +
            (p.volume ? '<span class="chip plain">' + esc(L.volumeLbl) + ": " + esc(p.volume) + "</span> " : "") +
            (p.value ? '<span class="chip plain">' + esc(L.valueLbl) + ": " + esc(p.value) + "</span>" : "") +
            "</div>" +
            (p.processes && p.processes.length ? '<div class="codes">' + p.processes.map(function (c) {
              return "<code>" + esc(c) + "</code>";
            }).join(" ") + "</div>" : "") +
            "</div>";
        }).join("") + "</div>";
    }

    h += "</td></tr></tbody></table>";
    document.getElementById("printdoc").innerHTML = h;
  }

  function onSearch(ev) {
    var q = ev.target.value.trim().toLowerCase();
    var hits = document.getElementById("hits");
    if (q.length < 2) { hits.classList.remove("open"); return; }
    var res = [];
    Object.keys(D.processes).forEach(function (code) {
      var s = D.processes[code];
      if (code.toLowerCase().indexOf(q) >= 0 || (s.title || "").toLowerCase().indexOf(q) >= 0) {
        res.push('<a class="hit" href="#/dept/' + s.department + "/doc/" + esc(code) + '"><code>' + esc(code) + "</code> " + esc(s.title) + "</a>");
      }
    });
    D.pains.forEach(function (p) {
      var hay = (p.id + " " + (p.title || "") + " " + (p.quote || "")).toLowerCase();
      if (hay.indexOf(q) >= 0) {
        res.push('<a class="hit" href="#/pains/' + esc(p.uid) + '"><code>' + esc(p.id) + "</code> " + esc(p.title) + "</a>");
      }
    });
    res = res.slice(0, 40);
    hits.innerHTML = res.length ? res.join("") : '<div class="none">' + esc(L.noResults) + "</div>";
    hits.classList.add("open");
  }

  function legend() {
    function item(color, bg, label, dashed) {
      return '<span><i style="border-color:var(' + color + ');background:var(' + bg + ')' +
        (dashed ? ";border-style:dashed" : "") + '"></i>' + esc(label) + "</span>";
    }
    var h = '<div class="legend">';
    if (mode === "kansen") {
      h += item("--auto-human", "--auto-human-bg", L.auto.human) +
        item("--auto-automation", "--auto-automation-bg", L.auto.automation) +
        item("--auto-agent", "--auto-agent-bg", L.auto.agent) +
        item("--auto-hybrid", "--auto-hybrid-bg", L.auto.hybrid) +
        item("--auto-neutral", "--auto-neutral-bg", L.auto.neutral) +
        item("--sev-undoc", "--sev-undoc-bg", L.sev.undoc, true);
    } else {
      h += item("--sev-none", "--sev-none-bg", L.sev.none) +
        item("--sev-minor", "--sev-minor-bg", L.sev.minor) +
        item("--sev-major", "--sev-major-bg", L.sev.major) +
        item("--sev-critical", "--sev-critical-bg", L.sev.critical) +
        item("--sev-undoc", "--sev-undoc-bg", L.sev.undoc, true);
    }
    return h + "</div>";
  }

  function procCard(code) {
    var s = proc(code);
    if (!s) return "";
    var sev = sevOf(code), auto = autoOf(code);
    return '<div class="proc-card sev-' + sev + (auto ? " auto-" + auto : "") + '" data-process="' + esc(code) + '">' +
      '<div class="m"><code class="bs">' + esc(code) + "</code></div>" +
      '<div class="t">' + esc(s.title) + "</div>" +
      '<div class="m">' + sevChip(sev) + (s.automability ? " " + autoChip(s.automability) : "") +
      (s.pains || []).map(function (u) {
        var p = painByUid[u];
        return p ? ' <span class="chip pain">' + esc(p.id) + "</span>" : "";
      }).join("") + "</div></div>";
  }

  function markDept(num) {
    document.querySelectorAll(".hdr nav a").forEach(function (a) {
      a.classList.toggle("on", a.getAttribute("href") === (num == null ? " " : "#/dept/" + num));
    });
  }

  function viewDept(num, docCode) {
    var d = deptByNum[num];
    if (!d) return viewIntro();
    markDept(num);
    var v = document.getElementById("view");
    var h = '<h1 class="pg">' + d.number + ". " + esc(d.title) + "</h1>";
    var sub = [];
    if (d.process) sub.push(esc(lbl(d.process.subtitle)));
    if (d.status) sub.push(esc(L.statusLbl) + ": " + esc(d.status));
    if (sub.length) h += '<p class="pg-sub">' + sub.filter(Boolean).join(" · ") + "</p>";
    if (d.intro_html) h += '<div class="card md">' + d.intro_html + "</div>";
    if (d.process) {
      h += '<div class="card diagram-card"><div class="diagram-head">' + legend() +
        '<div class="zoom"><button data-z="-">−</button><button data-z="0">⤢</button><button data-z="+">+</button></div></div>' +
        '<div class="diagram-scroll" id="dscroll">' + renderDiagram(d.process, docCode) + "</div></div>";
    } else if (d.processes.length) {
      h += '<p class="pg-sub">' + esc(L.deptDocOnly) + "</p>";
    }
    if (d.processes.length) {
      h += '<h2 class="sect">' + esc(L.allProcesses) + " (" + d.processes.length + ')</h2><div class="proc-grid">' +
        d.processes.map(procCard).join("") + "</div>";
    }
    if (!d.process && !d.processes.length) h += '<div class="empty">—</div>';
    v.innerHTML = h;

    var zoom = 1, svg = v.querySelector("svg.bpmn");
    var baseW = svg ? +svg.getAttribute("width") : 0;
    v.querySelectorAll(".zoom button").forEach(function (b) {
      b.addEventListener("click", function () {
        var z = b.getAttribute("data-z");
        zoom = z === "+" ? Math.min(zoom * 1.2, 3) : z === "-" ? Math.max(zoom / 1.2, .4) : 1;
        if (svg) { svg.setAttribute("width", baseW * zoom); svg.removeAttribute("height"); }
      });
    });
    v.querySelectorAll("[data-process]").forEach(function (n) {
      n.addEventListener("click", function () {
        location.hash = "#/dept/" + num + "/doc/" + n.getAttribute("data-process");
      });
    });
    v.querySelectorAll("svg [data-goto]:not([data-process])").forEach(function (n) {
      n.addEventListener("click", function () {
        var target = findFlowDept(n.getAttribute("data-goto"));
        if (target != null) location.hash = "#/dept/" + target;
      });
    });
    if (docCode) openPanel(docCode, num); else closePanel();
  }

  function findFlowDept(pid) {
    for (var i = 0; i < D.departments.length; i++) {
      if (D.departments[i].process && D.departments[i].process.id === pid) return D.departments[i].number;
    }
    return null;
  }

  function painInline(uid) {
    var p = painByUid[uid];
    if (!p) return "";
    return '<div class="pain-inline sev-' + esc(p.severity || "major") + '">' +
      "<h4><code class=\"bs\">" + esc(p.id) + "</code> " + esc(p.title) +
      ' <span class="chip ref link" data-nav="#/pains/' + esc(p.uid) + '">↗ ' + esc(L.register) + "</span></h4>" +
      (p.quote ? "<blockquote>“" + esc(p.quote) + "”</blockquote>" : "") +
      (p.source ? '<div class="src">' + esc(p.source) + "</div>" : "") +
      "<div>" +
      (p.type ? '<span class="chip plain">' + esc(L.ptype[p.type] || p.type) + "</span> " : "") +
      (p.severity ? sevChip(p.severity) + " " : "") +
      (p.volume ? '<span class="chip plain">' + esc(p.volume) + "</span>" : "") +
      "</div></div>";
  }

  function openPanel(code, deptNum) {
    var s = proc(code);
    var wrap = document.getElementById("panelwrap"), panel = document.getElementById("panel");
    if (!s) { closePanel(); return; }
    var d = deptByNum[s.department];
    var chips = sevChip(sevOf(code)) + (s.automability ? " " + autoChip(s.automability) : "");
    (s.pains || []).forEach(function (u) {
      var p = painByUid[u];
      if (p) chips += ' <span class="chip pain" data-nav="#/pains/' + esc(p.uid) + '">' + esc(p.id) + "</span>";
    });
    var goto_ = null;
    if (d && d.process) {
      d.process.nodes.some(function (n) { if (n.process === code && n.goto) { goto_ = n.goto; return true; } return false; });
    }
    var fields = "";
    ["werkwijze", "wie", "systemen", "volume"].forEach(function (k) {
      if (s.fields && s.fields[k]) {
        fields += "<dt>" + esc(L.fields[k]) + "</dt><dd>" + esc(s.fields[k]) + "</dd>";
      }
    });
    panel.innerHTML =
      '<div class="p-head"><button class="p-close" title="✕">✕</button>' +
      '<div class="codes"><code class="bs">' + esc(code) + "</code></div>" +
      "<h2>" + esc(s.title) + "</h2>" +
      '<div class="dom">' + (d ? d.number + ". " + esc(d.title) : "") + "</div></div>" +
      '<div class="p-body"><div class="p-meta">' + chips + "</div>" +
      (goto_ != null && findFlowDept(goto_) != null
        ? '<p><span class="chip ref" data-nav="#/dept/' + findFlowDept(goto_) + '">↗ ' + esc(L.gotoProcess) + "</span></p>" : "") +
      (fields ? '<dl class="p-fields">' + fields + "</dl>" : "") +
      '<div class="md">' + (s.html || (fields ? "" : "<p><em>—</em></p>")) + "</div>" +
      ((s.pains || []).length
        ? '<h3 class="sect">' + esc(L.linkedPains) + "</h3>" + s.pains.map(painInline).join("") : "") +
      "</div>";
    panel.querySelector(".p-close").addEventListener("click", closePanel);
    panel.querySelectorAll("[data-nav]").forEach(function (c) {
      c.addEventListener("click", function () { location.hash = c.getAttribute("data-nav"); });
    });
    panel.querySelector(".p-body").scrollTop = 0;
    wrap.classList.add("open");
  }

  function closePanel() {
    var w = document.getElementById("panelwrap");
    if (w) w.classList.remove("open");
    var m = location.hash.match(/^#\/dept\/(\d+)\/doc\//);
    if (m) history.replaceState(null, "", "#/dept/" + m[1]);
  }

  function viewIntro() {
    markDept(null);
    var v = document.getElementById("view");
    v.innerHTML = '<h1 class="pg">' + esc(L.intro) + "</h1>" +
      '<p class="pg-sub">' + esc(D.client.name) +
      (D.client.sector ? " · " + esc(D.client.sector) : "") +
      (D.meta && D.meta.version ? " · v" + esc(D.meta.version) : "") +
      (D.meta && D.meta.generated ? " · " + esc(L.generated) + " " + esc(D.meta.generated) : "") + "</p>" +
      '<div class="card md">' + (D.client.intro_html || "") + "</div>";
  }

  function viewScope() {
    markDept(null);
    var v = document.getElementById("view");
    var filters = ["all", "none", "minor", "major", "critical", "undoc", "out"];
    var flabel = { all: L.filterAll, none: L.sev.none, minor: L.sev.minor, major: L.sev.major,
                   critical: L.sev.critical, undoc: L.sev.undoc, out: L.outScope };
    var h = '<h1 class="pg">' + esc(L.processes) + '</h1><p class="pg-sub">' +
      D.coverage.filter(function (c) { return c.scope; }).length + " " + esc(L.inScope) + " · " +
      D.coverage.filter(function (c) { return !c.scope; }).length + " " + esc(L.outScope) + "</p>" +
      '<div class="filters">' + filters.map(function (f) {
        return '<button data-f="' + f + '"' + (f === "all" ? ' class="on"' : "") + ">" + esc(flabel[f]) + "</button>";
      }).join("") + "</div>" +
      '<table class="reg"><thead><tr>' + L.scopeCols.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>" +
      D.coverage.map(function (c) {
        var s = proc(c.code);
        var sev = c.scope ? (s ? sevOf(c.code) : "undoc") : "out";
        var d = deptByNum[c.department];
        return '<tr class="' + (s ? "click " : "") + (c.scope ? "" : "dim") + '" data-f="' + sev + '"' +
          (s ? ' data-process="' + esc(c.code) + '" data-dept="' + c.department + '"' : "") + ">" +
          '<td><code class="bs">' + esc(c.code) + "</code></td><td>" + esc(c.title) + "</td>" +
          "<td>" + (d ? d.number + ". " + esc(d.title) : esc(c.department)) + "</td>" +
          "<td>" + (c.scope ? esc(L.inScope) : esc(L.outScope)) + "</td>" +
          "<td>" + (c.scope ? sevChip(s ? sevOf(c.code) : "undoc") : "—") + "</td>" +
          "<td>" + esc(c.note || "") + "</td></tr>";
      }).join("") + "</tbody></table>";
    v.innerHTML = h;
    v.querySelectorAll(".filters button").forEach(function (b) {
      b.addEventListener("click", function () {
        v.querySelectorAll(".filters button").forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        var f = b.getAttribute("data-f");
        v.querySelectorAll("tbody tr").forEach(function (tr) {
          tr.style.display = f === "all" || tr.getAttribute("data-f") === f ? "" : "none";
        });
      });
    });
    v.querySelectorAll("tr.click").forEach(function (tr) {
      tr.addEventListener("click", function () {
        location.hash = "#/dept/" + tr.getAttribute("data-dept") + "/doc/" + tr.getAttribute("data-process");
      });
    });
  }

  function linkedProcChips(codes) {
    return (codes || []).map(function (c) {
      var s = proc(c);
      return s ? '<span class="chip ref link" data-nav="#/dept/' + s.department + "/doc/" + esc(c) + '">' + esc(c) + "</span>"
               : '<span class="chip plain">' + esc(c) + "</span>";
    }).join(" ");
  }

  function viewPains(highlightUid) {
    markDept(null);
    var v = document.getElementById("view");
    var types = [];
    D.pains.forEach(function (p) { if (p.type && types.indexOf(p.type) < 0) types.push(p.type); });
    var sevs = ["all", "minor", "major", "critical"];
    var h = '<h1 class="pg">' + esc(L.pains) + '</h1><p class="pg-sub">' + D.pains.length + "</p>" +
      '<div class="filters" id="pf-sev"><span class="flabel">' + esc(L.severityHdr) + "</span>" +
      sevs.map(function (f) {
        return '<button data-f="' + f + '"' + (f === "all" ? ' class="on"' : "") + ">" +
          esc(f === "all" ? L.filterAll : L.sev[f]) + "</button>";
      }).join("") + "</div>" +
      '<div class="filters" id="pf-type"><span class="flabel">' + esc(L.typeHdr) + "</span>" +
      ['<button data-f="all" class="on">' + esc(L.filterAll) + "</button>"].concat(types.map(function (t) {
        return '<button data-f="' + esc(t) + '">' + esc(L.ptype[t] || t) + "</button>";
      })).join("") +
      '<input id="pq" type="search" placeholder="' + esc(L.search) + '">' + "</div>" +
      (D.pains.length ? D.pains.map(function (p) {
        var d = deptByNum[p.department];
        var text = (p.id + " " + (p.title || "") + " " + (p.quote || "") + " " + (p.value || "")).toLowerCase();
        return '<div class="card pain-card sev-' + esc(p.severity || "major") + '" id="pain-' + esc(p.uid) +
          '" data-sev="' + esc(p.severity || "") + '" data-type="' + esc(p.type || "") +
          '" data-text="' + esc(text) + '">' +
          '<h3><code class="bs">' + esc(p.id) + "</code> " + esc(p.title) +
          (d ? ' <span class="dept">· ' + d.number + ". " + esc(d.title) + "</span>" : "") + "</h3>" +
          (p.quote ? "<blockquote>“" + esc(p.quote) + "”</blockquote>" : "") +
          (p.source ? '<div class="src">' + esc(p.source) + "</div>" : "") +
          (p.html ? '<div class="md">' + p.html + "</div>" : "") +
          '<div class="meta-row">' +
          (p.type ? '<span class="chip plain">' + esc(L.ptype[p.type] || p.type) + "</span>" : "") +
          (p.severity ? sevChip(p.severity) : "") +
          (p.volume ? "<span>" + esc(L.volumeLbl) + ": " + esc(p.volume) + "</span>" : "") +
          (p.value ? "<span>" + esc(L.valueLbl) + ": " + esc(p.value) + "</span>" : "") +
          "</div>" +
          (p.processes && p.processes.length ? '<div class="meta-row">' + linkedProcChips(p.processes) + "</div>" : "") +
          "</div>";
      }).join("") : '<div class="empty">—</div>');
    v.innerHTML = h;

    var fSev = "all", fType = "all", fText = "";
    function apply() {
      v.querySelectorAll(".pain-card").forEach(function (c) {
        var ok = (fSev === "all" || c.getAttribute("data-sev") === fSev) &&
                 (fType === "all" || c.getAttribute("data-type") === fType) &&
                 (!fText || c.getAttribute("data-text").indexOf(fText) >= 0);
        c.style.display = ok ? "" : "none";
      });
    }
    ["pf-sev", "pf-type"].forEach(function (id) {
      var box = document.getElementById(id);
      if (!box) return;
      box.querySelectorAll("button").forEach(function (b) {
        b.addEventListener("click", function () {
          box.querySelectorAll("button").forEach(function (x) { x.classList.remove("on"); });
          b.classList.add("on");
          if (id === "pf-sev") fSev = b.getAttribute("data-f"); else fType = b.getAttribute("data-f");
          apply();
        });
      });
    });
    var pq = document.getElementById("pq");
    if (pq) pq.addEventListener("input", function () { fText = pq.value.trim().toLowerCase(); apply(); });
    bindNav(v);
    if (highlightUid) {
      var card = document.getElementById("pain-" + highlightUid);
      if (card) {
        card.classList.add("hl");
        card.scrollIntoView({ block: "center" });
      }
    }
  }

  function bindNav(root) {
    root.querySelectorAll("[data-nav]").forEach(function (c) {
      c.addEventListener("click", function () { location.hash = c.getAttribute("data-nav"); });
    });
  }

  /* ---------------- router ---------------- */
  function route() {
    var h = location.hash || "";
    var m;
    if ((m = h.match(/^#\/dept\/(\d+)(?:\/doc\/([A-Za-z0-9.\-]+))?/))) {
      chromeOnce(null);
      viewDept(+m[1], m[2] || null);
      return;
    }
    closePanel();
    if ((m = h.match(/^#\/pains(?:\/([A-Za-z0-9.\-]+))?$/))) {
      chromeOnce("#/pains"); viewPains(m[1] || null); return;
    }
    if (h === "#/processen") { chromeOnce("#/processen"); viewScope(); return; }
    chromeOnce("#/intro"); viewIntro();
  }

  var chromed = null;
  function chromeOnce(active) {
    // rebuild header nav highlight cheaply; full chrome only once
    if (!chromed) { chrome(active); chromed = true; }
    document.querySelectorAll(".hdr nav a").forEach(function (a) {
      a.classList.toggle("on", a.getAttribute("href") === active);
    });
  }

  window.addEventListener("hashchange", route);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closePanel(); });
  route();
})();
