# Review — PR 408 pre-started waiting dossier sessions, round 2
Verdict: REVISE
Reviewed commit: c3709a3a151dbe4664671a120455f1ce7a062ed3
Reviewer: fresh-context

## Scope and method

- Subject: PR #408 at `c3709a3a151dbe4664671a120455f1ce7a062ed3`. The round-1 subject was `c4fc9b36`, and the repairs are 6 commits, `4f668cf9..c3709a3a`. Together they change 16 files. Over the merge-base `72ed0a59`, the whole PR touches 25 files: 14 added and 11 modified.
- Inputs read:
  - the round-1 raw, which is byte-identical to the reviewer's scratchpad copy (`git diff --no-index`, empty);
  - P-107 in the owner-selection record;
  - the direction record;
  - the v1.2 package diffs (`spec.md.patch`, `design.md.patch`, `SEMANTIC-DELTA.md`);
  - `waiting-sessions.ts`, the repair diffs of `session-handover.ts`, `render.ts` and `cli.ts`, and the new tests;
  - the mutant record;
  - `record_versioned_signoff.py` (`render_record`, `parse_head`).
- Probes:
  - Ran in a scratch worktree at the subject commit, after `npm ci` and `npm run build` (exit 0), with TMPDIR inside the scratchpad.
  - The PR's own suite: `waiting-sessions.test.ts` ran 101 tests, all passing.
  - Probe file `probe408r2.test.ts`: 9 probes (P1–P9). It reuses lines 1–121 of the PR's own CLI harness.
  - 7 recorded mutants were re-applied.
  - The probe file was removed, and the worktree and clone were deleted.
  - The main checkout's `git status --short` was unchanged: the same 3 pre-existing untracked entries.
- Sign-off rehearsal: a local `git clone` of this repository, checked out at the subject commit, with a synthetic raw.

## A. Round-1 findings at this head

| Finding | Status | Evidence |
|---|---|---|
| F1, symlinked session directory | **Closed for its own input; not closed for the class.** See Finding 1. | [Observed, P1] With `session-1` replaced by a link to a directory outside the state root, `await --submit inventory.json --stdin` exits 1 at stage `directory`, and `elsewhere/inventory.json` does not exist. Tests at lines 696–767 cover both await and delivery. |
| F2, design continuity | Closed | [Observed, P9] A first-round design verdict now renders, in the review-status region: "…is the review session's. No earlier packet was delivered to this review session, and no earlier verdict declares its session identifier. (Inferred, from …)". Tests at lines 666 and 678 cover first-round and continuing. Mutants F2a and F2b were re-applied and killed. |
| F3, unquoted heredoc | Closed | [Observed] Every printed hand-over goes through `stdinHandOver`, which emits `<<'SYZYGY_EOF'` and "With the delimiter quoted the shell never expands the body, so nothing in it runs". This includes both waiting prompts, the inventory and review `delivered` next-steps, and both repair next-steps. The same sentence is now a SHALL in the spec patch, with a falsifier arm. Mutant F3a was re-applied and killed, with 4 failing tests. [Inferred] A valid JSON body cannot contain a line that is exactly `SYZYGY_EOF`, because JSON escapes newlines inside strings. So the fixed delimiter cannot end the heredoc early on compliant input. |
| F4, mutant count | Closed | [Observed] The record now holds 112 mutants (112 killed) and 15 `notMutated` entries. The 4 survivors I named in round 1 are now F4a–F4d, all killed. See criterion C8. |
| F5, garbage submit | Closed as raised | [Observed, P4] An `inventory.json` passed its check (705 bytes). Submitting `garbage` then exits 1 at stage `submit` ("…nothing is written, and inventory.json stays as it was"), and the file is byte-identical. See Finding 3 for well-formed JSON that fails the schema. |
| F6, other permission layers | Closed (narrowed and disclosed) | [Observed, P8] The printed command carries `--disallowedTools Edit Write NotebookEdit WebFetch WebSearch Task Agent --strict-mcp-config`. The residual from the user, project and local settings layers is now in START_DISCLOSURES and in the spec's Inferred list. |
| F7, slice versus tool timeout | Closed | [Observed] Both waiting prompts carry `WAIT_TIMEOUT_ADVICE` ("…600000 milliseconds in Claude Code): one call waits up to 9 minutes"). `DEFAULT_WAIT_MINUTES` is still 9, and `sliceEnds` is measured from `startedAt`, so the slice is bounded inside the 10-minute tool limit. |
| F8, gate opens on filename | Closed as raised | [Observed, gate probe] A file whose content is only `x` opens nothing. See criterion B3 and Finding 4. |
| F9, subagents and redirection | Closed (disclosed) | [Observed] `Task` and `Agent` are denied. The spec patch now lists the subagent path as Inferred and redirection as Unknown, and START_DISCLOSURES says the same. |
| N1 | Closed | Direction item 4 now reads "The drafter reads this to mean … [Inferred: the drafter's reading of the selected words; the owner saw the option, not this mechanism]". |
| N2 | Closed | [Observed, P8] `bang` is `null` for all 3 waiting sessions, with a note explaining why. |
| N3 | Closed | Covered under F9. |
| N4 | Closed | The falsifier now reads "…in that session's directory; a printed instruction passes … ; a broader pre-approval is printed…". The stray "or" is gone. |
| N5 | Closed | `SEMANTIC-DELTA.md` lists the header-line move and the proposal's version line. |

