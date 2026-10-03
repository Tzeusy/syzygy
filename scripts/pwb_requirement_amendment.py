#!/usr/bin/env python3
"""Shared engine for inert PWB candidates that amend one requirement block.

A builder that imports this module declares one ``Amendment``: the candidate
directory, its manifest, the one requirement it touches, the load-bearing
phrases that requirement must carry once each, the signed lines it may
replace, its scenarios and its rule-6 mutants. The engine follows the
class-granular and release-label builders' form: the eleven-artifact PWB
behavior package is bound by the signed PWB sign-offs, so ``--check`` and
``--write`` apply the candidate's ``proposed/*.patch`` files only in a
scratch tree and hash those proposed bytes. ``--apply --at-adoption`` is the
one mode that writes signed subjects; it exists for
``scripts/record_versioned_signoff.py`` after an owner's version-tagged
sign-off and refuses unless the whole package verifies. A candidate commit,
review, manifest or merge performs no owner act.

Only the specification and its generated dependency declaration move. No
warrant moves, so ``CONTRACT-COVERAGE.md`` regenerates byte-identical over
the proposed bytes and ``--write`` refuses if it ever would not. Outside the
one requirement every byte of the specification must survive; inside it,
every signed line must survive except the declared replaced lines.

    --check      verify patches, structure, regeneration, coverage, sibling
                 classification, pending-sibling composition (each pair in
                 both orders, and one result across every order of all
                 pending patches) and the manifest
    --selftest   rule-6 mutants: one per structure predicate (a sample of the
                 required phrases, not each one), plus patch drift, divergent
                 application orders, the order-search cap and an unclassified
                 sibling
    --write      regenerate the derived GOVERNING-DEPENDENCIES patch and the
                 manifest over the proposed bytes
    --diff       print the proposed patches
    --apply --at-adoption   write the proposed bytes (sign-off change only)
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import difflib
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Callable


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_polaris_project_wide_spec_dependencies as dependencies  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"
COVERAGE_SCRIPT = pathlib.Path("scripts/build_polaris_project_wide_contract_coverage.py")
CONTRACT_INDEX = CANDIDATES / "05-CONTRACT-INDEX.yaml"
DECISIONS = pathlib.Path(".syzygy/governance/decisions")

BEHAVIOR_SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "CAPABILITY-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CONTRACT_COVERAGE,
            GOVERNING,
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
PATCHED = frozenset({GOVERNING, SPEC})
#: Subjects whose proposed bytes are generated from the others, never authored.
DERIVED = frozenset({GOVERNING})

#: Every candidate package whose spec patch targets the PWB spec, closed: a
#: sibling is performed (its record exists in decisions/), declined
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
#: Unsigned packages over the same subject. Each touches a different
#: requirement, so their spec patches must compose in either order; the
#: generated declaration is regenerated after whichever is signed second.
PENDING_SIBLINGS = frozenset({
    "pwb-accessible-name-amendment",
    "pwb-anchor-resolution-amendment",
    "pwb-class-granular-extraction-amendment",
    "pwb-opening-index-amendment",
    "pwb-release-label-amendment",
})

DIFF_TARGET_RE = re.compile(r"^\+\+\+ b/(.+)$", re.MULTILINE)
SOURCE_RE = re.compile(r"^> Source: `spec\.md` sha256 `([0-9a-f]{64})` — ", re.MULTILINE)
WARRANTS_RE = re.compile(r"^```yaml\nwarrants:\n.*?^```$", re.MULTILINE | re.DOTALL)


@dataclasses.dataclass(frozen=True)
class Amendment:
    candidate: str
    manifest: str
    title: str
    label: str
    requirement: str
    #: Load-bearing fragments of the proposed block, each exactly once
    #: (whitespace-normalized).
    required_once: tuple[str, ...]
    #: Signed limb-ending lines of the block the amendment extends, and
    #: nothing else; each must survive, less its full stop, as a line prefix.
    replaced: tuple[str, ...]
    kept_scenarios: tuple[str, ...]
    new_scenarios: tuple[str, ...]
    #: (name, old, new, expected finding prefix) over the proposed spec.
    mutants: tuple[tuple[str, str, str, str], ...]
    #: (old, new) over a context line of proposed/spec.md.patch.
    patch_drift: tuple[str, str]
    extra_findings: Callable[[str, str], list[str]] = lambda spec, block: []

    @property
    def directory(self) -> pathlib.Path:
        return CANDIDATES / self.candidate

    @property
    def proposed_dir(self) -> pathlib.Path:
        return self.directory / "proposed"

    @property
    def manifest_path(self) -> pathlib.Path:
        return self.directory / self.manifest


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


def patch_files(amendment: Amendment) -> list[pathlib.Path]:
    return sorted((ROOT / amendment.proposed_dir).glob("*.patch"), key=lambda path: path.name)


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


def proposed_bytes(
    amendment: Amendment, patches: list[pathlib.Path] | None = None
) -> dict[pathlib.Path, bytes]:
    return apply_patches(read_subjects(), patch_files(amendment) if patches is None else patches)


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


def semantic_proposed(amendment: Amendment) -> dict[pathlib.Path, bytes]:
    """Proposed bytes with the derived declaration regenerated, not patched."""
    semantic = [p for p in patch_files(amendment) if patch_target(p) not in DERIVED]
    proposed = proposed_bytes(amendment, patches=semantic)
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        raise ValueError("proposed spec warrants do not validate: " + " | ".join(errors))
    return {**proposed, GOVERNING: generated.encode("utf-8")}


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


def lost_lines(old: str, new: str) -> list[str]:
    remaining = collections.Counter(new.split("\n"))
    lost = []
    for line in old.split("\n"):
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


def spec_findings(amendment: Amendment, proposed: bytes, current: bytes) -> list[str]:
    rid = amendment.requirement
    try:
        new_head, new_blocks = requirement_blocks(proposed.decode("utf-8"))
        old_head, old_blocks = requirement_blocks(current.decode("utf-8"))
    except ValueError as error:
        return [str(error)]
    findings = []
    if new_head != old_head:
        findings.append("the specification text before the requirements changed")
    if [r for r, _ in new_blocks] != [r for r, _ in old_blocks]:
        return findings + ["requirement population or order differs"]
    old = dict(old_blocks)
    for other, block in new_blocks:
        if other != rid and block != old[other]:
            findings.append(f"{other} changed; the amendment touches only {rid}")
    block = dict(new_blocks)[rid]
    lost = [line for line in lost_lines(old[rid], block) if line not in amendment.replaced]
    if lost:
        findings.append(f"signed {rid} line edited or removed: {lost[0]!r}")
    # A replaced line is a signed limb ending that the amendment extends: its
    # signed text, less the closing full stop, must open a proposed line.
    for line in amendment.replaced:
        stem = line.rstrip(".")
        if not any(new.startswith(stem) for new in block.split("\n")):
            findings.append(f"signed {rid} replaced line lost its signed text: {line!r}")
    findings.extend(once_findings(rid, block, amendment.required_once))
    for phrase in amendment.kept_scenarios + amendment.new_scenarios:
        if block.count(phrase + "\n") != 1:
            findings.append(f"{rid} lacks exactly one: {phrase[:60]!r}")
    if WARRANTS_RE.findall(block) != WARRANTS_RE.findall(old[rid]):
        findings.append(f"{rid} warrants changed")
    findings.extend(amendment.extra_findings(proposed.decode("utf-8"), block))
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


def structure_findings(
    amendment: Amendment,
    proposed: dict[pathlib.Path, bytes],
    current: dict[pathlib.Path, bytes],
) -> list[str]:
    return spec_findings(amendment, proposed[SPEC], current[SPEC]) + generated_findings(proposed)


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
    """The coverage generator's --check, and byte-identical regeneration."""
    result, _ = run_coverage(proposed, "--check")
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip().splitlines() or ["no output"]
        return ["contract-coverage --check fails over the proposed bytes: " + output[-1]]
    result, generated = run_coverage(proposed)
    if result.returncode != 0:
        return ["contract-coverage generator fails over the proposed bytes"]
    if generated != proposed[CONTRACT_COVERAGE]:
        return ["CONTRACT-COVERAGE.md would change over the proposed bytes"]
    return []


