# One-command Polaris dossier run

Candidate exact behavioral delta; not adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds six requirements to the operator-agent mode of REQ-polaris-generation-033 to 036, in a *launched* form of that mode taken only when the operator starts a run with the one command: the one-command run (040), Syzygy-launched sessions (041), session isolation (042), one attended view (043), no execution in launched runs (044) and the local agent CLI subprocess runner (045), which fixes how Syzygy starts the operator's own `claude` or `codex` binary for every session. REQ-polaris-generation-045 was reviewed as a separate candidate in five rounds and is folded in here. REQ-polaris-generation-041, 042 and 045 state one set of working directories, writable paths and configuration homes for each role. It edits no byte of any predecessor requirement or scenario. For a launched run each added requirement names the predecessor text it displaces; every other sentence and scenario of REQ-polaris-generation-033 to 036 applies unchanged. A run started with `syzygy dossier init` is not a launched run, and none of these requirements applies to it.

## ADDED Requirements

### Requirement: One-command run

The operator-agent mode SHALL offer one command, `syzygy polaris <url>`, that takes a repository URL, the operator's own clone of it given with `--clone`, and the run limits of REQ-polaris-generation-033 (as options or, where absent, from one question the command asks before anything else) and carries the run through these steps, those REQ-polaris-generation-033 to 036 name with the launches of REQ-polaris-generation-041 and 045, in this order: preflight; the check of the operator's clone, as `init` checks it; `init`; `brief`; the authoring session with its draft and `check` loop; the inventory session and `inventory-check`; the fidelity review and its validation; `render`; the rendered-design review and its validation; and `close`. A run so started is a *launched run*, and the run record SHALL say so from the moment `init` writes it. Syzygy SHALL make no clone or fetch of the repository itself: the clone is the operator's own act, made before the command, and the command SHALL refuse when no `--clone` is given, naming the clone the operator is to make, because no act in force covers Syzygy acquiring a repository over the network.

The command SHALL stop only at one of these, and SHALL state which in human and machine form: a refusal by any step, with the step and its reason exactly as that step reports them; a question for the operator that the operator declines to answer; the run's declared deadline or token or turn limit; the operator's stop (a session that reaches its time bound under REQ-polaris-generation-045 counts as no result, and the step that needed its result refuses); or a closed run with its rendered dossier, naming the site directory and the run record. Running `syzygy polaris --resume <run>` SHALL continue a launched run from its first unfinished step, re-running every gate that step requires and, before each session start, every launch check of REQ-polaris-generation-042, 044 and 045, and SHALL refuse a run that is not a launched run, a closed run, and a run past its deadline.

Every check, freeze, packet, validation, refusal, label and disclosure SHALL be that of REQ-polaris-generation-033 to 036, of this requirement and of REQ-polaris-generation-041 to 045; the one command itself adds no step that decides readiness and removes none.

ID: REQ-polaris-generation-040
Source: VIS-1; governing warrants below.
Scope: v1-mandatory

#### Scenario: One command to a closed run

- **WHEN** the operator runs `syzygy polaris <url> --clone <dir>` with the operator's own clone of a repository whose gates are in force, answers the run-limit question, and every check and review passes
- **THEN** the run reaches `close` with no further command typed by the operator, and the command ends naming the site directory and the run record
- **AND** the run record lists, in order, every step of REQ-polaris-generation-033 to 036 that ran, with its outcome

#### Scenario: Refusal stops the run

- **WHEN** any step refuses, including preflight missing a gate, the command given no `--clone`, `init` refusing the clone, or `check` refusing past the repair-cycle limit
- **THEN** the command stops at that step, prints that step's own refusal and reason unchanged in human and machine form, and starts no later step
- **AND** no session the run launched is left running

#### Scenario: Resume after a stop

- **WHEN** the operator stops a launched run after the draft passes `check` and before the inventory is checked, and then runs `syzygy polaris --resume <run>` before the deadline
- **THEN** Syzygy re-runs the gates of REQ-polaris-generation-033, keeps the frozen draft revision, and continues at the inventory step
- **AND** resuming a run started with `syzygy dossier init`, a closed run, or a run past its deadline is refused with the reason

#### Scenario: Operator-started runs unchanged

- **WHEN** the operator starts a run with `syzygy dossier init` and hands sessions over with `session-prompt`
- **THEN** the run is not a launched run, REQ-polaris-generation-035 applies to it exactly, and `terminal` and `bang` remain its only launch forms

Form: event-response.

- **Case:** Run the command against fixture repositories and fixture gate records, with and without `--clone`, under a network observation, with a stand-in agent tool whose behaviour each case scripts (passing draft, failing draft, failing inventory, blocking finding, question, hang, a session past its time bound), varying the gates, the clone, the limits, the stop point and the resume point.
- **Observable:** The steps run and their order, each step's outcome and refusal text, the command's final statement in both forms, the run record, the processes alive after the command ends, and any network connection Syzygy's own processes open.
- **Oracle:** The step sequence, stop points and refusal texts expected from the fixture records and the scripted agent behaviour, written before the run; process liveness from an independent process listing.
- **Oracle independence:** Expected sequences and texts are written outside the code under test; liveness comes from the operating system's process table, never Syzygy's record.
- **Falsifier:** The command makes a clone or fetch of the repository itself, or runs without `--clone`; skips, reorders or adds a readiness-deciding step beyond those of REQ-polaris-generation-041 to 045; continues past a refusal; changes a step's refusal text; leaves a launched session running after it ends; resumes a run that is not launched, is closed or is past its deadline; or treats a `syzygy dossier init` run as launched.

