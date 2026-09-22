#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB missing-currency disclosure package.

The signed PWB bytes are never edited while this package is a candidate.
Proposed bytes live as patches, and the manifest hashes the eleven-artifact
subject after those patches. Applying them is an adoption-time operation.
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
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "pwb-missing-currency-disclosure-scenario"
)
PROPOSED = CANDIDATE / "proposed"
MANIFEST_OUT = CANDIDATE / "PWB-MISSING-CURRENCY-DISCLOSURE-MANIFEST.txt"
TITLE = "PWB MISSING-CURRENCY DISCLOSURE SCENARIO AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
DEPENDENCIES = CHANGE / "GOVERNING-DEPENDENCIES.md"
PROPOSAL = CHANGE / "proposal.md"
CAPABILITY_COVERAGE = CHANGE / "CAPABILITY-COVERAGE.md"
CONTRACT_REPAIR = CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"

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
PATCHED = tuple(
    sorted(
        (
            CAPABILITY_COVERAGE,
            CONTRACT_COVERAGE,
            CONTRACT_REPAIR,
            DEPENDENCIES,
            PROPOSAL,
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
HEADING = "#### Scenario: No effective currency bound is disclosed outside freshness"
NEXT_SCENARIO = "#### Scenario: Missing current evidence remains explicit Unknown"
NEXT_REQUIREMENT = "### Requirement: PWB-REQ-004"
EXACT_REASON = "`no-currency-bound-declared`"
EXACT_ROUTE = "`Declare\n  the bound in quality policy`"
OUTSIDE_SLOT = "outside the claim's freshness slot"
NO_FABRICATION = "no `fresh`, `stale`,\n  `broken`, `superseded` or fifth value is minted, inferred or force-fit"
NO_ABSORPTION = "no aggregate absorbs the claim into a current\n  or favourable value"

SIBLING_SPEC_PATCHES = {
    "exact-source": pathlib.Path(
        ".syzygy/governance/contracts/candidates/"
        "pwb-exact-source-render-mode-scenario/proposed/spec.md.patch"
    ),
    "machine-view": pathlib.Path(
        ".syzygy/governance/contracts/candidates/"
        "pwb-machine-view-amendment/proposed/spec.md.patch"
    ),
    "opening-band-dov.21": pathlib.Path(
        ".syzygy/governance/contracts/candidates/"
        "pwb-opening-band-scenario/proposed/spec.md.patch"
    ),
    "lane-b": pathlib.Path(
        ".syzygy/governance/contracts/candidates/"
        "pwb-scoped-attributes-amendment/proposed/spec.md.patch"
    ),
}
EXACT_SOURCE_CAPABILITY_PATCH = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "pwb-exact-source-render-mode-scenario/proposed/CAPABILITY-COVERAGE.md.patch"
)


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
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda path: path.name)


def apply_patches(
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
            raise ValueError(
                f"{patch.name} does not apply: {done.stderr.strip()}"
            )


def proposed_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
    patches: list[pathlib.Path] | None = None,
) -> dict[pathlib.Path, bytes]:
    current = current_bytes(overrides)
    patches = patch_files() if patches is None else patches
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        for rel, body in current.items():
            (base / rel).parent.mkdir(parents=True, exist_ok=True)
            (base / rel).write_bytes(body)
        apply_patches(base, patches)
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def scenario_findings(spec: bytes) -> list[str]:
    text = spec.decode("utf-8")
    findings: list[str] = []
    if text.count(HEADING) != 1:
        findings.append("missing or duplicate disclosure scenario")
        return findings
    requirement_start = text.find("### Requirement: PWB-REQ-007")
    scenario_start = text.find(HEADING)
    next_scenario = text.find(NEXT_SCENARIO, scenario_start)
    requirement_end = text.find(NEXT_REQUIREMENT, scenario_start)
    if not (
        0 <= requirement_start < scenario_start < next_scenario < requirement_end
    ):
        findings.append("disclosure scenario is not in the required PWB-REQ-007 position")
    section = text[scenario_start:next_scenario]
    for label, token in (
        ("exact Unknown reason", EXACT_REASON),
        ("exact resolution route", EXACT_ROUTE),
        ("outside-slot disclosure", OUTSIDE_SLOT),
        ("no fabricated freshness", NO_FABRICATION),
        ("no favourable aggregate absorption", NO_ABSORPTION),
        ("owner-act provenance", "effective owner-act provenance"),
        ("evaluation identity", "evaluation identity"),
    ):
        if token not in section:
            findings.append(f"scenario lacks {label}")
    return findings


def dependency_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_spec_dependencies as generator

    rendered, errors = generator.generate(proposed[SPEC].decode("utf-8"))
    if errors:
        return [f"proposed warrants do not validate: {'; '.join(errors)}"]
    if rendered.encode("utf-8") != proposed[DEPENDENCIES]:
        return [
            "proposed GOVERNING-DEPENDENCIES.md differs from regeneration "
            "over the proposed spec bytes"
        ]
    return []


def companion_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    findings: list[str] = []
    proposal = proposed[PROPOSAL].decode("utf-8")
    capability = proposed[CAPABILITY_COVERAGE].decode("utf-8")
    repair = proposed[CONTRACT_REPAIR].decode("utf-8")
    if "missing-bound condition is disclosed outside that slot" not in proposal:
        findings.append("proposal does not carry the outside-slot exception")
    if "except disclose a missing effective currency bound outside the freshness slot" not in capability:
        findings.append("capability coverage does not carry the exception")
    for consequence in (
        "RFC6-14.r1",
        "RFC6-14.r3",
        "RFC6-17.r1",
        "RFC7-16.r1",
        "RFC7-33.r1",
    ):
        row = next((line for line in repair.splitlines() if f"| {consequence} |" in line), "")
        if not row.endswith("| unknown-uncovered |"):
            findings.append(f"{consequence} is not honestly Unknown uncovered")

    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_contract_coverage as coverage

    try:
        rendered = coverage.render(repair_text=repair)
    except ValueError as error:
        findings.append(f"contract-coverage repair does not validate: {error}")
    else:
        if rendered.encode("utf-8") != proposed[CONTRACT_COVERAGE]:
            findings.append(
                "proposed CONTRACT-COVERAGE.md differs from regeneration over "
                "the proposed repair delta"
            )
    return findings


def _compose(order: list[pathlib.Path]) -> tuple[bool, bytes | str]:
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / SPEC).parent.mkdir(parents=True, exist_ok=True)
        (base / SPEC).write_bytes((ROOT / SPEC).read_bytes())
        try:
            apply_patches(base, order)
        except ValueError as error:
            return False, str(error)
        return True, (base / SPEC).read_bytes()


