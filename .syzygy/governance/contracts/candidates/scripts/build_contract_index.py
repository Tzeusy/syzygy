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
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_final_prespec import PHASE_RULE_CLAUSES  # noqa: E402

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
# The phase-boundary clauses: marked so a selector can force the governing
# phase rule into every packet that selects the contract (RFC11-4;
# boundary-review E1). **Read from the verifier, never typed here.** This
# file kept its own six while `verify_final_prespec.py` listed eleven, so
# the five round-2026-08d phase rules (RFC1-33, RFC2-26, RFC3-33, RFC4-30,
# RFC5-27) were indexed `normative` (review RD-6 E-3/C-1, F-3 row 2).
PHASE_RULES = frozenset(PHASE_RULE_CLAUSES)
# The section-number convention `clause_kind` applies, stated once here and
# printed into the generated header from this same mapping, so the
# convention is visible to an index reader rather than living only in code
# (RD-6 F-3 row 10). A section absent from the mapping is `normative`.
SECTION_KINDS = {"0": "informative", "6": "informative", "7": "informative",
                 "8": "open-question"}
# The field that speaks to authority, projected from front matter like every
# sibling key (RD-6 C-1, F-3 row 9). Its absence or disagreement across a
# contract's modules is rendered [Unknown] and fails `--check`.
STATUS_KEY = "status_source"
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
    """The kind SECTION_KINDS gives the clause's enclosing §-number, else normative."""
    sec = None
    for m in SECTION.finditer(text[:pos]):
        sec = m.group(1)
    return SECTION_KINDS.get(sec, "normative")


def header():
    """The generated banner: non-authority, then the conventions applied."""
    by_kind = {}
    for sec, kind in sorted(SECTION_KINDS.items(), key=lambda kv: int(kv[0])):
        by_kind.setdefault(kind, []).append(f"§{sec}")
    order = sorted(PHASE_RULES, key=lambda c: tuple(int(x) for x in re.findall(r"\d+", c)))
    return [
        "# CONTRACT-INDEX — generated projection; rebuild with scripts/build_contract_index.py",
        "# Authoritative metadata lives in the active contract files' front matter.",
        "#",
        "# NOT AUTHORITY. This candidate-lane projection binds nothing and states no",
        "# contract's acceptance: a contract's effective standing is whatever the",
        "# owner act record its `status_source` names says, never this file (RFC11-7).",
        f"# `{STATUS_KEY}` is read from each module's front matter; a contract whose",
        "# modules omit it or disagree shows [Unknown] here and fails --check.",
        "#",
    ] + ["# " + ln for ln in textwrap.wrap(
        "clause kind: phase-rule for a clause or limb of " + ", ".join(order)
        + "; otherwise by the enclosing section number — "
        + "; ".join(f"{', '.join(secs)} {kind}" for kind, secs in by_kind.items())
        + "; any other section normative.", width=76, break_on_hyphens=False)]


def emit(root):
    lines = header() + ["contracts:"]
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
                                       "boundary": {}, "boundary_file": "",
                                       "status": {}})
        entry["modules"].append(str(f.relative_to(rfcs)))
        status = fm.get(STATUS_KEY)
        entry["status"][str(f.relative_to(rfcs))] = \
            status if isinstance(status, str) and status else None
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
        lines.append(f"    {STATUS_KEY}: {status_projection(e['status'])}")
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


def status_projection(per_module):
    """One value when every module declares the same one; else [Unknown] with why."""
    values = set(per_module.values())
    if len(values) == 1 and None not in values:
        return values.pop()
    missing = sorted(m for m, v in per_module.items() if v is None)
    declared = sorted(v for v in values if v is not None)
    why = []
    if missing:
        why.append(f"{len(missing)} of {len(per_module)} module(s) declare none")
    if len(declared) > 1:
        why.append("modules disagree: " + ", ".join(declared))
    return "[Unknown] — " + "; ".join(why)


def status_mismatches(generated):
    return [ln.strip() for ln in generated.splitlines()
            if ln.startswith(f"    {STATUS_KEY}: [Unknown]")]


