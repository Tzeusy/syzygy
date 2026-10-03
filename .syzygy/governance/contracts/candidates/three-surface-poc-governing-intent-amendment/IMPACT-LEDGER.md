# Impact ledger — Three-Surface POC governing-intent amendment

> **Candidate — binds nothing.** This ledger describes the effect of a
> possible amendment to the signed three-surface-poc-experience
> specification. It performs no act, edits no signed byte and authorizes no
> implementation.

**Baseline:** `c371339d` (`origin/main` when this package was drafted).

**Subject:** four of the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`: `spec.md`,
`CONTRACT-COVERAGE.md`, `GOVERNING-DEPENDENCIES.md` and `proposal.md`. The
proposed bytes are the four patches under `proposed/`. There is no manifest
yet (see "Not done in this version" below).

## Discovery method and denominator

[Observed] Method 1 took every NUL-separated path from `git ls-files -z` at
`c371339d`, decoded each file's bytes as UTF-8 and ran the Python `re`
patterns below over the whole file.

- **Denominator:** **2,006 tracked files**.
- **Skipped:** four files that failed UTF-8 decoding. The skip predicate is
  decode failure, not "binary".
- **Excluded:** this package. It is untracked at the baseline, so it is not
  in the population.

[Observed] Method 2 is `git grep -c -F` for `POC-REQ-014` (no hits) and
`git grep -l -F` for `governedBy` (3 files). Both agree with method 1.

| Pattern (Python `re`, exact) | Files | Occurrences |
|---|---:|---:|
| `POC-REQ-014` | 0 | 0 |
| `POC-REQ-[^\n]*(?:, \|/\|\.\.\| and \|–)014\b` (continuation forms ending in a bare `014`) | 0 | 0 |
| `governedBy` | 3 | 14 |
| `\bP-100\b` | 0 | 0 |
| `010–013` | 3 | 3 |
| `three-surface-poc-experience/specs/three-surface-poc-experience/spec\.md` | 39 | 73 |
| `three-surface-poc-experience/CONTRACT-COVERAGE\.md` | 23 | 60 |

## Consumers, by kind

- **New identifiers: no collision.** `POC-REQ-014` and `P-100` occur nowhere
  in the population, in full or continuation form. `governedBy` occurs only
  in the three 2026-09-22 vision-pursuit records (`docs/pursuits/`), which
  use it for the field this package defines.
- **The group range `010–013`.** It occurs in the signed spec's reader note
  (patched here to `010–014`), in the identity amendment's spec patch (as
  context, see "Sibling packages") and in
  `docs/evidence/spec-readability-reconciliation-2026-10-02/README.md`, an
  evidence record of the bytes as they stood then. That record is not edited.
- **The code population the new requirement reaches** [Observed]:
  - `observeWorkItems` and the `WorkItemFact` projection in
    `packages/three-surface-poc-core/src/work-items.ts`;
  - the `MaterializationRecord` type in
    `packages/three-surface-poc-core/src/materialization.ts`, which carries no
    governing intent today;
  - Trajectory's rendering in `apps/three-surface-poc/`.

  None is touched here. Implementing POC-REQ-014 needs sign-off and then an
  implementation authorization.
- **Governance tooling.** These fail after the patches are applied unless the
  sign-off change updates them:
  - `scripts/check_spec_reconciliation.py`: `EXPECTED_TOTALS` pins the POC
    at 24 requirements and 24 scenarios, and its R2 subject rows pin the
    signed bytes;
  - `docs/evidence/spec-readability-reconciliation-2026-10-02/census.json`.

  The dependency generator `scripts/build_three_surface_poc_spec_dependencies.py`
  needs no change: run over the proposed `spec.md` in a scratch copy, it
  produced the proposed `GOVERNING-DEPENDENCIES.md` exactly.
- **Sibling packages.** `three-surface-poc-identity-amendment/` (P-84) patches
  the same four files, cut against the same signed bytes. Its hunks sit on
  neighbouring lines: the reader-note group list, the family table, the
  Part A totals and the insertion point before `## Acceptance inputs` in
  `proposal.md`. [Observed: both patch sets apply alone; applied in sequence,
  the second set does not apply unchanged.] Whichever is signed second is
  regenerated against the first one's applied bytes before sign-off. The two
  packages share no requirement, clause row or identifier.
- **Route pages.** `PROJECT-STATUS.md`, `openspec/README.md`, `README.md` and
  `AGENTS.md` do not name the new identifier. Naming it there before sign-off
  would describe an unadopted requirement as current.

## What changes for a reader of the signed specification

Nothing, until sign-off. After it [Observed: counted over the proposed bytes
in a scratch copy, by heading and by table row]:

- the specification reads 25 requirements and 26 scenarios;
- `GOVERNING-DEPENDENCIES.md` reads 88 distinct authorities and 77 contract
  clauses;
- the matrix reads 77 mapped clauses, 27 applicable-uncovered and 220
  believed not applicable, totalling 324; Part A reads 118 consequence rows,
  97 covered and 21 Unknown (second method: `grep -c -F` for `| covered` and
  `| **Unknown**` over the Part A section, 97 and 21);
- RFC8-22, RFC8-23 and RFC8-24 move from Part B2 to Part A, and their B2 rows
  are removed; RFC4-15 gains one amendment row. RFC8-21 stays in Part B2,
  unedited.

## Not done in this version

- **No manifest and no builder.** P-84's order decides which bytes this
  package is regenerated on, and P-100's answer may add an edge amendment
  beside it. A manifest hashed now would be stale
  on either answer. The version offered for sign-off gets a manifest and a
  `--check` builder in the shape of
  `scripts/build_three_surface_poc_identity_amendment.py`.
- **No register entry in `check_governance.py`.** No phrase or digest is
  proposed, so there is nothing for CG-7d to watch.
