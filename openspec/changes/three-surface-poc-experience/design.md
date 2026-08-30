# Design — three-surface-poc-experience

> Non-normative. Implementation guidance under the candidate spec; where
> this file and the spec disagree, the spec governs. Stack choices here
> are not required behavior (CC-SPEC-7) unless a requirement names them.

## Shape

Extend the existing POC packages rather than fork them:

- `packages/three-surface-poc-core`: add two observation modules —
  `code-structure.ts` (walks the configured repository at an exact git
  revision; emits paths, sizes, digests, language classifications) and
  `work-items.ts` (queries the Beads Dolt database read-only at the
  registered prefix; records the Dolt head revision read). Both feed
  the one `PocModel`; no second truth store.
- `apps/three-surface-poc`: three surface routes sharing one design
  token module; the exact tables remain the no-script and parity
  backstop (POC-REQ-022). Client bundles are build outputs under
  `build:poc`'s `tsc -b --force` discipline plus a bundler step —
  never runtime-fetched (POC-REQ-021).

## Surface sketches

- **Polaris**: server-rendered, paginated article layout; sections
  generated from intent entities with claim markers
  (`data-claim-provenance`) driving the POC-REQ-031 sweep.
- **Trajectory**: server-rendered board skeleton with a client
  enhancement layer; declared status→column mapping as a checked-in
  `as const` table; time lane computed from recorded instants only;
  scope statement rendered from selection-rule constants.
- **Orrery**: client-rendered spatial projection (candidate: deck.gl or
  three.js UMD bundle, pinned and vendored through the build);
  deterministic layout via a seeded, input-ordered treemap/grid — no
  physics, no randomness. Legend generated from the same encoding
  table the renderer consumes.

## Parity

Keep the independent comparator pattern: parity markers on every
rendered fact; the sweep counts its denominator and compares against
`GET /api/poc` (POC-REQ-020). Client-rendered facts must land in the
DOM with the same markers so the existing wire-parity approach extends
to enhanced surfaces.

## Test seams

Each requirement's oracle names its seam: sentinel sweep (REQ-002),
induced observer failure (REQ-003, REQ-013), double-run diff (REQ-004,
REQ-041, REQ-050), direct Dolt SQL comparison (REQ-010, REQ-040),
export mutation (REQ-012), marker-population sweeps with reported
denominators (REQ-011, REQ-020, REQ-031, REQ-051, REQ-052, REQ-053,
REQ-060, REQ-061). Rule-6 mutation checks apply per falsifier.
