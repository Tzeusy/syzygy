---
id: RFC-0004
title: Observation Sources, Evidence, Execution Records and Adapters — contract package index
status_source: owner-act-record
package: RFC-0004
modules: [general-contract, named-adapters, execution-record, fidelity-joins-and-mappings]
clauses: RFC4-1..RFC4-29 (sub-clauses RFC4-13(a), RFC4-13(b); no gaps, no retired numbers, no merges)
governs: [observation-sources, observers, adapters, evidence, execution-records, trusted-external-oracles, governed-checkers, fidelity-labels, provenance-joins, code-mappings]
applies_to: [kernel, trajectory, orrery]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005]
tags: [observation, provenance, gate-tiering, unknown-never-zero, liveness, reduced-fidelity, capture-before-horizon]
---

# RFC 0004 — Observation Sources, Evidence, Execution Records and Adapters

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — as an owner-adopted bootstrap act
until the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Date:** 2026-07-30 (amended through 2026-08-02; compacted and split into a
package at rev10). **Rationale, amendment history, alternatives, the resolved
foundation-defect trail, and answered §8 questions:**
`../../history/RFC-0004-history.md` (non-normative).

**Serves:** VIS-1, VIS-2, VIS-5, VIS-6, VIS-7; SEC-2, SEC-3, SEC-4, SEC-5;
architecture.md (typed authority; adapter-mediated externals; the closed
snapshot rule); trust-and-evidence.md (the evidence definition; staleness; the
trust floor). Implements **owner rulings** SDR-3, SDR-4, SDR-5, SDR-6, SDR-7,
SDR-8, SDR-9, SDR-10, SDR-31, SDR-32, SDR-33, and resolves SDR §5 question 7
(run envelope schema; adapter version registry; reduced-fidelity labeling).

---

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One `RFC4-n`
namespace, no duplicated normative clauses, no renumbering.

| Module | File | Clauses | Words |
|---|---|---|---|
| 1 — general contract | `general-contract.md` | RFC4-1..RFC4-9 | 1,680 |
| 2 — named adapters | `named-adapters.md` | RFC4-10..RFC4-17, incl. RFC4-13(a), RFC4-13(b) | 3,685 |
| 3 — execution record | `execution-record.md` | RFC4-18..RFC4-21 | 1,775 |
| 4 — fidelity, joins, mappings | `fidelity-joins-and-mappings.md` | RFC4-22..RFC4-29 | 1,742 |

Counts are `wc -w` at the rev10 compaction; no module approaches the ~7,000
ceiling.

**Lookup rule (deterministic).** For any citation `RFC4-n`, read `n` as an
integer and take the first row whose range contains it; a lettered sub-clause
`RFC4-13(a)` / `RFC4-13(b)` lives with its parent RFC4-13, in module 2. The
four ranges are contiguous and exhaustive over RFC4-1…RFC4-29 with no gaps, so
the rule never needs a search. Modules are numbered for reading order only —
citations name clauses, never modules.

**Reading order for a cold reader:** module 1 → 2 → 3 → 4. Module 1 is
presupposed by all others; modules 2–4 are independently readable given it.

## Package reader map (non-normative)

*If this map and a clause disagree, the clause wins.*

This package governs **how Syzygy sees the outside world**: every source (git,
CI, the work scheduler, spec files, code) is read through a registered observer
or adapter that declares up front what it reads, what it emits, its version,
and how it fails. Four rules carry most of the weight, one per module:

- an adapter **never silently normalizes, interpolates, or forgets**, and its
  output is admissible only if it is registered (module 1, RFC4-2/RFC4-7);
- **a green gate requires provenance, not just a file** — one of four routes,
  or the outcome caps at `report-fact`, "an artifact asserting this exists"
  (module 2, RFC4-13);
- every fleet run gets an immutable **Execution Record** whose absent values
  render **Unknown, never zero**, and whose indistinguishable runs are
  disclosed rather than collapsed (module 3, RFC4-19/RFC4-20);
