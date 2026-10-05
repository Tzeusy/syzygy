# Owner decision packet — Polaris dossier local-agent mode

> **Candidate — binds nothing.** Drafted 2026-10-05 under the owner direction
> `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`. It performs no act and
> carries no digest. Effect comes only from the owner's sign-off of the exact
> reviewed bytes, after a confirming review. A commit, a review or a merged
> pull request performs no act.

## What this is, in one paragraph

You directed that Polaris dossiers be written by your own Claude Code or Codex
session over a local clone, with Syzygy supplying the brief, the checks, a
fresh-context review step and the renderer, and making no provider call. This
package adds requirements 033 to 036 to the generator specification so that
the mode is specified, and says exactly which adopted sentences it replaces
for such a run (budgets, provider receipts, the registered provider route,
review independence, the discovery account, who answers clarifications). It
edits no adopted file, grants no read, egress, write or execution, and leaves
the provider mode parked, not withdrawn.

## What the package changes, in plain terms

- **Pinning.** `syzygy dossier init` checks that the clone's HEAD is a
  revision your observation consent names, records it, and from then on
  Syzygy reads only Git objects at that commit, never the working tree.
- **The agent writes, Syzygy checks.** Syzygy issues a brief (your five reader
  topics, the labelling and quotation rules, the schema). Every quotation must
  be one contiguous span of a cited file; Syzygy verifies it against the blob,
  and the page shows Syzygy's bytes, not the agent's. The agent cannot mark
  its own claims Observed. Findings go back to the agent until clean or until
  the repair limit you declared.
- **Review.** A separate session that has not seen the draft writes the
  inventory; another reviews from a packet Syzygy builds. Syzygy proves what
  the reviewer was given; it cannot prove the reviewer saw nothing else, and
  the page says so.
- **Limits and usage.** You declare the deadline, the agent's token or turn
  budget, the repair and question limits. Syzygy enforces the ones that bind
  its own steps. The agent's usage is your declared figure, labelled Inferred,
  never Observed or zero.
- **Disclosure.** Every page states the mode, your declared tool, version and
  provider, that the agent read the clone without restriction, that its read
  account is self-reported, and that Syzygy made no provider call.

## Questions for the owner

Each has a recommendation. None is decided by this packet.

**O1. Does the draft-layer consent condition of RFC7-20 and
REQ-polaris-generation-001 hold for a draft your own session computed?**
RFC7-20 (accepted) says: "Computing a draft is inference: absent SEC-2
named-provider consent it is **not computed** — the draft layer renders
Unknown (`unconsented-source-or-provider`)". Your ruling of 2026-10-05 put
your session's sends outside Syzygy's egress consent, with no egress record.
Read literally together, every operator-agent draft would render Unknown,
which makes the mode useless. This package does not resolve that; 033 makes
the draft layer depend on your ruling and renders Unknown without one.
*Recommended:* rule, with the sign-off, that RFC7-20's named-provider consent
governs drafts Syzygy computes or dispatches, and that for an operator-agent
run of a non-governed observed repository the condition is met by your own
act under the 2026-10-05 direction, with the disclosure 033 requires
[Inferred: this reads, and does not amend, an accepted clause]. *Alternative
A:* amend RFC7-20 through its own accepted-contract act first, then sign
this package; slower, and the escalation the direction did not ask for.
*Alternative B:* record a per-project statement naming your agent's provider,
which keeps RFC7-20 literal; but it is an egress-consent record in all but
name, which your Q3 answer declined.

**O2. Is the mode limited to observed repositories that are not governed
projects?** SEC-2 covers "governed-project content". Running the mode on a
governed project would send portfolio content to your agent's provider with
no per-project consent recorded. *Recommended (as drafted):* yes; governed
subjects stay in the provider mode. *Alternative:* allow a governed subject
when its existing egress consent names your agent's provider.

**O3. How is the agent kept from running code in the clone?** SEC-3 binds
Syzygy's execution; your agent can run anything your account can. *Recommended
(as drafted):* the brief forbids building, installing or running observed
code, the skill text advises a permission setting that denies the shell except
`syzygy` commands, and the run record discloses that Syzygy cannot observe
compliance. *Alternative:* require the operator to declare a no-shell
permission profile at `init`, and refuse the run without the declaration;
still unobservable, but explicit.

**O4. How independent must the review contexts be?** *Recommended (as
drafted):* separate top-level sessions for inventory and each review, same or
different tool, with session identifiers declared and checked to differ; a
subagent spawned inside the authoring session does not count, because the
author writes its prompt. *Alternative:* allow subagents, cheaper and weaker,
with the page saying so. *Stronger alternative:* require a different agent
tool for the fidelity review (a Codex review of a Claude Code draft).

**O5. Sign-off form.** The version-tagged sign-off of
`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` names "the
PWB specification deltas, the observer registry entry and the contract
successors queued behind them". A Polaris generator specification delta is
not named there [Inferred, from that text]. Your 2026-10-05 selection said
"bring it to you for a version-tag sign-off", which is a statement of intent
for this package, not an extension of Scope A. Precedents for this
specification: the understanding amendment was adopted by a phrase-and-digest
act; the tree-form amendment by a structured option selection recorded as a
plain direction; the profile change (032) recommends the same option
selection. *Recommended:* a structured option selection naming this package
and version `v1.0`, in which you also state that Scope A extends to Polaris
generator specification deltas; recorded with `scripts/record_versioned_signoff.py`
once the package has a builder that installs `proposed/` into `specs/` and
recounts (the same builder the profile change needs, so one serves both).
*Alternative:* the plain-direction recorder form used for the profile change
(`scripts/record_narrative_profile_adoption.py`), without a tag.

## What it does not do

It grants no read, egress, write, execution or release. It admits no
repository, withdraws no act, deletes no parked package, and amends no
doctrine, accepted contract or adopted byte. It binds nothing until reviewed
and acted on.

## Review

Fresh-context review before any offering, per `REVIEW-BRIEF.md`. No round has
run.
