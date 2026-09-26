#!/usr/bin/env python3
"""Recount the Polaris generation specification's effective scenario total.

Owner direction: `.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
Sec 5, "Before sign-off, a small script, with its own test, recounts the
effective composition's full scenario total from scratch, so the number the
page asserts is checked rather than carried forward." This is that script,
written for bead `syzygy-dov.23`.

It never edits any governed file. It reads the tree (or, with
`--with-proposed`, a scratch copy of the tree with one candidate package's
`proposed/*.patch` files applied) and independently recomputes, by two
different parsing methods, the scenario total the Polaris generation
capability's effective composition carries.

## What "effective composition" means here

AGENTS.md's Architecture note: "Polaris generation requirement lookup
composes the original `openspec/changes/polaris-manifesto-generation/` with
the explicit `polaris-manifesto-understanding-amendment/` overlay." This
script does not hard-code those two directory names. It globs every
`openspec/changes/*/specs/polaris-generation/spec.md` file, classifies each
by which OpenSpec delta sections it carries (a file with only an
`## ADDED Requirements` section is the base; a file carrying any
`MODIFIED`/`REMOVED`/`RENAMED` section is an overlay applied on top of the
base), and requires exactly one base and exactly one overlay -- refusing to
guess an order if a second overlay ever appears (verification rule 9: an
absence/uniqueness claim needs an enumerated sweep, not an assumption).

## Overlay semantics

Applied in the order the real OpenSpec tool uses at archive time (confirmed
2026-09-26 against `Fission-AI/OpenSpec`'s own
`openspec/specs/openspec-conventions/spec.md`, "Archiving changes with
deltas": RENAMED, then REMOVED, then MODIFIED, then ADDED), matching by
whitespace/case-normalized requirement name:

- RENAMED: `- FROM: \\`### Requirement: X\\`` / `- TO: \\`### Requirement: Y\\``
  renames a requirement already in the composition; its scenario count is
  carried over unchanged.
- REMOVED: drops a requirement (and every scenario under it) from the
  composition entirely.
- MODIFIED: REPLACES a requirement's entire scenario count with the
  overlay's version. It does not add to the predecessor's count -- this is
  the exact mistake this script exists to catch (see the "MODIFIED
  double-count" selftest fixture below).
- ADDED: inserts a new requirement. Colliding with an existing name is a
  fatal finding, not a silent merge.

Any dangling reference (a MODIFIED/REMOVED/RENAMED-FROM naming a requirement
absent from the composition so far, or an ADDED/RENAMED-TO colliding with an
existing one) is a fatal finding: this script fails closed rather than
guessing.

## Two independent methods (verification rule 2)

`parse_regex()` locates section and requirement boundaries with compiled
regular expressions. `parse_manual()` is a hand-written line-by-line state
machine that uses no regular expressions at all. Both run over the exact
same bytes; `build_composition()` composes each parser's output
independently and requires the two composed results to agree member-for-
member before trusting either one.

Usage:
  python3 scripts/count_polaris_effective_scenarios.py
  python3 scripts/count_polaris_effective_scenarios.py --check
  python3 scripts/count_polaris_effective_scenarios.py --check --expect 178
  python3 scripts/count_polaris_effective_scenarios.py --with-proposed \\
      .syzygy/governance/contracts/candidates/polaris-edit-repair-deletion-scenario --check
  python3 scripts/count_polaris_effective_scenarios.py --selftest
"""
from __future__ import annotations

import argparse
import contextlib
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_CAPABILITY = "polaris-generation"
STATUS_PAGE_REL = "PROJECT-STATUS.md"

SECTION_KINDS = ("ADDED", "MODIFIED", "REMOVED", "RENAMED")
SECTION_HEADER_RE = re.compile(r"^## (ADDED|MODIFIED|REMOVED|RENAMED) Requirements[ \t]*$", re.M)
REQ_HEADER_RE = re.compile(r"^### Requirement: (.+?)[ \t]*$", re.M)
SCENARIO_RE = re.compile(r"^#### Scenario:", re.M)
RENAME_FROM_RE = re.compile(r"^-\s*FROM:\s*`### Requirement:\s*(.+?)`\s*$", re.M)
RENAME_TO_RE = re.compile(r"^-\s*TO:\s*`### Requirement:\s*(.+?)`\s*$", re.M)
STATUS_FIGURE_RE = re.compile(rb"(\d+) requirements and (\d+) scenarios in the effective composition")


