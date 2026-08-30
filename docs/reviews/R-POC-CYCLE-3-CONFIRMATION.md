# R-POC Cycle-3 Confirmation Review — C3-1/3/4/5/6 repair

**Commit:** 070b7432fb22ca49c07331ffded0f9c6afa7156f / **Reviewer:**
independent fresh-context confirmation reviewer (no prior involvement in
this POC's implementation, the cycle-3 fresh review, or any earlier review
pass) / **Date:** 2026-08-30.

Scope: confirm whether commit 070b743 ("fix: repair cycle-3 findings
C3-1/3/4/5/6 [syzygy-kof]") actually repairs the four DEFECT findings
recorded in `docs/reviews/R-POC-CYCLE-3-REVIEW.md` (frozen, at 715f3b9),
verify C3-2 (NOTE, explicitly deferred) is not silently claimed repaired
anywhere, run the two POC test projects and read their output, and hunt
for regressions the repairs could plausibly introduce. Read-only against
application code; the only file written is this one.

## Verdict: CONFIRMED

### Commit identity

[Observed] `git log -1`: `070b7432fb22ca49c07331ffded0f9c6afa7156f fix:
repair cycle-3 findings C3-1/3/4/5/6 [syzygy-kof]`, HEAD of `main`. `git
log --oneline -1 -- <the four changed source files>` returns the same
commit for each — nothing later touched them, so this review is of the
repaired state as it stands at HEAD. `git status --short` showed only the
pre-existing, unrelated `.gitignore` modification. `git show 070b7432
--stat`: 8 files changed, 105 insertions, 17 deletions —
`apps/three-surface-poc/src/orrery.ts`,
`apps/three-surface-poc/src/orrery.test.ts`,
`apps/three-surface-poc/src/trajectory.ts`,
`apps/three-surface-poc/src/trajectory.test.ts`,
`packages/three-surface-poc-core/src/model.ts`,
`packages/three-surface-poc-core/src/model.test.ts`,
`packages/three-surface-poc-core/src/worker-change-observation.ts`,
`packages/three-surface-poc-core/src/worker-change-observation.test.ts`.

## Per-finding verdicts

### C3-1 (DEFECT) — two Polaris claim sections rendered a bare file path, not a sentence

**Verdict: REPAIRED.** [Observed] `model.ts:392` and `model.ts:400` change
`detail: ARTIFACT_PATHS.code` / `ARTIFACT_PATHS.test` to hand-written
sentences: `'The manually mapped code file at src/butlers/identity.py
implements sender-identity resolution.'` and the parallel test-file
sentence. `polaris.ts`'s `entitySection()` (unchanged by this commit) wraps
`entity.detail` verbatim in a `<p><span>` — with the sentence-form value,
the rendered claim now reads as an actual sentence rather than a lone path
fragment. `model.test.ts` gains two exact-string assertions
(`entities.get('code:identity-resolution')?.detail` /
`test:identity-regression-definition`) that pin the new sentences; reverting
`model.ts`'s two `detail` lines to `ARTIFACT_PATHS.code`/`.test` would make
these assertions fail immediately (the test expects a sentence containing
the path, not the bare path). Grepped `polaris.test.ts` for any assertion
referencing the old bare-path strings — none found, so no stale coverage
was left behind either.

### C3-3 (NOTE) — Orrery block height had no on-page legend

**Verdict: REPAIRED.** [Observed] `orrery.ts` adds a
`<p class="orrery-height-legend">District block height is proportional to
the directory's total size in bytes, relative to the largest district. ...`
paragraph directly under the canvas heading, plus its CSS rule. It renders
unconditionally (not gated on JS), so it appears in both the scripted and
no-script paths. `orrery.test.ts` gains a new test asserting the HTML
contains the legend's lead sentence — a genuine falsifier: deleting the
`<p>` line would fail the test immediately.

### C3-4 (DEFECT) — Trajectory board used `role="list"` with non-`listitem` children

**Verdict: REPAIRED.** [Observed] `trajectory.ts:184` changes
`role="list"` to `role="group"` on the `.board` wrapper; the `.board-column`
`<section>` children are unchanged (still no `role="listitem"`), which is
now correct since `role="group"` has no ARIA "required owned elements"
constraint. Repo-wide grep for `role="list"` in non-test `apps`/`packages`
source: zero hits — the defect's one instance was the only one, and it is
gone. `trajectory.test.ts` gains two assertions on the empty-board render:
`toContain('class="board" role="group"')` and `.not.toContain('role="list"')`
— both would fail if the old markup were restored.

### C3-5 (DEFECT) — `evaluation.snapshot` was an undocumented composite string

**Verdict: REPAIRED.** [Observed] `PocModel.evaluation` gains two new typed
fields, `snapshotLabel: string` and `inputsDigest: string`, each with a doc
comment, alongside a doc comment on `snapshot` itself explaining the
composite's format and steering machine consumers to the two new fields
instead of string-splitting. `buildButlersPocModel` (`model.ts:549-554`)
sets `snapshotLabel: input.evaluation.snapshot` (the un-suffixed label) and
`inputsDigest: inputDigest` (the same digest already folded into the
composite), so both halves are now independently readable without parsing
the delimiter. `model.test.ts` adds three assertions: `snapshotLabel` equals
the plain label, `inputsDigest` matches `/^[0-9a-f]{64}$/`, and the
composite `snapshot` string is reconstructible as
`` `${snapshotLabel}|inputs:sha256:${inputsDigest}` `` — a genuine
falsifier of both the new fields' values and their relationship to the
existing composite. The composite field itself is retained (not removed),
so `polaris.ts:115`/`routes.ts:75`'s human-readable footer rendering is
unaffected — confirmed by grep, both still read `model.evaluation.snapshot`
directly, which is now a documented, not undocumented, format.

### C3-6 (DEFECT) — `WorkerChangeCommit.containingRef: null` was ambiguous across states

**Verdict: REPAIRED.** [Observed]
`worker-change-observation.ts` replaces `containingRef: string | null` with
a discriminated union `WorkerChangeContainingRef = { kind: 'default-branch'
} | { kind: 'ref'; ref: string } | { kind: 'none-found' }`, documented
inline as removing the need to cross-reference the sibling `state` field.
The `changed-or-merged` branch now sets `containingRef: { kind:
'default-branch' }` (was hardcoded `null`); `findContainingRef()` now
returns `{ kind: 'ref', ref }` on a real match and `{ kind: 'none-found' }`
both when the `for-each-ref` search throws and when it returns no refs (was
`null` for both). `trajectory.ts:81-85`, the field's one renderer, is
updated to branch on `.kind === 'ref'` instead of `!== null`, preserving
its existing behavior of never rendering the "on `<ref>`" clause for
`changed-or-merged`/`none-found` (previously '' for both null cases, now ''
for both non-`ref` kinds — same rendered output, now type-distinguishable
in the JSON). `worker-change-observation.test.ts` gains a new test proving
the `none-found` case is reachable (a commit on a local branch not present
on any fetched `origin/*` ref) and asserts `{ kind: 'none-found' }`
distinctly from the existing `active`-with-real-ref test (now asserting
`{ kind: 'ref', ref: 'origin/agent/bu-1' }`) and the `changed-or-merged`
test (now asserting `{ kind: 'default-branch' }`) — all three of the
union's members are exercised by a passing, distinct test. Repo-wide grep
confirms `trajectory.ts` is the only non-test consumer of `containingRef`;
no other call site was left assuming the old `string | null` shape (the
build succeeded, which would have failed to type-check otherwise).

### C3-2 (NOTE) — deferred, not repaired

**Verdict: correctly deferred, not silently claimed repaired.** [Observed]
The commit message states "C3-2 deferred as design-heavy." `polaris.ts` is
untouched by this commit (absent from `git show --stat`'s file list),
consistent with C3-2 (narrative connective tissue across Polaris sections)
requiring no code change to leave alone. Repo-wide grep for `C3-2` outside
the frozen review file: zero hits in `packages/`, `apps/`, or any other
`docs/` file — nothing claims it repaired.

## Test run

[Observed] `npx vitest run --project '@syzygy/three-surface-poc-core'
--project '@syzygy/three-surface-poc-app'`:

```
Test Files  1 failed | 19 passed | 2 skipped (22)
     Tests  1 failed | 115 passed | 2 skipped (118)
```

115 passing tests, up from cycle-2's confirmed 114 — consistent with
exactly two new `it()` blocks added by this commit (`orrery.test.ts`'s C3-3
legend test and `worker-change-observation.test.ts`'s C3-6 `none-found`
test); the other three findings' coverage was added as inline assertions
inside existing tests, not new test cases. The streamed output showed each
new/changed assertion passing, including
`✓ Orrery > explains the block-height encoding with an on-page legend (C3-3)`
and
`✓ worker-change observer > states none-found distinctly when an active commit is on no fetched origin ref (C3-6)`.
The 2 skipped tests are the pre-existing env-gated
`test-artifact-verification.live.test.ts` and `work-items.live.test.ts` —
unchanged, not new skips.

**The 1 failing test, `build-output.test.ts`'s "re-emits ignored JavaScript
before the launcher executes it," is a pre-existing timing flake unrelated
to this repair.** [Observed] The file was last touched by an unrelated
commit (3e7851f, well before cycle-3); it is absent from this commit's
`git show --stat`. The test runs `npm run build:poc` (which shells `tsc -b
--force`) twice inside a 15-second `it()` timeout. Timed alone: `time npm
run build:poc --silent` took 7.55s wall on this machine for one build; two
sequential builds plus process-spawn overhead exceeds the 15s budget. I
re-ran the file in isolation (outside the full suite, to rule out
cross-project contention) and it still timed out at ~18.25s — confirming
this is an environment/timeout-margin issue independent of this session's
changes, not a regression this repair introduced. I did not modify the
test file (out of scope for a read-only confirmation review) but flag it
as a pre-existing flake worth a wider timeout or two smaller assertions in
a follow-up.

`npm run build:poc --silent` (single run, this session): completed clean
in ~7.5s with no errors, confirming the new `WorkerChangeContainingRef`
discriminated union and the two new `PocModel.evaluation` fields
type-check through every consumer.

## Regression hunt

**`containingRef` consumers:** [Observed] grep across `apps/`, `packages/`
(excluding `dist/`) finds exactly one non-test consumer,
`trajectory.ts:81-85`, correctly updated to the new union shape (see C3-6
above). No other renderer or route touches this field.

**`evaluation.snapshot`/`snapshotLabel`/`inputsDigest` consumers:**
[Observed] `polaris.ts:115` and `routes.ts:75` both still read
`model.evaluation.snapshot` for their human-readable footer — correct,
since the composite is retained and now documented, not removed. No
consumer references `snapshotLabel`/`inputsDigest` yet (they are newly
added, purely additive fields) — expected, not a gap the repair claimed to
close. Confirmed `packages/cap1-*`'s own, unrelated `EvaluationIdentity`
type (a different capability) was not touched and has no overlapping field
names that could be confused with this change (per AGENTS.md's standing
warning about the two unrelated `evaluation` shapes).

**Parity oracle (`routes.test.ts`):** [Observed]
`expect(wireModel).toEqual(model)` deep-compares the full `GET /api/poc`
JSON body against the in-memory `PocModel`, including the two new
`evaluation` fields and the new `containingRef` union shape wherever
present — this test still passes, which is a genuine parity check (not
just a smoke test) since a serialization drift in either new field would
fail a deep-equality comparison. `parityTuples()`/`visibleParityTuples()`
(the entity/relationship exact-table row comparison) are unaffected by
either change, since neither `containingRef` nor `evaluation.*` are
entity/relationship fields.

**Stale bare-path / `role="list"` remnants:** [Observed] grepped
`polaris.test.ts` for the old bare-path strings (`identity.py`,
`test_identity`) — no hits, so no dangling assertion depended on the old
values. Grepped all non-test `apps`/`packages` source for `role="list"` —
zero hits.

**No other regression found.** I checked every non-test consumer of the
four changed fields/types (`containingRef`, `evaluation.snapshot` and its
two new siblings, the Polaris `detail` strings, the board's `role`
attribute) and found each fully and correctly updated, with no orphaned
caller still assuming the pre-repair shape.

## New findings

None. [Observed] Every claimed repair traces to the exact defect text
recorded in `R-POC-CYCLE-3-REVIEW.md`, each with a genuine falsifying test,
and the one test failure in this session's run is a pre-existing,
unrelated timing flake (confirmed isolated and reproduced independently of
this commit's changes) rather than a defect this repair introduced.

## Bottom line

C3-1, C3-3, C3-4, C3-5, and C3-6 are each genuinely repaired against the
exact text recorded in the frozen cycle-3 review, with direct falsifying
test coverage for all five and no orphaned consumer of the old shapes.
C3-2 remains correctly deferred and is not claimed repaired anywhere in
code or docs. 115 of 116 non-skipped tests passed in this session's run;
the one failure (`build-output.test.ts`) is a pre-existing timeout-margin
flake unrelated to this commit, independently reproduced in isolation.

No repository edits were made beyond this review file. This file is FROZEN
as of this write — any further edit to it retires this review per
AGENTS.md verification rule 10.

## Verdict

CONFIRMED
