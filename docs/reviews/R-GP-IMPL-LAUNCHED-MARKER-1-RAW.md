# R-GP-IMPL-LAUNCHED-MARKER-1 — CC-REV-1 implementation review of syzygy-bpyt.8.8
Verdict: REVISE
Reviewed commit: 1e153a0d
Subject: review.diff sha256 472bd009085b3738a264e657b0d86542045721535b00ba632707ac2677e27fb6

Reviewer: a fresh-context CC-REV-1 reviewer for class 4 (security). I did not author the change. I fetched no target-repository
content, read no observed repository body, and made no network fetch. I did not edit the worktree; every mutant, harness and
probe ran in a scratch clone that is now deleted.

## 1. Subject identity checks

- [Observed] `sha256sum` of `lead/b88/review.diff` gives `472bd009085b3738a264e657b0d86542045721535b00ba632707ac2677e27fb6`,
  the digest in the brief.
- [Observed] `git diff 29e036f4ee6a051cdafde98b8ec37185438c0f74 1e153a0d` in the worktree, written to a scratch file, hashes to the
  same digest. The worktree was clean, and HEAD was `1e153a0d20ae55ed8a6bb1c129b010766f9c8f88` at the start and at the end.
- [Observed] The diff touches 17 files, with 2144 insertions and 23 deletions:
  - eight source files under `packages/polaris-dossier/src/`;
  - seven test files;
  - two evidence records under `docs/evidence/`.
