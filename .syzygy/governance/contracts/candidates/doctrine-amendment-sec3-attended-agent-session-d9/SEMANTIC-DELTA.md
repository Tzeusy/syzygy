# Semantic delta D9 — SEC-3 and the owner's attended agent session

> **Candidate — binds nothing.** Drafted 2026-10-05 and repaired once on
> 2026-10-06 after round 1 (`REVISE`, recorded in `ROUND-1-DISPOSITIONS.md`).
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
`eb7be564605c98fcc7b5f2464b200382dd1bfe39`. The doctrine tree is identical at
the two commits.

**Stable IDs affected:** only `SEC-3`, amended in place. Its identifier and
its rule title ("Observed code is untrusted, everywhere") keep every byte, in
the bold lead-in form `DIRECTIVE-REGISTER.md` parses. No other rule is
renumbered, retired or reworded. Clause (b) is optional. It appends one
sentence to `v1.md`'s "Observed code" bullet and rewraps that bullet's
second line, but keeps its existing sentence word for word.

**Two arms.** The owner chooses one (packet Q1).

- **Arm A, recommended, matches the ruling.** SEC-3's execution rule names
  its actor: Syzygy itself, every process Syzygy launches or schedules, and
  every instruction Syzygy's software issues. It names one permitted case:
  on the owner's recorded choice, Syzygy may issue an instruction that lets
  an attended session, started by the owner on the owner's own host, build
  and run observed code.
- **Arm W, wider, declared as a widening.** SEC-3 stays actor-free and
  gains one general exception: any agent session the owner starts and
  attends may run observed code whenever the owner chose that, with or
  without Syzygy. This goes beyond the ruling, which is scoped to the
  local-agent mode.

