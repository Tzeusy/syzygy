# Capability 1 — the owner decision packet

> # SUPERSEDED — do not route an owner here
>
> **Superseded 2026-08-13 by
> [`../round-2026-08g/CAPABILITY-1-OWNER-DECISION-INDEX.md`](../round-2026-08g/CAPABILITY-1-OWNER-DECISION-INDEX.md).**
> Review **RD-52** returned `REVISE` on this page, and its blocking finding
> f1 was that **the one-sitting claim is false by this page's own contents**.
> The replacement is an *index* that separates the decisions that can be made
> now from the ones that cannot yet, with the unblocking action named for
> each — which the disposition register recorded as "a rewrite, not an edit."
>
> RD-52 f3, also blocking, found the exclusion list omitting five open queue
> entries, three of them unperformed acts. **That reconciliation was never
> completed on this page** and will not be: the queue
> (`../../../decisions/PENDING-OWNER-DECISIONS.md`) owns the open set, and the
> index routes to it rather than restating it.
>
> Kept for the record, off every reading path. Nothing below is current, and
> its counts were correct only when written.

> **This file decides nothing.** It collects the rulings that stand between
> two confirmed contract waves and a first specification, in the order they
> must be taken, so they can be settled in one sitting. Each row links the
> packet that owns the question; none is reproduced here, and where a
> linked packet and this page disagree, the packet wins. The queue that
> owns the entries is `../../../decisions/PENDING-OWNER-DECISIONS.md`.
>
> No recommendation here is a decision, and no `[Inferred]` label is
> evidence. VIS-4: nothing in this repository performs an owner act.

**Launch target:** Capability 1 — Project registration and honest shape
visibility. **Contract prerequisite:** Waves A + B only. Waves C1/C2/D1/D2
are deferred and appear nowhere below.

---

## The dependency order, and why it is this order

```text
P-33  ─┬─→ Wave A act ──→ Wave B act ──┐
       │                               │
P-31  ─┤ (ratified AT the Wave A act)   │
P-37  ─┘ (cheapest before it)           ├──→ formal launch administration ──→ owner launch decision ──→ author Capability 1
                                        │
P-36, P-38, P-39, P-40, P-41, P-42, P-35, P-34 ─────────┘
```

Only three rows are ordered by *necessity*: **P-33 before the Wave A act**
(the act would freeze the install ceremony it questions), **P-31 and P-37 at
or before that act** (their arms live in Wave A bytes), and **P-34 before the
formal administration** (the administration is run under the policy P-34
approves). Everything else is ordered by cost, not by logic — each is
cheaper before a re-offer than after one.

**Corrected 2026-08-11 by review RD-49.** This page opened with "there is
no arm of P-33 that preserves the current Wave A confirmation". That was
false. The act's argument is the wave manifest's digest — nineteen module
rows — and the install ceremony lives in the acceptance record, which is in
no manifest. Arm **(1g)**, which RD-49 added, changes only the ceremony and
therefore retires **no** confirmation.

What is true: `[Inferred]` **every arm drafted before RD-49** moves at least
one accepted byte, so under (1a)–(1f) the Wave A exact-package gate re-runs
on a regenerated argument — which is why, if one of those is ruled, P-31 and
P-37 are cheaper batched into the same regeneration. Under (1g) there is no
regeneration to batch into, and that trade is the owner's to weigh.

---

## 1. P-33 — Wave A install shape ★ the only obstacle to offering Wave A

| | |
|---|---|
| **Question** | May the accepted-contract home hold the four non-contract companions the install copies into it, and if not, where do they go? Second question: may a 39-row package manifest install at an act that accepts 19 modules? |
| **Current authority** | RFC3-15's `contracts/` row — the home holds accepted contract content **exclusively** |
| **Options** | (1a) outside `governance/` · (1b) widen the cell · (1c) drop the copies · (1d) mint `contracts-companion/` · **(1e) typed closed enumeration** · (1f) install-time rewriting *(rejected in the packet, and why)* |
| **Recommendation** | `[Inferred]` **(1e)** — one module moves instead of thirty; Wave B's confirmation survives; every reference resolves untouched |
| **Consequence** | 19 of 19 Wave A and 11 of 11 Wave B modules link into `history/` — **68 references**. Any arm that relocates the companions rewrites all of them. (1d), the previous recommendation, is the **most expensive** arm and was recommended before that was measured. |
| **Digest invalidated** | (1b)/(1e): Wave A only — RD-31b's `CONFIRM` on `8972d963…` retires. (1a)/(1c)/(1d): **both** waves; RD-32c's `CONFIRM` on `193e3c1e…` retires too |
| **Earliest gate** | before the Wave A re-offer |
| **Next transaction** | rule an arm in `../../../decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`; the ceremony text is then drafted, the argument regenerates, and **one** fresh exact-package review runs |

