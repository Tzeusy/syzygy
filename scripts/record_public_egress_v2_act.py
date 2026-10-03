#!/usr/bin/env python3
"""Record or verify the owner's second Anthropic egress consent act (sitting row 8).

Package `contracts/candidates/public-egress-v2/`. One state-(1) owner act over
the one record named by the row of `PUBLIC-EGRESS-V2-MANIFEST.txt`: the egress
consent for `(project:syzygy, provider:anthropic)` at record version
0.2.0-candidate.1, which adds the `project-documentation` class (RFC5-14) and
the discovery stages to the first version's. The owner gives it by selecting an
option in a structured question that names the record "at the manifest row"
(packet Q5; the 2026-10-02 policy re-pin is the precedent). No phrase is typed
and no digest appears in any Markdown file of the package. This script
performs nothing by itself, and it refuses to record anything until the
package has a confirming review: `FROZEN_SUBJECT` is unset until a round
returns `CONFIRM` or a notes-only `CONFIRM WITH EXCEPTIONS`, and the frozen
digests below are then filled in by script, never by hand. It needs no git
object: the commit is provenance only.

ORDER. The act depends on sitting row 7 (the RFC5-14 amendment): until that
act is performed the class is outside the closed vocabulary, so the recorder
refuses while the row-7 record is absent from `decisions/`.

`--record KEY ARGUMENT --date D [--instant I] --question-opening Q
--selection-label L --selection-description S` requires, before anything is
written:

1. the argument is a 64-hex SHA-256 equal to the manifest's one row, the
   manifest row is exactly the builder's one record, and the builder verifies
   (current and ready: so a stale record or an undelivered stage list is
   refused);
2. the record on disk hashes to the argument;
3. the row-7 act record exists;
4. every file the review read hashes to the digest recorded below for it (the
   packet may gain one PERFORMED head), and the packet carries no 64-hex token;
5. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE>` and a verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter
   clears the bytes only when every finding is a `note` and the sibling
   `ROUND-<n>-DISPOSITIONS.md` names the raw and dispositions every finding;
6. the owner's selection (opening, label, description) is non-empty, one line
   each, and carries no 64-hex digest.

It then writes the dedicated record (with the UTC instant of recording) and
one `ACCEPTANCE-ACT-RECORD.md` section. `--check` re-derives both and counts
exactly one copy of the block. `--selftest` mutates each predicate and
requires it to fail closed.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_egress_v2 as build  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
PKG = build.PKG
MANIFEST_REL = PKG / build.MANIFEST_NAME
PACKET_REL = PKG / "OWNER-DECISION-PACKET.md"
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
SETTINGS_REL = PKG / "v2.json"
RECORD_REL = PKG / build.RECORD
#: Row 7's performed record. Until it exists the `project-documentation` class
#: is outside RFC5-14's closed vocabulary, so this act is refused.
CLASS_ACT_REL = DECISIONS / "RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md"
#: Provisional until a round returns: the confirming raw and its notes record.
CONFIRMATION_REVIEW_REL = PKG / "reviews/R-PUBLIC-EGRESS-V2-1-RAW.md"
DISPOSITION_REL = PKG / "ROUND-1-DISPOSITIONS.md"
#: The commit the confirming review read. None until a round returns CONFIRM
#: or notes-only CONFIRM WITH EXCEPTIONS; then set to that commit and the
#: round's two paths above, never hand-edited again. While None, every
#: `--record` is refused: an unreviewed package cannot be recorded.
FROZEN_SUBJECT: str | None = None
#: SHA-256 of each file the confirming review read, taken from that commit by
#: script (empty while FROZEN_SUBJECT is None). The commit is provenance only:
#: a rebase-merge leaves it unreachable from main, so validation compares the
#: presented bytes with these digests and never reads the commit (AGENTS.md:
#: bind by digest, not by commit). Keys: the manifest, packet, brief,
#: `v2.json` and the record.
FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {}
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
#: The moment of recording, UTC, whole seconds. A record that carried only a
#: date could be read as in force from the next UTC day at the earliest; the
#: instant lets a reader honour an act from the moment it was recorded.
INSTANT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RECORDED_RE = re.compile(r"^Recorded at \(UTC\): (\S+)$", re.MULTILINE)
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
ROW_RE = re.compile(r"^([0-9a-f]{64})  (\S+)$", re.MULTILINE)
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$", re.MULTILINE)
VERDICT_RE = re.compile(r"^Verdict: (.+?)\s*$")
PERFORMED_HEAD_RE = re.compile(
    rb"\A(# [^\n]+\n\n)"
    rb"> \*\*PERFORMED \d{4}-\d{2}-\d{2}\.\*\*[^\n]*\n(?:> [^\n]*\n)*\n"
)


@dataclass(frozen=True)
class Act:
    key: str
    label: str
    act_type: str
    identity_stem: str
    stem: str
    subject: pathlib.Path
    title: str
    effect: str

    @property
    def record(self) -> pathlib.Path:
        return DECISIONS / f"PUBLIC-EGRESS-V2-{self.stem}-ACT.md"


ACTS = (
    Act("egress-anthropic-v2", "CONSENT TO PUBLIC TARGET EGRESS TO ANTHROPIC VERSION 2",
        "consent-egress", "PUBLIC-EGRESS-ANTHROPIC-V2", "ANTHROPIC",
        RECORD_REL,
        "public-target egress consent to Anthropic, version 2",
        "The record is the owner's effective egress consent for the pair "
        "(`project:syzygy`, `provider:anthropic`), through the route the record "
        "names, for content read under an in-force observation consent for a "
        "repository the record lists, in the content classes it lists (those "
        "of the first version and `project-documentation`), carrying exactly "
        "the fields and stages of the record's generated table, under its "
        "retention and route conditions. It supersedes version 0.1.0-candidate.7 "
        "of the same record prospectively if an act over that version is in "
        "force (RFC5-13)."),
)
ACT_BY_KEY = {act.key: act for act in ACTS}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"public-egress-v2-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


@dataclass
class Inputs:
    """Everything validation reads, injectable for the selftest."""
    manifest: bytes
    subject: bytes
    packet: bytes
    review: str
    produced_paths: list[str]
    stale: list[str]
    frozen: str | None
    frozen_digest: Callable[[pathlib.Path], str]
    frozen_files: dict[pathlib.Path, bytes]
    disposition_check: Callable[[dict[int, str]], None]
    #: Row 7's performed record exists in `decisions/`.
    class_act_present: bool = True
    #: Why the builder says the record is not ready (empty when ready).
    not_ready: tuple[str, ...] = ()


def live_inputs(root: pathlib.Path) -> Inputs:
    # The builder expects the package as the repo-relative `PKG` and emits
    # repo-relative paths (the manifest rows are those paths). Handing it
    # `root / PKG` turned every produced path absolute and refused every
    # --record, so it is run with `root` as the working directory instead.
    cwd = os.getcwd()
    os.chdir(root)
    try:
        table = build.derive_table()
        produced = [RECORD_REL.as_posix()] if (root / RECORD_REL).is_file() else []
        stale = [str(p) for p in build.stale(table_fn=lambda: table)]
        _ready, not_ready = build.readiness(table=table)
    finally:
        os.chdir(cwd)
    files = {rel: (root / rel).read_bytes() for rel in
             [MANIFEST_REL, PACKET_REL, BRIEF_REL, SETTINGS_REL, RECORD_REL]
             if (root / rel).is_file()}
    review_path = root / CONFIRMATION_REVIEW_REL
    return Inputs(
        manifest=(root / MANIFEST_REL).read_bytes() if (root / MANIFEST_REL).is_file() else b"",
        subject=b"",
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        produced_paths=produced, stale=stale, frozen=FROZEN_SUBJECT,
        frozen_digest=lambda rel: FROZEN_FILE_DIGESTS.get(rel, ""),
        frozen_files=files,
        disposition_check=lambda findings: vs.validate_disposition(
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings),
        class_act_present=(root / CLASS_ACT_REL).is_file(),
        not_ready=tuple(not_ready),
    )


#: The shared severity form is `(note)` exactly. Round 7's raw, retained
#: verbatim (CC-REV-6), qualifies two notes as `(note — an open owner ruling…)`;
#: the first word is the severity, so this recorder reads that form too and
#: still refuses a qualified `(revise — …)` or `(blocking — …)`.
QUALIFIED_SEVERITY_RE = re.compile(
    r"^\*\*Finding (\d+) [—–-] [^\n]*?\*\*\s*\((blocking|revise|note)(?: [—–-][^)\n]*)?\)",
    re.MULTILINE)


def review_findings(review: str) -> dict[int, str]:
    section = vs.beh._raw_findings_section(review, vs.FINDINGS_HEADING)
    numbers = vs.beh._finding_number_set(
        section, label="review findings", forms=vs.beh.RAW_FINDING_FORMS)
    severities = {int(n): sev for n, sev in QUALIFIED_SEVERITY_RE.findall(section)}
    missing = sorted(numbers - set(severities))
    if missing:
        raise ValueError(f"review findings {missing} carry no (blocking|revise|note) severity")
    return {n: severities[n] for n in numbers}


def validate(act: Act, argument: str, inp: Inputs) -> tuple[str, str, str]:
    """Return (manifest file sha, reviewed commit, verdict) or raise ValueError."""
    if inp.frozen is None:
        raise ValueError("no confirming review is recorded: FROZEN_SUBJECT is unset, "
                         "so nothing may be recorded")
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    rows = ROW_RE.findall(inp.manifest.decode())
    paths = [path for _sha, path in rows]
    if len(paths) != 1 or paths != sorted(inp.produced_paths):
        raise ValueError("manifest row population differs from the builder's one record")
    row = next((sha for sha, path in rows if path == act.subject.as_posix()), None)
    if row is None:
        raise ValueError(f"manifest has no row for {act.subject.as_posix()}")
    if row != argument:
        raise ValueError(f"owner argument {argument} is not the {act.key} manifest row {row}")
    if inp.stale:
        raise ValueError("builder reports stale instances or manifest: " + ", ".join(inp.stale))
    if inp.not_ready:
        raise ValueError("builder reports the record is not ready: " + "; ".join(inp.not_ready))
    if not inp.class_act_present:
        raise ValueError(f"row 7's act record {CLASS_ACT_REL.as_posix()} does not exist: the "
                         "project-documentation class is outside RFC5-14's closed vocabulary")
    if digest(inp.subject) != argument:
        raise ValueError(f"{act.key} record hashes to {digest(inp.subject)}, not the owner argument")
    missing = [r.as_posix() for r in (MANIFEST_REL, PACKET_REL, BRIEF_REL, SETTINGS_REL, RECORD_REL)
               if r not in inp.frozen_files]
    if missing:
        raise ValueError("frozen-file set lacks " + ", ".join(missing))
    for rel, current in inp.frozen_files.items():
        expected = current if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", current, count=1)
        if digest(expected) != inp.frozen_digest(rel):
            raise ValueError(f"frozen subject does not carry the presented bytes of {rel.as_posix()}")
    if HEX64_RE.search(inp.packet.decode()):
        raise ValueError("owner packet carries a 64-hex token; arguments come only "
                         "from the manifest rows")
    manifest_sha = digest(inp.manifest)
    head = [line for line in inp.review.splitlines() if line.strip()][:4]
    if f"Manifest SHA-256: {manifest_sha}" not in head:
        raise ValueError("confirmation review head does not bind the manifest file's SHA-256")
    verdicts = [m.group(1) for line in head if (m := VERDICT_RE.match(line))]
    if len(verdicts) != 1 or verdicts[0] not in VERDICTS:
        raise ValueError("confirmation review head does not carry the verdict CONFIRM "
                         "or CONFIRM WITH EXCEPTIONS")
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    if verdicts[0] == "CONFIRM WITH EXCEPTIONS":
        findings = review_findings(inp.review)
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; only a "
                             "notes-only round clears the bytes")
        inp.disposition_check(findings)
    return manifest_sha, reviewed.group(1), verdicts[0]


@dataclass(frozen=True)
class Selection:
    opening: str
    label: str
    description: str

    def validate(self) -> None:
        for name, value in (("opening", self.opening), ("label", self.label),
                            ("description", self.description)):
            if not value.strip() or "\n" in value:
                raise ValueError(f"owner selection {name} must be one non-empty line")
            if HEX64_RE.search(value):
                raise ValueError(f"owner selection {name} carries a 64-hex digest")


def render_act(act: Act, argument: str, date: str, manifest_sha: str, reviewed: str,
               verdict: str, sel: Selection, frozen: str, instant: str) -> str:
    return f"""# Owner act — {act.title}

