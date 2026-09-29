# History review 12 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 4f9df571826d17ef4ab0ae5b68818afdca6bb3ef
- `scripts/record_polaris_understanding_adoption.py`: `963c14dcca3e8043cdfd3e98040043c69d085dd1342e5a381cf595481588c95c`

Reviewer: an independent fresh-context agent, 2026-09-29. I cloned
`/home/tze/GitHub/syzygy`, fetched `recorder/successor-rows` and checked out
the reviewed commit.

- Subject: `git diff origin/main 4f9df57`, 8 files. The recorder diff adds
  the tool pin (`successor_tool`, `:42-54`), `successor_rows` (`:293-322`),
  the widened drift branch (`:446-452`), the frozen view's delegation
  (`:556-557`) and two selftest blocks [Observed].
- `git diff 6cbc037 4f9df57` touches only `HISTORY-READING.md` and adds
  `HISTORY-REVIEW-11-RAW.md`. The recorder bytes are the ones round 11
  reviewed [Observed].
- I computed the recorder digest above with `sha256sum` in the clone.
  `scripts/readability_successor.py` hashes to `88358478…8256`, equal to
  `SUCCESSOR_TOOL_SHA` (`:35`) [Observed].

## Criteria results

1. **Fail-closed** [Observed, except where marked].
   - **Any failing package.** The per-package `try` (`:309-316`) catches
     `Exception`, so it also catches `RecursionError`, `AttributeError` and
     `TypeError`. A package that fails grants nothing and marks nothing
     contested. Rows 70 and 71 kill both narrower widths.
   - **Foreign predecessor and non-row bytes** are refused by the exact-pair
     test at `:452`: `row == (digest(adopted), digest(current))`. The
     `CONTESTED` sentinel holds non-hex strings, so it cannot equal a pair of
     digests. A missing row (`None`) fails the same test.
   - **Edited tool** is refused before execution (`:45-46`, row 68).
     `exec(compile(source, …))` runs the bytes that were hashed. An absent
     tool yields no rows, and so drift is refused (row 73).
   - **Contested paths.** The key is `posixpath.normpath(path)` (`:319`).
     The marking at `:320` fires on every repeat key, whatever the order and
     whether or not the pairs are equal. The refusal at `:451` looks up only
     the drifting path, so uncontested paths keep their rows. The selftest
     asserts this (`:1146-1149`).
     - I reproduced the identical-claim case with `probe_identical.py`. Two
       packages restyle one path from one predecessor to the same bytes.
       Each records from the same base, and the aggregate takes a
       union-merge of the two sections.
     - Both packages check `performed-exact`. The path's row is `CONTESTED`
       [Observed].
   - **Scope.** Only the `current subject drift` branch is widened.
     - Subjects are the eight `CHANGE` paths. None is in `FROZEN_PATHS`
       (`:243-244`) or `HISTORY_PATHS` (`:250`). So the C1 retirement
       check is unaffected [Observed].
     - `Frozen` delegates to the same live rows. No other gate changed in
       the diff.
2. **HISTORY-READING statements** [Observed against code and tool].
   - The exception sub-bullets (lines 23-44) hold:
     - the pair test (`:452`);
     - the pin and hashed-bytes execution (`:42-54`);
     - per-package isolation (`:309-316`);
     - normalization and contested refusal (`:319-320`, `:451`);
     - the chain refusal. Once a second restyle performs, the first package
       drifts and is skipped. The second's predecessor is not the adopted
       digest [Inferred from tool `check()` `:257-260` and `:452`].
     - the working-tree trust disclosure.
   - The rule-6 paragraph's counts hold. Per commit, the JSON has
     `082a331` 3, `d50197f` 5, `4ff4ab7` 7, `90f12ae` 10, `1d5b534` 12 and
     `5f7edaf` 14, which are rounds 6 to 11, and 79 rows in all.
   - The three no-row statements (lines 100-108) are now true:
     - The rows cache (`:303-304`, `:321`) changes only how often the tool
       runs.
     - Hashing and executing one byte string closes the read/hash race.
     - Identical claims on a changed path are reachable by merging, and the
       code refuses them (probe above). No selftest fixture builds them.
       The selftest's two claimants carry different pairs: the second's
       predecessor is the first's row (`:1126-1127`).
   - "Row 42 predates that form" is true. Its refusal records a literal
     `/tmp/tmp…` path. Re-run at `4ff4ab7`, it prints the same refusal with
     a different temp name.
