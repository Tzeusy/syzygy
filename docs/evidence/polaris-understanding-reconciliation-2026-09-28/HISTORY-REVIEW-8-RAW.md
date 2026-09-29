# History review 8 — reconciliation recorder
Verdict: REVISE
Reviewed commit: b2b4ed382135b123e62f53c5ca8a8d36d9e9e965
- `scripts/record_polaris_understanding_adoption.py`: `3003c48d691f7022ccf476e3a9a24900429792a03c2609241e7636a3a068293a`

Reviewer: independent fresh-context agent, 2026-09-29. Clone of
`/home/tze/GitHub/syzygy` with `recorder/successor-rows` fetched, checked out at
the reviewed commit. Subject: `git diff origin/main b2b4ed3` (4 files, +459/−6;
the recorder +154/−6). Digests computed with `sha256sum` in the clone
[Observed]: the recorder is `3003c48d…293a` and `scripts/readability_successor.py`
is `88358478…8256`. Both equal the brief's values and the pin at recorder line 33.

## Criteria results

1. **Fail-closed.** [Observed]
   - The tool pin refuses edited bytes (`:293-294`; row 38 kills it).
   - A foreign predecessor and non-row bytes are refused by the exact-pair
     test in `baseline_proof` (rows 36/37).
   - A missing tool grants nothing (`:292`).
   - Unperformed packages grant nothing (`:301`).
   - A malformed sibling (`{`) is isolated (`:305`). One escape remains (N1).
   - The only widening in `baseline_proof` is the drift branch. The `Frozen`
     view delegates to the same live rows (`:543-544`), and the population
     check and every other gate are untouched [Observed from the diff].
   - Every failure I found refuses. None grants.
2. **HISTORY-READING claims.** The claim "at most one package checks exact
   for a path" is **false**. I built a counterexample with the pinned tool
   (M1). The working-tree trust disclosure (HISTORY-READING lines 38-41) is
   accurate: `Package.check()` reads the act, the aggregate and the review
   raw with `read()` from the working tree (`readability_successor.py:235-256`).
3. `--selftest` exits 0 and prints four PASS lines, including `56
   trust-boundary mutations refused` and `PASS successor rows selftest:
   absent tool, unperformed, performed, malformed sibling, edited tool,
   displaced and drifted packages` [Observed]. `--check` exits 1 with exactly
   `FAIL exact digest reconciliation unresolved: latest history review not
   confirming:
   docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-7-RAW.md`
   [Observed]. This is the designed state.
4. **Rule-6 rows.** `history-reading-rule6.json` has 43 mutants. The rows
   added after HISTORY-REVIEW-6 are indices 31–42 (12 rows): 5 at `d50197f`
   and 7 at `4ff4ab7`.
   - Each ran in its own fresh clone at the row's commit. `old` occurred
     exactly once, `old→new` was applied, and the file's `command` was run
     (`python3 scripts/record_polaris_understanding_adoption.py --selftest`).
   - 12/12 exited 1, and 12/12 printed their recorded refusal [Observed].
   - Row 42's recorded refusal embeds a random tempdir path
     (`/tmp/tmp3n25cwo5/…`), so it can only match up to that path. The prefix
     and the `scripts/readability_successor.py` tail matched (N3).
   - `4ff4ab7` and `b2b4ed3` have identical recorder bytes: the diff between
     them touches only the two docs files [Observed].
   - Guards without a killing row are listed in N2.
5. `python3 scripts/check_governance.py` prints `31 OK, 21 WARN, 0 FAIL (52
   checks)` and exits 0. `--selftest` prints `347 fixtures, 0 failing` and
   exits 0 [Observed].

Round-7 dispositions (HISTORY-READING lines 126-132) against the code:

| Finding | Disposition | Result |
|---|---|---|
| M1 | tool pin | Answered (`:29-33`, `:293-294`, row 38) [Observed] |
| N1 | per-package isolation | Answered for `{`, `[1]`-style keys and non-string fields. One escape remains (N1 below) [Observed] |
| N2 | "the displacement rule (one exact package per path)" | **Not answered.** The rule does not hold (M1) [Observed] |
| N3 | disclosed | Answered (lines 38-41) [Observed] |
| N4 | round-8 rows | Partly answered: the performed filter, the missing-tool guard and the predecessor and row tests now have rows. The row-value guard R7 asked for has none (N2 below) [Observed] |
| N5 | rows cache | Answered, and `spec_from_file_location` now follows the `is_file()` test [Observed] |
| N6 | none | Nothing to answer. The figures "56, was 54", "Five more (round 7)" and "Seven more (round 8)" match the rows and the selftest output [Observed] |

## Blocking findings

**M1 — "At most one package checks exact for a path" is false, so N2 of
round 7 is still open. The selftest's "displaced" case passes only because
the synthetic fixture reuses one review-raw path.** [Observed]

Where the claim is made:
- HISTORY-READING.md lines 34-37: "At most one package checks exact for a
  path: a later successor changes the change directory, so the earlier one
  stops checking exact."
- The recorder docstring at `scripts/record_polaris_understanding_adoption.py:281-284`
  says the same.
- HISTORY-READING line 128 answers round-7 N2 ("ranking by directory name")
  "by the displacement rule above".

The mechanism fails whenever a later package lists the path as a subject but
leaves it unchanged. The tool allows this: `subjects` is the `predecessor`
key set (`readability_successor.py:87`), and `proposed()` needs only one
changed subject (`:109-110`). The later package's row for that path is then
`(R, R)`, today's bytes do not change, and the earlier package still checks
`performed-exact`.