class ScenarioCountError(RuntimeError):
    """Raised on any check failure; the CLI prints str(e) and exits 1."""


def normalize_name(name: str) -> str:
    return " ".join(name.split()).casefold()


@dataclass
class ReqEntry:
    name: str
    scenario_count: int


@dataclass
class FileDelta:
    added: list[ReqEntry] = field(default_factory=list)
    modified: list[ReqEntry] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    renamed: list[tuple[str, str]] = field(default_factory=list)

    def section_kinds(self) -> set[str]:
        kinds: set[str] = set()
        if self.added:
            kinds.add("ADDED")
        if self.modified:
            kinds.add("MODIFIED")
        if self.removed:
            kinds.add("REMOVED")
        if self.renamed:
            kinds.add("RENAMED")
        return kinds


# --------------------------------------------------------------------------
# Method 1: regex-based structural parser.
# --------------------------------------------------------------------------

def parse_regex(text: str, source: str) -> FileDelta:
    delta = FileDelta()
    section_matches = list(SECTION_HEADER_RE.finditer(text))
    if not section_matches:
        raise ScenarioCountError(f"{source}: no '## ... Requirements' section headers found (method 1)")
    for i, m in enumerate(section_matches):
        kind = m.group(1)
        start = m.end()
        end = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(text)
        body = text[start:end]
        if kind == "RENAMED":
            froms = RENAME_FROM_RE.findall(body)
            tos = RENAME_TO_RE.findall(body)
            if len(froms) != len(tos):
                raise ScenarioCountError(
                    f"{source}: RENAMED section FROM/TO count mismatch ({len(froms)} vs {len(tos)}) (method 1)"
                )
            for old, new in zip(froms, tos):
                delta.renamed.append((old.strip(), new.strip()))
            continue
        req_matches = list(REQ_HEADER_RE.finditer(body))
        for j, rm in enumerate(req_matches):
            rname = rm.group(1).strip()
            rstart = rm.end()
            rend = req_matches[j + 1].start() if j + 1 < len(req_matches) else len(body)
            rbody = body[rstart:rend]
            scount = len(SCENARIO_RE.findall(rbody))
            if kind == "ADDED":
                delta.added.append(ReqEntry(rname, scount))
            elif kind == "MODIFIED":
                delta.modified.append(ReqEntry(rname, scount))
            elif kind == "REMOVED":
                delta.removed.append(rname)
    return delta


# --------------------------------------------------------------------------
# Method 2: manual line-by-line state machine. No regular expressions.
# --------------------------------------------------------------------------

def _extract_backtick_requirement_name(line: str, source: str) -> str:
    first = line.find("`")
    last = line.rfind("`")
    if first == -1 or last == -1 or last <= first:
        raise ScenarioCountError(f"{source}: malformed FROM/TO line (method 2): {line!r}")
    inner = line[first + 1 : last]
    prefix = "### Requirement:"
    if not inner.startswith(prefix):
        raise ScenarioCountError(f"{source}: malformed FROM/TO requirement header (method 2): {inner!r}")
    return inner[len(prefix):].strip()


def parse_manual(text: str, source: str) -> FileDelta:
    delta = FileDelta()
    section: str | None = None
    saw_section = False
    cur_name: str | None = None
    cur_count = 0
    pending_from: str | None = None

    def flush() -> None:
        nonlocal cur_name, cur_count
        if cur_name is not None:
            if section == "ADDED":
                delta.added.append(ReqEntry(cur_name, cur_count))
            elif section == "MODIFIED":
                delta.modified.append(ReqEntry(cur_name, cur_count))
            elif section == "REMOVED":
                delta.removed.append(cur_name)
        cur_name = None
        cur_count = 0

    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\r")
        stripped = line.strip()
        section_label = None
        if line.startswith("## "):
            candidate = line[3:].strip()
            for kind in SECTION_KINDS:
                if candidate == f"{kind} Requirements":
                    section_label = kind
                    break
        if section_label is not None:
            flush()
            section = section_label
            saw_section = True
            pending_from = None
            continue
        if section is None:
            continue
        if line.startswith("### Requirement: "):
            flush()
            cur_name = line[len("### Requirement: "):].strip()
            cur_count = 0
            continue
        if section == "RENAMED":
            if stripped.startswith("- FROM:"):
                pending_from = _extract_backtick_requirement_name(stripped, source)
                continue
            if stripped.startswith("- TO:"):
                if pending_from is None:
                    raise ScenarioCountError(f"{source}: RENAMED TO with no preceding FROM (method 2)")
                to_name = _extract_backtick_requirement_name(stripped, source)
                delta.renamed.append((pending_from, to_name))
                pending_from = None
                continue
            continue
        if stripped.startswith("#### Scenario:"):
            if cur_name is not None and section in ("ADDED", "MODIFIED"):
                cur_count += 1
            continue
    flush()
    if not saw_section:
        raise ScenarioCountError(f"{source}: no '## ... Requirements' section headers found (method 2)")
    return delta


