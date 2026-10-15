# PWB anchor-resolution amendment — version-tagged sign-off v1.0

Date: 2026-10-14

Owner: Tzeusy

Package: pwb-anchor-resolution-amendment

Version: 1.0

Tag: pwb-anchor-resolution-amendment-v1.0

Kind: behavior amendment

Owner selection: P-96: Q1 "Sign v1.0" (by version tag under Scope A; the 9 notes carried in the separate notes record ROUND-2-DISPOSITIONS.md); Q2 "Keep RFC7-3" (no contract amendment commissioned); Q3 "Leave it" (no PWB-REQ-015 delta); Q4 "Machine only"

Review: docs/reviews/R-N9-MACHINE-CHANNEL-AMENDMENTS-2-RAW.md

Reviewed commit: ae8c074066d8e6c511d8064b505e3f89e3f2b43d

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: .syzygy/governance/contracts/candidates/pwb-anchor-resolution-amendment/ROUND-2-DISPOSITIONS.md

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `.syzygy/governance/contracts/candidates/pwb-anchor-resolution-amendment` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `pwb-anchor-resolution-amendment-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## Consequences recorded with the sign-off

Signing this version moves the PWB `spec.md` again, so it re-stales the
P-95 behaviour-contract re-pin package
(`pwb-behavior-contract-repin-tree-framing`, tracked by `syzygy-fxro` and
`syzygy-2g0d`): that package's builder now refuses it as stale, and it
must be redrafted over this sign-off and re-reviewed before its acts can
be offered (the package's `IMPACT-LEDGER.md`, "The behaviour-contract
pins"). The P-95 package is not edited by this sign-off. The
body-read gate does not read the pin, so no Butlers read is refused; the
pins read Unknown until the next re-pin.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
