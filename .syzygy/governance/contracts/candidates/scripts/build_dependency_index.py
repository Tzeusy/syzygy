#!/usr/bin/env python3
"""Deterministically derive CONTRACT-DEPENDENCY-INDEX.md from the active
contract modules' YAML front matter. The index is a rebuildable projection,
never a second truth store (RFC11-7): every row restates what a module already
declares, and the module wins wherever they disagree.

**`depends_on` is the single authored direction.** `provides_to` is
**derived** here by reversing it, and is deliberately absent from module front
matter. Two independently authored views of one edge set can disagree, and
did — 20 asymmetric edges at rev10 — which made the graph unusable as a
routing input for the Context Compiler. One authored direction cannot
disagree with itself. Each of those 20 was dispositioned before the switch:
11 were confirmed by the target module's own clause citations and became
`depends_on` edges; 3 were dropped as unsupported (no citation either way);
6 were reverse halves that this derivation now supplies automatically. See
`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md`.

Usage: build_dependency_index.py [--root DIR] [--check]
  --check: regenerate and diff against the committed index; nonzero exit on drift.
"""
import argparse
import sys
from pathlib import Path

LIST_KEYS = ("governs", "applies_to", "depends_on", "tags")


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
        fm = parse_front_matter(f.read_text(encoding="utf-8"))
        cid = fm.get("id")
        if not cid:
            continue
        rec = {
            "file": str(f.relative_to(rfcs)),
            "id": cid,
            "title": fm.get("title", ""),
            "depends_on": [x for x in fm.get("depends_on", [])],
            "applies_to": [x for x in fm.get("applies_to", [])],
        }
        modules.append(rec)
        c = contracts.setdefault(cid, {"title": rec["title"], "modules": [],
                                       "depends_on": set(), "provides_to": set(),
                                       "applies_to": set()})
        c["modules"].append(rec["file"])
        c["depends_on"] |= set(rec["depends_on"])
        c["applies_to"] |= set(rec["applies_to"])
        if not c["title"]:
            c["title"] = rec["title"]
    # Derive provides_to by reversing depends_on — contract level, then
    # module level. A module "provides to" every contract that declares a
    # dependency on the contract this module belongs to.
    for cid, c in contracts.items():
        c["provides_to"] = {o for o, oc in contracts.items()
                            if cid in oc["depends_on"]}
    for rec in modules:
        rec["provides_to"] = sorted(contracts[rec["id"]]["provides_to"])
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
    add("`--check`. Every `depends_on` and `applies_to` cell restates the")
    add("front matter of the active contract modules under `rfcs/`; every")
    add("`provides_to` cell is **derived** by reversing `depends_on`.")
    add("**The modules win over this file, always.** Nothing here is a clause")
    add("and nothing here may be cited as authority. No `depends_on` edge")
    add("appears that a module does not declare, and no `provides_to` edge")
    add("appears that is not the exact reverse of one (charter §11.5; RFC11-7")
    add("rebuildable-projection rule).")
    add("")
    add(f"Coverage: **{len(modules)} modules** across **{len(contracts)} contracts**.")
    add("")
    add("## Contract-level graph")
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
    add("## Module-level graph")
    add("")
    add("One row per module file, as declared in that file's own front matter.")
    add("A package README and its sibling modules may declare different edges;")
    add("both are reproduced, neither is reconciled here.")
    add("")
    add("| Module | Contract | depends_on | provides_to |")
    add("|---|---|---|---|")
    for m in modules:
        add("| `rfcs/{}` | `{}` | {} | {} |".format(
            m["file"], m["id"],
            ", ".join(m["depends_on"]) or "— (none)",
            ", ".join(m["provides_to"]) or "— (none)"))
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
