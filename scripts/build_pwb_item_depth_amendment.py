#!/usr/bin/env python3
"""Build and verify the inert PWB item-depth amendment candidate.

The current eleven-artifact PWB behavior package is act-bound. This builder
therefore applies the candidate's ``proposed/*.patch`` files only in a scratch
tree and hashes those proposed bytes. It has no signed-subject write mode: only
a future independently reviewed owner-act recorder may validate an effective
act, chain position and exact manifest before writing ``openspec/**``. A
candidate commit, review, manifest or merge performs no owner act.
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
TITLE = "PWB ITEM-DEPTH BEHAVIOR AMENDMENT MANIFEST"
SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"

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
    GOVERNING,
    CHANGE / "design.md",
    SPEC,
}
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
    semantic = [p for p in patch_files() if patch_target(p) != GOVERNING]
    proposed = proposed_bytes(patches=semantic)
    generated, errors = dependencies.generate(proposed[SPEC].decode("utf-8"))
    if errors or generated is None:
        raise ValueError("proposed spec warrants do not validate: " + " | ".join(errors))
    return unified_patch(GOVERNING, read_subjects()[GOVERNING], generated.encode())


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
        "RFC2-24 reason `missing-declaration`",
        "`contradicted-pending-adjudication` and the owner-adjudication route",
        "SHALL NOT infer a relation from a label, basename, similarity or generated",
        "relation claim's complete PWB-REQ-007 tuple",
        "Only an item detail for a matching declared capability may render",
        "A non-capability item detail SHALL render no",
        "and a `reality` band sourced only from the\n"
        "shared model",
        "catalog-to-detail-to-exact-source path SHALL preserve the item's stable",
        "#### Scenario: Catalog item reaches exact current intent or honest absence",
    )
    for fragment in required_once:
        count = spec.count(fragment)
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


def active_sibling_spec_patches() -> list[pathlib.Path]:
    root = ROOT / ".syzygy/governance/contracts/candidates"
    siblings: list[pathlib.Path] = []
    for patch in sorted(root.glob("*/proposed/spec.md.patch")):
        if CANDIDATE.as_posix() in patch.relative_to(ROOT).as_posix():
            continue
        text = patch.read_text(encoding="utf-8")
        if f"+++ b/{SPEC.as_posix()}" in text:
            siblings.append(patch)
    return siblings


def composition_findings(
    mine: pathlib.Path | None = None,
    siblings: list[pathlib.Path] | None = None,
) -> list[str]:
    mine = ROOT / PROPOSED / "spec.md.patch" if mine is None else mine
    siblings = active_sibling_spec_patches() if siblings is None else siblings
    findings: list[str] = []
    current = read_subjects()[SPEC]
    for sibling in siblings:
        try:
            first = apply_patches({**read_subjects(), SPEC: current}, [sibling, mine])[SPEC]
            second = apply_patches({**read_subjects(), SPEC: current}, [mine, sibling])[SPEC]
        except ValueError as error:
            findings.append(f"sibling composition failed for {sibling.relative_to(ROOT)}: {error}")
            continue
        if first != second:
            findings.append(f"sibling composition is order-dependent: {sibling.relative_to(ROOT)}")
    if not siblings:
        findings.append("no active sibling PWB spec patches found; composition denominator is empty")
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
            "patch targets differ from the closed five-subject population: "
            + ", ".join(path.as_posix() for path in targets)
        )
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    findings.extend(semantic_findings(proposed))
    findings.extend(generated_findings(proposed))
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
        "invalid relation reason": ("RFC2-24 reason `missing-declaration`", "reason `mapping-ambiguous`"),
        "non-capability proposal": ("A non-capability item detail SHALL render no", "A non-capability item detail MAY render"),
        "reordered bands": ("in order, an `argument` band marked", "in order, a `reality` band marked"),
        "second reality model": ("and a `reality` band sourced only from the\nshared model", "and a `reality` band sourced from a surface model"),
    }
    for name, (old, new) in semantic_mutants.items():
        mutated = dict(proposed)
        body = mutated[SPEC].replace(old.encode(), new.encode(), 1)
        mutated[SPEC] = body
        cases.append((name, bool(semantic_findings(mutated))))

    stale = render_manifest(proposed).replace(sha256(proposed[SPEC]), "0" * 64, 1)
    cases.append(("stale manifest", bool(manifest_findings(proposed, stale))))

    wrong_generated = dict(proposed)
    wrong_generated[GOVERNING] = proposed[GOVERNING].replace(
        sha256(proposed[SPEC]).encode(), b"0" * 64, 1
    )
    cases.append(("wrong generated digest", bool(generated_findings(wrong_generated))))

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

        mirror = temp_root / "cli-mirror"
        script_rel = pathlib.Path("scripts/build_pwb_item_depth_amendment.py")
        dependency_rels = (
            pathlib.Path("scripts/build_polaris_project_wide_spec_dependencies.py"),
            pathlib.Path("scripts/build_capability_1_spec_dependencies.py"),
        )
        for rel in (script_rel, *dependency_rels):
            target = mirror / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)
        for rel in BEHAVIOR_SUBJECTS:
            target = mirror / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / rel).read_bytes())
        shutil.copytree(ROOT / CANDIDATE, mirror / CANDIDATE)
        for sibling in active_sibling_spec_patches():
            rel = sibling.relative_to(ROOT)
            target = mirror / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(sibling.read_bytes())
        before: dict[pathlib.Path, bytes] = {}
        for rel in PATCHED:
            target = mirror / rel
            before[rel] = target.read_bytes()
        refused = subprocess.run(
            [sys.executable, str(mirror / script_rel), "--apply", "--at-adoption"],
            cwd=mirror,
            capture_output=True,
        )
        after = {rel: (mirror / rel).read_bytes() for rel in PATCHED}
        if refused.returncode != 2 or b"unrecognized arguments" not in refused.stderr:
            print(
                "  (standalone CLI refusal mismatch: "
                f"rc={refused.returncode}, stderr={refused.stderr.decode().strip()!r})"
            )
        cases.append((
            "standalone adoption CLI is absent and writes no signed subject",
            refused.returncode == 2
            and b"unrecognized arguments" in refused.stderr
            and after == before,
        ))

    siblings = active_sibling_spec_patches()
    cases.append(("missing sibling denominator", bool(composition_findings(siblings=[]))))
    cases.append(("sibling population present", len(siblings) > 0))
    first = proposed_bytes()
    second = proposed_bytes()
    cases.append(("deterministic regeneration", first == second and render_manifest(first) == render_manifest(second)))
    partial_findings, _ = check([p for p in patch_files() if patch_target(p) != GOVERNING])
    cases.append(("partial landing", bool(partial_findings)))

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


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()
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
    print(
        f"item-depth candidate matches {len(BEHAVIOR_SUBJECTS)} proposed subjects; "
        f"{len(active_sibling_spec_patches())} sibling spec patches compose"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
