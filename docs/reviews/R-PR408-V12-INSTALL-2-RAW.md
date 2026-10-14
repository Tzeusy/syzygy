# Review — PR 408 v1.2 recording and install
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 5a2b2f6b3b00f42d480e475655d66398f933f87c
Reviewer: fresh-context

## Scope and method

- Subject: the five commits `a3cdb3e6..5a2b2f6b`:
  - `10da68e2`, `3e688141`, `9fd203b1` and `e9ab09f8`: 19 files, 15 modified and 4 added [Observed, `git diff --name-status`];
  - `5a2b2f6b`, which touches only `docs/README.md` (the campaign row) and `docs/reviews/R-PR408-WAITING-SESSIONS-4-NOTES.md` (it replaces "to be filed" with `syzygy-syoj` and `syzygy-zzt5`).
  - Earlier PR #408 bytes were not re-reviewed.
- I first reviewed `e9ab09f8`. When the subject moved, I ran the Python battery again in a second scratch clone at `5a2b2f6b`, as listed under criterion 6. Criteria 1–5 rest on `e9ab09f8`, and `5a2b2f6b` changes none of their inputs.
- Inputs: AGENTS.md, the owner selection record `scratchpad/owner-selection-v1-2-2026-10-14.md`, the scratchpad raws 3 and 4, and the repository at the reviewed commit. Network use: `git fetch` only.
- Everything ran in a scratch clone at `e9ab09f8` under the scratchpad, with `TMPDIR` set to a scratchpad directory. After `npm ci` and `npm run build`, the clone was removed. Scripts: `v12rev_quote_check.py`, `v12rev_apply_check.py`, `v12rev_bound_check.py`, `v12rev_battery_count.py`, `v12rev_sweep_mutants.py`, `v12rev_vitest_failures.py`.

## Acceptance criteria

1. **Retained raws.** [Observed] `cmp` finds `docs/reviews/R-PR408-WAITING-SESSIONS-3-RAW.md` and `-4-RAW.md` byte-identical to the scratchpad copies. Over the range, `git diff --name-status -- '*-RAW.md'` lists only those two, both `A`. No other raw was edited. **Met.**

2. **Sign-off record** (`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md`).
   - [Observed] The question, 1,110 characters, appears in the record exactly and in quotation marks. The selected label "Sign version 1.2 (Recommended)" is quoted exactly. Both files are NFC. The record does not carry the unselected label "Not yet".
   - Line 15 says "The owner selected the offered option; the words were not typed."
   - The instant `2026-10-14T03:32:23.826Z` matches the selection record.
   - `Review:` names the round-4 raw. Its head says `Manifest SHA-256: d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2` over `a3cdb3e6…`.
   - The subject digest was derived again by script: `git apply` of the three patches at `a3cdb3e6` to that commit's v1.1 bytes gives `d6bce6b3…`. That equals the installed spec's `sha256sum`.
   - The record carries no `Options:` line and labels nothing beyond the selection.
   - The aggregate block's opening marker and heading each occur once in `ACCEPTANCE-ACT-RECORD.md`; `grep -c` gives 2 over both patterns together. The recorder reports `--check … --version 1.2`: "recorded polaris-dossier-local-agent-mode v1.2 sign-off regenerates exactly; applied tree verified".
   - **Met**, subject to note 1.

3. **Install.**
   - [Observed] For spec, design and proposal, the patches applied to the `a3cdb3e6` bytes equal the installed bytes at `e9ab09f8`. The installed bytes hash to the v1.2 `IMPACT-LEDGER.md` after-column: `d6bce6b3…`, `4e04bd40…` and `73ace9e2…`. `GOVERNING-DEPENDENCIES.md` hashes to `b0da7790…`, its ledger row, and `tasks.md` still hashes to its "unchanged" row `6ccaa689…`.
   - The only `openspec/**` changes are those three files, `GOVERNING-DEPENDENCIES.md` and the `openspec/README.md` row.
   - The package directory is unchanged over the range (empty diff).
   - `build_polaris_dependency_unions.py --check` printed "4 Polaris dependency unions match their warrants". `check_spec_reconciliation.py --check` R3 found that the census matched (119 examined, 0 findings).
   - The census diff is exactly 244→248 and the four new scenario names.
   - **Met.**

