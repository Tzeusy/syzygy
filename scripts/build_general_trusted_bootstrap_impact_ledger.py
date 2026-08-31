#!/usr/bin/env python3
"""Build the complete generalized trusted-bootstrap impact ledger."""

from __future__ import annotations

import argparse
import collections
import io
import pathlib
import subprocess
import tarfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
BASELINE = "20e5b6e7c512436b67dec9eb05e0ee926096a7b5"
TERMS = (
    "RFC3-16(a)",
    "RFC3-16(c)",
    "provenance does not verify",
    "unverifiable provenance",
    "verifiable owner-act provenance",
    "state-(1)",
    "A1-mechanism act",
)
EXPECTED = {
    "RFC3-16(a)": 191,
    "RFC3-16(c)": 45,
    "provenance does not verify": 37,
    "unverifiable provenance": 6,
    "verifiable owner-act provenance": 19,
    "state-(1)": 22,
    "A1-mechanism act": 6,
}
EXPECTED_UNION = 204
OUT = ROOT / (
    ".syzygy/governance/contracts/candidates/"
    "general-trusted-bootstrap-authorization/IMPACT-LEDGER.md"
)

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
    prefix = BASELINE + ":"
    paths = {
        line.removeprefix(prefix)
        for line in output.splitlines()
        if line
    }
    unexpected = [line for line in output.splitlines() if not line.startswith(prefix)]
    if unexpected:
        raise ValueError(f"unexpected git grep row: {unexpected[0]}")
    if len(paths) != EXPECTED[term]:
        raise ValueError(f"{term}: {len(paths)} paths != expected {EXPECTED[term]}")
    return paths


def archive_populations() -> dict[str, set[str]]:
    """Read the baseline through a second, index-independent byte path."""
    archive = subprocess.run(
        ("git", "archive", "--format=tar", BASELINE),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    encoded = {term: term.encode() for term in TERMS}
    populations = {term: set() for term in TERMS}
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        for member in bundle.getmembers():
            if not member.isfile():
                continue
            extracted = bundle.extractfile(member)
            if extracted is None:
                continue
            body = extracted.read()
            for term, needle in encoded.items():
                if needle in body:
                    populations[term].add(member.name)
    return populations


def classify(path: str, changed: set[str]) -> tuple[str, str]:
    if path in changed:
        return (
            "edit",
            "candidate transaction edit or regenerated projection; exact bytes require transaction review",
        )
    if path in POST_ACT_EDITS:
        return (
            "post-act edit",
            "append the performed amendment act only after the owner ceremony; existing entries stay immutable",
        )

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
        "POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-SEMANTIC-DELTA.md",
    )
    if any(marker in path for marker in historical_markers) or path.endswith(
        historical_names
    ):
        return (
            "no impact",
            "historical, raw-review, performed-act, or superseded candidate evidence; never rewritten to current semantics",
        )

    if path.startswith("openspec/changes/"):
        return (
            "re-review",
            "signed behavior may remain deliberately stricter or citation-only, but must be checked against the amended contract",
        )
    if path.startswith("packages/"):
        return (
            "re-review",
            "implementation remains under its signed lower-level specification until a separately signed amendment authorizes change",
        )
    if path.startswith(".syzygy/governance/contracts/rfcs/"):
        return (
            "re-review",
            "accepted contract citation remains valid; direct semantic owners are edited in the amendment set",
        )
    if path.startswith(".syzygy/governance/contracts/candidates/rfcs/"):
        return (
            "re-review",
            "candidate-mirror citation remains valid; direct semantic owners are edited in the amendment set",
        )
    return (
        "re-review",
        "current artifact was inspected for reliance on the retired A1-only effect rule",
    )


def render() -> str:
    populations = {term: paths_for(term) for term in TERMS}
    archive_sets = archive_populations()
    for term in TERMS:
        if archive_sets[term] != populations[term]:
            missing = sorted(populations[term] - archive_sets[term])
            extra = sorted(archive_sets[term] - populations[term])
            raise ValueError(
                f"{term}: git-grep/archive disagreement; "
                f"archive_missing={missing}, archive_extra={extra}"
            )
    union = sorted(set().union(*populations.values()))
    if len(union) != EXPECTED_UNION:
        raise ValueError(f"union: {len(union)} paths != expected {EXPECTED_UNION}")
    changed = set(run("git", "diff", "--name-only", BASELINE, "--").splitlines())

    rows = []
    counts: collections.Counter[str] = collections.Counter()
    for path in union:
        disposition, reason = classify(path, changed)
        counts[disposition] += 1
        cited = ", ".join(term for term in TERMS if path in populations[term])
        rows.append((path, cited, disposition, reason))

    lines = [
        "# General trusted-bootstrap authorization impact ledger",
        "",
        "> **Generated evidence — not authority.** Every file in the seven baseline",
        "> text populations is classified exactly once. `git grep` path sets are",
        "> independently reproduced from a `git archive` byte sweep. Regenerate with",
        "> `python3 scripts/build_general_trusted_bootstrap_impact_ledger.py`.",
        "",
        f"Baseline: `{BASELINE}`",
        "",
        "## Denominators",
        "",
        "| Baseline text | Files |",
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
            f"| post-act edit | {counts['post-act edit']} |",
            f"| re-review | {counts['re-review']} |",
            f"| no impact | {counts['no impact']} |",
            f"| **Total** | **{len(union)}** |",
            "",
            "A `post-act edit` is deliberately absent from the candidate bytes: the",
            "performed owner act is appended only after the exact manifest ceremony.",
            "",
            "## Complete ledger",
            "",
            "| Path | Baseline matches | Disposition | Reason |",
            "|---|---|---|---|",
        ]
    )
    for path, cited, disposition, reason in rows:
        lines.append(f"| `{path}` | {cited} | {disposition} | {reason} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = render()
    if args.check:
        if not OUT.exists() or OUT.read_text() != output:
            print(f"DRIFT: {OUT.relative_to(ROOT)}")
            return 1
        print(
            "impact ledger current — "
            f"{OUT.relative_to(ROOT)}; {EXPECTED_UNION} baseline files"
        )
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output)
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
