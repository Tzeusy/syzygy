# R-REDIS-LOCAL-AGENT-SITTING-BRIEF-2 — raw review
Subject: .syzygy/governance/contracts/candidates/REDIS-LOCAL-AGENT-SITTING-BRIEF.md
Subject SHA-256: d057ea0e0fdfc60cc33bd30a42810f5f65f04b077f45f4a5138041547b2b0cdc
Verdict: REVISE
Reviewed commit: a16de5cc

## Method

Fresh-context review, 2026-10-07, worktree
`/home/tze/GitHub/syzygy/.worktrees/parallel-agents/sitting-brief`, HEAD
`a16de5cc`. `sha256sum` on the subject printed the digest above before any
other step; it equals the digest in the brief. I read the subject in full, the
round-1 raw (`docs/reviews/R-REDIS-LOCAL-AGENT-SITTING-BRIEF-1-RAW.md`), and
`git diff 8dd0d589 a16de5cc` (one file changed: the subject, +93/-33). I read
the rehearsal record
`docs/evidence/redis-local-agent-sitting-rehearsal-2026-10-07.json`, and opened
the entry candidate JSON, `scripts/install_redis_local_agent_sitting.py`,
`scripts/build_pwb_behavior_contract_repin_tree_framing.py`,
`scripts/check_spec_reconciliation.py`, `packages/polaris-dossier/src/gate-sources.ts`,
the P-95 `OWNER-DECISION-PACKET.md`, the sitting direction, `security.md` and
the local-agent proposal. I ran `git merge-base --is-ancestor`, `git log` and
`git diff --stat` over the commits named, and `bd show syzygy-qggu`. No network
call, no `gh`, no content of any external repository. I did not re-run the
rehearsal. I edited nothing except this file. Line numbers refer to the subject
at `a16de5cc`.

Checks that passed (no finding):

- Entry clause, byte for byte. The brief's quotation at lines 239-241 ("implementationVersion 1.0.0 names that file
  as merged, and any change to it is a new implementation version and a new
  version of this entry.") is a substring of `implementationStatus`,
  `public-git-source-acquisition-local-agent/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json:14`
  (grep -F hit). "the entry still says 'not yet implemented'" (line 229) matches
  "is not yet implemented" in the same field.
- `8422119c` is the only change to `packages/polaris-dossier/src/git-object-reader.ts`
  after `ff7e5123` on the first-parent line to `a16de5cc` and to `origin/main`.
- Rehearsal base. `8c556f08` has `ff7e5123` (PR #367 merge), `ddbb78eb` (PR #370
  merge) and `8422119c` as ancestors (`merge-base --is-ancestor`, exit 0 each).
  The record's `baseHead` is `8c556f08…`, `merged` is `[]`, and its `answers`
  step notes "v1.1 already recorded on the base". `git diff --stat 8c556f08
  a16de5cc -- scripts/` and `… origin/main -- scripts/` each touch only
  `check_docs_review_campaign_partition.py`, so the six PR #376 scripts are
  unchanged as the brief says (line 504).
- Rehearsal results. The record shows nine `recorded:` lines (steps 3 to 9), the
  install-check output "recorder checks failing: none" / "not installed: none",
  `"commands": 91, "failing": 0`, and governance "32 OK, 21 WARN, 0 FAIL". The
  synthetic description "Perform the act at the manifest row, as the sitting
  brief recommends." is in the record, as the brief says at lines 505-507.
- "Six failing battery lines with four causes" (lines 520-530) is supported by
  commit `0a2edd64`'s message ("Rehearsal 4 found six battery failures after
  install"), which lists the three fixes the brief names and the reconciliation
  skip as the fourth.
- Builder claims under B (lines 147-152). `check()` gathers findings over both
  `SUBJECTS` (lines 285-293); `apply()` refuses while `check()` has any finding
  (lines 328-333: "refusing to apply: the package does not verify"); the module
  docstring lines 45-47 say the manifest file "carries both act arguments as
  rows" and line 53 that `--write` "changes both act arguments and retires any
  review bound to the old one".
- Direction C (lines 152-155). P-95 `OWNER-DECISION-PACKET.md` lines 134-138
  name `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md` as the
  policy role's expected supersession target.
