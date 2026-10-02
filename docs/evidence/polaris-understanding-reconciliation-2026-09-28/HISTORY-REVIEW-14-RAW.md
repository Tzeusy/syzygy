# History review 14 — reconciliation recorder
Verdict: REVISE
Reviewed commit: 249a9d81611d0109de5fd816bc03b5fe5a655ea6
- `scripts/record_polaris_understanding_adoption.py`: `f45a5679f42792c590ac79b1a74bbbf51b926705861e9a649e9f616cc036a559`

Reviewer: fresh-context agent, 2026-10-02. Scratch clones: `hist14/repo` (at 249a9d8)
and `hist14/post` (249a9d8 plus two scratch commits: placeholder raws and pins,
then the performed dependency-union successor). Probe scripts under `hist14/bf/`.
No repository file was edited outside the scratch clones.

[Observed] Recomputed sha256 at 249a9d8: recorder as in the head line above;
`scripts/readability_successor.py` is
`fdb4e483978dbe005249f60744bcdeec16ec5c4a8c71ca6bf37f018dd8afbdad`, equal to the
recorder's `SUCCESSOR_TOOL_SHA`. Diff base 6a013e8: four files changed (the tool,
the recorder, `HISTORY-READING.md`, `history-reading-rule6.json`).

## Criterion 1 — fail-closed chain

[Observed] The straightforward cases hold. In `hist14/post`, after performing
the union successor, a foreign digest written to `GOVERNING-DEPENDENCIES.md` is
refused by the tool (both packages that list the file) and by the recorder
(`current subject drift`). The tool's selftest covers foreign predecessor,
unperformed and partially recorded later packages; the recorder's composition
table covers forks, a repeated step, a cycle with no first digest, a second
chain and an off-chain unchanged claim. A step's `performed_rows` verifies the
act record, the aggregate block and the pins, and any exception in a sibling
package grants nothing.

[Observed] Three ways remain in which a state is accepted that no performed later
chain installed over the earlier row. All three were reproduced on real
fixtures built with the tool's own `synthetic`/`pin`/`later` helpers
(`hist14/bf/fixture.py`, `hist14/bf/alias.py`), and a brute-force model over
four digests and up to four packages (`hist14/bf/bf*.py`, using the recorder's
real `chain`) found 360 tool-green, recorder-accepted states that no
recording order of the performed packages can reach.

1. Recorder `chain()` absorbs a repeated step (M1). With packages A→B, A→B
   (a second package from the adopted bytes, e.g. two branches merged), B→C and
   C→B, every package checks `performed-exact`, and `chain` returns (A, C):
   `dict(steps)` silently drops the duplicate A→B, and the walk re-traverses
   B→C to make up the node count, so `len(nodes) == len(steps) + 1` passes.
   The last act installed B; the recorder refuses B and accepts C after a
   no-act edit to C. The docstring and `HISTORY-READING.md` both say a repeated
   step makes the file contested.
2. The tool's `later_rows` is unordered (M2). It follows any performed
   package's step, including earlier packages, so "later" is not enforced.
   Packages A→B, B→C, C→B (head B): after a no-act edit to C, all three report
   `performed-exact` (the C→B package's row B reaches C through the earlier
   B→C step). With A→B, B→A (head A), a no-act edit to B is also all green.
   The recorder refuses both (row (A, B) against C; the second is a cycle,
   CONTESTED), so only `--all --check` is false-green there.
3. The tool's `later_rows` includes the package itself (M3), see criterion 2.

