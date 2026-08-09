# The first specification sequence — revision 2 (round 2026-08d)

> **Candidate plan. Binds nothing, and creates nothing.** No OpenSpec
> changeset exists, no `openspec/` tree exists, and none may be created
> before the owner acts. This file records **what to specify first, in what
> order, and what each one depends on**. It supersedes
> `../round-2026-08c/FIRST-OPENSPEC-SEQUENCE.md`; the ordering and the
> four capabilities are unchanged — what changed is the gating, because the
> round-08d wave split means a capability no longer waits on the whole
> corpus, and three of the previous revision's contract gaps are now
> repaired in candidate bytes.
>
> It chooses no language, framework, database, graph store, rendering
> engine or deployment target, and it contains no schema.

## The rule this sequence is built on

Unchanged: **the capability whose absence would make the next one's
evidence uninterpretable goes first.** Each capability must be provable on
its own.

## The four capabilities, and what changed under each

### Capability 1 — Project registration and shape visibility

Scope and behaviour rows as in revision 1, with these corrections:

- Row 1.3 (fixed human entry): the fixed-path clause **now exists** —
  **RFC7-39** (`.syzygy/intent/OVERVIEW.md`, governed presentation never
  authority, absence renders). The revision-1 gap note is closed in
  candidate bytes.
- Row 1.6 (discoverability finding): now governed by **RFC7-40**
  (per-repository yes/no/Unknown kernel finding; propose, never write).
- Row 1.4 (seven independent facets): the anti-rollup obligations are now
  clause-borne — RFC6-19 as amended (work state and chain state never
  folded; uncomputed reconciliation renders Unknown).

**Wave gate:** Capability 1 cites RFC 0001–0007 only → **Waves A and B**.
It does not wait for C or D waves.

### Capability 2 — Deterministic context packet generation

Corrections against revision 1:

- Row 2.1/2.2: selection is now governed by RFC11-4 **as amended** plus
  the declared `implementation_boundary` metadata (**RFC11-13**) and the
  traversal/termination rules (**RFC11-14**).
- Row 2.3: `constrains` is **now named** — **RFC11-16** (clause-first
  consumption). P-21(c′) is repaired in candidate bytes.
- Row 2.7: **ten** golden fixtures, each carrying a task/answer boundary
  so reproduction is blind derivation, not answer-copying. They remain
  hand-selected and labelled as such — that honesty is the test's value.
- Open craft gap, unchanged: **`CC-BUDGET-1` is installed nowhere** until
  the knowledge-hygiene act fires (owner packet 10).

**Wave gate:** **Waves A, C1 and C2** (RFC-0011 both modules; RFC-0001
through 0006 for the corpus being selected over). B is not required; D is
not required.

### Capability 3 — Minimum Polaris comprehension slice

Rows unchanged from revision 1. **Wave gate: Waves A and B.** Still a
sibling of Capability 2, deliberately — a Polaris failure and a compiler
failure must not be confusable.

### Capability 4 — Integrated observatory proving slice

Rows unchanged. **Wave gate: all six waves proven**, and Capabilities 1–3
proven, not merely specified. The Mission caveat is updated: RFC1-7 now
carries a **mission extension profile** in candidate bytes (P-28 option
(b), drafted), so if Wave A is accepted as offered, a Mission *is* a
selectable identified entity — but Capability 4 still proves a
Mission-free path first, because mission execution is D-wave and V1
material (owner packets 3 and 5).

## Dependency graph

```text
Wave A ─┬─ Wave B ──► Capability 1 ──► Capability 3 ─┐
        │                  │                          ├──► Capability 4
        └─ Waves C1+C2 ──► Capability 2 ─────────────┘
   (Waves D1/D2 gate Mission specification, which is after this sequence)
```

## What must be settled before Capability 1 is authored

| Blocker | Kind | Where |
|---|---|---|
| Wave A and Wave B acts | Owner acts | acceptance record — until a wave act, its contracts are candidates and a specification citing them cites nothing |
| OpenSpec version | Owner decision | round-08d packet 11 |
| Project-shape facets | Owner decision | round-08d packet 7 (Wave A ratifies the drafted form) |
| Core vocabulary leaks repaired | Owner decision | round-08d packet 9 — cheapest before the overview act |

The license (packet 12) does not block specification; it blocks release.

## What must be settled before Capability 2 is authored

| Blocker | Kind | Where |
|---|---|---|
| Waves C1 and C2 acts | Owner acts | acceptance record |
| `CC-BUDGET-1` installed | Craft act | round-08d packet 10 — the decomposition threshold has no owning rule until then |
| Unknown-vs-Gap vocabulary | Owner decision | round-08d packet 2 — omission registers will use both words |

## What this file deliberately does not contain

Unchanged from revision 1: no changeset, no schema, no estimates, and no
claim that the sequence is right — `[Inferred]`, one defensible ordering
with its reasoning stated so the owner can disagree with the reasoning
rather than only the conclusion.
