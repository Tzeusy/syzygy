#!/usr/bin/env python3
"""Build and verify the inert PWB behaviour-contract re-pin package.

Bead `syzygy-jloi`; package
`contracts/candidates/pwb-behavior-contract-repin/`. This script performs no
owner act and writes no act record.

Two governed artifacts pin `governingBehaviorContract.version` to the PWB
`spec.md` of the 2026-09-05 truth-and-readiness act, and say in `signedBy`
that the act is still pending: the observer registry entry (argument of the
2026-09-30 `adopt-registry-entry` act) and the secret-classification policy
(argument of the 2026-09-05 `approve-policy` amendment act). Every PWB
specification change since has moved `spec.md`, so both pins name superseded
bytes. The package re-pins both to the `spec.md` digest the current signed
PWB package (`pwb-readability-successor` v1.0) carries as its manifest row,
and names that sign-off in `signedBy`. Nothing else in either file moves.

Each subject keeps the act in force over it until its own superseding act is
performed: the proposed bytes live only as one unified diff per subject under
`proposed/`, and the two-row `PWB-EFFECT-REPIN-MANIFEST.txt` hashes the bytes
those diffs produce. Each row is the argument a superseding act over that
subject would take; neither row binds the other.

`--check` verifies, per subject:

- before its act (no superseding record): the subject hashes to the exact
  digest of the act in force, the patch applies, and the result satisfies the
  package's structural claims; the pinned digest is also the current `spec.md`
  (a package drafted over a superseded spec is stale and must be redrafted);
- after its act (the superseding record exists): reversing the patch over the
  subject yields the predecessor act's bytes, so the tree carries exactly the
  proposed bytes;
- always: the manifest is the exact regeneration over the proposed bytes, and
  `proposed/` holds exactly the two declared patches.

`--selftest` copies every input into a scratch tree and mutates each predicate
in turn, requiring the check to fail; it also drives the post-act mode with a
synthetic record.

Review-head contract (for the recorder that is written after the review, as
`record_pwb_registry_currency_amendment.py` was): the raw's first four
non-blank lines carry exactly one `Reviewed commit: <40 hex>`, one
`Manifest SHA-256: <64 hex>` naming the SHA-256 of the manifest FILE
`PWB-EFFECT-REPIN-MANIFEST.txt` (which carries both act arguments as rows),
and one `Verdict:` line reading `CONFIRM` or `CONFIRM WITH EXCEPTIONS`.
Findings are numbered `**Finding N — title** (blocking|revise|note)`.
`--manifest-digest` prints the value that line must carry.

Bare invocation refuses to overwrite the manifest; `--write` regenerates it,
which changes both act arguments and retires any review bound to the old one.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-behavior-contract-repin")
PROPOSED = CANDIDATE / "proposed"
OUT = CANDIDATE / "PWB-EFFECT-REPIN-MANIFEST.txt"
TITLE = "PWB BEHAVIOUR-CONTRACT RE-PIN EFFECT AMENDMENT MANIFEST"

PWB_SPEC = pathlib.Path(
    "openspec/changes/polaris-project-wide-butlers-model/specs/"
    "polaris-project-wide-butlers-model/spec.md")
#: The signed package whose manifest row fixes the spec digest pinned.
SIGNING_MANIFEST = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-readability-successor/"
    "PWB-READABILITY-SUCCESSOR-MANIFEST.txt")
SIGNING_RECORD = DECISIONS / "PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md"
SIGNING_TAG = "pwb-readability-successor-v1.0"
CONTRACT_ID = "polaris-project-wide-butlers-model"
SIGNED_BY = (f"version-tagged sign-off {SIGNING_TAG}, recorded at "
             f"{SIGNING_RECORD.as_posix()}")
CONTRACT_KEYS = ("id", "version", "signedBy")

ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
EXACT_DIGEST_RE = re.compile(
    r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Subject:
    key: str
    path: pathlib.Path
    act_type: str
    predecessor: pathlib.Path      # the record of the act in force today
    record: pathlib.Path           # the superseding record this package offers
    locate: str                    # "entry" (entries[0]) or "top" (document)


SUBJECTS = (
    Subject(
        "registry",
        pathlib.Path(".syzygy/governance/declarations/adapter-registry/"
                     "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"),
        "adopt-registry-entry",
        DECISIONS / "PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md",
        DECISIONS / "PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md",
        "entry",
    ),
    Subject(
        "policy",
        pathlib.Path(".syzygy/governance/policies/"
                     "POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"),
        "approve-policy",
        DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md",
        DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md",
        "top",
    ),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def patch_path(subject: Subject) -> pathlib.Path:
    return PROPOSED / f"{subject.path.name}.patch"


def performed(root: pathlib.Path, subject: Subject) -> bool:
    return (root / subject.record).is_file()


def read(root: pathlib.Path, rel: pathlib.Path) -> bytes:
    target = root / rel
    if not target.is_file():
        raise ValueError(f"missing input: {rel.as_posix()}")
    return target.read_bytes()


def predecessor_digest(root: pathlib.Path, subject: Subject) -> str:
    found = EXACT_DIGEST_RE.findall(read(root, subject.predecessor).decode())
    if len(found) != 1:
        raise ValueError(f"{subject.predecessor.as_posix()} does not carry exactly "
                         "one exact digest line")
    return found[0]


def signed_spec_digest(root: pathlib.Path) -> str:
    rows = [sha for sha, path in ROW.findall(read(root, SIGNING_MANIFEST).decode())
            if path == PWB_SPEC.as_posix()]
    if len(rows) != 1:
        raise ValueError(f"{SIGNING_MANIFEST.as_posix()} does not carry exactly one "
                         f"row for {PWB_SPEC.as_posix()}")
    return rows[0]


def _apply(root: pathlib.Path, subject: Subject, body: bytes, reverse: bool) -> bytes:
    patch = root / patch_path(subject)
    if not patch.is_file():
        raise ValueError(f"missing patch: {patch_path(subject).as_posix()}")
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / subject.path).parent.mkdir(parents=True, exist_ok=True)
        (base / subject.path).write_bytes(body)
        args = ["git", "apply", "--whitespace=nowarn"]
        if reverse:
            args.append("-R")
        done = subprocess.run([*args, str(patch.resolve())], cwd=base,
                              capture_output=True, text=True)
        if done.returncode != 0:
            raise ValueError(
                f"{patch.name} does not {'reverse-' if reverse else ''}apply to "
                f"{subject.path.as_posix()}: {done.stderr.strip()}")
        return (base / subject.path).read_bytes()


def base_bytes(root: pathlib.Path, subject: Subject) -> bytes:
    """The bytes the patch applies to: the act in force's argument.

    Before the act, the tree. After it, the tree with the patch reversed;
    either way the result must hash to the predecessor act's exact digest.
    """
    live = read(root, subject.path)
    body = _apply(root, subject, live, reverse=True) if performed(root, subject) else live
    want = predecessor_digest(root, subject)
    if sha256(body) != want:
        state = ("the tree with the patch reversed" if performed(root, subject)
                 else "the subject")
        raise ValueError(
            f"{subject.key}: {state} hashes to {sha256(body)}, not the argument "
            f"{want} of {subject.predecessor.as_posix()}")
    return body


def proposed_bytes(root: pathlib.Path, subject: Subject) -> bytes:
    return _apply(root, subject, base_bytes(root, subject), reverse=False)


def _contract(doc, subject: Subject):
    if subject.locate == "entry":
        entries = doc.get("entries") if isinstance(doc, dict) else None
        if not isinstance(entries, list) or len(entries) != 1:
            raise ValueError("does not carry exactly one registry entry")
        holder = entries[0]
    else:
        holder = doc
    if not isinstance(holder, dict) or not isinstance(
            holder.get("governingBehaviorContract"), dict):
        raise ValueError("carries no governingBehaviorContract object")
    return holder, holder["governingBehaviorContract"]


def _count_contracts(node) -> int:
    if isinstance(node, dict):
        return sum((key == "governingBehaviorContract") + _count_contracts(value)
                   for key, value in node.items())
    if isinstance(node, list):
        return sum(_count_contracts(value) for value in node)
    return 0


def structure_findings(root: pathlib.Path, subject: Subject, base: bytes,
                       proposed: bytes) -> list[str]:
    """Every claim the package makes about one subject's proposed bytes."""
    label = subject.key
    try:
        new = json.loads(proposed)
        old = json.loads(base)
    except ValueError as error:
        return [f"{label}: proposed or base bytes are not valid JSON: {error}"]
    findings: list[str] = []
    if _count_contracts(new) != 1:
        findings.append(f"{label}: proposed bytes carry {_count_contracts(new)} "
                        "governingBehaviorContract objects, not one")
    try:
        _holder, contract = _contract(new, subject)
        _old_holder, old_contract = _contract(old, subject)
    except ValueError as error:
        return findings + [f"{label}: {error}"]
    if tuple(contract) != CONTRACT_KEYS:
        findings.append(f"{label}: governingBehaviorContract keys are "
                        f"{list(contract)}, not {list(CONTRACT_KEYS)}")
    if contract.get("id") != CONTRACT_ID:
        findings.append(f"{label}: governingBehaviorContract.id is "
                        f"{contract.get('id')!r}, not {CONTRACT_ID!r}")
    try:
        signed = "sha256:" + signed_spec_digest(root)
    except ValueError as error:
        findings.append(f"{label}: {error}")
    else:
        if contract.get("version") != signed:
            findings.append(f"{label}: governingBehaviorContract.version is "
                            f"{contract.get('version')!r}, not the signed spec.md "
                            f"row {signed}")
    if contract.get("signedBy") != SIGNED_BY:
        findings.append(f"{label}: signedBy does not name {SIGNING_TAG} and its record")
    record = root / SIGNING_RECORD
    if not record.is_file() or f"Tag: {SIGNING_TAG}" not in record.read_text().splitlines():
        findings.append(f"{label}: {SIGNING_RECORD.as_posix()} is missing or does not "
                        f"name the tag {SIGNING_TAG}")
    if contract == old_contract:
        findings.append(f"{label}: the proposed patch changes nothing in "
                        "governingBehaviorContract")
    # Nothing but the contract moves: with the old contract put back, the two
    # documents are equal, and so are the bytes outside its two value lines.
    restored = json.loads(proposed)
    _h, restored_contract = _contract(restored, subject)
    restored_contract.clear()
    restored_contract.update(old_contract)
    if restored != old:
        findings.append(f"{label}: the patch changes more than governingBehaviorContract")
    changed = [line for line in proposed.decode().splitlines()
               if line not in base.decode().splitlines()]
    if len(changed) != 2 or not all(
            line.strip().startswith(('"version": "sha256:', '"signedBy": '))
            for line in changed):
        findings.append(f"{label}: the patch does not change exactly the two "
                        "version and signedBy lines")
    return findings


