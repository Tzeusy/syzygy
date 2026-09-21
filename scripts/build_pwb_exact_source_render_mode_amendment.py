#!/usr/bin/env python3
"""Build and verify the inert PWB exact-source render-mode amendment manifest.

This script performs no owner act and writes no act record. The eleven PWB
behavior artifacts form one indivisible subject, exactly as in the performed
2026-09-05 truth-and-readiness amendment and in the sibling scoped-attributes
candidate. The proposed bytes are NOT applied to the tree while the package is
a candidate: CG-7h binds the current openspec bytes to the latest performed
act, so a drafted edit in place would read as drift. The proposed bytes live
as unified diffs under `proposed/` and the manifest rows hash the bytes those
diffs produce when applied to the current tree. `--apply` writes them into the
tree; it is the adoption step and belongs in the same change as the owner's
act record.

Two verifications beyond the precedent:

* GOVERNING-DEPENDENCIES.md is generated from spec.md and carries spec.md's
  sha256 in its source line. `--check` recomputes that digest over the
  PROPOSED spec.md bytes and refuses a row whose generated file disagrees, so
  no digest in this package is transcribed.
* The scoped-attributes candidate amends the same three files. `--check`
  applies that package's diffs first and then these, and asserts exactly which
  of these still apply: the three semantic patches must, and the generated
  GOVERNING-DEPENDENCIES.md patch must NOT, because both packages rewrite the
  one line that hashes spec.md. That collision is the merge rule, not a
  defect: whichever amendment lands second regenerates the file with
  `scripts/build_polaris_project_wide_spec_dependencies.py`.

Bare invocation refuses to overwrite the manifest; pass `--write` to
regenerate it. Once the packet quotes the manifest digest, a regeneration
retires the packet's argument (CG-7d/CG-7e catch the stale copy).
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario"
)
PROPOSED = CANDIDATE / "proposed"
LANE_B_PROPOSED = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed"
)
BEHAVIOR_OUT = CANDIDATE / "PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt"
TITLE = "PWB EXACT-SOURCE RENDER-MODE BEHAVIOR AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
#: Generated from SPEC; its source line carries SPEC's sha256.
GENERATED = CHANGE / "GOVERNING-DEPENDENCIES.md"
GENERATED_SOURCE_RE = re.compile(
    r"^> Source: `spec\.md` sha256 `([0-9a-f]{64})` — ", re.MULTILINE
)

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
            CHANGE / "CAPABILITY-COVERAGE.md",
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


def _apply_into(base: pathlib.Path, patch: pathlib.Path) -> tuple[int, str]:
    done = subprocess.run(
        ["git", "apply", "--whitespace=nowarn", str(patch)],
        cwd=base,
        capture_output=True,
        text=True,
    )
    return done.returncode, done.stderr.strip()


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
            code, error = _apply_into(base, patch)
            if code != 0:
                raise ValueError(
                    f"{patch.name} does not apply to the current subject bytes: {error}"
                )
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def generated_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    """The generated dependency file must carry the PROPOSED spec.md digest."""
    text = proposed[GENERATED].decode("utf-8")
    match = GENERATED_SOURCE_RE.search(text)
    if match is None:
        return [f"no source digest line found in {GENERATED.as_posix()}"]
    expected = sha256(proposed[SPEC])
    if match.group(1) != expected:
        return [
            f"{GENERATED.as_posix()} names a spec.md digest that is not the "
            f"proposed spec.md digest; regenerate it with "
            f"scripts/build_polaris_project_wide_spec_dependencies.py"
        ]
    return []


def lane_b_findings(
    patches: list[pathlib.Path] | None = None,
    lane_b_patches: list[pathlib.Path] | None = None,
) -> list[str]:
    """Assert exactly how these diffs behave on the scoped-attributes tree."""
    findings: list[str] = []
    if lane_b_patches is None:
        lane_b_patches = sorted(
            (ROOT / LANE_B_PROPOSED).glob("*.patch"), key=lambda p: p.name
        )
    if not lane_b_patches:
        return [
            "the scoped-attributes candidate's proposed/*.patch population is "
            f"empty or missing: {LANE_B_PROPOSED.as_posix()}"
        ]
    mine = patch_files() if patches is None else patches
    expected_collision = f"{GENERATED.name}.patch"
    if expected_collision not in {p.name for p in mine}:
        findings.append(
            f"no {expected_collision} in the proposed population; the declared "
            "regeneration collision cannot be tested"
        )
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        for rel, body in current_bytes().items():
            (base / rel).parent.mkdir(parents=True, exist_ok=True)
            (base / rel).write_bytes(body)
        for patch in lane_b_patches:
            code, error = _apply_into(base, patch)
            if code != 0:
                return findings + [
                    f"scoped-attributes {patch.name} does not apply to the "
                    f"current subject bytes: {error}"
                ]
        for patch in mine:
            code, error = _apply_into(base, patch)
            if patch.name == expected_collision:
                if code == 0:
                    findings.append(
                        f"{patch.name} applied after the scoped-attributes diffs; "
                        "the declared regeneration collision is gone, so the "
                        "merge rule in this package is no longer true"
                    )
            elif code != 0:
                findings.append(
                    f"{patch.name} does not apply after the scoped-attributes "
                    f"diffs: {error}"
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
    findings.extend(generated_findings(proposed))
    findings.extend(lane_b_findings())
    target = ROOT / BEHAVIOR_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {BEHAVIOR_OUT.as_posix()}")
    else:
        findings.extend(verify_manifest(target.read_text(), render(proposed)))
    return findings


def _rewrite_patch(scratch: pathlib.Path, name: str, old: str, new: str) -> pathlib.Path:
    original = (ROOT / PROPOSED / name).read_text()
    corrupted = original.replace(old, new, 1)
    if corrupted == original:
        raise ValueError(f"selftest fixture text not found in {name}: {old!r}")
    target = scratch / name
    target.write_text(corrupted)
    return target


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        print("SELFTEST FAILED: behavior population is not 11 unique paths")
        return 1
    if not set(PATCHED) <= set(BEHAVIOR_SUBJECTS):
        print("SELFTEST FAILED: a patched subject is outside the population")
        return 1
    proposed = proposed_bytes()
    baseline = render(proposed)
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
        b"levels. A reader who stops at any level SHALL retain a true, coarser",
        b"levels. A reader who stops at any level SHALL retain a truer, coarser",
        1,
    )
    if drifted == unpatched[SPEC]:
        print("SELFTEST FAILED: spec drift fixture text not found")
        return 1
    try:
        proposed_bytes({SPEC: drifted})
    except ValueError:
        pass
    else:
        print("SELFTEST FAILED: a patch applied over drifted subject bytes")
        return 1

    with tempfile.TemporaryDirectory() as scratch:
        broken = _rewrite_patch(
            pathlib.Path(scratch),
            "spec.md.patch",
            " deep dives and exact authoritative artifacts as progressively deeper reading",
            " deep dives and exact authoritative artifacts as progressively deeper readinz",
        )
        others = [p for p in patch_files() if p.name != "spec.md.patch"]
        try:
            proposed_bytes(patches=sorted(others + [broken], key=lambda p: p.name))
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a corrupted patch applied")
            return 1

    # The generated dependency file must fail closed on a transcribed digest.
    forged = dict(proposed)
    forged[GENERATED] = GENERATED_SOURCE_RE.sub(
        "> Source: `spec.md` sha256 `" + "0" * 64 + "` — ",
        proposed[GENERATED].decode("utf-8"),
        count=1,
    ).encode("utf-8")
    if forged[GENERATED] == proposed[GENERATED]:
        print("SELFTEST FAILED: generated-digest fixture did not change the file")
        return 1
    if not generated_findings(forged):
        print("SELFTEST FAILED: a wrong generated spec digest passed")
        return 1
    if generated_findings(proposed):
        print("SELFTEST FAILED: the proposed generated digest does not verify")
        return 1

    if lane_b_findings():
        print("SELFTEST FAILED: the lane interaction does not verify on current bytes")
        return 1

    lane_b = sorted((ROOT / LANE_B_PROPOSED).glob("*.patch"), key=lambda p: p.name)
    # (a) A wide-context design diff would collide with the scoped-attributes
    #     addition at the same insertion point; the check must say so.
    with tempfile.TemporaryDirectory() as scratch:
        design = CHANGE / "design.md"
        wide = list(
            difflib.unified_diff(
                unpatched[design].decode("utf-8").splitlines(keepends=True),
                proposed[design].decode("utf-8").splitlines(keepends=True),
                f"a/{design.as_posix()}",
                f"b/{design.as_posix()}",
                n=3,
            )
        )
        target = pathlib.Path(scratch) / "design.md.patch"
        target.write_text(
            f"diff --git a/{design.as_posix()} b/{design.as_posix()}\n" + "".join(wide)
        )
        widened = sorted(
            [p for p in patch_files() if p.name != "design.md.patch"] + [target],
            key=lambda p: p.name,
        )
        if proposed_bytes(patches=widened) != proposed:
            print("SELFTEST FAILED: the wide-context design diff is not equivalent")
            return 1
        if not lane_b_findings(patches=widened):
            print("SELFTEST FAILED: a wide-context design diff passed the lane check")
            return 1
    # (b) Without the scoped-attributes dependency diff there is no collision,
    #     and the check must refuse the merge rule it can no longer assert.
    without = [p for p in lane_b if p.name != f"{GENERATED.name}.patch"]
    if not lane_b_findings(lane_b_patches=without):
        print("SELFTEST FAILED: an absent regeneration collision passed")
        return 1

    print(
        "selftest: closed population, byte drift, path order, subject drift, "
        "patch corruption, transcribed generated digest, wide-context lane "
        "collision and absent regeneration collision fail closed"
    )
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
        print(
            "note: GOVERNING-DEPENDENCIES.md is generated from spec.md; its diff "
            "is a regeneration output and is re-derived, never merged, when "
            "another spec amendment lands first",
            file=sys.stderr,
        )
        return 0
    if args.apply:
        return apply(args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("PWB exact-source render-mode amendment manifest does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(f"PWB exact-source render-mode amendment manifest matches "
              f"{len(BEHAVIOR_SUBJECTS)} proposed behavior subjects "
              f"({len(PATCHED)} patched, {len(BEHAVIOR_SUBJECTS) - len(PATCHED)} "
              f"unchanged); the generated dependency file carries the proposed "
              f"spec.md digest; on the scoped-attributes tree the 3 semantic "
              f"patches apply and the generated one collides as declared")
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
