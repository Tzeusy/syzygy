# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-7 — screening scope v2 review, round 7 (narrow delta)
Reviewed commit: be724397b9a1a72837eb2c7811efd356f5c010de
Manifest SHA-256: 7757e70c4d0e8e65c19c77f4970853967456cdd7f225077feac1f91e16200e1e
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer method: I am a fresh-context governance reviewer (Claude Opus 5.5), dispatched by the lead on the owner's direction of 2026-10-07 ("run round 7 on screening scope version 2 now"). I ran `git fetch origin` and then worked only in a local clone (`git clone --no-checkout` of this repository) under my scratchpad, checked out at origin/main be724397. I read the repair diff `git diff 8a0bb2a1 e7ad7934` over the package and the builder. I ran the builder's `--check`, `--selftest`, `--ready --pending-prerequisite` and `--manifest-digest --pending-prerequisite`, the recorder's `--selftest` and `scripts/check_governance.py`. I applied six source mutants to the builder in the clone, ran `--selftest` and `--check` on each, and restored the file; `git status --porcelain` in the clone was empty at the end. I ran 21 probe paths through the builder's reference reader (`classify_documentation`) under all four variants' rules. I called no model provider, read no external repository body, made no network call other than git fetch, and edited no file in the repository. The manifest digest above was computed by `sha256sum` on the manifest file at be724397. It matches the digests at 8a0bb2a1 and e7ad7934 and the value printed by `--manifest-digest --pending-prerequisite`.

## Checks run (this session, at be724397)

- [Observed] `--check` printed "public-source screening scope v2: current".
- [Observed] `--selftest` printed "selftest: 116 of 116 predicates held".
- [Observed] `--ready --pending-prerequisite` printed "current" and two NOTE lines: the class is not in the installed RFC-0005 text, and the version-1 act is not recorded. This is the same as round 6.
- [Observed] The manifest file's SHA-256 is 7757e70c4d0e8e65c19c77f4970853967456cdd7f225077feac1f91e16200e1e at 8a0bb2a1, at e7ad7934 and at be724397 (`git show <c>:<manifest> | sha256sum`, three runs). The repair leaves the manifest unchanged, as ROUND-6-DISPOSITIONS.md:26-27 states.
- [Observed] Recorder `--selftest` printed "selftest: 70 of 70 predicates held".
- [Observed] `check_governance.py` printed "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] The repair population is as stated. `git diff --shortstat 8a0bb2a1 e7ad7934 -- <package> <builder>` reports "3 files changed, 20 insertions(+), 13 deletions(-)": the packet, the semantic delta and the builder (ROUND-6-DISPOSITIONS.md:23-27; packet:9-11).
- [Observed] Main carries these commits under other hashes after rebase-merge. `git diff 8a0bb2a1 e8c482a9` and `git diff e7ad7934 f04fc596`, over the package, the builder and the recorder, are both empty. So the round-6 reviewed bytes and the repair bytes are both on main.
- [Observed] Later commits are covered or outside the reviewed paths. `git diff e7ad7934 be724397` over the package, the builder and the recorder touches four files. Two are new: the round-6 raw and ROUND-6-DISPOSITIONS.md. One is the packet, and only its review-state statement (packet:7-14) changed. The fourth is the recorder (`--freeze`, commits 8df9729c, ba3a371a, 8931e9ab). No repair commit after e7ad7934 touches the builder, the patches, the manifest, the delta or the generated block.
- [Observed] Criterion 8 holds. A 64-hex sweep over the 10 package Markdown files outside `reviews/` found 0 tokens. The words accepted and approved appear only at REVIEW-BRIEF.md:57, the criterion that forbids them, and adopted appears nowhere. The generated blocks in the packet and the delta are byte-identical.

## Round-6 findings against the bytes

**R6-1: repaired.** [Observed] Packet:44 and SEMANTIC-DELTA.md:75 now read "a file directly inside a top-level licenses folder and ending .md or .txt is mapped whatever its stem unless a word above withholds it". The suffix text is generated from `LICENSE_TREE_SUFFIXES` (builder:599). Under all four variants, the reader withholds licenses/LICENSE, licenses/COPYING, licenses/README, licenses/README.rst and licenses/sub/README.md. It maps licenses/README.md, licenses/LICENSE.txt, licenses/LICENSE.MD and LICENSES/NOTICE.TXT. The clause now agrees with packet:36 and packet:45. The four new withheld fixtures are at builder:210, and the below-the-root predicate checks them and the suffix text (builder:808-817). Mutants: removing the suffix clause (M6) and hard-coding it to ".md" (M7) each fail `--selftest` (115 of 116) and `--check` (STALE).

**R6-2: repaired.** [Observed] The guard (builder:804-806) now uses sub/Guide. The reader maps docs/sub/Guide.md and withholds licenses/sub/Guide.md in all four variants, and the predicate asserts both halves. Round 6's surviving mutant M4, which drops `LICENSE_TREE_ROOTS[0]` from the default roots at builder:556, now fails `--selftest` (115 of 116). It still passes `--check`, which is expected, because it changes no generated text.

