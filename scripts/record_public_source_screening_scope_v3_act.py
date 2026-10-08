#!/usr/bin/env python3
"""Record or verify the owner's public-source screening-scope version-3 policy act.

Package `contracts/candidates/public-source-screening-scope-v3/` (register row
P-105, `syzygy-wsev`). One state-(1) `approve-policy` owner act over the
proposed secret-classification policy, whose argument is ONE of the two rows of
`PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt` (variant `all` or `non-web`).
The owner gives it by selecting an option in a structured question; the packet
(`decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`, decision 1) maps
that option to the words it offers, and no phrase is typed and no digest
appears in the packet. It supersedes, for the `approve-policy` role only, the
version-2 screening-scope act. This script performs nothing by itself.

FROZEN. Round 2 of the package review returned `CONFIRM WITH EXCEPTIONS`, notes
only, over commit `5db1dd72` (`docs/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2-RAW.md`;
notes in `ROUND-2-DISPOSITIONS.md`), which under the owner's notes-only rule
clears the package at its manifest. `FROZEN_FILE_DIGESTS` holds the SHA-256 of
each file that review read, taken from that commit by `--freeze-table 5db1dd72`,
never by hand.

ORDER. The version-2 act must be recorded and the policy on disk must be
exactly its argument. It refuses otherwise.

ONE VARIANT ONLY. The two rows are alternatives. The recorder refuses when the
policy on disk is already a row of this manifest, and when this act's record
exists.

`--record ARGUMENT --date D [--instant I] --question-opening Q
--selection-label L --selection-description S --packet-words W` requires,
before anything is written:

1. the argument is a 64-hex SHA-256 equal to one row of the manifest, the
   manifest rows are exactly the two variants of the policy, and the builder
   verifies the package against the policy on disk;
2. the policy on disk is exactly the version-2 act's argument, and the
   proposed bytes of the chosen variant hash to the argument;
3. every file the review read hashes to the digest recorded below for it (the
   packet may gain one PERFORMED head), and the packet carries no 64-hex token;
4. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE, the value the builder's --manifest-digest prints, never a row>` and a
   verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter clears the
   bytes only when every finding is a `note` and `ROUND-2-DISPOSITIONS.md`
   names the raw on a `Reviewed record:` line and dispositions every finding;
5. the owner's selection (opening, label, description) and the packet's words
   the selected option maps to are non-empty, one line each, and carry no
   64-hex digest; the words must be one of the packet's own offers.

It then writes the dedicated record (with the UTC instant of recording),
appends one `ACCEPTANCE-ACT-RECORD.md` section and applies the chosen variant's
bytes, so the policy on disk hashes to the argument. It does NOT re-point the
read gate: `scripts/install_redis_sitting.py` does that once, against the final
bytes. `--check` re-derives the record and the block after adoption, requires
the policy to hash to the argument, and counts exactly one copy of the block.
`--freeze-table [COMMIT]` prints the frozen-digest table for the files as they
are (or at COMMIT). `--selftest` mutates each predicate and requires it to fail
closed.
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_source_screening_scope_v3 as build  # noqa: E402
import record_public_source_screening_scope_v2_act as v2rec  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
PKG = build.PKG
MANIFEST_REL = build.MANIFEST
POLICY_REL = build.POLICY
PATCH_RELS = {v: build.patch_path(v) for v in build.VARIANTS}
PACKET_REL = DECISIONS / "DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md"
DELTA_REL = PKG / "SEMANTIC-DELTA.md"
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
LEDGER_REL = PKG / "IMPACT-LEDGER.md"
#: The version-2 act's performed record: the policy must be exactly its argument before this act.
V2_ACT_REL = v2rec.ACT.record
CONFIRMATION_REVIEW_REL = pathlib.Path("docs/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2-RAW.md")
DISPOSITION_REL = PKG / "ROUND-2-DISPOSITIONS.md"
#: The commit the confirming review read (provenance; binding is by the manifest digest in the raw's head).
FROZEN_SUBJECT: str | None = "5db1dd720338edd7963653f7e19ff727e1e99f32"
#: SHA-256 of each file the confirming review read, at FROZEN_SUBJECT, by `--freeze-table 5db1dd72`.
FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3/PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt"): "e5328701c62fa567d9f8dcc4d11c80266638b28bc368212b264514052bcec9e3",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3/proposed/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json.all.patch"): "66714784015bfa5ae4469f2479937f84da2c8eb43b39297e7207c27605b3d0dc",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3/proposed/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json.non-web.patch"): "96316c66e09a8cc98632d7e4179cdc5f9177ce2e4a3f48a0985966cfebbe040b",
    pathlib.Path(".syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md"): "0bd42fbba09380e024f26e016804a274a5b55623e195c26194ff1b5f170de664",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3/SEMANTIC-DELTA.md"): "8ab4d325d8738043ec7430b6fde769d656fd39329963be4a050f70ba83ace51d",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3/REVIEW-BRIEF.md"): "c5526cf65b1c0bf48e02fb9c90a57c67295cf3d938c122de02e65d79c7d4aebe",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v3/IMPACT-LEDGER.md"): "cc6e5a1e85c497b6e46bdcb7359bee40b1e3d59d2f25c732e0e45f44bef035e9",
}
#: The words the packet offers for decision 1; the owner's selection maps to exactly one.
PACKET_WORDS = ("Sign screening scope version 3, variant all", "Sign screening scope version 3, variant non-web")
VARIANT_OF_WORDS = dict(zip(PACKET_WORDS, ("all", "non-web")))
VERDICTS = v2rec.VERDICTS
DATE_RE = v2rec.DATE_RE
INSTANT_RE = v2rec.INSTANT_RE
RECORDED_RE = v2rec.RECORDED_RE
SHA_RE = v2rec.SHA_RE
HEX64_RE = v2rec.HEX64_RE
ROW_RE = re.compile(r"^([0-9a-f]{64})  (\S+)  \[variant: ([\w-]+)\]$", re.MULTILINE)
EXACT_DIGEST_RE = v2rec.EXACT_DIGEST_RE
REVIEWED_COMMIT_RE = v2rec.REVIEWED_COMMIT_RE
VERDICT_RE = v2rec.VERDICT_RE
PERFORMED_HEAD_RE = v2rec.PERFORMED_HEAD_RE
digest = v2rec.digest


@dataclass(frozen=True)
class Act:
    key: str
    label: str
    act_type: str
    identity_stem: str
    record: pathlib.Path
    title: str


ACT = Act("policy-v3", "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY", "approve-policy",
          "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-APPROVAL",
          DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md",
          "Polaris Butlers secret-classification policy approval (public-source screening scope, version 3)")


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"pwb-{act.act_type}-public-source-scope-v3-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


def frozen_rels() -> list[pathlib.Path]:
    return [MANIFEST_REL, *PATCH_RELS.values(), PACKET_REL, DELTA_REL, BRIEF_REL, LEDGER_REL]


def frozen_table(read: Callable[[pathlib.Path], bytes] | None = None) -> str:
    """The table `FROZEN_FILE_DIGESTS` would hold for the files as they are (or as `read` returns them), by script."""
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
    policy: bytes            # the policy on disk
    proposed: dict[str, bytes]   # variant -> the package's proposed bytes (pre-state only)
    packet: bytes
    review: str
    stale: list[str]         # builder.check findings
    predecessor: str         # digest the version-2 act names ("" when the record is absent)
    predecessor_date: str
    applied: str | None      # the variant whose row the policy on disk already is
    frozen: str | None
    frozen_digest: Callable[[pathlib.Path], str]
    frozen_files: dict[pathlib.Path, bytes]
    disposition_check: Callable[[dict[int, str]], None]


def live_inputs(root: pathlib.Path) -> Inputs:
    manifest = (root / MANIFEST_REL).read_bytes() if (root / MANIFEST_REL).is_file() else b""
    policy = (root / POLICY_REL).read_bytes() if (root / POLICY_REL).is_file() else b""
    rows = {variant: sha for sha, _p, variant in ROW_RE.findall(manifest.decode())}
    applied = next((v for v, sha in rows.items() if sha == digest(policy)), None)
    stale = build.check(root)
    proposed: dict[str, bytes] = {}
    if applied is None:
        try:
            base, _mode = build.base_bytes(root)
            proposed = {v: build.propose(base, v).encode() for v in build.VARIANTS}
        except (ValueError, OSError) as exc:
            stale.append(str(exc))
    pred = (root / V2_ACT_REL).read_text() if (root / V2_ACT_REL).is_file() else ""
    m = EXACT_DIGEST_RE.search(pred)
    d = re.search(r"^Date: (\d{4}-\d{2}-\d{2})$", pred, re.MULTILINE)
    files = {rel: (root / rel).read_bytes() for rel in FROZEN_FILE_DIGESTS if (root / rel).is_file()}
    review_path = root / CONFIRMATION_REVIEW_REL
    return Inputs(
        manifest=manifest, policy=policy, proposed=proposed,
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        stale=stale, predecessor=m.group(1) if m else "", predecessor_date=d.group(1) if d else "",
        applied=applied, frozen=FROZEN_SUBJECT, frozen_digest=lambda rel: FROZEN_FILE_DIGESTS.get(rel, ""),
        frozen_files=files,
        disposition_check=lambda findings: vs.validate_disposition(
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings),
    )


def validate(act: Act, argument: str, inp: Inputs) -> tuple[str, str, str, str]:
    """Return (variant, manifest file sha, reviewed commit, verdict) or raise ValueError."""
    if inp.frozen is None:
        raise ValueError("no confirming review is recorded: FROZEN_SUBJECT is unset, so nothing may be recorded")
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    rows = ROW_RE.findall(inp.manifest.decode())
    if [(p, v) for _s, p, v in rows] != [(POLICY_REL.as_posix(), v) for v in build.VARIANTS]:
        raise ValueError("manifest row population differs from the two variants of the one policy subject")
    by_digest = {sha: variant for sha, _p, variant in rows}
    if len(by_digest) != len(rows):
        raise ValueError("two manifest rows carry the same digest")
    if argument not in by_digest:
        raise ValueError(f"owner argument {argument} is not a row of the manifest")
    variant = by_digest[argument]
    if inp.applied is not None and inp.applied != variant:
        raise ValueError(f"the policy on disk is already variant {inp.applied} of this manifest; the variants are "
                         "alternatives, so a second variant act is refused")
    if inp.stale:
        raise ValueError("builder reports findings: " + "; ".join(inp.stale))
    if not SHA_RE.fullmatch(inp.predecessor) or not DATE_RE.fullmatch(inp.predecessor_date):
        raise ValueError("the version-2 act record is absent or names no exact digest and date")
    if inp.applied is not None:
        if digest(inp.policy) != argument:
            raise ValueError(f"policy hashes to {digest(inp.policy)}, not the owner argument")
    else:
        if digest(inp.policy) != inp.predecessor:
            raise ValueError("the policy on disk is not the version-2 act's argument; the patch cannot be applied "
                             "to anything else")
        if digest(inp.proposed.get(variant, b"")) != argument:
            raise ValueError("owner argument does not match the digest of the proposed bytes")
    if set(inp.frozen_files) != set(frozen_rels()):
        raise ValueError("frozen-file set is not exactly the files the review read")
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
    return variant, manifest_sha, reviewed.group(1), verdicts[0]


@dataclass(frozen=True)
class Selection:
    opening: str
    label: str
    description: str
    words: str

    def validate(self) -> None:
        for name, value in (("opening", self.opening), ("label", self.label), ("description", self.description),
                            ("packet words", self.words)):
            if not value.strip() or "\n" in value:
                raise ValueError(f"owner selection {name} must be one non-empty line")
            if HEX64_RE.search(value):
                raise ValueError(f"owner selection {name} carries a 64-hex digest")
        if self.words not in PACKET_WORDS:
            raise ValueError(f"the packet words {self.words!r} are none of the packet's offers {list(PACKET_WORDS)}")


def version_of(policy: bytes) -> str:
    m = re.search(rb'"policyVersion":\s*"([^"]+)"', policy)
    return m.group(1).decode() if m else ""


def render_act(act: Act, argument: str, variant: str, date: str, manifest_sha: str, reviewed: str,
               verdict: str, sel: Selection, frozen: str, instant: str,
               superseded: str, superseded_date: str, version: str, exempt: int) -> str:
    notes = (f" notes are dispositioned in `{DISPOSITION_REL.as_posix()}`;"
             if verdict == "CONFIRM WITH EXCEPTIONS" else " it carries no notes;")
    which = ("every one of the code-content rule's source extensions" if variant == "all"
             else "the code-content rule's source extensions outside the browser-side and server-templating list "
                  "(`.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`, `.tsx`, `.php`)")
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

Supersession / revocation: this act supersedes, for the `{act.act_type}` role only, the {superseded_date} act recorded at `{V2_ACT_REL.as_posix()}`. That is the version-2 screening-scope act. Its argument
`{superseded}` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented decision 1 of the packet at `{PACKET_REL.as_posix()}`,
which by design carries no digest. The package manifest has two rows, one per
variant; the owner picked exactly one. The act takes this phrase, whose
argument is the chosen row:

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
instruction, and the words name the variant and the manifest row.

Chosen variant: `{variant}`.

The argument was read from the chosen row of `{MANIFEST_REL.as_posix()}`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row.

Frozen provenance:

- frozen subject (package bytes): `{frozen}`;
- the manifest file hashes to `{manifest_sha}` (a container digest, no act's
  argument);
- confirmation review: `{CONFIRMATION_REVIEW_REL.as_posix()}`, verdict
  `{verdict}`, its head bound to the manifest file's SHA-256 above;{notes} the raw names
  reviewed commit `{reviewed}` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

The policy `polaris-butlers-project-shape-secrets`, policy-owning project
`project:syzygy`, is approved at version `{version}` as the observing project's
secret-classification policy. It is the version-2 policy plus one change inside
`publicSourceScope`: a body the scope classifies code-content whose final path
segment ends with one of {exempt} exempt extensions ({which}) is admitted
without the active-content scan, its success condition or the
malformed-code-context exclusion (`activeContent.codeContentExemption`). Every
detector still runs over every body; project-documentation bodies and every
other body are scanned as before; `renderRule` binds every body. The exemption
holds at a page only while the page writes the body as entity-encoded text
under an enforced Content-Security-Policy whose `default-src` is exactly
`'none'` and which carries no script-bearing directive (`renderCondition`); a
consumer that cannot confirm that scans the body as before for that page.
`policyVersion` is the only other value that changes.

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and the exemption changes no egress or consent
rule. The read gates refuse a policy on its digest first, so they keep refusing
this one until the install change re-points them once, against these bytes;
the recorder does not do that, and the screens admit nothing new until the
install change teaches them the exemption. It grants no write, execution,
deployment, release, recovery, mission, autonomous or multi-user authority,
widens no consent, edits no performed record, accepts no candidate contract
and amends no doctrine or specification. It proves no read, screening, parse,
render or answer result. It is the only variant act over this manifest.
"""


