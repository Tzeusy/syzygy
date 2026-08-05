# OpenSpec readiness report (directive §10/§14)

**Question answered:** is the project genuinely ready to begin its first
OpenSpec feature changesets — and in what order? **No changeset is
authored in this phase** (hard boundary; six phase-rule clauses).

## Readiness, criterion by criterion

| Criterion | State |
|---|---|
| Governing contracts stable and identifiable | 11 contracts, 322 clauses, exact digests at the gate; clause identities frozen (amend-in-place discipline) |
| RFC/OpenSpec boundary binding | Six shape-parallel phase-rule clauses (RFC6-28/7-38/8-32/9-52/10-16/11-12); no observable behavior schedulable from RFC prose |
| Routing prepared | `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md` + coverage skeleton; 8 future-spec domains named (provisional) |
| Context governance | Deterministic selection metadata (`05-CONTRACT-INDEX.yaml`), measured per-task loads (fixtures 1–5), packet contract (RFC-0011) |
| Machine-client contract | Closed at requirement level (RFC5-3/5/6); mechanism choice explicitly blocks V0 implementation, not specification |
| Acceptance semantics | Two-state model (RFC3-16(c)); honest bootstrap-vs-verified status in the final record |
| **Blocking before any changeset** | **The owner gate**: `ACCEPT COMPACTED FOUNDATIONAL RFCS` (plus the separately-gated topology/craft/overview acts as the owner chooses); RFC 0003 §8 q4 (`declarations/`) should be ruled at the gate (triage) |
| Open questions | None blocks specification authoring per the re-derived per-question arguments in `08-OPEN-QUESTION-TRIAGE.md` (6 may stay open; 13 close before V0 incl. the RFC9-9 follow-on; 7 before Mission Control V1) |

**Verdict: ready, conditional only on the owner gate.** After acceptance,
the first proposal runs `/th-projects project-feature-request` →
owner-approved OpenSpec delta → project-direction → beads-orchestration
(AGENTS.md post-bootstrap order); `_bootstrap/` archives per Prompt 24.

## Recommended first OpenSpec changeset sequence

**This sequence is advisory and commits nothing** — like the routing
matrix, this file is not a contract and creates no OpenSpec changeset;
each entry becomes real only through `/th-projects
project-feature-request` and an owner-approved delta. Ordered by
dependency and by v1.md's V0 mandate (the propagation
proof-of-concept: intent → gap → work → evidence at minimal breadth):

1. **`spec/selection-api` — cross-surface selection, query answers,
   machine parity** (RFC6-28's coverage matrix is the first deliverable).
   Every surface and every machine client consumes it; smallest surface
   area; unblocks parity testing for everything after.
2. **`spec/intent-surface` — Polaris core**: narrative model, claim
   blocks/anchors, adoption workflow, proposed-state presentation
   (RFC 0007 OS rows). The loop's entry point.
3. **`spec/work-surface` — Trajectory core**: normalized two-field state
   rendering, board, materialization/dispatch records (RFC 0008 OS
   rows). Completes the V0 propagation slice with evidence semantics.
4. **`spec/mission-control` — missions, envelopes, attention queue, CLI
   surface** (RFC10-4/5/7/12/13 + RFC11-10 registry surface). Requires
   1–3's vocabulary; carries the RFC10-5 lifecycle-freeze review against
   RFC 0008 states (§8 q1) and the autonomy-level enumeration (§8 q2).
5. **`spec/context-packets` — compiler observables**: packet inspection,
   omission reports, diagnostics (RFC11-1's OS part). Can proceed in
   parallel with 4 once 1 exists.
6. **`spec/map-surface` (+ `map-scenes`, `map-lenses`) — Orrery**
   (RFC 0009 OS rows). Largest; deliberately last in V0 or early V1 per
   v1.md's slice priorities; the D1-gated historical bundle stays
   dormant behind its own owner approval.

Each changeset must produce its clause-to-requirement coverage rows
against the skeleton, with reviewed N/A judgments for purely structural
clauses — the phase rules make this non-optional.

## What later committed conformance tooling must exist (directive §11)

After RFC acceptance, the review-tooling checks in `scripts/` graduate to
committed conformance checks: clause-continuity + citation resolution on
every contract amendment; index regeneration drift-check in CI;
context-packet completeness validation (RFC11-6) once a compiler exists;
package README ↔ module front-matter consistency. These are
implementation-phase deliverables, routed through OpenSpec like all
observable behavior.
