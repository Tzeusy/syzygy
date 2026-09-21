#!/usr/bin/env python3
"""Build and verify the inert PWB opening-band scenario manifest.

This script performs no owner act and writes no act record. The eleven PWB
behavior artifacts form one indivisible subject, exactly as in the performed
2026-09-05 truth-and-readiness amendment and in the lane B scoped-attributes
package. The proposed bytes are NOT applied to the tree while the package is
a candidate: CG-7h binds the current openspec bytes to the latest performed
act, so a drafted edit in place would read as drift. The proposed bytes live
as unified diffs under `proposed/` and the manifest rows hash the bytes those
diffs produce when applied to the current tree. `--apply` writes them into
the tree; it is the adoption step and belongs in the same change as the
owner's act record.

Two subjects move: the specification (one added scenario under PWB-REQ-010)
and the generated CC-IMPACT-1 dependency declaration, whose only changed byte
is the `spec.md` digest it quotes. `--check` therefore also regenerates the
declaration from the proposed specification bytes and requires the proposed
declaration to equal that regeneration, so the package can never carry a
hand-edited generated file.

`--check` additionally composes this package's specification patch with the
lane B package's specification patch, in both orders, in a scratch tree. The
two packages are independent offerings over the same signed subject; if
either is adopted first the other's patch must still apply.

Bare invocation refuses to overwrite the manifest; pass `--write` to
regenerate it. Once the packet quotes the manifest digest, a regeneration
retires the packet's argument (CG-7d/CG-7e catch the stale copy).
"""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-opening-band-scenario"
)
PROPOSED = CANDIDATE / "proposed"
LANE_B_SPEC_PATCH = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment"
    "/proposed/spec.md.patch"
)
LANE_B_DEPENDENCY_PATCH = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment"
    "/proposed/GOVERNING-DEPENDENCIES.md.patch"
)
MANIFEST_OUT = CANDIDATE / "PWB-OPENING-BAND-SCENARIO-MANIFEST.txt"
TITLE = "PWB OPENING-BAND SCENARIO AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
DEPENDENCIES = CHANGE / "GOVERNING-DEPENDENCIES.md"

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
    sorted((DEPENDENCIES, SPEC), key=lambda path: path.as_posix())
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


