# Review — PR 408 pre-started waiting dossier sessions
Verdict: REVISE
Reviewed commit: c4fc9b3687b48e7d553ee9ddb8d018467a6ba2a1
Reviewer: fresh-context

## Scope and method

- Subject: PR #408 at `c4fc9b3687b48e7d553ee9ddb8d018467a6ba2a1`. The merge-base with `origin/main` is `72ed0a596d34ff5795a55d80e5d3f439a919ebcc`. The diff touches 22 files: 10 modified and 12 added.
- Inputs read:
  - the owner-selection record (section P-107);
  - `DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`, decision 3;
  - the direction record;
  - the v1.2 package (`spec.md.patch`, `design.md.patch`, `SEMANTIC-DELTA.md`);
  - `waiting-sessions.ts`, the `session-handover.ts`, `cli.ts` and `render.ts` diffs, and `review.ts` `reviewCheck`;
  - the mutant evidence record;
  - the diffs of `record_versioned_signoff.py` and the v1.1 builder.
- Probes ran in a scratch worktree at the subject commit, after `npm ci`, `build:poc` and a full `npm run build` (both exit 0). TMPDIR was set inside the scratchpad.
  - I added a probe file (`probe408.test.ts`, 8 probes) that reuses the PR's own CLI harness. All probes ran.
  - Four extra mutants were applied and then restored. `git status` was clean apart from the probe file. The worktree was then removed.
- The sign-off rehearsal ran in a separate scratch clone with a synthetic raw. The main checkout's `git status --short` was unchanged after the run: the same three pre-existing untracked entries.

## Criteria results

1. **Direction record: met.** [Observed]
   - The question, the selected label and description, and the three options not selected match the owner-selection record word for word.
   - The instant is 2026-10-08T16:24:26.838Z. The record says "The owner selected the option; the owner did not type that phrase."
   - It quotes item 2 of the 2026-10-03 direction ("It changes nothing about what Syzygy the product may do: the product still coordinates no agents."). `git grep -F` found that text at line 35 of the cited direction.
   - It keeps "Nothing unattended that executes observed code".
   - It authorizes only option B with the continuing reviewer.
   - See note N1 on one interpretive sentence.
2. **Allow-list: met as printed.** The paths found are in F3, N2 and N3. [Observed]
   - Denominator: 3 sessions. Claude Code prints 7 rules: 4 `Read(//…/**)` (the clone and the inventory directory for the inventory session, plus each review directory) and 3 `Bash(syzygy dossier await <dir>/:*)`. There are 0 Edit, Write, WebFetch or other Bash rules.
   - Codex prints `null` for all 3 sessions and says so. The literal-list test passed at the subject commit.
   - Process and network sweep: 32 non-test modules under `packages/polaris-dossier/src`, matched against `fetch(|https?.request|node:net|node:http|child_process|spawn(|execFile`. 0 hits; every hit was in a `*.test.ts` or the testkit.
