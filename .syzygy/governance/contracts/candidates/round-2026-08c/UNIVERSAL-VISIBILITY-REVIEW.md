# The universal visibility contract — "Why am I seeing this?"

> **Candidate round record. Binds nothing.** This is Workstream I's output: a
> read of the shared query and evidence-drawer contract against one question,
> across six entity kinds and eleven required facts. Every gap it finds is
> routed, and none is repaired here.

## The question

For any answer any surface or endpoint gives, a reader must be able to ask:

> **Why am I seeing this?**

and get a complete answer from **one shared semantic source** — never
reassembled per view, and never duplicated into each view's own store.
RFC6-18's *one drawer, one fact set* and RFC6-13's *one truth, two consumers*
already carry that architecture. What this review tests is whether the fact set
those clauses mandate actually **contains** the eleven facts the answer needs,
for each of the six kinds of thing a reader can be looking at.

## 1. The eleven facts against RFC6-19's seven content classes

RFC6-19 enumerates seven drawer content classes. Mapping the eleven required
facts onto them:

| # | Required fact | Where it lives today | Held? |
|---|---|---|---|
| 1 | **owning authority** | RFC6-19.4 Provenance — *"the typed authority that answered each question"* | **Yes** |
| 2 | **source revision** | RFC6-19.3 Evidence — *"evidence–revision binding visible"* | **Partial.** The *evidence's* revision binding is required. The **selection's own governing revision** is not a named drawer fact |
| 3 | **state plane, where applicable** | — | **No.** `state plane` has **zero occurrences in RFC-0006** |
| 4 | **epistemic label** | RFC6-19.2 Epistemic state — *"label + tier + Unknown reason (verbatim RFC 0002 vocabulary)"* | **Yes** |
| 5 | **evidence tier** | RFC6-19.2, same clause; RFC6-17 requires all six of RFC2-25's tiers in aggregates | **Yes** |
| 6 | **evaluation identity and freshness** | RFC6-19.4 (producing evaluation: snapshot + as-of instant); RFC6-19.2 (freshness state); **RFC6-15** — *"An answer that cannot name its evaluation is not an answer"* | **Yes, and this is the strongest of the eleven** |
| 7 | **Unknown reason** | RFC6-19.2, verbatim vocabulary; RFC6-6 separates outcomes from Unknown reasons | **Yes** |
| 8 | **coverage / consent boundary** | RFC6-19.7 Policy visibility — exclusions with counts and consent state; RFC6-26 *unconsented renders as policy, never as error*; RFC6-27 *excluded is a rendered state* | **Yes** |
| 9 | **active challenge** | RFC6-19.6, with RFC2-13 lifecycle state travelling unflattened — `submitted` belongs to the fact set exactly as `admitted` does | **Yes** |
| 10 | **active contradiction** | RFC6-19.6 — *"contradictions pending adjudication"* | **Yes** |
| 11 | **relevant work and reconciliation state** | — | **No.** `reconcil` has **zero occurrences in RFC-0006**; so do `work item` and `Work item` |

**Method and denominator:** the whole file, swept with Python `re` over
whole-file text this session (verification rule 1 — `grep` here is ugrep and
bracket classes silently match nothing). Eleven facts examined, eleven
reported. Eight held, one partial, two absent.

**[Observed]** for every row: each is either a quotation from a clause or a
zero-hit sweep result.

## 2. The three gaps, in order of severity

### Gap A · Work and reconciliation state are not drawer facts — **the largest**

`reconcil` appears **nowhere** in the drawer contract, and neither does the
work item.

The reader who most needs this fact is the one this whole project is for:
someone looking at a capability rendered `Unknown` who wants to know **whether
anything is being done about it**. Today the drawer tells them what is claimed,
what evidence exists, who answered, and what is challenged — and says nothing
about whether work is in flight.

It is *reachable*: the `motivates` edge in RFC1-25's typed-relation table runs
Requirement reference / Decision / Policy → Work item, so a traversal finds it. But **reachable is not the same as in the
fact set**, and RFC6-18 is explicit that a fact a surface renders which the
fact set lacks is a kernel defect. A surface that shows "3 work items address
this gap" while the drawer does not carry that fact is exactly the defect
RFC6-18 names — and every surface will want to show it.

