#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Prepare, check, or record an exact-content owner transaction; never infer consent."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT = "project:syzygy"
PACKAGE = "package:syzygy:polaris-manifesto-generation"
BASELINE = "f4589e26aed9886a5776e5ac7a1c4fad4627fd26"
CHANGE = "openspec/changes/polaris-manifesto-generation/"
NAMES = (".openspec.yaml ADAPTER-DECLARATIONS.md APPLICABILITY-DECISIONS.md "
         "ASSET-CONTRACT.md CAPABILITY-COVERAGE.md DESIGN-ACCEPTANCE.md "
         "EFFECT-HOST-DESIGN.md ENTRY-AND-WALKTHROUGH.md EXECUTION-PHASES.md "
         "GOVERNING-DEPENDENCIES.md INTERFACES.md NAVIGATION-CONTRACT.md OWNER-FLOW.md "
         "SCHEMA-CONTRACT.md SECURITY-CONTRACT.md SOURCE-POLICY.md WORK-STATE-CONTRACT.md "
         "design.md proposal.md specs/polaris-generation/spec.md tasks.md").split()
POPULATION = sorted([CHANGE + n for n in NAMES] + [
    "docs/design/POLARIS-GENERATOR-DELIVERY.md", "docs/design/POLARIS-GENERATOR-OWNER-PACKET.md"])
