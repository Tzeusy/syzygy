# Owner decision packets — final pre-specification closure

> **Decides nothing.** Every packet below states a question an agent may not
> lawfully settle (VIS-4), the authority that governs it today, the options
> with their consequences, a recommendation the owner is free to reject, the
> earliest gate that forces the answer, and whether work can proceed without
> it.
>
> A recommendation here is an agent's `[Inferred]` reading. Where a
> recommendation and the owner's judgment differ, the owner's judgment is the
> only one with authority.

## Reading order

Packets **1, 4, 6 and 8** gate work that cannot start without them. Packets
**2, 3, 5, 7 and 9** can be deferred past the acceptance acts, at a stated
cost. Nothing here is ordered by importance.

---

## Packet 1 — The contract relation model (P-21)

**Question.** Adopt the three-relation model — `depends_on`, `constrains`,
`cites` — as the corpus's contract-relation vocabulary, or choose an
alternative?

**Current authority.** None. `depends_on` is authored in candidate front
matter; `constrains` was introduced this round and is declared on two modules;
`cites` is fully derived. **RFC11-4 enumerates the deterministic selection
inputs and names `depends_on`/`provides_to` and clause-level metadata — it does
not name `constrains`.** A conformant compiler built to the clause as written
would not read the new relation at all.

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | **Adopt all three**, and amend RFC11-4 to name `constrains` as a selection input with the clause-anchor rule (*load the anchored clause, not the contract*) | The relation becomes real. Costs one normative edit to act 1's digest subject — so either it lands **before** act 1 (re-digesting the manifest) or in an amendment **after** |
| **(b)** | **Adopt `depends_on` and `cites` only**; drop `constrains` | Simpler. The two clause-borne restrictions (RFC5-3 over RFC-0006; RFC7-3 over RFC-0001/0002/0004) go back to being enforced by nothing, which is the state RC-4 first flagged as P-21(a) |
| **(c)** | **Adopt all three but leave RFC11-4 unamended** | The current state. The relation is declared, projected and checked, and no specified component reads it. **This is the option that looks like a decision and is not one** |

**Sub-questions carried inside this packet:**

- **(b) Citation-without-declaration.** Eleven non-README `depends_on` edges
  carry zero clause evidence, three of them RFC-0011's. Is any a genuine missed
  dependency? Review RD-4 also disclosed that the earlier citation test was
  **scoped to 20 edges and the scoping was undisclosed**.
- **(c) `RFC 0008 §5` cited as authority** by RFC9-32 — a navigational section,
  not a clause.
- **The process finding (RD-4 F-17).** One arm of this pending question — the
  `constrains` relation — **was installed into candidate front matter while the
  question was still open**. That is how a pending decision becomes a fait
  accompli, and the owner should know it happened before ruling.

**Recommendation.** **(a)**, `[Inferred]`, landing the RFC11-4 amendment
*after* act 1 rather than before, so the manifest the owner is being asked to
accept does not move again.

**Earliest required gate.** Before **OpenSpec Capability 2** is authored. Not
before act 1.

**Can work proceed without it?** Yes — Capability 1 and Capability 3 do not
touch it. Capability 2 cannot be specified without it.

---

## Packet 2 — Registry authority home (P-22)

**Question.** RFC9-8(a) places an owner-gated, snapshot-input registry **inside
the workspace manifest**. RFC3-10/11/21 close the workspace manifest as
**personal presentation state** — a VIS-6(a) consequence. Which plane does the
registry belong to?

**Current authority.** Both clauses are candidates inside act 1's digest
subject. **The corpus contains both the error and its remedy:** RFC10-15
explicitly rejects the workspace placement and builds the correct alternative.

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | Registry moves to the **governance plane**; RFC9-8(a) amended | Consistent with RFC3-10/11/21 and RFC10-15. One normative edit |
| **(b)** | Workspace manifest gains an authority-bearing partition; RFC3-10/11/21 amended | Wider blast radius — it reopens what "personal state" means, which VIS-6(a) settles |
| **(c)** | Rule that the two clauses are compatible and record why | Cheapest. `[Inferred]` that it is not available: RFC3-21 closes the manifest, and a closed thing with an exception is not closed |

**Recommendation.** **(a)**, `[Inferred]`. It is the reading the corpus already
contains, written by the later clause, against the earlier one.

**Warning about how this is ruled.** The register already records this: rule
it, do not resolve it by *"a silent edit to whichever clause is younger."*

**Earliest required gate.** Before act 1, **or** as a recorded knowing
deferral inside act 1's acceptance.

