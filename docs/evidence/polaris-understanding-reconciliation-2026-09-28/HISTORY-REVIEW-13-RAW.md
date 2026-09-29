# History review 13 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 647eb6a3a10f06cdcb2c0875015b603ec79748f5
- `scripts/record_polaris_understanding_adoption.py`: `fce09524b68f202748c267b2fdcb8315b8267a9d3867cea2530f17d0d315d963`

Reviewer: fresh-context agent, 2026-09-29. Scratch clones: `hist13/repo` (at
647eb6a) and `hist13/post` (647eb6a plus a scratch commit performing the
understanding readability successor, plus a later scratch stub commit).
No repository file was edited.

## Subject

The only script change since round 12 (4f9df57) is the reconciliation
selftest fixture (`git diff 4f9df57 647eb6a -- scripts/`: 11 insertions,
8 deletions, all inside `reconciliation_selftest`, hunks at 688 and 779-817).
[Observed] The sha256 of the recorder at 647eb6a is the value in the head, computed with
sha256sum. It matches the value the brief gave.

## Criterion 1: the fixture change weakens no selftest

- [Observed] Pre-adoption (647eb6a) the selftest reports "57 trust-boundary
  mutations refused". The RULE6-WITNESSES list has the same 57
  (path, operation, refusal) triples, in the same order, as the 4f9df57
  recorder's selftest run over the same tree. Byte-for-byte equality over
  the triples.
- [Observed] Post-adoption (`hist13/post`) the selftest again passes. It
  gives 57 witnesses, and their triples are identical to the pre-adoption
  run's. So the installed successor rows (8 rows, 6 identity rows and a
  restyle row each for `proposal.md` and `design.md`) change no refusal
  reason.
- [Observed] The drift guard (recorder:447-452) only accepts
  `row == (digest(adopted), digest(current))`. Any mutation of a subject's
  current bytes therefore breaks the exact row equality, including a subject
  that has an installed row. This held post-adoption for
  `mutate(SPEC, 'current subject drift')` and `mutate(CHANGE + 'tasks.md', …)`,
  where both paths carry identity rows. Non-subject evidence is never
  checked against successor rows, so no row can mask a mutation there.
- [Observed] The proposal successor cases (recorder:782-817) now overlay
  `installed` and override only the `proposal.md` key. They build the restyle
  from `fixture.blob(ADOPTION, proposal)`. They restore `files[proposal] = today`
  and `successors = installed`, so the later mutations run against the
  same baseline as before.

## Criterion 2: post-adoption

- [Observed] I ran `readability_successor.py --record --phrase "SIGN OFF
  POLARIS UNDERSTANDING READABILITY SUCCESSOR: 2bd0892a…3b98"`, using the
  label from SUCCESSOR.json and the sha256 of SUCCESSOR-MANIFEST.txt as
  computed. It installed `proposal.md` and `design.md`, wrote the act, and
  appended the aggregate block. I committed the result.
- [Observed] After that commit, `--selftest` exits 0 with all four PASS
  lines.
- [Observed] Post-adoption, `--check` fails only on "latest history review
  does not bind the current recorder: …HISTORY-REVIEW-12-RAW.md".
- [Observed] With a stub `HISTORY-REVIEW-13-RAW.md` committed (CONFIRM,
  binding fce09524…), `--check` PASSes: "8 historical rows, 7 unchanged,
  REQ-004 adoption/current bytes; 31 requirements/182 scenarios".
- [Observed] Control: the 4f9df57 recorder's selftest in the same
  post-adoption tree fails with "current subject drift: …/design.md". This
  confirms the defect that the Round 13 bullet describes.

## Criterion 3: `--check` at 647eb6a

- [Observed] `--check` prints exactly one line: "FAIL exact digest
  reconciliation unresolved: latest history review does not bind the current
  recorder: docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-12-RAW.md".
  It is the only failure.

## Criterion 4: rule-6 rows

- [Observed] `git diff -U0 5f7edaf 647eb6a -- scripts/` touches only the seven
  fixture hunks.
- [Observed] Of the 79 rows in `history-reading-rule6.json`, every `old`
  fragment has the same occurrence count at 4f9df57 and 647eb6a. The fixture
  diff touches no guarded line.
- [Observed] Sixteen rows (d50197f ×4, 4ff4ab7 ×5, 90f12ae ×5, 1d5b534 ×2)
  have fragment count 0 at both commits. Those lines were superseded before
  round 12, so this change did not cause it.
- [Observed] I replayed all 14 rows at 5f7edaf at 647eb6a (pre-adoption). All
  14 exit 1 and print their recorded refusal. Row 74's recorded refusal carries a
  `<tmpdir>` placeholder, which I matched as a wildcard.

## Criterion 5: governance

- [Observed] At 647eb6a, `check_governance.py` gives "31 OK, 21 WARN, 0 FAIL
  (52 checks)". `--selftest` gives "347 fixtures, 0 failing".

## Blocking findings

None.

## Notes

- N1 [Observed] After the successor is performed, one rule-6 row at 5f7edaf
  (row 68 of 79, 1-based: `if current != adopted:` → `if True:`,
  recorder:447) survives. The selftest exits 0. The performed package grants
  a row for all eight subjects, identity rows included. So the fixture's
  baseline, which now starts from `installed`, no longer contains any subject
  where current == adopted and no row exists. That was the only case that
  killed this mutant. The mutant is fail-closed (it refuses more, never
  less), so it cannot hide a defect. But the rule-6 row stops being
  reproducible once the successor is performed.
  - [Inferred] One fixture case with `successors = {}` and every subject at
    its adopted bytes would keep the row killed in both states.
- N2 [Observed] Post-adoption, four more 5f7edaf rows are still killed, but
  with a refusal other than the recorded one:
  - Row 66 (`row is None or row[1] == …`) is now killed by "successor from a
    foreign predecessor accepted". Its recorded refusal was "mutation
    accepted: …spec.md", but the identity row on spec.md now refuses the
    spec mutation.
  - Rows 73, 77 and 79 are now killed at the fixture's base state, by
    "current subject drift: …/design.md". The real rows feed the fixture.

  Every one exits 1, so no mutant escapes. Rule-6 refusals recorded at
  5f7edaf describe the pre-adoption corpus only. A future replay after
  adoption should expect these texts.
- N3 [Observed] HISTORY-READING.md:189-195 (Round 13) is accurate against what
  I ran. The old fixture set `self.successors = {}`. The new fixture uses
  `dict(source.successor_rows())` and `blob(ADOPTION, …)`. The selftest passes
  both before and after the successor is performed, and `--check` fails until a
  confirming raw is retained.
