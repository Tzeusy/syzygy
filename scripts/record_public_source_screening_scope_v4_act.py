#!/usr/bin/env python3
"""Record or verify the owner's public-source screening-scope version-4 policy act.

Package `contracts/candidates/public-source-screening-scope-v4/` (register row
P-110, `syzygy-olmr`; recorder bead `syzygy-3sjj`). One state-(1)
`approve-policy` owner act over the proposed secret-classification policy,
whose argument is ONE of the two rows of
`PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt` (variant `span` or
`span-guides`). The owner gives it in words: the package's
`OWNER-DECISION-PACKET.md` offers "Sign screening scope version 4, variant
span-guides" and, in the same table, variant `span`; the owner's words name the
variant, and the variant names the manifest row. No digest is typed and none
appears in the packet. It supersedes, for the `approve-policy` role only, the
version-3 screening-scope act. This script performs nothing by itself.

FROZEN. Round 4 of the package review returned `CONFIRM WITH EXCEPTIONS`, five
findings, all `note`, over commit `65edb1cb`
(`docs/reviews/R-OLMR-SCREENING-SCOPE-V4-4-RAW.md`; notes in
`ROUND-4-DISPOSITIONS.md`), which under the owner's notes-only rule clears the
package at its manifest. `FROZEN_FILE_DIGESTS` holds the SHA-256 of each file
that review read (every package file then present, and the builder), taken
from that commit by `--freeze-table 65edb1cb`, never by hand. That commit is
unreachable from `main` (rebase-merged); binding is by the manifest digest in
the raw's head, and the commit is provenance only.

ORDER. The version-3 act must be recorded, the policy on disk must be exactly
its argument, and this act's instant must fall after the version-3 record's.
It refuses otherwise.

ONE VARIANT ONLY. The two rows are alternatives. The recorder refuses when the
policy on disk is already a row of this manifest, and when this act's record
exists.

`--record ARGUMENT --date D [--instant I] --owner-words W` requires, before
anything is written:

1. the argument is a 64-hex SHA-256 equal to one row of the manifest, the
   manifest rows are exactly the two variants of the policy, and the builder
   verifies the package against the policy on disk;
2. the policy on disk is exactly the version-3 act's argument, and the
   proposed bytes of the chosen variant hash to the argument;
3. every file the review read hashes to the digest recorded below for it (the
   packet may gain one PERFORMED head), the packet carries no 64-hex token,
   and the packet's variant table carries the chosen variant's row;
4. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE, the value the builder's --manifest-digest prints, never a row>` and a
   verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter clears the
   bytes only when every finding is a `note` and `ROUND-4-DISPOSITIONS.md`
   names the raw on a `Reviewed record:` line and dispositions every finding
   by number (`record_versioned_signoff.validate_disposition`);
5. the owner's words are one non-empty line, carry no 64-hex digest, are
   exactly one of `OWNER_WORDS`, and name the argument's variant.

It then writes the dedicated record (with the UTC instant of recording),
appends one `ACCEPTANCE-ACT-RECORD.md` section and applies the chosen variant's
bytes, so the policy on disk hashes to the argument. It does NOT re-point the
read gates or install anything: that is a separate change. `--check`
re-derives the record and the block after adoption, requires the policy to
hash to the argument, and counts exactly one copy of the block.
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
import build_public_source_screening_scope_v4 as build  # noqa: E402
import record_public_source_screening_scope_v3_act as v3rec  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = v3rec.DECISIONS
AGGREGATE_REL = v3rec.AGGREGATE_REL
PKG = build.PKG
MANIFEST_REL = build.MANIFEST
POLICY_REL = build.POLICY
PATCH_RELS = {v: build.patch_path(v) for v in build.VARIANTS}
PACKET_REL = PKG / "OWNER-DECISION-PACKET.md"
DELTA_REL = PKG / "SEMANTIC-DELTA.md"
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
LEDGER_REL = PKG / "IMPACT-LEDGER.md"
#: The earlier rounds' records the round-4 reviewer was given (raw lines 7-14).
ROUND_RELS = tuple(PKG / name for name in (
    "ROUND-1-DISPOSITIONS.md", "ROUND-2-DISPOSITIONS.md", "ROUND-2-REPAIR.md",
    "ROUND-3-DISPOSITIONS.md", "ROUND-3-OWNER-DIRECTION.md", "ROUND-3-REPAIR.md"))
BUILDER_REL = pathlib.Path("scripts/build_public_source_screening_scope_v4.py")
#: The version-3 act's performed record: the policy must be exactly its argument before this act.
V3_ACT_REL = v3rec.ACT.record
CONFIRMATION_REVIEW_REL = pathlib.Path("docs/reviews/R-OLMR-SCREENING-SCOPE-V4-4-RAW.md")
DISPOSITION_REL = PKG / "ROUND-4-DISPOSITIONS.md"
#: The commit the confirming review read (provenance; binding is by the manifest digest in the raw's head).
FROZEN_SUBJECT: str | None = "65edb1cbbec97384afd7b71e9c069736c89d767c"
#: SHA-256 of each file the confirming review read, at FROZEN_SUBJECT, by `--freeze-table 65edb1cb`.
FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt"): "0621d646f91ef3b5572d882f4bb17f5bd0785d316b30516693e48884365157ec",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/proposed/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json.span.patch"): "8c69fa54d1116a9dbdf76ed086560a87874f9c43777bf48f4c6cf20310eeeb25",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/proposed/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json.span-guides.patch"): "0d28caefaca3093c82fd25e986cb25646222083867571048970238c94f23b994",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/OWNER-DECISION-PACKET.md"): "d80f359d8feecfb0f3e283760e9fe6b327a4b8e0d1072b9764e706a86d51ecd7",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/SEMANTIC-DELTA.md"): "28d9aa9e8ccd5d0cac2474eed2a31d3e984f521d645ff1725bb923e3b864b44d",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/REVIEW-BRIEF.md"): "815ed7ef3b85a6da9ccf9bbbb34e8bba38c6993f3b6aacc59abfb19cb8357e75",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/IMPACT-LEDGER.md"): "6a281d976215abf6e6182e387d53fd304f3719c9bc53e096e5aed32303528a32",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-1-DISPOSITIONS.md"): "f958249cb87a5f293d7fcdc92f75f2a6663919cee13ee4e29bddd03fdabae2d1",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-2-DISPOSITIONS.md"): "1a2c866ec6bf9eded9e4514ac88d13ec1a19c184393191ee1cd2209813671f72",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-2-REPAIR.md"): "92b12e148a6a28f3d82176423489c01a59fa4bc99454a685925bc1dda001c5ea",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-3-DISPOSITIONS.md"): "d7309a409436cc6b3a955de7ab023d7455fc9e209ae00a5db528280ed3c8ea80",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-3-OWNER-DIRECTION.md"): "2da0c18701a9550d771a8baf0509d1e36e823f77cb32099ce6af8e8cdc517725",
    pathlib.Path(".syzygy/governance/contracts/candidates/public-source-screening-scope-v4/ROUND-3-REPAIR.md"): "ae04fb3049de15239b55d049227703ff876fe9e45f74905d7f16da9b2cb23b8e",
    pathlib.Path("scripts/build_public_source_screening_scope_v4.py"): "92dd6765b0f7a16b2d1ea9e69df7d55aca2a1c9b03424ca6f003c2d094ea6713",
}
#: The words the packet offers: its quoted words for `span-guides` (packet line 49-50) and the same form for
#: the table's other variant `span` (packet line 46; ROUND-4-DISPOSITIONS.md's offer line). Decline takes no act.
OWNER_WORDS = tuple(f"Sign screening scope version 4, variant {v}" for v in build.VARIANTS)
VARIANT_OF_WORDS = dict(zip(OWNER_WORDS, build.VARIANTS))
VERDICTS = v3rec.VERDICTS
DATE_RE = v3rec.DATE_RE
INSTANT_RE = v3rec.INSTANT_RE
RECORDED_RE = v3rec.RECORDED_RE
SHA_RE = v3rec.SHA_RE
HEX64_RE = v3rec.HEX64_RE
ROW_RE = v3rec.ROW_RE
EXACT_DIGEST_RE = v3rec.EXACT_DIGEST_RE
REVIEWED_COMMIT_RE = v3rec.REVIEWED_COMMIT_RE
VERDICT_RE = v3rec.VERDICT_RE
PERFORMED_HEAD_RE = v3rec.PERFORMED_HEAD_RE
digest = v3rec.digest


@dataclass(frozen=True)
class Act:
    key: str
    label: str
    act_type: str
    identity_stem: str
    record: pathlib.Path
    title: str


ACT = Act("policy-v4", v3rec.ACT.label, "approve-policy",
          "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL",
          DECISIONS / "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-ACT.md",
          "Polaris Butlers secret-classification policy approval (public-source screening scope, version 4)")


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"pwb-{act.act_type}-public-source-scope-v4-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


def frozen_rels() -> list[pathlib.Path]:
    return [MANIFEST_REL, *PATCH_RELS.values(), PACKET_REL, DELTA_REL, BRIEF_REL, LEDGER_REL, *ROUND_RELS,
            BUILDER_REL]


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
    predecessor: str         # digest the version-3 act names ("" when the record is absent)
    predecessor_date: str
    predecessor_instant: str
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
    pred = (root / V3_ACT_REL).read_text() if (root / V3_ACT_REL).is_file() else ""
    m = EXACT_DIGEST_RE.findall(pred)
    d = re.findall(r"^Date: (\d{4}-\d{2}-\d{2})$", pred, re.MULTILINE)
    i = RECORDED_RE.findall(pred)
    files = {rel: (root / rel).read_bytes() for rel in frozen_rels() if (root / rel).is_file()}
    review_path = root / CONFIRMATION_REVIEW_REL
    return Inputs(
        manifest=manifest, policy=policy, proposed=proposed,
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        stale=stale,
        # exactly one of each, or the record is treated as naming none
        predecessor=m[0] if len(m) == 1 else "", predecessor_date=d[0] if len(d) == 1 else "",
        predecessor_instant=i[0] if len(i) == 1 else "",
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
    if (not SHA_RE.fullmatch(inp.predecessor) or not DATE_RE.fullmatch(inp.predecessor_date)
            or not INSTANT_RE.fullmatch(inp.predecessor_instant)):
        raise ValueError("the version-3 act record is absent or does not name exactly one digest, date and instant")
    if inp.applied is not None:
        if digest(inp.policy) != argument:
            raise ValueError(f"policy hashes to {digest(inp.policy)}, not the owner argument")
    else:
        if digest(inp.policy) != inp.predecessor:
            raise ValueError("the policy on disk is not the version-3 act's argument; the patch cannot be applied "
                             "to anything else")
        if digest(inp.proposed.get(variant, b"")) != argument:
            raise ValueError("owner argument does not match the digest of the proposed bytes")
    if set(inp.frozen_files) != set(frozen_rels()):
        raise ValueError("frozen-file set is not exactly the files the review read")
    for rel, current in inp.frozen_files.items():
        expected_bytes = current if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", current, count=1)
        if digest(expected_bytes) != inp.frozen_digest(rel):
            raise ValueError(f"frozen subject does not carry the presented bytes of {rel.as_posix()}")
    packet = inp.packet.decode()
    if HEX64_RE.search(packet):
        raise ValueError("owner packet carries a 64-hex token; the argument comes only from the manifest row")
    if not re.search(r"^\| `" + re.escape(variant) + r"` \|", packet, re.MULTILINE):
        raise ValueError(f"owner packet's variant table carries no row for variant {variant}; it was not offered")
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
    findings = vs.review_findings(inp.review)
    bad = {n: s for n, s in findings.items() if s != "note"}
    if bad:
        raise ValueError(f"review carries non-note findings {bad}; only a notes-only round clears the bytes")
    if verdicts[0] == "CONFIRM WITH EXCEPTIONS":
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        inp.disposition_check(findings)
    return variant, manifest_sha, reviewed.group(1), verdicts[0]


def validate_words(words: str) -> None:
    if not words.strip() or "\n" in words or "\r" in words:
        raise ValueError("owner words must be one non-empty line")
    if HEX64_RE.search(words):
        raise ValueError("owner words carry a 64-hex digest")
    if words not in OWNER_WORDS:
        raise ValueError(f"the owner words {words!r} are none of the packet's offers {list(OWNER_WORDS)}")


def version_of(policy: bytes) -> str:
    return v3rec.version_of(policy)


def effect_of(policy: bytes, variant: str) -> str:
    """The effect paragraph, from the approved bytes' own values, never from prose held here."""
    try:
        doc = build.json.loads(policy)
        red = doc[build.SCOPE_KEY]["secretRedaction"]
        whole = ", ".join(f"`{d}`" for d in red["wholeArtifactDetectors"])
        classes = ", ".join(f"`{c}`" for c in red["redactedClasses"])
        guard = red["guardLines"]
        red["redactionClass"], red["wholeArtifactFragments"]  # noqa: B018 - read before rendering
        rule = build.doc_rule(doc[build.SCOPE_KEY]) if variant == "span-guides" else None
        if rule is not None:
            rule["rootGuideStems"], rule["rootGuideSuffixes"]  # noqa: B018
    except (ValueError, KeyError, TypeError, StopIteration) as exc:
        raise ValueError(f"the approved bytes do not carry the version-4 values the record names: {exc!r}") from exc
    text = (f"It is the version-3 policy plus one change inside `publicSourceScope`, the new object "
            f"`secretRedaction`: a body of class {classes} in which a detector matches is retained as "
            f"`{red['redactionClass']}` (RFC5-17) instead of excluded whole, when none of its matches is from "
            f"{whole}, no line matches `wholeArtifactLinePattern` and the body holds none of the "
            f"{len(red['wholeArtifactFragments'])} `wholeArtifactFragments`. Every match from every offset counts; "
            f"each line a match touches, and {guard} guard line(s) on each side, is withheld; every detector runs "
            "again over the retained text and any match there excludes the body whole; a cited span that includes a "
            "withheld line is withheld whole. Every other class, code-content included, is excluded whole on any "
            "match as before, and the active-content scan is unchanged. The scope's `detectors` and "
            "`inheritedRules` sentences each name the exception once.")
    if rule is not None:
        sfx = ", ".join(f"`{s}`" for s in rule["rootGuideSuffixes"])
        text += (f" Variant `span-guides` also lets the project-documentation root-document rule admit "
                 f"{len(rule['rootGuideStems'])} root guide names (`rootGuideStems`), only with a suffix from "
                 f"`rootGuideSuffixes` ({sfx}).")
    else:
        text += " Variant `span` leaves every content-classification rule as version 3 has it."
    return text + " `policyVersion` is the only other value that changes."


