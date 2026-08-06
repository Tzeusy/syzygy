# Project-shape facets — candidate design brief

> **Candidate design material. Binds nothing, accepts nothing, and specifies
> nothing.** User-observable behaviour is defined in OpenSpec, which does not
> exist yet. This brief describes a *model* and routes each part of it to the
> contract that would own it; the routing is
> `PROJECT-SHAPE-FACETS-ROUTING.md`. Where this brief and a contract clause
> disagree, the clause wins.

## The question this answers

An owner registers a project with Syzygy. What can Syzygy then say about it?

The wrong answer is a badge. `compliant`, `healthy`, `mature`, a score, a
traffic light — every one of them takes six or seven independent facts, at
least two of which are Unknown, and reports one colour. A single value cannot
be honest about a set of independent measurements, and the moment it exists,
the pressure to make it green is applied to whichever fact is easiest to move
rather than to whichever fact matters.

**There is no composite. There will not be one.** This brief defines seven
facets that are computed separately, rendered separately, and never rolled up.

## The seven facets

Each answers one plain question. Each has its own evidence, its own Unknown
reasons, and its own evaluation identity.

| Facet | Plain-language question |
|---|---|
| **Registered** | Is there a valid project declaration, an owner, a declared repository set, and consent? |
| **Shape present** | Are the required Project Genome classes declared and reachable? |
| **Human-understandable** | Is there a primary narrative, and has it passed the current fresh-reader test? |
| **Observable** | Can Syzygy read the declared repositories and required evidence sources, at a current evaluation? |
| **Traceable** | Do capabilities, requirements, implementation, tests, evidence and work resolve through declared links? |
| **Mission-ready** | Can a lawful Mission envelope and a complete context packet be formed? |
| **Reconciled** | Does current evidence satisfy the declared intent, for the selected scope? |

### What each facet is, precisely

**Registered.** A `project.yaml` exists at exactly one governance root, parses
against its closed field set, names an owner, declares its repository set, and
carries the consent records the declared sources require. This is the only
facet a project can satisfy on its own paperwork.

**Its value domain is four-valued, not three:** `true` · `false` · `Unknown` ·
**`Contradiction`**. RFC3-4 routes the two-roots case — two repositories each
claiming to be the same project's governance root — to contradiction machinery
rather than picking a winner, so the facet must be able to say so. A boolean
facet would have had to choose one, silently. *(Review RD-2 finding B-5: the
routing document carried this value and this brief did not; a facet's value
domain stated in one document and not the other is the drift the two-document
split makes easy.)*

**Shape present.** The Project Genome's universally-required classes are
declared and each declaration resolves to something reachable. Note the shape
of the question: *declared and reachable*, not *good*. A project with a
one-line doctrine file and an empty handcrafted-region declaration is Shape
present. What it says is a different facet's problem, and mostly not Syzygy's.

**Human-understandable.** A primary narrative exists, its source anchors
resolve, and a fresh reader unfamiliar with the project could answer the
project's own version of *what is this, what does it promise, what is Unknown,
which artifact owns the answer*. This facet is the only one whose evidence is
a **human judgment recorded as evidence** rather than a computed predicate,
and it is stated that way rather than faked into a metric.

**Observable.** At a named evaluation, Syzygy could actually read the declared
repositories and the evidence sources the other facets depend on. This is the
facet that most often degrades without anything changing in the project: a
token expires, a CI provider's retention window passes, a repository is
renamed. It is therefore **evaluation-stamped and degrades by default** — an
Observable answer with no as-of instant is not an answer.

**Traceable.** The declared links resolve, in both directions, across the
chain: capability → requirement → implementation → test → evidence → work →
warrant. A broken join renders as broken; it is never skipped. This facet
reports **coverage of the declared links**, and says nothing about links
nobody declared — a project can be perfectly Traceable and describe almost
nothing, which is why it is not a quality score.

**Mission-ready.** Two conditions, both mechanical: a lawful Mission envelope
could be formed for this project (its consent, execution profiles, effect
classifications and attention bounds are declared and internally consistent),
and a complete context packet could be compiled for at least one declared task
class. **This facet depends on unaccepted Mission doctrine and says so** — see
"Staging", below.

**Reconciled.** For a *selected scope* — never for a project as a whole —
current evidence satisfies the declared intent. Reconciliation is the
expensive one, the human-triggered one, and the one that decays fastest. It is
last because everything above it is a precondition, and because a project that
is not Observable cannot be Reconciled: it can only be Unknown.

## The ten rules these facets live under

1. **They are independent.** No facet is computed from another. Several are
   *precondition-related* — an unregistered project cannot be Observable —
   and the relationship is rendered as an Unknown *reason*, never as a
   propagated value. "Unknown, because Registered is false" is an answer;
   silently inheriting `false` is not.

2. **Each carries exact source and evaluation identity.** Every facet answer
   names the (source snapshot, as-of instant) pair it was computed at, and
   the artifacts it read. A facet answer with no evaluation identity is not an
   answer.

