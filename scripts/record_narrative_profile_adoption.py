#!/usr/bin/env python3
"""Record or verify the owner's adoption of the non-governed narrative profile.

Package `contracts/candidates/non-governed-narrative-profile/` (PR #256) and the
OpenSpec change `polaris-non-governed-narrative-profile`. The adoption form the
package recommends (its question O3) is a structured option selection that
names the package, recorded as a plain owner direction in the manner of
`POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`: it binds no digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing in `check_governance.py`. The
owner's selection states whether the version-tagged Scope A sign-off is read to
cover a Polaris generation specification delta (it does not name one
[Inferred]); `scripts/record_versioned_signoff.py` is not used, because its
package-builder contract is unmet by this package. If the owner chooses the
phrase-and-digest form instead, this script does not apply.

The script performs nothing by itself. `--record` requires, before it writes:

1. the specification file (under `proposed/` before the install step, under
   `specs/` after it) hashes to `SUBJECT_SHA`, the digest the confirming
   review's head names; the digest is held here, never in package Markdown;
2. the confirming raw's first four non-blank lines carry
   `Reviewed commit: <40 hex>`, `Subject SHA-256: <SUBJECT_SHA>` and a verdict
   of `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; the latter clears the bytes only
   when every finding is a `note` and the sibling dispositions record names the
   raw on a `Reviewed record:` line and dispositions every note
   (2026-09-26 owner ruling);
3. the owner's selection (opening, label, description) is non-empty, one line
   each, and carries no 64-hex digest.

It then writes the decision record. It does not move the specification: that
is `scripts/install_redis_sitting.py` (runbook F8, F11), which runs after the
acts. `--check` regenerates the record from the live bytes and compares.
`--selftest` mutates each predicate and requires it to fail closed.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import pathlib
import re
import sys
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).resolve().parents[1]

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
PKG = pathlib.Path(".syzygy/governance/contracts/candidates/non-governed-narrative-profile")
CHANGE = pathlib.Path("openspec/changes/polaris-non-governed-narrative-profile")
SPEC_PROPOSED = CHANGE / "proposed/polaris-generation/spec.md"
SPEC_ADOPTED = CHANGE / "specs/polaris-generation/spec.md"
PACKET_REL = PKG / "OWNER-DECISION-PACKET.md"
REVIEW_REL = PKG / "reviews/R-NON-GOVERNED-NARRATIVE-PROFILE-3-RAW.md"
DISPOSITION_REL = PKG / "reviews/ROUND-3-DISPOSITIONS.md"
RECORD_REL = DECISIONS / "POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md"

#: SHA-256 of the specification file the confirming review (round 3, notes-only
#: CONFIRM WITH EXCEPTIONS) read, as its head states it. Taken from the raw's
#: own head line by script, not typed; the repairs after the review touched
#: non-subject files only, so the file is unchanged.
SUBJECT_SHA = "3b2abfe9221c6aba641c86a23819a3fce5bb0e15617170e7aa7351fc479cb9b3"

VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INSTANT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RECORDED_RE = re.compile(r"^Recorded at \(UTC\): (\S+)$", re.MULTILINE)
HEX64_RE = re.compile(r"[0-9a-f]{64}")
REVIEWED_COMMIT_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})\s*$")
SUBJECT_LINE_RE = re.compile(r"^Subject SHA-256: ([0-9a-f]{64})\s*$")
VERDICT_RE = re.compile(r"^Verdict: (.+?)\s*$")
FINDINGS_NUMBER_RE = re.compile(r"^\*\*Finding (\d+) [—–-] [^\n]*?\*\*\s*\((blocking|revise|note)\b", re.M)
DISPOSITION_NOTE_RE = re.compile(r"^\*\*Note (\d+)\b", re.M)
INSTANT_OK = "2026-10-04T09:30:00Z"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


@dataclass
class Inputs:
    spec: bytes
    review: str
    disposition: str
    packet: str


def live_inputs(root: pathlib.Path) -> Inputs:
    def read(rel, binary=False):
        p = root / rel
        if not p.is_file():
            return b"" if binary else ""
        return p.read_bytes() if binary else p.read_text()
    spec = read(SPEC_ADOPTED, True) or read(SPEC_PROPOSED, True)
    return Inputs(spec, read(REVIEW_REL), read(DISPOSITION_REL), read(PACKET_REL))


def validate(inp: Inputs, subject_sha: str = SUBJECT_SHA) -> tuple[str, str]:
    """Return (reviewed commit, verdict) or raise ValueError."""
    if not inp.spec:
        raise ValueError("the specification file is in neither proposed/ nor specs/")
    if digest(inp.spec) != subject_sha:
        raise ValueError(f"the specification hashes to {digest(inp.spec)}, not the digest the confirming review read")
    if HEX64_RE.search(inp.packet):
        raise ValueError("owner packet carries a 64-hex token; the package carries no digest")
    head = [line for line in inp.review.splitlines() if line.strip()][:4]
    commits = [m.group(1) for line in head if (m := REVIEWED_COMMIT_RE.match(line))]
    if len(commits) != 1:
        raise ValueError("confirmation review head does not name exactly one reviewed commit")
    subjects = [m.group(1) for line in head if (m := SUBJECT_LINE_RE.match(line))]
    if subjects != [subject_sha]:
        raise ValueError("confirmation review head does not bind the specification's SHA-256 on a `Subject SHA-256:` line")
    verdicts = [m.group(1) for line in head if (m := VERDICT_RE.match(line))]
    if len(verdicts) != 1 or verdicts[0] not in VERDICTS:
        raise ValueError("confirmation review head does not carry the verdict CONFIRM or CONFIRM WITH EXCEPTIONS")
    if verdicts[0] == "CONFIRM WITH EXCEPTIONS":
        findings = {int(n): sev for n, sev in FINDINGS_NUMBER_RE.findall(inp.review)}
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; only a notes-only round clears the bytes")
        if f"Reviewed record: {REVIEW_REL.as_posix()}" not in inp.disposition.splitlines():
            raise ValueError("disposition record does not name the reviewed raw on a `Reviewed record:` line")
        noted = {int(n) for n in DISPOSITION_NOTE_RE.findall(inp.disposition)}
        if noted != set(findings):
            raise ValueError(f"disposition record notes {sorted(noted)} do not match the review's {sorted(findings)}")
    return commits[0], verdicts[0]


def render(date: str, instant: str, sel: Selection, reviewed: str, verdict: str) -> str:
    return f"""# Polaris non-governed narrative profile — adoption

