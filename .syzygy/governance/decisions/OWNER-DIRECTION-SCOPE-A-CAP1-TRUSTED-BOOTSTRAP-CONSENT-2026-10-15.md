# Owner direction — Scope A extended to the CAP1 trusted-bootstrap consent amendment alone

Date: 2026-10-15

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-SCOPE-A-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2026-10-15`

Extends: `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` (this
directory). Neither that direction nor
`OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md` is edited.

This is a plain owner direction in the shape of
`OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`. It binds no
artifact digest, adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers
nothing in `scripts/check_governance.py`. It adopts nothing by itself.

## The owner's words

[Observed: the question and selection as the lead Claude Code session
relayed them to this lane; the owner's answer itself is in that session,
not in this repository.] On 2026-10-15, in the lead Claude Code session, the
owner answered one multi-select structured question. Its text:

> Which cleared packets do you sign or adopt now? (Unticked items wait.) P-108: POC vocabulary/epistemic amendment v1.0. Review note 13: if no rendering is marked, its checks pass on zero; I'd file a follow-up so zero reads Unknown. P-109: CAP1 trusted-bootstrap consent v1.0, replacing CAP1-REQ-011/046, signed by version tag (this extends Scope A to this one package). Coverage tables get superseded at adoption. P-112: the dov.24 loaded-profile act; its packet recommends WAITING for slice 5 limbs 1–4, and it would bring in a pin that's four sign-offs stale.

The option this record carries, as shown:

> Adopt P-109 v1.0 — Recommended. Scope A tag cap1-trusted-bootstrap-consent-v1.0; replaces CAP1-REQ-011 and 046.

The owner selected "Sign P-108 v1.0", "Adopt P-109 v1.0" and "Authorize
P-109 impl". "Perform P-112 now" was not selected, so P-112 waits.

The question said "signed by version tag (this extends Scope A to this one
package)". That is the packet's recommended arm of P-109 Question 2,
"Extend Scope A to this package alone", and this record carries that
reading and no wider one.

## The direction

1. **Route.** The Capability 1 amendment
   `openspec/changes/cap1-trusted-bootstrap-consent/` (register row P-109)
   may be adopted by version tag under Scope A, as the PWB specification
   deltas are signed: the owner's selection of an option naming the package
   and a `major.minor` version is the adoption, bound by the annotated tag
   `cap1-trusted-bootstrap-consent-v<major>.<minor>`. No typed phrase and no
   digest argument is required. The selection above names v1.0.
2. **Everything else in Scope A stands.** A version is offered only after a
   fresh-context round returns CONFIRM, or CONFIRM WITH EXCEPTIONS with
   notes only; the mechanical checks stay; VIS-4 holds.
3. **How `syzygy-u2a.1` criterion 3 is read.** That criterion asks for an
   "exact-digest specification/applicability adoption". Under this route the
   exact binding is the tagged commit, which carries the reviewed bytes and
   the applied result, as the packet's Question 2 states.

## Bounds

- **This one package.** It does not reach any other Capability 1 change,
  the adopted Capability 1 specification's own bytes, doctrine, accepted
  contracts, craft policy or registry entries. The 2026-10-14 POC extension
  excluded "the Capability 1 specification"; this record is the only
  extension reaching CAP1, and only for this package.
- **Route only.** It authorizes no implementation. Implementation is
  authorized separately by
  `OWNER-DIRECTION-CAP1-CONSENT-IMPLEMENTATION-2026-10-15.md` (this
  directory).
- **Withdrawal.** A later direction may narrow or withdraw this one;
  withdrawal defeats grant.

## What the tooling needed

`scripts/record_versioned_signoff.py` names this record as the `extension`
of the `cap1-trusted-bootstrap-consent` package: the dedicated record
carries a `Scope A extension:` line naming it, the aggregate block's
Direction row names it, and recording or `--check` refuses when this file
is missing. No check, act phrase or `ACT_DIGEST_COPY_FILES` row is added.
