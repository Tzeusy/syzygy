#!/usr/bin/env python3
"""Build and verify the inert PWB release-label amendment candidate.

The amendment adds a release label to PWB-REQ-001 (bead ``syzygy-l362``):
Polaris names the observed revision by its nearest release tag, such as
"Butlers v1.0.23", and keeps the full Git object id beneath it as the identity
every claim binds to. It follows the tree-framing builder's form: the current
eleven-artifact PWB behavior package is bound by the tree-framing v1.0
sign-off. ``--check`` and ``--write`` therefore apply the candidate's
``proposed/*.patch`` files only in a scratch tree and hash those proposed
bytes. ``--apply --at-adoption`` is the one mode that writes signed subjects;
it exists for ``scripts/record_versioned_signoff.py`` after an owner's
version-tagged sign-off and refuses unless the whole package verifies. A
candidate commit, review, manifest or merge performs no owner act.

    --check      verify patches, structure, regeneration, coverage, siblings,
                 one result across every order of this and the pending
                 siblings' spec patches, and the manifest
    --selftest   rule-6 mutants: one per structure predicate (a sample of the
                 required phrases, not each one), plus patch drift, an
                 unclassified sibling, the pending patch population, and
                 divergent and failing application orders
    --write      regenerate the two derived patches (GOVERNING-DEPENDENCIES and
                 CONTRACT-COVERAGE) and the manifest over the proposed bytes
    --diff       print the proposed patches
    --apply --at-adoption   write the proposed bytes (sign-off change only)

Outside PWB-REQ-001, every requirement block and the text before the
requirements must survive byte for byte, and no signed line of the proposal,
the design, the capability table or the contract-coverage repair delta may be
lost, except the two capability count lines that ``capability_findings``
recomputes and the repair delta's two declared-totals lines, which the
contract-coverage generator's own ``--check`` recomputes.
"""

from __future__ import annotations

import argparse
import collections
import difflib
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_polaris_project_wide_spec_dependencies as dependencies  # noqa: E402
import pwb_requirement_amendment as orders  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
CANDIDATE = CANDIDATES / "pwb-release-label-amendment"
PROPOSED = CANDIDATE / "proposed"
MANIFEST = CANDIDATE / "PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt"
MANIFEST_OUT = MANIFEST
TITLE = "PWB RELEASE-LABEL BEHAVIOR AMENDMENT MANIFEST"
SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"
CAPABILITY = CHANGE / "CAPABILITY-COVERAGE.md"
DESIGN = CHANGE / "design.md"
PROPOSAL = CHANGE / "proposal.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"
COVERAGE_SCRIPT = pathlib.Path("scripts/build_polaris_project_wide_contract_coverage.py")
CONTRACT_INDEX = CANDIDATES / "05-CONTRACT-INDEX.yaml"
DECISIONS = pathlib.Path(".syzygy/governance/decisions")

BEHAVIOR_SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CAPABILITY,
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CONTRACT_COVERAGE,
            GOVERNING,
            CHANGE / "contract-coverage-matrix/RFC-0001-0003.md",
            CHANGE / "contract-coverage-matrix/RFC-0004-0006.md",
            CHANGE / "contract-coverage-matrix/RFC-0007-0009.md",
            DESIGN,
            PROPOSAL,
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
REPAIR_DELTA = CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md"
PATCHED = frozenset({CAPABILITY, REPAIR_DELTA, CONTRACT_COVERAGE, GOVERNING, DESIGN, PROPOSAL, SPEC})
#: Subjects whose proposed bytes are generated from the others, never authored.
DERIVED = frozenset({GOVERNING, CONTRACT_COVERAGE})