Date: {date}

Recorded at (UTC): {instant}

Owner: Tzeusy

On {date} the owner adopted the non-governed narrative profile: requirement 032
of the Polaris generation specification, as a plain owner direction by option
selection. The direction binds no digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing in `scripts/check_governance.py`.

- **The owner's words.** The structured question in the Claude Code CLI opened
  "{sel.opening}"; the selected option, label and description verbatim:

| Label | Description |
|---|---|
| "{sel.label}" | "{sel.description}" |

- **What it adopts:** requirement 032 in
  `{SPEC_ADOPTED.as_posix()}`, as merged with this
  record, over the package at `{PKG.as_posix()}/`
  (delta, ledger, brief and packet). The specification file adopted is the
  file the confirming review read, checked by script from the digest the
  review's head names; this record carries no digest.
- **Confirming review:** `{REVIEW_REL.as_posix()}`, verdict `{verdict}`; the
  raw names reviewed commit `{reviewed}` [Observed — the raw's own line;
  provenance only]. Its notes are dispositioned in
  `{DISPOSITION_REL.as_posix()}`.
- **Scope A.** Whether the version-tagged sign-off of
  `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` covers a Polaris
  generation specification delta is the owner's reading, stated in the
  selection above (packet question O3); this record states no reading of its
  own.
- **Install step:** the specification moves from `proposed/` to `specs/` and
  the status page's effective-composition figure follows the recount tool, in
  the change that records this direction (`scripts/install_redis_sitting.py`).

