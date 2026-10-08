#!/usr/bin/env python3
"""Record or verify the owner's act over version 2 of the Redis agent-provider statement.

Package `contracts/candidates/dossier-agent-provider-v2/` (register row P-106).
One state-(1) `consent-agent-provider` owner act over the one record the
package manifest names: the Redis statement for Claude Code with Anthropic, at
version `0.2.0-candidate.1`, which adds `project-documentation` to version 1's
classes. The owner gives it by selecting an option in a structured question;
the packet (`decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`,
decision 2) maps that option to the words it offers, and no phrase is typed
and no digest appears in the packet. The act supersedes, prospectively from its
own instant (RFC5-13), the version-1 act recorded by
`scripts/record_dossier_local_agent_acts.py` (key `redis-agent-anthropic`).
This script performs nothing by itself.

FROZEN. Round 2 of the package review returned `CONFIRM WITH EXCEPTIONS`, notes
only, over commit `5db1dd72` (`docs/reviews/R-DOSSIER-AGENT-PROVIDER-V2-2-RAW.md`;
notes in `ROUND-2-DISPOSITIONS.md`), which under the owner's notes-only rule
clears the package at its manifest. `FROZEN_FILE_DIGESTS` holds the SHA-256 of
each file that review read whose bytes the act relies on, taken from that
commit by `--freeze-table 5db1dd72`, never by hand: the manifest, the record,
its template and params, the brief and the decision packet.
`SEMANTIC-DELTA.md` is not frozen: round-2 note 1 was taken in it after the
review (a prose edit naming the merged `--tool` prerequisite), and it is
neither the act's argument nor a file the act's record cites.

ORDER. The version-1 act must be recorded and bind the version-1 record's
current bytes; its date and argument go into the supersession line, which the
gate reads.

`--record ARGUMENT --date D [--instant I] --question-opening Q
--selection-label L --selection-description S --packet-words W` requires,
before anything is written:

1. the argument is a 64-hex SHA-256 equal to the manifest's one row, the row
   names exactly the builder's one record, and the builder reports nothing
   stale (so the record still differs from version 1 by the declared lines
   only);
2. the record on disk hashes to the argument;
3. the version-1 act record exists and binds the version-1 record's bytes;
4. every frozen file hashes to the digest recorded below for it (the packet
   may gain one PERFORMED head), and the packet carries no 64-hex token;
5. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE, the value the builder's --manifest-digest prints, never a row>` and a
   verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter clears the
   bytes only when every finding is a `note` and `ROUND-2-DISPOSITIONS.md`
   names the raw on a `Reviewed record:` line and dispositions every finding;
6. the owner's selection (opening, label, description) and the packet words it
   maps to are non-empty, one line each, carry no 64-hex digest, and the words
   are the packet's own offer.

It then writes the dedicated record (with the UTC instant of recording) and
appends one `ACCEPTANCE-ACT-RECORD.md` section. The record is read by
`packages/polaris-dossier/src/gate-sources.ts` through a byte-for-byte port of
`render_act` (`PROVIDER_V2_TEMPLATE`), held to this script by a test; its prose
carries no other act family's sweep stems (round-2 note 3), which the selftest
checks. `--check` re-derives both and counts exactly one copy of the block.
`--freeze-table [COMMIT]` prints the frozen-digest table. `--selftest` mutates
each predicate and requires it to fail closed.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_dossier_agent_provider_v2 as build  # noqa: E402
import record_dossier_local_agent_acts as v1rec  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
PKG = build.PKG
MANIFEST_REL = PKG / build.MANIFEST_NAME
SUBJECT_REL = PKG / "instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md"
PACKET_REL = DECISIONS / "DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md"
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
TEMPLATE_REL = PKG / "templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md"
PARAMS_REL = PKG / "instances/redis/params.json"
CONFIRMATION_REVIEW_REL = pathlib.Path("docs/reviews/R-DOSSIER-AGENT-PROVIDER-V2-2-RAW.md")
DISPOSITION_REL = PKG / "ROUND-2-DISPOSITIONS.md"
#: The version-1 act this one supersedes, and the record it binds.
V1_ACT = v1rec.ACT_BY_KEY["redis-agent-anthropic"]
#: The commit the confirming review read (provenance; binding is by the manifest digest in the raw's head).
FROZEN_SUBJECT: str | None = "5db1dd720338edd7963653f7e19ff727e1e99f32"
#: SHA-256 of each frozen file at FROZEN_SUBJECT, by `--freeze-table 5db1dd72`.
FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {
    pathlib.Path(".syzygy/governance/contracts/candidates/dossier-agent-provider-v2/DOSSIER-AGENT-PROVIDER-V2-MANIFEST.txt"): "62cd699a6fbc4ad07777509e17530948f68efc7978800f6c0e4db358c7d06af7",
    pathlib.Path(".syzygy/governance/contracts/candidates/dossier-agent-provider-v2/instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md"): "b7a8d099ce108bfd70133b729327534f29806cb0118ee0b3e0f9ca077a946df3",
    pathlib.Path(".syzygy/governance/contracts/candidates/dossier-agent-provider-v2/templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md"): "0a991f30a3238c1bba77afb6e3b9c7c042a0fcd8b23daf4b1b1d981f5f57ac02",
    pathlib.Path(".syzygy/governance/contracts/candidates/dossier-agent-provider-v2/instances/redis/params.json"): "0306719233a81a0e825a59d0f21149e7a35821f240a42971db12d70545bb5162",
    pathlib.Path(".syzygy/governance/contracts/candidates/dossier-agent-provider-v2/REVIEW-BRIEF.md"): "f92edb4bcacefadc8d486ff5f80b18b95e25e28554db2691f0628ba52012992a",
    pathlib.Path(".syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md"): "0bd42fbba09380e024f26e016804a274a5b55623e195c26194ff1b5f170de664",
}
#: The words the packet offers for decision 2's sign option.
PACKET_WORDS = ("Sign the Redis Anthropic provider statement, version 2",)
SHA_RE = v1rec.SHA_RE
HEX64_RE = v1rec.HEX64_RE
ROW_RE = v1rec.ROW_RE
REVIEWED_COMMIT_RE = v1rec.REVIEWED_COMMIT_RE
VERDICT_RE = v1rec.VERDICT_RE
VERDICTS = v1rec.VERDICTS
DATE_RE = v1rec.DATE_RE
INSTANT_RE = v1rec.INSTANT_RE
RECORDED_RE = v1rec.RECORDED_RE
PERFORMED_HEAD_RE = v1rec.PERFORMED_HEAD_RE
EXACT_DIGEST_RE = re.compile(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`$", re.MULTILINE)


@dataclass(frozen=True)
class Act:
    key: str
    label: str
    act_type: str
    identity_stem: str
    record: pathlib.Path
    title: str
    scope: str


ACT = Act("redis-agent-anthropic-v2", "CONSENT TO ANTHROPIC AGENT PROVIDER VERSION 2 FOR REDIS",
          "consent-agent-provider", "AGENT-PROVIDER-V2-REDIS-ANTHROPIC",
          DECISIONS / "DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md",
          "agent-provider statement for redis/redis, version 2: Claude Code with Anthropic",
          "operator-agent runs over this one repository with this one tool and provider")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"dossier-agent-provider-v2-redis-anthropic-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


def frozen_rels() -> list[pathlib.Path]:
    return [MANIFEST_REL, SUBJECT_REL, TEMPLATE_REL, PARAMS_REL, BRIEF_REL, PACKET_REL]


def frozen_table(read: Callable[[pathlib.Path], bytes] | None = None) -> str:
    read = read or (lambda rel: (ROOT / rel).read_bytes())
    lines = []
    for rel in frozen_rels():
        data = read(rel)
        data = PERFORMED_HEAD_RE.sub(rb"\1", data, count=1) if rel == PACKET_REL else data
        lines.append(f'    pathlib.Path("{rel.as_posix()}"): "{digest(data)}",')
    return "FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {\n" + "\n".join(lines) + "\n}"


@dataclass
class Inputs:
    """Everything validation reads, injectable for the selftest."""
    manifest: bytes
    subject: bytes
    packet: bytes
    review: str
    produced_paths: list[str]
    stale: list[str]
    predecessor: str         # the version-1 act's argument ("" when its record is absent)
    predecessor_date: str
    predecessor_subject: bytes   # the version-1 record's current bytes
    frozen: str | None
    frozen_digest: Callable[[pathlib.Path], str]
    frozen_files: dict[pathlib.Path, bytes]
    disposition_check: Callable[[dict[int, str]], None]


def live_inputs(root: pathlib.Path) -> Inputs:
    pred = (root / V1_ACT.record).read_text() if (root / V1_ACT.record).is_file() else ""
    m = EXACT_DIGEST_RE.search(pred)
    d = re.search(r"^Date: (\d{4}-\d{2}-\d{2})$", pred, re.MULTILINE)
    review_path = root / CONFIRMATION_REVIEW_REL
    try:
        produced = [rel.as_posix() for rel, _t in build.instances(root)]
    except (ValueError, KeyError, OSError):
        produced = []
    return Inputs(
        manifest=(root / MANIFEST_REL).read_bytes() if (root / MANIFEST_REL).is_file() else b"",
        subject=(root / SUBJECT_REL).read_bytes() if (root / SUBJECT_REL).is_file() else b"",
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        produced_paths=produced, stale=build.stale(root),
        predecessor=m.group(1) if m else "", predecessor_date=d.group(1) if d else "",
        predecessor_subject=(root / V1_ACT.subject).read_bytes() if (root / V1_ACT.subject).is_file() else b"",
        frozen=FROZEN_SUBJECT, frozen_digest=lambda rel: FROZEN_FILE_DIGESTS.get(rel, ""),
        frozen_files={rel: (root / rel).read_bytes() for rel in FROZEN_FILE_DIGESTS if (root / rel).is_file()},
        disposition_check=lambda findings: vs.validate_disposition(
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings),
    )


def validate(act: Act, argument: str, inp: Inputs) -> tuple[str, str, str]:
    """Return (manifest file sha, reviewed commit, verdict) or raise ValueError."""
    if inp.frozen is None:
        raise ValueError("no confirming review is recorded: FROZEN_SUBJECT is unset, so nothing may be recorded")
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    rows = ROW_RE.findall(inp.manifest.decode())
    if sorted(p for _s, p in rows) != sorted(inp.produced_paths) or [p for _s, p in rows] != [SUBJECT_REL.as_posix()]:
        raise ValueError("manifest row population is not exactly the builder's one record")
    if rows[0][0] != argument:
        raise ValueError(f"owner argument {argument} is not the manifest row {rows[0][0]}")
    if inp.stale:
        raise ValueError("builder reports stale records or manifest: " + ", ".join(inp.stale))
    if digest(inp.subject) != argument:
        raise ValueError(f"the record hashes to {digest(inp.subject)}, not the owner argument")
    if not SHA_RE.fullmatch(inp.predecessor) or not DATE_RE.fullmatch(inp.predecessor_date):
        raise ValueError("the version-1 act record is absent or names no exact digest and date")
    if digest(inp.predecessor_subject) != inp.predecessor:
        raise ValueError("the version-1 act does not bind the version-1 record's current bytes")
    if set(inp.frozen_files) != set(frozen_rels()):
        raise ValueError("frozen-file set is not exactly the files the act relies on")
    for rel, current in inp.frozen_files.items():
        expected = current if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", current, count=1)
        if digest(expected) != inp.frozen_digest(rel):
            raise ValueError(f"frozen subject does not carry the presented bytes of {rel.as_posix()}")
    if HEX64_RE.search(inp.packet.decode()):
        raise ValueError("owner packet carries a 64-hex token; the argument comes only from the manifest row")
    manifest_sha = digest(inp.manifest)
    head = [line for line in inp.review.splitlines() if line.strip()][:4]
    if f"Manifest SHA-256: {manifest_sha}" not in head:
        raise ValueError("confirmation review head does not bind the manifest file's SHA-256")
    verdicts = [m.group(1) for line in head if (m := VERDICT_RE.match(line))]
    if len(verdicts) != 1 or verdicts[0] not in VERDICTS:
        raise ValueError("confirmation review head does not carry the verdict CONFIRM or CONFIRM WITH EXCEPTIONS")
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    if verdicts[0] == "CONFIRM WITH EXCEPTIONS":
        findings = vs.review_findings(inp.review)
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; only a notes-only round clears the bytes")
        inp.disposition_check(findings)
    return manifest_sha, reviewed.group(1), verdicts[0]


@dataclass(frozen=True)
class Selection:
    opening: str
    label: str
    description: str
    words: str

    def validate(self) -> None:
        for name, value in (("opening", self.opening), ("label", self.label), ("description", self.description),
                            ("packet words", self.words)):
            if not value.strip() or "\n" in value or "\r" in value:
                raise ValueError(f"owner selection {name} must be one non-empty line")
            if HEX64_RE.search(value):
                raise ValueError(f"owner selection {name} carries a 64-hex digest")
        if self.words not in PACKET_WORDS:
            raise ValueError(f"the packet words {self.words!r} are not the packet's offer {list(PACKET_WORDS)}")


def render_act(act: Act, argument: str, date: str, manifest_sha: str, reviewed: str, verdict: str,
               sel: Selection, frozen: str, instant: str, superseded: str, superseded_date: str) -> str:
    """Ported byte for byte to `PROVIDER_V2_TEMPLATE` in packages/polaris-dossier/src/gate-sources.ts."""
    return f"""# Owner act — {act.title}

