# R-CAPTURE-TEST-ARTIFACT-NO-SPAWN-2
Verdict: REVISE
Reviewed commit: 0e6b549242ed9568c912df3e28770c8bfdf26dfe
Subject: PR #383 (syzygy-4mbu)

Reviewer: fresh-context agent, 2026-10-07, round 2. I read the bytes with
`git diff origin/main...0e6b5492…` and `git show 0e6b5492…:<path>`. I ran
the tests in a scratch `git worktree add --detach` at the head, after
`npm ci`. The five-file command recorded in the evidence file gave 5 files
and 94/94 passed [Observed]. No content of any target or external
repository was fetched. The scratch worktree has been removed.

## Governing references (quoted; located by `DIRECTIVE-REGISTER.md`)

- Direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07` item 4
  (`.syzygy/governance/decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:46`):
  "test-capture tool (`npm run poc:capture-test-artifact`) is to stop running
  the observed project's tests itself: it prints the command for the
  operator to run and ingests only the result file the operator hands it."
- SEC-3 (register row `DIRECTIVE-REGISTER.md:49` →
  `.syzygy/governance/doctrine/security.md:61`): "Syzygy runs observed-project
  code only inside an explicit, opt-in execution profile." Its bullet at :65:
  "What this binds: Syzygy itself, every process Syzygy launches or
  schedules, and every instruction a Syzygy feature gives an agent (a brief,
  prompt, skill or work item)."
- RFC5-18 (register row :342 →
  `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md:91`):
  "Observed-project code executes only when all of: (a) this RFC is
  accepted; (b) an execution profile …; (e) the run is captured as an
  Execution record …"
- RFC5-19 (register row :343 → same file :130, text at :140-150): "Consuming
  evidence produced outside Syzygy … is observation, not execution — no
  profile is required to read a report" and "This boundary governs whether a
  profile is required; it confers no tier. … an artifact of unverifiable
  origin caps at `report-fact` however retained, well-formed, and
  revision-bound it is. Reading is free; being believed is not."

## Round-1 finding dispositions

| R1 # | Round-1 tag | Disposition | Evidence |
|---|---|---|---|
| 1 | REVISE (AC4): operator exit status rendered "Observed / Verified" | **Repaired** | [Observed] The record type is now a union. `OperatorReportedTestArtifactRecord` (`provenance: 'operator-reported'`, `ingestedAt`, no `capturedAt`) is at `test-artifact-verification.ts:44-47`. The resolver returns `{kind:'reported', tier:'report-fact', disclosure}` and never `verified` for it (`:480-483`). Trajectory renders it as `epistemic-unknown` with `data-evidence-tier="report-fact"`, the label "Not verified by Syzygy — operator-reported (report-fact)" and the RFC5-19 disclosure (`trajectory.ts:79-85`). `model.ts:568-571` adds it to the Unknown subjects. The record reader refuses mixed timings (`isTestArtifactRecord`, `:79-84`). The consumer sweep finds three consumers, two `kind === 'verified'` comparisons and zero `case 'verified':` arms. My own grep for `'verified'` in non-test `apps/`, `packages/` and `scripts/` agrees: two comparisons in `trajectory.ts`, two definition sites in core. |
| 2 | REVISE (AC3): unbounded / non-regular read; quadratic regex; double parse | **Repaired** | [Observed] `readBoundedRegularFile` (`test-artifact-verification.ts:181-209`) does `lstat` → regular-file and size check → `open(O_NOFOLLOW\|O_NONBLOCK)` → `fstat` dev/ino match → reads at most max+1 bytes. The 4 MiB ceiling is `:137`. The regexes are replaced by forward scans (`firstOpeningTagBody` `:149-164`, `parseTagAttrs` `:213-229`); by reading, each is linear (every loop step advances the index). Timing tests at the ceiling are in `test-artifact-verification.test.ts`. Run-check tests cover FIFO, symlink, oversize and exact-ceiling. `buildOperatorReportedTestArtifactRecord` parses once (`:358`), and `ingestTestArtifact` no longer parses. |
| 3 | REVISE (AC5): source check missed `getBuiltinModule`; M6 killed incidentally | **Repaired as specified; a residual of the same class remains (new finding 1)** | [Observed] A TypeScript-AST check now forbids these identifiers: `getBuiltinModule`, `dlopen`, `binding`, `globalThis`, `global`, `eval`, `Function`, `require`, `Worker`, `Reflect`. It also forbids non-member use of `process`, bracket access on `process`, dynamic `import()`, and imports outside an allow-list (`capture-test-artifact-main.test.ts:76-121`). Mutants M7 (no cast) and M8 (bracket via alias) each start `sh` (`shSentinelWritten: true`) and are killed by the source check alone, on their own merits. |
| 4 | NOTE: negative / non-numeric counts; zero tests at status 0 | **Repaired** | [Observed] `COUNT = /^(?:0\|[1-9][0-9]{0,8})$/` is applied to every present count, and counts above the total are refused (`:233-249`). Zero tests at status 0 is refused (`:368-372`). Tests and mutants M11 and M12 cover these. |
| 5 | NOTE: "capture time" wording; dirty tree undetected | **Repaired** | [Observed] `docs/THREE-SURFACE-POC.md` now says "the ingest time is neither after the evaluation nor earlier than the commit itself. Passing this says nothing about when the tests ran." It also discloses that a switched checkout and uncommitted changes go undetected, and so do the printed text and the disclosure. |
| 6 | NOTE: SEC-3 agent-instruction line | **Repaired** | [Observed] `capture-test-artifact.ts` prints "For the owner or a human operator. An agent session must not run step 2 / unless the owner has recorded a SEC-3 choice for that run." USAGE and the docs carry the same line, and a test asserts it. |
| 7 | NOTE: no subject digest in the evidence record | **Repaired** | [Observed] `subjectDigests` lists 10 files. I recomputed all 10 with `sha256sum` at the head and all 10 match. `git diff --stat bbf9dd1f 0e6b5492` changes only the evidence file, so the digests hold for the reviewed commit. |
| 8 | NOTE: imported core barrel binds `execFileSync` elsewhere | **Partly addressed; unchanged residual** | [Observed] The check now requires every core import to be exported by `test-artifact-verification.ts`, and it applies the AST check to that file. The tool still imports the package barrel, so every core module is loaded. Round 1's [Inferred] point stands: no core module makes a top-level spawn call. No action required. |

## New findings

1. **REVISE (AC1, AC5) — a string-evaluation route reached through
   `.constructor` starts a process and passes every check. The source check
   forbids the names `Function` and `eval` but not the Function constructor
   reached as a property.**
   AC1 requires every indirect route to be rejected by the source check.
   The PR's own list names "evaluation of a string"
   (`capture-test-artifact-main.test.ts:84-87`). Its word regexes and the
   AST check only look for the identifiers `Function` and `eval`. Every
   object's `.constructor.constructor` is `Function`, and an allowed member
   of `process` is an object.
   I applied this mutant to the scratch worktree only, as the first line of
   the `print` branch of `capture-test-artifact-main.ts`:
   ```ts
   const g = (process.stdout.constructor as unknown as { constructor: (s: string) => () => Record<string, (n: string) => Record<string, (...a: unknown[]) => unknown>> }).constructor('return this.process')();
   g[['get', 'Builtin', 'Module'].join('')]?.(['child', 'process'].join('_'))[['spawn', 'Sync'].join('')]?.('sh', ['-c', 'touch <scratchpad>/EVADED-R2']);
   ```
   Result [Observed]: the evidence file's five-file command passed 94/94,
   and the sentinel `EVADED-R2` existed afterwards, so `sh` was started.
   - The AST check sees `process` only as `process.stdout`, which is allowed.
   - `getBuiltinModule` appears only as split strings.
   - The bracket access is on `g`, not on `process`.
   - `constructor` is not a forbidden name.
   - The run check traps only the `--python` binary.

   I did not establish whether the mutant typechecks: an app-wide `tsc` in
   the scratch tree failed on unbuilt sibling packages [Unknown]. Vitest
   does not typecheck, and the casts go through `unknown`, so it would
   likely typecheck [Inferred].
   The code as shipped starts only `git rev-parse HEAD` [Observed by
   reading]. What fails is the second half of AC1, the guard: a future edit
   of this shape regresses silently.

   *Repair*, in either form:
   - (a) Add `constructor`, `prototype` and `__proto__` to
     `FORBIDDEN_IDENTIFIERS` and to the `indirect` regex. Also reject every
     `ElementAccessExpression` whose argument is not a numeric or plain
     string literal, in all three checked files. Without that,
     `x['constr' + 'uctor']` still evades.
   - (b), more robust and spelling-independent: make the run check
     execute the CLI in a child `node` run with
     `--disallow-code-generation-from-strings`, under Node's permission
     model (`--permission`, no `--allow-child-process`) for `print`. For
     `ingest`, a test-injected commit resolver lets it run under the same
     flags. Any spawn then throws, however it is spelled.

   Record this mutant, with its old/new fragment, in the evidence file,
   killed by whichever guard is added.

2. **NOTE (AC4) — a record with no `provenance` still renders "Verification:
   Verified" as Observed, and nothing lawful produces such a record any
   more.**
   `isTestArtifactRecord` (`test-artifact-verification.ts:79-84`) accepts
   `{capturedAt, no provenance}`, and the resolver returns `verified` for it
   (`:483`). The docs say so honestly: "only for a record whose exit status
   and capture time the capturing process observed itself, which this tool
   no longer produces."
   Any such record now in a state directory therefore either predates this
   PR, produced by the old spawn that this PR retires as SEC-3-non-compliant,
   or was hand-written. Either way it shows Observed/Verified with no
   disclosure. Whether a live state directory holds one is [Unknown]. This
   is not an operator-reported value, so AC4 as written holds, but it sits
   in the same honesty space. *Repair (optional):* have the reader map a
   no-provenance record to `reported`/Unknown with a "legacy capture"
   disclosure, or have the tool's docs tell the operator to clear the state
   file (`clearTestArtifactRecordFile`). Or record the owner's choice to keep
   legacy records Verified.

3. **NOTE (AC4) — the consumer count omits the machine channel.**
   `routes.ts:233` serves `JSON.stringify(model)` at `/api/poc`, which
   carries `testArtifactVerification` verbatim. The sweep's `CONSUMER`
   regex (`test-artifact-verification-consumers.test.ts:31`) matches only
   `.testArtifactVerification` and the type name. It would also miss a
   destructuring reader (`const { testArtifactVerification } = model`).
   The wire value is self-describing (`kind: 'reported'`,
   `tier: 'report-fact'`, `disclosure`), so nothing reads as verified there
   [Observed by reading]. But the PR body's "three consumers" is a count
   over one predicate, not over every reader. *Repair:* name the machine
   channel in the PR body and in `EXPECTED_CONSUMERS`'s commentary, and add
   `\btestArtifactVerification\b` (bare) to the sweep.

4. **NOTE — the Unknown subject for a reported run uses reason code
   `missing-evidence`** (`model.ts:570`). The evidence is present but capped
   at `report-fact`, and `missing-evidence` tells a machine reader something
   different from "reported, not believed". If the reason-code vocabulary
   (RFC2-24) has a closer code, use it; otherwise disclose the mapping. Not
   blocking: the human surface carries the full disclosure.

5. **NOTE — the "file's digest" is the digest of the UTF-8-decoded string,
   not of the file bytes.** `readBoundedRegularFile` returns
   `buffer.toString('utf8')` (`:205`), and `junitDigest` re-encodes it
   (`:296-298`). For bytes that are not valid UTF-8, the stored digest
   differs from `sha256sum` of the handed-in file [Inferred from Node's
   replacement-character decoding]. This behaviour predates the PR, but
   `docs/THREE-SURFACE-POC.md` now says "the file's digest". *Repair:* hash
   the raw buffer, or say "digest of the decoded text".

6. **NOTE — duplicate attributes resolve last-wins** (`parseTagAttrs`,
   `Map.set`). For example, `failures="1" … failures="0"` reads as 0 and
   passes the status-0 check. pytest does not emit duplicates, and the
   operator can edit the bytes anyway, so this is consistency only.
   Refusing a duplicate count attribute would be fail-closed.

## Acceptance criteria summary

- AC1: the code meets it, but the guard does not — new finding 1 (REVISE).
- AC2: met [Observed]. `print` calls only `io.stdout(operatorInstructions(…))`
  and prints the exact command with the SEC-3 agent line.
- AC3: met [Observed]. Bounded regular-file read, linear scans, a single
  parse, and refusals for a moved checkout, an exit status that is not an
  integer 0–255 (or is written with a leading zero), non-integer, negative
  or over-total counts, status 0 beside failures, and zero tests at status 0.
- AC4: met for operator-reported values on every consumer found
  [Observed]. Notes 2–4.
- AC5: largely met. Old/new fragments, commit and 10 subject digests are
  all verified, and M7/M8 are killed on their own merits. The new evasion
  in finding 1 is unrecorded and survives.
- AC6: met [Observed]. No `CONTRACT-COVERAGE.md` is in the diff. The round-1
  raw at the head has blob `6424fa6a…`, identical to the retained scratch
  copy (`git hash-object`). There is a `docs/README.md` row, and the
  partition script carries the campaign pattern.

## Count

Round-1 findings: 7 of 8 repaired, and 1 (R1-8) partly addressed with no
action needed. R1-3 is repaired as specified, with a residual carried as
new finding 1.
New findings: 6 — 1 REVISE (1), 5 NOTE (2, 3, 4, 5, 6).
