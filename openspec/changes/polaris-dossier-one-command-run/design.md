# Design — one-command Polaris dossier run

> **Candidate — binds nothing.** Design sketch for the six added
> requirements in `proposed/polaris-generation/spec.md`. Where this file and
> the spec disagree, the spec governs.

## Shape

```
operator ── syzygy polaris <url> --clone <dir> ──► supervisor (Syzygy, in a tmux session)
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
preflight → clone check → init → brief → AUTHOR ⇄ check
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
  avoided the reported hand-over delay in the first Redis run [Inferred;
  the external run evidence is Unknown to this repair].
- `--resume` re-enters at the first unfinished state, re-running that
  state's gates. Every new session, on resume or otherwise, repeats the
  full host and runner checks of REQ-042, 044 and 045 before it starts. A
  helper starts before delivery, even when its input already exists. State
  lives in the run directory; the supervisor holds none it cannot rebuild.

## Isolation (REQ-042)

- **Mechanism:** bubblewrap (`bwrap`), unprivileged user namespaces; no
  root, no new OS user. One view per role, built from a pure function
  `viewFor(role, run)` whose output is hashed into the launch record.
- **Mounts:** `/usr`, `/etc` and the agent tool's install, read-only. A
  private configuration home per session, read-write, holds only the copied
  credential file and the tool's own state for that session; the operator's
  own configuration directory is never mounted. The author and inventory
  views mount the clone read-only; review views do not mount it. No view
  mounts the Syzygy checkout or its gate records. Each view gets only a
  minimal command shim; role commands cross its local broker to the
  supervisor outside the view. The shim imports no checkout content, and
  broker output is subject to the same delivery-class gate as a packet.
  Each helper's own directory is read-write. The author works in the run's state directory, read-only, with `drafts/`
  read-write. Nothing else from `$HOME` or the state root.
- **Network:** shared at the operating-system level, because the agent tool
  must reach its provider. No session is given a tool that reaches anything
  else: no general shell, no web fetch or search, and no network-opening MCP
  server (REQ-045). The tool's own auxiliary telemetry, error reporting and
  update checks must be disabled by controls observed for that executable
  and version; absent or unobserved controls refuse even its login-status
  invocation. Network destinations remain unrestricted at the OS level,
  and that the tool opened nothing else for its whole life is Inferred.
- **Probe:** before `init` and every session start, replacements and resume
  included, build a throwaway view and test read, write and listing for each
  path class; refuse on any failure (Q4). The mounted-ancestor check also
  refuses an installation or system mount exposing the checkout or a
  forbidden state path.
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

## The agent CLI runner (REQ-045)

- **The executable comes from the declaration.** The operator declares the
  tool's absolute path, its version and its provider. Syzygy checks all
  three before `init` and again before every session start, replacement
  and resumed starts included, and never resolves a binary from `PATH` or
  the environment.
- **Settings isolation**, per tool, comes from the flag evaluation kept with
  the reviewed candidate
  (`.syzygy/governance/contracts/candidates/dossier-local-cli-subprocess-runner/SEMANTIC-DELTA.md`,
  "Settings isolation: the flags evaluated"). For Claude Code that means
  `--restricted` or `--setting-sources` with `--strict-mcp-config`, a
  private configuration home holding only the copied credential file, and
  never `--bare`, which forces key-only authentication. For Codex it means
  `--ignore-user-config` and `--ignore-rules`. Every exclusion stays
  unobserved, and refuses the run, until an operator-started attended probe
  outside a launched run observes the real tool and version enforcing it
  against synthetic fixtures. A stand-in establishes only the runner
  invocation and refusal. No probe is run by this candidate repair.
- **Managed settings** are read only for their provider-relevant keys, by
  name. A key that redirects the provider, or authenticates by anything
  other than the credential file, refuses the run.
- **Login and launch checks.** Before every session start, the tool's own
  login-status command runs inside the view, after the auxiliary controls
  and their real-tool evidence are checked. The runner also re-checks the
  executable digest and version, managed settings, exclusions, tool limits,
  fixed permissions and host view at each start. `HOME` and the declared
  tool's `CLAUDE_CONFIG_DIR` or `CODEX_HOME` select only the private
  configuration home Syzygy sets; none is inherited. Permission controls
  must deny widening while attached as well as detached; `dontAsk` is only
  a candidate until observed, and enabling bypass as an option is forbidden.

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
- `RECORDS_WITHIN_REACH` gets a launched variant: Syzygy checkout and gate
  records absent from every view; the author's state path read-only except
  `drafts/`; view requested by Syzygy; holding Inferred.
- Launching-step output labels its own launch fields Observed as it makes
  the launch. Every later display from a stored record labels those fields
  Inferred, including view digests, login and managed-settings checks and
  controls. Pages also disclose execution not permitted and OS network
  destinations unrestricted.

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
   existing step functions, the check of the operator's `--clone`, run-limit
   question, resume with repeated launch checks, final statement in both forms (REQ-040). *Depends on 3.*
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
   https://github.com/redis/redis --clone <operator-prepared-dir>` at a
   consented revision, only after the real-tool evidence and every other
   gate passes; evidence record retained. *Depends on 7; closes the motif.*

