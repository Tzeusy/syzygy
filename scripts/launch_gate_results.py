#!/usr/bin/env python3
"""Validate a launch-gate administration record and generate its trend row.

Scope, stated so nobody mistakes it: this tool **validates the record and
computes its derived figures**. Readiness semantics are owned by
`launch-gate-pre-specifications.md` (§4); where this tool applies the §4
formula it is checking the record's self-consistency against the instrument,
never deciding readiness independently of it. A record this tool passes can
still support nothing if the instrument's non-mechanical requirements
(fresh context, family disclosure, full administration) were not honored —
those live in the record's prose and the reader's judgment.

Checks (each with a `--selftest` mutation fixture):

  LG-1  header parses: date, named commit (existing in this repository),
        instrument version, instrument sha256, parameter-block sha256
  LG-2  instrument digest matches the committed instrument at the named
        commit; parameter-block digest matches §8 of that instrument
        (skipped with a printed notice when git or the path is unavailable)
  LG-3  verdict vocabulary is closed: Met / Not met /
        Not met (out of launch scope) / Unknown(reason); anything else —
        "Partially met", "Met with caveats" — is an error. The scoped form
        is lawful only in A–D (instrument §2/§4)
  LG-4  G1 is present as a section; a record without G1 cannot support a
        gate decision, and a G1 verdict *row* is an error — G1 yields no
        Met/Not-met verdict (instrument §3)
  LG-5  counts are computed from the rows, never trusted from prose; the
        explicit `Deferred count:` and `Reopened count:` fields are
        required — their absence is an error, never an implicit zero
        (VIS-2); the printed trend row carries the computed and parsed
        figures. Field occurrences disagreeing in value are an error — a
        narrative line must not shadow a declared field (RD36-03) — and
        every field value is line-anchored, so an empty field is absent
        rather than borrowing the next line's text (RD36-02)
  LG-6  the terminal `GATE VERDICT:` line — the last line CONTAINING the
        literal token, not the last regex match (RD35-02) — exists,
        parses to the closed verdict set (a qualified or quoted terminal
        verdict is an error, never an invitation to look upward), carries
        no `|` in the captured verdict (it would corrupt §6's nine-column
        trend row), and is consistent with the §4 formulas as computable
        from the rows. BOTH pass branches run the full conjunct battery
        (RD34-01): every E row Met, no plain Not met in A–D (the scoped
        form does not block), F3 Met, F4 Met, F1 Met-or-Unknown. Plain
        READY FOR additionally requires **F2 Met and zero declared
        deferrals**; READY-WITH-DEFERRALS substitutes exactly the F2 limb
        with an owner-cited deferral (instrument §4)
  LG-7  any record whose `Deferred count:` is nonzero — under ANY verdict
        (RD34-07) — and any READY-WITH-DEFERRALS verdict requires the
        `Owner deferral decision:` field, whose value must be a
        repository path (verified to exist at the named commit when git
        checks run — a leading `./` is a prefix strip, RD35-01 — and to
        be a file, not a directory, RD36-06) or an SDR-n identifier
        (existence-checked against the decisions home at the named
        commit, RD36-06). P-n names the pending queue, D-n a delta item,
        and B-n is round-2026-08c review-finding numbering — none grants
        a deferral (RD35-06, RD36-01); label wording like "(owner only)"
        is rejected (RD34-02); a deferral-carrying verdict with
        `Deferred count: 0` is an error
  LG-8  E1's five sub-verdict rows (form, home, granularity,
        acceptance-authority, change-process) are present, and an E1
        rollup of Met requires all five sub-rows Met
  LG-9  a record with any scoped row must name at least one defect on the
        deferred-wave findings line — "names nothing" is a shared rule
        (LG-9/LG-12/LG-13), not an enumeration: a value whose first
        token is a negation word ("no defects found", "none identified")
        asserts emptiness (RD36-04), and otherwise at least one token
        must fall outside the placeholder lexicon, so decorated forms
        ("(none known)", "-- none --", "unknown", "tba") fail too
        (instrument §4, RD33-01; widened RD34-06; lexicon rule RD35-05)
  LG-10 the full question roster is present AND nothing else is — A1–A6,
        B1–B5, C1–C7, D1–D4, E1 with its five sub-rows, E2–E6, F1–F6; a
        missing row is an error, never a pass (a delta record cannot
        support a gate decision, instrument §2/§5, RD33-05), and a row ID
        outside the roster is an error too, so an invented question
        cannot enter the trend row's computed columns (RD34-11)
  LG-11 the record's declared instrument version matches the committed
        instrument at the named commit, and its `Launch target:` line
        equals — whitespace-normalized — the parameter block's
        LAUNCH_TARGET or its first sentence, per §5's "verbatim"
        (RD33-06; upgraded from containment, RD34-08); the SAME equality
        test applies to a `READY FOR <target>` verdict line's tail — the
        one string the trend log carries cannot name a target §8 never
        bound (RD35-03). Needs git, skipped with LG-2's notice otherwise;
        the missing-line case errors regardless
  LG-12 §5's declared record fields are present — the non-authority
        banner (RD24-02), `Reviewer:` (the fresh-context disclosure,
        RD36-05), `Reviewer model family:`, `Materials given:`,
        `Operationalization notes:`, `E3 reopen-list:`, `Unknowns and
        what would settle them:`, `Reviewer's falsification notes:` — a
        template field deleted without an error reads as answered; and a
        record with any Unknown row must name settling evidence in the
        Unknowns field — an empty or placeholder value fails, per §4
        (RD35-07, RD36-02). Presence tests are content-blind by design:
        the field's truthfulness stays with the record's prose and the
        reader's judgment
  LG-13 the E3 reopen-list cross-check: a non-empty `E3 reopen-list:`
        beside `E3 | Met` or any READY verdict is an error — §3's own
        "the list is non-empty; 'ready' is then false regardless of
        every other verdict" is the instrument's self-declared sharpest
        single gate, enforced beside LG-8/LG-9 as the same shape: a
        declared field contradicting a verdict row (RD35-04)

Usage:
  python3 scripts/launch_gate_results.py <record.md>
      [--instrument launch-gate-pre-specifications.md] [--prior <record.md>]
  python3 scripts/launch_gate_results.py --selftest
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INSTRUMENT_DEFAULT = "launch-gate-pre-specifications.md"

VERDICT_RE = re.compile(
    r"^(Met|Not met \(out of launch scope\)|Not met|"
    r"Unknown\s*(?:\(|—|-).+)$")
ROW_RE = re.compile(
    r"^\|\s*\**([A-G]\d+(?:-[a-z][a-z-]*)?)\**\s*\|\s*\**([^|]+?)\**\s*\|")
SECTION_OF = lambda q: q[0]
SCOPED = "Not met (out of launch scope)"
E1_SUBS = ("E1-form", "E1-home", "E1-granularity",
           "E1-acceptance-authority", "E1-change-process")
# The full-administration roster (instrument §3/§5): a record missing any
# of these rows cannot support a gate decision — absence is never a pass.
ROSTER = (tuple(f"A{i}" for i in range(1, 7))
          + tuple(f"B{i}" for i in range(1, 6))
          + tuple(f"C{i}" for i in range(1, 8))
          + tuple(f"D{i}" for i in range(1, 5))
          + E1_SUBS + ("E1",)
          + tuple(f"E{i}" for i in range(2, 7))
          + tuple(f"F{i}" for i in range(1, 7)))
GATE_VERDICT_RE = re.compile(
    r"GATE VERDICT[:\s]+\**\s*(READY FOR [^*\n]+?|NOT READY|"
    r"READY-WITH-DEFERRALS[^*\n]*)\s*\**\s*$", re.M)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_show(commit: str, path: str):
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO), "show", f"{commit}:{path}"],
            capture_output=True)
        return out.stdout if out.returncode == 0 else None
    except OSError:
        return None


def commit_exists(sha: str) -> bool:
    try:
        return subprocess.run(
            ["git", "-C", str(REPO), "cat-file", "-e", f"{sha}^{{commit}}"],
            capture_output=True).returncode == 0
    except OSError:
        return False


def param_block_bytes(instrument_text: bytes):
    """§8's bytes: from the '## 8.' heading to the next '## ' heading."""
    txt = instrument_text.decode("utf-8", errors="replace")
    m = re.search(r"^## 8\..*$", txt, re.M)
    if not m:
        return None
    rest = txt[m.start():]
    nxt = re.search(r"^## (?!8\.)", rest[1:], re.M)
    span = rest if not nxt else rest[: nxt.start() + 1]
    return span.encode("utf-8")


def _norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# RD35-06/RD36-01: only families that name MADE decisions may claim a
# granted deferral. P-n is this repository's pending-decision queue (a
# decision not yet made), D-n is a semantic-delta item number, and B-n is
# round-2026-08c's review-finding numbering (zero B-n tokens exist in the
# decisions home) — none grants anything. The one identifier family naming
# made decisions is SDR-n; every other decision is cited by its repository
# path.
DECISION_ID_RE = re.compile(r"SDR-\d+[a-z]?(?:\([a-z]\))?$")
_UNMADE_ID_RE = re.compile(r"(?:P|D)-\d+[a-z]?(?:\([a-z]\))?$")
_FINDING_ID_RE = re.compile(r"B-\d+[a-z]?(?:\([a-z]\))?$")

DECISIONS_HOME = ".syzygy/governance/decisions"


def _sdr_exists(ident, commit):
    """RD36-06/RD37-05: an SDR-n citation must name a decision present in
    the decisions home at the named commit — matched at identifier
    boundaries, never by substring (a fixed-string search would accept an
    unminted `SDR-3` on the strength of a minted `SDR-33` if the
    population ever had gaps), and scoped to MADE decisions: the
    pending-decision queue is excluded, because a mention in the queue of
    decisions not yet made grants nothing — the guard's own stated
    purpose. Honest cap: the live SDR population (SDR-1…33, gapless)
    makes the substring direction unfixturable against the real corpus
    today; the boundary anchoring is asserted structurally here and
    disclosed in the v1.10 delta rather than silently."""
    pat = r"(^|[^-A-Za-z0-9])" + re.escape(ident) + r"($|[^0-9a-z(])"
    try:
        return subprocess.run(
            ["git", "-C", str(REPO), "grep", "-qE", pat, commit,
             "--", DECISIONS_HOME,
             f":(exclude){DECISIONS_HOME}/PENDING-OWNER-DECISIONS.md"],
            capture_output=True).returncode == 0
    except OSError:
        return False


def _deferral_citation_error(val, commit, _git):
    """RD34-02: the citation must be a repository path (existing at the
    named commit when git checks run) or a made-decision identifier —
    label wording is not a citation."""
    v = val.strip().strip("`")
    if DECISION_ID_RE.fullmatch(v):
        if not _git or not commit:
            return None  # shape lawful; existence unverifiable without git
        if not _sdr_exists(v, commit):
            return (f"{v!r} names no decision in {DECISIONS_HOME} at the "
                    "named commit — the SDR population is finite, and a "
                    "citation to an unminted ruling grants nothing "
                    "(RD36-06)")
        return None
    if _UNMADE_ID_RE.fullmatch(v):
        return (f"{v!r} names the pending-decision queue (P-n) or a "
                "semantic-delta item (D-n) — a deferral is granted only by "
                "a made decision: SDR-n or its repository path (RD35-06)")
    if _FINDING_ID_RE.fullmatch(v):
        return (f"{v!r} is review-finding numbering (round-2026-08c's B-n "
                "findings) — it names no decision in this repository and "
                "grants nothing; cite SDR-n or the decision's repository "
                "path (RD36-01)")
    if "/" in v:
        if not _git or not commit:
            return None  # shape lawful; existence unverifiable without git
        # RD35-01: prefix strip, never str.lstrip — a character-class strip
        # turned `.syzygy/…` into `syzygy/…` and rejected every real
        # decision path in the repository's own decision home.
        path = v[2:] if v.startswith("./") else v
        blob = git_show(commit, path)
        if blob is None:
            return (f"path {v!r} does not exist at the named commit — a "
                    "citation to nowhere authorizes nothing")
        if blob.startswith(b"tree "):
            return (f"path {v!r} is a directory at the named commit — a "
                    "tree is not a decision record; cite the record file "
                    "itself (RD36-06)")
        return None
    return (f"{v!r} is neither a repository path nor a decision identifier "
            "— label wording is not a citation (RD34-02)")


# One definition of "names nothing", serving LG-9 and LG-12 — the two
# checks where "names nothing" IS the error — RD35-04/RD35-05. It no
# longer serves LG-13: there "names nothing" was the NO-error branch, so
# the two consumers read one predicate with opposite polarities, and
# RD36-04's widening (the negation-prefix rule) tightened LG-9/LG-12 while
# silently LOOSENING LG-13 — a negation-led line still enumerating reopen
# items ("no items are resolved: (1) …") validated clean beside `E3 | Met`
# under READY, a measured regression against v1.8. A predicate may not be
# shared by consumers of opposite polarity (RD37-01); LG-13 now carries
# its own positive emptiness test below.
# A lexicon rule, not an enumeration: after stripping punctuation and
# articles, the value must contain at least one token outside this set, so
# decorated placeholders (`(none known)`, `-- none --`) fail without a
# fourth enumeration extension.
_PLACEHOLDER_LEXICON = frozenset((
    "none", "known", "na", "n", "a", "an", "the", "tbd", "tba", "todo",
    "to", "be", "determined", "announced", "pending", "not", "applicable",
    "unknown", "empty", "nil", "nothing", "see", "above", "below",
    "various", "several", "some", "many", "misc", "miscellaneous", "etc",
    "x", "yes", "no"))


def _names_nothing(val: str) -> bool:
    if val.startswith("<"):
        return True  # an unfilled template slot names nothing
    tokens = re.findall(r"[A-Za-z0-9]+", val.lower())
    # RD36-04: a leading negation is an emptiness claim, whatever nouns
    # follow — "no defects found", "none identified", "nothing of note"
    # name nothing. A semantic rule, not a fifth enumeration extension.
    if tokens and tokens[0] in ("no", "none", "nothing", "zero"):
        return True
    return all(t.isdigit() or t in _PLACEHOLDER_LEXICON for t in tokens)


# RD37-01: LG-13's emptiness is a POSITIVE test over a closed marker
# vocabulary, full-match — never the negation of a placeholder test, so
# widening `_names_nothing` can never loosen LG-13 again. RD38-02/07:
# the vocabulary is VALIDATOR POLICY beneath §5's `<empty | enumerated
# items>` slot — it is grounded in no instrument clause, it is published
# to the administrator in LG-13's own error message, and it covers the
# honest emptiness wordings RD-38 measured while still rejecting
# placeholders (`TBD`, `unknown`): E3 is the sharpest single gate, and
# its decisive field deserves a definite answer. Decoration (backticks,
# bold, underscores, surrounding parens/dashes, trailing punctuation) is
# stripped before matching; fullmatch keeps it structurally impossible
# for any enumeration to pass as a marker.
_E3_MARKERS = ("empty", "none", "none identified", "none known", "n/a",
               "na", "nil", "nothing", "zero", "0")
