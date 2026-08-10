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


def _row_verdicts(text: str) -> dict:
    """Parse verdict rows with one normalization for record and prior alike
    (RD33-02: the prior side previously used startswith over the scoped
    form while the current side matched exactly — asymmetric)."""
    out = {}
    for line in text.splitlines():
        m = ROW_RE.match(line.strip())
        if m and m.group(1) != "Q":
            out[m.group(1)] = m.group(2).strip()
    return out


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
    out = []
    fence_char, fence_len = None, 0
    in_comment = False
    for ln in txt.splitlines():
        if fence_char is not None:
            s = ln.lstrip()
            indent = len(ln) - len(s)
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
                out.append(ln)
            continue
        s = ln.lstrip()
        indent = len(ln) - len(s)
        mo = re.match(r"(`{3,}|~{3,})", s)
        if mo and indent <= 3:
            fence_char = mo.group(1)[0]
            fence_len = len(mo.group(1))
            continue
        out.append(ln)
    return "\n".join(out)


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
    # kept for exactly one rule: the terminal GATE VERDICT line (RD39-01).
    _raw = record_path.read_text(encoding="utf-8")
    txt = _active_text(_raw)

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
    _ver = _decl(r"^Instrument version:[^\S\n]*\**[^\S\n]*(v[\d.]+)", txt,
                 errors, "LG-1", "Instrument version:")
    mver = _Field(_ver) if _ver else None
    _instd = _decl(
        r"^Instrument version:[^\n]*sha256:[^\S\n]*`?([0-9a-f]{64})`?",
        txt, errors, "LG-1", "Instrument version: … sha256:")
    minstd = _Field(_instd) if _instd else None
    _paramd = _decl(r"^Parameter block sha256:[^\S\n]*`?([0-9a-f]{64})`?",
                    txt, errors, "LG-1", "Parameter block sha256:")
    mparamd = _Field(_paramd) if _paramd else None
    _lt = _decl(r"^Launch target:[^\S\n]*(\S.*)$", txt,
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
    # of an incidental mention.
    if not re.search(r"^#+\s*G1\b", txt, re.M):
        errors.append("LG-4: no G1 section — an administration missing G1 "
                      "is incomplete and cannot support a gate decision")

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
    _dc = _decl(r"^Deferred count[^:\n]*:[^\S\n]*(\d+)", txt,
                errors, "LG-5", "Deferred count:")
    _rc = _decl(r"^Reopened count[^:\n]*:[^\S\n]*(\d+)", txt,
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
    owner_dec = _decl(r"^Owner deferral decision:[^\S\n]*(\S.*)$", txt,
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
        txt, errors, "LG-9",
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
    # RD39-01: "last" is measured over the RAW record bytes, never the
    # stripped text — inserting the fence strip upstream of this rule
    # silently redefined "last", so a stored terminal NOT READY behind an
    # unterminated fence was reported as READY FOR the verbatim target. If
    # the raw terminal line is not the active terminal line — fenced,
    # comment-carried, swallowed by an unterminated fence, or shadowed by
    # a quoted verdict line placed after the record's own — the record
    # errors loudly; no earlier line is ever parsed in its place.
    # That line must itself parse to the closed verdict set; a terminal
    # verdict outside the set is an error, never an invitation to look
    # upward. A captured verdict containing `|` is rejected — it would
    # structurally corrupt §6's nine-column trend row.
    _gv_lines = [ln for ln in txt.splitlines() if "GATE VERDICT:" in ln]
    _gv_raw = [ln for ln in _raw.splitlines() if "GATE VERDICT:" in ln]
    mg = None
    n_not = sum(1 for v in verdicts.values() if v == "Not met")
    n_unk = sum(1 for v in verdicts.values() if v == "Unknown")
    if not _gv_raw:
        errors.append("LG-6: no GATE VERDICT line found")
    elif not _gv_lines or _gv_lines[-1] != _gv_raw[-1]:
        errors.append(
            "LG-6: the record's terminal `GATE VERDICT:` line — "
            f"{_gv_raw[-1].strip()!r} — is not the record's active "
            "terminal line: it sits inside a fenced or comment-carried "
            "block, after an unterminated fence, or a quoted verdict "
            "line follows the record's own. §5's terminal line is the "
            "LAST line carrying the token in the record's own bytes; "
            "the verdict a reader sees must be the verdict the trend "
            "row reports, and a verdict quoted after the terminal one "
            "makes the terminal ambiguous (RD35-02, RD39-01)")
    else:
        mg = GATE_VERDICT_RE.search(_gv_lines[-1])
        if not mg:
            errors.append(
                "LG-6: the terminal `GATE VERDICT:` line — "
                f"{_gv_lines[-1].strip()!r} — does not parse to the closed "
                "verdict set (READY FOR <LAUNCH_TARGET> / NOT READY / "
                "READY-WITH-DEFERRALS); a qualified or quoted verdict is "
                "not a verdict (§5's terminal line; RD35-02)")
        elif "|" in mg.group(1):
            errors.append(
                "LG-6: the terminal verdict contains '|' — it would "
                "corrupt the nine-column trend row §6 defines and F1 is "
                "answered from (RD35-02)")
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
    # RD39-02/RD39-07: presence is a line-anchored FIELD read, never a
    # substring scan — the record-versus-quotation distinction the value
    # checks already own (RD36-02/RD38-03), applied to the presence
    # surface. A label at <=3 spaces of indentation (CommonMark's own
    # bound), optionally list-marked or bold-wrapped, with internal
    # whitespace normalized, is the record's own field; a blockquoted
    # `> Label:`, a >=4-space-indented line, and a mid-line prose
    # mention are quotations of the label, not the field. Fences and
    # HTML comments are already gone from `txt` (_active_text). The
    # non-authority banner is structural rather than label-shaped: §5's
    # banner IS a blockquote, so its test is a blockquote line carrying
    # the phrase — prose or any other carrier fails it.
    def _label_present(label):
        words = label.rstrip(":").split()
        pat = (r"^ {0,3}(?:[-*+][^\S\n]+)?\**"
               + r"[^\S\n]+".join(re.escape(w) for w in words)
               + r"[^\S\n]*:")
        return re.search(pat, txt, re.M) is not None
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
        if not _label_present(token):
            errors.append(f"LG-12: required §5 field missing — {token!r} "
                          f"({why}; RD35-07)")
    if not any(re.match(r" {0,3}>", ln)
               and "evidence, never an owner act" in _norm_ws(ln)
               for ln in txt.splitlines()):
        errors.append("LG-12: required §5 field missing — 'evidence, "
                      "never an owner act' (the non-authority banner "
                      "(RD24-02) — a blockquote line carrying the "
                      "phrase, §5's own form; prose and quotation "
                      "carriers satisfy nothing, RD39-02; RD35-07)")
    _unk_val = _decl(
        r"^Unknowns and what would settle them:[^\S\n]*(\S.*)$",
        txt, errors, "LG-12", "Unknowns and what would settle them:")
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
    _e3_val = _decl(r"^E3 reopen-list:[^\S\n]*(\S.*)$", txt,
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
Instrument version: v1.11  sha256: {inst}
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
    # LG-1 commit existence needs git; exercise against the repo
    case("nonexistent commit rejected (git on)",
         good.replace(sha, "f" * 40), "does not exist", _git=True)

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
        good_head = GOOD.format(sha=head, inst=inst, param=param)
        case("instrument digest mismatch rejected (git on, LG-2)",
             good_head, "digest mismatch", _git=True)
        case("instrument version disagreement rejected (RD33-06, LG-11)",
             good_head.replace("Instrument version: v1.11",
                               "Instrument version: v1.2"),
             "LG-11: record claims instrument version", _git=True)
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
         f"Instrument version: v1.11  sha256: {inst}",
         f"Instrument version: v0.0  sha256: {inst}"),
        ("Instrument version: … sha256:",
         f"Instrument version: v1.11  sha256: {inst}",
         "Instrument version: v1.11  sha256: " + "9" * 64),
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
    case("list-marked `- Operationalization notes:` satisfies presence "
         "(RD39-07)",
         good.replace("Operationalization notes: none",
                      "- Operationalization notes: none"),
         None)

    # RD39-03: the internal-whitespace case — the behavioral change the
    # v1.11 normalization repair actually made — carries its fixture,
    # so reverting `_decl`'s return to the exact v1.10 `.strip()` bytes
    # fails here (rule 6 against the code the repair replaced).
    case("`E3 reopen-list: none  identified` (internal double space) "
         "accepted as the marker (RD39-03)",
         good.replace("E3 reopen-list: empty",
                      "E3 reopen-list: none  identified"),
         None)

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
