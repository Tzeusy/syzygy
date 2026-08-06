# RD-2 — Registered-project human-clarity review

**Commissioned:** 2026-08-06, fresh reader, no authoring context.

# VERDICT
VERDICT: REVISE

---

## How to read this file

Two parts. **Part 1** is my measurement as a fresh reader of *this* repository:
six questions, what I read, how many hops. **Part 2** judges the design the
three briefs propose for making those questions answerable in an arbitrary
governed project, against criteria A–G.

I did not read commit messages and did not open any file under
`round-2026-08c/reviews/`. I found the briefs only because the commission gave
me their paths — see finding **E-3**.

Method notes: all clause-text checks were done with Python `re` over the file
tree, not with `grep`, per the repository's own ugrep warning. Clause quotes
are from `.syzygy/governance/contracts/candidates/rfcs/**` at the working-tree
state of 2026-08-07.

---

# PART 1 — The six questions, as the reader I actually was

**Reading path, in order:** `README.md` → (`PROJECT-STATUS.md`,
`CONTRIBUTING.md` together) → `.syzygy/intent/OVERVIEW.md` →
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. Four hops of
default-path reading. Everything below is on that path unless noted.

**I could answer all six.** That is a genuinely good result and I want to say
it before the criticism starts: this repository is the best-signposted
governance corpus I have read. The failure modes below are in the *generalized*
design, not in this repo's front door.

## Q1 — What is this project?

**Answerable in 1 hop. [Observed]**

