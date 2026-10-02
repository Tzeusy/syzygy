# History review 15 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 05271067045b2de86e188a8df9e3e25300d82a36
- `scripts/record_polaris_understanding_adoption.py`: `603619a8deddbd0bff036b9c6d0711ac9d1e6a7c60710204183e1220f4d66a86`

Reviewer: fresh-context agent, 2026-10-02. Scratch clones under `xp95/hist15/`: `repo`
(at 0527106), `post` (0527106 plus three scratch commits), `r14` (at 249a9d8) and
`base` (at 6a013e8) for before/after comparison. Probe scripts are in `xp95/hist15/bf/`.
No repository file was edited outside the scratch clones.

[Observed] Recomputed sha256 at 0527106: the recorder as in the head line above;
`scripts/readability_successor.py` is
`f9e24b6563eca5bfc274dc19170ed7488e5f4ab4caa33558fe86cfa480e57df7`, equal to the
recorder's `SUCCESSOR_TOOL_SHA` (line 35). `git diff 2f1e7da 0527106` touches only
`HISTORY-READING.md` and `history-reading-rule6.json`, so the round-15 rows recorded
at 2f1e7da run against the same script bytes as the reviewed commit.

## Criterion 1 — M1 to M3 repaired

[Observed] M1 (repeated step). `chain([(a,b),(a,b),(b,c),(c,b)])` is now CONTESTED;
at 249a9d8 it returned (a, c). `chain([(a,b),(b,c),(c,b),(d,e),(e,d)])` is CONTESTED.
The step back `[(a,b),(b,c),(c,b)]` still gives (a, b), and a longer return
`[(a,b),(b,c),(c,d),(d,b)]` gives (a, b). The new loop stops at the first revisited
digest, and `len(walked) != len(steps)` refuses whenever `dict(steps)` collapsed a
repeat or a fork, because `walked` can hold at most `len(following)` digests.
On real fixtures (`bf/probe15.py`, P3: A->B, a second A->B, B->C, C->B at strictly
increasing instants), the recorder row is CONTESTED both at head B and after a
no-act edit to C. At 249a9d8 the same probe gave (A, C) and the recorder accepted
C.

[Observed] M2 (earlier packages followed). Review 14's probe scripts survive under
`hist14/bf/`. I copied `fixture.py`, `alias.py` and `bf.py` into `hist15/bf/` with
only the repository path changed, and wrote `probe15.py` with explicit act instants,
because the new `later` helper gives every later package the same default instant.
- P1 (A->B, B->C, C->B, then a no-act edit to C): the tool now refuses the C->B
  package (`subject differs from its successor row`), so `--all --check` is red.
- P2 (A->B, B->A, then a no-act edit to B): the B->A package is refused, so the tool
  is red too.
At 249a9d8 every package checked `performed-exact` in both cases.
`bf.py` as copied still models the round-14 unordered `later_rows`, so its counts
do not describe the new code. `bf/model15.py` is the replacement (criterion 2).

[Observed] M3 (own row). With `alias.py` on the new tool, a package naming
`x` (changed) and `./x` (kept) is refused at `--record` with `subject differs
from its successor row: ./openspec/changes/example/proposal.md`. That is the
6a013e8 behaviour. The first step needs an instant strictly after the package's own
instant, so the package can never extend its own chain.

## Criterion 2 — the chain stays fail-closed

[Observed] Instants: `body()` fullmatches
`[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z` and parses it with
`strptime`. `performed_rows` re-renders the act from the parsed instant and refuses
any mismatch, so every instant compared in `later_rows` has this fixed width. Text
order is therefore time order. Because instants strictly increase along a chain, a
cycle of digests cannot loop: the walk terminates, and `seen` bounds it further.

[Observed] Ties and backdating, on real fixtures:
- P4: A->B and B->C both at 2026-09-29T00:00:00Z. The A->B package is refused,
  and the recorder row is (B, C), so the recorder refuses too.
- P5: B->C recorded with `--instant`-style backdating to before A->B. Same result.
Both fail closed: an equal or earlier instant never extends a chain.

