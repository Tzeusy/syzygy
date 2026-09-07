# Owner decision packet — seven questions about the written estate

> **Status: answered. All seven were ruled on 2026-09-07** — see
> [`DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md`](DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md),
> which owns the rulings and their application, and quotes the owner's reply
> verbatim. This packet remains the question each was ruled on; it is not the
> state of any of them, and the register rows it names have moved to
> [`DECISION-HISTORY.md`](DECISION-HISTORY.md). *(Until 2026-09-07 the line
> below read as the head of this file.)*
>
> **Marked 2026-09-07: "none depends on another" is true of the questions and
> false of the applications.** P-55 and P-57 are coupled — the `openspec/`
> index authorized by P-57 has to say what the two empty directories mean,
> and what they mean was settled only by P-55. Ruled the other way, the index
> would have described a tree about to be restructured. They were ruled
> together, so nothing went wrong.
>
> **Pending. This packet decides nothing and adopts nothing.** It states seven
> questions, gives the evidence for each, recommends an answer, and says what
> happens if you say nothing. Register rows: **P-54 … P-59 and P-66** in
> [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md). Answer all seven
> in one reply, or any subset; none depends on another — though P-58 and P-59
> are two defects on the same page and are cheapest answered together.
>
> Written 2026-09-05 during a documentation consolidation pass; P-58 and P-59
> added 2026-09-06 during the second pass, P-66 the same day during the
> fifth. Nothing in
> this packet is a change to any accepted artifact; each question exists
> precisely because the change it asks about would land on the governed plane,
> where only you may put it.

## Why these, and why together

The repository holds roughly twelve megabytes of tracked prose, most of it the
closed record of work that is finished. A consolidation pass can safely repair
navigation, staleness, and duplicate homes on the implementation side without
asking you anything — and that part is done. What remained are the items an
agent may not decide, because each would write to, remove from, or restructure
the governed plane. They are gathered here rather than raised one at a time.

---

## P-54 — The OpenSpec config file is still the vendor's example

**What is there.** `openspec/config.yaml` is five useful bytes and twenty
lines of shipped-example comment. Its only live setting is
`schema: spec-driven`. Everything below that is the OpenSpec starter template,
including a commented-out example describing a TypeScript/React e-commerce
platform and an example rule capping proposals at five hundred words.

**Why it matters.** The commented `context:` block is described in the file
itself as text "shown to AI when creating artifacts." Left as the vendor's
example, it does nothing; filled in, it becomes standing instruction to every
agent that authors a specification here. That is a governed-plane authoring
input, so what goes in it is yours to write, not an agent's to guess.

**The arms.**

- **(a)** Write a real `context:` block — the stack, the two-plane rule, the
  epistemic-labelling requirement, and the fact that a proposal binds nothing
  until you sign it. An agent can draft it for your edit; you decide the
  bytes.
- **(b)** Delete the commented example lines, leaving `schema: spec-driven`
  alone, and rule that this project's context travels through `AGENTS.md` and
  the governed plane rather than a tool config.
- **(c)** Leave it exactly as it is.

**Recommendation: (b).** The project already has a well-maintained place where
an agent learns its context, and CC-REV-3 warns against a second home for the
same answer — a populated `context:` block would become one, invisible to
anyone not reading tool config. Deleting the example is the smaller change and
removes an e-commerce paragraph that has never described this project.

**Default if unanswered:** nothing changes; the file keeps the vendor example.

---

## P-55 — `openspec/specs/` and `openspec/changes/archive/` are both empty

**What is there.** Three change directories under `openspec/changes/`:
`project-registration-and-honest-shape-visibility` (adopted 2026-08-20),
`three-surface-poc-experience`, and `polaris-project-wide-butlers-model`. The
two directories the OpenSpec convention reserves for *settled* material —
`specs/` and `changes/archive/` — are empty, and have been since the tree was
created.

**Why it matters.** In the ordinary OpenSpec lifecycle a change is archived
once it lands, and the requirements it introduced come to rest in `specs/`,
which then reads as the current specification. Here, Capability 1 is adopted
and implemented, yet its requirements are still only reachable inside a
directory named `changes/`. A reader looking for "what does this system
specify today" finds an empty `specs/` and has to know to look somewhere that
sounds provisional.

