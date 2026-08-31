#!/usr/bin/env python3
"""Build the complete trusted-bootstrap citation impact ledger."""

from __future__ import annotations

import collections
import pathlib
import subprocess


ROOT = pathlib.Path(__file__).resolve().parents[1]
BASELINE = "3f5853004dad849815ea7a76909b24fddaef9632"
TERMS = ("RFC3-16(a)", "RFC3-16(c)", "RFC4-7", "RFC5-16", "PWB-REQ-005")
EXPECTED = {
    "RFC3-16(a)": 191,
    "RFC3-16(c)": 45,
    "RFC4-7": 35,
    "RFC5-16": 40,
    "PWB-REQ-005": 24,
}
OUT = ROOT / ".syzygy/governance/contracts/candidates/trusted-bootstrap-observation/IMPACT-LEDGER.md"

POST_ACT_EDITS = {
    ".syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md",
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md",
}


def run(*args: str) -> str:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout


def paths_for(term: str) -> set[str]:
    output = run("git", "grep", "-l", "-F", term, BASELINE, "--")
    paths = set()
    for line in output.splitlines():
        if not line:
            continue
        prefix = BASELINE + ":"
        if not line.startswith(prefix):
            raise ValueError(f"unexpected git grep row: {line}")
        paths.add(line[len(prefix) :])
    if len(paths) != EXPECTED[term]:
        raise ValueError(f"{term}: {len(paths)} paths != expected {EXPECTED[term]}")
    return paths


def classify(path: str, changed: set[str]) -> tuple[str, str]:
    if path in changed:
        return "edit", "candidate bytes or generated projection change in this transaction"
    if path in POST_ACT_EDITS:
        return "edit", "append/update only after the owner act; current historical bytes remain untouched pre-act"

    historical_markers = (
        "/history/",
        "/round-2026-",
        "/reviews/",
        "docs/reviews/",
        "docs/superpowers/",
    )
    historical_names = (
        "-RAW.md",
        "COMPACTION-REPORT.md",
        "COMPACTION-CHARTER.md",
        "LEAD-SWEEP-NOTES.md",
        "WORKER-REPORT-DIGEST.md",
        "POLARIS-POC-BOOTSTRAP-OBSERVATION-EXCEPTION-SEMANTIC-DELTA.md",
    )
    if any(marker in path for marker in historical_markers) or path.endswith(historical_names):
        return "no impact", "historical, raw-review or rejected diagnostic evidence; never edited to follow current semantics"

    if path.startswith(".syzygy/governance/contracts/rfcs/"):
        return "re-review", "accepted clause citation remains valid; non-observation effect keeps the A1 gate"
    if path.startswith(".syzygy/governance/contracts/candidates/rfcs/"):
        return "re-review", "candidate mirror citation remains valid; direct semantic owners are edited separately"
    if path.startswith("openspec/changes/project-registration-and-honest-shape-visibility/"):
        return "re-review", "Capability 1 behavior is outside the trusted-observation mode; no byte change required"
    if path.startswith("openspec/changes/three-surface-poc-experience/"):
        return "re-review", "original-slice behavior remains; its coverage scope artifact is edited separately"
    if path.startswith("openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/"):
        return "re-review", "pre-signoff audit input; signed normalized matrices and repair overlay own current dispositions"
    if path.startswith("packages/cap1-"):
        return "re-review", "Capability 1 runtime does not consume the PWB trusted-observation mode"
    if path.startswith(".syzygy/map/topology-candidates/"):
        return "re-review", "candidate topology still describes typed authority; no accepted placement changes"
    return "re-review", "citation inspected; no semantic assertion is invalidated by the read-only-only trust mode"


def render() -> str:
    populations = {term: paths_for(term) for term in TERMS}
    union = sorted(set().union(*populations.values()))
    changed = set(run("git", "diff", "--name-only", BASELINE, "--").splitlines())

    rows = []
    counts: collections.Counter[str] = collections.Counter()
    for path in union:
        classification, reason = classify(path, changed)
        counts[classification] += 1
        cited = ", ".join(term for term in TERMS if path in populations[term])
        rows.append((path, cited, classification, reason))

    lines = [
        "# Trusted-bootstrap observation citation impact ledger",
        "",
        "> **Generated evidence — not authority.** Every file in the five baseline",
        "> citation populations is classified exactly once. Regenerate with",
        "> `python3 scripts/build_trusted_bootstrap_impact_ledger.py`.",
        "",
        f"Baseline: `{BASELINE}`",
        "",
        "## Denominators",
        "",
        "| Identifier | Files |",
        "|---|---:|",
    ]
    lines.extend(f"| `{term}` | {len(populations[term])} |" for term in TERMS)
    lines.extend(
        [
            "",
            f"Unique union: **{len(union)} files**.",
            "",
            "## Dispositions",
            "",
            "| Disposition | Files |",
            "|---|---:|",
            f"| edit | {counts['edit']} |",
            f"| re-review | {counts['re-review']} |",
            f"| no impact | {counts['no impact']} |",
            f"| **Total** | **{len(union)}** |",
            "",
            "`edit` includes explicitly deferred post-act current-state/act-record",
            "updates; their pre-act bytes remain unchanged by design.",
            "",
            "## Complete ledger",
            "",
            "| Path | Citations | Disposition | Reason |",
            "|---|---|---|---|",
        ]
    )
    for path, cited, classification, reason in rows:
        lines.append(f"| `{path}` | {cited} | {classification} | {reason} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    output = render()
    if OUT.exists() and OUT.read_text() == output:
        print(f"impact ledger current — {OUT.relative_to(ROOT)}")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output)
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
