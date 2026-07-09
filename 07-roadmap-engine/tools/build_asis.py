#!/usr/bin/env python3
"""Compile a client's AS-IS review into one interactive HTML file.

Usage:
    python3 07-roadmap-engine/tools/build_asis.py 03-clients/<client-slug> [-o output.html]

Reads (under 03-clients/<slug>/):
    engagement-config.json          client name, language, accent colour, departments in scope
    asis/intro.md                   the "Inleiding" chapter (optional, client-specific)
    departments/NN-<dept>/pains.md              ## PAIN-x blocks
    departments/NN-<dept>/content/NN-<dept>.md  ## <CODE> AS-IS blocks + status header table
    departments/NN-<dept>/coverage.md           scope matrix: | Code | Proces | Scope | Reden |
    departments/NN-<dept>/flows/*.process.json  client flows; override standard by `domain`

Plus the shared assets (under 07-roadmap-engine/):
    catalog/departments.json    department & process catalog (controlled vocabulary)
    flows/*.process.json        standard AS-IS flows (fallback per department)
    viewer/{template.html,viewer.css,viewer.js}

Writes:
    03-clients/<slug>/asis/output/ASIS-<slug>.html  (self-contained, offline, shareable)

Python stdlib only — no dependencies.
"""

from __future__ import annotations

import argparse
import datetime
import html
import json
import re
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent  # 07-roadmap-engine/
CATALOG_PATH = ENGINE / "catalog" / "departments.json"
STD_FLOWS = ENGINE / "flows"
VIEWER = ENGINE / "viewer"

CODE_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,4}\.\d{3}\b")
PAIN_RE = re.compile(r"\bPAIN-\d+\b")

SEVERITIES = ("none", "minor", "major", "critical")
PAIN_SEVERITIES = ("minor", "major", "critical")
AUTOMABILITIES = ("human", "automation", "agent", "hybrid")
PAIN_TYPES = ("retype", "chase", "wait", "error", "skill-bottleneck", "no-visibility")
STATUSES = ("draft", "consultant-review", "client-review", "approved")

WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"  ! {msg}", file=sys.stderr)


def loc(v, lang: str) -> str:
    """Resolve a {nl,en} label object (or plain string) to one language."""
    if isinstance(v, dict):
        return v.get(lang) or v.get("nl") or v.get("en") or ""
    return v or ""


# --------------------------------------------------------------------------- markdown
INLINE_RULES = [
    (re.compile(r"`([^`]+)`"), lambda m: f"<code>{html.escape(m.group(1))}</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), r"<em>\1</em>"),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)"), r'<a href="\2" target="_blank" rel="noopener">\1</a>'),
]


def md_inline(text: str) -> str:
    out = html.escape(text, quote=False)
    for rule, repl in INLINE_RULES:
        out = rule.sub(repl, out)
    return out


