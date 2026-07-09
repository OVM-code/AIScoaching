#!/usr/bin/env python3
"""Mechanical validator for one Roadmap Engine engagement workspace.

Usage:
    python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug> [--strict]

Mirrors the Gates section of 07-roadmap-engine/README.md (the binding spec):
  engagement-config.json    required fields, language nl|en, departments are
                            catalog numbers (catalog missing -> warn + skip codes)
  engagements.csv           exact header, unique slugs, stage enum, YYYY-MM-DD
                            dates, a row for this slug, stage consistent with
                            the artifacts present
  departments/NN-*/         content status header table + enums, PAIN references
                            resolve to pains.md blocks, pain enums + process
                            codes, flow *.process.json referential integrity
  analysis/opportunities.md OPP enums, scores 1-5, verdict = computed quadrant
                            (high >= 3.5), references resolve, Waardeformule
                            tokens all in assumptions.json, Wave 1-3 needs a
                            formula, no opportunities before every in-scope
                            department is approved
  analysis/assumptions.json schema, unique snake_case ids, min <= default <= max

Exit codes: 0 ok - 1 errors - 2 only warnings (with --strict).
Zero errors and warnings is the definition of done after every authoring step.
Stdlib only; no network.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- constants

STAGES = ["intake", "discovery", "asis-review", "diagnosis", "proposal",
          "confirmed", "delivery", "aftercare", "closed"]
STAGE_IDX = {s: i for i, s in enumerate(STAGES)}
CSV_HEADER = ["slug", "client_name", "sector", "language", "stage",
              "departments_in_scope", "next_action", "last_updated", "notes"]
LANGUAGES = {"nl", "en"}
CONFIG_REQUIRED = ("client", "slug", "language", "sector", "departments",
                   "day_rate", "currency")

PAIN_TYPES = {"retype", "chase", "wait", "error", "skill-bottleneck",
              "no-visibility"}
PAIN_SEVERITIES = {"minor", "major", "critical"}
CONTENT_STATUSES = {"draft", "consultant-review", "client-review", "approved"}
BLOCK_SEVERITIES = {"none", "minor", "major", "critical"}
AUTOMABILITIES = {"human", "automation", "agent", "hybrid"}
OPP_STATUSES = {"proposed", "confirmed", "deferred", "discarded"}
ALLOCATIONS = {"automation", "agent-T1", "agent-T2", "agent-T3", "hybrid"}
EFFORTS = {"S", "M", "L"}
WAVES = {"1", "2", "3", "-"}
VERDICTS = {"quick-win", "big-bet", "fill-in", "discard"}
NODE_TYPES = {"start", "end", "task", "subprocess", "gateway",
              "gateway-parallel"}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CODE_RE = re.compile(r"\b[A-Z]{2,5}\.\d{3}\b")
PAIN_RE = re.compile(r"\bPAIN-\d+\b")
ID_RE = re.compile(r"^[a-z_][a-z0-9_]*$")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
DEPT_DIR_RE = re.compile(r"^(\d{2})-")
SEPARATOR_ROW_RE = re.compile(r"^\|[\s\-:|]+\|$")
FORMULA_TOKEN_RE = re.compile(r"\d+(?:\.\d+)?|[a-z_][a-z0-9_]*|[+\-*/()]|\S")

ERRORS: list[str] = []
WARNS: list[str] = []


def err(m: str) -> None:
    ERRORS.append(m)
    print(f"  ✗ {m}")


def warn(m: str) -> None:
    WARNS.append(m)
    print(f"  ! {m}")


def ok(m: str) -> None:
    print(f"  ✓ {m}")


# ------------------------------------------------------------------ helpers

def read_md(path: Path) -> str:
    """Read markdown with HTML comments stripped — commented-out example
    blocks in skeletons must not count as real blocks."""
    return COMMENT_RE.sub("", path.read_text(encoding="utf-8"))


def split_blocks(text: str, id_pattern: str) -> list[tuple[str, str]]:
    """[(block id, body)] for every '## <id> ...' heading."""
    heads = list(re.finditer(r"^##\s+(" + id_pattern + r")\b[^\n]*$",
                             text, re.M))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out.append((m.group(1), text[m.end():end]))
    return out


def field(block: str, name: str) -> str | None:
    m = re.search(r"\*\*" + re.escape(name) + r"\s*:\*\*\s*(.+)", block)
    if not m:
        return None
    val = m.group(1).strip()
    return val or None


def header_status(text: str) -> tuple[str | None, str | None]:
    """(status, reviewed-date) from the '| Client | Afdeling | Status |
    Laatst gereviewd |' header table; (None, None) when absent."""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("|") and re.search(r"\|\s*Status\s*\|", s, re.I):
            cols = [c.strip().lower() for c in s.strip("|").split("|")]
            for j in range(i + 1, min(i + 4, len(lines))):
                d = lines[j].strip()
                if not d.startswith("|") or SEPARATOR_ROW_RE.match(d):
                    continue
                vals = [c.strip() for c in d.strip("|").split("|")]
                row = dict(zip(cols, vals))
                return row.get("status"), row.get("laatst gereviewd")
            return None, None
    return None, None


