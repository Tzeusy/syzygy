# R-GP-IMPL-LAUNCHED-MARKER-2 — CC-REV-1 implementation review of syzygy-bpyt.8.8, round 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: cf3ba3fe
Subject: r2-review.diff sha256 42f082bd2852be4e0ef0ba35e75cb44656621e885b0f635601afd182127dd9bd

Reviewer: a fresh-context CC-REV-1 reviewer for class 4 (security), round 2. I did not author the change and I did not write round 1.
I fetched no target-repository content, read no observed repository body, and made no network fetch. I did not edit the worktree.
Every mutant, harness and probe ran in a scratch clone of the worktree at `cf3ba3fe`, with its own `npm ci`. I made no `bd`
mutation, no commit and no push.

## 1. Subject identity checks

- [Observed] `sha256sum` of `lead/b88/r2-review.diff` gives
  `42f082bd2852be4e0ef0ba35e75cb44656621e885b0f635601afd182127dd9bd`, the digest in the brief.
- [Observed] `git diff fe20dd5f cf3ba3fefb3969e2293afb0038685b4cd41e6788` in the worktree, written to a scratch file, hashes to the
  same digest. HEAD is `cf3ba3fefb3969e2293afb0038685b4cd41e6788`; `fe20dd5f` resolves to `fe20dd5fda6c99925f6ec33e126775dc583ab07a`,
  which is `origin/main` in the worktree. The worktree was clean.
- [Observed] The diff touches 21 files, with 5063 insertions and 25 deletions:
  - eight source files under `packages/polaris-dossier/src/` (`brief.ts`, `cli.ts`, `execution-rule.ts`, `index.ts`, `inventory.ts`,
    `launched.ts`, `review.ts`, `session-handover.ts`);
  - seven test files, one of them new (`launched.test.ts`);
  - four evidence records under `docs/evidence/` (round 1's two and round 2's two);
  - the round-1 raw, `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-1-RAW.md`;
  - `docs/README.md`.
- [Observed] `git diff --stat cc0aba21 HEAD -- packages` lists only five files under `packages/three-surface-poc-core/` (from the
  merge of main). No file under `packages/polaris-dossier/` differs between the round-2 evidence commit `cc0aba21` and HEAD, so both
  round-2 records describe the reviewed code and tests.
- [Observed] A script (`check_subject_digests.py`) made 74 checks with 0 mismatches:
  - the differential's 16 subject digests, base side at `fdc866af` and fix side at `cc0aba21`, plus its 8 fix-side digests against
    HEAD;
  - the differential's stored driver and harness texts against their declared sha256;
  - the mutants record's 6 subject digests at `cc0aba21` and at HEAD;
  - each of the 18 mutants' `old` fragment occurring exactly once in its file, at `cc0aba21` and at HEAD.
- [Observed] `git diff fdc866af fe20dd5f -- packages/polaris-dossier` is empty, so the differential's base (`fdc866af`) and this diff's
  base (`fe20dd5f`) hold the same `polaris-dossier` bytes.
- [Observed] The round-1 evidence files are byte-unchanged since `e632d276`, and the round-1 raw since `f56dccce` (`git diff --stat`
  empty for each). The retained raw hashes to `1d8ea7c8b28762be27dc28b14eb49876db6efca5aee19972b6d64958a3099360`, the same as the
  round-1 reviewer's own file under `lead/b88/reviewer/`, so it was retained verbatim (CC-REV-6).

## 2. Clauses relied on

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:18-20, 37`): "Changes touching any of seven
  classes require review by an independent, fresh-context reviewer"; class 4 is "**security** — anything under SEC-1…SEC-5, auth
  surfaces, egress paths".
- **SEC-3 as amended by D9** (`.syzygy/governance/doctrine/security.md`):
  - lines 65-69: "**What this binds:** Syzygy itself, every process Syzygy launches or schedules, and every instruction a Syzygy
    feature gives an agent (a brief, prompt, skill or work item)";
  - lines 90-91: "**Whom the case binds:** Syzygy. Syzygy never gives the instruction to a session it started or to one left running
    unattended";
  - lines 95-99: "**What the permitted case costs:** the session runs with the owner's own credentials and network … Nothing contains
    it, so it gives none of a profile's guarantees."
- **REQ-polaris-generation-033** (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:15`): the brief
  may say the agent may build and run the observed project only when, among other things, the authoring session is one the owner
  started and attends, "never a session Syzygy started, one left running unattended, or one left under an automatic-approval or
  permission-bypass setting while the owner is away"; "Otherwise the brief SHALL carry SEC-3's rule".
