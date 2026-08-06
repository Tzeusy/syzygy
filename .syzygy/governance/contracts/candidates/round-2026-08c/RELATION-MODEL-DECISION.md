# The contract relation model — decision record and rationale

> **Candidate. Binds nothing.** This records a design decision made inside a
> candidate package and the reasoning behind it. The owner's ruling on whether
> to keep it is **P-21**. Where this file and the generated
> `../CONTRACT-DEPENDENCY-INDEX.md` disagree, the index is derived from the
> modules and the modules win over both.

## What was wrong

One key, `depends_on`, was carrying three different relations at once:

1. **A load obligation** — you cannot correctly interpret or modify B without
   A in front of you.
2. **A one-way semantic constraint** — A restricts something B owns, while B
   remains perfectly readable on its own.
3. **An ordinary citation** — A points at a clause of B for navigation,
   comparison, or as a forward reference.

A selector cannot tell these apart, and neither could the corpus. Review RC-4
found the consequence in both directions:

- **Constraints had no home.** RFC-0006 restricts RFC-0005 (a client class
  never changes an answer's fact set, only admission), and RFC8-9 asserts
  ownership against RFC7-24's seam. In both cases the restriction is stated in
  one contract, **acknowledged by no clause in the other, and enforced by
  neither**. `depends_on` cannot hold them, because neither is a load
  obligation.
- **Citations looked like dependencies.** Eight contracts cite clauses of
  contracts they declare no dependency on. A previous round applied
  "cites ⇒ depends_on" to eleven edges; RC-4 refuted four of them, because
  the test was *does the target cite the source's clauses* when the sharper
  question is *is that citation a reliance*. Applied corpus-wide it would have
  given the kernel — the contract that depends on nothing and is cited by
  everything — six dependencies.

Both failure modes are the same mistake: **one edge type standing in for three
relations that a reader, and a compiler, must distinguish.**

## The model

Three relations, literal technical names, no public vocabulary added:

```text
depends_on
    Contract/module A must be loaded to interpret or modify B correctly.

constrains
    A places a semantic restriction on something B owns, but B may be
    independently understandable without loading A in every task.

cites
    A refers to B for navigation, comparison, rationale, or a forward
    pointer without implying load dependency or ownership.
```

**These are contract-index mechanics, not vocabulary.** They are field names in
front matter and columns in a generated index. They are deliberately absent
from the term registry, and `TERM-REGISTRY-SEMANTIC-DELTA.md` records that
absence as a decision rather than leaving it to be reversed by default next
round.

## One authored direction each; every inverse derived

This is the rule the previous round paid for. Two independently authored views
of one edge set **can** disagree, and did: twenty asymmetric
`depends_on`/`provides_to` edges at rev10, sitting under a green drift check —
because regenerating a knowingly-broken graph reproduces the same
knowingly-broken file.

| Relation | Authored on | Derived inverse |
|---|---|---|
| `depends_on` | the **dependent** — B declares what it needs | `provides_to` |
| `constrains` | the **constraining** contract — A declares what it restricts | `constrained_by` |
| `cites` | **nobody** — fully derived | `cited_by` |

### Why `constrains` is authored on the constraining side

The alternative — requiring the constrained contract to acknowledge the
restriction — is what failed. RC-4's finding was precisely that RFC-0005 and
RFC-0007 carry **no acknowledging clause**, and adding one to each would mean
editing two contracts to record a fact a third already states.

Three reasons for the direction chosen:

1. **A restriction is stated where it is written.** RFC-0006's text is what
   restricts RFC-0005. RFC-0006 knows; RFC-0005 does not, and requiring it to
   know is what left the edge unrecorded for two rounds.
2. **The constrained side gets it anyway, derived.** `constrained_by` on
   RFC-0005 is computed by reversal — the visibility RC-4 asked for, without a
   second authored copy that can disagree.
3. **Adding a constraint is a one-file edit.** If declaring an edge requires
   editing the contract you are constraining, the cheapest path is not to
   declare it. That is how a relation stops being used.

**The counter-argument, stated because it is not weak:** an engineer editing
RFC-0005 opens RFC-0005 and sees nothing. They must consult the generated
index to learn they are constrained. That is a real cost, it is why review
RD-4 was asked to argue both sides, and it is the reason the "operative or
merely recorded?" question is criterion 6 of that commission.

### Why `cites` is derived rather than authored

Authoring it would create a **third hand-maintained edge set** in a corpus
that has already shipped one stale by twenty edges. Deriving it means:

- a new citation appears in the index the moment the prose does, with no
  edit and no chance of omission;
- it cannot go stale, because there is nothing to keep in step;
- and the derivation is the honest bar for what a citation *is* — a clause
  reference in the body — rather than someone's judgment about which
  references were worth recording.

The derivation is deliberately narrow. It matches `RFC<n>-<m>` — a **clause**
identity — and not `RFC 0008 §5`, a navigational section reference. Citing a
section as authority is a defect (P-21(c)), not an edge worth recording, and
the one instance of it in the corpus was repaired rather than encoded.

**Verified the moment it was switched on:** RFC-0010's rev11b amendments cite
RFC4-18..21 and RFC2-25, and the index gained `RFC-0010 cites RFC-0004,
RFC-0009` on regeneration with no edge authored by anyone. That is the
property the derivation exists for.

## What the Context Compiler does with each

| Relation | Selector behaviour |
|---|---|
| `depends_on` | **Mandatory load**, transitively. This is the only relation that puts something in a packet unconditionally |
| `constrains` | Loaded **when the task class crosses the constrained seam**. Editing B loads A's constraining clauses via the derived `constrained_by`; a task that does not touch the seam does not carry them |
| `cites` | **Never automatic.** Navigational evidence a human or an agent may follow. It enters no packet by itself |

**`constrains` is the interesting one, and its rule is a judgment call stated
as such.** The alternative readings are "always load" (which makes it a
`depends_on` under another name, and inflates every packet touching a
constrained contract) and "never load" (which makes it decorative). The
task-class rule sits between them and requires the selector to classify the
task — which is exactly the thing RFC11-4 says mandatory selection must do
deterministically, and exactly the thing no implementation does yet.

**So this is a selection rule with no selector.** It is stated so that the
first implementation has something to implement, not because anything today
honours it. `FINAL-CONTEXT-SELECTION-REPORT.md` is where that gap is measured.

## The current edge set

Two `constrains` edges, both from RC-4's finding, both declared this round:

| From | To | The restriction, and where it is stated |
|---|---|---|
| `RFC-0006` | `RFC-0005` | A client class never changes an answer's fact set, only admission. Stated in RFC-0006; RFC-0005 carries no acknowledging clause |
| `RFC-0008` | `RFC-0007` | RFC8-9 asserts Trajectory's ownership of the drafting queue and work lifecycle **against Polaris**, at RFC7-24's seam. Stated in RFC-0008; RFC-0007 carries no acknowledging clause |

Declared on the module whose text states the restriction, and on the package
README where one exists, so that the module union and the package row agree.

**Whether these are the only two is an open question** and is criterion 2 of
review RD-4's commission. A sweep by the authoring session found no third; a
sweep by the authoring session is the weakest evidence in this repository.

`cites` currently derives **twenty-two** edges across eight contracts. Read the
generated table, not this sentence — the figure moves whenever a clause
reference is added, which is the point.

## What this does not resolve

- **P-21(b) stays open.** Whether any of the derived citation edges is a
  *genuine missed dependency* is an owner ruling, not a derivation. The model
  makes the population visible and classified; it does not adjudicate it.
- **No `depends_on` edge was added or removed this round.** The relation split
  is additive. Re-testing the existing edges against the sharper "is this a
  reliance?" question is RD-4 criterion 3, and its findings are for the next
  pass, not this one.
- **`constrains` is recorded, not enforced.** No check verifies that a
  constrained contract's editor loaded the constraining clause, because
  nothing in this repository observes what an editor loads. RC-4's "enforced
  by neither" is **half closed**: the constraint is now *stated in a place
  both sides can see*, and it is still enforced by nobody.
