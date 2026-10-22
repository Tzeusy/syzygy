# R-GP-IMPL-OUTSIDE-RAW-CLEANUP-1 — CC-REV-1 implementation review of syzygy-bpyt.4.12, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: a670f988
Subject: r1-review.diff sha256 5430edc6184be10f9305ce856d7519d6294a00112d5d3266b5c456158cc03130

Reviewer: rev-513, a fresh-context CC-REV-1 reviewer, on the default model. I did not author the change. I was read-only: I made
no edit to any repository or worktree, no push, no PR comment, no merge and no bd mutation. I read no observed-repository content.
Below, `<scratch>` is `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/rev-513/`, and
`<clone>` is `<scratch>clone`, a scratch clone checked out at `a670f988a701f23edb08ee4fa216896a7ef45567`.

Summary: no blocking finding, four notes.
- N1: I rule the change class 1, so GP-Q0's owner notice belongs in the cycle report.
- N2: the review-path row covers only a leading `..`. A reviewer mutant that checks only the first segment survives the whole file.
  This gap was already there before the change, and a one-row fix is verified in scratch.
- N3: the bead's AC3 says `~0` and class none. `Tests: +0 ~1 -0` is the right count, and the class is 1 (N1).
- N4: nothing fails mechanically if a test leaks into TMPDIR again. The leak was found by hand.

## 1. Subject identity checks

1. **Digest.** [Observed] `sha256sum` of the frozen `lead/b412/r1-review.diff` gives
   `5430edc6184be10f9305ce856d7519d6294a00112d5d3266b5c456158cc03130`, which matches the brief.
   - `git diff a04069678c02881cd41a25b850e14f79d581c083 a670f988a701f23edb08ee4fa216896a7ef45567`, written by
     `git diff --output=<scratch>rederived.diff` in `<clone>`, hashes to the same value. It matches.
2. **Commit and base.**
   - [Observed] `git fetch origin agent/syzygy-bpyt.4.12` in `<clone>` gives `FETCH_HEAD`
     `a670f988a701f23edb08ee4fa216896a7ef45567`.
   - [Observed] `gh pr view 513 --json headRefOid` gives the same sha, so the reviewed commit is the PR head.
   - [Observed] `git merge-base a0406967 a670f988` gives `a04069678c02881cd41a25b850e14f79d581c083`, which matches the brief.
3. **Paths.** [Observed] `git diff --name-only -z a0406967 a670f988` lists 2 paths:
   - `docs/evidence/waiting-sessions-outside-raw-cleanup-2026-10-22.json` (new, +152);
   - `packages/polaris-dossier/src/waiting-sessions.test.ts` (+4/−1). `git diff --stat` shows `5 +-`.
