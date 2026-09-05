#!/usr/bin/env python3
"""Record or verify the owner's amended PWB effect acts (Decisions 2 and 3).

Decisions 2 and 3 of `contracts/candidates/pwb-truth-policy-amendment/
OWNER-DECISION-PACKET.md` re-perform the 2026-09-02 policy-approval and
registry-adoption acts over the amended artifact bytes. Each is one separate
state-(1) human owner act bound to the artifact's own SHA-256; each performed
act gets its own new dedicated decision record and its own appended section
in the aggregate `ACCEPTANCE-ACT-RECORD.md`. The 2026-09-02 record, digest and
tag of the superseded act are never edited: they remain immutable history.

This script performs nothing by itself. It verifies an owner-written phrase
against the frozen subject, the effect manifest, the presented packet and the
final packet review, and writes the records that quote it.
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
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
OWNER_PACKET = packet.CANDIDATE / "OWNER-DECISION-PACKET.md"
FINAL_PACKET_REVIEW_REL = pathlib.Path(
    "docs/reviews/R-PWB-TRUTH-POLICY-OWNER-PACKET-FINAL-RAW.md"
)
#: The commit whose bytes every offered phrase binds (packet §"Frozen subject").
FROZEN_SUBJECT = "4daea0868a0e15ea2f9407efc18f143dbabbd64b"
#: The commit carrying the owner packet the owner was shown.
PACKET_HEAD = "875ef026f00b3b2a87b72f2977ab12380af5cc2a"
#: The commit carrying the final owner-packet review.
FINAL_EVIDENCE_HEAD = "62d3bb74b21e43b07a7b708f5c743e6ee27ac946"
#: The act that Decisions 2 and 3 presuppose (Decision 1 of the same packet).
BEHAVIOR_ACT_REL = DECISIONS / "PWB-TRUTH-READINESS-AMENDMENT-ACT.md"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


class Act:
    def __init__(self, act_type, label, artifact, record_name, predecessor_name,
                 identity, title, effect, not_authorized):
        self.act_type = act_type
        self.label = label
        self.artifact = artifact
        self.record = DECISIONS / record_name
        self.predecessor = DECISIONS / predecessor_name
        self.identity = identity
        self.title = title
        self.effect = effect
        self.not_authorized = not_authorized


POLICY, REGISTRY = (
    next(p for p in packet.EFFECT_SUBJECTS if p.as_posix().startswith(".syzygy/governance/policies/")),
    next(p for p in packet.EFFECT_SUBJECTS if "adapter-registry" in p.as_posix()),
)

ACTS = {
    "approve-policy": Act(
        "approve-policy",
        "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY",
        POLICY,
        "PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md",
        "PWB-SECRET-CLASSIFICATION-POLICY-ACT.md",
        "PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-AMENDMENT",
        "Polaris Butlers secret-classification policy approval (amendment)",
        """The amended policy below (`polaris-butlers-project-shape-secrets`, version
`1.1.0-candidate.1`, policy-owning project `project:syzygy`) is approved as the
observing project's secret-classification policy for the pair
(`project:syzygy`, `repository:butlers-configured-poc`) and the one content
class `declared-project-shape-text`, across every ingest boundary the PWB spec
names, in place of the 2026-09-02 approval. Every denied credential filename
and suffix, all four secret detectors, strict UTF-8 without NUL and the closed
extraction class per source are unchanged and mandatory; every detector still
runs over the complete body, inert code contexts included. The amendment adds
one closed Markdown code-context profile: markup-like bytes wholly inside a
syntactically closed inline code span or fenced code block are inert for
active-content detection only, while a genuine active form outside such a
context, or a malformed code context, excludes the whole artifact. Any
detector match excludes the whole artifact with class `excluded-artifact`,
anything unclassifiable excludes it with class `unclassifiable-excluded`, and
only the digest, path, policy id/version and detector id or exclusion reason
are retained. Raw bodies are never stored, logged, rendered, returned or sent
anywhere, and admitted Markdown is never rendered as HTML.""",
        """This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and adopts no
