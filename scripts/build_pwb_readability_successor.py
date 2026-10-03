#!/usr/bin/env python3
"""Build and verify the inert PWB readability successor candidate.

The successor restyles the eleven-artifact PWB behavior package for reading
(CC-REV-8) without changing what any requirement requires. The signed
subjects are the effective predecessor: the bytes the item-depth v1.0
sign-off left in place. ``--check`` and ``--write`` apply the candidate's
``proposed/*.patch`` files only in a scratch tree and hash those proposed
bytes. ``--apply --at-adoption`` is the one mode that writes signed subjects;
it exists for ``scripts/record_versioned_signoff.py`` after an owner's
version-tagged sign-off and refuses unless the whole package verifies. A
candidate commit, review, manifest or merge performs no owner act.

What the checks hold fixed, per requirement of the specification:

- the requirement heading, its group/form line, its order and the population
  of seventeen requirements;
- the normative words, compared after removing only layout: line breaks,
  list markers, a line-end hyphen or slash rejoined, and the closed set of
  bold reading labels this package adds;
- the verification block, every scenario and the warrants block, byte for
  byte; and the modal counts (SHALL, SHALL NOT, MAY, MUST).

The Purpose section's reader definitions keep their words the same way; the
added reading guide is checked against the requirement population it lists.
The proposal and design are restyled prose; their claims are classified in
``SEMANTIC-MAP.json`` and judged by review, while the checks hold the
coverage quotations, the relation diagram and the removal of stale status
sentences.

**After sign-off** (syzygy-6bv9, 2026-10-03). The owner signed this package
off as v1.0 on 2026-10-02 (``decisions/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md``).
``--check`` then reported the applied state through ``applied()``. That lasted
until the tree-framing v1.0 sign-off of 2026-10-03 rewrote five of the eleven
subjects. Since then ``applied()`` is false and ``--check`` falls through to
the candidate check. Its predecessor pins and patches no longer match, so it
fails with "stale predecessor" and "patch does not apply". That result means
superseded, not broken. ``--selftest`` builds from the pre-adoption bytes and
fails the same way. To check the bytes in force, run the builder of the latest
sign-off (``build_pwb_tree_framing_amendment.py --check`` as of 2026-10-03).
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_polaris_project_wide_spec_dependencies as dependencies  # noqa: E402
import check_polaris_response_ceiling_reading as ceiling  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-readability-successor"
)
PROPOSED = CANDIDATE / "proposed"
MANIFEST = CANDIDATE / "PWB-READABILITY-SUCCESSOR-MANIFEST.txt"
MANIFEST_OUT = MANIFEST
SEMANTIC_MAP = CANDIDATE / "SEMANTIC-MAP.json"
TITLE = "PWB READABILITY SUCCESSOR MANIFEST"
SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
PROPOSAL = CHANGE / "proposal.md"
DESIGN = CHANGE / "design.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"
CAPABILITY_COVERAGE = CHANGE / "CAPABILITY-COVERAGE.md"
COVERAGE_SCRIPT = pathlib.Path("scripts/build_polaris_project_wide_contract_coverage.py")
CONTRACT_INDEX = pathlib.Path(
    ".syzygy/governance/contracts/candidates/05-CONTRACT-INDEX.yaml"
)
#: The item-depth v1.0 manifest: the link this successor follows.
PREVIOUS_LINK = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-item-depth-amendment/"
    "PWB-ITEM-DEPTH-AMENDMENT-MANIFEST.txt"
)

BEHAVIOR_SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CAPABILITY_COVERAGE,
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
#: The effective predecessor: each subject's digest after the item-depth v1.0
#: sign-off. A tree that differs is a stale predecessor and fails closed.
PREDECESSOR = {
    CHANGE / ".openspec.yaml": "bd2504cb580ca73eeb2510481ca4665ee11e2127360fc0be12c104f347fb515f",
    CAPABILITY_COVERAGE: "a3753f0d6e2ef65bff16532cfe7d26dd39decca46dd2b34b381c9e122fc83da9",
    CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md": "1e4c0c80d5d120647fb616c50dbead8bc3047410771691fc19d154018beb22f6",
    CONTRACT_COVERAGE: "d54acd212916fb83047874484c9e47acd1fade453384403ba600a7b2a0244d9c",
    GOVERNING: "1397920a9b5a1446519517771bc09fc3f95829827b84fce6c732f27d9c1dd013",
    CHANGE / "contract-coverage-matrix/RFC-0001-0003.md": "f28404be66a4241503f2214757d640361751934b2ab308dafeada5c6d2152e50",
    CHANGE / "contract-coverage-matrix/RFC-0004-0006.md": "ec091e743cb95070b30980021f2b5bdf054128161a86f6f8a8bbdf7678ffbc29",
    CHANGE / "contract-coverage-matrix/RFC-0007-0009.md": "6e480d6b94734abd41b15fbdcab1e6d7df9d60f68f0f3f5b0d66f98462728cd0",
    DESIGN: "3cff39a87cb13f780e0758d2b35eb2a3a3d22292dddb08b2777d27cb37463f92",
    PROPOSAL: "3ce6c5ba4db2af6590b63672251db5f2bb177a3941dfb8381e45be87e2c69a9f",
    SPEC: "ae5004a54f46028f8378a46622b41acc512413b1d000b7d4ad350362ca87c78d",
}
PATCHED = {DESIGN, GOVERNING, PROPOSAL, SPEC}
#: Subjects whose proposed bytes are generated from the others, never authored.
DERIVED = frozenset({GOVERNING})
#: Sibling packages the owner declined and never applied
#: (POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md). Closed list.
DECLINED_SIBLINGS = frozenset({"pwb-scoped-attributes-amendment"})
REQUIREMENT_COUNT = 17

#: The bold reading labels this package adds at the head of a requirement's
#: top-level bullets, plus the verification separator. Closed: any other
#: added bold text survives normalization and fails the word comparison.
LABELS = frozenset({
    "Read authority.", "Inputs and disclosure.", "State validity.",
    "Invalid cases.", "Population totals.", "Invalid-case outcome.",
    "Exact subjects.", "Scope of the acts.",
    "Containment.", "Inert code contexts.", "Active content.",
    "Code-context profile.", "Resource envelope.", "Ceilings and breaches.",
    "Complete tuple.", "Aggregates.", "Dismissal records.", "Effect.",
    "Rendering under a dismissal.", "Records that dismiss nothing.",
    "Closed fact population.", "Root-index counts.", "Precedence table.",
    "Owning layer.", "Disagreement.",
    "Reading levels.", "Render modes.", "Withheld sources.", "Gates.",
    "Scroll anchors.", "Machine recovery.",
    "One detail per item.", "Capability matching.", "Three bands.",
    "Contract band contents.", "Relation claim.", "Captured relations.",
    "Relation results.", "Inference and recovery.", "Proposals.",
    "Identity and storage.",
    "What is compared.", "Derived read-only machine views.",
    "Generated editorial draft view.", "Membership.", "Recoverability.",
    "Mandatory prompts.", "Nine answers.", "Readiness.",
    "Relation to PWB-REQ-022.",
    "Success criterion.", "Act state.", "Evaluation inputs.",
    "Closed case population.", "Readiness fields.", "Outcomes.",
})
VERIFICATION = "**Verification.**"
GUIDE_LEAD = "**Reading guide (non-normative).**"
DEFINITIONS_LEAD = "Reader definitions:"
#: Status sentences the predecessor carries that are no longer true.
STALE = (
    (PROPOSAL, "is a candidate and binds nothing until a"),
    (PROPOSAL, "Until that exact act, the 2026-09-02 bytes remain the"),
    (DESIGN, "This amendment remains inert until a later"),
    (DESIGN, "The current shared model contains one manually selected"),
)
STATUS_BANNER = "> **Status:** in force."
CLASSIFICATIONS = ("preserved", "clarified", "changed")
CONSEQUENCES = ("observable", "coverage", "contract", "implementation")

ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
DIFF_TARGET_RE = re.compile(r"^\+\+\+ b/(.+)$", re.MULTILINE)
SOURCE_RE = re.compile(r"^> Source: `spec\.md` sha256 `([0-9a-f]{64})` — ", re.MULTILINE)
REQ_RE = re.compile(r"^### Requirement: (PWB-REQ-\d{3}) — ([^\n]+)$", re.MULTILINE)
SCENARIO_RE = re.compile(r"^#### Scenario: ([^\n]+)$", re.MULTILINE)
BLOCK_RE = re.compile(
    r"^### Requirement: (PWB-REQ-\d{3}) — [^\n]+\n([\s\S]*?)(?=^### Requirement: |\Z)",
    re.MULTILINE,
)
GROUP_RE = re.compile(r"^Group: [^\n]+$", re.MULTILINE)
WARRANT_RE = re.compile(r"```yaml\n(warrants:[\s\S]*?)\n```", re.MULTILINE)
MODAL_RE = re.compile(r"\b(?:SHALL NOT|SHALL|MAY|MUST NOT|MUST)\b")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
OUT_OF_SCOPE_RE = re.compile(r"proposal `Out of scope`, “([^”]+)”")
NON_GOALS_RE = re.compile(r"design `Non-Goals`, “([^”]+)”")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ------------------------------------------------------------------ bytes

def read_subjects(overrides: dict[pathlib.Path, bytes] | None = None,
                  root: pathlib.Path | None = None) -> dict[pathlib.Path, bytes]:
    root = ROOT if root is None else root
    overrides = overrides or {}
    out: dict[pathlib.Path, bytes] = {}
    for rel in BEHAVIOR_SUBJECTS:
        if rel in overrides:
            out[rel] = overrides[rel]
            continue
        path = root / rel
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


def apply_patches(current: dict[pathlib.Path, bytes],
                  patches: list[pathlib.Path]) -> dict[pathlib.Path, bytes]:
    with tempfile.TemporaryDirectory() as temp:
        base = pathlib.Path(temp)
        for rel, body in current.items():
            target = base / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        for patch in patches:
            done = subprocess.run(["git", "apply", "--whitespace=nowarn", str(patch)],
                                  cwd=base, capture_output=True, text=True)
            if done.returncode != 0:
                raise ValueError(f"{patch.name} does not apply: {done.stderr.strip()}")
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def proposed_bytes(overrides: dict[pathlib.Path, bytes] | None = None,
                   patches: list[pathlib.Path] | None = None) -> dict[pathlib.Path, bytes]:
    return apply_patches(read_subjects(overrides),
                         patch_files() if patches is None else patches)


def unified_patch(rel: pathlib.Path, before: bytes, after: bytes) -> str:
    rendered = "".join(difflib.unified_diff(
        before.decode("utf-8").splitlines(keepends=True),
        after.decode("utf-8").splitlines(keepends=True),
        fromfile=f"a/{rel.as_posix()}", tofile=f"b/{rel.as_posix()}", n=2))
    # Blank hunk lines stay prefix-free so the patch has no trailing
    # whitespace; git apply accepts this form (see the sibling PWB patches).
    return rendered.replace("\n \n", "\n\n")


# ------------------------------------------------------------------ words

def normalize(text: str, *, labels: bool) -> str:
    """The words of `text` with layout removed (see the module docstring)."""
    text = re.sub(r"(\w)-[ \t]*\n[ \t]*(\w)", r"\1-\2", text)
    text = re.sub(r"(\S)/[ \t]*\n[ \t]*(\S)", r"\1/\2", text)
    if labels:
        def strip(match: re.Match) -> str:
            return match.group(1) if match.group(2) in LABELS else match.group(0)
        text = re.sub(r"(?m)^([ \t]*- )\*\*([^*\n]+)\*\* ", strip, text)
        text = text.replace("\n" + VERIFICATION + "\n", "\n")
    text = re.sub(r"(?m)^[ \t]*- ", "", text)
    return " ".join(text.split())


def requirement_blocks(text: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in BLOCK_RE.finditer(text)}


def split_block(block: str) -> tuple[str, str, str]:
    """(group line, normative region, verification-onward tail)."""
    group = GROUP_RE.search(block)
    case = block.find("\n- **Case")
    if group is None or case < 0:
        raise ValueError("requirement has no group line or no Case block")
    return group.group(0), block[group.end():case], block[case:]


def purpose_parts(text: str) -> tuple[str, str, str]:
    """(opening, guide, definitions) of the Purpose section."""
    purpose = text.split("\n## ADDED Requirements\n", 1)[0]
    head, definitions = purpose.split(DEFINITIONS_LEAD + "\n", 1)
    if GUIDE_LEAD in head:
        opening, guide = head.split(GUIDE_LEAD, 1)
        return opening, GUIDE_LEAD + guide, definitions
    return head, "", definitions


def spec_findings(spec: str, current: str) -> list[str]:
    findings: list[str] = []
    old_ids, new_ids = REQ_RE.findall(current), REQ_RE.findall(spec)
    if old_ids != new_ids or len(new_ids) != REQUIREMENT_COUNT:
        findings.append("requirement identity, title or order differs from the "
                        f"{REQUIREMENT_COUNT}-requirement predecessor")
    if SCENARIO_RE.findall(current) != SCENARIO_RE.findall(spec):
        findings.append("scenario heading population or order changed")
    old_blocks, new_blocks = requirement_blocks(current), requirement_blocks(spec)
    for rid, _title in old_ids:
        old, new = old_blocks.get(rid), new_blocks.get(rid)
        if old is None or new is None:
            findings.append(f"missing requirement block: {rid}")
            continue
        try:
            old_group, old_body, old_tail = split_block(old)
            new_group, new_body, new_tail = split_block(new)
        except ValueError as error:
            findings.append(f"{rid}: {error}")
            continue
        if old_group != new_group:
            findings.append(f"group/form changed: {rid}")
        if normalize(old_body, labels=False) != normalize(new_body, labels=True):
            findings.append(f"normative words changed: {rid}")
        if (MODAL_RE.findall(" ".join(old_body.split()))
                != MODAL_RE.findall(" ".join(new_body.split()))):
            findings.append(f"modal sequence changed: {rid}")
        if not new_body.endswith("\n\n" + VERIFICATION + "\n"):
            findings.append(f"verification separator missing or moved: {rid}")
        if new_body.count(VERIFICATION) != 1:
            findings.append(f"verification separator not exactly once: {rid}")
        if old_tail != new_tail:
            findings.append(f"verification, scenario or warrant bytes changed: {rid}")
        if WARRANT_RE.findall(old) != WARRANT_RE.findall(new):
            findings.append(f"warrants changed: {rid}")
    old_open, old_guide, old_defs = purpose_parts(current)
    new_open, new_guide, new_defs = purpose_parts(spec)
    if old_guide:
        findings.append("predecessor already carries a reading guide")
    if old_open.rstrip("\n") != new_open.rstrip("\n"):
        findings.append("Purpose opening changed")
    if normalize(old_defs, labels=False) != normalize(new_defs, labels=False):
        findings.append("reader-definition words changed")
    used = set(re.findall(r"(?m)^- \*\*([^*\n]+)\*\* ", "\n".join(
        split_block(block)[1] for block in new_blocks.values() if "\n- **Case" in block)))
    if used != LABELS:
        findings.append("reading labels differ from the closed label set: "
                        f"unused {sorted(LABELS - used)}, unknown {sorted(used - LABELS)}")
    findings.extend(guide_findings(new_guide, spec))
    for label, rel, quote in ceiling.QUOTES:
        if rel == SPEC.as_posix() and ceiling.normalize(quote) not in ceiling.normalize(spec):
            findings.append(f"ceiling-reading quote no longer found: {label}")
    return findings


def guide_findings(guide: str, spec: str) -> list[str]:
    if not guide:
        return ["reading guide missing"]
    findings = []
    if "adds,\nremoves and changes no requirement" not in guide:
        findings.append("reading guide lost its non-normative statement")
    rows = re.findall(r"^\| (PWB-REQ-\d{3}) \| ([^|]+) \| ([^|]+) \|$", guide, re.MULTILINE)
    expected = []
    for rid, block in requirement_blocks(spec).items():
        title = dict(REQ_RE.findall(spec))[rid]
        group = re.search(r"^Group: ([^.]+)\.", block, re.MULTILINE).group(1)
        expected.append((rid, group, title))
    if rows != expected:
        findings.append("reading-guide table differs from the requirement population")
    if len(MERMAID_RE.findall(guide)) != 1:
        findings.append("reading guide must carry exactly one diagram")
    return findings


# ------------------------------------------------------------------ prose

def section(text: str, heading: str) -> str:
    match = re.search(rf"^{re.escape(heading)}\n([\s\S]*?)(?=^#{{1,3}} |\Z)", text, re.MULTILINE)
    return match.group(1) if match else ""


def prose_findings(proposed: dict[pathlib.Path, bytes],
                   current: dict[pathlib.Path, bytes]) -> list[str]:
    findings: list[str] = []
    proposal = proposed[PROPOSAL].decode("utf-8")
    design = proposed[DESIGN].decode("utf-8")
    coverage = proposed[CAPABILITY_COVERAGE].decode("utf-8")
    scope = " ".join(section(proposal, "## Scope").split())
    for quote in OUT_OF_SCOPE_RE.findall(coverage):
        if " ".join(quote.split()) not in scope.split("Out of scope:", 1)[-1]:
            findings.append(f"proposal Out of scope lost a coverage quotation: {quote!r}")
    non_goals = " ".join(design.split("**Non-Goals:**", 1)[-1].split("## ", 1)[0].split())
    for quote in NON_GOALS_RE.findall(coverage):
        if " ".join(quote.split()) not in non_goals:
            findings.append(f"design Non-Goals lost a coverage quotation: {quote!r}")
    for heading in ("## Why", "## What Changes", "## Capabilities", "## Impact"):
        if not re.search(rf"^{re.escape(heading)}$", proposal, re.MULTILINE):
            findings.append(f"proposal lost its {heading!r} section")
    if not proposal.startswith(STATUS_BANNER):
        findings.append("proposal does not open with the present-tense status banner")
    for rel, fragment in STALE:
        text = proposed[rel].decode("utf-8")
        if " ".join(fragment.split()) in " ".join(text.split()):
            findings.append(f"stale status sentence retained in {rel.name}: {fragment!r}")
    old_diagram = [b for b in MERMAID_RE.findall(current[DESIGN].decode("utf-8"))
                   if "NOBOUND" in b]
    new_diagram = [b for b in MERMAID_RE.findall(design) if "NOBOUND" in b]
    if len(old_diagram) != 1 or new_diagram != old_diagram:
        findings.append("design relation diagram changed")
    return findings


def unchanged_findings(proposed: dict[pathlib.Path, bytes],
                       current: dict[pathlib.Path, bytes]) -> list[str]:
    return [f"subject outside the restyle changed: {rel.as_posix()}"
            for rel in BEHAVIOR_SUBJECTS
            if rel not in PATCHED and proposed[rel] != current[rel]]


# ------------------------------------------------------------------ derived

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


def regenerate_governing_patch() -> str:
    semantic = [p for p in patch_files() if patch_target(p) not in DERIVED]
    proposed = proposed_bytes(patches=semantic)
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        raise ValueError("proposed spec warrants do not validate: " + " | ".join(errors))
    return unified_patch(GOVERNING, read_subjects()[GOVERNING], generated.encode())


def coverage_mirror(proposed: dict[pathlib.Path, bytes], temp: pathlib.Path) -> pathlib.Path:
    for rel in (COVERAGE_SCRIPT,
                pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
                pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
                CONTRACT_INDEX):
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


def coverage_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    """The contract-coverage generator's own --check over the proposed bytes."""
    with tempfile.TemporaryDirectory() as temp:
        mirror = coverage_mirror(proposed, pathlib.Path(temp))
        done = subprocess.run([sys.executable, str(mirror / COVERAGE_SCRIPT), "--check"],
                              cwd=mirror, capture_output=True, text=True)
        if done.returncode != 0:
            last = (done.stdout + done.stderr).strip().splitlines() or ["(no output)"]
            return ["contract-coverage --check fails over the proposed bytes: " + last[-1]]
    return []


