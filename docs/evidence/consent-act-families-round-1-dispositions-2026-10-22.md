# Consent act families: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.8.4`
(pull request #505). That change makes the consent gate's admission,
screening-scope policy (versions 1 to 4) and RFC5-14 class-act readers rows of
one form shape, `ActForm`, read by one `parseActRecord`. Their three withdrawal
sweeps and the digest-bound sweep become one `namesAct`, walked by one
`findActRecords`, in `packages/polaris-generation-consent/src/package-reader.ts`.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-ACT-FAMILIES-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `9f49b6cb` | `r1-review.diff` sha256 `c0fc8b9ed4e570d4040f32563ade0ac29109540c231a9fbbd2530693eb1a3415` |

The subject equals `git diff b7697f6a 9f49b6cb`. Main has since moved, and
the branch merged it at landing. After that merge,
`git diff origin/main HEAD | sha256sum` printed the same digest, so the merge
brought only main's bytes.

The reviewer found "No blocking finding." (section 4) and 11 notes, and wrote
that "GP-Q0 part 3 is not engaged". Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## Retained review evidence

The reviewer's tools and the outputs this record relies on are retained
under `docs/evidence/consent-act-families-review-2026-10-22/`:
- `tools/`: the reviewer's scripts named in raw section 3;
- `row-spec.json` and `row-mutants.json`: the 16 supplementary row mutants
  (N3), with each mutant's `old` and `new` fragment, the commit `9f49b6cb`
  and the `package-reader.ts` digest;
- `dossier-spec.json` and `dossier-rerun.json`: the five dossier mutants
  re-run under their own project (N11);
- `differential-sensitivity-pol-quoted.json`: the negative-control run of
  the differential, which reports 6 mismatches (raw section 3 item 7);
- `probe-rerun.txt`: the 50 constructed worlds, 0 of 350 answers differing
  (raw section 3 item 8).

The two 1.4 MB re-run records (the differential and the 101-mutant replay)
are not retained. The raw states that they reproduce the committed records
exactly (items 6 and 9).

## N1: classes 1 and 4, not 4 alone

[Observed by the reviewer] The change also rewrites the sweep and parse path
of `readDigestBoundActState` and `readVersionedSignoffState`. The dossier
start gates (`gate-sources.ts`) read both to decide whether the
source-acquisition adapter is authorized, which is CC-REV-1 class 1.

**Disposition:** accepted. The pull request body now says "classes 1 and 4",
and so does the owner notice on `syzygy-bpyt.10`. GP-Q0 sets the same extra
checks for class 1 as for class 4, so no further evidence is owed.

## N2: the owner notice

**Disposition:** posted on `syzygy-bpyt.10` at landing. It names classes 1
and 4, the differential and mutant records, and the knob decision (N9).

## N3: the rule-6 record has no mutant for most form rows

[Observed by the reviewer] The record leaves several rows unmutated:
- the version 1, 2 and 4 policy spreads;
- the version 1 to 3 identities and the version 4 title;
- three admission rows;
- each family's `forms` list and each strict reader's choice of dialect.

So the pull request body's "every form-row field the change touches"
overstates the record. The reviewer's 16 supplementary mutants over exactly
those rows are all killed (raw section 3 item 10).

**Disposition:** corrected here. The 16 mutants are retained in
`docs/evidence/consent-act-families-review-2026-10-22/row-mutants.json`.
Together with the lane's record, they give one killed mutant per form row.
Two of the 16 are killed by one test each (raw section 3 item 10).

## N4: `adm-needles` survives and is equivalent

[Observed by the reviewer, raw section 3 item 11] The folded spelling of each
of the four `ADMISSION_PATHS` needles contains the folded spelling of an
`ADMISSION_STEMS` needle, so the mutant is equivalent, in head and in base.
Acceptance criterion 3 is met with that proof.

**Disposition:** equivalence accepted. Dropping `ADMISSION_PATHS` from the
text needles is a change to a consent sweep, so it is filed as
`syzygy-bpyt.8.22` (P4) with its own differential and review.

## N5: the differential binds the source digest, not what ran

[Observed by the reviewer] `scripts/differential_consent_act_families.mjs`
runs each tree's `dist` but records only the `src/package-reader.ts` digest.
The reviewer edited `dist` alone: the run reported 6 mismatches, and its record
still named the source digest.

**Disposition:** the committed record is unaffected. The reviewer reproduced
every one of its 3890 world rows from fresh, freshly built clones (raw
section 3 item 6). Any later differential must record the compiled digests;
this requirement is posted on `syzygy-bpyt.8.20`, the next bead to run such a
differential.

## N6: "1510 distinct answer vectors" measures content, not verdicts

[Observed by the reviewer] Each compared answer carries the parsed act's
text, so the 1510 vectors carry only 167 distinct labels (verdict and reason).
`policy-chain@2026-10-08` never answers `ok` in any of the 3890 worlds. The
records port is compared on the 8 base worlds only.

**Disposition:** corrected here. "1510 distinct answer vectors" in the
record and the pull request body is not a measure of verdict coverage. The
chain-term code is not in the diff, and the unchanged suite's chain test
passes (raw N6). The fix for later records, labels beside vectors plus one
world where the mid instant reaches `ok`, is posted on `syzygy-bpyt.8.20`.

## N7: the altered-prose corpus copy

[Observed by the reviewer] The differential's altered-prose corpus is a
behaviour-equal copy of `PROSE_ALTERATIONS` and `HEAD_FIELD_ALTERATION` from
PR #500's `recorder-fixtures.testkit.ts`. The raw says #500 "has not merged".

**Correction:** #500 merged on 2026-10-21 as `3000698f`, before this review
ran (`gh pr view 500`: `MERGED`, head `e0101c1e`). [Observed by the
coordinator] The reviewer's `tools/compare_corpus.py`, run against main's
`packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts` and
this pull request's script, prints "EQUAL after stripping TS annotations"
with 0 of 16 literals missing. `git diff c08a015d origin/main` on that
testkit is empty. So the copy matches the merged corpus.

**Disposition:** corrected here. The record stays valid for its own bytes.
Importing the corpus instead of copying it is posted on `syzygy-bpyt.8.20`.

## N8: the runner's recorded `command` is not the command run

[Observed by the reviewer] `scripts/rule6_mutation_runner.py` now passes
three reporter flags that its recorded `command` omits. No existing caller's
verdict changes, and no CI step, battery line or script calls the runner.

**Disposition:** added to `syzygy-bpyt.11` (the runner bead).

## N9: the unaligned knobs, some fail-open

[Observed by the reviewer] The per-family knobs were kept, as GP-Q0 part 3
requires, and `act-families.test.ts` pins them. Some are fail-open. In the
reviewer's world `policy-quoted-agg-act-id`, a blockquoted
`> Act identity:` line naming policy version 1 in the aggregate record leaves
the policy `ok` in both trees.

**Disposition:** filed as the owner decision `syzygy-bpyt.1.12`, one option
per knob. Every alignment makes a gate stricter, so nothing changes here.

## N10: the bead's own text is stale

**Disposition:** at close, the bead description is amended to name policy
versions 1 to 4 and `packages/polaris-generation-consent/src/package-reader.ts`.

## N11: replaying the record scores five empty runs as kills

[Observed by the reviewer] The mutant record mixes projects, and its five
dossier mutants carry no `project` key. Replayed as a spec, they run under the
consent project. Vitest prints "No test files found, exiting with code 1", and
the runner counts that as killed. Re-run under `@syzygy/polaris-dossier`, all
five are killed with the record's counts, so 101 of 101 match the record.

**Disposition:** corrected here. To replay
`docs/evidence/consent-act-family-mutants-2026-10-22.json`, take each
mutant's project from its recorded `command`
(`consent-act-families-review-2026-10-22/tools/dossier_spec.py` does this).
The record is bound to the reviewed bytes and is not split. Added to
`syzygy-bpyt.11`: stop the run, rather than score a kill, when vitest selects
no test file.

## Risk class

Classes 1 and 4 (N1). GP-Q0's checks:
- the differential: met. 0 of 18,366 answers changed over 3,890 worlds, which
  the reviewer reproduced exactly, and 0 of 350 over the reviewer's own 50
  worlds. A recorded negative control reports 6 mismatches.
- a rule-6 mutant per predicate: met. The lane's 101 mutants reproduce (100
  killed, 1 equivalent survivor), and the reviewer's 16 row mutants are all
  killed (N3, N4).
- the owner notice: posted at landing.
