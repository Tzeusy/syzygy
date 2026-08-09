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

#: A clause definition opener, used to verify that a declared `constrains`
#: edge is anchored in a numbered clause of the declaring module rather than
#: in navigational prose. Review RD-4 finding F-1: the first `constrains` edge
#: ever declared rested on a sentence 50 lines past the last clause, inside a
#: §5 Integration section — promoting navigational prose to structured
#: metadata, which makes it read as more load-bearing than its source.
CLAUSE_DEF = re.compile(r"^\*\*(RFC\d+-\d+)(?:\([a-z]\))?\s*(?:\.|—|-)", re.M)

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
            "constrains_source": fm.get("constrains_source", ""),
            "clause_defs": set(CLAUSE_DEF.findall(body)),
            "applies_to": [x for x in fm.get("applies_to", [])],
            "refs": {f"RFC-{int(n):04d}" for n in CLAUSE_REF.findall(body)},
        }
        rec["refs"].discard(cid)
        modules.append(rec)
        c = contracts.setdefault(cid, {"title": rec["title"], "modules": [],
                                       "depends_on": set(), "provides_to": set(),
                                       "constrains": set(),
                                       "constrains_sources": set(),
                                       "constrained_by": set(),
                                       "cites": set(), "cited_by": set(),
                                       "refs": set(), "applies_to": set()})
        c["modules"].append(rec["file"])
        c["depends_on"] |= set(rec["depends_on"])
        c["constrains"] |= set(rec["constrains"])
        if rec["constrains"]:
            c["constrains_sources"].add((rec["constrains_source"], rec["file"]))
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


def asymmetries(contracts, modules):
    """Structural defects in the declared edge set.

    Three predicates, each paid for by a finding:

    * **dangling** — a declared edge names a contract with no module here.
    * **unanchored `constrains`** — the declaring module does not define the
      clause its `constrains_source` names, or names none. Review RD-4
      recommendation 2: a constraint whose source text is not inside a numbered
      clause of the declaring contract is prose promoted to metadata. This one
      predicate rejects the first edge ever declared and admits both the
      reviewer found missing, which is the correct sort on all three.
    * **`A constrains B` where `A depends_on B`** — reported, because it is the
      signal that a constraint was read off a dependency rather than found. The
      earlier form checked only the other direction (`A in B.depends_on`) and
      therefore did not fire on the one declared edge that turned out to be
      misdirected (RD-4 finding F-16).

    A `constrains` edge that `B depends_on A` already covers is **not** a
    defect and is not reported here — B loads A regardless, so the constraint
    is discharged by the stronger relation. It is annotated in the emitted
    table instead, so the reader can see which edges are load-covered and which
    are the whole reason the relation exists.
    """
    by_file = {m["file"]: m for m in modules}
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

        for src, f in sorted(contracts[a]["constrains_sources"]):
            if not src:
                out.append((a, "—", "unanchored",
                            f"`{f}` declares `constrains` with no "
                            f"`constrains_source`; a constraint with no clause "
                            f"anchor is prose promoted to metadata"))
            elif src not in by_file[f]["clause_defs"]:
                out.append((a, "—", "unanchored",
                            f"`{f}` names `constrains_source: {src}`, which it "
                            f"does not define; the anchor must be a clause of "
                            f"the declaring module"))
    return out


def coincident_edges(contracts):
    """`A constrains B` where `A depends_on B` — reported, never a defect.

    Both relations can be genuinely true of one pair: RFC-0007 needs RFC-0001
    to know what a claim *is* (`depends_on`), and RFC7-3 restricts what a claim
    may cite (`constrains`). But the pair is also the exact shape of a
    constraint read off a dependency rather than found in a clause — which is
    how the first misdirected edge in this corpus was declared, and RD-4
    finding F-16 asked for the signal. So it is printed and prompts a
    re-examination; it does not fail anything.
    """
    return [(a, b) for a in sorted(contracts)
            for b in sorted(contracts[a]["constrains"])
            if b in contracts[a]["depends_on"]]