3. **Unknown is a first-class value with a reason.** Not `false`, not `0`, not
   an empty badge. Each facet declares which Unknown reasons it can emit,
   **verbatim from RFC2-24's closed twelve** — `missing-declaration`,
   `missing-evidence`, `no-currency-bound-declared`,
   `stale-beyond-currency-bound`, `mapping-coverage-absent`,
   `unconsented-source-or-provider`, `excluded-content`,
   `contradicted-pending-adjudication`, `challenge-suspended`,
   `source-uncaptured-or-unreachable`, `reference-unresolvable`,
   `execution-blocked`.

   **This rule was violated by an earlier revision of this brief, and the
   violation is worth keeping visible.** It minted three reasons the
   vocabulary does not carry. RFC2-24 forecloses exactly that: *"no
   implementation may mint, spell, or force-fit a secondary value the list
   does not carry"*, and *"A condition genuinely not among the twelve is
   disclosed as a **fact of the render** — named, expandable, routed to its
   resolving action — never dressed as a reason; the honest move is to amend
   this list, never to annotate outside it."* Review RD-2 caught it at the
   brief's first contact with a closed corpus vocabulary — in the document
   whose whole claim is to be a projection of the corpus rather than an
   addition to it. Every reason below is now one of the twelve; conditions
   that are not are rendered as **facts of the render**, in the detail line.

4. **They never roll up.** No colour, no score, no count-of-facets-passing, no
   "5 of 7". A count is a composite wearing a different hat: it makes two
   projects with disjoint failures look identical, and it makes the cheapest
   facet the one to fix.

5. **A missing declaration and failed evidence are different answers.**
   "You never declared a test suite" and "your test suite could not be read"
   are different facts with different remedies. Collapsing them is the single
   most common way a status system lies.

6. **Both humans and agents get the same answers.** One semantic API, the same
   labels, the same Unknown reasons, the same evaluation stamps — the facets
   are not a UI feature with an API afterthought.

7. **They reuse existing entities and evaluation semantics.** A facet is a
   **derived claim class over the existing graph**, not a new record type and
   not a new store. Seven facets must not become seven truth stores; the
   routing document's job is to show that each one is computable from what
   the corpus already defines.

8. **Anything resting on unaccepted doctrine is staged and says so** — in the
   facet's own answer, not only in a staging section elsewhere.

9. **Every facet declares its own scope, in its own answer.** Observable's
   scope is the declared repository and evidence-source set; Traceable's is
   the declared link set; Reconciled's is the *selected* scope, which is
   narrower than both and chosen per query. A facet that reports a result
   without naming what it examined lets a reader read narrow coverage as broad
   — and lets two facets over different scopes appear to contradict each other
   when they do not. *(Review RD-2 finding B-2 constructed exactly that case:
   an Observable computed over the full declared set and a Reconciled computed
   over a narrower selected scope can disagree with no defect anywhere.
   Disagreement between differently-scoped facets is not a contradiction; it
   is two answers to two questions, and only visible scope makes that
   legible.)*

10. **A facet that cannot be `false` is not a facet.** For each of the seven,
    the project state that makes it `false` must be constructible and
    written down. Two were caught failing this test by review RD-2:

    - **Human-understandable.** Its `false` comes from **RFC7-31's two
      floors** — *"a dangling internal link on the walkthrough path fails
      (trust floor, release-blocking)"* and *"a confident wrong answer
      attributable to what the surface rendered fails"*. Both are recorded
      verdicts, not judgment calls, so `false` is reachable without anyone
      grading a narrative.
    - **Traceable.** Its `false` is a **declared link that does not resolve** —
      distinct from `Unknown — missing-declaration`, which is the answer when
      no link was declared at all. The distinction is rule 5, and without it
      Traceable would be two-valued.

    Where a facet is genuinely two-valued, it says so and says why. None of
    the seven currently is.

## Staging — the facet that is not like the others

**Mission-ready depends on material that is not adopted.** RFC-0010 is a
candidate contract inside act 1's digest subject, and whether bounded missions
are lawful under unamended doctrine is open question **D4** (owner item
**P-24**). Until both resolve, Mission-ready is:

> **`Unknown` — reason: `missing-declaration`**, with the render fact
> *"governing contract unaccepted (RFC-0010 candidate; owner items P-24,
> P-28)"* named beside it.

`missing-declaration` is reason #1: *"No governing declaration … exists."* An
unaccepted candidate contract is not a governing declaration, so the reason
fits without stretching. **Why the contract's candidate status is a render fact
and not a reason:** it is a condition of *Syzygy's own corpus*, not of the
governed project, and RFC2-24 says a condition outside the twelve is named,
expandable and routed — never dressed as a reason.

Not `false`. Not omitted from the set. The facet exists, it is queryable, and
its answer states exactly why it cannot be computed. A facet that disappears
when its authority is missing teaches the reader that the question does not
matter.

