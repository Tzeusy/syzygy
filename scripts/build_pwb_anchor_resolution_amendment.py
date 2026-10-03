#!/usr/bin/env python3
"""Build and verify the inert PWB anchor-resolution amendment candidate.

The amendment adds two obligations to PWB-REQ-014 (bead ``syzygy-u05.9``,
pursuit move N9): every anchor the machine narrative serves takes one shape
and names its block, and every anchored claim block, and the narrative as a
whole, carries an ``anchorsResolved`` pair counted against the machine
answer. The pair counts resolution and never confers authority: every
narrative unit stays ``non-citable``, as signed PWB-REQ-014 and accepted RFC7-3
require. The current eleven-artifact PWB behavior package is bound by the
signed PWB sign-offs, so ``--check`` and ``--write`` apply the candidate's
``proposed/*.patch`` files only in a scratch tree and hash those proposed
bytes. ``--apply --at-adoption`` is the one mode that writes signed subjects;
it exists for the sign-off change and refuses unless the whole package
verifies. A candidate commit, review, manifest or merge performs no owner act.

    --check      verify patches, structure, regeneration, coverage, siblings,
                 composition with each pending sibling and the manifest
    --selftest   rule-6 mutants, one per structure predicate (a sample of the
                 required phrases, not each one), plus patch drift, an
                 unclassified sibling and a non-composing sibling
    --write      regenerate the derived GOVERNING-DEPENDENCIES patch and the
                 manifest over the proposed bytes
    --diff       print the proposed patches
    --apply --at-adoption   write the proposed bytes (sign-off change only)

The checking engine is family-neutral: ``Package`` names one specification
change, its subjects, its target requirements and its siblings, and the
Three-Surface POC block-provenance builder drives the same engine with its
own ``Package``. Outside the target requirements every requirement block and
the text before the first requirement must survive byte for byte; inside
them every signed line must survive except the declared replaced lines, and
the warrants block may not move, so no contract-coverage row moves either.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import difflib
import hashlib
import importlib
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Callable


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
DIFF_TARGET_RE = re.compile(r"^\+\+\+ b/(.+)$", re.MULTILINE)
SOURCE_RE = re.compile(r"^> Source: `spec\.md` sha256 `([0-9a-f]{64})` — ", re.MULTILINE)
WARRANTS_RE = re.compile(r"```yaml\nwarrants:\n.*?```", re.DOTALL)


@dataclasses.dataclass(frozen=True)
class Target:
    """One requirement the package amends, and what its proposed text must hold."""

    req_id: str
    #: Load-bearing fragments; each must occur exactly once, whitespace-normalized.
    required_once: tuple[str, ...]
    #: Signed lines the amendment replaces, and nothing else.
    replaced: tuple[str, ...]
    #: Every scenario heading the proposed block carries, in order.
    scenarios: tuple[str, ...]
    #: Exact occurrence counts of tokens (regular expressions) in the proposed
    #: block, so an inserted sentence that names one fails even when every
    #: required phrase survives.
    token_counts: tuple[tuple[str, int], ...] = ()


@dataclasses.dataclass(frozen=True)
class Package:
    label: str
    candidate: pathlib.Path
    manifest: pathlib.Path
    title: str
    change: pathlib.Path
    spec: pathlib.Path
    governing: pathlib.Path
    subjects: tuple[pathlib.Path, ...]
    patched: frozenset[pathlib.Path]
    generator: str
    req_prefix: str
    targets: tuple[Target, ...]
    #: Sibling packages whose spec patch targets the same specification, closed.
    performed_siblings: dict[str, str]
    declined_siblings: frozenset[str]
    pending_siblings: frozenset[str]
    coverage: Callable[[dict[pathlib.Path, bytes]], list[str]] | None = None

    @property
    def proposed_dir(self) -> pathlib.Path:
        return self.candidate / "proposed"

    @property
    def derived(self) -> frozenset[pathlib.Path]:
        return frozenset({self.governing})


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def flat(text: str) -> str:
    return " ".join(text.split())


# --- proposed bytes ------------------------------------------------------------

def read_subjects(pkg: Package) -> dict[pathlib.Path, bytes]:
    out: dict[pathlib.Path, bytes] = {}
    for rel in pkg.subjects:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"missing subject: {rel}")
        out[rel] = path.read_bytes()
    return out


def patch_files(pkg: Package) -> list[pathlib.Path]:
    return sorted((ROOT / pkg.proposed_dir).glob("*.patch"), key=lambda path: path.name)


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
        return {rel: (base / rel).read_bytes() for rel in current}


def proposed_bytes(pkg: Package, patches: list[pathlib.Path] | None = None) -> dict[pathlib.Path, bytes]:
    return apply_patches(read_subjects(pkg), patch_files(pkg) if patches is None else patches)


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
    # Blank context lines stay prefix-free, as in the sibling patches.
    return rendered.replace("\n \n", "\n\n")


def generate(pkg: Package, spec_text: str) -> tuple[str | None, list[str]]:
    return importlib.import_module(pkg.generator).generate(spec_text)


def regenerate_governing_patch(pkg: Package) -> str:
    semantic = [p for p in patch_files(pkg) if patch_target(p) not in pkg.derived]
    proposed = proposed_bytes(pkg, patches=semantic)
    generated, errors = generate(pkg, proposed[pkg.spec].decode("utf-8"))
    if errors or generated is None:
        raise ValueError("proposed spec warrants do not validate: " + " | ".join(errors))
    return unified_patch(pkg.governing, read_subjects(pkg)[pkg.governing], generated.encode())


# --- structure ---------------------------------------------------------------

def requirement_blocks(pkg: Package, spec: str) -> tuple[str, list[tuple[str, str]]]:
    parts = re.split(r"(?m)^(?=### Requirement: )", spec)
    blocks = []
    for part in parts[1:]:
        match = re.match(rf"### Requirement: ({re.escape(pkg.req_prefix)}\d{{3}}) — ", part)
        if match is None:
            raise ValueError("unparseable requirement heading")
        blocks.append((match.group(1), part))
    return parts[0], blocks


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


def spec_findings(pkg: Package, proposed: bytes, current: bytes) -> list[str]:
    try:
        new_head, new_blocks = requirement_blocks(pkg, proposed.decode("utf-8"))
        old_head, old_blocks = requirement_blocks(pkg, current.decode("utf-8"))
    except ValueError as error:
        return [str(error)]
    findings = []
    if new_head != old_head:
        findings.append("the specification text before the first requirement changed")
    if [rid for rid, _ in new_blocks] != [rid for rid, _ in old_blocks]:
        return findings + ["requirement population or order differs"]
    old, new = dict(old_blocks), dict(new_blocks)
    targets = {target.req_id: target for target in pkg.targets}
    for rid, block in new_blocks:
        if rid not in targets and block != old[rid]:
            findings.append(f"{rid} changed; the amendment touches only {', '.join(targets)}")
    for rid, target in targets.items():
        block = new[rid]
        lost = [line for line in lost_lines(old[rid], block) if line not in target.replaced]
        if lost:
            findings.append(f"signed {rid} line edited or removed: {lost[0]!r}")
        findings.extend(once_findings(rid, block, target.required_once))
        headings = tuple(re.findall(r"(?m)^#### Scenario: .*$", block))
        if headings != target.scenarios:
            findings.append(f"{rid} scenario population differs: {headings}")
        if WARRANTS_RE.findall(block) != WARRANTS_RE.findall(old[rid]):
            findings.append(f"{rid} warrants changed")
        for token, expected in target.token_counts:
            found = len(re.findall(token, block))
            if found != expected:
                findings.append(f"{rid} carries {found} matches of token {token!r}, expected {expected}")
    return findings


def generated_findings(pkg: Package, proposed: dict[pathlib.Path, bytes]) -> list[str]:
    text = proposed[pkg.governing].decode("utf-8")
    match = SOURCE_RE.search(text)
    if match is None:
        return ["proposed GOVERNING-DEPENDENCIES has no source digest"]
    if match.group(1) != sha256(proposed[pkg.spec]):
        return ["proposed GOVERNING-DEPENDENCIES does not name the proposed spec digest"]
    generated, errors = generate(pkg, proposed[pkg.spec].decode("utf-8"))
    if errors or generated is None:
        return ["proposed specification warrants do not validate: " + " | ".join(errors)]
    if text != generated:
        return ["proposed GOVERNING-DEPENDENCIES differs from regeneration"]
    return []


def structure_findings(
    pkg: Package, proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]
) -> list[str]:
    return spec_findings(pkg, proposed[pkg.spec], current[pkg.spec]) + generated_findings(pkg, proposed)


# --- siblings ----------------------------------------------------------------

def sibling_patches(pkg: Package, candidates: pathlib.Path | None = None) -> dict[str, pathlib.Path]:
    candidates = candidates or ROOT / CANDIDATES
    found = {}
    for patch in sorted(candidates.glob("*/proposed/spec.md.patch")):
        name = patch.parent.parent.name
        if name == pkg.candidate.name:
            continue
        try:
            if patch_target(patch) != pkg.spec:
                continue
        except ValueError:
            continue
        found[name] = patch
    return found


def sibling_findings(pkg: Package, candidates: pathlib.Path | None = None) -> list[str]:
    findings = []
    found = sibling_patches(pkg, candidates)
    for name in found:
        if name in pkg.declined_siblings or name in pkg.pending_siblings:
            continue
        record = pkg.performed_siblings.get(name)
        if record is None:
            findings.append(f"unclassified sibling package patches the spec: {name}")
        elif not (ROOT / DECISIONS / record).is_file():
            findings.append(f"sibling {name} is listed performed but its record is missing: {record}")
    for name in sorted(pkg.pending_siblings - set(found)):
        findings.append(f"pending sibling has no spec patch: {name}")
    return findings


def composition_findings(
    pkg: Package, spec_bytes: bytes | None = None, siblings: dict[str, pathlib.Path] | None = None
) -> list[str]:
    """This spec patch and each pending sibling's compose to one spec in either order."""
    mine = ROOT / pkg.proposed_dir / "spec.md.patch"
    spec_bytes = (ROOT / pkg.spec).read_bytes() if spec_bytes is None else spec_bytes
    siblings = sibling_patches(pkg) if siblings is None else siblings
    findings = []
    for name in sorted(pkg.pending_siblings):
        sibling = siblings.get(name)
        if sibling is None:
            continue
        try:
            first = apply_patches({pkg.spec: spec_bytes}, [sibling, mine])[pkg.spec]
            second = apply_patches({pkg.spec: spec_bytes}, [mine, sibling])[pkg.spec]
        except ValueError as error:
            findings.append(f"composition with pending sibling {name} fails: {error}")
            continue
        if first != second:
            findings.append(f"composition with pending sibling {name} depends on order")
            continue
        _, errors = generate(pkg, first.decode("utf-8"))
        if errors:
            findings.append(f"composed spec with {name} has invalid warrants: " + " | ".join(errors))
    return findings


