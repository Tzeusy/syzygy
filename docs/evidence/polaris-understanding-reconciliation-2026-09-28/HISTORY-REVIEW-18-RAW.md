# History review 18 — reconciliation recorder
Verdict: REVISE
Reviewed commit: e93849ea825999949f5151157fe45b3bfbaefa24
- `scripts/record_polaris_understanding_adoption.py`: `9788c945b3589c1b2e3629a5f864212a5ccb5ab7daf522cebca34b75f6e717d1`

Reviewer: fresh-context independent reviewer (history review 18), 2026-10-15.

## Identity

- [Observed] Scratch clone HEAD is the reviewed commit (`git rev-parse HEAD`).
  Environment deviation: `/tmp` had 9 free inodes of 1,048,576 (`df -i /tmp`),
  so the brief's clone path under the scratchpad failed mid-checkout. The
  failed clone was removed and the review clone, a probe clone and a TMPDIR
  were made under `/home/tze/.cache/review18-scratch/` instead. Only this raw
  is written to the scratchpad path the brief names.
- [Observed] The recorder digest above was computed with `sha256sum` and
  again with Python `hashlib` over the same file; `git hash-object` of the
  working file equals `git rev-parse e93849ea…:scripts/record_polaris_understanding_adoption.py`
  (blob a13bd77c7f17d38d279bd941ba031a066a8a5438), so the hashed bytes are
  the committed bytes.
- [Observed] `git diff --stat a4a864e6 e93849ea` touches exactly three files:
  the recorder, `HISTORY-READING.md` and `history-reading-rule6.json`.
  `git diff --stat ea764977 e93849ea` touches only the two evidence files, so
  the recorder bytes the rule-6 rows ran at (`ea764977`) are the reviewed bytes.

## Criterion 1 — the code implements the published predicate

Reading of `successor_bindings`, `reconciliation_reviews`,
`reconciliation_population` and the changed `reviewed_template` against the
HISTORY-READING.md bullet "A later vision.md, under a fresh reconciliation
review":

- [Observed] Population and retention: same Git query as the history
  population (`--no-renames --full-history --diff-merges=combined
  --diff-filter=A --name-only -z`) over `docs/reviews/`, joined with the
  on-disk listing; numbering 1..n by integer; deletion, double-add,
  never-committed, changed-since-introduction, introduction == C2 and
  C2-not-ancestor are each refused.
- [Observed] Near-miss names: any basename under `docs/reviews/` or below
  that `re.search`es `understanding[^a-z0-9]*reconciliation` (IGNORECASE) and
  is not the strict top-level name is refused.
- [Observed] Latest raw: exactly one `Verdict:` header equal to ` CONFIRM` or
  ` CONFIRM WITH EXCEPTIONS`; exactly one `Reviewed commit:` header that is a
  full lowercase 40-hex SHA (provenance only, never resolved); the binding
  lines, sorted, must equal `SUCCESSOR_BOUND`, which evaluates to the seven
  paths README.md, proof.json, technical-record-template.json,
  final-documentation.patch, documentation-images.json, review-inputs.json,
  vision.md (`{*FROZEN_PATHS, INPUTS} - set(HISTORY_PATHS)`, line 271).
- [Observed] Only `REBINDABLE = (VISION,)` may differ from C1's binding
  (line 744); today's bytes of every non-history input must equal
  `successor.get(path, sha)`; the frozen `candidate_check` view reads
  `vision.md` at C1.