4. **History.** [Observed] `git log --graph` shows the history.
   - `73772882` (the test change) and `375a1e74` (the evidence record) sit on top of `4b31531c`.
   - `a670f988` merges main `a0406967` (#511) into them.
   - `73772882` and `375a1e74` are both ancestors of `a670f988` (`git merge-base --is-ancestor`, exit 0).
5. **The lane's claim that the main merge brought only main's bytes.**
   - [Observed] `git diff 4b31531c 375a1e74` hashes to `5430edc6…` as well, identical to the subject diff.
6. **Byte digests**, computed by `<scratch>tools/identity.py` (sha256 `c3a9ae5ba86f621aecec683930d97351b49bafd58f0cef64328ebfca962018e8`).
   - [Observed] `waiting-sessions.test.ts`:
     - `914d929d72fcc57c1d6b2db7701dab500829026c5f04a628a3c8274e0fcd86c6` at both `a0406967` and `4b31531c` (blob `1b8191eb`);
     - `89b2f9c0a19a0568c1dc5abd04f777b54848678ff266e82f5f9d74a379c7e853` at `73772882`, `375a1e74` and `a670f988` (blob `d71395aa`).
   - [Observed] `waiting-sessions.ts`: `a72090179eb44ac5c6b349edcdbcf74dbc6be68173c54be57ba2d11e63833e9b` at `a0406967`, `4b31531c`,
     `73772882` and `a670f988` (blob `5d0b98f1`). The reader is byte-identical across the whole history.
   - [Observed] The evidence record at `a670f988` hashes to `40e84bb3b8ae1225823248d2f002dc26add48dec5bc42902e215506e5325fb9d`, the
     value the PR body states.

## 2. Clauses relied on, and my class ruling

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`, at `a670f988`):
  - `:18-20`: "Changes touching any of seven classes require review by an independent, fresh-context reviewer, and the agent
    performing the change never finally decides which classes it touches."
  - `:31-32`: "1. **authority boundaries** — write-universe, typed-authority table, adapter authorization (VIS-5, VIS-6);"
  - `:37`: "4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;"
  - `:49-50`: "**The change record states** which classes the change touches, or "none," so a misclassification is a findable violation
    after the fact."
  - `:51`: "**A reviewer or the owner** may reclassify at any time."
- **GP-Q0** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - `:52-55`: "'Behavior-preserving' means none of the following changes: a rendered byte, a wire format, a refusal string or an exit
    code; a signed or digest-bound artifact; a consent, security or retention decision."
  - `:62`: "**Which ones:** pull requests touching class 1 (authority boundaries), class 3 (deterministic observation) or class 4
    (security), and class-6 pull requests that remove an endpoint."
  - `:63-66`: "**The checks:** an old-versus-new differential over a mutated-record corpus that includes records with altered prose; a
    rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report."
- **AGENTS.md** at `a670f988`:
  - Verification rule 6 (`:126-127`): "Mutate the input and confirm the check fails, per predicate, before trusting it".
  - Verification rule 9 (`:132`): "A claim of absence needs a sweep with a denominator."
  - Verification rule 11 (`:134-135`): "An evidence record names its subject and the subject's digest; a record that names neither
    cannot be re-checked against the bytes it describes."
  - Guardrail (`:263-265`): "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the commit it ran at; ids and
    outcomes alone are not re-runnable, and a rebase-merge leaves the recorded commit reachable from no ref."
- **Test-rigor bar** (`/home/tze/.claude/skills/th-engineering/subskills/test-rigor/SKILL.md`):
  - `:43`: "**A test is worth keeping only if some plausible bug makes it fail.**"
  - `:59-60`: "**Every bugfix ships a regression test** — Written to fail on pre-fix code."
  - `:61-64`: "**Edge and failure paths are first-class** — … Happy-path-only coverage of a failure-prone component is a finding."
  - `:94-101`: "Reviews state the net test delta".
- **The code the row guards** (`packages/polaris-dossier/src/waiting-sessions.ts`, at `a670f988`):
  - `:38`: "Gated: until the owner signs off version 1.2 of the specification, `waitModeSigned` is false and every wait-mode step
    refuses."
  - `:109-110`: "// path.join keeps even an absolute review path inside the records root; only a '..' segment could leave it." and
    `if (review === undefined || review.split('/').includes('..')) return false;`
- **Precedent**, the #506 raw (`docs/reviews/R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md:270-287`), N3:
  - "The FIFO and race rows of `launched.test.ts` are the rule-6 kill evidence for the SEC-3 fail-closed reader. A change to them
    changes what that security check can detect".
  - "I rule it **class 4**".

**Ruling: class 1 (authority boundaries).** The PR declares "class none".
- The changed row, "the record names a review outside the records root (mutant: drop the review-path check)", is the rule-6 kill
  evidence for the review-path predicate of `appliedSubjectHolds` (`:110`).
- That predicate is one leg of `waitModeSignedIn` (`:121-130`). It decides whether an owner sign-off of v1.2 exists, and so whether
  Syzygy may make session directories, write briefs and deliver packets in wait mode (`:22-38`). That is an authorization boundary on
  Syzygy's effects.
- As in #506, a change to a row that holds the kill evidence for a classed predicate touches that class, even when no production
  byte changes. The change could have weakened what the row detects; §3 item 6 shows a plausible variant that would have done so.
- I considered class 4 and do not rule it.
  - The predicate stops a review path in the owner's own decisions directory from leaving the records root.
  - It is an authenticity check on the owner act, and it touches none of the SEC-1…SEC-5 surfaces CC-REV-1 `:37` names (auth,
    egress, untrusted execution, write consent, secrets).
  - The owner may reclassify (`:51`).
- GP-Q0 `:62` therefore applies, and its three extras are taken one by one in N1.

## 3. What I ran and the results

All runs were in `<clone>` at `a670f988`.
- [Observed] Node `v24.6.0` (the `node-compile-cache/v24.6.0-x64-…` name) and vitest `3.2.7` (`node_modules/vitest/package.json`).
- `npm ci` (exit 0, "added 115 packages").
- Host load average was 36–46 throughout (`uptime`).

1. **`npm run typecheck`.** [Observed] The log `<scratch>typecheck.log` ends `exit=0`, with no diagnostic lines. The command runs
   `tsc -b` over the ten projects in `package.json:27`.
2. **`check_governance.py`.**
   - [Observed] I ran `python3 <scratch>clone-gov/scripts/check_governance.py`. `clone-gov` is a second scratch clone at `a670f988`,
     so the harness's in-place mutations could not race it.
   - Its head says "repo root: …/rev-513/clone-gov" and "3276 tracked".
   - Its last line: "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted", then `exit=0`.
   - The 21 WARN lines are the checker's standing report-only and allowlist buckets; I read each header line (log lines 6–1148).
     No line of the 1,156-line log names either changed path: `grep -cF -e waiting-sessions -e outside-raw-cleanup` counts 0.
   - Disclosure: an earlier invocation used a relative path. Its script locates its root from `__file__`, so it checked the main
     checkout `/home/tze/GitHub/syzygy`, not the subject. It is read-only, and `git -C /home/tze/GitHub/syzygy status --porcelain`
     afterwards shows only the two untracked files present at session start. Its log, `<scratch>check_governance.log`, is not
     evidence about this subject, and I cite nothing from it.
3. **Reviewer harness** `<scratch>tools/rev513.py` (sha256 `2b4c763bb051d6057f47c8ffe63710cd33379c05fe47ec9f8fe21a3c205e6b90`).
   Results: `<scratch>rev513-results.json` (sha256 `56f64ad546da27f19b12a0444349198faabcf9013fdda1477622ed3e4fe97eb0`). Per-run vitest
   JSON is in `<scratch>reports/`.
   - **Method.**
     - Each scenario writes exact fragment edits, each of which must occur exactly once, into the reader and/or the test file.
     - It runs `CI=1 TMPDIR=/tmp/r513-rev/t<n> npx vitest run --project @syzygy/polaris-dossier --reporter=json
       --outputFile=<scratch>reports/<id>.json [extra] packages/polaris-dossier/src/waiting-sessions.test.ts`, in a fresh, empty
       TMPDIR per run.
     - It lists that TMPDIR before and after: the top level, plus every path not under `node-compile-cache`.
     - It restores the bytes and checks both files' sha256 against the originals.
   - [Observed] `restored: true` in every run, and `trackedTreeCleanAfter: true`.

   | Id | Edits / args | Exit | Counts (pass/total) | Review-path row | TMPDIR after (before: empty in every run) |
   |---|---|---|---|---|---|
   | U-fix | none (fix tests) | 0 | 116/116 | passed | `node-compile-cache` |
   | U-base | none (base tests, `914d929d…`) | 0 | 116/116 | passed | `dossier-signoff-naWaoW-outside-RAW.md`, `node-compile-cache` |
   | R1-fix | lane's R1 on the reader | 1 | 115/116 | **failed**: `AssertionError: expected true to be false // Object.is equality` | `node-compile-cache` |
   | R1-base | lane's R1, base tests | 1 | 115/116 | **failed**, same line | `dossier-signoff-TzToKO-outside-RAW.md`, `node-compile-cache` |
   | R2-fix | reviewer R2 on the reader (below) | 0 | 116/116 | passed: **R2 survives** | `node-compile-cache` |
   | T-eager+R1-fix | removal moved to just after the write, plus R1 | 0 | 116/116 | passed: **R1 survives** | `node-compile-cache` |
   | T-drop-fix | the `cleanups.push(…)` line removed | 0 | 116/116 | passed | `dossier-signoff-u7P9A4-outside-RAW.md`, `node-compile-cache` |
   | P-throw-fix | `throw new Error('probe: thrown after the write')` after the write | 1 | 115/116 | failed: `Error: probe: thrown after the write` | `node-compile-cache` |
   | P-retry+R1-fix | R1, `--retry=2` | 1 | 115/116 | failed, 3 failure messages, each `AssertionError: expected true to be false // Object.is equality` | `node-compile-cache` |
   | P-timeout-fix | `--testTimeout=1` | 1 | 2/116 | failed: vitest timeout error (stack head `Error: STACK_TRACE_ERROR`; row duration 1.587 ms) | `node-compile-cache` |

   - **Fragments**, stored verbatim in the results file:
     - R1: `  if (review === undefined || review.split('/').includes('..')) return false;` → `  if (review === undefined) return false;`
       (the lane's mutant).
     - R2: the same `old` → `  if (review === undefined || review.split('/')[0] === '..') return false;`, which rejects only a leading
       `..` segment.
     - T-eager: `      fs.writeFileSync(outside, reviewHead(digest));\n` → that line followed by `      fs.rmSync(outside);\n`.
     - T-drop: `      cleanups.push(() => fs.rmSync(outside, { force: true }));\n` → empty.
   - **The timeout row.** [Inferred] The first line `Error: STACK_TRACE_ERROR` is vitest's timeout error.
     - `makeTimeoutError` (`node_modules/@vitest/runner/dist/chunk-hooks.js:2005-2011`) builds "Test timed out in 1ms." and replaces
       its stack with the registration-site stack, whose first line the JSON reporter prints.
     - The row is synchronous, so its body ran to completion. Then `resolve` found the elapsed time ≥ the bound (`:1883-1885`) and
       rejected.
4. **Is the leak closed on every path?**
   - [Observed] Code: the row builds `outside` once, registers `cleanups.push(() => fs.rmSync(outside, { force: true }))` and only
     then writes (`waiting-sessions.test.ts:277-279`). The module-level `afterEach` drains `cleanups` in reverse (`:25-26`).
   - [Observed] Vitest 3.2.7 runs `afterEach` once per try, outside the try that runs the test body
     (`chunk-hooks.js:1556-1602`: the body's `catch (e) { failTask(…) }` at `:1587-1589`, then
     `await callSuiteHook(suite, test, "afterEach", …)` at `:1597`). So every failure or retry path still drains the cleanups.
   - [Observed] Measured above, each path left no `dossier-*` entry:
     - a failing assertion (R1-fix);
     - a throw after the write (P-throw);
     - three tries under `--retry=2` (P-retry);
     - the timeout path (P-timeout).
   - [Inferred] A thrown write is also covered.
     - The removal is registered before `writeFileSync`, and `rmSync(…, { force: true })` on an absent path does not throw.
     - [Observed] I probed it with `node -e`: an absent path gives "absent ok".
   - [Inferred] What it can delete.
     - It removes exactly one path, with no glob. `outside` is `<dirname(root)>/<basename(root)>-outside-RAW.md`, where `root` is a
       fresh `mkdtemp` directory (`:27-31`). So the name is unique to this test's root, and no other worker or file writes it.
     - [Observed] Without `recursive`, `rmSync` refuses a directory. A `node -e` probe on a directory printed
       "threw ERR_FS_EISDIR exists true".
   - [Inferred] Residual: a hard kill.
     - SIGKILL, a worker crash or an aborted run skips `afterEach`. That leaves both this file and the `mkdtemp` root, as it already
       does for every `tempDir` in the file.
     - It is parity with the existing pattern, not a regression. Nesting the records root one level inside the `mkdtemp` directory
       would put the raw inside the directory one removal deletes. The bead allowed either shape.
5. **Is every assertion unchanged?**
   - [Observed] The diff touches only lines inside the row's `mutate` callback (`:276-279` new, one old line). The shared body
     `:283-290`, with `expect(waitModeSignedIn(root)).toBe(true)` before `mutate` and `.toBe(false)` after it, is untouched.
   - [Observed] The raw's path expression and bytes (`reviewHead(digest)`) and the record rewrite (`:281`) are unchanged.
   - [Observed] R1 is killed by the same row with the same first line at base and at the fix.
   - [Observed] Test names: `<scratch>tools/names.py` (sha256 `685670437fb1c6a75d0543587fa80deb00c29a78eaca5da208bb0843402339aa`)
     over the U-base and U-fix reports prints "base 116 fix 116 distinct 116 116", "added []" and "removed []".
6. **What T-eager shows.** [Observed] With the raw removed right after it is written, R1 survives (116/116). The row's kill depends on
   the raw still existing when `waitModeSignedIn` is asked the second time. The fix keeps the removal in `afterEach`, after the
   assertion, and that ordering is what preserves the kill. A plausible "simpler" fix would have silently lost it. This is why I rule
   class 1 above. N2 proposes a comment that says so.
7. **The lane's evidence record, against rules 6 and 11.**
   - [Observed] It names its subject (`"subject": ["packages/polaris-dossier/src/waiting-sessions.test.ts"]`) and the subject's
     digests at base and at the fix (`testSha256`, both equal to §1 item 6). It also names the reader's digest, the commit it ran at
     (`73772882d31c9be10c7dfb472092675f7fccc105`), its base (`4b31531c…`) and the command.
   - [Observed] It stores each mutant's file and `old`/`new` fragment, each failed test with its first error line, a full TMPDIR
     listing before and after every run, and the harness source. The embedded `harnessSource` string hashes to
     `58500a5bdbb31b9083f7f5d7905c4d5d8a6e0f8e958870dbd1d12d3f14235927`.
   - [Observed] Its recorded commit is an ancestor of `a670f988`.
     - [Inferred] It stays reachable after landing if the PR lands by merge commit, as recent PRs did (`32c16625 Merge pull request
       #493`, `a0406967 Merge pull request #511`).
   - [Observed] Its base `4b31531c` is not the current merge base `a0406967`, but both files are the same blobs at both (§1 item 6).
   - [Observed] I re-derived its listings.
     - The base leaves exactly one `dossier-signoff-<6 chars>-outside-RAW.md` beside `node-compile-cache`, unmutated and under R1.
     - The fix leaves only `node-compile-cache`, unmutated and under R1.
     - The suffixes differ, as `mkdtemp` makes them random.
   - [Observed] The record counts a timed-out run as "killed". Neither of its R1 runs timed out (`"blocked": false`), and the only
     failed test in each is the row. So that rule does not affect its outcome here.
8. **Other leaks** (rule 9, population: the ten fresh TMPDIRs of item 3 and the three of item 9, 13 runs of this file).
   - [Observed] Apart from this row's raw, the only entry any run left was `node-compile-cache`: Node 24's own module compile cache, a
     directory `v24.6.0-x64-ef5a0af0-1000/` of hashed files.
     - The deep listing outside it was empty in every run where the row cleans up.
     - The raw appeared only where the row's cleanup was absent: U-base, R1-base and T-drop.
   - [Inferred] The change neither causes nor fixes `node-compile-cache`, and no test writes it.
   - [Observed] No 5 s timeout of the kind `syzygy-bpyt.4.13` tracks occurred in any run of this file.
9. **N2's proposed row, checked in scratch.** Not part of the PR.
   - Script: `<scratch>tools/proposal.py` (sha256 `be014974e381a1374991ee8d5ed4b1d5485cd723960a526875647ffec84c2259`).
   - Results: `<scratch>proposal-results.json` (sha256 `f8d64e3fcae6920b94d42068ff1bf023a02a6738e77cae6ac84efee1d9f4a4ae`).
   - The script adds one row before `  ])('opens on no record when %s'`, identical to the reviewed row except that the record names
     `Review: docs/../../${path.basename(root)}-outside-RAW.md`.
   - [Observed]:
     - unmutated: 117/117 pass;
     - R2: exit 1, 116/117. The new row fails with `AssertionError: expected true to be false // Object.is equality`, and the
       existing row passes;
     - R1: exit 1, 115/117. Both rows fail with the same line.
   - [Observed] Every TMPDIR after held only `node-compile-cache`. Bytes were restored, and the tracked tree was clean afterwards.

## 4. Findings

No F (blocking) findings.

### N1 — note, process. I rule the change class 1, so GP-Q0's three extras apply. Two are met; the owner notice is pending

- **Severity.** Low (process). It does not block merge: GP-Q0 `:66` calls the notice "non-blocking".
- **Evidence.**
  - [Observed] The PR body declares "class none declared; class 1 possible by the #506 N3 precedent".
  - My ruling and reasons are in §2. GP-Q0 `:62-66`'s extras:
    1. **Differential.** Met by identity, and degenerate. [Observed] `waiting-sessions.ts` is byte-identical at base and head
       (`a7209017…` at all four commits, §1 item 6), and no production or root file changes (§5). So any old-versus-new differential
       over any record corpus is identical by construction. I did not run a mutated-record corpus: identity of the code is the
       stronger evidence. This is the #506 raw's reasoning (`R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md:279-280`).
    2. **A rule-6 mutant for each predicate.** Met for the one predicate this row covers. [Observed] R1 is killed at base and at fix,
       in the lane's record and in mine. The other gate predicates have their own rows, and the diff leaves those rows untouched.
       This row's coverage is partial (N2), but that was already so before the change.
    3. **A non-blocking owner notice in the cycle report.**
       - [Observed] `bd comments syzygy-bpyt.10`, read today, has no line naming #513 or `syzygy-bpyt.4.12`.
       - [Inferred] Earlier notices were posted after landing, so the absence before merge is expected. The #511 raw found the
         same ("syzygy-bpyt.8.14 merged (PR #506)", `R-GP-IMPL-LAUNCH-FORM-POSTCONDITION-1-RAW.md:286-287`).
- **Failure scenario.** The cycle report omits a class-1 PR. The owner's GP-Q0 notice trail then has a gap, and the PR record still
  says "class none", which CC-REV-1 `:49-50` makes a findable misclassification.
- **Proposed fix.**
  - At landing, the coordinator adds one OWNER NOTICE comment for PR #513 to `syzygy-bpyt.10`, for example: "test-only; class 1 by
    reviewer ruling (the review-path row is kill evidence for the v1.2 sign-off gate); no production byte changed; R1 killed at base
    and fix; follow-up <N2 bead>".
  - The dispositions record notes that the declared class is superseded by this ruling. Do not edit the PR's evidence record.

### N2 — note, test rigor, pre-existing. The review-path row covers only a leading `..`. R2 survives the whole file

- **Severity.** Low-to-medium (test rigor bar 3), on an owner-gate predicate. The gap was there before this change, which neither
  causes nor widens it. [Inferred] R2 at base would behave identically: the reader and the row's record line (`:281`) are the same
  bytes at base and fix. I ran R2 at the fix only.
- **Evidence.**
  - [Observed] The reader rejects any `..` segment (`waiting-sessions.ts:110`). The row exercises only `Review: ../<root>-outside-RAW.md`
    (`waiting-sessions.test.ts:281`).
  - [Observed] R2 (`review.split('/')[0] === '..'`) passes 116/116 at the fix (§3 item 3). The same holds for any check of the form
    "starts with `../`".
  - [Observed] Under such a mutant, a record naming `docs/../../<root>-outside-RAW.md` resolves through `path.join` to the same file
    outside the root. In §3 item 9 the gate opens on it: the proposed row fails under R2.
- **Failure scenario.**
  - A later refactor "simplifies" the containment check to a leading-segment test, perhaps to satisfy a linter or to reuse a helper.
  - CI stays green, and a sign-off record whose review path climbs out after its first segment opens the v1.2 gate on a review the
    records root does not hold.
- **Proposed fix.** A follow-up bead in the dossier area, or under `syzygy-bpyt.4`.
  - Add one row to the same `it.each` at `waiting-sessions.test.ts:256-290`. Copy the reviewed row, change the record line to
    `` `Review: docs/../../${path.basename(root)}-outside-RAW.md` ``, and title it e.g. "the record names a review that leaves the
    records root after its first segment (mutant: check only the first segment)". `Tests: +1 ~0 -0`.
  - Record R2 and R1 against it. §3 item 9 already shows the expected shape: 117/117 unmutated; R2 kills only the new row; R1 kills
    both.
  - In the same change, extend the reviewed row's comment to say that the raw must exist until the gate is asked. T-eager (§3 item 6)
    shows that removing it before the assertion silently loses R1's kill.
  - This is a row addition, so it cannot ride in this PR: AC2 fixes the assertions, and AC3 fixes the count.

### N3 — note, record accuracy. AC3 says `~0` and class none. The right values are `~1` and class 1

- **Severity.** Trivial (record). No byte changes.
- **Evidence.**
  - [Observed] The bead's AC3 reads "Tests +0 ~0 -0; class none". The PR says `Tests: +0 ~1 -0` and argues that `~0` "means that
    titles are unchanged".
  - [Observed] In this campaign's raws, `~n` counts the expanded tests whose bodies changed while their titles stayed the same:
    - "The diff changes only those two parametrised bodies, so `Tests: +0 ~20 -0` is right"
      (`R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md:122`);
    - "expands to the 17 rows of `PRESENT_BUT_NOT_THE_MARKER`, so `Tests: +0 ~17 -0` is right"
      (`R-GP-IMPL-LAUNCH-FORM-POSTCONDITION-1-RAW.md:132`).
  - [Observed] Here exactly one of the five rows of the `it.each` at `:256-290` has a changed callback, and the shared body is
    unchanged. So one expanded test's executed code changed: `~1`.
  - [Observed] Names are 116 = 116, with none added or removed (§3 item 5).
  - The class is ruled in N1.
- **Does the gap matter?** No, for the merge. AC3's evident intent, no added or removed tests, holds. `~1` is the accurate delta and
  the PR states it. The bead's text is wrong on its face, and only the record needs correcting.
- **Failure scenario.** A later reader checks the PR against AC3 literally and records a false "AC3 not met". Or someone copies "~0"
  into the cycle report as the delta.
- **Proposed fix.** The dispositions record states "AC3: `Tests: +0 ~1 -0` is correct (one row's callback changed, titles
  unchanged); class 1 by reviewer ruling (N1)". The coordinator closes the bead with that wording. Do not edit the PR.

### N4 — note, test rigor. No mechanical guard against a recurrence. The leak was found by hand

- **Severity.** Low (test rigor bar 2, at suite level).
- **Evidence.**
  - [Observed] The fix is verified by the evidence record's before/after listing, which a person ran. No test or CI step fails if a
    row writes outside its temp root again. With the cleanup line removed (T-drop), the suite stays 116/116 green and only the
    listing shows the stray.
  - [Observed] The same class of leak is open in two sibling beads:
    - `syzygy-bpyt.4.10`, POC fixture directories;
    - `syzygy-bpyt.4.11`, Chrome singleton directories.
  - [Observed] Each of these three was found by a person listing a TMPDIR.
- **Failure scenario.** A new dossier or POC row writes beside its `mkdtemp` root, every run passes, and files accumulate under the
  shared `/tmp` across lanes and batteries, as in the 2026-10-15 inode exhaustion that `syzygy-bpyt.4.10` cites.
- **Proposed fix.** A follow-up bead, or an added acceptance criterion on `syzygy-bpyt.4.3` (the tiers bead) or `syzygy-bpyt.4.4`
  (the test-kit bead, whose `tempDir()` is the natural owner).
  - The unit tier runs once with a fresh private TMPDIR.
  - The step fails if anything other than `node-compile-cache` remains afterwards, and it prints the leftover names.
  - Record a rule-6 run: base `914d929d…` of `waiting-sessions.test.ts` must make the step fail.

## 5. Every changed output, or the evidence that there is none

None. [Observed] Three methods over `a0406967..a670f988` agree, computed by `<scratch>tools/identity.py`:
1. **Paths changed.** `git diff --name-only -z` lists 2 paths, the test file and the new evidence JSON.
   - Filtered to production or root files (`packages/`, `apps/` or `scripts/` outside `*.test.ts` and `*.testkit.ts`, or any
     top-level file), the list is `[]`.
2. **Per-path blobs.** I compared `git ls-tree -r -z` at both commits over the union of 3,276 tracked paths. Exactly 2 differ, the
   same two.
3. **Diff with the two excluded.** `git diff --quiet a0406967 a670f988 -- . ':(exclude)<test>' ':(exclude)<evidence>'` exits 0.

The lane's "2 of 3,264 tracked files" is measured at `375a1e74`. [Observed] `git ls-tree` gives 3,264 there and 3,276 at
`a670f988`. Method 2 shows that the 12-file difference is main's bytes: none of them differs from `a0406967`.

[Observed] The reader, `waiting-sessions.ts`, is byte-identical at every commit in question (§1 item 6). So no refusal string, exit
code, rendered byte or gate decision can differ. No signed or digest-bound artifact is touched (GP-Q0 `:52-55`): the only new file
is an unbound evidence JSON, and `check_governance` reports 0 FAIL at `a670f988`.

## 6. Verdict per acceptance criterion

1. **AC1** ("A fresh-TMPDIR run of waiting-sessions.test.ts leaves no dossier-signoff-* file (listing recorded before and after)"):
   **Pass.**
   - [Observed] At the fix, seven fresh-TMPDIR runs leave no `dossier-*` entry: unmutated, R1, R2, throw, retry, timeout and
     T-eager. Four of them fail the row.
   - The base reproduces exactly one.
   - The lane's record holds the listings, and I re-derived them (§3 items 3 and 7).
2. **AC2** ("The test's assertions are unchanged and it still fails when the outside raw is wrongly honoured (rule-6 mutant
   recorded)"): **Pass.**
   - [Observed] No assertion line changed (§3 item 5).
   - R1 is killed by the row at the fix, with the same first line as at base, in the lane's record and in my run.
   - The row's coverage of other path shapes is N2, which was already so before the change.
3. **AC3** ("Tests +0 ~0 -0; class none"): **Met in substance; wrong as written on both counts (N3, N1).**
   - [Observed] No test is added or removed (116 = 116, the same names).
   - The accurate delta is `+0 ~1 -0`, as the PR states.
   - The class is 1 by my ruling, not none.
   - Neither correction changes the reviewed bytes.

## 7. Test quality

- **Core rule** (`:43`). [Observed] The changed row still fails under a plausible bug, the traversal check dropped (R1), at the fix.
- **Bar 2** (regression test). [Observed] The leak's fix has no test that fails on the pre-fix code. Only the listing in the evidence
  record shows it. That is acceptable for a test-hygiene fix, but it leaves recurrence unguarded: N4.
- **Bar 3** (edge and failure paths). [Observed] The predicate is pinned for one path shape only: N2.
- **Bar 4** (no tautologies). [Observed] The expectations are the literals `true`/`false`. The digest is computed from the spec's
  bytes on disk, independently of the reader.
- **Bar 6** (determinism). [Inferred] The change adds no nondeterminism.
  - The removal is idempotent (`force: true`), registered before the write and drained per try (§3 item 4).
  - The row is synchronous, so a timeout cannot interleave between write and assertion.
  - [Observed] In 13 runs of this file under load 36–46, the only failures were the ones the mutants and probes caused.
- **Bar 7** (failure names the defect). Unchanged. The title names the mutant it kills. The failure line is the generic
  `expected true to be false`, but the row title localizes it.
- **Bar 8** (maintained code). [Observed] Readability improves.
  - The outside path is now built once, as `outside`, where it was inlined into the write before.
  - The new comment explains why this row cleans up itself: "The raw lies beside the records root, outside the temp directory the
    test removes, so the test removes it itself."
  - The comment does not say that the removal must wait until after the assertion. T-eager shows this matters (N2's last bullet).
- **Bar 10** (growth). `+0 ~1 -0`. No growth. Cleaning up in place, in the row that leaked, is the right shape.

## 8. Cleanup

- [Observed] Before deletion, `git -C <clone> status --porcelain` printed nothing. Both harnesses restored every byte they mutated
  and checked the digests.
- I delete `<clone>`, `<scratch>clone-gov`, and the private TMPDIR roots `/tmp/r513-rev` and `/tmp/r513-prop`. The directory probe of
  §3 item 4 removed itself (`fs.rmdirSync`).
- I deleted nothing else in `/tmp`.
- These stay beside this raw in `<scratch>`:
  - the tools: `tools/rev513.py`, `tools/proposal.py`, `tools/identity.py` and `tools/names.py`;
  - the results: `rev513-results.json`, `proposal-results.json`, `reports/`, `proposal-reports/`, `rederived.diff`,
    `typecheck.log`, `check_governance-clone.log` and `rev513.log`/`proposal.log`;
  - the disclosed, non-subject `check_governance.log` (§3 item 2).
- No background process of mine is left running.
