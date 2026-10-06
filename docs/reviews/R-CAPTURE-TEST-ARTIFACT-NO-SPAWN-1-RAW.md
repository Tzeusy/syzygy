# R-CAPTURE-TEST-ARTIFACT-NO-SPAWN-1
Verdict: REVISE
Reviewed commit: 0c59614c9cc2ddfc868ffe921ea7192a0b3f343d
Subject: PR #383 (syzygy-4mbu)

Reviewer: fresh-context agent, 2026-10-07. Bytes read with
`git show 0c59614c…:<path>` and `git diff origin/main...0c59614c…`. Tests run
in a `git archive` export of the head in a scratch directory (`npm ci`, then
`vitest run apps/three-surface-poc/src/capture-test-artifact`): 2 files, 29/29
passed [Observed]. No content of any target or external repository was
fetched.

## Governing references (quoted)

- Owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07` item 4
  (`.syzygy/governance/decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md`
  lines 43-50): "The test-capture tool (`npm run poc:capture-test-artifact`)
  is to stop running the observed project's tests itself: it prints the
  command for the operator to run and ingests only the result file the
  operator hands it."
- SEC-3 (`.syzygy/governance/doctrine/security.md:61-62`): "Syzygy runs
  observed-project code only inside an explicit, opt-in execution profile."
  Its binding bullet: "What this binds: Syzygy itself, every process Syzygy
  launches or schedules, and every instruction a Syzygy feature gives an
  agent (a brief, prompt, skill or work item)."
- RFC5-18 (`.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md:91`):
  "Observed-project code executes only when all of: (a) this RFC is
  accepted; (b) an execution profile …"
- RFC5-19 (same file): "Consuming evidence produced outside Syzygy … is
  observation, not execution — no profile is required to read a report" and
  "This boundary governs whether a profile is required; it confers no tier.
  … an artifact of unverifiable origin caps at `report-fact` however
  retained, well-formed, and revision-bound it is. Reading is free; being
  believed is not."
- Clause location: a `DIRECTIVE-REGISTER.md` row grep for `SEC-3`/`RFC5-18`
  with my table-row pattern returned nothing; I located both clauses by
  `git grep -F` over the doctrine and installed RFC trees at the reviewed
  commit instead [Observed].

## Acceptance criteria summary

- AC1 (no process but `git rev-parse HEAD`): met by the code as written
  [Observed]. `capture-test-artifact-main.ts:37` is the only process start;
  `capture-test-artifact.ts` imports only core pure functions; the core
  functions it calls (`parseJUnitRootTotals`, `buildTestArtifactRecordFromJUnit`,
  `writeTestArtifactRecordFile`) start nothing
  (`packages/three-surface-poc-core/src/test-artifact-verification.ts`).
- AC2 (`print` prints an exact command, starts nothing): met [Observed]
  (`capture-test-artifact-main.ts` print branch calls only `io.stdout`).
- AC3: partly met — see finding 2 (REVISE) and finding 4 (NOTE).
- AC4: not met — finding 1 (REVISE).
- AC5: partly met — finding 3 (REVISE), finding 7 (NOTE).
- AC6: met. The diff touches exactly six files
  (`git diff --stat origin/main...0c59614c`); no `CONTRACT-COVERAGE.md`
  (four tracked copies under `openspec/changes/`, plus candidate `.patch`
  files) is among them [Observed]. Docs mostly match behaviour; one stale
  phrase in finding 5.

## Findings

1. **REVISE (AC4) — an operator-reported exit status now feeds an
   "Observed / Verified" rendering with no provenance mark.**
   Before this PR Syzygy ran the command and observed the exit status itself
   (origin/main `capture-test-artifact.ts`, `exitCode = input.runCommand(...)`).
   Now `capture-test-artifact.ts:89-92` takes `--exit-code` from the operator
   and `:125-132` writes it into the same `TestArtifactRecord` shape
   (`test-artifact-verification.ts:11-19`), which has no field saying the
   exit status, the run itself, or "ran as printed" are self-reported.
   `resolveTestArtifactVerification` (`test-artifact-verification.ts:254`)
   gates `verified` on that number, and `trajectory.ts:75` renders it as
   `class="epistemic epistemic-observed"` "Verification: Verified", titled
   "A captured, passing focused-pytest artifact bound to commit …". What
   Syzygy actually observes is: the JUnit bytes' digest and root-tag totals,
   and that HEAD equalled the reported commit **at ingest time**. That
   the tests ran, at that commit, on a clean tree, with that exit status, is
   operator report. RFC5-19 caps such an artifact at `report-fact`; VIS-2
   honesty forbids rendering it as Observed beyond what was verified. The
   USAGE text (`capture-test-artifact-main.ts`, "ingest time") is honest,
   but the record field is still named `capturedAt` and the verifier's
   "captured before the commit existed" guard (`test-artifact-verification.ts:273`)
   now compares *ingest* time, which is weaker than it reads.
   *Repair:* add a provenance field to the record (for example
   `provenance: 'operator-reported'` with `exitCodeSource` and
   `ingestedAt` naming), have `ingest` set it, and have the verified badge
   render that case as Inferred / report-fact with a disclosure ("exit
   status and run reported by the operator; Syzygy observed the artifact
   digest and HEAD at ingest"). If the owner prefers to keep the badge as
   is, that is a rendering-posture decision to put to the owner, not to
   leave implicit.

2. **REVISE (AC3) — no size or file-type bound on the handed-in file, and
   the root-tag regex is quadratic on hostile input.**
   `capture-test-artifact-main.ts:43` is `readFileSync(path, 'utf8')` on any
   resolved path: no size cap, no regular-file check (a FIFO blocks forever;
   `/dev/zero` reads until memory fails). The JUnit bytes are produced by
   running observed code, so they are untrusted. `TESTSUITE_TAG_PATTERN =
   /<testsuite\s+([^>]*?)\/?>/i` (`test-artifact-verification.ts:103`) is
   O(n^2) with many unterminated opening tags. Measured with Node on this
   host [Observed]: `'<testsuite a'` repeated 20,000 / 40,000 / 80,000 times
   (240 KB / 480 KB / 960 KB) took 1,885 / 7,541 / 30,713 ms for one `exec`.
   `ingestTestArtifact` now parses the same bytes twice
   (`capture-test-artifact.ts:117` and inside `buildTestArtifactRecordFromJUnit`),
   and on no match the `<testsuites` pattern runs too, so a 1 MB file costs
   about two minutes and a few MB is effectively a hang. XML-parser hazards
   (XXE, entity expansion) do not arise, since no XML parser is used
   [Observed]. *Repair:* `statSync`/`fstat` the path, refuse anything that
   is not a regular file or exceeds a stated ceiling (pytest JUnit for a
   focused scope is small; for example 4 MiB), and either bound the regex
   scan to a prefix window or replace it with an `indexOf`-based scan of
   the first `<testsuite` tag. Add tests for oversize, non-regular, and the
   pathological-tag input.

3. **REVISE (AC5) — the source check does not name `process.getBuiltinModule`.
   A mutant that uses it to start a non-python process survives both
   checks, and recorded mutant M6 was killed by an incidental type
   annotation, not by the check its id names.**
   The starters regex (`capture-test-artifact-main.test.ts:83`) and the token
   list after it cover `spawn…(`, `exec…(`, `fork(`, `import(`, `require(`,
   `process.binding`, `Worker`, `node:worker_threads`, `node:vm`, but not
   `getBuiltinModule`, `process.dlopen`, `eval` or `Function(`. The run check
   traps only the `--python` binary. I applied this mutant to the scratch
   export only, in the `print` branch:
   `(process as unknown as { getBuiltinModule(n: string): Record<string, (...a: unknown[]) => unknown> }).getBuiltinModule(['child', 'process'].join('_'))[['spawn', 'Sync'].join('')]?.('sh', ['-c', 'touch <scratch>/EVADED']);`
   Result: 29/29 passed, and the sentinel file `EVADED` existed afterwards
   [Observed]. So a process was started and no test failed. The evidence
   file's `M6-builtin-module-evades-source-check` lists three source-check
   failures, but those fire because its fragment contains
   `as typeof import('node:child_process')` (matches `\bimport\s*\(` and the
   module literal), not because `getBuiltinModule` is guarded [Observed by
   reading the fragment against the regexes]. Its `print` run-check failure
   is real, because it spawns the trap python. AC1 names
   `process.getBuiltinModule` explicitly.
   *Repair:* add `getBuiltinModule`, `process.dlopen`, `\beval\s*\(` and
   `\bFunction\s*\(` to the forbidden tokens. Optionally harden the run check
   by running the CLI with a `PATH` whose `sh`, `bash`, `pytest`, `python`
   and `python3` are trap shims. Record a re-run mutant without the type
   annotation (the one above, or M6 with the cast removed), showing it
   killed by the source check.

4. **NOTE (AC3) — the "status 0 beside failing tests" refusal can be
   sidestepped by non-integer or negative counts, and a zero-test run is
   accepted at status 0.**
   `totalsFromAttrs` (`test-artifact-verification.ts:132`) maps a
   non-numeric `failures` to 0 and accepts negatives. `failures="-1"
   errors="1"` sums to 0, so `capture-test-artifact.ts:118` does not refuse,
   and `failures="x"` reads as 0 [Observed by reading; not executed].
   `tests="0"` at status 0 is accepted, though pytest exits 5 when it
   collects nothing [Inferred from general pytest knowledge]. The operator
   can edit the bytes anyway, so this is a consistency check and not a
   security boundary. Still, fail-closed means refusing what cannot be read.
   *Repair:* in `ingest`, require every present count to be a non-negative
   integer and refuse `tests == 0` at status 0, and test both cases.

5. **NOTE (AC4/AC6) — commit binding is "HEAD at ingest equals the reported
   commit". The docs still call the timestamp "capture time".**
   A checkout switched between steps 2 and 3 and back, or a dirty working
   tree, goes undetected (`capture-test-artifact.ts:97-108`). In
   `docs/THREE-SURFACE-POC.md` §"Capturing test-run evidence", the bullet
   "the capture time is neither future-dated nor earlier than the commit
   itself" now means ingest time, while the bullet above it correctly says
   "ingest time". *Repair:* reword to "the ingest time …". Optionally
   disclose that a dirty tree is not detected, or check
   `git status --porcelain` empty. That is a second git process, so AC1's
   wording and the source check would need to admit it.

6. **NOTE (SEC-3) — the printed text is an instruction to run observed
   code, and SEC-3 binds "every instruction a Syzygy feature gives an
   agent".**
   The owner direction addresses "the operator" and chose this design, and
   the text says "Run these yourself, in your own shell"
   (`capture-test-artifact.ts:46-58`). If an agent session runs `print` and
   follows its output, though, the instruction reaches an agent, and
   SEC-3's permitted case needs a per-run owner choice recorded first.
   *Repair:* add one line to the printed text and to the docs: "For the
   owner or a human operator. An agent session must not run step 2 unless
   the owner has recorded a SEC-3 choice for that run."

7. **NOTE (AC5, rule 6/11) — the evidence record has old/new fragments and
   a commit, but no subject digest, and its commit becomes unreachable on
   rebase-merge.**
   `docs/evidence/capture-test-artifact-no-spawn-mutants-2026-10-07.json`
   records `commit: d7d8244d…`, every mutant's `old`/`new` fragments, its
   exit, its test count and the failing test names [Observed]. Between
   d7d8244d and the head, only the evidence file changes [Observed:
   `git diff --stat`]. Under rule-6 lesson (AGENTS.md), a rebase-merge
   leaves that commit reachable from no ref. Rule 11 asks for the subject's
   digest. *Repair:* add a `subjectDigests` map (sha256 of the four source
   and test files at the run) so the record can be re-checked after merge.

8. **NOTE (AC1) — the source check covers two files. Their imported core
   barrel binds `execFileSync` in other modules.**
   `@syzygy/three-surface-poc-core` modules such as `work-items.ts`,
   `materialization.ts` and `code-structure.ts` import `execFileSync`
   [Observed]. This tool's call path reaches none of them [Observed by
   reading the three functions used], and importing them runs nothing at
   load [Inferred; no top-level calls were swept]. No change required; a
   future edit that calls one of those helpers from this tool would pass the
   source check, though the run check might catch it.

## Count

8 findings: 3 REVISE (1, 2, 3), 5 NOTE (4, 5, 6, 7, 8).
