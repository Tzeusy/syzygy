# R-PWB-N8-SLICE4 review — PR #95 at 1f92432

Verdict: CONFIRM

## Scope and setup

- `git fetch origin` (193de50..1482b68 main -> origin/main).
- `git worktree add .../rev95 1f92432ed930d8982d583dca5de9acd7ad5ab010`; `npm ci` (113 packages, 0 errors, only pre-existing npm audit advisories).
- Artifact: `git diff origin/main...1f92432ed930d8982d583dca5de9acd7ad5ab010 --stat`:
  ```
   .../src/governance-inputs.test.ts | 38 +++++++++++++++-
   apps/three-surface-poc/src/governance-inputs.ts | 50 ++++++++++++++++++++--
   2 files changed, 84 insertions(+), 4 deletions(-)
  ```
  Only `governance-inputs.ts` and `governance-inputs.test.ts` change. Confirms (f) directly: `model.ts`, `polaris.ts`, `routes.ts`, `project-shape-extraction.ts`, `project-shape-manifest.ts` are byte-untouched (`git diff` over each is empty; separately confirmed `git-observation.ts` is empty-diff too).

- `bd show syzygy-u05.8`: slice 4 is the last of N8's four slices. The bead's slice-4 pre-check comment (2026-09-23 00:08) records the reconciliation with `syzygy-u2a.7` (open, unrelated CAP1 subsystem, no locator to reuse) and recommends exactly the "smallest step" this PR implements: turn the single `BodyReadAuthorityExpectations` object into a project-keyed lookup with one entry, fail closed on an unknown project, leave `PWB_APPROVED_REPOSITORY_LOCATOR` as the sole locator, add no second project/repository/consent. The PR's own bd comment (00:17) matches this design 1:1.

## (a) Pure refactor, exactly one entry, no new locator/read/egress

`governance-inputs.ts` diff:
- Old `pwbAuthorityExpectations` body (the literal `BodyReadAuthorityExpectations` object) is renamed to a private function `pwbSyzygyButlersExpectations` with **byte-identical contents** — diffed the object body lines directly (`sed` extract of the object literal from both `origin/main` and `1f92432`, `diff` shows the differing lines are only the surrounding comments/function name, none inside the object literal).
- New: `PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT: ReadonlyMap<string, ...>` constructed as `new Map([[PWB_OBSERVING_PROJECT, pwbSyzygyButlersExpectations]])` — literally one entry, keyed by the pre-existing `'project:syzygy'` string (now named `PWB_OBSERVING_PROJECT`).
- `pwbAuthorityExpectationsForProject(observingProject, evaluationInstant)` looks the builder up in the map and calls it; `pwbAuthorityExpectations` becomes a one-line back-compat wrapper calling it with `PWB_OBSERVING_PROJECT`.
- No new repository locator, no new consent/policy/registry artifact path, no network/egress code anywhere in the diff. `PWB_APPROVED_REPOSITORY_LOCATOR` (`git-observation.ts:6`) is untouched (confirmed empty diff on that file).

This is a pure refactor with exactly one entry, matching (a).

## (b) Fail-closed for an unknown project, every path checked

