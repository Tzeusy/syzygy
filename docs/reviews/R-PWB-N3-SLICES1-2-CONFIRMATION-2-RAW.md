# Review — PWB N3 slices 1-2 second confirmation (PR #81)
Reviewed commit: eea5fb052352bff6fa07e36d921dcd93b27761e5
Verdict: CONFIRM WITH EXCEPTIONS

## Scope

Fresh-context confirmation review (CC-REV-4, CC-REV-6) of PR #81 (bead
`syzygy-u05.3`, N3 slices 1-2 only), in a fresh worktree
`.worktrees/pr81-conf2`, detached at `eea5fb0`. Two prior raws precede this
one: the original review (`R-PWB-N3-SLICES1-2-REVIEW-RAW.md`, REVISE at
`8965020`, three findings) and the first confirmation
(`R-PWB-N3-SLICES1-2-CONFIRMATION-RAW.md`, REVISE at `91b0cbe`, three
findings resolved, one new finding: `maxSources.observed` undercounted
`manifest.sources.length` for path-only sources). This review confirms the
repair at `eea5fb0` (`git diff 91b0cbe..eea5fb0`), re-derives its own
answers to the dispatch questions rather than trusting the bd comment, and
runs its own rule-6 mutation distinct from either prior raw's. Acceptance
criteria: `bd show syzygy-u05.3` (slices 1-2: "summary() exposes
declared/observed/remaining for all seven limits plus the cost record; a
guard test fails when a registry pass identity pushes the worst source past
the declared margin and names the source"), AGENTS.md, and VIS-2
(`.syzygy/governance/doctrine/vision.md:96-104`).

## Task 1 — disposition of every finding from both prior raws

**Review-raw Finding 1 (false zero for 5/7 limits) — RESOLVED at `91b0cbe`,
unchanged and still correct at `eea5fb0`.** `ResourceLimitObservation` is a
discriminated union (`resource-ledger.ts:98-100`); confirmed by reading the
type and the `byLimit` construction in `summary()` (`resource-ledger.ts:368-375`).

**Review-raw Finding 2 (`maxBytesPerSource` ignored the populated `bodies`
map) — RESOLVED at `91b0cbe`, unchanged and correct at `eea5fb0`.**
`observationFor`'s `maxBytesPerSource` case reads
`Math.max(0, ...bodies.values())`, folding in a breach only when higher
(`resource-ledger.ts:337-340`).

**Review-raw Finding 3 (`maxIndexDepth` unused constant) — RESOLVED at
`91b0cbe`, unchanged and correct at `eea5fb0`.** `observationFor`'s
`maxIndexDepth` case returns `PWB_INDEX_DEPTH` unconditionally
(`resource-ledger.ts:352-355`); `PWB_INDEX_DEPTH = 3` is a fixed literal
(`project-shape-manifest.ts:45`), independent of any per-run traversal.

**Review-raw Observation (`project-account-extraction` mischaracterized as
"future") — RESOLVED at `91b0cbe`**, confirmed still reads "an
already-registered pass identity...newly applying to this source" in
`resource-ledger.test.ts`.

**Confirmation-raw Finding (`maxSources.observed` used `passes.size`
instead of `manifest.sources.length`) — RESOLVED at `eea5fb0`.** See Task 2
for the independent re-derivation of why this repair is structurally sound,
not just fixture-deep.

No finding from either prior raw is open.

## Task 2 — `declareSourcePopulation` population identity and call-site coverage

Traced `declareSourcePopulation` end to end rather than trusting the diff's
own claim.

**Same population as the breach check, structurally, not just by luck in
one fixture.** `project-shape-observation.ts:550` calls
`ledger.declareSourcePopulation(manifest.sources.length)`; five lines later
(`:555-557`) the pipeline's own `maxSources` breach check compares
`manifest.sources.length > limits.maxSources` — the identical expression,
read from the identical local. `manifest` is a `const` bound once at
`:542` and never reassigned, so these two reads cannot diverge within one
call. I also verified `manifest.sources.length` equals `shape.counts.sources`
structurally, not just for this PR's fixture: `classifyManifestSources`
(`content-classification.ts:529`) does `manifest.sources.map(...)` — a 1:1
map, never a filter — into `results`, and `project-shape-coverage.ts:580`
sets `counts.sources = sources.length` from that same-length array. So
`declareSourcePopulation`'s argument, the breach check's population, and
`shape.counts.sources` are the same number by construction for every
manifest this pipeline can produce, not only the PR's 15-source fixture.

**Call-site coverage — every path that can reach `ledger.summary()` has
already called `declareSourcePopulation`.** `observeProjectShapeSources`
has four early returns before line 550 (empty/option-shaped
`repositoryId`/`revision` at :494-496, non-ISO `capturedAt` at :498,
`gitCaptureFailed` at :512/:519/:525/:527, and `derived.kind ===
'invalid-input'` at :541) — every one returns `{kind: 'invalid-input'}` or
`{kind: 'unknown', ...}` via `ProjectShapeObservationResult`, neither of
which carries a `resourceUse` field at all. The only consumer of
`ledger.summary()` in production is `project-shape-model.ts:641`
(`resourceUse: ledger.summary()`), reached exclusively through the
`kind: 'observed'` branch of `ProjectShape`; every early-exit path in
`buildProjectShape` (`observationFailed`, `:452-459`) constructs a
`{kind: 'observation-failed', ...}` shape, which likewise has no
`resourceUse` field (confirmed: `Extract<ProjectShape, {kind:
'observation-failed'}>` carries `failure` and `claim` only). So there is no
path in this codebase where `summary()` is called before
`declareSourcePopulation` has already run, and no path where a shape
reports stale data — `sourcePopulation` is a fresh closure variable per
`createResourceLedger` call, and exactly one ledger is created per
`buildProjectShape` invocation (`project-shape-model.ts:472`, inside the
`read` closure), so there is no cross-call staleness either. **Answer: no,
a path cannot leave it undeclared while reporting Unknown for a known
value, and no path can report a stale value** — the two facts (declare,
then possibly breach, then possibly summarize) are sequential in the same
function call on the same ledger instance.

## Task 3 — the invariant test

`shape.resourceUse.byLimit.maxSources.observed` is compared with `toEqual`
against `{ state: 'observed', value: shape.counts.sources }`
(`project-shape-model.test.ts:935`), and
`shape.resourceUse.sourcesTraversed` is asserted `not.toBe(shape.counts.sources)`
(`:936`) — confirming the two populations genuinely diverge in this fixture
(14 vs 15) rather than the invariant being vacuously true. I confirmed by
mutation (Task 5) that removing the `declareSourcePopulation` call breaks
exactly this invariant and nothing else. Literals: `declared: 512` for
`maxSources` in the fixture (`:895`) matches
`PWB_RESOURCE_LIMITS.maxSources` hand-typed, not imported
(`project-shape-observation.ts:76`); `observed.value: 15` and
`remaining.value: 497` are likewise hand-typed, matching `POPULATION`'s
15-entry array (`:268-283`) and `512 - 15`. No expected value is computed
by calling the module under test.

One accuracy slip, not a correctness issue: both the `resource-ledger.ts`
doc comment and the `project-shape-model.test.ts` fixture comment describe
`openspec/specs/alpha/spec.md` as "POPULATION's 15th entry" — it is
actually the 13th of 15 (`POPULATION[12]`, counted directly against the
array at `project-shape-model.test.ts:268-283`). The test assertions
themselves (`shape.counts.sources === 15`,
`byLimit.maxSources.observed === {state:'observed', value: 15}`) are
unaffected; this is purely a mis-numbered comment, inherited from the same
mistake in the confirmation-raw's own finding text. Listed as an
Observation below, not a Finding.

## Task 4 — every limit's `observed` source, re-examined

- **`maxTotalBytes`** — `total`, incremented only in `chargeBody` when the
  body is actually admitted (`evaluateBody` returns early with a breach,
  uncounted, when the projected total would exceed the limit;
  `resource-ledger.ts:256-263, 289-297`). Consistent with the registry
  semantics ("count each...body once") and the module's own doc comment.
  Not disputed.
- **`maxParsePassesPerSource`** — `maxPassesOnOneSource = Math.max(0,
  ...passes.values())`, and, unlike `maxBytesPerSource`/`maxSources`, this
  case does **not** fold in `observedFromBreaches`
  (`resource-ledger.ts:335-336`). I checked whether this is an
  inconsistency with the other two fold-in cases and concluded it is not:
  `chargePass` explicitly does not increment `passes` on breach — "the
  traversal never runs, so it is not counted as performed"
  (`:270-275`, `resource-ledger.ts:59-61`'s class doc). Unlike a manifest
  source (which exists whether or not it is traversed) or a body's byte
  length (known from Git metadata whether or not the body is opened), a
  parse pass that never ran genuinely did not happen — folding in the
  breach's `observed` (the *attempted* pass count) here would itself be
  dishonest, claiming a pass occurred that the pipeline refused to run.
  Not a Finding.
- **`maxBytesPerSource`** — reconfirmed unchanged from the prior
  confirmation; genuine ledger evidence (`worstBodyBytes`), folding a
  breach only when higher.
- **`maxIndexDepth`** — reconfirmed unchanged; fixed constant, honest given
  the architecture's fixed three-level shape (prior confirmation's
  reasoning still holds; `PWB_INDEX_DEPTH` is stamped unconditionally at
  `project-shape-manifest.ts:512`).
- **`maxHumanResponseBytes` / `maxMachineResponseBytes`** — reconfirmed via
  grep that `boundedResponse` (`apps/three-surface-poc/src/routes.ts:138`)
  takes no `ledger` parameter and is the sole call site for both response
  types (`:152, 162, 177`); genuinely unmeasured by this ledger, correctly
  `state: 'unknown'`.
- **`maxSources`** — the repair's own logic (Task 2) is sound. But probing
  it with rule-6 mutation (Task 5 below) surfaced one untested branch —
  see the Exception below.

## Task 5 — own rule-6 mutations

Two mutations, both against tracked source, both reverted with `git
checkout --` before continuing (`git status --porcelain` empty after each):

1. **Removed the `declareSourcePopulation` call** at
   `project-shape-observation.ts:550` (commented out). Ran
   `project-shape-model.test.ts`: exactly 1 failure, in the "resource
   envelope" test, `shape.resourceUse` mismatch — `maxSources.observed`
   became `{state: 'unknown', reason: '...'}` instead of `{state:
   'observed', value: 15}`. 28 other tests in that file unaffected. This
   confirms the call is load-bearing and the invariant test (Task 3)
   actually exercises it.

2. **Changed `observationFor`'s `maxSources` fold** from
   `Math.max(sourcePopulation ?? 0, breach ?? 0)` to `sourcePopulation ??
   breach ?? 0` (i.e., dropped the `Math.max`, preferring the declared
   population outright over a larger breach value when both are present).
   Ran `resource-ledger.test.ts` + `project-shape-model.test.ts` (56 tests)
   and then the full `npm test` (134 files / 1780 tests): **all passed,
   zero failures** — this mutation survives the entire suite.

## Exception — the `maxSources` population/breach fold has an untested branch (not a live bug)

Mutation 2 above is a real gap: no test in this PR (or the codebase)
exercises the case where `declareSourcePopulation` has been called *and* a
`maxSources` breach was separately recorded with a *different* (in
particular, larger) value than the declared population — the only
scenario in which `Math.max(sourcePopulation ?? 0, breach ?? 0)` differs
from `sourcePopulation ?? breach ?? 0`. `resource-ledger.test.ts:319-326`'s
"a recorded breach can raise maxSources...above what this ledger charged
directly" test records a breach with **no** `declareSourcePopulation` call
at all (`sourcePopulation` stays `undefined`), so it exercises only the
`breach`-alone side of the `??` chain, not the fold-when-both-present side.

This is not, today, a live honesty defect: the sole production call site
(`project-shape-observation.ts:550-557`) always calls
`declareSourcePopulation(manifest.sources.length)` immediately before
checking `manifest.sources.length > limits.maxSources` and recording the
breach with `observed: manifest.sources.length` — the identical local, so
`sourcePopulation` and any recorded `maxSources` breach's `observed` are
always numerically identical in production by construction (confirmed in
Task 2). The `Math.max` is therefore currently vestigial for `maxSources`
specifically (unlike `maxBytesPerSource`, where the breach and the
ledger's own charged-body evidence are genuinely two different
measurements that can diverge). But AGENTS.md's rule 6 ("mutate the input
and confirm the check fails, per predicate") is exactly the discipline
that would have caught the confirmation-raw's `passes.size` bug earlier had
it been applied per-branch rather than per-limit — this fold is a real
`if`/`??` branch with no assertion pinned to it, and if a future change
decouples the two calls (a second call site, a reordering, a
population correction after a breach is recorded) the current "prefer the
max" behavior versus "prefer the declared population" behavior would
silently diverge with nothing to catch which one shipped. I recommend (not
require) a test pinning the combined case — e.g. `declareSourcePopulation(N)`
then `recordBreach({limit: 'maxSources', observed: M})` with `M > N`,
asserting the fold's chosen policy — before the next slice that touches
this file. This does not block CONFIRM on its own: no test in the PR's own
fixture is contradicted, no rendered value is wrong, and the identical gap
already existed, unflagged, for `maxBytesPerSource`'s equivalent fold
before this PR (its own combined-case test also only exercises
breach-with-nothing-charged, `resource-ledger.test.ts:319-326`), so this is
not a regression introduced by this repair — it is a pre-existing class of
gap this repair's own new fold-branch inherited.

## Task 6 — full battery

All run fresh in `.worktrees/pr81-conf2` after `npm ci`, tree clean before
and after:

- `npm test` — 134 files passed, 3 skipped; 1780 tests passed, 3 skipped, 0
  failed. Matches the bd comment's self-reported numbers.
- `npx tsc -b packages/three-surface-poc-core` — clean.
- `npx tsc --noEmit -p apps/three-surface-poc` — clean (run after the core
  build, per the AGENTS.md guardrail on stale `dist` declarations).
- `npm run build:poc` (`tsc -b --force` across all four packages) — clean.
- `python3 scripts/check_governance.py` — 32 OK, 20 WARN, 0 FAIL (52
  checks); all WARNs are the same pre-existing, default-path findings
  unrelated to `packages/three-surface-poc-core` (CG-22b, CG-23, CG-24,
  CG-25's three downgrades, CG-27's `decisions/README.md` prerequisite
  rows). Matches the bd comment's self-reported numbers.

## Observations (not exceptions)

- The "POPULATION's 15th entry" comment slip (Task 3) should be corrected
  to "13th entry" the next time either file is touched — purely
  descriptive, no test or code depends on the ordinal.
- `maxParsePassesPerSource`'s deliberate non-fold (Task 4) is correct but
  relies on a reader independently working out why it differs from the
  two sibling fold-in cases; a one-line comment there (mirroring the
  existing `maxBytesPerSource`/`maxSources` doc block's style) would save
  the next reviewer the trace.
- Scope stayed exactly the same four files as the prior confirmation
  (`git diff origin/main...HEAD --stat`): `resource-ledger.ts`,
  `resource-ledger.test.ts`, `project-shape-model.test.ts`,
  `project-shape-observation.ts`. No renderer or route reads
  `resourceUse`/`byLimit` yet (slices 3-4 remain untouched and out of
  scope), reconfirmed by grep.

## Commands run

```
cd /home/tze/GitHub/syzygy/.worktrees/pr81-conf2
git log --oneline -5; git status; git rev-parse HEAD
npm ci
bd show syzygy-u05.3
grep -n "VIS-2" .syzygy/governance/doctrine/vision.md
git diff 91b0cbe..eea5fb0 --stat
git diff 91b0cbe..eea5fb0 -- packages/three-surface-poc-core/src/resource-ledger.ts
git diff 91b0cbe..eea5fb0 -- packages/three-surface-poc-core/src/project-shape-observation.ts
git diff 91b0cbe..eea5fb0 -- packages/three-surface-poc-core/src/resource-ledger.test.ts packages/three-surface-poc-core/src/project-shape-model.test.ts
git diff origin/main...HEAD --stat
# traced observeProjectShapeSources / buildProjectShape control flow (Read)
# traced classifyManifestSources / project-shape-coverage.ts population identity (Read/grep)
grep -rn "resourceUse\|byLimit" apps/three-surface-poc/src/*.ts packages/three-surface-poc-core/src/*.ts
# rule-6 mutation 1: comment out ledger.declareSourcePopulation(...) call
npx vitest run packages/three-surface-poc-core/src/project-shape-model.test.ts
git checkout -- packages/three-surface-poc-core/src/project-shape-observation.ts
# rule-6 mutation 2: Math.max(sourcePopulation ?? 0, breach ?? 0) -> sourcePopulation ?? breach ?? 0
npx vitest run packages/three-surface-poc-core/src/resource-ledger.test.ts packages/three-surface-poc-core/src/project-shape-model.test.ts
npm test
git checkout -- packages/three-surface-poc-core/src/resource-ledger.ts
git status --porcelain   # empty
npx tsc -b packages/three-surface-poc-core
npx tsc --noEmit -p apps/three-surface-poc
npm run build:poc
python3 scripts/check_governance.py
npm test   # final confirmation on clean tree
```

## Verdict

**CONFIRM WITH EXCEPTIONS.**

- All three findings from the original review and the one finding from the
  first confirmation are resolved, independently re-derived here rather
  than trusted from the bd comment.
- `declareSourcePopulation` reports exactly the population the breach check
  compares against, provably by construction (not just for this PR's
  fixture), and is called on every path that can reach `ledger.summary()`
  — no path can leave it undeclared while reporting a known value as
  Unknown, and no path can report a stale value (Task 2).
- The new invariant test is real and its literals are hand-typed (Task 3).
- Re-examining all seven limits found the six already-settled ones sound,
  including confirming `maxParsePassesPerSource`'s asymmetric (non-folding)
  design is intentional and correct rather than an oversight (Task 4).
- My own rule-6 mutation on the `declareSourcePopulation` call site was
  caught precisely; a second mutation, on the `maxSources` `Math.max`
  fold-in, survived the entire test suite — a genuine but non-live gap
  (Exception above): the fold's "prefer the larger of declared population
  and breach" policy is currently unreachable-in-practice (the two are
  always equal in production) and untested for the case where they
  disagree, a pre-existing class of gap this repair's new branch inherited
  from the same fold pattern already used, unpinned, for
  `maxBytesPerSource`. Recommended, not required, before the next slice
  touching this file.
- Full battery green and matching the bd comment's self-reported numbers.
