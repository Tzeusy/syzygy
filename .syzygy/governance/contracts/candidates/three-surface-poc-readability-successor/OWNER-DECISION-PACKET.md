# Three-Surface POC readability successor — owner decision packet

> **Status:** Proposal. It binds nothing until the owner performs the act
> below (VIS-4). Until then the signed POC specification stays exactly as
> `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` and the general trusted-bootstrap
> transaction bound it.

The package restyles the six-file Three-Surface POC specification for
reading. No requirement changes: the same 24 POC-REQ identities keep their
words, scenarios and warrants, and the POC stays bounded and non-release.

## What you are asked to decide

Whether to sign off the restyled specification, in one act. To sign off,
write exactly:

```text
SIGN OFF THREE-SURFACE POC READABILITY SUCCESSOR: 221f1ececa321bf0cc6cd5e01f401e9eada38466c3c00dde43095f8cb8a0cd4d
```

The argument is the sha256 of
[`THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt`](THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt),
whose six rows name each subject's proposed digest. If you say nothing, the
current signed bytes stay in force.

## What changes

- **Requirements.** Each opens with its required behavior; its quantified
  scope moves into a child bullet beneath. Requirement words are unchanged;
  the package builder checks every body.
- **Proposal and design.** Each leads with the capability and its one-model
  flow: evidence enters one shared `PocModel`, and Polaris, Trajectory,
  Orrery and the machine answer project it without minting facts.
- **Generated dependencies** follow the new spec digest.
- `CONTRACT-COVERAGE.md` and `.openspec.yaml` are unchanged.

## What adopting does

The recorder, `scripts/record_three_surface_poc_readability_successor.py`,
writes the act record and its section in the acceptance record, then installs
the four restyled files. Its `--check` then verifies all six subjects against
their successor rows.

It widens no implementation direction and grants no source, provider, write,
deployment or release permission.

## Evidence

- **Specification reviews** (draft PR #136): rounds 1–3 `REVISE`, each
  repaired; round 4 `CONFIRM`, over these exact manifest bytes
  ([`R-POC-READABILITY-SUCCESSOR-REVIEW-4-RAW.md`](../../../../../docs/reviews/R-POC-READABILITY-SUCCESSOR-REVIEW-4-RAW.md)).
- **Package review**, over this packet, the recorder and its checker
  registration: pending. The recorder refuses to record until that review
  confirms the manifest digest above.
- **Read-only checks:**

  ```text
  python3 scripts/build_three_surface_poc_readability_successor.py --check
  python3 scripts/record_three_surface_poc_readability_successor.py --check
  ```
