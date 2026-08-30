# Tasks — three-surface-poc-experience

> Gated: no task below is authorized until the owner signs off this
> candidate change
> (`.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-AUTHORIZATION.md`).
> All tasks execute under the one existing work item `syzygy-z2b` (the
> eight-item POC cap admits no new items), WIP one for shared-model
> changes.

## Pre-sign-off (spec authoring completion)

- [x] 1.1 Sweep RFC 0001–0009 clause-by-clause against the scope
  statement; produce the CC-SPEC-8 coverage matrix
  (`CONTRACT-COVERAGE.md`). Owner-recorded N/A judgments remain open —
  they are owner acts that ride the sign-off decision (1.3).
- [x] 1.2 Fill `contracts[]` warrants from that sweep; generate the
  CC-IMPACT dependency union (`GOVERNING-DEPENDENCIES.md`).
- [ ] 1.3 Owner sign-off act recorded in `.syzygy/governance/decisions/`.

## Prerequisite infrastructure (POC-REQ-001…022)

- [ ] 2.1 Code-structure observer with revision binding, metadata-only
  capture, failure→Unknown, determinism tests (REQ-001…004).
- [ ] 2.2 Beads-on-Dolt observer: read-only Dolt query at registered
  prefix, Dolt-revision stamping, export-independence and
  failure→Unknown tests (REQ-010…013).
- [ ] 2.3 Client build seam: bundled, self-served client code; parity
  markers in client-rendered DOM; no-script backstop (REQ-020…022).

## Surfaces (POC-REQ-030…061)

- [ ] 3.1 Shared design tokens + epistemic encoding table + legend
  generation (REQ-060).
- [ ] 3.2 Polaris long-form document with claim markers and Unknown
  disclosure (REQ-030…032).
- [ ] 3.3 Trajectory board + time lane + scope statement +
  activity≠satisfaction encoding (REQ-040…043).
- [ ] 3.4 Orrery spatial projection: deterministic layout, unmapped
  Unknown region, no inferred edges, route resolution (REQ-050…053).
- [ ] 3.5 Accessibility floor sweeps across all three (REQ-061).

## Verification

- [ ] 4.1 Focused tests per requirement oracle, with reported
  denominators; rule-6 mutation checks per falsifier.
- [ ] 4.2 Fresh-checkout demo run; wire-parity sweep extended to the
  three surfaces.
