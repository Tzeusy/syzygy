# Proposal — three-surface-poc-experience

> **Candidate specification.** Authoring was authorized by the owner's
> direction of 2026-08-30
> (`.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-AUTHORIZATION.md`
> — authorization to author only, never a product-behavior warrant).
> This change is a **candidate and binds nothing** until the owner signs
> it off (VIS-4). Owner sign-off of this change also gates
> implementation of the surface-redesign work item `syzygy-z2b`.
> This change specifies a **bounded, non-release proof of concept**; it
> must never be represented as conforming, complete, or released.

## Why

The first POC slice proved the honest-data spine — one shared model,
human/machine parity, epistemic labels, provenance — but rendered the
three surfaces as three list panels and two exact tables on one page.
The owner's 2026-08-30 redesign direction
(`.syzygy/governance/decisions/THREE-SURFACE-POC-REDESIGN-DIRECTION.md`)
requires three visually distinct surface experiences on one design
language, fed by two new observations (Butlers code structure; work
items from the Beads database on Dolt) and a client-side rendering
seam. Those are real behavioral contracts — what each surface may
claim, what it must render Unknown, what its observations may read and
must record — and building the largest POC item against prose direction
alone would be implementation without spec coverage. This change states
that behavior as falsifiable requirements for the owner to sign off
before the build.

**One-sentence capability:** The POC serves one observed external
project as three honest surface experiences — Polaris as a long-form
white-paper, Trajectory as a work-item board over the project's Beads
Dolt database, Orrery as a spatial code map — all consuming one shared
fact model, with every Unknown visible and every positive claim
provenance-backed.

## What Changes

- **New capability**: the three-surface POC experience — two new
  observation kinds (code structure; Dolt-hosted work items), a
  client-side rendering seam under the existing parity discipline, and
  the three redesigned surface experiences, in seven requirement
  groups.
- The adopted Capability 1 change is not modified. The existing POC
  page and its shared-model spine are the implementation baseline this
  capability reshapes; its behavioral floor (parity, epistemic honesty,
  provenance) is restated here only where this capability adds
  obligations to it.

## Capabilities

- **New Capabilities**:
  - `three-surface-poc-experience` — one coherent capability (the
    redesigned POC experience over one configured external project),
    one owner-readable product argument, one sign-off decision
    (SDR-37's granularity rule).
- **Modified Capabilities**: none.

## Scope

In scope: observing the configured Butlers repository's code structure
at an exact git revision (metadata, sizes, languages, hashes — never
indexed contents); observing work items from the Butlers Beads database
hosted on Dolt over the registered bead-prefix, recording the Dolt
revision read; a client-side rendering seam whose rendered facts are
the shared model's facts; Polaris as a multi-page long-form narrative;
Trajectory as a kanban-with-time visualization; Orrery as a
deterministic spatial code projection; one design language and an
accessibility floor across all three.

Out of scope (non-goals, CC-SPEC-5): production release or deployment;
any project beyond the one configured Butlers repository; a general 3D
engine or repository-wide semantic indexing; inferred mappings or
edges; writes to the observed project; autonomous behavior; multi-user
support; changes to Capability 1's adopted behavior.

Known Unknowns, disclosed rather than specified away: the POC's work
item / test-evidence / live-runtime relationships remain governed by
the existing POC items (`syzygy-2on`, `syzygy-8e1`, `syzygy-0r9`) and
stay Unknown until those items land their authoritative artifacts;
production reachability of the observed project remains Unknown
throughout.

## Open authoring obligations (stated, not hidden)

- **CC-SPEC-8 contract-coverage matrix**: not yet produced. The
  clause-by-clause applicability sweep of RFC 0001–0009 against this
  scope statement, with owner-recorded N/A judgments, must be completed
  before sign-off. Until then, contract coverage is **Unknown** — this
  proposal claims no coverage.
- **`contracts[]` warrants**: requirement warrants below cite adopted
  doctrine and recorded owner decisions. Accepted contract clauses that
  materially govern individual requirements have not been swept and are
  not yet declared; the empty `contracts[]` fields are an authoring gap
  to close in the same pre-sign-off pass, not an assertion that no such
  clause applies.
- **CC-IMPACT generated dependency union**: to be generated once
  warrants are complete; no hand-maintained specification-level list is
  introduced meanwhile.
