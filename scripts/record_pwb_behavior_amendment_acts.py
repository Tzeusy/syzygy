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

Confirmation-review head contract. `validate_packet` reads only the first
four lines of the confirmation review (blank lines count as lines; nothing
below line 4 is read) and accepts exactly one of two cases, per
`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
§1 ("When a confirmation review clears a package's bytes"):

- **Case (a) — CONFIRM.** The head carries an exact line `Verdict: CONFIRM`,
  an exact line `Manifest SHA-256: <the offered argument>`, and a line
  matching `Reviewed commit: <40-hex sha>`. Unchanged from before this
  decision; a CONFIRM-only act's rendered bytes are byte-identical to what
  this script rendered before this change (see `--selftest`).
- **Case (b) — CONFIRM WITH EXCEPTIONS, notes only.** The head carries an
  exact line `Verdict: CONFIRM WITH EXCEPTIONS`, the same
  `Manifest SHA-256:` and `Reviewed commit:` lines as case (a), AND the
  `Act` entry names a `disposition_record` path, AND that disposition
  record (read directly from the tree; never git-blob-pinned) satisfies
  every one of:
    - it exists;
    - it carries an exact line `Reviewed record: <the raw's repo path,
      exactly as `act.confirmation_review` names it>`;
    - it carries an exact line `Manifest SHA-256: <the offered argument>`;
    - it carries an exact line `Revise-severity findings: 0` (any other
      digit, or the line's absence, refuses — this is the only accepted
      zero-count line form);
    - it dispositions every numbered finding of the raw: read each text's
      own line-leading markers `^(\d+)\.\s` (MULTILINE); the raw's finding
      count N is the longest unbroken run 1..N starting at 1 (0 if line
      `1.` never opens a line); the disposition's own line-leading markers
      must equal the exact set `{1, ..., N}` — not a superset or a subset.
  Any other combination (a REVISE-style verdict, a missing or malformed
  disposition, a digest mismatch, a nonzero revise count, an unmatched
  finding, or case (b) with no `disposition_record` configured on the Act)
  refuses with a specific error. No `ACTS` entry currently names a
  `disposition_record`; wiring one is a later, separately reviewed change.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$", re.MULTILINE)
FINDING_MARK_RE = re.compile(r"^(\d+)\.\s", re.MULTILINE)
CONFIRM_LINE = "Verdict: CONFIRM"
EXCEPTIONS_LINE = "Verdict: CONFIRM WITH EXCEPTIONS"
EXPECTED_ROWS = 11


def _numbered_markers(text: str) -> set[int]:
    """The set of numbers that open a line as `<n>. ` (MULTILINE)."""
    return {int(n) for n in FINDING_MARK_RE.findall(text)}


def _raw_finding_count(text: str) -> int:
    """The longest unbroken run 1..N of `_numbered_markers`, starting at 1;
    0 if a line `1. ` never opens a line."""
    seen = _numbered_markers(text)
    n = 0
    while (n + 1) in seen:
        n += 1
    return n


class Act:
    def __init__(self, act_type, builder, label, record_name, identity, title,
                 frozen_subject, packet_head, confirmation_review, tag_stem,
                 effect, not_authorized, disposition_record=None):
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
        # Case (b) only (POLARIS-GATE-SITTING-2026-09-26-DECISION.md §1): the
        # disposition record a CONFIRM WITH EXCEPTIONS verdict is bound to.
        # None means this Act accepts only case (a), CONFIRM.
        self.disposition_record = (
            pathlib.Path(disposition_record) if disposition_record is not None else None
        )
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


def validate_disposition(
    root: pathlib.Path, act: Act, argument: str, review: str,
    disposition_override: bytes | None = None,
) -> pathlib.Path:
    """Stage 2b (case (b) only) — a notes-only CONFIRM WITH EXCEPTIONS verdict
    is bound to a disposition record beside the package
    (POLARIS-GATE-SITTING-2026-09-26-DECISION.md §1), never by editing the
    reviewed bytes. See the module docstring for the exact predicate. Returns
    the disposition record's path, relative to `root`.
    """
    if act.disposition_record is None:
        raise ValueError(
            "confirmation review head carries CONFIRM WITH EXCEPTIONS but this "
            "act names no disposition record"
        )
    disposition_path = root / act.disposition_record
    if disposition_override is None and not disposition_path.is_file():
        raise ValueError(
            f"missing disposition record: {act.disposition_record.as_posix()}"
        )
    text = (disposition_override.decode() if disposition_override is not None
            else disposition_path.read_text())
    lines = text.splitlines()
    if f"Reviewed record: {act.confirmation_review.as_posix()}" not in lines:
        raise ValueError("disposition record does not name the reviewed raw's exact path")
    if f"Manifest SHA-256: {argument}" not in lines:
        raise ValueError("disposition record does not bind the offered manifest digest")
    if "Revise-severity findings: 0" not in lines:
        raise ValueError("disposition record does not state zero revise-severity findings")
    expected = set(range(1, _raw_finding_count(review) + 1))
    actual = _numbered_markers(text)
    if actual != expected:
        raise ValueError(
            f"disposition record findings {sorted(actual)} do not match the "
            f"raw's numbered findings {sorted(expected)}"
        )
    return act.disposition_record


def validate_packet(
    root: pathlib.Path, act: Act, argument: str,
    packet_override: bytes | None = None, review_override: str | None = None,
    disposition_override: bytes | None = None,
) -> tuple[str, str, pathlib.Path | None]:
    """Stage 2 — the owner was shown this phrase, and a review confirmed these bytes.

    Accepts exactly the two head cases the module docstring states. Returns
    `(reviewed_commit, verdict, disposition_record_or_None)`; the reviewed
    commit is provenance, not binding, and `disposition_record` is set only
    for a case-(b) verdict.
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
    if CONFIRM_LINE in head:
        verdict = "CONFIRM"
    elif EXCEPTIONS_LINE in head:
        verdict = "CONFIRM WITH EXCEPTIONS"
    else:
        raise ValueError(
            "confirmation review head does not carry an accepted exact verdict "
            "line (Verdict: CONFIRM or Verdict: CONFIRM WITH EXCEPTIONS)"
        )
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    disposition_record = None
    if verdict == "CONFIRM WITH EXCEPTIONS":
        disposition_record = validate_disposition(
            root, act, argument, review, disposition_override=disposition_override,
        )
    return reviewed.group(1), verdict, disposition_record


def validate(root: pathlib.Path, act: Act, argument: str, applied: bool):
    rows = validate_subject(root, act, argument, applied)
    reviewed, verdict, disposition_record = validate_packet(root, act, argument)
    return rows, reviewed, verdict, disposition_record


def tag_for(act: Act, date: str) -> str:
    return f"{act.tag_stem}-signed-{date}"


def render_act(act: Act, argument: str, date: str, rows, reviewed: str,
               verdict: str = "CONFIRM",
               disposition_rel: pathlib.Path | None = None) -> str:
    artifact_table = "\n".join(f"| `{path}` | `{sha}` |" for sha, path in rows)
    if disposition_rel is None:
        review_bullet = (
            f"- confirmation review: `{act.confirmation_review.as_posix()}`, verdict\n"
            f"  `{verdict}`, bound to this manifest digest; the raw names reviewed commit\n"
            f"  `{reviewed}` [Observed — the raw's own line; binding is by digest]; and"
        )
    else:
        review_bullet = (
            f"- confirmation review: `{act.confirmation_review.as_posix()}`, verdict\n"
            f"  `{verdict}`, bound to this manifest digest; the raw names reviewed commit\n"
            f"  `{reviewed}` [Observed — the raw's own line; binding is by digest];\n"
            f"- disposition record: `{disposition_rel.as_posix()}`, dispositioning\n"
            f"  the review's notes under the `{verdict}` verdict, never by editing\n"
            f"  the reviewed bytes; and"
        )
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
{review_bullet}
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


def render_aggregate_block(act: Act, argument: str, date: str,
                           verdict: str = "CONFIRM",
                           disposition_rel: pathlib.Path | None = None) -> str:
    review_row = f"`{act.confirmation_review.as_posix()}`: `{verdict}`, bound to this manifest digest"
    if disposition_rel is not None:
        review_row += f"; disposition: `{disposition_rel.as_posix()}`"
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
| Review outcome | {review_row} |
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
    rows, reviewed, verdict, disposition_record = validate(root, act, argument, applied)
    aggregate = (root / AGGREGATE_REL).read_text()
    heading = aggregate_heading(act, date)
    occurrences = aggregate.count(heading)
    if occurrences > 1:
        raise ValueError("aggregate record contains duplicate sections for this act")
    prefix = aggregate.split(heading, 1)[0].rstrip() if occurrences else aggregate.rstrip()
    return {
        act.record: render_act(act, argument, date, rows, reviewed, verdict, disposition_record),
        AGGREGATE_REL: prefix + "\n\n" + render_aggregate_block(
            act, argument, date, verdict, disposition_record),
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
        _, _, verdict, disposition_record = validate(root, act, argument, applied=True)
        aggregate = (root / AGGREGATE_REL).read_text()
        if aggregate.count(render_aggregate_block(
                act, argument, date, verdict, disposition_record)) != 1:
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


class _FixtureAct:
    """A minimal stand-in exposing only what `validate_packet` reads. Used
    solely to exercise the case-(b) disposition predicate without adding a
    `disposition_record` to any real `ACTS` entry (POLARIS-GATE-SITTING-
    2026-09-26-DECISION.md §1: "wiring a real package is a later step")."""

    def __init__(self, label, packet, packet_head, confirmation_review,
                 disposition_record=None):
        self.label = label
        self.packet = packet
        self.packet_head = packet_head
        self.confirmation_review = confirmation_review
        self.disposition_record = disposition_record


def selftest_disposition() -> list[tuple[str, bool]]:
    """Case (b) mutation fixtures, built entirely under a temp directory
    (never the tracked tree). Exercises every refusal condition the module
    docstring's case (b) lists, plus one positive fixture."""
    results = []

    def rejects(fn, needle, *args, **kwargs):
        try:
            fn(*args, **kwargs)
        except ValueError as exc:
            return needle in str(exc)
        return False

    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        rel_packet = pathlib.Path("PACKET.md")
        rel_review = pathlib.Path("REVIEW-RAW.md")
        rel_disposition = pathlib.Path("DISPOSITION.md")
        argument = "c" * 64

        act = _FixtureAct("FIXTURE CASE-B LABEL", rel_packet, "0" * 40, rel_review)

        (root / rel_packet).write_text(f"# Packet\n\n{phrase_for(act, argument)}\n")
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "fixture@example.invalid"],
                       cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Fixture"], cwd=root, check=True)
        subprocess.run(["git", "add", rel_packet.as_posix()], cwd=root, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "fixture packet"], cwd=root, check=True)
        act.packet_head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=True,
        ).stdout.strip()

        review_text = (
            "# Review — fixture (round 1, confirmation)\n"
            f"Reviewed commit: {'b' * 40}\n"
            f"Manifest SHA-256: {argument}\n"
            "Verdict: CONFIRM WITH EXCEPTIONS\n"
            "\n"
            "## Findings\n"
            "\n"
            "1. First finding, notes only.\n"
            "2. Second finding, notes only.\n"
        )

        good_disposition = (
            "# Disposition — fixture\n"
            f"Reviewed record: {rel_review.as_posix()}\n"
            f"Manifest SHA-256: {argument}\n"
            "Revise-severity findings: 0\n"
            "\n"
            "1. Accepted as noted; no repair needed.\n"
            "2. Owner already ruled on this; dispositioned by that ruling.\n"
        )

        results.append((
            "case-b: no disposition_record configured on the Act rejected",
            rejects(validate_packet, "names no disposition record",
                    root, act, argument, review_override=review_text,
                    disposition_override=good_disposition.encode())))

        act.disposition_record = rel_disposition

        try:
            reviewed, verdict, disposition = validate_packet(
                root, act, argument, review_override=review_text,
                disposition_override=good_disposition.encode())
            positive_ok = (verdict == "CONFIRM WITH EXCEPTIONS"
                          and disposition == rel_disposition
                          and reviewed == "b" * 40)
        except ValueError as exc:
            positive_ok = False
            print(f"  (case-b positive fixture failure: {exc})")
        results.append((
            "case-b: valid CONFIRM WITH EXCEPTIONS with matching disposition accepted",
            positive_ok))

        results.append((
            "case-b: missing disposition record file rejected",
            rejects(validate_packet, "missing disposition record",
                    root, act, argument, review_override=review_text)))

        bad_path = good_disposition.replace(
            f"Reviewed record: {rel_review.as_posix()}",
            "Reviewed record: some/other/RAW.md", 1)
        results.append((
            "case-b: disposition naming the wrong raw path rejected",
            rejects(validate_packet, "does not name the reviewed raw's exact path",
                    root, act, argument, review_override=review_text,
                    disposition_override=bad_path.encode())))

        bad_digest = good_disposition.replace(
            f"Manifest SHA-256: {argument}", "Manifest SHA-256: " + "d" * 64, 1)
        results.append((
            "case-b: disposition digest mismatch rejected",
            rejects(validate_packet, "does not bind the offered manifest digest",
                    root, act, argument, review_override=review_text,
                    disposition_override=bad_digest.encode())))

        nonzero_revise = good_disposition.replace(
            "Revise-severity findings: 0", "Revise-severity findings: 1", 1)
        results.append((
            "case-b: nonzero revise-severity count rejected",
            rejects(validate_packet, "does not state zero revise-severity findings",
                    root, act, argument, review_override=review_text,
                    disposition_override=nonzero_revise.encode())))

        missing_finding = good_disposition.replace(
            "2. Owner already ruled on this; dispositioned by that ruling.\n", "")
        results.append((
            "case-b: disposition missing one of the raw's numbered findings rejected",
            rejects(validate_packet, "do not match the raw's numbered findings",
                    root, act, argument, review_override=review_text,
                    disposition_override=missing_finding.encode())))

        extra_finding = good_disposition + "3. An extra disposition the raw never raised.\n"
        results.append((
            "case-b: disposition naming an extra finding beyond the raw's rejected",
            rejects(validate_packet, "do not match the raw's numbered findings",
                    root, act, argument, review_override=review_text,
                    disposition_override=extra_finding.encode())))

        revise_review = review_text.replace(
            "Verdict: CONFIRM WITH EXCEPTIONS", "Verdict: REVISE", 1)
        results.append((
            "case-b: REVISE verdict rejected outright even with a valid disposition present",
            rejects(validate_packet, "does not carry an accepted exact verdict line",
                    root, act, argument, review_override=revise_review,
                    disposition_override=good_disposition.encode())))

    return results


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
            reviewed_commit, staged_verdict, staged_disposition = validate_packet(ROOT, act, exact)
            staged = bool(reviewed_commit) and staged_verdict == "CONFIRM" and staged_disposition is None
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
        exceptions_verdict = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS", 1)
        results.append((
            f"{act.act_type}: CONFIRM WITH EXCEPTIONS rejected when this act "
            "names no disposition record",
            rejects(validate_packet, "names no disposition record",
                    ROOT, act, exact, review_override=exceptions_verdict)))
        revise_verdict = review.replace("Verdict: CONFIRM", "Verdict: REVISE", 1)
        results.append((f"{act.act_type}: REVISE verdict rejected outright",
                        rejects(validate_packet, "does not carry an accepted exact verdict line",
                                ROOT, act, exact, review_override=revise_verdict)))
        buried = "\n".join(["# heading", "", ""] + review.splitlines())
        results.append((f"{act.act_type}: review markers outside the four-line head rejected",
                        rejects(validate_packet, "does not bind the offered manifest",
                                ROOT, act, exact, review_override=buried)))
        rows_pre, reviewed_pre, verdict_pre, disposition_pre = validate(ROOT, act, exact, False)
        rendered_act = render_act(act, exact, "2026-09-26", rows_pre, reviewed_pre,
                                  verdict_pre, disposition_pre)
        rendered_aggregate = render_aggregate_block(act, exact, "2026-09-26",
                                                     verdict_pre, disposition_pre)
        results.append((
            f"{act.act_type}: CONFIRM-only render_act byte-identical to the "
            "pre-case-(b) baseline",
            digest(rendered_act.encode())
            == "4dcbd3c2a74a2cfffa0bc1fb4832419906380a4dc2a267f64066f86cb60248ee",
        ))
        results.append((
            f"{act.act_type}: CONFIRM-only render_aggregate_block byte-identical "
            "to the pre-case-(b) baseline",
            digest(rendered_aggregate.encode())
            == "7967bf357378235ee4da53e68bb47f8a48f7fc984be90dd3bc029a2e5bb71241",
        ))
    results.extend(selftest_disposition())
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
