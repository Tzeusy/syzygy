# Review — PR 406 session-prompt tool statement gate
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: b077815b9302b57ea5c8cea1eae4d0ad0d1d3e42
Reviewer: fresh-context

## Scope and method

Subject: PR #406, head `b077815b`, bead syzygy-up98. The finding under repair
is R-DOSSIER-AGENT-PROVIDER-V2-1 F1 (raw lines 66-85). The PR touches 4 files
(`git diff --stat origin/main...b077815b`): `cli.ts` (usage text),
`review.test.ts`, `session-handover.ts` and the new evidence JSON
`docs/evidence/session-prompt-tool-statement-mutants-2026-10-08.json`.

Runs, in a scratch worktree detached at `b077815b` after `npm ci`, removed
afterwards:
- `vitest run --project @syzygy/polaris-dossier review.test.ts inventory.test.ts`
  gave 90 passed of 90 (2 files). That matches the evidence record's
  `totalTests: 90`.
- the whole `@syzygy/polaris-dossier` project gave 929 passed and 1 skipped of
  930 (26 files).
- one reviewer mutant (R1, below), which survived. The file was restored
  from git afterwards.

## Criterion 1: the finding is closed

[Observed] `session-handover.ts:143-146`: the tool is still
`request.tool ?? declared.agentTool`. It is now followed by
`sessionStatementRefusal(opened, tool, deps.sources, now)`, and a non-null
result returns `refuse('statement', …)`. The function (`:225-235`) returns
null only when `opened.contentClasses === null`, or when
`providerStatementGate(records, tool, provider, now)` is `ok` for
`provider = opened.declared.agentProvider` and every class in
`opened.contentClasses` is in that statement's classes.

Every way a session's tool or provider is chosen or overridden. Population: 6
surfaces, swept over `cli.ts` (every command branch), `session-handover.ts`,
`run-config.ts`, `reverify.ts`, and the readers of the prompt records in
`inventory.ts:420` and `review.ts:634`.
1. Run configuration `agentTool` and `agentProvider`. They are gated at `init`
   (`init.ts:133`) and by the step guard at every step (`reverify.ts:156`).
   Once briefed, they are pinned to the brief record (`reverify.ts:131`).
   Unchanged by the PR.
2. `session-prompt --tool`. Now gated: closed.
3. `session-prompt --tool-version` and `--model`. They are not part of the
   (tool, provider) pair, and no statement names them.
4. Session provider. There is no `--provider` flag (`cli.ts`, the
   `session-prompt` branch parses only `--kind --tool --tool-version
   --model`). The session pair always takes the run's declared provider.
5. `launch-form`. It records only the form and chooses no tool
   (`session-handover.ts`, `launchForm`).
6. `review-packet`. It writes the packet under `reviews/` and hands it to no
   session and no tool.