**This is also the one gap where the omission is arguably principled**, and the
principle cuts the other way. RFC1-5's plane table says execution **"may never
satisfy a desired-state claim — work is never proof"**, and a drawer that
displays work beside status invites precisely that confusion. The resolution is
not to omit the fact; it is to carry it **with its plane label attached**, so
that the reader sees work *and* sees that work is not evidence. Omitting it
does not protect the reader — it just makes each surface fetch it separately,
which is a second truth store with extra steps.

**Routing:** a drawer content class 8, homed in **RFC6-19**. Normative
addition to act 1's digest subject; **not made here**.

### Gap B · The state plane is not a drawer fact

RFC-0001 builds the entire model on state planes — governance/desired,
temporal/epistemic, proposal/work, structure — and the plane is what makes
*"work is never proof"* legible rather than a slogan. The drawer never names
it.

RFC6-19.1 carries lifecycle state, which is a different thing: `retired` is a
lifecycle state, `Execution` is a plane. A reader who cannot see which plane a
fact came from cannot apply the one rule that stops the most common category
error in the system.

**Routing:** **RFC6-19.1**, one phrase. Not made here.

### Gap C · The selection's own governing revision is partial

Evidence carries its revision binding, and RFC6-10's two URL temporalities pin
an evaluation. What is not a named drawer fact is **which revision of the
governing normative artifact the claim was evaluated against** — the thing
RFC2-18's reconciliation evaluation and the materialization record's *pinned
warranted intent revision* both turn on.

**[Inferred]** that this is derivable from the provenance class in practice,
and **[Unknown]** whether any implementer would derive it without being told
to. That gap between *derivable* and *required* is where second truth stores
come from.

**Routing:** **RFC6-19.4**. Not made here.

## 3. The six entity kinds — and the one that has no drawer at all

RFC6-2 makes *"every V0-core entity (RFC1-5)"* selectable, and RFC6-18 gives
every selection one fact set. So the question of whether a drawer exists for an
entity kind reduces to whether RFC1-5 lists it.

| Entity kind | In RFC1-5's closed V0-core vocabulary? | Drawer reachable? |
|---|---|---|
| **Project** | Yes — *Governance / desired* | Yes |
| **Capability** | Yes — *"§3.4; the map anchor"* | Yes |
| **Requirement** | Yes — *Requirement reference · Scenario reference*, kernel holds references; content authority is `openspec/**` | Yes, with the authority split visible |
| **Work item** | Yes — *"Scheduler-issued, **mirrored never minted**"* | Yes |
| **Map entity** | Yes — Topology entry, Declared region, Code element; districts/scenes/lenses via RFC1-7's **map** profile | Yes |
| **Mission** | **No** | **No** |

### The Mission finding — **[Observed], and it is the sharpest thing in this review**

**`Mission` has zero occurrences in RFC-0001.** Verified by Python `re` sweep
over the whole file this session.

Yet **RFC10-4** reads:

> A **Mission** is a first-class identified entity (minted under RFC 0001's
> identity rules) …

and **RFC10-12** says the same of the **Attention Item**.

Three clauses make this a real seam and not a wording quibble:

1. **RFC1-5** closes the vocabulary: *"The **V0-core entity vocabulary is
   closed** at the following classes. An entity not listed here enters the
   graph only through an extension profile (RFC1-7) or an amendment to this
   RFC."* Neither Mission nor Attention Item is in the table.
2. **RFC1-7** enumerates five extension profiles — inference, presentation,
   map, portfolio, annotation/dismissal. **There is no mission profile**, and
   RFC-0010 names none.
3. RFC1-7 closes with *"Profile contents are defined by RFCs 0002–0009"* — a
   range that **excludes RFC-0010**.

So RFC10-4 mints an entity under identity rules that, read literally, do not
admit it. **The consequence for this workstream is direct: RFC6-2 does not make
a Mission selectable, RFC6-18 gives it no fact set, and none of the eleven
facts is contractually available for a Mission at all** — including, sharply,
the Unknown reason and the consent boundary of the one entity class that can
spend budget and touch the world.

