#!/usr/bin/env python3
"""Build and verify the inert PWB registry machine-ceiling amendment (P-114).

Package `contracts/candidates/pwb-registry-machine-ceiling-amendment/`
(`syzygy-59s5`). This script performs no owner act and writes no act record.

The subject is the Polaris Butlers project-shape observer registry entry. Its
current bytes are the argument of the performed 2026-10-02 re-pin act B
(`decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`), the act
the PWB-REQ-005 body-read gate follows today. The amendment changes one value,
`entries[0].resourceLimits.maxMachineResponseBytes`, from 8388608 (8 MiB) to
16777216 (16 MiB), and no other byte. The proposed bytes live only as one
unified diff under `proposed/`; the one-row manifest hashes the bytes that
diff produces. That row is what a superseding `adopt-registry-entry` record
would name as the entry's exact digest; the owner signs by version tag and
types no digest.

`--check` verifies the package against the subject on disk, in either state:

- unapplied: the subject carries the old literal exactly once; the proposed
  bytes are the subject with that one literal replaced; parsed as JSON the two
  differ at that one key path only;
- applied: the subject hashes to the manifest row, and replacing the new
  literal back recovers a base that verifies the same way;
- any other subject (a sibling package applied first) fails closed: the
  package must be regenerated with `--write` over the new base and reviewed
  again.

In both states the patch file and the one-row manifest equal their
regeneration, and no package Markdown file carries a 64-hex token. The patch
is also run through `git apply --check` (forward unapplied, reverse applied).
That step is defence in depth: while the patch equals its regeneration it
cannot fail, so no selftest mutant isolates it.

The check also holds the code to the entry, because the daemon hard-codes
the ceiling rather than reading it. It parses the `PWB_RESOURCE_LIMITS`
object (comments removed) and the gate's three registry pointer sites in
`governance-inputs.ts`: `PWB_ACT_RECORDS`, `PWB_SUPERSEDED_ACT_RECORDS` and
the registry authority's `actIdentity` and `recordingTag`.

- Unapplied: the constant says 8388608, and the gate still names act B's
  record, identity and tag. Code never runs ahead of the signed entry.
- Applied: the constant says 16777216. The record and identity are no
  longer act B's, the tag is `pwb-registry-machine-ceiling-amendment-v1.0`,
  and the supersession target is act B's record. Any other state makes the
  PWB-REQ-005 gate refuse every Butlers read.

The check does not run automatically until its `--check` line joins the
battery, which happens in the sign-off commit.

  --write             regenerate the patch and the manifest
  --check             verify (writes nothing)
  --digests           print the manifest row (refuses while stale)
  --manifest-digest   print the SHA-256 of the manifest FILE (refuses while stale)
  --selftest          mutate each predicate; each must fail

Review-head contract: the raw's first four non-blank lines carry
`Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
FILE, as --manifest-digest prints it>` and a `Verdict:` line (`CONFIRM`,
`CONFIRM WITH EXCEPTIONS` or `REVISE`); findings are numbered
`**Finding N — title** (blocking|revise|note)`.
"""

from __future__ import annotations

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
SUBJECT = pathlib.Path(".syzygy/governance/declarations/adapter-registry/"
                       "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json")
