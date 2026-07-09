#!/usr/bin/env python3
"""build_proposal.py — compile a client's opportunity register + assumptions
into the interactive roadmap-proposal HTML (single self-contained file).

Usage:
    python3 07-roadmap-engine/tools/build_proposal.py 03-clients/<slug> [--dry-run] [--strict] [--baselines <path>]

Reads (in the client workspace):
    engagement-config.json
    analysis/opportunities.md      ## OPP-x blocks per the spec in 07-roadmap-engine/README.md
    analysis/assumptions.json
    proposal/keep.md               optional "what NOT to change" content (passthrough)
    departments/NN-*/content/*.md  gate: every in-scope department must be Status: approved

Reads (engine):
    07-roadmap-engine/proposal/template.html, proposal.css, proposal.js
    07-roadmap-engine/baselines/effort-baselines.json  (built-in fallback if absent)

Writes:
    03-clients/<slug>/proposal/output/ROADMAP-<slug>.html

Zero dependencies, Python 3 stdlib only. Value formulas are validated
(tokens: assumption ids, numbers, + - * / parens only) and compiled to static
JS arrow functions — the page never evals anything at runtime.

Exit code 0 = built (or dry-run clean); 1 = errors (or warnings with --strict).
"""

import ast
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent   # 07-roadmap-engine/
TEMPLATE_DIR = ENGINE_DIR / "proposal"
DEFAULT_BASELINES = ENGINE_DIR / "baselines" / "effort-baselines.json"
BRANDING_DIR = ENGINE_DIR / "branding"

BRAND_URL_RE = re.compile(r"""url\(\s*(['"]?)([^)'"]+)\1\s*\)""")


def branding_css(client_dir):
    """Optional white-label design tokens, prepended to the built CSS so the
    HTML stays fully self-contained (contract: 07-roadmap-engine/branding/README.md).
    Engine tokens first, then the per-client override (client wins by cascade);
    url() references to png/svg files in the branding folder are inlined as
    data-URIs. No branding files -> returns "" (build output byte-identical).
    Note: the per-client accentColor still wins for the accent — the proposal
    page applies it at runtime from the data payload."""
    import base64
    parts = []
    for folder in (BRANDING_DIR, client_dir / "branding"):
        tokens = folder / "tokens.css"
        if not tokens.is_file():
            continue

        def inline(m):
            f = folder / m.group(2).strip()
            if f.suffix.lower() in (".png", ".svg") and f.is_file():
                mime = "image/png" if f.suffix.lower() == ".png" else "image/svg+xml"
                b64 = base64.b64encode(f.read_bytes()).decode("ascii")
                return f'url("data:{mime};base64,{b64}")'
            return m.group(0)

        parts.append(BRAND_URL_RE.sub(inline, tokens.read_text(encoding="utf-8")).rstrip() + "\n")
    return "\n".join(parts)

# Fallback matching the spec example in 07-roadmap-engine/README.md — used
# until baselines/effort-baselines.json ships (another workstream owns it).
FALLBACK_BASELINES = {
    "version": "0.1-seed-builtin-fallback",
    "day_rate_default": 950,
    "implementation_days": {
        "automation": {"S": 3,  "M": 8,  "L": 18},
        "agent-T1":   {"S": 5,  "M": 12, "L": 25},
        "agent-T2":   {"S": 8,  "M": 18, "L": 35},
        "agent-T3":   {"S": 12, "M": 30, "L": 60},
        "hybrid":     {"S": 5,  "M": 12, "L": 25},
    },
}

STATUS_ENUM = {"proposed", "confirmed", "deferred", "discarded"}
ALLOC_ENUM = {"automation", "agent-T1", "agent-T2", "agent-T3", "hybrid"}
EFFORT_ENUM = {"S", "M", "L"}
WAVE_ENUM = {"1", "2", "3", "-"}
VERDICT_ENUM = {"quick-win", "big-bet", "fill-in", "discard"}

