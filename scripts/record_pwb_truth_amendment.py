#!/usr/bin/env python3
"""Record or verify the exact owner-signed PWB truth-and-readiness amendment act.

Decision 1 of `contracts/candidates/pwb-truth-policy-amendment/
OWNER-DECISION-PACKET.md`. This script performs nothing by itself: it accepts
the owner's exact argument, recomputes it from the frozen manifest bytes, and
appends the dedicated and aggregate act records. The policy and registry
effect acts (Decisions 2 and 3) are separate and are not written here.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys

import build_pwb_truth_policy_amendment as packet


ROOT = pathlib.Path(__file__).resolve().parents[1]
CANDIDATE = packet.CANDIDATE
OWNER_PACKET = CANDIDATE / "OWNER-DECISION-PACKET.md"
ACT_REL = pathlib.Path(
    ".syzygy/governance/decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md"
)
AGGREGATE_REL = pathlib.Path(
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
)
FINAL_PACKET_REVIEW_REL = pathlib.Path(
    "docs/reviews/R-PWB-TRUTH-POLICY-OWNER-PACKET-FINAL-RAW.md"
)
FROZEN_SUBJECT = "4daea0868a0e15ea2f9407efc18f143dbabbd64b"
PACKET_HEAD = "875ef026f00b3b2a87b72f2977ab12380af5cc2a"
FINAL_EVIDENCE_HEAD = "62d3bb74b21e43b07a7b708f5c743e6ee27ac946"
ACT_LABEL = "SIGN OFF PWB TRUTH-AND-READINESS AMENDMENT"
ACT_DATE = "2026-09-05"
TAG_NAME = "pwb-truth-readiness-amendment-signed-2026-09-05"
AGGREGATE_HEADING = (
    f"## PWB truth-and-readiness amendment — performed {ACT_DATE}"
)
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def committed_blob(root: pathlib.Path, commit: str, rel: pathlib.Path) -> bytes:
    return subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{rel.as_posix()}"],
        check=True,
        capture_output=True,
    ).stdout


def validate_subject(
    root: pathlib.Path, argument: str
) -> tuple[str, list[tuple[str, str]]]:
    manifest_path = root / packet.BEHAVIOR_OUT
    if not manifest_path.is_file():
        raise ValueError(f"missing manifest: {packet.BEHAVIOR_OUT}")
    manifest_bytes = manifest_path.read_bytes()
    manifest_sha = digest(manifest_bytes)
    if argument != manifest_sha:
        raise ValueError(
            f"owner argument {argument} does not match manifest {manifest_sha}"
        )
    expected = packet.outputs()[packet.BEHAVIOR_OUT]
    findings = packet.verify_manifest(
        manifest_bytes.decode(), packet.BEHAVIOR_SUBJECTS, expected
    )
    if findings:
        raise ValueError("manifest does not verify: " + " | ".join(findings))
    if committed_blob(root, FROZEN_SUBJECT, packet.BEHAVIOR_OUT) != manifest_bytes:
        raise ValueError("frozen subject does not carry current manifest bytes")
    rows = ROW_RE.findall(manifest_bytes.decode())
    if len(rows) != 11:
        raise ValueError(f"manifest carries {len(rows)} rows, expected 11")
    for expected_sha, path in rows:
        actual = digest(committed_blob(root, FROZEN_SUBJECT, pathlib.Path(path)))
        if actual != expected_sha:
            raise ValueError(f"frozen subject row mismatch: {path}")

    owner_packet_path = root / OWNER_PACKET
    if not owner_packet_path.is_file():
        raise ValueError(f"missing owner packet: {OWNER_PACKET}")
    owner_packet = owner_packet_path.read_bytes()
    phrase = f"{ACT_LABEL}: {argument}"
    if owner_packet.decode().count(phrase) != 1:
        raise ValueError("owner packet does not contain exactly one exact phrase")
    if committed_blob(root, PACKET_HEAD, OWNER_PACKET) != owner_packet:
        raise ValueError("packet-head commit does not carry the presented packet bytes")

    final_review = root / FINAL_PACKET_REVIEW_REL
    if not final_review.is_file():
        raise ValueError(f"missing final packet review: {FINAL_PACKET_REVIEW_REL}")
    review_body = final_review.read_text()
    required_review_markers = (
        f"Exact wrapper commit: `{PACKET_HEAD}`",
        f"Owner packet SHA-256: `{digest(owner_packet)}`",
        f"Frozen semantic subject: `{FROZEN_SUBJECT}`",
        f"Behavior manifest SHA-256: `{argument}`",
        "**EXACT VERDICT: CONFIRM**",
    )
    if any(marker not in review_body for marker in required_review_markers):
        raise ValueError("final packet review does not bind the exact offered subject")
    return manifest_sha, rows


def render_act(argument: str, rows: list[tuple[str, str]]) -> str:
    artifact_table = "\n".join(
        f"| `{path}` | `{artifact_sha}` |" for artifact_sha, path in rows
    )
    return f"""# Owner act — PWB truth-and-readiness amendment sign-off

