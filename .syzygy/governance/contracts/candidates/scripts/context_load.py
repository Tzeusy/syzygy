#!/usr/bin/env python3
"""Measure a context-packet selection: word and token-estimate totals for a
set of governed artifacts. Used by the five context-selection fixtures so
their size claims are re-runnable from the delivered packet on any machine.
Review tooling only — not application code (directive §11).

Usage:
  context_load.py [--root DIR] PATH [PATH ...]

PATHs are relative to root (the final-prespec directory by default; paths
starting with 'doctrine:' or 'craft:' resolve against the repository's
canonical homes when present, else against packet copies under the given
root — whichever exists). Token estimate: words × 1.35 (stated heuristic,
not a tokenizer; the fixture's acceptance target uses the same heuristic
everywhere so comparisons are internally consistent).
"""
import argparse
import sys
from pathlib import Path

TOKENS_PER_WORD = 1.35

PREFIX_HOMES = {
    "doctrine:": [".syzygy/governance/doctrine", "doctrine"],
    "craft:": [".syzygy/governance/policies/craft-and-care", "craft-and-care"],
}


def resolve(root, spec):
    for prefix, homes in PREFIX_HOMES.items():
        if spec.startswith(prefix):
            name = spec[len(prefix):]
            # try repo-canonical home (walking up from root), then packet copy;
            # the chosen source is printed to stderr so a drifted-host run can
            # never silently swap sources under the same command
            for anc in [root, *root.parents]:
                cand = anc / homes[0] / name
                if cand.exists():
                    print(f"[source] {spec} -> {cand} (canonical home)",
                          file=sys.stderr)
                    return cand
            cand = root / homes[1] / name
            if cand.exists():
                print(f"[source] {spec} -> {cand} (packet copy)", file=sys.stderr)
                return cand
            return None
    cand = root / spec
    return cand if cand.exists() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("paths", nargs="+")
    args = ap.parse_args()
    root = args.root.resolve()
    total = 0
    rows = []
    missing = []
    for spec in args.paths:
        p = resolve(root, spec)
        if p is None:
            missing.append(spec)
            continue
        w = len(p.read_text(encoding="utf-8").split())
        rows.append((spec, w))
        total += w
    width = max(len(s) for s, _ in rows) if rows else 10
    for spec, w in rows:
        print(f"{w:>7}  {spec}")
    print(f"{'-' * 7}")
    print(f"{total:>7}  TOTAL words")
    print(f"{int(total * TOKENS_PER_WORD):>7}  estimated tokens (words × {TOKENS_PER_WORD})")
    if missing:
        print("\nMISSING (selection invalid until resolved):")
        for spec in missing:
            print(f"  ✗ {spec}")
        sys.exit(1)


if __name__ == "__main__":
    main()
