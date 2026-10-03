# Semantic delta — Messages API provider route registry entry

> **Candidate — binds nothing.** Drafted 2026-10-03 by an agent as route B of
> the provider choice. Effect would come only from this entry's own owner act
> over its exact bytes. No review has run against these bytes.

**Artifact:** one new whole file under `proposed/` in this directory,
`POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json`. It does not
exist in the installed home `.syzygy/governance/declarations/adapter-registry/`
and this package installs nothing there.

**Stable IDs affected:** none minted, renamed or retired. The entry answers
REQ-polaris-generation-017 (Source: RFC4-2) and cites RFC4-1, RFC4-2, RFC4-3,
RFC2-23, RFC2-24, RFC3-16(a), RFC5-15 and RFC5-16.

**Change class:** Normative (it creates a registry entry; an entry is honored
only under an owner act, RFC4-7).

## Current meaning

[Observed] The installed registry holds one entry, the Butlers project-shape
observer. No entry registers a provider route. PR #255 proposes one, through
the Claude Agent SDK runtime; PR #264 implements a route that calls the
Messages API directly through `@anthropic-ai/sdk` 0.131.0. Under
REQ-polaris-generation-017 an unregistered route establishes no deterministic
fact.

## Proposed meaning

One entry, `polaris-provider-route-anthropic-messages-api`, for the same
authority as PR #255's entry: project `project:syzygy`, provider
`provider:anthropic`, type `model-provider`.

- **Substitute, never an addition.** RFC4-1 allows one adapter per external
  authority per project. This entry and PR #255's entry are alternatives;
  the entry's `routeSubstitution` block names the other, and exactly one may
  be adopted. Adopting this one means PR #255's provider entry is not.
- **Request bytes.** The entry lists them: endpoint `POST /v1/messages`;
  generator-built parts; the SDK-fixed headers and `stream`; and a profile it
  pins itself (model `claude-opus-5-5`, tools absent, effort `high`, thinking
  off or adaptive only, a max_tokens ceiling of 64000). The route has no
  runtime process, so no system prefix, metadata, environment message or probe.
- **Credential.** An API key only, read from one environment variable
  (`ANTHROPIC_API_KEY`, an [Inferred] proposal) and never written to a log.
  No owner sign-in credential class exists on this route.
- **Runtime egress gate.** A loopback forwarder passes a request only when the
  acceptance predicate holds, `permitted()` is true and an explicit upstream
  is set; otherwise it answers 403. Provenance is pinned by commit and blob
  in the entry.
- **Implementation version stays null.** RFC4-3 admits no output from it
  until a later entry version names the implementation.

## Consistency with the confirmed egress record

[Inferred] A drafter's comparison, set out in the entry's `egressRecordFit`:
no enforceable condition of the egress record (PR #215) is violated, and this
route sends strictly less than the Agent SDK route. Three wordings need the
owner's reading: the record names the Agent SDK as the route; it says a route
adds only bytes "fixed by the runtime" and these pinned profile fields are
not; and it says the captured request shows the generator's parts "and
nothing else". The last two apply equally to PR #255's entry. This package
therefore does not claim that no egress record version is needed; it claims
that none is needed if the owner reads the first as descriptive and the other
two as the entry's pinned fields allow.

## What it does not do

It grants no read, egress, write, execution or release, edits no adopted
specification, policy, consent or the egress record, and does not touch the
Butlers entry. It makes no provider call and reads no external repository.
