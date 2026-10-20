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

In both states the patch file equals its regeneration and applies with
`git apply --check` (forward unapplied, reverse applied), the manifest is
exactly one row equal to the proposed bytes' SHA-256, and no package Markdown
file carries a 64-hex token. It also holds the code to the entry, since the
daemon hard-codes the ceiling rather than reading it: unapplied, the
`PWB_RESOURCE_LIMITS` constant must still say 8388608 (code never runs ahead
of the signed entry); applied, it must say 16777216 and the gate's registry
act pointer must have left the 2026-10-02 re-pin act, or every Butlers read
is refused.

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
#: The act the gate follows for the registry today; an applied entry must not still point at it.
CURRENT_GATE_RECORD = ".syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md"
KEY_PATH = ("entries", 0, "resourceLimits", "maxMachineResponseBytes")
OLD_VALUE = 8388608
NEW_VALUE = 16777216
OLD = f'"maxMachineResponseBytes": {OLD_VALUE},'.encode()
NEW = f'"maxMachineResponseBytes": {NEW_VALUE},'.encode()
CONSTANT_OLD = f"maxMachineResponseBytes: {OLD_VALUE},"
CONSTANT_NEW = f"maxMachineResponseBytes: {NEW_VALUE},"
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
    elif len(ROW_RE.findall(manifest.read_text(encoding="utf-8"))) != 1:
        out.append("the manifest does not carry exactly one row")
    if state == "applied" and sha(subject.read_bytes()) != sha(proposed):
        out.append("the applied subject does not hash to the manifest row")
    for md in sorted((root / PKG).glob("*.md")):
        if re.search(r"ROUND-\d+-DISPOSITIONS\.md$", md.name):
            continue
        if HEX64.search(md.read_text(encoding="utf-8")):
            out.append(f"{md.name}: carries a 64-hex token")
    constant = (root / CONSTANT_FILE).read_text(encoding="utf-8") if (root / CONSTANT_FILE).is_file() else ""
    if state == "unapplied" and CONSTANT_OLD not in constant:
        out.append(f"{CONSTANT_FILE.as_posix()} no longer declares {CONSTANT_OLD!r}: code runs ahead of the signed entry")
    if state == "applied":
        if CONSTANT_NEW not in constant:
            out.append(f"the entry is applied but {CONSTANT_FILE.as_posix()} does not declare {CONSTANT_NEW!r}")
        gate = (root / GATE_FILE).read_text(encoding="utf-8") if (root / GATE_FILE).is_file() else ""
        if f"registry: '{CURRENT_GATE_RECORD}'" in gate:
            out.append(f"the entry is applied but {GATE_FILE.as_posix()} still points the registry act at "
                       f"{CURRENT_GATE_RECORD}: the PWB-REQ-005 gate refuses every Butlers read")
    return out, state


def write(root: pathlib.Path = ROOT) -> int:
    base, _ = base_and_state((root / SUBJECT).read_bytes())
    proposed = proposed_bytes(base)
    (root / PATCH).parent.mkdir(parents=True, exist_ok=True)
    (root / PATCH).write_text(render_patch(base, proposed), encoding="utf-8")
    (root / MANIFEST).write_text(render_manifest(proposed), encoding="utf-8")
    print(f"wrote {PATCH.as_posix()} and {MANIFEST.as_posix()}")
    return 0


# --- selftest ---------------------------------------------------------------

def _fixture(tmp: pathlib.Path) -> pathlib.Path:
    for rel in (SUBJECT, CONSTANT_FILE, GATE_FILE):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, tmp / rel)
    (tmp / PKG).mkdir(parents=True, exist_ok=True)
    base, _ = base_and_state((ROOT / SUBJECT).read_bytes())
    (tmp / SUBJECT).write_bytes(base)
    (tmp / CONSTANT_FILE).write_text((ROOT / CONSTANT_FILE).read_text().replace(CONSTANT_NEW, CONSTANT_OLD))
    write_quiet(tmp)
    return tmp


