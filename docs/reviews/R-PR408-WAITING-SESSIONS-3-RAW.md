# Review — PR 408 pre-started waiting dossier sessions, round 3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: a3cdb3e644258561e1630eae0436905819e0ddb8
Reviewer: fresh-context

## Scope and method

- Subject: PR #408 at `a3cdb3e644258561e1630eae0436905819e0ddb8`. The round-2 subject was `c3709a3a`. The repairs `c3709a3a..a3cdb3e6` change 12 files. Over the merge-base `72ed0a59`, the whole PR touches 26 files: 14 added and 12 modified.
- Inputs read:
  - AGENTS.md;
  - the round-2 raw;
  - P-107 in the owner-selection record;
  - the repair diff (`git diff c3709a3a..a3cdb3e6`);
  - `waiting-sessions.ts` and `session-handover.ts` at the head;
  - the mutant record;
  - `record_versioned_signoff.py` (docstring, `parse_head`, the v1.2 package entry);
  - the v1.2 builder (`subject_bytes`, `check`, `signed_findings`).
- Probes ran in a local `git clone` under the scratchpad, checked out at the subject commit.
  - `npm ci` and `npm run build` both exited 0.
  - TMPDIR was set inside the scratchpad.
  - Every test run had a `timeout`.
- The PR's own suite: `waiting-sessions.test.ts`, 114 tests, all passing.
- Probe file `probe408r3.test.ts`:
  - It reuses lines 1–121 of the PR's own CLI harness verbatim.
  - It holds 6 probe tests (P1–P6), all run.
  - It was removed afterwards, with the clone.
- The retained raws in the PR are byte-identical to the reviewers' scratchpad copies: `git diff --no-index`, empty for round 1 and round 2.

## A. Round-2 findings at this head

| Finding | Status | Evidence |
|---|---|---|
| F1, linked sessions root (revise) | **Closed** | [Observed, P1] Round 2's input was re-run. `<run>.sessions` was moved to `<tmp>/p2-root-elsewhere`, outside the state root, with a symlink left in its place. `await <run>.sessions/session-1/ --submit inventory.json --stdin` with a valid inventory then exits 1, `outcome: refused`, `stage: directory`, with the reason "the sessions root … is not a directory of its own (a link, or another kind of file), so Syzygy writes nothing through it". `<tmp>/p2-root-elsewhere/session-1/inventory.json` does not exist. A plain `await` through the same link is also refused at `directory`. [Observed, P2] With the same link after `readyForReview`, `session-prompt <run> review --kind fidelity` exits 1 at stage `write` with the same reason. `p3-root-elsewhere/fidelity-1/` stays empty, and no delivery record or packet is written under `reviews/`: the check at `waiting-sessions.ts:213` runs before `writePacket` at `:223`. [Observed, P3] No false refusal: a state root reached through a symlinked ancestor (`<state>-via-link/<run>.sessions/session-1/`) submits and passes, exit 0, `passed: true`. That is because `lstat` follows intermediate links, and both real paths resolve through the same ancestor. |
| F2, bang for a waiting session (note) | Closed | [Observed, P4] `launch-form <run> review bang --kind design` for a waiting design session exits 1 at stage `form`. The PR test at line 482 covers the inventory and fidelity sessions. A terminal form is still recorded. |
| F3, comment overstating the syntax check (note) | Closed | `waiting-sessions.ts:362-366` now says "That is a syntax check only: well-formed JSON that fails the role's check still replaces it". |
| F4, gate is a format check (note) | **Closed as raised** | [Observed, rehearsal] Round 2's forged state was re-run in a scratch root: a six-line hand-written head, bare markers, no raw and the v1.1 spec. `waitModeSignedIn` returns `false` (V13 below). The residual is Finding 2. |
| F5, deny list only (note) | Closed, with the Unknown disclosed | See "`--tools`" below. |
| F6, two `notMutated` without reasons (note) | Closed | The old [7] (rethrow) is now mutant `R2-NM7`, killed with 2 failing tests; I re-applied it. The old [14] (usage errors) is now `R2-6a` and `R2-6b` for the two wait-mode flags given twice, and the record's scope sentence puts the shared positional-count checks outside the population. All 14 current `notMutated` entries are reviewed in criterion C7. |