- `syzygy-qggu` (line 158) is OPEN, titled "Re-derive the P-95 tree-framing
  re-pin package over the v2 policy bytes after the Redis local-agent sitting",
  and its description carries B and D, both acts' review binding and C.
- Character rule (lines 96-99). `install_redis_local_agent_sitting.py` lines
  168-176 require one line and no 64-hex digest for every field, and refuse
  ": ", " #" and "'" for every key except `v1.1` and `entry-v1.0`.
- D9 quotation (line 379) matches `security.md` lines 78-79 across the wrap.
  "A Redis dossier needs both" (line 315) is at `proposal.md` lines 112-113
  across the wrap.
- No digest. The subject carries no 64-hex token; the hex tokens it carries are
  8-character commit prefixes.
- VIS-4. Nothing in the subject performs, adopts or signs. "signed off" for 1.0
  and 1.1 and the "Answered" banner report records that exist.

## Round-1 repairs

| Round-1 item | Status | Evidence |
|---|---|---|
| 1 (revise) E said a later reader repair is approved by the same sign-off | **partly** | The false sentence is gone; the entry's clause is quoted exactly (lines 239-241); `[Unknown]` is stated (line 243); the reading is put to the owner (lines 247-255). Round 1's fix also asked that, if `8422119c` counts, "E is offered at a version that names the reader as it stands on main". That part is not done: the recommendation stays v1.0 under either answer, and the brief does not say what answer (a) does at the sitting. See finding 1. |
| 2 (revise) "P-95's act B is not affected" | repaired | Lines 147-159 state the package-as-unit refusal, retirement of both acts' review binding, C's redraft, and label the registry bytes `[Inferred]`. Each claim checks against the builder and the P-95 packet (above). |
| 3 (note) rehearsal claim rests on no retained record | repaired | The record is retained and cited (line 499); base head named (lines 501-502); "Steps 3 to 10, and the `python3` lines of step 11" (lines 496-497); the skipped P-95 case is disclosed (lines 516-518). Residual on labels: finding 3. |
| 4 (note) unmarked pre-answer/pre-merge sentences | **partly** | Marked: slices (40-43), D's recommendation and "now" words (201-203, 208-209), E's gate (225-229), table rows J-M (78-81), step 8 (477-478). Not marked: the section J body (finding 2). |
| 5 (note) `syzygy-2g0d` closed | repaired | Line 158 names `syzygy-qggu`, open. |
| 6 (note) no description for A-H; character rule | repaired | Note at lines 92-99. |
| 7 (note) "the first four are met" | repaired | Line 462: "all four are met; the installer merged in PR #376". |

## Findings

### 1 — E's new question does not say what answer (a) does at the sitting, and E's "Declining costs" understates the cost under the installer as merged (revise)

Anchor: lines 218, 247-258.

Quoted bytes:

- Line 218: "**Declining costs:** no read; a later sitting for this one act."
- Lines 247-255: "(a) the reader as PR #367 merged it, so `8422119c` needs a new
  implementation version and a v1.1 of the entry before E describes the
  reader on `main` … The recommendation below is unchanged; this question is
  asked first."
- Line 256: "**Recommended:** sign, once PR #367 has merged."

Evidence:

- Only v1.0 can be signed. The entry package holds one proposed file
  (`ls -R public-git-source-acquisition-local-agent/`: `SEMANTIC-DELTA.md`,
  `proposed/…CANDIDATE.json`). The installer hard-codes it:
  `install_redis_local_agent_sitting.py:283`
  `("public-git-source-acquisition-local-agent", "1.0", ENTRY_REVIEW, ENTRY_NOTES)`.
- E is required for the whole install. Line 126:
  `REQUIRED = ("screening-v1", "redis-observation", "entry-v1.0", "rfc7-20-reading-in-force", "profile")`;
  lines 157-159 append "no answer for entry-v1.0: a local-agent run needs it,
  and an act is never inferred" to the refusal reasons, and the docstring (lines
  29-33) says it requires these "Before anything is written". So with no E
  answer, the one-command step 10 records none of B, C, D, A, F, G, H or I.
  Line 218's "a later sitting for this one act" is not what happens with the
  tool the brief routes the owner to.
- Signing v1.0 under (a) is not checked by anything. `gate-sources.ts:157-161`
  reads `implementationId` and refuses only a missing or blank
  `implementationVersion` string; no reader bytes are compared. So under
  reading (a), a signed v1.0 lets the gate admit runs of the reader at
  `8422119c`, which that reading says v1.0 does not cover. The owner is not told
  this.
