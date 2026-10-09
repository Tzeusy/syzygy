> **Candidate — binds nothing.** This semantic delta is drafted under the
> owner direction `POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08` and CC-REV-2.
> It performs no act and amends no signed byte. Version 1.1 of
> `polaris-dossier-local-agent-mode` stays in force until the owner signs off
> version 1.2 after a fresh independent review of these exact bytes.

# Semantic delta DOSSIER-LOCAL-AGENT-1.2 — waiting sessions and a continuing reviewer

Version 1.2 lets the operator start the inventory and review sessions at the
start of a run, before their input exists, and lets one review session review
later revisions of its subject. Today each hand-over stops the run until the
operator is there to start the next session; the 2026-10-08 blockers packet
names that as the stall, and the owner chose option B for it, with the
sub-answer that one reviewer may continue across revisions, disclosed on the
review page.

**Artifact(s):** the signed change
`openspec/changes/polaris-dossier-local-agent-mode/`, at its v1.1 bytes on
`main` (tag `polaris-dossier-local-agent-mode-v1.1`; the spec last changed at
`32a067aa`). Three files move, by the patches under `proposed/`:

- `specs/polaris-generation/spec.md` (`spec.md.patch`), including its
  header line, which moves from "Exact behavioral delta, version 1.1" to
  version 1.2, names the v1.1 sign-off record beside the v1.0 one, and says
  the bytes bind only by the sign-off of version 1.2 (non-normative);
- `design.md` (`design.md.patch`);
- `proposal.md` (`proposal.md.patch`), including its version line.

`GOVERNING-DEPENDENCIES.md` is regenerated on install
(`check_spec_reconciliation.py --regenerate`) and gains the decision
`POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08`. `tasks.md` is unchanged.

**Stable IDs affected:** REQ-polaris-generation-035, amended in place: one
paragraph added to the requirement text, four scenarios added, the case, the
observable, the falsifier and the warrant block's `decisions` extended. No
other requirement changes. No identifier is minted, retired, renamed or
renumbered, and no requirement title changes.

**Change class:** **Normative.** Under v1.1 each inventory and review session
is given its input when the operator starts it; a session that starts first
and waits for its packet, or a review session that reviews a second revision,
has no rule saying what Syzygy must check or disclose. Under v1.2 both are
permitted, each with the checks and disclosures below; a build that lets a
session read an un-re-hashed delivery, waits past the deadline, prints a
broad pre-approval, or counts a continuing reviewer's verdict without saying
so fails v1.2.

**Author:** agent drafting for the owner direction (lane-handoff).

**Date:** 2026-10-09, drafted over v1.1 as installed on `main`.

## Sources

- The owner direction
  `.syzygy/governance/decisions/POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`
  (`POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08`): option B, the
  sub-answer that one reviewer may continue with disclosure, and the
  recommended mitigation taken with the option.
- Decision 3 of
  `.syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`,
  which states the option, the sub-question and the mitigation.

## Current meaning

At v1.1, REQ-polaris-generation-035:

- requires each inventory and review to be produced "in a separate top-level
  agent session that the operator starts", and refuses a subagent, a process
  of the authoring session or a headless session it starts;
- says for each review "Syzygy SHALL emit a review packet", which the review
  context re-hashes before it reads it; it says nothing of when the session
  starts relative to the packet, and the design hands each session its
  packet in the directory it is started in;
- says nothing of a session that reviews more than one revision. "Any
  revision of the subject or the inventory retires the verdicts bound to it",
  and each later review is, by the design, a new session.

## Proposed meaning

1. **Sessions may start before their input.** "An inventory or review session
   MAY be started before its input exists". At the start of a run Syzygy may
   write the inventory brief, make the review directories and print a command
   per session; "the operator starts each such session as above, and neither
   Syzygy nor the authoring session starts, resumes or signals it."
   "Because a waiting session holds its terminal for the whole run, Syzygy
   SHALL print its command for a new terminal only and SHALL refuse a
   shell-escape launch form declared for it." The rule that a subagent, a
   process of the authoring session or a headless session it starts does not
   count is unchanged.
2. **One command, bounded, local, re-hashing.** A waiting session "SHALL
   obtain its input only through one Syzygy command named for its directory,
   which reads only the local file system and makes no network request; waits
   at most a bounded time, never past the run's declared deadline, and then
   tells the session to run it again; and before the session reads its input
   re-hashes it against the digest Syzygy recorded in the run's state
   directory when it wrote it, refusing on any mismatch."