def render_act(act: Act, argument: str, variant: str, date: str, manifest_sha: str, reviewed: str,
               verdict: str, words: str, frozen: str, instant: str,
               superseded: str, superseded_date: str, version: str, effect: str) -> str:
    notes = (f" notes are dispositioned in `{DISPOSITION_REL.as_posix()}`;"
             if verdict == "CONFIRM WITH EXCEPTIONS" else " it carries no notes;")
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
explicitly given by the owner's words recorded below

Supersession / revocation: this act supersedes, for the `{act.act_type}` role only, the {superseded_date} act recorded at `{V3_ACT_REL.as_posix()}`. That is the version-3 screening-scope act. Its argument
`{superseded}` was the policy's exact digest until this act's patch was
applied. That record, its digest, its tag and the bytes it bound remain
immutable history. This act is revoked only by a later exact owner act naming
it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the packet at `{PACKET_REL.as_posix()}`, which by
design carries no digest. Its one question offers two variants and decline;
the package manifest has two rows, one per variant, and the owner named
exactly one. The act takes this phrase, whose argument is the chosen row:

```text
{phrase_for(act, argument)}
```

The owner did not type the phrase. On {date} the owner gave these words,
verbatim, in the Claude Code CLI session:

> {words}

The words name the variant, and the variant names the manifest row.

