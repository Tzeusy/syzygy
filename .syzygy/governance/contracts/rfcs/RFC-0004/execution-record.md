---
id: RFC-0004
title: Observation Sources and Evidence — the Execution Record and the minimum run envelope
status_source: owner-act-record
module: execution-record
clauses: RFC4-18..RFC4-21 (no gaps, no retirements, no merges)
governs: [execution-record, run-envelope, run-identity, derivation-collision, enrichment, cost-and-token-semantics, partial-aggregates]
applies_to: [kernel, trajectory]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005]
tags: [evidence, execution-plane, run-envelope, unknown-never-zero, sdr-5, sdr-6, sdr-8, sdr-31, sdr-32]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 3 of 4 of the RFC 0004 contract package. Index, clause map,
lookup rule, package-level integration and deferrals: `README.md`. Rationale,
amendment history, alternatives, and answered §8 questions:
`../../history/RFC-0004-history.md`.

**Serves:** VIS-1, VIS-2, VIS-6; SEC-2, SEC-5; trust-and-evidence.md (the
evidence definition; durability and integrity-verifiability). Implements
**owner rulings** SDR-5, SDR-6, SDR-8, SDR-31, SDR-32, and resolves the run
envelope schema half of SDR §5 question 7.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what Syzygy durably records about a fleet run**: the
Execution Record's classification as an Evidence kind rather than a new
doctrine class (RFC4-18), the minimum durable run envelope field-by-field
(RFC4-19), what enrichment may never be required to add (RFC4-20), and the
model/timing/token/cost semantics under Unknown-never-zero (RFC4-21). Read it
to answer: *what must this record contain, and what may it never invent?*

The envelope table in RFC4-19 is the single place the minimum content is
stated — RFC 0005's own run-envelope obligations (profile identity, RFC5-18(e);
policy-violation recording, RFC5-21) are carried here as named rows rather than
cross-referenced, so no reader has to assemble the envelope from two contracts.
Two rules bind hardest: an absent value renders **Unknown, never zero**, and a
**derivation collision is disclosed, never collapsed** — a silent single record
is a violation.

Observers producing these records must satisfy the general contract (module 1);
the gate tiers the envelope's gate rows carry are defined in module 2
(RFC4-13); the `reduced-fidelity` causes it cites are the closed list in
module 4 (RFC4-24).

---

## 3. The contract

Clauses are numbered `RFC4-n` for stable citation. Amend in place; retire
rather than renumber.

### 3.4 The Execution Record and the minimum run envelope

**RFC4-18 — Classification (SDR-8).** An **Execution Record** is an **Evidence
artifact** — durable, identified, integrity-verifiable, immutable once
recorded — residing under `.syzygy/work/**`. It is a *kind* of the existing
Evidence class (RFC1-5); **no new doctrine-level evidence class exists**. It
is execution-plane evidence (RFC1-22): it may support claims about what the
fleet did, and it may never satisfy a desired-state claim — work is never
proof intent is satisfied. It is captured historical evidence and, like all
evidence, is not required to be rebuildable from a source that no longer
exists; observation records cite it (RFC2-1 item 6).

**RFC4-19 — The minimum durable run envelope.** One Execution Record per
execution run (RFC1-5), including Syzygy's own propagation acts. Field
classes: **R** = required (record inadmissible without it), **EA** =
`expected-where-available` — expected wherever the source can supply it,
**Unknown-with-reason otherwise** (never zero, never defaulted) — and **O** =
optional enrichment.

| Field | Class | Semantics |
|---|---|---|
| record identity + envelope schema version | R | Deterministically derived; schema version is RFC 0003's to physically encode |
| capture metadata | R | Capture instant; capturing observer identity + version; references to the source artifacts the record was derived from (RFC4-3) |
| project identity | R | The governed project (never a filesystem path) |
| run identity | R | Toolchain-emitted where it exists; otherwise **adapter-derived** deterministically from durable joins (work item, branch, dispatch-distinguishing facts), labeled `derived` — the two origins are queryably distinct. **Derivation collision must be detected and disclosed:** where the derivation inputs cannot distinguish two dispatches, the affected records render `reduced-fidelity` with cause `indistinguishable-runs` (RFC4-24) and the **run count renders Unknown** — never a silent single record (RFC4-20) |
| parent run identity | EA | Null at the root; what makes nested spans truthful rather than guessed |
| work item identity + substrate alias | R | Substrate-neutral identity primary; `bead_id` as alias (RFC4-6). Unattributable runs are admissible only rendered as unattributed execution noise, never dropped [Observed: vision.md anchoring mandate] |
| warrant reference | EA | The materialization record identity, and through it the pinned intent revision and resolvable spec anchor (SDR-32). Absent or unresolvable → Unknown, never rejection |
| run start / end instants | EA | Toolchain-recorded where available; else derivation bounds (first/last commit, report instants) labeled `reduced-fidelity` |
| runtime + model | EA | Provider-qualified or not at all [Observed]; absent → Unknown |
| worktree | O | Descriptive, machine-local; never identity-bearing |
| branch + base revision | EA | The convention-grade correlation join, with its basis declared (RFC4-22) |
| commits produced | EA | SHA set where reachable at capture; post-squash → PR-granularity, `reduced-fidelity` (RFC4-11) |
| PR identity + merge-fact reference | EA | From the hosting sub-adapter, never from scheduler closure |
| terminal outcome + blocker set | R | The toolchain's closed report-status vocabulary, transmitted verbatim with the substrate qualified; blockers structured as reported. Where no report exists to transmit — a vanished worker — the field carries the Syzygy-side value `unknown-terminal` with the reason, so the record stays admissible and the run is never dropped (§8 q2's proposed answer, drafted for ratification at the act; composes with this table's never-dropped rule and RFC4-16(3)) |
| gate outcomes + artifact references | EA | Each with its RFC2-25 tier; `gate-backed` only under **both** RFC4-13 predicates — a retained resolvable artifact bound to the exact revision (SDR-9) **and** a qualifying provenance route; unverifiable origin caps at `report-fact` |
| tokens / cost | EA | Per RFC4-21; absent → Unknown, never zero (SDR-6) |
| **profile identity + version** | EA | The execution profile the run launched under, as RFC5-18(e) requires; absent for runs Syzygy did not launch, rendered Unknown-with-reason, never blank. A run Syzygy *did* launch with no recoverable profile identity is not attributable and its outputs cannot be `gate-backed` (RFC4-13 route 1) |
| **policy-violation flags** | EA | Whether the run violated its declared profile policy (undeclared egress, write outside scope, resource bound exceeded, out-of-purpose credential use), as RFC5-21 requires recorded on the Execution record; a violating run terminates and its outputs cap at `report-fact`. Absent → Unknown-with-reason, never read as "no violation" |
| prose fields (summary, reasons) | O | Admitted only through **the observing project's** declared secret-detection policy (SEC-5; RFC3-30); unclassifiable content excluded, exclusion rendered. Prompt/transcript bodies never enter; a prompt hash may — the authority for what may be *stored* is **SEC-5 and RFC5-17** (screening; hash-not-body provenance), not SEC-2, which governs egress |

