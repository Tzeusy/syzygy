# Shape-to-spec impact policy — candidate craft rule set

> **Proposed post-act amendment — non-binding.** Acts 6 and 7 confirmed the
> predecessor CC-IMPACT bytes at sha256
> `cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0`.
> Those predecessor bytes remain the binding mainline policy. The edited
> bytes below are a draft successor: they do not bind, replace, or amend the
> confirmed policy unless an independent review is completed and the owner
> confirms the exact proposed digest in a new act.
>
> Identifiers `CC-IMPACT-1…7` remain stable and are never renumbered. This
> file and `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` remain one model.
> The plain-language change summary, exact before/after text, evidence,
> non-goals, and review requirements are in
> `../round-2026-08l/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-3.md`.
> Evidence for the earlier blind propagation exercise remains resolvable in
> `../round-2026-08g/reviews/DISPOSITION-REGISTER.md`; this banner does not
> repeat or independently assert that record's verdict.

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

**CC-IMPACT-2 — A shape delta performs a reverse-reference sweep, and the
trigger set is the requirement-provenance set.**

> **The identities that can trigger a sweep are exactly the identities a
> requirement may cite as governing provenance** — CC-SPEC-2's six fields,
> and no others. This set explains why requirement text belongs; it is not the
> work-warrant set that authorizes creating or prioritizing work.

When an adopted doctrine rule, an accepted contract clause, an approved
craft/policy clause, a recorded owner decision, an accepted topology
identity, or an accepted parent requirement or specification changes, the
change carries a sweep over the specification corpus for every
specification whose CC-IMPACT-1 declarations name the changed identity, or
whose requirements consume its vocabulary. **The sweep is part of the
change, not a follow-up task.**

**`Consumes its vocabulary` remains undefined by accepted authority.** This
amendment does not decide that pre-existing ambiguity. Declaration matching is
still usable; any additional relationship whose answer depends on the
undefined phrase is `undecidable` under CC-IMPACT-4 and renders Unknown with
what would settle it. It may not be classified as unaffected.

Stating the trigger set as an *identity* rather than as a second enumeration
is deliberate: two lists drift, and the drift is silent. Any class added to
requirement provenance becomes sweepable in the same act; any class that
cannot trigger a sweep may not serve as requirement provenance.

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
a denominator, and satisfies nothing. The denominator discipline is also
stated by **CC-KNOW-16**; whether or not that separate clause is in force at
the sweep's act, this clause applies the discipline to the specification
corpus and VIS-2 supplies its governing basis.

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
is adequate. The confirmer's independence from the sweep author is the rule;
no external pattern is needed to interpret it, because a sweeper grading their
own denominator is the unassigned judgment E5 exists to remove. "The author"
is a name; "someone" is not. Where the actor is the owner (VIS-4), the
amendment waits on the owner and the wait is visible.

**CC-IMPACT-6 — Affected specs move in the same logical change; this policy
creates no exception.** *Same logical change* means the shape delta and every
specification amendment it requires land in one merge transaction, so mainline
never contains one without the other. CC-REV-2's merge invariant governs,
unmodified and uncarved, and **behavioral specs are the first population
CC-REV-2 names**. CC-REV-2 admits no exception limb of its own; its only
carve-out is doctrine's owner gate.

**This clause creates no alternative.** The owner declined the previously
offered lagging-specification exception, so it supplies no authority and this
amendment does not revive it. A lagging specification could become lawful only
if CC-REV-2 were itself amended in place through a new craft act. Until such an
act is performed, no lawful lag exists, and a shape change whose specification
amendments cannot land with it does not merge.

**CC-IMPACT-7 — The path is exercised before it is relied on.** Before any
shape amendment relies on the propagation path, a passing **blind** run must
exist against this named fixture with a known answer:

```text
fixture   ../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md
sha256    685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0
answer    ../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md
          — a separate file, which the administrator does not open
```

The exercise has four requirements:

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

## What this rule set does not do

- It does not require or assert the existence of a sweep script. A sweep may be
  mechanical or manual, and either way CC-IMPACT-3's four sets, its denominator
  and its **method** are what make it checkable. Each sweep record says which
  method it actually used.
- It does not define **"consumes its vocabulary"**. The operative rule above
  exposes that pre-existing ambiguity and routes dependent cases to
  `undecidable`, never `unaffected`; a separate authorized amendment is needed
  to define the term.
- It does not govern shape changes to *candidates*. Until a contract is
  accepted, changing it propagates to nothing, because no specification may
  cite an unaccepted clause.
- It does not create, imply, or authorize specification work. Specification
  authoring, adoption, and implementation each require their own authority;
  this policy only governs propagation once the relevant artifacts exist.

## Why each rule is here, in one line each

| Rule | The failure it prevents |
|---|---|
| CC-IMPACT-1 | a specification no sweep can see, and a declaration that may disagree with the requirements it summarizes |
| CC-IMPACT-2 | a requirement-provenance class that cannot trigger a sweep |
| CC-IMPACT-3 | a numerator with no denominator, and a true reason producing a wrong answer |
| CC-IMPACT-4 | "not listed" quietly reading as "not affected" |
| CC-IMPACT-5 | an amendment everyone agrees is needed and nobody owns; a sweeper grading their own sweep |
| CC-IMPACT-6 | an approved clause weakened by a side-clause nobody had to amend |
| CC-IMPACT-7 | a propagation path first exercised on the day it is needed, with no pass mark |

## Amendment acceptance

The predecessor CC-IMPACT policy is already in force at the digest in the top
banner. This proposed successor remains non-binding until the owner confirms
its exact digest in a new craft act after the required independent review.
It must be reviewed and offered with the specification-acceptance policy:
CC-IMPACT-1 generates from CC-SPEC-2, and CC-IMPACT-2's trigger set is
CC-SPEC-2's provenance set. Drafting, review, or a pull request is not that
act.
