# Decisions sweep: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of
`syzygy-bpyt.8.20` with `syzygy-bpyt.8.22`, both carried by pull request #512.
- **8.20.** In `packages/polaris-generation-consent/src/package-reader.ts`,
  `findActRecords` builds one per-file memo of the swept text's spellings
  (`textForms`). Each spelling is computed on its first use, inside one call,
  with no module state. `statementsFor` and `readDigestBoundActState` no
  longer fold each decisions file up to 19 times per sweep.
- **8.22.** The admission family's text needles drop `ADMISSION_PATHS`. Its
  field needles are unchanged.

The change adds `decisions-sweep.test.ts` (19 tests) and the scripts and
records under `docs/evidence/` that `decisions-sweep-memo-2026-10-22.md`
reports.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-DECISIONS-SWEEP-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `c6875163` | `r1-review.diff` sha256 `4456fd9a451e8b549978844e8fcc92ecce1c54a3c555377a4f021b51de8492c7` |

The subject equals `git diff 4b31531c c6875163`. The pull request head then
moved to `b5513ac0`, an unreviewed memo edit (N3), which was reverted by
`074d199e` before landing. `git diff c6875163 074d199e` is empty. Main had
moved on to `d410a34c` (#511 and #513), and the branch merged it at landing as
`d22f630a`. After that merge, `git diff origin/main HEAD | sha256sum` printed the
subject's digest, so the merge brought only main's bytes.

The reviewer found "No blocking finding (no F). Six notes." (section 4).
Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## Retained review evidence

The reviewer's tools and results are kept under
`docs/evidence/decisions-sweep-review-2026-10-22/`:
- `tools/containment_822.mjs` and `results-containment-822.txt`: 8.22's
  containment proof, run against the built `dist/package-reader.js`
  (section 3, item 2).
- `tools/mutant_fragments.py`, `tools/make_review_spec.py`, `review-spec.json`
  and `results-rule6-review.json`: the rule-6 reproduction (M0, M2, M2b, M4,
  M5, M22a, and the reviewer's R2, R0 and R5) at a 120,000 ms test timeout
  (section 3, item 5).
- `tools/compare_rows.py` and `results-diff-sample.json`: the 655-world
  differential sample, matched against the record row for row (section 3,
  item 6).
- `tools/apply_mutant.py`, `results-control-m2.json` and
  `results-control-m2b.json`: the M2 negative control, reproduced exactly, and
  the reviewer's own M2b control: 20 mismatches, 19 of them more lenient
  (section 3, item 9).
- `results-timing.json`: the timing reproduction at load1 34.11–37.48
  (section 3, item 10).
- `tools/zz-review-cost.test.ts`: the reviewer's draft non-loose cost test
  (N2). It sits outside every Vitest project's `include` and is not run.

The run logs are not kept; the raw quotes their result lines. The M22a
control re-run the reviewer stopped at 250 of 1,541 worlds wrote no record,
and nothing from it is counted (section 3, item 11).

## N1: classes 1 and 4, not 4 alone

[Observed by the reviewer] The changed sweep also serves
`readVersionedSignoffState`. `gate-sources.ts` reads that for `registryEntry`,
which decides whether the source-acquisition adapter is authorized: CC-REV-1
class 1, "adapter authorization (VIS-5, VIS-6)". This is the same ruling as
N1 of the PR #505 review. Class 4 still holds for SEC-2 consent and egress.

**Disposition:** the classes are 1 and 4. The declared "class 4" is
superseded, and neither the memo nor the pull request text is edited. GP-Q0
sets the same three extras for both classes, and the review finds all three
present. The owner notice for #512 on `syzygy-bpyt.10` names both classes.

## N2: M5 is a surviving cost mutant, not an equivalent one

[Observed by the reviewer] M5 computes the slack spelling eagerly. It changes
no answer (0 of 489 tests fail at 120 s), but it breaks the memo's "computed on
its first use" promise and adds a whole-text fold per file to every non-loose
sweep. On the admission sweep over the cost test's six files that is 12 folds
against 18 (+50 %), and 60 on the old tree. The committed cost test reads only
a loose sweep, so it allows M5. The reviewer's draft kills M5 and passes on the
subject.

**Disposition:** M5 is recorded as **survived: cost-only, accepted by the
lead's ruling**, not as equivalent. The ruling of 2026-10-21 chose not to build
that test. The memo's "equivalent" wording for M5 is superseded by this
record, and the memo is not edited. Filed as `syzygy-bpyt.8.28` (P3,
test-only): a fold-count bound on one non-loose sweep, plus a per-file bound on
the existing loose cost test. M22b stays equivalent: the reviewer finds it
"genuinely equivalent", since 8.22 is behaviour-neutral by proof and is not a
cost change (section 6, 8.22 AC3).

## N3: the head moved past the reviewed commit

[Observed by the reviewer] `b5513ac0` edited
`docs/evidence/decisions-sweep-memo-2026-10-22.md` after the review froze
`c6875163`. That edit named `syzygy-bpyt.4.13` for the load timeouts and
restated M5 as equivalent.

**Disposition:** reverted by `074d199e`, so the landed memo is the reviewed
bytes. The timing figures `b5513ac0` added are carried to `syzygy-bpyt.4.13`
as a bead comment of 2026-10-22. Its M5 wording is superseded by N2 above.

## N4: AC1's absolute bound holds only under its load condition

[Observed by the reviewer] The lead set the bound before measurement: every
new sample at most 5 s at load1 ≤ 30, and a median paired ratio of at most
0.4.
- The record of reference holds it at load1 25.27–27.39: new samples at most
  3,048 ms, median ratio 0.253.
- The retained high-load run (35.68–50.36) does not.
- The reviewer's reproduction (34.11–37.48) has two of four new samples over
  5 s, with a median ratio of 0.305.

The median ratio held in all three runs: 0.253, 0.207 and 0.305. These calls
run with no timeout, so a slow sample costs latency, never a refusal or a
grant.

**Disposition:** AC1 is met as written, under its condition. The owner notice
leads with the ratio (about 0.2–0.3 in every run), gives the absolute figure
with its load condition, and cites both timing records.

## N5: the void mutant record does not say it is void

[Observed by the reviewer]
`docs/evidence/decisions-sweep-mutants-void-high-load-2026-10-22.json` has no
void or control field, and it records M5, M22b and M22c as `killed`. Only its
filename and the memo say the run is void.

**Disposition:** the generated record is not edited. It is **void**: the run
had no unmutated control, every mutant it scores `killed` was killed by a
timeout the unmutated suite also hit, and none of its outcomes counts. The
memo and this record are the indexes that list it, and both say so. The
runner fix, an identity control first and a stop when it fails, is
`syzygy-bpyt.11.1`.

## N6: the memo's `gate-sources.ts` import sentence

[Observed by the reviewer] The memo says `gate-sources.ts` "imports only the
consent package and a type". It also imports `node:fs/promises` and
`node:path`. The digest claim the sentence supports is exact.

**Disposition:** wording only. The memo is not edited. The accurate statement
is: only the consent package, Node built-ins and a type.

## M22c and the lane's follow-ups

[Observed by the reviewer] M22c, which drops the admission paths from the
field needles too, is "genuinely equivalent by the same containment on field
values". It is outside 8.22's scope, because 8.22's AC1 keeps the field
needles unchanged (section 6, 8.22 AC3). That ruling unblocks
`syzygy-bpyt.8.25`, the optional field-needle simplification, which keeps its
own differential.

The lane's discovered follow-ups were already filed:
- `syzygy-bpyt.11.1`: the rule-6 runner's identity control;
- `syzygy-bpyt.8.25`: M22c;
- `syzygy-bpyt.8.26`: the records port in the probe and real-file worlds.

## Acceptance criteria (raw section 6)

`syzygy-bpyt.8.20`:
- AC1 met under its stated condition (N4).
- AC2 met: 0 of 36,515 answers differ over 4,643 worlds, with the PR #500
  altered-prose corpus, 1,648 answer vectors and 256 label vectors. The
  reviewer reproduced the corpus digest, the tree digests, a 655-world sample
  and the M2 control exactly.
- AC3 met, with N2: M1, M2, M2b, M3, M4, M6 and M7 are killed. M5 survives as
  a cost mutant.
- AC4: this round, and the owner notice naming classes 1 and 4 (N1).

`syzygy-bpyt.8.22`:
- AC1 met: `needles: ADMISSION_PATHS` becomes `needles: []`, and the field
  needles are `everyField(ADMISSION_NEEDLES)` as before.
- AC2 met: 0 answers differ over all 184 decisions files with a needle
  appended, and the four paths in 92 probe and 12 real-file worlds. The M22a
  negative control is retained, and its mutated-tree digests check out.
- AC3 met: M22a is killed (28 failures, reproduced). M22b and M22c are
  genuinely equivalent.
- AC4: this round.

The coordinator's three conditions are met (raw section 6): the PR #505
record is not edited; 8.22's criteria and evidence are stated apart from
8.20's; and the class-4 extras are present. The classes are 1 and 4 (N1).
