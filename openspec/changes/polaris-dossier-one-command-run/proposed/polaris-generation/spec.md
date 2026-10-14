# One-command Polaris dossier run

Candidate exact behavioral delta; not adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds five requirements to the operator-agent mode of REQ-polaris-generation-033 to 036, in a *launched* form of that mode taken only when the operator starts a run with the one command: the one-command run (040), Syzygy-launched sessions (041), session isolation (042), one attended view (043) and no execution in launched runs (044). It edits no byte of any predecessor requirement or scenario. For a launched run each added requirement names the predecessor text it displaces; every other sentence and scenario of REQ-polaris-generation-033 to 036 applies unchanged. A run started with `syzygy dossier init` is not a launched run, and none of these requirements applies to it.

## ADDED Requirements

### Requirement: One-command run

The operator-agent mode SHALL offer one command, `syzygy polaris <url>`, that takes a repository URL and the run limits of REQ-polaris-generation-033 (as options or, where absent, from one question the command asks before anything else) and carries the run through every step REQ-polaris-generation-033 to 036 name, in this order: preflight; the one-commit clone of a consented revision into a directory under the state root, or the operator's existing clone given with `--clone`, checked as `init` checks it; `init`; `brief`; the authoring session with its draft and `check` loop; the inventory session and `inventory-check`; the fidelity review and its validation; `render`; the rendered-design review and its validation; and `close`. A run so started is a *launched run*, and the run record SHALL say so from the moment `init` writes it.

The command SHALL stop only at one of these, and SHALL state which in human and machine form: a refusal by any step, with the step and its reason exactly as that step reports them; a question for the operator that the operator declines to answer; the run's declared deadline or token or turn limit; the operator's stop; or a closed run with its rendered dossier, naming the site directory and the run record. Running `syzygy polaris --resume <run>` SHALL continue a launched run from its first unfinished step, re-running every gate that step requires, and SHALL refuse a run that is not a launched run, a closed run, and a run past its deadline.

Every check, freeze, packet, validation, refusal, label and disclosure SHALL be that of REQ-polaris-generation-033 to 036; the one command adds no step that decides readiness and removes none.

ID: REQ-polaris-generation-040
Source: VIS-1; governing warrants below.
Scope: v1-mandatory

#### Scenario: One command to a closed run

- **WHEN** the operator runs `syzygy polaris <url>` for a repository whose gates are in force, answers the run-limit question, and every check and review passes
- **THEN** the run reaches `close` with no further command typed by the operator, and the command ends naming the site directory and the run record
- **AND** the run record lists, in order, every step of REQ-polaris-generation-033 to 036 that ran, with its outcome

#### Scenario: Refusal stops the run

- **WHEN** any step refuses, including preflight missing a gate, `init` refusing the clone, or `check` refusing past the repair-cycle limit
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

- **Case:** Run the command against fixture repositories and fixture gate records with a stand-in agent tool whose behaviour each case scripts (passing draft, failing draft, failing inventory, blocking finding, question, hang), varying the gates, the clone, the limits, the stop point and the resume point.
- **Observable:** The steps run and their order, each step's outcome and refusal text, the command's final statement in both forms, the run record, and the processes alive after the command ends.
- **Oracle:** The step sequence, stop points and refusal texts expected from the fixture records and the scripted agent behaviour, written before the run; process liveness from an independent process listing.
- **Oracle independence:** Expected sequences and texts are written outside the code under test; liveness comes from the operating system's process table, never Syzygy's record.
- **Falsifier:** The command skips, reorders or adds a readiness-deciding step; continues past a refusal; changes a step's refusal text; leaves a launched session running after it ends; resumes a run that is not launched, is closed or is past its deadline; or treats a `syzygy dossier init` run as launched.

```yaml
warrants:
  primary: VIS-1
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, SEC-2, SEC-3]
  contracts: [RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05, POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08]
  topology: []
  parent_requirements: [REQ-polaris-generation-033, REQ-polaris-generation-034, REQ-polaris-generation-035, REQ-polaris-generation-036]
```

### Requirement: Syzygy-launched sessions

In a launched run Syzygy SHALL start every agent session of the run, the authoring session and the inventory, fidelity-review and rendered-design-review sessions, itself: each as a child of the run's supervisor process and never of another session, from the fixed prompt Syzygy writes for that role and records by digest, in that session's own directory, with the agent tool, version and model the operator declared for the run. Each helper session SHALL be started before its input exists and SHALL obtain its input only through the waiting command of REQ-polaris-generation-035; Syzygy SHALL deliver packets exactly as that requirement states. No session SHALL be able to start, resume, signal or write input to another session through Syzygy; Syzygy SHALL expose no command or file by which the authoring session causes a helper session to start or receive input.