## B. Regressions

1. **Printed flags exist.**
   - [Observed] `claude --help` (2.1.295) lists `--allowedTools <tools...>`, `--disallowedTools <tools...>` and `--strict-mcp-config`.
   - `--permission-mode`'s listed choices are acceptEdits, auto, bypassPermissions, manual, dontAsk and plan, so `default` is not listed. However, `claude --permission-mode default --version` exits 0, while `--permission-mode bogusmode` exits 1 with "argument 'bogusmode' is invalid". So `default` is accepted as an unlisted alias.
   - The full printed flag set parses: `claude --permission-mode default --allowedTools 'Read(//tmp/x/**)' 'Bash(syzygy dossier await /tmp/x/:*)' --disallowedTools Edit Write NotebookEdit WebFetch WebSearch Task Agent --strict-mcp-config --version` printed the version and exited 0.
2. **Quoted-heredoc wording.** Correct and pinned (see F3).
   - The prompt is shell-quoted by `shellQuote` (`'\''` escaping). The literal test at line 265 pins the whole terminal string, quoting included.
3. **Sign-off predicate.**
   - [Observed] In the scratch clone, `record_versioned_signoff.py --record polaris-dossier-local-agent-mode --version 1.2` ran with a synthetic CONFIRM raw whose head digest is the v1.2 subject digest. That digest is `4c4ea2a7…`, re-derived by script through `subject_bytes`. The recorder applied the patches, wrote the record and appended the block. `waitModeSignedIn(clone)` returned `true`, and on the PR tree it returned `false`.
   - Forged and partial variants, 10 in all, built from the real record:

     | Variant | Gate opens |
     |---|---|
     | copy of the real record and aggregate | true |
     | record only, no aggregate | false |
     | aggregate with the block removed | false |
     | block only, no record | false |
     | record content `x` | false |
     | verdict changed to REVISE | false |
     | record truncated to its title | false |
     | short commit | false |
     | Tag line removed | false |
     | **hand-forged 6-line head and bare markers, no review and no applied patch** | **true** (see Finding 4) |
4. **Timeout and slice.** No regression. The slice length did not change; only advice was added. [Inferred] `--wait-minutes` up to 60 is still accepted, and the advice "one call waits up to 9 minutes" holds only for the default. This is harmless: the tool times out and the session runs await again.
5. **Design continuity on unsigned (v1.1) runs.** [Observed by reading `render.ts:556`]
   - The continuity sentence is now emitted for every counted design verdict, including runs where wait mode never ran.
   - The fidelity arm already did this at round 1, so this is a consistent extension and not a new class.