**`--tools` (Finding 5).**
- [Observed] The printed waiting command is: `… --permission-mode default --tools Read,Glob,Grep,Bash --allowedTools 'Read(…/**)' 'Bash(syzygy dossier await …/:*)' --disallowedTools Edit Write NotebookEdit WebFetch WebSearch Task Agent --strict-mcp-config` (P6).
- [Observed] `claude --help` (2.1.295) lists `--tools <tools...>`: "Specify the list of available tools from the built-in set. Use "" to disable all tools, "default" to use all tools, or specify tool names (e.g. "Bash,Edit,Read")".
- [Observed] The full printed flag set, without a prompt and with `--version`, parses and prints `2.1.295 (Claude Code)`.
- [Unknown] Whether `--tools` actually removes every other built-in tool at runtime cannot be established without starting a session, which I did not do. The help text is the vendor's documentation of that behaviour.
- The spec patch lists "that the printed limit on the agent tool's own tools leaves the session no other of them" as **Inferred**, not Unknown. It lists "whether a tool from outside the agent tool's own set … remains available" as **Unknown**. START_DISCLOSURES says the same.
- I judge Inferred an honest label: there is documentary evidence of the behaviour and no observation of it. It is not an overclaim, because the spec states it as not Observed.

## B. Regressions

1. **Gate predicate on a real record: opens.** [Observed]
   - Subject digest re-derived by script (`hashlib.sha256(build_polaris_dossier_local_agent_mode_v1_2.subject_bytes(clone))`) gives `d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2`. The builder state is `unapplied`, and the digest equals the IMPACT-LEDGER's v1.2 spec row.
   - A synthetic CONFIRM raw was written with a head of title, `Verdict: CONFIRM`, `Reviewed commit: a3cdb3e6…` (40 hex) and `Manifest SHA-256: d6bce6b3…`. It names the package.
   - `record_versioned_signoff.py --record polaris-dossier-local-agent-mode --version 1.2 --date 2026-10-09 --review docs/reviews/R-SYNTH-R3-DOSSIER-V12-RAW.md --owner-selection-quote …` applied v1.2 ("PROJECT-STATUS.md now reads 36 requirements and 248 scenarios"), wrote the record and appended the block.
   - `waitModeSignedIn(clone)`, called through the built `dist/waiting-sessions.js`, gave `false` before the recording, `true` after it, and still `true` after `check_spec_reconciliation.py --regenerate`.
   - Then:
     - `--check … --version 1.2`: "regenerates exactly; applied tree verified";
     - `--check … --version 1.1`: "superseded by a later version";
     - v1.2 builder `--check`: "OK: the v1.2 package verifies (applied)";
     - v1.2 `--selftest`: "39 fixtures, 0 failing";
     - `openspec validate polaris-dossier-local-agent-mode --strict`: "Change 'polaris-dossier-local-agent-mode' is valid";
     - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
   - The applied `design.md`, `proposal.md` and `GOVERNING-DEPENDENCIES.md` hash to the ledger's v1.2 column (`4e04bd40…`, `73ace9e2…`, `b0da7790…`).
   - The patch line counts are 71, 82 and 41, as the ledger states.
2. **Gate predicate on forged and partial states.** [Observed] Each variant is a fresh scratch root built from the real recorded files:

   | Variant | Opens |
   |---|---|
   | V01 copy of record, aggregate, applied spec, raw | true |
   | V02 no review raw | false |
   | V03 raw head digest off by one character | false |
   | V04 digest moved past the raw's four-line head | false |
   | V05 installed spec edited (one byte appended) | false |
   | V06 v1.1 spec installed, raw head naming the v1.1 digest | false |
   | V07 record's `Review:` names `../…-RAW.md` outside the root | false |
   | V08b two `Manifest SHA-256` lines within the four-line head | false |
   | V09 aggregate block removed | false |
   | V10 record only, no aggregate | false |
   | V11 no installed spec | false |
   | V12 record verdict `REVISE` | false |
   | V13 round-2 F4 forged six-line head + bare markers, no raw, v1.1 spec | false |
   | V14 the same forged head with the v1.2 spec applied, no `Review:` line | false |
   | V15 forged head **with** a `Review:` line, a forged two-line raw (`# x`, `Manifest SHA-256: d6bce6b3…`), bare markers, applied v1.2 spec | **true** (Finding 2) |

   - A second digest on line 5 (variant V08, not tabled) still opens. This is consistent with the recorder: `parse_head` reads the same first-four-non-blank-lines window.
