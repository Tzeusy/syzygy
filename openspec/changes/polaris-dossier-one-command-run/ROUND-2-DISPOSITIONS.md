# Round 2 dispositions — one-command Polaris dossier run

> **Candidate — binds nothing.** This file classifies the round-2 findings. It performs no act and repairs nothing.

Raw: `docs/reviews/R-POLARIS-DOSSIER-ONE-COMMAND-RUN-2-RAW.md`, verdict
`REVISE` (line 4), over commit `5f026d9cadacba639454d4e4d393d63174267810`.
Round-1 closure: 16 closed, 4 partly closed, 0 not closed, and 1 closed with
no change. New findings: 7 revise and 10 notes (raw line 199).

The lead's rule for this change was: repair once, run one more review, and
stop and report if that review is still `REVISE`. It is `REVISE`. So the
change is **not cleared**, **not offered for sign-off**, and **not edited
further** by this lane. Register row P-111 says so.

| # | Class | Owner choice? | Classification |
|---|---|---|---|
| N1 | revise | Possibly | Every view mounts the whole Syzygy checkout readable. The agent tool can then send its contents to its provider, including the Butlers-derived content the checkout carries, and no act covers that. Drafter repair (recommended): take the checkout out of every view and keep only the command shim, since the role's Syzygy commands run outside the view through the broker. The other route is to name an act, which only the owner can make. |
| N2 | revise | No | REQ-041 is fixed, but the view digest in REQ-042 and the login, managed-settings and launch-record fields in REQ-045 are still labelled Observed when shown from a stored record. Apply REQ-041's rule to them: Observed in the launching step's output, Inferred afterwards. |
| N3 | revise | Yes | The agent tool's own non-provider connections (telemetry, error reporting, update checks) are disclosed but neither covered nor refused. One option is to require each tool's switches that turn off that traffic, observed per version, and refuse where none are observed (drafter repair). The other is to ask the owner whether the 2026-10-14 Q2 ruling extends to such connections. |
| N4 | revise | No | design.md slice 4 still names the "one-commit clone", and slice 8 runs the command without `--clone`. Align both with REQ-040. |
| N5 | revise | No | The design's prototype section does not say that the authoring session gets no tool limit (a general Bash, WebFetch, WebSearch and ambient MCP under auto mode), nor that each helper's Bash is a general shell. Disclose both. |
| N6 | revise | No | On resume, the binary, version, login, managed-settings, exclusion, limit and host checks are not re-run. Run them before every session start, resumed starts included. |
| N7 | revise | No | REQ-041's "started before its input exists" conflicts with resume, which starts a fresh helper after its brief already exists. Read it as "before its input is delivered to it", or exempt resumed starts. |
| n1 | note | No | "SHALL NOT widen during the run" in practice needs a deny-unless-pre-approved mode (`dontAsk`), which stays forbidden until observed. Name `--allow-dangerously-skip-permissions` too. |
| n2 | note | No | Say where the first per-version observation is made, for example an attended probe outside a launched run. Until then no launched run can start, which fails closed. |
| n3 | note | No | Line 13 should also say "and of this requirement". |
| n4 | note | No | Quote the second REQ-033 displacement exactly ("write reach"), except `drafts/` for the author, and cover REQ-035's "new terminal only" sentence. |
| n5 | note | No | Prose drift: the packet's Observed sentence, proposal line 130's refusal list, and the unchecked review box in tasks.md. |
| n6 | note | Yes | Requiring `--clone` means the operator runs a clone command before the one command. That departs from "the user only ever runs one command". A source-acquisition act covering a Syzygy-made fetch would remove the cost; only the owner can take that act. |
| n7 | note | No | Say whether `CLAUDE_CONFIG_DIR`, `HOME` and `CODEX_HOME` are admitted to the environment. The private configuration home depends on one of them. |
| n8 | note | No | Say whether the content-class limit covers the brief, the instructions file and command output, not only packets. |
| n9 | note | No | The REQ-044 Oracle tests only the command line Syzygy builds. Say that the real tool's enforcement rests on the per-version observation. |
| n10 | note | No | Round-1 note 21 is still Unknown: it rests on material outside this repository. |

Next step, on the owner's or the lead's direction:
1. Answer N3 and n6, and possibly N1.
2. Repair N1–N7 and the notes.
3. Run a round 3.