[Observed] An exhaustive model of one path. `bf/model15.py` and `model15b.py` use
each commit's real `chain()`; `later_rows` is re-implemented from the source of each
commit, and the 6a013e8 recorder contests any two claims. A state is "bad" when the
current digest is not the head of any order in which the packages could have been
recorded, each starting at its recorded predecessor. "Combined" means
`--all --check` is green and the recorder accepts.
- Digests {a,b,c}, up to 4 packages, instants 1..4 with ties: 3,455,208 non-adopted
  states. Combined-bad: 0 at 0527106, 0 at 6a013e8, 30,720 at 249a9d8 (the first is
  review 14's M1 shape).
- Digests {a,b,c,d}: up to 3 packages with instants 1..3 (338,832 states), and up to
  4 packages with instants 1..2 (3,247,200 states). Combined-bad: 0 at 0527106 in
  both.
- Every state the new pair accepts and the 6a013e8 pair refused is an honest head:
  0 newly accepted bad states, against 23,964 and 2,559 newly accepted good ones.

[Inferred] Why the combined result holds. Take the act with the greatest instant
among the performed packages that name the path. Under `--all` its `later_rows` is
empty, so the current digest must equal its row. A tie at the greatest instant
needs both rows equal. Anything else is drift.

[Observed] Recorder alone, without the tool's `--all`. The recorder drops a package
that fails its tool check (the disclosed "blocks no other" rule), so it can accept a
superseded digest whenever the tool's `--all` is red. In the model, 6,126 bad states
over {a,b,c}, n<=3, are recorder-accepted with the tool red. Most predate the
chain. For example, an honest A->B->C followed by a no-act edit back to B is
accepted by the recorder at 6a013e8, 249a9d8 and 0527106 alike (probe P6). But
1,692 bad states over that population were refused by the 6a013e8 recorder and are
accepted now. The smallest one with no fork, no tie and no kept claim is P1 above:
the recorder row becomes (A, C) and `--check` passes on a hand edit to C. The 6a013e8
recorder refused it (row (B, C)), and so did the 249a9d8 recorder (row (A, B)). C was
installed by a performed act, and the state is a chain case, so it is outside both
blocking definitions in this brief; see N1.

[Observed] Forged instants. Moving a performed act's instant means rewriting its
dedicated record and its acceptance-record block together, because `performed_rows`
compares the two byte for byte. That is a forged act, which `HISTORY-READING.md`
already discloses as trusted working-tree input.

## Criterion 3 — behaviour outside a chain kept

[Observed] At 0527106:
- Tool `--selftest`: `40 fixtures, 0 failing`. The new fixtures are the step back,
  the hand-restored intermediate bytes, and the own-row-twice refusal.
- Recorder `--selftest`: four PASS lines, no FAIL, and `15 composition cases`.
- `readability_successor.py --all --check`: 4 PASS. Three are `performed-exact` and
  the union package is `candidate-unperformed`.
- Recorder `--check` fails only on `latest history review not confirming:
  ...HISTORY-REVIEW-14-RAW.md`, which is expected until this review is retained.

[Observed] For a path that only one package claims, `later_rows` can find no step,
so the package is strict, as it was at 6a013e8. These states are refused at all
three commits: a foreign predecessor, drift (both the tool and `current subject
drift`), unperformed, partial, an own-row alias (M3) and backdating (P5). The
model found 0 states that are bad, accepted by the new pair and refused by the
6a013e8 pair.

## Criterion 4 — rule 6

[Observed] `history-reading-rule6.json` has 111 mutants. 17 are at 2f1e7da (rows
94-110, the round-15 rows) and 15 are at ab2a58b (the round-14 rows, kept). I
reproduced eight round-15 rows in throwaway copies of `repo` (`bf/rule6_15.py`).
Each `old` fragment occurs exactly once and is replaced once.
- 95, tool, predecessor test dropped: killed, `FAIL successor from a foreign
  predecessor supersedes nothing: accepted`.
- 96, tool, later-instant test dropped: killed, `FAIL an earlier act's bytes
  restored by hand refused: accepted` (the own-row fixture also fails).
- 97, tool, strictness `at >= after`: killed, `FAIL an act's own row never
  supersedes its other row: accepted`.
- 101, tool, empty start frontier: killed, with the recorded supersede refusal.
- 102, tool, path key not normalized, with the recorder's `SUCCESSOR_TOOL_SHA`
  re-pinned to the mutant's bytes, recorder selftest: killed, `subject differs
  from its successor row: openspec/changes/example/./proposal.md`.
- 104, recorder, walked-step count dropped: killed, `a forked successor chain
  accepted`.
- 107, recorder, step filter dropped: killed, the recorded wrong-refusal text.
- 110, recorder, walk stop dropped: no result within 150 s, consistent with the
  recorded timeout.
Every reproduced refusal contains the recorded `refusal` text.

[Observed] The two guards the page calls equivalent are equivalent:
- Normalizing a later package's path. `proposed()` names changed subjects from
  normalized relative paths, so an aliased key can only be a kept claim. A kept
  step (x, x) at instant t adds x, which is already reached. Its frontier entry
  (x, t) explores a subset of the steps that the earlier entry for x already
  explores, because that entry has an earlier instant.
- Skipping `found is None`. Without it, `at, rows = None` raises TypeError inside
  the per-package `try`, so the package grants nothing, as before.

[Observed] Row 97 is killed only by the own-row fixture. No fixture ties two distinct
packages at one instant (probe P4 shows that case refused). See N3.

## Criterion 5 — rehearsal in `hist15/post`

[Observed] At 0527106, on a scratch branch, I made three scratch commits:
1. A placeholder `HISTORY-REVIEW-15-RAW.md` binding the recorder digest. Recorder
   `--check` then passed (8 historical rows, 7 unchanged).
2. A placeholder confirming raw under `docs/reviews/`, carrying `Verdict: CONFIRM`
   and the `Manifest-file SHA-256:` of the package's `SUCCESSOR-MANIFEST.txt`,
   with `pins` set in `SUCCESSOR.json`. `--all --check` and the recorder `--check`
   both passed.
3. The act, performed with the `--record` command and phrase given in the brief.
   It wrote the dedicated record and the aggregate block and installed
   `GOVERNING-DEPENDENCIES.md`.

[Observed] Results after step 3:
- `readability_successor.py --all --check`: 4 PASS, all `performed-exact`. The
  readability successor stays exact through the union's later step.
- `record_polaris_understanding_adoption.py --check`: PASS.
- `record_polaris_understanding_adoption.py --selftest`: four PASS lines, no FAIL.
- `check_spec_reconciliation.py --check`: R2 FAIL, `GOVERNING-DEPENDENCIES.md no
  longer hashes to its signed row` (polaris-understanding). This is expected by
  design. R6 WARN, report only. The other five predicates are OK.

[Observed] Two further probes, both reverted afterwards:
- Writing back the pre-act bytes: the tool fails the union package; the recorder
  passes, because the file is at its adopted bytes (review 14's N1).
- Appending a foreign line: the tool fails both packages that list the file; the
  recorder fails with `current subject drift`.

## Criterion 6 — governance checker

[Observed] At 0527106, in a clean clone:
- `check_governance.py`: `31 OK, 21 WARN, 0 FAIL (52 checks)`.
- `--selftest`: `369 fixtures, 0 failing`.

## Blocking findings

None. I found no digest accepted without a performed act, by the tool, by the
recorder or by both together. No state outside a chain that was refused before
is accepted now.

## Notes

- N1. The M2 repair moved a false green from the tool to the recorder.
  - The case: A->B, B->C, C->B at increasing instants, then a no-act edit to C
    (probe P1). The tool now refuses the C->B package, and the recorder drops
    that package. It then composes (A, C) from the other two and its `--check`
    passes.
  - Both earlier recorders refused this tree: 6a013e8 with row (B, C), 249a9d8
    with row (A, B). Over {a,b,c} with n<=3 there are 1,692 such recorder-only
    regressions against 6a013e8.
  - The battery stays fail-closed only because it also runs
    `readability_successor.py --all --check`.
  - `HISTORY-READING.md` answers review 14's N1 with "predates the chain". That is
    true of the honest-chain undo (P6), but not of this instance.
  - Suggested repair, whenever the tool next changes: in `successor_rows`, mark a
    package's normalized paths CONTESTED when its `performed_rows` verifies but
    its `check()` fails. A malformed or unperformed sibling would still block
    nothing. Until then, correct the page's sentence.
- N2. Two honest acts recorded in the same second refuse the earlier package
  (probe P4). This fails closed. It cannot happen through the default `now()`
  unless two acts land within one second, but the remedy is not written down.
- N3. Row 97 (`at >= after`) is killed only by the own-row fixture. A two-package
  tie fixture would pin strictness for distinct packages as well.
- N4. `bf.py` from round 14 hard-codes the unordered `later_rows`, and the default
  `later(...)` instant is the same for every package. A reviewer who reuses either
  without explicit instants measures ties, not chains.
- N5. The model has limits. It covers one path. The recorder's acceptance is
  reduced to `chain(passing) == (adopted, current)` or `current == adopted`.
  `later_rows` is a re-implementation, not an import. Six real-fixture probes
  (P1-P6) matched the model's verdicts at all three commits.
