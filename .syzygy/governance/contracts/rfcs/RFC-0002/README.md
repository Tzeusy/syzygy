---
id: RFC-0002
title: Observation, Evaluation and Reconciliation — contract package index
status_source: owner-act-record
package: RFC-0002
modules: [snapshot-and-evaluation-core, challenge-lifecycle, reconciliation-chain, rendering-vocabularies]
clauses: RFC2-1..RFC2-26 (contiguous; sub-clause RFC2-19(a) in reconciliation-chain.md; no gaps, no retired numbers, no merges)
implementation_boundary:
  kind: requires-openspec
  clause: RFC2-26
governs: [source-snapshot, evaluation-identity, observation-record, inference-overlay, currency, staleness, challenge, contradiction, gap, aligned, converged, reconciliation-chain, failure-states, unknown-reason, rendering-tier]
applies_to: [kernel, all-surfaces]
depends_on: [RFC-0001, RFC-0003, RFC-0004, RFC-0005]
tags: [foundational, temporal, epistemic, evidence, closed-vocabulary, v0-v1-staging]
---

# RFC 0002 — Observation, Evaluation and Reconciliation

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this
contract binds nothing.

**Date:** 2026-07-30 (amended through 2026-08-02; compacted and split into a
package at rev10). **Rationale, amendment history, alternatives, and answered
§8 questions:** `../../history/RFC-0002-history.md` (non-normative).

**Serves:** architecture.md ("Snapshots and the loop", "Typed authority",
Aligned/Converged/Genome-complete, broadened contradiction);
trust-and-evidence.md (evidence, three-label rule, gap exits,
inference-as-challenge, staleness, trust floor); VIS-1/2/6/7; SEC-2/5;
SDR-2/3/6/9/12/33; SDR §5 q4–5 (owned here: Unknown-reason vocabulary closure
and the closed rendering-tier registry).

---

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One `RFC2-n`
namespace, no duplicated normative clauses, no renumbering.

| Module | File | Clauses |
|---|---|---|
| 1 — snapshot and evaluation core | `snapshot-and-evaluation-core.md` | RFC2-1..RFC2-11 |
| 2 — challenge lifecycle | `challenge-lifecycle.md` | RFC2-12..RFC2-14 |
| 3 — reconciliation chain | `reconciliation-chain.md` | RFC2-15..RFC2-22 |
| 4 — rendering vocabularies | `rendering-vocabularies.md` | RFC2-23..RFC2-26 |

Module sizes are deliberately **not stated here**. A measurement copied into
contract prose goes stale the moment any module moves, and moves this
package's content digest for a reason that has nothing to do with what the
package says. This artifact is governed by the applicable context-budget
policy; the current measurement lives in the generated budget report
`../../CONTEXT-BUDGET-REPORT.md`, which is regenerated, never transcribed.

**Lookup rule (deterministic).** For any citation `RFC2-n`, read `n` as an
integer and take the first row whose range contains it. RFC 0002 has exactly
**one lettered sub-clause** — **RFC2-19(a)**, minted 2026-08-10 (the RD-30
batch) inside `reconciliation-chain.md` and resolving by its integer to that
module — and every other `(a)`/`(b)` appearing in package text cites another
contract, so the integer always resolves. The four ranges are contiguous
and exhaustive over RFC2-1…RFC2-26 with no gaps, so the rule never needs a
search. Modules are numbered for reading order only — citations name clauses,
never modules.

**Reading order for a cold reader:** module 1 → 2 → 3 → 4. Module 1 is
presupposed by all others; modules 2–4 are independently readable given it.

## Package reader map (non-normative)

*If this map and a clause disagree, the clause wins.*

This package is the **time-and-truth contract**: when Syzygy may believe
something, how long the belief stays valid, and what happens when it cannot
decide. Four rules carry most of the weight, one per module:

- everything is computed at an **identified evaluation** — a
  `(snapshot, as-of instant)` pair — and over an unchanged snapshot claims may
  only **degrade**; statuses never improve on their own (module 1,
  RFC2-3/RFC2-4);
- **inference can only challenge, never confirm**, and admission checks the
  *presence* of the floor criteria rather than their merit — which is why a
  machine-minted challenge additionally needs a recorded human admission act
  (module 2, RFC2-8/RFC2-13);
- **merging code proves nothing**: merged work stays "merged, not yet
  evaluated" until a reconciliation evaluation checks it against the exact
  intent revision that warranted it (module 3, RFC2-18/RFC2-19);
- every Unknown carries exactly one of **twelve closed reasons**, and only
  `gate-backed` Observed evidence can make anything green (module 4,
  RFC2-24/RFC2-25).

Two invariants span the package: **a contradiction goes to the owner and is
never resolved by picking a winner, while a gap exits only by evidence or by an
expiring, reasoned dismissal** — the two are never merged in any surface,
count, or UI string (RFC2-15, RFC2-17); and **an uncaptured input is an
uninfluential one**, so a conclusion whose input is missing from the snapshot
renders Unknown rather than quietly proceeding (RFC2-2).

