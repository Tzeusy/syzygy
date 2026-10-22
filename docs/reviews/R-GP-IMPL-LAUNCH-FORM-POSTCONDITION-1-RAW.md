# R-GP-IMPL-LAUNCH-FORM-POSTCONDITION-1 — CC-REV-1 implementation review of syzygy-bpyt.8.18, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 35094bcf
Subject: r1-review.diff sha256 32fdb9a8c05c5d3a3129f5eba3ba0f22600ef7523c685edd4d3bb6c54657545a

Reviewer: independent fresh-context reviewer (Claude Opus 5.5), 2026-10-22. I did not author the change and did not share its session.
No observed-repository content was fetched or read. No credential file was opened. No bd mutation, push, comment or merge was made.
Environment: Node v24.6.0, Vitest v3.2.7, a scratch clone of `/home/tze/GitHub/syzygy` with `npm ci`. The host was loaded by other
lanes throughout (`uptime` load average 34 to 40). In paths below, `…/` stands for
`/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/`, and `<scratch>` for its `rev-511/`.

Summary: the change does what it says, and only that. Each of the three launch-form asks in the unreadable-marker row now asserts
`expect(launchedMarkerState(dir)).toBe('unreadable')` afterwards. The recorded rule-6 run reproduces 12 of 12 entries at the reviewed
head. D1, D2, F2 and the `bang` drain mutant are each killed by `launched.test.ts` alone. No production byte changed. There are three
notes and no blocking finding:
- N1: the new comment says each ask must leave its run "as it found it". The assertion checks only that the run still reads
  `unreadable`, using the reader under test as its oracle. Three reviewer mutants that alter the run survive the file. Two stay
  `unreadable` and are not fail-open. The third (a reader that remembers its answer, plus a removal) leaves the run `absent` on disk;
  only other test files kill it.
- N2: the record shows the new assertion failing only for the first ask (`terminal`), and in 16 of the 17 rows. This review's
  per-form mutants are the evidence that each of the three post-conditions is load-bearing, which GP-Q0's "a rule-6 mutant for each
  predicate" asks for.
- N3: I confirm the class-4 ruling. GP-Q0's owner notice for #511 is not yet on `syzygy-bpyt.10`.

## 1. Subject identity checks

1. **Digest.** [Observed] `sha256sum` of the brief's `…/lead/b818/r1-review.diff` gives
   `32fdb9a8c05c5d3a3129f5eba3ba0f22600ef7523c685edd4d3bb6c54657545a`. In my clone,
   `git diff 68c553b8ca643fcec1558768b6cad4c0af911f28 35094bcf11d4eb3f7be2b7e558f88371d78174b2 | sha256sum` gives the same digest.
   **It matches.**
2. **Head.** [Observed] `git ls-remote origin` gives `35094bcf11d4eb3f7be2b7e558f88371d78174b2` for both
   `refs/heads/agent/syzygy-bpyt.8.18` and `refs/pull/511/head`, and `gh pr view 511` reports that `headRefOid`. The reviewed commit is
   the PR head.
3. **Files.** [Observed] `git diff --stat 68c553b8 35094bcf` lists 2 files, 737 insertions and 3 deletions:
   `docs/evidence/launched-marker-test-postcondition-mutants-2026-10-22.json` (+727, new) and
   `packages/polaris-dossier/src/launched.test.ts` (+10/−3). The lane's own diff before the merge, `git diff --name-status 9c3350fb
   1c85ae3a`, is the same 2 paths. `a723137d` touches only the test file, and `1c85ae3a` only adds the record.
4. **The merge brought only main's bytes.** [Observed] `35094bcf`'s parents are `1c85ae3a` (the lane) and `68c553b8` (main), and
   `git merge-base 68c553b8 35094bcf` is `68c553b8`.
   - Method 1: `git diff --name-status 1c85ae3a 35094bcf` and `git diff --name-status 9c3350fb 68c553b8`, each sorted, list the same
     31 lines (`cmp` identical).
   - Method 2: a script over `git ls-tree -r -z` of both trees compares every blob. The union is 3188 paths (3187 at `68c553b8`,
     3188 at `35094bcf`). Exactly 2 differ, the 2 files of item 3.
5. **Main has not moved.** [Observed] At the time of the check, `git ls-remote origin refs/heads/main` gave `68c553b8…`, the merge
   base. The brief's warning that PR #510 may land does not apply to the bytes reviewed here.
6. **Digests named in the record, against git blobs** (`sha256sum` over `git show <commit>:<path>`):

   | Commit | `launched.test.ts` sha256 | `launched.ts` sha256 |
   |---|---|---|
   | `5837512f` (the record's `preRefill`) | `e151d977…f0be9003` = record `testSha256.pre-refill` | `c7a25b8b…71424921` = record `readerSha256` |
   | `9c3350fb` (the record's `base`) | `3ffaed9f…adcb0ef7` = record `testSha256.base` | `c7a25b8b…71424921` |
   | `a723137d` (the record's `commit`) | `1243441d…6fe6158c1141` = record `testSha256.fix` | `c7a25b8b…71424921` |
   | `1c85ae3a` | `1243441d…6fe6158c1141` | `c7a25b8b…71424921` |
   | `68c553b8` (merge base, main) | `3ffaed9f…adcb0ef7` (same as `9c3350fb`) | `c7a25b8b…71424921` |
   | `35094bcf` (reviewed head) | `1243441d…6fe6158c1141` | `c7a25b8b…71424921` |

   [Observed] **The tested file is the same at `a723137d` and at the reviewed head**, and so is the reader. The record ran at
   `a723137d` rather than the head, which does not matter for its outcomes. It also names the subject and its digest (rule 11).
   `a723137d` is an ancestor of `35094bcf`, so it stays reachable if the PR lands by merge commit, as recent PRs have
   (`68c553b8 Merge pull request #505`).

