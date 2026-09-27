#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Record/check the owner's adoption of the contract readability restyle.

The act is the second link of `CONTRACT_SUCCESSOR_CHAIN` in
`check_governance.py`. Its argument is the sha256 of the package manifest
`candidates/contract-readability-restyle/CONTRACT-AMENDMENT-MANIFEST.txt`,
built and verified by `scripts/build_contract_readability_restyle.py`.

`--record --instruction "<owner words verbatim>"` writes the dedicated act
record and appends one marked section to `ACCEPTANCE-ACT-RECORD.md`. Each
carries the binding line `ADOPT CONTRACT READABILITY RESTYLE: <sha256>` once,
as the only line that contains the label (CG-7h requires exactly one bare
full-line occurrence per record). Recording refuses unless the package
verifies: either the patches still produce the manifest rows over both
identical mirrors (record, then `--apply --at-adoption` in the same change),
or both mirrors already equal every row (applied first).

`--check` verifies the dedicated record regenerates exactly and that the
aggregate holds exactly one copy of the marked block; it reports "not
performed" and exits 0 when neither record exists, and fails on a partial
record. `--selftest` runs fixtures in a temporary directory.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (".syzygy/governance/contracts/candidates/contract-readability-restyle/"
            "CONTRACT-AMENDMENT-MANIFEST.txt")
ACT = ".syzygy/governance/decisions/CONTRACT-READABILITY-RESTYLE-ADOPTION-ACT.md"
AGGREGATE = ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
BUILDER = "scripts/build_contract_readability_restyle.py"
LABEL = "ADOPT CONTRACT READABILITY RESTYLE"
MARKER = "CONTRACT-READABILITY-RESTYLE-ADOPTION"
INSTANT = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(root, rel):
    path = Path(rel)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("invalid path")
    target = root / path
    if any(p.is_symlink() for p in [target, *target.parents] if p != root.parent):
        raise ValueError("symlinked subject")
    return target.read_bytes()