# --------------------------------------------------------------------------
# Composition.
# --------------------------------------------------------------------------

def compose(deltas: list[tuple[str, FileDelta]]) -> dict[str, tuple[str, int]]:
    """deltas: [(source_label, FileDelta), ...], base first, overlays after,
    in application order. Returns {normalized_name: (display_name, count)}.
    Raises ScenarioCountError on any dangling reference or collision --
    never silently drops or double-counts a requirement."""
    composed: dict[str, tuple[str, int]] = {}
    findings: list[str] = []
    for idx, (label, delta) in enumerate(deltas):
        if idx == 0:
            if delta.modified or delta.removed or delta.renamed:
                findings.append(f"{label}: base file carries MODIFIED/REMOVED/RENAMED sections")
            for req in delta.added:
                key = normalize_name(req.name)
                if key in composed:
                    findings.append(f"{label}: duplicate base requirement name {req.name!r}")
                    continue
                composed[key] = (req.name, req.scenario_count)
            continue
        # Overlay application order per the OpenSpec archive convention:
        # RENAMED, REMOVED, MODIFIED, ADDED.
        for old, new in delta.renamed:
            key_old = normalize_name(old)
            if key_old not in composed:
                findings.append(f"{label}: RENAMED FROM {old!r} not found in composition")
                continue
            _display, count = composed.pop(key_old)
            key_new = normalize_name(new)
            if key_new in composed:
                findings.append(f"{label}: RENAMED TO {new!r} collides with an existing requirement")
                composed[key_old] = (_display, count)
                continue
            composed[key_new] = (new, count)
        for name in delta.removed:
            key = normalize_name(name)
            if key not in composed:
                findings.append(f"{label}: REMOVED {name!r} not found in composition")
                continue
            del composed[key]
        for req in delta.modified:
            key = normalize_name(req.name)
            if key not in composed:
                findings.append(f"{label}: MODIFIED {req.name!r} has no predecessor in composition")
                continue
            composed[key] = (req.name, req.scenario_count)  # REPLACE, never add.
        for req in delta.added:
            key = normalize_name(req.name)
            if key in composed:
                findings.append(f"{label}: ADDED {req.name!r} collides with an existing requirement")
                continue
            composed[key] = (req.name, req.scenario_count)
    if findings:
        raise ScenarioCountError("composition findings:\n" + "\n".join(f"  - {f}" for f in findings))
    return composed


def _assert_composed_agree(
    composed_1: dict[str, tuple[str, int]],
    composed_2: dict[str, tuple[str, int]],
    label_1: str,
    label_2: str,
) -> None:
    if composed_1 == composed_2:
        return
    keys_1, keys_2 = set(composed_1), set(composed_2)
    diffs: list[str] = []
    for key in sorted(keys_1 - keys_2):
        diffs.append(f"only in {label_1}: {composed_1[key][0]!r} ({composed_1[key][1]} scenarios)")
    for key in sorted(keys_2 - keys_1):
        diffs.append(f"only in {label_2}: {composed_2[key][0]!r} ({composed_2[key][1]} scenarios)")
    for key in sorted(keys_1 & keys_2):
        if composed_1[key] != composed_2[key]:
            diffs.append(f"{key!r}: {label_1}={composed_1[key]!r} vs {label_2}={composed_2[key]!r}")
    raise ScenarioCountError(
        f"the two counting methods disagree ({label_1} vs {label_2}):\n" + "\n".join(f"  - {d}" for d in diffs)
    )