3. **New SHALLs stay inside option B.**
   - [Observed] The owner's selected words are "run unattended with only read tools plus their one syzygy command pre-approved" (owner-selection record line 33; direction record line 37).
   - The tool-set SHALL ("Where the agent tool can limit which of its own tools a session has at all, the printed command SHALL also limit a waiting session to its read tools and the shell its one command runs in") removes tools. It pre-approves nothing new: the allow-list is unchanged.
   - The launch-form SHALL ("Syzygy SHALL print its command for a new terminal only and SHALL refuse a shell-escape launch form declared for it") narrows v1.1's two forms to one, for waiting sessions only. The SEMANTIC-DELTA states that exception under "Not changed".
   - Both falsifier arms only add refusals. Neither widens what option B authorized.
4. **`launch-form` for non-waiting sessions.** [Observed, P4] All of these are recorded:
   - unsigned, v1.1 `session-prompt <run> inventory`, then `launch-form … inventory bang` (exit 0, form `bang`);
   - the same with `terminal`;
   - on a signed tree after `all`, `review --kind fidelity --fresh` (session 2), then `launch-form … review bang --kind fidelity` (exit 0).
   - A bogus form (`headless`) is still refused at `form`.
5. **Repairs do not move the mutant subjects.** [Observed] The four code files at the head equal their digests at `bf10c10e` and `b8896a97`. The test file at the head equals its digest at `b8896a97`. The repairs after `b8896a97` touch only prose, evidence and the raw.

## C. Standing criteria

1. **Allow-list: met.** [Observed, P6]
   - Denominator: 3 waiting sessions and 7 rules.
   - Inventory: `Read(/<clone>/**)`, `Read(/<sessions>/session-1/**)` and `Bash(syzygy dossier await <sessions>/session-1/:*)`.
   - Fidelity and design: `Read(/<dir>/**)` and `Bash(syzygy dossier await <dir>/:*)` each.
   - That is 0 Edit, Write or web rules and 0 other Bash rules.
   - `bang` is `null` for all 3 sessions.
   - Codex: `allowedTools` is `null` for all 3 sessions, and the note says no pre-approval is printed.
2. **Submit path: met.**
   - It is bounded: `readStdinBytes` stops past `DRAFT_MAX_BYTES`, and `SUBMIT_JSON_LIMITS` sets maxNodes 500,000 and maxDepth 16.
   - It validates syntax before the rename.
   - It is link-safe at the session-directory level (round 1, F1) and at the sessions-root level (P1, P2).
   - See Finding 1 for the check-then-use window.
3. **Continuity disclosure, both kinds: met.**
   - `render.ts` is unchanged since round 2, by digest.
   - The tests assert first-round and continuing text for fidelity (lines 680, 698, 717, 732) and for design (lines 768, 784).
4. **#406 tool-statement gate and #403 class gate: met.** [Observed, P5, probed with `--tool`]
   - With only a claude-code statement, `session-prompt all --tool codex` is refused at `statement`, and no sessions root is made.
   - With a codex statement in force that lists only `prose-content`, `all --tool codex` is refused at `statement`: "…does not list code-content, which the run's statement lets its packets carry…".
   - Waiting sessions were started under codex with both statements. After the codex statement narrowed to `prose-content`, the delivery was refused at `statement` ("…so no packet is delivered"), and `fidelity-1/` stayed empty.
   - A delivery with `--tool claude-code` is refused at `context`.
   - `--fresh --tool codex` with only a claude statement is refused at `statement`, and no `fidelity-2` is made.
   - With both statements withdrawn, the delivery and a later `await` are both refused at `reverify`.
   - The per-span class gate is still in `buildFidelityPacket` (`review.ts:202`), which `deliverReview` calls.
5. **Gate complete when unsigned: met.** [Observed by reading, and gate probe]
   - The three wait-mode entry points each evaluate the gate first:
     - `startSessions` at `session-handover.ts:386`;
     - `deliverReview` at `:465`;
     - `awaitSession` at `waiting-sessions.ts:407`.
   - Each defaults to `waitModeSignedIn(sources.recordsRoot)` when no port is injected.
   - On the unrecorded head tree the gate returns `false`.
   - `handOver` reaches `deliverReview` only when a waiting session exists. Otherwise it falls to the v1.1 `sessionPrompt`.
