#!/usr/bin/env python3
"""Build and verify the inert PWB item-depth amendment candidate.

The current eleven-artifact PWB behavior package is act-bound. ``--check``
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
    ".syzygy/governance/contracts/candidates/pwb-item-depth-amendment"
)
PROPOSED = CANDIDATE / "proposed"
MANIFEST = CANDIDATE / "PWB-ITEM-DEPTH-AMENDMENT-MANIFEST.txt"
MANIFEST_OUT = MANIFEST
TITLE = "PWB ITEM-DEPTH BEHAVIOR AMENDMENT MANIFEST"
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
    CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
    CONTRACT_COVERAGE,
    GOVERNING,
    CHANGE / "design.md",
    SPEC,
}
#: Subjects whose proposed bytes are generated from the others, never authored.
DERIVED = frozenset({GOVERNING, CONTRACT_COVERAGE})
#: Sibling packages the owner declined and never applied; their patches no
#: longer apply and compose with nothing (POLARIS-LANE-B-DECLINED-AND-TARGET-
#: REVISED-DIRECTION.md). Closed list: any other sibling must classify.
DECLINED_SIBLINGS = frozenset({"pwb-scoped-attributes-amendment"})
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


def regenerate_coverage_patch() -> str:
    semantic = [p for p in patch_files() if patch_target(p) not in DERIVED]
    proposed = proposed_bytes(patches=semantic)
    return unified_patch(
        CONTRACT_COVERAGE, read_subjects()[CONTRACT_COVERAGE], generated_coverage(proposed)
    )


def render_manifest(proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        f"# {TITLE}\n"
        "# These rows bind only by an owner act naming this file's digest in\n"
        "# ACCEPTANCE-ACT-RECORD.md; until that act they bind nothing.\n"
        "# 11 artifacts; rows sorted by codepoint path.\n"
        "# All rows take effect together or none do.\n"
        "# Rows hash PROPOSED bytes; signed openspec bytes remain unchanged.\n"
    )
    rows = "".join(
        f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in BEHAVIOR_SUBJECTS
    )
    return header + rows


def semantic_findings(
    proposed: dict[pathlib.Path, bytes], current_spec: bytes | None = None
) -> list[str]:
    spec = proposed[SPEC].decode("utf-8")
    findings: list[str] = []
    required_once = (
        "### Requirement: PWB-REQ-015 — Item detail preserves authority bands and exact intent",
        "Every item in the complete declared `catalog-entry` population",
        "in order, an `argument` band marked",
        "Each contract band SHALL carry an item-to-intent relation claim",
        "fixed relation role `governing-intent`",
        "SHALL NOT change or borrow the item's",
        "`governing-intent-relation`",
        "admit no such declaration, so this requirement mints none",
        "Two captured governing relations exclude one another only when an admitted declaration names them as mutually exclusive",
        "class, label, basename, similarity, generated prose and a PWB-REQ-004 precedence outcome never create or resolve an exclusion",
        "a requirement and a non-goal never exclude one another by class",
        "each item's population of captured relations has exactly one result",
        "With one or more, no two of which exclude one another, it is Observed over that whole set",
        "compatible relations never become separate claims or a conflict",
        "With any two that exclude one another, it is Unknown over the whole population with `contradicted-pending-adjudication`",
        "however many compatible relations the population also holds",
        "RFC2-24 reason `missing-declaration` and its resolution route",
        "`contradicted-pending-adjudication` and the owner-adjudication route",
        "SHALL NOT infer a relation from a label,",
        "tuple SHALL be recoverable in both channels under PWB-REQ-020",
        "A declared capability matches a catalog item only when the capability's own declared key equals that item's declared key",
        "A capability matching no item, or more than one, receives no item detail",
        "through PWB-REQ-011's exact-source route, which is the only place that text is encoded",
        "this never changes the relation claim below",
        "Only an item detail for a matching declared capability may render",
        "A non-capability item detail SHALL render no",
        "and a `reality` band sourced only from the shared model",
        "catalog-to-detail-to-exact-source path SHALL preserve the item's stable",
        "#### Scenario: Catalog item reaches exact current intent or honest absence",
    )
    flat = " ".join(spec.split())
    for fragment in required_once:
        count = flat.count(" ".join(fragment.split()))
        if count != 1:
            findings.append(f"proposed spec expected one {fragment!r}, found {count}")
    forbidden = (
        "### Requirement: PWB-REQ-015 — Capability detail preserves authority bands",
        "one honest absence carrying the item's Unknown reason",
        "Every item detail may render active or proposed OpenSpec work",
    )
    for fragment in forbidden:
        if fragment in spec:
            findings.append(f"proposed spec retains superseded fragment: {fragment!r}")
    current = (read_subjects()[SPEC] if current_spec is None else current_spec).decode("utf-8")
    if "### Requirement: PWB-REQ-015 — Capability detail preserves authority bands and exact intent" not in current:
        findings.append("signed PWB-REQ-015 bytes moved in place")
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


def sibling_population(
    siblings: list[pathlib.Path] | None = None, current: bytes | None = None
) -> dict[str, list[pathlib.Path]]:
    siblings = sibling_spec_patches() if siblings is None else siblings
    out: dict[str, list[pathlib.Path]] = {
        "pending": [], "applied": [], "declined": [], "unclassified": []}
    for sibling in siblings:
        if sibling.parent.parent.name in DECLINED_SIBLINGS:
            out["declined"].append(sibling)
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
) -> list[str]:
    mine = ROOT / PROPOSED / "spec.md.patch" if mine is None else mine
    current = read_subjects()[SPEC] if current is None else current
    population = sibling_population(siblings, current)
    findings = [
        f"sibling spec patch is neither pending nor applied: {display(path)}"
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


def check(patches: list[pathlib.Path] | None = None) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    findings: list[str] = []
    patches = patch_files() if patches is None else patches
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != PATCHED or len(targets) != len(PATCHED):
        findings.append(
            "patch targets differ from the closed six-subject population: "
            + ", ".join(path.as_posix() for path in targets)
        )
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    findings.extend(semantic_findings(proposed))
    findings.extend(generated_findings(proposed))
    findings.extend(coverage_findings(proposed))
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

    semantic_mutants = {
        "missing item population": ("Every item in the complete declared `catalog-entry` population", "Every item in the declared item population"),
        "guessed relation": ("SHALL NOT infer a relation", "MAY infer a relation"),
        "unstable relation identity": ("fixed relation role `governing-intent`", "route-selected relation role"),
        "borrowed item tuple": ("SHALL NOT change or borrow the item's", "MAY borrow the item's"),
        "single-relation collapse": ("With one or more, no two of which exclude one another, it is Observed over that whole set", "With exactly one, it is Observed over that relation"),
        "compatible set split": ("compatible relations never become separate claims or a conflict", "compatible relations become separate claims"),
        "invalid relation reason": ("RFC2-24 reason `missing-declaration` and its resolution route", "reason `mapping-ambiguous` and its resolution route"),
        "non-capability proposal": ("A non-capability item detail SHALL render no", "A non-capability item detail MAY render"),
        "reordered bands": ("in order, an `argument` band marked", "in order, a `reality` band marked"),
        "second reality model": ("and a `reality` band sourced only from the shared model", "and a `reality` band sourced from a surface model"),
        "mixed population observed": ("With any two that exclude one another, it is Unknown over the whole population with `contradicted-pending-adjudication`", "With any two that exclude one another, it is Observed over the compatible subset with `contradicted-pending-adjudication`"),
        "mixed population loses its compatible members": ("however many compatible relations the population also holds", "when no compatible relation is also held"),
        "exclusion inferred from class": ("a requirement and a non-goal never exclude one another by class", "a requirement and a non-goal exclude one another by class"),
        "precedence resolves exclusion": ("a PWB-REQ-004 precedence outcome never create or resolve an exclusion", "a PWB-REQ-004 precedence outcome resolves an exclusion"),
        "exclusion undeclared": ("exclude one another only when an admitted declaration names them as mutually exclusive", "exclude one another when a label or similarity suggests it"),
        "relation source assumed admitted": ("admit no such declaration, so this requirement mints none", "admit such a declaration, so this requirement mints it"),
        "relation currency class unnamed": ("`governing-intent-relation`", "`item-fact`"),
        "population without a single result": ("each item's population of captured relations has exactly one result", "each item's population of captured relations has a result"),
        "capability matched by label": ("equals that item's declared key, compared exactly and without normalization", "resembles that item's label"),
        "capability with several matches keeps a detail": ("A capability matching no item, or more than one, receives no item detail", "A capability matching more than one item receives each item detail"),
        "body encoded outside the exact-source route": ("which is the only place that text is encoded", "which is one place that text is encoded"),
        "withheld source changes the relation": ("this never changes the relation claim below", "this makes the relation claim Unknown"),
    }
    def fuzzy(body: bytes, old: str, new: str) -> bytes:
        pattern = r"\s+".join(re.escape(word) for word in old.split())
        replaced, count = re.subn(pattern, lambda _m: new, body.decode("utf-8"), count=1)
        assert count == 1, f"selftest mutant target absent: {old!r}"
        return replaced.encode()

    for name, (old, new) in semantic_mutants.items():
        mutated = dict(proposed)
        mutated[SPEC] = fuzzy(mutated[SPEC], old, new)
        cases.append((name, bool(semantic_findings(mutated))))

    stale = render_manifest(proposed).replace(sha256(proposed[SPEC]), "0" * 64, 1)
    cases.append(("stale manifest", bool(manifest_findings(proposed, stale))))

    wrong_generated = dict(proposed)
    wrong_generated[GOVERNING] = proposed[GOVERNING].replace(
        sha256(proposed[SPEC]).encode(), b"0" * 64, 1
    )
    cases.append(("wrong generated digest", bool(generated_findings(wrong_generated))))

    stale_coverage = dict(proposed)
    stale_coverage[CONTRACT_COVERAGE] = read_subjects()[CONTRACT_COVERAGE]
    cases.append(("stale derived contract-coverage summary", bool(coverage_findings(stale_coverage))))

    semicolon = dict(proposed)
    repair = CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md"
    assert b"covered:PWB-REQ-013,PWB-REQ-015" in semicolon[repair]
    semicolon[repair] = semicolon[repair].replace(
        b"covered:PWB-REQ-013,PWB-REQ-015", b"covered:PWB-REQ-013;PWB-REQ-015", 1)
    cases.append(("semicolon coverage separator", bool(coverage_findings(semicolon))))

    unknown_requirement = dict(proposed)
    unknown_requirement[repair] = unknown_requirement[repair].replace(
        b"covered:PWB-REQ-013,PWB-REQ-015", b"covered:PWB-REQ-013,PWB-REQ-999", 1)
    cases.append(("coverage row citing a missing requirement", bool(coverage_findings(unknown_requirement))))

    cases.append(("generated coverage equals the proposed row",
                  generated_coverage({**proposed, CONTRACT_COVERAGE: read_subjects()[CONTRACT_COVERAGE]})
                  == proposed[CONTRACT_COVERAGE]))

    duplicate = dict(proposed)
    duplicate[SPEC] = proposed[SPEC] + (
        b"\n### Requirement: PWB-REQ-015 \xe2\x80\x94 Item detail preserves authority bands and exact intent\n"
    )
    cases.append(("duplicate replacement", bool(semantic_findings(duplicate))))

    moved_signed = read_subjects()[SPEC].replace(
        b"### Requirement: PWB-REQ-015 \xe2\x80\x94 Capability detail preserves authority bands and exact intent",
        b"### Requirement: PWB-REQ-015 \xe2\x80\x94 Item detail preserves authority bands and exact intent",
        1,
    )
    cases.append(("signed-byte drift", bool(semantic_findings(proposed, moved_signed))))

    with tempfile.TemporaryDirectory() as temp:
        temp_root = pathlib.Path(temp)
        broken = temp_root / "spec.md.patch"
        broken.write_text("not a patch\n", encoding="utf-8")
        broken_findings, _ = check([broken])
        cases.append(("corrupt patch", bool(broken_findings)))

        def make_mirror(name: str) -> pathlib.Path:
            mirror = temp_root / name
            script_rel = pathlib.Path("scripts/build_pwb_item_depth_amendment.py")
            dependency_rels = (
                pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
                pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
            )
            for rel in (script_rel, COVERAGE_SCRIPT, CONTRACT_INDEX, *dependency_rels):
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
            for sibling in sibling_spec_patches():
                rel = sibling.relative_to(ROOT)
                target = mirror / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(sibling.read_bytes())
            return mirror

        def run_cli(mirror: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
            return subprocess.run(
                [sys.executable, str(mirror / "scripts/build_pwb_item_depth_amendment.py"), *args],
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
        stale = run_cli(mirror, "--apply", "--at-adoption")
        cases.append((
            "apply at adoption with a stale manifest writes no signed subject",
            stale.returncode == 1 and targets(mirror) == before,
        ))

        mirror = make_mirror("apply-ok")
        before = targets(mirror)
        applied = run_cli(mirror, "--apply", "--at-adoption")
        after = targets(mirror)
        cases.append((
            "apply at adoption writes exactly the six proposed subjects",
            applied.returncode == 0
            and all(after[rel] == proposed[rel] for rel in BEHAVIOR_SUBJECTS)
            and {rel for rel in BEHAVIOR_SUBJECTS if after[rel] != before[rel]} == PATCHED,
        ))

        # Sibling classification and composition over synthetic patches.
        current = read_subjects()[SPEC]
        text = current.decode("utf-8")

        def synthetic(name: str, old: str, new: str, state: str = "pending") -> pathlib.Path:
            assert text.count(old) == 1, old
            moved = text.replace(old, new, 1).encode()
            body = unified_patch(SPEC, current, moved) if state == "pending" else unified_patch(SPEC, moved, current)
            path = temp_root / name / "proposed" / "spec.md.patch"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
            return path

        far = "### Requirement: PWB-REQ-012 \u2014 Owner-facing copy is direct and concise"
        pending_far = synthetic("pending-far", far, far + " (x)")
        applied_far = synthetic("applied-far", far, far + " (x)", "applied")
        near = "### Requirement: PWB-REQ-015 \u2014 Capability detail preserves authority bands and exact intent"
        pending_near = synthetic("pending-near", near, near + " (x)")
        stray = temp_root / "stray" / "proposed" / "spec.md.patch"
        stray.parent.mkdir(parents=True)
        stray.write_text(
            unified_patch(SPEC, b"a line the spec lacks\n", b"another line\n"), encoding="utf-8")
        declined = temp_root / "pwb-scoped-attributes-amendment" / "proposed" / "spec.md.patch"
        declined.parent.mkdir(parents=True)
        declined.write_bytes(stray.read_bytes())
        def handmade(name: str, hunks: list[tuple[str, str]]) -> pathlib.Path:
            path = temp_root / name / "proposed" / "spec.md.patch"
            path.parent.mkdir(parents=True, exist_ok=True)
            body = f"--- a/{SPEC.as_posix()}\n+++ b/{SPEC.as_posix()}\n"
            for old, new in hunks:
                body += f"@@ -1 +1 @@\n-{old}\n+{new}\n"
            path.write_text(body, encoding="utf-8")
            return path

        both_present = handmade("both-present", [(
            "### Requirement: PWB-REQ-012 \u2014 Owner-facing copy is direct and concise",
            "### Requirement: PWB-REQ-013 \u2014 Proposed work stays subordinate to current project truth")])
        mixed = handmade("mixed", [
            ("### Requirement: PWB-REQ-012 \u2014 Owner-facing copy is direct and concise",
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
                               ("near", pending_near), ("stray", stray))
        }
        cases.append(("a disjoint unapplied sibling classifies pending", states["far"] == "pending"))
        cases.append(("an already-applied sibling classifies applied", states["applied"] == "applied"))
        cases.append(("a sibling whose text is absent classifies unclassified", states["stray"] == "unclassified"))
        cases.append(("a disjoint pending sibling composes in both orders",
                      composition_findings(siblings=[pending_far]) == []))
        cases.append(("an overlapping pending sibling is reported",
                      bool(composition_findings(siblings=[pending_near]))))
        cases.append(("an unclassified sibling is reported",
                      bool(composition_findings(siblings=[stray]))))
        cases.append(("an applied sibling is not composed",
                      composition_findings(siblings=[applied_far]) == []))
        cases.append(("a declined sibling is skipped by its closed name",
                      composition_findings(siblings=[declined]) == []))
    population = sibling_population()
    cases.append(("every real sibling spec patch classifies", not population["unclassified"]))
    cases.append(("the real sibling population is the whole tracked set",
                  sum(len(group) for group in population.values()) == len(sibling_spec_patches())))
    first = proposed_bytes()
    second = proposed_bytes()
    cases.append(("deterministic regeneration", first == second and render_manifest(first) == render_manifest(second)))
    partial_findings, _ = check([p for p in patch_files() if patch_target(p) != GOVERNING])
    cases.append(("partial landing", bool(partial_findings)))
    coverage_partial, _ = check([p for p in patch_files() if patch_target(p) != CONTRACT_COVERAGE])
    cases.append(("a landing without the contract-coverage subject", bool(coverage_partial)))

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
    coverage_patch = regenerate_coverage_patch()
    (ROOT / PROPOSED / "CONTRACT-COVERAGE.md.patch").write_text(coverage_patch, encoding="utf-8")
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
        print("ITEM-DEPTH CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    population = sibling_population()
    print(
        f"item-depth candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects; "
        f"{len(population['pending'])} pending sibling spec patches compose "
        f"({len(population['applied'])} applied, {len(population['declined'])} "
        "declined, none unclassified)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
