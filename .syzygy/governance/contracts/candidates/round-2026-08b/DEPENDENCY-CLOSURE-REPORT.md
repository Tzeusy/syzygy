# Dependency closure — the 20 asymmetric edges, dispositioned

> **Non-authoritative round record.** The contract modules' front matter is
> the authority for what they declare; this file records why it now says what
> it says. Where they disagree, the modules win.

## The defect

`CONTRACT-DEPENDENCY-INDEX.md` reported **20 asymmetric or dangling edges**
at every generation, in its own "Graph consistency" section, and had done so
for as long as the section existed. The index's drift check nevertheless
reported "no drift" — because the check compares the generated file against
regeneration, and a knowingly inconsistent graph regenerates to the same
knowingly inconsistent file. A green check sat over a broken graph.

This mattered beyond tidiness. The dependency graph is the routing input the
Context Compiler uses to decide what a task must load. A routing layer cannot
be trusted over a graph whose two halves disagree about which edges exist:
depending on which direction you read, "what must I load to work on RFC-0011"
had two different answers.

## The root cause

`depends_on` and `provides_to` were **two independently authored views of one
edge set**. Nothing forced them to agree, so over eleven contracts and 32
modules they drifted apart at 20 points. This is not a data-entry failure
that more care would have prevented; it is the predictable outcome of storing
one fact twice.

## The fix, structurally

**`depends_on` is now the single authored direction. `provides_to` is derived
by reversing it, and has been removed from all 32 modules' front matter.**

One authored direction cannot disagree with itself, so the asymmetry class is
now unrepresentable rather than merely absent. What the index still checks is
**dangling** edges — a dependency naming a contract with no module in the
package — which remains a real, possible defect.

## The fix, per edge

Each of the 20 was dispositioned before the switch, because switching alone
would have silently dropped every edge declared only on the `provides_to`
side. Judgment was not the instrument: **the test was whether the target
module actually cites the source contract's clauses in its own body.** A
module that says "per RFC5-18 profile identity" cannot be applied without
RFC-0005 — that is a dependency, demonstrated by the text rather than
asserted about it.

### Group A — 6 edges: reverse half missing, now supplied automatically

Declared on `depends_on`, absent from the target's `provides_to`. Derivation
supplies the missing half by construction; no front matter changed.

| From | To |
|---|---|
| `RFC-0002` | `RFC-0003` |
| `RFC-0002` | `RFC-0004` |
| `RFC-0005` | `RFC-0002` |
| `RFC-0007` | `RFC-0004` |
| `RFC-0007` | `RFC-0005` |
| `RFC-0009` | `RFC-0005` |

> **Superseded in part — read "Correction after RC-4" below before using
> Group B.** Four of the eleven Group B edges were refuted by independent
> review and have been reverted. The table is left standing rather than
> silently edited, because the error it records is instructive.

### Group B — 11 edges: `provides_to`-only, confirmed by citation → `depends_on` added

The target cites the source's clauses in its own body. The `provides_to`
declaration was right and the missing `depends_on` was the omission.

| Source | Target | `depends_on` added to |
|---|---|---|
| `RFC-0003` | `RFC-0006` | `RFC-0006-cross-surface-selection-query-drawer.md` |
| `RFC-0004` | `RFC-0003` | `RFC-0003/governance-homes-and-owner-acts.md`, `RFC-0003/manifests-and-namespace.md` |
| `RFC-0005` | `RFC-0003` | `RFC-0003/governance-homes-and-owner-acts.md`, `RFC-0003/manifests-and-namespace.md` |
| `RFC-0006` | `RFC-0011` | `RFC-0011-context-compiler.md` |
| `RFC-0007` | `RFC-0008` | `RFC-0008/identity-authority-materialization.md` |
| `RFC-0007` | `RFC-0009` | `RFC-0009/README.md`, `RFC-0009/interaction-parity-and-release.md`, `RFC-0009/visual-grammar-and-lenses.md` |
| `RFC-0008` | `RFC-0011` | `RFC-0011-context-compiler.md` |
| `RFC-0009` | `RFC-0007` | `RFC-0007/README.md`, `RFC-0007/rendering-and-surface.md` |
| `RFC-0009` | `RFC-0008` | `RFC-0008/README.md`, `RFC-0008/accounting-reconciliation-and-release.md`, `RFC-0008/state-vocabulary-and-cost.md` |
| `RFC-0009` | `RFC-0010` | `RFC-0010-mission-control-autonomy.md` |
| `RFC-0009` | `RFC-0011` | `RFC-0011-context-compiler.md` |

