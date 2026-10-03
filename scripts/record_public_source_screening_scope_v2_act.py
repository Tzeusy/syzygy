#!/usr/bin/env python3
"""Record or verify the owner's public-source screening-scope version-2 policy act.

Package `contracts/candidates/public-source-screening-scope-v2/` (sitting row
12). One state-(1) `approve-policy` owner act over the proposed secret-
classification policy, whose argument is ONE of the four rows of
`PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt` (variant none, manifesto,
architecture or both). The owner gives it by selecting an option in a
structured question that names the policy "at the manifest row"; no phrase is
typed and no digest appears in any Markdown file of the package. It supersedes,
for the `approve-policy` role only, the version-1 screening-scope act (sitting
row 1). This script performs nothing by itself, and it refuses to record
anything until the package has a confirming review: `FROZEN_SUBJECT` is unset
until a round returns `CONFIRM` or a notes-only `CONFIRM WITH EXCEPTIONS`, and
the frozen digests are then filled in by script (`--freeze-table`), never by
hand. It needs no git object: the commit is provenance only.

ORDER. The act depends on sitting rows 1 and 7: the version-1 act must be
recorded and the policy on disk must be exactly its argument, and the RFC5-14
act (row 7) must be recorded. It refuses otherwise.

ONE VARIANT ONLY. The four rows are alternatives. The recorder refuses when the
policy on disk is already any row of this manifest (this act, or another
variant's, is in force), and when this act's record exists. Changing variant
afterwards is a new owner act over a declared successor package, never a second
act over this manifest.

`--record ARGUMENT --date D [--instant I] --question-opening Q
--selection-label L --selection-description S` requires, before anything is
written:

1. the argument is a 64-hex SHA-256 equal to one row of the manifest, the
   manifest rows are exactly the four variants of the policy, and the builder
   verifies the package against the policy on disk and is ready;
2. the policy on disk is exactly the version-1 act's argument (so the patch can
   be applied to nothing else), and the proposed bytes of the chosen variant
   hash to the argument;
3. the version-1 act record and the row-7 act record exist;
4. every file the review read hashes to the digest recorded below for it (the
   packet may gain one PERFORMED head), and the packet carries no 64-hex token;
5. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE>` and a verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter
   clears the bytes only when every finding is a `note` and the sibling
   `ROUND-<n>-DISPOSITIONS.md` names the raw and dispositions every finding;
6. the owner's selection (opening, label, description) is non-empty, one line
   each, and carries no 64-hex digest.

It then writes the dedicated record (with the UTC instant of recording),
appends one `ACCEPTANCE-ACT-RECORD.md` section and applies the chosen variant's
bytes, so the policy on disk hashes to the argument. It does NOT re-point the
read gate: the install change (`scripts/install_redis_sitting.py`) does that
once, against the final bytes. `--check` re-derives the record and the block
after adoption, requires the policy to hash to the argument, and counts exactly
one copy of the block. `--freeze-table` prints the frozen-digest table for the
current files. `--selftest` mutates each predicate and requires it to fail
closed.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import pathlib
import re
import sys
from dataclasses import dataclass
from typing import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_source_screening_scope_v2 as build  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
PKG = build.PKG
MANIFEST_REL = build.MANIFEST
POLICY_REL = build.POLICY
PATCH_RELS = {v: build.patch_path(v) for v in build.VARIANTS}
PACKET_REL = build.PACKET
DELTA_REL = build.DELTA
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
LEDGER_REL = PKG / "IMPACT-LEDGER.md"
#: Row 1's performed record: the policy must be exactly its argument before this act.
V1_ACT_REL = DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md"
#: Row 7's performed record: until it exists the class is outside RFC5-14's vocabulary.
CLASS_ACT_REL = DECISIONS / "RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md"
#: Provisional until a round returns: the confirming raw and its notes record.
CONFIRMATION_REVIEW_REL = PKG / "reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-4-RAW.md"
DISPOSITION_REL = PKG / "ROUND-4-DISPOSITIONS.md"
#: The commit the confirming review read. None until a round returns CONFIRM or
#: notes-only CONFIRM WITH EXCEPTIONS; then set (with the table below, by
#: `--freeze-table`) and never hand-edited again. While None every `--record` is
#: refused: an unreviewed package cannot be recorded.
FROZEN_SUBJECT: str | None = None
#: SHA-256 of each file the confirming review read, taken by script. Keys: the
#: manifest, the four patches, the packet, the delta, the brief and the ledger.
FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {}
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INSTANT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RECORDED_RE = re.compile(r"^Recorded at \(UTC\): (\S+)$", re.MULTILINE)
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
ROW_RE = re.compile(r"^([0-9a-f]{64})  (\S+)  \[variant: (\w+)\]$", re.MULTILINE)
EXACT_DIGEST_RE = re.compile(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`", re.MULTILINE)
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
    record: pathlib.Path
    title: str


ACT = Act("policy-v2", "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY", "approve-policy",
          "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL",
          DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md",
          "Polaris Butlers secret-classification policy approval (public-source screening scope, version 2)")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"pwb-{act.act_type}-public-source-scope-v2-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


def frozen_table() -> str:
    """The table `FROZEN_FILE_DIGESTS` would hold for the files as they are, by script."""
    rels = [MANIFEST_REL, *PATCH_RELS.values(), PACKET_REL, DELTA_REL, BRIEF_REL, LEDGER_REL]
    lines = []
    for rel in rels:
        data = (ROOT / rel).read_bytes()
        data = PERFORMED_HEAD_RE.sub(rb"\1", data, count=1) if rel == PACKET_REL else data
        lines.append(f'    pathlib.Path("{rel.as_posix()}"): "{digest(data)}",')
    return "FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {\n" + "\n".join(lines) + "\n}"


@dataclass
class Inputs:
    """Everything validation reads, injectable for the selftest."""
    manifest: bytes
    policy: bytes            # the policy on disk
    proposed: dict[str, bytes]   # variant -> the package's proposed bytes (pre-state only)
    packet: bytes
    review: str
    stale: list[str]         # builder.check findings (pre-state only)
    not_ready: list[str]     # builder.readiness findings (pre-state only)
    predecessor: str         # digest the version-1 act names ("" when the record is absent)
    class_act: bool          # the row-7 record exists
    applied: str | None      # the variant whose row the policy on disk already is
    frozen: str | None
    frozen_digest: Callable[[pathlib.Path], str]
    frozen_files: dict[pathlib.Path, bytes]
    disposition_check: Callable[[dict[int, str]], None]


CLASS_NOT_INSTALLED = "not defined in the installed RFC-0005 text"


def readiness_after_row7(root: pathlib.Path) -> list[str]:
    """The builder's readiness, except that the row-7 act itself puts the class in force: at the
    sitting the amendment's text is installed by the install change that follows every recorder,
    so the recorder asks for the row-7 record (checked separately) and not for the installed text.
    Until row 7 is recorded the builder's finding stands."""
    found = build.readiness(root)
    if (root / CLASS_ACT_REL).is_file():
        found = [f for f in found if CLASS_NOT_INSTALLED not in f]
    return found


