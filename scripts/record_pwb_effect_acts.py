#!/usr/bin/env python3
"""Record or verify the owner's separate PWB effect acts (consent, policy, registry).

Each act is one state-(1) human owner act on one artifact, bound to that
artifact's own SHA-256. The owner may perform any subset; each performed act
gets its own dedicated decision record and its own appended section in the
aggregate `ACCEPTANCE-ACT-RECORD.md`. This script never performs an act: it
only verifies an owner-written phrase against the frozen subject and writes
the records that quote it.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

import build_pwb_effect_acts_packet as packet


ROOT = pathlib.Path(__file__).resolve().parents[1]
AGGREGATE_REL = pathlib.Path(".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md")
FINAL_PACKET_REVIEW_REL = pathlib.Path(
    "docs/reviews/R-PWB-EFFECT-ACTS-OWNER-PACKET-RAW.md"
)
#: The commit whose bytes every offered phrase binds (packet §"Frozen candidate commit").
FROZEN_SUBJECT = "48e0f5db645d1fb08e5e3a65c5e50dbcece40412"
#: The commit carrying the generated owner packet the owner was shown. Filled
#: in once that commit exists; the placeholder fails every validation closed.
PACKET_HEAD = "a322a60e9f2b166273a80e3fc145bc3a8193c962"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


class Act:
    def __init__(self, act_type, label, artifact, record_name, identity, title, effect, not_authorized):
        self.act_type = act_type
        self.label = label
        self.artifact = artifact
        self.record = pathlib.Path(".syzygy/governance/decisions") / record_name
        self.identity = identity
        self.title = title
        self.effect = effect
        self.not_authorized = not_authorized


ACTS = {
    "consent-observation": Act(
        "consent-observation",
        "CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION",
        packet.CONSENT,
        "PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md",
        "PWB-BUTLERS-OBSERVATION-CONSENT",
        "Butlers project-shape observation consent",
        """The consent record below is the owner's effective observation consent for
the pair (`project:syzygy`, `repository:butlers-configured-poc`) and the one
content class `declared-project-shape-text`. Scope: read-only Git objects
selected by the signed PWB source population at the Butlers revision the POC
observes. Excluded: PostgreSQL and every other data store, credential stores
and secret APIs, `.env` and credential files, arbitrary implementation-file
bodies, working-tree traversal, code execution, network egress, writes to
Butlers, and any second repository. The consent has no silent expiry; the
owner may narrow or revoke it only by a later exact act. It does not
retroactively authorize the reads recorded in the precondition-read incident.""",
        """This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It approves no secret-classification policy and
adopts no adapter-registry entry; a body read still needs both of those acts
in a valid state, plus separate PWB implementation authorization (task 1.8).""",
    ),
    "approve-policy": Act(
        "approve-policy",
        "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY",
        packet.POLICY,
        "PWB-SECRET-CLASSIFICATION-POLICY-ACT.md",
        "PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL",
        "Polaris Butlers secret-classification policy approval",
        """The policy below (`polaris-butlers-project-shape-secrets`, policy-owning
project `project:syzygy`) is approved as the observing project's
secret-classification policy for that pair and content class, across every
ingest boundary the PWB spec names. Denied credential filenames and suffixes,
four detectors, strict UTF-8 without NUL and a closed extraction class per
source are mandatory; any detector match excludes the whole artifact with
class `excluded-artifact`, anything unclassifiable excludes it with class
`unclassifiable-excluded`, and only the digest, path, policy id/version and
detector id or exclusion reason are retained. Raw bodies are never stored,
logged, rendered, returned or sent anywhere.""",
        """This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and adopts no
adapter-registry entry; a body read still needs both of those acts in a
valid state, plus separate PWB implementation authorization (task 1.8).""",
    ),
    "adopt-registry-entry": Act(
        "adopt-registry-entry",
        "ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY",
        packet.REGISTRY,
        "PWB-OBSERVER-REGISTRY-ENTRY-ACT.md",
        "PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION",
        "Polaris Butlers project-shape observer registry-entry adoption",
        """The adapter-registry entry below (`polaris-butlers-project-shape`) is
adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, with read-only authority and an empty
write surface. It declares exactly what the observer may read (the signed PWB
source population), which policy screens it, and that the observer has no
write, execution, egress or second-repository capability. The entry is a
declared mapping only: no such module exists yet, and adopting the entry
authorizes none to be written.""",
        """This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and approves no
secret-classification policy; a body read still needs both of those acts in
a valid state, plus separate PWB implementation authorization (task 1.8).""",
    ),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def validate_artifact(root: pathlib.Path, act: Act, argument: str) -> None:
    """Stage 1 — the phrase names the artifact's current and frozen bytes."""
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
    frozen_sha = digest(packet.committed_blob(root, FROZEN_SUBJECT, act.artifact))
    if frozen_sha != argument:
        raise ValueError(f"frozen subject {FROZEN_SUBJECT} carries a different {act.artifact}")
    manifest_bytes = (root / packet.OUT).read_bytes()
    findings = packet.verify(manifest_bytes.decode(), root)
    if findings:
        raise ValueError("manifest does not verify: " + " | ".join(findings))
    if manifest_bytes.decode() != packet.render(root):
        raise ValueError("manifest differs from exact regeneration")
    rows = dict((path, sha) for sha, path in packet.ROW_RE.findall(manifest_bytes.decode()))
    if rows.get(act.artifact.as_posix()) != argument:
        raise ValueError("manifest row for the artifact does not equal the owner argument")


