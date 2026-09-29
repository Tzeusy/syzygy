# Design — project-registration-and-honest-shape-visibility

**This design organizes and warrants the requirement set; it builds nothing.**
It fixes how requirements are grouped, identified, warranted and covered, and
names what it deliberately leaves open. No language, framework, database,
renderer, graph store, storage layout, API shape or deployment model is chosen
here, and nothing in this file is an implementation decision. The
implementation plan lives in `docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md`.

## Context

This is the repository's first specification. Its governing shape was fixed
before it was written:

- adopted doctrine (VIS-1…7, SEC-1…5);
- the accepted Wave A/B contracts (RFC 0001–0009);
- the in-force craft policies (CC-SPEC-1…11, CC-IMPACT-1…7);
- the recorded owner rulings, notably SDR-34…37 and the P-38 human-entry
  ruling.

The specification projects that shape onto one capability's observable
behavior. It invents no new shape.

## Decisions

### D1 — Six literal groups plus cross-cutting, gap-numbered stable IDs

- **Groups.** Requirements follow the six owner-visible behavior groups —
  declaration; consent and coverage; human entry; shape answers; explanation
  and parity; discoverability — plus a seventh, cross-cutting group.
- **Identifiers.** `CAP1-REQ-001…064`, with deliberate gaps per group so a
  later insertion stays inside its group. An identifier is minted once,
  amended in place, retired rather than reused and never renumbered
  (CC-SPEC-3).

### D2 — Warrants live inline; the specification-level list is generated

- Each requirement carries one fenced `warrants` YAML block naming its
  material authorities in CC-SPEC-2's six classes.
- `scripts/build_capability_1_spec_dependencies.py` generates the
  specification-level declaration, `GOVERNING-DEPENDENCIES.md`, as the union
  of those blocks (CC-IMPACT-1). No second hand-maintained list exists, so
  the two cannot drift.

### D3 — The spec authors the facet vocabulary; general rules govern values

- SDR-36 sites the seven-facet drafting in this specification (site a2).
- CAP1-REQ-030 defines each facet as a question plus its constituent facts.
- It mints **no** per-facet value enumerations. Values follow the general
  rules: the two-term rule (SDR-35), the closed Unknown reasons (RFC2-24), and
  the deferred posture for Mission-ready (SDR-36 rule 3). This avoids
  vocabulary no accepted clause warrants (CC-SPEC-6).

### D4 — Oracles are behavioral fixtures, never implementation probes

- Every oracle is phrased over served output — human view, machine answer,
  write records — against fixtures a checker controls. Any conforming
  implementation can be tested without naming one (CC-SPEC-5).
- A universally quantified requirement states its counterexample schema and
  sweep denominator instead of a single example (CC-SPEC-4's bounded-oracle
  rule; verification rule 9).

### D5 — Coverage ships as two tables plus one generated union

- `CAPABILITY-COVERAGE.md` places every declared Capability 1 obligation in
  exactly one of covered, lawfully out of scope or Unknown (CC-SPEC-11).
- `CONTRACT-COVERAGE.md` maps each applicable observable consequence of the
  accepted clauses to requirements (CC-SPEC-8). A consequence believed
  inapplicable renders **Unknown pending an owner-reviewed N/A**; the author
  mints no N/A on their own authority.

## Deliberately not designed here

- **How the behavior is built:** stack, storage, schema, process model,
  protocol.
- **`Mission-ready` semantics:** deferred with the Context/Mission waves; the
  spec fixes only its honest deferred posture.
- **The comprehension-walkthrough machinery** behind `Human-understandable`:
  the facet reads recorded evidence where it exists and renders `Unknown`
  otherwise.
- **Reconciliation computation:** V0 posture, uncomputed renders `Unknown`
  (SDR-12, SDR-34).

## Risks and trade-offs

- **Inline YAML inside requirement blocks** is unusual for OpenSpec. The
  pinned validator (1.9.0, `--strict`) accepts it, and the generator treats
  the fenced blocks as the single machine-readable home. If a future OpenSpec
  version objects, the blocks move: a mechanical transform, with identity
  kept by requirement ID.
- **Requirement-identity survival across edit and rename** is an RFC 0004
  adapter obligation, acknowledged in the proposal's Unknowns and not
  resolved here.

## Open questions this specification does not settle

- **The open decision queue stays open** (CC-SPEC-6): P-1's deferred C/D
  waves, P-21 (deterministic context) and the other open register rows. No
  requirement forecloses or presumes any of them.
- **No pending decision is a warrant.** The generated
  `GOVERNING-DEPENDENCIES.md` `decisions` section holds only recorded rulings
  (SDR-12, SDR-34, SDR-35, SDR-36 and the P-38 ruling), which is checkable
  mechanically.
- **`CAPABILITY-COVERAGE.md`** carries the obligation-level disposition; its
  U-01 names the one question this spec leaves open on purpose.