def live_inputs(root: pathlib.Path) -> Inputs:
    manifest = (root / MANIFEST_REL).read_bytes() if (root / MANIFEST_REL).is_file() else b""
    policy = (root / POLICY_REL).read_bytes() if (root / POLICY_REL).is_file() else b""
    rows = {variant: sha for sha, _p, variant in ROW_RE.findall(manifest.decode())}
    on_disk = digest(policy)
    applied = next((v for v, sha in rows.items() if sha == on_disk), None)
    stale: list[str] = []
    not_ready: list[str] = []
    proposed: dict[str, bytes] = {}
    if applied is None:
        stale = build.check(root)
        not_ready = readiness_after_row7(root)
        try:
            proposed = {v: build.propose(policy.decode(), v).encode() for v in build.VARIANTS}
        except ValueError as exc:
            stale.append(str(exc))
    pred = (root / V1_ACT_REL).read_text() if (root / V1_ACT_REL).is_file() else ""
    m = EXACT_DIGEST_RE.search(pred)
    files = {rel: (root / rel).read_bytes() for rel in FROZEN_FILE_DIGESTS if (root / rel).is_file()}
    review_path = root / CONFIRMATION_REVIEW_REL
    return Inputs(
        manifest=manifest, policy=policy, proposed=proposed,
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        stale=stale, not_ready=not_ready, predecessor=m.group(1) if m else "",
        class_act=(root / CLASS_ACT_REL).is_file(), applied=applied,
        frozen=FROZEN_SUBJECT, frozen_digest=lambda rel: FROZEN_FILE_DIGESTS.get(rel, ""),
        frozen_files=files,
        disposition_check=lambda findings: vs.validate_disposition(
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings),
    )


