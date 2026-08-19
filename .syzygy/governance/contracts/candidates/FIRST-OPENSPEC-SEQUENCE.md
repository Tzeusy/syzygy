# The first specification sequence — revision 4 (specification stage, 2026-08-20)

> **Candidate plan. Binds nothing, and creates nothing.** The Capability 1
> OpenSpec change `project-registration-and-honest-shape-visibility`
> **exists since 2026-08-20** under the owner's launch decision
> (`decisions/CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md`) — as a
> **candidate**, adopted by no one; this plan neither created it nor
> governs it. **This is the single current first-spec document**: it
> supersedes `round-2026-08d/FIRST-OPENSPEC-SEQUENCE.md`
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
acceptance decision (granularity rule, ratified 2026-08-16 as **SDR-37**,
`decisions/SURFACE-DECISION-RECORD.md`; P-40).

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
| 1.3 | Serve the fixed human entry at the declared entry path | `RFC7-39` | — *(none directly; the clause governs)* | — |
| 1.4 | Answer the shape facets independently — no rollup, no composite badge; uncomputed reconciliation renders Unknown | `RFC2-24`, `RFC6-17`, `RFC6-18`, `RFC6-19`, `RFC6-22`, `RFC8-18`, `RFC8-19` | `VIS-2` | — |
| 1.5 | Expose the owning authority and the Unknown reason for every answer, identically to human and machine | `RFC3-16`, `RFC6-13`, `RFC6-14`, `RFC6-15`, `RFC6-23`, `RFC7-33` | `VIS-2` | — |
| 1.6 | Render per-repository discoverability in the closed four-value domain; propose the link, never write it | `RFC1-27`, `RFC3-3`, `RFC7-40` | `VIS-5` | — |
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

