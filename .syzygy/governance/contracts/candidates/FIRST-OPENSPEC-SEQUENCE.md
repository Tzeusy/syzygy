# The first specification sequence — revision 3 (launch-closure pass, 2026-08-10)

> **Candidate plan. Binds nothing, and creates nothing.** No OpenSpec
> changeset exists, no `openspec/` tree exists, and none may be created
> before the owner acts. **This is the single current first-spec
> document**: it supersedes `round-2026-08d/FIRST-OPENSPEC-SEQUENCE.md`
> (revision 2) and, through it, the round-08c revision; the
> banner-superseded `09-OPEN-SPEC-READINESS-REPORT.md` sequencing is
> historical and competes with nothing. It chooses no language,
> framework, database, graph store, rendering engine, or deployment
> target, and contains no schema.

## The rule this sequence is built on

Unchanged since revision 1: **the capability whose absence would make the
next one's evidence uninterpretable goes first.** Each capability must be
provable on its own. One capability = one OpenSpec change = one owner
acceptance decision (granularity rule, P-40, pending).

## The one first specification (E2)

```text
Capability 1 — Project registration and honest shape visibility
```

Scope as in revision 2 (rows 1.1–1.6 with the round-08d corrections:
RFC7-39 fixed entry, RFC7-40 discoverability finding, RFC6-19 anti-rollup
amendments), read against the seven-facet decision P-37. **Wave gate:
Waves A and B only.** Capability 1 does not wait for — and must not
silently rely on — Waves C1/C2/D1/D2 (`DEFERRED-WAVE-POSTURE.md`).

Mission-ready renders `not evaluated / deferred / Unknown` until the C/D
semantics exist (P-37 rule 3); registration is never certification.

## Prerequisites for authoring Capability 1 — each with exactly one state

States: `satisfied` / `owner-waived` / `blocking` / `not applicable`.

| Prerequisite | Kind | State (2026-08-10) |
|---|---|---|
| Wave A act performed at a confirmed argument | Owner act | **blocking** — repairs landed this pass; fresh exact-package review then the offer |
| Wave B act performed at a confirmed argument | Owner act | **blocking** — same |
| P-33 Wave A install shape ruled | Owner decision | **blocking** (gates the Wave A re-offer; packet `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`) |
| P-31 merged-unreconciled exemption ratified | Owner decision | **blocking** (drafted arm rides Wave A; ruling wanted at or before that act) |
| P-39 OpenSpec form/version | Owner decision | **blocking** (`decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md`) |
| P-40 specification granularity | Owner decision | **blocking** (`decisions/SPECIFICATION-GRANULARITY-DECISION.md`) |
| P-36 Unknown vs Gap | Owner decision | **blocking** (acceptance criteria use both words) |
| P-37 project-shape facets | Owner decision | **blocking** (Wave A ratifies the drafted form) |
| P-38 human entry and discoverability | Owner decision | **blocking** (on the E3 path; Wave B ratifies) |
| Specification acceptance standard in force | Craft act | **blocking** — candidate exists (`policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`); wants review + its craft act, or the owner knowingly authors against the candidate |
| P-12 knowledge hygiene (CC-BUDGET-1) | Craft act | **blocking** for Capability 2; for Capability 1 the budget rule is not consumed — **not applicable** to Capability 1's own authoring, listed for visibility |
| P-34 launch-gate v1.5 authority + formal administration READY | Process | **blocking** for the launch decision (the owner may lawfully decide without it, but this pass's charter treats the formal administration as the evidence bar) |
| P-14 license | Owner decision | **not applicable** — blocks release, not specification |
| P-35 operating constraints | Owner decision | **blocking** for the formal administration's A6/F5 verdicts; the spec itself does not consume it |
| Waves C1/C2/D1/D2, P-29, P-30, P-32, D3/D4 | — | **not applicable** — deferred per `DEFERRED-WAVE-POSTURE.md`; not on Capability 1's path |

Nothing is `satisfied` and nothing is `owner-waived` today; every
`blocking` row is a prepared decision or a prepared act, none an
archaeology exercise. The concept-level trace behind this table is
`round-2026-08e/FIRST-SPEC-TRACE-TABLE.md` (E3).

## The rest of the sequence (unchanged in substance from revision 2)

- **Capability 2 — deterministic context packet generation.** Waves A,
  C1, C2 (deferred today); plus CC-BUDGET-1 in force (P-12) and P-36.
- **Capability 3 — minimum Polaris comprehension slice.** Waves A and B.
  Sibling of Capability 2 deliberately.
- **Capability 4 — integrated observatory proving slice.** All six waves
  and Capabilities 1–3 **proven, not merely specified**; runs on one
  real, messy project; must show one Unknown region rendering honestly.

```text
Wave A ─┬─ Wave B ──► Capability 1 ──► Capability 3 ─┐
        │                                             ├──► Capability 4
        └─ Waves C1+C2 ──► Capability 2 ─────────────┘
   (Waves D1/D2 gate Mission specification, after this sequence)
```

## What this file deliberately does not contain

No changeset, no schema, no estimates, and no claim that the sequence is
right — `[Inferred]`, one defensible ordering with its reasoning stated
so the owner can disagree with the reasoning rather than only the
conclusion.
