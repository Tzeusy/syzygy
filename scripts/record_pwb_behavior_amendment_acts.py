#!/usr/bin/env python3
"""Record or verify an owner-signed PWB behavior-amendment act (table-driven).

Each entry in `ACTS` is one candidate package over the eleven-artifact PWB
behavior population whose act would be a new link in the successor chain
(`PWB_SUCCESSOR_CHAIN` in `scripts/check_governance.py`). The act phrase is
`<LABEL>: <sha256 of the package's behavior manifest>`; the manifest rows
hash the PROPOSED bytes, so the act and the application of the package's
`proposed/*.patch` are one change.

This script performs nothing by itself. `--record` accepts the owner's
exact argument, recomputes it from the manifest bytes, checks that the
frozen subject, the presented packet and the confirmation review all bind
the same manifest digest, applies the package's patches through its own
builder (`--apply --at-adoption` semantics), confirms every manifest row
now hashes the tree, and writes the dedicated act record and one aggregate
section of `ACCEPTANCE-ACT-RECORD.md`. `--check` re-derives both records
from the tree after adoption and requires exactly one copy of the aggregate
block (later acts append after it). `--selftest` mutates each predicate and
requires it to fail closed.

Pins. Each entry's `frozen_subject` is the commit on `main` whose manifest
and packet bytes the offered phrase binds. Whenever a package's manifest is
regenerated (a later-landing package re-derives `GOVERNING-DEPENDENCIES.md`
and its row moves), the argument changes, the packet copy is re-derived,
a fresh confirmation review is needed, and this entry's pins are re-set —
never edited into agreement by hand. Review commits are cited as the raw
states them; review binding is by manifest digest, because a rebase-merge
can leave a branch-head commit reachable from no ref.

The successor-chain link and the existence-gated copy registrations in
`check_governance.py` are the performing change's to add; this script
prints what it knows and edits no check.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import pathlib
import re
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$", re.MULTILINE)
EXPECTED_ROWS = 11


class Act:
    def __init__(self, act_type, builder, label, record_name, identity, title,
                 frozen_subject, packet_head, confirmation_review, tag_stem,
                 effect, not_authorized):
        self.act_type = act_type
        self.builder = builder
        self.label = label
        self.record = DECISIONS / record_name
        self.identity = identity
        self.title = title
        self.frozen_subject = frozen_subject
        self.packet_head = packet_head
        self.confirmation_review = pathlib.Path(confirmation_review)
        self.tag_stem = tag_stem
        self.effect = effect
        self.not_authorized = not_authorized
        self._module = None

    @property
    def module(self):
        if self._module is None:
            self._module = importlib.import_module(self.builder)
        return self._module

    @property
    def candidate(self) -> pathlib.Path:
        return self.module.CANDIDATE

    @property
    def packet(self) -> pathlib.Path:
        return self.candidate / "OWNER-DECISION-PACKET.md"

    @property
    def manifest(self) -> pathlib.Path:
        return self.module.BEHAVIOR_OUT

    @property
    def subjects(self) -> tuple[pathlib.Path, ...]:
        return tuple(self.module.BEHAVIOR_SUBJECTS)

    @property
    def patched(self) -> tuple[pathlib.Path, ...]:
        return tuple(self.module.PATCHED)


ACTS = {
    "render-mode": Act(
        "render-mode",
        "build_pwb_exact_source_render_mode_amendment",
        "SIGN OFF PWB EXACT-SOURCE RENDER-MODE AMENDMENT",
        "PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md",
        "PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-SIGNOFF",
        "PWB exact-source render-mode amendment sign-off",
        # main commit carrying the offered manifest and packet bytes
        "9d741859dceee935f256b99ebb68e095545b868b",
        "9d741859dceee935f256b99ebb68e095545b868b",
        "docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-CONFIRMATION-RAW.md",
        "pwb-exact-source-render-mode-amendment",
        """PWB-REQ-011 is amended so that the exact-source route serves every source