3. **Delivery.** Syzygy delivers a packet "only by writing the packet and its
   digest into that session's directory as the next numbered round and
   recording the delivery, and only after the gates of
   REQ-polaris-generation-033, including the per-project provider statement
   for the waiting session's own declared agent tool, pass at that delivery;
   a delivery SHALL NOT change the session's declared agent tool, version or
   model."
4. **The mitigation the owner took with the option.** The selected option
   reads "with only read tools plus their one syzygy command pre-approved".
   The printed command "SHALL pre-approve, where the agent tool offers rules
   that narrow, only read tools over the session's own directory (and, for
   the inventory session, the clone) and that one Syzygy command for that
   directory, and never a write or a general shell"; where the tool offers
   none, "Syzygy SHALL print no pre-approval and SHALL say so." "Where the
   agent tool can limit which of its own tools a session has at all, the
   printed command SHALL also limit a waiting session to its read tools and
   the shell its one command runs in." Because the
   session may not write, "A waiting session SHALL hand its inventory or
   verdict to that command, as content it passes to the command or as a file
   under its own directory that the command reads", and "Syzygy writes the
   content into the session's directory under the role's own file name (the
   inventory, or the verdict of a round Syzygy delivered), and only there".
   Content passed to the command may quote the observed project, so "every
   instruction Syzygy prints for passing content SHALL pass it so that the
   shell expands nothing in it, and SHALL say so." "A waiting session SHALL
   NOT carry the execution permission of REQ-polaris-generation-033."
5. **A continuing reviewer, disclosed.** "One waiting review session MAY
   receive the packet of each later revision of its subject as its next
   round", and its verdict is validated and counted under the existing rules,
   so a revision still retires the verdicts bound to the earlier packet. "For
   every counted verdict the review page SHALL disclose whether its session
   had received an earlier round, or declares the session identifier of an
   earlier verdict of its kind, and where it had, that the reviewer has seen
   its own earlier verdict, which may anchor this one."
6. **What stays Inferred.** The delivery records, the delivered files and
   the declared session identifiers lie within the sessions' write reach, so
   "that a waiting session read the packet Syzygy delivered, unaltered, that
   the operator used the printed command, that the agent tool applied the
   printed pre-approval as written, that no allow rule in a settings layer
   the operator keeps outside the printed command (the agent tool's user,
   project or local settings) widens what the session may run unattended,
   that the session started no subagent, which would act with the same
   pre-approval, that the printed limit on the agent tool's own tools leaves
   the session no other of them, and a reviewer's continuity or its absence
   are Inferred; whether a tool from outside the agent tool's own set, such
   as one connected through the operator's account, remains available to the
   session, and whether the agent tool's rule for the one command admits an
   output redirection, a write outside the role's own file, are Unknown; and
   no surface states any of them as Observed." The printed pre-approval is
   narrowed where the tool allows it (the implementation also limits Claude
   Code to its built-in Read, Glob, Grep and Bash tools, denies the write,
   web and subagent tools and loads no MCP server), but no printed flag
   reaches the operator's own settings layers or a tool outside the agent
   tool's own set, so those residuals are named rather than claimed closed.

Four scenarios carry these: "Waiting session started before its packet",
"Packet delivered to a waiting session", "Printed pre-approval for a waiting
session" and "Continuing reviewer disclosed". The falsifier gains one arm per
item, and the case and the observable gain the waiting sessions. `design.md`
gains a paragraph in decision 5, two command rows and exit status 3;
`proposal.md` gains its version line and one paragraph under "Reviews in
sessions the operator starts".

## What explicitly does NOT change

- Who starts a session. The operator starts every session; a subagent, a
  process the authoring session's agent launches (headless or not) or any
  context whose instructions the authoring session wrote still does not
  satisfy the inventory or a review. Options C and D of the blockers packet
  were not chosen.
- Syzygy coordinates no agent: it starts, resumes and signals no session
  (owner direction of 2026-10-03, item 2).
- The packet's contents, the verdict's validation, the session-identifier
  rule, the launch-form rule (but for a waiting session, whose declared form
  is a new terminal only: item 1) and the rule that any revision retires the
  verdicts bound to it. A waiting session declares its identifier as before;
  the identifier rule only refuses a reviewer that declares the author's or
  the inventory session's identifier.
