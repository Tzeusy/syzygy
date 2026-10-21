# R-GP-IMPL-POC-APP-HYGIENE-1 — CC-REV-1 implementation review of syzygy-bpyt.5.5, round 1
Verdict: REVISE
Reviewed commit: 4f3c3ebf
Subject: r1-review.diff sha256 fbbfadfd7b5b6ca2bc345528797f2d5b45eb0162d8a0db960e3f5a3c34138e78

Reviewer: rev-501, fresh context, default model. Date: 2026-10-22.
PR #501, branch `agent/syzygy-bpyt.5.5`, base `26ff52ce260e925b191d03ee78b052383328b65c`,
head `4f3c3ebf249c70dc3f22af843b336edd90c5ed4e`.
No target repository content was fetched or read. Every probe used the app's own
fixtures or a scratch fixture repository I created (`git init` plus one empty commit).

## 1. Subject identity checks

- [Observed] `git diff 26ff52ce260e925b191d03ee78b052383328b65c 4f3c3ebf249c70dc3f22af843b336edd90c5ed4e`,
  run by script in my head clone, hashes to sha256
  `fbbfadfd7b5b6ca2bc345528797f2d5b45eb0162d8a0db960e3f5a3c34138e78`. That equals the brief's digest
  and the subject file's digest. `--name-only` lists 75 files.
- [Observed] `gh pr view 501 --json headRefOid` returns `4f3c3ebf249c70dc3f22af843b336edd90c5ed4e`.
- [Observed] In my clone, the merge base of the head with the fetched `origin/main` is `26ff52ce`.
  `origin/main` has moved since: `git ls-remote` HEAD was `b7697f6a` during this review. Under
  rule 7 every result below holds for `4f3c3ebf` only. The merge result was not tested.
- Clones: `rev-501/head` was checked out at `4f3c3ebf`, and `rev-501/base` at `26ff52ce`. Each got
  `npm ci` and then `npm run build:poc`. Every test and script ran with the clone as its cwd
  (`env -C <clone> …`).

## 2. Clauses relied on (quoted)

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:18-20, 31-39, 45-47`):
  "Changes touching any of seven classes require review by an independent, fresh-context reviewer,
  and the agent performing the change never finally decides which classes it touches."
  "1. **authority boundaries** — write-universe, typed-authority table, adapter authorization
  (VIS-5, VIS-6);" "3. **deterministic observation** — snapshot composition, evaluation identity,
  the deterministic/inferred seam (VIS-7);" "4. **security** — anything under SEC-1…SEC-5, auth
  surfaces, egress paths;" "6. **public interface** — machine-queryable endpoints, adapter
  contracts, anything an external consumer can depend on;" "A reviewer or the owner may reclassify
  at any time."
- **GP-Q0, part 1**
  (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:52-55`):
  "\"Behavior-preserving\" means none of the following changes: a rendered byte, a wire format, a
  refusal string or an exit code; a signed or digest-bound artifact; a consent, security or
  retention decision."
- **GP-Q0, review rule** (same file, lines 61-66): "Some pull requests also get three further checks:
  **Which ones:** pull requests touching class 1 (authority boundaries), class 3 (deterministic
  observation) or class 4 (security), and class-6 pull requests that remove an endpoint. **The
  checks:** an old-versus-new differential over a mutated-record corpus that includes records with
  altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle
  report."
- **GP-Q0, part 3** (same file, lines 95-96): "Any change not listed here to what a gate accepts or
  refuses stops and returns to the owner."
