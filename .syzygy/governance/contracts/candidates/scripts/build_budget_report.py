#!/usr/bin/env python3
"""Own every volatile context measurement in one generated place.

This repository has shipped a stale derived number four times: word counts in
package READMEs, token estimates in fixtures, check totals in the offering,
and fixture digests inside act 1's digest set. Each was correct when written.
Each was transcribed into a second artifact, and the second artifact had no
way to notice the first had moved.

The rule this script exists to make executable is not "refresh the numbers".
It is: **a measurement has exactly one home, and that home is generated.**

Two jobs, one measurement pass:

1. Rewrite the two *anchored* fields inside each context fixture — the
   `Measured:` figure and the packet digest — from a recomputation. Nothing
   else in a fixture may state a measurement; prose points at the anchored
   field. `check_governance.py` CG-18 independently verifies the anchors, so
   this script writing them is not also the thing that checks them.

2. Emit `CONTEXT-BUDGET-REPORT.md` beside the contract index, which owns
   the current figures for every fixture and every contract module.
   Anything elsewhere that wants a number links there rather than copying
   one. Its home is stable and round-independent on purpose: contract prose
   may point at it without acquiring a round number.

Usage:
  build_budget_report.py            rewrite fixture anchors, write the report
  build_budget_report.py --check    recompute and diff; nonzero exit on drift
  build_budget_report.py --selftest mutate each rewrite target, confirm --check fails
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CANDIDATES = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(CANDIDATES, "..", "..", "..", ".."))
DOCTRINE = os.path.join(ROOT, ".syzygy/governance/doctrine")
CRAFT = os.path.join(ROOT, ".syzygy/governance/policies/craft-and-care")
FIXTURES = os.path.join(CANDIDATES, "fixtures")
RFCS = os.path.join(CANDIDATES, "rfcs")
REPORT = os.path.join(CANDIDATES, "CONTEXT-BUDGET-REPORT.md")

#: The only token heuristic this repository uses in prose. It is an estimate
#: and is labelled as one everywhere it appears; no tokenizer is vendored,
#: because vendoring one would be a stack choice.
TOKENS_PER_WORD = 1.35
#: The decomposition trigger the candidate knowledge-hygiene policy proposes
#: as CC-BUDGET-1. It is *not installed* — no `CC-BUDGET-*` identifier
#: resolves to a governed artifact today (review RC-12 §5). Recorded here as
#: the proposed line every disposition below is measured against, never as a
#: rule in force.
PROPOSED_TRIGGER_TOKENS = 20000
PROPOSED_BAND = (5000, 15000)

ANCHOR_MEASURED = re.compile(
    r"(Measured:\s*\*\*)([\d,]+)(\s*words\s*≈\s*)([\d,]+)(\s*estimated tokens)")
ANCHOR_CHARS = re.compile(
    r"(\*\*)([\d,]+)(\s*estimated tokens\*\*\s*at chars\s*÷\s*4 over\s*)([\d,]+)"
    r"(\s*characters)")
WAIVER_ROW = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*$", re.M)

#: RFC11-4's index-digest duty, machine-writable. Review RD-12 finding 4: two
#: fixtures select a contract without loading its index and bind the recorded
#: declaration with *"read at the index bytes the packet digest below was
#: stamped against"* — but the packet digest is sha256 over the **mandatory**
#: files, and a README that was not loaded is not among them, so no index
#: digest is recorded anywhere and the clause's whole point (a later index
#: edit invalidates the declaration) is unserved. The repair the review asks
#: for is that the digest be *machine-written and CG-18-covered, never
#: transcribed* — so the anchor lives here, beside the two anchors this
#: script already owns.
#:
#: A fixture opts in by writing the anchor with any placeholder:
#:     Index read at `<sha256>` — `rfcs/RFC-0004/README.md`
#: This script fills it from the named file on every run. **Zero fixtures
#: carry it today** — the fixture-side edit is R-FIX's and P-29 may bind
#: those bytes — so the count below prints 0 until they do, which is the
#: honest state and not a silent no-op.
ANCHOR_INDEX_DIGEST = re.compile(
    r"(Index read at\s*`)([0-9a-f]{8,64})(…?`\s*[—-]\s*`)([^`]+)(`)")

#: Named so `--check` can state its denominator as a number of *fields*
#: rather than a number this script would otherwise transcribe.
ANCHORED_FIELDS = ("Measured:", "chars ÷ 4", "packet digest",
                   "index digest")


def resolve_load_spec(spec):
    """Same resolution CG-18 uses. Kept textually parallel on purpose: if the
    two ever diverge, the generator and the check disagree about what a
    fixture selected, which is the one failure neither would report."""
    if spec.startswith("doctrine:"):
        return os.path.join(DOCTRINE, spec[len("doctrine:"):])
    if spec.startswith("craft:"):
        return os.path.join(CRAFT, spec[len("craft:"):])
    return os.path.join(CANDIDATES, spec)


def fixture_paths():
    if not os.path.isdir(FIXTURES):
        return []
    return [os.path.join(FIXTURES, n) for n in sorted(os.listdir(FIXTURES))
            if n.startswith("context-selection-") and n.endswith(".md")]


def measure_fixture(path):
    body = open(path, encoding="utf-8").read()
    cmd = re.search(r"```\s*\n(scripts/context_load\.py[\s\S]*?)\n```", body)
    if not cmd:
        raise SystemExit(f"{path}: no load command; a fixture with no "
                         f"reproducible selection is unmeasurable, not passing")
    specs = [s for s in cmd.group(1).replace("\\\n", " ").split()
             if s != "scripts/context_load.py" and s.strip()]
    blob, words, chars, missing = b"", 0, 0, []
    for s in specs:
        p = resolve_load_spec(s)
        if not os.path.exists(p):
            missing.append(s)
            continue
        data = open(p, "rb").read()
        blob += data
        text = data.decode("utf-8", "replace")
        words += len(text.split())
        chars += len(text)
    if missing:
        raise SystemExit(f"{path}: mandatory load names {missing}, which do "
                         f"not exist; the fixture cannot be reproduced")
    return {
        "path": path,
        "name": os.path.basename(path),
        "body": body,
        "files": len(specs),
        "words": words,
        "chars": chars,
        "tokens": round(words * TOKENS_PER_WORD),
        "tokens_chardiv": round(chars / 4),
        "digest": hashlib.sha256(blob).hexdigest(),
    }


#: A measurement figure transcribed inside a fixture's prose. §2 quotes that
#: prose; §3 measures the files. When the two disagree the generated report
#: contradicts itself under its own do-not-copy-a-figure banner — which is
#: what happened: fixtures 7 and 8 carry "RFC-0001 is indivisible (8,353 w …)"
#: while this script's own §3 table computes 8,342 for the same file, eleven
#: words apart and thirty lines apart in one generated artifact. Review RD-5
#: found it. The figure is therefore **redacted at transcription** and routed
#: to the table that measures it, so a stale number in a fixture cannot reach
#: this report at all. Redactions are counted and printed, never silent.
PROSE_MEASUREMENT = re.compile(
    r"\b\d{1,2},\d{3}(?:\s*(?:w\b|words?\b|(?:est\.?|estimated)\s+tokens?\b"
    r"|tokens?\b))?")
REDACTION = "[figure removed — see §3]"


#: A relative path inside a transcribed field. The fixtures live one level
#: below this report (`candidates/fixtures/` → `candidates/`), so a `../x`
#: written correctly *there* is broken *here* — four copies of
#: `../round-2026-08b/reviews/RC-12-budget-waiver-RAW.md` pointed one level
#: above the package (review RD-7, and it was invisible until the link
#: checker stopped discarding `../` traversal). This is the measurement
#: defect in a different currency: a value correct in its own frame,
#: transcribed into a frame where it is false. One leading `../` is stripped;
#: a deeper traversal is left alone and will fail the link check loudly,
#: because guessing at it would be the same mistake with more steps.
PROSE_RELPATH = re.compile(r"`\.\./(?!\.)([^`]+)`")


def reparent_paths(text, counter):
    def sub(m):
        counter.append(m.group(0).strip("`"))
        return f"`{m.group(1)}`"
    return PROSE_RELPATH.sub(sub, text)


def redact_measurements(text, counter):
    """Replace transcribed measurement figures with a pointer to §3."""
    def sub(m):
        counter.append(m.group(0))
        return REDACTION
    return PROSE_MEASUREMENT.sub(sub, text)


def waiver_fields(body, counter, path_counter):
    """Pull the waiver/justification table rows a fixture declares.

    Parsed rather than kept in a table here: a second copy of the reviewer,
    scope and expiry is exactly the duplication this script exists to remove.
    A fixture with no such block reports Unknown, never 'none' — absence of a
    waiver record is not evidence that no waiver is owed (VIS-2).

    Measurement figures inside the transcribed prose are redacted: this file
    owns every measurement it prints, and a figure it copies is a figure it
    does not own.
    """
    out = {}
    for key, value in WAIVER_ROW.findall(body):
        k = key.strip().lower()
        if k in ("reason", "scope", "reviewer", "expiry / revisit trigger",
                 "decomposition reviewed", "artifact", "correction"):
            out[k] = reparent_paths(
                redact_measurements(value.strip(), counter), path_counter)
    return out


def disposition(tokens):
    if tokens > PROPOSED_TRIGGER_TOKENS:
        pct = (tokens - PROPOSED_TRIGGER_TOKENS) / PROPOSED_TRIGGER_TOKENS * 100
        return f"**above the proposed trigger** by {pct:.1f}%"
    if tokens > PROPOSED_BAND[1]:
        return "above the proposed default band, under the proposed trigger"
    if tokens < PROPOSED_BAND[0]:
        return "below the proposed default band"
    return "inside the proposed default band"


def rewrite_anchors(m, body):
    """Write the measured figure and the packet digest from the measurement.

    Only these two fields are machine-written. Everything else in a fixture is
    authored prose, including every sentence *about* the figure — which is why
    no sentence may restate it.
    """
    def measured(mo):
        return (f"{mo.group(1)}{m['words']:,}{mo.group(3)}"
                f"{m['tokens']:,}{mo.group(5)}")
    body, n_meas = ANCHOR_MEASURED.subn(measured, body)

    def chars(mo):
        return (f"{mo.group(1)}{m['tokens_chardiv']:,}{mo.group(3)}"
                f"{m['chars']:,}{mo.group(5)}")
    body = ANCHOR_CHARS.sub(chars, body)

    head, sep, tail = body.partition("## Packet digest")
    n_dig = 0
    if sep:
        def dig(mo):
            return f"`{m['digest'][:len(mo.group(1))]}…`"
        tail, n_dig = re.subn(r"`([0-9a-f]{8,64})(?:…|\.\.\.)`", dig, tail,
                              count=1)
        body = head + sep + tail

    # RFC11-4's index digest, computed from the file the fixture names. The
    # anchor's *target path* is authored; the digest never is.
    def idx(mo):
        p = os.path.join(CANDIDATES, mo.group(4))
        if not os.path.exists(p):
            return mo.group(0)
        d = hashlib.sha256(open(p, "rb").read()).hexdigest()
        width = len(mo.group(2))
        return f"{mo.group(1)}{d[:width]}{mo.group(3)}{mo.group(4)}{mo.group(5)}"
    body, n_idx = ANCHOR_INDEX_DIGEST.subn(idx, body)
    return body, n_meas, n_dig, n_idx


def module_words():
    rows = []
    for dirpath, _dirs, names in os.walk(RFCS):
        for n in sorted(names):
            if not n.endswith(".md"):
                continue
            p = os.path.join(dirpath, n)
            rel = os.path.relpath(p, CANDIDATES)
            text = open(p, encoding="utf-8").read()
            rows.append((rel, len(text.split())))
    return sorted(rows)


def head_commit():
    try:
        out = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"],
                             capture_output=True, text=True, check=True)
        dirty = subprocess.run(["git", "-C", ROOT, "status", "--porcelain"],
                               capture_output=True, text=True, check=True)
        return out.stdout.strip(), bool(dirty.stdout.strip())
    except Exception:
        return "unknown", True


def render_report(measures):
    sha, dirty = head_commit()
    mods = module_words()
    total = sum(w for _, w in mods)
    lines = []
    a = lines.append
    a("# Context budget report — generated, non-authoritative")
    a("")
    a("> **Generated file. Do not edit by hand, and do not copy a figure out")
    a("> of it.** Regenerate with the command in §5. Every number here is a")
    a("> measurement of the repository *as it currently stands*; it is stale")
    a("> the moment any measured file changes, which is why it is the only")
    a("> place a measurement lives. Prose that needs a figure links here.")
    a(">")
    a("> This report accepts nothing, waives nothing, and grants nothing. The")
    a("> threshold every disposition below is measured against — the")
    a("> 20,000-token decomposition trigger proposed as `CC-BUDGET-1` — is")
    a("> **installed nowhere**: it lives in a candidate policy with no owner")
    a("> act, and no `CC-BUDGET-*` identifier resolves to a governed artifact")
    a("> today. A waiver against a rule that does not bind is a different")
    a("> object from a waiver against one that does (review RC-12 §5), and")
    a("> every row below says `candidate budget exception`, never `waiver`.")
    a("")
    a(f"**As-of commit:** `{sha}`"
      + ("  *(plus uncommitted working-tree edits at generation time)*"
         if dirty else ""))
    a("")
    a("This file is regenerated in the *same change* that moves any measured")
    a("file. Two independent currency tests exist and neither is this line:")
    a("`build_budget_report.py --check` recomputes the fixture anchors, and")
    a("`check_governance.py` CG-18 recomputes them again from separate code.")
    a("")
    a("## 1. Context fixtures — hand-authored selections, mechanically measured")
    a("")
    a("Every selection below was **chosen by a human**. There is no context")
    a("compiler in this repository. `scripts/context_load.py` resolves a path")
    a("list it is handed and counts words; it has no notion of a task, a")
    a("warrant, a risk class, or a dependency edge. What is mechanical here is")
    a("the *measurement*, never the *selection*.")
    a("")
    a("| Fixture | Files | Words | Est. tokens (×1.35) | Disposition vs the proposed trigger | Packet digest |")
    a("|---|---:|---:|---:|---|---|")
    for m in measures:
        a(f"| `{m['name']}` | {m['files']} | {m['words']:,} | "
          f"{m['tokens']:,} | {disposition(m['tokens'])} | "
          f"`{m['digest'][:16]}…` |")
    a("")
    breaches = [m for m in measures if m["tokens"] > PROPOSED_TRIGGER_TOKENS]
    a(f"**{len(breaches)} of {len(measures)} fixtures are above the proposed "
      f"20,000-token trigger.**")
    a("")
    redacted, reparented = [], []
    a("## 2. Candidate budget exceptions — one row per breaching fixture")
    a("")
    a("Fields are read out of each fixture's own declaration. A missing field")
    a("renders `[Unknown]`, never blank and never `none`: an unrecorded")
    a("reviewer is not the same fact as no reviewer being required.")
    a("")
    # **No figure in this paragraph is transcribed.** It used to read "88
    # measurement-shaped figures across the nine fixtures \u2026 CG-18 covering 18
    # of them" \u2014 three hard-coded numbers, two of them already false: \u00a71
    # above measures ten fixtures, and CG-18's coverage is twice the fixture
    # count. The file then denied in \u00a74 that it contained any fixture count or
    # coverage denominator, which is a generated artifact contradicting
    # itself under its own do-not-copy-a-figure banner (review RD-17
    # finding 5). Review RD-5's own counts are named as *its* findings, dated,
    # and not restated as current.
    a("**How dense the redactions are is itself the finding.** Review RD-5")
    a("(2026-08-08) found that most measurement-shaped figures inside these")
    a("fields were transcriptions checked by nothing, and that several")
    a("contradicted their own fixture's headline. A disposition argued")
    a("against an unchecked number is a disposition argued against nothing.")
    a(f"Reading the {len(measures)} fixture(s) measured above with the")
    a("figures removed shows how much of each argument was resting on one.")
    a("")
    a("**Measurement figures inside these transcribed fields are redacted and")
    a("routed to \u00a73**, which measures the files rather than quoting a")
    a("fixture. An earlier revision transcribed them, and two fixtures'")
    a("*\"RFC-0001 is indivisible\"* parenthetical disagreed with this file's")
    a("own computed table thirty lines below \u2014 a stale figure reaching the")
    a("generated report through the one door left open (review RD-5). The")
    a("current measurement of that module is the \u00a73 row for it, and this")
    a("sentence deliberately does not repeat it. The count of redactions is")
    a("printed at the foot of \u00a75.")
    a("")
    for m in breaches:
        w = waiver_fields(m["body"], redacted, reparented)
        a(f"### `{m['name']}`")
        a("")
        over = ((m["tokens"] - PROPOSED_TRIGGER_TOKENS)
                / PROPOSED_TRIGGER_TOKENS * 100)
        a(f"- **Measured:** {m['words']:,} words ≈ {m['tokens']:,} estimated "
          f"tokens — {over:.1f}% above the proposed trigger.")
        for label, key in (("Reason", "reason"), ("Scope", "scope"),
                           ("Reviewer", "reviewer"),
                           ("Expiry / revisit trigger",
                            "expiry / revisit trigger"),
                           ("Decomposition reviewed",
                            "decomposition reviewed")):
            a(f"- **{label}:** {w.get(key, '[Unknown] — not declared in the fixture')}")
        a("")
    a("## 3. Contract modules — the corpus this budget is spent on")
    a("")
    a(f"**{len(mods)} modules, {total:,} words.** The 7,000-word per-module")
    a("ceiling and the 35–50k corpus target band are the compaction charter's,")
    a("recorded in `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`; both are")
    a("candidate figures under the same non-installed policy as §1's trigger.")
    a("")
    a("| Module | Words | Over the 7,000 ceiling |")
    a("|---|---:|---|")
    for rel, w in mods:
        a(f"| `{rel}` | {w:,} | {'**yes**' if w > 7000 else '—'} |")
    a("")
    a("## 4. What this report deliberately does not contain")
    a("")
    a("- **No check counts, fixture counts, or coverage denominators.** Those")
    a("  are printed by `check_governance.py` on every run, with each check's")
    a("  own denominator. Copying them here would recreate the class this")
    a("  report exists to end, one register further out.")
    a("- **No act digests.** Those belong to the acceptance record and are")
    a("  verified by CG-7a…d against their subject artifacts.")
    a("- **No verdict on whether any figure is acceptable.** A budget")
    a("  disposition is a measurement against a proposed line. Whether the")
    a("  line binds is owner item **P-12**.")
    a("")
    a("## 5. Regeneration")
    a("")
    a("```sh")
    a("python3 .syzygy/governance/contracts/candidates/scripts/build_budget_report.py")
    a("python3 .syzygy/governance/contracts/candidates/scripts/build_budget_report.py --check")
    a("python3 scripts/check_governance.py   # CG-18 verifies the anchors independently")
    a("```")
    a("")
    a(f"**Redacted transcriptions:** {len(redacted)}. Every measurement figure")
    a("a fixture stated inside a \u00a72 field was replaced with a pointer to")
    a("\u00a73 rather than copied. The redacted strings, verbatim, so the")
    a("redaction is auditable rather than a silent deletion:")
    a("")
    for r in sorted(set(redacted)):
        a(f"- `{r}`")
    a("")
    a(f"**Re-parented relative paths:** {len(reparented)}. A fixture lives one")
    a("level below this report, so a `../x` correct in a fixture is broken")
    a("here. One leading `../` is stripped; anything deeper is left to fail")
    a("the link check loudly rather than guessed at. Rewritten, verbatim —")
    a("printed without code spans, because an earlier revision printed the")
    a("*original* path in a backtick span and the audit trail became the")
    a("broken reference it was auditing:")
    a("")
    for r in sorted(set(reparented)):
        a(f"- {r} → {r[3:]}")
    a("")
    return "\n".join(lines) + "\n"


def _without_asof(text):
    """Drop the as-of line before comparing.

    The commit identity moves on every commit, and a clone has no git at all,
    so comparing it would report drift on a file that is byte-correct for its
    content. The content is what --check is for; currency is CG-18's and the
    commit discipline's.
    """
    if text is None:
        return None
    return "\n".join(l for l in text.splitlines()
                      if not l.startswith("**As-of commit:**"))


def exit_code(drift):
    """`--check`'s exit decision, as one testable function.

    It exists as a function so the repair can be mutation-tested without a
    filesystem baseline: the defect review RD-17 finding 2 found was one
    comprehension here — `[d for d in drift if "CONTEXT-BUDGET-REPORT" not in
    d]` — which removed every finding about the generated report itself from
    the exit code. **Any drift is drift.** `_without_asof()` already removes
    the one legitimately volatile line before the comparison, so there is
    nothing left for an exemption to be for.
    """
    return 1 if drift else 0


def run(check=False):
    measures = [measure_fixture(p) for p in fixture_paths()]
    drift = []
    n_index_anchors = 0
    for m in measures:
        new, n_meas, n_dig, n_idx = rewrite_anchors(m, m["body"])
        n_index_anchors += n_idx
        if n_meas == 0:
            drift.append(f"{m['name']} — no `Measured:` anchor to write; a "
                         f"fixture that states no measurement cannot be "
                         f"budgeted")
        if n_dig == 0:
            drift.append(f"{m['name']} — no packet digest anchor under "
                         f"`## Packet digest`")
        if new != m["body"]:
            drift.append(f"{m['name']} — anchored measurement is stale")
            if not check:
                open(m["path"], "w", encoding="utf-8").write(new)
                m["body"] = new
    report = render_report(measures)
    existing = (open(REPORT, encoding="utf-8").read()
                if os.path.exists(REPORT) else None)
    if _without_asof(existing) != _without_asof(report):
        drift.append("CONTEXT-BUDGET-REPORT.md — differs from regeneration")
        if not check:
            os.makedirs(os.path.dirname(REPORT), exist_ok=True)
            open(REPORT, "w", encoding="utf-8").write(report)
    if check:
        # **No exemption.** This block used to filter every finding about the
        # report itself out of the exit code, on the stated ground that the
        # as-of commit line moves whenever HEAD does — but `_without_asof()`
        # already strips that line before the comparison, so the exemption
        # suppressed nothing except real content drift. Review RD-17 finding
        # 2 hand-edited the report's §3 headline from `39 modules, 110,081
        # words` to `32 modules, 99,067 words` and one module row from 8,556
        # to 1,234: `--check` printed the drift and returned 0, and the whole
        # documented battery stayed green. The values it injected were the
        # *actual* rev10-era figures still living elsewhere in the package,
        # so the hole permitted precisely the regression the report exists to
        # end. `AGENTS.md` lists this command as the check for "every
        # volatile measurement"; now it is one.
        for d in drift:
            print(f"DRIFT: {d}")
        print(f"population: {len(measures)} fixture(s), "
              f"{len(ANCHORED_FIELDS)} anchored field kind(s), "
              f"{n_index_anchors} RFC11-4 index-digest anchor(s) present, "
              f"{len(module_words())} module(s) in the report")
        if exit_code(drift):
            return 1
        print("fixture anchors and the generated report match regeneration")
        return 0
    print(f"measured {len(measures)} fixture(s); wrote anchors and "
          f"{os.path.relpath(REPORT, ROOT)}")
    return 0


def selftest():
    """Mutate each rewrite target and confirm --check reports it.

    Verification rule 6: a check nobody has seen fail is not evidence. Both
    anchors are mutated independently, because one regex covering two fields
    can pass on the field it does see.
    """
    import shutil
    import tempfile
    ok = True
    cases = []

    # Review RD-17 finding 2, as a predicate rather than a filesystem
    # baseline: a drift finding naming the generated report alone must exit
    # nonzero. Under the old comprehension it exited 0, and a hand-falsified
    # §3 headline passed the documented battery.
    cases.append(("report-only drift exits nonzero",
                  exit_code(["CONTEXT-BUDGET-REPORT.md — differs from "
                             "regeneration"]) == 1))
    cases.append(("a clean run exits zero", exit_code([]) == 0))

    # Review RD-17 finding 5: the §2 paragraph carried three hard-coded
    # figures, two already false, inside a file whose §4 denies containing a
    # fixture count. Every figure the generator writes is now computed in the
    # run that writes it.
    rendered = render_report([measure_fixture(p) for p in fixture_paths()])
    cases.append(("no transcribed fixture count in the generated report",
                  "the nine fixtures" not in rendered
                  and "covering 18" not in rendered
                  and "8,353 w" not in rendered))
    cases.append(("the generated report states its measured fixture count",
                  f"{len(fixture_paths())} fixture(s) measured above"
                  in rendered))

    for label, pattern, repl in (
        ("measured word count", ANCHOR_MEASURED,
         lambda mo: f"{mo.group(1)}111,111{mo.group(3)}{mo.group(4)}{mo.group(5)}"),
        ("packet digest", re.compile(r"`([0-9a-f]{16})…`"),
         lambda mo: "`0000000000000000…`"),
    ):
        target = fixture_paths()[0]
        backup = tempfile.mktemp()
        shutil.copy(target, backup)
        try:
            body = open(target, encoding="utf-8").read()
            mutated, n = pattern.subn(repl, body, count=1)
            if n == 0:
                print(f"SELFTEST INCONCLUSIVE: {label} — no site to mutate")
                ok = False
                continue
            open(target, "w", encoding="utf-8").write(mutated)
            rc = run(check=True)
            if rc == 0:
                print(f"SELFTEST FAIL: {label} mutation not detected")
                ok = False
            else:
                print(f"SELFTEST OK: {label} mutation detected")
        finally:
            shutil.copy(backup, target)
            os.unlink(backup)
    for label, passed in cases:
        print(f"SELFTEST {'OK' if passed else 'FAIL'}: {label}")
        ok = ok and passed
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    sys.exit(selftest() if args.selftest else run(check=args.check))