# --------------------------------------------------------------------------
# Discovery and top-level composition build.
# --------------------------------------------------------------------------

def discover_composition_files(root: Path) -> list[Path]:
    pattern = f"openspec/changes/*/specs/{SPEC_CAPABILITY}/spec.md"
    candidates = sorted(root.glob(pattern))
    if not candidates:
        raise ScenarioCountError(f"no spec.md files found under {pattern} (rooted at {root})")
    bases: list[Path] = []
    overlays: list[Path] = []
    for p in candidates:
        text = p.read_text(encoding="utf-8")
        kinds = {m.group(1) for m in SECTION_HEADER_RE.finditer(text)}
        if not kinds:
            raise ScenarioCountError(f"{p}: no recognized '## ... Requirements' section found")
        if kinds & {"MODIFIED", "REMOVED", "RENAMED"}:
            overlays.append(p)
        elif kinds == {"ADDED"}:
            bases.append(p)
        else:
            raise ScenarioCountError(f"{p}: unrecognized section shape {sorted(kinds)}")
    if len(bases) != 1:
        raise ScenarioCountError(
            f"expected exactly one base spec.md under {pattern}, found {len(bases)}: "
            f"{[str(b) for b in bases]}"
        )
    if len(overlays) != 1:
        raise ScenarioCountError(
            f"expected exactly one overlay spec.md under {pattern} (this script refuses to guess "
            f"a composition order for more than one overlay), found {len(overlays)}: "
            f"{[str(o) for o in overlays]}"
        )
    return [bases[0], overlays[0]]


@dataclass
class CompositionResult:
    files: list[str]
    per_file: list[tuple[str, FileDelta, FileDelta]]  # label, method-1 delta, method-2 delta
    per_requirement: dict[str, tuple[str, int]]
    total: int


def build_composition(root: Path) -> CompositionResult:
    files = discover_composition_files(root)
    per_file: list[tuple[str, FileDelta, FileDelta]] = []
    deltas_1: list[tuple[str, FileDelta]] = []
    deltas_2: list[tuple[str, FileDelta]] = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        label = f.relative_to(root).as_posix()
        d1 = parse_regex(text, label)
        d2 = parse_manual(text, label)
        per_file.append((label, d1, d2))
        deltas_1.append((label, d1))
        deltas_2.append((label, d2))
    composed_1 = compose(deltas_1)
    composed_2 = compose(deltas_2)
    _assert_composed_agree(composed_1, composed_2, "method 1 (regex)", "method 2 (manual scan)")
    total = sum(count for _name, count in composed_1.values())
    return CompositionResult(
        files=[f.relative_to(root).as_posix() for f in files],
        per_file=per_file,
        per_requirement=composed_1,
        total=total,
    )


def read_status_assertion(root: Path) -> tuple[int, int]:
    path = root / STATUS_PAGE_REL
    if not path.is_file():
        raise ScenarioCountError(f"missing {STATUS_PAGE_REL} at {root}")
    data = path.read_bytes()
    m = STATUS_FIGURE_RE.search(data)
    if not m:
        raise ScenarioCountError(
            f"could not find 'N requirements and N scenarios in the effective composition' "
            f"sentence in {path}"
        )
    return int(m.group(1)), int(m.group(2))


# --------------------------------------------------------------------------
# --with-proposed: apply a candidate package's proposed/*.patch files in a
# scratch copy. The tracked tree is never touched.
# --------------------------------------------------------------------------

def _run_git_apply(cwd: Path, patch_file: Path, check_only: bool) -> None:
    args = ["git", "apply", "--whitespace=nowarn"]
    if check_only:
        args.append("--check")
    args.append(str(patch_file))
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise ScenarioCountError(
            f"git apply {'--check ' if check_only else ''}failed for {patch_file.name}:\n"
            f"{result.stdout}{result.stderr}"
        )


def _patch_target_path(patch_file: Path) -> str:
    for line in patch_file.read_text(errors="replace").splitlines():
        if line.startswith("+++ b/"):
            return line[len("+++ b/"):]
        if line.startswith("+++ "):
            candidate = line[4:]
            return candidate[2:] if candidate.startswith("b/") else candidate
    raise ScenarioCountError(f"could not find a patch target line in {patch_file}")


