# Tasks — three-surface-poc-experience

> Signed off by the owner on 2026-08-30
> (`.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`);
> implementation tasks below are authorized under work item
> `syzygy-z2b`. All tasks execute under the one existing work item `syzygy-z2b` (the
> eight-item POC cap admits no new items), WIP one for shared-model
> changes.

## Pre-sign-off (spec authoring completion)

- [x] 1.1 Sweep RFC 0001–0009 clause-by-clause against the scope
  statement; produce the CC-SPEC-8 coverage matrix
  (`CONTRACT-COVERAGE.md`). Owner-recorded N/A judgments remain open —
  they are owner acts that ride the sign-off decision (1.3).
- [x] 1.2 Fill `contracts[]` warrants from that sweep; generate the
  CC-IMPACT dependency union (`GOVERNING-DEPENDENCIES.md`).
- [x] 1.3 Owner sign-off act recorded:
  `.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`
  (2026-08-30, six artifacts frozen at commit `db5eaee` digests).

## Prerequisite infrastructure (POC-REQ-001…022)

- [x] 2.1 Code-structure observer with revision binding, metadata-only
  capture, failure→Unknown, determinism tests (REQ-001…004).
  `packages/three-surface-poc-core/src/code-structure.ts`, tested in
  `code-structure.test.ts` and against the real Butlers repo in
  `work-items.live.test.ts` (gated on `SYZYGY_POC_BUTLERS_REPO`).
- [x] 2.2 Beads-on-Dolt observer: read-only Dolt query at registered
  prefix, Dolt-revision stamping, export-independence and
  failure→Unknown tests (REQ-010…013).
  `packages/three-surface-poc-core/src/work-items.ts`, reads only via
  `bd sql` against the live Dolt server — the JSONL export path is never
  referenced (asserted by a static-source sweep in `work-items.test.ts`).
- [x] 2.3 Client build seam: self-served client code (inlined into the
  Orrery response, never runtime-fetched from an external origin);
  parity markers in client-rendered DOM (`data-parity-field="orrery-*"`);
  no-script backstop (`<noscript>` plus the always-rendered exact
  tables). REQ-020/021/022 covered by `cross-cutting.test.ts` and
  `orrery.test.ts`. Diverges from this file's "bundled" sketch above
  (design.md is explicitly non-normative, CC-SPEC-7): the client script
  is inline text compiled by the normal `tsc -b --force` build rather
  than a separately bundled asset file — simpler and equally compliant
  with REQ-021's actual prohibition (no runtime fetch from a foreign
  origin).

## Surfaces (POC-REQ-030…061)

- [x] 3.1 Shared design tokens + epistemic encoding table + legend
  generation (REQ-060).
  `apps/three-surface-poc/src/design-tokens.ts` + `page-shell.ts`; all
  four pages (home, Polaris, Trajectory, Orrery) render from the one
  token/legend source, swept in `cross-cutting.test.ts`.
- [x] 3.2 Polaris long-form document with claim markers and Unknown
  disclosure (REQ-030…032). `apps/three-surface-poc/src/polaris.ts`.
  One sectioned document (not literally multiple routed pages — the
  requirement text accepts "pages/sections").
- [x] 3.3 Trajectory board + time lane + scope statement +
  activity≠satisfaction encoding (REQ-040…043).
  `apps/three-surface-poc/src/trajectory.ts` +
  `packages/three-surface-poc-core/src/trajectory-projection.ts`.
- [x] 3.4 Orrery spatial projection: deterministic layout, unmapped
  Unknown region, no inferred edges, route resolution (REQ-050…053).
  `apps/three-surface-poc/src/orrery.ts` +
  `packages/three-surface-poc-core/src/orrery-projection.ts`.
- [~] 3.5 Accessibility floor sweeps across all three (REQ-061).
  **Partial.** Structural coverage only: skip-link on every page,
  interactive elements are native `<a>`/`<button>` (no non-native
  click handlers), `prefers-reduced-motion` respected, and a
  legend-to-encoding sweep (`cross-cutting.test.ts`). **Not done:**
  automated WCAG AA contrast measurement and a real keyboard-traversal
  browser E2E — no browser-automation tooling is wired into this repo
  yet. Follow-up filed.

## Verification

- [~] 4.1 Focused tests per requirement oracle, with reported
  denominators; rule-6 mutation checks per falsifier.
  Oracle-shaped tests with reported denominators exist for
  REQ-001…004, REQ-010…013, REQ-030…032, REQ-040…043, REQ-050…053, and
  REQ-060/061 (partial); rule-6 mutation checks were added for the
  reconciliation-shaped oracles (orrery/trajectory projections, Polaris
  coverage). Not every requirement has a paired mutation check yet.
- [~] 4.2 Fresh-checkout demo run; wire-parity sweep extended to the
  three surfaces.
  A real end-to-end run against the configured Butlers checkout was
  performed manually this session (`npm run build:poc` +
  `node apps/three-surface-poc/dist/main.js --repo
  /home/tze/GitHub/butlers`), serving real facts for 6,112 observed
  files and 6,973 work items across all three surfaces plus
  `GET /api/poc`. Parity is structural-by-construction (every surface
  reads directly from the one shared `PocModel`, verified per-surface
  in `polaris.test.ts` / `trajectory.test.ts` / `orrery.test.ts`), but
  no single automated sweep yet counts and compares *every* parity
  marker across all three surfaces against the machine answer in one
  pass, the way `routes.test.ts` already does for the home page. Not
  yet re-run through a truly fresh `git clone` (only a fresh `npm ci`
  in this worktree). Follow-up filed.
