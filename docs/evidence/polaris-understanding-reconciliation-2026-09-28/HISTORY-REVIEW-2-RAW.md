# History review 2 — reconciliation recorder

Verdict: REVISE
Reviewed commit: eb728bf6d75c8e2ef0a0f34d2aa691954d87e732
Reviewer: independent fresh-context agent, 2026-09-28

Recorder bytes reviewed (sha256 computed by sha256sum over `git show` at the reviewed commit, and equal to the worktree file):

- `scripts/record_polaris_understanding_adoption.py`: `f3e968d56f6fa9d763495d49b8f92a2eb60a912406479664cab15ce4209772a2`

## Scope

Subject: `git diff a9a0830 eb728bf` — the recorder script, `HISTORY-READING.md`,
`history-reading-rule6.json` and the PROJECT-STATUS.md link, as the second
round after History review 1 (REVISE over f5fdde7: M1, M2, N1–N6). Governing
references read: owner ruling "R1: read as history"
(`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md:27`), the reconciliation
package `README.md` and `REVIEW-RAW.md`, and the `CONFIRM CRAFT AMENDMENT:
CC-SPEC@` lines of `ACCEPTANCE-ACT-RECORD.md`. All experiments ran in a scratch
clone checked out at the reviewed commit; the reviewed worktree was not
modified. The recorder bytes at b949a68 (the rule-6 JSON's recorded commit)
and eb728bf are identical [Observed: `git diff --quiet` exit 0].

## Facts established

- [Observed] CC-SPEC at C1 (`9322656dcfcc00b436868e93f2754f812dfa9db9`) hashes
  to `6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621`; the
  acceptance record carries exactly two anchored
  `CONFIRM CRAFT AMENDMENT: CC-SPEC@` lines, 66 and 95, and line 95 is that
  digest.
- [Observed] `--selftest` exits 0: "3 valid states …; 47 trust-boundary
  mutations refused". `--check` exits 1 with "latest history review not
  confirming: …HISTORY-REVIEW-1-RAW.md", as the brief expects.
- [Observed] `check_governance.py` in the clone: 31 OK, 21 WARN, 0 FAIL.
- [Observed] All 16 mutants in `history-reading-rule6.json` were re-run in the
  scratch clone (each `old` fragment occurs exactly once; `--selftest` run per
  mutant). Every one exits non-zero and its output contains the recorded
  refusal string.
- [Observed] Positive end-to-end paths in the scratch clone, each after
  committing a `HISTORY-REVIEW-2-RAW.md` with `CONFIRM` over the current digest
  (`--check` then passes):
  - commit raw 3 `REVISE` → refused "latest history review not confirming";
    then `git rm` raw 3 and commit → refused "history review deleted" (the
    round-1 M1 reproduction is now closed);
  - commit raw 4 with no raw 3 → refused "history review numbering is not 1..n";
  - untracked raw 3 → refused "history review not retained";
  - delete raw 2 and re-add it in a later commit → refused "reintroduced
    evidence".

## Criterion 1 — CC-SPEC read at C1, performed digest required

Met. [Observed] `HISTORY_PATHS` (script line 227) includes POLICY, so the
"review retired by changed input" comparison is skipped for it; lines 471-472
require the C1 blob's digest to be among the anchored
`^CONFIRM CRAFT AMENDMENT: CC-SPEC@([0-9a-f]{64})$` captures of the current
acceptance record, and the Frozen view reads POLICY at C1. This is R1's
wording. The anchoring is now tested (rule-6 mutant 12, selftest line 718).
The round-1 N1 limit (performed is inferred from line shape) is now disclosed
at `HISTORY-READING.md:18-20` [Observed].

## Criterion 2 — self-binding relaxed and compensated

Not met: two fail-open paths remain in the deletion guard (M1 below). The
ordering, numbering, verdict parsing, binding parsing, retention and empty
population arms are otherwise correct and now exercised [Observed: selftest
mutants and the end-to-end paths above].

## Findings

### M1 — Material: the "ever added" population misses raws that arrive by rename or whose addition is pruned by merge simplification, so a deleted non-confirming raw re-opens the check

[Observed] `Evidence.history_population` (script lines 269-273) runs
`git log --diff-filter=A --name-only --format= HEAD -- <EVIDENCE>` with Git's
defaults: rename detection on (git 2.54, `diff.renames` unset) and default
history simplification. Two reproductions in the scratch clone, each starting
from a committed `CONFIRM` raw 2 over the current digest (`--check` PASS):

1. **Rename in.** Commit `HISTORY-REVIEW-3-DRAFT.md` (`REVISE`), then `git mv`
   it to `HISTORY-REVIEW-3-RAW.md` and commit → `--check` refuses "latest
   history review not confirming" (the per-path `introduction` query sees an
   add, since the rename source is outside its pathspec). The directory-wide
   log lists the add of the `-DRAFT` name only, not raw 3. `git rm` raw 3 and
   commit → `--check` **PASS**.
