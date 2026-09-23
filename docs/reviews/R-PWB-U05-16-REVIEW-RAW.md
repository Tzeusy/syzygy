# Review — Polaris generation admission validation (PR #90)
Reviewed commit: 95f37d65c0ab1197871ac9876f550987dd5004b5
Verdict: CONFIRM

## Scope

Bead syzygy-u05.16 asks `admitSourcePopulation` (`packages/polaris-generation-core/src/admitted-input.ts`)
to fail closed on the same `sourceId` handle pattern/length bound and `text`
upper bound that `provider-draft.ts`'s `sourceSchema` already enforces at
`validateStage` (i.e. on the provider's *reply*, after `pipeline.ts`'s
`stage()` has already sent the envelope to `ports.generate`), sharing one
definition rather than duplicating literals, with rule-6 tests. The diff
(`git diff origin/main...HEAD`) touches exactly the three files the bead
scoped: `provider-draft.ts` (+16/-2), `admitted-input.ts` (+28/-2, all
additive) and `admitted-input.test.ts` (+51). No other file changed.

## (1) Single shared definition, byte-equivalent to before

`provider-draft.ts` now exports `SOURCE_ID_PATTERN = '^[A-Za-z0-9][A-Za-z0-9_.:-]*$'`,
`SOURCE_ID_MIN_LENGTH = 1`, `SOURCE_ID_MAX_LENGTH = 100`,
`SOURCE_TEXT_MAX_LENGTH = 100_000`, and the two prior inline schema literals
now reference them:

- `handle` schema: `minLength: 1, maxLength: 100, pattern: '^[A-Za-z0-9][A-Za-z0-9_.:-]*$'`
  (before) → `minLength: SOURCE_ID_MIN_LENGTH, maxLength: SOURCE_ID_MAX_LENGTH,
  pattern: SOURCE_ID_PATTERN` (after). Values identical, confirmed by diff.