- coarse data is labeled `reduced-fidelity` with its cause, liveness is never
  guessed, and an absence claim needs an executed coverage record (module 4).

Two further invariants span the package: **one store per fact** — Syzygy never
keeps an editable copy of an external system's field, and never writes its own
facts into external stores except as re-derivable pointers (RFC4-5); and
Syzygy must be **fully truthful with zero toolchain changes** — richer
instrumentation only upgrades labeled Unknowns and may never be required
(RFC4-28, RFC4-29).

## Scope

This RFC is the contract between Syzygy and everything it observes: what any
observer or adapter must declare and emit; the version registry and behavior
under skew; the named adapters for the initial substrates (OpenSpec,
git/hosting, code structure, test/CI/runtime reports, Beads); the **Execution
Record** — an Evidence artifact under `.syzygy/work/**` (SDR-8) — and its
**minimum durable run envelope**; model/timing/token/cost semantics under
Unknown-never-zero (SDR-6); the provenance joins and worker-liveness rules; the
reduced-fidelity labeling schema (SDR-33); declared-versus-inferred code
mappings and the executed-coverage rule behind every absence claim (SDR-3/4);
and the derivation-first posture (SDR-31). It is **contracts only**: no storage
engine, wire format, transport, or language is chosen; physical schemas belong
to RFC 0003.

## 2. Doctrine grounding (non-normative)

Doctrine routes every question about what currently exists to code, tests, CI,
and runtime observations, and every effect on an external authority through a
typed, explicitly authorized adapter — those stores are never Syzygy-owned
namespaces [Observed: architecture.md; VIS-5]. Evidence must be durable,
identified, and integrity-verifiable, carrying source, capture time, scope, and
provenance [Observed: trust-and-evidence.md]. Observer, adapter, parser, and
policy versions are themselves deterministic snapshot inputs, and an uncaptured
source must not influence a claim [Observed: architecture.md; RFC2-1 item 7,
RFC2-2]. A substrate audit found the installed actuator toolchain both richer
and more forgetful than assumed [Observed — findings and citations in history];
the owner resolved the resulting posture questions (SDR-5, SDR-8, SDR-31,
SDR-32, SDR-33). [Inferred] The failure mode this contract guards against is
the *confident adapter*: an integration that silently normalizes, silently
interpolates, or silently forgets — manufacturing exactly the comprehensible
fiction VIS-1 forbids.

## 4. Violation cases — package-spanning

*Cases 1–3 are in module 1, 4 and 6–8 in module 2, 9 in module 3, 10–12 in
module 4. Numbering is the stable package numbering; cases are distributed,
never renumbered. Only case 5 spans two modules and is held here.*

5. *(RFC4-11/22)* Per-commit history for squash-merged work is rendered at
   commit granularity by parsing the squash body; a branch-name join renders
   without its convention basis.

## 5. Integration — package-level

**Relies on RFC 0001:** entity classes and minting authorities (RFC1-5,
RFC1-9) — this package supplies the code-element identity obligations and the
execution-run identity realization RFC1 delegates; the act-assignment rule
(RFC1-23); materialization records (RFC1-29) as the warrant join. **On
RFC 0002:** the evidence semantics execution records satisfy; the tier registry
(RFC2-25) whose `gate-backed`/`report-fact`/`asserted-by-worker`/
`reduced-fidelity` tiers these observers emit; Unknown reasons (RFC2-24);
failure states (RFC2-23); the substrate-translation duty (RFC2-17) realized by
RFC4-6. **On RFC 0003:** the RFC3-16(a) owner-act predicate, which gates six
clauses across three modules — the registry entry (RFC4-7), the
secret-detection policy version (RFC4-12), the oracle and governed-checker
artifacts (RFC4-13/13(b)), the retention bound and inter-pass interval
(RFC4-16), the staleness bound (RFC4-23), and the marker-adoption policy
(RFC4-26). **On RFC 0005:** profile identity (RFC5-18(e)), policy-violation
recording (RFC5-21), and prose-field storage authority (RFC5-17).

