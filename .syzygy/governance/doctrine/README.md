# Heart and Soul — Doctrine

> **Status:** Adopted project doctrine — owner adoption `ADOPT DOCTRINE`, 2026-07-30.

## Amendment log

| Id | Date | What changed | Authority |
|---|---|---|---|
| D1 | 2026-08-01 | `architecture.md`, two sites (layout comment; `map/` definition bullet): the map's scope now reads "observed, intended, proposed, and historical system state" — historical rendering added unconditionally. | Owner decision D1, ratifying the packet at `_bootstrap/rfc-phase/DOCTRINE-AMENDMENT-MAP-HISTORICAL.md`; scope made unconditional by rev7 rework directive item A2 (not owner decision A2) |

This folder answers **WHY** Syzygy exists, what it believes, what it refuses to
be, and which constraints bind every downstream decision. It is constitutional,
not aspirational: every rule is stated so that a violation is recognizable.

## Glossary (read first)

- **Syzygy** — provisional codename for this project; literally, the
  astronomical alignment of three bodies — here: vision, specification, code.
  Adopting this doctrine ratifies Syzygy, Polaris, Trajectory, and Orrery as
  **working codenames only**; final product naming is a separate, later owner
  decision (architecture.md, Vocabulary).
- **Owner** — the single human accountable for a governed project's intent.
  Everywhere this doctrine says "human sign-off" or "consent," the owner is that
  human. (Multi-user operation is deferred; see v1.md.)
- **Governed project** — one or more repositories with exactly one
  **designated governance root** (the repository holding the project's single
  `openspec/**` + `.syzygy/**` plane) and one owner, explicitly brought under
  Syzygy observation; additional repositories are declared observed-source
  repositories, read-only to Syzygy unless separately onboarded, and every
  observed repository requires consent (architecture.md; security.md SEC-4).
- **`.syzygy/` and `openspec/`** — the exactly-two in-tree namespaces Syzygy
  writes directly in any governed project (vision.md VIS-5; architecture.md
  defines the `.syzygy/` layout: `governance/`, `intent/`, `work/`, `map/`,
  `cache/`, `local/`). Everything else Syzygy only reads, or affects through
  typed adapters.
- **Polaris / Trajectory / Orrery** — provisional codenames for Syzygy's three
  surfaces: intent and comprehension; gaps, work, and convergence; the
  observed/projected system twin (architecture.md).
- **OpenSpec** — the designated initial behavioral-specification substrate for
  `openspec/`; **Beads** — the designated initial work-scheduling substrate
  (issues, dependencies); **the `/th-*` skills and claude/codex CLIs** — the
  designated initial agent toolchain for workers and actuators. All substrate
  tools are designated initial realizations of roles, substitutable per
  architecture.md; nothing here claims an integration already exists.
- **Rule identifiers** — vision.md's non-negotiable rules are `VIS-1`–`VIS-7`;
  security.md's are `SEC-1`–`SEC-5`. The namespaces are deliberately disjoint
  from the product lifecycle stages `V0`/`V1` (v1.md), so a rule citation can
  never be read as a release stage. Identifiers are stable after adoption:
  amend text in place; retire rather than renumber.

## Reading order

1. **[vision.md](vision.md)** — the owner's transformation, the thesis, what
   Syzygy is and is not, rules VIS-1–VIS-7, the regeneration north star, the
   fleet observability mandate, and what success and failure mean.
2. **[v1.md](v1.md)** — the scope boundary: what V0 ships (and in what
   increments), what V1 adds, deferrals with rationale, platform and audience,
   and the stage-labeled success tests with their evidence artifacts.
3. **[architecture.md](architecture.md)** — constitutional structure: governed
   projects and the orthogonal plane, typed authority, contradictions vs gaps,
   the Project Genome and convergence, snapshots and the loop, one kernel and
   three surfaces, and the frozen vocabulary.
4. **[trust-and-evidence.md](trust-and-evidence.md)** — claims, evidence,
   warrants, staleness, the deterministic/inferred seam, and the normative
   statement of the trust floor.
5. **[security.md](security.md)** — the trust model: rules SEC-1–SEC-5 on
   exposure, data egress, executing observed code, write blast radius, and
   secrets.

## Scope boundary

- Engineering standards, review discipline, testing rules, provenance formats →
  the quality and evidence policy in `.syzygy/governance/` (not here).
- Technical contracts (graph schemas, adjudication and certificate semantics,
  execution profiles, deeper `.syzygy/**` schemas) → accepted contracts (RFCs)
  in `.syzygy/governance/` (not here).
- Required observable behavior → `openspec/`. Component placement → declared
  topology in `.syzygy/governance/`.

Doctrine is slow to change. Every amendment is owner-adopted, and downstream
artifacts must be re-checked for alignment when it changes.
