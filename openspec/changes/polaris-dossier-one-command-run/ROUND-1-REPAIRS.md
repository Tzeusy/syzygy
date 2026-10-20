# Round 1 repairs — one-command Polaris dossier run

> **Candidate — binds nothing.** Repair map for review round 1. A repair
> performs no act.

Raw: `docs/reviews/R-POLARIS-DOSSIER-ONE-COMMAND-RUN-1-RAW.md`, verdict
`REVISE` (line 4), over commit `8afadc5544efc6c88c44e0d0fa6f261551a60b96`:
11 revise findings and 10 notes (raw line 317). Under the lead's process
rule, these findings are repaired once and one more review follows. If that
review is `REVISE`, the lane stops and reports.

Every repair keeps the fail-closed arm. None of them needs a new owner act.

| # | Class | Repair |
|---|---|---|
| 1 | revise | REQ-040 no longer has Syzygy clone or fetch anything. The command takes the operator's own clone with `--clone` and refuses without one, because no act covers a Syzygy-made fetch. The steps are named as those of REQ-033 to 036 together with the launches of REQ-041 and 045. The proposal and the design follow, and the prototype's fetch is disclosed. |
| 2 | revise | REQ-041 labels a launch record Observed only in the output of the step that makes the launch. Wherever a later step or page shows it from the stored record, it is Inferred, as REQ-033 requires. No part of that rule is displaced. The scenario and the Falsifier follow. |
| 3 | revise | REQ-041 now also displaces REQ-035's sentence "each is labelled Inferred … until its launch form is declared", quoted exactly, so that a launched inventory needs its launch record. |
| 4 | revise | REQ-041 reads REQ-035's "The command Syzygy prints for a waiting session" and "the printed command" as the command line Syzygy runs, so their tool narrowing binds. REQ-045 now gives each role only its tools: read tools, author writes under `drafts/`, and a shell only as the runner of the role's Syzygy commands. It allows no general shell and no network-reaching tool, and it refuses where that limit cannot be applied or has not been observed. |
| 5 | revise | REQ-044 now binds the process: no launched session has a tool that can run a program other than its role's Syzygy commands. It refuses where that limit is not applied or not observed. The Case adds a stand-in probe that tries to start a program from the clone. |
| 6 | revise | REQ-045 gives no session a tool that reaches any destination other than the provider, and every named MCP server must open no network connection. REQ-042's network sentence now says this, and it discloses as Inferred that the tool itself opened nothing else. |
| 7 | revise | REQ-045 forbids automatic-approval modes as well as bypass modes, naming them per tool. A mode it does not name counts as forbidden until it has been observed. The Case and the Falsifier test each one. |
| 8 | revise | REQ-042 now states each role's working directory and writable paths, and the private configuration home as read-write. REQ-041 and REQ-045 refer to it, and REQ-045's indirect reading of REQ-042 is removed (note 20). |
| 9 | revise | REQ-040's closing sentence names REQ-041 to 045 alongside REQ-033 to 036. |
| 10 | revise | Fixed in the proposal: child of the supervisor, the per-role view, the `LAUNCH_FORMS` claim (dated and corrected), and packet Q2 marked as answered. The design's mounts now match REQ-045. |
| 11 | revise | The design's prototype section now also discloses `--permission-mode auto`, the `PATH` lookup, the prompt passed as an argument, `tmux send-keys`, the fetch, and the hard-coded provider and owner flags. |
| 12 | note | REQ-045 removes the credential copies and the private configuration homes at session end, close, stop, deadline and refusal, and records each removal. Failing to remove one is a finding. |
| 13 | note | REQ-043 defines a permission as a tool-use approval that is fixed at launch, and takes its oracle from the stand-in's record of approvals. |
| 14 | note | REQ-043 says that operator typing in a helper pane is the operator's act, which the review page discloses as Inferred. Syzygy never types into a pane. |
| 15 | note | REQ-040's stop list says that a session past its time bound is no result, and the step that needed that result refuses. |
| 16 | note | Packet Q2 no longer attributes the RFC7-20 clause to the 2026-10-08 packet. |
| 17 | note | The tasks.md leftover is replaced by one plain sentence. |
| 18 | note | REQ-042 says that a REQ-035 delivery is not a forbidden copy. |
| 19 | note | REQ-042's host check refuses a forbidden path that lies inside a mounted path. The Case and the Falsifier follow. |
| 20 | note | Taken with finding 8. |
| 21 | note | No change. The two observations rest on material outside this repository, which this review could not read, and they stay as they are written. |
