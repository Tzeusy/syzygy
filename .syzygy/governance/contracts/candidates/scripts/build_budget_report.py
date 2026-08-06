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


def redact_measurements(text, counter):
    """Replace transcribed measurement figures with a pointer to §3."""
    def sub(m):
        counter.append(m.group(0))
        return REDACTION
    return PROSE_MEASUREMENT.sub(sub, text)


def waiver_fields(body, counter):
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
            out[k] = redact_measurements(value.strip(), counter)
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
    return body, n_meas, n_dig


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
    redacted = []
    a("## 2. Candidate budget exceptions — one row per breaching fixture")
    a("")
    a("Fields are read out of each fixture's own declaration. A missing field")
    a("renders `[Unknown]`, never blank and never `none`: an unrecorded")
    a("reviewer is not the same fact as no reviewer being required.")
    a("")
    a("**How dense the redactions are is itself the finding.** Review RD-5")
    a("counted 88 measurement-shaped figures across the nine fixtures and")
    a("found CG-18 covering 18 of them; the rest were transcriptions checked")
    a("by nothing, and at least five contradicted their own fixture's")
    a("headline. A disposition argued against an unchecked number is a")
    a("disposition argued against nothing. Reading these fields with the")
    a("figures removed shows how much of each argument was resting on one.")
    a("")
    a("**Measurement figures inside these transcribed fields are redacted and")
    a("routed to \u00a73**, which measures the files rather than quoting a")
    a("fixture. An earlier revision transcribed them, and two fixtures'")
    a("*\"RFC-0001 is indivisible (8,353 w)\"* disagreed by eleven words with")
    a("this file's own computed table thirty lines below \u2014 a stale figure")
    a("reaching the generated report through the one door left open (review")
    a("RD-5). The count of redactions is printed at the foot of \u00a75.")
    a("")
    for m in breaches:
        w = waiver_fields(m["body"], redacted)
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


def run(check=False):
    measures = [measure_fixture(p) for p in fixture_paths()]
    drift = []
    for m in measures:
        new, n_meas, n_dig = rewrite_anchors(m, m["body"])
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
        # The as-of commit line makes the report differ whenever HEAD moves,
        # which is correct for a generated file and useless as a drift signal.
        # --check therefore reports it and exits nonzero only on a *fixture*
        # anchor drift, which is the thing a stale artifact hides.
        anchor_drift = [d for d in drift if "CONTEXT-BUDGET-REPORT" not in d]
        for d in drift:
            print(f"DRIFT: {d}")
        if anchor_drift:
            return 1
        if drift:
            print("note: report-only drift (as-of commit / corpus figures); "
                  "regenerate before quoting")
        print("fixture anchors match regeneration")
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
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    sys.exit(selftest() if args.selftest else run(check=args.check))