PKG = pathlib.Path(".syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment")
PATCH = PKG / "proposed" / f"{SUBJECT.name}.patch"
MANIFEST = PKG / "PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-MANIFEST.txt"
CONSTANT_FILE = pathlib.Path("packages/three-surface-poc-core/src/project-shape-observation.ts")
GATE_FILE = pathlib.Path("apps/three-surface-poc/src/governance-inputs.ts")
#: Act B, the registry act the gate follows today: unapplied, the gate must still name it;
#: applied, the gate must name a new record, identity and tag, with act B as the supersession target.
ACT_B_RECORD = ".syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md"
ACT_B_IDENTITY = "PWB-OBSERVER-REGISTRY-ENTRY-BEHAVIOR-CONTRACT-REPIN-2026-10-02"
ACT_B_TAG = "pwb-adopt-registry-entry-signed-2026-10-02"
NEW_TAG = "pwb-registry-machine-ceiling-amendment-v1.0"
KEY_PATH = ("entries", 0, "resourceLimits", "maxMachineResponseBytes")
OLD_VALUE = 8388608
NEW_VALUE = 16777216
OLD = f'"maxMachineResponseBytes": {OLD_VALUE},'.encode()
NEW = f'"maxMachineResponseBytes": {NEW_VALUE},'.encode()
HEX64 = re.compile(r"[0-9a-f]{64}")
ROW_RE = re.compile(r"^([0-9a-f]{64})  (\S+)$", re.MULTILINE)
HEADER = (
    "# PWB REGISTRY MACHINE-CEILING AMENDMENT MANIFEST (P-114)\n"
    "# Candidate; this file and its row bind nothing by themselves.\n"
    "# 1 artifact; the row hashes the PROPOSED bytes: the subject with\n"
    "# proposed/*.patch applied (one value, maxMachineResponseBytes\n"
    "# 8388608 -> 16777216). It matches the tree only after the sign-off\n"
    "# applies the patch; until then the subject's current bytes stay the\n"
    "# argument of the act in force.\n")


class Refusal(RuntimeError):
    """The package does not verify; nothing is written."""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def base_and_state(subject: bytes) -> tuple[bytes, str]:
    """(base bytes, 'unapplied' | 'applied'), or raise Refusal."""
    if subject.count(OLD) == 1 and subject.count(NEW) == 0:
        return subject, "unapplied"
    if subject.count(NEW) == 1 and subject.count(OLD) == 0:
        return subject.replace(NEW, OLD), "applied"
    raise Refusal("the subject carries neither exactly one old nor exactly one new literal: "
                  "a sibling changed it; regenerate with --write over the new base and review again")


def proposed_bytes(base: bytes) -> bytes:
    return base.replace(OLD, NEW, 1)


def render_patch(base: bytes, proposed: bytes) -> str:
    path = SUBJECT.as_posix()
    lines = difflib.unified_diff(base.decode("utf-8").splitlines(keepends=True),
                                 proposed.decode("utf-8").splitlines(keepends=True),
                                 fromfile=f"a/{path}", tofile=f"b/{path}", n=3)
    return f"diff --git a/{path} b/{path}\n" + "".join(lines)


def render_manifest(proposed: bytes) -> str:
    return HEADER + f"{sha(proposed)}  {SUBJECT.as_posix()}\n"


def _leaves(node, prefix=()):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _leaves(v, prefix + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _leaves(v, prefix + (i,))
    else:
        yield prefix, node


def json_findings(base: bytes, proposed: bytes) -> list[str]:
    try:
        a, b = json.loads(base), json.loads(proposed)
    except ValueError as exc:
        return [f"subject or proposed bytes are not JSON: {exc}"]
    la, lb = dict(_leaves(a)), dict(_leaves(b))
    changed = sorted((k for k in set(la) | set(lb) if la.get(k, object()) != lb.get(k, object())), key=str)
    if changed != [KEY_PATH]:
        return [f"parsed entry differs at {changed}, not exactly at {KEY_PATH}"]
    if (la[KEY_PATH], lb[KEY_PATH]) != (OLD_VALUE, NEW_VALUE):
        return [f"the value moves {la[KEY_PATH]} -> {lb[KEY_PATH]}, not {OLD_VALUE} -> {NEW_VALUE}"]
    return []


def _git_apply_check(root: pathlib.Path, patch_text: str, reverse: bool) -> str | None:
    with tempfile.TemporaryDirectory() as t:
        tmp = pathlib.Path(t)
        (tmp / SUBJECT).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / SUBJECT, tmp / SUBJECT)
        (tmp / "p.patch").write_text(patch_text, encoding="utf-8")
        args = ["git", "apply", "--check"] + (["-R"] if reverse else []) + ["p.patch"]
        done = subprocess.run(args, cwd=tmp, capture_output=True, text=True)
        return None if done.returncode == 0 else done.stderr.strip()


