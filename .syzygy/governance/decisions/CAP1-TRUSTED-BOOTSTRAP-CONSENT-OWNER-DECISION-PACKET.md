# Owner decision packet — CAP1 trusted-bootstrap consent amendment

> **Candidate — binds nothing.** Nothing here is signed, adopted, authorized
> or labelled accepted. This packet puts one binding ask to the owner, in
> three questions; only the owner's answer binds anything (VIS-4). Register
> row: P-110. Bead: `syzygy-u2a.1`.

**Status:** drafted 2026-09-14 under the owner's choice of that day
(CAP1-CONSENT option A: prepare the bounded trusted-bootstrap amendment and
obtain independent review; recorded in the notes of `syzygy-u2a.1`). Reviews
1 and 2 ran over the 2026-09-14 bytes: review 1 `REVISE`, repaired; review 2
`PASS` / `PASS`, CC-SPEC-11 `CONFIRMED`
(`docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2-RAW.md` lines 1–3). The
candidate was never committed until 2026-10-15, when it was rebased onto main
(two protected predecessors had moved under the 2026-09-29 Capability 1
readability successor; no requirement changed). Rebasing retired review 2
for the changed bytes. **Review 3 over the rebased bytes: pending.**

## The one binding ask

Adopt the candidate `openspec/changes/cap1-trusted-bootstrap-consent/` at an
exact version, **v1.0**, the bytes review 3 reads, as the successor to two
adopted Capability 1 requirements; and, separately, decide whether to
authorize implementing it. Adoption alone starts no implementation.

## What you would be adopting

Full replacements of **CAP1-REQ-011** (consent is a recorded fact) and
**CAP1-REQ-046** (owning authority and effective status). Every other
Capability 1 requirement stays as adopted. In short:

- **Bootstrap consent without an audit service.** A consent act you perform
  that explicitly selects RFC3-16(a) state (1), with all nine RFC3-16(b)
  bindings and the audit identity explicitly absent, admits observation of
  exactly that project and repository. State (2), independently correlated,
  stays supported; building its provider is out of scope.
- **Fail closed.** Every invalid act state (missing, malformed, digest or
  scope mismatch, future-dated, stale, expired, superseded, revoked, known
  non-human) refuses the dependent read, renders authorization Unknown and
  routes the contradiction to you. Failed correlation never falls back to
  bootstrap. Valid withdrawal defeats a grant.
- **Honest provenance in both channels.** The human and machine answers show
  "owner-adopted (bootstrap, uncorrelated)" or "Syzygy-verified", the exact
  act and artifact, and never infer that an authorized effect succeeded.

**What it costs.** [Inferred] Bootstrap rests on trust in your recorded tree:
hashes detect changed bytes, not forgeries. A forged owner record stays
unauthorized, but CAP1 cannot detect one that is byte-identical. This is the
trade-off RFC3-16(a) already accepts; the candidate states it rather than
claiming attendance verification.

## Question 1 — adopt v1.0?

| Option | Meaning |
|---|---|
| **Adopt v1.0** (recommended once review 3 clears) | The adoption change installs the two replacements and the candidate coverage and dependency consequences in one transaction (CC-REV-2); the predecessor files and acts stay as history. |
| Decline | CAP1-REQ-011 and 046 stay as adopted; the Choice C fail-closed hold stays; `syzygy-u2a.1` stays blocked. |
| Revise | Name what to change; a new version gets a new review round. |

## Question 2 — by which route?

The 2026-10-02 Scope A direction names the PWB specification deltas, the
observer registry entry and the queued contract successors; its 2026-10-14
extension covers Three-Surface POC amendments and says it does not reach the
Capability 1 specification. So this amendment has no version-tag route yet.

| Option | Meaning |
|---|---|
| **Extend Scope A to this package alone** (recommended) | A plain direction; you sign by selecting "Adopt v1.0", bound by the tag `cap1-trusted-bootstrap-consent-v1.0` on the reviewed commit and recorded with `scripts/record_versioned_signoff.py`. |
| Phrase and digest | A dedicated recorder is written first, and you type a phrase naming a manifest digest, as the 2026-09-29 readability successor was signed. |

## Question 3 — authorize implementation?

The 2026-08-21 Capability 1 implementation authorization escalates any
specification amendment and any change to security posture or a normative
data contract to a new owner act, so adopting v1.0 does not let anyone build
it.

| Option | Meaning |
|---|---|
| **Authorize the bounded consent slice** (recommended, after Q1) | Implementation of the amended CAP1-REQ-011/046 only, through the existing held tasks (`syzygy-u2a.2`, then `.6`–`.9`), with the exact record encoding and interface reviewed before code. No provider, credential, retention store, real-project read, egress, deployment or release. |
| Not yet | Adopted intent with no implementation; the operational hold stays. |

## What none of this does

No consent grant for any repository, no reading of any target repository, no
audit or ceremony service, no change to doctrine, accepted contracts or craft
policy, and no edit to any act-bound byte.