- [Observed] Commit `c03d3e63` (the mutants record's commit) and HEAD differ only by the two evidence files, so the mutants ran on
  the reviewed code and tests.
- [Observed] Both evidence records name their subject files with sha256 digests (rule 11). A script checked 36 digest assertions
  against `git show <commit>:<path>` and found 0 mismatches:
  - the differential's base side at `29e036f4` and its fix side at `900a494b`;
  - the mutants record at both `c03d3e63` and `1e153a0d`;
  - the eight fix-side files, which are byte-identical at `900a494b` and HEAD.
- [Observed] The differential stores its harness verbatim in `harness.source`. The UTF-8 bytes of that string hash to the
  declared `fe428f4cab43e8b21ad6f63faba4fd0ceb2fa2c2a4a6fa3a16ac6085d01c668a`.

## 2. Clauses relied on

- **CC-REV-1** (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:16-20, 37`): "Changes touching any of
  seven classes require review by an independent, fresh-context reviewer". Class 4 is "**security** — anything under
  SEC-1…SEC-5, auth surfaces, egress paths".
- **SEC-3 as amended by D9** (`.syzygy/governance/doctrine/security.md`):
  - lines 65-69: "**What this binds:** Syzygy itself, every process Syzygy launches or schedules, and every instruction a Syzygy
    feature gives an agent (a brief, prompt, skill or work item)";
  - lines 90-92: "**Whom the case binds:** Syzygy. Syzygy never gives the instruction to a session it started or to one left
    running unattended";
  - lines 95-99: "**What the permitted case costs:** the session runs with the owner's own credentials and network … Nothing
    contains it, so it gives none of a profile's guarantees."
- **REQ-polaris-generation-033** (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:15`):
  - the brief may permit execution only when the authoring session is one the owner started and attends, "never a session Syzygy
    started, one left running unattended, or one left under an automatic-approval or permission-bypass setting while the owner is
    away";
  - "Otherwise the brief SHALL carry SEC-3's rule".
- **Candidate REQ-polaris-generation-041** (`openspec/changes/polaris-dossier-one-command-run/proposed/polaris-generation/spec.md:65`;
  candidate, binds nothing): "An inventory or verdict from a launched run SHALL count only when its session's launch record exists
  and names that session's directory; Syzygy SHALL refuse a declared `terminal` or `bang` launch form in a launched run."
- **Candidate REQ-polaris-generation-044** (the same file, line 208; candidate): "Syzygy SHALL refuse `allow-execution` for a
  launched run". Its falsifier, line 231, includes "An execution choice is recorded for a launched run".
- **The owner's approval** (`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`):
  - Part 3, line 93: "New | `isLaunchedRun` is read fail-closed, at both `allow-execution` and brief issuance".
  - Lines 95-96: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
  - GP-Q0, lines 59-66: class 1/3/4 pull requests get "an old-versus-new differential over a mutated-record corpus that includes
    records with altered prose; a rule-6 mutant for each predicate; a non-blocking owner notice in the cycle report."
- **The bead** (`bd show syzygy-bpyt.8.8`, read-only):
  - outcome: "a run whose launched marker is present but unreadable or malformed is treated as launched (refused) at both syzygy
    dossier allow-execution and brief issuance; an absent marker still means not launched";
  - acceptance criterion 3: "PR lists each changed refusal".
- **AGENTS.md:**
  - verification rules 2, 4, 6, 9 and 11;
  - the guardrails "Fail-closed polarity: withdrawal defeats grant; future-dated evidence is stale; no evidence → Unknown",
    "Conformance expected values are hard-coded literals, never imported from the module under test", and the rule-6 record
    guardrail (each mutant's `old`/`new` and the commit it ran at).

## 3. What I ran and the results

All runs used a scratch clone at `1e153a0d` with `npm ci`, plus a second worktree of that clone at `29e036f4` with its own
`npm ci`.

1. **The full `@syzygy/polaris-dossier` vitest project at HEAD.** [Observed] `Test Files  29 passed (29)`, `Tests  1162 passed |
   1 skipped (1163)`. The one skip is the host-dependent strace proof in `no-egress.test.ts` (`describe.skipIf(HAVE_STRACE)`,
   lines 94-96), which this diff does not touch. No load flake occurred.
2. **Type check.** [Observed] `npx tsc -b packages/polaris-dossier` exits 0 at HEAD. Every caller of `decideExecutionRule`
   therefore passes the newly required `launched` field.
3. **The differential, re-run from its record.**
   - Method: I extracted `harness.source`, ran it at the fix, then restored the eight subject files from `29e036f4` and ran it
     again, as the record's `method` and `command` state.
   - [Observed] A comparison script found 0 mismatches against the recorded rows: 15 variants × 5 probes = 75 comparisons, of
     which 50 changed. The `absent` variant is unchanged at all five probes.
   - [Observed] All 30 arm-off briefs (old and new) share one byte pair: `brief.md`
     `af5253644108fad53e59187f757f6f0607c88bd881801e868f675dc5fe37feed`, `brief.json`
     `19feb99936b134767dfa2ecf7e302dc8244288fd72d6ca533cc8e83a60b67e12`.
   - [Observed] No changed comparison permits more at the new commit: no choice written, record written, null launch-form refusal
     or permitting brief that the old commit lacked.
4. **The rule-6 mutants, re-run from their record.**
   - Method: for each mutant I checked that `old` occurs exactly once (it does for all 12), applied `new`, ran the recorded
     command, and restored the bytes.
   - [Observed] Unmutated: `Tests  217 passed (217)`.
   - [Observed] All 12 recorded mutants were killed. Each reproduced the recorded `Tests` line and exit code exactly, and the
     tracked tree was clean afterwards.
   - My four extra mutants:
     - R1, `inventory.ts:235` `launched: launchedMarkerState(opened.run)` → `launched: 'absent'`: **survived**. It is an
       equivalent mutant; see N4.
     - R2, `review.ts:664` wording reverted to the old ternary: **survived**. The author disclosed this in `notCovered`; see N5.
     - R3, `session-handover.ts:556` `marker === 'launched'` → `String(marker) === 'never'`: killed, 1 failed.
     - R4, `launched.ts:40` `fs.lstatSync` → `fs.statSync`: killed, 2 failed. The dangling-link fixture holds the
       lstat-not-stat choice.
5. **Probes beyond the recorded corpus, on built `dist` at both commits.** Each probe ran in its own `node` process with a 20-30
   second timeout. Scripts and outputs are kept under the scratch root (§9).

| Marker state | Old (`isLaunchedRun`) | New (`launchedMarkerState`) |
|---|---|---|
| symlink to a valid marker elsewhere | true | `launched` |
| FIFO at `launched.json` | blocks | blocks |
| symlink to `/dev/null` | false | `unreadable` |
| symlink loop | false | `unreadable` |
| `{"__proto__": {"format": …}}` | false | `unreadable` |
| valid marker with surrounding whitespace and an extra field | true | `launched` |
| non-UTF-8 bytes | false | `unreadable` |
| run path whose parent is a file (ENOTDIR) | false | `unreadable` |
| run directory mode 000 | false | `unreadable` |
| run directory mode 0300 (search only) with a valid marker | true | `launched` |

   - Arm-off `brief` (`issueBrief`, the shipped build) with a FIFO marker: old **issues** the brief in 44 ms with the bytes
     above; new **blocks** past the 20 s timeout. [Observed]
   - Arm-off `brief` with `launched.json` → `/dev/zero`, under `prlimit --as=3000000000`: old issues the same bytes in 39 ms; new
     **aborts**, with `terminate called after throwing an instance of 'std::bad_alloc'`, exit 134. [Observed]
   - `session-prompt inventory`, which builds the inventory brief, with a FIFO marker: old completes in 9 ms; new **blocks** past
     30 s. With absent and valid markers, old and new write byte-identical inventory briefs. [Observed]
   - CLI `allow-execution` with a FIFO marker blocks at both commits. With a symlink to a valid marker, both refuse at stage
     `launched`. With a run path under a file, old refuses at stage `reverify` and new at stage `launched`. [Observed]
   - Library `allowExecution`, called directly with a valid launched marker: it **records a choice at both commits**. A brief
     issued afterwards with the arm switched on through the real `RUN_DIRECTORY_CHOICES` reader and a passing fixture probe is
     `permitting` at base and `sec-3` at the fix. [Observed]
   - Check-then-act window: CLI `allow-execution` with a `d9` port that writes the launched marker after the CLI has read it.
     The choice is recorded at both commits. The following arm-on brief is `permitting` at base and `sec-3` at the fix. [Observed]
6. **Reader sweep.**
   - Script: `sweep_readers.py`, run over `git ls-files` at HEAD.
   - Denominator: 2942 tracked files; 2938 read as UTF-8 and 4 skipped as binary.
   - Patterns: `launched\.json`, `RUN_LAYOUT\.launched\b`, the bracket form, `\bisLaunchedRun\b`, `\blaunchedMarkerState\b`,
     `\bLAUNCHED_FORMAT\b`, `polaris-dossier-launched/`, and `Object.(values|keys|entries)(RUN_LAYOUT)`.
   - [Observed] Non-test code that opens the marker exists only in `launched.ts`: line 38 reads it and line 64 writes it.
   - [Observed] The non-test callers of the reader, confirmed by a second sweep (`grep -F` for `launchFormRefusal`,
     `writeLaunchedMarker`, `expectedLaunch`, `SYZYGY_LAUNCHED`) are:
     - `cli.ts:365`;
     - `brief.ts:226`;
     - `inventory.ts:235` and `:436`;
     - `review.ts:664`;
     - `session-handover.ts:555`;
     - `launchFormRefusal` at `launched.ts:109`, which `inventory.ts:434` and `review.ts:662` call.
   - [Observed] `status.ts:66` lists `RUN_LAYOUT` names as known entries but never opens them. `polaris.ts:303` writes the marker.
   - [Observed] No code reference to `isLaunchedRun` remains at HEAD; the 6 remaining hits are in docs and decision records.
7. **The proposed fix in F1.** I applied it in the scratch clone and then reverted it.
   - [Observed] The seven subject test files pass, `Tests  217 passed (217)`, and `tsc -b` exits 0.
   - [Observed] Arm-off `brief` issues the base bytes for the FIFO, `/dev/zero`, `/dev/null`, symlink-to-valid, absent and valid
     markers.
   - [Observed] `allow-execution` refuses a FIFO marker at stage `launched` in 69 ms instead of blocking.

## 4. Findings

### F1 — blocking. Brief issuance and the inventory brief now block or abort on a marker that is not a regular file, with the arm off

- **Evidence.**
  - `launched.ts:40` only `lstat`s the name. `launched.ts:45` then calls `fs.readFileSync(file, 'utf8')`, which follows links,
    opens without `O_NONBLOCK` and reads without a size bound. [Observed]
  - The change adds two new eager reads on paths that never read the marker at base:
    - `brief.ts:226` evaluates `launchedMarkerState(run)` as an argument before `decideExecutionRule` is entered;
    - `inventory.ts:235` does the same for the inventory brief.
  - With the arm off, `decideExecutionRule` returns at `execution-rule.ts:94` (non-authoring role) or `:95` (arm off) without
    consulting `launched`. The read changes nothing about the rule, but it still runs. [Observed]
  - Probe results (§3, item 5): with a FIFO at `launched.json`, the shipped `brief` and `session-prompt inventory` complete at base
    and block indefinitely at the fix. With `launched.json` → `/dev/zero`, `brief` completes at base and aborts the process
    (`std::bad_alloc`, exit 134) at the fix. [Observed]
  - By code reading, the same applies to `syzygy dossier inventory-brief` (`cli.ts:339` → `inventory.ts:261`) and `startSessions`
    (`session-handover.ts:409`), which call `buildInventoryBrief`. [Inferred: not run]
- **Failure scenario.**
  - In an operator-started run, the run's state directory lies within the agent sessions' write reach (REQ-033, spec.md:25).
  - A session, or any process with that reach, creates `launched.json` as a FIFO or as a link to a character device.
  - `syzygy dossier brief`, `session-prompt … inventory`, `session-prompt … all` and `inventory-brief` then hang or crash with no
    reason and no exit code, where the shipped build used to issue the brief.
  - This permits nothing, so it is not a lenience. It does, however, change the shipped arm-off behavior at brief issuance, which
    acceptance criterion 3 forbids ("brief bytes are unchanged for every marker state"). It also turns a readable refusal into a
    silent hang or crash.
  - The same blocking read already existed at base at `allow-execution`, `launch-form` and the two of-record counters. This change
    carries it onto the two brief paths.
- **Proposed fix.** I verified it in the scratch clone (§3, item 7). Open the marker without following links and without blocking,
  then decide from the open descriptor:
  ```ts
  let fd: number;
  try { fd = fs.openSync(file, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK); }
  catch (error) { return (error as NodeJS.ErrnoException).code === 'ENOENT' ? 'absent' : 'unreadable'; }
  try {
    const stat = fs.fstatSync(fd);
    if (!stat.isFile() || stat.size > 4096) return 'unreadable';
    const marker = JSON.parse(fs.readFileSync(fd, 'utf8')) as unknown;
    return typeof marker === 'object' && marker !== null && (marker as Record<string, unknown>)['format'] === LAUNCHED_FORMAT ? 'launched' : 'unreadable';
  } catch { return 'unreadable'; } finally { fs.closeSync(fd); }
  ```
  - This also closes the gap between the `lstat` and the open.
  - It makes a symlink to a valid marker `unreadable` rather than `launched`. That only refuses more, because `writeLaunchedMarker`
    writes a regular file with flag `wx` and never a link. The PR should list it as a changed outcome.
  - Separately, either do not read the marker for the inventory brief at all (see N4), or make `ExecutionInputs.launched` a thunk
    that is read only after the arm check. Then the arm-off path cannot be affected by the marker's state.
  - Add FIFO and character-device fixtures to `launched.test.ts`, and an arm-off `brief` case with a FIFO marker. A fixture that
    opens with `O_NONBLOCK` will not hang the test runner.

### F2 — blocking (owner routing, not a code defect). Changed accept/refuse outcomes at gates the owner's row does not list

- **The listed change.** The owner listed "`isLaunchedRun` is read fail-closed, at both `allow-execution` and brief issuance"
  (line 93), followed by "Any change not listed here to what a gate accepts or refuses stops and returns to the owner" (lines
  95-96).
- **The author's position, tested.** The author's position is that the listed change is the reader, so every caller inherits it,
  and every changed outcome refuses more.
  - [Observed] The monotonic half is true:
    - every input the base reader treated as launched is still `launched`;
    - `absent` behaves as base at every probe;
    - every input that moved from "not launched" to `unreadable` is refused at every reader;
    - no change permits more (§3, item 3).
  - The scope half does not follow from the record.
- **Changed outcomes at the listed sites.** [Observed: differential and probes]
  - `allow-execution` (CLI, `cli.ts:365-371`): for the 12 unreadable variants, a recorded choice (exit 0) becomes a refusal at
    stage `launched` (exit 1) with no record.
  - `allow-execution`, already refused: for an ENOTDIR or EACCES run path, the refusal moves from stage `reverify` to stage
    `launched`, with a new reason.
  - Brief issuance with the arm on: for the 2 launched and 12 unreadable variants, `permitting` becomes `sec-3` with a new
    `notPermittedBecause` reason. With the arm off, the bytes are unchanged for the 15 recorded variants (except F1).
- **Changed outcomes at sites not listed.** [Observed]
  - `launch-form` (`session-handover.ts:555-557`): for the 12 unreadable variants, a recorded terminal launch-form record becomes
    a refusal at stage `form` with a new reason.
  - `launchFormRefusal` (`launched.ts:108-117`): in an unreadable-marker run, a declared `terminal` or `bang` form that was
    accepted is now refused. Through it, `inventoryOfRecord` (`inventory.ts:434-436`) and the review of record
    (`review.ts:662-664`, reached via the inventory) go from counting to not counting. Their refusal sentences change too: "is not
    a terminal or bang launch" becomes "is not a countable launch (the run's launched marker is present but unreadable, so none
    counts)".
  - This holds whenever a marker that was a regular file at hand-over is corrupted later (`inventory.test.ts:449-458`,
    `review.test.ts:476-485`).
- **Why this goes back to the owner.** The approval rested on a factual premise that was false at the commit it cites.
  - The bead says "[Observed at eba011df] … Only cli.ts:365 (allow-execution) reads it".
  - The packet review that fed the owner's question says "`isLaunchedRun` is fail-open (`launched.ts:31-37`) and only
    `allow-execution` checks it (`cli.ts:365`)" (`docs/reviews/R-GREENFIELD-PARITY-PACKET-2-RAW.md:127`).
  - The same review says "[Inferred] … the fix changes no output and can land now under GP-Q0, at both sites"
    (`R-GREENFIELD-PARITY-PACKET-2-RAW.md:134`).
  - [Observed: `git grep -n -F isLaunchedRun eba011df -- packages`, and the same at `29e036f4`] Both commits have five non-test
    call sites: `cli.ts:365`, `inventory.ts:436`, `launched.ts:90` (inside `launchFormRefusal`), `review.ts:664` and
    `session-handover.ts:555`.
  - So the owner approved the change believing the reader had one caller and that no other gate would move. The two sites the row
    names are exactly the sites in that premise.
  - The changes at `launch-form` and the two of-record counters are changes "to what a gate accepts or refuses" that the row does
    not list. The owner's rule says they stop and return to the owner, whatever their direction.
- **Proposed resolution.**
  - Put one question to the owner, with this enumeration. My recommended answer is to confirm that the row covers every reader of
    the marker. The changed outcomes follow REQ-033 and SEC-3's "never gives the instruction to a session it started", and point
    the same way as candidate REQ-041. They only refuse more. Keeping a fail-open reader at the counters would let a corrupted
    marker in a launched run count a declared `terminal` form, which REQ-041 as drafted forbids.
  - The alternative is to narrow the code so that `launch-form` and `launchFormRefusal` keep the base mapping, with `unreadable`
    read as `absent`. I do not recommend it. It keeps a fail-open reader at two gates.
  - Either way, the PR must list every changed refusal (bead acceptance criterion 3), including F1's symlink consequence if that
    fix lands.

### Notes (non-blocking)

- **N1 — the library `allowExecution` takes a choice in a launched run.**
  - [Observed] `allowExecution` (`execution-choice.ts:84-133`) has no marker check and is exported (`index.ts:68`). Only the CLI
    wrapper (`cli.ts:365-371`) refuses.
  - A direct library call recorded a choice in a run with a valid launched marker at both commits (§3, item 5). That is candidate
    REQ-044's falsifier "An execution choice is recorded for a launched run".
  - The fix's new check at brief issuance keeps that choice from ever producing a permitting brief when the arm is on [Observed],
    so the exposure is now limited to a stray record.
  - Proposed: move the marker check into `allowExecution` and add `launched` to `AllowExecutionStage`. Doing so would add the
    `disclosures` field to the CLI's `launched` refusal JSON, which today lacks it, unlike every other `allow-execution` refusal.
    That is itself an output change, so it is better carried with the F2 question than slipped in.
- **N2 — check-then-act at `allow-execution`.**
  - [Observed] The CLI reads the marker (`cli.ts:365`) before the awaited reverify and D9 checks and the `wx` write
    (`execution-choice.ts:125`). A marker written in that window leaves a recorded choice beside it, at both commits.
  - The brief-issuance check closes the consequence: the arm-on brief is `sec-3` at the fix and was `permitting` at base. No fix
    is needed. It should be named in the PR as the reason the brief-site check is load-bearing.
- **N3 — trust on absence remains, as designed.**
  - [Inferred] Deleting `launched.json` makes a launched run read as operator-started at every reader. The bead fixes that `absent`
    means not launched, so this is in scope by design.
  - The supervisor's own state record under the state root (`polaris.ts:92-98`, `readState`) and the `syzygy-launched` launch
    records could corroborate it. That would be a new accept/refuse change and needs the owner.
  - Out of scope: `polaris --resume` does not check for a recorded execution choice (`polaris.ts:92-98`), which candidate REQ-044
    line 208 would require. Both belong in the `syzygy-bpyt.1.6` flip packet.
- **N4 — the marker read for the inventory brief is dead input.**
  - [Observed] Mutant R1 survived because the role `inventory` returns at `execution-rule.ts:94` before `launched` is read.
  - The read at `inventory.ts:235` therefore contributes only F1's exposure. Drop it, or pass the value lazily.
- **N5 — `review.ts:664` wording is untested.**
  - [Observed] Mutant R2 survived. The record's `notCovered` discloses that the sentence is not reachable through the public path,
    because the inventory stops counting first.
  - That is accurate at this commit. The sentence becomes reachable only if the marker changes between the two reads.
- **N6 — test fixture independence.**
  - [Observed] Expected values in every new test are literal strings. None is imported from the module under test, including the
    arm-off reason at `brief.test.ts:230`.
  - Every "valid marker" fixture is produced by `writeLaunchedMarker`, the module's own writer. A literal JSON fixture for one
    valid case would catch a reader and writer that drift together.
  - The byte-order-mark fixture (`launched.test.ts:28`) holds a raw U+FEFF. AGENTS.md advises a `﻿` escape where exact bytes
    matter.
- **N7 — removing the `isLaunchedRun` export.**
  - [Observed] `index.ts:104` drops `isLaunchedRun` from the package index, and no code reference remains (§3, item 6). The package
    is `"private": true`.
  - [Inferred] This is not a class-6 endpoint removal.
- **N8 — process items outside the frozen subject.** [Unknown]
  - the PR's CC-REV-1 class statement;
  - its list of changed refusals (bead acceptance criterion 3);
  - GP-Q0's non-blocking owner notice in the cycle report (`syzygy-bpyt.10`).
- **N9 — the "altered prose" corpus.**
  - [Observed] GP-Q0's differential asks for records with altered prose. Its one altered-field variant is "launched format, another
    runId".
  - [Inferred] Because the reader compares only `format`, any other prose alteration with the right format reads as `launched`,
    the strict side. So the omission is not material.

## 5. Verdict per acceptance criterion

1. **An absent marker is unchanged from the base.** **Pass.** [Observed] The `absent` row is identical at all five differential
   probes. The arm-off `brief`, CLI `allow-execution` and `session-prompt inventory` probes are also identical. A missing run
   directory reads as `absent`, as base did.
2. **A present marker that is not Syzygy's is never more lenient than a launched run, at every reader.** **Pass, with F1's
   liveness caveat.** [Observed] Every one of these states is refused at `allow-execution` with no record, gives SEC-3's rule at
   arm-on brief issuance, records no declared form at `launch-form`, and stops the of-record counters:
   - the 12 recorded states;
   - a symlink loop, a link to `/dev/null`, a `__proto__`-shaped object, non-UTF-8 bytes, an ENOTDIR run path and a mode-000 run
     directory.

   A symlink to a valid marker reads as `launched`, identical to launched. A FIFO permits nothing at any reader, but it refuses
   nothing either: every reader blocks.
3. **With the arm off, brief bytes are unchanged for every marker state.** **Fail** (F1). [Observed] Bytes are identical for the
   15 recorded states and for a symlink to a valid marker, a link to `/dev/null`, and an absent or valid marker. A FIFO marker
   blocks `brief` and `session-prompt inventory`, and a character-device link aborts `brief`. Base issued both briefs.
4. **The differential and mutants are re-runnable and reproduce.** **Pass.** [Observed] The differential has 0 mismatches over 75
   comparisons. All 12 mutants reproduce their `Tests` lines and exit codes exactly. Each mutant record carries `old`, `new`, the
   commit and the subject digests.
5. **Scope.** **Finding F2.** Every changed outcome only refuses more, but the outcomes changed at `launch-form` and the two
   of-record counters are outside the two sites the owner's row lists. The row's premise was that the reader had a single caller,
   which was false. Under lines 95-96 this returns to the owner.

## 6. Test quality

- [Observed] The new tests assert exact refusal objects with `toEqual`. They assert that no record is written
  (`execution-choice.json`, `inventory/session-1.launch.json`). They assert exact `notPermittedBecause` arrays, so with the
  fixture choice otherwise valid, the marker reason is the only reason.
- [Observed] The reader's unit tests cover 12 present-but-not-the-marker states. Every new predicate had a recorded mutant, and
  each was killed; my R3 and R4 extras were also killed.
- Gaps:
  - there is no FIFO or device fixture (F1);
  - the inventory-brief read is dead input (N4);
  - `review.ts:664` wording is unreachable through the public path (N5);
  - the valid-marker fixtures come from the module's own writer (N6).
- [Observed] The mode-000 fixture assumes a non-root runner. `.github/workflows/node-ci.yml` runs on `ubuntu-latest` and uses
  `sudo` for installs, so tests run as a non-root user [Inferred]. Five other test files in the repository use the same pattern.

## 7. Summary of what must change before merge

1. **F1:** make `launchedMarkerState` non-blocking, no-follow, regular-file-only and size-bounded, or keep the arm-off paths from
   reading the marker. Add FIFO and device fixtures, and list the symlink consequence.
2. **F2:** obtain the owner's ruling on the changed outcomes at `launch-form` and the inventory and review of-record counters,
   using the enumeration in F2. The recommendation is to confirm. List every changed refusal in the PR.

Any repair retires this review (rule 10). The repaired head needs a fresh CC-REV-1 review.

## 8. Scope of this review

- [Observed] Read:
  - the diff;
  - `launched.ts`, `execution-rule.ts`, `execution-choice.ts`, and the relevant ranges of `cli.ts`, `session-handover.ts`,
    `inventory.ts`, `polaris.ts` and `status.ts`;
  - the governing clauses quoted in §2;
  - the bead;
  - the packet raws named in F2.
- Not inspected:
  - live launched runs under `syzygy polaris`, and whether a launched session's view really holds the run directory read-only (the
    `launched.ts:9-13` comment says it does) [Unknown];
  - the PROJECT-STATUS battery, which this brief did not ask for.

## 9. Cleanup

- [Observed] The scratch clone, its base worktree and every probe run directory are deleted.
- [Observed] The worktree is unchanged: `git status --short` is empty and HEAD is `1e153a0d20ae55ed8a6bb1c129b010766f9c8f88`.
- Retained under `lead/b88/reviewer/`:
  - harnesses: `sweep_readers.py`, `check_subject_digests.py`, `compare_differential.py`, `run_mutants.py`, `run_probes.py`,
    `probe-marker.mjs`, `run_handover.py`, `probe-handover.mjs` and `apply_proposed_fix.py`;
  - the extracted harness: `extracted/zz-b88-differential.test.ts`;
  - outputs: `regen.diff`, `full-run-1.log`, `diff-old.json`, `diff-new.json`, `mutants-rerun.json`, `mutants-rerun.log`,
    `probes-old.json`, `probes-new.json`, `probes-proposed.json` and `probes-handover.json`.
