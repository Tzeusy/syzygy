# Impact ledger — Three-Surface POC identity amendment

> **Candidate — binds nothing.** This ledger describes the effect of a
> possible amendment to the signed three-surface-poc-experience
> specification under ruling P-75. It performs no act, edits no signed byte
> and authorizes no implementation.

**Baseline:** `ab22492` (`origin/main` when this package was drafted).

**Subject:** the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`. The proposed bytes are four
patches under `proposed/`, and the manifest hashes the result after they are
applied.

## Discovery method and denominator

[Observed] Method 1 took every NUL-separated path from `git ls-files -z` at
`ab22492`, decoded each file's bytes as UTF-8 and ran the Python `re`
patterns below over the whole file.

- **Denominator:** **1,924 tracked files**.
- **Skipped:** four files that failed UTF-8 decoding. The skip predicate is
  decode failure, not "binary".
- **Excluded:** this package. It is untracked at the baseline, so it is not
  in the population.

[Observed] Method 2 is `git grep -c` for the same literals. It agrees on the
file counts for `POC-REQ-060` and the spec path.

| Pattern (Python `re`, exact) | Files | Occurrences |
|---|---:|---:|
| `POC-REQ-060` | 46 | 242 |
| `POC-REQ-[^\n]*(?:, \|/\|\.\.\| and \|–)060\b` (continuation forms ending in a bare `060`) | 2 | 2 |
| `POC-REQ-05[45]` | 3 | 8 |
| `POC-REQ-052` | 15 | 43 |
| `three-surface-poc-experience/specs/three-surface-poc-experience/spec\.md` | 37 | 68 |
| `three-surface-poc-experience/CONTRACT-COVERAGE\.md` | 21 | 55 |

## Consumers, by kind

- **New identifiers: no collision.** `POC-REQ-054` and `POC-REQ-055` occur in
  three files: `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` and the two
  2026-09-13 pursuit JSON records. Each uses them for the requirement this
  package mints.
- **Code citing the amended requirement.** Three implementation files cite
  `POC-REQ-060`: `apps/three-surface-poc/src/design-tokens.ts`,
  `apps/three-surface-poc/src/cross-cutting.test.ts` and
  `apps/three-surface-poc/src/surface-routes.test.ts`. The amendment keeps
  the encoding sentence they test. The record-shape and Inferred limbs are
  new obligations, and they land with M9 slices 4a and 4b after sign-off.
  Sign-off alone changes no test's truth.
- **The code population the new requirements reach** [Observed]:
  - the `PocEpistemic` union and the `PocEntity` and `PocRelationship` types in
    `packages/three-surface-poc-core/src/model.ts`;
  - the nine seeded relationships in
    `packages/three-surface-poc-core/src/poc-seeds.ts`;
  - the exact-table kind rendering in
    `apps/three-surface-poc/src/exact-tables.ts`.

  Each is a slice 4, 6 or 8 target and is untouched here.
- **Governance tooling.** These fail after the patches are applied unless the
  sign-off change updates them:
  - `scripts/check_spec_reconciliation.py`: its R2 subject rows and its R3
    census, which pins 24 POC-REQ;
  - the reconciliation `census.json`.

  The dependency generator `scripts/build_three_surface_poc_spec_dependencies.py`
  needs no change: it regenerates the proposed file exactly, and the builder
  checks that.
- **Sibling packages: none.** Of the 83 tracked `*.patch` files under
  `.syzygy/governance/contracts/candidates/`, the only ones that patch this
  change belong to the readability successor. That successor was performed
  2026-09-29, and the tree carries its successor bytes. [Observed: all six
  subjects hash to its manifest rows.] So there is no composition order to
  declare.
- **Route pages.** `PROJECT-STATUS.md`, `openspec/README.md`, `README.md` and
  `AGENTS.md` do not name the new identifiers. Naming them there before
  sign-off would fail the reconciliation checker's R4, and would describe an
  unadopted requirement as current.

## What changes for a reader of the signed specification

Nothing, until sign-off. After it:

- the specification reads 26 requirements and 28 scenarios [Observed:
  counted over the proposed bytes by heading];
- the matrix reads 78 mapped clauses;
- one signed row stands beside an amendment row and a disclosure that tells
  the reader which of the two to trust.
