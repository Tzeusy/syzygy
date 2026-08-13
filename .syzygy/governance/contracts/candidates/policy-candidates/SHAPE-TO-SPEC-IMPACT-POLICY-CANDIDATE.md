# Shape-to-spec impact policy — candidate craft rule set

> **Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT`
> act.** Proposed at the 2026-08-11 structured-closure pass to close
> launch-gate question **E6** — "is there a defined propagation path for a
> shape change *after* specs exist: how affected specs are detected, who
> amends them, and how the interim disagreement is surfaced rather than
> hidden?"
>
> **The specific hole it fills.** Detection is the open half of E6: the
> propagation fixture states, of its own step 2, *"This step has no owner in
> any authority today."* Steps 3 and 4 already have owners — VIS-2 and
> CC-REV-2 — and this policy **cites** them.
> Identifiers `CC-IMPACT-1…7`; amended in place, never renumbered.
>
> **Amended 2026-08-13** — the declaration is now generated rather than
> hand-authored, the trigger set is defined as *the same set* as the warrant
> set, the exception limb no longer weakens CC-REV-2 by side-clause, and the
> fixture is named by path and digest. The delta is
> `../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`; the
> findings it answers are RD-51's, raw at
> `../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`.
> **This file and `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` are one
> model** and are reviewed and offered together.

## The rule

**CC-IMPACT-1 — Every accepted specification declares what governs it, and
the declaration is generated.** A specification carries, in a fixed and
machine-readable place, a declaration over the **same six classes**
CC-SPEC-2 defines for a requirement:

```text
doctrine[]              contracts[]             policies[]
decisions[]             topology[]              parent_requirements[]
```

Three rules:

1. **The specification-level declaration is the union of its requirements'
   CC-SPEC-2 declarations, generated — never hand-authored.** A declaration
   narrower than that union is a defect, and a second hand-maintained list
   beside it is the duplicate-authority CC-REV-3 forbids.
2. **A specification specifies one capability** (CC-SPEC-1). The capability
   identity is a property of the specification, not a list.
3. An **empty** field asserts that the specification relies on nothing of
   that kind, and is reviewable as such. An **absent** declaration is a
   defect: it makes the specification invisible to every sweep below, and
   invisibility is exactly what this rule set exists to prevent.

*(Rewritten 2026-08-13, RD-51 f10 (blocking) and f16. The clause previously
defined four spec-level declaration classes of its own — capability
identities, doctrine rule IDs, contract clause IDs, topology identities —
hand-authored, with **nothing requiring them to match the requirements'
warrants**. A specification whose REQ-3 named `RFC6-19` while its
declaration listed only `RFC6-18` satisfied both policies and was invisible
to CC-IMPACT-2's sweep: the fixture's own headline failure case, reproduced
inside the policy written to catch it. It also wrote "which capability (or
capabilities) it specifies" while CC-SPEC-1 mandated **one**.)*

**CC-IMPACT-2 — A shape delta performs a reverse-reference sweep, and the
trigger set is the warrant set.**

> **The identities that can trigger a sweep are exactly the identities that
> can warrant a requirement** — CC-SPEC-2's six classes, and no others.

When an adopted doctrine rule, an accepted contract clause, an approved
craft/policy clause, a recorded owner decision, an accepted topology
identity, or an accepted parent requirement or specification changes, the
change carries a sweep over the specification corpus for every
specification whose CC-IMPACT-1 declarations name the changed identity, or
whose requirements consume its vocabulary. **The sweep is part of the
change, not a follow-up task.**

Stating the trigger set as an *identity* rather than as a second enumeration
is deliberate: two lists drift, and the drift is silent. Any class that
becomes warrantable becomes sweepable in the same act; any class that cannot
trigger a sweep may not warrant a requirement.

*(Rewritten 2026-08-13, RD-51 f9 (blocking). The triggers were "an accepted
doctrine rule, contract clause, or topology identity" — three classes —
while CC-SPEC-2 admitted five warrant classes including owner decisions. A
requirement lawfully warranted by an owner decision was invisible when that
decision was amended: warrantable-but-unsweepable, which is silent staleness
by construction. The two enumerations are now one set by definition.)*

**CC-IMPACT-3 — The sweep records four sets, with its denominator and its
method.** The sweep's output names:

```text
population              every specification and requirement examined, counted
affected                those a declaration or a consumption ties to the change
explicitly unaffected   those examined and found untied — each with the reason
                        AND the method that established untiedness
