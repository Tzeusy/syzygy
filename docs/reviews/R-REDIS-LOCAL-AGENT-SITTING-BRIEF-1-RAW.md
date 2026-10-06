# R-REDIS-LOCAL-AGENT-SITTING-BRIEF-1 — raw review
Subject: .syzygy/governance/contracts/candidates/REDIS-LOCAL-AGENT-SITTING-BRIEF.md
Subject SHA-256: 49318780cccfd27c30c276298ff5bec5e245a01b70827a53aad2195e0a6357b6
Verdict: REVISE
Reviewed commit: d3519781

Reviewer method: fresh-context review, 2026-10-07. Worktree
`/home/tze/GitHub/syzygy/.worktrees/parallel-agents/sitting-brief`, HEAD
`d3519781`. `sha256sum` on the subject printed the digest above before any other
step. I read the subject in full and opened the files and commits named below. I
ran `gh pr view` on Tzeusy/syzygy for #120, #278, #367, #368, #370, #372 and #376,
and `bd show` on `syzygy-qkea.4`, `syzygy-qkea.16` and `syzygy-2g0d`. I did not
re-run the rehearsal. I read no external repository content and edited nothing.
Line numbers refer to the subject at `d3519781`.

Checks that passed (no finding):

- PR states. #367 MERGED 2026-10-06T18:35:16Z (merge `ff7e5123`). #370 MERGED
  2026-10-06T18:43:24Z (`ddbb78eb`). #372 MERGED 2026-10-06T17:32:40Z; its title
  records the v1.1 sign-off with N6. #376 MERGED 2026-10-06T20:10:39Z, head
  `8c556f08`, merge `72ef12d3`. #368 MERGED. #278 MERGED 2026-10-03. #120 OPEN.
  The UTC times fall on 2026-10-07 in the repository's +0800 commit dates, so
  "2026-10-07" is consistent.
- Round 7 of screening scope v2. The head of
  `public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-7-RAW.md`
  reads `Verdict: CONFIRM WITH EXCEPTIONS`. Its findings 1 to 5 are all
  `(note)`. `ROUND-7-DISPOSITIONS.md` is present. `FROZEN_SUBJECT` in
  `record_public_source_screening_scope_v2_act.py` is set at `8c556f08`.
  Round 6's raw reads `Verdict: REVISE`, and `e7ad7934` is the round-6 repair.
