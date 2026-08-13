# Semantic delta — a lagging-specification exception, offered as an amendment to CC-REV-2

> **Candidate offer. Binds nothing. This file performs no act.** It exists
> because the alternative — writing the exception into a *new* candidate
> clause beside CC-REV-2 — would weaken an owner-approved clause without
> amending it, which is what RD-51 finding 1 called blocking. The lawful
> route for a rule that changes CC-REV-2's meaning is a semantic delta
> against CC-REV-2 itself, adopted by the owner's craft-amendment act.
>
> Queue row: **P-44** in `../../../decisions/PENDING-OWNER-DECISIONS.md`.
> **Two arms are offered, and declining is one of them.**

**Artifact:** `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`
**Stable IDs affected:** `CC-REV-2` (amended in place; no identifier is minted, retired or renumbered)
**Change class:** **Normative** — an obligation is narrowed. Someone who complied before still complies; someone blocked before may now merge under a recorded exception.
**Author:** authoring session, 2026-08-13. An agent may draft a delta; adoption belongs to the owner (VIS-4).
**Date:** 2026-08-13

## Why this file exists at all

Owner charter §9.6 directs that *"any lagging specification requires a
lawful owner-visible exception mechanism owned by craft policy"*, naming
five required elements, and directs equally that no *casual* exception
conflicting with CC-REV-2 be created. Those two directions have exactly one
consistent implementation: amend CC-REV-2.

`[Observed]` The candidate `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`
previously took the other route. Its CC-IMPACT-6 said it "adds exactly one
lawful alternative" to the merge invariant. Both clauses would have sat in
craft-cluster **tier 2**, and the cluster's own precedence rule
(`policies/craft-and-care/README.md`) resolves *cross-tier* conflict only —
"a lower layer can strengthen a higher one; it can never weaken it" — so
two same-tier clauses would have given opposite answers to "may this merge
land?" with nothing to arbitrate. That side-clause is withdrawn; this is its
replacement route.

## Current meaning

CC-REV-2, quoted exactly
(`policies/craft-and-care/review-and-documentation.md`):

> A change that invalidates any authoritative artifact updates **every**
> invalidated authoritative artifact in the same logical change: behavioral
> specs (`openspec/`), declared topology, accepted contracts, and the
> policies in this cluster. "We'll sync the spec later" is a violation, not
> a plan (canonical bias 7, strengthened to *all* typed authorities).
> [Observed — FD-020 E1-b … and E10 …] The rule is a **merge invariant, not
> a property of how work is packaged**: no merge may leave mainline with an
> invalidated authoritative artifact still asserting the old truth.
> Splitting one logical change across sequenced merges that pass through
> such a state *is* the violation — an open follow-up PR is "syncing later"
> by another name.
>
> The one structural carve-out: **doctrine** is amended only through the
> owner gate (VIS-4). When a change would invalidate doctrine text, the
> change stops and routes to the owner as a contradiction — it does not edit
> doctrine in-change, and it does not merge while the contradiction is open.

There is **one** carve-out and it is doctrine's owner gate. A behavioral
specification may not lag its shape change under any circumstance.

## Proposed meaning — arm (a)

Append to CC-REV-2, after the doctrine carve-out paragraph, exactly:

> **The second structural carve-out: a lagging behavioral specification
> under a recorded exception.** Where a shape change invalidates a
> behavioral specification whose amendment cannot lawfully land in the same
> change, the specification may lag **only** under an exception recorded
> before the merge, carrying all five of:
>
> ```text
> affected specification   named, by identity
> reason                   why the amendment cannot land in this change
> owner                    the named actor who will amend it — never "someone"
> end condition            the event or date at which the exception expires;
>                          an exception with no end condition is not recorded
> interim state            the specification renders `contradicted` or
>                          `Unknown` on its own surface for the duration —
>                          never as current, never silently
> ```
>
> The exception is **confirmed by a party other than the change's author**
> (the CC-TEST-4 pattern: never made by the implementing agent alone;
> confirmed by the change's reviewer, or by the owner where no reviewer
> exists). An exception the author writes and merges alone is this rule's
> violation with a form attached.
>
> An expired exception is a violation from the moment it expires, not a
> renewable state. Nothing here reaches doctrine, whose carve-out above is
> unchanged.