## 2. Clauses relied on (quoted)

- AGENTS.md at `35094bcf`, verification rules:
  - Rule 6: "Mutate the input and confirm the check fails, per predicate, before trusting it (`--selftest` holds the fixtures)."
  - Rule 9: "A claim of absence needs a sweep with a denominator."
  - Rule 10: "Freeze the bytes a review is bound to; any later edit retires the review."
  - Rule 11: "An evidence record names its subject and the subject's digest; a record that names neither cannot be re-checked against
    the bytes it describes."
- AGENTS.md guardrails:
  - "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at; ids and outcomes alone are not
    re-runnable, and a rebase-merge leaves the recorded commit reachable from no ref."
  - "A mutation that throws at describe time reports zero tests and scores as survived — build fixtures in `beforeAll`."
  - "Conformance expected values are hard-coded literals, never imported from the module under test."
- CC-REV-1 (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`):
  - `:18`: "Changes touching any of seven classes require review by an independent, fresh-context reviewer, and the agent performing
    the change never finally decides which classes it touches."
  - `:37`: "4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;"
  - `:49`: "**The change record states** which classes the change touches, or "none," so a misclassification is a findable violation
    after the fact."
  - `:51`: "**A reviewer or the owner** may reclassify at any time."
- GP-Q0 (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - `:52-55`: `"Behavior-preserving" means none of the following changes:`, then three items: "a rendered byte, a wire format, a
    refusal string or an exit code;", "a signed or digest-bound artifact;" and "a consent, security or retention decision."
  - `:62`: "**Which ones:** pull requests touching class 1 (authority boundaries), class 3 (deterministic observation) or class 4
    (security), and class-6 pull requests that remove an endpoint."
  - `:64-66`: "an old-versus-new differential over a mutated-record corpus that includes records with altered prose;", "a rule-6
    mutant for each predicate;", "a non-blocking owner notice in the cycle report."
- `packages/polaris-dossier/src/launched.ts:34`: "No caller may treat `unreadable` more leniently than `launched`", and `:36`, the
  state type: `'absent' | 'launched' | 'unreadable'`.
- Test-rigor bar (`th-engineering/subskills/test-rigor/SKILL.md`):
  - `:43`, core rule: "A test is worth keeping only if some plausible bug makes it fail."
  - Bar 4 (`:67-68`): "Expected values are literals or independently derived."
  - Bar 6 (`:79-80`): "A test that fails intermittently is worse than no test".
  - Bar 7 (`:85`): "A maintainer should localize the bug from failure output alone."
  - Bar 10 (`:94-95`): "A test is worth *adding* only if it catches a plausible bug no existing test catches".
- Bead `syzygy-bpyt.8.18` (`bd show --json`, read only), acceptance criteria: "1. Each launch-form ask asserts the run still reads
  unreadable afterwards; Tests: +0 ~17 -0 (titles unchanged). 2. Recorded rule-6 run: D1, D2, F2 and the bang drain mutant each
  killed by launched.test.ts alone, with old/new fragments and commit. 3. @syzygy/polaris-dossier project green. 4. CC-REV-1 class 4
  (reviewer ruling on #506): independent review and owner notice."
- Origin, `docs/reviews/R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md`:
  - N1's proposed code (`:229-237`), whose comment reads "Each ask must leave its run as it found it, so a reader that alters an
    unreadable marker cannot pass here.", and "Do the same for `bang` and `syzygy-launched`." (`:238`).
  - N2's fix (`:267-268`): "If the row is touched again (N1), add the `bang` drain mutant to that change's rule-6 record."

## 3. What I ran and the results

All runs were in the scratch clone at `35094bcf`, each under its own private `TMPDIR` (`/tmp/r511-<n>`), with `CI=1`. The vitest
command was `npx vitest run --project @syzygy/polaris-dossier …`.

1. **The touched file.** [Observed] `… packages/polaris-dossier/src/launched.test.ts` gave `Tests  43 passed (43)`. The only entry
   left in its `TMPDIR` was `node-compile-cache`.
2. **The dossier project.**
   - [Observed] First run, loaded: `Tests  2 failed | 1193 passed | 1 skipped (1196)`. Both failures were in
     `start-gates.test.ts`, which this PR does not touch, and both were `Error: Test timed out in 5000ms.` (5949 ms and 5114 ms).
     `launched.test.ts` passed in that run: `launched.test.ts (43 tests) 669ms`.
   - [Observed] `start-gates.test.ts` in isolation gave `Tests  104 passed (104)`.
   - [Observed] A full re-run of the project, after the typecheck build, gave `Test Files  29 passed (29)` and
     `Tests  1195 passed | 1 skipped (1196)`, exit 0. `launched.test.ts (43 tests) 544ms`.
   - [Inferred] The first run's two failures were load.
3. **Typecheck.** [Observed] `npm run typecheck` (`tsc -b` over the ten projects) exited 0 and printed 0 `error TS` lines. The
   dossier project's `tsconfig.json` includes `src`, so the test file is compiled: the fresh build emitted
   `dist/launched.test.js`.
4. **Governance.** [Observed] `python3 scripts/check_governance.py` exited 0 and printed
   `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted`. In a worktree at base `68c553b8` it printed the same
   summary, and the 53 `OK`/`WARN`/`FAIL` status lines are identical between the two (`diff` empty). The only differences in the logs
   are the repo root and the scope line: 3187 tracked files at base, and at head 3188 tracked plus 1 untracked-not-ignored, the
   `.beads.gate.lock` that my own read-only `bd show` attempt left in the clone. I did not run the full PROJECT-STATUS battery; the
   lane's `commands=110 nonzero=0` stays lane-reported.
5. **Name sets** (`vitest list --json` over `launched.test.ts`, with the base `9c3350fb` bytes and then the head bytes in place).
   [Observed] Base 43 names (43 distinct), head 43 (43 distinct), added `[]`, removed `[]`. The diff changes one `it.each` body, which
   expands to the 17 rows of `PRESENT_BUT_NOT_THE_MARKER`, so `Tests: +0 ~17 -0` is right.
6. **The recorded harness, re-run.** I wrote the record's `harnessSource` to `<scratch>/tools/recorded-mutants.py` byte for byte
   (8474 bytes, sha256 `0a7ea43eb46affc0ad992bb7dd1f9d3ab5334396db665fe9d5955bcbc4b140dc`) and ran it at `35094bcf` with base
   `9c3350fb` and pre-refill `5837512f`. Output: `<scratch>/recorded-rerun.json`, sha256
   `48931cd230eae399457a12bd92e8f14e0c86637faf851d851db8132201731988`. Comparison script: `<scratch>/tools/compare.py`, sha256
   `7b83e45906c5a9355a7fb0e4f5ef3e3fa900161cd5be7a14e35f247427d30737`.
   - [Observed] It printed the same summary as the record: D1 killed / survived / killed, D2 killed / killed / killed, F2 survived /
     killed / killed, M-bang survived / killed / killed (pre-refill / base / fix).
   - [Observed] Field by field, 12 of 12 mutant entries are identical on `id`, `tests`, `edits`, `exitCode`, `counts`,
     `failedTests` (each `firstErrorLine` included), `blocked`, `outcome` and `restored`. The script normalises one thing, the
     random temp directory inside `ENOENT` lines: `/tmp/la-b818/polaris-marker-` plus six random characters in the record, and
     `/tmp/r511-6/polaris-marker-` plus six in mine.
   - [Observed] Of the record's 15 top-level fields, 14 are identical. Only `commit` differs: `a723137d…` in the record and
     `35094bcf…` in the re-run, at which both files are byte-identical (§1 item 6).
   - [Observed] Every `old` fragment occurs exactly once in the bytes it targets: the harness asserts `count(old) == 1` before each
     edit, and it completed all 12.
7. **Reviewer mutants of `launched.ts`**, each run against `launched.test.ts` alone at base (`9c3350fb` bytes) and at head. Harness
   `<scratch>/tools/rev511.py`, sha256 `3d254073c9cfb1a5d2465ff6cec3e6598d72d585d840c33fe0e041bfdf3d7c86`. Results
   `<scratch>/rev511-results.json`, sha256 `3bf0d35ddf96d211ef2569dab96b37b477a5fc2779f84a990a7c749720d54fc0`. Fragments are in
   Appendix A. "Lines" are the `launched.test.ts` lines named in each failure's stack: `:124` is the post-condition inside `asked`,
   and `:128`, `:129` and `:130` are the `terminal`, `bang` and `syzygy-launched` asks.

   | Mutant | Base tests | Head tests | Head first error line, lines |
   |---|---|---|---|
   | D1-terminal-only | survived, 43/43 | **killed, 17 failed** | `expected 'absent' to be 'unreadable'`, `:124` from `:128` |
   | D1-bang-only | survived, 43/43 | **killed, 17 failed** | same, `:124` from `:129` |
   | D1-syzygy-launched-only | survived, 43/43 | **killed, 17 failed** | same, `:124` from `:130` |
   | D1-any-remover | survived, 43/43 | **killed, 17 failed** (the dangling link included) | same, `:124` from `:128` |
   | D3-repair-to-launched | survived, 43/43 | **killed, 17 failed** | `expected 'launched' to be 'unreadable'`, `:124` from `:128` |
   | D4-truncate | survived, 43/43 | **survived, 43/43** | — |
   | M-every-form-drains-then-refuses | survived, 43/43 | **survived, 43/43** | — |

   - [Observed] Unmutated: base 43/43 and head 43/43, exit 0. After each run the reader was restored with its digest checked, the
     test bytes were intact, and `git status --porcelain --untracked-files=no` was empty at the end.
   - [Observed] Each failing test in the head runs is in the `launch forms in a run whose marker is unreadable` row. No other test
     in the file failed.
8. **Two more reviewer mutants**, against the head file only. Harness `<scratch>/tools/rev511b.py`, sha256
   `a4346991ab3cb6a24f27e36f8e20c4ece72c52b4a9b259366271878a02d36cf2`. Results `<scratch>/rev511b-results.json`, sha256
   `d9ca60645a2d77b662cc69512ae0d0c0a89c274e90e5fb5c1d20c87b446e8e6e`.
   - [Observed] **D1-with-memoized-reader** (the reader remembers each run directory's first answer, and `launchFormRefusal` removes
     an unreadable marker): **survived, 43/43**.
   - [Observed] **T-ask-of-an-unplanted-run** (a test-side mutant: `asked` takes `runDir()` instead of `planted()`): killed, 17
     failed, each `expected 'absent' to be 'unreadable'` at `:124` from `:128`. So a row whose plant never took effect fails at the
     post-condition, before the refusal assert.
   - The same D1-with-memoized-reader mutant against the whole dossier project (`<scratch>/tools/rev511c.py`, sha256
     `c2c5475e082872e17a31082560d35c0d965fea68b8eff4f4bfc1e2ca54ad8695`; results `<scratch>/rev511c-results.json`, sha256
     `527698d68f9045e940e0adb41d7ae9e97723d34c7b524b4dbe35dd8b5cbb7283`). [Observed] Killed, `1191 passed`, 4 failed:
     `inventory.test.ts` ("the inventory of record stops counting a declared launch once…"), `review.test.ts` ("review-check stops
     counting a declared launch once…"), `render.test.ts` ("rendered-design review (S9b) counts a validated design verdict only once
     its launch form is recorded"), each `expected { counts: true, … } to deeply equal { counts: false, …(1) }`, and
     `session-view.test.ts` ("launch forms by kind of run a launched run counts syzygy-launched, never a declared form"),
     `expected 'absent' to be 'launched'`. [Inferred] The session-view failure is the memo's own staleness, not D1's removal.
9. **Why the record's D1 and D2 fail 16 of the 17 launch-form rows.** [Observed] A probe under Node v24.6.0 created a dangling symbolic link and
   called `fs.rmSync(link, { recursive: true, force: true })`. It threw nothing and left the link in place (`lstat` still found it).
   `fs.unlinkSync` removed it. On a link to `/dev/zero`, `rmSync` removed the link. So the record's D1 and D2 never alter the
   `a dangling symbolic link` row, and that row's post-condition is untested by them. D1-any-remover (item 7) adds an unlink
   fallback and is killed on all 17 rows, the dangling link included.
10. **Flakiness and leaks.** [Observed] I ran the head `launched.test.ts` 10 times in a row under one private, empty `TMPDIR`. All
    10 printed `Tests  43 passed (43)`, and after each run the only entry in that directory was `node-compile-cache`: no
    `polaris-marker-*` directory, FIFO or temp file. With item 1, both project runs, and the unmutated head runs in items 6 and 7,
    that is 15 head runs, all 43/43, under load.
11. **Out of scope, observed in passing.** [Observed] Each full project run left one file in its `TMPDIR`:
    `dossier-signoff-<random>-outside-RAW.md`. It is written by `waiting-sessions.test.ts:276` into `path.dirname(root)`, outside the
    temp directory that test cleans. This PR does not touch that file. A sweep of `.beads/issues.jsonl` (370 lines) finds 0 lines
    naming `outside-RAW` or `waiting-sessions.test`; [Unknown] the export may lag the tracker. The coordinator may file it; it is not
    a finding against this PR.

## 4. Findings

No finding is blocking. Each of the following is a note.

### N1 — note, low. The comment promises "as it found it"; the assertion checks only that the run still reads `unreadable`, by the reader under test

- **Evidence.**
  - [Observed] `launched.test.ts:120` says: "Each ask must leave its run as it found it, so a reader that alters an unreadable marker
    cannot pass here." `:124` asserts `expect(launchedMarkerState(dir)).toBe('unreadable')`. The comment is copied from the origin
    raw's proposal (`R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md:229`), so the overstatement started there, not with the lane.
  - [Observed] Three mutants alter the run and survive the head file, 43/43 each (§3 items 7 and 8). What each does to the run is
    [Inferred] from its code:
    - D4-truncate: `launchFormRefusal` truncates the file at the marker's name. `truncate` follows a link, so in the
      `a symbolic link to the marker Syzygy writes` row it empties the target.
    - M-every-form-drains-then-refuses: every read takes the bytes before judging the type, so each ask drains the
      `FIFO holding the marker's bytes` row's pipe. The #506 raw's byte probe observed this read shape take all 231 bytes on each
      fresh run (`R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md:178-180`).
    - D1-with-memoized-reader: the marker is removed, and the post-condition asks a reader that remembers `unreadable`.
  - D4 and M-every-form are not fail-open. With a faithful reader the post-condition passes only on `unreadable`, one of three states
    (`launched.ts:36`), and every form still refuses; the row's refusal asserts pass under both. The alterations toward `absent` or
    `launched` that I tried, D1-any-remover and D3, are killed on all 17 rows.
  - D1-with-memoized-reader **is** fail-open across processes [Inferred]: the run is `absent` on disk, so the next process to read it,
    with an empty memory, counts a declared `terminal` or `bang` form. Within the test process every ask still refuses, which is why
    the row passes. [Observed] It is killed project-wide, by the same three files the origin raw's N1 named and by
    `session-view.test.ts` (§3 item 8). [Inferred] The `session-view.test.ts` failure is the memory's own staleness, not the
    removal.
  - The post-condition asks the module under test. Its expected value is a literal (bar 4 holds), but its observation is not
    independent of the code under test.
- **Failure scenario.** [Inferred: no such code exists today] A maintainer reads `:120`, takes the row as the guarantee that a launch
  form never touches the run, and approves a reader change on that basis. Two examples: the reader "normalises" an unreadable file in
  place, or it adds a per-run cache, as a reader consulted several times per evaluation might, alongside a cleanup of unreadable
  markers. The row stays green. The cache case is the fail-open one, and it then rests, as D1 did before this PR, on readers in other
  files consulting the marker more than once.
- **Proposed fix.** Test-only; no outcome changes. Either:
  - (a) Make the comment say what is checked: "Each ask must leave its run unreadable, so a reader that removes or rewrites an
    unreadable marker into an absent or launched one cannot pass here." This is the smaller change. With a faithful reader it covers
    SEC-3's fail-closed direction; or
  - (b) Make the comment true with an oracle independent of the reader: before each ask, snapshot
    `fs.lstatSync(marker(dir), { throwIfNoEntry: false })` (`mode`, `ino`, `size`) and, where the plant is a regular file the test
    can read, its bytes through `readFileSync`. After the ask, assert the snapshot is unchanged, then keep the existing state assertion.
    Planting a FIFO cannot be byte-snapshotted without draining it, so for the FIFO rows keep the state assertion alone.
  - [Inferred: not run] (b) would also kill D1-with-memoized-reader in the reader's own file, because the snapshot does not ask the
    reader. (a) leaves that case to the other files, as today.
  - I recommend (a), unless the owner wants the reader's own file to close the cache case; then (b). Either way it is a `~17` body
    change with titles unchanged, and the change's rule-6 record would be re-run.

### N2 — note, low. The record proves the new assertion for the first ask only and in 16 of 17 rows; the per-predicate evidence is this review's

- **Evidence.**
  - [Observed] The record's D1 and D2 remove the marker on every ask. Vitest stops a test at its first failed `expect`, so each
    failure is the `terminal` ask's post-condition. The `bang` and `syzygy-launched` post-conditions (`:124` called from `:129` and
    `:130`) are never shown failing in the record.
  - [Observed] The record's D1 and D2 fail 16 rows. The 17th, `a dangling symbolic link`, is not altered at all, because
    `fs.rmSync` with `force` leaves a dangling link in place under Node v24.6.0 (§3 item 9). That row's post-condition is untested by
    the record. Neither the record nor the PR body says why the 17th row passes.
  - [Observed] This review's D1-terminal-only, D1-bang-only and D1-syzygy-launched-only each survive at base and are killed at head
    on 17 rows, each at `:124` from its own ask's line (`:128`, `:129`, `:130`). D1-any-remover is killed on all 17 rows, the
    dangling link included (§3 item 7).
  - Rule 6 asks for a failing check "per predicate", and GP-Q0 `:65` asks for "a rule-6 mutant for each predicate". The change adds
    three predicates, one per ask.