Date: {ACT_DATE}

Owner: Tzeusy

Act identity: `PWB-TRUTH-READINESS-AMENDMENT-SIGNOFF-{ACT_DATE}`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented Decision 1 of the independently confirmed packet at
`{OWNER_PACKET.as_posix()}`
and performed the offered indivisible behavior amendment by writing exactly:

```text
{ACT_LABEL}: {argument}
```

The argument is the SHA-256 of
`{packet.BEHAVIOR_OUT.as_posix()}`.
It was recomputed at recording and matched the phrase. All eleven rows verified
against frozen subject `{FROZEN_SUBJECT}`. The presented packet bytes were
verified against the packet head and against the final owner-packet review.

Frozen provenance:

- reviewed subject: `{FROZEN_SUBJECT}`;
- owner-packet head: `{PACKET_HEAD}`;
- final evidence head: `{FINAL_EVIDENCE_HEAD}`;
- final contract/oracle, security/public-interface and fresh-reader
  comprehension verdicts: `CONFIRM`;
- final owner-packet verdict: `CONFIRM`, zero findings; and
- recording tag: `{TAG_NAME}`, on the commit carrying this act record.

## Effect

The eleven artifacts below are signed as the amended behavioral authority for
the bounded, local, non-release, one-Butlers-repository POC. Within that
bound, the signed change now:

- closes four project-fact families and the exact root cardinal/precedence
  grammar, including the item/count family map, literal layer/ownership rows
  and the recorded eight-versus-nine domain-butler conflict;
- admits markup-like examples only in syntactically valid inert code
  contexts, while complete secret scanning and genuine active-content
  exclusion remain;
- defines one phase-A-plus-phase-B byte ledger, deterministic parse passes
  within a closed vocabulary and ceiling, separate human-HTML and
  authenticated-machine-JSON output ceilings, and bounded typed failure in
  place of truncated success;
- makes one selected, classified baseline requirement transiently verbatim
  through the existing exact-source path; and
- closes nine-answer readiness under PWB-REQ-021 while PWB-REQ-022 stays at
  exactly 84 present-invalid plus 2 absent cases.

PWB-REQ-005's 195 invalid cases, its valid state-(1)/state-(2) combinations,
the one configured repository and the `declared-project-shape-text` content
class are unchanged. Only state (2) may be called independently verified;
state (1) remains owner-trusted and uncorrelated. Invalid acts fail closed and
acts remain warrants, never evidence that an effect succeeded.

Deterministic grammar is intentionally brittle: a future Butlers syntax
outside it becomes Unknown until a new reviewed amendment, never a guess.

This act supersedes the eleven PWB artifact digests made current by the
2026-09-02 state-(1) amendment. That prior act, its manifest, digests, tag and
bytes remain immutable historical evidence.

## Signed artifacts

| Repository-relative artifact | sha256 |
|---|---|
{artifact_table}

All eleven rows take effect together or none do. An edit to any listed artifact
breaks this act's digest binding and must use the amendment path.

## What this act does not authorize

This act approves no amended secret-classification policy and adopts no
amended observer registry entry; the 2026-09-02 policy and registry acts
remain the effective authorities for their roles until the owner performs
their exact successor acts (Decisions 2 and 3 of the same packet). It widens
no consent, creates no walkthrough judgment, and authorizes no PWB
implementation of the amended semantics: implementation authorization must be
separately continued by the owner across its signed-spec, policy and registry
escalation triggers.

