# R-POC Cycle-1 Confirmation Review — PRF-2/PRF-3/PRF-4 repair

**Commit:** de6535b9de998f503ab6ce7b97df6b2b2ed58019 / **Reviewer:** independent
fresh-context confirmation reviewer (no prior involvement in this POC's
implementation or the original product review) / **Date:** 2026-08-30 /
**Node:** `node -v` not re-captured this pass; test run below used the
repository's configured toolchain.

Scope: confirm whether commit de6535b ("fix: repair deferred product-review
findings PRF-2, PRF-3, PRF-4 [syzygy-2ne]") actually repairs the three
non-blocking findings recorded in `docs/reviews/R-POC-PRODUCT-REVIEW.md`
("Findings for the repair pass" section), run the two POC test projects and
read their output, and attempt truth-floor counterexamples at the changed
seams. Read-only against application code; the only file written is this one.

## Verdict: CONFIRMED WITH EXCEPTIONS

All three findings are genuinely repaired and test-covered for their primary
scenario. One new NOTE-severity gap survives: the "materialized item exists
but falls outside the current board selection" branch added for PRF-3
(`trajectory.ts:175`) has no test coverage — code inspection shows it is
correct, but per AGENTS.md verification rule 6 it has not been proven by a
falsifier. This does not defeat the repair (no incorrect behavior was
observed), so I am not withholding CONFIRMED outright, but it should not be
called fully proven either.

### Commit identity

[Observed] `git log -1` at review time: `de6535b9de998f503ab6ce7b97df6b2b2ed58019
fix: repair deferred product-review findings PRF-2, PRF-3, PRF-4 [syzygy-2ne]`,
HEAD of `main`. Working tree at review time carried only the pre-existing,
unrelated `.gitignore` modification (per `git status`) — no POC file was
dirty. `git show de6535b --stat`: 7 files changed, 181 insertions, 7
deletions — `apps/three-surface-poc/src/materialize-action.ts`,
`apps/three-surface-poc/src/trajectory.test.ts`,
`apps/three-surface-poc/src/trajectory.ts`,
`packages/three-surface-poc-core/src/materialization.test.ts`,
`packages/three-surface-poc-core/src/materialization.ts`,
`packages/three-surface-poc-core/src/model.test.ts`,
`packages/three-surface-poc-core/src/model.ts`.

## Per-finding verdicts

### PRF-2 — dual-badge cards need one line distinguishing Bead status from worker-change state

**Verdict: REPAIRED.** [Observed]

`apps/three-surface-poc/src/trajectory.ts:88` adds, inside
`workerChangeBadge()`, a line rendered only when a worker-change badge is
attached to a card:

```
<span class="worker-change-note">Independent of the Bead status above: this row is the worker-change state observed from git on the bounded seam, not the Beads status.</span>
```

This function is called from `itemCard()` (`trajectory.ts:107`) with
`workerChange` set to non-null only when `workerChange.beadId === item.id`
(`trajectory.ts:161`) — i.e., exactly the one card (at most) that carries
both the always-present Bead-status span (`wi-status`, `trajectory.ts:105`)
and the worker-change block. `workerChangeBadge()` returns `''` when
`workerChange === null` (`trajectory.ts:72-74`), so the note cannot appear on
a single-badge card.

Test evidence: `trajectory.test.ts` (new test, "calls out and highlights the
demonstrated item, and separates Bead status from worker-change state
(PRF-2, PRF-3)") asserts `demoCard.toContain('Independent of the Bead status
above')` and `unrelatedCard.not.toContain(...)` for a card sharing the same
board but with no worker-change match.

### PRF-3 — surface the demonstrated item so a fresh reader need not scroll ~244 cards

**Verdict: REPAIRED for the primary scenario; the "materialized but excluded
from selection" branch is untested (see New Findings, N-1).** [Observed]

`trajectory.ts:149-183` adds:
- `demonstratedId = currentMaterializedBeadId(model)` (the same lookup the
  materialize panel already used; the diff only renames it from
  `currentBeadId` to the now-exported `currentMaterializedBeadId` in
  `materialize-action.ts`, function body unchanged).
- An intro `<p class="demo-callout notice">` naming and linking the
  demonstrated item when it is both materialized and present in the current
  board selection: `The demonstrated item is <a href="#workitem-...">`.
- A distinct, honest wording when the item was materialized but is not in
  the rendered selection ("...was materialized by this POC but falls outside
  the current board selection, so no card is shown for it.").
- No callout at all (`''`) when nothing has been materialized.
- Per-card highlighting: `wi-card-demonstrated` class and a `Demonstrated
  item` badge span, gated on `item.id === demonstratedId`
  (`trajectory.ts:99-102,163`).

The declared denominator (`trajectory.renderedCount`/`totalCount`/
`excludedCount`, `data-parity-field="trajectory-scope"` /
`"trajectory-excluded-count"`, `trajectory.ts:178-181`) is untouched by the
diff — confirmed by reading the surrounding lines against the pre-repair
version in `git show de6535b -- apps/three-surface-poc/src/trajectory.ts`,
which shows only additive hunks around the scope-statement block.

Test evidence: the same new `trajectory.test.ts` test asserts the demo card
gets `wi-card-demonstrated` and the badge text, the unrelated card gets
neither, and a second model (`noneModel`, no `materializationRecord`) yields
`noneHtml.not.toContain('class="demo-callout')` and `.not.toContain('Demonstrated item')`.

**Not tested:** the "materialized but outside the current board selection"
branch (`trajectory.ts:175`) — a real, reachable state, since the board's
selection rule excludes older closed items beyond
`RECENT_CLOSED_WINDOW = 50` (`model.ts:17`, `trajectory-projection.ts`), so a
long-since-closed materialized item would hit exactly this path. I read the
ternary at `trajectory.ts:172-175` and it looks correct (checks
`demonstratedRendered`, computed at `trajectory.ts:150-151` as
`trajectory.rendered.some((item) => item.id === demonstratedId)`), but no
test exercises `demonstratedId !== null && demonstratedRendered === false`.
This is a coverage gap, not an observed defect — see N-1.

### PRF-4 — word created vs reused from the materialization record

**Verdict: REPAIRED.** [Observed]

`packages/three-surface-poc-core/src/materialization.ts:77` adds an optional
`origin?: 'created' | 'reused'` field to `MaterializationRecord`, documented
exactly as the finding asked: "Absent on records written before this field
existed — readers must render that as 'created or reused', never guess."
`materializeWorkItem()` sets `origin: 'reused'` on the found-by-external-ref
path (`materialization.ts:330`) and `origin: 'created'` on the real-create
path (`materialization.ts:370`).

`packages/three-surface-poc-core/src/model.ts:209-267`
(`resolveMaterializationEpistemic`) surfaces `origin: record.origin ?? null`
into a new `MaterializationEpistemic.origin` field, and
`relationship:intent-to-work`'s statement (`model.ts:468-479`) is now
conditional:

```
materialization.origin === 'created'
  ? 'created'
  : materialization.origin === 'reused'
    ? 'reused the existing'
    : 'created or reused'
```

Test evidence: `model.test.ts` (new test, "words the intent-to-work basis by
the record origin: created, reused, or the honest legacy both (PRF-4)")
directly asserts all three basis strings, including the no-`origin`-field
legacy case producing exactly `'The human-triggered materialization step
created or reused Beads item bu-materialized1.'` — never a guess.

This statement string is not confined to a unit test fixture: it is the same
`relationship.statement` field rendered on Polaris
(`apps/three-surface-poc/src/polaris.ts:43`) and on the shared
entity/relationship table used by the home page and Orrery's backstop
(`apps/three-surface-poc/src/exact-tables.ts:43`,
`data-parity-field="relationship-statement"`), so the fix propagates to every
surface that showed the old always-"created" wording, not just `model.ts`'s
own unit tests.

`materialization.test.ts` also gained direct assertions that a real create
persists `origin: 'created'` and a real found-by-external-ref reuse persists
`origin: 'reused'`.

## Test run

[Observed] `npx vitest run --project '@syzygy/three-surface-poc-core' --project '@syzygy/three-surface-poc-app'`:

```
Test Files  20 passed | 2 skipped (22)
     Tests  113 passed | 2 skipped (115)
```

The 2 skipped tests are the pre-existing live-gated
`test-artifact-verification.live.test.ts` and `work-items.live.test.ts`
(gated by `SYZYGY_POC_BUTLERS_REPO`/`SYZYGY_POC_BUTLERS_PYTHON`), consistent
with prior reviews' runs — not new skips introduced by this commit. All
newly-added tests (`trajectory.test.ts`'s PRF-2/PRF-3 test, `model.test.ts`'s
PRF-4 test, and the two `materialization.test.ts` origin assertions) are
included in the 113 passing and were individually visible in the streamed
output (e.g. `✓ Trajectory > calls out and highlights the demonstrated item,
and separates Bead status from worker-change state (PRF-2, PRF-3)`).

`python3 scripts/check_governance.py` at de6535b: **32 OK, 19 WARN, 0 FAIL
(51 checks)** — read from script output, identical totals to the original
product review's run at commit 2c1f8d5 and the PRF-1 confirmation pass at
f1c2901. Unaffected by this repair, as expected for an application-code-only
change with no governance-plane edits.

## Truth-floor counterexample attempts

**(a) Could a legacy materialization record lacking `origin` ever render as
definitively "created"?** No. [Observed] `model.ts:214` documents "null for
pre-origin records"; the ternary at `model.ts:472-478` only reaches
`'created'` when `materialization.origin === 'created'` exactly — a legacy
record (`origin` undefined) resolves to `origin: null` at
`model.ts:258` (`record.origin ?? null`) and therefore falls through to the
final `'created or reused'` branch. Directly proven by the `model.test.ts`
test's third assertion, `basisFor(record)` (no `origin` key) →
`'created or reused'`.

**(b) Could the demonstrated-item highlight/callout attach to the wrong
card, or render when nothing was materialized?** Not by anything I could
construct from reading the code and tests. [Observed] `demonstratedId` comes
from the same exact-string-match Bead ID (`currentMaterializedBeadId`,
unchanged logic, only renamed) that the pre-existing materialize panel
already relied on; card attachment is a plain `item.id === demonstratedId`
string equality (`trajectory.ts:163`), and `demonstratedId` is `null`
whenever nothing is materialized (`materialize-action.ts:37-44` returns
`null` unless the `work:whatsapp-single-event-normalization` entity is
`Observed`), so `item.id === null` is never true for a real card ID —
confirmed by the `noneModel` test case rendering neither the callout nor any
`Demonstrated item` badge. **Caveat** [Inferred]: `currentMaterializedBeadId`
extracts the ID via a regex against the entity's human-readable `detail`
string (`/Beads item (\S+)\.$/` against `Materialized as Beads item
${id}.`), a pre-existing fragile coupling between display text and
materialize logic that this commit did not introduce or touch — flagged
below as N-2, not a new defect from this repair.

**(c) Does the PRF-2 note appear only on cards that actually carry both
badges?** Yes. [Observed] Every card always carries the Bead-status span
(`wi-status`, unconditional at `trajectory.ts:105`); the note is emitted
only inside `workerChangeBadge()`'s non-null branch, which itself only
renders for the one card (at most) whose `id` matches the observed
worker-change's `beadId`. No path renders the note on a card without a
worker-change block.

**(d) Does any of the new markup weaken the human/machine parity fields or
the declared board denominator?** No parity field was removed or altered.
[Observed] The Trajectory page's existing `data-parity-field` attributes
(`trajectory-scope`, `trajectory-excluded-count`, `work-item-title`,
`work-item-id`, `work-item-status`, `work-item-verification`,
`worker-change-state`, `worker-change-verification`) are all untouched by
the diff. The new `demo-callout`/`demo-badge` markup carries no
`data-parity-field` attribute of its own, so it makes no claim the JSON
answer is checked against — it is additive presentation over already-parity-
tracked fields (`demonstratedId`/`demonstratedRendered` are derived at
render time from `model.trajectory.rendered` and the same entity the
materialize panel already reads, not new state). [Inferred] I note this as
consistent with the existing per-surface parity posture recorded in
AGENTS.md's "Notes to self" (Trajectory is not covered by the exhaustive
`routes.test.ts`-style marker sweep, which is scoped to the home page only,
per `apps/three-surface-poc/src/routes.test.ts:242`) — this commit neither
improves nor regresses that pre-existing scope.

## New findings

- **N-1 (NOTE — test-coverage gap):** the "materialized item exists but
  falls outside the current board selection" branch added for PRF-3
  (`apps/three-surface-poc/src/trajectory.ts:175`) has no test exercising
  `demonstratedId !== null && demonstratedRendered === false`. Code reading
  shows the ternary at `trajectory.ts:172-175` is structurally correct, but
  per AGENTS.md verification rule 6 ("mutate the input and confirm the check
  fails... before trusting it") this specific rendering path has not been
  proven by a falsifier. Recommend a follow-up test that materializes an
  item and constructs a `workItems` fixture where that item is excluded from
  `trajectory.rendered` (e.g., an old closed item outside the
  `RECENT_CLOSED_WINDOW`).
- **N-2 (NOTE — pre-existing, not introduced by this commit):** the
  demonstrated-item lookup (`currentMaterializedBeadId`,
  `apps/three-surface-poc/src/materialize-action.ts:37-44`) determines the
  materialized Bead ID by regex-matching the entity's human-readable
  `detail` sentence (`Materialized as Beads item ${id}.`,
  `packages/three-surface-poc-core/src/model.ts:395`) rather than reading
  `materialization.beadId` directly through the model. This commit reused
  and merely exported this existing function under a new name rather than
  wiring PRF-3's highlight through a more direct, less string-fragile path.
  Not a defect today (both the panel and the new highlight/callout logic
  agree, and the sentence format is a `model.ts`-owned constant), but a
  future change to the detail sentence's wording would silently break the
  demonstrated-item highlight without any type error.
- **N-3 (NOTE — cosmetic):** the worker-change badge's own "External worker:
  ..." span reuses the `wi-status` CSS class
  (`apps/three-surface-poc/src/trajectory.ts:87`), the same class the
  Bead-status span uses (`trajectory.ts:105`). Both render with identical
  styling (`.wi-status { ... color: var(--muted); text-transform:
  uppercase; }`, `trajectory.ts:123`), so the two fields PRF-2 asked to be
  distinguished still look visually identical apart from their differing
  label text and the newly-added prose note beneath them. Does not
  contradict the PRF-2 fix (the prose note is the actual repair, and it
  works), but a future pass could give the two badges distinct classes so
  the visual design reinforces the copy.

## Bottom line

PRF-2, PRF-3, and PRF-4 are each genuinely repaired against the exact text
of the deferred findings, with direct test coverage for every scenario
except one reachable-but-untested branch (N-1). All 113 non-skipped tests in
the two POC vitest projects pass, including every newly-added assertion;
governance totals are unchanged at 32 OK / 19 WARN / 0 FAIL. I found no
counterexample where a legacy record renders a false "created" claim, where
the demonstrated-item highlight attaches to the wrong card or appears absent
materialization, where the PRF-2 note leaks onto a single-badge card, or
where the repair weakens any existing parity field or the declared board
denominator. **CONFIRMED WITH EXCEPTIONS** — the exception being N-1's
untested branch, which I could not falsify by reading but also did not see
exercised by any test, plus two non-blocking NOTEs (N-2, N-3) for the next
improvement cycle.

No repository edits were made beyond this review file. This file is FROZEN
as of this write — any further edit to it retires this review per AGENTS.md
verification rule 10.
