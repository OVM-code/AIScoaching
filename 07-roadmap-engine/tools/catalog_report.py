#!/usr/bin/env python3
"""catalog_report.py — evidence report over the Roadmap Engine process catalog.

Per department: which processes carry engagement evidence (and how old it is),
which never got any, and which opportunity patterns were never confirmed by a
real engagement. Lightweight analog of the ERP catalog reconcile; the evidence
itself is written by /harvest-engagement (drafted, human-approved).

Evidence entry format (catalog/departments.json, per process, optional):
    "evidence":       ["<client-slug> <artifact-path> <YYYY-MM>[ (demo)]"]
    "last_validated": "YYYY-MM"        # absent = never validated (fine for seeds)
Demo workspaces (slug starting with "_") illustrate the convention but never
count as real evidence.

Usage:
    python3 07-roadmap-engine/tools/catalog_report.py [--strict]

--strict exits 1 if any evidence entry references a nonexistent client slug or
carries a malformed/missing date. Python stdlib only.
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent            # 07-roadmap-engine/
CATALOG = ENGINE / "catalog" / "departments.json"
DEPT_MD = ENGINE / "catalog" / "departments"
CLIENTS = ENGINE.parent / "03-clients"
STALE_MONTHS = 12

EVIDENCE_RE = re.compile(r"^(\S+)\s+(\S+)\s+(\d{4}-(?:0[1-9]|1[0-2]))(\s+\(demo\))?$")
MONTH_RE = re.compile(r"^\d{4}-(?:0[1-9]|1[0-2])$")


def months_ago(ym: str) -> int:
    today = datetime.date.today()
    y, m = int(ym[:4]), int(ym[5:7])
    return (today.year - y) * 12 + (today.month - m)


def patterned_codes(dept_file: str) -> set[str]:
    """Process codes whose catalog authoring page documents opportunity patterns."""
    path = DEPT_MD / (dept_file or "")
    if not path.is_file():
        return set()
    codes, current = set(), None
    for line in path.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^##\s+([A-Z][A-Z0-9]{1,4}\.\d{3})\b", line.strip())
        if h:
            current = h.group(1)
        elif current and re.search(r"\*\*Opportunity patterns?:?\*\*", line):
            codes.add(current)
    return codes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on bad client slugs or malformed dates in evidence")
    args = ap.parse_args()

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    problems: list[str] = []
    print(f"catalog evidence report — {CATALOG.relative_to(ENGINE.parent)}\n")

    for dept in catalog.get("departments", []):
        num = dept["number"]
        procs = [p for p in catalog.get("processes", []) if p.get("department") == num]
        patterns = patterned_codes(dept.get("file", ""))
        with_ev = [p for p in procs if p.get("evidence")]
        title = dept.get("title", {}).get("en") or dept.get("id", "")
        print(f"{num:02d} {title} ({dept.get('prefix', '?')}) — "
              f"{len(with_ev)}/{len(procs)} processes with evidence")

        for p in procs:
            code, real = p["code"], 0
            for entry in p.get("evidence", []):
                m = EVIDENCE_RE.match(entry)
                if not m:
                    problems.append(f"{code}: malformed evidence entry {entry!r} "
                                    "(expected '<slug> <artifact> <YYYY-MM>[ (demo)]')")
                    continue
                slug = m.group(1)
                if not (CLIENTS / slug).is_dir():
                    problems.append(f"{code}: evidence references unknown client slug '{slug}'")
                if not m.group(4):
                    real += 1
            if p.get("evidence"):
                lv = p.get("last_validated")
                if lv and not MONTH_RE.match(lv):
                    problems.append(f"{code}: malformed last_validated {lv!r} (expected YYYY-MM)")
                    lv = None
                age = f"validated {lv} ({months_ago(lv)} mo ago)" if lv else "no last_validated"
                stale = "  [STALE]" if lv and months_ago(lv) > STALE_MONTHS else ""
                demo = "" if real else "  [demo-only]"
                print(f"    {code}: {len(p['evidence'])} evidence entr"
                      f"{'y' if len(p['evidence']) == 1 else 'ies'}, {age}{demo}{stale}")

        without = [p["code"] for p in procs if not p.get("evidence")]
        if without:
            print(f"    without evidence: {', '.join(without)}")
        never = sorted(c for c in patterns
                       if not any(EVIDENCE_RE.match(e) and not EVIDENCE_RE.match(e).group(4)
                                  for p in procs if p["code"] == c
                                  for e in p.get("evidence", [])))
        if never:
            print(f"    opportunity patterns never confirmed: {', '.join(never)}")
        print()

    if problems:
        print(f"{len(problems)} problem(s):")
        for pr in problems:
            print(f"  ! {pr}")
        if args.strict:
            return 1
    else:
        print("evidence entries: all well-formed, all client slugs resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
