# R-GP-IMPL-LAUNCHED-TEST-REFILL-1 — CC-REV-1 implementation review of syzygy-bpyt.8.14, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 9f09e5ca
Subject: r1-review.diff sha256 200b17206ebe87b10e639bdf22d61ea04fa50dffcdfb674fffaf2964ad485cea

Reviewer: independent fresh-context reviewer (Claude Opus 5.5), 2026-10-22. I did not author the change and did not share its session.
No observed-repository content was fetched or read. No credential file was opened. No bd mutation, push, comment or merge was made.
Environment: Node v24.6.0, Vitest v3.2.7, a scratch clone of `/home/tze/GitHub/syzygy` with `npm ci` and `npm run build`. The host
was loaded by other lanes throughout. In paths below, a leading `…/` stands for
`/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/`, and `<scratch>` for its `rev-506/`.

Summary: the change does what it says. Each launch form is now asked of a run that still holds data, and each race case asserts
`rewritten` before the state. The mutants record reproduces 8 of 8 entries exactly at the reviewed head. The battery gave
`commands=110 nonzero=0` in my clone, and the dossier project is green. There are three notes and no blocking finding:
- N1: planting afresh for all 17 rows, not only the FIFO row, removes this file's only kill of a reader that alters an unreadable run.
  Three other files still kill that mutant.
- N2: the mutant that acceptance criterion 1 names (F1) does not discriminate. AC1's intent rests on F2, on this review's
  `bang` mutant and on the byte probe.
- N3: I rule the change class 4, so GP-Q0's owner notice belongs in the cycle report.

## 1. Subject identity checks

1. **Digest.** [Observed] `sha256sum` of the brief's `r1-review.diff` gives
   `200b17206ebe87b10e639bdf22d61ea04fa50dffcdfb674fffaf2964ad485cea`. I re-derived the diff with
   `git diff 1d6731bb073cb235aa47fa9043c3ce956b9b7ea6 9f09e5ca25690cca4b68fe211dcd87c0e5cd0108 --output=…/rederived.diff` in my
   clone, and `sha256sum` of that file gives the same digest. **It matches.**
2. **Head.** [Observed] `git ls-remote` gives `9f09e5ca25690cca4b68fe211dcd87c0e5cd0108 refs/heads/agent/syzygy-bpyt.8.14` and the
   same sha for `refs/pull/506/head`. `gh pr view 506` reports `headRefOid` `9f09e5ca…`. The reviewed commit is the PR head.
3. **Files.** [Observed] `git diff --stat 1d6731bb 9f09e5ca` lists 2 files, 313 insertions and 6 deletions:
   `docs/evidence/launched-marker-test-refill-mutants-2026-10-22.json` (+305) and `packages/polaris-dossier/src/launched.test.ts`
   (+8/−6). The lane's own diff before the merge, `git diff --stat b7697f6a dc231c89`, is the same 2 files with the same counts.
