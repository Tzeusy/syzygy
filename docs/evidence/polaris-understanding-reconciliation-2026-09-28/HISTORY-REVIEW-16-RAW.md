# History review 16 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 11e8ab30afc819811c90152d9ccbb26cb2dea4e4
- `scripts/record_polaris_understanding_adoption.py`: `058eab0460bc3c2bd1bddab585db64ddcf259e18298e65da08457a9b24b82cfd`

Reviewer: fresh-context independent reviewer, 2026-10-03. Work done in a scratch clone
(`review16/repo`, detached at the reviewed commit) and a second clone for mutants
(`review16/mut`, detached at bec7a87c3bfa14a322c413e01f059e2dfe8e1aec). No repository
file was edited.

## Identity

- [Observed] `sha256sum` at the reviewed commit: the recorder hashes to
  058eab0460bc3c2bd1bddab585db64ddcf259e18298e65da08457a9b24b82cfd, and
  `scripts/readability_successor.py` to
  f9e24b6563eca5bfc274dc19170ed7488e5f4ab4caa33558fe86cfa480e57df7, which equals the
  recorder's `SUCCESSOR_TOOL_SHA` (line 35). The tool at 4c5c22a15780dd34bc8ac14b04c04fbc0407fb97
  hashes to the same value, so the tool is unchanged by this change.
- [Observed] `git diff --stat bec7a87c3bfa14a322c413e01f059e2dfe8e1aec 11e8ab30afc819811c90152d9ccbb26cb2dea4e4`
  touches only `HISTORY-READING.md` and `history-reading-rule6.json`: the recorder at
  the code commit and at the reviewed commit are the same bytes.

## Criterion 1 — N1 repaired

- [Observed] `successor_rows` now has two `try` blocks. The first loads the package,
  computes its normalized subject keys and calls `performed_rows()`; any exception or a
  `None` result skips the package (grants and contests nothing). The second requires
  `check() == 'performed-exact'`, reads the manifest rows and builds pairs; any
  exception adds the keys to `contested`. After composition,
  `rows.update(dict.fromkeys(contested, CONTESTED))` overrides every composed row for
  those keys.
- [Observed] Own probe on real fixtures (`synthetic`, `pin`, `record`, `later` with
  explicit instants), loading both the reviewed recorder and the 4c5c22a1 recorder
  (P1): A->B at t0, B->C at t1, C->B at t2, then a no-act write of C. Tool states:
  `example-cb` refused, the other two `performed-exact`. Reviewed recorder row for the
  proposal: CONTESTED. Pre-fix recorder row: (A, C). The repair refuses the N1 tree.
- [Observed] `baseline_proof` refuses a CONTESTED row before comparing it, with the
  message extended to name both causes; only the message changed there.

## Criterion 2 — N3 covered

- [Observed] The selftest adds a two-history loop; the second history, "two packages at
  one instant", records a second distinct package B->C at the first package's own instant
  t0. It asserts the tool refuses exactly one package and the row is CONTESTED. It
  passes at the reviewed commit.
- [Observed] Own probe P2 (same shape): tool refuses `example-readability-successor`,
  `example-tie` is `performed-exact`; reviewed recorder CONTESTED; pre-fix recorder
  (B, C).
- [Observed] Rule-6 row 113 (pre-fix body with the N1 history removed, so the tie
  fixture runs alone) is killed with "a performed successor the tool refuses was composed
  around: two packages at one instant". The fixture fails against the pre-fix
  composition.

## Criterion 3 — No widening and no regression

- [Observed] `python3 scripts/readability_successor.py --all --check` in the clone: four
  `PASS performed-exact` lines (capability-1, polaris-generator-base, polaris-understanding
  dependency-union, polaris-understanding readability), "4 successor package(s) checked",
  rc 0.
- [Observed] `--selftest`: rc 0; four PASS lines, the successor-rows one ending "a refused
  performed package contests its paths after a step back and at an instant tie; 15
  composition cases". The 15 `chain` cases are unchanged in the diff.
- [Observed] Real-tree rows: 38 rows, 0 CONTESTED; the changed subjects (both
  `proposal.md`/`design.md` pairs in the three changes and the amendment's
  `GOVERNING-DEPENDENCIES.md`) carry distinct predecessor and successor digests.
- [Observed] `--check` at the reviewed commit fails only with "latest history review does
  not bind the current recorder: …HISTORY-REVIEW-15-RAW.md", as the brief expects.
- [Observed] Own probes: honest A->B->C (P3) yields (A, C) under both recorders; the
  honest step back A->B, B->C, C->B at current B (P4) yields (A, B) under both, with all
  three packages `performed-exact`. Unperformed, malformed, deeply nested and wrongly
  typed siblings still leave the rows unchanged (selftest assertions at lines 1156-1185,
  all passing; rule-6 rows 117 and 118 kill the two ways of making them contest).
- [Observed] Escapes examined:
  - Path spelling: contested keys are `posixpath.normpath`ed, the same normalization
    as claims (row 120 kills its removal; the drifted fixture includes a `./` alias).
  - Exception class: both handlers catch `Exception`; a narrower exception from
    `check()` (e.g. `FileNotFoundError` from a missing subject) would still be caught. A
    `BaseException` would abort the whole recorder, which is fail-closed.
  - Ordering: `contested` is applied after every package is composed, so glob order
    cannot let a later claim override it (row 116 covers the "only unclaimed paths"
    variant).
  - Act-unverified: a refused package whose act record is then edited escapes the
    marking; see N1. This follows from the criterion's requirement that act-unverified
    packages contest nothing, and the tool still refuses the tree.
