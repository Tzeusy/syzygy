# Owner direction — one-command Polaris dossier run

Date: 2026-10-14 (UTC; the owner's reply was read at about 07:39Z)

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`

This is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It amends no doctrine,
contract or specification. It directs the drafting of the candidate change
`openspec/changes/polaris-dossier-one-command-run/`, which binds nothing
until the owner signs it off by its version tag (VIS-4;
`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`). It authorizes no
implementation code.

## The owner's words

In a Claude Code CLI session on 2026-10-14, the owner wrote, unprompted:

> "The UX is pretty important here; a user of syzygy shouldn't have multiple
> start-stop episodes when trying to generate Polaris for a repository. In
> fact, ideal case is that the calling of the syzygy polaris binary
> implicitly calls all relevant CLI calls inside; with the independence
> requirements etc. settled within the syzygy workflow, and the user only
> ever runs one command"

The session drafted the candidate change and put packet questions Q0 and Q1
(`openspec/changes/polaris-dossier-one-command-run/OWNER-PACKET.md`) to the
owner in one question, with a second question about publishing:

> "First decision, Q0+Q1: record your request as an owner direction that
> supersedes those three directions, for runs started with `syzygy polaris`
> only?"

> "Separately: shall I push the branch and open a PR?"

The owner replied:

> "Yes and yes. I care less about the governance of changes compared to
> actually generating useful product for now; we can always focus on
> correctness and verification after proving usefulness"

## What it directs

1. **Q0.** The request above is recorded as this direction, the warrant of
   the candidate change.
2. **Q1.** For runs started with the one command (`syzygy polaris`) only,
   these are superseded:
   - the item "**No Syzygy-launched sessions.**" of
     [`POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`](POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md);
   - item 2 of
     [`OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`](OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md),
     as far as it says the product coordinates no agents;
   - item 2 of
     [`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`](POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md),
     as far as it says the operator starts the review session.

   Runs started with `syzygy dossier init` keep all three exactly, and
   REQ-polaris-generation-035 is unchanged for them.
3. **Priority.** The owner ranks a usable product above governance
   correctness for this work for now, with correctness and verification to
   follow once usefulness is shown. [Inferred] This states a priority; it
   does not itself authorize implementation or waive VIS-4's sign-off.

Packet questions Q2 to Q7 remain open.
