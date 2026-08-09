#!/usr/bin/env python3
"""Portable mechanical verification for the rev10 final pre-specification
package. Review tooling only — not application code (directive §11).

Root resolution: --root <dir>, else the script's own grandparent
(scripts/ lives directly under final-prespec/). No absolute-path
assumptions; every claim re-runnable from the delivered packet.
"""
import argparse
import re
import sys
from pathlib import Path

# Accepts both marker styles: '**RFCn-m.**' (rev9) and '**RFCn-m — Title.**'
# (rev10 compacted), anchored at line start so bold in-text citations don't
# count as definitions.
CLAUSE_DEF = re.compile(r"^\*\*(RFC(\d+)-(\d+))(\([a-z]\))?\s*(?:\.|—|—)", re.M)
CLAUSE_REF = re.compile(r"\bRFC(\d+)-(\d+)\b")
# A live History parenthetical, not a backtick-quoted mention of the form.
HISTORY_PAREN = re.compile(r"(?<!`)\*\(History:")

# Modules allowed above the ~7,000-word default-load ceiling, each with the
# owner-facing justification the charter requires. Anything else over the
# ceiling still fails.
#
# **No justification here states a word count.** The verifier prints the
# computed figure on the same line as the justification, so a number written
# into these strings is a second copy of a measurement whose home is the run
# that produced it — and both entries had already gone stale that way: one
# said "6,996 words" of a module that had grown past 7,700, the other pinned
# a floor the module has since been ordered to grow above. A justification
# explains *why the size is the size*; the size itself is measured.
JUSTIFIED_OVERSIZE = {
    "rfcs/RFC-0001-project-graph-identity-state-planes.md":
        "dictionary-shaped kernel contract: roughly a quarter of it is "
        "verbatim closed vocabularies (entity/plane/relation/four-sense "
        "tables), and its reader groups are not distinct, so no honest split "
        "exists. Two compaction passes established a floor, recorded as of "
        "their date in the historical `03-ACTIVE-CONTRACT-COMPACTION-REPORT"
        ".md`; the growth above that floor is review-ordered clause addition "
        "(the RFC1-33 phase rule and the round-2026-08e per-consequence "
        "paragraphs, per `round-2026-08e/WAVE-A-SEMANTIC-DELTA.md`), not "
        "padding",
    "rfcs/RFC-0009/semantic-geography.md":
        "sat just under the ceiling before round-2026-08d and was carried "
        "over it by the owner-ordered RFC9-8(a) amendment, which homes the "
        "portfolio layout registry on RFC3-15/RFC3-16(a) — in-wave, and no "
        "longer the cross-wave RFC10-15 reliance an earlier revision of this "
        "sentence described (RFC10-15 survives as a stated citation, not a "
        "reliance). No further compaction of other clauses is available "
        "without a semantic delta to reviewed text",
}

# Rev9 baseline: authoritative numbered-clause ends per RFC (frozen facts;
# see FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md §3 of the rev9 package).
REV9_ENDS = {1: 32, 2: 25, 3: 32, 4: 29, 5: 26, 6: 28, 7: 38, 8: 32, 9: 52}
# Rev10 new contracts and their expected ends. RFC-0010 extended to 22 at
# rev11: the correction plane (RFC10-17..22) closing the post-failure seams
# an adversarial safety review found open. Nothing was renumbered or retired,
# so the range only grows — see RFC-0010 §5a.
REV10_ENDS = {10: 22, 11: 12}
# Round-2026-08d structural closure (owner work order): clauses appended,
# never renumbered. Phase rules RFC1-33/RFC2-26/RFC3-33/RFC4-30/RFC5-27
# (RD-5 disposition); RFC7-39/40 (fixed human entry, front-door
# discoverability); RFC10-23/24 (effect dimensions, D3 operating
# precondition); RFC11-13..16 (deterministic-selection module).
ROUND_08D_ENDS = {1: 33, 2: 26, 3: 33, 4: 30, 5: 27, 7: 40, 10: 24, 11: 16}
ENDS = {**REV9_ENDS, **REV10_ENDS, **ROUND_08D_ENDS}

# Packages (split RFCs) are discovered as rfcs/RFC-00NN/ directories; clause
# ownership is validated from actual definitions per module (each clause in
# exactly one module, union complete), with front-matter 'clauses:' declared
# ranges cross-checked where they parse.
PHASE_RULE_CLAUSES = ["RFC1-33", "RFC2-26", "RFC3-33", "RFC4-30", "RFC5-27",
                      "RFC6-28", "RFC7-38", "RFC8-32", "RFC9-52", "RFC10-16",
                      "RFC11-12"]
