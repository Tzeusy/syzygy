#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Record/check the owner's explicit adoption of the reviewed understanding amendment."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHANGE = "openspec/changes/polaris-manifesto-understanding-amendment/"
NAMES = ".openspec.yaml COVERAGE.md GOVERNING-DEPENDENCIES.md SYNTHESIS-MAP.json design.md proposal.md specs/polaris-generation/spec.md tasks.md".split()
REVIEW = "docs/reviews/R-POLARIS-UNDERSTANDING-FORMAL-SPEC-2026-09-13-RAW.md"
REVIEW_SHA = "36c93a0b8777629c854adf126a2927449bd557589f6107647668e449fe42785a"
MANIFEST = "docs/evidence/polaris-understanding-adoption-manifest-2026-09-13.json"
ACT = ".syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md"
AGGREGATE = ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
LABEL = "ADOPT POLARIS UNDERSTANDING AMENDMENT"
MARKER = "POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION"


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


def canonical(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def current_subject(root):
    raw = read(root, REVIEW)
    if digest(raw) != REVIEW_SHA:
        raise ValueError("review changed")
    bindings = re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`$", raw.decode(), re.M)
    if len(bindings) != 12 or len(dict(bindings)) != 12:
        raise ValueError("review binding population")
    for path, expected in bindings:
        if digest(read(root, path)) != expected:
            raise ValueError("reviewed bytes changed: " + path)
    population = sorted(CHANGE + name for name in NAMES)
    actual = sorted(p.relative_to(root).as_posix() for p in (root / CHANGE).rglob("*") if p.is_file())
    if population != actual or not set(population) <= dict(bindings).keys():
        raise ValueError("amendment population changed")
    return {"version": 1, "project": "project:syzygy",
            "artifact": "specification:syzygy:polaris-generation:understanding-amendment",
            "artifacts": [{"path": path, "sha256": digest(read(root, path)),
                           "role": "behavior-specification" if path.endswith("/spec.md") else "amendment-support"} for path in population],
            "review": {"path": REVIEW, "sha256": REVIEW_SHA},
            "reviewed_context": [{"path": path, "sha256": sha} for path, sha in bindings if path not in population],
            "modified_requirements": ["REQ-polaris-generation-" + n for n in ["002", "004", "006", "009", "012", "014", "019"]],
            "added_requirements": ["REQ-polaris-generation-030", "REQ-polaris-generation-031"],
            "scope": "Specification amendment adoption only; no implementation extension or new source, provider, write, deployment or release permission."}


def validate(root):
    expected = canonical(current_subject(root))
    if read(root, MANIFEST) != expected:
        raise ValueError("adoption manifest mismatch")
    return digest(expected)


def body(sha, instant):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", instant):
        raise ValueError("invalid act instant")
    datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
    return f"""# Polaris understanding specification amendment adoption

Owner: Tzeusy

Act instant: {instant}

Project identity: project:syzygy

Artifact identity: specification:syzygy:polaris-generation:understanding-amendment

Act type: adopt specification amendment

Provenance: owner-adopted (bootstrap, uncorrelated)

A1 audit-record identity: explicitly absent

Owner instruction, recorded verbatim: “Adopt it”

The instruction refers to the reviewed formal amendment offered immediately
before it. The manifest below binds its exact eight-file subject and retained
review/context hashes. This recorder-generated binding is not presented as a
longer phrase typed by the owner:

{LABEL}: {sha}

Manifest: {MANIFEST}

Scope: adopt the specification amendment at the manifest's exact bytes.
REQ-polaris-generation-002, 004, 006, 009, 012, 014 and 019 take their full
amended clauses and preserved scenarios; 030 and 031 are added. The other 22
predecessor requirements remain unchanged. Effective composition is 31
requirements and 177 scenarios, not an implementation completion verdict.

Supersession relationship: partial specification amendment to the subject of
POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md. Only the seven named requirement
blocks are superseded by their extended blocks; the predecessor remains in force
for its unchanged requirements and is preserved byte-for-byte.

Revocation relationship: none. Existing implementation and applicability acts
retain their own exact scopes. This act grants no implementation extension,
source/provider/content permission, write consent, deployment or release.

Adoption leaves the reviewed files and their candidate-era banners unchanged.
The act record determines effective status. This is bootstrap owner provenance,
not independent authorship verification, runtime evidence or product readiness.
"""


def block(content):
    return f"<!-- {MARKER}:BEGIN -->\n{content}<!-- {MARKER}:END -->\n"


def check(root):
    sha = validate(root)
    actual = read(root, ACT).decode()
    match = re.search(r"^Act instant: (.+)$", actual, re.M)
    if not match or actual != body(sha, match.group(1)):
        raise ValueError("dedicated act mismatch")
    aggregate = read(root, AGGREGATE).decode()
    if any(aggregate.count(f"<!-- {MARKER}:{suffix} -->") != 1 for suffix in ["BEGIN", "END"]) or aggregate.count(block(actual)) != 1:
        raise ValueError("aggregate act missing, changed or duplicated")


def record(root, instruction, instant):
    if instruction != "Adopt it":
        raise ValueError("unexpected owner instruction")
    sha = validate(root)
    content = body(sha, instant)
    aggregate = read(root, AGGREGATE)
    if (root / ACT).exists() or MARKER.encode() in aggregate:
        raise ValueError("adoption already recorded or partial")
    validate(root)
    with (root / ACT).open("x") as stream:
        stream.write(content)
    with (root / AGGREGATE).open("ab") as stream:
        stream.write(("\n" + block(content)).encode())
    check(root)


def selftest():
    bindings = re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`$", read(ROOT, REVIEW).decode(), re.M)
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for rel in [REVIEW, *[p for p, _ in bindings]]:
            target = root / rel; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(read(ROOT, rel))
        (root / MANIFEST).parent.mkdir(parents=True, exist_ok=True)
        (root / MANIFEST).write_bytes(canonical(current_subject(root)))
        (root / AGGREGATE).parent.mkdir(parents=True, exist_ok=True)
        (root / AGGREGATE).write_text("# Synthetic aggregate\n")
        def refuses(fn):
            try: fn()
            except ValueError: return
            raise AssertionError("mutation accepted")
        target = root / (CHANGE + "design.md"); saved = target.read_bytes()
        target.write_bytes(saved + b"changed"); refuses(lambda: validate(root)); target.write_bytes(saved)
        extra = root / (CHANGE + "extra.md"); extra.write_text("extra")
        refuses(lambda: validate(root)); extra.unlink()
        refuses(lambda: record(root, "continue", "2026-09-13T00:00:00Z"))
        refuses(lambda: record(root, "Adopt it", "2026-02-30T00:00:00Z"))
        record(root, "Adopt it", "2026-09-13T00:00:00Z")
        refuses(lambda: record(root, "Adopt it", "2026-09-13T00:00:00Z"))
        with (root / AGGREGATE).open("a") as stream: stream.write("\nLater unrelated record.\n")
        check(root)
        with (root / AGGREGATE).open("a") as stream: stream.write(block(read(root, ACT).decode()))
        refuses(lambda: check(root))
    print("PASS subject drift, extra file, wrong instruction, invalid instant, duplicate act, non-tail readback and duplicated aggregate")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    for action in ["prepare", "record", "check", "selftest"]: mode.add_argument("--" + action, action="store_true")
    parser.add_argument("--owner-instruction"); parser.add_argument("--instant")
    args = parser.parse_args()
    if args.selftest: selftest()
    elif args.prepare:
        with (ROOT / MANIFEST).open("xb") as stream: stream.write(canonical(current_subject(ROOT)))
        print("Prepared exact reviewed amendment manifest; no act recorded")
    elif args.record:
        record(ROOT, args.owner_instruction, args.instant)
        print("Recorded explicit owner adoption; bootstrap provenance; A1 absent")
    else:
        check(ROOT); print("PASS exact amendment and dedicated/aggregate adoption records")

if __name__ == "__main__":
    main()