Date: {date}

Recorded at (UTC): {instant}

Owner: Tzeusy

Act identity: `{identity_for(act, date)}`

Act type: `{act.act_type}`

Project identity: `project:syzygy`

Artifact identity: `{act.subject.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes the first version of the same
record, if an act over it is in force, prospectively and as the record's own
revocation line states (RFC5-13); with none in force it supersedes nothing. It
is revoked only by a later exact owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at
`{PACKET_REL.as_posix()}`, which by design carries no digest. The act takes
this phrase, whose argument is this record's row of the package manifest:

```text
{phrase_for(act, argument)}
```

The owner did not type the phrase. On {date} the owner answered a structured
question in the Claude Code CLI that opened "{sel.opening}" by selecting the
option below; the selection is the instruction, and it names the records "at
the manifest rows". The label and description, verbatim:

| Label | Description |
|---|---|
| "{sel.label}" | "{sel.description}" |

The argument was read from this record's row of
`{MANIFEST_REL.as_posix()}` at the frozen commit and matched the record on
disk at recording. A swapped argument would have been refused: the recorder
rejects an argument that is not this record's row.

Frozen provenance:

- frozen subject (package bytes): `{frozen}`;
- manifest SHA-256: `{manifest_sha}`;
- confirmation review: `{CONFIRMATION_REVIEW_REL.as_posix()}`, verdict
  `{verdict}`, its head bound to the manifest file's SHA-256 above; notes, if
  any, are dispositioned in `{DISPOSITION_REL.as_posix()}`; the raw names
  reviewed commit `{reviewed}` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

{act.effect}

## What this act does not authorize

This act satisfies only its own authority; the sitting's other acts each take
their own act and none implies another (REQ-polaris-generation-025). The
RFC5-14 amendment it depends on is a separate act, performed first. It
adopts no registry entry or screening policy, amends no contract, and grants
no read, egress, write, execution, deployment, release, autonomous or
multi-user authority beyond what its Effect states. Observation consent
permits no egress, and egress consent permits no read. It proves no read,
screening, generation or answer result.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Public egress version 2 act — {act.act_type} — {act.key} — performed {date}"


def render_aggregate_block(act: Act, argument: str, date: str, manifest_sha: str,
                           verdict: str, frozen: str, instant: str) -> str:
    return f"""{aggregate_heading(act, date)}

**Phrase the act takes (given {date} by option selection, not typed; see the
dedicated record):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{act.act_type}` / `{act.subject.as_posix()}` |
| Argument | SHA-256 of the artifact itself: its row of the package manifest, recomputed at recording |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Frozen subject | `{frozen}` |
| Manifest | `{MANIFEST_REL.as_posix()}`, SHA-256 `{manifest_sha}` |
| Review outcome | `{CONFIRMATION_REVIEW_REL.as_posix()}`: `{verdict}`, its head bound to the manifest file |
| Recorded at (UTC) | `{instant}` |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: this one record is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own role only. The sitting's
other acts remain separate.
"""


def expected(act: Act, argument: str, date: str, sel: Selection, inp: Inputs, instant: str):
    sel.validate()
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    if not INSTANT_RE.fullmatch(instant) or not instant.startswith(date + "T"):
        raise ValueError("instant must be YYYY-MM-DDTHH:MM:SSZ (UTC) on the act's date")
    manifest_sha, reviewed, verdict = validate(act, argument, inp)
    frozen = inp.frozen or ""
    return (render_act(act, argument, date, manifest_sha, reviewed, verdict, sel, frozen, instant),
            render_aggregate_block(act, argument, date, manifest_sha, verdict, frozen, instant))


def with_subject(inp: Inputs, root: pathlib.Path, act: Act) -> Inputs:
    path = root / act.subject
    inp.subject = path.read_bytes() if path.is_file() else b""
    return inp


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
              instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()}")
        return 1
    try:
        record, block = expected(act, argument, date, sel, with_subject(live_inputs(root), root, act), instant)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED (nothing written): {exc}")
        return 1
    aggregate = (root / AGGREGATE_REL).read_text()
    if aggregate_heading(act, date) in aggregate:
        print("FAILED: aggregate record already carries this act's heading")
        return 1
    (root / act.record).write_text(record)
    (root / AGGREGATE_REL).write_text(aggregate.rstrip() + "\n\n" + block)
    print(f"recorded at {instant}")
    print(f"wrote {act.record.as_posix()}\nappended one section to {AGGREGATE_REL.as_posix()}")
    print(f"next, in the same change: tag {tag_for(act, date)} on the commit carrying them; "
          "scripts/check_governance.py: add the chain link and the performed-act "
          "registration for this label (the candidate registration stays until then)")
    return 0


def do_check(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
             instant: str | None = None) -> int:
    if instant is None:   # the instant is part of the record: read it, then regenerate and compare
        on_disk = (root / act.record).read_text() if (root / act.record).is_file() else ""
        found = RECORDED_RE.findall(on_disk)
        if len(found) != 1:
            print(f"FAILED: {act.record.as_posix()} carries {len(found)} 'Recorded at (UTC)' lines, not 1")
            return 1
        instant = found[0]
    try:
        record, block = expected(act, argument, date, sel, with_subject(live_inputs(root), root, act), instant)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED: {exc}")
        return 1
    path = root / act.record
    drift = not path.is_file() or path.read_text() != record
    count = (root / AGGREGATE_REL).read_text().count(block)
    if drift:
        print(f"recorded act differs from regeneration: {act.record.as_posix()}")
    if count != 1:
        print(f"aggregate record carries {count} copies of this act's block, not 1")
    if drift or count != 1:
        return 1
    print(f"recorded {act.key} act matches the exact owner argument")
    return 0


def selftest() -> int:
    """One mutant per predicate; each must be refused for the stated reason."""
    act = ACTS[0]
    record = b"record egress v2\n"
    pkt = b"# Packet\n\n> Candidate - binds nothing.\n\nbody\n"
    rsha = digest(record)
    manifest = (f"# header\n{rsha}  {act.subject.as_posix()}\n").encode()
    msha = digest(manifest)
    review = (f"# R1\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, PACKET_REL: pkt, BRIEF_REL: b"brief",
             SETTINGS_REL: b'{"version": "x"}', RECORD_REL: record}

    def make(**over) -> Inputs:
        base = dict(manifest=manifest, subject=record, packet=pkt, review=review,
                    produced_paths=[act.subject.as_posix()], stale=[], frozen="f" * 40,
                    frozen_digest=lambda rel: digest(blobs[rel]), frozen_files=dict(blobs),
                    disposition_check=lambda findings: None)
        base.update(over)
        return Inputs(**base)

    results: list[tuple[str, bool]] = []

    def refused(needle, argument, inp) -> bool:
        try:
            validate(act, argument, inp)
        except ValueError as exc:
            return needle in str(exc)
        return False

    arg = rsha
    try:
        ok = validate(act, arg, make())[2] == "CONFIRM"
    except ValueError as exc:
        print(f"  (exact-argument failure: {exc})")
        ok = False
    results.append(("exact argument validates", ok))
    if FROZEN_SUBJECT is None:
        print("  (nothing is frozen yet: the bare-copy digest check runs once a round returns)")
    else:
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            bare = pathlib.Path(d)
            ok = bool(FROZEN_FILE_DIGESTS)
            for rel, want in FROZEN_FILE_DIGESTS.items():
                src = ROOT / rel
                (bare / rel).parent.mkdir(parents=True, exist_ok=True)
                (bare / rel).write_bytes(src.read_bytes())
                cur = (bare / rel).read_bytes()
                cur = cur if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", cur, count=1)
                ok = ok and digest(cur) == want
            results.append(("frozen files verify from a copy with no git object",
                            ok and not (bare / ".git").exists()))
    results.append(("the shipped recorder is unfrozen or has exactly the five frozen files",
                    FROZEN_SUBJECT is None and not FROZEN_FILE_DIGESTS
                    or set(FROZEN_FILE_DIGESTS) == {MANIFEST_REL, PACKET_REL, BRIEF_REL,
                                                    SETTINGS_REL, RECORD_REL}))
    results.append(("unset FROZEN_SUBJECT refused",
                    refused("FROZEN_SUBJECT is unset", arg, make(frozen=None))))
    results.append(("non-hex argument refused", refused("not a 64-hex", "xyz", make())))
    results.append(("wrong argument refused", refused("manifest row", "0" * 64, make())))
    results.append(("two manifest rows refused",
                    refused("row population", arg, make(
                        manifest=manifest + f"{'1' * 64}  other.md\n".encode(),
                        produced_paths=[act.subject.as_posix(), "other.md"]))))
    results.append(("manifest row out of population refused",
                    refused("row population", arg, make(produced_paths=["x"]))))
    results.append(("stale builder output refused", refused("stale", arg, make(stale=["x"]))))
    results.append(("a record that is not ready refused",
                    refused("not ready", arg, make(not_ready=("requiredStages is empty",)))))
    results.append(("row 7 absent refused",
                    refused("row 7", arg, make(class_act_present=False))))
    results.append(("record not hashing to the argument refused",
                    refused("hashes to", arg, make(subject=record + b"x"))))
    short = {k: v for k, v in blobs.items() if k != SETTINGS_REL}
    results.append(("a frozen-file set missing v2.json refused",
                    refused("frozen-file set lacks", arg, make(frozen_files=short))))
    drift = dict(blobs)
    drift[PACKET_REL] = pkt + b"x"
    results.append(("frozen commit lacking the presented packet refused",
                    refused("frozen subject does not carry", arg,
                            make(frozen_digest=lambda rel: digest(drift[rel])))))
    drift = dict(blobs)
    drift[SETTINGS_REL] = b'{"version": "y"}'
    results.append(("frozen commit lacking the presented v2.json refused",
                    refused("frozen subject does not carry", arg,
                            make(frozen_digest=lambda rel: digest(drift[rel])))))
    performed = pkt.replace(b"\n\n", b"\n\n> **PERFORMED 2026-10-04.** Recorded.\n\n", 1)
    perf_files = dict(blobs)
    perf_files[PACKET_REL] = performed
    results.append(("PERFORMED head over the frozen packet accepted",
                    not refused("frozen subject does not carry", arg,
                                make(packet=performed, frozen_files=perf_files))))
    results.append(("packet carrying a digest refused",
                    refused("64-hex token", arg, make(packet=pkt + arg.encode()))))
    results.append(("review binding another manifest digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, "0" * 64)))))
    results.append(("review binding the record row instead of the file digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, arg)))))
    results.append(("verdict REVISE refused",
                    refused("verdict", arg, make(review=review.replace("CONFIRM", "REVISE")))))
    results.append(("verdict displaced past the fourth head line refused",
                    refused("verdict", arg, make(review=review.replace(
                        "Verdict: CONFIRM", "Note: x\nVerdict: CONFIRM")))))
    exc_review = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
        "none", "**Finding 1 \u2014 t** (revise)\nbody")
    results.append(("a revise finding under CONFIRM WITH EXCEPTIONS refused",
                    refused("non-note", arg, make(review=exc_review))))
    notes = exc_review.replace("(revise)", "(note)")
    results.append(("notes-only CONFIRM WITH EXCEPTIONS accepted", _accepts(act, arg, make(review=notes))))
    results.append(("a qualified note severity is read as note",
                    _accepts(act, arg, make(review=notes.replace("(note)", "(note \u2014 an open owner ruling)")))))
    results.append(("a qualified revise severity is still refused",
                    refused("non-note", arg, make(review=exc_review.replace("(revise)", "(revise \u2014 note)")))))

    def bad_disposition(findings):
        raise ValueError("disposition record does not name the reviewed raw")
    results.append(("missing disposition refused",
                    refused("disposition", arg, make(review=notes, disposition_check=bad_disposition))))
    for name, sel in (("empty label", Selection("q", "", "d")),
                      ("multi-line description", Selection("q", "l", "a\nb")),
                      ("digest in opening", Selection("q " + "a" * 64, "l", "d"))):
        try:
            sel.validate()
            results.append((f"selection with {name} refused", False))
        except ValueError:
            results.append((f"selection with {name} refused", True))
    ok_sel = Selection("Perform the egress version 2 act?", "Perform it now", "Perform the act at the manifest row.")
    try:
        rec, block = expected(act, arg, "2026-10-04", ok_sel, make(), INSTANT_OK)
        results.append(("record and block render, naming the row and the tag",
                        arg in rec and arg in block and tag_for(act, "2026-10-04") in rec))
        results.append(("record carries the phrase exactly once in its ceremony",
                        rec.count(phrase_for(act, arg)) == 1))
        results.append(("record and block carry the instant exactly once each",
                        rec.count(f"Recorded at (UTC): {INSTANT_OK}") == 1 and block.count(f"`{INSTANT_OK}`") == 1))
    except ValueError as exc:
        print(f"  (render failure: {exc})")
        results.append(("record and block render", False))
    results.append(("bad date refused", _raises(lambda: expected(
        act, arg, "04/10", ok_sel, make(), INSTANT_OK))))
    for name, bad in (("a date-only instant", "2026-10-04"), ("a local-offset instant", "2026-10-04T09:30:00+08:00"),
                      ("fractional seconds", "2026-10-04T09:30:00.5Z"), ("an instant on another date", "2026-10-05T00:00:00Z"),
                      ("a lowercase z", "2026-10-04T09:30:00z")):
        results.append((f"{name} refused", _raises(lambda bad=bad: expected(
            act, arg, "2026-10-04", ok_sel, make(), bad))))
    results.append(("record, check and a repeat --record on a scratch tree with no git", _end_to_end()))
    failed = [name for name, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def _end_to_end() -> bool:
    """Run --record and --check for real on a scratch copy of both packages
    with no git at all, a synthetic confirming raw bound to the scratch
    manifest, and the row-7 record present; then with row 7 absent, where
    --record must refuse and write nothing. A path or root-handling bug in the
    recorder's own input reading fails the selftest, not the owner's sitting."""
    import contextlib
    import io
    import shutil
    import tempfile
    global FROZEN_SUBJECT, FROZEN_FILE_DIGESTS
    saved = (FROZEN_SUBJECT, FROZEN_FILE_DIGESTS)
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        shutil.copytree(ROOT / PKG, root / PKG)
        shutil.copytree(ROOT / build.V1, root / build.V1)
        (root / DECISIONS).mkdir(parents=True, exist_ok=True)
        (root / AGGREGATE_REL).write_text("# Acceptance record\n")
        act = ACTS[0]
        # the scratch copy is generated from the live code, so it is current and ready
        os.chdir(root)
        try:
            table = build.derive_table()
            (root / RECORD_REL).write_text(build.record_text(table_fn=lambda: table))
            (root / MANIFEST_REL).write_text(build.manifest_text(table_fn=lambda: table))
            ready, why = build.readiness(table=table)
        finally:
            os.chdir(ROOT)
        if not ready:
            print("  (end-to-end: record not ready in the scratch copy: " + "; ".join(why) + ")")
            return False
        arg = digest((root / act.subject).read_bytes())
        raw = root / CONFIRMATION_REVIEW_REL
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text(f"# R1\nReviewed commit: {'a' * 40}\n"
                       f"Manifest SHA-256: {digest((root / MANIFEST_REL).read_bytes())}\n"
                       "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
        FROZEN_SUBJECT = "f" * 40
        FROZEN_FILE_DIGESTS = {r: digest((root / r).read_bytes())
                               for r in (MANIFEST_REL, PACKET_REL, BRIEF_REL, SETTINGS_REL, RECORD_REL)}
        sel = Selection("Perform the egress version 2 act?", "Perform it now", "Perform the act at the manifest row.")
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                refused_no_row7 = do_record(root, act, arg, "2026-10-04", sel, INSTANT_OK)
                absent_clean = not (root / act.record).exists()
                (root / CLASS_ACT_REL).write_text("# row 7 stand-in\n")
                wrote = do_record(root, act, arg, "2026-10-04", sel, INSTANT_OK)
                checked = do_check(root, act, arg, "2026-10-04", sel)
                again = do_record(root, act, arg, "2026-10-04", sel, INSTANT_OK)
        finally:
            FROZEN_SUBJECT, FROZEN_FILE_DIGESTS = saved
        if wrote != 0:
            print("  (end-to-end --record said: " + out.getvalue().strip().splitlines()[-1][:200] + ")")
        record = (root / act.record).read_text() if (root / act.record).is_file() else ""
        return (refused_no_row7 == 1 and absent_clean and wrote == 0 and checked == 0 and again == 1
                and record.count(f"Recorded at (UTC): {INSTANT_OK}") == 1
                and not (root / ".git").exists())


INSTANT_OK = "2026-10-04T09:30:00Z"


def _accepts(act, argument, inp) -> bool:
    try:
        validate(act, argument, inp)
        return True
    except ValueError:
        return False


def _raises(fn) -> bool:
    try:
        fn()
    except ValueError:
        return True
    return False


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", nargs=2, metavar=("KEY", "ARGUMENT"))
    mode.add_argument("--check", nargs=2, metavar=("KEY", "ARGUMENT"))
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--instant", help="UTC instant YYYY-MM-DDTHH:MM:SSZ; --record defaults to now, --check reads it from the record")
    ap.add_argument("--question-opening")
    ap.add_argument("--selection-label")
    ap.add_argument("--selection-description")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
    key, argument = args.record or args.check
    if key not in ACT_BY_KEY:
        print(f"unknown act key {key}; one of {', '.join(ACT_BY_KEY)}", file=sys.stderr)
        return 2
    if not (args.date and args.question_opening and args.selection_label
            and args.selection_description):
        print("--date, --question-opening, --selection-label and "
              "--selection-description are required", file=sys.stderr)
        return 2
    sel = Selection(args.question_opening, args.selection_label, args.selection_description)
    fn = do_record if args.record else do_check
    return fn(ROOT, ACT_BY_KEY[key], argument, args.date, sel, args.instant)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
