#!/usr/bin/env python3
"""A quotation attributed to a file and line must have been said by that file.

Review RD-6 (`round-2026-08c/reviews/RD-6-source-of-truth-RAW.md`, finding
F-2) found a verifier justification attributed to a report that did not
contain it, and two earlier reviews had accepted the attribution as
recorded. Its closure report routed the class to bead `syzygy-0wf`: nothing
checked that a quotation matches its source. This script is that check. It
is read-only and writes nothing.

**What counts as a quotation with a source.** Only a quoted span written
directly beside a `path:line` locator, in one of three adjacency forms,
inside one paragraph (hard-wrapped lines are joined first, so a quotation
that wraps is still one quotation):

  * `loc-paren-quote` — `path:12` ("quoted text")
  * `loc-colon-quote` — `path:12`: "quoted text"; the separator may also be
    `—`, `–`, `,` or a table-cell `|`, optionally followed by `reads`,
    `says` or `states`
  * `quote-paren-loc` — "quoted text" (`path:12`)

The predicate is the regexes `LOCATOR`, `QUOTE` and `FORMS` below, not this
prose: a locator is `<path>.<ext>:<line>` or `:<first>-<last>`, backticks
optional, `<ext>` one of `EXTENSIONS`; a quoted span is `"…"` or `“…”` of at
least four characters, with up to two emphasis asterisks either side.

**What "matches" means.** Both sides are folded the same way (`fold()`):
emphasis asterisks and backticks dropped, every quote character made one,
blockquote markers dropped, whitespace collapsed, case folded. An ellipsis
(`…`, `...`) or a bracketed editorial insertion (`[…]`, `[the clause]`) in
the quotation is a gap: the fragments either side must occur in the source
in order.

**Three outcomes, and only one fails.**

  1. Found in the cited file now. Passes. If it sits outside the cited
     lines (±`DRIFT_SLACK`), it is counted as **locator drift** — line
     numbers move with every edit, and the claim this check defends is the
     words.
  2. Not in the file now, but in a committed revision of it (`git log
     --follow`). The source was amended after it was quoted: an applied
     doctrine amendment quoting the sentence it replaced is the live case.
     Reported with the most recent revision that carried it, never failed.
  3. In no revision of the file, ever. **That is a finding** — the shape of
     F-2, a quotation its source never contained.

**Resolution.** A locator path is tried relative to the citing file, then
to the repository root; only when neither exists, as a suffix of every
tracked path. Every candidate found is searched, so `README.md:60` written
in `decisions/` passes on the root README as well as its own. A locator that resolves to no tracked file is
counted and skipped: CG-1 owns dangling paths.

**Population.** Tracked `.md` files, less three classes that are verbatim
records of what a source said *then*: raw review output
(`check_governance._is_raw_review`, imported, never copied — a second copy
of a population rule is RD-6 F-3's defect), the eleven `round-*`
directories, and `contracts/candidates/history/`. Their quotations are
scanned and their not-found-now counts printed, so the exclusion is a
reported denominator rather than a silence; their history is not searched.

**RESIDUAL LIMIT.** A quotation with no adjacent locator, a blockquote under
a locator line, a paraphrase, and a quotation of a source outside the
repository are all outside the population, and so is a quotation in a code
comment — F-2's own site. Measured 2026-10-03 over every tracked `.py`,
`.ts` and `.mjs` file, the forms below reach one span there, and it is code,
not a quotation. A locator naming the wrong file
that happens to contain the same words passes. A revision lookup follows
renames of the resolved path only. In a shallow clone the history is
partial, so an amended quotation reads as a finding — red, never falsely
green; the run says when the clone is shallow.

The routing of RD-6's fourteen open findings, and this check's rule-6
mutation record, live in
`docs/evidence/rd6-source-of-truth-routing-2026-10-03/`.

Usage:
  check_quotations.py              check the tracked corpus; exit 1 on findings
  check_quotations.py --verbose    also list drift and amended quotations
  check_quotations.py --selftest   run the synthetic fixtures
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from check_governance import _is_raw_review  # noqa: E402

EXTENSIONS = ("md", "py", "yaml", "yml", "txt", "json", "ts", "mjs", "toml")
LOCATOR = (r"`?(?P<path>[A-Za-z0-9_][A-Za-z0-9_./\-]*\.(?:"
           + "|".join(EXTENSIONS)
           + r")):(?P<first>\d+)(?:[-–](?P<last>\d+))?`?")
QUOTE = (r"\*{0,2}(?:\"(?P<q1>[^\"\n]{4,}?)\"|“(?P<q2>[^”\n]{4,}?)”)"
         r"\*{0,2}")
FORMS = (
    ("loc-paren-quote",
     re.compile(LOCATOR + r"\s*\(\s*(?:(?:reads|says)\s*)?" + QUOTE)),
    ("loc-colon-quote",
     re.compile(LOCATOR + r"\s*(?::|—|–|,|\|)?\s*"
                r"(?:(?:reads|says|states)\s*)?:?\s*" + QUOTE)),
    ("quote-paren-loc",
     re.compile(QUOTE + r"\s*\(\s*" + LOCATOR + r"\s*\)")),
)
GAP = re.compile(r"…|\.\.\.|\[[^\]]*\]")
QUOTE_CHARS = re.compile(r"[\"'“”‘’]")
ROUND_DIR = re.compile(r"(?:^|/)round-\d{4}-\d{2}[a-z]?/")
HISTORY_DIR = ".syzygy/governance/contracts/candidates/history/"
FENCE = re.compile(r"^\s*(```|~~~)")
#: A quotation found within this many lines of its cited range is "at" it.
DRIFT_SLACK = 2

#: Findings recorded rather than repaired, each with why the citing bytes
#: stay as they are. A recorded finding is printed every run and never
#: fails; an entry that no longer matches a finding fails, so the list
#: cannot outlive the defects it names. Keyed by (citing file, quotation
#: prefix as written).
RECORDED = (
    (".syzygy/governance/contracts/candidates/policy-candidates/"
     "DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md",
     "endpoints in real **actuator** use *and* the three-axis propagation",
     "the quotation ends \"slice\"; doctrine/v1.md:53 at 9bdfe98a, the one "
     "revision carrying the sentence, ends \"proof-of-concept\", and no "
     "revision carries \"propagation slice\". Drafting text of the P-25(c) "
     "packet, "
     "applied within doctrine amendment D5, whose head banner says the "
     "text below it is unchanged; found by this check, 2026-10-03"),
)


def excluded_class(rel):
    """Why `rel` is a verbatim record outside the failing population."""
    if _is_raw_review(rel) or rel.endswith("-RAW.md"):
        return "raw review"
    if ROUND_DIR.search(rel):
        return "round directory"
    if rel.startswith(HISTORY_DIR):
        return "candidates history"
    return None


def fold(text):
    text = QUOTE_CHARS.sub('"', text)
    text = re.sub(r"^[ \t]*>[ \t]?", "", text, flags=re.M)
    text = re.sub(r"[*`]", "", text)
    return re.sub(r"\s+", " ", text).strip().casefold()


@dataclasses.dataclass
class Folded:
    """A source folded once, with the folded offset each line starts at."""
    text: str
    starts: list

    @classmethod
    def of(cls, raw):
        parts, starts, pos = [], [], 0
        for line in raw.split("\n"):
            starts.append(pos)
            f = fold(line)
            if f:
                parts.append(f)
                pos += len(f) + 1
        return cls(" ".join(parts), starts)

    def line_at(self, offset):
        n = 1
        for i, start in enumerate(self.starts, 1):
            if start <= offset:
                n = i
        return n


def fragments(quote):
    return [f.strip() for f in GAP.split(fold(quote)) if f.strip()]


def find_in_order(frags, text):
    """Offset of the first fragment if all occur in order, else -1."""
    pos, start = 0, -1
    for frag in frags:
        i = text.find(frag, pos)
        if i < 0:
            return -1
        if start < 0:
            start = i
        pos = i + len(frag)
    return start if frags else -1


def paragraphs(text):
    """(first line number, joined text) for each paragraph outside fences."""
    buf, start, fenced = [], 1, False
    for n, line in enumerate(text.split("\n"), 1):
        if FENCE.match(line):
            fenced = not fenced
            if buf:
                yield start, " ".join(buf)
            buf = []
            continue
        if fenced or not line.strip():
            if buf:
                yield start, " ".join(buf)
            buf = []
            continue
        if not buf:
            start = n
        buf.append(line.strip())
    if buf:
        yield start, " ".join(buf)


@dataclasses.dataclass
class Quotation:
    citer: str
    line: int
    form: str
    path: str
    first: int
    last: int
    text: str


def quotations(rel, text):
    for line, para in paragraphs(text):
        seen = set()
        for form, rx in FORMS:
            for m in rx.finditer(para):
                quote = m.group("q1") or m.group("q2")
                key = (quote, m.group("path"), m.group("first"))
                if key in seen:
                    continue
                seen.add(key)
                first = int(m.group("first"))
                last = int(m.group("last") or first)
                yield Quotation(rel, line, form, m.group("path"), first,
                                last, quote)


def resolve(citer, path, corpus, tracked):
    """The tracked files `path` names from `citer`: relative or root-relative
    if either exists, else every tracked path ending in it."""
    out = []
    for cand in (os.path.normpath(os.path.join(os.path.dirname(citer), path)),
                 os.path.normpath(path)):
        if cand in corpus and cand not in out:
            out.append(cand)
    if out:
        return out
    return [rel for rel in tracked if rel.endswith("/" + path) and rel in corpus]


def git_history(root):
    """Return `revisions(path)`: (short sha, text) per committed revision."""
    cache = {}

    def revisions(path):
        if path in cache:
            return cache[path]
        log = subprocess.run(
            ["git", "-C", root, "log", "--follow", "--format=%h",
             "--name-only", "--", path],
            capture_output=True, text=True).stdout.split("\n")
        out, sha = [], None
        for line in log:
            if not line.strip():
                continue
            if sha is None:
                sha = line.strip()
                continue
            blob = subprocess.run(["git", "-C", root, "show",
                                   f"{sha}:{line.strip()}"],
                                  capture_output=True, text=True)
            if blob.returncode == 0:
                out.append((sha, blob.stdout))
            sha = None
        cache[path] = out
        return out

    return revisions


@dataclasses.dataclass
class Result:
    examined: collections.Counter = dataclasses.field(
        default_factory=collections.Counter)
    findings: list = dataclasses.field(default_factory=list)
    recorded: list = dataclasses.field(default_factory=list)
    amended: list = dataclasses.field(default_factory=list)
    drift: list = dataclasses.field(default_factory=list)
    unresolved: int = 0
    citing_files: int = 0
    excluded: collections.Counter = dataclasses.field(
        default_factory=collections.Counter)
    excluded_misses: collections.Counter = dataclasses.field(
        default_factory=collections.Counter)


def check(corpus, tracked=None, revisions=None, recorded=RECORDED):
    """`corpus` maps repo-relative path to text; `revisions(path)` yields
    (sha, text) for each committed revision, newest first. Returns a Result."""
    tracked = sorted(corpus) if tracked is None else tracked
    revisions = revisions or (lambda path: [])
    folded = {}
    res = Result()
    unmatched = list(recorded)
    for rel in sorted(corpus):
        if not rel.endswith(".md"):
            continue
        cls = excluded_class(rel)
        counted = False
        for q in quotations(rel, corpus[rel]):
            targets = resolve(rel, q.path, corpus, tracked)
            if not targets:
                res.unresolved += 1
                continue
            frags = fragments(q.text)
            hit = None
            for tgt in targets:
                if tgt not in folded:
                    folded[tgt] = Folded.of(corpus[tgt])
                at = find_in_order(frags, folded[tgt].text)
                if at >= 0:
                    hit = (tgt, folded[tgt].line_at(at))
                    break
            if cls:
                res.excluded[cls] += 1
                res.excluded_misses[cls] += hit is None
                continue
            counted = True
            res.examined[q.form] += 1
            where = f"{q.citer}:{q.line}"
            shown = q.text[:70] + ("…" if len(q.text) > 70 else "")
            if hit is not None:
                tgt, n = hit
                if not q.first - DRIFT_SLACK <= n <= q.last + DRIFT_SLACK:
                    res.drift.append(f"{where} — cites {q.path}:{q.first}, "
                                     f"text now at {tgt}:{n}")
                continue
            past = next(((tgt, sha) for tgt in targets
                         for sha, text in revisions(tgt)
                         if find_in_order(frags, fold(text)) >= 0), None)
            if past:
                res.amended.append(f"{where} — \"{shown}\" left {past[0]} "
                                   f"after {past[1]}")
                continue
            named = ", ".join(targets[:3]) + (
                f" and {len(targets) - 3} more" if len(targets) > 3 else "")
            finding = (f"{where} — quotes {q.path}:{q.first} (\"{shown}\"), "
                       f"in no revision of {named}")
            entry = next((e for e in unmatched
                          if e[0] == rel and q.text.startswith(e[1])), None)
            if entry:
                unmatched.remove(entry)
                res.recorded.append(f"{finding} — recorded: {entry[2]}")
            else:
                res.findings.append(finding)
        res.citing_files += counted
    for citer, prefix, _ in unmatched:
        res.findings.append(f"RECORDED entry for {citer} "
                            f"(\"{prefix[:50]}…\") matches no finding — "
                            f"remove it")
    return res


def tracked_corpus(root):
    out = subprocess.run(["git", "-C", root, "ls-files", "-z"],
                         capture_output=True, text=True, check=True).stdout
    tracked = [p for p in out.split("\0") if p]
    corpus = {}
    for rel in tracked:
        if rel.rsplit(".", 1)[-1] not in EXTENSIONS:
            continue
        try:
            with open(os.path.join(root, rel), encoding="utf-8") as fh:
                corpus[rel] = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
    return corpus, tracked


def report(res, verbose=False):
    total = sum(res.examined.values())
    status = "FAIL" if res.findings else ("OK" if total else "WARN")
    forms = ", ".join(f"{name} {res.examined[name]}" for name, _ in FORMS)
    print(f"{status:5} QC-1  a quotation beside a path:line locator was said "
          f"by that file — {total} quotations examined in "
          f"{res.citing_files} files ({forms}), {len(res.findings)} findings")
    for f in res.findings:
        print(f"        {f}")
    print(f"note  QC-1  {len(res.recorded)} recorded findings, printed every "
          f"run and never failed (`RECORDED`)")
    for f in res.recorded:
        print(f"        {f}")
    notes = (
        (res.amended, f"{len(res.amended)} of {total} are in an earlier "
                      f"revision of their source only: amended since quoted, "
                      f"reported, never failed"),
        (res.drift, f"{len(res.drift)} of {total} found outside their cited "
                    f"lines (±{DRIFT_SLACK}): locator drift, reported, never "
                    f"failed"),
    )
    for lines, summary in notes:
        print(f"note  QC-1  {summary}")
        if verbose:
            for line in lines:
                print(f"        {line}")
    print(f"note  QC-1  {res.unresolved} locators name no tracked file "
          f"(CG-1 owns dangling paths); not examined")
    for cls in sorted(res.excluded):
        print(f"note  QC-1  excluded verbatim records, {cls}: "
              f"{res.excluded[cls]} quotations, {res.excluded_misses[cls]} "
              f"not in their source now; history not searched")
    return 1 if res.findings else 0


# ------------------------------------------------------------------ selftest

SOURCE = ("# Source\n\nline two\n\nThe modules win over this file, always.\n"
          "A *second* sentence that wraps\nacross two lines.\n\n"
          "She said “nothing here is dismissed”.\n")
FIXTURE = {
    "a/SOURCE.md": SOURCE,
    "README.md": "Two rules everything else follows from:\n",
    "docs/README.md": "unrelated\n",
}
OLD_SOURCE = "An earlier sentence the amendment replaced.\n"

#: (name, citing text, expected (examined, findings, amended, drift)).
CASES = (
    ("loc-paren-quote passes",
     '`a/SOURCE.md:5` ("The modules win over this file, always.")',
     (1, 0, 0, 0)),
    ("a quotation wrapped across the citing lines is one quotation",
     '`a/SOURCE.md:5` ("The modules win\nover this file, always.")',
     (1, 0, 0, 0)),
    ("loc-colon-quote passes across a wrap and emphasis",
     'See `SOURCE.md:6-7`: "a second sentence that wraps across two lines"',
     (1, 0, 0, 0)),
    ("a table-cell separator is a colon form",
     '| `a/SOURCE.md:5` | "The modules win over this file" |', (1, 0, 0, 0)),
    ("quote-paren-loc passes with an ellipsis gap",
     '"The modules win … always" (`a/SOURCE.md:5`)', (1, 0, 0, 0)),
    ("a bracketed insertion is a gap",
     '"The modules [of the package] win over this file" (`a/SOURCE.md:5`)',
     (1, 0, 0, 0)),
    ("nested quote characters fold",
     "`a/SOURCE.md:9` reads \"She said 'nothing here is dismissed'.\"",
     (1, 0, 0, 0)),
    ("a changed word is a finding",
     '`a/SOURCE.md:5` ("The modules lose to this file, always.")',
     (1, 1, 0, 0)),
    ("fragments out of order are a finding",
     '"always … The modules win" (`a/SOURCE.md:5`)', (1, 1, 0, 0)),
    ("the wrong line is drift, not a finding",
     '`a/SOURCE.md:1` ("The modules win over this file")', (1, 0, 0, 1)),
    ("a sentence an earlier revision carried is amended, not a finding",
     '`a/SOURCE.md:3` ("An earlier sentence the amendment replaced")',
     (1, 0, 1, 0)),
    ("an ambiguous basename passes on any candidate",
     '`README.md:1` says "Two rules everything else follows from:"',
     (1, 0, 0, 0)),
    ("a fenced example is not a quotation",
     '```\n`a/SOURCE.md:5` ("not in the source at all")\n```', (0, 0, 0, 0)),
    ("an unresolved locator is skipped, not failed",
     '`nowhere/MISSING.md:3` ("anything at all here")', (0, 0, 0, 0)),
)


def fake_revisions(path):
    return [("c0ffee1", OLD_SOURCE)] if path == "a/SOURCE.md" else []


def _git(cwd, *args):
    subprocess.run(["git", "-C", cwd, *args], check=True, capture_output=True)


def selftest():
    failed = total = 0

    def expect(name, ok, got):
        nonlocal failed, total
        total += 1
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'}  {name}: {got}")

    for name, text, want in CASES:
        corpus = dict(FIXTURE, **{"docs/CITER.md": text + "\n"})
        res = check(corpus, revisions=fake_revisions, recorded=())
        got = (sum(res.examined.values()), len(res.findings),
               len(res.amended), len(res.drift))
        expect(name, got == want, f"examined/findings/amended/drift {got}, "
                                  f"expected {want}")

    corpus = dict(FIXTURE)
    corpus["docs/reviews/R-X-RAW.md"] = '`a/SOURCE.md:5` ("not there")\n'
    corpus["x/round-2026-08c/NOTE.md"] = '`a/SOURCE.md:5` ("not there")\n'
    res = check(corpus, revisions=fake_revisions, recorded=())
    want = {"raw review": 1, "round directory": 1}
    expect("verbatim records are counted, never failed",
           not res.findings and dict(res.excluded_misses) == want,
           dict(res.excluded_misses))

    wrong = '`a/SOURCE.md:5` ("The modules lose to this file")\n'
    entry = ("docs/CITER.md", "The modules lose", "fixture")
    res = check(dict(FIXTURE, **{"docs/CITER.md": wrong}),
                revisions=fake_revisions, recorded=(entry,))
    got = (len(res.findings), len(res.recorded))
    expect("a recorded finding is printed, not failed", got == (0, 1),
           f"findings/recorded {got}")
    res = check(dict(FIXTURE, **{"docs/CITER.md": "no quotation\n"}),
                revisions=fake_revisions, recorded=(entry,))
    expect("a recorded entry with no finding fails", len(res.findings) == 1,
           f"findings {len(res.findings)}")

    # The revision lookup itself, against a real two-commit repository with
    # a rename between the commits, so `--follow` is what finds the old text.
    with tempfile.TemporaryDirectory() as tmp:
        _git(tmp, "init", "-q")
        _git(tmp, "config", "user.email", "selftest@example.invalid")
        _git(tmp, "config", "user.name", "selftest")
        #: Enough unchanged lines that git still sees one file renamed.
        kept = "".join(f"Unchanged line {i} of the source.\n"
                       for i in range(12))
        current = kept + "The sentence that replaced it.\n"
        with open(os.path.join(tmp, "OLD.md"), "w") as fh:
            fh.write(kept + OLD_SOURCE)
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "one")
        _git(tmp, "mv", "OLD.md", "NEW.md")
        with open(os.path.join(tmp, "NEW.md"), "w") as fh:
            fh.write(current)
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "two")
        corpus = {"NEW.md": current,
                  "CITER.md": ('`NEW.md:13` ("An earlier sentence the '
                               'amendment replaced")\n`NEW.md:13` ("A '
                               'sentence no revision ever carried")\n')}
        res = check(corpus, revisions=git_history(tmp), recorded=())
        got = (len(res.findings), len(res.amended))
        expect("git history across a rename: one amended, one finding",
               got == (1, 1), f"findings/amended {got}")

    print(f"selftest: {total - failed} of {total} passed")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--root", default=ROOT)
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    corpus, tracked = tracked_corpus(args.root)
    shallow = subprocess.run(
        ["git", "-C", args.root, "rev-parse", "--is-shallow-repository"],
        capture_output=True, text=True).stdout.strip()
    if shallow == "true":
        print("note  QC-1  shallow clone: revision history is partial, so an "
              "amended quotation reads as a finding")
    return report(check(corpus, tracked, git_history(args.root)),
                  verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
