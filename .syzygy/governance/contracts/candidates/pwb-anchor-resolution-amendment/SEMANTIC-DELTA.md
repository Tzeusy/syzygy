# Semantic delta — PWB anchor-resolution amendment (N9, PWB half)

> **Candidate — binds nothing.** This package proposes one amendment to the
> signed PWB specification. Nothing here is signed, adopted or labelled
> accepted, and no implementation is authorized (VIS-4). Only the owner's
> sign-off binds it, and building it needs a fresh implementation
> authorization after that.

**Artifact(s):** `openspec/changes/polaris-project-wide-butlers-model/`:
`specs/polaris-project-wide-butlers-model/spec.md` (PWB-REQ-014 only) and
`GOVERNING-DEPENDENCIES.md` (regenerated; only its `Source:` digest moves).
**Stable IDs affected:** PWB-REQ-014. No identifier is added, renumbered or
retired.
**Change class:** Normative. Two obligations are added to PWB-REQ-014: one
anchor shape that names its block, and a counted `anchorsResolved` pair. An
implementation that complied before does not comply now, because it serves
no pair.
**Author:** a drafting session (Claude), bead `syzygy-u05.9`.
**Date:** 2026-10-03, over `main` at `71b4f525`.

**Sibling package.** The other half of N9 is a separate OpenSpec change
against a different specification:
`three-surface-poc-block-provenance-amendment/` (POC-REQ-001 and POC-REQ-010).
The two share one review round and are signed separately. Neither depends on
the other.

## Warrant

- **The move.** [Observed] Bead `syzygy-u05.9`, pursuit move N9 of
  `docs/pursuits/2026-09-22-vision-pursuit.md`, released for drafting when
  the pursuit's hold gate `syzygy-dca` closed. Its acceptance criteria asked
  for a spec delta "under dov.22's family before any code" with "citable
  computed from anchors (934/934 true on the current corpus)".
