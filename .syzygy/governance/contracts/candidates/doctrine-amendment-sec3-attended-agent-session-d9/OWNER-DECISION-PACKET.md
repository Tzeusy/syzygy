# Doctrine amendment packet — D9 (proposed): your own agent session may run the project you are observing

**Status: DRAFT. Not applied, not adopted; binds nothing.** Amending
doctrine is an owner act (VIS-4). An agent session drafted this packet on
2026-10-05, as the review-1 rulings direction asked, and repaired it twice on
2026-10-06. It edits no doctrine byte and authorizes no implementation. A
commit, a merged pull request, a review, a closed bead or silence performs
nothing. Only your own words, in your own session, do.

**Review state.** Rounds 1 and 2 returned `REVISE`
(docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md and
docs/reviews/R-DOCTRINE-AMENDMENT-D9-2-RAW.md). After round 2 the stopping
rule brought the package to you, and on 2026-10-06 you answered two
questions (POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-DIRECTION.md, section 1
below). Each finding was repaired once more, as recorded in
`ROUND-2-DISPOSITIONS.md`. Round 3 is the last confirming round. If it
returns `REVISE`, this packet comes back to you with all three raws.

**Identifier.** `D9` is provisional. The amendment log holds D1, D5 and D6,
and D3, D7 and D8 are open packets. If another packet is adopted first and
takes D9, this one takes the next free number.

**Companions in this directory:**

- `SEMANTIC-DELTA.md`: the exact current and proposed text for both arms;
- `IMPACT-LEDGER.md`: everything that cites SEC-3, and what happens to it;
- `REVIEW-BRIEF.md`;
- `ROUND-1-DISPOSITIONS.md` and `ROUND-2-DISPOSITIONS.md`.

---

## 1. What you decided, and why this packet exists

On 2026-10-05 you said three things:

- the Polaris dossier is written by your own Claude Code or Codex session
  over a local clone;
- "in the local-agent mode" that session may build and run the project it is
  reading, for example starting `redis-server` to see how it behaves;
- claims resting on such a run are labelled Inferred, and the run record
  lists the commands the agent says it ran.

A fresh-context review then pointed out that SEC-3, as written, forbids
this:

> **SEC-3 — Observed code is untrusted, everywhere.** Observed-project code
> runs only inside an explicit, opt-in execution profile.

The text does not say *who* runs the code. So a session you start on your
machine, running Redis because a Syzygy brief said it may, is observed code
running outside a profile.

You were offered three options, with SEC-3 quoted to you:

- **"Only in a sandbox"** (recommended at the time): the session may run the
  project only inside a contained environment.
- **"Forbid, disclose"**: the session may not run the project.
- **"Allow on host, amend SEC-3"**: the option you chose.

You also directed that this amendment be drafted, reviewed and adopted
before the dossier mode can be signed. Until then, nothing in the dossier
mode may tell an agent to run observed code outside a profile.

**What you answered on 2026-10-06, after round 2.** Round 2 found that the
recommended text permits more than the dossier: any Syzygy instruction, in
any feature, could let your attended session run the project once a choice
was recorded. This packet had called that text minimal. You chose **"Any
feature, per-run choice"**: any Syzygy instruction may permit execution,
but only on a choice you record for that one run, naming what it covers,
with no standing approval. You also chose to extend the credential
condition to every process the session starts, for as long as any runs, and
to allow one more review round. Those answers settle the *scope* of the
recommended text. They do not adopt it: adoption is still yours, below.

## 2. The recommended text (arm A), in plain words

- **SEC-3 says whose rule it is.** The rule binds Syzygy itself, anything
  Syzygy launches or schedules, and every instruction a Syzygy feature gives
  an agent: a brief, prompt, skill or work item. None of them runs observed
  code outside a profile, or tells anything else to, except in one case.
- **The one case, in any feature.** Syzygy may give an instruction that lets
  an agent session run the project when three things hold. The session is
  on your own machine. You started it and attend it, meaning you are present
  to see and stop what it does. And you have recorded a choice for that one
  run, naming what the instruction covers. A standing approval, or one
  recorded once per project, does not count.
- **This is wider than your dossier ruling, by your 2026-10-06 choice.** It
  is not limited to the dossier. A future feature that dispatches a work
  item telling a worker to run the project's tests falls under the same
  case, needs a choice you record for each run, and needs no new doctrine
  act.
- **The conditions:**
  1. Your choice for the run is recorded before Syzygy gives the
     instruction.
  2. Anything learned by running the project is labelled Inferred, never
     Observed.
  3. Every command the session says it ran is disclosed, as the session's
     own account. This matches your words: "the run record lists the
     commands".
  4. *(Optional, Q3)* Syzygy keeps the credentials it holds for its
     adapters where neither the session nor any process it starts can read
     them, for as long as any of them runs. "Read" means at the
     operating-system level, not merely blocked by the agent's own tool
     permissions, which the processes it starts ignore.