## C. Round-1 criteria

1. **Direction record: met.** [Observed]
   - The question, the selected label and description, and the 3 options not selected match P-107 of the owner-selection record. Checked by script; the blockquote prefixes were read by eye.
   - The instant 2026-10-08T16:24:26.838Z is at lines 3 and 19.
   - The record contains "Nothing unattended" and "the product still coordinates no agents".
   - The repair changed only item 4's labelling (N1).
2. **Allow-list: met.**
   - [Observed, P8 and the test at line 259] Denominator: 3 sessions, 7 rules.
     - Inventory: `Read(/<clone>/**)`, `Read(/<inv>/**)` and `Bash(syzygy dossier await <inv>/:*)`.
     - Fidelity and design: `Read(/<dir>/**)` and `Bash(syzygy dossier await <dir>/:*)` each.
     - 0 Edit, Write, WebFetch or other Bash rules.
   - Codex gets `null` for all 3 sessions.
   - See Finding 5 for tools outside the printed lists.
3. **Submit path: partly met.**
   - Bounded: `readStdinBytes` stops past `DRAFT_MAX_BYTES`, and `parseBoundedJson` has maxNodes 500,000 and maxDepth 16.
   - Validates syntax before the write (P4).
   - Link-safe for the session directory, but not for the sessions root (Finding 1).
4. **Continuity: met** for fidelity (tests at 577–640) and design (P9 and tests at 666/678).
5. **Tool and class gates: met.** [Observed, P5]
   - `session-prompt all --tool codex` with only a claude-code statement is refused at stage `statement`.
   - A delivery with `--tool codex` is refused at stage `context`.
   - `--fresh --tool codex` is refused at stage `statement`.
   - With a withdrawn statement, the delivery and a later `await` are both refused at stage `reverify`.
   - `fidelity-1` stayed empty.
   - The class gate is still inside `buildFidelityPacket`, which `deliverReview` calls (`session-handover.ts:480`).
6. **Gate and rehearsal: met.** [Observed]
   - Unsigned (P6): `await --submit --stdin` and the delivery each refuse at stage `unsigned`. The inventory is unchanged and no `round-1` is created. `--fresh` falls back to the v1.1 hand-over and issues session 2.
   - Rehearsal checks after recording:
     - `--check` passed for 1.2 ("regenerates exactly; applied tree verified") and for 1.1 ("superseded by a later version");
     - the v1.2 builder's `--check` passed ("verifies (applied)");
     - the v1.2 `--selftest` reported "39 fixtures, 0 failing";
     - `check_governance.py` reported "32 OK, 21 WARN, 0 FAIL (53 checks)";
     - `openspec validate polaris-dossier-local-agent-mode --strict` returned "Change 'polaris-dossier-local-agent-mode' is valid". This closes round 1's Unknown.
7. **Spec delta: met.**
   - It adds one SHALL (the shell expands nothing), one falsifier arm, two Inferred items and one Unknown. All of them are inside REQ-polaris-generation-035, the only affected identifier, and each is stated in `SEMANTIC-DELTA.md`.
   - Each one narrows or discloses; none widens what option B authorized.
8. **Mutant record: met, with notes.** [Observed]
   - Every one of the 112 mutants carries `old`, `new` and `commit`, and every `old` occurs exactly once in its file at its commit. Script: 0 problems over 112.
   - All 18 subject digests (3 commits × 5 files, plus 3 builder subjects at `8c054a73`) re-derive from `git show`. The 4 code subjects at each commit equal the head bytes.
   - All 21 builder mutants carry old and new.
   - Spot-check: I re-applied 7 mutants on the head tree (F1d, F2a, F5b, F8e, F3a, F4c and F6b). All 7 were killed, and each failing-test count matched the record (1, 1, 2, 1, 4, 1, 1). The file was restored byte for byte.
   - F4n is "killed (timeout)" and the record says so.
   - Of the 15 `notMutated` entries, 13 give a real reason: unreachable, subsumed, equivalent, race-only, fault-injection-only, or forwarding. Two do not; see Finding 6.