undecidable             those whose relationship the sweep could not settle,
                        each with what would settle it
```

**The reason and the method are two different things, and both are
required.** "Does not declare the changed identity" is an *observation*; if
declaration-matching is the whole method, the sweep says so, and everything
that method cannot decide routes to `undecidable` under CC-IMPACT-4 rather
than to `explicitly unaffected`. A true reason producing a wrong answer,
carried by a denominator and full compliance, is the failure mode this limb
exists to prevent.

A sweep that reports only the affected set has reported a numerator without
a denominator, and satisfies nothing. The denominator discipline itself is
**CC-KNOW-16**'s (candidate, P-12, `CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`) —
cited, not restated; this clause is that rule's application to the
specification corpus, and if CC-KNOW-16 is not approved the discipline still
rests on VIS-2.

*(Amended 2026-08-13, RD-51 f11 and f20. Two defects: the clause named
**CC-IMPACT-2** as "the defect this exists to fix" when the defect described
was its own, contradicting the file's own table; and it justified itself by
a claim of absence — that the denominator discipline "lives only in
operating procedure" — made with no sweep, when CC-KNOW-16 in the same
directory already carried it. The method limb is f20's repair.)*

**CC-IMPACT-4 — Undecidable impact renders as Unknown or contradiction,
never as unaffected.** A specification the sweep could not settle is
rendered `Unknown` with its settling evidence named, or `contradicted`
where the shape change and the requirement now disagree. Silence is not an
answer, and "not listed as affected" is never evidence of being unaffected
(VIS-2, applied to the sweep's own output).

**CC-IMPACT-5 — Every required amendment names its actor, and the sweep
names one too.** Each affected specification's amendment is owned by a named
actor before the change lands. **The sweep itself has an actor**: the shape
change's author performs it, and a party other than that author confirms it
is adequate — the CC-TEST-4 pattern, because a sweeper grading their own
denominator is the unassigned judgment E5 exists to remove. "The author" is
a name; "someone" is not. Where the actor is the owner (VIS-4), the
amendment waits on the owner and the wait is visible.

*(Sweep actor added 2026-08-13, RD-51's finding that CC-IMPACT-2's "the
change carries a sweep" is passive voice, and that after CC-IMPACT-1…7
detection had acquired a *requirement* and still had **no owner** — which
was the exact words of the hole the policy was written to close.)*

**CC-IMPACT-6 — Affected specs move in the same logical change. There is no
exception today.** CC-REV-2's merge invariant governs, unmodified and
uncarved: the shape change and its spec amendments land together, so
mainline never asserts the old truth, and **behavioral specs are the first
population CC-REV-2 names**. CC-REV-2 admits no exception limb of its own;
its only carve-out is doctrine's owner gate.

**This clause creates no alternative.** A lagging specification is lawful
only if CC-REV-2 is **itself amended**, in place, through the craft
cluster's own amendment act. That amendment is offered separately —
`CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md` in this directory,
queued as **P-44** — and it carries five required elements plus a confirmer
distinct from the change's author. **Until that act is performed, no lawful
lag exists**, and a shape change whose spec amendments cannot land with it
does not merge.

*(Rewritten 2026-08-13, RD-51 f1 (blocking). The clause previously said it
"adds exactly one lawful alternative" permitting an affected specification
to lag under a four-field recorded exception. Three independent problems.
**It weakened an owner-approved clause by writing a new clause beside it
rather than amending it** — and both would sit in cluster tier 2, where the
cluster's own precedence rule addresses cross-tier weakening only, so
nothing would arbitrate two clauses giving opposite answers to "may this
merge land?". **It created a second home for the merge invariant**, which
CC-REV-3 forbids. **The exception had no confirmer** — the author of the
shape change would write their own exception to CC-REV-2 and merge, which is
the CC-REV-2 violation with a form attached; compare CC-TEST-1 and CC-TEST-4,
the cluster's two approved exception mechanisms, both of which name a second
party. A fourth fact: the predecessor fixture records this same limb as
previously **invented and withdrawn** for want of any craft clause containing
it, and the candidate reinstated it. Creating a rule by act is lawful;
creating one that overrides a different approved clause without amending it
is not.)*

**CC-IMPACT-7 — The path is exercised before it is relied on.** Before the
first real shape amendment after specifications exist, the propagation path
is run **blind** against a named fixture with a known answer:

```text
fixture   ../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md
sha256    685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0
answer    ../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md
          — a separate file, which the administrator does not open
