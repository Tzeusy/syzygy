# Review brief — three acts for a test-only self-observation

> **Candidate — binds nothing.** This brief says what an independent
> reviewer should be given and what they are asked to decide. It is not a
> review and gives no verdict. Round 1 returned REVISE over commit
> `5323721` (`docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-RAW.md`); round 2
> returned REVISE over `35e497b`
> (`docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-2-RAW.md`); round 3 returned
> REVISE over `64746a4`
> (`docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-3-RAW.md`). The round-3
> repair has not been reviewed.

## Status of the package under review

The package is drafted to step 2 of
`.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
and stops there. The drafter did not review it. Before any review, the
owner should answer the packet's open questions, because every answer that
changes a value also changes an act argument and retires any review of the
earlier bytes (verification rule 10).

## What the reviewer is given, and nothing else

- This directory: `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md`,
  `IMPACT-LEDGER.md`, the three manifests, and the three files under
  `proposed/`.
- `scripts/build_pwb_self_observation_acts.py`.
- The governing texts:
  - the P-74 and P-76 rows of
    `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`;
  - §2 question 4 of
    `.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`;
  - RFC1-3 in
    `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`;
  - PWB-REQ-005 in
    `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`;
  - `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`;
  - SEC-4 and SEC-5 in `.syzygy/governance/doctrine/security.md`;
  - `docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md`, question 3 and slice 6.
- For a confirmation round: the round-1, round-2 and round-3 raws and the
  packet's "Review record" tables, to check each disposition against the
  repaired bytes.
- For comparison, the Butlers originals:
  - the Butlers consent record and its act in `.syzygy/governance/decisions/`;
  - `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`;
  - `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`.

The reviewer should not be given this session's reasoning, the bead
history, or any other candidate package.

## What the reviewer decides

1. Does each drafted artifact do only what the P-74 ruling asks, and
   nothing wider? In particular, check that nothing observed can reach a
   route, cache, log, stored evaluation or walkthrough record.
2. Does the policy extension leave every Butlers rule byte-identical? Does
   its `inheritedRules` sentence really carry every screening rule over to
   the self scope, with no gap?
3. Is the `selfReferenceRule` enough to stop a governance file in this
   repository from acting as an authority input to its own observation?
4. Does the consent record avoid putting words in the owner's mouth? Is
   every sentence that says the owner ruled, chose or answered something
   backed by the owner's answer cell in the decision record, never by the
   record's own reading or "What it means" column?
5. Are the landing-order table and the regeneration claims in the packet
   correct against the tree?
6. Do the `--selftest` mutants each break a distinct check, and does any
   check in `check()` have no mutant?
7. Are the [Observed] labels backed by a sweep with a stated denominator?
8. For a confirmation round: is each finding of rounds 1 to 3 repaired as
   its disposition says, and did any repair introduce a new defect?
9. Does `--check` pin everything each draft says about what may be read,
   how, and where the result may go, as the packet's "How to verify" list
   says? Can any widening of a draft still pass it?

Store the verdict word exactly and the raw output unchanged, in a file whose
name ends in `-RAW.md` under `docs/reviews/`.

## The raw's head

This package has three act arguments, so the head carries all three on one
line. The first four non-blank lines of the raw must be, in order:

```text
# <title of the review>
Verdict: <verdict word>
Reviewed commit: <40 hex digits>
Manifest rows (act arguments, proposed-bytes sha256): consent <64 hex>; registry <64 hex>; policy <64 hex>
```

As a Python `re` pattern matched against the fourth non-blank line:
`^Manifest rows \(act arguments, proposed-bytes sha256\): consent ([0-9a-f]{64}); registry ([0-9a-f]{64}); policy ([0-9a-f]{64})$`.
Each digest is that act's manifest *row*: the SHA-256 of the proposed bytes
(for the policy, its current bytes with the patch applied), which is the
act argument and which `--check` prints. It is never the SHA-256 of a
manifest file. Round 3's raw already used this form.
