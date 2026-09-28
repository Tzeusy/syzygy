# History review 3 — reconciliation recorder

Verdict: REVISE
Reviewed commit: e6d06bcd6045aa37e97a656919ea1ab03103147b
Reviewer: independent fresh-context agent, 2026-09-28

Recorder bytes reviewed (sha256 computed by sha256sum at the reviewed commit, over both `git show` and the checked-out file, which agree):

- `scripts/record_polaris_understanding_adoption.py`: `65ebe0ed08b37478e5ee87a2032b65e69fee43dc36b73135d36710b058f3e4f5`

## Scope

Subject: `git diff a9a0830 e6d06bc -- scripts/ HISTORY-READING.md history-reading-rule6.json PROJECT-STATUS.md`,
round 3 after History review 1 (REVISE, M1 plain deletion, M2 untested
predicates) and History review 2 (REVISE, M1 rename-in and merge-drop).
Governing references read: owner ruling "R1: read as history"
(`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md:27`), the reconciliation
package `README.md` and `REVIEW-RAW.md`, and the `CONFIRM CRAFT AMENDMENT:
CC-SPEC@` lines of `ACCEPTANCE-ACT-RECORD.md`. Every experiment ran in a
scratch clone of the worktree checked out at the reviewed commit; the reviewed
worktree was not modified. The scripts at c58ef3e (the rule-6 JSON's recorded
commit) and e6d06bc are identical [Observed: `git diff --quiet c58ef3e e6d06bc -- scripts/` exit 0].

## Facts established

- [Observed] CC-SPEC at C1 (`9322656d…`, the `REVIEW-RAW.md` reviewed commit)
  hashes to the digest on `ACCEPTANCE-ACT-RECORD.md:95`, one of exactly two
  anchored `CONFIRM CRAFT AMENDMENT: CC-SPEC@` lines (66, 95).
- [Observed] `--selftest` exits 0: "49 trust-boundary mutations refused" and
  "PASS history population selftest: 2 real-Git cases". `--check` fails with
  "latest history review not confirming: …HISTORY-REVIEW-2-RAW.md", as the
  brief expects.
- [Observed] `python3 scripts/check_governance.py`: 31 OK, 21 WARN, 0 FAIL
  (52 checks). `--selftest`: 328 fixtures, 0 failing.
- [Observed] All 19 mutants in `history-reading-rule6.json` re-run on the
  reviewed bytes: each `old` fragment occurs exactly once, each mutant makes
  `--selftest` exit 1, and each output contains the recorded refusal text.
  The JSON is accurate.
- [Observed] Base positive path: committing `HISTORY-REVIEW-3-RAW.md` with
  `Verdict: CONFIRM` and the current recorder digest makes `--check` PASS.
- [Observed] Round-2 M1 reproductions (rename-in then delete; side-branch raw
  dropped by an `-s ours` merge) are now refused. The real-Git selftest covers
  both, and mutants 17-18 show that each flag is load-bearing.

## Criterion 1 — CC-SPEC read at C1, performed digest required

Met. [Observed] POLICY is in `HISTORY_PATHS` (script line 227), so it is
skipped by the today's-bytes comparison. Lines 473-474 require the C1 blob's
digest to be among the anchored `POLICY_ACT` captures of the current
acceptance record, and the `Frozen` view (lines 477-481) reads POLICY at C1.
Mutants 1 and 13 test this.

## Criterion 2 — self-binding relaxed and compensated

Not met. Two fail-open paths remain in how history reviews are retained, and
both come from merge commits (M1). Ordering, numbering, verdict parsing,
binding parsing, the malformed-name refusal, the empty population and plain,
rename or merge-drop deletion are otherwise correct and exercised [Observed].

## Findings

### M1 — Material: a merge can replace or erase a committed non-confirming history raw, and `--check` passes

[Observed] Both reproductions start from the base passing state above
(raw 3 `CONFIRM`, committed).

1. **Same-numbered raw replaced through a merge.** On the main line, commit
   `HISTORY-REVIEW-4-RAW.md` with `Verdict: REVISE`: `--check` refuses
   ("latest history review not confirming"). A side branch forked from before
   that commit adds its own `HISTORY-REVIEW-4-RAW.md` with `Verdict: CONFIRM`
   over the same digest. Merge it, resolve the add/add conflict with
   `--theirs`, and commit: `--check` **PASS**. The REVISE commit stays
   reachable on the first-parent line (`git log --graph` shows 92592ec
   "raw4 revise" beneath the merge).
   - Cause, population side: the `--full-history --no-renames` population log
     lists raw 4 as added **twice**, once per branch. `history_reviews`
     collapses the list to a set (script lines 497-499 and 502), so the
     duplicate is never noticed.
   - Cause, retention side: `introduction` (line 277-282) still runs
     `git log --diff-filter=A HEAD -- <path>` with default history
     simplification. The merge is TREESAME to the side parent for that path,
     so the main-line add is pruned and one commit comes back. Its bytes
     equal today's, so "retained history review changed" (line 517) and
     "reintroduced evidence" (line 280) both stay silent.
   - [Inferred] This is the documented duplicate-dispatch incident in
     `AGENTS.md`: two leads got REVISE and CONFIRM WITH EXCEPTIONS over the
     same bytes. A conflict resolution that keeps one raw now silently
     discards the other verdict. Round 2 proposed applying the flags to
     `introduction` as well, and that was not done.
