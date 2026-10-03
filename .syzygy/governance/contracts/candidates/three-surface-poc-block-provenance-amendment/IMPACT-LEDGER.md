# Impact ledger — Three-Surface POC block-provenance amendment (N9, POC half)

> **Candidate — binds nothing.** This ledger names what the amendment would
> touch if signed and then authorized. It changes nothing itself.

## Predicate and population

- **Governed subjects.** The six POC artifacts the manifest names. Two are
  patched (`spec.md`, `GOVERNING-DEPENDENCIES.md`); four are byte-identical,
  and `--check` fails if that stops being true.
- **Implementation files.** [Observed] At `71b4f525`, the tracked files under
  `apps/` and `packages/` (excluding the Polaris generation tree) that contain
  the literal `doltRevision` number 17: 10 test files and 7 others, one of
  which is the shared test fixture `test-model-fixture.ts`. Readers of `codeStructure.revision` were found by reading every
  non-test use of the row type `CodeStructureFileEntry` and of
  `codeStructure.files`.
- **Who reads a row's revision.** [Observed] No non-test source does. The
  work-item row type is consumed by `trajectory-projection.ts`'s `laneItem`,
  which copies no revision; the code-structure rows are consumed by
  `model.ts`, `orrery-projection.ts` and `proposed-work.ts`, which read only
  `path` and the row count. Every surface reads the block header.

## Files a later implementation would touch

Nothing here is authorized. After a sign-off and a fresh implementation
authorization:

- `packages/three-surface-poc-core/src/work-items.ts` and
  `code-structure.ts`: drop the per-row field; replace the header's
  `doltRevision` / `revision` with one provenance record in the shared shape
  (`model.ts`'s `PocProvenance`, with a kind added for the Dolt database).
- Header readers, which move to the record: `model.ts` (line 530),
  `trajectory-projection.ts`, `apps/three-surface-poc/src/trajectory.ts`,
  `polaris.ts` (the two region anchors and their copy) and `orrery.ts`.
- Tests and fixtures that build rows with a revision:
  `test-model-fixture.ts`, `work-items.test.ts`, `model.test.ts`,
  `model-observations.test.ts`, `trajectory-projection.test.ts`,
  `trajectory.test.ts`, `polaris-narrative.test.ts`,
  `page-size-delta.test.ts`, and the two `.live.test.ts` files.
- A new sweep test per requirement: over every field of the observation, its
  own and every row's, exactly one holds the revision (the record's) and
  exactly one the capture instant (the observation's own, leaving out a work
  item's database times), with rule-6 mutants that put a copy back in a row
  and in the header.
- `materialization.ts`'s `doltRevisionAtCreation` is a different record (the
  Dolt head when a bead was materialized) and is out of scope.

[Observed] At this capture `/api/poc` loses 772,900 bytes of row fields
(13.44% of 5,751,883) and gains two small records. The response-identity
digest changes with the body, as it does for any body change.

## Packages and fields this collides with

- **`three-surface-poc-identity-amendment`** (pending, P-84). It adds
  POC-REQ-054 and 055 and amends POC-REQ-060 and the reader notes; it does not
  touch POC-REQ-001 or 010. [Observed] `--check` applies both spec patches in
  both orders and gets identical bytes with valid warrants. Both rewrite the
  dependency declaration's `Source:` line, so the later-signed package
  regenerates that patch with `--write`. Its own impact ledger says "Sibling
  packages: none"; that sentence was true when written and predates this
  package. It is not edited here.
- **`three-surface-poc-readability-successor`** (performed 2026-09-29). Its
  manifest rows are today's subject bytes. After this package's `--apply`, its
  `--check` reports the installed rows changed, which the sign-off change must
  carry (below).
- **`pwb-anchor-resolution-amendment`** (pending, the PWB half of N9).
  Different specification, no shared subject.
- **POC-REQ-060's "one record shape"** (signed, and amended by P-84). That
  rule is about epistemic encodings, not provenance records. [Inferred] No
  conflict; the reviewer is asked to check.

## At adoption — what the sign-off change must carry

1. `python3 scripts/build_three_surface_poc_block_provenance_amendment.py
   --apply --at-adoption`.
2. `scripts/check_spec_reconciliation.py`: its R2 binding of the six POC
   subjects to the readability successor's rows needs this package registered
   as the POC child's successor, as the PWB tree-framing sign-off was for the
   PWB child; regenerate `census.json`. [Observed] The R3 literal census does
   not move: 24 requirements, 24 scenarios, one scenario each.
3. `scripts/build_three_surface_poc_readability_successor.py --check` in the
   battery: [Inferred] it fails once the spec moves, so the sign-off change
   must teach it to accept a registered successor's bytes.
4. If the owner extends Scope A to POC amendments (P-84 Q2):
   `scripts/record_versioned_signoff.py` gains this package in
   `real_packages()`, which today lists only PWB packages. If the owner
   chooses phrase and digest instead, a dedicated recorder is written.
5. The register row P-97 closes, and `PROJECT-STATUS.md`'s open-gate row goes.

## Registry entry and policy

None. No new read, route or ceiling. The body shrinks.
