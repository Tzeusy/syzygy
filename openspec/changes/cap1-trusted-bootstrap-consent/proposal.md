# CAP1 consent without a mandatory audit service

> **Candidate — binds nothing.** Candidate proposal, non-effective. Owner
> direction authorizes drafting and independent review only. Adoption and
> implementation require later decisions.

## Why

[Observed] The August 24 runtime-hardening plan requires independently correlated
consent and the owner selected Choice C to avoid adding provider infrastructure.
The September 1 general trusted-bootstrap transaction amended RFC3-16 to admit
explicit owner-trusted state (1), but changed CAP1 coverage only. The adopted
coverage file still marks valid-state admission and other invalid-act cases
Unknown. The September 14 owner choice authorizes this candidate route, not a
consent grant or permission to execute it.

[Inferred] CAP1 can support the owner's explicit, scoped consent without an audit
service while stating honestly that it cannot independently verify attendance.
The practical cost is trust in the owner's recorded tree: hashes detect changed
bytes, not forgeries. A forged owner record is never authorized by this proposal.

## What Changes

Propose full replacements of CAP1-REQ-011 and the consent-specific addition to
CAP1-REQ-046. The other requirement bodies remain the adopted predecessors.
The first defines admission/refusal before dependent content reads; the second
makes exact provenance and refusal visible through existing human/machine facts.
A valid correlated state (2) remains supported by the domain contract; building
its provider is outside this slice. Failed correlation cannot become bootstrap.

The spec file contains full proposed replacements. PREDECESSOR-REQUIREMENTS.md
contains the exact old requirements for comparison. This is a normative behavior
and security/data-contract amendment, not an editorial correction.

## Capabilities

### Modified Capabilities

- `project-registration-and-honest-shape-visibility`: observation-consent admission
  and consent provenance disclosure only, preserving existing stable IDs.

## Impact

The candidate design supersedes only the provider-mandatory consent limb of the
August 23 design and August 24 plan if adopted later. Existing snapshot, coverage,
discoverability and parity work consumes one closed consent result; there is no
parallel implementation backlog. APPLYING.md gives exact downstream gates.

Adopted specifications, accepted contracts, historical plans, act records,
performed manifests and raw reviews remain unchanged. No current state or generated
authority view is updated in anticipation of adoption. Candidate applicability
and consequence mapping are recorded in APPLYING.md and CONTRACT-COVERAGE.md;
CAPABILITY-COVERAGE.md supplies the scoped obligation partition and
GOVERNING-DEPENDENCIES.json derives the full composed requirement-warrant union; it does not declare full CAP1 coverage repaired.

## Non-goals

No implementation, provider or ceremony service, owner-held keys, credentials,
new retention system, real-project observation, provider egress, runtime operation,
production deployment, release, policy adoption, or general authority-input system.
No changes to the walkthrough, Polaris generator, terminal PR review stops,
launch-gate policy or deferred Mission/Context work. No automatic conversion of
existing records to trusted bootstrap or weakening of secret screening.

## Owner review outcome

[Unknown] Final specification sign-off and bounded implementation authorization
are not present. This candidate leaves the operational Choice C hold in place.
The next reviewable owner action is adoption of exact reviewed candidate bytes;
implementation is a distinct subsequent authorization, not implied adoption.
