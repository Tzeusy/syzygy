#!/usr/bin/env python3
"""Build and verify the inert PWB tree-framing amendment candidate.

The amendment adds tree-form openings and supported, inert diagrams to
PWB-REQ-014 (bead ``syzygy-73e.9``). It follows the item-depth builder's
form: the current eleven-artifact PWB behavior package is act-bound. ``--check``
and ``--write`` therefore apply the candidate's ``proposed/*.patch`` files
only in a scratch tree and hash those proposed bytes. ``--apply
--at-adoption`` is the one mode that writes signed subjects; it exists for
``scripts/record_versioned_signoff.py`` after an owner's version-tagged
sign-off and refuses unless the whole package verifies. A candidate commit,
review, manifest or merge performs no owner act.
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

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-tree-framing-amendment"
)
PROPOSED = CANDIDATE / "proposed"
MANIFEST = CANDIDATE / "PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt"
MANIFEST_OUT = MANIFEST
TITLE = "PWB TREE-FRAMING BEHAVIOR AMENDMENT MANIFEST"
SCRIPT = pathlib.Path("scripts/build_pwb_tree_framing_amendment.py")
SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"
COVERAGE_SCRIPT = pathlib.Path("scripts/build_polaris_project_wide_contract_coverage.py")
CONTRACT_INDEX = pathlib.Path(
    ".syzygy/governance/contracts/candidates/05-CONTRACT-INDEX.yaml"
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
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
PATCHED = {
    CHANGE / "CAPABILITY-COVERAGE.md",
    GOVERNING,
    CHANGE / "design.md",
    CHANGE / "proposal.md",
    SPEC,
}
#: Subjects whose proposed bytes are generated from the others, never authored.
#: The contract-coverage summary is not one of them: no contract row moves, and
#: the coverage generator's own `--check` must pass over the proposed bytes.
DERIVED = frozenset({GOVERNING})
#: Sibling packages the owner declined and never applied; their patches no
#: longer apply and compose with nothing (POLARIS-LANE-B-DECLINED-AND-TARGET-
#: REVISED-DIRECTION.md). Closed list: any other sibling must classify.
DECLINED_SIBLINGS = frozenset({"pwb-scoped-attributes-amendment"})
#: Sibling packages already performed, each with the record that performed it.
#: The 2026-10-02 readability successor restyled the spec after them, so their
#: hunks no longer match the current text in either direction; a sibling here
#: is history, never composed, and only while its record exists. Without the
#: record it falls back to textual classification and an unmatched patch fails.
PERFORMED_SIBLINGS = {
    "pwb-container-shape-profile-amendment":
        "PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md",
    "pwb-dismissal-expiry-amendment": "PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md",
    "pwb-exact-source-render-mode-scenario": "PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md",
    "pwb-item-depth-amendment": "PWB-ITEM-DEPTH-AMENDMENT-SIGNOFF-v1.0.md",
    "pwb-machine-view-amendment": "PWB-MACHINE-VIEW-AMENDMENT-ACT.md",
    "pwb-missing-currency-disclosure-scenario":
        "PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md",
    "pwb-opening-band-scenario": "PWB-OPENING-BAND-SCENARIO-ACT.md",
    "pwb-readability-successor": "PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md",
}
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
DIFF_TARGET_RE = re.compile(r"^\+\+\+ b/(.+)$", re.MULTILINE)
SOURCE_RE = re.compile(
    r"^> Source: `spec\.md` sha256 `([0-9a-f]{64})` — ", re.MULTILINE
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_subjects(overrides: dict[pathlib.Path, bytes] | None = None) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    out: dict[pathlib.Path, bytes] = {}
    for rel in BEHAVIOR_SUBJECTS:
        if rel in overrides:
            out[rel] = overrides[rel]
            continue
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
        raise ValueError(f"patch has no target: {patch.relative_to(ROOT)}")
    return pathlib.Path(match.group(1))


def apply_patch(base: pathlib.Path, patch: pathlib.Path) -> tuple[int, str]:
    result = subprocess.run(
        ["git", "apply", "--whitespace=nowarn", str(patch)],
        cwd=base,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stderr.strip()


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
            code, error = apply_patch(base, patch)
            if code != 0:
                raise ValueError(f"{patch.name} does not apply: {error}")
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def proposed_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
    patches: list[pathlib.Path] | None = None,
) -> dict[pathlib.Path, bytes]:
    return apply_patches(read_subjects(overrides), patch_files() if patches is None else patches)


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
    # Repository patch artifacts keep blank hunk lines prefix-free so the
    # patch file itself has no trailing whitespace; git apply accepts this
    # established form (see the sibling PWB candidate patches).
    return rendered.replace("\n \n", "\n\n")


def regenerate_governing_patch() -> str:
    semantic = [p for p in patch_files() if patch_target(p) not in DERIVED]
    proposed = proposed_bytes(patches=semantic)
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        raise ValueError("proposed spec warrants do not validate: " + " | ".join(errors))
    return unified_patch(GOVERNING, read_subjects()[GOVERNING], generated.encode())


def coverage_mirror(proposed: dict[pathlib.Path, bytes], temp: pathlib.Path) -> pathlib.Path:
    """A scratch tree holding the contract-coverage generator and proposed bytes."""
    for rel in (
        COVERAGE_SCRIPT,
        pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
        pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
        CONTRACT_INDEX,
    ):
        target = temp / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, target)
    for rel, body in proposed.items():
        target = temp / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
    parent = pathlib.Path("openspec/changes/three-surface-poc-experience")
    shutil.copytree(ROOT / parent, temp / parent)
    return temp


def run_coverage(temp: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(temp / COVERAGE_SCRIPT), *args],
        cwd=temp, capture_output=True, text=True,
    )


def generated_coverage(proposed: dict[pathlib.Path, bytes]) -> bytes:
    """CONTRACT-COVERAGE.md as the repository generator writes it over `proposed`."""
    with tempfile.TemporaryDirectory() as temp:
        mirror = coverage_mirror(proposed, pathlib.Path(temp))
        result = run_coverage(mirror)
        if result.returncode != 0:
            raise ValueError(
                "contract-coverage generator failed: "
                + (result.stdout + result.stderr).strip()
            )
        return (mirror / CONTRACT_COVERAGE).read_bytes()


def coverage_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    """Run the neighbouring generator's own --check over the proposed bytes."""
    with tempfile.TemporaryDirectory() as temp:
        mirror = coverage_mirror(proposed, pathlib.Path(temp))
        result = run_coverage(mirror, "--check")
        if result.returncode != 0:
            return [
                "contract-coverage --check fails over the proposed bytes: "
                + (result.stdout + result.stderr).strip().splitlines()[-1]
            ]
    return []