4. **Integration edits.**
   - [Observed] Over the 2,655 tracked files at `e9ab09f8`, I searched for the pre-range digest of each of the 15 modified files (16-hex prefix). Results:
     - Six files had no citer: the workflow, `ACCEPTANCE-ACT-RECORD.md`, `PENDING-OWNER-DECISIONS.md`, `PROJECT-STATUS.md`, `docs/README.md` and `openspec/README.md`. The census, the two tests and the remaining files of the 15 had none either.
     - The two SKILL.md digests are cited only by `docs/evidence/polaris-dossier-clone-{allowlist,config}-mutants-2026-10-07.json`. Those are rule-11 evidence records of the bytes they mutated, not acts.
     - The old openspec digests are cited only by the v1.1 and v1.2 `IMPACT-LEDGER.md` before-columns and by v1.1 history (the raw, the notes and the S11 mutants), as expected.
     - No manifest or acceptance record binds a modified file.
   - The battery block has 95 `python3` lines, and the workflow has 95 `python3` run steps. Both sets have 95 distinct entries and differ by none. The three new lines are the v1.2 recorder `--check` and the v1.2 builder `--check`/`--selftest`. The sentence says "ninety-five". CG-26 printed "95 published, 95 hosted, 95 shared".
   - The P-107 row and the dated note are correct, and the register row count is unchanged, consistent with P-105/P-106.
   - The `openspec/README.md` row names the v1.2 record, and R5 passes.
   - The agent-texts pin moves to "Exact behavioral delta, version 1.2.", and the test passes.
   - The skill and Codex texts use only CLI forms that `cli.ts:66-89` defines (`session-prompt … all`, `--fresh`, `await <session-dir>/`). **Met**, subject to note 3.

5. **Authority-sweep change.** [Observed] The family regex admits only the literal `WAITING-SESSIONS` arm with a date. Mutant results:

   | Mutant | Result |
   |---|---|
   | M0, unmutated | 5/5 pass |
   | M1, family regex reverted | 2 fail |
   | M2, declaration line end-anchored again | 1 fail |
   | M3, family widened to `POLARIS-DOSSIER-[A-Z0-9-]+-date` | 1 fail |
   | M4, the direction's ID re-dated to `-10-09` | 1 fail |
   | M5, declaration line left unanchored after the closing backtick | **survives** |

   Each run used a 300 s timeout and restored the file. The widened declaration-line regex is note 2. **Met with a note.**

6. **Battery in the clone** [Observed, output read]:
   - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)". The WARNs I read are report-only, and none names a file the range touched. The 17 CG-27 findings are all in `decisions/README.md`, which the range does not touch.
   - The recorder `--check` gives:
     - 1.2: "…regenerates exactly; applied tree verified";
     - 1.1 and 1.0: "…regenerates exactly; superseded by a later version".
   - The builders' `--check` print:
     - v1.0: "OK: the package verifies (applied)";
     - v1.1: "OK: the v1.1 package verifies (applied, options ['n6'])";
     - v1.2: "OK: the v1.2 package verifies (applied)".
     - The v1.2 `--selftest` gives "39 fixtures, 0 failing".
   - `openspec validate polaris-dossier-local-agent-mode --strict`: "Change 'polaris-dossier-local-agent-mode' is valid". It was run in the clone. A first invocation ran by mistake in the session's own cwd and is disregarded.
   - `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL; PASS". The R6 WARN covers two behaviour-contract pins and predates the range.
   - `check_docs_review_campaign_partition.py`: "total=393 assigned=393 … unmatched=0 overlaps=0". The campaign row counts 5.
   - Full `vitest run` gives 4,560 passed, 6 failed and 19 skipped. All six failures are "browser exited with signal before announcing a DevTools endpoint" (a Chrome crash-report lock under `~/.config/google-chrome`). Two further suites fail at the browser start for the same reason. [Inferred: these are environmental, and none is in a file the range touched.] The two changed test files pass: 11 of 11.

   - **Re-run at `5a2b2f6b`** [Observed, output read]:
     - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)", with the same WARN set.
     - The recorder `--check` for 1.2 gives "regenerates exactly; applied tree verified"; for 1.1 and 1.0, "regenerates exactly; superseded by a later version".
     - The v1.0, v1.1 and v1.2 builders' `--check` give the same OK lines as above.
     - `openspec validate … --strict` reports the change valid.
     - `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL; PASS".
     - The partition reports "total=393 assigned=393 … unmatched=0 overlaps=0".
     - npm and vitest were not run again: `5a2b2f6b` changes no code or test.

7. **The notes record and the edit at `5a2b2f6b`**: lawful. See note 4.

## Findings

**1 — The sign-off record binds a review that finished after the owner's selection, while quoting the owner's question that counts three rounds** (note)