the evaluation admitted as a classified blob, in exactly one render mode
drawn from a closed two-mode set: the existing requirement-section mode for
sources with requirement headings, and a whole-body mode for the rest. A
source whose record outcome is excluded is served in no mode, as its own
invariant and scenario. Every mode applies the same authority, exact-object,
secret-detection and inert-content gates to the complete transient body
before encoding any part of it; a failed gate leaves the body Unknown with
its reason. Each served mode exposes a presentation-only scroll anchor per
reading unit a citation can name, which never enters, replaces or qualifies
any source, claim or narrative anchor identity. Each served route's mode,
each source identity and each refusal's reason are recoverable per rendered
tuple from the same evaluation in the machine answer, so the parity sweep
extends over the anchor parameter. `design.md` §8 carries the argument for
the wider source population inside the one consented content class,
`CAPABILITY-COVERAGE.md` row 10 restates the obligation, and
`GOVERNING-DEPENDENCIES.md` is regenerated.""",
        """No content class widens: the route reads only what the performed consent
covers, and the nine withheld sources (seven TOML butler manifests, one
frontend page, one excluded artifact) stay digest-only with the source
denominator unchanged. No detector changes. PWB-REQ-014, PWB-REQ-020,
PWB-REQ-003, -005, -006 and -015 are not amended; the P-81 Q5 PWB-REQ-015
delta and the P-82 PWB-REQ-002 delta are separate changes. This act
authorizes no implementation of the amended semantics: the pursuit bead
under M14 opens only under a fresh, separate owner authorization, and the
269-of-278 figure and the page-size effect are measured there, never
assumed here.""",
    ),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


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


def manifest_rows(text: str, act: Act) -> list[tuple[str, str]]:
    rows = ROW_RE.findall(text)
    if len(rows) != EXPECTED_ROWS:
        raise ValueError(f"manifest carries {len(rows)} rows, expected {EXPECTED_ROWS}")
    expected_paths = [p.as_posix() for p in act.subjects]
    if [path for _sha, path in rows] != expected_paths:
        raise ValueError("manifest path population or order differs from the builder's subjects")
    return rows


def validate_subject(
    root: pathlib.Path, act: Act, argument: str, applied: bool,
    manifest_override: bytes | None = None,
) -> list[tuple[str, str]]:
    """Stage 1 — the phrase names the manifest, and the manifest names the tree.

    `applied=False` is the pre-adoption state: the rows must equal the
    builder's PROPOSED bytes and the builder's own `--check` must be clean.
    `applied=True` is the post-adoption state: every row must hash the tree.
    Returns the rows.
    """
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    manifest_path = root / act.manifest
    if manifest_override is None and not manifest_path.is_file():
        raise ValueError(f"missing manifest: {act.manifest.as_posix()}")
    manifest_bytes = (manifest_override if manifest_override is not None
                      else manifest_path.read_bytes())
    manifest_sha = digest(manifest_bytes)
    if argument != manifest_sha:
        raise ValueError(
            f"owner argument {argument} does not match manifest {manifest_sha}"
        )
    if committed_blob(root, act.frozen_subject, act.manifest) != manifest_bytes:
        raise ValueError("frozen subject does not carry the presented manifest bytes")
    rows = manifest_rows(manifest_bytes.decode(), act)
    if applied:
        for expected_sha, path in rows:
            target = root / path
            actual = digest(target.read_bytes()) if target.is_file() else "absent"
            if actual != expected_sha:
                raise ValueError(f"manifest row does not hash the tree: {path}")
    else:
        findings = act.module.check()
        if findings:
            raise ValueError("package does not verify: " + " | ".join(findings))
        proposed = act.module.proposed_bytes()
        for expected_sha, path in rows:
            if digest(proposed[pathlib.Path(path)]) != expected_sha:
                raise ValueError(f"manifest row does not hash the proposed bytes: {path}")
    return rows


def validate_packet(
    root: pathlib.Path, act: Act, argument: str,
    packet_override: bytes | None = None, review_override: str | None = None,
) -> str:
    """Stage 2 — the owner was shown this phrase, and a review confirmed these bytes.

    Returns the reviewed commit the raw states (provenance, not binding).
    """
    packet_path = root / act.packet
    if packet_override is None and not packet_path.is_file():
        raise ValueError(f"missing owner packet: {act.packet.as_posix()}")
    packet_bytes = packet_override if packet_override is not None else packet_path.read_bytes()
    if packet_bytes.decode().count(phrase_for(act, argument)) != 1:
        raise ValueError("owner packet does not contain exactly one exact phrase")
    if committed_blob(root, act.packet_head, act.packet) != packet_bytes:
        raise ValueError("packet-head commit does not carry the presented packet bytes")
    review_path = root / act.confirmation_review
    if review_override is None and not review_path.is_file():
        raise ValueError(f"missing confirmation review: {act.confirmation_review.as_posix()}")
    review = review_override if review_override is not None else review_path.read_text()
    lines = review.splitlines()
    head = lines[:4]
    if f"Manifest SHA-256: {argument}" not in head:
        raise ValueError("confirmation review does not bind the offered manifest digest")
    if "Verdict: CONFIRM" not in head:
        raise ValueError("confirmation review head does not carry the exact verdict CONFIRM")
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    return reviewed.group(1)


def validate(root: pathlib.Path, act: Act, argument: str, applied: bool):
    rows = validate_subject(root, act, argument, applied)
    reviewed = validate_packet(root, act, argument)
    return rows, reviewed


def tag_for(act: Act, date: str) -> str:
    return f"{act.tag_stem}-signed-{date}"


def render_act(act: Act, argument: str, date: str, rows, reviewed: str) -> str:
    artifact_table = "\n".join(f"| `{path}` | `{sha}` |" for sha, path in rows)
    return f"""# Owner act — {act.title}

