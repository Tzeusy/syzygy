# Three-Surface POC governing-intent amendment — version-tagged sign-off v1.0

Date: 2026-10-14

Owner: Tzeusy

Package: three-surface-poc-governing-intent-amendment

Version: 1.0

Tag: three-surface-poc-governing-intent-amendment-v1.0

Kind: specification amendment

Owner selection: P-100: Q1 "Syzygy's records only" (recorded as the direction for the later link amendment; it authorizes nothing now); Q2 "Sign v1.0" (by version tag under the Scope A extension to POC amendments; the 7 notes carried in the separate notes record ROUND-3-DISPOSITIONS.md); Q3 "Keep deferred"

Review: docs/reviews/R-N10-POC-GOVERNING-INTENT-3-RAW.md

Reviewed commit: 52c1d0f5536260628de7633126ef21748fe5e95e

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: .syzygy/governance/contracts/candidates/three-surface-poc-governing-intent-amendment/ROUND-3-DISPOSITIONS.md

Scope A extension: `.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md` extends the direction below to this package's kind

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `.syzygy/governance/contracts/candidates/three-surface-poc-governing-intent-amendment` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's checks passed (every patch applies to the signed
bytes, and the dependency generator over the patched specification
reproduces the patched declaration) before its patches were applied.

The binding is the annotated tag `three-surface-poc-governing-intent-amendment-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## Consequences recorded with the sign-off

Q1 "Syzygy's records only" is recorded as the owner's direction for the
later amendment that defines the governing-intent link: Syzygy keeps the
intent reference in its own record when it creates a work item and shows
the link from there, and reads no new Butlers field (no `external_ref`,
`description` or `design`). That amendment, its sign-off and an
implementation authorization are still needed; this direction authorizes
nothing now. Q3 "Keep deferred": the source-to-claims index stays
deferred to a later PWB change.

The pending identity amendment (P-84) patches the same four files, and
the two are a declared mutually exclusive pair, so P-84 is regenerated
over this sign-off's applied bytes before it is offered. Its next review
also re-judges POC-REQ-014's encoding arm and its RFC2-24 and RFC8-24
rows against P-84's amended POC-REQ-060, which that arm now reads (the
round-3 raw's note 4). The P-84 package is not edited by this sign-off.

## Applied subjects

This package carries no manifest. Each row below is the SHA-256 of one
subject as this sign-off applied it, in manifest row form; the
reconciliation and later-row readers take this record as the package's
manifest.

```text
9187547d8cc17017ebd44132527d2d5e096d1ef9705de80cc4f1cf34531f6976  openspec/changes/three-surface-poc-experience/.openspec.yaml
2657a33d5089464ee0d89f29e4354f69f81892c3bccf35744e84fa1168c35ae3  openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md
7c68dbdde5bb6ec84c83cf2c15c5a5be3e06e340cebc4d0f817c34fe9507d92a  openspec/changes/three-surface-poc-experience/GOVERNING-DEPENDENCIES.md
6d39ea6f6111abaea32c74ce96c975ae53e077485f0ed8f7c97545e64d7ba295  openspec/changes/three-surface-poc-experience/design.md
b890f44f0ed082546da4a2faf499058b96395eb7c4d5930b2f79f406963605f7  openspec/changes/three-surface-poc-experience/proposal.md
6b302779843366674eecc63f5a0b4fac6a03213c6b7eda2502c2624ebb075b56  openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md
```

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
