# History review 17 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 0f835ee91da9bd6ade4d17bee0faccfd0e14160b
- `scripts/record_polaris_understanding_adoption.py`: `e97973ab4660b1f39eb2e8775ade703ab159d522e02f59eb24244793ca42f8b3`

Fresh-context review of the two commits after main `c540438d` (`d9f14202`, the
recorder code and selftest fixtures; `0f835ee9`, the reading and rule-6 rows
121-126). All work was done in a scratch clone under `review17/`. No repository
file was edited.

## Identity

- [Observed] The scratch clone of the `syzygy-lmjg` worktree is checked out
  detached at `0f835ee91da9bd6ade4d17bee0faccfd0e14160b`. `git log` shows
  `0f835ee9` -> `d9f14202` -> `c540438d`.
- [Observed] `sha256sum scripts/record_polaris_understanding_adoption.py` gives
  the digest in the head above.
- [Observed] `sha256sum scripts/readability_successor.py` is
  `f9e24b6563eca5bfc274dc19170ed7488e5f4ab4caa33558fe86cfa480e57df7`. This
  equals `SUCCESSOR_TOOL_SHA` (recorder line 35). The tool is not in the diff.
- [Observed] Change population: `git diff --stat c540438d 0f835ee9` lists three
  files.
  - `d9f14202` touches only the recorder.
  - `0f835ee9` touches only `HISTORY-READING.md` and
    `history-reading-rule6.json`.
  - Rule-6 rows 1-120 are unchanged: their mutant list equals the one at
    `c540438d`. 126 rows in all.

## Criterion 1 — P5 closed

- [Observed] Probe P5 (`probe.py`) uses the real tool's `synthetic`, `pin` and
  `later` helpers. The tree:
  - A->B is recorded at `…:00Z`, `example-bc` B->C at `…:01Z`, and
    `example-cb` C->B at `…:02Z`.
  - Then a no-act write of C to `proposal.md`.
  - Then one line is appended to `example-cb`'s dedicated act record.
- [Observed] Result for P5:
  - The tool refuses `example-cb` ("dedicated act mismatch"), and
    `--all --check` exits 1.
  - The reviewed recorder's `successor_rows()` gives **CONTESTED** for the path.
  - The pre-fix recorder (`git show c540438d:…`, loaded from the scratch dir)
    gives the composed pair **(A, C)**.
- [Observed] Three variants of breaking the act record:

  | Probe | What was broken | Tool | Reviewed recorder | Pre-fix recorder |
  |---|---|---|---|---|
  | P5a | dedicated act file removed, aggregate block kept | refuses ("aggregate carries the act but the dedicated record is absent") | CONTESTED | (A, C) |
  | P5b | aggregate block removed, act file kept | refuses ("expected exactly one binding line") | CONTESTED | (A, C) |
  | P1 | the plain N1 tree, act not edited | refuses | CONTESTED | CONTESTED |

- [Observed] The listed-pins copy fixture (selftest lines 1224-1230) under the
  performed package's own act:
  - The tool's `--all --check` exits 1 with an uncaught
    `AttributeError: 'list' object has no attribute 'values'`.
  - The reviewed recorder contests both named paths (`probe4.py`).
  - So the tool and the recorder agree.

## Criterion 2 — P10 closed

The probe is `probe3.py`, run on the real tree. It subclasses `Evidence` so that
`current(path)` returns the adoption blob and `successor_rows()` returns a
chosen row. It ran for both changed subjects, `proposal.md` and
`GOVERNING-DEPENDENCIES.md`.

- [Observed] Reviewed recorder, written-back file:
  - With the real restyle row `(adopted, restyled)`, `baseline_proof` and
    `check_evidence` both refuse with "subject written back over its performed
    successor row: …".
  - With the row CONTESTED, both refuse with "two performed successors claim …".
