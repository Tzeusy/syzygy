# Owner direction — the dossier's model step runs the operator's local agent CLI as a subprocess

Date: 2026-10-15

Owner: Tzeusy

Decision ID: `DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15`

This is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It amends no doctrine,
contract or specification, signs no package, and labels nothing accepted
(VIS-4). It is a direction, not a consent: it widens no read, egress, write,
execution or launch authority (see "What this direction does not grant").

## The owner's words

On 2026-10-15, in the Claude Code CLI, the lead session put one structured
question (AskUserQuestion) to the owner. The question, verbatim:

> "Provider routes (bc0g, yqtg): on 2026-10-05 you parked Syzygy making its
> own LLM provider calls and chose local-agent mode for the dossier instead.
> Un-parking means a new direction, picking a route, and consenting to
> provider egress. Do you want to un-park?"

The options offered were "Keep parked", "Un-park route B (Messages API
adapter #264)" and "Un-park route A (Agent SDK adapter #258)". The owner
selected none of them and answered in free text, verbatim:

> "Syzygy should run *our local codex or claude cli binary* like a subprocess
> with explicit workspace/instructions/artifacts path and skill/mcp guidance,
> no custom SDK or API tooling"

[Observed: the question and answer as relayed to this drafting lane by the
lead session; the transcript itself is not stored in this repository.]

## The direction

1. **Provider routes stay parked and are no longer pursued.** Syzygy does not
   make its own model-provider calls through a custom SDK or API client for
   the dossier. Neither route A (the Agent SDK provider execution route) nor
   route B (the Messages API provider execution route) is offered for
   sign-off, and the egress gate work that existed only for route B is not
   pursued. Nothing is deleted.
2. **The model step is the operator's local agent CLI, run as a
   subprocess.** Where Syzygy itself drives the model step of a dossier run,
   it runs the operator's own locally installed `codex` or `claude` binary as
   a child process, with the workspace directory, the instructions file, the
   artifacts output path and any skill or MCP guidance passed to it
   explicitly. [Inferred: the drafter's reading of "explicit
   workspace/instructions/artifacts path and skill/mcp guidance"; the owner's
   words do not name the flags.]
3. **Relation to the one-command run.** This confirms the launch route the
   prototype of `POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`
   ([`POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`](POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md),
   item 5) already takes for Claude Code, and states it as the only model-step
   route for Syzygy-driven runs. [Inferred] It is read as applying to runs
   Syzygy launches (the `syzygy polaris` launched form); it changes nothing
   for runs started with `syzygy dossier init`, which keep the
   operator-started sessions of REQ-polaris-generation-035.
4. **Drafting authorized.** A candidate specification delta for a local CLI
   subprocess runner may be drafted and reviewed. It binds nothing until the
   owner signs it off (VIS-4).

## What it supersedes

- **Item 4 of `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`**
  ([`POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`](POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md),
  lines 80–83): "The provider-route registry entries, the egress v1 and v2
  packages and the provider adapter are parked: not offered for sign-off,
  not deleted." Superseded only as to its open-endedness: the parking was a
  hold pending a later choice; that choice is now made, and the packages are
  not pursued. The item's text, and items 1–3 and 5, are unchanged. That
  file is not edited.
- **Route A's registry material.** The Agent SDK provider route entry, row 1
  of `.syzygy/governance/contracts/candidates/public-admission-registry-entries/PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt`
  (proposed file
  `public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json`),
  and that package's provider-route question. This direction says nothing of
  the same manifest's row 2, the Git source-acquisition entry; the
  source-acquisition entry signed on 2026-10-07 is a separate local-agent
  version (`PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1.0.md`), which
  this direction leaves in force.
- **Route B's registry material.** The whole candidate package
  `.syzygy/governance/contracts/candidates/provider-route-messages-api-entry/`
  (merged as a candidate in PR #273), its recorder
  `scripts/record_messages_api_route_registry_act.py` and its builder.
- **Register rows P-87 to P-91 of the unmerged sitting packet (PR #260)**,
  as far as they offer a provider route or a provider-egress consent; in its
  latest form the provider-route choice is row P-89 ("O3 the provider route
  is one choice between route A here and route B (PR #273)"). Those rows are
  not on `main` and are not edited here.
- **The un-merged adapters and wiring** that depend on a route: PRs #258
  (Agent SDK adapter), #264 (Messages API adapter) and #334 (`poc:dossier`
  route flag and gate). They are superseded candidates; closing them is the
  owner's or the triage lane's, not this record's.

## What this direction does not grant

- **It is not a consent.** Whatever the CLI sends to its provider is egress
  of the content it reads. Target-repository content may go through a
  launched CLI only where an act already in force covers that repository,
  that content class and that agent tool with its provider:
  - **redis/redis:** under its observation consent
    (`PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`), the public-source
    screening-scope act in force
    (`PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md`)
    and the Claude Code with Anthropic agent-provider statement
    (`DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md`). No Codex or OpenAI
    statement exists for Redis, so a Codex launch over Redis content has no
    act to stand on until one is signed.
  - **Butlers:** only under its own acts (`PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`
    and the PWB registry and policy acts), which consent to Syzygy's own
    reads and name no agent tool or provider. No act lets a launched CLI
    receive Butlers content.
  - **Any other repository:** nothing.

  One limit stands beside this [Inferred, from round 1 of the delta's
  review, finding 4]: a launched session can read the whole clone, so the
  tool can send its provider content of classes the statement does not
  list. The 2026-10-05 ruling (item 2 of the local-agent mode direction)
  treats the agent's own reading and sending as the operator's act, which is
  the basis on which that is disclosed rather than refused. Whether to
  disclose it or to refuse such runs is the owner's question, carried as
  P-111 Q2; this direction does not settle it.
- It adopts no registry entry, records no egress, and does not make a
  launched session's transmissions anything other than what the one-command
  run's packet Q2 answer says they are.
- It authorizes no implementation beyond what the acts and directions in
  force already authorize; in particular it does not sign
  `openspec/changes/polaris-dossier-one-command-run/`, which stays a
  candidate.
- It does not let any session execute observed code (SEC-3; REQ-polaris-generation-044 as drafted).
- It withdraws no act in force.

## Where it is recorded

- Register row P-111 in [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md)
  carries the open sign-off of the candidate runner delta.
- The candidate delta:
  `.syzygy/governance/contracts/candidates/dossier-local-cli-subprocess-runner/SEMANTIC-DELTA.md`.
- Beads: `syzygy-bc0g` re-scoped to the CLI-subprocess route;
  `syzygy-yqtg` closed as superseded by this direction.