- **Failure scenario.** A later reader of the dispositions or of the bead takes the record as the per-predicate evidence. A later
  edit could then drop the `bang` or `syzygy-launched` post-condition, for example by moving it out of `asked` for one form, and no
  recorded mutant would object. The 16-of-17 count could also be read as a gap at the dangling-link row, where there is none.
- **Proposed fix.** In the dispositions record, state that GP-Q0's per-predicate check is met by:
  - the record, for the `terminal` post-condition, and for D2, F2 and M-bang;
  - this review's §3 item 7, for the `bang` and `syzygy-launched` post-conditions and for the dangling-link row.

  State also that the record's 16 of 17 is a property of the mutant's removal call, not of the test. Do not edit the record
  (rule 10). If the row is touched again (for example for N1), use an unlink fallback in D1's removal, and add the three per-form D1
  variants to that change's rule-6 record (fragments in Appendix A).

### N3 — note, process. I confirm class 4; GP-Q0's owner notice for #511 is not yet posted

- **Evidence.**
  - [Observed] The PR body states "**CC-REV-1 classes:** none in the code, because no production file changes", and that "the #506
    reviewer ruled a change to them class 4 (R1 N3)". It asks for "a class-4 review and a non-blocking GP-Q0 owner notice".
  - The changed rows are the reader's own rule-6 kill evidence for SEC-3's fail-closed launched-marker reader. This change restores a
    kill (D1) that #506 lost. Under CC-REV-1 `:51` ("A reviewer or the owner may reclassify at any time"), I rule it **class 4**,
    as the #506 reviewer did.
  - GP-Q0 `:62` applies its three checks to class 4. Here:
    1. **Differential.** It is degenerate. The full-tree blob comparison (§1 item 4) shows that no file other than the test and the
       new record differs. Every reader's output over any corpus is therefore identical by construction, and showing the code
       identical satisfies the check more strongly than any finite corpus could. The analogue that does carry information for a
       test-only change is old-test against new-test over a mutant corpus. The record provides that (pre-refill / base / fix), and
       so do §3 items 7 and 8 (base / head).
    2. **A rule-6 mutant for each predicate.** Met by the record plus this review (N2).
    3. **A non-blocking owner notice in the cycle report.** [Observed] `bd comments syzygy-bpyt.10` (478 lines, read only) carries
       an owner notice for #506 that names `syzygy-bpyt.8.18` as the follow-up. It has no notice for #511 yet. Earlier notices were
       posted after landing ("syzygy-bpyt.8.14 merged (PR #506)"), so its absence before merge is expected.
