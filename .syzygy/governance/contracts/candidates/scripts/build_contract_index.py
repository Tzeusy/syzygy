#!/usr/bin/env python3
"""Deterministically derive 05-CONTRACT-INDEX.yaml from the active contract
artifacts (front matter + clause scan). The index is a rebuildable
projection, never a second truth store (RFC11-7). Review tooling only.

Usage: build_contract_index.py [--root DIR] [--check] [--selftest]
  --check:    regenerate and diff against the committed index; nonzero exit
              on drift. States its population — review RD-17 finding 13: a
              corpus that lost its front matter would regenerate to a
              smaller index and `--check` would still print "no drift".
  --selftest: mutate a copy per predicate class and confirm --check fails.
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


#: The one nested block this projection reads. Review RD-12 finding 11:
#: RFC11-4 names this index as a deterministic *selection input* and says the
#: mandatory set always includes what a contract's implementation-boundary
#: declaration names (RFC11-13), "consumed from the contract's own index" —
#: and the projection carried **0 occurrences** of `implementation_boundary`
#: across 540 lines. No clause was violated (RFC11-13 locates the
#: declaration in the governed artifact), but a selector working from the
#: projection had to open eleven package READMEs for a field the projection
#: could carry, which is friction pointed straight at the clause with the
#: least tolerance for it. 11 of 11 contracts declare it.
NESTED_BLOCKS = ("implementation_boundary",)
NESTED_KEY = re.compile(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$")


def parse_front_matter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    fm = {}
    block = None
    for line in text[4:end].splitlines():
        if block is not None:
            m = NESTED_KEY.match(line)
            if m:
                fm[block][m.group(1)] = m.group(2).strip().strip('"')
                continue
            block = None
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip().strip('"')
            if k in NESTED_BLOCKS and not v:
                fm[k] = {}
                block = k
                continue
            m = LIST_VAL.match(v)
            fm[k] = [x.strip() for x in m.group(1).split(",") if x.strip()] if m else v
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
        entry = by_id.setdefault(cid, {"fm": fm, "modules": [], "clauses": [],
                                       "constrains": [], "constrains_source": "",
                                       "boundary": {}, "boundary_file": ""})
        entry["modules"].append(str(f.relative_to(rfcs)))
        # Declared on exactly one module per contract (the package index, or
        # the single file). Projected with the file it was read from, so the
        # projection points at the governed artifact rather than replacing it.
        ib = fm.get("implementation_boundary")
        if isinstance(ib, dict) and ib and not entry["boundary"]:
            entry["boundary"] = ib
            entry["boundary_file"] = str(f.relative_to(rfcs))
        # `constrains` is declared on the module whose clause states the
        # restriction, never on the package README — a README defines no
        # clauses, so an anchor declared there cannot be verified. The
        # contract-level value is therefore the union of its modules', in
        # declaration order, and is derived here rather than transcribed.
        for t in fm.get("constrains", []):
            if t not in entry["constrains"]:
                entry["constrains"].append(t)
        if isinstance(fm.get("constrains_source"), str) and fm["constrains_source"]:
            entry["constrains_source"] = fm["constrains_source"]
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
        # `provides_to` is gone from every module's front matter (it is derived
        # by reversal in build_dependency_index.py) and is kept in this loop's
        # key list only so that a module re-introducing it by hand is still
        # projected rather than silently dropped. `constrains` and its clause
        # anchor are projected because RFC11-4 names this index as a selection
        # input, and a relation absent from the selector's declared inputs is a
        # relation no selector reads — review RD-4, finding F-14.
        for key in ("governs", "applies_to", "depends_on", "provides_to",
                    "tags"):
            val = fm.get(key)
            if isinstance(val, list):
                lines.append(f"    {key}: [{', '.join(val)}]")
        if e["constrains"]:
            lines.append(f"    constrains: [{', '.join(e['constrains'])}]")
        if e["constrains_source"]:
            lines.append(f"    constrains_source: {e['constrains_source']}")
        if e["boundary"]:
            b = e["boundary"]
            lines.append("    implementation_boundary:")
            for k in sorted(b):
                lines.append(f"      {k}: {b[k]}")
            lines.append(f"      declared_in: {e['boundary_file']}")
        else:
            # Absence is projected, not omitted: a contract that lost the
            # declaration RFC11-4 depends on must be visible here as
            # Unknown, never as a row that simply has one fewer key.
            lines.append("    implementation_boundary: "
                         "[Unknown] — no declaration found in this "
                         "contract's front matter")
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


def population(root, generated):
    """The denominator `--check` states, computed from the generated text.

    A module with no front-matter `id` is skipped by `emit()` (there is
    nothing to key it by), so a corpus that lost its front matter would
    regenerate to a *smaller* index and a bare "no drift" would be true and
    useless. Both counts print, so the shrink is visible.
    """
    rfcs = root / "rfcs"
    files = sorted(rfcs.glob("RFC-00*.md"))
    for pkg in sorted(p for p in rfcs.glob("RFC-00*") if p.is_dir()):
        files += sorted(pkg.glob("*.md"))
    keyed = sum(1 for f in files
                if parse_front_matter(f.read_text(encoding="utf-8")).get("id"))
    contracts = sum(1 for ln in generated.splitlines()
                    if ln.startswith("  - id: "))
    clauses = sum(1 for ln in generated.splitlines()
                  if ln.lstrip().startswith("- {id: RFC"))
    boundaries = sum(1 for ln in generated.splitlines()
                     if ln.strip().startswith("implementation_boundary:")
                     and "[Unknown]" not in ln)
    return (f"{contracts} contract(s), {keyed} of {len(files)} module(s) "
            f"carry a front-matter id, {clauses} clause(s), "
            f"{boundaries} implementation-boundary declaration(s)")


def selftest(root):
    """Mutate a copy per predicate class; confirm the regeneration differs.

    Review RD-17 finding 13: this script shipped no fixture at all, so its
    green `--check` was a claim nobody had seen fail. Three classes, because
    one comparison covering three can pass on the shape it happens to see.
    """
    import shutil
    import tempfile
    cases = []
    base = emit(root)

    def mutated(rel, fn, label):
        d = Path(tempfile.mkdtemp(prefix="index-selftest-"))
        try:
            shutil.copytree(root / "rfcs", d / "rfcs")
            p = d / rel
            p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")
            after = emit(d)
            cases.append((label, after != base))
            return after
        finally:
            shutil.rmtree(d, ignore_errors=True)

    first_pkg = sorted(p for p in (root / "rfcs").glob("RFC-00*")
                       if p.is_dir())[0]
    readme = f"rfcs/{first_pkg.name}/README.md"

    # 1. A dropped front-matter id removes a whole module from the index.
    mutated(readme, lambda t: t.replace("\nid: ", "\nid_was: ", 1),
            "dropped front-matter id changes the projection")
    # 2. A dropped implementation_boundary must show as [Unknown], not vanish.
    after = mutated(readme,
                    lambda t: t.replace("implementation_boundary:",
                                        "implementation_boundary_was:", 1),
                    "dropped implementation_boundary changes the projection")
    cases.append(("dropped implementation_boundary renders [Unknown]",
                  "[Unknown]" in (after or "")))
    # 3. A clause definition removed must leave the clause list.
    mods = [p for p in sorted(first_pkg.glob("*.md")) if p.name != "README.md"]
    if mods:
        rel = f"rfcs/{first_pkg.name}/{mods[0].name}"
        mutated(rel, lambda t: re.sub(r"^\*\*(RFC\d+-\d+)", r"__\1", t,
                                      count=1, flags=re.M),
                "removed clause definition changes the projection")
    else:
        cases.append(("removed clause definition changes the projection",
                      False))

    ok = True
    for label, passed in cases:
        print(f"SELFTEST {'OK' if passed else 'FAIL'}: {label}")
        ok = ok and passed
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    if args.selftest:
        sys.exit(selftest(root))
    out = root / "05-CONTRACT-INDEX.yaml"
    generated = emit(root)
    pop = population(root, generated)
    if args.check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != generated:
            print("DRIFT: 05-CONTRACT-INDEX.yaml differs from regeneration")
            print(f"population: {pop}")
            sys.exit(1)
        print(f"index matches regeneration — no drift over {pop}")
    else:
        out.write_text(generated, encoding="utf-8")
        print(f"wrote {out} ({len(generated.splitlines())} lines) — {pop}")


if __name__ == "__main__":
    main()
