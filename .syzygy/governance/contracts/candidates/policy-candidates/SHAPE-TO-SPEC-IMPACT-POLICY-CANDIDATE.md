# Shape-to-spec impact policy — candidate craft rule set

> **Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT`
> act.** Proposed at the 2026-08-11 structured-closure pass to close
> launch-gate question **E6** — "is there a defined propagation path for a
> shape change *after* specs exist: how affected specs are detected, who
> amends them, and how the interim disagreement is surfaced rather than
> hidden?"
>
> **The specific hole it fills.** The propagation fixture
> (`../round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`) states, of its
> own step 2: *"This step has no owner in any authority today."* Detection
> is the open half of E6. Steps 3 and 4 already have owners — VIS-2 and
> CC-REV-2 — and this policy does not restate them, it cites them.
> Identifiers `CC-IMPACT-1…7`; amended in place, never renumbered.

## The rule

**CC-IMPACT-1 — Every accepted specification declares what governs it.**
A specification carries, in a fixed and machine-readable place, four
declarations:

```text
capability identities        which capability (or capabilities) it specifies
doctrine rule IDs            the adopted rules it serves
contract clause IDs          the accepted clauses it relies on
topology identities          the placements it assumes
```

A declaration that is empty is an assertion that the specification relies
on nothing of that kind, and is reviewable as such. A declaration that is
*absent* is a defect: it makes the specification invisible to every sweep
below, and invisibility is exactly what this rule set exists to prevent.

**CC-IMPACT-2 — A shape delta performs a reverse-reference sweep.** When
an accepted doctrine rule, contract clause, or topology identity changes,
the change carries a sweep over the specification corpus for every
specification whose CC-IMPACT-1 declarations name the changed identity, or
whose requirements consume its vocabulary. The sweep is part of the change,
not a follow-up task.

**CC-IMPACT-3 — The sweep records four sets, with its denominator.** The
sweep's output names:

```text
population              every specification examined, counted
affected                specs a declaration or a consumption ties to the change
explicitly unaffected   specs examined and found untied, each with the reason
undecidable             specs whose relationship the sweep could not settle
```

A sweep that reports only the affected set has reported a numerator without
a denominator, and satisfies nothing (VIS-2; the denominator discipline is
this repository's verification rule 9, restated here because a rule that
lives only in operating procedure is not citable authority — which is the
defect CC-IMPACT-2 exists to fix).

**CC-IMPACT-4 — Undecidable impact renders as Unknown or contradiction,
never as unaffected.** A specification the sweep could not settle is
rendered `Unknown` with its settling evidence named, or `contradicted`
where the shape change and the requirement now disagree. Silence is not an
answer, and "not listed as affected" is never evidence of being unaffected.

**CC-IMPACT-5 — Every required amendment names its actor.** Each affected
specification's amendment is owned by a named actor before the change
lands. "The author" is a name; "someone" is not. Where the actor is the
owner (VIS-4), the amendment waits on the owner and the wait is visible.

**CC-IMPACT-6 — Affected specs move in the same logical change, or the
exception is owner-visible.** The default is CC-REV-2's merge invariant:
the shape change and its spec amendments land together, so mainline never
asserts the old truth. **CC-REV-2 admits no exception limb of its own** —
its only carve-out is doctrine's owner gate. This rule therefore adds
exactly one lawful alternative, and adds it explicitly rather than by
implication: an affected specification may lag its shape change **only**
under a recorded exception that names the specification, the reason, the
owning actor, and the condition that ends it — and the exception is
rendered on the specification itself, where a reader of the specification
sees it, not only in a change record they may never open.

**CC-IMPACT-7 — The path is exercised before it is relied on.** Before the
first real shape amendment after specifications exist, the propagation path
is run against a fixture with a known answer, blind: the reviewer derives
the affected, unaffected and undecidable sets without reading the answer,
and the comparison is recorded. A path that has never been run is a plan,
not a process.

## What this rule set does not do

- It does not define *how* the sweep is implemented. There is no script
  today, and this policy does not pretend one exists: the sweep may be
  mechanical or manual, and either way CC-IMPACT-3's four sets and its
  denominator are what make it checkable. Claiming a mechanical detector
  before one exists would be the precise failure VIS-2 forbids.
- It does not govern shape changes to *candidates*. Until a contract is
  accepted, changing it propagates to nothing, because no specification may
  cite an unaccepted clause.
- It does not create, imply, or authorize `openspec/`. Every specification
  it speaks of is future.

## Why each rule is here, in one line each

| Rule | The failure it prevents |
|---|---|
| CC-IMPACT-1 | a specification no sweep can see, because nothing about it is declared |
| CC-IMPACT-2 | detection deferred to a follow-up nobody files |
| CC-IMPACT-3 | a numerator with no denominator — "we checked" without "we checked what" |
| CC-IMPACT-4 | "not listed" quietly reading as "not affected" |
| CC-IMPACT-5 | an amendment everyone agrees is needed and nobody owns |
| CC-IMPACT-6 | mainline asserting the old truth while a spec silently lags |
| CC-IMPACT-7 | a propagation path first exercised on the day it is needed |

## Acceptance

This is a **candidate**. It comes into force only by its own
`CONFIRM CRAFT AMENDMENT` act, at a digest computed at the act — the route
the craft cluster defines. Nothing in it binds today, and no verdict of the
launch gate may cite it as in force until that act is performed. Its queue
row is minted with the shape-to-spec craft act in
`../../../decisions/PENDING-OWNER-DECISIONS.md`.
