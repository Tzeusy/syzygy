# Launch-form post-condition: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.8.18`
(pull request #511). In `packages/polaris-dossier/src/launched.test.ts`, each
of the three launch-form asks in the unreadable-marker row (`terminal`, `bang`
and `syzygy-launched`) now asserts afterwards that its run still reads
`unreadable`. The change also adds the rule-6 record
`docs/evidence/launched-marker-test-postcondition-mutants-2026-10-22.json`.
No production file changes.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-LAUNCH-FORM-POSTCONDITION-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `35094bcf` | `r1-review.diff` sha256 `32fdb9a8c05c5d3a3129f5eba3ba0f22600ef7523c685edd4d3bb6c54657545a` |

The subject equals `git diff 68c553b8 35094bcf`. Main then moved to
`4b31531c` (#510), and the branch merged it at landing. After that merge,
`git diff origin/main HEAD | sha256sum` printed the same digest, so the merge
brought only main's bytes.

The reviewer found "No finding is blocking." (section 4), with three notes.
Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## Retained review evidence

The reviewer's tools and results are retained under
`docs/evidence/launch-form-postcondition-review-2026-10-22/`. Each file's
sha256 equals the one the raw gives for it (section 3, items 6 to 8):
- `tools/recorded-mutants.py`, the record's embedded harness written out byte
  for byte, and `tools/compare.py`;
- `recorded-rerun.json`, the re-run of the record at `35094bcf`;
- `tools/rev511.py` and `rev511-results.json`, the reviewer's seven
  `launched.ts` mutants against `launched.test.ts` alone, at base and at head;
- `tools/rev511b.py` and `rev511b-results.json`, two more mutants against the
  head file;
- `tools/rev511c.py` and `rev511c-results.json`, the memoized-reader mutant
  against the whole dossier project.

The mutant fragments are in the raw's Appendix A. Not retained: the run logs
and the two `check_governance` transcripts. The raw quotes their result lines.

## N1: the comment promises more than the assertion checks

[Observed by the reviewer] `launched.test.ts:120` says each ask "must leave its
run as it found it". The assertion at `:124` checks only that the run still
reads `unreadable`, through `launchedMarkerState`, the module under test.
Three reviewer mutants that alter the run survive the file:
- D4-truncate and M-every-form-drains-then-refuses leave the run `unreadable`.
  They are not fail-open.
- D1-with-memoized-reader removes the marker and asks a reader that remembers
  its first answer. The run is `absent` on disk, which is fail-open across
  processes. Only `inventory.test.ts`, `review.test.ts`, `render.test.ts` and
  `session-view.test.ts` kill it.

The wording came from the PR #506 raw's proposal, not from the lane.

**Disposition:** filed as `syzygy-bpyt.8.24` (P3, test-only). The coordinator
chose the raw's option (b): snapshot the marker's `lstat` (and its bytes,
where the plant is a readable regular file) before each ask, and assert the
snapshot unchanged afterwards. The FIFO rows keep the state assertion alone,
because reading their bytes would drain them. The reason for (b) over (a), the
comment-only fix, is that an oracle independent of the code under test
(test-rigor bar 4) closes the memoized-reader case in the reader's own file,
instead of leaving it to other files.

## N2: which evidence meets GP-Q0's per-predicate check

[Observed by the reviewer] The change adds three predicates, one post-condition
per ask. In the lane's record, every D1 and D2 failure is the `terminal` ask's
post-condition, because Vitest stops a test at its first failed `expect`. The
record also fails 16 of the 17 rows, not 17. Under Node v24.6.0,
`fs.rmSync(link, { recursive: true, force: true })` leaves a dangling symbolic
link in place, so the record's D1 and D2 never alter the `a dangling symbolic
link` row. That is a property of the mutant's removal call, not of the test.

**Disposition:** GP-Q0's "a rule-6 mutant for each predicate" is met by two
sources together:
- the lane's record, for the `terminal` post-condition and for D2, F2 and the
  `bang` drain mutant;
- the raw's section 3, item 7 (`rev511-results.json`), for the `bang` and
  `syzygy-launched` post-conditions and for the dangling-link row.
  D1-terminal-only, D1-bang-only and D1-syzygy-launched-only each survive at
  base and are killed at head on 17 rows, at `:124` from `:128`, `:129` and
  `:130`. D1-any-remover, which adds an unlink fallback, is killed on all 17
  rows.

The lane's record is not edited (rule 10). `syzygy-bpyt.8.24` carries the
unlink fallback and the three per-form D1 variants into its own rule-6 record.

## N3: class and owner notice

[Observed by the reviewer] The reviewer rules the change class 4, as the #506
reviewer did: the changed rows are the reader's own rule-6 kill evidence for
SEC-3's fail-closed launched-marker reader. GP-Q0's differential is
degenerate. A blob comparison over all 3,188 paths finds only the test and the
record changed, so every reader's output is identical by construction. The
analogue for a test-only change, old test against new test over a mutant
corpus, is the record and the raw's section 3, items 7 and 8.

**Disposition:** the owner notice for #511 is posted on `syzygy-bpyt.10` at
landing.

## Out of scope, observed in passing

The reviewer saw each full dossier-project run leave one
`dossier-signoff-<random>-outside-RAW.md` file in its `TMPDIR`, written by
`waiting-sessions.test.ts:276`. That is `syzygy-bpyt.4.12`, which lane A is
working on now.

## Acceptance criteria (raw section 6)

- AC1 met: each of the three asks asserts `unreadable` afterwards, each
  post-condition is load-bearing on its own, and `Tests: +0 ~17 -0` with the
  43 names unchanged.
- AC2 met: the record's D1, D2, F2 and `bang` drain mutant are each killed by
  `launched.test.ts` alone at the fix, with old/new fragments and the commit.
  The reviewer's re-run reproduces 12 of 12 entries.
- AC3 met: the dossier project's re-run gave `Tests  1195 passed | 1 skipped
  (1196)`. The first run's two timeouts were in `start-gates.test.ts`, which
  passes 104/104 alone.
- AC4: the review is this round. The owner notice is posted at landing (N3).