**Foundation defects reported against RFC 0001 — all four resolved.** No
RFC 0001 or RFC 0002 change is outstanding and none blocks acceptance. The
trail (the RFC1-29 pinned-intent-revision gap; the RFC1-5 verification-run
wording; the RFC1-5 execution-run identity licence; the RFC1-6 delegation
overreach) is preserved with §8 q5's confirmation in
`../../history/RFC-0004-history.md` §5.

**Provides to:** **RFC 0003** — registry, envelope, coverage-record, and
reduced-fidelity-label semantics to physically encode; **RFC 0005** — the
machine-client surface adapters authenticate through and the SEC-3
execution-profile boundary these observers stop at (RFC 0005's run-envelope
obligations are carried as named rows of RFC4-19, so the envelope's minimum
content is stated in one place); **RFC 0008** — the faithful substrate-state
feed (RFC4-15) its normalized work ontology maps, and the liveness rules
(RFC4-23) Trajectory renders; **RFC 0009** — the coverage records (RFC4-27)
behind every empty plot; **RFC 0011** — the evidence-identity, capture-cadence,
and adapter-boundary semantics a context packet binds against. **Not this
RFC's:** retention-bound and staleness-bound *values* (quality/evidence
policy); normalized work-state mapping (RFC 0008); live streaming and control
(deferred, SDR-5).

## 6. Alternatives considered

Seven rejected alternatives and the three post-draft (review 3) adjustments are
recorded in `../../history/RFC-0004-history.md` §6. One stays load-bearing for
reading a live clause: **first-class VCS entities** (commit/ref nodes) are
**declined** — commits and PRs serve every current need as evidence artifacts
and join fields (RFC1-6, RFC1-25) — so this RFC mints no node types, and
RFC1-5's closed V0-core vocabulary is reopened only by amendment to RFC 0001,
never by delegation to this one.

## 7. Deliberately deferred — package-level

Physical schemas for the registry, envelope, coverage records, and labels →
RFC 0003. Machine-client authentication for adapter/agent access, and every
execution-profile question (fresh test execution, build-required parsing) →
RFC 0005 (SEC-3 blocks until accepted). Normalized work-state vocabulary and
its projection of RFC4-15's feed → RFC 0008. Retention-bound, staleness-bound,
and currency-bound **values**, and RFC4-16(2)'s maximum inter-pass interval →
quality/evidence policy; all four remain **undeclared open defaults**, and
claims depending on them render Unknown until declared. Live streaming,
intervention, and control — deferred with telemetry as their entry criterion
(SDR-5). Inference-profile machinery over these sources (semantic clustering,
drift challenges) → RFC 0002's challenge lifecycle and the inference profile;
this RFC only feeds them deterministic inputs. Whether per-subworker report
contracts are worth an actuator change → the co-evolution roadmap (RFC4-29),
owner-paced.

## 8. Owner questions — package index

Numbering is stable across the package; each question's full text lives in the
module owning its clause, and answered items' reasoning is in
`../../history/RFC-0004-history.md` §8.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | Adapter-derived run identity (RFC4-19) | **answered — owner decision B11** | `execution-record.md` §8 |
| q2 | Envelope minimality (`terminal outcome` R on field or value) | **open** | `execution-record.md` §8 |
| q3 | Marker adoption granularity (RFC4-26) | **open** | `fidelity-joins-and-mappings.md` §8 |
| q4 | Capture cadence duty (RFC4-16) | **open (confirmation)** | `named-adapters.md` §8 |
| q5 | Defect resolutions (§5) | **confirmed — all four closed** | this README §5; history §8 |
| q6 | The `gate-backed` provenance predicate (RFC4-13) | **answered — owner decision A2** | `named-adapters.md` §8 |

---

*End of RFC 0004 package index. Clauses RFC4-1 … RFC4-29, with sub-clauses
RFC4-13(a) and RFC4-13(b), distributed across four modules. No retired numbers,
no merged numbers, no gaps in the range, and no clause identity in more than
one module.*
