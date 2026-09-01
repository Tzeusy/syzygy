#!/usr/bin/env python3
"""Build and verify the exact eleven-artifact PWB state-(1) amendment manifest."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-state1-amendment"
)
OUT = CANDIDATE / "PWB-AMENDMENT-MANIFEST.txt"
SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "proposal.md",
            CHANGE / "design.md",
            CHANGE / "specs/polaris-project-wide-butlers-model/spec.md",
            CHANGE / "CAPABILITY-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CHANGE / "GOVERNING-DEPENDENCIES.md",
            CHANGE / "contract-coverage-matrix/RFC-0001-0003.md",
            CHANGE / "contract-coverage-matrix/RFC-0004-0006.md",
            CHANGE / "contract-coverage-matrix/RFC-0007-0009.md",
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.M)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def subject_bytes(
    root: pathlib.Path, overrides: dict[pathlib.Path, bytes] | None = None
) -> dict[pathlib.Path, bytes]:
    if len(SUBJECTS) != 11 or len(set(SUBJECTS)) != 11:
        raise ValueError("PWB amendment population must be 11 unique paths")
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in SUBJECTS:
        if rel in overrides:
            values[rel] = overrides[rel]
            continue
        target = root / rel
        if not target.is_file():
            raise ValueError(f"required PWB amendment subject missing: {rel}")
        values[rel] = target.read_bytes()
    return values


def render(
    root: pathlib.Path = ROOT,
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> str:
    values = subject_bytes(root, overrides)
    lines = [
        "# PWB STATE-(1) AMENDMENT MANIFEST",
        "# Candidate; binds nothing until the human owner signs this exact manifest digest.",
        "# 11 signed artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
    ]
    lines.extend(f"{digest(values[rel])}  {rel.as_posix()}" for rel in SUBJECTS)
    return "\n".join(lines) + "\n"


def verify(text: str, root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    rows = ROW_RE.findall(text)
    expected_paths = [path.as_posix() for path in SUBJECTS]
    actual_paths = [path for _, path in rows]
    if actual_paths != expected_paths:
        findings.append(
            "manifest paths differ from the exact ordered eleven-artifact population"
        )
        return findings
    for expected_digest, path in rows:
        target = root / path
        if not target.is_file():
            findings.append(f"manifest subject missing: {path}")
            continue
        actual_digest = digest(target.read_bytes())
        if actual_digest != expected_digest:
            findings.append(
                f"manifest digest mismatch: {path} {actual_digest} != {expected_digest}"
            )
    return findings


def selftest() -> int:
    first = render()
    second = render()
    if first != second:
        print("SELFTEST FAILED: manifest rendering is nondeterministic")
        return 1
    if verify(first):
        print("SELFTEST FAILED: rendered manifest does not verify")
        return 1

    proposal = CHANGE / "proposal.md"
    original = (ROOT / proposal).read_bytes()
    mutated = render(overrides={proposal: original + b"\nmutation\n"})
    if mutated == first:
        print("SELFTEST FAILED: subject-byte mutation did not change manifest")
        return 1
    before_rows = dict((path, sha) for sha, path in ROW_RE.findall(first))
    after_rows = dict((path, sha) for sha, path in ROW_RE.findall(mutated))
    changed = [path for path in before_rows if before_rows[path] != after_rows[path]]
    if changed != [proposal.as_posix()]:
        print(f"SELFTEST FAILED: mutation changed wrong rows: {changed}")
        return 1

    malformed = first.replace(f"  {SUBJECTS[0].as_posix()}\n", "  missing.md\n", 1)
    if not verify(malformed):
        print("SELFTEST FAILED: path mutation was not rejected")
        return 1

    print("selftest: 11-row population, determinism, byte mutation and path mutation hold")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    expected = render()
    target = ROOT / OUT
    if args.check:
        if not target.is_file():
            print(f"PWB amendment manifest missing: {OUT}")
            return 1
        actual = target.read_text()
        if actual != expected:
            print("PWB amendment manifest differs from regeneration")
            return 1
        findings = verify(actual)
        if findings:
            for finding in findings:
                print(f"FAILED: {finding}")
            return 1
        print("PWB amendment manifest matches regeneration — 11 artifacts")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(expected)
    print(f"wrote {OUT} — 11 artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
