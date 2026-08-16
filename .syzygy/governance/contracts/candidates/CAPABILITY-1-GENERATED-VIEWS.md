# Capability 1 — generated views

> **Generated. Never hand-edited.** Every table below is derived from
> `CAPABILITY-1-CHARTER.yaml` by
> `scripts/build_capability_1_views.py`. Edit the charter and
> regenerate; an edit here is overwritten and `--check` fails first.
>
> **Candidate planning metadata, not authority.** Every clause named
> here belongs to a confirmed-but-unaccepted wave and binds nothing.
> No `openspec/` exists and none may be created.
>
> Charter sha256 `9f21e68519e290eafa221bdf6c9e2465b3499dddd80d42241083cf25e80f45da`.

**CAP-1 — Project registration and honest shape visibility**

> A project can be registered and its shape read honestly — every facet answered on its own, every Unknown carrying its reason and its owning authority, and the same facts reaching a human and a machine — without any claim the evidence does not support.

## View 2 — the behaviour rows

Also injected into `FIRST-OPENSPEC-SEQUENCE.md` between its generated
markers, so the sequence and this file cannot disagree.

| Row | Behaviour | Governing clauses | Doctrine | Owner decisions |
|---|---|---|---|---|
| 1.1 | Parse and validate the project declaration; an invalid declaration is a named failure, never partial registration | `RFC1-1`, `RFC3-1`, `RFC3-4`, `RFC3-5`, `RFC3-9` | `VIS-2` | — |
| 1.2 | Record consent and repository coverage; the boundary renders as a fact, not silence | `RFC1-3`, `RFC1-4`, `RFC3-6`, `RFC3-7`, `RFC3-16(a)`, `RFC5-3`, `RFC6-26` | `VIS-5` | — |
| 1.3 | Serve the fixed human entry at the declared entry path | `RFC7-39` | — *(none directly; the clause governs)* | — |
| 1.4 | Answer the shape facets independently — no rollup, no composite badge; uncomputed reconciliation renders Unknown | `RFC2-24`, `RFC6-17`, `RFC6-18`, `RFC6-19`, `RFC6-22`, `RFC8-18`, `RFC8-19` | `VIS-2` | — |
| 1.5 | Expose the owning authority and the Unknown reason for every answer, identically to human and machine | `RFC3-16`, `RFC6-13`, `RFC6-14`, `RFC6-15`, `RFC6-23`, `RFC7-33` | `VIS-2` | — |
| 1.6 | Render per-repository discoverability in the closed four-value domain; propose the link, never write it | `RFC1-27`, `RFC3-3`, `RFC7-40` | `VIS-5` | — |

## View 3 — the E3 trace-table skeleton

One row per (behaviour row, clause). **The `Anchored text` column is
deliberately empty**: an anchor is a quotation from the clause at its
current bytes, and a generator that quoted clause prose would have
re-opened the door it closed. The skeleton says what must be anchored
and by whom; the anchoring is human work.

| Row | Clause | Authority home | Anchored text |
|---|---|---|---|
| 1.1 | `RFC1-1` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | |
| 1.1 | `RFC3-1` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.1 | `RFC3-4` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.1 | `RFC3-5` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.1 | `RFC3-9` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.2 | `RFC1-3` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | |
| 1.2 | `RFC1-4` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | |
| 1.2 | `RFC3-6` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.2 | `RFC3-7` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.2 | `RFC3-16(a)` | `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | |
| 1.2 | `RFC5-3` | `rfcs/RFC-0005/admission-and-boundary.md` | |
| 1.2 | `RFC6-26` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.3 | `RFC7-39` | `rfcs/RFC-0007/rendering-and-surface.md` | |
| 1.4 | `RFC2-24` | `rfcs/RFC-0002/rendering-vocabularies.md` | |
| 1.4 | `RFC6-17` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.4 | `RFC6-18` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.4 | `RFC6-19` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.4 | `RFC6-22` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.4 | `RFC8-18` | `rfcs/RFC-0008/state-vocabulary-and-cost.md` | |
| 1.4 | `RFC8-19` | `rfcs/RFC-0008/state-vocabulary-and-cost.md` | |
| 1.5 | `RFC3-16` | `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | |
| 1.5 | `RFC6-13` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.5 | `RFC6-14` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.5 | `RFC6-15` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.5 | `RFC6-23` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | |
| 1.5 | `RFC7-33` | `rfcs/RFC-0007/rendering-and-surface.md` | |
| 1.6 | `RFC1-27` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | |
| 1.6 | `RFC3-3` | `rfcs/RFC-0003/manifests-and-namespace.md` | |
| 1.6 | `RFC7-40` | `rfcs/RFC-0007/rendering-and-surface.md` | |

