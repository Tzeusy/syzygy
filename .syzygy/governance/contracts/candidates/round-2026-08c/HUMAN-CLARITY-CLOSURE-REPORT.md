# Human clarity for governed projects — closure report

> **Non-authoritative round record.** The raw review is
> `reviews/RD-2-human-clarity-RAW.md` and is never edited. Where this file and
> the raw review disagree about what the reviewer found, **the raw review
> wins**. Verdict words are copied, not summarised.

## The commission and the verdict

A reader with no project context was asked to do two things: answer six
questions about **this** repository as a fresh arrival, and then judge whether
the design in `HUMAN-ENTRY-POINT-BRIEF.md` and `PROJECT-SHAPE-FACETS-BRIEF.md`
would let them answer the same six for an **arbitrary governed project**.

**`VERDICT: REVISE`.**

## Part one — the repository's own front door

**Six of six answerable. The reviewer gave up on nothing.**

| Question | Answerable? | Hops |
|---|---|---|
| What is this project? | yes | 1 |
| What does it promise, and what does it refuse? | yes | 1 + 1 |
| What is missing or Unknown? | yes | 2–3 |
| Which artifact owns the answer? | yes (shape) / degraded (clause) | 1 / 5 |
| Where are the exact requirements? | yes (declared absent) | 1 |
| Does the root repository expose the entry point? | yes | 0 |

**The one degraded row is worth its own sentence.** "Which artifact owns the
answer" was answerable at the *shape* level in one hop and took **five** to
reach a governing clause. That is the governing standard's own task — *reach
the exact contract governing one task* — and five hops is the honest
measurement of where it stands.

## Part two — the verdict on the design, in the reviewer's words

> The **model** is right. Seven independent facets with no composite, Unknown
> as a first-class value with a reason, and a hard refusal of a badge is the
> correct design and I would not weaken any of it. What fails is the
> **routing evidence** offered for it.

Three material findings, each independently verified this session before
repair.

### R1 · The briefs minted three Unknown reasons the corpus's closed vocabulary does not carry — **closed**

**RFC2-24 — "Twelve reasons, closed."** Its own terms: *"no implementation may
mint, spell, or force-fit a secondary value the list does not carry"*, and
*"A condition genuinely not among the twelve is disclosed as a **fact of the
render** — named, expandable, routed to its resolving action — never dressed as
a reason."*

The briefs emitted four reasons. **Three were not in the twelve:**
`governing-contract-unaccepted`, `no-evaluation-performed`,
`no-declared-intent-in-scope`.

This is the sharpest kind of finding available against these documents, because
the routing's whole claim is to be *"a projection of the corpus rather than an
addition to it"* — and at its **first contact with a closed corpus vocabulary
it minted three values**.

**Repaired at the source, each mapped rather than renamed:**

| Was | Now | Why |
|---|---|---|
| `no-evaluation-performed` | **#2 `missing-evidence`** | RFC7-30's own outcome in its own words: *"absent its record, the test renders Unknown, never met"* |
| `no-declared-intent-in-scope` | **#1 `missing-declaration`** | Reason #1 is *"No governing declaration … exists"* |
| `governing-contract-unaccepted` | **#1 `missing-declaration`**, with the candidate-contract status as a **fact of the render** beside it | It is a condition of *Syzygy's own corpus*, not of the governed project — exactly the case RFC2-24 says to name and route rather than dress as a reason |

**Swept this session**, per verification rule 2: every `reason:`-adjacent token
in all three round documents enumerated against the twelve by Python `re`.
**Zero non-vocabulary reasons remain**, across three files.

**RD-2's second-order consequence, which is the one that matters:** had those
three reasons stood, **RFC6-14 would have become unsatisfiable** — it requires
the Unknown reason *verbatim from the RFC 0002 vocabulary*, and a minted reason
cannot be carried verbatim from a vocabulary that does not contain it.

### R2 · The "real contract gap" for Human-understandable was not real — **closed**

The routing said: *"A contract gap, and it is real. No clause defines a
fresh-reader evaluation as an evidence-producing act."*