WEIGHTS = {
    "value": {"hours": 0.50, "quality": 0.25, "strategic": 0.25},
    "feasibility": {"data": 0.40, "technical": 0.30, "ownership": 0.30},
    "high": 3.5,
}

ID_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
FORMULA_CHARS_RE = re.compile(r"^[A-Za-z0-9_+\-*/().\s]*$")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def dump(self):
        for e in self.errors:
            print(f"  ERROR   {e}")
        for w in self.warnings:
            print(f"  WARNING {w}")


# ---------------------------------------------------------------- parsing

def parse_opp_blocks(text, rep):
    """Split analysis/opportunities.md into ## OPP-x blocks of metadata bullets."""
    blocks = []
    current = None
    for line in text.splitlines():
        m = re.match(r"^##\s+(OPP-\d+)\s*(?:[—–-]+\s*(.*))?$", line)
        if m:
            current = {"id": m.group(1), "title": (m.group(2) or "").strip(), "fields": {}, "_last": None}
            blocks.append(current)
            continue
        if current is None:
            continue
        b = re.match(r"^-\s+\*\*(.+?):?\*\*\s*:?\s*(.*)$", line)
        if b:
            key = b.group(1).strip().rstrip(":").lower()
            current["fields"][key] = b.group(2).strip()
            current["_last"] = key
        elif line.strip() and not line.startswith("#") and current["_last"]:
            # continuation line of the previous bullet
            current["fields"][current["_last"]] += " " + line.strip()
    seen = set()
    for blk in blocks:
        if blk["id"] in seen:
            rep.error(f"{blk['id']}: duplicate OPP id")
        seen.add(blk["id"])
        if not blk["title"]:
            rep.warn(f"{blk['id']}: block has no title after the id")
    return blocks


def parse_scores(raw, keys, oid, label, rep):
    out = {}
    for m in re.finditer(r"([A-Za-z_]+)\s*=\s*([0-9.]+)", raw or ""):
        out[m.group(1)] = float(m.group(2))
    for k in keys:
        if k not in out:
            rep.error(f"{oid}: {label} is missing '{k}' (got: {raw!r})")
            out[k] = 0.0
        elif not (1 <= out[k] <= 5):
            rep.error(f"{oid}: {label} '{k}={out[k]:g}' out of range 1-5")
    extra = set(out) - set(keys)
    if extra:
        rep.warn(f"{oid}: {label} has unknown keys {sorted(extra)}")
    return out


def parse_csv_ids(raw):
    return [p.strip() for p in (raw or "").replace(";", ",").split(",") if p.strip()]


# ---------------------------------------------------------------- formulas

class FormulaChecker(ast.NodeVisitor):
    """Allow only: numbers, assumption names, + - * /, unary +/-, parentheses."""

    def __init__(self):
        self.names = set()
        self.bad = []

    def visit_Expression(self, node):
        self.visit(node.body)

    def visit_BinOp(self, node):
        if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            self.bad.append(type(node.op).__name__)
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        if not isinstance(node.op, (ast.UAdd, ast.USub)):
            self.bad.append(type(node.op).__name__)
        self.visit(node.operand)

    def visit_Constant(self, node):
        if not isinstance(node.value, (int, float)):
            self.bad.append(f"constant {node.value!r}")

    def visit_Name(self, node):
        self.names.add(node.id)

    def generic_visit(self, node):
        if isinstance(node, (ast.Expression, ast.Load)):
            super().generic_visit(node)
        else:
            self.bad.append(type(node).__name__)


