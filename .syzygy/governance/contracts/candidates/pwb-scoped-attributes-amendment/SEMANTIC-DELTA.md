# Semantic delta — PWB page-level evaluation stamp (PWB-REQ-007/020, RFC7-33)

> **Candidate — binds nothing.** Agents drafted these bytes under the owner's
> 2026-09-13 P-67 ruling (question 2: lane B after lane A is measured) and the
> owner's 2026-10-02 direction to narrow lane B to page-invariant values.
> Only the human owner may amend the signed PWB behavior or the RFC-0007
> module, each by its own sign-off. Silence, a commit, a review, a merged pull
> request or a manifest performs no act. Nothing here authorizes an
> implementation.

**Artifact(s):**

- `openspec/changes/polaris-project-wide-butlers-model/`, the eleven-artifact
  signed PWB behavioral package. Three of the eleven change:
  `specs/polaris-project-wide-butlers-model/spec.md`, `design.md`, and the
  regenerated `GOVERNING-DEPENDENCIES.md` (its source-digest line and its
  `RFC7-34` row, which gains PWB-REQ-007). The other eight rows of
  `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` equal the current bytes.
- `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` (the
  accepted contract module) and its byte-identical candidate mirror under
  `contracts/candidates/rfcs/`. RFC7-33 changes by
  `proposed/contract/RFC-0007-rendering-and-surface.md.patch`: one
  parenthetical in its opening sentence and one inserted paragraph. The module
  is not a row of the behavior manifest; it binds through its own successor
  package, `contracts/candidates/rfc7-scoped-values-successor/`.

**Stable IDs affected:** `PWB-REQ-007`, `PWB-REQ-020`, `RFC7-33`. Nothing is
minted, retired or renumbered. PWB-REQ-007's `contracts:` warrant list gains
`RFC7-34`, the clause its new text-on-the-element obligation answers, and the
generated dependency declaration follows. `PWB-REQ-014`, `PWB-REQ-016` and
`RFC7-34` are cited and not amended.

**Change class:** Normative (behavioral and contract). The amended clauses
admit one human rendering the current clauses forbid: the evaluation identity
stated once on a page-level scope. They add one falsifier and mutant class,
`stamp-hidden`. Nothing is newly forbidden and no falsifier is weakened.

**Author:** the pursuit session for bead `syzygy-dov.17` (agents), drafting
only.

**Date:** 2026-10-02.

**Baseline:** commit `9e0b8ca835d82054b135af36b2a12fbdb0b58154` (main). The
behavior subjects are the bytes after the performed opening-band, render-mode
and machine-view acts; the RFC-0007 module is as installed at that commit.

---

## Why

The Polaris page names the evaluation on every claim tuple, and the evaluation
identity is one value per page. The lane A record counts 713 claim tuples and
one distinct evaluation identity on each capture
(`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`). The
current clauses require it per claim: PWB-REQ-007 requires the complete tuple
on every claim, and RFC7-33 requires each distinction as an attribute on the
rendered unit. This amendment lets that one value be stated once.

An earlier draft let any tuple field shared by every claim under a scope be
stated once. Fresh review found the conflict built into that reach: a claim
reached apart from its scope (by anchor, find-in-page or a hand copy) lacks the
Unknown, draft, stale or review distinction RFC7-33 requires on the unit. The
owner narrowed the package on 2026-10-02 to page-invariant values. The
evaluation identity is the one such value that is not a VIS-1/VIS-2
distinction of a claim. The two presentation flags are the `non-citable` /
`presentation-artifact` pair; RFC7-33's sub-clause requires them on every
unit, so they are not scoped.

## Current meaning

Cited by identifier; read the clauses at the baseline commit.

- PWB-REQ-007 requires every project claim to carry its complete epistemic
  tuple, and its scenario requires the evaluation identity to remain visible.
- PWB-REQ-020 requires every project-shape parity marker on Polaris to be
  recoverable from the same evaluation in the machine answer.
- RFC7-33 requires each enumerated distinction to be a machine-readable
  attribute on the rendered unit, served identically through the endpoints and
  preserved in plain-text or exported renderings.