def render_manifest(proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        f"# {TITLE}\n"
        "# Candidate: binds nothing until the owner signs off a version of this\n"
        "# package (OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md).\n"
        "# 11 artifacts; rows sorted by codepoint path.\n"
        "# All rows take effect together or none do.\n"
        "# Rows hash PROPOSED bytes; signed openspec bytes remain unchanged.\n"
    )
    rows = "".join(
        f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in BEHAVIOR_SUBJECTS
    )
    return header + rows


#: Load-bearing fragments of the proposed PWB-REQ-014 text. Each must occur
#: exactly once (whitespace-normalized); the selftest mutates each one.
REQUIRED_ONCE = (
    "### Requirement: PWB-REQ-014 — Every narrative claim is bounded, anchored and non-authoritative",
    "**Tree form.** Syzygy-authored framing SHALL read as an abstraction tree under CC-REV-8.",
    "Each top-level project category, catalog, item detail and evidence group SHALL open with one Syzygy-authored opening",
    "An opening is a lede under PWB-REQ-012 and a narrative unit of this requirement.",
    "An opening SHALL state only what that group's own rendered children state, derived from the same evaluation's shared model",
    "never a claim found nowhere beneath it",
    "Butlers-declared text SHALL stay verbatim in its own leaf.",
    "SHALL NOT paraphrase, condense or stand in for that text",
    "An opening that counts claims SHALL carry PWB-REQ-007's aggregate disclosure.",
    "Before the first capability catalog no opening counts Unknown claims, so PWB-REQ-010's opening aggregate stays the only one there.",
    "the RFC7-17 authority bands and the exact-source route keep their structure",
    "**Diagrams.** A relationship among claims the shared model holds SHALL be drawn where the independent rendered-design review judges",
    "The review record SHALL list every flow, dependency, ordering, boundary or placement it judged",
    "a relationship judged prose-sufficient needs no diagram",
    "A relationship is drawable only when at least one of its edges is a claim the shared model holds.",
    "SHALL NOT be drawn from prose, labels or inference",
    "Every drawn node, edge and label SHALL draw exactly one claim",
    "by that claim's stable identity",
    "An element is drawn Unknown only where a claim establishes the element and its state is Unknown; no other element is drawn.",
    "Each diagram SHALL have an adjacent text equivalent naming every node, edge, label and marking it draws",
    "Each drawn tuple SHALL equal its machine claim's tuple under PWB-REQ-020",
    "the diagram's declarative node-and-edge source SHALL be recoverable from the machine narrative",
    "A diagram SHALL render as inline static SVG reduced to an allow-list of shapes, paths, text and styling",
    "with no script, event-handler attribute, animation, `foreignObject`, link, or external or unsafe-scheme reference",
    "SHALL be validated against that allow-list before it reaches a sink",
    "A diagram that fails rendering or validation SHALL NOT be emitted; its text equivalent remains and the failure is disclosed in place.",
    "count toward PWB-REQ-006's final human-output ceiling, and are never authority",
    "#### Scenario: A group opens with its answer",
    "#### Scenario: An opening above Butlers text stays outside it",
    "the verbatim text is byte-identical with and without the opening",
    "#### Scenario: A supported relationship is drawn inertly",
    "#### Scenario: A relationship with no supported edge is disclosed, not drawn",
    "#### Scenario: A failed or unsafe diagram emits nothing active",
    "no SVG for that diagram reaches either sink",
    "doctrine: [VIS-1, VIS-2, VIS-7, SEC-3]",
    "policies: [CC-BAR-3, CC-REV-3, CC-REV-8, CC-TEST-5]",
)
#: The selftest's one mutant per required fragment: (old, new).
SEMANTIC_MUTANTS = {
    "tree form loses its policy": ("abstraction tree under CC-REV-8", "abstraction tree"),
    "groups need no opening": ("evidence group SHALL open with one Syzygy-authored opening", "evidence group MAY open with one Syzygy-authored opening"),
    "opening escapes the lede rules": ("An opening is a lede under PWB-REQ-012", "An opening is free text outside PWB-REQ-012"),
    "opening states beyond its children": ("An opening SHALL state only what that group's own rendered children state", "An opening SHALL state what the author judges useful"),
    "truncation may hide a claim": ("never a claim found nowhere beneath it", "sometimes a claim found nowhere beneath it"),
    "Butlers text not kept verbatim": ("Butlers-declared text SHALL stay verbatim in its own leaf.", "Butlers-declared text MAY be summarized in its own leaf."),
    "opening may paraphrase Butlers": ("SHALL NOT paraphrase, condense or stand in for that text", "MAY paraphrase, condense or stand in for that text"),
    "counting opening drops the aggregate tuple": ("An opening that counts claims SHALL carry PWB-REQ-007's aggregate disclosure.", "An opening that counts claims carries no disclosure."),
    "second Unknown aggregate before the catalog": ("Before the first capability catalog no opening counts Unknown claims", "Before the first capability catalog each opening counts Unknown claims"),
    "bands lose their structure": ("the RFC7-17 authority bands and the exact-source route keep their structure", "the RFC7-17 authority bands may be merged"),
    "author decides the diagrams": ("where the independent rendered-design review judges", "where the author judges"),
    "review record keeps no list": ("The review record SHALL list every flow", "The review record MAY list a flow"),
    "figure quota returns": ("a relationship judged prose-sufficient needs no diagram", "every relationship needs a diagram"),
    "edgeless boxes count as drawable": ("drawable only when at least one of its edges is a claim the shared model holds", "drawable whenever its nodes are claims the shared model holds"),
    "relationship drawn from prose": ("SHALL NOT be drawn from prose, labels or inference", "MAY be drawn from prose, labels or inference"),
    "drawn element without a claim": ("Every drawn node, edge and label SHALL draw exactly one claim", "Every drawn node and edge SHOULD draw a claim"),
    "element identity by label": ("by that claim's stable identity", "by that claim's label"),
    "unsupported Unknown element drawn": ("An element is drawn Unknown only where a claim establishes the element", "An element is drawn Unknown wherever support is missing"),
    "no text equivalent": ("Each diagram SHALL have an adjacent text equivalent", "Each diagram MAY have an adjacent text equivalent"),
    "drawn tuple differs from the machine": ("Each drawn tuple SHALL equal its machine claim's tuple", "Each drawn tuple SHOULD resemble its machine claim's tuple"),
    "declarative source lost": ("source SHALL be recoverable from the machine narrative", "source is discarded after rendering"),
    "SVG not allow-listed": ("reduced to an allow-list of shapes, paths, text and styling", "reduced to common SVG elements"),
    "foreignObject admitted": ("animation, `foreignObject`, link,", "animation, link,"),
    "SVG emitted before validation": ("SHALL be validated against that allow-list before it reaches a sink", "MAY be validated against that allow-list after it reaches a sink"),
    "failed diagram emitted": ("A diagram that fails rendering or validation SHALL NOT be emitted", "A diagram that fails rendering or validation SHALL be emitted unchanged"),
    "diagrams escape the ceiling": ("count toward PWB-REQ-006's final human-output ceiling", "are exempt from PWB-REQ-006's final human-output ceiling"),
    "verbatim scenario weakened": ("the verbatim text is byte-identical with and without the opening", "the verbatim text is similar with and without the opening"),
    "unsafe scenario weakened": ("no SVG for that diagram reaches either sink", "a sanitized copy of that SVG reaches each sink"),
    "warrant drops SEC-3": ("doctrine: [VIS-1, VIS-2, VIS-7, SEC-3]", "doctrine: [VIS-1, VIS-2, VIS-7]"),
    "warrant drops CC-REV-8": ("CC-REV-3, CC-REV-8, CC-TEST-5", "CC-REV-3, CC-TEST-5"),
}
#: Signed bytes this package must find unapplied before sign-off.
SIGNED_FALSIFIER = (
    "- **Falsifier**: an unclassified narrative unit, uncovered claim, surplus or\n"
    "  ambiguous anchor, missing non-citable attribute, or downstream citation to\n"
    "  Polaris.\n"
)


