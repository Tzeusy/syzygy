# R-REDIS-LOCAL-AGENT-SITTING-BRIEF-3 — raw review
Subject: .syzygy/governance/contracts/candidates/REDIS-LOCAL-AGENT-SITTING-BRIEF.md
Subject SHA-256: 75b703d49c5f83a777ac940de2c9f1e1b279488bf130ec0290ea81adec330f4b
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 6568ed95

## Method

Fresh-context review, 2026-10-07, worktree
`/home/tze/GitHub/syzygy/.worktrees/parallel-agents/sitting-brief`, HEAD
`6568ed95`. Before any other step I ran `sha256sum` on the subject. It printed
the digest above, which equals the digest in the brief. I then read:

- the round-2 raw (`docs/reviews/R-REDIS-LOCAL-AGENT-SITTING-BRIEF-2-RAW.md`);
- `git diff 2ca610d3 6568ed95`, which changes one file, the subject;
- the subject in full;
- `scripts/install_redis_local_agent_sitting.py` in full.

I checked each repaired sentence against the bytes it cites:

- `registryEntryUsable` in `packages/polaris-dossier/src/gate-sources.ts`
  (lines 146-165);
- the `Owner selection:` line and `validate_inputs` in
  `scripts/record_versioned_signoff.py` (lines 320-333 and 546);
- `_tree_framing_mutant` and `POLICY_SCOPE_ACT` in
  `scripts/check_spec_reconciliation.py` (lines 1479-1495), and the record
  file name in `scripts/record_public_source_screening_scope_act.py:124`;
- the message of commit `a3ef4d98`;
- `bd show syzygy-stgw`;
- the last section of `decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md`.

I also ran:

- `git merge-base --is-ancestor a3ef4d98 origin/main` and the same against
  `6568ed95`, both exit 0;
- `grep -rn -F "git-object-reader"` over `packages/polaris-dossier/src` and
  `scripts`, which found 15 files. I opened the non-test hits that could check
  reader bytes: `init.ts`, `reverify.ts`, `clone-head.ts`, `gate-sources.ts`
  and `build_public_git_source_acquisition_local_agent.py`;
- `grep -c -E "[0-9a-f]{64}"` on the subject, which returns 0.

I made no network call, used no `gh`, and read no content of any external
repository. I re-ran no rehearsal. I edited nothing except this file. Line
numbers refer to the subject at `6568ed95`.

## Round-2 repairs

| Round-2 item | Status | Evidence |
|---|---|---|
| 1 (revise) E's question did not say what answer (a) does; "Declining costs" understated the cost | **repaired** | See the four rows below. |
| 1, the (a) branch | | Lines 271-283 state what each answer does at the sitting. Lines 274-275 name the v1.1 bead. `bd show syzygy-stgw` shows the bead OPEN and titled "Draft public-git-source-acquisition-local-agent entry v1.1 naming the reader at 8422119c, if the owner reads 'as merged' as PR #367's merge". |
| 1, the gate claim | | Lines 276-280 say the gate does not check the reader's bytes. `gate-sources.ts:158-163` compares `implementationId` with `DOSSIER_READER_IMPLEMENTATION_ID` and refuses only "no implementation version (Unknown)". The builder checks only that `IMPLEMENTATION` "is absent" or present (`build_public_git_source_acquisition_local_agent.py:243-244`). No hit I opened compares the reader's bytes. |
| 1, the recording path | | Lines 284-290 say how the reading is recorded. `record_versioned_signoff.py:546` writes "Owner selection: {quote}". `validate_inputs` (lines 325-333) accepts the example quote: it is one line, carries no digest, and contains "Extend Scope A". |
| 1, "Declining costs" | | Line 218 was corrected at the sentence, dated (lines 231-234). The new paragraph at lines 101-110 maps correctly onto `REQUIRED` and the installer's other refusals. Residue in notes 1 and 3. |
| 2 (note) section J body had no marker | **repaired** | Lines 382-383: "*(Settled 2026-10-07 by direction; not asked again. The text below is kept as offered.)*" |
| 3 (note) `[Observed]` labels cited a record that does not hold them | **repaired** | See the two rows below. |
| 3, the cited commit | | Lines 153-155 and 561-562 now cite `a3ef4d98` on `main` (ancestor of `origin/main`, exit 0). Its message reads "Rehearsal 4 found six battery failures after install" and "check_spec_reconciliation.py: the tree-framing re-pin mutant is skipped, said aloud, only once the screening v1 act supersedes the policy act that package re-pins from". |
| 3, the code and the report | | "once B is recorded" matches the code: `check_spec_reconciliation.py:1490` skips only when `POLICY_SCOPE_ACT` is a file, and that is the record that `record_public_source_screening_scope_act.py:124` writes. Lines 558-559 now say the retained report does not hold the output. The commit differs from the round-2 raw's `0a2edd64`; both carry the same subject line, and the cited one is on `main`, which is the better citation. |
| 4 (note) the superseded quotation and current guidance shared a paragraph | **repaired** | Line 578 is blank, so line 579 starts its own paragraph. |
| 5 (note) E's words called the quote an option label | **partly** | Lines 286 and 293-295 now say "E has no label field" and "the selection quoted as". The new line 284 brings the word back: "let the option you select name your reading". See note 2. |