```

Four requirements, each of which the clause previously lacked:

1. **The administrator is fresh-context** per CC-REV-1 — not the author of
   the sweep method, not sharing its session.
2. **The pass criterion is the answer key's**, quoted there and not
   restated here: the derived `affected` set contains every golden affected
   requirement, the designated undecidable relationship is never filed as
   `explicitly unaffected`, and the population is stated with every
   requirement placed in exactly one set.
3. **Every divergence carries a recorded disposition** (CC-REV-6), whether
   the run passes or fails.
4. **The consequence of failure is stated: the path is not relied on until
   a passing run exists.** A recorded failing run satisfies this clause's
   *record* obligation and does not satisfy the clause.

If the fixture's bytes no longer match the digest above, the run is void:
supersede the fixture rather than editing it.

*(Rewritten 2026-08-13, RD-51 f13 and f8. The clause previously required
only that "the comparison is recorded" — so a blind run that missed every
impacted specification, recorded honestly, satisfied it in full — and named
no fixture, no administrator standard, and no consequence. The only fixture
then in the corpus was itself defective: its golden ANSWER graded "a
recorded exception" as correct while its own governing step 4 said CC-REV-2
admits no such limb, so a reviewer answering correctly was marked divergent.
Fixture 2 supersedes it.)*

## What this rule set does not do

- It does not define *how* the sweep is implemented. There is no script
  today, and this policy does not pretend one exists: the sweep may be
  mechanical or manual, and either way CC-IMPACT-3's four sets, its
  denominator and its **method** are what make it checkable. Claiming a
  mechanical detector before one exists would be the precise failure VIS-2
  forbids.
- It does not define **"consumes its vocabulary"**. `[Unknown]` — the term
  is undefined, and its undefinedness decides real cases: a requirement
  impacted at one remove through another clause's composition rule can be
  read either way. CC-IMPACT-4 is what keeps that honest — such a case is
  `undecidable`, never `unaffected` — but the term itself remains an open
  finding against this file (RD-51's G section), not a closed one.
- It does not govern shape changes to *candidates*. Until a contract is
  accepted, changing it propagates to nothing, because no specification may
  cite an unaccepted clause.
- It does not create, imply, or authorize `openspec/`. Every specification
  it speaks of is future.

## Why each rule is here, in one line each

| Rule | The failure it prevents |
|---|---|
| CC-IMPACT-1 | a specification no sweep can see, and a declaration that may disagree with the requirements it summarizes |
| CC-IMPACT-2 | a warrant class that can authorize a requirement but cannot trigger a sweep |
| CC-IMPACT-3 | a numerator with no denominator, and a true reason producing a wrong answer |
| CC-IMPACT-4 | "not listed" quietly reading as "not affected" |
| CC-IMPACT-5 | an amendment everyone agrees is needed and nobody owns; a sweeper grading their own sweep |
| CC-IMPACT-6 | an approved clause weakened by a side-clause nobody had to amend |
| CC-IMPACT-7 | a propagation path first exercised on the day it is needed, with no pass mark |

## Acceptance

This is a **candidate**. It comes into force only by its own
`CONFIRM CRAFT AMENDMENT` act, at a digest computed at the act — the route
the craft cluster defines. Nothing in it binds today, and no verdict of the
launch gate may cite it as in force until that act is performed. Its queue
row is **P-42** in `../../../decisions/PENDING-OWNER-DECISIONS.md`, and it
is offered **together with** the specification-acceptance policy (P-41):
CC-IMPACT-1 generates from CC-SPEC-2, and CC-IMPACT-2's trigger set *is*
CC-SPEC-2's warrant set, so accepting one without the other reintroduces the
two blocking defects this amendment removed.