Chosen variant: `{variant}`.

The argument was read from the chosen row of `{MANIFEST_REL.as_posix()}`,
re-derived from the builder's proposed bytes for that variant at recording,
and, after the variant's patch was applied in the same change, matched the
policy on disk. A swapped argument would have been refused: the recorder
rejects an argument that is not a row, and words that name the other variant.

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
secret-classification policy. {effect}

## What this act does not authorize

This act is the policy authority the public-source scope needs and satisfies
only its own. It names no repository and grants no observation consent, no
read, no egress and no provider call: each takes its own act
(REQ-polaris-generation-025), and the redaction changes no egress or consent
rule. The read gates refuse a policy on its digest first, so they keep refusing
this one until the install change re-points them once, against these bytes;
the recorder does not do that, and the screens redact nothing until the
install change teaches them the rule. It grants no write, execution,
deployment, release, recovery, mission, autonomous or multi-user authority,
widens no consent, edits no performed record, accepts no candidate contract
and amends no doctrine or specification. It proves no read, screening, parse,
render or answer result. It is the only variant act over this manifest.
"""


#: Section markers: an order check stops reading an earlier act's section at the next marker,
#: so this block's phrase cannot be read as part of it.
BLOCK_BEGIN = "<!-- PWB-POLICY-SCOPE-V4:BEGIN -->"
BLOCK_END = "<!-- PWB-POLICY-SCOPE-V4:END -->"


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Public-source screening scope version 4 act — {act.act_type} — performed {date}"


def render_aggregate_block(act: Act, argument: str, variant: str, date: str, manifest_sha: str,
                           verdict: str, frozen: str, instant: str) -> str:
    return f"""{BLOCK_BEGIN}
{aggregate_heading(act, date)}