[Observed] At this commit `STATEMENT_FORMS['redis-redis']`
(`gate-sources.ts:233-238`) defines exactly two pairs:
(`claude-code`, `anthropic`) and (`codex`, `openai`). The session provider is
always the run's (item 4), so for a governed or unstated Redis run any
`--tool` other than the declared one forms (`codex`, `anthropic`) or
(`claude-code`, `openai`). No form exists for either, so both are refused.
[Inferred] So F1's failing input, `session-prompt <run> review --kind fidelity
--tool codex` on a claude-code/anthropic governed run, is refused at this
commit, and no remaining surface hands a newly built packet or inventory brief
to an uncovered pair. Two exceptions remain, E2 and N2.

## Criterion 2: non-governed runs need no session statement

[Observed] Spec `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:11`
(REQ-polaris-generation-033): "For a non-governed subject the agent sessions'
sends are the operator's own act as stated above and no statement is
required. For a governed subject, and for a subject whose project input does
not state whether a drawer exists, Syzygy SHALL refuse to issue a brief unless
an in-force, recorded, per-project statement names the operator's agent
provider and the content classes it may receive". The scenario "Non-governed
subject needs no statement" (`:113-117`) says: "Syzygy issues the brief
without a per-project statement".

The clause speaks of "the agent sessions'" sends in the plural, so it covers
the inventory and review sessions as well as the authoring session. The lane's
choice matches it. [Observed] `contentClasses` is null exactly when
`governed.statementRequired` is false (`reverify.ts:153-165`), and that is
`kind !== 'non-governed'` (`governed.ts:54`). So "unstated" drawer subjects
are checked, as the clause requires.

What the spec does and does not require: the spec keys the statement to the
**provider** only ("names the operator's agent provider"). REQ-035
(`spec.md:324`) records "the agent tool, version and model of the authoring,
inventory and review contexts as the operator declares them". It records no
per-context provider. Neither requirement contains any clause about a session
tool differing from the run's. The (tool, provider) narrowing comes from the
statement record itself. Its "What it does not do" section of
`instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md` says it "permits ... no
other tool or provider". It also comes from the gate's SEC-2 reading
(`gate-sources.ts:296-298`). The PR's check is stricter than the spec and
does not contradict it.

## Criterion 3: refusal before any write, typed and readable

[Observed] The gate runs at `:145-146`, which is before
`sessionsRootViolation` (`:163`), before `reviewSession` (and so before
`writePacket` and every `mkdirSync`/`writeFileSync`), and before
`buildInventoryBrief`. `openRun` writes nothing. A `session-prompt` refusal
appends no step-log line, the same as every other `session-prompt` refusal.
The refusal is typed: `{ command: 'session-prompt', outcome: 'refused', stage:
'statement', reason, disclosures }`. Its reason names the tool, the provider
and the gate's `why`, or names the classes that are missing. The design kind
takes the same path: the gate runs before the kind dispatch. The tests do not
exercise the design kind (N3).

## Criterion 4: packet digests

[Observed] `review.ts`, `render.ts`, `reverify.ts` and `class-gate.ts` are
not in the diff. The packets stay class-gated on `opened.contentClasses`, the
run's classes (`review.ts:202`, `render.ts:262`). `review-check` rebuilds with
that same value. So the digest Syzygy rebuilds is unchanged by the PR.
[Inferred] It is also identical whichever tool the session uses. The whole
package suite, which includes the review-check rebuild tests, passed (929/930,
1 skipped).

## Criterion 5: the mutants

[Observed] The record stores `old`/`new`/`file`/`tests` for all 9 mutants, the
subject commit `df6e26c0`, the runner path and the runner's sha256. It also
stores the sha256 of the mutated file and of both test files. I re-derived all
four digests at `b077815b` and they match. `git diff --stat df6e26c0
b077815b` shows only the evidence file. The recorded counts are 9 killed of 9.

Predicate coverage:
- wiring: U1
- the null branch, both directions: U2, U3
- tool, not the declared tool, in the gate and in the classes: U4, U5
- the subset check, its presence and its direction: U6, U9
- absent statement: U7
- provider: U8

The unrun equivalent mutant, `?? []`, is justified. [Observed]
`providerStatementGate` returns `ok` iff `liveStatements(...).length === 1`
(`gate-sources.ts:303`). `statementContentClasses` returns non-null iff the
same filter over the same arguments gives length 1 (`:291-293`). After an `ok`
gate the fallback cannot be reached.

Gaps are listed under E1 and N1.

## Criterion 6: governed planes

[Observed] The diff touches no path under `.syzygy/**` or `openspec/**`
(4 files, listed above).

## Findings

**E1 — the "writes no session" test does not cover the packet written under
`reviews/`; a late gate survives** (low)

`packages/polaris-dossier/src/review.test.ts` (new `it.each` "refuses a review
and an inventory session … and writes no session"). The test checks three
things: the sessions root holds only `session-1`, `reviews/fidelity-session-1.json`
is absent and `inventory/session-2.json` is absent. It does not check
`reviews/fidelity-packet-<sha>/`, which `writePacket` (`review.ts:257-263`)
writes as the first act of `reviewSession`. [Observed] Reviewer mutant R1:
- at `session-handover.ts:146`, change
  `if (unstated !== null) return refuse('statement', unstated);` to
  `if (unstated !== null && request.role !== 'review') return refuse('statement', unstated);`;
- after `writePacket(run, kind, built);` in `reviewSession`, insert
  `const late = await sessionStatementRefusal(opened, context.agentTool, deps.sources, now); if (late !== null) return refuse('statement', late);`.

Result: review.test.ts + inventory.test.ts **90 passed of 90 (survived)**.
Failing input the suite does not catch: under R1, `session-prompt <run> review
--kind fidelity --tool codex` with no codex statement writes the packet
directory and then refuses. The shipped code is correct (criterion 3). Only
the test's predicate is narrower than "refusal before anything is written".
Repair: assert that the `reviews/` listing, or the whole run directory's file
set, is unchanged across the refused call.

**E2 — the session pair's statement is neither cited nor re-checked after the
hand-over** (low, latent at this commit)

`session-handover.ts:225-235` discards `statement.record`. The prompt record's
`context` (`:151-160`) cites no statement. The readers that count an
inventory or a verdict read only the prompt's digest and the launch form
(`inventory.ts:420-427`, `review.ts:634-641`). They never read the session's
tool or re-check its pair. Spec `spec.md:11`: "its withdrawal SHALL refuse
further steps of any run that relies on it".

Failing input (fixture world): a governed run declared claude-code/anthropic,
with a further in-force (`codex`, `anthropic`) statement. `session-prompt
review --kind fidelity --tool codex` is issued. The codex statement is then
withdrawn, and `review-check` and `render` still count that session's
verdict. The run's own statement, which the step guard re-checks, is
unaffected.

A run directory whose codex prompt record was issued before this fix is also
counted unchanged. [Unknown] whether any such run directory exists.

[Inferred] The gap cannot be reached for new hand-overs with this commit's
`STATEMENT_FORMS`, where any override is refused (criterion 1). It becomes
reachable once a form for a second tool with the same provider is added.
Repair: either record the admitting statement in the prompt record's
`context` and re-check it when the session's inventory or verdict is counted,
or disclose the limit.

**N1 — the ambiguous arm is untested, and its reason reads "no statement in
force"** (note)

`session-handover.ts:229-230`. When two in-force statements name the session
pair, `providerStatementGate` returns `refused` with "… is ambiguous"
(`gate-sources.ts:304`). The wrapper prefixes that with "has no per-project
statement in force". No test supplies two live codex statements. [Inferred]
The mutant `statement.state !== 'ok'` → `statement.state === 'absent'` would
not be killed by any test. It would still refuse, because of the `?? []` and
subset check. The `?? []` is equivalent only while the gate condition holds
intact. Add one fixture row with two in-force codex statements.

**N2 — the session's provider is the run's, by construction** (note)

`session-handover.ts:227`: `const provider = opened.declared.agentProvider;`.
No flag declares a session provider, and REQ-035 (`spec.md:324`) records only
"the agent tool, version and model" per context. [Inferred] A codex session
whose real provider differs from the run's would be checked against
(codex, run-provider). Today no such form exists, so the check fails closed.
The model is a spec property (one provider per run), not a defect of this PR.
State it in the disclosure or the design if the forms ever admit a
cross-provider tool.

**N3 — the design kind is not exercised** (note)

The new tests cover `review --kind fidelity` and `inventory` only. [Observed]
The gate precedes the kind dispatch (`:145` versus `:165`), so design is
covered by construction. Neither U1 nor R1 would distinguish a gate placed
inside the fidelity branch only.

## Summary

F1 is closed for every hand-over issued from this commit: 6 surfaces were
swept, and the one tool-choosing surface is now gated. The non-governed
exemption matches REQ-033's "no statement is required" for the agent
sessions. Refusal precedes every write, and the refusal is typed. Packet
digests are untouched. The mutant record is re-runnable, and its digests
re-derive.

Exceptions:
- E1: a test predicate narrower than the claim. R1 survived.
- E2: the session statement is uncited and not re-checked, which is latent
  under this commit's forms.

Neither exception reopens F1's failing input.
