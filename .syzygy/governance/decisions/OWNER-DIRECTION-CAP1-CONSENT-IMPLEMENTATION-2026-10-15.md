# Owner direction — implementation of the CAP1 trusted-bootstrap consent amendment v1.0

Date: 2026-10-15

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-CAP1-CONSENT-IMPLEMENTATION-2026-10-15`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in
the family of `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`
(this directory). It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing in
`scripts/check_governance.py`. It adopts nothing and edits no act-bound
byte.

It answers register row P-109 Question 3. The 2026-08-21 Capability 1
implementation authorization
(`CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`) escalates any
specification amendment and any change to security posture or a normative
data contract to a new owner act. Adopting v1.0 therefore lets no one build
it. This record is that separate act.

## The owner's words

[Observed: the question and selection as the lead Claude Code session
relayed them to this lane; the owner's answer itself is in that session,
not in this repository.] On 2026-10-15, in the lead Claude Code session, the
owner answered one multi-select structured question:

> Which cleared packets do you sign or adopt now? (Unticked items wait.) P-108: POC vocabulary/epistemic amendment v1.0. Review note 13: if no rendering is marked, its checks pass on zero; I'd file a follow-up so zero reads Unknown. P-109: CAP1 trusted-bootstrap consent v1.0, replacing CAP1-REQ-011/046, signed by version tag (this extends Scope A to this one package). Coverage tables get superseded at adoption. P-112: the dov.24 loaded-profile act; its packet recommends WAITING for slice 5 limbs 1–4, and it would bring in a pin that's four sign-offs stale.

The option this record carries, as shown:

> Authorize P-109 impl — Recommended with adoption. Bounded slice u2a.2 then u2a.6–9: no provider, credentials, retention store, real-project read, egress or release.

The owner selected "Sign P-108 v1.0", "Adopt P-109 v1.0" and "Authorize
P-109 impl". The adoption is recorded in
`CAP1-TRUSTED-BOOTSTRAP-CONSENT-SIGNOFF-v1.0.md` (this directory), tag
`cap1-trusted-bootstrap-consent-v1.0`, and its route in
`OWNER-DIRECTION-SCOPE-A-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2026-10-15.md`.

## What is authorized

Implementation of exactly the adopted v1.0 text of CAP1-REQ-011 and
CAP1-REQ-046 (the composition `openspec/changes/cap1-trusted-bootstrap-consent/`
declares), through the existing serialized Capability 1 hardening tasks, in
this order:

| Order | Bead | Task |
|---|---|---|
| 1 | `syzygy-u2a.2` | Bind evaluations to authorized captured snapshots (plan Task 1), reconciled to the amended consent decision |
| 2 | `syzygy-u2a.6` | Project and serve reference-bound consent coverage; consumes `.2`'s closed decision, never re-grants |
| 3 | `syzygy-u2a.7` | Serve evidence-backed repository discoverability; consumes the same decision |
| 4 | `syzygy-u2a.8` | Reconcile spec to code for the hardening |
| 5 | `syzygy-u2a.9` | Generate the epic report |

The bead dependencies already fix this order; nothing here reorders it.
Each task keeps its other prerequisites and review gates.

## Bounds

- **Exactly the adopted text.** No requirement, scenario or behaviour
  beyond v1.0. The round-4 note 2 gap (CAP1-REQ-046's refusal disclosure
  does not on its own require the refused artifact's identity) is not
  closed by implementation; it needs a v1.1 and its own review and adoption.
- **No provider, credentials, retention store, real-project read, egress
  or release.** No audit or ceremony service, no state-(2) correlation
  provider, no key or credential material, no persistence store for
  retained acts, no read of any real target repository, no provider
  egress, no deployment and no release.
- **Record encoding and interface reviewed before code.** The exact consent
  record encoding and the authority-input interface `syzygy-u2a.2` builds
  on are frozen and independently reviewed before implementation code for
  them lands (`syzygy-u2a.1` acceptance criterion 4).
- **The daemon never executes observed code.** Separate operator commands
  run tests.
- **Reviewed and verified per craft-and-care.** Each lane runs under the
  normal implementation workflow: conformance expected values are literals,
  never imported from the module under test; each falsifier limb has a
  rule-6 mutant that fails; the battery runs at a committed tree in a clone
  (rule 7); and a fresh-context review precedes merge.
- **Escalation.** A lane that finds the adopted text cannot be built as
  written stops and returns to the owner: an amendment travels under
  CC-REV-2 and needs its own adoption. No act-bound byte is edited.
- **Withdrawal.** A later direction may narrow or withdraw this one;
  withdrawal defeats grant.