def validate_packet(root: pathlib.Path, act: Act, argument: str) -> dict:
    """Stage 2 — the owner was shown a reviewed packet carrying exactly this phrase."""
    if PACKET_HEAD == "0" * 40:
        raise ValueError("packet head not yet frozen in this recorder")
    finalized = packet.finalized_outputs(root, FROZEN_SUBJECT)
    owner_packet = finalized[packet.OWNER_PACKET]
    if owner_packet.count(phrase_for(act, argument)) != 1:
        raise ValueError("owner packet does not contain exactly one exact phrase for this act")
    if packet.committed_blob(root, PACKET_HEAD, packet.OWNER_PACKET).decode() != owner_packet:
        raise ValueError("packet-head commit does not carry generated packet bytes")
    final_review = root / FINAL_PACKET_REVIEW_REL
    if not final_review.is_file():
        raise ValueError(f"missing final packet review: {FINAL_PACKET_REVIEW_REL}")
    body = final_review.read_text()
    markers = (
        PACKET_HEAD,
        FROZEN_SUBJECT,
        argument,
        "**EXACT VERDICT: CONFIRM**",
        "**OWNER PACKET MAY BE PRESENTED TO THE OWNER: YES",
    )
    missing = [m for m in markers if m not in body]
    if missing:
        raise ValueError("final packet review does not bind the exact offered subject")
    return finalized


def validate(root: pathlib.Path, act: Act, argument: str) -> None:
    validate_artifact(root, act, argument)
    validate_packet(root, act, argument)


def render_act(act: Act, argument: str, date: str) -> str:
    tag = f"pwb-{act.act_type}-signed-{date}"
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

Supersession / revocation: none — this act supersedes no earlier act and is
revoked only by a later exact owner act naming it

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`{packet.OWNER_PACKET.as_posix()}`
and performed this one act by writing exactly:

```text
{phrase_for(act, argument)}
```

The argument is the SHA-256 of the artifact itself. It was recomputed at
recording and matched the phrase, the manifest row and the bytes committed at
frozen subject `{FROZEN_SUBJECT}`. The act instant is the moment the owner
wrote the phrase, in-interaction, on {date}.

Frozen provenance:

- reviewed subject: `{FROZEN_SUBJECT}` (this pins `ACT-SEMANTICS.md`, the
  manifest and all three artifacts as one tree);
- owner-packet head: `{PACKET_HEAD}`;
- security review of the original subject and confirmation review of this
  subject: `CONFIRM`;
- owner-packet readability review: `CONFIRM`; and
- recording tag: `{tag}`, on the commit carrying this act record.

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
second-repository, autonomous or multi-user authority, edits no signed
artifact, accepts no candidate contract and amends no doctrine.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## PWB effect act — {act.act_type} — performed {date}"


def render_aggregate_block(act: Act, argument: str, date: str) -> str:
    tag = f"pwb-{act.act_type}-signed-{date}"
    return f"""{aggregate_heading(act, date)}

**Phrase, exactly as written by the owner (in-interaction, {date}):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{act.act_type}` / `{act.artifact.as_posix()}` |
| Argument | SHA-256 of the artifact itself, recomputed at recording and equal to the phrase and the manifest row |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Supersession | none |
| Reviewed subject / owner-packet head | `{FROZEN_SUBJECT}` / `{PACKET_HEAD}` |
| Review outcome | security, confirmation and owner-packet reviews: `CONFIRM` |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag}` on the commit carrying these records |

Effective status: this one artifact is **effective owner authority — owner-
adopted (bootstrap, uncorrelated)** for its own PWB-REQ-005 role only. The
other two effect acts and PWB implementation authorization remain separate;
no body read, write, egress, execution, deployment, release, recovery or
mission authority follows from this act.
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
    except ValueError as exc:
        print(f"FAILED: {exc}")
        return 1
    if check:
        drift = [
            rel for rel, content in outputs.items()
            if not (root / rel).is_file() or (root / rel).read_text() != content
        ]
        for rel in drift:
            print(f"recorded act differs from regeneration: {rel}")
        if drift:
            return 1
        print(f"recorded {act.act_type} act matches exact owner argument")
        return 0
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record}")
        return 1
    for rel, content in outputs.items():
        (root / rel).write_text(content)
        print(f"wrote {rel}")
    print(f"next: git add the two records, commit, then tag "
          f"pwb-{act.act_type}-signed-{date} on that commit")
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
        try:
            validate_artifact(ROOT, act, exact)
            ok = True
        except ValueError as exc:
            ok = False
            print(f"  ({act.act_type} exact-argument failure: {exc})")
        results.append((f"{act.act_type}: exact argument validates against frozen subject", ok))
        packet_stage = "not frozen" if PACKET_HEAD == "0" * 40 else "frozen"
        try:
            validate_packet(ROOT, act, exact)
            staged = True
        except ValueError as exc:
            staged = False
            note = str(exc)
        if packet_stage == "frozen" and not staged and "missing final packet review" in note:
            results.append((f"{act.act_type}: packet stage fails closed while final review absent", True))
        elif packet_stage == "frozen":
            results.append((f"{act.act_type}: packet stage validates", staged))
        else:
            results.append((f"{act.act_type}: packet stage fails closed while head unfrozen", not staged and "not yet frozen" in note))
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