2. **Merge that drops the raw.** On a side branch, commit raw 3 (`REVISE`) →
   `--check` refuses. On the main line, make an unrelated commit and merge the
   side branch with `-s ours` (the side commit is reachable from HEAD) → the
   raw is gone from the tree, the evidence directory is TREESAME to the first
   parent, simplification prunes the side, and the log lists no add of raw 3 →
   `--check` **PASS**. The repository's history has 27 merge commits, so merges
   are a live path, not a hypothetical.

In both cases a non-confirming later review is defeated by its removal, which
is exactly the round-1 M1 class. [Observed] With
`git log --diff-filter=A --no-renames --full-history --name-only --format= HEAD -- <EVIDENCE>`
the same two histories are refused "history review deleted: …HISTORY-REVIEW-3-RAW.md",
and the base state still passes (probe with the population query overridden,
run over the unmodified script's other logic).

Contributing cause [Observed]: the selftest's `Fixture.history_population`
(script line 626) replaces the real Git query with synthetic lists, so the
query itself is never exercised. Two mutants of the real seam survive
`--selftest` (exit 0, PASS line): returning `[]` as the added list (deletion
detection disabled wholesale), and adding `'--max-count=1'` to the log call.

`HISTORY-READING.md:33-34` ("The population is every raw ever added on HEAD's
history plus every raw on disk, so a deleted raw is refused, not skipped")
states the property the code does not have.

Proposed fix: pass `--no-renames` and `--full-history` to the population log
(and consider the same flags on `introduction`, script line 276, so a raw added
only on a pruned side is still found); add a real-Git selftest arm that builds
a throwaway repository (or `git worktree`) with the rename-then-delete and
drop-by-merge histories and expects "history review deleted"; record both,
plus a mutant that removes each flag, in `history-reading-rule6.json`.

### N1 — Note: a mis-named history raw is silently ignored rather than refused

[Observed] `HISTORY_REVIEW` (line 228) fullmatches `HISTORY-REVIEW-<n>-RAW.md`
with no leading zero; anything else is outside the population. In the scratch
clone a committed `REVISE` raw named `HISTORY-REVIEW-03-RAW.md`, and another
named `HISTORY-REVIEW-3-RAW-ADDENDUM.md`, each left `--check` at PASS. The
selftest's decoy (line 591) encodes this as intended. [Inferred] A reviewer or
a lead retaining a second raw "under a distinct name" (the AGENTS.md
duplicate-dispatch lesson) could hide a REVISE this way without any deletion.
Proposed fix: refuse any path in the evidence directory (on disk or ever
added) that starts with `HISTORY-REVIEW-` (case-insensitive) and does not
fullmatch the strict pattern; add a mutant.

### N2 — Note: round-1 N2 remains open (pre-existing)

[Observed] Adding `VISION`, or the evidence `README.md`, `final-documentation.patch`
and `documentation-images.json`, to `HISTORY_PATHS` still survives
`--selftest`. The code still checks those inputs against current bytes
(lines 467-470 region) [Observed by inspection], so this diff weakens nothing;
the test gap predates it and was not dispositioned. Proposed fix unchanged
from round 1: one "review retired by changed input" mutant per remaining
non-history input, or a disposition line saying it is deferred.

### N3 — Note: round-1 findings have no recorded disposition

[Observed] The repairs map onto round 1 cleanly in the code and prose
(M1 → lines 487-500; M2 → rule-6 mutants 8-15; N1 → HISTORY-READING.md:18-20;
N3 → lines 10-13; N4 → lines 35-37; N5 → lines 44-45; N6 → lines 38-41), but
no file states which finding each change answers or that round-1 N2 is
deferred. Proposed fix: one disposition paragraph in `HISTORY-READING.md` or
the package README's successor record naming each round-1 finding and its
repair commit.

## Criterion 3 and 4 summary

- M2 is repaired [Observed: the six round-1 surviving mutants are now killed,
  rule-6 mutants 8-13]. M1 is repaired for the plain-deletion case only (M1
  above). Every other frozen input is checked as before [Observed by
  inspection: `reviewed_template` and `check_evidence` unchanged outside the
  history arms]. `--selftest` passes; the rule-6 JSON is accurate over all 16
  mutants.
- `HISTORY-READING.md` is present tense and matches the code except
  lines 33-34 (M1). Its line 44-45 statement that two mutants fail by an
  exception is accurate (mutants 5 and 6).

## Housekeeping

[Observed] The reviewed worktree carries untracked sibling paths (a spec-policy
readability restyle candidate package and two scripts) that this review did
not create or read as subject. All scratch work ran in a separate clone.