- **Whom the case binds: Syzygy, not the session.** Syzygy never gives the
  instruction to a session it started or to one left running unattended,
  and never asks for a process that outlives the session. Those are limits
  on Syzygy's instruction. Once the instruction is given, SEC-3 governs what
  Syzygy does about the session, not what the session does. If you walk
  away, or the session leaves a server running, SEC-3 does not forbid it;
  the cost below is what you accept. Condition 4, if adopted, is still
  Syzygy's duty for as long as any process the session started runs.
- **The cost, written into the rule.** The session runs with your own
  credentials and network, including Syzygy's endpoints and any Syzygy
  credential readable on that machine. Code it runs can reach them, and can
  change any file you can, the clone included. Nothing contains it. The rule
  records that you accepted this risk instead of a sandbox-only rule or a
  ban.
- **Kept word for word.** "Untrusted, everywhere", "It is untrusted whoever
  owns the project", the profile rules, and the original violation, "an
  execution profile that inherits the host user's ambient credentials 'for
  convenience.'"
- **Why the case is not that violation.** The rule says so outright: the
  exposure to your credentials is the same. What differs is that nothing
  pretends otherwise. The case claims no containment, runs only on a choice
  you recorded for that run, and nothing it produces is shown as more than
  Inferred. Two new violations are named: instructing a session before your
  choice for that run is recorded, or on a standing record; and showing a
  claim that rests on the run as Observed.

The optional second clause adds one sentence to `v1.md`'s "Observed code"
line, naming this case. The line describes Syzygy's platform and stays true
without it, so it is optional.

## 3. What you should know before deciding

The reviews found the earlier drafts wrong in several ways, and each one
bears on your choice:

- **The first draft was wider than your ruling.** It let any session you
  attend run observed code, whether or not Syzygy was involved. That text is
  still offered, as **arm W**, because you may want the general form. It is
  a widening beyond what you ruled. Round 2 brought it in line with your
  per-run answer, so it too needs a choice recorded for each run wherever
  Syzygy instructs the session.
- **The second draft was wider than this packet said.** Arm A covers every
  Syzygy feature, not only the dossier, and this packet called it "what you
  ruled and nothing more". You have now chosen that width on purpose, with
  a per-run choice. The packet no longer calls it minimal.
- **"One exception" would have made ordinary things violations.** If SEC-3
  stays actor-free and lists only this exception, then the observed
  project's own CI and a test command you type by hand become explicit SEC-3
  violations. That is arm W's cost. Arm A avoids it by naming Syzygy as the
  rule's actor. Arm A does not *permit* CI or hand-typed commands; it simply
  does not govern them.
- **Arm A turns an earlier reading into doctrine.** When you first chose
  "Allow, disclose", the question framed SEC-3 as binding only Syzygy's own
  execution. The review-1 rulings direction recorded that this "was the
  lead's reading, not the doctrine's text". Choosing arm A makes that
  reading the doctrine's text, for execution. It restores the premise of
  your first answer; it is also a change to what SEC-3 says today.
- **A Syzygy tool already runs observed code without a profile, today.**
  `npm run poc:capture-test-artifact` is Syzygy code that runs Butlers'
  focused pytest suite directly, with your environment. Verification can
  then show `Verified`, when the commit matches, the run exits 0 and the
  capture time is in range. This breaks SEC-3 as written today,
  independently of D9. It also breaks RFC 0005's gate, and the POC coverage
  line "POC never executes Butlers code". Neither arm cures it. It is tracked
  as bead `syzygy-4mbu`; no code is changed here.
- **Two accepted contract clauses change in effect.** RFC 0005 says
  execution consent is required: "Absent: no observed code runs" (RFC5-12).
  It also says Syzygy's adapter credentials are "never visible to
  observed-project code" (RFC5-24). In the case D9 permits, observed code
  runs without an execution consent. Unless condition 4 is adopted, Syzygy's
  adapter credentials could be visible to it. That is Q3.