Every edge was applied at **module** granularity — to the specific module
whose text carries the citation — so module-level rows stay honest and a
package README does not absorb a sibling's dependency.

### Group C — 3 edges: unsupported, dropped

The target never cites the source's clauses. These were over-claims: a
contract asserting that another one uses it, where the other one never said
so and never showed it.

| Source | Target | Why dropped |
|---|---|---|
| `RFC-0005` | `RFC-0006` | RFC-0006's body cites no RFC5-* clause |
| `RFC-0006` | `RFC-0005` | RFC-0005's body cites no RFC6-* clause |
| `RFC-0008` | `RFC-0007` | RFC-0007's body cites no RFC8-* clause |

Dropping is the conservative choice here in the direction that matters: it
**narrows** what a context packet claims is required, and if a later clause
edit creates a genuine dependency, the citation appears and the edge is added
with evidence. The reverse error — carrying an unsupported edge — inflates
every packet that touches those contracts, permanently.

## What this does not fix

**Citation is evidence of dependency, not proof of it.** A clause reference
can be a forward pointer ("elaborated in RFC9-12") rather than a reliance.
The sweep that produced Groups B and C was scoped to the 20 known
asymmetries, deliberately: applying "cites ⇒ depends_on" corpus-wide would
have added, for example, six dependencies to RFC-0001 — the kernel contract
that depends on nothing and is cited by everything. Those broader
citation-without-declaration cases are **left alone and recorded here** as a
known, bounded imprecision:

| Contract | Cites clauses of, without declaring a dependency |
|---|---|
| `RFC-0001` | RFC-0002, 0003, 0004, 0005, 0006, 0009 |
| `RFC-0002` | RFC-0006, RFC-0007 |
| `RFC-0003` | RFC-0006, 0007, 0008, 0009, 0010 |
| `RFC-0004` | RFC-0008 |
| `RFC-0006` | RFC-0009 |
| `RFC-0008` | RFC-0009 *(now declared)* |
| `RFC-0010` | RFC-0007 |
| `RFC-0011` | RFC-0007 |

Most of these are genuine forward references from a lower-layer contract to
the surface that consumes it, and turning them into dependencies would make
the kernel depend on everything — which is exactly backwards. **Whether any
of them is a real missed dependency is an open question for the owner**, not
something this pass decided silently. It is tracked in
`PENDING-OWNER-DECISIONS.md`.

## Correction after RC-4

Review RC-4 (`reviews/RC-4-contract-semantics-RAW.md`, verdict **REVISE**)
returned after the edits above were applied and refuted **four of the eleven
Group B edges**. Its objection was not a difference of judgment; it was that
my test was too weak. I asked *does the target cite the source's clauses*.
RC-4 asked the sharper question: *is that citation a reliance?* Two citation
shapes answer "no" and my sweep counted both as "yes":

- the **status banner** — every module carries an identical `RFC3-16`
  correlation notice at line ~18, boilerplate that RFC-0001 also carries
  while declaring `depends_on: []`;
- the **shape-parallel parenthetical** — `(Shape-parallel with RFC6-28,
  RFC7-38, RFC8-32, RFC9-52.)`, a note that two clauses have the same shape,
  which is the opposite of consuming one.

I re-ran the evidence myself rather than accepting the verdict. All four are
confirmed refuted, each by its own text:

| Reverted edge | The only citation, and why it is not a reliance |
|---|---|
| `RFC-0006` → `RFC-0003` | `RFC-0006-…drawer.md:18` — the status banner, and nothing else in the file |
| `RFC-0008` → `RFC-0009` | Five citations, all naming RFC9-32 as the **consumer** of RFC-0008's two-field handoff. The direction is inverted; the true `RFC-0008 → RFC-0009` edge was already declared |
| `RFC-0010` → `RFC-0009` | `RFC-0010-…autonomy.md:482` — the shape-parallel parenthetical inside RFC10-16, which states its own phase rule |
| `RFC-0011` → `RFC-0009` | `RFC-0011-context-compiler.md:224` — the same parenthetical inside RFC11-12 |