def check_formula(expr, assumption_ids, oid, rep):
    """Validate a Waardeformule; return the set of assumption ids it uses, or None."""
    if not FORMULA_CHARS_RE.match(expr):
        bad = sorted(set(re.sub(r"[A-Za-z0-9_+\-*/().\s]", "", expr)))
        rep.error(f"{oid}: Waardeformule contains illegal characters {bad} "
                  "(allowed: assumption ids, numbers, + - * / parens)")
        return None
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        rep.error(f"{oid}: Waardeformule does not parse: {exc.msg}")
        return None
    chk = FormulaChecker()
    chk.visit(tree)
    if chk.bad:
        rep.error(f"{oid}: Waardeformule uses disallowed constructs: {sorted(set(chk.bad))}")
        return None
    dangling = sorted(chk.names - set(assumption_ids))
    if dangling:
        rep.error(f"{oid}: Waardeformule references unknown assumption id(s): {', '.join(dangling)}")
        return None
    return chk.names


def eval_formula(expr, values):
    """Evaluate a validated formula at given assumption values (pure walker, no eval)."""
    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.BinOp):
            l, r = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add):
                return l + r
            if isinstance(node.op, ast.Sub):
                return l - r
            if isinstance(node.op, ast.Mult):
                return l * r
            return l / r if r != 0 else float("inf")
        if isinstance(node, ast.UnaryOp):
            v = walk(node.operand)
            return -v if isinstance(node.op, ast.USub) else v
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return values[node.id]
        raise ValueError(f"unexpected node {type(node).__name__}")
    return walk(ast.parse(expr, mode="eval"))


def compile_formula_js(expr):
    """Compile a validated formula to a static JS arrow function string."""
    body = re.sub(r"\b[A-Za-z_][A-Za-z0-9_]*\b", lambda m: "A." + m.group(0), expr)
    body = " ".join(body.split())
    return f"(A) => ({body})"


# ---------------------------------------------------------------- validation

def load_json(path, rep, what):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        rep.error(f"{what} missing: {path}")
    except json.JSONDecodeError as exc:
        rep.error(f"{what} is not valid JSON ({path}): {exc}")
    return None


def validate_assumptions(doc, rep):
    if doc is None:
        return []
    items = doc.get("assumptions")
    if not isinstance(items, list) or not items:
        rep.error("assumptions.json: top-level 'assumptions' array missing or empty")
        return []
    if not 4 <= len(items) <= 8:
        rep.warn(f"assumptions.json: {len(items)} assumptions (spec recommends 4-8)")
    seen = set()
    out = []
    for a in items:
        aid = a.get("id", "")
        if not ID_RE.match(aid):
            rep.error(f"assumptions.json: invalid id {aid!r} (must be a bare identifier)")
            continue
        if aid in seen:
            rep.error(f"assumptions.json: duplicate id '{aid}'")
            continue
        seen.add(aid)
        for k in ("min", "max", "step", "default"):
            if not isinstance(a.get(k), (int, float)):
                rep.error(f"assumptions.json '{aid}': '{k}' missing or not a number")
        if all(isinstance(a.get(k), (int, float)) for k in ("min", "max", "step", "default")):
            if a["min"] >= a["max"]:
                rep.error(f"assumptions.json '{aid}': min must be < max")
            if not (a["min"] <= a["default"] <= a["max"]):
                rep.error(f"assumptions.json '{aid}': default {a['default']} outside [min, max]")
            if a["step"] <= 0:
                rep.error(f"assumptions.json '{aid}': step must be > 0")
        if not a.get("label"):
            rep.warn(f"assumptions.json '{aid}': no label")
        if not a.get("source"):
            rep.warn(f"assumptions.json '{aid}': no source/calibration note")
        out.append({
            "id": aid, "label": a.get("label", aid), "unit": a.get("unit", ""),
            "min": a.get("min", 0), "max": a.get("max", 1), "step": a.get("step", 1),
            "default": a.get("default", 0), "source": a.get("source", ""),
        })
    return out


