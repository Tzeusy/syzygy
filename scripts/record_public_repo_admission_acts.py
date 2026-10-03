#!/usr/bin/env python3
"""Record or verify the owner's public-repository admission acts.

Package `contracts/candidates/public-repo-admission/`. Each act is a separate
state-(1) owner act over one record named by a row of
`PUBLIC-REPO-ADMISSION-MANIFEST.txt`: an observation consent per
`(project:syzygy, repository)` pair, and the one egress consent for
`(project:syzygy, provider:anthropic)`. The owner gives each by selecting an
option in a structured question that names the records "at the manifest rows"
(packet Q5; the 2026-10-02 policy re-pin is the precedent). No phrase is typed
and no digest appears in any Markdown file of the package. This script
performs nothing by itself, and it refuses to record anything until the
package has a confirming review: `FROZEN_SUBJECT` is None until then.

`--record KEY ARGUMENT --date D --question-opening Q --selection-label L
--selection-description S` requires, before anything is written:

1. the argument is a 64-hex SHA-256 equal to this record's manifest row, the
   manifest rows are exactly the builder's instance records, and the builder
   verifies (so another record's row, a stale record or an orphan is refused);
2. the record on disk hashes to the argument;
3. the frozen commit carries the manifest, the packet, the review brief and
   every instance record exactly as presented (the packet may gain one
   PERFORMED head), and the packet carries no 64-hex token;
4. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
   FILE>` and a verdict of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter
   clears the bytes only when every finding is a `note` and the sibling
   `ROUND-<n>-DISPOSITIONS.md` names the raw and dispositions every finding;
5. the owner's selection (opening, label, description) is non-empty, one line
   each, and carries no 64-hex digest.

It then writes the dedicated record and one `ACCEPTANCE-ACT-RECORD.md`
section. `--check` re-derives both and counts exactly one copy of the block.
`--selftest` mutates each predicate and requires it to fail closed.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_repo_admission as build  # noqa: E402
import record_versioned_signoff as vs  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
PKG = build.PKG
MANIFEST_REL = PKG / build.MANIFEST_NAME
PACKET_REL = PKG / "OWNER-DECISION-PACKET.md"
BRIEF_REL = PKG / "REVIEW-BRIEF.md"
CONFIRMATION_REVIEW_REL = pathlib.Path("docs/reviews/R-PUBLIC-ADMISSION-5-RAW.md")
DISPOSITION_REL = PKG / "ROUND-5-DISPOSITIONS.md"
ANSWERS_REL = DECISIONS / "PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md"
#: The commit the confirming review read. None until a round returns CONFIRM
#: or notes-only CONFIRM WITH EXCEPTIONS; then set to that commit and the
#: round's two paths above, never hand-edited again. While None, every
#: `--record` is refused: an unreviewed package cannot be recorded.
FROZEN_SUBJECT: str | None = None
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
ROW_RE = re.compile(r"^([0-9a-f]{64})  (\S+)$", re.MULTILINE)
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$", re.MULTILINE)
VERDICT_RE = re.compile(r"^Verdict: (.+?)\s*$")
PERFORMED_HEAD_RE = re.compile(
    rb"\A(# [^\n]+\n\n)"
    rb"> \*\*PERFORMED \d{4}-\d{2}-\d{2}\.\*\*[^\n]*\n(?:> [^\n]*\n)*\n"
)


@dataclass(frozen=True)
class Act:
    key: str
    label: str
    act_type: str
    identity_stem: str
    stem: str
    subject: pathlib.Path
    title: str
    effect: str

    @property
    def record(self) -> pathlib.Path:
        return DECISIONS / f"PUBLIC-REPO-ADMISSION-{self.stem}-ACT.md"


ACTS = (
    Act("requests-observation", "CONSENT TO PUBLIC OBSERVATION OF PSF-REQUESTS",
        "consent-observation", "PUBLIC-OBS-REQUESTS", "REQUESTS-OBSERVATION",
        PKG / "instances/requests/OBSERVATION-CONSENT.md",
        "psf/requests public-repository observation consent",
        "The record is the owner's effective observation consent for the pair "
        "(`project:syzygy`, `repository:psf-requests`) at the admitted "
        "revisions it lists: read-only reads of those commits' Git objects, "
        "fetched one commit at a time, with no execution, no write and no "
        "egress."),
    Act("redis-observation", "CONSENT TO PUBLIC OBSERVATION OF REDIS-REDIS",
        "consent-observation", "PUBLIC-OBS-REDIS", "REDIS-OBSERVATION",
        PKG / "instances/redis/OBSERVATION-CONSENT.md",
        "redis/redis public-repository observation consent",
        "The record is the owner's effective observation consent for the pair "
        "(`project:syzygy`, `repository:redis-redis`) at the four admitted "
        "revisions it lists: read-only reads of those commits' Git objects, "
        "fetched one commit at a time, with no execution, no write and no "
        "egress."),
    Act("egress-anthropic", "CONSENT TO PUBLIC TARGET EGRESS TO ANTHROPIC",
        "consent-egress", "PUBLIC-EGRESS-ANTHROPIC", "EGRESS-ANTHROPIC",
        PKG / "instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md",
        "public-target egress consent to Anthropic",
        "The record is the owner's effective egress consent for the pair "
        "(`project:syzygy`, `provider:anthropic`), through the Claude Agent "
        "SDK runtime, for content read under an in-force observation consent "
        "for a repository the record lists, in the content classes it lists, "
        "under its retention and route conditions."),
)
ACT_BY_KEY = {act.key: act for act in ACTS}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def phrase_for(act: Act, argument: str) -> str:
    return f"{act.label}: {argument}"


def tag_for(act: Act, date: str) -> str:
    return f"public-admission-{act.key}-signed-{date}"


def identity_for(act: Act, date: str) -> str:
    return f"{act.identity_stem}-{date}"


def git_blob(root: pathlib.Path, commit: str, rel: pathlib.Path) -> bytes:
    done = subprocess.run(["git", "-C", str(root), "show", f"{commit}:{rel.as_posix()}"],
                          capture_output=True)
    if done.returncode != 0:
        raise ValueError(f"cannot read {rel.as_posix()} at {commit}: "
                         f"{done.stderr.decode().strip() or 'git show failed'}")
    return done.stdout


@dataclass
class Inputs:
    """Everything validation reads, injectable for the selftest."""
    manifest: bytes
    subject: bytes
    packet: bytes
    review: str
    produced_paths: list[str]
    stale: list[str]
    frozen: str | None
    frozen_blob: Callable[[pathlib.Path], bytes]
    frozen_files: dict[pathlib.Path, bytes]
    disposition_check: Callable[[dict[int, str]], None]


def live_inputs(root: pathlib.Path) -> Inputs:
    subject_dirs = list((root / PKG / "instances").glob("*/params.json"))
    del subject_dirs
    produced = [path.as_posix() for path, _t in build.instances(root / PKG)]
    stale = [str(p) for p in build.stale(root / PKG)]
    files = {rel: (root / rel).read_bytes() for rel in
             [MANIFEST_REL, PACKET_REL, BRIEF_REL] + [pathlib.Path(p) for p in produced]
             if (root / rel).is_file()}
    review_path = root / CONFIRMATION_REVIEW_REL
    return Inputs(
        manifest=(root / MANIFEST_REL).read_bytes() if (root / MANIFEST_REL).is_file() else b"",
        subject=b"",
        packet=(root / PACKET_REL).read_bytes() if (root / PACKET_REL).is_file() else b"",
        review=review_path.read_text() if review_path.is_file() else "",
        produced_paths=produced, stale=stale, frozen=FROZEN_SUBJECT,
        frozen_blob=lambda rel: git_blob(root, FROZEN_SUBJECT or "", rel),
        frozen_files=files,
        disposition_check=lambda findings: vs.validate_disposition(
            root, CONFIRMATION_REVIEW_REL.as_posix(), DISPOSITION_REL.as_posix(), findings),
    )


def validate(act: Act, argument: str, inp: Inputs) -> tuple[str, str, str]:
    """Return (manifest file sha, reviewed commit, verdict) or raise ValueError."""
    if inp.frozen is None:
        raise ValueError("no confirming review is recorded: FROZEN_SUBJECT is unset, "
                         "so nothing may be recorded")
    if not SHA_RE.fullmatch(argument):
        raise ValueError("owner argument is not a 64-hex SHA-256")
    rows = ROW_RE.findall(inp.manifest.decode())
    paths = [path for _sha, path in rows]
    if paths != sorted(inp.produced_paths):
        raise ValueError("manifest row population differs from the builder's instance records")
    row = next((sha for sha, path in rows if path == act.subject.as_posix()), None)
    if row is None:
        raise ValueError(f"manifest has no row for {act.subject.as_posix()}")
    if row != argument:
        raise ValueError(f"owner argument {argument} is not the {act.key} manifest row {row}")
    if inp.stale:
        raise ValueError("builder reports stale instances or manifest: " + ", ".join(inp.stale))
    if digest(inp.subject) != argument:
        raise ValueError(f"{act.key} record hashes to {digest(inp.subject)}, not the owner argument")
    for rel, current in inp.frozen_files.items():
        expected = current if rel != PACKET_REL else PERFORMED_HEAD_RE.sub(rb"\1", current, count=1)
        if inp.frozen_blob(rel) != expected:
            raise ValueError(f"frozen subject does not carry the presented bytes of {rel.as_posix()}")
    if HEX64_RE.search(inp.packet.decode()):
        raise ValueError("owner packet carries a 64-hex token; arguments come only "
                         "from the manifest rows")
    manifest_sha = digest(inp.manifest)
    head = [line for line in inp.review.splitlines() if line.strip()][:4]
    if f"Manifest SHA-256: {manifest_sha}" not in head:
        raise ValueError("confirmation review head does not bind the manifest file's SHA-256")
    verdicts = [m.group(1) for line in head if (m := VERDICT_RE.match(line))]
    if len(verdicts) != 1 or verdicts[0] not in VERDICTS:
        raise ValueError("confirmation review head does not carry the verdict CONFIRM "
                         "or CONFIRM WITH EXCEPTIONS")
    reviewed = REVIEWED_COMMIT_RE.search("\n".join(head))
    if not reviewed:
        raise ValueError("confirmation review head does not name its reviewed commit")
    if verdicts[0] == "CONFIRM WITH EXCEPTIONS":
        findings = vs.review_findings(inp.review)
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; only a "
                             "notes-only round clears the bytes")
        inp.disposition_check(findings)
    return manifest_sha, reviewed.group(1), verdicts[0]


@dataclass(frozen=True)
class Selection:
    opening: str
    label: str
    description: str

    def validate(self) -> None:
        for name, value in (("opening", self.opening), ("label", self.label),
                            ("description", self.description)):
            if not value.strip() or "\n" in value:
                raise ValueError(f"owner selection {name} must be one non-empty line")
            if HEX64_RE.search(value):
                raise ValueError(f"owner selection {name} carries a 64-hex digest")


def render_act(act: Act, argument: str, date: str, manifest_sha: str, reviewed: str,
               verdict: str, sel: Selection, frozen: str) -> str:
    return f"""# Owner act — {act.title}