def parse_scores(text: str) -> dict[str, float]:
    """'hours=4, quality=3' -> {'hours': 4.0, 'quality': 3.0}"""
    return {k: float(v) for k, v in
            re.findall(r"([a-z]+)\s*=\s*(\d+(?:\.\d+)?)", text)}


def as_number(text: str | None) -> float | None:
    if text is None:
        return None
    m = re.match(r"(\d+(?:\.\d+)?)", text)
    return float(m.group(1)) if m else None


# ------------------------------------------------------------------ catalog

def load_catalog(repo: Path) -> dict | None:
    path = repo / "07-roadmap-engine" / "catalog" / "departments.json"
    if not path.exists():
        warn("catalog: 07-roadmap-engine/catalog/departments.json not found "
             "— department/process-code checks skipped")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        err(f"catalog: departments.json is not valid JSON ({e})")
        return None
    depts = data.get("departments", [])
    procs = data.get("processes", [])
    cat = {
        "numbers": {d.get("number") for d in depts},
        "prefixes": {d.get("prefix") for d in depts},
        "codes": {p.get("code") for p in procs},
        "code_dept": {p.get("code"): p.get("department") for p in procs},
    }
    ok(f"catalog: {len(depts)} department(s), {len(procs)} process code(s)")
    return cat


# ----------------------------------------------------- engagement-config.json

def check_config(client: Path) -> dict | None:
    path = client / "engagement-config.json"
    if not path.exists():
        err("engagement-config.json missing")
        return None
    try:
        cfg = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        err(f"engagement-config.json: invalid JSON ({e})")
        return None
    for key in CONFIG_REQUIRED:
        if key not in cfg:
            err(f"engagement-config.json: required field '{key}' missing")
    if cfg.get("slug") and cfg["slug"] != client.name:
        err(f"engagement-config.json: slug '{cfg['slug']}' does not match "
            f"folder name '{client.name}'")
    lang = cfg.get("language")
    if lang is not None and lang not in LANGUAGES:
        err(f"engagement-config.json: language must be one of nl|en, "
            f"got '{lang}'")
    deps = cfg.get("departments")
    if deps is not None:
        if (not isinstance(deps, list)
                or not all(isinstance(d, int) and not isinstance(d, bool)
                           for d in deps)):
            err("engagement-config.json: departments must be a list of "
                "catalog department numbers (integers)")
            cfg["departments"] = [d for d in deps if isinstance(d, int)
                                  and not isinstance(d, bool)] \
                if isinstance(deps, list) else []
        elif len(set(deps)) != len(deps):
            err("engagement-config.json: duplicate department numbers")
        elif not deps:
            warn("engagement-config.json: departments is empty — nothing "
                 "in scope")
    rate = cfg.get("day_rate")
    if rate is not None and (isinstance(rate, bool)
                             or not isinstance(rate, (int, float))
                             or rate <= 0):
        err(f"engagement-config.json: day_rate must be a positive number, "
            f"got {rate!r}")
    accent = cfg.get("accentColor")
    if accent and not re.fullmatch(r"#[0-9A-Fa-f]{6}", str(accent)):
        warn(f"engagement-config.json: accentColor '{accent}' is not #RRGGBB")
    if not ERRORS:
        ok("engagement-config.json: fields valid")
    return cfg


