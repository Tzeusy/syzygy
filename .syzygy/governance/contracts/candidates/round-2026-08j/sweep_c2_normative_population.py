#!/usr/bin/env python3
"""C2 population sweep — enumerate normative-modal lines and their owner class.

Administration 1 (2026-08-18) returned C2 `Unknown` because the full
population denominator was never reconstructed: which lines in the
normative corpus carry a normative modal, and what class of artifact owns
each. This sweep constructs that denominator, reproducibly.

Population (the instrument's `C2_POPULATION`): `README.md`, `AGENTS.md`,
and every `.md`/`.yaml` under `.syzygy/governance/`.

What it does NOT do: it does not judge whether two artifacts state the
same rule — that is the report's (and the next administrator's) reading
job, made tractable by this enumeration. A modal inside a quotation or a
code fence is still counted: over-counting is the safe direction for a
denominator (VIS-2 — never claim less than the sweep saw).

Usage: python3 sweep_c2_normative_population.py [--repo PATH]
Output: the report table on stdout; exit 0 always (it measures, decides
nothing).
"""

import argparse
import re
from pathlib import Path

MODAL = re.compile(
    r"\b(must(?:\s+not)?|shall(?:\s+not)?|never|may\s+not|required\s+to|"
    r"forbidden|should(?:\s+not)?|do\s+not|prohibi\w+)\b", re.IGNORECASE)

#: Owner classes, first match wins. The class names follow the authority
#: table in AGENTS.md / README.md; the conflict rule between classes is the
#: table itself plus each artifact's own "where X and Y disagree" banner.
CLASSES = (
    ("historical/frozen (round trees, history, launch-gate raw)",
     re.compile(r"round-2026-|/history/|-RAW\.|HISTORICAL|_bootstrap")),
    ("adopted doctrine", re.compile(r"governance/doctrine/")),
    ("owner-approved craft", re.compile(r"policies/craft-and-care/")),
    ("substrate lock (record)", re.compile(r"GOVERNANCE-SUBSTRATE-LOCK")),
    ("owner decisions and acts", re.compile(r"governance/decisions/")),
    ("accepted contracts (Waves A/B)", re.compile(r"contracts/rfcs/")),
    ("generated views (presentation, never authority)",
     re.compile(r"TASK-ROUTER|05-CONTRACT-INDEX|CONTEXT-BUDGET-REPORT|"
                r"CAPABILITY-1-GENERATED-VIEWS|ACTIVE-CONTRACT-MANIFEST|"
                r"04-DEPENDENCY-INDEX")),
    ("candidate contracts and policies", re.compile(r"contracts/candidates/")),
    ("map candidates", re.compile(r"map/topology-candidates/")),
    ("root operating docs (README/AGENTS)", re.compile(r"^(README|AGENTS)\.md$")),
    ("other governance records", re.compile(r".")),
)


def classify(rel):
    for name, rx in CLASSES:
        if rx.search(rel):
            return name
    return "unclassified"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None)
    args = ap.parse_args()
    repo = Path(args.repo) if args.repo else Path(__file__).resolve().parents[5]
    if not (repo / ".syzygy" / "governance").is_dir():
        raise SystemExit(f"not a syzygy repo root: {repo}")

    pop = [repo / "README.md", repo / "AGENTS.md"]
    gov = repo / ".syzygy" / "governance"
    pop += sorted(p for p in gov.rglob("*")
                  if p.is_file() and p.suffix in (".md", ".yaml"))

    per_class = {}
    total_files = total_lines = total_hits = 0
    for path in pop:
        rel = str(path.relative_to(repo))
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        total_files += 1
        total_lines += len(lines)
        hits = sum(1 for ln in lines if MODAL.search(ln))
        total_hits += hits
        cls = classify(rel)
        files, hsum = per_class.get(cls, (0, 0))
        per_class[cls] = (files + 1, hsum + hits)

    print("C2 normative-modal population sweep")
    print(f"population: {total_files} file(s), {total_lines} line(s); "
          f"{total_hits} line(s) carry a normative modal")
    print()
    print("| owner class | files | modal lines |")
    print("|---|---|---|")
    for name, _ in CLASSES:
        if name in per_class:
            f, h = per_class[name]
            print(f"| {name} | {f} | {h} |")
    print()
    print("counts computed by this script, never transcribed; "
          "re-run to reproduce.")


if __name__ == "__main__":
    main()