def builder():
    spec = importlib.util.spec_from_file_location("restyle_builder", ROOT / BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(root, verify_package=True):
    """The manifest's digest, once the package verifies at `root`."""
    if not (root / MANIFEST).is_file():
        raise ValueError(f"manifest absent: {MANIFEST}")
    if verify_package:
        package = builder()
        try:
            findings = [] if package.applied(root) else package.check(root)
        except OSError as error:
            raise ValueError(f"package inputs unreadable: {error}") from error
        if findings:
            raise ValueError("package does not verify: " + "; ".join(findings[:3]))
    return digest(read(root, MANIFEST))


def validate_instruction(instruction):
    if not instruction or not instruction.strip():
        raise ValueError("owner instruction is empty")
    if "\n" in instruction or "\r" in instruction:
        raise ValueError("owner instruction spans lines; record it on one line "
                         "verbatim or amend this recorder, never reflow it")
    if LABEL in instruction or MARKER in instruction or "<!--" in instruction:
        raise ValueError("owner instruction carries the act label or a record marker")


def body(sha, instant, instruction):
    if not INSTANT.fullmatch(instant):
        raise ValueError("invalid act instant")
    datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
    validate_instruction(instruction)
    return f"""# Contract readability restyle adoption

Owner: Tzeusy

Act instant: {instant}

Project identity: project:syzygy

Artifact identity: contract:syzygy:rfc-0001-0009:readability-restyle

Act type: adopt contract amendment (successor to the general trusted-bootstrap contract manifest)

Provenance: owner-adopted (bootstrap, uncorrelated)

A1 audit-record identity: explicitly absent

Owner instruction, recorded verbatim: “{instruction}”

The instruction refers to the reviewed restyle package offered immediately
before it. The manifest below binds the exact post-restyle bytes of 29 of the
30 accepted RFC 0001-0009 modules, every one except
rfcs/RFC-0007/rendering-and-surface.md. This recorder-generated binding is
not presented as a longer phrase typed by the owner:

{LABEL}: {sha}

Manifest: {MANIFEST}

Scope: readability restyle only. Clause identities, clause leads, front
matter and headings are unchanged by construction (the package builder
verifies all three); the installed and candidate mirrors take the same bytes.

Supersession relationship: link 2 of the contract successor chain. For its 29
paths it supersedes the current-byte rows of the general trusted-bootstrap
contract manifest, and of any earlier performed chain link, which remain
preserved as act-time history. RFC-0007's rendering module stays bound where
it was.

Revocation relationship: none. This act grants no implementation, source,
provider, write, deployment or release permission.

This is bootstrap owner provenance, not independent authorship verification,
runtime evidence or product readiness.
"""


def block(content):
    return f"<!-- {MARKER}:BEGIN -->\n{content}<!-- {MARKER}:END -->\n"


def parse(actual):
    instant = re.search(r"^Act instant: (.+)$", actual, re.M)
    instruction = re.search(r"^Owner instruction, recorded verbatim: “(.*)”$", actual, re.M)
    if not instant or not instruction:
        raise ValueError("dedicated act unparseable")
    return instant.group(1), instruction.group(1)


def check(root, verify_package=False):
    """Returns False when nothing is recorded; raises on any partial or drifted record."""
    act_exists = (root / ACT).exists()
    aggregate = read(root, AGGREGATE).decode()
    if not act_exists and MARKER not in aggregate and LABEL not in aggregate:
        return False
    if not act_exists:
        raise ValueError("aggregate carries the act but the dedicated record is absent")
    sha = validate(root, verify_package=verify_package)
    actual = read(root, ACT).decode()
    if actual != body(sha, *parse(actual)):
        raise ValueError("dedicated act mismatch")
    for text, where in ((actual, ACT), (aggregate, AGGREGATE)):
        lines = [line for line in text.splitlines() if LABEL in line]
        if lines != [f"{LABEL}: {sha}"]:
            raise ValueError(f"{where}: expected exactly one binding line")
    if (any(aggregate.count(f"<!-- {MARKER}:{suffix} -->") != 1
            for suffix in ["BEGIN", "END"])
            or aggregate.count(block(actual)) != 1):
        raise ValueError("aggregate act missing, changed or duplicated")
    return True


def record(root, instruction, instant, verify_package=True):
    validate_instruction(instruction)
    sha = validate(root, verify_package=verify_package)
    content = body(sha, instant, instruction)
    aggregate = read(root, AGGREGATE)
    if (root / ACT).exists() or MARKER.encode() in aggregate or LABEL.encode() in aggregate:
        raise ValueError("adoption already recorded or partial")
    with (root / ACT).open("x", encoding="utf-8") as stream:
        stream.write(content)
    with (root / AGGREGATE).open("ab") as stream:
        stream.write(("\n" + block(content)).encode())
    if not check(root, verify_package=False):
        raise ValueError("record did not read back")


def selftest():
    results = []

    def refuses(label, fn):
        try:
            fn()
        except ValueError:
            results.append((label, True))
            return
        results.append((label, False))

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / AGGREGATE).parent.mkdir(parents=True, exist_ok=True)
        (root / AGGREGATE).write_text("# Synthetic aggregate\n")
        (root / MANIFEST).parent.mkdir(parents=True, exist_ok=True)
        manifest = "# synthetic\n" + "".join(
            f"{digest(str(i).encode())}  rfcs/RFC-{i:04d}.md\n" for i in range(29))
        (root / MANIFEST).write_text(manifest)
        sha = digest(manifest.encode())
        instant = "2026-09-28T00:00:00Z"
        words = "Adopt the contract readability restyle"
        results.append(("nothing recorded reads as not performed",
                        check(root) is False))
        refuses("empty instruction", lambda: record(root, "  ", instant, False))
        refuses("multi-line instruction", lambda: record(root, "a\nb", instant, False))
        refuses("instruction carrying the label",
                lambda: record(root, f"{LABEL}: x", instant, False))
        refuses("invalid instant", lambda: record(root, words, "2026-02-30T00:00:00Z", False))
        manifest_file = root / MANIFEST
        manifest_file.rename(root / "moved")
        refuses("absent manifest", lambda: record(root, words, instant, False))
        (root / "moved").rename(manifest_file)
        refuses("unverified package refused by the builder",
                lambda: record(root, words, instant, True))
        record(root, words, instant, verify_package=False)
        act = (root / ACT).read_text()
        results.append(("dedicated record binds the manifest digest on one line",
                        [l for l in act.splitlines() if LABEL in l] == [f"{LABEL}: {sha}"]))
        results.append(("provenance, A1 absence and verbatim instruction recorded",
                        "Provenance: owner-adopted (bootstrap, uncorrelated)" in act
                        and "A1 audit-record identity: explicitly absent" in act
                        and f"“{words}”" in act))
        results.append(("recorded act checks", check(root) is True))
        refuses("second record refused", lambda: record(root, words, instant, False))
        with (root / AGGREGATE).open("a") as stream:
            stream.write("\nLater unrelated record.\n")
        results.append(("non-tail readback checks", check(root) is True))
        saved = manifest_file.read_bytes()
        manifest_file.write_bytes(saved + b"# changed\n")
        refuses("manifest drift after recording", lambda: check(root))
        manifest_file.write_bytes(saved)
        saved_aggregate = (root / AGGREGATE).read_bytes()
        with (root / AGGREGATE).open("a") as stream:
            stream.write(block(act))
        refuses("duplicated aggregate block", lambda: check(root))
        (root / AGGREGATE).write_bytes(saved_aggregate)
        with (root / AGGREGATE).open("a") as stream:
            stream.write(f"\n{LABEL}: {sha}\n")
        refuses("second aggregate binding line", lambda: check(root))
        (root / AGGREGATE).write_bytes(saved_aggregate)
        (root / ACT).write_text(act.replace(words, words + "!"))
        refuses("edited dedicated record", lambda: check(root))
        (root / ACT).unlink()
        refuses("aggregate without dedicated record", lambda: check(root))
    failing = [label for label, ok in results if not ok]
    for label, ok in results:
        print(f"  {'pass' if ok else 'FAIL'}  {label}")
    print(f"{len(results)} fixtures, {len(failing)} failing")
    return 1 if failing else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    for action in ["record", "check", "selftest"]:
        mode.add_argument("--" + action, action="store_true")
    parser.add_argument("--instruction", help="the owner's words, verbatim")
    parser.add_argument("--instant", help="UTC act instant (default: now)")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    if args.record:
        instant = args.instant or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        record(ROOT, args.instruction, instant)
        print("Recorded owner adoption of the contract readability restyle; "
              "bootstrap provenance; A1 absent. Next: "
              f"python3 {BUILDER} --apply --at-adoption")
        return 0
    if check(ROOT):
        print("PASS exact restyle manifest and dedicated/aggregate adoption records")
    else:
        print("contract readability restyle not performed: no dedicated or aggregate record")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as error:
        print(f"FAIL {error}")
        sys.exit(1)