6. **Spec delta well formed: met.** [Observed]
   - A whitespace- and blockquote-normalized match finds 26 double-quoted passages of 12 or more characters in `SEMANTIC-DELTA.md`:
     - 23 occur in the applied v1.2 spec, design or proposal;
     - 1 occurs only in v1.1 ("Exact behavioral delta, version 1.1", quoted as the old text);
     - 2 occur in neither. Both are traced elsewhere: "with only read tools plus their one syzygy command pre-approved" is the owner's option text (direction record line 37), and "The code may merge only once version 1.2 is signed off" is direction item text (line 89).
   - All changes are inside REQ-polaris-generation-035.
   - `openspec validate --strict` passes on the applied tree (B1).
7. **Mutant record: met.** [Observed, script over `git show`]
   - There are 125 mutants with 125 distinct ids: 124 `killed` and 1 `killed (timeout)` (F4n).
   - 124 ran at `bf10c10e` and 1 (`R2-4d`) at `b8896a97`, as the `commitNote` says.
   - Every mutant carries `old`, `new` and `commit`. Every `old` occurs exactly once in its file at its commit, and no `old` equals its `new`: 0 problems over 125.
   - All 10 code subject digests (2 commits × 5 files) and all 3 builder subjects at `b8896a97` re-derive.
   - All 21 builder mutants are killed. Each carries old and new, and each `old` occurs once.
   - I re-applied 9 R2 mutants on the head tree: R2-1a, R2-1b, R2-2, R2-4a, R2-4b, R2-4d, R2-4f, R2-5 and R2-NM7.
     - All 9 were killed.
     - Their failing-test counts matched the record: 1, 1, 1, 6, 1, 1, 1, 1 and 2.
     - Each file was restored byte for byte.
   - All 14 `notMutated` entries give a real reason: unreachable, subsumed, equivalent, race-only, fault-injection-only, forwarding, fail-closed, or not a predicate.
     - [5] says that without a catch the exception "leaves the gate … so the step neither opens nor writes". That holds, because each of the three gate calls precedes any write (C5).
