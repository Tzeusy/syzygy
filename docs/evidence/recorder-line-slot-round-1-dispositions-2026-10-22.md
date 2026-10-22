# Recorder line slot: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.8.17`
(pull request #508). That change replaces the recorder template's `SLOT.line`
pattern in `packages/polaris-generation-consent/src/recorder-template.ts`:
`[^\r\n]*\S[^\r\n]*` becomes `[^\S\r\n]*\S[^\r\n]*`, so a line slot is read
one way. The evidence it carries is `docs/evidence/recorder-line-slot-2026-10-22.md`
and its three JSON records.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-RECORDER-LINE-SLOT-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `18f9557f` | `r1-review.diff` sha256 `a7901624d36912a8b6486dbd39740b8fec024d7255ea680837e64076e59e1b05` |

The subject equals `git diff 5837512f 18f9557f`. Main then moved to
`c55acb73`, and the branch merged it. After that merge,
`git diff origin/main HEAD | sha256sum` prints the same digest, so the merge
brought only main's bytes.

The reviewer found "No blocking findings (F-series): none." (section 4), with
four notes. Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## N1: the label/description row is still quadratic

[Observed by the reviewer, raw section 3.3] A single line slot is now linear.
The row `| "{label}" | "{description}" |` is not. It holds two line slots and
appears in 7 of the 8 exported templates; the sign-off is the exception. In
the reviewed tree, a record whose label holds `" | "` many times and which
fails at its last byte refuses in:
- 252.7 ms at 14 KB (provider v2);
- 396.0 ms at 13.6 KB (D9);
- 16.1 s and 17.4 s at about 104 KB.

The old pattern is far slower on the same shapes, so the change is still a
strict improvement. No verdict or captured value differs.

The report, `docs/evidence/recorder-line-slot-2026-10-22.md:77-79`, says:
"The new pattern has one way to match a given end, so each slot tries each end
once and the literal after it rejects all but the few where that literal
appears; nothing multiplies across slots." **That sentence is wrong for the
label/description row.** There the literal after the label (`" | "`) can
appear many times on one line, and for each place the label may end, the
description scans to the end of the line. The report is bound to the reviewed
bytes and is not edited; this record carries the correction.

The pull request title says "a failing record refuses in milliseconds". That
holds for the 8.10 corpus and the real provider v2 record (AC1), not for a
crafted label row. The merge commit carries the narrower title.

**Disposition:** filed as `syzygy-bpyt.8.21` (P2, class 4): make that row's
read linear with no change to the language or the captures, pinned by a
timing-bounded test on a real exported template. A size bound on act records
would change verdicts, so it is out of scope and would go to the owner. The
owner notice says the stall is closed for the recorded corpus and reduced, not
closed, for a crafted label row.

## N2: the differential cannot see a capture change

[Observed by the reviewer, raw section 3.6] Three plausible slot mutants each
give "0 mismatches" over the lane's 1,651 template inputs: a lazy tail, a
dropped leading run, and a blank slot accepted. Only a bounded-tail mutant
gives 15 mismatches. The corpus holds no label containing `" | "`, no slot
starting with a blank, and no blank slot. The record carries no
negative-control run.

**Disposition:** corrected here. The evidence that captured values are
unchanged is:
- the structural argument (raw section 3.1, which the reviewer re-derived);
- the five property tests, which kill the lazy-tail, leading-run and blank
  mutants;
- the reviewer's own check (raw section 3.2(c): 16,000 template records, 0
  differences, with two negative controls that each report differences).

The differential's role is narrower: no recorded act and no altered-prose
record changes verdict. AC2 is met in that sense. `syzygy-bpyt.8.21` reuses
the differential, so its acceptance adds the three corpus shapes above and one
recorded negative-control run that must report mismatches.

## N3: the #500 timing tool now times the new slot against itself

[Observed by the reviewer] `scripts/measure_slot_line_backtracking.mjs` takes
`SLOT` from the built consent package (`:33`), so on any tree carrying this
change it times `[^\S\r\n]*\S[^\r\n]*` against itself. Its timing record
carries the script's digest, so the script is not edited.

**Disposition:** corrected here.
`docs/evidence/consent-gate-slot-line-timing-2026-10-21.json` reproduces
only at a commit before `40d5de76`, the first commit carrying the new pattern.
Re-run it at `3000698f`, for example. A re-run on main that reads 0 ms for
both patterns is expected, not a contradiction of #500's record.

## N4: one load figure has no record

[Observed by the reviewer] The report says, at
`docs/evidence/recorder-line-slot-2026-10-22.md:85-87`: "Forty-nine `uptime`
samples, taken once a minute while the differential ran and not retained,
ranged from 18.6 to 54.2." No retained file carries those figures.

**Disposition:** corrected here. That sentence is not evidence. The retained
load figures are the timing record's own samples,
`docs/evidence/recorder-line-slot-timing-2026-10-22.json`, which range from
19.8 to 36.54.

## Risk class

Class 4 (SEC-2 consent recognition); the reviewer did not reclassify. GP-Q0's
checks:
- the differential: met, 0 of 14,288 answers changed over every decisions
  record and the altered-prose corpus; the reviewer's sampled re-run gave 0
  of 13,240 (N2 states what it can and cannot show);
- a rule-6 mutant per predicate: met, 8 of 8 as expected, re-run by the
  reviewer (raw section 3.5);
- the owner notice: posted at landing, carrying N1.
