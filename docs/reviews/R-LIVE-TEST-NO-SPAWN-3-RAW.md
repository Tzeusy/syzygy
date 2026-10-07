# R-LIVE-TEST-NO-SPAWN-3
Verdict: REVISE
Reviewed commit: c74214e1ac79745b8bc8afa80c6ff7549c47ca4e
Subject: PR #386 (syzygy-hjuz, syzygy-z774)

Reviewer: fresh-context agent, 2026-10-07, round 3 (final). I read the bytes
with `git diff origin/main...c74214e1`, `git show` of `6b4fe6ca` (the round-2
repair) and `c74214e1` (its evidence), and both prior raws at the head. I ran
tests and probes in a scratch `git worktree add --detach` at the head, after
`npm ci`. Probes went into that scratch tree only and were reverted with
`git checkout --`. The worktree and the sentinel directory were removed
afterwards. I fetched no content of any target or external repository. No
Butlers checkout was touched, and the live test stayed skipped
(`SYZYGY_POC_BUTLERS_REPO` unset).

Runs at the head [Observed]:
- `vitest run` over `test-artifact-verification-live-source.test.ts`,
  `test-artifact-verification.test.ts`, the live test,
  `sync-child-process-guard.test.ts` and `capture-test-artifact-main.test.ts`:
  146 passed, 1 skipped (the live test), across 4 passed files and 1 skipped
  file.
- `check_docs_review_campaign_partition.py` was not re-run: it refuses a
  check target that is not the HEAD-bound `docs/README.md` relative to the
  cwd, and I did not `cd`. The row and count were checked by reading (AC5).

Governing references: the same as round 2 (direction item 4,
`REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:42-48`; SEC-3; RFC5-18/19; VIS-2).
They are quoted in `R-LIVE-TEST-NO-SPAWN-2-RAW.md` and not repeated here.

The lead's binding decision for this round:
- stop extending git literal deny-lists;
- refuse any `env` option on git and bd calls;
- state git as a whole code-execution surface, record such probes as
  expected survivors with reasons;
- limit vitest imports to a named allow-list.

## Round-2 findings: disposition

| R2 item | Directed disposition | At `c74214e1` | Status |
|---|---|---|---|
| 1 REVISE: git starts a shell via literal `core.fsmonitor` (A), `--upload-pack=` (B), and an `env` option (D) | Refuse `env` on git/bd calls; restate git's residual as its class; A and B as expected survivors | `test-artifact-verification-live-source.test.ts:182-191`: options must be one object literal with readable keys, none `env`; more than 3 arguments is refused. Six fragments, among them probe D, a quoted `'env'`, the shorthand `{ env }`, a non-literal options object, a spread and a 4th argument. Header `:26-39` restates the class: "Any git call whose subcommand, arguments, options, config or target repository the closure chooses can run a shell … The static check bounds only the capture tool's one pinned call." H24 (D, module scope, sentinel written before repair) is killed. H26 (A) and H27 (B) are expected survivors with `reason` fields, and their sentinels were written | Repaired / dispositioned as directed [Observed] |
| 2 REVISE: `vi.importActual` loads the process module by a run-time name (C) | Allow-list the vitest imports | `:121` `VITEST_IMPORTS` holds `describe`, `it`, `expect` and the four hooks. `:151-155` refuse any other name, read by its exported name, so `vi as v` is caught too. Default, namespace, side-effect and re-export forms are also refused. Five fragments; H25 (C, module scope, sentinel written before repair) is killed | Repaired [Observed] |
| 3 NOTE: no `reason` on survivors; wrong `5a50f004` message; H23 sentinel cannot show liveness | Add reasons; correct; module-scope variant | Every `expectedSurvivor` (H15, H23, H26, H27, H28) carries a `reason` naming its header residual. `6b4fe6ca`'s message corrects the H23 sentence; the earlier message is not rewritten. H28 is H23 at module scope, with `shSentinelWritten: true` | Repaired [Observed] |
| 4 NOTE: `cd '-x'` reads as an option | Print `cd --` | `test-artifact-verification.ts:406` prints `cd -- ${repo}`. H22 now also fails the new "ends cd's options" test | Repaired in the live test's instructions [Observed]; the capture tool's own printout is not (new note 3) |
| 5 NOTE: the capture tool has no new route | none | Unchanged; see AC3 | n/a |