REGISTERED_OFFER = "docs/evidence/polaris-generator-approval-offer-2026-09-12.json"
SUBJECT = "docs/evidence/polaris-generator-review-subject-2026-09-12.json"
DECISIONS = ".syzygy/governance/decisions/"
AGGREGATE = DECISIONS + "ACCEPTANCE-ACT-RECORD.md"
LABEL = "ADOPT POLARIS GENERATOR SPECIFICATION, SCOPED APPLICABILITY AND IMPLEMENTATION"
EFFECTS = {
    "SPECIFICATION-ADOPTION": "Adopt the exact specification-role artifacts in the bound offer.",
    "APPLICABILITY": "Adopt GNA-1, GNA-2 and GNA-3 only within APPLICABILITY-DECISIONS.md's exact scope, and the exact conditional coverage references in the bound offer. No blanket waiver; conditional obligations remain attached to future enablement.",
    "IMPLEMENTATION-AUTHORIZATION": "Authorize the full EXECUTION-PHASES.md implementation goal, including protected effect host, complete owner experience, two-project and changed-source proof obligations. Phase A alone is not completion. Real-project reads, provider egress and destination writes remain separately admitted; no effect, production release, broad remote access or observed-project code execution is authorized by this act.",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read(root: Path, rel: str) -> bytes:
    path = Path(rel)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != rel:
        raise ValueError("non-canonical relative path")
    target = root / path
    if any(p.is_symlink() for p in [target, *target.parents] if p != root.parent):
        raise ValueError("symlinked input")
    return target.read_bytes()


def pin(root: Path, rel: str) -> dict:
    return {"path": rel, "sha256": sha(read(root, rel))}


def canonical(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def governing(root: Path, baseline: str = BASELINE) -> list[dict]:
    result = subprocess.run(["git", "ls-tree", "-rz", baseline, "--", ".syzygy", "openspec"], cwd=root, check=True, capture_output=True)
    rows = []
    for row in result.stdout.split(b"\0"):
        if not row:
            continue
        meta, name = row.split(b"\t", 1)
        mode, kind, oid = meta.split()
        rel = name.decode()
        if kind != b"blob" or mode == b"120000":
            raise ValueError("unexpected governing tree entry")
        content = subprocess.run(["git", "cat-file", "blob", oid.decode()], cwd=root, check=True, capture_output=True).stdout
        current = read(root, rel)
        if rel == AGGREGATE and current.startswith(content):
            suffix = current[len(content):].decode()
            for kind in EFFECTS:
                pattern = re.escape(f"<!-- POLARIS-GENERATOR-{kind}:BEGIN -->") + r"[\s\S]*?" + re.escape(f"<!-- POLARIS-GENERATOR-{kind}:END -->")
                suffix = re.sub(pattern, "", suffix, count=1)
            if suffix.strip():
                raise ValueError("unrecognized governing aggregate drift")
        elif current != content:
            raise ValueError("governing baseline drift: " + rel)
        rows.append({"path": rel, "sha256": sha(content)})
    if not rows:
        raise ValueError("empty governing baseline")
    baseline_paths = {row["path"] for row in rows}
    allowed = baseline_paths | {CHANGE + name for name in NAMES} | {
        DECISIONS + f"POLARIS-GENERATOR-{kind}-ACT.md" for kind in EFFECTS
    }
    current_paths = set()
    for home in (".syzygy", "openspec"):
        for path in (root / home).rglob("*"):
            rel = path.relative_to(root).as_posix()
            # These two declared runtime homes carry no governing authority.
            if rel in (".syzygy/cache", ".syzygy/local") or rel.startswith((".syzygy/cache/", ".syzygy/local/")):
                continue
            if path.is_symlink():
                raise ValueError("symlink in governed population: " + rel)
            if not path.is_file():
                continue
            # Only Python's bytecode artifacts are exempt, never arbitrary ignored
            # files or documents placed under a directory named __pycache__.
            if path.parent.name == "__pycache__" and re.fullmatch(r".+\.cpython-[0-9]+(?:\.opt-[0-9]+)?\.pyc", path.name):
                continue
            current_paths.add(rel)
    if current_paths - allowed or baseline_paths - current_paths:
        raise ValueError("governed path population drift: " + ", ".join(sorted((current_paths - allowed) | (baseline_paths - current_paths))))
    return rows


def sources(root: Path) -> list[dict]:
    subject = json.loads(read(root, SUBJECT))
    rows = subject["subjects"]
    if subject["baseline"] != BASELINE or sorted(r["path"] for r in rows) != POPULATION:
        raise ValueError("subject population or baseline mismatch")
    actual = sorted(p.relative_to(root).as_posix() for p in (root / CHANGE).rglob("*") if p.is_file())
    if actual != sorted(CHANGE + n for n in NAMES):
        raise ValueError("candidate directory population mismatch")
    for row in rows:
        if row != pin(root, row["path"]):
            raise ValueError("source digest mismatch: " + row["path"])
    return sorted(rows, key=lambda r: r["path"])


def prepare(root: Path, reviews: list[str], references: list[str], baseline_rows=None, owner="Tzeusy") -> dict:
    if not reviews or not references or len(set(reviews)) != len(reviews) or len(set(references)) != len(references):
        raise ValueError("unique review evidence and conditional coverage references required")
    refs = []
    for ref in sorted(references):
        path, marker = ref.split("#", 1)
        body = read(root, path).decode()
        if marker.startswith("json:"):
            pointer = marker[5:]
            if not pointer.startswith("/"):
                raise ValueError("JSON pointer must address a selected value")
            selected = json.loads(body)
            for token in pointer[1:].split("/"):
                if re.search(r"~(?![01])", token):
                    raise ValueError("invalid JSON pointer escape")
                key = token.replace("~1", "/").replace("~0", "~")
                if isinstance(selected, list):
                    if not re.fullmatch(r"0|[1-9][0-9]*", key):
                        raise ValueError("invalid JSON array index")
                    try:
                        selected = selected[int(key)]
                    except IndexError as error:
                        raise ValueError("JSON pointer index absent") from error
                elif isinstance(selected, dict) and key in selected:
                    selected = selected[key]
                else:
                    raise ValueError("JSON pointer does not resolve")
            selected_digest = sha(canonical(selected))
        else:
            if not marker or body.count(marker) != 1:
                raise ValueError("conditional literal reference must occur exactly once")
            selected_digest = sha(marker.encode())
        refs.append({**pin(root, path), "reference": marker, "selected_sha256": selected_digest})
    return {"version": 1, "project": PROJECT, "package": PACKAGE, "baseline": BASELINE, "owner": owner, "subject": pin(root, SUBJECT),
            "sources": [{**row, "roles": (["specification"] if row["path"].startswith(CHANGE) else ["implementation-guidance"]) + (["applicability"] if row["path"].endswith("APPLICABILITY-DECISIONS.md") else [])} for row in sources(root)],
            "governing": governing(root) if baseline_rows is None else baseline_rows,
            "reviews": [pin(root, p) for p in sorted(reviews)], "conditional_references": refs,
            "acts": EFFECTS, "provenance": "owner-adopted (bootstrap, uncorrelated)", "A1": "explicitly absent"}


def validate(root: Path, offer: Path, argument: str, baseline_rows=None, owner="Tzeusy") -> dict:
    data = offer.read_bytes()
    if sha(data) != argument:
        raise ValueError("owner argument does not match exact offer bytes")
    value = json.loads(data)
    expected = prepare(root, [r["path"] for r in value["reviews"]], [r["path"] + "#" + r["reference"] for r in value["conditional_references"]], baseline_rows, owner)
    if value != expected or data != canonical(value):
        raise ValueError("offer changed or no longer matches current inputs")
    return value


def records(argument: str, instant: str, owner: str) -> dict[str, str]:
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", instant):
        raise ValueError("act instant requires exact UTC YYYY-MM-DDTHH:MM:SSZ")
    parsed = datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
    if not re.fullmatch(r"[A-Za-z0-9 _.-]+", owner):
        raise ValueError("invalid owner")
    if not re.fullmatch(r"[a-f0-9]{64}", argument):
        raise ValueError("invalid offer digest")
    return {kind: f"""# Polaris generator {kind.lower()} owner act

Date: {parsed.date().isoformat()}

Act instant: {instant}

Owner: {owner}

Project identity: {PROJECT}

Artifact/package identity: {PACKAGE}

Act identity: act:syzygy:polaris-generator:{kind.lower()}:{argument}

Act type: {kind.lower()}

Supersession relationship: none; new act, no predecessor.

Revocation relationship: none; this act revokes no prior act.

Provenance state: owner-adopted (bootstrap, uncorrelated)

A1 audit-record identity: explicitly absent

Exact offer SHA-256: {argument}

Scope references: the exact offer's /sources artifact-role manifest, /acts/{kind},
/project and /package identities, /governing baseline, /reviews evidence, and
/conditional_references selected-value digests. Applicability further binds the
APPLICABILITY-DECISIONS.md source row; implementation binds EXECUTION-PHASES.md.

Exact transaction phrase:

```text
{LABEL}: {argument}
```

The SHA-256 argument binds the complete immutable offer, including source, role,
governing baseline, review and conditional-reference digests. It asserts no
committed-source identity.

{effect}

This record does not claim independently verified authorship, review verdict,
successful effects or implementation completion.
""" for kind, effect in EFFECTS.items()}


def block(kind: str, body: str) -> str:
    return f"<!-- POLARIS-GENERATOR-{kind}:BEGIN -->\n{body}<!-- POLARIS-GENERATOR-{kind}:END -->\n"


def check_records(root: Path, expected: dict[str, str]) -> None:
    aggregate = read(root, AGGREGATE).decode()
    for kind, body in expected.items():
        if read(root, DECISIONS + f"POLARIS-GENERATOR-{kind}-ACT.md").decode() != body:
            raise ValueError("dedicated act mismatch")
        for suffix in ("BEGIN", "END"):
            if aggregate.count(f"<!-- POLARIS-GENERATOR-{kind}:{suffix} -->") != 1:
                raise ValueError("duplicate or missing aggregate act marker")
        if aggregate.count(block(kind, body)) != 1:
            raise ValueError("aggregate act mismatch")


def require_registered_offer(root: Path, offer: Path) -> None:
    if offer.absolute() != (root / REGISTERED_OFFER).absolute():
        raise ValueError("scratch offer is not recordable; use registered offer path")
    read(root, REGISTERED_OFFER)  # Reject symlinks as well as alternative paths.


def record(root: Path, offer: Path, phrase: str, instant: str, owner: str, baseline_rows=None, expected_owner="Tzeusy") -> None:
    require_registered_offer(root, offer)
    prefix = LABEL + ": "
    if not phrase.startswith(prefix):
        raise ValueError("wrong owner phrase")
    argument = phrase[len(prefix):]
    value = validate(root, offer, argument, baseline_rows, expected_owner)
    if owner != value["owner"]:
        raise ValueError("owner differs from immutable offer")
    expected = records(argument, instant, owner)
    aggregate = read(root, AGGREGATE)
    for kind in expected:
        if (root / (DECISIONS + f"POLARIS-GENERATOR-{kind}-ACT.md")).exists() or f"POLARIS-GENERATOR-{kind}".encode() in aggregate:
            raise ValueError("act already exists")
    # Revalidate exact subject immediately before the first write. Exclusive creates
    # refuse existing dedicated records; partial I/O failures require operator repair.
    validate(root, offer, argument, baseline_rows, expected_owner)
    for kind, body in expected.items():
        with (root / (DECISIONS + f"POLARIS-GENERATOR-{kind}-ACT.md")).open("x") as stream:
            stream.write(body)
    with (root / AGGREGATE).open("ab") as stream:
        stream.write(("\n" + "\n".join(block(k, b) for k, b in expected.items())).encode())
    check_records(root, expected)


def selftest() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel in POPULATION + [AGGREGATE, "review.md", "coverage.md"]:
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("synthetic conditional-row\n")
        subject = root / SUBJECT
        subject.parent.mkdir(parents=True, exist_ok=True)
        subject.write_bytes(canonical({"baseline": BASELINE, "subjects": [pin(root, p) for p in POPULATION]}))
        offer = root / REGISTERED_OFFER
        offer.write_bytes(canonical(prepare(root, ["review.md"], ["coverage.md#conditional-row"], [])))
        argument = sha(offer.read_bytes())
        def refuses(fn):
            try:
                fn()
            except (ValueError, FileNotFoundError):
                return
            raise AssertionError("invalid input accepted")
        scratch = root / "scratch-offer.json"
        scratch.write_bytes(offer.read_bytes())
        refuses(lambda: record(root, scratch, LABEL + ": " + argument, "2026-09-12T12:00:00Z", "Tzeusy", []))
        assert not (root / (DECISIONS + "POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md")).exists()
        refuses(lambda: validate(root, offer, "0" * 64, []))
        old = subject.read_bytes()
        subject.write_bytes(old + b" ")
        refuses(lambda: validate(root, offer, argument, []))
        subject.write_bytes(old)
        missing = root / POPULATION[0]
        content = missing.read_bytes()
        missing.unlink()
        refuses(lambda: validate(root, offer, argument, []))
        missing.write_bytes(content)
        extra = root / CHANGE / "extra.md"
        extra.write_text("extra")
        refuses(lambda: validate(root, offer, argument, []))
        extra.unlink()
        refuses(lambda: record(root, offer, LABEL + ": " + argument, "2026-09-12T12:00:00Z", "Other Owner", []))
        coverage = root / "coverage.json"
        coverage.write_text('{"scopes":{"disabled":{"applies":false}},"a/b":{"~key":[7]}}')
        referenced = prepare(root, ["review.md"], ["coverage.json#json:/scopes/disabled", "coverage.json#json:/a~1b/~0key/0"], [])
        assert referenced["conditional_references"][1]["selected_sha256"] == sha(canonical({"applies": False}))
        refuses(lambda: prepare(root, ["review.md"], ["coverage.json#json:/missing"], []))
        coverage.write_text("duplicate duplicate")
        refuses(lambda: prepare(root, ["review.md"], ["coverage.json#duplicate"], []))
        record(root, offer, LABEL + ": " + argument, "2026-09-12T12:00:00Z", "Tzeusy", [])
        expected = records(argument, "2026-09-12T12:00:00Z", "Tzeusy")
        refuses(lambda: records(argument, "2026-02-30T12:00:00Z", "Tzeusy"))
        refuses(lambda: records(argument, "2026-09-12", "Tzeusy"))
        act_path = root / (DECISIONS + "POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md")
        original_act = act_path.read_text()
        for old, new in [(PROJECT, "project:other"), (PACKAGE, "package:other"), ("12:00:00Z", "13:00:00Z")]:
            act_path.write_text(original_act.replace(old, new))
            refuses(lambda: check_records(root, expected))
            act_path.write_text(original_act)
        original_offer = offer.read_bytes()
        for field in ("project", "package"):
            changed = json.loads(original_offer)
            changed[field] = "other"
            offer.write_bytes(canonical(changed))
            refuses(lambda: validate(root, offer, sha(offer.read_bytes()), []))
            offer.write_bytes(original_offer)
        with (root / AGGREGATE).open("a") as stream:
            stream.write("\nUnrelated later record\n")
        check_records(root, expected)
        refuses(lambda: record(root, offer, LABEL + ": " + argument, "2026-09-12T12:00:00Z", "Tzeusy", []))
        with (root / AGGREGATE).open("a") as stream:
            stream.write(block(next(iter(expected)), next(iter(expected.values()))))
        refuses(lambda: check_records(root, expected))
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        governed = root / ".syzygy/governance/doctrine/test.md"
        governed.parent.mkdir(parents=True)
        governed.write_text("synthetic governing baseline")
        def git(*args):
            return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True).stdout.decode().strip()
        git("init", "--quiet")
        git("add", ".syzygy")
        tree = git("write-tree")
        assert len(governing(root, tree)) == 1
        governed.write_text("changed authority")
        refuses(lambda: governing(root, tree))
        governed.write_text("synthetic governing baseline")
        extra = governed.parent / "new.md"
        extra.write_text("untracked authority")
        refuses(lambda: governing(root, tree))
        git("add", ".syzygy")
        refuses(lambda: governing(root, tree))
        git("-c", "user.name=Synthetic", "-c", "user.email=synthetic@example.invalid", "commit", "-qm", "synthetic fixture")
        refuses(lambda: governing(root, tree))
        extra.unlink()
        ignored = governed.parent / "ignored.md"
        (root / ".gitignore").write_text("ignored.md\n__pycache__/\n")
        ignored.write_text("ignored authority")
        refuses(lambda: governing(root, tree))
        ignored.unlink()
        bytecode = governed.parent / "__pycache__"
        bytecode.mkdir()
        (bytecode / "helper.cpython-313.pyc").write_bytes(b"synthetic")
        assert len(governing(root, tree)) == 1
        (bytecode / "authority.md").write_text("not bytecode")
        refuses(lambda: governing(root, tree))
    print("PASS synthetic wrong argument, subject drift, omitted/extra file, owner mismatch, JSON pointer selection, ambiguous literal, duplicate act, success readback, non-tail checks and actual Git governing baseline drift; project/package/instant tamper and invalid calendar date, closed governed population and alternative offer rejection")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    for name in ("prepare", "check", "record", "selftest"):
        action.add_argument("--" + name, action="store_true")
    parser.add_argument("--offer", type=Path)
    parser.add_argument("--review", action="append", default=[])
    parser.add_argument("--coverage-reference", action="append", default=[])
    parser.add_argument("--argument")
    parser.add_argument("--owner-phrase")
    parser.add_argument("--instant", help="Exact owner-act UTC instant YYYY-MM-DDTHH:MM:SSZ; reused for recorded checks")
    parser.add_argument("--owner")
    parser.add_argument("--recorded", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return
    if args.offer is None:
        parser.error("--offer is required")
    if args.prepare:
        value = prepare(ROOT, args.review, args.coverage_reference)
        with args.offer.open("xb") as stream:
            stream.write(canonical(value))
        if args.offer.absolute() != (ROOT / REGISTERED_OFFER).absolute():
            print("SCRATCH OFFER: NOT RECORDABLE")
        print(LABEL + ": " + sha(args.offer.read_bytes()))
    elif args.check:
        value = validate(ROOT, args.offer, args.argument)
        if args.owner is not None and args.owner != value["owner"]:
            raise ValueError("owner differs from immutable offer")
        if args.recorded:
            require_registered_offer(ROOT, args.offer)
            check_records(ROOT, records(args.argument, args.instant or "", args.owner or ""))
        scratch = args.offer.absolute() != (ROOT / REGISTERED_OFFER).absolute()
        print("PASS exact offer" + (" and recorded acts" if args.recorded else "; no act asserted") + ("; SCRATCH OFFER: NOT RECORDABLE" if scratch else ""))
    else:
        record(ROOT, args.offer, args.owner_phrase or "", args.instant or "", args.owner or "")
        print("Recorded bootstrap owner transaction; A1 absent")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