- RFC7-16 requires every claim tuple to name its evaluation.

## Proposed meaning

The patches under `proposed/` are the authority for the text; this section
states the rule they carry.

1. **The stamp (PWB-REQ-007).** On the human view the evaluation identity MAY
   be stated once on a page-level scope element in place of on each claim
   tuple. The scope is one element with a machine-readable marker, states the
   identity as text on itself in reading order before its claims, and is
   emitted only when every claim under it has that evaluation identity in the
   machine answer. A claim naming another evaluation invalidates the scope; no
   scope is emitted and each claim carries its own. A scope never overrides a
   claim's own evaluation identity, carries no other tuple field and no claim
   identity. The machine answer carries the identity on every claim.
2. **Parity (PWB-REQ-020).** Recoverability is judged after the human view is
   expanded under that rule. The comparator expands it with its own statement
   of the rule, and the mutation proof gains the `stamp-hidden` class, a stamp
   that hides one claim's differing evaluation.
3. **The contract (RFC7-33).** A paragraph permits the stamp on the
   interactive surface only, the HTML document served for a browser. It
   excludes every label, tier, reason, freshness, challenge, review, draft or
   adoption state, Unknown, claim identity and the `non-citable` /
   `presentation-artifact` pair; the endpoints, exports and any copy, share or
   export function carry the evaluation identity on every claim; the
   non-citability sub-clause stands in full.

## What explicitly does NOT change

- Every tuple field other than the evaluation identity stays on each claim,
  on every rendering.
- `PWB-REQ-014`'s non-authority attributes and the `non-citable` /
  `presentation-artifact` pair stay on every unit.
- The machine answer, the tuple vocabulary, claim identity, anchors and the
  Unknown reason's route are untouched.
- `PWB-REQ-011`, `-015`, `-016`, `-021` and `-022` are not amended.
- No read, route, egress, consent or implementation is authorized.

## Non-visual recoverability (PWB-REQ-016, RFC7-34)

The stamp states its value as text on its own element, before the claims it
covers, so a reader without vision meets the evaluation once where a sighted
reader does. The text-on-the-element falsifier in PWB-REQ-007 obliges the
accessibility checker; PWB-REQ-016's own oracle is unchanged.

## Warrant

`VIS-2` (primary), `VIS-1`, `VIS-7`; `RFC7-16`, `RFC7-33`, `RFC7-34`,
`RFC6-14`; `CC-BAR-3`, `CC-TEST-5`, `CC-TEST-6`. The change class follows
`RFC2-26` as for the earlier PWB behavior amendments.

## Evidence or decision basis

- Lane A measurement:
  `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json` (713
  tuples, one distinct evaluation identity per capture).
- Page-size funnel: `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, which
  measured the `data-evaluation-id` attributes at 699 occurrences and 49,629
  bytes on the capture it read.
- Owner direction 2026-10-02: narrow lane B to page-invariant values.
- The retained fresh reviews of the earlier, broader draft and of the contract
  paragraph are under `docs/reviews/`; this narrowed draft has had no review.

## Terms introduced or retired

Introduced: *page-level evaluation stamp* (a scope carrying only the
evaluation identity) and the mutant class `stamp-hidden`. Retired from the
earlier draft: *scope-hidden* and *over-asserting-scope* for arbitrary tuple
fields, and the general inheritance rule.

## Downstream impact

`IMPACT-LEDGER.md` lists the implementation sites. The renderer emits one
page-level scope in place of the per-claim evaluation attribute; the shared
model's tuple emission is unchanged; the Polaris parity comparator and the
accessibility checker each gain their own expansion of the rule.

## Migration and supersession plan

1. The contract successor package amends RFC7-33; it is signed first.
2. The behavior amendment is signed second and applies the three patches. It
   supersedes, by date, the funnel's earlier draft delta.
3. An implementation bead opens only under a separate owner authorization and
   re-measures the page; the saving figure in the owner packet is an estimate.

## Review

No fresh-context review has read these narrowed bytes. A review precedes any
sign-off, and a later edit to a package byte needs a new round before the next
version is offered.