The selftest's second package (`:1081-1105`) is exactly this case: it shares
the proposal unchanged. The first package stops checking exact there only
because `readability_successor.pin()` always writes the one path
`docs/reviews/R-EXAMPLE-RAW.md` (`readability_successor.py:349-352`). Pinning
the second package overwrites the first package's pinned raw, and the first
then fails `validate_pins` ("review raw … differs from its pinned sha256"). I
reproduced that refusal with the selftest's own construction.

Counterexample, run with the pinned tool (`88358478…`):
- **Setup.** I used the selftest's construction, but gave the second
  package's review its own raw (`docs/reviews/R-EXAMPLE-2-RAW.md`) and put the
  first raw's bytes back.
- **Both packages check exact.** `Package.check()` returned `performed-exact`
  for both `example-readability-successor` (subjects `proposal.md`,
  `spec.md`) and the second package (subjects `design.md`, `proposal.md`).
- **Second package named `example-second-readability-successor`** (sorts
  last). `Evidence(root).successor_rows()['…/proposal.md']` is `(8de181a0…,
  8de181a0…)`, the restyled bytes to themselves. The recorder would refuse
  the lawful adopted→restyled pair `(e05fb1d2…, 8de181a0…)` with `current
  subject drift`.
- **Second package named `aa-example-second-readability-successor`** (sorts
  first). The rows give `(e05fb1d2…, 8de181a0…)`, and the recorder would
  accept.
- Script: `$S/probe_two2.py`, run as `python3 probe_two2.py repo <name>`.

So the outcome still depends on directory order, which is round-7 N2
unchanged. Two surviving mutants confirm that the selftest does not pin
precedence [Observed]. Each was applied at `b2b4ed3` and `--selftest` still
exited 0:
- `rows[path] = (predecessor, successor)` →
  `rows.setdefault(path, (predecessor, successor))` (first wins);
- `sorted(... .glob(...))` → `sorted(..., reverse=True)`.

Severity:
- Fail-closed only. A forged or foreign pair is never accepted, because
  acceptance still needs `(adopted digest, today's digest)` exactly.
- No two of today's 3 packages share a subject: 38 subject paths, 0 shared
  [Observed]. The case is therefore latent. It arises only if a later
  successor lists one of these 8 amendment files as an unchanged subject.

It is blocking because it fails acceptance criterion 2. A claim on the page
that binds the recorder, the recorder's own docstring and a round-7
disposition are false, and a selftest case asserts a property it does not
test.

Required, either of:
- (a) Make the rule true in code. For example, when more than one
  performed-exact package names a path, grant the pair only if some package
  records `(adopted, current)` for it. Alternatively, keep every exact pair
  per path and accept a match. Then fix the fixture so that each package pins
  its own raw, and add a rule-6 row that kills first-wins and last-wins
  precedence.
- (b) Or keep the code, and replace the claim and the N2 disposition with the
  true behaviour: several packages may check exact for a path, and the last
  in sorted directory order decides, fail-closed. Re-describe the selftest
  case as what it tests.

## Notes

**N1 — The per-package isolation has one escape: `RecursionError`.**
[Observed]
- A sibling `zz-deep/SUCCESSOR.json` made of 200,000 nested `[` and `]`
  raised `RecursionError` out of `successor_rows()`. It is not in the tuple at
  `:305`, and it is not in `main`'s tuple at `:1139`.
- This is fail-closed (non-zero exit with a traceback), but it contradicts
  "blocks no other package" (HISTORY-READING line 33).
- By contrast, a config with `"label": 5` raised `TypeError` inside `Package`
  and was isolated. It returned `{}`.

**N2 — Guards in the diff with no killing row, besides the rows cache.**
[Observed] Each mutant was applied once at `b2b4ed3`, then `--selftest` was run.
- **Row value.** `pairs = [(path, package.predecessor[path], installed[path])`
  → `(path, installed[path], installed[path])` (`:304`), or
  → `(path, package.predecessor[path], package.predecessor[path])`. Both are
  killed by `performed successor row`, but no row pins them. Round 7 N4 asked
  for this one as a security-polarity row.
- **Except tuple.** Removing `KeyError, TypeError` from the tuple at `:305`
  **survives**: the selftest still passes. Row 40 narrows the tuple only to
  `OSError`, so it is killed through `JSONDecodeError`. The `TypeError` member
  does live work: the `"label": 5` package above escapes without it
  [Inferred from the Python semantics; the isolated case was Observed].
- **Precedence.** Last-wins at `:308` and the sort order survive (M1).
- The rows cache (`:288-289`): removing it survives, as the page says (line
  92).

**N3 — Row 42's refusal cannot be reproduced literally.** It records a
`tempfile` path. A re-run can match only the prefix `FAIL exact digest
reconciliation unresolved: [Errno 2] No such file or directory:` and the
suffix. Consider recording the stable part only, or a pattern.

**N4 — Minor.**
- The pin is checked on one read (`:293`), and `exec_module` then re-reads
  the file (`:295-297`). That is a check-then-use gap on the working tree. It
  is cosmetic under the disclosed working-tree trust.
- `successor_rows_selftest` loads the tool from `ROOT` (`:1044-1047`), not
  through the pin. A tool edit therefore surfaces there as the `edited tool`
  expectation failing indirectly rather than as a named refusal. This is
  acceptable.
