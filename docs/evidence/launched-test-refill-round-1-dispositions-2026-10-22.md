# Launched-marker test refill: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.8.14`
(pull request #506), the test-only change to
`packages/polaris-dossier/src/launched.test.ts` that answers notes R3-N1 and
R3-N2 of `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-3-RAW.md`.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-LAUNCHED-TEST-REFILL-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `9f09e5ca` | `r1-review.diff` sha256 `200b17206ebe87b10e639bdf22d61ea04fa50dffcdfb674fffaf2964ad485cea` |

The subject equals `git diff 1d6731bb 9f09e5ca`. It is also
`git diff 5837512f af895800`, the diff between main and this pull request's
merge of that main.

The reviewer found "No finding is blocking" and three notes (section 4).
Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## N1: the reader's own file no longer kills a reader that alters an unreadable run

[Observed by the reviewer] Planting a fresh run for all 17 rows of
`PRESENT_BUT_NOT_THE_MARKER`, not only the FIFO row, removes one job the
shared run did. Mutant D1, in which `launchFormRefusal` removes the marker when
it reads `unreadable`, is killed by the base file with 16 failures. It
survives the head file, 43 of 43. Three other files still kill it:
`inventory.test.ts:455`, `review.test.ts:480` and `render.test.ts:705`.

**Disposition:** filed as `syzygy-bpyt.8.18` (P2, test-only). After each ask,
the launch-form row asserts that the run still reads `unreadable`. The
reviewer checked this in scratch: it kills D1, D2, F2 and the `bang` drain
mutant.

## N2: what acceptance criterion 1 rests on

**Correction.** AC1 names a mutant, F1 (the `isFile` check removed from the
syzygy-launched path only). F1 is killed, as the criterion requires, but it is
killed by the base tests too, so it does not show the refill. AC1 is met on
three other pieces of evidence:
- F2 in `docs/evidence/launched-marker-test-refill-mutants-2026-10-22.json`,
  for `syzygy-launched`;
- the reviewer's `M-all-forms-drain-bang-unchecked`, for `bang` (fragments in
  the raw's Appendix A): the base tests let it survive, and the head tests kill
  it;
- the reviewer's byte probe, for all three forms: 231 / 231 / 231 bytes left
  in the pipe at each form's call in the head layout, against 231 / 0 / 0 in
  the base layout.

`terminal` is trivially first. The mutants record is not edited.
`syzygy-bpyt.8.18` adds the `bang` drain mutant to its own rule-6 record.

## N3: risk class

**Disposition:** the reviewer ruled the change CC-REV-1 **class 4**. The
changed rows are the kill evidence for the SEC-3 fail-closed reader, and N1
shows that a change to them can weaken it. The coordinator accepts the ruling.
GP-Q0's three extra checks:
- The differential is degenerate. No production byte changed (raw section 5:
  `launched.ts` hashes the same at base and head), so every reader's output
  is unchanged over any corpus.
- A rule-6 mutant for each predicate is met by the record and the reviewer's
  section 3 item 7.
- The owner notice is posted on `syzygy-bpyt.10` at landing.