# --- siblings and manifest ---------------------------------------------------

def sibling_findings(amendment: Amendment, candidates: pathlib.Path | None = None) -> list[str]:
    candidates = candidates or ROOT / CANDIDATES
    findings = []
    for patch in sorted(candidates.glob("*/proposed/spec.md.patch")):
        name = patch.parent.parent.name
        if name == amendment.candidate:
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


def composition_findings(amendment: Amendment, mine: pathlib.Path | None = None) -> list[str]:
    """This spec patch and each pending sibling's must compose, in either order."""
    mine = mine or ROOT / amendment.proposed_dir / "spec.md.patch"
    findings = []
    for name in sorted(PENDING_SIBLINGS - {amendment.candidate}):
        theirs = ROOT / CANDIDATES / name / "proposed/spec.md.patch"
        if not theirs.is_file():
            findings.append(f"pending sibling has no spec patch: {name}")
            continue
        for order in ((mine, theirs), (theirs, mine)):
            with tempfile.TemporaryDirectory() as temp:
                base = pathlib.Path(temp)
                (base / SPEC).parent.mkdir(parents=True, exist_ok=True)
                (base / SPEC).write_bytes((ROOT / SPEC).read_bytes())
                for patch in order:
                    result = subprocess.run(
                        ["git", "apply", "--whitespace=nowarn", "--include", SPEC.as_posix(), str(patch)],
                        cwd=base, capture_output=True, text=True,
                    )
                    if result.returncode != 0:
                        findings.append(
                            f"spec patch does not compose with {name} "
                            f"({'after' if patch is mine else 'before'} it)"
                        )
                        break
    return findings