def write_quiet(root: pathlib.Path) -> None:
    import contextlib
    import io
    with contextlib.redirect_stdout(io.StringIO()):
        write(root)


def _apply_fixture(tmp: pathlib.Path) -> None:
    (tmp / SUBJECT).write_bytes(proposed_bytes((tmp / SUBJECT).read_bytes()))
    (tmp / CONSTANT_FILE).write_text((tmp / CONSTANT_FILE).read_text().replace(CONSTANT_OLD, CONSTANT_NEW))
    gate = (tmp / GATE_FILE).read_text()
    (tmp / GATE_FILE).write_text(gate.replace(f"registry: '{CURRENT_GATE_RECORD}'",
                                              "registry: '.syzygy/governance/decisions/NEXT-ACT.md'"))


def selftest() -> int:
    results: list[tuple[str, bool]] = []

    def case(name, mutate, needle=None, expect_clean=False):
        with tempfile.TemporaryDirectory() as t:
            tmp = _fixture(pathlib.Path(t))
            mutate(tmp)
            found, _ = check(tmp)
            ok = (found == []) if expect_clean else any(needle in f for f in found)
            results.append((name, ok))

    case("the shipped package verifies unapplied", lambda tmp: None, expect_clean=True)
    case("the applied state verifies with the paired code change", _apply_fixture, expect_clean=True)

    def edit_subject_elsewhere(tmp):
        p = tmp / SUBJECT
        p.write_bytes(p.read_bytes().replace(b'"maxHumanResponseBytes": 2097152', b'"maxHumanResponseBytes": 2097153', 1))
    case("a sibling's edit to the subject makes the patch stale", edit_subject_elsewhere, "differs from its regeneration")

    def two_values(tmp):
        p = tmp / SUBJECT
        p.write_bytes(p.read_bytes() + b"\n" + OLD)
    case("a second old literal refuses", two_values, "neither exactly one")

    def stale_manifest(tmp):
        m = tmp / MANIFEST
        m.write_text(m.read_text().replace(m.read_text().splitlines()[-1][:4], "0000", 1))
    case("a stale manifest row refuses", stale_manifest, "MANIFEST.txt differs")

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

    def code_ahead(tmp):
        p = tmp / CONSTANT_FILE
        p.write_text(p.read_text().replace(CONSTANT_OLD, CONSTANT_NEW))
    case("code running ahead of the signed entry refuses", code_ahead, "runs ahead")

    def applied_no_code(tmp):
        _apply_fixture(tmp)
        p = tmp / CONSTANT_FILE
        p.write_text(p.read_text().replace(CONSTANT_NEW, CONSTANT_OLD))
    case("an applied entry without the constant change refuses", applied_no_code, "does not declare")

    def applied_old_gate(tmp):
        _apply_fixture(tmp)
        shutil.copyfile(ROOT / GATE_FILE, tmp / GATE_FILE)
    case("an applied entry with the gate still on the 2026-10-02 act refuses", applied_old_gate,
         "refuses every Butlers read")

    # The JSON predicate on its own: a proposal that moves a second key.
    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        base = (tmp / SUBJECT).read_bytes()
        bad = proposed_bytes(base).replace(b'"maxBriefingResponseBytes": 20480', b'"maxBriefingResponseBytes": 20481')
        found = json_findings(base, bad)
        results.append(("a second changed key is refused by the parsed comparison",
                        any("not exactly at" in f for f in found)))
        wrong = base.replace(OLD, b'"maxMachineResponseBytes": 9999999,', 1)
        results.append(("another new value is refused by the parsed comparison",
                        any("not 8388608 -> 16777216" in f for f in json_findings(base, wrong))))
        results.append(("the proposed bytes differ from the base in exactly one line",
                        sum(1 for a, b in zip(base.splitlines(), proposed_bytes(base).splitlines()) if a != b) == 1
                        and len(base.splitlines()) == len(proposed_bytes(base).splitlines())))

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
