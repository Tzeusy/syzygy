# Impact ledger — Three-Surface POC vocabulary and epistemic-record amendment

> **Candidate — binds nothing.** This ledger describes the effect of a
> possible amendment to the signed three-surface-poc-experience
> specification under ruling P-75 (A), as narrowed on 2026-10-14. It
> performs no act, edits no signed byte and authorizes no implementation.

**Baseline:** `7460aec8` (`origin/main` when this package was drafted).

**Subject:** the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`. The proposed bytes are
four patches under `proposed/`, and the manifest hashes the result after
they are applied.

## Discovery method and denominator

[Observed] Method 1 took every NUL-separated path from `git ls-files -z` at
`7460aec8`, decoded each file's bytes as UTF-8, and ran the Python `re`
patterns below over the whole file.

- **Denominator:** **2,704 tracked files**.
- **Skipped:** four files that failed UTF-8 decoding, all PNG captures under
  `docs/evidence/`. The skip predicate is decode failure, not "binary".
- **Excluded:** this package and its builder. Both are untracked at the
  baseline, so neither is in the population.

[Observed] Method 2 is `git grep -c -F POC-REQ-055 HEAD`. It agrees on the
file count for `POC-REQ-055`: 23 files.

| Pattern (Python `re`, exact) | Files | Occurrences |
|---|---:|---:|
| `POC-REQ-055` | 23 | 80 |
| `POC-REQ-054` | 28 | 123 |
| `POC-REQ-060` | 84 | 383 |
| `POC-REQ-[^\n]*(?:, \|/\|\.\.\| and \|–)0(?:55\|60)\b` (continuation forms ending in a bare `055` or `060`) | 8 | 9 |
| `three-surface-poc-experience/specs/three-surface-poc-experience/spec\.md` | 45 | 83 |
| `three-surface-poc-experience/CONTRACT-COVERAGE\.md` | 30 | 70 |

## Consumers, by kind

- **The new identifier: no collision.** [Observed] The 23 files that name
  `POC-REQ-055` are:
  - the parked package (13 files) and its builder;
  - its six round raws;
  - the register, `docs/README.md` and
    `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md`.

  [Inferred] Each uses it for the vocabulary requirement this package
  mints. No file under `apps/` or `packages/` names it.
- **The deferred identifier.** [Observed] `POC-REQ-054` is named in 28
  files: the parked package (13 files), its builder and its six raws; the
  signed block-provenance package (3 files); the register,
  `docs/README.md` and the M9 design; and the two 2026-09-13 pursuit JSON
  records under `docs/pursuits/`. This package does not mint it. [Inferred] A later identity package may still use it,
  since a deferral retires nothing.
- **Code citing the amended requirement.** [Observed] Six implementation
  files cite `POC-REQ-060`:
  - `apps/three-surface-poc/src/cross-cutting.test.ts`;
  - `apps/three-surface-poc/src/design-tokens.ts`;
  - `apps/three-surface-poc/src/surface-routes.test.ts`;
  - `apps/three-surface-poc/src/trajectory.ts`;
  - `apps/three-surface-poc/src/unknown-marker.ts`;
  - `apps/three-surface-poc/src/unknown-route-sweep.test.ts`.

  The amendment keeps the encoding sentence they rely on, with Inferred
  added to its list. The record-shape and Inferred limbs are new
  obligations, and they land with M9 slices 4a and 4b once those are
  authorized. Sign-off alone changes no test's truth. [Inferred]
- **The code population the requirements reach** [Observed]:
  - the `PocEpistemic` union and the `PocEntity` and `PocRelationship` types
    in `packages/three-surface-poc-core/src/model.ts` (lines 68, 93 and
    111);
  - the nine seeded relationships in
    `packages/three-surface-poc-core/src/poc-seeds.ts` (lines 192–264);
  - the exact-table kind rendering in
    `apps/three-surface-poc/src/exact-tables.ts`.

  Each is a slice 4 or slice 8 target, and each is untouched here.
- **The signed sibling requirement.** POC-REQ-014, signed under P-100,
  decides its governing-intent encoding against POC-REQ-060's declared
  table. Its block is unchanged, and the builder fails if it moves. Adding
  an Inferred entry to the table adds one state POC-REQ-014's "any other
  state" limb excludes. [Inferred]
- **Governance tooling.** These fail after `--apply` unless the sign-off
  change updates them (`SEMANTIC-DELTA.md` residuals 2 and 3):
  - `scripts/check_spec_reconciliation.py`, through its R3 `EXPECTED_TOTALS`
    entry for POC (25 requirements, 26 scenarios) and its R2 successor
    chain;
  - the reconciliation `census.json`;
  - `scripts/record_versioned_signoff.py`'s `real_packages()`, which does not
    list this package.

  The dependency generator
  `scripts/build_three_surface_poc_spec_dependencies.py` needs no change: it
  regenerates the proposed file exactly, and the builder checks that.
- **Sibling packages.** [Observed] Four packages under
  `.syzygy/governance/contracts/candidates/` carry `*.patch` files that
  patch this change:
  - `three-surface-poc-readability-successor/`, performed 2026-09-29;
  - `three-surface-poc-block-provenance-amendment/` (P-97), signed v1.0 on
    2026-10-14;
  - `three-surface-poc-governing-intent-amendment/` (P-100), signed v1.0
    on 2026-10-14;
  - `three-surface-poc-identity-amendment/` (P-84), parked on 2026-10-14.

  The first three are in the signed tree this package's patches apply to.
  The parked one touches the same lines as this one: the reader notes'
  group and decision-key lines, the POC-REQ-060 block, and the RFC1-25,
  RFC1-26, RFC2-24, RFC2-25 and RFC6-14 rows. Its patches already fail to
  apply to the signed tree, as its register row records. It is parked, so
  no composition order is declared and this builder runs no sibling check.
- **Route pages.** `PROJECT-STATUS.md`, `openspec/README.md`, `README.md`
  and `AGENTS.md` do not name POC-REQ-055. Naming it there before sign-off
  would describe an unadopted requirement as current.

## What changes for a reader of the signed specification

Nothing, until sign-off. After it:

- the specification reads 26 requirements and 28 scenarios [Observed:
  counted over the proposed bytes by heading];
- the matrix reads 78 mapped clauses in 144 Part A rows, 105 covered and 39
  Unknown [Observed: computed by the builder's `--check`, and re-counted by
  a separate script that imports nothing from the builder];
- one signed row stands beside an amendment row and a disclosure that tells
  the reader which of the two to trust.
