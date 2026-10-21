# R-GP-IMPL-LAUNCHED-MARKER-3 — CC-REV-1 implementation review of syzygy-bpyt.8.12, round 3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: c76050f9
Subject: r3-review.diff sha256 3fc4a0b78057e578ca73a7375e3b5facad258dd1aff043d266bd291e43331f0a

Reviewer: a fresh-context CC-REV-1 reviewer (classes 4 and 1), round 3. I did not write this change or either earlier round. I fetched
no target-repository content and read no observed repository body. The only network fetch was the Syzygy branch itself from
`https://github.com/Tzeusy/syzygy.git`, plus two read-only `gh pr view 497` calls. I edited no coordinator or lane worktree. I made no
`bd` mutation, no commit, no push and no PR comment. Every run below was in my own scratch clones of the reviewed commit, each with its
own `npm ci`, on Node v24.6.0, as uid 1000 (not root).

## 1. Subject identity checks

- [Observed] `sha256sum lead/b812/r3-review.diff` gives `3fc4a0b78057e578ca73a7375e3b5facad258dd1aff043d266bd291e43331f0a`, the digest
  in the brief.
- [Observed] In my clone, `git fetch https://github.com/Tzeusy/syzygy.git agent/syzygy-bpyt.8.12` gives FETCH_HEAD
  `c76050f9ed21c2e5a7dbfb4b78d6042b5562109e`. `gh pr view 497` reports the same head. I wrote
  `git diff 32c16625e3a14e6db995adff81379cf32baf49c3 c76050f9ed21c2e5a7dbfb4b78d6042b5562109e` to a file, and it hashes to the same
  digest. **The digest matches.**
- [Observed] `git merge-base 32c16625 c76050f9` is `32c16625e3a14e6db995adff81379cf32baf49c3`. The branch adds four commits:
  - `24fcf9c4`, the fix;
  - `76471746`, the testkit added to the no-egress population;
  - `8b6fdba0`, the evidence;
  - `c76050f9`, a merge of `origin/main`.
- [Observed] The diff touches 9 files, with 3444 insertions and 12 deletions:
  - one source file, `packages/polaris-dossier/src/launched.ts` (13 lines added, 3 removed: the bounded read and two comments);
  - five test files: `brief.test.ts`, `cli.test.ts`, `inventory.test.ts`, `launched.test.ts`, `render.test.ts`;
  - one new test-support module, `fs-patch.testkit.ts`;
  - two evidence records: `docs/evidence/launched-marker-fail-closed-differential-2026-10-21-r3.json` and `…-mutants-2026-10-21-r3.json`.
  Nothing under `.syzygy/**` or `openspec/**` changes, and `docs/README.md` does not change.
- [Observed] `git diff c571fb9f e26a615d -- packages/` is empty. `e26a615d` is the parent of the fix commit, so the PR's statement
  "`packages/` is identical between c571fb9f and the branch base" holds for that base. Between `c571fb9f` and `32c16625`, only
  `packages/three-surface-poc-core/` differs (5 files, from main). `packages/polaris-dossier` is identical.
- [Observed] `git diff --stat 24fcf9c4 c76050f9 -- packages/` lists `polaris-dossier/src/cli.test.ts`, the testkit population row,
  and the five `three-surface-poc-core` files from main. So both records, made at `24fcf9c4`, describe the reviewed `launched.ts` and
  every subject and test file in their commands.
- [Observed] A script made 48 checks with 0 mismatches:
  - the mutants record's 7 subject digests at `24fcf9c4` and again at `c76050f9` (14 checks);
  - the differential record's subject digest at its base `c571fb9f`, at its fix `24fcf9c4`, and its fix digest at `c76050f9` (3);
  - each of the 31 mutants' `old` fragment, which occurs exactly once in its file at `c76050f9` (31).
- [Observed] The differential record's stored `harness.text` and `driver.text` hash to their declared sha256 values
  (`a2c31f87…` and `0f3971fe…`). They are byte-equal to the lane's `harness.test.ts` and `drive.py`. The mutants record's
  `harnessText` hashes to `bb5a6d84…`, byte-equal to the lane's `mutants.py`. I ran the copies extracted from the records, not the
  lane's files.

## 2. Clauses relied on (quoted)

- **GP-Q0 Part 3** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - line 93: "| New | `isLaunchedRun` is read fail-closed, at both `allow-execution` and brief issuance |";
  - lines 95-96: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- **The review rule of the same record**, Part 1: pull requests touching class 1, 3 or 4 get "an old-versus-new differential over a
  mutated-record corpus that includes records with altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in
  the cycle report".
