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
                 siblings' spec patches and of any companion subject a
                 pending sibling also patches, and the manifest
    --selftest   rule-6 mutants: one per structure predicate (a sample of the
                 required phrases, not each one), plus patch drift, an
                 unclassified sibling, the pending patch population,
                 divergent and failing application orders, a colliding
                 companion patch, and the lost-line guard against an
                 independent subsequence count
    --write      regenerate the two derived patches (GOVERNING-DEPENDENCIES and
                 CONTRACT-COVERAGE) and the manifest over the proposed bytes
    --diff       print the proposed patches
    --apply --at-adoption   write the proposed bytes (sign-off change only)

Outside PWB-REQ-001, every requirement block and the text before the
requirements must survive byte for byte. Inside it, every signed line must
survive, except its doctrine and contracts warrant lists, which may only grow.
No signed line of the proposal,
the design, the capability table or the contract-coverage repair delta may be
lost, except the two capability count lines that ``capability_findings``
recomputes and the repair delta's two declared-totals lines, which the
contract-coverage generator's own ``--check`` recomputes.
"""

from __future__ import annotations

import argparse
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
    # Signed v1.0 2026-10-14 (P-96); moved from pending by the sign-off change.
    "pwb-anchor-resolution-amendment": "PWB-ANCHOR-RESOLUTION-AMENDMENT-SIGNOFF-v1.0.md",
    # Signed v1.0 2026-10-14 (P-86); moved from pending by the sign-off change.
    "pwb-class-granular-extraction-amendment": "PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-SIGNOFF-v1.0.md",
    # Signed v1.0 2026-10-15 (P-99); moved from pending by the sign-off change.
    "pwb-accessible-name-amendment": "PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md",
    # Signed v1.0 2026-10-15 (P-98); moved from pending by the sign-off change.
    "pwb-opening-index-amendment": "PWB-OPENING-INDEX-AMENDMENT-SIGNOFF-v1.0.md",
}
DECLINED_SIBLINGS = frozenset({"pwb-scoped-attributes-amendment"})
#: Unsigned packages over the same subject. The class-granular extraction
#: amendment (M15, ``syzygy-dov.15.1``) touches PWB-REQ-002 and the reader
#: definitions, not PWB-REQ-001, but it also added design decision 12 and
#: capability row 34; it was signed first (2026-10-14), so this package was
#: regenerated over its applied bytes as decision 13 and row 35, and
#: ``companion_order_findings`` now composes the companion subjects too. The
#: anchor-resolution amendment
#: (N9, ``syzygy-u05.9``) was signed v1.0 on 2026-10-14 and is performed
#: above; this package's patches were regenerated over its applied bytes.
#: The opening-index (PWB-REQ-010) and
#: accessible-name (PWB-REQ-016) amendments (``syzygy-u05.12``) each touch
#: one other requirement and the generated declaration only; their spec
#: patches compose with this one. Both are now signed (P-99 and P-98,
#: 2026-10-15) and performed above, so no PWB sibling is pending.
PENDING_SIBLINGS: frozenset[str] = frozenset()

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
    "Nothing presents a tag as unmoved.",
    "so every label value Polaris presents is recoverable from it",
    "Expected labels come from the checker's own Git listing of each fixture",
    "an uncaptured tag set or incomplete ancestry stated as untagged",
    "The count of those sites is the denominator.",
    "zero occurrences of the tag message",
    # Round 2, Finding 1: one true statement per not-read test, and a
    # decide-line and falsifier limb that check it.
    'Its statement is "release tags were not read".',
    'Its statement is "the history needed to judge release tags was not read".',
    "beside the statement of the test that applied",
    "exact equality of form, statement, tag name, distance, tied names",
    "a not-read or untagged label whose statement is not its test's",
    # Round 2, Finding 2: a fixture whose captured history holds a reaching tag.
    "a shallow clone whose captured history holds a reaching tag",
    "a count of later commits computed from incomplete ancestry",
    # Round 2, Finding 3, re-repaired for round 3, Finding 1: a naming site is
    # a marked label unit; other visible ids are a separate prohibition with
    # marked exceptions (three in round 3, four since round 4).
    "Attribute values and link targets are not owner-visible text",
    "marked as a label unit, so that a checker finds it without judgment",
    "zero swept occurrences outside a label unit and the excepted elements",
    "Polaris names the observed revision only in a label unit, a naming being one that the text sweep below finds, and the excepted elements below the only exceptions.",
    "Every Polaris page SHALL present at least one label unit.",
    "Outside a label unit, owner-visible Polaris text SHALL NOT show",
    "Butlers-declared text that PWB-REQ-014 keeps verbatim in its own leaf",
    "at least one label unit on every Polaris page",
    # Round 4, Finding 1: a provenance stamp is decided structurally, from
    # its citation and the record its cite names, never from its mark; and
    # "the label leads" has its own observable.
    "what the checker reads decides each kind, never the mark alone",
    "a provenance stamp, the revision element of one citation.",
    "no letter or digit outside the cite's text and the stamp's",
    "The cite names, by its identity, one anchor the machine narrative serves or one source record the machine answer serves at the same evaluation",
    "the stamp's whole text is the revision that record carries, in full or as its first twelve hexadecimal digits",
    # Round 6, Finding 1 (owner: "Weaker wording + review"): "therefore never
    # a stamp" is withdrawn and both gaps are stated as limits.
    "Two limits stay. Where a citation or an excepted identity (below) sits is not decided by this requirement: a citation or an identity placed inside a sentence, a heading or other running text passes these tests, though its words then name the revision outside a label unit, an identity by the revision's full object id.",
    "Which tokens an anchor's served locator holds is not decided either: PWB-REQ-014's anchor shape requires a locator and fixes no values, so a one-token locator that reads as a phrase passes",
    "**AND** whether that citation or an excepted identity sits inside the sentence is not decided by this requirement",
    "**THEN** outside a citation and an excepted identity the sentence shows neither R's full object id nor its first twelve hexadecimal digits",
    # Round 7, Finding 2 (lead, cycle 6): an excepted identity's placement
    # is part of the first limit; Note 3: scenario 5's WHEN is guarded.
    "It shows that identity whole, and where it sits is the first limit above;",
    "**WHEN** a Polaris page has a sentence about the observed revision R outside every label unit - **THEN**",
    # Round 6, Note 1: the cycle-4 wordings the digest alone guarded.
    "It holds no occurrence that the text sweep below finds.",
    "holding no whitespace or equal to a path in the checker's own Git listing, and holding no swept occurrence",
    "holds whitespace and is not a path in the checker's own Git listing, or holds a swept occurrence",
    "So a stamp's citation holds only a served name with no space in it, or a real path, beside the revision.",
    "with no whitespace unless it is a path in R's tree, and R's id as its stamp",
    # Round 6, Note 3: a naming is what the sweep finds; a shorter prefix is
    # a stated gap.
    "These three are the namings the text sweep below finds, and \"names the observed revision\" means them: a shorter prefix of the object id is not decided by this requirement.",
    "Within each label unit the label precedes the full object id in document order.",
    "the first occurrence in document order that the text sweep below finds outside the operability status line lies in a label unit",
    "decides the kind from those alone",
    "the first swept occurrence outside the operability status line inside a label unit, and in each label unit the label before the full object id",
    "every provenance stamp inside a citation whose cite names one anchor or source record served at that evaluation",
    "No excepted element's kind is taken from its mark: the mark only finds it.",
    "a naming of the observed revision marked as a provenance stamp",
    # Round 4, Note 2: an identity shown whole is the fourth excepted kind,
    # decided by equality with a served identity.
    "Four kinds of element are excepted.",
    "an identity, whose whole text equals the evaluation identity that the machine answer serves",
    "every excepted identity's whole text equal to the evaluation identity",
    # Round 4, Note 3: the status line's warrant is stated, not attributed.
    "the operability status line that the shared page shell renders on every surface, Polaris included",
    "No requirement of this specification or of the Three-Surface POC specification names that line",
    # Round 4, Note 4: the closed term list, block scope and an aligned limb.
    "`unmoved`, `not moved`, `unchanged`, `stable` or `still points`, matched case-insensitively",
    "A block is the nearest enclosing paragraph, list item, table cell, heading, caption or summary element, read as its whole text.",
    "The term list is closed: a paraphrase outside it is not decided by this requirement.",
    "a tag name and a term in different inline elements of one block are read together",
    "a stability term in a label unit, the label record or a block holding a captured tag name",
    # Round 4, Note 5: test 3's three conditions each have a fixture.
    "with the tag-set read admitted and the ancestry read not admitted",
    "with one commit of the revision's history made unreadable",
    "with a graft boundary imposed on its object database",
    # Round 4, Note 6: the closed page population.
    "The Polaris pages are the human HTML responses to `GET /polaris` and to every request of PWB-REQ-011's exact-source route, served or refused, in every mount form.",
    "are not Polaris pages",
    # Round 5, Finding 1: the cite's visible text is decided by equality with
    # a value the checker reads from the record it names, so a sentence cast
    # as a citation fails.
    "The cite's whole visible text, whitespace-normalized, equals one value the checker reads from the record it names",
    "the locator of that anchor, as the machine narrative serves it, or the path of that source record, as the machine answer serves it",
    "That text holds no whitespace, or it is a path that the checker's own Git listing of the observed revision holds.",
    "every such cite's whole text equal to its record's served locator or path",
    "a cite whose text is not its record's served locator or path",
    "the identity each citation's cite names, and that record's served locator or path",
    # Round 5, Note 1: the identity exception's record population is closed.
    "or the source identity of one source record that the machine answer serves at that evaluation, and is not a revision's id alone.",
    "These two are the whole population: an identity of any other record is not excepted.",
    "or to the source identity of one source record served at that evaluation, and not a revision's id alone",
    "an element marked as an identity whose text is neither the evaluation identity nor one served source record's source identity, or is a revision's id alone",
    # Round 5, Note 2: the page exclusions as one whole sentence.
    "The machine answer, PWB-REQ-020's derived machine views and generation draft view, and the response to a human re-observation request are not Polaris pages.",
    # Round 3, Finding 2: the not-read tests read checker-owned construction
    # records.
    "These construction records are fixture facts the checker owns, not the observer's captured inputs.",
    "Tests 1 and 3 apply to its construction records",
    "Tests 2, 4 and 5 apply to its own recorded listing",
    "as the construction records identify it",
    # Round 3, Finding 4: no stability statement, swept and decided.
    "zero stability terms found by the fifth sweep",
    # Round 3, Finding 5: the expansion lies in the unit; the record is
    # decided by equality alone.
    "the expansion of any tied names",
    "expandable on the surface, inside the label unit.",
    "the label record is decided by this equality alone",
    # Round 2, Finding 4: "release tag" is defined by the captured tag set.
    "These are the release tags the label counts.",
    'beside the statement "no release tag reaches this revision"',
    # Round 2, Finding 6: disclosure wherever the name is carried; a failed peel.
    "SHALL be disclosed as moved wherever its name is carried",
    "Its name is carried in a label, among the tied names in the machine answer, and in the surface's expansion of those names.",
    "When any ref under `refs/tags/` cannot be read or peeled, reading the tag set failed.",
    "two tags tied at the revision, the later in codepoint order moved",
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
    "#### Scenario: Citation and identity contents are decided, not placement",
)
#: Contracts PWB-REQ-001 must newly warrant; read from its warrants block.
WARRANT_CONTRACTS = frozenset({"RFC2-2", "RFC2-24"})
WARRANT_RE = re.compile(r"^  contracts: \[([^\]\n]*)\]$", re.MULTILINE)
#: The two warrant lists the amendment extends. Every other signed line of
#: PWB-REQ-001 must survive byte for byte (round 2, Finding 5); these two may
#: grow, but must keep every signed identifier.
WARRANT_LIST_RE = re.compile(r"^  (doctrine|contracts): \[([^\]\n]*)\]$", re.MULTILINE)
REPAIR_ROWS = (
    "| RFC4-11.r1 | RFC4-11.c4 | RFC4-11 | A count over commit history is computed only from completely captured ancestry and is never reconstructed from history the adapter cannot reach | covered:PWB-REQ-001 |",
    "| RFC4-11.r2 | RFC4-11.c4 | RFC4-11 | Squash/deletion loss becomes reduced-fidelity PR facts | believed-not-applicable |",
)
REPAIR_TOTALS_LINES = (
    "Declared totals: **92 rows; 77 superseded base rows; 60 covered; 27 Unknown",
    "uncovered; 5 believed not applicable.**",
)
#: Row 35 and decision 13: the class-granular amendment (P-86), signed v1.0
#: on 2026-10-14 under its Question 5 answer "First ready lands first", took
#: row 34 and decision 12, so this package was regenerated over its bytes.
CAPABILITY_ROW = (
    "| 35 | Lead every human naming of the observed revision with its release "
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
DECISION_RE = re.compile(r"^### (\d+)\. ", re.MULTILINE)
DESIGN_PHRASES = (
    "### 13. Name the revision by its release label",
    "until a registry amendment does, every label takes the not-read form.",
    # Round 6, Note 2: decision 13 carries the cycle-4 and cycle-5 rules.
    "and whose cite text is that record's served locator or path. Two gaps stay open and are stated in the requirement",
    "an identity shown whole, equal to the evaluation identity or to one served source record's source identity, and no other record's",
    "first twelve digits, or project name followed by a tag name; a shorter prefix is not decided.",
    # Round 7, Note 3: which gaps, and their polarity.
    "Two gaps stay open and are stated in the requirement: where the citation or an excepted identity sits (inside a sentence passes), and which tokens a served locator holds;",
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
    signed = old[REQ_001]
    lost = lost_lines(signed, block, lambda line: bool(WARRANT_LIST_RE.match(line)))
    if lost:
        findings.append(f"signed PWB-REQ-001 line edited, moved or removed: {lost[0]!r}")
    for key, items in WARRANT_LIST_RE.findall(signed):
        kept = re.search(rf"^  {key}: \[([^\]\n]*)\]$", block, re.MULTILINE)
        now = {item.strip() for item in kept.group(1).split(",")} if kept else set()
        dropped = sorted({item.strip() for item in items.split(",")} - now)
        if dropped:
            findings.append(f"PWB-REQ-001 drops signed {key} warrant {', '.join(dropped)}")
    text = flat(block)
    for phrase in REQUIRED_ONCE:
        count = text.count(flat(phrase))
        if count != 1:
            findings.append(f"PWB-REQ-001 carries {count} copies of required phrase: {phrase!r}")
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
    """Signed lines that do not survive, in their signed order, in ``new``.

    The amendment only inserts lines (and replaces the ``skip`` lines), so the
    signed lines must be a subsequence of the new ones. A greedy match finds a
    subsequence whenever one exists; a line edited, removed or moved past a
    later signed line is reported (round 3, Finding 6: a multiset comparison
    let a signed line move).

    Duplicate lines (round 4, Note 7). Matching a signed line to the earliest
    later copy is exact for the subsequence property, twins included: if any
    matching exists, the earliest one leaves the most room for the lines
    after it. An edit that deletes a signed line and still leaves the signed
    lines a subsequence produces bytes identical to an insertions-only edit
    of the signed text, so no byte comparison can tell the two apart, and
    nothing the amendment may not do is hidden by it. ``--selftest`` checks
    this function against an independent longest-common-subsequence count
    over seeded random texts made mostly of repeated lines.
    """
    lines = new.split("\n")
    lost = []
    position = 0
    for line in old.split("\n"):
        if skip(line):
            continue
        try:
            position = lines.index(line, position) + 1
        except ValueError:
            lost.append(line)
    return lost


def capability_findings(proposed: bytes, current: bytes) -> list[str]:
    new, old = proposed.decode("utf-8"), current.decode("utf-8")
    findings = []
    lost = lost_lines(old, new, lambda line: bool(CAPABILITY_COUNT_LINES.match(line)))
    if lost:
        findings.append(f"signed capability line edited, moved or removed: {lost[0]!r}")
    if new.count(CAPABILITY_ROW) != 1:
        findings.append("capability row 35 for the release label is missing")
    numbers = [int(number) for number, _ in CAPABILITY_ROW_RE.findall(new)]
    if numbers != list(range(1, len(numbers) + 1)):
        findings.append("capability rows are not numbered 1..n in order")
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
        findings.append(f"signed repair-delta line edited, moved or removed: {lost[0]!r}")
    for row in REPAIR_ROWS:
        if new.count(row) != 1:
            findings.append(f"repair row missing: {row.split(' | ')[0][2:]}")
    return findings


def companion_findings(proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]) -> list[str]:
    findings = []
    for rel in (PROPOSAL, DESIGN):
        lost = lost_lines(current[rel].decode("utf-8"), proposed[rel].decode("utf-8"))
        if lost:
            findings.append(f"signed {rel.name} line edited, moved or removed: {lost[0]!r}")
    if PROPOSAL_PHRASE not in proposed[PROPOSAL].decode("utf-8"):
        findings.append("proposal does not carry the release-label bullet")
    design_text = proposed[DESIGN].decode("utf-8")
    design = flat(design_text)
    for phrase in DESIGN_PHRASES:
        if flat(phrase) not in design:
            findings.append(f"design lacks: {phrase[:60]!r}")
    # Round 4, Note 8: a patch applied after a sibling's took the same number
    # relocates silently, so the decisions must stay numbered 1..n in order.
    decisions = [int(number) for number in DECISION_RE.findall(design_text)]
    if decisions != list(range(1, len(decisions) + 1)):
        findings.append(f"design decisions are not numbered 1..n in order: {decisions}")
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


#: Authored companion subjects this package patches beside the spec. The
#: derived subjects are regenerated at each sign-off, so only these compose.
COMPANIONS = (CAPABILITY, REPAIR_DELTA, DESIGN, PROPOSAL)


def companion_order_patches(
    rel: pathlib.Path, candidates: pathlib.Path | None = None,
) -> list[tuple[str, pathlib.Path]]:
    """This package's patch of ``rel``, then each pending sibling's, by name."""
    candidates = candidates or ROOT / CANDIDATES
    mine = [p for p in patch_files() if patch_target(p) == rel]
    patches = [(CANDIDATE.name, mine[0])] if mine else []
    for name in sorted(PENDING_SIBLINGS):
        for theirs in sorted((candidates / name / "proposed").glob("*.patch")):
            try:
                if patch_target(theirs) == rel:
                    patches.append((name, theirs))
            except ValueError:
                continue
    return patches


def companion_order_findings(candidates: pathlib.Path | None = None) -> list[str]:
    """Round 4, Note 8: the order check covered the spec only, so a sibling's
    design or capability patch could collide unseen. Every companion subject
    that a pending sibling also patches gets the same all-orders search."""
    findings = []
    for rel in COMPANIONS:
        patches = companion_order_patches(rel, candidates)
        if len(patches) < 2:
            continue
        for finding in orders.all_orders_findings((ROOT / rel).read_bytes(), patches, rel):
            findings.append(f"{rel.name}: {finding}")
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
    findings.extend(companion_order_findings())
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


def phrase_finding(phrase: str) -> str:
    """The exact finding a mutant deleting one required phrase must raise
    (round 3, Finding 6: a shared prefix let any missing phrase satisfy it)."""
    return f"PWB-REQ-001 carries 0 copies of required phrase: {phrase!r}"


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
            phrase_finding("SHALL show the revision's full Git object id beneath the label, on the same surface and without expanding anything"),
        ),
        "unread shown as untagged": (
            SPEC, _replace(proposed[SPEC], "It never states\n  that the revision is untagged.", "It may state\n  that the revision is untagged."),
            phrase_finding('It never states that the revision is untagged.'),
        ),
        "tag message read": (
            SPEC, _replace(proposed[SPEC], "no tag message or signature is read into\n    the model or rendered", "the tag message is rendered"),
            phrase_finding('no tag message or signature is read into the model or rendered'),
        ),
        "incomplete-ancestry statement false": (
            SPEC, _replace(proposed[SPEC], 'Its statement is\n     "the history needed to judge release tags was not read".', 'Its statement is\n     "release tags were not read".'),
            phrase_finding('Its statement is "the history needed to judge release tags was not read".'),
        ),
        "statement decide-line dropped": (
            SPEC, _replace(proposed[SPEC], "    - exact equality of form, statement, tag name,", "    - exact equality of form, tag name,"),
            phrase_finding('exact equality of form, statement, tag name, distance, tied names'),
        ),
        "visible reaching-tag shallow fixture dropped": (
            SPEC, _replace(proposed[SPEC], "    - a shallow clone whose captured history holds a reaching tag;\n", ""),
            phrase_finding('a shallow clone whose captured history holds a reaching tag'),
        ),
        "naming sites back to every element": (
            SPEC, _replace(proposed[SPEC], "    - zero swept occurrences outside a label unit and the excepted elements;", "    - zero swept occurrences;"),
            phrase_finding('zero swept occurrences outside a label unit and the excepted elements'),
        ),
        "release tag left undefined": (
            SPEC, _replace(proposed[SPEC], " These are the release tags the label counts.", ""),
            phrase_finding('These are the release tags the label counts.'),
        ),
        "tied moved tag undisclosed": (
            SPEC, _replace(proposed[SPEC], "SHALL be\n    disclosed as moved wherever its name is carried", "SHALL be\n    disclosed as moved wherever a label names that tag"),
            phrase_finding('SHALL be disclosed as moved wherever its name is carried'),
        ),
        "failed peel undecided": (
            SPEC, _replace(proposed[SPEC], " When any ref under `refs/tags/` cannot be read or peeled,\n    reading the tag set failed.", ""),
            phrase_finding('When any ref under `refs/tags/` cannot be read or peeled, reading the tag set failed.'),
        ),
        "signed oracle clause deleted": (
            SPEC, _replace(proposed[SPEC], "  distinct from source-claimed time. Exact set, stamp and input-identity\n  equality decides.\n", "  equality decides.\n"),
            "signed PWB-REQ-001 line edited, moved or removed",
        ),
        "signed falsifier clause edited": (
            SPEC, _replace(proposed[SPEC], "  deterministic input identity is missing, or exposed sources use different\n", "  deterministic input identity is missing, or exposed sources differ in\n"),
            "signed PWB-REQ-001 line edited, moved or removed",
        ),
        "signed observable clause edited": (
            SPEC, _replace(proposed[SPEC], "  per-emission identity.\n  For the release label", "  identity.\n  For the release label"),
            "signed PWB-REQ-001 line edited, moved or removed",
        ),
        "signed doctrine warrant dropped": (
            SPEC, _replace(proposed[SPEC], "  doctrine: [VIS-1, VIS-2, VIS-7, SEC-3]", "  doctrine: [VIS-1, VIS-2, VIS-7]"),
            "PWB-REQ-001 drops signed doctrine warrant SEC-3",
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
            SPEC, _replace(proposed[SPEC], "  3. **Not read**, when the captured ancestry is incomplete.", "  3."),
            phrase_finding('**Not read**, when the captured ancestry is incomplete.'),
        ),
        # Round 3, Finding 1: the naming site is a marked label unit, and the
        # visible-id prohibition has three bounded, marked exceptions.
        "label unit floor dropped": (
            SPEC, _replace(proposed[SPEC], "Every Polaris page\n    SHALL present at least one label unit.", "Every Polaris page\n    MAY present a label unit."),
            phrase_finding("Every Polaris page SHALL present at least one label unit."),
        ),
        "provenance stamp unbounded": (
            SPEC, _replace(proposed[SPEC], "    - a provenance stamp, the revision element of one citation.", "    - a provenance stamp, any element the implementation marks as one."),
            phrase_finding("a provenance stamp, the revision element of one citation."),
        ),
        # Round 4, Finding 1: the stamp is structural and record-verified, and
        # "the label leads" is decided.
        "stamp kind taken from its mark": (
            SPEC, _replace(proposed[SPEC], "it, and what the checker reads\n    decides each kind, never the mark alone:", "it, and the mark decides each kind:"),
            phrase_finding("what the checker reads decides each kind, never the mark alone"),
        ),
        "stamp purpose clause deleted": (
            SPEC, _replace(proposed[SPEC], " The cite names, by its\n      identity, one anchor the machine narrative serves or one source record\n      the machine answer serves at the same evaluation, and the stamp's whole\n      text is the revision that record carries, in full or as its first\n      twelve hexadecimal digits.", ""),
            phrase_finding("The cite names, by its identity, one anchor the machine narrative serves or one source record the machine answer serves at the same evaluation"),
        ),
        # Round 6, Finding 1: the two stated limits, and the claim withdrawn.
        "placement limit withdrawn": (
            SPEC, _replace(proposed[SPEC], "      - Two limits stay. Where a citation or an excepted identity (below)\n        sits is not decided by this requirement: a citation or an identity\n        placed inside a sentence, a heading or other running text passes\n        these tests,", "      - A revision id in a sentence, a heading or any other running text is\n        therefore never a stamp,"),
            phrase_finding("Two limits stay. Where a citation or an excepted identity (below) sits is not decided by this requirement: a citation or an identity placed inside a sentence, a heading or other running text passes these tests, though its words then name the revision outside a label unit, an identity by the revision's full object id."),
        ),
        "locator limit withdrawn": (
            SPEC, _replace(proposed[SPEC], " Which tokens an anchor's served\n        locator holds is not decided either: PWB-REQ-014's anchor shape\n        requires a locator and fixes no values, so a one-token locator that\n        reads as a phrase passes;", ";"),
            phrase_finding("Which tokens an anchor's served locator holds is not decided either: PWB-REQ-014's anchor shape requires a locator and fixes no values, so a one-token locator that reads as a phrase passes"),
        ),
        "scenario placement limit dropped": (
            SPEC, _replace(proposed[SPEC], "- **AND** whether that citation or an excepted identity sits inside the\n  sentence is not decided by this requirement\n", ""),
            phrase_finding("**AND** whether that citation or an excepted identity sits inside the sentence is not decided by this requirement"),
        ),
        "scenario THEN back to the overclaim": (
            SPEC, _replace(proposed[SPEC], "- **THEN** outside a citation and an excepted identity the sentence shows", "- **THEN** outside a citation the sentence shows"),
            phrase_finding("**THEN** outside a citation and an excepted identity the sentence shows neither R's full object id nor its first twelve hexadecimal digits"),
        ),
        # Round 7, Finding 2 and Note 3: identity placement, the WHEN, and
        # the design's gap list and polarity.
        "identity placement limit dropped": (
            SPEC, _replace(proposed[SPEC], "that identity whole, and where it sits is the first limit above;", "that identity whole;"),
            phrase_finding("It shows that identity whole, and where it sits is the first limit above;"),
        ),
        "scenario WHEN widened": (
            SPEC, _replace(proposed[SPEC], "about the observed revision R\n  outside every label unit\n", "about the observed revision R\n  outside every label unit or citation\n"),
            phrase_finding("**WHEN** a Polaris page has a sentence about the observed revision R outside every label unit - **THEN**"),
        ),
        "design gap polarity flipped": (
            DESIGN, _replace(proposed[DESIGN], "sits (inside a sentence passes), and", "sits (inside a sentence fails), and"),
            "design lacks",
        ),
        "design identity gap dropped": (
            DESIGN, _replace(proposed[DESIGN], "where the\n    citation or an excepted identity sits", "where the\n    citation sits"),
            "design lacks",
        ),
        # Round 6, Note 1: the reviewer's six digest-only deletions.
        "cite swept-occurrence clause dropped": (
            SPEC, _replace(proposed[SPEC], " It holds no\n        occurrence that the text sweep below finds.", ""),
            phrase_finding("It holds no occurrence that the text sweep below finds."),
        ),
        "cite decide-line tail dropped": (
            SPEC, _replace(proposed[SPEC], "      path, holding no whitespace or equal to a path in the checker's own\n      Git listing, and holding no swept occurrence;", "      path;"),
            phrase_finding("holding no whitespace or equal to a path in the checker's own Git listing, and holding no swept occurrence"),
        ),
        "cite falsifier tail dropped": (
            SPEC, _replace(proposed[SPEC], " holds\n    whitespace and is not a path in the checker's own Git listing, or holds\n    a swept occurrence;", ";"),
            phrase_finding("holds whitespace and is not a path in the checker's own Git listing, or holds a swept occurrence"),
        ),
        "cite consequence dropped": (
            SPEC, _replace(proposed[SPEC], "      - So a stamp's citation holds only a served name with no space in it,\n        or a real path, beside the revision. ", "      - "),
            phrase_finding("So a stamp's citation holds only a served name with no space in it, or a real path, beside the revision."),
        ),
        "scenario whitespace clause dropped": (
            SPEC, _replace(proposed[SPEC], "only the record's served locator or path, with no whitespace unless it is\n  a path in R's tree, and R's id as its stamp", "only the record's served locator or path and R's id as its stamp"),
            phrase_finding("with no whitespace unless it is a path in R's tree, and R's id as its stamp"),
        ),
        # Round 6, Note 3: the sweep defines a naming.
        "short-prefix gap unstated": (
            SPEC, _replace(proposed[SPEC], " These three\n    are the namings the text sweep below finds, and \"names the observed\n    revision\" means them: a shorter prefix of the object id is not decided\n    by this requirement.", ""),
            phrase_finding("These three are the namings the text sweep below finds, and \"names the observed revision\" means them: a shorter prefix of the object id is not decided by this requirement."),
        ),
        # Round 6, Note 2: design decision 13 matches the requirement.
        "design identity population reopened": (
            DESIGN, _replace(proposed[DESIGN], "equal to the evaluation identity or to one\n    served source record's source identity, and no other record's;", "equal to the evaluation identity or a served\n    record's own identity;"),
            "design lacks",
        ),
        "design cite-text rule dropped": (
            DESIGN, _replace(proposed[DESIGN], "that revision, and whose cite text is that record's served locator or\n    path. Two gaps", "that revision. Two gaps"),
            "design lacks",
        ),
        "stamp citation decide-line dropped": (
            SPEC, _replace(proposed[SPEC], "    - every provenance stamp inside a citation whose cite names one anchor or\n      source record served at that evaluation,", "    - every provenance stamp"),
            phrase_finding("every provenance stamp inside a citation whose cite names one anchor or source record served at that evaluation"),
        ),
        "lead rule dropped": (
            SPEC, _replace(proposed[SPEC], " On each Polaris page, the first occurrence\n    in document order that the text sweep below finds outside the\n    operability status line lies in a label unit.", ""),
            phrase_finding("the first occurrence in document order that the text sweep below finds outside the operability status line lies in a label unit"),
        ),
        "label-before-id dropped": (
            SPEC, _replace(proposed[SPEC], " Within each label unit the label precedes the full\n    object id in document order.", ""),
            phrase_finding("Within each label unit the label precedes the full object id in document order."),
        ),
        "naming-as-stamp falsifier dropped": (
            SPEC, _replace(proposed[SPEC], "  - a naming of the observed revision marked as a provenance stamp:", "  - a stamp:"),
            phrase_finding("a naming of the observed revision marked as a provenance stamp"),
        ),
        # Round 4, Note 2: the identity exception is decided by equality.
        "identity exception unbounded": (
            SPEC, _replace(proposed[SPEC], "    - an identity, whose whole text equals the evaluation identity that the\n      machine answer serves", "    - an identity, whose text includes the evaluation identity that the\n      machine answer serves"),
            phrase_finding("an identity, whose whole text equals the evaluation identity that the machine answer serves"),
        ),
        # Round 4, Note 3: the reviewer's widened status-line mutant.
        "status-line exception widened": (
            SPEC, _replace(proposed[SPEC], "    - the operability status line that the shared page shell renders on\n      every surface, Polaris included.", "    - any element the implementation marks as a provenance stamp."),
            phrase_finding("the operability status line that the shared page shell renders on every surface, Polaris included"),
        ),
        "status-line warrant reattributed": (
            SPEC, _replace(proposed[SPEC], "No requirement of this specification\n      or of the Three-Surface POC specification names that line;", "The POC specification governs that line;"),
            phrase_finding("No requirement of this specification or of the Three-Surface POC specification names that line"),
        ),
        # Round 4, Note 4: the reviewer's narrowed-term mutant, and the block.
        "stability terms narrowed": (
            SPEC, _replace(proposed[SPEC], "`unmoved`, `not moved`, `unchanged`, `stable` or `still points`,", "`unmoved`,"),
            phrase_finding("`unmoved`, `not moved`, `unchanged`, `stable` or `still points`, matched case-insensitively"),
        ),
        "stability sweep back to text nodes": (
            SPEC, _replace(proposed[SPEC], " A block is the nearest enclosing paragraph,\n    list item, table cell, heading, caption or summary element, read as its\n    whole text.", " A block is a text node."),
            phrase_finding("A block is the nearest enclosing paragraph, list item, table cell, heading, caption or summary element, read as its whole text."),
        ),
        # Round 4, Note 5: test 3's unadmitted-ancestry fixture.
        "unadmitted-ancestry fixture dropped": (
            SPEC, _replace(proposed[SPEC], "with the tag-set read admitted and the ancestry\n      read not admitted, ", ""),
            phrase_finding("with the tag-set read admitted and the ancestry read not admitted"),
        ),
        # Round 4, Note 6: the page population.
        "page population dropped": (
            SPEC, _replace(proposed[SPEC], "  - The Polaris pages are the human HTML responses to `GET /polaris` and to\n    every request of PWB-REQ-011's exact-source route, served or refused, in\n    every mount form.", "  - The Polaris pages are the human HTML responses Polaris serves."),
            phrase_finding("The Polaris pages are the human HTML responses to `GET /polaris` and to every request of PWB-REQ-011's exact-source route, served or refused, in every mount form."),
        ),
        # Round 5, Finding 1: the reviewer's sentence-cast-as-citation page
        # passes once the cite's text is free again.
        "cite text left free": (
            SPEC, _replace(proposed[SPEC], "      - The cite's whole visible text, whitespace-normalized, equals one\n        value the checker reads from the record it names:", "      - The cite's visible text is any words the implementation chooses, beside"),
            phrase_finding("The cite's whole visible text, whitespace-normalized, equals one value the checker reads from the record it names"),
        ),
        "cite value widened": (
            SPEC, _replace(proposed[SPEC], "the locator of\n        that anchor, as the machine narrative serves it, or the path of\n        that source record, as the machine answer serves it.", "any label of\n        that record."),
            phrase_finding("the locator of that anchor, as the machine narrative serves it, or the path of that source record, as the machine answer serves it"),
        ),
        "cite whitespace bound dropped": (
            SPEC, _replace(proposed[SPEC], "      - That text holds no whitespace, or it is a path that the checker's\n        own Git listing of the observed revision holds.", "      - That text may hold whitespace."),
            phrase_finding("That text holds no whitespace, or it is a path that the checker's own Git listing of the observed revision holds."),
        ),
        "cite decide-line dropped": (
            SPEC, _replace(proposed[SPEC], "    - every such cite's whole text equal to its record's served locator or\n      path,", "    - every such cite's text"),
            phrase_finding("every such cite's whole text equal to its record's served locator or path"),
        ),
        "cite falsifier dropped": (
            SPEC, _replace(proposed[SPEC], "  - a cite whose text is not its record's served locator or path,", "  - a cite"),
            phrase_finding("a cite whose text is not its record's served locator or path"),
        ),
        "cite value unobservable": (
            SPEC, _replace(proposed[SPEC], "the identity each citation's cite names, and that\n  record's served locator or path.", "and the identity each citation's cite names."),
            phrase_finding("the identity each citation's cite names, and that record's served locator or path"),
        ),
        "citation scenario dropped": (
            SPEC, _replace(proposed[SPEC], "#### Scenario: Citation and identity contents are decided, not placement", "#### Scenario: Citation and identity contents are decided"),
            "PWB-REQ-001 lacks exactly one",
        ),
        # Round 5, Note 1: the reviewer's identity-population mutants.
        "identity population reopened": (
            SPEC, _replace(proposed[SPEC], "or the source\n      identity of one source record that the machine answer serves at that\n      evaluation, and is not a revision's id alone.", "or the whole value\n      of an `identity` field of any record the machine answer serves."),
            phrase_finding("or the source identity of one source record that the machine answer serves at that evaluation, and is not a revision's id alone."),
        ),
        "identity population not closed": (
            SPEC, _replace(proposed[SPEC], " These two are the whole\n      population: an identity of any other record is not excepted.", ""),
            phrase_finding("These two are the whole population: an identity of any other record is not excepted."),
        ),
        "identity decide-line revision clause dropped": (
            SPEC, _replace(proposed[SPEC], "      evaluation, and not a revision's id alone;", "      evaluation;"),
            phrase_finding("or to the source identity of one source record served at that evaluation, and not a revision's id alone"),
        ),
        "identity falsifier revision clause dropped": (
            SPEC, _replace(proposed[SPEC], ", or is a\n    revision's id alone;", ";"),
            phrase_finding("an element marked as an identity whose text is neither the evaluation identity nor one served source record's source identity, or is a revision's id alone"),
        ),
        # Round 5, Note 2: the reviewer's page-exclusion mutant.
        "page exclusion widened": (
            SPEC, _replace(proposed[SPEC], "The machine answer, PWB-REQ-020's derived machine views\n    and generation draft view, and the response to a human re-observation\n    request are not Polaris pages.", "The machine answer, PWB-REQ-020's derived machine views,\n    the exact-source route and the response to a human re-observation\n    request are not Polaris pages."),
            phrase_finding("The machine answer, PWB-REQ-020's derived machine views and generation draft view, and the response to a human re-observation request are not Polaris pages."),
        ),
        # Round 4, Note 7: a deleted signed line, with twins later, is lost.
        "signed blank line deleted": (
            SPEC, _replace(proposed[SPEC], "**Verification.**\n\n- **Case**: observe a repository at a known revision", "**Verification.**\n- **Case**: observe a repository at a known revision"),
            "signed PWB-REQ-001 line edited, moved or removed",
        ),
        "verbatim exception dropped": (
            SPEC, _replace(proposed[SPEC], "Butlers-declared text that PWB-REQ-014 keeps verbatim in its own leaf,", "Butlers-declared text,"),
            phrase_finding("Butlers-declared text that PWB-REQ-014 keeps verbatim in its own leaf"),
        ),
        # Round 3, Finding 2: tests 1 and 3 read the construction records.
        "not-read tests off the construction records": (
            SPEC, _replace(proposed[SPEC], "Tests 1 and 3 apply to its\n    construction records", "Tests 1 and 3 apply to its\n    recorded listing"),
            phrase_finding("Tests 1 and 3 apply to its construction records"),
        ),
        # Round 3, Finding 4: a stability statement is swept and decided.
        "stability decide-line dropped": (
            SPEC, _replace(proposed[SPEC], "    - zero stability terms found by the fifth sweep;\n", ""),
            phrase_finding("zero stability terms found by the fifth sweep"),
        ),
        # Round 3, Finding 5: the label record is decided by equality alone.
        "label record under the page predicates": (
            SPEC, _replace(proposed[SPEC], "; the label-unit predicates apply to page sites\n      only, and the label record is decided by this equality alone", ""),
            phrase_finding("the label record is decided by this equality alone"),
        ),
        # Round 3, Finding 6: a signed line moved within PWB-REQ-001 fails
        # the order-aware lost-line guard.
        "signed line moved": (
            SPEC, _replace(proposed[SPEC], "  distinct from source-claimed time. Exact set, stamp and input-identity\n  equality decides.\n", "  equality decides.\n  distinct from source-claimed time. Exact set, stamp and input-identity\n"),
            "signed PWB-REQ-001 line edited, moved or removed",
        ),
        "repair row dropped": (
            REPAIR_DELTA, _replace(proposed[REPAIR_DELTA], REPAIR_ROWS[0] + "\n", ""),
            "repair row missing: RFC4-11.r1",
        ),
        "signed repair row edited": (
            REPAIR_DELTA, _replace(proposed[REPAIR_DELTA], "| RFC2-1.r2 | RFC2-1.c12 |", "| RFC2-1.r2 | RFC2-1.c13 |"),
            "signed repair-delta line edited, moved or removed",
        ),
        "capability row dropped": (
            CAPABILITY, _replace(proposed[CAPABILITY], CAPABILITY_ROW + "\n", ""),
            "capability row 35 for the release label is missing",
        ),
        "capability totals drift": (
            CAPABILITY, _replace(proposed[CAPABILITY], "Totals: 29 covered", "Totals: 30 covered"),
            "capability totals are not the computed figures",
        ),
        # Round 4, Note 8: a row or decision number taken twice.
        "capability row number reused": (
            CAPABILITY, _replace(proposed[CAPABILITY], "| 35 | Lead every human naming", "| 34 | Lead every human naming"),
            "capability rows are not numbered 1..n in order",
        ),
        "design decision number reused": (
            DESIGN, _replace(proposed[DESIGN], "### 13. Name the revision by its release label", "### 12. Name the revision by its release label"),
            "design decisions are not numbered 1..n in order",
        ),
        "signed capability row edited": (
            CAPABILITY, _replace(proposed[CAPABILITY], "| 1 | Bind every source to one exact Butlers revision |", "| 1 | Bind every source to one Butlers revision |"),
            "signed capability line edited, moved or removed",
        ),
        "signed proposal line edited": (
            PROPOSAL, _replace(proposed[PROPOSAL], "- **Every declared item is counted.**", "- **Items are counted.**"),
            "signed proposal.md line edited, moved or removed",
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
            "signed design.md line edited, moved or removed",
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
        failed += companion_order_selftest(pathlib.Path(temp) / "companions")
    failed += lost_lines_selftest()
    if failed:
        return 1
    print(
        f"selftest: {len(mutants)} structure mutants, patch drift, an unclassified "
        "sibling, the pending patch population, divergent and failing "
        "application orders, a colliding companion patch, and the lost-line "
        "guard against an independent subsequence count all fail closed on "
        "their own predicates"
    )
    return 0


def _lcs(old: list[str], new: list[str]) -> int:
    """Longest common subsequence length, by dynamic programming."""
    row = [0] * (len(new) + 1)
    for line in old:
        previous = 0
        for j, other in enumerate(new, 1):
            current = row[j]
            row[j] = previous + 1 if line == other else max(row[j], row[j - 1])
            previous = current
    return row[-1]


def lost_lines_selftest(trials: int = 4000) -> int:
    """Round 4, Note 7: ``lost_lines`` reports nothing exactly when the old
    lines are a subsequence of the new, over seeded random texts drawn from
    three lines, one of them blank, so nearly every line has twins."""
    import random

    generator = random.Random(20261014)
    alphabet = ["", "- a", "- b"]
    for _ in range(trials):
        old_text = "\n".join(generator.choice(alphabet) for _ in range(generator.randint(1, 7)))
        new_text = "\n".join(generator.choice(alphabet) for _ in range(generator.randint(1, 9)))
        old, new = old_text.split("\n"), new_text.split("\n")
        greedy_clean = not lost_lines(old_text, new_text)
        subsequence = _lcs(old, new) == len(old)
        if greedy_clean != subsequence:
            print(f"SELFTEST FAILED: lost_lines disagrees with the subsequence count on {old!r} -> {new!r}")
            return 1
    return 0


#: A synthetic pending sibling the order selftests add to the real pending
#: set. Since the P-98 sign-off (2026-10-15) no PWB sibling is pending, and
#: an order check over this package alone would be exercised by nothing.
SELFTEST_PENDING = "pwb-selftest-pending-sibling"


def _with_selftest_pending(run):
    original = globals()["PENDING_SIBLINGS"]
    globals()["PENDING_SIBLINGS"] = frozenset(original | {SELFTEST_PENDING})
    try:
        return run()
    finally:
        globals()["PENDING_SIBLINGS"] = original


def companion_order_selftest(temp: pathlib.Path) -> int:
    return _with_selftest_pending(lambda: _companion_order_selftest(temp))


def _companion_order_selftest(temp: pathlib.Path) -> int:
    """A pending sibling's patch of a companion subject joins the all-orders
    search: one that edits this package's context fails in one order."""
    fake = temp / "candidates"
    sibling = fake / SELFTEST_PENDING / "proposed"
    sibling.mkdir(parents=True)
    before = (ROOT / DESIGN).read_bytes()
    after = _replace(before, "## Risks / Trade-offs\n", "## Risks and trade-offs\n")
    (sibling / "design.md.patch").write_text(unified_patch(DESIGN, before, after), encoding="utf-8")
    found = companion_order_findings(fake)
    if not any(f.startswith("design.md: pending spec patches do not apply in every order") for f in found):
        print(f"SELFTEST FAILED: a colliding companion patch gave {found}")
        return 1
    if companion_order_findings(temp / "empty"):
        print("SELFTEST FAILED: the companion order check reports with no pending companion patch")
        return 1
    return 0


#: This package's spec patch first, then every pending sibling's, sorted;
#: the synthetic one stands in for the siblings signed since round 5.
ORDER_POPULATION = [
    "pwb-release-label-amendment",
    *sorted(PENDING_SIBLINGS | {SELFTEST_PENDING}),
]

#: The shared engine's shift fixtures. Every pair gives one result in both
#: orders, so only an all-orders search fails them.
ORDER_FIXTURES = (
    ("divergent", orders.ORDER_FIXTURE_SHIFT_BASE, orders.ORDER_FIXTURE_SHIFT[:3], [
        "pending spec patches give 2 different results across the 3! application orders",
    ]),
    ("failing", orders.ORDER_FIXTURE_SHIFT_BASE, orders.ORDER_FIXTURE_SHIFT, [
        "pending spec patches do not apply in every order: "
        "shift-first-copy after [shift-a, shift-b, shift-relocating]",
    ]),
)


def order_selftest(temp: pathlib.Path) -> int:
    return _with_selftest_pending(lambda: _order_selftest(temp))


def _order_selftest(temp: pathlib.Path) -> int:
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