def render(proposed: dict[str, bytes]) -> str:
    lines = [
        f"# {TITLE}",
        "# Candidate; this file and its rows bind nothing by themselves.",
        "# 2 artifacts; rows sorted by codepoint path; each row hashes the PROPOSED",
        "# bytes (the act-in-force bytes with proposed/<name>.patch applied) and is",
        "# the argument of one superseding act over that subject.",
        "# Each row requires its own separate owner act; neither row binds the other.",
    ]
    lines.extend(f"{sha256(proposed[s.key])}  {s.path.as_posix()}"
                 for s in sorted(SUBJECTS, key=lambda s: s.path.as_posix()))
    return "\n".join(lines) + "\n"


def check(root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    found = sorted(p.name for p in (root / PROPOSED).glob("*")) if (root / PROPOSED).is_dir() else []
    want = sorted(patch_path(s).name for s in SUBJECTS)
    if found != want:
        findings.append(f"proposed/ holds {found}, not exactly {want}")
    proposed: dict[str, bytes] = {}
    for subject in SUBJECTS:
        try:
            base = base_bytes(root, subject)
            body = _apply(root, subject, base, reverse=False)
        except ValueError as error:
            findings.append(str(error))
            continue
        proposed[subject.key] = body
        findings.extend(structure_findings(root, subject, base, body))
        if performed(root, subject):
            if read(root, subject.path) != body:
                findings.append(f"{subject.key}: the act is performed but the subject "
                                "is not the proposed bytes")
        else:
            current = "sha256:" + sha256(read(root, PWB_SPEC))
            pinned = json.loads(body)
            _h, contract = _contract(pinned, subject)
            if contract.get("version") != current:
                findings.append(
                    f"{subject.key}: the proposed pin {contract.get('version')} is not "
                    f"the current {PWB_SPEC.as_posix()} ({current}); the package is "
                    "stale and must be redrafted before its act")
    if len(proposed) == len(SUBJECTS):
        target = root / OUT
        if not target.is_file():
            findings.append(f"manifest missing: {OUT.as_posix()}")
        else:
            text = target.read_text()
            rows = [path for _sha, path in ROW.findall(text)]
            if rows != sorted(s.path.as_posix() for s in SUBJECTS):
                findings.append("manifest row population or order differs")
            if text != render(proposed):
                findings.append("manifest differs from exact regeneration over the "
                                "proposed bytes")
    return findings


def apply(at_adoption: bool, keys: tuple[str, ...], root: pathlib.Path = ROOT) -> int:
    """The adoption step for the named subjects; belongs in the act's change."""
    if not at_adoption:
        print("refusing: --apply writes over an artifact a performed act still "
              "binds; it is the adoption step. Pass --at-adoption.")
        return 2
    findings = check(root)
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    for subject in SUBJECTS:
        if subject.key in keys and not performed(root, subject):
            (root / subject.path).write_bytes(proposed_bytes(root, subject))
            print(f"applied {subject.path.as_posix()}")
    return 0


# --- selftest ----------------------------------------------------------------

def _inputs() -> list[pathlib.Path]:
    paths = {OUT, PWB_SPEC, SIGNING_MANIFEST, SIGNING_RECORD}
    for subject in SUBJECTS:
        paths |= {subject.path, subject.predecessor, patch_path(subject)}
    return sorted(paths, key=lambda p: p.as_posix())


def _scratch(dest: pathlib.Path) -> None:
    """Copy every input into `dest` in the pre-act state.

    The superseding records are not inputs, so once an act is performed the
    subject is replayed as the bytes the act in force bound (the tree with
    the patch reversed); the fixtures then mean the same before and after
    the 2026-10-02 acts.
    """
    for rel in _inputs():
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, dest / rel)
    for subject in SUBJECTS:
        if performed(ROOT, subject):
            (dest / subject.path).write_bytes(base_bytes(ROOT, subject))


