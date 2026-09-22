# Review — PWB N8 slice 3 (PR #86)
Reviewed commit: eaa27a8b18bc45edec94f9c14e272acef6c39aa7
Verdict: CONFIRM

## Commission

Fresh-context independent review (CC-REV-1, CC-REV-4, CC-REV-6) of PR #86,
implementing bead syzygy-u05.8 (N8) slice 3: "admitted-input.ts +
SourcePopulation port; generator front door consumes it (relates
syzygy-mea, REQ-polaris-generation-030/031)". Reviewed in a dedicated
worktree (`/home/tze/GitHub/syzygy/.worktrees/pr86-review`, detached at
`eaa27a8b18bc45edec94f9c14e272acef6c39aa7`), no tracked files edited or
committed, nothing pushed or merged. `bd show syzygy-u05.8` and `bd show
syzygy-mea` read for criteria; `git ls-remote origin 'review/*'` and a
filename sweep found no prior raw for this PR/commit, so this is a first
review, not a duplicate dispatch.

Diff reviewed: `git diff origin/main...HEAD` — 6 files, +232/-5:
`packages/polaris-generation-core/src/{admitted-input.ts (new),
admitted-input.test.ts (new), index.ts, pipeline.ts, pipeline.test.ts}`,
`apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts`.

## Findings

No findings. Every claim in the bead comment and PR body was independently
re-derived; none needed correction.

## Checks performed, with independent re-derivation

**(1) REQ-030 non-selection vocabulary.** Located
`REQ-polaris-generation-030` ("Accounted unfamiliar-project discovery") at
`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md:531`
(DIRECTIVE-REGISTER.md does not index openspec spec-clause IDs — it covers
only the five governed trees named in AGENTS.md's authority table — so the
brief's grep-openspec fallback was used). Its governing "Accounted
unfamiliar-project discovery" requirement text (lines immediately above,
529) reads: "Before claiming source coverage it SHALL expose the selected
project boundary and audience, admitted source classes, supported
languages/source forms/repository shapes and scale bounds, inspected and
selected material, and **reasons relevant material is excluded,
unavailable, unresolved or deferred by budget**." `admitted-input.ts:37`
defines `SourceExclusionReason = 'excluded' | 'unavailable' | 'unresolved'
| 'deferred-by-budget'` — the same four reasons, in the same order, with
"deferred by budget" folded into one hyphenated token (a normal
prose→identifier transliteration, not a semantic change). No invented
fifth reason, no dropped reason, no reworded reason. The doc comment at
`admitted-input.ts:4-13,34-36` quotes the clause verbatim and cites the
exact file:line. `REQ-polaris-generation-031` ("Purpose beyond mechanics")
is named in the bead/PR title's "relates ... REQ-030/031" but is not
implemented by this slice's code (source-admission accounting is REQ-030's
concern; REQ-031 governs a separate purpose-question flow) — the code
comments correctly cite only REQ-030 and make no REQ-031 implementation
claim, so there is nothing to hold the diff to on REQ-031 here.

**(2) Byte-identity, reproduced independently.** Added a scratch worktree
at `origin/main` (`9712619`), ran `npm ci` + `npm run build:poc` in both
that worktree and the PR worktree (both clean), then ran
`node apps/three-surface-poc/dist/polaris-generation/pipeline-demo-main.js
--out <dir>` in each, producing 7 files (`garden.html/json`,
`archive.html/json`, `garden-changed.html/json`, `report.json`) at both
commits. `diff -rq <base-out> <head-out>` reported zero differences;
`sha256sum` over all 7 files at each commit matched exactly, e.g.
`garden.html` = `34df9c35aaf961699f10e4319ec075803c3d2220621592aeadbb0106b804c76b`
identically at both commits (all 7 pairs matched; full checksums retained
in the session scratchpad). This is expected from reading the diff:
`admitSourcePopulation([...]).selected` returns the exact array reference
passed in (no clone, no reorder), so `pipeline-demo.ts`'s new
`admittedSources(admitSourcePopulation([...]))` call yields the identical
object graph the old bare array literal did. Base worktree removed after
use (`git worktree remove --force`).

