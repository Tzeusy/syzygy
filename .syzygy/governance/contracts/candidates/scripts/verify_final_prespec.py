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
# owner-facing justification the charter requires (also carried in
# 03-ACTIVE-CONTRACT-COMPACTION-REPORT.md). Anything else over the ceiling
# still fails.
JUSTIFIED_OVERSIZE = {
    "rfcs/RFC-0001-project-graph-identity-state-planes.md":
        "dictionary-shaped kernel contract: 23% verbatim closed vocabularies "
        "(entity/plane/relation/four-sense tables); reader groups not "
        "distinct, so no honest split exists; floor established by two "
        "compaction passes (see 03 report)",
    "rfcs/RFC-0009/semantic-geography.md":
        "at 6,996 words (99.9% of ceiling) before round-2026-08d; the "
        "owner-ordered RFC9-8(a) amendment relocating the portfolio layout "
        "registry to the RFC10-15 workspace governance store, with its "
        "staged reference, adds the remainder; no further compaction of "
        "other clauses is available without semantic delta to reviewed text",
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

    # Context-selection fixtures: five, each with required fields + digest.
    fx = root / "fixtures"
    ctx = sorted(fx.glob("context-selection-*.md")) if fx.is_dir() else []
    if len(ctx) < 5:
        fail(f"context-selection fixtures: found {len(ctx)}, need ≥5")
    for p in ctx:
        t = p.read_text(encoding="utf-8")
        for req in ("Required context", "Omitted", "estimate", "constraint", "Suggested", "digest"):
            if req.lower() not in t.lower():
                fail(f"{p.relative_to(root)}: missing '{req}' section")

    print(f"\nactive corpus (RFC files): {total_words} words across {len(files)} modules")
    for k, v in sorted(module_words.items()):
        print(f"  {v:>6}  {k}")
    if not 0 < total_words:
        fail("word count computation failed")
    if total_words > 57000:
        note(f"total {total_words} exceeds the 35–50k target band plus new RFCs; "
             f"owner-facing justification required (charter)")

    print(f"\nnumbered clauses defined: {len(numbered_defined)}")
    for n in notes:
        print(f"note: {n}")
    if failures:
        print(f"\nFAIL — {len(failures)} finding(s):")
        for msg in failures:
            print(f"  ✗ {msg}")
        sys.exit(1)
    print("\nPASS — all checks clean")


if __name__ == "__main__":
    main()