## View 4 — the initial clause-coverage population

The denominator a coverage matrix is judged against: every clause
this capability declares it relies on, and where it is homed. A clause
absent from this table is out of Capability 1's declared scope, which
is a claim a reviewer can contradict.

```text
population        29 clause(s)
authority homes   8 module(s), all within Waves A+B
deferred waves    C1, C2, D1, D2 — 0 clauses, checked at generation
```

| Clause | Authority home | Behaviour row |
|---|---|---|
| `RFC1-1` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | 1.1 |
| `RFC1-27` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | 1.6 |
| `RFC1-3` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | 1.2 |
| `RFC1-4` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | 1.2 |
| `RFC2-24` | `rfcs/RFC-0002/rendering-vocabularies.md` | 1.4 |
| `RFC3-1` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.1 |
| `RFC3-16` | `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 1.5 |
| `RFC3-16(a)` | `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 1.2 |
| `RFC3-3` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.6 |
| `RFC3-4` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.1 |
| `RFC3-5` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.1 |
| `RFC3-6` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.2 |
| `RFC3-7` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.2 |
| `RFC3-9` | `rfcs/RFC-0003/manifests-and-namespace.md` | 1.1 |
| `RFC5-3` | `rfcs/RFC-0005/admission-and-boundary.md` | 1.2 |
| `RFC6-13` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.5 |
| `RFC6-14` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.5 |
| `RFC6-15` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.5 |
| `RFC6-17` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.4 |
| `RFC6-18` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.4 |
| `RFC6-19` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.4 |
| `RFC6-22` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.4 |
| `RFC6-23` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.5 |
| `RFC6-26` | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | 1.2 |
| `RFC7-33` | `rfcs/RFC-0007/rendering-and-surface.md` | 1.5 |
| `RFC7-39` | `rfcs/RFC-0007/rendering-and-surface.md` | 1.3 |
| `RFC7-40` | `rfcs/RFC-0007/rendering-and-surface.md` | 1.6 |
| `RFC8-18` | `rfcs/RFC-0008/state-vocabulary-and-cost.md` | 1.4 |
| `RFC8-19` | `rfcs/RFC-0008/state-vocabulary-and-cost.md` | 1.4 |

## View 5 — the blocking-decision list

Every decision or act that blocks **authoring** this capability: the
charter's capability-level list, then every decision a behaviour row
names, in charter order and deduplicated. Each is verified at
generation to be an **open** row of the queue's own open section — a
resolved or executed row is refused, and so is one the queue does not
carry.

```text
P-1    capability-level
P-21   capability-level
P-22   capability-level
P-28   capability-level
P-41   capability-level
P-42   capability-level
```

**Open upstream, at a later gate — not consumed by authoring:** `P-34`.

## Non-goals

- Any composite or rolled-up project score, badge, or single health number
- Certification of any kind — registration is never certification
- Writing to a governed repository: the discoverability link is proposed, never written
- Mission evaluation, which renders `not evaluated / deferred / Unknown` until the C/D semantics exist
- Deterministic context-packet generation, which is Capability 2
- Any choice of language, framework, database, graph store, rendering engine, or deployment target

## Deferred semantics

| What | Why it is deferred |
|---|---|
| facet vocabulary | The facet names themselves are drafted in no accepted module. P-37 ruled 2026-08-16 (SDR-36): the Capability 1 specification owns them (site a2), not a Wave A amendment. The vocabulary still needs authoring into this specification when it is written — the ruling names the site, not the text. |
| Mission-ready facet | Renders `not evaluated / deferred / Unknown` while Waves D1/D2 are deferred. The facet exists; its semantics do not. |
| merged-but-unreconciled reason | P-31 ruled 2026-08-16 (SDR-34): the drafted RFC2-19(a) exemption is ratified as written — the flagship V0 rendering is bound to no thirteenth reason; the condition is disclosed as a fact of the render. |

---

Generated by `scripts/build_capability_1_views.py` from `CAPABILITY-1-CHARTER.yaml` — 6 behaviour row(s), 29 clause(s), 8 module(s), 6 blocking decision(s). Counts computed, never asserted.
