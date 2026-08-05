# Owner direction record — rev10 final pre-specification run

**Source:** `REV9-FINAL-PRESPEC-DIRECTIVE.md`, owner-supplied 2026-08-02.
This record restates the *settled* direction ("record, do not re-ask") so the
rework can cite it as owner authority. Each item cites its directive section.
These are owner rulings for this run; where one requires a doctrine amendment
or an acceptance act, that gate is still separately owner-held.

## OD-R10-1 — Mission Control exists, as platform capability (§1.1)

Syzygy gains a workspace-level **Mission Control** operator domain: humans set
objectives, constraints, budgets, and risk limits; agent fleets plan, execute,
verify, recover, and re-plan inside an approved envelope. It is **not** a
fourth project-specific truth surface and must not create a second
project-internal source of truth. Architecture contract: **one canonical
long-lived Syzygy control-plane service, one semantic API**; web UI, official
`syzygy` CLI, scripts, and an MCP (or equivalent) agent adapter are clients
seeing the same identities, evaluations, evidence, missions, attention items,
and policy results. Language, packaging, transport, and whether distribution
is literally one binary remain implementation choices — **not chosen in this
run** (stack boundary holds).

## OD-R10-2 — Human-triggered bounded autonomy (§1.2)

Doctrine's posture stands: not an unattended reconciler by default. A human
may deliberately trigger and approve a **bounded Mission** — one act
authorizing agents to plan, materialize, execute, verify, re-plan, and
recover without routine prompts until a terminal condition: objective
achieved; budget/time bound reached; risk exceeds delegated threshold;
protected/prohibited surface would be touched; unresolved contradiction or
genuine product choice appears; evidence cannot establish progress; recovery
becomes unsafe; pause/cancel/expiry. High-level human control, not silent
default autonomy. If doctrine needs the minimal clarification that
"human-triggered propagation may authorize a bounded mission rather than one
work item at a time," a **narrow amendment is drafted, never self-applied**
(draft: `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`, this workspace).

## OD-R10-3 — Context bloat is an architecture problem (§1.3)

The ~90k-word active RFC corpus is a material human- and LLM-maintainability
risk **now**, before acceptance turns it into a maintenance burden. An
active-contract extraction and compaction pass runs **before** RFC
acceptance. Optimization target, verbatim: "minimum complete governed context
required for one decision or work item, not minimum document count." More,
smaller, selectively loadable files are acceptable. Compaction targets
(acceptance targets, not doctrine): active corpus ~35,000–50,000 normative
words; modules ~2,000–6,000 words; no default-loaded module over ~7,000
without owner-facing justification and a context-load test; acceptance record
~3,000–5,000 words. Constraints may not be deleted or compressed into
machine-only language to hit the numbers.

## OD-R10-4 — Context Compiler is first-class (§1.4)

Every Mission, plan, work item, review, and agent run receives a **versioned,
digest-bound, task-specific context packet**. "Read all project
documentation" is not a lawful agent instruction. Deterministic
graph/applicability rules select mandatory context; inference may suggest
additions but never silently remove mandatory context. Raw chat history is
not canonical project memory; durable memory is accepted decisions, evidence,
summaries, lessons, mappings, governed artifacts.

## OD-R10-5 — Acceptance semantics repaired without weakening (§2)

The two-state model is adopted: **owner-adopted bootstrap act** (phrase +
digest + commit/tag; the human may govern development by it) vs
**Syzygy-verified effective act** (bootstrap act correlated through the
independent A1 audit mechanism). Until correlation exists, Syzygy must not
claim independent verification, provenance renders the gap honestly, and the
acceptance record must not equate a same-tree committed record with
independently verified effective status. **Preserved owner decision: git
commits or tags alone are never sufficient.** RFC 0005's machine-client
question closes or is explicitly scoped so the browser-vs-machine-client
contract and authentication requirement are firm enough to specify Mission
Control truthfully (credential technology may stay open).

## OD-R10-6 — RFC 0009 split ruling reversed (§4)

The rev9 "do not split" recommendation is **overruled by the owner**: context
bloat is a first-class concern and pre-acceptance is the least expensive
moment. RFC 0009 becomes an indexed contract package (`RFC-0009/` with README
index + modules), preserving one authoritative `RFC9-n` namespace, stated
clause ranges per module, deterministic lookup, citation preservation via the
index, no duplicated normative clauses. Other RFCs split only where reader
groups are genuinely distinct — no ceremonial file multiplication.

## OD-R10-7 — The gate for this package (§12)

One final owner gate over the compacted package:
`ACCEPT COMPACTED FOUNDATIONAL RFCS: <package-manifest-digest>`, with
`REWORK COMPACTED FOUNDATIONAL RFCS: <reason>` /
`REJECT COMPACTED FOUNDATIONAL RFCS: <reason>`. Topology, craft amendment,
and overview keep **separate gates**. Nothing adopts implicitly; the agent
does not execute any gate. The run ends at directive §14's exit condition
with the owner-judgment list returned.

## Standing boundaries reaffirmed (directive header)

Pre-OpenSpec, pre-Beads, pre-implementation, pre-stack. No application code,
no package scaffolds, no OpenSpec changesets, no Beads mutation, no
language/database/graph-store/framework/3D-engine/RPC/packaging selection, no
wholesale doctrine rewrite, no silent autonomy expansion.
