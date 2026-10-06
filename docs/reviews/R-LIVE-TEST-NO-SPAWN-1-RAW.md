# R-LIVE-TEST-NO-SPAWN-1
Verdict: REVISE
Reviewed commit: 1d053f12fcf32581e56d52fd55a578659fca4fdf
Subject: PR #386 (syzygy-hjuz, syzygy-z774)

Reviewer: fresh-context agent, 2026-10-07, round 1. I read the bytes with
`git diff origin/main...1d053f12…`, `git show 1d053f12…:<path>` and
`gh pr view 386`. I ran tests in a scratch `git worktree add --detach` at the
head, after `npm ci`, and removed it afterwards. All probes below were applied
only to that scratch tree. I fetched no content of any target or external
repository; the one live-test run used a non-existent scratch path as
`SYZYGY_POC_BUTLERS_REPO`, so no Butlers checkout was touched.

Runs at the head [Observed]:
- `vitest run` over `test-artifact-verification-live-source.test.ts`,
  `sync-child-process-guard.test.ts`, `capture-test-artifact-main.test.ts`
  and `trajectory.test.ts`: 4 files, 91/91 passed.
- `SYZYGY_POC_BUTLERS_REPO=<scratch>/no-such-repo vitest run
  …/test-artifact-verification.live.test.ts`: 1 failed, with the
  "Syzygy does not run the Butlers test suite. For the owner or a human
  operator: an agent session must not run the pytest command below unless the
  owner has recorded a SEC-3 choice …" message and the printed command; no
  git or pytest ran before the throw.
- `scripts/check_governance.py` (run from the worktree root): "32 OK, 21 WARN,
  0 FAIL (53 checks)".
- `scripts/check_docs_review_campaign_partition.py --check docs/README.md
  --second-method` (run from the worktree root): "second-method PASS: git
  ls-files=366; git ls-tree=366" and "partition PASS: denominator=366;
  assigned=366; raw=338; other=28; unmatched=0; overlaps=0; campaigns=77".

## Governing references (located by `DIRECTIVE-REGISTER.md`, quoted)

- Direction item 4,
  `.syzygy/governance/decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:42-50`:
  "The test-capture tool (`npm run poc:capture-test-artifact`) is to stop
  running the observed project's tests itself: it prints the command for the
  operator to run and ingests only the result file the operator hands it."
- SEC-3 (register `:49` → `.syzygy/governance/doctrine/security.md:61`):
  "Syzygy runs observed-project code only inside an explicit, opt-in
  execution profile." and (`:65-69`) "**What this binds:** Syzygy itself,
  every process Syzygy launches or schedules, …"
- RFC5-18 (register `:342` →
  `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md:91,111-113`):
  "Absent any of these the run does not launch, and claims needing the
  evidence it would have produced render Unknown with the **primary** reason
  **`execution-blocked`**".
- RFC5-19 (register `:343` → same file `:130`), as quoted in the code's
  disclosure: "an artifact of unverifiable origin caps at `report-fact`
  however retained, well-formed, and revision-bound it is."
- RFC2-25 (register `:260` →
  `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:168,178`):
  "A tier qualifies how a claim renders and may only *restrict* its parent
  label's authority" and the row "`report-fact` | **Observed** | "X reported
  Y" is Observed as a fact about the report; Y itself is not thereby
  Observed (SDR-9)".
- VIS-2 (register `:34` → `.syzygy/governance/doctrine/vision.md:133`): "No
  evidence means Unknown, not success."

## Findings

