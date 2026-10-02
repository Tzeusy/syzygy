# Public-target egress consent — Anthropic (Claude API)

> Instance filled from `../../templates/EGRESS-CONSENT-TEMPLATE.md` by
> `scripts/build_public_repo_admission.py`. Candidate — binds nothing
> until the owner acts on this record's exact bytes.

Date: 2026-10-03 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `PUBLIC-EGRESS-anthropic`

Record version: `0.1.0-candidate.4`

Consent class: egress — one record per (project, provider) pair (RFC5-12)

Subject: `(project:syzygy, provider:anthropic)`

Provider and route: Anthropic (Claude API), reached only through the registered provider
execution route (REQ-polaris-generation-017) and the single egress check
(RFC5-15). The model is recorded per run, not fixed here.

Permitted content classes (RFC5-14 closed vocabulary):

- `governance-text`
- `code-structure`
- `code-content`
- `evidence-content`
- `derived-composites`

Retention: provider requests, provider replies and run records are retained in a run directory under `project:syzygy`'s state directory, outside git. Requests and replies contain the source spans sent, so the run directory holds those spans for as long as the run is retained; nothing is retained in git, logs or machine responses. The provider's own retention is as its API terms state, disclosed rather than promised.

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier consent

## Scope

Only content read under an in-force observation consent for one of these
`(project:syzygy, repository)` pairs:

- `(project:syzygy, repository:psf-requests)`

together with the generator's own instruction text (its stage prompts and
response schemas, authored in Syzygy's repository), which every request
carries. Every other source of `project:syzygy` content is outside this
consent, including the Butlers repository, the rest of Syzygy's own
repository and any work history, and stays unsent.

## Conditions

- Only content screened under `project:syzygy`'s effective public-source
  screening scope may be sent. Excluded or unclassifiable content is never
  sent (RFC5-14, RFC5-16).
- A composite's class is computed from what it embeds; one whose class cannot
  be determined is refused and the refusal shown (RFC5-14).
- Every transmission passes the single egress check and emits an audit record
  (RFC5-15).
- This record's own condition: provider output is generated editorial draft.
  It is never recorded as an Observed claim, as adopted intent, or as the
  target project's own statement.

## Effect

Without an effective owner act over this record's exact bytes, no content
reaches this provider, and the generated draft layer renders Unknown
(`unconsented-source-or-provider`) (REQ-polaris-generation-001). Revocation
is prospective (RFC5-13).