- [Observed] Reviewed recorder, row kept `(adopted, adopted)`:
  - `baseline_proof` passes.
  - `check_evidence` gets past the baseline and stops only at the expected
    "latest history review does not bind the current recorder".
  - With no row, the result is the same.
  - The selftest fixture (lines 864-883) runs `check_evidence` to a full pass
    over a kept row.
- [Observed] Pre-fix recorder: in all four row cases, `baseline_proof` passes
  the written-back file, and `check_evidence` reaches the history-review step.
  So it accepted P10.
- [Observed] In a fixture, a performed A->B package followed by a no-act write
  back to A (P10) behaves as follows:
  - The tool refuses the package and exits 1.
  - The row is CONTESTED under both recorders.
  - The reviewed `baseline_proof` now refuses a CONTESTED row whatever the
    bytes.

## Criterion 3 — No wrongful refusal, no widening

**Checks run**

- [Observed] `readability_successor.py --all --check`: four
  `PASS performed-exact` lines, "4 successor package(s) checked", rc 0.
- [Observed] `--selftest`: "40 fixtures, 0 failing", rc 0.
- [Observed] Recorder `--selftest`: rc 0, with all four PASS lines. The
  successor-rows line now ends "…and still does after its act record is
  edited; a copy claiming a performed act contests; 15 composition cases".
- [Observed] Real tree: `r.baseline_proof(r.Evidence(r.ROOT))` returns with no
  error.
  - 38 rows, 0 CONTESTED.
  - All 8 amendment subjects have rows. Five are kept rows: `.openspec.yaml`,
    `COVERAGE.md`, `SYNTHESIS-MAP.json`, `spec.md` and `tasks.md`. Three are
    restyles: `GOVERNING-DEPENDENCIES.md`, `design.md` and `proposal.md`.

**Packages that must change nothing**

- [Observed] An honest unperformed candidate B->C beside a performed A->B (P13):
  the tool exits rc 0, and both recorders give (A, B).
- [Observed] The selftest's malformed, deeply nested and wrongly typed siblings,
  and the listed-pins copy under its own never-recorded act, leave the rows
  unchanged (lines 1209-1235, passing).
- [Observed] An unloadable refused config (P5e) blocks no other package: the
  rows still compose (A, C).

**Honest trees, and trees the tool refuses**

| Probe | Tree | Tool | Reviewed | Pre-fix |
|---|---|---|---|---|
| P3 | A->B->C | rc 0 | (A, C) | (A, C) |
| P4 | step back, current B | rc 0 | (A, B) | (A, B) |
| P11 | A->B, then B->A by a performed act, current A | rc 0 | CONTESTED | CONTESTED |
| P12 | A->B performed, beside a stale unperformed candidate whose predecessor is A | rc 1 | (A, B) | (A, B) |
| P5c | N1 tree, act file and aggregate block both erased | rc 0 | (A, C) | (A, C) |
| P5d | N1 tree, refused config repointed to a never-recorded act | rc 1 (manifest differs) | (A, C) | (A, C) |
| P5g | as P5d, with the manifest regenerated | rc 0 | (A, C) | (A, C) |
| P5e | refused config made unloadable | rc 1 | (A, C) | (A, C) |
| P5f | refused package directory removed | rc 0 | (A, C) | (A, C) |

- [Observed] **New refusal of an honest tree: P11.**
  - The tool accepts P11.
  - Pre-fix, a CONTESTED row was ignored because `current == adopted`. The
    reviewed `baseline_proof` now consults the row and refuses: "two performed
    successors claim …".
  - [Inferred] This is fail-closed and consistent with the documented rule that
    "a cycle with no first digest" is contested. It is still a tree the tool
    accepts that the recorder now refuses. See N1.
- [Observed] **Escapes still left.** P12 and P5d are trees the tool refuses that
  the recorder alone still accepts, before and after the fix. See N2.
  - P5c, P5g and P5f pass both the tool and the recorder.
  - P5e is the documented unloadable-config residual.
- [Inferred] I found no other new refusal. The new contested set is exactly the
  packages whose `performed_rows()` is non-None and whose `check()` raises.
  `check()` calls `performed_rows()` first, so the tool refuses every one of
  them.