**(3) Does narrowing `sources: unknown` → `readonly AdmittedSource[]`
remove runtime validation?** No. Read `provider-draft.ts:107-111`:
`validateStage` unconditionally runs `check(sourceSchema, context.sources)`
on every stage call (`sourceSchema` requires each entry to satisfy the
`handle` pattern on `sourceId` and 1-100000 length `text`), then
`unique(...)` over `sourceId`s (throws `duplicate-handle` on any repeat).
This check is a separate, independent runtime function that does not read
or depend on the TypeScript type of `PipelineRequest.sources` at all —
JS erases the static type at runtime regardless of whether the field was
declared `unknown` or `readonly AdmittedSource[]`, so the type change by
itself changes nothing here. `pipeline.ts:174`'s
`JSON.parse(encodeCanonicalJson(request, ...))` round-trip (byte/node/depth
limits only, no shape schema) is also unchanged behavior, present before
and after this diff. `admitSourcePopulation` itself independently
re-validates non-empty `sourceId`/`text` and cross-list duplicate freedom
before a population is ever built (`admitted-input.ts:83-96`) — this is an
*added* validation layer at the front door, not a replacement for
`validateStage`'s own. Net: two independent runtime checks now guard
`sources`, neither removed, and both pre-existing behavior except the new
`admitSourcePopulation` addition.

**(4) Stays inside the syzygy-mea limit?** Yes. `syzygy-mea`'s limit is
"Existing generator candidate must be reconciled and adopted before new
observable implementation; current PWB consent does not authorize
second-project reads or provider egress." Read `admitted-input.ts` in
full: no filesystem, network, or process I/O of any kind — every exported
function (`admitSourcePopulation`, `admittedSources`,
`sourcePopulationDenominator`) is a pure, synchronous, total function over
its arguments. The one behavioral call-site change
(`pipeline-demo.ts`) routes the same synthetic, already-hard-coded fixture
data through the new functions; per (2) above the output is byte-identical,
so "nothing about what is admitted changed" is independently confirmed,
not just asserted. `git diff --stat` confirms `model.ts`, `routes.ts`,
`polaris.ts` and everything under `.syzygy/**`/`openspec/**` are untouched.

**(5) Test quality.** `admitted-input.test.ts`'s 9 tests use literal
expected values throughout (hard-coded `selected`/`excluded` fixture
arrays and `toEqual`/`toBe` against literals or straightforward arithmetic
on their `.length`s — never re-deriving an expectation from the module
under test). Coverage includes: selected-only and mixed populations;
projection returns exactly and only `selected`, in order, with an explicit
assertion that no excluded id leaks into it; within-selected duplicate,
cross-list duplicate, empty-`sourceId` (both lists), empty-`text`, and
empty-`detail` rejections; and a table asserting the *exact* failure code
per rejection kind (guards against silently returning the wrong code).
Ran my own rule-6 mutation independent of the one recorded in the PR body
(which disabled the duplicate check): commented out the `empty-text` guard
in `admitSourcePopulation` (`admitted-input.ts:86`). Result: 2/9 tests
failed as expected (`rejects an empty text on a selected source`, `reports
the exact failure code for each rejection kind`, the latter showing
`empty-text: undefined` where `empty-text` was expected) — confirming the
test suite is not vacuously passing. Reverted via the pre-edit backup;
`git status --short` on the file is empty (byte-identical to HEAD) and all
9 tests pass again. Separately verified `pipeline.test.ts`'s `id` →
`sourceId` fixture rename (the only other test file changed) is a
compile-time-only fix: that file's `harness().ports.validate` is a stub
that never inspects field names, so the rename has no bearing on that
test's actual assertions — it exists only because the fixture literal must
now satisfy `AdmittedSource`'s structural type.

