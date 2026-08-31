# Owner direction — general trusted-bootstrap authorization

Date: 2026-08-31

Owner: Tzeusy

Decision ID: `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-DIR-2026-08-31`

The owner responded to the prior read-only boundary:

> “`generalize that relaxation to writes, egress, execution, deployment, or
> autonomous effects without another explicit decision.` please generalize it”

## Direction

Independent external correlation remains a trust principle and the only basis
for calling an owner act **Syzygy-verified**. It is not a systemic prerequisite
for an exact, digest-bound owner bootstrap act to take effect.

An `owner-adopted (bootstrap, uncorrelated)` act may authorize every effect
class that already has an explicit owner gate, including:

- repository observation and writes;
- external egress and model-provider disclosure;
- observed-code execution under an approved execution profile;
- deployment, release and recovery effects;
- autonomy envelopes, missions and their bounded adapter effects; and
- approvals, adjudications, dismissals and other owner decisions.

The act remains visibly uncorrelated. Human and machine surfaces may say it is
owner-trusted; they may not say it is independently verified. A later A1
correlation upgrades provenance confidence through a new evaluation but is not
what makes the owner act effective.

## Existing gates remain

This direction changes the provenance requirement, not the effect-specific
authorization contract. Every effect still requires its existing exact act,
scope and safety checks:

- observation/write consent remains per repository;
- egress consent remains per project/provider and content-class set;
- execution still requires the exact approved profile, isolation, resource,
  credential and network boundaries;
- writes remain attributed, atomic and individually revertable;
- deployment/release still requires its own explicit owner authorization and
  recovery contract;
- autonomy remains inside the exact owner-approved mission/envelope and may not
  widen itself; and
- authentication, SEC-5 secret exclusion, Unknown handling, provenance,
  deterministic evidence and human/machine parity remain binding.

Machines and agents do not become owners. They may not mint, impersonate,
self-approve, silently widen, rewrite or revoke owner acts. A missing,
mismatched, stale, expired, superseded, revoked, unattributed or wrong-scope act
still authorizes nothing.

This direction does not itself deploy, release, write, egress, execute or start
an autonomous effect. It changes what provenance state may satisfy a later
effect-specific owner gate.

## Accepted risk

The owner accepts that same-tree bootstrap records are trust assertions rather
than independently unforgeable proof. Exact digests detect drift relative to
the trusted record; they do not prove who wrote it. Any false fact, secret
exposure, unauthorized scope widening or misrepresented provenance remains a
trust-floor violation.

## Supersession

This direction supersedes the read-only-only boundary in
`POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md` before its candidate
transaction was signed. The retired transaction manifest
`1b0424ab27e0fedbcb13653796f8a55101761438a8b79f0c9be46d2ba814696a`
and its owner phrase sign nothing.

This decision authorizes a fresh generalized semantic delta and review. It does
not edit accepted RFCs or signed specs. Those exact bytes require a new owner
sign-off transaction before implementation or any effect relies on the
generalized rule.