- **Failure scenario.** The cycle report omits #511, and the owner's GP-Q0 notice trail has a gap for a class-4 change.
- **Proposed fix.** At landing, the coordinator posts one notice for #511 on `syzygy-bpyt.10`. It says: test-only, class 4 by
  reviewer ruling, no production byte changed (§1 item 4), the D1 kill restored in the reader's own file, the GP-Q0 checks as above,
  and N1.

## 5. Every changed output, or the evidence that there is none

- [Observed] No production byte changed. Method 1: `git diff --name-status 68c553b8 35094bcf` lists 2 paths. Method 2: a blob
  comparison over all 3188 paths in the union of the two trees finds 2 that differ, the same 2 (§1 item 4). Of those, one is a test
  file and the other is a new JSON file under `docs/evidence/`. **Non-test files changed outside `docs/evidence/`: 0 of 3188.**
- [Observed] `launched.ts` hashes `c7a25b8b45fe12e2add7874f88d46b2bad1eef16ffa4a17e2464d5c671424921` at `5837512f`, `9c3350fb`,
  `a723137d`, `1c85ae3a`, `68c553b8` and `35094bcf`.
- [Observed] The new JSON is read by no code and cited by no tracked file at `35094bcf`. `git grep -F` over the tree finds 0 hits
  for `postcondition-mutants` and 0 for `launched-marker-test-postcondition`. [Unknown] A citation wrapped across a line break is not
  covered by that sweep. The PR body cites the record.