# ---------------------------------------------------------- engagements.csv

def check_csv(clients_dir: Path, client: Path,
              config: dict | None) -> str | None:
    """Validate 03-clients/engagements.csv; return this slug's stage."""
    path = clients_dir / "engagements.csv"
    if not path.exists():
        err("03-clients/engagements.csv missing — it is the single source "
            "of truth for engagement stage")
        return None
    with path.open(newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))
    if not rows or rows[0] != CSV_HEADER:
        err("engagements.csv: header must be exactly: " + ",".join(CSV_HEADER))
        return None
    slugs: set[str] = set()
    mine: dict[str, str] | None = None
    for lineno, row in enumerate(rows[1:], start=2):
        if not any(cell.strip() for cell in row):
            continue
        if len(row) != len(CSV_HEADER):
            err(f"engagements.csv line {lineno}: {len(row)} field(s), "
                f"expected {len(CSV_HEADER)}")
            continue
        rec = dict(zip(CSV_HEADER, row))
        slug = rec["slug"]
        if slug in slugs:
            err(f"engagements.csv: duplicate slug '{slug}'")
        slugs.add(slug)
        if rec["stage"] not in STAGES:
            err(f"engagements.csv {slug}: unknown stage '{rec['stage']}' "
                f"(expected one of {'|'.join(STAGES)})")
        if not DATE_RE.match(rec["last_updated"]):
            err(f"engagements.csv {slug}: last_updated "
                f"'{rec['last_updated']}' is not YYYY-MM-DD")
        if rec["language"] and rec["language"] not in LANGUAGES:
            warn(f"engagements.csv {slug}: language '{rec['language']}' "
                 f"is not nl|en")
        if slug == client.name:
            mine = rec
    if client.name == "_template":
        ok("engagements.csv: header valid (template workspace — no row "
           "required)")
        return None
    if mine is None:
        err(f"engagements.csv: no row for '{client.name}' — add one "
            f"(stage is tracked there, not in the workspace)")
        return None
    stage = mine["stage"] if mine["stage"] in STAGES else None
    if config:
        cfg_deps = {d for d in (config.get("departments") or [])
                    if isinstance(d, int)}
        csv_deps = {int(n) for n in
                    re.findall(r"\d+", mine["departments_in_scope"])}
        if cfg_deps != csv_deps:
            warn(f"engagements.csv {client.name}: departments_in_scope "
                 f"{sorted(csv_deps)} differs from engagement-config.json "
                 f"{sorted(cfg_deps)}")
        if (mine["language"] and config.get("language")
                and mine["language"] != config["language"]):
            warn(f"engagements.csv {client.name}: language "
                 f"'{mine['language']}' differs from engagement-config.json "
                 f"'{config['language']}'")
    ok(f"engagements.csv: row found — stage '{mine['stage']}'")
    return stage


# -------------------------------------------------------------- departments

def check_pains(dept_dir: Path, cat: dict | None) -> dict[str, str]:
    """Validate pains.md; return {PAIN-id: block}."""
    label = f"departments/{dept_dir.name}"
    path = dept_dir / "pains.md"
    if not path.exists():
        warn(f"{label}: no pains.md yet")
        return {}
    pains: dict[str, str] = {}
    for pid, block in split_blocks(read_md(path), r"PAIN-\d+"):
        if pid in pains:
            err(f"{label}/pains.md: duplicate block id {pid}")
            continue
        pains[pid] = block
        ptype = field(block, "Type")
        if ptype not in PAIN_TYPES:
            err(f"{label}/pains.md {pid}: Type '{ptype}' not in "
                f"{'|'.join(sorted(PAIN_TYPES))}")
        sev = field(block, "Severity")
        if sev not in PAIN_SEVERITIES:
            err(f"{label}/pains.md {pid}: Severity '{sev}' not in "
                f"minor|major|critical")
        procs = field(block, "Processen")
        if not procs:
            warn(f"{label}/pains.md {pid}: no Processen mapping to catalog "
                 f"codes")
        elif cat:
            for code in CODE_RE.findall(procs):
                if code not in cat["codes"]:
                    err(f"{label}/pains.md {pid}: process code {code} not "
                        f"in catalog")
        if not field(block, "Citaat"):
            warn(f"{label}/pains.md {pid}: no literal client quote (Citaat)")
        if not field(block, "Bron"):
            warn(f"{label}/pains.md {pid}: no source citation (Bron)")
    return pains


