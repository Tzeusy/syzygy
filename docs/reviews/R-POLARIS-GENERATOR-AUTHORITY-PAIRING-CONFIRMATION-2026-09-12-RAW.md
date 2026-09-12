# Bounded pairing and authority staging repair confirmation

Verdict: CONFIRMED for the remaining AR-3 pairing finding. AR-1 remains
CONFIRMED as a phase/refusal design disposition.

This confirmation covers the exact subjects below and only the prior pairing
finding plus the clarified next-run refusal wording. It is not specification
adoption, implementation authorization, effect consent, an N/A judgment, a
full-security audit or evidence of working runtime behavior. AR-2 remains outside
this confirmation.

EFFECT-HOST-DESIGN.md now separates authenticated machine preparation from fresh
owner-attended confirmation on the trusted supervisor interface. Generator append
operations cannot create attendance or privileged recovery record classes.
Caller flags, ordinary machine credentials, TTY presence and mutable files cannot
supply proof. A host lacking the trusted attended path refuses pairing. The
exact request binds origin, scope, nonce/challenge and expiry; grant redemption
is one-use. The resulting session remains credential-identified, not device- or
network-bound, with lifetime and revocation preserved. This closes the ambiguity
against RFC5-4 and the existing bootstrap/issuance boundaries.

Requirement 021's new scenario explicitly refuses issuance for an authenticated
machine caller without the exact fresh attendance proof. Host verification now
requires the corresponding unattended issuance/replay negative case. These are
meaningful implementation acceptance obligations, not claims they already pass.

Requirement 028 now clearly applies unsupported-profile refusal to the next
requested live run, avoiding an implication that already captured provider
receipts could retroactively prevent a prior dispatch. The accepted work-state
predicate is not amended. Historical receipts, unsupported-case disclosure,
explicit profile choice and mandatory later owner-flow/real-project stages remain.

No additional blocker is identified within this bounded repair scope. Exact
trusted-interface implementation, actor-isolation tests, real browser behavior
and effective owner/project/provider permissions remain future evidence.

## Frozen subjects

- openspec/changes/polaris-manifesto-generation/EFFECT-HOST-DESIGN.md: ccda79b1094edd2e10024a124c73690cf9a8e27d05621ca734da76314a5744d7
- openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md: 8e3e2c4494df964addb76a885a5b349051f5a0a543346ff4dc15f7c1598b1245
- openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md: c3012b0c4103276f6b3a3ddcb93406008bb5ed6b73c23c2bc2aed4485785b5c0
