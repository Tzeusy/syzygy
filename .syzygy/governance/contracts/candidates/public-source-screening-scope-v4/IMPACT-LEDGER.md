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
- **The Butlers (base) read gate.** `apps/three-surface-poc/src/governance-inputs.ts`
  lines 76-104 (`pwbSyzygyButlersExpectations`) pin the version-3
  `policyVersion`, act identity, recording tag and scope anchors, so any
  version-4 act closes the Butlers body-read gate until it is re-pinned, as
  the version-3 ledger said of its own act (round 1, finding 5). The tests pin
  it too
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

- **Policy-path consumers not yet assessed.** From the 30-file policy-path
  sweep: `scripts/install_redis_sitting.py` (derives its policy step from the
  recorded act), `scripts/simulate_redis_sitting.py`,
  `scripts/check_spec_reconciliation.py`, and the app's
  `checkoutPolicyActPort` in
  `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts`
  (it reads `POLICY_ACT_FORMS[0]` only). Whether each breaks is Unknown; the
  install assesses each.
- **Policy-path files that read the path for their own purposes.** The rest
  of the 30-file sweep: `apps/three-surface-poc/src/walkthrough-inputs.ts`
  (the path only, in `OTHER_ACT_BOUND_ARTIFACTS`),
  `apps/three-surface-poc/src/test-walkthrough-judgment-fixture.ts`,
  `scripts/build_public_source_screening_scope.py`,
  `scripts/build_pwb_behavior_contract_repin.py`,
  `scripts/build_pwb_behavior_contract_repin_tree_framing.py`,
  `scripts/build_pwb_effect_acts_packet.py`,
  `scripts/build_pwb_truth_policy_amendment.py`,
  `scripts/record_public_source_screening_scope_v2_act.py` and
  `packages/polaris-generation-consent/README.md`. [Inferred] most are
  earlier packages' builders and recorders that read the path for their own
  superseded `--check`; whether any breaks is Unknown, and the install
  assesses each with the four above.
- **Provider egress population.** In provider mode cited span text reaches the
  provider through `packages/polaris-generation-core/src/pipeline.ts` under
  the egress consent; version 4 widens that population to spans of retained
  bodies. No egress rule changes, but the install's egress tests cover it.

## What the install must build (redaction)

- **Match offsets.** `detectSecrets` in
  `packages/three-surface-poc-core/src/content-classification.ts` returns the
  first matching detector id only. The rule needs every match's start and end
  from every start offset (overlapping matches included) over the complete
  body. That gives up the screens' early stop at the first
  hit and needs a per-offset (sticky) loop; [Inferred] `credential-bearing-url`'s
  `[^/@\s]+:[^/@\s]+@` can backtrack quadratically over a long run without
  `/`, `@` or whitespace at every `http` offset, so the install bounds the scan
  within the resource limits and treats a breach as a whole-file exclusion. Then the line placement, guard,
  re-screen and
  span test the builder's reference oracle (`withheld_lines`) states. The
  oracle runs the patterns in Python `re`; the screens run them as JavaScript
  `RegExp`, whose `\s` class differs (round 1, note 9), so the install runs
  the builder's body fixtures through the TypeScript screens as well.
- **The two screens.** `packages/polaris-dossier/src/screen.ts` and
  `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts`
  must agree on every body of `screen.test.ts`'s population, including the
  builder's body fixtures (`TODO(syzygy-qkea.17)` keeps them copies).
- **Class gating.** Redaction applies only to a body the scope classifies
  project-documentation (`redactedClasses`); the screens consult
  `contentClass` before choosing redaction, and every other body keeps
  whole-file exclusion.
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
- **Rendering.** A page that shows a retained body shows one marker in place
  of each run of consecutive withheld lines, each naming the redaction and the
  body's total withheld-line count, as `secretRedaction.withheldLines` says.

## What the install must build (variant `span-guides` only)

- `readProjectDocumentationRule` and `publicSourceContentClass` in
  `packages/polaris-generation-core/src/public-source-classification.ts`
  learn `rootGuideStems` and `rootGuideSuffixes`; the builder's
  documentation fixtures are the oracle.

## What it does not touch

The base (Butlers) scope's rules, the consent and egress readers, and every
specification. The Butlers read gate's pin is touched, as above: the rules
it reads are not.
