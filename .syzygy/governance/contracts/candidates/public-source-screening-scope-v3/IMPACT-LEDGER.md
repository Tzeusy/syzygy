# Impact ledger — public-source screening scope, version 3

> **Candidate — binds nothing.** Drafted 2026-10-08.

## Method

`grep -rlF` over `packages/`, `apps/`, `scripts/` and `.github/` at this
package's first base commit for the policy's path
(`POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`) and for the
key names `activeContent` and `codeContentExemption`, then read each hit that
is not under `dist/`. A second sweep, added after round-1 review finding 7,
covers the version literal, because a version pin does not name the path:
`grep -rlF '1.3.0-public-source-candidate.1.none'` over the same four trees,
which also hits untracked built copies under `dist/`. A second method,
`git grep -lF` over tracked files, gives 6 files; it was re-run after the
rebase onto PR #403's merge and gave the same 6 files. A second
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
- **The version-2 recorder's two battery lines.** These are
  `record_public_source_screening_scope_v2_act.py --check` and `--selftest`,
  at `PROJECT-STATUS.md:403-404` and
  `.github/workflows/governance-docs.yml:222-226`. Both fail after a version-3
  act. `--check` checks the applied subject. `--selftest` crashes, because the
  version-2 builder refuses a policy that is neither its base nor its row
  [Observed by the package's round-1 reviewer, who simulated the act]. The
  version-3 recorder's lines replace all four (the CG-26 triple, once).
- **`check_governance.py` CG-7e.** [Observed by the same simulation] after a
  version-3 act, CG-7e fails six ways:
  - the version-2 manifest, the version-2 act record (its bare `Exact digest`
    line) and `ACCEPTANCE-ACT-RECORD.md` each "does not contain its current
    argument";
  - the version-3 manifest is in neither act-copy registry.

  This package registers the version-3 manifest now, gated on the version-3
  act record's existence (`_activate_public_source_scope_v3_copy_registry`),
  so the registration does nothing before the act. The version-2 copies need
  historical pinning at install, as after earlier superseding acts; a
  version-3 recorder cannot supply that.
- **The two screens and the three call sites that use them.** The screens
  are `packages/polaris-dossier/src/screen.ts:85` and
  `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:138`.
  Both run `scanActiveContent` on every body. Three non-test call sites
  screen a blob body:
  - `apps/three-surface-poc/src/polaris-generation/repo-corpus.ts:227`;
  - `packages/polaris-dossier/src/check.ts:577`;
  - `packages/polaris-dossier/src/review.ts:188`.

  The other three `screenBody(` callers (`render.ts:257`, `render.ts:360`,
  `close.ts:124`) screen agent text, and use only the secret result.

  Without a code change, the screens keep withholding the C files under the
  version-3 bytes: the act alone admits nothing. `screenBody(body)` carries
  no path and no class, so the change must give the screen the body's path or
  class. It skips the scan only for a code-content body whose extension
  `exemptExtensions` lists, and keeps it for every other body.

  That decision is one per body, not per sink: the exempt body is
  screening-admitted everywhere (`egress`). Only a page sink that cannot meet
  `renderCondition` scans again, and only for that page. [Observed] Since
  PR #403, both screens take a path's class from one shared function,
  `publicSourceContentClass` in
  `packages/polaris-generation-core/src/public-source-classification.ts`
  (`screen.ts:5`, `public-source-screening.ts:43`). That module is one home
  from which both could read the exemption. The renderer as it stands meets
  the render condition (see the delta). The change should add a test that
  fails if a page path stops encoding, or if a page loses its CSP or moves it
  after body bytes.
- **The app reader's act port (pre-existing).** `checkoutPolicyActPort`
  (`public-source-screening.ts:72`) reads only the version-1 act record
  (`PUBLIC_SOURCE_ACT_RECORD_PATH`, `:51`). [Inferred by the round-1
  reviewer, from the code and the records; not run] It has refused on the
  real checkout since the version-2 act. Its file says it has "no production
  caller" (`:36`). This is PR #403's F3, tracked as `syzygy-p83h`. Teaching
  this screen the exemption needs that reader moved to the act chain first.
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
- `check_spec_reconciliation.py` and `simulate_redis_sitting.py` name the
  policy path. Whether each pins the digest is for the installer to derive
  [Unknown at drafting]. `check_governance.py` is covered above.

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
  remaining guards are `renderCondition`, the base `renderRule` and the
  secret detectors.

## What is unchanged

Secret detectors, denied paths, strict UTF-8 and NUL, resource limits,
`project-documentation` screening, classes, access boundary, raw-body
handling, consents.
