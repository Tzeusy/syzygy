# What binds today, what is only offered, and what does not exist

> **Non-authoritative round record.** Every row points at the artifact that
> owns the fact. Where a row and its artifact disagree, the artifact wins.
> As-of 2026-08-05b.

The question this answers: *a competent engineer joins tomorrow and is handed
one task — which of these documents may they rely on, and which are merely
proposals?* Getting that wrong in either direction is expensive. Treating a
candidate as binding invents obligations nobody agreed to; treating adopted
doctrine as a draft discards the only settled ground there is.

## Binds today

| What | Where | Since |
|---|---|---|
| **Doctrine** — VIS-1…7, SEC-1…5, the three-state thesis, the non-negotiables | `.syzygy/governance/doctrine/` | Adopted 2026-07-30, tag `doctrine-adopted-2026-07-30`; amendment **D1** in force |
| **Owner decisions** — SDR-1…33, extracted warrants, the pending queue | `.syzygy/governance/decisions/` | As recorded |
| **Engineering bar** — craft-and-care, CC-* | `.syzygy/governance/policies/craft-and-care/` | Owner-approved (**D2**). Clause-level force begins at foundational-contract acceptance — see `INSTALL-RECORD.md` |
| **The glossary** | `.syzygy/governance/doctrine/README.md:15` | With doctrine |

Doctrine is the only layer that answers *why*. Nothing below it may contradict
it, and no contract, policy, or plan can widen it.

## Offered, and binding nothing

Each of these is complete, digest-bound, and **awaiting one owner act**. An
agent may read and discuss them; none may be cited as authority, and none may
be installed into an accepted home.

| What | Where | Act |
|---|---|---|
| 32 foundational contract modules, RFC 0001–0011 | `contracts/candidates/rfcs/` | 1 |
| Craft amendment CC-TEST-2 | `craft-and-care/testing-and-verification.md` | 2 |
| Topology bundle, nine files | `.syzygy/map/topology-candidates/` | 3 |
| Project overview | `.syzygy/intent/OVERVIEW.md` | 4 |
| Doctrine amendment D3, bounded missions | `candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | 5, optional |
| Knowledge-hygiene craft policy | `candidates/policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` | its own craft act (P-12) |
| Term registry, T-01…T-30 | `candidates/policy-candidates/TERM-REGISTRY.md` | P-16 |
| Editorial doctrine amendment, glossary citation | `candidates/policy-candidates/DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md` | P-25 |

Exact phrases and the ceremony: `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`.
What each act covers and what is knowingly imperfect inside it:
`FINAL-OWNER-ACCEPTANCE-RECORD.md`.

## Never authority, whatever it says

| Kind | Examples | Why |
|---|---|---|
| **Generated projections** | `05-CONTRACT-INDEX.yaml`, `CONTRACT-DEPENDENCY-INDEX.md` | Rebuildable from the modules (RFC11-7). If a projection and a module disagree, the module is right and the projection is stale |
| **Round records and reports** | everything under `round-2026-08*/`, the numbered `0n-*.md` reports | They record what a round did. They do not oblige anyone |
| **Raw reviewer output** | `*/reviews/*-RAW.md` | Evidence. Stored verbatim and never edited — a verdict word is copied, never re-labelled |
| **Routing matrices** | `SURFACE-CLAUSE-ROUTING-MATRIX.md` | Says where a clause's content *will* belong after acceptance. Creates no OpenSpec content and schedules nothing |
| **Agent operating procedure** | `AGENTS.md`, `CLAUDE.md`, the skills | Repository procedure, not project truth |
| **Excluded history** | `_bootstrap/**` | Git-excluded, absent from every clone. May be cited only as unavailable history |

## Does not exist, and its absence is correct

| What | Why its absence is the right state |
|---|---|
| `.syzygy/governance/contracts/rfcs/` | The accepted-contract home. Created **only** by act 1 |
| `.syzygy/map/topology/` | Created **only** by act 3 |
| `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` | Created by the first act performed. Its absence is the proof no act has been performed |
| `openspec/` | Required observable behavior. Nothing may be authored there before act 1 |
| `src/`, `apps/`, `packages/`, any toolchain manifest | No stack has been chosen; choosing one requires an accepted contract |
| A context compiler | Would be application code. `context_load.py` measures a selection; it does not make one |

## The one-line test

**If an artifact's authority came from an owner act, name the act.** If you
cannot name one, it is a candidate, a record, or a projection — and it binds
nothing, however carefully it is written.
