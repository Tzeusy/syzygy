# Impact ledger — public-source screening scope, version 3

> **Candidate — binds nothing.** Drafted 2026-10-08.

## Method

`grep -rlF` over `packages/`, `apps/`, `scripts/` and `.github/` at this
package's base commit for the policy's path
(`POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`) and for the
key names `activeContent` and `codeContentExemption`, then read each hit that
is not under `dist/`. A second sweep, added after round-1 review finding 7,
covers the version literal, because a version pin does not name the path:
`grep -rlF '1.3.0-public-source-candidate.1.none'` over the same four trees
(12 files, 6 of them under `dist/`), confirmed by
`git grep -lF` over tracked files (the same 6 non-`dist` files). A second
method for the act-chain readers: read
`packages/polaris-generation-consent/src/package-reader.ts` lines 342-440.

## What the act breaks until the install change lands

Every policy act replaces the policy digest, so the set the version-2 ledger
names is re-pointed a third time. The installer derives it from the recorded
act at the sitting (`scripts/install_redis_sitting.py`, step `policy`), not
from this page. Known members [Observed by the sweep above]:

- **The public-target read gate: `syzygy-fxro`.** `POLICY_ACT_FORMS`
  (`package-reader.ts:346-356`) is a closed list of two forms, version 1 and
  version 2, and `readPolicyActs` (`:394-418`) reads exactly those two as a
  chain. A third act record in `decisions/` whose file name or text carries the
  scope stem and is not a registered form makes `namesPolicy` (`:371`) refuse
  the read, so **the Redis gate closes** the moment the version-3 recorder
  writes its record, unless the same install commit adds a third
  `POLICY_ACT_FORMS` entry (file, title, identity) and extends the chain to
  version 3 needing version 2, later and over other bytes, with its
  supersession naming version 2's record path and argument.
- **The version-2 recorder's battery line.** `record_public_source_screening_scope_v2_act.py --check`
  in `PROJECT-STATUS.md` and `.github/workflows/governance-docs.yml` checks
  the applied subject, so it fails after a version-3 act by design; the
  version-3 recorder's line replaces it (the CG-26 triple, once).
- **The two consumers that run the scan.** `packages/polaris-dossier/src/screen.ts:66`
  and `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:108`
  call `scanActiveContent` on every body. Without a code change they keep
  withholding the C files under the version-3 bytes: the act alone admits
  nothing. Each must read `codeContentExemption.exemptExtensions`, skip the
  scan only for a code-content body whose extension it lists, and keep the
  scan for every other body. The render condition is met by the renderer as it
  stands (see the delta); the change should add a test that fails if a
  renderer path stops encoding.
- **The Butlers read gate** pins the policy by digest and then version (the
  version-2 ledger's statement), so it refuses until re-pinned, as after
  versions 1 and 2. [Observed] the source files that name the policy path
  there are `packages/three-surface-poc-core/src/content-classification.ts`,
  `apps/three-surface-poc/src/governance-inputs.ts` and
  `apps/three-surface-poc/src/walkthrough-inputs.ts`, plus tests.
- **Version pins.** [Observed by the version-literal sweep] the version-2
  `policyVersion` string is pinned in
  `packages/three-surface-poc-core/src/git-object-reader.ts:43` (its comment:
  "proven byte-equal in the test") and
  `apps/three-surface-poc/src/governance-inputs.ts:83` and `:104`, and carried
  by `content-classification.test.ts`, `project-shape-model.test.ts`,
  `governance-inputs.test.ts` and the version-2 recorder
  (`scripts/record_public_source_screening_scope_v2_act.py`). Each source pin
  moves to the chosen variant's version at install, with its test.
- `scripts/check_governance.py`, `check_spec_reconciliation.py` and
  `simulate_redis_sitting.py` name the policy path; whether each pins the
  digest is for the installer to derive [Unknown at drafting].

## Population this reaches

[Unknown] What any target contains beyond the run's own report; no body was
read. [Inferred] Under `all`, every admitted file with one of the 25 source
extensions; under `non-web`, the 18 outside the web list.

That same set of newly admitted bodies widens two populations the egress rule
does not change (round-1 review, finding 5):

- **What Syzygy transmits.** Review packets carry "the cited spans as Syzygy
  read them" (REQ-polaris-generation-035,
  `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:320`).
  In provider mode, span text goes to the provider
  (`packages/polaris-generation-core/src/pipeline.ts:265`, which maps each
  referenced source's spans to `{ sourceId, anchorId, text }`) under the
  public egress record. A body withheld under version 2 could be in neither;
  an exempt body can be in both. [Inferred] The added risk is small, because
  the agent session already reads the whole clone and the provider already
  receives code-content.
- **What Syzygy renders.** Every exempt body becomes quotable on a page. Its
  only remaining guards are `renderCondition` and the secret detectors.

## What is unchanged

Secret detectors, denied paths, strict UTF-8 and NUL, resource limits,
`project-documentation` screening, classes, access boundary, raw-body
handling, consents.