#: Section markers: the contract successor link's order check stops reading an earlier act's
#: section at the next marker, so this block's phrase cannot be read as part of it.
BLOCK_BEGIN = "<!-- PWB-POLICY-SCOPE-V3:BEGIN -->"
BLOCK_END = "<!-- PWB-POLICY-SCOPE-V3:END -->"


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Public-source screening scope version 3 act — {act.act_type} — performed {date}"


def render_aggregate_block(act: Act, argument: str, variant: str, date: str, manifest_sha: str,
                           verdict: str, frozen: str, instant: str) -> str:
    return f"""{BLOCK_BEGIN}
{aggregate_heading(act, date)}

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
consent, read or egress, and the read gates are re-pointed by a separate change.
{BLOCK_END}
"""


def expected(act: Act, argument: str, date: str, sel: Selection, inp: Inputs, instant: str):
    sel.validate()
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    if not INSTANT_RE.fullmatch(instant) or not instant.startswith(date + "T"):
        raise ValueError("instant must be YYYY-MM-DDTHH:MM:SSZ (UTC) on the act's date")
    variant, manifest_sha, reviewed, verdict = validate(act, argument, inp)
    if VARIANT_OF_WORDS[sel.words] != variant:
        raise ValueError(f"the packet words {sel.words!r} name variant {VARIANT_OF_WORDS[sel.words]}, "
                         f"not the argument's variant {variant}")
    bytes_ = inp.proposed[variant] if inp.applied is None else inp.policy
    exempt = len(build.json.loads(bytes_)[build.SCOPE_KEY]["activeContent"]["codeContentExemption"]["exemptExtensions"])
    return (render_act(act, argument, variant, date, manifest_sha, reviewed, verdict, sel, inp.frozen or "",
                       instant, inp.predecessor, inp.predecessor_date, version_of(bytes_), exempt),
            render_aggregate_block(act, argument, variant, date, manifest_sha, verdict, inp.frozen or "", instant))


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection,
              instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()} (one variant act only)")
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
    print("next, in the same change: run scripts/install_redis_sitting.py once after every recorder (it re-points "
          "the read gates against these bytes and registers this act)")
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