OUTCOMES = (
    "retained unchanged",
    "retained with wording sharpened",
    "merged into",
    "moved to rationale/history",
    "routed to OpenSpec candidate",
    "routed to craft-and-care",
    "retired as superseded/redundant",
    "new at rev10",
    "open — retained",
    "answered — moved to history",
)

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def note(msg):
    notes.append(msg)


def parse_front_matter(text, path):
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML front matter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        fail(f"{path}: unterminated front matter")
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def active_files(root):
    rfcs = root / "rfcs"
    files = sorted(rfcs.glob("RFC-00*.md"))
    for pkg in sorted(rfcs.glob("RFC-00*/")):
        files += sorted(pkg.glob("*.md"))
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = ap.parse_args()
    root = args.root.resolve()
    print(f"root: {root}")

    files = active_files(root)
    if not files:
        fail("no active RFC files found under rfcs/")

    defined = {}          # clause id -> file
    per_rfc_nums = {}     # rfc number -> set of clause numbers
    total_words = 0
    module_words = {}

    for f in files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(root)
        words = len(text.split())
        module_words[str(rel)] = words
        total_words += words
        if words > 7000:
            if str(rel) in JUSTIFIED_OVERSIZE:
                note(f"{rel}: {words} words over the 7,000 ceiling — "
                     f"JUSTIFIED: {JUSTIFIED_OVERSIZE[str(rel)]}")
            else:
                fail(f"{rel}: {words} words exceeds the 7,000-word module ceiling")
        fm = parse_front_matter(text, rel)
        for key in ("id", "status_source"):
            if key not in fm:
                fail(f"{rel}: front matter missing '{key}'")
        if fm.get("status_source") not in (None, "owner-act-record"):
            fail(f"{rel}: status_source is '{fm.get('status_source')}'")
        if HISTORY_PAREN.search(text):
            fail(f"{rel}: '*(History:' parenthetical remains in active file")
        for m in CLAUSE_DEF.finditer(text):
            cid, rfc_n, num, letter = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
            key = cid + (letter or "")
            if key in defined and not letter:
                fail(f"{rel}: duplicate definition of {key} (also in {defined[key]})")
            defined.setdefault(key, rel)
            per_rfc_nums.setdefault(rfc_n, set()).add(num)

    # Clause continuity per RFC (gaps allowed only when declared in front
    # matter 'clauses:' line of the owning file — checked as merged/retired
    # mentions in the migration matrix below).
    matrix = (root / "04-CLAUSE-MIGRATION-MATRIX.md")
    matrix_text = matrix.read_text(encoding="utf-8") if matrix.exists() else ""
    if not matrix_text:
        fail("04-CLAUSE-MIGRATION-MATRIX.md missing or empty")

    for rfc_n, end in ENDS.items():
        nums = per_rfc_nums.get(rfc_n, set())
        if not nums:
            fail(f"RFC{rfc_n}: no clauses found in active files")
            continue
        expected = set(range(1, end + 1))
        missing = expected - nums
        extra = nums - expected
        for n in sorted(missing):
            cid = f"RFC{rfc_n}-{n}"
            pat = re.compile(rf"\|\s*{re.escape(cid)}[^|]*\|\s*(merged into|retired as|moved to rationale/history|routed to)")
            if not pat.search(matrix_text):
                fail(f"{cid}: absent from active files and not accounted "
                     f"for (merged/retired/moved/routed) in the migration matrix")
            else:
                note(f"{cid}: gap accounted for in migration matrix")
        if extra:
            fail(f"RFC{rfc_n}: clause numbers beyond declared end {end}: {sorted(extra)}")

    # Package validation: for each rfcs/RFC-00NN/ directory, every clause of
    # that RFC is defined in exactly one module, the union is complete over
    # 1..end (minus matrix-accounted gaps), and a README with a module map
    # exists. Declared front-matter clause sets are cross-checked where
    # parseable: 'RFCn-a..RFCn-b' ranges plus singleton 'RFCn-m' entries
    # (non-contiguous module maps, round-2026-08d). A singleton token is any
    # clause identifier not inside a range match.
    range_pat = re.compile(r"RFC(\d+)-(\d+)\.\.RFC\1-(\d+)")
    single_pat = re.compile(r"RFC(\d+)-(\d+)")
    for pkg in sorted(p for p in (root / "rfcs").glob("RFC-00*") if p.is_dir()):
        rfc_n = int(pkg.name.split("-")[1])
        end = ENDS.get(rfc_n)
        readme = pkg / "README.md"
        if not readme.exists():
            fail(f"{pkg.name}: package README.md missing")
        seen = {}
        for p in sorted(pkg.glob("*.md")):
            if p.name == "README.md":
                continue
            text = p.read_text(encoding="utf-8")
            fm = parse_front_matter(text, p.relative_to(root))
            declared = set()
            clauses_fm = fm.get("clauses", "")
            range_spans = []
            for mm in range_pat.finditer(clauses_fm):
                range_spans.append(mm.span())
                if int(mm.group(1)) == rfc_n:
                    declared.update(range(int(mm.group(2)), int(mm.group(3)) + 1))
            for mm in single_pat.finditer(clauses_fm):
                if any(a <= mm.start() and mm.end() <= b for a, b in range_spans):
                    continue
                if int(mm.group(1)) == rfc_n:
                    declared.add(int(mm.group(2)))
            for m in CLAUSE_DEF.finditer(text):
                if int(m.group(2)) != rfc_n:
                    continue
                n = int(m.group(3))
                if n in seen and seen[n] != p.name and not m.group(4):
                    fail(f"RFC{rfc_n}-{n}: defined in both {seen[n]} and {p.name}")
                seen.setdefault(n, p.name)
                if declared and n not in declared:
                    fail(f"{pkg.name}/{p.name}: defines RFC{rfc_n}-{n} outside "
                         f"declared clause set")
        if end:
            missing = set(range(1, end + 1)) - set(seen)
            for n in sorted(missing):
                cid = f"RFC{rfc_n}-{n}"
                pat = re.compile(rf"\|\s*{re.escape(cid)}[^|]*\|\s*(merged into|retired as|moved to rationale/history|routed to)")
                if not pat.search(matrix_text):
                    fail(f"{pkg.name}: {cid} in no module and unaccounted in matrix")
    if not (root / "rfcs" / "RFC-0009").is_dir():
        fail("rfcs/RFC-0009/ package directory missing (owner-ordered split)")

    # Citation resolution across active files + migration-matrix outcome vocab.
    numbered_defined = {k for k in defined if "(" not in k}
    for f in files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(root)
        for m in CLAUSE_REF.finditer(text):
            rfc_n, num = int(m.group(1)), int(m.group(2))
            if rfc_n not in ENDS:
                fail(f"{rel}: citation to unknown contract RFC{rfc_n}-{num}")
                continue
            cid = f"RFC{rfc_n}-{num}"
            if cid not in numbered_defined:
                pat = re.compile(rf"\|\s*{re.escape(cid)}[^|]*\|\s*merged into\s*(RFC\d+-\d+)")
                mm = pat.search(matrix_text)
                if mm:
                    fail(f"{rel}: cites {cid}, which was merged into {mm.group(1)} — update citation")
                else:
                    fail(f"{rel}: unresolved citation {cid}")

    # Migration matrix rows use only the closed outcome vocabulary.
    for line in matrix_text.splitlines():
        if line.startswith("| RFC") and "|" in line[2:]:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and not any(cells[1].startswith(o) for o in OUTCOMES):
                fail(f"matrix row for {cells[0]}: outcome '{cells[1]}' not in closed vocabulary")

    # Phase-rule clauses present.
    for cid in PHASE_RULE_CLAUSES:
        if cid not in numbered_defined:
            fail(f"phase-rule clause {cid} not found in active files")

    # Context-selection fixtures: the population is measured, and every
    # member carries the required sections.
    #
    # **The floor is gone.** It read `need ≥5` with a comment saying "five",
    # against a population that has been ten since the round-2026-08d split
    # (review RD-23, m3). A transcribed floor is the class this package keeps
    # paying for, and a floor derived from the population it is checking
    # verifies nothing anyway. What is checkable is that the directory is not
    # empty — an empty one makes RFC-0011 module 2's acceptance criterion
    # unreachable — and that every fixture present is complete. The count is
    # printed so a shrinking population is visible rather than inferred.
    fx = root / "fixtures"
    ctx = sorted(fx.glob("context-selection-*.md")) if fx.is_dir() else []
    fixture_sections = ("Required context", "Omitted", "estimate",
                        "constraint", "Suggested", "digest")
    if not ctx:
        fail("context-selection fixtures: none found — RFC-0011 module 2's "
             "acceptance criterion is stated over this population")
    for p in ctx:
        t = p.read_text(encoding="utf-8")
        for req in fixture_sections:
            if req.lower() not in t.lower():
                fail(f"{p.relative_to(root)}: missing '{req}' section")
    note(f"context-selection fixtures: {len(ctx)} examined × "
         f"{len(fixture_sections)} required section(s)")

    print(f"\nactive corpus (RFC files): {total_words} words across {len(files)} modules")
    for k, v in sorted(module_words.items()):
        print(f"  {v:>6}  {k}")
    if not 0 < total_words:
        fail("word count computation failed")
    if total_words > 57000:
        note(f"total {total_words} exceeds the 35–50k target band plus new RFCs; "
             f"owner-facing justification required (charter)")

    print(f"\nnumbered clauses defined: {len(numbered_defined)}")
    # Every summary line states its denominator — the constraint
    # `check_governance.py` holds itself to, applied here after review RD-17
    # finding 13 observed that this script's `PASS — all checks clean` stated
    # no population at all.
    print(f"population: {len(files)} module(s), {len(ENDS)} contract(s) with "
          f"a declared clause end, {len(PHASE_RULE_CLAUSES)} phase-rule "
          f"clause(s), {len(numbered_defined)} numbered clause identities")
    for n in notes:
        print(f"note: {n}")
    if failures:
        print(f"\nFAIL — {len(failures)} finding(s):")
        for msg in failures:
            print(f"  ✗ {msg}")
        return 1
    print("\nPASS — all checks clean")
    return 0


