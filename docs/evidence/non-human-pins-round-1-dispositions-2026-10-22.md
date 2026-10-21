# Non-human-principal pins: round-1 review dispositions

[Observed] This record dispositions the notes of
`docs/reviews/R-GP-IMPL-NON-HUMAN-PINS-1-RAW.md`, the round-1 CC-REV-1
review of `syzygy-bpyt.6.8` (pull request #504).

- Verdict: `CONFIRM WITH EXCEPTIONS` (line 2 of the raw).
- Reviewed commit: `df2f67e1` (line 3).
- Subject: `r1-review.diff` sha256
  `3f6e1daeb2508375a90a998749aed21cbdab188251b868fa6e2104c7163ffe58` (line 4),
  equal to `git diff b7697f6a df2f67e14da12b5d553276b4324511227288b009`.

The raw says "No F-findings. Four notes." (section 4) and, for changed
outputs, "There is none." (section 5). Under the owner's notes-only stopping
rule (`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the notes ask
for. It is an implementation record and binds nothing.

Revise-severity findings: 0

## N1: the unchanged rule refuses some human names

[Observed by the reviewer] "Claude Monet", "Jean-Claude Van Damme" and
"Marie-Claude Lee" match `NON_HUMAN_PRINCIPAL` through its `claude` word, and
"Ci Wang" through `^ci` plus whitespace. The non-human test runs before the
expected-owner test, so a registered owner with such a name would be refused
as `owner-non-human`. This is fail-closed and predates the pull request. None
of the 17 new owners is a human name, and the one new human name,
`Annagpt Lee`, is held human.

**Disposition:** the pins stay. Narrowing the rule changes what a gate
refuses, so the question goes to the owner as `syzygy-bpyt.1.10` (owner-gated),
together with the lane's question on merging the two line-start arms. That
question is stated narrowly: a merged arm changes only owners of the form
`machine/...`. The bead's recommendation is labelled Inferred. The question is
carried in the `syzygy-bpyt.10` owner notice.

## N2: the classification and the GP-Q0 checks

[Observed by the reviewer] The reviewer classifies the pull request as
CC-REV-1 class 4 at the test-oracle level, replacing the declared "none
(contestable class 4)". It got the review that class 4 requires.

**Disposition:** class 4 is recorded. Against the three GP-Q0 checks:
1. The old-versus-new differential is met vacuously. Every non-test,
   non-evidence path is byte-identical between base and head (0 of 10 changed
   paths, per the raw's sections 3A and 3B), so any such differential returns
   no changed row.
2. A rule-6 mutant per predicate is met: 45 of 53 killed, and the 8 survivors
   are language-equivalent (raw section 7). The reviewer re-ran 53 of 53.
3. The owner notice is posted on `syzygy-bpyt.10` when the pull request
   merges, with N1's question.

## N3: the test comment and the headline overstate

[Observed by the reviewer] The comment above both `NON_HUMAN_OWNERS` tables
says each owner is "matched by no other alternative". The first six owners are
each matched by the word in both line-start arms, and the comment leaves out
`daemon-7`. The pull request's headline, "every alternative ... has a test that
fails when it is deleted", has eight exceptions, which its Residuals disclose.

**Disposition:** the comment fix is filed as `syzygy-bpyt.6.11` (P3), a
test-comment-only edit. In this record and in the owner notice, the headline is
read as "every alternative whose deletion changes the language".

## N4: evidence re-checkability and a missing harness guard

[Observed by the reviewer] `verification-2026-10-22.json` lists digests of
seven logs that are not retained. Its governance note is a literal in
`assemble_verification.py`, not derived from the logs. The mutants records do
not store the harness's own sha256. `run_tests` never compares a mutant's total
with the baseline, so a mutant that broke module load would count as a
survivor. That did not happen here: every recorded total equals the baseline.

**Disposition:** filed as `syzygy-bpyt.6.11` together with the lane's
harness-selftest follow-up. The retained records are not edited. A new record
replaces them where a re-check needs it.