1. **REVISE (AC1): the live-test closure check does not see TypeScript
   `import x = require(…)`, and that route starts `sh` with every guard
   green.**
   `scan` (`test-artifact-verification-live-source.test.ts:85-94`) checks
   module specifiers only on `ImportDeclaration`/`ExportDeclaration`, and its
   identifier rules never see `require` in an import-equals, because the
   TypeScript tree stores that keyword as a token, not an `Identifier`. So
   an `ImportEqualsDeclaration` reaches any module without meeting the
   allow-list (`:71`). Probe, applied in scratch after the imports of
   `test-artifact-verification.live.test.ts`:
   ```ts
   import m = require('node:module');
   (m.createRequire(import.meta.url)(['node:child', 'process'].join('_')) as { spawnSync: (c: string, a: string[]) => unknown }).spawnSync('sh', ['-c', 'touch <scratchpad>/EVADED-P3']);
   ```
   Result [Observed]: the closure check (27/27) and
   `sync-child-process-guard.test.ts` (5/5) both passed, and the sentinel
   `EVADED-P3` was written. The live test was skipped; the line ran at module
   load, so it would run in the default suite too. The sync guard misses it
   because the string `child_process` never appears whole. The capture tool's
   check is not exposed the same way: its `indirect` regex
   (`capture-test-artifact-main.test.ts:230`) refuses `\brequire\s*\(` and
   `node:module` [Observed by reading]. This route is not the stated residual
   (a run-time key inside an imported module): it is in the live test itself
   and needs no computed key.

   *Repair:* in `scan`, treat `ts.isImportEqualsDeclaration(node)` with an
   `ExternalModuleReference` as an import (check its literal against
   `ALLOWED_PACKAGES`, follow relative ones), or refuse import-equals outright;
   add the probe as an `it.each` fragment and as a recorded mutant with its
   sentinel.

