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

## The eight rules these facets live under

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
   an empty badge. Each facet declares which Unknown reasons it can emit, from
   the closed corpus-wide vocabulary.

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

8. **Anything resting on unaccepted doctrine is staged and says so.**

## Staging — the facet that is not like the others

**Mission-ready depends on material that is not adopted.** RFC-0010 is a
candidate contract inside act 1's digest subject, and whether bounded missions
are lawful under unamended doctrine is open question **D4** (owner item
**P-24**). Until both resolve, Mission-ready is:

> **`Unknown` — reason: `governing-contract-unaccepted`.**

Not `false`. Not omitted from the set. The facet exists, it is queryable, and
its answer states exactly why it cannot be computed. A facet that disappears
when its authority is missing teaches the reader that the question does not
matter.

**Human-understandable is staged differently and for a different reason.** Its
evidence is a recorded human judgment. Until there is a declared process that
produces one, it is `Unknown — reason: no-evaluation-performed`, which is the
honest answer for every project that has never been read by a fresh reader.

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
                                 (six classes examined, four missing)

Human-understandable  Unknown    reason: no-evaluation-performed
                                 no primary narrative is declared

Observable            true       @ eval-2026-08-06T12:00Z
                                 2 of 2 repositories readable
                                 CI provider readable, retention 90d

Traceable             Unknown    reason: missing-declaration
                                 no capability→requirement links declared;
                                 this is not "0% traceable"

Mission-ready         Unknown    reason: governing-contract-unaccepted

Reconciled            Unknown    reason: no-declared-intent-in-scope
```

**Six of the seven answers are useful and two of them are `true`.** No score
is computable from this and none should be. What a reader takes away is
specific: *the project is registered and readable; nothing has been declared
about what it is supposed to do.* That is an actionable sentence, and it is
what a green "4/7" would have destroyed.

## Where this goes next

Nothing here is implementable now. Each facet's observable behaviour — how it
is computed, what it renders, what it emits over the API — is routed to
future OpenSpec by `PROJECT-SHAPE-FACETS-ROUTING.md`, and the first
capability that would carry them is **Capability 1** in
`FIRST-OPENSPEC-SEQUENCE.md`.

The one thing that should be decided *before* that: whether the owner accepts
seven independent facets and rejects a composite. That is a decision packet,
not an agent's call — `OWNER-DECISION-PACKETS.md`, packet 6.
