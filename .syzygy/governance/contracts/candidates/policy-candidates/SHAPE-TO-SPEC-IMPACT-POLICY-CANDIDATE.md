# Shape-to-spec impact policy — craft rule set

> **Candidate before an exact-digest act; confirmed successor after one.**
> Authority state resolves from the active acceptance record. These bytes are a
> proposal while no performed owner act names their exact sha256. If such an
> act later names this exact digest, these same bytes are the confirmed
> successor from that act; no banner edit is needed. The
> 2026 acts identify the predecessor digests they confirmed and do not bind a
> different digest. Whether those predecessor bytes are current or superseded
> is likewise answered by the act record, never inferred from this banner.
> Drafting, review, a commit, or a pull request changes no authority state.
>
> Identifiers `CC-IMPACT-1…7` remain stable and are never renumbered. This
> file and `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` remain one model.
> The plain-language change summary, exact before/after text, evidence,
> non-goals, and review requirements are in
> `../round-2026-08l/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-3.md`.
> The historical blind-propagation evidence record is
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

**Resolve `consumes its vocabulary` at the sweep's named source revision.**
This amendment supplies no definition. If an adopted, accepted, approved, or
recorded authority eligible under CC-SPEC-2 at that revision supplies a
definition, the sweep cites and applies its exact identity and digest. If none
does, declaration matching remains
usable but every additional relationship whose answer depends on the phrase is
`undecidable` under CC-IMPACT-4 and renders Unknown with what would settle it.
It may not be classified as unaffected.

Stating the trigger set as an *identity* rather than as a second enumeration
is deliberate: two lists drift, and the drift is silent. Any class added to
requirement provenance becomes sweepable in the same act; any class that
cannot trigger a sweep may not serve as requirement provenance.

**CC-IMPACT-3 — The sweep records a fixed population and four result sets,
with its denominator and method.** Before matching any identity or vocabulary, freeze the **input
corpus**: every accepted specification at one named source revision and every
stable requirement entry in those specifications, including entries marked
retired. Enumerate specifications by applying CC-SPEC-10's governing-record
selection to the owner-Decision corpus at that revision, not from declaration
matches or a filesystem guess; then enumerate every stable requirement entry
in each selected specification. Record the revision, record-selection results,
enumeration method, specification count, and requirement count. An unresolved
record contradiction stops population construction before result rows exist.
The durable sweep record is created first; its **population-construction**
section owns this `Unknown` and records the source revision, candidate adoption
record identities and digests, conflicting or missing supersession facts, and
what owner Decision would settle them. Human and machine impact projections
render the same Unknown and link to that section. No requirement or
specification result rows are emitted until the contradiction is settled. A
missing declaration or zero-match result never removes an item from this input
corpus.

For each requirement in that fixed corpus, **affected** means the method
establishes either that its CC-SPEC-2 provenance names the changed identity or
that the shape delta changes an authority-defined obligation, boundary,
oracle, coverage mapping, or defined vocabulary the requirement uses. A
relationship that depends on the undefined `consumes its vocabulary` phrase is
`undecidable`, not affected or unaffected. A retired entry stays in the
denominator and may be explicitly unaffected with retirement as the reason,
unless the delta changes the retirement fact or any condition for interpreting
or reversing it.

**`Contradicted`, defined.** The method establishes that the changed
authoritative claim and the requirement cannot both be satisfied in the same
declared scope. Classification precedence is deterministic: `contradicted`
first, then `affected`, then `undecidable`, then `explicitly unaffected`.

The requirement-level output names:

```text
population              every stable requirement entry in the frozen input
                        corpus, counted
affected                a declaration match or other relationship established
                        by the stated method
contradicted            the changed authority and requirement cannot both be
                        satisfied — each with both conflicting claims
explicitly unaffected   the method establishes no tie — each with the reason
                        AND the method that established untiedness
undecidable             the method cannot settle the relationship — each with
                        what would settle it
```

The four result sets are disjoint and exhaustive: every requirement in the
population appears in exactly one.

**Enumerate direct specification relationships before deriving the
specification result.** For each specification, read exactly CC-IMPACT-1's six
generated fields. Record every `(specification identity, field name, authority
identity)` entry in source order, plus the per-field entry counts; an empty
field contributes a recorded zero, while an absent field contributes one
`undecidable` sentinel row because CC-IMPACT-1 makes absence a defect. This
direct-relationship population is fixed before matching.

Classify every direct row in the same four result sets and precedence as
requirements: `affected` when its authority identity equals the changed
identity; `explicitly unaffected` when well-formed exact-identity comparison
establishes inequality; `undecidable` when the entry is absent, malformed, or
unresolvable; and `contradicted` when the generated entry disagrees with the
requirements' CC-SPEC-2 union or another authoritative specification entry.
Record the comparison method and reason on every row. The direct-row sets are
disjoint and exhaustive.

Then derive one specification result over its direct rows and child requirement
rows:

1. **contradicted** if at least one direct row or child requirement is
   `contradicted`;
2. otherwise **affected** if at least one direct row or child requirement is
   `affected`;
3. otherwise **undecidable** if at least one direct row or child requirement is
   `undecidable`; or
4. otherwise **explicitly unaffected**, with the method and reason.

Every specification in the frozen corpus appears in exactly one of those
four specification sets. This is the requirement-to-specification propagation
rule: a contradicted requirement makes its parent specification contradicted;
otherwise an affected requirement makes its parent specification affected; an
undecidable requirement makes its parent specification undecidable unless a
higher-precedence child result applies.

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

**CC-IMPACT-4 — Undecidable impact renders as Unknown; contradiction remains
inside the exhaustive partition.** The sweep record's `undecidable` requirement
or specification row is the owning record: it names the unsettled relationship
and what would settle it. The parent specification's impact result is recorded
as `Unknown`, identified as an impact result, and every human view and machine
projection renders that same result with a link to the row. A `contradicted`
row instead links the two authoritative claims that cannot be satisfied
together. Silence is not an answer, and "not listed as affected" is never
evidence of being unaffected (VIS-2, applied to the sweep's own output).
A specification whose impact result is `Unknown` or `contradicted` prevents the
shape delta from satisfying CC-IMPACT-6: the delta does not merge until the
relationship is settled or adjudicated and every required specification
amendment can land in the same logical change. This policy defines no exception
that treats an undecidable specification as unaffected.

**Merge-relevant adjudication is an owner Decision, not a review
disposition.** The Decision lives in `.syzygy/governance/decisions/`, is
selected under CC-SPEC-10's governing-record rule, names the contradiction row
and both conflicting claims, and records the owner's resolution and any
superseded Decision (RFC3-15, RFC3-16). After that Decision and every authority
amendment it requires exist, run a new sweep at the new source revision. The
prior sweep retains its historical `contradicted` row; the new sweep links the
Decision and classifies the relationship by the four-set precedence above.
Only that new non-Unknown, non-contradicted current result can satisfy this
gate before CC-IMPACT-6 is evaluated.

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
  resolves definition availability at the named source revision and routes a
  missing definition to `undecidable`, never `unaffected`; a separate
  authorized amendment is needed to add a definition.
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

The active acceptance record determines this exact file's state as the top
banner describes: proposal when no performed owner act names its digest,
confirmed successor from an act that does. It must be reviewed and offered
with the specification-acceptance policy: CC-IMPACT-1 generates from
CC-SPEC-2, and CC-IMPACT-2's trigger set is CC-SPEC-2's provenance set.
Drafting, review, a commit, or a pull request is not that act.
