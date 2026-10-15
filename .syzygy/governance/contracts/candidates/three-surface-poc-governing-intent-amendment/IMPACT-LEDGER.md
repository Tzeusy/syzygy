# Impact ledger — Three-Surface POC governing-intent amendment

> **Candidate — binds nothing.** This ledger describes the effect of a
> possible amendment to the signed three-surface-poc-experience
> specification. It performs no act, edits no signed byte and authorizes no
> implementation.

**State:** round-2 findings repaired once on 2026-10-14, unconfirmed pending
round 3 (`ROUND-2-DISPOSITIONS.md` §"Repairs, 2026-10-14 (cycle 2)").

**Baseline:** `c371339d` (`origin/main` when this package was drafted) for
the discovery sweep below. The patches were regenerated on 2026-10-14 over
the signed bytes at `origin/main` `814fbcc1`, after the block-provenance
amendment (P-97) was signed; see "Sibling packages".

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
    signed bytes. [Observed at `814fbcc1`] Its POC child now lists one later
    version-tagged sign-off, the block-provenance amendment, under
    `successors`, each entry naming a record, a manifest and the `proposed/`
    directory; this package would be the second entry, so it needs a
    manifest first (see "Not done in this version");
  - `docs/evidence/spec-readability-reconciliation-2026-10-02/census.json`;
  - `scripts/record_versioned_signoff.py`, which registers each POC package
    signed by version tag with the Scope A extension record
    (`decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`, which
    says "P-84 and P-100 take the same field when they are added").

  The dependency generator `scripts/build_three_surface_poc_spec_dependencies.py`
  needs no change: run over the proposed `spec.md` in a scratch worktree at
  `814fbcc1`, it produced the proposed `GOVERNING-DEPENDENCIES.md`, and its
  `--check` passed there at 25 requirements and 88 distinct authorities.
- **Sibling packages.** Two, named here since round 2 (finding 4).
  - **`three-surface-poc-block-provenance-amendment/` (P-97), signed v1.0 on
    2026-10-14.** It patched `spec.md` (POC-REQ-001 and POC-REQ-010) and
    the `Source:` line of `GOVERNING-DEPENDENCIES.md`. Its builder,
    `scripts/build_three_surface_poc_block_provenance_amendment.py`, lists
    this package under `pending_siblings` and says the `Source:` line "is
    rewritten by all three, so whichever is signed later is regenerated with
    --write over the earlier one's applied bytes". [Observed at `814fbcc1`:]
    this package's round-2 dependency patch failed at that line, so all four
    patches were regenerated over P-97's applied bytes; each now passes
    `git apply --check`. The two packages share no requirement or clause row.
    [Observed at `814fbcc1`, for the sign-off change:] that builder's own
    `--check` now exits 1, because its patches are the signed bytes and no
    longer apply to them; it is not in the `PROJECT-STATUS.md` battery. This
    package does not touch it.
  - **`three-surface-poc-identity-amendment/` (P-84), unsigned.** It patches
    the same four files. Its hunks sit on neighbouring lines: the reader-note
    group list, the family table, the Part A totals and the insertion point
    before `## Acceptance inputs` in `proposal.md`. [Observed in round 1:
    both patch sets applied alone; applied in sequence, the second set did
    not apply unchanged.] The P-97 builder declares the two a mutually
    exclusive pair (`exclusive_pending`, a coordinator's process ruling of
    2026-10-04). Whichever is signed second is regenerated against the first
    one's applied bytes before sign-off. P-84 is being repaired in a
    separate lane on 2026-10-14; this package does not edit it, and
    composition with its repaired patches is [Unknown] here. The two packages
    share no requirement, clause row or identifier.
- **Route pages.** `PROJECT-STATUS.md`, `openspec/README.md`, `README.md` and
  `AGENTS.md` do not name the new identifier. Naming it there before sign-off
  would describe an unadopted requirement as current.

## What changes for a reader of the signed specification

Nothing, until sign-off. After it [Observed 2026-10-14: counted over the
proposed bytes applied at `814fbcc1` in a scratch worktree, by heading and by
table row, by a Python sweep]:

- the specification reads 25 requirements and 26 scenarios;
- `GOVERNING-DEPENDENCIES.md` reads 88 distinct authorities and 77 contract
  clauses, and the Part A clause set equals its `contracts[]` set (symmetric
  difference empty);
- the matrix reads 77 mapped clauses, 28 applicable-uncovered and 219
  believed not applicable, totalling 324; Part A reads 122 consequence rows,
  98 covered and 24 Unknown; Part B1 reads 29 rows over 28 clauses;
- RFC8-22, RFC8-23 and RFC8-24 move from Part B2 to Part A, and their B2 rows
  are removed; RFC4-15 gains one amendment row; the signed RFC2-24 reason-#10
  row gains POC-REQ-014. RFC8-21 moves from Part B2 to Part B1 (round 2,
  note 7; `SEMANTIC-DELTA.md` says why), so the RFC8 family reads 8 / 1 / 23.

## Not done in this version

- **No manifest and no builder.** P-84's order decides which bytes this
  package is regenerated on, and P-100's answer may add an edge amendment
  beside it. A manifest hashed now would be stale
  on either answer. P-97's sign-off already moved the base once (2026-10-14). The version offered for sign-off gets a manifest and a
  `--check` builder in the shape of
  `scripts/build_three_surface_poc_identity_amendment.py`.
- **No register entry in `check_governance.py`.** No phrase or digest is
  proposed, so there is nothing for CG-7d to watch.
