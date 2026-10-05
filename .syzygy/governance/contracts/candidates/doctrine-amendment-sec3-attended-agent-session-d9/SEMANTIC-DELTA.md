# Semantic delta D9 — SEC-3 and the owner's attended agent session

> **Candidate — binds nothing.** Drafted 2026-10-05 in the form of
> `../policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. Doctrine amendment is
> an owner act (VIS-4); this delta is the proposal, never the act. The
> owner's questions live in `OWNER-DECISION-PACKET.md` (this directory).
> Where the two differ, the fenced blocks under "Proposed meaning" below are
> the proposed text.

**Artifact(s):** `.syzygy/governance/doctrine/security.md` (sha256
`c2be53d1e25c18f9329e9e18caea2256773f584e7fd45077b9caa6323aaf4892`) and
`.syzygy/governance/doctrine/v1.md` (sha256
`99d3164f2150a0faeebe0221fe0a977cb6c9c07e8d456f328f42717b247e1505`), both
read on 2026-10-05 at `origin/main` commit
`eacb85d10ed7eba1d1af6d286d5a0ccd626c641a`.

**Stable IDs affected:** `SEC-3` only, amended in place. Its identifier and
its rule title ("Observed code is untrusted, everywhere") keep every byte, in
the bold lead-in form `DIRECTIVE-REGISTER.md` parses. No other rule is
renumbered, retired or reworded. Clause (b) adds one sentence to `v1.md`'s
"Platform and audience" list and changes none of its existing bytes.

**Change class:** Normative, widened [Inferred: the drafter's
classification]. Today SEC-3's text admits no execution of observed-project
code outside a profile, by anyone. After (a), one named case is lawful: an
agent session the owner starts and attends on the owner's own host, running
observed code because the owner chose that, under three conditions. A design
that was compliant before stays compliant. One that was not compliant becomes
compliant only inside that case.

**Author:** agent drafting session (lane-doctrine) at the owner's direction.

**Date:** 2026-10-05

## Current meaning

`security.md` lines 61–70, quoted exactly. The quotation below is the
output of `sed -n '61,70p' .syzygy/governance/doctrine/security.md` at the
commit above, each line prefixed `> `. Those ten lines hash to sha256
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
explicit, opt-in execution profile" names no actor. The first fresh-context
review of the local-agent dossier amendment (finding 8) found that the text is
not limited to code Syzygy runs. That raw is not on `main` at this commit; the
finding and the owner's answer are recorded in
`decisions/POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`, which
says the narrower framing "was the lead's reading, not the doctrine's text".
On the text as written, an agent session that the owner starts and that runs
the observed project on the owner's host, because a Syzygy brief permitted
it, is observed code running outside a profile. That is forbidden.

The accepted contract that implements SEC-3 is narrower. RFC5-19 reads:
"Consuming evidence produced **outside Syzygy** (the project's own CI
artifacts, a worker's retained gate artifact) is observation, not execution
— no profile is required to read a report; profiles govern only code Syzygy
itself launches." (`contracts/rfcs/RFC-0005/execution-profiles.md`, RFC5-19,
last bullet). This amendment does not rest on RFC5-19. The owner directed a
doctrine amendment rather than a reading. Ledger §3.2 records how the two
relate.

## Proposed meaning

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
    owner's choice is recorded first;
  - every claim that rests on that execution is labelled Inferred, never
    Observed;
  - the commands the session reports having run are disclosed with the
    claims they support, as the session's own report.
- **What the exception does not cover:** Syzygy itself, and any process
  Syzygy launches or schedules, still runs observed code only inside a
  profile. A session Syzygy starts, or one left running unattended, is not
  the owner's attended session.
- **What the exception costs:** the session runs with the owner's own
  credentials and network, including any Syzygy credential or endpoint on
  that host. Observed code it runs can reach them, and can change any file
  the owner can, the clone it runs in included. Nothing contains it, so it
  gives none of a profile's guarantees. The owner accepted that risk over two
  alternatives: allowing execution only in a sandbox, and forbidding it.
- *Violation:* an execution profile that inherits the host user's ambient
  credentials "for convenience." The attended session is not such a profile:
  it claims no containment, it runs observed code only on the owner's
  recorded choice, and nothing resting on it renders as more than Inferred.
  Also violations: Syzygy telling an agent session to run observed code
  before the owner's choice is recorded; a claim that rests on the session's
  execution rendered Observed.
```

The block's bytes between the fences hash to sha256
`857184d82b8b54fcfb630a21aac3b1872551cfbc55cbee41b2544cb6a28e3e74`.

**(b) `v1.md`: replace lines 119–120 with exactly:**

```markdown
- **Observed code:** executing it is opt-in, profiled, and blocked until the
  execution-profile RFC is accepted (SEC-3). SEC-3's one exception is the
  owner's own attended agent session.
```

The block's bytes between the fences hash to sha256
`73b2036b7978622f3b2d16841df52ec65ce3417fcc6dc3be740d352ebefc9b68`.

**What the proposed text means:**