Date: {date}

Owner: Tzeusy

Act identity: `{act.identity}-{date}`

Project identity: `project:syzygy`

Provenance state: `owner-adopted (bootstrap, uncorrelated)`

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the independently confirmed packet at
`{act.packet.as_posix()}`
and performed the offered indivisible behavior amendment by writing exactly:

```text
{phrase_for(act, argument)}
```

The argument is the SHA-256 of
`{act.manifest.as_posix()}`.
It was recomputed at recording and matched the phrase. The manifest bytes
were verified against frozen subject `{act.frozen_subject}`; the package's
patches were applied through its builder in the same change, and all eleven
rows were then verified to hash the tree. The presented packet bytes were
verified against the packet head. The act instant is the moment the owner
wrote the phrase, in-interaction, on {date}.

Frozen provenance:

- frozen subject (manifest and packet bytes): `{act.frozen_subject}`;
- owner-packet head: `{act.packet_head}`;
- confirmation review: `{act.confirmation_review.as_posix()}`, verdict
  `CONFIRM`, bound to this manifest digest; the raw names reviewed commit
  `{reviewed}` [Observed — the raw's own line; binding is by digest]; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

{act.effect}

This act is the latest link over the eleven-artifact PWB behavior
population. Every earlier act's rows remain immutable act-time history;
none is edited, retired or re-hashed by this record.

## Signed artifacts

| Repository-relative artifact | sha256 |
|---|---|
{artifact_table}

All eleven rows take effect together or none do. An edit to any listed
artifact breaks this act's digest binding and must use the amendment path.

## What this act does not authorize

{act.not_authorized}

It approves no policy, adopts no registry entry, widens no consent, and
grants no write, egress, observed-code execution, deployment, release,
recovery, mission, second repository, wider content class, autonomous
behavior or multi-user support. It proves no read, screening, parse, render,
answer or comprehension result. It does not edit the signed parent
`three-surface-poc-experience` artifacts, accept RFC 0010 or RFC 0011, amend
doctrine, or start automatic follow-on work.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## PWB behavior amendment — {act.act_type} — performed {date}"


def render_aggregate_block(act: Act, argument: str, date: str) -> str:
    return f"""{aggregate_heading(act, date)}

**Phrase, exactly as written by the owner (in-interaction, {date}):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Argument | SHA-256 of `{act.manifest.as_posix()}`, recomputed at recording and equal to the phrase |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Frozen subject / packet head | `{act.frozen_subject}` / `{act.packet_head}` |
| Review outcome | `{act.confirmation_review.as_posix()}`: `CONFIRM`, bound to this manifest digest |
| Ceremony verification | {EXPECTED_ROWS} of {EXPECTED_ROWS} manifest rows verified against the tree after the package's patches were applied; manifest digest equals the phrase `[Observed, this act]` |
| Supersession | the latest link over the eleven-artifact PWB behavior population; every earlier act's rows remain immutable history |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: the eleven-artifact PWB package is **signed behavioral
authority — owner-adopted (bootstrap, uncorrelated)** at these bytes.

This act approves no policy, adopts no registry entry, widens no consent and
authorizes no implementation of the amended semantics; no write, egress,
execution, deployment, release, recovery or mission authority follows from
this act.
"""


def expected_outputs(root: pathlib.Path, act: Act, argument: str, date: str,
                     applied: bool) -> dict[pathlib.Path, str]:
    rows, reviewed = validate(root, act, argument, applied)
    aggregate = (root / AGGREGATE_REL).read_text()
    heading = aggregate_heading(act, date)
    occurrences = aggregate.count(heading)
    if occurrences > 1:
        raise ValueError("aggregate record contains duplicate sections for this act")
    prefix = aggregate.split(heading, 1)[0].rstrip() if occurrences else aggregate.rstrip()
    return {
        act.record: render_act(act, argument, date, rows, reviewed),
        AGGREGATE_REL: prefix + "\n\n" + render_aggregate_block(act, argument, date),
    }


def registration_notes(act: Act, argument: str, date: str) -> str:
    return (
        "next, in the same change:\n"
        f"  1. git add the applied subjects ({len(act.patched)} patched files), "
        f"the two records, then commit and tag {tag_for(act, date)} on that commit\n"
        "  2. scripts/check_governance.py: append the PWB_SUCCESSOR_CHAIN link "
        f"for label {act.label!r} (its copy registration is already existence-gated)\n"
        "  3. run the PROJECT-STATUS.md battery; this package's builder --check "
        "now fails by design (proposed == current) and must leave the battery "
        "with the count sentence and hosted workflow updated together (CG-26)\n"
        f"  argument recorded: {argument}"
    )


def record(root: pathlib.Path, act: Act, argument: str, date: str, check: bool) -> int:
    if not DATE_RE.fullmatch(date):
        print("FAILED: --date must be YYYY-MM-DD")
        return 1
    if check:
        try:
            outputs = expected_outputs(root, act, argument, date, applied=True)
        except (ValueError, subprocess.CalledProcessError) as exc:
            print(f"FAILED: {exc}")
            return 1
        drift = []
        dedicated = root / act.record
        if not dedicated.is_file() or dedicated.read_text() != outputs[act.record]:
            drift.append(act.record)
        aggregate = (root / AGGREGATE_REL).read_text()
        if aggregate.count(render_aggregate_block(act, argument, date)) != 1:
            drift.append(AGGREGATE_REL)
        for rel in drift:
            print(f"recorded act differs from regeneration: {rel.as_posix()}")
        if drift:
            return 1
        print(f"recorded PWB {act.act_type} behavior amendment act matches exact "
              f"owner argument; {EXPECTED_ROWS} of {EXPECTED_ROWS} rows hash the tree")
        return 0
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()}")
        return 1
    try:
        validate(root, act, argument, applied=False)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED (before applying anything): {exc}")
        return 1
    code = act.module.apply(True)
    if code != 0:
        print(f"FAILED: builder --apply --at-adoption returned {code}; nothing recorded")
        return 1
    try:
        outputs = expected_outputs(root, act, argument, date, applied=True)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED after apply: {exc}\n  the tree now carries the applied "
              "patches and no record; restore it with git checkout before retrying")
        return 1
    for rel, content in outputs.items():
        (root / rel).write_text(content)
        print(f"wrote {rel.as_posix()}")
    print(registration_notes(act, argument, date))
    return 0