@contextlib.contextmanager
def with_proposed_scratch(root: Path, package_dir: Path):
    proposed = package_dir / "proposed"
    if not proposed.is_dir():
        raise ScenarioCountError(f"no 'proposed' directory under {package_dir}")
    patch_files = sorted(proposed.glob("*.patch"))
    if not patch_files:
        raise ScenarioCountError(f"no *.patch files found under {proposed}")
    comp_files = discover_composition_files(root)
    targets = {_patch_target_path(p) for p in patch_files}
    needed = {f.relative_to(root).as_posix() for f in comp_files} | {STATUS_PAGE_REL} | targets
    with tempfile.TemporaryDirectory(prefix="polaris-scenario-recount-") as tmp:
        scratch = Path(tmp)
        for rel in sorted(needed):
            src = root / rel
            if not src.is_file():
                continue  # a patch creating a brand-new file: nothing to seed
            dest = scratch / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(src.read_bytes())
        for pf in patch_files:
            _run_git_apply(scratch, pf, check_only=True)
        for pf in patch_files:
            _run_git_apply(scratch, pf, check_only=False)
        yield scratch


# --------------------------------------------------------------------------
# Reporting.
# --------------------------------------------------------------------------

def render_report(result: CompositionResult, label: str) -> str:
    lines = [f"Composition ({label}):"]
    for f in result.files:
        lines.append(f"  - {f}")
    lines.append("")
    lines.append("Per-file raw counts (before composition; MODIFIED/ADDED scenario tallies only):")
    for file_label, d1, _d2 in result.per_file:
        added_n = sum(r.scenario_count for r in d1.added)
        modified_n = sum(r.scenario_count for r in d1.modified)
        lines.append(
            f"  {file_label}: ADDED {len(d1.added)} requirements/{added_n} scenarios, "
            f"MODIFIED {len(d1.modified)} requirements/{modified_n} scenarios, "
            f"REMOVED {len(d1.removed)}, RENAMED {len(d1.renamed)}"
        )
    lines.append("")
    lines.append(f"Per-requirement composed scenario counts ({len(result.per_requirement)} requirements):")
    for _key, (name, count) in sorted(result.per_requirement.items()):
        lines.append(f"  {count:3d}  {name}")
    lines.append("")
    lines.append(f"TOTAL: {len(result.per_requirement)} requirements, {result.total} scenarios")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# selftest: rule-6 mutation fixtures, each built in an isolated temp dir.
# --------------------------------------------------------------------------

GOOD_BASE_SPEC = """# Fixture base capability

## ADDED Requirements

### Requirement: Alpha

Alpha body.

#### Scenario: A1

- **WHEN** one
- **THEN** two

#### Scenario: A2

- **WHEN** one
- **THEN** two

### Requirement: Beta

Beta body.

#### Scenario: B1

- **WHEN** one
- **THEN** two

### Requirement: Gamma

Gamma body.

#### Scenario: G1

- **WHEN** one
- **THEN** two
"""

GOOD_OVERLAY_SPEC = """# Fixture overlay

## RENAMED Requirements
- FROM: `### Requirement: Gamma`
- TO: `### Requirement: Gamma Prime`

## REMOVED Requirements

### Requirement: Beta

(no longer needed)

## MODIFIED Requirements

### Requirement: Alpha

Alpha modified body.

#### Scenario: A1

- **WHEN** one
- **THEN** two (modified)

## ADDED Requirements

### Requirement: Delta

Delta body.

#### Scenario: D1

- **WHEN** one
- **THEN** two

#### Scenario: D2

- **WHEN** one
- **THEN** two
"""

# Composed: Alpha(1, replaced) + Gamma Prime(1, renamed) + Delta(2, added) = 4
# scenarios over 3 requirements. Beta(1) is removed.
GOOD_TOTAL_SCENARIOS = 4
GOOD_TOTAL_REQUIREMENTS = 3

GOOD_STATUS_PAGE = (
    "# Fixture project status\n\n"
    f"Read the predecessor together with the overlay: {GOOD_TOTAL_REQUIREMENTS} requirements "
    f"and {GOOD_TOTAL_SCENARIOS} scenarios in the effective composition.\n"
)