**Phrase the act takes (given {date} by the owner's words, not typed as a
phrase; see the dedicated record):**

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


def expected(act: Act, argument: str, date: str, words: str, inp: Inputs, instant: str):
    validate_words(words)
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    if not INSTANT_RE.fullmatch(instant) or not instant.startswith(date + "T"):
        raise ValueError("instant must be YYYY-MM-DDTHH:MM:SSZ (UTC) on the act's date")
    variant, manifest_sha, reviewed, verdict = validate(act, argument, inp)
    if instant <= inp.predecessor_instant:
        raise ValueError(f"instant {instant} is not after the version-3 act's {inp.predecessor_instant}")
    if VARIANT_OF_WORDS[words] != variant:
        raise ValueError(f"the owner words {words!r} name variant {VARIANT_OF_WORDS[words]}, "
                         f"not the argument's variant {variant}")
    bytes_ = inp.proposed[variant] if inp.applied is None else inp.policy
    return (render_act(act, argument, variant, date, manifest_sha, reviewed, verdict, words, inp.frozen or "",
                       instant, inp.predecessor, inp.predecessor_date, version_of(bytes_),
                       effect_of(bytes_, variant)),
            render_aggregate_block(act, argument, variant, date, manifest_sha, verdict, inp.frozen or "", instant))


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, words: str,
              instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()} (one variant act only)")
        return 1
    inp = live_inputs(root)
    try:
        record, block = expected(act, argument, date, words, inp, instant)
    except (ValueError, OSError) as exc:
        print(f"FAILED (nothing written): {exc}")
        return 1
    if inp.applied is not None:
        print("FAILED: the policy on disk already carries a variant of this manifest")
        return 1
    aggregate = (root / AGGREGATE_REL).read_text()
    if aggregate_heading(act, date) in aggregate or BLOCK_BEGIN in aggregate:
        print("FAILED: aggregate record already carries this act's section")
        return 1
    variant = next(v for sha, _p, v in ROW_RE.findall(inp.manifest.decode()) if sha == argument)
    (root / act.record).write_text(record)
    (root / AGGREGATE_REL).write_text(aggregate.rstrip() + "\n\n" + block)
    (root / POLICY_REL).write_bytes(inp.proposed[variant])
    print(f"recorded at {instant}")
    print(f"wrote {act.record.as_posix()}\nappended one section to {AGGREGATE_REL.as_posix()}\n"
          f"applied variant {variant}: {POLICY_REL.as_posix()} now hashes to the argument")
    print("next, in the same change: the install re-points the read gates against these bytes, adds the "
          "check_governance chain link and pins the version-3 copies as history")
    return 0