For each launched session the run record SHALL record the launch form `syzygy-launched` and, labelled Observed because Syzygy itself did each: the role; the agent tool's executable path and the digest of the full command line Syzygy ran; the session directory; the isolation view of REQ-polaris-generation-042 by digest; the process identifier; the start instant; and the exit instant and status, or that the run stopped it. The session identifier each session declares, the model the provider actually served, and that the context was fresh SHALL remain Inferred. An inventory or verdict from a launched run SHALL count only when its session's launch record exists and names that session's directory; Syzygy SHALL refuse a declared `terminal` or `bang` launch form in a launched run.

For a launched run this requirement displaces exactly this predecessor text of REQ-polaris-generation-035: "a separate top-level agent session that the operator starts", read as "a separate session that Syzygy starts under this requirement"; "the operator starts each such session as above, and neither Syzygy nor the authoring session starts, resumes or signals it", read as "Syzygy starts each such session under this requirement, and the authoring session neither starts, resumes nor signals it"; "its launch form, which is a new terminal or the shell-escape prefix, as the operator declares it", read as "its launch form, `syzygy-launched`, as Syzygy recorded it"; and, among what remains Inferred, "that each session was a top-level session the operator started, in the launch form declared, and not a subagent or process of the authoring session", which becomes Observed from the launch record. The rule that a subagent or a process of the authoring session SHALL NOT satisfy the inventory or a review is unchanged.

ID: REQ-polaris-generation-041
Source: VIS-3; governing warrants below.
Scope: v1-mandatory

#### Scenario: Four sessions launched by Syzygy

- **WHEN** a launched run issues its brief
- **THEN** Syzygy starts the authoring, inventory, fidelity-review and design-review sessions, each in its own directory from its own fixed prompt, each a child of the supervisor
- **AND** the run record holds a `syzygy-launched` launch record for each, labelled Observed, and the review page discloses which fields are Observed and which Inferred

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
- **Falsifier:** A session is a child of another session; a helper starts, receives input or is signalled because of the authoring session; a launch record is missing or disagrees with the process table; a submission without a launch record, or with `terminal` or `bang`, counts in a launched run.

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-2, VIS-3, VIS-4, SEC-3]
  contracts: [RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05, POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08]
  topology: []
  parent_requirements: [REQ-polaris-generation-006, REQ-polaris-generation-035]
```

### Requirement: Session isolation

In a launched run Syzygy SHALL start every session inside a file-system view it builds for that session's role before the session's process starts, so that the session and every process it starts can reach only: for the authoring session, the clone read-only, its own directory read-write, and the run's draft path read-write; for the inventory session, the clone read-only and its own directory read-write; for each review session, its own directory read-write; for every session, the Syzygy checkout read-only, the agent tool's own installation and configuration as the tool requires, and the system paths a process needs to run, all read-only except the agent tool's own state. No session SHALL be able to read or write another session's directory, the run's state directory, or the run's `drafts/` and `checks/` paths other than as stated. Network access SHALL be left to the agent tool; Syzygy SHALL disclose that it does not restrict where a session sends data.

Before it starts any session Syzygy SHALL check that it can build these views on the host, and SHALL refuse the launched run before `init` where it cannot, naming what is missing; it SHALL NOT start a launched session without its view. The run record SHALL record each view by digest of its full specification, labelled Observed as the view Syzygy requested; that the view held for the session's whole life SHALL be labelled Inferred, resting on the operating system. Syzygy SHALL NOT describe the view as containing observed code, as a sandbox under SEC-3 or RFC5-18 to 23, or as an execution profile.

For a launched run this requirement displaces exactly this predecessor text of REQ-polaris-generation-033: "SHALL NOT claim that directory is outside the agent sessions' write reach; no separate operating-system user or sandbox is required", read as "MAY claim that directory is outside the agent sessions' reach only as the view Syzygy requested, labelled as this requirement states"; and, in the disclosure that the records Syzygy read for its gates lie within the agent sessions' reach, the launched run instead discloses that they lie read-only in every session's view.

ID: REQ-polaris-generation-042
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Inventory cannot see the draft

- **WHEN** the inventory session of a launched run, or any process it starts, tries to list, read or write the run's `drafts/`, `checks/`, `brief.md`, the authoring session's directory or a review session's directory
- **THEN** the attempt fails at the operating-system level and nothing of those paths reaches the session
- **AND** the clone remains readable and the session's own directory writable

#### Scenario: Gate records out of every session's write reach

- **WHEN** any launched session, or a process it starts, tries to write a file in the Syzygy checkout, including a gate record
- **THEN** the write fails at the operating-system level and the record's bytes are unchanged
- **AND** the run record and every page disclose the records as read-only in each view, and the view as requested by Syzygy, with its holding labelled Inferred

#### Scenario: Host cannot build the views

- **WHEN** the operator runs `syzygy polaris <url>` on a host where Syzygy cannot build a session view
- **THEN** Syzygy refuses the launched run before `init`, naming what is missing, and starts no session
- **AND** the refusal names `syzygy dossier init` as the operator-started route that remains

Form: event-response.

- **Case:** On a host that can build views and on one made unable to, run launched runs with stand-in sessions that probe every path class above for read, write and listing, from the session and from a child process it starts.
- **Observable:** Each probe's operating-system result, the bytes of the probed files before and after, the refusals, and the recorded view digests and labels.
- **Oracle:** The reachability matrix by role and path class written before the run, and file digests taken outside the view.
- **Oracle independence:** Probe results come from the stand-ins' own system calls and digests from a process outside every view, never from Syzygy's record.
- **Falsifier:** Any session or its child reads, lists or writes a path the matrix forbids; a gate record's bytes change; a session starts without a view; a refused host starts a session; or a page calls the view a sandbox, containment or execution profile.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, SEC-2, SEC-3, SEC-5]
  contracts: [RFC5-21]
  policies: [CC-SPEC-2, CC-SPEC-4, CC-SEC-3]
  decisions: [POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05]
  topology: []
  parent_requirements: [REQ-polaris-generation-033, REQ-polaris-generation-035]
```