def _write_good_fixture(base: Path) -> None:
    base_spec = base / "openspec/changes/fixture-base-change/specs/polaris-generation/spec.md"
    overlay_spec = base / "openspec/changes/fixture-overlay-change/specs/polaris-generation/spec.md"
    base_spec.parent.mkdir(parents=True, exist_ok=True)
    overlay_spec.parent.mkdir(parents=True, exist_ok=True)
    base_spec.write_text(GOOD_BASE_SPEC)
    overlay_spec.write_text(GOOD_OVERLAY_SPEC)
    (base / STATUS_PAGE_REL).write_text(GOOD_STATUS_PAGE)


def _check_totals(result: CompositionResult, status_reqs: int, status_scenarios: int, *, expect: int | None = None) -> None:
    expected = expect if expect is not None else status_scenarios
    if result.total != expected:
        raise ScenarioCountError(
            f"scenario total mismatch: recomputed {result.total}, expected {expected} "
            f"({'--expect override' if expect is not None else 'PROJECT-STATUS.md assertion'})"
        )
    if expect is None and len(result.per_requirement) != status_reqs:
        raise ScenarioCountError(
            f"requirement count mismatch: recomputed {len(result.per_requirement)}, "
            f"PROJECT-STATUS.md asserts {status_reqs}"
        )


def _run_check(root: Path, *, expect: int | None = None) -> tuple[CompositionResult, int, int]:
    result = build_composition(root)
    status_reqs, status_scenarios = read_status_assertion(root)
    _check_totals(result, status_reqs, status_scenarios, expect=expect)
    return result, status_reqs, status_scenarios


def _expect_fail(label: str, fn) -> None:
    try:
        fn()
    except ScenarioCountError:
        print(f"  [ok] {label}: check failed closed as expected")
        return
    raise ScenarioCountError(f"selftest fixture '{label}' did not fail: the check passed on a mutated input")


