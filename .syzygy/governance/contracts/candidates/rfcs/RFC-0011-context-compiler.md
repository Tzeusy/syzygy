---
id: RFC-0011
title: Context Compiler and Governed Context Packets
status_source: owner-act-record
clauses: "RFC11-1..RFC11-12"
governs: [context-packets, context-selection, governed-memory, agent-profiles]
applies_to: [mission-control, context, all-surfaces, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0010]
provides_to: []
tags: [context, provenance, memory, selection, agents]
---

# RFC 0011 — Context Compiler and Governed Context Packets

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until
the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Serves:** VIS-7/trust floor (what an agent saw is a provable fact, not a
guess); SEC-2 (deny-by-default context/tool grants); owner direction
OD-R10-3/OD-R10-4 (recorded in the rev10 owner-direction record, a
bootstrap process artifact retained with the delivery packet). New at
rev10 — no rev9 predecessor.

## 0. Reader's summary (non-normative)

No agent is ever told to "read all project documentation." Every governed
run — mission, plan, work item, review, query task — receives a **Context
Packet**: a versioned, immutable, digest-bound artifact stating exactly
which doctrine rules, contract clauses, requirements, policies, evidence,
decisions, and permissions the agent saw, what applicable material was
omitted and why, and under which evaluation instant. Mandatory context is
selected **deterministically** from graph and applicability rules; inference
may suggest more, never silently remove. The packet digest lands in the
resulting execution record, so "what did the agent know?" is answerable
forever. Chat transcripts are not project memory; durable memory is
governed artifacts.

## 1. Summary

This contract fixes: packet identity and immutability (RFC11-1..3);
deterministic selection semantics and the incompleteness rule (RFC11-4..7);
governed memory boundaries (RFC11-8..9); the minimal agent/model profile for
routing (RFC11-10); the context-budget posture (RFC11-11); and the OpenSpec
phase rule (RFC11-12). Storage engines, retrieval technology, and the exact
token-budget number are explicitly not chosen here.

## 2. Motivation and doctrine grounding

[Observed] The rev9 corpus offered no answer to "which context did this
agent receive?" — the packet gap named at rev10
adversarial finding F7 (a bootstrap process record retained with the
delivery packet) — and whole-corpus loading was the only
safe instruction, which OD-R10-3 rules an architecture problem. [Inferred]
Context selection is a **provenance** problem, not a convenience problem: an
execution record whose inputs are unrecorded cannot support the trust floor
(VIS-7), and an agent that silently dropped a constraint is indistinguishable
from one never given it. The optimization target, verbatim from the owner:
"minimum complete governed context required for one decision or work item,
not minimum document count."

## 3. The contract

### 3.1 Context packet identity

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

### 3.2 Selection semantics

