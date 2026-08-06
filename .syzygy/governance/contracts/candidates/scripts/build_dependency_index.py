#!/usr/bin/env python3
"""Deterministically derive CONTRACT-DEPENDENCY-INDEX.md from the active
contract modules' YAML front matter. The index is a rebuildable projection,
never a second truth store (RFC11-7): every row restates what a module already
declares, and the module wins wherever they disagree.

**Three relations, not one.** Overloading `depends_on` was the defect owner
item P-21 named: it was carrying load obligations, one-way semantic
constraints, and ordinary citations at once, and a selector cannot tell them
apart. They are now distinct, and each has exactly one source of truth:

    depends_on   Contract A must be loaded to interpret or modify B
                 correctly. AUTHORED on the dependent (B declares it).
                 Inverse `provides_to` is DERIVED by reversal.

    constrains   A places a semantic restriction on something B owns, while
                 B stays independently understandable without loading A in
                 every task. AUTHORED on the constraining contract — A is the
                 one whose text states the restriction, and requiring B to
                 acknowledge it is what left the two known cases enforced by
                 neither. Inverse `constrained_by` is DERIVED by reversal.

    cites        A refers to a clause of B for navigation, comparison, or a
                 forward pointer, implying neither load obligation nor
                 ownership. FULLY DERIVED from a clause-reference scan of the
                 module bodies, minus whatever `depends_on` already covers.
                 Authoring it would create a third hand-maintained edge set
                 to go stale; deriving it means a new citation appears in the
                 index the moment the prose does.

**No relation has two authored directions.** Two independently authored views
of one edge set can disagree, and did — 20 asymmetric `depends_on`/
`provides_to` edges at rev10, under a green drift check, because regenerating
a knowingly-broken graph reproduces the same knowingly-broken file. Each of
those 20 was dispositioned before the switch: 11 were confirmed by the target
module's own clause citations and became `depends_on` edges; 3 were dropped as
unsupported; 6 were reverse halves this derivation now supplies. See
`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md` and
`round-2026-08c/RELATION-MODEL-DECISION.md`.

Usage: build_dependency_index.py [--root DIR] [--check]
  --check: regenerate and diff against the committed index; nonzero exit on drift.
"""
import argparse
import re
import sys
from pathlib import Path

LIST_KEYS = ("governs", "applies_to", "depends_on", "constrains", "tags")

#: A clause reference. `RFC9-32` is a clause; `RFC 0008 §5` (with a space) is a
#: navigational section reference and is deliberately not matched — citing a
#: section as authority is itself a defect (P-21(c)), not an edge to record.
CLAUSE_REF = re.compile(r"\bRFC(\d+)-\d+")