def check_content(dept_dir: Path, number: int, cat: dict | None,
                  pain_ids: set[str],
                  stage_idx: int | None) -> tuple[bool, set[str]]:
    """Validate content/NN-*.md; return (approved, referenced PAIN ids)."""
    label = f"departments/{dept_dir.name}"
    files = sorted((dept_dir / "content").glob("[0-9][0-9]-*.md"))
    if not files:
        msg = (f"{label}: no content/{number:02d}-<dept>.md AS-IS "
               f"documentation yet")
        if stage_idx is not None and stage_idx >= STAGE_IDX["asis-review"]:
            err(msg)
        else:
            warn(msg)
        return False, set()
    approved = True
    referenced: set[str] = set()
    for f in files:
        text = read_md(f)
        rel = f"{label}/content/{f.name}"
        status, reviewed = header_status(text)
        if status is None:
            err(f"{rel}: missing status header table "
                f"(| Client | Afdeling | Status | Laatst gereviewd |)")
            approved = False
        elif status not in CONTENT_STATUSES:
            err(f"{rel}: Status '{status}' not in "
                f"draft|consultant-review|client-review|approved")
            approved = False
        elif status != "approved":
            approved = False
        if reviewed and not DATE_RE.match(reviewed):
            warn(f"{rel}: 'Laatst gereviewd' '{reviewed}' is not YYYY-MM-DD")
        seen: set[str] = set()
        blocks = split_blocks(text, r"[A-Z]{2,5}\.\d{3}")
        if not blocks:
            warn(f"{rel}: no '## <CODE>' AS-IS blocks yet")
        for code, block in blocks:
            if code in seen:
                err(f"{rel}: duplicate block {code}")
            seen.add(code)
            if cat:
                if code not in cat["codes"]:
                    err(f"{rel} {code}: process code not in catalog")
                elif cat["code_dept"].get(code) != number:
                    warn(f"{rel} {code}: catalog assigns this code to "
                         f"department {cat['code_dept'].get(code)}, folder "
                         f"is {number}")
            sev = field(block, "Severity")
            if sev is None:
                warn(f"{rel} {code}: no Severity (drives the flow color)")
            elif sev not in BLOCK_SEVERITIES:
                err(f"{rel} {code}: Severity '{sev}' not in "
                    f"none|minor|major|critical")
            auto = field(block, "Automability")
            if auto is None:
                warn(f"{rel} {code}: no Automability (F4 first look)")
            elif auto not in AUTOMABILITIES:
                err(f"{rel} {code}: Automability '{auto}' not in "
                    f"human|automation|agent|hybrid")
            for ref in PAIN_RE.findall(field(block, "Pijn") or ""):
                referenced.add(ref)
                if ref not in pain_ids:
                    err(f"{rel} {code}: {ref} does not resolve to a block "
                        f"in {label}/pains.md")
    return approved, referenced


