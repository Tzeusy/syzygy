# Owner decision packet — Polaris dossier local-agent mode, version 1.2

> **Candidate — binds nothing.** Drafted 2026-10-09 under the owner
> direction `POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08`. It performs no act
> and carries no phrase. Effect comes only from your version-tagged sign-off
> of the exact reviewed bytes, after a confirming review. A commit, a review
> or a merged pull request performs no act.

## What this is, in one paragraph

On 2026-10-08 (UTC; 2026-10-09 your time) you chose option B for the dossier hand-offs: the helper
sessions start at the beginning of a run and wait for their packets, and
one reviewer may continue across revisions if the review page says so. The
signed version 1.1 says each helper session gets its input when you start
it, so the code that does option B cannot be used until the specification
says otherwise. Version 1.2 says it, and nothing else.

## What 1.2 changes, in plain terms

- **Start everything at once.** At the start of a run Syzygy can print a
  command for the inventory session and for each reviewer. You start them
  when you like, and walk away. Syzygy still starts none of them, and
  neither does the authoring session.
- **Waiting is one command, bounded and local.** Each waiting session runs
  one Syzygy command that looks in its own folder for its packet, gives up
  after a few minutes (never past the run's deadline) and asks to be run
  again. It never touches the network. When a packet arrives it checks the
  packet against the fingerprint Syzygy recorded, and refuses if they
  differ.
- **Delivery re-checks the gates.** Syzygy drops a packet into a waiting
  reviewer's folder only after checking the run's gates again, including
  the per-project provider statement for that reviewer's own tool. A
  delivery cannot switch the reviewer's tool or model.
- **Narrow pre-approval, as you took with the option.** The printed Claude
  Code command lets the session read its own folder (the inventory session
  also reads the clone) and run its one Syzygy command, and nothing else
  without asking: read tools plus that one command, as your option said. It
  writes no file. It hands its inventory or verdict to its one command, and
  Syzygy writes that one file in the session's folder and checks it. For
  Codex, Syzygy cannot tell
  how narrow a pre-approval would be, so it prints none and says so; a
  waiting Codex session asks before each step.
- **A reviewer may continue; the page says so.** The same reviewer may look
  at the repaired draft as its next round. Every counted review on the
  review page now says whether its reviewer had seen an earlier round, and
  that such a reviewer has seen its own earlier verdict, which may anchor
  the next one. A repair still retires the old verdict as before.
- **What stays a claim, not a fact.** That a session read the packet
  unaltered, that you used the printed command, that the agent tool applied
  the pre-approval as printed, and whether a reviewer continued, all rest on
  files the sessions can write, so each is shown as Inferred.

Not changed: who may start a session (you, never a subagent or a headless
session the author starts); the execution rule (no waiting session may build
or run the project); the review packet; the rule that a revision retires old
verdicts.

## The cost you accepted with option B

A pre-approved waiting session reads untrusted text, from the clone or its
packet, while nobody is watching, and a sentence in its prompt saying that
text is data does not stop a session that obeys injected text. The narrow
pre-approval limits what such a session can do without asking you: read its
folder (and, for the inventory, the clone) and run its one command. It cannot
write a file, and it cannot build or run the project. Whether the agent tool enforces the printed rules exactly is
something Syzygy cannot see.

## The question

### Sign off version 1.2?

- **(a) Sign off 1.2** as reviewed. Recommended: it is the text of the
  direction you gave, and the code is ready behind it.
- **(b) Not now.** Version 1.1 stays in force; the wait-mode code stays
  switched off (it refuses every waiting step until a v1.2 sign-off record
  exists), and runs keep stalling at each hand-over.

The tool that records 1.2 is ready on the same branch: a builder that applies
these patches and its entry in the sign-off recorder. It changes no text you
sign. Once 1.2 is recorded, the battery fails unless the installed files are
exactly the reviewed 1.2 bytes; your version-tagged sign-off is still the only
thing that makes 1.2 binding.

## If you agree with the recommendation

"1.2 signed off."

## Where the evidence is

- The change: `SEMANTIC-DELTA.md`; what it touches: `IMPACT-LEDGER.md`;
  the review brief: `REVIEW-BRIEF.md`; all in this directory, with the exact
  edits under `proposed/`.
- Your direction:
  `.syzygy/governance/decisions/POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`.
- The reviews of 1.2:
  `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-2-<n>-RAW.md`,
  retained by the lead.