Date: {date}

Recorded at (UTC): {instant}

Owner: Tzeusy

Act identity: `{identity_for(act, date)}`

Act type: `{act.act_type}`

Project identity: `project:syzygy`

Artifact identity: `{SUBJECT_REL.as_posix()}`

Exact digest (SHA-256): `{argument}`

Scope: {act.scope}

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, prospectively from its own instant (RFC5-13), the {superseded_date} act recorded at `{V1_ACT.record.as_posix()}`, which binds version 1 of the same record at `{superseded}`. That record, its digest and the bytes it bound remain immutable history. This act is revoked only by a later exact owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented decision 2 of the packet at
`{PACKET_REL.as_posix()}`, which by design carries no digest.
The act takes this phrase, whose argument is the one row of the package
manifest:

```text
{phrase_for(act, argument)}
```

The owner did not type the phrase. On {date} the owner answered a structured
question in the Claude Code CLI that opened "{sel.opening}" by selecting the
option below. The label and description, verbatim:

| Label | Description |
|---|---|
| "{sel.label}" | "{sel.description}" |

The packet maps that option to its words "{sel.words}"; the selection is the
instruction, and the words name the record at the manifest row.

The argument was read from the one row of
`{MANIFEST_REL.as_posix()}` and matched the record on disk
at recording. A swapped argument would have been refused: the recorder
rejects an argument that is not that row.