3. **Submit path: partly met.** Size bound, empty input, wrong-role names, undelivered rounds, a round directory linked to another session (probe P2) and a link at `round-1/verdict.json` (P3, the link's target was untouched) are all refused or handled safely. [Observed]
   - The session directory itself is not link-safe. See F1.
   - Content is written before any validation. See F5.
4. **Continuing reviewer: met for fidelity, not for design.** See F2.
   - Independence: a reviewer receives only the packet, the fixed prompt and `await`'s own messages. [Observed]
5. **Tool and class gates: met.** All probes in P6 [Observed]:
   - `session-prompt all --tool codex` without a codex statement is refused at stage `statement`.
   - A delivery with `--tool codex` is refused at stage `context`.
   - `--fresh --tool codex` is refused at stage `statement`.
   - A withdrawn statement refuses a delivery (`reverify`), and a later `await` is also refused (`reverify`).
   - The class gate stays inside `buildFidelityPacket` (`review.ts:202`), which the delivery calls.
6. **Gate and rehearsal: met.** [Observed]
   - Unsigned (P7): `await --submit --stdin` and the delivery each refuse at stage `unsigned`. `round-1` is not created. `--fresh` falls back to the signed v1.1 hand-over, as intended.
   - In the scratch clone, `record_versioned_signoff.py --record polaris-dossier-local-agent-mode --version 1.2` with a synthetic CONFIRM raw applied the patches. `PROJECT-STATUS.md` then read 36 requirements and 248 scenarios.
   - After recording:
     - `--check` passed for 1.2, 1.1 and 1.0;
     - all three builders' `--check` passed;
     - the v1.2 `--selftest` reported 39 fixtures, 0 failing;
     - `check_governance.py` reported 32 OK, 21 WARN, 0 FAIL;
     - `waitModeSignedIn(clone)` returned true, and false on the PR tree.
   - `check_spec_reconciliation.py --check` failed R3 (census), R4 (`GOVERNING-DEPENDENCIES.md`) and R5 (`openspec/README.md` row). These are the install-time steps the PR's checklist names.
   - `openspec validate --strict` on the applied tree was not re-run. [Unknown]
7. **Spec delta: well formed, with two notes.** The affected identifier (REQ-polaris-generation-035) is stated, and the patch changes only that requirement plus the version header line. See N5.
8. **Mutant records: partly met.**
   - Each of the 50 code mutants and 21 builder mutants carries `old` and `new`. Three have `new` empty, which is a deletion.
   - The code record pins commit `cfdd1a40`, with subject digests. All 8 subject digests in the two records match the bytes at the subject commit. [Observed]
   - The count of unmutated predicates and one justification are wrong. See F4.
9. **Bound bytes and placement: met.** [Observed]
   - Over 2,637 tracked files at the merge-base, no performed act's manifest or record cites the base digest (full or 16-hex prefix) of any of the 10 modified files. The only citers are three mutation-evidence records under `docs/evidence/`, which are provenance and not acts.
   - 0 `-RAW.md` files are touched.
   - 0 `.ts`, `.js`, `.py` or `.mjs` files are under `openspec/**` or `.syzygy/**`.
   - Nothing is labelled accepted. A case-folded sweep of the new governance files for "accepted", "adopted", "in force" and "signed off" found only historical or conditional uses.

## Findings

**Finding 1 — A symlinked session directory sends Syzygy's writes outside the sessions root** (revise)
- Where:
  - `packages/polaris-dossier/src/waiting-sessions.ts:354`: `const realDir = realOrNull(directory);`
  - `:288`: `target = path.join(realDir, INVENTORY_SUBMIT_FILE);`
  - `:133-134` in `deliverToWaiting`: the lexical check `path.dirname(directory) !== sessionsRoot(run)` only.
- Clause: v1.2 REQ-polaris-generation-035 says Syzygy writes the content "into the session's directory under the role's own file name …, and only there". Its falsifier arm reads: "Syzygy writes a session's handed-over content anywhere but the role's own file in that session's directory".
- Failing input [Observed, probe P1]:
  1. After `session-prompt <run> all`, replace `<run>.sessions/session-1` with a symlink to `<tmp>/elsewhere`, a directory outside the state root.
  2. Run `await <run>.sessions/session-1/ --submit inventory.json --stdin`.
  - Result: exit 0, `passed: true`, and `<tmp>/elsewhere/inventory.json` was written.
  - The same root cause applies to a review session's `round-N/verdict.json`. `deliverToWaiting` also `mkdir`s `round-N/` and writes `packet.json` (screened target text) into the symlink's target. [Inferred from the code path; not run]
- The directory argument is checked only lexically. `realDir` is never compared with `sessionsRoot(run)/<name>`, and the code never checks with `lstat` that the session directory is not a link.
- Any writer in the state root can plant the link, for example the authoring session. That is the "write reach" the package itself names.
- Repair:
  - require `fs.lstatSync(directory).isDirectory()` and `realpath(directory) === path.join(realpath(sessionsRoot), name)` before writing or delivering;
  - add a mutant for each check.

**Finding 2 — A design verdict with no continuation is not disclosed, and the design disclosure is untested** (revise)
- Where: `packages/polaris-dossier/src/render.ts:556`. The continuity sentence is appended only `${continuation?.continuing ? … : ''}`.
- Clause:
  - "For every counted verdict the review page SHALL disclose whether its session had received an earlier round, or declares the session identifier of an earlier verdict of its kind".
  - Scenario "Continuing reviewer disclosed", AND clause: "for a counted verdict with neither, the review page says so, labelled Inferred".
  - The applied spec carries both, at lines 326 and 398.
- Failing input [Observed by reading; the fidelity arm has the "Reviewer continuity" item, `render.ts:499` and the following lines]: a counted rendered-design verdict from a first-round session. The review-status line says nothing about continuity, so the page does not disclose "whether".
- The mutant record lists this predicate as not mutated because "no test there runs a design review to a counted verdict through a waiting session". That is a coverage gap, not a reason. The spec's falsifier arm "a counted verdict of a continuing reviewer is not disclosed as such" has no test for the design kind.
- Repair:
  - emit the "No earlier packet …" text for a counted design verdict too;
  - add a design-kind test, both continuing and not, and its mutants.

**Finding 3 — The printed hand-over says "(a heredoc)" with no quoted delimiter, so the shell can run text from the observed project** (revise)
- Where: `waiting-sessions.ts:406` and `:459`: "pass the verdict's JSON as the standard input of `… --submit … --stdin` (a heredoc)". The same instruction is in `waitingInventoryPrompt` and `waitingReviewPrompt` in `session-handover.ts`.
- Clause:
  - Direction: "Nothing unattended that executes observed code".
  - v1.2: "A waiting session SHALL NOT carry the execution permission".
  - The prompt's own SEC-3 line: "build, test and run nothing".
- Failing input [Inferred: POSIX shell semantics; not run]:
  1. A fidelity verdict quotes a span from a Redis shell or Tcl file containing `$(…)` or backticks, as a verdict must when it cites spans.
  2. The session follows the instruction literally: `syzygy dossier await <dir>/ --submit round-1/verdict.json --stdin <<EOF` … `EOF`.
  - With an unquoted delimiter the shell performs command substitution on the heredoc body. Text from the observed project then runs under the pre-approved `Bash(syzygy dossier await <dir>/:*)` rule.
  - Whether Claude Code's prefix matcher refuses or flags a heredoc that holds a substitution is [Unknown]. The PR discloses only that heredoc matching itself is Inferred.
- Repair:
  - make every printed instruction name a quoted delimiter (`<<'SYZYGY_EOF'`), and say that the body is never expanded;
  - pin that wording in a test.

**Finding 4 — The mutant record's "two unmutated predicates" is a false count: at least four more predicates survive the suite** (revise)
- Where:
  - `docs/evidence/polaris-dossier-waiting-sessions-mutants-2026-10-09.json`, `notMutated` (2 entries), and its scope sentence "One mutant per predicate: … each directory-argument check; the waiting-mode, containment and latest-session checks …".
  - The PR body: "Two predicates are not mutated".
- Clause: AGENTS.md rule 6 ("Mutate the input and confirm the check fails, per predicate") and rule 2.
- Failing input [Observed]:
  1. In the scratch worktree at the subject commit, I applied four deletions together:
     - `path.dirname(roundDir) !== realDir ||` at `waiting-sessions.ts:293`, the round-directory containment;
     - the `prompt['directory'] !== path.relative(…)` refusal at `:342`;
     - the `path.dirname(directory) !== sessionsRoot(run)` refusal at `:134`;
     - the `promptSha256` comparison at `:338`, reduced to `prompt === undefined`.
  2. I ran `npx vitest run packages/polaris-dossier/src/waiting-sessions.test.ts`.
  - Result: 44 passed, 44 tests.
  - Removing a check can only turn a refusal into a success, so each mutant also survives alone.
  - Other predicates appear in no mutant, and I did not run them: [Inferred]
    - the `--round` and `--wait-minutes` grammar and the 60-minute cap;
    - "--submit takes no --round or --wait-minutes";
    - the inventory `round !== 1` refusal;
    - the `reopened` gate re-check after delivery;
    - `handOver`'s refusal of `all` with `--kind`/`--fresh` and of inventory with `--fresh`.
- Repair:
  - add tests and mutants for each of these, or list each one in `notMutated` with a real reason;
  - restate the count in the record and the PR body.
  - Finding 1's fix adds two more predicates to cover.

**Finding 5 — `--stdin` writes before it validates, replacing a file that had passed** (note)
- Where: `waiting-sessions.ts:298-310`. Only the name, the size and emptiness are checked before `renameSync(pending, target)`. JSON and schema validation run after, in `checkInventory`/`reviewCheck`.
- Clause: the review criterion "validates before writing". The spec text itself orders "writes … and checks it", so this is not a spec violation.
- Failing input [Observed, probe P4]:
  1. A session's `inventory.json` had passed its check (705 bytes).
  2. It submits `garbage` on standard input.
  - Result: exit 1, and `inventory.json` now reads `garbage`.
  - Effect is limited: `reviewCheck` and the inventory check freeze their own copies in the run directory (`review.ts:473`), so a counted result is not changed.
- Suggestion: parse the input as bounded UTF-8 JSON before the rename, or state the order in the PR description.

**Finding 6 — "Only" is not enforced against the operator's other permission layers** (note)
- Where: `session-handover.ts`, `sessionCommands`: `--permission-mode default --allowedTools …`. Also `START_DISCLOSURES`: "The printed Claude Code command pre-approves only reading its directory … and its one `syzygy dossier await` command, never a write".
- Clause: the direction's "only read tools plus their one syzygy command pre-approved".
- Failing input [Inferred: Claude Code merges `--allowedTools` with the allow rules of user, project and local settings, and loads configured MCP servers]: an operator whose settings allow, for example, `WebFetch`, `Bash(npm test:*)` or an MCP tool. Their waiting session then runs those calls unattended, outside the printed rules.
  - On this host `~/.claude/settings.json` has 0 allow rules, so this host does not trigger it. [Observed]
- Suggestion:
  - add deny rules (`--disallowedTools` for Edit, Write, WebFetch, WebSearch and NotebookEdit) and `--strict-mcp-config`, or a settings-source restriction if the tool offers one;
  - or name the residual in the disclosure and the spec's Inferred list.

**Finding 7 — The default 9-minute slice exceeds a common default shell-tool timeout** (note)
- Where: `waiting-sessions.ts:47` (`DEFAULT_WAIT_MINUTES = 9`).
- Problem: the first prompt says "Run syzygy dossier await <dir>/ and wait" and gives no timeout. Only the "waiting" outcome tells the session to use its longest timeout.
- [Inferred] Claude Code's Bash tool defaults to 2 minutes, so the first call is killed before it returns. There is no unsafe effect, but the session receives a tool error rather than the outcome `waiting`.
- Suggestion: put the timeout advice, or `--wait-minutes 1`, in the fixed prompt.

**Finding 8 — The wait-mode gate opens on a filename alone** (note)
- Where: `waiting-sessions.ts:56` and `:66-73`.
- [Observed] Any file named `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md` with any content in `decisions/` opens every wait-mode step. The PR's own test writes the content `'x'`.
- The records root lies within the sessions' write reach, as `RECORDS_WITHIN_REACH` says. It may be worth checking the aggregate block or the record's head, as the recorder's `--check` does.

**Finding 9 — Paths outside the allow-list: subagents and output redirection** (note)
- [Inferred] Claude Code's subagent tool and its to-do tool need no approval. A waiting session can therefore start subagents unattended, with the same rules. Such a subagent is not a top-level session and satisfies no role.
- [Unknown] Whether the prefix rule `Bash(syzygy dossier await <dir>/:*)` admits an output redirection such as `syzygy dossier await <dir>/ > ~/x`. That redirection would be a write outside the role's file.
- Neither is stated in the package's disclosures or Inferred list.

## Notes

- **N1** (`POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`, item 4)
  - "A session therefore hands its inventory or verdict to that command, and Syzygy writes the file" is the lead's inference of a mechanism. The owner did not see it: they saw the form, not the packet. It is consistent with the selected words.
  - Consider labelling it as the drafter's reading [Inferred].
- **N2.** Bang form for waiting sessions [Inferred]: `! cd <dir> && claude '…'` runs inside the authoring session's shell for the whole run, and three are printed. That probably blocks or entangles the authoring terminal. Consider printing only the terminal form for `all`.
- **N3.** Shell redirection is covered under Finding 9.
- **N4.** Editorial, in the falsifier at applied `spec.md:406`: "…in that session's directory; or a broader pre-approval is printed…" has a stray "or" in the middle of the list.
- **N5.** `SEMANTIC-DELTA.md` lists the spec's files and identifier, but not the spec header line change ("version 1.1" to "1.2", adding the v1.1 record). It is non-normative; list it under the artifacts for completeness.
