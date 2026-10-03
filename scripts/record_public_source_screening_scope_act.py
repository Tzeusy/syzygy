#!/usr/bin/env python3
"""Record or verify the owner's public-source screening-scope policy act.

Package `contracts/candidates/public-source-screening-scope/`. One state-(1)
`approve-policy` owner act over the proposed secret-classification policy
(`approve-policy` over the exact bytes: the current policy with the package's
patch applied), whose argument is the single row of
`PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt`. The owner gives it by selecting an
option in a structured question that names the policy "at the manifest row"
(the 2026-10-02 re-pin is the precedent); no phrase is typed and no digest
appears in any Markdown file of the package. It supersedes, for the
`approve-policy` role only, the behaviour-contract re-pin act of 2026-10-02.
This script performs nothing by itself, and it refuses to record anything
until the package has a confirming review: the frozen file digests below name
the bytes round 4 read, plus the two prose files the round-4 notes repair
touched (notes-only CONFIRM WITH EXCEPTIONS, 2026-10-03). It needs no git
object: the commit is provenance only.

`--record ARGUMENT --date D [--instant I] --question-opening Q
--selection-label L --selection-description S` requires, before anything is
written:

1. the argument is a 64-hex SHA-256 equal to the manifest's one row, and the
   builder verifies the package against the policy on disk;
2. the policy on disk is exactly the superseded act's argument and the
   package's patch applied to it hashes to the argument;
3. act-readiness: the closed exclusion-reason set is readable from the exported
   constant `GENERATION_EXCLUSION_REASONS` (the package says the symbol must
   exist before the act); the reader refuses otherwise;
4. every file the review read hashes to the digest recorded below for it (the
   packet may gain one PERFORMED head), and the packet carries no 64-hex token;
5. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE>` and a verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter
   clears the bytes only when every finding is a `note` and the sibling
   `ROUND-<n>-DISPOSITIONS.md` names the raw and dispositions every finding;
6. the owner's selection is non-empty, one line each, and carries no 64-hex
   digest.

It then writes the dedicated record (with the UTC instant of recording),
appends one `ACCEPTANCE-ACT-RECORD.md` section and applies the patch, so the
policy on disk hashes to the argument. It does NOT re-point the read gate: the
change that records the act re-points the list the package's simulation
produces (packet Q2) in the same commit, by hand. `--check` re-derives the
record and the block after adoption, requires the policy to hash to the
argument, and counts exactly one copy of the block. `--selftest` mutates each
predicate and requires it to fail closed.
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
import build_public_source_screening_scope as build  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
PKG = build.PKG
MANIFEST_REL = build.MANIFEST
PATCH_REL = build.PATCH
POLICY_REL = build.POLICY
PACKET_REL = PKG / "OWNER-DECISION-PACKET.md"
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
DELTA_REL = PKG / "SEMANTIC-DELTA.md"
LEDGER_REL = PKG / "IMPACT-LEDGER.md"
CONFIRMATION_REVIEW_REL = PKG / "reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-4-RAW.md"
DISPOSITION_REL = PKG / "ROUND-4-DISPOSITIONS.md"
PREDECESSOR_REL = DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md"
#: The commit at which the table below was taken from the package. Provenance
#: only: validation never reads git. None until a round clears the bytes; while
#: None every `--record` is refused.
FROZEN_SUBJECT: str | None = "02c37988264d77d7a3114895a49c34795aba45b7"
#: SHA-256 of each file the confirming review read (the manifest and the patch
#: are byte-identical to the reviewed ones; the ledger and the brief carry the
#: round-4 notes repairs dispositioned in ROUND-4-DISPOSITIONS.md), taken by
#: script, never transcribed.
FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {
    MANIFEST_REL: "1cbf45a0da07a4cf769a17b6ac98960c6ae214c2d88a4f974e7b9d5026bc4f83",
    PATCH_REL: "0f3c6bd0a81f4b51b4ee500a260046ace6d68d164d44e4050da58be77a2eae03",
    PACKET_REL: "299d07b4519d230a77157d10258ca8fdc103951d635e4ebd701be90a79156655",
    BRIEF_REL: "ba6529c4df37ebc02dfa0d82e0ce88aa47f18bd9bf743bfd082df8e7a036a634",
    DELTA_REL: "2df12f215b0ff9994ff35e138bdd7e561870f17b5521fc2acea4b6692b92f3ce",
    LEDGER_REL: "56f81e0292160e55889183a2909b57c03521d631ebc9b283ffdcf74f8cdac0da",
}
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
#: The moment of recording, UTC, whole seconds (see the admission recorders).
INSTANT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RECORDED_RE = re.compile(r"^Recorded at \(UTC\): (\S+)$", re.MULTILINE)
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
ROW_RE = re.compile(r"^([0-9a-f]{64})  (\S+)$", re.MULTILINE)
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


ACT = Act("policy", "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY", "approve-policy",
          "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL",
          DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md",
          "Polaris Butlers secret-classification policy approval (public-source screening scope)")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"pwb-{act.act_type}-public-source-scope-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


@dataclass
class Inputs:
    """Everything validation reads, injectable for the selftest."""
    manifest: bytes
    policy: bytes            # the policy on disk
    proposed: bytes          # the package's patch applied to the policy on disk (pre-state only)
    packet: bytes
    review: str
    stale: list[str]         # builder.check findings (pre-state only)
    not_ready: list[str]     # builder.readiness findings (pre-state only)
    predecessor: str         # digest the superseded act names
    applied: bool            # the policy on disk is already the proposed bytes
    frozen: str | None
    frozen_digest: Callable[[pathlib.Path], str]
    frozen_files: dict[pathlib.Path, bytes]
    disposition_check: Callable[[dict[int, str]], None]


def live_inputs(root: pathlib.Path) -> Inputs:
    manifest = (root / MANIFEST_REL).read_bytes() if (root / MANIFEST_REL).is_file() else b""
    policy = (root / POLICY_REL).read_bytes() if (root / POLICY_REL).is_file() else b""
    rows = ROW_RE.findall(manifest.decode())
    applied = bool(rows) and digest(policy) == rows[0][0] and build.SCOPE_KEY in policy.decode()
    stale: list[str] = []
    not_ready: list[str] = []
    proposed = b""
    if not applied:
        stale = build.check(root)
        not_ready = build.readiness(root)
        try:
            proposed = build.propose(policy.decode()).encode()
        except ValueError as exc:
            stale.append(str(exc))
    pred = (root / PREDECESSOR_REL).read_text() if (root / PREDECESSOR_REL).is_file() else ""
    m = EXACT_DIGEST_RE.search(pred)
    files = {rel: (root / rel).read_bytes() for rel in FROZEN_FILE_DIGESTS if (root / rel).is_file()}
    review_path = root / CONFIRMATION_REVIEW_REL
    return Inputs(
        manifest=manifest, policy=policy, proposed=proposed,
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        stale=stale, not_ready=not_ready, predecessor=m.group(1) if m else "", applied=applied,
        frozen=FROZEN_SUBJECT, frozen_digest=lambda rel: FROZEN_FILE_DIGESTS.get(rel, ""),
        frozen_files=files,
        disposition_check=lambda findings: vs.validate_disposition(
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings),
    )


def validate(act: Act, argument: str, inp: Inputs) -> tuple[str, str, str]:
    """Return (manifest file sha, reviewed commit, verdict) or raise ValueError."""
    if inp.frozen is None:
        raise ValueError("no confirming review is recorded: FROZEN_SUBJECT is unset, "
                         "so nothing may be recorded")
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    rows = ROW_RE.findall(inp.manifest.decode())
    if [path for _sha, path in rows] != [POLICY_REL.as_posix()]:
        raise ValueError("manifest row population differs from the one policy subject")
    row = rows[0][0]
    if row != argument:
        raise ValueError(f"owner argument {argument} is not the manifest row {row}")
    if inp.applied:
        if digest(inp.policy) != argument:
            raise ValueError(f"policy hashes to {digest(inp.policy)}, not the owner argument")
    else:
        if inp.stale:
            raise ValueError("builder reports findings: " + "; ".join(inp.stale))
        if inp.not_ready:
            raise ValueError("; ".join(inp.not_ready))
        if not SHA_RE.fullmatch(inp.predecessor) or digest(inp.policy) != inp.predecessor:
            raise ValueError("the policy on disk is not the superseded act's argument; "
                             "the patch cannot be applied to anything else")
        if digest(inp.proposed) != argument:
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


def version_of(policy: bytes) -> str:
    m = re.search(rb'"policyVersion":\s*"([^"]+)"', policy)
    return m.group(1).decode() if m else ""


def render_act(act: Act, argument: str, date: str, manifest_sha: str, reviewed: str,
               verdict: str, sel: Selection, frozen: str, instant: str,
               superseded: str, version: str) -> str:
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
the 2026-10-02 act recorded at `{PREDECESSOR_REL.as_posix()}`. Its argument
`{superseded}` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at `{PACKET_REL.as_posix()}`, which
by design carries no digest. The act takes this phrase, whose argument is the
row of the package manifest:

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

The argument was read from the row of `{MANIFEST_REL.as_posix()}`, re-derived
from the builder's proposed bytes at recording, and, after the package's patch
was applied in the same change, matched the policy on disk. A swapped argument
would have been refused: the recorder rejects an argument that is not the row.

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
secret-classification policy: the base scope for the pair
(`project:syzygy`, `repository:butlers-configured-poc`) and the one content class
`declared-project-shape-text` is byte-identical to the bytes the superseded act
approved, and the policy gains one additive top-level object,
`publicSourceScope`, for admitted public repositories. That scope classifies
only into `code-structure`, `code-content` and `derived-composites`, never
`work-history`; every other admitted blob is indeterminate and excluded from
reading and egress; every detector and the active-content rule apply unchanged;
and the closed exclusion-reason set is the values of the exported constant
`GENERATION_EXCLUSION_REASONS`, which the recorder required to be readable
before recording. `policyVersion` is the only existing value that changes.

## What this act does not authorize

This act is the policy authority PWB-REQ-005 and the public-source scope need
and satisfies only its own. It names no repository and grants no observation
consent, no read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025). The Butlers read gate refuses a policy on its
digest first, so it keeps refusing this one until the change that records this
act re-points the gate as the packet's Q2 describes; the recorder does not do
that. It grants no write, execution, deployment, release, recovery, mission,
autonomous or multi-user authority, widens no consent, edits no performed
record, accepts no candidate contract and amends no doctrine. It proves no
read, screening, parse, render or answer result.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Public-source screening scope act — {act.act_type} — performed {date}"


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
| Act type / artifact | `{act.act_type}` / `{POLICY_REL.as_posix()}` |
| Argument | SHA-256 of the artifact itself: the row of the package manifest, recomputed at recording |
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
    manifest_sha, reviewed, verdict = validate(act, argument, inp)
    frozen = inp.frozen or ""
    superseded = inp.predecessor
    version = version_of(inp.proposed if not inp.applied else inp.policy)
    return (render_act(act, argument, date, manifest_sha, reviewed, verdict, sel, frozen, instant,
                       superseded, version),
            render_aggregate_block(act, argument, date, manifest_sha, verdict, frozen, instant))


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
              instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()}")
        return 1
    inp = live_inputs(root)
    try:
        record, block = expected(act, argument, date, sel, inp, instant)
    except (ValueError, OSError) as exc:
        print(f"FAILED (nothing written): {exc}")
        return 1
    if inp.applied:
        print("FAILED: the policy on disk already carries the proposed bytes")
        return 1
    aggregate = (root / AGGREGATE_REL).read_text()
    if aggregate_heading(act, date) in aggregate:
        print("FAILED: aggregate record already carries this act's heading")
        return 1
    (root / act.record).write_text(record)
    (root / AGGREGATE_REL).write_text(aggregate.rstrip() + "\n\n" + block)
    (root / POLICY_REL).write_bytes(inp.proposed)
    print(f"recorded at {instant}")
    print(f"wrote {act.record.as_posix()}\nappended one section to {AGGREGATE_REL.as_posix()}\n"
          f"applied the patch: {POLICY_REL.as_posix()} now hashes to the argument")
    print(f"next, in the same change: tag {tag_for(act, date)} on the commit carrying them; "
          "re-point the read gate and the pins the package's simulation lists (packet Q2); "
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
    inp = live_inputs(root)
    if not inp.applied:
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
    import contextlib
    import io
    import shutil
    import tempfile
    act = ACT
    base = b'{"policyVersion": "1.1.0-candidate.1"}\n'
    proposed = b'{"policyVersion": "1.2.0-public-source-candidate.1", "publicSourceScope": {}}\n'
    arg = digest(proposed)
    manifest = (f"# header\n{arg}  {POLICY_REL.as_posix()}\n").encode()
    msha = digest(manifest)
    pkt = b"# Packet\n\n> Candidate - binds nothing.\n\nbody\n"
    review = (f"# R5\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, PACKET_REL: pkt, BRIEF_REL: b"brief", DELTA_REL: b"delta",
             LEDGER_REL: b"ledger", PATCH_REL: b"patch"}

    def make(**over) -> Inputs:
        values = dict(manifest=manifest, policy=base, proposed=proposed, packet=pkt, review=review,
                      stale=[], not_ready=[], predecessor=digest(base), applied=False,
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
    results.append(("an applied policy validates against the argument",
                    _accepts(act, arg, make(policy=proposed, applied=True))))
    results.append(("an applied policy not hashing to the argument refused",
                    refused("hashes to", arg, make(policy=proposed + b" ", applied=True))))
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
        results.append(("frozen files verify from a copy with no git object", ok and not (bare / ".git").exists()))
    results.append(("unset FROZEN_SUBJECT refused", refused("FROZEN_SUBJECT is unset", arg, make(frozen=None))))
    results.append(("non-hex argument refused", refused("not a 64-hex", "xyz", make())))
    results.append(("wrong argument refused", refused("manifest row", "0" * 64, make())))
    results.append(("manifest row for another subject refused",
                    refused("row population", arg, make(manifest=manifest.replace(POLICY_REL.name.encode(), b"other.json")))))
    results.append(("stale builder output refused", refused("builder reports", arg, make(stale=["x"]))))
    results.append(("a package not act-ready refused",
                    refused("not ready for an act", arg, make(not_ready=["not ready for an act: no constant"]))))
    results.append(("policy not at the superseded act's argument refused",
                    refused("superseded act's argument", arg, make(policy=base + b" "))))
    results.append(("a missing predecessor digest refused",
                    refused("superseded act's argument", arg, make(predecessor=""))))
    results.append(("proposed bytes not hashing to the argument refused",
                    refused("proposed bytes", arg, make(proposed=proposed + b" "))))
    drift = dict(blobs)
    drift[PACKET_REL] = pkt + b"x"
    results.append(("frozen file lacking the presented packet refused",
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
                        "1.2.0-public-source-candidate.1" in record))
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

    # end to end in a scratch copy with no git: record, check, refuse a repeat;
    # and refuse while the exclusion-reason constant is absent
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        for rel in (PKG, build.PIPELINE.parent):
            shutil.copytree(ROOT / rel, root / rel)
        for rel in (POLICY_REL, PREDECESSOR_REL):
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / rel, root / rel)
        (root / AGGREGATE_REL).write_text("# Acceptance record\n")
        gs = root / build.GENERATION_SOURCE
        real_arg = ROW_RE.findall((root / MANIFEST_REL).read_text())[0][0]
        sel = Selection("Approve the policy?", "Approve now", "Approve the policy at the manifest row.")
        gs.write_text("export const OTHER = ['a'] as const;\n")
        with contextlib.redirect_stdout(io.StringIO()):
            refused_unready = do_record(root, act, real_arg, "2026-10-04", sel, INSTANT_OK)
        results.append(("recording refused while the exclusion-reason constant is absent",
                        refused_unready == 1 and not (root / act.record).exists()
                        and digest((root / POLICY_REL).read_bytes()) != real_arg))
        gs.write_text(f"export const {build.EXCLUSION_REASON_SYMBOL['symbol']} = ['oversize-source-excluded', 'empty-file'] as const;\n")
        with contextlib.redirect_stdout(io.StringIO()):
            wrote = do_record(root, act, real_arg, "2026-10-04", sel, INSTANT_OK)
            checked = do_check(root, act, real_arg, "2026-10-04", sel)
            again = do_record(root, act, real_arg, "2026-10-04", sel, INSTANT_OK)
            (root / act.record).write_text((root / act.record).read_text().replace(INSTANT_OK, "2026-10-04T09:31:00Z"))
            tampered = do_check(root, act, real_arg, "2026-10-04", sel)
        results.append(("record then check in a bare copy applies the patch and passes",
                        wrote == 0 and checked == 0 and again == 1
                        and digest((root / POLICY_REL).read_bytes()) == real_arg
                        and not (root / ".git").exists()))
        results.append(("a record whose instant was altered fails the check against the block", tampered == 1))
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
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--instant", help="UTC instant YYYY-MM-DDTHH:MM:SSZ; --record defaults to now, --check reads it from the record")
    ap.add_argument("--question-opening")
    ap.add_argument("--selection-label")
    ap.add_argument("--selection-description")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
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