def validate_opp(blk, assumption_ids, baselines, day_rate, rep):
    oid = blk["id"]
    f = blk["fields"]

    def get(*keys):
        for k in keys:
            if k in f:
                return f[k]
        return ""

    status = get("status")
    if status not in STATUS_ENUM:
        rep.error(f"{oid}: Status '{status}' not in {sorted(STATUS_ENUM)}")
    alloc = get("allocatie", "allocation")
    if alloc not in ALLOC_ENUM:
        rep.error(f"{oid}: Allocatie '{alloc}' not in {sorted(ALLOC_ENUM)}")
    effort = get("effort")
    if effort not in EFFORT_ENUM:
        rep.error(f"{oid}: Effort '{effort}' not in {sorted(EFFORT_ENUM)}")
    wave_raw = get("wave")
    if wave_raw not in WAVE_ENUM:
        rep.error(f"{oid}: Wave '{wave_raw}' not in {sorted(WAVE_ENUM)}")
    wave = 0 if wave_raw == "-" else int(wave_raw) if wave_raw in {"1", "2", "3"} else 0

    vs = parse_scores(get("value-scores"), ("hours", "quality", "strategic"), oid, "Value-scores", rep)
    fs = parse_scores(get("feasibility-scores"), ("data", "technical", "ownership"), oid, "Feasibility-scores", rep)
    try:
        adoption = float(get("adoptie", "adoption") or 0)
    except ValueError:
        adoption = 0.0
    if not (1 <= adoption <= 5):
        rep.error(f"{oid}: Adoptie '{get('adoptie', 'adoption')}' out of range 1-5")

    value = round(sum(WEIGHTS["value"][k] * vs[k] for k in vs if k in WEIGHTS["value"]), 2)
    feas = round(sum(WEIGHTS["feasibility"][k] * fs[k] for k in fs if k in WEIGHTS["feasibility"]), 2)
    hi = WEIGHTS["high"]
    quadrant = ("quick-win" if feas >= hi else "big-bet") if value >= hi else \
               ("fill-in" if feas >= hi else "discard")

    verdict_raw = get("verdict")
    vm = re.match(r"^(quick-win|big-bet|fill-in|discard)\s*(?:[—–-]+\s*confidence\s*:\s*(\S+))?\s*$",
                  verdict_raw, re.IGNORECASE)
    if not vm:
        rep.error(f"{oid}: Verdict '{verdict_raw}' unparseable "
                  "(expected '<quick-win|big-bet|fill-in|discard> — confidence: <level>')")
        verdict, confidence = "", ""
    else:
        verdict, confidence = vm.group(1).lower(), (vm.group(2) or "").strip()
        if not confidence:
            rep.warn(f"{oid}: Verdict carries no confidence level")
    if verdict and verdict != quadrant:
        rep.error(f"{oid}: verdict/quadrant mismatch — Verdict says '{verdict}' but "
                  f"Value {value:.2f} × Feasibility {feas:.2f} computes '{quadrant}' (high = >= {hi})")

    # formula
    formula = get("waardeformule", "value formula")
    used_ids = set()
    annual_default = None
    if formula:
        used = check_formula(formula, assumption_ids, oid, rep)
        if used is not None:
            used_ids = used
            declared = set(parse_csv_ids(get("aannames", "assumptions")))
            unknown_declared = declared - set(assumption_ids)
            if unknown_declared:
                rep.error(f"{oid}: Aannames lists unknown assumption id(s): {', '.join(sorted(unknown_declared))}")
            if declared and declared != used:
                rep.warn(f"{oid}: Aannames list {sorted(declared)} != formula ids {sorted(used)}")
    elif wave in (1, 2, 3):
        rep.error(f"{oid}: Wave {wave} requires a Waardeformule (only discards may omit it)")

    # cost model: implementation = days(alloc, effort) x day_rate; year1 = impl + 12 x tooling
    tooling_raw = get("tooling €/maand", "tooling eur/maand", "tooling")
    tooling = 0.0
    if tooling_raw:
        try:
            tooling = float(tooling_raw.replace("€", "").replace(",", ".").strip())
        except ValueError:
            rep.error(f"{oid}: Tooling €/maand '{tooling_raw}' is not a number")
    days = 0
    impl_days = baselines.get("implementation_days", {})
    if alloc in ALLOC_ENUM and effort in EFFORT_ENUM:
        if alloc not in impl_days:
            rep.error(f"{oid}: allocation '{alloc}' has no entry in the effort baselines")
        elif effort not in impl_days[alloc]:
            rep.error(f"{oid}: effort '{effort}' has no entry in baselines for '{alloc}'")
        else:
            days = impl_days[alloc][effort]
    impl_cost = days * day_rate
    year1_cost = impl_cost + 12 * tooling

    return {
        "id": oid,
        "title": blk["title"],
        "status": status,
        "departments": parse_csv_ids(get("afdelingen", "departments")),
        "processes": parse_csv_ids(get("processen", "processes")),
        "pains": parse_csv_ids(get("pijnpunten", "pains")),
        "allocation": alloc,
        "effort": effort,
        "wave": wave,
        "scores": {**{k: vs[k] for k in ("hours", "quality", "strategic") if k in vs},
                   **{k: fs[k] for k in ("data", "technical", "ownership") if k in fs},
                   "adoption": adoption},
        "value": value,
        "feasibility": feas,
        "quadrant": quadrant,
        "verdict": verdict or quadrant,
        "confidence": confidence,
        "tooling": tooling,
        "days": days,
        "impl_cost": round(impl_cost),
        "year1_cost": round(year1_cost),
        "formula_text": formula,
        "would_change": get("wat dit zou veranderen", "what would change this"),
        "enablers": get("enablers"),
        "risk": get("risico / ai act", "risico", "risk / ai act", "risk"),
        "first_step": get("eerste stap", "first step"),
        "_formula_ids": sorted(used_ids),
        "_annual_default": annual_default,
    }