Checks that passed (no finding):

- **The new paragraph against the installer (criterion 1).**
  - `REQUIRED = ("screening-v1", "redis-observation", "entry-v1.0", "rfc7-20-reading-in-force", "profile")`
    (line 126) is B, A, E, H and I.
  - `DRAWER_OR_PROVIDER = ("redis-no-evidence-drawer", "redis-agent-anthropic", "redis-agent-openai")`
    (line 125) is F and its 3a and 3b.
  - `"screening-v2" in acts and "rfc5" not in acts` (line 162) is "signing D
    while declining C is refused".
  - `rfc5`, `screening-v2` and `d9-in-force` are optional (docstring lines
    35-36), which is C, D and G.
  - `record_and_install` validates before it writes and prints "REFUSED
    (nothing written)" (lines 538-545), which supports "refuses before
    writing anything".
- **E (a) and the installer.** "an installer change to sign it" (line 283)
  is supported. The installer hard-codes
  `("public-git-source-acquisition-local-agent", "1.0", ENTRY_REVIEW, ENTRY_NOTES)`
  (line 283) and refuses without an `entry-v1.0` answer (lines 157-159).
- **VIS-4.** Nothing in the repaired text signs, adopts or performs. Each
  answer is stated as the owner's ("it is your question, not this page's";
  "This question is asked first"). The recommendation is conditional on the
  owner's reading (lines 291-292), not on the brief's own choice.
- **No digest.** The subject carries no 64-hex token. The commit prefixes
  are 8 characters.
- **Labels.** Each new substantive claim carries a label: [Observed] at lines
  103 and 276, and the rehearsal-4 label at line 153. Line 267 keeps its
  [Inferred].

## Findings

### 1 — The new paragraph cites `REQUIRED` for refusals that two other predicates make, and its last clause does not say how far the refusal reaches (note)

Anchor: lines 101-110.

Quoted bytes: "[Observed] the installer
(`scripts/install_redis_local_agent_sitting.py`, `REQUIRED`) refuses before
writing anything unless it has answers for A, B, E, H and I, and for one of
F's options. … C, D and G may be declined without that effect, except that
signing D while declining C is refused (D's policy maps a class only C
defines)."

Evidence:

- `REQUIRED` (line 126) holds A, B, E, H and I only. The F clause rests on
  `DRAWER_OR_PROVIDER` and the check at lines 160-161. The D-without-C
  clause rests on line 162 ("screening-v2 needs rfc5"). Each claim is true,
  but the cited identifier is not the clause for two of them (rule 8).
- "is refused" does not say what is refused. In `validate_answers` the
  D-without-C reason is one more entry in `why`, so the whole run is refused
  and nothing is written: the same effect as declining A. Read after
  "without that effect, except", the clause can be taken to mean that only D
  fails.
- [Inferred] "the others wait for a later sitting or a changed installer"
  names two routes. Steps 3 to 9 of "After the sitting" still show each
  recorder's own `--record` command with no remark that they are run only
  through the installer. A reader holding E could take those commands as a
  third route. The brief does not say whether running them by hand, without
  step 10's registrations and battery lines, is lawful or would leave the
  battery passing.

Fix:

- Cite `REQUIRED`, `DRAWER_OR_PROVIDER` and `validate_answers`.
- Write "signing D while declining C refuses the whole run in the same way".
- Optionally, say whether steps 3 to 9 may be run by hand.

### 2 — Line 284 calls E's quote "the option you select" (note)

Anchor: line 284.

Quoted bytes: "**If you sign**, let the option you select name your reading, … E
has no label field: the installer passes your selection as one quoted line".

Evidence: round-2 note 5 asked that E stop being described as an option or
a label, because the installer passes it as `--owner-selection-quote`
(installer line 286). Line 293 now follows that. Line 284, added in this
repair, says "option" in the sentence just before it says there is no label
field. This is harmless to the act: the recorder writes whatever quote is
given.

Fix: "let your quoted selection name your reading".

### 3 — "nothing else in this brief depends on its timing except step 7" is now false under the installer and is not marked at the sentence (note)

Anchor: lines 250-251.

Quoted bytes: "If PR #367 has not merged by the sitting, this row waits; nothing
else in this brief depends on its timing except step 7 below."

Evidence:

- The new paragraph (lines 103-107) says that holding E means "step 10
  records no act at this sitting".
- The installer refuses an `entry-v1.0` answer while the reader is absent
  ("offer the entry only after PR #367 merges", line 236), and refuses any
  run with no `entry-v1.0` answer (lines 157-159). So under the installer as
  merged, every act at the sitting depended on PR #367's timing, not only
  step 7.
- The dated update below the sentence (lines 252-262) marks the merge. It
  does not mark this dependency claim.
- The condition is spent, because PR #367 has merged, so the sentence
  misleads no one about the current sitting. It is still a false sentence
  standing unmarked on a page whose own rule is to mark at the sentence
  (lines 24-25).

Fix: add a dated marker after the sentence, for example: "*(Corrected
2026-10-07: under the installer as merged, every act at the sitting waited
on this, since the installer requires E.)*"
