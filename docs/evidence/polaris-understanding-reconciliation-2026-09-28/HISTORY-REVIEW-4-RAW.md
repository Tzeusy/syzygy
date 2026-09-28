# History review 4 — reconciliation recorder

Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 3400e46774fc1f3ace85f6cf7dfa8466be23e877
Reviewer: independent fresh-context agent, 2026-09-28

Recorder bytes reviewed (sha256 computed by sha256sum at the reviewed commit):

- `scripts/record_polaris_understanding_adoption.py`: `6564084eeba4902f2877ba782b65f542d4a69a8a698aa7b51939a8bc18ebbad3`

## Scope

Subject: `git diff a9a0830 3400e46 -- scripts/ docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-READING.md docs/evidence/polaris-understanding-reconciliation-2026-09-28/history-reading-rule6.json PROJECT-STATUS.md`.
This is round 4, after History reviews 1, 2 and 3 (all REVISE).

Governing references read:
- the owner ruling "R1: read as history" in `OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`;
- the `CONFIRM CRAFT AMENDMENT: CC-SPEC@` lines of `ACCEPTANCE-ACT-RECORD.md`;
- the reconciliation package's `REVIEW-RAW.md`;
- the three prior history raws.

The sibling spec-policy restyle scripts in the diff range are outside this
recorder's subject and were not reviewed. Every experiment ran in scratch
clones (`exp1`, `pos`, `a1`–`a11`) beside the reviewed clone. The reviewed
clone was not modified: `git status --short` is empty.

## Facts established

