#!/usr/bin/env python3
"""Build and verify the inert PWB class-granular extraction amendment candidate.

The amendment narrows PWB-REQ-002's "never a partial item set" contract from
the whole source to each class of a source (bead ``syzygy-dov.15.1``, move
M15, ruling P-82): one class's grammar failure no longer withholds the items
of the classes that read beside it, a heading a list or table row does not
enumerate is surfaced instead of skipped, and every population rule declares
whether it needs the root index read. It follows the release-label builder's
form: the current eleven-artifact PWB behavior package is bound by the
signed PWB sign-offs, so ``--check`` and ``--write`` apply the candidate's
``proposed/*.patch`` files only in a scratch tree and hash those proposed
bytes. ``--apply --at-adoption`` is the one mode that writes signed subjects;
it exists for ``scripts/record_versioned_signoff.py`` after an owner's
version-tagged sign-off and refuses unless the whole package verifies. A
candidate commit, review, manifest or merge performs no owner act.

    --check      verify patches, structure, regeneration, coverage, siblings
                 and the manifest
    --selftest   rule-6 mutants: one per structure predicate (a sample of the
                 required phrases, not each one), plus patch drift and an
                 unclassified sibling
    --write      regenerate the derived GOVERNING-DEPENDENCIES patch and the
                 manifest over the proposed bytes, refusing if CONTRACT-COVERAGE
                 would change
    --diff       print the proposed patches
    --apply --at-adoption   write the proposed bytes (sign-off change only)

Outside PWB-REQ-002 and the reader definitions, every requirement block and
the text before the reader definitions must survive byte for byte. Inside
them, every signed line must survive except the declared replaced lines, and
no signed line of the proposal, the design or the capability table may be
lost, except the two capability count lines that ``capability_findings``
recomputes.
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

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
CANDIDATE = CANDIDATES / "pwb-class-granular-extraction-amendment"
PROPOSED = CANDIDATE / "proposed"
MANIFEST = CANDIDATE / "PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-MANIFEST.txt"
TITLE = "PWB CLASS-GRANULAR EXTRACTION AMENDMENT MANIFEST"
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
PATCHED = frozenset({CAPABILITY, GOVERNING, DESIGN, PROPOSAL, SPEC})
#: Subjects whose proposed bytes are generated from the others, never authored.
#: CONTRACT-COVERAGE.md is not among them: no warrant or coverage row moves, so
#: its regeneration over the proposed bytes is byte-identical, and `--write`
#: refuses if it ever is not.
DERIVED = frozenset({GOVERNING})

#: Every other candidate package whose spec patch targets the PWB spec, closed:
#: a sibling is performed (its record exists in decisions/), declined
#: (POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md) or pending. An
#: unlisted sibling fails the check; it may be a pending package this one must
#: compose with. Performed status is read from the record's existence only.
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
#: Unsigned packages over the same subject. Each touches other requirements,
#: but both add design decision 12 and capability row 34, so whichever is
#: signed second is regenerated over the first's applied bytes and re-reviewed.
PENDING_SIBLINGS = frozenset({"pwb-release-label-amendment"})

REQ_002 = "PWB-REQ-002"
READER_MARK = "\nReader definitions:\n"
#: Load-bearing fragments of the proposed reader definitions. Each must occur
#: exactly once, whitespace-normalized.
READER_REQUIRED_ONCE = (
    "Each rule declares whether it needs the root index read, and every source carries the name of the rule that admitted it.",
    "The flag belongs to the rule; a loaded profile sets it for each tree population it declares.",
    "The pillar-root and pillar-index rules need the root index; the baseline-spec and roster rules, whose path patterns these definitions write, do not.",
    "When the root index was not read, a rule that needs it mints no item",
    "the pillar rules name no source without the root index, so they admit none",
    "When the root index was not read, a rule that does not need it still admits its sources",
    "every class and category item denominator, and every source-path population total, that counts one of them states that it was derived without a read root index",
    "it fails the class whose row it reads, in that source",
    "a heading at that level that no row of the source's grammar declares is an unenumerated heading",
    "An unenumerated heading mints no item and fails nothing",
    "It is surfaced, never skipped",
    "with the reason unenumerated-heading and the count of such headings",
    "a tree population that does not declare it needs the root index",
    "Each class a source is assigned is read on its own.",
    "the class yields none of its items from that source. A class that fails never produces a partial item set;",
    "an unenumerated heading is not a failure, and the items it leaves in place are complete for the headings the row declares.",
    "A source in which a class fails keeps every other class it is assigned",
    "partially extracted, and states for each class either its items and denominator or its failure and reason",
    "A source's own item denominator is Unknown whenever any class it is assigned has an Unknown item denominator in it, for any reason",
    "is extracted, not partially extracted, and its own item denominator is still Unknown",
    "A class's item denominator across its sources, and its category's, is Unknown whenever the class is Unknown in any of those sources",
    "has no class that reads: every class it is assigned has an Unknown item denominator in it.",
)
#: Each of Butlers' two tree populations declares it does not need the root index.
READER_TREE_PHRASE = "its tree population does not need the root index"
#: Signed reader-definition lines the amendment replaces, and nothing else.
READER_REPLACED = (
    "    `<key>` segment is a single directory name.",
    "  - A missing heading, malformed row/list/TOML, unexpected duplicate key or",
    "    ambiguous leading label makes the enclosing source's item denominator",
    "    Unknown; it never produces a partial item set.",
    "    openspec/specs/<one-directory>/spec.md; the one directory is the key.",
    "    `[butler].name` must be non-empty.",
)
#: Load-bearing fragments of the proposed PWB-REQ-002 text.
REQ_REQUIRED_ONCE = (
    "Each class of a source SHALL be accounted for on its own",
    "SHALL leave its own item denominator there Unknown without withholding the items of any other class the source reads",
    "a source with a class whose item denominator is Unknown SHALL leave its own item denominator Unknown",
    "an unenumerated heading SHALL be surfaced, never skipped",
    "a count derived without a read root index SHALL say so wherever it is shown",
    "a source assigned three classes in which one class fails and two read",
    "holds a tenth level-3 heading",
    "an observation whose root index was not read",
    "each partially extracted source's per-class outcome, each unenumerated heading with its anchor and route, and each root-index qualification",
    "The comparison is made per source and class",
    "a failed class's D is Unknown while each sibling's D is known",
    "each source with a class whose D is Unknown has its own D Unknown",
    "an independent scan of each enclosing section finds every unenumerated heading, the count per source and class equals the count the answer gives",
    "every source names the rule that an independent derivation of the source-path population admits it under",
    "a failed class emits a partial population",
    "a failed class withholds the items of a sibling class that reads",
    "a class or category item denominator that counts a failed class or an unenumerated heading is presented as known",
    "a source with a class whose item denominator is Unknown presents its own item denominator as known",
    "an unenumerated heading is skipped or mints an item or is miscounted",
    "a source names no rule or a rule other than the one that admitted it",
    "a count derived without a read root index is shown without that qualification",
    "the failed class's item denominator in that source, its class's and its category's item denominators render Unknown with the failure's reason",
    "and the V1 index's own item denominator, render Unknown with the reason unenumerated-heading",
    "nor does any source of a loaded profile's tree population that does not declare `rootIndexRequired`",
    "every admitted source names the rule that admitted it",
    "a rule that needs the root index mints an item when it was not read",
)
#: Signed PWB-REQ-002 lines the amendment replaces, and nothing else.
REQ_REPLACED = (
    "- **Falsifier**: the independent extractors disagree, a malformed source emits",
    "  a partial population, a known source disappears, an admitted item appears twice or",
    "  loaded profile.",
    "- **Observable**: per-category identities and reconciling counts are visible in",
    "  the machine answer and reachable from Polaris.",
    "  denominator.",
)
KEPT_SCENARIOS = (
    "#### Scenario: Declared shape reconciles",
    "#### Scenario: Butlers' profile reproduces the written grammar",
    "#### Scenario: Loaded profile gives one class no row",
    "#### Scenario: Loaded profile names a shape outside the vocabulary",
    "#### Scenario: Refused or unread Butlers profile does not fall back",
    "#### Scenario: Project with no profile has Unknown item denominators",
)
NEW_SCENARIOS = (
    "#### Scenario: A failing class keeps its siblings",
    "#### Scenario: An unenumerated heading is surfaced, not skipped",
    "#### Scenario: Counts derived without a read root index say so",
)
WARRANTS_002 = (
    "```yaml\nwarrants:\n  primary: VIS-2\n  doctrine: [VIS-1, VIS-2, VIS-7]\n"
    "  contracts: [RFC1-14, RFC2-23, RFC6-16, RFC6-17, RFC7-15]\n"
    "  policies: [CC-SPEC-4, CC-SPEC-11, CC-TEST-5, CC-TEST-6]\n"
)
CAPABILITY_ROW_33 = (
    "| 33 | Open each group of Syzygy-authored framing with its model-derived "
    "answer, keep Butlers text verbatim beneath it, and draw supported "
    "relationships as allow-listed static SVG with a text equivalent, "
    "disclosing unsupported ones | covered — PWB-REQ-014 |"
)
CAPABILITY_ROW = (
    "| 34 | Account for each class of a source on its own: a failing class "
    "leaves only itself Unknown, a heading the grammar does not enumerate is "
    "surfaced rather than skipped, and a count made without a read root index "
    "says so | covered — PWB-REQ-002 |"
)
CAPABILITY_COUNT_LINES = re.compile(r"^(?:Population: \d+ positive|Totals: )")
CAPABILITY_ROW_RE = re.compile(r"^\| (\d+) \| [^\n]* \| ([^|\n]+) \|$", re.MULTILINE)
TOTALS_RE = re.compile(
    r"^Totals: (\d+) covered, (\d+) lawfully out of scope, (\d+) Unknown/unresolved; (\d+) total\.$",
    re.MULTILINE,
)
POPULATION_RE = re.compile(r"^Population: (\d+) positive", re.MULTILINE)
PROPOSAL_PHRASE = "  - Each class of a source is read on its own:"
DESIGN_PHRASES = (
    "### 12. Read each class of a source on its own",
    "- **Root independence.** Rules 1 and 2 need the root index read;",
    "*partially extracted*",
    "No `catalog-count` declaration is minted for it; that family stays closed at nine.",
    "Butlers' baseline-spec and roster rules declare that they do not need it, so its manifest admits the same sources as before.",
)

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


def once_findings(where: str, text: str, phrases: tuple[str, ...]) -> list[str]:
    flattened = flat(text)
    return [
        f"{where} carries {flattened.count(flat(phrase))} copies of required phrase: {phrase[:60]!r}"
        for phrase in phrases
        if flattened.count(flat(phrase)) != 1
    ]


def spec_findings(proposed: bytes, current: bytes) -> list[str]:
    try:
        new_head, new_blocks = requirement_blocks(proposed.decode("utf-8"))
        old_head, old_blocks = requirement_blocks(current.decode("utf-8"))
    except ValueError as error:
        return [str(error)]
    findings = []
    new_pre, mark, new_reader = new_head.partition(READER_MARK)
    old_pre, _, old_reader = old_head.partition(READER_MARK)
    if not mark or new_pre != old_pre:
        findings.append("the specification text before the reader definitions changed")
    lost = [line for line in lost_lines(old_reader, new_reader) if line not in READER_REPLACED]
    if lost:
        findings.append(f"signed reader-definition line edited or removed: {lost[0]!r}")
    findings.extend(once_findings("the reader definitions", new_reader, READER_REQUIRED_ONCE))
    if flat(new_reader).count(READER_TREE_PHRASE) != 2:
        findings.append("the reader definitions do not exempt exactly Butlers' two tree populations")
    if [rid for rid, _ in new_blocks] != [rid for rid, _ in old_blocks]:
        return findings + ["requirement population or order differs"]
    old = dict(old_blocks)
    for rid, block in new_blocks:
        if rid != REQ_002 and block != old[rid]:
            findings.append(f"{rid} changed; the amendment touches only PWB-REQ-002")
    block = dict(new_blocks)[REQ_002]
    lost = [line for line in lost_lines(old[REQ_002], block) if line not in REQ_REPLACED]
    if lost:
        findings.append(f"signed PWB-REQ-002 line edited or removed: {lost[0]!r}")
    findings.extend(once_findings("PWB-REQ-002", block, REQ_REQUIRED_ONCE))
    for phrase in KEPT_SCENARIOS + NEW_SCENARIOS:
        if block.count(phrase) != 1:
            findings.append(f"PWB-REQ-002 lacks exactly one: {phrase[:60]!r}")
    if block.count(WARRANTS_002) != 1:
        findings.append("PWB-REQ-002 warrants changed")
    return findings


def capability_findings(proposed: bytes, current: bytes) -> list[str]:
    new, old = proposed.decode("utf-8"), current.decode("utf-8")
    findings = []
    lost = lost_lines(old, new, lambda line: bool(CAPABILITY_COUNT_LINES.match(line)))
    if lost:
        findings.append(f"signed capability line edited or removed: {lost[0]!r}")
    if new.count(CAPABILITY_ROW) != 1:
        findings.append("capability row 34 for class-granular extraction is missing")
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


def companion_findings(proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]) -> list[str]:
    findings = []
    for rel in (PROPOSAL, DESIGN):
        lost = lost_lines(current[rel].decode("utf-8"), proposed[rel].decode("utf-8"))
        if lost:
            findings.append(f"signed {rel.name} line edited or removed: {lost[0]!r}")
    if PROPOSAL_PHRASE not in proposed[PROPOSAL].decode("utf-8"):
        findings.append("proposal does not carry the class-granular bullet")
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
    proposed = proposed_bytes(patches=[p for p in patch_files() if patch_target(p) not in DERIVED])
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
        findings.append("patch targets differ from the closed five-subject population")
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
    spec = proposed[SPEC]
    mutants = {
        "other requirement drift": (
            SPEC, _replace(spec, "### Requirement: PWB-REQ-003 — Missing, unreadable and excluded sources remain visible\n", "### Requirement: PWB-REQ-003 — Missing sources remain visible\n"),
            "PWB-REQ-003 changed",
        ),
        "preamble drift": (
            SPEC, _replace(spec, "## Purpose\n", "## Purpose (amended)\n"),
            "the specification text before the reader definitions changed",
        ),
        "signed reader line edited": (
            SPEC, _replace(spec, "  - Narrative links do not recurse.\n", "  - Narrative links recurse once.\n"),
            "signed reader-definition line edited or removed",
        ),
        "whole-source discard restored": (
            SPEC, _replace(spec, "keeps every other class it is assigned", "keeps no other class it is assigned"),
            "the reader definitions carries 0 copies of required phrase",
        ),
        "partial class set allowed": (
            SPEC, _replace(spec, "A\n    class that fails never produces a partial item set;", "A\n    class that fails may produce a partial item set;"),
            "the reader definitions carries 0 copies of required phrase",
        ),
        "unenumerated heading skipped": (
            SPEC, _replace(spec, "It is surfaced, never skipped:", "It is skipped:"),
            "the reader definitions carries 0 copies of required phrase",
        ),
        "tree flag default flipped": (
            SPEC, _replace(spec, "a tree population that does not declare it needs the root\n    index.", "a tree population that does not declare it does not need\n    the root index."),
            "the reader definitions carries 0 copies of required phrase",
        ),
        "roster exemption dropped": (
            SPEC, _replace(spec, "must be non-empty; its tree population does not need the\n    root index.", "must be non-empty."),
            "the reader definitions do not exempt exactly Butlers' two tree populations",
        ),
        "falsifier limb dropped": (
            SPEC, _replace(spec, "a failed class withholds the items of a sibling class\n  that reads, ", ""),
            "PWB-REQ-002 carries 0 copies of required phrase",
        ),
        "per-class oracle dropped": (
            SPEC, _replace(spec, "The comparison is made per source and class:", "The comparison is made per source:"),
            "PWB-REQ-002 carries 0 copies of required phrase",
        ),
        "category clause dropped": (
            SPEC, _replace(spec, "across its sources, and its category's, is", "across its sources is"),
            "the reader definitions carries 0 copies of required phrase: \"A class's item denominator across",
        ),
        "root admission inverted": (
            SPEC, _replace(spec, "a rule that does not need it still\n    admits its sources", "a rule that does not need it mints\n    no item"),
            "the reader definitions carries 0 copies of required phrase: 'When the root index was not read, a rule that does not need",
        ),
        "population total unqualified": (
            SPEC, _replace(spec, "and\n    every source-path population total, that", "that"),
            "the reader definitions carries 0 copies of required phrase: 'every class and category item denominator, and every",
        ),
        "rule provenance dropped": (
            SPEC, _replace(spec, ", and every\n    source carries the name of the rule that admitted it.", "."),
            "the reader definitions carries 0 copies of required phrase: 'Each rule declares whether",
        ),
        "source denominator rule dropped": (
            SPEC, _replace(spec, "A source's own item denominator is Unknown whenever", "A source's own item denominator is known whenever"),
            "the reader definitions carries 0 copies of required phrase: \"A source's own item denominator is Unknown",
        ),
        "source denominator SHALL dropped": (
            SPEC, _replace(spec, "a source with a\nclass whose item denominator is Unknown SHALL leave its own item denominator\nUnknown; ", ""),
            "PWB-REQ-002 carries 0 copies of required phrase: 'a source with a class whose item denominator is Unknown",
        ),
        "SHALL broadened": (
            SPEC, _replace(spec, "an unenumerated heading SHALL be surfaced", "a heading no grammar enumerates SHALL be surfaced"),
            "PWB-REQ-002 carries 0 copies of required phrase: 'an unenumerated heading SHALL",
        ),
        "denominator falsifier dropped": (
            SPEC, _replace(spec, "a class or category item denominator that counts a failed class\n  or an unenumerated heading is presented as known, ", ""),
            "PWB-REQ-002 carries 0 copies of required phrase: 'a class or category item denominator that counts",
        ),
        "qualification falsifier dropped": (
            SPEC, _replace(spec, "a count derived without a read root index is shown without\n  that qualification, ", ""),
            "PWB-REQ-002 carries 0 copies of required phrase: 'a count derived without a read root index is shown",
        ),
        "observable additions dropped": (
            SPEC, _replace(spec, ", together with each partially\n  extracted source's per-class outcome, each unenumerated heading with its\n  anchor and route, and each root-index qualification.", "."),
            "PWB-REQ-002 carries 0 copies of required phrase: \"each partially extracted source",
        ),
        "heading count oracle dropped": (
            SPEC, _replace(spec, "the count per source and class\n  equals the count the answer gives", "the count per source is shown"),
            "PWB-REQ-002 carries 0 copies of required phrase: 'an independent scan of each enclosing",
        ),
        "scenario category weakened": (
            SPEC, _replace(spec, "its class's\n  and its category's item denominators", "and its class's\n  item denominator"),
            "PWB-REQ-002 carries 0 copies of required phrase: \"the failed class's item denominator in that source",
        ),
        "signed PWB-REQ-002 line edited": (
            SPEC, _replace(spec, "Group: Coverage. Form: **invariant**.\n", "Group: Coverage. Form: **sweep**.\n"),
            "signed PWB-REQ-002 line edited or removed",
        ),
        "signed scenario dropped": (
            SPEC, _replace(spec, "#### Scenario: Loaded profile gives one class no row", "#### Scenario: Loaded profile gives a class no row"),
            "PWB-REQ-002 lacks exactly one",
        ),
        "new scenario dropped": (
            SPEC, _replace(spec, "#### Scenario: A failing class keeps its siblings", "#### Scenario: A failing class"),
            "PWB-REQ-002 lacks exactly one",
        ),
        "warrant dropped": (
            SPEC, _replace(spec, "  contracts: [RFC1-14, RFC2-23, RFC6-16, RFC6-17, RFC7-15]\n  policies: [CC-SPEC-4, CC-SPEC-11, CC-TEST-5, CC-TEST-6]\n", "  contracts: [RFC1-14, RFC6-16, RFC6-17, RFC7-15]\n  policies: [CC-SPEC-4, CC-SPEC-11, CC-TEST-5, CC-TEST-6]\n"),
            "PWB-REQ-002 warrants changed",
        ),
        "capability row dropped": (
            CAPABILITY, _replace(proposed[CAPABILITY], CAPABILITY_ROW + "\n", ""),
            "capability row 34 for class-granular extraction is missing",
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
            PROPOSAL, _replace(proposed[PROPOSAL], PROPOSAL_PHRASE, "  - Classes are read:"),
            "proposal does not carry the class-granular bullet",
        ),
        "design catalog-count sentence dropped": (
            DESIGN, _replace(proposed[DESIGN], "No `catalog-count` declaration is minted for it;", "A `catalog-count` declaration is minted for it;"),
            "design lacks",
        ),
        "signed design line edited": (
            DESIGN, _replace(proposed[DESIGN], "## Risks / Trade-offs", "## Risks"),
            "signed design.md line edited or removed",
        ),
        "dependency drift": (
            GOVERNING, _replace(proposed[GOVERNING], "PWB-REQ-002", "PWB-REQ-000"),
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
        mutated_text = text.replace("\n   - Narrative links do not recurse.", "\n   - Narrative links recurse.", 1)
        if mutated_text == text:
            print("SELFTEST FAILED: patch-drift fixture matched nothing")
            failed += 1
        drifted.write_text(mutated_text, encoding="utf-8")
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
    if failed:
        return 1
    print(
        f"selftest: {len(mutants)} structure mutants, patch drift and an unclassified "
        "sibling all fail closed on their own predicates"
    )
    return 0


# --- modes -------------------------------------------------------------------

def write() -> int:
    governing = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    governing.write_text(regenerate_governing_patch(), encoding="utf-8")
    if regenerate_coverage_patch():
        print("refusing: CONTRACT-COVERAGE.md would change; declare it a patched subject first")
        return 1
    (ROOT / MANIFEST).write_text(render_manifest(proposed_bytes()), encoding="utf-8")
    print(f"wrote the derived GOVERNING-DEPENDENCIES patch and {MANIFEST}")
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
        print("CLASS-GRANULAR CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    _, blocks = requirement_blocks(proposed[SPEC].decode("utf-8"))
    scenarios = proposed[SPEC].decode("utf-8").count("\n#### Scenario: ")
    print(
        f"class-granular candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects "
        f"({len(PATCHED)} patched); {len(blocks)} requirements, {scenarios} scenarios; "
        "structure, regeneration, contract coverage and sibling classification verify"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