3. **Selftest and check** [Observed].
   - `--selftest` exits 0 with four PASS lines, including `57
     trust-boundary mutations refused`, `22 real-Git cases` and the
     successor rows line.
   - `--check` exits 1 with exactly `FAIL exact digest reconciliation
     unresolved: latest history review not confirming:
     docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-11-RAW.md`.
     This is the designed state.
4. **Rule-6 rows** [Observed].
   - Method:
     - I used one worktree per commit, detached at the row's commit.
     - `old` occurred exactly once. I applied `old→new` and ran the file's
       `command`.
     - A row passes on a non-zero exit plus its recorded refusal in the
       output, with `<tmpdir>` matched as `/tmp/[^/\s']+`.
     - I restored the tree between rows.
   - All fourteen rows at `5f7edaf` (65-78): 14/14 pass.
   - Earlier post-round-6 spot-checks: row 29 (`082a331`); rows 32 and 35
     (`d50197f`); rows 37, 40 and 42 (`4ff4ab7`); rows 44, 48 and 51
     (`90f12ae`); rows 54, 57, 60 and 63 (`1d5b534`). All 13 exit 1 with the
     refusal. Row 42 matches once its literal temp name is allowed to vary,
     as disclosed.
5. **Governance checks** [Observed].
   - `python3 scripts/check_governance.py` prints `31 OK, 21 WARN, 0 FAIL
     (52 checks)`.
   - `--selftest` prints `347 fixtures, 0 failing`.
   - `readability_successor.py --all --check` reports 3 packages, all
     `candidate-unperformed`.

### Round-11 dispositions (HISTORY-READING Round 11 bullet)

| Finding | Disposition | Result |
|---|---|---|
| R11 M1 | corrected no-row statement | Holds. Lines 104-108 now say that identical claims are reachable by merging, are refused, and have no row. This matches the code and my probe [Observed] |
| R11 N1 | line 87 wrapped; lines 9 and 81 stay whole | Holds. Only lines 9 (143 columns) and 81 (81) exceed 80. Line 9 holds a link and line 81 a code-span link [Observed] |
| R11 N2 | one package naming a file twice fails closed | Holds. It self-contests by normalized key [Inferred from `:318-320`] |
| R11 N3 | stands as round 9's N4 | Unchanged. The tool still imports `difflib` (tool `:38`) [Observed; not re-probed] |

The earlier dispositions (rounds 7-10) still hold in the code at `4f9df57`
[Observed]:

- the tool pin and hashed-bytes execution;
- per-package isolation over `Exception`;
- the two-claimant refusal, limited to the contested path;
- path normalization;
- the rows cache;
- the `<tmpdir>` form;
- the working-tree trust disclosure.

The spot-checked rows above still kill at their commits.

## Blocking findings

None.

## Notes

**N1 — The pinned tool couples packages through label substrings.**
[Observed by `probe_prefix.py`]

- Tool `check()` counts the aggregate lines that contain its own label
  (tool `:251`). So a performed package B, whose label contains A's label,
  makes A fail with "expected exactly one binding line".
- A then drops out of `successor_rows`. It neither grants a row nor contests
  B's claim.
- In the probe, A and B made the identical changed-path claim, and B's pair
  was granted instead of `CONTESTED`.
- The bytes granted are still a performed-exact successor's row, from the
  adopted predecessor, so nothing outside the exception's design is
  accepted.
- HISTORY-READING's statements stay literally true, because A is not
  `performed-exact` under the tool. This is a property of the pinned tool.
  It is not a recorder defect.

**N2 — Some failures outside the per-package `try` fail the whole check.**
[Inferred from `:306-309`]

- The candidates `glob`, `relative_to` and a symlinked tool run outside the
  `try`. So does the recorder's `read` refusing a symlinked tool.
- If one of them raises, the whole check fails. It does not skip one
  package.
- This is fail-closed and grants nothing.

**N3 — Carried from round 9 N4, round 10 N3 and round 11 N3.** The executed
tool resolves `difflib` through `sys.path[0]`. This is the recorder's own
import trust class [Inferred; not re-probed].