def selftest() -> None:
    print("Running rule-6 mutation fixtures (each must make the check fail closed)...")

    with tempfile.TemporaryDirectory(prefix="polaris-scenario-count-selftest-") as tmp:
        base = Path(tmp)

        # Sanity: the good fixture itself must pass, with the exact literal
        # totals hard-coded above (never imported from the module).
        good = base / "good"
        _write_good_fixture(good)
        result, status_reqs, status_scenarios = _run_check(good)
        if result.total != GOOD_TOTAL_SCENARIOS or len(result.per_requirement) != GOOD_TOTAL_REQUIREMENTS:
            raise ScenarioCountError(
                f"good fixture did not recompute the expected literal total: "
                f"got {len(result.per_requirement)} requirements / {result.total} scenarios, "
                f"expected {GOOD_TOTAL_REQUIREMENTS} / {GOOD_TOTAL_SCENARIOS}"
            )
        if (status_reqs, status_scenarios) != (GOOD_TOTAL_REQUIREMENTS, GOOD_TOTAL_SCENARIOS):
            raise ScenarioCountError("good fixture's own PROJECT-STATUS.md sentence did not parse as authored")
        print("  [ok] good fixture: recomputed total matches the hard-coded literal and PROJECT-STATUS.md")

        # Fixture 1: dropped scenario. Delete one '#### Scenario:' block from
        # the overlay's ADDED Delta requirement (which the composition keeps
        # verbatim); PROJECT-STATUS.md is left stating the old, now-stale
        # total. --check must catch the drift.
        f1 = base / "f1"
        _write_good_fixture(f1)
        overlay_path = f1 / "openspec/changes/fixture-overlay-change/specs/polaris-generation/spec.md"
        dropped = overlay_path.read_text().replace(
            "#### Scenario: D2\n\n- **WHEN** one\n- **THEN** two\n", ""
        )
        if dropped == overlay_path.read_text():
            raise ScenarioCountError("selftest setup error: dropped-scenario replacement made no change")
        overlay_path.write_text(dropped)
        _expect_fail("dropped scenario not reflected in a stale PROJECT-STATUS.md", lambda: _run_check(f1))

        # Fixture 2: MODIFIED double-count. A requirement is (erroneously)
        # listed under both MODIFIED and ADDED in the same overlay. If
        # compose() ever summed instead of raising, Alpha's scenarios would
        # be double-counted. The collision must be a fatal finding.
        f2 = base / "f2"
        _write_good_fixture(f2)
        overlay_path2 = f2 / "openspec/changes/fixture-overlay-change/specs/polaris-generation/spec.md"
        doubled = overlay_path2.read_text() + (
            "\n### Requirement: Alpha\n\nDuplicated erroneously.\n\n"
            "#### Scenario: A-dup\n\n- **WHEN** one\n- **THEN** two\n"
        )
        overlay_path2.write_text(doubled)
        _expect_fail("requirement double-listed under MODIFIED and ADDED", lambda: _run_check(f2))

        # Fixture 3: digit mismatch. Spec files are untouched; PROJECT-STATUS.md
        # states a scenario total inconsistent with the (correct) recount.
        f3 = base / "f3"
        _write_good_fixture(f3)
        status_path3 = f3 / STATUS_PAGE_REL
        status_path3.write_text(
            status_path3.read_text().replace(f"{GOOD_TOTAL_SCENARIOS} scenarios", "999 scenarios")
        )
        _expect_fail("PROJECT-STATUS.md digit inconsistent with the recount", lambda: _run_check(f3))

        # Fixture 4: disagreement between the two methods. Exercised directly
        # against the comparison primitive (bypassing text parsing, which
        # cannot itself be made to disagree on well-formed input without
        # reintroducing a parser bug) -- the fatal path in build_composition
        # must fire whenever the two independently-derived composed results
        # differ at all, in either direction.
        composed_a = {"alpha": ("Alpha", 2)}
        composed_b = {"alpha": ("Alpha", 3)}

        def _disagree():
            _assert_composed_agree(composed_a, composed_b, "method A", "method B")

        _expect_fail("the two counting methods disagree", _disagree)

        # Fixture 5: RENAMED FROM names a requirement absent from the
        # composition (a dangling reference must not be silently ignored).
        f5 = base / "f5"
        _write_good_fixture(f5)
        overlay_path5 = f5 / "openspec/changes/fixture-overlay-change/specs/polaris-generation/spec.md"
        overlay_path5.write_text(
            overlay_path5.read_text().replace(
                "- FROM: `### Requirement: Gamma`", "- FROM: `### Requirement: Nonexistent`"
            )
        )
        _expect_fail("RENAMED FROM names an absent requirement", lambda: _run_check(f5))

        # Fixture 6: discovery finds two overlays (ambiguous composition
        # order) and must refuse rather than guess.
        f6 = base / "f6"
        _write_good_fixture(f6)
        second_overlay = f6 / "openspec/changes/fixture-second-overlay/specs/polaris-generation/spec.md"
        second_overlay.parent.mkdir(parents=True, exist_ok=True)
        second_overlay.write_text(GOOD_OVERLAY_SPEC)
        _expect_fail("two overlays found (no derivable order)", lambda: build_composition(f6))

    print("selftest: all 7 checks failed closed (or passed, for the one good fixture) as expected.")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="compare the recomputed total to PROJECT-STATUS.md's digit (or --expect)")
    parser.add_argument("--expect", type=int, default=None, metavar="N", help="compare against N instead of PROJECT-STATUS.md's stated scenario total")
    parser.add_argument("--with-proposed", metavar="DIR", default=None, help="apply DIR/proposed/*.patch in a scratch copy before counting")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    try:
        if args.selftest:
            selftest()
            return 0

        if args.with_proposed:
            package_dir = Path(args.with_proposed)
            if not package_dir.is_absolute():
                package_dir = (ROOT / package_dir).resolve()
            with with_proposed_scratch(ROOT, package_dir) as scratch:
                result = build_composition(scratch)
                status_reqs, status_scenarios = read_status_assertion(scratch)
                label = f"scratch copy with {package_dir.relative_to(ROOT) if package_dir.is_relative_to(ROOT) else package_dir}'s proposed patches applied"
                print(render_report(result, label))
                print()
                print(f"(scratch) PROJECT-STATUS.md asserts: {status_reqs} requirements, {status_scenarios} scenarios")
        else:
            result = build_composition(ROOT)
            status_reqs, status_scenarios = read_status_assertion(ROOT)
            print(render_report(result, "tracked tree (HEAD)"))
            print()
            print(f"PROJECT-STATUS.md asserts: {status_reqs} requirements, {status_scenarios} scenarios")

        if args.check:
            _check_totals(result, status_reqs, status_scenarios, expect=args.expect)
            expected = args.expect if args.expect is not None else status_scenarios
            print(f"CHECK PASS: recomputed total {result.total} matches expected {expected}.")
    except ScenarioCountError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