def _flat(text: str) -> str:
    return " ".join(text.split())


def semantic_findings(
    proposed: dict[pathlib.Path, bytes], current_spec: bytes | None = None
) -> list[str]:
    spec = proposed[SPEC].decode("utf-8")
    findings: list[str] = []
    flat = _flat(spec)
    for fragment in REQUIRED_ONCE:
        count = flat.count(_flat(fragment))
        if count != 1:
            findings.append(f"proposed spec expected one {fragment!r}, found {count}")
    # Every other requirement keeps its exact bytes: only the PWB-REQ-014 block moves.
    current = (read_subjects()[SPEC] if current_spec is None else current_spec).decode("utf-8")
    before, after = requirement_blocks(current), requirement_blocks(spec)
    if list(before) != list(after):
        findings.append("proposed spec changes the requirement population or order")
    for rid in before:
        if rid != "PWB-REQ-014" and before[rid] != after.get(rid):
            findings.append(f"proposed spec edits {rid}, outside the amended requirement")
    if spec.split("### Requirement:", 1)[0] != current.split("### Requirement:", 1)[0]:
        findings.append("proposed spec edits the text before the first requirement")
    if SIGNED_FALSIFIER not in current or "**Tree form.**" in current:
        findings.append("signed PWB-REQ-014 bytes moved in place")
    return findings