def emit(root):
    modules, contracts = collect(root)
    asym = asymmetries(contracts, modules)
    coincident = coincident_edges(contracts)
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
    add("## The three relations")
    add("")
    add("| Relation | Meaning | Source of truth |")
    add("|---|---|---|")
    add("| `depends_on` | A must be loaded to interpret or modify B correctly | **authored** on the dependent |")
    add("| `constrains` | A restricts something B owns; B stays independently readable | **authored** on the constraining contract, anchored to a clause of it |")
    add("| `cites` | A refers to a clause of B for navigation, comparison, or a forward pointer | **derived** from a clause-reference scan |")
    add("")
    add("**What a selector should do with each is deliberately not stated")
    add("here.** An earlier revision of this file carried a \"Context Compiler")
    add("behaviour\" column — mandatory-load, load-on-seam-crossing,")
    add("never-automatic — and **no clause states any of it**. A binding")
    add("selector rule homed in a file whose own banner reads *nothing here may")
    add("be cited as authority* is the defect this package keeps re-acquiring,")
    add("appearing inside the repair for it (review RD-4, finding F-15).")
    add("")
    add("The proposal lives in `round-2026-08c/RELATION-MODEL-DECISION.md`,")
    add("marked as a proposal. Its home if adopted is **RFC11-4**, which")
    add("enumerates the deterministic selection inputs today and names")
    add("`depends_on` / `provides_to` and clause-level metadata — and does")
    add("**not** name `constrains`. Until that clause changes, a conformant")
    add("compiler would not read this relation at all.")
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
    add("A one-way restriction one contract places on something another owns —")
    add("**anchored to a clause of the constraining contract**, which is")
    add("verified below rather than asserted here.")
    add("")
    add("These are edges `depends_on` cannot hold: they drive no load")
    add("obligation in the general case. What they have in common is that the")
    add("restricting text names what *other* contracts may do, and the")
    add("constrained contract does not carry it (owner item **P-21(a)**).")
    add("")
    add("**Two things this table does not claim.** It does not claim the")
    add("constrained contract is silent — RFC-0007 states the SDR-18 seam in")
    add("RFC7-24 from its own authority, and an earlier revision of this")
    add("sentence generalised across every row and was false for one of them.")
    add("And it does not claim to be complete: the population was found by two")
    add("Python `re` sweeps over whole-file text (line-based and")
    add("whitespace-normalised) for restriction-shaped clause language, and a")
    add("sweep by the party that authored the edges is the weakest evidence in")
    add("this repository. **[Unknown]** whether a third edge exists.")
    add("")
    constrained = [cid for cid in sorted(contracts)
                   if contracts[cid]["constrains"] or contracts[cid]["constrained_by"]]
    if constrained:
        add("An edge marked **(load-covered)** is one where the constrained")
        add("contract already declares `depends_on` the constraining one, so it")
        add("loads it regardless and the constraint is discharged by the")
        add("stronger relation. The unmarked edges are the whole reason this")
        add("relation exists.")
        add("")
        add("| Contract | constrains | anchored at | constrained_by |")
        add("|---|---|---|---|")
        for cid in constrained:
            c = contracts[cid]
            outs = []
            for b in sorted(c["constrains"]):
                covered = cid in contracts.get(b, {}).get("depends_on", set())
                outs.append(f"{b}{' *(load-covered)*' if covered else ''}")
            src = ", ".join(f"`{s}`" for s, _ in sorted(c["constrains_sources"])
                            if s) or "—"
            add("| `{}` | {} | {} | {} |".format(
                cid, ", ".join(outs) or "— (none)", src,
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
    # The count that used to sit in this sentence ("the 20 asymmetric edges")
    # was hard-coded here and emitted into a file whose header reads
    # *derived, never authority* — a generator transcribing a figure of a
    # prior state into its own output (review RD-17 finding 5). It is now
    # named as a dated historical figure owned by the report that measured
    # it, and this file states no number it has not computed.
    add("**The graph is closed by construction.** `depends_on` is the single")
    add("authored direction; `provides_to` is derived by reversing it and")
    add("appears in no module's front matter. The two therefore cannot")
    add("disagree — the asymmetric edges this section used to report were not")
    add("a data-entry problem but a consequence of maintaining both")
    add("directions by hand. Their count, as measured at rev10, and their")
    add("per-edge dispositions are recorded in")
    add("`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md`; this file does not")
    add("restate a figure it cannot recompute.")
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
    if coincident:
        add("### Reported, not a defect: `A constrains B` where `A depends_on B`")
        add("")
        add("Both relations can be genuinely true of one pair. They are also")
        add("the exact shape of a constraint read off a dependency rather than")
        add("found in a clause, which is how the first misdirected edge in this")
        add("corpus was declared. Printed so it is re-examined; it fails")
        add("nothing.")
        add("")
        for a, b in coincident:
            add(f"- `{a}` constrains `{b}`, and also depends on it")
        add("")
    add("The contract graph is **not acyclic** — mutual edges between kernel")
    add("contracts are declared deliberately (a contract can both rely on and")
    add("feed another). Read it as a reference graph for context selection, not")
    add("as a build order.")
    return "\n".join(L) + "\n"


def population(root):
    """The denominator `--check` states, recomputed each run.

    A module with no front-matter `id` is skipped by `collect()`, so a corpus
    that lost its front matter would regenerate to a smaller graph and a bare
    "no drift" would be true and useless (review RD-17 finding 13). Both the
    file count and the keyed count print, so the shrink is visible.
    """
    _rfcs, files = module_files(root)
    modules, contracts = collect(root)
    edges = sum(len(m["depends_on"]) for m in modules)
    constrains = sum(len(c["constrains"]) for c in contracts.values())
    return (f"{len(modules)} of {len(files)} module(s) carry a front-matter "
            f"id, {len(contracts)} contract(s), {edges} authored "
            f"`depends_on` edge(s), {constrains} `constrains` edge(s)")


def selftest(root):
    """Mutate a copy per predicate class; confirm the regeneration differs.

    Review RD-17 finding 13: this script shipped no fixture, so its green
    `--check` was a claim nobody had seen fail — and two of its three
    predicates (the dangling test and the `constrains` anchor test) exist
    because a reviewer found the defect they now catch.
    """
    import re as _re
    import shutil
    import tempfile
    cases = []
    base = emit(root)

    def mutate(rel, fn, label, extra=None):
        d = Path(tempfile.mkdtemp(prefix="depindex-selftest-"))
        try:
            shutil.copytree(root / "rfcs", d / "rfcs")
            p = d / rel
            p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")
            after = emit(d)
            cases.append((label, after != base))
            if extra:
                cases.append((extra[0], extra[1](after, d)))
        finally:
            shutil.rmtree(d, ignore_errors=True)

    _rfcs, files = module_files(root)
    victim = str(files[0].relative_to(root))

    # 1. A dangling `depends_on` must reach the emitted defect table, not be
    #    absorbed into a clean graph.
    mutate(victim,
           lambda t: _re.sub(r"^depends_on: \[", "depends_on: [RFC-0099, ",
                             t, count=1, flags=_re.M),
           "dangling depends_on changes the projection",
           extra=("dangling depends_on is named in the defect table",
                  lambda after, _d: "RFC-0099" in after and "dangling" in after))

    # 2. A `constrains` edge whose source clause the declaring module does
    #    not define — review RD-4 finding F-1's exact shape.
    src = next((f for f in files
                if "constrains_source:" in f.read_text(encoding="utf-8")), None)
    if src is not None:
        rel = str(src.relative_to(root))
        mutate(rel,
               lambda t: _re.sub(r"^constrains_source: .*$",
                                 "constrains_source: RFC99-99", t, count=1,
                                 flags=_re.M),
               "unanchored constrains_source changes the projection",
               extra=("unanchored constrains_source is named as a defect",
                      lambda after, _d: "unanchored" in after))
    else:
        cases.append(("unanchored constrains_source changes the projection",
                      False))

    # 3. A dropped front-matter id silently shrinks the graph. The
    #    denominator is what makes it visible; the projection must move too.
    mutate(victim, lambda t: t.replace("\nid: ", "\nid_was: ", 1),
           "dropped front-matter id changes the projection")

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
    out = root / "CONTRACT-DEPENDENCY-INDEX.md"
    generated = emit(root)
    pop = population(root)
    if args.check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != generated:
            print("DRIFT: CONTRACT-DEPENDENCY-INDEX.md differs from regeneration")
            print(f"population: {pop}")
            sys.exit(1)
        print(f"dependency index matches regeneration — no drift over {pop}")
    else:
        out.write_text(generated, encoding="utf-8")
        print(f"wrote {out} ({len(generated.splitlines())} lines) — {pop}")


if __name__ == "__main__":
    main()