- `8422119c` matches the brief: "fix(polaris-dossier): cap reader paths at
  git's core.maxTreeDepth (4096) … (R-POLARIS-DOSSIER-S2-READER-3 note 1)". It
  touches `packages/polaris-dossier/src/git-object-reader.ts` and sits after
  `ff7e5123` (#367's merge) in `git log --first-parent`.
- `db510842` matches the brief: "feat(polaris-dossier): S3 preflight and init
  gates, pinned revision, governed predicate".
- The scripts are byte-identical. `git diff --stat 8c556f08 d3519781 -- scripts/`
  is empty. The six files #376 touched (`gh pr view 376 --json files`) are the
  six scripts.
- Rehearsal mechanics, read from the scripts:
  - the simulator runs every `python3` line of the battery
    (`battery()`, lines 194-207);
  - it requires `0 FAIL` from governance (line 255);
  - Vitest runs only with `--vitest` (line 256);
  - the installer's `--check` prints "recorder checks failing:" and
    "not installed:" (installer lines 594-595);
  - the recorder order is v1.1, screening-v1, rfc5, screening-v2,
    redis-observation, entry, statements, profile (installer lines 271-274),
    which matches steps 3 to 9.
- The accept-all string at lines 395-400 matches, character for character, the
  quotation in `decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md` lines 22-28.
- Owner-words strings:
  - "1.1 signed off with N6; N1 and N2 as recommended." is at
    `polaris-dossier-local-agent-mode-v1-1/OWNER-DECISION-PACKET.md:143`;
  - "No drawer (Recommended)" is at
    `dossier-local-agent-acts/OWNER-SITTING-PACKET.md:214`;
  - `record_versioned_signoff.py:317,330` refuses a quote without
    "Extend Scope A";
  - the labels the brief gives for B, C, D, I and A/G/H match the simulator's
    `ANSWERS` (lines 61-88);
  - none of the strings contains `': '`, `' #'` or `'`, which the installer
    refuses (line 175).
- No digest. `grep -c -E "[0-9a-f]{64}"` returns 0. A second method,
  Python `re` over `[0-9a-fA-F]{32,}`, returns `[]`. The only hex tokens are six
  8-character commit prefixes.
- VIS-4. Nothing in the subject performs, adopts or signs. The "Answered" and
  "Done" notes report records that exist (the v1.1 sign-off record and the
  direction both exist at `d3519781`).
- PR #370 round 3. The head of
  `dossier-local-agent-acts/reviews/R-DOSSIER-LOCAL-AGENT-SITTING-3-RAW.md`
  names `Reviewed commit: d19ec98b…` and reads `Verdict: CONFIRM WITH EXCEPTIONS`.
  Narrative profile round 3 also reads `Verdict: CONFIRM WITH EXCEPTIONS`.
- `install_redis_sitting.py` still carries `REQUIRED_RECORDS` (line 65) and
  `missing_records()` (line 278).

### 1 — E's update says a later reader repair is approved by the same sign-off; the entry it signs says the opposite (revise)

Anchor: lines 207-211, "The entry is still bound to no reader bytes, so a later
reader repair is approved by the same sign-off."

Evidence: E's subject is
`public-git-source-acquisition-local-agent/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json`.
Its line 14 (`implementationStatus`) reads: "implementationVersion 1.0.0 names
that file as merged, and any change to it is a new implementation version and a
new version of this entry." PR #370's `ROUND-3-DISPOSITIONS.md` line 75 agrees:
"The entry defines 1.0.0 as the file 'as merged'."

`git log --first-parent d3519781` puts `8422119c`, which changes
`packages/polaris-dossier/src/git-object-reader.ts`, after `ff7e5123`, the merge
of PR #367. So the file on `main` is no longer the file as merged.

By the entry's own words, that change, and any later reader repair, is a new
implementation version and a new entry version. It is not approved by the v1.0
sign-off. The brief tells the owner the reverse, with no label, inside a bracket
that opens `[Observed]`. Whether `8422119c` already falls outside 1.0.0 depends
on which merge "as merged" means. That is a reading question the brief should
put to the owner, not settle for them.

Fix: replace the sentence. Quote the entry's clause and say that, by it, a reader
change after merge is a new implementation version and a new entry version.
State as `[Unknown]`, or as an owner question, whether `8422119c` already counts
against 1.0.0. If it does, E is offered at a version that names the reader as it
stands on `main`.

### 2 — "P-95's act B, the registry, is not affected" is unsupported: the package refuses as a whole, and its re-derivation retires B's review binding too (revise)

Anchor: lines 130-137 (under B) and lines 180-181 (under D, "see B").

Evidence:

- Whose argument the policy subject's predecessor carries.
  `build_pwb_behavior_contract_repin_tree_framing.py` lines 118-126 give the
  policy subject the predecessor
  `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`, which is
  the 2026-10-02 re-pin act. `base_bytes()` (lines 182-197) refuses unless the
  policy file hashes to that record's digest.
- What the sitting does to that file. `install_redis_sitting.py`
  `policy_acts()` (lines 877-897) reads v1 with `supersedes=REPIN_ACT` and v2
  with `supersedes=SCOPE_ACT`. It refuses unless
  `POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` hashes to the
  final act's argument. That is the tree-framing package's policy subject.
- So the brief's main claim is correct. After the sitting, act A's predecessor
  is superseded, and the policy half must be re-derived over the v2 bytes.
  Strictly, recording B alone causes it. D moves the bytes again.
- Act B is not independent in the tooling:
  - `check()` (lines 278-319) gathers findings across both subjects.
  - `apply()` (lines 322-338) refuses any `--apply`, including
    `--apply registry --at-adoption`, while `check()` has any finding.
  - The P-95 packet ("At adoption", step 1) records each act through that
    `--apply <subject> --at-adoption`.
  - The manifest comparison (line 307) is skipped once one subject fails.
  - Regenerating the manifest "changes both act arguments and retires any
    review bound to the old one" (docstring lines 52-53).
  - The review head binds the manifest FILE digest, which carries both rows
    (docstring lines 44-47).
  - So after the sitting, B cannot be recorded through this package until the
    policy half is re-derived. Re-deriving it retires the review binding for B
    as well as A.
- B's row digest may well be unchanged. `[Inferred]`: no sitting step writes
  the observer registry file, since `build_public_git_source_acquisition_local_agent.py`
  only reads it (lines 206, 252). But "not affected" is not true of B as an act
  the owner can perform.
- The rehearsal did not observe B separately.
  `check_spec_reconciliation.py` `_tree_framing_mutant` (lines 1482-1497) builds
  both subjects through `_repin_package` and skips as a whole when the package
  refuses. The `[Observed in the 2026-10-07 rehearsal]` label is placed before
  this sentence, but the sentence is not covered by it.
- The P-95 direction C is also affected, which the brief does not mention. The
  P-95 packet lines 128-138 put C as re-pointing a gate that "still expects the
  2026-10-02 re-pin acts", with the policy supersession target named as the
  2026-10-02 policy record. After the sitting, the installer has re-pointed the
  gate's policy role to the screening v2 act and its supersession target to v1
  (`repoint_gate`, lines 905-949; `policy_acts`). C's wording for the policy
  role is then stale too.

Fix:

- Under B, say that recording B supersedes the act P-95's policy half re-pins
  from, so P-95's act A must be re-derived over the final (v2) policy bytes.
- Say that the P-95 package (builder, manifest, review binding) must then be
  regenerated and re-reviewed as one unit. That also retires B's review
  binding, and C's policy-role wording must be redrafted.
- Label B's argument as unchanged `[Inferred]`, not unaffected.
- Under D, say "recording B (and then D) stales…", or keep "see B".

### 3 — The rehearsal claim rests on no retained record, and its subject is named loosely (note)

Anchor: lines 451-470.

Evidence:

- No report is retained in the repository.
  `git grep -F "local-agent-sitting-rehearsal" d3519781` hits only the
  simulator's `--report` default.
- The PR #376 body gives the 91/0 figure for "Rehearsal 5: origin/main
  `154e4767` plus PR #370 and PR #367 merged". It says "Rehearsal 6: this
  branch on real main. The result is in the PR comments", but
  `gh pr view 376 --json comments,reviews` returns empty lists.
- The only record of a run at `8c556f08` is the close reason of
  `syzygy-qkea.16` ("Installer merged via #376 at 8c556f08; rehearsal 7 green
  91/0"), plus the subject's own commit message.
- The simulator does not rehearse a commit as such. It clones `--base`
  (default `refs/remotes/origin/main`) and overlays five scripts from the
  running tree (`OVERLAY`, lines 47-50; `overlay()`). The base head is in the
  unretained report only.
- `main` at `72ef12d3` also differs from `8c556f08` outside `scripts/`
  (S4/S5 package code, `git diff --stat 8c556f08 72ef12d3`).
- The claim is plausible, and the bullet's own rule-7 sentence honestly scopes
  it. But under rule 11 a reader cannot re-check it.
- Line 451 says "Steps 3 to 11 were rehearsed", but step 11's Vitest half was
  not run (line 463). Only the bullet below corrects that.
- Line 469 says each failure "was fixed". For the P-95 case, the "fix" is that
  the reconciliation selftest now skips its tree-framing mutant with a note
  (`_tree_framing_mutant`, lines 1487-1495). The 0-failing battery therefore
  includes one case that no longer runs after the sitting.

Fix:

- Cite the record that carries the result (the bead close reason), or retain
  the report beside the brief.
- Name the base head the scratch was built from.
- Say "Steps 3 to 10 and the `python3` lines of step 11".
- Under "What it does not cover", add that the reconciliation selftest's P-95
  case is skipped, not passed, once B is recorded.

### 4 — Sentences that still describe pre-answer or pre-merge state without a marker (note)

Anchor and evidence:

- Lines 177-178 and 182. "Recommended: ask for round 7 now, before the
  sitting…" and "**Your words now:** 'Run round 7 on screening scope version
  2.'" Round 7 has run (finding-free check above), and the dated note sits only
  in the "Its state" bullet. This routes the owner to an offering that is
  already spent.
- Lines 196-198. "…declarations … that belong to the gate, which is not written
  yet." `bd show syzygy-qkea.4` is CLOSED ("PR #375 merged (8df5be2a): S3
  preflight/init gates"), and `gate-sources.ts` lines 141-159 now refuse an
  entry that does not name the reader. The update at lines 40-42 does not reach
  this sentence. Whether the S3 gate is the whole of "the gate" is for the
  drafter to state.
- Line 78. The K row reads "No; 1.0 stays in force". K is recorded
  (`decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.1.md` exists), and the
  row has no marker. CG-27-style row scope means the K section's marker does
  not cover the table row.
- Lines 38-40. "S4 and S5 are in progress". The `syzygy-qkea.4` BLOCKS list
  shows S4 (`qkea.5`) and S5 (`qkea.6`) closed. The dated note defers to the
  beads, which is acceptable, but it names only S2 and S3.
- Line 433. "which lands with PR #370". PR #370 has merged.
- Lines 299-311. Section J sits before the K section's "Settled" marker and has
  none of its own, so its "Your words" reads as still to be asked.

Fix: add a dated note at each of these sentences, in the form already used at
lines 40-42, keeping the original text.

### 5 — "The re-derivation is tracked on `syzygy-2g0d`": that bead is closed (note)

Anchor: lines 136-137.

Evidence: `bd show syzygy-2g0d` gives "[P2 · CLOSED]", with the close reason
"PR 272 merged; package binds nothing, routed to owner via P-95". The
re-derivation appears only as a 2026-10-06 comment. A closed bead does not
surface as work in `bd ready`.

Fix: name an open bead that carries the re-derivation, or say it is recorded as
a comment on a closed bead and not yet tracked.

### 6 — The brief says "the words given below are the words that would be recorded", but gives no description for A to H (note)

Anchor: lines 85-89, and the "Your words" lines of A to H.

Evidence: every selection recorder requires `--question-opening`,
`--selection-label` and `--selection-description`
(`record_dossier_local_agent_acts.py` lines 732-737, and the installer's
`validate_answers`, lines 168-176). Only I gives a description. The rehearsal
filled A to H with its own synthetic description ("Perform the act at the
manifest row, as the sitting brief recommends.") and invented question
openings (simulator lines 58-86).

The installer also refuses any opening, label or description that contains
`': '`, `' #'` or `'` (line 175). The asker composing the questions should
know that.

Fix: give the description to be offered for each of A to H, or say that the
asker supplies it. Note the character constraint for the question openings.

### 7 — "the first four are met" counts a list of four (note)

Anchor: lines 416-419.

Evidence: the preconditions are round 7, PR #370, PR #367 and the installer,
which is four. "The first four are met; the installer merged in PR #376" reads
as though the installer were a fifth.

Fix: "all four are met (the installer merged in PR #376)."