def _edit(rel: pathlib.Path, old: str, new: str):
    def mutate(root: pathlib.Path) -> None:
        text = (root / rel).read_text()
        if old not in text:
            raise AssertionError(f"mutation target absent in {rel.as_posix()}: {old[:60]!r}")
        (root / rel).write_text(text.replace(old, new, 1))
    return mutate


def selftest() -> int:
    registry, policy = SUBJECTS
    results: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory() as tmp:
        clean = pathlib.Path(tmp) / "clean"
        _scratch(clean)
        baseline = check(clean)
        results.append(("the unmutated scratch copy verifies", baseline == []))
        if baseline:
            print("\n".join(f"  {f}" for f in baseline))
        spec_digest = signed_spec_digest(clean)
        old_pin = "sha256:42d073cdeaf7fa7940c5e822b05213267ec1d0064faaaad092f21d264b76a2b1"
        reg_patch, pol_patch = patch_path(registry), patch_path(policy)

        def manifest_flip(root):
            text = (root / OUT).read_text()
            sha = ROW.findall(text)[0][0]
            (root / OUT).write_text(text.replace(sha, ("0" if sha[0] != "0" else "1")
                                                 + sha[1:], 1))

        def add_record(subject):
            def mutate(root):
                (root / subject.record).write_text("# synthetic superseding record\n")
            return mutate

        def extra_key(root):
            _edit(reg_patch, f'+        "signedBy": "{SIGNED_BY}"',
                  f'+        "signedBy": "{SIGNED_BY}",\n+        "note": "x"')(root)
            _edit(reg_patch, "@@ -17,8 +17,8 @@", "@@ -17,8 +17,9 @@")(root)

        def version_only(root):
            # The registry patch moves `version` and leaves `signedBy` as
            # context: one changed line, which only the count predicate sees.
            path = root / reg_patch
            lines = path.read_text().split("\n")
            minus_s = next(i for i, l in enumerate(lines) if l.startswith('-        "signedBy"'))
            plus_v = next(i for i, l in enumerate(lines) if l.startswith('+        "version"'))
            plus_s = next(i for i, l in enumerate(lines) if l.startswith('+        "signedBy"'))
            assert (minus_s, plus_v, plus_s) == (minus_s, minus_s + 1, minus_s + 2)
            kept = " " + lines[minus_s][1:]
            lines[minus_s:plus_s + 1] = [lines[plus_v], kept]
            path.write_text("\n".join(lines))

        mutants = (
            # name, mutation, expected finding fragment
            ("registry subject drift", _edit(
                registry.path, '"schemaVersion": 1', '"schemaVersion": 2'),
             "not the argument"),
            ("policy subject drift", _edit(
                policy.path, '"policyVersion"', '"policyVersion" '), "not the argument"),
            ("predecessor record names another digest", _edit(
                policy.predecessor, "Exact digest (SHA-256): `d", "Exact digest (SHA-256): `e"),
             "not the argument"),
            ("corrupted patch context", _edit(
                reg_patch, ' "id": "polaris-project-wide-butlers-model"',
                ' "id": "polaris-project-wide-butlers-modelx"'), "does not apply"),
            ("patch pins the superseded digest", _edit(
                pol_patch, f'+    "version": "sha256:{spec_digest}"',
                f'+    "version": "{old_pin}"'), "not the signed spec.md row"),
            ("patch pins an unsigned digest", _edit(
                reg_patch, f'+        "version": "sha256:{spec_digest}"',
                '+        "version": "sha256:' + "ab" * 32 + '"'),
             "not the signed spec.md row"),
            ("signedBy names another tag", _edit(
                pol_patch, SIGNING_TAG, "pwb-readability-successor-v0.9"),
             "signedBy does not name"),
            ("contract id changed", _edit(
                reg_patch, '\n         "id": "polaris-project-wide-butlers-model",',
                '\n-        "id": "polaris-project-wide-butlers-model",'
                '\n+        "id": "polaris-project-wide-butlers-other",'),
             "governingBehaviorContract.id is"),
            ("an extra contract key", extra_key, "keys are"),
            ("a second field changed outside the contract", _edit(
                pol_patch, '\n   "accessBoundary": {\n',
                '\n-  "accessBoundary": {\n+  "accessBoundaries": {\n'),
             "more than governingBehaviorContract"),
            # Round-1 finding 1: JSON-equal, so only the two-line predicate sees it.
            ("a whitespace-only line change", _edit(
                pol_patch, '\n     "id": "polaris-project-wide-butlers-model",',
                '\n-    "id": "polaris-project-wide-butlers-model",'
                '\n+    "id":  "polaris-project-wide-butlers-model",'),
             "exactly the two"),
            ("a patch that moves only the version line", version_only,
             "exactly the two"),
            ("signing record missing", lambda root: (root / SIGNING_RECORD).unlink(),
             "is missing or does not name"),
            ("signing manifest drops the spec row", _edit(
                SIGNING_MANIFEST, PWB_SPEC.as_posix(), PWB_SPEC.as_posix() + ".x"),
             "exactly one row"),
            ("current spec.md moved past the pin (stale package)", _edit(
                PWB_SPEC, "### Requirement: PWB-REQ-001", "### Requirement:  PWB-REQ-001"),
             "is not the current"),
            ("manifest digest flipped", manifest_flip, "exact regeneration"),
            ("manifest path mutated", _edit(OUT, "policies/", "policy/"),
             "row population"),
            ("manifest missing", lambda root: (root / OUT).unlink(), "manifest missing"),
            ("a third patch under proposed/", lambda root: (
                root / PROPOSED / "EXTRA.patch").write_text(""), "proposed/ holds"),
            ("a patch missing", lambda root: (root / pol_patch).unlink(), "missing patch"),
            ("registry act recorded but subject unapplied", add_record(registry),
             "reverse-apply"),
            ("policy act recorded but subject unapplied", add_record(policy),
             "reverse-apply"),
        )
        for name, mutate, expect in mutants:
            tree = pathlib.Path(tmp) / re.sub(r"\W+", "-", name)
            shutil.copytree(clean, tree)
            mutate(tree)
            got = check(tree)
            results.append((f"fails: {name}", any(expect in f for f in got)))
            if not any(expect in f for f in got):
                print(f"  ({name}: got {got or 'nothing'})")

        # A patch that changes nothing: proposed bytes equal to the base.
        base = (clean / registry.path).read_bytes()
        results.append(("fails: a patch that changes nothing", any(
            "changes nothing" in f
            for f in structure_findings(clean, registry, base, base))))

        # Invalid JSON in the proposed bytes fails the structural claim.
        results.append(("fails: proposed bytes that are not JSON", any(
            "not valid JSON" in f for f in structure_findings(
                clean, policy, (clean / policy.path).read_bytes(), b"{"))))

        # Post-act mode: apply both, add both records, and the check passes;
        # then drift the applied subject and it fails.
        tree = pathlib.Path(tmp) / "performed"
        shutil.copytree(clean, tree)
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            code = apply(True, ("registry", "policy"), tree)
        for subject in SUBJECTS:
            add_record(subject)(tree)
        results.append(("post-act: applied subjects with both records verify",
                        code == 0 and check(tree) == []))
        _edit(PWB_SPEC, "### Requirement: PWB-REQ-001",
              "### Requirement:  PWB-REQ-001")(tree)
        results.append(("post-act: a later spec.md change leaves the performed "
                        "package verifying (R6 reports the new pin gap)", check(tree) == []))
        _edit(registry.path, '"schemaVersion": 1', '"schemaVersion": 2')(tree)
        results.append(("post-act: drift in an applied subject fails",
                        any("registry" in f for f in check(tree))))
        with contextlib.redirect_stdout(io.StringIO()):
            refused = apply(False, ("registry",), clean)
        results.append(("--apply without --at-adoption refuses", refused == 2))

    failing = sum(0 if ok else 1 for _n, ok in results)
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"{len(results)} fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--apply", choices=("registry", "policy", "both"))
    mode.add_argument("--diff", action="store_true", help="print the proposed diffs")
    mode.add_argument("--manifest-digest", action="store_true",
                      help="print the SHA-256 a review head's `Manifest SHA-256:` carries")
    mode.add_argument("--write", action="store_true",
                      help="regenerate the manifest (changes both act arguments)")
    parser.add_argument("--at-adoption", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.diff:
        for subject in SUBJECTS:
            sys.stdout.write((ROOT / patch_path(subject)).read_text())
        return 0
    if args.manifest_digest:
        print(sha256(read(ROOT, OUT)))
        return 0
    if args.apply:
        keys = ("registry", "policy") if args.apply == "both" else (args.apply,)
        return apply(args.at_adoption, keys)
    if args.check:
        findings = check()
        if findings:
            print("PWB behaviour-contract re-pin package does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        states = ", ".join(
            f"{s.key}: {'performed, subject = proposed bytes' if performed(ROOT, s) else 'patch applies to the act-in-force bytes'}"
            for s in SUBJECTS)
        print(f"PWB behaviour-contract re-pin manifest matches its 2 proposed subjects "
              f"(pin = the {SIGNING_TAG} spec.md row); {states}")
        return 0
    if not args.write:
        print("refusing: regenerating the manifest changes both act arguments; "
              "pass --write")
        return 2
    proposed = {s.key: proposed_bytes(ROOT, s) for s in SUBJECTS}
    (ROOT / OUT).write_text(render(proposed))
    print(f"wrote {OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