- [Observed] Test outputs: name sets equal (43 = 43, §3 item 5), and every test passes at head (§3 items 1, 2 and 7).
- Under GP-Q0 `:52`, nothing on its list changes: no rendered byte, wire format, refusal string or exit code; no signed or digest-bound
  artifact; no consent, security or retention decision. **More lenient: 0. Changed outcomes: 0.**

## 6. Verdict per acceptance criterion

1. **AC1 (each ask asserts unreadable afterwards; `+0 ~17 -0`, titles unchanged): Pass.**
   - [Observed] `:121-126` define `asked`, which plants a fresh run, asks, asserts `launchedMarkerState(dir)` is `'unreadable'` and
     returns the reason. `:128-130` route all three forms through it.
   - [Observed] Each of the three post-conditions is load-bearing on its own (D1 per form, §3 item 7). The name sets are equal, and
     one parametrised body over 17 rows changed.
2. **AC2 (recorded rule-6 run: D1, D2, F2 and the bang drain mutant each killed by `launched.test.ts` alone, with old/new fragments and
   commit): Pass.**
   - [Observed] At the fix side the record has D1 killed (16), D2 killed (19), F2 killed (1) and M-all-forms-drain-bang-unchecked
     killed (1). The command runs `launched.test.ts` alone. Every entry stores `old`/`new` per edit, and the record names `commit`,
     `base`, `preRefill` and the test and reader digests. My re-run reproduces 12 of 12 entries (§3 item 6).
   - **On the lane's remark about base.** The AC asks only for kills at the fix. It does not ask that the four survive at base, and
     I find no text in the bead that says they do. The bead's "base killed it with 16 failures, head passes 43/43" is about #506's base
     and head. The three-sided record is more than the AC asks: it shows D1 discriminating this change (base survived, fix killed),
     and F2 and M-bang discriminating #506's refill (pre-refill survived, base killed). The latter is what the origin raw's N2 asked
     for ("so each form has a discriminating mutant"). D2 at base is killed only by the race rows' incidental `ENOENT`, as the PR
     body says. It does not affect AC2.
   - The per-predicate gap in what the record shows is N2. The AC's list of four mutants is met.