def _apply_all(
    base: pathlib.Path, patches: list[pathlib.Path]
) -> None:
    for patch in patches:
        done = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", str(patch)],
            cwd=base,
            capture_output=True,
            text=True,
        )
        if done.returncode != 0:
            name = patch.name
            raise ValueError(
                f"{name} does not apply to the base bytes: {done.stderr.strip()}"
            )


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
        _apply_all(base, patches)
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def dependency_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    """The proposed generated declaration must equal its own regeneration."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_spec_dependencies as generator

    rendered, errors = generator.generate(proposed[SPEC].decode("utf-8"))
    if errors:
        return [f"proposed spec warrants do not validate: {'; '.join(errors)}"]
    if rendered.encode("utf-8") != proposed[DEPENDENCIES]:
        return [
            "proposed GOVERNING-DEPENDENCIES.md differs from regeneration over "
            "the proposed spec bytes"
        ]
    return []


def composition_findings(
    first: pathlib.Path | None = None,
    second: pathlib.Path | None = None,
) -> list[str]:
    """This package's spec patch and lane B's must compose, in either order."""
    first = ROOT / LANE_B_SPEC_PATCH if first is None else first
    second = ROOT / PROPOSED / "spec.md.patch" if second is None else second
    if not first.is_file():
        return [f"missing lane B spec patch: {LANE_B_SPEC_PATCH.as_posix()}"]
    findings: list[str] = []
    for order in ((first, second), (second, first)):
        with tempfile.TemporaryDirectory() as scratch:
            base = pathlib.Path(scratch)
            (base / SPEC).parent.mkdir(parents=True, exist_ok=True)
            (base / SPEC).write_bytes((ROOT / SPEC).read_bytes())
            try:
                _apply_all(base, list(order))
            except ValueError as error:
                findings.append(
                    "spec patches do not compose in the order "
                    f"{order[0].name}, {order[1].name}: {error}"
                )
    return findings


def dependency_patches_collide() -> bool:
    """True when this package's and lane B's declaration patches conflict.

    Both rewrite the one generated digest line, so they cannot both apply.
    The composition is resolved by regenerating the declaration after the
    second specification patch lands, never by applying both diffs.
    """
    mine = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    theirs = ROOT / LANE_B_DEPENDENCY_PATCH
    if not (mine.is_file() and theirs.is_file()):
        return False
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / DEPENDENCIES).parent.mkdir(parents=True, exist_ok=True)
        (base / DEPENDENCIES).write_bytes((ROOT / DEPENDENCIES).read_bytes())
        try:
            _apply_all(base, [theirs, mine])
        except ValueError:
            return True
    return False


def render(values: dict[pathlib.Path, bytes]) -> str:
    lines = [
        f"# {TITLE}",
        "# These rows bind only by the owner act that names this file's digest in",
        "# ACCEPTANCE-ACT-RECORD.md; until that act is performed they bind nothing.",
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
    findings.extend(dependency_findings(proposed))
    findings.extend(composition_findings())
    target = ROOT / MANIFEST_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST_OUT.as_posix()}")
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
    drifted = unpatched[SPEC].replace(
        b"- **AND** the slice is labeled as one capability within the complete catalog",
        b"- **AND** the slice is labeled as one capability within the whole catalog",
        1,
    )
    if drifted == unpatched[SPEC]:
        print("SELFTEST FAILED: the spec drift fixture matched nothing")
        return 1
    try:
        proposed_bytes({SPEC: drifted})
    except ValueError:
        pass
    else:
        print("SELFTEST FAILED: a patch applied over drifted subject bytes")
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        corrupted = original.replace(
            "- **THEN** the Polaris entry explains Butlers before linking to that slice",
            "- **THEN** the Polaris entry explains Butlers before linking to the slice",
            1,
        )
        if corrupted == original:
            print("SELFTEST FAILED: the patch-corruption fixture matched nothing")
            return 1
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a corrupted patch applied")
            return 1
        if not composition_findings(second=broken):
            print("SELFTEST FAILED: a corrupted patch composed with lane B")
            return 1
    good = proposed_bytes()
    tampered = dict(good)
    tampered[DEPENDENCIES] = good[DEPENDENCIES].replace(
        b"17 requirement(s)", b"18 requirement(s)", 1
    )
    if tampered[DEPENDENCIES] == good[DEPENDENCIES]:
        print("SELFTEST FAILED: the declaration fixture matched nothing")
        return 1
    if not dependency_findings(tampered):
        print("SELFTEST FAILED: a hand-edited generated declaration passed")
        return 1
    if composition_findings():
        print("SELFTEST FAILED: the spec patches do not compose with lane B")
        return 1
    if not dependency_patches_collide():
        print("SELFTEST FAILED: the declaration patches no longer collide; the "
              "packet's regeneration note must be re-derived")
        return 1
    print("selftest: closed population, byte drift, path order, subject drift, "
          "patch corruption, lane B composition (both orders and a corrupted "
          "case), generated-declaration tampering and the declaration-patch "
          "collision all fail closed")
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
    parser.add_argument("--write", action="store_true",
                        help="regenerate the manifest (retires any packet quoting it)")
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
            print("PWB opening-band scenario manifest does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(f"PWB opening-band scenario manifest matches {len(BEHAVIOR_SUBJECTS)} "
              f"proposed behavior subjects ({len(PATCHED)} patched, "
              f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); the proposed "
              f"declaration equals its regeneration and the spec patch composes "
              f"with the lane B spec patch in both orders")
        return 0
    if not args.write:
        print("refusing: regenerating the manifest changes the act argument; pass "
              "--write, then update every registered copy of the digest")
        return 2
    body = render(proposed_bytes())
    target = ROOT / MANIFEST_OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body)
    print(f"wrote {MANIFEST_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