def selftest(root):
    """Mutate a copy per predicate class; confirm `main()` fails on it.

    Review RD-17 finding 13: this script shipped no fixture. Its predicates
    *do* fail under mutation — the reviewer proved it by hand — but a check
    proved only in someone else's scratch clone is not evidence the battery
    carries (verification rule 6).

    Each case runs the whole verifier against a mutated copy and asserts a
    nonzero return. `failures`/`notes` are module-level, so they are cleared
    between runs.
    """
    import io
    import contextlib
    import re as _re
    import shutil
    import tempfile
    global failures, notes
    cases = []

    def run(d):
        failures, notes = [], []
        globals()["failures"], globals()["notes"] = failures, notes
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main_with_root(Path(d))
        return rc, buf.getvalue()

    def case(label, rel, fn, want_fail=True):
        d = tempfile.mkdtemp(prefix="prespec-selftest-")
        try:
            shutil.copytree(root / "rfcs", Path(d) / "rfcs")
            for extra in ("04-CLAUSE-MIGRATION-MATRIX.md",):
                if (root / extra).exists():
                    shutil.copy(root / extra, Path(d) / extra)
            if (root / "fixtures").is_dir():
                shutil.copytree(root / "fixtures", Path(d) / "fixtures")
            if rel is not None:
                p = Path(d) / rel
                p.write_text(fn(p.read_text(encoding="utf-8")),
                             encoding="utf-8")
            elif fn is not None:
                fn(Path(d))
            rc, _out = run(d)
            cases.append((label, (rc != 0) == want_fail))
        finally:
            shutil.rmtree(d, ignore_errors=True)

    files = active_files(root)
    victim = str(files[0].relative_to(root))

    # The baseline must pass, or every mutation below proves nothing.
    case("unmutated copy verifies clean", None, None, want_fail=False)
    # 1. A citation to a clause no module defines.
    case("unresolved clause citation detected", victim,
         lambda t: t + "\n\nSee RFC1-999 for the rule.\n")
    # 2. Front matter stripped of its id.
    case("missing front-matter id detected", victim,
         lambda t: t.replace("\nid: ", "\nid_was: ", 1))
    # 3. A live History parenthetical returning to an active file.
    case("live History parenthetical detected", victim,
         lambda t: t + "\n*(History: this was rev9 text.)*\n")
    # 4. The whole fixture population removed — the acceptance criterion of
    #    RFC-0011 module 2 is stated over it, so zero is a failure and the
    #    stale `need ≥5` floor is not what makes it one.
    case("empty fixture population detected", None,
         lambda d: shutil.rmtree(d / "fixtures", ignore_errors=True))
    # 5. A required section removed from one fixture.
    fx = sorted((root / "fixtures").glob("context-selection-*.md")) \
        if (root / "fixtures").is_dir() else []
    if fx:
        case("fixture missing a required section detected",
             f"fixtures/{fx[0].name}",
             lambda t: _re.sub(r"Omitted", "Left out", t, flags=_re.I))
    else:
        cases.append(("fixture missing a required section detected", False))

    ok = True
    for label, passed in cases:
        print(f"SELFTEST {'OK' if passed else 'FAIL'}: {label}")
        ok = ok and passed
    return 0 if ok else 1


def main_with_root(root):
    """`main()` against an explicit root, for `--selftest`."""
    import sys as _sys
    argv = _sys.argv
    _sys.argv = [argv[0], "--root", str(root)]
    try:
        return main()
    finally:
        _sys.argv = argv


if __name__ == "__main__":
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", type=Path,
                    default=Path(__file__).resolve().parent.parent)
    known, _rest = ap.parse_known_args()
    if known.selftest:
        sys.exit(selftest(known.root.resolve()))
    sys.exit(main())
