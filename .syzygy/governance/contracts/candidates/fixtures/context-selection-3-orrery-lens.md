# Context-selection fixture 3 — Orrery architecture-lens change

**Objective.** A governed work item: draft the specification delta for a
change to an Orrery lens (adjusting what an existing V0 lens encodes on a
reserved channel). Risk class: encoding-meaning change — touches the
channel registry class (RFC9-26, an RFC3-16(a) artifact by example list),
but this task drafts the proposal; no adoption act occurs inside it.

**Selection rule trace (RFC11-4).** Warrant names the lens →
`applies_to: orrery`, module `visual-grammar-and-lenses` + package README
(lens contract RFC9-31..35, channel contract RFC9-24..30). Lenses render
claim/Unknown states → RFC-0002 `rendering-vocabularies` + README. The
map's doctrine posture (VIS-7 trust floor, map scope amendment D1) →
`architecture.md`.

## Required context (mandatory, deterministic)

```
scripts/context_load.py rfcs/RFC-0009/README.md \
  rfcs/RFC-0009/visual-grammar-and-lenses.md rfcs/RFC-0002/README.md \
  rfcs/RFC-0002/rendering-vocabularies.md doctrine:architecture.md
```

Measured: **14,013 words ≈ 18,918 estimated tokens** — inside the 15–20k
working target.

## Omitted applicable candidates, with reasons

- RFC-0009 `semantic-geography` — geography/anchoring/layout are
  untouched by a channel-encoding change; its clauses are not in the
  warrant's set. `interaction-parity-and-release` — parity obligations
  bind the implementation phase; the drafted delta must route through
  OpenSpec anyway (RFC9-52, restated in the README the packet carries).
- RFC-0002 core/challenge/reconciliation — rendering vocabulary suffices;
  evaluation machinery is pinned by the packet's as-of.
- RFC-0003 governance-homes — the proposal does not perform the
  registry's owner act; when the adoption ceremony becomes the task, that
  packet loads it (fixture 4's shape).
- RFC-0001/0004/0005/0006/0007/0008/0010/0011, `security.md`, craft — no
  kernel, evidence, client, or work surface touched.

## Why no applicable constraint was lost

The channel contract, reserved palette, lens conformance clauses, and the
package phase rule are all in the mandatory set; the registry's
authorization-bearing character is stated inside RFC9-26 itself
(carried), with the deeper RFC3-16(a) machinery deferred to the adoption
task by the phase rule. Performance and motion bounds (RFC9-49..51)
live in the omitted module 3 and load on demand (the README's package map
names RFC9-49's rule; RFC9-50..51 sit beside it) — the omission is safe
because the fixture's warrant does not alter frame or motion budgets.

## Suggested inferred additions (provenance: index adjacency)

RFC-0009 `interaction-parity-and-release` (non-3D equivalence for the
changed encoding — needed at surface-spec authoring); RFC-0006 (drawer
disclosure of encoded facts).

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`096b5623b8b6d645…`.

**Selection: hand-authored golden selection. Measurement: mechanical.
Compiler implementation: absent.** `scripts/context_load.py` resolves a
path list it is handed and counts words; it has no notion of a task, a
warrant, a risk class, an `applies_to` value, or a dependency edge. The
selection above was made by a human and the trace is the reasoning that
produced it, written down — not a machine's output narrated afterwards.

*The `Compiler:`/`selection rules` line this fixture used to carry was
dropped rather than carried forward: there is no compiler, and
`rev10-fixtures` resolved to nothing in this repository — a version
identifier that names nothing is worse than none (the convention fixture 9
set). The digest and measurement above are written by
`scripts/build_budget_report.py` and independently recomputed by
`scripts/check_governance.py` CG-18; neither figure is transcribed.*

*Re-measured 2026-08-05b by `scripts/check_governance.py` CG-18, which recomputes the digest and the word count from the declared mandatory set rather than trusting the recorded figures. Previous: 14,134 words, digest `2e408eaf40278ca7…`. Selection unchanged; the movement is contract edits landing under a fixture that had no mechanical freshness check until now.*
