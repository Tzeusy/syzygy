# One-command Polaris dossier run

> **Candidate — binds nothing.** Drafted 2026-10-14 from the owner's request
> in an operator session, not yet recorded as an owner direction (packet Q0).
> It is not adopted, performs no act, and grants no read, egress, write,
> launch or execution. Effect comes only from owner acts over exact reviewed
> bytes; `OWNER-PACKET.md` in this directory lists them. Tracking bead:
> `syzygy-zwja`.

**The operator should run one command and get a dossier.** Today a Redis
dossier takes at least four operator-started sessions and a hand-over at each
stage. The first operator-agent run against Redis
(`run-e8b77d72780cc48f4dd032267d963d93`, briefed 2026-10-08) expired with no
inventory because the inventory session started about eleven hours after the
brief, past a three-hour deadline [Observed: that run's `run.json`, deadline
`PT3H`, pinned 2026-10-08T01:52Z; inventory session opened 16:22Z].

## Why

**Warrant (pending):** the owner's words in an operator session on
2026-10-14, to be recorded as a plain owner direction before any review of
these bytes counts (packet Q0):

> "The UX is pretty important here; a user of syzygy shouldn't have multiple
> start-stop episodes when trying to generate Polaris for a repository. In
> fact, ideal case is that the calling of the syzygy polaris binary
> implicitly calls all relevant CLI calls inside; with the independence
> requirements etc. settled within the syzygy workflow, and the user only
> ever runs one command"

And, on how independence could be kept without the operator starting each
session:

> "I don't agree that there's no way to make this subagent fully
> independent? e.g. a bash script with the exact instructions calling the
> claude or codex CLIs (so a subagent but not via harness)?"

What stands in the way today [Observed unless marked]:

- **REQ-polaris-generation-035** requires each inventory and review session
  to be "a separate top-level agent session that the operator starts", and
  accepts only two launch forms, a new terminal or the shell-escape prefix.
  `packages/polaris-dossier/src/inventory.ts` hard-codes
  `LAUNCH_FORMS = ['terminal', 'bang']`.
- **The waiting-sessions direction** (`decisions/POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`,
  2026-10-08) says "**No Syzygy-launched sessions.** Syzygy starts, resumes
  and signals no session", and keeps the 2026-10-03 direction's item 2: "the
  product still coordinates no agents". The owner chose option B over
  option D (Syzygy launches) in `DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`.
- **The scope-review direction** of 2026-10-05, item 2, puts the fidelity
  review in "a separate top-level session that the operator starts".
- **Independence is declared, not enforced.** Every session runs as the same
  operating-system user, so any session can write another's directory and the
  gate records; REQ-033 says "no separate operating-system user or sandbox is
  required", and the code discloses this as `RECORDS_WITHIN_REACH`. Who
  started each session is the operator's declaration, labelled Inferred.

The doctrine does not stand in the way. Vision says Syzygy "harnesses the
existing actuator toolchain to close it" and that the "orchestration tools
remain the mechanisms; Syzygy integrates them" (`doctrine/vision.md`), and
the loop stays human-triggered: the operator's one command triggers it.

## What changes

Five added requirements to `polaris-generation`, all in a new *launched*
form of the operator-agent mode, taken only when the operator starts a run
with the one command:

- **040, one-command run.** `syzygy polaris <url>` runs preflight, the
  one-commit clone, `init`, `brief`, the authoring session, the inventory,
  `check` and `inventory-check`, both reviews, `render` and `close`, and
  stops only at a refusal, a question for the operator, the deadline, the
  operator's stop, or a rendered and closed dossier. Re-running it with the
  run's identifier resumes the run. The existing `syzygy dossier` commands
  and the operator-started flow are unchanged.
- **041, Syzygy-launched sessions.** Syzygy, not the authoring session and
  not the operator, starts each session (authoring, inventory, fidelity
  review, design review) as a sibling process of its own supervisor, from
  its fixed prompt, in that session's directory, using the agent tool the
  operator declared. A new launch form, `syzygy-launched`, is recorded from
  what Syzygy itself did (process, command digest, directory, start, exit),
  labelled Observed. The authoring session cannot start, signal or feed a
  helper session; packets still pass only through Syzygy.
- **042, session isolation.** Each session runs inside a file-system view
  Syzygy builds for its role: the clone read-only, its own directory
  writable, the Syzygy checkout (gate records included) read-only, and every
  other session's directory and the run's state directory absent. Syzygy
  refuses a launched run where it cannot build that view. This is a
  separation of the sessions from each other and from the gate records; it is
  not a containment of observed code and changes nothing under SEC-3.
- **043, one attended view.** The operator watches and answers every session
  from one terminal view, can detach and reattach, and can stop the run;
  every question any session or Syzygy asks surfaces there.
- **044, launched runs execute nothing.** A launched run carries the
  no-execution rule of SEC-3 in every brief; Syzygy refuses `allow-execution`
  for it, because the D9 text says "Syzygy never gives the instruction to a
  session it started" (`doctrine/security.md`).

Each added requirement names the predecessor text it displaces for launched
runs and edits no byte of REQ-033 to 036.

## Scope and preserved boundaries

- **The operator-started flow stays.** Runs started with `syzygy dossier
  init` keep REQ-035 exactly, launch forms `terminal` and `bang` included.
- **Syzygy still makes no model-provider call itself.** It launches the
  operator's own agent tool under the operator's account; whether that launch
  keeps the agents' transmissions the operator's own act is packet Q2.
- **No execution, no sandbox claim for observed code.** Launched runs are
  reading-only. Execution stays in operator-started runs under D9.
- **No new egress, consent or read.** Admission, screening, checks, packets
  and verdict validation are those of REQ-033 to 036.
- **Out of scope:** remote or multi-host sessions; agent tools other than
  those with a per-project provider statement in force; automatic retries of
  a refused check beyond the declared repair-cycle limit; any change to
  `polaris-dossier-arbitrary-public-repo`.

## Acts this needs before it can bind

1. A plain owner direction recording the request and superseding, for
   launched runs only, the 2026-10-08 "No Syzygy-launched sessions" item, the
   2026-10-03 item 2 as it applies to the product, and the 2026-10-05 item 2
   (packet Q0, Q1).
2. This spec, signed by version tag, after fresh-context review.

The owner packet orders them and recommends answers.

## Capabilities

- **Modified:** `polaris-generation`, by five added requirements (040 to
  044; free at `origin/main` `09c7a61d`, after the arbitrary-repo
  candidate's 037 to 039).
- **New:** none.

## Amendment relation

- It extends the composition of `polaris-manifesto-generation`,
  `polaris-manifesto-understanding-amendment`,
  `polaris-non-governed-narrative-profile` and
  `polaris-dossier-local-agent-mode`. No byte of any of them is edited.
- Whether this belongs in a v1.3 amendment of
  `polaris-dossier-local-agent-mode` instead of a new change is packet Q1;
  this draft follows the arbitrary-repo precedent of a separate change with
  added requirements.
- The candidate spec is held in `proposed/`, not `specs/`, so the
  dependency-union tooling does not count it before an act.
