# Shape-to-spec impact policy

> **Authority depends on an exact-digest owner act, not this banner.** These
> bytes are a proposal while no performed owner Decision names their SHA-256.
> From an act that names that digest, the same bytes are the confirmed
> successor; no edit is needed. Decisions are selected under CC-SPEC-10.
> Drafting, review, a commit, or a pull request changes no authority.
>
> IDs `CC-IMPACT-1` through `CC-IMPACT-7` stay stable. This policy and
> `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` form one model. The proposal,
> history, exact mapping, and review contract are in
> `../round-2026-08l/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-3.md`.

## Shared terms and results

A **shape delta** changes an adopted doctrine rule, accepted contract clause,
approved policy clause, recorded owner Decision, accepted topology identity,
or accepted parent requirement/specification. An **impact sweep** fixes its
inputs at one source revision before matching. It creates its durable record
before population rows.

Every requirement, direct specification relationship, and specification is
placed in exactly one result, using this precedence:

1. **contradicted** — two authoritative claims in one scope cannot both hold;
2. **affected** — the stated method establishes a relationship to the delta;
3. **undecidable** — the method cannot settle the relationship; or
4. **explicitly unaffected** — the method establishes no relationship and
   records why.

`Undecidable` renders Unknown. It is not an unaffected result.

## **CC-IMPACT-1 — Generate each specification's authority declaration**

- **Purpose:** Make every accepted specification discoverable without a second
  authority list.
- **Inputs/population:** All requirement declarations under CC-SPEC-2.
- **Decision:** For each of the same six fields—`doctrine`, `contracts`,
  `policies`, `decisions`, `topology`, and `parent_requirements`—generate the
  set union of stable identities from all requirements. Never hand-author it.
  A present empty field asserts an empty union; an absent field is a defect.
  Record one capability identity as a specification property, not a list.
- **Possible results:** Satisfied when all six generated fields equal their
  requirement unions; Not satisfied for a proved mismatch or second list;
  otherwise Unknown.
- **Missing evidence:** An absent field, requirement declaration, or resolvable
  identity is Unknown and cannot support an unaffected result.
- **Retained evidence:** Generator/version, requirement inputs, six expected
  unions, six actual fields, comparison, and capability identity.
- **Sources:** CC-SPEC-1; CC-SPEC-2; CC-REV-3.

## **CC-IMPACT-2 — Sweep every provenance-triggered relationship**

- **Purpose:** Ensure every authority class that can govern a requirement can
  also trigger propagation.
- **Inputs/population:** The changed identities and CC-SPEC-2's same closed six
  provenance classes.
- **Decision:** The shape-delta author carries a reverse-reference sweep in the
  same change. Match declarations and test other authority-defined relationships.
  The phrase `consumes its vocabulary` has no definition in this policy: at the
  sweep revision, apply only an eligible accepted definition with exact identity
  and digest. Without one, every case depending on that phrase is undecidable.
- **Possible results:** Satisfied when every changed identity and dependent
  relationship enters the exhaustive sweep; Not satisfied for a proved
  omission; otherwise Unknown.
- **Missing evidence:** A missing definition or unresolvable relationship is
  undecidable, records what would settle it, and never becomes unaffected.
- **Retained evidence:** Revision, changed identities, definition identity/
  digest if any, match method, and unresolved relationships.
- **Sources:** VIS-2; CC-SPEC-2. These provenance fields explain why text belongs;
  RFC1-25 separately governs permission to create or prioritize work.

## **CC-IMPACT-3 — Freeze populations and partition every item**

- **Purpose:** Produce a reproducible denominator and deterministic parent result.
- **Inputs/population:** First select every accepted specification at one revision
  by CC-SPEC-10's Decision rule, then enumerate every stable requirement entry,
  including retired entries. Do not select from declaration matches or filesystem
  presence. Before rows exist, `population-construction` records revision,
  candidate Decisions/digests, selection trace, method, and both counts.
- **Decision:** Classify every requirement by the shared precedence. A provenance
  match or an authority-defined changed obligation, boundary, oracle, mapping, or
  vocabulary is affected; incompatible claims are contradicted; unsupported
  relationship tests are undecidable; a retired row may be unaffected only with
  retirement as reason unless the delta changes retirement.

  For each specification and field, compute the expected CC-SPEC-2 requirement
  union and read the actual CC-IMPACT-1 field. Before matching the delta, create
  a reconciliation row for every identity in the union of expected and actual
  entries, recording presence on both sides; add a field-absent sentinel when
  the field is absent. Thus a present empty field cannot hide an expected
  identity. Mark each row's projection check `match`, `generated-missing`, or
  `generated-extra`. Either mismatch makes CC-IMPACT-1 Not satisfied and blocks
  CC-IMPACT-6; it is not a contradiction because the generated field is not
  authority. Classify impact from the expected authoritative identity when
  present: affected if it changed, otherwise explicitly unaffected. An
  actual-only, malformed, unresolvable, or field-absent row is undecidable.
  Use contradicted only for two incompatible authoritative claims. Record method
  and reason on every row.

  Derive each specification once over its reconciliation and child-requirement
  rows using the same precedence.