- **The scope direction** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-LAUNCHED-MARKER-SCOPE-2026-10-21.md`):
  - lines 56-61: "The GP-Q0 Part 3 approval of reading the launched-run marker fail-closed covers every reader of that marker:
    `allow-execution`; brief issuance; `launch-form`; the inventory and review of-record counters."
  - lines 70-73: "The question put every change as one that refuses more, so this record reads the approval as covering only such
    changes. A change at any of these gates that would permit something the base refused is not covered. Neither is a change at a gate
    that does not read the marker. Either one returns to the owner."
- **The bead's acceptance criteria** (`bd show syzygy-bpyt.8.12`, read-only): "1. New tests fail at c571fb9f (the 8.8 merge) and pass
  with the fix. 2. Rule-6 successor mutants record with old/new fragments and the commit it ran at; any-file-type and each size-bound
  mutant killed. 3. Successor differential: every outcome in docs/evidence/launched-marker-fail-closed-differential-2026-10-21-r2.json
  unchanged except a marker grown past the bound after fstat now reads unreadable (stated as a fail-closed change of an already-unsafe
  input); 0 more lenient. 4. Tests: +a ~b -c in the PR. 5. PROJECT-STATUS battery green in a clean clone at the PR head."
- **AGENTS.md at `c76050f9`:**
  - rule 6 (line 126): "Mutate the input and confirm the check fails, per predicate, before trusting it";
  - rule 10 (line 133): "Freeze the bytes a review is bound to; any later edit retires the review.";
  - rule 11 (lines 134-135): "An evidence record names its subject and the subject's digest";
  - guardrail (lines 257-258): "A mutation that throws at describe time reports zero tests and scores as survived — build fixtures in
    `beforeAll`.";
  - guardrail (lines 259-261): "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at";
  - guardrail (lines 269-270): "Conformance expected values are hard-coded literals, never imported from the module under test."
- **The previous round:** `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-2-RAW.md` §5 (R2-N1, R2-N2, R2-N4) and §4 (round-1 N5). Its
  dispositions are in `docs/evidence/launched-marker-round-2-dispositions-2026-10-21.md`.

## 3. What I ran and the results

1. **The full `@syzygy/polaris-dossier` vitest project** at `c76050f9`. [Observed] Verbatim: `Test Files  29 passed (29)` and
   `Tests  1184 passed | 1 skipped (1185)`. The skip is the no-strace placeholder; `strace` is installed here.
2. **`npm run typecheck`.** [Observed] Exit 0. The only output is npm's two header lines.
3. **`python3 scripts/check_governance.py`.** [Observed] Exit 0, verbatim: `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not
   asserted`.
4. **The PWB-REQ-014 authority sweep and the sync-child-process guard**
   (`apps/three-surface-poc/src/polaris-authority-sweep.test.ts`, `sync-child-process-guard.test.ts`). [Observed] `Test Files  2
   passed (2)`, `Tests  11 passed (11)`.
5. **The PROJECT-STATUS battery** (§"How to verify this page"), run line by line from the page's own block by `run_battery.py`, in a
   clean second clone at `c76050f9`.
   - [Observed] `commands 110 nonzero 0 flagged 0 head c76050f9ed21c2e5a7dbfb4b78d6042b5562109e clean True`.
   - Second method: there are 110 per-command logs, and `grep -l -x 'exit=0'` matches all 110.
   - A case-insensitive sweep for `traceback|FAIL|FAILED` over the 110 logs finds only selftest prose ("0 failing", "fail closed",
     "killed … (failed: R1)") and the governance line `32 OK, 21 WARN, 0 FAIL (53 checks)`. There is no traceback and no failing
     check.
   - The tree was clean afterwards.
6. **The new tests at `c571fb9f`**, with `launched.ts` checked out from `c571fb9f` over the five touched test files, then restored to
   `c7a25b8b…`.
   - [Observed] `Test Files  1 failed | 4 passed (5)`, `Tests  2 failed | 209 passed (211)`.
   - The two failures are the grow-after-fstat and the grow-between-reads cases, each `expected 'launched' to be 'unreadable'`. See
     R3-N2 for why the second fails at base.
7. **The r3 differential, re-run from the record's stored driver and harness**:
   `python3 -I extracted/drive.py <clone-b> c571fb9f… <scratch> diff-rerun.json`.
   - [Observed] `done 22 22`. Fix `c76050f9`, subject `['packages/polaris-dossier/src/launched.ts']`, `trackedTreeClean` true.
   - [Observed] `compare_differential.py` compares 22 variants × 5 probes × 2 sides: `side comparisons 220 mismatches 0` against the
     record.
   - [Observed] My own classifier, independent of `build_differential.py`, over 110 comparisons gives: 102 unchanged, 2 stricter,
     6 with the same admission and a new outcome, and **0 more lenient**. The record says 102 / 2 / 6 / 0 / 0.
   - [Observed] Every round-2 comparison is equal to the round-2 record's fix side (`cf3ba3fe`): `comparisons 95 base equal 95 fix
     equal 95`.
   - [Observed] All 44 arm-off briefs are `ok` and share one byte pair: `af525364…` / `19feb999…`.
8. **The r3 mutants, re-run from the record's stored harness** (`python3 -I extracted/mutants.py <clone> mutants-rerun.json`, all 31,
   300 s timeout). This ran concurrently with item 5.
   - [Observed] Unmutated: `Tests  279 passed (279)`, exit 0. The 7 subject digests are equal to the record's. The tracked tree was
     clean before and after, and every file was restored.
   - [Observed] `summary {'planned': 31, 'killed': 29}`. All 31 outcomes equal the record. The survivors are `inventory-brief-marker-not-read`
     and `read-loop-past-buffer`. `open-blocks` and `read-no-end-of-file-stop` blocked and were killed at 300 s, as recorded.
   - [Observed] 29 of 31 mutants match the record exactly: outcome, blocked flag, exit code, Tests line and failed-test name set (with
     durations removed). Two differ only in their failed sets (R3-N3):
     - `foreign-shape-absent` gave `17 failed`, against the recorded `15`. The two extra failures are in `review-check`.
     - `rule-unreadable-reason-off` gave `3 failed`, against the recorded `4`. The record has one more failure, in `review-check`.
   - [Observed] Re-run alone and unloaded (`rerun_one.py`, twice each at `c76050f9`):
     - `foreign-shape-absent` gives `15 failed` both times, matching the record;
     - `rule-unreadable-reason-off` gives `3 failed` both times. It gives `3 failed` again at the record's own commit `24fcf9c4`.
9. **My extra mutants** on `launched.ts` (`extra-mutants.json`, same command and timeout). [Observed]
   - E1 `length += read` → `length = read`: **killed**, `Tests  1 failed | 278 passed (279)`.
   - E2 `length > MARKER_BYTES_MAX` → `length > stat.size`: **survived**, `Tests  279 passed (279)`. This mutant only refuses more: it
     refuses any growth after fstat, even within the bound. It is never more lenient than the fix, because `stat.size` ≤ 4096 is
     already enforced on the line before. Nothing pins "a marker grown within the bound reads launched", and the documentation does not
     promise that. Not a finding (§8).
   - E3 `bytes.toString('utf8', 0, length)` → `bytes.toString('utf8')`: **killed**, `Tests  7 failed | 272 passed (279)`.
10. **Equivalence checks for the two recorded survivors.**
    - `read-loop-past-buffer` (`<` → `<=`). [Observed] On Node v24.6.0, `fs.readSync(fd, b, 4097, 0, null)` on a 4097-byte buffer
      returns `0` and does not throw. The guards differ only when `length === 4097`. At that point the extra iteration reads 0 bytes,
      breaks, and `4097 > 4096` refuses. **Equivalent.**
    - `inventory-brief-marker-not-read`. [Observed] `execution-rule.ts:95` returns SEC-3 for any role other than `authoring` before the
      `inputs.launched()` call at `:101`. `inventory.ts:233-235` passes `role: 'inventory'`. **Equivalent**, as rounds 1 and 2 found.
11. **Unforced race probes against the built `dist/launched.js` at `c76050f9`** (`probes/probe-race.mjs`). A child process rewrites
    `launched.json` in a loop for 10 s while this process calls `launchedMarkerState` as fast as it can. `fs.readSync` is wrapped to
    count the bytes each call reads. [Observed]

| Toggler | Commit | Calls | States | Calls that read > 4096 bytes | Most bytes in one call | Peak RSS |
|---|---|---|---|---|---|---|
| a valid 231-byte marker, then `truncate` to 64 MiB | fix | 181,472 | 100,035 `unreadable`, 81,437 `launched` | 4,869 | 4097 | 79 MiB |
| a 49-byte invalid prefix, then a valid 5051-byte marker | fix | 266,354 | 266,354 `unreadable`, **0 `launched`** | 16,523 | 4097 | 128 MiB |
| the same | base (`c571fb9f`'s `launched.ts`, type-stripped by Node) | 223,293 | 218,506 `unreadable`, **4,787 `launched`** | (not visible: see R3-N2) | — | 113 MiB |

In the table's first row, `launched` is the 231-byte valid marker read whole, which is the correct state for it.

12. **A FIFO holding the marker's bytes, called in the table's order** (`probes/probe-fifo-drain.mjs`). [Observed]
    - At the fix, all three calls (terminal, bang, syzygy-launched) return the unreadable refusal. They do so again after a refill.
    - Under the `any-file-type` mutant (applied to a copy of the built file):
      - `terminal` returns "a launched run counts only sessions Syzygy launched…";
      - `bang` returns the unreadable refusal;
      - `syzygy-launched` returns the unreadable refusal;
      - after a refill, `syzygy-launched` returns `null (counts)`.
    See R3-N1.
13. **Does `readFileSync(fd, 'utf8')` call `fs.readSync`?** [Observed] On Node v24.6.0, with `fs.readSync` wrapped through the CommonJS
    module and `syncBuiltinESMExports`: `utf8 via fd: readSync calls 0`, and `buffer via fd: readSync calls 1`.
14. **Testkit leak probes** (`probes/leak/`, copied into the second clone's `src/`, run with `--maxWorkers=1`, then removed). [Observed]
    - Two files each first check that a sentinel `openSync` gives `ENOENT`, then leave a throwing patch installed and never restore it.
      Both pass, so neither file saw the other's patch.
    - A third file runs an `opensOf` whose act never settles. That test times out by design (`Test timed out in 300ms`). The next test
      in the same file still sees the counting wrapper (`fs.openSync === atLoad` is false), and the wrapper forwards (a missing file
      still throws `ENOENT`).
    - `vitest.config.ts` sets no `pool` or `isolate`. Vitest 3.2.7's defaults are `pool: "forks"` and `isolate: true`
      (`node_modules/vitest/dist/chunks/defaults.*.js:79,83`).
15. **Reader sweep at `c76050f9`** (`git grep -F` over 373 tracked non-test files under `packages`, `apps` and `scripts`, for
    `launched.json`, `RUN_LAYOUT.launched` and both bracket forms). [Observed] There are three code hits:
    - `launched.ts:42` (the reader);
    - `launched.ts:84` (the writer);
    - `state-directory.ts:29` (the name).
    The diff changes no caller of `launchedMarkerState` or `launchFormRefusal`. No reader bypasses the bounded reader.
16. **Test population, by name.** `vitest list --json` at `c76050f9`, and again with `packages/polaris-dossier` at `32c16625`. [Observed]
    1184 names at head and 1175 at base, all distinct. That is 11 names added and 2 removed. The 2 removed names are the old "padded
    past 4096 bytes" rows of the two tables, which were renamed to "of 4097 bytes, one past the bound".
17. **`python3 scripts/check_docs_review_campaign_partition.py --check docs/README.md`.** [Observed]
    - At `c76050f9`: exit 1, `ERROR: stale partition summary: README=(107, 504, 504, '2026-10-21'); derived=(107, 504, 504,
      '2026-10-22')`.
    - At `32c16625`: exit 0, `partition PASS: denominator=504; assigned=504; raw=470; other=34; unmatched=0; overlaps=0;
      campaigns=107`.
    See R3-N4.

## 4. The round-2 notes, tested against these bytes

- **R2-N1 (the bound was checked at fstat but not enforced on the read): answered.**
  - [Observed] `launched.ts:55-62` reads through the same `O_RDONLY | O_NOFOLLOW | O_NONBLOCK` descriptor (`:48`) into
    `Buffer.alloc(MARKER_BYTES_MAX + 1)`, in a `readSync` loop that stops at end-of-file or a full buffer. It refuses
    `length > MARKER_BYTES_MAX`. The fstat `isFile()` and size checks stay at `:54`.
  - [Observed] Under an unforced toggler, no call read more than 4097 bytes, and peak RSS stayed at Node's baseline (§3 item 11).
  - [Observed] The round-2 case, a 49-byte prefix completed after fstat into a valid 5051-byte marker, read `launched` on 4,787 calls
    at base and on 0 calls at the fix.
  - The type documentation (`:30-35`) and the comment (`:43-45`) now say what the code does.
- **R2-N2 (`any-file-type` was called equivalent; it is not): answered, with one gap (R3-N1).**
  - [Observed] The "a FIFO holding the marker's bytes" row (`launched.test.ts:26-33`, `:50`) kills the mutant: 2 failed in the record
    and in my re-run.
  - The r3 record's `round2Correction` corrects the round-2 claim. The r2 record is unedited (it is not in the diff).
  - Gap: in the `launchFormRefusal` table the row's first call drains the pipe. The `syzygy-launched` assertion, which is R2-N2's
    scenario, therefore runs on an empty FIFO (R3-N1).
- **R2-N4 (nothing at the call sites held "never opens the marker"): answered.**
  - [Observed] `brief.test.ts:222-228` counts 0 opens for the arm-off brief and 1 for the arm-on brief, the positive control.
  - [Observed] `inventory.test.ts:544-550` counts 0 for the hand-over and for `inventory-brief`, and 1 for `launch-form`.
  - [Observed] X2 (`brief-reads-marker-eagerly`) and X3 (`inventory-brief-reads-marker-eagerly`) are killed, 1 failed each, in the
    record and in my re-run.
  - [Observed] The comment at `brief.test.ts:236-237` now says what the FIFO and `/dev/zero` cases show.
- **Round-1 N5 (the `review.ts:664` wording was untested): answered.**
  - [Observed] `render.test.ts:715-723` writes an empty marker into a counted design-review run and asks `designReviewOfRecord`
    directly. It asserts the exact literal `why`.
  - [Observed] X1 (`review-of-record-wording-reverted`) is killed, 1 failed.
  - [Observed] The test first checks `stored.sha256` against the verdict's digest, so the refusal it reaches is the launch-form line,
    not a stale packet.
- R2-N3 was the owner-direction record. It is outside this bead, and the scope direction answered it.

## 5. Findings

No finding is blocking. Each of the following is a note.

### R3-N1 — note, low. The FIFO row's `syzygy-launched` assertion runs on a drained pipe

- **Evidence.**
  - [Observed] `launched.test.ts:115-121` calls `launchFormRefusal` three times on one planted fixture: `terminal`, `bang`, then
    `syzygy-launched`.
  - For the FIFO row, the fixture (`:26-33`) writes the marker's bytes once. A reader that reads the pipe consumes them.
  - Under `any-file-type` (§3 item 12):
    - the `terminal` call reads them and returns the launched-run refusal, so the test fails;
    - the `bang` and `syzygy-launched` calls see an empty FIFO and read as unreadable, so they pass;
    - after a refill, `syzygy-launched` returns `null`, which counts.
  - The mutant is still killed, and its kill is correct. But the assertion that R2-N2 named ("a `syzygy-launched` form counts") is
    never evaluated with data in the pipe.
  - The PR says the row is asserted "at `launchFormRefusal`, where it must count no `syzygy-launched` form". That holds at the fix
    only because `isFile()` refuses before any read.
- **Failure scenario.** A later change keeps a FIFO path that only the `terminal` or `bang` branch reaches. For example, the
  `syzygy-launched` form could be checked against a second, differently guarded read. A FIFO with data would then count a
  `syzygy-launched` form, and this row would not see it. [Inferred: no such code exists today.]
- **Proposed fix.** Refill the FIFO before each of the three calls for that row, or plant a fresh FIFO per form. Round 2's proposed
  fixture called `fill()` before the `syzygy-launched` assertion. Alternatively, correct the sentence in the dispositions record. Only
  test bytes change; no outcome changes.

### R3-N2 — note, low. The grow-between-reads test fails at c571fb9f because its hook never fires there

- **Evidence.**
  - [Observed] `c571fb9f` reads with `fs.readFileSync(fd, 'utf8')`. On Node v24.6.0 that path makes 0 calls to `fs.readSync`
    (§3 item 13). So the `readSync` hook at `launched.test.ts:98` never rewrites the file.
  - The base reads the static hand-typed marker as `launched`, and the test fails at its first `expect`. It never reaches
    `expect(rewritten).toBe(true)`.
  - The failure at base is real, but it is not the race the test's name describes. Only the fstat case (`:96`) stages its race at
    base, because `fs.fstatSync` is called by name at both commits.
  - The PR's line "Two tests fail with `expected 'launched' to be 'unreadable'`" is literally true.
  - The same fact explains why the base row in §3 item 11 shows no byte counts.
- **Why it matters little.** Criterion 1 asks the tests to catch the defect being fixed. The fstat-growth case does that at base, and
  at the fix the between-reads case kills `read-once`, which nothing else kills.
- **Proposed fix.** Record this in the round-3 dispositions. Optionally, in a later test edit, assert `rewritten` before the state:
  ```ts
  const state = launchedMarkerState(dir);
  expect(rewritten).toBe(true);
  expect(state).toBe('unreadable');
  ```
  Then a run in which the race is not staged fails with the reason it has.

### R3-N3 — note, low. Two of the mutants record's failed-test sets include failures that do not reproduce

- **Evidence.**
  - [Observed] For `rule-unreadable-reason-off` the record lists `Tests  4 failed | 275 passed (279)`. One failure is `review-check >
    observes only the packet, its digest and that the verdict names it: …`.
  - That test passes in three unloaded re-runs: twice at `c76050f9` and once at the record's commit `24fcf9c4`. Each re-run gives
    `Tests  3 failed | 276 passed (279)`.
  - [Observed] My loaded re-run of `foreign-shape-absent` gave 2 extra `review-check` failures. Unloaded re-runs give the recorded 15.
  - [Observed] Unloaded, those `review-check` tests take up to 2,748 ms under the mutant.
  - [Inferred] The extras are timeouts against Vitest's default 5 s test timeout when the host is loaded.
  - Every outcome reproduces (31 of 31), so no kill rests on a transient failure. The other 29 mutants reproduce exactly.
- **Failure scenario.** A later reader re-runs the record under rule 6, sees `3 failed` where the record says `4`, and cannot tell
  drift from noise. The stored names carry durations but not failure messages, so a timeout cannot be told from an assertion failure.
- **Proposed fix.** In the dispositions record, say that the reproducible claim is each mutant's outcome, and that failed sets are as
  observed under the host's load at the time. Name `rule-unreadable-reason-off`'s fourth failure as one that does not reproduce
  unloaded. Do not edit the r3 record (rule 10). For later harnesses, store each failed test's first error line beside its name.

### R3-N4 — note, process. The docs review-campaign partition check fails at the PR head on its date alone

- **Evidence.** [Observed] At `c76050f9`, `check_docs_review_campaign_partition.py --check docs/README.md` exits 1 with `ERROR: stale
  partition summary: README=(107, 504, 504, '2026-10-21'); derived=(107, 504, 504, '2026-10-22')`. At `32c16625` it passes.
  - The PR does not touch `docs/README.md`.
  - The helper derives the date from `git show -s --format=%cs HEAD` (`scripts/check_docs_review_campaign_partition.py:483-488`). The
    merge commit `c76050f9` has a committer date of `2026-10-22T00:31:50+08:00`.
  - The check is not in the battery or the hosted workflow. AGENTS.md asks for it to be run immediately before merging.
- **Failure scenario.** The raw is retained as `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-3-RAW.md` and the row count is updated, but
  the date in the count sentence is left at `2026-10-21`. The pre-merge check then fails, or a later session "fixes" it in an
  unrelated commit.
- **Proposed fix.** Retaining this raw needs a `docs/README.md` edit anyway: the Greenfield-parity row's count goes from 6 to 7, and
  504 goes to 505. In that same commit, re-derive the count sentence, including "HEAD dated", by running the helper. Re-run it again
  on the final head after any rebase.

## 6. Every changed outcome, with the count that is more lenient

[Observed: the re-run differential (§3 item 7), the probes (§3 items 11-12) and the code at `c76050f9`.] Over 22 variants × 5 probes,
the 110 comparisons are:
- 102 unchanged;
- 8 changed, all in the two variants whose marker grows past 4096 bytes after fstat (to exactly 4097 bytes, and to 5051 bytes);
- **0 more lenient.**

The changed outcomes, by reader:

1. **`launchFormRefusal`** (`launched.ts:128-137`), 2 changes, stricter.
   - Base: `syzygyLaunched: null`, so a `syzygy-launched` form counted. `terminal` and `bang` got "a launched run counts only sessions
     Syzygy launched (syzygy-launched, Observed)".
   - Fix: all three get "the run's launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts,
     declared or syzygy-launched".
   - [Inferred, from the code] The inventory of record (`inventory.ts:434-436`) and the review of record (`review.ts:662-664`) call
     this function. So for such a marker they stop counting a `syzygy-launched` session. The fidelity packet build, render and the
     supervisor's poll inherit that through the counters.
2. **`allow-execution`** (`cli.ts:365`), 2 changes, refused at both commits with a new reason.
   - Exit 1 at stage `launched`, no choice written, at both commits.
   - The reason changes from "this run was launched by `syzygy polaris`…" to "this run's launched marker is present but cannot be read
     as the one `syzygy polaris` writes, so the run is treated as launched…".
3. **`launch-form`** (`session-handover.ts:555`), 2 changes, refused at both commits with a new reason.
   - Stage `form`, no record written, at both commits.
   - The reason changes to "…present but cannot be read as the one `syzygy polaris` writes, so whether Syzygy started its sessions
     cannot be told, and no launch form is declared for it".
4. **Arm-on brief issuance** (`execution-rule.ts:101-103`, not shipped), 2 changes, `sec-3` at both commits. `notPermittedBecause`
   changes from the launched reason to the unreadable reason.
5. **Arm-off brief issuance** (shipped): no change. All 44 briefs share one byte pair, and the brief never opens the marker
   (`brief.test.ts:222-228`).
6. **Beyond the corpus.**
   - [Observed in round 2, not re-run here] At base, a growth to 4 GiB under a 3 GB address-space limit aborted the process.
   - [Observed] Under an unforced toggler (§3 item 11), the fix never read more than 4097 bytes, never returned `launched` for a marker
     past the bound, and never returned `absent`.
   - [Inferred, from the code] The only states the fix changes are `launched` (or a crash) becoming `unreadable`, for a regular file
     that grows past 4096 bytes between fstat and the end of the read. Every other input reads the same bytes it did at base:
     - a file of 4096 bytes or fewer, static or changing within the bound, decodes the same way through
       `bytes.toString('utf8', 0, length)` as through `readFileSync(fd, 'utf8')`;
     - every error still reaches the same `catch`.

Every changed outcome is at a reader the scope direction lists, or at a gate that reads the marker only through a counter. Each one
refuses more or refuses with a new reason, inside "covering only such changes" (scope direction, lines 70-71). No gate that does not
read the marker changes. **More lenient: 0.**

## 7. Verdict per acceptance criterion

1. **New tests fail at c571fb9f and pass with the fix. Pass.**
   - [Observed] At base, `Tests  2 failed | 209 passed (211)` over the five touched files. At the fix, all pass (§3 item 1).
   - The PR is right that only 2 of the new tests can fail at base. The others pin behaviour that was already correct at
     `c571fb9f`: the fstat bound, `isFile`, never-opens, and the review wording. They are the round-2 coverage gaps, so they cannot fail
     at base by construction.
   - The criterion's purpose is that the tests catch the defect this bead fixes (R2-N1). The fstat-growth test does. For the others,
     a recorded and reproduced mutant kill is the right evidence: `any-file-type`, the eight read-bound and fstat-edge mutants, X1, X2
     and X3 (§3 item 8). That satisfies the purpose.
   - Caveat: the second failing test fails at base for an incidental reason (R3-N2).
2. **Rule-6 successor mutants record. Pass.**
   - [Observed] It stores `old`/`new`, the commit (`24fcf9c4`), the command, the timeout, the subject digests and the harness text.
   - `any-file-type` is killed.
   - Of the 11 mutants in its `sizeBound` list, 10 are killed. `read-loop-past-buffer` survives and is equivalent (§3 item 10).
   - The other survivor, `inventory-brief-marker-not-read`, is equivalent.
   - The record reproduces outcome for outcome (31/31). The failed sets have the caveat in R3-N3.
3. **Successor differential. Pass.**
   - [Observed] 95 of 95 round-2 comparisons are unchanged at both sides.
   - The only changes are the two grown-past-the-bound variants, and 0 are more lenient.
   - `changedOutcomes.text` states the change as "a fail-closed change of an input that was already unsafe at c571fb9f".
   - It reproduces 220/220 from the stored driver and harness.
4. **`Tests: +9 ~4 -0` in the PR, and correct. Pass.**
   - [Observed] The name-level population moves from 1175 to 1184: 11 names added and 2 removed. The 2 removed are renames of the two
     padded rows, whose fixture was tightened to exactly 4097 bytes.
   - Counting those renames as modifications gives +9 added and 2 modified. Add the extended render test and the population literal in
     `cli.test.ts`, and the total is ~4, with -0.
   - The extraction of the hand-typed marker into `TYPED` does not change the test. I verified the literal is byte-identical, and it is
     reasonably not counted.
5. **PROJECT-STATUS battery green in a clean clone at the PR head. Pass.** [Observed] 110 commands, 0 nonzero, checked by two methods
   (§3 item 5).

Brief questions:
- **Is every changed outcome a refuse-more change at a marker reader (inside ref 3)?** Yes (§6).
- **Does any reader now block, abort or read without bound?** No.
  - [Observed] The read is capped at 4097 bytes.
  - The descriptor is non-blocking, no-follow and `isFile()`-checked, so the loop ends at end-of-file or a full buffer.
  - The arm-off brief and the inventory brief do not open the marker.
- **Is the evidence re-runnable from what the records store?** Yes (§3 items 7-8). The R3-N3 caveat applies to failed sets.

## 8. Test quality

- **Literal expectations.** [Observed] Every new expectation is a literal: `'launched'`, `'unreadable'`, `0`, `1`, `4096`, and the
  full refusal and `why` strings. None is imported from `launched.ts`.
  - The race cases also check `Buffer.byteLength(after)` against the file. That is a fixture check, not module output.
  - The 4096-byte test checks that `padded()` is exact (`statSync(...).size === 4096`), which also fixes the 4097 rows.
- **Fixtures at describe time.** The `it.each` tables compute strings at describe time (`padded(4097)`, `TYPED`). These are pure string
  operations on test constants and cannot throw under any mutant of the module. All filesystem fixtures are built inside the tests,
  through `runDir()` and the plant functions. The `beforeAll` guardrail's concern, a fixture that throws under mutation, does not
  arise.
- **Tests that could pass for the wrong reason.**
  - The race cases assert `rewritten` and the rewritten size, so at the fix a case that did not stage its race fails. R3-N2 covers
    base.
  - The open-count tests do not assert that the arm-off brief and `inventory-brief` were issued (`ok`). A future early refusal could
    make `0` trivially true. But X2 and X3 are killed by these tests, so today they reach the call sites. A one-line
    `toMatchObject({ ok: true })` would make that explicit. This is not a note.
  - R3-N1 is the one assertion that is weaker than the PR says.
- **`fs-patch.testkit.ts` state.**
  - [Observed] Restores are LIFO: `launched.test.ts`'s `afterEach` reverses `cleanups`, and `opensOf` uses `finally`.
  - [Observed] No patch crosses a file boundary (§3 item 14). Vitest's defaults here are forks with isolation, and no other module in
    `polaris-dossier/src` patches a builtin or calls `syncBuiltinESMExports`, so the global re-sync propagates nothing else.
  - [Observed] An `opensOf` whose act never settles leaves its counting wrapper installed for the rest of that file. This only happens
    after a test has already failed by timeout, and the wrapper forwards every call, so what leaks is a counter, not a behaviour.
  - [Inferred] The testkit compiles into `dist/` like the two existing `*.testkit.ts`. `index.ts` does not import it, and the package
    is private.
- **Coverage left open.**
  - E2 survives, as described in §3 item 9. The read bound's value is pinned from the lenient side only (check-off, inclusive, one-past,
    buffer-at-bound). That is the side that matters for fail-closed.
  - `read-no-end-of-file-stop` is caught only by the suite timeout, because a synchronous infinite loop cannot be interrupted by
    Vitest's per-test timeout. That matches round 2's `open-blocks` and is recorded as `blocked`.
- **Mode-000 fixture.** It still assumes a non-root runner. That held here (uid 1000).

## 9. Cleanup

- [Observed] Both scratch clones ended at `c76050f9ed21c2e5a7dbfb4b78d6042b5562109e` with `git status --porcelain` empty:
  - after the mutants and extra mutants (every file restored to its digest);
  - after the differential (the driver's own `trackedTreeClean: true`);
  - after the base checkouts for §3 items 6 and 16 and the partition check at `32c16625`;
  - after the leak probe files were removed.
- [Observed] I removed two `/tmp/polaris-marker-*` directories that my killed `open-blocks` and `read-no-end-of-file-stop` runs left:
  one holding a FIFO (00:58) and one holding a 231-byte file (01:06). Four older ones, dated before my clone existed (18:01, 19:58,
  00:06, 00:15), are not mine and were left in place. The race and FIFO probes removed their own directories (0 left).
- Both scratch clones are deleted after this file is written.
- Retained under `scratchpad/rev-497/`:
  - scripts: `compare_differential.py`, `compare_mutants.py`, `rerun_one.py`, `run_battery.py`, `extra-mutants.json`,
    `probes/probe-race.mjs`, `probes/probe-fifo-drain.mjs` and `probes/leak/*.test.ts`;
  - extracted record harnesses: `extracted/drive.py`, `extracted/harness.test.ts` and `extracted/mutants.py`;
  - outputs: `rederived.diff`, `full-run.log`, `typecheck.log`, `governance.log`, `authority-sweep.log`, `at-base.log`,
    `diff-rerun.json`, `diff-rerun.log`, `compare-differential.out`, `mutants-rerun.json`, `mutants-rerun.log`, `compare-mutants.out`,
    `mutant-logs/`, `mutant-logs-24fcf9c4/`, `extra-mutant-logs/`, `battery/` (110 logs and `summary.json`), `battery.out`,
    `list-head.json`, `list-base.json` and `leak-probe.log`.
- The built-file copies under `probes/dist-*` are deleted with the clones. Re-running §3 items 11-12 needs a `tsc -b` of
  `packages/polaris-dossier` at `c76050f9`, and, for the base row, `git show c571fb9f:packages/polaris-dossier/src/launched.ts` beside
  the built `state-directory.js`.
