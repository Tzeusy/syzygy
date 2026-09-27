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
  owner's answer on this builder, asked in the `.18` package, was "Retire
  it in the adoption change (Recommended)"
  (`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md` §2,
  question 4). The packet explains what follows for act 3.
- `scripts/build_pwb_effect_acts_packet.py` builds the performed 2026-09-02
  package. `PROJECT-STATUS.md` keeps it out of the battery on purpose: its
  `--check` already fails by design. No change.
- `scripts/check_governance.py` holds the policy label's subject and its
  amendment row. A new amendment row lands with act 3's record, never
  before.

## Sweep 2 — code that pins the policy version and the policy act

Re-derived 2026-09-27 at commit `6eb406d` after round-1 review finding F7.
The first version of this sweep used a regex and missed one line.

Command: `git grep -nF '1.1.0-candidate.1' 6eb406d -- apps packages scripts`.
Denominator: the 348 tracked files under `apps/`, `packages/` and
`scripts/` at that commit. Each hit was then read and classified by hand.

`6eb406d` is on no remote ref: the branch was rebased again, onto
`66114ac` and then onto `08d4d02`. Re-run at the rebased round-2 head over
the same 348 files, the sweep finds 22 lines [Observed]. The one extra line
is this package's own builder, whose count went from 2 to 3 in the round-1
repair; the 16 lines under `apps/` and `packages/` are unchanged.

[Observed] 21 matching lines. The version string names two different
things, so the lines split three ways:

| Kind | Lines | Where |
|---|---:|---|
| Policy version | 10 lines in 4 files | `apps/three-surface-poc/src/governance-inputs.ts:72` and `:93` (the policy's scope anchors); `packages/three-surface-poc-core/src/git-object-reader.ts:43` (`PWB_POLICY_IDENTITY`, which `content-classification.ts` reuses); `content-classification.test.ts:255, 286, 406, 474, 488`; `project-shape-model.test.ts:435, 592` |
| Butlers observer version (not the policy) | 6 lines in 4 files | `governance-inputs.ts:105` (the registry's scope anchors); `project-shape-model.test.ts:464`; `project-shape-observation.test.ts:241, 268, 318`; `project-shape-observation.ts:50` |
| Scripts | 5 lines in 3 files (6 at the round-2 head) | `scripts/record_pwb_effect_amendment_acts.py:77` (policy) and `:111` (observer), in the recorder of a performed act, never edited; `scripts/build_pwb_registry_currency_briefing_amendment.py:54` (registry version); and 2 lines in this package's own builder (3 at the round-2 head) |

The version is not the only thing act 3 moves. Act 3 is a superseding
`approve-policy` act, and the same `policy` object in
`governance-inputs.ts` (lines 87-96) also names the act in force:

- `actIdentity` (line 89) and `recordingTag` (line 92) name the
  2026-09-05 amendment act. `governance-inputs.test.ts:166` asserts the tag.
- `supersession.target` (line 95) resolves through
  `PWB_SUPERSEDED_ACT_RECORDS.policy` (line 53) to the 2026-09-02 act
  record, and `PWB_ACT_RECORDS.policy` (line 48) names the 2026-09-05
  amendment act record.
- `governingActInstant` (line 76) is `2026-09-02`.

[Inferred] Act 3's adoption change must move all of these together: the ten
policy-version lines, and the act identity, recording tag, act-record path,
supersession target and scope anchors to the new act. Whether
`governingActInstant` moves too depends on what act 3's record says. If the
version or any one of those stays behind, the Butlers read authority fails
closed on PWB-REQ-005's wrong-but-present act-record cases, and the Butlers
page reads Unknown until the rest catch up. The six observer-version lines
do not move: act 3 changes no registry entry.

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
`grep -l` on `+++ b/` headers over the patch files in the 8 candidate
`proposed/` directories. The first run globbed one level deep and counted
21. Listed recursively (`git ls-files` under each `proposed/`) there are
22: this package's own, and 21 in the 7 others, one of them nested at
`pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch`.
The nested patch targets RFC-0007, not the specification, so the five
below are unchanged. The five are:

- `pwb-opening-band-scenario` (`.21`)
- `pwb-exact-source-render-mode-scenario` (`.30`)
- `pwb-machine-view-amendment` (`.22`)
- `pwb-scoped-attributes-amendment` (lane B)
- `pwb-missing-currency-disclosure-scenario` (`.20`)

`dov.29` has no committed package on this base or on `08d4d02`
[Observed]. Each of these acts forces the registry-entry manifest here to
be regenerated.

## Sweep 4 — collisions with other candidate patches

Command: the builder's `composition_findings`, run on every `--check`.
Since round-1 review finding F11 it reads every file under every other
candidate package's `proposed/` directory: a patch fails if its `+++ b/`
target is one of the three targets, and any file fails if its name is one
of the three targets' names.

[Observed] At `6eb406d`, and again at the round-2 head on `08d4d02`, the
other packages hold 21 `proposed/` files in 7 packages, all of them
patches, listed recursively. 0 target the policy or either install path,
and 0 share a name with any of the three. The round-1 builder found 20 at
`3ee61c7` because its glob was one level deep and missed the nested
`pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch`;
the population did not grow. The glob is now recursive, and a selftest
case with a nested sibling patch requires it. The only patch that touches
the Butlers registry entry is `.18`'s, and that is a different file from
the self entry.

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

[Observed] On 2026-09-27 the three acts were applied, in the order the
packet proposes (consent, policy, registry), to a fresh Git repository made
from a copy of this worktree with the round-1 repair committed: 1,552
files, the same as `git ls-files` at that repair (round-1 head `6eb406d`
plus the retained raw; the reviewed head `35e497b` had 1,554). The
round-2 review repeated the run in all six orders at `35e497b`, with the
same three paths. After the three
`--apply … --at-adoption` runs, `git status --porcelain` in that copy listed
exactly three paths: the policy (modified) and the two new files. A fourth
`--apply consent` was refused. Every other tracked file was unchanged,
including:

- the Butlers consent record and its act;
- the Butlers registry entry;
- PWB-REQ-005 and the rest of the PWB specification.

`--check` still passed in that copy and reported all three acts as
installed (the builder's word since round 2; only an owner act makes an act
performed). The builder's `--selftest` repeats this in all six orders, in a
scratch copy of the files `--check` reads.

The builder checks that every policy key other than `policyVersion` and
`selfObservationScope` stays equal.