def check_flow(path: Path, number: int, cat: dict | None) -> None:
    rel = f"departments/{path.parent.parent.name}/flows/{path.name}"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        err(f"{rel}: invalid JSON ({e})")
        return
    for key in ("id", "title", "lanes", "nodes", "flows"):
        if key not in data:
            err(f"{rel}: required key '{key}' missing")
    if "domain" not in data:
        err(f"{rel}: required key 'domain' missing")
    elif data["domain"] != number:
        warn(f"{rel}: domain {data['domain']} differs from department "
             f"folder number {number} — it will not override the standard "
             f"flow for this department")
    lanes = {ln.get("id") for ln in data.get("lanes", [])
             if isinstance(ln, dict)}
    node_ids: set[str] = set()
    for node in data.get("nodes", []):
        nid = node.get("id")
        if not nid:
            err(f"{rel}: node without id")
            continue
        if nid in node_ids:
            err(f"{rel}: duplicate node id '{nid}'")
        node_ids.add(nid)
        if node.get("type") not in NODE_TYPES:
            err(f"{rel} node '{nid}': type '{node.get('type')}' not in "
                f"{'|'.join(sorted(NODE_TYPES))}")
        if not node.get("label"):
            warn(f"{rel} node '{nid}': no label")
        lane = node.get("lane")
        if lane and lane not in lanes:
            err(f"{rel} node '{nid}': lane '{lane}' not defined in lanes")
        proc = node.get("process")
        if proc and cat and proc not in cat["codes"]:
            err(f"{rel} node '{nid}': process code {proc} not in catalog")
    for i, fl in enumerate(data.get("flows", [])):
        for side in ("from", "to"):
            if fl.get(side) not in node_ids:
                err(f"{rel} flow #{i + 1}: '{side}' target "
                    f"'{fl.get(side)}' is not a node id")
    if len(node_ids) > 20:
        warn(f"{rel}: {len(node_ids)} nodes — keep flows at 10-20, split "
             f"into a subprocess + goto")


def check_coverage(dept_dir: Path) -> None:
    label = f"departments/{dept_dir.name}"
    path = dept_dir / "coverage.md"
    if not path.exists():
        warn(f"{label}: no coverage.md — every catalog process needs a "
             f"scope decision")
        return
    rows = [ln for ln in read_md(path).splitlines()
            if ln.strip().startswith("|")
            and not SEPARATOR_ROW_RE.match(ln.strip())
            and not re.match(r"^\|\s*Code\s*\|", ln.strip(), re.I)]
    if not rows:
        warn(f"{label}: coverage.md has no scope rows yet")


def check_departments(client: Path, config: dict | None, cat: dict | None,
                      stage_idx: int | None
                      ) -> tuple[dict[str, int], list[str]]:
    """All in-scope department workspaces.
    Returns ({PAIN-id: #depts defining it}, [unapproved dept labels])."""
    in_scope = [d for d in ((config or {}).get("departments") or [])
                if isinstance(d, int) and not isinstance(d, bool)]
    ddir = client / "departments"
    pain_counts: dict[str, int] = {}
    unapproved: list[str] = []
    # unexpected NN-* folders (folders starting with '_' are examples)
    known = set()
    if ddir.is_dir():
        for sub in sorted(p for p in ddir.iterdir() if p.is_dir()):
            m = DEPT_DIR_RE.match(sub.name)
            if not m:
                continue
            n = int(m.group(1))
            known.add(sub.name)
            if n not in in_scope:
                warn(f"departments/{sub.name}: department {n} is not in "
                     f"engagement-config.json scope")
    is_template = client.name == "_template"
    for n in in_scope:
        if cat and n not in cat["numbers"]:
            err(f"engagement-config.json: department {n} does not exist in "
                f"the catalog")
        hits = sorted(ddir.glob(f"{n:02d}-*")) if ddir.is_dir() else []
        hits = [h for h in hits if h.is_dir()]
        if not hits:
            if is_template:
                # placeholder scope — workspaces are created on copy
                unapproved.append(f"{n:02d}-?")
                continue
            msg = (f"department {n} in scope but no "
                   f"departments/{n:02d}-<dept>/ workspace yet")
            if stage_idx is not None and stage_idx >= STAGE_IDX["asis-review"]:
                err(msg)
            else:
                warn(msg)
            unapproved.append(f"{n:02d}-?")
            continue
        for dept_dir in hits:
            pains = check_pains(dept_dir, cat)
            for pid in pains:
                pain_counts[pid] = pain_counts.get(pid, 0) + 1
            approved, referenced = check_content(
                dept_dir, n, cat, set(pains), stage_idx)
            if not approved:
                unapproved.append(dept_dir.name)
            orphans = sorted(set(pains) - referenced)
            if orphans:
                warn(f"departments/{dept_dir.name}: pain(s) not linked from "
                     f"any content block: {', '.join(orphans)}")
            check_coverage(dept_dir)
            flows_dir = dept_dir / "flows"
            if flows_dir.is_dir():
                for f in sorted(flows_dir.glob("*.process.json")):
                    check_flow(f, n, cat)
            if approved:
                ok(f"departments/{dept_dir.name}: AS-IS approved, "
                   f"{len(pains)} pain(s)")
    return pain_counts, unapproved