- **The coordinator's rulings, 2026-10-03.** [Observed] The bead's notes
  record them; they are drafting decisions, not owner acts:
  1. keep non-citability, offer a numeric `anchorsResolved` count inside
     PWB-REQ-014 instead, and put the RFC7-3 question to the owner without
     drafting it;
  2. draft the per-row provenance rule as a separate POC-family change, so no
     OpenSpec change crosses categories;
  3. the bead's "must land before dov.10.1" ordering is stale: dov.10.1
     merged on 2026-09-22 (PR #56).
- **Why the bead's literal ask cannot be drafted here.** [Observed] Signed
  PWB-REQ-014 requires every narrative unit to carry `non-citable`, and its
  first scenario requires both forms to "mark the block non-citable
  presentation". Accepted RFC 0007 says, at
  `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` line
  111: "**RFC7-3 — Nothing cites the rendering.** No claim, gap, mapping,
  evidence link, work warrant, source anchor, or citation anywhere in Syzygy
  may resolve to a Polaris narrative, section, claim block, rendering, or
  editorial draft as its authority". RFC7-4, four lines below, adds
  "Non-authority is total." A spec delta may not contradict an accepted
  contract. Making a block citable when its anchors resolve would need a
  contract amendment first, and that is an owner decision this package only
  asks about (`OWNER-DECISION-PACKET.md`, question 2).
- **The sign-off route.** [Observed] Scope A
  (`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, item
  1) covers "the PWB specification deltas". This package is one, so it is
  signed by version tag.

## Evidence or decision basis

Every figure below is [Observed] at Syzygy `71b4f525` and Butlers
`32f38feb`, from one private-daemon evaluation, recorded in
`docs/evidence/n9-machine-channel-provenance-measurement-2026-10-03.json`
with both captures' byte counts and digests. The script that produced it is
`scripts/measure_machine_channel_provenance.py`.

- **The machine narrative today.** `GET /api/poc/polaris` serves 697 narrative
  blocks, all `citable: false`, all with anchors; 902 anchors with 902
  distinct identities.
- **One anchor shape already.** All 902 anchors carry the same seven keys
  (`anchorId`, `captured`, `locator`, `revision`, `supports`, `targetClass`,
  `targetId`).
- **Block-to-anchor ids already exist.** All 902 anchor identities begin with
  their block's identity and `#`, and each anchor's `supports` lies within
  its block's claims (902 of 902). The bead's "link each narrative block to
  its anchors by id" is therefore already met. This delta does not invent
  that work; it writes it down as an obligation (the **Anchor shape**
  bullet), so a later change cannot lose it silently.
- **Resolution under this delta's predicate: 883 of 902.** An anchor resolves
  when the machine answer serves exactly one record whose own served identity
  equals the anchor's target identity. Today the only records with a served
  identity are the 285 `projectShape.sources[]` entries. 883 anchors resolve
  to exactly one of them; none resolves to more than one. The 19 that do not
  are:
  - 17 evidence anchors whose targets are provenance records (11
    `repository-file`, 5 `manual-mapping`, 1 `git-revision`);
  - the code-structure region anchor (`git-tree:<revision>`);
  - the work-items region anchor (`beads-dolt:<dolt revision>`).

  A second method agrees: none of those 19 target identities occurs as a
  whole string value anywhere in the `/api/poc` body.
- **The pursuit's figures are superseded.** "730 blocks", "934 anchors" and
  "934 of 934 resolved" were measured at an earlier Butlers revision, and the
  resolution figure named no predicate. [Unknown] Which predicate produced
  it; the pursuit data does not say.

## What changes, and why each part has the shape it has

### 1. One anchor shape that names its block

The coordinator's ruling asked for "one provenance shape on /api/poc/polaris".
That route's provenance is its anchors, and they already share one shape. The
delta states that shape as a SHALL: identity naming its block, target class
and identity, revision, supported claims, captured state, locator. It names
fields by meaning, not by JSON key, as the rest of PWB-REQ-014 does.

Not included: the capability deep-dive's `intent.leaf` record (`path`,
`revision`, `identity`) is a second encoding of a source reference on the same
route. [Observed] One instance at this capture. It belongs to PWB-REQ-015's
exact-intent band, not to the anchor set, and changing it would touch a
second requirement. It is put to the owner as question 3.

### 2. The `anchorsResolved` pair

- **Where it sits.** On each anchored claim block, and once for the
  narrative. The narrative's pair is the sum of its blocks' pairs, so a
  reader can check one against the other.
- **What "resolves" means.** The predicate is stated against the machine
  answer, not the narrative builder. That keeps the field inside PWB-REQ-020's
  rule for a derived read-only view: every value it serves must be derivable
  from the machine answer's own bytes at that evaluation.
- **No rounding.** A count below its total is served as counted. 883 of 902
  is the honest figure today, and the 19 are named above.
- **Never authority.** The pair sits beside `non-citable`, never in place of
  it. No field derived from the pair may make a unit citable or act as an
  epistemic label. This is the point of ruling 1: resolution is not
  authority.
- **Openings.** An opening carries child identities in place of an anchor set
  (signed text), so it has no pair.
- **No rendering duty.** The pair is a machine-narrative field, not a
  project-shape claim. PWB-REQ-020 compares project-shape facts, so Polaris
  need not render it. If the owner wants it on the page, that is a
  PWB-REQ-020 change (question 4).

## Current meaning, and proposed meaning

The proposed bytes are `proposed/spec.md.patch`; read them with
`python3 scripts/build_pwb_anchor_resolution_amendment.py --diff`. Six signed
lines are re-wrapped, each to append a sentence or a falsifier limb; the
builder lists them in `REQ_014.replaced` and fails if any other signed line
is lost.

| Part | Current | Proposed |
|---|---|---|
| Obligations | Typed, revision-bound anchor sets, closed target classes, `non-citable` units | Adds **Anchor shape** and **Anchor resolution count** after the anchor-target bullet |
| Case | Sweep of units, claims, anchors and downstream citations | Adds: resolve every anchor against the machine answer, withhold one resolved target's identity, resolve again |
| Observable | Roles and non-authority attributes are machine-readable | Adds: every anchor's shape, and each pair |
| Oracle | Covering, minimality, captured state, zero Polaris authority targets | Adds: every anchor has the one shape and names its block; an independent resolver reproduces every pair exactly; withholding one target lowers exactly the right blocks' counts, and those blocks stay non-citable |
| Oracle independence | Expected spans from captured artifacts | Adds: expected counts from the independent resolver, never the builder |
| Falsifier | Unclassified unit, uncovered claim, missing `non-citable`, … | Adds: an anchor off the shape or naming no or another block; a missing, wrong or rounded pair; a unit made citable by its pair |
| Scenarios | 8 | 9: adds "Anchor resolution is counted, never made authority" |

The warrants block does not move. RFC7-3 is already among its contracts.

## What explicitly does NOT change

- Every narrative unit stays `presentation-artifact` and `non-citable`. RFC7-3
  and RFC7-4 are untouched.
- Every other requirement, the reader definitions, the warrants, the
  capability table, the proposal, the design and the contract-coverage
  matrix are byte-identical. `--check` runs the coverage generator over the
  proposed bytes, and it passes unchanged.
- No new route, field on `/api/poc`, read or byte ceiling.
- The human page's anchor rendering (`data-anchor-id` only) is unchanged.
  Linking a page anchor to its resolver (pursuit move S6-M2 slice 2) is out of
  scope.

## Terms introduced / retired

- **`anchorsResolved` pair** (introduced): resolved anchors over anchors, per
  anchored block and for the narrative.
- **Resolves** (introduced, for anchors): defined in the amended text.

None retired.

## Downstream impact

See `IMPACT-LEDGER.md`. In short, once signed and authorized: the narrative
builder (`apps/three-surface-poc/src/polaris-narrative.ts`) emits the pair; an
independent resolver test in the app's test suite checks it; the PWB
spec-reconciliation census moves PWB-REQ-014 from 8 to 9 scenarios.

## Migration / supersession plan

- **Sign-off.** Scope A, by version tag. The sign-off change runs
  `--apply --at-adoption`, then updates the reconciliation checker and its
  census in the same commit (`IMPACT-LEDGER.md`, "At adoption").
- **Order against the pending siblings.** The class-granular and
  release-label packages patch other requirements. All three spec patches
  compose in either order, and `--check` proves it. Each package rewrites the
  dependency declaration's one `Source:` line, so whichever is signed later
  must be regenerated with `--write` over the earlier one's applied bytes,
  and re-reviewed if its spec bytes moved.

## Review

**Required class:** fresh-context review (CC-REV-1), one round shared with
the POC half; stopping rule: on REVISE, repair once, dispatch no second round,
and route the result to the owner.
**Reviewer:** a fresh-context subagent that did not draft this package.
**Verdict:** recorded verbatim in the raw under `docs/reviews/`, and in
`ROUND-1-DISPOSITIONS.md` beside this file once the round has run.