def validate(act: Act, argument: str, inp: Inputs) -> tuple[str, str, str, str]:
    """Return (variant, manifest file sha, reviewed commit, verdict) or raise ValueError."""
    if inp.frozen is None:
        raise ValueError("no confirming review is recorded: FROZEN_SUBJECT is unset, "
                         "so nothing may be recorded")
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    rows = ROW_RE.findall(inp.manifest.decode())
    if [(p, v) for _s, p, v in rows] != [(POLICY_REL.as_posix(), v) for v in build.VARIANTS]:
        raise ValueError("manifest row population differs from the four variants of the one policy subject")
    by_digest = {sha: variant for sha, _p, variant in rows}
    if len(by_digest) != len(rows):
        raise ValueError("two manifest rows carry the same digest")
    if argument not in by_digest:
        raise ValueError(f"owner argument {argument} is not a row of the manifest")
    variant = by_digest[argument]
    if inp.applied is not None and inp.applied != variant:
        raise ValueError(f"the policy on disk is already variant {inp.applied} of this manifest; the "
                         "variants are alternatives, so a second variant act is refused (changing "
                         "variant is a new owner act over a declared successor package)")
    if inp.applied is not None:
        if digest(inp.policy) != argument:
            raise ValueError(f"policy hashes to {digest(inp.policy)}, not the owner argument")
    else:
        if not inp.class_act:
            raise ValueError("the row-7 act record (RFC5-14 project-documentation) is absent; the class "
                             "is outside the closed vocabulary until it exists")
        if not SHA_RE.fullmatch(inp.predecessor):
            raise ValueError("the version-1 act record (row 1) is absent or names no exact digest")
        if inp.stale:
            raise ValueError("builder reports findings: " + "; ".join(inp.stale))
        if inp.not_ready:
            raise ValueError("; ".join(inp.not_ready))
        if digest(inp.policy) != inp.predecessor:
            raise ValueError("the policy on disk is not the version-1 act's argument; "
                             "the patch cannot be applied to anything else")
        if digest(inp.proposed.get(variant, b"")) != argument:
            raise ValueError("owner argument does not match the digest of the proposed bytes")
    for rel, current in inp.frozen_files.items():
        expected = current if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", current, count=1)
        if digest(expected) != inp.frozen_digest(rel):
            raise ValueError(f"frozen subject does not carry the presented bytes of {rel.as_posix()}")
    if HEX64_RE.search(inp.packet.decode()):
        raise ValueError("owner packet carries a 64-hex token; the argument comes only "
                         "from the manifest row")
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
        findings = vs.review_findings(inp.review)
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; only a "
                             "notes-only round clears the bytes")
        inp.disposition_check(findings)
    return variant, manifest_sha, reviewed.group(1), verdicts[0]


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


def version_of(policy: bytes) -> str:
    m = re.search(rb'"policyVersion":\s*"([^"]+)"', policy)
    return m.group(1).decode() if m else ""