INSTANT_OK = "2026-10-09T09:30:00Z"


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


def selftest() -> int:
    """One mutant per predicate; each must be refused for the stated reason."""
    global FROZEN_FILE_DIGESTS
    import contextlib
    import io
    import json
    import shutil
    import tempfile
    act = ACT
    base = b'{"policyVersion": "1.3.0-public-source-candidate.1.none"}\n'
    proposed = {v: (b'{"policyVersion": "1.4.0-public-source-candidate.1.none.code-' + v.encode() + b'"}\n')
                for v in build.VARIANTS}
    rows = {v: digest(b) for v, b in proposed.items()}
    arg = rows["all"]
    manifest = ("# header\n" + "".join(f"{rows[v]}  {POLICY_REL.as_posix()}  [variant: {v}]\n"
                                       for v in build.VARIANTS)).encode()
    msha = digest(manifest)
    pkt = b"# Packet\n\n> Candidate - binds nothing.\n\nbody\n"
    review = (f"# R2\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, PACKET_REL: pkt, BRIEF_REL: b"brief", DELTA_REL: b"delta",
             LEDGER_REL: b"ledger", **{rel: b"patch " + v.encode() for v, rel in PATCH_RELS.items()}}

    def make(**over) -> Inputs:
        values = dict(manifest=manifest, policy=base, proposed=dict(proposed), packet=pkt, review=review,
                      stale=[], predecessor=digest(base), predecessor_date="2026-10-07", applied=None,
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
    results.append(("the shipped table covers exactly the files the review read",
                    set(FROZEN_FILE_DIGESTS) == set(frozen_rels())
                    and all(SHA_RE.fullmatch(d) for d in FROZEN_FILE_DIGESTS.values())))
    results.append(("an applied policy not hashing to the argument refused",
                    refused("hashes to", arg, make(policy=proposed["all"] + b" ", applied="all"))))
    results.append(("a second variant act refused while the other is in force",
                    refused("second variant act", rows["non-web"], make(policy=proposed["all"], applied="all"))))
    results.append(("unset FROZEN_SUBJECT refused", refused("FROZEN_SUBJECT is unset", arg, make(frozen=None))))
    results.append(("non-hex argument refused", refused("not a 64-hex", "xyz", make())))
    results.append(("an argument that is no row refused", refused("not a row", "0" * 64, make())))
    results.append(("manifest row for another subject refused",
                    refused("row population", arg, make(manifest=manifest.replace(POLICY_REL.name.encode(), b"other.json")))))
    results.append(("a manifest with a variant missing refused",
                    refused("row population", arg, make(manifest=b"\n".join(manifest.split(b"\n")[:-2]) + b"\n"))))
    results.append(("a missing version-2 act refused", refused("version-2 act record", arg, make(predecessor=""))))
    results.append(("stale builder output refused", refused("builder reports", arg, make(stale=["x"]))))
    results.append(("policy not at the version-2 act's argument refused",
                    refused("version-2 act's argument", arg, make(policy=base + b" "))))
    results.append(("proposed bytes not hashing to the argument refused",
                    refused("proposed bytes", arg, make(proposed=dict(proposed, all=proposed["all"] + b" ")))))
    results.append(("a frozen-file set missing the ledger refused",
                    refused("frozen-file set", arg, make(frozen_files={k: b for k, b in blobs.items() if k != LEDGER_REL}))))
    drift = dict(blobs)
    drift[PACKET_REL] = pkt + b"x"
    results.append(("frozen file lacking the presented packet refused",
                    refused("frozen subject does not carry", arg, make(frozen_digest=lambda rel: digest(drift[rel])))))
    drift = dict(blobs)
    drift[PATCH_RELS["non-web"]] = b"other"
    results.append(("frozen file lacking a presented patch refused",
                    refused("frozen subject does not carry", arg, make(frozen_digest=lambda rel: digest(drift[rel])))))
    performed = pkt.replace(b"\n\n", b"\n\n> **PERFORMED 2026-10-09.** Recorded.\n\n", 1)
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
    words = PACKET_WORDS[0]
    for name, sel in (("empty label", Selection("q", "", "d", words)),
                      ("multi-line description", Selection("q", "l", "a\nb", words)),
                      ("digest in opening", Selection("q " + "a" * 64, "l", "d", words)),
                      ("words the packet does not offer", Selection("q", "l", "d", "Sign it")),
                      ("empty packet words", Selection("q", "l", "d", ""))):
        results.append((f"selection with {name} refused", _raises(sel.validate)))
    ok_sel = Selection("Which screening policy?", "Variant all (Recommended)", "Every source extension skips the check.", words)
    results.append(("packet words naming the other variant refused",
                    _raises(lambda: expected(act, arg, "2026-10-09",
                                             Selection(ok_sel.opening, ok_sel.label, ok_sel.description, PACKET_WORDS[1]),
                                             make(), INSTANT_OK))))
    record = block = ""
    real = dict(proposed)
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / POLICY_REL).parent.mkdir(parents=True)
        shutil.copy(ROOT / POLICY_REL, root / POLICY_REL)
        (root / v2rec.build.MANIFEST).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(ROOT / v2rec.build.MANIFEST, root / v2rec.build.MANIFEST)
        (root / PKG).mkdir(parents=True, exist_ok=True)
        shutil.copytree(ROOT / PKG / "proposed", root / PKG / "proposed")
        shutil.copy(ROOT / MANIFEST_REL, root / MANIFEST_REL)
        base_text, _mode = build.base_bytes(root)
        real = {v: build.propose(base_text, v).encode() for v in build.VARIANTS}
    real_rows = {v: digest(b) for v, b in real.items()}
    real_manifest = ("# header\n" + "".join(f"{real_rows[v]}  {POLICY_REL.as_posix()}  [variant: {v}]\n"
                                            for v in build.VARIANTS)).encode()
    real_review = review.replace(msha, digest(real_manifest))
    real_inp = make(manifest=real_manifest, proposed=real, policy=base_text.encode(),
                    predecessor=digest(base_text.encode()), review=real_review,
                    frozen_files={**blobs, MANIFEST_REL: real_manifest},
                    frozen_digest=lambda rel: digest({**blobs, MANIFEST_REL: real_manifest}[rel]))
    try:
        record, block = expected(act, real_rows["all"], "2026-10-09", ok_sel, real_inp, INSTANT_OK)
        results.append(("record and block render, naming the row and the tag",
                        real_rows["all"] in record and real_rows["all"] in block and tag_for(act, "2026-10-09") in record))
        results.append(("record carries the phrase exactly once in its ceremony",
                        record.count(phrase_for(act, real_rows["all"])) == 1))
        results.append(("record names the policy version it approves and the exempt count",
                        "1.4.0-public-source-candidate.1.none.code-all" in record and "one of 25 exempt extensions" in record))
        results.append(("record quotes the selected label and the packet words it maps to",
                        f'| "{ok_sel.label}" |' in record and f'its words "{words}"' in record))
        results.append(("record names the chosen variant", "Chosen variant: `all`." in record))
        results.append(("the supersession line has the read gate's form, naming the version-2 record and argument",
                        re.search(r"^Supersession / revocation: this act supersedes, for the `approve-policy` role only, "
                                  r"the \d{4}-\d{2}-\d{2} act recorded at `" + re.escape(V2_ACT_REL.as_posix()) + r"`\.",
                                  record, re.MULTILINE) is not None and f"`{digest(base_text.encode())}`" in record))
        results.append(("no line opens with 'recorded at' but the one field (the reader's loose instant count)",
                        len(re.findall(r"^\s*recorded at\b", record, re.I | re.M)) == 1))
        results.append(("the record carries none of the other families' sweep needles",
                        not any(n in record.lower() for n in ("public-egress-", "public-repo-admission", "public-obs-",
                                                              "rfc5-project-documentation", "dossier-local-agent"))))
        results.append(("a CONFIRM record cites no dispositions file", DISPOSITION_REL.as_posix() not in record))
        r3, _b3 = expected(act, real_rows["all"], "2026-10-09", ok_sel,
                           make(**{**real_inp.__dict__, "review": real_review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
                               "none", "**Finding 1 — t** (note)\nbody")}), INSTANT_OK)
        results.append(("a notes-only CONFIRM WITH EXCEPTIONS record cites its dispositions file",
                        DISPOSITION_REL.as_posix() in r3))
        results.append(("the aggregate block is bracketed by section markers",
                        block.count(BLOCK_BEGIN) == 1 and block.count(BLOCK_END) == 1))
        nw = Selection(ok_sel.opening, "Variant non-web", "Eighteen extensions.", PACKET_WORDS[1])
        r2, _b2 = expected(act, real_rows["non-web"], "2026-10-09", nw, real_inp, INSTANT_OK)
        results.append(("the other variant renders its own record", r2 != record and "Chosen variant: `non-web`." in r2
                        and "one of 18 exempt extensions" in r2))
    except ValueError as exc:
        print(f"  (render failure: {exc})")
        results.append(("record and block render", False))
    results.append(("bad date refused", _raises(lambda: expected(act, arg, "09/10", ok_sel, make(), INSTANT_OK))))
    results.append(("record and block carry the instant exactly once each",
                    record.count(f"Recorded at (UTC): {INSTANT_OK}") == 1 and block.count(f"`{INSTANT_OK}`") == 1))
    for name, bad in (("a date-only instant", "2026-10-09"), ("a local-offset instant", "2026-10-09T09:30:00+08:00"),
                      ("an instant on another date", "2026-10-10T00:00:00Z")):
        results.append((f"{name} refused", _raises(lambda bad=bad: expected(act, arg, "2026-10-09", ok_sel, make(), bad))))

    # end to end in a scratch copy with no git: record variant all, check, refuse a repeat and the other variant
    saved = FROZEN_FILE_DIGESTS
    try:
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            for rel in (POLICY_REL, v2rec.build.MANIFEST, PACKET_REL, CONFIRMATION_REVIEW_REL):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / rel, root / rel)
            shutil.copytree(ROOT / PKG, root / PKG, dirs_exist_ok=True)
            (root / POLICY_REL).write_text(base_text)
            (root / V2_ACT_REL).write_text(f"# v2\n\nDate: 2026-10-07\n\nExact digest (SHA-256): `{digest(base_text.encode())}`\n")
            (root / AGGREGATE_REL).write_text("# Acceptance record\n")
            mf = (root / MANIFEST_REL).read_bytes()
            raw = root / CONFIRMATION_REVIEW_REL
            raw.write_text(f"# R2 (synthetic, scratch only)\nReviewed commit: {'a' * 40}\n"
                           f"Manifest SHA-256: {digest(mf)}\nVerdict: CONFIRM\n\n## Findings\n\nnone\n")
            FROZEN_FILE_DIGESTS = {rel: digest((root / rel).read_bytes()) for rel in frozen_rels()}
            rowmap = {v: sha for sha, _p, v in ROW_RE.findall(mf.decode())}
            with contextlib.redirect_stdout(io.StringIO()):
                wrote = do_record(root, act, rowmap["all"], "2026-10-09", ok_sel, INSTANT_OK)
                checked = do_check(root, act, rowmap["all"], "2026-10-09", ok_sel)
                again = do_record(root, act, rowmap["all"], "2026-10-09", ok_sel, INSTANT_OK)
                (root / act.record).rename(root / (act.record.name + ".moved"))
                other = do_record(root, act, rowmap["non-web"], "2026-10-09",
                                  Selection(ok_sel.opening, "l", "d", PACKET_WORDS[1]), INSTANT_OK)
                (root / (act.record.name + ".moved")).rename(root / act.record)
                (root / act.record).write_text((root / act.record).read_text().replace(INSTANT_OK, "2026-10-09T09:31:00Z"))
                tampered = do_check(root, act, rowmap["all"], "2026-10-09", ok_sel)
            results.append(("record then check in a bare copy applies the variant and passes",
                            wrote == 0 and checked == 0 and again == 1
                            and digest((root / POLICY_REL).read_bytes()) == rowmap["all"]
                            and not (root / ".git").exists()))
            results.append(("a second variant act in the same tree is refused and writes nothing",
                            other == 1 and json.loads((root / POLICY_REL).read_text())["policyVersion"].endswith(".code-all")
                            and (root / AGGREGATE_REL).read_text().count("## Public-source screening scope version 3 act") == 1))
            results.append(("a record whose instant was altered fails the check against the block", tampered == 1))
    finally:
        FROZEN_FILE_DIGESTS = saved
    failed = [name for name, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


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