# ------------------------------------------------------------- assumptions

def check_assumptions(client: Path) -> set[str] | None:
    """Return the set of assumption ids, or None when the file is absent."""
    path = client / "analysis" / "assumptions.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        err(f"analysis/assumptions.json: invalid JSON ({e})")
        return set()
    items = data.get("assumptions")
    if not isinstance(items, list):
        err("analysis/assumptions.json: top-level 'assumptions' must be "
            "a list")
        return set()
    ids: set[str] = set()
    for i, a in enumerate(items, start=1):
        if not isinstance(a, dict):
            err(f"analysis/assumptions.json #{i}: entry is not an object")
            continue
        aid = a.get("id")
        name = aid or f"#{i}"
        if not aid or not ID_RE.match(str(aid)):
            err(f"analysis/assumptions.json {name}: id must be lowercase "
                f"snake_case")
        elif aid in ids:
            err(f"analysis/assumptions.json: duplicate id '{aid}'")
        else:
            ids.add(aid)
        nums = {}
        for key in ("min", "max", "default"):
            v = a.get(key)
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                err(f"analysis/assumptions.json {name}: '{key}' missing or "
                    f"not a number")
            else:
                nums[key] = v
        if len(nums) == 3 and not (nums["min"] <= nums["default"]
                                   <= nums["max"]):
            err(f"analysis/assumptions.json {name}: expected "
                f"min <= default <= max, got {nums['min']} / "
                f"{nums['default']} / {nums['max']}")
        step = a.get("step")
        if step is not None and (isinstance(step, bool)
                                 or not isinstance(step, (int, float))
                                 or step <= 0):
            err(f"analysis/assumptions.json {name}: step must be a positive "
                f"number")
        if not a.get("label"):
            warn(f"analysis/assumptions.json {name}: no label")
        if not a.get("source"):
            warn(f"analysis/assumptions.json {name}: no calibration source")
    return ids


# ----------------------------------------------------------- opportunities

def check_formula(oid: str, formula: str,
                  assumption_ids: set[str] | None) -> None:
    for m in FORMULA_TOKEN_RE.finditer(formula):
        tok = m.group(0)
        if re.fullmatch(r"\d+(?:\.\d+)?", tok) or tok in "+-*/()":
            continue
        if ID_RE.match(tok):
            if assumption_ids is None:
                err(f"{oid}: Waardeformule uses '{tok}' but "
                    f"analysis/assumptions.json is missing")
            elif tok not in assumption_ids:
                err(f"{oid}: Waardeformule token '{tok}' is not an "
                    f"assumption id in assumptions.json")
        else:
            err(f"{oid}: Waardeformule contains invalid token '{tok}' "
                f"(allowed: assumption ids, numbers, + - * / parentheses)")


def expected_verdict(value: float, feasibility: float) -> str:
    high_v, high_f = value >= 3.5, feasibility >= 3.5
    if high_v and high_f:
        return "quick-win"
    if high_v:
        return "big-bet"
    if high_f:
        return "fill-in"
    return "discard"


