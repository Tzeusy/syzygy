# R-POC Cycle-2 Confirmation Review — N-1/N-2/N-3 repair

**Commit:** aa18b36ad926109ebbff314e6af17c148ce128ba / **Reviewer:** independent
fresh-context confirmation reviewer (no prior involvement in this POC's
implementation, the original product review, or the cycle-1 confirmation
review) / **Date:** 2026-08-30 / **Node/toolchain:** repository's configured
toolchain, not re-captured this pass.

Scope: confirm whether commit aa18b36 ("fix: repair cycle-1 confirmation
findings N-1, N-2, N-3 [syzygy-veq]") actually repairs the three NOTE
findings recorded in `docs/reviews/R-POC-CYCLE-1-CONFIRMATION.md`, run the
two POC test projects and read their output, and attempt truth-floor
counterexamples at the changed seams. Read-only against application code;
the only file written is this one.

## Verdict: CONFIRMED

All three NOTE findings are genuinely repaired, each with direct test
coverage (N-1's new falsifying test; N-2/N-3 asserted inline in the
existing PRF-2/PRF-3 test). No new BLOCKER, DEFECT, or NOTE finding
survived counterexample attempts.

### Commit identity

[Observed] `git log -1` at review time: `aa18b36ad926109ebbff314e6af17c148ce128ba
fix: repair cycle-1 confirmation findings N-1, N-2, N-3 [syzygy-veq]`, HEAD
of `main`. `git status --short` showed only the pre-existing, unrelated
`.gitignore` modification — no POC file was dirty. `git show aa18b36
--stat`: 4 files changed, 74 insertions, 9 deletions —
`apps/three-surface-poc/src/materialize-action.ts`,
`apps/three-surface-poc/src/trajectory.test.ts`,
`apps/three-surface-poc/src/trajectory.ts`,
`packages/three-surface-poc-core/src/model.ts`.

## Per-finding verdicts

### N-1 — "materialized item exists but falls outside the current board selection" branch had no test

**Verdict: REPAIRED.** [Observed]

`apps/three-surface-poc/src/trajectory.test.ts` gains a new test, "states
honestly when the materialized item falls outside the board selection
(N-1)". It builds a fixture with a materialized bead (`bu-old-closed`,
`closed_at: '2026-01-01T00:00:00Z'`) plus 50 other closed items with later
`closed_at` dates in `2026-08-*`. `packages/three-surface-poc-core/src/
trajectory-projection.ts:80-87` sorts closed items by `closedAt` descending
and keeps `.slice(0, options.recentClosedWindow)` (`RECENT_CLOSED_WINDOW =
50`, per `model.ts`); with exactly 50 strictly-newer closed items present,
`bu-old-closed` is mathematically guaranteed to be the one item pushed past
the window and excluded from `trajectory.rendered`.

The test asserts:
```
expect(model.materializedBeadId).toBe('bu-old-closed');
expect(model.trajectory.rendered.some((item) => item.id === 'bu-old-closed')).toBe(false);
...
expect(html).toContain(
  'The demonstrated item <code>bu-old-closed</code> was materialized by this POC but falls outside the current board selection',
);
expect(html).not.toContain('data-work-item-id="bu-old-closed"');
expect(html).not.toContain('The demonstrated item is <a');
```
This directly exercises `trajectory.ts:171-176`'s
`demonstratedId === null ? '' : demonstratedRendered ? <in-selection wording> : <out-of-selection wording>`
branch at exactly `demonstratedId !== null && demonstratedRendered ===
false` — the precise gap N-1 named. Test run below confirms it passes.

### N-2 — demonstrated-item lookup regex-parsed a human-readable sentence

**Verdict: REPAIRED.** [Observed]

`packages/three-surface-poc-core/src/model.ts:106-113` adds a typed field
to `PocModel`:
```
readonly materializedBeadId: string | null;
```
documented as "The confirmed materialized Bead id... The typed source for
renderers — never re-derived from human-readable entity text." It is set
at `model.ts:553` from `materialization.beadId`, the same value already
computed by `resolveMaterializationEpistemic` (`model.ts:230-272`) — which
only returns a non-null `beadId` once the record's `beadId` is confirmed
present in the live-observed work items (see truth-floor (b) below).

