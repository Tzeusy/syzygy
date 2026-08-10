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
  LG-6  the LAST `GATE VERDICT:` line (§5's "terminal line" — RD34-03)
        exists, uses the closed verdict set, and is consistent with the
        §4 formulas as computable from the rows. BOTH pass branches run
        the full conjunct battery (RD34-01): every E row Met, no plain
        Not met in A–D (the scoped form does not block), F3 Met, F4 Met,
        F1 Met-or-Unknown. Plain READY FOR additionally requires **F2 Met
        and zero declared deferrals**; READY-WITH-DEFERRALS substitutes
        exactly the F2 limb with an owner-cited deferral (instrument §4)
  LG-7  any record whose `Deferred count:` is nonzero — under ANY verdict
        (RD34-07) — and any READY-WITH-DEFERRALS verdict requires the
        `Owner deferral decision:` field, whose value must be a
        repository path (verified to exist at the named commit when git
        checks run) or a decision identifier (SDR-n/P-n/D-n/B-n shape) —
        label wording like "(owner only)" is rejected (RD34-02); a
        deferral-carrying verdict with `Deferred count: 0` is an error
  LG-8  E1's five sub-verdict rows (form, home, granularity,
        acceptance-authority, change-process) are present, and an E1
        rollup of Met requires all five sub-rows Met
  LG-9  a record with any scoped row must name at least one defect on the
        deferred-wave findings line — a placeholder ("none", "n/a",
        "TBD", bare digits or punctuation) asserts a scoped defect exists
        and that none exists (instrument §4, RD33-01; set widened
        RD34-06)
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
        (RD33-06; upgraded from containment, RD34-08; needs git, skipped
        with LG-2's notice otherwise; the missing-line case errors
        regardless)

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


DECISION_ID_RE = re.compile(r"(?:SDR|P|D|B)-\d+[a-z]?(?:\([a-z]\))?$")


def _deferral_citation_error(val, commit, _git):
    """RD34-02: the citation must be a repository path (existing at the
    named commit when git checks run) or a decision identifier — label
    wording is not a citation."""
    v = val.strip().strip("`")
    if DECISION_ID_RE.fullmatch(v):
        return None
    if "/" in v:
        if not _git or not commit:
            return None  # shape lawful; existence unverifiable without git
        if git_show(commit, v.lstrip("./")) is None:
            return (f"path {v!r} does not exist at the named commit — a "
                    "citation to nowhere authorizes nothing")
        return None
    return (f"{v!r} is neither a repository path nor a decision identifier "
            "— label wording is not a citation (RD34-02)")


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
    mtarget = re.search(r"^Launch target:\s*(\S.*)$", txt, re.M)
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
    if not re.search(r"^#+ .*G1", txt, re.M):
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
    deferred_m = re.search(r"^Deferred count[^:]*:\s*(\d+)", txt, re.M)
    reopened_m = re.search(r"^Reopened count[^:]*:\s*(\d+)", txt, re.M)
    if not deferred_m:
        errors.append("LG-5: no `Deferred count:` field — the trend row's "
                      "Deferred figure has no source; absence is an error, "
                      "never zero")
    if not reopened_m:
        errors.append("LG-5: no `Reopened count:` field — a zero Reopened "
                      "claim needs a stated count, not a missing field")
    n_deferred_decl = int(deferred_m.group(1)) if deferred_m else None

    # ---- Owner deferral citation (used by LG-6/LG-7) ----------------------
    owner_dec_m = re.search(r"^Owner deferral decision:\s*(\S.*)$", txt,
                            re.M)
    owner_dec = owner_dec_m.group(1).strip() if owner_dec_m else None
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
    mfind = re.search(
        r"^Deferred-wave findings recorded outside launch scope:\s*(.+)$",
        txt, re.M)
    if n_scoped:
        val = mfind.group(1).strip() if mfind else None
        if val is None:
            errors.append(
                f"LG-9: {n_scoped} scoped row(s) but no deferred-wave "
                "findings line — §4 requires each scoped defect named "
                "there; the disclosure is the scoped form's honesty")
        elif val.startswith("<") or re.fullmatch(
                r"(?i)[`*\s]*(?:none|n/?a|tbd|todo|pending|"
                r"not applicable|[\W\d]+)[`*.\s]*", val):
            errors.append(
                f"LG-9: {n_scoped} scoped row(s) beside a deferred-wave "
                f"findings line reading {val!r} — a placeholder names no "
                "defect; the record asserts a scoped defect exists and "
                "that none exists (instrument §4; RD34-06)")

    # ---- LG-6 / LG-7 gate verdict line ------------------------------------
    # §5's "terminal line" is the LAST match — a summary line earlier in the
    # record must not shadow it (RD34-03; the pilot record has two).
    _gv_matches = list(GATE_VERDICT_RE.finditer(txt))
    mg = _gv_matches[-1] if _gv_matches else None
    n_not = sum(1 for v in verdicts.values() if v == "Not met")
    n_unk = sum(1 for v in verdicts.values() if v == "Unknown")
    if not mg:
        errors.append("LG-6: no GATE VERDICT line found")
    else:
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

    # ---- LG-5 trend row ---------------------------------------------------
    deferred = deferred_m.group(1) if deferred_m else "—"
    reopened = reopened_m.group(1) if reopened_m else "—"
    new_vs_prior = "n/a — no prior record supplied"
    if prior_path:
        ptxt = Path(prior_path).read_text(encoding="utf-8")
        # §6 (v1.7, RD34-04): newly-Not-met rows count (incl. a scoped row
        # turning plain — it newly blocks; the r5 behavior RD-34 verified),
        # plus newly scoped rows that were no finding before under either
        # rendering — reclassification never double-counts.
        prior_rows = _row_verdicts(ptxt)
        prior_not = {q for q, v in prior_rows.items() if v == "Not met"}
        prior_scoped = {q for q, v in prior_rows.items() if v == SCOPED}
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
Instrument version: v1.7  sha256: {inst}
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

    head = _head_commit()
    if head:
        good_head = GOOD.format(sha=head, inst=inst, param=param)
        case("instrument digest mismatch rejected (git on, LG-2)",
             good_head, "digest mismatch", _git=True)
        case("instrument version disagreement rejected (RD33-06, LG-11)",
             good_head.replace("Instrument version: v1.7",
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
    else:
        print("  note  git unavailable — 3 git-dependent fixtures skipped")

    # RD33-02: a prior scoped row that turns plain Not met must count as a
    # new finding — the prior/current comparison uses one normalization.
    n_cases[0] += 1
    import tempfile
    prior_txt = good.replace(
        "| C2 | Met | x |", "| C2 | Not met (out of launch scope) | x |")
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
