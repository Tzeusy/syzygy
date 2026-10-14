# Design — one-command Polaris dossier run

> **Candidate — binds nothing.** Design sketch for the five added
> requirements in `proposed/polaris-generation/spec.md`. Where this file and
> the spec disagree, the spec governs.

## Shape

```
operator ── syzygy polaris <url> ──► supervisor (Syzygy, in a tmux session)
                                        │
                ┌───────────────┬───────┴───────┬────────────────┐
                ▼               ▼               ▼                ▼
          bwrap view A     bwrap view I     bwrap view F     bwrap view D
          claude (author)  claude (inv.)    claude (fid.)    claude (design)
                │               │               │                │
                └── files ──► Syzygy steps (check, inventory-check, packets,
                              review-check, render, close) ◄── files ──┘
```

- **One supervisor, sibling sessions.** The supervisor is Syzygy's own
  process. Every agent session is its child and no session is another's
  child (REQ-041). Sessions talk to Syzygy only through files in their own
  directories and the waiting command; Syzygy runs every step itself, in
  the supervisor, never inside a session's view.
- **Prompts are Syzygy's.** Each role's prompt is the fixed text
  `session-prompt` already writes, digest recorded. The authoring session
  never writes a helper's instructions.

## State machine

```
preflight → clone → init → brief → AUTHOR ⇄ check
   → INVENTORY ⇄ inventory-check → freeze
   → FIDELITY (packet → verdict → review-check)
       └─ blocking finding → AUTHOR (new draft revision retires reviews)
   → render → DESIGN (packet → verdict → review-check)
       └─ blocking finding → AUTHOR
   → close → done
any state ── refusal | deadline | limit | stop ──► stopped (resumable unless
                                                  closed or past deadline)
```

- Helper sessions start at `brief` and wait (REQ-035's waiting sessions), so
  the inventory starts in parallel with authoring. That alone would have
  saved the first Redis run.
- `--resume` re-enters at the first unfinished state, re-running that
  state's gates. State lives in the run directory; the supervisor holds
  none it cannot rebuild.

## Isolation (REQ-042)

- **Mechanism:** bubblewrap (`bwrap`), unprivileged user namespaces; no
  root, no new OS user. One view per role, built from a pure function
  `viewFor(role, run)` whose output is hashed into the launch record.
- **Mounts:** `/usr`, `/etc`, the agent tool's install read-only; the
  agent tool's own config and state directory read-write (it needs its
  login and transcripts); the clone read-only; the Syzygy checkout
  read-only; the session's own directory read-write; for the author only,
  the run's draft path read-write. Nothing else from `$HOME` or the state
  root.
- **Network:** shared. The agent tool must reach its provider. Restricting
  destinations is out of scope and disclosed.
- **Probe:** before `init`, build a throwaway view and test read, write and
  listing for each path class; refuse on any failure (Q4).
- **Not a sandbox claim.** It separates sessions from each other and from
  the records; it is not SEC-3 containment, and launched runs execute
  nothing anyway (REQ-044).

Trade-offs considered:

- *Separate OS users per session* — stronger, but needs root to set up and
  breaks the agent tool's login; rejected.
- *Landlock only* — no namespaces needed, but cannot hide paths from
  listing on older kernels and needs a helper to apply; kept as a fallback
  to investigate, not drafted.
- *Containers (podman/docker)* — heavier, image management, and the docker
  socket is itself a privilege; rejected.

## Attended view (REQ-043)

- **tmux**, because detach and reattach come free, it already runs on the
  owner's hosts, and pane contents can be captured independently for tests.
  The supervisor creates session `polaris-<run>` with windows `run`,
  `author`, `inventory`, `fidelity`, `design`, then attaches.
- The `run` window shows the step, deadline left, limits spent, what is
  awaited, and which window holds an unanswered question.
- `syzygy polaris --attach <run>` and `--stop <run>` are the printed
  commands. Stop sends SIGTERM to each session's process group, then
  SIGKILL after a grace period, then records the stop.