`README.md:3-5` gives the thesis in three lines: *"A specification-driven
control plane for software projects: humans define what should be true,
evidence shows what is true, and agent fleets do bounded work to close the
difference — with the difference always rendered honestly."*
`README.md:14-15` adds the intended shape (*"a local-first daemon with a
browser app"*). `.syzygy/intent/OVERVIEW.md:16-19` restates it at the same
altitude. The two agree; I did not have to choose.

## Q2 — What does it promise, and what does it refuse?

**Answerable in 1 hop for the promise, 1 hop for the refusal. [Observed]**

Promise: `README.md:36-38` names the two rules (VIS-1 comprehensible truth,
VIS-2 no evidence means Unknown). Refusal is unusually well served —
`README.md:114-120` is titled "What is not implemented" and begins
*"Everything."*, and `CONTRIBUTING.md:12-18` states the no-implementation
boundary as a binding rule.

**Friction worth recording:** the promise/refusal split is *implicit*. Nothing
labels a section "what this refuses to be". I assembled it from three places
(README's non-implementation section, CONTRIBUTING's boundary, OVERVIEW's
"north star, honestly labelled" at `OVERVIEW.md:102-111`). A fresh reader with
less patience would get the promise and miss the refusal. This matters for
Part 2 because RFC7-30 makes "naming at least one non-goal **and reaching its
rule text**" a load-bearing prompt of the corpus's own comprehension test, and
I could not reach a non-goal's rule text from the front door in one hop.

## Q3 — What is missing or Unknown?

**Answerable in 2 hops. [Observed]**

`README.md:101` → `PROJECT-STATUS.md`, whose gate table (lines 18-31) carries
five ⏳ and two ⛔ rows, and whose "Known blocking defects" section (lines
55-82) is the most honest paragraph in the repository — it names a residual
("no confirming review is bound to the bytes now offered", `PROJECT-STATUS.md:66-74`)
rather than hiding it. `PENDING-OWNER-DECISIONS.md` is the third hop for the
full queue (P-1…P-27).

This is the question the repository answers best.

## Q4 — Which artifact owns the answer?

**Answerable in 1 hop for the *shape* of the answer; 3–5 hops to actually
settle a specific claim. [Observed]**

`README.md:73-88` gives the typed-authority table with a Status column; the
same table appears in `AGENTS.md` and again as OVERVIEW's Drawer 2
(`OVERVIEW.md:213-249`), which maps every claim on that page to an owning
authority and marks each Adopted / Recorded / Candidate. Drawer 2 is the single
best artifact I read for this question.

**Where it degraded:** settling a claim at *clause* level took me five hops and
one dead end. Nothing on the default path tells a reader that clause files live
under `contracts/candidates/rfcs/` in per-RFC directories with 2–4 modules each
(`RFC-0002/snapshot-and-evaluation-core.md`, etc.); I found the layout with
`ls -R`. `AGENTS.md` says *"`contracts/rfcs/` exists only after act 1"*, which
reads as "there are no RFC files yet" until you notice the `candidates/` prefix
does the work. **[Inferred]** A reader who trusted AGENTS.md's phrasing would
conclude the clause text does not exist.

## Q5 — Where are the exact requirements?

**Answerable in 1 hop, and the answer is "nowhere yet". [Observed]**

`README.md:84`: *"Required observable behavior | `openspec/` | Does not exist
yet"*. Confirmed: `ls openspec` → no such file or directory.
`PROJECT-STATUS.md:30` gates it (gate 11, ⛔, blocked on gate 4).

This is the cleanest of the six, precisely because the answer is a declared
absence rather than a location.

## Q6 — Does the root repository expose the entry point?

**Answerable in 0 hops. `yes`. [Observed]**

`README.md:97-98` is item 1 under "## Start here":
*"[`.syzygy/intent/OVERVIEW.md`](.syzygy/intent/OVERVIEW.md) — the project
argument, 30 seconds to full depth (draft; adoption pending)."*

By the entry-point brief's own tri-state (`HUMAN-ENTRY-POINT-BRIEF.md:96-97`)
this repository renders `yes`. Note that this is the *only* repository that can
currently render `yes`, and it does so because a human wrote that line, not
because any mechanism produced it.

## Part 1 scoreboard

| Q | Answerable? | Hops | Where it came from |
|---|---|---|---|
| 1 What is this | yes | 1 | `README.md:3-5,14-15` |
| 2 Promise / refusal | yes | 1 + 1 | `README.md:36-38`; `README.md:114-120`, `CONTRIBUTING.md:12-18` |
| 3 Missing / Unknown | yes | 2–3 | `PROJECT-STATUS.md:18-82`; `PENDING-OWNER-DECISIONS.md` |
| 4 Who owns the answer | yes (shape) / degraded (clause) | 1 / 5 | `README.md:73-88`; `OVERVIEW.md:213-249` |
| 5 Exact requirements | yes (declared absent) | 1 | `README.md:84` |
| 6 Entry point exposed | yes | 0 | `README.md:97-98` |

**Six of six.** I gave up on nothing.

---

# PART 2 — Judging the design

## Summary of the verdict

The **model** is right. Seven independent facets with no composite, Unknown as
a first-class value with a reason, and a hard refusal of a badge is the correct
design and I would not weaken any of it. What fails is the **routing evidence**
offered for it, and it fails on three material, checkable points:

- **R1 — the Unknown-reason vocabulary is violated.** Three of the four Unknown
  reasons the brief uses do not exist in RFC2-24's closed twelve, which the
  brief's own rule 3 says it draws from. This alone falsifies the routing's
  headline result.
- **R2 — the "real contract gap" for Human-understandable is not real.**
  RFC7-30/31/32 already define the fresh-reader evaluation as an
  evidence-producing act, in detail, with two homes and a record. No brief
  cites them. RFC-0007 module 2 appears to have gone unread.
- **R3 — a quotation attributed to RFC3-4 does not exist anywhere in the
  repository**, and the nearest real sentence (RFC3-9) says something the facet
  model must treat as different.

Each is a one-pass repair. None indicts the seven-facet decision. Hence
REVISE, not REJECT.

---

## A. Is the fixed entry point the right choice?

**Largely yes, with one unlisted cost that I think is the biggest hole in the
brief.**

### A-1. The reasoning against a co-located `README.md` is sound. [Observed]

`HUMAN-ENTRY-POINT-BRIEF.md:21-23`: *"Two default entry points is the same
defect as none: a reader who finds one cannot know whether the other disagrees,
and an author with two homes uses whichever is nearer."* That is correct and it
is the same argument the corpus makes everywhere else (one owning home per
fact). The third bullet — a `README.md` in a directory reads as a directory
index — is a real convention argument, not a rationalization. §1's closing
paragraph (`:40-44`) pre-settles the question before someone answers it by
adding a file, which is good practice.

### A-2. A project with a strong root README: handled, but only by luck of scope. [Inferred]

The brief's answer is that the root README is *outside* the write boundary, so
Syzygy renders a `yes/no/Unknown` finding and proposes a one-line link
(`:91-115`). For a project with a strong root README this is actually the best
case: the owner applies a one-line addition and the strong README stays the
front door for humans while `OVERVIEW.md` is the front door for Syzygy. Nothing
breaks.

What the brief does not say is that this produces **two narratives**, which is
the exact defect §1 rejected — the strong root README and `OVERVIEW.md` will
disagree, and the brief's own reasoning ("a reader who finds one cannot know
whether the other disagrees") applies with full force. The corpus has an answer
the brief does not reach for: **RFC7-6** binds *"A governed project has at most
one **primary narrative**"* (`rfcs/RFC-0007/narrative-contract.md:147-150`),
and *"Additional named narratives are permitted under the same class and rules;
none outranks another"*. A root README is not under Syzygy's write boundary and
so cannot be a governed narrative at all — meaning RFC7-6's cardinality rule
does not reach it, and the two-narrative problem is real and unaddressed.
**Recommendation:** say in §6 that the discoverability link is a *pointer*
obligation, not a content one, and that the root README's content is
out-of-model by construction.

### A-3. **Many repositories: this is the unlisted cost, and it is severe.** [Observed]

RFC3-29 (`rfcs/RFC-0003/manifests-and-namespace.md:415-418`): *"One plane per
repository; one root per Project — upheld. A repository carries at most one
`.syzygy/` plane, at its root (RFC3-4). There are no directory-scoped
sub-roots."* RFC3-30 (`:420-429`): an observing project *"reads the observed
repository's entire tree — including its `.syzygy/**` and `openspec/**` plane —
read-only: A's direct-write universe is A's own governance root's two
namespaces and nothing else (VIS-5); A never writes, migrates, or 'repairs'
B's plane."*

So for a project with N repositories, **exactly one has an entry point, and
Syzygy may not create one in the other N−1** — not the file, not a stub, not a
pointer. A competent engineer who opens observed-source repository #4 has no
path in and no *rendered gap* either, because the discoverability finding as
drafted (`HUMAN-ENTRY-POINT-BRIEF.md:92-97`) is singular: *"repository front
door links to the Syzygy project entry"*. One README, one answer.

`HUMAN-ENTRY-POINT-BRIEF.md:139-151` is titled "What this costs, honestly" and
lists three costs. This is not among them, and it is larger than all three.
The problem the brief opens with — *"a competent engineer who opens its
repository can have **no idea any of that exists**"* (`:11-13`) — is
**unsolved for every repository but one**, and the design as written cannot
even render that it is unsolved.

**What I would do:** make the discoverability finding **per declared repository
entry** (RFC3-6 already gives you the entry to hang it on, and the brief
already routes it there at `:162`), yielding one `yes/no/Unknown` per
repository. That costs nothing, uses a clause that exists, and converts a
silent hole into a rendered one — which is the whole thesis.

### A-4. A tension with RFC7-3's deletion invariant, which the corpus already solved once. [Observed]

RFC7-3 (`rfcs/RFC-0007/narrative-contract.md:103-105`): *"Deleting everything
under `.syzygy/intent/**` changes **no truth, status, work, consent, or
normative fact**."* The brief makes a file under `.syzygy/intent/` the required
entry point whose absence a facet answer depends on. RFC7-31 hit this exact
problem and solved it (`rfcs/RFC-0007/rendering-and-surface.md:170-174`):
*"Storing either under `.syzygy/intent/**` would let deletion of that tree flip
a v1.md-tracked success test from a recorded verdict to Unknown — exactly what
RFC7-3's deletion invariant forbids."* — which is why walkthrough records go to
`.syzygy/governance/records/` and judgments to `.syzygy/governance/decisions/`.

The brief needs one sentence saying that the *entry point artifact* lives in
`intent/` while any *facet answer about it* is computed from records outside
`intent/`, so deletion of `intent/` degrades presentation and not status. It is
a small repair, but leaving it out reproduces a defect the corpus has already
paid for.

---

## B. Are the seven facets independent, or does one secretly compute another?

**They do not compute one another. But "independent" is claimed more strongly
than the model supports, and I can construct both requested cases.**

### B-1. The precondition claim survives a first reading. [Observed]

`PROJECT-SHAPE-FACETS-BRIEF.md:88-92`: *"Several are precondition-related — an
unregistered project cannot be Observable — and the relationship is rendered as
an Unknown reason, never as a propagated value."* I could not find a place
where a facet's *value* is derived from another facet's *value*. That part
holds.

### B-2. **Construction: two facets that must disagree, via asymmetric scoping.** [Inferred]

Reconciled is explicitly scope-selected — *"For a **selected scope** — never
for a project as a whole"* (`:81`). Observable is not: *"the declared
repositories and the evidence sources the other facets depend on"* (`:63-64`),
i.e. project-wide.

Take a project declaring repositories A and B. B's token expires. A is
readable, and the declared intent scope selected for reconciliation lives
entirely in A.

- **Observable = `false`** (or `Unknown`), because "2 of 2 repositories
  readable" is now "1 of 2".
- **Reconciled = `true`**, lawfully, because RFC2-21's predicate
  (`rfcs/RFC-0002/reconciliation-chain.md:225-233`) is evaluated *"Over a
  declared scope at E"* and every element of that scope is in A.

A reader sees `Observable: false` beside `Reconciled: true` and has no way to
know the two answers are about different scopes, because only one of them
declares its scope. This is not a rollup bug; it is a **missing scope
parameter on Observable**, and it is exactly the failure RFC6-16 exists to
prevent: *"an answer names what was filtered and never presents a filtered or
partial result as full scope"*
(`rfcs/RFC-0006-cross-surface-selection-query-drawer.md:225-228`). The routing
cites RFC6-16 at `PROJECT-SHAPE-FACETS-ROUTING.md:166` and then does not apply
it to the one facet that needs it.

**Fix:** state that every facet declares its scope, and that Observable's
default scope is the full declared repository set.

### B-3. **Construction: a facet unanswerable without another's answer.** [Inferred]

Human-understandable's mechanical half requires *"its source anchors resolve"*
(`:55`), routed to RFC7-10/11 (`ROUTING.md:67`). Anchors resolve into owned
artifacts, which requires reading them — Observable's subject exactly. So
Human-understandable's mechanical half is not computable without Observable's
inputs.

The brief's escape is that this renders as an Unknown *reason*. But the brief
then **fixes** Human-understandable's Unknown reason to a single value
regardless of cause: *"Until there is a declared process that produces one, it
is `Unknown — reason: no-evaluation-performed`"* (`:140-142`). A project whose
anchors are unreadable and a project that has simply never been read by a fresh
reader get the identical answer. That is rule 5's own violation
(*"A missing declaration and failed evidence are different answers"*, `:110`)
committed inside the facet that states it. And the staging premise is false
anyway — see **R2 / D-2**.

### B-4. Shared inputs mean the independence is weaker than a reader will read it as. [Inferred]

RFC3-6 (`rfcs/RFC-0003/manifests-and-namespace.md:178-183`) makes an
unresolved consent reference render as *"not observed"* — the same fact feeds
Registered (as a consent record) and Observable (as readability). Two facets
that can never disagree about consent are not independent measurements in the
sense a reader takes from "seven independent answers"; they are two projections
of a partly-shared input set. The brief should say "computed separately from
shared inputs", not leave "independent" to carry the epistemic weight.

### B-5. **The briefs disagree with each other about a facet's value domain.** [Observed]

`ROUTING.md:37-42`: *"Registered must therefore be able to answer
`Contradiction`, not only true/false/Unknown — which the corpus already
supports, and which a boolean facet would have lost."*

`PROJECT-SHAPE-FACETS-BRIEF.md` never mentions `Contradiction`. Its rules
(`:99-101`) name only *"Unknown is a first-class value with a reason. Not
`false`, not `0`"*, and its worked example uses only `true` / `false` /
`Unknown`. Two candidate documents in the same round state different value
domains for the same facet. Per `CONTRIBUTING.md:88-93` this is a contradiction
to surface, not to reconcile: I report both readings. **The routing is the one
that matches the corpus** (RFC3-4 routes the two-roots case to contradiction
machinery, `rfcs/RFC-0003/manifests-and-namespace.md:156-160`), so the brief is
the document that should change.

### B-6. Intra-facet rollup is permitted; inter-facet rollup is forbidden; no principle distinguishes them. [Inferred]

Rule 4 (`:103-106`) forbids *"no count-of-facets-passing, no '5 of 7'"* because
*"A count is a composite wearing a different hat"*. But **Shape present** emits
a single `false` computed by AND over six Genome classes, and **Traceable** is
defined as *"coverage of the declared links"* (`:70-71`) — a fraction. Both are
composites inside a facet, by rule 4's own definition.

The routing half-notices: *"It must report **per class**, never as a count.
'4 of 6 Genome classes present' is a composite inside a facet"*
(`ROUTING.md:57-60`). It does not then explain what the facet's *single value*
is, or why AND-ing six heterogeneous classes into one `false` is honest when
counting seven heterogeneous facets is not. There is a defensible answer
(within a facet the classes answer one question; across facets they answer
seven), but the brief does not give it, and without it rule 4 reads as
arbitrary. **A reader looking for a loophole will find this one.**

---

## C. Is any facet unfalsifiable?

**Two of the seven have no constructible `false` state under the brief as
written.** For each facet I tried to build the project that makes it false.

| Facet | Project state that makes it `false` | Falsifiable as written? |
|---|---|---|
| Registered | No `project.yaml`; or a field outside RFC3-5's closed set; or an owner field absent | **Yes** |
| Shape present | The worked example: doctrine, behavioural requirements, topology, handcrafted-region declaration all absent | **Yes** |
| Human-understandable | *see C-1* | **No** |
| Observable | Declared repository unreadable at E (token expired, repo renamed) | **Yes** |
| Traceable | *see C-2* | **No** |
| Mission-ready | An envelope permitting an effect class that is not classified reversible/compensatable/irreversible — RFC10-19: *"An effect class not so classified is not authorized"* (`rfcs/RFC-0010-mission-control-autonomy.md:529-534`) | **Yes** (once unstaged) |
| Reconciled | RFC2-21's predicate fails with a merged change evaluated `unsatisfied` | **Yes** at V1; at V0 the routing correctly says only `merged` / `reconciliation-pending` / `Unknown` render (RFC8-29, `rfcs/RFC-0008/accounting-reconciliation-and-release.md:236-240`) |

### C-1. Human-understandable cannot be `false`. [Inferred]

Every failure route in the brief lands on Unknown:

- No narrative → RFC7-6 says a narrative may be thin *"but never absent"*
  (`narrative-contract.md:152-157`); the brief's own answer for a project with
  no narrative is `Unknown — no-evaluation-performed` (worked example,
  `BRIEF.md:181-182`).
- Broken anchors → RFC7-11 is titled *"Broken anchors render Unknown, never
  silent"* (`narrative-contract.md:225`). Unknown.
- No fresh-reader judgment → `Unknown — no-evaluation-performed` (`:140-142`).

Value domain `{true, Unknown}`. **The corpus has the missing `false`** and the
brief did not use it: RFC7-31 (`rendering-and-surface.md:148-156`) names two
floors that *"are not judgment calls"* — *"a **dangling internal link on the
walkthrough path** fails (trust floor, release-blocking); a confident wrong
answer **attributable to what the surface rendered** fails."* Those are the
`false` states. Import them.

### C-2. Traceable cannot be `false` either. [Inferred]

RFC8-22 (`accounting-reconciliation-and-release.md:92-97`): *"A broken join
renders; it is never silently skipped. Where a link cannot be established at
the answering evaluation, the chain renders the break at that link — **Unknown
with its RFC2-24 reason**."* So a broken declared link is Unknown, not false.
An absent declared link is, per the brief, *"`Unknown — missing-declaration`"*
(`ROUTING.md:108-111`). Both failure modes are Unknown. There is no path to
`false`.

That is not fatal — a facet whose honest domain is `{true, Unknown}` is
defensible — but the brief presents seven facets as if they share a domain, and
`Traceable: Unknown` will be read by a newcomer as "not measured" when it
actually means "measured, and the links are broken". **Either give Traceable a
`false` for the declared-but-broken case, or say explicitly that Traceable is a
two-valued facet and why.**

---

## D. Does the routing hold?

I spot-checked **eleven** citations against clause text, not four. Most hold.
Three do not, and two of the three are load-bearing for the routing's headline
claim.

### D-1. ✅ Facet 1 inputs (RFC3-4/5/6/7/8) — hold.

RFC3-4 *"Location is designation"* (`manifests-and-namespace.md:152-160`);
RFC3-5's closed field table (`:162-176`) contains `owner`, `repositories[]`,
`consents[]` exactly as the routing's compute rule needs; RFC3-6 repository
entries (`:178-183`); RFC3-7 consent records as governance acts (`:185-208`);
RFC3-8 revocation (`:210-222`). The routing's compute sentence
(`ROUTING.md:32`) is a faithful conjunction of these. **Supported.**

### D-2. ❌ Facet 3's "contract gap, and it is real" — **not supported; the gap is largely already filled.**

`ROUTING.md:69`: *"**A contract gap, and it is real.** No clause defines a
*fresh-reader evaluation* as an evidence-producing act. RFC7-13 states the
progressive-disclosure obligation; nothing states who tests it, at what tier
the result is admitted, or when it expires"*.

Three of those four assertions are false against the corpus:

- **A clause defines the fresh-reader evaluation.** RFC7-30
  (`rendering-and-surface.md:128-140`): *"This surface's acceptance test is the
  **cold-open comprehension walkthrough**: a fresh reader (human or agent, no
  authoring context — VIS-3's independence standard), entering at the primary
  narrative (RFC7-6) with navigation confined to Polaris, states in their own
  words: why the project exists; what it promises; what it refuses to be
  (naming at least one non-goal and reaching its rule text); what its major
  capabilities are and how they fit; **where exactness lives** — reaching a
  verbatim requirement leaf; and **one thing the project does not currently
  know about itself**…"*
- **A clause states who tests it and where the result lives.** RFC7-31
  (`:148-176`): the verdict is *"the owner's recorded human judgment — never
  rendered Observed, never a score"*, and *"**Two artifacts, two homes.** Each
  run mints a **walkthrough execution record** — `kernel-recorded`, in
  `.syzygy/governance/records/` (RFC3-15) … absent its record, the test renders
  Unknown, never met."* That sentence **is** "a fresh-reader evaluation as an
  evidence-producing act", stated verbatim.
- **A clause states when it runs.** RFC7-32 (`:179-184`): *"At **material
  narrative changes and release milestones** — not every prose edit"*.

Only **expiry** and **which RFC2-25 tier admits the judgment** are genuinely
open — a much narrower gap than the routing describes, and the routing's chosen
home (RFC2-25's tier registry, "at surface specification") is right for the
*tier* half and wrong for the rest, which already has a home.

**Mechanical confirmation of the blind spot:** none of the three briefs
contains the string `RFC7-30`, `RFC7-31`, `RFC7-32`, or
`.syzygy/governance/records`. RFC-0007 module 2
(`rendering-and-surface.md`) does not appear to have been read. This also means
`HUMAN-ENTRY-POINT-BRIEF.md`'s eight-question list (`:51-58`) was authored
without reference to RFC7-30's six prompts, and the two lists differ — the
brief has no "reaching a non-goal's rule text" and no "reaching a verbatim
requirement leaf"; RFC7-30 has no "where does work live" and no "how do I ask
programmatically". **Two comprehension criteria now exist for one project.**
That is the two-entry-points defect the brief itself opens by rejecting,
committed one level up.

Relatedly, `HUMAN-ENTRY-POINT-BRIEF.md:161` routes the fixed-path gap to RFC7-6
without noticing that RFC-0007 module 1 §7 already binds *"the primary
narrative RFC7-6 requires is RFC7-30's entry point"*
(`narrative-contract.md:566-567`). RFC7-6 may still be the right home for the
*path*; the routing table should say why it is not RFC7-30.

### D-3. ❌ Facet 1's Unknown-reason quotation — **the quoted sentence does not exist.**

`ROUTING.md:33`: *"RFC3-4's own rule already supplies the sharpest one:
*"a missing or invalid `project.yaml` renders every dependent claim Unknown"* —
the contract says the fail-closed direction outright"*.

A Python `re` sweep for `missing or invalid` across `.syzygy/**` returns
**exactly one hit: `ROUTING.md:33` itself.** The sentence is not in RFC3-4
(`manifests-and-namespace.md:152-160`, which says nothing about Unknown) and
not in the corpus.

The nearest real sentence is **RFC3-9**, not RFC3-4
(`manifests-and-namespace.md:227-229`): *"An **unparseable** or invalid
`project.yaml` renders every dependent claim Unknown; Syzygy never auto-repairs
it — a repair is a Proposal (RFC1-27) through the owner gate."*

Two defects, and the second is worse than the misattribution: **"missing" is not
"unparseable".** RFC3-9's first sentence handles the missing case by a different
route entirely — *"On a newly governed or undeclared project, Syzygy may draft
declaration content … drafted values render unadopted and bind nothing"*
(`:224-227`). A missing declaration is a drafting route; an unparseable one is a
fail-closed Unknown. Swapping the words collapses precisely the
missing-declaration-versus-failed-evidence distinction that is rule 5 of the
brief and that `HUMAN-ENTRY-POINT-BRIEF.md:99-103` calls *"exactly the
missing-declaration-versus-failed-evidence rule the facet model turns on"*.

A document whose sole purpose is citation fidelity must not carry a fabricated
quotation. This finding by itself would justify REVISE.

### D-4. ⚠️ Facet 2 (RFC1-8) — supported, but the routing overstates what the clause is.

RFC1-8 (`RFC-0001-project-graph-identity-state-planes.md:211-213`) does say:
*"**Genome** is a membership predicate answered by the governance plane's
declared inventory, not an entity."* **Supported.** The clause is titled
"Frozen-noun mapping" and Genome is one line of it, so "RFC1-8 rules Genome a
membership predicate" is accurate but reads as though the clause is about
Genome. Cosmetic.

The six universally-required classes also check out against adopted doctrine
(`doctrine/architecture.md:143-146`): doctrine, behavioral requirements,
topology, quality policy, verification contract, handcrafted-region
declaration. The worked example's six match exactly. **Supported.**

**But an unaddressed vocabulary collision:** adopted doctrine already names
this claim. `architecture.md:178-181`: *"**Genome-complete**: a claim about the
**normative corpus itself** — every required Genome element is present,
current, and traceable at the evaluation."* And RFC1-8 rules *"**Converged**
and **genome-complete** are aggregate Claim predicates over a declared scope."*
"Shape present" is genome-complete minus "current and traceable". Neither brief
mentions either word, while `BRIEF.md:157-162` claims *"Not new vocabulary …
Six of the seven facet names are ordinary English compounds of terms the
registry already admits."* Introducing a second name for a doctrine-defined
predicate, then asserting no new vocabulary, is the kind of thing this corpus
catches elsewhere. **Either name the relationship to genome-complete or call
the facet Genome-present.**

### D-5. ✅ Facet 4 (RFC2-2, RFC2-3, RFC2-4, RFC2-10) — hold.

RFC2-2 *"Uncaptured means uninfluential"*
(`RFC-0002/snapshot-and-evaluation-core.md:107-113`); RFC2-3 evaluation
identity as the (snapshot, as-of) pair (`:116-117`); RFC2-4
*"Degradation-only over an unchanged snapshot"* (`:129-139`); RFC2-10's four
freshness states (`:206-210`). The routing's gloss *"RFC2-4 is why this facet
cannot be cached"* (`:90-94`) is a fair reading of *"A later evaluation over
the same snapshot at a later as-of instant may only degrade claims"*.
**Supported.**

### D-6. ⚠️ Facet 5 (RFC8-21, RFC8-22) — the clauses are real; **they are not the chain the brief describes.**

RFC8-21 (`accounting-reconciliation-and-release.md:78-91`) binds this chain:
*"warrant (normative reference or Decision) → approved plan item
(execution-intent Proposal) → materialization record → work item → execution
run(s) → commits/PR → merge fact → reconciliation verdict"*.

The brief's Traceable chain (`BRIEF.md:69-70`) is: *"capability → requirement →
implementation → test → evidence → work → warrant"*.

**These are different chains.** RFC8-21 is work provenance; the brief's is the
specification-to-verification chain. RFC8-21 contains no capability, no
requirement, no implementation, no test. A `re` sweep for
`capability → requirement`, `requirement → implementation`,
`implementation → test`, `test → evidence` across the whole rfcs tree returns
**zero hits** — the brief's chain is not written anywhere in the corpus.

The capability↔code half is owned elsewhere: RFC1-16 / the `implements` and
`covers` edges (`RFC-0001…:473,476`), the **declared implementation mapping**
governance artifact (SDR-4, `RFC-0001…:283-287`), and RFC-0004's
`fidelity-joins-and-mappings.md`. So `ROUTING.md:104`'s *"**Nothing at contract
level. RFC8-21 and RFC8-22 are this facet already**"* is true for the half the
routing quoted and false for the half the brief defined. **Either narrow the
brief's chain to RFC8-21's, or add RFC-0001/0004 to Traceable's owning
contracts.**

### D-7. ✅ Facet 6 (RFC10-7, RFC10-19, RFC10-22, RFC11-4, RFC11-6) — hold.

RFC10-7's envelope minimum (`RFC-0010-mission-control-autonomy.md:194-203`);
RFC10-19 *"An effect class not so classified is not authorized"* (`:529-534`);
RFC10-22's *"an undeclared maximum means one outstanding item — the narrowest
reading"* (`:659-667`); RFC11-4 deterministic mandatory selection
(`RFC-0011-context-compiler.md:105-114`); RFC11-6 *"**Incomplete is Unknown,
and Unknown blocks when policy says complete**"* (`:127-136`). **Supported.**
The routing's own caveat at `:130-134` — that today a Mission-ready answer would
rest on nine hand-authored golden selections and is *"no answer at all for a
tenth"* — is the most honest sentence in the routing document, and it is
consistent with `PROJECT-STATUS.md:76-82`.

### D-8. ✅ Facet 7 (RFC2-17, RFC2-19, RFC2-20, RFC2-21, RFC8-29, RFC8-30) — hold.

RFC2-17 reservation of the words (`RFC-0002/reconciliation-chain.md:104-111`);
RFC2-19 *"The loop is human-triggered"* (`:205-212`); RFC2-20 the closure
fallacy (`:214-221`); RFC2-21's "no gap at E" predicate (`:225-233`); RFC8-29
V0 renders the absence honestly (`…release.md:236-240`); RFC8-30 no aggregate
renders closed as done (`:242-248`). **Supported**, including the routing's
V0-staging note.

### D-9. ✅ Cross-cutting RFC-0006 row — holds.

RFC6-6 *"Outcomes are not Unknown reasons"*
(`RFC-0006-cross-surface-selection-query-drawer.md:142-147`); RFC6-13 *"One
truth, two consumers"* (`:197-203`); RFC6-14 label parity, including *"**A
machine answer never omits epistemic state**"* (`:205-213`); RFC6-15
evaluation-stamping (`:220-224`); RFC6-17 aggregation discloses (`:232-240`).
**Supported.** The routing's *"RFC6-6 is the one to read twice"* is a good
call.

Note a tension it creates: RFC6-17 *permits* aggregates provided they disclose
composition. The brief's rule 4 forbids them absolutely. The corpus's position
is "disclose", the brief's is "never" — a stricter local rule is lawful, but
the brief should say it is deliberately stricter than RFC6-17 rather than
implying the corpus already forbids counting.

### D-10. ❌❌ **The Unknown-reason vocabulary — the finding that falsifies the routing's headline.**

`BRIEF.md:99-102`, rule 3: *"Unknown is a first-class value with a reason … Each
facet declares which Unknown reasons it can emit, **from the closed corpus-wide
vocabulary**."*

The closed corpus-wide vocabulary is **RFC2-24 — "Twelve reasons, closed"**
(`RFC-0002/rendering-vocabularies.md:82-127`): `missing-declaration`,
`missing-evidence`, `no-currency-bound-declared`, `stale-beyond-currency-bound`,
`mapping-coverage-absent`, `unconsented-source-or-provider`, `excluded-content`,
`contradicted-pending-adjudication`, `challenge-suspended`,
`source-uncaptured-or-unreachable`, `reference-unresolvable`,
`execution-blocked`.

RFC2-24's own terms: *"Every Unknown claim instance carries exactly one primary
reason from this list … the list changes only by amendment to this RFC"*
(`:82-84`), and *"no implementation may mint, spell, or force-fit a secondary
value the list does not carry"* (`:91-93`), and *"A condition genuinely not
among the twelve is disclosed as a **fact of the render** — named, expandable,
routed to its resolving action — **never dressed as a reason**; the honest move
is to amend this list, never to annotate outside it"* (`:100-104`).

The briefs emit four Unknown reasons. **Three are not in the twelve:**

| Reason used | Where | In RFC2-24's twelve? |
|---|---|---|
| `governing-contract-unaccepted` | `BRIEF.md:132`, `BRIEF.md:192`, `ROUTING.md:126` | **No** |
| `no-evaluation-performed` | `BRIEF.md:141`, `BRIEF.md:181` | **No** |
| `no-declared-intent-in-scope` | `BRIEF.md:194` | **No** |
| `missing-declaration` | `BRIEF.md:188` | Yes (#1) |

Consequences, in order of severity:

1. **The routing's headline result is false as stated.**
   `ROUTING.md:192`: *"**Six of seven facets need no new clause.** That is the
   result this document was written to establish."* Emitting these three
   reasons requires **an amendment to RFC-0002** by RFC2-24's own closure rule.
   That is a contract gap in **Human-understandable, Mission-ready and
   Reconciled** — three facets, not one. The summary table
   (`ROUTING.md:182-190`) shows `—` in the "Contract gap" column for
   Mission-ready and Reconciled; both should read `yes`.
2. **RFC6-14 becomes unsatisfiable.** It requires the Unknown reason
   *"verbatim from the RFC 0002 vocabulary"* (`:205-208`). A minted reason
   cannot be carried verbatim from a vocabulary that does not contain it, which
   is the exact argument RFC2-24 gives for closing the list at all.
3. **Each minted reason has a plausible existing mapping**, which makes the
   minting gratuitous: `no-declared-intent-in-scope` → #1
   `missing-declaration`; `no-evaluation-performed` → #2 `missing-evidence`;
   `governing-contract-unaccepted` → arguably #1, or (better, and exactly what
   RFC2-24 prescribes) *a fact of the render*, not a reason.

This is not a nit. The brief's entire claim to be *"a projection of the corpus
rather than an addition to it"* (`ROUTING.md:194-195`) rests on reusing the
corpus's closed vocabularies, and at the first contact with one it minted three
values. **Fix:** map every facet's Unknown reasons onto the twelve, and where
one genuinely does not fit, either propose the RFC-0002 amendment openly (the
brief already knows how to name a gap and leave it unfilled — see
`HUMAN-ENTRY-POINT-BRIEF.md:165-168`) or render it as a fact of the render per
RFC2-24's own instruction.

### D-11. ⚠️ Three cited sibling documents do not exist.

`ROUTING.md:134` cites `FINAL-CONTEXT-SELECTION-REPORT.md`;
`ROUTING.md:203` / `BRIEF.md:213` cite `OWNER-DECISION-PACKETS.md` ("packet
6"); `BRIEF.md:208-209` and `HUMAN-ENTRY-POINT-BRIEF.md:163` cite
`FIRST-OPENSPEC-SEQUENCE.md` ("Capability 1"). A filename sweep across
`.syzygy/**` finds **none of the three**. Every facet's specification gap
routes to "Capability 1 in `FIRST-OPENSPEC-SEQUENCE.md`", so the routing's
entire right-hand column points at an artifact that is not in the tree.

If they are forthcoming in this round, say so; if they are elsewhere, fix the
paths. As it stands the routing's forward references are dangling, which is the
condition RFC7-11 renders Unknown and RFC7-31 calls a release-blocking trust
floor when it happens on a walkthrough path.

### D-12. ✅ Entry-point brief's own routing table (`:156-163`) — spot-checked, holds.

RFC7-3 *"Nothing cites the rendering"* (`narrative-contract.md:98-107`);
RFC7-4 *"Non-authority is total"* (`:109-111`); RFC3-18 *"`intent/`, `work/`,
and `map/` are schema-versioned governed namespaces"*
(`manifests-and-namespace.md:310-315`); VIS-5's two-namespace confinement
(`doctrine/vision.md:141-165`). **Supported.** The one clause I would question
is RFC3-1 as a home for "the two-root write boundary" — RFC3-1
(`manifests-and-namespace.md:94-104`) is about manifests as semantic contracts
and serialization, not the write boundary; the boundary is VIS-5 plus RFC3-29
/ RFC3-30. Minor.

---

## E. The discoverability finding — honest, or a way of never solving it?

**Honest on the doctrine, and the write boundary genuinely is not negotiable.
But the finding is scoped and placed in ways that make it weaker than it needs
to be, and the brief does not say so.**

### E-1. The write boundary is correctly read. [Observed]

VIS-5 (`doctrine/vision.md:141-149`): *"Syzygy's **direct project-content
writes** touch only `openspec/**` … and `.syzygy/**` … No governance manifest,
configuration, or convention may extend that direct-write universe … it may
never directly create, modify, move, or delete project content outside its two
roots."* The adapter carve-out is explicitly for *"version-control metadata such
as commits and tags, configured work-scheduler state, CI, runtime systems"* —
a root README is project content, not metadata. RFC3-7's write consent is
*"write (governance-root plane only)"* (`manifests-and-namespace.md:190-191`).

So `HUMAN-ENTRY-POINT-BRIEF.md:84-88` — *"The two-root boundary is not a rule
with a discoverability carve-out; a carve-out is how a write boundary stops
being one"* — is **correct, and I would not soften it.** Rendering the gap
rather than writing the fix is the right call, and §6's admission that *"A `no`
on discoverability may sit forever"* (`:148-151`) is the honesty this project
claims for itself.

### E-2. But the finding is under-scoped and mis-placed. [Inferred]

Two changes would make it a real instrument rather than a gesture, and neither
touches the boundary:

- **Per repository, not per project** — see **A-3**. As written, N−1
  repositories of an N-repository project have no entry point *and no rendered
  gap saying so*. RFC3-6 already owns repository entries and the brief already
  routes the finding there (`:162`); making the answer per-entry is free.
- **The finding belongs to Human-understandable, not Registered.** The brief
  puts it under Registered because *"promoting it would make eight facets where
  seven is already at the edge"* (`:117-119`). That is a presentation argument
  applied to a placement decision. Discoverability is *about* whether a human
  can find the project — Human-understandable's exact subject, and RFC7-30's
  first clause is *"entering at the primary narrative"*, which presupposes the
  reader got there. Under Registered, a project renders `Registered: true` with
  `discoverable: no` buried in a drawer, while the facet a newcomer would
  actually consult about human comprehension is silent on whether a human can
  reach the door at all.

### E-3. **The strongest evidence that "render, don't write" is insufficient is this repository.** [Observed]

I checked whether any default-path artifact leads to the briefs. A string sweep
of `README.md`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`, `AGENTS.md`,
`.syzygy/intent/OVERVIEW.md`, `PENDING-OWNER-DECISIONS.md`,
`contracts/candidates/00-README.md` and `contracts/candidates/README.md` for
`round-2026-08c`, `HUMAN-ENTRY-POINT-BRIEF` and `PROJECT-SHAPE-FACETS` returns
**zero hits in all eight files.**

The documents that define the human entry point for every governed project are
themselves unreachable from this project's human entry point. Nothing renders
that gap; nothing proposes a fix; the round's own material is invisible to the
reader it is written for. Whatever the answer is for a root README under a write
boundary, **this** case is squarely inside `.syzygy/**` — writable, governed,
and unaddressed. It is the cleanest possible demonstration that "render the
gap" only works when something is actually rendering.

### E-4. What I would do instead, given the boundary holds.

1. **Per-repository finding** (E-2), so the gap is at least fully rendered.
2. **Make it a registration-time question, not only an ongoing render.**
   Registration is an owner act with consent records (RFC3-7). Asking the owner
   once, at the act, "does your front door link here? (yes / no / I'll do it
   later)" costs one line in the ceremony, is not a gate on anything, and
   catches the case at the only moment the owner is already present and
   motivated. The brief's *"Not a gate"* (`BRIEF.md:150-152`) is about facets
   blocking work; a question asked during a ceremony blocks nothing.
3. **Ship the proposal as an applyable artifact, not prose.** §4 item 3 says
   the proposal *"states exactly what it would add and where, so that applying
   it is a five-second decision"* (`:112-113`). VIS-5 explicitly permits
   committing *"the **proposal artifact itself** into `.syzygy/**`"*
   (`doctrine/vision.md:155-156`). Make it a patch file the owner applies with
   one command. That is the difference between a finding and a fix, and it is
   entirely inside the boundary.

---

## F. Registration is not certification — is the distinction actually clear?

**The sentence is good. Its placement obligation is under-specified, and the
facet set as rendered will still be read as a scoreboard.**

### F-1. The sentence itself. [Observed]

`HUMAN-ENTRY-POINT-BRIEF.md:126-130` / `BRIEF.md:153-156`: *"Registering a
project grants a declared observation and governance relationship. It does not
certify that the project is shaped, understandable, observable, traceable,
Mission-ready, or reconciled."*

It is quotable, it is correct, and naming the six other facets *"on purpose"*
(`:131-134`) is the right instinct. I would keep it verbatim.

### F-2. But it presupposes the reader knows the facets. [Inferred]

A newcomer meeting `Registered: true` for the first time reads a sentence whose
back half is a list of six words they have not yet been taught. "shaped",
"understandable", "observable", "traceable", "Mission-ready", "reconciled" are
facet labels, not plain English at that moment. The correction lands only for a
reader who has already read the facet set — i.e. not the reader
`HUMAN-ENTRY-POINT-BRIEF.md:131-134` says it exists for.

**Fix:** render the sentence *with the six live answers inline*, so the
disclaimer and the evidence arrive together: "does not certify that the project
is shaped (`false`), understandable (`Unknown`), observable (`true`)…". Then it
is not a disclaimer, it is the data.

### F-3. **Nothing makes the sentence travel with the machine answer.** [Observed]

`HUMAN-ENTRY-POINT-BRIEF.md:123-125` requires it *"human-visible on the entry
point **and** machine-queryable through the same API"*. But "machine-queryable"
is not "attached". RFC6-14 binds *labels* to travel with every machine answer
(`RFC-0006…:205-213`); a prose disclaimer is not a label and no clause makes it
accompany a `Registered: true` response. An agent that queries the Registered
facet gets `true` and nothing else, and — per RFC7-33's own warning about
external consumers — *"It can tell draft from curated and not presentation from
authority"* (`rendering-and-surface.md:203-206`).

If the sentence is load-bearing, it needs a home that travels: a required field
on the Registered facet's answer, not a paragraph on a page.

### F-4. **Would they still read `true` as endorsement? Probably yes, for one avoidable reason.** [Inferred]

Registered is listed **first**, is the **only facet a project can satisfy on
its own paperwork** (`BRIEF.md:44-46`, stated plainly and well), and in the
worked example is one of the two `true`s in a column of `false`/`Unknown`. A
reader scanning that column does not see seven independent measurements; they
see a checklist with two ticks. Rule 4 forbids Syzygy from computing "2 of 7";
it cannot stop a reader's eye from computing it, and the brief's own summary
line does it for them — see **G-2**.

---

## G. The worked example — honest?

**Mostly yes. It is the best part of the brief. But it violates two of the
brief's own rules within twenty lines of stating them, and one reading of it is
misleadingly reassuring.**

### G-1. What is honest and good. [Observed]

`BRIEF.md:168-195`. Every answer carries a reason or a detail line. Traceable's
detail *"no capability→requirement links declared; this is not '0% traceable'"*
(`:189-190`) is exactly right and is the sort of thing most status systems get
wrong. `Human-understandable Unknown` on a project with no narrative is the
honest answer. The takeaway sentence at `:199-201` — *"the project is
registered and readable; nothing has been declared about what it is supposed to
do"* — is genuinely actionable, and it is the sentence a badge would have
destroyed. If the model survives, this example is why.

### G-2. ❌ **The example's own summary emits the count rule 4 forbids.** [Observed]

Rule 4 (`:103-106`): *"They never roll up. No colour, no score, **no
count-of-facets-passing, no '5 of 7'**. A count is a composite wearing a
different hat."*

Line 197: *"**Six of the seven answers are useful and two of them are
`true`.**"*

That is a count of facets passing, in bold, in the summary of the example that
demonstrates the rule. "Six of seven" and "two of them are true" are two
composites in one sentence. The very next sentence says *"No score is
computable from this and none should be"* (`:198-199`) — immediately after
computing two.

Whether "useful" is a defensible axis is beside the point: a reader who has
just been told never to count is shown a count as the takeaway. Delete the
sentence; `:199-201` already carries the takeaway better.

### G-3. ❌ **The Shape present line emits the fraction the routing forbids.** [Observed]

`ROUTING.md:57-60`: *"It must report **per class**, never as a count. '4 of 6
Genome classes present' is a composite inside a facet, and it makes *doctrine
absent* and *handcrafted-region declaration absent* interchangeable."*

`BRIEF.md:179`: *"(six classes examined, four missing)"*.

That is "4 of 6" in different words, appended to the per-class list the routing
demanded instead of it. There is a real defence — RFC6-17 requires an aggregate
to disclose its denominator (`RFC-0006…:232-240`), and "six examined" is
exactly that disclosure — but then the routing's absolute prohibition is wrong
and should be restated as "disclose the denominator, never substitute the
fraction for the classes". As it stands, brief and routing contradict each
other over one line of one example.

### G-4. ⚠️ **The same epistemic situation produces `false` in one facet and `Unknown` in another, with no stated principle.** [Inferred]

In the example, *nothing has been declared* produces:

- `Shape present: false` — "doctrine: absent", "topology: absent"…
- `Traceable: Unknown — missing-declaration` — "no capability→requirement links
  declared".

Both are absent declarations. Rule 5 (`:108-112`) — *"A missing declaration and
failed evidence are different answers … Collapsing them is the single most
common way a status system lies"* — is the rule a reader will reach for, and it
tells them a missing declaration should render as its own thing, which
Traceable does and Shape present does not.

There *is* a good answer (Shape present asks "is it declared?", so absence is
the answer; Traceable asks "do declared links resolve?", so with no denominator
there is nothing to answer). **The brief never states it**, and without it the
example teaches a reader that the false/Unknown boundary is discretionary —
which is the door through which "make it green" eventually walks.

### G-5. **The misleadingly reassuring reading, stated plainly.** [Inferred]

Take the example exactly as printed and read only the value column:

```
true / false / Unknown / true / Unknown / Unknown / Unknown
```

Four of the seven Unknowns and falses are *unfalsifiable or staged*:
Human-understandable **cannot be false** (C-1), Traceable **cannot be false**
(C-2), Mission-ready is `Unknown` for an institutional reason that has nothing
to do with this project (`governing-contract-unaccepted` — it will read
identically for every project on earth until act 1), and Reconciled is
`Unknown` for want of declared intent.

So the two `true`s are the only facets in the example that were genuinely at
risk of being false and were not. A reader who does not notice this reads
"2 true, 1 false, 4 not-yet-measured" — a project one step from good. The
accurate reading is "2 measured true, 1 measured false, 4 not measurable by
this system today". **The example does not distinguish "Unknown because this
project is thin" from "Unknown because Syzygy cannot yet answer this for
anyone."** Mission-ready's line is the sharpest case: it is a constant, not a
measurement, and printing it in the same column as measured answers is the
closest thing in these briefs to comprehensible fiction.

**Fix:** mark the staged facets visibly as staged — the brief already knows to
do this in prose (`:123-142`, "Staging — the facet that is not like the
others") and then does not do it in the example that a reader will actually
remember.

---

# What would move this to CONFIRM

Ordered by weight. All are one-pass repairs; none requires rethinking the
model.

1. **Map every Unknown reason onto RFC2-24's closed twelve** (D-10), or
   propose the RFC-0002 amendment openly. Correct the summary table's contract-gap
   column for Human-understandable, Mission-ready and Reconciled.
2. **Read RFC-0007 module 2 and rewrite Facet 3's routing** (D-2). RFC7-30/31/32
   already define the fresh-reader evaluation, its two record homes, and its
   cadence. Narrow the stated gap to tier-admission and expiry. Reconcile the
   entry point's eight questions with RFC7-30's six prompts, or say why there
   are two lists.
3. **Remove the fabricated RFC3-4 quotation** (D-3); cite RFC3-9 with its actual
   word, `unparseable`, and say what happens in the *missing* case
   (RFC3-9's drafting route).
4. **Make the discoverability finding per declared repository entry** (A-3,
   E-2), and add the N-repository blind spot to §6's honest costs.
5. **Give Human-understandable and Traceable a constructible `false`** (C-1,
   C-2) — RFC7-31's two floors supply the first — or state that they are
   two-valued and why.
6. **Fix the worked example** (G-2, G-3, G-5): delete "six of the seven answers
   are useful and two of them are `true`"; reconcile "(six classes examined,
   four missing)" with the routing's per-class rule; mark staged facets as
   staged in the example itself.
7. **Reconcile the two briefs on Registered's value domain** (B-5) —
   `Contradiction` is in one document and not the other.
8. **Give Observable a declared scope** (B-2), so it cannot silently disagree
   with scope-selected Reconciled.
9. **Fix or explain the three dangling sibling citations** (D-11).
10. **Address RFC7-3's deletion invariant** for an entry point that lives in
    `.syzygy/intent/**` (A-4) — RFC7-31 shows the pattern.
11. **Name the relationship to doctrine's `genome-complete`** (D-4), or rename
    the facet.

---

# Would the briefs let me answer the six questions for an arbitrary project?

| Q | Covered by the design? | Assessment |
|---|---|---|
| 1 What is this | **Yes** | Entry-point row 1 → RFC7-6's primary narrative. Well routed. |
| 2 Promise / refusal | **Partly** | Row 2 covers the promise via the project's own doctrine, and *"a plain statement that it declares none"* is the right fallback. **The refusal half is unbacked**: nothing requires a non-goal to be reachable, while RFC7-30 makes reaching a non-goal's rule text a load-bearing prompt. Add it. |
| 3 Missing / Unknown | **Yes** | Row 8 plus per-facet Unknown reasons — the strongest part of the design, once the reasons come from RFC2-24. |
| 4 Who owns the answer | **Yes, and this is the design's best idea** | Facets are derived claim classes over named contract inputs; every answer carries evaluation identity (rule 2, RFC6-15). A reader can always ask "what would settle this". |
| 5 Exact requirements | **Yes** | Row 4 → `openspec/**` routed by capability. Same clean answer this repo gives. |
| 6 Entry point exposed | **Partly, and knowingly** | One repository per project, rendered not fixed. Honest about the boundary; not honest about the N−1 repositories it cannot see (A-3). |

**Four and a half of six** would be answerable for an arbitrary governed
project under this design as drafted; six of six with the repairs above.

---

*End of RD-2. Raw reviewer output, stored verbatim.*