## 1. Scope

This package fixes the semantics — never the storage, schema, or technology —
of: source snapshot and identified status evaluation; the immutable observation
record and the degradation-only temporal rule; base graph versus inference
overlays; currency, staleness, and identity-bearing freshness; the challenge
lifecycle; contradiction-versus-gap and the two gap exits; Aligned versus
Converged; **the post-merge reconciliation chain**, which no substrate provides
today and which this RFC creates; no-gap and fixed-point semantics; failure and
degradation states; the **closed Unknown-reason vocabulary** (twelve reasons);
and the **closed registry of rendering tiers** (six tiers). [Observed] No
surveyed substrate provides the reconciliation evaluation — no object, no
field, no convention exists for it anywhere. Storage substrates, wire formats,
and product behavior are out of scope.

## 2. Doctrine grounding (non-normative)

Doctrine already commits Syzygy to determinism per identified evaluation
(VIS-7), Unknown-not-success (VIS-2), time as an explicit input
(architecture.md), and inference holding challenge authority only
(trust-and-evidence.md). [Observed] What doctrine deliberately leaves to RFCs,
and this package closes: the snapshot's representation, challenge admissibility
detail and lifecycle, currency-bound mechanics, the Unknown/tier vocabularies
(SDR §5 q4–5), and the semantics of the reconciliation evaluation whose absence
SDR-12 stages across V0/V1. [Observed — architecture.md; SDR §5.]

## 4. Violation cases — package-spanning

*Cases 1–2 are in module 1, 10 in module 2, 4 and 6–9 and 12 in module 3, and
13–15 in module 4. Numbering is the stable package numbering; cases are
distributed, never renumbered. Only cases 3, 5 and 11 span two modules and are
held here.*

3. *(RFC2-8/12/14)* An inference overlay establishes or raises a status; an
   inadmissible challenge suspends a claim; a suspension hides its
   deterministic basis.
5. *(RFC2-15/25)* A gap rendered resolved on a dismissal, or green on anything
   but gate-backed Observed evidence.
11. *(RFC2-9/13; RFC3-16(a))* A currency bound, admission-latency bound,
    resolution policy, or sweep policy honored without an effective owner act,
    or with its exact provenance state hidden.

## 5. Integration — package-level

**Relies on RFC 0001 (kernel/graph):** durable identity minting and continuity
for claims, gaps, and capabilities (SDR-2); the relation vocabulary realizing
Aligned as a claim predicate; the plan-item and materialization-record
representations the reconciliation chain joins through (SDR-7); Contradiction
minting and the `adjudicates` Decision (RFC1-5, RFC1-18(b), RFC1-25).
**Relies on RFC 0003:** the RFC3-16 owner-act predicate — RFC3-16(a) gating
every authorization-bearing artifact this package names (currency bound,
admission-latency bound, resolution policy, sweep policy), and RFC3-16(b) item
9 behind snapshot input 11. **Relies on RFC 0004:** RFC4-13 route 4 and its
governed-checker requirement (RFC4-13(b)) as a `gate-backed` route for doc-only
and governance-only reconciliation. **Relies on RFC 0005:** consent-record
representation behind reason #6; execution profiles gating fresh verification
evidence (SEC-3); RFC5-25's audit-record correlation.

**Provides to RFC 0003:** the semantics snapshot, evaluation, and
observation-record representations must encode; RFC 0003 owns physical form and
migration. **Provides to RFC 0004:** the evidence classes execution records must
satisfy; the `reduced-fidelity` tier whose labeling schema RFC 0004 defines; the
substrate-term translation duty of RFC2-17. **Provides to RFC 0006 and RFCs
0007–0009 (surfaces):** the label+tier+reason triple every surface renders
verbatim; the RFC2-18 chain states Trajectory renders; the Unknown-aggregation
rule. **Provides to RFC 0010:** the evidence, completion-predicate, and
contradiction-escalation semantics a bounded Mission terminates on. **Provides
to RFC 0011:** the selected evaluation and as-of instant, and the contradiction
machinery, a context packet binds against. **Not this RFC's:** certificate
semantics (post-V1 RFC); currency-bound *values* and retention periods (quality
policy); the V1 gap-computation algorithm (V1 RFC); challenge admissibility
*tooling*.

**Forward references are informative, with one stated exception.** Where this
package cites a sibling *draft* by clause number (RFC4-n, RFC5-n, and the
surface RFCs), the citation is **informative until that RFC is accepted**: it
names where an obligation will be discharged, never a dependency of this
contract's meaning, and a renumbering in a sibling draft changes nothing here.
Citations to **adopted doctrine**, to the **SDR**, and to **RFC 0001** are
load-bearing, and so are this package's citations of **RFC4-13 route 4 and
RFC4-13(b)** — RFC2-18's chain-outcome gate uses that route normatively, so
those citations are a stated reliance discharged by Wave A binding RFC 0002
and RFC 0004 together, not an informative forward reference; archived corpus
citations are informative in every case.

