#!/usr/bin/env python3
"""Build and verify the inert PWB machine-view amendment manifest.

This script performs no owner act and writes no act record. The eleven PWB
behavior artifacts form one indivisible subject, exactly as in the performed
2026-09-05 truth-and-readiness amendment and in the sibling scoped-attributes
candidate. The proposed bytes are NOT applied to the tree while the package
is a candidate: CG-7h binds the current openspec bytes to the latest
performed act, so a drafted edit in place would read as drift. The proposed
bytes live as unified diffs under `proposed/` and the manifest rows hash the
bytes those diffs produce when applied to the current tree. `--apply` writes
them into the tree; it is the adoption step and belongs in the same change as
the owner's act record.

Two subjects move: the specification (one inserted block of prose inside
PWB-REQ-020, before its SHALL sentence) and `GOVERNING-DEPENDENCIES.md`,
whose `Source:` line is generated from the specification's digest. The second
is not an editorial choice — `--check` re-derives the proposed declaration
from the proposed specification text with the same generator CI runs, so the
row cannot drift from the spec it reports.

Two packages are pending against the same eleven subjects at once. `--check`
therefore also verifies that this package's spec patch applies to the tree
after the sibling `pwb-scoped-attributes-amendment` spec patch, and in the
other order, so neither owner decision is forced by patch mechanics. The
generated dependency declaration is a different matter: both packages rewrite
its one `Source:` digest line, so that patch is order-dependent by
construction. Whichever package the owner signs second must be regenerated
with `--write` against the tree after the first lands.

Bare invocation refuses to overwrite the manifest; pass `--write` to
regenerate it. Once the packet quotes the manifest digest, a regeneration
retires the packet's argument (CG-7d/CG-7e catch the stale copy).
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_polaris_project_wide_spec_dependencies as dependencies  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-machine-view-amendment"
)
PROPOSED = CANDIDATE / "proposed"
BEHAVIOR_OUT = CANDIDATE / "PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt"
TITLE = "PWB MACHINE-VIEW BEHAVIOR AMENDMENT MANIFEST"

#: The sibling candidate pending against the same eleven subjects.
SIBLING_SPEC_PATCH = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment"
    "/proposed/spec.md.patch"
)

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"

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
            GOVERNING,
            SPEC,
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


def apply_patches(rel: pathlib.Path, body: bytes, patches: list[pathlib.Path]) -> bytes:
    """`body` at repo path `rel` with unified diffs applied in order, in a scratch tree."""
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
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
                    f"{patch.name} does not apply to {rel.as_posix()}: "
                    f"{done.stderr.strip()}"
                )
        return (base / rel).read_bytes()


def derivation_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    """The proposed dependency declaration must be generated, never transcribed."""
    generated, errors = dependencies.generate(proposed[SPEC].decode())
    if errors:
        return [
            "proposed spec warrants do not validate: " + "; ".join(errors)
        ]
    if generated.encode() != proposed[GOVERNING]:
        return [
            "proposed GOVERNING-DEPENDENCIES.md bytes are not the generator's "
            "output over the proposed spec.md bytes"
        ]
    return []


def coexistence_findings(
    spec_bytes: bytes | None = None,
    sibling: pathlib.Path | None = None,
) -> list[str]:
    """Both pending spec patches must compose, in either order, into one spec."""
    findings: list[str] = []
    sibling = ROOT / SIBLING_SPEC_PATCH if sibling is None else sibling
    mine = ROOT / PROPOSED / "spec.md.patch"
    if not sibling.is_file():
        return [f"missing sibling spec patch: {SIBLING_SPEC_PATCH.as_posix()}"]
    if spec_bytes is None:
        spec_bytes = (ROOT / SPEC).read_bytes()
    try:
        sibling_first = apply_patches(SPEC, spec_bytes, [sibling, mine])
    except ValueError as error:
        return findings + [f"sibling-first composition failed: {error}"]
    try:
        mine_first = apply_patches(SPEC, spec_bytes, [mine, sibling])
    except ValueError as error:
        return findings + [f"this-package-first composition failed: {error}"]
    if sibling_first != mine_first:
        findings.append(
            "the two pending spec patches compose to different bytes depending "
            "on order"
        )
        return findings
    _generated, errors = dependencies.generate(sibling_first.decode())
    if errors:
        findings.append(
            "composed spec warrants do not validate: " + "; ".join(errors)
        )
    return findings


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
    findings.extend(derivation_findings(proposed))
    findings.extend(coexistence_findings())
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
    drifted = unpatched[SPEC].replace(
        b"Group: Parity. Form: **invariant**.",
        b"Group: Parity. Form: **invariant** .", 1)
    assert drifted != unpatched[SPEC]
    try:
        proposed_bytes({SPEC: drifted})
    except ValueError:
        pass
    else:
        print("SELFTEST FAILED: a patch applied over drifted subject bytes")
        return 1
    stored = (ROOT / BEHAVIOR_OUT).read_text() if (ROOT / BEHAVIOR_OUT).is_file() else None
    with tempfile.TemporaryDirectory() as scratch:
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        # A corrupted context line must make the patch refuse to apply.
        broken = pathlib.Path(scratch) / "context.patch"
        corrupted = original.replace(
            " Group: Parity. Form: **invariant**.",
            " Group: Parity. Form: **invariant** .", 1)
        assert corrupted != original
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a patch with a corrupted context line applied")
            return 1
        # A corrupted added line still applies, so the manifest must catch it.
        added = pathlib.Path(scratch) / "added.patch"
        corrupted = original.replace(
            "+neither multiset compared below. The member of this category is the",
            "+neither multiset compared below. The member of this category iz the", 1)
        assert corrupted != original
        added.write_text(corrupted)
        gd_patch = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
        corrupted_bytes = proposed_bytes(patches=[gd_patch, added])
        if corrupted_bytes[SPEC] == proposed_bytes()[SPEC]:
            print("SELFTEST FAILED: the corrupted added line changed nothing")
            return 1
        if stored is None:
            print("SELFTEST FAILED: no manifest to compare the corrupted patch against")
            return 1
        if not verify_manifest(stored, render(corrupted_bytes)):
            print("SELFTEST FAILED: a corrupted added line passed the manifest")
            return 1
        if not derivation_findings(corrupted_bytes):
            print("SELFTEST FAILED: a corrupted added line passed the derivation check")
            return 1
    if derivation_findings(proposed_bytes()):
        print("SELFTEST FAILED: the derivation check does not hold on current bytes")
        return 1
    proposed = proposed_bytes()
    transcribed = dict(proposed)
    transcribed[GOVERNING] = proposed[GOVERNING].replace(b" 17 requirement(s)",
                                                         b" 18 requirement(s)", 1)
    assert transcribed[GOVERNING] != proposed[GOVERNING]
    if not derivation_findings(transcribed):
        print("SELFTEST FAILED: a transcribed dependency declaration passed")
        return 1
    unwarranted = dict(proposed)
    unwarranted[SPEC] = proposed[SPEC].replace(b"  primary: RFC6-22\n", b"", 1)
    assert unwarranted[SPEC] != proposed[SPEC]
    if not derivation_findings(unwarranted):
        print("SELFTEST FAILED: a spec with a missing warrant passed")
        return 1
    if coexistence_findings():
        print("SELFTEST FAILED: the two pending spec patches do not compose")
        return 1
    sibling_context = unpatched[SPEC].replace(
        b"metric walls or count walls; coverage counts remain available on demand.",
        b"metric walls or count walls; coverage counts remain available on request.",
        1)
    assert sibling_context != unpatched[SPEC]
    if not coexistence_findings(spec_bytes=sibling_context):
        print("SELFTEST FAILED: drift under the sibling patch passed")
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        missing = pathlib.Path(scratch) / "absent.patch"
        if not coexistence_findings(sibling=missing):
            print("SELFTEST FAILED: a missing sibling patch passed")
            return 1
    print("selftest: closed population, byte drift, path order, subject drift, "
          "context-line and added-line patch corruption, transcribed and "
          "unwarranted dependency declarations, sibling drift and a missing "
          "sibling patch fail closed")
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
        print("note: the dependency declaration patch is generated from the "
              "proposed spec.md bytes and is order-dependent against the sibling "
              "candidate; regenerate with --write after either package lands",
              file=sys.stderr)
        return 0
    if args.apply:
        return apply(args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("PWB machine-view amendment manifest does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(f"PWB machine-view amendment manifest matches {len(BEHAVIOR_SUBJECTS)} "
              f"proposed behavior subjects ({len(PATCHED)} patched, "
              f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); the dependency "
              f"declaration is regenerated from the proposed spec and the spec patch "
              f"composes with the sibling candidate in either order")
        return 0
    if not args.write:
        print("refusing: regenerating the manifest changes the act argument; pass "
              "--write, then update every registered copy of the digest")
        return 2
    body = render(proposed_bytes())
    target = ROOT / BEHAVIOR_OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body)
    print(f"wrote {BEHAVIOR_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
