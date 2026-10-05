# Doctrine amendment packet — D9 (proposed): your own agent session may run the project you are observing

**Status: DRAFT. Not applied, not adopted; binds nothing.** Amending
doctrine is an owner act (VIS-4). An agent session drafted this packet on
2026-10-05, as the review-1 rulings direction asked, and repaired it once on
2026-10-06. It edits no doctrine byte and authorizes no implementation. A
commit, a merged pull request, a review, a closed bead or silence performs
nothing. Only your own words, in your own session, do.

**Review state.** Round 1 returned `REVISE`
(docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md). Every finding was repaired
once, as recorded in `ROUND-1-DISPOSITIONS.md`. Round 2 is the confirming
round. If it also returns `REVISE`, this packet comes to you with both raws.

**Identifier.** `D9` is provisional. The amendment log holds D1, D5 and D6,
and D3, D7 and D8 are open packets. If another packet is adopted first and
takes D9, this one takes the next free number.

**Companions in this directory:**

- `SEMANTIC-DELTA.md`: the exact current and proposed text for both arms;
- `IMPACT-LEDGER.md`: everything that cites SEC-3, and what happens to it;
- `REVIEW-BRIEF.md`;
- `ROUND-1-DISPOSITIONS.md`.

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

## 2. The recommended text (arm A), in plain words

- **SEC-3 says whose rule it is.** The rule binds Syzygy itself, anything
  Syzygy launches or schedules, and any instruction Syzygy's software
  issues, such as a dossier brief. None of them runs observed code outside a
  profile, or tells anything else to, except in one case.
- **The one case.** When you have chosen it, and your choice is recorded
  first, Syzygy may issue an instruction that lets an agent session run the
  project. The session must be on your own machine, and you must have
  started it and be attending it.
- **The conditions:**
  1. Your choice is recorded before Syzygy issues the instruction.
  2. Anything learned by running the project is labelled Inferred, never
     Observed.
  3. Every command the session says it ran is disclosed, as the session's
     own account. This matches your words: "the run record lists the
     commands".
  4. *(Optional, Q3)* No credential Syzygy holds for its adapters is
     readable by the session.
- **Where the case ends.** A session Syzygy starts, or one left running
  unattended, does not count. Subagents of your session are part of it. A
  process left running after the session ends is not, and Syzygy never asks
  for one.
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
  pretends otherwise. The case claims no containment, runs only on your
  recorded choice, and nothing it produces is shown as more than Inferred.

The optional second clause adds one sentence to `v1.md`'s "Observed code"
line, naming this case. The line describes Syzygy's platform and stays true
without it, so it is optional.

## 3. What you should know before deciding

Round 1 found the first draft wrong in four ways, and each one bears on your
choice:

- **The first draft was wider than your ruling.** It let any session you
  attend run observed code, whether or not Syzygy was involved. It called
  itself "the smallest text", but it was only the smallest in words. That
  text is still offered, as **arm W**, because you may want the general
  form. It is a widening beyond what you ruled, not the carrier of your
  ruling.
- **"One exception" would have made ordinary things violations.** If SEC-3
  stays actor-free and lists only this exception, then the observed
  project's own CI and a test command you type by hand become explicit SEC-3
  violations. That is arm W's cost. Arm A avoids it by naming Syzygy as the
  rule's actor. Arm A does not *permit* CI or hand-typed commands; it simply
  does not govern them. Whether SEC-3 should govern them is Q2.
- **A Syzygy tool already runs observed code without a profile, today.**
  `npm run poc:capture-test-artifact` is Syzygy code that runs Butlers'
  focused pytest suite directly, with your environment. Verification then
  shows `Verified`. This breaks SEC-3 as written today, independently of D9.
  It also breaks RFC 0005's gate, and the POC coverage line "POC never
  executes Butlers code". Neither arm cures it. It is reported here and
  routed for a separate fix; no code is changed.