- `sourceSchema`'s `text` field: `maxLength: 100000` (before) → `maxLength:
  SOURCE_TEXT_MAX_LENGTH` (after, `= 100_000`, same numeric value, different
  literal notation only). `minLength: 1` is unchanged and was not extracted
  (not asked for; harmless).

`admitted-input.ts` imports all three (not `SOURCE_ID_MIN_LENGTH`, which it
does not need — see below) from `./provider-draft.js` rather than
duplicating them. One definition, one place these bytes can drift from.

`check()` (provider-draft.ts:52-57), the function `sourceSchema` runs
through, computes string bounds via `[...value].length` (code-point count)
against `minLength`/`maxLength`, and matches `pattern` via `new
RegExp(schema.pattern, 'u').test(value)`. `admitted-input.ts`'s new checks
use the identical counting method (`[...source.sourceId].length`,
`[...source.text].length`) and the identical `new RegExp(SOURCE_ID_PATTERN,
'u')` construction — same flag, same pattern string, same length semantics.
This is not merely "the same numbers", it is the same *comparison*, so no
divergent edge behavior (e.g. surrogate-pair counting) is possible between
the two call sites.

## (2) Boundary parity: admission rejects exactly what sourceSchema would

Read `check()` and `admitSourcePopulation` side by side: sourceSchema's
reject predicate for `sourceId` is `len<1 OR len>100 OR !pattern.test`;
admission's is `len===0 → empty-source-id` else `(len>100 OR
!pattern.test) → invalid-source-id`. Since `len===0 ⟺ len<1` for a
string, these are the same predicate split across two error codes, not two
different predicates. Same argument for `text` (`len<1 OR len>100000` vs
`len===0 → empty-text` else `len>100000 → text-too-long`).

I did not trust this by inspection alone. I drove `validateStage('inventory',
…)` (isolating the `sourceSchema` check on `context.sources` from the
value's own shape check by supplying a well-formed inventory envelope) and
`admitSourcePopulation` side by side over 18 probe cases in a throwaway
Vitest file (`packages/polaris-generation-core/src/_probe.test.ts`, written,
run, then deleted — worktree is clean; `git status --porcelain` empty):
id at the 100-char bound (accept) and 101 (reject); leading `_`/`-`/`.`/`:`
(all reject — the pattern's first-char class is `[A-Za-z0-9]` only);
trailing `_` (accept); embedded space, combining-accent character, newline,
empty id (all reject); all-allowed-punctuation id (accept); text at the
100,000-bound and one over; empty text; and, specifically to probe the
surrogate-pair edge the shared code-point counting is meant to handle
correctly, 100,000 U+1F600 emoji (200,000 UTF-16 code units, 100,000 code
points) — accepted by both — and 100,001 emoji — rejected by both. All 18
cases agreed between `admitSourcePopulation` and `validateStage`'s
`sourceSchema` check. No boundary mismatch found.

## (3) Excluded sources: unchecked is sound, verified in pipeline.ts

`admitSourcePopulation` only applies the new pattern/length checks to
`selected` sources; `excluded` sources are still only checked for
non-empty `sourceId`/`detail` and no cross-list duplicate id. I verified
this is sound, not merely assumed "never sent" from the docstring:

- `PipelineRequest` (`pipeline.ts:15-27`) has exactly one sources field —
  `readonly sources: readonly AdmittedSource[]` — and **no `excluded`
  field at all**. `SourcePopulation.excluded: readonly ExcludedSource[]`
  structurally cannot be assigned there; there is no field for it to travel
  through.
- `stage()` builds `context.sources = frozen.sources` (`pipeline.ts:201`,
  where `frozen` is a canonical-JSON round-trip snapshot of `request`), and
  the first-stage envelope's `inputs.sources` is `context.sources`
  (`pipeline.ts:312`). That envelope is what gets `encodeCanonicalJson`'d
  and handed to `ports.generate({ …, input: encoded, … })`
  (`pipeline.ts:250`). There is no other place `ports.generate` reads
  sources from.
- The one real caller building a `PipelineRequest`,
  `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts:41-46`,
  gets `sources` via `admittedSources(population)`, which (`admitted-input.ts:128-130`)
  returns `population.selected` and only `population.selected`.

So the soundness of "excluded is unchecked because it's never sent" rests
on `PipelineRequest`'s shape, not on caller discipline alone — a caller
would have to actively mislabel excluded material as an `AdmittedSource` to
smuggle it past this seam, which is a pre-existing type-contract property
outside this bead's scope (the bead is about pattern/length validation of
what's already labeled `selected`, not about defending against a
mislabeling caller).

## (4) Byte-identity of the pipeline demo output, origin/main vs HEAD

Added and removed a scratch worktree (`git worktree add --detach
<scratchpad>/pr90-base origin/main`, later `git worktree remove --force`;
not left behind — confirmed absent from `git worktree list` afterward).
`npm ci` in both the scratch base worktree (origin/main, `d3d5d9d`) and this
review worktree (HEAD, `95f37d6`), `npm run build:poc --silent` in both,
then `pipeline-demo-main.js --out <dir>` in both. `sha256sum` of the 7
output files (`archive.html/json`, `garden.html/json`,
`garden-changed.html/json`, `report.json`) is byte-identical file-for-file
between the two runs. No behavior change on the demo's valid synthetic
fixtures, as the PR description claims.

## (5) Rule-6 mutation

Mutated `admitted-input.ts:108` from `[...source.sourceId].length >
SOURCE_ID_MAX_LENGTH` to `>=` (an off-by-one on the accept/reject boundary)
and ran `admitted-input.test.ts`: the new boundary test ("accepts a
selected sourceId exactly at the handle length bound…") failed as expected
(`SourcePopulationError: invalid-source-id` on the 100-char case that
should be accepted); the other 12 tests in the file still passed. Reverted
from a saved copy; `git status --porcelain` and `git diff --stat` are both
empty afterward — worktree is byte-identical to the reviewed commit.

## (6) Full verification battery

- `npm test`: 134 files / 1784 tests passed, 3 skipped, **1 failed**:
  `apps/three-surface-poc/src/production-reobserve.test.ts` > "keeps served
  bytes and asOf stable when the same capture is rebuilt across wall-clock
  instants" timed out at 5000ms under full-suite parallel load. This file
  is untouched by the PR diff and unrelated to source admission. Re-ran it
  in isolation (`npx vitest run apps/three-surface-poc/src/production-reobserve.test.ts`):
  all 4 tests passed, including the one that had timed out, in 4.35s total.
  Pre-existing timing flakiness under load, not a regression from this PR.
- `npm run build:poc`: clean, no errors.
- `python3 scripts/check_governance.py`: **32 OK, 20 WARN, 0 FAIL (52
  checks)** — matches the count the PR description itself reports. No
  governance-prose files were touched by this diff; the WARNs are all
  pre-existing, unrelated report-only findings (CG-19b substrate pins,
  CG-22b allowlist, CG-23 vocabulary, CG-24 selftest coverage, CG-25
  downgrades, CG-27 default-path claims).

## Observations (not exceptions)

- Within the `selected` loop, the new `invalid-source-id`/`text-too-long`
  checks run *before* the pre-existing `duplicate-source-id` check. For a
  source that is both pattern-invalid (or over-length) *and* a duplicate,
  the thrown code is now `invalid-source-id` where before this PR it would
  have been `duplicate-source-id` (the old code had no pattern/length check
  at all, so only the duplicate check could fire). This is a sound
  fail-closed ordering — shape is checked before bookkeeping — and no
  existing test asserts the old precedence, but it's worth naming since it
  is a genuine (if inconsequential) change in which `SourcePopulationFailure`
  code a caller observes for that specific combined case.
- `admitted-input.test.ts`'s new tests hard-code `SOURCE_TEXT_UPPER_BOUND =
  100_000` and literal repeat counts (`100`, `101`) rather than importing
  `SOURCE_ID_MAX_LENGTH`/`SOURCE_TEXT_MAX_LENGTH` from `provider-draft.ts`,
  with an explicit comment explaining why ("the independent expectation…,
  not a tautology against the shared constant itself"). This is the same
  discipline AGENTS.md's conformance guardrail asks of `cap1-conformance`
  fixtures, applied here on the author's own initiative — good practice,
  worth calling out positively.
- The JSDoc additions in both files are accurate to the code as read (I
  checked each claim against the lines it describes, not just against
  itself) and correctly distinguish "this seam" from the still-open gap
  that `pipeline.ts`'s own `stage()` performs no shape check before
  `ports.generate` — that gap is closed by this PR at the admission front
  door, which is exactly the bead's ask.
