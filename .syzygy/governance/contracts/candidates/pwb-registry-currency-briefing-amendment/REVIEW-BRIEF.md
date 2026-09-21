# Review brief — registry currency bounds and the briefing ceiling

> **Candidate — binds nothing.** This brief states what an independent
> reviewer is to be given and what they are to decide. It is not a review,
> contains no verdict word, and no review has been run against this
> package. Effect over the subject would come from one superseding
> `adopt-registry-entry` owner act and from nothing else.

## Status of the package under review

Drafted to step 2 of
`.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
and stopped there, as the drafting authorization requires. No self-review
was performed.

## What the reviewer is given, and nothing else

CC-REV requires a fresh context holding only the artifact, its governing
references and the acceptance criteria. For this package that is:

**The artifact under review** — the five files of
`.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, this brief,
`OWNER-DECISION-PACKET.md`, `PWB-EFFECT-AMENDMENT-MANIFEST.txt`), the
single patch under `proposed/`, and
`scripts/build_pwb_registry_currency_briefing_amendment.py`.

**The subject** —
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
at its current bytes.

**Governing references** —

- `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
  (rows P-69, P-72, P-77, P-78 and the cross-cutting readings).
- `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
  and its predecessor
  `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`, for
  the ceremony shape and the supersession boundary.
- `RFC2-9` and `RFC2-10`, by identifier, located through
  `DIRECTIVE-REGISTER.md` and read at their defining clause.
- `PWB-REQ-006` and `PWB-REQ-007` in
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`.
- `NORMATIVE-CHANGE-WORKFLOW.md` and `SEMANTIC-DELTA-TEMPLATE.md`.
- `packages/cap1-core/src/staleness.ts`, for the judge's five return
  paths and the `CurrencyBoundDeclaration` shape.
- `apps/three-surface-poc/src/routes.ts`, for the two current response
  ceilings and the closed identity union.

**Deliberately withheld** — the design funnels under `docs/design/`. They
are where these fields were designed and they recommend; the ruling record
decides, and on P-69 the owner took an arm the funnel did not recommend. A
reviewer reading the funnel first is reading a superseded recommendation
as if it were the warrant.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Is the change class right?** The delta assigns Normative with three
   stated reasons. Is any of them wrong, and is Structural or Clarifying
   the better class?
2. **Is the subject untouched?** Confirm the registry entry's bytes in the
   tree are the bytes the act in force bound, that the package's only
   proposed change is the unified diff under `proposed/`, and that no act
   record, no superseded record and no manifest of a prior act is edited.
3. **Does the package verify, and does its verification mean anything?**
   Run `--check` and `--selftest`. `--selftest` mutates ten predicates in
   turn; confirm each mutation is one the package would actually be wrong
   about, not a tautology, and name any predicate the package asserts that
   no mutant covers.
4. **Is the thirteen-class population complete and disjoint?** The delta
   claims the thirteen rows cover every claim identity the shape model
   mints and nothing else. Check it against the nine extraction classes
   and the six claim-id families in the two source files, and say what a
   class minted in future code would do.
5. **Do the seven `currencyBoundSemantics` sentences say what `RFC2-9`
   and `RFC2-10` require, and do they say anything they must not?** In
   particular: does `undeclaredClass` correctly leave the claim Unknown
   rather than minting a freshness value; does `outOfBoundResult` fail
   closed on all three bases; and does `boundChange` restate `RFC2-9`
   without narrowing or widening it?
6. **Does the third ceiling sit correctly against `PWB-REQ-006`?** The
   ruling minted it; the question for review is whether the sentence's
   scope — a derived read-only machine view composed from an evaluation
   already served under `maxMachineResponseBytes` — is exact enough that
   an implementer cannot serve a fourth kind of body under it.
7. **Is the impact ledger's method sound and its denominator honest?**
   Re-run both sweeps. Confirm the counts, the 43-file partition
   arithmetic, and that the stated remainders are the only ones.
8. **Is the adoption plan indivisible as claimed, and is anything missing
   from it?** In particular, is any consumer of the subject's bytes absent
   from the ledger's tables 2 and 3?
9. **Does the package avoid quoting any act argument?** Confirm no
   64-hex digest appears beside an act phrase anywhere in the package, and
   that the packet's reasoning for that is correct rather than merely
   convenient.
10. **Does the package claim any authority it does not have?** Confirm no
    file labels anything accepted, adopted, signed off or in force; that
    every banner says the package binds nothing; and that the separate
    continuation direction and the two separate specification packages are
    described as gates rather than as things this package supplies.

## Out of scope for this review

- The thirteen `maxAgeMs` values and the 20,480-byte ceiling. They are the
  owner's numbers. A reviewer may say a value is internally inconsistent
  with a sentence in the same file, and should; a reviewer does not choose
  them.
- The derived read-only machine view **category**, which a sibling
  specification package declares.
- The undeclared-class disclosure route, which a separate CC-REV-2
  clarification scenario owns.
- Whether to perform the act. That is the owner's, and only the owner's.

## Recording

Raw output is stored verbatim under `docs/reviews/`, in a file whose name
ends `-RAW.md`, and verdict words are copied exactly. A digest quoted in
a raw review freezes the bytes it names: any later edit to this package
retires that confirmation, so the reviewed bytes are frozen from the
moment a review is issued.
