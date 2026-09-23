#!/usr/bin/env python3
"""Builder for the polaris-edit-repair-deletion-scenario candidate package.

Candidate — binds nothing. Drafted for bead syzygy-dov.23, "Gate: CC-REV-2
scenario for the generator edit-stage deletion (P-73 slice 4)", per the
owner direction in
.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md
(P-73): "The scenario may be drafted at once; drafting binds nothing."

This script never edits the two governed files it names. It reads their
current bytes, applies this package's proposed/*.patch files only inside a
scratch tempdir, and renders/verifies a sha256 manifest of the resulting
(proposed) bytes. The manifest binds nothing until an owner act names its
digest in ACCEPTANCE-ACT-RECORD.md. The one path that writes the real tree
is `--apply --at-adoption`, reserved for the adoption step itself.

Follows the shape of scripts/build_pwb_opening_band_scenario.py and
scripts/build_pwb_exact_source_render_mode_amendment.py (AGENTS.md
"Governance recorders").

Usage:
  python3 scripts/build_polaris_edit_repair_deletion_scenario.py --check
  python3 scripts/build_polaris_edit_repair_deletion_scenario.py --selftest
  python3 scripts/build_polaris_edit_repair_deletion_scenario.py --write
  python3 scripts/build_polaris_edit_repair_deletion_scenario.py --diff
  python3 scripts/build_polaris_edit_repair_deletion_scenario.py --apply --at-adoption
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = ".syzygy/governance/contracts/candidates/polaris-edit-repair-deletion-scenario"
CANDIDATES_REL = ".syzygy/governance/contracts/candidates"
MANIFEST_NAME = "POLARIS-EDIT-REPAIR-DELETION-SCENARIO-MANIFEST.txt"

# Every artifact this package's manifest binds. Rows sorted by codepoint
# path (matches the sibling PWB packages' convention).
AMENDMENT_SPEC = "openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md"
PREDECESSOR_SPEC = "openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md"
STATUS_PAGE = "PROJECT-STATUS.md"
UNDERSTANDING_ACT = ".syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md"
OWNER_RULINGS = ".syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md"
CC_REV_POLICY = ".syzygy/governance/policies/craft-and-care/review-and-documentation.md"

BEHAVIOR_SUBJECTS: tuple[str, ...] = tuple(sorted([
    AMENDMENT_SPEC,
    CC_REV_POLICY,
    OWNER_RULINGS,
    PREDECESSOR_SPEC,
    STATUS_PAGE,
    UNDERSTANDING_ACT,
]))

# The only two files this package's patches actually change. Every other
# BEHAVIOR_SUBJECTS row is read-only reference: its manifest row exists so
# --check catches drift in the bound bytes this package's claims quote from.
PATCHED: frozenset[str] = frozenset({AMENDMENT_SPEC, STATUS_PAGE})

PATCH_FILENAME: dict[str, str] = {
    AMENDMENT_SPEC: "spec.md.patch",
    STATUS_PAGE: "PROJECT-STATUS.md.patch",
}

SCENARIO_MARKER = b"#### Scenario:"
COMPOSITION_FIGURE_RE = re.compile(rb"(\d+) requirements and (\d+) scenarios in the effective composition")


class BuildError(RuntimeError):
    """Raised on any check failure; the CLI prints str(e) and exits 1."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def package_dir(root: Path) -> Path:
    return root / PACKAGE_REL


def proposed_dir(root: Path) -> Path:
    return package_dir(root) / "proposed"


def manifest_path(root: Path) -> Path:
    return package_dir(root) / MANIFEST_NAME


def current_bytes(root: Path, rel: str) -> bytes:
    path = root / rel
    if not path.is_file():
        raise BuildError(f"missing behavior subject: {rel}")
    return path.read_bytes()


def patch_bytes(root: Path, rel: str) -> bytes:
    name = PATCH_FILENAME[rel]
    path = proposed_dir(root) / name
    if not path.is_file():
        raise BuildError(f"missing proposed patch for {rel}: {path}")
    return path.read_bytes()


def _run_git_apply(cwd: Path, patch_file: Path, check_only: bool) -> None:
    args = ["git", "apply", "--whitespace=nowarn"]
    if check_only:
        args.append("--check")
    args.append(str(patch_file))
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise BuildError(
            f"git apply {'--check ' if check_only else ''}failed for {patch_file.name}:\n"
            f"{result.stdout}{result.stderr}"
        )


