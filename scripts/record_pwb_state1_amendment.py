#!/usr/bin/env python3
"""Record or verify the exact owner-signed PWB state-(1) amendment act."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

import build_pwb_state1_amendment_manifest as packet


ROOT = pathlib.Path(__file__).resolve().parents[1]
ACT_REL = pathlib.Path(
    ".syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md"
)
AGGREGATE_REL = pathlib.Path(
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
)
FINAL_PACKET_REVIEW_REL = pathlib.Path(
    "docs/reviews/R-PWB-STATE1-OWNER-PACKET-FINAL-RAW.md"
)
FROZEN_SUBJECT = "8847feef1442bf55fd5276a73248d3c58409e4db"
PACKET_HEAD = "cc809f90f5cc0bacddad83adce19864a361dbc8b"
FINAL_EVIDENCE_HEAD = "5c2a792c7896f6cbfeb460adfb4d05276675cf8b"
ACT_LABEL = "SIGN OFF PWB STATE-(1) AMENDMENT"
TAG_NAME = "pwb-state1-amendment-signed-2026-09-02"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_subject(root: pathlib.Path, argument: str) -> tuple[str, list[tuple[str, str]]]:
    manifest_path = root / packet.OUT
    if not manifest_path.is_file():
        raise ValueError(f"missing manifest: {packet.OUT}")
    manifest_bytes = manifest_path.read_bytes()
    manifest_sha = digest(manifest_bytes)
    if argument != manifest_sha:
        raise ValueError(
            f"owner argument {argument} does not match manifest {manifest_sha}"
        )
    findings = packet.verify(manifest_bytes.decode(), root)
    if findings:
        raise ValueError("manifest does not verify: " + " | ".join(findings))
    if manifest_bytes.decode() != packet.render(root):
        raise ValueError("manifest differs from exact regeneration")
    if packet.committed_blob(root, FROZEN_SUBJECT, packet.OUT) != manifest_bytes:
        raise ValueError("frozen subject does not carry current manifest bytes")
    rows = packet.ROW_RE.findall(manifest_bytes.decode())
    for expected, path in rows:
        actual = digest(packet.committed_blob(root, FROZEN_SUBJECT, pathlib.Path(path)))
        if actual != expected:
            raise ValueError(f"frozen subject row mismatch: {path}")

    finalized = packet.finalized_outputs(root, FROZEN_SUBJECT)
    owner_packet = finalized[packet.OWNER_PACKET]
    phrase = f"{ACT_LABEL}: {argument}"
    if owner_packet.count(phrase) != 1:
        raise ValueError("owner packet does not contain exactly one exact phrase")
    if packet.committed_blob(root, PACKET_HEAD, packet.OWNER_PACKET).decode() != owner_packet:
        raise ValueError("packet-head commit does not carry generated packet bytes")

    final_review = root / FINAL_PACKET_REVIEW_REL
    if not final_review.is_file():
        raise ValueError(f"missing final packet review: {FINAL_PACKET_REVIEW_REL}")
    review_body = final_review.read_text()
    required_review_markers = (
        PACKET_HEAD,
        FROZEN_SUBJECT,
        argument,
        "**EXACT VERDICT: CONFIRM**",
        "**OWNER PACKET MAY BE PRESENTED TO THE OWNER: YES",
    )
    if any(marker not in review_body for marker in required_review_markers):
        raise ValueError("final packet review does not bind the exact offered subject")
    return manifest_sha, rows


def render_act(argument: str, rows: list[tuple[str, str]]) -> str:
    artifact_table = "\n".join(
        f"| `{path}` | `{artifact_sha}` |" for artifact_sha, path in rows
    )
    return f"""# Owner act — PWB state-(1) amendment sign-off

Date: 2026-09-02

Owner: Tzeusy

Act identity: `PWB-STATE1-AMENDMENT-SIGNOFF-2026-09-02`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`.syzygy/governance/contracts/candidates/pwb-state1-amendment/OWNER-SIGNOFF-PACKET.md`
and performed the offered indivisible amendment by writing exactly:

```text
{ACT_LABEL}: {argument}
```

