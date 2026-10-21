# R-GP-IMPL-POC-APP-HYGIENE-2 — CC-REV-1 implementation review of syzygy-bpyt.5.5, round 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 20b23d90
Subject: r2-review.diff sha256 c72823c311a55a3f4d45abb4e6d257efc5f410bebfd8e9410218701993741a83

Reviewer: rev-501b. Fresh context, independent of the implementer and of the round-1 reviewer.
Constraint observed: I fetched no target repository content. No Butlers body or other observed
repository was read. Every probe used fixture repositories, empty scratch directories, or
`git init` directories under my scratch area. Date: 2026-10-22.

Summary: no blocking findings. The gate position, refusal strings and exit codes are preserved.
Importing `poc-main.ts` has no side effect. `deps` reaches production only through `REAL_DEPS`.
Every branch predicate in `poc-main.ts` has a killed mutant. The repairs re-derive their figures.
Seven notes follow (N1–N7). Each can be acted on cold.

---

## 1. Subject identity checks

| Check | Result |
|---|---|
| `sha256sum r2-review.diff` | [Observed] `c72823c311a55a3f4d45abb4e6d257efc5f410bebfd8e9410218701993741a83`. This is byte-equal to `git diff 1d6731bb 20b23d90` in my head clone, which covers 89 files. **Match.** |
| `sha256sum r2-repair.diff` | [Observed] `7c032fc386f60c03f4b7dd135d53b9c8024befd5b19c7e224933b20a7aee16ce`. This is byte-equal to `git diff 8acc6ca3 48944066`, which covers 28 files. **Match.** |
| Round-1 raw | [Observed] sha256 `0d4b1d5c7fea0de74025a8ccc332484783110a2ff4ab15ca32ea29047dc35202`. Its prefix matches the brief's `0d4b1d5c…`. |
| PR state | [Observed] `gh pr view 501`: headRefOid `20b23d909c4263aa9bf8e0446ba20f483ec04a47`, state OPEN. My head clone's `git rev-parse HEAD` returns the same. |
| Merge `8acc6ca3` (main `b7697f6a` into `4f3c3ebf`) | [Observed] `merge_check.py` compares each path's blob in the merge with the parent that changed it since the merge base: branch-only 75, main-only 10, both 0, bad 0. |
| Merge `20b23d90` (main `1d6731bb` into `48944066`) | [Observed] branch-only 89, main-only 13, both 0, bad 0. Both merges brought only main's bytes. No path was conflict-resolved. |
| `fa79bca6` (the records' `ranAtCommit`) → `20b23d90` | [Observed] `git diff --stat` lists 26 files. None is under `apps/`. Under `packages/` only `three-surface-poc-core/src/body-read-authority.test.ts` and `walkthrough-judgment.test.ts` changed, both from PR 504. The other 24 are under `docs/`. |
| Key blobs at head | [Observed] `poc-main.ts` `c5e5dc78…`, `main.ts` `cfb0a4e6…`; base `main.ts` `470ff646…`, which is the differential's `oldMainSha256`. |

## 2. Clauses relied on (quoted)

- **GP-Q0, part 1**
  - Source: `.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:52-55`.
  - Quote: "'Behavior-preserving' means none of the following changes: - a rendered byte, a wire
    format, a refusal string or an exit code; - a signed or digest-bound artifact; - a consent,
    security or retention decision."
- **GP-Q0, review rule**
  - Source: same file, lines 59-66.
  - Quote: "pull requests touching class 1 (authority boundaries), class 3 (deterministic
    observation) or class 4 (security) … an old-versus-new differential over a mutated-record
    corpus that includes records with altered prose; a rule-6 mutant for each predicate; a
    non-blocking owner notice in the cycle report."
- **GP-Q0, part 3**
  - Source: same file, lines 95-96.
  - Quote: "Any change not listed here to what a gate accepts or refuses stops and returns to the
    owner."
- **CC-REV-1**
  - Source: `.syzygy/governance/policies/craft-and-care/review-and-documentation.md:28-35`.
  - Class 1: "**authority boundaries** — write-universe, typed-authority table, adapter
    authorization (VIS-5, VIS-6)".
  - Class 3: "**deterministic observation** — snapshot composition, evaluation identity, the
    deterministic/inferred seam (VIS-7)".
- **PWB-REQ-005**
  - Source: `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:640-645`.
  - Quote: "The POC SHALL NOT read any Butlers project-shape body until each of the exact
    per-repository observation-consent record, the observing Syzygy project's concrete
    secret-detection/classification policy and the project-shape observer's governance-plane
    adapter-registry entry carries an effective human owner act …"
- **PWB-REQ-001**
  - Source: same spec, lines 361-364.
  - Quote: "WHEN the POC observes Butlers, it SHALL bind the complete source-path population to the
    configured repository's exact Git revision and SHALL bind the consent record, secret-policy
    version, source-discovery version and observer/parser version as deterministic evaluation
    inputs."