Analysis, with method and denominators: `P33-SEMANTIC-INSTALL-ANALYSIS.md`.

## 2. P-31 — merged, but not reconciled

| | |
|---|---|
| **Question** | The flagship V0 rendering — merged, evidence exists, reconciliation not yet computed — is bound to no RFC2-24 reason. Ratify the drafted exemption, or revert it? |
| **Current authority** | RFC2-24's closed twelve-reason list (decision A5 closed it); the drafted arm is **RFC2-19(a)** in `RFC-0002/reconciliation-chain.md`, disclosed in place as awaiting this ruling |
| **Recommendation** | `[Inferred]` **ratify** — a merge is not evidence of satisfaction, and the honest rendering of "not yet computed" is Unknown |
| **Consequence** | ratifying keeps the drafted bytes; reverting removes them and leaves the flagship rendering unbound to any reason, which VIS-2 disfavors |
| **Digest invalidated** | none *additional* — the arm is already in the candidate bytes; the ruling decides whether the Wave A act ratifies or the revert regenerates |
| **Earliest gate** | at the Wave A act (§7 of the acceptance record lists what the act ratifies beyond its digest) |
| **Next transaction** | record the ruling on the queue row P-31; if revert, batch it into the P-33 regeneration |

## 3. P-37 — project-shape facets and their authority home