**This is not a Mission-safety defect** — RFC-0010's envelope clauses stand on
their own, and RD-1b tests them independently. It is an **identity seam**: two
contracts that each make sense alone and do not compose.

**Three ways to close it, and choosing is not an agent's call:**

| Option | What it costs |
|---|---|
| **(a)** Amend RFC1-5 to add Mission and Attention Item to the closed V0-core vocabulary | Widens V0-core by two entity classes; RFC1-5's closure is reopened by amendment, which RFC1-6 says is the only lawful route |
| **(b)** Add a **mission** extension profile to RFC1-7 and widen its "RFCs 0002–0009" range to 0010 | Keeps V0-core narrow; makes Mission per-project-loadable, which matches P-23's V0/V1 staging — a project not running Missions carries no Mission vocabulary |
| **(c)** Amend RFC10-4 to stop claiming RFC-0001 identity minting | Cheapest edit, worst outcome: a first-class entity outside the identity system is exactly the ungoverned-identity failure RFC1-9 exists to prevent |

**Recommendation (b)**, `[Inferred]`, on the grounds that it is the only option
that composes with P-23's staged Mission placement. **Not applied.** All three
are normative edits to act 1's digest subject in the pass that froze it for
review, and this one additionally interacts with the D3 doctrine amendment.

**New owner item — P-28.**

## 4. What the contract already gets right

Recorded because a review that lists only gaps misrepresents the artifact.

- **RFC6-15's absolutism.** *"An answer that cannot name its evaluation is not
  an answer."* That is the "why am I seeing this" question answered at the
  envelope level, without an escape hatch.
- **RFC6-13 and RFC6-14 make the machine consumer first-class.** Label parity
  means an agent and a human get the same epistemic state. Most systems bolt an
  API onto a UI and let it flatten Unknown for convenience; CC-DEP-5 names that
  exact failure and RFC6-13 forecloses it.
- **RFC6-17 refuses the honest-looking aggregate.** *"Observed ×30" is honest
  only when the reader can also see that all 30 are `reduced-fidelity` and 12
  are stale.* This is the single clause that most directly serves the question
  this workstream asks.
- **RFC6-19.6 carries `submitted` challenges, not just `admitted` ones.** The
  reader sees a challenge that suspends nothing. That is a fact most systems
  would filter as noise, and it is the difference between "nobody has objected"
  and "somebody has objected and it has not been adjudicated."

## 5. "Why am I seeing this *item*?" — an honest limitation

RFC6-16 makes filters part of the answer's envelope, and RFC6-17 makes
aggregates expand to their members. Between them, a reader can determine why a
**set** looks the way it does.

**No clause requires a per-item inclusion reason.** For a filtered list, the
reason is derivable — the item's own facts plus the declared filters. For a
*ranked*, *recommended*, or *inferred* list, it is not, and RFC-0006 does not
distinguish those cases.

**[Inferred]** that this becomes a defect the first time any surface orders
results by anything other than a declared, disclosed key. **[Unknown]** whether
it is a contract gap or an OpenSpec obligation. Recorded, not routed — routing
it would require deciding which, and the honest answer is that this review
cannot.

## 6. Routing summary

| Missing observable behaviour | Route |
|---|---|
| Drawer carries work + reconciliation state, plane-labelled | **RFC6-19** (contract gap) → then **OpenSpec Capability 1** for the rendered behaviour |
| Drawer carries the state plane | **RFC6-19.1** (contract gap) |
| Drawer carries the selection's governing revision | **RFC6-19.4** (contract gap) |
| A Mission is a selectable entity with a fact set | **P-28** — owner decision on RFC1-5 / RFC1-7 / RFC10-4; then **OpenSpec Capability 4** |
| Per-item inclusion reason for non-declarative ordering | Recorded; classification **[Unknown]** |
| The eleven facts rendered identically to human and machine | **OpenSpec Capability 1** — RFC6-13/6-14 bind the parity; the observable endpoint behaviour is specification work |

**No fact is duplicated into a view by anything proposed here.** Every routed
addition lands in RFC6-19's single fact set, which is the clause that exists to
prevent exactly that.
