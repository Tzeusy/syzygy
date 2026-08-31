---
id: RFC-0011
title: Context Compiler — packet identity, provenance, governed memory, and profiles
status_source: owner-act-record
module: packet-identity-provenance-and-memory
clauses: "RFC11-1..RFC11-3, RFC11-5..RFC11-10, RFC11-12 (non-contiguous — see the package clause map)"
governs: [context-packets, governed-memory, agent-profiles, phase-boundary]
applies_to: [mission-control, context, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010]
tags: [context, provenance, memory, immutability, unknown-fails-closed]
---

# RFC 0011 — Context Compiler: packet identity, provenance, governed memory, and profiles

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this
contract binds nothing.

**Package:** module 1 of 2 of the RFC 0011 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.

**Serves:** VIS-7/trust floor (what an agent saw is a provable fact, not a
guess); SEC-2 (deny-by-default context/tool grants); owner direction
OD-R10-3/OD-R10-4.

## 1. Scope of this module

What a Context Packet **is** and what may be trusted about it: identity and
immutability (RFC11-1..3); the mandatory/suggested distinction (RFC11-5);
the incomplete-is-Unknown rule (RFC11-6); the no-second-truth-store rule
(RFC11-7); governed memory (RFC11-8..9); agent/model profiles (RFC11-10);
and the binding phase rule (RFC11-12), which binds the whole package. This
module does **not** claim deterministic selection is solved; how the
mandatory set is derived is module 2's subject.

## 2. The contract

### 2.1 Context packet identity