## New findings

1. **REVISE (AC2): the `shell` option on the permitted runner starts
   `/bin/sh` directly, with git never involved.** The options rule
   (`:182-191`) refuses only the key `env`. With `shell: true`, Node joins
   the command and its arguments into one string and runs it with `/bin/sh -c`.
   The literal `'git'` is then only a word in a shell command line. A string
   `shell:` value names the program Node starts in place of `/bin/sh`.
   Probe E, at module scope in the live test (after `const SCOPE`), with no
   import added:
   ```ts
   try { execFileSync('git', ['--version;', 'touch', `${PROBES}/EVADED-E-shell`], { shell: true, encoding: 'utf8' }); } catch { /* probe */ }
   ```
   Result [Observed]: the closure test and the sync guard both passed (52/52
   and 5/5), and `EVADED-E-shell` was written. Node printed DEP0190
   ("Passing args to a child process with shell option true …").
   This is outside every stated residual. It is not git's surface: git does
   not choose or run the program; `sh` runs `touch` after `git --version`.
   It is not a run-time key, and it is not inherited configuration.
   No closure source passes `shell` (`shell\s*:` matches 0 code lines under
   `three-surface-poc-core/src` and `cap1-core/src` [Observed, `git grep`]).
   The closure's three runner calls use only `encoding`, `maxBuffer` and
   `stdio` (`code-structure.ts:82-85`, `work-items.ts:52-55`,
   `worker-change-observation.ts:66-69`).
   *Repair:* replace the `env` deny with a key allow-list (`encoding`,
   `maxBuffer`, `stdio`, and `cwd` if wanted), and add fragments for
   `shell: true` and `shell: '/bin/x'`.
   The capture tool is not exposed: its `isRevParseHead` admits only `cwd`
   and `encoding` [Observed by reading].

