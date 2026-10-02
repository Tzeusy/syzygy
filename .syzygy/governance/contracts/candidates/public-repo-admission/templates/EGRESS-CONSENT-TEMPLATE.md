# Public-target egress consent — {{PROVIDER}}

> Template. Replace every `{{…}}` field; a filled record with any `{{` left is
> invalid. Candidate — binds nothing until the owner acts on the filled record.
> One record exists per (project, provider) pair; admitting or withdrawing a
> target is a new version of it.

Date: {{DRAFT_DATE}} (drafted); the act, if performed, records its own instant

Owner: {{OWNER}}

Record ID: `PUBLIC-EGRESS-{{PROVIDER_ID}}`

Record version: `{{VERSION}}`

Consent class: egress — one record per (project, provider) pair (RFC5-12)

Subject: `(project:syzygy, provider:{{PROVIDER_ID}})`

Provider and route: {{PROVIDER}}, reached only through the registered provider
execution route (REQ-polaris-generation-017) and the single egress check
(RFC5-15). The model is recorded per run, not fixed here.

Permitted content classes (RFC5-14 closed vocabulary):

{{CONTENT_CLASSES}}

Retention: {{RETENTION}}

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; {{SUPERSEDES}}

## Scope

Only content read under an in-force observation consent for one of these
`(project:syzygy, repository)` pairs:

{{ADMITTED_REPOSITORIES}}

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