9. **Bound bytes and placement: met.** [Observed]
   - The repairs add 1 file under `docs/reviews/` (the round-1 raw, byte-identical) and edit no other `-RAW.md`.
   - There are 0 code files under `openspec/**` or `.syzygy/**` (whole-PR name-status, 25 files).
   - The direction record is a plain direction and binds no digest.
   - A case-folded sweep of the 5 new governance files for "accepted|adopted|in force|is signed off|binds now|now binds" found 9 hits. All of them are historical ("SEC-3 and D9 as adopted", "craft acts 6 and 7 in force") or conditional ("may merge only once version 1.2 is signed off", "Version 1.1 stays in force").

## D. `session-prompt review` without `--kind`

[Observed, P7] At this head it does not fall through to a fresh session.

- With a fidelity session waiting, `session-prompt <run> review` exits 1, `outcome: refused`, `stage: role`, with the reason "a review session takes --kind fidelity or --kind design".
- `review --fresh` with no `--kind` is refused the same way.
- No `fidelity-2` is made and `fidelity-1` stays empty.
- Path: `handOver` (`session-handover.ts:446`) skips delivery because `isReviewKind(undefined)` is false. `sessionPrompt` then refuses at line 172 before any write.

The lane's observation does not reproduce, so there is no v1.2 violation. [Inferred] Even a fall-through would hand over a new session, which v1.2 permits as an option ("add --fresh"), not a delivery outside the rules.

## Findings

**Finding 1 — The F1 repair pins the session directory but trusts the sessions root: a linked `<run>.sessions` still sends await's and delivery's writes outside the state root** (revise)
- Where:
  - `packages/polaris-dossier/src/waiting-sessions.ts:115-116`: `realRoot = fs.realpathSync(root)` … `if (real !== path.join(realRoot, path.basename(directory)))`;
  - callers at `:180` (`deliverToWaiting`) and `:401` (`awaitSession`, with `root` = `parent`).
- Clause:
  - v1.2 REQ-polaris-generation-035: "Syzygy writes the content into the session's directory under the role's own file name …, and only there".
  - The design patch (`design.md.patch:53`): "Syzygy writes into a session directory, or delivers to one, only when it is a directory of its own whose real path lies in the sessions root".
  - The function's own doc comment (`:109`): "so no write Syzygy makes for a session lands outside the root".
- Failing input [Observed]:
  - **P2 (await).**
    1. Run `session-prompt <run> all` and pass a draft.
    2. Move `<run>.sessions` to `<tmp>/p2-root-elsewhere`, a sibling of the state root, and leave a symlink at `<run>.sessions`.
    3. Run `await <run>.sessions/session-1/ --submit inventory.json --stdin` with a valid inventory.
    - Result: exit 0, `outcome: submitted`, `passed: true`, and `<tmp>/p2-root-elsewhere/session-1/inventory.json` exists.
  - **P3 (delivery).** The same link after `readyForReview`, then `session-prompt <run> review --kind fidelity`.
    - Result: exit 0, `outcome: delivered`, and `<tmp>/p3-root-elsewhere/fidelity-1/round-1/packet.json` was written. That is the screened target text, outside the state root.
- Cause:
  - Both the root and the entry are resolved, so a linked root moves both together and the comparison still holds.
  - `sessionsRootViolation` runs only at `session-prompt all`, and it only rejects a root inside the clone.
- This is F1's threat (any writer in the state root plants a link), one path component up.
- [Observed by reading] A linked `<run>` does not redirect these writes: `.sessions` stays a real sibling, so the leaf check holds.
- Repair:
  - also require `lstat(root).isDirectory()` (not a link), and `realpath(root) === path.join(realpath(path.dirname(root)), path.basename(root))`, in `sessionDirectoryRefusal`;
  - add a test and a mutant for each check.