_E3_EMPTY_RE = re.compile(
    r"(?:" + "|".join(re.escape(m) for m in _E3_MARKERS) + r")$", re.I)


def _e3_is_empty(val: str) -> bool:
    plain = re.sub(r"^[\s`*_(\[{-]+|[\s`*_)\]}.;:,-]+$", "", val)
    return bool(_E3_EMPTY_RE.fullmatch(plain))


class _Field:
    """A parsed field value with a match-like interface (RD36-03)."""

    def __init__(self, value):
        self._value = value

    def group(self, _i=0):
        return self._value


def _active_text(txt: str) -> str:
    """RD38-01/RD39-02/RD39-06: a quotation is not the record. §5's
    template — including its G1 heading, every declared field label,
    and example verdict rows — is quoted inside the instrument in a
    fenced block, and a record may lawfully quote it the same way;
    RD-38 built a record that deleted G1 and six declared fields yet
    satisfied seven checks by quoting the template in a fenced
    appendix. Every scan therefore reads the record with fenced code
    blocks AND HTML comments removed — rows, declared fields, presence
    tokens, the G1 anchor, and the terminal verdict line alike: one
    rule at the source, for every consumer, rather than a per-check
    exemption. RD39-02 added HTML comments: a comment is invisible in
    rendered markdown, so bytes inside it are the one carrier a reader
    can never see — they are not the record. The fence grammar follows
    CommonMark where RD39-06 measured divergence: a fence marker
    counts only at <=3 spaces of indentation (deeper backticks are
    literal content of an indented code block, so the prose between
    them stays active), and a closing run must be the same character
    and at least as long as the opening run, alone on its line. An
    unterminated fence or comment blanks the rest of the record —
    loud on the roster when it swallows rows, and loud on LG-6 when
    it swallows or shadows the terminal verdict line, which is
    compared against the RAW bytes (RD39-01). Blockquotes are NOT
    stripped: §5's own non-authority banner is a blockquote; the
    presence checks refuse blockquote carriers by anchoring instead
    (RD39-02)."""
    return "\n".join(ln for _, ln in _active_lines(txt))


def _active_lines(txt: str):
    """Core of _active_text, keeping raw line indices: returns a list of
    (raw_index, line) for every line that survives fence and comment
    stripping (a comment-spliced line survives with the comment removed,
    same index). RD40-01/RD40-06: the terminal-verdict rule judges
    survival by RAW LINE INDEX, never by string equality, so an inline
    comment on the verdict line is not a false hiding. RD40-03: every
    indentation measurement expands tabs to CommonMark's 4-column stops
    first — a tab-indented backtick run is literal content of an
    indented code block, visible to the reader and therefore text to
    this validator; "CommonMark's own bound" is a column bound, not a
    space count."""
    out = []
    fence_char, fence_len = None, 0
    in_comment = False
    for idx, ln in enumerate(txt.splitlines()):
        if fence_char is not None:
            s = ln.expandtabs(4).lstrip(" ")
            indent = len(ln.expandtabs(4)) - len(s)
            mc = re.match(r"(`{3,}|~{3,})[^\S\n]*$", s)
            if (mc and indent <= 3 and mc.group(1)[0] == fence_char
                    and len(mc.group(1)) >= fence_len):
                fence_char, fence_len = None, 0
            continue
        if in_comment:
            if "-->" not in ln:
                continue
            ln = ln.split("-->", 1)[1]
            in_comment = False
        ln = re.sub(r"<!--.*?-->", "", ln)
        if "<!--" in ln:
            ln = ln[:ln.index("<!--")]
            in_comment = True
            if ln.strip():
                out.append((idx, ln))
            continue
        s = ln.expandtabs(4).lstrip(" ")
        indent = len(ln.expandtabs(4)) - len(s)
        mo = re.match(r"(`{3,}|~{3,})", s)
        if mo and indent <= 3:
            fence_char = mo.group(1)[0]
            fence_len = len(mo.group(1))
            continue
        out.append((idx, ln))
    return out


_LIST_MARK_RE = re.compile(r"(?:[-*+]|\d{1,9}[.)])(?:[^\S\n]|$)")
_SETEXT_RE = re.compile(r" {0,3}(?:=+|-{2,})[^\S\n]*$")
_BLOCK_START_RE = re.compile(
    r"(?:>|#{1,6}(?:[^\S\n]|$)|`{3,}|~{3,}"
    r"|(?:[-*+]|\d{1,9}[.)])(?:[^\S\n]|$))")
_UNI_WS_RE = re.compile("[\u00a0\u1680\u2000-\u200a\u202f\u205f\u3000]")


def _norm_uni_ws(s: str) -> str:
    """RD41-08 — a non-breaking space inside `GATE VERDICT:` renders
    identically for a human reader and matches no literal substring, so
    a record's visible terminal `NOT READY` became invisible to the
    validator and an earlier own `READY FOR` was reported in its place:
    0 errors, the wrong verdict in the trend row. Unicode whitespace is
    folded to ASCII spaces before the token is searched for and before
    the verdict is parsed. The instrument exists because a record's
    bytes and a reader's eyes can disagree; this is that disagreement
    in its purest form."""
    return _UNI_WS_RE.sub(" ", s)


def _own_flags(lines):
    """RD-41's prescription, adopted whole: **the predicate carries
    state.** "Is this line the record's own, not a quotation of it?" is
    not answerable from the line — a container is a REGION, not a line.
    `- `, `> `, `1. ` and four spaces each mark a block's FIRST line,
    and every one of them continues without its marker, so v1.13's
    line-local classifier refused the line that opened a list item and
    called its continuation lines the record's own. RD-38's composite
    reproduced whole through that door, a fifth time (RD41-01).

    This is CommonMark's block-structure phase, in the subset the
    instrument needs: for each line, the stack of containers open at
    it — blockquote at any depth, list item at its content column,
    raw-HTML block — maintained across lines, with **lazy
    continuation** (an unmarked paragraph line continuing a blockquote
    or list item belongs to that container, exactly as a reader sees
    it). A line is the record's OWN iff that stack is empty, its own
    indentation is at most 3 columns (tabs expanded to CommonMark's
    4-column stops), and no raw-HTML block is open. It is "bq1" iff the
    stack is exactly one blockquote — §5's non-authority banner IS a
    single-level blockquote, so the banner test consumes bq1 while a
    nested `> >` quotation of it fails (RD40-02).

    Two things deliberately left OUT of this predicate, each named
    where it now lives. **Setext headings** are not a containment
    question — a heading is the record's own visible text, not a
    quotation of it — so `_is_setext_text` is a separate declaration-
    form requirement consumed by the presence reads, the banner and
    LG-4, and NOT by the terminal-verdict rule, where v1.13's version
    made a `---` after the verdict hide the decisive line behind a
    message untrue of it (RD41-06). **Fences and HTML comments** are
    stripped upstream by `_active_lines`; this predicate is computed
    once, over the stripped lines, and the terminal rule maps back by
    raw index — so §9's "after the fence and HTML-comment strip" is
    true of every consumer, which at v1.13 it was not (RD41-06).

    `_decl` IS a consumer as of v1.14 (RD41-02): a declared value
    carried only on non-own lines is an absent field, never a supplied
    one. A `<details>` block reaches column 0, so at v1.13 it silently
    supplied `E3 reopen-list:`, `Deferred count:` and the owner's
    deferral citation — the instrument's sharpest single gate, answered
    from inside collapsed content a reader may never open."""
    flags = []
    stack = []
    html_depth = 0
    para_open = False
    for ln in lines:
        e = ln.expandtabs(4)
        if not e.strip():
            flags.append("no")
            para_open = False
            continue
        pos, matched = 0, 0
        for c in stack:
            rest = e[pos:]
            ind = len(rest) - len(rest.lstrip(" "))
            if c == "bq":
                if ind <= 3 and rest.lstrip(" ").startswith(">"):
                    pos += ind + 1
                    if pos < len(e) and e[pos] == " ":
                        pos += 1
                    matched += 1
                    continue
                break
            if ind >= c[1]:
                pos += c[1]
                matched += 1
                continue
            break
        rest = e[pos:]
        body = rest.lstrip(" ")
        # Lazy continuation applies to LIST ITEMS only, and the reason
        # is §5's own frozen template: it places the declared fields on
        # unmarked lines immediately beneath the blockquote banner, with
        # no blank line between them. Strict CommonMark laziness makes
        # those fields blockquote content — which would refuse every
        # lawful record, §5's template first. A blockquote therefore
        # ends at the first line not carrying its marker. The residual
        # this leaves is stated in §9 and measured: see _own_flags.
        lazy = (matched < len(stack) and para_open and body
                and "bq" not in stack[matched:]
                and len(rest) - len(body) < 4
                and not _BLOCK_START_RE.match(body))
        if not lazy:
            del stack[matched:]
            while True:
                ind = len(rest) - len(rest.lstrip(" "))
                s = rest.lstrip(" ")
                if ind > 3 or not s:
                    break
                if s.startswith(">"):
                    stack.append("bq")
                    rest = s[1:]
                    if rest.startswith(" "):
                        rest = rest[1:]
                    continue
                m = _LIST_MARK_RE.match(s)
                if m:
                    stack.append(("li", ind + len(m.group(0))))
                    rest = s[len(m.group(0)):]
                    continue
                break
        content = rest.lstrip(" ")
        cind = len(rest) - len(content)
        cls = "no"
        if html_depth == 0 and content and cind <= 3:
            if not stack:
                cls = "own"
            elif stack == ["bq"]:
                cls = "bq1"
        flags.append(cls)
        para_open = bool(content)
        html_depth += len(re.findall(
            r"<(?:details|summary)\b(?![^>]*/>)", content, re.I))
        html_depth -= len(re.findall(
            r"</(?:details|summary)>", content, re.I))
        html_depth = max(0, html_depth)
    return flags


def _takewhile_before_heading(lines):
    """The G1 section is what lies between its heading and the next one
    (RD41-04). The record's terminal verdict is never section content —
    a `## G1` placed immediately above `GATE VERDICT:` opens nothing."""
    out = []
    for ln in lines:
        if re.match(r" {0,3}#{1,6}(?:[^\S\n]|$)", ln.expandtabs(4)):
            break
        out.append(ln)
    return out


def _carriers(idxs, raw_lines, flag_by_raw, kept_idx):
    """RD41-06 — the LG-6 all-quoted message named five causes and could
    be emitted when none of them was true of the record. It now reports
    the carrier each verdict line actually sits in, computed from the
    same predicate that refused it, so an administrator reading the
    refusal learns where the validator thinks their verdict is."""
    seen = []
    for i in idxs:
        e = raw_lines[i].expandtabs(4)
        s = e.lstrip(" ")
        if i not in kept_idx:
            c = "inside a fence or an HTML comment"
        elif flag_by_raw.get(i) == "bq1" or s.startswith(">"):
            c = "blockquoted"
        elif _LIST_MARK_RE.match(s):
            c = "inside a list item"
        elif len(e) - len(s) >= 4:
            c = "indented as code"
        elif not re.match(r" {0,3}\**GATE VERDICT:", e):
            c = "mid-line, not at the start of its own line"
        else:
            c = "inside a container opened on an earlier line"
        if c not in seen:
            seen.append(c)
    return "; ".join(seen) if seen else "in a quotation"


def _is_setext_text(lines, i):
    """A declaration-form requirement, NOT a containment one (RD41-06).
    §5 declares its fields as `Label: value` lines; an ATX heading
    (`## Materials given:`) never satisfied a presence read, and a
    setext-underlined line renders as exactly the same heading, so the
    two are refused alike. Consumed by the presence reads, the banner
    and LG-4 — never by the terminal-verdict rule, where a `---` under
    the verdict is a heading a reader sees, not a quotation."""
    s = lines[i].expandtabs(4).lstrip(" ")
    return (bool(s) and not s.startswith("#") and not s.startswith("|")
            and i + 1 < len(lines)
            and bool(_SETEXT_RE.match(lines[i + 1].expandtabs(4))))


def _decl(pattern, txt, errors, check, label):
    """RD37-02/RD37-06 — the uniformity rule: EVERY declared field (§5
    labels and the label-shaped §2 integrity anchors alike) parses by
    collecting ALL occurrences; occurrences disagreeing in value are an
    error in both orders, and the last (declared) value is taken.
    RD36-03's repair applied this to four fields of fifteen; the three
    content fields driving LG-9, LG-12 and LG-13 stayed on first match,
    so a decoy above the declared line silently discarded the honest
    answer. A parsing rule repaired for some of its consumers was the
    chain's sixth class — it is repaired for all of them, and the
    selftest asserts the uniformity itself, not the instance."""
    vals = re.findall(pattern, txt, re.M)
    distinct = list(dict.fromkeys(map(_norm_ws, vals)))
    if len(distinct) > 1:
        errors.append(
            f"{check}: `{label}` appears more than once with disagreeing "
            "values (" + "; ".join(repr(v) for v in distinct) + ") — a "
            "narrative line must not shadow the declared field, and the "
            "honest answer must not be silently discarded (RD36-03, "
            "uniform per RD37-02)")
    # RD38-07: return the SAME normalization the disagreement compares on
    # — two occurrences declared "agreeing" must yield the value they
    # agree on, not a whitespace variant a downstream test then rejects.
    return _norm_ws(vals[-1]) if vals else None