def do_check(root: pathlib.Path, act: Act, argument: str, date: str, words: str,
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
        record, block = expected(act, argument, date, words, inp, instant)
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


INSTANT_OK = "2026-10-20T09:30:00Z"
V3_INSTANT = "2026-10-08T16:24:27Z"


def _accepts(act, argument, inp) -> bool:
    try:
        validate(act, argument, inp)
        return True
    except ValueError as exc:
        print(f"  (unexpected refusal: {exc})")
        return False


def _raises(fn, needle: str = "") -> bool:
    try:
        fn()
    except ValueError as exc:
        return needle in str(exc)
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
    base = b'{"policyVersion": "1.4.0-public-source-candidate.1.none.code-all"}\n'
    proposed = {v: (b'{"policyVersion": "1.5.0-public-source-candidate.1.none.code-all.redact-' + v.encode() + b'"}\n')
                for v in build.VARIANTS}
    rows = {v: digest(b) for v, b in proposed.items()}
    arg = rows["span"]
    manifest = ("# header\n" + "".join(f"{rows[v]}  {POLICY_REL.as_posix()}  [variant: {v}]\n"
                                       for v in build.VARIANTS)).encode()
    msha = digest(manifest)
    pkt = (b"# Packet\n\n> Candidate - binds nothing.\n\n| Variant | What | Rec |\n|---|---|---|\n"
           b"| `span-guides` | x | Yes |\n| `span` | y | |\n| decline | z | |\n")
    review = (f"# R4\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, PACKET_REL: pkt, BRIEF_REL: b"brief", DELTA_REL: b"delta",
             LEDGER_REL: b"ledger", BUILDER_REL: b"builder",
             **{rel: b"round " + rel.name.encode() for rel in ROUND_RELS},
             **{rel: b"patch " + v.encode() for v, rel in PATCH_RELS.items()}}

    def make(**over) -> Inputs:
        values = dict(manifest=manifest, policy=base, proposed=dict(proposed), packet=pkt, review=review,
                      stale=[], predecessor=digest(base), predecessor_date="2026-10-08",
                      predecessor_instant=V3_INSTANT, applied=None,
                      frozen="f" * 40, frozen_digest=lambda rel: digest(blobs[rel]) if rel in blobs else "",
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
    results.append(("the shipped frozen subject is a full commit id",
                    FROZEN_SUBJECT is not None and re.fullmatch(r"[0-9a-f]{40}", FROZEN_SUBJECT) is not None))
    results.append(("an applied policy not hashing to the argument refused",
                    refused("hashes to", arg, make(policy=proposed["span"] + b" ", applied="span"))))
    results.append(("a second variant act refused while the other is in force",
                    refused("second variant act", rows["span-guides"], make(policy=proposed["span"], applied="span"))))
    results.append(("unset FROZEN_SUBJECT refused", refused("FROZEN_SUBJECT is unset", arg, make(frozen=None))))
    results.append(("non-hex argument refused", refused("not a 64-hex", "xyz", make())))
    results.append(("an argument that is no row refused", refused("not a row", "0" * 64, make())))
    results.append(("a version-3 row as argument refused", refused("not a row", digest(base), make())))
    results.append(("manifest row for another subject refused",
                    refused("row population", arg, make(manifest=manifest.replace(POLICY_REL.name.encode(), b"other.json")))))
    results.append(("a manifest with a variant missing refused",
                    refused("row population", arg, make(manifest=b"\n".join(manifest.split(b"\n")[:-2]) + b"\n"))))
    results.append(("a manifest with the variants swapped in order refused",
                    refused("row population", arg, make(manifest=manifest.replace(b"[variant: span]", b"[variant: tmp]")
                                                        .replace(b"[variant: span-guides]", b"[variant: span]")
                                                        .replace(b"[variant: tmp]", b"[variant: span-guides]")))))
    results.append(("two rows with one digest refused",
                    refused("same digest", arg, make(manifest=manifest.replace(rows["span-guides"].encode(), arg.encode())))))
    results.append(("a missing version-3 act refused", refused("version-3 act record", arg, make(predecessor=""))))
    results.append(("a version-3 act with no date refused", refused("version-3 act record", arg, make(predecessor_date=""))))
    results.append(("a version-3 act with no instant refused",
                    refused("version-3 act record", arg, make(predecessor_instant=""))))
    results.append(("stale builder output refused", refused("builder reports", arg, make(stale=["x"]))))
    results.append(("policy not at the version-3 act's argument refused",
                    refused("version-3 act's argument", arg, make(policy=base + b" "))))
    results.append(("proposed bytes not hashing to the argument refused",
                    refused("proposed bytes", arg, make(proposed=dict(proposed, span=proposed["span"] + b" ")))))
    for rel in (LEDGER_REL, BUILDER_REL, ROUND_RELS[-1]):
        results.append((f"a frozen-file set missing {rel.name} refused",
                        refused("frozen-file set", arg, make(frozen_files={k: b for k, b in blobs.items() if k != rel}))))
    results.append(("a frozen-file set with an extra file refused",
                    refused("frozen-file set", arg, make(frozen_files={**blobs, DISPOSITION_REL: b"x"}))))
    for rel in (PACKET_REL, PATCH_RELS["span-guides"], BUILDER_REL, DELTA_REL):
        drift = dict(blobs)
        drift[rel] = blobs[rel] + b"x"
        results.append((f"frozen file lacking the presented {rel.name} refused",
                        refused("frozen subject does not carry", arg,
                                make(frozen_digest=lambda r, drift=drift: digest(drift[r]) if r in drift else ""))))
    performed = pkt.replace(b"\n\n", b"\n\n> **PERFORMED 2026-10-20.** Recorded.\n\n", 1)
    perf_files = dict(blobs)
    perf_files[PACKET_REL] = performed
    results.append(("PERFORMED head over the frozen packet accepted",
                    _accepts(act, arg, make(packet=performed, frozen_files=perf_files))))
    later = pkt + b"\n> **PERFORMED 2026-10-20.** Recorded.\n"
    results.append(("a PERFORMED note anywhere but the head refused",
                    refused("frozen subject does not carry", arg, make(packet=later, frozen_files={**blobs, PACKET_REL: later}))))
    results.append(("packet carrying a digest refused", refused("64-hex token", arg, make(packet=pkt + arg.encode()))))
    results.append(("packet with no table row for the chosen variant refused",
                    refused("no row for variant span", arg, make(packet=pkt.replace(b"| `span` |", b"| span |")))))
    results.append(("review binding another manifest digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, "0" * 64)))))
    results.append(("review binding a row instead of the file digest refused",
                    refused("manifest file's SHA-256", arg, make(review=review.replace(msha, arg)))))
    results.append(("verdict REVISE refused", refused("verdict", arg, make(review=review.replace("CONFIRM", "REVISE")))))
    results.append(("verdict displaced past the fourth head line refused",
                    refused("verdict", arg, make(review=review.replace("Verdict: CONFIRM", "Note: x\nVerdict: CONFIRM")))))
    results.append(("a head with no reviewed commit refused",
                    refused("reviewed commit", arg, make(review=review.replace("Reviewed commit:", "Commit:")))))
    exc_review = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
        "none", "**Finding 1 — t** (revise)\nbody")
    results.append(("a revise finding under CONFIRM WITH EXCEPTIONS refused",
                    refused("non-note", arg, make(review=exc_review))))
    results.append(("a revise finding under a bare CONFIRM refused",
                    refused("non-note", arg, make(review=exc_review.replace("CONFIRM WITH EXCEPTIONS", "CONFIRM")))))
    results.append(("CONFIRM WITH EXCEPTIONS with no finding refused",
                    refused("no countable finding", arg, make(review=review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS")))))
    notes = exc_review.replace("(revise)", "(note)")
    results.append(("notes-only CONFIRM WITH EXCEPTIONS accepted", _accepts(act, arg, make(review=notes))))

    def bad_disposition(findings):
        raise ValueError("disposition record does not name the reviewed raw")
    results.append(("missing disposition refused",
                    refused("disposition", arg, make(review=notes, disposition_check=bad_disposition))))
    # the real disposition check, wired as live_inputs wires it, over scratch files
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / CONFIRMATION_REVIEW_REL).parent.mkdir(parents=True)
        (root / CONFIRMATION_REVIEW_REL).write_text(notes)
        (root / DISPOSITION_REL).parent.mkdir(parents=True)
        wired = lambda findings: vs.validate_disposition(  # noqa: E731
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings)
        good = f"# R4 dispositions\n\nReviewed record: {CONFIRMATION_REVIEW_REL.as_posix()}\n\n## 1 — t (note)\n\nok\n"
        (root / DISPOSITION_REL).write_text(good)
        results.append(("a disposition naming the raw and finding 1 accepted",
                        _accepts(act, arg, make(review=notes, disposition_check=wired))))
        (root / DISPOSITION_REL).write_text(good.replace("Reviewed record: ", "Review: "))
        results.append(("a disposition with no `Reviewed record:` line refused",
                        refused("Reviewed record", arg, make(review=notes, disposition_check=wired))))
        (root / DISPOSITION_REL).write_text(good.replace("## 1 — t", "## 2 — t"))
        results.append(("a disposition numbering another finding refused",
                        refused("do not match", arg, make(review=notes, disposition_check=wired))))
        (root / DISPOSITION_REL).unlink()
        results.append(("an absent disposition refused",
                        refused("missing disposition", arg, make(review=notes, disposition_check=wired))))

    words = OWNER_WORDS[0]
    results.append(("the offered words are the two variants' and nothing else",
                    OWNER_WORDS == ("Sign screening scope version 4, variant span",
                                    "Sign screening scope version 4, variant span-guides")))
    for name, w, needle in (("empty words", "", "one non-empty line"),
                            ("multi-line words", words + "\nyes", "one non-empty line"),
                            ("words carrying a digest", words + " " + "a" * 64, "64-hex"),
                            ("the version-3 words", "Sign screening scope version 3, variant all", "none of the packet's"),
                            ("words with a trailing period", words + ".", "none of the packet's"),
                            ("words in another case", words.lower(), "none of the packet's"),
                            ("a decline", "Decline screening scope version 4", "none of the packet's")):
        results.append((f"{name} refused", _raises(lambda w=w: validate_words(w), needle)))
    results.append(("words naming the other variant refused",
                    _raises(lambda: expected(act, arg, "2026-10-20", OWNER_WORDS[1], make(), INSTANT_OK),
                            "name variant span-guides")))
    results.append(("an instant at the version-3 act's refused",
                    _raises(lambda: expected(act, arg, "2026-10-08", words, make(), V3_INSTANT), "not after")))
    results.append(("an instant before the version-3 act's refused",
                    _raises(lambda: expected(act, arg, "2026-10-08", words, make(), "2026-10-08T00:00:00Z"), "not after")))

    record = block = ""
    real: dict[str, bytes] = {}
    base_text = ""
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        for rel in (POLICY_REL, build.v3.MANIFEST, MANIFEST_REL):
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / rel, root / rel)
        shutil.copytree(ROOT / PKG / "proposed", root / PKG / "proposed")
        base_text, _mode = build.base_bytes(root)
        real = {v: build.propose(base_text, v).encode() for v in build.VARIANTS}
    real_rows = {v: digest(b) for v, b in real.items()}
    real_manifest = ("# header\n" + "".join(f"{real_rows[v]}  {POLICY_REL.as_posix()}  [variant: {v}]\n"
                                            for v in build.VARIANTS)).encode()
    real_review = review.replace(msha, digest(real_manifest))
    real_blobs = {**blobs, MANIFEST_REL: real_manifest}
    real_inp = make(manifest=real_manifest, proposed=real, policy=base_text.encode(),
                    predecessor=digest(base_text.encode()), review=real_review,
                    frozen_files=real_blobs, frozen_digest=lambda rel: digest(real_blobs[rel]) if rel in real_blobs else "")
    try:
        record, block = expected(act, real_rows["span"], "2026-10-20", words, real_inp, INSTANT_OK)
        results.append(("record and block render, naming the row and the tag",
                        real_rows["span"] in record and real_rows["span"] in block and tag_for(act, "2026-10-20") in record))
        results.append(("record carries the phrase exactly once in its ceremony",
                        record.count(phrase_for(act, real_rows["span"])) == 1))
        results.append(("record names the policy version it approves",
                        "`1.5.0-public-source-candidate.1.none.code-all.redact-span`" in record))
        results.append(("record quotes the owner's words verbatim, once", record.count(f"> {words}\n") == 1))
        results.append(("record names the chosen variant", "Chosen variant: `span`." in record))
        results.append(("the span record's effect names the whole-artifact detectors from the bytes",
                        "`private-key-material`, `known-token-formats`" in record
                        and "leaves every content-classification rule" in record and "rootGuideStems" not in record))
        results.append(("the supersession line has the read gate's form, naming the version-3 record and argument",
                        re.search(r"^Supersession / revocation: this act supersedes, for the `approve-policy` role only, "
                                  r"the \d{4}-\d{2}-\d{2} act recorded at `" + re.escape(V3_ACT_REL.as_posix()) + r"`\.",
                                  record, re.MULTILINE) is not None and f"`{digest(base_text.encode())}`" in record))
        results.append(("no line opens with 'recorded at' but the one field (the reader's loose instant count)",
                        len(re.findall(r"^\s*recorded at\b", record, re.I | re.M)) == 1))
        results.append(("the record carries none of the other families' sweep needles",
                        not any(n in record.lower() for n in ("public-egress-", "public-repo-admission", "public-obs-",
                                                              "rfc5-project-documentation", "dossier-local-agent"))))
        results.append(("the record carries exactly two 64-hex arguments and the manifest digest",
                        set(HEX64_RE.findall(record)) == {real_rows["span"], digest(base_text.encode()),
                                                          digest(real_manifest)}))
        results.append(("a CONFIRM record cites no dispositions file", DISPOSITION_REL.as_posix() not in record))
        r3, _b3 = expected(act, real_rows["span"], "2026-10-20", words,
                           make(**{**real_inp.__dict__, "review": real_review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
                               "none", "**Finding 1 — t** (note)\nbody")}), INSTANT_OK)
        results.append(("a notes-only CONFIRM WITH EXCEPTIONS record cites its dispositions file",
                        DISPOSITION_REL.as_posix() in r3))
        results.append(("the aggregate block is bracketed by section markers",
                        block.count(BLOCK_BEGIN) == 1 and block.count(BLOCK_END) == 1))
        r2, _b2 = expected(act, real_rows["span-guides"], "2026-10-20", OWNER_WORDS[1], real_inp, INSTANT_OK)
        results.append(("the other variant renders its own record", r2 != record
                        and "Chosen variant: `span-guides`." in r2
                        and f"{len(build.ROOT_GUIDE_STEMS)} root guide names" in r2
                        and "redact-span-guides" in r2))
    except ValueError as exc:
        print(f"  (render failure: {exc})")
        results.append(("record and block render", False))
    results.append(("approved bytes without the redaction object refused before rendering",
                    _raises(lambda: expected(act, arg, "2026-10-20", words, make(), INSTANT_OK), "do not carry")))
    results.append(("bad date refused", _raises(lambda: expected(act, arg, "20/10", words, make(), INSTANT_OK))))
    results.append(("record and block carry the instant exactly once each",
                    record.count(f"Recorded at (UTC): {INSTANT_OK}") == 1 and block.count(f"`{INSTANT_OK}`") == 1))
    for name, bad in (("a date-only instant", "2026-10-20"), ("a local-offset instant", "2026-10-20T09:30:00+08:00"),
                      ("an instant on another date", "2026-10-21T00:00:00Z")):
        results.append((f"{name} refused", _raises(lambda bad=bad: expected(act, arg, "2026-10-20", words, make(), bad))))

    # end to end in a scratch copy with no git: record variant span, check, refuse a repeat and the other variant
    saved = FROZEN_FILE_DIGESTS
    try:
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            for rel in (POLICY_REL, build.v3.MANIFEST, BUILDER_REL, CONFIRMATION_REVIEW_REL):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / rel, root / rel)
            shutil.copytree(ROOT / PKG, root / PKG, dirs_exist_ok=True)
            (root / POLICY_REL).write_text(base_text)
            (root / DECISIONS).mkdir(parents=True, exist_ok=True)
            (root / V3_ACT_REL).write_text(f"# v3\n\nDate: 2026-10-08\n\nRecorded at (UTC): {V3_INSTANT}\n\n"
                                           f"Exact digest (SHA-256): `{digest(base_text.encode())}`\n")
            (root / AGGREGATE_REL).write_text("# Acceptance record\n")
            mf = (root / MANIFEST_REL).read_bytes()
            raw = root / CONFIRMATION_REVIEW_REL
            raw.write_text(f"# R4 (synthetic, scratch only)\nReviewed commit: {'a' * 40}\n"
                           f"Manifest SHA-256: {digest(mf)}\nVerdict: CONFIRM\n\n## Findings\n\nnone\n")
            FROZEN_FILE_DIGESTS = {rel: digest((root / rel).read_bytes()) for rel in frozen_rels()}
            rowmap = {v: sha for sha, _p, v in ROW_RE.findall(mf.decode())}
            with contextlib.redirect_stdout(io.StringIO()):
                before = do_check(root, act, rowmap["span"], "2026-10-20", words, INSTANT_OK)
                early = do_record(root, act, rowmap["span"], "2026-10-08", words, "2026-10-08T00:00:00Z")
                wrote = do_record(root, act, rowmap["span"], "2026-10-20", words, INSTANT_OK)
                checked = do_check(root, act, rowmap["span"], "2026-10-20", words)
                again = do_record(root, act, rowmap["span"], "2026-10-20", words, INSTANT_OK)
                (root / act.record).rename(root / (act.record.name + ".moved"))
                other = do_record(root, act, rowmap["span-guides"], "2026-10-20", OWNER_WORDS[1], INSTANT_OK)
                (root / (act.record.name + ".moved")).rename(root / act.record)
                wrong_words = do_check(root, act, rowmap["span"], "2026-10-20", OWNER_WORDS[1])
                (root / AGGREGATE_REL).write_text((root / AGGREGATE_REL).read_text() * 2)
                doubled = do_check(root, act, rowmap["span"], "2026-10-20", words)
                (root / AGGREGATE_REL).write_text((root / AGGREGATE_REL).read_text()[:len((root / AGGREGATE_REL).read_text()) // 2])
                restored = do_check(root, act, rowmap["span"], "2026-10-20", words)
                (root / act.record).write_text((root / act.record).read_text().replace(INSTANT_OK, "2026-10-20T09:31:00Z"))
                tampered = do_check(root, act, rowmap["span"], "2026-10-20", words)
            results.append(("check before the act is recorded fails", before == 1))
            results.append(("a record before the version-3 act's instant writes nothing",
                            early == 1 and wrote == 0))
            results.append(("record then check in a bare copy applies the variant and passes",
                            wrote == 0 and checked == 0 and again == 1
                            and digest((root / POLICY_REL).read_bytes()) == rowmap["span"]
                            and not (root / ".git").exists()))
            results.append(("a second variant act in the same tree is refused and writes nothing",
                            other == 1 and json.loads((root / POLICY_REL).read_text())["policyVersion"].endswith(".redact-span")
                            and (root / AGGREGATE_REL).read_text().count("## Public-source screening scope version 4 act") == 1))
            results.append(("check with the other variant's words fails", wrong_words == 1))
            results.append(("check counting two copies of the block fails, one copy passes",
                            doubled == 1 and restored == 0))
            results.append(("a record whose instant was altered fails the check against the block", tampered == 1))
    finally:
        FROZEN_FILE_DIGESTS = saved
    failed = [name for name, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def at_commit_reader(commit: str) -> Callable[[pathlib.Path], bytes]:
    return v3rec.at_commit_reader(commit)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", metavar="ARGUMENT")
    mode.add_argument("--check", metavar="ARGUMENT")
    mode.add_argument("--freeze-table", nargs="?", const="", metavar="COMMIT")
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--instant", help="UTC instant YYYY-MM-DDTHH:MM:SSZ; --record defaults to now, --check reads it from the record")
    ap.add_argument("--owner-words", help="the owner's words, verbatim, e.g. 'Sign screening scope version 4, variant span'")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
    if args.freeze_table is not None:
        print(frozen_table(at_commit_reader(args.freeze_table) if args.freeze_table else None))
        return 0
    argument = args.record or args.check
    if not (args.date and args.owner_words):
        print("--date and --owner-words are required", file=sys.stderr)
        return 2
    fn = do_record if args.record else do_check
    return fn(ROOT, ACT, argument, args.date, args.owner_words, args.instant)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