**The arms.**

- **(a)** Adopt the lifecycle: archive the adopted change and materialize its
  requirements into `specs/`. This moves adopted bytes, so it is an act, and
  it needs its own review — an agent may prepare it, never perform it.
- **(b)** Rule that this project deliberately does not use the archive and
  spec-materialization steps: `changes/` is the permanent home, and
  `.syzygy/governance/` plus `PROJECT-STATUS.md` answer "what is specified
  today." Then the two empty directories get a one-line README saying they are
  intentionally unused, so their emptiness stops reading as an omission.
- **(c)** Defer, with the emptiness disclosed as a known gap.

**Recommendation: (b).** The lifecycle move buys navigation the governed plane
already provides, at the cost of relocating bytes you have accepted and bound
by digest. Saying plainly that the convention is not used is cheaper, is
honest, and removes the only thing an empty directory currently communicates,
which is that someone forgot.

**Default if unanswered:** both directories stay empty and unexplained.

---

## P-56 — A spent owner prompt sits at the repository root

**What is there.** `syzygy_begin_specification_stage_capability1_prompt.md`,
about nine hundred lines, at the top level of the repository. It is the prompt
that opened the Capability 1 specification stage. That stage is finished:
Capability 1 is adopted and implemented.

**Why it matters.** It is not junk — the Capability 1 specification-authoring
decision record cites it, and cites it *by its location*, calling it
"(repository root)." So it is evidence for a recorded decision, and moving it
silently would break that citation. But the repository root is the first thing
a newcomer sees, and it currently carries a spent working prompt beside the
README, the licence, and the status page.

**The arms.**

- **(a)** Move it into the historical tree (alongside the other spent
  round material) and amend the one citing sentence in the decision record to
  name the new path. The decision record is not digest-bound; the amendment
  is a single-line path correction with no semantic content.
- **(b)** Leave it at the root, and add one line to its head saying it is
  spent, what it opened, and that it is kept at the root because a decision
  record cites it there.
- **(c)** Leave it entirely as is.

**Recommendation: (b).** It is cheap, it breaks no citation, and it fixes the
actual defect, which is that nothing on the page tells a reader the prompt has
already been answered. (a) is also lawful and tidier, but it edits a decision
record to buy a tidier root listing, and the trade seems the wrong way round.

**Default if unanswered:** the file stays at the root, unmarked.

---

## P-57 — `openspec/` has no door

**What is there.** No index at any level of `openspec/`. A reader arriving at
the directory sees `config.yaml`, `changes/`, `specs/`, and three change
directories whose names do not say which one is adopted, which is a bounded
non-release experiment, and which is a later repair to that experiment. One of
the three proposals also lacks the "Candidate specification" banner the other
two carry, so its status is invisible at its head — and it cannot be given
one: every byte of `polaris-project-wide-butlers-model/` is bound by the PWB
truth-and-readiness amendment performed 2026-09-05, and its `proposal.md`
still hashes to the manifest row that act's argument covers. Adding a banner
there would break a performed act's argument.

**Why it matters.** This is the same defect that was just repaired in `docs/`
and in the contract tree: authority exists and is correct, but nothing routes
a reader to it, so people navigate by guessing at directory names. The
difference is that `openspec/` is the governed plane, so an agent adding a
page there is exactly the kind of quiet governed-plane authorship the two-plane
rule exists to prevent — even when the page is pure navigation.

**The arms.**

- **(a)** Authorize an agent to write a top-level README under `openspec/` as navigation only:
  which change is adopted and under which act, which are candidate, what the
  empty directories mean (see P-55), and a banner saying the page is never
  authority. Owner review before it lands.
- **(b)** Rule that the governed plane takes no navigation pages, and route
  readers to `openspec/` from `PROJECT-STATUS.md` and `AGENTS.md` instead —
  both of which are outside the plane and already own current state.
- **(c)** Leave `openspec/` without a door.

