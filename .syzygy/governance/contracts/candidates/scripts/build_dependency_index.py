#!/usr/bin/env python3
"""Deterministically derive CONTRACT-DEPENDENCY-INDEX.md from the active
contract modules' YAML front matter. The index is a rebuildable projection,
never a second truth store (RFC11-7): every row restates what a module already
declares, and the module wins wherever they disagree.

Edges are read, never inferred. Where `depends_on` and `provides_to` disagree
about the same pair, the disagreement is reported as an asymmetry — this script
does not repair the graph, because both fields are authored metadata and only
their owner may change them.

Usage: build_dependency_index.py [--root DIR] [--check]
  --check: regenerate and diff against the committed index; nonzero exit on drift.
"""
import argparse
import sys
from pathlib import Path

LIST_KEYS = ("governs", "applies_to", "depends_on", "provides_to", "tags")


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
            "provides_to": [x for x in fm.get("provides_to", [])],
            "applies_to": [x for x in fm.get("applies_to", [])],
        }
        modules.append(rec)
        c = contracts.setdefault(cid, {"title": rec["title"], "modules": [],
                                       "depends_on": set(), "provides_to": set(),
                                       "applies_to": set()})
        c["modules"].append(rec["file"])
        c["depends_on"] |= set(rec["depends_on"])
        c["provides_to"] |= set(rec["provides_to"])
        c["applies_to"] |= set(rec["applies_to"])
        if not c["title"]:
            c["title"] = rec["title"]
    return modules, contracts


def asymmetries(contracts):
    out = []
    for a in sorted(contracts):
        for b in sorted(contracts[a]["depends_on"]):
            if b not in contracts:
                out.append((a, b, "dangling", "`depends_on` names a contract with no module in this package"))
            elif a not in contracts[b]["provides_to"]:
                out.append((a, b, "depends_on", f"`{a}.depends_on` names {b}, but `{b}.provides_to` does not name {a}"))
        for b in sorted(contracts[a]["provides_to"]):
            if b not in contracts:
                out.append((a, b, "dangling", "`provides_to` names a contract with no module in this package"))
            elif a not in contracts[b]["depends_on"]:
                out.append((a, b, "provides_to", f"`{a}.provides_to` names {b}, but `{b}.depends_on` does not name {a}"))
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
    add("`--check`. Every row restates the `depends_on` / `provides_to` /")
    add("`applies_to` front matter of the active contract modules under `rfcs/`.")
    add("**The modules win over this file, always.** Nothing here is a clause,")
    add("nothing here may be cited as authority, and no edge appears here that a")
    add("module does not declare — the generator reads edges, it never infers")
    add("them (charter §11.5; RFC11-7 rebuildable-projection rule).")
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
    add("`depends_on` and `provides_to` are two independently authored views of")
    add("the same edge set, so they can disagree. Each disagreement below is")
    add("**reported, not repaired**: adding the missing half would be inventing")
    add("an edge no module declares, and removing the stated half would delete")
    add("one. Resolving them is an edit to the modules' front matter, and")
    add("belongs to whoever owns those modules.")
    add("")
    if asym:
        add(f"**{len(asym)} asymmetric or dangling edges** at generation:")
        add("")
        add("| From | To | Declared on | Disagreement |")
        add("|---|---|---|---|")
        for a, b, kind, why in asym:
            add(f"| `{a}` | `{b}` | `{kind}` | {why} |")
    else:
        add("**No asymmetric or dangling edges** at generation: every declared")
        add("`depends_on` has a matching `provides_to` and vice versa.")
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
