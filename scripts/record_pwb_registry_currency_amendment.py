#!/usr/bin/env python3
"""Record or verify the superseding PWB registry currency-and-briefing act.

Gate bead `syzygy-dov.18`; package
`contracts/candidates/pwb-registry-currency-briefing-amendment/`. The act is
one `adopt-registry-entry` owner act in the shape of the 2026-09-05 record,
superseding `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` for that role
only, over the same subject. The phrase form is unchanged:
`ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: <sha256>`,
where the argument is the SHA-256 of the registry artifact itself.

The argument is deliberately absent from every Markdown file in the
package: the bytes that hash to it exist only as the result of applying
`proposed/*.patch` to the bytes the act in force bound, and the package's
one-row `PWB-EFFECT-AMENDMENT-MANIFEST.txt` carries that digest
machine-derived. This script performs nothing by itself. `--record` accepts
the owner's exact argument, requires it to equal the manifest row and the
digest of the builder's proposed bytes, requires the current subject bytes
to be exactly the predecessor act's argument, applies the patch through the
builder (`--apply --at-adoption` semantics), confirms the subject now hashes
to the argument, and writes the dedicated record and one aggregate section
of `ACCEPTANCE-ACT-RECORD.md`. `--check` re-derives both after adoption.
`--selftest` mutates each predicate and requires it to fail closed.

At adoption the performing change also adds, in `check_governance.py`, the
new `PWB_EFFECT_AMENDMENT_ACTS` row (new record path, act-time digest), the
existence-gated copy registration of the new record, and the record's own
entry; and `scripts/build_pwb_truth_policy_amendment.py --check` goes red
by design because the subject bytes it hashes have moved (packet open
question 4). This script prints those consequences and edits no check.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys

import build_pwb_registry_currency_briefing_amendment as packet


ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
OWNER_PACKET = packet.CANDIDATE / "OWNER-DECISION-PACKET.md"
CONFIRMATION_REVIEW_REL = pathlib.Path(
    "docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-CONFIRMATION-RAW.md"
)
#: The commit on main carrying the package bytes (manifest, patch, packet)
#: the offered argument is derived from. Re-set, never hand-edited, whenever
#: the patch or an owner value changes.
FROZEN_SUBJECT = "9d741859dceee935f256b99ebb68e095545b868b"
PACKET_HEAD = "9d741859dceee935f256b99ebb68e095545b868b"
ACT_TYPE = "adopt-registry-entry"
ACT_LABEL = "ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY"
RECORD_REL = DECISIONS / "PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md"
PREDECESSOR_REL = DECISIONS / "PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md"
PREDECESSOR_DATE = "2026-09-05"
IDENTITY = "PWB-OBSERVER-REGISTRY-ENTRY-CURRENCY-BRIEFING-AMENDMENT"
TITLE = ("Polaris Butlers project-shape observer registry-entry adoption "
         "(currency bounds and briefing ceiling amendment)")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
EXACT_DIGEST_RE = re.compile(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`\s*$", re.MULTILINE)
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$", re.MULTILINE)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(argument: str) -> str:
    return f"{ACT_LABEL}: {argument}"


def committed_blob(root: pathlib.Path, commit: str, rel: pathlib.Path) -> bytes:
    done = subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{rel.as_posix()}"],
        capture_output=True,
    )
    if done.returncode != 0:
        raise ValueError(
            f"cannot read {rel.as_posix()} at {commit}: "
            f"{done.stderr.decode().strip() or 'git show failed'}"
        )
    return done.stdout


def predecessor_digest(root: pathlib.Path) -> str:
    record = root / PREDECESSOR_REL
    if not record.is_file():
        raise ValueError(f"superseded {PREDECESSOR_DATE} act record missing: {PREDECESSOR_REL.as_posix()}")
    found = EXACT_DIGEST_RE.findall(record.read_text())
    if len(found) != 1:
        raise ValueError("superseded act record does not carry exactly one exact digest line")
    return found[0]


def validate_artifact(
    root: pathlib.Path, argument: str, applied: bool,
    manifest_override: bytes | None = None, subject_override: bytes | None = None,
) -> str:
    """Stage 1 — the phrase names the proposed bytes, and the tree is in the right state.

    `applied=False` (before adoption): the subject's current bytes are the
    predecessor act's argument, the builder verifies, and the argument is
    the digest of its proposed bytes. `applied=True` (after adoption): the
    subject hashes to the argument. In both states the manifest row equals
    the argument and the frozen subject carries the manifest bytes.
    Returns the manifest's SHA-256, which the confirmation review binds.
    """
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    manifest_path = root / packet.OUT
    if manifest_override is None and not manifest_path.is_file():
        raise ValueError(f"missing effect manifest: {packet.OUT.as_posix()}")
    manifest_bytes = (manifest_override if manifest_override is not None
                      else manifest_path.read_bytes())
    rows = packet.ROW.findall(manifest_bytes.decode())
    if [path for _sha, path in rows] != [packet.SUBJECT.as_posix()]:
        raise ValueError("effect manifest row population or path differs")
    if rows[0][0] != argument:
        raise ValueError(
            f"owner argument {argument} does not match the effect manifest row {rows[0][0]}"
        )
    if committed_blob(root, FROZEN_SUBJECT, packet.OUT) != manifest_bytes:
        raise ValueError("frozen subject does not carry the presented effect manifest bytes")
    subject_path = root / packet.SUBJECT
    if subject_override is None and not subject_path.is_file():
        raise ValueError(f"artifact missing: {packet.SUBJECT.as_posix()}")
    subject_bytes = subject_override if subject_override is not None else subject_path.read_bytes()
    current_sha = digest(subject_bytes)
    if applied:
        if current_sha != argument:
            raise ValueError(
                f"subject hashes to {current_sha}, not the owner argument; the patch was not applied"
            )
    else:
        superseded = predecessor_digest(root)
        if current_sha != superseded:
            raise ValueError(
                f"subject hashes to {current_sha}, not the superseded act's argument "
                f"{superseded}; the package was drafted over different bound bytes"
            )
        findings = packet.check() if subject_override is None else []
        if findings:
            raise ValueError("package does not verify: " + " | ".join(findings))
        proposed = packet.proposed_bytes(subject_override)
        if digest(proposed) != argument:
            raise ValueError("owner argument does not match the digest of the proposed bytes")
    return digest(manifest_bytes)


def validate_packet(
    root: pathlib.Path, argument: str, manifest_sha: str,
    packet_override: bytes | None = None, review_override: str | None = None,
) -> str:
    """Stage 2 — the owner was shown the reviewed packet, which carries no digest.

    Returns the reviewed commit the raw states (provenance, not binding).
    """
    packet_path = root / OWNER_PACKET
    if packet_override is None and not packet_path.is_file():
        raise ValueError(f"missing owner packet: {OWNER_PACKET.as_posix()}")
    packet_bytes = packet_override if packet_override is not None else packet_path.read_bytes()
    if HEX64_RE.search(packet_bytes.decode()):
        raise ValueError(
            "owner packet carries a 64-hex token; the package declares its argument "
            "absent from every Markdown file and derived only from the manifest row"
        )
    if committed_blob(root, PACKET_HEAD, OWNER_PACKET) != packet_bytes:
        raise ValueError("packet-head commit does not carry the presented packet bytes")
    review_path = root / CONFIRMATION_REVIEW_REL
    if review_override is None and not review_path.is_file():
        raise ValueError(f"missing confirmation review: {CONFIRMATION_REVIEW_REL.as_posix()}")
    review = review_override if review_override is not None else review_path.read_text()
    head = review.splitlines()[:4]
    if f"Manifest SHA-256: {manifest_sha}" not in head:
        raise ValueError("confirmation review does not bind the offered effect manifest")
    if "Verdict: CONFIRM" not in head:
        raise ValueError("confirmation review head does not carry the exact verdict CONFIRM")
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    return reviewed.group(1)


def validate(root: pathlib.Path, argument: str, applied: bool) -> tuple[str, str]:
    manifest_sha = validate_artifact(root, argument, applied)
    return manifest_sha, validate_packet(root, argument, manifest_sha)


def tag_for(date: str) -> str:
    return f"pwb-{ACT_TYPE}-signed-{date}"


def render_act(argument: str, date: str, manifest_sha: str, reviewed: str,
               superseded_digest: str) -> str:
    return f"""# Owner act — {TITLE}

