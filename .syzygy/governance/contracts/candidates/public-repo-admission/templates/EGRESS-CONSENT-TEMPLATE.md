# {{TARGET_NAME}} egress consent — {{PROVIDER}}

> Template. Replace every `{{…}}` field; a filled record with any `{{` left is
> invalid. Candidate — binds nothing until the owner acts on the filled record.

Date: {{DRAFT_DATE}} (drafted); the act, if performed, records its own instant

Owner: {{OWNER}}

Record ID: `PUBLIC-EGRESS-{{TARGET_ID}}-{{PROVIDER_ID}}-{{DRAFT_DATE}}`

Record version: `{{VERSION}}`

Consent class: egress — one record per (project, provider) pair (RFC5-12)

Subject: `(project:{{PROJECT_ID}}, provider:{{PROVIDER_ID}})`

Provider and route: {{PROVIDER}}, reached only through the registered provider
execution route (REQ-polaris-generation-017) and the single egress check
(RFC5-15). The model is recorded per run, not fixed here.

Permitted content classes (RFC5-14 closed vocabulary):

{{CONTENT_CLASSES}}

Retention: {{RETENTION}}

Proposed revocation state: active; supersedes no earlier consent

## Conditions

- Only content admitted under this project's in-force observation consent
  and screened under the observing project's effective secret policy may be
  sent. Excluded or unclassifiable content is never sent (RFC5-14, RFC5-16).
- A composite's class is computed from what it embeds; one whose class cannot
  be determined is refused and the refusal shown (RFC5-14).
- Every transmission emits an audit record (RFC5-15, RFC5-25).
- Provider output is editorial inference: it never becomes an Observed claim,
  adopted intent or the target project's own statement
  (REQ-polaris-generation-010).

## Effect

Without an effective owner act over this record's exact bytes, no content of
this project reaches this provider, and the generated draft layer renders
Unknown (`unconsented-source-or-provider`) (REQ-polaris-generation-001).
Revocation is prospective (RFC5-13).
