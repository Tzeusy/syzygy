# requests egress consent — Anthropic (Claude API) — pending Q1

> Instance for target T1, filled from `../../templates/EGRESS-CONSENT-TEMPLATE.md`. Candidate —
> binds nothing until the owner acts on this record's exact bytes. Fields
> marked "pending Q…" follow the packet's open questions and change if the
> owner answers differently.

Date: 2026-10-03 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `PUBLIC-EGRESS-REQUESTS-anthropic-2026-10-03`

Record version: `0.1.0-candidate.1`

Consent class: egress — one record per (project, provider) pair (RFC5-12)

Subject: `(project:oss-requests, provider:anthropic)`

Provider and route: Anthropic (Claude API) — pending Q1, reached only through the registered provider
execution route (REQ-polaris-generation-017) and the single egress check
(RFC5-15). The model is recorded per run, not fixed here.

Permitted content classes (RFC5-14 closed vocabulary):

- `governance-text`
- `code-structure`
- `code-content`
- `evidence-content`
- `derived-composites`

(`work-history` excluded — pending Q2.)

Retention: provider replies and run records retained in the observing project's state directory, outside git; source bodies not retained beyond the run's scratch clone; the provider's own retention is as its API terms state, disclosed rather than promised — pending Q3.

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