Real-Git probes, each a fresh tree off the reviewed commit in a scratch clone,
run once as-is (the expected HISTORY-REVIEW-17 refusal marks "reconciliation
predicate passed") and once with a probe `HISTORY-REVIEW-18-RAW.md` binding the
recorder so the whole `--check` runs to its end:

| Probe | `--check` with probe history raw 18 |
|---|---|
| no change | PASS |
| vision.md amended, no raw | FAIL review retired by changed input: vision.md |
| vision.md amended, raw 1 CONFIRM binding it | PASS |
| same, CONFIRM WITH EXCEPTIONS | PASS |
| raw 1 on disk, not committed | FAIL reconciliation review not retained |
| raw 1 REVISE | FAIL latest reconciliation review not confirming |
| raw 1 CONFIRM then raw 2 REVISE | FAIL latest … not confirming: …-2-RAW.md |
| raw binds a different vision digest | FAIL review retired by changed input: vision.md |
| template changed and rebound by the raw | FAIL reconciliation review moved a fixed input: template |
| README.md changed and rebound | FAIL … moved a fixed input: README.md |
| review-inputs.json rewritten to the new vision digest and rebound | FAIL … moved a fixed input: review-inputs.json |
| review-inputs.json reformatted (same JSON) and rebound | FAIL … moved a fixed input: review-inputs.json |
| REVIEW-RAW.md changed beside a valid raw | FAIL retained C2 review changed |
| raw carries an eighth binding line (the recorder's) | FAIL reconciliation review input population |
| raw 1 edited in a later commit | FAIL retained reconciliation review changed |
| only raw 2 (gap) | FAIL reconciliation review numbering is not 1..n |
| `R-POLARIS-UNDERSTANDING-RECONCILIATION-PLAN.md` beside raw 1 | FAIL malformed reconciliation review name |
| valid raw placed in the evidence directory instead | FAIL review retired by changed input: vision.md |
| `Verdict: CONFIRM\r` | FAIL latest … not confirming |
| vision.md deleted, raw binds the empty digest | FAIL missing evidence: vision.md |

- [Observed] No probe tree made `--check` pass with a changed C1 input other
  than vision.md, with a vision.md no confirming retained raw binds, with
  REVIEW-RAW.md changed, or with a REVISE latest raw.

## Criterion 2 — the owner's Q-A1 arm

- [Observed] `HISTORY_PATHS` (line 250) is unchanged and does not contain
  `VISION`; the diff adds no path to it. `REVIEW-RAW.md` is not in the diff,
  and its C2 retention test is unchanged. The owner's answer, "Re-review over
  the amended vision.md.", is quoted at `DOCTRINE-AMENDMENT-LOG.md:13`.
- [Observed] The brief (§"What the Q-A1 path therefore needs", item 1)
  suggested, "for example", a successor raw "in the evidence directory"; the
  change puts the raws in `docs/reviews/`. HISTORY-READING.md states the
  placement and its reason. Not a deviation from the owner's choice.

## Criterion 3 — rule 6

- [Observed] Rows 127–155 are 29 rows, each `killed: true`, commit
  `ea764977…`, with `old`/`new` fragments. I re-ran 11 of them (127-155
  sample: 129, 134, 135, 140, 144, 146, 148, 150, 152, 153, 155) in a scratch
  clone: each `old` fragment occurs exactly once, each mutated selftest exits
  1, and each row's recorded refusal text appears in the output. The clone was
  clean after each restore.
- [Observed] Mutants I wrote that are not rows (selftest result):
  - exempt review-inputs.json from the fixed-input test
    (`if path not in REBINDABLE + (INPUTS,):`): **survives** (exit 0). See M1.
  - drop the `$` anchor from the successor binding regex (line 739): survives
    (exit 0). N1.
  - loosen the reviewed-commit test to `r' .{40}'` (line 737): survives
    (exit 0). N1.
  - make the added-once guard never fire: killed
    (`reconciliation mutation accepted: add-reconciliation-review-twice`).

### M1 — the fixed-input test's only non-redundant reach has no killing fixture

- [Observed] The only fixture that reaches "reconciliation review moved a
  fixed input" rebinds `technical-record-template.json` (line 1167). For that
  path, and for README.md, proof.json, the patch and the image list, the
  original freeze's `candidate_check` refuses the same tree anyway
  ("candidate input drift" or a canonical mismatch), which is why rows 145 and
  146 fail only by "wrong reconciliation refusal: candidate input drift".
  `review-inputs.json` is not one of its own rows, so for that one path the
  fixed-input test is the sole guard, and no fixture rebinds it.
- [Observed] With the scope mutant above applied and committed in a probe
  tree, and a probe history raw binding the mutated bytes, `--check` PASSES a
  tree whose `review-inputs.json` is reformatted (same JSON, new bytes) and
  rebound by a CONFIRM raw beside an amended vision.md. Unmutated, the same
  tree FAILS with "reconciliation review moved a fixed input:
  …/review-inputs.json". So the reviewed code is correct, but the selftest
  would not notice a refactor that drops this arm, and that arm is precisely
  the published promise "each of the other six bindings must equal C1's"
  for the one input nothing else protects.
- [Inferred] The exposure the mutant opens is bounded — `candidate_check`
  still requires the parsed rows to match, so only formatting, key order or
  duplicate-key bytes could move — but criterion 1 asks exactly whether a
  changed C1 input other than vision.md can pass, and rule 6 requires the
  check to fail per predicate before it is trusted.
- HISTORY-READING.md's sentence that rows 127–155 pin "the fixed-input test
  and its scope" is true of the rows as written but overstates what they
  prove: row 146's scope mutant exempts a path the freeze already guards.
- Repair: add a fixture that rebinds `review-inputs.json` to new bytes with
  unchanged rows (e.g. re-indented JSON) and expects "reconciliation review
  moved a fixed input: …/review-inputs.json", plus a rule-6 row for the
  `REBINDABLE + (INPUTS,)` scope mutant.

## Criterion 4 — expected state

- [Observed] `--selftest` (TMPDIR on the /home disk) exits 0: "6 valid
  states …; 89 trust-boundary mutations refused", "history population
  selftest: 27 real-Git cases", successor rows selftest PASS.
- [Observed] `--check` exits 1 with exactly "FAIL exact digest reconciliation
  unresolved: latest history review does not bind the current recorder:
  docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-17-RAW.md".
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL
  (53 checks)".

## Criterion 5 — HISTORY-READING.md accuracy

- [Observed] The bullet's statements on numbering, retention, the near-miss
  pattern, the header rules, the seven-path population, the single rebindable
  path, the frozen view and the unchecked reviewed commit each match the code
  (lines 265–271, 399–411, 687–747, 613–633).
- [Observed] "`docs/README.md` gives them a campaign row": importing
  `check_docs_review_campaign_partition.matches` on
  `docs/reviews/R-POLARIS-UNDERSTANDING-RECONCILIATION-1-RAW.md` returns
  `['polaris-understanding']`, one campaign, so the claim holds.
- [Observed] "Nine fail by an exception or a different refusal": the nine
  named are rows 134 (missing evidence), 135 (type error), 136 and 137 (blob
  at an absent commit), 142 (IndexError), 143 (KeyError, printed as the bare
  quoted path), 145 and 146 (candidate input drift), 151 (IndexError). The
  recorded refusals match that list and its count; the other twenty fail by
  "mutation accepted" assertions or by a valid state refused with the
  predicate's own reconciliation refusal.
- The "fixed-input test and its scope" wording: see M1.

## Criterion 6 — fail-closed polarity versus the predecessor

- [Observed] With no reconciliation raw, `successor_bindings` returns `{}`
  and every comparison is the predecessor's (row 151 pins the early return).
  The new code adds refusals and one exemption, scoped to vision.md under a
  confirming retained raw. No predecessor refusal was removed in the diff.
- [Observed] Any `docs/reviews/` basename matching the near-miss pattern now
  breaks `--check` even when vision.md is unchanged. Fail-closed; today no
  tracked or historical `docs/reviews/` path matches (the `--check` result
  above reaches the history-review refusal).

## Notes (non-blocking)

- N1 [Observed] Two predicate details have no killing fixture: the `$` anchor
  of the successor binding regex (line 739) and the hex-only class of the
  reviewed-commit test (line 737; `bad-commit` is not 40 characters, so a
  `.{40}` mutant survives). The code refuses both shapes; the selftest does
  not pin them. A fixture with an uppercase or non-hex 40-character commit,
  and one with a trailing-text binding line, would.
- N2 [Observed] The `--check` PASS line is the same whether vision.md is
  bound by C1 or by reconciliation raw n. An operator cannot see from the
  output which binding applied; naming the raw in the PASS line would make
  the admission visible.
- N3 [Observed] A committed confirming raw plus an uncommitted vision.md
  edit passes (`--check` reads the working tree). This is the predecessor's
  behaviour for every C1 input, not new in this change.
- N4 [Inferred] The latest raw's binding is the reviewer's claim and its
  reviewed commit is never resolved, as HISTORY-READING.md says. Whoever
  briefs the fresh reconciliation review should quote this raw-head contract
  (seven binding lines, no other line of that form — so the reviewer must not
  bind the recorder in that form) in the brief, per the recorder-head lesson.

## Probe record

Scripts (scratch, outside every repository): `probe.py` (real-Git probe
trees; `PROBE_H18`, `PROBE_MUT`, `PROBE_ONLY` switches), `replay.py` (rule-6
row replay by `old`/`new` fragment), `mutant.py` (non-row mutants), under
`/home/tze/.cache/review18-scratch/`; all run against the probe clone reset to
the reviewed commit, and the review clone's `git status --porcelain` was
empty at the end.