```yaml
warrants:
  primary: VIS-1
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, SEC-2, SEC-3]
  contracts: [RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05, POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08]
  topology: []
  parent_requirements: [REQ-polaris-generation-033, REQ-polaris-generation-034, REQ-polaris-generation-035, REQ-polaris-generation-036]
```

### Requirement: Syzygy-launched sessions

In a launched run Syzygy SHALL start every agent session of the run, the authoring session and the inventory, fidelity-review and rendered-design-review sessions, itself: each as a child of the run's supervisor process and never of another session, from the fixed prompt Syzygy writes for that role and records by digest, in the working directory REQ-polaris-generation-042 gives its role, with the agent tool, version and model the operator declared for the run. Each helper session, including a fresh session started on resume, SHALL be started before its input is delivered to it and SHALL obtain its input only through the waiting command of REQ-polaris-generation-035; Syzygy SHALL deliver packets exactly as that requirement states. No session SHALL be able to start, resume, signal or write input to another session through Syzygy; Syzygy SHALL expose no command or file by which the authoring session causes a helper session to start or receive input.

For each launched session the run record SHALL record the launch form `syzygy-launched` and: the role; the agent tool's executable path and the digest of the full command line Syzygy ran; the session directory; the isolation view of REQ-polaris-generation-042 by digest; the process identifier; the start instant; and the exit instant and status, or that the run stopped it. Syzygy SHALL label each of these Observed only in the output of the step that makes the launch, as it makes it, because Syzygy itself did each; wherever a later step or page shows them from the stored launch record they SHALL be labelled Inferred, as REQ-polaris-generation-033 requires of a value read from a stored record, and this requirement displaces no part of that rule. The session identifier each session declares, the model the provider actually served, and that the context was fresh SHALL remain Inferred. An inventory or verdict from a launched run SHALL count only when its session's launch record exists and names that session's directory; Syzygy SHALL refuse a declared `terminal` or `bang` launch form in a launched run.

For a launched run this requirement displaces exactly this predecessor text of REQ-polaris-generation-035: "a separate top-level agent session that the operator starts", read as "a separate session that Syzygy starts under this requirement"; "the operator starts each such session as above, and neither Syzygy nor the authoring session starts, resumes or signals it", read as "Syzygy starts each such session under this requirement, and the authoring session neither starts, resumes nor signals it"; "its launch form, which is a new terminal or the shell-escape prefix, as the operator declares it", read as "its launch form, `syzygy-launched`, as Syzygy recorded it"; "each is labelled Inferred and attributed to whoever declared it. Syzygy SHALL refuse an inventory or verdict whose declared launch form is neither, and neither SHALL count until its launch form is declared.", read as "each is labelled Inferred and attributed to whoever declared it, except the launch form, which is labelled as REQ-polaris-generation-041 states. Syzygy SHALL refuse an inventory or verdict that has no `syzygy-launched` launch record naming its session directory, and neither SHALL count until that record exists."; among what remains Inferred, "that each session was a top-level session the operator started, in the launch form declared, and not a subagent or process of the authoring session", which for a launched run rests on the launch record and is labelled as that record is; and, in the waiting-session rules, "The command Syzygy prints for a waiting session" and "the printed command", each read as "the command line Syzygy runs for the launched session", so that the pre-approval and tool limit stated there bind it, with the refusal of REQ-polaris-generation-045 in place of "where the agent tool offers no rules that narrow, Syzygy SHALL print no pre-approval and SHALL say so"; and "Syzygy SHALL print its command for a new terminal only", read as "Syzygy SHALL run its command for the launched session itself, not print a command for the operator to start". The rule that a subagent or a process of the authoring session SHALL NOT satisfy the inventory or a review is unchanged.

ID: REQ-polaris-generation-041
Source: VIS-3; governing warrants below.
Scope: v1-mandatory

#### Scenario: Four sessions launched by Syzygy

- **WHEN** a launched run issues its brief
- **THEN** Syzygy starts the authoring, inventory, fidelity-review and design-review sessions, each in the working directory of its role from its own fixed prompt, each a child of the supervisor
- **AND** the run record holds a `syzygy-launched` launch record for each, labelled Observed in the launching step's output and Inferred wherever a later step or page shows it, and the review page discloses which fields are which

#### Scenario: Authoring session tries to reach a helper

- **WHEN** the authoring session runs any Syzygy command, or writes any file it can reach, intending to start, signal or give input to a helper session
- **THEN** no helper session starts, receives input or is signalled as a result
- **AND** a helper's input is only what Syzygy delivered under REQ-polaris-generation-035, matching its recorded digest

#### Scenario: Inventory without a launch record

- **WHEN** an inventory or verdict is submitted in a launched run for a session directory that has no `syzygy-launched` launch record, or with a declared launch form of `terminal` or `bang`
- **THEN** Syzygy refuses it and it does not count
- **AND** readiness names the inventory or review still required

Form: event-response.

- **Case:** Run launched runs with a stand-in agent tool that records its own parent process, working directory and argv; script the authoring stand-in to attempt every route it can reach to start, signal or feed a helper; submit inventories and verdicts with and without launch records and with each declared launch form.
- **Observable:** The process tree, each stand-in's recorded parent, directory and argv, the launch records, deliveries and their digests, and the counted and refused submissions.
- **Oracle:** The process tree and argv expected from the fixed prompts and declared tool, written before the run; a helper's expected inputs are only the packets the fixture dictates.
- **Oracle independence:** Parentage and argv come from the stand-in's own record and the operating system's process table, not from Syzygy's launch record.
- **Falsifier:** A session is a child of another session; a helper starts, receives input or is signalled because of the authoring session; a launch record is missing or disagrees with the process table; a submission without a launch record, or with `terminal` or `bang`, counts in a launched run; a later step or page shows a stored launch record as Observed.

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-2, VIS-3, VIS-4, SEC-3]
  contracts: [RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05, POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08]
  topology: []
  parent_requirements: [REQ-polaris-generation-006, REQ-polaris-generation-035]
