---
id: RFC-0002
title: Source Snapshot, Evaluation Identity and the Observation Record
status_source: owner-act-record
module: snapshot-and-evaluation-core
clauses: RFC2-1..RFC2-11 (no gaps, no retirements, no merges)
governs: [source-snapshot, snapshot-inputs, evaluation-identity, degradation-only-rule, claim-identity, observation-record, inference-overlay, currency-bound, freshness, evidence-revision-binding]
applies_to: [kernel, all-surfaces]
depends_on: [RFC-0001, RFC-0003, RFC-0005]
tags: [foundational, temporal, epistemic, determinism, vis-7, vis-2, vis-6, sdr-2]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 1 of 4 of the RFC 0002 contract package. Index, clause map,
lookup rule, package-level scope, integration, deferrals and alternatives:
`README.md`. Rationale, amendment history, and answered §8 questions:
`../../history/RFC-0002-history.md` (non-normative).

**Serves:** architecture.md ("Snapshots and the loop"; the closed snapshot rule;
determinism over the deterministic observed graph and base layout);
trust-and-evidence.md (evidence, staleness, the currency bound,
inference-as-challenge); VIS-2, VIS-6, VIS-7; SEC-2. Implements **owner
ruling** SDR-2 (two-level claim identity) and carries SDR-8's
Execution-Record-as-Evidence reading as snapshot input 6.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what an evaluation is computed over, what identifies it, and
which direction its conclusions may move**. Read it to answer: *is this claim
even well-formed, and may it have got better?* Every other module in this
package presupposes it — a challenge (module 2), a chain verdict (module 3), or
an Unknown reason (module 4) attaches to a claim instance minted here, at an
evaluation identified here.

Four rules carry most of the weight. A snapshot identifies **every**
deterministic input capable of affecting a conclusion, and its eleven-item
minimum list is enumerated rather than described (RFC2-1) — **item numbers are
cited from other contracts and never change**. An input not in the snapshot
must not influence that snapshot's claims (RFC2-2). An evaluation is identified
by `(source snapshot, as-of instant)` and by nothing else, so no
implementation may add a third identity component (RFC2-3). And over an
unchanged snapshot, claims may only **degrade** — improvement requires a new
snapshot carrying one of five permitted authoritative inputs (RFC2-4). The
currency-bound declaration (RFC2-9) is the module's one authorization-bearing
artifact: it is what lets a claim class leave Unknown, so it is honored only
under the RFC3-16(a) owner-act predicate.

---

## 3. The contract

Clauses are numbered `RFC2-n` for stable citation. Amend in place; retire
rather than renumber.

### Source snapshot

**RFC2-1 — The closed rule, restated as binding.** A source snapshot
identifies, by version or content hash, **every deterministic input capable of
affecting the observed graph or a status claim**. [Observed — architecture.md.]
Minimum input list (each entry independently identity-bearing; item numbers are
load-bearing and cited elsewhere — never renumber):

1. every observed repository (governance root and each consented
   observed-source repository) and its declared working-tree state;
2. governance artifacts (`.syzygy/governance/**`, `openspec/**`) per-artifact,
   with adoption status as a fact, not formatting;
3. the work-state export and its capture instant;
4. consumed test, CI, and verification report artifacts, each with the
   revision it claims to describe, and any **external-confirmation capture
   artifacts** bound to them (RFC4-13(a)) — an externally confirmed gate
   outcome is in the snapshot only together with its captured confirmation;
5. the runtime observation dataset **and its window**, when used;
6. captured execution evidence consumed by the evaluation (Execution Records
   are Evidence artifacts, SDR-8);
7. observer, adapter, parser, layout, and policy versions (secret-detection,
   quality/evidence, currency-bound declarations), and the evaluation engine
   (kernel) version;
8. deterministic configuration affecting parsing or classification;
9. open challenges (with their admission records, RFC2-13), recorded
   decisions (dismissals with reason and expiry), and adjudication results
   admitted as inputs;
10. the identified set of prior observation records admitted to the
    evaluation — at minimum, prior reconciliation-chain claim instances and
    their verdicts — each identity-bearing. Chain state (RFC2-18/20/21) and
    the open challenge and contradiction sets (RFC2-6) derive from snapshot
    items alone — merge facts plus this item — never from records read
    outside the snapshot;