8. **Bound bytes, raws, placement, labels: met.** [Observed]
   - The repairs add 1 `-RAW.md` (round 2, byte-identical to the reviewer's copy) and edit no other.
   - Whole-PR name-status puts 0 code files under `openspec/**` or `.syzygy/**`. The 9 `.syzygy` paths are Markdown or `.patch` files.
   - The repair-added governance lines claim nothing accepted. The new text is conditional ("A v1.1 run behaves the same…", "until then").
   - The direction record and the candidate package bind no digest.

## Findings

**Finding 1 — The link checks are check-then-use: the sessions root is resolved again, or written through by path, after `sessionDirectoryRefusal` returns** (note)
- Where:
  - `packages/polaris-dossier/src/waiting-sessions.ts:436-448`: `awaitSession` checks at 436, then `realDir = realOrNull(directory)` at 444, then `writeFromStdin(realDir, …)`;
  - `:213-230`: `deliverToWaiting` checks at 213, then `writePacket` and `fs.mkdirSync(roundDir)` / `writeFileSync` through the unresolved `directory`.
- Clause (design patch): "Syzygy writes into a session directory, or delivers to one, only when it is a directory of its own whose real path lies in the sessions root, and the sessions root is itself a directory of its own whose real path is its entry in the state directory."
- Failing input [Inferred, not reproduced: it needs a racing writer]:
  1. A writer in the state root renames `<run>.sessions` away and leaves a link to the same layout elsewhere.
  2. It does so between line 437 and line 444 (await), or between line 214 and line 225 (delivery).
  3. The write then lands at the link's target.
- The window is a few synchronous calls wide. The writer would be the same party the F1 threat names.
- Suggestion: resolve once, and write only through the resolved, checked path. Or open the directory and use the `*at`-style pattern Node allows. At minimum, name the race in the code comment.

**Finding 2 — The gate still opens on a forged record, a forged two-line raw and a hand-applied patch; it reads less of the raw than the recorder does** (note)
- Where: `waiting-sessions.ts:102-116`, `appliedSubjectHolds`.
- Clause (SEMANTIC-DELTA): "neither a file that only carries the name nor a hand-written head with no review and no applied patch opens anything". That claim holds: V13 and V14 are both `false`.
- Failing input [Observed, V15]:
  1. A hand-written six-line head plus `Review: docs/reviews/FORGED-RAW.md`.
  2. A raw holding only `# x` and `Manifest SHA-256: d6bce6b3…`.
  3. The two bare markers.
  4. The v1.2 spec patch applied by hand.
  - `waitModeSignedIn` returns `true`.
- The gate checks:
  - neither the raw's own `Verdict:` nor its `Reviewed commit:` line;
  - nor that the raw names the package;
  - nor that the record's reviewed commit matches the raw's.
  The recorder's step 3 requires all of these.
- RECORDS_WITHIN_REACH discloses that agent sessions can write the checkout, so this is the disclosed residual. Each wait-mode step is also an operator action.
- Suggestion: mirror `parse_head`, which needs exactly one each of `Reviewed commit`, `Manifest SHA-256` and a confirming `Verdict` in the four-line head, and the package key in the raw. That makes a forgery match the recorder's own bar.

**Finding 3 — A recorded sign-off over a drifted spec is refused with "the owner has not signed off"** (note)
- Where: `waiting-sessions.ts:153`, `WAIT_MODE_UNSIGNED`, returned by all three gated steps whenever `waitModeSignedIn` is false.
- Clause: the same constant states "which the owner has not signed off; until the version-tagged sign-off is recorded". The epistemic discipline (AGENTS.md) requires stating only what is observed.
- Failing input [Observed state, V05; message derived by reading `:407`]:
  1. Record v1.2 as in B1.
  2. Append one byte to the installed spec, as a later unrelated edit or a readability successor would.
  - `waitModeSignedIn` returns `false`, and `await` and `session-prompt all` then say the owner has not signed off. The sign-off is recorded; what fails is the applied-subject comparison.
- Fail-closed is correct. Only the stated reason is false in this state.
- Suggestion: distinguish "no record" from "a record whose applied subject no longer matches", in the refusal reason.

**Finding 4 — The settings-layer residual is presented as unclosable, while the agent tool's help lists flags that reach those layers** (note)
- Where:
  - `OWNER-DECISION-PACKET.md:57`: "still runs in a waiting session without asking, and the printed command cannot switch it off";
  - `SEMANTIC-DELTA.md:148`: "no printed flag reaches the operator's own settings layers".
- Evidence [Observed, `claude --help` 2.1.295]:
  - `--setting-sources <sources>`: "Comma-separated list of setting sources to load (user, project, local)";
  - `--restricted`: "…ignores user, project and local settings files (managed settings and --settings still apply…)".
- Failing input [Inferred from the help text; not run in a session]: a printed command with `--setting-sources` naming no layer, or with `--restricted --tools Read,Glob,Grep,Bash`, would plausibly drop the user, project and local allow rules that the disclosure names as the residual.
- The SEMANTIC-DELTA sentence is literally true of the flags printed. The owner packet's "cannot switch it off" reads as a limit of the tool, and the help does not support that reading.
- The spec itself labels the residual Inferred, so this is no conformance defect.
- Suggestion: either evaluate one of these flags, or reword the packet to "the printed command does not switch it off", naming the flag and why it is not used, for example because it would also drop the operator's model or auth-related settings.

**Finding 5 — The Codex note states unconditionally that a waiting Codex session asks before each call** (note)
- Where: `session-handover.ts:89`: "…so a waiting Codex session asks you before each call and waits while you are away."
- Evidence [Observed, local `codex --help`]:
  - `-a, --ask-for-approval` takes `never` ("Never ask for user approval");
  - `-c` overrides values "loaded from `~/.codex/config.toml`".
- Failing input [Inferred]: an operator whose `config.toml` sets an approval policy of `never` runs the printed `codex '<prompt>'`. The session then runs calls without asking, contrary to the printed sentence.
- The spec's Inferred item ("that no allow rule in a settings layer the operator keeps outside the printed command … widens what the session may run unattended") covers this generically. The printed Codex note states it as fact, with no label.
- The new tool-set SHALL is conditional ("Where the agent tool can limit which of its own tools…"). Whether Codex can, for example through `--sandbox read-only`, which governs command execution rather than the tool set, is not addressed. [Unknown]
- Suggestion: label the sentence as depending on the operator's Codex configuration, as the Claude Code disclosure does for its settings layers.