2. **REVISE (AC1): "a literal `git`" constrains the command, not what git
   runs, so the permitted call starts a shell.**
   The closure rule (`:96-103`, `:118-121`) and the capture tool's rule
   (`capture-test-artifact-main.test.ts:159-165`) check only that the first
   argument is the literal `'git'` (or `'bd'`). Git executes arbitrary
   commands from its own arguments and environment. Probe, applied in scratch
   after the imports of the live test:
   ```ts
   execFileSync('git', ['-c', 'alias.probe=!touch <scratchpad>/EVADED-P2', 'probe']);
   ```
   Result [Observed]: the closure check and the sync guard passed (32/32,
   live test skipped), and the sentinel `EVADED-P2` was written, so a shell
   ran. An alias such as `!cd <repo> && python3 -m pytest …` would start
   observed code the same way [Inferred]. Related routes of the same class,
   not run [Inferred]: `process.env` is a permitted member (`:66`), so
   `process.env.PATH`, `GIT_CONFIG_COUNT`/`GIT_CONFIG_KEY_0` or
   `GIT_EXTERNAL_DIFF` can redirect a later literal-`git` call; and in the
   capture tool, editing the one existing call's argument list passes both
   the AST rule and the `calls` regex (`:296-297`), which reads only the
   first argument. Neither the header residual (`:16-27`) nor the PR body
   states this class; H15 covers a different one.

   *Repair:* either (a) add an argument rule: the second argument must be an
   array literal whose leading elements are literals, refuse a literal
   `-c`, `--config-env`, `--exec-path`, `-p`/`--paginate` and any `alias.`
   string anywhere in the closure, and refuse assignment to `process.env`
   members; or (b) state this class in the check's header residual and the
   PR body beside H15, and record the probe above as a second expected
   survivor. (b) is enough to meet AC1 as worded ("beyond the stated
   residual"); (a) closes it for the obvious spellings.

3. **NOTE (AC1): the closure check misses a re-export from the process
   module; the sync guard catches it.**
   `export { spawn } from 'node:child_process';` in a closure module
   (`poc-seeds.ts`), imported and called in the live test, gives no closure
   violation, because the binding check at `:90-94` runs only for
   `ImportDeclaration`. `export * from` behaves the same. [Observed] Both
   probes were killed by `sync-child-process-guard.test.ts` ("poc-seeds.ts:2
   <unrecognized child_process binding>"), so the suite is green-blocked. The
   closure check's own claim "no file in that closure can start anything but
   git or bd" does not hold by itself. *Repair:* apply the binding rule to
   `ExportDeclaration`s whose specifier is the process module (refuse them).

4. **NOTE (AC1, pre-existing): the live test's `runGit` fallback runs git
   with observer-chosen arguments against the operator's checkout**
   (`test-artifact-verification.live.test.ts:130`). Git reads the checkout's
   local `.git/config`, which can name programs (for example
   `core.fsmonitor`) that index-refreshing subcommands run [Inferred]. That
   config is the operator's, not committed project content, and this PR did
   not introduce the line. No action needed in this PR; worth a sentence if
   finding 2 is answered with a residual.

5. **NOTE (AC2): the printed command interpolates `repoRoot` and `PYTHON`
   unquoted** (`:53-54`). A path with a space or a shell metacharacter prints
   a command that does something else when pasted. *Repair:* single-quote
   both, as a shell word.

6. **NOTE (AC3): the docs sentence is accurate but slightly broader than the
   code.** `docs/THREE-SURFACE-POC.md:313-320` says the demonstration item
   "now renders Unknown (`execution-blocked`)". Per the bullets just above
   (`:298-306`), only a matching, exit-0, in-window operator-reported run gets
   `execution-blocked`; an absent, unmarked or mismatched record renders "Not
   verified" with its own reason. Both are Unknown, so nothing over-claims.
   *Repair (optional):* "renders Unknown (`execution-blocked` for a matching
   operator-reported run)".

## Acceptance criteria

- **AC1, not met.** [Observed] The live test now has one process start, the
  literal `git rev-parse HEAD` (`:61`), plus the git fallback (`:130`); the
  sync guard has no exemption (`EXEMPT = new Set<string>()`). The round-3
  evasions are rejected: `.call`, `.apply` and the alias are `it.each`
  fragments in both checks, non-literal commands are refused, and a rename is
  refused in the capture check (and as `binds execFileSync as …` in the
  closure). The 89 computed-key sites are real: widening the rule to the whole
  closure in scratch gave 89 violations (1 + "…(88)") [Observed]. But
  findings 1 and 2 are trivial bypasses outside the stated residual.
- **AC2, met** [Observed]. The three variables are read from the environment
  and named as operator-reported in each assertion message; the exit status
  must be the string `'0'` and HEAD must equal the reported commit before
  anything is read; the file goes through `readBoundedRegularFile` and its
  bytes go to `buildOperatorReportedTestArtifactRecord`; the record's
  `provenance` must be `operator-reported`; the model must equal
  `{ kind: 'reported', tier: 'report-fact', record, disclosure:
  OPERATOR_REPORTED_DISCLOSURE }`. The source check pins these literals and
  refuses `readFileSync` and `toBe('verified')`.
- **AC3, met.** Note 1: the capture tool's rule is as stated
  (`capture-test-artifact-main.test.ts:156-165`), with six fragments. Note 2:
  `coreImports` reads `propertyName ?? name` and refuses namespace, default,
  side-effect and re-export forms (`:175-194`), with five fragments. Note 3:
  the sentence is present and accurate against POC-REQ-043 (a sweep for
  "verif" in the POC spec gives 7 lines, none a positive obligation) and the
  2026-08-29 direction's line 20 ("verification against the named intent
  revision"); see note 6. Note 4: the attribute is gone from the span, and
  the test asserts its absence on the badge and the whole card.
- **AC4, met** [Observed]. Both evidence files record `old`/`new` fragments,
  the run commit, exit, test count, failing names and `shSentinelWritten`.
  `git diff --stat ff2b53de 1d053f12` and `86364b2a..1d053f12` touch only the
  two evidence files, so the subjects are the head's bytes. I recomputed 6 of
  6 live-test `subjectDigests` (`b251ae99…`, `b58f467b…`, `a0774fc8…`,
  `cb66a5ff…`, `01fc9039…`, `8fdd9465…`) and 5 of 10 z774 digests
  (`c913063d…`, `547176f2…`, `18b4034f…`, `2eea9ae6…`, `119fe69c…`) with
  `sha256sum`; all match. #383's
  `capture-test-artifact-no-spawn-mutants-2026-10-07.json` is not in the PR's
  diff.
- **AC5, met** [Observed]. The committed round-3 raw is byte-identical to the
  reviewer's scratch copy (`git diff --no-index`, empty). The README row
  quotes `CONFIRM WITH EXCEPTIONS` at `:2`, and the partition is 366/366
  (above). The PR touches nothing under `.syzygy/**` or `openspec/**`.

## Count

Findings: 6 — 2 REVISE (1, 2), 4 NOTE (3, 4, 5, 6).
