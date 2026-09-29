# Polaris manifesto generation

> **Status:** on 2026-09-12 one owner phrase adopted this specification,
> decided its scoped applicability and authorized its implementation,
> recorded in
> [`POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`](../../../.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md)
> and its two sibling records. The understanding amendment
> (`../polaris-manifesto-understanding-amendment/`) later replaced seven of
> its requirements and added two. Project admission, provider
> consent, authorship and release remain separate acts.

**Polaris generates a project's manifesto: a coherent, browsable account of its
purpose and ideas, from authorized sources, through one reusable workflow.**

## Why

Polaris should make a project's purpose and ideas understandable through a
coherent, beautiful, browsable account. The current Butlers page uses fixed
copy and manually selected passages; it cannot reliably generate or
regenerate that experience for another project.

## What changes

- **Generation.** A project-neutral, human-triggered workflow over authorized
  source snapshots and explicitly permitted providers.
- **Drafts.** Structured editorial drafts with source-backed motives,
  concepts, claims, Unknowns, navigation and optional relationship assets.
- **Quality.** Bounded editorial construction, independent fidelity and
  design review, and revision.
- **Reliability.** Observable cancellation, recovery, source-drift
  regeneration, and preservation of human-curated presentation.
- **Adoption.** Contextual review and adoption in Polaris, using the existing
  human-act predicate; Trajectory keeps owning the drafting lifecycle.
- **Assets.** Reusable asset rendering, and separately authorized export,
  with no source-code change per project.

## Capabilities

- **New:** `polaris-generation` — generate, review, recover and adopt
  project-specific manifesto presentation from admitted snapshots through one
  reusable workflow.
- **Modified:** existing PWB observation, exact-text and truth-projection
  requirements stay intact. This is not a replacement source-observation
  policy.
  - **Host integration is explicit.** The new data-bearing and mutating
    generation operations need their own authentication and credential
    handling — session and anti-forgery admission, project scopes,
    verifier-only server storage and protected audit. None of it is assumed
    from the current read-only route helpers.
  - **No blanket "nothing modified" claim.** Where integration changes adopted
    PWB behavior, that change needs its own signed amendment.

## Impact

- **Integration.** The app needs a project-neutral presentation input and
  generation controls. The source and permission adapters, narrative
  renderer, drafting lifecycle and provider interface need explicit
  integration. This proposal selects no library, provider, storage engine or
  deployment.
- **In scope:** the complete local owner experience; reusable generation and
  regeneration; semantic and design validation; explicit draft and
  authorship states; recovery; permitted asset retention and export.
- **Out of scope:** autonomous intent adoption; implementation-code
  generation or writes; automatic release or deployment; unauthenticated
  remote service; multi-user collaboration; implicit model-provider egress;
  a second independent work queue.
  - These exclusions do not narrow cross-project reuse: independently
    admitted projects must use the same implementation.
- **Not authorized here:** reading another real project, or sending Butlers
  content to a provider. The existing PWB continuation explicitly excludes
  those effects. Synthetic bundles may establish mechanics but cannot
  discharge real-project quality evidence.

## Implementation and applicability scope

- **Staging.** `EXECUTION-PHASES.md` stages mechanics, the complete owner and
  effect flow, and real quality and portability proof, without shrinking
  completion.
- **Effect host.** `EFFECT-HOST-DESIGN.md` selects separate generator
  origin, process and credential stores, and a protected local recorder;
  legacy PWB and CAP1 routes keep their existing behavior.
- **Host overlap.** `docs/design/POLARIS-GENERATOR-HOST-OVERLAP.md` records
  the exact additive seams. A departure that changes an adopted outcome
  still needs its signed amendment, never an implicit compatibility claim.
- **Applicability.** `APPLICABILITY-DECISIONS.md` holds the narrowly scoped
  workspace and portfolio judgments; the owner's applicability act
  ([`POLARIS-GENERATOR-APPLICABILITY-ACT.md`](../../../.syzygy/governance/decisions/POLARIS-GENERATOR-APPLICABILITY-ACT.md))
  binds them. The generator still handles project relationships and declared
  child composition as specified.
- **RFC8 no-signal predicate.** Its independent amendment is not part of this
  specification. Supported-profile admission and explicit later obligations
  remain controlling.
