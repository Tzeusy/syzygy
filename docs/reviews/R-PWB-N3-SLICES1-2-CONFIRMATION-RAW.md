# Review — PWB N3 slices 1-2 confirmation (PR #81)
Reviewed commit: 91b0cbe3d4bdfd25c5f3f5fed88fe9e7f742fbc9
Verdict: REVISE

## Scope

Fresh-context confirmation review (CC-REV-4, CC-REV-6) of PR #81 (bead
syzygy-u05.3, N3 slices 1-2 only: "resource ledger summary headroom +
parse-pass margin guard"), at worktree `.worktrees/pr81-conf`, detached at
`91b0cbe`. Prior review at commit `8965020`
(`R-PWB-N3-SLICES1-2-REVIEW-RAW.md`) found REVISE on three findings. This
review dispositions those three, then applies the same scrutiny the prior
review used to every `ResourceLimitObservation` source per the dispatch
instructions, and independently found a fourth, new issue in the same
class the prior review targeted.

## Disposition of prior findings

**Finding 1 (false zero for 5 of 7 limits, contradicting VIS-2) — RESOLVED.**
`resource-ledger.ts` now returns a discriminated union
(`ResourceLimitObservation = {state:'observed', value} | {state:'unknown',
reason}`) from `summary()`'s `byLimit`. The two response ceilings
(`maxHumanResponseBytes`, `maxMachineResponseBytes`), which this ledger
never charges, now correctly report `state: 'unknown'` with a reason
naming `routes.ts`'s `boundedResponse` as the actual enforcement point,
instead of a false `0`. `maxSources` and `maxIndexDepth` are now wired to
real values instead of defaulting to `0`. Confirmed by reading the diff
`8965020..91b0cbe` and the updated `resource-ledger.test.ts` assertions,
and reproduced live in `project-shape-model.test.ts:904-915` (`state:
'unknown'` for both response ceilings, with the named reason).

**Finding 2 (`maxBytesPerSource` observed value ignored the populated
`bodies` map) — RESOLVED.** `observationFor`'s `maxBytesPerSource` case now
computes `Math.max(0, ...bodies.values())`, folding in the largest breach
observation only when a breach raised the number further. Confirmed
against the "resource envelope" fixture:
`about/heart-and-soul/v1.md` (342 bytes, the largest of the 14 charged
bodies) surfaces exactly as `byLimit.maxBytesPerSource.observed.value`
(`project-shape-model.test.ts:897`).

**Finding 3 (`maxIndexDepth` computed from an unused constant) —
RESOLVED**, see also the dedicated scrutiny below. `PWB_INDEX_DEPTH` is
now imported from `project-shape-manifest.ts` and wired into
`observationFor`'s `maxIndexDepth` case unconditionally.

**Observation from the prior review (mischaracterizing
`project-account-extraction` as a "future" pass identity in a mutation-test
comment) — RESOLVED.** The comment in `resource-ledger.test.ts` now reads
"an already-registered pass identity...newly applying to this source,"
matching the registry's actual state.

## Task 2 — scrutiny of every limit's `observed` source

**`maxTotalBytes`** — `state:'observed', value: totalBytesNow`, a running
cumulative sum of every charged body's bytes. Genuine observation, not
disputed.

**`maxParsePassesPerSource`** — `state:'observed', value:
maxPassesOnOneSource`, the max over the `passes` map. Genuine observation.

**`maxBytesPerSource`** — `Math.max(worstBodyBytes, breach ??
worstBodyBytes)` where `worstBodyBytes = Math.max(0, ...bodies.values())`.
Genuine observation over ledger-charged evidence, folding in a breach's
observed value only when a breach recorded something the ledger itself
never charged as highly (e.g. a source refused before every byte was
read). Sound.