#: Distinct (spec bytes, patches still to apply) states the all-orders search
#: may visit before it stops and reports instead of answering. Patches that
#: commute reach one state per subset of those applied, 2**n states and
#: n * 2**(n - 1) applications: 32 and 80 for today's five pending patches.
#: The cap admits twelve commuting patches; a larger state space, whether
#: from divergence or a thirteenth patch, stops the search with a finding
#: rather than a long or silent run.
ORDER_STATE_CAP = 4096


def all_orders_findings(
    base: bytes, patches: list[tuple[str, pathlib.Path]], rel: pathlib.Path = SPEC,
    cap: int = ORDER_STATE_CAP,
) -> list[str]:
    """Every application order of ``patches`` over ``base`` gives one result.

    Pairwise composition shows each pair applies both ways; it does not show
    the orders agree, because ``git apply`` relocates a hunk whose context
    moved, so two orders can both succeed and differ. This search covers all
    n! orders exactly: ``git apply`` is a function of its input bytes, so two
    orders that reach the same bytes with the same patches left share every
    outcome from there, and memoizing on that pair visits each distinct state
    once. Any order that fails to apply, or more than one final result, is a
    finding; exceeding ``cap`` states is a finding, never a silent pass.
    """
    findings: list[str] = []
    memo: dict[tuple[bytes, frozenset[str]], frozenset[bytes]] = {}
    paths = dict(patches)
    failures: set[str] = set()
    visited = [0]

    def apply_one(body: bytes, name: str) -> bytes | None:
        with tempfile.TemporaryDirectory() as temp:
            scratch = pathlib.Path(temp)
            (scratch / rel).parent.mkdir(parents=True, exist_ok=True)
            (scratch / rel).write_bytes(body)
            result = subprocess.run(
                ["git", "apply", "--whitespace=nowarn", "--include", rel.as_posix(), str(paths[name])],
                cwd=scratch, capture_output=True, text=True,
            )
            return (scratch / rel).read_bytes() if result.returncode == 0 else None

    def outcomes(body: bytes, left: frozenset[str], applied: tuple[str, ...]) -> frozenset[bytes]:
        key = (body, left)
        if key in memo:
            return memo[key]
        # A key is never re-entered before it is memoized: each step removes
        # a patch, so the count of first visits is the count of states.
        visited[0] += 1
        if visited[0] > cap:
            raise OverflowError
        if not left:
            memo[key] = frozenset({body})
            return memo[key]
        results: set[bytes] = set()
        for name in sorted(left):
            after = apply_one(body, name)
            if after is None:
                failures.add(f"{name} after [{', '.join(applied) or 'nothing'}]")
                continue
            results |= outcomes(after, left - {name}, applied + (name,))
        memo[key] = frozenset(results)
        return memo[key]

    try:
        results = outcomes(base, frozenset(paths), ())
    except OverflowError:
        return [f"composition search exceeded {cap} states over {len(paths)} pending patches; "
                "order-independence is unverified"]
    for failure in sorted(failures):
        findings.append(f"pending spec patches do not apply in every order: {failure}")
    if not results:
        findings.append("pending spec patches have no application order that applies")
    if len(results) > 1:
        findings.append(
            f"pending spec patches give {len(results)} different results across the "
            f"{len(paths)}! application orders"
        )
    return findings


