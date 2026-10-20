# History review 19 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 6df6bdcdfc5929bd201cdfafcaf2c08fbba5fb02
- `scripts/record_polaris_understanding_adoption.py`: `b993ec3077a5c04d985a961824b47b2e38ad0cbea0d9ef512bc6619e4392ad0e`

Reviewer: fresh-context independent reviewer (history review 19, re-dispatch), 2026-10-20.

## Identity

- [Observed] Scratch clone `/home/tze/.cache/review19b-scratch/clone`,
  `git rev-parse HEAD` = the reviewed commit. A second clone (`probe/`) at the
  same commit carried every mutation and probe; TMPDIR was under
  `/home/tze/.cache/review19b-scratch/`. The probe clone's
  `git status --porcelain` was empty after each run.
- [Observed] The recorder digest above is `sha256sum` over the file in the
  clone at the reviewed commit.
- [Observed] `git log --oneline origin/main..6df6bdcd` lists seven commits
  (46fbab0d … 6df6bdcd). `git diff e93849ea 6df6bdcd` on the recorder (round
  18's subject to this one) changes only `reconciliation_selftest`: the C1
  fixture reads `vision.md` at C1, and three fixtures are added (uppercase
  40-character reviewed commit, binding line with trailing text, and
  `review-inputs.json` re-indented and rebound). No non-selftest code changed
  since round 18.

## (a) Round-18 findings

- M1 [Observed] Closed. The new fixture re-indents `review-inputs.json`
  (asserting the bytes differ), rebinds it in the latest raw, and expects
  "reconciliation review moved a fixed input: …/review-inputs.json". Round
  18's scope mutant (`if path not in REBINDABLE + (INPUTS,):`, row 156) now
  fails the selftest with "reconciliation mutation accepted:
  rebind-review-inputs". A second mutant of mine, `REBINDABLE = (VISION,
  INPUTS)`, is killed the same way. Real-Git probe: re-indented
  `review-inputs.json` rebound by a committed CONFIRM raw 2 fails `--check`
  with "reconciliation review moved a fixed input: …/review-inputs.json".
- N1 [Observed] Closed. Row 157 (drop the `$` anchor) and row 158 (`.{40}`)
  each fail the selftest with "mutation accepted:
  docs/reviews/R-POLARIS-UNDERSTANDING-RECONCILIATION-10-RAW.md".
- N2 [Observed] Dispositioned as "not changed", which is a legitimate choice,
  but the stated reason is not true at the reviewed commit. See N1 below.
- N3 [Observed] Dispositioned as predecessor behaviour; correct (every C1
  input is read from the working tree, unchanged by this diff).
- N4 [Observed] Reconciliation review 1's head carries exactly the seven
  binding lines and no other line of that form: `--check` gets past
  `successor_bindings` to the history-review refusal, and with a probe
  history raw 19 runs to PASS.

## (b) The published predicate and the Q-A1 arm

- [Observed] `SUCCESSOR_BOUND` = `{*FROZEN_PATHS, INPUTS} - set(HISTORY_PATHS)`
  is exactly the set of C1 bindings that `reviewed_template` compares with
  today's bytes, so `successor.get(path, sha)` always finds its key when a
  raw exists, and every key other than `vision.md` is forced equal to C1's
  digest before that comparison.
- [Observed] `HISTORY_PATHS` (line 250) is unchanged from `origin/main` and
  does not contain `VISION`; `REVIEW-RAW.md` is still read and its C2
  retention test is unchanged. This matches row D8's Q-A1 answer, "Fresh
  reconciliation review" — "Re-review over the amended vision.md."
  (`DOCTRINE-AMENDMENT-LOG.md:13`).
- Real-Git probes, each a commit on top of a probe commit adding a CONFIRM
  `HISTORY-REVIEW-19-RAW.md` that binds the reviewed recorder bytes, then
  `--check`:

| Probe | `--check` |
|---|---|
| nothing else | PASS |
| `vision.md` edited, no new raw | FAIL review retired by changed input: vision.md |
| `vision.md` restored to its C1 bytes (raw 1 binds the amendment) | FAIL review retired by changed input: vision.md |
| raw 2 REVISE committed | FAIL latest reconciliation review not confirming: …-2-RAW.md |
| `vision.md` edited again, raw 2 CONFIRM binding it | PASS |
| README.md changed, raw 2 rebinds it | FAIL reconciliation review moved a fixed input: README.md |
| `review-inputs.json` re-indented, raw 2 rebinds it | FAIL … moved a fixed input: review-inputs.json |
| `proof.json` changed, raw 2 rebinds it | FAIL … moved a fixed input: proof.json |
| `REVIEW-RAW.md` changed | FAIL retained C2 review changed |
| raw 1 edited in a later commit | FAIL retained reconciliation review changed |
| raw 1 deleted | FAIL reconciliation review deleted |
| raw 2 on disk, not committed | FAIL reconciliation review not retained |
| raw 2 with an eighth (recorder) binding line | FAIL reconciliation review input population |
| raw 3 with no raw 2 | FAIL reconciliation review numbering is not 1..n |
| confirming raw placed in the evidence directory | FAIL review retired by changed input: vision.md |
| `R-POLARIS-UNDERSTANDING-RECONCILIATION-NOTES.md` in `docs/reviews/` | FAIL malformed reconciliation review name |

- [Observed] No probe tree made `--check` pass with a changed C1 input
  other than `vision.md`, with a `vision.md` that no confirming retained raw
  binds, with `REVIEW-RAW.md` changed, or with a REVISE latest raw.
- [Inferred] From the code reading above, the only path that can differ from
  C1's digest is `vision.md`, and only to the digest the latest retained,
  confirming raw binds; I found no tree outside that.

## (c) Rule 6

- [Observed] Rows 127–158 are 32 rows; each has non-empty `old` and `new`
  fragments that differ, a 40-hex `commit`, and `killed: true`. Rows 127–155
  carry `ea764977…`, rows 156–158 `f3e5ffa7…`. Every `old` fragment occurs
  exactly once in the reviewed recorder.
- [Observed] Re-run against the reviewed recorder in the probe clone, rows
  127, 131, 133, 138, 139, 141, 145, 147, 149, 154, 156, 157 and 158: each
  selftest exits 1 and each row's recorded refusal text appears in the
  output.
- [Observed] `git diff f3e5ffa7 6df6bdcd` does not touch the recorder (only
  `HISTORY-READING.md` and `history-reading-rule6.json` within the recorder
  and the package), so rows 156–158 ran on the reviewed bytes.
- Non-row mutants (selftest result):
  - drop the C1 read of `vision.md` in the selftest fixture: killed
    ("candidate input drift: .syzygy/governance/doctrine/vision.md").
  - `REBINDABLE = (VISION, INPUTS)`: killed (rebind-review-inputs).
  - read the first reconciliation raw instead of the latest: killed.
  - accept today's bytes at either the successor's or C1's digest: killed
    (vision-written-back).
  - frozen view reads today's `vision.md`: killed (candidate input drift).
  - drop `evidence.ancestor(c2, intro)`: killed, by a different refusal
    (the fixture's blob read at the unrelated commit); fails closed.
  - drop the `startswith(RECONCILIATION_DIR)` term from the malformed-name
    guard: survives; [Inferred] equivalent, since both population sources
    yield only paths under `docs/reviews/`.
  - compare `.strip()`ped verdict headers: survives. See N2.

## (d) The selftest's C1 read of vision.md

- [Observed] Sound. With (d2) applied, today's `vision.md` differs from C1's,
  so the fixture's synthetic C1 (`before`) must take C1's bytes, exactly as
  the frozen view does in `reviewed_template`; the mutant reverting it fails
  with the error `HISTORY-READING.md` records. The fixture's base state is
  then the pre-(d2) world, and `amended` is built from C1's bytes.
- [Inferred] It weakens nothing: the selftest never vouched for the real
  corpus's `vision.md` (that is `--check`'s job, which compares today's
  bytes with raw 1's binding), and every reconciliation fixture still runs
  with an amended `vision.md` against C1's.

## (e) Expected state

- [Observed] `--selftest` exits 0: "PASS reconciliation selftest: 6 valid
  states …; 92 trust-boundary mutations refused", "PASS history population
  selftest: 27 real-Git cases", successor rows selftest PASS.
- [Observed] `--check` exits 1 with exactly "FAIL exact digest
  reconciliation unresolved: latest history review not confirming:
  docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-18-RAW.md".
- [Observed] With a probe CONFIRM `HISTORY-REVIEW-19-RAW.md` binding the
  reviewed recorder digest committed in the probe clone, `--check` exits 0
  ("PASS owner direction observed; exact digest reconciled: …").
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL
  (53 checks)". `check_docs_review_campaign_partition.py`: unmatched=0,
  overlaps=0.

## (f) HISTORY-READING.md, round-18 additions

- [Observed] The rows 156–158 paragraph matches the rows: three predicates,
  the stated commit, killed. "the unrepaired selftest failed ('candidate
  input drift: vision.md')" is reproduced by my revert mutant.
- [Observed] The Round 18 entry's M1, N1, N3 and N4 dispositions match the
  code and the rows. The N2 disposition does not; see N1.

## Notes (non-blocking for the recorder)

- N1 [Observed] Round 18's N2 is dispositioned "not changed: the raw is
  named in this page and in the D8 log row" (`HISTORY-READING.md`, Round 18
  entry). At the reviewed commit row D8 of `DOCTRINE-AMENDMENT-LOG.md` names
  no reconciliation raw: it names the brief, says "(d2) adopted, not yet
  applied", and says "until then `vision.md` is unchanged" — false since
  1b0408e7 applied (d2), and the log is not in the branch's diff. Likewise
  `docs/README.md:74` says reconciliation review 1 is "dispositioned in row
  D8", which the row does not do. `HISTORY-READING.md` itself names the raw
  only by its pattern and as "reconciliation review 1". So the mitigation
  offered for N2 (an operator can find which raw bound `vision.md`) rests
  on a record that does not yet say it. Not revise-level here: none of these
  bytes is the recorder, this review binds only the recorder digest, and the
  repair (update row D8 to record (d2) applied, raw 1, its verdict and its
  notes' disposition, or reword the two citing sentences) retires nothing
  this verdict binds. It should land before merge.
- N2 [Observed] The reconciliation raw's exact verdict header form has no
  killing fixture: a mutant comparing `.strip()`ped headers survives, so a
  refactor could admit `Verdict:CONFIRM`, a trailing space or `\r` without
  the selftest noticing (round 18's probe showed the reviewed code refuses
  `\r`). [Unknown] whether `history_review`'s identical test is pinned; not
  measured here.
- N3 [Observed] Rows 156–158 record `f3e5ffa7…`, which is not an ancestor of
  the reviewed commit (`git merge-base --is-ancestor` exits 1; the branch was
  rewritten). The recorder bytes are identical at both commits and the
  stored fragments re-run at 6df6bdcd, so the rows remain re-runnable;
  `HISTORY-READING.md` could say the commit is off-branch.

## Probe record

Scripts outside every repository, under `/home/tze/.cache/review19b-scratch/tools/`:
`replay.py` (rule-6 row replay by `old`/`new` fragment, and non-row mutants
from `mutants.json`) and `probe.py` (real-Git probe trees on the probe clone,
reset to the reviewed commit before and after).

End of review.
