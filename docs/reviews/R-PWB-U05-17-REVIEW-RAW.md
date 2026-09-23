# R-PWB-U05-17 review — PR #94 at 9bec659

Verdict: CONFIRM

## Scope

PR #94, head `9bec659e3a83c381d13fc4671e295fd7400a1523` (branch tip commit
message: `test(three-surface-poc-core): pin the maxSources/maxBytesPerSource
population-vs-breach folds`). Diff against `origin/main` touches exactly one
file:

```
$ git diff origin/main...9bec659e3a83c381d13fc4671e295fd7400a1523 --stat
 .../src/resource-ledger.test.ts                    | 78 ++++++++++++++++++++++
 1 file changed, 78 insertions(+)
```

Governing bead: `bd show syzygy-u05.17` — "N3 ledger: pin the
maxSources/maxBytesPerSource population-vs-breach fold with a test", the
exception raised at `docs/reviews/R-PWB-N3-SLICES1-2-CONFIRMATION-2-RAW.md`
lines 190-231 (PR #81, CONFIRM WITH EXCEPTIONS). That raw records: a rule-6
mutation of `observationFor`'s `maxSources` branch in
`resource-ledger.ts` — `Math.max(sourcePopulation ?? 0, breach ?? 0)` →
`sourcePopulation ?? breach ?? 0` — survived the full 1780-test suite,
because no test declared a population *and* recorded a breach with a
different value for the same limit. It also names the pre-existing
identical gap in the analogous `maxBytesPerSource` fold
(`breach === undefined ? worstBodyBytes : Math.max(worstBodyBytes, breach)`).

## (a) Both folds pinned, both directions, each operand alone

`packages/three-surface-poc-core/src/resource-ledger.test.ts` adds two
`describe` blocks tagged `(syzygy-u05.17)`, each with exactly the four cases
the bead calls for:

- `maxSources fold`: (1) breach (20) > declared population (5) → 20 wins;
  (2) declared population (50) > breach (10) → 50 wins; (3) population (7)
  alone, no breach; (4) breach (9) alone, population never declared.
- `maxBytesPerSource fold`: (1) breach (50) > charged body (5) → 50 wins;
  (2) charged body (50) > breach (5) → 50 wins; (3) charged body (6) alone,
  no breach; (4) breach (8) alone, no body ever charged.

This is exactly the combined-population-and-breach case the raw found
untested, in both directions, plus the two single-operand cases — matches
criterion (a).

## (b) Expected values are hard-coded literals

Every `expect(...)` in the eight new tests asserts against a numeric literal
written directly in the assertion (`20`, `50`, `7`, `9`, `50`, `50`, `6`,
`8`) — none is computed from the module under test or re-derives
`Math.max(...)` on the inputs. Confirmed by reading the diff hunk directly
(reproduced below); no arithmetic expression appears on the right-hand side
of any `toEqual`.

## (c) No fixture built at describe time

Read the full body of both new `describe` blocks
(`resource-ledger.test.ts:372-431`): `createResourceLedger(PWB_RESOURCE_LIMITS)`
is called inside each `it()` callback, not at `describe` scope or in a
shared `beforeEach`/module-level `const`. `OID_A` is a pre-existing
module-level constant (`const OID_A = 'a'.repeat(40)`, line 36) already used
throughout the file as a fixed object-id string, not a new shared ledger
fixture. Satisfies criterion (c) and the AGENTS.md "mutation that throws at
describe time reports zero tests and scores as survived" guardrail.

## (d) Rule-6: reproduce the raw's mutation, add one of my own, confirm each fails, revert

All mutations applied to
`packages/three-surface-poc-core/src/resource-ledger.ts` in the worktree
`/tmp/claude-1000/.../scratchpad/rev94` at HEAD `9bec659`, one at a time,
each reverted with `git checkout --` before the next, confirmed by
`git status --porcelain` (empty both times).

**Mutation 1 — the raw's own mutation (line 350):**

```
- return { state: 'observed', value: Math.max(sourcePopulation ?? 0, breach ?? 0) };
+ return { state: 'observed', value: sourcePopulation ?? breach ?? 0 };
```

`npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts`
→ **1 failed, 34 passed.** The one failure is exactly the new test "a breach
independently larger than the declared population wins" (expected 20, got
5); every other test, including the three other new `(syzygy-u05.17)` tests
and all pre-existing tests, passed. Reverted; `git status --porcelain`
empty, `grep` confirmed the original `Math.max(...)` text is back.