# ------------------------------------------------------------------ package

def render_manifest(proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        f"# {TITLE}\n"
        "# Candidate: binds nothing until the owner signs off a version of this\n"
        "# package (OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md).\n"
        "# 11 artifacts; rows sorted by codepoint path.\n"
        "# All rows take effect together or none do.\n"
        "# Rows hash PROPOSED bytes; signed openspec bytes remain unchanged.\n"
    )
    return header + "".join(
        f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in BEHAVIOR_SUBJECTS)


def manifest_findings(proposed: dict[pathlib.Path, bytes], actual: str) -> list[str]:
    findings = []
    if actual != render_manifest(proposed):
        findings.append("manifest differs from deterministic proposed-byte regeneration")
    rows = ROW_RE.findall(actual)
    if [path for _sha, path in rows] != [rel.as_posix() for rel in BEHAVIOR_SUBJECTS]:
        findings.append(f"manifest rows are not the eleven signed subjects ({len(rows)} rows)")
    return findings


def predecessor_findings(current: dict[pathlib.Path, bytes]) -> list[str]:
    findings = [f"stale predecessor: {rel.as_posix()} no longer hashes to its pinned digest"
                for rel in BEHAVIOR_SUBJECTS if sha256(current[rel]) != PREDECESSOR[rel]]
    link = ROOT / PREVIOUS_LINK
    if link.is_file():
        rows = {path: sha for sha, path in ROW_RE.findall(link.read_text(encoding="utf-8"))}
        if rows != {rel.as_posix(): PREDECESSOR[rel] for rel in BEHAVIOR_SUBJECTS}:
            findings.append("pinned predecessor is not the item-depth v1.0 manifest")
    else:
        findings.append(f"previous chain link missing: {PREVIOUS_LINK}")
    return findings