**Recommendation: (a), with (b) as a close second.** The tree has three
sibling directories in three different states, and that is more than a
one-line pointer from elsewhere can carry honestly. But if you would rather
the governed plane stay free of agent-authored pages as a matter of principle,
(b) costs little: the same information can live in `PROJECT-STATUS.md`, which
is already the page that owns which acts are in force.

This also makes an index the *only* lawful place to disclose that third
change's status. Its head cannot carry a banner without breaking the act, so
if the answer is (b), the routing sentence in `PROJECT-STATUS.md` has to say
which of the three is bound and by which act — a pointer alone will not do.

**Default if unanswered:** `openspec/` keeps no index, and the status of the
three sibling changes stays legible only to a reader who already knows the act
record.

---

## P-58 — The two default-path pages each name "the two rules", and they name different pairs

**What is there.** Both of the project's front doors open the same way, with
the same sentence, and then diverge.

`README.md:60` says *"Two rules everything else follows from:"* and lists
**VIS-1** (comprehensible truth, never comprehensible fiction) and **VIS-2**
(no evidence means Unknown), each cited by identifier.

`.syzygy/intent/OVERVIEW.md:22` says the same sentence and lists **"No
evidence means Unknown"** and **"Doing the work is never proof the intent was
satisfied."** Neither is cited by identifier.

So the second door drops VIS-1 entirely, and in its place elevates a sentence
that doctrine does not number. In `.syzygy/governance/doctrine/vision.md`,
VIS-1 is at line 82 and VIS-2 at line 96; the "scheduled or completed work is
never proof" clause sits at line 23, inside the preamble, and is not a
numbered rule at all [Observed — swept 2026-09-06 by `grep -nF` for each rule
heading in `vision.md` and for the shared sentence in both pages].

**Why it matters.** This is a CC-REV-3 shadow-authority defect of the exact
kind that policy names: the same question — *which rules is everything else
downstream of?* — is answered in two homes, and the homes disagree. A reader
who arrives through `OVERVIEW.md` learns a two-rule doctrine that omits the
rule doctrine itself ranks first, and learns it without an identifier they
could check. Neither page is wrong about doctrine's *content*; both sentences
are true things the doctrine says. What is wrong is that each page presents
its own pair as the closed set.

CC-REV-3 also says an agent that finds one question answered in two homes
surfaces the contradiction rather than silently picking a winner. That is what
this item is.