| | |
|---|---|
| **Question** | Does the observable facet vocabulary belong to the Capability 1 specification, or to shared contract semantics? |
| **Current authority** | none — the vocabulary appears in **zero** of the 30 Waves A+B modules (swept, RD30-01), while three launch-path documents claimed the Wave A act ratifies it |
| **Recommendation** | `[Inferred]` **(a)** — the **Capability 1 specification owns the observable facet vocabulary**; Wave A owns the underlying constituent facts and evaluation semantics. **Seven** facets, per the linked packet, which wins over this row: Registered · Shape present · Human-understandable · Observable · Traceable · Reconciled · **Mission-ready**. *(Corrected 2026-08-11 by RD-52: this row said six and demoted Mission-ready to "a future extension", contradicting the packet's rule 3 — which is that **Mission-ready renders `not evaluated / deferred / Unknown`** until the C/D-wave semantics exist, because "a deferred facet renders its deferral honestly rather than waiting invisible". The difference is operational: seven rows render, one of them honestly deferred; six rows render and the seventh is silent, which is the invisible wait VIS-2 forbids.)* |
| **Consequence** | **No rollup.** Each facet exposes its constituent facts and reasons; no facet composes into a maturity or compliance score. If the owner instead wants facets to be shared contract semantics, **Wave A must be amended, regenerated, and freshly confirmed** |
| **Digest invalidated** | (a): none. The contract-semantics alternative: Wave A |
| **Earliest gate** | cheapest before the Wave A re-offer; strictly required before Capability 1 is authored |
| **Next transaction** | rule in `../../../decisions/PROJECT-SHAPE-FACETS-DECISION.md` |

## 4. P-36 — Unknown versus Gap

| | |
|---|---|
| **Question** | What separates the two words a reader will see everywhere? |
| **Recommendation** | `[Inferred]` **(a)**, in these words: **Unknown** — evidence is insufficient to decide satisfaction. **Gap** — current admissible evidence establishes non-satisfaction. Therefore: *no verifying evidence → Unknown; evidence of absence or failure → Gap* |
| **Consequence** | Capability 1's acceptance criteria use both words; leaving them undistinguished makes the first specification's tests unwritable |
| **Digest invalidated** | none |
| **Earliest gate** | before Capability 1 is authored |
| **Next transaction** | rule in `../../../decisions/UNKNOWNS-AND-GAPS-DECISION.md` |

## 5. P-38 — human entry and repository discoverability

| | |
|---|---|
| **Question** | What is the fixed human entry point, and what may Syzygy write? |
| **Recommendation** | `[Inferred]` **(a)** — `.syzygy/intent/OVERVIEW.md` is both the fixed Syzygy-owned human entry **and** the primary narrative. Per-repository discoverability keeps its four-value domain: **yes / no / not-applicable / Unknown**. Syzygy may **propose** a root README link and never directly writes one |
| **Consequence** | the write boundary stays where doctrine puts it — Syzygy writes only under `openspec/**` and `.syzygy/**` |
| **Digest invalidated** | (a): none. The alternative arm costs one Wave B regeneration plus a two-document seam |
| **Earliest gate** | Wave B act; on Capability 1's E3 path regardless |
| **Next transaction** | rule in `../../../decisions/HUMAN-ENTRY-DECISION.md` |

## 6. P-40 — specification granularity

| | |
|---|---|
| **Question** | What is one OpenSpec change? |
| **Recommendation** | `[Inferred]` **(a)**, in these words: *One OpenSpec change governs one coherent capability, or one coherent change to a capability, with one owner-readable product argument and one acceptance decision.* |
| **Consequence** | this defines what "Capability 1 is one spec" even means, and the specification-acceptance policy (P-41) is written against it — **rule P-40 before freezing that policy's bytes** |
| **Digest invalidated** | none |
| **Earliest gate** | before Capability 1 is authored; before P-41's policy is frozen for review |
| **Next transaction** | rule in `../../../decisions/SPECIFICATION-GRANULARITY-DECISION.md` |

## 7. P-39 — OpenSpec form and version

| | |
|---|---|
| **Question** | Which OpenSpec version does the project pin, and what is the migration posture? |
| **Recommendation** | `[Inferred]` **(a)** with the upgrade path noted — **but the deciding fact is checked at decision time, not guessed now**: verify the installed version, verify current official upstream, compare the artifact-format differences, record the choice and the migration posture, and pin it in the substrate lock |
| **Consequence** | this is the one launch-critical check needing material **from outside the clone** (two package versions). Treat it as a **pre-sitting task** with cost `[Unknown]` — network and registry availability — never a minutes-in-the-sitting step |
| **Digest invalidated** | none |
| **Earliest gate** | before the first OpenSpec changeset, which is Capability 1 |
| **Next transaction** | run the version comparison, then rule in `../../../decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md` and pin in `GOVERNANCE-SUBSTRATE-LOCK.yaml` |

## 8. P-41 and P-42 — two craft acts

| | |
|---|---|
| **Question** | Do the specification-acceptance standard (CC-SPEC-1…10) and the shape-to-spec impact rule come into force? |
| **Current authority** | both are candidates; each needs its own `CONFIRM CRAFT AMENDMENT` act |
| **Recommendation** | `[Inferred]` bring both into force **before** Capability 1 is authored. Without the first, spec acceptance is a vibe check (E5); without the second, the first post-spec shape amendment creates silent contradictions between layers (E6) |
| **Consequence** | both are Capability 1 prerequisites in the readiness standard. The specification-acceptance policy's bytes should be **frozen after P-40 is ruled**, then reviewed fresh, then repaired, then offered |
| **Digest invalidated** | none — neither touches contract bytes |
| **Earliest gate** | before Capability 1 authoring |
| **Next transaction** | rule P-40; freeze the policy; commission the fresh review; generate each craft-amendment offering |

## 9. P-35 — project operating constraints

| | |
|---|---|
| **Question** | What resources does this project actually have? |
| **Recommendation** | `[Inferred]` **(a)** — state them, or record honest `Unknown`s: operators · engineering attention · independent-review capacity · provider budget · maximum concurrent workstreams · proving project · time horizon · scope-reduction triggers |
| **Consequence** | A6 fails when the shape silently assumes a team, budget or cadence the project does not have; F5 reads the same file for independent-review capacity. **A scope-reduction trigger may request a doctrine or scope amendment; it may not silently move a doctrine-mandated 3D capability out of V0** |
| **Digest invalidated** | none |
| **Earliest gate** | before the formal launch administration — A6 and F5 read this file |
| **Next transaction** | answer in `../../../decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md` |

## 10. P-34 — the launch-gate policy itself

| | |
|---|---|
| **Question** | Does launch-gate **v2.0** become process policy? |
| **Recommendation** | `[Inferred]` approve **after** its two independent reviews return, not before |
| **Consequence** | the formal administration is run *under* this policy; approving it is what makes that administration's verdict mean anything |
| **Digest invalidated** | none — the instrument is not contract content |
| **Earliest gate** | before the formal launch administration |
| **Next transaction** | the bounded packet is `../../../decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` |

---

## What is *not* on this page, and why

- **The wave acts themselves** (P-1) — they are acts, not decisions; their
  phrases and digests live in the acceptance record, which wins over every
  offering.
- **The owner launch decision** — the last gate, taken after a formal
  administration returns READY, and never implied by one.
- **Waves C1/C2/D1/D2 and P-29/P-30/P-32** — deferred; they contaminate no
  row above.
- **P-12, P-14…P-28** — real, open, and not launch-critical. The queue holds
  them.

## The one-sitting claim, stated as a claim

This page is designed to be readable in one sitting and to route to nine
packets that are each bounded. Whether it *is* readable in one sitting is
an F3 question that this pass cannot answer about its own work — the
owner-packet comprehension review is commissioned separately, and until it
returns, the claim is `[Inferred]`, not `[Observed]`.
