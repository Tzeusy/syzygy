# Design — project-registration-and-honest-shape-visibility

> **Scope of this document.** This is *specification-level* design: how
> the requirement set is organized and warranted, and which decisions are
> deliberately not made. **Implementation design is deferred until the
> owner adopts this specification** — no language, framework, database,
> renderer, graph store, storage layout, API shape, or deployment model
> is chosen here, and nothing in this file may be read as an
> implementation decision.

## Context

This is the repository's first specification. The governing shape is
already fixed by adopted doctrine (VIS-1…7, SEC-1…5), the accepted Wave
A/B contracts (RFC 0001–0009), the in-force craft policies (CC-SPEC-1…11,
CC-IMPACT-1…7), and the recorded owner rulings (notably SDR-34…37 and the
P-38 human-entry ruling). The specification's job is to project that
shape onto one capability's observable behavior — not to invent new
shape.

## Decisions

### D1 — Six literal groups plus cross-cutting, gap-numbered stable IDs

Requirements are grouped by the six owner-visible behavior groups
(declaration; consent and coverage; human entry; shape answers;
explanation and parity; discoverability) with a seventh cross-cutting
group, and numbered `CAP1-REQ-001…064` with deliberate gaps per group.
IDs are minted once, amended in place, retired rather than reused, never
renumbered (CC-SPEC-3). Gaps keep later insertions inside their group
without renumbering.

### D2 — Warrants live inline per requirement; the spec-level list is generated

Each requirement carries one fenced `warrants` YAML block naming its
material authorities in CC-SPEC-2's six classes. The specification-level
dependency declaration is **generated** as the union of these blocks
(CC-IMPACT-1) by `scripts/build_capability_1_spec_dependencies.py` into
`GOVERNING-DEPENDENCIES.md` in this change directory; no second
hand-maintained list exists, so the two cannot drift.

### D3 — The facet vocabulary is authored in the spec, values governed by general rules

SDR-36 sites the seven-facet drafting in this specification (site a2).
CAP1-REQ-030 defines each facet as a question plus its constituent
facts, and deliberately does **not** mint per-facet value enumerations:
values follow the general rules (two-term rule per SDR-35; closed
Unknown reasons per RFC2-24; deferred posture for Mission-ready per
SDR-36 rule 3). This avoids inventing vocabulary no accepted clause
warrants (CC-SPEC-6).

### D4 — Oracles are behavioral fixtures, never implementation probes

Every oracle is phrased over served output (human view, machine answer,
write records) against fixtures a checker controls, so any conforming
implementation can be tested without naming one (CC-SPEC-5,
implementation independence). Universally quantified requirements state
their counterexample schema and sweep denominator instead of a single
example (CC-SPEC-4's bounded-oracle rule; verification rule 9).

### D5 — Coverage is shipped as two tables plus one generated union

Per CC-SPEC-11, `CAPABILITY-COVERAGE.md` places every declared
Capability 1 obligation in exactly one of covered / lawfully out of
scope / Unknown. Per CC-SPEC-8, `CONTRACT-COVERAGE.md` maps each
applicable observable consequence of the accepted clauses to
requirements; consequences believed inapplicable render **Unknown
pending an owner-reviewed N/A** — the author mints no N/A on their own
authority.

## Deliberately not designed here

- Anything about how the behavior is built (stack, storage, schema,
  process model, protocol) — deferred until adoption.
- `Mission-ready` semantics — deferred with the Context/Mission waves;
  the spec fixes only its honest deferred posture.
- The comprehension-walkthrough machinery behind `Human-understandable`
  — the facet reads recorded evidence where it exists and renders
  `Unknown` otherwise.
- Reconciliation computation — V0 posture: uncomputed renders `Unknown`
  (SDR-12, SDR-34).

## Risks / Trade-offs

- **Inline YAML inside requirement blocks** is unusual for OpenSpec; the
  pinned validator (1.9.0, `--strict`) accepts it, and the generator
  treats the fenced blocks as the single machine-readable home. If a
  future OpenSpec version objects, the blocks move — a mechanical
  transform, with identity preserved by requirement ID.
- **OpenSpec requirement-identity survival across edit/rename** is an
  RFC 0004 adapter obligation acknowledged in the proposal's Unknowns;
  this change does not resolve it.

## Open questions this specification does not settle

Recorded against the open decision queue (CC-SPEC-6): P-1's deferred C/D
waves, P-21 (deterministic context), and the other open register rows
are untouched — no requirement here forecloses or presumes any of them,
and no pending decision is cited as a warrant: the generated
`GOVERNING-DEPENDENCIES.md` `decisions` section holds only recorded
rulings (SDR-12, SDR-34, SDR-35, SDR-36, and the P-38 ruling), which is
checkable mechanically. `CAPABILITY-COVERAGE.md` carries the
obligation-level disposition; U-01 names the one question this spec
leaves open on purpose.
