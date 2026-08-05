#!/usr/bin/env python3
"""Deterministically derive 05-CONTRACT-INDEX.yaml from the active contract
artifacts (front matter + clause scan). The index is a rebuildable
projection, never a second truth store (RFC11-7). Review tooling only.

Usage: build_contract_index.py [--root DIR] [--check]
  --check: regenerate and diff against the committed index; nonzero exit on drift.
"""
import argparse
import re
import sys
from pathlib import Path

CLAUSE_DEF = re.compile(r"^\*\*(RFC\d+-\d+)(\([a-z]\))?\s*(?:\.|—|—)", re.M)
# A minority of lettered limbs open their bold headline with running prose
# instead of the `.`/em-dash separator CLAUSE_DEF requires — e.g.
# `**RFC9-16(d) is owner-gated, with one narrow carve-out**`. Those are
# clause definitions and were being dropped (§20.2 semantic-preservation
# review, finding 8: RFC9-16(d) missing from the RFC-0009 clause list).
# Admitting them needs a rule that does not also swallow the many bold
# *references* that open a paragraph (`**RFC9-52 binds the package…**`,
# `**RFC3-16(a) gates four artifacts…**`). Two corpus invariants make the
# distinction deterministic: a lettered limb is defined in the same file as
# its parent clause, and a module only defines clauses of its own contract.
# So a bold-opening lettered limb counts as a definition exactly when its
# RFC number matches the file's own front-matter `id` and its parent clause
# is itself defined in that file by CLAUSE_DEF. Unlettered ids are never
# admitted this way — they carry no parent to anchor them.
LETTERED_LIMB = re.compile(r"^\*\*(RFC(\d+)-\d+)(\([a-z]\))\s", re.M)
SECTION = re.compile(r"^#{2,3}\s+(\d+)\.?\s", re.M)
LIST_VAL = re.compile(r"^\[(.*)\]$")
# The six phase-boundary clauses: marked so a selector can force the
# governing phase rule into every packet that selects the contract
# (RFC11-4; boundary-review E1).
PHASE_RULES = {"RFC6-28", "RFC7-38", "RFC8-32", "RFC9-52", "RFC10-16", "RFC11-12"}
RULE_ID = re.compile(r"\b(VIS-\d+|SEC-\d+|CC-[A-Z]+-\d+)\b")
# Non-contract governance sources, projected so deterministic selection
# metadata exists for them too (digestibility E2). Since the 2026-08-05
# tracked-candidate relocation these resolve to the canonical homes
# (relative to this package root), not packet mirrors; labels keep the
# original packet-relative names for index stability.
GOV_SOURCES = [("../../doctrine", "doctrine", "doctrine"),
               ("../../policies/craft-and-care", "craft-and-care", "craft-policy"),
               ("../../../map/topology-candidates", "topology", "topology")]


def parse_front_matter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            v = v.strip().strip('"')
            m = LIST_VAL.match(v)
            fm[k.strip()] = [x.strip() for x in m.group(1).split(",") if x.strip()] if m else v
    return fm


def clause_kind(text, pos):
    """normative = numbered clause; open-question = §8; informative = §0/§6/§7 blocks."""
    sec = None
    for m in SECTION.finditer(text[:pos]):
        sec = m.group(1)
    if sec == "8":
        return "open-question"
    if sec in ("0", "6", "7"):
        return "informative"
    return "normative"


def emit(root):
    lines = ["# CONTRACT-INDEX — generated projection; rebuild with scripts/build_contract_index.py",
             "# Authoritative metadata lives in the active contract files' front matter.",
             "contracts:"]
    rfcs = root / "rfcs"
    files = sorted(rfcs.glob("RFC-00*.md"))
    for pkg in sorted(p for p in rfcs.glob("RFC-00*") if p.is_dir()):
        files += sorted(pkg.glob("*.md"))
    by_id = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        cid = fm.get("id")
        if not cid:
            continue
        entry = by_id.setdefault(cid, {"fm": fm, "modules": [], "clauses": []})
        entry["modules"].append(str(f.relative_to(rfcs)))
        if fm.get("module"):
            entry.setdefault("module_meta", []).append(
                {"file": str(f.relative_to(rfcs)), "clauses": fm.get("clauses", "")})
        # (position, parent, full_id) so limbs admitted by the second pass
        # land in document order rather than appended after the first pass.
        found = [(m.start(), m.group(1), m.group(1) + (m.group(2) or ""))
                 for m in CLAUSE_DEF.finditer(text)]
        strict_ids = {full for _, _, full in found}
        strict_parents = {parent for _, parent, _ in found}
        own_num = cid.split("-")[-1].lstrip("0") if cid else None
        for m in LETTERED_LIMB.finditer(text):
            full_id = m.group(1) + m.group(3)
            if full_id in strict_ids or m.group(1) not in strict_parents:
                continue
            if own_num is None or m.group(2).lstrip("0") != own_num:
                continue
            found.append((m.start(), m.group(1), full_id))
        for pos, parent, full_id in sorted(found):
            kind = "phase-rule" if parent in PHASE_RULES \
                else clause_kind(text, pos)
            entry["clauses"].append((full_id, str(f.relative_to(rfcs)), kind))
    for cid in sorted(by_id):
        e = by_id[cid]
        fm = e["fm"]
        lines.append(f"  - id: {cid}")
        if isinstance(fm.get("title"), str):
            lines.append(f"    title: {fm['title']}")
        lines.append("    status_source: owner-act-record")
        for key in ("governs", "applies_to", "depends_on", "provides_to", "tags"):
            val = fm.get(key)
            if isinstance(val, list):
                lines.append(f"    {key}: [{', '.join(val)}]")
        lines.append(f"    modules: [{', '.join(e['modules'])}]")
        if e.get("module_meta"):
            lines.append("    module_ranges:")
            for mm in e["module_meta"]:
                lines.append(f"      - {{file: {mm['file']}, clauses: \"{mm['clauses']}\"}}")
        lines.append("    clauses:")
        seen = set()
        for cl, mod, kind in e["clauses"]:
            if cl in seen:
                continue
            seen.add(cl)
            lines.append(f"      - {{id: {cl}, module: {mod}, kind: {kind}}}")
    lines.append("# Non-contract governance sources (read from the canonical homes;")
    lines.append("# selection metadata only — the canonical homes stay authoritative):")
    lines.append("governance_sources:")
    for dirpath, dirname, role in GOV_SOURCES:
        d = (root / dirpath).resolve()
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            ids = sorted(set(RULE_ID.findall(text)),
                         key=lambda s: (s.rsplit("-", 1)[0], int(s.rsplit("-", 1)[1])))
            words = len(text.split())
            lines.append(f"  - {{file: {dirname}/{f.name}, role: {role}, words: {words}"
                         + (f", rule_ids: [{', '.join(ids)}]" if ids else "") + "}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    out = root / "05-CONTRACT-INDEX.yaml"
    generated = emit(root)
    if args.check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != generated:
            print("DRIFT: 05-CONTRACT-INDEX.yaml differs from regeneration")
            sys.exit(1)
        print("index matches regeneration — no drift")
    else:
        out.write_text(generated, encoding="utf-8")
        print(f"wrote {out} ({len(generated.splitlines())} lines)")


if __name__ == "__main__":
    main()