- [Observed] Wrongly blocking an honest tree: the only new refusals I found are trees
  the tool also refuses (P1, P2, P8, P9). P9: a first package naming both `proposal.md`
  and `spec.md`, chained by B->C on `proposal.md`, with `spec.md` then drifted; the tool
  refuses the first package, and the reviewed recorder contests `proposal.md` too (the
  pre-fix recorder gave (B, C)). This is the stated "contests every file it names"
  behaviour and matches the tool. [Inferred] The instant tie (round 15's N2) is the one
  honest-intent case now refused by both, already documented as fail-closed.

## Criterion 4 — Rule-6 rows

- [Observed] Replayed all nine rows whose `commit` is
  bec7a87c3bfa14a322c413e01f059e2dfe8e1aec (rows 112-120 of 120), applying `old`->`new`
  and every `further_edits` entry once at that commit, each `old` fragment found exactly
  once, then running `python3 scripts/record_polaris_understanding_adoption.py --selftest`.
  All nine exit 1 (killed), matching `killed: true`. Rows 112-119 print exactly the
  recorded refusal. Row 119's re-pinned `SUCCESSOR_TOOL_SHA` matched the mutated tool
  (the run reached the fixture precondition, not the tool-digest refusal).
- [Observed] Row 120 is killed by the expected assertion ("drifted successor granted
  rows"), but the recorded refusal string embeds a set-derived dict repr whose key order
  varies between runs; see N2.
- [Inferred] New predicates and rows: performed-gate (117), act-unverified handler
  (118), contest add (114), contest apply (115), contest override of claimed paths (116),
  key normalization (120), the pre-fix composition under each fixture (112, 113), and
  the tool's strict instant the tie fixture relies on (119). The `require(check() ==
  'performed-exact')` guard is equivalent past a non-None `performed_rows()` (check
  either returns that string or raises), as the reading says. `manifest_rows()` and the
  `predecessor[path]` lookup inside the second `try` cannot fail once `performed_rows()`
  has verified (it calls `manifest_rows()` and subjects are the predecessor keys), so
  their landing in `contested` is unreachable and needs no row. The `baseline_proof`
  change is message text only. I found no new predicate without a row.

## Criterion 5 — The reading is accurate

- [Observed] The bullet split (unperformed / malformed / act-unverified grants and blocks
  nothing; act-verified but check-failing contests every file it names) matches the code
  and the new docstring.
- [Observed] The round-16 rule-6 paragraph's list (pre-fix composition under both
  fixtures and under the tie fixture alone; contesting nothing; contested not applied or
  only to unclaimed paths; unperformed or act-unverified contesting; normalization; the
  tool's strict instant under a moved pin) matches rows 112-120 one to one, and "rows
  112 to 120" is the right range. The one named equivalent guard is correctly argued.
- [Observed] Round 15's N1 and N3 are marked answered in round 16; N2 stays a
  documented fail-closed remedy. That matches the code and fixtures.
- [Observed] The sentence "so it can no longer accept a tree the tool refuses (round 15's
  N1)" is broader than the code; see N1.

## Notes (non-blocking)

- N1. The reading's "it can no longer accept a tree the tool refuses" overstates the
  repair. Two trees the tool refuses are still accepted by the recorder alone:
  - P5: the N1 tree, then one appended line in the refused C->B package's dedicated act
    record. `performed_rows()` now raises, so the package is skipped, and the reviewed
    recorder composes (A, C) again; `readability_successor.py --all --check` exits 1.
  - P10 (review 14's N1, already recorded): a performed A->B package, then a no-act
    write back to A. The row is CONTESTED, but `baseline_proof` consults rows only when
    `current != adopted`, so the recorder passes.
  The battery, which runs the tool, still refuses both, as round 15 N1 said. Suggested
  wording: "it no longer composes around a package whose act verifies but whose check
  fails", or name both residuals.
- N2. Row 120's `refusal` is not byte-reproducible: it embeds `repr` of a dict built from
  a `set`, so the key order follows `PYTHONHASHSEED`. Two reruns gave two different
  orders, neither the recorded one; the kill and the assertion text before the colon
  reproduce. Record the stable prefix, or sort the repr in the assertion message.
- N3. The contested scope is every path a refused package names, so drift on a path no
  adopted subject depends on can contest an adopted path (P9). This matches the tool
  and fails closed; recorded so the coupling is visible, not as a defect.

## Probe record

Probe script `review16/probe.py` (real tool fixtures, explicit instants
2026-09-29T00:00:0nZ; A/B/C/D are the four proposal byte strings):

- P1 N1 tree: tool refuses `example-cb`; reviewed CONTESTED; pre-fix (A, C).
- P2 tie: tool refuses the first package; reviewed CONTESTED; pre-fix (B, C).
- P3 honest A->B->C: both (A, C).
- P4 step back, current B: all `performed-exact`; both (A, B).
- P5 N1 tree plus act-record edit: reviewed (A, C); pre-fix (A, C); tool `--all --check` rc 1.
- P8 chain then no-act edit to D: both packages refused; reviewed CONTESTED; pre-fix no row.
- P9 first package refused via `spec.md` drift: reviewed CONTESTED; pre-fix (B, C).
- P10 no-act edit back to A: reviewed CONTESTED (unconsulted by `baseline_proof`); pre-fix no row.
