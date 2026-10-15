# PWB opening-index amendment — version-tagged sign-off v1.0

Date: 2026-10-15

Owner: Tzeusy

Package: pwb-opening-index-amendment

Version: 1.0

Tag: pwb-opening-index-amendment-v1.0

Kind: behavior amendment

Owner selection: P-98: Q1 "Sign v1.0" (by version tag under Scope A; carried to the version regenerated over P-99 by the cycle-3 answer "Carry if review clears"; the 4 notes carried in the separate notes record ROUND-5-DISPOSITIONS.md); Q2 "Walkthrough identities"; Q3 "Words visible on arrival"; Q4 "Human surface only"; Q5 "Existing roles" (confirming both readings); Q6 "Leave for now"; Q7 "Covered by syzygy-k0np"; Q8 "Names from the table"; Q9 "Keep name and place"; Q10 "The opening window"; Q11 "Step outward"; Q12 "Disclose it, as now"

Review: docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-5-RAW.md

Reviewed commit: eda0e345b032ef279d0db231a983f1d963fe9c8f

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: .syzygy/governance/contracts/candidates/pwb-opening-index-amendment/ROUND-5-DISPOSITIONS.md

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `pwb-opening-index-amendment-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## Consequences recorded with the sign-off

Q1 "Sign v1.0" was answered on 2026-10-15 for the version round 4
cleared. The owner's cycle-3 answer "Carry if review clears"
(`decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`) carries
it to the version regenerated over the P-99 sign-off, on two
conditions, each verified before recording: the round-5 review named
above is notes-only, and `proposed/spec.md.patch` is byte-identical to
the version round 4 read.

Signing this version moves the PWB `spec.md` again, so it re-stales the
P-95 behaviour-contract re-pin package
(`pwb-behavior-contract-repin-tree-framing`, tracked by `syzygy-fxro` and
`syzygy-2g0d`): it must be redrafted over this sign-off and re-reviewed
before its acts can be offered. The P-95 package is not edited by this
sign-off. The body-read gate does not read the pin, so no Butlers read is
refused; the pins read Unknown until the next re-pin.

It also moves `spec.md` and `GOVERNING-DEPENDENCIES.md` under the
pending release-label amendment (P-85), which is regenerated over this
sign-off's applied bytes and reviewed again before it is offered.
Implementation is covered on landing by
`decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`
(bead `syzygy-u05.23`, gate `syzygy-00ls`); this record authorizes
nothing itself.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
