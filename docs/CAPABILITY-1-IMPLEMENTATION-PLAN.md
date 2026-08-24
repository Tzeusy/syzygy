# Capability 1 implementation plan

> **Implementation guidance, never behavioral authority** (the
> authorization act's own limb). Required behavior is owned by the
> adopted specification
> (`openspec/changes/project-registration-and-honest-shape-visibility/`,
> adopted 2026-08-20 at exact digests). Authorized by
> `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`
> (2026-08-21); bounded by the P-35 operating constraints and the
> P-45/A6 envelope (2h/week owner attention, $200/mo, 2–3 workstreams).
> Scope: **Capability 1 only** — local development, tests, and a local
> demonstration; no production deployment, no external onboarding.

## Selected stack, with rationale

**TypeScript on Node.js (≥22.15 — raised from ≥20 on 2026-08-23: Node 20
left maintenance 2026-04), npm workspaces, Vitest, and the `yaml`
package pinned exact.** `[Inferred — one defensible choice, reasoning
stated so the owner can disagree with the reasoning]`

- **One language, one fact model, both channels.** The spec's hardest
  standing obligations are parity ones (CAP1-REQ-040…046: identical
  fact sets to human view and machine answer; a parity disagreement is
  a defect). One TypeScript fact model, serialized to the machine plane
  as JSON and rendered server-side to HTML for the human view, makes
  the two channels share their source by construction instead of by
  discipline.
- **Closed vocabularies as types.** `Unknown`/`Gap`/`satisfied`, the
  twelve reasons, the four-value discoverability domain, and the
  Mission-ready posture coordinates are literal union types — the
  verbatim-spelling oracles (REQ-013/030/034/036/050) get compile-time
  teeth plus runtime tests.
- **The YAML dialect is a conformance item** (RFC3-1; REQ-001…006): one
  parser (`yaml`), pinned at an exact version with its options
  committed in one module, becomes the fixed dialect.
- **No database.** Capability 1 stores declarations, consent records,
  and evaluations as files under the observed repository and the
  daemon's local state directory; choosing no database avoids a
  normative-data-contract escalation trigger entirely and fits
  local-first doctrine. Revisit only when a later capability needs one.
- **Doctrine fit.** The platform commitment (local-first daemon +
  browser app) is doctrine-level; Node serves both from one process.
  The Capability 1 human view is **server-rendered HTML** — a browser
  *app* framework is Polaris-family work, not this capability's.

## Selected repository layout

```text
packages/cap1-core/         pure domain, no I/O: declaration parse/validate,
                            consent & coverage, evaluation identity, the seven
                            facets, fact sets, reasons, discoverability
packages/cap1-daemon/       the daemon: filesystem observation, evaluation
                            orchestration, machine-queryable plane (HTTP+JSON),
                            server-rendered human views, credential admission
packages/cap1-conformance/  the requirement-keyed verification suite: one
                            module per CAP1-REQ-NNN, implementing that
                            requirement's Case/Oracle/Falsifier as tests
apps/syzygy/                the runnable entry point (config, startup, local
                            demo wiring)
docs/                       implementation guidance and retained evidence
package.json, tsconfig.base.json, vitest.config.ts       root manifests
```

`openspec/**` and `.syzygy/**` stay the governed plane — no
implementation file lands there. The daemon's own runtime writes are
themselves specified by CAP1-REQ-023/053/061 and tested externally
(harness-level filesystem diff), exactly as the spec's oracles demand.

## Initial implementation slices → CAP1 requirement IDs

| Slice | Content | Requirements |
|---|---|---|
| S0 | Workspace scaffold, toolchain, CI-less local test harness, fact-model and vocabulary types | (foundations for all; no requirement claimed implemented) |
| S1 | Declaration reading, validation, registration; root designation; named failures; determinism | CAP1-REQ-001, 002, 003, 004, 005, 006 |
| S2 | Consent records, coverage boundary, credential-classed machine retrieval, per-repository coverage results | CAP1-REQ-010, 011, 012, 013, 014, 015, 016 |
| S3 | Evaluation identity, stamps, staleness, stable identities, proposed-vs-current | CAP1-REQ-042, 060, 062, 063 (with 005 from S1) |
| S4 | The seven shape answers, independence, no-rollup, Unknown/Gap, deferred postures | CAP1-REQ-030, 031, 032, 033, 034, 035, 036, 037, 038 |
| S5 | "Why this answer?", human/machine parity, inferred-vs-observed, authority exposure | CAP1-REQ-040, 041, 043, 044, 045, 046 |
| S6 | Human entry serving + honest degradation; discoverability findings + link proposal | CAP1-REQ-020, 021, 022, 023, 050, 051, 052, 053 |
| S7 | Write-boundary hardening, non-visual distinctions, local demonstration end-to-end | CAP1-REQ-061, 064 (+ integration over all) |

Order: S0 → S1 → S2 → S3 → S4 → S5 → S6 → S7 (S3 may overlap S2). A
requirement is **implemented** only when its S-slice lands *and* its
conformance module passes; partial slices are never reported as done.

## Testing and retained evidence

- **`packages/cap1-conformance` is requirement-keyed**: one module per
  CAP1-REQ-NNN, its tests derived from that requirement's stated Case,
  Oracle, and Falsifier — including the sweep denominators for
  invariants/prohibitions. Unknown, stale, absent, and failure paths
  are first-class cases, per the act and VIS-2.
- Write-boundary requirements (023/053/061) are verified by
  **harness-external observation** (filesystem snapshot diff around the
  operation), never by the daemon's self-report — as the spec's own
  oracle-independence lines demand.
- **Defect rule**: a fix lands with its reproducing test, or the
  infeasibility is recorded in the fix's Beads issue.
- **Retained evidence**: each slice's review gate records the exact
  commit, the `vitest run` transcript, and the conformance-module pass
  list in its Beads issue before the issue closes; claims without a
  resolvable record are not made (`[Observed]`/`[Inferred]` discipline
  applies to implementation status too).

## Risk and review classes

| Class | What falls in it | Review bar |
|---|---|---|
| Risk-floor | write boundary (REQ-023/053/061), credential admission and consent enforcement (REQ-011/015/016, SEC-1/2/4), parity engine (REQ-041/043), YAML dialect module | **Independent review required** (fresh-context reviewer, not the author), th-engineering bar |
| Ordinary | facet computation, rendering, explanation drawers, discoverability | Standard review; th-engineering subskills as applicable |
| Trivial | tooling, formatting, non-semantic refactors | Author-verified; split before oversized (CC-REV) |

## Escalation back to the owner (from the act, restated)

A new owner act is required before any choice that: changes doctrine or
an accepted contract; needs a spec amendment; changes security, privacy,
retention, or a normative data contract; exceeds P-35/A6; or expands
beyond Capability 1. Everything else in stack/layout is settled by this
plan and its ordinary revisions.
