#!/usr/bin/env python3
"""Build and verify the inert PWB scoped-attributes amendment manifest.

This script performs no owner act and writes no act record. The eleven PWB
behavior artifacts form one indivisible subject, exactly as in the performed
2026-09-05 truth-and-readiness amendment. Unlike that precedent, the proposed
bytes are NOT applied to the tree while the package is a candidate: CG-7h
binds the current openspec bytes to the latest performed act, so a drafted
edit in place would read as drift. The proposed bytes live as unified diffs
under `proposed/` and the manifest rows hash the bytes those diffs produce
when applied to the current tree. `--apply` writes them into the tree; it is
the adoption step and belongs in the same change as the owner's act record.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment"
)
PROPOSED = CANDIDATE / "proposed"
BEHAVIOR_OUT = CANDIDATE / "PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt"
TITLE = "PWB SCOPED-ATTRIBUTES BEHAVIOR AMENDMENT MANIFEST"

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
#: The subjects the proposed diffs touch; every other row equals current bytes.
PATCHED = tuple(
    sorted(
        (
            CHANGE / "GOVERNING-DEPENDENCIES.md",
            CHANGE / "design.md",
            CHANGE / "specs/polaris-project-wide-butlers-model/spec.md",
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def current_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in BEHAVIOR_SUBJECTS:
        target = ROOT / rel
        if rel in overrides:
            values[rel] = overrides[rel]
        elif target.is_file():
            values[rel] = target.read_bytes()
        else:
            raise ValueError(f"missing amendment subject: {rel}")
    return values


def patch_files() -> list[pathlib.Path]:
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda p: p.name)


def proposed_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
    patches: list[pathlib.Path] | None = None,
) -> dict[pathlib.Path, bytes]:
    """Current subject bytes with every `proposed/*.patch` applied, in a scratch tree."""
    current = current_bytes(overrides)
    patches = patch_files() if patches is None else patches
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        for rel, body in current.items():
            (base / rel).parent.mkdir(parents=True, exist_ok=True)
            (base / rel).write_bytes(body)
        for patch in patches:
            done = subprocess.run(
                ["git", "apply", "--whitespace=nowarn", str(patch)],
                cwd=base,
                capture_output=True,
                text=True,
            )
            if done.returncode != 0:
                raise ValueError(
                    f"{patch.relative_to(ROOT).as_posix()} does not apply to the "
                    f"current subject bytes: {done.stderr.strip()}"
                )
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def render(values: dict[pathlib.Path, bytes]) -> str:
    lines = [
        f"# {TITLE}",
        "# Candidate; this file and its rows bind nothing by themselves.",
        f"# {len(BEHAVIOR_SUBJECTS)} artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
        "# Rows hash the PROPOSED bytes: current bytes with proposed/*.patch",
        "# applied. They match the tree only after --apply, the adoption step.",
    ]
    lines.extend(f"{sha256(values[rel])}  {rel.as_posix()}" for rel in BEHAVIOR_SUBJECTS)
    return "\n".join(lines) + "\n"


def verify_manifest(text: str, expected: str) -> list[str]:
    findings: list[str] = []
    rows = ROW.findall(text)
    expected_paths = [path.as_posix() for path in BEHAVIOR_SUBJECTS]
    if [path for _digest, path in rows] != expected_paths:
        findings.append("manifest path population or order differs")
        return findings
    if text != expected:
        findings.append("manifest differs from exact regeneration over the proposed bytes")
    return findings


def check() -> list[str]:
    findings: list[str] = []
    patches = patch_files()
    if [p.name for p in patches] != [f"{p.name}.patch" for p in PATCHED]:
        findings.append(
            "proposed/*.patch population differs from the declared patched subjects: "
            + ", ".join(p.name for p in patches)
        )
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    current = current_bytes()
    for rel in BEHAVIOR_SUBJECTS:
        changed = proposed[rel] != current[rel]
        if changed and rel not in PATCHED:
            findings.append(f"undeclared subject change: {rel.as_posix()}")
        if not changed and rel in PATCHED:
            findings.append(f"declared patched subject is byte-identical: {rel.as_posix()}")
    target = ROOT / BEHAVIOR_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {BEHAVIOR_OUT.as_posix()}")
    else:
        findings.extend(verify_manifest(target.read_text(), render(proposed)))
    return findings


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        print("SELFTEST FAILED: behavior population is not 11 unique paths")
        return 1
    if not set(PATCHED) <= set(BEHAVIOR_SUBJECTS):
        print("SELFTEST FAILED: a patched subject is outside the population")
        return 1
    baseline = render(proposed_bytes())
    unpatched = current_bytes()
    first = next(rel for rel in BEHAVIOR_SUBJECTS if rel not in PATCHED)
    mutated = render(proposed_bytes({first: unpatched[first] + b"\nmutation\n"}))
    if baseline == mutated:
        print("SELFTEST FAILED: subject-byte mutation did not change the manifest")
        return 1
    rows = ROW.findall(baseline)
    reordered = baseline.replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, baseline):
        print("SELFTEST FAILED: path-order mutation passed")
        return 1
    spec = next(rel for rel in PATCHED if rel.name == "spec.md")
    drifted = unpatched[spec].replace(
        b"coverage counts remain available on demand.",
        b"coverage counts remain available on request.", 1)
    assert drifted != unpatched[spec]
    try:
        proposed_bytes({spec: drifted})
    except ValueError:
        pass
    else:
        print("SELFTEST FAILED: a patch applied over drifted subject bytes")
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        corrupted = original.replace(
            "-  zero invalid, missing or folded values decides.",
            "-  zero invalid, missing or folded values decidez.", 1)
        assert corrupted != original
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a corrupted patch applied")
            return 1
    print("selftest: closed population, byte drift, path order, subject drift and "
          "patch corruption fail closed")
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print("refusing: --apply writes the proposed bytes into the tree and is the "
              "adoption step; pass --at-adoption in the change that records the act")
        return 2
    findings = check()
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    proposed = proposed_bytes()
    for rel in PATCHED:
        (ROOT / rel).write_bytes(proposed[rel])
        print(f"applied {rel.as_posix()}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--at-adoption", action="store_true")
    parser.add_argument("--diff", action="store_true",
                        help="print the proposed diffs and exit")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.diff:
        for patch in patch_files():
            sys.stdout.write(patch.read_text())
        return 0
    if args.apply:
        return apply(args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("PWB scoped-attributes amendment manifest does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(f"PWB scoped-attributes amendment manifest matches {len(BEHAVIOR_SUBJECTS)} "
              f"proposed behavior subjects ({len(PATCHED)} patched, "
              f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged)")
        return 0
    body = render(proposed_bytes())
    target = ROOT / BEHAVIOR_OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body)
    print(f"wrote {BEHAVIOR_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