REQUIREMENT_RE = re.compile(r"^### Requirement: (PWB-REQ-\d{3}) ", re.MULTILINE)


def requirement_blocks(spec: str) -> dict[str, str]:
    """Each requirement's text, from its heading to the next heading or end."""
    starts = [(m.group(1), m.start()) for m in REQUIREMENT_RE.finditer(spec)]
    out: dict[str, str] = {}
    for i, (rid, start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else len(spec)
        out[rid] = spec[start:end]
    return out


#: The arms the resolution diagram in design.md and SEMANTIC-DELTA.md must draw.
DIAGRAM_ARMS = (
    "rendered-design review",
    "Prose only",
    "Gap disclosed in place",
    "allow-list",
    "text equivalent",
    "No SVG emitted",
)
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)


def diagram_findings(design: str, delta: str) -> list[str]:
    """Both resolution diagrams draw every arm the proposed text names."""
    findings: list[str] = []
    for label, text in (("proposed design.md", design), ("SEMANTIC-DELTA.md", delta)):
        blocks = [m for m in MERMAID_RE.findall(text) if "rendered-design review" in m]
        if len(blocks) != 1:
            findings.append(f"{label}: expected one resolution diagram, found {len(blocks)}")
            continue
        for arm in DIAGRAM_ARMS:
            if arm not in blocks[0]:
                findings.append(f"{label}: resolution diagram lacks the {arm!r} arm")
    return findings


def manifest_findings(proposed: dict[pathlib.Path, bytes], actual: str) -> list[str]:
    findings: list[str] = []
    expected = render_manifest(proposed)
    if actual != expected:
        findings.append("manifest differs from deterministic proposed-byte regeneration")
    rows = ROW_RE.findall(actual)
    if len(rows) != len(BEHAVIOR_SUBJECTS):
        findings.append(f"manifest has {len(rows)} rows; expected 11")
    return findings


def generated_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    text = proposed[GOVERNING].decode("utf-8")
    match = SOURCE_RE.search(text)
    if match is None:
        return ["proposed GOVERNING-DEPENDENCIES has no source digest"]
    expected = sha256(proposed[SPEC])
    if match.group(1) != expected:
        return ["proposed GOVERNING-DEPENDENCIES does not name proposed spec digest"]
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        return ["proposed specification warrants do not validate: " + " | ".join(errors)]
    if text != generated:
        return ["proposed GOVERNING-DEPENDENCIES differs from regeneration"]
    return []