3. **AC3 (`@syzygy/polaris-dossier` project green): Pass.** [Observed] The full re-run gave `Tests  1195 passed | 1 skipped (1196)`,
   `Test Files  29 passed (29)`. The first run's two timeouts were in `start-gates.test.ts`, which this PR does not touch, and that
   file passes 104/104 in isolation (§3 item 2). `npm run typecheck` exited 0 with the test file compiled (§3 item 3).
4. **AC4 (class 4: an independent review and an owner notice): the review part is met by this raw; the notice is pending (N3).**
   [Observed] No notice for #511 is on `syzygy-bpyt.10` yet. By the cycle's practice it is posted at landing, so this does not block.

Brief questions:
- **Does the new assertion catch the bug it is meant to catch, at the right seam?** Yes. D1 is the bug N1 of #506 named, and it is
  killed in the reader's own file again (16 rows in the record, 17 with an unlink fallback). The seam is the run directory after the
  ask: the assertion reads what the next ask would read, so it catches exactly the fail-open direction (`absent` or `launched`).
- **Could it pass for a wrong reason?**
  - A run that was never planted: no. The post-condition fails first (T-ask-of-an-unplanted-run, §3 item 8). The `is unreadable for
    %s` table at `:81-85` also checks each plant.
  - A state that reads `unreadable` for some other cause: yes, in two ways (N1). Alterations that stay within `unreadable` pass, and
    they are not fail-open. A reader whose answer does not reflect the disk also passes; with a removal that is fail-open across
    processes, and only other files catch it.