**R6-3: repaired.** [Observed] Builder:809 matches each tree name by `(?<![A-Za-z])name(?![A-Za-z])`. Round 6's surviving mutant M5 rewrites the line to "outside docs …", dropping "doc". It now fails `--selftest` (115 of 116), as well as `--check`.

**R6-4: repaired.** [Observed] Packet:57-58 now reads "A recorder, frozen only after a confirming review, takes the chosen row", and packet:90-92 reads "the recorder refuses a second variant act over this manifest unless it is a declared superseding version". The recorder selftest holds "a second variant act refused while another variant is in force" and "a second variant act in the same tree is refused and writes nothing". The recorder is still unfrozen (`FROZEN_SUBJECT` None), so "frozen only after a confirming review" is true at these bytes.

**Nothing broken by the repair.** [Observed] The repair changes no policy byte, patch or manifest row. The only other code change is the `examples_hold` signature, whose default `roots` is the previous pair. It is called at three sites, and the sentence predicate's results are unchanged (116 of 116). Two further mutants change only the tests: M8 drops the positive half of the sub/Guide guard, and M9 reverts the whole-word regex to a substring test. Both survive. That is expected, because neither changes the subject. M5 shows that the regex is what catches a dropped "doc".

## Findings

**Finding 1 — the review brief was not updated for round 7** (note)

- [Observed] REVIEW-BRIEF.md:1 still says "round 6, narrow delta". Its recording section (REVIEW-BRIEF.md:103-104) names `R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-6-RAW.md`. No criterion covers R6-1 to R6-4. The last criterion, REVIEW-BRIEF.md:85-94, covers the round-5 diff.
- [Inferred] This round's scope came from the lead's dispatch, so the review was not misdirected. The recorder's `--freeze ROUND COMMIT` takes the round number as an argument (recorder:862-884), so the stale raw name does not block recording. The brief is one of the files `FROZEN_FILE_DIGESTS` hashes (recorder:153), so whatever the brief says at the freeze commit is what gets frozen. Proposed: add a round-7 criterion and raw name in the same commit that retains this raw, or record in ROUND-7-DISPOSITIONS.md that the dispatch stood in for the brief.

**Finding 2 — Q4's default overstates which READMEs under docs and licenses are mapped** (note)

- [Observed] Packet:114-116 gives the default as "the root README, and a README under the docs or doc folder or directly under the licenses folder". Under all four variants the reader withholds docs/README, licenses/README and licenses/README.rst, and maps docs/README.rst and doc/README.md. A README under docs is mapped only with .md, .rst or .txt, and one directly under licenses only with .md or .txt.
- [Inferred] This is the same shape as R6-1, but in hand-written question prose outside the generated block, and it predates the round-5 and round-6 diffs. The error runs toward overstating, which fails closed. SEMANTIC-DELTA.md calls the generated lists the only statement of what is sendable, and those lists are now correct. Proposed: "a README ending .md, .rst or .txt under the docs or doc folder, or ending .md or .txt directly under the licenses folder".

**Finding 3 — the review-state statement says round 6 "confirmed" the policy bytes** (note)

- [Observed] Packet:8 reads "the policy bytes were confirmed correct". The round-6 raw's verdict is REVISE (R-…-6-RAW.md:4). Its statement about the policy bytes is labelled [Inferred] ("The policy bytes are correct and fail closed", raw:47). Its [Observed] statement is narrower: no new weakening in the round-5 change (raw:78).
- [Inferred] "Confirmed" reads like a verdict word, and no round has confirmed these bytes. Proposed: "round 6 found the policy bytes correct". The statement sits outside the generated block, and the next round's review-state edit will replace it anyway.

**Finding 4 — "ending .md or .txt" omits "longer than it"** (note)

- [Observed] The reader withholds licenses/.md and licenses/.txt, because the licenses-tree rule requires a name that "ends with one of licenseTreeSuffixes and is longer than it" (builder:278-279, and the policy bytes). Packet:36 and packet:44 say only "ending .md or .txt".
- [Inferred] This is a degenerate edge, it fails closed, and the policy bytes are exact. No repair is needed. It is recorded so that a later reader does not count it as a contradiction.

**Finding 5 — `--freeze` hashes the packet as it stands at the freeze commit, not as reviewed** (note)

- [Observed] `do_freeze` (recorder:862-893) reads the raw, the manifest and the frozen table from the commit it is given. `raw_head_binds` (recorder:850) checks only the manifest file digest and the verdict, not that the raw's reviewed commit carries the same packet bytes. The table covers the packet, the delta, the brief and the ledger (recorder:153). Every round so far has edited the packet's review-state statement after the review, in the commit that retains the raw (080d76f0 did so for round 6).
- [Inferred] So the frozen packet will carry a review-state statement that no round read. The act's subject is the manifest row, and the generated block is checked by the builder, so this does not change what is signed. The owner nonetheless reads prose that is outside any review. This is outside this round's narrow scope and is offered as a disclosure. If the freeze commit is the one that retains this raw, keep the statement edit to a dated sentence naming this raw and its verdict.