def check(root: pathlib.Path = ROOT) -> tuple[list[str], str]:
    out: list[str] = []
    subject = root / SUBJECT
    if not subject.is_file():
        return [f"{SUBJECT.as_posix()} is missing"], "absent"
    try:
        base, state = base_and_state(subject.read_bytes())
    except Refusal as exc:
        return [str(exc)], "stale"
    proposed = proposed_bytes(base)
    out += json_findings(base, proposed)
    patch_text = render_patch(base, proposed)
    patch = root / PATCH
    if not patch.is_file() or patch.read_text(encoding="utf-8") != patch_text:
        out.append(f"{PATCH.as_posix()} differs from its regeneration; run --write")
    else:
        problem = _git_apply_check(root, patch_text, reverse=(state == "applied"))
        if problem is not None:
            out.append(f"the patch does not apply ({'reverse' if state == 'applied' else 'forward'}): {problem}")
    manifest = root / MANIFEST
    if not manifest.is_file() or manifest.read_text(encoding="utf-8") != render_manifest(proposed):
        out.append(f"{MANIFEST.as_posix()} differs from its regeneration; run --write")
    if state == "applied" and sha(subject.read_bytes()) != sha(proposed):
        out.append("the applied subject does not hash to the manifest row")
    for md in sorted((root / PKG).glob("*.md")):
        if re.search(r"ROUND-\d+-DISPOSITIONS\.md$", md.name):
            continue
        if HEX64.search(md.read_text(encoding="utf-8")):
            out.append(f"{md.name}: carries a 64-hex token")
    out += code_findings(root, state)
    return out, state


def _strip_comments(text: str) -> str:
    return re.sub(r"//[^\n]*", "", text)


def object_block(text: str, name: str) -> str | None:
    """The body of `export const <name> ... = { ... };`, comments removed."""
    m = re.search(rf"^export const {re.escape(name)}\b[^=]*=\s*\{{(.*?)^\}};", text, re.M | re.S)
    return None if m is None else _strip_comments(m.group(1))


def _quoted(block: str, key: str) -> list[str]:
    return re.findall(rf"\b{key}:\s*['\"`]([^'\"`]*)['\"`]", block)


def registry_authority(gate: str) -> str | None:
    """The `registry: { artifactPath: PWB_AUTHORITY_ARTIFACTS.registry, ... }` expectations object."""
    m = re.search(r"registry:\s*\{\s*artifactPath:\s*PWB_AUTHORITY_ARTIFACTS\.registry,(.*?)\n\s*\},", gate, re.S)
    return None if m is None else _strip_comments(m.group(1))


def code_findings(root: pathlib.Path, state: str) -> list[str]:
    """Hold the daemon's hard-coded ceiling and the gate's registry pointers to the entry's state."""
    out: list[str] = []
    text = (root / CONSTANT_FILE).read_text(encoding="utf-8") if (root / CONSTANT_FILE).is_file() else ""
    limits = object_block(text, "PWB_RESOURCE_LIMITS")
    values = [] if limits is None else [int(v) for v in re.findall(r"\bmaxMachineResponseBytes:\s*(\d+)", limits)]
    want = OLD_VALUE if state == "unapplied" else NEW_VALUE
    if values != [want]:
        what = ("code runs ahead of the signed entry" if state == "unapplied"
                else "the entry is applied without the constant change")
        out.append(f"{CONSTANT_FILE.as_posix()} PWB_RESOURCE_LIMITS.maxMachineResponseBytes is {values}, "
                   f"not [{want}]: {what}")
    gate = (root / GATE_FILE).read_text(encoding="utf-8") if (root / GATE_FILE).is_file() else ""
    records = object_block(gate, "PWB_ACT_RECORDS")
    superseded = object_block(gate, "PWB_SUPERSEDED_ACT_RECORDS")
    authority = registry_authority(gate)
    if records is None or superseded is None or authority is None:
        return out + [f"{GATE_FILE.as_posix()}: the registry act pointers cannot be located"]
    record = _quoted(records, "registry")
    target = _quoted(superseded, "registry")
    identity = _quoted(authority, "actIdentity")
    tag = _quoted(authority, "recordingTag")
    if state == "unapplied":
        if (record, identity, tag) != ([ACT_B_RECORD], [ACT_B_IDENTITY], [ACT_B_TAG]):
            out.append(f"{GATE_FILE.as_posix()}: the gate's registry act moved off act B before the entry: "
                       "code runs ahead of the signed entry")
        return out
    if record in ([], [ACT_B_RECORD]) or len(record) != 1:
        out.append(f"{GATE_FILE.as_posix()} PWB_ACT_RECORDS.registry is {record}: "
                   "the PWB-REQ-005 gate refuses every Butlers read")
    if target != [ACT_B_RECORD]:
        out.append(f"{GATE_FILE.as_posix()} PWB_SUPERSEDED_ACT_RECORDS.registry is {target}, not act B's record")
    if identity in ([], [ACT_B_IDENTITY]) or len(identity) != 1:
        out.append(f"{GATE_FILE.as_posix()} registry actIdentity is {identity}: still act B's")
    if tag != [NEW_TAG]:
        out.append(f"{GATE_FILE.as_posix()} registry recordingTag is {tag}, not {NEW_TAG!r}")
    return out