**Mutation 2 — my own maxBytesPerSource mutant (line 339), same shape:
prefer the charged-body operand outright over a larger breach when a body
was actually charged:**

```
- return { state: 'observed', value: breach === undefined ? worstBodyBytes : Math.max(worstBodyBytes, breach) };
+ return { state: 'observed', value: breach === undefined ? worstBodyBytes : worstBodyBytes || breach };
```

(`worstBodyBytes || breach` behaves identically to `Math.max` whenever
`worstBodyBytes` is 0, but wrongly picks `worstBodyBytes` outright whenever
it is non-zero and smaller than `breach` — the maxBytesPerSource analogue of
the raw's maxSources mutant.)

`npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts`
→ **1 failed, 34 passed.** The one failure is exactly the new test "a breach
independently larger than any charged body wins" (expected 50, got 5); all
other tests, including the other three new tests, passed. Reverted;
`git status --porcelain` empty, `grep` confirmed the original
`Math.max(worstBodyBytes, breach)` text is back.

Both mutations were caught by exactly the new test built for that branch and
nothing else — satisfies criterion (d) and rule 6.

## (e) Full `npm test` passes

Run from a clean worktree at `9bec659` after `npm ci`:

```
 Test Files  135 passed | 3 skipped (138)
      Tests  1805 passed | 3 skipped (1808)
   Duration  37.04s
```

Note the raw's earlier full-suite count (1780) was measured at PR #81's
head; this PR's own new 8 tests plus other intervening N3-slice work bring
the current total to 1805 passed / 3 skipped, all green. No failures.

## (f) No other files changed

`git diff origin/main...9bec659e3a83c381d13fc4671e295fd7400a1523 --stat`
(reproduced above) shows exactly one file touched:
`packages/three-surface-poc-core/src/resource-ledger.test.ts`, +78/-0.

## Additional notes

- The PR's code comment at the top of the new block (lines 358-369) restates
  the raw's finding accurately, including the correct verbatim quote of both
  fold expressions, and correctly scopes its claim to "no existing test
  declares a population *and* records a breach with a different value" —
  matches what Task 5 of the raw actually found.
- No conformance-literal violation: this is `resource-ledger.test.ts`, not a
  `cap1-conformance` file, so the "one conformance file per CAP1-REQ" rule
  does not apply; the general "hard-coded literal" instruction from AGENTS.md
  (never imported from the module under test) is satisfied as shown in (b).
- The PR closes the bead's exact ask and nothing more: it adds no production
  code, no behavior change, and does not touch `resource-ledger.ts` itself
  (correctly — the raw explicitly said the fold is not a live bug and the
  fix is a test, not a code change).

## Commands run (for reproducibility)

```
git fetch origin
git worktree add <scratch>/rev94 9bec659e3a83c381d13fc4671e295fd7400a1523
cd <scratch>/rev94 && npm ci
git diff origin/main...9bec659e3a83c381d13fc4671e295fd7400a1523 --stat
git diff origin/main...9bec659e3a83c381d13fc4671e295fd7400a1523 -- packages/three-surface-poc-core/src/resource-ledger.test.ts
npm test                                    # full battery, 135 files / 1805 passed / 3 skipped
# mutation 1 (raw's maxSources mutant) — edit, run, revert, confirm clean
npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts
git checkout -- packages/three-surface-poc-core/src/resource-ledger.ts
git status --porcelain                      # empty
# mutation 2 (own maxBytesPerSource mutant) — edit, run, revert, confirm clean
npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts
git checkout -- packages/three-surface-poc-core/src/resource-ledger.ts
git status --porcelain                      # empty
git worktree remove --force <scratch>/rev94
```

## Verdict rationale

All six acceptance criteria (a)-(f) are met with direct evidence: the tests
pin both folds in both directions plus each operand alone with hard-coded
literals, built inside `it()` (never at describe time); both the raw's named
mutation and an independently authored analogous `maxBytesPerSource` mutant
are each caught by exactly one new test and were reverted cleanly; the full
suite is green at 1805/1808 (3 skipped); and the diff touches only the one
test file. No exceptions found. **CONFIRM.**