11. the **owner-act records establishing effective status** (RFC3-16) for
    every governance artifact whose effective status the evaluation reads,
    each with the identity of the audit-record correlation it resolves to
    (RFC3-16(b) item 9; RFC5-25) — the audit trail's content lives outside
    the tree by rule, but the act-record set consumed is identity-bound in
    the snapshot like any other deterministic input, so two evaluations
    reading different act records cannot silently report the same
    effective status.

**RFC2-2 — Uncaptured means uninfluential.** A source not identified in the
snapshot must not influence any deterministic claim of that snapshot's
evaluations; affected claims render Unknown
(`source-uncaptured-or-unreachable`, RFC2-24) or the source renders
unavailable. [Observed — architecture.md.] The snapshot's representation (one
tuple vs a composite) is RFC 0003/0004 material; this RFC binds only the closed
rule and the minimum list.

### Evaluation

**RFC2-3 — Evaluation identity.** A status evaluation is identified by the
pair **(source snapshot, as-of instant)** — and nothing else. An evaluation's
*kind* (reconciliation, observation, propagate pass — RFC1-5) is a
**descriptive label, never identity-bearing**: two evaluations differing only
in kind are one evaluation, and no implementation may add a purpose, kind, or
run tag as a third identity component. The as-of instant is an explicit input,
never ambient wall-clock; every time-sensitive judgment — currency, staleness,
dismissal expiry, challenge expiry — is computed at it. Two runs of one
identified evaluation must be identical in the deterministic layer, including
logical freshness states (VIS-7 identity test); only display formatting is
excluded. [Observed — architecture.md.]

**RFC2-4 — Degradation-only over an unchanged snapshot.** A later evaluation
over the same snapshot at a later as-of instant may only *degrade* claims
(toward stale or Unknown), never establish or improve one. Improvement
requires a new snapshot containing a permitted authoritative input: new
evidence, an adjudication result, a challenge resolution, a recorded decision,
or **an adopted governance or spec artifact change** (a declaration, a policy,
an intent edit). [Observed — architecture.md, for the rule and the first four
inputs; the fifth is this RFC's explicit enumeration, because an adoption is
not a "recorded decision" in the RFC2-15 dismissal sense.] Corollary: no status
ever changes without a new identified evaluation — "the badge flipped
overnight" is a violation unless an evaluation with a new identity exists.

**RFC2-5 — Two-level claim identity (SDR-2).** Every claim and gap carries
(a) a **durable semantic identity** stable across evaluations, and (b)
**evaluation-specific instances** carrying status, epistemic label, rendering
tier, Unknown reason where applicable, evidence links, freshness, and
challenge state. History and the reconciliation chain (RFC2-17…20) join on the
durable identity; truth attaches only to instances.

### Observation record

**RFC2-6 — Contents and immutability.** An observation record is the immutable
result of exactly one identified evaluation and contains **deterministic facts
only**: the evaluation identity; the deterministic observed graph; **the
declared-identity base layout** (doctrine asserts determinism over the observed
graph *and base layout*, so the layout is inside the identity test and must be
recorded to stay checkable after the fact); every claim instance with label,
tier, reason, and resolvable evidence links; coverage records for any executed
mapping or oracle; freshness states; the open challenge and contradiction sets
as facts (not their inferred content); and observer/adapter versions. It is
evaluation-identified historical evidence, exempt from rebuildability under
VIS-6, exception (b), displayable after supersession only with staleness
visible on the primary surface. [Observed — architecture.md;
trust-and-evidence.md; VIS-6.] Inferred material never enters it (RFC2-7).

### Deterministic base graph and inference overlays

**RFC2-7 — The seam.** The deterministic base graph is computed solely from
snapshot inputs and is subject to the VIS-7 identity test. Each **inference
overlay** is a separate, separately versioned artifact recording the model,
model version, parameters, and exact inputs (by identity/digest) that produced
it, plus the snapshot it was computed over; it declares its own reproducibility
standard and is excluded from the identity test. [Observed — architecture.md;
trust-and-evidence.md.] Absent consent (SEC-2) an overlay is **not computed** —
the inferred layer renders Unknown (`unconsented-source-or-provider`), not
silently empty.