#: Every other candidate package whose spec patch targets the PWB spec, closed:
#: a sibling is either performed (its record exists in decisions/) or declined
#: (POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md). An unlisted
#: sibling fails the check; it may be a pending package this one must compose
#: with. Performed status is read from the record's existence only, which is
#: weaker than the tree-framing builder's patch-digest pin.
PERFORMED_SIBLINGS = {
    "pwb-container-shape-profile-amendment": "PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md",
    "pwb-dismissal-expiry-amendment": "PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md",
    "pwb-exact-source-render-mode-scenario": "PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md",
    "pwb-item-depth-amendment": "PWB-ITEM-DEPTH-AMENDMENT-SIGNOFF-v1.0.md",
    "pwb-machine-view-amendment": "PWB-MACHINE-VIEW-AMENDMENT-ACT.md",
    "pwb-missing-currency-disclosure-scenario": "PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md",
    "pwb-opening-band-scenario": "PWB-OPENING-BAND-SCENARIO-ACT.md",
    "pwb-readability-successor": "PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md",
    "pwb-tree-framing-amendment": "PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md",
}
DECLINED_SIBLINGS = frozenset({"pwb-scoped-attributes-amendment"})
#: Unsigned packages over the same subject. The class-granular extraction
#: amendment (M15, ``syzygy-dov.15.1``) touches PWB-REQ-002 and the reader
#: definitions, not PWB-REQ-001, but it also adds design decision 12 and
#: capability row 34, so whichever is signed second is regenerated over the
#: first's applied bytes and re-reviewed. The anchor-resolution amendment
#: (N9, ``syzygy-u05.9``) touches only PWB-REQ-014 and the generated
#: dependency declaration. The opening-index (PWB-REQ-010) and
#: accessible-name (PWB-REQ-016) amendments (``syzygy-u05.12``) each touch
#: one other requirement and the generated declaration only; their spec
#: patches compose with this one.
PENDING_SIBLINGS = frozenset({
    "pwb-accessible-name-amendment",
    "pwb-anchor-resolution-amendment",
    "pwb-class-granular-extraction-amendment",
    "pwb-opening-index-amendment",
})

REQ_001 = "PWB-REQ-001"
#: Load-bearing fragments of the proposed PWB-REQ-001 text. Each must occur
#: exactly once, whitespace-normalized.
REQUIRED_ONCE = (
    "Wherever Polaris names the observed revision, it SHALL lead with that revision's release label",
    "SHALL show the revision's full Git object id beneath the label, on the same surface and without expanding anything",
    "They are not a project-shape claim or fact, and they carry no epistemic tuple of their own.",
    "every claim, evaluation identity, link and comparison binds to it",
    "nothing binds to a tag name",
    "The captured tag set is every ref under `refs/tags/`",
    "Two deterministic evaluation inputs, each with an identity of its own, feed the label.",
    "no tag message or signature is read into the model or rendered",
    "A tag that peels to anything but a commit reaches no revision.",
    "It is complete only when every commit in that history was read",
    "The label takes exactly one of four forms.",
    "**Not read**, when the captured ancestry is incomplete.",
    "They are named in its inputs by evaluation identity",
    "It never states that the revision is untagged.",
    "the name of the reaching tag with the least distance",
    "every tied name is carried in the machine answer",
    "SHALL be disclosed as moved wherever a label names that tag",
    "Nothing presents a tag as unmoved.",
    "so every label value Polaris presents is recoverable from it",
    "Expected labels come from the checker's own Git listing of each fixture",
    "an uncaptured tag set or incomplete ancestry stated as untagged",
    "The count of those sites is the denominator.",
    "zero occurrences of the tag message",
)
#: Signed PWB-REQ-001 text the amendment keeps.
KEPT_IN_001 = (
    "WHEN the POC observes Butlers, it SHALL bind the complete source-path\n"
    "population to the configured repository's exact Git revision",
    "#### Scenario: Source population is complete at one revision",
)
NEW_SCENARIOS = (
    "#### Scenario: A tagged revision leads with its release label",
    "#### Scenario: A revision no tag reaches is labelled honestly",
    "#### Scenario: Unread tags are never shown as untagged",
    "#### Scenario: A moved tag is disclosed, not trusted",
)
#: Contracts PWB-REQ-001 must newly warrant; read from its warrants block.
WARRANT_CONTRACTS = frozenset({"RFC2-2", "RFC2-24"})
WARRANT_RE = re.compile(r"^  contracts: \[([^\]\n]*)\]$", re.MULTILINE)
REPAIR_ROWS = (
    "| RFC4-11.r1 | RFC4-11.c4 | RFC4-11 | A count over commit history is computed only from completely captured ancestry and is never reconstructed from history the adapter cannot reach | covered:PWB-REQ-001 |",
    "| RFC4-11.r2 | RFC4-11.c4 | RFC4-11 | Squash/deletion loss becomes reduced-fidelity PR facts | believed-not-applicable |",
)
REPAIR_TOTALS_LINES = (
    "Declared totals: **92 rows; 77 superseded base rows; 60 covered; 27 Unknown",
    "uncovered; 5 believed not applicable.**",
)
CAPABILITY_ROW = (
    "| 34 | Lead every human naming of the observed revision with its release "
    "label, keep the full object id beneath it as the identity claims bind to, "
    "disclose moved tags, and never state unread tags or incomplete history as untagged | "
    "covered — PWB-REQ-001 |"
)
CAPABILITY_COUNT_LINES = re.compile(r"^(?:Population: \d+ positive|Totals: )")
CAPABILITY_ROW_RE = re.compile(r"^\| (\d+) \| [^\n]* \| ([^|\n]+) \|$", re.MULTILINE)
TOTALS_RE = re.compile(
    r"^Totals: (\d+) covered, (\d+) lawfully out of scope, (\d+) Unknown/unresolved; (\d+) total\.$",
    re.MULTILINE,
)
POPULATION_RE = re.compile(r"^Population: (\d+) positive", re.MULTILINE)
PROPOSAL_PHRASE = "- **The revision reads as a release.**"
DESIGN_PHRASES = (
    "### 12. Name the revision by its release label",
    "until a registry amendment does, every label takes the not-read form.",
)

ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
DIFF_TARGET_RE = re.compile(r"^\+\+\+ b/(.+)$", re.MULTILINE)
SOURCE_RE = re.compile(r"^> Source: `spec\.md` sha256 `([0-9a-f]{64})` — ", re.MULTILINE)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def flat(text: str) -> str:
    return " ".join(text.split())