- Concerns: `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md:15` and `:17`.
  - Line 15 quotes the owner's question: "Three review rounds; the last was CONFIRM WITH EXCEPTIONS, notes only."
  - Line 17: `Review: docs/reviews/R-PR408-WAITING-SESSIONS-4-RAW.md`.
- [Observed] The selection record says "Subject reviewed: … review R-PR408-WAITING-SESSIONS-3-RAW.md" and "What the owner saw: … Not the raws". The answer instant is 03:32:23Z. The round-4 raw's scratchpad mtime is 03:42:36Z, and commit `3e688141` retained it at 03:45:20Z.
- [Inferred] The owner signed on round 3's outcome. Round 4 confirmed the same bytes afterwards, at the same commit and digest. Neither the record, the aggregate block, the P-107 row nor the notes record says that round 4 postdates the selection. The notes record (`R-PR408-WAITING-SESSIONS-4-NOTES.md:32-37`) says only that round 3's head could not be bound.
- The offer itself was lawful. `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md:40-42` says: "a package is offered only after a round that returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only". Round 3 met that before the offer. Round 4's four findings are notes, and the owner's question already carried their substance as residuals (1) and (3).
- Failing input: a later reader reads the record's `Review:` line as the review the owner relied on. That reader concludes the owner saw round 4's Codex-approval finding at signing. The owner did not.
- Suggestion: add one dated sentence to an unbound carrier, such as the P-107 row or a new dated note in the register, never the record. It should say that the owner was offered round 3, that round 4 ran over the same bytes after the selection, and why round 4 is the review of record.

**2 — The declaration-line regex is loosened for every `Decision ID:` line, not only the one that needs it, and no fixture pins its anchoring** (note)

