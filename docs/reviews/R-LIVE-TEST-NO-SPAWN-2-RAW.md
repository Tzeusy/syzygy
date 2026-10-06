# R-LIVE-TEST-NO-SPAWN-2
Verdict: REVISE
Reviewed commit: 5a50f00411442adf7bc72effc030002841680351
Subject: PR #386 (syzygy-hjuz, syzygy-z774)

Reviewer: fresh-context agent, 2026-10-07, round 2 (penultimate). I read the
bytes with `git diff origin/main...5a50f004…`, `git show <commit>` for
`16d33c62` (the repair) and `5a50f004` (the evidence), and
`gh pr view 386`. I ran tests and probes in a scratch
`git worktree add --detach` at the head, after `npm ci`. All probes were
applied only to that scratch tree, reverted with `git checkout --` after
each, and the worktree was removed afterwards. Sentinels and a throwaway
repository were written only under my scratchpad. I fetched no content of
any target or external repository. No Butlers checkout was touched, and the
live test stayed skipped (`SYZYGY_POC_BUTLERS_REPO` unset).

Runs at the head [Observed]:
- `vitest run` over `test-artifact-verification-live-source.test.ts`,
  `test-artifact-verification.test.ts`, `capture-test-artifact-main.test.ts`
  and the live test: 129 passed, 1 skipped. `sync-child-process-guard.test.ts`
  lives in `apps/three-surface-poc/src/`, and it passed 5/5 in the next run.
- `scripts/check_governance.py`, run from the worktree root: "32 OK, 21 WARN,
  0 FAIL (53 checks)".
- `scripts/check_docs_review_campaign_partition.py --check docs/README.md
  --second-method`: "second-method PASS: git ls-files=367; git ls-tree=367"
  and "partition PASS: denominator=367; assigned=367; raw=339; other=28;
  unmatched=0; overlaps=0; campaigns=78".

## Governing references (located by `DIRECTIVE-REGISTER.md`, quoted)

- Direction item 4,
  `.syzygy/governance/decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:42-48`:
  "The test-capture tool (`npm run poc:capture-test-artifact`) is to stop
  running the observed project's tests itself: it prints the command for the
  operator to run and ingests only the result file the operator hands it."
- SEC-3 (register `:49` → `.syzygy/governance/doctrine/security.md:61-68`):
  "Syzygy runs observed-project code only inside an explicit, opt-in
  execution profile." and "**What this binds:** Syzygy itself, every process
  Syzygy launches or schedules, …"
- RFC5-18 (register `:342` →
  `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md:91,111-113`):
  "Absent any of these the run does not launch, and claims needing the
  evidence it would have produced render Unknown with the **primary** reason
  **`execution-blocked`**".
- RFC5-19 (register `:343` → same file `:130`), as the code's disclosure
  quotes it: "an artifact of unverifiable origin caps at report-fact however
  retained, well-formed, and revision-bound it is."
- VIS-2 (register `:34` → `.syzygy/governance/doctrine/vision.md:133`): "No
  evidence means Unknown, not success."

## Round-1 findings: disposition

