# Project-shape facets — routing to existing contract homes

> **Candidate routing material. Binds nothing.** Its job is to show that the
> seven facets in `PROJECT-SHAPE-FACETS-BRIEF.md` are computable from
> contracts that already exist, and to name precisely what is missing where
> they are not. Every clause cited is **candidate** — inside act 1's digest
> subject, binding nothing until the act. Where this file and a clause
> disagree, the clause wins.

## The test this document has to pass

> **Seven facets must not become seven truth stores.**

A facet is a **derived claim class over the existing graph** — computed at an
evaluation, from records other contracts already own. If a facet needs a new
record type, a new store, or a new authority, then it is not a facet, it is a
feature, and it needs a contract of its own.

Each row below therefore answers three questions: which contract owns the
inputs, what the smallest missing piece is, and whether that piece is a
**contract gap** (needs clause text) or a **specification gap** (needs
OpenSpec, which is the correct place and does not exist yet).

---

## Facet 1 — Registered

| | |
|---|---|
| **Owning contract** | **RFC-0003** `manifests-and-namespace` |
| **Inputs, by clause** | RFC3-4 (location is designation — the declaration lives at exactly one governance root); RFC3-5 (the closed top-level field set); RFC3-6 (repository entries and declared repository identity); RFC3-7 (consent records as governance acts); RFC3-8 (revocation and withdrawal) |
| **How it computes** | Does `.syzygy/project.yaml` exist at one governance root, parse against RFC3-5's closed field set, name an owner, declare ≥1 repository per RFC3-6, and carry an in-force RFC3-7 consent record for every declared source that requires one? |
| **Unknown reasons available** | RFC3-4's own rule already supplies the sharpest one: *"a missing or invalid `project.yaml` renders every dependent claim Unknown"* — the contract says the fail-closed direction outright |
| **What is missing** | **Nothing at contract level.** Every input is a declared clause today |
| **Gap class** | **Specification** — the facet's rendering and API shape route to OpenSpec Capability 1 |