def display(path: pathlib.Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def sibling_spec_patches() -> list[pathlib.Path]:
    root = ROOT / ".syzygy/governance/contracts/candidates"
    siblings: list[pathlib.Path] = []
    for patch in sorted(root.glob("*/proposed/spec.md.patch")):
        if CANDIDATE.as_posix() in patch.relative_to(ROOT).as_posix():
            continue
        text = patch.read_text(encoding="utf-8")
        if f"+++ b/{SPEC.as_posix()}" in text:
            siblings.append(patch)
    return siblings


def _hunk_sides(patch_text: str) -> list[tuple[str, str]]:
    """(old side, new side) text of every hunk of a one-file unified patch."""
    hunks: list[tuple[list[str], list[str]]] = []
    for line in patch_text.splitlines():
        if line.startswith("@@"):
            hunks.append(([], []))
        elif hunks and line[:1] in (" ", "-", "+", ""):
            body = line[1:]
            if line[:1] in (" ", ""):
                hunks[-1][0].append(body)
                hunks[-1][1].append(body)
            elif line[:1] == "-":
                hunks[-1][0].append(body)
            else:
                hunks[-1][1].append(body)
    return [("\n".join(old) + "\n", "\n".join(new) + "\n") for old, new in hunks]


def patch_state(patch: pathlib.Path, current: bytes | None = None) -> str:
    """`pending`, `applied` or `unclassified` against the current spec.

    Each hunk's old and new sides are searched in the current spec as
    contiguous text (git's own reverse check cannot tell an insert-only hunk
    with one context line from a pending one). A patch is applied when every
    hunk's new side is present and its old side is absent or contained in the
    new side (an insertion); pending when every hunk's old side is present and
    its new side absent; anything else cannot be composed or retired and is
    reported.
    """
    text = (read_subjects()[SPEC] if current is None else current).decode("utf-8")
    sides = _hunk_sides(patch.read_text(encoding="utf-8"))
    if not sides:
        return "unclassified"
    states = set()
    for old, new in sides:
        in_old, in_new = old in text, new in text
        if in_new and (not in_old or old in new) and old != new:
            states.add("applied")
        elif in_old and not in_new:
            states.add("pending")
        else:
            states.add("unclassified")
    return states.pop() if len(states) == 1 else "unclassified"


def performed_record(name: str, root: pathlib.Path | None = None) -> bool:
    """True when `name` is a listed performed sibling whose record exists."""
    record = PERFORMED_SIBLINGS.get(name)
    return record is not None and ((root or ROOT) / DECISIONS / record).is_file()


def sibling_population(
    siblings: list[pathlib.Path] | None = None, current: bytes | None = None,
    root: pathlib.Path | None = None,
) -> dict[str, list[pathlib.Path]]:
    siblings = sibling_spec_patches() if siblings is None else siblings
    out: dict[str, list[pathlib.Path]] = {
        "pending": [], "applied": [], "performed": [], "declined": [], "unclassified": []}
    for sibling in siblings:
        name = sibling.parent.parent.name
        if name in DECLINED_SIBLINGS:
            out["declined"].append(sibling)
        elif performed_record(name, root):
            out["performed"].append(sibling)
        else:
            out[patch_state(sibling, current)].append(sibling)
    return out


def active_sibling_spec_patches() -> list[pathlib.Path]:
    """Sibling spec patches not yet part of the signed spec."""
    return sibling_population()["pending"]


def composition_findings(
    mine: pathlib.Path | None = None,
    siblings: list[pathlib.Path] | None = None,
    current: bytes | None = None,
    root: pathlib.Path | None = None,
) -> list[str]:
    mine = ROOT / PROPOSED / "spec.md.patch" if mine is None else mine
    current = read_subjects()[SPEC] if current is None else current
    population = sibling_population(siblings, current, root)
    findings = [
        f"sibling spec patch is neither pending, applied, performed nor declined: {display(path)}"
        for path in population["unclassified"]
    ]
    for sibling in population["pending"]:
        try:
            first = apply_patches({**read_subjects(), SPEC: current}, [sibling, mine])[SPEC]
            second = apply_patches({**read_subjects(), SPEC: current}, [mine, sibling])[SPEC]
        except ValueError as error:
            findings.append(f"sibling composition failed for {display(sibling)}: {error}")
            continue
        if first != second:
            findings.append(f"sibling composition is order-dependent: {display(sibling)}")
    return findings


def delta_text() -> str:
    path = ROOT / CANDIDATE / "SEMANTIC-DELTA.md"
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def check(patches: list[pathlib.Path] | None = None) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    findings: list[str] = []
    patches = patch_files() if patches is None else patches
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != PATCHED or len(targets) != len(PATCHED):
        findings.append(
            "patch targets differ from the closed five-subject population: "
            + ", ".join(path.as_posix() for path in targets)
        )
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    findings.extend(semantic_findings(proposed))
    findings.extend(generated_findings(proposed))
    findings.extend(coverage_findings(proposed))
    findings.extend(diagram_findings(
        proposed[CHANGE / "design.md"].decode("utf-8"), delta_text()))
    if not (ROOT / MANIFEST).is_file():
        findings.append(f"missing manifest: {MANIFEST}")
    else:
        actual = (ROOT / MANIFEST).read_text(encoding="utf-8")
        findings.extend(manifest_findings(proposed, actual))
    findings.extend(composition_findings())
    return findings, proposed


def selftest() -> int:
    findings, proposed = check()
    if findings or proposed is None:
        print("SELFTEST PRECONDITION FAILED:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    cases: list[tuple[str, bool]] = []

    def fuzzy(body: bytes, old: str, new: str) -> bytes:
        pattern = r"\s+".join(re.escape(word) for word in old.split())
        replaced, count = re.subn(pattern, lambda _m: new, body.decode("utf-8"), count=1)
        assert count == 1, f"selftest mutant target absent: {old!r}"
        return replaced.encode()

    # One mutant per load-bearing fragment, and every fragment has one.
    mutated_fragments = set()
    for name, (old, new) in SEMANTIC_MUTANTS.items():
        mutated = dict(proposed)
        mutated[SPEC] = fuzzy(mutated[SPEC], old, new)
        cases.append((name, bool(semantic_findings(mutated))))
        mutated_fragments.update(f for f in REQUIRED_ONCE if _flat(old) in _flat(f))
    headings_only = {f for f in REQUIRED_ONCE if f.startswith("#")}
    cases.append(("every non-heading required fragment has a mutant",
                  not (set(REQUIRED_ONCE) - headings_only - mutated_fragments)))
    for heading in sorted(headings_only):
        mutated = dict(proposed)
        mutated[SPEC] = fuzzy(mutated[SPEC], heading, heading[:-4] + "zzzz")
        cases.append((f"renamed heading {heading[:40]!r}", bool(semantic_findings(mutated))))

    current = read_subjects()[SPEC]
    stray = dict(proposed)
    stray[SPEC] = proposed[SPEC].replace(
        "Headings SHALL contain at most six words".encode(),
        "Headings SHALL contain at most eight words".encode(), 1)
    cases.append(("an edit to a neighbouring requirement (PWB-REQ-012)",
                  stray[SPEC] != proposed[SPEC] and bool(semantic_findings(stray))))
    guide = dict(proposed)
    guide[SPEC] = proposed[SPEC].replace(b"This guide is a reading aid.", b"This guide binds.", 1)
    cases.append(("an edit before the first requirement",
                  guide[SPEC] != proposed[SPEC] and bool(semantic_findings(guide))))
    dropped = dict(proposed)
    blocks = requirement_blocks(proposed[SPEC].decode("utf-8"))
    dropped[SPEC] = proposed[SPEC].replace(blocks["PWB-REQ-013"].encode(), b"", 1)
    cases.append(("a dropped requirement", bool(semantic_findings(dropped))))
    duplicate = dict(proposed)
    duplicate[SPEC] = proposed[SPEC] + b"\n#### Scenario: A group opens with its answer\n"
    cases.append(("a duplicated scenario heading", bool(semantic_findings(duplicate))))
    moved_signed = current.replace(SIGNED_FALSIFIER.encode(), b"- **Falsifier**: moved.\n", 1)
    cases.append(("signed-byte drift", bool(semantic_findings(proposed, moved_signed))))
    already = current + b"\n- **Tree form.** applied in place\n"
    cases.append(("tree form already applied in place", bool(semantic_findings(proposed, already))))

    design_rel = CHANGE / "design.md"
    design_text = proposed[design_rel].decode("utf-8")
    delta = delta_text()
    for arm in ("Gap disclosed in place", "No SVG emitted", "Prose only"):
        cases.append((f"design diagram drops the {arm!r} arm",
                      bool(diagram_findings(design_text.replace(arm, "x", 1), delta))))
        cases.append((f"delta diagram drops the {arm!r} arm",
                      bool(diagram_findings(design_text, delta.replace(arm, "x", 1)))))
    cases.append(("design diagram missing", bool(diagram_findings(
        MERMAID_RE.sub("", design_text), delta))))

    stale = render_manifest(proposed).replace(sha256(proposed[SPEC]), "0" * 64, 1)
    cases.append(("stale manifest", bool(manifest_findings(proposed, stale))))
    short = "".join(render_manifest(proposed).splitlines(keepends=True)[:-1])
    cases.append(("manifest missing a row", bool(manifest_findings(proposed, short))))

    wrong_generated = dict(proposed)
    wrong_generated[GOVERNING] = proposed[GOVERNING].replace(
        sha256(proposed[SPEC]).encode(), b"0" * 64, 1
    )
    cases.append(("wrong generated digest", bool(generated_findings(wrong_generated))))
    unwarranted = dict(proposed)
    unwarranted[SPEC] = proposed[SPEC].replace(
        b"CC-REV-3, CC-REV-8, CC-TEST-5", b"CC-REV-3, CC-REV-99, CC-TEST-5", 1)
    cases.append(("dependencies not regenerated after a warrant edit",
                  bool(generated_findings(unwarranted))))

    repair = CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md"
    moved_repair = dict(proposed)
    assert b"covered:PWB-REQ-013,PWB-REQ-015" in moved_repair[repair]
    moved_repair[repair] = moved_repair[repair].replace(
        b"covered:PWB-REQ-013,PWB-REQ-015", b"covered:PWB-REQ-013,PWB-REQ-999", 1)
    cases.append(("coverage row citing a missing requirement", bool(coverage_findings(moved_repair))))
    cases.append(("the contract-coverage summary needs no regeneration",
                  generated_coverage(proposed) == proposed[CONTRACT_COVERAGE]
                  == read_subjects()[CONTRACT_COVERAGE]))

    with tempfile.TemporaryDirectory() as temp:
        temp_root = pathlib.Path(temp)
        broken = temp_root / "spec.md.patch"
        broken.write_text("not a patch\n", encoding="utf-8")
        broken_findings, _ = check([broken])
        cases.append(("corrupt patch", bool(broken_findings)))

        def make_mirror(name: str) -> pathlib.Path:
            mirror = temp_root / name
            dependency_rels = (
                pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
                pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
            )
            for rel in (SCRIPT, COVERAGE_SCRIPT, CONTRACT_INDEX, *dependency_rels):
                target = mirror / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, target)
            for rel in BEHAVIOR_SUBJECTS:
                target = mirror / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / rel).read_bytes())
            shutil.copytree(ROOT / CANDIDATE, mirror / CANDIDATE)
            parent = pathlib.Path("openspec/changes/three-surface-poc-experience")
            shutil.copytree(ROOT / parent, mirror / parent)
            for record in PERFORMED_SIBLINGS.values():
                source = ROOT / DECISIONS / record
                if source.is_file():
                    target = mirror / DECISIONS / record
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
            for sibling in sibling_spec_patches():
                rel = sibling.relative_to(ROOT)
                target = mirror / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(sibling.read_bytes())
            return mirror

        def run_cli(mirror: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
            return subprocess.run(
                [sys.executable, str(mirror / SCRIPT), *args],
                cwd=mirror, capture_output=True,
            )

        def targets(mirror: pathlib.Path) -> dict[pathlib.Path, bytes]:
            return {rel: (mirror / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}

        mirror = make_mirror("apply-refused")
        before = targets(mirror)
        refused = run_cli(mirror, "--apply")
        cases.append((
            "apply without --at-adoption refuses and writes no signed subject",
            refused.returncode == 2 and targets(mirror) == before,
        ))

        mirror = make_mirror("apply-corrupt")
        before = targets(mirror)
        (mirror / PROPOSED / "design.md.patch").write_text("not a patch\n", encoding="utf-8")
        corrupt = run_cli(mirror, "--apply", "--at-adoption")
        cases.append((
            "apply at adoption with a corrupt patch writes no signed subject",
            corrupt.returncode == 1 and targets(mirror) == before,
        ))

        mirror = make_mirror("apply-stale")
        before = targets(mirror)
        manifest = mirror / MANIFEST
        manifest.write_text(
            manifest.read_text(encoding="utf-8").replace(
                sha256(proposed[SPEC]), "0" * 64, 1),
            encoding="utf-8",
        )
        stale_run = run_cli(mirror, "--apply", "--at-adoption")
        cases.append((
            "apply at adoption with a stale manifest writes no signed subject",
            stale_run.returncode == 1 and targets(mirror) == before,
        ))

        mirror = make_mirror("apply-ok")
        before = targets(mirror)
        applied = run_cli(mirror, "--apply", "--at-adoption")
        after = targets(mirror)
        cases.append((
            "apply at adoption writes exactly the five proposed subjects",
            applied.returncode == 0
            and all(after[rel] == proposed[rel] for rel in BEHAVIOR_SUBJECTS)
            and {rel for rel in BEHAVIOR_SUBJECTS if after[rel] != before[rel]} == PATCHED,
        ))

        # Sibling classification and composition over synthetic patches.
        text = current.decode("utf-8")

        def synthetic(name: str, old: str, new: str, state: str = "pending") -> pathlib.Path:
            assert text.count(old) == 1, old
            moved = text.replace(old, new, 1).encode()
            body = unified_patch(SPEC, current, moved) if state == "pending" else unified_patch(SPEC, moved, current)
            path = temp_root / name / "proposed" / "spec.md.patch"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
            return path

        far = "### Requirement: PWB-REQ-012 — Owner-facing copy is direct and concise"
        pending_far = synthetic("pending-far", far, far + " (x)")
        applied_far = synthetic("applied-far", far, far + " (x)", "applied")
        near = "  ambiguous anchor, missing non-citable attribute, or downstream citation to\n"
        pending_near = synthetic("pending-near", near, near.replace("ambiguous", "unclear"))
        stray_patch = temp_root / "stray" / "proposed" / "spec.md.patch"
        stray_patch.parent.mkdir(parents=True)
        stray_patch.write_text(
            unified_patch(SPEC, b"a line the spec lacks\n", b"another line\n"), encoding="utf-8")
        declined = temp_root / "pwb-scoped-attributes-amendment" / "proposed" / "spec.md.patch"
        declined.parent.mkdir(parents=True)
        declined.write_bytes(stray_patch.read_bytes())

        def handmade(name: str, hunks: list[tuple[str, str]]) -> pathlib.Path:
            path = temp_root / name / "proposed" / "spec.md.patch"
            path.parent.mkdir(parents=True, exist_ok=True)
            body = f"--- a/{SPEC.as_posix()}\n+++ b/{SPEC.as_posix()}\n"
            for old, new in hunks:
                body += f"@@ -1 +1 @@\n-{old}\n+{new}\n"
            path.write_text(body, encoding="utf-8")
            return path

        both_present = handmade("both-present", [(
            "### Requirement: PWB-REQ-012 — Owner-facing copy is direct and concise",
            "### Requirement: PWB-REQ-013 — Proposed work stays subordinate to current project truth")])
        mixed = handmade("mixed", [
            ("### Requirement: PWB-REQ-012 — Owner-facing copy is direct and concise",
             "a replacement line the spec lacks"),
            ("a removed line the spec lacks", "Group: Presentation. Form: **invariant**.")])
        hunkless = temp_root / "hunkless" / "proposed" / "spec.md.patch"
        hunkless.parent.mkdir(parents=True)
        hunkless.write_text(f"--- a/{SPEC.as_posix()}\n+++ b/{SPEC.as_posix()}\n", encoding="utf-8")
        cases.append(("a hunk whose old and new sides both exist is unclassified",
                      patch_state(both_present, current) == "unclassified"))
        cases.append(("a patch with one pending and one applied hunk is unclassified",
                      patch_state(mixed, current) == "unclassified"))
        cases.append(("a patch with no hunk is unclassified",
                      patch_state(hunkless, current) == "unclassified"))
        real_apply = globals()["apply_patches"]
        try:
            counter = iter(range(100))
            globals()["apply_patches"] = lambda _current, _patches: {SPEC: str(next(counter)).encode()}
            order_findings = composition_findings(siblings=[pending_far])
        finally:
            globals()["apply_patches"] = real_apply
        cases.append(("a sibling that composes to different bytes per order is reported",
                      any("order-dependent" in finding for finding in order_findings)))
        states = {
            name: patch_state(path, current)
            for name, path in (("far", pending_far), ("applied", applied_far),
                               ("near", pending_near), ("stray", stray_patch))
        }
        cases.append(("a disjoint unapplied sibling classifies pending", states["far"] == "pending"))
        cases.append(("an already-applied sibling classifies applied", states["applied"] == "applied"))
        cases.append(("a sibling whose text is absent classifies unclassified", states["stray"] == "unclassified"))
        cases.append(("a disjoint pending sibling composes in both orders",
                      composition_findings(siblings=[pending_far]) == []))
        cases.append(("an overlapping pending sibling is reported",
                      bool(composition_findings(siblings=[pending_near]))))
        cases.append(("an unclassified sibling is reported",
                      bool(composition_findings(siblings=[stray_patch]))))
        cases.append(("an applied sibling is not composed",
                      composition_findings(siblings=[applied_far]) == []))
        cases.append(("a declined sibling is skipped by its closed name",
                      composition_findings(siblings=[declined]) == []))
        performed = temp_root / "pwb-item-depth-amendment" / "proposed" / "spec.md.patch"
        performed.parent.mkdir(parents=True)
        performed.write_bytes(stray_patch.read_bytes())
        cases.append(("a listed performed sibling with its record is history",
                      composition_findings(siblings=[performed]) == []))
        cases.append(("a listed performed sibling without its record must classify",
                      bool(composition_findings(siblings=[performed], root=temp_root))))
        unlisted = temp_root / "pwb-unlisted-amendment" / "proposed" / "spec.md.patch"
        unlisted.parent.mkdir(parents=True)
        unlisted.write_bytes(stray_patch.read_bytes())
        cases.append(("an unlisted sibling is never treated as performed",
                      bool(composition_findings(siblings=[unlisted]))))
    population = sibling_population()
    cases.append(("every real sibling spec patch classifies", not population["unclassified"]))
    cases.append(("the real sibling population is the whole tracked set",
                  sum(len(group) for group in population.values()) == len(sibling_spec_patches())))
    first = proposed_bytes()
    second = proposed_bytes()
    cases.append(("deterministic regeneration", first == second and render_manifest(first) == render_manifest(second)))
    partial_findings, _ = check([p for p in patch_files() if patch_target(p) != GOVERNING])
    cases.append(("a landing without the regenerated dependencies", bool(partial_findings)))
    coverage_partial, _ = check([p for p in patch_files()
                                 if patch_target(p) != CHANGE / "CAPABILITY-COVERAGE.md"])
    cases.append(("a landing without the capability-coverage row", bool(coverage_partial)))

    failed = [name for name, caught in cases if not caught]
    for name, caught in cases:
        print(f"selftest: {name}: {'caught' if caught else 'SURVIVED'}")
    if failed:
        print("SELFTEST FAILED: " + ", ".join(failed))
        return 1
    print(f"selftest: {len(cases)} package predicates fail closed")
    return 0


def write() -> int:
    governing_patch = regenerate_governing_patch()
    target = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    target.write_text(governing_patch, encoding="utf-8")
    proposed = proposed_bytes()
    (ROOT / MANIFEST).write_text(render_manifest(proposed), encoding="utf-8")
    print(f"wrote {target.relative_to(ROOT)} and {MANIFEST}")
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
        print("TREE-FRAMING CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    population = sibling_population()
    print(
        f"tree-framing candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects "
        f"({len(PATCHED)} patched); {len(population['pending'])} pending sibling spec "
        f"patches compose ({len(population['applied'])} applied, "
        f"{len(population['performed'])} performed by record, "
        f"{len(population['declined'])} declined, none unclassified)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