```

### Requirement: Session isolation

In a launched run Syzygy SHALL start every session inside a file-system view it builds for that session's role before the session's process starts, so that the session and every process it starts can reach only: for the authoring session, the clone read-only, the run's state directory read-only as its working directory, and the run's `drafts/` path read-write; for the inventory session, the clone read-only and its own directory read-write as its working directory; for each review session, its own directory read-write as its working directory; for every session, the agent tool's installation read-only, the session's private configuration home of REQ-polaris-generation-045 read-write, a minimal Syzygy command shim read-only, and the system paths a process needs to run, read-only. The Syzygy checkout, its gate records and the operator's own configuration directory for the agent tool SHALL NOT be in any view, by any alias or mounted ancestor. The shim SHALL carry only the protocol needed to submit its role's allowed commands to the supervisor outside the view; it SHALL carry no checkout content or gate record and SHALL load neither from the checkout. Instructions and named guidance of REQ-polaris-generation-045 SHALL be supplied only as the explicit role files inside the session's own directory or private configuration home, never by mounting the checkout. No session SHALL be able to read or write another session's directory, the run's state directory, or the run's `drafts/` and `checks/` paths other than as stated. A command a session asks Syzygy to run on its behalf, outside its view, SHALL be refused unless it is one the session's role is allowed and names no path, file or option that would reach beyond that session's view; Syzygy SHALL NOT run such a command in a form that copies content from outside the view into a path the session can read; a delivery Syzygy makes under REQ-polaris-generation-035, of a packet it built and recorded by digest, is not such a copy. Network access SHALL be left to the agent tool's own connection to its declared provider: REQ-polaris-generation-045 gives no session a tool that reaches any other destination and requires observed controls that disable the agent tool's auxiliary network traffic before it is invoked. Syzygy SHALL disclose that it does not restrict network destinations at the operating-system level; the controls it applied are labelled under REQ-polaris-generation-045, and that the tool opened no other connection for its whole life is Inferred, never a claim of network containment.

Before `init`, and again before every session start, including a replacement session and a start on resume, Syzygy SHALL check that it can build that role's view on the host. It SHALL refuse the run where it cannot, naming what is missing, and where a path the view forbids to that role lies inside a path the view mounts (such as a state root or the Syzygy checkout inside the agent tool's installation or a system mount), naming both paths; it SHALL NOT start a launched session without its view. The run record SHALL record each view by digest of its full specification as the view Syzygy requested. That requested-view value SHALL be labelled Observed only in the output of the launching step as it makes the launch, and Inferred wherever a later step or page shows it from the stored record, as REQ-polaris-generation-041 states. That the view held for the session's whole life SHALL be labelled Inferred, resting on the operating system. Syzygy SHALL NOT describe the view as containing observed code, as a sandbox under SEC-3 or RFC5-18 to 23, or as an execution profile.

For a launched run this requirement displaces exactly this predecessor text of REQ-polaris-generation-033: "SHALL NOT claim that directory is outside the agent sessions' write reach; no separate operating-system user or sandbox is required", read as "MAY claim a path in that directory is outside a role's write reach only as the view Syzygy requested, labelled as this requirement states, except that the authoring session can write drafts/"; and, in the disclosure about the records Syzygy read for its gates, "lie within the agent sessions' write reach", read as "lie outside every launched session's view, with their absence labelled as this requirement states".

ID: REQ-polaris-generation-042
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Inventory cannot see the draft

- **WHEN** the inventory session of a launched run, or any process it starts, tries to list, read or write the run's state directory, including `drafts/`, `checks/` and `brief.md`, a review session's directory or the operator's own agent-tool configuration directory
- **THEN** the attempt fails at the operating-system level and nothing of those paths reaches the session
- **AND** the clone remains readable and the session's own directory writable

#### Scenario: Syzygy checkout absent from every view

- **WHEN** any launched session, or a process it starts, tries to list, read or write the Syzygy checkout or a gate record, directly or through an alias or mounted ancestor
- **THEN** the attempt fails at the operating-system level, no checkout or gate-record content reaches the session, and the record's bytes are unchanged
- **AND** the role's allowed commands still pass through the minimal shim to the supervisor outside the view; the run record and every later page disclose the checkout and gate records as absent from the requested view, labelled Inferred when read from the stored record, with the view's holding also Inferred

#### Scenario: Host cannot build the views

- **WHEN** the operator runs `syzygy polaris <url> --clone <dir>` on a host where Syzygy cannot build a session view
- **THEN** Syzygy refuses the launched run before `init`, naming what is missing, and starts no session
- **AND** the refusal names `syzygy dossier init` as the operator-started route that remains

Form: event-response.

- **Case:** On a host that can build views, on one made unable to before the first or a later start or resume, and with a forbidden state root or Syzygy checkout placed inside an otherwise mounted installation or system path, run launched runs with stand-in sessions that probe every path class above for read, write and listing, from the session and from a child process it starts.
- **Observable:** Each probe's operating-system result, the bytes of the probed files before and after, the refusals, and the recorded view digests and labels.
- **Oracle:** The reachability matrix by role and path class written before the run, and file digests taken outside the view.
- **Oracle independence:** Probe results come from the stand-ins' own system calls and digests from a process outside every view, never from Syzygy's record.
- **Falsifier:** Any session or its child reads, lists or writes a path the matrix forbids, including the Syzygy checkout through an alias, ancestor, shim or broker response; a gate record's bytes change; a session starts without a fresh host check or without its view; a refused host, or a forbidden path inside a mounted path, starts a session; a later page labels a stored requested-view value Observed; or a page calls the view a sandbox, containment or execution profile.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, SEC-2, SEC-3, SEC-5]
  contracts: [RFC5-21]
  policies: [CC-SPEC-2, CC-SPEC-4, CC-SEC-3]
  decisions: [POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05]
  topology: []
  parent_requirements: [REQ-polaris-generation-033, REQ-polaris-generation-035]
```