**False, and verified false this session.** `RFC-0007/rendering-and-surface.md`
defines it in three clauses:

- **RFC7-30** — the cold-open comprehension walkthrough, its six prompts, its
  independence standard (VIS-3), and at least one non-visual/keyboard-only run
  per release milestone.
- **RFC7-31** — verdict discipline, **two record homes** (execution record in
  `governance/records/`, judgment in `governance/decisions/`), **two
  release-blocking floors**, and the `verdict-unlawful` failure mode.
- **RFC7-32** — cadence: material narrative changes and release milestones.

RD-2 named the cause exactly: **RFC-0007 module 2 went unread.** That is worse
than missing a clause — it is a claim of absence with no sweep behind it, and
VIS-2's rule about absence applies to a reviewer's own claims first.

**The gap is now narrowed to what is genuinely missing:** at what **tier** an
RFC7-31 verdict is admitted into RFC2-25's registry, and **when a verdict
expires** — RFC7-32 gives a cadence for running the test, not a currency bound
for its result.

**One thing this finding also fixed for free:** RFC7-31's two floors give
Human-understandable a **constructible `false`**, closing RD-2's C-1.

### R3 · A quotation attributed to RFC3-4 does not exist — **closed**

The routing quoted RFC3-4 as saying *"a missing or invalid `project.yaml`
renders every dependent claim Unknown"*.

**Verified: that sentence exists nowhere in the repository.** The real sentence
is **RFC3-9's**, reads **"An unparseable or invalid `project.yaml`"**, and says
nothing about the *missing* case — which RFC3-9 routes to first-pass drafting.

A wrong clause number, a changed word, and a case the clause does not cover —
in a routing table whose entire purpose is to show that each facet's inputs are
real clauses. **It is the same class as review RD-4's finding F-1** — evidence
read from the *neighbourhood* of a clause rather than from the clause — showing
up in a different document in the same round. Two independent reviewers found
the same failure mode in the same week, which makes it a pattern rather than a
slip.

**Corrected, and the correction is recorded in place rather than quietly
applied.**

### The number that survived two cancelling errors

The routing's headline — *"Six of seven facets need no new clause"* — was
reached by **overstating** Human-understandable's gap (R2) while
**understating** three others to `—` (R1). The errors cancelled.

The corrected reading is still six of seven. **That is a coincidence, and the
document now says so:** *a number that survives two cancelling errors is not
evidence.* The claim rests on the per-row citations, each spot-checkable, not
on the total.

## The design findings, and what changed