| Prerequisite | Kind | State (2026-08-17) |
|---|---|---|
| Wave A act performed at a confirmed argument | Owner act | **satisfied — performed 2026-08-17** over the RD-31b-confirmed argument; recorded in `decisions/ACCEPTANCE-ACT-RECORD.md`, modules installed at `contracts/rfcs/` (shape (M)) |
| Wave B act performed at a confirmed argument | Owner act | **satisfied — performed 2026-08-17**, after the Wave A act, over the RD-32c-confirmed argument; recorded in `decisions/ACCEPTANCE-ACT-RECORD.md` |
| P-33 Wave A install shape ruled | Owner decision | **owner-waived** — ruled 2026-08-16, option (M); `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`, `decisions/PENDING-OWNER-DECISIONS.md` ("Resolved on 2026-08-16") |
| P-31 merged-unreconciled exemption ratified | Owner decision | **owner-waived** — ruled 2026-08-16, drafted `RFC2-19(a)` ratified as written; SDR-34 |
| P-39 OpenSpec form/version | Owner decision | **owner-waived** — ruled 2026-08-16, pin current upstream at 1.9.0; `GOVERNANCE-SUBSTRATE-LOCK.yaml` `openspec` block |
| P-40 specification granularity | Owner decision | **owner-waived** — ruled 2026-08-16, one capability per change; SDR-37 |
| P-36 Unknown vs Gap | Owner decision | **owner-waived** — ruled 2026-08-16, the two-term rule; SDR-35 |
| P-37 project-shape facets | Owner decision | **owner-waived** — ruled 2026-08-16, seven facets, drafting site = the Capability 1 specification (a2); SDR-36. The facet *vocabulary text* still needs authoring into that specification when written — the ruling names the site, not the text |
| P-38 human entry and discoverability | Owner decision | **owner-waived** — ruled 2026-08-16, option (a) as drafted; `decisions/HUMAN-ENTRY-DECISION.md` |
| P-41 + P-42 acceptance and impact standards in force | Craft acts | **satisfied — acts 6 and 7 performed 2026-08-17, one sitting** (review cycle: RD-69 → one blocker repair → RD-70 `CONFIRM WITH EXCEPTIONS`); CC-SPEC-1…11 and CC-IMPACT-1…7 in force at their reviewed digests; recorded in `decisions/ACCEPTANCE-ACT-RECORD.md` and the craft `INSTALL-RECORD.md` |
| P-12 knowledge hygiene (CC-BUDGET-1) | Craft act | **blocking** for Capability 2; for Capability 1 the budget rule is not consumed — **not applicable** to Capability 1's own authoring, listed for visibility |
| P-34 launch-gate instrument authority (current version per the instrument's own header; RD34-05) + formal administration READY | Process | **satisfied for authoring — by the owner's launch decision, 2026-08-20**: Administration 1 (`NOT READY`, 2026-08-18) was accepted as diagnostic evidence and the owner decided directly on the record in hand, a path the gate policy and the P-48 stop condition both reserve to the owner. No `READY` verdict exists, and none is claimed |
| P-14 license | Owner decision | **not applicable** — blocks release, not specification |
| P-35 operating constraints | Owner decision | **owner-waived** — ruled 2026-08-16, full table recorded; `decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md`. Still blocks the formal administration's A6/F5 verdicts, which read the recorded statement rather than the ruling event |
| Waves C1/C2/D1/D2, P-29, P-30, P-32, D3/D4 | — | **not applicable** — deferred per `DEFERRED-WAVE-POSTURE.md`; not on Capability 1's path |

**As of 2026-08-20 (post-launch-decision):** eight of the scoped rows are
`owner-waived` (ruled 2026-08-16, per `decisions/DECISION-HISTORY.md`),
**three rows are `satisfied` by acts** — the Wave A and B acts (performed
2026-08-17, A then B) and the P-41/P-42 craft acts (acts 6 and 7,
performed later the same day in one sitting) — and the P-34 process row
is **satisfied for authoring** by the owner's 2026-08-20 launch decision.
**No row blocks Capability 1 authoring.** The P-37 facet-vocabulary text
the a2 ruling assigned to the specification is now authored there
(CAP1-REQ-030). Adoption of the resulting specification remains a
separate future owner act.
The concept-level trace behind this table is
`round-2026-08e/FIRST-SPEC-TRACE-TABLE.md` (E3), which this batch did not
refresh — a follow-on task, not performed here.

## The rest of the sequence — later capability families (non-authoritative)

Restated 2026-08-20 as **capability families**, so later changes have a
named home before any is chartered. Each family is one or more future
OpenSpec changes under SDR-37's granularity rule; nothing below is
chartered, scheduled, or promised, and every family waits on Capability 1
being **adopted** first.

- **Shared foundation** — Capability 1 (this change): registration,
  consent boundary, entry, shape answers, explanation/parity,
  discoverability. Waves A + B.
- **Polaris family** — comprehension surfaces: the project white paper,
  walkthrough evidence (which would also settle this spec's U-01), intent
  views. Waves A + B.
- **Trajectory family** — work ingestion, execution accounting,
  reconciliation computation (retiring the uncomputed-`Reconciled`
  posture). Waves A + B; RFC 0004's machinery.
- **Orrery family** — the project map and aggregation views under the
  no-composite rules. Waves A + B; RFC 0008's machinery.
- **Cross-view family** — cross-surface integration (RFC 0009).
- **Integrated proof** — the observatory proving slice: the prior
  families **proven, not merely specified**, on one real, messy project,
  showing at least one Unknown region rendering honestly.
- **Mission Control — separate track.** Mission and deterministic-context
  capabilities (the former Capability 2) gate on the deferred Waves
  C1/C2/D1/D2 and their own owner acts (P-12, P-21, D3/D4); they join the
  sequence only after those acts, never by drift.

```text
Wave A ─┬─ Wave B ──► Shared foundation (Cap 1) ──► Polaris ──► Trajectory ──► Orrery ──► Cross-view ─► Integrated proof
        └─ Waves C1+C2+D1+D2 (deferred) ──► Mission Control track (separate)
```

## What this file deliberately does not contain

No changeset, no schema, no estimates, and no claim that the sequence is
right — `[Inferred]`, one defensible ordering with its reasoning stated
so the owner can disagree with the reasoning rather than only the
conclusion.
