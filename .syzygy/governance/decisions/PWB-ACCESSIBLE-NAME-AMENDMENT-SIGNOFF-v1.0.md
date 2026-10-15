# PWB accessible-name amendment — version-tagged sign-off v1.0

Date: 2026-10-15

Owner: Tzeusy

Package: pwb-accessible-name-amendment

Version: 1.0

Tag: pwb-accessible-name-amendment-v1.0

Kind: behavior amendment

Owner selection: P-99: Q1 "Sign v1.0" (by version tag under Scope A; carried to the version regenerated over P-86 by the cycle-3 answer "Carry if review clears"; the 3 notes carried in the separate notes record ROUND-4-DISPOSITIONS.md); Q2 "All focusable"; Q3 "One h1, no skips"; Q4 "File a POC-REQ-061 bead" (filed: syzygy-k0np); Q5 "First ready lands first"; Q6 "Every Polaris page"; Q7 "Label + source path"; Q8 "No exemption"

Review: docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-4-RAW.md

Reviewed commit: 83b29c96775d9c2215292fa41e1599080f0b802c

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: .syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/ROUND-4-DISPOSITIONS.md

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `pwb-accessible-name-amendment-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## Consequences recorded with the sign-off

Q1 "Sign v1.0" was answered on 2026-10-14 for the version round 3
cleared. The owner's cycle-3 answer "Carry if review clears"
(`decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`) carries
it to the version regenerated over the P-86 sign-off, on two
conditions, each verified before recording: the round-4 review named
above is notes-only, and `proposed/spec.md.patch` is byte-identical to
the version round 3 read.

Signing this version moves the PWB `spec.md` again, so it re-stales the
P-95 behaviour-contract re-pin package
(`pwb-behavior-contract-repin-tree-framing`, tracked by `syzygy-fxro` and
`syzygy-2g0d`): it must be redrafted over this sign-off and re-reviewed
before its acts can be offered. The P-95 package is not edited by this
sign-off. The body-read gate does not read the pin, so no Butlers read is
refused; the pins read Unknown until the next re-pin.

It also moves `spec.md` and `GOVERNING-DEPENDENCIES.md` under the two
pending PWB packages: the opening-index amendment (P-98) and the
release-label amendment (P-85) are regenerated over this sign-off's
applied bytes and reviewed again before they are offered.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