- **Two accepted contract clauses change in effect.** RFC 0005 says
  execution consent is required: "Absent: no observed code runs" (RFC5-12).
  It also says Syzygy's adapter credentials are "never visible to
  observed-project code" (RFC5-24). In the case D9 permits, observed code
  runs without an execution consent. Unless condition 4 is adopted, Syzygy's
  adapter credentials could be visible to it. That is Q3.

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

| # | Question | Options | Recommendation |
|---|---|---|---|
| Q1 | Which text? | **A** arm A: the rule binds Syzygy and what it launches, schedules or instructs, with one permitted case, Syzygy's instruction to your attended session on your recorded choice. **W** arm W: any session you attend may run observed code, with or without Syzygy; wider than your ruling, and it makes CI and hand-typed commands violations. **D** decline: the dossier brief must forbid running the project. The `v1.md` sentence is optional under A or W | **A**, with the `v1.md` sentence. A permits what you ruled and nothing more. W is offered only if you want the general form |
| Q2 | Should SEC-3's execution rule bind anyone other than Syzygy, such as the observed project's own CI or a command you type by hand? | **No:** SEC-3's execution rule governs Syzygy, what it launches or schedules, and what its software instructs; the code stays "untrusted, everywhere" as a classification (arm A's text). **Yes:** it binds everyone, and a redraft must list which outside executions are lawful, or CI and hand-typed commands are violations | **No.** RFC5-19 already treats "the project's own CI artifacts" as lawful evidence produced "outside Syzygy", and doctrine governs what Syzygy does. A Yes needs a new draft and a new review |
| Q3 | RFC5-12 ("Absent: no observed code runs") and RFC5-24 ("never visible to observed-project code") change in effect in the permitted case. How should that be handled? | **(a)** accept and record the effect change; the contract text stays literally untrue for this case until (c). **(b)** add condition 4: no credential Syzygy holds for its typed adapters is readable by the session. That keeps RFC5-24 true, and does nothing for RFC5-12. **(c)** later, a conforming RFC 0005 amendment (a digest-bound contract act with its own review) scoping both clauses and the three summary sentences to Syzygy | **(b) for RFC5-24, (a) for RFC5-12, and (c) queued, not blocking.** The real cost of (b): today it costs nothing, because Syzygy holds no adapter credential [Inferred, from a code search]; the dossier mode holds no provider credential, and the daemon's machine-client credential is not RFC5-24's population. Once Syzygy holds an adapter credential, it must be unreadable by your user during attended runs, which means a separate OS user or a protected store. That is the mechanism you declined for Syzygy's records on 2026-10-05 ("Separate OS user"). The cost of (a) alone: an accepted clause stays untrue in this case, recorded |
| Q4 | CC-SEC-3 now differs from doctrine, and the dossier brief is its named "tempting violation". When should it be brought in line? | **A** a conforming policy amendment after D9, without holding up the dossier sign-off. Meanwhile doctrine prevails, by CC-SEC-3's own preamble: "Doctrine's text prevails over any paraphrase here". **B** before the dossier sign-off | **A.** The clause defers to doctrine in its own text, and the edit is a separate policy change |
| Q5 | Are "attended" and "your own host" defined well enough? | **A** keep the definitions in place (started and attended by you; subagents included; processes left running excluded; a session Syzygy starts excluded); a cloud-hosted agent session is not your host; a remote VM you rent stays unsettled until you need it. **B** add a glossary entry | **A** |

**Preserved trade-off.** You chose to allow execution on your own machine
over a sandbox and over a ban, knowing the session holds your credentials.
This packet does not reopen that choice. It writes the choice, and its cost,
into the rule.

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
   was declined, delete the credential lines.
3. Regenerate the seven derived files (`IMPACT-LEDGER.md` §4) and run the
   canonical battery.
4. Add a `D9` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md` with
   your words, including the Q2–Q5 answers, and close register row P-103
   with the outcome.

A declined clause is recorded in the same row as declined.