def write(root: pathlib.Path = ROOT) -> int:
    base, _ = base_and_state((root / SUBJECT).read_bytes())
    proposed = proposed_bytes(base)
    (root / PATCH).parent.mkdir(parents=True, exist_ok=True)
    (root / PATCH).write_text(render_patch(base, proposed), encoding="utf-8")
    (root / MANIFEST).write_text(render_manifest(proposed), encoding="utf-8")
    print(f"wrote {PATCH.as_posix()} and {MANIFEST.as_posix()}")
    return 0


# --- selftest ---------------------------------------------------------------

def _set_constant(path: pathlib.Path, value: int) -> None:
    text = path.read_text(encoding="utf-8")
    block = object_block(text, "PWB_RESOURCE_LIMITS")
    assert block is not None
    new = re.sub(r"(\bmaxMachineResponseBytes:\s*)\d+", rf"\g<1>{value}", text, count=1)
    path.write_text(new, encoding="utf-8")


def _fixture(tmp: pathlib.Path) -> pathlib.Path:
    """The unapplied state over the real files: entry base, constant 8 MiB, gate on act B."""
    for rel in (SUBJECT, CONSTANT_FILE, GATE_FILE):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, tmp / rel)
    (tmp / PKG).mkdir(parents=True, exist_ok=True)
    base, _ = base_and_state((ROOT / SUBJECT).read_bytes())
    (tmp / SUBJECT).write_bytes(base)
    _set_constant(tmp / CONSTANT_FILE, OLD_VALUE)
    write_quiet(tmp)
    return tmp


def write_quiet(root: pathlib.Path) -> None:
    import contextlib
    import io
    with contextlib.redirect_stdout(io.StringIO()):
        write(root)


NEXT_RECORD = ".syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md"
NEXT_IDENTITY = "PWB-OBSERVER-REGISTRY-ENTRY-MACHINE-CEILING-2026-10-20"
CURRENCY_RECORD = ".syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md"


def _apply_fixture(tmp: pathlib.Path) -> None:
    """The state ask 2 prescribes: entry patched, constant 16 MiB, the four gate pointers moved
    (record, identity and tag to the new act; supersession target to act B)."""
    (tmp / SUBJECT).write_bytes(proposed_bytes((tmp / SUBJECT).read_bytes()))
    _set_constant(tmp / CONSTANT_FILE, NEW_VALUE)
    gate = (tmp / GATE_FILE).read_text(encoding="utf-8")
    gate = gate.replace(f"registry: '{ACT_B_RECORD}'", f"registry: '{NEXT_RECORD}'", 1)
    gate = gate.replace(f"registry: '{CURRENCY_RECORD}'", f"registry: '{ACT_B_RECORD}'", 1)
    gate = gate.replace(f"actIdentity: '{ACT_B_IDENTITY}'", f"actIdentity: '{NEXT_IDENTITY}'", 1)
    gate = gate.replace(f"recordingTag: '{ACT_B_TAG}'", f"recordingTag: '{NEW_TAG}'", 1)
    (tmp / GATE_FILE).write_text(gate, encoding="utf-8")


