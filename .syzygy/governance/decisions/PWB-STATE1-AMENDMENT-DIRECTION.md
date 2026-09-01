# Owner direction — PWB state-(1) amendment profile

Date: 2026-09-02

Owner: Tzeusy

Decision ID: `PWB-STATE1-AMENDMENT-DIR-2026-09-02`

Evidence baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`

## Decision

The owner was presented four amendment profiles for the signed project-wide
Polaris requirements:

- **A:** state (1) or state (2) for both PWB-REQ-005 body-read authority and
  PWB-REQ-022 walkthrough judgment;
- **B:** state (1) or state (2) for PWB-REQ-005 only;
- **C:** state (1) or state (2) for PWB-REQ-022 only; or
- **D:** retain both requirements as state-(2)-only pending A1.

The owner answered:

> **A**

## Direction

Draft and independently review a complete amendment of both PWB-REQ-005 and
PWB-REQ-022 so that a valid human owner act in state (1), `owner-adopted
(bootstrap, uncorrelated)`, or state (2), `Syzygy-verified`, may satisfy each
owner-act provenance gate. Every human and machine rendering must carry the
exact state; only state (2) may be called independently verified. Missing,
invalid, stale, revoked, superseded, wrong-scope, non-human or
digest-mismatched acts continue to fail closed.

The amendment must update each complete requirement block—normative prose,
cases, observables, independent oracles, falsifiers and scenarios—plus every
invalidated proposal, design, coverage, dependency and test obligation in the
same logical change.

## Accepted risk

State-(1) consent, secret-policy, adapter-registry and judgment records remain
same-tree forgeable from Syzygy's perspective. Exact digests detect drift from
the trusted record; they do not independently prove who authored or attended
the act. The remaining scope, read-only/empty-write, secret-screening,
authentication and fail-closed gates remain conjunctive but do not create
independent attendance proof.

The owner accepts that risk for this bounded, local, single-Butlers-repository
POC amendment profile.

## Authorization boundary

This direction authorizes only drafting and independent review of the PWB
amendment and preparation of a later exact-digest owner sign-off packet. It
does not:

- sign or apply amended PWB behavior;
- perform observation consent, secret-policy approval or adapter-registry
  adoption;
- authorize a repository-body read;
- authorize implementation or resume PWB implementation;
- authorize writes, egress, execution, deployment, release, recovery or
  missions; or
- change any transaction-bound contract artifact.

The amended behavioral artifacts remain candidate until a later human owner
signs their exact reviewed digests.

## Adversarial review

The corrected four-option decision received independent `Pass` verdicts for
both problem scope and recommendation at baseline `bef7f8d`. No material
correction remained. The reviewer confirmed that choosing A is authorization
to draft and review only and leaks no downstream operational authority.
