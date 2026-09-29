# History review 11 — reconciliation recorder
Verdict: REVISE
Reviewed commit: 6cbc03740e6b9e77bee99078e316498b40d9db95
- `scripts/record_polaris_understanding_adoption.py`: `963c14dcca3e8043cdfd3e98040043c69d085dd1342e5a381cf595481588c95c`

Reviewer: an independent fresh-context agent, 2026-09-29. I cloned
`/home/tze/GitHub/syzygy`, fetched `recorder/successor-rows` and checked out
the reviewed commit.
- Subject: `git diff origin/main 6cbc037`. It touches 7 files; the recorder
  diff adds the tool pin, `successor_rows`, the widened drift branch, the
  frozen view's delegation and two selftest blocks [Observed].
- I computed the recorder digest above with `sha256sum` in the clone
  [Observed].
- `scripts/readability_successor.py` hashes to `88358478…8256`, equal to
  `SUCCESSOR_TOOL_SHA` (recorder `:35`) [Observed].

## Criteria results

1. **Fail-closed.** The code refuses everything the criterion names
   [Observed, except where marked].
   - **Any failing package.** The per-package `try` catches `Exception`
     (`:315`). Malformed, deeply nested, wrongly typed (including listed
     pins, which raise `AttributeError`), unperformed and drifted packages
     are skipped and block nothing else. Rows 70 and 71 kill both narrower
     widths.
   - **Foreign predecessor and non-row bytes** are refused by the exact-pair
     test (`:452`, rows 65, 66, 76, 78).
   - **Edited tool** is refused (`successor_tool`, row 68). The executed
     bytes are the hashed bytes (`exec(compile(source, …))`).
   - **Contested paths.** Keys are `posixpath.normpath(path)` (`:319`). This
     folds `a//b`, `./a/b`, `a/./b`, `a/b/` and `a/b/.` to `a/b` [Observed
     by a one-line check]. The pinned tool refuses absolute paths
     (so `//a/b`, which `normpath` keeps), `..` and symlinked components
     (tool `:68-72`). So every alias of one file the tool will read
     normalizes to one key [Inferred from the tool's `read`]. The marking
     at `:320` is order-independent and fires for every repeat claim,
     identical or not. The refusal at `:451` touches only that key; the
     selftest asserts the uncontested path keeps its row. Round 10's M1 is
     closed.
   - **Scope.** Only the drift branch of `baseline_proof` (`:446-452`) is
     widened. `Frozen` delegates to the same rows (row 72). No other gate
     changed in the diff.
2. **HISTORY-READING claims.** One statement is false for a reachable input
   (M1: lines 103-107). The other exception sub-bullets (lines 23-44) and
   the rule-6 paragraph's counts hold.
   - The row counts are 5, 7, 10, 12 and 14 for rounds 7 to 11. They match
     the per-commit counts in `history-reading-rule6.json`: `d50197f` 5,
     `4ff4ab7` 7, `90f12ae` 10, `1d5b534` 12 and `5f7edaf` 14 (79 mutants in
     all) [Observed].
   - The fourteen round-11 rows (indices 65-78) map one-to-one onto the
     fourteen guards named on lines 94-98 [Observed].
   - The chain sentence (lines 39-40) holds. Once a second restyle
     performs, the first package's subjects drift, so its `check()` raises
     and it is skipped. The second package's predecessor is not the adopted
     digest, so the pair test refuses [Inferred from tool `check()` and
     `:452`].
3. **Selftest and check** [Observed].
   - `--selftest` exits 0 and prints four PASS lines, including `57
     trust-boundary mutations refused`, `22 real-Git cases` and the
     successor rows line.
   - `--check` exits 1 with exactly `FAIL exact digest reconciliation
     unresolved: latest history review not confirming:
     docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-10-RAW.md`.
     This is the designed state.
4. **Rule-6 rows** [Observed].
   - Method: one clone per commit, checked out at the row's commit. `old`
     occurred exactly once, `old→new` was applied, and the file's `command`
     was run. `<tmpdir>` was matched as `/tmp/[^/]+`. The tree was restored
     between rows.
   - Rows 65-78 at `5f7edaf`: 14/14 exit 1 and print their recorded
     refusal.
   - Spot-check of earlier post-round-6 rows 31, 34 (`d50197f`), 37, 39
     (`4ff4ab7`), 43, 46, 50 (`90f12ae`), 53, 55, 58, 61 and 64
     (`1d5b534`): 12/12 exit 1 and print their recorded refusal.
5. **Governance checks** [Observed].
   - `python3 scripts/check_governance.py` prints `31 OK, 21 WARN, 0 FAIL
     (52 checks)`.
   - `--selftest` prints `347 fixtures, 0 failing`.
   - `readability_successor.py --all --check` reports 3 packages, all
     `candidate-unperformed`.

Round-10 dispositions (HISTORY-READING Round 10 bullet) checked:

| Finding | Disposition | Result |
|---|---|---|
| R10 M1 | path normalization and an aliased-claimant fixture | Holds (`:319`; the selftest's second package spells `…/./proposal.md`; row 74 kills dropping `normpath`) [Observed] |
| R10 N1, first half | listed-pins fixture | Holds. Row 71 (narrowing to `(ValueError, OSError, RecursionError, TypeError)`) is killed by `AttributeError: 'list' object has no attribute 'values'` [Observed] |
| R10 N1, second half | the no-row statement above | Does not hold. The statement is false (M1) |
| R10 N2 | line 36 wrapped | Holds; lines 35-38 are now wrapped [Observed]. See N1 |
| R10 N3 | stands as round 9's N4 | Unchanged [Inferred; not re-probed] |

Earlier dispositions (rounds 7-9) still hold. The tool pin, per-package
isolation, the two-claimant refusal, the working-tree trust disclosure
(lines 41-44), the rows cache, `RecursionError` containment, `<tmpdir>`,
executing the hashed bytes, containing every exception and refusing only
the contested path are all present in the code at `6cbc037`. The spot-checked
rows above still kill at their commits [Observed].

## Blocking findings

**M1 — HISTORY-READING lines 103-107 are false. Two performed-exact
packages can make one identical claim for a path both change, and there
the contested marking decides between refusing and accepting.** [Observed]

The page says (lines 103-107): "Marking two identical claims as contested
changes no outcome. Two exact packages can make one identical claim only
for a path neither changes, where the predecessor equals the row and
today's bytes."

A reachable counterexample:
- Two candidate packages, A and B, restyle the same subject from the same
  predecessor to the same bytes.
- Each is recorded on its own branch from one base. Each `record()` runs
  while the other is still unperformed, so each passes its
  `candidate-unperformed` precondition.
- A merge brings them together. The subject's bytes are identical on both
  sides, and the aggregate takes both appended sections: the union merge
  the repository already uses for append-only registers.

Probe (`probe_identical.py`, scratch temp root, the tool's `synthetic`,
`pin` and `record`, simulating that merge):
- `module.packages(root)` reports both packages `performed-exact`.
- Both claim `(e05fb1d2…b154, 8de181a0…6ee1)` for
  `openspec/changes/example/proposal.md`. The predecessor differs from the
  row, so the path is changed, not unchanged.
- At `6cbc037`, `Evidence(root).successor_rows()[proposal]` is `CONTESTED`,
  so the recorder refuses. The code is correct.
- Mutant, applied once at `:320`:
  `rows[key] = CONTESTED if key in rows else …` →
  `rows[key] = CONTESTED if key in rows and rows[key] != (predecessor, successor) else …`.
  The same probe then returns the shared pair, not `CONTESTED`. With the
  predecessor equal to an adopted digest, `baseline_proof`'s pair test
  (`:452`) would accept the subject.
- That mutant **survives** `--selftest` (exit 0). The selftest's two
  claimants share the proposal but with different pairs: the second
  package's predecessor is the first package's row.

So the marking is load-bearing for identical claims. It is not pinned by
any row. The page's reason for giving it no row is a false statement about
what the code does. This is blocking under criterion 2 and the brief's
severity rule. No bytes are wrongly accepted today: the code refuses.

Required, either of:
- (a) Add an identical-claim fixture to `successor_rows_selftest`: two
  performed-exact packages, each recorded from the same base, one path,
  the same pair. Assert `CONTESTED`. Add a rule-6 row with the mutant
  above. Drop the third no-row statement and correct "Three guards have no
  row" to two.
- (b) Or replace lines 103-107 with a true statement, for example that
  identical claims are reachable by merging two independently recorded
  packages, that the marking refuses them, and that no row pins it.

## Notes

**N1 — Three lines of HISTORY-READING exceed 80 columns.** Line 9 (143
columns, a link), line 81 (81) and line 87 (117: "…not a fixture. The two
round-3 witnesses (dropping `| set(listed)`, and widening"). Line 87 was
last touched at `6cbc037`, this branch. This is cosmetic. No code span is split across
a line break [Observed].

**N2 — A single package naming one file twice is refused, not granted.**
The page talks only of two packages. A package whose `predecessor` names
both `x` and `./x` is contested against itself by the normalized key, so
that path is refused. This is fail-closed and consistent with the code.
The page does not claim otherwise [Inferred from `:318-320` and tool
`manifest_rows`].

**N3 — Carried from round 9 N4 and round 10 N3.** The executed tool
resolves `difflib` through `sys.path[0]`. This is the recorder's own
import trust class [Inferred; not re-probed].
