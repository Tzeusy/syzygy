# Owner decision packet — the specification-acceptance craft act (P-41)

> **This file decides nothing.** Written 2026-08-10 (RD30-07) so the
> blocking Capability 1 prerequisite P-41 has a packet like every other
> launch-critical decision, instead of only a register row.

## Question

Put a specification-acceptance standard in force before the first spec is
authored. The candidate is
`../contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
(**CC-SPEC-1…CC-SPEC-10**): what a spec must name, how testability is
judged, and the coverage bar (CC-SPEC-8) a spec is reviewed against. It
binds nothing until its own `CONFIRM CRAFT AMENDMENT` act.

## What cannot happen in this sitting — stated plainly

**This act is not performable today.** The candidate was authored
2026-08-10 and has had no fresh-context review; the craft-amendment
precedent (CC-TEST-2) is review-then-act; and no ceremony phrase or
digest subject is minted for it in `ACCEPTANCE-PHRASE-REGISTRY.yaml` —
the phrase is minted at the offering, after the review, with the digest
computed at the act (never transcribed in advance). What the owner *can*
do in the sitting is choose the route below; the act itself follows the
review.

## Ordering constraint (RD30-13)

**Rule P-40 (granularity) before this act.** CC-SPEC-1 consumes the
granularity rule by identifier ("one coherent capability, per the
granularity rule, P-40") — ruling P-40 option (b) or (c) changes
CC-SPEC-1's content without changing its text, so the standard must be
confirmed against a ruled P-40, not a pending one.

## Options

- **(a)** Order the review-then-act route: a fresh-context review of the
  candidate (CC-SPEC-1…10), repairs disposed, then the
  `CONFIRM CRAFT AMENDMENT` act binding the reviewed digest, recorded in
  the craft `INSTALL-RECORD.md` per the CC-TEST-2 precedent. Cost: one
  review cycle before the first spec can be judged acceptable; the
  standard is then in force and citable.
- **(b)** Knowingly author the first spec against the unconfirmed
  candidate, recording that choice at the launch decision. Cost: the
  first spec's acceptance is judged against text with no act behind it —
  the judgment binds by the owner's acceptance of the spec itself, not by
  a standard in force; a later act may then invalidate criteria the spec
  was already judged by.
- **(c)** Decline a written standard for the first spec entirely; judge
  Capability 1's acceptability ad hoc at its own acceptance decision.
  Cost: launch-gate E5 stays `Not met` on its own terms, and the second
  spec inherits no bar.

## Recommendation

`[Inferred]` **(a)** — the review is one cycle, the precedent exists, and
E5 is the one launch-gate criterion whose owner is entirely inside this
repository's control.

## Earliest required gate

Before the first specification is authored (`FIRST-OPENSPEC-SEQUENCE.md`
prerequisite row); after P-40.

## Independent work

The fresh-context review of the candidate can be ordered now, before any
other ruling.
