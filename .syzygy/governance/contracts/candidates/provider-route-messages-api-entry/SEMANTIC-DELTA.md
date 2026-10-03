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
RFC4-9, RFC2-23, RFC2-24, RFC3-16(a), RFC5-15 and RFC5-16.

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

One entry for the same authority as PR #255's entry, with that entry's role
identity and a new implementation identity, `polaris-generation/provider-messages-api`: project `project:syzygy`, provider
`provider:anthropic`, type `model-provider`.

- **Substitute, never an addition (RFC4-9).** RFC4-1 allows one adapter per
  external authority per project. RFC4-9, quoted whole in the entry's
  `routeSubstitution` block and here: "**RFC4-9 — Substitution.** Replacing an
  implementation (a different VCS host, a different scheduler) is a registry
  event: the role identity persists, a new implementation identity is
  registered, and prior records keep resolving under the old one.
  Substitution never rewrites history and never migrates substrate-native
  aliases into the new substrate's namespace." The entry therefore keeps PR
  #255's role identity (`observerId`) and registers a new implementation
  identity, so the two cannot both sit in the registry. If PR #255's entry is
  adopted first, adopting this one is the RFC4-9 replacement and its act names
  the implementation it retires; otherwise PR #255's entry is not adopted.
  [Inferred] The shared role name still spells the Agent SDK for historical
  reasons; renaming it is a change to PR #255's entry, not made here.
- **Request bytes.** The entry lists them: endpoint `POST /v1/messages`;
  generator-built parts; the SDK-fixed headers (every value a literal or a
  shape, `x-stainless-timeout` the literal 600) and `stream`; three headers
  that Node's built-in fetch sets, not the SDK, with Node unpinned; and a profile it
  pins itself (model `claude-opus-5-5`, tools absent, effort `high`, thinking
  off or adaptive only, a max_tokens ceiling of 64000). The route has no
  runtime process, so no system prefix, metadata, environment message or probe.
- **Credential.** An API key only, read from one environment variable
  (`SYZYGY_POLARIS_PROVIDER_API_KEY`, an [Inferred] proposal) and never written
  to a log. The name cannot start with `ANTHROPIC_`: [Observed] the adapter
  refuses to start when any such variable is set in the process.
  No owner sign-in credential class exists on this route.
- **Destination.** Exactly `https://api.anthropic.com/v1/messages`, POST. The
  gate rule that its configured upstream equals that origin, refusing any
  other scheme, host or port, is the entry's statement of what the
  implementation will enforce; the gate at the cited commit accepts any
  upstream URL; the work is tracked as bead syzygy-yqtg (lane-v) [Inferred: from the bead record].
- **SDK environment.** The client library reads `ANTHROPIC_`-prefixed
  variables of its own (an auth token, custom headers, a log level that can
  write the request body to the console, a base URL). The entry declares each
  as an input that must be unset, fail-closed; the adapter's refusal of any
  such variable is present at the cited commit and was absent at the commit
  round 1 read. Node's own transport variables (a TLS-validation switch, extra
  certificate authorities, the environment-proxy switch and the proxy variables)
  are declared as further inputs that must be unset, [Inferred] from Node's
  documented behaviour and enforced only by bead syzygy-yqtg.
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