def semantic_map_findings(value: object, spec: str) -> list[str]:
    if not isinstance(value, dict):
        return ["semantic map is not an object"]
    findings: list[str] = []
    entries: list[dict] = []
    reqs = value.get("requirements")
    expected = REQ_RE.findall(spec)
    if not isinstance(reqs, list) or [
            (r.get("id"), r.get("title")) for r in reqs if isinstance(r, dict)] != expected:
        findings.append("semantic map requirements are not the ordered 17-requirement population")
        reqs = []
    scenarios = value.get("scenarios")
    expected_scenarios = []
    for rid, block in requirement_blocks(spec).items():
        expected_scenarios.extend((rid, s) for s in SCENARIO_RE.findall(block))
    if not isinstance(scenarios, list) or [
            (s.get("requirement"), s.get("heading")) for s in scenarios
            if isinstance(s, dict)] != expected_scenarios:
        findings.append("semantic map scenarios are not the ordered scenario population")
        scenarios = []
    for row in reqs + scenarios:
        if row.get("classification") != "preserved":
            findings.append(f"requirement or scenario not classified preserved: {row}")
    entries.extend(reqs)
    entries.extend(scenarios)
    for key in ("purpose", "proposal", "design"):
        units = value.get(key)
        if not isinstance(units, list) or not units:
            findings.append(f"semantic map has no {key} units")
            continue
        entries.extend(units)
    for row in entries:
        if not isinstance(row, dict) or row.get("classification") not in CLASSIFICATIONS:
            findings.append(f"semantic map entry without a closed classification: {row!r}")
            continue
        if any(not isinstance(row.get(k), str) or not row.get(k) for k in CONSEQUENCES):
            findings.append(f"semantic map entry lacks a consequence field: {row.get('id') or row.get('unit')}")
    changed = sum(1 for r in entries if isinstance(r, dict) and r.get("classification") == "changed")
    if value.get("changed_count") != changed:
        findings.append(f"semantic map changed_count {value.get('changed_count')} "
                        f"differs from its {changed} changed entries")
    if value.get("baseline_digests") != {
            rel.as_posix(): PREDECESSOR[rel] for rel in BEHAVIOR_SUBJECTS}:
        findings.append("semantic map baseline digests differ from the pinned predecessor")
    return findings


