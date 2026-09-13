# Bounded authority staging and effect-host confirmation

Verdict: AR-1 CONFIRMED; AR-3 PARTIALLY CONFIRMED, ONE NARROW FINDING REMAINS.

This is a design/specification confirmation, not implementation evidence, an
owner act, N/A judgment, full contract review or generator completion.
AR-2 is outside this confirmation and remains separately reviewed.

## AR-1 disposition

CONFIRMED. EXECUTION-PHASES.md names fixture-only mechanics, full effect/owner
integration and real-project quality proof separately. Its Phase B consumer list
identifies the drafting-work drawer, Trajectory rows, work filters/counts/exports
and machine answers. Requirement 028 and WORK-STATE-CONTRACT.md now preserve
those integration obligations rather than treating stage receipts as work state.
An existing effective bound cannot be discarded or replaced. A selected profile
whose required normalized case has no accepted predicate refuses admission before
materialization/dispatch; another profile requires explicit owner choice.

This is a valid proposed refusal/staging boundary, not implementation of the
unsupported case. It neither changes RFC8-13's predicate nor proves universal
work-state conformance. All three phases and applicable requirements remain
mandatory for whole-goal completion. No-signal amendment need not gate unrelated
pure source/bundle/render mechanics, subject to actual implementation approval.

## AR-3 disposition

The recorder design now names a separate OS principal, supervisor-owned code,
protected journal/key, constrained Unix socket with peer identity, idempotent
append receipts and explicit restart/outage behavior. The two added requirement
022 scenarios test excluded-actor forgery/replacement and unavailable trusted
recovery. Real-principal denial evidence is required; same-user mocks cannot
certify the boundary. This resolves the missing concrete recorder arrangement.

One narrow authority ambiguity remains in EFFECT-HOST-DESIGN.md: the browser
pairing grant is “prepared by an already authenticated owner CLI,” but this
paragraph does not explicitly require fresh owner attendance on a trusted channel.
An authenticated CLI is a machine client, not proof that a human attended.
RFC5-4 requires browser sessions to be minted only through an owner-attended act
on a trusted channel; RFC5-5/6 also preserve attended bootstrap.

Repair: require the trusted pairing operation to verify owner attendance before
issuing its one-use browser grant, explicitly prohibit machine authentication
alone from minting that grant/session, and add a negative test that an unattended
but authenticated CLI cannot issue or redeem its way into a browser session.
Do not introduce a new approval for each editorial pass. The existing secret-free,
origin-bound, scoped, expiring single-use grant design can remain.

After that narrow repair, AR-3 can be confirmed as a design choice; actual host
provisioning, protection tests and effect permission remain later obligations.

## Frozen subjects

- openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md: 8e3e2c4494df964addb76a885a5b349051f5a0a543346ff4dc15f7c1598b1245
- openspec/changes/polaris-manifesto-generation/EFFECT-HOST-DESIGN.md: 8247447be519f0b9a9766c71b3fff96857817ce713b6e4f97846e6dd4d4141b9
- openspec/changes/polaris-manifesto-generation/WORK-STATE-CONTRACT.md: b86d0b944c395bbe66c4363d34be54531c55b6f72e76862626946851e199a986
- openspec/changes/polaris-manifesto-generation/tasks.md: d781a1b45fc0e4d216537f40a9e519d41df94eaf1ff252f3484c5f7fd5f794f6
- openspec/changes/polaris-manifesto-generation/CAPABILITY-COVERAGE.md: 4589e9ee4a5303fdc25d216a0a63e6d732c1185b5a1eb8bb23c7f1b8199b39e0
- openspec/changes/polaris-manifesto-generation/SECURITY-CONTRACT.md: c6f2703a92a33d31fa5f0644cb4ce669048187d6aa72ce61a4c3aee90bdad6b5
- openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md: a3ba2fb3c3019045d53a107791843082bdfe4aa9681e046ca2b9db1e09b25820
