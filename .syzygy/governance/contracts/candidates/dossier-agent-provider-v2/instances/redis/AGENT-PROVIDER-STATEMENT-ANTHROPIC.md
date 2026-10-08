# Agent-provider statement — redis-redis to anthropic

> Instance filled from `../../templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md` by
> `scripts/build_dossier_agent_provider_v2.py`. Candidate — binds nothing
> until the owner acts on this record's exact bytes.

Date: 2026-10-08 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `AGENT-PROVIDER-redis-redis-anthropic`

Record version: `0.2.0-candidate.1`

Record class: per-project consent (SEC-2; REQ-polaris-generation-033's
per-project statement)

Subject: `(project:syzygy, repository:redis-redis, agent-provider:anthropic)`

Agent tool: Claude Code, run by the operator with the operator's own account

Agent provider: Anthropic, under the terms and settings of the operator's own account; Syzygy holds no key or account for it

Content classes the provider may receive (RFC5-14 closed vocabulary):

- `governance-text`
- `code-structure`
- `code-content`
- `evidence-content`
- `derived-composites`
- `project-documentation`

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes version 0.1.0-candidate.1 of this record, if an act over that version is in force, from the effective instant of the act on this version (prospective, RFC5-13); with none in force it supersedes nothing

## What it decides

This record is the explicit, recorded, per-project consent SEC-2 requires
before this repository's content reaches a model provider, for the one case
REQ-polaris-generation-033 names: an operator-agent run in which the
operator's own sessions of the tool above, with the provider above, author
the draft, the inventory and the reviews over a local clone of this
repository. With it in force, and the run's other gates met, Syzygy may issue
the brief for this repository even when the repository counts as governed or
its project input is silent about an evidence drawer; the run record cites
this record.

The content classes above are the owner's statement of what the provider may
receive. They do not limit what the agent reads or sends: the agent reads the
clone without restriction, and content Syzygy's classification and screening
policies would exclude, secrets included, may reach the provider. Every page
of a run that relies on this record says so. Classification and screening
still bind every read Syzygy makes and everything Syzygy stores or renders.

## What it does not do

It is not an egress record and is not evidence of what the agent sent.
Syzygy makes no provider call, resolves no provider route and records no
egress for the agent's sends. It permits no read by Syzygy (the observation
consent does that), no other tool or provider, no other repository, and no
execution of the repository's code (that is SEC-3 as amended by D9, and the
owner's choice for each run).

## Withdrawal

Withdrawal is a later owner act naming this record. It is prospective
(RFC5-13): Syzygy refuses every later step of a run that relies on this
record and every new brief that would need it; records made under it remain,
shown as withdrawn.