**Why you and not an agent.** `README.md` is on the implementation plane and
an agent could repair it freely. `.syzygy/intent/OVERVIEW.md` cannot be
touched: its current bytes are the prepared argument of the unperformed act
**4, `ADOPT PROJECT OVERVIEW`**, whose row lives in
[`contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md)
line 61. Editing one word of the page regenerates that argument and retires
any confirmation bound to it. So every repair that reaches the divergence
costs an act argument, and choosing which page moves is choosing what act 4
will offer.

**The arms.**

- **(a)** Make `OVERVIEW.md` match `README.md`: VIS-1 and VIS-2, cited by
  identifier, with the activity-is-not-proof sentence kept where it already
  appears in the surrounding prose rather than promoted to a rule. Costs act
  4's argument; an agent may prepare the delta, only you may perform it.
- **(b)** Leave `OVERVIEW.md` alone and repair `README.md` instead — drop the
  "two rules" framing there and route to `doctrine/vision.md` for the numbered
  set, so only one page ever claims to enumerate it. Free: `README.md` binds
  nothing. But it leaves the uncited pair standing on the page a newcomer is
  most likely to read first.
- **(c)** Rule that the two pages address different audiences and may frame
  doctrine differently, and record that as a deliberate exception to CC-REV-3
  so the next audit does not re-raise it.

**Recommendation: (a), folded into act 4 whenever you next take it up.** The
page that will become an accepted artifact is the one that should carry
identifiers, and "everything follows from these two" is a claim about doctrine
that only doctrine's own numbering can settle. There is no urgency: nothing is
gated on this, and (a) costs nothing extra if it rides along with an act you
have not yet performed. If act 4 is not coming soon, (b) is the honest interim
— it removes the conflicting enumeration without touching a prepared argument.

**Default if unanswered:** both pages keep their own pair, and a reader's idea
of the two founding rules depends on which door they came through.

---

## P-59 — The public overview still opens "Nothing is implemented"

**What is there.** `.syzygy/intent/OVERVIEW.md:125`, under the heading *What
exists today*, reads in bold: **"Nothing is implemented"** — "no daemon, no
UI, no store, no endpoints, no chosen language, framework, or database."

`PROJECT-STATUS.md` owns that row and answers differently. Capability 1 and
its local daemon are implemented and running, and the bounded Three-Surface
POC has been authorized since 2026-08-29 with a runnable implementation
(`PROJECT-STATUS.md:22` and its POC row). The language, framework and store
questions the sentence lists as unchosen were all answered by that
implementation.

**Why it matters.** This is the same failure shape the second pass repaired on
three other default-path pages and wrote into `AGENTS.md` as a lesson: a page
restating state it does not own goes quietly false the first time that state
moves. Here the page does the right thing two paragraphs later — it routes the
gate table to `PROJECT-STATUS.md` and says explicitly that it will not restate
it, *because* its bytes are frozen. The bolded sentence above that paragraph
is the one claim it did restate, and it is the one that went false.

It is also, of the three, the sentence most likely to be read: it is under
*What exists today*, in bold, on the page `AGENTS.md` routes to as the public
narrative, and a newcomer reaches it before any status page.

**Why you and not an agent.** Same reason as P-58: these bytes are the
prepared argument of the unperformed act **4, `ADOPT PROJECT OVERVIEW`** (row
61 of
[`contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md)).
An agent may not edit one word of it, and the house repair — marking staleness
at the stale sentence with the superseded text quoted and dated — is itself an
edit. The defect is therefore disclosed here and nowhere on the page.

**The arms.**

- **(a)** Replace the sentence in the act-4 argument with the same move the
  paragraph below it already makes: say that current capability is stated once,
  in `PROJECT-STATUS.md`, and route there. An agent may prepare the delta; only
  you may perform it. This is P-58's arm (a) applied to the same file, and the
  two would ride on one act.
- **(b)** Leave the page and record the divergence here, treating the overview
  as a fixed historical statement of intended shape written before any
  implementation existed. Free, but the false sentence stays on a default path.
- **(c)** Retire act 4 and route the public narrative elsewhere, so no page
  outside `PROJECT-STATUS.md` ever claims current capability.

**Recommendation: (a), folded into act 4 alongside P-58.** Both defects are on
the same page, both cost the same one act argument, and neither is urgent —
but they should move together, because a second edit to act 4's argument later
would retire whatever confirmation the first one earned.

**Default if unanswered:** the project's public overview goes on telling a
first-time reader that nothing is implemented, seven days after the daemon,
the endpoints and the POC that reads them all became real.

---

## P-66 — CC-SPEC's amendment history names five of nine phase rules, and its bytes are frozen

**What is there.**
[`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`](../contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md)
— the in-force CC-SPEC policy — carries an amendment-history banner at lines
28-35 recording the 2026-08-17
RD-69 blocker repair. It says CC-SPEC-8 "now cites
RFC1-33/RFC6-28/RFC7-38/RFC8-32/RFC9-52 for the judgment's home, gate, unit,
and effect." The normative clause it is summarizing names **nine** confirmed
contract phase rules at lines 245-248: those five plus **RFC2-26, RFC3-33,
RFC4-30 and RFC5-27** [Observed — swept 2026-09-06 by extracting every
`RFC<n>-<n>` identifier from each line range with Python `re`; banner 5,
clause 9 phase rules, the four listed above present only in the clause].

The banner does not say "only", and the operative clause is exhaustive and
unambiguous, so nothing about the reviewed-N/A judgment's home, gate, unit or
effect is actually in doubt. What the banner under-reports is its own history:
a reader reconstructing what the repair did learns that CC-SPEC-8 defers to
five modules when it defers to nine.