def render_act(act: Act, argument: str, variant: str, date: str, manifest_sha: str, reviewed: str,
               verdict: str, sel: Selection, frozen: str, instant: str,
               superseded: str, version: str) -> str:
    adds = ", ".join(w.upper() for w in build.VARIANTS[variant]) or "neither MANIFESTO nor ARCHITECTURE"
    return f"""# Owner act — {act.title}

Date: {date}

Recorded at (UTC): {instant}

Owner: Tzeusy

Act identity: `{identity_for(act, date)}`

Act type: `{act.act_type}`

Project identity: `project:syzygy`

Artifact identity: `{POLICY_REL.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `{act.act_type}` role only,
the version-1 screening-scope act recorded at `{V1_ACT_REL.as_posix()}`. Its argument
`{superseded}` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at `{PACKET_REL.as_posix()}`, which
by design carries no digest. The package manifest has four rows, one per
variant; the owner picked exactly one. The act takes this phrase, whose
argument is the chosen row:

```text
{phrase_for(act, argument)}
```

The owner did not type the phrase. On {date} the owner answered a structured
question in the Claude Code CLI that opened "{sel.opening}" by selecting the
option below; the selection is the instruction, and it names the policy "at the
manifest row". The label and description, verbatim:

| Label | Description |
|---|---|
| "{sel.label}" | "{sel.description}" |

Chosen variant: `{variant}`.

The argument was read from the chosen row of `{MANIFEST_REL.as_posix()}`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row.

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

The policy `polaris-butlers-project-shape-secrets`, policy-owning project
`project:syzygy`, is approved at version `{version}` as the observing project's
secret-classification policy. It is the version-1 policy (the Butlers scope and
the public-source scope, byte-identical) plus one change inside
`publicSourceScope`: the RFC5-14 class `project-documentation` is classified by
the closed path rule of the variant chosen (root documents, the docs and doc
trees minus the withheld words, and the licenses tree), with the opt-in root
names {adds} {"mapped" if build.VARIANTS[variant] else "withheld"}. The class
is classified only while the in-force RFC-0005 vocabulary lists it; every
detector and the active-content rule apply unchanged to every admitted body;
`work-history` is never classified; and policy and governance text is withheld
by name only, as the package's generated lists state. `policyVersion` is the
only existing value that changes besides that scope.

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and a consent that does not list
`project-documentation` still permits no egress of it (RFC5-14). The Butlers
read gate refuses a policy on its digest first, so it keeps refusing this one
until the install change re-points the gate once, against these bytes; the
recorder does not do that. It grants no write, execution, deployment, release,
recovery, mission, autonomous or multi-user authority, widens no consent, edits
no performed record, accepts no candidate contract and amends no doctrine. It
proves no read, screening, parse, render or answer result. It is the only
variant act over this manifest: another variant needs a declared successor
package.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Public-source screening scope version 2 act — {act.act_type} — performed {date}"


def render_aggregate_block(act: Act, argument: str, variant: str, date: str, manifest_sha: str,
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
| Act type / artifact | `{act.act_type}` / `{POLICY_REL.as_posix()}` |
| Argument | SHA-256 of the artifact itself: the chosen row (variant `{variant}`) of the package manifest, recomputed at recording |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Frozen subject | `{frozen}` |
| Manifest | `{MANIFEST_REL.as_posix()}`, SHA-256 `{manifest_sha}` |
| Review outcome | `{CONFIRMATION_REVIEW_REL.as_posix()}`: `{verdict}`, its head bound to the manifest file |
| Recorded at (UTC) | `{instant}` |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: this one record is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own role only. It grants no
consent, read or egress, and the read gate is re-pointed by a separate change.
"""


