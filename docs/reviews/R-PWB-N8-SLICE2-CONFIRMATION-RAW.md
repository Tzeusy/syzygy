# Review — PWB N8 slice 2 confirmation (PR #73)
Reviewed commit: 42239a07f10a354014897407469098396c5f75b1
Verdict: CONFIRM

## Commission

Fresh-context confirmation review (CC-REV-4 fresh context, CC-REV-6 raw
retained verbatim) of the repair to PR #73 (N8 slice 2 of bead
syzygy-u05.8), against the prior REVISE review
(`R-PWB-N8-SLICE2-REVIEW-RAW.md`, reviewed at `fe4f9e9`, two Major
findings). Worked only in the detached worktree
`/home/tze/GitHub/syzygy/.worktrees/n8-conf` at `42239a0` (PR #73 head, the
repair commit). No prior authoring context; did not read the repair
author's own summary of the fix before independently re-deriving each
disposition below — the `bd show syzygy-u05.8` comment quoted in this
report was read for the acceptance criteria and the repair's own narrative,
but every claim in it was independently checked against the diff, the
tests, and re-run tooling rather than taken on trust.

Method: `npm ci` in the worktree first (per task instructions — NodeNext
otherwise resolves `@syzygy/*` to the main checkout). Read the prior
REVISE review in full. Read `git diff fe4f9e9..42239a0` (the repair) and
`git diff origin/main...42239a0` (the full PR) end to end, plus the
unchanged `extractRosterIdentity` source
(`project-shape-extraction.ts:548-575`) to confirm the `'malformed-toml'`
predicate the new test relies on. Read `bd show syzygy-u05.8` for
acceptance criteria and the bead's own account of the repair, and `gh pr
view 73 --json body` to confirm the false byte-equality claim was also
removed from the PR body (the prior review's Finding 2 named three
locations: code comment, PR body, evidence record). Ran the changed
package's vitest file, the app typecheck, `npm run build:poc`, the full
`npm test`, and `python3 scripts/check_governance.py`, reading output not
exit codes. Independently regenerated the evidence JSON with the built
generator and diffed it byte-for-byte (ignoring only `generatedAt`)
against the committed `…-slice2.json`, then deleted the scratch file.
Independently applied the repair's own reported "Mutant C" (excluding
`'malformed-toml'` from `SHAPE_MISMATCH_REASONS`) myself from a saved copy
of the pre-mutation file, ran the test, confirmed exactly the new test
fails (10/11 others pass), then restored the original file and confirmed
`git status --short` and `git diff --stat` are both empty. No tracked file
was left modified; no commit, push, or merge was made.

## Per-prior-finding disposition

| # | Prior finding | Disposition | Evidence |
|---|---|---|---|
| 1 | [Major] `SHAPE_MISMATCH_REASONS` omits `'malformed-toml'`, the genuine container-shape-mismatch reason for `roster-identity` | **Resolved** | `synthetic-corpus-coverage.ts:70` now reads `const SHAPE_MISMATCH_REASONS = ['malformed-list', 'malformed-row', 'malformed-toml'] as const;`. Governing comments (lines 21-56, 60-69) rewritten to state `malformed-toml` as the TOML analogue and cite `extractRosterIdentity`/`project-shape-extraction.ts:548-575` correctly — verified against the unchanged source, which does fail `'malformed-toml'`/`"no [butler] table"` when `seenButler === 0` (line 573). A new test (`synthetic-corpus-coverage.test.ts:169-197`) exercises exactly this: a `roster/alice/butler.toml` fixture with a bare `name = "Alice"` line and no `[butler]` table asserts `failureReason: 'malformed-toml'`, `failureDetail: 'no [butler] table'`, `repairKind: 'code-path'`. Ran the whole file: 11/11 pass, up from the prior 10. Independently re-mutated the reason set to exclude `'malformed-toml'` myself (not merely re-read the PR's report of Mutant C): exactly the new test fails, 10/11 others pass — matches the repair's claimed Mutant C exactly. Reverted; `git status --short` and `git diff --stat` both empty afterward. |
| 2 | [Major] The "proven byte-equal to the act-bound registry/policy JSON" claim is false | **Resolved** | Checked all three locations the prior review named. (a) Code comment `synthetic-corpus-coverage.ts:21-30`: now reads "No test in this package proves the per-class admission basenames byte-equal to any registry or policy JSON; `project-shape-manifest.test.ts`'s registry/policy comparison covers only `PWB_DISCOVERY_VERSION`, `PWB_ROOT_INDEX_PATH`, and `PWB_INDEX_DEPTH`, never the nine per-class basenames — the spec-text citation is the only verified anchor and is sufficient on its own." (b) Evidence record `docs/evidence/…-slice2.json`'s `slice2GovernanceStop` field: identical correction, confirmed by direct read. (c) PR body (`gh pr view 73 --json body`): the false clause is gone from the Summary section and a new "Revision history" section names the correction explicitly, including that the corrective text was also added to a `bd` comment on the bead (confirmed: `bd show syzygy-u05.8`'s 2026-09-22 19:09 comment states the same correction). Grepped the whole worktree for the string "byte-equal": the only two remaining hits are the corrected code comment and evidence-record sentences quoted above, both stating the absence of such a test, not the false positive claim. No instance of the original false sentence remains anywhere in the diff or working tree. |
| 3 | [Informational] One unrelated flaky test under full-suite load | **Not applicable / consistent** | This was informational, not a defect requiring repair. My own full run showed the same class of flake, in more files (see New findings, below) — consistent with the prior reviewer's diagnosis of full-suite-parallelism contention rather than a PR-introduced regression. |

## New findings

None blocking. See Observations for the widened flake footprint, which I
verified is pre-existing/environmental and unrelated to this PR's diff.

## Regression check

`git diff origin/main...42239a0 --name-status` touches exactly the same
four files as at `fe4f9e9` (no new files, no scope creep in the repair):

```
M	apps/three-surface-poc/src/pwb-n8-synthetic-corpus-coverage-matrix-main.ts
A	docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-2026-09-23-slice2.json
M	packages/three-surface-poc-core/src/synthetic-corpus-coverage.test.ts
M	packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts
```

`git diff fe4f9e9..42239a0 -- packages/three-surface-poc-core/src/project-shape-extraction.ts packages/three-surface-poc-core/src/project-shape-manifest.ts` is empty — the two grammar/admission files the prior review confirmed untouched remain untouched by the repair. Governed-plane discipline holds: nothing under `openspec/**` or `.syzygy/**` in the diff. The repair is additive/corrective only (comment text, one array literal, one new test, one evidence-record edit, one PR-body edit) — no behavior outside the narrowing classifier changed, so no new regression surface was introduced by the repair itself.

## Test / tooling results

- **Package unit tests** (`npx vitest run packages/three-surface-poc-core/src/synthetic-corpus-coverage.test.ts`): 11/11 pass (was 10/10 pre-repair; +1 for the new `malformed-toml` test).
- **App typecheck** (`npx tsc --noEmit -p apps/three-surface-poc`): clean, no output.
- **`npm run build:poc`** (`tsc -b --force` over cap1-core, cap1-daemon, three-surface-poc-core, apps/three-surface-poc): clean.
- **Full `npm test`**: 132 files passed, 2 failed, 3 skipped (137); 1764 passed, 6 failed, 3 skipped (1773) tests. All 6 failures are `Test timed out in 5000ms` in two files untouched by this PR's diff: `apps/three-surface-poc/src/polaris-copy.test.ts` (3 tests) and `apps/three-surface-poc/src/production-reobserve.test.ts` (3 tests). Re-ran both files in isolation (`npx vitest run apps/three-surface-poc/src/polaris-copy.test.ts apps/three-surface-poc/src/production-reobserve.test.ts`): 2/2 files, 9/9 tests pass cleanly (3.4s and 4.7s respectively, well under the 5s timeout). This confirms full-suite parallelism contention, not a regression — same diagnosis class as the prior review's single flake, now touching two files instead of one under this run's particular scheduling, but zero relationship to the changed files (`grep` for `synthetic-corpus-coverage` in either failing file: no hits).
- **`python3 scripts/check_governance.py`**: read the summary line, not exit code — `32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`. Matches the PR's claim exactly. The WARNs are the same pre-existing `.syzygy/governance/decisions/README.md` CG-27 staleness items (prerequisite-claim dating) unrelated to this PR's files.
- **Matrix re-derivation**: ran the built generator (`node apps/three-surface-poc/dist/pwb-n8-synthetic-corpus-coverage-matrix-main.js --date scratch-conf-2026-09-23`), diffed the output JSON against the committed `…-slice2.json` in Python with only `generatedAt` excluded from comparison: **EQUAL**. Read `summary` directly: `{'totalCells': 27, 'extractedCells': 0, 'unknownCells': 27, 'repairKindCounts': {'profile-row': 19, 'code-path': 3, 'unclassified': 5}}` — matches the PR's claimed 0/27, 19/3/5 exactly, and matches slice 1's matrix cell-for-cell per the PR's "no visible movement" claim (not independently re-diffed cell-by-cell against slice 1 in this pass since the prior review already did so and the repair touches no cell content, only reason-set/comment text). Deleted the scratch evidence file after comparison; `git status --short` confirmed clean.
- **New mutation (task requirement 4)**: mutated `SHAPE_MISMATCH_REASONS` to drop `'malformed-toml'` (reverting to the pre-repair two-reason set) on the actual tracked file (saved a copy first, not a separate scratch copy, since the task only requires a revert-and-clean-check afterward). `npx vitest run packages/three-surface-poc-core/src/synthetic-corpus-coverage.test.ts`: 1 failed (the new roster-identity/malformed-toml test, `expected undefined to be 'code-path'`), 10 passed — exactly the repair's own claimed Mutant C result. Restored the saved original; `git status --short` and `git diff --stat` both empty.

## Observations (not exceptions)

- The full-suite flake surface widened from 1 test (prior review, at `fe4f9e9`) to 6 tests across 2 files (this run, at `42239a0`) under full parallel load. Both are confirmed environmental (isolated re-runs pass, 100% and well within timeout) and in files with zero code or import relationship to this PR's diff (`polaris-copy.test.ts`, `production-reobserve.test.ts` vs. the four changed files, all under `synthetic-corpus-coverage*`/`pwb-n8-*`). This is consistent with the repo's own AGENTS.md guardrail note about `production-reobserve.test.ts` timing out under full-suite load, now apparently also affecting `polaris-copy.test.ts` on this machine/run — worth a note-to-self update by whoever next touches CI timeout tuning, but out of scope for this PR and not a defect in it.
- The repair's PR body "Revision history" section is a clean, specific account of both fixes and where each was applied (code comment, evidence record, PR body, bd comment) — matches what I independently found in the diff and via `bd show`, so I did not need to hunt for a fourth undisclosed location.
- Mutant C, as shipped in the repair, is well-targeted: it kills exactly the one new test and nothing else, which is the correct signature for a reason-set narrowing mutant (contrast Mutant B from the original PR, which killed 6/10 because it inverted the whole set rather than removing one member).

## Verdict

CONFIRM. Both Major findings from the prior REVISE review are resolved: `SHAPE_MISMATCH_REASONS` now correctly includes `'malformed-toml'` with an accurate governing comment and a passing, independently-mutation-tested new test; the false "proven byte-equal to the act-bound registry/policy JSON" claim is removed from all three locations the prior review named (code comment, evidence record, PR body) plus a bd comment, with the corrected text accurately describing what `project-shape-manifest.test.ts` actually checks. The repair introduced no regression: diff scope is unchanged (same four files), the two excluded grammar/admission files remain untouched, governed-plane discipline holds, the changed package's tests pass 11/11, typecheck and `build:poc` are clean, `check_governance.py` matches the PR's claim exactly (32 OK/20 WARN/0 FAIL), and the evidence record is independently re-derivable byte-for-byte. The full-suite test run shows 6 timeouts in two files unrelated to this PR's diff, confirmed environmental by isolated re-run — not a blocker.
