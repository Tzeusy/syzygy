# Autonomy extension register

Where each future autonomy concept belongs and the earliest gate at which it
is needed (directive §8). Classification vocabulary: `foundational now` ·
`required before V1 autonomy` · `required before auto-merge/deploy` ·
`post-V1` · `research only`. **Deliberately not six more foundational
RFCs** — RFC 0010/0011 establish the extension points; everything below
rides those points or a later, narrower contract at its stated gate.

| Concept | Belongs to | Earliest gate | Classification |
|---|---|---|---|
| Goal and outcome measure | Mission objective + completion predicate (RFC10-4/10-7); measurable outcomes become OpenSpec scenarios | Mission Control surface specification | **foundational now** (the predicate slot exists; measure vocabulary at OpenSpec) |
| Hypothesis and experiment | A mission subtype whose completion predicate is "evidence gathered", not "shape converged"; no new authority plane | Post-V1 product work | **post-V1** |
| Agent/Fleet profile registry | RFC11-10 profiles + registry home (RFC 0011 §8 q2, with RFC 0010 §8 q3 store) | Before first routed fleet dispatch | **required before V1 autonomy** |
| Simulation / shadow mode / historical replay | Execution-profile class that materializes nothing (RFC5-18 family) + RFC 0002 evaluations over historical snapshots | Before granting any envelope above propose-only on a real project | **required before V1 autonomy** (shadow mode); replay tooling **post-V1** |
| Policy regression tests | Craft-and-care testing policy + guardrail-runtime conformance suite (RFC10-10 decisions as test fixtures) | With the guardrail runtime's V0 implementation | **required before V1 autonomy** |
| Mission checkpoint / rollback / compensation / resume | RFC10-7's checkpoint and recovery obligations (slot exists); concrete format at OpenSpec | Checkpoint/resume: **required before V1 autonomy**. Compensation/rollback of *external* effects: **required before auto-merge/deploy** | split as stated |
| Incident and lesson loop | RFC11-8 governed memory ("lessons derived from incidents") + Attention Item resolution records (RFC10-12) | First real incident; formal loop | **required before V1 autonomy** |
| Environment/toolchain capsule | Execution-profile contents (RFC5-20) — a capsule is a profile made reproducible | When merges/deploys are delegated (reproducibility becomes load-bearing at that point) | **required before auto-merge/deploy** |
| Durable-state capsule | Extends checkpoint obligations (RFC10-7) for long-lived missions | When missions outlive single sessions routinely | **post-V1** |
| Convergence/regeneration certification | The Genesis hypothesis (seed, unadopted); would need its own RFC + owner adoption | No gate scheduled | **research only** — must not be smuggled in via mission predicates |

**Honest deferrals.** Nothing above is silently begun: each `required
before …` row names the gate that blocks V1 autonomy or auto-merge/deploy
until it exists; `post-V1`/`research only` rows carry no obligation at all.
Any row that later proves to need contract-level authority (rather than
policy/OpenSpec shape) returns to the owner as a new narrow RFC proposal —
the register itself authorizes nothing.
