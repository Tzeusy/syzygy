# Impact ledger — three acts for a test-only self-observation

> **Candidate — binds nothing.** What depends on the three artifacts this
> package drafts, and how each dependency was found. Every count below was
> produced by a command run on 2026-09-26 against base commit `3ee61c7`, over
> 1,537 tracked files. The command is named beside each count. Fixed-string
> matching (`grep -F`) was used throughout, per verification rule 1.

## Sweep 1 — who reads the policy file

Command: `git ls-files -z | xargs -0 grep -lF` on the policy's file name.

[Observed] 38 tracked files name
`POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`:

| Where | Files | What act 3 does to them |
|---|---:|---|
| `packages/three-surface-poc-core/src` | 6 | Code and tests. See sweep 2 for the ones that pin the version. |
| `apps/three-surface-poc/src` | 3 | `governance-inputs.ts` pins the version and scope anchors. The other two name the path only. |
| `scripts/` | 3 | See the rows below. |
| `.syzygy/governance/contracts/` | 9 | Candidate and performed packages. They name the path; only the truth-policy manifest hashes it. |
| `.syzygy/governance/decisions/` | 3 | Performed act records. Never edited. |
| `docs/` | 14 | Evidence, designs and raw reviews. Frozen or historical. No change. |

The three scripts:

- `scripts/build_pwb_truth_policy_amendment.py` hashes the current policy
  bytes. Its `--check` goes red when act 3 is applied. On 2026-09-23 the
  owner ruled that the `.18` adoption change "retires or rebases" this
  check. The packet explains what follows for act 3.
- `scripts/build_pwb_effect_acts_packet.py` builds the performed 2026-09-02
  package. `PROJECT-STATUS.md` keeps it out of the battery on purpose: its
  `--check` already fails by design. No change.
- `scripts/check_governance.py` holds the policy label's subject and its
  amendment row. A new amendment row lands with act 3's record, never
  before.

## Sweep 2 — code that pins the policy version

Command: `git ls-files -z apps packages scripts | xargs -0 grep -nE`, with
`(policyVersion|POLICY_VERSION|version).{0,20}1\.1\.0-candidate\.1`. The
matches were then read one by one.

[Observed] 10 matching lines. One of them
(`scripts/record_pwb_effect_amendment_acts.py:111`) is the observer
version, not the policy version. That leaves 9 policy-version lines in 4
files:

- `apps/three-surface-poc/src/governance-inputs.ts`: 1 line, plus the
  policy scope anchor on the same object.
- `packages/three-surface-poc-core/src/git-object-reader.ts`: 1 line, in
  `PWB_POLICY_IDENTITY`. `content-classification.ts` reuses this.
- `packages/three-surface-poc-core/src/content-classification.test.ts`:
  5 lines.
- `packages/three-surface-poc-core/src/project-shape-model.test.ts`:
  2 lines.

[Inferred] All four files must change in the same implementation change that
applies act 3. Otherwise the Butlers read authority fails closed and the
Butlers page reads Unknown.

## Sweep 3 — who pins the PWB specification's digest

Command: `git ls-files -z | xargs -0 grep -lF`, on the spec file's current
SHA-256, which is computed and never transcribed.

[Observed] 19 tracked files carry it:

- the Butlers registry entry and the policy;
- the specification's own `GOVERNING-DEPENDENCIES.md`, and 5 candidate
  patches to it;
- one performed manifest and one act record;
- 7 evidence files;
- 2 raw reviews.

The draft self registry entry is a twentieth, untracked until this commit.
It moves every time the specification moves.

[Observed] 5 candidate packages patch the specification itself. Command:
`grep -l` on `+++ b/` headers over all 21 patch files in the 8 candidate
`proposed/` directories. The five are:

- `pwb-opening-band-scenario` (`.21`)
- `pwb-exact-source-render-mode-scenario` (`.30`)
- `pwb-machine-view-amendment` (`.22`)
- `pwb-scoped-attributes-amendment` (lane B)
- `pwb-missing-currency-disclosure-scenario` (`.20`)

`dov.29` has no committed package on this base [Observed]. Each of these
acts forces the registry-entry manifest here to be regenerated.

## Sweep 4 — collisions with other candidate patches

Command: the builder's `composition_findings`, run on every `--check`. It
reads the `+++ b/` target of every `*/proposed/*.patch` in the other
candidate packages.

[Observed] 0 of the 20 patches from other packages target the policy or
either install path. The only patch that touches the Butlers registry entry
is `.18`'s, and that is a different file from the self entry.

## Sweep 5 — the observed pair

Command: `git ls-files -z | xargs -0 grep -lF 'repository:syzygy'`.

[Observed] 2 tracked files name it:

- `docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md`
- that design's raw review

No governed artifact names the pair today. The three drafts would be the
first.

## Sweep 6 — the authority lookup

Command: `grep -F PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT` over tracked
files.

[Observed] It appears in 2 files:

- `apps/three-surface-poc/src/governance-inputs.ts`, where it is defined;
- `docs/reviews/R-PWB-N8-SLICE4-REVIEW-RAW.md`, which reviewed N8 slice 4
  (`syzygy-u05.8`) and describes it as "literally one entry, keyed by" the
  observing project.

[Inferred] Both pairs have the same observing project, `project:syzygy`.
So the self pair's expectations cannot be added under the current key
without replacing the Butlers expectations. Slice 6's implementation has to
key the lookup by the (observing project, observed repository) pair.
Nothing in this package changes it.

## Not changed by any of the three acts

[Observed] These are byte-identical before and after `--apply` of all
three acts:

- the Butlers consent record and its act;
- the Butlers registry entry;
- PWB-REQ-005 and the rest of the PWB specification.

The builder checks that every policy key other than `policyVersion` and
`selfObservationScope` stays equal.
