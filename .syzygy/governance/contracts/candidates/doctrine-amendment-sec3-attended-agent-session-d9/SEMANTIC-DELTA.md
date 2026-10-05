# Semantic delta D9 — SEC-3 and the owner's attended agent session

> **Candidate — binds nothing.** Drafted 2026-10-05 and repaired twice on
> 2026-10-06: after round 1 (`REVISE`, recorded in `ROUND-1-DISPOSITIONS.md`)
> and after round 2 (`REVISE`, recorded in `ROUND-2-DISPOSITIONS.md`, under
> the owner's answers in POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-DIRECTION.md).
> It follows the form of `../policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`.
> Amending doctrine is an owner act (VIS-4); this delta is the proposal,
> never the act. The owner's questions are in `OWNER-DECISION-PACKET.md`
> (this directory). Where the two differ, the fenced blocks under "Proposed
> meaning" are the proposed text.

**Artifact(s):** `.syzygy/governance/doctrine/security.md` (sha256
`c2be53d1e25c18f9329e9e18caea2256773f584e7fd45077b9caa6323aaf4892`) and
`.syzygy/governance/doctrine/v1.md` (sha256
`99d3164f2150a0faeebe0221fe0a977cb6c9c07e8d456f328f42717b247e1505`). Both
were read on 2026-10-05 at `origin/main` `eacb85d10ed7eba1d1af6d286d5a0ccd626c641a`
and re-checked on 2026-10-06 at `origin/main`
`eb7be564605c98fcc7b5f2464b200382dd1bfe39` and
`5863d470931625e4fbbb012f8e79ef6eabb6411a`. The doctrine tree is identical at
the three commits.

**Stable IDs affected:** only `SEC-3`, amended in place. Its identifier and
its rule title ("Observed code is untrusted, everywhere") keep every byte, in
the bold lead-in form `DIRECTIVE-REGISTER.md` parses. No other rule is
renumbered, retired or reworded. Clause (b) is optional. It appends one
sentence to `v1.md`'s "Observed code" bullet and rewraps that bullet's
second line, but keeps its existing sentence word for word.

**Two arms.** The owner chooses one (packet Q1).

- **Arm A, recommended: any feature, on a choice recorded per run.** SEC-3's
  execution rule names its actor: Syzygy itself, every process Syzygy
  launches or schedules, and every instruction a Syzygy feature gives an
  agent (a brief, prompt, skill or work item). It names one permitted case,
  in any feature: Syzygy may give an instruction that lets an attended
  session, started by the owner on the owner's own host, build and run
  observed code, on a choice the owner has recorded for that one run, naming
  what the instruction covers. A standing or per-project record does not
  qualify. This is **wider than the owner's dossier ruling**, which named
  only the local-agent mode. The width is the owner's 2026-10-06 choice
  ("Any feature, per-run choice";
  POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-DIRECTION.md item 1). For example, a future feature that dispatches a work item telling
  a worker to run the project's tests falls under the same case, needs a
  choice recorded for each run, and needs no new doctrine act.
- **Arm W, wider, declared as a widening.** SEC-3 stays actor-free and
  gains one general exception: any agent session the owner starts and
  attends may run observed code whenever the owner chose that, with or
  without Syzygy. Where Syzygy instructs the session, the same per-run
  choice is required. This goes beyond the ruling, and beyond arm A, because
  it reaches sessions Syzygy does not instruct.

**Change class:** Normative [Inferred: the drafter's classification]. Under
either arm, the prohibition is narrowed for one case and obligations are
added: the conditions and two new violations. Arm A also states the rule's
actor, which the current text leaves open (packet Q1).

**Author:** agent drafting session (lane-doctrine) at the owner's direction.

**Date:** 2026-10-05; repaired twice on 2026-10-06.

## Current meaning

`security.md` lines 61–70, quoted exactly: the output of
`sed -n '61,70p' .syzygy/governance/doctrine/security.md`, each line
prefixed `> `. Those ten lines hash to sha256
`71ab005a4ad61cd18be74cf4b601382dae9016f3a9acef22de54c8d302a4c05a`.

> **SEC-3 — Observed code is untrusted, everywhere.** Observed-project code runs
> only inside an explicit, opt-in execution profile.
>
> - **It is untrusted whoever owns the project.**
> - **The profile is:** default-deny, with isolated credentials, declared
>   network access, resource limits, and gates on destructive operations.
> - **The profile contract is a blocking RFC:** no observed-project code runs
>   until it is accepted.
> - *Violation:* an execution profile that inherits the host user's ambient
>   credentials "for convenience."

`v1.md` lines 119–120, by the same method (sha256 of the two lines
`3826334a2fc50fd29ff36fdd3c3f44f4318a5a133bfcada093b65437e319d033`):

> - **Observed code:** executing it is opt-in, profiled, and blocked until the
>   execution-profile RFC is accepted (SEC-3).

**What the current text means.** "Observed-project code runs only inside an
explicit, opt-in execution profile" names no actor. Finding 8 of the first
fresh-context review of the local-agent dossier amendment
(`docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`) reads: "SEC-3's
text is not limited to code Syzygy runs." On that reading, the following are
all observed code running outside a profile, and so forbidden:

- an agent session the owner starts, running the observed project on the
  owner's host because a Syzygy brief permitted it;
- the observed project's own CI;
- a test command the owner types by hand;
- Syzygy's own operator capture tool (ledger §3.6).

The accepted contract is narrower. RFC5-19's last bullet reads: "Consuming
evidence produced **outside Syzygy** (the project's own CI artifacts, a
worker's retained gate artifact) is observation, not execution — no profile
is required to read a report; profiles govern only code Syzygy itself
launches." (`contracts/rfcs/RFC-0005/execution-profiles.md`).

## Proposed meaning

### Arm A (recommended)

**(a) `security.md`: replace lines 61–70 with exactly:**

```markdown
**SEC-3 — Observed code is untrusted, everywhere.** Syzygy runs
observed-project code only inside an explicit, opt-in execution profile.

- **It is untrusted whoever owns the project.**
- **What this binds:** Syzygy itself, every process Syzygy launches or
  schedules, and every instruction a Syzygy feature gives an agent (a brief,
  prompt, skill or work item). None of them runs observed code outside a
  profile, or tells anything else to, except in the one permitted case
  below.
- **The profile is:** default-deny, with isolated credentials, declared
  network access, resource limits, and gates on destructive operations.
- **The profile contract is a blocking RFC:** no observed-project code runs
  until it is accepted.
- **The one permitted case — the owner's attended agent session.** A Syzygy
  instruction may let an agent session build and run observed-project code
  outside a profile when three things hold: the session is on the owner's
  own host; the owner started it and attends it, being present to see and
  stop what it does; and the owner has recorded a choice for that one run,
  naming what the instruction covers. A standing or per-project record does
  not qualify. The code stays untrusted, and:
  - The owner's choice for the run is recorded before Syzygy issues the
    instruction.
  - Every claim that rests on that execution is labelled Inferred, never
    Observed.
  - Every command the session reports having run is disclosed, as the
    session's own report.
  - Syzygy keeps every credential it holds for its typed adapters where
    neither the session nor any process it starts, directly or not, can read
    it at the operating-system level, for as long as any of them runs.
- **Whom the case binds:** Syzygy. Syzygy never gives the instruction to a
  session it started or to one left running unattended, and never asks for a
  process that outlives the session. Work the session hands to its own
  subagents is part of the session. Once the instruction is given, SEC-3
  governs what Syzygy does about the session, not what the session does.
- **What the permitted case costs:** the session runs with the owner's own
  credentials and network, including Syzygy's endpoints and any Syzygy
  credential readable on that host. Observed code it runs can reach them,
  and can change any file the owner can, the clone it runs in included.
  Nothing contains it, so it gives none of a profile's guarantees. The owner
  accepted that risk over two alternatives: allowing execution only in a
  sandbox, and forbidding it.
- *Violation:* an execution profile that inherits the host user's ambient
  credentials "for convenience." The permitted case is not such a profile.
  Its exposure to the owner's credentials is the same; what differs is that
  nothing claims otherwise. It claims no containment, Syzygy instructs it
  only on the owner's recorded choice for that run, and nothing resting on
  it renders as more than Inferred. Also violations: Syzygy instructing a
  session to run observed code before the owner's choice for that run is
  recorded, or on a standing record; a claim that rests on the session's
  execution rendered Observed.
```

These 50 lines between the fences, with their trailing newline, hash to sha256
`cd2d0372263cb48e38fb6fdbbc401f2d8284c027fad957eddb7e03d6d1cce5fd`.

**(b), optional. `v1.md`: replace lines 119–120 with exactly:**

```markdown
- **Observed code:** executing it is opt-in, profiled, and blocked until the
  execution-profile RFC is accepted (SEC-3). SEC-3's one permitted case
  outside a profile is a Syzygy instruction, on the owner's recorded choice
  for that run, to the owner's own attended agent session.
```

These 4 lines between the fences, with their trailing newline, hash to sha256
`ee3c8b36fe57185ccac0d49ca8336179f64a1c5db7e188d689ff587e32a42743`.

### Arm W (wider than the ruling)

**(a) `security.md`: replace lines 61–70 with exactly:**

```markdown
**SEC-3 — Observed code is untrusted, everywhere.** Observed-project code runs
only inside an explicit, opt-in execution profile, with one exception: the
owner's own attended agent session, below.

- **It is untrusted whoever owns the project.**
- **The profile is:** default-deny, with isolated credentials, declared
  network access, resource limits, and gates on destructive operations.
- **The profile contract is a blocking RFC:** no observed-project code runs
  until it is accepted.
- **The one exception — the owner's attended agent session.** An agent
  session that the owner starts and attends on the owner's own host (a Claude
  Code or Codex CLI session, for example) may build and run observed-project
  code outside a profile when the owner has chosen that. The code stays
  untrusted, and:
  - Syzygy never instructs such a session to run observed code unless the
    owner's choice for that run, naming what the instruction covers, is
    recorded first. A standing or per-project record does not qualify.
  - Every claim that rests on that execution is labelled Inferred, never
    Observed.
  - Every command the session reports having run is disclosed wherever
    Syzygy renders anything drawn from the session, as the session's own
    report.
  - Syzygy keeps every credential it holds for its typed adapters where
    neither the session nor any process it starts, directly or not, can read
    it at the operating-system level, for as long as any of them runs.
- **What the exception does not cover:** Syzygy itself, and any process
  Syzygy launches or schedules, still runs observed code only inside a
  profile. A session Syzygy starts, or one left running unattended, is not
  the owner's attended session. Work the session hands to its own subagents
  stays part of it. A process it leaves running after it ends does not.
- **What the exception costs:** the session runs with the owner's own
  credentials and network, including Syzygy's endpoints and any Syzygy
  credential readable on that host. Observed code it runs can reach them, and
  can change any file the owner can, the clone it runs in included. Nothing
  contains it, so it gives none of a profile's guarantees. The owner accepted
  that risk over two alternatives: allowing execution only in a sandbox, and
  forbidding it.
- *Violation:* an execution profile that inherits the host user's ambient
  credentials "for convenience." The attended session is not such a profile.
  Its exposure to the owner's credentials is the same; what differs is that
  nothing claims otherwise. It claims no containment, it runs observed code
  only because the owner chose that (on a choice recorded for that run
  wherever Syzygy instructs it), and nothing resting on it renders as more
  than Inferred. Also violations: Syzygy instructing a session to run
  observed code before the owner's choice for that run is recorded, or on a
  standing record; a claim that rests on the session's execution rendered
  Observed.
```

These 47 lines between the fences, with their trailing newline, hash to sha256
`6f30724b09cbee5ad09e73ac69b13842ede9ad234a0d30d1547ed832c188e881`.

**(b), optional. `v1.md`: replace lines 119–120 with exactly:**

```markdown
- **Observed code:** executing it is opt-in, profiled, and blocked until the
  execution-profile RFC is accepted (SEC-3). SEC-3's one exception is the
  owner's own attended agent session.
```

These 3 lines between the fences, with their trailing newline, hash to sha256
`73b2036b7978622f3b2d16841df52ec65ce3417fcc6dc3be740d352ebefc9b68`.

### The credential condition (packet Q3)

Both arms carry, as the last item of their conditions list, the three lines
below. If the owner declines Q3 arm (b), delete exactly these bytes from the
chosen arm. Nothing else in the block changes: every item in the list ends
with a full stop, and no other sentence in either arm refers to this
condition.

"Read" is meant at the operating-system level: file permissions, a separate
OS user or a protected store. An agent's own tool-permission rules do not
satisfy it, because the processes the session starts do not obey them. The
condition lasts as long as any process the session started, directly or
not, still runs, so it reaches a server or background job the session
leaves behind.

```markdown
  - Syzygy keeps every credential it holds for its typed adapters where
    neither the session nor any process it starts, directly or not, can read
    it at the operating-system level, for as long as any of them runs.
```

These 3 lines between the fences, with their trailing newline, hash to sha256
`d28c1b72723ded7ca73098e2ef27ee3eb9927d844da486ae2c898759c9300fab`.

With these lines deleted, arm A (a) is 47 lines, sha256
`7eaf25dab5ddaea366397571ee0d1db14a53659e108a04d7f814439a4ef4c01a`,
and arm W (a) is 44 lines, sha256
`d6b9cf9c50399f029195cb2d6f83a65ab00bc075639c680336f6e1a6bc2777a9`.
Under arm A, SEC-4's heading then lands at line 109 of `security.md`
instead of 112 (ledger §2 and §4).

**What arm A means:**

- Observed-project code is still untrusted whoever owns the project.
- Syzygy itself, everything Syzygy launches or schedules, and every
  instruction a Syzygy feature gives an agent (a brief, prompt, skill or
  work item) run, or tell anything to run, observed code only inside a
  profile, with one exception, available to any feature. Syzygy may instruct
  an agent session on the owner's own host, which the owner started and
  attends, to build and run it, on a choice the owner has recorded for that
  one run, naming what the instruction covers. Conditions:
  - the choice for the run is recorded before the instruction is given; a
    standing or per-project record does not qualify;
  - claims resting on the run are Inferred, never Observed;
  - every command the session reports is disclosed;
  - optionally (Q3(b)), Syzygy keeps its typed-adapter credentials
    unreadable, at the operating-system level, by the session and by every
    process it starts, for as long as any of them runs.
- *Attends* is defined positively: the owner is present to see and stop
  what the session does. A session in an auto-approve or permission-bypass
  mode with the owner away is not attended [Inferred: the drafter's reading
  of "present to see and stop"].
- The case's limits bind Syzygy, not the session. Syzygy never gives the
  instruction to a session it started or to one left running unattended, and
  never asks for a process that outlives the session. Once the instruction is
  given, SEC-3 governs what Syzygy does about the session (including the
  credential condition, if adopted), not what the session does. The
  session's subagents are part of it.
- The cost is stated: the owner's credentials, Syzygy's endpoints and any
  readable Syzygy credential are exposed, and the session can write the
  clone. So are the two alternatives the owner declined.
- The original violation sentence stays verbatim. A new sentence says why
  the case is not that profile and that the exposure is the same. Two new
  violations are named: instructing a session before the owner's choice for
  that run is recorded, or on a standing record; and a claim resting on the
  run rendered Observed.
- What SEC-3's execution rule no longer reaches, because it now names
  Syzygy as its actor: the project's own CI, commands the owner types, and
  sessions the owner starts and Syzygy does not instruct. They are not
  permitted by SEC-3, only not governed by it. This makes the reading
  "SEC-3 only binds Syzygy's own execution", which the review-1 rulings
  direction called "the lead's reading, not the doctrine's text", the
  doctrine's text for execution (packet §3).
- Who writes the record of the owner's choice, and how it shows that the
  choice is the owner's, is left to the specification (packet §3).
- The title, "untrusted, everywhere", still classifies the code everywhere.

**What arm W means:** the same conditions, but the exception is not tied to
Syzygy's instruction. Any agent session the owner starts and attends may run
observed code on the owner's choice. That choice must be recorded, per run,
only when Syzygy instructs the session. Because the rule stays actor-free
and names only this one exception, the project's CI and the owner's
hand-typed commands become explicit SEC-3 violations [Inferred]. Arm W is
kept only because the owner may want SEC-3 to bind everyone.

## What explicitly does NOT change

- Kept byte for byte: SEC-3's identifier and title, and the bullets
  "**It is untrusted whoever owns the project.**", "**The profile is:** …"
  and "**The profile contract is a blocking RFC:** …".
- Kept byte for byte: the violation sentence "an execution profile that
  inherits the host user's ambient credentials "for convenience."".
- The text of accepted RFC 0005. The amendment creates no profile, no profile
  class and no consent class, and the owner's recorded choice is not an
  RFC5-12 execution consent. Two RFC 0005 clauses do change in *effect* in
  the permitted case: RFC5-12's "Absent: no observed code runs", and RFC5-24's
  "never visible to observed-project code" unless Q3(b) is chosen. Ledger
  §3.2 and packet Q3 cover them.
- SEC-1, SEC-2, SEC-4, SEC-5 and every VIS rule. The amendment says nothing
  about what the session may send (SEC-2; the owner's 2026-10-05 egress
  rulings stand on their own) or about secret screening (SEC-5).
- Syzygy's own pipelines. Every adopted specification that cites SEC-3
  (ledger §3.4) describes code Syzygy runs or reads, and each one still holds.

## Warrant

- **Owner direction:** `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  item 2: "In the local-agent mode the operator's agent session may build
  and run the observed project". Claims resting on the run are Inferred, and
  "the run record lists the commands the agent reports having run".
- **Owner direction:** `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`
  item 1. The owner selected "Allow on host, amend SEC-3" over "Only in a
  sandbox (Recommended)" and "Forbid, disclose". The dossier amendment "may
  not be signed until that doctrine amendment has been adopted by the
  owner's act". Until then, "nothing in the dossier mode may tell an agent
  to run observed code outside an execution profile."
- **Doctrine on amendment:** VIS-4, and the doctrine README: "The owner
  adopts every amendment, and downstream artifacts must be re-checked for
  alignment when it changes".

## Evidence or decision basis

- Finding 8 of `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`
  (verdict REVISE), quoted under "Current meaning".
- [Observed] `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`
  discloses that the lead's earlier question framed SEC-3 as binding only
  Syzygy's own execution, and that this "was the lead's reading, not the
  doctrine's text". The owner then answered with SEC-3 quoted.
- Round 1 of this package (docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md,
  `REVISE`) found three problems. The general exception was wider than the
  ruling (R2). The "one exception" form would make CI and hand-typed commands
  violations (R3). RFC5-12 and RFC5-24 change effect (R4). Arm A is the
  repair.
- Round 2 (docs/reviews/R-DOCTRINE-AMENDMENT-D9-2-RAW.md, `REVISE`) found
  that arm A covered any feature while the packet called it minimal (F1),
  and that the credential condition did not reach processes the session
  leaves running (F2). The owner answered both on 2026-10-06
  (POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-DIRECTION.md): any feature, on a
  choice recorded per run, and the condition extended to every process the
  session starts.
- The cost sentence rests on accepted text. RFC5-24 and RFC5-20 keep
  Syzygy's credentials and interfaces out of every profile ("no credential
  to Syzygy, and no route to Syzygy"), and the attended session has neither
  guarantee. Finding 1 of the dossier review showed that code the session
  runs can rewrite the clone Syzygy later reads.
- The owner's records ruling (`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`)
  took "Re-derive, label Inferred" over "Separate OS user" and "Sandbox the
  agent" for Syzygy's records on that machine. Q3(b)'s future cost uses the
  same mechanism the owner declined there (packet Q3).

## Terms introduced / retired

- **Introduced:** *the owner's attended agent session*, defined in place: an
  agent session on the owner's own host, which the owner started and
  attends, being present to see and stop what it does. Its subagents are
  part of it. Syzygy never gives the instruction to a session it started or
  to one left running unattended, and never asks for a process that
  outlives the session.
- **Introduced (arm A):** *an instruction a Syzygy feature gives an agent*,
  defined in the text itself: "a brief, prompt, skill or work item". A
  skill or prompt kit that Syzygy ships is covered whether or not Syzygy
  emits it at run time. A repository instruction file the owner keeps for
  their own repository, such as `AGENTS.md`, is not a Syzygy feature's
  instruction [Inferred; ledger §3.6].
- **Introduced:** *a choice recorded for that one run, naming what the
  instruction covers*. A standing or per-project record does not qualify.
  Who writes the record is left to the specification.
- **Retired:** none.
- *Operator* is not a doctrine term. The dossier specification's "operator"
  is doctrine's *owner* (the glossary: "the single human accountable";
  multi-user operation is deferred).

## Downstream impact

See `IMPACT-LEDGER.md`. In short:

- CC-SEC-3 paraphrases SEC-3's old reach, and the dossier brief is its named
  case (packet Q4).
- RFC5-12's "Absent:" limb and RFC5-24's "never visible" limb change effect
  in the permitted case (packet Q3).
- The capture tool `poc:capture-test-artifact` runs observed pytest without
  a profile. It is non-conforming today, independent of D9, and stays so
  under either arm (ledger §3.6).
- Seven derived files must be regenerated on application: four context
  fixtures, the budget report, the contract index and the directive
  register.
- The local-agent dossier amendment (PR #353) is the one dependent waiting on
  this act.

## Migration / supersession plan

On adoption, in one commit:

1. Re-check both anchors' sha256 (above). If either has moved, the change is
   a new review subject: re-anchor it through a fresh review (rule 10).
   Never apply judgment at the keyboard.
2. Replace the anchored lines with the fenced bytes of the chosen arm, for
   each adopted clause. If Q3(b) was declined, delete the credential lines
   and check the result against the no-credential digest given above.
3. Regenerate the seven derived files named by the ledger's application
   probe.
4. Add the `D9` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md`
   quoting the owner's words, and mark this package adopted.
5. Run the canonical battery.

A declined clause is recorded in the same row as declined.

## Review

VIS-3 requires a fresh-reader review; the brief is `REVIEW-BRIEF.md`.

- Round 1: `REVISE`, repaired once (`ROUND-1-DISPOSITIONS.md`).
- Round 2: `REVISE`; brought to the owner, who answered on 2026-10-06, and
  repaired once (`ROUND-2-DISPOSITIONS.md`).
- Round 3: the last confirming round. A `REVISE` returns to the owner.