# --- manifest and check --------------------------------------------------------

def render_manifest(pkg: Package, proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        f"# {pkg.title}\n"
        "# Candidate: binds nothing until the owner signs off a version of this\n"
        "# package (OWNER-DECISION-PACKET.md beside this file names the route).\n"
        f"# {len(pkg.subjects)} artifacts; rows sorted by codepoint path.\n"
        "# All rows take effect together or none do.\n"
        "# Rows hash PROPOSED bytes; signed openspec bytes remain unchanged.\n"
    )
    rows = "".join(f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in pkg.subjects)
    return header + rows


def check(pkg: Package, patches: list[pathlib.Path] | None = None) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    findings: list[str] = []
    patches = patch_files(pkg) if patches is None else patches
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != pkg.patched or len(targets) != len(pkg.patched):
        findings.append("patch targets differ from the declared patched subjects")
    try:
        proposed = proposed_bytes(pkg, patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    current = read_subjects(pkg)
    for rel in pkg.subjects:
        if (proposed[rel] != current[rel]) != (rel in pkg.patched):
            findings.append(f"subject change does not match its declaration: {rel.as_posix()}")
    findings.extend(structure_findings(pkg, proposed, current))
    if pkg.coverage is not None:
        findings.extend(pkg.coverage(proposed))
    findings.extend(sibling_findings(pkg))
    findings.extend(composition_findings(pkg))
    if not (ROOT / pkg.manifest).is_file():
        findings.append(f"missing manifest: {pkg.manifest}")
    elif (ROOT / pkg.manifest).read_text(encoding="utf-8") != render_manifest(pkg, proposed):
        findings.append("manifest differs from deterministic proposed-byte regeneration")
    return findings, proposed


# --- selftest ----------------------------------------------------------------

def replace_once(data: bytes, old: str, new: str) -> bytes:
    """Replace the one occurrence of `old`'s words, matching any whitespace
    between them, so a fixture survives a re-wrap of the text."""
    words = [re.escape(word) for word in old.split()]
    pattern = re.compile(r"\s+".join(words).encode("utf-8"))
    if len(pattern.findall(data)) != 1:
        raise AssertionError(f"selftest fixture does not match exactly once: {old[:60]!r}")
    return pattern.sub(lambda _match: new.encode("utf-8"), data, count=1)


UNQUOTE = str.maketrans("", "", "'\"")


def run_selftest(
    pkg: Package,
    mutants: dict[str, tuple[pathlib.Path, bytes, str]],
    context_line: tuple[str, str],
) -> int:
    """Each mutant must fail on its own predicate; then patch drift and siblings."""
    proposed = proposed_bytes(pkg)
    current = read_subjects(pkg)
    baseline = structure_findings(pkg, proposed, current)
    if baseline:
        print(f"SELFTEST FAILED: the package does not verify before mutation: {baseline}")
        return 1
    failed = 0
    for name, (rel, mutated, expected) in mutants.items():
        if mutated == proposed[rel]:
            print(f"SELFTEST FAILED: mutant {name!r} changed nothing")
            failed += 1
            continue
        findings = structure_findings(pkg, {**proposed, rel: mutated}, current)
        # repr() picks its quote by content, so compare with quotes removed.
        unquoted = expected.translate(UNQUOTE)
        if not any(finding.translate(UNQUOTE).startswith(unquoted) for finding in findings):
            print(f"SELFTEST FAILED: mutant {name!r} gave {findings}, expected {expected!r}")
            failed += 1
    spec_patch = ROOT / pkg.proposed_dir / "spec.md.patch"
    with tempfile.TemporaryDirectory() as temp:
        # Patch drift: a corrupted context line stops the spec patch applying.
        drifted = pathlib.Path(temp) / "spec.md.patch"
        text = spec_patch.read_text(encoding="utf-8")
        mutated_text = text.replace(context_line[0], context_line[1], 1)
        if mutated_text == text:
            print("SELFTEST FAILED: patch-drift fixture matched nothing")
            failed += 1
        drifted.write_text(mutated_text, encoding="utf-8")
        others = [p for p in patch_files(pkg) if p.name != "spec.md.patch"]
        findings, _ = check(pkg, others + [drifted])
        if not any("does not apply" in finding for finding in findings):
            print(f"SELFTEST FAILED: patch drift gave {findings}")
            failed += 1
        # An unclassified sibling that patches the spec fails closed, and a
        # declared pending sibling that has disappeared is named.
        fake = pathlib.Path(temp) / "candidates"
        (fake / "unlisted-sibling/proposed").mkdir(parents=True)
        (fake / "unlisted-sibling/proposed/spec.md.patch").write_text(
            f"--- a/{pkg.spec.as_posix()}\n+++ b/{pkg.spec.as_posix()}\n", encoding="utf-8")
        found = sibling_findings(pkg, fake)
        expected = ["unclassified sibling package patches the spec: unlisted-sibling"] + [
            f"pending sibling has no spec patch: {name}" for name in sorted(pkg.pending_siblings)
        ]
        if found != expected:
            print(f"SELFTEST FAILED: sibling classification gave {found}")
            failed += 1
        # A pending sibling whose patch rewrites a line this patch also
        # rewrites must fail composition.
        spec_text = (ROOT / pkg.spec).read_text(encoding="utf-8")
        first = next(line for line in pkg.targets[0].replaced if line.strip())
        clash = pathlib.Path(temp) / "clash.patch"
        clash.write_text(
            unified_patch(pkg.spec, spec_text.encode(), spec_text.replace(first, first + " (clash)", 1).encode()),
            encoding="utf-8",
        )
        name = sorted(pkg.pending_siblings)[0] if pkg.pending_siblings else "clash"
        found = composition_findings(
            dataclasses.replace(pkg, pending_siblings=frozenset({name})), siblings={name: clash})
        if not any(f.startswith(f"composition with pending sibling {name}") for f in found):
            print(f"SELFTEST FAILED: a clashing sibling composed: {found}")
            failed += 1
    if failed:
        return 1
    print(
        f"selftest: {len(mutants)} structure mutants, patch drift, an unclassified "
        "sibling, a vanished pending sibling and a clashing sibling all fail closed "
        "on their own predicates"
    )
    return 0


# --- modes -------------------------------------------------------------------

def write(pkg: Package) -> int:
    governing = ROOT / pkg.proposed_dir / f"{pkg.governing.name}.patch"
    governing.write_text(regenerate_governing_patch(pkg), encoding="utf-8")
    (ROOT / pkg.manifest).write_text(render_manifest(pkg, proposed_bytes(pkg)), encoding="utf-8")
    print(f"wrote the derived {pkg.governing.name} patch and {pkg.manifest}")
    return 0


def apply(pkg: Package, at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is an adoption-time operation; pass --at-adoption "
            "only in the sign-off change"
        )
        return 2
    findings, proposed = check(pkg)
    if findings or proposed is None:
        print("refusing to apply: package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    for rel in sorted(pkg.patched, key=lambda path: path.as_posix()):
        (ROOT / rel).write_bytes(proposed[rel])
        print(f"applied {rel.as_posix()}")
    return 0


def main(pkg: Package, selftest: Callable[[], int], argv: list[str]) -> int:
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
        return apply(pkg, args.at_adoption)
    if args.write:
        return write(pkg)
    if args.diff:
        for patch in patch_files(pkg):
            print(patch.read_text(encoding="utf-8"), end="")
        return 0
    if not args.check:
        print("refusing: choose --check, --selftest, --diff or --write")
        return 2
    findings, proposed = check(pkg)
    if findings:
        print(f"{pkg.label.upper()} CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    _, blocks = requirement_blocks(pkg, proposed[pkg.spec].decode("utf-8"))
    scenarios = proposed[pkg.spec].decode("utf-8").count("\n#### Scenario: ")
    print(
        f"{pkg.label} candidate matches {len(pkg.subjects)} proposed subjects "
        f"({len(pkg.patched)} patched); {len(blocks)} requirements, {scenarios} scenarios; "
        "structure, regeneration, siblings, composition and the manifest verify"
    )
    return 0


# --- this package --------------------------------------------------------------

CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"
COVERAGE_SCRIPT = pathlib.Path("scripts/build_polaris_project_wide_contract_coverage.py")
CONTRACT_INDEX = CANDIDATES / "05-CONTRACT-INDEX.yaml"
CANDIDATE = CANDIDATES / "pwb-anchor-resolution-amendment"

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

REQ_014 = Target(
    req_id="PWB-REQ-014",
    required_once=(
        "Every anchor the machine narrative serves SHALL take one shape:",
        "its own identity, which begins with the identity of the one block it belongs to followed by `#`; its target class and target identity; its revision; the claims of that block it supports; the target's captured label, tier and reason; and its locator.",
        "The machine narrative SHALL carry an `anchorsResolved` pair on each anchored claim block, and one for the whole narrative:",
        "An anchor resolves when the machine answer at the same evaluation serves exactly one record with an `identity` field of its own whose whole value equals the anchor's target identity.",
        "A field that refers to another record's identity, such as a stamp's or a support's source identity, is a reference and not a record's own identity, and an identity composed from other fields counts for nothing.",
        "An anchor whose target the machine answer does not serve, or serves without an identity of its own, does not resolve.",
        "It is not the relation RFC7-3 forbids, under which something resolves to Polaris as its authority.",
        "Both numbers are counted, never estimated, and the narrative's pair is the sum of its blocks' pairs.",
        "A count below its total SHALL be served as counted, never rounded up, omitted or rendered as a pass.",
        "When the machine answer at that evaluation serves no record with an identity of its own, every pair is Unknown with its reason, never a count.",
        "The pair counts resolution and never confers authority.",
        "A block whose every anchor resolves stays `presentation-artifact` and `non-citable`;",
        "no field derived from the pair SHALL make a narrative unit citable or stand in for an epistemic label.",
        "The pair is itself presentation: no evidence, snapshot input or status claim SHALL take it as input.",
        "An opening carries no anchor set, so it carries no pair",
        "The pair is a machine-narrative field, not a project-shape claim, and Polaris need not render it.",
        "then withhold one resolved target's identity from the machine answer and resolve again, and withhold every identity and resolve once more.",
        "and its identity begins with the identity of the block that serves it followed by `#`.",
        "An independent resolver that reads only the machine narrative's anchors and the machine answer's bytes at the same evaluation, and imports no rendering code, reproduces each block's `anchorsResolved` pair and the narrative's pair exactly;",
        "withholding one resolved target's identity lowers the resolved count of exactly the blocks anchored to it, by the number of their anchors that name it, and every such block stays non-citable; withholding every identity turns every pair Unknown.",
        "Expected resolution counts come from that independent resolver, never from the narrative builder.",
        "an anchor missing a field of the one shape or naming no block or another block;",
        "a pair that differs from the independent count, is rounded up, or is a count where it should be Unknown; or a narrative unit made citable, or a status claim fed, by its pair.",
        "the block's `anchorsResolved` pair is 2 of 3",
        "the block stays `non-citable` presentation, exactly as it would at 3 of 3",
        # The signed non-citability obligations this amendment leaves in force.
        "Every owner-visible narrative unit SHALL carry `presentation-artifact` and `non-citable` attributes",
        "No project artifact, evidence, snapshot input, work warrant or internal relation SHALL cite Polaris as its authority.",
    ),
    replaced=(
        "  element's presence and each excluded SVG construct in turn.",
        "  targets Polaris.",
        "  an emitted SVG only when the independent allow-list scan passes it.",
        "  independent allow-list scan, not the renderer.",
        "  diagram without its text equivalent; or an emitted SVG outside the",
        "  allow-list.",
    ),
    scenarios=(
        "#### Scenario: A project claim is supported without making Polaris authority",
        "#### Scenario: A group opens with its answer",
        "#### Scenario: An opening over an Unknown child is never more favourable",
        "#### Scenario: An opening above Butlers text stays outside it",
        "#### Scenario: A supported relationship is drawn inertly",
        "#### Scenario: A partly supported relationship names what it leaves out",
        "#### Scenario: A relationship with no supported edge is disclosed, not drawn",
        "#### Scenario: A failed or unsafe diagram emits nothing active",
        "#### Scenario: Anchor resolution is counted, never made authority",
    ),
    # Nine mentions of citability, all of them prohibitions or the signed
    # attribute; no permissive modal at all.
    token_counts=((r"citable", 9), (r"\bMAY\b", 0)),
)


def run_coverage(proposed: dict[pathlib.Path, bytes]) -> subprocess.CompletedProcess:
    """The contract-coverage generator's own --check, in a scratch mirror of the proposed bytes."""
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
        return subprocess.run(
            [sys.executable, str(mirror / COVERAGE_SCRIPT), "--check"],
            cwd=mirror, capture_output=True, text=True,
        )


def coverage_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    result = run_coverage(proposed)
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip().splitlines() or ["no output"]
        return ["contract-coverage --check fails over the proposed bytes: " + output[-1]]
    return []


PACKAGE = Package(
    label="PWB anchor-resolution",
    candidate=CANDIDATE,
    manifest=CANDIDATE / "PWB-ANCHOR-RESOLUTION-AMENDMENT-MANIFEST.txt",
    title="PWB ANCHOR-RESOLUTION AMENDMENT MANIFEST",
    change=CHANGE,
    spec=SPEC,
    governing=GOVERNING,
    subjects=BEHAVIOR_SUBJECTS,
    patched=frozenset({GOVERNING, SPEC}),
    generator="build_polaris_project_wide_spec_dependencies",
    req_prefix="PWB-REQ-",
    targets=(REQ_014,),
    # Same closed classification as the class-granular builder's, re-derived
    # 2026-10-03 from decisions/ and the candidates/ glob.
    performed_siblings={
        "pwb-container-shape-profile-amendment": "PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md",
        "pwb-dismissal-expiry-amendment": "PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md",
        "pwb-exact-source-render-mode-scenario": "PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md",
        "pwb-item-depth-amendment": "PWB-ITEM-DEPTH-AMENDMENT-SIGNOFF-v1.0.md",
        "pwb-machine-view-amendment": "PWB-MACHINE-VIEW-AMENDMENT-ACT.md",
        "pwb-missing-currency-disclosure-scenario": "PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md",
        "pwb-opening-band-scenario": "PWB-OPENING-BAND-SCENARIO-ACT.md",
        "pwb-readability-successor": "PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md",
        "pwb-tree-framing-amendment": "PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md",
    },
    declined_siblings=frozenset({"pwb-scoped-attributes-amendment"}),
    #: Unsigned packages over the same subject. Neither touches PWB-REQ-014, so
    #: the spec patches compose in either order; the dependency declaration's
    #: one Source line is rewritten by each, so whichever is signed later is
    #: regenerated with --write over the earlier one's applied bytes.
    pending_siblings=frozenset({
        "pwb-class-granular-extraction-amendment",
        "pwb-release-label-amendment",
    }),
    coverage=coverage_findings,
)


def selftest() -> int:
    pkg = PACKAGE
    proposed = proposed_bytes(pkg)
    spec = proposed[SPEC]
    phrase = "PWB-REQ-014 carries 0 copies of required phrase: "
    mutants = {
        "other requirement drift": (
            SPEC, replace_once(spec, "### Requirement: PWB-REQ-015 — Item detail preserves authority bands and exact intent\n", "### Requirement: PWB-REQ-015 — Item detail preserves authority bands\n"),
            "PWB-REQ-015 changed",
        ),
        "preamble drift": (
            SPEC, replace_once(spec, "## Purpose\n", "## Purpose (amended)\n"),
            "the specification text before the first requirement changed",
        ),
        "signed line edited": (
            SPEC, replace_once(spec, "- Narrative claim blocks SHALL use a machine type distinct from kernel Claim.\n", "- Narrative claim blocks SHALL use a machine type.\n"),
            "signed PWB-REQ-014 line edited or removed",
        ),
        "non-citability dropped": (
            SPEC, replace_once(spec, "every anchor resolves stays `presentation-artifact` and `non-citable`;", "every anchor resolves becomes citable;"),
            phrase + "'A block whose every anchor resolves",
        ),
        "citable-by-count allowed": (
            SPEC, replace_once(spec, "no field derived from the pair SHALL make a narrative unit citable", "a field derived from the pair may make a narrative unit citable"),
            phrase + "'no field derived from the pair",
        ),
        "authority sentence dropped": (
            SPEC, replace_once(spec, "The pair counts resolution and never confers authority.", ""),
            phrase + "'The pair counts resolution",
        ),
        "pair fed to evidence": (
            SPEC, replace_once(spec, "The pair is itself presentation: no evidence, snapshot input or status claim SHALL take it as input.", ""),
            phrase + "'The pair is itself presentation",
        ),
        "permissive citation inserted": (
            SPEC, replace_once(spec, "  - The pair is a machine-narrative field,", "  - A block at its full count is citable evidence.\n  - The pair is a machine-narrative field,"),
            "PWB-REQ-014 carries 10 matches of token 'citable', expected 9",
        ),
        "permissive modal inserted": (
            SPEC, replace_once(spec, "  - The pair is a machine-narrative field,", "  - A block at its full count MAY be cited as evidence.\n  - The pair is a machine-narrative field,"),
            "PWB-REQ-014 carries 1 matches of token '\\\\bMAY\\\\b', expected 0",
        ),
        "estimation allowed": (
            SPEC, replace_once(spec, "Both numbers are counted, never estimated,", "Both numbers may be estimated,"),
            phrase + "\"Both numbers are counted",
        ),
        "rounding allowed": (
            SPEC, replace_once(spec, "never rounded up, omitted or rendered as a pass.", "rounded to the nearest pass."),
            phrase + "'A count below its total",
        ),
        "Unknown arm dropped": (
            SPEC, replace_once(spec, "When the machine answer at that evaluation serves no record with an identity of its own, every pair is Unknown with its reason, never a count.", ""),
            phrase + "'When the machine answer at that evaluation",
        ),
        "resolution loosened": (
            SPEC, replace_once(spec, "serves exactly one record with an `identity` field of its own", "serves a record with an `identity` field of its own"),
            phrase + "'An anchor resolves when",
        ),
        "references admitted": (
            SPEC, replace_once(spec, "is a reference and not a record's own identity, and an identity composed from other fields counts for nothing.", "counts as the record's identity."),
            phrase + "\"A field that refers to another record",
        ),
        "identity-less target resolves": (
            SPEC, replace_once(spec, "or serves without an identity of its own, does not resolve.", "does not resolve."),
            phrase + "'An anchor whose target",
        ),
        "envelope pair dropped": (
            SPEC, replace_once(spec, "and the narrative's pair is the sum of its blocks' pairs.", "."),
            phrase + "\"Both numbers are counted",
        ),
        "shape field dropped": (
            SPEC, replace_once(spec, "its target class and target identity; its revision; the claims", "its target class and target identity; the claims"),
            phrase + "\"its own identity, which begins",
        ),
        "anchor-to-block link loosened": (
            SPEC, replace_once(spec, "its own identity, which begins with the identity of the one block it belongs to followed by `#`;", "its own identity;"),
            phrase + "\"its own identity, which begins",
        ),
        "independent resolver dropped": (
            SPEC, replace_once(spec, "An independent resolver that reads only the machine narrative's anchors", "The narrative builder, reading the machine narrative's anchors"),
            phrase + "\"An independent resolver",
        ),
        "withholding limb dropped": (
            SPEC, replace_once(spec, "Resolve every anchor of the machine narrative against the machine answer at the same evaluation, then withhold one resolved target's identity from the machine answer and resolve again, and withhold every identity and resolve once more.", ""),
            phrase + "\"then withhold",
        ),
        "falsifier limb dropped": (
            SPEC, replace_once(spec, "an anchor missing a field of the one shape or naming no block or another block;", ""),
            phrase + "'an anchor missing a field",
        ),
        "signed non-citable bullet dropped": (
            SPEC, replace_once(spec, "- Every owner-visible narrative unit SHALL carry `presentation-artifact` and `non-citable` attributes", "- Every owner-visible narrative unit SHALL carry `presentation-artifact` attributes"),
            "signed PWB-REQ-014 line edited or removed",
        ),
        "new scenario dropped": (
            SPEC, replace_once(spec, "#### Scenario: Anchor resolution is counted, never made authority", "#### Scenario: Anchor resolution is counted"),
            "PWB-REQ-014 scenario population differs",
        ),
        "warrant moved": (
            SPEC, replace_once(spec, "  contracts: [RFC7-1, RFC7-2, RFC7-3, RFC7-5,", "  contracts: [RFC7-1, RFC7-2, RFC7-5,"),
            "PWB-REQ-014 warrants changed",
        ),
        "dependency drift": (
            GOVERNING, replace_once(proposed[GOVERNING], "17 requirement(s)", "18 requirement(s)"),
            "proposed GOVERNING-DEPENDENCIES differs from regeneration",
        ),
    }
    return run_selftest(pkg, mutants, ("\n   and coordinates SHALL never serve as anchor identity.", "\n   and coordinates MAY serve as anchor identity."))


if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, selftest, sys.argv[1:]))