# --- proposed bytes ------------------------------------------------------------

def read_subjects() -> dict[pathlib.Path, bytes]:
    out: dict[pathlib.Path, bytes] = {}
    for rel in BEHAVIOR_SUBJECTS:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"missing PWB behavior subject: {rel}")
        out[rel] = path.read_bytes()
    return out


def patch_files() -> list[pathlib.Path]:
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda path: path.name)


def patch_target(patch: pathlib.Path) -> pathlib.Path:
    match = DIFF_TARGET_RE.search(patch.read_text(encoding="utf-8"))
    if match is None:
        raise ValueError(f"patch has no target: {patch.name}")
    return pathlib.Path(match.group(1))


def apply_patches(
    current: dict[pathlib.Path, bytes], patches: list[pathlib.Path]
) -> dict[pathlib.Path, bytes]:
    with tempfile.TemporaryDirectory() as temp:
        base = pathlib.Path(temp)
        for rel, body in current.items():
            target = base / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        for patch in patches:
            result = subprocess.run(
                ["git", "apply", "--whitespace=nowarn", str(patch)],
                cwd=base, capture_output=True, text=True,
            )
            if result.returncode != 0:
                raise ValueError(f"{patch.name} does not apply: {result.stderr.strip()}")
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def proposed_bytes(patches: list[pathlib.Path] | None = None) -> dict[pathlib.Path, bytes]:
    return apply_patches(read_subjects(), patch_files() if patches is None else patches)


def unified_patch(rel: pathlib.Path, before: bytes, after: bytes) -> str:
    rendered = "".join(
        difflib.unified_diff(
            before.decode("utf-8").splitlines(keepends=True),
            after.decode("utf-8").splitlines(keepends=True),
            fromfile=f"a/{rel.as_posix()}",
            tofile=f"b/{rel.as_posix()}",
            n=2,
        )
    )
    # Blank context lines stay prefix-free, as in the sibling PWB patches.
    return rendered.replace("\n \n", "\n\n")


def regenerate_governing_patch() -> str:
    semantic = [p for p in patch_files() if patch_target(p) not in DERIVED]
    proposed = proposed_bytes(patches=semantic)
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        raise ValueError("proposed spec warrants do not validate: " + " | ".join(errors))
    return unified_patch(GOVERNING, read_subjects()[GOVERNING], generated.encode())


# --- structure ---------------------------------------------------------------

def requirement_blocks(spec: str) -> tuple[str, list[tuple[str, str]]]:
    head, marker, body = spec.partition("\n## ADDED Requirements\n")
    if not marker:
        raise ValueError("spec has no ADDED Requirements section")
    parts = re.split(r"(?m)^(?=### Requirement: )", body)
    blocks = []
    for part in parts[1:]:
        match = re.match(r"### Requirement: (PWB-REQ-\d{3})", part)
        if match is None:
            raise ValueError("unparseable requirement heading")
        blocks.append((match.group(1), part))
    return head + marker + parts[0], blocks


