# Butlers project-shape observation consent

Date: 2026-08-31

Owner: Tzeusy

Record ID: `PWB-CONSENT-2026-08-31`

Record version: `1.0.0`

Consent class: observation

Subject: `(project:syzygy, repository:butlers-configured-poc)`

Current locator: `/home/tze/GitHub/butlers` (configuration, not repository
identity)

Status: **candidate awaiting an exact digest-bound owner consent act**

Statement date: 2026-08-31; the future act records its exact grant instant

Proposed revocation state: active; supersedes no earlier consent

The owner stated in this Codex project walkthrough:

> “you have consent for butlers observation; obviously don't read secrets
> from butler”

## Scope

The consent scope is the bounded, read-only project-shape observation defined
by `polaris-project-wide-butlers-model` at signed specification digest
`cf6e1378bcfa2d3439001b9d9bb47d590c2e0aa481630a0f2ddc2845fb1f22d8`.
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

If acted on, its initial provenance state is **owner-adopted (bootstrap,
uncorrelated)**. Under the proposed trusted-bootstrap observation amendment,
that state may authorize only this read-only observation scope and must remain
visible as uncorrelated; it is never “independently verified.” A later A1
correlation may upgrade the provenance state without editing this artifact.

No future act over this candidate retroactively authorizes the body reads in
`docs/reviews/R-POLARIS-PRECONDITION-READ-BOUNDARY-INCIDENT.md`.