def parse_front_matter(text):
    """Same shallow reader as build_contract_index.py: top-level `key: value`
    lines only, `[a, b]` inline lists split on commas."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            v = v.strip().strip('"')
            if v.startswith("[") and v.endswith("]"):
                fm[k.strip()] = [x.strip() for x in v[1:-1].split(",") if x.strip()]
            else:
                fm[k.strip()] = v
    return fm


def module_files(root):
    rfcs = root / "rfcs"
    files = sorted(rfcs.glob("RFC-00*.md"))
    for pkg in sorted(p for p in rfcs.glob("RFC-00*") if p.is_dir()):
        files += sorted(pkg.glob("*.md"))
    return rfcs, files


def collect(root):
    rfcs, files = module_files(root)
    modules, contracts = [], {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        cid = fm.get("id")
        if not cid:
            continue
        body = text[text.find("\n---\n", 4) + 5:]
        rec = {
            "file": str(f.relative_to(rfcs)),
            "id": cid,
            "title": fm.get("title", ""),
            "depends_on": [x for x in fm.get("depends_on", [])],
            "constrains": [x for x in fm.get("constrains", [])],
            "applies_to": [x for x in fm.get("applies_to", [])],
            "refs": {f"RFC-{int(n):04d}" for n in CLAUSE_REF.findall(body)},
        }
        rec["refs"].discard(cid)
        modules.append(rec)
        c = contracts.setdefault(cid, {"title": rec["title"], "modules": [],
                                       "depends_on": set(), "provides_to": set(),
                                       "constrains": set(),
                                       "constrained_by": set(),
                                       "cites": set(), "cited_by": set(),
                                       "refs": set(), "applies_to": set()})
        c["modules"].append(rec["file"])
        c["depends_on"] |= set(rec["depends_on"])
        c["constrains"] |= set(rec["constrains"])
        c["applies_to"] |= set(rec["applies_to"])
        c["refs"] |= rec["refs"]
        if not c["title"]:
            c["title"] = rec["title"]
    # Derive every inverse, and derive `cites` outright. A module "provides
    # to" every contract declaring a dependency on its own contract; is
    # "constrained by" every contract declaring a constraint on it; and
    # "cites" every contract whose clauses its body references and which its
    # `depends_on` does not already carry — a citation that is already a load
    # obligation is recorded once, as the stronger relation.
    for cid, c in contracts.items():
        c["provides_to"] = {o for o, oc in contracts.items()
                            if cid in oc["depends_on"]}
        c["constrained_by"] = {o for o, oc in contracts.items()
                               if cid in oc["constrains"]}
        c["cites"] = {t for t in c["refs"]
                      if t in contracts and t not in c["depends_on"]}
    for cid, c in contracts.items():
        c["cited_by"] = {o for o, oc in contracts.items() if cid in oc["cites"]}
    for rec in modules:
        c = contracts[rec["id"]]
        rec["provides_to"] = sorted(c["provides_to"])
        rec["cites"] = sorted(t for t in rec["refs"]
                              if t in contracts and t not in c["depends_on"])
    return modules, contracts


def asymmetries(contracts):
    """Dangling edges only.

    Asymmetry between the two directions is now unrepresentable: `provides_to`
    is derived from `depends_on`, so the two cannot disagree. What remains
    checkable is whether a declared dependency names a contract that exists.
    """
    out = []
    for a in sorted(contracts):
        for b in sorted(contracts[a]["depends_on"]):
            if b not in contracts:
                out.append((a, b, "dangling",
                            "`depends_on` names a contract with no module "
                            "in this package"))
        for b in sorted(contracts[a]["constrains"]):
            if b not in contracts:
                out.append((a, b, "dangling",
                            "`constrains` names a contract with no module "
                            "in this package"))
            elif a in contracts[b]["depends_on"]:
                out.append((a, b, "redundant",
                            "`constrains` where a `depends_on` already binds "
                            "the pair; the stronger relation covers it"))
    return out


def emit(root):
    modules, contracts = collect(root)
    asym = asymmetries(contracts)
    L = []
    add = L.append
    add("# Contract dependency index — derived, never authority")
    add("")
    add("**Generated projection.** Rebuild with")
    add("`python3 scripts/build_dependency_index.py`; check for drift with")
    add("`--check`. **The modules win over this file, always.** Nothing here")
    add("is a clause and nothing here may be cited as authority (RFC11-7")
    add("rebuildable-projection rule).")
    add("")
    add("## The three relations, and what a selector does with each")
    add("")
    add("| Relation | Meaning | Source | Context Compiler behaviour |")
    add("|---|---|---|---|")
    add("| `depends_on` | A must be loaded to interpret or modify B correctly | **authored** on the dependent | **mandatory load**, transitively |")
    add("| `constrains` | A restricts something B owns; B stays independently readable | **authored** on the constraining contract | loaded **when the task class crosses the constrained seam** — editing B loads A's constraining clauses; otherwise not |")
    add("| `cites` | A refers to a clause of B for navigation, comparison, or a forward pointer | **derived** from a clause-reference scan | **never automatic**. Navigational evidence a human or an agent may follow; it enters no packet by itself |")
    add("")
    add("`provides_to`, `constrained_by` and `cited_by` are the derived")
    add("inverses of the three and appear in no module's front matter. A")
    add("citation that is already a `depends_on` is recorded once, as the")
    add("stronger relation, and does not also appear under `cites`.")
    add("")
    add(f"Coverage: **{len(modules)} modules** across **{len(contracts)} contracts**.")
    add("")
    add("## Contract-level graph — load obligations")
    add("")
    add("One row per contract: the union of its modules' declared edges.")
    add("")
    add("| Contract | Title | applies_to | depends_on | provides_to |")
    add("|---|---|---|---|---|")
    for cid in sorted(contracts):
        c = contracts[cid]
        add("| `{}` | {} | {} | {} | {} |".format(
            cid, c["title"] or "—",
            ", ".join(sorted(c["applies_to"])) or "—",
            ", ".join(sorted(c["depends_on"])) or "— (none)",
            ", ".join(sorted(c["provides_to"])) or "— (none)"))
    add("")
    add("## Contract-level graph — semantic constraints")
    add("")
    add("A one-way restriction one contract places on something another owns.")
    add("These are the edges `depends_on` could not hold: they drive no load")
    add("obligation in the general case, and before this relation existed they")
    add("were stated in one contract, acknowledged by no clause in the other,")
    add("and enforced by neither (owner item **P-21(a)**).")
    add("")
    constrained = [cid for cid in sorted(contracts)
                   if contracts[cid]["constrains"] or contracts[cid]["constrained_by"]]
    if constrained:
        add("| Contract | constrains | constrained_by |")
        add("|---|---|---|")
        for cid in constrained:
            c = contracts[cid]
            add("| `{}` | {} | {} |".format(
                cid,
                ", ".join(sorted(c["constrains"])) or "— (none)",
                ", ".join(sorted(c["constrained_by"])) or "— (none)"))
    else:
        add("**No `constrains` edge is declared.** That is a claim, not an")
        add("absence: it says every cross-contract restriction in the corpus is")
        add("either a load obligation or does not exist.")
    add("")
    add("## Contract-level graph — citations")
    add("")
    add("Derived, never authored: contract A cites contract B where a module of")
    add("A references a clause `RFC<B>-n` in its body and A's `depends_on` does")
    add("not already carry B. **A citation is not a reliance.** Most of these")
    add("are forward references from a lower layer to the surface that consumes")
    add("it; turning them into dependencies would make the kernel depend on")
    add("everything, which is backwards. Whether any one of them is a genuine")
    add("missed dependency is owner item **P-21(b)**.")
    add("")
    add("| Contract | cites | cited_by |")
    add("|---|---|---|")
    for cid in sorted(contracts):
        c = contracts[cid]
        if not (c["cites"] or c["cited_by"]):
            continue
        add("| `{}` | {} | {} |".format(
            cid,
            ", ".join(sorted(c["cites"])) or "— (none)",
            ", ".join(sorted(c["cited_by"])) or "— (none)"))
    add("")
    add("## Module-level graph")
    add("")
    add("One row per module file. `depends_on` is that file's own front matter;")
    add("`cites` is derived from that file's own body. A package README and its")
    add("sibling modules may declare different edges; both are reproduced,")
    add("neither is reconciled here.")
    add("")
    add("| Module | Contract | depends_on | provides_to | cites |")
    add("|---|---|---|---|---|")
    for m in modules:
        add("| `rfcs/{}` | `{}` | {} | {} | {} |".format(
            m["file"], m["id"],
            ", ".join(m["depends_on"]) or "— (none)",
            ", ".join(m["provides_to"]) or "— (none)",
            ", ".join(m["cites"]) or "— (none)"))
    add("")
    add("## Graph consistency")
    add("")
    add("**The graph is closed by construction.** `depends_on` is the single")
    add("authored direction; `provides_to` is derived by reversing it and")
    add("appears in no module's front matter. The two therefore cannot")
    add("disagree — the 20 asymmetric edges this section used to report were")
    add("not a data-entry problem but a consequence of maintaining both")
    add("directions by hand. Their per-edge dispositions are recorded in")
    add("`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md`.")
    add("")
    add("What remains checkable is **dangling** edges: a declared dependency")
    add("on a contract with no module in this package.")
    add("")
    if asym:
        add(f"**{len(asym)} dangling edge(s)** at generation:")
        add("")
        add("| From | To | Kind | Problem |")
        add("|---|---|---|---|")
        for a, b, kind, why in asym:
            add(f"| `{a}` | `{b}` | `{kind}` | {why} |")
    else:
        add("**No dangling edges** at generation: every contract named by a")
        add(f"`depends_on` has at least one module in this package "
            f"({len(contracts)} contracts resolved).")
    add("")
    add("The contract graph is **not acyclic** — mutual edges between kernel")
    add("contracts are declared deliberately (a contract can both rely on and")
    add("feed another). Read it as a reference graph for context selection, not")
    add("as a build order.")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    out = root / "CONTRACT-DEPENDENCY-INDEX.md"
    generated = emit(root)
    if args.check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != generated:
            print("DRIFT: CONTRACT-DEPENDENCY-INDEX.md differs from regeneration")
            sys.exit(1)
        print("dependency index matches regeneration — no drift")
    else:
        out.write_text(generated, encoding="utf-8")
        print(f"wrote {out} ({len(generated.splitlines())} lines)")


if __name__ == "__main__":
    main()