- **Is it deterministic on a loaded host?** Yes, as far as I can test: see §3 item 10. The new code adds no timing, no shared state
  and nothing at describe time. `asked` is a closure in the test body, and every `planted()` registers its cleanup through `runDir()`.

## 7. Test quality

- **Core rule.** The changed body now fails under a plausible bug it missed at base: a reader that removes or rewrites an unreadable
  marker (D1, D1 per form, D3). That is the bug SEC-3's reader exists to prevent (`launched.ts:34`).
- **Literals (bar 4).** [Observed] Every expectation in the changed body is a literal: `'unreadable'` and the refusal string. The
  observation itself goes through `launchedMarkerState`, the module under test (N1).
- **Failure output (bar 7).** [Observed] Under D1-bang-only the failure is `expected 'absent' to be 'unreadable'`, and the stack names
  `:124` and then `:129`. The message alone does not say which form left the run altered; the stack's second line does. Minor, not a
  note: ``expect(launchedMarkerState(dir), `after the ${String(form['value'])} ask`)`` would put the form in the message.
- **Determinism and isolation (bar 6).** See §6 and §3 item 10.
- **Readability.** [Observed] The new comment at `:120` is 113 columns; the helper's lines are 79 columns or fewer. The longest line in
  the file is 264, so these lines are within the file's range. The comment's wording is N1.