It grants no read, egress, write, execution, deployment or release authority,
adopts no consent, policy or registry entry, and decides neither the altitude
order of a dossier nor the glossary question (packet O5). It amends no adopted
file and no contract.
"""


def expected(sel: Selection, date: str, instant: str, inp: Inputs, subject_sha: str = SUBJECT_SHA) -> str:
    sel.validate()
    if not DATE_RE.fullmatch(date):
        raise ValueError("date must be YYYY-MM-DD")
    if not INSTANT_RE.fullmatch(instant) or not instant.startswith(date + "T"):
        raise ValueError("instant must be YYYY-MM-DDTHH:MM:SSZ (UTC) on the direction's date")
    reviewed, verdict = validate(inp, subject_sha)
    return render(date, instant, sel, reviewed, verdict)


def do_record(root: pathlib.Path, date: str, sel: Selection, instant: str | None = None) -> int:
    if instant is None:
        instant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if (root / RECORD_REL).exists():
        print(f"FAILED: the adoption record already exists: {RECORD_REL.as_posix()}")
        return 1
    try:
        text = expected(sel, date, instant, live_inputs(root))
    except ValueError as exc:
        print(f"FAILED (nothing written): {exc}")
        return 1
    (root / RECORD_REL).write_text(text)
    print(f"recorded at {instant}\nwrote {RECORD_REL.as_posix()}")
    print("next, in the same change: python3 scripts/install_redis_sitting.py "
          "(moves the specification to specs/ and re-derives the status figure)")
    return 0


def do_check(root: pathlib.Path, date: str, sel: Selection, instant: str | None = None) -> int:
    path = root / RECORD_REL
    if instant is None:
        found = RECORDED_RE.findall(path.read_text()) if path.is_file() else []
        if len(found) != 1:
            print(f"FAILED: {RECORD_REL.as_posix()} carries {len(found)} 'Recorded at (UTC)' lines, not 1")
            return 1
        instant = found[0]
    try:
        text = expected(sel, date, instant, live_inputs(root))
    except ValueError as exc:
        print(f"FAILED: {exc}")
        return 1
    if path.read_text() != text:
        print(f"recorded direction differs from regeneration: {RECORD_REL.as_posix()}")
        return 1
    print("recorded adoption matches the live bytes")
    return 0


def _raises(fn) -> bool:
    try:
        fn()
    except ValueError:
        return True
    return False


def selftest() -> int:
    import contextlib
    import io
    import shutil
    import tempfile
    res: list[tuple[str, bool]] = []
    spec = b"spec bytes\n"
    sha = digest(spec)
    review = (f"# R3\nReviewed commit: {'a' * 40}\nSubject SHA-256: {sha}\nVerdict: CONFIRM\n\n## Findings\n\nnone\n")
    cwe = review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS").replace(
        "none", "**Finding 1 — t** (note)\nbody\n**Finding 2 — u** (note)\nbody")
    disp = f"Reviewed record: {REVIEW_REL.as_posix()}\n\n**Note 1 — t.** done\n\n**Note 2 — u.** done\n"

    def make(**over) -> Inputs:
        base = dict(spec=spec, review=review, disposition="", packet="# P\n")
        base.update(over)
        return Inputs(**base)

    def refused(needle, inp) -> bool:
        try:
            validate(inp, sha)
        except ValueError as exc:
            return needle in str(exc)
        return False

    def accepts(inp) -> bool:
        try:
            validate(inp, sha)
            return True
        except ValueError:
            return False

    res.append(("confirming review with the exact spec validates", accepts(make())))
    res.append(("missing specification refused", refused("neither", make(spec=b""))))
    res.append(("specification of other bytes refused", refused("hashes to", make(spec=spec + b"x"))))
    res.append(("packet carrying a digest refused", refused("64-hex", make(packet="a" * 64))))
    res.append(("head binding another subject digest refused",
                refused("Subject SHA-256", make(review=review.replace(sha, "0" * 64)))))
    res.append(("head naming no reviewed commit refused",
                refused("reviewed commit", make(review=review.replace("Reviewed commit: " + "a" * 40, "Reviewed commit: x")))))
    res.append(("verdict REVISE refused", refused("verdict", make(review=review.replace("CONFIRM", "REVISE")))))
    res.append(("verdict displaced past the fourth head line refused",
                refused("verdict", make(review=review.replace("Verdict: CONFIRM", "Note: x\nVerdict: CONFIRM")))))
    res.append(("notes-only CONFIRM WITH EXCEPTIONS with dispositions accepted",
                accepts(make(review=cwe, disposition=disp))))
    res.append(("a revise finding under CONFIRM WITH EXCEPTIONS refused",
                refused("non-note", make(review=cwe.replace("(note)", "(revise)", 1), disposition=disp))))
    res.append(("disposition naming another raw refused",
                refused("Reviewed record", make(review=cwe, disposition=disp.replace("R-NON", "R-OTHER")))))
    res.append(("disposition missing a note refused",
                refused("do not match", make(review=cwe, disposition=disp.replace("**Note 2", "**Aside 2")))))
    res.append(("CONFIRM WITH EXCEPTIONS with no finding refused",
                refused("no countable", make(review=review.replace("Verdict: CONFIRM", "Verdict: CONFIRM WITH EXCEPTIONS")))))
    for name, sel in (("empty label", Selection("q", "", "d")), ("multi-line description", Selection("q", "l", "a\nb")),
                      ("digest in opening", Selection("q " + "a" * 64, "l", "d"))):
        res.append((f"selection with {name} refused", _raises(sel.validate)))
    ok_sel = Selection("Adopt the profile?", "Adopt", "Adopt the package; Scope A is read to cover it.")
    text = expected(ok_sel, "2026-10-04", INSTANT_OK, make(), sha)
    res.append(("record renders the selection, the instant and no digest",
                "Adopt the package" in text and text.count(f"Recorded at (UTC): {INSTANT_OK}") == 1
                and not HEX64_RE.search(text)))
    res.append(("bad date refused", _raises(lambda: expected(ok_sel, "04/10", INSTANT_OK, make(), sha))))
    for name, bad in (("a date-only instant", "2026-10-04"), ("a local-offset instant", "2026-10-04T09:30:00+08:00"),
                      ("an instant on another date", "2026-10-05T00:00:00Z")):
        res.append((f"{name} refused", _raises(lambda bad=bad: expected(ok_sel, "2026-10-04", bad, make(), sha))))
    # end to end in a bare scratch copy: record, check, a second record refused, drift caught
    real = digest((ROOT / SPEC_PROPOSED).read_bytes()) if (ROOT / SPEC_PROPOSED).is_file() else (
        digest((ROOT / SPEC_ADOPTED).read_bytes()) if (ROOT / SPEC_ADOPTED).is_file() else "")
    if real != SUBJECT_SHA:
        print("  (skipped end-to-end: the live specification does not hash to SUBJECT_SHA)")
    else:
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            for rel in (PKG, CHANGE):
                shutil.copytree(ROOT / rel, root / rel)
            (root / DECISIONS).mkdir(parents=True)
            with contextlib.redirect_stdout(io.StringIO()):
                wrote = do_record(root, "2026-10-04", ok_sel, INSTANT_OK)
                checked = do_check(root, "2026-10-04", ok_sel)
                again = do_record(root, "2026-10-04", ok_sel, INSTANT_OK)
                (root / RECORD_REL).write_text((root / RECORD_REL).read_text() + "x")
                drifted = do_check(root, "2026-10-04", ok_sel)
            res.append(("record, check, refused repeat and caught drift in a bare copy",
                        (wrote, checked, again, drifted) == (0, 0, 1, 1)))
    failed = [n for n, g in res if not g]
    for n, g in res:
        print(("ok   " if g else "FAIL ") + n)
    print(f"selftest: {len(res) - len(failed)} of {len(res)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--instant", help="UTC instant YYYY-MM-DDTHH:MM:SSZ; --record defaults to now, --check reads it from the record")
    ap.add_argument("--question-opening")
    ap.add_argument("--selection-label")
    ap.add_argument("--selection-description")
    args = ap.parse_args(argv[1:])
    if args.selftest:
        return selftest()
    if not (args.date and args.question_opening and args.selection_label and args.selection_description):
        print("--date, --question-opening, --selection-label and --selection-description are required",
              file=sys.stderr)
        return 2
    sel = Selection(args.question_opening, args.selection_label, args.selection_description)
    return (do_record if args.record else do_check)(ROOT, args.date, sel, args.instant)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