`apps/three-surface-poc/src/materialize-action.ts` deletes the entire
regex path:
```diff
-export function currentMaterializedBeadId(model: PocModel): string | null {
-  const entity = model.entities.find((candidate) => candidate.id === WORK_ITEM_ENTITY_ID);
-  if (entity === undefined || entity.epistemic.label !== 'Observed') {
-    return null;
-  }
-  const match = /Beads item (\S+)\.$/.exec(entity.detail);
-  return match?.[1] ?? null;
-}
+export function currentMaterializedBeadId(model: PocModel): string | null {
+  return model.materializedBeadId;
+}
```
(also deletes the now-unused `WORK_ITEM_ENTITY_ID` constant — confirmed
dead by a repo-wide grep, no remaining references). `trajectory.ts`
continues to call the same exported `currentMaterializedBeadId(model)`
wrapper, so no call site needed to change — the fix is fully internal to
the two files that owned the regex.

Grepping `apps/three-surface-poc/src` and `packages/three-surface-poc-core/
src` for `Beads item` (excluding `.test.ts`) finds only the two places that
*generate* the sentence for display (`model.ts:400`, `model.ts:483`,
`materialize-action.ts:161`'s unrelated `${verb} Beads item ${result.beadId}`
heading) — none of them parse it back. No fragile string-to-ID coupling
remains anywhere in the non-test source.

Test evidence: the existing PRF-2/PRF-3 test in `trajectory.test.ts` gains
`expect(model.materializedBeadId).toBe('bu-demo-1');`, and `npx tsc -b
packages/three-surface-poc-core apps/three-surface-poc --force` (run this
session) compiles clean, confirming the typed field threads through with
no type error.

### N-3 — external-worker span reused the Bead-status span's CSS class

**Verdict: REPAIRED.** [Observed]

`trajectory.ts:87` changes the external-worker span's class from
`wi-status` to a new `worker-change-label`:
```
<span class="worker-change-label">External worker: ${escapeHtml(label)}</span>
```
A new rule is added at `trajectory.ts:129`:
```
.worker-change-label { font-family: var(--font-mono); font-size: .7rem; text-transform: uppercase; color: var(--cyan); }
```
against the pre-existing, unchanged `.wi-status { font-family: var(--font-mono); font-size: .7rem; color: var(--muted); text-transform: uppercase; }`
(`trajectory.ts:123`). The two classes now differ in `color`:
`var(--cyan)` (`#78e1d1`, `apps/three-surface-poc/src/design-tokens.ts:52`)
for the worker-change label versus `var(--muted)` (`#8ca3a4`,
`design-tokens.ts:47`) for the Bead-status span — a genuinely distinct,
non-trivial color contrast, not a no-op rename. The Bead-status span
(`trajectory.ts:105`, `<span class="wi-status" ...>`) is untouched.

