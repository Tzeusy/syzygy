#!/usr/bin/env python3
"""Build the complete generalized trusted-bootstrap impact ledger."""

from __future__ import annotations

import argparse
import collections
import hashlib
import io
import pathlib
import re
import shutil
import subprocess
import tarfile
import tempfile


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
OUT_REL = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "general-trusted-bootstrap-authorization/IMPACT-LEDGER.md"
)
OUT = ROOT / OUT_REL
TRANSACTION_MANIFEST_REL = OUT_REL.with_name("TRANSACTION-MANIFEST.txt")
ACT_REL = pathlib.Path(
    ".syzygy/governance/decisions/"
    "GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md"
)
AGGREGATE_ACT_REL = pathlib.Path(
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
)
ACT_LABEL = "SIGN OFF GENERAL TRUSTED-BOOTSTRAP AUTHORIZATION TRANSACTION"
ACT_PATTERN = re.compile(
    r"^" + re.escape(ACT_LABEL) + r": ([0-9a-f]{64})$", re.M
)

POST_ACT_EDITS = {
    ".syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md",
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md",
}


def run_command(root: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        args,
        cwd=root,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout


def paths_for(term: str, root: pathlib.Path = ROOT) -> set[str]:
    output = run_command(root, "git", "grep", "-l", "-F", term, BASELINE, "--")
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


def archive_populations(root: pathlib.Path = ROOT) -> dict[str, set[str]]:
    """Read the baseline through a second, index-independent byte path."""
    archive = subprocess.run(
        ("git", "archive", "--format=tar", BASELINE),
        cwd=root,
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


def baseline_populations(root: pathlib.Path = ROOT) -> dict[str, set[str]]:
    """Reproduce the seven frozen baseline path sets by two byte paths."""
    populations = {term: paths_for(term, root) for term in TERMS}
    archive_sets = archive_populations(root)
    for term in TERMS:
        if archive_sets[term] != populations[term]:
            missing = sorted(populations[term] - archive_sets[term])
            extra = sorted(archive_sets[term] - populations[term])
            raise ValueError(
                f"{term}: git-grep/archive disagreement; "
                f"archive_missing={missing}, archive_extra={extra}"
            )
    union = set().union(*populations.values())
    if len(union) != EXPECTED_UNION:
        raise ValueError(f"union: {len(union)} paths != expected {EXPECTED_UNION}")
    return populations


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record_digest(root: pathlib.Path, rel: pathlib.Path) -> str | None:
    record = root / rel
    if not record.is_file():
        return None
    matches = ACT_PATTERN.findall(record.read_text())
    if not matches:
        return None
    if len(set(matches)) != 1:
        raise ValueError(f"{rel}: conflicting performed transaction digests")
    return matches[-1]


def performed_digest(root: pathlib.Path) -> str | None:
    dedicated = record_digest(root, ACT_REL)
    aggregate = record_digest(root, AGGREGATE_ACT_REL)
    if dedicated is None and aggregate is None:
        return None
    if dedicated is None or aggregate is None:
        missing = ACT_REL if dedicated is None else AGGREGATE_ACT_REL
        raise ValueError(
            f"conflicting post-act state: performed signal missing from {missing}"
        )
    if dedicated != aggregate:
        raise ValueError(
            f"conflicting performed digests: {ACT_REL}={dedicated}, "
            f"{AGGREGATE_ACT_REL}={aggregate}"
        )
    return dedicated


def transaction_subject_digest(root: pathlib.Path, subject: pathlib.Path) -> str:
    manifest = root / TRANSACTION_MANIFEST_REL
    if not manifest.is_file():
        raise ValueError(f"required transaction manifest missing: {TRANSACTION_MANIFEST_REL}")
    rows = []
    for line_no, line in enumerate(manifest.read_text().splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (\S.*)", line)
        if not match:
            raise ValueError(
                f"{TRANSACTION_MANIFEST_REL}:{line_no}: malformed digest row"
            )
        if match.group(2) == subject.as_posix():
            rows.append(match.group(1))
    if len(rows) != 1:
        raise ValueError(
            f"{TRANSACTION_MANIFEST_REL}: expected one row for {subject}, "
            f"found {len(rows)}"
        )
    return rows[0]


def validate_frozen_ledger(
    root: pathlib.Path, populations: dict[str, set[str]] | None = None
) -> None:
    """Verify the performed ledger without recomputing post-act dispositions."""
    act_digest = performed_digest(root)
    if act_digest is None:
        raise ValueError("general trusted-bootstrap transaction is not performed")
    transaction = root / TRANSACTION_MANIFEST_REL
    if not transaction.is_file():
        raise ValueError(f"required transaction manifest missing: {TRANSACTION_MANIFEST_REL}")
    current_transaction_digest = sha256_file(transaction)
    if act_digest != current_transaction_digest:
        raise ValueError(
            f"performed transaction digest {act_digest} != current manifest "
            f"{current_transaction_digest}"
        )

    ledger = root / OUT_REL
    if not ledger.is_file():
        raise ValueError(f"frozen impact ledger missing: {OUT_REL}")
    expected_ledger_digest = transaction_subject_digest(root, OUT_REL)
    actual_ledger_digest = sha256_file(ledger)
    if actual_ledger_digest != expected_ledger_digest:
        raise ValueError(
            f"frozen impact ledger digest {actual_ledger_digest} != transaction "
            f"row {expected_ledger_digest}"
        )

    populations = populations or baseline_populations(root)
    expected_union = set().union(*populations.values())
    body = ledger.read_text()
    marker = "## Complete ledger\n"
    if marker not in body:
        raise ValueError("frozen impact ledger has no complete-ledger section")
    complete = body.split(marker, 1)[1]
    row_pattern = re.compile(
        r"^\| `([^`]+)` \| (.*?) \| "
        r"(edit|post-act edit|re-review|no impact) \| (.+) \|$"
    )
    rows: dict[str, set[str]] = {}
    duplicates: set[str] = set()
    for line in complete.splitlines():
        match = row_pattern.match(line)
        if not match:
            continue
        path = match.group(1)
        if path in rows:
            duplicates.add(path)
        cited = {term.strip() for term in match.group(2).split(",") if term.strip()}
        rows[path] = cited
    if duplicates:
        raise ValueError(f"duplicate frozen ledger paths: {sorted(duplicates)}")
    actual_paths = set(rows)
    if actual_paths != expected_union:
        raise ValueError(
            "frozen ledger path set differs from baseline union; "
            f"missing={sorted(expected_union - actual_paths)}, "
            f"extra={sorted(actual_paths - expected_union)}"
        )
    for path in sorted(expected_union):
        expected_terms = {term for term in TERMS if path in populations[term]}
        if rows[path] != expected_terms:
            raise ValueError(
                f"{path}: frozen baseline memberships {sorted(rows[path])} != "
                f"expected {sorted(expected_terms)}"
            )

    for term in TERMS:
        match = re.search(
            rf"^\| `{re.escape(term)}` \| (\d+) \|$", body, re.M
        )
        if not match or int(match.group(1)) != len(populations[term]):
            raise ValueError(f"{term}: frozen denominator missing or incorrect")
    union_match = re.search(r"^Unique union: \*\*(\d+) files\*\*\.$", body, re.M)
    if not union_match or int(union_match.group(1)) != len(expected_union):
        raise ValueError("frozen unique-union denominator missing or incorrect")


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


def render(root: pathlib.Path = ROOT) -> str:
    populations = baseline_populations(root)
    union = sorted(set().union(*populations.values()))
    changed = set(
        run_command(root, "git", "diff", "--name-only", BASELINE, "--").splitlines()
    )

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


def execute(
    check: bool,
    root: pathlib.Path = ROOT,
    populations: dict[str, set[str]] | None = None,
) -> int:
    try:
        frozen = performed_digest(root)
    except ValueError as exc:
        print(f"DRIFT: post-act state — {exc}")
        return 1
    target = root / OUT_REL
    if frozen is not None:
        try:
            validate_frozen_ledger(root, populations=populations)
        except ValueError as exc:
            print(f"DRIFT: immutable performed impact ledger — {exc}")
            return 1
        if check:
            print(
                "performed impact ledger frozen and valid — "
                f"{OUT_REL}; {EXPECTED_UNION} baseline files"
            )
        else:
            print(
                "immutable performed impact ledger unchanged — rewrite refused; "
                f"{OUT_REL}"
            )
        return 0

    output = render(root)
    if check:
        if not target.exists() or target.read_text() != output:
            print(f"DRIFT: {OUT_REL}")
            return 1
        print(f"impact ledger current — {OUT_REL}; {EXPECTED_UNION} baseline files")
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output)
    print(f"wrote {OUT_REL}")
    return 0


def selftest() -> int:
    populations = baseline_populations(ROOT)
    checks = []
    with tempfile.TemporaryDirectory(prefix="general-bootstrap-impact-") as temp:
        clone = pathlib.Path(temp)
        for rel in (
            OUT_REL, TRANSACTION_MANIFEST_REL, ACT_REL, AGGREGATE_ACT_REL
        ):
            target = clone / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)

        before = (clone / OUT_REL).read_bytes()
        clean = execute(False, clone, populations=populations) == 0
        checks.append((
            "performed clean write mode is a no-op success",
            clean and (clone / OUT_REL).read_bytes() == before,
        ))

        (clone / ACT_REL).unlink()
        missing_dedicated = execute(False, clone, populations=populations) == 1
        checks.append((
            "missing dedicated act record fails closed",
            missing_dedicated and (clone / OUT_REL).read_bytes() == before,
        ))
        shutil.copy2(ROOT / ACT_REL, clone / ACT_REL)

        (clone / AGGREGATE_ACT_REL).unlink()
        missing_aggregate = execute(False, clone, populations=populations) == 1
        checks.append((
            "missing aggregate act record fails closed",
            missing_aggregate and (clone / OUT_REL).read_bytes() == before,
        ))
        shutil.copy2(ROOT / AGGREGATE_ACT_REL, clone / AGGREGATE_ACT_REL)

        mutation = before + b"\npost-act mutation\n"
        (clone / OUT_REL).write_bytes(mutation)
        refused = execute(False, clone, populations=populations) == 1
        checks.append((
            "performed drift is rejected without rewrite",
            refused and (clone / OUT_REL).read_bytes() == mutation,
        ))

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    failures = sum(not passed for _name, passed in checks)
    print(f"{len(checks)} impact freeze mutations, {failures} failing")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return execute(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
