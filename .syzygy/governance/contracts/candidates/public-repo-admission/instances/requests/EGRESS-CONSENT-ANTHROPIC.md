# Public-target egress consent — Anthropic, through the Claude Agent SDK (Claude Code runtime), signed in with the owner's existing Claude account

> Instance filled from `../../templates/EGRESS-CONSENT-TEMPLATE.md` by
> `scripts/build_public_repo_admission.py`. Candidate — binds nothing
> until the owner acts on this record's exact bytes.

Date: 2026-10-03 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `PUBLIC-EGRESS-anthropic`

Record version: `0.1.0-candidate.6`

Consent class: egress — one record per (project, provider) pair (RFC5-12)

Subject: `(project:syzygy, provider:anthropic)`

Provider and route: Anthropic, through the Claude Agent SDK (Claude Code runtime), signed in with the owner's existing Claude account, reached only through the registered provider
execution route (REQ-polaris-generation-017) and the single egress check
(RFC5-15). The model is recorded per run, not fixed here.

Permitted content classes (RFC5-14 closed vocabulary):

- `governance-text`
- `code-structure`
- `code-content`
- `evidence-content`
- `derived-composites`

Retention: provider requests, provider replies, run records and the Agent SDK runtime's own state, including any session transcript, are written only inside a run directory under `project:syzygy`'s state directory, outside git, from the start of the run. A run whose runtime cannot be configured to keep its state and transcript inside that directory does not start. The run directory holds the source spans sent for as long as the run is retained; nothing is retained in git, logs or machine responses. Anthropic's own retention is as the terms of the signed-in account state, disclosed rather than promised.

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier consent

## Scope

Only content read under an in-force observation consent for one of these
`(project:syzygy, repository)` pairs:

- `(project:syzygy, repository:psf-requests)`

together with the generator's own instruction text — its stage prompts
and response schemas, authored in Syzygy's repository at
`packages/polaris-generation-core/src/prompts.ts` and classified
`code-content` of `project:syzygy` — which every request carries. Every other source of `project:syzygy` content is outside this
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
- The model sees only what each request carries. The route invokes no tools
  on the provider's or its runtime's side (no file access, command execution,
  web access or other tool), and adds no context of its own:
  the runtime loads no instruction or memory files, user or project settings,
  MCP servers, hooks or environment summary (working directory, Git status);
  its working directory is an empty directory inside the run directory. The
  adapter is accepted only when a captured request shows the system prompt
  and messages the generator built and nothing else.
- The route sends nothing to any destination other than the provider:
  the runtime's telemetry, error reporting and update checks are disabled; a
  run whose runtime cannot disable them does not start.
- This record's own condition: provider output is generated editorial draft.
  It is never recorded as an Observed claim, as adopted intent, or as the
  target project's own statement.

## Effect

Without an effective owner act over this record's exact bytes, no content
reaches this provider, and the generated draft layer renders Unknown
(`unconsented-source-or-provider`) (REQ-polaris-generation-001). Revocation
is prospective (RFC5-13).