def validate(record_path: Path, instrument_path: str, prior_path=None,
             _git=True):
    errors, notes = [], []
    _target_forms = None  # set when §8's LAUNCH_TARGET is readable (git on)
    # RD38-01: every check below reads the fence-stripped text — a fenced
    # quotation satisfies nothing and shadows nothing. The raw bytes are
    # kept for the terminal GATE VERDICT rule (RD39-01/RD40-01), and the
    # own-line predicate (_own_flags, RD40-02) is computed once here for
    # every consumer that asks "is this line the record's own?".
    _raw = record_path.read_text(encoding="utf-8")
    _act = _active_lines(_raw)
    _kept_idx = {i for i, _ in _act}
    _act_only = [ln for _, ln in _act]
    txt = "\n".join(_act_only)
    _act_flags = _own_flags(_act_only)
    _flag_by_raw = {ri: fl for (ri, _), fl in zip(_act, _act_flags)}
    # RD41-06: the declaration-form requirement is separate from the
    # containment one, and only the field-shaped consumers apply it.
    _decl_flags = ["no" if _is_setext_text(_act_only, k) else fl
                   for k, fl in enumerate(_act_flags)]
    # RD41-01, the limb §5's own frozen template makes structural: a
    # quotation whose fields land at column 0, unmarked, is byte-for-byte
    # §5's declaration form — §5 defines no marker that would tell a
    # quoted `Materials given:` from a declared one, and the template
    # itself puts the fields on unmarked lines directly beneath the
    # blockquote banner. What every such carrier DOES share is position:
    # it rides an appendix, after the record's conclusion. §5's template
    # places every declared field above `GATE VERDICT:`, and the verdict
    # is terminal. So a declaration is read only from the record's own
    # lines at or above its own terminal verdict line; an appendix below
    # it declares nothing, in any container.
    _raw_lines = [_norm_uni_ws(ln) for ln in _raw.splitlines()]
    _gv_all = [i for i, ln in enumerate(_raw_lines) if "GATE VERDICT:" in ln]
    _gv_own = [i for i in _gv_all
               if _flag_by_raw.get(i) == "own"
               and re.match(r" {0,3}\**GATE VERDICT:",
                            _raw_lines[i].expandtabs(4))]
    _decl_end = _gv_own[-1] if _gv_own else None
    _own_text = "\n".join(
        ln for (ri, ln), fl in zip(_act, _decl_flags)
        if fl == "own" and (_decl_end is None or ri <= _decl_end))

    # ---- LG-1 header ------------------------------------------------------
    # mdate/mcommit stay first-match deliberately, outside the _decl rule:
    # they are prose-shaped header patterns, not `Label:` fields — a lawful
    # record names other commits in evidence and narrative ("repaired at
    # commit `x`"), so a disagreement test over the prose shape would
    # reject lawful records. The header is the first occurrence by §5's
    # own construction. (RD37-06 scope decision, stated in the v1.10
    # delta.)
    mdate = re.search(r"administration\s+—\s+([0-9]{4}-[0-9]{2}-[0-9]{2})",
                      txt)
    mcommit = re.search(r"commit\s+`?([0-9a-f]{7,40})`?", txt)
    # RD36-02: every field value is anchored with [^\S\n]* — `\s*` crosses
    # the newline, so a field written with an EMPTY value silently borrowed
    # the next line's text as its answer. An empty field is absent.
    # RD37-02/RD37-06: every declared field parses through _decl — findall,
    # disagreement is an error in both orders, last value taken.
    # RD38-03: the three §2 anchor patterns carry RD36-02's anchoring like
    # every other declared field — `^`-anchored, `[^\S\n]*` never crossing
    # the newline — so an empty digest field is absent rather than
    # borrowing the next line, and a mid-line narrative mention ("I
    # checked whether Instrument version: v1.9 would be accepted") is
    # inert instead of becoming the value LG-2/LG-11 report on.
    _ver = _decl(r"^Instrument version:[^\S\n]*\**[^\S\n]*(v[\d.]+)", _own_text,
                 errors, "LG-1", "Instrument version:")
    mver = _Field(_ver) if _ver else None
    _instd = _decl(
        r"^Instrument version:[^\n]*sha256:[^\S\n]*`?([0-9a-f]{64})`?",
        _own_text, errors, "LG-1", "Instrument version: … sha256:")
    minstd = _Field(_instd) if _instd else None
    _paramd = _decl(r"^Parameter block sha256:[^\S\n]*`?([0-9a-f]{64})`?",
                    txt, errors, "LG-1", "Parameter block sha256:")
    mparamd = _Field(_paramd) if _paramd else None
    _lt = _decl(r"^Launch target:[^\S\n]*(\S.*)$", _own_text,
                errors, "LG-11", "Launch target:")
    mtarget = _Field(_lt) if _lt else None
    if not mdate:
        errors.append("LG-1: no administration date found")
    if not mcommit:
        errors.append("LG-1: no named commit found")
    elif _git and not commit_exists(mcommit.group(1)):
        errors.append(f"LG-1: named commit {mcommit.group(1)} does not exist"
                      " in this repository")
    if not mver:
        errors.append("LG-1: no instrument version recorded")
    if not minstd:
        errors.append("LG-1: no instrument sha256 recorded — a record "
                      "without the instrument digest cannot support a gate "
                      "decision (§2 integrity requirements)")
    if not mparamd:
        errors.append("LG-1: no parameter-block sha256 recorded")
    if not mtarget:
        errors.append("LG-11: no `Launch target:` line — the record must "
                      "name the launch target verbatim from the parameter "
                      "block (§5)")

    # ---- LG-2 / LG-11 digest, version, and target verification -----------
    if _git and mcommit and minstd:
        blob = git_show(mcommit.group(1), instrument_path)
        if blob is None:
            errors.append(
                f"LG-2: instrument `{instrument_path}` is not committed at "
                f"{mcommit.group(1)} — the §2 integrity requirement the "
                "pilot administration failed")
        else:
            actual = sha256_bytes(blob)
            if actual != minstd.group(1):
                errors.append(
                    f"LG-2: instrument digest mismatch — record quotes "
                    f"{minstd.group(1)[:12]}…, committed instrument is "
                    f"{actual[:12]}…")
            pb = param_block_bytes(blob)
            if mparamd:
                if pb is None:
                    errors.append("LG-2: committed instrument has no §8 "
                                  "parameter block to hash")
                elif sha256_bytes(pb) != mparamd.group(1):
                    errors.append(
                        f"LG-2: parameter-block digest mismatch — record "
                        f"quotes {mparamd.group(1)[:12]}…, §8 at the named "
                        f"commit hashes to {sha256_bytes(pb)[:12]}…")
            inst_ver_m = re.search(rb"^\s*effective_version:\s*(v[\d.]+)",
                                   blob, re.M)
            if mver and inst_ver_m:
                inst_ver = inst_ver_m.group(1).decode()
                if mver.group(1) != inst_ver:
                    errors.append(
                        f"LG-11: record claims instrument version "
                        f"{mver.group(1)} but the committed instrument at "
                        f"the named commit declares {inst_ver} — the "
                        "version a verdict names must be the version the "
                        "digest binds")
            if mtarget and pb is not None:
                pbt = pb.decode("utf-8", errors="replace")
                lt_m = re.search(
                    r"LAUNCH_TARGET:\s*>\n((?:[ \t]+\S[^\n]*\n)+)", pbt)
                lt = _norm_ws(lt_m.group(1)) if lt_m else _norm_ws(pbt)
                first_sentence = lt.split(". ")[0].rstrip(".")
                _target_forms = (lt.rstrip("."), first_sentence)
                tgt = _norm_ws(mtarget.group(1)).rstrip(".")
                # §5 requires the target verbatim: normalized equality with
                # the LAUNCH_TARGET scalar or its first sentence — a
                # fragment is not the target (RD34-08).
                if tgt and tgt not in (lt.rstrip("."), first_sentence):
                    errors.append(
                        f"LG-11: the record's launch target {tgt!r} is not "
                        "the parameter block's LAUNCH_TARGET (verbatim, "
                        "whitespace-normalized; its first sentence "
                        "suffices) — a fragment does not name the target "
                        "§8 binds (RD34-08)")
    elif not _git:
        notes.append("LG-2: git unavailable — digest, version, and target "
                     "verification skipped, record NOT fully validated")

    # ---- LG-3 / LG-4 verdict rows ----------------------------------------
    # This loop is the ONE row normalization for record and prior alike —
    # the prior side reaches it through D-5's recursive validate()
    # (RD33-02's one-normalization rule lives here; the former
    # _row_verdicts helper it named is deleted as dead code, RD40-07).
    verdicts = {}
    for line in txt.splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        q, v = m.group(1), m.group(2).strip()
        if q in ("Q",):
            continue
        if q == "G1":
            errors.append("LG-4: G1 appears as a verdict row — G1 yields no "
                          "Met/Not-met verdict; record it as a section "
                          "(instrument §3)")
            continue
        if not VERDICT_RE.match(v):
            errors.append(f"LG-3: question {q} carries verdict {v!r} — "
                          "outside the closed vocabulary (Met / Not met / "
                          "Not met (out of launch scope) / Unknown(reason))")
            continue
        if v == SCOPED and SECTION_OF(q) not in "ABCD":
            errors.append(f"LG-3: question {q} carries the scoped verdict — "
                          "lawful only in A–D (instrument §2)")
            continue
        if q in verdicts:
            errors.append(f"LG-3: question {q} appears twice")
        verdicts[q] = ("Unknown" if v.startswith("Unknown") else v)
    if not verdicts:
        errors.append("LG-5: no verdict rows parsed — nothing to compute")

    # ---- LG-4 G1 ----------------------------------------------------------
    # RD37-03: the heading must BE the G1 section's heading — G1 leads the
    # heading text. A substring test (`^#+ .*G1`) was satisfied by any
    # heading that merely mentioned G1, so a record with its
    # completeness-critic section deleted validated clean on the strength
    # of an incidental mention. RD40-02: the anchor consumes the shared
    # own-line predicate, so a heading quoted inside a <details> block,
    # a list item, or any other quotation carrier satisfies nothing.
    # RD41-04: two further doors, both measured open at v1.13. `\s*`
    # crossed the newline, so a bare `###` on one own line followed by
    # any own line beginning `G1 ` satisfied the anchor — RD37-03's own
    # class, returning through a door nobody checked. And the heading
    # alone satisfied LG-4 however EMPTY the section beneath it, which
    # the v1.13 records disclosed as opening no pass; it was in fact a
    # load-bearing limb of a 0-error pass. §4's clause is quoted in the
    # message: an administration missing G1 is incomplete. A heading
    # with nothing under it is a missing section, not a present one.
    _own_lines = _own_text.split("\n")
    _g1_at = next(
        (k for k, ln in enumerate(_own_lines)
         if re.match(r" {0,3}#{1,6}[^\S\n]*G1\b", ln.expandtabs(4))), None)
    if _g1_at is None:
        errors.append("LG-4: no G1 section — an administration missing G1 "
                      "is incomplete and cannot support a gate decision")
    elif not any(
            ln.strip()
            and not re.match(r" {0,3}#{1,6}(?:[^\S\n]|$)", ln.expandtabs(4))
            and not re.match(r" {0,3}\**GATE VERDICT:", ln.expandtabs(4))
            for ln in _takewhile_before_heading(_own_lines[_g1_at + 1:])):
        errors.append(
            "LG-4: the `G1` heading opens an EMPTY section — no content "
            "of the record's own follows it before the next heading. §4: "
            "\"an administration missing G1 is incomplete and cannot "
            "support a gate decision\"; a heading with nothing beneath it "
            "is a missing section, not a present one (RD41-04)")

    # ---- LG-10 roster -----------------------------------------------------
    if verdicts:
        missing_rows = [q for q in ROSTER if q not in verdicts]
        if missing_rows:
            errors.append(
                "LG-10: question rows missing: " + ", ".join(missing_rows) +
                " — a full administration answers every question; absence "
                "is never a pass, and a delta record cannot support a gate "
                "decision (instrument §2/§5)")
        unknown_rows = [q for q in verdicts if q not in ROSTER]
        if unknown_rows:
            errors.append(
                "LG-10: row ID(s) outside the question roster: "
                + ", ".join(sorted(unknown_rows)) +
                " — an invented question must not enter the trend row's "
                "computed columns (RD34-11)")

    # ---- LG-8 E1 sub-verdicts --------------------------------------------
    if "E1" in verdicts:
        missing_subs = [s for s in E1_SUBS if s not in verdicts]
        if missing_subs:
            errors.append("LG-8: E1 recorded without its five sub-verdict "
                          "rows — missing: " + ", ".join(missing_subs) +
                          " (instrument §3: five answers, not one)")
        elif verdicts["E1"] == "Met" and \
                any(verdicts[s] != "Met" for s in E1_SUBS):
            bad_subs = [s for s in E1_SUBS if verdicts[s] != "Met"]
            errors.append("LG-8: E1 rolls up Met over non-Met sub-verdicts: "
                          + ", ".join(bad_subs))

    # ---- LG-5 required count fields (parsed before LG-6 needs them) ------
    # The Deferred and Reopened figures are parsed from required explicit
    # fields, never derived from absence: a missing field is an error, not a
    # zero (VIS-2 — RD24-19 showed the prior build printed 0 from nothing).
    _dc = _decl(r"^Deferred count[^:\n]*:[^\S\n]*(\d+)", _own_text,
                errors, "LG-5", "Deferred count:")
    _rc = _decl(r"^Reopened count[^:\n]*:[^\S\n]*(\d+)", _own_text,
                errors, "LG-5", "Reopened count:")
    deferred_m = _Field(_dc) if _dc else None
    reopened_m = _Field(_rc) if _rc else None
    if not deferred_m:
        errors.append("LG-5: no `Deferred count:` field — the trend row's "
                      "Deferred figure has no source; absence is an error, "
                      "never zero")
    if not reopened_m:
        errors.append("LG-5: no `Reopened count:` field — a zero Reopened "
                      "claim needs a stated count, not a missing field")
    n_deferred_decl = int(deferred_m.group(1)) if deferred_m else None

    # ---- Owner deferral citation (used by LG-6/LG-7) ----------------------
    owner_dec = _decl(r"^Owner deferral decision:[^\S\n]*(\S.*)$", _own_text,
                      errors, "LG-7", "Owner deferral decision:")
    if owner_dec and (owner_dec.startswith("<")
                      or owner_dec.lower() in ("none", "n/a")):
        owner_dec = None
    if owner_dec:
        cite_err = _deferral_citation_error(
            owner_dec, mcommit.group(1) if mcommit else None, _git)
        if cite_err:
            errors.append("LG-7: `Owner deferral decision:` " + cite_err)
            owner_dec = None
    # §5: the citation is required whenever Deferred count is nonzero,
    # under ANY verdict (RD34-07) — an uncited deferral must not enter
    # the trend log.
    if n_deferred_decl and not owner_dec:
        errors.append(
            f"LG-7: `Deferred count:` is {n_deferred_decl} with no lawful "
            "`Owner deferral decision:` citation — only the owner defers, "
            "under any verdict (§5, RD34-07)")

    # ---- LG-9 scoped-row disclosure ---------------------------------------
    n_scoped = sum(1 for v in verdicts.values() if v == SCOPED)
    _find_val = _decl(
        r"^Deferred-wave findings recorded outside launch scope:"
        r"[^\S\n]*(\S.*)$",
        _own_text, errors, "LG-9",
        "Deferred-wave findings recorded outside launch scope:")
    if n_scoped:
        val = _find_val
        if val is None:
            errors.append(
                f"LG-9: {n_scoped} scoped row(s) but no deferred-wave "
                "findings line (or the line carries no value — an empty "
                "field is absent, RD36-02) — §4 requires each scoped "
                "defect named there; the disclosure is the scoped form's "
                "honesty")
        elif _names_nothing(val):
            errors.append(
                f"LG-9: {n_scoped} scoped row(s) beside a deferred-wave "
                f"findings line reading {val!r} — a placeholder names no "
                "defect; the record asserts a scoped defect exists and "
                "that none exists (instrument §4; RD34-06, lexicon rule "
                "RD35-05)")

    # ---- LG-6 / LG-7 gate verdict line ------------------------------------
    # §5's "terminal line" is the last line CONTAINING the literal token
    # `GATE VERDICT:` — not the last regex match (RD35-02: matching selected
    # a different, earlier line whenever the terminal verdict carried a
    # qualifier, so a terminal NOT READY was discarded for a pass line).
    # RD40-01: the rule is specified over the PROPERTY — "the record's own
    # verdict line" — via the shared own-line predicate on the RAW bytes:
    # a verdict line is a raw line that is own-shaped (≤3 columns, no
    # blockquote or list marker, tabs expanded) and starts with the token
    # (after optional bold). The terminal is the LAST such line. ANY other
    # token-carrying raw line after it — blockquoted, list-marked,
    # indented, fenced, comment-carried, or a mid-line prose mention — is
    # an ambiguity error, never silently resolved in either direction
    # (v1.12 compared raw text to stripped text, which distinguished only
    # the two carriers the strip removes; a verdict quoted in any carrier
    # the strip keeps silently became the terminal). An own-shaped
    # terminal that does not survive to active text (fenced or
    # comment-hidden) is the laundering error (RD39-01). Survival is
    # judged by raw line INDEX, so an inline comment on the verdict line
    # is not a false hiding (RD40-06); the line is parsed in its active
    # (comment-stripped) form. The parsed line must itself parse to the
    # closed verdict set; a captured verdict containing `|` is rejected —
    # it would structurally corrupt §6's nine-column trend row.
    _act_by_idx = dict(_act)
    mg = None
    n_not = sum(1 for v in verdicts.values() if v == "Not met")
    n_unk = sum(1 for v in verdicts.values() if v == "Unknown")
    if not _gv_all:
        errors.append("LG-6: no GATE VERDICT line found")
    elif not _gv_own:
        errors.append(
            "LG-6: every `GATE VERDICT:` line in the record sits "
            "inside a quotation container — " + _carriers(
                _gv_all, _raw_lines, _flag_by_raw, _kept_idx)
            + " — and a quoted verdict is not the record's verdict; "
            "§5's terminal line must be the record's own (RD35-02, "
            "RD40-01, RD41-06)")
    else:
        _t = _gv_own[-1]
        _later = [i for i in _gv_all if i > _t]
        if _later:
            errors.append(
                "LG-6: the record's terminal `GATE VERDICT:` line (raw "
                f"line {_t + 1}) is followed by {len(_later)} other "
                "line(s) carrying the token — a verdict quoted, fenced, "
                "commented, or mentioned after the record's own terminal "
                "verdict makes the terminal ambiguous, and is never "
                "silently resolved in either direction (RD35-02, "
                "RD39-01, RD40-01)")
        elif _t not in _kept_idx:
            errors.append(
                "LG-6: the record's terminal `GATE VERDICT:` line — "
                f"{_raw_lines[_t].strip()!r} — is not active text: it "
                "sits inside a fenced or comment-carried span, or after "
                "an unterminated fence. The verdict a reader sees must "
                "be the verdict the trend row reports (RD35-02, "
                "RD39-01)")
        else:
            mg = GATE_VERDICT_RE.search(
                _norm_uni_ws(_act_by_idx[_t]))
            if not mg:
                errors.append(
                    "LG-6: the terminal `GATE VERDICT:` line — "
                    f"{_act_by_idx[_t].strip()!r} — does not parse to "
                    "the closed verdict set (READY FOR <LAUNCH_TARGET> "
                    "/ NOT READY / READY-WITH-DEFERRALS); a qualified "
                    "or quoted verdict is not a verdict (§5's terminal "
                    "line; RD35-02)")
            elif "|" in mg.group(1):
                errors.append(
                    "LG-6: the terminal verdict contains '|' — it "
                    "would corrupt the nine-column trend row §6 "
                    "defines and F1 is answered from (RD35-02)")
                mg = None
    if mg:
        gv = mg.group(1).strip()
        if gv.startswith("READY"):
            # §4 (v1.7, RD34-01): both pass branches run the full conjunct
            # battery — the branches differ in exactly the F2 limb.
            e_rows = {q: v for q, v in verdicts.items()
                      if SECTION_OF(q) == "E"}
            ad_not = [q for q, v in verdicts.items()
                      if SECTION_OF(q) in "ABCD" and v == "Not met"]
            bad = []
            if not e_rows or any(v != "Met" for v in e_rows.values()):
                bad.append("an E question is not Met")
            if ad_not:
                bad.append(f"Not met in A–D: {', '.join(sorted(ad_not))}")
            for fq in ("F3", "F4"):
                if verdicts.get(fq) != "Met":
                    bad.append(f"{fq} is not Met")
            if verdicts.get("F1") == "Not met":
                bad.append("F1 is Not met — the §4 convergence conjunct "
                           "(F1 Met-or-Unknown) fails")
            if gv.startswith("READY FOR"):
                # RD35-03: the verdict line is the one string the trend log
                # carries — its target gets the same normalized-equality
                # test LG-11 applies to the header `Launch target:` line.
                # One placeholder, one enforcement standard.
                if _target_forms is not None:
                    vt = _norm_ws(gv[len("READY FOR"):]).rstrip(".")
                    if vt not in _target_forms:
                        errors.append(
                            f"LG-11: the verdict line claims READY FOR "
                            f"{vt!r} — not the parameter block's "
                            "LAUNCH_TARGET (verbatim, whitespace-"
                            "normalized; its first sentence suffices); "
                            "the one string the trend log carries must "
                            "name the target §8 binds (RD35-03)")
                if verdicts.get("F2") != "Met":
                    bad.append("F2 is not Met — a pass resting on an F2 "
                               "deferral is READY-WITH-DEFERRALS with an "
                               "owner citation, never plain READY FOR (§4)")
                if n_deferred_decl:
                    bad.append(f"Deferred count is {n_deferred_decl} — a "
                               "deferral-carrying pass is "
                               "READY-WITH-DEFERRALS, never plain READY "
                               "FOR (§4)")
                if bad:
                    errors.append("LG-6: verdict claims READY but the rows "
                                  "refuse it — " + "; ".join(bad))
            else:  # READY-WITH-DEFERRALS
                if not owner_dec:
                    errors.append(
                        "LG-7: READY-WITH-DEFERRALS without a lawful "
                        "`Owner deferral decision:` citation — only the "
                        "owner defers, and the template's own "
                        "'(owner only)' label satisfies nothing (§4/§5)")
                if n_deferred_decl == 0:
                    errors.append(
                        "LG-7: READY-WITH-DEFERRALS with `Deferred count: "
                        "0` — a deferral-carrying verdict must declare "
                        "its deferrals")
                if bad:
                    errors.append(
                        "LG-6: READY-WITH-DEFERRALS but a non-deferrable "
                        "conjunct fails — the E, A–D, F1, F3 and F4 "
                        "conjuncts are never deferrable (§4, RD34-01) — "
                        + "; ".join(bad))

    # ---- LG-12 §5 required record fields (RD35-07) ------------------------
    # A §5 template field deleted without an error reads as answered.
    # RD39-02/RD39-07/RD40-02: presence is a field read over the OWN
    # lines the shared predicate selects — one answer to the quotation
    # question for every consumer. The v1.12 anchor merged presence with
    # a lawful-decoration allowance, and the list-marker allowance it
    # granted is the canonical markdown quotation form, so a bullet-list
    # quotation of §5's template satisfied all six Label: checks
    # (RD40-02). At v1.13 the list marker is NOT lawful decoration for a
    # declared field: bold wrapping and internal whitespace variance
    # remain lawful; blockquotes, list items, deep indentation, setext
    # headings, <details> blocks, and mid-line prose are quotations.
    # Fences and HTML comments are already gone from the active text.
    # The non-authority banner is structural rather than label-shaped:
    # §5's banner IS a single-level blockquote, so its test consumes the
    # predicate's "bq1" class — a nested `> >` quotation fails it
    # (RD40-02's disclosed-limit exploit, closed).
    def _label_present(label):
        words = label.rstrip(":").split()
        pat = (r"^ {0,3}\**"
               + r"[^\S\n]+".join(re.escape(w) for w in words)
               + r"[^\S\n]*:[^\S\n]*(.*)$")
        return [m.group(1).strip()
                for m in re.finditer(pat, _own_text, re.M)]

    # RD41-01's last limb, and the honest form RD40-02 itself named. At
    # column 0, unmarked, above the verdict, a quotation of a §5 field
    # IS a declaration of it — §5 defines no marker that would tell the
    # two apart, so containment cannot answer this one. What a quotation
    # of the template carries that an answer never does is §5's own
    # PLACEHOLDER: `<model/version or human, fresh context: yes/no>`. A
    # field whose declared value is a bare angle-bracket placeholder has
    # not been answered, and saying so is a value-quality check, not a
    # quotation check — the two kept apart on purpose this time.
    _PLACEHOLDER_RE = re.compile(r"^\**<[^<>]*>\**$")
    for token, why in (
            ("Reviewer model family:",
             "the model-family disclosure F5 and §7 read"),
            ("Materials given:", "the §2 materials list"),
            ("Operationalization notes:",
             "the operationalization disclosure"),
            ("Unknowns and what would settle them:",
             "§4's Unknown-settling requirement"),
            ("Reviewer's falsification notes:",
             "the falsification discipline"),
            ("Reviewer:",
             "the fresh-context disclosure §2 requires — the eighth "
             "declared field, RD36-05"),
    ):
        _vals = _label_present(token)
        if not _vals:
            errors.append(f"LG-12: required §5 field missing — {token!r} "
                          f"({why}; RD35-07)")
        elif all(_PLACEHOLDER_RE.match(v) for v in _vals):
            errors.append(
                f"LG-12: the {token!r} field carries §5's own placeholder "
                f"({_vals[-1]!r}), not an answer ({why}; a quoted template "
                "declares nothing — RD41-01)")
    if not any(fl == "bq1"
               and "evidence, never an owner act" in _norm_ws(ln)
               for ln, fl in zip(_act_only, _act_flags)):
        errors.append("LG-12: required §5 field missing — 'evidence, "
                      "never an owner act' (the non-authority banner "
                      "(RD24-02) — a single-level blockquote line "
                      "carrying the phrase, §5's own form; prose, "
                      "nested-blockquote and other quotation carriers "
                      "satisfy nothing, RD39-02/RD40-02; RD35-07)")
    _unk_val = _decl(
        r"^Unknowns and what would settle them:[^\S\n]*(\S.*)$",
        _own_text, errors, "LG-12", "Unknowns and what would settle them:")
    if n_unk:
        if _unk_val is None:
            errors.append(
                f"LG-12: {n_unk} row(s) are Unknown but the Unknowns "
                "field carries no value (an empty field is absent, "
                "RD36-02) — §4 requires every Unknown to carry what "
                "evidence would settle it (RD35-07)")
        elif _names_nothing(_unk_val):
            errors.append(
                f"LG-12: {n_unk} row(s) are Unknown but the Unknowns "
                f"field reads {_unk_val!r} — §4 requires "
                "every Unknown to carry what evidence would settle it "
                "(RD35-07)")

    # ---- LG-13 E3 reopen-list cross-check (RD35-04) -----------------------
    # §3, E3: "the list is non-empty; 'ready' is then false regardless of
    # every other verdict" — the instrument's self-declared sharpest single
    # gate, enforced beside LG-8 and LG-9 as the same shape: a declared
    # field contradicting a verdict row.
    _e3_val = _decl(r"^E3 reopen-list:[^\S\n]*(\S.*)$", _own_text,
                    errors, "LG-13", "E3 reopen-list:")
    if _e3_val is None:
        errors.append("LG-12: no `E3 reopen-list:` field — §5 gives E3's "
                      "decisive answer a dedicated field; absence reads as "
                      "empty, and absence is never a pass (RD35-04)")
    elif not _e3_is_empty(_e3_val):
        # RD37-01: a POSITIVE emptiness test — a negation clause leading
        # an enumeration ("no items are resolved: (1) …") is a non-empty
        # reopen-list, never an emptiness claim.
        e3_val = _e3_val
        # RD38-07: the message publishes the vocabulary — the failure is
        # loud AND instructive — and says "carries", not "enumerates":
        # the value may be a wording this test cannot read as empty.
        _mk = " / ".join(_E3_MARKERS)
        if verdicts.get("E3") == "Met":
            errors.append(
                f"LG-13: `E3 reopen-list:` carries {e3_val!r} beside "
                "`E3 | Met` — a non-empty reopen-list is E3's own fail "
                "condition (§3; RD35-04). An empty list is written as "
                f"one of: {_mk} (validator marker vocabulary, RD37-01/"
                "RD38-07); anything else is read as enumerating items")
        if mg and mg.group(1).strip().startswith("READY"):
            errors.append(
                f"LG-13: `E3 reopen-list:` carries {e3_val!r} under a "
                "READY verdict — §3: \"'ready' is then false regardless "
                "of every other verdict\" (RD35-04). An empty list is "
                f"written as one of: {_mk} (validator marker vocabulary, "
                "RD37-01/RD38-07)")

    # ---- LG-5 trend row ---------------------------------------------------
    deferred = deferred_m.group(1) if deferred_m else "—"
    reopened = reopened_m.group(1) if reopened_m else "—"
    new_vs_prior = "n/a — no prior record supplied"
    if prior_path:
        # RD37-04/RD38-06/RD39-05: the prior is validated AS A RECORD,
        # at its OWN named commit — LG-1/LG-2/LG-11 already verify
        # against the commit a record itself names, so a prior lawfully
        # naming an older instrument version and older digests validates
        # cleanly, and a bare row block, a fabricated roster, or a
        # template-shaped fragment is refused whole. (RD-39 refuted the
        # v1.11 impossibility claim by exactly this construction: a
        # lawful v1.10-era record scored 0 errors under this validator
        # at its own named commit.) Recursion is depth 1: the prior's
        # own --prior is never followed. Honest cap, stated rather than
        # silent: a forged but fully lawful-shaped record naming a real
        # commit remains representable — this guard demands the full
        # lawful shape at the prior's own anchors, a raised bar, not an
        # impossibility claim.
        p_errors, _, prior_rows, _ = validate(Path(prior_path),
                                              instrument_path, None,
                                              _git=_git)
        if p_errors:
            errors.append(
                "LG-5: the --prior record fails validation as a record "
                f"at its own named commit ({len(p_errors)} error(s); "
                f"first: {p_errors[0]}) — an unvalidated prior must not "
                "suppress the New-findings column F1 is answered from "
                "(RD37-04, RD38-06, RD39-05)")
            new_vs_prior = "n/a — prior record failed validation"
        else:
            # §6 (v1.7, RD34-04): newly-Not-met rows count (incl. a
            # scoped row turning plain — it newly blocks; the r5 behavior
            # RD-34 verified), plus newly scoped rows that were no
            # finding before under either rendering — reclassification
            # never double-counts.
            prior_not = {q for q, v in prior_rows.items()
                         if v == "Not met"}
            prior_scoped = {q for q, v in prior_rows.items()
                            if v == SCOPED}
            cur_not = {q for q, v in verdicts.items() if v == "Not met"}
            cur_scoped = {q for q, v in verdicts.items() if v == SCOPED}
            new_set = (cur_not - prior_not) | (
                cur_scoped - (prior_scoped | prior_not))
            new_vs_prior = str(len(new_set))
    gate_word = mg.group(1).strip() if mg else "—"
    if n_scoped:
        notes.append(f"{n_scoped} scoped row(s) — `Not met (out of launch "
                     "scope)` — recorded as findings outside launch scope "
                     "in the trend row's Scoped column; they do not block "
                     "the §4 formula and are not in the Not-met column")
    trend = (f"| {mdate.group(1) if mdate else '—'} "
             f"| {mcommit.group(1)[:8] if mcommit else '—'} "
             f"| {n_not} | {n_scoped} | {n_unk} | {deferred} | {reopened} "
             f"| {new_vs_prior} | {gate_word} |")
    return errors, notes, verdicts, trend