def spec_findings(proposed: bytes, current: bytes) -> list[str]:
    try:
        new_head, new_blocks = requirement_blocks(proposed.decode("utf-8"))
        old_head, old_blocks = requirement_blocks(current.decode("utf-8"))
    except ValueError as error:
        return [str(error)]
    findings = []
    if new_head != old_head:
        findings.append("the specification text before the requirements changed")
    if [rid for rid, _ in new_blocks] != [rid for rid, _ in old_blocks]:
        return findings + ["requirement population or order differs"]
    old = dict(old_blocks)
    for rid, block in new_blocks:
        if rid != REQ_001 and block != old[rid]:
            findings.append(f"{rid} changed; the amendment touches only PWB-REQ-001")
    block = dict(new_blocks)[REQ_001]
    text = flat(block)
    for phrase in REQUIRED_ONCE:
        count = text.count(flat(phrase))
        if count != 1:
            findings.append(f"PWB-REQ-001 carries {count} copies of required phrase: {phrase[:60]!r}")
    for phrase in KEPT_IN_001 + NEW_SCENARIOS:
        if block.count(phrase) != 1:
            findings.append(f"PWB-REQ-001 lacks exactly one: {phrase.splitlines()[0][:60]!r}")
    warrants = WARRANT_RE.search(block)
    cited = {item.strip() for item in warrants.group(1).split(",")} if warrants else set()
    missing = sorted(WARRANT_CONTRACTS - cited)
    if missing:
        findings.append(f"PWB-REQ-001 warrants omit {', '.join(missing)}")
    return findings


def lost_lines(old: str, new: str, skip=lambda line: False) -> list[str]:
    remaining = collections.Counter(new.split("\n"))
    lost = []
    for line in old.split("\n"):
        if skip(line):
            continue
        if remaining[line]:
            remaining[line] -= 1
        else:
            lost.append(line)
    return lost


def capability_findings(proposed: bytes, current: bytes) -> list[str]:
    new, old = proposed.decode("utf-8"), current.decode("utf-8")
    findings = []
    lost = lost_lines(old, new, lambda line: bool(CAPABILITY_COUNT_LINES.match(line)))
    if lost:
        findings.append(f"signed capability line edited or removed: {lost[0]!r}")
    if new.count(CAPABILITY_ROW) != 1:
        findings.append("capability row 34 for the release label is missing")
    rows = CAPABILITY_ROW_RE.findall(new)
    covered = sum(1 for _, d in rows if d.strip().startswith("covered"))
    scoped = sum(1 for _, d in rows if d.strip().startswith("lawfully out of scope"))
    unknown = len(rows) - covered - scoped
    totals = TOTALS_RE.search(new)
    population = POPULATION_RE.search(new)
    if totals is None or population is None:
        return findings + ["capability totals or population line missing"]
    printed = tuple(int(group) for group in totals.groups())
    if printed != (covered, scoped, unknown, len(rows)) or int(population.group(1)) != len(rows):
        findings.append(
            f"capability totals are not the computed figures ({covered}, {scoped}, {unknown}, {len(rows)})"
        )
    return findings


def repair_findings(proposed: bytes, current: bytes) -> list[str]:
    new, old = proposed.decode("utf-8"), current.decode("utf-8")
    findings = []
    lost = lost_lines(old, new, lambda line: line in REPAIR_TOTALS_LINES)
    if lost:
        findings.append(f"signed repair-delta line edited or removed: {lost[0]!r}")
    for row in REPAIR_ROWS:
        if new.count(row) != 1:
            findings.append(f"repair row missing: {row.split(' | ')[0][2:]}")
    return findings


def companion_findings(proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]) -> list[str]:
    findings = []
    for rel in (PROPOSAL, DESIGN):
        lost = lost_lines(current[rel].decode("utf-8"), proposed[rel].decode("utf-8"))
        if lost:
            findings.append(f"signed {rel.name} line edited or removed: {lost[0]!r}")
    if PROPOSAL_PHRASE not in proposed[PROPOSAL].decode("utf-8"):
        findings.append("proposal does not carry the release-label bullet")
    design = flat(proposed[DESIGN].decode("utf-8"))
    for phrase in DESIGN_PHRASES:
        if flat(phrase) not in design:
            findings.append(f"design lacks: {phrase[:60]!r}")
    return findings