### Requirement: One attended view

A launched run SHALL present every session and Syzygy's own progress in one terminal view that the command opens: one pane or window per session, interactive exactly as the agent tool presents it, and one for the run's state, showing the current step, the deadline remaining, the limits spent and what the run is waiting for. Every question the run asks, whether from Syzygy (the run limits) or from the authoring session (REQ-polaris-generation-036), SHALL be answerable in that view, and the state pane SHALL name which pane holds an unanswered question.

The operator SHALL be able to detach from the view and reattach to it by one printed command without stopping the run, and to stop the run from the view or by one printed command; stopping SHALL end every launched session and record the stop. A permission here is an approval the agent tool grants a session for a tool use; a session's permissions are fixed at launch by the command line of REQ-polaris-generation-045 and SHALL NOT widen during the run, attached or detached. The declared tool and version SHALL deny every tool use outside that fixed set without offering an approval that widens it; until that behaviour has been observed under REQ-polaris-generation-045, the run SHALL be refused. While no operator is attached, the run SHALL continue only through steps that read, check, freeze, deliver or render; no session SHALL gain any permission, and the run SHALL record each attached and detached interval. Every pane is interactive, so the operator can type into a helper's pane; that is the operator's own act and not input under REQ-polaris-generation-035, and the review page SHALL disclose that whether the operator typed into a helper's pane is Inferred. Syzygy SHALL NOT type or paste into any session's pane. The run's deadline SHALL end every launched session.

ID: REQ-polaris-generation-043
Source: VIS-4; governing warrants below.
Scope: v1-mandatory

#### Scenario: Question surfaces in the view

- **WHEN** the authoring session of a launched run asks the operator a question
- **THEN** the state pane names the authoring pane as holding an unanswered question, and the operator answers it there
- **AND** the run's question count is that of REQ-polaris-generation-036

#### Scenario: Detach and reattach

- **WHEN** the operator detaches from the view during the authoring session and later reattaches with the printed command
- **THEN** the run continued while detached, every pane is as the sessions left it, and the run record lists the detached interval
- **AND** no session gained a permission while detached

#### Scenario: Stop from the view

- **WHEN** the operator stops the run from the view
- **THEN** every launched session ends, the run record records the stop and its instant, and the command reports the stop and the resume command
- **AND** no process of the run remains

Form: event-response.

- **Case:** Run launched runs with stand-in sessions that ask questions, run long and hang; detach and reattach at varied steps; stop from the view and by the printed command; let one run reach its deadline.
- **Observable:** The panes and their contents, the state pane's step, deadline and waiting line, the recorded attached and detached intervals, the processes alive after a stop or the deadline, and each session's permissions over time.
- **Oracle:** The pane set, waiting lines and stop outcomes expected from the scripted stand-ins, written before the run; liveness from the process table.
- **Oracle independence:** Pane contents are captured by the terminal multiplexer outside Syzygy; liveness comes from the operating system; permissions come from each stand-in's own record of the approvals it received and the command line in the process table.
- **Falsifier:** A question cannot be answered in the view; the state pane misnames or omits a waiting question; Syzygy types or pastes into a pane; the review page omits the helper-pane disclosure; detaching stops the run or reattaching loses a pane; a session gains a permission, attached or detached; a process survives a stop or the deadline.

```yaml
warrants:
  primary: VIS-4
  doctrine: [VIS-2, VIS-4]
  contracts: []
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08]
  topology: []
  parent_requirements: [REQ-polaris-generation-033, REQ-polaris-generation-036]
```

### Requirement: No execution in a launched run

Every brief Syzygy issues in a launched run SHALL carry SEC-3's rule that the observed project is not built or run. Because SEC-3 binds every process Syzygy launches, Syzygy SHALL start each launched session with no tool that can run a program other than the Syzygy commands its role is allowed (REQ-polaris-generation-045), so that no process Syzygy launches can run observed code; where that limit cannot be applied to the declared tool and version, or has not been observed for it, Syzygy SHALL refuse the launched run before that session starts. This limit and its per-version evidence SHALL be checked before every session start, including a replacement session and a start on resume, as REQ-polaris-generation-045 requires. Syzygy SHALL refuse `allow-execution` for a launched run, and SHALL refuse to start a launched run, or resume one, whose run directory holds a recorded execution choice. The run record and every page SHALL state that the run was launched by Syzygy and that execution was not permitted.

ID: REQ-polaris-generation-044
Source: SEC-3; governing warrants below.
Scope: v1-mandatory

#### Scenario: Execution choice refused

- **WHEN** the operator runs `allow-execution` for a launched run, before or after its brief
- **THEN** Syzygy refuses it, citing that Syzygy never gives the execution instruction to a session it started, and records nothing
- **AND** every brief of the run carries the no-execution rule

#### Scenario: Run directory with an execution choice

- **WHEN** `syzygy polaris --resume <run>` names a run directory that holds a recorded execution choice
- **THEN** Syzygy refuses to resume it as a launched run and starts no session

Form: event-response.

