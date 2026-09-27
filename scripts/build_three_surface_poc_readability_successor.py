#!/usr/bin/env python3
"""Build and verify the inert Three-Surface POC readability successor.

The six signed predecessor artifacts remain unchanged while this is a
candidate. Proposed bytes live as patches under the candidate package. This
builder has no signed-byte write path: only a later independently reviewed
owner-act recorder may implement the atomic successor transaction.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_three_surface_poc_spec_dependencies as dependencies  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/three-surface-poc-experience")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "three-surface-poc-readability-successor"
)
PROPOSED = CANDIDATE / "proposed"
MANIFEST = CANDIDATE / "THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt"
SEMANTIC_MAP = CANDIDATE / "SEMANTIC-MAP.json"
SPEC = CHANGE / "specs/three-surface-poc-experience/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"

SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "CONTRACT-COVERAGE.md",
            GOVERNING,
            CHANGE / "design.md",
            CHANGE / "proposal.md",
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
PATCHED = {GOVERNING, CHANGE / "design.md", CHANGE / "proposal.md", SPEC}
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
TARGET_RE = re.compile(r"^\+\+\+ b/(.+)$", re.MULTILINE)
REQ_RE = re.compile(r"^### Requirement: (POC-REQ-\d{3}) — ([^\n]+)$", re.MULTILINE)
SCENARIO_RE = re.compile(r"^#### Scenario: ([^\n]+)$", re.MULTILINE)
BLOCK_RE = re.compile(
    r"(^### Requirement: (POC-REQ-\d{3}) — [^\n]+\n)([\s\S]*?)"
    r"(?=^### Requirement: |\Z)",
    re.MULTILINE,
)
BODY_RE = re.compile(
    r"^Group: [^\n]+\n\n([\s\S]*?)(?=\n- \*\*Case)", re.MULTILINE
)
WARRANT_RE = re.compile(r"```yaml\n(warrants:[\s\S]*?)\n```", re.MULTILINE)
GROUP_RE = re.compile(r"^Group: ([^\n]+)$", re.MULTILINE)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def current_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in SUBJECTS:
        if rel in overrides:
            values[rel] = overrides[rel]
            continue
        target = ROOT / rel
        if not target.is_file():
            raise ValueError(f"missing signed subject: {rel}")
        values[rel] = target.read_bytes()
    return values


def patch_files() -> list[pathlib.Path]:
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda path: path.name)


def patch_target(patch: pathlib.Path) -> pathlib.Path:
    match = TARGET_RE.search(patch.read_text(encoding="utf-8"))
    if match is None:
        raise ValueError(f"patch has no target: {patch.relative_to(ROOT)}")
    return pathlib.Path(match.group(1))


def apply_patch(base: pathlib.Path, patch: pathlib.Path) -> tuple[int, str]:
    done = subprocess.run(
        ["git", "apply", "--whitespace=nowarn", str(patch)],
        cwd=base,
        capture_output=True,
        text=True,
    )
    return done.returncode, done.stderr.strip()


def proposed_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
    patches: list[pathlib.Path] | None = None,
) -> dict[pathlib.Path, bytes]:
    values = current_bytes(overrides)
    patches = patch_files() if patches is None else patches
    with tempfile.TemporaryDirectory() as directory:
        base = pathlib.Path(directory)
        for rel, body in values.items():
            target = base / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        for patch in patches:
            code, error = apply_patch(base, patch)
            if code != 0:
                raise ValueError(f"{patch.name} does not apply: {error}")
        return {rel: (base / rel).read_bytes() for rel in SUBJECTS}


def unified_patch(rel: pathlib.Path, before: bytes, after: bytes) -> str:
    rendered = "".join(
        difflib.unified_diff(
            before.decode().splitlines(keepends=True),
            after.decode().splitlines(keepends=True),
            fromfile=f"a/{rel.as_posix()}",
            tofile=f"b/{rel.as_posix()}",
            n=2,
        )
    )
    return rendered.replace("\n \n", "\n\n")


def regenerated_governing_patch() -> str:
    semantic = [patch for patch in patch_files() if patch_target(patch) != GOVERNING]
    proposed = proposed_bytes(patches=semantic)
    rendered, errors = dependencies.generate(proposed[SPEC].decode())
    if errors or rendered is None:
        raise ValueError("proposed warrants do not validate: " + " | ".join(errors))
    return unified_patch(GOVERNING, current_bytes()[GOVERNING], rendered.encode())


def render_manifest(proposed: dict[pathlib.Path, bytes]) -> str:
    header = (
        "# THREE-SURFACE POC READABILITY SUCCESSOR MANIFEST\n"
        "# Candidate: binds nothing without a later owner successor act.\n"
        "# Six signed artifacts; rows sorted by codepoint path.\n"
        "# Rows hash proposed bytes; predecessor bytes remain unchanged.\n"
    )
    return header + "".join(
        f"{sha256(proposed[rel])}  {rel.as_posix()}\n" for rel in SUBJECTS
    )


def requirement_blocks(text: str) -> dict[str, str]:
    return {match.group(2): match.group(0) for match in BLOCK_RE.finditer(text)}


def normalized_body(block: str, *, proposed: bool) -> str:
    match = BODY_RE.search(block)
    if match is None:
        raise ValueError("requirement has no normative body before Case")
    body = match.group(1)
    if proposed:
        body = body.replace("**Required behavior.** ", "", 1)
        body = body.replace("- **Scope.** ", "Scope of quantification: ", 1)
    return " ".join(
        line.strip() for line in body.splitlines() if line.strip()
    ).strip()


def semantic_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    current = current_bytes()[SPEC].decode()
    successor = proposed[SPEC].decode()
    findings: list[str] = []
    current_ids = REQ_RE.findall(current)
    proposed_ids = REQ_RE.findall(successor)
    if current_ids != proposed_ids or len(current_ids) != 24:
        findings.append("requirement identity/title/order differs from the 24-item predecessor")
    if SCENARIO_RE.findall(current) != SCENARIO_RE.findall(successor):
        findings.append("scenario heading population or order changed")
    old_blocks = requirement_blocks(current)
    new_blocks = requirement_blocks(successor)
    for requirement_id in [item[0] for item in current_ids]:
        old = old_blocks.get(requirement_id)
        new = new_blocks.get(requirement_id)
        if old is None or new is None:
            findings.append(f"missing requirement block: {requirement_id}")
            continue
        if normalized_body(old, proposed=False) != normalized_body(new, proposed=True):
            findings.append(f"normative body words changed: {requirement_id}")
        if GROUP_RE.findall(old) != GROUP_RE.findall(new):
            findings.append(f"group/form changed: {requirement_id}")
        old_tail = old.split("\n- **Case", 1)
        new_tail = new.split("\n- **Case", 1)
        if len(old_tail) != 2 or len(new_tail) != 2 or old_tail[1] != new_tail[1]:
            findings.append(f"case/oracle/scenario content changed: {requirement_id}")
        if WARRANT_RE.findall(old) != WARRANT_RE.findall(new):
            findings.append(f"warrants changed: {requirement_id}")
    if successor.count("**Required behavior.**") != 24:
        findings.append("successor does not carry one answer-first marker per requirement")
    expected_scopes = sum(
        normalized_body(block, proposed=False).count("Scope of quantification:")
        for block in old_blocks.values()
    )
    if successor.count("- **Scope.**") != expected_scopes:
        findings.append("scope-marker population differs from predecessor scope sentences")
    if proposed[CHANGE / ".openspec.yaml"] != current_bytes()[CHANGE / ".openspec.yaml"]:
        findings.append("hidden .openspec.yaml changed")
    if proposed[CHANGE / "CONTRACT-COVERAGE.md"] != current_bytes()[CHANGE / "CONTRACT-COVERAGE.md"]:
        findings.append("contract coverage changed without a mapped semantic movement")
    return findings


def generated_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    rendered, errors = dependencies.generate(proposed[SPEC].decode())
    if errors or rendered is None:
        return ["proposed dependency generation failed: " + " | ".join(errors)]
    return [] if proposed[GOVERNING].decode() == rendered else [
        "proposed GOVERNING-DEPENDENCIES differs from regeneration"
    ]


def manifest_findings(proposed: dict[pathlib.Path, bytes], actual: str) -> list[str]:
    findings: list[str] = []
    if actual != render_manifest(proposed):
        findings.append("manifest differs from proposed-byte regeneration")
    rows = ROW_RE.findall(actual)
    if len(rows) != 6 or [path for _digest, path in rows] != [
        rel.as_posix() for rel in SUBJECTS
    ]:
        findings.append("manifest path population/order is not the signed six")
    return findings


def semantic_map_findings(value: object | None = None) -> list[str]:
    findings: list[str] = []
    if value is None:
        try:
            value = json.loads((ROOT / SEMANTIC_MAP).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            return [f"semantic map is missing or invalid: {error}"]
    if not isinstance(value, dict):
        return ["semantic map is not an object"]
    rows = value.get("requirements")
    expected = [item[0] for item in REQ_RE.findall(current_bytes()[SPEC].decode())]
    if not isinstance(rows, list):
        findings.append("semantic map has no requirement rows")
    else:
        actual = [row.get("id") for row in rows if isinstance(row, dict)]
        if actual != expected or len(actual) != len(rows):
            findings.append("semantic map does not cover the ordered 24-ID population")
        if any(row.get("classification") != "meaning-preserved"
               for row in rows if isinstance(row, dict)):
            findings.append("semantic map carries a non-preserved requirement classification")
    if value.get("semantic_changes") != []:
        findings.append("semantic map carries an undisclosed semantic-change population")
    if value.get("baseline") != "3c915991fbb0eebc38f8daaaea4d05679914b6b8":
        findings.append("semantic map baseline is not the dispatched exact head")
    return findings


def check(
    patches: list[pathlib.Path] | None = None,
) -> tuple[list[str], dict[pathlib.Path, bytes] | None]:
    patches = patch_files() if patches is None else patches
    findings: list[str] = []
    try:
        targets = [patch_target(patch) for patch in patches]
    except ValueError as error:
        return [str(error)], None
    if set(targets) != PATCHED or len(targets) != len(PATCHED):
        findings.append("patch targets differ from the closed four-subject population")
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)], None
    findings.extend(semantic_findings(proposed))
    findings.extend(generated_findings(proposed))
    findings.extend(semantic_map_findings())
    if not (ROOT / MANIFEST).is_file():
        findings.append(f"missing manifest: {MANIFEST}")
    else:
        findings.extend(manifest_findings(
            proposed, (ROOT / MANIFEST).read_text(encoding="utf-8")
        ))
    return findings, proposed


def selftest() -> int:
    findings, proposed = check()
    if findings or proposed is None:
        print("SELFTEST PRECONDITION FAILED:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    cases: list[tuple[str, bool]] = []
    mutations = {
        "missing answer marker": (b"**Required behavior.** ", b""),
        "changed modal": (b" SHALL ", b" MAY "),
        "duplicate requirement id": (b"POC-REQ-002", b"POC-REQ-001"),
        "changed warrant": (b"primary: VIS-2", b"primary: VIS-1"),
        "changed scenario outcome": (b"renders that item", b"hides that item"),
    }
    for name, (old, new) in mutations.items():
        mutated = dict(proposed)
        mutated[SPEC] = proposed[SPEC].replace(old, new, 1)
        cases.append((name, bool(semantic_findings(mutated))))
    wrong_generated = dict(proposed)
    wrong_generated[GOVERNING] += b"drift\n"
    cases.append(("generated dependency drift", bool(generated_findings(wrong_generated))))
    stale = render_manifest(proposed).replace(sha256(proposed[SPEC]), "0" * 64, 1)
    cases.append(("stale manifest", bool(manifest_findings(proposed, stale))))
    partial, _ = check([patch for patch in patch_files() if patch_target(patch) != GOVERNING])
    cases.append(("partial patch population", bool(partial)))
    semantic_map = json.loads((ROOT / SEMANTIC_MAP).read_text(encoding="utf-8"))
    semantic_map["requirements"] = semantic_map["requirements"][:-1]
    cases.append(("incomplete semantic map", bool(semantic_map_findings(semantic_map))))
    before = current_bytes()
    with tempfile.TemporaryDirectory() as directory:
        corrupt = pathlib.Path(directory) / "spec.md.patch"
        original = next(
            patch for patch in patch_files() if patch_target(patch) == SPEC
        ).read_text(encoding="utf-8")
        target = "Group: Cross-cutting experience. Form: **invariant**."
        if original.count(target) < 1:
            raise AssertionError("late-patch mutation target is absent")
        corrupt.write_text(
            original.replace(target, "Group: Corrupted. Form: **invariant**.", 1),
            encoding="utf-8",
        )
        late_patches = [
            corrupt if patch_target(patch) == SPEC else patch
            for patch in patch_files()
        ]
        late_findings, _ = check(late_patches)
    cases.append((
        "late patch failure leaves every signed subject byte-identical",
        bool(late_findings) and current_bytes() == before,
    ))
    cases.append(("deterministic regeneration", proposed_bytes() == proposed_bytes()))
    failed = [name for name, caught in cases if not caught]
    for name, caught in cases:
        print(f"selftest: {name}: {'caught' if caught else 'SURVIVED'}")
    if failed:
        print("SELFTEST FAILED: " + ", ".join(failed))
        return 1
    print(f"selftest: {len(cases)} candidate predicates fail closed")
    return 0


def write() -> int:
    governing = ROOT / PROPOSED / "GOVERNING-DEPENDENCIES.md.patch"
    governing.write_text(regenerated_governing_patch(), encoding="utf-8")
    proposed = proposed_bytes()
    (ROOT / MANIFEST).write_text(render_manifest(proposed), encoding="utf-8")
    print(f"wrote {governing.relative_to(ROOT)} and {MANIFEST}")
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
        print("THREE-SURFACE POC READABILITY CANDIDATE FINDINGS:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    assert proposed is not None
    print("three-surface POC readability candidate matches 6 proposed subjects "
          "(4 patched, 2 unchanged); 24 requirement bodies preserve their words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
