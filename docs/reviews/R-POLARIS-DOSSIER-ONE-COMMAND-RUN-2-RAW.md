# Review R-POLARIS-DOSSIER-ONE-COMMAND-RUN-2
Reviewed commit: 5f026d9cadacba639454d4e4d393d63174267810
Subject SHA-256: 2a1c7442152655a4557d86f70442dbec871757ec1ba584efc5ebe61e579f60e2
Verdict: REVISE

Reviewer: fresh-context reviewer, round 2 (confirming round over repaired bytes). Not the author.

## What was checked

- [Observed] `git rev-parse HEAD` returned 5f026d9cadacba639454d4e4d393d63174267810, the expected commit.
- [Observed] `sha256sum` of `proposed/polaris-generation/spec.md` returned
  2a1c7442152655a4557d86f70442dbec871757ec1ba584efc5ebe61e579f60e2, the expected digest. Both match.
- Read in full: all six files of `openspec/changes/polaris-dossier-one-command-run/` (spec.md,
  proposal.md, design.md, OWNER-PACKET.md, tasks.md, ROUND-1-REPAIRS.md) and the round-1 raw
  `docs/reviews/R-POLARIS-DOSSIER-ONE-COMMAND-RUN-1-RAW.md`.
- Repair diff: `git diff --stat 8afadc55..5f026d9c` touches only the change directory and the round-1 raw.
  [Observed] No file under `apps`, `scripts` or `packages` changed, and no warrant-YAML line changed.
- Governing references read: the five named decisions under `.syzygy/governance/decisions/` in full;
  signed REQ-033 (local-agent spec lines 9-29) and REQ-035 (lines 320-328); `doctrine/security.md`
  lines 40-119.
- Displacement quotations: a Python check (`str.count`) over spec lines 67 and 116 against the signed
  local-agent spec. [Observed] All 8 quoted predecessor strings occur in the signed text (each once,
  except "the printed command", which occurs 3 times, all on signed line 326). The 7 replacement
  strings occur 0 times in the signed text, as expected.
- Prototype: `packages/polaris-dossier/src/polaris.ts` lines 282, 340, 353, 380-404, 446-447;
  `session-view.ts` by search; `session-handover.ts` lines 66, 70 and by search.