def expected(act: Act, argument: str, date: str, sel: Selection, inp: Inputs, instant: str):
    sel.validate()
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    if not INSTANT_RE.fullmatch(instant) or not instant.startswith(date + "T"):
        raise ValueError("instant must be YYYY-MM-DDTHH:MM:SSZ (UTC) on the act's date")
    variant, manifest_sha, reviewed, verdict = validate(act, argument, inp)
    frozen = inp.frozen or ""
    version = version_of(inp.proposed[variant] if inp.applied is None else inp.policy)
    return (render_act(act, argument, variant, date, manifest_sha, reviewed, verdict, sel, frozen,
                       instant, inp.predecessor, version),
            render_aggregate_block(act, argument, variant, date, manifest_sha, verdict, frozen, instant))


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
              instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()} "
              "(one variant act only; a change of variant needs a declared successor package)")
        return 1
    inp = live_inputs(root)
    try:
        record, block = expected(act, argument, date, sel, inp, instant)
    except (ValueError, OSError) as exc:
        print(f"FAILED (nothing written): {exc}")
        return 1
    if inp.applied is not None:
        print("FAILED: the policy on disk already carries a variant of this manifest")
        return 1
    aggregate = (root / AGGREGATE_REL).read_text()
    if aggregate_heading(act, date) in aggregate:
        print("FAILED: aggregate record already carries this act's heading")
        return 1
    variant = next(v for sha, _p, v in ROW_RE.findall(inp.manifest.decode()) if sha == argument)
    (root / act.record).write_text(record)
    (root / AGGREGATE_REL).write_text(aggregate.rstrip() + "\n\n" + block)
    (root / POLICY_REL).write_bytes(inp.proposed[variant])
    print(f"recorded at {instant}")
    print(f"wrote {act.record.as_posix()}\nappended one section to {AGGREGATE_REL.as_posix()}\n"
          f"applied variant {variant}: {POLICY_REL.as_posix()} now hashes to the argument")
    print(f"next, in the same change: tag {tag_for(act, date)} on the commit carrying them; run "
          "scripts/install_redis_sitting.py once after every recorder (it re-points the read gate "
          "against these bytes and registers this act)")
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
    inp = live_inputs(root)
    if inp.applied is None:
        print("FAILED: the policy on disk is not the argued bytes; the act is not applied")
        return 1
    try:
        record, block = expected(act, argument, date, sel, inp, instant)
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
    print("recorded policy act matches the exact owner argument")
    return 0


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