- [Observed] The recorder at 3400e46 hashes identically from `git show` and
  from the checked-out file (digest in the head above). `scripts/` is
  byte-identical between 3f4a512 (the rule-6 JSON's recorded commit) and
  3400e46: `git diff --quiet` exits 0.
- [Observed] `--selftest` exits 0. Its three summary lines are:
  - "52 trust-boundary mutations refused";
  - "PASS history population selftest: 5 real-Git cases";
  - the pre-existing recorder pass line.
- [Observed] `--check` fails only with "latest history review not confirming:
  …HISTORY-REVIEW-3-RAW.md", as the brief expects.
- [Observed] `python3 scripts/check_governance.py` reports 31 OK, 21 WARN and
  0 FAIL over 52 checks. `--selftest` reports 328 fixtures, 0 failing.
- [Observed] Positive path, in scratch clone `pos`:
  - A committed `HISTORY-REVIEW-4-RAW.md` with the CONFIRM verdict and the
    current recorder digest makes `--check` PASS.
  - A further committed raw 5 with the CONFIRM WITH EXCEPTIONS verdict also
    PASSes.
- [Observed] Criterion 3 holds:
  - `POLICY_ACT` is anchored (`^…$`, `re.M`).
  - CC-SPEC at the C1 commit named by `REVIEW-RAW.md` hashes to the argument
    on `ACCEPTANCE-ACT-RECORD.md` line 95. That line sits in the "General
    trusted-bootstrap authorization transaction — performed 2026-09-01"
    section, as the "Performed nested row-5 act argument".
  - Mutants 1 and 13 in the JSON witness the check.
- [Observed] Rule-6 JSON: I re-ran all 23 mutants against the reviewed bytes.
  - Each `old` fragment occurs exactly once.
  - Each mutant makes `--selftest` exit 1.
  - Each run's output contains the recorded `refusal` string.
  - The JSON is accurate over 23 of 23.
- [Observed] CI (`governance-docs.yml`) checks out with `fetch-depth: 0` and
  runs both `--check` and `--selftest`. The Git-history population is
  therefore complete in CI.

## Prior findings

- **Round 1, M1 (a deleted raw re-opened an earlier CONFIRM): repaired.**
  [Observed] Deleting raw 3 and re-adding it as CONFIRM is refused "history
  review added more than once" (clone `a6`). A plain deletion is refused
  "history review deleted" (clone `a2`, raw 5). Mutant 16 witnesses the
  deletion guard.
- **Round 1, M2 (untested predicates): repaired.** [Observed] Every guard in
  `history_reviews` and `history_review` has a killing mutant in the JSON:
  - malformed name (22, 23);
  - added twice (20);
  - numbering (15);
  - deletion (16);
  - empty population (6);
  - not retained (7);
  - changed (5);
  - verdict (3, 11);
  - binding (4, 12);
  - latest selection (9, 10);
  - Git flags (17, 18, 19);
  - disk listing (21).
- **Round 2, M1 (rename-in and merge-drop): repaired.** [Observed]
  - A rename away with a same-named CONFIRM swapped in, in one commit, is
    refused "retained history review changed" (clone `a7`).
  - An `-s ours` merge that drops a side-branch raw 4 is refused "added more
    than once" (clone `a4`).
  - The real-Git selftest covers rename-then-delete and merge-drop, and
    mutants 17 and 18 show both flags are load-bearing.
- **Round 3, M1 (merge-kept side raw; raw added by a merge commit): repaired.**
  [Observed] Each of round 3's reproductions was re-run on 3400e46:
  - Case 1: main commits raw 4 REVISE, and a side branch adds raw 4 CONFIRM.
    The merge is resolved `--theirs`. The main-line commit alone is refused
    "not confirming". After the merge, `--check` is refused "history review
    added more than once: …HISTORY-REVIEW-4-RAW.md" (clone `a1`).
  - Case 2: raw 5 REVISE is added inside a `--no-commit --no-ff` merge
    commit. While present it is refused "history review not retained". After
    `git rm` and a commit it is refused "history review deleted: …HISTORY-REVIEW-5-RAW.md"
    (clone `a2`).
  - Variants that also failed closed:
    - an evil merge rewriting a side-branch REVISE raw to CONFIRM ("retained
      history review changed", `a3`);
    - a side branch editing the already-retained raw 3 to CONFIRM, then
      merged ("retained history review changed", `a5`);
    - raw 3 replaced by a symlink to a confirming file ("symlinked subject",
      `a8`);
    - an uncommitted worktree edit of raw 3 ("retained history review
      changed", `a9`).
  - The real-Git selftest covers both round-3 cases, and mutants 19 and 20
    witness `--diff-merges=combined` and the added-once rule.
- **Round 3, N2 (case-sensitive, top-level-only malformed refusal):
  repaired.** [Observed] The refusal matches a lower-cased basename containing
  `history-review` anywhere under the directory. A lowercase
  `history-review-5-raw.md` is refused while present and still refused after
  it is deleted (clone `a11`).
- **Round 3, N3 (two surviving mutants): repaired.** [Observed]
  - Dropping `| set(listed)` now fails the selftest "uncommitted history
    review accepted".
  - `HISTORY_REVIEW_RAW.fullmatch` changed to `.search` in
    `check_governance.py` now fails the fixture "raw-review shape covers the
    reconciliation's history reviews only".
- **Notes from earlier rounds.** Round 1 N1, N3–N6, round 2 N1 and N3, and
  round 3 N1 each have a named disposition in HISTORY-READING.md's "Review
  rounds" list. Round 1/2 N2 and round 3 N4 (four inputs with no drift
  mutant) are disclosed as pre-existing and still open.

## Findings

No material findings.

### N1 — Note: a malformed raw name with a non-ASCII byte is not in the Git population

[Observed] `history_population` parses `git log --name-only` without `-z`, so
Git's `core.quotePath` quoting turns a non-ASCII path into a quoted string.
That string does not start with `EVIDENCE` and is dropped.

Reproduction (clone `a10`, starting from a passing raw 4 CONFIRM):
1. Commit `HISTORY-REVIEW-5-RAW-é.md` with a REVISE verdict. `--check` is
   refused "malformed history review name" from the disk listing.
2. `git rm` it and commit. `--check` PASSes.

The lowercase ASCII equivalent stays refused after deletion (see round 3,
N2 above), so the two cases are handled inconsistently.

Impact is bounded. The file was never a valid history raw, and no strictly
named raw can contain a non-ASCII byte, so no valid verdict can be defeated
this way. HISTORY-READING.md's claim that such a name "is refused, never
skipped" holds only while the file is on disk.

Suggested fix: use `-z` (or `-c core.quotePath=false`) and split on NUL, as
the repository's own `git ls-tree -z` guardrail already requires.

### N2 — Note: near-miss names without the literal `history-review` are skipped

[Observed] Clone `a11`: a committed `HISTORY_REVIEW-5-RAW.md` with a REVISE
verdict, placed beside a confirming raw 4, leaves `--check` PASS.
HISTORY-READING.md states the predicate accurately ("whose name contains
`history-review`"), so this is a disclosed boundary, not a false claim.
A reviewer who follows the brief's exact filename is unaffected.

### N3 — Note: the two round-3 witnesses are not rows in `history-reading-rule6.json`

[Observed] Both round-3 N3 mutants are now killed (see Prior findings):
- the check_governance exemption mutant (`fullmatch` to `search`);
- the recorder's `| set(listed)` drop.

The second is partly covered by JSON mutant 21 (the disk listing). Neither is
recorded as its own `old`/`new` row with a commit. HISTORY-READING.md says
the JSON "records each guard's mutant", but the check_governance exemption
guard has no row.

Suggested fix: add both rows at the next regeneration.

### N4 — Note: a committed malformed name refuses permanently

[Observed] Once an ASCII malformed name has been committed, `--check` is
refused even after the file is deleted (clone `a11`). The recorder cannot
return to passing without rewriting history.

This fails closed, which is the intended polarity. It is noted so that an
owner is not surprised: one mis-named commit on `main` blocks the
reconciliation check until an owner decides. The same is true of a raw
number added twice.

## Verdict rationale

The five acceptance criteria are met.

- **Criterion 1.** Every deletion, replacement, rename, merge-drop,
  merge-swap, merge-commit addition, evil merge, symlink swap and worktree
  edit I attempted was refused, each with a named refusal [Observed].
- **Criterion 2.** Only a CONFIRM or CONFIRM WITH EXCEPTIONS raw binding the
  current digest passed. A duplicate verdict line, a duplicate binding line
  and malformed names are refused, as the selftest mutants and my clones
  show.
- **Criterion 3.** It holds, and the performed argument is on line 95 of the
  acceptance record.
- **Criterion 4.** All 23 rule-6 mutants re-run exactly as recorded.
- **Criterion 5.** HISTORY-READING.md matches the code, in present tense.
  The one qualification is the non-ASCII edge in N1.

The four findings are notes only. None lets a validly named non-confirming
raw be defeated. Hence CONFIRM WITH EXCEPTIONS.