**Why you and not an agent.** The file's current bytes are bound. Its sha256
equals row 7 of
[`../contracts/candidates/general-trusted-bootstrap-authorization/TRANSACTION-MANIFEST.txt`](../contracts/candidates/general-trusted-bootstrap-authorization/TRANSACTION-MANIFEST.txt)
line 11 — the seventh subject of the indivisible amendment transaction the
owner performed 2026-09-01, recorded in
[`GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`](GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md)
row 5 [Observed — recomputed this session with `sha256sum` and compared
against the manifest row by `grep -F`; exact equality, not a prefix match].
So the banner is not merely uncorrected, it is frozen: editing one character
breaks a performed act's argument. This is the fourth uncorrectable banner on
this same page — path, filename and head banner all still say "candidate"
about a policy in force since 2026-08-17 — and the same shape as P-58/P-59,
except that here the act has already been performed rather than merely
prepared.

It was flagged as a non-blocking exception by the confirming reviewer at
[`../../../docs/reviews/R-GENERAL-TRUSTED-BOOTSTRAP-CONTRACT-CONFIRMATION-RAW.md`](../../../docs/reviews/R-GENERAL-TRUSTED-BOOTSTRAP-CONTRACT-CONFIRMATION-RAW.md),
which recorded that it "does not reopen authority or CC-REV-2 closure" and
called it a VIS-3 clarity blemish worth correcting in a future byte revision.
That review's verdict stands; this row exists because the correction it names
is an act, not an edit.

**The arms.**

- **(a)** Fold the banner correction into the next CC-SPEC amendment act
  whenever one is performed for some other reason. Costs nothing extra: the
  act already re-freezes the whole file, and the confirming review already
  reads these bytes.
- **(b)** Rule it a permanent, disclosed blemish — the operative clause is
  the authority, the banner is history, and history that under-counts is
  recorded rather than repaired — and let this register row be the disclosure
  so the next audit does not re-raise it.
- **(c)** Perform a standalone amendment act now whose only subject is the
  banner: a new confirming review on fresh bytes, a new manifest, a new
  ceremony.

**Recommendation: (b), with (a) riding along if a CC-SPEC amendment ever
comes.** Arm (c) spends a full review-and-act cycle to repair prose that binds
nothing, against a page whose three other banners are already permanently
wrong for the same reason; the honest move is to say so once, here. Nothing is
gated on this.

**Default if unanswered:** the banner keeps naming five of the nine, and a
reader of the amendment history under-counts the phase rules CC-SPEC-8 defers
to by four.

---

## What was repaired without asking

For contrast, so the boundary of this packet is legible. All of the following
were done in the two passes that produced this packet, on the implementation
plane or as pure disclosure repair, and none needed an act:

- The candidate contract package's front page claimed no owner act had ever
  been performed over any of it, and that the accepted home did not exist.
  Both had been false since 2026-08-17. Repaired, with the superseded
  paragraph kept and dated rather than deleted.
- `docs/` had no index at any level and cited no maintenance contract. It now
  has one, and it cites CC-REV-2/3/5/6/7 rather than restating them.
- The historical index listed five of eleven closed rounds. It now lists all
  eleven, and resolves the twelve filenames that occur in more than one round
  — three of which begin with `FINAL-` and are not final.

Added in the second pass, 2026-09-06:

- The candidate contract package's front page also *denied* the two craft
  policies that have been in force inside it since 2026-08-17
  (**CC-SPEC-1…11** and **CC-IMPACT-1…7**, at their committed home under
  `policy-candidates/`). The banner is corrected, the two files are named, and
  the consequences are disclosed — including that CC-IMPACT-7 mandates a blind
  run against a fixture a later review superseded, and that neither the clause
  nor the fixture may be edited. `check_governance.py`'s CG-4b carried the same
  expired premise and was fixed rather than worked around.
