# D9 for operator-agent runs — exact-bytes record

> Instance filled from `../../templates/D9-IN-FORCE-RECORD-TEMPLATE.md` by
> `scripts/build_dossier_local_agent_acts.py`. Candidate — binds nothing
> until the owner acts on this record's exact bytes.

Date: 2026-10-06 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `D9-IN-FORCE-OPERATOR-AGENT`

Record version: `0.1.0-candidate.1`

Record class: in-force record for adopted doctrine (RFC3-16(a); the review
note R3-F8 of the local-agent mode)

Subject: doctrine amendment D9 — SEC-3 in `security.md` and the observed-code
bullet of `v1.md` as D9 left them

Adoption: by the owner's own words on 2026-10-06, logged as row D9 of `.syzygy/governance/decisions/DOCTRINE-AMENDMENT-LOG.md`; that adoption binds no digest, which is why this record exists

Bound files (whole-file SHA-256 of each, computed when this record was
generated):

| File | SHA-256 |
|---|---|
| `.syzygy/governance/doctrine/security.md` | `766c953d01d1a7bba3319b538a35851c88b9901d8fe79399af0f23ec3011bc00` |
| `.syzygy/governance/doctrine/v1.md` | `88675bc7aa12a3cdc61b930a748e2a24038db0345dff54f4772bc6e8922fc6ca` |

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier record

## What it decides

D9 is adopted doctrine; this record does not adopt it again and changes no
doctrine byte. It gives the adoption the form RFC3-16(a) checks: an owner act
bound to exact bytes and a stated scope. REQ-polaris-generation-033 lets an
authoring brief permit the owner's attended agent session to build and run
the observed project only while D9 is in force, and the review note R3-F8
requires that to be established by the act cross-check, never by a status
word or a file's presence.

Scope: Syzygy may treat D9 as in force for REQ-polaris-generation-033's
execution rule while both files hash to the digests above. For any other
bytes, or with this record withdrawn, D9 is not established for that rule
and every brief carries SEC-3's rule that observed-project code runs only
inside an explicit, opt-in execution profile.

## What it does not do

It permits no execution by itself: a permitting brief also needs the owner's
choice recorded for that one run, the attended-session conditions and the
credential check that REQ-polaris-generation-033 states. It extends D9 to no
other feature, and it does not establish any other doctrine rule.

## Cost

The digests are of whole files. Any later edit to `security.md` or `v1.md`,
even one unrelated to SEC-3, leaves D9 unestablished for operator-agent runs
until a new version of this record is generated from the new bytes and acted
on. The failure is closed: briefs fall back to SEC-3's profile rule.

## Withdrawal

Withdrawal is a later owner act naming this record; it is prospective.