## Criterion 4 — Rule-6 rows 121-126

- [Observed] `replay.py` cloned the repo once per row at the recorded commit,
  `d9f14202ed8f52642bc7a191bcb57a22f3400b99`. In each row:
  - `old` occurs exactly once and is replaced once.
  - There are no `further_edits`.
  - The row's `command` is
    `python3 scripts/record_polaris_understanding_adoption.py --selftest`.
- [Observed] All six exit rc 1 (killed), matching `killed: true`.
- [Observed] The recorded `refusal` string reproduces verbatim in every row's
  output:
  - 121 "a refused package was skipped after its act record was edited: step
    back then edited (…)". The digests are those of fixed fixture bytes and
    reproduce.
  - 122 "unperformed successor granted rows".
  - 123 "AssertionError: a file written back over its performed successor
    accepted".
  - 124 "written-back refusal: current subject drift: …proposal.md".
  - 125 "subject written back over its performed successor row: …/.openspec.yaml".
  - 126 "written-back refusal: subject written back over its performed
    successor row: …proposal.md".
- [Observed] The recorder bytes at `d9f14202` equal those at the reviewed
  commit (`0f835ee9` changes no script). The unmutated `--selftest` passes there,
  so the kills are not baseline failures.
- [Inferred] Rows 124 and 126 are killed only by the selftest's refusal-message
  assertion. See N3.

## Criterion 5 — The reading is accurate

- [Observed] The three rewritten bullets match the code and the new docstring:
  - unperformed or unloadable: grants and blocks nothing;
  - any other failing package contests, whether or not its act verifies;
  - written-back refusal unless the row keeps the adopted bytes.