def check_opportunities(client: Path, cat: dict | None, config: dict | None,
                        pain_counts: dict[str, int],
                        assumption_ids: set[str] | None,
                        stage_idx: int | None) -> list[str]:
    """Validate analysis/opportunities.md; return the OPP statuses found."""
    path = client / "analysis" / "opportunities.md"
    if not path.exists():
        if stage_idx is not None and stage_idx >= STAGE_IDX["proposal"]:
            err("analysis/opportunities.md missing while stage is at/past "
                "'proposal'")
        elif stage_idx is not None and stage_idx >= STAGE_IDX["diagnosis"]:
            warn("analysis/opportunities.md not written yet (stage "
                 "'diagnosis')")
        return []
    text = read_md(path)
    blocks = split_blocks(text, r"OPP-\d+")
    in_scope = {d for d in ((config or {}).get("departments") or [])
                if isinstance(d, int)}
    statuses: list[str] = []
    seen: set[str] = set()
    for oid, block in blocks:
        if oid in seen:
            err(f"opportunities.md: duplicate block id {oid}")
            continue
        seen.add(oid)
        status = field(block, "Status")
        if status not in OPP_STATUSES:
            err(f"{oid}: Status '{status}' not in "
                f"proposed|confirmed|deferred|discarded")
            status = None
        else:
            statuses.append(status)
        alloc = field(block, "Allocatie")
        if alloc is None:
            warn(f"{oid}: no Allocatie (F4) — needed for the cost model")
        elif alloc not in ALLOCATIONS:
            err(f"{oid}: Allocatie '{alloc}' not in "
                f"automation|agent-T1|agent-T2|agent-T3|hybrid")
        effort = field(block, "Effort")
        if effort is None:
            warn(f"{oid}: no Effort — needed for the cost model")
        elif effort not in EFFORTS:
            err(f"{oid}: Effort '{effort}' not in S|M|L")
        wave = field(block, "Wave")
        if wave is None:
            warn(f"{oid}: no Wave")
        elif wave not in WAVES:
            err(f"{oid}: Wave '{wave}' not in 1|2|3|-")
        if status == "discarded" and wave not in (None, "-"):
            warn(f"{oid}: discarded but Wave is '{wave}' (use '-')")
        # scores
        vs = parse_scores(field(block, "Value-scores") or "")
        fs = parse_scores(field(block, "Feasibility-scores") or "")
        for group, keys, got in (("Value-scores",
                                  ("hours", "quality", "strategic"), vs),
                                 ("Feasibility-scores",
                                  ("data", "technical", "ownership"), fs)):
            for k in keys:
                if k not in got:
                    err(f"{oid}: {group} missing '{k}'")
                elif not 1 <= got[k] <= 5:
                    err(f"{oid}: {group} {k}={got[k]:g} out of range 1-5")
        adopt = as_number(field(block, "Adoptie"))
        if adopt is None:
            warn(f"{oid}: no Adoptie score (F3 tie-break)")
        elif not 1 <= adopt <= 5:
            err(f"{oid}: Adoptie {adopt:g} out of range 1-5")
        # verdict vs computed quadrant
        verdict_raw = field(block, "Verdict") or ""
        vm = re.match(r"([a-z][a-z\-]*)", verdict_raw)
        verdict = vm.group(1) if vm else None
        if verdict not in VERDICTS:
            err(f"{oid}: Verdict '{verdict_raw}' must start with "
                f"quick-win|big-bet|fill-in|discard")
        elif all(k in vs for k in ("hours", "quality", "strategic")) and \
                all(k in fs for k in ("data", "technical", "ownership")):
            value = round(0.50 * vs["hours"] + 0.25 * vs["quality"]
                          + 0.25 * vs["strategic"], 2)
            feas = round(0.40 * fs["data"] + 0.30 * fs["technical"]
                         + 0.30 * fs["ownership"], 2)
            expect = expected_verdict(value, feas)
            if verdict != expect:
                err(f"{oid}: Verdict '{verdict}' does not match computed "
                    f"quadrant '{expect}' (Value={value:g}, "
                    f"Feasibility={feas:g}, high >= 3.5)")
        if "confidence" not in verdict_raw:
            warn(f"{oid}: Verdict carries no confidence")
        if not field(block, "Wat dit zou veranderen"):
            warn(f"{oid}: no 'Wat dit zou veranderen' — every verdict must "
                 f"be falsifiable")
        # references
        for ref in PAIN_RE.findall(field(block, "Pijnpunten") or ""):
            n = pain_counts.get(ref, 0)
            if n == 0:
                err(f"{oid}: {ref} does not exist in any in-scope "
                    f"department's pains.md")
            elif n > 1:
                warn(f"{oid}: {ref} exists in {n} departments — reference "
                     f"is ambiguous")
        if cat:
            for code in CODE_RE.findall(field(block, "Processen") or ""):
                if code not in cat["codes"]:
                    err(f"{oid}: process code {code} not in catalog")
                elif in_scope and cat["code_dept"].get(code) not in in_scope:
                    warn(f"{oid}: process {code} belongs to department "
                         f"{cat['code_dept'].get(code)}, which is not in "
                         f"scope")
            depts = field(block, "Afdelingen") or ""
            for prefix in re.findall(r"\b[A-Z]{2,5}\b", depts):
                if prefix not in cat["prefixes"]:
                    err(f"{oid}: Afdelingen prefix '{prefix}' not in catalog")
        # formula
        formula = field(block, "Waardeformule")
        if formula:
            check_formula(oid, formula, assumption_ids)
        elif wave in ("1", "2", "3"):
            err(f"{oid}: Wave {wave} but no Waardeformule — every OPP that "
                f"carries a EUR value needs one (discards may omit it)")
        if status != "discarded" and not field(block, "Eerste stap"):
            warn(f"{oid}: no 'Eerste stap'")
    if blocks:
        ok(f"opportunities.md: {len(seen)} OPP block(s) checked")
        if assumption_ids is not None and not 4 <= len(assumption_ids) <= 8:
            warn(f"assumptions.json: {len(assumption_ids)} slider(s) — the "
                 f"assumption model should have 4-8")
    return statuses


