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

carried in a request's `inputs` as source spans, or as validated stage
artifacts computed from them (composites, RFC5-14). Every other source of
`project:syzygy` content is outside this consent, including the Butlers
repository, the rest of Syzygy's own repository and any work history, and
stays unsent.

## What a request carries

A request is one canonical-JSON envelope with exactly these five fields, as
the generator's pipeline builds it (`runGenerationPipeline` in
`packages/polaris-generation-core/src/pipeline.ts`): `promptVersion`,
`system`, `responseSchemaVersion`, `responseSchema` and `inputs`. The
`generate` port also receives a dispatch permit and an abort signal; neither
is part of the envelope and neither is sent.

- `promptVersion` and `system` come from `promptForStage` in
  `packages/polaris-generation-core/src/prompts.ts`: a shared preamble and one
  instruction per stage.
- `responseSchemaVersion` and `responseSchema` come from `stageSchema` in
  `packages/polaris-generation-core/src/provider-draft.ts`: one closed schema
  per stage.
- `inputs` carries, per stage, only these fields: inventory — `sources`,
  `sourcePopulation`, `readerQuestions`, `requestedAssets`; plan —
  `sources`, `readerQuestions`, `inventory`, `requestedAssets`; author —
  `sources`, `readerQuestions`, `inventory`, `plan`, `requestedAssets`; edit —
  those plus `draft`; fidelity — `sources`, `readerQuestions`, `inventory`,
  `draft`, `requestedAssets`; repair — those plus `findings`. `sources` are
  admitted target spans; `sourcePopulation` lists each source's id,
  classification basis and exclusion reason, without a body; the reader
  questions and requested assets are the run profile's.

The first two bullets are the only Syzygy-authored content a request carries
(the generator's instruction text). It is classified `code-content` of
`project:syzygy` by the instruction-text rule of `project:syzygy`'s effective
public-source screening scope, a closed rule that names exactly those two
symbols and no other file or symbol; the consent does not classify it. Each
audit record names the prompt and schema versions sent. The list above is
re-derivable from the code with `scripts/derive_generator_sent_text.mjs`.

Beyond the envelope, the route adds only the bytes that its registered
provider execution route entry lists as fixed by the runtime. A request
carrying any other byte, header or field is refused at the single egress
check.

## Conditions

- Only content screened under `project:syzygy`'s effective public-source
  screening scope may be sent, and only the instruction text its
  instruction-text rule classifies. Excluded or unclassifiable content is
  never sent (RFC5-14, RFC5-16); a request whose instruction text the rule
  does not name is refused.
- A composite's class is computed from what it embeds; one whose class cannot
  be determined is refused and the refusal shown (RFC5-14).
- Every transmission passes the single egress check and emits an audit record
  (RFC5-15).
- The model sees only what each request carries. The route invokes no tools
  on the provider's or its runtime's side (no file access, command execution,
  web access or other tool), and adds no context of its own:
  {{ROUTE_CONTEXT}}
- The route sends nothing to any destination other than the provider:
  {{ROUTE_TELEMETRY}}
- This record's own condition: provider output is generated editorial draft.
  It is never recorded as an Observed claim, as adopted intent, or as the
  target project's own statement. It is shown only on the local daemon's
  generated editorial draft view or as a static file in the run directory,
  and is never published.

## Effect

Without an effective owner act over this record's exact bytes, no content
reaches this provider, and the generated draft layer renders Unknown
(`unconsented-source-or-provider`) (REQ-polaris-generation-001). Revocation
is prospective (RFC5-13).