## Proposed meaning — arm (b)

**No amendment.** CC-REV-2 stands as approved, and no behavioral
specification may ever lag a shape change. Choosing this arm is choosing a
harder constraint knowingly, and it is a real option: it is RD-51 finding
1's own first-listed fix, and it costs nothing to adopt today because no
specification exists to lag.

## What explicitly does NOT change

Named because "I only touched X" is the most common false claim in
normative editing:

- **The doctrine carve-out** is untouched. A change invalidating doctrine
  text still stops and routes to the owner, and still does not merge while
  the contradiction is open.
- **The merge-invariant framing** is untouched: the rule remains a property
  of what mainline asserts, not of how work is packaged. Arm (a) does not
  reintroduce "syncing later" — a lagging spec under arm (a) is *not*
  silently asserting the old truth, because the interim-state element makes
  it render `contradicted` or `Unknown`.
- **Declared topology, accepted contracts, and the cluster's policies** are
  untouched. The carve-out reaches behavioral specifications only.
- **CC-REV-1, CC-REV-3…7** are untouched.
- **No identifier moves.** CC-REV-2 is amended in place (CC-REV-7).

## Warrant

Owner charter §9.6, and RD-51 finding 1 (blocking), raw at
`../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`.

## Evidence or decision basis

`[Observed]` — CC-REV-2's text as quoted, read at
`policies/craft-and-care/review-and-documentation.md`; the cluster
precedence rule at `policies/craft-and-care/README.md`; the two approved
exception mechanisms this borrows from, CC-TEST-1 and CC-TEST-4, at
`policies/craft-and-care/testing-and-verification.md`.

`[Inferred]` — that arm (a) is the safer of the two in a corpus that will
have owner-gated specifications: an owner who must personally adopt a spec
amendment (CC-SPEC-10) is a lawful reason an amendment cannot land in the
author's change, and under arm (b) that shape change simply cannot merge
until the owner acts. Whether that is a defect or the point is the owner's
call, not this file's.

## Terms introduced / retired

None. "Exception", "end condition" and "interim state" are used in their
existing senses; no durable term enters the registry.

## Downstream impact

Method: Python `re` sweep for `CC-REV-2` over `.syzygy/**` `*.md|*.yaml|*.json`,
plus the repository root, run in this session — see the delta
`../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`, which
records the count and the enumerated hits. The load-bearing dependants:

| Artifact | What arm (a) would change there |
|---|---|
| `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` CC-IMPACT-6 | it currently states that **no lawful lag exists** and names this offer. On arm (a)'s adoption it becomes a citation to the amended CC-REV-2; on arm (b) it is already correct as written and needs no edit |
| `../round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md` step 4 | already records the limb as invented and withdrawn. Superseded by fixture 2 either way |
| `../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md` | unaffected — it grades detection, not responsibility |

## Migration / supersession plan

CC-REV-2's file is **owner-approved (D2)**, so this delta cannot be applied
by any agent. On arm (a): the owner performs the craft-amendment act, the
digest is computed **at the act** and recorded in
`policies/craft-and-care/INSTALL-RECORD.md` (the CC-TEST-2 precedent), and
CC-IMPACT-6 is updated in the same logical change to cite the amended clause
rather than to state that no lag exists. On arm (b): this file is retired
with the ruling recorded, and CC-IMPACT-6 stands unchanged.

## Review

**Required class:** CC-REV-1 (the change alters a merge invariant governing
every authoritative artifact) and CC-REV-4 (normative artifact, material
amendment).
**Reviewer:** must not have authored this delta or shared its session. **Not
yet dispatched** — this offer is one day old and its own review is part of
the combined CC-SPEC/CC-IMPACT review that owner charter §9.8 sequences
after P-40 is ruled.
**Verdict:** `[Unknown]` — no review has been run against this file.