**RFC11-4.** **Mandatory context is selected deterministically** — same
inputs, same selection — from, at minimum: stable entity and relation
identities in the objective's scope; the work/mission warrant; affected
capabilities and components; contract dependencies (`depends_on` /
`provides_to`); explicit `applies_to` and clause-level metadata (the
contract-index projection — a rebuildable RFC11-7 projection of the
governed artifacts' own front matter and clause text); the declared risk
and change class; and the active state/evaluation. The selection rule set
is versioned with the compiler (RFC11-1's version identity). The mandatory
set always includes the **governing phase-rule clause of every selected
contract** (the module or README text carrying it) — no lawful packet
omits the boundary rule of a contract it loads. Before selecting from any
generated projection, the compiler **verifies the projection regenerates
faithfully from the governed artifacts** (RFC11-7); selection from a stale
or unfaithful projection is a violation, and the packet records the
projection verification it performed.

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

### 3.3 Governed memory

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

### 3.4 Agent and model profiles

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

### 3.5 Context budgets

**RFC11-11.** Packets carry a **size estimate** (words/tokens) and the
compiler enforces the governing policy's budget posture: a normal bounded
implementation task should receive a packet well below whole-corpus size,
with sharding or explicit exception (owner-visible, reasoned) when risk
genuinely requires more. [Inferred] The concrete numeric target is a policy
default, not doctrine — it must not be frozen into contract text without an
owner act; the working figure and its test evidence live in the rev10
context-load map and context-selection fixtures (delivery-packet evidence
artifacts, not part of this contract), and its permanent custody is §8 q1.
What binds here: exceeding the posture is a disclosed, reasoned event,
never silent; and budget pressure never justifies dropping mandatory
context (RFC11-5) — the lawful responses are sharding, narrowing the
objective, or escalating. Sharding has a **non-shardable core**: every
shard carries the envelope in full, the prohibited and human-only
surfaces, the applicable doctrine rules, and the governing phase rules
(RFC11-4) — a shard from which any of these is absent is not a lawful
packet.

### 3.6 Authority boundary at the OpenSpec seam (binding phase rule)

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

## 4. Violation cases

1. *(RFC11-3)* A fleet worker is dispatched with "read `.syzygy/` and the
   RFCs, then implement" — no packet, no omission accounting.
2. *(RFC11-5)* A retrieval layer ranks a mandatory doctrine rule below its
   cutoff and drops it; the packet shows no omission because "the selector
   never saw it."
3. *(RFC11-2)* An execution record says "context: latest docs" with no
   packet digest; six weeks later nobody can establish which revision of the
   envelope the agent saw.
4. *(RFC11-6)* Two applicable policies contradict; the compiler picks the
   newer one silently and the packet renders complete.
5. *(RFC11-8)* A planning chat's conclusions are cited as project authority
   ("as agreed in the transcript") without promotion to a governed decision.
6. *(RFC11-9)* A packet containing observed-project code is sent to a model
   provider under a consent covering only metadata.
7. *(RFC11-10)* A review is routed to an agent whose profile lacks the
   independence property the review class requires, because fallback order
   ignored it.

## 5. Integration

- **RFC 0001/0002:** packets pin evaluations and as-of instants; packet
  facts and omissions are identified; Unknown is first-class (RFC11-6).
- **RFC 0003:** packet and memory homes follow governance-home discipline;
  the contract-index projection (RFC11-7) is rebuildable, never
  authoritative; effective-status inputs come from owner-act records under
  the RFC3-16(c) two-state model — a packet states correlation gaps
  honestly.
- **RFC 0004:** evidence references enter packets by identity; capture
  cadence limits are disclosed as staleness, not hidden.
- **RFC 0005:** packets respect scopes (RFC5-6), egress consent (RFC5-14),
  and secret exclusion (RFC5-16/17); compiler acts are attributable
  (RFC5-25).
- **RFC 0006:** packet contents are queryable through the same semantic API
  with human/machine parity (RFC6-13/RFC6-14).
- **RFC 0010:** the envelope is a mandatory packet input; incomplete-context
  escalation flows through Attention Items; profiles never widen envelopes.

## 6. Alternatives considered (summary; this contract is new at rev10 and has no history file)

Pure retrieval ("embed everything, let relevance decide") — rejected:
non-deterministic mandatory selection cannot support the trust floor.
Whole-corpus loading as the safe default — rejected by OD-R10-3. Manual
per-task reading lists — rejected: hand-maintained selection is the drift
RFC11-7 forbids.

## 7. Deliberately deferred

Storage and retrieval technology; embedding/index formats; the numeric
token budget (policy default, evidenced in the load map); packet transport;
compiler scheduling; profile registry home.

## 8. Open questions for acceptance

1. **Budget figure custody.** The working target (well below whole-corpus;
   evidenced in the rev10 load map) is a policy default — does the owner want
   it recorded as a named policy artifact at V0, or left to the OpenSpec
   phase?
2. **Profile registry home.** Where agent/model profiles live (workspace
   governance store vs project home) — proposed at surface specification
   alongside RFC 0010 §8 q3.
3. **Promotion act granularity.** Is transcript-to-memory promotion
   (RFC11-8) always an explicit human act, or may a governed summarizer
   propose promotions that a human batch-approves? (Interacts with VIS-4;
   default until ruled: propose-only.)

---

*End of contract. Clauses RFC11-1..RFC11-12; no gaps, no retired numbers.*