The argument is the SHA-256 of
`.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
It was recomputed at recording and matched the phrase. All eleven rows verified
against frozen subject `{FROZEN_SUBJECT}`.

Frozen provenance:

- reviewed subject: `{FROZEN_SUBJECT}`;
- owner-packet head: `{PACKET_HEAD}`;
- final evidence head: `{FINAL_EVIDENCE_HEAD}`;
- final security, deterministic-oracle and transaction verdicts: `CONFIRM`;
- hardened owner-packet verdict: `CONFIRM`, zero findings; and
- recording tag: `{TAG_NAME}`, on the commit carrying this act record.

## Effect

The eleven artifacts below are signed as the amended behavioral authority for
the bounded, local, non-release, one-Butlers-repository POC. PWB-REQ-005 now
accepts each exact consent, policy and registry human owner act in valid state
(1) or state (2), including all eight equal/mixed triples. PWB-REQ-022 accepts
an exact-scope human owner judgment in valid state (1) or state (2).
PWB-REQ-020 preserves every exact state and disclosure across the human and
machine channels.

Only state (2) may be called independently verified. State (1) remains
owner-trusted, uncorrelated and same-tree forgeable from Syzygy's perspective;
its digest detects drift, not authorship or attendance. Invalid acts fail
closed. The signed test obligations close 195 admission-invalid cases, 84
present-invalid judgment cases, 2 absent cases and fail-then-restore mutation
proof. Acts remain warrants, never evidence that an effect succeeded.

The effective contract-coverage posture remains 622 consequences over 324
accepted clauses: 137 covered, 237 Unknown uncovered and 248 believed not
applicable. This act mints no owner-reviewed N/A judgment.

This act supersedes the six PWB artifact digests still current from the
2026-08-31 sign-off and the five coverage-artifact digests made current by the
2026-09-01 general trusted-bootstrap transaction. Those prior acts, manifests,
digests and bytes remain immutable historical evidence.

## Signed artifacts

| Repository-relative artifact | sha256 |
|---|---|
{artifact_table}

All eleven rows take effect together or none do. An edit to any listed artifact
breaks this act's digest binding and must use the amendment path.

## What this act does not authorize

This act creates or approves no observation consent, concrete secret policy,
adapter-registry entry or walkthrough judgment. It authorizes no repository-
body read and no PWB implementation. Separate effect-specific owner acts and
separate implementation authorization remain mandatory.

It grants no write, egress, execution, deployment, release, recovery, mission,
second repository, autonomous behavior or multi-user support. It does not edit
the signed parent `three-surface-poc-experience` artifacts, accept RFC 0010 or
RFC 0011, amend doctrine, or start automatic follow-on work.
"""


def render_aggregate_block(argument: str) -> str:
    return f"""## PWB state-(1) amendment — performed 2026-09-02

**Phrase, exactly as written by the owner (in-interaction, 2026-09-02):**

```text
{ACT_LABEL}: {argument}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Argument | SHA-256 of `contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`, recomputed at recording and equal to the phrase |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Reviewed subject | `{FROZEN_SUBJECT}` |
| Owner-packet / final evidence heads | `{PACKET_HEAD}` / `{FINAL_EVIDENCE_HEAD}` |
| Review outcome | final security, deterministic-oracle, transaction and hardened owner-packet reviews: `CONFIRM`, zero open findings |
| Ceremony verification | 11 of 11 manifest rows verified against the frozen subject; manifest digest equals the phrase `[Observed, this act]` |
| Recording | `.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md`; annotated tag `{TAG_NAME}` on the commit carrying these records |

Effective status: the eleven-artifact PWB package is **signed behavioral
authority — owner-adopted (bootstrap, uncorrelated)**. Valid state (1) and state
(2) human acts may satisfy PWB-REQ-005 and PWB-REQ-022; only state (2) is
independently verified. Invalid acts fail closed and acts remain warrants, not
success evidence.

This act grants no effect-specific consent or policy approval, registry
adoption, repository-body read, write, egress, execution, deployment, release,
recovery, implementation or mission authority. Separate effect-specific acts
and separate PWB implementation authorization remain open.
"""


def expected_outputs(root: pathlib.Path, argument: str) -> dict[pathlib.Path, str]:
    _manifest_sha, rows = validate_subject(root, argument)
    aggregate = (root / AGGREGATE_REL).read_text()
    heading = "## PWB state-(1) amendment — performed 2026-09-02"
    occurrences = aggregate.count(heading)
    if occurrences > 1:
        raise ValueError("aggregate record contains duplicate PWB act sections")
    prefix = aggregate.split(heading, 1)[0].rstrip() if occurrences else aggregate.rstrip()
    expected_aggregate = prefix + "\n\n" + render_aggregate_block(argument)
    return {
        ACT_REL: render_act(argument, rows),
        AGGREGATE_REL: expected_aggregate,
    }


def record(root: pathlib.Path, argument: str, check: bool) -> int:
    try:
        outputs = expected_outputs(root, argument)
    except ValueError as exc:
        print(f"FAILED: {exc}")
        return 1
    if check:
        drift = [
            rel for rel, content in outputs.items()
            if not (root / rel).is_file() or (root / rel).read_text() != content
        ]
        if drift:
            for rel in drift:
                print(f"recorded PWB act differs from regeneration: {rel}")
            return 1
        print("recorded PWB state-(1) act matches exact owner argument")
        return 0
    if (root / ACT_REL).exists():
        print(f"FAILED: dedicated act already exists: {ACT_REL}")
        return 1
    for rel, content in outputs.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        print(f"wrote {rel}")
    return 0


def selftest() -> int:
    manifest_sha = digest((ROOT / packet.OUT).read_bytes())
    try:
        validate_subject(ROOT, "0" * 64)
        wrong_rejected = False
    except ValueError as exc:
        wrong_rejected = "does not match manifest" in str(exc)
    valid = False
    try:
        valid = validate_subject(ROOT, manifest_sha)[0] == manifest_sha
    except ValueError:
        pass
    print(f"{'PASS' if wrong_rejected else 'FAIL'} wrong owner argument rejected")
    print(f"{'PASS' if valid else 'FAIL'} exact owner argument validates")
    passed = wrong_rejected and valid
    print(f"2 recording fixtures, {0 if passed else 1} failing")
    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", metavar="MANIFEST_SHA")
    parser.add_argument("--check", metavar="MANIFEST_SHA")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    selected = sum(bool(value) for value in (args.record, args.check, args.selftest))
    if selected != 1:
        parser.error("choose exactly one of --record, --check or --selftest")
    if args.selftest:
        return selftest()
    if args.record:
        return record(ROOT, args.record, check=False)
    return record(ROOT, args.check, check=True)


if __name__ == "__main__":
    sys.exit(main())