def generated_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    text = proposed[GOVERNING].decode("utf-8")
    match = SOURCE_RE.search(text)
    if match is None:
        return ["proposed GOVERNING-DEPENDENCIES has no source digest"]
    if match.group(1) != sha256(proposed[SPEC]):
        return ["proposed GOVERNING-DEPENDENCIES does not name the proposed spec digest"]
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        return ["proposed specification warrants do not validate: " + " | ".join(errors)]
    if text != generated:
        return ["proposed GOVERNING-DEPENDENCIES differs from regeneration"]
    return []


def run_coverage(proposed: dict[pathlib.Path, bytes], *args: str) -> tuple[subprocess.CompletedProcess, bytes]:
    """Run the contract-coverage generator in a scratch mirror of the proposed bytes."""
    with tempfile.TemporaryDirectory() as temp:
        mirror = pathlib.Path(temp)
        for rel in (
            COVERAGE_SCRIPT,
            pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
            pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
            CONTRACT_INDEX,
        ):
            target = mirror / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)
        for rel, body in proposed.items():
            target = mirror / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        parent = pathlib.Path("openspec/changes/three-surface-poc-experience")
        shutil.copytree(ROOT / parent, mirror / parent)
        result = subprocess.run(
            [sys.executable, str(mirror / COVERAGE_SCRIPT), *args],
            cwd=mirror, capture_output=True, text=True,
        )
        return result, (mirror / CONTRACT_COVERAGE).read_bytes()


def coverage_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    """The contract-coverage generator's own --check over the proposed bytes."""
    result, _ = run_coverage(proposed, "--check")
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip().splitlines() or ["no output"]
        return ["contract-coverage --check fails over the proposed bytes: " + output[-1]]
    return []


def regenerate_coverage_patch() -> str:
    semantic = [p for p in patch_files() if patch_target(p) not in DERIVED]
    proposed = proposed_bytes(patches=semantic)
    proposed = {**proposed, GOVERNING: dependencies.generate(proposed[SPEC].decode("utf-8"))[0].encode()}
    result, generated = run_coverage(proposed)
    if result.returncode != 0:
        raise ValueError("contract-coverage generator failed: " + (result.stdout + result.stderr).strip())
    return unified_patch(CONTRACT_COVERAGE, read_subjects()[CONTRACT_COVERAGE], generated)


def structure_findings(
    proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]
) -> list[str]:
    return (
        spec_findings(proposed[SPEC], current[SPEC])
        + capability_findings(proposed[CAPABILITY], current[CAPABILITY])
        + repair_findings(proposed[REPAIR_DELTA], current[REPAIR_DELTA])
        + companion_findings(proposed, current)
        + generated_findings(proposed)
    )


# --- siblings and manifest ---------------------------------------------------

def sibling_findings(candidates: pathlib.Path | None = None) -> list[str]:
    candidates = candidates or ROOT / CANDIDATES
    findings = []
    for patch in sorted(candidates.glob("*/proposed/spec.md.patch")):
        name = patch.parent.parent.name
        if name == CANDIDATE.name:
            continue
        try:
            if patch_target(patch) != SPEC:
                continue
        except ValueError:
            continue
        if name in DECLINED_SIBLINGS or name in PENDING_SIBLINGS:
            continue
        record = PERFORMED_SIBLINGS.get(name)
        if record is None:
            findings.append(f"unclassified sibling package patches the PWB spec: {name}")
        elif not (ROOT / DECISIONS / record).is_file():
            findings.append(f"sibling {name} is listed performed but its record is missing: {record}")
    return findings


def pending_order_patches(
    candidates: pathlib.Path | None = None, mine: pathlib.Path | None = None
) -> list[tuple[str, pathlib.Path]]:
    """This spec patch, then each pending sibling's that exists, by name."""
    candidates = candidates or ROOT / CANDIDATES
    patches = [(CANDIDATE.name, mine or ROOT / PROPOSED / "spec.md.patch")]
    for name in sorted(PENDING_SIBLINGS):
        theirs = candidates / name / "proposed/spec.md.patch"
        if theirs.is_file():
            patches.append((name, theirs))
    return patches