def pending_order_findings(amendment: Amendment, mine: pathlib.Path | None = None) -> list[str]:
    """This patch and every pending sibling's give one result in every order."""
    patches = [(amendment.candidate, mine or ROOT / amendment.proposed_dir / "spec.md.patch")]
    for name in sorted(PENDING_SIBLINGS - {amendment.candidate}):
        theirs = ROOT / CANDIDATES / name / "proposed/spec.md.patch"
        if theirs.is_file():
            patches.append((name, theirs))
    return all_orders_findings((ROOT / SPEC).read_bytes(), patches)


def render_manifest(amendment: Amendment, proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        f"# {amendment.title}\n"
        "# Candidate: binds nothing until the owner signs off a version of this\n"
        "# package (OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md).\n"
        f"# {len(BEHAVIOR_SUBJECTS)} artifacts; rows sorted by codepoint path.\n"
        "# All rows take effect together or none do.\n"
        "# Rows hash PROPOSED bytes; signed openspec bytes remain unchanged.\n"
    )
    rows = "".join(f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in BEHAVIOR_SUBJECTS)
    return header + rows


def check(
    amendment: Amendment, patches: list[pathlib.Path] | None = None
) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    findings: list[str] = []
    patches = patch_files(amendment) if patches is None else patches
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != PATCHED or len(targets) != len(PATCHED):
        findings.append("patch targets differ from the closed two-subject population")
    try:
        proposed = proposed_bytes(amendment, patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    current = read_subjects()
    for rel in BEHAVIOR_SUBJECTS:
        if (proposed[rel] != current[rel]) != (rel in PATCHED):
            findings.append(f"subject change does not match its declaration: {rel.as_posix()}")
    findings.extend(structure_findings(amendment, proposed, current))
    findings.extend(coverage_findings(proposed))
    findings.extend(sibling_findings(amendment))
    findings.extend(composition_findings(amendment))
    findings.extend(pending_order_findings(amendment))
    manifest = ROOT / amendment.manifest_path
    if not manifest.is_file():
        findings.append(f"missing manifest: {amendment.manifest_path}")
    elif manifest.read_text(encoding="utf-8") != render_manifest(amendment, proposed):
        findings.append("manifest differs from deterministic proposed-byte regeneration")
    return findings, proposed


# --- selftest ----------------------------------------------------------------

def _replace(data: bytes, old: str, new: str) -> bytes:
    if old.encode("utf-8") not in data:
        raise AssertionError(f"selftest fixture matched nothing: {old[:60]!r}")
    return data.replace(old.encode("utf-8"), new.encode("utf-8"), 1)


#: Two hunks whose context recurs: each applies before or after the other,
#: but ``git apply`` relocates whichever comes second, so the orders differ.
ORDER_FIXTURE_BASE = b"h\nk\nm\nw\nk\nm\nw\nt\n"
ORDER_FIXTURE_PATCHES = (
    ("fixture-edit", "@@ -2,3 +2,3 @@\n k\n-m\n+n\n w\n"),
    ("fixture-insert", "@@ -2,3 +2,4 @@\n k\n m\n+Z\n w\n"),
)

#: Two copies of one block. The relocating hunk edits the first copy, or the
#: second once the first is changed; with both copies changed it applies
#: nowhere. Every pair applies in both orders; two orders of the three fail.
ORDER_FIXTURE_TRIPLE_BASE = b"h\nx1\nx2\ny\nz1\nz2\ns\nx1\nx2\ny\nz1\nz2\nt\n"
ORDER_FIXTURE_TRIPLE = (
    ("triple-first-copy", "@@ -1,3 +1,3 @@\n h\n-x1\n+X1\n x2\n"),
    ("triple-second-copy", "@@ -7,3 +7,3 @@\n s\n-x1\n+X1\n x2\n"),
    ("triple-relocating", "@@ -2,5 +2,5 @@\n x1\n x2\n-y\n+Y\n z1\n z2\n"),
)
#: The failing state is memoized once, so it is named by the first prefix the
#: sorted search reaches; the other failing order shares its bytes.
ORDER_FIXTURE_TRIPLE_FINDINGS = [
    "pending spec patches do not apply in every order: "
    "triple-relocating after [triple-first-copy, triple-second-copy]",
    "pending spec patches give 2 different results across the 3! application orders",
]

#: Two copies of one block, with the relocating hunk's claimed line nearer the
#: second. Each insertion above shifts both copies down; after one it is still
#: the second copy that ``git apply`` picks, after both it is the first. Every
#: pair of these four patches gives one result in both orders, so a pairwise
#: check passes them all. The first three diverge, but only together; with
#: the fourth, which edits the first copy, the one order that sends the
#: relocating hunk there before the fourth applies fails, and every order
#: that applies agrees.
ORDER_FIXTURE_SHIFT_BASE = b"h\na1\nb1\nf\nk\nm\nw\ng0\nk\nm\nw\nt\n"
ORDER_FIXTURE_SHIFT = (
    ("shift-a", "@@ -2,2 +2,3 @@\n a1\n+A\n b1\n"),
    ("shift-b", "@@ -3,2 +3,3 @@\n b1\n+B\n f\n"),
    ("shift-relocating", "@@ -8,3 +8,3 @@\n k\n-m\n+M\n w\n"),
    ("shift-first-copy", "@@ -4,4 +4,4 @@\n f\n k\n-m\n+D\n w\n"),
)
ORDER_FIXTURE_SHIFT_FINDINGS = {
    3: ["pending spec patches give 2 different results across the 3! application orders"],
    4: ["pending spec patches do not apply in every order: "
        "shift-first-copy after [shift-a, shift-b, shift-relocating]"],
}


def _fixture_patches(temp: pathlib.Path, rel: pathlib.Path, hunks) -> list[tuple[str, pathlib.Path]]:
    patches = []
    for name, hunk in hunks:
        path = temp / f"{name}.patch"
        path.write_text(f"--- a/{rel}\n+++ b/{rel}\n{hunk}", encoding="utf-8")
        patches.append((name, path))
    return patches


def order_selftest(temp: pathlib.Path) -> int:
    """Divergent and failing orders fail the all-orders check while every pair
    of the same patches still applies in both orders."""
    rel = pathlib.Path("fixture.txt")
    patches = _fixture_patches(temp, rel, ORDER_FIXTURE_PATCHES)
    triple = _fixture_patches(temp, rel, ORDER_FIXTURE_TRIPLE)
    failed = 0
    for base, group in ((ORDER_FIXTURE_BASE, patches), (ORDER_FIXTURE_TRIPLE_BASE, triple)):
        for i, first in enumerate(group):
            for second in group[i + 1:]:
                pair = all_orders_findings(base, [first, second], rel)
                if any("do not apply" in finding or "no application order" in finding for finding in pair):
                    print(f"SELFTEST FAILED: fixture pair {first[0]}, {second[0]} does not apply both ways: {pair}")
                    failed += 1
    shift = _fixture_patches(temp, rel, ORDER_FIXTURE_SHIFT)
    for i, first in enumerate(shift):
        for second in shift[i + 1:]:
            pair = all_orders_findings(ORDER_FIXTURE_SHIFT_BASE, [first, second], rel)
            if pair:
                print(f"SELFTEST FAILED: shift fixture pair {first[0]}, {second[0]} gave {pair}")
                failed += 1
    for size, expected in ORDER_FIXTURE_SHIFT_FINDINGS.items():
        found = all_orders_findings(ORDER_FIXTURE_SHIFT_BASE, shift[:size], rel)
        if found != expected:
            print(f"SELFTEST FAILED: {size} shift patches gave {found}")
            failed += 1
    triple_found = all_orders_findings(ORDER_FIXTURE_TRIPLE_BASE, triple, rel)
    if triple_found != ORDER_FIXTURE_TRIPLE_FINDINGS:
        print(f"SELFTEST FAILED: failing orders gave {triple_found}")
        failed += 1
    nowhere = all_orders_findings(b"unrelated\n", patches[:1], rel)
    if "pending spec patches have no application order that applies" not in nowhere:
        print(f"SELFTEST FAILED: a patch that applies nowhere gave {nowhere}")
        failed += 1
    commuting = all_orders_findings(ORDER_FIXTURE_BASE, patches[:1], rel)
    if commuting:
        print(f"SELFTEST FAILED: a single patch gave order findings {commuting}")
        failed += 1
    found = all_orders_findings(ORDER_FIXTURE_BASE, patches, rel)
    if found != ["pending spec patches give 2 different results across the 2! application orders"]:
        print(f"SELFTEST FAILED: divergent orders gave {found}")
        failed += 1
    capped = all_orders_findings(ORDER_FIXTURE_BASE, patches, rel, cap=2)
    if not (len(capped) == 1 and capped[0].startswith("composition search exceeded 2 states")):
        print(f"SELFTEST FAILED: the state cap gave {capped}")
        failed += 1
    return failed


def selftest(amendment: Amendment) -> int:
    rid = amendment.requirement
    proposed = proposed_bytes(amendment)
    current = read_subjects()
    baseline = structure_findings(amendment, proposed, current)
    if baseline:
        print(f"SELFTEST FAILED: the package does not verify before mutation: {baseline}")
        return 1
    spec = proposed[SPEC]
    other = "PWB-REQ-003" if rid != "PWB-REQ-003" else "PWB-REQ-004"
    common = (
        ("other requirement drift", f"### Requirement: {other} — ", f"### Requirement: {other} —  ",
         f"{other} changed"),
        ("preamble drift", "## Purpose\n", "## Purpose (amended)\n",
         "the specification text before the requirements changed"),
        ("signed line edited", f"### Requirement: {rid} — ", f"### Requirement: {rid} – ",
         f"signed {rid} line edited or removed"),
        ("warrant dropped", "\nwarrants:\n  primary: ", "\nwarrants:\n  primary: X",
         f"{rid} warrants changed"),
        ("replaced line truncated", amendment.replaced[0].rstrip("."),
         amendment.replaced[0].rstrip(".")[:-6] + "zzzzzz",
         f"signed {rid} replaced line lost its signed text"),
    )
    failed = 0
    for name, old, new, expected in common + amendment.mutants:
        if name == "warrant dropped":
            block = dict(requirement_blocks(spec.decode("utf-8"))[1])[rid]
            mutated_block = _replace(block.encode("utf-8"), old, new).decode("utf-8")
            mutated = spec.replace(block.encode("utf-8"), mutated_block.encode("utf-8"), 1)
        else:
            mutated = _replace(spec, old, new)
        if mutated == spec:
            print(f"SELFTEST FAILED: mutant {name!r} changed nothing")
            failed += 1
            continue
        changed = {**proposed, SPEC: mutated}
        findings = spec_findings(amendment, mutated, current[SPEC])
        if not any(finding.startswith(expected) for finding in findings):
            print(f"SELFTEST FAILED: mutant {name!r} gave {findings}, expected {expected!r}")
            failed += 1
        if not generated_findings(changed):
            print(f"SELFTEST FAILED: mutant {name!r} left the declaration's digest current")
            failed += 1
    tampered = _replace(proposed[GOVERNING], rid, "PWB-REQ-000")
    if not generated_findings({**proposed, GOVERNING: tampered}):
        print("SELFTEST FAILED: a hand-edited generated declaration passed")
        failed += 1
    spec_patch = ROOT / amendment.proposed_dir / "spec.md.patch"
    with tempfile.TemporaryDirectory() as temp:
        drifted = pathlib.Path(temp) / "spec.md.patch"
        text = spec_patch.read_text(encoding="utf-8")
        old, new = amendment.patch_drift
        mutated_text = text.replace(old, new, 1)
        if mutated_text == text:
            print("SELFTEST FAILED: patch-drift fixture matched nothing")
            failed += 1
        drifted.write_text(mutated_text, encoding="utf-8")
        others = [p for p in patch_files(amendment) if p.name != "spec.md.patch"]
        findings, _ = check(amendment, others + [drifted])
        if not any("does not apply" in finding for finding in findings):
            print(f"SELFTEST FAILED: patch drift gave {findings}")
            failed += 1
        # --check must consult the all-orders predicate: a stand-in for it
        # returns a sentinel that has to reach an otherwise clean run's findings.
        sentinel = "order sentinel: --check consulted the all-orders predicate"
        global pending_order_findings
        real_order_findings = pending_order_findings
        pending_order_findings = lambda *args, **kwargs: [sentinel]  # noqa: E731
        try:
            findings, _ = check(amendment)
        finally:
            pending_order_findings = real_order_findings
        if findings != [sentinel]:
            print(f"SELFTEST FAILED: --check with a sentinel order predicate gave {findings}")
            failed += 1
        if not composition_findings(amendment, mine=drifted):
            print("SELFTEST FAILED: a drifted spec patch composed with the pending siblings")
            failed += 1
        failed += order_selftest(pathlib.Path(temp))
        fake = pathlib.Path(temp) / "candidates"
        (fake / "pwb-unlisted-sibling/proposed").mkdir(parents=True)
        (fake / "pwb-unlisted-sibling/proposed/spec.md.patch").write_text(
            f"--- a/{SPEC.as_posix()}\n+++ b/{SPEC.as_posix()}\n", encoding="utf-8")
        found = sibling_findings(amendment, fake)
        if found != ["unclassified sibling package patches the PWB spec: pwb-unlisted-sibling"]:
            print(f"SELFTEST FAILED: unclassified sibling gave {found}")
            failed += 1
    if failed:
        return 1
    total = len(common) + len(amendment.mutants)
    print(
        f"selftest: {total} structure mutants, declaration tampering, patch drift, "
        "drifted composition, divergent and failing application orders, a patch "
        "that applies nowhere, the order-search cap, "
        "--check's use of the all-orders predicate and "
        "an unclassified sibling all fail closed on their "
        "own predicates"
    )
    return 0


# --- modes -------------------------------------------------------------------

def write(amendment: Amendment) -> int:
    proposed = semantic_proposed(amendment)
    governing = ROOT / amendment.proposed_dir / "GOVERNING-DEPENDENCIES.md.patch"
    governing.write_text(
        unified_patch(GOVERNING, read_subjects()[GOVERNING], proposed[GOVERNING]), encoding="utf-8"
    )
    result, generated = run_coverage(proposed)
    if result.returncode != 0 or generated != proposed[CONTRACT_COVERAGE]:
        print("refusing: CONTRACT-COVERAGE.md would change; this engine patches only the spec")
        return 1
    (ROOT / amendment.manifest_path).write_text(
        render_manifest(amendment, proposed_bytes(amendment)), encoding="utf-8"
    )
    print(f"wrote the derived GOVERNING-DEPENDENCIES patch and {amendment.manifest_path}")
    return 0


def apply(amendment: Amendment, at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is an adoption-time operation; pass --at-adoption "
            "only through the version-tagged sign-off recorder"
        )
        return 2
    findings, proposed = check(amendment)
    if findings or proposed is None:
        print("refusing to apply: package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    for rel in sorted(PATCHED, key=lambda path: path.as_posix()):
        (ROOT / rel).write_bytes(proposed[rel])
        print(f"applied {rel.as_posix()}")
    return 0


def main(amendment: Amendment, argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--at-adoption", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest(amendment)
    if args.apply:
        return apply(amendment, args.at_adoption)
    if args.write:
        return write(amendment)
    if args.diff:
        for patch in patch_files(amendment):
            print(patch.read_text(encoding="utf-8"), end="")
        return 0
    if not args.check:
        print("refusing: choose --check, --selftest, --diff or --write")
        return 2
    findings, proposed = check(amendment)
    if findings:
        print(f"{amendment.label.upper()} CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    _, blocks = requirement_blocks(proposed[SPEC].decode("utf-8"))
    scenarios = proposed[SPEC].decode("utf-8").count("\n#### Scenario: ")
    print(
        f"{amendment.label} candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects "
        f"({len(PATCHED)} patched); {len(blocks)} requirements, {scenarios} scenarios; "
        "structure, regeneration, contract coverage, sibling classification and "
        "pending-sibling composition (pairwise, and one result in every order) verify"
    )
    return 0