- **Candidate REQ-polaris-generation-041** (`openspec/changes/polaris-dossier-one-command-run/proposed/polaris-generation/spec.md:65`;
  the file's head says "Candidate exact behavioral delta; not adopted, binds nothing"): "An inventory or verdict from a launched run
  SHALL count only when its session's launch record exists and names that session's directory; Syzygy SHALL refuse a declared
  `terminal` or `bang` launch form in a launched run."
- **Candidate REQ-polaris-generation-044** (the same file, line 208; candidate): "Syzygy SHALL refuse `allow-execution` for a launched
  run". Its falsifier (line 231) begins "An execution choice is recorded for a launched run; a brief of a launched run permits
  execution".
- **The owner's approval** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - lines 61-66: pull requests touching class 1, 3 or 4 get "an old-versus-new differential over a mutated-record corpus that
    includes records with altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report";
  - line 93: "New | `isLaunchedRun` is read fail-closed, at both `allow-execution` and brief issuance";
  - lines 95-96: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- **The owner's 2026-10-21 answer**, as recorded on bead `syzygy-bpyt.8.8` (`bd comments`, read-only; comment by Tzeusy at 11:33):
  "'Cover every reader (Recommended)': the GP-Q0 Part 3 approval of reading isLaunchedRun fail-closed covers every reader of the
  launched marker, including launch-form and the inventory and review of-record counters, not only allow-execution and brief
  issuance; the PR lists each changed refusal."
- **The bead** (`bd show syzygy-bpyt.8.8`): acceptance criteria "1. Both sites refuse on a present-but-unreadable or malformed marker;
  absent marker unchanged. 2. Brief bytes unchanged for every existing fixture (flag off). 3. PR lists each changed refusal. 4.
  Recorded rule-6 mutants; CC-REV-1 class-4 review raw retained."
- **AGENTS.md**: verification rules 2, 4, 6, 9, 10 and 11; the guardrails "Fail-closed polarity: withdrawal defeats grant;
  future-dated evidence is stale; no evidence → Unknown", "Conformance expected values are hard-coded literals, never imported from
  the module under test", the rule-6 record guardrail ("must store each mutant's `old`/`new` fragment and the commit it ran at"), and
  "The PWB-REQ-014 authority sweep reads evidence-record keys".

## 3. What I ran and the results

All runs used the scratch clone at `cf3ba3fe` with `npm ci`, on Node v24.6.0, as uid 1000 (not root).

1. **The full `@syzygy/polaris-dossier` vitest project.** [Observed] Result lines, verbatim:
   - `Test Files  29 passed (29)`
   - `Tests  1175 passed | 1 skipped (1176)`

   A grep of the log for `FAIL` finds nothing. The one skip is the no-strace placeholder at `no-egress.test.ts:94-96`
   (`describe.skipIf(HAVE_STRACE)`). It is skipped because `strace` is installed on this host, so the strace capture at line 62 ran.
   No load flake occurred.
2. **`npm run typecheck`.** [Observed] Exit 0. The output is only npm's two header lines (`> typecheck` and the `tsc -b …` command),
   with no diagnostic.
3. **`python3 scripts/check_governance.py`.** [Observed] Exit 0. The result line, verbatim: `32 OK, 21 WARN, 0 FAIL (53 checks) —
   counts derived, not asserted`. One output line names a changed file: the CG-1f block ("frozen-lane path references — 396
   references examined, 0 findings") prints `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-1-RAW.md -> inventory/session-1.launch.json` as a
   classified raw-review reference, not a finding.
4. **`python3 scripts/check_docs_review_campaign_partition.py --check docs/README.md`.** [Observed] Exit 0, verbatim:
   - `second-method PASS: git ls-files=488; git ls-tree=488; exact path sets equal`
   - `partition PASS: denominator=488; assigned=488; raw=454; other=34; unmatched=0; overlaps=0; campaigns=103`
5. **The PWB-REQ-014 authority sweep** (`apps/three-surface-poc/src/polaris-authority-sweep.test.ts`, because the round-1
   differential record carries a JSON key named `source`). [Observed] `Test Files  1 passed (1)`, `Tests  5 passed (5)`.
6. **The rule-6 mutants, re-run from the round-2 record** (`run_mutants.py`, which applies each recorded `old`/`new` verbatim, runs
   the recorded command in its own process group under the recorded 240 s timeout, restores the bytes and checks their digest).
   - [Observed] Unmutated: `Tests  229 passed (229)`, exit 0, as recorded.
   - [Observed] All 18 mutants reproduce their recorded `Tests` line, exit code and blocked flag exactly. With durations removed,
     the failing-test name sets are equal for all 18. `open-blocks` blocked and was killed at 240 s, as recorded. Every file was
     restored to its digest.
   - [Observed] The two recorded survivors survive: `any-file-type` and `inventory-brief-marker-not-read`, each `Tests  229 passed
     (229)`.
7. **My extra mutants**, with the same command and timeout:
   - **The `any-file-type` mutant plus one new fixture** (a FIFO that holds the marker's bytes; text in §5, R2-N2): **killed**,
     `Tests  1 failed | 230 passed (231)`. The one failure is the new fixture. [Observed]
   - **X1**, `review.ts:664` wording reverted to the old ternary form (`launchedMarkerState(run) === 'launched' ? 'a syzygy-launched
     launch' : 'a terminal or bang launch'`): **survived**, `Tests  229 passed (229)`. This is round 1's N5, still open. [Observed]
   - **X2**, `brief.ts:226` reading the marker eagerly (`launched: ((state) => () => state)(launchedMarkerState(run))`): **survived**,
     `Tests  229 passed (229)`. See R2-N4. [Observed]
   - **X3**, the same eager read at `inventory.ts:235`: **survived**, `Tests  229 passed (229)`. [Observed]
8. **The differential, re-run from its record.** I wrote the stored `driver.text` and `harness.text` out to files whose sha256
   matched the declared values. I ran `python3 drive.py <clone> fdc866af… <scratch> <out.json>` as the record's `command` states,
   with the clone as the worktree argument.
   - [Observed] The driver reports `done 19 19`, fix `cf3ba3fe…`, `trackedTreeClean: true` and 8 subject files.
   - [Observed] Compared with the recorded rows (`compare_differential.py`): 19 variants × 5 probes × 2 sides = 190 side
     comparisons, 0 mismatches. A blocked side compares on its `blocked` flag alone.
   - [Observed] Classified independently (`classify_changes.py`), both the record and my re-run give: 29 unchanged, 56 stricter, 4
     refused at both commits with a new reason, 6 not comparable (base blocked or not run), 0 more lenient.
   - [Observed] All 38 arm-off briefs (19 variants × 2 sides) share one byte pair: `brief.md`
     `af5253644108fad53e59187f757f6f0607c88bd881801e868f675dc5fe37feed`, `brief.json`
     `19feb99936b134767dfa2ecf7e302dc8244288fd72d6ca533cc8e83a60b67e12`.
9. **Reader probes beyond the recorded corpus.** Each ran against the built `dist/launched.js` in its own `node` process and process
   group under a 60 s kill timeout (`run_probes.py`, `probe-reader.mjs`). [Observed] HEAD's results:

| Marker state | HEAD (`launchedMarkerState`) |
|---|---|
| A FIFO that holds the marker's bytes (no writer left, a second reader keeps the pipe open) | `unreadable`; a `syzygy-launched` form is refused |
| A FIFO with a writer streaming data | `unreadable` in 312 ms |
| A Unix-domain socket at the name | `unreadable` |
| A symbolic-link loop | `unreadable` |
| A hard link to a valid marker | `launched` |
| A valid marker of exactly 4096 bytes / 4097 bytes | `launched` / `unreadable` |
| A UTF-16LE marker | `unreadable` |
| `{"__proto__": {"format": …}}` | `unreadable` |
| Duplicate `format` keys, the last valid / the last other | `launched` / `unreadable` |
| Non-UTF-8 bytes inside a string value of a valid marker | `launched` |
| A run directory of mode 000 holding a valid marker | `unreadable` |
| A run-directory name longer than `NAME_MAX` | `unreadable` |
| A run directory that is a symbolic link to a launched run | `launched` |
| A regular file of 231 bytes at `fstat`, grown to 64 MiB after it (deterministic hook) | `unreadable`, after `readFileSync(fd)` returned 67,108,864 characters |
| The same, grown to 4 GiB, under `prlimit --as=3000000000` | the process aborts: `terminate called after throwing an instance of 'std::bad_alloc'`, exit -6 |
| A 49-byte invalid prefix at `fstat`, appended after it into a valid marker of 5051 bytes | `launched` |
| An unprivileged process toggling the file between 231 bytes and 64 MiB, for 15 s | 903,433 calls; 588,531 passed the `fstat` check and reached the read; 386,653 of those read more than 4096 bytes, the largest 2,105,344 |

10. **Does the arm-off brief or the inventory brief open the marker?** I traced `openat`, `open` and `openat2` with `strace -f`.
    - [Observed] Over the five arm-off brief tests (`brief.test.ts`, "the permitting arm off, whatever the launched marker": no marker,
      the written marker, `null`, a FIFO and a link to `/dev/zero`), the only opens of `launched.json` are the two plant writes
      (`O_WRONLY|O_CREAT|O_EXCL|O_TRUNC` and `O_WRONLY|O_CREAT|O_TRUNC`). There is no read-side open.
    - [Observed] Over the inventory-brief test (`inventory.test.ts`, "prints Syzygy's own rendering…", which issues the arm-off
      authoring brief, hands the inventory session over and builds the inventory brief twice), there are 0 opens of `launched.json`,
      and 5 of `inventory-brief.md`. So the trace saw the brief work.
    - [Observed] Positive control: over the four arm-on brief tests ("gives SEC-3's rule, whatever choice it holds"), the reader's
      `O_RDONLY|O_NONBLOCK|O_NOFOLLOW|O_CLOEXEC` open appears once per variant.
11. **A FIFO or a large file at the run's own record.** [Observed] At HEAD, with `run.json` a FIFO and no marker, `syzygy dossier
    status` and `allow-execution` (through `runDossierCli` on the built CLI) both block until killed at 20 s. `status.ts:102` and
    `reverify.ts:103` read `run.json` with `fs.readFileSync(path, 'utf8')`.
12. **The proposed R2-N1 repair, applied to the built `dist/launched.js` and then restored** to its digest
    `1d58418602ef993889ee8f15692cd35653f09901e2090cf511cc1516c85e822d`. [Observed]
    - The two growth cases and the 4 GiB case read `unreadable` with no read beyond 4097 bytes. The 4 GiB case exits 0 under the same
      `prlimit`, and the grown-to-valid marker reads `unreadable`.
    - Every other probe above gives the same state as HEAD.
    - Applied to the clone's `src/launched.ts` and then reverted with `git checkout`, the recorded seven test files plus the two
      proposed tests give `Test Files  8 passed (8)`, `Tests  231 passed (231)`, and `npx tsc -b packages/polaris-dossier` exits 0.
    - At HEAD, the proposed growth test fails (`expected 'launched' to be 'unreadable'`) and the proposed FIFO test passes.
13. **Reader sweep** (`sweep_readers.py`, Python `re` over `git ls-files -z` at HEAD).
    - Denominator: 2956 tracked files; 2952 read as UTF-8 and 4 skipped (four `.png` files under `docs/evidence/`).
    - Patterns: `launched\.json`, `RUN_LAYOUT\s*\.\s*launched\b`, the bracket form, whole-object uses of `RUN_LAYOUT`
      (`Object.(values|keys|entries)`, spread, destructuring), `\blaunchedMarkerState\b`, `\bisLaunchedRun\b`,
      `\blaunchFormRefusal\b`, `\bexpectedLaunch\b`, `\bLAUNCHED_FORMAT\b`, `polaris-dossier-launched/` and
      `\bwriteLaunchedMarker\b`.
    - [Observed] Non-test code that opens the marker: `launched.ts:41/46` (the reader) and `launched.ts:74` (the writer), nothing
      else. `RUN_LAYOUT.launched` occurs only at those two lines, and the bracket form occurs nowhere.
    - [Observed] The one whole-object use is `status.ts:66`, `new Set(Object.values(RUN_LAYOUT))`, which `status.ts:179` uses only to
      name unrecognized entries; it opens nothing.
    - [Observed] The non-test callers of the reader are `cli.ts:365`, `brief.ts:226` (thunk), `inventory.ts:235` (thunk) and `:436`,
      `review.ts:664`, `session-handover.ts:555`, and `launched.ts:119` inside `launchFormRefusal`. `launchFormRefusal` is called at
      `inventory.ts:434` and `review.ts:662`.
    - [Observed] `isLaunchedRun` has 0 code-file hits; its 14 hits are in 5 docs and decision records.
    - [Observed] Second method: `git grep -n -F RUN_LAYOUT -- packages apps scripts` lists every `RUN_LAYOUT` use; none outside
      `launched.ts` names `launched`. `polaris.ts` writes the marker at line 303 and never reads it.
    - **No reader bypasses `launchedMarkerState`.**

## 4. Round-1 dispositions, tested against the current bytes

- **F1 (the arm-off brief and the inventory brief block or abort on a FIFO or a device link): answered.**
  - [Observed] `launched.ts:46` opens with `O_RDONLY | O_NOFOLLOW | O_NONBLOCK`. `launched.ts:48` maps ENOENT to `absent` and any
    other open error to `unreadable`. `launched.ts:51-52` rejects a non-file or a size above `MARKER_BYTES_MAX` (4096) on the open
    descriptor.
  - [Observed] `execution-rule.ts:101` calls the `launched` thunk only after the role check (`:95`), the arm check (`:96`) and the
    port check (`:98`).
  - [Observed] The traces in §3 item 10 show that neither the arm-off brief nor the inventory brief opens the marker. A FIFO, a
    device link, a socket and a FIFO with a writer all read `unreadable` without blocking.
  - The residual in R2-N1 (a file that grows after `fstat`) is not F1's scenario, which was a static FIFO or device.
- **F2 (changed outcomes at gates the owner's row did not list): answered by the owner, and tested.**
  - [Observed] The bead comment quoted in §2 exists. [Unknown] whether the selection was made as described: the session is not in
    this repository, the same provenance as the decision record's own answers.
  - [Observed] Under that answer, every changed outcome is at a reader of the marker or at a gate that consumes a counter's result,
    and none permits more (§6). Where the answer is recorded is R2-N3.
- **N1 (the library `allowExecution` takes a choice in a launched run): filed, out of scope.** [Observed] Bead `syzygy-bpyt.8.11` is
  open, depends on this bead and carries an owner gate before merge. This diff does not change `execution-choice.ts`.
- **N2 (check-then-act at `allow-execution`): still open, as a note.**
  - [Observed] `cli.ts:365` still reads the marker before `allowExecution` awaits its checks and writes the choice.
  - The arm-on brief check stays load-bearing. In the recorded differential, every non-absent marker state moves `briefArmOn` from
    `permitting` to `sec-3`.
  - [Inferred] The execution rule has the same shape: it reads the marker (`execution-rule.ts:101`) before awaiting D9, the choice
    source and the probe (`:104`, `:108`, `:125`), and the brief is written later (`brief.ts:248-250`). The only writer of the marker,
    `polaris.ts:303`, runs before the supervisor issues the brief (`:306`), so the window needs an operator to run `brief` by hand
    during a `syzygy polaris` start. No fix is needed here.
- **N3 (trust on absence): still open, by design.** [Observed] Deleting the marker still makes every reader report `absent`; the bead
  fixes that meaning.
- **N4 (the inventory-brief read was dead input): answered.** [Observed] The inventory brief no longer opens the marker (§3 item 10).
  The thunk at `inventory.ts:235` is never called, because the role check at `execution-rule.ts:95` returns first. The recorded
  survivor `inventory-brief-marker-not-read` is truly equivalent.
- **N5 (`review.ts:664` wording untested): still open, as a note.** [Observed] My X1 survived. The wording now comes from the shared
  `expectedLaunch`, whose three outputs `launched.test.ts:82-84` asserts as literals, so the remaining risk is the call site alone.
- **N6 (fixture independence): answered.**
  - [Observed] `launched.test.ts:52-56` asserts `launched` for hand-typed marker bytes.
  - [Observed] The byte-order-mark fixture (`launched.test.ts:29`) is the `﻿` escape. A byte count over the seven touched test
    files finds 0 raw `EF BB BF` sequences.
- **N7 (removing the `isLaunchedRun` export): unchanged, still a note.** [Observed] `index.ts:104` adds `expectedLaunch`,
  `launchedMarkerState` and `LaunchedMarkerState`, and drops `isLaunchedRun`. No code reference to it remains. [Inferred] Not a class-6
  endpoint removal; the package is private.
- **N8 (process items outside the frozen subject): still [Unknown].** The pull request, its class statement, its list of changed
  refusals and the cycle-report owner notice are not in the subject. §6 gives the list of changed refusals the pull request needs.
- **N9 (the altered-prose corpus): unchanged, still a note.** [Observed] The round-2 corpus still has one altered-prose variant
  ("launched format, another runId"). [Inferred] It is not material: the reader compares only `format`, so any other altered prose with
  the right format reads `launched`, the strict side.

## 5. New findings

No finding is blocking. Each of the following is a note.

### R2-N1 — note. The 4096-byte bound is checked at `fstat` but not enforced on the read

- **Evidence.**
  - `launched.ts:51-53` checks `stat.size > MARKER_BYTES_MAX` on the descriptor, then calls `fs.readFileSync(fd, 'utf8')`.
    [Observed] On Node v24.6.0 that call returns everything up to end-of-file, however far the file has grown since the `fstat` (§3
    item 9):
    - a 231-byte file grown to 64 MiB after `fstat` returned 67,108,864 characters;
    - grown to 4 GiB under a 3 GB address-space limit, the process aborted with `std::bad_alloc`;
    - an unprivileged toggler won the race on 386,653 of the 588,531 reads in 15 s, with reads up to 2,105,344 bytes;
    - a 49-byte prefix completed after `fstat` into a 5051-byte valid marker read `launched`.
  - That contradicts the type's documentation at `launched.ts:30-32`, which says a "file larger than any marker" is `unreadable`.
  - The comment at `launched.ts:42-43` is accurate as written: a FIFO or a device cannot hang or exhaust the reader, and the open
    descriptor stops a swap. It does not cover growth of the same inode.
- **Failure scenario.**
  - A process with write access to the run directory keeps extending `launched.json` while an operator runs `allow-execution`,
    `launch-form`, an inventory or review check, or render. [Observed] In an operator-started run, the authoring session writes into
    that directory: the brief tells it to write `drafts/next.json` in the run directory (`brief.ts:83`).
  - The reader then reads far past the bound and aborts or exhausts memory. With the arm switched on, brief issuance reads the
    marker too and is exposed the same way.
  - Nothing is permitted. Each outcome is `unreadable`, `launched` or a crash that records nothing.
- **Why a note, not blocking.**
  - [Observed] No reader is worse than at base. The base reader at `allow-execution`, `launch-form` and both counters read the whole
    file through a followed link with no race needed (round 1 observed it abort on `/dev/zero`). The shipped arm-off brief and the
    inventory brief never open the marker (§3 item 10).
  - [Observed] Anyone with that write access can already hang every dossier command with a FIFO at `run.json` (§3 item 11).
  - [Inferred] The new exposure is at arm-on brief issuance only, which is not shipped and needs its own CC-REV-1 class-4 review
    before the flag flips (the GP-Q7 answer, item 1).
- **Proposed fix** (verified on the built file in the scratch clone, §3 item 12). Read through the descriptor into a fixed buffer one
  byte past the bound, and keep the `fstat` check:
  ```ts
  const buffer = Buffer.alloc(MARKER_BYTES_MAX + 1);
  let length = 0;
  while (length < buffer.length) {
    const n = fs.readSync(fd, buffer, length, buffer.length - length, null);
    if (n === 0) break;
    length += n;
  }
  if (length > MARKER_BYTES_MAX) return 'unreadable';
  const marker = JSON.parse(buffer.toString('utf8', 0, length)) as unknown;
  ```
  - Add the growth test, the second test in `zz-r2-proposed-tests.test.ts` under `lead/b88/reviewer2/`. It fails at HEAD and passes
    with the fix.
  - With the bounded read, the `fstat` size check and the read bound back each other up. Re-derive which fixture kills each
    size-bound mutant (a valid marker of exactly 4097 bytes, grown after `fstat`, is the case the read bound alone decides) rather
    than reusing this round's record.
  - If this does not land with this bead, name it as a precondition in `syzygy-bpyt.1.6`, the flag-flip packet.

### R2-N2 — note. The `any-file-type` survivor is not equivalent; one fixture kills it, and the two records disagree

- **Evidence.**
  - The mutants record (`docs/evidence/launched-marker-fail-closed-mutants-2026-10-21-r2.json:350`) calls `any-file-type` "Equivalent
    at every fixture an unprivileged test can build", because "with O_NONBLOCK a FIFO opens and reads end-of-file". That holds only
    for an empty FIFO.
  - [Observed] With the mutant applied (on the built file, and separately on the source with the record's exact `old`/`new`), a FIFO
    holding the marker's bytes reads `launched`, and a `syzygy-launched` form counts (`launchFormRefusal` returns `null`). At HEAD the
    same fixture reads `unreadable`, and the form is refused.
  - [Observed] In the suite, this fixture kills the mutant: `Tests  1 failed | 230 passed (231)`.
  - The differential record (`…-differential-2026-10-21-r2.json:2147`) lists "A FIFO with a writer attached" as `notCovered`. That
    contradicts the equivalence claim.
  - So the `!stat.isFile()` predicate at `launched.ts:52` is load-bearing and has no killing test. By rule 6 it is not yet trusted, and
    GP-Q0 asks for "a rule-6 mutant for each predicate".
- **Failure scenario.** A later edit drops `isFile()`, for instance to "simplify" after the size check. A FIFO that holds a valid
  marker then reads `launched` [Observed under the mutant], and no test fails. [Inferred] A FIFO fed by a writer would also be read
  past the size bound for as long as data keeps arriving, because a FIFO's `st_size` is 0. My streaming-writer probe under the mutant
  still read `unreadable` in 312 ms, most likely on an `EAGAIN` between writes.
- **Proposed fix.**
  - Add this fixture to `launched.test.ts`. It is the first test in the scratch file `zz-r2-proposed-tests.test.ts` under
    `lead/b88/reviewer2/`.
    ```ts
    const marker = path.join(dir, 'launched.json');
    execFileSync('mkfifo', [marker]);
    const keep = fs.openSync(marker, fs.constants.O_RDONLY | fs.constants.O_NONBLOCK); // keeps the pipe alive
    const fill = () => { const w = fs.openSync(marker, fs.constants.O_WRONLY | fs.constants.O_NONBLOCK); fs.writeSync(w, TYPED); fs.closeSync(w); };
    fill(); expect(launchedMarkerState(dir)).toBe('unreadable');
    fill(); expect(launchFormRefusal(dir, { value: 'syzygy-launched', declaredBy: 'syzygy', label: 'Observed' })).toBe('the run\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched');
    ```
  - Record the corrected survivor status in a successor mutants record. Do not edit the round-2 record, which this review read
    (rule 10).

### R2-N3 — note. The owner's widening of the Part 3 row is recorded only in a bead comment and a docs index row

- **Evidence.**
  - [Observed] The decision record still reads, at line 93, "at both `allow-execution` and brief issuance", followed at lines 95-96 by
    "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
  - [Observed] The owner's answer that widens the row to every reader exists only in two places: the bead comment, and the
    `docs/README.md:155` campaign row (an index, never authority). A sweep of `.syzygy/`, `docs/` and `PROJECT-STATUS.md` for
    "Cover every reader", `bpyt.8.8` and `bpyt.8.11` finds no record under `decisions/`.
  - AGENTS.md says "Each authorization is a dated owner act or direction under `.syzygy/governance/decisions/`". The GP-Q0 answers
    themselves, given the same way in session, were written into a decision record.
- **Failure scenario.** A later audit compares the merged code with the decision record. It finds changed refusals at `launch-form`
  and both counters that the row does not list, and the bead tracker is not where that audit looks. This is round 1's F2 again, one
  step later.
- **Proposed fix.** Record the 2026-10-21 answer as a dated plain owner direction or addendum under `decisions/`. It binds no digest
  and edits no signed byte. Quote it in the pull request text with the comment's timestamp. Neither step edits the existing decision
  record.

### R2-N4 — note. Nothing at the `brief.ts` and `inventory.ts` call sites holds "never opens the marker"

- **Evidence.**
  - [Observed] X2 and X3 survived. A brief that reads the marker eagerly passes every test.
  - The arm-off FIFO and `/dev/zero` cases (`brief.test.ts:227-229`) say "the arm-off brief never opens the marker". With a
    non-blocking, no-follow reader, those fixtures cannot tell "never opens" from "opens safely".
  - Only the execution-rule thunk count (`execution-rule.test.ts:66-74`) holds the property, and only at the rule.
  - [Observed] The property holds at HEAD (§3 item 10).
- **Failure scenario.** A refactor passes `launchedMarkerState(run)` by value again, and the arm-off brief goes back to opening the
  marker on every issue. No test notices. This is harmless while the reader stays safe, but it is the property criterion 4 states.
- **Proposed fix.** Either correct the comment at `brief.test.ts:227` to say what the cases prove (no hang and the same bytes), or add a
  case that counts opens of `launched.json` during an arm-off `issueBrief`. A `createRequire('node:fs')` hook with
  `syncBuiltinESMExports()` works under this vitest setup; the growth probe in §3 used it.

## 6. Changed outcomes (criterion 6), every one refusing more

[Observed: the recorded differential re-run (§3 item 8), the extra probes, and the code at HEAD.] Over 19 variants × 5 probes, the 95
comparisons are:
- 29 unchanged;
- 56 stricter (a recorded choice, record or counted form at base becomes a refusal, or a permitting brief becomes SEC-3's rule);
- 4 refused at both commits with a new reason;
- 6 not comparable, because the base blocked on the FIFO or was not run on the link to `/dev/zero`, while HEAD refuses;
- **0 more lenient.**

By reader:

1. **`allow-execution` (CLI, `cli.ts:365-371`).**
   - The 12 present-but-not-the-marker states the base read as "not launched" go from a recorded choice (exit 0, choice written) to a
     refusal at stage `launched` (exit 1, nothing written), with the reason "this run's launched marker is present but cannot be read
     as the one `syzygy polaris` writes…". The 12 are: empty file, invalid JSON, `null`, an array, a string, another format, no format,
     a non-string format, a byte-order mark, a directory, a dangling link and a mode-000 marker.
   - A link to a valid marker, and a valid marker padded past 4096 bytes, were refused at both commits; the reason changes from "this
     run was launched…" to the unreadable reason.
   - A FIFO blocked at base and is refused at HEAD. A link to `/dev/zero` read without bound at base and is refused at HEAD.
   - A run path under a file (ENOTDIR), a mode-000 run directory (EACCES) or an over-long name (ENAMETOOLONG) moves from a later
     refusal to stage `launched`. Round 1 observed ENOTDIR and EACCES at the CLI; I observed ENAMETOOLONG at the reader only.
2. **`launchFormRefusal` (`launched.ts:118-127`).**
   - For the 12 states, a declared `terminal` or `bang` form that counted is refused with "the run's launched marker is present but
     cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched".
   - For a link to a valid marker and a padded marker, a `syzygy-launched` form that counted is refused.
   - Through `launchFormRefusal`, the inventory of record (`inventory.ts:434-436`) and the review of record (`review.ts:662-664`) go
     from counting to not counting. Their sentence changes from "is not a terminal or bang launch" to "is not a countable launch (the
     run's launched marker is present but unreadable, so none counts)".
   - Three gates consume those counters and inherit the refusals: the fidelity packet build (`review.ts:152`), render
     (`render.ts:173`) and the supervisor's poll (`polaris.ts:484`), which keeps polling until the run's deadline. [Inferred] These
     fall within "every reader of the launched marker, including … the inventory and review of-record counters", because they read
     the marker only through the counters.
3. **`launch-form` (`session-handover.ts:555-557`).** For the 12 states, a written `terminal` record becomes a refusal at stage
   `form`, with the reason "this run's launched marker is present but cannot be read as the one `syzygy polaris` writes, so whether
   Syzygy started its sessions cannot be told, and no launch form is declared for it". A link to a valid marker and a padded marker
   were refused at both commits and get the new reason.
4. **Brief issuance, arm off (the shipped build).** No change: the bytes are identical for all 19 variants, and the marker is never
   opened.
5. **Brief issuance, arm on (not shipped).** All 18 non-absent states, the two launched ones included, go from `permitting` to `sec-3`,
   with one new `notPermittedBecause` reason.
6. **No gate that never reads the marker changes.** [Observed] The diff changes only the readers above, the execution rule's arm-on
   path and the package index.

## 7. Verdict per acceptance criterion

1. **An absent marker is unchanged from the base. Pass.** [Observed] The `absent` row is identical at all five probes in the recorded
   differential and in my re-run. A missing run directory reads `absent` (`launched.test.ts:40-44`), and `launch-form` outside a run
   still takes the `absent` branch (`session-handover.ts:555`).
2. **A present marker that is not Syzygy's is never more lenient than a launched run. Pass.**
   - [Observed] Every state the brief names, and every probe in §3 item 9, reads `unreadable` or `launched`, never `absent`.
   - `unreadable` refuses at `allow-execution` with no record, gives SEC-3's rule at arm-on issuance, records no declared form at
     `launch-form`, and counts no form at either counter.
   - The states that read `launched` (a hard link, duplicate keys with the valid one last, non-UTF-8 inside a string value, a valid
     marker grown past 4096 bytes after `fstat`) are treated exactly as a launched run.
3. **No reader blocks, aborts or reads without bound. Not met in full: R2-N1.**
   - [Observed] A FIFO, a FIFO with a writer, a device link, a socket, a directory, a link loop and a static oversized file neither
     block nor overread at any reader.
   - A regular file that grows after `fstat` is read without bound and can abort the process. That residual reaches
     `allow-execution`, `launch-form`, both counters and arm-on brief issuance. It does not reach the arm-off brief or the inventory
     brief, which never open the marker.
   - I grade it a note for the reasons in R2-N1: no reader is worse than base, a simpler block already exists for the same actor, and
     the only new exposure is behind the unshipped arm.
4. **With the arm off, brief bytes are unchanged and neither brief opens the marker. Pass.** [Observed] All 38 arm-off briefs in my
   re-run of the differential (19 variants × 2 sides) share one byte pair, as recorded. The traces in §3 item 10 show no read-side open in the arm-off
   brief or the inventory brief, against a positive control. R2-N4 notes that no test holds the call-site half of this.
5. **The round-2 records are re-runnable and reproduce at `cc0aba21`.**
   - Mutants: **Pass.** [Observed] 18 of 18 reproduce exactly.
   - Differential: **Pass.** [Observed] 190 side comparisons, 0 mismatches, run at HEAD, whose `polaris-dossier` bytes equal
     `cc0aba21`'s.
   - Survivors: `inventory-brief-marker-not-read` is truly equivalent. **`any-file-type` is not equivalent:** the killing fixture is
     a FIFO that holds the marker's bytes (R2-N2).
6. **Every changed outcome is within the owner's 2026-10-21 answer and refuses more. Pass.** [Observed] 0 of 95 comparisons is more
   lenient, and every changed outcome is enumerated in §6. Where the answer is recorded is R2-N3.
7. **Partition and README quotes. Pass.**
   - [Observed] The partition check passes (§3 item 4).
   - The row for `syzygy-bpyt.6.2` quotes `CONFIRM WITH EXCEPTIONS` at `R-GP-IMPL-OWNER-ACT-FIELDS-1-RAW.md:2`, which reads
     "Verdict: CONFIRM WITH EXCEPTIONS".
   - The row for this bead quotes `REVISE` at `R-GP-IMPL-LAUNCHED-MARKER-1-RAW.md:2`, which reads "Verdict: REVISE". Its "over
     `1e153a0d`" matches line 3, and "two blocking findings and nine notes" matches F1-F2 and N1-N9.
   - The row's file count, 2, matches the two `R-GP-IMPL-*` raws.
   - Retaining this raw adds a file to `docs/reviews/`. The row's count, the row's text and the "488 files" sentence must move in the
     same commit, re-derived after any rebase.

## 8. Test quality

- [Observed] Every new expected value is a literal: the `toBe`/`toEqual` refusal strings and states in `launched.test.ts`,
  `brief.test.ts`, `execution-choice.test.ts`, `inventory.test.ts`, `review.test.ts` and `execution-rule.test.ts`. None is imported
  from the module under test. `writeLaunchedMarker` is used only to plant fixtures, and one valid-marker fixture is now typed by hand.
- [Observed] The refusal tests assert exact objects with `toEqual`, assert that no record is written, and assert exact
  `notPermittedBecause` arrays.
- [Observed] `launched.test.ts:20-37` covers 16 present-but-not-the-marker states, at both `launchedMarkerState` and
  `launchFormRefusal`.
- Gaps:
  - the `isFile()` predicate has no killing test (R2-N2);
  - the read bound is untested under growth (R2-N1);
  - nothing holds "never opens" at the call sites (R2-N4);
  - the `review.ts:664` wording is untested (N5).
- [Inferred] The mode-000 fixture assumes a non-root runner, as round 1 noted. It held here (uid 1000).

## 9. Cleanup

- [Observed] The scratch clone's tracked tree was clean after every mutant, after the differential (the driver's own
  `trackedTreeClean: true`) and after the proposed fix was reverted, with HEAD still `cf3ba3fe`. Both patches I made to
  `dist/launched.js` were restored to its digest.
- [Observed] The scratch clone and every probe run directory are deleted. So is one leftover `/tmp/polaris-marker-*` directory
  holding a FIFO, left by the killed `open-blocks` mutant run. Two older `/tmp/polaris-marker-*` directories, dated before my clone
  existed, are not mine and were left in place.
- [Observed] The worktree is unchanged: `git status --short` is empty, and HEAD is `cf3ba3fefb3969e2293afb0038685b4cd41e6788`.
- Retained under `lead/b88/reviewer2/`:
  - harnesses: `sweep_readers.py`, `check_subject_digests.py`, `run_mutants.py`, `extra-mutants.json`, `mutate_dist.py`,
    `run_probes.py`, `probe-reader.mjs`, `probe-config-fifo.mjs`, `classify_changes.py`, `compare_differential.py`,
    `apply_proposed_fix.py`, `zz-r2-reviewer-fixtures.test.ts` and `zz-r2-proposed-tests.test.ts`;
  - the extracted differential driver and harness under `extracted/`;
  - outputs: `regen.diff`, `full-run-1.log`, `typecheck.log`, `governance.log`, `authority-sweep.log`, `sweep.out`,
    `mutants-rerun.json`, `mutants-rerun.log`, `mutants-with-fixture.json`, `extra-mutants-rerun.json`, `probes-*.jsonl`,
    `strace-*.txt`, `strace-*.log`, `fixtures-head.log`, `proposed-tests-head.log`, `proposed-fix-suite.log`, `diff-rerun.json`,
    `diff-rerun.log` and `diff-scratch/`.
