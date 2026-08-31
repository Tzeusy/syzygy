# Butlers project-shape observation consent

Date: 2026-08-31

Owner: Tzeusy

Record ID: `PWB-CONSENT-2026-08-31`

Record version: `1.0.0-draft.1`

Consent class: observation

Subject: `(project:syzygy, repository:butlers-configured-poc)`

Current locator: `/home/tze/GitHub/butlers` (configuration, not repository
identity)

Status: **draft transcription of an owner consent statement; no machine effect**

Statement date: 2026-08-31; exact statement instant: Unknown

Proposed revocation state: active; supersedes no earlier consent

The owner stated in this Codex project walkthrough:

> “you have consent for butlers observation; obviously don't read secrets
> from butler”

## Scope

The proposed consent scope is the bounded, read-only project-shape observation defined
by `polaris-project-wide-butlers-model` at signed specification digest
`07392c115e3a63bb3aceb259362a70e0d1ee11d6ba2621492fd03cf1893aca61`.
It covers exact Git objects selected by that specification's closed source
population at one configured Butlers revision.

The proposed scope excludes:

- PostgreSQL, credential-store, secret API or runtime-service access;
- `.env` or other credential-file access;
- arbitrary implementation-file body reads;
- working-tree traversal, observed-code execution or network egress;
- write to Butlers; or
- second repository.

The grant has no silent expiry. The owner may narrow or revoke it through a
later recorded act; revocation does not erase prior observation records.

## Provenance state and effect

[Observed] This draft preserves the owner phrase, attribution, date, subject
and scope. It does not yet carry the exact final artifact digest and commit/tag
binding required for an RFC3-16(c) owner-adopted bootstrap act. [Unknown] No
independently kept RFC5-25 audit-record identity is available to correlate an
act through the RFC3-16(a) A1 mechanism.

Accordingly, this records the owner's consent statement for preparation of an
exact act, but is neither an owner-adopted bootstrap act nor a Syzygy-verified
effective act. It does not satisfy PWB-REQ-005's independently verifiable
provenance gate, authorizes no POC or Syzygy project-shape body read, and does
not retroactively authorize any prior read.