- **Possible results:** Four disjoint, exhaustive requirement sets; four disjoint,
  exhaustive reconciliation sets; and four disjoint, exhaustive specification
  sets. A numerator without all denominators is Not satisfied.
- **Missing evidence:** Record pre-enumeration failure in `population-construction`,
  render/link it in human and machine projections, and emit no child rows. Later
  uncertainty is an undecidable row. Zero matches never shrink a population.
- **Retained evidence:** Selection record; specification, requirement, and per-
  field expected/actual counts; every row and reason; method; four-set totals;
  parent derivation; and projection links.
- **Sources:** VIS-2; CC-SPEC-10.

## **CC-IMPACT-4 — Keep Unknown and contradiction durable until lawful exit**

- **Purpose:** Stop silence, review opinion, or an old result from enabling merge.
- **Inputs/population:** Every undecidable or contradicted population section,
  requirement row, reconciliation row, and specification result.
- **Decision:** The owning row records unsettled facts or both conflicting claims
  and a settling condition. Human and machine views render the same linked
  Unknown/contradiction. A generated-declaration defect exits by correcting the
  generator/output and rerunning CC-IMPACT-1 and the sweep, never by owner
  adjudication. A merge-relevant contradiction exits only through an
  eligible owner Decision selected for the purpose `adjudicate` by CC-SPEC-10's
  generic act-type/subject/digest/scope and explicit-supersession rule. The
  Decision names the contradiction and resolution; a review disposition is not
  eligible. After required authority amendments, run a new sweep at a new
  revision. Only its non-undecidable, non-contradicted result may proceed; retain
  the earlier row as history.
- **Possible results:** Satisfied when every open result is rendered and blocks;
  Not satisfied when one is hidden or bypassed; otherwise Unknown.
- **Missing evidence:** Missing owner Decision, authority amendment, or new sweep
  keeps the result open and prevents CC-IMPACT-6.
- **Retained evidence:** Owning rows, links, selected adjudication Decision and
  supersession trace, old/new revisions, amendments, and new result.
- **Sources:** Typed-authority contradiction rule; RFC1-25 `adjudicates`;
  RFC3-15; RFC3-16.

## **CC-IMPACT-5 — Assign authors and independent confirmation**

- **Purpose:** Give every sweep and required amendment accountable actors.
- **Inputs/population:** The sweep and every affected specification amendment.
- **Decision:** Name the shape-delta author as sweep author, a different named
  party as confirmer, and one named actor for each amendment. Owner-only work
  waits visibly for the owner.
- **Possible results:** Satisfied when all actors are named and independence is
  established; Not satisfied for self-confirmation or an unassigned amendment;
  otherwise Unknown.
- **Missing evidence:** Unknown actor identity or independence blocks reliance.
- **Retained evidence:** Actor assignments, confirmation record, exact sweep
  revision/digest, verdict, and dispositions.
- **Sources:** VIS-4; CC-REV-1; CC-REV-6.

## **CC-IMPACT-6 — Land shape and specification changes atomically**

- **Purpose:** Keep mainline from asserting the new shape with old specifications.
- **Inputs/population:** The shape delta and every amendment required by its
  current sweep.
- **Decision:** Land all of them in one merge transaction. An undecidable or
  contradicted specification, or any CC-IMPACT-1 Not satisfied/Unknown result,
  blocks that transaction. This policy creates no lagging-specification
  exception; the declined proposal supplies no authority. Only an owner-approved
  amendment to CC-REV-2 could change that rule.
- **Possible results:** Satisfied only by the atomic transaction; Not satisfied by
  a partial merge; Unknown while impact or authority remains unresolved.
- **Missing evidence:** Without exact transaction membership and current sweep
  evidence, do not merge.
- **Retained evidence:** Sweep, amendment set, exact revisions, merge transaction,
  and unresolved blockers.
- **Sources:** CC-REV-2; VIS-4.

## **CC-IMPACT-7 — Prove the path before relying on it**

- **Purpose:** Exercise propagation against a known answer before real use.
- **Inputs/population:** Fixture
  `../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` at SHA-256
  `685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0`
  and answer key
  `../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md` at
  SHA-256 `48286cc113ddfb797eb368c624122c77dc509cf7f036ab44f404109b98da4e3e`.
- **Decision:** A fresh-context administrator who cannot open the answer key runs
  blind and freezes the result digest. A different named CC-IMPACT-5 confirmer
  then verifies both input digests, opens the key, and grades: all golden
  affected requirements are affected, its designated undecidable case is not
  unaffected, and every requirement appears once. Disposition every divergence.
- **Possible results:** Satisfied only by a passing run; Not satisfied by a
  failing run or digest mismatch; Unknown when evidence is absent or invalid.
- **Missing evidence:** Do not rely on the path. Supersede a changed fixture or
  key; never edit one under its recorded digest.
- **Retained evidence:** Both paths/digests, administrator and grader identities,
  frozen result digest, method, complete results, key comparison, verbatim
  verdict, and dispositions.
- **Sources:** CC-REV-1; CC-REV-6.