**Finding 2 — `launch-form` still records `bang` for a waiting session that is printed no bang form** (note)
- Where: `session-handover.ts:531` accepts `terminal|bang` for every session. `startSessions`' `next` (`:429`) now names only `terminal`, and N2's note says "No bang form is printed for a waiting session".
- Failing input [Inferred from the code path; not run]: `launch-form <run> review bang --kind fidelity` after `session-prompt all` records `bang` for a waiting session.
- This violates no clause: v1.1 lets the operator declare either form, and the operator may type `!` themselves. It does, however, leave a run record that contradicts the printed advice.
- Consider refusing `bang` for a session whose prompt record has `mode: waiting`, or disclosing it.

**Finding 3 — Well-formed JSON that fails the schema still replaces a passing `inventory.json`** (note)
- Where: `waiting-sessions.ts:353`. Only `parseBoundedJson` runs before the rename. `checkInventory` and `reviewCheck` run after.
- Failing input [Observed, P4b]: after a passing inventory, submit `{}`. Result: exit 1, `outcome: submitted`, `passed: false`, and the file now reads `{}`.
- Clause: the spec orders "writes … and checks it", so this is conformant. The repair's comment "a bad submission never replaces the file there" (`:331`) holds for syntax only.
- Effect: as in round 1, the check of record is the frozen copy. [Inferred] The counted inventory is unaffected.
- Suggestion: narrow the comment's wording.

**Finding 4 — The wait-mode gate is a format check, not provenance: a hand-written six-line head plus two bare markers opens it** (note)
- Where: `waiting-sessions.ts` `signoffRecordHolds`, at line 79 and the lines after it.
- Failing input [Observed, gate probe]: in `decisions/`, write a record with the title, `Package:`, `Version: 1.2`, `Tag:`, `Reviewed commit: ` followed by 40 zeros, and `Review verdict: CONFIRM`. Then put an aggregate holding only the two v1.2 markers. `waitModeSignedIn` returns `true`, with no raw, no applied patch and no `--check`.
- The PR discloses this: RECORDS_WITHIN_REACH says the records "lie in Syzygy's checkout, which the agent sessions can write". The predicate now rejects every accidental or partial state I tried (9 of 9).
- Note-level, as in round 1. A stronger gate would require the applied v1.2 subject digest, which is cheap: the builder's `applied` state.

**Finding 5 — The deny list is a fixed set of seven names; other tools that need no approval are neither denied nor named** (note)
- Where: `session-handover.ts:57`, `WAITING_DENIED_TOOLS`.
- [Unknown] Whether the operator's Claude Code exposes other tools that run without approval in the default mode, and that can egress or write. Examples are the `Skill` tool, or a claude.ai-connected `Artifact` publish where enabled. Whether `--strict-mcp-config` excludes claude.ai-account connectors is also Unknown.
- The disclosure names only settings-layer allow rules, subagents and redirection.
- Suggestion: name "tools the agent tool runs without approval, other than those denied" in the Inferred list, or print `--tools Read,Glob,Grep,Bash` (`claude --help`: "Specify the list of available tools from the built-in set"), which narrows by allow-list rather than deny-list.

**Finding 6 — Two `notMutated` entries carry no reason that excuses the mutant** (note)
- Where: `docs/evidence/polaris-dossier-waiting-sessions-mutants-2026-10-09.json`, `notMutated[7]` and `notMutated[14]`.
- `notMutated[7]` reads: "Exercised, not mutated: … A mutant rethrowing instead would change that reason, but none was run". That states that the mutant was not run, not why it need not be.
- `notMutated[14]` reads: "Usage errors (exit 2) … are not mutated in this record". That is a scope choice, not a reason.
- Clause: AGENTS.md rule 6, and the record's own scope sentence: "Each predicate has one mutant below, or one entry in `notMutated` with its reason."
- Suggestion: run the rethrow mutant for [7]. For [14], either mutate the two `--stdin`/`--fresh`-twice checks or restate them as out of scope in the record's scope sentence.
