# Owner sign-off packet — PWB state-(1) amendment

Date: 2026-09-02

Candidate: `polaris-project-wide-butlers-model`

Frozen candidate commit: `8847feef1442bf55fd5276a73248d3c58409e4db`

Manifest: `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`

Manifest SHA-256: `14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e`

## Decision

Should the eleven exact artifacts below supersede the currently signed PWB
package as the behavioral authority for the bounded, local,
one-Butlers-repository POC?

## What changes

- PWB-REQ-005 accepts each exact consent, policy and registry human owner act
  in valid state (1) or state (2), including all eight mixed/equal triples.
- PWB-REQ-022 accepts an exact-scope human owner judgment in valid state (1) or
  state (2).
- Every human and machine rendering retains the exact state. Only state (2) is
  independently verified. State (1) discloses that it is owner-trusted,
  uncorrelated and same-tree forgeable from Syzygy's perspective.
- Invalid acts fail closed. The signed test obligations close 195
  admission-invalid cases, 84 present-invalid judgment cases, 2 absent cases,
  exact two-channel parity and fail-then-restore mutation proof.
- Acts remain warrants. They are not evidence that a read, screening,
  comprehension or any effect succeeded.

## Accepted risk

State-(1) consent, policy, registry and judgment records are same-tree
forgeable from Syzygy's perspective. Exact digests detect drift; they do not
establish authorship or owner attendance. Choice A accepted this residual risk
only for this bounded POC. The amendment exposes the limitation and keeps every
other security gate conjunctive.

## Evidence and disclosed gaps

- Three final independent review classes returned exact `CONFIRM` on the same
  frozen commit and manifest:

| Raw review | Exact verdict | sha256 |
|---|---|---|
| `docs/reviews/R-PWB-STATE1-FINAL-SECURITY-RAW.md` | `CONFIRM` | `bb97a69c2dccb9f11b11867b3961211da36da539c1ebf3acde318a4680963748` |
| `docs/reviews/R-PWB-STATE1-FINAL-ORACLES-RAW.md` | `CONFIRM` | `6d247c65420f2a3ea686a1a7cd0bbea09510e88fc21cdf053e201474d694c6aa` |
| `docs/reviews/R-PWB-STATE1-FINAL-TRANSACTION-RAW.md` | `CONFIRM` | `f503efbad51d26c15dace2682da669f3e0ebb6f93953d87115c72759a4fadcfe` |

- The effective contract matrix remains 622 consequences: 137 covered, 237
  Unknown uncovered and 248 believed not applicable. No believed-N/A row is an
  owner-reviewed N/A judgment.
- No implementation or runtime effect has been performed or proven.
- Before this sign-off, the full governance battery intentionally fails CG-7h
  on five unsigned current-vs-historical PWB rows. Recording this act in both
  required homes is what permits the successor manifest to become current.

## Exact eleven-artifact package

| Artifact relative to the PWB change | sha256 |
|---|---|
| `.openspec.yaml` | `bd2504cb580ca73eeb2510481ca4665ee11e2127360fc0be12c104f347fb515f` |
| `CAPABILITY-COVERAGE.md` | `ea19d64bfad013e6cc72aa3f3d3f3b6bd57de69af911982a1b2e09919a34eed9` |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | `77f6b685f7a92eff39d874b92ed36b99e832ded16d1970f1242b6750641b5349` |
| `CONTRACT-COVERAGE.md` | `ada47e4b993951873855a3055e0958bd5e0947ab51060404b0ef11eaff84c578` |
| `GOVERNING-DEPENDENCIES.md` | `3a92308493b501867e8de55a7d2a9cee2682c87102cee84385fe91b0ad3d8517` |
| `contract-coverage-matrix/RFC-0001-0003.md` | `f28404be66a4241503f2214757d640361751934b2ab308dafeada5c6d2152e50` |
| `contract-coverage-matrix/RFC-0004-0006.md` | `ec091e743cb95070b30980021f2b5bdf054128161a86f6f8a8bbdf7678ffbc29` |
| `contract-coverage-matrix/RFC-0007-0009.md` | `6e480d6b94734abd41b15fbdcab1e6d7df9d60f68f0f3f5b0d66f98462728cd0` |
| `design.md` | `5aad0cff64892b5b7d6fed82d9ed5e928938df767cfe575c89e746a481fc5fdc` |
| `proposal.md` | `200217d307ce72de804c82b75bedaf5aae462e29d0bcbfbe5e3b6c96f952a675` |
| `specs/polaris-project-wide-butlers-model/spec.md` | `2e453a6ec6dbc19c5df226650c6e7a94c46e81f65d9d180f57d1dc1dce7fd07e` |

The manifest generator independently verifies this closed, codepoint-sorted
population. All eleven rows take effect together or none do. `.openspec.yaml`
is unchanged semantically but remains bound as part of the indivisible package.

## Effect of sign-off

This act signs the amended PWB behavior and supersedes the six PWB artifact
digests still current from the 2026-08-31 sign-off plus the five coverage
artifact digests made current by the 2026-09-01 general trusted-bootstrap
transaction. Those prior acts, manifests, digests and bytes remain immutable
historical evidence.

If performed, the ceremony will be recorded as state (1), `owner-adopted
(bootstrap, uncorrelated)`, with A1 audit-record identity explicitly absent. It
is a real human owner act only if the owner performs the exact phrase below.
The commit, tag and in-tree records preserve context but do not establish
attendance or state (2).

## What sign-off does not authorize

Sign-off does not create or approve observation consent, the concrete secret
policy, the adapter-registry entry or a walkthrough judgment. It authorizes no
repository-body read and no PWB implementation. It grants no write, egress,
execution, deployment, release, recovery, mission, another repository,
autonomous behavior or multi-user support. Separate effect-specific owner acts
and separate implementation authorization remain mandatory.

## Exact owner response

If and only if these exact reviewed bytes should become the amended behavioral
authority, respond exactly:

```text
SIGN OFF PWB STATE-(1) AMENDMENT: 14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e
```