2. **A raw introduced by a merge commit, then deleted.** Make a merge
   (`--no-commit`) and add `HISTORY-REVIEW-4-RAW.md` (`REVISE`) in the merge
   commit itself: `--check` refuses ("history review not retained"). Then
   `git rm` it and commit: `--check` **PASS**.
   - Cause: `git log` shows no diff for merge commits by default, so neither
     the population log nor `introduction` ever lists the add.
   - [Inferred] This path is less likely than case 1, because the raw was
     never accepted as retained, but a committed REVISE is still defeated by
     deleting it.

`HISTORY-READING.md` states properties the code does not have:
- line 35: "Each raw's introducing commit holds the same bytes as today" (case 1 has two introducing commits, and only one is checked);
- lines 36-39: "every raw ever added on HEAD's history … so a deleted raw is refused" and "reads every commit and every merge parent" (case 2);
- lines 40-41: "earlier raws stay unchanged" (case 1).

Proposed fix, validated in the scratch clone on the unmodified check logic:
- Add `--diff-merges=combined` to the population log (line 273).
- In `history_reviews`, before the set is taken, require that each strictly
  named raw appears exactly once in the added list, with a refusal such as
  "history review added more than once".

With both changes:
- case 1 is refused "history review added more than once: …HISTORY-REVIEW-4-RAW.md";
- case 2 is refused "history review deleted: …HISTORY-REVIEW-4-RAW.md";
- the base state (the real e6d06bc history plus raw 3) still passes.

Two alternatives also work: give `introduction` the same flags and keep its
"reintroduced evidence" `<= 1` guard, or do both. Also:
- add both histories to `history_population_selftest`;
- add a rule-6 mutant for the duplicate check and one for `--diff-merges`;
- correct the three HISTORY-READING.md sentences.

### N1 — Note: round-1 findings N1 and N3–N6 still have no named disposition

[Observed] The "Review rounds" section (`HISTORY-READING.md:51-59`) covers:
- round-1 M1, M2 and N2;
- round-2 M1, N1 and N2.

It does not name round-1 N1, N3, N4, N5 or N6, or round-2 N3. Round-2 N3
asked for exactly this. The repairs exist in the prose:
- N1: lines 17-20;
- N3: lines 10-13;
- N4: lines 40-42;
- N5: lines 48-49;
- N6: lines 43-45.

Proposed fix: one line per finding naming its repair.

### N2 — Note: the malformed-name refusal is case-sensitive and top-level only

[Observed] The refusal (lines 492-495) keys on the literal prefix
`EVIDENCE + 'HISTORY-REVIEW'`. Two kinds of name therefore fall outside it:
- `History-Review-4-RAW.md` or `history-review-4-raw.md`;
- a raw in a subdirectory, such as `EVIDENCE/reviews/HISTORY-REVIEW-4-RAW.md`.

Such a raw is skipped silently rather than refused. Round-2 N1 proposed
case-insensitive matching; the repair took the prefix literally.
HISTORY-READING.md:31-33 describes the case-sensitive behaviour accurately.

Proposed fix: match the prefix with `re.I`, and refuse any path under
`EVIDENCE` that has a further `/` and a `HISTORY-REVIEW` basename.

### N3 — Note: two surviving mutants in the new guards

[Observed] Each survives its selftest (exit 0):

1. `reviews = sorted(set(added), key=number)` (line 502, dropping the on-disk
   population). An untracked higher-numbered raw is then ignored instead of
   refused as "not retained". Uncommitted raws bind nothing, so the effect
   is small.
2. In `check_governance.py` `_is_raw_review`,
   `HISTORY_REVIEW_RAW.fullmatch` → `.search`. That widens the exemption to
   any path containing the pattern, such as `x/docs/evidence/…/HISTORY-REVIEW-1-RAW.md.bak`.
   The four selftest cases have no prefixed or suffixed negative.

The other two exemption mutants are killed: the leading-zero form (`[0-9]+`)
and a wildcard directory. The exemption is narrow as written.

Proposed fix: add a negative selftest case carrying a suffix
(`…HISTORY-REVIEW-1-RAW.md.bak`). Optionally, add a fixture where an
untracked raw n+1 must be refused.

### N4 — Note: round-1/round-2 N2 (four inputs without a drift mutant) remains open

[Observed] This is disclosed at `HISTORY-READING.md:58-59` as predating the
change, and it is not weakened by it.

## Criterion 3 and 4 summary

- Round-1 M1/M2 and round-2 M1 are repaired for the cases they named
  [Observed]. The merge-commit cases in M1 above are new, not a regression.
- `--selftest`, `check_governance.py` and its `--selftest` pass. The rule-6
  JSON is accurate over all 19 mutants.
- HISTORY-READING.md matches the code except lines 35-41 (M1).
- The check_governance exemption is narrow and tested, with one survivor (N3).

## Housekeeping

[Observed] The reviewed worktree carries untracked sibling paths (a
spec-policy readability restyle package and scripts); this review neither read
them as subject nor touched them. The scratch clone's attack branches
(`base`, `attackA`, `sideA`, `attackB`, `sideB`) live only under
`scratchpad/histrev3/clone`.