- **Growth (bar 10).** `+0 ~17 -0`. No test was added; the nearest existing test was strengthened, which is the right shape.

## 8. Cleanup

- All mutation runs were in the scratch clone `<scratch>/clone`. After each harness, the mutated files were digest-checked as
  restored, and `git status --porcelain --untracked-files=no` was empty. Before the clone was removed, `launched.ts` and
  `launched.test.ts` hashed `c7a25b8b…71424921` and `1243441d…6fe6158c1141`.
- No worktree under `/home/tze/GitHub/syzygy/.worktrees/` was touched. No process was killed by pattern. The harnesses kill only
  their own process groups on timeout, and none timed out.
- [Observed] The base worktree (`git worktree remove --force`), the scratch clone, the harnesses' vitest report directory
  `<scratch>/rec-scratch/` and every private `TMPDIR` (`/tmp/r511-1` to `/tmp/r511-12`) were deleted once the runs ended.
  `ls -d /tmp/r511-*` then matched 0 entries. Nothing in `/tmp` outside those directories was deleted.
- The tools and result files stay beside this raw under `…/rev-511/`, with the digests given above: `tools/` (`recorded-mutants.py`,
  `compare.py`, `rev511.py`, `rev511b.py`, `rev511c.py`), `recorded-rerun.json`, `rev511-results.json`, `rev511b-results.json`,
  `rev511c-results.json`, and the run logs.

## Appendix A — reviewer mutant fragments (`packages/polaris-dossier/src/launched.ts` unless stated)

Each `old` fragment occurs exactly once in `launched.ts` at `35094bcf` (sha256 `c7a25b8b…71424921`); the harnesses assert it. Shared
pieces:

- REFUSAL-LINE (old):
  `  if (state === 'unreadable') return 'the run\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched';`
- REFUSAL-WITH(body) (new): `  if (state === 'unreadable') { <body>` + newline +
  `    return 'the run\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched'; }`
- REMOVE-ANY: `try { fs.rmSync(path.join(runDir, RUN_LAYOUT.launched), { recursive: true, force: true }); } catch { /* reviewer mutant */ } try { fs.unlinkSync(path.join(runDir, RUN_LAYOUT.launched)); } catch { /* reviewer mutant */ }`

| Mutant | Edit |
|---|---|
| D1-terminal-only | REFUSAL-LINE → REFUSAL-WITH(`if (form['value'] === 'terminal') { REMOVE-ANY }`) |
| D1-bang-only | REFUSAL-LINE → REFUSAL-WITH(`if (form['value'] === 'bang') { REMOVE-ANY }`) |
| D1-syzygy-launched-only | REFUSAL-LINE → REFUSAL-WITH(`if (form['value'] === SYZYGY_LAUNCHED) { REMOVE-ANY }`) |
| D1-any-remover | REFUSAL-LINE → REFUSAL-WITH(`REMOVE-ANY`) |
| D3-repair-to-launched | REFUSAL-LINE → REFUSAL-WITH(`REMOVE-ANY try { writeLaunchedMarker(runDir, 'run-x', 0); } catch { /* reviewer mutant */ }`) |
| D4-truncate | REFUSAL-LINE → REFUSAL-WITH(`try { fs.truncateSync(path.join(runDir, RUN_LAYOUT.launched), 0); } catch { /* reviewer mutant */ }`) |
| M-every-form-drains-then-refuses | `    if (!stat.isFile() \|\| stat.size > MARKER_BYTES_MAX) return 'unreadable';` → `    if (stat.size > MARKER_BYTES_MAX) return 'unreadable';`, and `    if (length > MARKER_BYTES_MAX) return 'unreadable';` → `    if (length > MARKER_BYTES_MAX \|\| !stat.isFile()) return 'unreadable';` |
| D1-with-memoized-reader | REFUSAL-LINE → REFUSAL-WITH(`REMOVE-ANY`), and `export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);` → `const REMEMBERED = new Map<string, LaunchedMarkerState>();\nexport function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const hit = REMEMBERED.get(runDir); if (hit) return hit;\n  const state = launchedMarkerStateOnce(runDir); REMEMBERED.set(runDir, state); return state;\n}\n\nfunction launchedMarkerStateOnce(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);` (`\n` is a newline) |
| T-ask-of-an-unplanted-run (`launched.test.ts`) | `      const dir = planted();` → `      const dir = runDir();` |

Command per run: `npx vitest run --project @syzygy/polaris-dossier --reporter=json --outputFile=<scratch>/rec-scratch/<name>.json
packages/polaris-dossier/src/launched.test.ts` (the project-level run drops the file argument), with `CI=1` and a 300 s timeout
(1500 s for the project run). Killed means a nonzero exit with at least one failed test, or a timeout. None timed out.