- **AGENTS.md verification rules**
  - Rule 4: "Read a check's output, not its exit code, and check its denominator against the whole
    population."
  - Rule 6: "Mutate the input and confirm the check fails, per predicate, before trusting it".
  - Rule 9: "A claim of absence needs a sweep with a denominator."
  - Rule 10: "Freeze the bytes a review is bound to; any later edit retires the review."
  - Rule 11: "An evidence record names its subject and the subject's digest; a record that names
    neither cannot be re-checked against the bytes it describes."
- **Bead acceptance criteria** (`bd show syzygy-bpyt.5.5`, read-only)
  1. "main.ts exports main(); a test drives it with a fake io (one behavior gate)."
  2. "Unused-export sweep (method stated) shows only deliberate test seams remain, each commented."
  3. "Orphan modules deleted or wired; suite and rendered bytes unchanged."

## 3. What I ran and the results

All runs used scratch clones of `/home/tze/GitHub/syzygy`:
- `head` at `20b23d90`, with the PR branch fetched as `refs/remotes/pr/bpyt55`;
- `base` at `1d6731bb`;
- `r1` at `4f3c3ebf`, the round-1 head, used as the control only.

Each clone had `npm ci` and then `npm run build:poc`. My scripts are in `rev-501b/scripts/` and my
outputs in `rev-501b/out/`.

**Tests and checks at head**

- **Targeted vitest** (`main.test.ts`, `watch-mode.test.ts`, `launcher.test.ts`,
  `polaris-authority-sweep.test.ts`). [Observed]
  - "Test Files  4 passed (4)"
  - "Tests  39 passed (39)"
  - main.test.ts reported "(18 tests)".
  - The PWB-REQ-014 sweep reported "(5 tests)", including "Zero downstream citations of Polaris as
    authority (PWB-REQ-014) > no source/authority/provenance field in the governance, spec, code or
    docs trees names the Polaris surface".
- **Three-surface-poc-app vitest project.** [Observed]
  - "Test Files  88 passed | 1 skipped (89)"
  - "Tests  1087 passed | 2 skipped (1089)"
- **Dependents of `./dossier-render`** (the 5 polaris-dossier test files). [Observed] 181 passed.
- **`npm run typecheck`**, run after `build:poc`. [Observed] Exit 0, no output.
- **`python3 scripts/check_governance.py`.** [Observed] "32 OK, 21 WARN, 0 FAIL (53 checks) — counts
  derived, not asserted".
- **`python3 scripts/check_quotations.py`.** [Observed] Output identical at base and head
  (QC-1: 33 quotations, 0 findings).
- **Two ceiling-act `--check` scripts.** [Observed] Both pass: "P-114 record … regenerate exactly."
  and "pwb-registry-machine-ceiling-amendment: applied, verifies".
- **Canonical battery.** [Unknown] I did not re-run it. The PR body's
  `commit=20b23d90… commands=110 nonzero=0` is lane-reported.

**Test lists (base `1d6731bb` against head)**

- [Observed] `npx vitest list` gives 4982 → 4992 lines.
- Added 19: 18 in `main.test.ts` and 1 in `watch-mode.test.ts`.
- Removed 9: all from `source-adapter.test.ts`.
- This reproduces "Tests: +19 ~0 -9". The record's own base was `b7697f6a`, which has 4919 → 4929
  lines; the delta is the same.

**F1 invocation checks (base against head)**

- **The implementer's `invocation_forms.py`**, re-run at `1d6731bb` against `20b23d90`.
  [Observed] "pairs=30 identical=30 distinctHeadOutputs=5".
- **Control**, the same script at `1d6731bb` against round 1's `4f3c3ebf`.
  - [Observed] "pairs=30 identical=10 distinctHeadOutputs=6".
  - The bare, package, import and root forms differ.
  - This shows the check can fail.
