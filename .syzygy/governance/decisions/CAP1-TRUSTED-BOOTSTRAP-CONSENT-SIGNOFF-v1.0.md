# CAP1 trusted-bootstrap consent amendment — version-tagged sign-off v1.0

Date: 2026-10-15

Owner: Tzeusy

Package: cap1-trusted-bootstrap-consent

Version: 1.0

Tag: cap1-trusted-bootstrap-consent-v1.0

Kind: specification adoption

Owner selection: Selected "Adopt P-109 v1.0" (Recommended. Scope A tag cap1-trusted-bootstrap-consent-v1.0; replaces CAP1-REQ-011 and 046.) in the multi-select question "Which cleared packets do you sign or adopt now?"

Review: docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4-RAW.md

Reviewed commit: 591950c76805f34886e7052adb9753c58b5ef737

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4-DISPOSITION.md

Scope A extension: `.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2026-10-15.md` extends the direction below to this package's kind

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `openspec/changes/cap1-trusted-bootstrap-consent` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `cap1-trusted-bootstrap-consent-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## Consequences recorded with the sign-off

Adopted as the full replacement of CAP1-REQ-011 and CAP1-REQ-046. The
bound Capability 1 change is not edited: the effective specification is
the composition the change's `GOVERNING-DEPENDENCIES.json` declares, and
the change's generated `ADOPTION.md` supersedes, in place, every
predecessor coverage surface round-4 note 1 names (the RFC3-16(a) row,
the Part A totals, the family table, the 38-mapped and 286-unmapped
sentences, the Part B RFC3 line and total, the self-check, and the
generated `GOVERNING-DEPENDENCIES.md`).

Round-4 note 2 stays a known gap: CAP1-REQ-046's refusal disclosure does
not on its own require the refused artifact's identity (bead
`syzygy-0v4l`, a v1.1). Implementation is authorized separately, bounded,
by `decisions/OWNER-DIRECTION-CAP1-CONSENT-IMPLEMENTATION-2026-10-15.md`;
this record authorizes nothing itself.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
