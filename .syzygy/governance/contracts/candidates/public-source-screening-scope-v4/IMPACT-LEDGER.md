# Impact ledger — public-source screening scope, version 4

> **Candidate — binds nothing.** Drafted 2026-10-15. It names what an act over
> one of this package's rows would break or require; the install is separate
> work after the act, not part of this package.

## Method

At this package's base commit (`origin/main` at `b5a7e27a`), `git grep -lF`
over `packages/`, `apps/` and `scripts/` and `.github/` for the version-3
version literal `1.4.0-public-source-candidate.1.none.code-all` (8 tracked
files), for the policy path (30 tracked files), and for the call form
`screenBody(` outside tests (5 files). The hits that consume the policy were
read; the version-3 ledger's population was taken as the starting list.

## What an act breaks until the install lands

- **The act-chain readers.** `POLICY_ACT_FORMS` in
  `packages/polaris-generation-consent/src/package-reader.ts` is a closed
  list of act forms read as a chain. A version-4 act record carrying the scope
  stem makes the reader refuse until the install adds a fourth form and
  extends the chain (version 4 needing version 3, later, over other bytes).
- **The read-gate pin** in `apps/three-surface-poc/src/governance-inputs.ts`
  names the version-3 version literal, and its tests do too
  (`governance-inputs.test.ts`); the recorder fixtures in
  `packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts` and
  `package-reader.test.ts`, and the literals in
  `packages/three-surface-poc-core/src/git-object-reader.ts`,
  `content-classification.test.ts` and `project-shape-model.test.ts`, move
  with it.
- **The version-3 recorder's battery lines.**
  `scripts/record_public_source_screening_scope_v3_act.py` checks the applied
  subject, so its `--check` fails once the policy moves; a version-4 recorder
  replaces its lines in the CG-26 triple, once, at the install.
- **`check_governance.py` CG-7e.** As after version 3, the version-3 manifest
  and act record no longer contain the current argument, and the version-4
  manifest needs an existence-gated registration in `ACT_DIGEST_COPY_FILES`
  beside `_activate_public_source_scope_v3_copy_registry`. This package adds
  none of that; it is drafted, not offered.

## What the install must build (redaction)

- **Match offsets.** `detectSecrets` in
  `packages/three-surface-poc-core/src/content-classification.ts` returns the
  first matching detector id only. The rule needs every match's start and end
  over the complete body, then the line placement, guard, re-screen and
  span test the builder's reference oracle (`withheld_lines`) states.
- **The two screens.** `packages/polaris-dossier/src/screen.ts` and
  `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts`
  must agree on every body of `screen.test.ts`'s population, including the
  builder's body fixtures (`TODO(syzygy-qkea.17)` keeps them copies).
- **The target-body call sites.** `review.ts` (the fidelity packet's
  `readBlobs` loop), `check.ts` (quotation checks), and the any-repo corpus
  reader `apps/three-surface-poc/src/polaris-generation/repo-corpus.ts` read
  target bodies and must carry the retained body and its withheld line set: a
  span overlapping one gets a withheld outcome naming `redacted-span`, and an
  admitted span carries the redaction count.
- **Agent-text call sites stay whole-text.** `render.ts` (lines 280, 383) and
  `close.ts` (line 124) screen agent-written prose; the policy's `appliesTo`
  keeps them unchanged. `render.ts` line 204 decides the version-3 render
  condition and reads target bodies; it must not be fed a body with withheld
  lines intact.
- **Rendering.** A page that shows a retained body shows a marker with the
  withheld-line count in place of each withheld run.

## What the install must build (variant `span-guides` only)

- `readProjectDocumentationRule` and `publicSourceContentClass` in
  `packages/polaris-generation-core/src/public-source-classification.ts`
  learn `rootGuideStems` and `rootGuideSuffixes`; the builder's
  documentation fixtures are the oracle.

## What it does not touch

The base (Butlers) scope and its consumers, the consent and egress readers,
and every specification.
