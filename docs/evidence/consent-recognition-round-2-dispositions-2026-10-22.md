# Consent-gate recognition models: review dispositions, rounds 1 and 2

[Observed] This record dispositions the two CC-REV-1 reviews of
`syzygy-bpyt.8.10` (pull request #500), whose subject is the measurement
report `docs/evidence/consent-gate-recognition-models-2026-10-21.md`.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-CONSENT-RECOGNITION-1-RAW.md` | `REVISE` | `c08a015d` | `r1-review.diff` sha256 `97c05f9c0e5d8f906b9a0d3d789c3292f8b4b5e983f22c63f0c819dcc1f249e2` |
| 2 | `docs/reviews/R-GP-IMPL-CONSENT-RECOGNITION-2-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `09a9807a` | `r2-review.diff` sha256 `a0e75a25b612d52479c2275301dfa6557f159a0fec1fe22ca6bb18aab80f5ded` |

Round 1's subject equals `git diff 26ff52ce c08a015d`. Round 2's subject
equals `git diff b7697f6a 09a9807a`. It is also `git diff 1d6731bb e547aaf9`,
the diff between main and this pull request's merge of that main.

Round 2 says "No finding has to change the reviewed bytes before merge or go
to the owner first" (section 7). Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), round 2 clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the round-2
notes ask for. It is an implementation record and binds nothing.

Revise-severity findings open after round 2: 0

## Round 1

Round 1 found two blocking findings and five notes. All seven were repaired
in commits `9216ca29` and `09a9807a`. Round 2 judged each one repaired (raw
section 4), and checked that the repair re-derived its figures and copied none
from round 1 ("Rule 10 check", section 4).

| Finding | Round 1 heading (raw section 4) | Repair, as round 2 confirms it |
|---|---|---|
| F1 | false [Observed] claim that no gate decision reads a field-parsed record's prose | The claim, headline bullet 3 and residual 3 are scoped to the consent readers. A new subsection names how the PWB P1 gate reads screening-scope v4. `consent-gate-recognition-models-pwb-gate-2026-10-22.json` measures that reading end to end, and `consent-gate-recognition-models-readers-2026-10-22.json` holds the reader sweep with its denominator. |
| F2 | the proposal leaves out recording-tag byte equality | A T3 row, costed beside K, T1 and T2, with a recording-tag census. The recommendation stays K, labelled [Inferred]. |
| N1 | `SLOT.line` reachability belongs in the report and in the owner notice | Residual 2 states who can trigger the stall and which five commands it stalls. The fix is `syzygy-bpyt.8.17`, and the owner notice on `syzygy-bpyt.10` names it as a class-4 availability finding. |
| N2 | the "only the 14 new tests" re-run is not retained, and runner output used as SPEC loses fields | Retained as `consent-gate-recognition-models-mutants-selected-2026-10-22.json` (43 of 43 killed). The runner's lost `project` and `subjectFiles` fields are carried on `syzygy-bpyt.11`. |
| N3 | "any appended text" overclaims | Corrected to the census's one appended suffix, with the HTML-comment opener's refusal cited. |
| N4 | the census and timing records bind a commit, not the build they executed | Residual 7 states the limitation. The new probe digests the `dist` directories it lists, which round 2's N1 qualifies below. |
| N5 | the three new scripts are outside the battery and CI, and the report does not say so | The report says so. 0 hits over the battery block and the three workflow files. |

## Round 2

### N1: the probe digests three of the four `dist` directories it loads

[Observed by the reviewer] The report's residual 7 says that the probe record
"names a digest of each `dist` directory it loaded from
(`measuredOn.built`)". The probe's `DISTS` list has three directories. Its
import closure also loads `packages/cap1-core/dist`, through
`three-surface-poc-core`'s index (`project-shape-model.js:18`). No value from
`cap1-core` is on the evaluator path, so no verdict depends on that directory.

**Correction.** Residual 7's last bullet reads: the probe record names a
digest of each of the three `dist` directories the script lists. Its import
closure also loads `packages/cap1-core/dist`, which it does not digest and
which no evaluator check reads. The retained record and the report are not
regenerated. A later version of the probe adds the fourth directory, or
derives the set from the loaded module graph.

### N2: "production" mislabels the reader sweep's population

[Observed by the reviewer] The report defines the population exactly: every
tracked `.ts` file under `packages/` and `apps/` whose name does not end in
`.test.ts`, `.testkit.ts` or `.d.ts`, 231 sources. The pull request body, the
readers record's `text` and the sweep script's docstring call those 231
"production" sources. The set also holds test support (`testing.ts`,
`test-walkthrough-judgment-fixture.ts`, the `cap1-system` harness). It is a
superset of the production `.ts` files, so the absence direction is
conservative. Outside it, 23 tracked files under `scripts/` name a census
record by file name. They are recorders, builders, CI checks and installers,
and [Inferred by the reviewer] none of them is a runtime gate.

**Correction.** Read the 231 as "non-test-named `.ts` under `packages/` and
`apps/` (runtime code plus test support)". `scripts/` was not swept: 23
tracked files there name census records, all of them operator or CI tooling.
These matter to any bead that changes the bytes those tools regenerate or
compare. That includes T1 or T3 if the owner chooses either at
`syzygy-bpyt.1.8`, whose notes carry this population.

## Owner notice

The class-4 owner notice for this pull request is posted on `syzygy-bpyt.10`
when it merges. It names `SLOT.line` as a class-4 availability finding
(`syzygy-bpyt.8.17`) and the K, T1, T2 and T3 choice at `syzygy-bpyt.1.8`.