def md_to_html(md: str) -> str:
    """Small CommonMark-ish renderer: headings, lists (2 levels), tables,
    blockquotes, hr, paragraphs, inline bold/italic/code/links."""
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    para: list[str] = []
    lists: list[str] = []  # stack of open list tags
    in_quote = False

    def flush_para() -> None:
        if para:
            out.append("<p>" + md_inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists(depth: int = 0) -> None:
        while len(lists) > depth:
            out.append(f"</{lists.pop()}>")

    def close_quote() -> None:
        nonlocal in_quote
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # table block
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]) and "-" in lines[i + 1]:
            flush_para(); close_lists(); close_quote()
            header = [md_inline(c.strip()) for c in stripped.strip("|").split("|")]
            out.append("<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in header) + "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [md_inline(c.strip()) for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</tbody></table>")
            continue

        m_h = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        m_ul = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        m_ol = re.match(r"^(\s*)\d+[.)]\s+(.*)$", line)

        if not stripped:
            flush_para(); close_lists(); close_quote()
        elif m_h:
            flush_para(); close_lists(); close_quote()
            level = len(m_h.group(1))
            out.append(f"<h{level}>{md_inline(m_h.group(2))}</h{level}>")
        elif re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush_para(); close_lists(); close_quote()
            out.append("<hr>")
        elif stripped.startswith(">"):
            flush_para(); close_lists()
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append("<p>" + md_inline(stripped.lstrip("> ").strip()) + "</p>")
        elif m_ul or m_ol:
            flush_para(); close_quote()
            indent, item = (m_ul or m_ol).group(1), (m_ul or m_ol).group(2)
            depth = 2 if len(indent) >= 2 else 1
            tag = "ul" if m_ul else "ol"
            while len(lists) > depth:
                out.append(f"</{lists.pop()}>")
            while len(lists) < depth:
                lists.append(tag)
                out.append(f"<{tag}>")
            out.append(f"<li>{md_inline(item)}</li>")
        else:
            if in_quote:
                out.append("<p>" + md_inline(stripped) + "</p>")
            elif lists and out and out[-1].endswith("</li>"):
                # continuation line of a wrapped list item
                out[-1] = out[-1][: -len("</li>")] + " " + md_inline(stripped) + "</li>"
            else:
                close_lists()
                para.append(stripped)
        i += 1

    flush_para(); close_lists(); close_quote()
    return "\n".join(out)


# --------------------------------------------------------------------------- parsing
META_LINE = re.compile(r"^\s*[-*]\s+\*\*([^:*]+):?\*\*:?\s*(.*)$")


def split_blocks(md: str, heading_re: re.Pattern) -> tuple[str, list[dict]]:
    """Split a markdown file into (preamble, [{key, title, meta{}, body}]) on ## headings
    matching heading_re. Metadata bullets (- **Field:** value) directly under a heading
    are lifted out of the body."""
    lines = md.replace("\r\n", "\n").split("\n")
    preamble: list[str] = []
    blocks: list[dict] = []
    cur: dict | None = None
    meta_zone = False
    for line in lines:
        m = re.match(r"^##\s+(.*)$", line.strip())
        hm = heading_re.match(m.group(1).strip()) if m else None
        if hm:
            cur = {"key": hm.group(1), "title": (hm.group(2) or "").strip(" -–—:"), "meta": {}, "body": []}
            blocks.append(cur)
            meta_zone = True
            continue
        if cur is None:
            preamble.append(line)
            continue
        if meta_zone:
            mm = META_LINE.match(line)
            if mm:
                cur["meta"][mm.group(1).strip().lower().rstrip(":")] = mm.group(2).strip()
                continue
            if line.strip():
                meta_zone = False
        cur["body"].append(line)
    for b in blocks:
        b["body"] = "\n".join(b["body"]).strip()
    return "\n".join(preamble).strip(), blocks


def parse_status_header(preamble: str, where: str) -> str | None:
    """Find the status header table (| Client | Afdeling | Status | Laatst gereviewd |)
    in the content-file preamble; return the status value, warning on problems."""
    lines = preamble.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip().lower() for c in s.strip("|").split("|")]
        if "status" not in cells:
            continue
        col = cells.index("status")
        # skip the separator row, take the first data row
        j = i + 1
        while j < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[j]):
            j += 1
        if j >= len(lines) or not lines[j].strip().startswith("|"):
            warn(f"{where}: status-headertabel zonder datarij")
            return None
        data = [c.strip() for c in lines[j].strip().strip("|").split("|")]
        status = data[col] if col < len(data) else ""
        if status not in STATUSES:
            warn(f"{where}: ongeldige status '{status}' (verwacht: {' | '.join(STATUSES)})")
            return None
        return status
    warn(f"{where}: status-headertabel ontbreekt (| Client | Afdeling | Status | Laatst gereviewd |)")
    return None