**Can work proceed without it?** Yes, with the contradiction carried openly.

---

## Packet 3 — Mission stage placement (P-23)

**Question.** Which of RFC-0010's correction-plane clauses must ship at V0, and
which may wait for V1?

**Current authority.** RFC-0010 is a candidate. Review RC-7 recommended holding
the full correction plane for V1 while capping V0's autonomy ceiling at
`propose-only`.

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | **V0 = Mission records, approval ceremony, read-only rendering, `propose-only` proof. V1 = effect-bearing Missions, the general correction plane, portfolio allocation** | Smallest first slice. A V0 that can only propose does not yet need reversal, adjudication or recovery machinery — the prevention plane suffices |
| **(b)** | Ship the correction plane with V0 | Larger first slice; nothing is deferred |

**The combination that is ruled out under either option:** a V0 that **can
apply effects** without RFC10-19 (reversibility and recovery) and RFC10-20
(stop guarantees). The ceiling and the plane move together.

**Recommendation.** **(a)** — the charter's own recommended staging, and the
reviewer's.

**Earliest required gate.** Before **OpenSpec Capability 4** is authored.

**Can work proceed without it?** Yes. Capabilities 1–3 are Mission-free.

---

## Packet 4 — D4, and whether D3 may be adopted as written (P-24)

**Question.** Does the D3 bounded-mission amendment lawfully place bounded
Missions inside VIS-4's existing mechanism, or does it require accepted
adjudication machinery first?

**Current authority.** VIS-4 (adopted). The D3 packet is rev1 and unadopted.
Review RC-7 finding F10 holds that the packet's `vision.md` insertion places a
bounded Mission inside VIS-4's bounds **by stipulation — inside the one
sentence whose second half exists to foreclose that move.** So **adopting D3 as
written also silently settles open question D4.**

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | **Rule D4 first**, then adopt whichever D3 text the ruling implies | The only option under which D4 is decided knowingly. The packet carries the reviewer's alternative text, which states the reason rather than assuming it |
| **(b)** | Adopt D3 as written | Settles D4 by side effect, in a sentence not written to settle it |
| **(c)** | Decline D3 | Bounded Missions stay outside doctrine; RFC-0010's terms have no adopted definition |

**If D4 is ruled the other way** — that adjudication machinery must be accepted
first — then **no `vision.md` insertion is lawful without an accepted
adjudication RFC, and act 1 becomes a *requirement* before act 5** rather than
the recommendation it currently is.

**Also inside this packet:** the `architecture.md` floor as drafted **omits any
maximum autonomy level**, which moves *"how autonomous may a Mission be"*
permanently out of doctrine. That is a separate ruling and it is easy to miss.

**Recommendation.** **(a)**. Not because of the outcome, but because (b)
decides a doctrine question in a place nobody would look for it.

**Earliest required gate.** Before **act 5**.

**Can work proceed without it?** Yes — act 5 is optional and Capabilities 1–3
do not depend on it.

---

## Packet 5 — Public vocabulary

**Question.** Approve the small-core / advanced split, the eleven core terms,
and the three unresolved vocabulary items below?

**Current authority.** `TERM-REGISTRY.md` is a **candidate**. Doctrine's
glossary (`governance/doctrine/README.md`) is adopted and governing.

**What is being approved.** Core reduced to **eleven** terms, each leading with
the plain question it answers; `Claim` demoted to advanced; **`Unknown`
promoted to its own entry T-31 with an *adopted* owning authority** (VIS-2,
`trust-and-evidence.md`, SDR-6); one admission rule with five conditions; a
first-use rule (*"the Observed plane"* / *"an Observed claim"*, never bare
*Observed*) that a fresh reader **tested successfully without being told it
existed**.

**Three items this packet must dispose, and the first is the sharp one:**

**(a) `Unknown` (T-31) vs `Gap` (T-20) classify the same example oppositely.**
Review RD-3 finding **D-1**, and the one adjacent pair a fresh reader could not
separate. T-20's example treats *"an adopted requirement with no verifying
evidence"* as a **Gap**; T-31 says a gap is something *known* to be absent and
that not knowing whether it is absent is an **Unknown**. This is the
missing-declaration-versus-failed-evidence distinction the entire facet model
turns on. **It is a question about what the corpus means, not about wording**,
and resolving it inside the pass that wrote T-31 would repeat a loop this round
has already been caught in twice.

