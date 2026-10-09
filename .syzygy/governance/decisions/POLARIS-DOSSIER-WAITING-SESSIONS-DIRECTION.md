# Owner direction — pre-started waiting sessions for the dossier hand-offs

Date: 2026-10-08T16:24:26.838Z (UTC); 2026-10-09 in the owner's local time

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08` (named for the
UTC date of the instant above)

This is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It amends no doctrine,
contract or specification: it authorizes code and the drafting of a
candidate specification version, which binds nothing until the owner signs
it off by its version tag (VIS-4;
`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`).

## The owner's words

At 2026-10-08T16:24:26.838Z (UTC; the transcript timestamp of the tool
result), in the Claude Code CLI, the lead put decision 3 of
[`DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`](DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md)
to the owner as an AskUserQuestion structured question, the same channel as
the 2026-10-07 Redis sitting, under the header chip "Hand-offs". The
question, verbatim from the lead's record of the selection:

> "Decision 3 (P-107): the run stalled for five hours because you must start
> each helper session (inventory, fidelity review, design review) by hand.
> Which hand-off model?"

The owner selected the option labelled:

> "B, reviewer may continue (Recommended)"

described as:

> "At run start you open all helper sessions. They wait for their packets and
> run unattended with only read tools plus their one syzygy command
> pre-approved. Cost: unattended sessions read untrusted clone text, and
> while you're away nothing executes Redis code. One reviewer may continue
> across revisions, disclosed on the page (its earlier verdict may anchor
> it). Needs a v1.2 spec package and a wait-mode code change."

Not selected:

- "B, fresh reviewer per revision": "Same as above, but each revision's
  review needs a session you start. That is more independent, and more
  stalls after repairs."
- "C, you attend, agent launches": "The authoring session launches each
  helper headless, and you approve each launch. You must be present. It
  supersedes your 2026-10-05 item 2 and weakens independence."
- "A, keep as is": "No change. Runs stall whenever you step away."

The owner saw the question form and the lead's earlier chat summaries of the
review verdicts and of the packet's content; not the raws, the dispositions
or the packet file itself.

The packet's "Words to give" maps the selected option to:

> "Direction: pre-started waiting sessions (option B), one reviewer may
> continue across revisions"

The owner selected the option; the owner did not type that phrase. It is
quoted here as the packet's own wording for the selection.

## The direction

1. **Option B, pre-started waiting sessions.** At the start of a dossier run
   the operator may open the inventory, fidelity-review and design-review
   sessions, from commands Syzygy prints. The inventory starts at once. Each
   reviewer runs a `syzygy dossier` command that waits for its packet, then
   re-hashes the packet and reviews it. The operator still starts every
   session; only when it is started changes.
2. **The sub-question: one reviewer may continue.** One waiting review
   session may review the next revision of its subject after a repair, from
   the next packet Syzygy delivers to it, instead of a session the operator
   starts for each revision. That continuation **must be disclosed on the
   review page**. The packet states the cost: the reviewer has seen its own
   earlier verdict, which anchors the next one, where this repository's own
   loops use a fresh reviewer each round.
3. **Authorized:**
   - the wait-mode code in `packages/polaris-dossier`: the waiting command,
     printing the start-of-run commands for every helper session, and
     recording and disclosing a continuing reviewer;
   - drafting the version 1.2 specification package for
     `openspec/changes/polaris-dossier-local-agent-mode/`, saying that a
     session may start before its packet exists and that a continuing
     reviewer is permitted and disclosed.

   The code may merge only once version 1.2 is signed off: until then the
   signed version 1.1 says each session is handed its packet when the
   operator starts it.
4. **The recommended mitigation, taken with the option.** A printed start
   command pre-approves only read tools and the role's one `syzygy dossier`
   command, never a general shell and never a write. The option the owner
   selected says "with only read tools plus their one syzygy command
   pre-approved"; the packet's words: "approve only read tools and the
   role's one `syzygy dossier` command [Inferred]". The drafter reads this
   to mean that a session hands its inventory or verdict to that command,
   and Syzygy writes the file [Inferred: the drafter's reading of the
   selected words; the owner saw the option, not this mechanism]. Where
   an agent tool offers no such narrow scope, Syzygy prints no broader one and
   says so.

## What this direction does not authorize

- **No headless launch by the author.** The authoring session, its agent
  and its subagents start no helper session, headless or otherwise. A
  session the authoring session's agent launches still does not satisfy the
  inventory or a review (REQ-polaris-generation-035; the owner direction of
  2026-10-05, item 2, in
  [`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`](POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md)).
  Options C and D were not chosen.
- **No Syzygy-launched sessions.** Syzygy starts, resumes and signals no
  session. Waiting is a command the operator's session runs; Syzygy only
  writes the packet into that session's directory. The owner's direction of
  2026-10-03, item 2, still stands: "It changes nothing about what Syzygy
  the product may do: the product still coordinates no agents."
  ([`OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`](OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md)).
- **Nothing unattended that executes observed code.** Helper sessions never
  carry the execution permission. The signed rule that the authoring
  session's permission lapses when the owner stops attending it is
  unchanged, so an unattended stretch of a run is a reading-only stretch.
- It widens no consent, read, egress, write or execution, and changes no
  provider-statement or content-class gate. It performs no act and signs
  nothing; version 1.2 is offered separately after its own review.

## Where it is recorded

Register row P-107 in
[`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md) is marked ruled
by this direction; its version 1.2 sign-off stays open there.