**Change class:** Normative [Inferred: the drafter's classification]. Under
either arm, the prohibition is narrowed for one case and obligations are
added: the conditions and two new violations. Arm A also states the rule's
actor, which the current text leaves open (packet Q2).

**Author:** agent drafting session (lane-doctrine) at the owner's direction.

**Date:** 2026-10-05; repaired 2026-10-06.

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
  schedules, and every instruction Syzygy's software issues. None of them
  runs observed code outside a profile, or tells anything else to, except in
  the one permitted case below.
- **The profile is:** default-deny, with isolated credentials, declared
  network access, resource limits, and gates on destructive operations.
- **The profile contract is a blocking RFC:** no observed-project code runs
  until it is accepted.
- **The one permitted case — the owner's attended agent session.** On the
  owner's recorded choice, Syzygy may issue an instruction that lets an
  agent session on the owner's own host, which the owner started and
  attends, build and run observed-project code outside a profile. The code
  stays untrusted, and:
  - The owner's choice is recorded before Syzygy issues the instruction.
  - Every claim that rests on that execution is labelled Inferred, never
    Observed.
  - Every command the session reports having run is disclosed, as the
    session's own report.
  - No credential Syzygy holds for its typed adapters is readable by the
    session.
- **Where the case ends:** a session Syzygy starts, or one left running
  unattended, is not the owner's attended session. Work the session hands to
  its own subagents stays part of it. A process it leaves running after it
  ends does not, and Syzygy's instruction never asks for one.
- **What the permitted case costs:** the session runs with the owner's own
  credentials and network, including Syzygy's endpoints and any Syzygy
  credential readable on that host. Observed code it runs can reach them, and
  can change any file the owner can, the clone it runs in included. Nothing
  contains it, so it gives none of a profile's guarantees. The owner accepted
  that risk over two alternatives: allowing execution only in a sandbox, and
  forbidding it.
- *Violation:* an execution profile that inherits the host user's ambient
  credentials "for convenience." The permitted case is not such a profile.
  Its exposure to the owner's credentials is the same; what differs is that
  nothing claims otherwise. It claims no containment, Syzygy instructs it
  only on the owner's recorded choice, and nothing resting on it renders as
  more than Inferred. Also violations: Syzygy instructing a session to run
  observed code before the owner's choice is recorded; a claim that rests on
  the session's execution rendered Observed.
```

These 43 lines between the fences, with their trailing newline, hash to sha256
`af06d7151abe8257e3783423143bc8d0d86ba01e46119edd9af1b4e85ea132b9`.

**(b), optional. `v1.md`: replace lines 119–120 with exactly:**

```markdown
- **Observed code:** executing it is opt-in, profiled, and blocked until the
  execution-profile RFC is accepted (SEC-3). SEC-3's one permitted case
  outside a profile is Syzygy's instruction, on the owner's recorded choice,
  to the owner's own attended agent session.
```

These 4 lines between the fences, with their trailing newline, hash to sha256
`a481b5a41bbc8fae940d989a723d597f5441b1aaff69aaebdb8a7fb5c677be2f`.

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
    owner's choice is recorded first.
  - Every claim that rests on that execution is labelled Inferred, never
    Observed.
  - Every command the session reports having run is disclosed wherever
    Syzygy renders anything drawn from the session, as the session's own
    report.
  - No credential Syzygy holds for its typed adapters is readable by the
    session.
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
  only because the owner chose that (on a recorded choice wherever Syzygy
  instructs it), and nothing resting on it renders as more than Inferred.
  Also violations: Syzygy instructing a session to run observed code before
  the owner's choice is recorded; a claim that rests on the session's
  execution rendered Observed.
```

These 44 lines between the fences, with their trailing newline, hash to sha256
`3b932aec500e2582933836a0f64b60f3e48754f8391ca2ce2d45697a1f9cf5dc`.

**(b), optional. `v1.md`: replace lines 119–120 with exactly:**

```markdown
- **Observed code:** executing it is opt-in, profiled, and blocked until the
  execution-profile RFC is accepted (SEC-3). SEC-3's one exception is the
  owner's own attended agent session.
```

These 3 lines between the fences, with their trailing newline, hash to sha256
`73b2036b7978622f3b2d16841df52ec65ce3417fcc6dc3be740d352ebefc9b68`.

### The credential condition (packet Q3)

Both arms carry, as the last item of their conditions list, the two lines
below. If the owner declines Q3 arm (b), delete exactly these bytes from the
chosen arm. Nothing else in the block changes, because every item in the
list ends with a full stop.

```markdown
  - No credential Syzygy holds for its typed adapters is readable by the
    session.
```

These 2 lines between the fences, with their trailing newline, hash to sha256
`2316b61d2bce82b795845ce1ab810cea6b01dc2bcbeb7564a3710ad61948ee17`.

**What arm A means:**

- Observed-project code is still untrusted whoever owns the project.
- Syzygy itself, everything Syzygy launches or schedules, and every
  instruction Syzygy's software issues run, or tell anything to run,
  observed code only inside a profile, with one exception. On the owner's
  recorded choice, Syzygy may instruct an agent session on the owner's own
  host, which the owner started and attends, to build and run it. Conditions:
  - the choice is recorded before the instruction is issued;
  - claims resting on the run are Inferred, never Observed;
  - every command the session reports is disclosed;
  - optionally (Q3(b)), no credential Syzygy holds for its typed adapters is
    readable by the session.
- The session's subagents are part of it. A process it leaves running after
  it ends is not, and Syzygy never asks for one.
- The cost is stated: the owner's credentials, Syzygy's endpoints and any
  readable Syzygy credential are exposed, and the session can write the
  clone. So are the two alternatives the owner declined.
- The original violation sentence stays verbatim. A new sentence says why
  the case is not that profile and that the exposure is the same. Two new
  violations are named.
- What SEC-3's execution rule no longer reaches, because it now names
  Syzygy as its actor: the project's own CI, commands the owner types, and
  sessions the owner starts and Syzygy does not instruct. They are not
  permitted by SEC-3, only not governed by it (packet Q2).
- The title, "untrusted, everywhere", still classifies the code everywhere.

**What arm W means:** the same conditions, but the exception is not tied to
Syzygy's instruction. Any agent session the owner starts and attends may run
observed code on the owner's choice. That choice must be recorded only when
Syzygy instructs the session. Because the rule stays actor-free and names
only this one exception, the project's CI and the owner's hand-typed
commands become explicit SEC-3 violations [Inferred]. Arm W is kept only
because the owner may want the general form. It is not the carrier of the
ruling.

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
  attends. A session Syzygy starts, or one left running unattended, is
  excluded. Its subagents are included. A process left running after it
  ends is excluded. Arm A also introduces *an instruction Syzygy's software
  issues*: a brief, prompt or work item that Syzygy's software emits. A
  repository instruction file the owner keeps, such as `AGENTS.md`, is not
  one [Inferred; ledger §3.6].
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
   each adopted clause. If Q3(b) was declined, delete the credential lines.
3. Regenerate the seven derived files named by the ledger's application
   probe.
4. Add the `D9` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md`
   quoting the owner's words, and mark this package adopted.
5. Run the canonical battery.

A declined clause is recorded in the same row as declined.

## Review

VIS-3 requires a fresh-reader review; the brief is `REVIEW-BRIEF.md`.

- Round 1: `REVISE`, repaired once (`ROUND-1-DISPOSITIONS.md`).
- Round 2: the confirming round.