**(b) The default path is not bounded in practice.** It is declared bounded to
eleven terms and carries **fifteen** Syzygy-specific terms with no entry and no
inline definition. Two are worse than the rest: **`workspace` has zero
occurrences in the entire adopted doctrine tree**, and **`experience` heads a
section of `README.md` and is defined nowhere**. These are not advanced terms
used early — they are words with no owner. Separately, **`plane` carries five
or six senses**, two of them on the default path, and it is the word T-06 is
built on.

**(c) May `OVERVIEW.md` be edited before act 4 fires?** Nine of the fifteen
undefined terms live there, as do RD-3's findings **A.5** (`Reconciliation`
used on the default path in the sense T-26 explicitly reserves against — and
the corpus has **no term at all** for *"the difference between desired and
observed"*, which is what the narrative is reaching for) and **A-6**
(`README.md` and `OVERVIEW.md` contradict each other on whether Mission Control
is a surface). Nothing was edited, because editing an artifact whose digest an
unperformed act binds is a worse defect than the one being corrected. **RD-3
makes the counter-argument better than this round can:**

> Findings A.5, A-6 and G-1 are repairs to a *pending* offering, not
> corrections to a bound artifact — which, if the act has not fired, is the
> cheapest moment they will ever be available.

**Recommendation.** Approve the core/advanced split and the eleven-term core.
For **(a)**, rule the distinction explicitly rather than rewording either
entry. For **(c)**, **authorize the edits and re-digest before act 4** —
`[Inferred]`, on RD-3's reasoning, and noting that it costs one manifest
regeneration and buys the fix at its cheapest moment.

**Earliest required gate.** **(c)** before act 4. **(a)** and **(b)** before
OpenSpec Capability 1, which renders facets whose meaning depends on the
`Unknown`/`Gap` line.

**Can work proceed without it?** Partly. (a) blocks nothing today and will
block the first facet specification.

---

## Packet 6 — Project-shape facets

**Question.** Approve seven independent facets, each with its own Unknown
reason, and **reject a composite compliance badge**?

**Current authority.** None — `PROJECT-SHAPE-FACETS-BRIEF.md` is a candidate
brief. VIS-1 (no confident state over Unknown) and VIS-2 (no evidence yields
Unknown) are adopted and govern the shape of any answer.

**What approval commits to.**

- Seven facets that **never roll up**. No score, no percentage, no traffic
  light, no "compliance level".
- **Registration is not certification**, stated in those words, human-visible
  and machine-queryable through the same API.
- A precondition relationship between facets renders as an Unknown **reason**,
  never as a propagated value.
- The root-README discoverability finding is a **detail of the Registered
  facet**, not an eighth facet, and it is **rendered, never written** — Syzygy
  may not edit a project's root README, and a carve-out for discoverability is
  how a write boundary stops being one.

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | Approve the seven independent facets; reject any composite | The honest rendering. Costs: seven answers is more than a reader wants, and every consumer will ask for a summary |
| **(b)** | Approve the facets and permit a composite for "at-a-glance" use | The composite becomes the number people quote, and the facets become its footnotes. `[Inferred]` that this is the failure mode the whole design exists to prevent |
| **(c)** | Fewer facets | Reduces reader load. Requires naming which two facts may be merged, and the brief's claim is that none may |

**Recommendation.** **(a)**, unambiguously.

**Earliest required gate.** Before **OpenSpec Capability 1** — it renders them.

**Can work proceed without it?** No. Capability 1 is the first capability and
the facets are 1.4.

---

## Packet 7 — Knowledge-hygiene policy (P-12)

**Question.** Which version of the knowledge-hygiene craft policy gets the
`CONFIRM CRAFT AMENDMENT` act — the original **22 rules** (CC-KNOW-1…18,
CC-BUDGET-1…4, ~3,500 words) or the **compaction to ten**?

**Current authority.** Neither is installed. Both are candidates.

**What the compaction does.** Drops no obligation, renumbers no identifier,
retires twelve into named survivors, carries the migration map, and **adds
exactly one obligation — listed rather than folded in silently.**

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | The **compact ten** | Shorter, and every deletion is accounted for. The one added obligation is disclosed |
| **(b)** | The original 22 | No migration map to trust |

**Also open:** the six sub-questions at the long version's foot.

**One consequence worth naming.** **`CC-BUDGET-1` — the context-budget
threshold — is installed nowhere under either version until this act fires.**
Four of the nine golden fixtures already exceed the *proposed* 20,000-token
decomposition trigger, and their budget dispositions are recorded against a
threshold no rule owns.

**Recommendation.** **(a)**, the compact version, after independent review — as
the charter itself prefers.