def selftest() -> int:
    """One mutant per predicate; each must be refused for the stated reason."""
    global FROZEN_SUBJECT, FROZEN_FILE_DIGESTS
    import contextlib
    import io
    import json
    import shutil
    import tempfile
    act = ACT
    base = b'{"policyVersion": "1.2.0-public-source-candidate.1"}\n'
    proposed = {v: (b'{"policyVersion": "1.3.0-public-source-candidate.1.' + v.encode() + b'"}\n')
                for v in build.VARIANTS}
    rows = {v: digest(b) for v, b in proposed.items()}
    arg = rows["none"]
    manifest = ("# header\n" + "".join(f"{rows[v]}  {POLICY_REL.as_posix()}  [variant: {v}]\n"
                                       for v in build.VARIANTS)).encode()
    msha = digest(manifest)
    pkt = b"# Packet\n\n> Candidate - binds nothing.\n\nbody\n"
    review = (f"# R4\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, PACKET_REL: pkt, BRIEF_REL: b"brief", DELTA_REL: b"delta",
             LEDGER_REL: b"ledger", **{rel: b"patch " + v.encode() for v, rel in PATCH_RELS.items()}}

    def make(**over) -> Inputs:
        values = dict(manifest=manifest, policy=base, proposed=dict(proposed), packet=pkt, review=review,
                      stale=[], not_ready=[], predecessor=digest(base), class_act=True, applied=None,
                      frozen="f" * 40, frozen_digest=lambda rel: digest(blobs[rel]),
                      frozen_files=dict(blobs), disposition_check=lambda findings: None)
        values.update(over)
        return Inputs(**values)

    results: list[tuple[str, bool]] = []

    def refused(needle, argument, inp) -> bool:
        try:
            validate(act, argument, inp)
        except ValueError as exc:
            return needle in str(exc)
        return False

    results.append(("exact argument validates", _accepts(act, arg, make())))
    for v in build.VARIANTS:
        results.append((f"each variant row validates: {v}", _accepts(act, rows[v], make())))
        results.append((f"variant {v}, applied, validates against its own row",
                        _accepts(act, rows[v], make(policy=proposed[v], applied=v))))
    results.append(("an applied policy not hashing to the argument refused",
                    refused("hashes to", arg, make(policy=proposed["none"] + b" ", applied="none"))))
    results.append(("a second variant act refused while another variant is in force",
                    refused("second variant act", rows["both"], make(policy=proposed["none"], applied="none"))))
    results.append(("a second variant act is refused whichever variant is in force",
                    all(refused("second variant act", rows[b], make(policy=proposed[a], applied=a))
                        for a in build.VARIANTS for b in build.VARIANTS if a != b)))
    if FROZEN_SUBJECT is None:
        results.append(("the frozen table is empty while FROZEN_SUBJECT is unset", not FROZEN_FILE_DIGESTS))
    else:
        with tempfile.TemporaryDirectory() as d:
            bare = pathlib.Path(d)
            ok = bool(FROZEN_FILE_DIGESTS)
            for rel, want in FROZEN_FILE_DIGESTS.items():
                (bare / rel).parent.mkdir(parents=True, exist_ok=True)
                (bare / rel).write_bytes((ROOT / rel).read_bytes())
                cur = (bare / rel).read_bytes()
                cur = cur if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", cur, count=1)
                ok = ok and digest(cur) == want
            results.append(("frozen files verify from a copy with no git object", ok and not (bare / ".git").exists()))
    results.append(("unset FROZEN_SUBJECT refused", refused("FROZEN_SUBJECT is unset", arg, make(frozen=None))))
    results.append(("non-hex argument refused", refused("not a 64-hex", "xyz", make())))
    results.append(("an argument that is no row refused", refused("not a row", "0" * 64, make())))
    results.append(("manifest row for another subject refused",
                    refused("row population", arg, make(manifest=manifest.replace(POLICY_REL.name.encode(), b"other.json")))))
    results.append(("a manifest with a variant missing refused",
                    refused("row population", arg, make(manifest=b"\n".join(manifest.split(b"\n")[:-2]) + b"\n"))))
    results.append(("a missing row-7 act refused", refused("row-7 act record", arg, make(class_act=False))))
    results.append(("a missing version-1 act refused", refused("version-1 act record", arg, make(predecessor=""))))
    results.append(("stale builder output refused", refused("builder reports", arg, make(stale=["x"]))))
    results.append(("a package not ready for an act refused",
                    refused("not ready for an act", arg, make(not_ready=["not ready for an act: class"]))))
    results.append(("policy not at the version-1 act's argument refused",
                    refused("version-1 act's argument", arg, make(policy=base + b" "))))
    results.append(("proposed bytes not hashing to the argument refused",
                    refused("proposed bytes", arg, make(proposed=dict(proposed, none=proposed["none"] + b" ")))))
    drift = dict(blobs)
    drift[PACKET_REL] = pkt + b"x"
    results.append(("frozen file lacking the presented packet refused",
                    refused("frozen subject does not carry", arg,
                            make(frozen_digest=lambda rel: digest(drift[rel])))))
    drift = dict(blobs)
    drift[PATCH_RELS["both"]] = b"other"
    results.append(("frozen file lacking a presented patch refused",
                    refused("frozen subject does not carry", arg,
                            make(frozen_digest=lambda rel: digest(drift[rel])))))
    performed = pkt.replace(b"\n\n", b"\n\n> **PERFORMED 2026-10-04.** Recorded.\n\n", 1)
    perf_files = dict(blobs)
    perf_files[PACKET_REL] = performed
    results.append(("PERFORMED head over the frozen packet accepted",
                    _accepts(act, arg, make(packet=performed, frozen_files=perf_files))))
    results.append(("packet carrying a digest refused", refused("64-hex token", arg, make(packet=pkt + arg.encode()))))
    results.append(("review binding another manifest digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, "0" * 64)))))
    results.append(("review binding a row instead of the file digest refused",
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
    for name, sel in (("empty label", Selection("q", "", "d")),
                      ("multi-line description", Selection("q", "l", "a\nb")),
                      ("digest in opening", Selection("q " + "a" * 64, "l", "d"))):
        try:
            sel.validate()
            results.append((f"selection with {name} refused", False))
        except ValueError:
            results.append((f"selection with {name} refused", True))
    ok_sel = Selection("Approve the policy?", "Approve now", "Approve the policy at the manifest row.")
    record = block = ""
    try:
        record, block = expected(act, arg, "2026-10-04", ok_sel, make(), INSTANT_OK)
        results.append(("record and block render, naming the row and the tag",
                        arg in record and arg in block and tag_for(act, "2026-10-04") in record))
        results.append(("record carries the phrase exactly once in its ceremony",
                        record.count(phrase_for(act, arg)) == 1))
        results.append(("record names the policy version it approves",
                        "1.3.0-public-source-candidate.1.none" in record))
        results.append(("record names the chosen variant", "Chosen variant: `none`." in record))
        r2, _b2 = expected(act, rows["both"], "2026-10-04", ok_sel, make(), INSTANT_OK)
        results.append(("a different variant renders a different record", r2 != record and "Chosen variant: `both`." in r2))
    except ValueError as exc:
        print(f"  (render failure: {exc})")
        results.append(("record and block render", False))
    results.append(("bad date refused", _raises(lambda: expected(act, arg, "04/10", ok_sel, make(), INSTANT_OK))))
    results.append(("record and block carry the instant exactly once each",
                    record.count(f"Recorded at (UTC): {INSTANT_OK}") == 1 and block.count(f"`{INSTANT_OK}`") == 1))
    for name, bad in (("a date-only instant", "2026-10-04"), ("a local-offset instant", "2026-10-04T09:30:00+08:00"),
                      ("fractional seconds", "2026-10-04T09:30:00.5Z"), ("an instant on another date", "2026-10-05T00:00:00Z"),
                      ("a lowercase z", "2026-10-04T09:30:00z")):
        results.append((f"{name} refused", _raises(lambda bad=bad: expected(
            act, arg, "2026-10-04", ok_sel, make(), bad))))

    # end to end in a scratch copy with no git: freeze the scratch package to a synthetic
    # confirming review, record variant manifesto, check, refuse a repeat and a second variant
    saved = (FROZEN_SUBJECT, FROZEN_FILE_DIGESTS)
    try:
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            real_policy = (ROOT / POLICY_REL).read_text()
            v1text, _mode = build.v1_bytes(real_policy)
            (root / PKG).mkdir(parents=True)
            for sub in ("", "proposed"):
                for f in (ROOT / PKG / sub).glob("*"):
                    if f.is_file():
                        (root / PKG / sub).mkdir(parents=True, exist_ok=True)
                        shutil.copy(f, root / PKG / sub / f.name)
            (root / build.V1_MANIFEST).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / build.V1_MANIFEST, root / build.V1_MANIFEST)
            (root / POLICY_REL).parent.mkdir(parents=True, exist_ok=True)
            (root / POLICY_REL).write_text(v1text)
            (root / V1_ACT_REL).parent.mkdir(parents=True, exist_ok=True)
            (root / V1_ACT_REL).write_text(f"# v1\n\nExact digest (SHA-256): `{digest(v1text.encode())}`\n")
            (root / CLASS_ACT_REL).write_text("# row 7\n")
            # the sitting state: the row-7 record exists, the amendment text is not installed yet
            (root / AGGREGATE_REL).write_text("# Acceptance record\n")
            mf = (root / MANIFEST_REL).read_bytes()
            review_path = root / CONFIRMATION_REVIEW_REL
            review_path.parent.mkdir(parents=True, exist_ok=True)
            review_path.write_text(f"# R4 (synthetic, scratch only)\nReviewed commit: {'a' * 40}\n"
                                   f"Manifest SHA-256: {digest(mf)}\nVerdict: CONFIRM\n\n## Findings\n\nnone\n")
            rels = [MANIFEST_REL, *PATCH_RELS.values(), PACKET_REL, DELTA_REL, BRIEF_REL, LEDGER_REL]
            FROZEN_SUBJECT = "f" * 40
            FROZEN_FILE_DIGESTS = {rel: digest((root / rel).read_bytes() if rel != PACKET_REL else
                                               PERFORMED_HEAD_RE.sub(rb"\1", (root / rel).read_bytes(), count=1))
                                   for rel in rels if (root / rel).is_file()}
            rowmap = {v: sha for sha, _p, v in ROW_RE.findall(mf.decode())}
            sel = Selection("Approve the policy?", "Approve now", "Approve the policy at the manifest row.")
            with contextlib.redirect_stdout(io.StringIO()):
                (root / CLASS_ACT_REL).unlink()
                no_class = do_record(root, act, rowmap["manifesto"], "2026-10-04", sel, INSTANT_OK)
                (root / CLASS_ACT_REL).write_text("# row 7\n")
                wrote = do_record(root, act, rowmap["manifesto"], "2026-10-04", sel, INSTANT_OK)
                checked = do_check(root, act, rowmap["manifesto"], "2026-10-04", sel)
                again = do_record(root, act, rowmap["manifesto"], "2026-10-04", sel, INSTANT_OK)
                (root / act.record).rename(root / (act.record.name + ".moved"))
                other = do_record(root, act, rowmap["both"], "2026-10-04", sel, INSTANT_OK)
                (root / (act.record.name + ".moved")).rename(root / act.record)
                (root / act.record).write_text((root / act.record).read_text().replace(INSTANT_OK, "2026-10-04T09:31:00Z"))
                tampered = do_check(root, act, rowmap["manifesto"], "2026-10-04", sel)
            results.append(("recording is refused while the row-7 record is absent", no_class == 1))
            results.append(("the row-7 record stands in for the installed RFC-0005 text at recording time",
                            not (root / build.RFC5_INSTALLED).exists() and wrote == 0))
            results.append(("without the row-7 record the builder's installed-text finding stands",
                            any(CLASS_NOT_INSTALLED in f for f in (lambda r: (r.joinpath(CLASS_ACT_REL).unlink(),
                                                                              readiness_after_row7(r))[1])(root))))
            (root / CLASS_ACT_REL).write_text("# row 7\n")
            results.append(("record then check in a bare copy applies the variant and passes",
                            wrote == 0 and checked == 0 and again == 1
                            and digest((root / POLICY_REL).read_bytes()) == rowmap["manifesto"]
                            and not (root / ".git").exists()))
            results.append(("a second variant act in the same tree is refused and writes nothing",
                            other == 1 and json.loads((root / POLICY_REL).read_text())["policyVersion"].endswith(".manifesto")
                            and (root / AGGREGATE_REL).read_text().count("## Public-source screening scope version 2 act") == 1))
            results.append(("a record whose instant was altered fails the check against the block", tampered == 1))
    finally:
        FROZEN_SUBJECT, FROZEN_FILE_DIGESTS = saved
    failed = [name for name, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", metavar="ARGUMENT")
    mode.add_argument("--check", metavar="ARGUMENT")
    mode.add_argument("--freeze-table", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--instant", help="UTC instant YYYY-MM-DDTHH:MM:SSZ; --record defaults to now, --check reads it from the record")
    ap.add_argument("--question-opening")
    ap.add_argument("--selection-label")
    ap.add_argument("--selection-description")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
    if args.freeze_table:
        print(frozen_table())
        return 0
    argument = args.record or args.check
    if not (args.date and args.question_opening and args.selection_label and args.selection_description):
        print("--date, --question-opening, --selection-label and "
              "--selection-description are required", file=sys.stderr)
        return 2
    sel = Selection(args.question_opening, args.selection_label, args.selection_description)
    fn = do_record if args.record else do_check
    return fn(ROOT, ACT, argument, args.date, sel, args.instant)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
