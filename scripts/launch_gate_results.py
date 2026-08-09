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
        figures
  LG-6  the gate-verdict line exists, uses the closed verdict set, and is
        consistent with the §4 formula as computable from the rows:
        READY requires all E rows Met, no plain Not met in A–D (the scoped
        form does not block), F3 Met, F4 Met, F2 Met or an explicit
        owner-deferral marker, and F1 Met-or-Unknown — a Not met F1 blocks
  LG-7  READY-WITH-DEFERRALS carries an owner-decision citation — the
        reviewer may not self-authorize a deferral
  LG-8  E1's five sub-verdict rows (form, home, granularity,
        acceptance-authority, change-process) are present, and an E1
        rollup of Met requires all five sub-rows Met

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


def validate(record_path: Path, instrument_path: str, prior_path=None,
             _git=True):
    errors, notes = [], []
    txt = record_path.read_text(encoding="utf-8")

    # ---- LG-1 header ------------------------------------------------------
    mdate = re.search(r"administration\s+—\s+([0-9]{4}-[0-9]{2}-[0-9]{2})",
                      txt)
    mcommit = re.search(r"commit\s+`?([0-9a-f]{7,40})`?", txt)
    mver = re.search(r"Instrument version:\s*\**\s*(v[\d.]+)", txt)
    minstd = re.search(
        r"Instrument version:[^\n]*sha256:\s*`?([0-9a-f]{64})`?", txt)
    mparamd = re.search(r"Parameter block sha256:\s*`?([0-9a-f]{64})`?", txt)
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

    # ---- LG-2 digest verification ----------------------------------------
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
            if mparamd:
                pb = param_block_bytes(blob)
                if pb is None:
                    errors.append("LG-2: committed instrument has no §8 "
                                  "parameter block to hash")
                elif sha256_bytes(pb) != mparamd.group(1):
                    errors.append(
                        f"LG-2: parameter-block digest mismatch — record "
                        f"quotes {mparamd.group(1)[:12]}…, §8 at the named "
                        f"commit hashes to {sha256_bytes(pb)[:12]}…")
    elif not _git:
        notes.append("LG-2: git unavailable — digest verification skipped, "
                     "record NOT fully validated")

    # ---- LG-3 / LG-5 verdict rows ----------------------------------------
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
    if not re.search(r"^#+ .*G1", txt, re.M):
        errors.append("LG-4: no G1 section — an administration missing G1 "
                      "is incomplete and cannot support a gate decision")

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

    # ---- LG-6 gate verdict line ------------------------------------------
    mg = GATE_VERDICT_RE.search(txt)
    n_not = sum(1 for v in verdicts.values() if v == "Not met")
    n_unk = sum(1 for v in verdicts.values() if v == "Unknown")
    if not mg:
        errors.append("LG-6: no GATE VERDICT line found")
    else:
        gv = mg.group(1).strip()
        if gv.startswith("READY"):
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
            # The deferral marker must be an F2 statement, not any line
            # containing the words — §5's own `Deferred count (owner-
            # deferred …)` field label would otherwise satisfy it.
            f2_deferral = re.search(
                r"^[^\n]*F2[^\n]*owner-deferred|^[^\n]*owner-deferred"
                r"[^\n]*F2", txt, re.I | re.M)
            if verdicts.get("F2") != "Met" and not f2_deferral:
                bad.append("F2 neither Met nor explicitly owner-deferred")
            if verdicts.get("F1") == "Not met":
                bad.append("F1 is Not met — the §4 convergence conjunct "
                           "(F1 Met-or-Unknown) fails")
            if bad and gv.startswith("READY FOR"):
                errors.append("LG-6: verdict claims READY but the rows "
                              "refuse it — " + "; ".join(bad))
            if gv.startswith("READY-WITH-DEFERRALS") and \
                    "owner" not in gv.lower() and \
                    not re.search(r"owner decision", txt, re.I):
                errors.append("LG-7: READY-WITH-DEFERRALS without an owner-"
                              "decision citation — only the owner defers")

    # ---- LG-5 trend row ---------------------------------------------------
    # The Deferred and Reopened figures are parsed from required explicit
    # fields, never derived from absence: a missing field is an error, not a
    # zero (VIS-2 — RD24-19 showed the prior build printed 0 from nothing).
    deferred_m = re.search(r"^Deferred count[^:]*:\s*(\d+)", txt, re.M)
    reopened_m = re.search(r"^Reopened count[^:]*:\s*(\d+)", txt, re.M)
    if not deferred_m:
        errors.append("LG-5: no `Deferred count:` field — the trend row's "
                      "Deferred figure has no source; absence is an error, "
                      "never zero")
    if not reopened_m:
        errors.append("LG-5: no `Reopened count:` field — a zero Reopened "
                      "claim needs a stated count, not a missing field")
    deferred = deferred_m.group(1) if deferred_m else "—"
    reopened = reopened_m.group(1) if reopened_m else "—"
    new_vs_prior = "n/a — no prior record supplied"
    if prior_path:
        ptxt = Path(prior_path).read_text(encoding="utf-8")
        prior_not = {m.group(1) for m in
                     (ROW_RE.match(l.strip()) for l in ptxt.splitlines())
                     if m and m.group(2).strip().startswith("Not met")}
        cur_not = {q for q, v in verdicts.items() if v == "Not met"}
        new_vs_prior = str(len(cur_not - prior_not))
    gate_word = mg.group(1).strip() if mg else "—"
    n_scoped = sum(1 for v in verdicts.values() if v == SCOPED)
    if n_scoped:
        notes.append(f"{n_scoped} scoped row(s) — `Not met (out of launch "
                     "scope)` — recorded as findings outside launch scope; "
                     "they do not block the §4 formula and are not in the "
                     "trend row's Not-met column")
    trend = (f"| {mdate.group(1) if mdate else '—'} "
             f"| {mcommit.group(1)[:8] if mcommit else '—'} "
             f"| {n_not} | {n_unk} | {deferred} | {reopened} "
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
          " — counts computed from the rows, never transcribed")
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