Test evidence: the PRF-2/PRF-3 test asserts
`expect(demoCard).toContain('class="worker-change-label">External worker:');`
and `expect(demoCard).not.toContain('class="wi-status">External worker:');`
on a card confirmed (via the same test's earlier assertions) to carry both
a Bead-status span and a worker-change block — a genuine two-badge card,
not a single-badge one.

## Test run

[Observed] `npx vitest run --project '@syzygy/three-surface-poc-core'
--project '@syzygy/three-surface-poc-app'`:

```
Test Files  20 passed | 2 skipped (22)
     Tests  114 passed | 2 skipped (116)
```

One more passing test than cycle-1's confirmed run (113 → 114), consistent
with exactly one new test (`trajectory.test.ts`'s N-1 test) being added by
this commit; the streamed output showed
`✓ Trajectory > states honestly when the materialized item falls outside the board selection (N-1)`
and the updated
`✓ Trajectory > calls out and highlights the demonstrated item, and separates Bead status from worker-change state (PRF-2, PRF-3)`
(now carrying the added N-2/N-3 assertions) among the passing tests. The 2
skipped tests are the pre-existing live-gated
`test-artifact-verification.live.test.ts` and `work-items.live.test.ts`
(env-var gated), unchanged from prior reviews — not new skips.

`npx tsc -b packages/three-surface-poc-core apps/three-surface-poc --force`
(run this session): clean, no output, exit reflects success — confirms the
new `materializedBeadId: string | null` field type-checks through every
consumer.

## Truth-floor counterexample attempts

**(a) Is the N-1 test a genuine falsifier?** Yes. [Observed] It constrains
three independent things at once: the out-of-selection message text, the
absence of the excluded item's card (`data-work-item-id="bu-old-closed"`
must not appear), and the absence of the in-selection wording
(`'The demonstrated item is <a'` must not appear). If the ternary at
`trajectory.ts:172-175` had its condition inverted, or if
`demonstratedRendered` were computed against the wrong collection, at least
one of these three assertions would fail — the test was not run against a
deliberately-broken copy this session (application code was not modified,
per this review's read-only mandate), but the assertion shape leaves no
gap for the branch to silently pass while broken: [Inferred] a reviewer
reading only the ternary and the test together can confirm the test would
catch a swap of the two branches' wording, a missing exclusion check, or a
stray card render.

**(b) Does `materializedBeadId` stay null whenever the record is
unconfirmed?** Yes. [Observed] `resolveMaterializationEpistemic`
(`model.ts:230-272`) returns `beadId: null` on all three unconfirmed paths:
`record === null` (line 235), `workItems.kind === 'unknown'` (lines
238-245), and the named bead not found among observed items (lines
248-256). Only the fourth path — `found !== undefined`, i.e. the record's
`beadId` is actually present in this evaluation's live-observed work items
— returns a non-null `beadId` (line 262). `model.ts:553` assigns
`materializedBeadId: materialization.beadId` straight from this result, so
the typed field inherits the exact same fail-closed guarantee the
pre-existing `epistemic`/`origin` fields already had. No path lets an
unconfirmed record produce a non-null id.

**(c) Does the machine JSON expose `materializedBeadId` consistently with
the human page (no human/machine drift)?** Yes. [Observed]
`apps/three-surface-poc/src/routes.ts:96`: the machine endpoint body is
`JSON.stringify(getModel())` — the entire `PocModel` object serialized
verbatim, with no field allowlist/denylist. Since `materializedBeadId` is
a plain top-level field on `PocModel` (`model.ts:113`), it is automatically
included in every `GET /api/poc` response the moment it exists on the
model, with zero additional wiring — there is no code path where the human
page's `currentMaterializedBeadId(model)` (now a passthrough to
`model.materializedBeadId`) and the machine JSON's copy of the same field
could diverge; both read the identical in-memory value from the one shared
`PocModel` instance, consistent with this POC's parity-by-construction
architecture (`GET /api/poc` is `JSON.stringify(model)` verbatim, per
AGENTS.md's Notes to self). This is a strict improvement over the pre-fix
state, where the human page derived the id via a regex against `entities`
(a field the machine JSON already exposed) while no dedicated field named
the value directly — now both channels carry the same explicitly-named
field.

**(d) Any weakened parity field, denominator, or Unknown disclosure?** No.
[Observed] `trajectory.ts`'s existing `data-parity-field` attributes
(`trajectory-scope`, `trajectory-excluded-count`, `work-item-title`,
`work-item-id`, `work-item-status`, `work-item-verification`,
`worker-change-state`, `worker-change-verification`) are all untouched by
the diff — confirmed by reading the full diff hunk-by-hunk (`git show
aa18b36`), which only adds a field to `PocModel`, renames one CSS class
(and adds one new rule), simplifies a lookup function to a passthrough, and
adds tests. The `RECENT_CLOSED_WINDOW`/`selectionRule`/`renderedCount`/
`excludedCount`/`totalCount` denominators in `trajectory-projection.ts` are
untouched (not part of this diff at all). `materializedBeadId` is purely
additive to `PocModel`; nothing was removed or narrowed.

## New findings

None. [Observed] I traced every changed line in `git show aa18b36` against
each of N-1/N-2/N-3's exact recorded text, ran both affected vitest
projects, confirmed a clean `tsc -b` build, greped for any surviving
regex-on-detail-text coupling (none), and confirmed the two badges'
computed colors are genuinely distinct rather than a cosmetic no-op. I
found no new coverage gap, no weakened parity field, and no human/machine
drift introduced by this repair.

## Bottom line

N-1, N-2, and N-3 are each genuinely repaired against the exact text
recorded in `docs/reviews/R-POC-CYCLE-1-CONFIRMATION.md`. The N-1 fix adds
a real falsifying test for the previously-untested branch (114 passing
tests, up from 113, with the new test and the two new inline assertions
all individually visible in the streamed output). The N-2 fix removes the
fragile regex entirely — a repo-wide grep confirms no remaining
string-to-ID parsing dependency anywhere in non-test source, replaced by a
typed `PocModel.materializedBeadId` field that is fail-closed by
construction (inherits `resolveMaterializationEpistemic`'s existing
confirm-against-live-observed-work-items guarantee) and exposed
identically to both the human page and the machine JSON endpoint. The N-3
fix gives the external-worker label a distinct CSS class with a genuinely
different color (`var(--cyan)` vs `var(--muted)`), not just a renamed
selector. I found no counterexample against any of the four truth-floor
questions and no new BLOCKER/DEFECT/NOTE finding. **CONFIRMED.**

No repository edits were made beyond this review file. This file is FROZEN
as of this write — any further edit to it retires this review per AGENTS.md
verification rule 10.