It grants no write, egress, observed-code execution, deployment, release,
recovery, mission, second repository, wider content class, autonomous
behavior or multi-user support. It proves no read, screening, parse, render,
answer or comprehension result. It does not edit the signed parent
`three-surface-poc-experience` artifacts, accept RFC 0010 or RFC 0011, amend
doctrine, or start automatic follow-on work.
"""


def render_aggregate_block(argument: str) -> str:
    return f"""{AGGREGATE_HEADING}

**Phrase, exactly as written by the owner (in-interaction, {ACT_DATE}):**

```text
{ACT_LABEL}: {argument}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Argument | SHA-256 of `contracts/candidates/pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`, recomputed at recording and equal to the phrase |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Reviewed subject | `{FROZEN_SUBJECT}` |
| Owner-packet / final evidence heads | `{PACKET_HEAD}` / `{FINAL_EVIDENCE_HEAD}` |
| Review outcome | final contract/oracle, security/public-interface, comprehension and owner-packet reviews: `CONFIRM`, zero open findings |
| Ceremony verification | 11 of 11 manifest rows verified against the frozen subject; manifest digest equals the phrase `[Observed, this act]` |
| Supersession | the eleven digests of the 2026-09-02 PWB state-(1) amendment; that act remains immutable history |
| Recording | `.syzygy/governance/decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md`; annotated tag `{TAG_NAME}` on the commit carrying these records |

Effective status: the eleven-artifact PWB package is **signed behavioral
authority — owner-adopted (bootstrap, uncorrelated)** at these bytes. The
closed fact/precedence grammar, inert-code admission, deterministic resource
envelope, transient verbatim baseline requirement and PWB-REQ-021 readiness
are now signed requirements; PWB-REQ-005's and PWB-REQ-022's denominators are
unchanged.

This act approves no policy, adopts no registry entry, widens no consent and
authorizes no implementation of the amended semantics. Decisions 2 and 3 of
the packet and a separate continuation of implementation authorization remain
open; no write, egress, execution, deployment, release, recovery or mission
authority follows from this act.
"""


def expected_outputs(root: pathlib.Path, argument: str) -> dict[pathlib.Path, str]:
    _manifest_sha, rows = validate_subject(root, argument)
    aggregate = (root / AGGREGATE_REL).read_text()
    occurrences = aggregate.count(AGGREGATE_HEADING)
    if occurrences > 1:
        raise ValueError("aggregate record contains duplicate PWB act sections")
    prefix = (
        aggregate.split(AGGREGATE_HEADING, 1)[0].rstrip()
        if occurrences
        else aggregate.rstrip()
    )
    expected_aggregate = prefix + "\n\n" + render_aggregate_block(argument)
    return {
        ACT_REL: render_act(argument, rows),
        AGGREGATE_REL: expected_aggregate,
    }


def record(root: pathlib.Path, argument: str, check: bool) -> int:
    try:
        outputs = expected_outputs(root, argument)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED: {exc}")
        return 1
    if check:
        # Later acts append after this section, so the aggregate is checked
        # for exactly one exact copy of this act's block, not for being the
        # tail of the file.
        drift = []
        if not (root / ACT_REL).is_file() or (root / ACT_REL).read_text() != outputs[ACT_REL]:
            drift.append(ACT_REL)
        aggregate = (root / AGGREGATE_REL).read_text()
        if aggregate.count(render_aggregate_block(argument)) != 1:
            drift.append(AGGREGATE_REL)
        if drift:
            for rel in drift:
                print(f"recorded PWB act differs from regeneration: {rel}")
            return 1
        print("recorded PWB truth-and-readiness act matches exact owner argument")
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
    manifest_sha = digest((ROOT / packet.BEHAVIOR_OUT).read_bytes())
    try:
        validate_subject(ROOT, "0" * 64)
        wrong_rejected = False
    except ValueError as exc:
        wrong_rejected = "does not match manifest" in str(exc)
    valid = False
    try:
        valid = validate_subject(ROOT, manifest_sha)[0] == manifest_sha
    except ValueError as exc:
        print(f"  exact argument failed: {exc}")
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