**(6) Full verification battery**, run in the PR worktree at
`eaa27a8b18bc45edec94f9c14e272acef6c39aa7`:
- `npm test` → 135 test files passed, 3 skipped, 1781 tests passed, 0
  failed (matches the PR body's reported count).
- `npm run build:poc` (`tsc -b --force` across `cap1-core`, `cap1-daemon`,
  `three-surface-poc-core`, `apps/three-surface-poc`) → clean, no output.
- `npx tsc -b packages/polaris-generation-core --force` and `npx tsc
  --noEmit -p apps/three-surface-poc` → both clean (ran the core build
  first per the AGENTS.md `dist`-declaration gotcha, so the app typecheck
  isn't reporting phantom errors).
- `python3 scripts/check_governance.py` → 32 OK, 20 WARN, 0 FAIL — all 20
  WARNs are pre-existing governance-prose items (CG-22b, CG-23, CG-24,
  CG-25, CG-27) unrelated to this implementation-plane diff; matches the
  PR body's reported count exactly.

## Observations (not exceptions)

- `ExcludedSource.reason` can literally hold the value `'excluded'`
  (i.e., a record inside the `excluded` array whose own `reason` field
  reads `'excluded'`), which reads redundantly at first glance. This is a
  faithful, unavoidable consequence of REQ-030's own wording listing
  "excluded" as one of its four named reasons alongside "unavailable",
  "unresolved" and "deferred by budget" — not a defect in the port.
- `admitSourcePopulation`'s own field-level checks (non-empty `sourceId`,
  1-char-minimum `text`) are lighter than `provider-draft.ts`'s
  `sourceSchema` (which also enforces the `handle` regex pattern on
  `sourceId` and an upper bound on `text` length). This means a
  caller-supplied `sourceId` containing e.g. whitespace would pass
  `admitSourcePopulation` and only be rejected later, inside
  `validateStage`, which — as today's architecture already has it, before
  and unchanged by this diff — runs on the provider's *reply*, after the
  envelope containing that `sourceId` has already been sent via
  `ports.generate`. This is pre-existing pipeline behavior, not introduced
  or worsened by this slice (verified: `pipeline.ts`'s `stage()` sends
  `envelope` via `ports.generate` before `ports.validate` is ever called on
  the reply, identically at `origin/main`). Worth a note for whichever
  future slice builds the real discovery behavior REQ-030 describes: if a
  front door ever assembles `sourceId`s from anything other than
  hand-written fixtures, validating the full `handle` pattern before first
  send (not only before accepting the reply) would close that gap.
- The PR title/bead text's "relates ... REQ-030/031" is inherited framing
  from the bead's slice-3 design line, not a claim this diff implements
  REQ-031; worth keeping in mind only so a later reader doesn't mistake the
  bead cross-reference for an implementation claim about REQ-031's own
  scenarios (purpose-question flow), which this slice does not touch.

## Commands run

```
cd /home/tze/GitHub/syzygy/.worktrees/pr86-review && npm ci
bd show syzygy-u05.8
bd show syzygy-mea
grep -n "REQ-030\|REQ-031" DIRECTIVE-REGISTER.md   # (repo root; empty)
grep -rln "REQ-030\|REQ-031" openspec/changes/
sed -n '500,620p' openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md
git diff origin/main...HEAD --stat
git worktree add <scratch>/base-main origin/main --detach
(cd <scratch>/base-main && npm ci && npm run build:poc)
(cd .worktrees/pr86-review && npm run build:poc)
node apps/three-surface-poc/dist/polaris-generation/pipeline-demo-main.js --out <scratch>/out-main   # from base-main
node apps/three-surface-poc/dist/polaris-generation/pipeline-demo-main.js --out <scratch>/out-head   # from pr86-review
diff -rq <scratch>/out-main <scratch>/out-head
sha256sum <scratch>/out-main/* ; sha256sum <scratch>/out-head/*
git worktree remove <scratch>/base-main --force
# rule-6 mutation
cp admitted-input.ts admitted-input.ts.bak
# edit: comment out `if (source.text.length === 0) throw ... 'empty-text'`
npx vitest run packages/polaris-generation-core/src/admitted-input.test.ts   # 2/9 failed
cp admitted-input.ts.bak admitted-input.ts               # revert
npx vitest run packages/polaris-generation-core/src/admitted-input.test.ts   # 9/9 passed
git status --short packages/polaris-generation-core/src/admitted-input.ts   # empty
npm test
npm run build:poc
npx tsc -b packages/polaris-generation-core --force
npx tsc --noEmit -p apps/three-surface-poc
python3 scripts/check_governance.py
git ls-remote origin 'review/*'
```