- The PWB implementation plan quoted figures from two mutation runs without
  naming the evidence files that produced them. Both are now cited by path and
  commit; every file in `docs/evidence/` is now cited by something.

  *Qualified, dated 2026-09-06:* that claim was true, but only under a sweep
  that matched filename **stems**. One of the two citations had been written
  across a line break — `…-2026-09-05.` ending one line and `json` opening
  the next — so a sweep matching whole filenames read that file as uncited.
  Both sweeps were correct and the citation existed throughout. The wrap is
  repaired, and the lesson is in `AGENTS.md`: these pages are hard-wrapped at
  78 columns, so a reflow that breaks inside a code span puts an unmeasured
  error term under every absence figure in the repository.
- The PWB live-review campaign recorded fifteen findings and no index of where
  each one is answered. `docs/reviews/2026-09-05-pwb-live-finding-traceability.md`
  now says, per finding, which record names it, which reviewer identifier the
  packet renumbered it from, and where its disposition lives.

  *Superseded, dated:* until later on 2026-09-06 the sentence above ended "and
  renders **Unknown** for the eight that nothing names, rather than inferring
  an outcome." That was a false absence, not a gap: the sweep behind it matched
  full identifiers only and missed the continuation forms this corpus writes
  them in (`PWB-LIVE-02, 03, 05 and 15`). Re-swept with an expansion-aware
  pattern over thirteen sources, **fifteen of fifteen are named**, each by
  exactly one repair child. The lesson is `AGENTS.md` verification rule 9's:
  an absence claim's denominator must cover the *forms* an identifier takes.

Added in the third and fourth passes, 2026-09-06:

- Eight prose files in three prepared act packages asserted their own
  inertness about transactions the owner had already performed. Each now
  opens with a dated **PERFORMED** note citing the act record by path; the
  pre-act banner stays beneath it, unedited, as the drafter's record. The
  seven bound files in those packages were left byte-identical, including one
  that will permanently read "Candidate — binds nothing" about a transaction
  performed 2026-09-01, because its own sibling manifest carries its digest.
- The eleven work rounds had four different file counts in circulation across
  four pages. `contracts/candidates/ROUND-ESTATE.md` now derives all four from
  one table and proves them mutually consistent, and the pages that quoted a
  figure point at it instead of copying one.
- `decisions/launch-gate/README.md` said "Empty today, correctly: no formal
  administration has been run" for nineteen days after Administration 1 landed
  in that directory with its generated report and validation transcript. It
  also stated a filename convention the one record never followed and did not
  say the JSON is canonical while the Markdown is generated. Marked at the
  stale sentences, dated; the superseded text is kept because a stored review
  quotes it verbatim as evidence of this project's epistemic discipline.
- All seven raw reports under `contracts/candidates/reviews/` read as uncited
  by any basename sweep, because their index titles its sections by short name
  ("rev10-boundary") and never by filename. That index may not be edited — an
  act package's impact ledger classifies it as raw-review evidence never
  rewritten to current semantics, and that ledger is bound — so the mapping
  from filename to verdict of record to disposition section was added to
  `contracts/candidates/README.md` instead.
- The count of unbannered round-file heads (96) was being read as a work
  estimate. Only **19** of the 96 are reachable by any act: 74 are raw
  reviewer output that CC-REV-6 protects regardless of authorization, two are
  digest-bound, and one is byte-compared by CI. Published on `ROUND-ESTATE.md`
  and corrected at the sentence in `HISTORICAL-INDEX.md`.

**No new question came out of the third and fourth passes.** Everything above
was either implementation-plane or pure disclosure repair.

Added in the fifth pass, 2026-09-06:

- Round 08d's two unpromoted process lessons were promoted into
  `PROCESS-LESSONS.md`; three independent audits confirmed rounds 08e, 08f,
  08j and 08k need none. The round estate's own uncited-file count had decayed
  from 84 to 82 within three commits of publication — falsified by prose from
  the pass that published it — and is now stated with its citer predicate,
  which moves the answer across 82 / 75 / 63 over the same 237 files. The
  96-unbannered-heads figure was published on a predicate ("four status words
  or similar") that reproduces as 118; the two missing literals were recovered
  by search and both pages now carry the exact six-literal set.
- One new question came out of this pass: **P-66**, above.

The register rows this packet owns are P-54 … P-59 and P-66, unanswered.
