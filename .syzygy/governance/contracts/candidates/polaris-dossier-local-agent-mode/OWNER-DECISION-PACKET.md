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
- **Running the project.** The agent may build and run it; anything it
  concludes from that is Inferred, and the commands it reports are listed.
  Syzygy runs nothing.
- **Limits and usage.** You declare the deadline, the agent's token or turn
  budget, the repair and question limits. Syzygy enforces the ones that bind
  its own steps. The agent's usage is your declared figure, labelled Inferred,
  never Observed or zero.
- **Disclosure.** Every page states the mode, your declared tool, version and
  provider, that the agent read the clone without restriction, that its read
  account is self-reported, and that Syzygy made no provider call.

## Questions for the owner

Each has a recommendation. None is decided by this packet.

**O1. RFC7-20 and an operator-computed draft — ruled 2026-10-05.** The owner
chose "Rule it by interpretation" over the recommended "Name my provider per
project" (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`, item 1, recorded in
`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`).
RFC7-20's condition is read as governing drafts Syzygy computes; an
operator-computed draft is admitted with disclosure, a declared and recorded
tool and provider, and byte-verified quotes. Requirement 033 applies exactly
those three conditions and renders the draft layer Unknown when any fails or
the reading is withdrawn. **The trade-off stays open in this package:** the
option's own description said "a reviewer may call it a contract change". If
the review finds that it is one, that finding comes back to you; the package
neither concedes nor rebuts it. No question is put here.

**O2. Is the mode limited to observed repositories that are not governed
projects?** SEC-2 covers "governed-project content". Running the mode on a
governed project would send portfolio content to your agent's provider with
no per-project consent recorded. *Recommended (as drafted):* yes; governed
subjects stay in the provider mode. *Alternative:* allow a governed subject
when its existing egress consent names your agent's provider.

**O3. Code execution by the agent — ruled 2026-10-05.** The owner chose
"Allow, disclose" over the recommended "Forbid, disclose" (rulings direction,
item 2). The brief says the agent may build and run the observed project;
claims resting on that are Inferred and name their commands; the run record
lists the commands the agent reports, as its report; Syzygy executes none
(SEC-3). No question is put here.

**O4. How independent must the review contexts be?** *Recommended (as
drafted):* separate top-level sessions for inventory and each review, same or
different tool, with session identifiers declared and checked to differ. In
the one-line flow (`design.md`) the authoring session may launch them
headless, but only with the fixed prompt Syzygy prints, so the author never
writes the reviewer's instructions; a subagent whose prompt the author writes
does not count. *Alternative:* allow subagents, cheaper and weaker,
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
