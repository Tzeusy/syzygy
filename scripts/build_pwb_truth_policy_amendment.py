#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB truth/policy amendment manifests.

This script performs no owner act and writes no act record. The eleven PWB
behavior artifacts form one indivisible subject. The policy and registry are
separate subjects because each requires its own effect-specific owner act.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-truth-policy-amendment"
)
BEHAVIOR_OUT = CANDIDATE / "PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt"
EFFECT_OUT = CANDIDATE / "PWB-EFFECT-AMENDMENT-MANIFEST.txt"

BEHAVIOR_SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "CAPABILITY-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CHANGE / "CONTRACT-COVERAGE.md",
            CHANGE / "GOVERNING-DEPENDENCIES.md",
            CHANGE / "contract-coverage-matrix/RFC-0001-0003.md",
            CHANGE / "contract-coverage-matrix/RFC-0004-0006.md",
            CHANGE / "contract-coverage-matrix/RFC-0007-0009.md",
            CHANGE / "design.md",
            CHANGE / "proposal.md",
            CHANGE / "specs/polaris-project-wide-butlers-model/spec.md",
        ),
        key=lambda path: path.as_posix(),
    )
)
EFFECT_SUBJECTS = tuple(
    sorted(
        (
            pathlib.Path(
                ".syzygy/governance/policies/"
                "POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"
            ),
            pathlib.Path(
                ".syzygy/governance/declarations/adapter-registry/"
                "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
            ),
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def subject_bytes(
    subjects: tuple[pathlib.Path, ...],
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in subjects:
        target = ROOT / rel
        if rel in overrides:
            values[rel] = overrides[rel]
        elif target.is_file():
            values[rel] = target.read_bytes()
        else:
            raise ValueError(f"missing amendment subject: {rel}")
    return values


def render(
    title: str,
    subjects: tuple[pathlib.Path, ...],
    indivisible: bool,
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> str:
    values = subject_bytes(subjects, overrides)
    effect = (
        "All rows take effect together or none do."
        if indivisible
        else "Each row requires its own separate owner act; neither row binds the other."
    )
    lines = [
        f"# {title}",
        "# Candidate; this file and its rows bind nothing by themselves.",
        f"# {len(subjects)} artifacts; rows sorted by codepoint path.",
        f"# {effect}",
    ]
    lines.extend(f"{sha256(values[rel])}  {rel.as_posix()}" for rel in subjects)
    return "\n".join(lines) + "\n"


def outputs(overrides: dict[pathlib.Path, bytes] | None = None) -> dict[pathlib.Path, str]:
    return {
        BEHAVIOR_OUT: render(
            "PWB TRUTH-AND-READINESS BEHAVIOR AMENDMENT MANIFEST",
            BEHAVIOR_SUBJECTS,
            True,
            overrides,
        ),
        EFFECT_OUT: render(
            "PWB POLICY-AND-REGISTRY EFFECT AMENDMENT MANIFEST",
            EFFECT_SUBJECTS,
            False,
            overrides,
        ),
    }


def verify_manifest(
    text: str, subjects: tuple[pathlib.Path, ...], expected: str
) -> list[str]:
    findings: list[str] = []
    rows = ROW.findall(text)
    expected_paths = [path.as_posix() for path in subjects]
    if [path for _digest, path in rows] != expected_paths:
        findings.append("manifest path population or order differs")
        return findings
    for digest, path in rows:
        target = ROOT / path
        if not target.is_file():
            findings.append(f"subject missing: {path}")
        elif sha256(target.read_bytes()) != digest:
            findings.append(f"subject digest mismatch: {path}")
    if text != expected:
        findings.append("manifest differs from exact regeneration")
    return findings


def check() -> list[str]:
    findings: list[str] = []
    for out, expected in outputs().items():
        target = ROOT / out
        if not target.is_file():
            findings.append(f"manifest missing: {out}")
            continue
        subjects = BEHAVIOR_SUBJECTS if out == BEHAVIOR_OUT else EFFECT_SUBJECTS
        findings.extend(f"{out}: {item}" for item in verify_manifest(target.read_text(), subjects, expected))
    return findings


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        print("SELFTEST FAILED: behavior population is not 11 unique paths")
        return 1
    if len(EFFECT_SUBJECTS) != 2 or len(set(EFFECT_SUBJECTS)) != 2:
        print("SELFTEST FAILED: effect population is not 2 unique paths")
        return 1
    first = BEHAVIOR_SUBJECTS[0]
    baseline = outputs()
    mutated = outputs({first: subject_bytes(BEHAVIOR_SUBJECTS)[first] + b"\nmutation\n"})
    if baseline[BEHAVIOR_OUT] == mutated[BEHAVIOR_OUT]:
        print("SELFTEST FAILED: subject-byte mutation did not change behavior manifest")
        return 1
    rows = ROW.findall(baseline[BEHAVIOR_OUT])
    reordered = baseline[BEHAVIOR_OUT].replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, BEHAVIOR_SUBJECTS, baseline[BEHAVIOR_OUT]):
        print("SELFTEST FAILED: path-order mutation passed")
        return 1
    print("selftest: closed populations, byte drift and path order fail closed")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.check:
        findings = check()
        if findings:
            print("PWB amendment manifests do not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print("PWB amendment manifests match 11 behavior and 2 separate effect subjects")
        return 0
    for rel, body in outputs().items():
        target = ROOT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body)
        print(f"wrote {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