- **Case:** Attempt `allow-execution` against launched runs at each step; resume runs whose directories do and do not hold an execution-choice record; script a stand-in session, through every tool its command line leaves it, to start a program from the clone; declare a tool version for which the limit has not been observed.
- **Observable:** The refusals and reasons, each brief's execution rule, the run record and the pages' disclosure, and the stand-in's record of every program it tried to start and whether it started.
- **Oracle:** The refusals and the rule text expected from SEC-3 as adopted, written before the run. A stand-in establishes only which command line and tool limits Syzygy requested and when it refused; enforcement by the real tool rests on the independently observed per-version evidence required by REQ-polaris-generation-045, not on a stand-in's behaviour.
- **Oracle independence:** The expected rule text is copied from `doctrine/security.md` outside the code under test; the real-tool evidence comes from the attended probe and independent observations specified by REQ-polaris-generation-045.
- **Falsifier:** An execution choice is recorded for a launched run; a brief of a launched run permits execution; a launched run resumes over an execution-choice record; a launched session starts a program from the clone; any session, including a replacement or resumed start, starts with a tool version whose limit is unobserved or without re-running its launch check.

```yaml
warrants:
  primary: SEC-3
  doctrine: [SEC-3, VIS-4]
  contracts: []
  policies: [CC-SPEC-2, CC-SPEC-4, CC-SEC-3]
  decisions: [POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05]
  topology: []
  parent_requirements: [REQ-polaris-generation-033]
```

### Requirement: Local agent CLI subprocess runner