def pending_order_findings(
    patches: list[tuple[str, pathlib.Path]] | None = None, spec_bytes: bytes | None = None,
    rel: pathlib.Path = SPEC,
) -> list[str]:
    """Every application order of the pending spec patches gives one spec.

    Two patches can each apply in either order and still differ, because
    ``git apply`` relocates a hunk whose context moved, and three can apply
    pairwise yet fail together; the shared engine's all-orders search sees both.
    """
    patches = pending_order_patches() if patches is None else patches
    spec_bytes = (ROOT / rel).read_bytes() if spec_bytes is None else spec_bytes
    return orders.all_orders_findings(spec_bytes, patches, rel)


def render_manifest(proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        f"# {TITLE}\n"
        "# Candidate: binds nothing until the owner signs off a version of this\n"
        "# package (OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md).\n"
        f"# {len(BEHAVIOR_SUBJECTS)} artifacts; rows sorted by codepoint path.\n"
        "# All rows take effect together or none do.\n"
        "# Rows hash PROPOSED bytes; signed openspec bytes remain unchanged.\n"
    )
    rows = "".join(f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in BEHAVIOR_SUBJECTS)
    return header + rows


def check(patches: list[pathlib.Path] | None = None) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    findings: list[str] = []
    patches = patch_files() if patches is None else patches
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != PATCHED or len(targets) != len(PATCHED):
        findings.append("patch targets differ from the closed seven-subject population")
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    current = read_subjects()
    for rel in BEHAVIOR_SUBJECTS:
        if (proposed[rel] != current[rel]) != (rel in PATCHED):
            findings.append(f"subject change does not match its declaration: {rel.as_posix()}")
    findings.extend(structure_findings(proposed, current))
    findings.extend(coverage_findings(proposed))
    findings.extend(sibling_findings())
    findings.extend(pending_order_findings())
    if not (ROOT / MANIFEST).is_file():
        findings.append(f"missing manifest: {MANIFEST}")
    elif (ROOT / MANIFEST).read_text(encoding="utf-8") != render_manifest(proposed):
        findings.append("manifest differs from deterministic proposed-byte regeneration")
    return findings, proposed


# --- selftest ----------------------------------------------------------------

def _replace(data: bytes, old: str, new: str) -> bytes:
    if old.encode("utf-8") not in data:
        raise AssertionError(f"selftest fixture matched nothing: {old[:60]!r}")
    return data.replace(old.encode("utf-8"), new.encode("utf-8"), 1)


