# The first specification sequence

> **SUPERSEDED — historical record.** Revision 2 is
> `../round-2026-08d/FIRST-OPENSPEC-SEQUENCE.md`. Three contract gaps this
> file reports (the fixed-path clause, the discoverability finding,
> `constrains` unnamed by RFC11-4) were repaired in candidate bytes at
> round 2026-08d, the five-act gating became six wave acts, and the nine
> fixtures became ten with a task/answer boundary.

> **Candidate plan. Binds nothing, and creates nothing.** No OpenSpec
> changeset exists, no `openspec/` tree exists, and none may be created before
> the owner acts. This file records **what to specify first, in what order, and
> what each one depends on** — so that the sequence is a decision made in the
> open rather than an accident of whoever authors first.
>
> It chooses no language, framework, database, graph store, rendering engine or
> deployment target, and it contains no schema.

## The rule this sequence is built on

Each capability must be **provable on its own**. A capability whose only
evidence is that the next one works has not been verified — it has been
assumed, and that is the pattern doctrine's *scheduled is not satisfied* rule
exists to break.

So the ordering is not "easiest first" and not "most visible first". It is:
**the capability whose absence would make the next one's evidence
uninterpretable goes first.**

## Capability 1 — Project registration and shape visibility

**Why first:** every other capability needs to name a project, and every
statement Syzygy will ever make is scoped to one. Until registration is
specified, nothing else has a subject.

**Observable behaviour to specify:**

| # | Behaviour | Governing candidate clauses |
|---|---|---|
| 1.1 | Parse and validate the project declaration; an invalid declaration is a named failure, never a partial registration | RFC3-1..3 (`.syzygy/**` manifests), RFC1-1 (Project identity) |
| 1.2 | Record consent and repository coverage, including the **boundary** — what is *not* covered is a rendered fact, not silence | RFC1-3 (Consent record), RFC5-3 (admission), RFC6-26 (unconsented renders as policy, never as error) |
| 1.3 | Serve the fixed human entry point at `.syzygy/intent/OVERVIEW.md` | RFC7-6 (primary narrative); **the fixed-path clause does not exist** — see gaps below |
| 1.4 | Answer the seven project-shape facets **independently**, each with its own Unknown reason; **no composite badge** | `PROJECT-SHAPE-FACETS-BRIEF.md`; routed per `PROJECT-SHAPE-FACETS-ROUTING.md` |
| 1.5 | Expose owning authority and Unknown for every answer, identically to human and machine | RFC6-13 (one truth, two consumers), RFC6-14 (label parity), RFC6-15 (evaluation-stamped) |
| 1.6 | Render the root-README discoverability finding as `yes / no / Unknown`, and **propose** the link without writing it | `HUMAN-ENTRY-POINT-BRIEF.md` §4; VIS-6 two-root write boundary |

**Proves:** that a project can be registered and honestly described, and that
`Registered: true` reads as a relationship rather than an endorsement.

**Depends on:** nothing. This is the root of the sequence.

**Known contract gaps blocking full specification:** the fixed-path clause
(smallest home RFC7-6) and the discoverability finding (smallest home RFC3-6).
Both are one-line additions recorded in `HUMAN-ENTRY-POINT-BRIEF.md` §7 and
neither is made. **Capability 1 can be specified without them** — they change
where the rule is homed, not what the behaviour is — but the specification
would cite a clause that does not yet say it.

## Capability 2 — Deterministic Context Packet Generation

**Why second:** it is the capability this whole round has been standing in for.
Nine context selections exist and **every one was made by a human**. Until a
selector produces them, "context is compiled, never accumulated" is a practice,
not a property.

**Observable behaviour to specify:**

| # | Behaviour | Governing candidate clauses |
|---|---|---|
| 2.1 | Classify a task into one of the declared task classes | RFC11-4; `TASK-TO-CONTRACT-INDEX.md` |
| 2.2 | Select mandatory authority deterministically — same task + same corpus revision ⇒ same set | **RFC11-4**; VIS-7 determinism |
| 2.3 | Traverse the declared relations — `depends_on`, and **`constrains` via its clause anchor**, loading the anchored clause rather than the whole contract | RFC11-4 (**does not name `constrains` today** — P-21(c)) |
| 2.4 | Emit an **omission record**: every applicable candidate not selected, named with a reason | **RFC11-6** — incomplete is Unknown and blocks |
| 2.5 | Emit a packet digest over exact bytes | RFC11-5, RFC11-7 (no second truth store) |
| 2.6 | Estimate size, and decompose or refuse when a declared budget is exceeded | RFC11-11; **the threshold `CC-BUDGET-1` is installed nowhere** |
| 2.7 | Reproduce all nine golden fixtures | `CONTEXT-BUDGET-REPORT.md`; `fixtures/` |

**Proves:** that an agent can be given a small, explicit, reproducible set of
governing artifacts with omissions visible — the second half of this round's
governing success condition.

**Depends on Capability 1** for the project scope a packet is compiled within.
It does **not** depend on 3 or 4.

**Honest statement of where this stands:** the nine fixtures are *hand-selected
and labelled as such*. That labelling was one of this round's repairs, and it
is what makes 2.7 a real test rather than a tautology — an implementation that
reproduces nine selections a human made independently is evidence; an
implementation checked against its own output is not.

## Capability 3 — Minimum Polaris comprehension slice

**Why third:** the first capability a *person* uses rather than a machine, and
the first place the fresh-engineer standard is measured on running software
rather than on prose.

**Observable behaviour to specify:**