In a launched run Syzygy SHALL perform every model step only by starting the operator's locally installed agent command-line tool as a child process of the run's supervisor, and by no other means. The tool SHALL be one of a closed set, `claude` (Claude Code) and `codex` (Codex CLI). The operator SHALL declare for the run the tool by name, absolute executable path and version, and the model provider the tool is to use; Syzygy SHALL NOT search for, substitute or fall back to another tool, path, version or provider, and SHALL take the executable from that declaration alone, never from an environment variable or other ambient setting; a test stand-in is declared by absolute path like any tool. Syzygy SHALL start the tool with a process environment it writes and records in full, from an allow-list that admits no credential variable or provider-selection or provider-redirection variable. Syzygy SHALL set `HOME` to the session's private configuration home and, for Claude Code, `CLAUDE_CONFIG_DIR`, or for Codex, `CODEX_HOME`, to the corresponding directory within that same home; it SHALL never inherit any of these variables. These fixed paths select only the private configuration home this requirement describes, never an ambient credential or provider route. No other configuration-home selector is admitted unless its equivalent restriction has been observed for the declared tool and version. No credential variable passes to the tool, and the tool authenticates only through its own credential file, the operator's local login. Every provider-selecting option of the tool (such as a configuration profile, a configuration override, or a local or third-party provider switch) SHALL be either absent or set by Syzygy to the declared provider. Syzygy SHALL NOT start the tool in any mode that bypasses its permission checks or approves requests automatically (for Claude Code the permission modes `bypassPermissions`, `auto` and `acceptEdits` and the flags `--dangerously-skip-permissions` and `--allow-dangerously-skip-permissions`; for Codex `--dangerously-bypass-approvals-and-sandbox`, `--dangerously-bypass-hook-trust` and `--approve-for-me`); an unlisted permission mode or permission-widening option counts as forbidden until it has been observed, for the declared tool and version, to deny every use outside the role's fixed pre-approved tools, even while the operator is attached. This includes Claude Code's `dontAsk`: its name alone establishes no enforcement. Syzygy SHALL NOT contain, load or call a model-provider SDK or API client, open a connection to a model provider, or resolve a provider route for this step. Syzygy SHALL read no provider credential except to copy the tool's own credential file, unparsed, to where the tool expects it inside the session's view, and SHALL record that it did; the read-only inspection of the administrator-managed settings' provider-relevant keys in the next paragraph is the one other permitted read, and its values reach no record, log, page or child process. Authentication is the tool's own, under the operator's account. Syzygy SHALL remove every copy of the credential file it made, with the session's private configuration home, when the session ends and at the run's close, stop, deadline or refusal, SHALL record each removal, and SHALL report a copy it could not remove as a finding. Before every session start, including a replacement session and a start on resume, Syzygy SHALL check that the tool's own credential file is present where the declared tool and version expects it and that the tool reports itself logged in from it alone, by running the tool's own login-status command inside the session's view and with the environment this paragraph writes, and SHALL record that check (the command's digest, its exit status and the result, never a credential value) in the launch record, labelled under the launch-field rule below; where the file is absent, the tool's login is held elsewhere (such as a system keychain), the declared tool and version has no login-status command, or the check cannot be made, Syzygy SHALL refuse the launched run, naming the failure, start no session, and report the run's readiness and every claim that depends on the model step as Unknown.

Syzygy SHALL give the tool, explicitly on its command line or in files it names there, and in no other way: the session's working directory and its writable paths, as REQ-polaris-generation-042 gives them for its role; the role's instructions file, written by Syzygy and recorded by digest; the artifacts output path the session's result is handed in through; and the skill and MCP guidance for the role, each skill as a named file or directory and each MCP server as an explicit configuration, or the explicit statement that the role has none; and the tools of its role and no other: read tools over the paths its view makes readable; for the authoring session, writes only under the run's `drafts/`; and a shell only as the runner of the Syzygy commands its role is allowed (for a helper, the waiting command of REQ-polaris-generation-035 for its own directory; for the authoring session, the dossier check and run-report commands for its run), never a general shell, and no tool that fetches, searches or otherwise reaches the network. Every MCP server named for a role SHALL be a local process Syzygy names that opens no network connection. Where the declared tool and version cannot be limited so, or enforcement of the limit has not been observed for it in the real-tool attended probe specified below, Syzygy SHALL refuse the launched run before any session starts, naming the tool. Syzygy SHALL NOT give a session instructions or input by typing or pasting into its terminal. Every other settings, instruction and MCP source SHALL be excluded: the tool's user, project and local settings layers; user-level and project-level instruction files (such as `CLAUDE.md` and `AGENTS.md`); the settings, instruction and MCP files of every directory the session can read, the clone included; skills, custom agents, custom commands and output styles, whether in the operator's home or in any directory the session can read, the clone included, other than the skills Syzygy names; plugins; hooks; and ambient MCP configuration. Syzygy SHALL exclude each by the tool's own flags where they exist, and otherwise by a private configuration home inside the session's view, writable by the session, holding only what Syzygy wrote there and the tool's own state for that session. A source counts as excluded only once its exclusion has been observed for the declared tool and version in the real-tool attended probe specified below; until then it counts as not excluded. Where any source other than the tool's administrator-managed settings is not excluded, Syzygy SHALL refuse the launched run before any session starts, naming the source. Administrator-managed settings, which neither tool offers a flag to exclude, SHALL be recorded as not excluded, labelled under the launch-field rule below, and disclosed on the run page. Before every session start, including a replacement session and a start on resume, Syzygy SHALL read, from the tool's administrator-managed settings at the locations the declared tool and version documents, only the keys that can select, redirect or authenticate a model provider, its environment block included; this is tool configuration on the operator's host, not target content. The read is read-only; a key's value is used only to decide a mismatch and is never recorded, logged, stored, transmitted or passed to the tool. Where any such key names or could select a provider, endpoint or credential route other than the declared provider, or authenticates the tool by any means other than its own credential file (such as an API key, a key helper or a token, even for the declared provider), Syzygy SHALL refuse the launched run, naming the key and file. Where a managed-settings location exists but cannot be read or parsed, or the managed layer's provider-relevant keys for the declared tool and version are not known, Syzygy SHALL refuse the launched run and report the session's effective provider and every claim that depends on the model step as Unknown. The launch record SHALL hold each managed-settings location checked, whether it was present, and the provider-relevant keys found by name.

Before `init`, and again before every session start, including a replacement session and a start on resume, Syzygy SHALL check that the declared executable exists at its path, is executable, and reports the declared version; where any check fails it SHALL refuse the launched run, naming the failure, start no session, and report the run's readiness and every claim that depends on the model step as Unknown, never as ready, passed or empty. Each session SHALL carry a time bound, declared for the run and no later than the run deadline; Syzygy SHALL stop a session that exceeds it, record the stop, and leave the session's result absent and its dependent claims Unknown. A session that exits non-zero, writes no result at its artifacts path, or writes one that fails validation SHALL count as no result.

For each launched session the launch record of REQ-polaris-generation-041 SHALL also hold: the tool's name, executable path and reported version; the declared provider; the process environment the tool was started with, by variable name and by digest over its names and values; the digest of the instructions file; the artifacts output path; the exact skill and MCP guidance given, by path and digest, or that none was given; each settings layer and whether it was excluded, and by what means; and the session's time bound and whether it was reached.

Before invoking the declared tool, for its login-status check as well as for a session, Syzygy SHALL apply the tool's own controls that disable auxiliary network traffic, including telemetry, error reporting and update checks, for that invocation and its tool-managed child processes. The controls and their effect SHALL have been observed for that executable and version in the real-tool attended probe below. If a control is unavailable, its effect is unobserved or the observed controls leave any destination other than the declared provider available for such traffic, Syzygy SHALL refuse before invoking the tool, name the missing control or observation, and leave readiness and dependent claims Unknown. This requirement grants no auxiliary egress permission. The launch record SHALL identify the controls applied and the per-version evidence, under the launch-field rule below.

The first observation of real-tool limits, exclusions, fixed permissions and auxiliary-traffic controls SHALL come from an operator-started attended probe outside a launched run, using synthetic fixtures and an independent record of the attempted tool uses, settings effects and per-process network attempts. The evidence SHALL identify its subject executable by path and digest, reported version, controls and fixtures, capture time, outcomes and record digest. It SHALL establish each required restriction separately; a stand-in's argv, a flag's name or a tool's help text establishes no real-tool enforcement. The probe grants no project read, provider egress, launch or execution authority; it uses no target-repository content and runs only under authority already in force. Until this evidence exists, launched runs refuse. Before every session start, including each replacement and resumed start, Syzygy SHALL re-run the host-view, executable, version, login, managed-settings, exclusion, tool-limit, fixed-permission and auxiliary-control checks, matching the current executable digest and version to that evidence. A prior successful start or a stored preflight result SHALL NOT substitute; any failed or unobserved check refuses that start and stops the run.

Every launch-record field in this requirement, including login and managed-settings checks, exclusions, controls and metadata, follows REQ-polaris-generation-041: Observed only in the output of the launching step as Syzygy makes the launch, and Inferred wherever a later step or page shows the value from the stored record. No stored launch record establishes an Observed label.

This requirement grants no consent. A run whose declared tool and provider have no agent-provider statement in force for the target SHALL be refused before any session starts, naming the missing statement. Every target-derived input Syzygy gives a launched session, including a packet, brief, instructions file, named guidance and the output of a brokered Syzygy command, SHALL carry only the content classes that statement lists and pass the unchanged screening rules. The supervisor SHALL refuse a delivery that would carry an unlisted class; the minimal shim grants no route around that limit. This restricts Syzygy's deliveries, not the agent session's own reading of its permitted clone. The authoring and inventory sessions can read the whole clone, so their tools can transmit to their provider content of any class in the clone, listed or not. That reading and sending rests on the owner's rulings that the agent session's own reading and sending are the operator's own act (`POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` item 2, and for launched runs the one-command run's packet Q2 and `DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15` item 2), not on the statement, and a launched run SHALL NOT be refused for it. Review sessions see only their own delivered inputs as REQ-polaris-generation-042 states. The run page SHALL disclose this: it SHALL name the statement and the classes it lists; it SHALL give the list of content classes present in the clone at the pinned revision, as Syzygy's own path listing of that tree exposes them (REQ-polaris-generation-030), which covers the pinned tree only and says so, each marked as listed or not listed by the statement, with any class the listing cannot determine shown as Unknown; and it SHALL state which roles could read the whole clone and that their tools may have sent their provider content of the classes the statement does not list.