- Help quotations: `claude --help` and `codex exec --help` were run locally. [Observed] Claude Code's
  `--permission-mode` choices are "acceptEdits", "auto", "bypassPermissions", "manual", "dontAsk"
  and "plan". It also has `--allow-dangerously-skip-permissions` ("Enable bypassing all permission
  checks as an option"). Codex has `--approve-for-me`, `--dangerously-bypass-approvals-and-sandbox`
  and `--dangerously-bypass-hook-trust`. The forbidden-mode names in REQ-045 are accurate.
- Test change (criterion 7): `polaris-authority-sweep.test.ts` lines 28-37 and 138-169 are unchanged
  since round 1. [Observed] Every decision id in the warrant YAML still matches `DOSSIER_DECISION` or
  `DOSSIER_RUNNER_DECISION`. The round-1 assessment stands, and there is no finding. The test was not
  executed.
- Not checked: any target repository, dossier state root or run directory (forbidden). The contents
  of the Butlers-measurement evidence files in this repository were not opened. No `syzygy`, npm or
  node command was run.

## Round-1 finding closure

| # | Status | Reason (quoted) and citation |
|---|---|---|
| 1 | partly closed | Spec closed. Line 9 reads "Syzygy SHALL make no clone or fetch of the repository itself ... the command SHALL refuse when no `--clone` is given". In the prose, design.md slice 4 (line 149) still lists "one-commit clone", and slice 8 (lines 160-161) runs the command with no `--clone`. See N4. |
| 2 | partly closed | REQ-041 line 65 is repaired: "label each of these Observed only in the output of the step that makes the launch ... this requirement displaces no part of that rule". The same defect stands in REQ-042 line 114 ("record each view by digest ... labelled Observed") and in REQ-045 lines 246, 248 and 252 ("in the launch record, labelled Observed"; "The launch record SHALL hold, labelled Observed"; "the launch record ... SHALL also hold, labelled Observed"). Round 1 named both. See N2. |
| 3 | closed | Line 67 now displaces the signed sentence exactly: "each is labelled Inferred and attributed to whoever declared it. Syzygy SHALL refuse an inventory or verdict whose declared launch form is neither, and neither SHALL count until its launch form is declared." [Observed] It is verbatim at signed line 324. |
| 4 | closed | Line 67 reads "The command Syzygy prints for a waiting session" and "the printed command" as "the command line Syzygy runs for the launched session". Line 248 gives "the tools of its role and no other ... never a general shell, and no tool that fetches, searches or otherwise reaches the network". |
| 5 | closed | Line 208: "Syzygy SHALL start each launched session with no tool that can run a program other than the Syzygy commands its role is allowed ... Syzygy SHALL refuse the launched run". The Case at line 227 adds a probe "to start a program from the clone". |
| 6 | partly closed | The session-tool route is closed at line 248. Line 112 still accepts and only discloses the tool's own non-provider connections: "a connection the agent tool itself opens beyond its provider is not prevented". Line 112 also mounts the Syzygy checkout readable in every view. See N1 and N3. |
| 7 | closed | Line 246 names `bypassPermissions`, `auto`, `acceptEdits`, `--dangerously-skip-permissions`, `--dangerously-bypass-approvals-and-sandbox`, `--dangerously-bypass-hook-trust` and `--approve-for-me`, and adds "a mode not so named counts as forbidden until it has been observed". See n1 for one flag it does not name. |
| 8 | closed | Line 112 states each role's working directory and writable paths, and "the session's private configuration home of REQ-polaris-generation-045 read-write". Lines 63 and 248 refer to REQ-042. |
| 9 | closed | Line 13: "SHALL be that of REQ-polaris-generation-033 to 036 and of REQ-polaris-generation-041 to 045". See n3 for a small residue. |
| 10 | closed | proposal.md line 91 ("a child process of its own supervisor"), lines 98-104 (the per-role view), lines 44-46 (the `LAUNCH_FORMS` claim, dated) and lines 147-149 (Q2 answered); design.md lines 56-62 (the mounts). |
| 11 | partly closed | design.md lines 188-207 now disclose the six items. They do not disclose that the prototype's authoring session gets no tool limit at all (see N5). |
| 12 | closed | Line 246: "SHALL remove every copy of the credential file it made ... SHALL record each removal, and SHALL report a copy it could not remove as a finding". The round-1 point about refresh-token rotation is not addressed [Inferred: low impact]. |
| 13 | closed | Line 163: "A permission here is an approval the agent tool grants a session for a tool use". Line 192: "permissions come from each stand-in's own record of the approvals it received". |
| 14 | closed | Line 163: "that is the operator's own act and not input under REQ-polaris-generation-035, and the review page SHALL disclose that whether the operator typed into a helper's pane is Inferred". |
| 15 | closed | Line 11: "a session that reaches its time bound under REQ-polaris-generation-045 counts as no result, and the step that needed its result refuses". |
| 16 | closed | OWNER-PACKET.md lines 58-60: "This packet's drafter added that RFC7-20 and the public egress record would then apply; that addition is not in the 2026-10-08 packet." |
| 17 | closed | tasks.md lines 10-12: "Each answer took the drafted arm, so no requirement was struck or narrowed." |
| 18 | closed | Line 112: "a delivery Syzygy makes under REQ-polaris-generation-035, of a packet it built and recorded by digest, is not such a copy". |
| 19 | closed | Line 114: "where a path these views forbid to a role lies inside a path that role's view mounts ... naming both paths". The Case (line 142) and the Falsifier (line 146) follow. |
| 20 | closed | REQ-045's indirect reading of REQ-042 is gone. Line 248 now reads "as REQ-polaris-generation-042 gives them for its role". |
| 21 | closed (no change) | ROUND-1-REPAIRS.md line 36: "No change." Both observations are still [Unknown] to this review. |

## New findings

N1. [revise] Every launched session can read the whole Syzygy checkout, so the agent tool can send
its contents, Butlers-derived content included, to its provider. No act covers that, and it is not
refused (criteria 1 and 3). Line 112 gives every view "the Syzygy checkout read-only". The repaired
line 248 gives each role "read tools over the paths its view makes readable". The rulings the change
rests on concern target content: `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` item 2 says "The
operator's agent session sending target content to its own provider is the operator's own act", and
line 254 cites only that ruling, packet Q2 and the repair-and-disclose item 2. [Observed] The checkout
carries Butlers source structure. `AGENTS.md` line 617 names Butlers file names, and `AGENTS.md` notes
that retained raws quote Butlers paths. `OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`
lines 110-111 say: "No act lets a launched CLI receive Butlers content." The Syzygy repository is
itself a governed project under SEC-2. [Observed] The prototype binds the checkout read-only into
every view (`session-view.ts` lines 37-38 and 53; `polaris.ts` line 391). [Inferred] The checkout is
not needed inside a view for reading: line 112 has a session's Syzygy commands run "outside its view",
and the prototype already forwards them through a broker. The repair is one of three: take the
checkout out of the views and keep only the shim the commands need; limit read tools to the role's
own paths (the clone and the session's directory or `drafts/`); or name an act that covers the send.
This predates round 1, but the repaired line 248 makes it explicit.

N2. [revise] The residue of round-1 finding 2: stored launch-record fields outside REQ-041 are still
labelled Observed, against the undisplaced REQ-033 rule "Syzygy SHALL NOT rest an Observed label on a
record it stored" (local-agent spec line 25). The affected text is REQ-042 line 114 ("labelled
Observed as the view Syzygy requested") and REQ-045 line 246 (the login check "in the launch record,
labelled Observed"), line 248 ("The launch record SHALL hold, labelled Observed, each managed-settings
location") and line 252 ("SHALL also hold, labelled Observed"). REQ-041's limit applies to "each of
these", meaning REQ-041's own fields. It does not plainly reach the REQ-042 and REQ-045 fields, and
REQ-042 line 132 has "every page" disclose the view "as requested by Syzygy" with no label for a later
display. Each should carry REQ-041's rule: Observed in the launching step's output, Inferred where it
is shown from the stored record.

N3. [revise] The agent tool's own connections to destinations other than its provider are disclosed
but neither covered nor refused (criterion 1; round-1 finding 6 asked for one or the other). Line 112:
"a connection the agent tool itself opens beyond its provider is not prevented, and that none was
opened is Inferred." No act or direction in force names such connections; packet Q2 is headed
"provider transmissions" (OWNER-PACKET line 55). [Inferred] Such connections include telemetry,
error reporting and update checks, some to third parties. Whether they carry target content is
[Unknown]. The repair is one of two. The spec could require each tool's switches that turn off
non-essential traffic, observed per tool and version, and refuse where none are observed; the
`--plugin-url`, `--file`, `--remote-control` and `--chrome` flags are already excluded by line 248's
"in no other way". Or the change could name this as an owner question that extends the Q2 ruling.

N4. [revise] The prose still describes the Syzygy-made fetch that REQ-040 now forbids (criterion 6).
design.md lines 148-150, slice 4: "The state machine above over the existing step functions,
one-commit clone, run-limit question, resume". Slice 8 (lines 160-161) runs "`syzygy polaris
https://github.com/redis/redis`" with no `--clone`, which REQ-040 refuses (line 9). An implementer who
follows the slice list builds the step that line 9 forbids.

N5. [revise] The prototype section does not disclose that the authoring session gets no tool limit
(criterion 6; this bears on SEC-3 and on egress). [Observed] `polaris.ts` line 395 starts the author
with `--permission-mode auto` and two `--allowedTools` entries, and passes no `--tools`, no
`--disallowedTools` and no `--strict-mcp-config`. The helpers get all three (lines 396-397). The
author therefore has Claude Code's default tool set: a general Bash, WebFetch, WebSearch and ambient
MCP servers. Their use is gated only by the auto-mode classifier. Each helper's Bash is likewise a
general shell under auto mode (`session-handover.ts` line 70: `WAITING_TOOLS = ['Read', 'Glob',
'Grep', 'Bash']`). design.md discloses auto mode (line 192) and the missing settings-source flag
(lines 208-209). It never says that the prototype departs from REQ-044 line 208 and REQ-045 line 248
("the tools of its role and no other").

N6. [revise] On resume, the binary and version checks are not re-run, so a resumed run can start
sessions under a tool version whose limits and exclusions were never observed (fails open; criterion
2). REQ-045 line 250 places the executable, path and version check "Before `init`". REQ-040 line 11
has `--resume` continue "from its first unfinished step", and `init` is not re-run. The login,
managed-settings and limit checks say "Before any session starts" (lines 246, 248), which reads most
naturally as before the run's first session. REQ-044 line 208 makes the same check before "any
session starts". [Inferred] Claude Code can update itself between a stop and a resume, and during a
long run. The fix: make the REQ-045 executable, version, login, managed-settings, exclusion and limit
checks, and REQ-042's host check, before every session start, a resumed start included, and refuse
otherwise.

N7. [revise] REQ-041 and REQ-040's resume contradict each other (criterion 4). Line 63: "Each helper
session SHALL be started before its input exists". A stop ends every session (line 163: "stopping
SHALL end every launched session"). The resume scenario (lines 33-34) then continues "at the
inventory step", which needs a new inventory session whose brief already exists. A conforming
implementation cannot meet both. REQ-041 should exempt a resumed start, or should read "before its
input is delivered to it".

n1. [note] REQ-043 line 163 now requires that permissions "SHALL NOT widen during the run". This is
stricter than the Q5 answer ("no session gains any permission while detached"), and it fails closed.
In practice it needs a tool mode that denies anything not pre-approved, so that an operator who is
attached cannot approve a prompt in a pane. For Claude Code that mode is `dontAsk`, which line 246
treats as forbidden until observed. The Falsifier (line 193) tests widening only "while detached".
Line 246 also does not name `--allow-dangerously-skip-permissions`, which lets the bypass mode be
switched on in the middle of a session. It is a flag, not a mode, so the catch-all "a mode not so
named" may not reach it.

n2. [note] The rules "observed ... in a stand-in or attended run whose record is retained as evidence"
(lines 208 and 248) have no stated way to start. A stand-in cannot show what the real tool does, and
a launched run refuses until the observation exists. The change should say where the first
observation is made, for example an attended probe outside a launched run. Until then no launched run
can start. That fails closed.

n3. [note] Line 13 says every "refusal ... SHALL be that of REQ-polaris-generation-033 to 036 and of
REQ-polaris-generation-041 to 045". REQ-040 adds refusals of its own: no `--clone`, and the three
resume refusals on line 11. The line should say "and of this requirement".

n4. [note] Line 116's second displacement, "in the disclosure that the records Syzygy read for its
gates lie within the agent sessions' reach", paraphrases the signed text and does not quote it. The
signed text (line 27) reads "lie within the agent sessions' write reach". The replacement "MAY claim
that directory is outside the agent sessions' write reach" makes no exception for `drafts/`, which
lies inside the state directory and is writable by the author (line 112). Also, the signed REQ-035
sentence "Syzygy SHALL print its command for a new terminal only" (line 326) is not addressed for
launched runs.

n5. [note] Prose drift. OWNER-PACKET.md lines 34-36 say "In a launched run Syzygy records each launch
itself (Observed)" and line 38 lists what stays Inferred. Neither reflects the repaired rule that a
stored launch record is Inferred on later pages. proposal.md line 130 lists only "a bypass-permissions
mode" among the refusals and leaves out automatic-approval modes. tasks.md lines 26-28 leave the
round-1 review unchecked, although its raw is retained.

n6. [note] This is an owner choice. With `--clone` now required (line 9), the operator runs a clone
command before the one command, which departs from the owner's words "the user only ever runs one
command" (proposal lines 25-30). The fail-closed arm is right, but OWNER-PACKET.md does not put this
cost to the owner. A source-acquisition act that covers a Syzygy-made fetch would be the way to
remove it.

n7. [note] Line 246's environment allow-list "admits no variable selecting, redirecting or
authenticating a model provider, with no exception". The spec does not say whether `CLAUDE_CONFIG_DIR`,
`HOME` or `CODEX_HOME` count. Each selects which credential file the tool reads. The private
configuration home of line 248 depends on one of them. A strict reading forbids that route and fails
closed. Say which of them are admitted.

n8. [note] Line 254 limits only "Packets Syzygy itself writes for a launched session" to the classes
the statement lists. The brief, the role's instructions file (line 248) and the Syzygy command output
returned to a session are also content Syzygy gives the tool. Say whether the limit covers them.

n9. [note] REQ-044's Oracle (line 229) and the stand-in Case (line 227) test the command line Syzygy
builds. They cannot show that the real tool enforces the limit. That rests on the per-version
observation of line 208, which the Form block does not test. Say so in the Oracle.

n10. [note] Round-1 note 21 remains [Unknown] to this review: the Redis `run.json` figures and the
bubblewrap observation rest on material outside this repository.

Counts: 7 revise, 10 notes (17 new findings); round-1 closure: 16 closed, 4 partly closed, 0 not closed, 1 closed with no change.