def _compose_target(
    target: pathlib.Path, order: list[pathlib.Path]
) -> tuple[bool, bytes | str]:
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / target).parent.mkdir(parents=True, exist_ok=True)
        (base / target).write_bytes((ROOT / target).read_bytes())
        try:
            apply_patches(base, order)
        except ValueError as error:
            return False, str(error)
        return True, (base / target).read_bytes()


def composition_findings(
    mine: pathlib.Path | None = None,
    siblings: dict[str, pathlib.Path] | None = None,
) -> list[str]:
    """Exercise both raw patch orders and enforce the declared regeneration rule."""
    mine = ROOT / PROPOSED / "spec.md.patch" if mine is None else mine
    siblings = SIBLING_SPEC_PATCHES if siblings is None else siblings
    findings: list[str] = []
    for name, relative in siblings.items():
        sibling = ROOT / relative if not relative.is_absolute() else relative
        if not sibling.is_file():
            findings.append(f"missing sibling spec patch: {relative}")
            continue
        sibling_first, first_result = _compose([sibling, mine])
        mine_first, second_result = _compose([mine, sibling])
        if not sibling_first:
            findings.append(f"{name} then this package does not compose: {first_result}")
        if name == "lane-b":
            if mine_first:
                findings.append(
                    "lane B unexpectedly applies after this package; re-derive the "
                    "declared later-package regeneration rule"
                )
        elif not mine_first:
            findings.append(f"this package then {name} does not compose: {second_result}")
        elif first_result != second_result:
            findings.append(f"{name} composition changes final spec bytes by order")
    capability_sibling = ROOT / EXACT_SOURCE_CAPABILITY_PATCH
    capability_mine = ROOT / PROPOSED / "CAPABILITY-COVERAGE.md.patch"
    if not capability_sibling.is_file():
        findings.append(f"missing sibling capability patch: {EXACT_SOURCE_CAPABILITY_PATCH}")
    else:
        first_ok, first_result = _compose_target(
            CAPABILITY_COVERAGE, [capability_sibling, capability_mine]
        )
        second_ok, second_result = _compose_target(
            CAPABILITY_COVERAGE, [capability_mine, capability_sibling]
        )
        if not first_ok or not second_ok:
            findings.append(
                "exact-source capability coverage does not compose in both orders: "
                f"{first_result}; {second_result}"
            )
        elif first_result != second_result:
            findings.append(
                "exact-source capability coverage changes final bytes by order"
            )
    return findings