**RFC11-1.** A **Context Packet** is a versioned, **immutable**,
digest-bound execution artifact, minted per compiled run. It identifies, at
minimum: the **objective** (mission, plan, work item, review, or query task
it serves — by stable identity); the **project and workspace identity**; the
**selected evaluation and as-of instant** (RFC 0002's temporal machinery);
the **exact doctrine rules** included, by identifier; the **exact RFC
clauses**, by clause ID at stated revision/digest; the **exact OpenSpec
requirements and scenarios**, once such exist; the **topology and craft
policies** included; the **work warrant and autonomy envelope** governing
the run (RFC10-7 — the envelope is a mandatory input for any
mission-spawned run); relevant **code, test, and evidence references**, by
identity; the **active decisions, contradictions, challenges, and Unknowns**
in scope; the **allowed tools and permissions** (deny-by-default, within
the envelope); the **context-compiler and adapter versions**; the
**explicitly omitted candidate context, each with its reason**; and the
packet's **final digest**. A packet **reports** the envelope and
permissions it was compiled under; it is never itself an authorization
source — enforcement re-derives every permission from the envelope and its
act provenance at the choke point (RFC10-8, RFC3-16(a)); whoever mints
packets grants nothing.

**RFC11-2.** The packet digest is part of every resulting **Execution
Record** (RFC8-18..RFC8-20 / RFC 0002 evidence): an execution record for a compiled
run without its packet digest is incomplete evidence. Amending context
mid-run mints a **new packet version** (with its own digest, linked to its
predecessor) — packets are never edited in place, and the record binds every
packet version the run consumed.

**RFC11-3.** For governed runs — any run under a mission, work warrant, or
review charter — a context packet is **required**: instructing an agent to
"read all project documentation," or dispatching it with no packet, is a
violation, not a fallback. (Un-governed interactive exploration by a human
is outside this clause; the moment its output feeds a governed act, that act
needs a packet.)

### 2.2 What the packet must represent about its own completeness

**RFC11-5.** Inference (model judgment, semantic retrieval) **may add
suggested context, with provenance marking it suggested and by what**; it
may **never suppress, demote, or replace** mandatory deterministic context.
A packet distinguishes its mandatory core from its suggested additions.

**RFC11-6.** **Incomplete is Unknown, and Unknown blocks when policy says
complete.** If required context cannot be determined, conflicts internally
(two applicable rules contradict — RFC 0002's contradiction machinery), is
stale against the selected evaluation, or is itself Unknown, the packet is
marked **incomplete/Unknown with the gap named**, and **by default the run
does not launch** — the condition escalates (RFC10-12) rather than
proceeding on silently thinned context. Proceeding on disclosed-incomplete
context is lawful only under an **explicit, owner-visible relaxation** in
the governing policy or envelope — never an unstated default (the
fail-closed posture of RFC5-14, RFC5-16, and SEC-5 applies here too).
Staleness and contradiction are disclosed *inside* the packet even where a
relaxation permits proceeding.

**RFC11-7.** **No second truth store.** Selection metadata is present in, or
deterministically derived from, the active governed artifacts themselves;
generated indexes, embeddings, and retrieval structures are rebuildable
projections. A hand-maintained metadata sidecar that can drift from the
artifacts is a violation of this clause.

### 2.3 Governed memory

**RFC11-8.** **Raw chat history is not canonical project memory.** Raw
prompts, private chain-of-thought, and chat transcripts are never canonical
memory and are never mandatory context. Durable project memory consists of
governed artifacts: accepted decisions; evidence; structured run summaries;
lessons derived from incidents; mappings and supersession records; and
approved contextual notes — each identified, provenance-labeled
([Observed]/[Inferred]/[Unknown] discipline included), and governed by its
home's contract. Promotion from transcript to memory is an explicit,
attributable act, not an ambient side effect. Until the owner rules §8 q3,
promotion is **propose-only**: a machine principal proposes, a human act
promotes. A memory artifact that *interprets* an envelope, gate, or
prohibited surface — rather than recording facts — is authorization-bearing
under RFC3-16(a): without owner-act provenance it binds nothing and never
enters mandatory context as an interpretation.

**RFC11-9.** **Retention and privacy boundaries** (no storage engine chosen
here): governed memory lives in governed homes (RFC 0003 discipline);
secret material never enters packets or memory (SEC-5, RFC5-16/17); any
packet content crossing an egress boundary (e.g. to a model provider) is
subject to the egress-consent gate (RFC5-14/15) — a packet is not a consent
loophole; retention/deletion of non-canonical raw material (transcripts,
scratch) is a declared policy, while canonical memory follows its home's
lifecycle (RFC3-16 category lifecycles), never silent deletion.

### 2.4 Agent and model profiles

**RFC11-10.** Work routing may consult a minimal **agent/model profile** —
an optional extension identifying, at most need: supported tools and skills;
data/egress permissions; task and risk classes served; context capacity;
cost and latency class; historical evidence of quality (as identified
evidence, not reputation prose); independence requirements (for review
roles — the fresh-context property is a profile fact); and fallback order.
Profiles are versioned, and **no current model or provider name is
hard-coded as permanent semantics** — names are data in profile instances,
never constants in contracts. A profile can narrow what reaches an agent
(capacity, permissions); it can never widen an envelope (RFC10-8). Profile
fields that *satisfy an envelope-required gate* — independence,
permissions, risk classes served — are authorization-bearing under
RFC3-16(a): they satisfy the gate only when backed by owner-act provenance
or identified evidence; a self-asserted field **fails closed** for gate
satisfaction and the gate stands unsatisfied.

### 2.5 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC11-12.** This contract schedules nothing: **it is not a specification
of record from which implementation work may be scheduled**. No
implementation work for user-observable Context Compiler behavior — packet
inspection views, CLI commands, API endpoints, compiler diagnostics,
omission reports — may be scheduled solely from this RFC. Before
implementation, every observable consequence either maps to an approved
OpenSpec requirement and scenario in the governance root's `openspec/**`
plane, or carries a reviewed N/A judgment proving it purely structural
with no independently testable behavior. At surface specification a
clause-to-requirement coverage matrix over RFC11-1..RFC11-12 is produced —
**that matrix is review material, never authority**. This clause creates
no OpenSpec content now (none may exist during bootstrap). (Shape-parallel
with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16.)

## 8. Owner questions

*Package numbering; question numbers never shift. Full package index:
`README.md` §8.*

2. **Profile registry home — OPEN.** Where agent/model profiles live
   (workspace governance store vs project home) — proposed at surface
   specification alongside RFC 0010 §8 q3.
3. **Promotion act granularity — OPEN.** Is transcript-to-memory promotion
   (RFC11-8) always an explicit human act, or may a governed summarizer
   propose promotions that a human batch-approves? (Interacts with VIS-4;
   default until ruled: propose-only.)

---

*End of RFC 0011 module 1. Clauses RFC11-1 … RFC11-3, RFC11-5 … RFC11-10,
RFC11-12 — non-contiguous by design; the package README's clause map is the
lookup authority. Nothing merged, nothing retired.*