- Without tmux: refuse with a reason (a built-in multiplexer is out of
  scope).

## Records and disclosure

- New launch form `syzygy-launched` beside `terminal` and `bang`
  (`inventory.ts`), accepted only in a run whose record says launched, and
  only with a matching launch record.
- Launch record fields per REQ-041, written by the supervisor at spawn and
  exit.
- `RECORDS_WITHIN_REACH` gets a launched variant: records read-only in every
  view, view requested by Syzygy, holding Inferred.
- Pages disclose: launched by Syzygy; which fields are Observed; execution
  not permitted; network unrestricted.

## Implementation slices

Not filed as beads until the owner signs; `syzygy-zwja` tracks the gate.
Ordered by dependency.

1. **Launch records and the third launch form.** `LAUNCH_FORMS`, run-record
   `launched` flag, launch-record schema, `inventory-check` and
   `review-check` acceptance rules, launched disclosures. Unit and
   conformance tests per REQ-041 scenarios 3. *No dependency.*
2. **Session views.** `viewFor(role, run)`, bwrap argv builder, host probe,
   view digest. Probe-matrix tests from REQ-042 using stand-in processes.
   *No dependency.*
3. **Supervisor and launcher.** Spawn the declared agent tool in its view
   from the fixed prompt; process groups; launch records at spawn and exit;
   stop and deadline teardown; `allow-execution` refusal (REQ-044).
   *Depends on 1, 2.*
4. **`syzygy polaris` orchestrator.** The state machine above over the
   existing step functions, one-commit clone, run-limit question, resume,
   final statement in both forms (REQ-040). *Depends on 3.*
5. **Attended view.** tmux session layout, state window, attach and stop
   commands, attached/detached interval recording (REQ-043). *Depends on 4.*
6. **End-to-end fixture battery.** A stand-in agent tool that scripts
   drafts, inventories, verdicts, questions and hangs; every Form block's
   Case run in CI against fixture records; rule-6 mutants per predicate.
   *Depends on 5.*
7. **Docs and skill.** Runbook path "Run L (launched)", the polaris-dossier
   skill's step list, `PROJECT-STATUS.md` rows, `openspec/README.md` row.
   *Depends on 6.*
8. **First launched Redis run.** One attended `syzygy polaris
   https://github.com/redis/redis` at a consented revision, evidence record
   retained. *Depends on 7; closes the motif.*

## Prototype status (2026-10-14)

Slices 1 to 5 exist as a prototype on branch `feat/polaris-one-command-prototype`
(bead `syzygy-1z8m`), under the follow-up of
`POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`. Where it departs from the sketch
above:

- **Process parent.** Sessions run in tmux windows, so each session's parent
  is the tmux server, not the supervisor. The launch record holds the pane's
  process identifier. REQ-041's "child of the supervisor" is not met as
  written; sibling-ness (no session is another's child) is.
- **Command broker.** A session cannot reach the run directory, so its
  `syzygy` command is a shim that forwards to the supervisor over a
  per-session Unix socket (`broker.ts`, `broker-client.ts`). Helpers may run
  only `dossier await` on their own directory; the author only the dossier
  check and run-report commands on its run. This is local IPC beside the "no route" sweep, which
  exempts those two files and checks they listen on a path only.
- **Private agent configuration.** Each session gets its own
  `CLAUDE_CONFIG_DIR` with a copy of the operator's Claude Code credentials,
  so no session can read another's transcripts in `~/.claude/projects`, and
  the operator's hooks, skills and CLAUDE.md do not load in launched
  sessions.
- **Author view.** The run directory read-only and `drafts/` writable, rather
  than "own directory plus draft path".
- **Not built:** question detection in the state window (REQ-043 names the
  pane holding a question), the attached/detached interval record, the
  Observed launch record for the author, slice 6's fixture battery and
  slice 8's Redis run.
