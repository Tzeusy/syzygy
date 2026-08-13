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
>
> **It owns no state it reports.** The wave rows are owned by
> `PROJECT-STATUS.md` and the `P-nn` rows by
> `decisions/PENDING-OWNER-DECISIONS.md`; where this plan and one of those
> disagree, **the owning record wins and this plan is stale**. Report the
> disagreement rather than resolving it yourself.

## The rule this sequence is built on

Unchanged since revision 1: **the capability whose absence would make the
next one's evidence uninterpretable goes first.** Each capability must be
provable on its own. One capability = one OpenSpec change = one owner
acceptance decision (granularity rule, P-40, pending).

## The one first specification (E2)

```text
Capability 1 — Project registration and honest shape visibility
```

Scope, stated here so no superseded revision must be opened *(inlined
2026-08-10, RD30-10 — the former pointer chained through revision 2 into
revision 1)*.

**The table below is generated** *(2026-08-13, owner charter §10)* from
`CAPABILITY-1-CHARTER.yaml` by `scripts/build_capability_1_views.py`, which
resolves every clause to its authority home through the generated contract
index and refuses one homed outside Waves A+B. **Do not edit it here** —
edit the charter and regenerate; `--check` fails on drift. The same table,
with the trace skeleton, the clause-coverage population and the
blocking-decision list, is in `CAPABILITY-1-GENERATED-VIEWS.md`.

<!-- BEGIN GENERATED: capability-1 behaviour rows -->
| Row | Behaviour | Governing clauses | Doctrine | Owner decisions |
|---|---|---|---|---|
| 1.1 | Parse and validate the project declaration; an invalid declaration is a named failure, never partial registration | `RFC1-1`, `RFC3-1`, `RFC3-4`, `RFC3-5`, `RFC3-9` | `VIS-2` | — |
| 1.2 | Record consent and repository coverage; the boundary renders as a fact, not silence | `RFC1-3`, `RFC1-4`, `RFC3-6`, `RFC3-7`, `RFC3-16(a)`, `RFC5-3`, `RFC6-26` | `VIS-5` | — |
| 1.3 | Serve the fixed human entry at the declared entry path | `RFC7-39` | — *(none directly; the clause governs)* | `P-38` |
| 1.4 | Answer the shape facets independently — no rollup, no composite badge; uncomputed reconciliation renders Unknown | `RFC2-24`, `RFC6-17`, `RFC6-18`, `RFC6-19`, `RFC6-22`, `RFC8-18`, `RFC8-19` | `VIS-2` | `P-31`, `P-36`, `P-37` |
| 1.5 | Expose the owning authority and the Unknown reason for every answer, identically to human and machine | `RFC3-16`, `RFC6-13`, `RFC6-14`, `RFC6-15`, `RFC6-23`, `RFC7-33` | `VIS-2` | `P-36` |
| 1.6 | Render per-repository discoverability in the closed four-value domain; propose the link, never write it | `RFC1-27`, `RFC3-3`, `RFC7-40` | `VIS-5` | `P-38` |
<!-- END GENERATED: capability-1 behaviour rows -->

Read against the seven-facet decision P-37 (corrected form) and the E3
trace (`round-2026-08e/FIRST-SPEC-TRACE-TABLE.md`), which anchors each
row's clauses at the current bytes. **Wave gate:
Waves A and B only.** Capability 1 does not wait for — and must not
silently rely on — Waves C1/C2/D1/D2 (`DEFERRED-WAVE-POSTURE.md`).

Mission-ready renders `not evaluated / deferred / Unknown` until the C/D
semantics exist (P-37 rule 3); registration is never certification.

## Prerequisites for authoring Capability 1 — one state per row, scoped

Each row carries **one state for authoring Capability 1**. A row whose
blocking force belongs to a *different* gate (the launch decision, the
formal administration, a later capability) says so in its own cell as a
scope note — that is a scoped state, not a second one.

States: `satisfied` / `owner-waived` / `blocking` / `not applicable`.

| Prerequisite | Kind | State (2026-08-11) |
|---|---|---|
| Wave A act performed at a confirmed argument | Owner act | **blocking** — the *argument* is confirmed (`VERDICT: CONFIRM`, RD-31b); what blocks is that no act has been performed, and the offer itself is withheld solely by **P-33**. Corrected 2026-08-11, RD-50 f2: this cell previously read "fresh exact-package review then the offer", which the confirmation had already overtaken |
| Wave B act performed at a confirmed argument | Owner act | **blocking** — same shape: confirmed (`VERDICT: CONFIRM`, RD-32c), unoffered, and it follows Wave A. Nothing else withholds it |
| P-33 Wave A install shape ruled | Owner decision | **blocking** (gates the Wave A re-offer; packet `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`) |
| P-31 merged-unreconciled exemption ratified | Owner decision | **blocking** (drafted arm rides Wave A; ruling wanted at or before that act) |
| P-39 OpenSpec form/version | Owner decision | **blocking** (`decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md`) |
| P-40 specification granularity | Owner decision | **blocking** (`decisions/SPECIFICATION-GRANULARITY-DECISION.md`) |
| P-36 Unknown vs Gap | Owner decision | **blocking** (acceptance criteria use both words) |
| P-37 project-shape facets | Owner decision | **blocking** — the anti-rollup ground (RFC6-18/19 as amended) is Wave A's; the facet vocabulary itself is drafted **nowhere** and needs P-37's ruling plus its chosen drafting site (corrected 2026-08-10, RD30-01) |
| P-38 human entry and discoverability | Owner decision | **blocking** (on the E3 path; Wave B ratifies) |
| P-41 specification acceptance standard in force | Craft act | **blocking** — candidate exists (`policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`); queued as **P-41**; wants review + its craft act, or the owner knowingly authors against the candidate |
| P-12 knowledge hygiene (CC-BUDGET-1) | Craft act | **blocking** for Capability 2; for Capability 1 the budget rule is not consumed — **not applicable** to Capability 1's own authoring, listed for visibility |
| P-34 launch-gate instrument authority (current version per the instrument's own header; RD34-05) + formal administration READY | Process | **blocking** for the launch decision (the owner may lawfully decide without it, but this pass's charter treats the formal administration as the evidence bar) |
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