- The answer has no recording path. The installer's E answer has a single
  `quote` field (line 168). The brief gives no words for the question, and does
  not say that the owner's reading should go into E's quote. So no record will
  show which meaning of "as merged" the v1.0 sign-off was given under.
- [Inferred] With the recommendation "unchanged" under both answers, an owner who
  answers (a) is left choosing between three things the brief does not name:
  - sign v1.0 for a reader that, by their own reading, it does not describe;
  - decline E, which stalls the whole install;
  - wait for an entry v1.1 that does not exist and that no bead is named for.

Fix:

- Under the question, state the consequence of each answer at this sitting.
  - (b): sign v1.0 as recommended.
  - (a): state whether to sign v1.0 now (and that the gate does not check the
    reader bytes), or to hold E. If E is held, say that the installer refuses
    every act until E is answered, or that the installer must change first.
    Name the bead for the v1.1 entry.
- Say how the answer is recorded, for example in E's quoted words, which the
  installer allows to carry free text.
- Correct line 218 so that it matches the installer's `REQUIRED`.

### 2 — Section J's body still reads as a question to ask (note)

Anchor: lines 343-355.

Quoted bytes: "Plain directions; no review needed; each has a lawful default." …
"**Your words:** "10a no ruling; 10b maintainer-stated only; 10c after the
first run.""

Evidence: the J table row is now marked (line 78, "Settled 2026-10-07 by
direction; not asked again."). The section body has no marker of its own. The
only marker that names J is in section K (lines 359-362: "Items J to M are not
asked again"), which comes after J's "Your words". Round 1, note 4, last bullet,
named this section. The same is true of section M (lines 416-432); it is
covered by K's marker above it, so M is acceptable.

Fix: add the dated "Settled 2026-10-07 by direction; not asked again" marker at
the head of section J.

### 3 — Two `[Observed]` claims cite the rehearsal, but the retained record does not carry them (note)

Anchor: line 142 ("**Why** [Observed in the 2026-10-07 rehearsal]: … After the
sitting, that package's builder refuses against the policy on disk.") and lines
516-518 ("the reconciliation selftest no longer builds the P-95 package, and
says so in its output").

Evidence:

- The record's `steps` hold no reconciliation-selftest output and no builder
  refusal, and its `findings` is `[]`.
- The skip is observable in the code. `check_spec_reconciliation.py:1490-1495`
  prints "note: pins-after-tree-framing-repin-acts not run: the package does
  not build over this tree …".
- The finding itself is reported in commit `0a2edd64`'s message (rehearsal 4).
  That was not the rehearsal the retained record describes.
- The paragraph at lines 520-530 ("An earlier run found six failing battery
  lines…") cites nothing. `0a2edd64` supports it.

The claims are true as far as I can check. The label names a record that does
not hold them (rule 11).

Fix: label these "[Observed in the checker and rehearsal 4, commit `0a2edd64`]",
or retain the selftest output beside the record. Cite `0a2edd64` for the
earlier-run paragraph.

### 4 — The superseded quotation and current guidance share one paragraph (note)

Anchor: lines 532-538.

Quoted bytes: "…Rehearse in a scratch clone before the sitting."" followed on the
next line, with no blank line, by "The order of steps 1 and 9 matters for the
status page's composition figure: …".

Evidence: in Markdown, lines 532-538 form a single paragraph. The current
statement about the order of steps 1 and 9 therefore renders inside the
paragraph that opens "The superseded sentence, kept as written before the
rehearsal". A reader may take it as part of the superseded text.

Fix: insert a blank line before "The order of steps 1 and 9".

### 5 — E's "Your words" calls the quote an option label (note)

Anchor: lines 257-258 and 96-99.

Quoted bytes:

- Line 257: "**Your words:** option "Extend Scope A to this entry and sign v1.0".
  The recorder refuses a label that does not contain "Extend Scope A"."
- Line 99: "E is recorded from your quoted words instead."

Evidence: the installer passes E as `--owner-selection-quote` (line 286), and
refuses on `ans.get("quote")` (line 181). There is no label for E. The two
passages describe the same input in two ways.

Fix: in line 257, say "quote" in place of "option" and "label".
