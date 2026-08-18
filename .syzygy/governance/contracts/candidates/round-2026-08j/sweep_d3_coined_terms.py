#!/usr/bin/env python3
"""D3 coined-term sweep — every registered term, its first default-path use,
and its definition site.

Administration 1 (2026-08-18) returned D3 `Unknown` because the prescribed
enumeration — every coined term from `D3_POPULATION`, its first use on the
default path, and its definition site — was never reproduced as one
retained artifact. This sweep produces it.

Populations (the instrument's parameters):
  D3_POPULATION      the term registry (T-01…T-31 entries) plus the
                     doctrine glossary (doctrine/README.md §Glossary)
  DEFAULT_ROUTE_SET  README.md, AGENTS.md, .syzygy/intent/OVERVIEW.md,
                     PROJECT-STATUS.md, .syzygy/governance/doctrine/README.md,
                     .syzygy/governance/contracts/candidates/TASK-ROUTER.md

A term's "first use" is the first line containing it, scanning the route
set in the order listed (the reader's default order). Matching is a plain
case-sensitive phrase match: ordinary-word shadowing (Project, Evidence,
Claim, Unknown …) therefore OVER-reports use — the safe direction for this
question, since D3's failure mode is a term used before defined. Judging
whether a given hit is the coined sense or the ordinary word is the
reading step the report layer owns (CG-23 in check_governance.py is the
standing per-term companion measurement).

Usage: python3 sweep_d3_coined_terms.py [--repo PATH]
"""

import argparse
import re
from pathlib import Path

ROUTE_SET = (
    "README.md",
    "AGENTS.md",
    ".syzygy/intent/OVERVIEW.md",
    "PROJECT-STATUS.md",
    ".syzygy/governance/doctrine/README.md",
    ".syzygy/governance/contracts/candidates/TASK-ROUTER.md",
)
REGISTRY = (".syzygy/governance/contracts/candidates/policy-candidates/"
            "TERM-REGISTRY.md")
GLOSSARY = ".syzygy/governance/doctrine/README.md"

REG_ENTRY = re.compile(r"^#### (T-\d+) · (.+?)\s*$", re.M)
GLOS_ENTRY = re.compile(r"^- \*\*(.+?)\*\*", re.M)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None)
    args = ap.parse_args()
    repo = Path(args.repo) if args.repo else Path(__file__).resolve().parents[5]
    if not (repo / ".syzygy" / "governance").is_dir():
        raise SystemExit(f"not a syzygy repo root: {repo}")

    terms = []  # (term, definition site)
    reg = (repo / REGISTRY).read_text(encoding="utf-8")
    for tid, name in REG_ENTRY.findall(reg):
        terms.append((name.strip(), f"TERM-REGISTRY.md {tid} (candidate)"))
    glos = (repo / GLOSSARY).read_text(encoding="utf-8")
    glos_section = glos.split("## Glossary", 1)[1].split("\n## ", 1)[0]
    for raw in GLOS_ENTRY.findall(glos_section):
        # strip markup like `.syzygy/`, split slash-joined codenames
        # ("Polaris / Trajectory / Orrery") and and-joined pairs
        # ("`.syzygy/` and `openspec/`")
        parts = []
        for chunk in re.split(r"\s+and\s+", raw.replace("`", "")):
            parts.extend(re.split(r"\s*/\s+", chunk))
        for name in parts:
            name = name.strip(" *—-").rstrip("/")
            if name and not any(t == name for t, _ in terms):
                terms.append((name, "doctrine/README.md §Glossary (adopted)"))

    route_lines = []
    for rel in ROUTE_SET:
        body = (repo / rel).read_text(encoding="utf-8").splitlines()
        route_lines.extend((rel, i + 1, ln) for i, ln in enumerate(body))

    print("D3 coined-term sweep")
    print(f"population: {len(terms)} term(s) "
          f"(registry {len(REG_ENTRY.findall(reg))}, glossary remainder), "
          f"route set {len(ROUTE_SET)} file(s), {len(route_lines)} line(s)")
    print()
    print("| term | definition site | first default-path use |")
    print("|---|---|---|")
    unused = 0
    for term, site in terms:
        hit = next(((rel, n) for rel, n, ln in route_lines if term in ln), None)
        if hit:
            print(f"| {term} | {site} | `{hit[0]}:{hit[1]}` |")
        else:
            unused += 1
            print(f"| {term} | {site} | — not used on the default path |")
    print()
    print(f"{unused} term(s) never appear on the default path; "
          "counts computed by this script, never transcribed.")


if __name__ == "__main__":
    main()