### Requirement: One attended view

A launched run SHALL present every session and Syzygy's own progress in one terminal view that the command opens: one pane or window per session, interactive exactly as the agent tool presents it, and one for the run's state, showing the current step, the deadline remaining, the limits spent and what the run is waiting for. Every question the run asks, whether from Syzygy (the run limits) or from the authoring session (REQ-polaris-generation-036), SHALL be answerable in that view, and the state pane SHALL name which pane holds an unanswered question.

The operator SHALL be able to detach from the view and reattach to it by one printed command without stopping the run, and to stop the run from the view or by one printed command; stopping SHALL end every launched session and record the stop. While no operator is attached, the run SHALL continue only through steps that read, check, freeze, deliver or render; no session SHALL gain any permission, and the run SHALL record each attached and detached interval. The run's deadline SHALL end every launched session.

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
- **Oracle independence:** Pane contents are captured by the terminal multiplexer outside Syzygy; liveness and permissions come from the operating system.
- **Falsifier:** A question cannot be answered in the view; the state pane misnames or omits a waiting question; detaching stops the run or reattaching loses a pane; a session gains a permission while detached; a process survives a stop or the deadline.

```yaml
warrants:
  primary: VIS-4
  doctrine: [VIS-2, VIS-4]
  contracts: []
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08]
  topology: []
  parent_requirements: [REQ-polaris-generation-033, REQ-polaris-generation-036]
```

### Requirement: No execution in a launched run

Every brief Syzygy issues in a launched run SHALL carry SEC-3's rule that the observed project is not built or run. Syzygy SHALL refuse `allow-execution` for a launched run, and SHALL refuse to start a launched run, or resume one, whose run directory holds a recorded execution choice. The run record and every page SHALL state that the run was launched by Syzygy and that execution was not permitted.

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

- **Case:** Attempt `allow-execution` against launched runs at each step; resume runs whose directories do and do not hold an execution-choice record.
- **Observable:** The refusals and reasons, each brief's execution rule, the run record and the pages' disclosure.
- **Oracle:** The refusals and the rule text expected from SEC-3 as adopted, written before the run.
- **Oracle independence:** The expected rule text is copied from `doctrine/security.md` outside the code under test.
- **Falsifier:** An execution choice is recorded for a launched run; a brief of a launched run permits execution; a launched run resumes over an execution-choice record.

```yaml
warrants:
  primary: SEC-3
  doctrine: [SEC-3, VIS-4]
  contracts: []
  policies: [CC-SPEC-2, CC-SPEC-4, CC-SEC-3]
  decisions: [POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05]
  topology: []
  parent_requirements: [REQ-polaris-generation-033]
```