| # | Finding | Disposition |
|---|---|---|
| **A-3 / E-2** | **The discoverability finding was singular, so N−1 of a project's N repositories had no entry point *and no rendered gap saying so*** | **Closed.** The finding is now **per declared repository entry** (RFC3-6). RFC3-29 allows one plane per repository; RFC3-30 makes every other repository read-only. The cost is now listed in §6, where RD-2 correctly noted it was absent and *"larger than all three"* costs that were listed |
| **E-2 (placement)** | Discoverability belongs to Human-understandable, not Registered — *"a project renders `Registered: true` with `discoverable: no` buried in a drawer, while the facet a newcomer would actually consult about human comprehension is silent on whether a human can reach the door at all"* | **Recommended, not applied.** RD-2's argument is the stronger one and is quoted in full in the brief. Which facet owns a finding is a design decision inside **packet 6** |
| **B-5** | The two briefs disagreed about Registered's value domain — `Contradiction` in one, absent from the other | **Closed.** The brief now states the four-valued domain and cites RFC3-4's two-roots case |
| **B-2** | Two facets can silently disagree through asymmetric scoping | **Closed** by new **rule 9**: every facet declares its own scope in its own answer. Disagreement between differently-scoped facets is two answers to two questions, and only visible scope makes that legible |
| **C-1, C-2** | Human-understandable and Traceable could not be `false` | **Closed** by new **rule 10**: a facet that cannot be `false` is not a facet, with the constructible `false` written down for both — RFC7-31's floors, and a *declared* link that does not resolve |
| **G-2, G-3** | The worked example emitted two counts, in the example illustrating the rule against counts | **Closed.** Both removed; per-class lines carry the information |
| **G-5** | The example does not distinguish *"Unknown because this project is thin"* from *"Unknown because Syzygy cannot answer this for anyone"* — Mission-ready *"is a constant, not a measurement"* | **Closed.** Staged facets are marked `STAGED` in the example itself, and RD-2's reading is quoted so the misreading it warns about is visible next to the example that produces it |
| **G-4** | The same epistemic situation yields `false` in one facet and `Unknown` in another with no stated principle | **Closed.** The principle is stated: whether the negative was **observed** or merely **unobservable** |
| **F-3** | *"Machine-queryable"* is not *"attached"* — an agent querying Registered gets `true` and nothing else | **Closed as a requirement, open as a home.** The non-certification sentence is now specified as a **required field on the Registered facet's answer**, in the same envelope as the value. **[Unknown]** which clause makes it required — RFC6-14 governs labels, not envelope fields — so it routes to **OpenSpec Capability 1** rather than being smuggled into RFC-0006 |
| **D-11** | Three cited sibling documents did not exist | **Two now exist**, written later in this same session: `FIRST-OPENSPEC-SEQUENCE.md` and `OWNER-DECISION-PACKETS.md`. **`FINAL-CONTEXT-SELECTION-REPORT.md` is still outstanding** and is named here rather than left dangling. RD-2 was reading a round mid-flight and its objection was correct at the moment it was made |
| **A-4** | RFC7-3's deletion invariant vs an entry point living in `.syzygy/intent/**` | **Open.** RFC7-31 shows the pattern — records that must survive deletion of `intent/` live elsewhere. The entry point is presentation and cites nothing, so **[Inferred]** the invariant is not violated; **[Unknown]** whether anything *derived from* the entry point could be. Recorded |
| **B-4, B-6** | Facets share inputs, so independence is weaker than a reader will read it as; intra-facet rollup is permitted while inter-facet rollup is forbidden, with no stated principle distinguishing them | **Open, and this is the sharpest unrepaired finding.** The distinguishing principle is not written down, and writing one is a design decision rather than a repair. Routed to **packet 6** |
| **D-4, D-6** | Two routing citations are real clauses that the routing overstates | **Open.** Recorded; neither changes a facet's inputs |
| **A-2, D-1, D-5, D-7, D-8, D-9, D-12** | Spot-checks that hold | Recorded. RD-2 verified **seven** citation groups as sound |
| **Q2 coverage gap** | *"The refusal half is unbacked"* — nothing requires a non-goal to be reachable, while RFC7-30 makes reaching a non-goal's rule text a load-bearing prompt | **Open, routed to OpenSpec Capability 1 and 3.** A real gap between what the entry point promises and what any clause requires |

## What this closes and what it does not

**Closed:** three material defects, all in documents this round authored — a
minted vocabulary, a fabricated gap, and a fabricated quotation — plus seven
design findings repaired at the source, two new rules, and a worked example
that no longer emits the thing its own rules forbid.

**Not closed:**

- **The rollup principle (B-4/B-6).** Why aggregation within a facet is honest
  and aggregation across facets is not has no stated principle. **Packet 6.**
- **Discoverability's facet home (E-2).** Recommended, deferred to the owner.
- **The non-certification field's contract home (F-3).**
- **The non-goal reachability gap (Q2).**
- **RFC7-3's deletion invariant over the entry point (A-4).**

**The model is not in question.** RD-2 tried to break it — constructing two
facets that must disagree, a facet unanswerable without another's answer, and
an unfalsifiable facet — and every construction produced a repairable defect in
the *evidence*, not in the seven-facet decision. **No finding argues for a
composite badge, fewer facets, or a rolled-up score.**

**Reviewer independence, stated plainly:** RD-2 is not a confirming review of
these repairs. The repairs were made after it returned, in the same session
that authored the defects. **A repair pass and the review of that pass cannot
be the same pass** — so the corrected facet documents have been read by no
independent reviewer, and that is recorded rather than papered over.