| R1 item | Directed disposition | At `5a50f004` | Status |
|---|---|---|---|
| 1 REVISE: `import m = require('node:module')` invisible | Refuse import-equals | `scan` adds `import = require` for every `ImportEqualsDeclaration` (`test-artifact-verification-live-source.test.ts`, inside `scan`, after the re-export rule). Two `it.each` fragments; mutant H18, the reviewer's probe, is killed. In the capture check, import-equals is still refused by the `indirect` regex (`\brequire\s*\(`, `node:module`) and the module-literal count [Observed by reading] | Repaired [Observed] |
| 2 REVISE: a literal `git` starts a shell via `-c alias.…` | Capture tool's call exactly `('git', ['rev-parse','HEAD'], {cwd, encoding})`; the closure refuses `-c`, `--config-env*`, `--exec-path*`, `alias.`, and `process.env` writes; residuals stated | Capture: `resolveCommitWithGit` is now exactly that call (`capture-test-artifact-main.ts:48`), held by `isRevParseHead`, with seven fragments (M32–M34 killed). Closure: `GIT_PROGRAM_OPTIONS` (`:70-75`) checked on every string or template piece (`:146-147`); `process.env` is allowed only as `process.env.NAME`, and not as a write target (`:149-153`). Twelve fragments; H20 and H21 are killed. The residual is stated at `:26-35`, and H23 is recorded as the expected survivor | Repaired as directed, but the literal list is too narrow; see new finding 1 |
| 3 NOTE: re-export from the process module | Refuse | `re-exports from the process module` for any `ExportDeclaration` with that specifier; two fragments, H19 killed | Repaired [Observed] |
| 4 NOTE: the git fallback reads the checkout's `.git/config` | State as residual | Stated at `:30-34` (`core.fsmonitor` named) | Dispositioned [Observed] |
| 5 NOTE: unquoted printed paths | Shell-quote | `posixShellWord` and `liveTestOperatorInstructions` (`test-artifact-verification.ts:390-410`), with exact-string tests over `/tmp/my repo/it's`; H22 killed. I fed the test's expected words to `dash` and they came back as `[/tmp/my repo/it's]`, `[/opt/py 3/bin/python']`, `[tests/a b.py]`, `[$(touch x); \`y\`]` | Repaired [Observed]; one small remainder in note 4 |
| 6 NOTE: docs sentence too broad | Narrow | `docs/THREE-SURFACE-POC.md:316-318`: "Unknown: `execution-blocked` for a matching operator-reported run, and "Not verified" with its own reason for an absent, unmarked or mismatched record" | Repaired [Observed] |

## New findings

1. **REVISE (AC2): git starts a program through literal arguments and an
   `env` option that none of the refused literals name, and that falls
   outside the stated residuals.**
   The closure rule refuses four literal shapes (`:70-75`). The header
   (`:26-35`) states two residuals for git: "an option assembled from pieces
   at run time (the expected survivor H23)", and what git *inherits*: "the
   GIT_CONFIG_* variables, PATH and GIT_EXEC_PATH of the operator's
   environment, and the checkout's own `.git/config`". The three probes
   below are all literals, inherit nothing, and do not touch the checkout. I
   put them at module scope in the live test, after its imports, with
   `writeFileSync` added to an allowed `node:fs` import. Each was wrapped in
   `try {} catch {}`:
   ```ts
   // A: git writes a config of its own repository, then runs the program it names
   execFileSync('git', ['init', '-q', `${PROBES}/repoA`]);
   execFileSync('git', ['-C', `${PROBES}/repoA`, 'config', 'core.fsmonitor', `touch ${PROBES}/EVADED-A-fsmonitor; true`]);
   execFileSync('git', ['-C', `${PROBES}/repoA`, 'status'], { encoding: 'utf8' });
   // B: a transport option names the program
   execFileSync('git', ['ls-remote', `--upload-pack=touch ${PROBES}/EVADED-B-uploadpack; git-upload-pack`, `${PROBES}/repoA`], { encoding: 'utf8' });
   // D: the call's own env option points git at a config file the test wrote
   writeFileSync(`${PROBES}/cfgD`, `[alias]\n\tprobe = !touch ${PROBES}/EVADED-D-envconfig\n`);
   execFileSync('git', ['probe'], { env: { GIT_CONFIG_GLOBAL: `${PROBES}/cfgD`, PATH: '/usr/bin:/bin' }, encoding: 'utf8' });
   ```
   Result [Observed]: the closure test ("…no file in that closure can start
   anything but git or bd") and the sync guard ("runs only short local
   tools…") both passed. All three sentinels were written: `EVADED-A-fsmonitor`,
   `EVADED-B-uploadpack` and `EVADED-D-envconfig`. The live test was skipped,
   but the lines ran at module load, so they would run under the default
   `npm test` too. Each is a shell started with every guard green:
   - A takes no `-c`, and its key is `core.fsmonitor`, not `alias.`;
   - B's `--upload-pack=` is not in the list;
   - D's config section header `[alias]` does not contain `alias.`, and an
     `env` key on the call's options object is not a `process.env` write.

   The capture tool is not exposed this way: its one call is pinned to
   `('git', ['rev-parse', 'HEAD'], { cwd, encoding })` [Observed by reading
   and by its fragments]. The same holds for `--receive-pack`, `--template`
   (hooks), `--git-dir` or `-C` pointed at a repository whose config the
   closure wrote, `clone --config=…`, and the `GIT_SSH_COMMAND`,
   `GIT_EXTERNAL_DIFF` or `GIT_CONFIG_COUNT` keys in an `env` option
   [Inferred, not run].

   *Repair* (either one is enough for AC2 as worded):
   - (a) Close the obvious spellings. Refuse an `env` property in any options
     object passed to the git runner in the closure (no non-test source
     under core or cap1-core passes one: `env\s*:` matches 0 lines there,
     over 7 runner calls [Observed by `git grep`]). Refuse the literals
     `config`, `init`, `clone`, `fetch`, `ls-remote`, `submodule`,
     `--upload-pack`, `--receive-pack`, `--template`, `--git-dir`,
     `--work-tree` and `--config`. Add fragments for A, B and D.
   - (b) Restate the residual as the class: "any git call whose arguments,
     options, or target repository the closure chooses can run a program its
     configuration names; the literal refusals cover only git's global
     options". Record A, B and D as expected survivors beside H15 and H23.

   For the last round, (b) and the `env` key from (a) are the cheapest
   honest pair.

2. **REVISE (AC2): the test framework's module loader starts any program.
   `vi.importActual` is an allowed import's member, reached with no
   forbidden word.**
   `vitest` is in `ALLOWED_PACKAGES` (`:112`). Its `vi.importActual` loads
   any module by a run-time string, which is the same capability as the
   refused dynamic `import()` and `getBuiltinModule`. Probe C, at module
   scope in the live test (`vi` added to the existing `vitest` import):
   ```ts
   const cp = await vi.importActual<{ spawnSync: (c: string, a: string[]) => unknown }>(['node:child', 'process'].join('_'));
   cp.spawnSync('touch', [`${PROBES}/EVADED-C-importActual`]);
   ```
   Result [Observed]: both guards passed, and `EVADED-C-importActual` was
   written. This is not H15: that residual is a run-time key in an
   *imported* module, and this is in the live test itself with no computed
   access. It is not H23 or anything git inherits either. It is a new member
   of a class the check already refuses (module loading by a computed name),
   and the refusal does not cover it.
   *Repair:* in the closure, accept only named `vitest` imports from an
   allow-list (`describe`, `expect`, `it`, `beforeAll`, `afterAll`,
   `beforeEach`, `afterEach`). That refuses `vi`, and with it
   `importActual`, `importMock`, `doMock` and `mock` factories. Add C as a
   fragment and a recorded mutant with its sentinel.

3. **NOTE (AC4): the evidence is sound. Two labels and one sentence are
   off.**
   [Observed] Both new records give the run commit `b56834f8…`, which
   resolves to a commit object, and `old`/`new` per edit, exit, test count,
   failing names and `shSentinelWritten`. I recomputed with `sha256sum` over
   the head's bytes:
   - 9 of 9 live-test `subjectDigests`, among them `e6c500f3…` (live test),
     `5c80b05b…` (source check), `08ef138f…` (core) and `45cf6c52…`
     (capture main);
   - 4 of 10 capture digests: `bd2d2e42…`, `d56544de…`, `119fe69c…`, and
     `45cf6c52…` again.

   All match, so the rebase did not change the subject bytes. I re-ran H23
   at the head: 82/82 passed, exit 0, as recorded (it survives). Three
   remainders:
   - (i) The survivors are labelled only by an id suffix,
     `-EXPECTED-SURVIVOR`. The JSON carries no reason field, and the reason
     lives in the source header and the PR body. Add a `"reason"` naming the
     header residual it falls under.
   - (ii) The evidence commit's message `5a50f004` says H23 is "a git option
     built from pieces in an imported module", but H23 edits the live test
     itself. The PR body and the header are right.
   - (iii) H23's `shSentinelWritten: false` cannot show that the route is
     live, because the line sits inside the skipped test. A module-scope
     variant, as in finding 1, would show that it starts `sh`.

4. **NOTE (AC3): the quoting is correct for POSIX sh. One small edge
   remains.** `posixShellWord` is the standard `'…'` with `'` written as
   `'\''`, and `dash` agrees with it (table, row 5). A checkout path that
   begins with `-` would still be read as an option by `cd` (`cd '-x'`).
   *Repair (optional):* print `cd -- <repo>`. The `--junitxml=<file>`
   placeholder is unchanged from before and is clearly a placeholder.

5. **NOTE (AC5): no new process-start path in the capture tool.** I tried
   import-equals, `createRequire` through allowed imports, and `vm` or
   `worker` imports against its check by reading it. The `indirect` regex
   and the per-file import allow-list refuse each one, and its git call is
   shape-pinned [Observed by reading; not mutated].

## Acceptance criteria

- **AC1, met** [Observed]. Every round-1 finding and note is repaired or
  dispositioned as the lead directed (table above).
- **AC2, not met** [Observed]. Four probes start a process with every guard
  green, outside every stated residual: three through git (finding 1) and
  one through `vi.importActual` (finding 2). Every other form I tried was
  refused, by a fragment test or by reading the rule:
  - import-equals, and `createRequire` via import-equals;
  - re-exports;
  - `node:worker_threads`, `node:vm` and `node:module` imports;
  - `-c`, `--config-env` and `--exec-path`;
  - `process.env` writes.
- **AC3, met** [Observed] (note 4).
- **AC4, met** [Observed], with the label remainders in note 3.
- **AC5, met** [Observed]:
  - the committed round-1 raw is byte-identical to the round-1 reviewer's
    scratch copy (`git diff --no-index`, empty);
  - the new README row quotes `REVISE` at `R-LIVE-TEST-NO-SPAWN-1-RAW.md:2`,
    which is the verdict line;
  - the partition is 367/367 with 78 campaigns, and the count sentence says
    the same;
  - `origin/main` has no new `docs/reviews` or `docs/README.md` change since
    the merge base, so the count does not race today;
  - the PR touches nothing under `.syzygy/**` or `openspec/**`.

## Count

Findings: 5 — 2 REVISE (1, 2), 3 NOTE (3, 4, 5).
