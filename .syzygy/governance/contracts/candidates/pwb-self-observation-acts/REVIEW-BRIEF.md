# Review brief — three acts for a test-only self-observation

> **Candidate — binds nothing.** This brief says what an independent
> reviewer should be given and what they are asked to decide. It is not a
> review and gives no verdict. No review has been run on this package.

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
  - the P-74 row of
    `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`;
  - RFC1-3 in
    `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`;
  - PWB-REQ-005 in
    `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`;
  - `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`;
  - SEC-4 and SEC-5 in `.syzygy/governance/doctrine/security.md`.
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
4. Does the consent record avoid putting words in the owner's mouth?
5. Are the landing-order table and the regeneration claims in the packet
   correct against the tree?
6. Do the `--selftest` mutants each break a distinct check, and does any
   check in `check()` have no mutant?
7. Are the [Observed] labels backed by a sweep with a stated denominator?

Store the verdict word exactly and the raw output unchanged, in a file whose
name ends in `-RAW.md` under `docs/reviews/`.