# ---------------------------------------------------------------- gates

def check_department_gate(client_dir, config, rep, gate_error):
    """Every in-scope department's content file must carry Status: approved."""
    report = gate_error  # rep.error normally; rep.warn under --dry-run
    dept_dir = client_dir / "departments"
    for num in config.get("departments", []):
        prefix = f"{int(num):02d}-"
        matches = sorted(dept_dir.glob(prefix + "*")) if dept_dir.is_dir() else []
        if not matches:
            report(f"gate: in-scope department {num} has no workspace under departments/{prefix}*")
            continue
        content_files = sorted(matches[0].glob("content/*.md"))
        if not content_files:
            report(f"gate: department {num} ({matches[0].name}) has no content/*.md — AS-IS not documented")
            continue
        for cf in content_files:
            status = None
            for line in cf.read_text(encoding="utf-8").splitlines():
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 4 and cells[2].lower() in {"draft", "consultant-review", "client-review", "approved"}:
                    status = cells[2].lower()
                    break
            if status is None:
                report(f"gate: {cf.relative_to(client_dir)} has no status header table")
            elif status != "approved":
                report(f"gate: {cf.relative_to(client_dir)} Status is '{status}' — proposal requires 'approved'")


# ---------------------------------------------------------------- keep.md

def md_to_html(md):
    """Minimal, dependency-free markdown -> HTML for proposal/keep.md passthrough."""
    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    out, in_list, para = [], False, []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    for line in md.splitlines():
        stripped = line.strip()
        h = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if h:
            flush_para(); close_list()
            level = min(len(h.group(1)) + 2, 5)  # '#'/'##' -> h3, deeper -> h4/h5
            out.append(f"<h{level}>{inline(h.group(2))}</h{level}>")
        elif stripped.startswith(("- ", "* ")):
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + inline(stripped[2:]) + "</li>")
        elif not stripped:
            flush_para(); close_list()
        else:
            close_list()
            para.append(stripped)
    flush_para(); close_list()
    return "\n".join(out)


# ---------------------------------------------------------------- build