def selftest() -> int:
    proposed = proposed_bytes()
    current = read_subjects()
    baseline = structure_findings(proposed, current)
    if baseline:
        print(f"SELFTEST FAILED: the package does not verify before mutation: {baseline}")
        return 1
    mutants = {
        "other requirement drift": (
            SPEC, _replace(proposed[SPEC], "### Requirement: PWB-REQ-002 — Every declared project-shape item is accounted for\n", "### Requirement: PWB-REQ-002 — Every declared project-shape item is counted\n"),
            "PWB-REQ-002 changed",
        ),
        "preamble drift": (
            SPEC, _replace(proposed[SPEC], "## Purpose\n", "## Purpose (amended)\n"),
            "the specification text before the requirements changed",
        ),
        "object id no longer beneath": (
            SPEC, _replace(proposed[SPEC], "and SHALL show the revision's full\n  Git object id beneath the label", "and MAY show the revision's full\n  Git object id near the label"),
            "PWB-REQ-001 carries 0 copies of required phrase",
        ),
        "unread shown as untagged": (
            SPEC, _replace(proposed[SPEC], "It never\n  states that the revision is untagged.", "It may\n  state that the revision is untagged."),
            "PWB-REQ-001 carries 0 copies of required phrase",
        ),
        "tag message read": (
            SPEC, _replace(proposed[SPEC], "no tag\n    message or signature is read into the model or rendered", "the tag\n    message is rendered"),
            "PWB-REQ-001 carries 0 copies of required phrase",
        ),
        "signed scenario dropped": (
            SPEC, _replace(proposed[SPEC], "#### Scenario: Source population is complete at one revision", "#### Scenario: Source population is complete"),
            "PWB-REQ-001 lacks exactly one",
        ),
        "new scenario dropped": (
            SPEC, _replace(proposed[SPEC], "#### Scenario: A moved tag is disclosed, not trusted", "#### Scenario: A moved tag"),
            "PWB-REQ-001 lacks exactly one",
        ),
        "warrant dropped": (
            SPEC, _replace(proposed[SPEC], "RFC2-1, RFC2-2, RFC2-24, RFC4-1", "RFC2-1, RFC2-2, RFC4-1"),
            "PWB-REQ-001 warrants omit RFC2-24",
        ),
        "ancestry limb dropped": (
            SPEC, _replace(proposed[SPEC], "  3. **Not read**, when the captured ancestry is incomplete.\n", ""),
            "PWB-REQ-001 carries 0 copies of required phrase",
        ),
        "repair row dropped": (
            REPAIR_DELTA, _replace(proposed[REPAIR_DELTA], REPAIR_ROWS[0] + "\n", ""),
            "repair row missing: RFC4-11.r1",
        ),
        "signed repair row edited": (
            REPAIR_DELTA, _replace(proposed[REPAIR_DELTA], "| RFC2-1.r2 | RFC2-1.c12 |", "| RFC2-1.r2 | RFC2-1.c13 |"),
            "signed repair-delta line edited or removed",
        ),
        "capability row dropped": (
            CAPABILITY, _replace(proposed[CAPABILITY], CAPABILITY_ROW + "\n", ""),
            "capability row 34 for the release label is missing",
        ),
        "capability totals drift": (
            CAPABILITY, _replace(proposed[CAPABILITY], "Totals: 28 covered", "Totals: 29 covered"),
            "capability totals are not the computed figures",
        ),
        "signed capability row edited": (
            CAPABILITY, _replace(proposed[CAPABILITY], "| 1 | Bind every source to one exact Butlers revision |", "| 1 | Bind every source to one Butlers revision |"),
            "signed capability line edited or removed",
        ),
        "signed proposal line edited": (
            PROPOSAL, _replace(proposed[PROPOSAL], "- **Every declared item is counted.**", "- **Items are counted.**"),
            "signed proposal.md line edited or removed",
        ),
        "proposal bullet dropped": (
            PROPOSAL, _replace(proposed[PROPOSAL], PROPOSAL_PHRASE, "- **The revision.**"),
            "proposal does not carry the release-label bullet",
        ),
        "design read-authority sentence dropped": (
            DESIGN, _replace(proposed[DESIGN], "every label takes\n  the not-read form.", "labels are read."),
            "design lacks",
        ),
        "signed design line edited": (
            DESIGN, _replace(proposed[DESIGN], "## Risks / Trade-offs", "## Risks"),
            "signed design.md line edited or removed",
        ),
        "dependency drift": (
            GOVERNING, _replace(proposed[GOVERNING], "PWB-REQ-001", "PWB-REQ-000"),
            "proposed GOVERNING-DEPENDENCIES differs from regeneration",
        ),
    }
    failed = 0
    for name, (rel, mutated, expected) in mutants.items():
        if mutated == proposed[rel]:
            print(f"SELFTEST FAILED: mutant {name!r} changed nothing")
            failed += 1
            continue
        findings = structure_findings({**proposed, rel: mutated}, current)
        if not any(finding.startswith(expected) for finding in findings):
            print(f"SELFTEST FAILED: mutant {name!r} gave {findings}, expected {expected!r}")
            failed += 1
    # Patch drift: a corrupted context line stops the spec patch applying.
    spec_patch = ROOT / PROPOSED / "spec.md.patch"
    with tempfile.TemporaryDirectory() as temp:
        drifted = pathlib.Path(temp) / "spec.md.patch"
        text = spec_patch.read_text(encoding="utf-8")
        drifted.write_text(text.replace("\n scope, capture instant and observer identity/version.", "\n scope and observer identity/version.", 1), encoding="utf-8")
        others = [p for p in patch_files() if p.name != "spec.md.patch"]
        findings, _ = check(others + [drifted])
        if not any("does not apply" in finding for finding in findings):
            print(f"SELFTEST FAILED: patch drift gave {findings}")
            failed += 1
        # An unclassified sibling that patches the PWB spec fails closed.
        fake = pathlib.Path(temp) / "candidates"
        (fake / "pwb-unlisted-sibling/proposed").mkdir(parents=True)
        (fake / "pwb-unlisted-sibling/proposed/spec.md.patch").write_text(
            f"--- a/{SPEC.as_posix()}\n+++ b/{SPEC.as_posix()}\n", encoding="utf-8")
        found = sibling_findings(fake)
        if found != ["unclassified sibling package patches the PWB spec: pwb-unlisted-sibling"]:
            print(f"SELFTEST FAILED: unclassified sibling gave {found}")
            failed += 1
        failed += order_selftest(pathlib.Path(temp) / "orders")
    if failed:
        return 1
    print(
        f"selftest: {len(mutants)} structure mutants, patch drift, an unclassified "
        "sibling, the pending patch population, and divergent and failing "
        "application orders all fail closed on their own predicates"
    )
    return 0