**The exception: this package's citations of RFC 0003 are load-bearing.** They
are exactly four — RFC3-2's write-authority classes, RFC3-15's categories,
the RFC3-16 family, and RFC3-17(a)'s home for challenge and admission
records — and each names a condition or a home this package's own clauses
require, never a place where an obligation of this package will later be
discharged. RFC3-16(a) is the sharp case: it is a condition inside this
package's own gates — the currency-bound declaration (RFC2-9) and the admission-latency,
resolution and sweep policies (RFC2-13) are honored **only** under it, and
snapshot input 11 (RFC2-1) binds the act records RFC3-16(b) item 9 identifies.
Read as informative, those gates would honor an authorization on nothing but
its presence in a tree untrusted writers can commit to — the widening RFC2-13
and RFC3-16(a) exist to prevent. **This package therefore does not bind unless
RFC 0003 is bound by the same act or an earlier one**; an act binding these
modules while RFC 0003 remains unbound leaves the gates above without their
condition, and is not an act this package's meaning survives.

## 6. Alternatives considered

Five rejected alternatives are recorded in `../../history/RFC-0002-history.md`
§6. Two stay load-bearing for reading a live clause: a **fourth epistemic
label** for worker assertions was rejected because the three-label rule is
exclusive by adopted doctrine — hence `asserted-by-worker` is a tier *within*
Inferred (RFC2-25); and **binding the chain verdict to the current intent
revision** was rejected because post-merge spec drift would retroactively
falsify finished work — hence RFC2-18's pinned warranted revision, with the
current-revision assessment kept as a second claim inside the same evaluation.

## 7. Deliberately deferred — package-level

- Currency-bound and retention **values** per claim class → quality/evidence
  policy (craft-and-care). They remain **undeclared open defaults**: a claim
  class with no declared bound renders Unknown until one exists (RFC2-9).
- Certificate semantics, invalidation, expiry → post-V1 RFC (future-tagged).
- The V1 reconciliation-gap computation as navigable work-generating objects,
  and any batching of reconciliation into propagate passes → V1 RFC, after
  SDR-12's V0 rendering has run on the proving ground.
- Physical schema of snapshots, observation records, and the chain → RFC 0003;
  event envelope and adapter fidelity labeling → RFC 0004.
- Whether captured execution evidence needs a doctrine amendment as a narrow
  new evidence class — this package follows SDR-8 (Execution Record = Evidence
  artifact) and takes no position. [Unknown — owner's to rule if the tension
  resurfaces.]
- **Composite maturity rendering — deferred here so it is tracked, not merely
  missing.** architecture.md reserves the maturity axes *and any composite
  maturity rendering* to "the graph/status RFC". This package is the status
  half of that pair and **does not discharge the reservation at V0**: it
  defines no maturity axes, no composite, and no rule for collapsing axes — and
  neither does RFC 0001, which RFC7-16 records after looking. Until an
  amendment to this RFC or a named successor claims it, **no surface renders a
  composite maturity number** (RFC7-16 binds Polaris to that; the prohibition
  is general). [Observed — architecture.md's reservation; Inferred — that this
  RFC is the addressee; Unknown — which contract eventually discharges it.]

## 8. Owner questions — package index

Numbering is **RFC-level and immutable**: a question keeps its number wherever
its clause lives. Each question's stub sits in the module owning its clause;
full text and reasoning are in `../../history/RFC-0002-history.md` §8. All five
are answered — no open question remains in this package.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | Unknown-reason granularity (RFC2-24) | **answered — owner decision A5** | `rendering-vocabularies.md` §8 |
| q2 | Challenge expiry (RFC2-13) | **answered — owner decision B1** | `challenge-lifecycle.md` §8 |
| q3 | Reconciliation evidence class (RFC2-18/25) | **answered — RFC4-13 route 4** | `reconciliation-chain.md` §8 |
| q4 | Binding to the warranted intent revision (RFC2-18) | **answered — binding stands; one paired state, never two independent aggregates** | `reconciliation-chain.md` §8 |
| q5 | Challenge admission (RFC2-13) | **answered — owner decision B2** | `challenge-lifecycle.md` §8 |

---

## Phase boundary

The phase rule **RFC2-26** binds the whole package: this contract fixes
evidence, evaluation and rendering semantics and is not a specification of
record from which implementation work may be scheduled. The clause text is
in `rendering-vocabularies.md`, and its clause-to-requirement coverage
matrix must cover **RFC2-1…RFC2-26 across all four modules**, not module 4
alone.

---

*End of RFC 0002 package index. Clauses RFC2-1 … RFC2-26, contiguous and
distributed across four modules. One lettered sub-clause — RFC2-19(a), in
`reconciliation-chain.md` — no retired numbers, no merged numbers, no gaps
in the range, and no clause identity in more than one module. The clause
range is closed: amend in place, add lettered sub-clauses, never renumber.*