- Observed-project code is still untrusted whoever owns the project.
- Syzygy, and every process Syzygy launches or schedules, still runs it only
  inside a profile.
- One case is newly lawful: an agent session that the owner starts and
  attends on the owner's own host may build and run observed code because the
  owner chose that. Three conditions apply:
  - Syzygy never instructs such a session to run observed code before the
    owner's choice is recorded;
  - claims resting on that execution are Inferred, never Observed;
  - the commands the session reports having run are disclosed with the
    claims they support, as the session's own report.
- The text states the cost (ambient credentials, Syzygy's own included;
  write reach over the clone) and the two alternatives the owner declined.
- The original violation example stays verbatim, with a sentence saying why
  the attended session is not that profile. Two new violations are named.

## What explicitly does NOT change

- SEC-3's identifier and title, and the bullets "**It is untrusted whoever
  owns the project.**", "**The profile is:** …" and "**The profile contract
  is a blocking RFC:** …", byte for byte.
- The violation sentence "an execution profile that inherits the host user's
  ambient credentials "for convenience."", byte for byte.
- Every execution-profile clause of accepted RFC 0005 (RFC5-18…RFC5-23,
  RFC5-24's credential rule). The amendment creates no profile, no profile
  class and no consent class. The owner's recorded choice is not an
  RFC5-12 execution consent and approves no profile.
- SEC-1, SEC-2, SEC-4, SEC-5 and every VIS rule. In particular, the exception
  says nothing about what the session may *send* (SEC-2: the owner's
  2026-10-05 egress ruling stands on its own, unchanged here) or about secret
  screening (SEC-5).
- Syzygy's own pipelines. Every adopted specification that cites SEC-3
  (ledger §3.4) describes code Syzygy runs or reads, and each one still holds.
- `v1.md`'s existing sentence, byte for byte; clause (b) only appends.

## Warrant

- **Owner direction:** `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  item 2 (the agent session "may build and run the observed project"; claims
  resting on it Inferred; commands listed).
- **Owner direction:**
  `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md` item 1 (PR
  #356; not on `main` when drafted). The owner selected "Allow on host, amend
  SEC-3" over "Only in a sandbox (Recommended)" and "Forbid, disclose". The
  direction says the dossier amendment "may not be signed until that doctrine
  amendment has been adopted by the owner's act", and "Until then, nothing in
  the dossier mode may tell an agent to run observed code outside an
  execution profile."
- **Doctrine on amendment:** VIS-4 and the doctrine README ("The owner adopts
  every amendment, and downstream artifacts must be re-checked for alignment
  when it changes").

## Evidence or decision basis

- The review finding quoted under "Current meaning" (finding 8 of
  `R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1`, verdict REVISE, reviewed commit
  `f1bd0b5ccb09056905e85270037eb8cd92efa918`).
- [Observed] The lead's earlier question to the owner framed SEC-3 as binding
  only Syzygy's own execution. The review-1 rulings direction discloses that
  framing as the lead's reading, not the doctrine's text. The owner then
  answered with SEC-3 quoted to them.
- The cost sentence rests on accepted text: RFC5-24 and RFC5-20 keep
  Syzygy's credentials and interfaces out of every profile ("no credential to
  Syzygy, and no route to Syzygy"). The attended session gets neither
  guarantee. The review's finding 1 showed that a session running observed
  code can rewrite the clone that Syzygy later reads.

## Terms introduced / retired

- **Introduced:** *the owner's attended agent session*, defined in place: an
  agent session the owner starts and attends on the owner's own host. A
  session Syzygy starts, or one left running unattended, is excluded.
  "Attended" is not otherwise defined in doctrine. The packet (§4, Q4) asks
  whether the doctrine README glossary should carry it.
- **Retired:** none.
- *Operator* is not a doctrine term. The dossier specification's "operator"
  is the doctrine's *owner* (glossary: "the single human accountable";
  multi-user operation is deferred).

## Downstream impact

See `IMPACT-LEDGER.md`. In short:

- one craft-and-care clause (CC-SEC-3) paraphrases SEC-3's old reach (packet
  Q2);
- RFC 0005's preamble sentences read literally as wider than RFC5-19 (packet
  Q3);
- seven derived files must be regenerated on application: four context
  fixtures, the budget report, the contract index and the directive register;
- the local-agent dossier amendment (PR #353) is the one dependent waiting on
  this act.

## Migration / supersession plan

On adoption, in one commit:

1. Re-check both anchors' sha256 (above). If either moved, the change is a
   new review subject: re-anchor through a fresh review (rule 10). Never
   apply judgment at the keyboard.
2. Replace the anchored lines with the fenced bytes for each adopted clause.
3. Regenerate the seven derived files the ledger's application probe names.
4. Add the `D9` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md`,
   quoting the owner's words, and mark this package adopted.
5. Run the canonical battery.

A declined clause is recorded in the same row as declined.

## Review

VIS-3 requires a fresh-reader review; `REVIEW-BRIEF.md` is the brief. No
review has run on these bytes.