- Concerns: `apps/three-surface-poc/src/polaris-authority-sweep.test.ts:132`, ``/^Decision ID: `([A-Z0-9-]+)`(?:$| )/gm`` (was `` `$ ``).
- [Observed] `.syzygy/governance/decisions/` has 23 `Decision ID:` lines. Only `POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md:7` carries trailing text ("(named for the"), so today the declared set grows by exactly that one id. M2 shows the change is needed. The direction is a plain owner direction, and its wording need not change.
- Failing input [Inferred]: a later decision file writes ``Decision ID: `POLARIS-DOSSIER-LOCAL-AGENT-X-2026-11-01` (withdrawn; see …)``. That line now counts as an owning declaration. Also, mutant M5 (drop the `(?:$| )` guard entirely) passes all five tests, so nothing pins the guard's anchoring.
- Suggestion: either admit trailing text only as `` ` (`` followed by a parenthetical, or add one negative fixture for the declaration matcher. Either way, a widened matcher should fail a test.

**3 — The Claude Code skill states waiting-session confinement and "walk away" without the qualifiers that the Codex text and the spec carry** (note)

- Concerns: `.claude/skills/polaris-dossier/SKILL.md:74-77`: "can then walk away. Each session waits on its own `syzygy dossier await <session-dir>/` command, reads only its own directory (the inventory session also the clone), writes no file".
- The Codex text at `.codex/skills/polaris-dossier/SKILL.md:59-61` now qualifies the same statements by the operator's approval policy. The spec (`spec.md:326`) holds as Inferred "that no allow rule in a settings layer the operator keeps outside the printed command … widens what the session may run unattended". Round-4 finding 3 holds as Unknown whether the heredoc hand-over runs without a prompt.
- Failing input [Inferred]: the operator's `~/.claude` settings allow `Bash(make test:*)`. A waiting inventory session can then run it unattended. Or the prefix matcher asks on the heredoc, and the operator who "can then walk away" returns to a stalled submission.
- The skill is an instruction text, not a surface. The spec forbids only stating these as Observed on a surface. This is the same class as round-4 finding 2, which is deferred to `syzygy-syoj`. Fold it into that bead.

**4 — The edit at `5a2b2f6b` to the notes record after recording is lawful: no digest of the record is bound, and the recorder's `--check` still passes. It rewrites in place rather than adding a dated line, and two bead notes now say the opposite** (note)

- Concerns: `docs/reviews/R-PR408-WAITING-SESSIONS-4-NOTES.md:41-48` and seven "Deferred to …" sentences. At `9fd203b1`/`e9ab09f8` they read "Two follow-up beads are **to be filed** by the lead; this record files neither" and "Deferred to the first bead (to be filed)". At `5a2b2f6b` they read "Each is deferred to one of two follow-up beads, filed by the lead" and "Deferred to `syzygy-syoj`".
- How the record is cited [Observed]:
  - The sign-off record cites it by path only: `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md:23`, ``Disposition: docs/reviews/R-PR408-WAITING-SESSIONS-4-NOTES.md``.
  - The aggregate block cites it the same way, in its `Review outcome` row.
  - Over the 2,655 tracked files at `5a2b2f6b`, I searched for the record's sha256 at `3e688141`, `9fd203b1` and `e9ab09f8`, all the same, `87761a57…`. I also searched for its sha256 at `5a2b2f6b` (`8b78949d…`) and for both git blob ids (`e3ff8af2…`, `d187001b…`), each at 8, 12 and 16 hex characters and in full. **0 hits.**
  - The record's path appears in four files: `ACCEPTANCE-ACT-RECORD.md`, `PENDING-OWNER-DECISIONS.md`, the v1.2 sign-off record and `docs/README.md`. `check_governance.py` is not among them, so it is not in `ACT_DIGEST_COPY_FILES`.
- What the recorder checks [Observed]:
  - `validate_disposition` (`scripts/record_versioned_signoff.py:398-415`) checks only three things: that the file exists, that it names the reviewed raw, and that its finding numbers match.
  - The recorder's own selftest asserts this (`:1190-1193`): "an edited sibling disposition record is not package bytes".
  - At `5a2b2f6b`, `--check … --version 1.2` prints "recorded polaris-dossier-local-agent-mode v1.2 sign-off regenerates exactly; applied tree verified". 1.1 and 1.0 regenerate exactly too.
- Was the substance kept? [Observed] Yes. The mapping is unchanged: the "first bead" (round-4 findings 1, 2 and 4; round-3 notes 1, 2, 3 and 5) is now `syzygy-syoj`, and the "second bead" (round-3 note 4; round-4 finding 3) is now `syzygy-zzt5`. That matches both beads' descriptions (read with `bd --readonly show`). The `Reviewed record:` line and every finding heading are unchanged.
- [Inferred] So nothing binds the old bytes:
  - There is no act digest, no registered copy and no raw that quotes the record's digest.
  - The annotated tag `polaris-dossier-local-agent-mode-v1.2`, which the sign-off record names as "the binding", does not exist yet: `git tag --list` shows only v1.0 and v1.1. When it is created on the merged commit, it will freeze the `5a2b2f6b` bytes.
  - The only review that read the old bytes is this one, at its earlier subject `e9ab09f8`. That pass was never retained and is superseded by this one at `5a2b2f6b` (rule 10).
  - `9fd203b1`'s path citation now resolves to different bytes. The citation asserts nothing about content beyond the three predicates the recorder checks, and those still hold.
- Two notes remain:
  - The edit rewrites the prior wording in place, with no dated marker. The repository's own practice for a sentence that has become stale is a dated addition that keeps the old text, as with the register's "Updated …" notes and the AGENTS.md stale-sentence lesson. `git log` keeps the old bytes, so this is a style point, not a defect. The rewrapped lines at `:67`, `:74`, `:83`, `:92`, `:101` and `:119` now run past the 78-column wrap.
  - The beads' notes fields say the opposite of what happened. `syzygy-syoj`: "bound by the v1.2 sign-off, not edited"; `syzygy-zzt5`: "the record is bound by the v1.2 sign-off and is not edited". Both are now false and should be corrected in the tracker. Separately, `syzygy-syoj`'s description names `docs/reviews/R-PR408-WAITING-SESSIONS-3-NOTES.md`, which `3e688141` deleted. Both are outside the PR's bytes.

**5 — The `docs/README.md` partition sentence carries the new count under the old date** (note)

- Concerns: `docs/README.md:143-144`: "393 files, 393 assigned, no remainder [Observed — re-derived for HEAD dated 2026-10-09 …".
- [Observed] The helper at `e9ab09f8` and again at `5a2b2f6b` prints `total=393 … observed=2026-10-14`. The figure is right, but its as-of date is the date of the previous derivation.
- Suggestion: set the date to the derivation that produced 393.

No finding is revise. The install matches the reviewed patches, the records regenerate, and the battery is clean apart from the browser-environment failures named in criterion 6.

## Recorded limits

- [Unknown] Whether the two suites with no failed assertions (`orrery.browser.test.ts`, `polaris-accessibility.browser.test.ts`) pass in a working browser environment. Both depend on the Chrome start that failed here.
- I did not check the lead's chat summaries, which the selection record says the owner saw.
