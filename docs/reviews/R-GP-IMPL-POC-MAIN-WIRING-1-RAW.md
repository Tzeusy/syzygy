# R-GP-IMPL-POC-MAIN-WIRING-1 — CC-REV-1 implementation review of syzygy-bpyt.5.8, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: fe46265d
Subject: r1-review.diff sha256 fedee71fede54ca972abc2b52a53c69e0d6a9fe6abc361277563d5b2e936c861

- Reviewer: an independent CC-REV-1 reviewer with fresh context. I did not author the change. Date 2026-10-22.
- PR: #507, branch `agent/syzygy-bpyt.5.8`.
  - Full head: `fe46265da86ad62f90ca92c2a360d6e2b72fb7c1`.
  - Base: `0d4d50984f6aa501217fe7109b6aec1b9679e4c9`.
- Constraints kept:
  - No target repository content was fetched or read. Every probe used fixture repositories that I created in my scratch directory.
  - I opened no credential file.
  - I ran no bd mutation and made no push, PR comment or merge. I killed no process.
  - I edited nothing under `/home/tze/GitHub/syzygy`. The two clones were made with `git clone` from it, and I ran read-only `git show`, `git grep`, `git cat-file` and `bd show`/`bd comments`.
  - Every mutant edit was made in a scratch clone and restored byte for byte. `git status --porcelain` printed nothing on both clones before they were deleted.

## 1. Subject identity checks