| # | Behaviour | Governing candidate clauses |
|---|---|---|
| 3.1 | Show the primary narrative — at most one per project | RFC7-6 |
| 3.2 | Show the capability catalog | RFC1-5 (Capability, "the map anchor") |
| 3.3 | Reach the **exact requirement leaf** — the task the governing standard names | RFC1-5 (Requirement reference; authority is `openspec/**`) |
| 3.4 | Show source anchors, and render a broken anchor as broken | RFC7-11 |
| 3.5 | Cold-open walkthrough: a reader with no context reaches a requirement without being told where to look | CC-BAR-3 (comprehensible truth is a merge constraint) |
| 3.6 | Non-visual navigation reaching the same facts | RFC6-13, RFC6-14; RFC6-22 equivalence |
| 3.7 | Show the seven shape facets, still independent, still no badge | Capability 1's facet answers, rendered — **not recomputed** |

**Proves:** the human half of the governing success condition, on software.

**Depends on Capability 1** (facets, authority, Unknown) and, for 3.3, on the
`openspec/**` plane existing. It does **not** depend on Capability 2 —
deliberately, so that a Polaris failure and a compiler failure cannot be
confused for each other.

**3.6 is the row most likely to be deferred and should not be.** RFC6-22's
equivalence obligation is what stops the non-visual path becoming a degraded
second rendering, and a degraded second rendering is a second truth store.

## Capability 4 — Integrated observatory proving slice

**Why last:** it is the only one that can fail in a way the other three cannot
detect, and it must run **on one real, messy project** — not on a fixture.

**The end-to-end sequence to prove:**

```text
register
→ show thin honest narrative
→ map one capability to code and tests
→ show one Unknown region
→ show one real work item
→ show the same capability in coarse Orrery
→ build the context packet for changing it
```

**What each step is actually testing:**

| Step | The failure it is there to catch |
|---|---|
| register | A real project's declaration is not a fixture's |
| **thin honest narrative** | The temptation to render a thin project as adequate. A thin narrative must **look thin** |
| map one capability to code and tests | Whether the capability↔code mapping survives a codebase nobody wrote for it |
| **show one Unknown region** | The single most important step. A messy project has regions with no evidence, and they must render Unknown — **never green, never zero** (VIS-2) |
| show one real work item | Whether the scheduler adapter mirrors rather than mints (RFC1-5: *"mirrored never minted"*) — and whether work renders **without** being read as proof |
| the same capability in coarse Orrery | RFC6-22 equivalence across a genuinely different rendering |
| build the context packet for changing it | Capability 2, on a corpus that was not designed for it |

**Depends on Capabilities 1, 2 and 3 — all three.** It is the only capability
that does, and that is why it is last rather than why it is hard.

**One dependency it also carries, and it is an owner decision:** the sequence
shows a work item and builds a packet, but **not** a Mission. Whether a Mission
is even a selectable entity is **open** — `Mission` has zero occurrences in
RFC-0001, while RFC10-4 declares it a first-class identified entity minted
under RFC-0001's rules. See `UNIVERSAL-VISIBILITY-REVIEW.md` §3 and owner item
**P-28**. Until that is ruled, Capability 4 proves a Mission-free path.

## Dependency graph

```text
Capability 1  (registration + shape visibility)
    │
    ├──────────────► Capability 2  (deterministic context packets)
    │                     │
    ├──────────────► Capability 3  (Polaris comprehension slice)
    │                     │
    └─────────────────────┴──────► Capability 4  (integrated proving slice)
```

- **2 and 3 are siblings, not a chain.** Either may be specified and proven
  without the other. Serialising them would make a compiler defect and a
  presentation defect indistinguishable.
- **4 requires all three**, and requires them *proven*, not merely specified.
  A proving slice run against unproven components proves the slice, not the
  components.

## What must be settled before Capability 1 is authored

| Blocker | Kind | Where |
|---|---|---|
| The five owner acceptance acts | Owner acts | `FINAL-OWNER-ACCEPTANCE-RECORD.md` — until act 1, no contract is citable as binding, and a specification citing candidate clauses cites nothing |
| **OpenSpec version** | Owner decision | Packet 8. Choosing it after the first changeset means migrating the first changeset |
| **License** | Owner / legal | Packet 9. Not an agent's call |
| Project-shape facets approved | Owner decision | Packet 6 — Capability 1 renders them |
| Fixed-path and discoverability clause homes | Contract gap | Recorded, not made |

## What must be settled before Capability 2 is authored

| Blocker | Kind | Where |
|---|---|---|
| **RFC11-4 does not name `constrains`** | Contract gap | **P-21(c)**. A selector built to the clause as written ignores the relation this round just built |
| **`CC-BUDGET-1` is installed nowhere** | Craft gap | The decomposition trigger is a *proposed* 20,000 tokens with no owning rule. Four fixtures already exceed it |
| Relation model adopted | Owner decision | Packet 1 (P-21) |

## What this file deliberately does not contain

- **No changeset.** None is created, and creating one before act 1 would be
  the boundary violation this whole lifecycle stage exists to hold.
- **No schema, no endpoint shape, no data model.** Those are specification
  content and belong in the changesets this file is only sequencing.
- **No estimates.** How long any of this takes is `[Unknown]`, and a number
  here would be the volatile-value defect this round spent a workstream
  removing.
- **No claim that the sequence is right.** `[Inferred]`. It is one defensible
  ordering with its dependency reasoning stated so the owner can disagree with
  the reasoning rather than only with the conclusion.