**Human-understandable is staged differently and for a different reason.** Its
evidence is a recorded human judgment — and, contrary to an earlier revision of
this brief, **the process that produces one already exists in the corpus**:
RFC7-30 defines the cold-open comprehension walkthrough, RFC7-31 its verdict
discipline and two record homes, RFC7-32 its cadence. Absent that record the
answer is **`Unknown` — reason: `missing-evidence`** (#2: *"Declaration
exists; no current evidence artifact for the claim"*), which is RFC7-30's own
outcome in its own words: *"absent its record, the test renders Unknown, never
met."*

## What this is *not*

- **Not a scoring system.** There is no rank, no percentage, no comparison
  between projects.
- **Not a gate.** No facet blocks anything. Facets are *rendered*; whether a
  low answer should stop work is an owner's policy call, and a different
  contract's business.
- **Not certification.** Registering a project grants a declared
  observation and governance relationship. **It does not certify that the
  project is shaped, understandable, observable, traceable, Mission-ready, or
  reconciled.** That sentence is meant to be quotable, and it is the reason
  Registered is a facet in its own right rather than a precondition hidden
  from view.
- **Not new vocabulary.** Six of the seven facet names are ordinary English
  compounds of terms the registry already admits. None is proposed for
  admission to the term registry: a facet is a *derived claim class*, and its
  name is a label on an answer, not a concept a reader must learn. See
  `TERM-REGISTRY-SEMANTIC-DELTA.md` on internal metadata versus public
  vocabulary.

## Worked example — a project that is honestly mixed

A real repository, freshly registered, with CI and no narrative:

```text
Registered            true       @ eval-2026-08-06T12:00Z
                                 project.yaml parses; owner declared;
                                 2 repositories; 1 consent record

Shape present         false      doctrine: absent
                                 behavioral requirements: absent
                                 topology: absent
                                 quality policy: declared → reachable
                                 verification contract: declared → reachable
                                 handcrafted-region declaration: absent

Human-understandable  Unknown    reason: missing-evidence
                                 no primary narrative is declared (RFC7-6);
                                 no walkthrough record (RFC7-30/31)

Observable            true       @ eval-2026-08-06T12:00Z
                                 declared scope: 2 repositories, 1 CI provider
                                 2 of 2 repositories readable
                                 CI provider readable, retention 90d

Traceable             Unknown    reason: missing-declaration
                                 no capability→requirement links declared;
                                 this is not "0% traceable"

Mission-ready         Unknown    reason: missing-declaration
                                 render fact: governing contract unaccepted
                                 (RFC-0010 candidate; P-24, P-28) — STAGED

Reconciled            Unknown    reason: missing-declaration
                                 no declared intent in scope
```

**What a reader takes away is specific:** *the project is registered and
readable; nothing has been declared about what it is supposed to do.* That is
an actionable sentence, and it is what a green "4/7" would have destroyed.

**Three things this example is careful about, each because an earlier revision
was not:**

- **No count anywhere.** The earlier revision closed with *"six of the seven
  answers are useful and two of them are `true`"* and annotated Shape present
  with *"(six classes examined, four missing)"* — a count of facets and a count
  within a facet, in the example illustrating rule 4's ban on counts. Review
  RD-2 found both. Per-class lines carry the information; the tally added
  nothing except the thing the rule forbids.
- **`Mission-ready` is marked STAGED in the example itself**, not only in the
  staging section three screens above it. A reader who meets the facet set here
  first would otherwise read a staged facet as an ordinary Unknown.
- **`Observable` names its declared scope** before its result, so *"2 of 2
  readable"* cannot be mistaken for coverage of everything the project
  contains. See rule 9.

**Two kinds of Unknown, and the example must not blur them.** Review RD-2 read
the example's value column alone and got *"2 true, 1 false, 4 not-yet-measured
— a project one step from good"*, where the accurate reading is *"2 measured
true, 1 measured false, 4 not measurable by this system today."* The sharpest
case is Mission-ready: **it is a constant, not a measurement.** It will read
identically for every project on earth until act 1, and printing a constant in
the same column as measured answers is the closest thing in these briefs to
comprehensible fiction. Hence the `STAGED` marker in the example itself — a
reader must be able to tell *"Unknown because this project is thin"* from
*"Unknown because Syzygy cannot yet answer this for anyone."*

**Why `Shape present` is `false` and `Traceable` is `Unknown` on the same
project** — the distinction a reader will trip over, and it is rule 5 doing its
work: *Shape present* asks whether a **declaration** exists, and its absence is
directly observed, so `false` is the honest answer. *Traceable* asks about
links between things that were **never declared in the first place**, so there
is nothing to have observed — `Unknown — missing-declaration`. The test is
whether the negative was **observed** or merely **unobservable**.

## Where this goes next

Nothing here is implementable now. Each facet's observable behaviour — how it
is computed, what it renders, what it emits over the API — is routed to
future OpenSpec by `PROJECT-SHAPE-FACETS-ROUTING.md`, and the first
capability that would carry them is **Capability 1** in
`FIRST-OPENSPEC-SEQUENCE.md`.

The one thing that should be decided *before* that: whether the owner accepts
seven independent facets and rejects a composite. That is a decision packet,
not an agent's call — `OWNER-DECISION-PACKETS.md`, packet 6.