ID: REQ-polaris-generation-045
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Declared tool started with explicit inputs only

- **WHEN** a launched run starts a session with the declared tool
- **THEN** the process tree shows that tool, at the declared path, as a child of the supervisor, with a command line naming the workspace, the instructions file, the artifacts path and the role's skill and MCP guidance
- **AND** the launch record holds each of those by path and digest, and the settings layers with how each was excluded

#### Scenario: Operator settings do not widen a session

- **WHEN** the operator's user, project and local settings for the tool carry an allow rule, a hook, a plugin and an MCP server that the role is not given
- **THEN** none of them is in effect in the launched session: the allow rule grants nothing, the hook does not fire, and the plugin and MCP server are absent
- **AND** where an exclusion has not been observed for the declared tool and version, the launched run is refused before any session starts, naming the source

#### Scenario: Clone carries tool settings and instructions

- **WHEN** the clone, or the operator's home, holds tool settings, an MCP configuration, instruction files, skills, custom agents, custom commands and output styles (such as `.claude/settings.json`, `.mcp.json`, `CLAUDE.md`, `AGENTS.md`, `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/output-styles/`, `.codex/`) granting an allow rule, starting an MCP server and telling the agent to write outside its directory
- **THEN** none of them is in effect in any launched session that can read the clone
- **AND** where their exclusion has not been observed for the declared tool and version, the launched run is refused before any session starts

#### Scenario: Provider redirected by the environment

- **WHEN** the operator's environment carries a variable or tool option that selects, redirects or authenticates a model provider other than the declared one
- **THEN** the launched session's environment and command line carry none of it, and the session's effective provider is the declared one
- **AND** the launch record lists the environment Syzygy wrote by variable name, and no credential variable is among them; the tool authenticates only through its own credential file

#### Scenario: Managed settings redirect or cannot be read

- **WHEN** the tool's administrator-managed settings carry an environment block or key that selects, redirects or authenticates a provider other than the declared one, or that authenticates the tool by any means other than its own credential file, even for the declared provider, or a managed-settings location exists but cannot be read or parsed, or the managed layer's provider-relevant keys for the declared tool and version are not known
- **THEN** Syzygy refuses the launched run before any session starts, naming the key and file, the unreadable location, or the unknown version
- **AND** the session's effective provider and every claim depending on the model step read Unknown, and the launch record lists each location checked

#### Scenario: Stand-in taken from the environment

- **WHEN** an environment variable such as `SYZYGY_POLARIS_AGENT` names an executable other than the declared one
- **THEN** Syzygy starts the declared executable or refuses the run, and never starts the one the variable names

#### Scenario: Binary absent

- **WHEN** the declared executable is missing, not executable, or reports a different version
- **THEN** Syzygy refuses the launched run before `init` on its initial check, or before that session on a later or resumed check, naming the failure, and starts no session at that start
- **AND** the run's readiness and every claim depending on the model step read Unknown, and no page or status reads ready or green

#### Scenario: Every session start repeats preflight

- **WHEN** the executable, reported version, login, managed settings, host view, an exclusion, a fixed permission, a tool limit or an auxiliary-traffic control fails its check after an earlier successful start, before a later, replacement or resumed session starts
- **THEN** Syzygy re-runs the checks for that start and refuses before starting that session, naming the failure
- **AND** the run stops, no earlier launched session remains running, and readiness and every dependent claim are Unknown

#### Scenario: Auxiliary-traffic control unobserved

- **WHEN** the declared tool and version lacks an observed control disabling telemetry, error reporting, update checks or another auxiliary connection beyond its declared provider
- **THEN** Syzygy refuses before invoking the tool, including its login-status command, naming the missing control or evidence
- **AND** no stand-in observation or earlier tool version counts as evidence of the real tool's enforcement

#### Scenario: Delivered input exceeds the provider statement

- **WHEN** a packet, brief, instructions file, named guidance or brokered command output would give a launched session target-derived content of a class its agent-provider statement does not list
- **THEN** Syzygy refuses that delivery and gives the session none of that input
- **AND** the session's own reading of the clone, where its role has it, remains subject to the run-page disclosure rather than this delivery gate

#### Scenario: Stored launch values remain Inferred

- **WHEN** a later step or page displays a view digest, login check, managed-settings check, exclusion, applied control or other metadata from a stored launch record
- **THEN** each displayed value is labelled Inferred, even if the launching step's output labelled it Observed

#### Scenario: Session exceeds its time bound

- **WHEN** a launched session is still running at its time bound
- **THEN** Syzygy stops it and records the stop
- **AND** the session's result is absent and its dependent claims are Unknown

#### Scenario: No provider client

- **WHEN** the built, non-test runtime output of the Syzygy packages and the lockfile are inspected, and a launched run is made with stand-in tools under a network observation
- **THEN** no model-provider SDK or API client, no provider endpoint host and no read of a provider credential variable or credential file (other than the recorded copy of the tool's own credential file, and the read-only inspection of the managed settings' provider-relevant keys, whose values are never recorded or passed on) is present in or reachable from the launched-run code
- **AND** no process that is not the declared tool or a process it started opens a connection to a model-provider endpoint during the run

#### Scenario: Tool without a provider statement

- **WHEN** the operator declares `codex` for a target that has an agent-provider statement in force only for Claude Code with Anthropic
- **THEN** Syzygy refuses the launched run before any session starts, naming the missing statement

#### Scenario: Run page discloses unlimited reading