- **My own probe, `my_invocations.py`.**
  - Population: 7 forms × 13 argument sets = 91 pairs.
  - Forms:
    - `js`;
    - `bare`, which is extensionless;
    - `package` dir;
    - `abs-outside-cwd`;
    - `stdin-pipe`;
    - `import-pkg`;
    - `import-then-log`, a diagnostic form that imports the entry and then prints
      `process.exitCode`.
  - Argument sets:
    - `help`, `help-and-repo`, `none`, `unknown`, `bad-port`, `repo-no-value`, `repo-twice`;
    - `unreadable`, `relative-missing`;
    - `rejected-empty`, `rejected-gitinit`, `rejected-symlink`;
    - `rejected-watch-state`, which sets `--state-dir <scratch>/never-state`.
  - [Observed] 89 of 91 pairs are identical.
  - The 2 differences are both `import-then-log` × {`help`, `help-and-repo`}. Base prints
    `undefined` and head prints `0`. The process exit status is the same (see N4).
  - [Observed] After the run, `never-state` does not exist: a rejected binding created no state
    directory. (The record's key is misnamed `neverStateCreated` and holds `exists()` = `false`.)
- **stdin probe, `stdin_probe.py`.**
  - Population: an open-never-closed pipe and a PTY, × `--help`, `--frob`, unreadable,
    rejected = 8 pairs.
  - [Observed] 8 of 8 identical, and none hung within 15 s.
  - Head reads `process.stdin` eagerly when it builds `io`. That has no observable effect on these
    paths.

**Importing `poc-main.ts` (side effects)**

- [Observed] `import('apps/three-surface-poc/dist/poc-main.js')` exports `["main"]`.
  `process.exitCode` stays `undefined`.
- [Observed] The `SIGINT`/`SIGTERM` listener count is 0 before and 0 after.
- [Observed] Nothing is written to stdout or stderr. No active handle is left.
- [Observed] Under `strace -f`:
  - no child `execve`;
  - no `connect`, `mkdir`, `unlink` or `rename`;
  - 0 `openat` calls with `O_WRONLY`, `O_RDWR` or `O_CREAT`;
  - the only `.json` file opened is `package.json`.

**Reach of `deps`**

- [Observed] `git grep` at head finds `poc-main` imported only by:
  - `main.ts`;
  - `main.test.ts`;
  - the evidence harness `.txt`.
- [Observed] The package `exports` map exposes `"."` (`dist/main.js`) and `./dossier-render`.
  It does not expose `poc-main`.
- [Observed] `main.ts` calls `main(argv, io)` with no third argument, so `deps` defaults to
  `REAL_DEPS` (`poc-main.ts:85-94`). `REAL_DEPS` is not exported.
- [Inferred] Production therefore cannot inject `resolveBinding` or any other collaborator.

**Gate position (base `main.ts` against head `main.ts` + `poc-main.ts`)**

- **Indentation-insensitive block diff** (`block_diff.py`). [Observed] Every substantive edit is
  one of:
  - `process.*` → `io.*`;
  - collaborators → `deps.*`;
  - `process.exitCode = n` → `return n`;
  - sentinel empty strings removed;
  - the two observation copies merged into `observeCheckouts`/`observeCapture`;
  - `now: io.now`;
  - `buildRevision = capture.observerRevision`.
- [Observed] The order of operations is unchanged, both at start and on re-observation:
  1. repository;
  2. observer;
  3. clean check;
  4. horizon;
  5. clock.
- [Observed] Head (`poc-main.ts:103-127`) refuses in this order:
  1. help → 0;
  2. invalid → 1;
  3. `realpathSync(resolve(...))` failure → "configured repository is not readable", 1;
  4. `launchAfterPwbRepositoryBinding(repoRoot, deps.resolveBinding, (boundRepoRoot) => serveBoundRepository(boundRepoRoot, …))`;
  5. rejected → "authority rejected (${launch.reason})", 1.
- [Observed] Every observation, model build, daemon start and state-directory computation is inside
  `serveBoundRepository`. Only the launcher's continuation calls it.
- [Observed] The refusal strings are textually identical to base:
  - startup "observer-checkout-dirty";
  - re-observe "POC runtime inputs are dirty; re-observation was refused";
  - "daemon did not start (…)";
  - "observation failed (…)".
- [Observed] The horizon read stays outside the checkout `try` (`poc-main.ts:157`), as at base. The
  differential scenario `horizon-throws-at-start` pins this.
- [Observed] `pocObserverInputsAreClean` in `git-observation.ts` covers the prefix
  `apps/three-surface-poc/`, so the new `poc-main.ts` is covered.
- [Observed] `watch-mode.test.ts` adds `poc-main.ts` to `REOBSERVATION_SOURCES`.

**Old-versus-new differential**

- [Observed] Re-run of `run_differential.py`: base `1d6731bb`, harness sha `a93c6443…`, oldMain
  `470ff646…`.
- [Observed] Vitest exit 0; 44 tests, 44 passed.
- [Observed] My `cmp_transcripts.py`:
  - 42 of 42 scenarios have `old == new == entry`;
  - 39 distinct transcripts;
  - 37 transcripts byte-equal to the recorded transcripts file.
- The 5 that differ are `happy-default-state-dir`, `happy-pages`, `reobserve-ok`, `reobserve-dirty`
  and `watch-enter-reobserves`. They differ only in temporary paths and in body shas that embed
  those paths. [Inferred from the diffs]

**Mutants**

- **Recorded 27, `main-test-mutants`.** [Observed] Re-run at `20b23d90`: 27 of 27 killed. The
  fragments, outcomes and failing-test sets match the record in 27 of 27.
- **`limb_isolation.py`.** [Observed] Re-run reproduces the record's cells, with exits `[0,1,1,0,1]`.
- **My Enter-limb probe, `enter_limb.py`.**
  - [Observed] The mutant attaches the console unconditionally and sends its output to a
    `PassThrough`.
  - Under it, the "ignores Enter without --watch" test fails.
  - So the call-log/Enter limb carries weight on its own.
- **My 18 extra mutants against `main.test.ts`** (`extra_mutants.py`). [Observed] 10 survive:
  - `bound-locator-ignored`;
  - `revision-change-root`;
  - `reobserve-horizon-root`;
  - `session-clock`;
  - `state-dir-unresolved`;
  - `verbatim-reader-root`;
  - `materialize-target-root`;
  - `served-recorder-dropped`;
  - `credential-provision-dropped`;
  - `reevaluation-dropped`.
- **The same 18 against the differential harness.** [Observed] 6 survive:
  - `bound-locator-ignored`;
  - `reobserve-horizon-root`;
  - `session-clock`;
  - `verbatim-reader-root`;
  - `materialize-target-root`;
  - `served-recorder-dropped`.
- **Equivalence of `served-recorder-dropped`.** [Observed] `servedResponses` occurs twice in
  `poc-main.ts`: its declaration and its one use. `pocRoutes`'s `recorder` parameter defaults to
  `new ServedResponseRecorder()` (`routes.ts:205`), so the mutant is equivalent.
- **My 8 predicate mutants** (`predicate_mutants.py`, `out/predicate-mutants-main-test.json`).
  These mutate the condition, not the branch body. [Observed] All 8 killed, with 0 survivors:
  - `help-predicate-false`, 1 failing test;
  - `invalid-predicate-false`, 1;
  - `dirty-predicate-negated`, 12;
  - `started-predicate-false`, 1;
  - `error-class-predicate-true`, 1;
  - `error-class-predicate-false`, 3;
  - `watch-flag-negated`, 3;
  - `state-dir-default-always`, 1.
- **Restoration.** [Observed] `poc-main.ts` was restored and re-hashed after every run (`c5e5dc78…`).
  `git status --short` in `head` is empty.

**Dist compare**

- [Observed] Re-run of `dist-compare.mjs` base→head:
  - "common=90 {"byte-identical":41,"identical after normalisation":47,"differs":2} added=1 removed=1 recordReading=29 {"byte-identical":14,"identical after normalisation":15,"differs":0}"
  - "differs: main.js, polaris-narrative.js"
- [Observed] The `polaris-narrative.js` difference consists only of:
  - the deleted `MAX_ANCHORS_PER_BLOCK` declaration, its only occurrence in the base tree;
  - export removals, which normalise away.
- [Inferred] It is therefore behavior-preserving.
- [Observed] The app's `src` has 0 `import * as` and 0 dynamic imports of app modules. So
  un-exporting cannot change what a namespace import observes.
- See N2 for the selector.

**Route capture**

- [Observed] With my own fixture path, two base runs and one head run are byte-identical
  (`7ff5d8c8…`). The fixture revision `1f892687` was recreated.
- [Observed] With the recorded path `/tmp/zz-route-capture-fixture-repo`, the head run gives exactly
  the recorded `486bea4a0ab57d759a70fbd81f7543f979afc6d567c59b71f906c923cf6ff74c`.
  - That directory already existed; lane C left it.
  - I only read it.

**Sweeps**

- **Seam comments** (`seam_check.py`). [Observed] There are 90 `// Test seam:` comments in 37 non-test
  files under `apps/three-surface-poc/src`.
  - All 90 annotate an exported declaration, and every one's name occurs in a test file.
  - 2 names also occur in non-test code elsewhere; both are benign:
    - `PWB_AUTHORITY_ARTIFACTS` is parsed inside an object literal by
      `build_pwb_registry_machine_ceiling_amendment.py`;
    - `AdmissionRecordsPort` appears in a doc comment in `package-reader.ts`.
- **Un-exported and deleted names** (`unexported_names.py`).
  - Population: 165 names. This is my own extraction: every removed `export` declaration line in a
    non-test file under `apps/three-surface-poc/src` except `main.ts`, including the deleted
    `source-adapter.ts`, plus the export-list removals.
  - [Observed] 0 whole-word occurrences in 631 other tracked code files. Of those files, 121 are
    `.py`, and 115 of the `.py` files are outside `docs/evidence`.
- **Stale literals** (`stale_literals.py`).
  - Population: 357 removed lines.
  - [Observed] None appears in an executable file elsewhere, except the moved `main.ts` lines, which
    are now in `poc-main.ts`.
  - Old `export const` lines appear only in prose and in one dated mutants record. That record,
    `dossier-engine-exclusion-reasons-mutants.json`, pins `source-adapter` at `71af9aa8` and is not
    re-run by anything.
- **PR #499 sweep** (`git grep -l -F adapter-credential-declaration 20b23d90`).
  - Denominator: 3064 tracked files.
  - [Observed] 2 hits, both records themselves:
    - `docs/evidence/adapter-credential-declaration-sweep-2026-10-22.json`;
    - its sibling `…-differential-2026-10-22.json`.
  - No script, workflow or test names either file.
  - [Observed] Applying the sweep's own `linePattern` (`cred_hits.py`):
    - base `main.ts` hits lines `[50, 125, 159, 174, 182, 183]`, which matches the record;
    - head `main.ts` hits `[]`;
    - head `poc-main.ts` hits `[51, 172, 194, 209, 217, 218]`, the same six source lines moved.
- **Owner notice.** [Observed] `bd show syzygy-bpyt.10 --json` (read-only) has 0 matches for
  `bpyt\.5\.5|PR 501|#501`.
- **Record-reading selector** (`selector_sides.py`). See N2.

## 4. Round-1 findings

| Finding | Status | Evidence |
|---|---|---|
| F1 — entry guard changed exit code/output | **Repaired** | [Observed] The guard is gone. `main.ts` is unconditional and `poc-main.ts` has no import-time effect (strace). Invocation pairs: 30/30 identical, my 89/91 identical (diagnostic-only differences, N4) and stdin 8/8. The control at `4f3c3ebf` gives 10/30, so the check can fail. |
| F2(a) — classes | **Repaired** | [Observed] The PR body says: "**1 (P1 repository-binding composition) and 3 (`PocRuntimeCapture` composition)**, as ruled in R-GP-IMPL-POC-APP-HYGIENE-1". |
| F2(b) — bare `PocObservationError` | **Repaired** | [Observed] Two literal-stderr tests are present, and they kill `suffix-filter-dropped` in my re-run. |
| F2(c) — rule-6 per predicate | **Repaired** | [Observed] 27/27 recorded mutants killed on re-run. My 8 condition-level predicate mutants were all killed. The guard predicates no longer exist. The remaining survivors are argument wiring, not predicates (N1). |
| F2(d) — altered-prose limb mapping | **Repaired, with an overclaim** | [Observed] `gpq0ExtraChecks.alteredProseLimb` exists and reproduces. Its selector sentence is wider than its predicate (N2). The conclusion holds on the 90-module tally: 88 identical, and the 2 that differ are explained. |
| F2(e) — owner notice | **Open by design (non-blocking)** | [Observed] The PR body says: "the owner notice is left to the coordinator at landing". 0 mentions in `syzygy-bpyt.10`. GP-Q0 makes it non-blocking. It must be posted at landing. |
| N1 — parse-anchor comments / `.py` consumers | **Repaired** | [Observed] The two `governance-inputs.ts` comments name the scripts. The `install_redis_sitting.py` `GATE_COMMENT` regex starts at "// The policy act is the", so it is unaffected. My own sweep found 0 of 165 names in 631 code files, re-derived rather than copied. |
| N2 — `existsSync` limb could not fail | **Repaired** | [Observed] `limb_isolation.py` re-run gives exits `[0,1,1,0,1]`, as recorded. The fake daemon creates the state dir and refuses to start. |
| N3 — re-runnability | **Repaired, with residue** | [Observed] Commits are reachable. The fixture revision `1f892687` and its creation are recorded, and the recorded digest reproduces at the recorded path. Denominators are defined and every record has `ranAtCommit`. Residue: the dist-compare record names trees by path only, and the verification note is stale at `20b23d90` (N3). |
| N4 — type privacy | **Repaired** | [Observed] The census `method` states the policy. "53 of 100" is recomputed, not copied. |
| N5 — sleeps / seam notes | **Repaired, with residue** | [Observed] The `--watch` test uses `vi.waitFor`, and the no-watch test waits two `setImmediate` turns and checks the call log. There is one seam note each. Residue: timing margins (N5). |
| Rule 10 (figures re-derived?) | **Yes** | [Observed] The repair re-derives its own figures and does not copy round 1's: 90 common modules rather than round 1's 178-module population, 162 names with `.py` consumers, 91/80 and 91/79 denominators, and `Tests: +19 ~0 -9` against `b7697f6a`. |

## 5. New findings

No F-findings (blocking). Seven notes.

### N1 — note (low-medium; class-1/3 wiring) — the bound locator and four repository-rooted arguments survive both the shipped test and the differential

- **Evidence.**
  - [Observed] Five non-equivalent mutants of `poc-main.ts` survive both `main.test.ts` and the
    differential harness.
  - `bound-locator-ignored`
    - Old: `(boundRepoRoot) => serveBoundRepository(boundRepoRoot, parsed.config, io, deps)`.
    - New: `… serveBoundRepository(repoRoot, …)`.
  - `reobserve-horizon-root`
    - Old: `(pinned) => deps.observeGitHorizon(repoRoot, pinned)`.
    - New: `… (io.cwd(), pinned)`.
  - `session-clock`
    - Old: `now: io.now,`.
    - New: `now: () => new Date().toISOString(),`.
  - `verbatim-reader-root`
    - Old: `gitBlobReaderFor(repoRoot)`.
    - New: `gitBlobReaderFor(io.cwd())`.
  - `materialize-target-root`
    - Old: `targetRepoRoot: repoRoot,`.
    - New: `targetRepoRoot: io.cwd(),`.
  - [Observed] Four more survive `main.test.ts` but are killed only by the differential, which is
    not in CI: `revision-change-root`, `state-dir-unresolved`, `credential-provision-dropped` and
    `reevaluation-dropped`.
  - [Observed] Every branch predicate is killed, so the GP-Q0 "rule-6 mutant for each predicate"
    limb is met. These survivors are data flow.
  - [Observed] The block diff shows the same wiring textually at base: base reassigns
    `repoRoot = boundRepoRoot`. Base had no `main` tests at all. So this is a gap the new tests
    leave, not a behavior change.
- **Failure scenario.**
  - [Inferred] The real resolver returns `locator = realpath(resolve(configuredLocator))`
    (`git-observation.ts:44`). That equals `main`'s `repoRoot` except when a symlink in the path is
    re-pointed between the two `realpath` calls.
  - A later refactor that passes the configured path instead of the bound locator, or roots the
    re-observation horizon, the verbatim blob reader or the materialize target at the observer
    checkout, would pass CI.
  - The materialize target fails closed. [Inferred from
    `packages/three-surface-poc-core/src/materialization.ts:327-330`] The core refuses with
    "target repository mismatch" when the packet's `targetRepoRoot` and the action's differ. So
    that mutant disables the human materialize action silently, and no test sees it.
  - The other roots have no such backstop.
  - The PWB-REQ-001 binding ("bind the complete source-path population to the configured
    repository's exact Git revision") would then rest on an untested argument.
- **Proposed fix.** In a follow-up bead:
  - Add a `main.test.ts` case whose fake `resolveBinding` returns `{ kind: 'bound', locator: '<other>' }`.
    Assert that every repository-rooted collaborator receives `<other>`: `observeGitRepository`,
    `observeGitHorizon` at start and on re-observe, `observeRevisionChange`, the model's `repoRoot`,
    and the default state-dir digest input.
  - `poc-main.ts` passes no `runQuery` or `runCreate` to `materializeRoutes`, so a `main`-level
    test cannot fake `bd`. Instead:
    - add `materializeRoutes` to `PocMainDeps`, defaulting to the real one in `REAL_DEPS`;
    - in the test, capture the options it receives;
    - assert `targetRepoRoot` and `stateDir()`;
    - call the captured `onMaterialized`, then assert the horizon root and the injected `io.now`
      instant on the next evaluation.
  - Add one verbatim-route request on a fake whose blob reader records its root.
  - Record the five mutants above as killed (old/new fragment and commit).

### N2 — note (low; evidence wording) — the `alteredProseLimb` selector is evaluated on the head side only and misses package-mediated readers

- **Evidence.**
  - [Observed] `dist-compare.mjs:72` evaluates the predicate on the head emission only:
    `const readsFiles = /from ['"]node:(?:fs|fs\/promises|child_process)['"]/.test(h);`
  - The record's `predicate` string does not say "head". The `mapping` says the selected modules
    are "the modules that can read a record or observed text".
  - [Observed] `selector_sides.py` over the 90 common modules:
    - "predicate on base 30 differ ['main.js']";
    - "predicate on head 29 differ []";
    - "base-only matches ['main.js']".
  - Base `main.ts:2` imports `realpathSync` from `node:fs`. So the one common module that differs
    and matched the predicate at base falls out of the 29 by construction.
  - [Observed] "common modules importing a core package and not selected 12". These include
    `production-reobserve.js`, which reads materialization and test-artifact records through
    `@syzygy/three-surface-poc-core` and imports no `node:fs`.
  - [Observed] The conclusion survives on the unselected tally. Of 90 common modules, 88 are
    byte-identical or identical after normalisation. `main.js` is covered by the differential, and
    `polaris-narrative.js` differs only by the deleted dead constant. The mapping names both.
- **Failure scenario.**
  - A later PR copies "of 29 record-reading modules, 0 differ" as its altered-prose discharge.
  - It relies on a selector that excludes a module because the PR removed its `node:fs` import.
  - It also misses any reader that goes through a package port.
- **Proposed fix.**
  - In the dispositions record, restate the limb on the 90-module tally: 88 identical, 2 differ, both
    explained. Disclose that the 29-module selector is head-side and import-based.
  - For later uses of `dist-compare.mjs`:
    - evaluate the predicate on either side;
    - add modules that import a record-reading package export;
    - or drop the selector and argue from the full tally.

### N3 — note (low; rule 11) — the dist-compare record names its trees by path, and the verification note is stale at the reviewed head

- **Evidence.**
  - [Observed] `dist-compare-2026-10-22.json` `trees` holds two paths and no commit and no
    `ranAtCommit`:
    - base: `…/scratchpad/lane-c/p501/base`;
    - head: `/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-bpyt.5.5`.
  - [Observed] `verification-2026-10-22.json` `subject.note` says: "the pushed head differs from it
    only by files under docs/evidence/poc-hygiene-2026-10-22/ (this record set)".
  - [Observed] At `20b23d90` that note is false. `fa79bca6..20b23d90` touches 26 files, including:
    - two `packages/three-surface-poc-core` test files;
    - `docs/README.md`;
    - `docs/reviews/R-GP-IMPL-NON-HUMAN-PINS-1-RAW.md`;
    - the non-human-pins evidence.
  - [Observed] The PR body states the merged difference correctly. No `apps/` path differs.
  - [Observed] My re-run of the dist compare at `1d6731bb`/`20b23d90` reproduces the record.
- **Failure scenario.** A reader of the record alone cannot tell which commits the 41/47/2 tally
  describes. A reader of the verification note alone believes the PR's `packages/` bytes were
  covered by the runs.
- **Proposed fix.** The dispositions record names:
  - the dist-compare trees as `b7697f6a` (base) and `fa79bca6` (head);
  - this review's reproduction at `1d6731bb`/`20b23d90`;
  - the corrected scope of the verification note.

  Future `dist-compare.mjs` records should write `git rev-parse HEAD` for each tree.

### N4 — note (low; disclosure) — head sets `process.exitCode = 0` where base left it `undefined`

- **Evidence.**
  - [Observed] `main.ts:7` assigns `process.exitCode = await main(…)` unconditionally.
  - Base set `process.exitCode` only on failure paths (base `main.ts:61,68,94,171,211,218`).
  - [Observed] My `import-then-log` form prints `undefined` at base and `0` at head after `--help`.
    The process exit status is 0 in both.
  - [Inferred] The same holds after a clean `SIGINT` shutdown.
- **Failure scenario.**
  - Only an in-process importer that reads `process.exitCode` can see it.
  - No GP-Q0 output changes: the exit code is identical. But the PR body's "Changed outputs:
    **None.**" is unqualified.
- **Proposed fix.** The dispositions record lists this under changed outputs as "in-process
  `process.exitCode` now `0` on success paths; exit status unchanged". No code change.

### N5 — note (low; test timing) — `vi.waitFor` timeout equals the test timeout, and `started()` polls without a bound

- **Evidence.**
  - [Observed] `main.test.ts:339` reads
    `await vi.waitFor(() => …toContain(refusal), { timeout: 5000 })`.
  - Vitest 3.2.7's default `testTimeout` is 5000 ms, and none is configured for this project.
  - [Observed] `main.test.ts:142`'s `started()` polls every 5 ms with
    `while (fake.registered() < 2)`, with no stop condition.
  - When `run` settles first, the race resolves to `'finished'` and the assertion fails, but the
    polling loop keeps scheduling timers until the worker exits.
- **Failure scenario.**
  - Under the host load the brief describes, the `--watch` test fails with "Test timed out in
    5000ms" instead of the `waitFor` assertion diff. That hides which expectation was unmet.
  - A finished-early run leaves a live timer loop in the worker.
- **Proposed fix.**
  - Set the `waitFor` timeout below the test timeout, or give that test an explicit larger timeout
    (for example `it(..., 15000)` with `waitFor` at 10000).
  - Give `started()` a `let done = false` flag that the `run.then` arm sets, and exit the loop on it.

### N6 — note (low; dated record) — the PR #499 adapter-credential sweep record names `main.ts` lines that now sit in `poc-main.ts`

- **Evidence.**
  - [Observed] No check, script, workflow or test re-runs or reads the record: 2 tracked files of
    3064 contain `adapter-credential-declaration`, both of them records.
  - [Observed] Its builder exists only as embedded `sweepSource`/`builderSource`. That code asserts
    `set(hits) == set(classified)` and places `apps/three-surface-poc/src/main.ts` in the class "the
    cap1 machine credential, which authenticates clients to Syzygy and is not one Syzygy holds for a
    typed adapter".
  - [Observed] The hits moved one-to-one, as listed in section 3.
- **Failure scenario.**
  - Nothing goes stale silently today.
  - A future regeneration fails loudly on the `assert`, with `poc-main.ts` unclassified, and lists
    `main.ts` with no hits.
- **Proposed fix.**
  - A disposition is enough for this PR; the record is dated and must not be edited.
  - At the next regeneration, put `apps/three-surface-poc/src/poc-main.ts` in that same class in
    place of `main.ts`.

### N7 — note (low; housekeeping) — the route-capture digest depends on a persistent path outside any scratch area

- **Evidence.** [Observed] The recorded `486bea4a…` reproduces only with the fixture at
  `/tmp/zz-route-capture-fixture-repo`, and that directory persists. My own fixture path gives
  `7ff5d8c8…`, the same for base and head. Lane C left the directory, not me.
- **Failure scenario.**
  - The directory is a leftover against bead guardrail 7: "Delete scratch clones when done".
  - Once it is deleted, the recorded digest still reproduces, because the script recreates the
    revision. But the record's whole-file digest can never be checked from any other path.
- **Proposed fix.**
  - Delete the directory after landing.
  - For future captures, hash the transcript with the fixture path replaced by a placeholder, so
    the digest is path-independent. Keep the raw digest beside it.

## 6. Every changed output

| Output | Changed? | Evidence |
|---|---|---|
| Rendered bytes (fixture capture, 230 responses, 19 routes, 5 models) | No | [Observed] head = recorded `486bea4a…` at the recorded path. Base ×2 = head (`7ff5d8c8…`) at my path. |
| Live Butlers pages | [Unknown] | Not captured, by constraint: no repository body may be read. Any `src` edit changes the live surface version. |
| Wire format / routes / credential classes | No | [Observed] The route list and daemon options are deeply equal in all 42 differential scenarios. The route capture is identical. |
| Refusal strings, stdout/stderr | No | [Observed] Differential 42/42. Invocations 30/30 and 89/91. The 2 differences are my diagnostic printing of `process.exitCode`, not stdout or stderr from the entry. |
| Exit codes | No | [Observed] Same pairs as above. |
| In-process `process.exitCode` | Yes, from `undefined` to `0` on success | N4. |
| Emitted JS | 2 of 90 common modules differ, 1 added, 1 removed | [Observed] `main.js` is the composition root and is covered by the differential. `polaris-narrative.js` lost the dead constant. `poc-main.js` is added. `source-adapter.js` is removed; it has no importer, and my 165-name sweep found 0 uses. |
| Public package surface | Type-only un-exports | [Observed] `./dossier-render` still exports `renderDossier`, and its 5 dependents pass (181). |
| Signed or digest-bound artifacts | No | [Observed] There are no edits under `.syzygy/**` or `openspec/**` in the 89-file diff. `check_governance` reports 0 FAIL, the same as base. `check_quotations` is identical to base. Both ceiling `--check` scripts pass. |
| Consent / security / retention decision | No | [Observed] The P1 gate is in the same position with the same rejection string. No `REAL_DEPS` injection reaches production. A rejected binding creates no state directory. |
| Test list | +19 ~0 −9 | [Observed] §3. |

## 7. Verdict per acceptance criterion

1. **"main.ts exports main(); a test drives it with a fake io (one behavior gate)."** — **Met as
   amended by the coordinator's F1 ruling.**
   - [Observed] `main` is exported from `poc-main.ts`, not `main.ts`. That is the preferred arm the
     coordinator recorded: "move `main` into a side-effect-free `poc-main.ts`, keep `main.ts` an
     unconditional entry".
   - `main.test.ts` drives it with a fake `PocIo` through the P1 gate (18 tests).
2. **"Unused-export sweep (method stated) shows only deliberate test seams remain, each
   commented."** — **Met, with the declared exceptions.**
   - [Observed] The census method is stated, and my seam check confirms all 90 comments.
   - The declared exceptions are:
     - `polaris.ts` and `public-source-screening.ts`, untouched by instruction;
     - the `test-*.ts` support modules, which have module-head comments;
     - one export in `pwb-mutation.ts`, because the mutation runners are left alone by instruction.
3. **"Orphan modules deleted or wired; suite and rendered bytes unchanged."** — **Met on fixtures.**
   - [Observed] `source-adapter.ts` and its test are deleted, and nothing references the module.
   - The suite passes: the app project is green, and −9 is exactly the deleted test file.
   - The fixture rendered bytes are identical.
   - Live pages are [Unknown] by constraint.

## 8. Test quality

- **Literal expectations.**
  - [Observed] `main.test.ts` asserts exact stderr strings, for example
    `'syzygy POC: POC runtime inputs have uncommitted changes\n'` and
    `'syzygy POC: a required git revision could not be observed (git exit 128)\n'`.
  - It asserts exact call logs, for example
    `` [`bind ${repoRoot}`, `observe ${repoRoot}`, `observe ${OBSERVER_ROOT}`] ``.
  - These are literals, not values imported from `poc-main.ts`.
- **One host-dependent alternation.**
  - [Observed] The "shipped collaborators" test accepts
    `(locator-mismatched|binding-unreadable)`. Which one appears depends on whether the approved
    locator exists on the host.
  - The real resolver calls `realpath` on the approved locator, which is metadata only, and rejects
    before any `git` call. No body read. Acceptable.
- **Fixtures.** [Observed] They are built in `beforeAll` (`main.test.ts:29`). Nothing is built at
  describe time, so a fixture throw cannot report zero tests.
- **Gate-bypass isolation.** [Observed]
  - `launcher-gate-bypassed` and `pre-gate-state-directory-write` are killed.
  - `limb_isolation` reproduces the record: the `existsSync` limb alone kills a bypass, and the old
    fake could not.
- **Enter limb.** [Observed] It carries weight alone (`enter_limb.py`).
- **Timing.** [Observed] There are no fixed sleeps. The remaining margins are in N5.
- **Coverage gaps.** [Observed] Data-flow wiring after the gate is not pinned (N1). Every branch
  predicate is pinned: 27 recorded mutants plus my 8 predicate mutants and 4 predicate-adjacent
  extras, all killed.
- **Load.** [Observed] No 5 s timeouts occurred in any of my runs, so none needed an isolation
  re-run.

## 9. Cleanup

- I deleted the scratch clones `rev-501b/head`, `rev-501b/base` and `rev-501b/r1`, and the run area
  `rev-501b/tmp`, after this file was written. Before deleting, `git status --short` in `head` was
  empty.
- My scripts (`rev-501b/scripts/`) and outputs (`rev-501b/out/`) remain beside this raw so the
  figures above can be re-checked.
- I did not touch `/tmp/zz-route-capture-fixture-repo` (lane C's; N7).
- No `bd` mutation, push, PR comment or merge was made.
- Nothing under `/home/tze/GitHub/syzygy/.worktrees/` or the main checkout was edited.
  - One `npx vitest run` was invoked by mistake with the main checkout as its working directory.
  - It found no test files and exited 1 without writing anything.
