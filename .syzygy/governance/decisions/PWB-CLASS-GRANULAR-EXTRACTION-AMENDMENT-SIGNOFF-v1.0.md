# PWB class-granular extraction amendment — version-tagged sign-off v1.0

Date: 2026-10-14

Owner: Tzeusy

Package: pwb-class-granular-extraction-amendment

Version: 1.0

Tag: pwb-class-granular-extraction-amendment-v1.0

Kind: behavior amendment

Owner selection: P-86: Q1 "Sign v1.0" (by version tag under Scope A; the 4 notes carried in the separate notes record ROUND-4-DISPOSITIONS.md); Q2 "Unknown, list headings"; Q3 "Independent + note"; Q4 "Multi-heading rows" (list and table rows naming two or more headings at one level); Q5 "First ready lands first"; Q6 "Separate REQ-004 delta"; Q7 "Its body was read"; Q8 "Drafted order" (the code is changed at build where it differs)

Review: docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-4-RAW.md

Reviewed commit: c88a621f483b8a702c15b3bcb6f894252a9b0af5

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: .syzygy/governance/contracts/candidates/pwb-class-granular-extraction-amendment/ROUND-4-DISPOSITIONS.md

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `.syzygy/governance/contracts/candidates/pwb-class-granular-extraction-amendment` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `pwb-class-granular-extraction-amendment-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## Consequences recorded with the sign-off

Signing this version moves the PWB `spec.md` again, so it re-stales the
P-95 behaviour-contract re-pin package
(`pwb-behavior-contract-repin-tree-framing`, tracked by `syzygy-fxro` and
`syzygy-2g0d`): it must be redrafted over this sign-off and re-reviewed
before its acts can be offered. The P-95 package is not edited by this
sign-off. The body-read gate does not read the pin, so no Butlers read is
refused; the pins read Unknown until the next re-pin.

It also moves `design.md` and `CAPABILITY-COVERAGE.md`, where the pending
release-label amendment (P-85) adds the same design decision 12 and
capability row 34: under Q5 "First ready lands first" that package is
regenerated over this one's applied bytes, renumbered and reviewed again
before it is offered.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