def apply_in_scratch(root: Path, *, check_only_first: bool = True) -> dict[str, bytes]:
    """Materialize every BEHAVIOR_SUBJECTS path in a scratch dir, apply this
    package's patches to the PATCHED subset, and return the resulting bytes
    for every subject (patched or not). Never touches root itself."""
    with tempfile.TemporaryDirectory(prefix="polaris-edit-repair-deletion-") as tmp:
        scratch = Path(tmp)
        for rel in BEHAVIOR_SUBJECTS:
            dest = scratch / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(current_bytes(root, rel))
        for rel in sorted(PATCHED):
            pfile = proposed_dir(root) / PATCH_FILENAME[rel]
            if not pfile.is_file():
                raise BuildError(f"missing proposed patch for {rel}: {pfile}")
            if check_only_first:
                _run_git_apply(scratch, pfile, check_only=True)
            _run_git_apply(scratch, pfile, check_only=False)
        return {rel: (scratch / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def render_manifest(root: Path) -> str:
    proposed = apply_in_scratch(root)
    lines = [
        "# POLARIS EDIT/REPAIR DELETION-ACCOUNT SCENARIO MANIFEST",
        "# Bead syzygy-dov.23. These rows bind only by the owner act that names",
        "# this file's digest in ACCEPTANCE-ACT-RECORD.md; until that act is",
        "# performed they bind nothing.",
        f"# {len(BEHAVIOR_SUBJECTS)} artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
        "# PATCHED rows hash the PROPOSED bytes: current bytes with",
        "# proposed/*.patch applied. They match the tree only after --apply",
        "# --at-adoption. Reference rows hash CURRENT bytes and exist so this",
        "# package's own --check catches drift in bytes it quotes from.",
    ]
    for rel in BEHAVIOR_SUBJECTS:
        tag = "PATCHED" if rel in PATCHED else "REFERENCE"
        digest = sha256_bytes(proposed[rel])
        lines.append(f"{digest}  {rel}  # {tag}")
    lines.append("")
    return "\n".join(lines)


def verify_manifest(root: Path) -> list[str]:
    mpath = manifest_path(root)
    if not mpath.is_file():
        return [f"manifest not found at {mpath}; run --write"]
    recorded: dict[str, str] = {}
    for line in mpath.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("  ", 2)
        if len(parts) < 2:
            continue
        digest, rel = parts[0], parts[1]
        recorded[rel] = digest
    problems: list[str] = []
    if set(recorded) != set(BEHAVIOR_SUBJECTS):
        missing = set(BEHAVIOR_SUBJECTS) - set(recorded)
        extra = set(recorded) - set(BEHAVIOR_SUBJECTS)
        if missing:
            problems.append(f"manifest missing rows for: {sorted(missing)}")
        if extra:
            problems.append(f"manifest has stale rows for: {sorted(extra)}")
    proposed = apply_in_scratch(root)
    for rel in BEHAVIOR_SUBJECTS:
        if rel not in recorded:
            continue
        actual = sha256_bytes(proposed[rel])
        if actual != recorded[rel]:
            problems.append(f"manifest digest mismatch for {rel}: recorded {recorded[rel]}, actual {actual}")
    return problems


def scenario_delta_finding(root: Path) -> list[str]:
    """Cross-check, by two independent readings, that this package's patches
    move the composed scenario count by exactly +1 and nothing else.

    Method 1: count literal '#### Scenario:' headers in the amendment spec
    file itself, before and after the patch. Method 2: the literal integer
    PROJECT-STATUS.md states for 'scenarios in the effective composition',
    before and after its patch. The two deltas must agree (verification
    rule 2: no claim without a second method). This does NOT re-derive the
    full composed total from the composition formula (predecessor's 22
    untouched requirements plus the amendment's 9) — it trusts the existing
    177 baseline as the bound act's own figure (cited, not recomputed) and
    checks only that both files move by the same +1."""
    problems: list[str] = []
    old_amendment = current_bytes(root, AMENDMENT_SPEC)
    old_status = current_bytes(root, STATUS_PAGE)
    proposed = apply_in_scratch(root)
    new_amendment = proposed[AMENDMENT_SPEC]
    new_status = proposed[STATUS_PAGE]

    old_scenario_count = old_amendment.count(SCENARIO_MARKER)
    new_scenario_count = new_amendment.count(SCENARIO_MARKER)
    scenario_delta = new_scenario_count - old_scenario_count

    old_match = COMPOSITION_FIGURE_RE.search(old_status)
    new_match = COMPOSITION_FIGURE_RE.search(new_status)
    if not old_match or not new_match:
        problems.append("could not locate the 'N requirements and N scenarios' sentence in PROJECT-STATUS.md")
        return problems

    old_reqs, old_total = int(old_match.group(1)), int(old_match.group(2))
    new_reqs, new_total = int(new_match.group(1)), int(new_match.group(2))
    status_delta = new_total - old_total

    if old_reqs != new_reqs:
        problems.append(f"requirement count must not move: {old_reqs} -> {new_reqs}")
    if scenario_delta != 1:
        problems.append(
            f"amendment file's own '#### Scenario:' header count must move by exactly +1, "
            f"moved by {scenario_delta} ({old_scenario_count} -> {new_scenario_count})"
        )
    if status_delta != 1:
        problems.append(
            f"PROJECT-STATUS.md's stated scenario total must move by exactly +1, "
            f"moved by {status_delta} ({old_total} -> {new_total})"
        )
    if scenario_delta == 1 and status_delta == 1 and scenario_delta != status_delta:
        problems.append("unreachable: deltas both 1 but compared unequal")  # defensive
    return problems


def _iter_sibling_packages(candidates_dir: Path, exclude: str) -> list[Path]:
    if not candidates_dir.is_dir():
        return []
    out = []
    for entry in sorted(candidates_dir.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name == exclude:
            continue
        if (entry / "proposed").is_dir():
            out.append(entry)
    return out


def _patch_target(patch_file: Path) -> str | None:
    for line in patch_file.read_text(errors="replace").splitlines():
        if line.startswith("+++ b/"):
            return line[len("+++ b/"):]
        if line.startswith("+++ "):
            candidate = line[4:]
            return candidate[2:] if candidate.startswith("b/") else candidate
    return None


def composition_findings(root: Path) -> list[str]:
    """Sweep every other candidate package with a proposed/ directory for a
    patch that targets either of this package's two PATCHED paths. As of
    drafting there is no known sibling collision (denominator: every
    directory directly under contracts/candidates/ that has its own
    proposed/ subdirectory); a future package added after this one would be
    caught here on the next --check, per AGENTS.md's landing-order note."""
    findings: list[str] = []
    candidates_dir = root / CANDIDATES_REL
    siblings = _iter_sibling_packages(candidates_dir, exclude="polaris-edit-repair-deletion-scenario")
    for sib in siblings:
        for patch_file in sorted((sib / "proposed").glob("*.patch")):
            target = _patch_target(patch_file)
            if target in PATCHED:
                findings.append(
                    f"sibling package {sib.name}'s {patch_file.name} also patches {target}: "
                    "whichever act lands second must regenerate this package's manifest with --write"
                )
    return findings


def check(root: Path = ROOT, *, verbose: bool = True) -> None:
    problems: list[str] = []
    try:
        for rel in BEHAVIOR_SUBJECTS:
            current_bytes(root, rel)
    except BuildError as exc:
        raise BuildError(str(exc)) from exc

    try:
        apply_in_scratch(root)
    except BuildError as exc:
        raise BuildError(f"patch application failed: {exc}") from exc

    problems.extend(verify_manifest(root))
    problems.extend(scenario_delta_finding(root))

    collisions = composition_findings(root)
    if collisions:
        # A collision is informational at drafting time (no sibling collides
        # today) but must stop --check the moment one appears, per the same
        # landing-order rule the model PWB packages document: an unnoticed
        # second patch to a path this manifest already binds would make the
        # manifest wrong the instant either act lands.
        problems.extend(collisions)

    if problems:
        raise BuildError("FAIL:\n" + "\n".join(f"  - {p}" for p in problems))
    if verbose:
        print(f"PASS: {len(BEHAVIOR_SUBJECTS)} behavior subjects, {len(PATCHED)} patched, "
              f"0 manifest mismatches, scenario delta +1 confirmed by two methods, "
              f"0 sibling patch collisions.")


# --------------------------------------------------------------------------
# selftest: rule-6 mutation fixtures. Each builds an isolated fixture root
# (never the real ROOT) with exactly one thing wrong, and asserts check()
# raises BuildError against it. A fixture that fails to fail closed is a
# selftest failure.
# --------------------------------------------------------------------------

def _fixture_root(base: Path) -> Path:
    """Copy every file this script reads (behavior subjects + this
    package's own proposed/ and manifest) into an isolated fixture tree
    rooted at `base`, preserving relative paths."""
    for rel in BEHAVIOR_SUBJECTS:
        dest = base / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(current_bytes(ROOT, rel))
    pkg_src = package_dir(ROOT)
    pkg_dst = base / PACKAGE_REL
    pkg_dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(pkg_src / "proposed", pkg_dst / "proposed")
    real_manifest = manifest_path(ROOT)
    if real_manifest.is_file():
        (pkg_dst / MANIFEST_NAME).write_bytes(real_manifest.read_bytes())
    return base


def _expect_fail(label: str, root: Path) -> None:
    try:
        check(root, verbose=False)
    except BuildError:
        print(f"  [ok] {label}: check failed closed as expected")
        return
    raise BuildError(f"selftest fixture '{label}' did not fail: check() passed on a mutated input")


def selftest() -> None:
    print("Running rule-6 mutation fixtures (each must make check() fail closed)...")
    with tempfile.TemporaryDirectory(prefix="polaris-edit-repair-deletion-selftest-") as tmp:
        base = Path(tmp)

        # Fixture 1: manifest digest tampered (flip the first hex character
        # of the first data row, i.e. a line that is not a '#' comment).
        f1 = base / "f1"
        _fixture_root(f1)
        mpath = f1 / PACKAGE_REL / MANIFEST_NAME
        lines = mpath.read_text().splitlines(keepends=True)
        for i, line in enumerate(lines):
            if line.startswith("#") or not line.strip():
                continue
            flipped = "0" if line[0] != "0" else "1"
            lines[i] = flipped + line[1:]
            break
        else:
            raise BuildError("selftest fixture 'manifest digest tampered' found no data row to mutate")
        mpath.write_text("".join(lines))
        _expect_fail("manifest digest tampered", f1)

        # Fixture 2: proposed patch corrupted so it no longer applies.
        f2 = base / "f2"
        _fixture_root(f2)
        ppath = f2 / PACKAGE_REL / "proposed" / PATCH_FILENAME[AMENDMENT_SPEC]
        corrupted = ppath.read_text().replace("Independent review and repair", "Something else entirely")
        ppath.write_text(corrupted)
        _expect_fail("proposed patch corrupted (context mismatch)", f2)

        # Fixture 3: base file drifted since the patch was authored (context
        # the patch expects is no longer present).
        f3 = base / "f3"
        _fixture_root(f3)
        drifted = f3 / AMENDMENT_SPEC
        drifted.write_bytes(drifted.read_bytes().replace(
            b"The generator SHALL not classify its own wording change as immaterial.",
            b"The generator SHALL not classify its own wording change as unimportant.",
        ))
        _expect_fail("base file drifted under the patch's context", f3)

        # Fixture 4: PROJECT-STATUS.md patch mismatches the scenario-header
        # delta actually produced by the spec patch (off-by-one).
        f4 = base / "f4"
        _fixture_root(f4)
        spath = f4 / PACKAGE_REL / "proposed" / PATCH_FILENAME[STATUS_PAGE]
        bad = spath.read_text().replace("178 scenarios", "179 scenarios")
        spath.write_text(bad)
        _expect_fail("PROJECT-STATUS.md patch states a scenario total inconsistent with the spec patch", f4)

        # Fixture 5: an unnoticed sibling package patches the same file.
        f5 = base / "f5"
        _fixture_root(f5)
        sib_dir = f5 / CANDIDATES_REL / "fixture-colliding-package" / "proposed"
        sib_dir.mkdir(parents=True, exist_ok=True)
        (sib_dir / "collide.patch").write_text(
            "--- a/PROJECT-STATUS.md\n+++ b/PROJECT-STATUS.md\n"
            "@@ -1 +1 @@\n-x\n+y\n"
        )
        _expect_fail("undocumented sibling package patches the same behavior subject", f5)

        # Fixture 6: a behavior subject file is missing entirely (simulates
        # a moved/deleted reference file).
        f6 = base / "f6"
        _fixture_root(f6)
        (f6 / CC_REV_POLICY).unlink()
        _expect_fail("a referenced behavior subject is missing", f6)

    print("selftest: all 6 fixtures failed closed as expected.")


def apply_at_adoption(root: Path = ROOT) -> None:
    for rel in sorted(PATCHED):
        target = root / rel
        pfile = proposed_dir(root) / PATCH_FILENAME[rel]
        _run_git_apply(root, pfile, check_only=True)
    for rel in sorted(PATCHED):
        pfile = proposed_dir(root) / PATCH_FILENAME[rel]
        _run_git_apply(root, pfile, check_only=False)
    print(f"Applied {len(PATCHED)} patches to the real tree. This is the adoption step; "
          "it must run only inside the same change that records the performing owner act.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--write", action="store_true", help="regenerate the manifest file")
    parser.add_argument("--diff", action="store_true", help="print both proposed patches")
    parser.add_argument("--apply", action="store_true", help="write patches to the real tree (needs --at-adoption)")
    parser.add_argument("--at-adoption", action="store_true", dest="at_adoption")
    args = parser.parse_args()

    if not any([args.check, args.selftest, args.write, args.diff, args.apply]):
        parser.print_help()
        return 1

    try:
        if args.diff:
            for rel in sorted(PATCHED):
                pfile = proposed_dir(ROOT) / PATCH_FILENAME[rel]
                print(f"# {pfile.relative_to(ROOT)}")
                print(pfile.read_text())
        if args.write:
            manifest_path(ROOT).write_text(render_manifest(ROOT))
            print(f"Wrote {manifest_path(ROOT).relative_to(ROOT)}")
        if args.check:
            check(ROOT)
        if args.selftest:
            selftest()
        if args.apply:
            if not args.at_adoption:
                raise BuildError("--apply refused without --at-adoption: this writes the real tree")
            apply_at_adoption(ROOT)
    except BuildError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