def detect_hourly_id(assumptions, opps):
    """Find the loaded-hourly-cost assumption so the page can derive hours released."""
    candidates = [a["id"] for a in assumptions
                  if re.search(r"hourly|uurkost|uurloon|hour_cost|per_hour|per_uur", a["id"], re.IGNORECASE)]
    if not candidates:
        return None
    preferred = [c for c in candidates if "hourly_cost" in c] or candidates
    hid = preferred[0]
    if any(hid in o["_formula_ids"] for o in opps):
        return hid
    return None


def build_data_payload(config, slug, assumptions, opps, keep_html, built):
    hourly_id = detect_hourly_id(assumptions, opps)
    payload = {
        "client": config.get("client", slug),
        "slug": slug,
        "lang": config.get("language", "nl"),
        "accent": config.get("accentColor", "#D9480F"),
        "sector": config.get("sector", ""),
        "currency": config.get("currency", "EUR"),
        "day_rate": config.get("day_rate", FALLBACK_BASELINES["day_rate_default"]),
        "built": built,
        "weights": WEIGHTS,
        "hourly_id": hourly_id,
        "assumptions": assumptions,
        "opps": [],
        "keep_html": keep_html,
    }
    formulas_js = []
    for o in opps:
        entry = {k: v for k, v in o.items() if not k.startswith("_")}
        entry["uses_hourly"] = bool(hourly_id) and hourly_id in o["_formula_ids"]
        payload["opps"].append(entry)
        if o["formula_text"]:
            formulas_js.append(f'    "{o["id"]}": {compile_formula_js(o["formula_text"])}')
    data_json = json.dumps(payload, ensure_ascii=False, indent=2)
    data_json = data_json.replace("</", "<\\/")  # never break out of the <script> tag
    # splice the (non-JSON) compiled formula functions into the object literal
    formulas_block = ",\n  \"formulas\": {\n" + ",\n".join(formulas_js) + "\n  }\n}"
    assert data_json.rstrip().endswith("}")
    return data_json.rstrip()[:-1].rstrip() + formulas_block


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    flags = [a for a in argv if a.startswith("--")]
    baselines_path = None
    if "--baselines" in argv:
        i = argv.index("--baselines")
        if i + 1 >= len(argv):
            print("ERROR: --baselines needs a path argument")
            return 1
        baselines_path = Path(argv[i + 1])
        args = [a for a in args if a != argv[i + 1]]
    dry_run = "--dry-run" in flags
    strict = "--strict" in flags
    unknown = [f for f in flags if f not in ("--dry-run", "--strict", "--baselines")]
    if unknown:
        print(f"ERROR: unknown flag(s) {unknown}\n\n{__doc__}")
        return 1
    if len(args) != 1:
        print(__doc__)
        return 1

    client_dir = Path(args[0]).resolve()
    if not client_dir.is_dir():
        print(f"ERROR: client workspace not found: {client_dir}")
        return 1
    slug = client_dir.name
    rep = Report()

    # ---- inputs
    config = load_json(client_dir / "engagement-config.json", rep, "engagement-config.json")
    if config is None:
        rep.dump()
        return 1
    if config.get("language") not in ("nl", "en"):
        rep.error(f"engagement-config.json: language '{config.get('language')}' must be 'nl' or 'en'")
    if not isinstance(config.get("day_rate"), (int, float)):
        rep.warn("engagement-config.json: no numeric day_rate — using baselines default")

    baselines_file = baselines_path or DEFAULT_BASELINES
    if baselines_file.is_file():
        baselines = load_json(baselines_file, rep, "effort baselines") or FALLBACK_BASELINES
    else:
        baselines = FALLBACK_BASELINES
        rep.warn(f"effort baselines not found at {baselines_file} — using built-in fallback "
                 f"({FALLBACK_BASELINES['version']})")
    day_rate = config.get("day_rate") or baselines.get("day_rate_default", 950)

    gate_report = rep.warn if dry_run else rep.error
    assumptions_doc = None
    apath = client_dir / "analysis" / "assumptions.json"
    if apath.is_file():
        assumptions_doc = load_json(apath, rep, "analysis/assumptions.json")
    else:
        gate_report("gate: analysis/assumptions.json missing — the proposal cannot be built without the assumption model")
    assumptions = validate_assumptions(assumptions_doc, rep)
    assumption_ids = [a["id"] for a in assumptions]

    opath = client_dir / "analysis" / "opportunities.md"
    opps = []
    if opath.is_file():
        blocks = parse_opp_blocks(opath.read_text(encoding="utf-8"), rep)
        if not blocks:
            rep.error("analysis/opportunities.md contains no ## OPP-x blocks")
        opps = [validate_opp(b, assumption_ids, baselines, day_rate, rep) for b in blocks]
    else:
        gate_report("gate: analysis/opportunities.md missing — no opportunity register to build from")

    check_department_gate(client_dir, config, rep, gate_report)

    keep_path = client_dir / "proposal" / "keep.md"
    keep_html = md_to_html(keep_path.read_text(encoding="utf-8")) if keep_path.is_file() else ""

    # evaluate formulas at defaults for the console summary
    defaults = {a["id"]: a["default"] for a in assumptions}
    for o in opps:
        if o["formula_text"] and not rep.errors:
            try:
                o["_annual_default"] = eval_formula(o["formula_text"], defaults)
            except Exception:
                pass

    # ---- report
    print(f"build_proposal — {slug}")
    print(f"  opportunities: {len(opps)}   assumptions: {len(assumptions)}   "
          f"baselines: {baselines.get('version', '?')}   day rate: € {day_rate:g}")
    rep.dump()
    failed = bool(rep.errors) or (strict and bool(rep.warnings))
    if failed:
        print(f"\nFAILED — {len(rep.errors)} error(s), {len(rep.warnings)} warning(s)"
              + (" [--strict]" if strict and not rep.errors else ""))
        return 1

    if opps:
        print(f"  {'id':7} {'V':>5} {'F':>5}  {'quadrant':10} {'wave':4} {'€/yr@def':>10} {'year-1':>8} {'payback':>8}")
        for o in opps:
            val = o.get("_annual_default")
            pb = (o["year1_cost"] / (val / 12)) if val else None
            print(f"  {o['id']:7} {o['value']:5.2f} {o['feasibility']:5.2f}  {o['quadrant']:10} "
                  f"{(o['wave'] or '-'):>4} {('%.0f' % val) if val is not None else '—':>10} "
                  f"{o['year1_cost']:>8} {('%.1f mnd' % pb) if pb else '—':>8}")

    if dry_run:
        print(f"\nDRY-RUN OK — {len(rep.warnings)} warning(s), nothing written")
        return 0

    # ---- render
    template = (TEMPLATE_DIR / "template.html").read_text(encoding="utf-8")
    css = branding_css(client_dir) + (TEMPLATE_DIR / "proposal.css").read_text(encoding="utf-8")
    js = (TEMPLATE_DIR / "proposal.js").read_text(encoding="utf-8")
    built = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data_js = build_data_payload(config, slug, assumptions, opps, keep_html, built)

    lang = config.get("language", "nl")
    title = f"{config.get('client', slug)} — " + ("AI-integratie roadmap" if lang == "nl" else "AI integration roadmap")
    for needle in ("__ROADMAP_TITLE__", "/*__ROADMAP_CSS__*/", "/*__ROADMAP_DATA__*/ null", "/*__ROADMAP_JS__*/"):
        assert needle in template, f"template.html is missing placeholder {needle}"
    page = (template
            .replace("__ROADMAP_TITLE__", html.escape(title))
            .replace("/*__ROADMAP_CSS__*/", css)
            .replace("/*__ROADMAP_DATA__*/ null", data_js)
            .replace("/*__ROADMAP_JS__*/", js))

    out_dir = client_dir / "proposal" / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"ROADMAP-{slug}.html"
    out_path.write_text(page, encoding="utf-8")
    print(f"\nOK — wrote {out_path} ({out_path.stat().st_size // 1024} KB), "
          f"{len(rep.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
