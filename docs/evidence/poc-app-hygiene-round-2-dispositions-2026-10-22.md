# POC app hygiene: review dispositions, rounds 1 and 2

[Observed] This record dispositions the two CC-REV-1 reviews of
`syzygy-bpyt.5.5` (pull request #501): the `main(argv, io, deps)` entry point,
the un-exported internals, and the deleted orphan module.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-POC-APP-HYGIENE-1-RAW.md` | `REVISE` | `4f3c3ebf` | `r1-review.diff` sha256 `fbbfadfd7b5b6ca2bc345528797f2d5b45eb0162d8a0db960e3f5a3c34138e78` |
| 2 | `docs/reviews/R-GP-IMPL-POC-APP-HYGIENE-2-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `20b23d90` | `r2-review.diff` sha256 `c72823c311a55a3f4d45abb4e6d257efc5f410bebfd8e9410218701993741a83` |

Round 1's subject equals `git diff 26ff52ce 4f3c3ebf`. Round 2's subject
equals `git diff 1d6731bb 20b23d90`. It is also `git diff 3000698f 2cae50f9`,
the diff between main and this pull request's merge of that main.

The reviewers ruled the CC-REV-1 classes as **1** (the P1 repository-binding
composition) and **3** (the `PocRuntimeCapture` composition), not the
declared "none". Round 2 found "No F-findings (blocking). Seven notes."
(section 5). Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), round 2 clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the round-2
notes ask for. It is an implementation record and binds nothing.

Revise-severity findings open after round 2: 0

## Round 1

Round 1 found two blocking findings and five notes, all repaired in commits
`06324099`, `cb35ce13`, `999877e5`, `fa79bca6` and `48944066`. Round 2 judged
each one in its section 4 and confirmed that the repair re-derived its figures
rather than copying them from round 1. F1 was repaired by the coordinator's
choice of arm: `main` moved into the side-effect-free `poc-main.ts`, and
`main.ts` stays an unconditional entry.

| Finding | Round 2 status |
|---|---|
| F1: the entry-script guard changed the exit code and output for two invocation forms | Repaired. 30/30 invocation pairs identical; the control at `4f3c3ebf` gives 10/30 |
| F2(a): classes 1 and 3, not "none" | Repaired |
| F2(b), F2(c): the bare `PocObservationError` case and the suffix-filter mutant | Repaired; 27/27 recorded mutants killed |
| F2(d): the altered-prose limb mapping | Repaired, with an overclaim corrected below (round-2 N2) |
| F2(e): the owner notice | Posted on `syzygy-bpyt.10` at merge |
| N1 to N5 | Repaired; N3 and N5 with residue (round-2 N3 and N5) |

## Round 2

### N1: five repository-rooted arguments survive the tests

[Observed by the reviewer] Five non-equivalent mutants of `poc-main.ts`
survive both `main.test.ts` and the differential:
- `bound-locator-ignored`;
- `reobserve-horizon-root`;
- `session-clock`;
- `verbatim-reader-root`;
- `materialize-target-root`.

Four more mutants are killed only by the differential, which CI does not run.
Every branch predicate is killed, so the GP-Q0 limb "a rule-6 mutant per
predicate" is met. The code matches base, and base had no `main` tests.

**Disposition:** filed as `syzygy-bpyt.5.8` (P2). It adds a fake
`resolveBinding` returning a different locator, a `materializeRoutes` seam and
a blob-reader root check, and it records all nine mutants as killed by
`main.test.ts`.

### N2: the altered-prose selector is head-side and import-based

[Observed by the reviewer] `dist-compare.mjs` selects the 29 "record-reading"
modules by a head-side test for a `node:fs`, `node:fs/promises` or
`node:child_process` import. Base `main.js` matches that test and differs, so
it falls out of the 29 by construction. Twelve modules that read records
through a package, among them `production-reobserve.js`, are not selected.

**Correction.** The altered-prose limb rests on the 90-module tally. Of 90
common non-test modules, 88 are byte-identical or identical once comments and
`export` are removed. The 2 that differ are explained: `main.js` is the
composition root, which the 42-scenario differential covers, and
`polaris-narrative.js` lost only the deleted dead constant. The "29, 0 differ"
figure is a head-side, import-based subset and does not by itself discharge
the limb. A later use of `dist-compare.mjs` should evaluate the selector on
both sides and include package-mediated readers, or argue from the full tally.

### N3: the dist-compare trees and the verification note

**Correction.** `dist-compare-2026-10-22.json` compared base `b7697f6a` with
head `fa79bca6`, which its `trees` field names only by path. Round 2
reproduced the comparison at `1d6731bb` against `20b23d90`.
`verification-2026-10-22.json`'s `subject.note` says the pushed head differs
only by the record set. That holds for `apps/`, but not for the tree:
`fa79bca6..20b23d90` touches 26 files, the merge of main included. Future
`dist-compare.mjs` records write `git rev-parse HEAD` for each tree.

### N4: an in-process changed output

**Correction to "Changed outputs: None".** `main.ts` now assigns
`process.exitCode = await main(…)` unconditionally, so on success paths an
in-process importer reads `0` where base left it `undefined`. The process exit
status is unchanged: 0 at both base and head. No GP-Q0 output changes.

### N5: test timing

[Observed by the reviewer] The `vi.waitFor` timeout equals vitest's default
test timeout, and `started()` polls with no stop condition.

**Disposition:** carried in `syzygy-bpyt.5.8` with N1.

### N6: the PR #499 credential sweep record names `main.ts`

[Observed by the reviewer] No check reads the dated sweep record. Its
embedded builder asserts that every hit is classified, so a regeneration
fails loudly until `poc-main.ts` takes `main.ts`'s place.

**Disposition:** the record is not edited. The note is carried on
`syzygy-bpyt.1.6`, the CC-SEC-3 packet, which is where a regeneration would
happen.

### N7: the route-capture fixture path

[Observed by the reviewer] The recorded capture digest (`baseCaptureSha256`
and `headCaptureSha256` in
`docs/evidence/poc-hygiene-2026-10-22/route-capture-2026-10-22.json`)
reproduces only with the fixture at `/tmp/zz-route-capture-fixture-repo`. The
base-versus-head equality reproduces at any path.

**Disposition:** the directory is deleted after landing, and the recorded
whole-file digest is read as path-bound. A future capture hashes its
transcript with the fixture path replaced by a placeholder, and keeps the raw
digest beside it.