- **Who records your choice is left to the specification.** Doctrine
  requires your choice to be recorded before the instruction, but does not
  say how the record shows that it is yours. In the dossier design (PR #353)
  the agent records it in a state directory that the agent can edit. The
  dossier specification may close that; doctrine leaves it open.

There is one more thing you should know plainly. The craft-and-care security
clause, CC-SEC-3, binds every Syzygy change. It names "run the project's
own test command to get better evidence" as "exactly the tempting
violation". A dossier brief that lets the agent run the project to observe
it is that case, word for word (Q4).

## 4. What else this touches

The full list is in `IMPACT-LEDGER.md`: 241 files cite SEC-3 at
`origin/main` `eb7be564`, and each is classified. Most are unaffected,
because they describe Syzygy's own pipelines, which still never run observed
code. The dossier specification (PR #353) waits on this act. Its execution
rule must carry whatever conditions you adopt, word for word. Applying the
amendment regenerates seven derived files, and none of them needs a decision
from you.

## 5. Your questions

Q1 and Q2 were one choice presented as two (round 2, N1), so Q2 is folded
into Q1. The numbers of Q3–Q5 are kept, because the other files cite them.

| # | Question | Options | Recommendation |
|---|---|---|---|
| Q1 | Which text, and so whom does SEC-3's execution rule bind? | **A** arm A: the rule binds Syzygy, what it launches or schedules, and every instruction a Syzygy feature gives an agent. One permitted case, in any feature: Syzygy's instruction to your attended session, on a choice you record for that one run naming what it covers. The observed project's own CI and commands you type are not governed by SEC-3; the code stays "untrusted, everywhere" as a classification. **W** arm W: SEC-3 binds everyone, with one exception: any session you attend may run observed code on your choice, with or without Syzygy. It makes CI and hand-typed commands violations, and does not list any lawful outside execution. **D** decline: the dossier brief must forbid running the project. The `v1.md` sentence is optional under A or W | **A**, with the `v1.md` sentence. Its scope is the one you chose on 2026-10-06: any feature, per-run choice. It is wider than your dossier ruling. RFC5-19 already treats "the project's own CI artifacts" as lawful evidence produced "outside Syzygy". W is offered only if you want SEC-3 to bind everyone; a W that also listed lawful outside executions would need a new draft and review |
| Q2 | *(Folded into Q1 in round 2.)* | — | — |
| Q3 | RFC5-12 ("Absent: no observed code runs") and RFC5-24 ("never visible to observed-project code") change in effect in the permitted case. How should that be handled? | **(a)** accept and record the effect change; the contract text stays literally untrue for this case until (c). **(b)** add condition 4: Syzygy keeps its typed-adapter credentials where neither the session nor any process it starts can read them at the operating-system level, for as long as any of them runs. That keeps RFC5-24 true, including for a server the session leaves running, and does nothing for RFC5-12. **(c)** later, a conforming RFC 0005 amendment (a digest-bound contract act with its own review) scoping both clauses and the three summary sentences to Syzygy | **(b) for RFC5-24, (a) for RFC5-12, and (c) queued, not blocking.** The real cost of (b): today it costs nothing, because Syzygy holds no adapter credential [Inferred, from a code search]; the dossier mode holds no provider credential, and the daemon's machine-client credential is not RFC5-24's population. Once Syzygy holds an adapter credential, your user account must not be able to read it while any process the session started is still running, which in practice means a separate OS user or a protected store. That is the mechanism you declined for Syzygy's records on 2026-10-05 ("Separate OS user"). The cost of (a) alone: an accepted clause stays untrue in this case, recorded |
| Q4 | CC-SEC-3 now differs from doctrine, and the dossier brief is its named "tempting violation". When should it be brought in line? | **A** a conforming policy amendment after D9, without holding up the dossier sign-off. Meanwhile doctrine prevails, by CC-SEC-3's own preamble: "Doctrine's text prevails over any paraphrase here". **B** before the dossier sign-off | **A.** The clause defers to doctrine in its own text, and the edit is a separate policy change |
| Q5 | Are "attended" and "your own host" defined well enough? | **A** keep the definitions in place: you started the session and attend it, being present to see and stop what it does; its subagents are included; a session Syzygy starts is excluded. A session in an auto-approve or permission-bypass mode with you away from it is not attended. A cloud-hosted agent session is not your host; a remote VM you rent stays unsettled until you need it. **B** add a glossary entry | **A** |

**Preserved trade-off.** You chose to allow execution on your own machine
over a sandbox and over a ban, knowing the session holds your credentials.
On 2026-10-06 you chose to let any Syzygy feature use that permission, one
recorded run at a time, over limiting it to the dossier and over a standing
approval. This packet does not reopen either choice. It writes them, and
their cost, into the rule.

## 6. What adoption would not do

- It does not sign the dossier specification. That is your separate
  sign-off, which may follow adoption.
- It creates no execution profile, approves none, and is not an execution
  consent under RFC 0005.
- It changes nothing about what the session may *send* (SEC-2) or about
  secret screening (SEC-5). Your egress rulings of 2026-10-05 stand on their
  own.
- It edits no contract, no policy, no specification and no code. It does not
  fix the capture tool.

## 7. How adoption would be recorded

Doctrine amendments carry no magic phrase and bind no digest; D1, D5 and D6
set that precedent. Say it plainly, naming the arm and the Q3 choice. For
example: "Adopt D9, arm A, with the v1 sentence and the credential
condition". Then, in one commit:

1. Re-check both anchors' sha256 (in `SEMANTIC-DELTA.md`). If either has
   moved, the change goes back for a fresh review.
2. Replace the anchored lines with the chosen arm's exact bytes. If Q3(b)
   was declined, delete the credential lines and check the result against
   the digest the delta gives for that case.
3. Regenerate the seven derived files (`IMPACT-LEDGER.md` §4) and run the
   canonical battery.
4. Add a `D9` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md` with
   your words, including the Q3–Q5 answers, and close register row P-103
   with the outcome.

A declined clause is recorded in the same row as declined.