**`maxIndexDepth`** — `state:'observed', value: PWB_INDEX_DEPTH`, a fixed
architectural constant (`project-shape-manifest.ts:45`, "Root index →
pillar index → named file", value `3`), independent of the declared limit
(`4`, `project-shape-observation.ts:79`). This is a genuinely known,
disclosed value, not a declared/configured value dressed up as observed —
it does not equal the declared limit, it is stamped unconditionally into
every manifest (`project-shape-manifest.ts:512`), and
`project-shape-observation.ts:544-545` already breaches on
`PWB_INDEX_DEPTH > limits.maxIndexDepth`, i.e. the pre-existing pipeline
already treats this constant as ground truth for the same comparison the
ledger now surfaces. Labeling it `'observed'` is honest **given what the
architecture actually guarantees**: unlike a traversal count, the pipeline
never partially walks the index — it is a fixed three-level shape by
construction, so "the constant" and "the depth actually reached" are the
same fact for every manifest this pipeline can produce. Not a Finding.
Worth an Observation (below) because the value is invariant regardless of
per-source read success or failure, which a future reader could mistake
for a per-run measurement.

**`maxSources`** — this is the one value that does **not** hold up under
the same scrutiny, and is a new Finding below.

## Finding — `maxSources`'s `observed` value undercounts `manifest.sources.length`, demonstrable within the PR's own fixture

`observationFor`'s `maxSources` case computes `Math.max(passes.size,
breach ?? passes.size)` — i.e., it reads the number of *distinct paths the
ledger charged at least one parse pass to*, folding in a breach value only
when a breach exceeded that count. But `passes.size` is not the quantity
the pipeline itself compares against the declared `maxSources` limit for
breach purposes: `project-shape-observation.ts:547-548` breaches on
`manifest.sources.length > limits.maxSources`, i.e. the full manifest
population, independent of whether each source was ever read.

These two populations structurally diverge for any source classified
`'derived'` (path-only) by `classifyManifestSources`
(`content-classification.ts:514-548`) — currently, exclusively the
`baseline-spec-tree` population rule (`openspec/specs/<dir>/spec.md`,
handled via `extractBaselineSpec` in `project-shape-extraction.ts:493-498`,
which reads only the path string, never Git content). For such sources,
`reader.read()` is never called and no `chargePass` is ever recorded, so
they are absent from `passes` — but they are still full members of
`manifest.sources`, and AGENTS.md records this as a standing production
condition ("Phase B classifies baseline specs path-only"), not a corner
case: every Butlers `openspec/specs/*/spec.md` entry is guaranteed present
in the real target repository.

This is demonstrable inside the PR's own test fixture without any new
test. `project-shape-model.test.ts`'s shared `POPULATION` fixture (lines
268-284) includes `openspec/specs/alpha/spec.md` as its 15th entry, and
`BASE_TEXTS` is built from it. Three separate assertions elsewhere in the
same file, against the identical `BASE_TEXTS` fixture, establish
`shape.counts.sources` (which traces to `manifest.sources.length` via
`project-shape-coverage.ts:580` and `project-shape-observation.ts:553`) is
**15** for this fixture (`project-shape-model.test.ts:454, 931, 949,
987`). Yet the PR's own "resource envelope" test, built from the same
`BASE_TEXTS` fixture (`build({ texts: BASE_TEXTS })`,
`project-shape-model.test.ts:865`), hand-types
`byLimit.maxSources.observed.value` as **14**
(`project-shape-model.test.ts:896`) — exactly one less, exactly the count
of the `openspec/specs/alpha/spec.md` source the ledger never charged a
pass to. `remaining` is correspondingly overstated by 1 (`498` instead of
`497` against the declared `512`).

No test in the PR asserts `byLimit.maxSources.observed.value ===
shape.counts.sources` (or `manifest.sources.length`), so this
self-contradiction inside the PR's own fixture went unnoticed — the same
failure mode (an easily-checked invariant between two fields of the same
`ProjectShape`, silently violated) that produced the prior review's
Finding 1. The magnitude here is a fixed off-by-one only in this small
fixture; in the real Butlers repository, where the `baseline-spec-tree`
population rule applies to every OpenSpec change directory, the gap scales
with however many such directories exist, silently understating
`maxSources` usage (and overstating `remaining`) by that count every time.
This is a VIS-2-relevant accuracy defect in exactly the metric this slice
exists to make honest, for a source category the architecture guarantees
is present, not a hypothetical edge case.

Suggested repair direction (not prescriptive): `maxSources`'s `observed`
should read `manifest.sources.length` (or an equivalent full-population
count already available to `summary()`'s caller) rather than
`passes.size`, mirroring how `project-shape-observation.ts` itself
evaluates the breach. If `summary()` has no access to the manifest length
today, that is itself worth surfacing rather than substituting the
smaller, ledger-local proxy.

## Task 3 — discriminated-union consumer safety

Grepped every call site of `summary()` and every reference to
`resourceUse`/`byLimit` outside the ledger and its own tests:
`project-shape-model.ts:641` is the only production consumer
(`resourceUse: ledger.summary()`, stored verbatim onto `ProjectShape`).
No renderer, route, or JSON-serialization path reads `resourceUse` or
`byLimit` yet — slices 3-4 (rendering) are untouched by this PR and remain
out of scope, confirmed by `git diff origin/main...HEAD --stat` showing
only `resource-ledger.ts`, `resource-ledger.test.ts`, and
`project-shape-model.test.ts` changed. No coercion or silent narrowing
risk exists today because nothing downstream yet reads the new shape.

## Task 4 — own rule-6 mutation

Mutated `remainingFor`'s `unknown`-branch in `resource-ledger.ts` to
`{ state: 'observed', value: 0 }` (replacing the pass-through of
`observed.reason`). Ran `npm test`: exactly 2 test files failed, both
failing only on the mutated field (the two response-ceiling `remaining`
assertions in `project-shape-model.test.ts` and `resource-ledger.test.ts`
expecting `state:'unknown'`), no unrelated failures. Reverted with `git
checkout --`; `git status --porcelain` confirmed clean before proceeding.

## Task 5 — full battery

All green, in the worktree after `npm ci`:
- `npm test` — 134 files / 1779 tests passed.
- `tsc -b packages/three-surface-poc-core` — clean.
- `tsc --noEmit -p apps/three-surface-poc` — clean (run after the core
  build per the AGENTS.md guardrail on stale `dist` declarations).
- `npm run build:poc` — clean.
- `python3 scripts/check_governance.py` — 32 OK / 20 WARN / 0 FAIL.

These numbers match the bd comment's self-reported results.

## Observations (not exceptions)

- `maxIndexDepth`'s `observed` value is invariant regardless of whether
  the index was actually walked to completion or a source lower in the
  tree was refused/excluded first — it reflects the architecture's fixed
  shape, not a per-run traversal measurement. This is honest given the
  architecture (see scrutiny above) but is easy for a future reader to
  mistake for a measured depth; a one-line comment already partially
  covers this (`resource-ledger.ts`'s `maxIndexDepth` case comment,
  pre-existing) but does not say it is architecture-invariant rather than
  run-invariant.
- The `remainingFor` helper is a clean, minimal translation
  (`observed.state === 'observed' ? {...declared-observed} :
  {...observed.reason}`) and was the exact site my rule-6 mutation
  targeted with a clean catch.

## Commands run

```
npm ci
npm test
npx tsc -b packages/three-surface-poc-core
npx tsc --noEmit -p apps/three-surface-poc
npm run build:poc
python3 scripts/check_governance.py
git diff 8965020..91b0cbe
git diff origin/main...HEAD --stat
git status --porcelain   # before and after the rule-6 mutation/revert
git ls-remote origin 'review/*'   # duplicate-dispatch check
```

## Verdict

**REVISE.** The three findings from the prior review are cleanly resolved,
the discriminated union is consumer-safe (nothing downstream reads it
yet), my own rule-6 mutation was caught precisely, and the full battery is
green. But the dispatch instructions' explicit direction to scrutinize
every limit's `observed` source the same way the prior review scrutinized
the first five surfaced a new, code-verified and fixture-demonstrable
issue in the same doctrine-relevant class as the resolved findings:
`maxSources`'s `observed` value (`passes.size`) diverges from
`manifest.sources.length` — the actual quantity the pipeline compares
against the declared limit — for any source the pipeline classifies
path-only (currently `baseline-spec-tree`, a population rule guaranteed
present in the real target repository). This is demonstrable today inside
the PR's own `BASE_TEXTS` fixture: `shape.counts.sources` is 15
(`project-shape-model.test.ts:454,931,949,987`) while the PR's own
"resource envelope" test hand-types `byLimit.maxSources.observed.value`
as 14 for the identical fixture (`project-shape-model.test.ts:896`).