[Observed] The pattern followed, `_later_rows` in
`scripts/record_pwb_behavior_amendment_acts.py` (lines 605-620), is laxer still
(any other performed manifest's row, no chain). The new tool is stricter than
that pattern, but the acceptance criterion here asks for refusal by both tools.

[Inferred] None of the three states exists in the repository today: they need
a digest cycle (a successor that restores earlier bytes) or a duplicated or
aliased claim. They are nonetheless exactly the classes the brief names.

## Criterion 2 — pre-change behaviour preserved

[Observed] At 249a9d8: tool `--selftest` 37 fixtures, 0 failing; recorder
`--selftest` prints four PASS lines and no FAIL; `readability_successor.py --all
--check` passes 4 packages (3 performed-exact, the union candidate-unperformed);
recorder `--check` fails only on `latest history review does not bind the current
recorder: ...HISTORY-REVIEW-13-RAW.md`, expected until this review is retained.

[Observed] One previously refused state is now accepted (M3). A package whose
config names one file twice, `x` changed and `./x` kept, was refused by the
6a013e8 tool at `--record` (`subject differs from its successor row: ./x`). The
249a9d8 tool records it and reports `performed-exact`: `later_rows('./x', A)`
normalizes the key and finds the package's own (A, B) step for `x`. Its
manifest then permanently says the file is at A while it is at B. The recorder
would compose (A, B) and (A, A) to (A, B) (selftest case "an unchanged claim of
the first digest"), where before two claims on one path were CONTESTED.

[Observed] For a path no other package claims, `later_rows` returns at most the
row itself, so a lone package stays strict, as before. Other pre-change
refusals spot-checked in fixtures stay refused (foreign predecessor, drift,
unperformed, partial).

## Criterion 3 — rule 6

[Observed] `history-reading-rule6.json` has 94 mutants; the 15 at commit ab2a58b
are the round-14 rows (7 tool, 8 recorder). I reproduced nine of them in
throwaway copies of `hist14/repo` (`hist14/bf/rule6.py`), each `old` fragment
occurring exactly once and replaced once:

- tool, `predecessor == reached` dropped: killed, `FAIL successor from a
  foreign predecessor supersedes nothing: accepted`.
- tool, `performed_rows` replaced by `manifest_rows`: killed (unperformed and
  partial fixtures both fail).
- tool, start frontier emptied: killed (both supersede fixtures fail).
- tool, path key not normalized, recorder `SUCCESSOR_TOOL_SHA` re-pinned to the
  mutant's bytes, recorder selftest: killed, `subject differs from its
  successor row: openspec/changes/example/./proposal.md`.
- recorder, single-first-digest test removed: killed (`two separate chains`).
- recorder, length test removed: killed (`a forked successor chain accepted`).
- recorder, step filter removed: killed (`wanted current subject drift`).
- recorder, composition replaced by last pair: killed (`an unchanged later
  claim did not compose onto the chain`).
- recorder, loop bound removed: selftest did not finish in 150 s, matching
  the recorded timeout.

Every reproduced refusal matched the recorded `refusal` text.

[Observed] The two guards disclosed as equivalent are equivalent:
- Normalizing a later package's path: `proposed()` derives changed subjects
  from `relative_to(...).as_posix()` names and refuses any not in the config
  keys, so an aliased key can only be a kept claim; a kept (x, x) step adds no
  digest beyond one already reached.
- Skipping `rows is None`: without it `rows[path]` raises TypeError inside the
  per-package `try`, which grants nothing; a package with no matching subject
  yields nothing either way.

[Observed] No rule-6 row pins M1-M3, since the fixtures do not exercise them.

## Criterion 4 — rehearsal in `hist14/post`

[Observed] At 249a9d8 I committed a placeholder `HISTORY-REVIEW-14-RAW.md`
binding the recorder digest, a placeholder confirming raw under `docs/reviews/`
carrying `Verdict: CONFIRM` and `Manifest-file SHA-256:` of the package's
`SUCCESSOR-MANIFEST.txt`, and the matching `pins`. Before recording, both
checks passed. `readability_successor.py --package ...dependency-union-successor
--record --phrase "SIGN OFF POLARIS UNDERSTANDING DEPENDENCY UNION SUCCESSOR:
<manifest sha256>"` recorded the act, wrote the dedicated record and aggregate
block and installed `GOVERNING-DEPENDENCIES.md`; I committed that. Then:
- `readability_successor.py --all --check`: 4 PASS, all performed-exact
  (the readability successor stays exact through the chain).
- `record_polaris_understanding_adoption.py --check`: PASS (8 historical
  rows, 7 unchanged).
- `record_polaris_understanding_adoption.py --selftest`: four PASS lines, no FAIL.
- `check_spec_reconciliation.py --check`: R2 FAIL, `GOVERNING-DEPENDENCIES.md no
  longer hashes to its signed row` (polaris-understanding), expected by design.
  R6 WARN (two behaviour-contract pins, report only).

[Observed] Undoing the union act with no act (writing back the bytes from before
it) leaves the recorder green (the file is at its adopted bytes, so no row is
consulted) while the tool fails the union package. See N1.

## Criterion 5 — governance checker

[Observed] At 249a9d8, `check_governance.py`: `31 OK, 21 WARN, 0 FAIL (52
checks)`; `--selftest`: `369 fixtures, 0 failing`.

## Blocking findings

- M1. `chain()` in the recorder accepts a repeated step when a later revisit
  can stand in for it: `chain([(a,b),(a,b),(b,c),(c,b)]) == (a,c)`, contrary to
  its docstring and `HISTORY-READING.md`. On real fixtures every package is
  `performed-exact`, the recorder refuses the true head B and accepts C after a
  no-act edit. Suggested repair: contest unless `len(dict(steps)) ==
  len(steps)` (each digest has at most one outgoing step), and add the case to
  the composition table with a rule-6 row.
- M2. The tool's `later_rows` follows steps of earlier packages as well as
  later ones, so after a restyle-and-revert (A→B, B→C, C→B, or A→B, B→A) a
  no-act edit back to an intermediate digest is `performed-exact` for every
  package. The recorder refuses these states, but `--all --check` is green.
  Suggested repair: accept a later digest only along one unbranched chain of
  other packages that starts at this package's row (the recorder's `chain`
  rule), and test the revert cases.
- M3. `later_rows` includes the package itself. A package naming one file
  twice (`x` changed, `./x` kept) was refused by the 6a013e8 tool and is now
  recorded and `performed-exact`, with a manifest row that is false. That
  turns a pre-change refusal into an acceptance (criterion 2). Suggested
  repair: skip `other.dir == self.dir`, or refuse config keys that collide
  after normalization at load time.

## Notes

- N1. The recorder ignores a later package that fails its tool check
  ("blocks no other"), so when the later act's bytes are undone without an
  act the recorder stays green and only `readability_successor.py --all
  --check` catches it. This predates round 14 and is disclosed in
  `HISTORY-READING.md`; it holds only while the battery runs both checks.
- N2. `chain` legitimately accepts a trail that revisits a digest
  (`[(a,b),(b,c),(c,b)]` gives (a,b)). The "cycle" wording in the docstring and
  `HISTORY-READING.md` means a cycle with no first digest; say so.
- N3. Recording order is not stored anywhere the tool reads except the act
  instant; any ordered repair for M2 would have to rely on it or on chain
  shape alone.
- N4. The rule-6 rows record commit ab2a58b; the reviewed commit 249a9d8 adds
  only the evidence files on top, so the rows remain re-runnable here.
