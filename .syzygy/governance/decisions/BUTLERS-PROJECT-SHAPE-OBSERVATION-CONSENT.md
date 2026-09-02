# Butlers project-shape observation consent

Date: 2026-08-31

Owner: Tzeusy

Record ID: `PWB-CONSENT-2026-08-31`

Record version: `1.0.0-candidate.3`

Consent class: observation

Observation content class: `declared-project-shape-text`

Subject: `(project:syzygy, repository:butlers-configured-poc)`

Current locator: `/home/tze/GitHub/butlers` (configuration, not repository
identity)

Status: **candidate, act-ready; no effect until the owner acts on this exact
digest** (self-declared stamp; effective status comes only from an owner-act
record, RFC3-16)

Statement date: 2026-08-31; the future act records its exact grant instant

Proposed revocation state: active; supersedes no earlier consent

The owner stated in this Codex project walkthrough:

> “you have consent for butlers observation; obviously don't read secrets
> from butler”

## Scope

The consent scope is the bounded, read-only project-shape observation defined
by `polaris-project-wide-butlers-model` as signed on 2026-09-02: specification
digest `2e453a6ec6dbc19c5df226650c6e7a94c46e81f65d9d180f57d1dc1dce7fd07e`, one of the
eleven artifacts bound by the act recorded at
`.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md`.
It covers exact Git objects selected by that specification's closed source
population at each identified Butlers revision observed by the POC.

The scope excludes:

- PostgreSQL, credential-store, secret API or runtime-service access;
- `.env` or other credential-file access;
- arbitrary implementation-file body reads;
- working-tree traversal, observed-code execution or network egress;
- write to Butlers; or
- second repository.

The grant has no silent expiry. The owner may narrow or revoke it through a
later recorded act; revocation does not erase prior observation records.

## Provenance state and effect

[Observed] This candidate preserves the owner phrase, attribution, date,
subject and scope. It has no effect until the owner acts on its exact digest.
The act it is prepared for is one of the three separate effect-specific acts
required by PWB-REQ-005 and PWB task 1.7; the other two (the secret policy and
the observer registry entry) are separate artifacts with separate acts, and a
body read requires all three to be valid.

If acted on, its provenance state is **owner-adopted (bootstrap,
uncorrelated)** — state (1) under RFC3-16(c) — only if the human act explicitly
selects state (1) and records the A1 audit-record identity as absent. That
state authorizes only this read-only observation scope, must remain visible as
uncorrelated, and is never “independently verified.” A later A1 correlation
may upgrade the provenance state without editing this artifact. The act is a
warrant to observe within this scope; it is never evidence that any read
occurred, that screening succeeded, or that any derived claim is true.

No future act over this candidate retroactively authorizes the body reads in
`docs/reviews/R-POLARIS-PRECONDITION-READ-BOUNDARY-INCIDENT.md`.