amended adapter-registry entry (Decision 3 of the same packet remains a
separate owner act); a body read under the amended semantics still needs
the consent act and the applicable registry act in a valid state, plus the
owner's separate continuation of PWB implementation authorization across
the signed-spec, policy and registry escalation triggers.""",
    ),
    "adopt-registry-entry": Act(
        "adopt-registry-entry",
        "ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY",
        REGISTRY,
        "PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md",
        "PWB-OBSERVER-REGISTRY-ENTRY-ACT.md",
        "PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-AMENDMENT",
        "Polaris Butlers project-shape observer registry-entry adoption (amendment)",
        """The amended adapter-registry entry below (`polaris-butlers-project-shape`,
observer version `1.1.0-candidate.1`, discovery version
`pwb-discovery-v2-candidate.1`) is adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, in place of the 2026-09-02 entry, with
read-only authority and an empty write surface. It keeps the signed PWB
source population, the policy that screens it and the absence of write,
execution, egress and second-repository capability, and adds the closed
observation grammar (fact families, fixed class, catalog and project-account
keys, the root cardinal summary and the literal seven-row precedence table),
the deterministic resource envelope (parse-pass ceiling and separate human
and machine response ceilings with bounded typed failure in place of
truncated success) and the two new output classes `project-fact-declaration`
and `precedence-rule`. The entry is a declared mapping: adopting it changes
no code and authorizes none to be written.""",
        """This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and approves no
secret-classification policy; a body read under the amended semantics still
needs the consent act and the applicable policy act in a valid state, plus
the owner's separate continuation of PWB implementation authorization across
the signed-spec, policy and registry escalation triggers.""",
    ),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def committed_blob(root: pathlib.Path, commit: str, rel: pathlib.Path) -> bytes:
    return subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{rel.as_posix()}"],
        check=True,
        capture_output=True,
    ).stdout


def validate_artifact(root: pathlib.Path, act: Act, argument: str) -> str:
    """Stage 1 — the phrase names the artifact's current and frozen bytes.

    Returns the effect manifest's SHA-256, which the final review binds.
    """
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    current = root / act.artifact
    if not current.is_file():
        raise ValueError(f"artifact missing: {act.artifact}")
    current_sha = digest(current.read_bytes())
    if argument != current_sha:
        raise ValueError(
            f"owner argument {argument} does not match current {act.artifact} ({current_sha})"
        )
    frozen_sha = digest(committed_blob(root, FROZEN_SUBJECT, act.artifact))
    if frozen_sha != argument:
        raise ValueError(f"frozen subject {FROZEN_SUBJECT} carries a different {act.artifact}")
    manifest_path = root / packet.EFFECT_OUT
    if not manifest_path.is_file():
        raise ValueError(f"missing effect manifest: {packet.EFFECT_OUT}")
    manifest_bytes = manifest_path.read_bytes()
    findings = packet.verify_manifest(
        manifest_bytes.decode(), packet.EFFECT_SUBJECTS, packet.outputs()[packet.EFFECT_OUT]
    )
    if findings:
        raise ValueError("effect manifest does not verify: " + " | ".join(findings))
    if committed_blob(root, FROZEN_SUBJECT, packet.EFFECT_OUT) != manifest_bytes:
        raise ValueError("frozen subject does not carry current effect manifest bytes")
    rows = dict((path, sha) for sha, path in packet.ROW.findall(manifest_bytes.decode()))
    if rows.get(act.artifact.as_posix()) != argument:
        raise ValueError("effect manifest row for the artifact does not equal the owner argument")
    if not (root / act.predecessor).is_file():
        raise ValueError(f"superseded 2026-09-02 act record missing: {act.predecessor}")
    if not (root / BEHAVIOR_ACT_REL).is_file():
        raise ValueError(f"Decision 1 act record missing: {BEHAVIOR_ACT_REL}")
    return digest(manifest_bytes)


def validate_packet(root: pathlib.Path, act: Act, argument: str, manifest_sha: str) -> None:
    """Stage 2 — the owner was shown a reviewed packet carrying exactly this phrase."""
    owner_packet_path = root / OWNER_PACKET
    if not owner_packet_path.is_file():
        raise ValueError(f"missing owner packet: {OWNER_PACKET}")
    owner_packet = owner_packet_path.read_bytes()
    if owner_packet.decode().count(phrase_for(act, argument)) != 1:
        raise ValueError("owner packet does not contain exactly one exact phrase for this act")
    if committed_blob(root, PACKET_HEAD, OWNER_PACKET) != owner_packet:
        raise ValueError("packet-head commit does not carry the presented packet bytes")
    final_review = root / FINAL_PACKET_REVIEW_REL
    if not final_review.is_file():
        raise ValueError(f"missing final packet review: {FINAL_PACKET_REVIEW_REL}")
    body = final_review.read_text()
    markers = (
        f"Exact wrapper commit: `{PACKET_HEAD}`",
        f"Owner packet SHA-256: `{digest(owner_packet)}`",
        f"Frozen semantic subject: `{FROZEN_SUBJECT}`",
        f"Effect manifest SHA-256: `{manifest_sha}`",
        "**EXACT VERDICT: CONFIRM**",
    )
    if any(marker not in body for marker in markers):
        raise ValueError("final packet review does not bind the exact offered subject")


def validate(root: pathlib.Path, act: Act, argument: str) -> None:
    validate_packet(root, act, argument, validate_artifact(root, act, argument))


def tag_for(act: Act, date: str) -> str:
    return f"pwb-{act.act_type}-signed-{date}"


def render_act(act: Act, argument: str, date: str) -> str:
    return f"""# Owner act — {act.title}