**Earliest required gate.** Before **OpenSpec Capability 2**, which needs
`CC-BUDGET-1` to have an owner.

**Can work proceed without it?** Yes, with the budget dispositions carried as
proposals rather than compliance.

---

## Packet 8 — OpenSpec version

**Question.** Which version of OpenSpec does this project target?

**Current authority.** None. No `openspec/` tree exists and no version is
named anywhere in the corpus.

**Consequence of not choosing.** Choosing after the first changeset means
**migrating the first changeset** — and the first changeset is the one every
later author copies.

**Options.** Not enumerable by an agent: the answer depends on what versions
exist and what the owner is willing to depend on. This packet asks the
question; it does not pre-answer it.

**Recommendation.** None. `[Unknown]` — an agent that recommended a version
here would be choosing a dependency, which this lifecycle stage forbids.

**Earliest required gate.** Before the **first OpenSpec changeset**.

**Can work proceed without it?** No. It is the first thing the first changeset
needs.

---

## Packet 9 — License

**Question.** Which license?

**Current authority.** None. `LICENSE-DECISION-PACKET.md` holds four candidates
and three `[Unknown]`s, **including copyleft reach into governed
repositories** — which for a tool that writes into other people's projects is
not a routine question.

**Recommendation.** **None, and deliberately.** This wants qualified legal
review and is not to be chosen autonomously. Stating a preference here would be
the thing this packet exists to prevent.

**Earliest required gate.** Before any public release. `[Unknown]` whether it
gates the first changeset — that depends on whether the repository is public at
that point.

**Can work proceed without it?** Yes, and it should not be allowed to drift far
past act 1.

---

## Packet 10 — Mission as a graph entity (P-28, new this round)

**Question.** RFC10-4 declares a **Mission** *"a first-class identified entity
(minted under RFC 0001's identity rules)"*, and RFC10-12 says the same of the
**Attention Item**. **`Mission` has zero occurrences in RFC-0001.** How does a
Mission enter the graph?

**Current authority.** RFC1-5 closes the V0-core entity vocabulary and contains
neither: *"An entity not listed here enters the graph only through an extension
profile (RFC1-7) or an amendment to this RFC."* RFC1-7 enumerates five profiles
— inference, presentation, map, portfolio, annotation/dismissal — none of them
mission-shaped, and closes with *"Profile contents are defined by RFCs
0002–0009"*, a range that **excludes RFC-0010**.

**Why it matters beyond tidiness.** RFC6-2 makes *every V0-core entity*
selectable and RFC6-18 gives every selection one fact set. A Mission is neither,
so **none of the eleven universal-visibility facts is contractually available
for a Mission** — including its Unknown reason and its consent boundary, for
the one entity class that can spend budget and touch the world.

**Options.**

| | Option | Consequence |
|---|---|---|
| **(a)** | Amend **RFC1-5** to add Mission and Attention Item to V0-core | Widens V0-core by two classes. RFC1-6 says reopening RFC1-5's closure by amendment is the only lawful route, so this is in-bounds |
| **(b)** | Add a **mission** extension profile to **RFC1-7** and widen its "RFCs 0002–0009" range to 0010 | Keeps V0-core narrow and makes Mission per-project-loadable — which composes with Packet 3's staging: a project not running Missions carries no Mission vocabulary |
| **(c)** | Amend **RFC10-4** to stop claiming RFC-0001 identity minting | Cheapest edit, worst outcome: a first-class entity outside the identity system is exactly the ungoverned-identity failure RFC1-9 exists to prevent |

**Recommendation.** **(b)**, `[Inferred]` — the only option that composes with
Packet 3.

**This is not a Mission-safety defect.** RFC-0010's envelope clauses stand on
their own. It is an identity seam: two contracts that each make sense alone and
do not compose.

**Earliest required gate.** Before **OpenSpec Capability 4**. All three options
are normative edits to act 1's digest subject, and **(b)** additionally
interacts with the D3 amendment in Packet 4.

**Can work proceed without it?** Yes — Capabilities 1–3 prove a Mission-free
path.

---

## What is *not* in these packets

Deliberately, so their absence is not mistaken for oversight:

- **No packet asks the owner to accept an artifact.** The five acceptance acts
  live in `FINAL-OWNER-ACCEPTANCE-RECORD.md` with their exact phrases and
  digests, and this file restates no digest.
- **No packet proposes a language, framework, database or platform.**
- **No packet asks the owner to ratify a repair.** Repairs made this round are
  recorded in their closure reports with the review verdicts that prompted
  them, uncopied and unsoftened.