- **WHEN** a launched run renders its pages
- **THEN** the run page names the agent-provider statement and the content classes it lists
- **AND** lists the content classes present in the clone at the pinned revision, each marked listed or not listed, any undeterminable class shown as Unknown
- **AND** states which roles could read the whole clone and that their tools may have sent their provider content of the unlisted classes, and the run is not refused for them

#### Scenario: Tool cannot authenticate from its own credential file

- **WHEN** the declared tool's credential file is absent, its login is held only in a system keychain, the declared tool and version has no login-status command, or its logged-in status cannot be checked inside the session's view
- **THEN** Syzygy refuses the launched run before any session starts, naming the failure, and starts no session
- **AND** the run's readiness and every claim depending on the model step read Unknown

Form: event-response.

- **Case:** Launched runs with stand-in `claude` and `codex` executables that record their own argv, environment, parent process and the files they can read; an operator home seeded with a permissive allow rule, a hook that writes a marker file, a plugin and an MCP server; a clone and an operator home seeded with tool settings, an MCP configuration, instruction files, skills, custom agents, custom commands and output styles; an operator environment seeded with a provider-redirecting variable, a provider-selecting tool option, a provider credential variable and a `SYZYGY_POLARIS_AGENT` naming another executable; administrator-managed settings seeded, in an attended run, with a provider-redirecting environment block, with an API key or key helper for the declared provider, made unreadable, and presented for a tool version whose provider-relevant managed keys are not known; an operator home whose credential file is absent, one whose login is keychain-only, and a stand-in tool with no login-status command; a clone holding content classes the statement does not list; a declared bypass-permissions mode; runs with the binary removed, made non-executable and reporting a wrong version; a stand-in that never exits; each automatic-approval and bypass mode declared; a stand-in whose command line would leave it a general shell, a web-fetch or web-search tool, or an MCP server that opens a network connection; attempted permission widening both attached and detached; per-version real-tool evidence present, absent, wrong-digest and wrong-version; auxiliary controls absent or unobserved, including before login-status; each launch check changed between an initial start and a later, replacement or resumed start; each delivered input kind seeded with an unlisted content class; stored launch metadata shown on a later page; a session ended, a run stopped and a run refused, each with the credential copies inspected afterwards; a declared tool with no provider statement for the target; an inspection of the built non-test runtime output and the lockfile; a run in a network namespace whose connection attempts are recorded per process, with the provider endpoints resolved to a local recorder.
- **Observable:** Each stand-in's recorded argv, environment and readable files, the hook's and the clone's marker files, the process tree, the per-process connection record, the launch records, the refusals and their wording, each page's readiness and disclosure wording, the stop records, the inspection's output, each repeated launch check, each refused delivery, and each live and later stored-record label.
- **Oracle:** The expected argv, environment allow-list, guidance and settings-exclusion list per role and tool, the refusal, disclosure and Unknown wording, and the expected present-class set, listed and unlisted, for each seeded clone, written before the run. Stand-ins establish only the requested invocation, refusal and delivery behaviour; the real tool's enforcement rests on the separate per-version attended-probe evidence above. For the inspection, the known provider SDK package names, provider endpoint hosts, credential variable names and credential file paths, scoped to built non-test runtime output and the lockfile so that test fixtures holding those strings as sentinels are out of scope, and excepting exactly two uses: the copy of the tool's own credential file, and the read-only inspection of the managed settings' provider-relevant keys by name, whose values reach no record, log, page or child process.
- **Oracle independence:** Argv, environment, readable files, markers and connections come from the stand-ins, the file system and the network namespace, not from Syzygy's launch record; the inspection reads the lockfile and built output, not Syzygy's own claims.
- **Falsifier:** A session starts with an undeclared tool, path, version or provider, with an executable taken from the environment, or in a bypass-permissions mode; an operator or clone allow rule, hook, plugin, MCP server, instruction file, skill, custom agent, custom command or output style takes effect; a provider-redirecting variable or option, or any credential variable, reaches the tool; a managed-settings value appears in any record, log or page or reaches the tool; a run starts while managed settings redirect the provider, authenticate it by any means other than the tool's own credential file, cannot be read, or have provider-relevant keys not known for the declared version; a session starts in an automatic-approval mode, or with a general shell, a network-reaching tool or a network-opening MCP server, or under an unobserved tool limit; a credential copy or private configuration home remains after its session ends or the run closes, stops, passes its deadline or is refused, with no finding; Syzygy types or pastes into a session's terminal; a session starts when the tool cannot authenticate from its own credential file alone or its login check ran outside the session's view or was not recorded, or that refusal leaves any readiness or claim other than Unknown; a run is refused for unlisted content classes in the clone, or the run page omits the present-class list or the may-have-sent statement, or the list omits or mislabels a present class; a credential read other than the two excepted uses is present in runtime output; instructions or guidance reach the tool by any route not on its command line or in a file it names; a run starts with an unobserved exclusion; a missing or mismatched binary leaves any readiness or claim other than Unknown, or a session starts; any first, later, replacement or resumed session starts without re-running every required launch check; the tool is invoked before auxiliary controls and their real-tool evidence are checked; an ambient configuration-home selector is inherited; any delivered input carries an unlisted target content class; a later display labels stored launch metadata Observed; a session runs past its bound; a provider SDK, API client or endpoint host is present in runtime output; a process other than the declared tool or its descendants opens a connection to a model-provider endpoint; a run without a provider statement for its tool starts a session; or the run page omits the unlimited-reading disclosure.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, VIS-4, SEC-2, SEC-3]
  contracts: [RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15, DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15, POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14, POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05]
  topology: []
  parent_requirements: [REQ-polaris-generation-041, REQ-polaris-generation-042]
```