**RFC2-8 — Authority ceiling.** An overlay holds challenge authority only: it
may propose (rendered visually distinct, never anchoring the map) and it may
**challenge** (RFC2-12); it may never establish, raise, or independently
satisfy a positive status claim. Conservative suspension is the universal
default: an open admitted challenge suspends the displayed claim to Unknown
(`challenge-suspended`, `suspended` tier, deterministic basis and inference
provenance both visible) until resolved by a human or a declared deterministic
policy. [Observed — trust-and-evidence.md.]

### Currency and staleness

**RFC2-9 — The declaration mechanism.** Every claim class must declare a
currency bound — how old its evidence may be and still count as current —
before any of its claims can leave Unknown. Bound *values* are craft material
in the quality/evidence policy; this RFC binds the mechanism: the declaration
is a snapshot input (RFC2-1 item 7); an undeclared bound renders the class's
claims Unknown (`no-currency-bound-declared`); an exceeded bound renders
`stale-beyond-currency-bound`. Currency is judged at the evaluation's as-of
instant, never by ambient clock. [Observed — trust-and-evidence.md; VIS-2.]

The bound declaration is itself an **authorization-bearing governance
artifact** — it is the act that lets a claim class leave Unknown — and is
therefore honored only under the owner-act provenance predicate (RFC3-16(a),
informative until RFC 0003 is accepted). A currency bound present in the tree
without verifiable owner-act provenance does not unblock its class: the claims
continue to render Unknown, and the unverifiable declaration is routed to the
owner as a contradiction rather than silently honored. [Inferred — composition
with RFC3-16(a); the alternative would let an untrusted writer widen what counts
as current.]

**RFC2-10 — Identity-bearing freshness.** Logical freshness state — `fresh`,
`stale`, `broken`, `superseded` — changes status and therefore participates in
the VIS-7 identity test: two runs of one evaluation must agree on every
freshness state. [Observed — architecture.md.] Freshness is orthogonal to the
three labels and the tier registry; it never substitutes for either.

**RFC2-11 — Evidence–revision binding.** [Inferred — from the evidence
definition and the SHA-binding rule.] A report artifact is evidence only *for*
the revision it names; one whose claimed revision differs from the snapshot's
is stale for that snapshot regardless of age, and renders stale on the primary
surface.

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.*

1. *(RFC2-3/4)* A status flips with no new identified evaluation; a later
   evaluation over an unchanged snapshot *improves* a claim.
2. *(RFC2-10; VIS-7)* Two runs of one evaluation disagree on a freshness state.

Cases 3 and 11 span this module and module 2, and case 5 spans modules 3 and 4;
all three are held at the package level (`README.md` §4).

---

## 5. Integration (module-local)

**Relies on RFC 0001:** durable identity minting and continuity for claims,
gaps, and capabilities (RFC2-5; SDR-2). **Relies on RFC 0003:** the RFC3-16
owner-act predicate — RFC3-16(a) gating the currency-bound declaration
(RFC2-9), and RFC3-16(b) item 9 supplying the audit-correlation identity that
snapshot input 11 binds. **Relies on RFC 0005:** RFC5-25's audit-record
correlation, likewise behind input 11.

**Provides to RFC 0003:** the semantics that snapshot, evaluation, and
observation-record representations must physically encode. **Provides to
RFC 0004:** the snapshot minimum-input list (items 4, 6, 7) every observer and
adapter maps its declared inputs onto, and the uncaptured-source rule its
outputs are admissible under. **Provides to RFC 0011:** the selected evaluation
and as-of instant a context packet binds against. **Provides to the rest of
this package:** the claim instance (RFC2-5) that a challenge suspends, a chain
verdict attaches to, and an Unknown reason stamps; the degradation-only rule
(RFC2-4) that makes automatic challenge expiry unavailable in module 2; and the
authority ceiling (RFC2-8) that module 2's lifecycle operationalizes.

## 8. Owner questions

This module owns no §8 owner question. The package index is in `README.md` §8.
