# Doctrine amendment packet — D9 (proposed): your own agent session may run the project you are observing

**Status: DRAFT — not applied, not adopted; binds nothing.** Doctrine
amendment is an owner act (VIS-4). An agent session drafted this packet on
2026-10-05, as the review-1 rulings direction asked. It edits no doctrine
byte and authorizes no implementation. A commit, a merged pull request, a
review, a closed bead or silence performs nothing; only your own words in
your own session do.

**Review state.** Not yet reviewed. `REVIEW-BRIEF.md` (this directory) is
the brief for a fresh-context review. This packet comes to you after that
review, with its verdict.

**Identifier.** `D9` is provisional. The amendment log holds D1, D5 and D6;
D3, D7 and D8 are open packets. If another packet is adopted first and takes
D9, this one takes the next free number.

**Companions in this directory:** `SEMANTIC-DELTA.md` (exact current and
proposed text), `IMPACT-LEDGER.md` (everything that cites SEC-3, and what
happens to it), `REVIEW-BRIEF.md`.

---

## 1. What you decided, and why this packet exists

On 2026-10-05 you said that the Polaris dossier is to be written by your own
Claude Code or Codex session over a local clone, and that this session may
build and run the project it is reading. For example, it may start
`redis-server` to see how it behaves. Claims that rest on such a run are
labelled Inferred, and the run record lists the commands the agent says it
ran.

A fresh-context review then pointed out that SEC-3, as written, forbids
this:

> **SEC-3 — Observed code is untrusted, everywhere.** Observed-project code
> runs only inside an explicit, opt-in execution profile.

The text says nothing about *who* runs the code. So a session you start, on
your machine, running Redis because a Syzygy brief said it may, is observed
code running outside a profile.

You were offered three options, with SEC-3 quoted to you:

- **"Only in a sandbox" (recommended at the time):** the session may run
  the project only inside a contained environment.
- **"Forbid, disclose":** the session may not run the project.
- **"Allow on host, amend SEC-3":** the option you chose.

You also directed that this amendment be drafted, reviewed and adopted
before the dossier mode can be signed. Until then, nothing in the dossier
mode may tell an agent to run observed code outside a profile.

## 2. What the amendment says, in plain words

SEC-3 keeps its title, its "untrusted whoever owns the project" rule, its
profile requirements, and its original violation example word for word. It
gains one exception:

- **Who:** an agent session that *you* start and *you* attend, on *your*
  own machine. A session Syzygy starts, or one left running unattended, does
  not count.
- **When:** only when you have chosen to let it run the project.
- **Three conditions:**
  1. Syzygy never tells such a session to run the project unless your
     choice is recorded first.
  2. Anything learned by running the project is labelled Inferred, never
     Observed.
  3. The commands the session says it ran are shown beside the claims they
     support, as the session's own account.
- **What does not change:** Syzygy itself, and anything Syzygy launches or
  schedules, still runs observed code only inside a profile.
- **The cost, written into the rule:** the session runs with your own
  credentials and network, including any Syzygy credential or endpoint on
  that machine. Code it runs can reach them, and can change any file you
  can, the clone included. Nothing contains it. The rule records that you
  accepted this risk instead of a sandbox-only rule or a ban.
- **Why this is not the forbidden "ambient credentials for convenience"
  profile:** that violation is a *profile*, Syzygy's own containment, that
  quietly carries your credentials, so a run that looks contained is not.
  The attended session claims no containment. It runs the project only on
  your recorded choice, and nothing it produces is shown as more than
  Inferred. The credential exposure is real either way, and the text says
  so; it does not pretend otherwise.

A second, smaller clause adds one sentence to `v1.md`. Its "Observed code"
line says execution is "opt-in, profiled, and blocked until the
execution-profile RFC is accepted". The added sentence reads: "SEC-3's one
exception is the owner's own attended agent session."