def dependency_patch_findings() -> list[str]:
    mine = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    findings: list[str] = []
    for name, spec_patch in SIBLING_SPEC_PATCHES.items():
        sibling = ROOT / spec_patch.parent / "GOVERNING-DEPENDENCIES.md.patch"
        if not sibling.is_file():
            findings.append(f"missing {name} generated dependency patch")
            continue
        first_ok, _ = _compose_target(DEPENDENCIES, [sibling, mine])
        second_ok, _ = _compose_target(DEPENDENCIES, [mine, sibling])
        if first_ok or second_ok:
            findings.append(
                f"{name} generated dependency patch no longer collides in both orders; "
                "re-derive the later-package regeneration rule"
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
    lines.extend(
        f"{sha256(values[rel])}  {rel.as_posix()}" for rel in BEHAVIOR_SUBJECTS
    )
    return "\n".join(lines) + "\n"


def verify_manifest(text: str, expected: str) -> list[str]:
    rows = ROW.findall(text)
    expected_paths = [path.as_posix() for path in BEHAVIOR_SUBJECTS]
    if [path for _digest, path in rows] != expected_paths:
        return ["manifest path population or order differs"]
    if text != expected:
        return ["manifest differs from exact regeneration over proposed bytes"]
    return []


def check() -> list[str]:
    findings: list[str] = []
    patches = patch_files()
    if [patch.name for patch in patches] != [f"{path.name}.patch" for path in PATCHED]:
        findings.append("proposed patch population differs from declared subjects")
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    current = current_bytes()
    for rel in BEHAVIOR_SUBJECTS:
        changed = proposed[rel] != current[rel]
        if changed and rel not in PATCHED:
            findings.append(f"undeclared subject change: {rel}")
        if not changed and rel in PATCHED:
            findings.append(f"declared patched subject is unchanged: {rel}")
    findings.extend(scenario_findings(proposed[SPEC]))
    findings.extend(dependency_findings(proposed))
    findings.extend(companion_findings(proposed))
    findings.extend(composition_findings())
    findings.extend(dependency_patch_findings())
    target = ROOT / MANIFEST_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST_OUT}")
    else:
        findings.extend(verify_manifest(target.read_text(), render(proposed)))
    return findings


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        print("SELFTEST FAILED: behavior subject is not eleven unique paths")
        return 1
    proposed = proposed_bytes()
    baseline = render(proposed)
    current = current_bytes()
    first = next(path for path in BEHAVIOR_SUBJECTS if path not in PATCHED)
    drifted_manifest = render(
        proposed_bytes({first: current[first] + b"\nsubject drift\n"})
    )
    if baseline == drifted_manifest:
        print("SELFTEST FAILED: subject drift did not stale the manifest")
        return 1
    rows = ROW.findall(baseline)
    reordered = baseline.replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, baseline):
        print("SELFTEST FAILED: manifest path-order mutation passed")
        return 1
    spec = proposed[SPEC]
    mutations = {
        "missing scenario": spec.replace((HEADING + "\n").encode(), b"", 1),
        "duplicate scenario": spec.replace(
            (HEADING + "\n").encode(), (HEADING + "\n" + HEADING + "\n").encode(), 1
        ),
        "placement": spec.replace(
            (HEADING + "\n").encode(), b"#### Scenario: misplaced\n", 1
        ),
        "fabricated freshness": spec.replace(
            NO_FABRICATION.encode(),
            b"freshness `stale` is force-fit for this condition",
            1,
        ),
        "aggregate absorption": spec.replace(
            NO_ABSORPTION.encode(), b"an aggregate may absorb the claim", 1
        ),
    }
    for name, mutated in mutations.items():
        if mutated == spec or not scenario_findings(mutated):
            print(f"SELFTEST FAILED: {name} mutation passed")
            return 1
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        corrupted = original.replace(
            "#### Scenario: Missing current evidence remains explicit Unknown",
            "#### Scenario: Missing present evidence remains explicit Unknown",
            1,
        )
        if corrupted == original:
            print("SELFTEST FAILED: patch-drift fixture matched nothing")
            return 1
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: patch drift passed")
            return 1
        if not composition_findings(mine=broken):
            print("SELFTEST FAILED: corrupted patch passed sibling composition")
            return 1
    tampered = dict(proposed)
    tampered[DEPENDENCIES] = proposed[DEPENDENCIES].replace(
        b"17 requirement(s)", b"18 requirement(s)", 1
    )
    if tampered[DEPENDENCIES] == proposed[DEPENDENCIES] or not dependency_findings(tampered):
        print("SELFTEST FAILED: generated dependency drift passed")
        return 1
    coverage_drift = dict(proposed)
    coverage_drift[CONTRACT_COVERAGE] = proposed[CONTRACT_COVERAGE].replace(
        b"132 covered", b"133 covered", 1
    )
    if coverage_drift[CONTRACT_COVERAGE] == proposed[CONTRACT_COVERAGE] or not companion_findings(coverage_drift):
        print("SELFTEST FAILED: generated contract-coverage drift passed")
        return 1
    if composition_findings():
        print("SELFTEST FAILED: sibling composition does not verify")
        return 1
    print(
        "selftest: missing/duplicate scenario, placement, fabricated freshness, "
        "aggregate absorption, stale manifest, path order, patch drift, dependency "
        "drift, contract-coverage drift, sibling orders and generated-patch "
        "collision all fail closed"
    )
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is an adoption-time operation; pass --at-adoption "
            "only in the owner's act change"
        )
        return 2
    findings = check()
    if findings:
        print("refusing to apply: package does not verify")
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
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--at-adoption", action="store_true")
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
            print("PWB missing-currency disclosure package does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(
            f"PWB missing-currency disclosure manifest matches {len(BEHAVIOR_SUBJECTS)} "
            f"proposed subjects ({len(PATCHED)} patched, "
            f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); scenario, "
            "dependency regeneration and sibling-order rules verify"
        )
        return 0
    if not args.write:
        print(
            "refusing: regenerating the manifest retires copied act arguments; "
            "pass --write and update every registered digest copy"
        )
        return 2
    proposed = proposed_bytes()
    structure = (
        scenario_findings(proposed[SPEC])
        + dependency_findings(proposed)
        + companion_findings(proposed)
    )
    if structure:
        for finding in structure:
            print(f"  {finding}")
        return 1
    target = ROOT / MANIFEST_OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(proposed))
    print(f"wrote {MANIFEST_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