**Note on the honest edge.** RFC3-4 governs the *contradiction* case (two
repositories each claiming to be the same project's root) by routing it to
contradiction machinery rather than picking a winner. Registered must
therefore be able to answer `Contradiction`, not only true/false/Unknown —
which the corpus already supports, and which a boolean facet would have lost.

---

## Facet 2 — Shape present

| | |
|---|---|
| **Owning authority** | **`architecture.md` "Project Genome" (adopted)** — the three-tier inventory. **RFC1-8** (candidate) supplies the mechanism |
| **Inputs, by clause** | `architecture.md`'s universally-required tier (doctrine and behavioural requirements; topology and quality policy; the verification contract; a handcrafted-region declaration, which may be empty), its required-when-present tier, and its not-Genome exclusions. RFC1-8 rules Genome a **membership predicate over the declared inventory**, not a graph entity |
| **How it computes** | For each universally-required class: is it declared, and does the declaration resolve to something reachable? Report per class, never as a fraction |
| **What is missing** | **Nothing at contract level, and this is the facet with the cleanest fit.** RFC1-8's "membership predicate over the declared inventory" is exactly the shape a facet needs — the contract already refused to make Genome an entity, which is what would have forced a new store |
| **Gap class** | **Specification** |

**The one design constraint this facet imposes.** It must report **per class**,
never as a count. "4 of 6 Genome classes present" is a composite inside a
facet, and it makes *doctrine absent* and *handcrafted-region declaration
absent* interchangeable. They are not.

---

## Facet 3 — Human-understandable

| | |
|---|---|
| **Owning contract** | **RFC-0007** `narrative-contract` |
| **Inputs, by clause** | RFC7-6 (**one primary narrative** — a governed project has at most one); RFC7-9 (granularity, covering, minimality, bounding of source anchors); RFC7-10 (anchor form — machine-readable and typed); RFC7-11 (**broken anchors render Unknown, never silent**); RFC7-11(a) (anchors whose target changed render as *drifted*); RFC7-13 (progressive disclosure and the V0 default path) |
| **How it computes** | Two halves. **Mechanical:** a primary narrative is declared (RFC7-6), and its anchors resolve rather than rendering Unknown or drifted (RFC7-10/11/11(a)). **Judged:** a fresh reader answered the project's comprehension questions, and the answer was recorded as evidence |
| **What is missing** | **A contract gap, and it is real.** No clause defines a *fresh-reader evaluation* as an evidence-producing act. RFC7-13 states the progressive-disclosure obligation; nothing states who tests it, at what tier the result is admitted, or when it expires |
| **Gap class** | **Contract** — and it should be filled at *surface specification*, not now. The reason: the missing piece is an evidence-production rule, and RFC2-25's tier registry is the right home for how such a judgment is admitted. Drafting it here would put an evidence rule in a narrative contract |

**This is the facet most likely to be quietly faked**, because the mechanical
half is easy and the judged half is not. The brief states plainly that its
evidence is a recorded human judgment. Absent that judgment the answer is
`Unknown — no-evaluation-performed`, and a project whose anchors all resolve
is **not** thereby Human-understandable.

---

## Facet 4 — Observable

| | |
|---|---|
| **Owning contracts** | **RFC-0002** `snapshot-and-evaluation-core` for identity and decay; **RFC-0004** for what can be read; **RFC-0005** for whether it may be |
| **Inputs, by clause** | RFC2-1 (the closed rule — a source snapshot identifies what was captured); **RFC2-2 (uncaptured means uninfluential)**; RFC2-3 (evaluation identity — the (source snapshot, as-of instant) pair); **RFC2-4 (degradation-only over an unchanged snapshot)**; RFC2-10 (identity-bearing freshness: `fresh` / `stale` / `broken` / `superseded`); RFC-0004's adapter and observer contracts; RFC5-12/5-14 (consent and egress gates) |
| **How it computes** | At a named evaluation: for each declared repository and each required evidence source, was it readable, and what is its RFC2-10 freshness state? |
| **What is missing** | **Nothing at contract level** |
| **Gap class** | **Specification** |

**RFC2-4 is why this facet cannot be cached.** Over an unchanged snapshot a
later evaluation may only *degrade* an answer. An Observable answer with no
as-of instant is not stale — it is malformed, and the contract already says
so. The facet inherits that property rather than restating it.

---

## Facet 5 — Traceable

| | |
|---|---|
| **Owning contract** | **RFC-0008** `accounting-reconciliation-and-release` |
| **Inputs, by clause** | **RFC8-21 (walk the chain in both directions: warrant → work → run → change → evaluation)**; **RFC8-22 (a broken join renders; it is never silently skipped)**; RFC8-23 (a work item, run, or merged change with no traceable warrant); RFC8-24 (which RFC2-24 reasons this surface most renders); RFC8-25 (small inherited mutations riding a parent warrant) |
| **How it computes** | Over the declared scope, walk RFC8-21's chain in both directions and report, per link class, how many joins resolve and how many render broken under RFC8-22 |
| **What is missing** | **Nothing at contract level. RFC8-21 and RFC8-22 are this facet already**, written for a surface rather than for a project-level answer |
| **Gap class** | **Specification** |

**The trap this facet must not fall into.** Traceable reports coverage of the
**declared** links. A project that declares no links is not 0% traceable; it
is `Unknown — missing-declaration`. RFC8-22's "renders, never silently
skipped" is about *broken* joins — a different fact from *absent* ones, and
rule 5 of the brief exists because these two are the pair most often merged.

---

## Facet 6 — Mission-ready

| | |
|---|---|
| **Owning contracts** | **RFC-0010** (envelope lawfulness) and **RFC-0011** (packet completeness) |
| **Inputs, by clause** | RFC10-7 (what an envelope must bound, and the unstated-is-narrowest rule in both directions); RFC10-9 (the envelope is authorization-bearing and needs verifiable owner-act provenance); RFC10-19 (every permitted effect class declared reversible / compensatable / irreversible — **unclassified is unauthorized**); RFC10-19(a) (sibling disposition declared); RFC10-22 (attention bounds declared). Then RFC11-4 (mandatory context selected deterministically); **RFC11-6 (incomplete is Unknown, and Unknown blocks when policy says so)**; RFC11-11 (packets carry a size estimate) |
| **How it computes** | Could a lawful envelope be formed — every RFC10-7 field either declared or resolving to its narrowest reading without contradiction — **and** could a complete packet be compiled for at least one declared task class under RFC11-4? |
| **What is missing** | Nothing at *clause* level. What is missing is **acceptance**: RFC-0010 and RFC-0011 are candidates, and whether bounded missions are lawful under unamended doctrine is open question **D4** |
| **Gap class** | **Owner act, then specification** |

**Staged, and it says so.** Until act 1 and the D4 ruling, this facet's answer
is `Unknown — governing-contract-unaccepted`. It is present in the set,
queryable, and honest about why it cannot be computed. Removing it until its
authority lands would teach a reader that the question is optional.

**And a dependency worth naming.** RFC11-6's *incomplete is Unknown* means the
packet half of this facet cannot be computed by a compiler that does not
exist. Today a Mission-ready answer would rest on the nine hand-authored
golden selections — which is a fine answer for those nine task classes and no
answer at all for a tenth. See `FINAL-CONTEXT-SELECTION-REPORT.md`.

---

## Facet 7 — Reconciled

| | |
|---|---|
| **Owning contract** | **RFC-0002** `reconciliation-chain` |
| **Inputs, by clause** | **RFC2-17 (reservation of the words — unqualified *reconciliation* means one thing)**; RFC2-18 (the chain: every materialized work item reaching merge enters it); **RFC2-19 (trigger and staging — the loop is human-triggered)**; **RFC2-20 (the closure fallacy, forbidden)**; RFC2-21 (what "no gap at evaluation E" means, over a declared scope); RFC2-22 (fixed point / idempotence). Rendering: RFC8-28 (chain states carried beside work states), RFC8-30 (no aggregate renders a closed item as done absent `reconciled@E`) |
| **How it computes** | Over a **declared scope** at an evaluation: RFC2-21's "no gap at E" predicate, with each item's RFC2-18 chain state carried separately |
| **What is missing** | **Nothing at contract level** |
| **Gap class** | **Specification** — plus a staging fact: RFC8-29 records that V0 does not produce the verdict-bearing chain outcomes, so at V0 this facet renders `merged`, `reconciliation-pending` and `Unknown(reason)` only, honestly |

**RFC2-19 is why this facet is never automatic.** The loop is human-triggered.
A Reconciled answer that appeared without anyone triggering reconciliation
would be exactly the closure fallacy RFC2-20 forbids, arriving through a new
door.

---

## Cross-cutting: how a facet is queried, by anyone

Brief rule 6 — humans and agents get the same answers — is not a new
obligation and is deliberately not restated as one. **RFC-0006 already binds
it**, and a facet is inside its scope the moment it is a claim about a
selectable entity:

| Obligation | Clause |
|---|---|
| Facets are selectable, one way, like every V0-core entity | RFC6-2 |
| Every facet answer names the evaluation it was computed at | **RFC6-15** |
| The filters that produced a scoped answer are part of the answer | RFC6-16 |
| An aggregate discloses what it aggregated | **RFC6-17** |
| Machine endpoints and human renderings carry the same facts | **RFC6-13** |
| Every label a human sees is the label a machine gets | **RFC6-14** |
| The drawer for one selection is one fact set | RFC6-18 |
| Outcomes are not Unknown reasons | **RFC6-6** |

**RFC6-6 is the one to read twice.** It already forbids collapsing
`not-applicable` and `retired` into Unknown — the corpus-level version of the
brief's rule 5. The facets inherit it rather than restating it, which is what
"reuse existing semantics" has to mean in practice.

---

## Summary — what would actually have to be built, and where

| Facet | Contract gap | Specification gap | Blocked on an act |
|---|---|---|---|
| Registered | — | Capability 1 | — |
| Shape present | — | Capability 1 | — |
| Human-understandable | **yes** — no clause defines a fresh-reader evaluation as an evidence-producing act; home is RFC2-25's tier registry, at surface specification | Capability 1 + 3 | — |
| Observable | — | Capability 1 | — |
| Traceable | — | Capability 1 | — |
| Mission-ready | — | Capability 2 | **act 1, and the D4 ruling (P-24)** |
| Reconciled | — | later than Capability 1 | — |

**Six of seven facets need no new clause.** That is the result this document
was written to establish, and it is the argument that the facet model is a
projection of the corpus rather than an addition to it. The seventh names its
gap, names the right home for it, and does not fill it here.

**No facet introduces a record type, a store, or an authority.** Verified by
walking each row's inputs: every one is a claim computed at an evaluation over
records RFC-0001 through RFC-0011 already define.

## Owner decisions this routing depends on

- **Packet 6** — approve seven independent facets and reject a composite.
  Nothing below matters if a badge is wanted instead.
- **P-24 / D4** — Mission-ready's staging.
- **P-21** — the relation model, because Traceable's link walk and
  Mission-ready's packet completeness both consume it.