def run(record, instrument, prior):
    errors, notes, verdicts, trend = validate(Path(record), instrument,
                                              prior)
    n = len(verdicts)
    print(f"rows parsed: {n} "
          f"(Met {sum(1 for v in verdicts.values() if v == 'Met')}, "
          f"Not met {sum(1 for v in verdicts.values() if v == 'Not met')}, "
          f"scoped {sum(1 for v in verdicts.values() if v == SCOPED)}, "
          f"Unknown {sum(1 for v in verdicts.values() if v == 'Unknown')})"
          " — row counts computed from the rows; Deferred/Reopened are "
          "declared required fields (instrument §5)")
    for x in notes:
        print("NOTE  " + x)
    print("trend row:")
    print(trend)
    if errors:
        for e in errors:
            print("ERROR " + e)
        print(f"{len(errors)} error(s) — this record cannot support a gate "
              "decision as stored")
        return 1
    print("record valid — verdict semantics remain the instrument's, "
          "not this tool's")
    return 0


# --------------------------------------------------------------- selftest

def _template_rows() -> str:
    qs = ([f"A{i}" for i in range(1, 7)] + [f"B{i}" for i in range(1, 6)]
          + [f"C{i}" for i in range(1, 8)] + [f"D{i}" for i in range(1, 5)]
          + list(E1_SUBS) + ["E1"] + [f"E{i}" for i in range(2, 7)]
          + [f"F{i}" for i in range(1, 7)])
    lines = []
    for q in qs:
        if q == "F1":
            lines.append("| F1 | Unknown (first administration) | x |")
        elif q == "F2":
            lines.append("| F2 | Not met | x |")
        else:
            lines.append(f"| {q} | Met | x |")
    return "\n".join(lines)


