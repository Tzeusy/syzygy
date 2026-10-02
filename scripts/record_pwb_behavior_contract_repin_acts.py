#!/usr/bin/env python3
"""Record or verify the two superseding PWB behaviour-contract re-pin acts.

Bead `syzygy-jloi`; package
`contracts/candidates/pwb-behavior-contract-repin/`. Two separate state-(1)
owner acts, each in the shape of the act it supersedes and each over one
subject, for that subject's PWB-REQ-005 role only:

- `policy` — `approve-policy`, superseding the 2026-09-05 policy amendment
  act (`PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`);
- `registry` — `adopt-registry-entry`, superseding the 2026-09-30
  currency-and-briefing act
  (`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`).

The phrase forms are unchanged from the acts superseded; each argument is the
SHA-256 of that artifact's proposed bytes, which is that subject's row of the
two-row `PWB-EFFECT-REPIN-MANIFEST.txt`. No argument appears in any Markdown
file of the package. This script performs nothing by itself.

`--record SUBJECT ARGUMENT --date D` accepts the owner's argument for one
subject and requires, before anything is written:

1. the argument equals that subject's manifest row (so an argument meant for
   the other subject is refused), the manifest and both patches are the
   bytes the frozen package commit carries, and the argument is the digest
   of the builder's proposed bytes;
2. the subject's current bytes are exactly the superseded act's argument,
   and the builder verifies;
3. the owner packet carries no 64-hex token and is the frozen packet under at
   most one PERFORMED head; and
4. the confirming raw is bound by its head: its first four non-blank lines
   carry `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the
   manifest FILE>` (the form `REVIEW-BRIEF.md` "Recording" sets, which
   differs from the registry-currency recorder's row form), and a verdict of
   `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter clears the bytes only
   when every finding is a `note` and the sibling `ROUND-1-DISPOSITIONS.md`
   names the raw and dispositions every finding.

It then applies the patch through the builder (`--apply <subject>
--at-adoption`), confirms the subject hashes to the argument, and writes the
dedicated record and one `ACCEPTANCE-ACT-RECORD.md` section. `--check`
re-derives both after adoption and counts exactly one copy of the aggregate
block. `--selftest` mutates each predicate and requires it to fail closed.

The two acts were given on 2026-10-02 by an option selection in a structured
question, not by typed phrases; each record says so and quotes the selection.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import contextlib
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass

import build_pwb_behavior_contract_repin as packet
import record_versioned_signoff as vs


ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
OWNER_PACKET = packet.CANDIDATE / "OWNER-DECISION-PACKET.md"
CONFIRMATION_REVIEW_REL = pathlib.Path("docs/reviews/R-PWB-BEHAVIOR-CONTRACT-REPIN-RAW.md")
DISPOSITION_REL = packet.CANDIDATE / "ROUND-1-DISPOSITIONS.md"
DIRECTION_REL = DECISIONS / "OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md"
#: The commit the confirming review read; it carries the manifest, both
#: patches and the owner packet exactly as offered. Re-set, never hand-edited,
#: if the package is ever re-offered.
FROZEN_SUBJECT = "140874b7364266475dd8980be480e2783e0d8e72"
PACKET_HEAD = FROZEN_SUBJECT
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$", re.MULTILINE)
VERDICT_RE = re.compile(r"^Verdict: (.+?)\s*$")

#: The owner's selection, verbatim as relayed to the recording session. The
#: question's opening words are known; the rest of its text was not relayed
#: and is not reconstructed here.
QUESTION_OPENING = "Perform the PWB behaviour-contract re-pin?"
SELECTION_LABEL = "A + B + C now (Recommended)"
SELECTION_DESCRIPTION = (
    "Perform both acts at the manifest rows and give direction C; I write the "
    "recorder, record both acts and re-point the gate in one change, so reads "
    "keep working.")
GARBLED_PARENTHETICAL = (
    "(policy ad9cd6… is the registry row; 66cd41… is the policy row)")


@dataclass(frozen=True)
class Act:
    key: str
    label: str
    act_type: str
    identity_stem: str
    record: pathlib.Path
    predecessor: pathlib.Path
    predecessor_date: str
    title: str
    #: Strings the read gate's scope check expects in the record's Effect.
    anchors: tuple[str, ...]


def _subject(key: str) -> packet.Subject:
    return next(s for s in packet.SUBJECTS if s.key == key)


ACTS = (
    Act("policy", "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY",
        "approve-policy",
        "PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-BEHAVIOR-CONTRACT-REPIN",
        _subject("policy").record, _subject("policy").predecessor, "2026-09-05",
        "Polaris Butlers secret-classification policy approval "
        "(behaviour-contract re-pin)",
        ("polaris-butlers-project-shape-secrets", "1.1.0-candidate.1",
         "project:syzygy")),
    Act("registry", "ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY",
        "adopt-registry-entry",
        "PWB-OBSERVER-REGISTRY-ENTRY-BEHAVIOR-CONTRACT-REPIN",
        _subject("registry").record, _subject("registry").predecessor, "2026-09-30",
        "Polaris Butlers project-shape observer registry-entry adoption "
        "(behaviour-contract re-pin)",
        ("polaris-butlers-project-shape", "1.2.0-candidate.1",
         "pwb-discovery-v2-candidate.1",
         ".syzygy/governance/declarations/adapter-registry", "project:syzygy",
         "read-only", "empty write surface")),
)
ACT_BY_KEY = {act.key: act for act in ACTS}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"pwb-{act.act_type}-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


def committed_blob(root: pathlib.Path, commit: str, rel: pathlib.Path) -> bytes:
    done = subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{rel.as_posix()}"],
        capture_output=True,
    )
    if done.returncode != 0:
        raise ValueError(f"cannot read {rel.as_posix()} at {commit}: "
                         f"{done.stderr.decode().strip() or 'git show failed'}")
    return done.stdout


def manifest_row(manifest_bytes: bytes, act: Act) -> str:
    rows = packet.ROW.findall(manifest_bytes.decode())
    if sorted(path for _sha, path in rows) != sorted(
            s.path.as_posix() for s in packet.SUBJECTS) or len(rows) != 2:
        raise ValueError("effect manifest row population differs from the two subjects")
    return next(sha for sha, path in rows if path == _subject(act.key).path.as_posix())


def validate_artifact(
    root: pathlib.Path, act: Act, argument: str, applied: bool,
    manifest_override: bytes | None = None, subject_override: bytes | None = None,
) -> str:
    """Stage 1 — the argument names this subject's proposed bytes.

    Returns the manifest file's SHA-256, which the review head binds.
    """
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    subject = _subject(act.key)
    manifest_path = root / packet.OUT
    if manifest_override is None and not manifest_path.is_file():
        raise ValueError(f"missing effect manifest: {packet.OUT.as_posix()}")
    manifest_bytes = (manifest_override if manifest_override is not None
                      else manifest_path.read_bytes())
    row = manifest_row(manifest_bytes, act)
    if row != argument:
        raise ValueError(f"owner argument {argument} does not match the {act.key} "
                         f"manifest row {row}")
    if committed_blob(root, FROZEN_SUBJECT, packet.OUT) != manifest_bytes:
        raise ValueError("frozen subject does not carry the presented effect manifest bytes")
    for s in packet.SUBJECTS:
        if committed_blob(root, FROZEN_SUBJECT, packet.patch_path(s)) != (
                root / packet.patch_path(s)).read_bytes():
            raise ValueError(f"frozen subject does not carry {packet.patch_path(s).as_posix()}")
    if subject_override is None and not (root / subject.path).is_file():
        raise ValueError(f"artifact missing: {subject.path.as_posix()}")
    subject_bytes = (subject_override if subject_override is not None
                     else (root / subject.path).read_bytes())
    current = digest(subject_bytes)
    if applied:
        if current != argument:
            raise ValueError(f"{act.key} subject hashes to {current}, not the owner "
                             "argument; the patch was not applied")
        return digest(manifest_bytes)
    superseded = packet.predecessor_digest(root, subject)
    if current != superseded:
        raise ValueError(f"{act.key} subject hashes to {current}, not the superseded "
                         f"act's argument {superseded}")
    if subject_override is None:
        findings = packet.check(root)
        if findings:
            raise ValueError("package does not verify: " + " | ".join(findings))
    proposed = packet._apply(root, subject, subject_bytes, reverse=False)
    if digest(proposed) != argument:
        raise ValueError("owner argument does not match the digest of the proposed bytes")
    # The record's Effect names the artifact's identity and version label;
    # the proposed bytes must carry both, unchanged (no version bump).
    text = proposed.decode()
    missing = [anchor for anchor in act.anchors[:2] if f'"{anchor}"' not in text]
    if missing:
        raise ValueError(f"proposed bytes do not carry the identity/version anchors {missing}")
    return digest(manifest_bytes)


#: The one head a packet may gain after the act, between its title and the
#: banner it was offered with; nothing else in the presented bytes may move.
PERFORMED_HEAD_RE = re.compile(
    rb"\A(# [^\n]+\n\n)"
    rb"> \*\*PERFORMED \d{4}-\d{2}-\d{2}\.\*\*[^\n]*\n(?:> [^\n]*\n)*\n"
)


def strip_performed_head(packet_bytes: bytes) -> bytes:
    return PERFORMED_HEAD_RE.sub(rb"\1", packet_bytes, count=1)


def validate_packet(
    root: pathlib.Path, manifest_sha: str,
    packet_override: bytes | None = None, review_override: str | None = None,
    disposition_root: pathlib.Path | None = None,
) -> tuple[str, str]:
    """Stage 2 — the packet shown carries no digest; the raw confirms it.

    Returns (reviewed commit, verdict); the commit is provenance, not binding.
    """
    packet_path = root / OWNER_PACKET
    if packet_override is None and not packet_path.is_file():
        raise ValueError(f"missing owner packet: {OWNER_PACKET.as_posix()}")
    packet_bytes = packet_override if packet_override is not None else packet_path.read_bytes()
    if HEX64_RE.search(packet_bytes.decode()):
        raise ValueError("owner packet carries a 64-hex token; the package derives its "
                         "arguments only from the manifest rows")
    if committed_blob(root, PACKET_HEAD, OWNER_PACKET) != strip_performed_head(packet_bytes):
        raise ValueError("packet-head commit does not carry the presented packet bytes")
    review_path = root / CONFIRMATION_REVIEW_REL
    if review_override is None and not review_path.is_file():
        raise ValueError(f"missing confirmation review: {CONFIRMATION_REVIEW_REL.as_posix()}")
    review = review_override if review_override is not None else review_path.read_text()
    head = [line for line in review.splitlines() if line.strip()][:4]
    if f"Manifest SHA-256: {manifest_sha}" not in head:
        raise ValueError("confirmation review head does not bind the effect manifest "
                         "file's SHA-256")
    verdicts = [m.group(1) for line in head if (m := VERDICT_RE.match(line))]
    if len(verdicts) != 1 or verdicts[0] not in VERDICTS:
        raise ValueError("confirmation review head does not carry the verdict CONFIRM "
                         "or CONFIRM WITH EXCEPTIONS")
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    if verdicts[0] == "CONFIRM WITH EXCEPTIONS":
        findings = vs.review_findings(review)
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; only a "
                             "notes-only round clears the bytes")
        vs.validate_disposition(disposition_root or root,
                                CONFIRMATION_REVIEW_REL.as_posix(),
                                DISPOSITION_REL.as_posix(), findings)
    return reviewed.group(1), verdicts[0]


def validate(root: pathlib.Path, act: Act, argument: str, applied: bool) -> tuple[str, str, str]:
    manifest_sha = validate_artifact(root, act, argument, applied)
    reviewed, verdict = validate_packet(root, manifest_sha)
    return manifest_sha, reviewed, verdict


def render_effect(act: Act) -> str:
    if act.key == "policy":
        return """The re-pinned policy (`polaris-butlers-project-shape-secrets`, version
`1.1.0-candidate.1`, policy-owning project `project:syzygy`) is approved as
the observing project's secret-classification policy for the pair
(`project:syzygy`, `repository:butlers-configured-poc`) and the one content
class `declared-project-shape-text`, in place of the 2026-09-05 approval.
Exactly two values change: `governingBehaviorContract.version` now names the
PWB `spec.md` that the `pwb-readability-successor-v1.0` sign-off binds (the
`spec.md` row of that package's manifest), and `signedBy` names that
version-tagged sign-off and its record. Every denied credential filename and
suffix, every detector, the strict-UTF-8 rule, the closed extraction class
per source, the Markdown code-context profile and every retention rule are
byte-identical to the bytes the 2026-09-05 act approved."""
    return """The re-pinned adapter-registry entry (`polaris-butlers-project-shape`,
version `1.2.0-candidate.1`, discovery version
`pwb-discovery-v2-candidate.1`) is adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, in place of the 2026-09-30 entry, with
read-only authority and an empty write surface. Exactly two values change:
`governingBehaviorContract.version` now names the PWB `spec.md` that the
`pwb-readability-successor-v1.0` sign-off binds (the `spec.md` row of that
package's manifest), and `signedBy` names that version-tagged sign-off and
its record. The source population, observation grammar, resource envelope,
currency bounds, briefing ceiling and the absence of write, execution,
egress and second-repository capability are byte-identical to the bytes the
2026-09-30 act adopted."""


def render_act(act: Act, argument: str, date: str, manifest_sha: str,
               reviewed: str, verdict: str, superseded_digest: str) -> str:
    subject = _subject(act.key)
    other = "registry entry" if act.key == "policy" else "secret-classification policy"
    return f"""# Owner act — {act.title}

Date: {date}

Owner: Tzeusy

Act identity: `{identity_for(act, date)}`

Act type: `{act.act_type}`

Project identity: `project:syzygy`

Artifact identity: `{subject.path.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: this act supersedes, for the `{act.act_type}` role only, the {act.predecessor_date} act recorded at `{act.predecessor.as_posix()}`.
Its argument `{superseded_digest}` was the subject's exact digest until
this act's patch was applied. That record, its digest, its tag and the bytes
it bound remain immutable history. This act is revoked only by a later exact
owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`{OWNER_PACKET.as_posix()}`,
which by design carries no digest. The act takes this phrase, whose argument
is this subject's row of the effect manifest:

```text
{phrase_for(act, argument)}
```

The owner did not type the phrase. On {date} the owner answered a structured
question in the Claude Code CLI that opened "{QUESTION_OPENING}" by
selecting the option below; the selection is the instruction, and it names
both acts "at the manifest rows". The label and description, verbatim:

| Label | Description |
|---|---|
| "{SELECTION_LABEL}" | "{SELECTION_DESCRIPTION}" |

[Observed] The question text also carried a garbled parenthetical,
verbatim: "{GARBLED_PARENTHETICAL}". Its first word can be read as
pairing the policy with the registry row's prefix; the rest of it states the
pairing the manifest carries. It is not the binding: the option binds each
act to its own manifest row. The argument above was read from the {act.key} row of
`{packet.OUT.as_posix()}` at the reviewed
commit, re-derived from the builder's proposed bytes at recording, and,
after the package's patch was applied through its builder in the same
change, matched the artifact on disk. A swapped argument would have been
refused: the recorder rejects an argument that is not this subject's row.
The full account is `{DIRECTION_REL.as_posix()}`.

Frozen provenance:

- frozen subject (package bytes) and owner-packet head: `{FROZEN_SUBJECT}`;
- effect manifest SHA-256: `{manifest_sha}`;
- confirmation review: `{CONFIRMATION_REVIEW_REL.as_posix()}`, verdict
  `{verdict}`, its head bound to the effect manifest file's SHA-256 above;
  its two findings are notes, dispositioned in
  `{DISPOSITION_REL.as_posix()}`; the raw names reviewed commit
  `{reviewed}` [Observed — the raw's own line; binding is by digest]; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

{render_effect(act)}

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent, and it neither
approves nor adopts the {other}, which took its own separate act the same
day. The read gate evaluates this act only under the owner's plain
continuation direction C of the same selection, recorded at
`{DIRECTION_REL.as_posix()}`; no implementation consumes
`governingBehaviorContract` or any other field it did not read before.

It grants no write, egress, execution, deployment, release, recovery,
mission, second-repository, autonomous or multi-user authority, widens no
consent, changes no version label, edits no performed record, accepts no
candidate contract and amends no doctrine. It proves no read, screening,
parse, render or answer result.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return (f"## PWB effect-act amendment — {act.act_type} — behaviour-contract "
            f"re-pin — performed {date}")


def render_aggregate_block(act: Act, argument: str, date: str, manifest_sha: str,
                           verdict: str) -> str:
    subject = _subject(act.key)
    return f"""{aggregate_heading(act, date)}

**Phrase the act takes (given {date} by option selection, not typed; see the
dedicated record):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{act.act_type}` / `{subject.path.as_posix()}` |
| Argument | SHA-256 of the artifact itself: the {act.key} row of the effect manifest, recomputed at recording and equal to the artifact on disk after the package's patch was applied |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Supersession | the {act.predecessor_date} `{act.act_type}` act recorded at `{act.predecessor.as_posix()}`; that act, its digest and its tag remain immutable history |
| Frozen subject / packet head | `{FROZEN_SUBJECT}` / `{PACKET_HEAD}` |
| Effect manifest | `{packet.OUT.as_posix()}`, SHA-256 `{manifest_sha}` |
| Review outcome | `{CONFIRMATION_REVIEW_REL.as_posix()}`: `{verdict}`, notes only, its head bound to the effect manifest file |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: this one re-pinned artifact is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own PWB-REQ-005 role only.
The other effect authorities and the plain continuation direction remain
separate; no body read, write, egress, execution, deployment, release,
recovery or mission authority follows from this act.
"""


def expected_outputs(root: pathlib.Path, act: Act, argument: str, date: str,
                     applied: bool) -> tuple[dict[pathlib.Path, str], str]:
    manifest_sha, reviewed, verdict = validate(root, act, argument, applied)
    superseded = packet.predecessor_digest(root, _subject(act.key))
    block = render_aggregate_block(act, argument, date, manifest_sha, verdict)
    return ({act.record: render_act(act, argument, date, manifest_sha, reviewed,
                                    verdict, superseded)}, block)


def registration_notes(act: Act, argument: str, date: str, superseded: str) -> str:
    return (
        "next, in the same change:\n"
        f"  1. git add {_subject(act.key).path.as_posix()} and the two records; tag "
        f"{tag_for(act, date)} on the commit carrying them\n"
        "  2. scripts/check_governance.py: the PWB_EFFECT_AMENDMENT_ACTS row "
        f"(predecessor {act.predecessor.as_posix()}, its performed digest "
        f"{superseded}; new record {act.record.as_posix()}) and its offering\n"
        "  3. direction C's re-point of the read gate, with its tests; the "
        "battery, hosted workflow and CG-26 count in one edit"
    )


def check_recorded(root: pathlib.Path, act: Act, argument: str, date: str) -> int:
    try:
        outputs, block = expected_outputs(root, act, argument, date, applied=True)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED: {exc}")
        return 1
    findings = packet.check(root)
    drift = [rel for rel, content in outputs.items()
             if not (root / rel).is_file() or (root / rel).read_text() != content]
    count = (root / AGGREGATE_REL).read_text().count(block)
    for rel in drift:
        print(f"recorded act differs from regeneration: {rel.as_posix()}")
    if count != 1:
        print(f"aggregate record carries {count} copies of this act's block, not 1")
    for finding in findings:
        print(f"package: {finding}")
    if drift or count != 1 or findings:
        return 1
    print(f"recorded {act.act_type} re-pin act matches the exact owner argument; "
          "the subject hashes to it and the package verifies in its performed state")
    return 0


def record(root: pathlib.Path, act: Act, argument: str, date: str) -> int:
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()}")
        return 1
    try:
        validate(root, act, argument, applied=False)
        superseded = packet.predecessor_digest(root, _subject(act.key))
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED (before applying anything): {exc}")
        return 1
    code = packet.apply(True, (act.key,), root)
    if code != 0:
        print(f"FAILED: builder --apply {act.key} --at-adoption returned {code}; nothing recorded")
        return 1
    try:
        outputs, block = expected_outputs(root, act, argument, date, applied=True)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED after apply: {exc}\n  the subject now carries the applied patch "
              "and no record; restore it with git checkout before retrying")
        return 1
    for rel, content in outputs.items():
        (root / rel).write_text(content)
        print(f"wrote {rel.as_posix()}")
    aggregate = (root / AGGREGATE_REL).read_text()
    if aggregate.count(aggregate_heading(act, date)):
        print("FAILED: aggregate record already carries this act's heading")
        return 1
    (root / AGGREGATE_REL).write_text(aggregate.rstrip() + "\n\n" + block)
    print(f"appended one section to {AGGREGATE_REL.as_posix()}")
    print(registration_notes(act, argument, date, superseded))
    return 0


def selftest() -> int:
    results: list[tuple[str, bool]] = []
    manifest_bytes = (ROOT / packet.OUT).read_bytes()
    manifest_sha = digest(manifest_bytes)
    rows = {path: sha for sha, path in packet.ROW.findall(manifest_bytes.decode())}
    review = (ROOT / CONFIRMATION_REVIEW_REL).read_text()
    frozen_packet = committed_blob(ROOT, PACKET_HEAD, OWNER_PACKET)

    def rejects(fn, needle, *args, **kwargs):
        try:
            fn(*args, **kwargs)
        except ValueError as exc:
            return needle in str(exc)
        return False

    for act in ACTS:
        subject = _subject(act.key)
        exact = rows[subject.path.as_posix()]
        other = rows[_subject("registry" if act.key == "policy" else "policy").path.as_posix()]
        pre_subject = committed_blob(ROOT, FROZEN_SUBJECT, subject.path)
        k = act.key
        results.append((f"{k}: wrong owner argument rejected",
                        rejects(validate_artifact, "does not match the", ROOT, act, "0" * 64, False,
                                subject_override=pre_subject)))
        results.append((f"{k}: the other subject's row offered as this act's argument rejected",
                        rejects(validate_artifact, "does not match the", ROOT, act, other, False,
                                subject_override=pre_subject)))
        results.append((f"{k}: the superseded digest offered as the argument rejected",
                        rejects(validate_artifact, "does not match the", ROOT, act,
                                digest(pre_subject), False, subject_override=pre_subject)))
        pre = False
        try:
            pre = validate_artifact(ROOT, act, exact, False,
                                    subject_override=pre_subject) == manifest_sha
        except ValueError as exc:
            print(f"  ({k} exact-argument failure: {exc})")
        results.append((f"{k}: exact argument validates before adoption", pre))
        results.append((f"{k}: unapplied subject rejected in applied mode",
                        rejects(validate_artifact, "the patch was not applied",
                                ROOT, act, exact, True, subject_override=pre_subject)))
        results.append((f"{k}: subject bytes other than the superseded act's argument rejected",
                        rejects(validate_artifact, "not the superseded act's argument",
                                ROOT, act, exact, False, subject_override=pre_subject + b"\n")))
        mutated = manifest_bytes.replace(exact.encode(), ("0" * 64).encode(), 1)
        results.append((f"{k}: manifest bytes the frozen subject lacks rejected",
                        rejects(validate_artifact, "frozen subject does not carry",
                                ROOT, act, "0" * 64, False, manifest_override=mutated,
                                subject_override=pre_subject)))
        dropped = b"\n".join(line for line in manifest_bytes.split(b"\n")
                             if not line.endswith(subject.path.as_posix().encode()))
        results.append((f"{k}: manifest missing this subject's row rejected",
                        rejects(validate_artifact, "row population differs",
                                ROOT, act, exact, False, manifest_override=dropped,
                                subject_override=pre_subject)))

    staged = None
    try:
        staged = validate_packet(ROOT, manifest_sha, packet_override=frozen_packet)
    except ValueError as exc:
        print(f"  (packet-stage failure: {exc})")
    results.append(("frozen packet and the notes-only raw bind the manifest",
                    staged is not None and staged[1] == "CONFIRM WITH EXCEPTIONS"))
    live = (ROOT / OWNER_PACKET).read_bytes()
    results.append(("live packet is the frozen packet under at most one PERFORMED head",
                    strip_performed_head(live) == frozen_packet))
    leaked = frozen_packet + f"\n{phrase_for(ACTS[0], '0' * 64)}\n".encode()
    results.append(("packet carrying a transcribed digest rejected",
                    rejects(validate_packet, "carries a 64-hex token", ROOT, manifest_sha,
                            packet_override=leaked)))
    title, rest = frozen_packet.split(b"\n\n", 1)
    performed_only = title + b"\n\n> **PERFORMED 2026-10-02.** Recorded.\n\n" + rest
    results.append(("PERFORMED head alone accepted",
                    strip_performed_head(performed_only) == frozen_packet))
    results.append(("edit beneath a PERFORMED head rejected",
                    rejects(validate_packet, "packet-head commit does not carry", ROOT,
                            manifest_sha, packet_override=performed_only.replace(
                                b"binds nothing", b"binds everything", 1))))
    results.append(("packet bytes the packet head lacks rejected",
                    rejects(validate_packet, "packet-head commit does not carry", ROOT,
                            manifest_sha, packet_override=frozen_packet + b"\n")))
    line = f"Manifest SHA-256: {manifest_sha}"
    assert line in review, "fixture raw lacks the manifest line"
    results.append(("review head binding another manifest digest rejected",
                    rejects(validate_packet, "does not bind the effect manifest", ROOT,
                            manifest_sha, packet_override=frozen_packet,
                            review_override=review.replace(line, "Manifest SHA-256: " + "0" * 64, 1))))
    row_form = review.replace(line, f"Manifest SHA-256: {rows[_subject('policy').path.as_posix()]}", 1)
    results.append(("review head carrying a manifest row instead of the file digest rejected",
                    rejects(validate_packet, "does not bind the effect manifest", ROOT,
                            manifest_sha, packet_override=frozen_packet, review_override=row_form)))
    verdict = "Verdict: CONFIRM WITH EXCEPTIONS"
    assert f"\n{verdict}\n" in review, "fixture raw lacks its verdict line"
    results.append(("verdict REVISE rejected",
                    rejects(validate_packet, "does not carry the verdict", ROOT, manifest_sha,
                            packet_override=frozen_packet,
                            review_override=review.replace(verdict, "Verdict: REVISE", 1))))
    results.append(("verdict displaced past the fourth non-blank head line rejected",
                    rejects(validate_packet, "does not carry the verdict", ROOT, manifest_sha,
                            packet_override=frozen_packet,
                            review_override=review.replace(
                                f"\n{verdict}\n", f"\nReviewer note: none\n{verdict}\n", 1))))
    results.append(("a revise finding under CONFIRM WITH EXCEPTIONS rejected",
                    rejects(validate_packet, "non-note findings", ROOT, manifest_sha,
                            packet_override=frozen_packet,
                            review_override=review.replace("** (note)", "** (revise)", 1))))
    results.append(("an unclassified finding rejected",
                    rejects(validate_packet, "severity", ROOT, manifest_sha,
                            packet_override=frozen_packet,
                            review_override=review.replace("** (note)", "**", 1))))
    extra = review.replace("## What I verified",
                           "**Finding 3 — extra** (note)\n\nundispositioned\n\n## What I verified", 1)
    results.append(("a finding the disposition record does not cover rejected",
                    rejects(validate_packet, "do not match", ROOT, manifest_sha,
                            packet_override=frozen_packet, review_override=extra)))
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        scratch = pathlib.Path(tmp)
        (scratch / DISPOSITION_REL).parent.mkdir(parents=True)
        text = (ROOT / DISPOSITION_REL).read_text()
        (scratch / DISPOSITION_REL).write_text(text.replace(
            f"Reviewed record: {CONFIRMATION_REVIEW_REL.as_posix()}", "Reviewed record: elsewhere", 1))
        results.append(("a disposition record not naming the raw rejected",
                        rejects(validate_packet, "does not name the reviewed raw", ROOT,
                                manifest_sha, packet_override=frozen_packet,
                                disposition_root=scratch)))
    act = ACTS[1]
    rendered = render_act(act, "a" * 64, "2026-10-02", manifest_sha, "b" * 40,
                          "CONFIRM WITH EXCEPTIONS", "c" * 64)
    effect = rendered.split("## Effect", 1)[1].split("## ", 1)[0]
    flat = " ".join(effect.split())
    results.append(("registry record's Effect carries every read-gate scope anchor",
                    all(a in flat for a in act.anchors)))
    policy_effect = " ".join(render_act(ACTS[0], "a" * 64, "2026-10-02", manifest_sha,
                                        "b" * 40, "CONFIRM", "c" * 64)
                             .split("## Effect", 1)[1].split("## ", 1)[0].split())
    results.append(("policy record's Effect carries every read-gate scope anchor",
                    all(a in policy_effect for a in ACTS[0].anchors)))
    results.append(("record's supersession line is the one-line form the gate parses",
                    re.search(r"^Supersession / revocation: this act supersedes, for the "
                              r"`adopt-registry-entry` role only, the 2026-09-30 act recorded at "
                              r"`[^`]+`\.$", rendered, re.M) is not None))
    with contextlib.redirect_stdout(io.StringIO()):
        bad_date = main_args(["--check", "policy", "0" * 64, "--date", "02-10-2026"])
    results.append(("malformed --date rejected", bad_date == 1))
    failing = 0
    for name, passed in results:
        failing += 0 if passed else 1
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"{len(results)} recording fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main_args(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", nargs=2, metavar=("SUBJECT", "ARGUMENT"))
    mode.add_argument("--check", nargs=2, metavar=("SUBJECT", "ARGUMENT"))
    mode.add_argument("--selftest", action="store_true")
    parser.add_argument("--date", metavar="YYYY-MM-DD",
                        help="the date the owner gave the act")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.date or not DATE_RE.fullmatch(args.date):
        print("FAILED: --date YYYY-MM-DD is required with --record/--check")
        return 1
    key, argument = args.record or args.check
    if key not in ACT_BY_KEY:
        print(f"FAILED: subject must be one of {sorted(ACT_BY_KEY)}")
        return 1
    act = ACT_BY_KEY[key]
    if args.check:
        return check_recorded(ROOT, act, argument, args.date)
    return record(ROOT, act, argument, args.date)


if __name__ == "__main__":
    sys.exit(main_args(sys.argv[1:]))
