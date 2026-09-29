# Proposal — three-surface-poc-experience

The bounded POC serves the configured Butlers repository through three honest
surfaces over one shared fact model:

- **Polaris** — a long-form account of project intent.
- **Trajectory** — a work-item board over the project's Beads Dolt database.
- **Orrery** — a spatial projection of observed code structure.

Every Unknown stays visible. Every positive claim retains resolvable
provenance. This is a non-release proof of concept, never a claim of product
completion or conformance.

## Why

The first POC established the truth-bearing spine but presented three list
panels and exact tables on one page.

- **What already worked:** one shared model, human/machine parity, epistemic
  labels and provenance.
- **What the redesign adds:** distinct surface experiences, code-structure and
  work-item observations, and a client-rendering seam that preserves the same
  truth.
- **Why this specification exists:** those additions decide what each surface
  may claim, which sources it may observe, and how failures remain Unknown.
  Building them from prose direction alone would leave observable behavior
  unspecified.

The owner's 2026-08-30 authoring and redesign directions are the warrant for
this specification. Adoption and implementation authority live in their
recorded acts; this proposal does not restate their lifecycle state.

## Capability

`three-surface-poc-experience` is one coherent capability: a redesigned,
owner-readable POC over the configured Butlers repository, with one acceptance
decision under SDR-37.

- **New observations:** exact-revision code structure and revision-stamped
  work items from Dolt.
- **New presentation:** three surfaces sharing one design language and one
  fact model.
- **Preserved floor:** parity, epistemic honesty and provenance from the
  existing POC spine.
- **Unchanged authority:** Capability 1's adopted behavior is not modified.

## Scope

- **Observe Butlers code structure.** Read metadata, sizes, language
  classifications and digests at one exact Git revision. Never index file
  contents.
- **Observe Butlers work.** Read the registered bead-prefix population from
  the Butlers Beads Dolt database and record the exact Dolt revision.
- **Render one shared model.** Client-enhanced facts remain identical to the
  machine answer and to the script-less exact routes.
- **Present three surfaces.** Polaris explains intent; Trajectory presents
  work and recorded time; Orrery projects code structure deterministically.
- **Apply one accessibility floor.** Keyboard use, text alternatives, contrast,
  reduced motion and truthful legends apply across all three surfaces.

### Non-goals

- Production release or deployment.
- Any project beyond the configured Butlers repository, or a general
  multi-repository product.
- A general 3D engine or repository-wide semantic indexing.
- Inferred mappings, edges or missing intent.
- Writes to the configured Butlers repository.
- Autonomous behavior or multi-user support.
- Any change to Capability 1's adopted behavior.

## Known Unknowns

The work-item/test-evidence/live-runtime relationships stay Unknown until their
existing POC work lands authoritative artifacts. Production reachability of the
configured Butlers repository also remains Unknown. This specification does
not turn missing
evidence into an empty or successful state.

## Acceptance inputs

- `CONTRACT-COVERAGE.md` carries the clause-consequence review input and its
  unresolved owner judgments. The author mints no N/A decision: every
  uncovered consequence remains Unknown until an effective owner act says
  otherwise.
- `GOVERNING-DEPENDENCIES.md` is generated from every requirement's warrants.
- The behavioral specification contains the falsifiable requirements and
  scenarios. These supporting views do not replace it.
