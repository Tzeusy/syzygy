# Owner decision packet — Polaris dossier local-agent mode, version 1.1

> **Candidate — binds nothing.** Drafted 2026-10-06 under bead
> `syzygy-qkea.1`. It performs no act and carries no phrase. Effect comes
> only from your version-tagged sign-off of the exact reviewed bytes, after
> a confirming review. A commit, a review or a merged pull request performs
> no act.

## What this is, in one paragraph

You signed off version 1.0 of the dossier local-agent mode on 2026-10-06,
right after adopting D9. Round 3 of its review left notes that 1.0 carried
as implementation duties or as lines for a later amendment, and D9's review
left one more that was routed to the dossier specification. Version 1.1 writes those into the
specification itself, so a build that skips them no longer conforms. It
adds no new permission. One further change, which only you can accept, is
drafted separately (question 2).

## What 1.1 changes, in plain terms

- **Credentials.** Once Syzygy has issued a brief that lets an agent build
  and run a project, it must never again keep a typed-adapter credential
  where your user account can read it. It checks this at every step of the
  run, not only at check and close, and says plainly that it cannot see
  what happens between steps. Today Syzygy holds no such credential, so
  this costs nothing yet. This is how D9's note N2 recommends you read
  D9's credential condition (question 3).
- **Your declaration.** Before Syzygy issues a brief that permits running
  the project, `syzygy dossier allow-execution` records that you started the
  authoring session on your own machine and are attending it. No
  declaration, no permission. The page shows it as your word, not something
  Syzygy saw.
- **D9's cost, quoted.** The run record quotes D9's bullet "What the
  permitted case costs" word for word, instead of a shortened paraphrase
  that left out the parts about reaching credentials and having no
  containment.
- **Who can type the choice.** The specification now says plainly, for you
  as its reader, that the agent, which runs the neighbouring commands, could
  run `allow-execution` itself or write its record, and that only the skill
  and agent instructions forbid it. The rendered page does not repeat that
  sentence; it goes on showing who ran the command, that you are the owner,
  and your declaration, each as your word rather than something Syzygy saw.
- **When running is not permitted.** The brief quotes SEC-3's adopted first
  sentence and then tells the agent, in plain words, not to build or run the
  project outside an execution profile. Version 1.0 asked it to quote a
  sentence SEC-3 no longer has.
- **Not an execution consent.** Your per-run choice is never treated, stored
  or shown as the per-project execution consent the base rules define, and
  approves no execution profile.
- **Where the gate answers come from.** Syzygy decides whether your consent,
  the registry entry, the policy acts, any per-project statement, D9 and your
  RFC7-20 reading are in force by reading the record of your act, never a
  status word or a file being there. The page also says that the records it
  reads for these gates sit where the agent sessions can write.
- **The skill never grants running.** The `/polaris-dossier` skill and the
  Codex instructions only point to the run's brief. Without a brief they say
  not to build or run the project.
- **Wording fixes.** A scenario that said "adopted capability declaration"
  now matches the rule ("adopted or not"); the proposal lists everything 1.0
  modifies in effect; the skill's description says "any repository you hold
  the consents for", not "a public repository".
- **Status sentences.** The specification, proposal and design still said
  "candidate, binds nothing", "not adopted" and "drafted as D9", and the
  proposal still said the specification sat in `proposed/`. 1.1 says what is
  true: version 1.0 signed off, D9 adopted, these bytes binding only when you
  sign off 1.1. The task checklist keeps its old head; it is not
  specification text. This one was not in the review notes; drop it if you
  prefer, and nothing else changes.

Not included: round-3 finding 6, which applied only if you had declined
D9's credential condition. You kept it.

## The questions

### Question 1 — sign off version 1.1?

Options:

- **(a) Sign off 1.1** as reviewed (with or without question 2's hunk,
  depending on your answer there). Recommended.
- **(b) Not now.** Version 1.0 stays in force; the implementation goes on
  against 1.0, carrying these items as duties as it already does.

Recording 1.1 needs a small tool change first (a builder that applies these
patches, and its entry in the sign-off recorder); that is implementation
work after your answer and changes no text you sign. Until it exists, no
check in the battery can tell 1.0's signed bytes from 1.1's: your
version-tagged sign-off is the only thing that makes 1.1 binding.

### Question 2 — D9 note N6: flag commands outside the named scope?

D9 says your per-run choice "names what the instruction covers". That
limits what Syzygy tells the agent, not what the agent does: under D9, a
session that runs more than the named scope does not break SEC-3. Syzygy
still labels everything resting on the run Inferred and lists every command.

The note asks whether the run record should also compare each reported
command with the named scope and flag the ones outside it, so overreach is
visible rather than forbidden.

The drafted hunk, if you take it: where running was permitted, the brief
asks the agent to report, for each command, where it ran it and whether it
was in scope, and a draft missing either is still admitted. Syzygy flags any command reported outside the
clone, with no location, or called out of scope by the agent. A flag blocks
nothing and hides nothing. It cannot catch an out-of-scope command the agent
ran inside the clone and called in scope, because Syzygy cannot see the
commands, only the agent's report of them.

- **(a) Take the hunk.** Recommended by D9's notes, in keeping with your
  choice of disclosure over containment.
- **(b) Leave it out.** Commands are still listed; nothing is flagged.

### Question 3 — D9 note N2: for how long is the credential condition kept?

D9's condition 4 holds "for as long as any of them runs". Syzygy cannot
see which processes a session started, and code can set itself up to
restart later. So once any permitted run has happened, the only way to be
sure is to keep adapter credentials unreadable by your user account from
then on.

- **(a) Accept it as a standing cost** (recommended). It costs nothing today;
  once Syzygy holds a credential, it is kept from your user account
  permanently. Version 1.1's credential sentence is written this way.
- **(b) Rule otherwise.** Then 1.1's credential sentence no longer matches
  your ruling. Hold 1.1 (question 1 (b)) and it is redrafted to your
  ruling and reviewed again.

### Question 4 — D9 note N1: what counts as "one run"?

D9 records a choice "for that one run" without defining a run. A feature
that called a long-lived job one run could come close to the standing
approval you ruled out. The dossier already bounds it: the choice covers
one run, its pinned revision, and building and running the project from
that run's authoring session.

- **(a) Leave the definition to each feature's specification** (recommended),
  each required to bound a run by one session, a named scope and an end.
- **(b) Define it in doctrine.** That is new doctrine text with its own
  review, and does not change 1.1.

## If you agree with every recommendation

"1.1 signed off with N6; N1 and N2 as recommended."

## Where the evidence is

- The change: `SEMANTIC-DELTA.md`; what it touches: `IMPACT-LEDGER.md`;
  the review brief: `REVIEW-BRIEF.md`; all in this directory, with the exact
  edits under `proposed/`.
- The notes it carries: `POLARIS-DOSSIER-LOCAL-AGENT-MODE-REVIEW-NOTES.md`
  and `DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md`, one directory up.
- The reviews of 1.1: `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-<n>-RAW.md`,
  retained by the lead.