def load_map() -> object:
    try:
        return json.loads((ROOT / SEMANTIC_MAP).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {"error": str(error)}


# ------------------------------------------------------------------ siblings

def sibling_spec_patches() -> list[pathlib.Path]:
    root = ROOT / ".syzygy/governance/contracts/candidates"
    return [patch for patch in sorted(root.glob("*/proposed/spec.md.patch"))
            if patch.parent.parent.name != CANDIDATE.name
            and f"+++ b/{SPEC.as_posix()}" in patch.read_text(encoding="utf-8")]


def _hunk_sides(patch_text: str) -> list[tuple[str, str]]:
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


def patch_state(patch: pathlib.Path, current: bytes) -> str:
    """`applied`, `pending` or `unclassified` against the current spec."""
    text = current.decode("utf-8")
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


def sibling_findings(siblings: list[pathlib.Path] | None = None,
                     current: bytes | None = None) -> list[str]:
    """A restyle must follow every other PWB spec change; none may be pending."""
    siblings = sibling_spec_patches() if siblings is None else siblings
    current = read_subjects()[SPEC] if current is None else current
    findings = []
    for sibling in siblings:
        if sibling.parent.parent.name in DECLINED_SIBLINGS:
            continue
        state = patch_state(sibling, current)
        if state != "applied":
            findings.append(f"sibling spec patch is {state}, so the restyle would not "
                            f"follow it: {sibling.parent.parent.name}")
    return findings


# ------------------------------------------------------------------ check

def check(patches: list[pathlib.Path] | None = None,
          semantic_map: object | None = None) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    findings: list[str] = []
    patches = patch_files() if patches is None else patches
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != PATCHED or len(targets) != len(PATCHED):
        findings.append("patch targets differ from the closed four-subject population: "
                        + ", ".join(sorted(path.as_posix() for path in targets)))
    current = read_subjects()
    findings.extend(predecessor_findings(current))
    try:
        proposed = proposed_bytes(patches=[p for p in patches if patch_target(p) in PATCHED])
    except ValueError as error:
        return findings + [str(error)], None
    spec = proposed[SPEC].decode("utf-8")
    findings.extend(spec_findings(spec, current[SPEC].decode("utf-8")))
    findings.extend(prose_findings(proposed, current))
    findings.extend(unchanged_findings(proposed, current))
    findings.extend(generated_findings(proposed))
    findings.extend(coverage_findings(proposed))
    findings.extend(semantic_map_findings(
        load_map() if semantic_map is None else semantic_map, spec))
    if not (ROOT / MANIFEST).is_file():
        findings.append(f"missing manifest: {MANIFEST}")
    else:
        findings.extend(manifest_findings(proposed, (ROOT / MANIFEST).read_text(encoding="utf-8")))
    findings.extend(sibling_findings())
    return findings, proposed


def applied() -> bool:
    """True once every signed subject carries its manifest row (after sign-off)."""
    if not (ROOT / MANIFEST).is_file():
        return False
    rows = {path: sha for sha, path in
            ROW_RE.findall((ROOT / MANIFEST).read_text(encoding="utf-8"))}
    return bool(rows) and rows == {
        rel.as_posix(): sha256((ROOT / rel).read_bytes()) for rel in BEHAVIOR_SUBJECTS}


# ------------------------------------------------------------------ selftest

def fuzzy(body: bytes, old: str, new: str) -> bytes:
    pattern = r"\s+".join(re.escape(word) for word in old.split())
    replaced, count = re.subn(pattern, lambda _m: new, body.decode("utf-8"), count=1)
    assert count == 1, f"selftest mutant target absent: {old!r}"
    return replaced.encode()


def selftest() -> int:
    findings, proposed = check()
    if findings or proposed is None:
        print("SELFTEST PRECONDITION FAILED:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    current = read_subjects()
    current_spec = current[SPEC].decode("utf-8")
    cases: list[tuple[str, bool]] = []

    def spec_caught(mutated: bytes) -> bool:
        return bool(spec_findings(mutated.decode("utf-8"), current_spec))

    spec_mutants = {
        "weakened modal": ("SHALL NOT read any Butlers project-shape body",
                           "SHOULD NOT read any Butlers project-shape body"),
        "modal swapped for MAY": ("Only state (2) MAY be called independently verified",
                                  "Only state (2) SHALL be called independently verified"),
        "dropped Unknown qualification": ("record class below as Unknown, never as zero",
                                          "record class below as zero"),
        "dropped fail-closed refusal": ("SHALL NOT be served in any mode", "may be served"),
        "dropped refusal clause": ("and never one whose primary reason is",
                                   "including one whose primary reason is"),
        "relabelled outside the closed set": ("**Read authority.**", "**Who may read.**"),
        "added word in a label position": ("**Containment.** The POC", "**Containment.** Today the POC"),
        "renamed requirement": ("PWB-REQ-012 — Owner-facing copy is direct and concise",
                                "PWB-REQ-012 — Owner-facing copy is direct"),
        "renamed scenario": ("#### Scenario: Excluded source fails closed",
                             "#### Scenario: Excluded source fails"),
        "changed oracle": ("exact final encoded-byte counts decide",
                           "approximate final encoded-byte counts decide"),
        "changed warrant": ("primary: SEC-5\n  doctrine: [VIS-1, VIS-2, VIS-7, SEC-5]",
                            "primary: VIS-2\n  doctrine: [VIS-1, VIS-2, VIS-7, SEC-5]"),
        "changed reader definition": ("The vocabulary is closed at nine shapes",
                                      "The vocabulary is open beyond nine shapes"),
        "changed Purpose opening": ("with complete coverage, exact sources and visible gaps",
                                    "with coverage and sources"),
        "verification separator dropped": ("\n**Verification.**\n\n- **Case (counterexample sweep)**",
                                           "\n- **Case (counterexample sweep)**"),
        "reading guide loses its non-normative statement": (
            "adds,\nremoves and changes no requirement", "adds requirements"),
        "reading-guide table names a wrong title": (
            "| PWB-REQ-013 | Presentation | Proposed work stays subordinate to current project truth |",
            "| PWB-REQ-013 | Presentation | Proposed work stays subordinate |"),
        "ceiling-reading quote broken": ("explicit byte ceiling", "explicit ceiling"),
    }
    for name, (old, new) in spec_mutants.items():
        body = proposed[SPEC]
        if "\n" in old:
            assert body.decode("utf-8").count(old) == 1, old
            mutated = body.decode("utf-8").replace(old, new, 1).encode()
        else:
            mutated = fuzzy(body, old, new)
        cases.append((name, spec_caught(mutated)))
    swapped = REQ_RE.findall(proposed[SPEC].decode("utf-8"))
    order = proposed[SPEC].decode("utf-8")
    first = order.index("### Requirement: PWB-REQ-012")
    second = order.index("### Requirement: PWB-REQ-013")
    third = order.index("### Requirement: PWB-REQ-014")
    reordered = order[:first] + order[second:third] + order[first:second] + order[third:]
    cases.append(("reordered requirements", bool(swapped) and spec_caught(reordered.encode())))
    dropped = re.sub(r"### Requirement: PWB-REQ-016[\s\S]*?(?=### Requirement: )", "",
                     order, count=1)
    cases.append(("missing requirement ID", spec_caught(dropped.encode())))

    def prose_caught(rel: pathlib.Path, old: str, new: str) -> bool:
        mutated = dict(proposed)
        mutated[rel] = fuzzy(proposed[rel], old, new)
        return bool(prose_findings(mutated, current))

    cases.append(("out-of-scope quotation dropped",
                  prose_caught(PROPOSAL, "inferring missing capabilities;", "")))
    cases.append(("non-goal quotation dropped",
                  prose_caught(DESIGN, "LLM generation or inference", "Model generation")))
    cases.append(("stale status sentence restored",
                  prose_caught(PROPOSAL, "> **Status:** in force.",
                               "> **Status:** in force. This is a candidate and binds "
                               "nothing until a later sign-off.")))
    cases.append(("status banner removed",
                  prose_caught(PROPOSAL, "> **Status:** in force.", "> **Status:** pending.")))
    cases.append(("relation diagram changed",
                  prose_caught(DESIGN, 'U1["Unknown<br/>missing-declaration"]',
                               'U1["Unknown"]')))
    outside = dict(proposed)
    outside[CAPABILITY_COVERAGE] = proposed[CAPABILITY_COVERAGE] + b"\n"
    cases.append(("unchanged subject edited", bool(unchanged_findings(outside, current))))

    wrong_generated = dict(proposed)
    wrong_generated[GOVERNING] = proposed[GOVERNING].replace(
        sha256(proposed[SPEC]).encode(), b"0" * 64, 1)
    cases.append(("wrong generated digest", bool(generated_findings(wrong_generated))))
    stale_generated = dict(proposed)
    stale_generated[GOVERNING] = current[GOVERNING]
    cases.append(("dependency file not regenerated", bool(generated_findings(stale_generated))))
    broken_coverage = dict(proposed)
    broken_coverage[CONTRACT_COVERAGE] = proposed[CONTRACT_COVERAGE].replace(
        b"**324**", b"**325**", 1)
    cases.append(("contract coverage drift", bool(coverage_findings(broken_coverage))))

    stale = render_manifest(proposed).replace(sha256(proposed[SPEC]), "0" * 64, 1)
    cases.append(("stale manifest", bool(manifest_findings(proposed, stale))))
    short = "".join(line for line in render_manifest(proposed).splitlines(keepends=True)
                    if ".openspec.yaml" not in line)
    cases.append(("ten-row manifest", bool(manifest_findings(proposed, short))))

    drifted = dict(current)
    drifted[DESIGN] = current[DESIGN] + b"\n"
    cases.append(("stale predecessor", bool(predecessor_findings(drifted))))

    smap = load_map()
    assert isinstance(smap, dict)
    spec_text = proposed[SPEC].decode("utf-8")
    for name, mutate in (
            ("semantic map missing an ID", lambda m: m["requirements"].pop()),
            ("semantic map scenario dropped", lambda m: m["scenarios"].pop(0)),
            ("semantic map requirement marked changed",
             lambda m: m["requirements"][0].update(classification="changed")),
            ("semantic map unknown classification",
             lambda m: m["design"][0].update(classification="equivalent")),
            ("semantic map changed count wrong",
             lambda m: m.update(changed_count=m["changed_count"] + 1)),
            ("semantic map consequence missing",
             lambda m: m["proposal"][0].pop("implementation")),
            ("semantic map stale baseline",
             lambda m: m["baseline_digests"].update({SPEC.as_posix(): "0" * 64}))):
        mutated = json.loads(json.dumps(smap))
        mutate(mutated)
        cases.append((name, bool(semantic_map_findings(mutated, spec_text))))

    with tempfile.TemporaryDirectory() as temp:
        temp_root = pathlib.Path(temp)
        broken = temp_root / "spec.md.patch"
        broken.write_text("not a patch\n", encoding="utf-8")
        cases.append(("corrupt patch", bool(check([broken])[0])))
        partial, _ = check([p for p in patch_files() if patch_target(p) != GOVERNING])
        cases.append(("partial apply (no dependency patch)", bool(partial)))
        partial, _ = check([p for p in patch_files() if patch_target(p) != DESIGN])
        cases.append(("partial apply (no design patch)", bool(partial)))
        unknown = temp_root / "tasks.md.patch"
        unknown.write_text(unified_patch(CHANGE / "tasks.md", b"a\n", b"b\n"), encoding="utf-8")
        cases.append(("unknown-source patch target",
                      bool(check(patch_files() + [unknown])[0])))

        def synthetic(name: str, old: str, new: str, state: str) -> pathlib.Path:
            text = current[SPEC].decode("utf-8")
            assert text.count(old) == 1, old
            moved = text.replace(old, new, 1).encode()
            body = (unified_patch(SPEC, current[SPEC], moved) if state == "pending"
                    else unified_patch(SPEC, moved, current[SPEC]))
            path = temp_root / name / "proposed" / "spec.md.patch"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
            return path

        far = "### Requirement: PWB-REQ-012 — Owner-facing copy is direct and concise"
        pending = synthetic("pending", far, far + " (x)", "pending")
        done = synthetic("applied", far, far + " (x)", "applied")
        stray = temp_root / "stray" / "proposed" / "spec.md.patch"
        stray.parent.mkdir(parents=True)
        stray.write_text(unified_patch(SPEC, b"a line the spec lacks\n", b"another\n"),
                         encoding="utf-8")
        declined = temp_root / "pwb-scoped-attributes-amendment" / "proposed" / "spec.md.patch"
        declined.parent.mkdir(parents=True)
        declined.write_bytes(stray.read_bytes())
        cases.append(("a pending sibling (restyle would precede it) is reported",
                      bool(sibling_findings([pending], current[SPEC]))))
        cases.append(("an unclassified sibling is reported",
                      bool(sibling_findings([stray], current[SPEC]))))
        cases.append(("an applied sibling passes", sibling_findings([done], current[SPEC]) == []))
        cases.append(("a declined sibling is skipped by its closed name",
                      sibling_findings([declined], current[SPEC]) == []))

        def make_mirror(name: str) -> pathlib.Path:
            mirror = temp_root / name
            for rel in (pathlib.Path("scripts/build_pwb_readability_successor.py"),
                        pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
                        pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
                        pathlib.Path("scripts/check_polaris_response_ceiling_reading.py"),
                        COVERAGE_SCRIPT, CONTRACT_INDEX, PREVIOUS_LINK):
                target = mirror / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, target)
            for rel in BEHAVIOR_SUBJECTS:
                target = mirror / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(current[rel])
            shutil.copytree(ROOT / CANDIDATE, mirror / CANDIDATE)
            parent = pathlib.Path("openspec/changes/three-surface-poc-experience")
            shutil.copytree(ROOT / parent, mirror / parent)
            for sibling in sibling_spec_patches():
                rel = sibling.relative_to(ROOT)
                (mirror / rel).parent.mkdir(parents=True, exist_ok=True)
                (mirror / rel).write_bytes(sibling.read_bytes())
            return mirror

        def run_cli(mirror: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
            return subprocess.run(
                [sys.executable, str(mirror / "scripts/build_pwb_readability_successor.py"),
                 *args], cwd=mirror, capture_output=True)

        def targets(mirror: pathlib.Path) -> dict[pathlib.Path, bytes]:
            return {rel: (mirror / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}

        mirror = make_mirror("apply-refused")
        before = targets(mirror)
        refused = run_cli(mirror, "--apply")
        cases.append(("apply without --at-adoption refuses and writes no signed subject",
                      refused.returncode == 2 and targets(mirror) == before))
        mirror = make_mirror("apply-corrupt")
        before = targets(mirror)
        (mirror / PROPOSED / "design.md.patch").write_text("not a patch\n", encoding="utf-8")
        corrupt = run_cli(mirror, "--apply", "--at-adoption")
        cases.append(("apply at adoption with a corrupt patch writes no signed subject",
                      corrupt.returncode == 1 and targets(mirror) == before))
        mirror = make_mirror("apply-stale")
        before = targets(mirror)
        (mirror / MANIFEST).write_text((mirror / MANIFEST).read_text(encoding="utf-8").replace(
            sha256(proposed[SPEC]), "0" * 64, 1), encoding="utf-8")
        stale_run = run_cli(mirror, "--apply", "--at-adoption")
        cases.append(("apply at adoption with a stale manifest writes no signed subject",
                      stale_run.returncode == 1 and targets(mirror) == before))
        mirror = make_mirror("apply-ok")
        before = targets(mirror)
        ok = run_cli(mirror, "--apply", "--at-adoption")
        after = targets(mirror)
        cases.append(("apply at adoption writes exactly the four proposed subjects",
                      ok.returncode == 0
                      and all(after[rel] == proposed[rel] for rel in BEHAVIOR_SUBJECTS)
                      and {rel for rel in BEHAVIOR_SUBJECTS if after[rel] != before[rel]}
                      == PATCHED))
        installed = run_cli(mirror, "--check")
        cases.append(("check after apply reports the applied state",
                      installed.returncode == 0 and b"applied" in installed.stdout))

    first_run, second_run = proposed_bytes(), proposed_bytes()
    cases.append(("deterministic regeneration",
                  first_run == second_run
                  and render_manifest(first_run) == render_manifest(second_run)
                  and regenerate_governing_patch() == regenerate_governing_patch()))

    failed = [name for name, caught in cases if not caught]
    for name, caught in cases:
        print(f"selftest: {name}: {'caught' if caught else 'SURVIVED'}")
    if failed:
        print("SELFTEST FAILED: " + ", ".join(failed))
        return 1
    print(f"selftest: {len(cases)} package predicates fail closed")
    return 0


# ------------------------------------------------------------------ modes

def write() -> int:
    target = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    target.write_text(regenerate_governing_patch(), encoding="utf-8")
    (ROOT / MANIFEST).write_text(render_manifest(proposed_bytes()), encoding="utf-8")
    print(f"wrote {target.relative_to(ROOT)} and {MANIFEST}")
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print("refusing: --apply is an adoption-time operation; pass --at-adoption "
              "only through the version-tagged sign-off recorder")
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
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for flag in ("--check", "--selftest", "--diff", "--write", "--apply", "--at-adoption"):
        parser.add_argument(flag, action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        # After sign-off the fixtures need the pre-adoption subjects: run this
        # file's current bytes in an archive of the sign-off's parent commit
        # (syzygy-tmkb). Before sign-off the record is absent and this is None.
        import pwb_signed_selftest
        rerun = pwb_signed_selftest.rerun_before_signoff(
            __file__,
            ".syzygy/governance/decisions/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md",
            "0dbe7ce6038c15b8eaffcfc2512580320614d345",  # parent of sign-off bd47409c
        )
        return selftest() if rerun is None else rerun
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
    if applied():
        print(f"PWB readability successor applied: all {len(BEHAVIOR_SUBJECTS)} signed "
              "subjects carry their manifest rows")
        return 0
    findings, proposed = check()
    if findings:
        print("PWB READABILITY CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    smap = load_map()
    print(f"PWB readability candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects "
          f"({len(PATCHED)} patched, {len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); "
          f"{REQUIREMENT_COUNT} requirement bodies keep their words; "
          f"{len(smap['scenarios'])} scenarios byte-equal; semantic map "
          f"{smap['changed_count']} changed units; "
          f"{len(sibling_spec_patches())} sibling spec patches applied or declined")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