#: This package's spec patch first, then every pending sibling's, sorted.
ORDER_POPULATION = [
    "pwb-release-label-amendment",
    "pwb-accessible-name-amendment",
    "pwb-anchor-resolution-amendment",
    "pwb-class-granular-extraction-amendment",
    "pwb-opening-index-amendment",
]

#: The shared engine's order fixtures. Every pair applies in both orders, so
#: only an all-orders search fails them.
ORDER_FIXTURES = (
    ("divergent", orders.ORDER_FIXTURE_BASE, orders.ORDER_FIXTURE_PATCHES, [
        "pending spec patches give 2 different results across the 2! application orders",
    ]),
    ("failing", orders.ORDER_FIXTURE_TRIPLE_BASE, orders.ORDER_FIXTURE_TRIPLE, [
        "pending spec patches do not apply in every order: "
        "triple-relocating after [triple-first-copy, triple-second-copy]",
        "pending spec patches give 2 different results across the 3! application orders",
    ]),
)


def order_selftest(temp: pathlib.Path) -> int:
    """The order check covers this patch and every pending sibling's, fails
    divergent and failing orders, and ``check`` reports what it finds."""
    failed = 0
    fake = temp / "candidates"
    for name in sorted(PENDING_SIBLINGS | DECLINED_SIBLINGS | {"pwb-unlisted-sibling"}):
        (fake / name / "proposed").mkdir(parents=True)
        (fake / name / "proposed/spec.md.patch").write_text("", encoding="utf-8")
    population = [name for name, _ in pending_order_patches(fake)]
    if population != ORDER_POPULATION:
        print(f"SELFTEST FAILED: the pending patch population is {population}")
        failed += 1
    rel = pathlib.Path("fixture.txt")
    for label, base, hunks, expected in ORDER_FIXTURES:
        patches = orders._fixture_patches(temp, rel, hunks)
        found = pending_order_findings(patches, base, rel)
        if found != expected:
            print(f"SELFTEST FAILED: {label} application orders gave {found}")
            failed += 1
    original = globals()["pending_order_findings"]
    globals()["pending_order_findings"] = lambda *_args, **_kwargs: ["order-check sentinel"]
    try:
        findings, _ = check()
    finally:
        globals()["pending_order_findings"] = original
    if "order-check sentinel" not in findings:
        print(f"SELFTEST FAILED: check does not report the order check: {findings}")
        failed += 1
    return failed


# --- modes -------------------------------------------------------------------

def write() -> int:
    governing = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    governing.write_text(regenerate_governing_patch(), encoding="utf-8")
    coverage = ROOT / PROPOSED / "CONTRACT-COVERAGE.md.patch"
    coverage.write_text(regenerate_coverage_patch(), encoding="utf-8")
    (ROOT / MANIFEST).write_text(render_manifest(proposed_bytes()), encoding="utf-8")
    print(f"wrote the two derived patches and {MANIFEST}")
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is an adoption-time operation; pass --at-adoption "
            "only through the version-tagged sign-off recorder"
        )
        return 2
    findings, proposed = check()
    if findings or proposed is None:
        print("refusing to apply: package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    for rel in sorted(PATCHED, key=lambda path: path.as_posix()):
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
    if args.apply:
        return apply(args.at_adoption)
    if args.write:
        return write()
    if args.diff:
        for patch in patch_files():
            print(patch.read_text(encoding="utf-8"), end="")
        return 0
    if not args.check:
        print("refusing: choose --check, --selftest, --diff or --write")
        return 2
    findings, proposed = check()
    if findings:
        print("RELEASE-LABEL CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    _, blocks = requirement_blocks(proposed[SPEC].decode("utf-8"))
    scenarios = proposed[SPEC].decode("utf-8").count("\n#### Scenario: ")
    print(
        f"release-label candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects "
        f"({len(PATCHED)} patched); {len(blocks)} requirements, {scenarios} scenarios; "
        "structure, regeneration, contract coverage, sibling classification and pending-patch order verify"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