# A full §5-template-shaped record (RD33-08a: the reduced fixture guarded
# nothing about template↔parser coupling; this one breaks loudly if §5's
# field names and the parser ever drift apart again).
GOOD = """# Launch-gate administration — 2026-08-10, commit {sha}
> This administration record is evidence, never an owner act; its verdict
> authorizes nothing (instrument preamble; VIS-4).
Instrument version: v1.13  sha256: {inst}
Parameter block sha256: {param}
Launch target: Capability 1 — Project registration and honest shape visibility
Reviewer: human, fresh context: yes
Reviewer model family: human
Materials given: the fixed §2 list, no deviations
Operationalization notes: none

| Q | Verdict | Evidence |
|---|---------|----------|
""" + _template_rows() + """

## G1 — completeness critic
none proposed

E3 reopen-list: empty
Deferred-wave findings recorded outside launch scope: none
Deferred count (owner-deferred findings this administration): 0
Reopened count (previously recorded resolved, recurred): 0
Unknowns and what would settle them: F1 — a second formal administration
Reviewer's falsification notes: tried to break the roster; couldn't
GATE VERDICT: NOT READY
"""


def _head_commit():
    try:
        r = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                           capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    except OSError:
        return None


def selftest():
    import tempfile
    fails = []
    n_cases = [0]

    def case(name, text, expect_error_containing, _git=False):
        n_cases[0] += 1
        with tempfile.NamedTemporaryFile("w", suffix=".md",
                                         delete=False) as f:
            f.write(text)
            p = Path(f.name)
        errors, *_ = validate(p, INSTRUMENT_DEFAULT, None, _git=_git)
        p.unlink()
        joined = " || ".join(errors)
        if expect_error_containing is None:
            ok = not errors
        else:
            ok = expect_error_containing in joined
        print(("  pass  " if ok else "  FAIL  ") + name)
        if not ok:
            fails.append((name, joined))

    sha = "0" * 40
    inst = "1" * 64
    param = "2" * 64
    good = GOOD.format(sha=sha, inst=inst, param=param)

    case("well-formed full-template record validates (git checks off)",
         good, None)
    case("invalid verdict word rejected",
         good.replace("| A1 | Met |", "| A1 | Partially met |"),
         "outside the closed vocabulary")
    case("softened verdict rejected",
         good.replace("| E1 | Met |", "| E1 | Met with caveats |"),
         "outside the closed vocabulary")
    case("missing G1 rejected",
         good.replace("## G1 — completeness critic", "## notes"), "LG-4")
    case("missing instrument digest rejected",
         good.replace(f"sha256: {inst}", ""), "no instrument sha256")
    case("missing parameter digest rejected",
         good.replace(f"Parameter block sha256: {param}", ""),
         "no parameter-block sha256")
    case("missing launch-target line rejected (RD33-06)",
         good.replace("Launch target: Capability 1 — Project registration and honest shape visibility\n", ""),
         "no `Launch target:` line")
    case("missing gate verdict rejected",
         good.replace("GATE VERDICT: NOT READY", ""), "no GATE VERDICT")
    case("READY over a Not met E row rejected",
         good.replace("| E1 | Met |", "| E1 | Not met |")
             .replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1"),
         "rows refuse it")
    case("READY with F3 not Met rejected",
         good.replace("| F3 | Met |", "| F3 | Not met |")
             .replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1"),
         "F3 is not Met")
    case("duplicate question rejected",
         good.replace("| A1 | Met | x |", "| A1 | Met | x |\n| A1 | Met | x |"),
         "appears twice")
    case("no verdict rows rejected",
         re.sub(r"^\|.*\|$", "", good, flags=re.M),
         "no verdict rows parsed")

    # --- v1.5 fixtures: RD-24's mutation-proven defects, kept closed ------
    ready = (good.replace("| F2 | Not met | x |", "| F2 | Met | x |")
                 .replace("GATE VERDICT: NOT READY",
                          "GATE VERDICT: READY FOR Capability 1"))
    scoped_c2 = ready.replace(
        "| C2 | Met | x |", "| C2 | Not met (out of launch scope) | x |")
    case("scoped A-D row with disclosure does not block READY "
         "(RD24-05 T2, lawful form)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "RFC-0010 mission-profile drift (Wave D1)"),
         None)
    case("plain Not met in A-D still blocks READY (RD24-05 T1)",
         ready.replace("| A1 | Met | x |", "| A1 | Not met | x |"),
         "Not met in A–D")
    case("scoped verdict outside A-D rejected",
         good.replace("| E1-form | Met | x |",
                      "| E1-form | Not met (out of launch scope) | x |"),
         "lawful only in A–D")
    case("READY over a Not met F1 rejected (RD24-09 T3)",
         ready.replace("| F1 | Unknown (first administration) | x |",
                       "| F1 | Not met | x |"),
         "F1 is Not met")
    case("missing Deferred count field rejected (RD24-19)",
         good.replace(
             "Deferred count (owner-deferred findings this "
             "administration): 0\n", ""),
         "no `Deferred count:`")
    case("missing Reopened count field rejected (RD24-19)",
         good.replace(
             "Reopened count (previously recorded resolved, recurred): 0\n",
             ""),
         "no `Reopened count:`")
    case("G1 verdict row rejected (RD24-10)",
         good.replace("| A1 | Met | x |",
                      "| A1 | Met | x |\n| G1 | Met | x |"),
         "G1 appears as a verdict row")
    case("E1 without its five sub-rows rejected (RD24-21)",
         re.sub(r"^\| E1-[a-z-]+ \| Met \| x \|\n", "", good, flags=re.M),
         "LG-8")
    case("E1 Met over a Not met sub-row rejected (RD24-21)",
         good.replace("| E1-form | Met | x |", "| E1-form | Not met | x |"),
         "rolls up Met")

    # --- v1.6 fixtures: RD-33's findings, kept closed ---------------------
    case("scoped row beside findings line 'none' rejected (RD33-01, r2)",
         scoped_c2, "LG-9")
    case("READY FOR over unresolved F2 rejected even with owner-deferred "
         "wording in the evidence cell (RD33-04, r4)",
         good.replace("| F2 | Not met | x |",
                      "| F2 | Not met | treated as owner-deferred pending "
                      "a reduction plan |")
             .replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1"),
         "F2 is not Met")
    case("plain READY FOR over a nonzero Deferred count rejected (RD33-04)",
         ready.replace(
             "Deferred count (owner-deferred findings this "
             "administration): 0",
             "Deferred count (owner-deferred findings this "
             "administration): 1"),
         "deferral-carrying pass")
    with_def = (good.replace(
        "GATE VERDICT: NOT READY",
        "GATE VERDICT: READY-WITH-DEFERRALS (owner only)")
        .replace("Deferred count (owner-deferred findings this "
                 "administration): 0",
                 "Deferred count (owner-deferred findings this "
                 "administration): 1"))
    case("READY-WITH-DEFERRALS satisfied by the template's own '(owner "
         "only)' label rejected (RD33-03, r3)",
         with_def, "LG-7")
    case("READY-WITH-DEFERRALS with an owner-decision citation validates",
         with_def.replace(
             "Unknowns and what would settle them:",
             "Owner deferral decision: SDR-33\n"
             "Unknowns and what would settle them:"),
         None)
    case("label wording as citation rejected (RD34-02, H3)",
         with_def.replace(
             "Unknowns and what would settle them:",
             "Owner deferral decision: (owner only)\n"
             "Unknowns and what would settle them:"),
         "neither a repository path nor a decision identifier")
    case("all-Not-met record under READY-WITH-DEFERRALS rejected "
         "(RD34-01, H9d)",
         with_def.replace("| Met | x |", "| Not met | x |")
                 .replace("Unknowns and what would settle them:",
                          "Owner deferral decision: SDR-33\n"
                          "Unknowns and what would settle them:"),
         "non-deferrable conjunct fails")
    case("terminal GATE VERDICT line is the one parsed (RD34-03, H6)",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1")
             .replace("## G1 — completeness critic",
                      "Summary: GATE VERDICT: NOT READY\n\n"
                      "## G1 — completeness critic"),
         "F2 is not Met")
    case("nonzero Deferred count without citation rejected under any "
         "verdict (RD34-07, H4)",
         good.replace("Deferred count (owner-deferred findings this "
                      "administration): 0",
                      "Deferred count (owner-deferred findings this "
                      "administration): 3"),
         "only the owner defers, under any verdict")
    case("placeholder findings line rejected (RD34-06, H1)",
         (ready.replace("| C2 | Met | x |",
                        "| C2 | Not met (out of launch scope) | x |")
               .replace("Deferred-wave findings recorded outside launch "
                        "scope: none",
                        "Deferred-wave findings recorded outside launch "
                        "scope: TBD")),
         "placeholder")
    case("invented question ID rejected (RD34-11, H5)",
         good.replace("| A1 | Met | x |",
                      "| A1 | Met | x |\n| A9 | Met | x |"),
         "outside the question roster")
    case("READY-WITH-DEFERRALS with zero declared deferrals rejected",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY-WITH-DEFERRALS (owner only)")
             .replace("Unknowns and what would settle them:",
                      "Owner deferral decision: .syzygy/governance/"
                      "decisions/SDR-99-EXAMPLE.md\n"
                      "Unknowns and what would settle them:"),
         "must declare its deferrals")
    case("missing question row rejected (RD33-05, p2)",
         good.replace("| E5 | Met | x |\n", ""), "LG-10")
    case("omitted E1 rollup row rejected (RD33-10, p4)",
         good.replace("| E1 | Met | x |\n", ""), "LG-10")

    # --- v1.8 fixtures: RD-35's findings, kept closed ---------------------
    case("qualified terminal verdict rejected — the terminal line must "
         "parse, never be skipped for an earlier match (RD35-02)",
         good.replace("GATE VERDICT: NOT READY",
                      "Summary: GATE VERDICT: READY FOR Capability 1\n\n"
                      "GATE VERDICT: NOT READY — pending the owner's F2 "
                      "deferral decision"),
         "does not parse to the closed verdict set")
    case("quoted §5 template line as terminal GATE VERDICT rejected — "
         "'|' in a captured verdict corrupts the trend row (RD35-02)",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: NOT READY\n\n"
                      "Appendix, quoting §5's own template:\n"
                      "GATE VERDICT: READY FOR <LAUNCH_TARGET> | "
                      "NOT READY |"),
         "would corrupt the nine-column trend row")
    case("non-empty E3 reopen-list beside `E3 | Met` rejected (RD35-04)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: (1) whether a Mission is a "
                      "first-class object; (2) evidence adapters in "
                      "Wave A"),
         "E3's own fail condition")
    case("non-empty E3 reopen-list under a READY verdict rejected "
         "(RD35-04)",
         ready.replace("E3 reopen-list: empty",
                       "E3 reopen-list: the write-boundary scope"),
         "ready' is then false")
    case("deleted E3 reopen-list field rejected (RD35-04)",
         good.replace("E3 reopen-list: empty\n", ""),
         "no `E3 reopen-list:` field")
    case("decorated placeholder '(none known)' findings line rejected "
         "(RD35-05)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "(none known)"),
         "names no defect")
    case("decorated placeholder '-- none --' findings line rejected "
         "(RD35-05)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "-- none --"),
         "names no defect")
    case("VIS-2's own word 'unknown' as findings line rejected (RD35-05)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "unknown"),
         "names no defect")
    case("P-n (pending queue) as deferral citation rejected (RD35-06)",
         with_def.replace(
             "Unknowns and what would settle them:",
             "Owner deferral decision: P-34\n"
             "Unknowns and what would settle them:"),
         "pending-decision queue")
    case("D-n (delta item) as deferral citation rejected (RD35-06)",
         with_def.replace(
             "Unknowns and what would settle them:",
             "Owner deferral decision: D-10\n"
             "Unknowns and what would settle them:"),
         "pending-decision queue")
    case("B-n (review-finding numbering) as deferral citation rejected "
         "(RD36-01)",
         with_def.replace(
             "Unknowns and what would settle them:",
             "Owner deferral decision: B-1\n"
             "Unknowns and what would settle them:"),
         "review-finding numbering")
    case("deleted non-authority banner rejected (RD35-07)",
         good.replace(
             "> This administration record is evidence, never an owner "
             "act; its verdict\n> authorizes nothing (instrument "
             "preamble; VIS-4).\n", ""),
         "evidence, never an owner act")
    case("deleted `Reviewer model family:` field rejected (RD35-07)",
         good.replace("Reviewer model family: human\n", ""),
         "Reviewer model family:")
    case("deleted `Materials given:` field rejected (RD35-07)",
         good.replace("Materials given: the fixed §2 list, no "
                      "deviations\n", ""),
         "Materials given:")
    case("deleted `Operationalization notes:` field rejected (RD35-07)",
         good.replace("Operationalization notes: none\n", ""),
         "Operationalization notes:")
    case("deleted `Unknowns and what would settle them:` field rejected "
         "(RD35-07)",
         good.replace("Unknowns and what would settle them: F1 — a "
                      "second formal administration\n", ""),
         "Unknowns and what would settle them:")
    case("deleted `Reviewer's falsification notes:` field rejected "
         "(RD35-07)",
         good.replace("Reviewer's falsification notes: tried to break "
                      "the roster; couldn't\n", ""),
         "Reviewer's falsification notes:")
    case("Unknown rows beside a placeholder Unknowns field rejected "
         "(RD35-07)",
         good.replace("Unknowns and what would settle them: F1 — a "
                      "second formal administration",
                      "Unknowns and what would settle them: TBD"),
         "carry what evidence would settle it")

    # --- v1.9 fixtures: RD-36's findings, kept closed ---------------------
    # RD-36's fixture discipline, adopted: predicates fixtured in BOTH
    # directions; the empty and shadowed field cases fixtured, not only
    # the absent case.
    case("EMPTY findings line beside a scoped row rejected — an empty "
         "field is absent, never the next line's text (RD36-02)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope:"),
         "LG-9")
    case("EMPTY Unknowns field beside Unknown rows rejected (RD36-02)",
         good.replace("Unknowns and what would settle them: F1 — a "
                      "second formal administration",
                      "Unknowns and what would settle them:"),
         "carries no value")
    case("narrative line shadowing a declared Deferred count rejected "
         "(RD36-03)",
         good.replace("Deferred count (owner-deferred findings this "
                      "administration): 0",
                      "Deferred count summary for the reader: 0\n"
                      "Deferred count (owner-deferred findings this "
                      "administration): 3"),
         "disagreeing values")
    case("negation-phrased emptiness claim 'no defects found' as "
         "findings line rejected (RD36-04)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "no defects found"),
         "names no defect")
    case("negation-phrased emptiness claim 'none identified' as "
         "findings line rejected (RD36-04)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "none identified"),
         "names no defect")
    case("'E3 reopen-list: none identified' is a lawful empty marker — "
         "no false rejection beside E3 Met (RD36-04)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: none identified"),
         None)
    case("deleted `Reviewer:` fresh-context line rejected (RD36-05)",
         good.replace("Reviewer: human, fresh context: yes\n", ""),
         "Reviewer:")

    # --- v1.10 fixtures: RD-37's findings, kept closed --------------------
    # RD-37's uniformity rule, adopted: a predicate serves consumers of
    # one polarity only; a parsing repair reaches every field; the meta
    # check below asserts the uniformity itself.
    case("negation-led ENUMERATED reopen-list beside `E3 | Met` rejected "
         "— an emptiness claim must be an empty marker, not a negation "
         "prefix (RD37-01)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: no items are resolved: (1) whether "
                      "a Mission is a first-class object; (2) evidence "
                      "adapters in Wave A"),
         "E3's own fail condition")
    case("negation-led enumerated reopen-list under a READY verdict "
         "rejected (RD37-01)",
         ready.replace("E3 reopen-list: empty",
                       "E3 reopen-list: none of these are closed: the "
                       "write-boundary scope"),
         "ready' is then false")
    case("unfilled E3 template slot is not an emptiness claim — rejected "
         "beside `E3 | Met` (RD37-01, positive marker test)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: <empty | enumerated items>"),
         "E3's own fail condition")
    case("decoy E3 line above the declared field rejected — the honest "
         "enumeration must not be silently discarded (RD37-02)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: empty\n"
                      "E3 reopen-list: (1) whether a Mission is a "
                      "first-class object"),
         "disagreeing values")
    case("decoy Unknowns line shadowing the declared field rejected "
         "(RD37-02)",
         good.replace("Unknowns and what would settle them: F1 — a "
                      "second formal administration",
                      "Unknowns and what would settle them: F1 — a "
                      "second formal administration\n"
                      "Unknowns and what would settle them: TBD"),
         "disagreeing values")
    case("decoy findings line shadowing the declared field rejected "
         "(RD37-02)",
         scoped_c2.replace(
             "Deferred-wave findings recorded outside launch scope: none",
             "Deferred-wave findings recorded outside launch scope: "
             "RFC-0010 mission-profile drift (Wave D1)")
             .replace("Reviewer's falsification notes:",
                      "Deferred-wave findings recorded outside launch "
                      "scope: none\n"
                      "Reviewer's falsification notes:"),
         "disagreeing values")
    case("agreeing duplicate declared field is not a shadow — no false "
         "rejection (RD37-02)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: empty\n"
                      "E3 reopen-list: empty"),
         None)
    case("disagreeing duplicate `Parameter block sha256:` line rejected "
         "— the §2 integrity anchors obey the same rule (RD37-06)",
         good.replace("Reviewer's falsification notes:",
                      "Parameter block sha256: " + "3" * 64 + "\n"
                      "Reviewer's falsification notes:"),
         "disagreeing values")
    case("heading that merely MENTIONS G1 does not satisfy LG-4 — the "
         "completeness-critic section itself is required (RD37-03)",
         good.replace("## G1 — completeness critic",
                      "## Materials: we cite §3's G1 rule"),
         "LG-4")
    case("bare `### G1` heading satisfies LG-4 — the anchor rejects "
         "mentions, not lawful headings (RD37-03)",
         good.replace("## G1 — completeness critic", "### G1"),
         None)

    head = _head_commit()
    if head:
        # RD40-04: the RD34-05 shape-substitution guard, applied to
        # good_head exactly as to good_real — the template's version
        # literal is rewritten to the COMMITTED effective_version by
        # shape, and the disagreement fixture mutates by shape, so no
        # future version bump can strand this builder into a fixture
        # whose unmutated baseline already emits the asserted substring
        # (a check that cannot fail is not a check).
        _blob_v = git_show(head, INSTRUMENT_DEFAULT)
        _iv_v = (re.search(rb"^\s*effective_version:\s*(v[\d.]+)",
                           _blob_v, re.M) if _blob_v else None)
        good_head = GOOD.format(sha=head, inst=inst, param=param)
        if _iv_v:
            good_head = re.sub(r"Instrument version: v[\d.]+",
                               f"Instrument version: "
                               f"{_iv_v.group(1).decode()}",
                               good_head, count=1)
        # RD41-11: built from a REAL commit, so the mutation is what
        # makes the assertion true. The v1.13 form mutated `good`, whose
        # template sha is a `0`*40 placeholder that does not exist
        # either — the unmutated baseline already emitted the asserted
        # substring, the RD40-04 class with one instance left.
        case("nonexistent commit rejected (git on, LG-1)",
             good_head.replace(head, "f" * 40), "does not exist",
             _git=True)
        case("instrument digest mismatch rejected (git on, LG-2)",
             good_head, "digest mismatch", _git=True)
        case("instrument version disagreement rejected (RD33-06, LG-11)",
             re.sub(r"Instrument version: v[\d.]+",
                    "Instrument version: v0.2", good_head, count=1),
             "LG-11: record claims instrument version v0.2", _git=True)
        case("launch target outside the parameter block rejected "
             "(RD33-06, p5)",
             good_head.replace(
                 "Launch target: Capability 1 — Project registration and honest shape visibility",
                 "Launch target: Capability 7 — anything the reviewer "
                 "names"),
             "is not the parameter block's LAUNCH_TARGET", _git=True)
        case("fragment launch target rejected (RD34-08, H7)",
             good_head.replace(
                 "Launch target: Capability 1 — Project registration and honest shape visibility",
                 "Launch target: Capability 1"),
             "a fragment does not name the target", _git=True)
        case("nonexistent citation path rejected (RD34-02, git on)",
             good_head.replace(
                 "GATE VERDICT: NOT READY",
                 "GATE VERDICT: READY-WITH-DEFERRALS (owner only)")
                 .replace("Deferred count (owner-deferred findings this "
                          "administration): 0",
                          "Deferred count (owner-deferred findings this "
                          "administration): 1")
                 .replace("Unknowns and what would settle them:",
                          "Owner deferral decision: .syzygy/governance/"
                          "decisions/NO-SUCH-DECISION.md\n"
                          "Unknowns and what would settle them:"),
             "does not exist at the named commit", _git=True)
        # RD35-01: the passing direction, fixtured — every prior path
        # fixture asserted a rejection, so a check that rejected its
        # entire lawful input set read as green (rule 6's blind spot).
        # These use the REAL committed digests and version at HEAD, so
        # LG-1/LG-2/LG-11 and the citation-existence path all execute
        # and the record must validate CLEAN.
        blob_head = git_show(head, INSTRUMENT_DEFAULT)
        if blob_head is not None:
            _iv_m = re.search(rb"^\s*effective_version:\s*(v[\d.]+)",
                              blob_head, re.M)
            # Version-agnostic substitution (the RD34-05 lesson): the
            # template's version literal must never strand this builder
            # across a bump, so it is matched by shape, not by value.
            good_real = (re.sub(
                r"Instrument version: v[\d.]+",
                f"Instrument version: {_iv_m.group(1).decode()}",
                GOOD.format(
                    sha=head, inst=sha256_bytes(blob_head),
                    param=sha256_bytes(param_block_bytes(blob_head))),
                count=1)
                if _iv_m else None)
        else:
            good_real = None
        if good_real:
            case("existing repository path as deferral citation ACCEPTED "
                 "at the named commit (RD35-01)",
                 good_real.replace(
                     "GATE VERDICT: NOT READY",
                     "GATE VERDICT: READY-WITH-DEFERRALS (owner only)")
                     .replace("Deferred count (owner-deferred findings "
                              "this administration): 0",
                              "Deferred count (owner-deferred findings "
                              "this administration): 1")
                     .replace("Unknowns and what would settle them:",
                              "Owner deferral decision: .syzygy/"
                              "governance/decisions/"
                              "LAUNCH-GATE-AUTHORITY-DECISION.md\n"
                              "Unknowns and what would settle them:"),
                 None, _git=True)
            ready_real = (good_real
                          .replace("| F2 | Not met | x |",
                                   "| F2 | Met | x |")
                          .replace("GATE VERDICT: NOT READY",
                                   "GATE VERDICT: READY FOR Capability 1 "
                                   "— Project registration and honest "
                                   "shape visibility"))
            case("full-template READY FOR record with the verbatim "
                 "verdict-line target validates clean (git on, RD35-03)",
                 ready_real, None, _git=True)
            case("verdict line naming a target §8 never bound rejected "
                 "(RD35-03)",
                 ready_real.replace(
                     "GATE VERDICT: READY FOR Capability 1 — Project "
                     "registration and honest shape visibility",
                     "GATE VERDICT: READY FOR Capability 7 — full "
                     "Mission Control and mission prevention"),
                 "the verdict line claims READY FOR", _git=True)
            with_def_real = (good_real.replace(
                "GATE VERDICT: NOT READY",
                "GATE VERDICT: READY-WITH-DEFERRALS (owner only)")
                .replace("Deferred count (owner-deferred findings this "
                         "administration): 0",
                         "Deferred count (owner-deferred findings this "
                         "administration): 1"))
            case("existing SDR-n identifier as deferral citation "
                 "ACCEPTED at the named commit (RD36-06)",
                 with_def_real.replace(
                     "Unknowns and what would settle them:",
                     "Owner deferral decision: SDR-33\n"
                     "Unknowns and what would settle them:"),
                 None, _git=True)
            case("unminted SDR-n identifier rejected at the named commit "
                 "(RD36-06)",
                 with_def_real.replace(
                     "Unknowns and what would settle them:",
                     "Owner deferral decision: SDR-9999\n"
                     "Unknowns and what would settle them:"),
                 "names no decision in", _git=True)
            case("directory path as deferral citation rejected — a tree "
                 "is not a decision record (RD36-06)",
                 with_def_real.replace(
                     "Unknowns and what would settle them:",
                     "Owner deferral decision: .syzygy/governance/"
                     "decisions/\n"
                     "Unknowns and what would settle them:"),
                 "is a directory at the named commit", _git=True)
        else:
            print("  note  committed instrument unreadable at HEAD — 3 "
                  "RD35 git-dependent fixtures skipped")
    else:
        print("  note  git unavailable — 3 git-dependent fixtures skipped")

    # RD33-02: a prior scoped row that turns plain Not met must count as a
    # new finding — the prior/current comparison uses one normalization.
    n_cases[0] += 1
    import tempfile
    # RD39-05: the prior must now be a fully lawful record at its own
    # anchors, so the scoped prior names its scoped defect (LG-9).
    prior_txt = (good.replace(
        "| C2 | Met | x |", "| C2 | Not met (out of launch scope) | x |")
        .replace("Deferred-wave findings recorded outside launch scope: "
                 "none",
                 "Deferred-wave findings recorded outside launch scope: "
                 "RFC-0010 mission-profile drift (Wave D1)"))
    cur_txt = good.replace("| C2 | Met | x |", "| C2 | Not met | x |")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(prior_txt)
        pp = Path(f.name)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(cur_txt)
        cp = Path(f.name)
    _, _, _, trend = validate(cp, INSTRUMENT_DEFAULT, pp, _git=False)
    pp.unlink()
    cp.unlink()
    fields = [x.strip() for x in trend.strip().strip("|").split("|")]
    ok = fields[7] == "1"
    print(("  pass  " if ok else "  FAIL  ")
          + "prior scoped → current plain Not met counts as new "
          "(RD33-02, r5)")
    if not ok:
        fails.append(("prior scoped asymmetry", trend))

    # RD34-04: a brand-new scoped finding counts in New-findings.
    n_cases[0] += 1
    cur2_txt = (good.replace("| C2 | Met | x |",
                             "| C2 | Not met (out of launch scope) | x |")
                    .replace("Deferred-wave findings recorded outside "
                             "launch scope: none",
                             "Deferred-wave findings recorded outside "
                             "launch scope: RFC-0010 mission-profile "
                             "drift (Wave D1)"))
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(good)
        pp2 = Path(f.name)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(cur2_txt)
        cp2 = Path(f.name)
    _, _, _, trend2 = validate(cp2, INSTRUMENT_DEFAULT, pp2, _git=False)
    pp2.unlink()
    cp2.unlink()
    f2 = [x.strip() for x in trend2.strip().strip("|").split("|")]
    ok2 = f2[7] == "1"
    print(("  pass  " if ok2 else "  FAIL  ")
          + "brand-new scoped finding counts in New-findings (RD34-04)")
    if not ok2:
        fails.append(("new scoped not counted", trend2))

    # RD37-04: a non-record prior must be refused, loudly, and the trend
    # column must say so — an arbitrary file must not suppress the
    # New-findings column F1 is answered from.
    n_cases[0] += 1
    bogus_prior = ("| A1 | Not met | x |\n| B2 | Not met | x |\n"
                   "| G1 | Not met | x |\n")
    cur3_txt = good.replace("| A1 | Met | x |", "| A1 | Not met | x |")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(bogus_prior)
        pp3 = Path(f.name)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(cur3_txt)
        cp3 = Path(f.name)
    errs3, _, _, trend3 = validate(cp3, INSTRUMENT_DEFAULT, pp3, _git=False)
    pp3.unlink()
    cp3.unlink()
    f3 = [x.strip() for x in trend3.strip().strip("|").split("|")]
    ok3 = (any("RD37-04" in e for e in errs3)
           and f3[7] == "n/a — prior record failed validation")
    print(("  pass  " if ok3 else "  FAIL  ")
          + "non-record --prior refused; trend column says so (RD37-04)")
    if not ok3:
        fails.append(("bogus prior accepted", trend3 + " || "
                      + " || ".join(errs3)))

    # RD37-02's uniformity assertion, made BEHAVIORAL (RD38-04: the
    # v1.10 source-scan proxy was evadable by three trivial refactors,
    # one of them a literal re.search on a literal label with a long
    # comment pushing the pattern outside the scan window). This loop
    # drives a disagreeing decoy through EVERY declared label, in both
    # orders — a reversion of any one field to a first-match read is
    # caught by the behavior it actually changes, not by a syntactic
    # pattern. The loop IS the uniformity fixture: a new declared field
    # means a new row here, and the disagreement must fire in both
    # directions or the selftest fails.
    _decoys = (
        ("Launch target:",
         "Launch target: Capability 1 — Project registration and honest "
         "shape visibility",
         "Launch target: Capability 9 — a decoy target"),
        ("Instrument version:",
         f"Instrument version: v1.13  sha256: {inst}",
         f"Instrument version: v0.0  sha256: {inst}"),
        ("Instrument version: … sha256:",
         f"Instrument version: v1.13  sha256: {inst}",
         "Instrument version: v1.13  sha256: " + "9" * 64),
        ("Parameter block sha256:",
         f"Parameter block sha256: {param}",
         "Parameter block sha256: " + "8" * 64),
        ("Deferred count:",
         "Deferred count (owner-deferred findings this administration): 0",
         "Deferred count declared elsewhere in prose: 7"),
        ("Reopened count:",
         "Reopened count (previously recorded resolved, recurred): 0",
         "Reopened count stated in narrative: 5"),
        ("Owner deferral decision:", None,  # absent from GOOD: both
         "Owner deferral decision: SDR-33"),  # lines are inserted below
        ("Deferred-wave findings recorded outside launch scope:",
         "Deferred-wave findings recorded outside launch scope: none",
         "Deferred-wave findings recorded outside launch scope: "
         "RFC-0010 mission-profile drift (Wave D1)"),
        ("Unknowns and what would settle them:",
         "Unknowns and what would settle them: F1 — a second formal "
         "administration",
         "Unknowns and what would settle them: TBD"),
        ("E3 reopen-list:",
         "E3 reopen-list: empty",
         "E3 reopen-list: (1) a decoy reopen item"),
    )
    for _lbl, _real, _decoy in _decoys:
        if _real is None:
            # label absent from the template: insert two disagreeing
            # occurrences, in both orders
            case(f"inserted disagreeing pair for `{_lbl}` rejected, "
                 "order 1 (RD37-02/RD38-04 behavioral loop)",
                 good.replace(
                     "Unknowns and what would settle them:",
                     "Owner deferral decision: SDR-1\n" + _decoy
                     + "\nUnknowns and what would settle them:"),
                 "disagreeing values")
            case(f"inserted disagreeing pair for `{_lbl}` rejected, "
                 "order 2 (RD37-02/RD38-04 behavioral loop)",
                 good.replace(
                     "Unknowns and what would settle them:",
                     _decoy + "\nOwner deferral decision: SDR-1\n"
                     "Unknowns and what would settle them:"),
                 "disagreeing values")
            continue
        case(f"decoy ABOVE the declared `{_lbl}` rejected "
             "(RD37-02/RD38-04 behavioral loop)",
             good.replace(_real, _decoy + "\n" + _real),
             "disagreeing values")
        case(f"decoy BELOW the declared `{_lbl}` rejected "
             "(RD37-02/RD38-04 behavioral loop)",
             good.replace(_real, _real + "\n" + _decoy),
             "disagreeing values")

    # --- v1.11 fixtures: RD-38's findings, kept closed ---

    # RD38-01: a quotation is not the record. A fenced block satisfies
    # nothing (a deleted section cannot hide behind its quoted template)
    # and shadows nothing (a quoted example must not fire duplicate or
    # disagreement checks against the record quoting it).
    _fence_appendix = (
        "\n## Appendix — the §5 template, quoted for reference\n"
        "```\n"
        "Instrument version: v0.1  sha256: " + "9" * 64 + "\n"
        "Parameter block sha256: " + "8" * 64 + "\n"
        "E3 reopen-list: (1) a quoted example item\n"
        "| A1 | Not met | quoted example row |\n"
        "## G1 — completeness critic\n"
        "```\n")
    case("G1 section present only inside a fenced quotation rejects — "
         "a quotation satisfies nothing (RD38-01)",
         good.replace("## G1 — completeness critic\nnone proposed\n", "")
         + _fence_appendix,
         "LG-4")
    case("`Reviewer model family:` present only inside a fenced "
         "quotation rejects (RD38-01)",
         good.replace("Reviewer model family: human\n", "")
         + "\n```\nReviewer model family: human\n```\n",
         "Reviewer model family:")
    case("lawful record WITH a fenced template appendix still validates "
         "— a quotation shadows nothing (RD38-01)",
         good + _fence_appendix, None)
    case("fenced example table with a duplicate A1 row does not fire "
         "the duplicate check (RD38-01)",
         good + "\n```\n| A1 | Not met | quoted duplicate |\n```\n",
         None)

    # RD38-03: the §2 anchors carry the same anchoring as every other
    # declared field — an empty digest field is absent (never borrowing
    # the next line), and a mid-line narrative mention is inert.
    case("empty `Parameter block sha256:` with the digest on the next "
         "line is ABSENT, never borrowed (RD38-03)",
         good.replace(f"Parameter block sha256: {param}",
                      "Parameter block sha256:\n" + param),
         "no parameter-block sha256")
    case("mid-line narrative mention of an instrument version is inert "
         "(RD38-03)",
         good.replace(
             "Reviewer's falsification notes: tried to break the roster; "
             "couldn't",
             "Reviewer's falsification notes: tried to break the roster; "
             "couldn't; I checked whether Instrument version: v1.9 would "
             "be accepted"),
         None)

    # RD38-07 / RD37-01: the widened closed-marker vocabulary, and
    # decoration stripping — an honest empty marker in bold or with a
    # trailing period is still the marker.
    case("`E3 reopen-list: n/a` accepted as empty (RD38-07 vocabulary)",
         good.replace("E3 reopen-list: empty", "E3 reopen-list: n/a"),
         None)
    case("decorated `E3 reopen-list: **None.**` accepted as empty "
         "(RD38-07 decoration strip)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: **None.**"),
         None)

    # RD38-07's behavioral witness: the none-marker test on
    # `Owner deferral decision:` compares the RETURNED value exactly —
    # a trailing space must not turn the honest none marker into a
    # citation the validator then rejects. _decl returns the same
    # normalization the disagreement compares on.
    case("`Owner deferral decision: none ` (trailing space) is the none "
         "marker — the declared value is whitespace-normalized (RD38-07)",
         good.replace("Unknowns and what would settle them:",
                      "Owner deferral decision: none \n"
                      "Unknowns and what would settle them:"),
         None)

    # RD38-06/RD39-05: a roster-complete prior whose verdicts leave the
    # closed vocabulary, one carrying a duplicate row, and — RD39-05 — a
    # bare roster-complete row block with LAWFUL verdicts are all refused
    # the same way: the prior must be a fully lawful record at its own
    # named commit before it drives the New-findings column.
    for _nm, _bad_prior in (
            ("roster-complete prior with out-of-vocabulary verdicts "
             "refused (RD38-06)",
             "| Q | Verdict | Evidence |\n|---|---|---|\n"
             + _template_rows().replace("| Met |", "| Partially met |")),
            ("roster-complete prior with a duplicate row refused "
             "(RD38-06)",
             "| Q | Verdict | Evidence |\n|---|---|---|\n"
             + _template_rows() + "\n| A1 | Not met | x |"),
            ("bare roster-complete row block with lawful verdicts "
             "refused as a prior — the prior is validated as a record "
             "at its own named commit (RD39-05)",
             "| Q | Verdict | Evidence |\n|---|---|---|\n"
             + _template_rows())):
        n_cases[0] += 1
        with tempfile.NamedTemporaryFile("w", suffix=".md",
                                         delete=False) as f:
            f.write(_bad_prior)
            pp = Path(f.name)
        with tempfile.NamedTemporaryFile("w", suffix=".md",
                                         delete=False) as f:
            f.write(good)
            cp = Path(f.name)
        _e, _, _, _t = validate(cp, INSTRUMENT_DEFAULT, pp, _git=False)
        pp.unlink()
        cp.unlink()
        _f = [x.strip() for x in _t.strip().strip("|").split("|")]
        _ok = (any("RD39-05" in e for e in _e)
               and _f[7] == "n/a — prior record failed validation")
        print(("  pass  " if _ok else "  FAIL  ") + _nm)
        if not _ok:
            fails.append((_nm, _t + " || " + " || ".join(_e)))

    # --- v1.12 fixtures: RD-39's findings, kept closed ---

    # RD39-01: the terminal GATE VERDICT line is the last line carrying
    # the token in the RAW record bytes; if that line is not the active
    # terminal line, the record errors — a stored NOT READY can never be
    # reported as READY, and a verdict quoted after the terminal one is
    # ambiguous, never silently resolved upward.
    case("terminal NOT READY laundered behind an unterminated fence "
         "rejected — the raw terminal line rules (RD39-01)",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1 — Project "
                      "registration and honest shape visibility\n```\n"
                      "GATE VERDICT: NOT READY"),
         "RD39-01")
    case("a quoted verdict line AFTER the record's terminal verdict "
         "rejected as ambiguous (RD39-01)",
         good + "\n```\nGATE VERDICT: READY FOR OPENSPEC AUTHORING\n"
         "```\n",
         "RD39-01")
    case("terminal NOT READY between four-space-indented backticks is "
         "ordinary prose and parses correctly (RD39-01/RD39-06)",
         good.replace("GATE VERDICT: NOT READY",
                      "    ```\nGATE VERDICT: NOT READY\n    ```"),
         None)

    # RD39-06: CommonMark fence grammar — a closing run must be at
    # least as long as the opening run, so a 4-backtick fence is not
    # closed by 3 and its quoted content stays stripped.
    case("four-backtick fence not closed by three — quoted duplicate "
         "row stays stripped (RD39-06)",
         good + "\n````\n```\n| A1 | Not met | x |\n````\n",
         None)

    # RD39-02: an HTML comment is not the record — the invisible
    # carrier is stripped at the source, on every surface.
    case("`Reviewer model family:` present only inside an HTML comment "
         "rejects (RD39-02)",
         good.replace("Reviewer model family: human\n", "")
         + "\n<!--\nReviewer model family: human\n-->\n",
         "Reviewer model family:")
    case("G1 heading present only inside an HTML comment rejects "
         "(RD39-02)",
         good.replace("## G1 — completeness critic\nnone proposed\n", "")
         + "\n<!--\n## G1 — completeness critic\n-->\n",
         "LG-4")
    case("lawful record with an inline HTML comment still validates "
         "(RD39-02)",
         good.replace("Operationalization notes: none",
                      "Operationalization notes: none "
                      "<!-- reviewed inline -->"),
         None)

    # RD39-02: presence is a line-anchored field read — blockquote,
    # deep-indent and mid-line prose carriers of a label are quotations
    # of the label, not the field; the banner's test is structural.
    case("blockquoted `> Materials given:` does not satisfy presence "
         "(RD39-02)",
         good.replace("Materials given: the fixed §2 list, "
                      "no deviations\n", "")
         + "\n> Materials given: the fixed §2 list, no deviations\n",
         "Materials given:")
    case("four-space-indented label line does not satisfy presence "
         "(RD39-02)",
         good.replace("Operationalization notes: none\n", "")
         + "\n    Operationalization notes: none\n",
         "Operationalization notes:")
    case("mid-line prose mention of `Reviewer:` does not satisfy "
         "presence (RD39-02)",
         good.replace("Reviewer: human, fresh context: yes\n", "")
         + "\nThe administration was run by Reviewer: human with fresh "
         "context.\n",
         "fresh-context disclosure")
    case("prose restatement of the non-authority banner does not "
         "satisfy the structural blockquote test (RD39-02)",
         good.replace("> This administration record is evidence, never "
                      "an owner act; its verdict\n> authorizes nothing "
                      "(instrument preamble; VIS-4).\n",
                      "This record is evidence, never an owner act; its "
                      "verdict authorizes nothing.\n"),
         "non-authority banner")

    # RD39-07: presence reads normalize whitespace and accept lawful
    # decoration — a present field is never reported missing.
    case("bold-wrapped `**Materials given:**` satisfies presence "
         "(RD39-07)",
         good.replace("Materials given: the fixed §2 list, no deviations",
                      "**Materials given:** the fixed §2 list, "
                      "no deviations"),
         None)
    case("`Reviewer  model family:` (two internal spaces) satisfies "
         "presence (RD39-07)",
         good.replace("Reviewer model family: human",
                      "Reviewer  model family: human"),
         None)
    # RD40-02 REVERSED the v1.12 acceptance here: the list marker is the
    # canonical markdown quotation form, so it is not lawful decoration
    # for a declared field — a list-marked label is a quotation of the
    # label. Recorded on the v1.13 delta's directionality axes.
    case("list-marked `- Operationalization notes:` is a quotation and "
         "does NOT satisfy presence (RD40-02, reversing the v1.12 "
         "acceptance)",
         good.replace("Operationalization notes: none",
                      "- Operationalization notes: none"),
         "Operationalization notes:")

    # RD39-03: the internal-whitespace case — the behavioral change the
    # v1.11 normalization repair actually made — carries its fixture,
    # so reverting `_decl`'s return to the exact v1.10 `.strip()` bytes
    # fails here (rule 6 against the code the repair replaced).
    case("`E3 reopen-list: none  identified` (internal double space) "
         "accepted as the marker (RD39-03)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: none  identified"),
         None)

    # --- v1.13 fixtures: RD-40's findings, kept closed ---

    # RD40-01: the terminal verdict is the record's own last verdict
    # line, judged by the shared own-line predicate over the RAW bytes;
    # any other token-carrying line after it is an ambiguity error, in
    # EVERY carrier — not only the two the strip removes.
    for _cname, _carrier in (
            ("blockquote", "> GATE VERDICT: READY FOR OPENSPEC "
             "AUTHORING"),
            ("indented code block", "    GATE VERDICT: READY FOR "
             "OPENSPEC AUTHORING"),
            ("list item", "- GATE VERDICT: READY FOR OPENSPEC "
             "AUTHORING"),
            ("running prose", "For reference, the template's terminal "
             "line reads GATE VERDICT: READY FOR OPENSPEC AUTHORING "
             "in full.")):
        case(f"verdict line quoted after the terminal in a {_cname} "
             "rejected as ambiguous (RD40-01)",
             good + "\n" + _carrier + "\n",
             "RD40-01")
    case("record whose ONLY verdict line is blockquoted has no verdict "
         "— a quoted verdict is not the record's verdict (RD40-01)",
         good.replace("GATE VERDICT: NOT READY",
                      "> GATE VERDICT: NOT READY"),
         "a quoted verdict is not the record's verdict")
    case("inline HTML comment on the terminal verdict line is lawful — "
         "survival is judged by raw line index (RD40-06)",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: NOT READY <!-- final -->"),
         None)

    # RD40-03: tabs expand to CommonMark's 4-column stops before every
    # indentation measurement — a tab-indented backtick run is literal
    # content, so the honest line between the backticks stays text.
    case("terminal NOT READY between TAB-indented backticks is ordinary "
         "prose and parses correctly (RD40-03)",
         good.replace("GATE VERDICT: NOT READY",
                      "\t```\nGATE VERDICT: NOT READY\n\t```"),
         None)

    # RD40-02: the own-line predicate's container matrix — each
    # quotation carrier of a declared field or the G1 heading satisfies
    # nothing.
    case("bullet-list quotation of `Materials given:` does not satisfy "
         "presence (RD40-02)",
         good.replace("Materials given: the fixed §2 list, "
                      "no deviations\n", "")
             .replace("GATE VERDICT:",
                      "- Materials given: the fixed §2 list, no "
                      "deviations\n\nGATE VERDICT:"),
         "Materials given:")
    case("setext-heading text `Reviewer's falsification notes:` does "
         "not satisfy presence (RD40-02)",
         good.replace("Reviewer's falsification notes: tried to break "
                      "the roster; couldn't\n", "")
             .replace("GATE VERDICT:",
                      "Reviewer's falsification notes: quoted as a "
                      "heading\n---\n\nGATE VERDICT:"),
         "Reviewer's falsification notes:")
    case("`<details>`-wrapped `Reviewer model family:` does not "
         "satisfy presence (RD40-02)",
         good.replace("Reviewer model family: human\n", "")
             .replace("GATE VERDICT:",
                      "<details>\nReviewer model family: human\n"
                      "</details>\n\nGATE VERDICT:"),
         "Reviewer model family:")
    case("nested-blockquote `> >` banner quotation does not satisfy "
         "the structural banner test (RD40-02)",
         good.replace("> This administration record is evidence, never "
                      "an owner act; its verdict\n> authorizes nothing "
                      "(instrument preamble; VIS-4).\n",
                      "> > This administration record is evidence, "
                      "never an owner act; its verdict\n> > authorizes "
                      "nothing (instrument preamble; VIS-4).\n"),
         "non-authority banner")
    case("`<details>`-wrapped `## G1` heading does not satisfy LG-4 "
         "(RD40-02)",
         good.replace("## G1 — completeness critic\nnone proposed\n", "")
             .replace("GATE VERDICT:",
                      "<details>\n## G1 — completeness critic\nnone "
                      "proposed\n</details>\n\nGATE VERDICT:"),
         "LG-4")

    # RD40-05: the fence-close rule's REJECTION limb, previously
    # unfixtured — a label between a four-backtick and a three-backtick
    # run is stripped (the short run does not close), so its deletion
    # errors.
    case("label between a 4-backtick open and 3-backtick non-close is "
         "stripped — presence errors (RD40-05, D-4's rejection limb)",
         good.replace("Materials given: the fixed §2 list, "
                      "no deviations\n", "")
         + "\n````\n```\nMaterials given: the fixed §2 list, "
         "no deviations\n````\n",
         "Materials given:")

    # ---- v1.14: the predicate carries state (RD-41) ----------------------
    # RD41-01: a container is a REGION, not a line. Each of these rides a
    # continuation line — the line the v1.13 line-local classifier called
    # the record's own because it carried no marker of its own.
    _tmpl = ("Reviewer: <model/version or human, fresh context: yes/no>\n"
             "Reviewer model family: <alternate families>\n"
             "Materials given: <list, with deviations called out>\n"
             "Operationalization notes: <every judgment call made>\n"
             "Reviewer's falsification notes: <what they tried>\n")
    _real_tmpl = ("Reviewer: human, fresh context: yes\n"
                  "Reviewer model family: human\n"
                  "Materials given: the fixed §2 list, no deviations\n"
                  "Operationalization notes: none\n"
                  "Reviewer's falsification notes: tried the roster\n")
    _stripped = good
    for _f in ("Reviewer: human, fresh context: yes\n",
               "Reviewer model family: human\n",
               "Materials given: the fixed §2 list, no deviations\n",
               "Operationalization notes: none\n",
               "Reviewer's falsification notes: tried to break the "
               "roster; couldn't\n"):
        _stripped = _stripped.replace(_f, "")
    # Each of these places its quotation ABOVE the record's own terminal
    # verdict, so the repair under test is the containment one and not
    # the terminal-line restriction that also guards this shape.
    case("list-item CONTINUATION lines are inside the list item, not the "
         "record's own — indented continuation (RD41-01)",
         _stripped.replace(
             "GATE VERDICT:",
             "- Quoting §5's template:\n  "
             + _tmpl.replace("\n", "\n  ").rstrip()
             + "\n\nGATE VERDICT:"),
         "required §5 field missing — 'Reviewer:'")
    case("LAZY continuation of a list item — unmarked, unindented lines "
         "continuing the item — is inside it (RD41-01)",
         _stripped.replace(
             "GATE VERDICT:",
             "- Quoting §5's template:\n" + _real_tmpl + "\nGATE VERDICT:"),
         "required §5 field missing — 'Reviewer:'")
    # The disclosed limit §5's own frozen template forces (RD41-01):
    # a blockquote ENDS at the first line not carrying its marker,
    # because §5 puts the declared fields on unmarked lines directly
    # beneath the blockquote banner. So unmarked lines under any
    # blockquote are the record's own — including under `> Quoting §5`.
    # Fixtured in the ACCEPTING direction, so the limit is a measured
    # behaviour of this validator rather than a sentence about it; the
    # exploit it would otherwise carry is closed by the placeholder
    # check and by the terminal-line restriction, each fixtured above.
    case("unmarked lines under a blockquote are the record's own — §5's "
         "template form, fixtured as the limit it is (RD41-01)",
         _stripped.replace(
             "GATE VERDICT:",
             "> Quoting §5's template:\n" + _real_tmpl + "\nGATE VERDICT:"),
         None)
    case("a `> ` banner quoted inside a list item does not satisfy the "
         "banner test (RD41-01)",
         good.replace("> This administration record is evidence, never "
                      "an owner act; its verdict\n> authorizes nothing "
                      "(instrument preamble; VIS-4).\n",
                      "- quoting the preamble:\n  > This administration "
                      "record is evidence, never an owner act; its "
                      "verdict authorizes nothing (instrument preamble; "
                      "VIS-4).\n"),
         "non-authority banner")
    case("§5's own placeholder is not an answer — a template quoted at "
         "column 0 above the verdict declares nothing (RD41-01)",
         _stripped.replace("GATE VERDICT:", _tmpl + "\nGATE VERDICT:"),
         "carries §5's own placeholder")
    _real = ("Reviewer: human, fresh context: yes\n"
             "Reviewer model family: human\n"
             "Materials given: the fixed §2 list, no deviations\n"
             "Operationalization notes: none\n"
             "Reviewer's falsification notes: tried the roster\n")
    case("a field declared BELOW the record's own terminal verdict "
         "declares nothing — the verdict is terminal (RD41-01)",
         _stripped.rstrip("\n") + "\n\n" + _real,
         "required §5 field missing — 'Reviewer:'")
    case("a lawful record whose value merely contains angle brackets is "
         "not a placeholder (RD41-01, the accepting direction)",
         good.replace("Materials given: the fixed §2 list, no deviations",
                      "Materials given: the fixed §2 list <plus the "
                      "parameter block>, no deviations"),
         None)

    # RD41-02: _decl consumes the predicate — a value carried only on
    # non-own lines is an ABSENT field, never a supplied one.
    for _lbl, _line, _want in (
            ("E3 reopen-list", "E3 reopen-list: empty",
             "no `E3 reopen-list:` field"),
            ("Deferred count",
             "Deferred count (owner-deferred findings this "
             "administration): 0", "no `Deferred count:` field")):
        _base = "\n".join(l for l in good.split("\n")
                           if not l.startswith(_lbl))
        case(f"`{_lbl}:` carried only inside a `<details>` block is an "
             "absent field, not a supplied value (RD41-02)",
             _base.replace("GATE VERDICT:",
                           f"<details>\n{_line}\n</details>\n\n"
                           "GATE VERDICT:"), _want)
        case(f"`{_lbl}:` carried only as setext-heading text is an "
             "absent field (RD41-02)",
             _base.replace("GATE VERDICT:",
                           f"{_line}\n---\n\nGATE VERDICT:"), _want)
    case("an `Owner deferral decision:` citation carried only inside a "
         "`<details>` block does not license a deferral (RD41-02)",
         good.replace("Deferred count (owner-deferred findings this "
                      "administration): 0",
                      "Deferred count (owner-deferred findings this "
                      "administration): 3")
             .replace("GATE VERDICT:",
                      "<details>\nOwner deferral decision: SDR-33\n"
                      "</details>\n\nGATE VERDICT:"),
         "no lawful `Owner deferral decision:` citation")

    # RD41-04: LG-4's two doors — the anchor crossing a newline, and a
    # heading that opens nothing.
    case("a bare `###` followed by a line beginning `G1 ` does not "
         "satisfy LG-4 — the anchor never crosses a newline (RD41-04)",
         good.replace("## G1 — completeness critic\nnone proposed\n", "")
             .replace("GATE VERDICT:",
                      "###\nG1 was considered elsewhere.\n\nGATE VERDICT:"),
         "no G1 section")
    case("a `## G1` heading opening an EMPTY section does not satisfy "
         "LG-4 — the terminal verdict is not section content (RD41-04)",
         good.replace("## G1 — completeness critic\nnone proposed\n", "")
             .replace("GATE VERDICT:",
                      "## G1 — completeness critic\n\nGATE VERDICT:"),
         "opens an EMPTY section")

    # RD41-06: the raw-side predicate ran on un-stripped text, so these
    # five lawful records were refused — four of them with a message
    # naming five causes, none of which was true of the record.
    case("a fenced `<details>` example does not hide the verdict "
         "(RD41-06)",
         good + "\n```html\n<details>\n<summary>x</summary>\n```\n",
         None)
    case("a self-closing `<details/>` mentioned in prose is inert "
         "(RD41-06)",
         good + "\nA <details/> element was considered.\n", None)
    case("an HTML comment mentioning `<details>` is inert (RD41-06)",
         good + "\n<!-- see <details> below -->\n", None)
    case("a `---` on the line after the terminal verdict is a heading a "
         "reader sees, not a quotation (RD41-06)",
         good + "---\n", None)

    # RD41-08: unicode whitespace inside the token.
    # Witnessed behaviorally, not by an error string: `good` carries
    # `F2 | Not met`, which refuses READY. If the NBSP line is invisible
    # the validator reads the earlier READY and the §4 conjunct fires;
    # reading the record's visible terminal NOT READY, nothing fires.
    case("a non-breaking space inside `GATE VERDICT:` does not hide the "
         "record's visible terminal verdict (RD41-08)",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1 — Project "
                      "registration and honest shape visibility\n\n"
                      "GATE\u00a0VERDICT: NOT READY"),
         None)

    # RD41-10: the predicate clauses that had no single-layer witness.
    case("a TAB-indented `Materials given:` is indented code, not a "
         "declaration (RD41-10, the predicate's tab limb)",
         good.replace("Materials given: the fixed §2 list, no deviations",
                      "\tMaterials given: the fixed §2 list, no deviations"),
         "Materials given:")
    case("a TAB-indented banner is indented code, not §5's banner "
         "(RD41-10 — a defence-in-depth guard, not a single-layer "
         "witness: see the v1.14 delta's disclosure)",
         good.replace("> This administration record is evidence",
                      "\t> This administration record is evidence"),
         "non-authority banner")
    case("a 4-space-indented banner is indented code, not §5's banner "
         "(RD41-10 — a defence-in-depth guard, not a single-layer "
         "witness: see the v1.14 delta's disclosure)",
         good.replace("> This administration record is evidence",
                      "    > This administration record is evidence"),
         "non-authority banner")
    case("a 4-column-indented `## G1` heading does not satisfy LG-4 "
         "(RD41-10, the predicate's indent limb)",
         good.replace("## G1 — completeness critic",
                      "    ## G1 — completeness critic"),
         "no G1 section")

    print(f"{n_cases[0]} fixtures, {len(fails)} failing — a check that "
          "cannot fail is not a check")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record", nargs="?")
    ap.add_argument("--instrument", default=INSTRUMENT_DEFAULT)
    ap.add_argument("--prior")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest())
    if not args.record:
        ap.error("record path required (or --selftest)")
    sys.exit(run(args.record, args.instrument, args.prior))


if __name__ == "__main__":
    main()