Date: {date}

Owner: Tzeusy

Act identity: `{identity_for(act, date)}`

Act type: `{act.act_type}`

Project identity: `project:syzygy`

Artifact identity: `{act.subject.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
explicitly selected by the owner's option selection recorded below

Supersession / revocation: none recorded by this act; an earlier version of
the same record, if one was performed, is superseded only by a later act that
names it. This act is revoked only by a later exact owner act naming it.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner was presented the confirmed packet at
`{PACKET_REL.as_posix()}`, which by design carries no digest. The act takes
this phrase, whose argument is this record's row of the package manifest:

```text
{phrase_for(act, argument)}
```

The owner did not type the phrase. On {date} the owner answered a structured
question in the Claude Code CLI that opened "{sel.opening}" by selecting the
option below; the selection is the instruction, and it names the records "at
the manifest rows". The label and description, verbatim:

| Label | Description |
|---|---|
| "{sel.label}" | "{sel.description}" |

The argument was read from this record's row of
`{MANIFEST_REL.as_posix()}` at the frozen commit and matched the record on
disk at recording. A swapped argument would have been refused: the recorder
rejects an argument that is not this record's row.

Frozen provenance:

- frozen subject (package bytes): `{frozen}`;
- manifest SHA-256: `{manifest_sha}`;
- confirmation review: `{CONFIRMATION_REVIEW_REL.as_posix()}`, verdict
  `{verdict}`, its head bound to the manifest file's SHA-256 above; notes, if
  any, are dispositioned in `{DISPOSITION_REL.as_posix()}`; the raw names
  reviewed commit `{reviewed}` [Observed — the raw's own line; binding is by
  digest]; and
- recording tag: `{tag_for(act, date)}`, on the commit carrying this act record.

## Effect

{act.effect}

## What this act does not authorize

This act satisfies only its own authority; the package's other records each
take their own act and none implies another (REQ-polaris-generation-025). It
adopts no registry entry or screening policy, amends no contract, and grants
no read, egress, write, execution, deployment, release, autonomous or
multi-user authority beyond what its Effect states. Observation consent
permits no egress, and egress consent permits no read. It proves no read,
screening, generation or answer result.
"""


def aggregate_heading(act: Act, date: str) -> str:
    return f"## Public-repository admission act — {act.act_type} — {act.key} — performed {date}"


def render_aggregate_block(act: Act, argument: str, date: str, manifest_sha: str,
                           verdict: str, frozen: str) -> str:
    return f"""{aggregate_heading(act, date)}

**Phrase the act takes (given {date} by option selection, not typed; see the
dedicated record):**

```text
{phrase_for(act, argument)}
```

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Act type / artifact | `{act.act_type}` / `{act.subject.as_posix()}` |
| Argument | SHA-256 of the artifact itself: its row of the package manifest, recomputed at recording |
| Provenance state | `owner-adopted (bootstrap, uncorrelated)` — a state-(1) human act, owner-trusted and never independently verified |
| A1 audit-record identity | explicitly absent, satisfying RFC3-16(b) item 9 for state (1) |
| Frozen subject | `{frozen}` |
| Manifest | `{MANIFEST_REL.as_posix()}`, SHA-256 `{manifest_sha}` |
| Review outcome | `{CONFIRMATION_REVIEW_REL.as_posix()}`: `{verdict}`, its head bound to the manifest file |
| Recording | `{act.record.as_posix()}`; annotated tag `{tag_for(act, date)}` on the commit carrying these records |

Effective status: this one record is **effective owner authority —
owner-adopted (bootstrap, uncorrelated)** for its own role only. The package's
other records remain separate acts.
"""


def expected(act: Act, argument: str, date: str, sel: Selection, inp: Inputs):
    sel.validate()
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    manifest_sha, reviewed, verdict = validate(act, argument, inp)
    frozen = inp.frozen or ""
    return (render_act(act, argument, date, manifest_sha, reviewed, verdict, sel, frozen),
            render_aggregate_block(act, argument, date, manifest_sha, verdict, frozen))


def with_subject(inp: Inputs, root: pathlib.Path, act: Act) -> Inputs:
    path = root / act.subject
    inp.subject = path.read_bytes() if path.is_file() else b""
    return inp


def do_record(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection) -> int:
    if (root / act.record).exists():
        print(f"FAILED: dedicated act already exists: {act.record.as_posix()}")
        return 1
    try:
        record, block = expected(act, argument, date, sel, with_subject(live_inputs(root), root, act))
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"FAILED (nothing written): {exc}")
        return 1
    aggregate = (root / AGGREGATE_REL).read_text()
    if aggregate_heading(act, date) in aggregate:
        print("FAILED: aggregate record already carries this act's heading")
        return 1
    (root / act.record).write_text(record)
    (root / AGGREGATE_REL).write_text(aggregate.rstrip() + "\n\n" + block)
    print(f"wrote {act.record.as_posix()}\nappended one section to {AGGREGATE_REL.as_posix()}")
    print(f"next, in the same change: tag {tag_for(act, date)} on the commit carrying them; "
          "scripts/check_governance.py: add the chain link and the performed-act "
          "registration for this label (the candidate registration stays until then)")
    return 0


def do_check(root: pathlib.Path, act: Act, argument: str, date: str, sel: Selection) -> int:
    try:
        record, block = expected(act, argument, date, sel, with_subject(live_inputs(root), root, act))
    except (ValueError, subprocess.CalledProcessError) as exc:
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
    print(f"recorded {act.key} act matches the exact owner argument")
    return 0


def selftest() -> int:
    """One mutant per predicate; each must be refused for the stated reason."""
    manifest_files = {a.subject.as_posix(): f"record {a.key}\n".encode() for a in ACTS}
    pkt = b"# Packet\n\n> Candidate - binds nothing.\n\nbody\n"
    rows = sorted((p, digest(b)) for p, b in manifest_files.items())
    manifest = ("# header\n" + "".join(f"{s}  {p}\n" for p, s in rows)).encode()
    msha = digest(manifest)
    review = (f"# R5\nReviewed commit: {'a' * 40}\nManifest SHA-256: {msha}\n"
              "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
    blobs = {MANIFEST_REL: manifest, PACKET_REL: pkt, BRIEF_REL: b"brief",
             **{pathlib.Path(p): b for p, b in manifest_files.items()}}

    def make(**over) -> Inputs:
        base = dict(manifest=manifest, subject=b"", packet=pkt, review=review,
                    produced_paths=[p for p, _ in rows], stale=[], frozen="f" * 40,
                    frozen_blob=lambda rel: blobs[rel], frozen_files=dict(blobs),
                    disposition_check=lambda findings: None)
        base.update(over)
        return Inputs(**base)

    results: list[tuple[str, bool]] = []

    def refused(needle, act, argument, inp) -> bool:
        try:
            validate(act, argument, inp)
        except ValueError as exc:
            return needle in str(exc)
        return False

    act = ACTS[0]
    other = ACTS[1]
    good = dict(zip([p for p, _ in rows], [s for _, s in rows]))
    arg = good[act.subject.as_posix()]
    subj = manifest_files[act.subject.as_posix()]
    try:
        ok = validate(act, arg, make(subject=subj))[2] == "CONFIRM"
    except ValueError as exc:
        print(f"  (exact-argument failure: {exc})")
        ok = False
    results.append(("exact argument validates", ok))
    results.append(("unset FROZEN_SUBJECT refused",
                    refused("FROZEN_SUBJECT is unset", act, arg, make(subject=subj, frozen=None))))
    results.append(("non-hex argument refused",
                    refused("not a 64-hex", act, "xyz", make(subject=subj))))
    results.append(("wrong argument refused",
                    refused("manifest row", act, "0" * 64, make(subject=subj))))
    results.append(("another record's row refused",
                    refused("manifest row", act, good[other.subject.as_posix()], make(subject=subj))))
    results.append(("manifest rows out of population refused",
                    refused("row population", act, arg, make(subject=subj, produced_paths=["x"]))))
    results.append(("stale builder output refused",
                    refused("stale", act, arg, make(subject=subj, stale=["x"]))))
    results.append(("record not hashing to the argument refused",
                    refused("hashes to", act, arg, make(subject=subj + b"x"))))
    drift = dict(blobs)
    drift[PACKET_REL] = pkt + b"x"
    results.append(("frozen commit lacking the presented packet refused",
                    refused("frozen subject does not carry", act, arg,
                            make(subject=subj, frozen_blob=lambda rel: drift[rel]))))
    performed = pkt.replace(b"\n\n", b"\n\n> **PERFORMED 2026-10-04.** Recorded.\n\n", 1)
    perf_files = dict(blobs)
    perf_files[PACKET_REL] = performed
    results.append(("PERFORMED head over the frozen packet accepted",
                    not refused("frozen subject does not carry", act, arg,
                                make(subject=subj, packet=performed, frozen_files=perf_files))))
    results.append(("packet carrying a digest refused",
                    refused("64-hex token", act, arg, make(subject=subj, packet=pkt + arg.encode()))))
    results.append(("review binding another manifest digest refused",
                    refused("manifest file's SHA-256", act, arg,
                            make(subject=subj, review=review.replace(msha, "0" * 64)))))
    results.append(("review binding a row instead of the file digest refused",
                    refused("manifest file's SHA-256", act, arg,
                            make(subject=subj, review=review.replace(msha, arg)))))
    results.append(("verdict REVISE refused",
                    refused("verdict", act, arg,
                            make(subject=subj, review=review.replace("CONFIRM", "REVISE")))))
    results.append(("verdict displaced past the fourth head line refused",
                    refused("verdict", act, arg,
                            make(subject=subj, review=review.replace(
                                "Verdict: CONFIRM", "Note: x\nVerdict: CONFIRM")))))
    exc_review = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
        "none", "**Finding 1 — t** (revise)\nbody")
    results.append(("a revise finding under CONFIRM WITH EXCEPTIONS refused",
                    refused("non-note", act, arg, make(subject=subj, review=exc_review))))
    notes = exc_review.replace("(revise)", "(note)")
    results.append(("notes-only CONFIRM WITH EXCEPTIONS accepted",
                    _accepts(act, arg, make(subject=subj, review=notes))))

    def bad_disposition(findings):
        raise ValueError("disposition record does not name the reviewed raw")
    results.append(("missing disposition refused",
                    refused("disposition", act, arg,
                            make(subject=subj, review=notes, disposition_check=bad_disposition))))
    for name, sel in (("empty label", Selection("q", "", "d")),
                      ("multi-line description", Selection("q", "l", "a\nb")),
                      ("digest in opening", Selection("q " + "a" * 64, "l", "d"))):
        try:
            sel.validate()
            results.append((f"selection with {name} refused", False))
        except ValueError:
            results.append((f"selection with {name} refused", True))
    ok_sel = Selection("Perform the admission acts?", "All three now", "Perform the acts at the manifest rows.")
    try:
        record, block = expected(act, arg, "2026-10-04", ok_sel, make(subject=subj))
        results.append(("record and block render, naming the row and the tag",
                        arg in record and arg in block and tag_for(act, "2026-10-04") in record))
        results.append(("record carries the phrase exactly once in its ceremony",
                        record.count(phrase_for(act, arg)) == 1))
    except ValueError as exc:
        print(f"  (render failure: {exc})")
        results.append(("record and block render", False))
    results.append(("bad date refused", _raises(lambda: expected(
        act, arg, "04/10", ok_sel, make(subject=subj)))))
    failed = [name for name, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def _accepts(act, argument, inp) -> bool:
    try:
        validate(act, argument, inp)
        return True
    except ValueError:
        return False


def _raises(fn) -> bool:
    try:
        fn()
    except ValueError:
        return True
    return False


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", nargs=2, metavar=("KEY", "ARGUMENT"))
    mode.add_argument("--check", nargs=2, metavar=("KEY", "ARGUMENT"))
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--question-opening")
    ap.add_argument("--selection-label")
    ap.add_argument("--selection-description")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
    key, argument = args.record or args.check
    if key not in ACT_BY_KEY:
        print(f"unknown act key {key}; one of {', '.join(ACT_BY_KEY)}", file=sys.stderr)
        return 2
    if not (args.date and args.question_opening and args.selection_label
            and args.selection_description):
        print("--date, --question-opening, --selection-label and "
              "--selection-description are required", file=sys.stderr)
        return 2
    sel = Selection(args.question_opening, args.selection_label, args.selection_description)
    fn = do_record if args.record else do_check
    return fn(ROOT, ACT_BY_KEY[key], argument, args.date, sel)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