Traced every path into the lookup:
- `pwbAuthorityExpectationsForProject`: `PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT.get(observingProject)`; if `undefined`, throws `no body-read authority expectations are registered for observing project "<id>"`. No fallback branch exists in the source.
- `pwbAuthorityExpectations` (back-compat wrapper): always calls the keyed resolver with the constant `PWB_OBSERVING_PROJECT` — cannot be used to smuggle an arbitrary id.
- `loadBodyReadAuthorityInputs`'s new optional `observingProject` field: `options.observingProject ?? PWB_OBSERVING_PROJECT` is computed at line 356, **before** the `load` closure that does any artifact/record read (`readArtifact`/`readOptionalText`/`lifecycleFor` all live inside `load`, invoked afterward at line 377). An unregistered id throws before any I/O — zero reads happen on the failing path, not just zero authority.
- Grepped every call site of `loadBodyReadAuthorityInputs` in the app (`production-reobserve.ts` is the only production caller in this worktree's `main.ts`, which delegates to it; `project-shape-discovery.live.test.ts` and `governance-inputs.test.ts` are the only others). None passes a user- or CLI/env-derived value for `observingProject`; `grep -rn "process.env\|process.argv"` in `main.ts`/`production-reobserve.ts`/`cli.ts` shows no project-related env/argv plumbing. So today, no caller can pass an arbitrary id at all — the option exists on the type but nothing outside the tests exercises it with anything other than the default.
- The one real caller (`production-reobserve.ts`) wraps the whole `evaluateBodyReadAuthority(loadBodyReadAuthorityInputs(...))` call in try/catch, converting any thrown error (including this new one) into `projectShapeDetail` with `projectShape` left `undefined`, i.e. `not-evaluated`/Unknown — never a synthesized admit. This is the pre-existing idiom for every other failure mode this loader already throws for (invalid governance revision, path escaping repo root, lifecycle enumeration failure, vanished record — `governance-inputs.ts:186,192,279,288`).

So: could a caller pass an arbitrary id and get authority? No — every path either hits the map (one key) or throws before any read; there is no default/fallback branch that returns borrowed or synthetic authority.

## (c) Butlers behavior and served bytes unchanged

- `pwbSyzygyButlersExpectations`'s returned object is byte-identical to the pre-refactor `pwbAuthorityExpectations`'s object (see (a)).
- Full `npm test` run (below) is green including `production-reobserve.test.ts`'s byte-stability assertions over capture→authority→project-shape-model, `page-size-delta.test.ts` (delta measurement unaffected), `cross-cutting.test.ts`, and the real-Syzygy-governance-tree test in `governance-inputs.test.ts`.

## (d) Tests: hard-coded literals, fixtures outside describe time

New `describe('pwbAuthorityExpectationsForProject ...')` block, 4 new tests:
- Assertions against the module use hard-coded literals (`'project:syzygy'`, `'repository:butlers-configured-poc'`, and the exact regex on the thrown message) — not values imported from the module under test. `PWB_OBSERVING_PROJECT` (imported from `governance-inputs.ts`) is used only as an **input** to `pwbAuthorityExpectationsForProject`/`loaderFor` (the well-known registered key a caller would pass), never as the expected value being asserted — no circularity.
- `keyed` vs `legacy` (`toEqual`) is a cross-check between two outputs of the same module (old vs new API surface), which is a legitimate equivalence/back-compat check, not a substitute for the literal checks that follow it in the same test.
- `fakeTree()` is called inside each `it()` body (not at `describe`/module scope), consistent with the rest of the file and avoiding the "fixture built at describe time" trap.

## (e) Rule 6 — mutate the fail-closed branch myself

Backed up `governance-inputs.ts`, then mutated the resolver to fall back to the map's first entry instead of throwing:
```ts
const build = PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT.get(observingProject) ?? PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT.values().next().value;
```
Ran `npx vitest run apps/three-surface-poc/src/governance-inputs.test.ts`:
```
× fails closed for an unknown observing project: no default fallback to Butlers
  → expected [Function] to throw an error
× propagates the fail-closed error through loadBodyReadAuthorityInputs for an unregistered project
  → expected [Function] to throw an error
Test Files  1 failed (1)
     Tests  2 failed | 19 passed (21)
```
Both fail-closed tests failed as expected; the other 19 (including the "resolves default the same as explicit" test, since the mutation is a no-op when the id *is* registered) stayed green. Reverted via `cp` from the backup; `diff` against the backup: `IDENTICAL`; re-ran the same test file: `21 tests passed`.

## (g) Build and test battery

- `npx tsc -b packages/three-surface-poc-core packages/polaris-generation-core` — clean, no output.
- `npx tsc --noEmit -p apps/three-surface-poc` — **initially failed** with `Cannot find module '@syzygy/cap1-daemon'` across many files (not this PR's files) because `packages/cap1-core`/`packages/cap1-daemon` had no `dist/` yet in the fresh worktree (per AGENTS.md's "App typecheck resolves core through dist declarations" note, extended here to cap1-daemon too). After `npx tsc -b packages/cap1-core packages/cap1-daemon`, `tsc --noEmit -p apps/three-surface-poc` is clean. Not a defect in this PR — an artifact of a fresh worktree needing its dependency packages built first.
- `npx vitest run apps/three-surface-poc/src/governance-inputs.test.ts` — 21/21 passed (17 pre-existing + 4 new).
- `npm test` (full suite): **135 passed | 3 skipped (138 files), 1801 passed | 3 skipped (1804 tests), 0 failed**, 38.6s. `production-reobserve.test.ts` (the test flagged as having a known load-timeout) passed cleanly in this run (4 tests, ~10s) — no re-run needed.
- `python3 scripts/check_governance.py` — **32 OK, 20 WARN (all pre-existing governance-prose findings unrelated to this diff, e.g. `PENDING-OWNER-DECISIONS.md` prerequisite-claim warnings), 0 FAIL.**

All match or exceed the PR author's own reported numbers (their run had 1 flaky timeout under full-suite load; mine had 0).

## Design judgment: throw vs. Unknown/refused return

Throwing is the right polarity here, for three independent reasons:

1. **Type shape forces it.** `BodyReadAuthorityExpectations` (`body-read-authority.ts:243-256`) is a fully-populated, non-nullable struct with no `Unknown`/absent variant, and every comparison against it downstream (`expectations.observingProject`, `expectations.authorities[kind]`, etc., used directly with no null-guards throughout `body-read-authority.ts` and `walkthrough-judgment.ts`) assumes it exists. Returning a sentinel "unknown expectations" value would require inventing a new variant and threading null-checks through every comparison site — a much larger, riskier change for a "pure refactor" slice.
2. **It matches the file's existing idiom exactly.** `governance-inputs.ts` already throws for structurally similar situations — invalid governance revision (`:186`), a path escaping the repo root (`:192`), lifecycle enumeration failure (`:279`), a vanished lifecycle record (`:288`) — and both real callers (`production-reobserve.ts`, and this worktree's `main.ts` via it) already wrap `evaluateBodyReadAuthority(loadBodyReadAuthorityInputs(...))` in one try/catch that turns *any* thrown failure into `not-evaluated` (Unknown, failure named), never a synthetic admit or reject. Adding a second failure-signaling mechanism (a return-value refusal) alongside the existing throw-based one would fragment that handling for no benefit.
3. **It fails before any I/O**, which is stronger than "fails closed" alone would require — an unregistered project causes zero reads of the governance tree, not just an unauthorized read result.

The one soft observation: `LoadGovernanceInputsOptions.observingProject` is public API surface that no real caller currently drives from outside (no CLI flag, no env var), so its fail-closed behavior is presently exercised only by tests. That's expected for a slice whose own bead explicitly scopes out building a second project or a new locator — the seam is deliberately inert until a second project is authorized, and the reconciliation comment on the bead documents that this is intentional, not an oversight. Nothing in this PR forecloses adding proper caller wiring later, and the current unreachability doesn't weaken the fail-closed guarantee since the only paths that exist all resolve to the single registered project.

## Verdict rationale

All acceptance criteria (a)-(g) are met, verified independently rather than by re-reading the PR's own claims: exact-diff scope, byte-identical Butlers object, fail-closed-before-I/O tracing across every call path, hard-coded test literals, a self-performed rule-6 mutation-and-revert, and a from-scratch build/test/governance-check battery all green. The design (throw, not a returned Unknown/refused value) is the correct choice given the non-nullable expectations type and the file's existing try/catch idiom at both call sites.

**Verdict: CONFIRM.**