def check_findings(current, generated):
    """What `--check` fails on: drift, and every status_source it could not project."""
    findings = []
    if current != generated:
        findings.append("DRIFT: 05-CONTRACT-INDEX.yaml differs from regeneration")
    findings += [f"STATUS MISMATCH: {line}" for line in status_mismatches(generated)]
    return findings


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
    phase = sum(1 for ln in generated.splitlines()
                if ln.lstrip().startswith("- {id: RFC") and ln.endswith("kind: phase-rule}"))
    projected = contracts - len(status_mismatches(generated))
    return (f"{contracts} contract(s), {keyed} of {len(files)} module(s) "
            f"carry a front-matter id, {clauses} clause(s), "
            f"{boundaries} implementation-boundary declaration(s), "
            f"{phase} phase-rule clause(s) over {len(PHASE_RULES)} shared rule(s), "
            f"{STATUS_KEY} projected for {projected} of {contracts}")


def selftest(root):
    """Mutate a copy per predicate class; confirm the regeneration differs.

    Review RD-17 finding 13: this script shipped no fixture at all, so its
    green `--check` was a claim nobody had seen fail. One case per predicate
    class, because one comparison covering several can pass on the shape it
    happens to see; review RD-6 E-3/C-1 and F-3 rows 2, 9 and 10 added the
    status_source, phase-rule and header classes.
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

    # 4. A module whose status_source differs is reported, never overwritten
    #    (RD-6 C-1): the contract's row turns [Unknown] and names both values.
    after = mutated(readme,
                    lambda t: t.replace(f"\n{STATUS_KEY}: owner-act-record",
                                        f"\n{STATUS_KEY}: self-declared", 1),
                    "a divergent status_source changes the projection")
    cases.append(("a divergent status_source renders [Unknown] naming both values",
                  any("disagree: owner-act-record, self-declared" in ln
                      for ln in status_mismatches(after or ""))))
    cases.append(("--check fails on a mismatch even when the committed index agrees",
                  any(f.startswith("STATUS MISMATCH")
                      for f in check_findings(after or "", after or ""))))
    # 5. A module that drops status_source is counted, not papered over.
    after = mutated(readme,
                    lambda t: t.replace(f"\n{STATUS_KEY}:", f"\n{STATUS_KEY}_was:", 1),
                    "a dropped status_source changes the projection")
    cases.append(("a dropped status_source renders [Unknown] with its count",
                  any("module(s) declare none" in ln
                      for ln in status_mismatches(after or ""))))
    # 6. Every shared phase rule is indexed phase-rule, the five round-2026-08d
    #    rules included (RD-6 F-3 row 2), and nothing else is.
    phase = {ln.split("id: ", 1)[1].split(",", 1)[0].split("(", 1)[0]
             for ln in base.splitlines()
             if ln.lstrip().startswith("- {id: RFC") and ln.endswith("kind: phase-rule}")}
    cases.append(("the indexed phase-rule set is exactly the shared list",
                  phase == set(PHASE_RULE_CLAUSES)))
    cases.append(("the five round-2026-08d phase rules are indexed phase-rule",
                  {"RFC1-33", "RFC2-26", "RFC3-33", "RFC4-30", "RFC5-27"} <= phase))
    # 7. The banner and the clause-kind convention are in the generated header,
    #    and the convention line is derived from SECTION_KINDS and PHASE_RULES.
    head = base.split("\ncontracts:\n", 1)[0]
    cases.append(("the header carries the non-authority banner",
                  "NOT AUTHORITY." in head and "binds nothing" in head))
    cases.append(("the header states every section-kind and phase rule it applies",
                  all(f"§{sec}" in head for sec in SECTION_KINDS)
                  and all(kind in head for kind in SECTION_KINDS.values())
                  and all(rule in head for rule in PHASE_RULE_CLAUSES)))

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
        findings = check_findings(current, generated)
        if findings:
            for finding in findings:
                print(finding)
            print(f"population: {pop}")
            sys.exit(1)
        print(f"index matches regeneration — no drift over {pop}")
    else:
        out.write_text(generated, encoding="utf-8")
        print(f"wrote {out} ({len(generated.splitlines())} lines) — {pop}")


if __name__ == "__main__":
    main()