4. **The merge brought only main's bytes.** [Observed] `9f09e5ca`'s parents are `dc231c89` (the lane) and `1d6731bb` (main).
   - `git diff --stat dc231c89 9f09e5ca` over the 2 lane files is empty, so the merge did not change them.
   - `git diff --name-status dc231c89 9f09e5ca` and `git diff --name-status b7697f6a 1d6731bb` list the same 13 paths with the same
     statuses, all from #504: 3 `M` (`docs/README.md` and two `three-surface-poc-core` test files) and 10 `A`.
   - `git diff 1d6731bb 9f09e5ca` touches only the 2 lane files (item 3).
   - Two methods (the lane-side merge delta against main's delta, and the head-against-main diff) agree that every path other than
     the 2 lane files is main's blob at `1d6731bb`.
5. **Main has moved since.** [Observed] `origin/main` is now `3000698f`, and `git merge-base 9f09e5ca 3000698f` is `1d6731bb`.
   `git diff --name-status 1d6731bb 3000698f` lists 22 paths, and neither lane path is among them. Of those 22,
   `packages/polaris-dossier/src/gate-acts.test.ts` is in the same package but does not touch `launched.ts` or its test.
6. **Digests named in the mutants record, against git blobs** (scripted with `hashlib` over `git show <commit>:<path>`):

   | Commit | `launched.test.ts` sha256 | `launched.ts` sha256 |
   |---|---|---|
   | `b7697f6a` (the record's `base`) | `e151d977…f0be9003` = record `testSha256.base` | `c7a25b8b…71424921` = record `readerSha256` |
   | `1d6731bb` (the PR merge base) | `e151d977…f0be9003` | `c7a25b8b…71424921` |
   | `f25b335c` (the record's `commit`) | `3ffaed9f…ef7` = record `testSha256.fix` | `c7a25b8b…71424921` |
   | `dc231c89` | `3ffaed9f…ef7` | `c7a25b8b…71424921` |
   | `9f09e5ca` (reviewed head) | `3ffaed9f…ef7` | `c7a25b8b…71424921` |

   [Observed] The record's `base` (`b7697f6a`) differs from the PR's merge base (`1d6731bb`). Both files are byte-identical at the
   two commits, so the base-side mutant runs apply to either. Every `old` fragment in the record's 8 mutant entries occurs exactly
   once in the bytes it targets: 18 of 18 edit fragments, 1 occurrence each.

## 2. Clauses relied on (quoted)

- AGENTS.md (reviewed commit), verification rules:
  - Rule 6: "Mutate the input and confirm the check fails, per predicate, before trusting it (`--selftest` holds the fixtures)."
  - Rule 9: "A claim of absence needs a sweep with a denominator."
  - Rule 10: "Freeze the bytes a review is bound to; any later edit retires the review."
  - Rule 11: "An evidence record names its subject and the subject's digest; a record that names neither cannot be re-checked
    against the bytes it describes."
- AGENTS.md guardrails:
  - "A mutation that throws at describe time reports zero tests and scores as survived — build fixtures in `beforeAll`."
  - "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at; ids and outcomes alone are not
    re-runnable, and a rebase-merge leaves the recorded commit reachable from no ref."
  - "Conformance expected values are hard-coded literals, never imported from the module under test."
- CC-REV-1 (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:16-52`):
  - "Changes touching any of seven classes require review by an independent, fresh-context reviewer, and the agent performing the
    change never finally decides which classes it touches."
  - "4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;"
  - "**A reviewer or the owner** may reclassify at any time."
- GP-Q0 (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md:52-66`):
  - "'Behavior-preserving' means none of the following changes: a rendered byte, a wire format, a refusal string or an exit code; a
    signed or digest-bound artifact; a consent, security or retention decision."
  - Review rule: "pull requests touching class 1 (authority boundaries), class 3 (deterministic observation) or class 4 (security),
    and class-6 pull requests that remove an endpoint." The checks: "an old-versus-new differential over a mutated-record corpus that
    includes records with altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report."
- Test-rigor bar (`th-engineering/subskills/test-rigor/SKILL.md`):
  - Core rule: "A test is worth keeping only if some plausible bug makes it fail."
  - Bar 4: "Expected values are literals or independently derived."
  - Bar 6: "A test that fails intermittently is worse than no test".
  - Bar 7: "A maintainer should localize the bug from failure output alone."
- Bead `syzygy-bpyt.8.14`, acceptance criteria (`bd show --json`, read only):
  1. "The FIFO row evaluates each of terminal, bang and syzygy-launched with data in the pipe (shown by a recorded rule-6 mutant: an
     isFile check removed from the syzygy-launched path only is killed by this row)."
  2. "Each race case asserts rewritten before the state; with the readSync hook disabled the case fails on the rewritten expect."
  3. "Tests: ~n only (no added or removed names); @syzygy/polaris-dossier project green."
  - The bead's design: "Refill the FIFO (or plant a fresh FIFO) before each of the three launchFormRefusal calls for that row."
- Origin, `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-3-RAW.md`:
  - R3-N1 (`:215-234`), proposed fix: "Refill the FIFO before each of the three calls for that row, or plant a fresh FIFO per form."
  - R3-N2 (`:236-255`), proposed fix: "assert `rewritten` before the state".

## 3. What I ran and the results

All runs were in the scratch clone at `9f09e5ca`. The commands were `npm test --prefix <clone> -- …`, that is
`vitest run --project @syzygy/polaris-dossier …`, plus the scripts named below.

1. **The touched file.** [Observed] `vitest run --project @syzygy/polaris-dossier packages/polaris-dossier/src/launched.test.ts` gave
   `Tests  43 passed (43)`.
2. **The dossier project.**
   - [Observed] First run, loaded: `Tests  1 failed | 1191 passed | 1 skipped (1193)`. The one failure was
     `start-gates.test.ts > … refuses config naming a remote, a promisor, an include or a command the agent's git would run …`,
     `Error: Test timed out in 5000ms.`, in a file this PR does not touch.
   - [Observed] That file in isolation gave `Tests  104 passed (104)`, and the same test took `2049ms`.
   - [Observed] A full re-run of the project gave `Test Files  29 passed (29)` and `Tests  1192 passed | 1 skipped (1193)`.
   - [Inferred] The first failure was load.
3. **Typecheck.** [Observed] `npm run typecheck` (`tsc -b …` over all ten projects) printed no diagnostic, and the tool reported no
   nonzero exit.
4. **Battery.** [Observed] I extracted the `PROJECT-STATUS.md` §"How to verify this page" block at `9f09e5ca` and ran it line by line.
   Assignment lines (`CS=`, `DR=`) set the environment; comment lines were skipped.
   - The result was `commands=110 nonzero=0 head=9f09e5ca25690cca4b68fe211dcd87c0e5cd0108`. A second method, counting the result lines
     in the log, gives 110 lines, of which 110 start with exit code `0`.
   - `check_governance.py` printed `32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted`.
   - `--selftest` printed `406 fixtures, 0 failing — a check that cannot fail is not a check`.
   - Battery record: `…/rev-506/battery.json`, sha256 `164bb8aea9802e7ce4737c96175e5650b854dc03a122d63ba9c7fdd4d763f45b`.
5. **Name sets** (`vitest list --json` over `launched.test.ts`, with the base bytes and then the head bytes in place).
   - [Observed] base 43 names (43 distinct) and head 43 (43 distinct), equal as sets: added `[]`, removed `[]`.
   - By family at both: 17 `launch forms in a run whose marker is unreadable > count neither…` rows, 3
     `launchedMarkerState > is unreadable for a marker that …` rows, and 23 others.
   - The diff changes only those two parametrised bodies, so `Tests: +0 ~20 -0` is right.
6. **The recorded harness, re-run.** I wrote the record's `harnessSource` byte for byte to a file (8062 bytes, sha256
   `2fbebbaf0311803dfd256e12a2894c3ffd03efbae5274dcf53fb4e5314c8c585`) and ran it at `9f09e5ca` with base `b7697f6a`.
   - [Observed] It printed the same summary as the record: F1 killed/killed, F2 survived/killed, H1 killed/killed, H2 killed/killed.
   - [Observed] A field comparison against the committed record shows 8 of 8 mutant entries identical on `id`, `tests`, `edits`,
     `exitCode`, `counts`, `failedTests` (including each `firstErrorLine`), `blocked`, `outcome` and `restored`.
   - `unmutated`, `summary`, `testSha256`, `readerSha256`, `command`, `timeoutSeconds`, `harnessSource` and `trackedTreeCleanAfter`
     are identical too. Only `commit` differs: `f25b335c` in the record, `9f09e5ca` in the re-run. The test and reader bytes are
     identical at the two commits (§1 item 6).
   - **H1 and H2, re-run** (the brief asked for these specifically). [Observed] At base, each failed
     `AssertionError: expected 'launched' to be 'unreadable' // Object.is equality`. At the fix, each failed
     `AssertionError: expected false to be true // Object.is equality` on the same test,
     `…grows past 4096 bytes between two reads, the first of which held the whole marker`. That is the `rewritten` expect at
     `launched.test.ts:110`.
7. **Reviewer mutants of `launched.ts`**, each run against the base and the head `launched.test.ts`. The D mutants were also run
   against the whole dossier project at head. Harness: `…/rev-506/tools/rev506.py`, sha256
   `ae3a1ffc2308bb88e74773596945fd04388b1906ff2c7faa88d9ced7e678ab15`. Results: `…/rev-506/rev506-results.json`, sha256
   `0af53e3d0133a8a5e13ff5644bb0000db3475c0af7343218894e8d13c01a79d1`. Each mutant's fragments are in Appendix A.

   | Mutant | Base tests | Head tests | Project at head |
   |---|---|---|---|
   | M-terminal-only-reads-fifo | killed, 1 failed (FIFO row) | killed, 1 failed (FIFO row) | — |
   | M-bang-only-reads-fifo | killed, 1 failed (FIFO row) | killed, 1 failed (FIFO row) | — |
   | M-syzygy-launched-only-reads-fifo (= F1) | killed, 1 failed (FIFO row) | killed, 1 failed (FIFO row) | — |
   | M-all-forms-drain-bang-unchecked | **survived**, 43/43 | **killed**, 1 failed (FIFO row) | — |
   | M-all-forms-drain-syzygy-launched-unchecked (= F2) | **survived**, 43/43 | **killed**, 1 failed (FIFO row) | — |
   | D1-launchFormRefusal-removes-an-unreadable-marker | **killed, 16 failed** (every launch-form row but the dangling link) | **survived, 43/43** | killed, 3 failed |
   | D2-launchedMarkerState-removes-an-unreadable-marker | killed, 19 failed | killed, 3 failed (the race rows only) | killed, 6 failed |

   - [Observed] First error lines:
     - Under M-terminal-only, M-bang-only and M-all-forms-drain-bang-unchecked, the FIFO row failed with
       `expected 'a launched run counts only sessions S…' to be 'the run\'s launched marker is present…'`.
     - Under F1 and F2 it failed with `expected null to be 'the run\'s launched marker is present…'`.
     - Under D1 at the project level, three assertion failures (not timeouts), each
       `AssertionError: expected { counts: false, …(1) } to deeply equal { counts: false, …(1) }`:
       `inventory.test.ts:455`, `review.test.ts:480` and `render.test.ts:705`.
     - Under D2, the head file fails only through the race rows' final `fs.statSync(marker(dir))`:
       `Error: ENOENT: no such file or directory, stat '/tmp/polaris-marker-…/launched.json'`.
   - [Observed] Unmutated: base 43/43 and head 43/43, exit 0. Both files were restored (digest-checked), and the tracked tree was clean
     after.
8. **Byte probe.** `…/rev-506/tools/probe506.test.ts`, sha256 `a7759869ddd8bcbd7719d30110c0ba953bb91f74dc2472bee495f01999c29199`,
   source in Appendix B.
   - Method: I copied the probe into `packages/polaris-dossier/src/` for the run, then deleted it. It plants the
     FIFO-holding-the-marker fixture with the same open flags and the same 231 `TYPED` bytes as `launched.test.ts:26-33`. It asks the
     three forms in two layouts: `shared` (one planted run, the base layout) and `fresh` (one run per form, the head layout). It
     counts the bytes `readSync` returns on the reader's own descriptor for each call, and then drains the test's own `keep`
     descriptor to count what was left in the pipe.
   - [Observed] Unmutated reader:
     - Every call reads 0 bytes in both layouts. `isFile()` refuses first, at `launched.ts:54`.
     - `shared` leaves 231 bytes in the pipe after all three calls, and `fresh` leaves 231 in each form's pipe. Every call returns the
       unreadable refusal.
   - [Observed] Under a mutant in which all three forms read any file type:
     - `shared` read 231 / 0 / 0 bytes for terminal / bang / syzygy-launched, leaving 0 bytes.
     - `fresh` read 231 / 231 / 231.
     - In `fresh`, `syzygy-launched` returns `null` (counted), and terminal and bang return
       `a launched run counts only sessions Syzygy launched (syzygy-launched, Observed)`.
   - [Observed] Under F2:
     - `shared` read 231 / 0 / 0, and every call returns the unreadable refusal. This is why F2 survives the base tests.
     - `fresh` read 231 / 231 / 231, and `syzygy-launched` returns `null`. This is why F2 is killed at head.
9. **Flakiness and leaks.** I ran the head `launched.test.ts` 10 times with `TMPDIR` pointed at a private empty directory.
   - [Observed] 10 of 10 runs passed 43/43, exit 0.
   - [Observed] After every run, the only entry in that directory was `node-compile-cache` (Node's compile cache). There was no
     `polaris-marker-*` directory, FIFO or temp file.
   - Five further runs of the head file also passed 43/43 under load: item 1, the two project runs in item 2, the fix-side
     unmutated run in item 6 and the head-side unmutated run in item 7. That is 15 head runs in all.
10. **N1's proposal, checked in scratch** (not in the PR). Script: `…/rev-506/tools/verify_proposal.py`, sha256
    `0687e6719072f829cf66e2136831f12a2e7111873105afae0a6a2754bd970331`. Results: `…/rev-506/proposal-results.json`, sha256
    `cc87e018537b8682cee74fe0d63e367c6a188edce0f55bfbdc7a4bfbff0cca50`.
    - [Observed] The head test with N1's post-condition (fragment in N1) gave:
      - unmutated: 43/43;
      - D1: killed, 16 failed, `expected 'absent' to be 'unreadable'`;
      - D2: killed, 19 failed;
      - F2: killed, 1 failed;
      - M-all-forms-drain-bang-unchecked: killed, 1 failed.
    - Both files were restored (digest-checked), and `git status --porcelain` was empty after.

## 4. Findings

No finding is blocking. Each of the following is a note.

### N1 — note, low. Planting afresh for all 17 rows drops this file's kill of a reader that alters an unreadable run

- **Evidence.**
  - [Observed] Base `launched.test.ts:115-121` asked all three forms of one planted run. Head `:118-123` plants a fresh run per call
    for every row of `PRESENT_BUT_NOT_THE_MARKER` (17 rows), not only the FIFO row that R3-N1 and the bead's design named ("for that
    row").
  - The PR body says so: "Every row now gets a fresh run, not only the FIFO row, so no row depends on what an earlier call left
    behind."
  - The shared layout did one more job. A later call on the same run could see what an earlier call did to it.
  - [Observed] Mutant D1 makes `launchFormRefusal` remove the marker when it reads `unreadable` (Appendix A). It is killed by the
    base file with 16 failures (`expected null to be 'the run\'s launched marker is present…'`: the `bang` call sees `absent` and
    counts). It **survives** the head file, 43/43.
  - [Observed] The suite still kills D1, through 3 assertion failures in other files: `inventory.test.ts:455`, `review.test.ts:480`
    and `render.test.ts:705`. [Inferred, from the failure shape] Those kills rely on each of those readers consulting the marker more
    than once in one evaluation.
  - [Observed] D2, the same removal inside `launchedMarkerState`, is still killed by the head file. But the head file kills it only
    through the race rows' final `fs.statSync` throwing `ENOENT`, an incidental throw, not a launch-form assertion.
- **Failure scenario.** [Inferred: no such code exists today]
  - A later change "cleans up" a marker it cannot read, for example so that a re-`init` of the run can proceed.
  - The run then reads `absent`, an operator-started run, on its next ask, and a declared `terminal` or `bang` form counts. That is
    the fail-open direction SEC-3's reader exists to prevent (`launched.ts:34-35`: "No caller may treat `unreadable` more leniently
    than `launched`").
  - Today three files outside `launched.test.ts` would catch it. A refactor of those readers to consult the marker once would leave
    nothing that names the defect, and the reader's own test file would stay green.
- **Proposed fix.** This is a test-only follow-up, and no outcome changes. In the launch-form row, assert after each ask that the run
  still reads as it did:
  ```ts
  // Each ask must leave its run as it found it, so a reader that alters an unreadable marker cannot pass here.
  const asked = (form: Readonly<Record<string, unknown>>): string | null => {
    const dir = planted();
    const reason = launchFormRefusal(dir, form);
    expect(launchedMarkerState(dir)).toBe('unreadable');
    return reason;
  };
  expect(asked({ value: 'terminal', declaredBy: 'operator', label: 'Inferred' })).toBe(refusal);
  ```
  Do the same for `bang` and `syzygy-launched`.
  - Checked in scratch (§3 item 10): it passes unmutated and kills D1 (16 failed), D2 (19), F2 and the `bang` drain mutant.
  - For the FIFO row, the post-condition reads nothing under the real reader (`isFile()` refuses first), so it drains no pipe.
  - Titles are unchanged, so the delta would be `Tests: +0 ~17 -0`.
  - The alternative is to plant afresh only for the FIFO row, as the bead's design said, and to keep the shared run for the other 16.

### N2 — note, low. AC1's named evidence (F1) does not discriminate; its intent rests on F2, this review's bang mutant and the byte probe

- **Evidence.**
  - [Observed] AC1 says the data-in-the-pipe property is "shown by a recorded rule-6 mutant: an isFile check removed from the
    syzygy-launched path only is killed by this row". That is F1.
  - F1 is killed by the base tests and by the head tests in the same row, with the same first error line, in the record and in my
    re-run (§3 item 6). So F1 cannot show that the refill does anything: it would pass AC1 with no change at all.
  - The PR body says this itself ("The mutant that needs the refill is F2").
  - [Observed] Per form:
    - `terminal` is the first call, and the probe shows it had the pipe's 231 bytes in the base layout too.
    - `syzygy-launched`: the record's F2 shows the head row catches a lenient branch after a draining one, and the base row does not.
    - `bang`: the record has no discriminating mutant. Only this review's M-all-forms-drain-bang-unchecked shows it (base survived,
      head killed, §3 item 7), with the probe's `fresh` 231 / 231 / 231 against `shared` 231 / 0 / 0 (§3 item 8).
  - [Observed] Every single-branch mutant (one form alone reads a FIFO) is killed at both base and head, for all three forms. Under
    such a mutant the other forms refuse before reading, so nothing drains the pipe ahead of the reading form. The refill matters only
    for a drain-then-lenient pair.
- **Failure scenario.** A later reader of the dispositions or of the bead takes "F1 killed" as the evidence for AC1. The next change
  to the row could then drop the per-form planting while F1 stays killed, and no recorded mutant would object for `bang`.
- **Proposed fix.** In the dispositions record, state that AC1 is met on:
  - F2 (record) for `syzygy-launched`;
  - this review's M-all-forms-drain-bang-unchecked for `bang` (fragments in Appendix A);
  - the probe for all three forms, with `terminal` trivially first.

  Say also that F1 is a valid but non-discriminating kill. Do not edit the mutants record (rule 10). If the row is touched again (N1),
  add the `bang` drain mutant to that change's rule-6 record.

### N3 — note, process. I rule the change class 4, so GP-Q0's owner notice belongs in the cycle report

- **Evidence.**
  - [Observed] The PR states "CC-REV-1 classes: none in the code, because no production file changes. The tests cover the
    launched-marker reader, which is a class-4 (security) reader".
  - The FIFO and race rows of `launched.test.ts` are the rule-6 kill evidence for the SEC-3 fail-closed reader. A change to them
    changes what that security check can detect: N1 shows such a change can weaken it.
  - Under CC-REV-1 ("A reviewer or the owner may reclassify at any time"), I rule it **class 4**.
  - GP-Q0's three extra checks then apply:
    1. Differential. It is degenerate: no production byte changes (§5), so every reader's output over any corpus is unchanged. I did
       not run a mutated-record corpus; identity of the code is the stronger evidence.
    2. A rule-6 mutant for each predicate. This is met by the record plus §3 item 7: each form's leg, each race row's staging assert
       (H1 and H2), and the post-call run state (N1).
    3. A non-blocking owner notice in the cycle report. [Unknown] I did not check `syzygy-bpyt.10`, and the PR does not mention one.
- **Failure scenario.** The cycle report omits a class-4 PR, and the owner's GP-Q0 notice trail has a gap.
- **Proposed fix.** The coordinator adds one line for PR #506 to `syzygy-bpyt.10`'s cycle report as a non-blocking owner notice
  ("test-only; class 4 by reviewer ruling; no production byte changed"), or records why it is not needed if the coordinator rules the
  class otherwise.

## 5. Every changed output, or the evidence that there is none

- [Observed] No production byte changes. Method 1: `git diff --stat 1d6731bb 9f09e5ca` lists 2 paths, a test file and a new evidence
  JSON. Method 2: the merge analysis (§1 item 4) shows every other path is main's blob.
- [Observed] `launched.ts` hashes `c7a25b8b45fe12e2add7874f88d46b2bad1eef16ffa4a17e2464d5c671424921` at `b7697f6a`, `1d6731bb`,
  `f25b335c`, `dc231c89` and `9f09e5ca`.
- [Observed] The new JSON is read by no code and cited by no tracked file. `git grep -n -F` over the tree at `9f09e5ca`, for both
  `launched-marker-test-refill` and `test-refill-mutants`, returns 0 hits. [Unknown] A citation wrapped across a line break is not
  covered by that sweep. The PR body cites the record, and the dispositions record will.
- [Observed] Test outputs: the name sets are equal (43 = 43), and all pass at head (§3 items 1, 2 and 5).
- Under GP-Q0 part 1, nothing on its list changes: no rendered byte, wire format, refusal string, exit code, signed or digest-bound
  artifact, or consent, security or retention decision. **More lenient: 0. Changed outcomes: 0.**

## 6. Verdict per acceptance criterion

1. **AC1 (each form evaluated with data in the pipe): Pass on intent, with N2.**
   - [Observed] The probe's head layout leaves 231 bytes in each form's pipe at its call. Under an all-forms-read mutant, each form
     reads 231 bytes, against 231 / 0 / 0 in the base layout.
   - Mutants that drain on an earlier form and are lenient on a later one survive the base tests and are killed by the head tests:
     F2 for `syzygy-launched` and M-all-forms-drain-bang-unchecked for `bang`.
   - The AC's parenthetical mutant (F1) is killed, as required, but it is killed at base too, so it is not the evidence (N2).
2. **AC2 (rewritten asserted before the state; hook disabled fails on the rewritten expect): Pass.**
   - [Observed] Head `launched.test.ts:109-111` computes `state`, asserts `expect(rewritten).toBe(true)`, then asserts
     `expect(state).toBe('unreadable')`.
   - H1 (hook disabled for `readSync`) and H2 (the `c571fb9f` `readFileSync` read) fail at head with `expected false to be true` on
     the between-reads row, re-run by me. At base they fail with `expected 'launched' to be 'unreadable'`.
   - The two fstat rows are unaffected by H1, because `call !== 'readSync'` holds for them.
3. **AC3 (~n only; project green): Pass.**
   - [Observed] The name sets are equal at 43 / 43, so `+0 ~20 -0`: 17 launch-form rows and 3 race rows.
   - The dossier project gave `1192 passed | 1 skipped (1193)` on the full re-run. The first run's single timeout was in an
     untouched file and passes in isolation (§3 item 2).

Brief questions:
- **Does each launch form now read a pipe that still holds data?** Yes, by the probe (§3 item 8). Under the real reader no form reads
  the pipe at all, because `isFile()` refuses first. The data is there for a mutant that would read it.
- **Does a mutant that lets exactly one branch read a FIFO fail the row for each form?** Yes, for all three (§3 item 7). Each was also
  killed at base, for the reason in N2.
- **Is the `rewritten` assert placed so that a race that never staged fails on it?** Yes (AC2).
- **Is F1 discriminating, and does AC1 rest on it?** No, and no: AC1 rests on F2, the `bang` drain mutant and the probe (N2).
- **Can any new fixture throw at describe time, leak, or flake?**
  - [Observed] The only new code is `planted`, a closure inside the test body (`:119`). The `it.each` tables are unchanged, so nothing
    new runs at describe time.
  - Each `planted()` registers `rmSync` through `runDir()`, and `fifoHoldingTheMarker` registers `closeSync(keep)` after it. The
    LIFO `afterEach` closes before it removes.
  - There were 0 leftovers over 10 runs, and 15 head runs in all passed under load (§3 item 9).
  - [Inferred] Nothing is timing-dependent. The FIFO write of 231 bytes is below `PIPE_BUF`, with a reader held open, and the race
    hooks are synchronous patches.
- **Evidence re-runnability (rules 6 and 11): Yes.**
  - The record names its subject (`launched.test.ts`) with base and fix digests, the reader's digest, the commit, the base, the
    command and the timeout.
  - It stores each mutant's `old`/`new` fragments and its whole harness. It reproduces 8 of 8 entries field for field at the
    reviewed head (§3 item 6).
  - `f25b335c` stays reachable through the merge commit if the PR lands by merge commit, which is how recent PRs have landed (for
    example `32c16625 Merge pull request #493`).
  - Minor, not a note: the harness's per-mutant `restored` field checks `launched.ts` only, so for H1, which edits the test file, test
    restoration rests on the `finally` and on `trackedTreeCleanAfter: true`. No outcome depends on it.

## 7. Test quality

- **Literal expectations.** [Observed] Every expectation in the changed bodies is a literal: the refusal string, `'unreadable'` and
  `true`. Bar 4 holds.
- **What each changed test catches** (core rule):
  - The launch-form row now catches a drain-then-lenient reader on `bang` and on `syzygy-launched`, which the base row missed.
  - It still catches every single-branch FIFO reader.
  - It no longer catches a reader that alters an unreadable run (N1).
  - The race rows now report a race that did not stage as `expected false to be true` at `:110`, the reason it has. Before, they
    reported it as a wrong state. That improves bar 7.
- **Readability.**
  - The two new comments (`:108`, `:118`) say why. They are 138 and 130 columns (`awk length`), within the file's existing range: 6
    lines run past 140, up to 264.
  - Minor wording, not a note: `:108` says the race "is asserted staged before the state is judged". The state is *computed* before
    the staging assert and *asserted* after it. The bead's own wording ("compute the state, then expect(rewritten), then expect the
    state") is clearer.
- **Determinism and isolation** (bar 6): see the brief question in §6. `patchFs` restores are LIFO through the shared `cleanups`, and
  the race patches are installed and used synchronously within one test.
- **Growth** (bar 10): `+0 ~20 -0`, with no new test. That is the right shape for a strengthening.

## 8. Cleanup

- All mutation and probe runs were in the scratch clone at
  `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-506/clone`.
- [Observed] After each harness, both mutated files were digest-checked as restored, the probe file was deleted, and
  `git status --porcelain` was empty.
- No worktree under `/home/tze/GitHub/syzygy/.worktrees/` was touched, and no process was killed by pattern. The harnesses kill only
  their own process groups on timeout, and none timed out.
- The scratch clone is deleted after this file is written. The reviewer's tools and result files stay beside this raw under
  `…/scratchpad/rev-506/` (`tools/`, `rev506-results.json`, `recorded-rerun.json`, `proposal-results.json` and `battery.json`), with
  the digests given above.

## Appendix A — reviewer mutant fragments (`packages/polaris-dossier/src/launched.ts`)

Each fragment occurs exactly once in `launched.ts` at `9f09e5ca` (sha256 `c7a25b8b…71424921`). Shared pieces:

- SIG: old `export function launchedMarkerState(runDir: string): LaunchedMarkerState {` → new
  `export function launchedMarkerState(runDir: string, anyFileType = false): LaunchedMarkerState {`.
- TYPE-GATED: old `    if (!stat.isFile() || stat.size > MARKER_BYTES_MAX) return 'unreadable';` → new
  `    if ((!anyFileType && !stat.isFile()) || stat.size > MARKER_BYTES_MAX) return 'unreadable';`.
- TYPE-AFTER-READ: two edits.
  - old `    if (!stat.isFile() || stat.size > MARKER_BYTES_MAX) return 'unreadable';` → new
    `    if (stat.size > MARKER_BYTES_MAX) return 'unreadable';`.
  - old `    if (length > MARKER_BYTES_MAX) return 'unreadable';` → new
    `    if (length > MARKER_BYTES_MAX || (!anyFileType && !stat.isFile())) return 'unreadable';`.
- CALL(x): old `  const state = launchedMarkerState(runDir);\n  if (state === 'unreadable')` → new
  `  const state = launchedMarkerState(runDir, x);\n  if (state === 'unreadable')`.

| Mutant | Edits |
|---|---|
| M-terminal-only-reads-fifo | SIG, TYPE-GATED, CALL(`form['value'] === 'terminal'`) |
| M-bang-only-reads-fifo | SIG, TYPE-GATED, CALL(`form['value'] === 'bang'`) |
| M-syzygy-launched-only-reads-fifo (= F1) | SIG, TYPE-GATED, CALL(`form['value'] === SYZYGY_LAUNCHED`) |
| M-all-forms-drain-bang-unchecked | SIG, TYPE-AFTER-READ, CALL(`form['value'] === 'bang'`) |
| M-all-forms-drain-syzygy-launched-unchecked (= F2) | SIG, TYPE-AFTER-READ, CALL(`form['value'] === SYZYGY_LAUNCHED`) |
| probe "all-forms-read-fifo" | SIG, TYPE-GATED, CALL(`true`) |

D1 (the new fragment is the two code spans below concatenated, `\n` being a newline): replace
`  if (state === 'unreadable') return 'the run\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched';`
with
`  if (state === 'unreadable') { try { fs.rmSync(path.join(runDir, RUN_LAYOUT.launched), { recursive: true, force: true }); } catch { /* reviewer mutant */ }`
`\n    return 'the run\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched'; }`.

D2: replace
`export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);`
with
`export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const state = launchedMarkerStateOnce(runDir);\n  if (state === 'unreadable') { try { fs.rmSync(path.join(runDir, RUN_LAYOUT.launched), { recursive: true, force: true }); } catch { /* reviewer mutant */ } }\n  return state;\n}\n\nfunction launchedMarkerStateOnce(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);`.

Command per run: `npx vitest run --project @syzygy/polaris-dossier --reporter=json --outputFile=<scratch>/rev-vitest.json packages/polaris-dossier/src/launched.test.ts`
(the project-level D runs omit the file argument), with `CI=1` and a 900 s timeout. None timed out. Killed means a nonzero exit with
at least one failed test.

## Appendix B — byte probe source (`probe506.test.ts`, run as `packages/polaris-dossier/src/zz-probe506.test.ts`)

```ts
// Reviewer probe for PR 506 (not part of the PR). For the FIFO-holding-the-marker fixture, asks the three launch forms in two layouts:
// "shared" (one planted run for all three, the base test's layout) and "fresh" (one planted run per form, the fix's layout). For each
// call it records the bytes the reader's own descriptor read, and, after the calls, the bytes still in each pipe.
import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { afterAll, it } from 'vitest';
import { patchFs } from './fs-patch.testkit.js';
import { launchFormRefusal } from './launched.js';

const TYPED = '{\n  "format": "polaris-dossier-launched/1",\n  "runId": "run-x",\n  "startedAt": "2026-10-21T00:00:00.000Z",\n  "command": "syzygy polaris",\n  "executionPermitted": false,\n  "direction": "POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14"\n}\n';
const FORMS = [
  { value: 'terminal', declaredBy: 'operator', label: 'Inferred' },
  { value: 'bang', declaredBy: 'operator', label: 'Inferred' },
  { value: 'syzygy-launched', declaredBy: 'syzygy', label: 'Observed' },
] as const;
const OUT = process.env['PROBE_506_OUT'] ?? '';
const result: Record<string, unknown> = { typedBytes: Buffer.byteLength(TYPED) };
const dirs: string[] = [];
const keeps = new Set<number>();

const plant = (): { dir: string; keep: number } => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'probe506-'));
  dirs.push(dir);
  const file = path.join(dir, 'launched.json');
  execFileSync('mkfifo', [file]);
  const keep = fs.openSync(file, fs.constants.O_RDONLY | fs.constants.O_NONBLOCK);
  keeps.add(keep);
  const writer = fs.openSync(file, fs.constants.O_WRONLY | fs.constants.O_NONBLOCK);
  fs.writeSync(writer, TYPED);
  fs.closeSync(writer);
  return { dir, keep };
};

let readByReader = 0;
const restore = patchFs('readSync', (original) => ((...args: unknown[]) => {
  const n = (original as (...a: unknown[]) => number)(...args);
  if (!keeps.has(args[0] as number)) readByReader += n;
  return n;
}) as never);

const left = (keep: number): number => {
  const buffer = Buffer.alloc(8192);
  let total = 0;
  for (;;) {
    let n = 0;
    try { n = fs.readSync(keep, buffer, 0, buffer.length, null); } catch { break; }
    if (n === 0) break;
    total += n;
  }
  return total;
};

it('probe: shared layout', () => {
  const { dir, keep } = plant();
  const calls = FORMS.map((form) => {
    readByReader = 0;
    const refusal = launchFormRefusal(dir, form);
    return { form: form.value, bytesReadByReader: readByReader, refusal };
  });
  result['shared'] = { calls, bytesLeftInPipeAfterAllThree: left(keep) };
});

it('probe: fresh layout', () => {
  const calls = FORMS.map((form) => {
    const { dir, keep } = plant();
    readByReader = 0;
    const refusal = launchFormRefusal(dir, form);
    return { form: form.value, bytesReadByReader: readByReader, refusal, bytesLeftInItsPipeAfter: left(keep) };
  });
  result['fresh'] = { calls };
});

afterAll(() => {
  restore();
  for (const keep of keeps) fs.closeSync(keep);
  for (const dir of dirs) fs.rmSync(dir, { recursive: true, force: true });
  if (OUT) fs.writeFileSync(OUT, `${JSON.stringify(result, null, 2)}\n`);
});
```