GOOD = """# Launch-gate administration — 2026-08-10, commit {sha}
> This administration record is evidence, never an owner act.
Instrument version: v1.5  sha256: {inst}
Parameter block sha256: {param}
Launch target: Capability 1
Reviewer: human, fresh context: yes
Reviewer model family: human

| Q | Verdict | Evidence |
|---|---------|----------|
| A1 | Met | x |
| E1-form | Met | x |
| E1-home | Met | x |
| E1-granularity | Met | x |
| E1-acceptance-authority | Met | x |
| E1-change-process | Met | x |
| E1 | Met | x |
| F1 | Unknown (first administration) | x |
| F2 | Not met | x |
| F3 | Met | x |
| F4 | Met | x |

## G1 — completeness critic
none proposed

Deferred count (owner-deferred findings this administration): 0
Reopened count (previously recorded resolved, recurred): 0

GATE VERDICT: NOT READY
"""


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

    case("well-formed record validates (git checks off)", good, None)
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
    case("READY with F2 not met and no owner deferral rejected",
         good.replace("GATE VERDICT: NOT READY",
                      "GATE VERDICT: READY FOR Capability 1"),
         "F2 neither Met nor explicitly owner-deferred")
    case("duplicate question rejected",
         good.replace("| A1 | Met | x |", "| A1 | Met | x |\n| A1 | Met | x |"),
         "appears twice")
    case("no verdict rows rejected",
         re.sub(r"^\|.*\|$", "", good, flags=re.M),
         "no verdict rows parsed")
    # LG-1 commit existence and LG-2 need git; exercise against the repo
    case("nonexistent commit rejected (git on)",
         good.replace(sha, "f" * 40), "does not exist", _git=True)

    # --- v1.5 fixtures: RD-24's mutation-proven defects, kept closed ------
    ready = (good.replace("| F2 | Not met | x |", "| F2 | Met | x |")
                 .replace("GATE VERDICT: NOT READY",
                          "GATE VERDICT: READY FOR Capability 1"))
    case("scoped A-D row does not block READY (RD24-05 T2, lawful form)",
         ready.replace(
             "| A1 | Met | x |",
             "| A1 | Met | x |\n"
             "| C2 | Not met (out of launch scope) | x |"),
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