def strip_status_header(preamble: str) -> str:
    """Remove the status header table from the preamble so it doesn't render as intro."""
    out, skipping = [], False
    for line in preamble.splitlines():
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip().lower() for c in s.strip("|").split("|")]
            if "status" in cells and "client" in cells:
                skipping = True
                continue
            if skipping:
                continue
        skipping = False
        out.append(line)
    return "\n".join(out).strip()


def parse_coverage(md: str, dept_num: int, where: str) -> list[dict]:
    """Parse the scope matrix table. Expected columns: | Code | Proces | Scope | Reden |"""
    rows = []
    for line in md.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 3 or not CODE_RE.match(cells[0]):
            continue
        scope_raw = cells[2].lower() if len(cells) > 2 else ""
        in_scope = (any(t in scope_raw for t in ("in", "ja", "yes", "x", "✓"))
                    and not any(t in scope_raw for t in ("uit", "nee", "niet", "out", "no")))
        rows.append({
            "code": cells[0],
            "title": cells[1] if len(cells) > 1 else "",
            "department": dept_num,
            "scope": in_scope,
            "severity": None,
            "note": cells[3] if len(cells) > 3 else "",
        })
    if not rows:
        warn(f"{where}: geen scope-rijen gevonden (verwacht | Code | Proces | Scope | Reden |)")
    return rows