2. **REVISE (AC2): `import.meta.glob` loads a package that the import
   allow-list refuses, and that package starts a process.** Vitest runs test
   files through Vite's transform, which turns `import.meta.glob(…, { eager:
   true })` into static imports. The scan sees no `ImportDeclaration`, so
   `ALLOWED_PACKAGES` (`:117`) never applies. The scan also has no
   dynamic-`import()` call (`:173`), no forbidden identifier and no computed
   key. Probe F, at module scope in the live test:
   ```ts
   const globbed = import.meta.glob('/node_modules/tinyexec/dist/main.js', { eager: true });
   for (const mod of Object.values(globbed)) {
     try { await (mod as { x: (c: string, a: string[]) => Promise<unknown> }).x('touch', [`${PROBES}/EVADED-F-glob`]); } catch { /* probe */ }
   }
   ```
   Result [Observed]: both guards passed in the same run as probe E, and
   `EVADED-F-glob` was written. `tinyexec` is installed as a vitest
   dependency; any installed module that exports a spawner would serve.
   This is outside every stated residual: no git or bd, no run-time key
   (the pattern and the access are literals or `Object.values`), and nothing
   inherited. It is the same class as finding 2 of round 2: module loading
   that the import rules do not see.
   No non-test file in the closure packages uses `import.meta` (`git grep -F
   import.meta` has hits only in `*.test.ts` files outside the closure, and
   in the source check itself [Observed]).
   *Repair:* refuse `import.meta` in the closure, either as any
   `MetaProperty` or every member but `url`. Add fragments for `glob` and
   `globEager`.

3. **NOTE: the capture tool's printout still lacks `cd --`.** Round-2
   note 4 was repaired in the live test's instructions only.
   `apps/three-surface-poc/src/capture-test-artifact.ts:54` still prints
   `` `  2. cd ${shellQuote(input.repoRoot)} && ${run}; …` ``. The text is
   for display only, so this is optional.

4. **NOTE (AC4): the evidence's run commit is reachable from no ref in this
   PR.** `live-verification-test-no-spawn-mutants-round2-repairs-2026-10-07.json`
   names `b06a92be…`. That object exists (`git cat-file -t` gives `commit`),
   and its log names the round-2 repair. It is not an ancestor of
   `c74214e1` (`git merge-base --is-ancestor` exits 1), because the branch
   was rebased. The subject digests carry the anchor: I recomputed 9 of 9
   with `sha256sum` over the head bytes, and all match. Among them are
   `e6c500f3…` (live test), `5ccbbfb9…` (source check), `3826deea…` (core
   module), `a0774fc8…` (sync guard), `cb66a5ff…` (worker-change observer)
   and `45cf6c52…` (capture main). So rule 11 holds through the digests
   [Observed]. H2 and H3 record `old`/`new` as placeholders
   (`<whole file>` and `<origin/main:…>`), not as fragments. The second one
   names a ref that will move [Observed]. Neither matters now; a re-run
   would pin `origin/main` to a SHA.

5. **NOTE: the stated git residual is honest and bounded as directed.**
   `--receive-pack`, `--template`, `clone --config`, and `-C` at a repository
   whose config the closure wrote are all git-surface routes. Under the lead
   decision they are NOTE-level at most [Inferred, not run]. I did not count
   probe E as one, because git starts nothing there.

## Acceptance criteria

- **AC1, met** [Observed]. Every round-2 finding and note is repaired or
  dispositioned as the lead directed (table above).
- **AC2, not met** [Observed]. Two probes start a process with every guard
  green, outside every stated residual: the runner's `shell` option
  (finding 1) and `import.meta.glob` (finding 2).
- **AC3, met** [Observed].
  - `capture-test-artifact-main.ts:49` is
    `execFileSync('git', ['rev-parse', 'HEAD'], { cwd: repoRoot, encoding: 'utf8' })`.
  - The capture source check's `isRevParseHead` admits exactly those two
    literals, an options object of `cwd` and `encoding` only, and no 4th
    argument.
  - `.call`, `.apply`, aliases, renames, `env` and spreads are each refused
    by a fragment, and all 52 capture tests passed.
  - `shell` is excluded by that options allow-list, and the capture tool
    runs under plain `node`, not Vite, so `import.meta.glob` does not apply
    there [Inferred from `package.json:18`].
- **AC4, met** [Observed].
  - Every mutant records `old`/`new`, exit, test count, failing names and
    `shSentinelWritten`.
  - Every expected survivor carries a `reason`.
  - The 28 mutants (23 killed, 5 expected survivors) match the commit
    message.
  - The digests were recomputed 9/9.
  - Remainders are in note 4.
- **AC5, met** [Observed].
  - The committed `R-LIVE-TEST-NO-SPAWN-2-RAW.md` is byte-identical to the
    round-2 reviewer's scratch copy (`git diff --no-index`, empty; both
    13,971 bytes).
  - The README row quotes `REVISE` at `R-LIVE-TEST-NO-SPAWN-2-RAW.md:2`,
    which is the verdict line.
  - The campaign pattern `R-LIVE-TEST-NO-SPAWN-.*\.md` is registered.
  - The count sentence says 78 rows over 368 files. That is round 2's
    367/78 plus one raw [Inferred; the partition script was not re-run].
  - The PR touches nothing under `.syzygy/**` or `openspec/**` (`--stat`).

## Count

Findings: 5 — 2 REVISE (1, 2), 3 NOTE (3, 4, 5).