Date: {date}

Owner: Tzeusy

Act identity: `{IDENTITY}-{date}`

Act type: `{ACT_TYPE}`

Project identity: `project:syzygy`

Artifact identity: `{packet.SUBJECT.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by performing the offered state-(1) phrase

Supersession / revocation: this act supersedes, for the `{ACT_TYPE}` role
only, the {PREDECESSOR_DATE} act recorded at `{PREDECESSOR_REL.as_posix()}`,
whose argument `{superseded_digest}` was the subject's exact digest until
this act's patch was applied. That record, its digest, its tag and the bytes
it bound remain immutable history. This act is revoked only by a later exact
owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`{OWNER_PACKET.as_posix()}`,
which by design carries no digest, and performed this one act by writing
exactly:

```text
{phrase_for(argument)}
```

The argument is the SHA-256 of the artifact itself. It was recomputed at
recording from the package's proposed bytes, matched the single row of
`{packet.OUT.as_posix()}`,
and, after the package's patch was applied through its builder in the same
change, matched the artifact on disk. The act instant is the moment the
owner wrote the phrase, in-interaction, on {date}.

Frozen provenance:

- frozen subject (package bytes): `{FROZEN_SUBJECT}`;
- owner-packet head: `{PACKET_HEAD}`;
- effect manifest SHA-256: `{manifest_sha}`;
- confirmation review: `{CONFIRMATION_REVIEW_REL.as_posix()}`, verdict
  `CONFIRM`, bound to that manifest digest; the raw names reviewed commit
  `{reviewed}` [Observed — the raw's own line; binding is by digest]; and
- recording tag: `{tag_for(date)}`, on the commit carrying this act record.

## Effect

The amended adapter-registry entry (`polaris-butlers-project-shape`,
version `{packet.PROPOSED_VERSION}`) is adopted in Syzygy's governance home
`.syzygy/governance/declarations/adapter-registry` for `project:syzygy` and
the configured Butlers repository, in place of the {PREDECESSOR_DATE} entry
(version `{packet.CURRENT_VERSION}`), with read-only authority and an empty
write surface. It keeps the signed PWB source population, the policy that
screens it, the closed observation grammar, the deterministic resource
envelope and the absence of write, execution, egress and second-repository
capability, and adds two declarations the owner chose value by value:
{len(packet.CURRENCY_CLASSES)} explicit per-class currency bounds under one
closed semantics block (P-69 question 2, arm (a)), under which an
undeclared class remains Unknown and an out-of-bound assessment is a typed
result, never a guess; and one further response ceiling,
`{packet.BRIEFING_LIMIT_KEY}` (P-72 question 2), which bounds a
single-subject view built from an already-served evaluation and serves
bounded typed failure, never truncated success. The entry is a declared
mapping: adopting it changes no code and authorizes none to be written.

## What this act does not authorize

This act is one of the three separate authorities PWB-REQ-005 requires and
satisfies only its own. It grants no observation consent and approves no
secret-classification policy. No implementation consumes the new fields
until the owner issues the separate plain continuation direction the
ruling record names, and no briefing route is served before the derived
read-only machine-view specification is signed off and its ceiling is
declared. It leaves the entry's `status` and `adoptionStatus` keys, which
carry its governance lifecycle, byte-identical.

It grants no write, egress, execution, deployment, release, recovery,
mission, second-repository, autonomous or multi-user authority, widens no
consent, edits no signed artifact, accepts no candidate contract and amends
no doctrine. It proves no read, screening, parse, render or answer result.
"""


def aggregate_heading(date: str) -> str:
    return f"## PWB effect-act amendment — {ACT_TYPE} — currency and briefing — performed {date}"


def render_aggregate_block(argument: str, date: str, manifest_sha: str) -> str:
    return f"""{aggregate_heading(date)}

**Phrase, exactly as written by the owner (in-interaction, {date}):**

```text
{phrase_for(argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{ACT_TYPE}` / `{packet.SUBJECT.as_posix()}` |
| Argument | SHA-256 of the artifact itself, recomputed at recording and equal to the phrase, the effect-manifest row and the artifact on disk after the package's patch was applied |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Supersession | the {PREDECESSOR_DATE} `{ACT_TYPE}` act recorded at `{PREDECESSOR_REL.as_posix()}`; that act, its digest and its tag remain immutable history |
| Frozen subject / packet head | `{FROZEN_SUBJECT}` / `{PACKET_HEAD}` |
| Effect manifest | `{packet.OUT.as_posix()}`, SHA-256 `{manifest_sha}` |
| Review outcome | `{CONFIRMATION_REVIEW_REL.as_posix()}`: `CONFIRM`, bound to that manifest digest |
| Recording | `{RECORD_REL.as_posix()}`; annotated tag `{tag_for(date)}` on the commit carrying these records |

Effective status: this one amended artifact is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own PWB-REQ-005 role only.
The other effect authorities, the plain continuation direction and the
machine-view sign-off remain separate; no body read, write, egress,
execution, deployment, release, recovery or mission authority follows from
this act.
"""


def expected_outputs(root: pathlib.Path, argument: str, date: str,
                     applied: bool) -> dict[pathlib.Path, str]:
    manifest_sha, reviewed = validate(root, argument, applied)
    superseded = predecessor_digest(root)
    aggregate = (root / AGGREGATE_REL).read_text()
    heading = aggregate_heading(date)
    occurrences = aggregate.count(heading)
    if occurrences > 1:
        raise ValueError("aggregate record contains duplicate sections for this act")
    prefix = aggregate.split(heading, 1)[0].rstrip() if occurrences else aggregate.rstrip()
    return {
        RECORD_REL: render_act(argument, date, manifest_sha, reviewed, superseded),
        AGGREGATE_REL: prefix + "\n\n" + render_aggregate_block(argument, date, manifest_sha),
    }


def registration_notes(argument: str, date: str, superseded: str) -> str:
    return (
        "next, in the same change:\n"
        f"  1. git add {packet.SUBJECT.as_posix()} and the two records, commit, "
        f"then tag {tag_for(date)} on that commit\n"
        "  2. scripts/check_governance.py: add the PWB_EFFECT_AMENDMENT_ACTS row "
        f"(predecessor {PREDECESSOR_REL.as_posix()}, its performed digest "
        f"{superseded}; new record {RECORD_REL.as_posix()}, act-time digest "
        f"{argument}), the existence-gated ACT_DIGEST_COPY_FILES registration "
        "of the new record, and the record's own entry\n"
        "  3. scripts/build_pwb_truth_policy_amendment.py --check now fails by "
        "design (the subject bytes moved); disclose it beside the battery, "
        "and update the count sentence and hosted workflow together (CG-26)"
    )


def record(root: pathlib.Path, argument: str, date: str, check: bool) -> int:
    if not DATE_RE.fullmatch(date):
        print("FAILED: --date must be YYYY-MM-DD")
        return 1
    if check:
        try:
            outputs = expected_outputs(root, argument, date, applied=True)
            manifest_sha = digest((root / packet.OUT).read_bytes())
        except (ValueError, subprocess.CalledProcessError) as exc:
            print(f"FAILED: {exc}")
            return 1
        drift = []
        dedicated = root / RECORD_REL
        if not dedicated.is_file() or dedicated.read_text() != outputs[RECORD_REL]:
            drift.append(RECORD_REL)
        aggregate = (root / AGGREGATE_REL).read_text()
        if aggregate.count(render_aggregate_block(argument, date, manifest_sha)) != 1:
            drift.append(AGGREGATE_REL)
        for rel in drift:
            print(f"recorded act differs from regeneration: {rel.as_posix()}")
        if drift:
            return 1
        print("recorded superseding adopt-registry-entry act matches exact owner "
              "argument; the subject hashes to it")
        return 0
    if (root / RECORD_REL).exists():
        print(f"FAILED: dedicated act already exists: {RECORD_REL.as_posix()}")
        return 1
    try:
        validate(root, argument, applied=False)
        superseded = predecessor_digest(root)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED (before applying anything): {exc}")
        return 1
    code = packet.apply(True)
    if code != 0:
        print(f"FAILED: builder --apply --at-adoption returned {code}; nothing recorded")
        return 1
    try:
        outputs = expected_outputs(root, argument, date, applied=True)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED after apply: {exc}\n  the subject now carries the applied "
              "patch and no record; restore it with git checkout before retrying")
        return 1
    for rel, content in outputs.items():
        (root / rel).write_text(content)
        print(f"wrote {rel.as_posix()}")
    print(registration_notes(argument, date, superseded))
    return 0


def selftest() -> int:
    results = []
    manifest_bytes = (ROOT / packet.OUT).read_bytes()
    exact = packet.ROW.findall(manifest_bytes.decode())[0][0]
    manifest_sha = digest(manifest_bytes)
    packet_bytes = (ROOT / OWNER_PACKET).read_bytes()
    review = (ROOT / CONFIRMATION_REVIEW_REL).read_text()

    def rejects(fn, needle, *args, **kwargs):
        try:
            fn(*args, **kwargs)
        except ValueError as exc:
            return needle in str(exc)
        return False

    results.append(("wrong owner argument rejected",
                    rejects(validate_artifact, "does not match the effect manifest row",
                            ROOT, "0" * 64, False)))
    current_sha = digest((ROOT / packet.SUBJECT).read_bytes())
    results.append(("current (superseded) subject digest offered as argument rejected",
                    rejects(validate_artifact, "does not match the effect manifest row",
                            ROOT, current_sha, False)))
    pre = False
    try:
        pre = validate_artifact(ROOT, exact, False) == manifest_sha
    except ValueError as exc:
        print(f"  (exact-argument failure: {exc})")
    results.append(("exact argument validates before adoption", pre))
    results.append(("unapplied subject rejected in applied mode",
                    rejects(validate_artifact, "the patch was not applied",
                            ROOT, exact, True)))
    drifted_subject = (ROOT / packet.SUBJECT).read_bytes() + b"\n"
    results.append(("subject bytes other than the superseded act's argument rejected",
                    rejects(validate_artifact, "not the superseded act's argument",
                            ROOT, exact, False, subject_override=drifted_subject)))
    mutated_manifest = manifest_bytes.replace(exact.encode(), ("0" * 64).encode(), 1)
    results.append(("manifest bytes the frozen subject lacks rejected",
                    rejects(validate_artifact, "frozen subject does not carry",
                            ROOT, "0" * 64, False, manifest_override=mutated_manifest)))
    staged = False
    try:
        staged = bool(validate_packet(ROOT, exact, manifest_sha))
    except ValueError as exc:
        print(f"  (packet-stage failure: {exc})")
    results.append(("packet and confirmation review bind the argument", staged))
    leaked = packet_bytes + f"\n{phrase_for(exact)}\n".encode()
    results.append(("packet carrying a transcribed digest rejected",
                    rejects(validate_packet, "carries a 64-hex token",
                            ROOT, exact, manifest_sha, packet_override=leaked)))
    drifted = packet_bytes + b"\n"
    results.append(("packet bytes the packet head lacks rejected",
                    rejects(validate_packet, "packet-head commit does not carry",
                            ROOT, exact, manifest_sha, packet_override=drifted)))
    unbound = review.replace(f"Manifest SHA-256: {manifest_sha}", "Manifest SHA-256: " + "0" * 64, 1)
    results.append(("review not binding the effect manifest rejected",
                    rejects(validate_packet, "does not bind the offered effect manifest",
                            ROOT, exact, manifest_sha, review_override=unbound)))
    wrong_verdict = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS", 1)
    results.append(("review verdict other than CONFIRM rejected",
                    rejects(validate_packet, "exact verdict CONFIRM",
                            ROOT, exact, manifest_sha, review_override=wrong_verdict)))
    failing = 0
    for name, passed in results:
        failing += 0 if passed else 1
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"{len(results)} recording fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--record", metavar="ARTIFACT_SHA")
    parser.add_argument("--check", metavar="ARTIFACT_SHA")
    parser.add_argument("--date", metavar="YYYY-MM-DD", help="the date the owner wrote the phrase")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    selected = sum(bool(v) for v in (args.record, args.check, args.selftest))
    if selected != 1:
        parser.error("choose exactly one of --record, --check or --selftest")
    if args.selftest:
        return selftest()
    if not args.date:
        parser.error("--date is required with --record/--check")
    return record(ROOT, args.record or args.check, args.date, check=bool(args.check))


if __name__ == "__main__":
    sys.exit(main())