# --------------------------------------------------------------------------- build
def load_flows(dept_dirs: dict[int, Path]) -> dict[int, dict]:
    """Client flows win; standard flows (07-roadmap-engine/flows/) are the fallback.
    Keyed by `domain` (= catalog department number)."""
    flows: dict[int, dict] = {}
    sources: list[Path] = []
    if STD_FLOWS.is_dir():
        sources.append(STD_FLOWS)
    sources += [d / "flows" for d in dept_dirs.values() if (d / "flows").is_dir()]
    for src in sources:
        for f in sorted(src.glob("*.process.json")):
            try:
                p = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                warn(f"{f}: ongeldig JSON ({e}) — overgeslagen")
                continue
            if "domain" not in p:
                warn(f"{f}: geen 'domain'-veld — overgeslagen")
                continue
            flows[p["domain"]] = p
    return flows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("client", help="path to the client folder, e.g. 03-clients/installtech")
    ap.add_argument("-o", "--output", help="output HTML path (default: <client>/asis/output/ASIS-<slug>.html)")
    ap.add_argument("--catalog", help=f"catalog JSON override (default: {CATALOG_PATH})")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any warning was raised")
    ap.add_argument("--dry-run", action="store_true", help="validate only, write nothing")
    args = ap.parse_args()

    client_dir = Path(args.client).resolve()
    if not client_dir.is_dir():
        print(f"error: {client_dir} bestaat niet", file=sys.stderr)
        return 1
    slug = client_dir.name

    # ---- engagement config ----------------------------------------------------------
    cfg_path = client_dir / "engagement-config.json"
    if not cfg_path.exists():
        print(f"error: {cfg_path} ontbreekt — is dit een clientmap?", file=sys.stderr)
        return 1
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        print(f"error: {cfg_path} is geen geldig JSON: {e}", file=sys.stderr)
        return 1
    client_name = cfg.get("client", slug)
    lang = cfg.get("language", "nl")
    if lang not in ("nl", "en"):
        warn(f"engagement-config.json: onbekende taal '{lang}' — 'nl' gebruikt")
        lang = "nl"
    in_scope_depts: list[int] = cfg.get("departments", [])
    if not in_scope_depts:
        warn("engagement-config.json: geen 'departments' in scope")

    # ---- catalog ---------------------------------------------------------------------
    catalog_path = Path(args.catalog).resolve() if args.catalog else CATALOG_PATH
    if not catalog_path.exists():
        print(f"error: catalogus {catalog_path} ontbreekt (gebruik --catalog voor een alternatief)", file=sys.stderr)
        return 1
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"error: {catalog_path} is geen geldig JSON: {e}", file=sys.stderr)
        return 1
    cat_depts = {d["number"]: d for d in catalog.get("departments", [])}
    cat_procs = {p["code"]: p for p in catalog.get("processes", [])}

    for n in in_scope_depts:
        if n not in cat_depts:
            warn(f"engagement-config.json: afdeling {n} staat niet in de catalogus")

    def check_code(code: str, where: str) -> None:
        if code not in cat_procs:
            warn(f"{where}: {code} staat niet in de catalogus (typfout?)")

    # ---- department workspaces --------------------------------------------------------
    dept_dirs: dict[int, Path] = {}
    depts_root = client_dir / "departments"
    if depts_root.is_dir():
        for d in sorted(depts_root.iterdir()):
            m = re.match(r"^(\d+)-", d.name)
            if d.is_dir() and m:
                num = int(m.group(1))
                if num in dept_dirs:
                    warn(f"departments/: meerdere mappen voor afdeling {num} — {d.name} genegeerd")
                    continue
                dept_dirs[num] = d
    for num in dept_dirs:
        if num not in in_scope_depts:
            warn(f"departments/{dept_dirs[num].name}: afdeling {num} staat niet in scope "
                 f"(engagement-config.json 'departments') — genegeerd in de build")

    processes: dict[str, dict] = {}      # code -> process doc
    pains: list[dict] = []               # global register, uid = "<dept>.<PAIN-x>"
    pain_by_uid: dict[str, dict] = {}
    coverage: list[dict] = []
    dept_intro: dict[int, str] = {}
    dept_title_override: dict[int, str] = {}
    dept_status: dict[int, str | None] = {}
    dept_order: dict[int, list[str]] = {}

    for num in sorted(in_scope_depts):
        ddir = dept_dirs.get(num)
        dname = ddir.name if ddir else f"afdeling {num}"

        # ---- pains.md ----
        dept_pains: dict[str, dict] = {}
        pains_path = ddir / "pains.md" if ddir else None
        if pains_path and pains_path.exists():
            _, blocks = split_blocks(pains_path.read_text(encoding="utf-8"),
                                     re.compile(r"^(PAIN-\d+)\s*[-–—:]?\s*(.*)$"))
            for b in blocks:
                pid = b["key"]
                where = f"{dname}/pains.md {pid}"
                if pid in dept_pains:
                    warn(f"{dname}/pains.md: {pid} komt meermaals voor")
                ptype = (b["meta"].get("type") or "").strip()
                psev = (b["meta"].get("severity") or "").strip()
                if ptype and ptype not in PAIN_TYPES:
                    warn(f"{where}: ongeldig type '{ptype}' (verwacht: {' | '.join(PAIN_TYPES)})")
                if psev and psev not in PAIN_SEVERITIES:
                    warn(f"{where}: ongeldige severity '{psev}' (verwacht: {' | '.join(PAIN_SEVERITIES)})")
                codes = CODE_RE.findall(b["meta"].get("processen") or b["meta"].get("processes") or "")
                for c in codes:
                    check_code(c, where)
                pain = {
                    "uid": f"{num}.{pid}",
                    "id": pid,
                    "department": num,
                    "title": b["title"],
                    "quote": (b["meta"].get("citaat") or b["meta"].get("quote") or "").strip().strip('"“”'),
                    "source": b["meta"].get("bron") or b["meta"].get("source") or "",
                    "type": ptype,
                    "severity": psev,
                    "volume": b["meta"].get("volume") or "",
                    "value": b["meta"].get("waardehypothese") or b["meta"].get("value hypothesis") or "",
                    "processes": codes,
                    "html": md_to_html(b["body"]) if b["body"] else "",
                }
                dept_pains[pid] = pain
                pains.append(pain)
                pain_by_uid[pain["uid"]] = pain

        # ---- content/NN-<dept>.md ----
        content_dir = ddir / "content" if ddir else None
        content_files = sorted(content_dir.glob("*.md")) if content_dir and content_dir.is_dir() else []
        if not content_files:
            warn(f"afdeling {num} ({dname}) is in scope maar heeft geen contentbestand "
                 f"(departments/{dname}/content/*.md)")
        for f in content_files:
            text = f.read_text(encoding="utf-8")
            preamble, blocks = split_blocks(text, re.compile(r"^([A-Z][A-Z0-9]{1,4}\.\d{3})\s*[-–—:]?\s*(.*)$"))
            dept_status[num] = parse_status_header(preamble, f"{dname}/content/{f.name}")
            preamble = strip_status_header(preamble)
            h1 = re.search(r"^#\s+(\d+)\.\s*(.*)$", preamble, re.M)
            if h1:
                dept_title_override[num] = h1.group(2).strip()
                preamble = re.sub(r"^#\s+.*$", "", preamble, count=1, flags=re.M).strip()
            if preamble:
                dept_intro[num] = md_to_html(preamble)
            for b in blocks:
                code = b["key"]
                where = f"{dname}/content/{f.name} {code}"
                check_code(code, where)
                if code in processes:
                    warn(f"{where}: is al gedocumenteerd in een ander blok/bestand — laatste wint")
                sev = (b["meta"].get("severity") or "none").strip()
                if sev not in SEVERITIES:
                    warn(f"{where}: ongeldige severity '{sev}' (verwacht: {' | '.join(SEVERITIES)}) — 'none' gebruikt")
                    sev = "none"
                auto = (b["meta"].get("automability") or "").strip() or None
                if auto and auto not in AUTOMABILITIES:
                    warn(f"{where}: ongeldige automability '{auto}' (verwacht: {' | '.join(AUTOMABILITIES)})")
                    auto = None
                pain_ids = PAIN_RE.findall(b["meta"].get("pijn") or b["meta"].get("pains") or "")
                pain_uids: list[str] = []
                for pid in pain_ids:
                    p = dept_pains.get(pid)
                    if p is None:
                        warn(f"{where}: verwijst naar {pid} maar die staat niet in {dname}/pains.md")
                        continue
                    pain_uids.append(p["uid"])
                    if code not in p["processes"]:
                        p["processes"].append(code)
                cat = cat_procs.get(code)
                processes[code] = {
                    "code": code,
                    "title": b["title"] or (loc(cat.get("title"), lang) if cat else code),
                    "department": num,
                    "severity": sev,
                    "automability": auto,
                    "pains": pain_uids,
                    "fields": {
                        "werkwijze": b["meta"].get("huidige werkwijze") or "",
                        "wie": b["meta"].get("wie") or b["meta"].get("who") or "",
                        "systemen": b["meta"].get("systemen") or b["meta"].get("systems") or "",
                        "volume": b["meta"].get("volume & tijd") or b["meta"].get("volume") or "",
                    },
                    "html": md_to_html(b["body"]) if b["body"] else "",
                }
                dept_order.setdefault(num, []).append(code)

        # ---- coverage.md ----
        cov_path = ddir / "coverage.md" if ddir else None
        if cov_path and cov_path.exists():
            rows = parse_coverage(cov_path.read_text(encoding="utf-8"), num, f"{dname}/coverage.md")
            for r in rows:
                check_code(r["code"], f"{dname}/coverage.md")
                cat = cat_procs.get(r["code"])
                if cat and cat.get("department") not in (None, num):
                    r["department"] = cat["department"]
            coverage.extend(rows)

    # pains -> processes: make links symmetric (incl. cross-department references)
    for p in pains:
        for code in p["processes"]:
            proc = processes.get(code)
            if proc is not None and p["uid"] not in proc["pains"]:
                proc["pains"].append(p["uid"])

    # ---- coverage completion ----------------------------------------------------------
    cov_codes = {c["code"] for c in coverage}
    for c in coverage:
        if not c["title"]:
            cat = cat_procs.get(c["code"])
            c["title"] = (loc(cat.get("title"), lang) if cat else "") or \
                         (processes[c["code"]]["title"] if c["code"] in processes else c["code"])
        if c["scope"] and c["code"] in processes:
            c["severity"] = processes[c["code"]]["severity"]
        elif c["scope"]:
            warn(f"coverage: {c['code']} is 'in scope' maar heeft geen documentatie in content/")
    for code, s in sorted(processes.items()):
        if code not in cov_codes:
            coverage.append({"code": code, "title": s["title"], "department": s["department"],
                             "scope": True, "severity": s["severity"], "note": ""})
    coverage.sort(key=lambda c: (c["department"] if c["department"] is not None else 99, c["code"]))

    # ---- flows -------------------------------------------------------------------------
    flows = load_flows(dept_dirs)
    flow_codes: set[str] = set()
    for dom, p in flows.items():
        if dom not in in_scope_depts:
            continue
        for n in p.get("nodes", []):
            code = n.get("process")
            if code:
                flow_codes.add(code)
                check_code(code, f"flow '{p.get('id', dom)}' node '{n.get('id')}'")

    # content blocks that appear in no flow node AND not in the coverage matrix
    for code in processes:
        if code not in flow_codes and code not in cov_codes:
            warn(f"{code} is gedocumenteerd maar komt in geen enkele flow-node voor "
                 f"en staat niet in coverage.md")

    # ---- departments -------------------------------------------------------------------
    departments = []
    for num in sorted(in_scope_depts):
        cat = cat_depts.get(num)
        departments.append({
            "number": num,
            "id": cat.get("id") if cat else None,
            "title": dept_title_override.get(num)
                     or (loc(cat.get("title"), lang) if cat else f"Afdeling {num}"),
            "intro_html": dept_intro.get(num, ""),
            "status": dept_status.get(num),
            "process": flows.get(num),
            "processes": dept_order.get(num, []),
        })

    # ---- intro -------------------------------------------------------------------------
    intro_path = client_dir / "asis" / "intro.md"
    intro_html = md_to_html(intro_path.read_text(encoding="utf-8")) if intro_path.exists() else ""

    data = {
        "client": {
            "name": client_name,
            "title": cfg.get("title", "AS-IS review"),
            "sector": cfg.get("sector", ""),
            "language": lang,
            "intro_html": intro_html,
            "labels": cfg.get("labels", {}),
        },
        "meta": {
            "catalog": catalog.get("source", ""),
            "version": cfg.get("version", ""),
            "generated": datetime.date.today().isoformat(),
        },
        "departments": departments,
        "processes": processes,
        "coverage": coverage,
        "pains": pains,
    }

    # ---- assemble ----------------------------------------------------------------------
    tpl = (VIEWER / "template.html").read_text(encoding="utf-8")
    css = (VIEWER / "viewer.css").read_text(encoding="utf-8")
    js = (VIEWER / "viewer.js").read_text(encoding="utf-8")
    if cfg.get("accentColor"):
        css += f'\n:root {{ --accent: {cfg["accentColor"]}; }}\n'
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out_html = (tpl
                .replace("__ASIS_TITLE__", html.escape(f"{data['client']['title']} — {client_name}"))
                .replace("/*__ASIS_CSS__*/", css)
                .replace("/*__ASIS_DATA__*/ null", payload)
                .replace("/*__ASIS_JS__*/", js))

    out_path = Path(args.output) if args.output else client_dir / "asis" / "output" / f"ASIS-{slug}.html"
    if not args.dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_html, encoding="utf-8")

    in_scope = sum(1 for c in coverage if c["scope"])
    print(("gecontroleerd (dry-run): " if args.dry_run else "AS-IS gebouwd: ") + str(out_path))
    print(f"  {len(departments)} afdelingen · {len(processes)} gedocumenteerde processen · "
          f"{in_scope} in scope · {len(pains)} pijnpunten")
    if WARNINGS:
        print(f"  {len(WARNINGS)} waarschuwing(en) — zie hierboven")
        if args.strict:
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