- [Observed] The listed-pins copy sentence ("A copy of a performed package that
  names that package's act and fails its check contests too, as the tool refuses
  it") holds (`probe4.py`).
- [Observed] The round-17 rule-6 paragraph names six predicates. They map one to
  one, in order, onto rows 121-126.
  - "Row 123 fails by the fixture's own assertion" is right (an
    `AssertionError`).
  - "row 125 fails on the real tree's first kept row, before the fixture" is
    right (`.openspec.yaml` is the first kept row).
- [Observed] The round-16 notes entry now says "Both residuals are closed in
  round 17's change". This matches P5 and P10 above.
- [Observed] The "What the recorder alone still accepts" bullet is correct for
  the two cases it names:
  - unloadable config: P5e, where the tool refuses;
  - removed directory: P5f, outside both.
- [Observed] The bullet is incomplete as an enumeration. It omits P12 and P5d,
  which the tool refuses, and P5c/P5g, which are outside both like a removed
  directory. Its closing "The battery, never the recorder alone, is the claim"
  keeps it from claiming completeness. Non-blocking; see N2.
- [Observed] No bullet claims P11-style reverts pass. The written-back bullet
  ("passes only when the row keeps the adopted bytes") implies they are refused,
  but does not say that an honest revert through performed acts is caught. See
  N1.

## Criterion 6 — Expected state

- [Observed] At the reviewed commit, `python3
  scripts/record_polaris_understanding_adoption.py --check` exits 1 with exactly:
  "FAIL exact digest reconciliation unresolved: latest history review does not
  bind the current recorder:
  docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-16-RAW.md".

## Notes (non-blocking)

- N1. **An honest revert to the adopted bytes is now refused (P11).**
  - The tree: performed A->B, then a performed B->A, with current A. The tool
    accepts it (`--all --check` rc 0, both packages `performed-exact`).
  - `chain` gives CONTESTED (no first digest). The reviewed `baseline_proof` now
    reads the row although `current == adopted`, so it refuses with "two
    performed successors claim …". The pre-fix recorder accepted this tree.
  - [Inferred] This fails closed. It cannot be undone by a further act: any
    later step keeps the cycle or leaves the adopted bytes. A recorder change is
    needed.
  - The message names two successors "claiming" the file, which misdescribes an
    honest revert.
  - Suggest the reading name this case explicitly beside the written-back
    bullet, as a tree the tool accepts and the recorder refuses.
- N2. **The "What the recorder alone still accepts" list is not exhaustive.**
  The recorder alone also accepts:
  - P12: a stale unperformed candidate whose predecessor differs from today's
    bytes. The tool refuses it ("subject differs from its predecessor digest").
    The recorder skips every unperformed package. This predates this change.
  - P5d: a refused package whose config is repointed to a never-recorded
    label/marker/act. The tool refuses it on manifest regeneration.
  - Outside both, like a removed directory: P5c (act file and aggregate block
    both erased) and P5g (repointed config with a regenerated manifest).
  - Suggest naming the unperformed-but-tool-refused class, or saying the list
    is examples.
- N3. **Rows 124 and 126 are message-only kills.**
  - When `current == adopted`, the drift guard `row == (digest(adopted),
    digest(current))` already requires `row == (adopted, adopted)`. So the new
    written-back `require` is equivalent in effect to the drift test, and only
    its message differs.
  - The contested guard is likewise redundant for written-back bytes: a
    CONTESTED row is not equal to `(adopted, adopted)`.
  - Rows 124 and 126 die only because the selftest asserts the refusal text.
    The predicate the change needs is row 123's (consulting the row at all).
  - Not a defect. The reading could say the written-back guard is a dedicated
    message over the drift test.
- N4. Readability: inside `baseline_proof`'s loop, the new `row =
  evidence.successor_rows().get(path)` rebinds the loop variable `row` (the
  manifest artifact dict). It is read after rebinding only as the successor row,
  so behaviour is correct, but a distinct name would be clearer.

## Probe record

Scripts live in `review17/`. They load the reviewed recorder from `repo/` and
the pre-fix recorder from `prefix/scripts/`, which is `git show c540438d:…`. A,
B and C are the three fixture byte strings `# Why\n\nlong prose\n`,
`# Why\n\nShort prose.\n` and `# Why\n\nThird.\n`. Instants run
`2026-09-29T00:00:0nZ`.

**`probe.py`** (tool rc / reviewed rows / pre-fix rows)

| Probe | Tool rc | Reviewed | Pre-fix |
|---|---|---|---|
| P1 | 1 | CONTESTED | CONTESTED |
| P5 | 1 | CONTESTED | (A, C) |
| P5a | 1 | CONTESTED | (A, C) |
| P5b | 1 | CONTESTED | (A, C) |
| P5c | 0 | (A, C) | (A, C) |
| P5d | 1 | (A, C) | (A, C) |
| P5e | 1 | (A, C) | (A, C) |
| P5f | 0 | (A, C) | (A, C) |
| P3 | 0 | (A, C) | (A, C) |
| P4 | 0 | (A, B) | (A, B) |
| P11 | 0 | CONTESTED | CONTESTED |
| P10 | 1 | CONTESTED | CONTESTED |
| P12 | 1 | (A, B) | (A, B) |
| P13 | 0 | (A, B) | (A, B) |

**Other scripts**

- `probe2.py`: P5g gives tool 0, reviewed (A, C) and pre-fix (A, C).
- `probe3.py`: the real-tree written-back matrix. Two paths × {restyle,
  contested, kept, none} × {`baseline_proof`, `check_evidence`} × {reviewed,
  pre-fix}, with results as in Criterion 2.
- `probe4.py`: a listed-pins copy under the performed act. The tool gives rc 1
  with `AttributeError`; the reviewed recorder gives both paths CONTESTED.
- `replay.py`: rows 121-126 at `d9f14202`. All six are killed, and all six
  recorded refusals reproduce.
- Commands at the reviewed commit:
  - `readability_successor.py --all --check` rc 0;
  - `--selftest` rc 0;
  - recorder `--selftest` rc 0;
  - recorder `--check` rc 1 with the expected HISTORY-REVIEW-16 binding refusal;
  - the `baseline_proof` one-liner returns.