- **PWB-REQ-005**
  (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:640-646`):
  "The POC SHALL NOT read any Butlers project-shape body until each of the exact per-repository
  observation-consent record, the observing Syzygy project's concrete secret-detection/classification
  policy and the project-shape observer's governance-plane adapter-registry entry carries an
  effective human owner act under RFC3-16(a) …"
- **AGENTS.md verification rules** (at `4f3c3ebf`): 6 "Mutate the input and confirm the check fails,
  per predicate, before trusting it"; 7 "Run the battery in a clone before calling it green; the
  report is valid only for that commit."; 11 "An evidence record names its subject and the
  subject's digest; a record that names neither cannot be re-checked against the bytes it
  describes."
- **Bead syzygy-bpyt.5.5 acceptance criteria** (`bd show … --json`, read-only): "1. main.ts exports
  main(); a test drives it with a fake io (one behavior gate). 2. Unused-export sweep (method
  stated) shows only deliberate test seams remain, each commented. 3. Orphan modules deleted or
  wired; suite and rendered bytes unchanged." From the bead description: "Anything else that would
  change rendered bytes, a wire format, a signed or digest-bound artifact, a spec, or a consent,
  security or retention decision is out of scope: stop and return it to the owner as a new
  decision bead under syzygy-bpyt.1."

## 3. What I ran and the results

Tests and checks (head unless stated):

- [Observed] `npx vitest run apps/three-surface-poc/src/main.test.ts` →
  "✓ |@syzygy/three-surface-poc-app| apps/three-surface-poc/src/main.test.ts (16 tests)".
- [Observed] The three-surface-poc vitest project →
  " Test Files  88 passed | 1 skipped (89)" / "      Tests  1084 passed | 2 skipped (1086)".
- [Observed] The PWB-REQ-014 authority sweep (`polaris-authority-sweep.test.ts`) →
  "✓ |@syzygy/three-surface-poc-app| apps/three-surface-poc/src/polaris-authority-sweep.test.ts (5 tests)".
- [Observed] The five `packages/polaris-dossier` test files that import the changed
  `dossier-render.ts` → "Tests  19 passed (19)" (close, execution-flags) and
  "Tests  162 passed (162)" (render, run-evidence, waiting-sessions).
- [Observed] `npm run typecheck` (after `npm run build:poc`) exited 0.
- [Observed] `python3 scripts/check_governance.py`, at base and at head →
  "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted". The two outputs differ only
  in file counts (3024→3036 files; CG-2a 1924→1929; CG-3 1806→1807).
- [Observed] `python3 scripts/check_quotations.py`: the base and head outputs are byte-identical
  (`cmp` silent). The first line at head reads "OK    QC-1  a quotation beside a path:line locator was said by
  that file — 33 quotations examined in 15 of 918 .md files scanned … 0 findings".
- [Observed] `python3 scripts/record_pwb_registry_machine_ceiling_act.py --check` → "P-114 record,
  approved registry row, retained review/selection and one aggregate block regenerate exactly."
  `python3 scripts/build_pwb_registry_machine_ceiling_amendment.py --check` →
  "pwb-registry-machine-ceiling-amendment: applied, verifies". Both scripts parse
  `governance-inputs.ts` (see N1).
- [Observed] The `GATE_COMMENT` regex of `scripts/install_redis_sitting.py:1042`, applied to
  `governance-inputs.ts`, matches once at base and once at head, and the two matches are
  identical. `install_redis_sitting.py --check` cannot run in this tree:
  "REFUSED: required act records are missing (nothing written)". That is a precondition unrelated
  to this PR.
- [Observed] `npx vitest list`: base 4904 tests, head 4911. By full name, the head adds 16
  (`main.test.ts`) and removes 9 (`source-adapter.test.ts`), which matches "Tests: +16 ~0 -9".
- `SYZYGY_FRESH_CLONE=1 npm run test:system`: **not run**. [Observed] Among the system tests,
  `packages/cap1-system/src/daemon-entry-unchanged.system.test.ts:205` is the only one that names the
  app. It asserts a literal `dossier-render` import line in `apps/syzygy/src/main.ts`. No system
  test starts the POC app, so the brief's condition for running the suite is not met.

Removals, re-derived:

- [Observed] My own diff classifier (`classify_diff.py`) covers the `src` diff without `main.ts`,
  `main.test.ts` or the deleted adapter. It finds 160 removed `export` keywords, one export-list
  edit (`readText` in `governance-inputs.ts`), one deleted constant (`MAX_ANCHORS_PER_BLOCK`) and
  95 added comment lines (90 `Test seam`, 5 `Test support`). `main.ts` adds 2 more `Test seam`
  lines, for 92 in all. My un-export list of 161 names equals the census record's list exactly.
- [Observed] Importer sweep: I ran `git grep -w -F` for each of 162 names (161 plus the deleted
  constant) over the 3032 tracked files at head. Hits occur only in `.md` and `.json` files under
  `docs/`, reviews and candidates. No code file (`.ts .mts .mjs .js .cjs .py .sh`) outside the
  declaring file names any of them. Among the 178 JS files emitted to `dist` in both trees, 0
  import an app module as a namespace.
- [Observed] Fragment check: I extracted the string literals from the 616 tracked code files and
  tested them against the head sources. None of them is a mutation-runner or script fragment that
  existed at base and is missing at head, apart from generic short strings. Separately, the
  literal `export const PWB_ACT_RECORDS` and `export const PWB_SUPERSEDED_ACT_RECORDS` anchors
  that three Python scripts read are still present (N1).
- [Observed] `dist` comparison over the 178 common emitted JS files: 129 byte-identical; 47
  identical once the `export` keyword and the seam comments are removed (`governance-inputs.js`
  among them, with its export list); 2 differ in substance. Those two are `main.js` (the rewrite)
  and `polaris-narrative.js` (the dead constant removed). `source-adapter.js` is gone.
- [Observed] Citers of `polaris-generation/source-adapter.ts` at head:
  `R-PUBLIC-SOURCE-SCREENING-SCOPE-3-RAW.md:192,242` and `-4-RAW.md:165` (retained raws in the
  candidate package, written "At the reviewed commit"),
  `docs/evidence/dossier-engine-exclusion-reasons-mutants.json` (a rule-6 record that names its
  own commit and the adapter's digest) and `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md:50`
  (a research note dated 2026-10-03 at `ef5d5f03`). I hashed each of the four citing files and
  searched for each 12-hex prefix: 0 tracked files contain one. The package manifest
  `PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt` has one row, the policy JSON. No digest-bound file
  pins the adapter's path, and the PR edits none of the four citers. The deletion is inside GP-Q0
  part 1 [Inferred from the above, the JS comparison and the identical captures].
- [Observed] Census re-run (`export_census.py`, sha256 matching the record). Base: 561 exports;
  3 dead, 268 prod, 167 self-only, 123 test-only. Head: 398; 1 dead, 272 prod, 5 self-only,
  120 test-only. The 120 test-only split into 92 with a comment, 17 in `test-*.ts` support
  modules, 10 in `polaris.ts` and `public-source-screening.ts`, and 1 in `pwb-mutation.ts`. The 6
  remaining dead or self-only exports all sit in `polaris.ts` and `public-source-screening.ts`.
- [Observed] The comment-stripping correction holds. At `redis-shaped-measure.ts:11`, the regex
  literal `/^[ /*[]/u` opens a false block comment under the census stripper, which hid the uses
  at lines 14 and 76. `RedisShapedMeasurement` is still exported at head, which is correct.

Behavior:

- [Observed] Route capture: I ran the lane's `route-capture.mjs` (sha256 matches its record)
  against my own fixture repository at revision `1f892687d53c829f9c2a4ee99bccccb23d6158df`. It
  produced: base run 1, base run 2 and head, all with whole-file sha256 `3d8a78dd…`. The capture
  has 230 responses: 5 fixture variants × 46 request keys. Every route is requested in direct and
  tailnet Host forms, and machine routes as bearer and anonymous. Statuses: 200×150, 401×40,
  403×20, 502×20.
- [Observed] Distinctness: the 5 variants are pairwise distinct. Of the 46 keys, 26 give 5
  distinct bodies across the variants, 4 give 4, and 16 give one body (the 401/403/502 refusals).
  Over 230 responses there are 73 distinct bodies.
- [Observed] The recorded capture digest `760f650e…e9cf` does not reproduce here: 80 of my 230
  responses match the recorded per-response digests and 150 differ. The record does not name the
  fixture repository's revision (N3). Base and head agree byte for byte under one fixture
  revision, and that is the claim that matters.
- [Observed] Scope of the capture: it builds `pocRoutes(() => model)`, `materializeRoutes` and
  `reobserveRoutes` on a private daemon (`port: 0`). It does not run `main`'s own composition,
  which passes the verbatim reader factory, `ServedResponseRecorder`, the credential-provision
  callback and `session.latest`. That composition line is byte-identical between base `main.ts:159`
  and head `main.ts:196`, and the differential records the route list in every scenario.
- [Observed] Differential re-run: I ran the retained harness
  `main-old-vs-new-differential.test.ts.txt` (sha256 `7117e3a4…`, matching the record) as a vitest
  file at `4f3c3ebf`. The old script was a copy of base `main.ts` (sha256 `470ff646…`, matching the
  record's `oldMain`). 44 tests passed, and old and new were deeply equal in 42 of 42 scenarios.
  Five transcripts differ from the recorded ones only in their temporary paths.
- [Observed] Mutant re-run: all 24 `mutate_main.py` mutants against `main.test.ts` at `4f3c3ebf`
  were killed, with the recorded failing-test sets and the recorded fragments (output
  "survivors: []").
- [Observed] My own per-predicate mutants against `main.test.ts` at `4f3c3ebf`
  (`predicate_mutants.py`, `main.ts` sha256 `5fc4e364…`, restored and re-hashed afterwards).
  Killed: P-help, P-invalid, P-rejected, P-dirty, P-not-started, P-closing, P-observation-error,
  P-readiness, P-state-dir-default. **Survived** ("Tests  16 passed (16)"):
  - P-suffix-filter: `.filter((part): part is string => part !== undefined)` →
    `.filter((part): part is string => true)`;
  - P-entry-argv-undefined: `if (script === undefined) return false;` → `if (true) return false;`;
  - P-entry-equality: `return realpathSync(script) === realpathSync(fileURLToPath(import.meta.url));`
    → `return false;`;
  - P-entry-guard: `if (isEntryScript()) {` → `if (false && isEntryScript()) {`.
- [Observed] Real process, base against head, `node apps/three-surface-poc/dist/main.js` with
  `--help`, `--bogus`, `--repo /no/such/zz`, and `--repo <fixture repo>` (refused by the binding
  gate): same stdout, stderr and exit code in each pair.
- [Observed] Real process, other invocation forms (F1). At head,
  `node apps/three-surface-poc/dist/main --repo /no/such/zz` prints nothing and exits 0. At base the
  same command prints "syzygy POC: configured repository is not readable" and exits 1. At head
  `node apps/three-surface-poc --help` (the package directory, resolved through `"main"`) prints
  nothing and exits 0. At base the same forms print the usage or refusal.
- [Observed] Import: `node -e "await import('<head>/apps/three-surface-poc/dist/main.js')"` prints
  nothing and leaves `process.exitCode` undefined. At base, importing runs the script, which
  prints "--repo is required…" and exits 1. The PR intends this change and discloses it.

Gate trace (base `main.ts`, top-level script; head `main()` and `serveBoundRepository()`):

- [Observed] Order on both sides: parse → `realpathSync(resolve(repo))` (refusal "configured
  repository is not readable", exit 1) → `launchAfterPwbRepositoryBinding(repoRoot, resolveBinding,
  continuation)` (refusal "configured repository authority rejected (<reason>)", exit 1) → inside
  the continuation only: observe repository, then observer (`cwd`), then the dirty check
  ("observer-checkout-dirty") → horizon → clock → state directory → session and model →
  observatory → daemon. Re-observation keeps the same order: repository, observer, dirty check
  ("POC runtime inputs are dirty; re-observation was refused"), horizon, clock.
- [Observed] Every serving path sits inside the continuation that `launchAfterPwbRepositoryBinding`
  calls only on `kind: 'launched'`. `launcher.ts` changed in one way: `LauncherBindingResult` lost
  its `export`.
- [Observed] `deps` (`PocMainDeps`, which includes `resolveBinding`) is injectable only through
  `main`'s third parameter. The only production call is the entry guard's, and it passes no
  `deps`, so the default `REAL_DEPS` applies. The package `"."` export resolves to `dist/main.js`.
  I ran `git grep` over the tracked `.ts .mts .mjs .js .cjs .json` files for the package name. No
  file imports `@syzygy/three-surface-poc-app` without a subpath. The only import sites,
  `apps/syzygy/src/main.ts:258` and `:270`, both import `/dossier-render`. [Inferred] A caller that
  could pass a fake `resolveBinding` already runs code in-process with full filesystem access, so
  the seam opens no new path past the gate.
- [Inferred] At base, an empty revision string from `observeGitRepository` would have skipped
  serving (the `''` sentinel). The head has no such check. `observeGitRepository` returns
  `git rev-parse` output or throws, so this path cannot be reached.
- [Inferred] A horizon failure at startup sits outside the try on both sides. Each becomes an
  unhandled rejection with exit code 1; only the stack frames differ.

## 4. Findings

### F1 — blocking — the entry-script guard changes the exit code and silences output for two invocation forms, and none of its predicates is tested

- **Evidence.** [Observed] Head `main.ts:253-272` runs `main` only when
  `realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url))`, and returns
  false whenever `realpathSync` throws. Node puts the path as typed into `argv[1]`, not the file
  it resolved. So `node apps/three-surface-poc/dist/main …` gives an `argv[1]` with no `.js` and
  `realpathSync` throws. `node apps/three-surface-poc …` gives the package directory, which never
  equals `main.js`. In both cases the process exits 0 with no output. Base gave the same
  refusal/usage output and exit code as the `.js` form (§3). Three of the four mutants that
  survive `main.test.ts` are this guard's predicates (P-entry-argv-undefined, P-entry-equality,
  P-entry-guard). No recorded mutant touches the guard: the 24 in `main-test-mutants-2026-10-22.json`
  and the 24 in `main-differential-2026-10-22.json` all target `main` and `serveBoundRepository`.
  The PR body says "Changed outputs: **None.**", and GP-Q0 part 1 counts an exit code as an output.
- **Who calls these forms.** [Observed] None in the repository. `package.json:16` (`npm run poc`),
  `fresh-checkout-demo-main.ts:98`, `restart.ts:79`, `build-output.test.ts:47` and
  `openspec/changes/three-surface-poc-experience/tasks.md:88` all use the `.js` path, so the
  documented and scripted runs are unchanged.
- **Failure scenario.** An operator or wrapper runs `node apps/three-surface-poc --repo <path>` or
  drops the extension. At base this either ran the POC or refused with exit 1. At head it does
  nothing and exits 0, so a supervisor or script treats it as success and nothing serves. The
  guard also fails open on every error, because `catch { return false; }` turns any realpath
  failure into a silent no-op. A future change to the guard (for example to `import.meta.main`,
  which [Unknown] may not exist at the `engines` floor `"node": ">=22.15"`) would go unnoticed by
  the suite.
- **Proposed fix (preferred).** Remove the guard. Move `main`, `serveBoundRepository`, `PocIo`,
  `PocMainDeps` and `REAL_DEPS` into a side-effect-free module such as `src/poc-main.ts`.
  `src/main.ts` stays the unconditional entry: one import, then
  `process.exitCode = await main(process.argv.slice(2), { …real io… })`. `main.test.ts` imports
  from `poc-main.ts`. Every invocation form, `restart.ts`'s expected script and the package `"."`
  export then behave exactly as at base, and nothing is left to mutate.
  **Alternative.** Keep the guard, but resolve `argv[1]` the way Node does before comparing (for
  example `createRequire(import.meta.url).resolve(resolve(argv[1]))` inside the try). Add tests
  for the `.js` form, the extensionless form, the package directory, a symlink, an undefined
  `argv[1]` and an unrelated script, and record each predicate's mutant.
  Either way, re-run the 42-scenario differential and the mutants at the new head and record
  them, and correct the PR body's "Changed outputs" line, which should name the import change
  either way. If the guard is kept with its current behavior, the exit-code change falls outside
  GP-Q0 part 1 and is not listed in part 3. Under the bead's own text it then goes to the owner
  as a decision bead under `syzygy-bpyt.1`.

### F2 — blocking — the PR touches classes 1 and 3, not "none", and two of the GP-Q0 extra checks are incomplete

- **Classification (my ruling under CC-REV-1).**
  - **Class 1, touched.** [Observed] `main.ts` composes the P1 repository-binding gate
    (`launchAfterPwbRepositoryBinding` with `resolvePwbRepositoryBinding`). That gate decides which
    repository the project-shape observer adapter may observe at all, which is "adapter
    authorization". The PR rewrites that composition and makes `resolveBinding` an injectable
    parameter.
  - **Class 3, touched.** [Observed] `observeCapture` and `observeCheckouts` now hold the only
    composition of `PocRuntimeCapture`: repository and observer revisions, the working-tree digest,
    and the evaluation evidence instant plus horizon. That capture is the evaluation-identity input
    for both the initial evaluation and every re-evaluation. The PR merges the two copies into one,
    which is "snapshot composition, evaluation identity".
  - **Class 4, not touched in substance.** [Observed] No change to authentication (the routes and
    their credential classes are byte-identical in the capture), egress, secret handling or the
    credential banner. The refusal strings that the PR calls "class 4 adjacent" are pinned by the
    differential.
  - **Class 6, not touched in substance.** [Observed] No route or endpoint is added or removed.
    The private package's `./dossier-render` subpath lost the type exports `RenderedDossier` and
    `stopReasonLabel`, and no code file imports either. Its only consumers, `apps/syzygy/src/main.ts`,
    `scripts/dossier_scale_measure.mjs` and the `polaris-dossier` tests, use `renderDossier`, which
    is still exported (162 + 19 dossier tests pass).
- **GP-Q0 extra checks, against the evidence as committed:**
  - *Differential.* [Observed] The `main` differential (42 scenarios, re-run: identical) is a real
    old-versus-new differential. It runs over fakes, though, not over "a mutated-record corpus that
    includes records with altered prose". [Observed] The modules that read records (for example
    `governance-inputs.ts` and the body-read-authority path) changed only `export` keywords and
    comments, and their emitted JS is identical once those are removed (§3). That discharges the
    altered-prose limb in substance, but no record says so.
  - *Rule-6 mutant per predicate.* **Not met.** Four predicates in `main.ts` survive the shipped
    suite: the three guard predicates (F1) and the suffix filter at `main.ts:241`. The retained
    differential includes a `model-throws-poc-observation-error-bare` scenario, so it would
    probably kill P-suffix-filter [Inferred, not run], but it is not in CI and no mutant is
    recorded for that predicate.
  - *Owner notice.* [Unknown] I cannot see one. It belongs in the cycle report `syzygy-bpyt.10` and
    is non-blocking under GP-Q0.
- **Failure scenario.** A class-1/3 change merges on a "none" declaration, and the GP-Q0 checks the
    owner required for exactly this class stay incomplete. Today a refactor that renders a bare
    `PocObservationError` as `observation failed (<kind>): undefined` passes the shipped suite.
- **Proposed fix.** (a) Change the PR body's class line to "1, 3" and cite this review. (b) Add a
  `main.test.ts` case that throws `new PocObservationError(kind)` with neither `artifactPath` nor
  `detail`. It should expect exactly `syzygy POC: observation failed (<kind>)\n` on stderr and
  exit 1. Record the P-suffix-filter mutant (old/new fragment, commit) as killed. (c) Resolve the
  guard predicates through F1's fix: removing the guard leaves nothing to mutate, and a kept guard
  needs tests and recorded mutants. (d) In `main-differential-2026-10-22.json` (or the
  verification record), add one field that maps the altered-prose limb to the
  emitted-JS-identity evidence for the record-reading modules, with the list of modules and the
  comparison method. (e) Post the non-blocking owner notice in `syzygy-bpyt.10`.

### N1 — note — two `Test seam` comments in `governance-inputs.ts` invite an un-export that would break three governance scripts

- **Evidence.** [Observed] `governance-inputs.ts:46` (above `PWB_ACT_RECORDS`, line 63) and `:69`
  (above `PWB_SUPERSEDED_ACT_RECORDS`, line 70) say "Test seam: exported for the tests; production
  code reaches it only inside this file." Three scripts find these declarations by their literal
  `export const` text:
  - `scripts/build_pwb_registry_machine_ceiling_amendment.py:216`
    (`^export const {re.escape(name)}\b…`);
  - `scripts/record_pwb_registry_machine_ceiling_act.py:470`
    (`gate.index('export const ' + name)`);
  - `scripts/install_redis_sitting.py:1042,1053` (`(?=export const PWB_ACT_RECORDS:)`, and the
    marker `"export const PWB_ACT_RECORDS:"`).

  The census's code set is `.ts .mts .mjs .js .cjs` (`export_census.py:26`) and excludes `.py`,
  which is why these readers were missed. [Observed] The line-40 comment on
  `PWB_AUTHORITY_ARTIFACTS` is accurate enough, because the Python reads that name only inside
  an object literal.
- **Failure scenario.** A later hygiene pass takes the comment at its word and removes `export`.
  The ceiling-act `--check` scripts then raise on a missing anchor in the battery, and
  `install_redis_sitting.py` refuses to re-point the gate.
- **Proposed fix.** Rewrite the two comments along these lines: "Parse anchor: scripts/
  build_pwb_registry_machine_ceiling_amendment.py, record_pwb_registry_machine_ceiling_act.py and
  install_redis_sitting.py find this declaration by its `export const` text; keep the keyword."
  Then either add `.py` to the census code set, or state the exclusion in the census record's
  `method`.

### N2 — note — the `existsSync(stateDir)` limb of the rejected-binding test cannot fail

- **Evidence.** [Observed] In `main.test.ts`, "a rejected binding exits 1 and reaches no
  observation, model, daemon or state directory" asserts `existsSync(stateDir) === false`. With the
  fakes, the state directory is created only by the real `createDaemon`. The fake creates nothing,
  and `main` never makes the directory itself, so the limb holds even when the gate is bypassed.
  The call-log limb (`[bind <repoRoot>]`) and the exit code carry the test: P-rejected was killed
  through them. The PR body says this test pins "no … state directory" with "an `existsSync`
  check".
- **Failure scenario.** A regression that writes into the state directory before the gate (for
  example a future pre-gate credential mint) would pass this test.
- **Proposed fix.** Either make the fake `createDaemon` call `mkdirSync(options.stateDir)` so the
  limb can fail, and record a gate-bypass mutant that it kills, or drop the limb and the PR body's
  claim.

### N3 — note — four re-runnability gaps in the evidence records (rules 6, 7, 11)

- **Evidence.**
  - [Observed] `export-census-2026-10-22.json`'s diff method cites `git diff 32c16625 60877d39`.
    In my clone, after fetching `origin` and the PR branch, `60877d39` is reachable from no ref
    (its tree equals `b6aa5eee`'s).
  - [Observed] `route-capture-2026-10-22.json` records the whole-file sha256 `760f650e…`, which
    depends on a fixture repository whose revision the record does not name. My run of the same
    script gives a different digest (§3).
  - [Observed] The census JSON gives the denominators as 80/79 "declaring files", while the PR body
    and the tool's output say 91/90. 80/79 counts files with at least one export; 91/90 counts the
    files scanned.
  - [Observed] Every record names base `32c16625` and code commit `b6aa5eee`, not the reviewed
    `4f3c3ebf`. My re-runs at `4f3c3ebf` reproduce the mutant outcomes and the differential (§3).
- **Failure scenario.** A later reader cannot regenerate the census diff from a reachable commit,
  and cannot reproduce the capture digest that the PR quotes.
- **Proposed fix.** Cite `b6aa5eee` (or the merged commit) in the census diff method. Record the
  fixture repository's revision, and how the script creates it, in the route-capture record. Name
  both denominators with their definitions. When the evidence is regenerated for F1/F2, record
  `ranAtCommit` at the new head.

### N4 — note — 53 of the 100 un-exported types are named in a still-exported declaration

- **Evidence.** [Observed] Method: for each un-exported `type` or `interface`, search the same file
  for a whole-word match on a line that declares a still-exported function, const, type or
  interface. That finds 53 of 100. Examples: `DossierEvaluationArgs` in `evaluateDossierDirectory`,
  `FocusedTestCommandInput` in `focusedTestCommand`, `MaterializeRoutesOptions` in
  `materializeRoutes`, and `PocCliParse` in `parsePocCli`. Typecheck and declaration emit pass.
- **Failure scenario.** A future caller cannot name a parameter or return type of an exported
  function and has to use `Parameters<typeof f>`, or the type gets re-exported piecemeal and the
  census drifts. This is a code-quality judgment, not a defect. The bead's literal rule ("used
  nowhere outside their file") is met.
- **Proposed fix.** Pick one policy and state it in the census record's `method`: either types
  that appear in an exported signature stay exported (re-export the 53), or they stay private by
  design. Either is fine.

### N5 — note — fixed sleeps in the watch tests, and a duplicated seam comment in `main.ts`

- **Evidence.** [Observed] The `--watch` tests in `main.test.ts` wait fixed 100 ms and 50 ms
  intervals for console re-observation instead of awaiting a signal. AGENTS.md records repeated
  load timeouts on this host. Separately, `main.ts:58` and `:72` add a
  `// Test seam: exported type …` line directly above JSDoc that already says "Exported as a test
  seam" (`:61`, `:74`).
- **Failure scenario.** Under heavy parallel load the re-observation has not finished within the
  window, so the test fails intermittently on code that is correct.
- **Proposed fix.** Await a promise that the fake `reobserve`/`observe` resolves, or use
  `vi.waitFor`, instead of sleeping. Keep one of the two seam notes in each place.

## 5. Every changed output

1. [Observed] **Exit code and stdout/stderr for the extensionless and package-directory invocations**:
   1 or 0 with usage/refusal at base; 0 and silent at head (F1).
2. [Observed] **Importing `dist/main.js` or the package `"."` export** no longer runs the POC. This is
   intended and disclosed. There are 0 importers.
3. [Observed] **Exported TypeScript surface**: 161 symbols lose `export`, among them
   `RenderedDossier` and `stopReasonLabel` on the `./dossier-render` subpath; `MAX_ANCHORS_PER_BLOCK`
   and the `source-adapter` module are deleted. There are 0 code importers.
4. [Inferred] **Live surface version** (sha256 over both `src` trees): it changes on any `src` edit,
   as the PR discloses. In the fixture captures, base and head bytes are identical, so the captured
   pages do not depend on it. Any walkthrough record bound to an earlier surface version is already
   stale with respect to every later `src` commit, so this PR adds no new class of staleness.
5. [Inferred] **Stack frames** of an uncaught horizon failure at startup differ. The exit code
   (1) and the first error line are the same.
6. [Observed] **No change** in: the 230 fixture route responses (base equals head, run twice at
   base); the 42 differential transcripts (stdout, stderr, exit code, call order, daemon options,
   route list, post-start responses, close count); the `.js` CLI forms; the `check_quotations`
   output; the `check_governance` verdicts; the two ceiling-act `--check` regenerations; the
   emitted JS of 176 of 178 common files (byte-identical or identical modulo `export` and
   comments).

## 6. Verdict per acceptance criterion

1. **"main.ts exports main(); a test drives it with a fake io (one behavior gate)."** Met as
   written [Observed]: `main(argv, io, deps)` is exported and `main.test.ts` drives it with a fake
   `PocIo` (16 tests). The entry guard that came with it changes behavior (F1) and leaves three
   predicates untested (F1, F2), so the criterion's outcome is not clean until F1 is fixed.
2. **"Unused-export sweep (method stated) shows only deliberate test seams remain, each commented."**
   Met as scoped [Observed]. 92 commented seams; 17 exports in `test-*.ts` support modules under
   module-head comments; the 10 test-only and 6 dead or self-only exports remaining are all in
   `polaris.ts` and `public-source-screening.ts`, excluded by instruction; 1 sits in
   `pwb-mutation.ts`, a mutation runner excluded by instruction. Two of the seam comments
   misstate why the export exists (N1).
3. **"Orphan modules deleted or wired; suite and rendered bytes unchanged."** Met [Observed]:
   `source-adapter.ts` and its test are deleted, no digest-bound file pins the path, the suite
   passes with +16/−9, and the fixture rendered bytes are identical base against head under one
   fixture revision. The live Butlers surface was not captured, which is lawful and disclosed.

## 7. Test quality

- [Observed] `main.test.ts` hard-codes its expected strings and exit codes as literals: usage text,
  refusal lines, banner lines, the `[bind …]` call log. They are not imported from `main.ts`.
- [Observed] Fixtures and fakes are built inside `it`/`beforeEach` bodies. Nothing that can throw
  runs at describe time: each of my 13 mutant runs reports 16 tests, never 0.
- [Observed] No test passes for the wrong reason, except the `existsSync` limb (N2). The P-rejected
  kill comes from the call log and the exit code.
- [Observed] The 3 differential survivors (`observer-read-at-process-cwd`,
  `model-observer-root-process-cwd`, `observation-instant-from-clock`) are equivalent under the
  harness by construction. The harness spies `process.cwd` to return `io.cwd()`'s value and fakes
  `Date` to `io.now()`'s instant. The composition root defines `io` as exactly those, and
  `main.test.ts` kills each one in my re-run of the lane's 24 mutants.
- [Observed] Gaps: the suffix filter and the three guard predicates (F1, F2), and the fixed
  sleeps (N5).
- [Observed] Re-runnability: the mutant records store old/new fragments, command and commit
  (rule 6), and re-ran here with the same outcomes. The gaps are in N3.

## 8. Cleanup

- The scratch clones `rev-501/head` and `rev-501/base` and the fixture repository
  `rev-501/fixture-repo` were deleted after this file was written. Before deletion, both clones had
  a clean `git status`, and `main.ts` at head was restored and re-hashed to `5fc4e364…` after the
  mutant runs.
- Retained in `rev-501/`: this raw; my scripts (`classify_diff.py`, `unexport_sweep.py`,
  `fragment_check.py`, `seam_claims.py`, `dist_compare.py`, `predicate_mutants.py`); and their
  outputs (`predicate-mutants.json`, `mutants-rerun.json`, `capture-*.json`, `census-*.json`,
  `cg-*.txt`, `cq-*.txt`, `export-removed.tsv`).
- Nothing was pushed, commented, merged or written under `/home/tze/GitHub/syzygy/.worktrees/`, and
  no `bd` mutation was run.
