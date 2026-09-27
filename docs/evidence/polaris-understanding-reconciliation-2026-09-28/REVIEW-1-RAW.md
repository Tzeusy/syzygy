Title: Polaris understanding exact-digest reconciliation — C1 review

Verdict: REVISE  
Reviewed commit: af327b062fda0c987ad5bb2205b381c7c27feac0  
Reviewer: independent fresh-context agent

## Blocking findings

**M1 — A non-confirming raw review can satisfy the confirmation gate.** In `scripts/record_polaris_understanding_adoption.py`, `reviewed_template()` counts only lines matching `^Verdict: PASS$`. A raw containing a `Verdict: REVISE` header and one later `Verdict: PASS` line is accepted as confirming. I reproduced that predicate result read-only. Require exactly one verdict header, whose complete value is `PASS`, and add a refusal mutation for contradictory headers.

**M2 — An ambiguous reviewed-commit header is accepted.** The same function extracts only well-formed SHA headers. A raw containing `Reviewed commit: wrong` and a later valid `Reviewed commit: af327b062fda0c987ad5bb2205b381c7c27feac0` produces one accepted commit match. Require exactly one reviewed-commit header before validating its full SHA, and add a refusal mutation. These two gaps mean the retained raw can be ambiguous while `--check` reports a confirmed chain. Do not append the technical record from this C1.

## Evidence checked

[Observed] The owner record at `077089d6268323c86fab9f6a5c32217e4955c006` identifies amended REQ-004 “as merged with this record.” Independent Git reads confirm the historical eight-row manifest, seven unchanged subject blobs, and the REQ-004 transition from `b7c95f57ca5f67a18570b7124d20b223dff99aea2a936efef76d5940a400f93f` to `6841e63cda0ccdb81966a6fabbdfaf3721910df8ea04959711eb59843859ba58`. Only REQ-004 changes; its five added scenarios change the effective composition from 31/177 to 31/182. The historical act, aggregate block, owner direction, packet, four raw reviews, spec, and implementation bytes are preserved. [Inferred] The owner-to-blob correspondence is deterministic; this technical package performs no new owner act.

[Observed] `--candidate-check` passes repeatedly; 25 reconciliation mutations are refused; production `--check` fails as intended while the review and record are absent. After validation scratch was moved outside the worktree, `check_governance.py` reported 0 FAIL, its selftest reported 305 passing fixtures, and the clean-clone log records 36 passing battery checks. The worktree is clean at the reviewed commit.

**Nonblocking:** `git diff --check f7d80ca...HEAD` flags whitespace on blank context lines inside `final-documentation.patch`. The patch applies and its before/after hashes validate; clean the artifact when preparing the new freeze.

## Reviewed input hashes

- `.github/workflows/governance-docs.yml`: `4207b793de709a3003428bf32190a42f279585adc3865177646e8cc2a6336f14`
- `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`: `6093dbbe519dad6c35a5aaeeb31355d2e435d76ec4f0c2c9affb0d1e5b6b5621`
- `.syzygy/governance/decisions/README.md`: `1d960d556c940a6367813f54b087a08c1e89cfb09070df47ff1b14b7a13ade12`
- `.syzygy/governance/doctrine/vision.md`: `93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d`
- `PROJECT-STATUS.md`: `53e9ae06b4b969f7ebe05c54c66f89f29751ab8ab952db4325e34f7a827347df`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/README.md`: `feab56ce976b36024781efa557e001fbf1c58e6a096c3372f4faf30783a3afe9`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/documentation-images.json`: `4feab500ead279f8ff6d9a2926bc670d59c47aa9a4a5856fcd7fb49fe41eb75f`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/final-documentation.patch`: `96f889b6054811f240a973982d2c38a0f580802d6a7e0f26321457ec5d7109e1`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/proof.json`: `0d61eb32066d9ceebc41e2f8ff9ce964cd47cd6162f843cbb9caf9ef264e1712`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/technical-record-template.json`: `582f5be9a744254e7ebc3c0ea79907d1dca92d9511c78c4807a7ea257ead9ecb`
- `scripts/record_polaris_understanding_adoption.py`: `a95212d4ea11db4934dfbe099c3791f15c3ba49bbfdac9e357eb316a9f443ac0`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/review-inputs.json`: `7ee083bc538c7ee8e2ccd0ba61b6fd9c905ce5a92cbc09bd5ca38e7d8ad4463b`