| Check | Result |
|---|---|
| sha256 of the subject file | [Observed] `fedee71fede54ca972abc2b52a53c69e0d6a9fe6abc361277563d5b2e936c861`. **Matches the brief.** |
| `git diff 0d4d5098 fe46265d`, re-derived by script | [Observed] Same sha256 as the subject file. 26 files: 2 code files and 24 under `docs/evidence/poc-main-wiring-2026-10-22/`. |
| `git diff 5837512f adefdc3c` (the lane's own diff: lane base to its evidence commit) | [Observed] Same sha256 again, so the merge adds no bytes to the lane's diff. |
| `git merge-tree --write-tree adefdc3c 0d4d5098` | [Observed] `06044c0634c46a9d109ef2a60e973910b62bc713`, equal to `git rev-parse fe46265d^{tree}`. The merge commit is git's clean automatic merge; no byte in it was resolved by hand. |
| Files touched by each side since the lane base `5837512f` | [Observed] The lane touches 26 files. Main touches 50 files over 28 commits (`git rev-list --count 5837512f..0d4d5098` = 28). Overlap: 0. Main files under `apps/`: 0. Main does change `packages/three-surface-poc-core/src/*` (9 files) and the polaris-dossier tests. |
| **Conclusion on the merge** | [Observed] The merge brought only main's bytes. |
| Commit chain | [Observed] `25aa1ac8` adds the tests and the seam. It is the only lane commit that touches `poc-main.ts` (`git log 5837512f..e8cb47d5 -- poc-main.ts`). `e8cb47d5` adds the explicit `started()` test timeouts, `adefdc3c` adds the evidence, and `fe46265d` merges main `0d4d5098`. |
| Code-file digests at the reviewed commit | [Observed] At `fe46265d`, `poc-main.ts` hashes to `e09e8f203a186b41b2b5ba554fa2fc7f7018a02d7ca85085bff273ba7617bdc0` and `main.test.ts` to `1c9a992991cd200e18659fc0da170aae35b05e3de9eda29e34619e7d2fb382ab`. Both equal the `sha256AtCommit` values the lane's head mutant record gives for `e8cb47d5`. |
| Code-file digests at base | [Observed] At `0d4d5098` the two files hash to `c5e5dc78cd9107d0e99dc39e32a6d7e4bfa493d527f76bdb26e17f94fe9337c1` and `55bc26ce4643d35ed8c1f7f5c378f1ca4054953f6a93d726df0ce313c0472e8b`. Both equal the base record's values for `5837512f`. |
| PR state | [Observed] `gh pr view 507`: `"headRefOid":"fe46265da86ad62f90ca92c2a360d6e2b72fb7c1"`, `"state":"OPEN"`, `"mergeable":"MERGEABLE"`. |

## 2. Clauses relied on (quoted, rule 8)

### CC-REV-1

From `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:

- "Changes touching any of seven classes require review by an independent, fresh-context reviewer, and the agent performing the change never finally decides which classes it touches."
- "1. **authority boundaries** — write-universe, typed-authority table, adapter authorization (VIS-5, VIS-6);"
- "3. **deterministic observation** — snapshot composition, evaluation identity, the deterministic/inferred seam (VIS-7);"
- "**A reviewer or the owner** may reclassify at any time."

I keep classes 1 and 3 [Inferred]:

- Class 1: the new seam makes the factory for the human materialize action injectable. That action writes a Bead into the observed repository's tracker (`materialize-action.ts`, `MATERIALIZE_ATTRIBUTION`).
- Class 3: the tests pin the `PocRuntimeCapture` composition, the clock and the horizon root.

I add no class:

- `PocMainDeps` is a test-seam type that only tests construct. It is not a machine-queryable endpoint or adapter contract, so class 6 does not apply.

### Owner direction GP-Q0

From `.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`. Part 1:

- "\"Behavior-preserving\" means none of the following changes: a rendered byte, a wire format, a refusal string or an exit code; a signed or digest-bound artifact; a consent, security or retention decision."
- "POC beads are admitted as improvement-cycle work. Bead `syzygy-bpyt.10` is the cycle report, and POC shared-model work stays at WIP one."

The review rule:

- "pull requests touching class 1 (authority boundaries), class 3 (deterministic observation) or class 4 (security) …"
- The three further checks: "an old-versus-new differential over a mutated-record corpus that includes records with altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report."

Part 3:

- "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."

### AGENTS.md at `fe46265d`

Verification rules:

- Rule 4: "Read a check's output, not its exit code, and check its denominator against the whole population."
- Rule 6: "Mutate the input and confirm the check fails, per predicate, before trusting it".
- Rule 7: "Run the battery in a clone before calling it green; the report is valid only for that commit."
- Rule 9: "A claim of absence needs a sweep with a denominator."
- Rule 11: "An evidence record names its subject and the subject's digest; a record that names neither cannot be re-checked against the bytes it describes."

Guardrails:

- "A mutation that throws at describe time reports zero tests and scores as survived — build fixtures in `beforeAll`."
- "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at; ids and outcomes alone are not re-runnable, and a rebase-merge leaves the recorded commit reachable from no ref."
- "Conformance expected values are hard-coded literals, never imported from the module under test."

Beads scope:

- "POC shared-model changes have WIP one."

### Test-rigor bar

From `th-engineering/subskills/test-rigor/SKILL.md`:

- "A test is worth keeping only if some plausible bug makes it fail."
- Bar 4: "Expected values are literals or independently derived."
- Bar 6: "Deterministic or quarantined".
- Bar 7: "A failure names the defect — Test names state expected behavior".
- Bar 10: "Reviews state the net test delta".

## 3. What I ran and the results

### Setup

- I made two clones of `/home/tze/GitHub/syzygy` under my scratch directory, fetched `agent/syzygy-bpyt.5.8`, and detached one at `fe46265d` (head) and one at `0d4d5098` (base).
- In each clone, `npm ci --no-audit --no-fund` exited 0 and `npm run build:poc` exited 0.
- Every vitest run below used a private `TMPDIR` under my scratch directory unless the row says otherwise.

### Gate position (poc-main.ts, base against head)

The production diff is 4 lines [Observed]:

- `git diff --numstat 5837512f e8cb47d5 -- apps packages` prints `3	1	apps/three-surface-poc/src/poc-main.ts` and `213	19	apps/three-surface-poc/src/main.test.ts`.
- The 4 lines:
  - `poc-main.ts:83` `readonly materializeRoutes: typeof materializeRoutes;`
  - `:95` `materializeRoutes,` (in `REAL_DEPS`)
  - `:197` `...deps.materializeRoutes({`, replacing base `:195` `...materializeRoutes({`.

The gate:

- Head `:120-124`, base `:118-122`: both call `launchAfterPwbRepositoryBinding(repoRoot, deps.resolveBinding, (boundRepoRoot) => serveBoundRepository(boundRepoRoot, parsed.config, io, deps))`. The text is byte-identical [Observed].
- `launcher.ts` calls `launch(binding.locator)` only after `if (binding.kind === 'rejected') return binding;` [Observed].
- `launcher.ts` and the body-read authority module are not in the diff [Observed].
- So every serving path is still behind the P1 gate, in the same order.

The seam:

- `deps.materializeRoutes(...)` sits in the same spread position inside the `deps.createDaemon({ routes: [...] })` literal, after `...pocRoutes(...)` and before `...reobserveRoutes(...)`, at head `:196-203` and base `:194-201` [Observed]. It receives the same four options.
- [Observed] `materialize-action.ts` has no `this` in code. All 10 matches for the word are in comments or strings. So calling it as a method of `deps` cannot change its behaviour.
- [Observed] The differential's daemon log records the registered route list in order: 19 routes, among them `POST /trajectory/materialize human-open` and `POST /butlers-syzygy/trajectory/materialize human-open`. The list is equal at base and head (see section 5).

Production reaches `deps` only through `REAL_DEPS` [Observed]:

- `main.ts` calls `main(process.argv.slice(2), {…})` with two arguments.
- `REAL_DEPS` is a non-exported `const`.
- `poc-main` is named by exactly 3 files under `apps/`, `packages/` and `scripts/` (`.ts/.mjs/.js/.py/.json`, excluding `node_modules` and `dist`):
  - `main.ts`, the entry;
  - `main.test.ts`;
  - `watch-mode.test.ts:89`, which holds the path as a string literal.

Importing poc-main has no side effect [Observed]:

- `node --input-type=module -e "…await import('<head>/apps/three-surface-poc/dist/poc-main.js')…"` printed `exports main signal listeners added 0 active handles none exitCode undefined` and exited under a 30 s `timeout`.

### Commands and results

| # | What | Tree | Result (verbatim where quoted) |
|---|---|---|---|
| 1 | `npx vitest run apps/three-surface-poc/src/main.test.ts` | head | [Observed] `Tests  24 passed (24)`. The private TMPDIR then held only `node-compile-cache`. |
| 2 | Same file, 10 sequential runs (`repeat_main_test.sh`) | head | [Observed] 10 of 10 `exit=0`, each `Tests  24 passed (24)`. Wall times 2.29–2.79 s. Load average 6.41–9.06 on 12 cores. |
| 3 | Same file, 12 concurrent copies, each with its own TMPDIR | head | [Observed] 12 of 12 `exit=0`, `Tests  24 passed (24)`. `load after: 14.86 14.14 13.62`. Durations 5.48–6.78 s. 0 entries left in any copy's TMPDIR besides `node-compile-cache`. |
| 4 | Same file, 24 concurrent copies | head | [Observed] 24 of 24 `exit=0`, `Tests  24 passed (24)`. `load after: 33.94 18.41 15.03`. Durations 9.42–12.66 s. The test phase of three sampled logs was `tests 377ms`, `tests 808ms` and `tests 691ms`, far under the tightest bound (2,000 ms). 0 entries left besides `node-compile-cache`. |
| 5 | The 13 recorded mutants, fragments copied verbatim from `mutants-main-test-head-2026-10-22.json` and run by my own runner (`run_mutants.py`) against `main.test.ts` alone | head | [Observed] `control 0 24 0`, then 13 of 13 `killed`, `survivors: []`. For all 13 the outcome and the set of failing tests equal the lane's record. |
| 6 | The same 13 | base | [Observed] `control 0 18 0`. The 9 N1 mutants are all `SURVIVED 18 0`. `state-dir-digest-input killed 18 1`. `materialize-seam-bypassed`, `started-ignores-finish` and `started-ignores-bound` are `FRAGMENT-COUNT-0` (the fragments do not exist at base). For the 9 the outcome and failing sets equal the lane's base record. |
| 7 | The reviewer's own 18 mutants (`own.json`, listed in section 7) | head / base | [Observed] Head: 16 of 16 production mutants killed. Base: 11 of those 16 survive, so these are newly covered, and 5 were already killed. The 2 test-constant mutants survive at head (note N3). |
| 8 | Full failure diffs for `reobserve-horizon-root`, `session-clock`, `revision-change-root` and `started-ignores-bound` (`show_mutant.py`) | head | [Observed] Quoted under N1 in section 6. |
| 9 | Lane's `sweep_waits.py` | head / base | [Observed] Head: `{"itBlocks": 24, "viWaitForCalls": 1, "blocksWithAWait": 11, "boundedBlocks": 11, "waitingBlocksNotBounded": []}`. Base: `"itBlocks": 18, … "blocksWithAWait": 5, "boundedBlocks": 0`, five blocks listed with `"testTimeoutMs": 5000`, exit 1. |
| 10 | Second method for row 9 (`count_waits.py`: regex over every `it(`/`test(` call at any indent) | head / base | [Observed] Head: `it/test calls: 24`, `with a wait: 11`, `with a wait and an explicit timeout: 11`, timeouts `['2_000', 'TEST_TIMEOUT_MS']`. Base: `18`, `5`, `0`. The two methods agree. |
| 11 | Lane's `mutate_sweep_waits.py` | head | [Observed] 6 of 6 `killed`, `survivors: []`. |
| 12 | `npm run typecheck`, after `build:poc` | head | [Observed] Exit 0, no diagnostics printed. |
| 13 | `python3 scripts/check_governance.py` | head / base | [Observed] Both trees: `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted`. The set of verdict lines, counts stripped, hashes the same at base and head (`59d55cdf…`). Scope at head: `3147 tracked`. |
| 14 | `python3 scripts/check_quotations.py` | head / base | [Observed] Output files byte-identical at base and head (sha256 `a18c4bf91b0efceaf722ba5d86789f00efc616366238c86e1e2a302970d07d27`). |
| 15 | PWB-REQ-014 sweep: `npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts` | head | [Observed] `Tests  5 passed (5)`. |
| 16 | My own sweep of the 14 JSON evidence records for keys named `source`, `provenance`, `evidence` or `anchor` (case-folded) | head | [Observed] `json files 14 keys walked 2934 hits 0`. No record key can trip the authority sweep. |
| 17 | 42-scenario differential (`run_differential_fixed_roots.py` against old script `1d6731bb`; harness sha256 `a93c6443…767a`, the same in both trees). Same fixed root and same TMPDIR for both runs. | base, then head | [Observed] Both runs: `"replacements": 6, "run": {"exit": 0, "tests": 44, "passed": 44, "failed": []}`. Section 5 has the comparison. |
| 18 | Route capture (`route-capture.mjs`), same fixture path for every run: base, head, base again | base / head / base | [Observed] Each run: `variants=5 routesPerVariant=19,19,19,19,19 responses=230`. Fixture revision `1f892687d53c829f9c2a4ee99bccccb23d6158df`, the same as the lane's. |
| 19 | Emitted-output comparison of every `dist/` (`.js` and `.d.ts`) | base / head | [Observed] Section 5. |
| 20 | The three-surface-poc vitest project, `npx vitest run --project @syzygy/three-surface-poc-app` | head | [Observed] First run, private TMPDIR: `Test Files  10 failed \| 78 passed \| 1 skipped (89)` and `Tests  6 failed \| 1046 passed \| 43 skipped (1095)`. All 10 failures were `Error: browser exited with signal before announcing a DevTools endpoint`. Explanation in the next three rows. |
| 20a | `orrery.browser.test.ts` | base, same long TMPDIR | [Observed] Fails with the same error. |
| 20b | `orrery.browser.test.ts` | head, system TMPDIR | [Observed] `Tests  1 passed (1)`. |
| 20c | The 10 failing files | head, system TMPDIR | [Observed] `Test Files  10 passed (10)` and `Tests  88 passed \| 1 skipped (89)`. |

The project failures in row 20 come from the host, not from this PR:

- [Inferred] My TMPDIR is 105 characters, so Chrome's `SingletonSocket` path is 147 bytes, beyond the Unix socket path limit.
- None of the 10 files is touched by this PR, and base fails the same way.

Not run by me:

- [Unknown] The whole-repository `npx vitest run` and the canonical battery. The lane reports these as 5,012 passed at `e8cb47d5` and `commands=110 nonzero=0` at `fe46265d`.

## 4. Findings

No blocking (F) findings. Five notes. Each is written to be acted on cold.

### N1 — note (low; evidence records): four record-level defects and a tool temp-directory leak; no conclusion rests on them

**Evidence.** [Observed] in each item.

1. **`productionChange["poc-main.ts"]` holds the test diff.**
   - In `verification-2026-10-22.json`, `productionChange` has the keys `files` and `poc-main.ts`. `poc-main.ts` lists 236 `+`/`-` lines.
   - By `git diff --numstat 5837512f e8cb47d5 -- apps packages`, 232 of those lines are from `main.test.ts` and 4 from `poc-main.ts`.
   - The list is built at `assemble_records.py:73-75` from `git diff base code -- apps packages`.
   - The PR body itself says "Every other change is in `main.test.ts`".
2. **`nonVacuity.distinctScenarioTranscripts: 42` is 42 by construction.**
   - In `differential-2026-10-22.json` the value comes from `compare_differentials.py:67`, `len({json.dumps(t, sort_keys=True) for t in head})`, and each `t` carries the scenario `name`.
   - Over the old-arm transcript alone (stdout, stderr, exit code, calls, thrown, after, closed), my head run has **39 distinct transcripts across 42 scenarios**. Three pairs are identical:
     - `help` / `help-short`;
     - `repo-git-fails-no-status` / `repo-git-status-out-of-range`;
     - `model-throws-custom-error` / `model-throws-string`.
   - The pairs are legitimate: each pair is one classified refusal [Inferred].
   - The figure is not a non-vacuity measure, and the PR body repeats it as "42 distinct transcripts". None of the 9 perturbations in `mutants-comparators-2026-10-22.json` would expose it.
3. **"Three statements" against six replacements.**
   - `run_differential_fixed_roots.py`'s docstring says "a copy of the harness in which three statements are replaced", and the PR body says "replaces three statements of the harness".
   - `REPLACEMENTS` has 6 entries, and the runner prints `"replacements": 6`.
4. **"4 extra mutants killed" counts one that base already killed.**
   - `verification-2026-10-22.json` says `extraMutantsKilledAtHead: "4 of 4"`, which is true.
   - But `state-dir-digest-input` is already killed at base (row 6: `state-dir-digest-input killed 18 1`, failing test "defaults the state directory to a per-repository directory under the OS temp directory").
   - The base record lists only the 9 N1 mutants, so it cannot show that 1 of the 4 extras is not new coverage.
5. **The evidence tools leak a temp directory per run.**
   - `run_differential_fixed_roots.py` creates `tempfile.mkdtemp(prefix='zz-differential-')` and never removes it. Two `zz-differential-*` directories were left in my TMPDIR after my two runs.
   - `mutate_wiring.py`'s `zz-mutate-wiring-` directory has the same shape [Inferred from code; I did not run that script].

**Failure scenario.**

- A cold reader takes `productionChange["poc-main.ts"]` as the production diff and finds 236 lines where the PR says 4.
- A later reviewer cites `distinctScenarioTranscripts` as non-vacuity for a differential in which every scenario printed the same refusal. It would still read 42.

**Proposed fix.**

- These records are bound to the reviewed bytes, so carry the corrections in the round dispositions record. Do not edit the records.
- If the tools are reused:
  - split the diff per file under a key such as `codeDiffLinesByFile`;
  - compute distinctness over `t['old']` without `name`, and report it beside the scenario count;
  - make the docstring say "six replacements, three of which fix the roots";
  - record the base outcome of every extra mutant;
  - remove the report temp directory in a `finally`.

### N2 — note (low; evidence scope): the route capture cannot observe a change to `poc-main.ts`

**Evidence.**

- [Observed] `docs/evidence/poc-hygiene-2026-10-22/route-capture.mjs` imports these files from `dist` and never imports `poc-main.js`:
  - `cap1-daemon/dist/index.js`;
  - `routes.js`, `materialize-action.js` and `reobserve-action.js`;
  - `test-model-fixture.js`, `test-project-shape-fixture.js` and `browser-origin.js`.
- [Observed] It composes the routes itself:
  - `...pocRoutes(() => model)` with one argument, where `main` passes six;
  - `...materializeRoutes({ … targetRepoRoot: path.join(scratch, variant, 'target') … })`;
  - `...reobserveRoutes(…)`.
- [Inferred] So no edit to `poc-main.ts` can change its output. Its 230/230 byte equality (section 5) is true, but it is a control on the route modules and on main's merged core. It does not test this PR's seam.
  - Example: `credential-provision-dropped` and `reevaluation-dropped` change what `GET /` renders in production. They cannot move this capture.
- [Observed] What does observe the seam:
  - the 42-scenario differential, which calls `main` with `REAL_DEPS`, logs the 19-route registration in order, serves four pages and posts a re-observe;
  - the emitted-output comparison.

**Failure scenario.** A future composition-root change cites route-capture equality as "no changed output" while it changed what the composed routes receive (the credential provision, the latest re-evaluation, the verbatim reader root). Nothing measured it.

**Proposed fix.**

- In the dispositions, state that for this PR the route capture is a control on the route modules only.
- For future `poc-main.ts`-only changes, either drive the capture through `main()` with fake collaborators (the `main.test.ts` harness already does), or leave it off the "no changed output" list.

### N3 — note (low; test rigor): the N5 bound relation is enforced only outside CI

**Evidence.**

- [Observed] `main.test.ts:44-48` states the invariant in a comment ("every test that waits has a timeout above two of them") and in two constants, `WAIT_MS = 10_000` and `TEST_TIMEOUT_MS = 30_000`.
- [Observed] My mutant `R-wait-ms-above-test-timeout`, `const WAIT_MS = 10_000;` → `const WAIT_MS = 40_000;`, survives `main.test.ts` at head (24 passed). Each `started()` bound now exceeds its test's timeout.
- [Observed] Only the lane's `sweep_waits.py` detects it. Over all 3,147 tracked files at `fe46265d`, `git grep -l -F sweep_waits` lists 6 files, all under `docs/evidence/poc-main-wiring-2026-10-22/`.
- [Observed] A targeted `git grep -c` over `.github` (3 workflow files), `scripts`, `package.json` and `PROJECT-STATUS.md` prints nothing.
- So no CI step runs the sweep.

**Failure scenario.** A later edit raises `WAIT_MS`, or adds a waiting `it` without `, TEST_TIMEOUT_MS`. Under host load the test then fails "Test timed out in …ms" instead of naming the unmet expectation, which is exactly what N5 repaired, and CI stays green until that happens.

**Proposed fix.** Either one makes the comment's invariant mechanical:

- derive the timeout as `const TEST_TIMEOUT_MS = 3 * WAIT_MS;`; or
- add a one-line case asserting `expect(2 * WAIT_MS).toBeLessThan(TEST_TIMEOUT_MS)`.

### N4 — note (low; test naming and literals): "reads the exact requirement text" reads no text

**Evidence.** [Observed]

- The test is at `main.test.ts:480`.
- The module mock at `:34-40` makes every reader return `undefined` for every object.
- The test asserts three things (`:492-494`):
  - `response.status` is 200;
  - `blobReader.roots` equals `[BOUND]`;
  - `blobReader.objectIds.length` is greater than 0, which is not a literal.
- The root pin, the purpose N1 gave it, is sound: `verbatim-reader-root` and `R-verbatim-reader-configured` both fail at `:493`.

**Failure scenario.** [Inferred] A regression that asks the reader for the wrong object id, or that ignores the bytes the reader returns, still passes. A maintainer reading the name believes the exact-requirement text path is covered (test-rigor bar 7).

**Proposed fix.** Either:

- rename the test to say what it pins, for example "builds the Polaris blob reader for the bound repository and asks it for objects"; or
- have the fake return the fixture's baseline-spec blob for its object id, assert the exact requirement line appears in the response, and pin the requested object id(s) as literals from the fixture.

### N5 — note (low; GP-Q0 record): the PR does not say how the altered-prose limb is met

**Evidence.**

- [Observed] The PR body says "The GP-Q0 extras apply" and lists four proofs: the differential, the route capture, the emitted output and the tests. None of the evidence names a mutated-record corpus or altered prose.
- [Observed] The limb is met vacuously:
  - The only emitted differences are the 5 seam lines in `poc-main.js` and `poc-main.d.ts` (section 5).
  - Those lines pass one function reference and read no record.
  - In the differential, every record reader (`git-observation.js`, `production-reobserve.js`) is a fake.
- The earlier owner notices in `syzygy-bpyt.10` state such vacuity explicitly. For example, the PR #504 notice says "The old-versus-new differential is met vacuously, because the gate bytes are identical".

**Failure scenario.** The owner notice for this bead says "GP-Q0 extras applied" without saying the altered-prose limb is vacuous and why. A reader cannot then tell whether it was checked or skipped.

**Proposed fix.** In the owner notice and the dispositions, say that the altered-prose limb is met vacuously: the changed bytes read no record, and the emitted difference is 2 files, 5 lines, all seam wiring. Cite this section.

## 5. Every changed output, or the evidence that there is none

### Emitted code

[Observed] I compared every `.js` and `.d.ts` under the six `dist/` directories built in both clones:

- `apps/three-surface-poc`, `cap1-core`, `cap1-daemon`, `polaris-generation-consent`, `polaris-generation-core` and `three-surface-poc-core`.

The result:

- 376 shipped files compared, with 316 test files counted apart;
- 0 files in only one tree;
- **2 files differ**, `apps/three-surface-poc/dist/poc-main.js` and `apps/three-surface-poc/dist/poc-main.d.ts`;
- `diff -rq` over the whole `packages/` trees, `node_modules` excluded and `dist` included, printed nothing.

The exact differing lines:

- `poc-main.js`: `>     materializeRoutes,` and `<                 ...materializeRoutes({` → `>                 ...deps.materializeRoutes({`.
- `poc-main.d.ts`: `> import { materializeRoutes } from './materialize-action.js';` and `>     readonly materializeRoutes: typeof materializeRoutes;`.
- Also differing: `main.test.js`, the `.map` files and `.tsbuildinfo`.

The lane's record compares 5 projects, 360 files and 306 tests, at `5837512f`/`e8cb47d5`. That is a different population at a different tree pair. Its 2 differing files and their lines are the same as mine [Observed].

### Differential

My runs compared base `0d4d5098` with head `fe46265d` [Observed]:

| Measure | Result |
|---|---|
| Scenarios | 42 at both trees, names in the same order. |
| Equal base against head | **42 of 42**. |
| Raw transcript files | **Byte-equal**: both hash to `2213af9c0553b4cd0f9f9c7841609d356c2da180b07f0d41f015a62bf4595ac2`. The canonical forms both hash to `d3d097cf3043393ac6fb0e1721688b4ebdf661df2036010484d15a1ecfde5645`. |
| `old == new` within each tree | 42 of 42; `entryEqualsOld` true in 42 of 42. |
| Distinct outputs | **39 distinct old-arm transcripts over 42 scenarios** (N1, item 2). 10 distinct stdouts and 22 distinct stderrs. Exit codes `[0, 1]`. |
| Scenarios that served | 16. |
| Scenarios with post-start actions | 8. They return `GET /polaris: 200 … len=107695`, `GET /trajectory: 200 … len=32488`, `GET /orrery: 200 … len=46583`, `GET /api/poc: 200 application/json len=33866`, and five `POST /polaris/reobserve: 502` bodies. |
| Daemon calls | 22, of 3 distinct forms. Each registers 19 routes. |

How the digests relate to the lane's:

- [Observed] My canonical transcripts equal the lane's kept `differential-transcripts-2026-10-22.json` (sha256 `b0c6823f…`) in 37 of 42 scenarios.
- The other 5 are the scenarios the PR body names as root-bound: `happy-default-state-dir`, `happy-pages`, `reobserve-ok`, `reobserve-dirty` and `watch-enter-reobserves`.
  - Their page lengths are equal.
  - Their body digests and the default state directory embed my fixed root and my TMPDIR.
- **The lane's AC2 result, measured at `e8cb47d5`, holds at the merged head.**

### Route capture

[Observed] My three capture files, base, head and base again, are byte-identical: all three hash to `af652b948bcde395f749d8f94cd9ae518a7d1bc68e87cc92b5861d883969b3d0`.

| Measure | Result |
|---|---|
| Request keys | 230; equal base against head 230 of 230; equal base against base again 230 of 230. |
| Statuses | `200` 150, `401` 40, `403` 20, `502` 20. |
| Distinct body digests | 73. |
| Request paths whose body varies by fixture | 30 of 46. |

These figures equal the lane's. My digests differ from the lane's (`55586857…`) only because body digests are bound to the fixture path, as the lane disclosed. The lane's kept `route-capture-head-2026-10-22.json` hashes to `55586857…`, its comparison's `head.rawSha256` [Observed]. The capture's scope is limited (note N2).

### Refusal strings and exit codes

- [Observed] The differential's 23 refused, 1 rejected-with-throw and 2 usage scenarios are equal at base and head, as above.
- [Observed] In `main.test.ts`, the 18 existing tests keep their names (0 removed). Their bodies changed only in the test-timeout argument and one `waitFor` option. The harness's fake `observeRevisionChange` now records a call; the existing call-log assertions are unchanged and pass.

### Gates

[Observed] No gate accepts or refuses differently:

- the gate call is byte-identical;
- `launcher.ts` and the body-read authority module are not in the diff;
- the P1-gate cases pass, and `R-gate-bypass` is killed by 7 tests at head and 5 at base.

### Shared model and governed planes

[Observed] The diff touches no `packages/**`, `openspec/**` or `.syzygy/**` file. So the "WIP one" rule for POC shared-model changes does not bind this PR, and no digest-bound artifact is edited (`check_quotations` output is byte-identical).

**Conclusion.** No changed output, except the 2 emitted seam files above.

## 6. Verdict per acceptance criterion

### AC1 — "All nine N1 mutants killed by main.test.ts (recorded)": MET

[Observed] At `fe46265d`, 9 of 9 are killed by `main.test.ts` alone. At `0d4d5098`, 9 of 9 survive (18 tests). The lane's records reproduce exactly (row 5 and row 6).

Each new test kills its mutant for the stated reason, at a named assertion and not by an incidental throw:

| Mutant | Where it fails |
|---|---|
| `bound-locator-ignored` | `:448` `expected 'Syzygy Three-Surface POC: http://127.…' to contain 'Observed repository: /bound/butlers-c…'`, and `:493` (blob reader roots). |
| `reobserve-horizon-root` | `:469`: `-   "horizon /bound/butlers-checkout butlers-rev",` / `+   "horizon /observer/syzygy butlers-rev",` |
| `session-clock` | `:469`: `-   "model 2 butlers-rev /bound/butlers-checkout /observer/syzygy 2026-10-22T09:01:00.000Z",` / `+   "model 2 butlers-rev /bound/butlers-checkout /observer/syzygy 2026-10-21T22:30:34.239Z",` |
| `verbatim-reader-root` | `:493` `expected [ '/observer/syzygy' ] to deeply equal [ '/bound/butlers-checkout' ]` |
| `materialize-target-root` | `:462` `expected '/observer/syzygy' to be '/bound/butlers-checkout'` |
| `revision-change-root` | `:469`: `-   "change /bound/butlers-checkout butlers-rev-build-1 butlers-rev-build-2",` / `+   "change /observer/syzygy butlers-rev-build-1 butlers-rev-build-2",` |
| `state-dir-unresolved` | `:507` `expected false to be true` (`isAbsolute`). |
| `credential-provision-dropped` | `:528` `… to contain 'credential minted;'` |
| `reevaluation-dropped` | `:529` `… to contain 'Observed-project limb: no prior evalu…'` |

The four extras are killed at head:

| Extra | Where it fails |
|---|---|
| `materialize-seam-bypassed` | `expected undefined to be '/bound/butlers-checkout'`. |
| `state-dir-digest-input` | Also killed at base (N1, item 4). |
| `started-ignores-finish` | `expected 10004 to be less than 5000`. |
| `started-ignores-bound` | `Error: Test timed out in 2000ms.` This is a kill by the test timeout, as the PR says. |

The fake `resolveBinding`'s locator is distinguishable at every argument it should reach [Observed]:

- `BOUND` is `'/bound/butlers-checkout'`, `:432`.
- The configured `--repo` is the realpath of a `mkdtemp` directory.
- The observer is `'/observer/syzygy'`.
- `:447` asserts `digest16(BOUND)` differs from `digest16(repoRoot)`.

Coverage beyond the recorded mutants [Observed]:

- I wrote 11 further mutants that substitute the *configured* path (`config.repoRoot`, the other wrong source in scope) for the bound locator, at each repository-rooted argument and in the materialize options:
  - `R-observe-configured` and `R-horizon-start-configured`;
  - `R-model-root-configured` and `R-reobserve-horizon-configured`;
  - `R-revision-change-configured` and `R-verbatim-reader-configured`;
  - `R-materialize-target-configured` and `R-banner-configured`;
  - `R-state-digest-configured` and `R-materialize-state-config`;
  - `R-on-materialized-dropped`.
- All 11 are killed at head and survive at base.

### AC2 — "No changed output: differential 42/42 equal, route capture byte-identical": MET at the merged head

- [Observed] Differential: 42 of 42, raw files byte-equal, 39 distinct outputs.
- [Observed] Route capture: three byte-identical files, 230 of 230 keys.
- Both were measured base `0d4d5098` against head `fe46265d`, not at the lane's `e8cb47d5`.
- Notes N1 (item 2) and N2 qualify what these figures prove.

### AC3 — "No unbounded poll; waitFor timeout below the test timeout": MET

The waits:

- [Observed] `started()` (`:186-194`) exits its loop on whichever comes first: both listeners registered, the run settled (`exitCode` set by both arms of `run.then`), or `Date.now() < deadline` failing. So it cannot spin forever.
- [Observed] The bound is the parameter `boundMs`, default `WAIT_MS`.
- [Observed] The one `vi.waitFor` (`:402`) takes `{ timeout: WAIT_MS }`.

The denominators:

- [Observed] 11 of 11 waiting blocks are bounded at head, by two methods. 0 of 5 are bounded at base.

Under load:

- [Observed] 10 sequential runs, 12 concurrent copies and 24 concurrent copies (load average 33.94 on 12 cores) passed, 46 of 46 runs.
- [Observed] The test phase stayed under 1 s, so these bounds do not turn load into flakes.
- The relation between the bounds is not enforced in CI (N3).

### AC4 — "CC-REV-1 class 1/3 review with the GP-Q0 extras; owner notice": MET by this review, except the owner notice, which is pending

- This file is the independent CC-REV-1 review for classes 1 and 3.
- The GP-Q0 extras:
  - The differential is present and equal. Its altered-prose limb is met vacuously but not stated (N5).
  - A rule-6 mutant per predicate: the production change adds no predicate. The two loop conjuncts of the test helper that bound the wait are mutated and killed.
  - [Unknown] I did not mutate `fake.registered() < 2` or the post-loop `if` order.
- The owner notice:
  - [Observed] It is not yet posted. `bd comments syzygy-bpyt.10` lists 10 notices, the latest for PR #506, and none for `syzygy-bpyt.5.8`.
  - [Observed] Every earlier notice in that bead was posted after its PR merged.
  - The PR body says the notice "is the coordinator's to post". It needs no byte change, and it should carry N5's statement.

## 7. Test quality

Literal expectations:

- [Observed] The new tests compare against literal strings and arrays: the call logs at `:450-458` and `:469-474`, the page phrases at `:528-534`, the error messages at `:546` and `:554`.
- [Observed] Two expectations are computed:
  - `:446`, `join(tmpdir(), 'syzygy-three-surface-poc', digest16(BOUND))`, re-derives the state-directory formula. Base's default-state-directory test used the same pattern. `:447` guards it by asserting the two digests differ.
  - `:508`, `join(process.cwd(), 'relative', 'poc-state')`.
- Neither imports from the module under test. I take both as independently derived under bar 4 [Inferred].
- The one non-literal count is N4's `objectIds.length > 0`.

Fixtures cannot throw at describe time:

- [Observed] `buildFixtureModel` runs inside `it` bodies (`:482`, `:519`).
- [Observed] The `describe` bodies hold only constants and pure closures (`BOUND`, `bindTo`, `digest16`).
- [Observed] `vi.hoisted` and `vi.mock` are module-level and pure: the mock factory spreads the original module and replaces one function.
- [Observed] Control runs report 24 tests at head and 18 at base, so no file reported zero tests.

No leaked temporary directories:

- [Observed] Every run of `main.test.ts` alone left nothing in its private TMPDIR except Node's `node-compile-cache`. That is runs 1 to 4 and the 26 mutant runs: 47 TMPDIR observations in all.
- [Observed] Fixture copies go into `fixtureDirectories`, and `afterAll` (`:57-61`) removes them. The template is removed through `syzygyAfterTestFile`.
- The project-wide run did leave `.com.google.Chrome.*` and one `polaris-draft-browser-*` directory. They came from the Chrome crashes in row 20, in files this PR does not touch.

Determinism:

- [Observed] The injected clock `() => \`2026-10-22T09:0${tick++}:00.000Z\`` (`:441`) produces malformed text after 10 reads. The test makes 2 reads, so it is deterministic. It is fragile if `main` gains clock reads, though that would also be a behaviour change the test should catch.
- [Observed] The `gives up after its bound` case leaves one never-settling `main` promise. It holds no timer.

Net test delta (bar 10):

- [Observed] In `main.test.ts`, +6 tests, 0 removed, 18 renamed or changed in name: 0.
- I did not re-derive the PR's whole-project `Tests: +6 ~0 -0` [Unknown].
- Each added test kills at least one mutant that no base test kills (rows 6 and 7), so none is growth without protection.

The reviewer's own mutants, as rule 6 requires, each `old` → `new` in `apps/three-surface-poc/src/poc-main.ts` unless marked:

| Mutant | Old | New | Head | Base |
|---|---|---|---|---|
| `R-observe-configured` | `const repository = deps.observeGitRepository(repoRoot);` | `…(config.repoRoot);` | killed | survived |
| `R-horizon-start-configured` | `deps.observeGitHorizon(repoRoot, repository.revision)` | `config.repoRoot` | killed | survived |
| `R-model-root-configured` | `    repoRoot,\n    stateDir,\n    observerRoot: io.cwd(),` | `repoRoot: config.repoRoot,` | killed | survived |
| `R-reobserve-horizon-configured` | `deps.observeGitHorizon(repoRoot, pinned)` | `config.repoRoot` | killed | survived |
| `R-revision-change-configured` | `deps.observeRevisionChange(repoRoot, from, to)` | `config.repoRoot` | killed | survived |
| `R-verbatim-reader-configured` | `gitBlobReaderFor(repoRoot)` | `gitBlobReaderFor(config.repoRoot)` | killed | survived |
| `R-materialize-target-configured` | `targetRepoRoot: repoRoot,` | `targetRepoRoot: config.repoRoot,` | killed | survived |
| `R-banner-configured` | `` `Observed repository: ${repoRoot}` `` | `${config.repoRoot}` | killed | survived |
| `R-state-digest-configured` | `.update(repoRoot).digest('hex')` | `.update(config.repoRoot)…` | killed | survived |
| `R-materialize-state-config` | `stateDir: () => stateDir,` | `stateDir: () => config.stateDir ?? stateDir,` | killed | survived |
| `R-on-materialized-dropped` | `onMaterialized: session.afterMaterialized,` | `onMaterialized: () => undefined,` | killed | survived |
| `R-observatory-root` | `deps.observeObservatoryDrift(io.cwd(), buildRevision)` | `(repoRoot, buildRevision)` | killed | killed |
| `R-observer-root` | `const observer = deps.observeGitRepository(io.cwd());` | `(repoRoot)` | killed | killed |
| `R-model-observer-root` | `    observerRoot: io.cwd(),\n  });` | `observerRoot: repoRoot,` | killed | killed |
| `R-capture-clock` | `buildPocEvaluationEvidence(io.now(),` | `buildPocEvaluationEvidence(new Date().toISOString(),` | killed | killed |
| `R-gate-bypass` | `    deps.resolveBinding,\n` | `() => ({ kind: 'bound', locator: repoRoot, gitCommonDirectory: '' }),` | killed (7 tests) | killed (5 tests) |
| `R-wait-ms-above-test-timeout` (main.test.ts) | `const WAIT_MS = 10_000;` | `const WAIT_MS = 40_000;` | **survived** (N3) | n/a |
| `R-waitfor-unbounded-again` (main.test.ts) | `{ timeout: WAIT_MS }` | `{ timeout: 5000 }` | survived | n/a |

`R-waitfor-unbounded-again` is equivalent for AC3 [Inferred]: 5,000 ms is still below the 30,000 ms test timeout.

Evidence re-runnability (rules 6 and 11):

- [Observed] The directory holds **14 JSON records and 10 scripts**, 24 files. The brief said 15 records. The 26-file diff is these 24 plus the 2 code files.
- [Observed] These records name both the subject commit and the subject's digest:
  - `mutants-main-test-head` and `mutants-main-test-base`: `treeCommit` and `sha256AtCommit` for both code files, plus `old`/`new` for 13 and 9 mutants;
  - `sweep-waits-head` and `sweep-waits-base`: `treeCommit` and `fileSha256`;
  - `differential`: tree commits, the harness and old-script sha256, and the raw and canonical transcript sha256;
  - `route-capture-comparison`: tree commits and the raw and canonical sha256 of the three captures;
  - `verification`: commits and `toolDigests` for all 10 scripts.
- [Observed] The two data files are named by digest from their comparison records: `differential-transcripts` hashes to `b0c6823f…` and `route-capture-head` to `55586857…`.
- [Observed] These records name a commit only, with no subject digest: `dist-compare`, `test-lists`, `mutants-comparators` and `mutants-dist-compare`.
  - The last two describe their perturbations in prose, for example "head transcript of one scenario differs from base".
  - The perturbation code lives in the retained scripts, whose digests `verification.toolDigests` records. So they can be re-run.
- [Observed] `mutants-sweep-waits` carries `old`/`new`, but the test file's digest only through `sweep-waits-head`.
- [Observed] What reproduces:
  - both mutant records reproduce exactly (rows 5 and 6);
  - `mutate_sweep_waits.py` reproduces 6 of 6 (row 11);
  - the wait sweep reproduces 11/11 and 0/5 (row 9);
  - the differential and capture equalities reproduce at the merged tree pair.
- [Inferred] The recorded commits `e8cb47d5` and `5837512f` stay reachable if the PR lands as a merge commit, as #493 and #503 did. If it is rebase-merged, the mutant and sweep records can still be checked through their file digests, which equal the bytes at `fe46265d`.

## 8. Cleanup

Deleted:

- both scratch clones;
- the route-capture fixture repository and its `.json`;
- the differential's fixed root;
- every private TMPDIR, which held the `zz-differential-*`, `rev507-report-*` and `.com.google.Chrome.*` leftovers.

Kept in `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-507/` for the coordinator:

- `scripts/`: my runners, `run_mutants.py`, `show_mutant.py`, `make_mutants.py`, `count_waits.py`, `compare_transcripts.py`, `record_identity.py`, `repeat_main_test.sh` and `stress_main_test.sh`;
- `out/`: the mutant lists and results, the transcripts, the captures, and the governance and quotation outputs;
- the two re-derived diffs.

One leftover in `/tmp`:

- [Observed] `/tmp/.com.google.Chrome.SQHmB0` was created at 06:42:14, during my system-TMPDIR browser re-run (row 20c). It holds a live-looking `SingletonSocket` and `SingletonCookie`.
- I did not delete it because its owner is uncertain [Inferred: probably mine, but another lane's Chrome may be using it].
- Nothing else in `/tmp` was created in that minute.