# ------------------------------------------------------------------- gates

def check_gates(client: Path, stage: str | None, unapproved: list[str],
                opp_statuses: list[str], has_opps: bool) -> None:
    stage_idx = STAGE_IDX.get(stage) if stage else None
    if has_opps and unapproved and \
            (stage_idx is None or stage_idx < STAGE_IDX["diagnosis"]):
        err(f"opportunities present but in-scope department(s) not approved: "
            f"{', '.join(unapproved)} — no diagnosis before AS-IS approval")
    if stage_idx is None:
        return
    if stage_idx >= STAGE_IDX["diagnosis"] and unapproved:
        err(f"stage '{stage}' requires every in-scope department's content "
            f"Status: approved; not approved: {', '.join(unapproved)}")
    if stage_idx >= STAGE_IDX["confirmed"]:
        if not (client / "proposal" / "decision-log.md").exists():
            err(f"stage '{stage}' requires proposal/decision-log.md")
        if "confirmed" not in opp_statuses:
            err(f"stage '{stage}' requires at least one OPP with "
                f"Status: confirmed")


# -------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Mechanical validator for one Roadmap Engine engagement "
                    "workspace (07-roadmap-engine/README.md is the spec).")
    ap.add_argument("client", help="path to 03-clients/<slug>")
    ap.add_argument("--strict", action="store_true",
                    help="warnings also fail (exit 2)")
    args = ap.parse_args()
    client = Path(args.client).resolve()
    if not client.is_dir():
        print(f"error: {client} is not a directory", file=sys.stderr)
        return 1
    clients_dir = client.parent

    print(f"check_engagement: {client.name}")
    config = check_config(client)
    stage = check_csv(clients_dir, client, config)
    stage_idx = STAGE_IDX.get(stage) if stage else None
    cat = load_catalog(clients_dir.parent)
    assumption_ids = check_assumptions(client)
    pain_counts, unapproved = check_departments(client, config, cat,
                                                stage_idx)
    opp_statuses = check_opportunities(client, cat, config, pain_counts,
                                       assumption_ids, stage_idx)
    has_opps = bool(opp_statuses) or bool(
        (client / "analysis" / "opportunities.md").exists()
        and split_blocks(read_md(client / "analysis" / "opportunities.md"),
                         r"OPP-\d+"))
    check_gates(client, stage, unapproved, opp_statuses, has_opps)

    print(f"result: {len(ERRORS)} error(s), {len(WARNS)} warning(s)")
    if ERRORS:
        return 1
    if WARNS and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