**One thing to know before adopting.** The exception names no Syzygy
feature, so it is general. It also covers your ordinary development
sessions that run tests in a project Syzygy observes, which the current text
arguably forbids. Its conditions bind only what Syzygy instructs and
displays. [Inferred: the drafter's reading.] If you want it limited to the
dossier mode, say so (Q1, arm C).

## 3. What else this touches

The full list is in `IMPACT-LEDGER.md`: 240 files cite SEC-3, and each is
classified. Most are unaffected, because they describe Syzygy's own
pipelines, which still never run observed code. Three are worth your
attention:

- **CC-SEC-3**, the craft-and-care security clause, still says observed
  code "never executes outside an accepted profile". It names "run the
  project's own test command to get better evidence" as "exactly the
  tempting violation". Its own preamble says doctrine prevails over its
  wording, so after adoption doctrine wins where they differ. The sentence
  would still stand, though, and it changes only by a policy amendment (Q2).
- **RFC 0005**, the accepted execution-profile contract, says profiles
  "govern only code Syzygy itself launches" (RFC5-19). That fits this
  amendment. Two reader-map sentences in the same package say "no
  observed-project code executes until this RFC is accepted and a
  per-project profile exists". Read literally, they are wider (Q3).
- **The dossier specification** (PR #353) waits on this act, and its
  execution rule must match whatever text you adopt.

Applying the amendment regenerates seven derived files (four context
fixtures, the budget report, the contract index, the directive register). None of
them needs a decision from you.

## 4. Your questions

| # | Question | Options | Recommendation |
|---|---|---|---|
| Q1 | Adopt D9? | **A** adopt (a) and (b) as drafted; **B** adopt (a) only; **C** adopt with the exception limited to sessions working for a Syzygy mode (a redraft and a new review); **D** decline, so the dossier brief must forbid running the project | **A.** It is the smallest text that carries your ruling, and (b) keeps `v1.md` from reading as a flat "always profiled" |
| Q2 | CC-SEC-3 now differs from doctrine. When should it be brought in line? | **A** a conforming policy amendment after D9, without holding up the dossier sign-off (doctrine prevails meanwhile, by CC-SEC-3's own preamble); **B** before the dossier sign-off | **A.** The clause defers to doctrine in its own text, and the edit is a separate category |
| Q3 | RFC 0005: rely on RFC5-19's scope, or amend the contract? | **A** rely on RFC5-19 ("profiles govern only code Syzygy itself launches"), with no contract change; **B** commission a conforming RFC 0005 amendment, which is a digest-bound act | **A**, unless the review finds that RFC5-18 reaches the attended session. A reviewer who finds that should report it to you, not resolve it |
| Q4 | Should "attended agent session" get a glossary entry in the doctrine README? | **A** no: it is defined where it is used; **B** yes | **A** |

**Preserved trade-off.** You chose to allow execution on your host over a
sandbox and over a ban, knowing that the session holds your credentials.
This packet does not reopen that choice. It writes the choice, and its
cost, into the rule.

## 5. What adoption would not do

- It does not sign the dossier specification. That remains your separate
  sign-off, which may follow adoption.
- It creates no execution profile, approves none, and is not an execution
  consent under RFC 0005.
- It changes nothing about what the session may *send* (SEC-2) or about
  secret screening (SEC-5). Your egress rulings of 2026-10-05 stand on
  their own.
- It edits no contract, no policy and no specification.

## 6. How adoption would be recorded

Doctrine amendments carry no magic phrase and bind no digest (D1, D5 and D6
precedent). Say it plainly, for example "Adopt D9", or "Adopt D9 (a) only".
Then, in one commit:

1. Re-check both anchors' sha256 (in `SEMANTIC-DELTA.md`). If either has
   moved, the change goes back for a fresh review.
2. Replace the anchored lines with the delta's exact proposed bytes.
3. Regenerate the seven derived files (`IMPACT-LEDGER.md` §4) and run the
   canonical battery.
4. Add a `D9` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md` with
   your words, and close register row P-103 with the outcome.

A declined clause is recorded in the same row as declined.