def _edit_gate(tmp: pathlib.Path, old: str, new: str) -> None:
    gate = (tmp / GATE_FILE).read_text(encoding="utf-8")
    assert gate.count(old) >= 1, old
    (tmp / GATE_FILE).write_text(gate.replace(old, new, 1), encoding="utf-8")


def selftest() -> int:
    results: list[tuple[str, bool]] = []

    def case(name, mutate, needle=None, expect_clean=False):
        with tempfile.TemporaryDirectory() as t:
            tmp = _fixture(pathlib.Path(t))
            mutate(tmp)
            found, _ = check(tmp)
            ok = (found == []) if expect_clean else any(needle in f for f in found)
            if not ok:
                print(f"     ({name}: {found})")
            results.append((name, ok))

    case("the shipped package verifies unapplied", lambda tmp: None, expect_clean=True)
    case("the prescribed applied state verifies (entry, constant, four gate pointers)",
         _apply_fixture, expect_clean=True)

    def edit_inside_context(tmp):
        p = tmp / SUBJECT
        p.write_bytes(p.read_bytes().replace(b'"maxHumanResponseBytes": 2097152', b'"maxHumanResponseBytes": 2097153', 1))
    case("a sibling's edit inside the hunk context makes the patch stale", edit_inside_context,
         ".patch differs from its regeneration")

    def edit_outside_context(tmp):
        p = tmp / SUBJECT
        p.write_bytes(p.read_bytes().replace(b'"schemaVersion": 1,', b'"schemaVersion": 1, ', 1))
    case("a sibling's edit outside the hunk context makes the manifest stale", edit_outside_context,
         "MANIFEST.txt differs from its regeneration")

    def two_values(tmp):
        p = tmp / SUBJECT
        p.write_bytes(p.read_bytes() + b"\n" + OLD)
    case("a second old literal refuses", two_values, "neither exactly one")

    def stale_manifest(tmp):
        m = tmp / MANIFEST
        last = m.read_text().splitlines()[-1]
        m.write_text(m.read_text().replace(last, "0" * 64 + last[64:]))
    case("a stale manifest row refuses", stale_manifest, "MANIFEST.txt differs from its regeneration")

    def edited_patch(tmp):
        p = tmp / PATCH
        p.write_text(p.read_text().replace("16777216", "16777217"))
    case("an edited patch refuses", edited_patch, ".patch differs from its regeneration")

    def hex_in_md(tmp):
        (tmp / PKG / "SEMANTIC-DELTA.md").write_text("x " + "a" * 64 + "\n")
    case("a digest in a package Markdown file refuses", hex_in_md, "64-hex")

    def disposition_hex(tmp):
        (tmp / PKG / "ROUND-1-DISPOSITIONS.md").write_text("x " + "a" * 64 + "\n")
    case("a round disposition record may quote a digest", disposition_hex, expect_clean=True)

    case("code running ahead of the signed entry refuses",
         lambda tmp: _set_constant(tmp / CONSTANT_FILE, NEW_VALUE), "code runs ahead")

    def ahead_with_comment(tmp):
        _set_constant(tmp / CONSTANT_FILE, NEW_VALUE)
        p = tmp / CONSTANT_FILE
        p.write_text(p.read_text().replace("export const PWB_RESOURCE_LIMITS",
                                           "// maxMachineResponseBytes: 8388608,\nexport const PWB_RESOURCE_LIMITS", 1))
    case("an old value left in a comment does not hide code running ahead", ahead_with_comment, "code runs ahead")

    def ahead_comment_inside(tmp):
        _set_constant(tmp / CONSTANT_FILE, NEW_VALUE)
        p = tmp / CONSTANT_FILE
        p.write_text(p.read_text().replace("  maxMachineResponseBytes: 16777216,",
                                           "  // maxMachineResponseBytes: 8388608,\n  maxMachineResponseBytes: 16777216,", 1))
    case("an old value in a comment inside the object does not hide code running ahead",
         ahead_comment_inside, "code runs ahead")

    case("the gate moving off act B before the entry refuses",
         lambda tmp: _edit_gate(tmp, f"recordingTag: '{ACT_B_TAG}'", f"recordingTag: '{NEW_TAG}'"),
         "moved off act B before the entry")

    def applied_no_code(tmp):
        _apply_fixture(tmp)
        _set_constant(tmp / CONSTANT_FILE, OLD_VALUE)
    case("an applied entry without the constant change refuses", applied_no_code, "without the constant change")

    def applied_record_unmoved(tmp):
        _apply_fixture(tmp)
        _edit_gate(tmp, f"registry: '{NEXT_RECORD}'", f"registry: '{ACT_B_RECORD}'")
    case("applied, the act record pointer left on act B refuses", applied_record_unmoved,
         "refuses every Butlers read")

    def applied_record_double_quoted(tmp):
        _apply_fixture(tmp)
        _edit_gate(tmp, f"registry: '{NEXT_RECORD}'", f'registry: "{ACT_B_RECORD}"')
    case("applied, act B's record in double quotes still refuses", applied_record_double_quoted,
         "refuses every Butlers read")

    def applied_target_unmoved(tmp):
        _apply_fixture(tmp)
        _edit_gate(tmp, f"registry: '{ACT_B_RECORD}'", f"registry: '{CURRENCY_RECORD}'")
    case("applied, the supersession target left on the currency-briefing act refuses", applied_target_unmoved,
         "not act B's record")

    def applied_identity_unmoved(tmp):
        _apply_fixture(tmp)
        _edit_gate(tmp, f"actIdentity: '{NEXT_IDENTITY}'", f"actIdentity: '{ACT_B_IDENTITY}'")
    case("applied, act B's identity left in place refuses", applied_identity_unmoved, "still act B's")

    def applied_tag_unmoved(tmp):
        _apply_fixture(tmp)
        _edit_gate(tmp, f"recordingTag: '{NEW_TAG}'", f"recordingTag: '{ACT_B_TAG}'")
    case("applied, act B's recording tag left in place refuses", applied_tag_unmoved, "recordingTag")

    def gate_unlocatable(tmp):
        _edit_gate(tmp, "export const PWB_ACT_RECORDS", "export const PWB_ACT_RECORDZ")
    case("a gate whose pointers cannot be located refuses", gate_unlocatable, "cannot be located")

    # The JSON predicate on its own: a proposal that moves a second key, or another value.
    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        base = (tmp / SUBJECT).read_bytes()
        bad = proposed_bytes(base).replace(b'"maxBriefingResponseBytes": 20480', b'"maxBriefingResponseBytes": 20481')
        results.append(("a second changed key is refused by the parsed comparison",
                        any("not exactly at" in f for f in json_findings(base, bad))))
        wrong = base.replace(OLD, b'"maxMachineResponseBytes": 9999999,', 1)
        results.append(("another new value is refused by the parsed comparison",
                        any("not 8388608 -> 16777216" in f for f in json_findings(base, wrong))))

    failed = [n for n, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if argv == ["--write"]:
        return write(ROOT)
    if argv in (["--check"], ["--digests"], ["--manifest-digest"]):
        findings, state = check(ROOT)
        if argv == ["--check"]:
            for f in findings:
                print(f"FAIL {f}")
            print(f"pwb-registry-machine-ceiling-amendment: {state}, "
                  + (f"{len(findings)} findings" if findings else "verifies"))
            return 1 if findings else 0
        if findings:
            print("refusing: the package is stale; run --check")
            return 1
        if argv == ["--digests"]:
            print(ROW_RE.search((ROOT / MANIFEST).read_text()).group(0))
        else:
            print(f"{sha((ROOT / MANIFEST).read_bytes())}  {MANIFEST.as_posix()}")
        return 0
    print(__doc__)
    print("refusing: pass exactly one of --write, --check, --digests, --manifest-digest, --selftest")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