def selftest() -> int:
    results = []
    for act in ACTS.values():
        exact = digest((ROOT / act.manifest).read_bytes())
        packet_bytes = (ROOT / act.packet).read_bytes()
        review = (ROOT / act.confirmation_review).read_text()

        def rejects(fn, needle, *args, **kwargs):
            try:
                fn(*args, **kwargs)
            except ValueError as exc:
                return needle in str(exc)
            return False

        results.append((f"{act.act_type}: wrong owner argument rejected",
                        rejects(validate_subject, "does not match manifest",
                                ROOT, act, "0" * 64, False)))
        pre = False
        try:
            pre = len(validate_subject(ROOT, act, exact, False)) == EXPECTED_ROWS
        except ValueError as exc:
            print(f"  ({act.act_type} exact-argument failure: {exc})")
        results.append((f"{act.act_type}: exact argument validates before adoption", pre))
        results.append((f"{act.act_type}: unapplied tree rejected in applied mode",
                        rejects(validate_subject, "does not hash the tree",
                                ROOT, act, exact, True)))
        mutated_manifest = (ROOT / act.manifest).read_bytes().replace(b"\n", b"\n", 1) + b"#\n"
        results.append((f"{act.act_type}: manifest bytes the frozen subject lacks rejected",
                        rejects(validate_subject, "frozen subject does not carry",
                                ROOT, act, digest(mutated_manifest), False,
                                manifest_override=mutated_manifest)))
        staged = False
        try:
            staged = bool(validate_packet(ROOT, act, exact))
        except ValueError as exc:
            print(f"  ({act.act_type} packet-stage failure: {exc})")
        results.append((f"{act.act_type}: packet and confirmation review bind the argument", staged))
        phrase = phrase_for(act, exact).encode()
        doubled = packet_bytes.replace(phrase, phrase + b"\n" + phrase, 1)
        results.append((f"{act.act_type}: packet carrying two phrase copies rejected",
                        rejects(validate_packet, "exactly one exact phrase",
                                ROOT, act, exact, packet_override=doubled)))
        drifted = packet_bytes + b"\n"
        results.append((f"{act.act_type}: packet bytes the packet head lacks rejected",
                        rejects(validate_packet, "packet-head commit does not carry",
                                ROOT, act, exact, packet_override=drifted)))
        unbound = review.replace(f"Manifest SHA-256: {exact}", "Manifest SHA-256: " + "0" * 64, 1)
        results.append((f"{act.act_type}: review not binding the manifest rejected",
                        rejects(validate_packet, "does not bind the offered manifest",
                                ROOT, act, exact, review_override=unbound)))
        wrong_verdict = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS", 1)
        results.append((f"{act.act_type}: review verdict other than CONFIRM rejected",
                        rejects(validate_packet, "exact verdict CONFIRM",
                                ROOT, act, exact, review_override=wrong_verdict)))
        buried = "\n".join(["# heading", "", ""] + review.splitlines())
        results.append((f"{act.act_type}: review markers outside the four-line head rejected",
                        rejects(validate_packet, "does not bind the offered manifest",
                                ROOT, act, exact, review_override=buried)))
    failing = 0
    for name, passed in results:
        failing += 0 if passed else 1
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"{len(results)} recording fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--record", nargs=2, metavar=("ACT_TYPE", "MANIFEST_SHA"))
    parser.add_argument("--check", nargs=2, metavar=("ACT_TYPE", "MANIFEST_SHA"))
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