- The execution rule and permission of REQ-polaris-generation-033, D9, the
  credential condition and the provider-statement gate. A waiting session is
  a reading-only session.
- REQ-polaris-generation-033, 034 and 036, every adopted requirement
  001–032, and the base and understanding changes.
- No doctrine, contract or policy text, and no implementation code.

## Warrant

- **The owner direction** `POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08` for
  items 1 to 5; it joins 035's `decisions` warrants.
- **VIS-1, VIS-2** for item 6: a value Syzygy cannot observe is Inferred and
  said so. **VIS-3** stays 035's primary warrant.
- **CC-REV-2** (an amendment of a signed specification travels as a new
  version with its own review) and the owner's direction
  `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02`, as extended to
  Polaris generator deltas by the v1.0 selection.

## Evidence or decision basis

- The direction record and the packet named above.
- [Observed, this session, over the v1.1 bytes on `main` with these patches
  applied] `openspec validate polaris-dossier-local-agent-mode --strict`
  reports the change valid; `scripts/count_polaris_effective_scenarios.py`
  gives 36 requirements and 248 scenarios, against 36 and 244 at v1.1.
- An implementation behind a v1.2 gate exists on the branch that carries this
  package (`packages/polaris-dossier/src/waiting-sessions.ts`); it is evidence
  that the text can be met, not a reading of it.

## Terms introduced / retired

- **Waiting session**: an inventory or review session started before its
  input exists, which obtains its input through its one Syzygy command.
- **Round**: one delivery of a packet to a waiting review session, numbered
  from 1.
- **Continuing reviewer**: a review session whose counted verdict follows an
  earlier round delivered to it, or which declares the session identifier of
  an earlier verdict of its kind.
- Nothing retired.

## Downstream impact

See `IMPACT-LEDGER.md`. In short: three files of one change move, one
generated file and the census are regenerated, `PROJECT-STATUS.md`'s Polaris
figure moves from 244 to 248 scenarios, one test pin moves, and the wait-mode
code becomes conformant only once these bytes are signed.

## Migration / supersession plan

- The v1.2 sign-off is recorded as v1.1 was: the recorder applies the three
  patches through a builder, writes a v1.2 record and aggregate block, and
  `--regenerate` refreshes the union and the census. The v1.0 and v1.1
  records are never edited.
- **The recording tools** (scripts, outside this package, on the branch
  that carries it): `scripts/build_polaris_dossier_local_agent_mode_v1_2.py`
  verifies, applies and tells signed from unsigned v1.2 bytes;
  `record_versioned_signoff.py`'s `real_packages()` carries the entry
  `polaris-dossier-local-agent-mode@1.2`, whose reviewed subject is the
  installed spec with `spec.md.patch` applied; and the v1.1 builder reads its
  own layer once these patches are applied and leaves a later version to the
  v1.2 builder. Once v1.2 is recorded, the battery's existing dossier
  `--check` lines fail unless the tree is the signed v1.1 plus exactly these
  patches and the spec hashes to the digest the v1.2 review read; while v1.1
  is the latest record, a tree carrying these patches fails them.
- **Install-time edits the recorder does not make:** the
  `polaris-dossier-local-agent-mode` row of `openspec/README.md` names the
  v1.2 record (R5 of `check_spec_reconciliation.py --check` requires it);
  `--regenerate` refreshes the union and the census; the recorder's apply
  moves `PROJECT-STATUS.md`'s figure itself.
- The wait-mode code refuses every wait-mode step until a
  `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md` (or later) record exists
  in `decisions/` with the head `record_versioned_signoff.py` writes (title,
  package, version, tag, a 40-hex reviewed commit and a confirming verdict)
  and exactly one marked block for that version in
  `ACCEPTANCE-ACT-RECORD.md`, over a tree that carries the applied, reviewed
  subject: the installed spec names the version in its head and hashes to
  the one `Manifest SHA-256` in the head of the review the record names, the
  comparison the v1.2 builder's signed check makes. A v1.1 run behaves the
  same with the code present, and neither a file that only carries the name
  nor a hand-written head with no review and no applied patch opens
  anything. That gate
  does not lift the direction's order: "The code may merge only once version
  1.2 is signed off". The proposed order is review, sign-off, recording,
  then merging the code.

## Review

Fresh-context review rounds on the default model, at most three, under
`REVIEW-BRIEF.md`. Raws are stored verbatim under `docs/reviews/` as
`R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-2-<n>-RAW.md`.
