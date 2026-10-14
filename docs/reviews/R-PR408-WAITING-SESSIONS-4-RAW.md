# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-2-4
Reviewed commit: a3cdb3e644258561e1630eae0436905819e0ddb8
Manifest SHA-256: d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2
Verdict: CONFIRM WITH EXCEPTIONS

Package: `polaris-dossier-local-agent-mode`, version 1.2. Candidate directory:
`.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-2/`
(PR 408). This is round 4, a second, independent confirmation over the same
bytes as round 3. The verdict was reached here without reading round 3's
verdict as an input. Round 3's raw was read afterwards, only to check whether
its findings were closed.

Reviewer context: fresh. I was given the brief's governing references, the
direction record, the owner's P-107 selection
(`owner-selections-2026-10-08.md` in the lead's scratchpad) and the earlier
raws. I did not receive the drafting conversation. No network was used beyond
`git fetch` of this repository. The one exception is a local `codex --help`,
which is a local binary and not a fetch.

## Subject digest

[Observed] In a scratch clone checked out at `a3cdb3e6…`:

- the `sha256` of `build_polaris_dossier_local_agent_mode_v1_2.subject_bytes(root)` is `d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2`;
- a plain `git apply` of `proposed/spec.md.patch` onto a copy of the installed `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md` gives the same digest (second method);
- the installed v1.1 spec at that commit hashes to `6414597d…`, which equals the ledger's v1.1 row.

Script: `r408r4_digest.py`. Both methods agree. The head carries this figure.

## Checks run

1. **Ledger sweep re-run.** [Observed] Script `r408r4_sweep.py` at `06ecd8ca…` (the commit the ledger names):
   - Population: 2,651 files from `git ls-tree -r -z`.
   - The four phrase rows give 4, 2, 1 and 4 files, with the same members as the ledger.
   - `POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08` appears in 6 files, the same six. The `…-2026-10-09` form appears in 0.
   - The digests of all five files under the change match the v1.1 column.
   - The overlap predicate `git grep -l -F REQ-polaris-generation-035 -- openspec` returns the ledger's three files.
   - Package bytes are identical between `06ecd8ca` and `a3cdb3e6`. The head commit edits only the ledger, and the subject digest is unchanged.
2. **Tests.** [Observed] After `npm ci` in the clone, `vitest run --project @syzygy/polaris-dossier packages/polaris-dossier/src/waiting-sessions.test.ts`, under a 600-second `timeout`, gave 114 of 114 passed. The whole `@syzygy/polaris-dossier` project gave 1,074 passed and 1 skipped, over 27 files.
3. **Code against spec.** [Observed by reading `waiting-sessions.ts` and `session-handover.ts` at the head; tests above]
   - **Wait.** The slice is `min(start + minutes, deadline)`. Minutes run from 1 to 60, 9 by default. Each look is a local `existsSync` (`waiting-sessions.ts:503-525`).
   - **Gates and re-hash on arrival.** The gates are re-checked on arrival (`openRun`, line 529). The packet is re-hashed against three things before the session is told what to read: `delivery.json`, `packet.sha256` and the run-directory delivery record (lines 537-543). The inventory brief is re-hashed against the prompt record's digest (lines 487-491).
   - **Delivery.**
     - The gates and the provider statement are checked for the waiting session's own recorded tool (`session-handover.ts` `deliverReview`).
     - `--tool`, `--tool-version` and `--model` are refused on delivery.
     - The delivery record is written first, and `delivery.json` is written last, by rename.
   - **Launch form.** A bang launch form is refused for a waiting session (`launchForm`).
   - **Printed Claude Code command:**
     - `--permission-mode default`;
     - `--tools Read,Glob,Grep,Bash`;
     - `--allowedTools 'Read(//<dir>/**)' … 'Bash(syzygy dossier await <dir>/:*)'`;
     - a deny list of the write, web and subagent tools;
     - `--strict-mcp-config`;
     - no bang form.
   - **Codex.** `allowedTools: null`, and the note says so.
   - **Hand-over.** It is a heredoc with `<<'SYZYGY_EOF'`. `--stdin` writes only `inventory.json` or a delivered `round-N/verdict.json`, and only after a bounded JSON parse.
   - **Disclosure.** `continuationOf` drives a review-page item for every counted fidelity verdict. For every counted design verdict, it drives the review-status region (`render.ts:499-506`, `551-557`).
4. **Recorder rehearsal.** [Observed] The rehearsal ran in the same scratch clone, and its results are in the section "Recorder rehearsal" below.

## Acceptance criteria

1. **Scope.** [Observed] Every hunk maps to an item of the direction, or is a version or status line:
   - spec hunk 1 is the version header;
   - the 035 paragraph covers items 1, 2 and 4;
   - the four scenarios, the case, the observable and the falsifier cover items 1, 2 and 4;
   - the warrant `decisions` is the direction ID;
   - the design paragraph, the two command rows and exit status 3 cover items 1 and 4;
   - the proposal adds a version line and one paragraph.

   No hunk lets Syzygy or the authoring session start, resume or signal a session. No hunk admits a headless or subagent session. The two new narrowing SHALLs are within item 4 and the owner's words "with only read tools plus their one syzygy command pre-approved": the tool-set limit, and the refusal of the shell-escape form for a waiting session. Both narrow, and neither widens.
2. **Mitigation.**
   - The pre-approval admits no write, as written.
   - The hand-over is within the owner's words. The session passes content to its one pre-approved command. Syzygy, not the session, writes exactly the role's own file in the session's directory, the target of the session's own submission. The spec bounds this to "under the role's own file name … and only there".
   - The quoted-delimiter rule closes shell expansion of the body [Inferred]. A valid JSON document cannot contain a line that is exactly the bare delimiter, so the body cannot end the heredoc early.
   - The residuals (settings layers, subagents, tools outside the agent tool's set, output redirection) are labelled Inferred or Unknown, not claimed closed.
   - For Codex, the conditional rule is coherent as text. See Finding 1 on what it leaves unnamed.
3. **Continuing reviewer.**
   - The disclosure is required "For every counted verdict", on the review page, with the anchoring cost ("has seen its own earlier verdict, which may anchor this one").
   - Continuity is detected by delivered rounds or by a repeated declared identifier. Both it and its absence are kept Inferred (scenario "Continuing reviewer disclosed").
4. **Existing 035 rules.** [Observed]
   - Retirement on revision is unchanged.
   - The session-identifier rule refuses only the author's or the inventory's identifier. A continuing reviewer's re-declared identifier collides with neither.
   - The launch-form rule narrows only for waiting sessions, and the delta says so.
   - The packet's contents are unchanged.
5. **Observed claims.** What the spec has Syzygy observe is what it wrote and the bytes it re-hashed. The following are all Inferred, and the sentence ends "no surface states any of them as Observed":
   - the session's reading;
   - the operator's use of the command;
   - the tool's honouring of the rules;
   - continuity.
6. **Bounded and local.** "waits at most a bounded time, never past the run's declared deadline" and "reads only the local file system and makes no network request" admit no unbounded or networked reading.
7. **Falsifiable.** Each new scenario has one WHEN/THEN with an AND. The falsifier gains an arm per new rule, and each arm is something a wrong build would trip. The suite's mutants show that the arms can be exercised (evidence record; not re-run here).
8. **Class.** Normative is right: the change adds SHALLs that a v1.1 build would not meet.
9. **Ledger.** Reproduced; see "Checks run" item 1.
10. **Owner packet.** It is fair, and the recommendation is labelled. It discloses the unattended-reading risk. Two sentences overstate; see Findings 1 and 2.
11. **Design stays design.** `design.md` names flags and a heredoc form as design. It contains no implementation code. Nothing under `openspec/**` is code.

## Earlier findings, checked closed

[Observed at the head]

- **Round 1.**
  - F1 (a linked session directory) is closed. `sessionDirectoryRefusal` lstat-checks the root and the directory, and pins each real path to its parent's entry.
  - F2 (design continuity) is closed: `designStatusItem` always carries the continuation text.
  - F3 (the unquoted heredoc) is closed: `stdinHandOver` uses `<<'SYZYGY_EOF'`.
- **Round 2.**
  - F1 (a linked sessions root) is closed by the same root check.
  - F2 (`bang` for a waiting session) is closed, refused in `launchForm`.
- **Round 3.**
  - Its notes remain as notes at these bytes. Its F5 (the Codex note) is the root of Finding 1 below, which I reached independently and widened to the owner packet and the spec's residual list.
  - Its missing `Manifest SHA-256:` head line is what this raw supplies.

## Findings

**Finding 1 — The Codex arm: the printed note and the owner packet say a waiting Codex session asks before each call, and the spec's residual list does not name the agent tool's own default approval behaviour** (note, for the owner)

- Concerns: package prose (`OWNER-DECISION-PACKET.md:43-45`, "a waiting Codex session asks before each step"), the implementation (`packages/polaris-dossier/src/session-handover.ts:89`, "…so a waiting Codex session asks you before each call and waits while you are away.") and, as an omission, the patch's residual sentence.
- Evidence [Observed, local `codex --help`]: `-a, --ask-for-approval` lists `on-request: The model decides when to ask the user for approval` and `never`. `-s, --sandbox` offers `read-only, workspace-write, danger-full-access`.
- Failing input [Inferred]: the operator runs the printed `codex '<prompt>'` for a waiting session, under an approval policy of `on-request`. The help text gives that policy to the model to apply. The model may then run a shell call without asking while nobody is present, and the printed sentence is false for that call.
- The spec's Inferred clause ("that no allow rule in a settings layer the operator keeps outside the printed command (the agent tool's user, project or local settings) widens what the session may run unattended") names settings layers. It does not name the agent tool's own approval behaviour when Syzygy prints no pre-approval. Even so, a successor should name it.
- The quoted SHALLs are not broken. The Codex note and the packet sentence state as fact something the spec would at most allow as Inferred.
- Whether `--sandbox read-only` is a way Codex "can limit which of its own tools a session has at all" is Unknown. It governs command execution, not the tool set. It would also likely block `await --stdin`'s own write, made by a sandboxed child process [Inferred]. Printing nothing is therefore defensible under the spec's text.
- Suggestion: in the packet and the note, say that what a waiting Codex session runs without asking depends on Codex's approval policy [Inferred]. In a later version, add that dependence to 035's Inferred list.

**Finding 2 — The owner packet's cost paragraph says flatly "It cannot write a file, and it cannot build or run the project", which its own earlier paragraph and the spec qualify** (note, for the owner)

- Concerns: package prose, `OWNER-DECISION-PACKET.md:77-78`.
- The same packet says at lines 55-62 that an allow rule in the operator's own settings, "for example for a test command", "still runs in a waiting session without asking". It also says whether the one command's rule "would let the session redirect its output into a file" is Unknown. The spec holds that redirection Unknown, and holds settings-layer allow rules Inferred.
- Failing input [Inferred]: an operator whose user settings allow `Bash(make test:*)` starts a waiting inventory session. A session that obeys text injected from the clone can run that command unattended, which builds and runs the project. The cost paragraph's "cannot" is false for that operator. The sentence after it ("allow rules in your own settings still apply") hedges the claim but does not withdraw it.
- Suggestion: "cannot, through anything the printed command pre-approves" instead of a bare "cannot".

**Finding 3 — Whether Claude Code's prefix rule admits the multi-line heredoc hand-over unprompted is Unknown, and a refusal reintroduces the stall the direction targets** (note)

- Concerns: implementation evidence (`waitingAllowedTools`, `stdinHandOver`), not the patches.
- The printed rule is `Bash(syzygy dossier await <dir>/:*)`. The hand-over the session is told to run is `syzygy dossier await <dir>/ --submit … --stdin <<'SYZYGY_EOF'`, followed by JSON lines and the delimiter. Whether the agent tool's prefix matcher treats a heredoc-bearing command as matching the prefix, rather than asking, is Unknown. The JSON may quote `$(`, backticks or `;` from the observed project, and a cautious matcher may ask.
- If the matcher asks, the failure is safe: the call waits for the operator. But the submission of a waiting session's inventory or verdict would then stall unattended, which is the condition option B was chosen to remove.
- The spec is unaffected: it states the pre-approval as a ceiling, and the tool's application of it as Inferred.
- Suggestion: record one attended observation of a real waiting session's submission before relying on unattended runs.

**Finding 4 — "A v1.1 run behaves the same with the code present" is not quite so: the render adds a continuity item for every counted verdict whatever the sign-off state** (note)

- Concerns: package prose, `SEMANTIC-DELTA.md:252-253` and `IMPACT-LEDGER.md:102` ("so v1.1 behaviour is unchanged while this package is unsigned"). The implementation is `render.ts:499-506` and `:551-557`.
- [Observed by reading] `continuationOf` is called, and its item rendered, whenever a fidelity or design verdict counts. It is not gated on `waitModeSignedIn`. A v1.1 run's review page gains a "Reviewer continuity" item, and its design review-status line gains a continuity sentence. Without any v1.2 sign-off, a v1.1 reviewer that re-declares an earlier verdict's session identifier is disclosed as "Continuing reviewer".
- The effect is a disclosure added, never a permission. The direction's merge order ("The code may merge only once version 1.2 is signed off") makes it moot once followed. The sentence describes the wait-mode gate correctly but the rendering imprecisely.
- Suggestion: scope the sentence to "every wait-mode step", or gate the render item.

No finding is blocking or revise. No finding concerns a defect in the patches against a quoted clause.

## Recorder rehearsal

[Observed] The rehearsal ran in a scratch clone at `a3cdb3e6…`, which is now removed.

**The synthetic raw and disposition.**

- A copy of this raw was placed at `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-2-4-RAW.md`.
- A synthetic `ROUND-4-DISPOSITIONS.md` was written beside the package. It carries `Reviewed record:` and Findings 1–4.

**This raw, read by the recorder's own functions.** The script is `r408r4_parse.py`.

- `parse_head` returns `('a3cdb3e644258561e1630eae0436905819e0ddb8', 'CONFIRM WITH EXCEPTIONS')`.
- `review_findings` returns `{1: 'note', 2: 'note', 3: 'note', 4: 'note'}`.
- The raw names the package key.
- `review_binds` accepts it: the head digest equals `subject_bytes` at the head.

**Before recording.** `waitModeSignedIn(root)`, from the built `dist/waiting-sessions.js`, returned `false`.

**Recording.** The command was `record_versioned_signoff.py --record polaris-dossier-local-agent-mode --version 1.2 --date 2026-10-14 --review <raw> --disposition <synthetic> --owner-selection-quote "Rehearsal only: 1.2 signed off."`. It printed:

- "applied v1.2; PROJECT-STATUS.md now reads 36 requirements and 248 scenarios";
- that it wrote `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md`;
- that it appended the aggregate block.

**After recording.**

- `--check … --version 1.2` printed "recorded polaris-dossier-local-agent-mode v1.2 sign-off regenerates exactly; applied tree verified".
- `--check` for 1.1 and 1.0 each printed "…regenerates exactly; superseded by a later version".
- The v1.0 builder's `--check` printed OK (applied).
- The v1.1 builder's `--check` printed OK (applied, options `['n6']`).
- The v1.2 builder's `--check` printed OK (applied).
- The installed spec's `sha256sum` was `d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2`, a third method for the head digest.
- `waitModeSignedIn` returned `true`: the gate opens.

**Mutation.** One newline was appended to the installed spec.

- `waitModeSignedIn` returned `false`.
- The v1.2 `--check` printed "FAILED: the latest signed version is not applied to the tree".
- Restoring the bytes reopened the gate (`true`).

`check_spec_reconciliation.py --regenerate`, the install-time edit to the `openspec/README.md` row, and the battery were not run here. The ledger names them as install-time steps.