Frozen provenance:

- frozen subject (package bytes): `{frozen}`;
- the package manifest file hashes to `{manifest_sha}` (a container
  digest, no act's argument);
- confirmation review: `{CONFIRMATION_REVIEW_REL.as_posix()}`, verdict
  `{verdict}`, its head bound to the manifest file's SHA-256 above; notes, if
  any, are dispositioned in `{DISPOSITION_REL.as_posix()}`; the raw names
  reviewed commit `{reviewed}` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

The record is the owner's explicit, recorded, per-project consent (SEC-2)
that the operator's Claude Code sessions, with Anthropic, may receive the
content classes it lists from (`project:syzygy`, `repository:redis-redis`) in
an operator-agent run, so a brief may issue for that repository even when it
counts as governed. Version 2 lists `project-documentation` beside version
1's five classes and differs from version 1 in nothing else but its draft
date, version and supersession line. From this act's instant the gate reads
version 2 and not version 1; before it, version 1 alone.

## What this act does not authorize

This act satisfies only its own authority (REQ-polaris-generation-025). It
gives no observation consent, adopts no registry entry or screening policy,
amends no doctrine, contract or specification, and grants no read, egress,
write, execution, deployment, release, autonomous or multi-user authority
beyond what its Effect states. It is not an egress record and widens no
consent to another tool, provider or repository. It proves no read,
screening, generation or answer result.
"""


#: Section markers, as the screening-scope acts write them.
BLOCK_BEGIN = "<!-- DOSSIER-AGENT-PROVIDER-V2:BEGIN -->"
BLOCK_END = "<!-- DOSSIER-AGENT-PROVIDER-V2:END -->"


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Agent-provider statement version 2 act — {act.act_type} — {act.key} — performed {date}"


def render_aggregate_block(act: Act, argument: str, date: str, manifest_sha: str,
                           verdict: str, frozen: str, instant: str) -> str:
    return f"""{BLOCK_BEGIN}
{aggregate_heading(act, date)}

Act instant: {instant}

**Phrase the act takes (given {date} by option selection, not typed; see the
dedicated record):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{act.act_type}` / `{SUBJECT_REL.as_posix()}` |
| Scope | {act.scope} |
| Argument | SHA-256 of the artifact itself: the one row of the package manifest, recomputed at recording |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Frozen subject | `{frozen}` |
| Manifest | `{MANIFEST_REL.as_posix()}`, SHA-256 `{manifest_sha}` |
| Review outcome | `{CONFIRMATION_REVIEW_REL.as_posix()}`: `{verdict}`, its head bound to the manifest file |
| Recorded at (UTC) | `{instant}` |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: this one record is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own role only. It supersedes
the version-1 statement act prospectively; that act's record is unchanged.
{BLOCK_END}
"""


def expected(act: Act, argument: str, date: str, sel: Selection, inp: Inputs, instant: str):
    sel.validate()
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    if not INSTANT_RE.fullmatch(instant) or not instant.startswith(date + "T"):
        raise ValueError("instant must be YYYY-MM-DDTHH:MM:SSZ (UTC) on the act's date")
    manifest_sha, reviewed, verdict = validate(act, argument, inp)
    frozen = inp.frozen or ""
    return (render_act(act, argument, date, manifest_sha, reviewed, verdict, sel, frozen, instant,
                       inp.predecessor, inp.predecessor_date),
            render_aggregate_block(act, argument, date, manifest_sha, verdict, frozen, instant))


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
              instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()}")
        return 1
    try:
        record, block = expected(act, argument, date, sel, live_inputs(root), instant)
    except (ValueError, OSError) as exc:
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
    print(f"next, in the same change: tag {tag_for(act, date)} on the commit carrying them")
    return 0


def do_check(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
             instant: str | None = None) -> int:
    if instant is None:
        on_disk = (root / act.record).read_text() if (root / act.record).is_file() else ""
        found = RECORDED_RE.findall(on_disk)
        if len(found) != 1:
            print(f"FAILED: {act.record.as_posix()} carries {len(found)} 'Recorded at (UTC)' lines, not 1")
            return 1
        instant = found[0]
    try:
        record, block = expected(act, argument, date, sel, live_inputs(root), instant)
    except (ValueError, OSError) as exc:
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
    print("recorded provider statement version-2 act matches the exact owner argument")
    return 0


# --- selftest ---------------------------------------------------------------

INSTANT_OK = "2026-10-09T09:30:00Z"
#: Other act families' sweep needles (case-folded, whitespace read as dashes) the record must not carry: the admission and egress
#: families, the class act, the policy family, the version-1 statement's own stems beyond the supersession path and artifact
#: basename (which the version-1 form reads past, at this template's exact render only), the OpenAI statement, the drawer, D9 and
#: the RFC7-20 reading, and the registry sign-off.
FOREIGN_NEEDLES = (
    "public-repo-admission", "public-egress-", "public-obs-", "rfc5-project-documentation", "public-source-scope",
    "pwb-secret-classification-policy", "agent-provider-redis-anthropic", "agent-provider-statement-—-redis-redis",
    "agent-provider-redis-redis-anthropic", "consent-to-agent-provider-anthropic-for-redis-redis",
    "agent-provider-statement-for-redis/redis:-claude-code-with-anthropic", "agent-provider:anthropic",
    "openai", "no-evidence-drawer", "no-kernel-evidence-drawer", "d9-in-force", "d9-for-operator-agent-runs",
    "rfc7-20-reading", "public-git-source-acquisition", "dossier-local-agent-acts",
)


def _fold(value: str) -> str:
    return re.sub("-+", "-", re.sub(r"[_\s]+", "-", value.lower()))


def selftest() -> int:
    """One mutant per predicate; each must be refused for the stated reason."""
    act = ACT
    record = b"record v2\n"
    pred_record = b"record v1\n"
    rsha = digest(record)
    pkt = b"# Packet\n\n> Candidate - binds nothing.\n\nbody\n"
    manifest = ("# header\n" + f"{rsha}  {SUBJECT_REL.as_posix()}\n").encode()
    msha = digest(manifest)
    review = (f"# R2\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, SUBJECT_REL: record, TEMPLATE_REL: b"tpl", PARAMS_REL: b"{}",
             BRIEF_REL: b"brief", PACKET_REL: pkt}

    def make(**over) -> Inputs:
        base = dict(manifest=manifest, subject=record, packet=pkt, review=review,
                    produced_paths=[SUBJECT_REL.as_posix()], stale=[], predecessor=digest(pred_record),
                    predecessor_date="2026-10-07", predecessor_subject=pred_record, frozen="f" * 40,
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
    results.append(("exact argument validates", _accepts(act, arg, make())))
    results.append(("the shipped table covers exactly the frozen files",
                    set(FROZEN_FILE_DIGESTS) == set(frozen_rels())
                    and all(SHA_RE.fullmatch(d) for d in FROZEN_FILE_DIGESTS.values())))
    results.append(("the version-1 act is the sitting's Anthropic statement act",
                    V1_ACT.subject.as_posix().endswith("dossier-local-agent-acts/instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md")))
    results.append(("the label is no prefix of, and has no prefix among, the version-1 labels (CG-7d reads LABEL: digest)",
                    not any(a.label.startswith(act.label) or act.label.startswith(a.label) for a in v1rec.ACTS)))
    results.append(("unset FROZEN_SUBJECT refused", refused("FROZEN_SUBJECT is unset", arg, make(frozen=None))))
    results.append(("non-hex argument refused", refused("not a 64-hex", "xyz", make())))
    results.append(("an argument that is not the row refused", refused("not the manifest row", "1" * 64, make())))
    results.append(("an extra manifest row refused",
                    refused("row population", arg, make(manifest=manifest + f"{'3' * 64}  {PKG.as_posix()}/instances/x/X.md\n".encode()))))
    results.append(("a row for another path refused",
                    refused("row population", arg, make(manifest=manifest.replace(b"ANTHROPIC.md", b"OPENAI.md")))))
    results.append(("stale builder output refused", refused("stale", arg, make(stale=["x"]))))
    results.append(("record not hashing to the argument refused", refused("hashes to", arg, make(subject=record + b"x"))))
    results.append(("a missing version-1 act refused", refused("version-1 act record", arg, make(predecessor=""))))
    results.append(("a version-1 act that no longer binds its record refused",
                    refused("version-1 record's current bytes", arg, make(predecessor_subject=pred_record + b"x"))))
    results.append(("a frozen-file set missing the template refused",
                    refused("frozen-file set", arg, make(frozen_files={k: b for k, b in blobs.items() if k != TEMPLATE_REL}))))
    drift = dict(blobs)
    drift[PACKET_REL] = pkt + b"x"
    results.append(("frozen commit lacking the presented packet refused",
                    refused("frozen subject does not carry", arg, make(frozen_digest=lambda rel: digest(drift[rel])))))
    drift = dict(blobs)
    drift[PARAMS_REL] = b"[]"
    results.append(("frozen commit lacking the presented params refused",
                    refused("frozen subject does not carry", arg, make(frozen_digest=lambda rel: digest(drift[rel])))))
    performed = pkt.replace(b"\n\n", b"\n\n> **PERFORMED 2026-10-09.** Recorded.\n\n", 1)
    perf_files = dict(blobs)
    perf_files[PACKET_REL] = performed
    results.append(("PERFORMED head over the frozen packet accepted",
                    _accepts(act, arg, make(packet=performed, frozen_files=perf_files))))
    results.append(("packet carrying a digest refused", refused("64-hex token", arg, make(packet=pkt + arg.encode()))))
    results.append(("review binding another manifest digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, "0" * 64)))))
    results.append(("review binding the row instead of the file digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, arg)))))
    results.append(("verdict REVISE refused", refused("verdict", arg, make(review=review.replace("CONFIRM", "REVISE")))))
    results.append(("verdict displaced past the fourth head line refused",
                    refused("verdict", arg, make(review=review.replace("Verdict: CONFIRM", "Note: x\nVerdict: CONFIRM")))))
    exc_review = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
        "none", "**Finding 1 — t** (revise)\nbody")
    results.append(("a revise finding under CONFIRM WITH EXCEPTIONS refused",
                    refused("non-note", arg, make(review=exc_review))))
    notes = exc_review.replace("(revise)", "(note)")
    results.append(("notes-only CONFIRM WITH EXCEPTIONS accepted", _accepts(act, arg, make(review=notes))))

    def bad_disposition(findings):
        raise ValueError("disposition record does not name the reviewed raw")
    results.append(("missing disposition refused",
                    refused("disposition", arg, make(review=notes, disposition_check=bad_disposition))))
    words = PACKET_WORDS[0]
    for name, sel in (("empty label", Selection("q", "", "d", words)),
                      ("multi-line description", Selection("q", "l", "a\nb", words)),
                      ("a carriage return in the label", Selection("q", "l\rx", "d", words)),
                      ("digest in opening", Selection("q " + "a" * 64, "l", "d", words)),
                      ("words the packet does not offer", Selection("q", "l", "d", "Decline")),
                      ("empty packet words", Selection("q", "l", "d", ""))):
        results.append((f"selection with {name} refused", _raises(sel.validate)))
    ok_sel = Selection("Which way on the provider statement?", "Sign version 2 (Recommended)",
                       "Docs text goes to your own Claude Code sessions.", words)
    rec = block = ""
    try:
        rec, block = expected(act, arg, "2026-10-09", ok_sel, make(), INSTANT_OK)
        results.append(("record and block render, naming the row and the tag",
                        arg in rec and arg in block and tag_for(act, "2026-10-09") in rec))
        results.append(("record carries the phrase exactly once", rec.count(phrase_for(act, arg)) == 1))
        results.append(("record quotes the selected label and the packet words",
                        f'| "{ok_sel.label}" |' in rec and f'its words "{words}"' in rec))
        results.append(("the supersession paragraph is one line naming the version-1 record and its argument",
                        re.search(r"^Supersession / revocation: [^\n]*`" + re.escape(V1_ACT.record.as_posix())
                                  + r"`[^\n]*`" + digest(pred_record) + r"`[^\n]*\n\n", rec, re.MULTILINE) is not None))
        results.append(("no line opens with 'recorded at' but the one field (the reader's loose instant count)",
                        len(re.findall(r"^\s*recorded at\b", rec, re.I | re.M)) == 1))
        body = _fold(rec.replace(V1_ACT.record.as_posix(), "").replace(SUBJECT_REL.as_posix(), ""))
        hits = [n for n in FOREIGN_NEEDLES if _fold(n) in body]
        if hits:
            print(f"  (foreign needles: {hits})")
        results.append(("the record carries no other family's stems beyond the two paths it must name", not hits))
        results.append(("the record names the version-1 record only in its supersession line",
                        [i for i, line in enumerate(rec.split("\n")) if V1_ACT.record.as_posix() in line]
                        == [i for i, line in enumerate(rec.split("\n")) if line.startswith("Supersession / revocation:")]))
        results.append(("the aggregate block is bracketed by section markers and carries the act instant",
                        block.count(BLOCK_BEGIN) == 1 and block.count(BLOCK_END) == 1
                        and block.count(f"Act instant: {INSTANT_OK}\n") == 1))
    except ValueError as exc:
        print(f"  (render failure: {exc})")
        results.append(("record and block render", False))
    results.append(("bad date refused", _raises(lambda: expected(act, arg, "09/10", ok_sel, make(), INSTANT_OK))))
    for name, bad in (("a date-only instant", "2026-10-09"), ("an instant on another date", "2026-10-10T00:00:00Z")):
        results.append((f"{name} refused", _raises(lambda bad=bad: expected(act, arg, "2026-10-09", ok_sel, make(), bad))))
    results.append(("record, check, a repeat --record and a tampered instant on a scratch tree", _end_to_end(ok_sel)))
    failed = [name for name, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def _end_to_end(sel: Selection) -> bool:
    """--record and --check for real on a scratch copy of the package, the version-1 record and a version-1 act binding it."""
    import contextlib
    import io
    import shutil
    import tempfile
    global FROZEN_FILE_DIGESTS
    saved = FROZEN_FILE_DIGESTS
    with tempfile.TemporaryDirectory() as d:
        root = build._fixture(pathlib.Path(d))
        (root / DECISIONS).mkdir(parents=True, exist_ok=True)
        (root / AGGREGATE_REL).write_text("# Acceptance record\n")
        shutil.copy(ROOT / PACKET_REL, root / PACKET_REL)
        v1sha = digest((root / V1_ACT.subject).read_bytes())
        (root / V1_ACT.record).write_text(f"# v1\n\nDate: 2026-10-07\n\nExact digest (SHA-256): `{v1sha}`\n")
        raw = root / CONFIRMATION_REVIEW_REL
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text(f"# R2 (synthetic, scratch only)\nReviewed commit: {'a' * 40}\n"
                       f"Manifest SHA-256: {digest((root / MANIFEST_REL).read_bytes())}\n"
                       "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
        FROZEN_FILE_DIGESTS = {r: digest((root / r).read_bytes()) for r in frozen_rels()}
        arg = digest((root / SUBJECT_REL).read_bytes())
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                wrote = do_record(root, ACT, arg, "2026-10-09", sel, INSTANT_OK)
                checked = do_check(root, ACT, arg, "2026-10-09", sel)
                again = do_record(root, ACT, arg, "2026-10-09", sel, INSTANT_OK)
                path = root / ACT.record
                path.write_text(path.read_text().replace(INSTANT_OK, "2026-10-09T09:31:00Z"))
                tampered = do_check(root, ACT, arg, "2026-10-09", sel)
        finally:
            FROZEN_FILE_DIGESTS = saved
        if wrote != 0:
            print("  (end-to-end --record said: " + out.getvalue().strip().splitlines()[-1][:200] + ")")
        return wrote == 0 and checked == 0 and again == 1 and tampered == 1


def _accepts(act, argument, inp) -> bool:
    try:
        validate(act, argument, inp)
        return True
    except ValueError as exc:
        print(f"  (unexpected refusal: {exc})")
        return False


def _raises(fn) -> bool:
    try:
        fn()
    except ValueError:
        return True
    return False


def at_commit_reader(commit: str) -> Callable[[pathlib.Path], bytes]:
    def read(rel: pathlib.Path) -> bytes:
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:{rel.as_posix()}"], capture_output=True)
        if r.returncode:
            raise ValueError(f"{rel.as_posix()} is not in commit {commit}")
        return r.stdout
    return read


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", metavar="ARGUMENT")
    mode.add_argument("--check", metavar="ARGUMENT")
    mode.add_argument("--freeze-table", nargs="?", const="", metavar="COMMIT")
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--instant", help="UTC instant YYYY-MM-DDTHH:MM:SSZ; --record defaults to now, --check reads it from the record")
    ap.add_argument("--question-opening")
    ap.add_argument("--selection-label")
    ap.add_argument("--selection-description")
    ap.add_argument("--packet-words")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
    if args.freeze_table is not None:
        print(frozen_table(at_commit_reader(args.freeze_table) if args.freeze_table else None))
        return 0
    argument = args.record or args.check
    if not (args.date and args.question_opening and args.selection_label and args.selection_description and args.packet_words):
        print("--date, --question-opening, --selection-label, --selection-description and --packet-words are required",
              file=sys.stderr)
        return 2
    sel = Selection(args.question_opening, args.selection_label, args.selection_description, args.packet_words)
    fn = do_record if args.record else do_check
    return fn(ROOT, ACT, argument, args.date, sel, args.instant)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