RC-4's decisive internal proof for the last two: RFC7-38 is named in the same
parenthetical on the same line, yet RFC-0007 does not declare
`provides_to: RFC-0010`. Identical evidence, opposite treatment — so the
evidence was never doing the work.

**Group B is therefore 7 edges, not 11.** The four reverted edges are
recorded here and not re-litigated in the module front matter.

### Two edges dropped by Group C are real, but not dependencies

RC-4 also disputed two of Group C's three drops — `RFC-0006` → `RFC-0005`
and `RFC-0008` → `RFC-0007` — calling them **genuinely one-way constraint
edges** rather than over-claims, and recommending a separate `constrains:`
field to hold them.

The drops stand, and the reason is what `depends_on` is *for*. It is the
load-routing input: it answers "what must I read to work on this module."
RC-4's own analysis establishes that the answer here is *nothing* — "RFC-0005's
clauses are complete without loading RFC-0006." A one-way constraint is a real
relation, but it is not a load obligation, and putting it in the field that
drives loading would inflate every packet touching those contracts.

What RC-4 is right about is the residual: RFC-0006 states a constraint on
RFC-0005 (client class never changes an answer's fact set), RFC-0005 carries
no clause acknowledging it, and so the constraint is **stated in one contract
and enforced in neither**. That is a real gap, it is not fixed by a front-
matter edge, and it is now an owner item in `PENDING-OWNER-DECISIONS.md`
rather than a silent omission. The same applies to the RFC7-24/RFC8-9 seam,
which RC-4 found stated independently and completely from both sides with no
citation link in either direction.

### One package-README convention, verified rather than assumed

Checking the reverts surfaced a second question: six package-README rows
declare dependencies with no clause-level citation anywhere in the README. A
mechanical test of all six packages shows why, and it is not a defect — a
package README's `depends_on` is the **union of its modules'**. That held
exactly in 4 of 6 packages; the two exceptions (`RFC-0003`, `RFC-0008`) were
packages where this session's own module-level additions had not been
propagated to the README. Both are now propagated, and the union rule holds
in 6 of 6. It is a checkable invariant and is listed for the check battery.

### One vocabulary ordinal corrected

RC-4 found `missing-declaration` cited as **RFC2-24 #4** at
`rfcs/RFC-0009/semantic-geography.md:270`, where #4 is
`stale-beyond-currency-bound` and `missing-declaration` is #1 — a wrong value
inside a closed vocabulary that RFC6-14 requires emitted verbatim, and one
the owner ruled on directly (`OWNER-ANSWERS-2026-08-01.md` A5/B15: "unmapped
substrate status stays #1"). Corrected to #1. A sweep of all **13**
`RFC2-24 #N` citations in the corpus finds **0** remaining mismatches.

### What this episode says about the method

The dependency pass and its reviewer used the same evidence and reached
different answers, because "cites" and "relies on" are different predicates
and only one of them is mechanically cheap. The report already carried this
caveat — "citation is evidence of dependency, not proof of it" — and the pass
then leaned on the cheap predicate anyway. The bounded-imprecision table
below is the part of that caveat that was handled correctly; these four edges
are the part that was not.

## Verification

Run in the session that wrote this file:

```sh
python3 .syzygy/governance/contracts/candidates/scripts/build_dependency_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_contract_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py
```

Results: dependency index and contract index both regenerate with no drift;
the packet verifier reports PASS. `CONTRACT-DEPENDENCY-INDEX.md`'s "Graph
consistency" section now reports **no dangling edges** over 11 resolved
contracts — a statement with a denominator, over a population that was
actually examined.

**Note on the sequence.** These edits change every touched module's digest,
and therefore act 1's manifest argument. That is expected and handled: the
manifest is regenerated by script, never transcribed, and
`check_governance.py` CG-7 compares every act argument against its subject
before any act may be performed.