## Prototype limitations (historical prototype, reviewed in round 2)

The 2026-10-14 draft reports slices 1 to 5 as a prototype on branch
`feat/polaris-one-command-prototype`
(bead `syzygy-1z8m`), under the follow-up of
`POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`. The departures below include the source observations retained in
`docs/reviews/R-POLARIS-DOSSIER-ONE-COMMAND-RUN-2-RAW.md`. These limitations
are not a claim that this repair exercised the prototype:

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
  intended to separate transcripts in `~/.claude/projects` and ambient
  configuration. A private home alone does not establish the hook, skill
  or instruction exclusions REQ-045 requires.
- **Author view.** The run directory read-only and `drafts/` writable, rather
  than "own directory plus draft path".
- **Agent executable from the environment or `PATH`.** `claudeExecutable()`
  honours `SYZYGY_POLARIS_AGENT` and otherwise resolves `claude` from `PATH`
  (`command -v claude`). REQ-045 forbids both: the executable is declared by
  absolute path.
- **Automatic approval.** Every session starts with `--permission-mode auto`.
  REQ-045 forbids automatic-approval modes.
- **Author tool limits absent.** The prototype gives the author
  `--allowedTools` entries but no `--tools`, `--disallowedTools` or
  `--strict-mcp-config`. It retains the default general Bash, WebFetch,
  WebSearch and ambient MCP, gated by auto mode. Each helper's allowed
  Bash is also a general shell. Neither is the restricted command runner
  of REQ-044 and 045.
- **Checkout exposure.** The prototype mounts the Syzygy checkout read-only
  in every view; REQ-042 now excludes it and its gate records entirely.
- **Auxiliary traffic and repeated checks.** The prototype is not evidence
  of the per-version controls or the full checks before every replacement
  and resumed start required here.
- **Prompt as an argument.** The role prompt goes on the command line as a
  positional argument, not as an instructions file the command line names.
- **Typing into the author's pane.** Syzygy sends messages to the authoring
  pane with `tmux send-keys`. REQ-043 and REQ-045 forbid typing or pasting
  into a session's terminal.
- **Syzygy fetches the clone.** The prototype runs a one-commit
  `git fetch` itself. REQ-040 now requires the operator's own clone, given
  with `--clone`, because no act covers a Syzygy-made fetch.
- **Hard-coded declarations.** `agentProvider: 'anthropic'` and
  `operatorIsOwner: true` are written into the run configuration rather than
  declared by the operator.
- **Bypass mode.** The authoring session can be started with
  `--dangerously-skip-permissions` (`state.authorSkipPermissions`). REQ-045
  forbids every bypass mode.
- **No settings-source flag.** The prototype relies on its private home
  alone and passes neither `--setting-sources` nor `--restricted`.
- **Not built:** question detection in the state window (REQ-043 names the
  pane holding a question), the attached/detached interval record, the
  launch record for the author with REQ-041's live/stored labels,
  slice 6's fixture battery and slice 8's Redis run.