Date: {date}

Owner: Tzeusy

Act identity: `{act.identity}-{date}`

Act type: `{act.act_type}`

Project identity: `project:syzygy`

Artifact identity: `{act.artifact.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by performing the offered state-(1) phrase

Supersession / revocation: this act supersedes, for the `{act.act_type}` role
only, the 2026-09-02 act recorded at `{act.predecessor.as_posix()}`. That
record, its digest, its tag and the bytes it bound remain immutable history.
This act is revoked only by a later exact owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`{OWNER_PACKET.as_posix()}`,
after Decision 1 of that packet was recorded at
`{BEHAVIOR_ACT_REL.as_posix()}`,
and performed this one act by writing exactly:

```text
{phrase_for(act, argument)}
```

The argument is the SHA-256 of the artifact itself. It was recomputed at
recording and matched the phrase, the effect-manifest row and the bytes
committed at frozen subject `{FROZEN_SUBJECT}`. The act instant is the moment
the owner wrote the phrase, in-interaction, on {date}.

Frozen provenance:

- reviewed subject: `{FROZEN_SUBJECT}` (this pins the effect manifest and
  both amended artifacts with the eleven behavior artifacts as one tree);
- owner-packet head: `{PACKET_HEAD}`;
- final evidence head: `{FINAL_EVIDENCE_HEAD}`;
- final contract/oracle, security/public-interface and fresh-reader
  comprehension verdicts: `CONFIRM`;
- final owner-packet verdict: `CONFIRM`, zero findings; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

{act.effect}

The act is a warrant, never evidence that any effect succeeded. State (1) is
owner-trusted, uncorrelated and same-tree forgeable from Syzygy's
perspective; its digest detects later drift, not authorship or attendance.
An edit to the artifact breaks this act's digest binding; changes travel as a
new act.

## What this act does not authorize

{act.not_authorized}

It grants no write, egress, execution, deployment, release, recovery, mission,
second-repository, autonomous or multi-user authority, widens no consent,
edits no signed artifact, accepts no candidate contract and amends no
doctrine. It proves no read, screening, parse, render or answer result.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## PWB effect-act amendment — {act.act_type} — performed {date}"


def render_aggregate_block(act: Act, argument: str, date: str) -> str:
    return f"""{aggregate_heading(act, date)}

**Phrase, exactly as written by the owner (in-interaction, {date}):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{act.act_type}` / `{act.artifact.as_posix()}` |
| Argument | SHA-256 of the artifact itself, recomputed at recording and equal to the phrase and the effect-manifest row |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Supersession | the 2026-09-02 `{act.act_type}` act recorded at `{act.predecessor.as_posix()}`; that act, its digest and its tag remain immutable history |
| Reviewed subject | `{FROZEN_SUBJECT}` |
| Owner-packet / final evidence heads | `{PACKET_HEAD}` / `{FINAL_EVIDENCE_HEAD}` |
| Review outcome | final contract/oracle, security/public-interface, comprehension and owner-packet reviews: `CONFIRM`, zero open findings |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: this one amended artifact is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own PWB-REQ-005 role only.
The other effect authorities and the continuation of PWB implementation
authorization remain separate; no body read, write, egress, execution,
deployment, release, recovery or mission authority follows from this act.
"""


def expected_outputs(root: pathlib.Path, act: Act, argument: str, date: str) -> dict[pathlib.Path, str]:
    validate(root, act, argument)
    aggregate = (root / AGGREGATE_REL).read_text()
    heading = aggregate_heading(act, date)
    occurrences = aggregate.count(heading)
    if occurrences > 1:
        raise ValueError("aggregate record contains duplicate sections for this act")
    prefix = aggregate.split(heading, 1)[0].rstrip() if occurrences else aggregate.rstrip()
    return {
        act.record: render_act(act, argument, date),
        AGGREGATE_REL: prefix + "\n\n" + render_aggregate_block(act, argument, date),
    }


def record(root: pathlib.Path, act: Act, argument: str, date: str, check: bool) -> int:
    if not DATE_RE.fullmatch(date):
        print("FAILED: --date must be YYYY-MM-DD")
        return 1
    try:
        outputs = expected_outputs(root, act, argument, date)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED: {exc}")
        return 1
    if check:
        # Acts are separable and append in owner order, so the aggregate is
        # checked for exactly one exact copy of this act's block, not for
        # being the tail of the file.
        drift = []
        dedicated = root / act.record
        if not dedicated.is_file() or dedicated.read_text() != outputs[act.record]:
            drift.append(act.record)
        aggregate = (root / AGGREGATE_REL).read_text()
        if aggregate.count(render_aggregate_block(act, argument, date)) != 1:
            drift.append(AGGREGATE_REL)
        for rel in drift:
            print(f"recorded act differs from regeneration: {rel}")
        if drift:
            return 1
        print(f"recorded amended {act.act_type} act matches exact owner argument")
        return 0
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record}")
        return 1
    for rel, content in outputs.items():
        (root / rel).write_text(content)
        print(f"wrote {rel}")
    print(f"next: git add the two records, commit, then tag "
          f"{tag_for(act, date)} on that commit")
    return 0


def selftest() -> int:
    results = []
    for act in ACTS.values():
        exact = digest((ROOT / act.artifact).read_bytes())
        try:
            validate_artifact(ROOT, act, "0" * 64)
            wrong = False
        except ValueError as exc:
            wrong = "does not match current" in str(exc)
        results.append((f"{act.act_type}: wrong argument rejected", wrong))
        other = next(a for a in ACTS.values() if a is not act)
        try:
            validate_artifact(ROOT, act, digest((ROOT / other.artifact).read_bytes()))
            swapped = False
        except ValueError as exc:
            swapped = "does not match current" in str(exc)
        results.append((f"{act.act_type}: another artifact's digest rejected", swapped))
        manifest_sha = None
        try:
            manifest_sha = validate_artifact(ROOT, act, exact)
            ok = True
        except ValueError as exc:
            ok = False
            print(f"  ({act.act_type} exact-argument failure: {exc})")
        results.append((f"{act.act_type}: exact argument validates against frozen subject", ok))
        staged = False
        if manifest_sha is not None:
            try:
                validate_packet(ROOT, act, exact, manifest_sha)
                staged = True
            except ValueError as exc:
                print(f"  ({act.act_type} packet-stage failure: {exc})")
        results.append((f"{act.act_type}: packet stage validates", staged))
        try:
            validate_packet(ROOT, act, exact, "0" * 64)
            unbound = False
        except ValueError as exc:
            unbound = "does not bind" in str(exc)
        results.append((f"{act.act_type}: review not binding the effect manifest rejected", unbound))
    failing = 0
    for name, passed in results:
        failing += 0 if passed else 1
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"{len(results)} recording fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", nargs=2, metavar=("ACT_TYPE", "ARTIFACT_SHA"))
    parser.add_argument("--check", nargs=2, metavar=("ACT_TYPE", "ARTIFACT_SHA"))
    parser.add_argument("--date", metavar="YYYY-MM-DD", help="the date the owner wrote the phrase")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    selected = sum(bool(v) for v in (args.record, args.check, args.selftest))
    if selected != 1:
        parser.error("choose exactly one of --record, --check or --selftest")
    if args.selftest:
        return selftest()
    act_type, argument = args.record or args.check
    if act_type not in ACTS:
        parser.error(f"ACT_TYPE must be one of {', '.join(ACTS)}")
    if not args.date:
        parser.error("--date is required with --record/--check")
    return record(ROOT, ACTS[act_type], argument, args.date, check=bool(args.check))


if __name__ == "__main__":
    sys.exit(main())
