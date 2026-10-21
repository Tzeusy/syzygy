# POC core hygiene: review dispositions, rounds 1 and 2

[Observed] This record dispositions the two CC-REV-1 reviews of
`syzygy-bpyt.7.6` (pull request #503). The change deletes dead
`three-surface-poc-core` exports, marks the deliberate test seams, and keeps
three of the audit's four orphan candidates on recorded consumer evidence.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-POC-CORE-HYGIENE-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `e81883f3` | `r1-review.diff` sha256 `1f3fd9bb472af2a3b62fbf3e2899b3e7c902f2db9ce99ddc1f8bb919efffba86` |
| 2 | `docs/reviews/R-GP-IMPL-POC-CORE-HYGIENE-2-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `edca4490` | `r2-review.diff` sha256 `be299245e2fcaeb6b1858f75702a462b6a8983c7a36a3abdbaddfa0d29108c10` |

Round 1's subject equals `git diff b7697f6a e81883f3`. Round 2's subject
equals `git diff 1d6731bb edca4490`, and it is also
`git diff f3641c85 30fe5169`: the diff between main and this pull request's
merge of that main.

Round 1 cleared `e81883f3` under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1). The lane then repaired its notes, which changed the bytes that
would merge. Round 2 was therefore run over the repaired head (AGENTS.md
rule 10). It found "No blocking findings (F) in this round. Four notes"
(section 5), and so clears the bytes it read. Those bytes are not edited.
This record sits beside them, and it is an implementation record that binds
nothing.

Both rounds ruled the CC-REV-1 class **none**. Round 2 re-ruled it after the
repair, which restored the P1 gate `body-read-authority.ts` to its base bytes.
GP-Q0's extra checks for classes 1, 3 and 4 therefore do not apply. No owner
notice is required.

Revise-severity findings open after round 2: 0

## Round 1 notes, as judged by round 2 (section 4)

| Note | Round 2 status |
|---|---|
| N1: the head moved past the reviewed commit | Repaired; round 2 binds `edca4490` |
| N2: overstated comments | Repaired, with one new imprecision (round-2 N11) |
| N3: census selftest gaps and undisclosed lexer limits | Partly repaired; the remainder is round-2 N9 |
| N4: record identity and re-runnability | Repaired |
| N5: AC1 met by disposition | Repaired by disclosure in the PR body; recorded below |
| N6: AC2's selection predicate | Repaired |
| N7: mutation records for the gate and the evaluator | Repaired; the gate is byte-identical to base |

## Acceptance criteria at close

- **AC1** ("each orphan's consumer sweep recorded … and each removed or
  relocated") is met in substance, and its literal wording is met by
  disposition (round-1 N5). The sweeps are recorded by two agreeing methods
  over 3039 tracked files at both trees. One orphan is deleted. Two are kept
  because recorded consumers falsify the orphan premise: `evidence-population.ts`
  and `owner-act-drafter.ts`. One is kept as test support: `test-cleanup.ts`.
- **AC2** (the six test-only exports enumerated and resolved) is met, with
  round-2 N10. Five are resolved by a "Test seam" comment. The sixth,
  `appendEvaluation`, is resolved by the recorded disposition in
  `docs/evidence/poc-core-hygiene-2026-10-22/dispositions-2026-10-22.json`
  rather than by a comment, so that the gate's bytes stay unchanged.
- **AC3** is met. Round 2 re-ran the evidence at `edca4490`:
  - suite: 4982 passed, 5 skipped;
  - `Tests: +0 ~0 -0`;
  - fixture route responses: 230 of 230 identical, and 5 of 5 fixtures distinct.

## Round 2 notes

### N8: the comment-only check's whitespace blind spot

[Observed by the reviewer] `comment_only_check.py` drops blank lines and
trailing spaces everywhere, so it cannot see a whitespace edit inside a
template literal. Its "6 of 6 mutants" includes one negative control. It does
not affect this pull request: the reviewer's own TypeScript-printer comparison
agrees over the whole delta.

**Disposition:** carried in `syzygy-bpyt.7.12` as a repair to make before the
tool is reused.

### N9: two census-lexer template predicates are unpinned

[Observed by the reviewer] Two lexer template mutants survive the 28-case
selftest:
- nested-template entry;
- re-entering template mode after `}`.

The docstring says the limits only under-count. They can over-count too. No
figure in this pull request is affected, because the lexer and the TypeScript
printer agree on 495 of 495 files at base and 496 of 496 at head.

**Disposition:** carried in `syzygy-bpyt.7.12`, the follow-up un-export sweep
of the 233 exports used only in their own file, which will reuse the census.

### N10: AC2's sixth subject

**Disposition:** recorded under "Acceptance criteria at close" above.

### N11: the M1 citation range

[Observed by the reviewer] Three artifacts cite three different ranges of
`docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`:
- the comment in `evidence-population.ts` gives `:382-383`;
- the lane's dispositions give `:380-384`;
- the PR body gives `:380-386`.

The passage the claim rests on is `:380-386`.

**Disposition:** the reviewed bytes are not edited. The next edit to either
file for another reason cites `:380-386` in both.

## Other follow-ups from the lane's report

- `syzygy-bpyt.7.13`: two near-duplicate fixture-directory cleanup helpers,
  `removeFixtureDirectory` in the core package and `removeTemporaryDirectory`
  in the app.