**RFC4-20 — Enrichment is explicitly non-required.** Fine-grained heartbeats,
nested tool events, phase transitions, per-span telemetry, and streaming
capture are **optional enrichment**: their absence never blocks a record,
never degrades the record below its envelope, and no kernel or surface
behavior may require them (SDR-31; SDR-5 keeps live streaming and control
deferred entirely). Multiple runs against one work item are distinct records —
redispatches and attempts are countable only from records, never inferred from
a mutation trail.

**Derivation collision is detected and disclosed, never collapsed.** Where run
identity is adapter-derived (RFC4-19) and the derivation inputs cannot
distinguish two genuine dispatches — a redispatch after a failed attempt, an
owner re-run on the same work item and branch, with the substrate recording no
dispatch-distinguishing fact — deterministic identity is by construction
non-unique and the records would otherwise collapse into one. The adapter must
instead emit the affected records at `reduced-fidelity` with cause
**`indistinguishable-runs`** (RFC4-24) and render the **run count for that
work item Unknown**. **A silent single record is a violation.** [Inferred]
This is SDR-6's Unknown-never-zero generalized to counts. The safeguard is
normative regardless of how §8 q1 is ruled — under austerity the identity
itself renders Unknown, and this count obligation is what stops the austere
form from silently under-joining either (owner decision **B11**: derive, and
disclose collisions).

**RFC4-21 — Model, timing, token, and cost semantics.** Values come only from
runtime-reported or toolchain-recorded facts captured as evidence; a cost
computed from token counts and a rate table is **Inferred** (rate tables
drift) and labeled with its derivation [Observed]. Absent values render
Unknown, never zero (SDR-6). **Partial aggregates are disclosed**: any sum,
average, or account over runs where some values are Unknown must state its
coverage ("cost known for n of m runs") and must never render as a complete
total — an undisclosed partial aggregate is the zero-fallacy at portfolio
scale. Cost measures stay independent; no composite "effort" number. Event
instants are execution facts, distinct from any evaluation's as-of instant;
they never alter a status outside a new identified evaluation.

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.*

9. *(RFC4-19/21)* A run record with no cost data renders `$0.00`; a portfolio
   cost total sums twelve known and eight Unknown runs without disclosing
   coverage; **or a redispatched work item shows "1 run" because both attempts
   derived the same identity and no `indistinguishable-runs` label was
   emitted.**

---

## 5. Integration (module-local)

**Relies on RFC 0001:** the Evidence and execution-run entity classes (RFC1-5)
this record is a kind of, and the execution-plane boundary (RFC1-22) that stops
it satisfying a desired-state claim. **On RFC 0002:** the observation record
that cites it (RFC2-1 item 6) and the tier registry (RFC2-25) its gate rows
carry. **On RFC 0003:** the physical encoding of the envelope, and the RFC3-30
secret-detection policy the prose-field row admits content through. **On
RFC 0005:** profile identity and version (RFC5-18(e)), policy-violation
recording (RFC5-21), and the storage authority for prose fields (RFC5-17).

**Provides to RFC 0003:** the run-envelope semantics it must physically encode.
**To RFC 0005:** the single stated home of the envelope's minimum content.
**To RFC 0008:** the records from which redispatches and attempts are counted —
never inferred from a mutation trail. **To RFC 0011:** the evidence identity and
capture provenance a context packet binds against.

---

## 8. Owner questions

*Package numbering; answered items keep their number and their reasoning is in
`../../history/RFC-0004-history.md` §8. Full package index: `README.md` §8.*

1. **Adapter-derived run identity (RFC4-19).** **ANSWERED — owner decision
   B11:** derive, and disclose collisions; austerity not taken. The collision
   safeguard is normative either way and lives in RFC4-20.
2. **Envelope minimality — OPEN.** `terminal outcome` is required (R); a run
   whose worker vanished without any report would then be recordable only as
   an `unknown-terminal` outcome value. Should the envelope instead admit
   records with outcome Unknown-by-reason, keeping R for the field but not the
   value? Proposed: yes — the field is required, `unknown-terminal` is a legal
   value; stated for explicit confirmation. **[Drafted 2026-08-10 (RD26-05):**
   the row above now carries the proposed answer as candidate text; the owner
   ratifies or reverts it at the act that binds this module.]
