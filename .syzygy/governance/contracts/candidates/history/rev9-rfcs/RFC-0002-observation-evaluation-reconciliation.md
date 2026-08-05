# RFC 0002 — Observation, Evaluation and Reconciliation

> **Status:** Proposed foundational contract. This line is a self-declaration
> at authoring time (RFC3-16): effective status is established solely by the
> owner-act record binding this file's exact content digest, and acceptance
> edits nothing here. Absent such a record, this contract binds nothing.
> **Date:** 2026-07-30 (amended through 2026-08-02).
> **Serves:** architecture.md ("Snapshots and the loop", "Typed authority",
> Aligned/Converged/Genome-complete, broadened contradiction);
> trust-and-evidence.md (evidence, three-label rule, gap exits,
> inference-as-challenge, staleness, trust floor); VIS-1/2/6/7; SEC-2/5;
> SDR-2/3/6/9/12/33; SDR §5 q4–5 (owned here: Unknown-reason vocabulary
> closure and the closed rendering-tier registry).

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- This RFC is the **time-and-truth contract**. It says when Syzygy is allowed
  to believe something, how long that belief stays valid, and what happens
  when it can't decide.
- Everything is computed at an **identified evaluation** — a (snapshot,
  as-of instant) pair. A snapshot must capture every input that could affect a
  conclusion; an uncaptured input means the affected conclusion is Unknown.
- **Statuses never improve on their own.** Between evaluations over the same
  snapshot, claims can only degrade (go stale, go Unknown). Improvement
  requires new evidence, a decision, or an adopted change — in a new snapshot.
- **Inference (AI/heuristics) can only challenge, never confirm.** An admitted
  challenge suspends a claim to Unknown until a human or a pre-declared
  policy resolves it. Human-raised challenges are admitted mechanically;
  machine-raised ones additionally need a human admission act (decision B2),
  so an inference process can't suspend claims at machine volume.
- A **contradiction** (authoritative claims that can't all be true) goes to
  the owner for adjudication — never resolved by picking a winner. A **gap**
  (desired but not yet real) exits only by evidence or by an expiring,
  reasoned dismissal — never by being ignored.
- **Merging code proves nothing.** Merged work enters a reconciliation chain
  and stays "merged, not yet evaluated" until a reconciliation evaluation
  checks it against the exact intent revision that warranted it. In V0 that
  absence is rendered honestly — a wall of "reconciliation evidence absent" on
  a fleet-built project is correct output.
- Every Unknown carries exactly one of **twelve closed reasons** (e.g.
  `missing-declaration`, `stale-beyond-currency-bound`, `execution-blocked`),
  each naming what would resolve it. Six closed **rendering tiers** qualify
  how claims display; only `gate-backed` Observed evidence can make anything
  green.

Structure: §3 is the contract (RFC2-1 … RFC2-25); §4 violation cases; §8
owner questions, answered ones marked in place.

## 1. Summary

Syzygy's temporal and epistemic contract. It fixes the semantics — never the
storage, schema, or technology — of: source snapshot and identified status
evaluation; the immutable observation record and the degradation-only temporal
rule; base graph versus inference overlays; currency, staleness, and
identity-bearing freshness; the challenge lifecycle; contradiction-versus-gap
and the two gap exits; Aligned versus Converged; **the post-merge
reconciliation chain**, which no substrate provides today and which this RFC
creates; no-gap and fixed-point semantics; failure and degradation states; the
**closed Unknown-reason vocabulary** (twelve reasons); and the **closed registry
of rendering tiers** (six tiers). [Observed] No surveyed substrate provides
the reconciliation evaluation — no object, no field, no convention exists for
it anywhere; this RFC creates it (historical: `06-TRAJECTORY-BRIEF` §7 link
11; `DISPOSITIONS-03` residual risk 1 — archived corpus, informative only).

## 2. Motivation and doctrine grounding

Doctrine already commits Syzygy to determinism per identified evaluation
(VIS-7), Unknown-not-success (VIS-2), time as an explicit input
(architecture.md), and inference holding challenge authority only
(trust-and-evidence.md). [Observed] What doctrine deliberately leaves to RFCs:
the snapshot's representation, challenge admissibility detail and lifecycle,
currency-bound mechanics, the Unknown/tier vocabularies (SDR §5 q4–5), and the
semantics of the reconciliation evaluation whose absence SDR-12 stages across
V0/V1. [Observed — architecture.md; SDR §5.] This RFC closes those, and only
those; storage substrates, wire formats, and product behavior are out of scope.

## 3. The contract

Clauses are numbered `RFC2-n` for stable citation. Amend in place; retire
rather than renumber. Parentheticals beginning *History:* are amendment
records — when and why text changed — and carry no normative force; the
clause text around them is the contract.

### Source snapshot

**RFC2-1 — The closed rule, restated as binding.** A source snapshot
identifies, by version or content hash, **every deterministic input capable of
affecting the observed graph or a status claim**. [Observed — architecture.md.]
Minimum input list (each entry independently identity-bearing):

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
    effective status. *(History: added at the rev8 final review — the rev8
    rework made effective status an act-record-derived fact, and the input
    that decides it belongs on the list that exists to make such inputs
    impossible to forget.)*

**RFC2-2 — Uncaptured means uninfluential.** A source not identified in the
snapshot must not influence any deterministic claim of that snapshot's
evaluations; affected claims render Unknown
(`source-uncaptured-or-unreachable`, RFC2-24) or the source renders
unavailable. [Observed — architecture.md.] The snapshot's representation (one
tuple vs a composite) is RFC 0003/0004 material; this RFC binds only the
closed rule and the minimum list.

### Evaluation

**RFC2-3 — Evaluation identity.** A status evaluation is identified by the
pair **(source snapshot, as-of instant)** — and nothing else. An evaluation's
*kind* (reconciliation, observation, propagate pass — RFC1-5) is a
**descriptive label, never identity-bearing**: two evaluations differing only
in kind are one evaluation, and no implementation may add a purpose, kind, or
run tag as a third identity component. The as-of instant is an explicit
input, never ambient wall-clock; every time-sensitive judgment — currency,
staleness, dismissal expiry, challenge expiry — is computed at it. Two runs of
one identified evaluation must be identical in the deterministic layer,
including logical freshness states (VIS-7 identity test); only display
formatting is excluded. [Observed — architecture.md.]

**RFC2-4 — Degradation-only over an unchanged snapshot.** A later evaluation
over the same snapshot at a later as-of instant may only *degrade* claims
(toward stale or Unknown), never establish or improve one. Improvement
requires a new snapshot containing a permitted authoritative input: new
evidence, an adjudication result, a challenge resolution, a recorded
decision, or **an adopted governance or spec artifact change** (a
declaration, a policy, an intent edit). [Observed — architecture.md, for the
rule and the first four inputs; the fifth is this RFC's explicit enumeration,
matching the resolution routes RFC2-24 gives reasons #1, #3 and #7 and the
"intent edit" reopening input of RFC2-22 — an adoption is not a "recorded
decision" in the RFC2-15 dismissal sense, and leaving it implicit invited two
implementations to differ on whether a policy edit may un-Unknown a claim
class.] Corollary: no status ever changes
without a new identified evaluation — "the badge flipped overnight" is a
violation unless an evaluation with a new identity exists.

**RFC2-5 — Two-level claim identity (SDR-2).** Every claim and gap carries
(a) a **durable semantic identity** stable across evaluations, and (b)
**evaluation-specific instances** carrying status, epistemic label, rendering
tier, Unknown reason where applicable, evidence links, freshness, and
challenge state. History and the reconciliation chain (RFC2-17…20) join on
the durable identity; truth attaches only to instances.

### Observation record

**RFC2-6 — Contents and immutability.** An observation record is the immutable
result of exactly one identified evaluation and contains **deterministic facts
only**: the evaluation identity; the deterministic observed graph; **the
declared-identity base layout** (doctrine asserts determinism over the
deterministic observed graph *and base layout*, so the layout is inside the
identity test and must be recorded for it to be checkable after the fact);
every claim instance with label, tier, reason, and resolvable evidence links;
coverage records for any executed mapping or oracle; freshness states; the open
challenge and contradiction sets as facts (not their inferred content); and
observer/adapter versions. It is evaluation-identified historical evidence,
exempt from rebuildability under VIS-6, exception (b), displayable after
supersession only with staleness visible on the primary surface. [Observed — architecture.md;
trust-and-evidence.md; VIS-6.] Inferred material never enters it (RFC2-7).

### Deterministic base graph and inference overlays

**RFC2-7 — The seam.** The deterministic base graph is computed solely from
snapshot inputs and is subject to the VIS-7 identity test. Each **inference
overlay** is a separate, separately versioned artifact recording the model,
model version, parameters, and exact inputs (by identity/digest) that
produced it, plus the snapshot it was computed over; it declares its own
reproducibility standard and is excluded from the identity test. [Observed —
architecture.md; trust-and-evidence.md.] Absent consent (SEC-2) an overlay is
**not computed** — the inferred layer renders Unknown
(`unconsented-source-or-provider`), not silently empty.

**RFC2-8 — Authority ceiling.** An overlay holds challenge authority only: it
may propose (rendered visually distinct, never anchoring the map) and it may
**challenge** (RFC2-12); it may never establish, raise, or independently
satisfy a positive status claim. Conservative suspension is the universal
default: an open admitted challenge suspends the displayed claim to Unknown
(`challenge-suspended`, `suspended` tier, deterministic basis and inference
provenance both visible) until resolved by a human or a declared
deterministic policy. [Observed — trust-and-evidence.md.]

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
therefore honored only under the owner-act provenance predicate
(RFC3-16(a), informative until RFC 0003 is accepted). A currency bound
present in the tree without verifiable owner-act provenance does not
unblock its class: the class's claims continue to render Unknown, and the
unverifiable declaration is routed to the owner as a contradiction rather
than silently honored. [Inferred — composition of this clause with
RFC3-16(a); the alternative would let an untrusted writer widen what counts
as current.]

**RFC2-10 — Identity-bearing freshness.** Logical freshness state — `fresh`,
`stale`, `broken`, `superseded` — changes status and therefore participates in
the VIS-7 identity test: two runs of one evaluation must agree on every
freshness state. [Observed — architecture.md.] Freshness is orthogonal to the
three labels and the tier registry; it never substitutes for either.

**RFC2-11 — Evidence–revision binding.** [Inferred — from the evidence
definition and the research's SHA-binding rule.] A report artifact is evidence
only *for* the revision it names; one whose claimed revision differs from the
snapshot's is stale for that snapshot regardless of age, and renders stale on
the primary surface.

### Challenge lifecycle

**RFC2-12 — Admissibility (doctrine floor, made operational).** A challenge is
admissible only if it: identifies exactly one claim (by durable identity,
RFC2-5); states a specific falsifiable concern; carries its inference
provenance (or, if human-authored, attribution); and is individually
resolvable. Mere model uncertainty, batch objections, and unfalsifiable
unease are inadmissible: recorded as rejected, never suspending anything.
[Observed floor — trust-and-evidence.md; the operational tests are this RFC's.]

**RFC2-13 — States, admission, resolution, expiry.**
`submitted → admitted | rejected`;
`admitted → resolved-upheld | resolved-dismissed | withdrawn | expired`.
Only `admitted` suspends (RFC2-8).

**Admission.** `submitted → admitted | rejected` is a **deterministic kernel
check of the mechanically checkable parts** of the RFC2-12 floor: the
challenge binds **exactly one** claim by durable identity, and inference
provenance — or, for a human-authored challenge, attribution — is present.
Those are the whole of the mechanical set: admission **never adds a criterion
the RFC2-12 floor does not carry**, since a stricter admission check would
reject challenges doctrine admits. The judgment-bearing parts of the floor
(that the concern is *specific and falsifiable*, that it is *individually
resolvable*) are checked as **presence, not merit**: whether a falsifiable
concern is stated, never whether it is a good one. Merit belongs to
resolution. The admission or rejection record is a **kernel fact written to
the governed plane** (home: `.syzygy/governance/records/`, RFC3-15's fifth
category; write authority: `kernel-recorded`, RFC3-2; see RFC3-17(a)), and it is the
artifact RFC2-1 item 9 identifies as a snapshot input — so admission state is
rebuildable (VIS-6) rather than ambient.

**In what sense admission is deterministic — two readings, not the same
claim.** Admission is deterministic **relative to the snapshot**: because the
admission record is itself a snapshot input (RFC2-1 item 9), re-running an
evaluation over the same snapshot reproduces the same admission state for
every challenge in it, and VIS-7's identity test holds over evaluations
exactly as it does for every other deterministic conclusion. What is **not**
determined by computation is *how an admitter resolves the judgment-bearing
criteria in the first place* — whether a stated concern counts as specific and
falsifiable, whether it is individually resolvable. Those are checked for
presence, not merit, and presence is still a judgment: **two admitters can
differ on the same challenge**, and no re-computation adjudicates between
them. So the act of admitting is an act recorded as a fact, not a computation;
the *state* that act produces is a deterministic input to every evaluation
that follows. Nothing downstream may assume the first sense implies the
second — that an evaluation reproduces an admission state is never evidence
that the admission was the only one available. §8 q5 puts the mechanism
itself to the owner.

**The pre-admission window.** A `submitted` challenge **suspends nothing**,
but is **rendered visibly on the affected claim**: the claim holds its
deterministic status with the pending challenge disclosed, never hidden.

**That disclosure is named `challenge-pending`.** It is a rendered state with
a value, not an unnamed decoration: RFC6-13 makes anything a surface renders
queryable, RFC6-14 requires every machine answer to carry rendered state
**verbatim**, and RFC6-22/23 make two renderings disagreeing over one declared
scope release-blocking — none of which a nameless disclosure can satisfy.
`challenge-pending` is deliberately **not** any of the three existing
categories, and naming what it is not is the whole of its semantics: it is
**not the `suspended` tier** (RFC2-25 reserves that for admitted challenges
and contradictions, and this state suspends nothing); it is **not an RFC2-24
Unknown reason** (the claim is not Unknown — it holds its deterministic label
and tier unchanged); and it is **not a sibling surface state** in RFC2-25's
sense, because *dismissed by decision*, *unadopted draft* and *editorial
draft* **replace** a status rendering, whereas `challenge-pending`
**accompanies** one that is unchanged. It therefore never displaces the claim's label, tier, reason, or
freshness on any surface or answer — it travels beside them. It ends when the
kernel records admission or rejection: `admitted` moves the claim to Unknown
(`challenge-suspended`, `suspended` tier), and `rejected` clears the
disclosure with the rejection record standing. [Inferred — the name and its
categorisation are this RFC's; the rendering obligation is the clause's
original text.]

A **declared policy bound on
admission latency** is required before a claim class may carry challenges; the
bound's *value* is quality-policy material (craft-and-care), the obligation to
declare it is this clause's. That bound is itself an authorization-bearing
governance artifact under RFC3-16(a) and is honored only under the owner-act
provenance predicate: it unblocks a claim class in the predicate's exact
sense, and a permissive worker-minted bound widens the window in which a claim
renders its deterministic status while a challenge against it sits
unadmitted — suspending nothing, disclosed but not yet biting. Where the
bound's provenance does not verify, the claim class does not carry challenges
at all, rather than carrying them under an unverified bound. *(Deliberate adjustment: doctrine makes
conservative suspension the default for an open inferred challenge but names
no admitting authority. Making admission mechanical and recorded avoids an
unbounded `submitted` limbo that quietly narrows the suspension default.)*

**Admission authority is split by who minted the challenge** *(ruled at
acceptance by owner decision B2, amending the drafted uniform-mechanical
position).* The floor check is identical in both branches; what differs is
whether passing it is sufficient to admit.

| Challenger | Admission |
|---|---|
| An **attributed human**, via the governance plane | The deterministic kernel check alone, within the declared latency bound. |
| **The declared inference process** (RFC1-5, RFC2-7) | The deterministic kernel check **and** a recorded human admission act. The latency bound governs the mechanical check; the human act carries no bound, and the challenge sits `challenge-pending` — suspending nothing, disclosed — until it occurs. |

[Inferred — the split's justification.] Attribution is already mandatory at the
RFC2-12 floor, so the branch is free to evaluate and adds no new field. The
asymmetry closes a path the uniform rule left open: **admission checks the
*presence* of floor criteria, never their merit**, so a declared inference
process can mint well-formed challenges at machine volume, each passing the
check, each suspending its claim to Unknown. That is a denial-of-truth path
with no rate bound anywhere in this contract, and it is the same
self-certification VIS-4 forbids in its own domain — an inference process
certifying its own output as admissible. Human challenges are rare, costly to
author, and individually attributable, so the mechanical path carries no
comparable exposure; this keeps challenges cheap to raise for the party that
actually needs them cheap.

**Resolution authority:** a human, or a deterministic policy declared in
`.syzygy/governance/policies/` before the challenge was admitted. Such a
policy is a resolution authority **co-equal with a human**, so it is honored
**only under RFC3-16(a)** — pre-declaration establishes *when* it was
written, never *who* wrote it, and the governance plane is writable by
fleet workers (SEC-3's untrusted actor class, extended to committed
artifacts by the premise RFC3-16(a) states). A worker-minted resolution policy would
un-suspend, in a single sweep, every claim an admitted challenge
conservatively suspended to Unknown, converting suspension back to
deterministic status wholesale without any human act; an unverifiable policy
resolves nothing and the suspensions stand (RFC3-16(a)'s effect rule).
`resolved-upheld`: the concern was substantiated and the challenged claim is
revised — via a new snapshot carrying the resolution as an authoritative
input, and a new evaluation. `resolved-dismissed` restores the claim's
deterministic status, likewise via a new snapshot carrying the resolution as
an authoritative input, and a new evaluation. `withdrawn` is challenger
retraction, recorded the same way.

**Provider revocation is not a resolution.** Where consent for the model
provider whose inference overlay produced a challenge is revoked (SEC-2/SEC-4;
RFC5-13), that provider's overlays are not recomputed and admit no **new**
challenges — but challenges **already admitted** persist through the lifecycle
above unchanged, and leave it only by one of the four resolutions named here.
Revocation ending a suspension would improve a claim (Unknown → its
deterministic status) by a consent-record change rather than a resolution act,
against RFC2-4; conservative suspension protects truth and does not lapse with
the provider. RFC5-13 states the revocation-side consequences and cites this
rule; the lifecycle is this clause's. [Inferred — this RFC's ruling, moved
here from RFC5-13 so that the challenge lifecycle is complete where it is
defined.]

**Expiry is eligibility, never an outcome.** An expiry declared in the
admitting record makes the challenge *eligible* to be resolved as `expired`
at and after that instant; it does **not** end the suspension. An
expiry-eligible challenge **continues to suspend** the claim until a recorded
resolution act — a human, or the pre-declared deterministic policy sweep —
resolves it as `expired`; that act is an authoritative input of a **new
snapshot**, and the un-suspension takes effect only at an evaluation over that
new snapshot. **Automatic expiry at the instant is not available**: it would
improve a claim (Unknown → its deterministic status) over an unchanged
snapshot by pure passage of the as-of instant — the exact violation RFC2-4 and
architecture.md's degradation-only rule forbid. Dismissal expiry (RFC2-15) may
look like a counter-example but runs the other way: it *degrades*, making a
suppressed gap visible again, which the temporal rule permits. *(Deliberate
adjustment
from the first draft, which let expiry act at the instant; §8 q2, and routed
to the acceptance packet.)* [Inferred — this RFC's design within doctrine's
constraints.]

**A sweep policy is required wherever expiry is declared** *(History: added at
acceptance by owner decision B1).* A claim class whose challenges may carry an
expiry **must** have a declared sweep policy naming what resolves an
expiry-eligible challenge — the resolving party or the deterministic rule, and
the cadence at which it runs. **An undeclared sweep is not a permissive
default**: where no sweep policy is declared, expiry-eligible challenges simply
continue to suspend indefinitely, and the class renders that fact rather than
implying that eligibility means anything. Without this requirement `expired`
is a status word nobody acts on, and "eligible" degenerates into no-expiry with
extra vocabulary.

The sweep policy is an **authorization-bearing governance artifact under
RFC3-16(a)** and is honored only under the owner-act provenance predicate — for
the same reason the resolution authority above is: a sweep converts suspended
Unknowns back to deterministic status **in bulk and without a human act**, which
is precisely the "unblocks or widens a claim class" limb of the predicate.
Where the sweep policy's provenance does not verify, it resolves nothing and
the suspensions stand. [Inferred — the requirement and its fail-closed
direction are the owner's decision; the RFC3-16(a) binding follows from the
predicate's existing limbs.]

**RFC2-14 — Suspension is not erasure.** A suspended claim's deterministic
basis stays visible for the entire lifecycle; resolving the challenge is the
only path that restores or revises the status; an inference never silently
overrides deterministic evidence. [Observed — trust-and-evidence.md.]

### Contradiction versus gap, and the two exits

**RFC2-15 — Definitions and exits.** A **contradiction** is a set of
authoritative claims in one declared scope that cannot simultaneously be
satisfied (across or within typed authorities): it renders the affected
conclusion Unknown (reason `contradicted-pending-adjudication`, `suspended`
tier), routes to owner adjudication, is never resolved by precedence, never
auto-scheduled into work. A **gap** is compatible desired state not yet
realized in observed state. [Observed — architecture.md.] A gap leaves a
surface in exactly two non-interchangeable ways: **factual resolution or
absence** — a status claim requiring current evidence; or **decision
dismissal** — a recorded, attributed human decision with reason and expiry,
committed out to the governed plane, always rendered *dismissed by decision*,
never green, resolved, or aligned. A dismissal whose reason or expiry is not
current at the as-of instant renders the gap again — through a new
evaluation, never a wall-clock flip. [Observed — trust-and-evidence.md;
VIS-6, exception (a).]

### Aligned versus Converged

**RFC2-16 — As claim predicates.** **Aligned**: one observed subject satisfies
one cited normative claim at one identified evaluation, with the evidence
trail current at its as-of instant. **Converged**: an aggregate over a
declared target scope at one identified evaluation — every mandatory claim in
scope aligned; behavioral equivalence under the declared verification oracle;
policy compliance; no unresolved contradiction touching the scope; no
actionable gap open in it. [Observed — architecture.md definitions.] Added
operational rules: a Converged claim renders its oracle's declared coverage
alongside it; an oracle with unassessed adequacy yields Unknown; both
predicates are established only by gate-backed Observed evidence (RFC2-25)
and only at a named evaluation — "Aligned" without an evaluation identity is
not a well-formed claim.

### The post-merge reconciliation chain

**RFC2-17 — Reservation of the words.** Unqualified **reconciliation** means
exactly one thing in Syzygy: the post-merge evaluation of whether a merged
change satisfies the intent revision that warranted it. Work-scheduler
substrates use the same word for **scheduler-state repair** — a substrate
label and its `reconciled`-style state events, meaning "the scheduler's own
records were brought back into agreement" — which is a substrate term the
adapter translates on read; the two senses never share a field, a count, or a
UI string.

The same reservation binds the pair **`unsatisfied`** versus
**`contradiction-raised` / Contradiction** (RFC2-18): an unsatisfied warrant
is a **gap** (compatible desired state not realized); a Contradiction is the
co-unsatisfiable-authoritative-claims entity of RFC2-15, whose only lawful
exit is adjudication. No surface, aggregate, endpoint, count, or UI string may
merge the two, and no substrate's "conflict", "failed", or "blocked" label may
be translated into either without the adapter naming which one it means.
[Adopted here as binding. The substrate survey behind the reconciliation
reservation is archived corpus (historical: `06` §2; `04` §3.5) —
informative only; the rule above stands without it.]

**RFC2-18 — The chain.** Every materialized work item that reaches merge
enters a first-class chain on its durable identity: `merged →
reconciliation-pending → (reconciliation evaluation) → reconciled@E |
unsatisfied | contradiction-raised | Unknown(reason)`.

Chain state at any evaluation is computed **from snapshot items alone** — the
merge facts carried by RFC2-1 items 1 and 3 (repository state and the
work-state export) plus the prior chain verdicts admitted under item 10. No implementation may read observation records from outside
the snapshot to decide a chain state; doing so would make the state depend on
an uncaptured input (RFC2-2) and let two implementations with different record
retention compute different chain states over one snapshot (VIS-7).

- **merged** is execution state: the change reached the integration branch.
  Never proof intent is satisfied; never green. [Observed — vision.md thesis.]
- **reconciliation-pending** attaches automatically and deterministically at
  the first evaluation that captures the merge fact (inside RFC2-19's
  deliberately triggered passes — never on a live merge event) — the honest
  default state of all merged work, asserted from the merge fact plus the
  absence of a reconciliation verdict among the prior observation records
  admitted to that evaluation (RFC2-1 item 10) — two snapshot-identified
  inputs, and nothing else.
- The **reconciliation evaluation** is an ordinary identified status
  evaluation (RFC2-3) whose snapshot must include, at minimum: the post-merge
  revision of every affected repository; the **exact intent revision** —
  requirement, scenario, or governance clause version — cited by the work
  item's warrant, as pinned in the immutable materialization record (SDR-7);
  and the verification evidence claimed for satisfaction. The chain's verdict
  binds to the warranted revision. Assessing the same merged change against
  the *current* intent revision is permitted — but as a **second claim within
  the same evaluation, not a second evaluation**. Evaluation identity is
  exactly (snapshot, as-of) (RFC2-3), and both the pinned revision (inside the
  immutable materialization record) and the current revision (a governance
  artifact) are inputs of **one** snapshot, so nothing remains to identify a
  second evaluation with; inventing a purpose or kind tag to do it would
  reopen the closed identity scheme through a side door. The two assessments
  are instead distinguished by their `cites` target — pinned intent revision
  versus current intent revision, already different durable identities under
  RFC1-18 — and only the warranted-revision claim carries the chain verdict.
  Intent drift after merge therefore surfaces as a new gap on the
  current-revision claim, never as retroactive failure of the work.

  **The two claims render as one paired state, never as two independent
  numbers** *(ruled at acceptance by owner decision on §8 q4).* Where a
  project's warranted-revision claims are reconciled and its current-revision
  claims are not, the surface renders a **single explained state** naming both
  halves and what separates them — in the shape "reconciled against what was
  approved; N gaps against intent as it now stands" — with each half separately
  expandable to its claims. Rendering them as two unlinked aggregates is a
  violation of this clause even though both aggregates are individually
  accurate. [Inferred] Both facts are true and dropping either would be a lie,
  so the binding is unchanged; what the pairing fixes is that "fully
  reconciled" and "gap-ridden" sitting side by side with no stated relation is
  the single most confusing thing a new reader encounters, and a reader who
  cannot reconcile them concludes the surface is broken rather than that intent
  moved. The obligation is on the **pairing**, not on any particular wording;
  RFC6-17's aggregation disclosure applies to each half independently.
- **Outcomes.** `reconciled@E`: the merged change satisfies the warranted
  intent revision — a positive status claim requiring gate-backed Observed
  evidence (RFC2-25), always rendered with its evaluation identity.
  **`unsatisfied`**: the warranted intent revision is not satisfied by the
  merged change and nothing is co-unsatisfiable — by RFC2-15's own definitions
  that is a **gap**, so this outcome opens a gap, or routes upward to the
  owner as a spec-indictment (the loop's one upward arrow); it renders
  *merged, evaluated, unsatisfied*, never silently reopened and never green.
  **`contradiction-raised`**: the evaluation found authoritative claims in
  scope that cannot simultaneously be satisfied — a **Contradiction** is
  minted per RFC1-5/RFC1-18(b)/RFC2-15, the affected conclusion renders
  Unknown (reason #8 `contradicted-pending-adjudication`, `suspended` tier),
  and its only lawful exit is an `adjudicates` Decision (RFC1-25): never
  resolved by precedence, never auto-scheduled into work, and specifically
  never routed into work through a gap opened on its behalf. The two negative
  outcomes are separately named, separately counted, and separately routed —
  the word reservation of RFC2-17 binds them. `Unknown(reason)`: the
  evaluation could not decide; rendered with its RFC2-24 reason.
- **Record.** The verdict is a claim instance inside an ordinary observation
  record (RFC2-6); no new record type exists. Its durable identity links
  warrant → materialization record → merge fact → reconciliation verdict,
  making "merged-but-unreconciled" a first-class, queryable distinction:
  *reconciled at E with evidence* vs *merged, not yet evaluated* vs
  *evaluated and unsatisfied* vs *evaluated, contradiction raised*. That
  verdict record is what a later evaluation admits under RFC2-1 item 10.

**RFC2-19 — Trigger and staging.** The loop is human-triggered: reconciliation
evaluations run inside a deliberately triggered propagate/sync or observation
pass, never autonomously on merge events. [Observed — architecture.md.]
Staging per SDR-12: **V0 renders the absence honestly** — merged-but-
unreconciled work renders "reconciliation evidence absent / Unknown", and a
wall of such Unknowns on a fleet-built project is correct output, not a
defect; **V1 computes** the reconciliation evaluation and its gap as
navigable, work-generating objects. Nothing in V0 may simulate the verdict.

**RFC2-20 — The closure fallacy, forbidden.** Work-scheduler closure (`closed`,
merged, abandoned, superseded) is execution state and never implies
`reconciled`. Rendering closed work as "done" without a reconciliation
verdict, or counting scheduler repairs as reconciliations (RFC2-17), violates
this contract. The closed-but-unreconciled distinction is computed the same
way as every other chain state: from the merge and closure facts in the
snapshot plus the prior verdicts admitted under RFC2-1 item 10 — never from
records read outside the snapshot.

### No-gap and fixed-point semantics

**RFC2-21 — What "no gap at evaluation E" means.** Over a declared scope at E:
every mandatory normative claim in scope has a current, gate-backed Aligned
instance; no open admitted challenge or unadjudicated contradiction touches
the scope; every merged change in scope is `reconciled@E'` with evidence still
current at E — as recorded in the prior observation records admitted to E
under RFC2-1 item 10, never as read from outside the snapshot; every dismissal
carries a reason and unexpired expiry. What it
does **not** mean: anything about instants after E's as-of instant; anything
beyond the declared oracle's rendered coverage; genome-completeness (a
separate corpus claim); or maturity on any axis. [Inferred — composition of
adopted definitions.]

**RFC2-22 — Fixed point (idempotence).** A pass over an unchanged, no-gap
source snapshot — at any as-of instant — must not mutate authoritative project
artifacts, create or reprioritize work, or establish or improve any status
claim; a later evaluation over the same snapshot may only degrade. [Observed —
architecture.md.] The fixed point is per-snapshot, not perpetual: any new
snapshot input (evidence, intent edit, adjudication) legitimately re-opens
computation.

### Failure and degradation states

**RFC2-23 — Each with its rendering obligation.** [Inferred — composed from
trust-and-evidence.md staleness rules, SEC-2/SEC-5, and the closed snapshot
rule.]

| State | Semantics | Rendering obligation |
|---|---|---|
| **Observer failed** | An observer/adapter errored during capture | Degrade to last-good observation record, marked `stale`/`broken` on the primary surface; never fail invisibly; affected new claims → Unknown (`source-uncaptured-or-unreachable`) |
| **Source unreachable** | A declared source could not be read at snapshot time | Source renders unavailable; dependent claims → Unknown (`source-uncaptured-or-unreachable`); the snapshot records the absence as a fact |
| **Consent withdrawn** | SEC-2/SEC-4 consent revoked for a repository or provider | Dependent claims → Unknown (`unconsented-source-or-provider`); inference overlays for that provider are not computed; prior records remain (immutable) but render with the withdrawal visible |
| **Partial snapshot** | Some minimum inputs (RFC2-1) captured, others not | Never presented as complete: captured scope declared explicitly; uncaptured portion → Unknown; no aggregate over the full scope may render as if whole (VIS-1: narrow the declared scope, never fake coverage) |
| **Excluded content** | Secret policy matched, or content unclassifiable (fails closed) | Exclusion rendered with count; nothing derived from excluded content in any surface, label, or endpoint; claims needing it → Unknown (`excluded-content`) |
| **Missing quantity** | Cost/tokens/measures absent | **Unknown, never zero** (SDR-6); no aggregate silently treats absent as 0 |

### The closed Unknown-reason vocabulary

**RFC2-24 — Twelve reasons, closed.** Every Unknown claim instance carries
exactly one primary reason from this list (secondary reasons may annotate);
the list changes only by amendment to this RFC, and covers Unknown states
only — *dismissed by decision*, *unadopted draft* and *editorial draft* are
the three sibling surface states, never Unknown reasons. [Seven-reason base from the archived corpus
(historical: `07-ORRERY-BRIEF` §6 — informative only); the four additions are
this RFC's, justified inline.]

**The secondary-annotation vocabulary is closed, and it is this same list.**
A secondary annotation is one or more further reasons **drawn from the twelve
below**; there is no separate secondary vocabulary, and no implementation may
mint, spell, or force-fit a secondary value the list does not carry. This is
not a stylistic preference: RFC6-14 requires every machine answer to carry its
Unknown reason **verbatim from this vocabulary**, and RFC6-22/23 make two
renderings disagreeing over one declared scope release-blocking under the
trust floor — a secondary value existing in no vocabulary can be neither
carried verbatim nor checked for parity, and leaving it unstated is how the
value gets chosen by whoever implements the render first. Which further
reasons the vocabulary should carry was the owner's choice, answered at
acceptance: **#12 `execution-blocked`** added, list closed at twelve (A5 —
settling §8 q1, RFC 0005 §8 q3 and RFC 0008 §8 q7 together). A condition that is genuinely not one of the twelve is disclosed as a
**fact of the render** — named, expandable, routed to its resolving action —
and is never dressed as a reason; the honest move is to amend this list, never
to annotate outside it. [Inferred — the closure follows from RFC6-14's
verbatim requirement; the original clause stated the permission without its
bound.]

| # | Reason | Condition | Resolution route |
|---|---|---|---|
| 1 | `missing-declaration` | No governing declaration (capability, topology, mapping, policy) exists | First-pass drafting for owner sign-off (v1.md) |
| 2 | `missing-evidence` | Declaration exists; no current evidence artifact for the claim | Produce/capture evidence |
| 3 | `no-currency-bound-declared` | The claim class has never declared a currency bound, so no evidence can count as current | Declare the bound in quality policy. *Added:* doctrine states this case separately from staleness, and its resolution is a governance act, not fresh evidence [Observed — trust-and-evidence.md] |
| 4 | `stale-beyond-currency-bound` | Evidence exists but exceeds its declared bound at the as-of instant | Capture fresh evidence via a new snapshot |
| 5 | `mapping-coverage-absent` | No executed mapping with stated coverage backs the claim (empty-plot rule: absence claims need a coverage record) | Run/declare the mapping |
| 6 | `unconsented-source-or-provider` | SEC-2/SEC-4 consent absent or withdrawn for a needed repository or model provider | Record consent. *Renamed* from "unconsented repository/provider" to include model providers explicitly |
| 7 | `excluded-content` | Secret-detection policy excluded the content, or it was unclassifiable (fails closed, SEC-5) | Policy change by the owner, or accept the exclusion |
| 8 | `contradicted-pending-adjudication` | An unresolved contradiction touches the conclusion | Owner adjudication |
| 9 | `challenge-suspended` | An open admitted challenge conservatively suspends the claim (RFC2-8) | Challenge resolution (RFC2-13). *Added:* a challenge is neither a contradiction nor missing evidence — the deterministic basis exists and stays visible; folding it into #8 would misroute resolution (adjudication vs challenge lifecycle) |
| 10 | `source-uncaptured-or-unreachable` | A deterministic input capable of affecting the claim was not captured in the snapshot (RFC2-2), including observer failure and unreachable sources | Repair the observer/source; new snapshot. *Added:* the closed snapshot rule names this outcome and its diagnosis differs from #2 — the input was never in the evaluation, versus present-but-unevidenced |
| 11 | `reference-unresolvable` | The source **was** captured and the governing declaration **does** exist, but a cited internal anchor no longer resolves — an OpenSpec requirement or scenario reference broken by edit (RFC1-15), a topology or region anchor whose target is gone (RFC1-26) | Repair the reference, owned by the governed project. *Added post-draft:* driven by four independent findings — RFC 0006 §5 (defect note) and its §8 q3, RFC 0007 §5 item 2, RFC 0008 §5 defect 5's cross-reference, and this review's K-R18. #1 implies no declaration ever existed and #10 implies a capture failure, so both misroute the diagnosis; the same routing argument justifies #9 and #10. Flagged for owner confirmation at §8 q1(a) — the owner may strike it at acceptance |
| 12 | `execution-blocked` | The declaration and the evidence route both exist, and the **execution that would produce the evidence was refused or prevented** — by execution profile, absent or withdrawn consent for the run, or an environment the profile could not satisfy. Distinct from #6, which is about a *source or provider* being unconsented rather than a *run* being blocked | **Unblock or authorize the run** (execution profile, consent, environment), then capture in a new snapshot. *Added at acceptance by owner decision (A5).* Chosen over annotating #2 with a secondary: a reason names what would resolve it, and "go capture evidence" misdescribes the remedy when the capture path is the thing that is blocked. Because the secondary vocabulary **is** this list, the pre-acceptance drafting had no lawful value to annotate with — RFC5-18's "secondary reason" had no referent, which is why this addition and not the annotation is the honest fix |

**Rendering rule.** Unknown regions may aggregate ("Unknown ×40") but must
disclose reason counts and expand; every reason routes to its resolving
action; the vocabulary is shared verbatim across 3D, tabular, and endpoint
surfaces. [Observed — `07` §6; VIS-1.] **Reason counts are this vocabulary's
share of a larger obligation, never a substitute for it:** the disclosure any
aggregate owes is **RFC6-17's in full** — the RFC6-22 equivalence tuple,
per-label, per-tier, per-Unknown-reason and per-freshness-state counts and
sibling surface states — and this rule is that obligation's Unknown-reason
component. An aggregate satisfying this sentence alone still violates RFC6-17.
The obligation is cited here, not restated, so the two cannot drift.

### The closed rendering-tier registry

**RFC2-25 — Six tiers, closed, each inside exactly one parent label.** A tier
qualifies how a claim renders and may only *restrict* its parent label's
authority, never extend it. **No new tier without an amendment to this RFC,
and a tier never becomes a fourth epistemic label** — the three-label rule is
exclusive and exhaustive; an untier'd claim renders at its bare label.
[Observed — SDR §5 q4; three-label rule per trust-and-evidence.md.]

| Tier | Parent label | Semantics | Authority |
|---|---|---|---|
| `gate-backed` | **Observed** | The claim is backed by a retained, resolvable gate artifact (report, log, run record) bound to the exact revision (SDR-9) | The **only** tier that may support a positive status claim (Aligned, Converged, reconciled, green) |
| `report-fact` | **Observed** | "X reported Y" is Observed as a fact about the report; Y itself is not thereby Observed (SDR-9) | Supports claims about the report only; never about the subject matter |
| `reduced-fidelity` | **Observed** | Deterministic at a declared coarse granularity (e.g. PR-level where event-level is unavailable, SDR-33); rendered explicitly as reduced fidelity | Full Observed authority *at its declared granularity*; finer-granularity questions render Unknown, never invented |
| `asserted-by-worker` | **Inferred** | An LLM worker's assertion of an outcome with no retained artifact (an LLM assertion is Inferred, never Observed) | Visible, never green, challengeable, never a status input (per T-F9/R-11 disposition) |
| `declared-only` | **Unknown** | Composite rendering: the declaration is Observed; its satisfaction is Unknown (SDR-3 — a declared mapping or capability with no verification). Both halves must render | The Observed half carries only declaration facts; the satisfaction claim has no positive authority |
| `suspended` | **Unknown** | An Unknown that carries a visible deterministic or authoritative basis under question — open challenge (#9) or contradiction (#8). The basis and, where inferred, the challenger's provenance render alongside | No positive authority while suspended; the basis is never erased (RFC2-14) |

*Deliberately outside the registry — **three** sibling surface states, closed:*
`dismissed-by-decision`, `unadopted-draft` and `editorial-draft`. These are
governed directly by doctrine (trust-and-evidence.md gap exits; v1.md drafting
rule) — equally closed, but not tiers of a claim label: a dismissal claims
nothing about facts, and a draft is not yet a claim source.

**`editorial-draft`** *(History: minted at acceptance by owner decision B10, discharging
RFC 0007 §5 defect 1.)* Narrative prose under revision — the editorial-draft
case SDR-15 names. It is distinct from `unadopted-draft` in **what each is
waiting for and what it becomes**: an unadopted draft awaits an **adoption gate
into authority**, and once through it, it binds and is citable. An editorial
draft awaits a **human authorship act into a non-authoritative artifact**, and
**stays non-citable even after that act completes** — narrative never becomes a
claim source, adopted or not (RFC7-20). Collapsing the two would therefore
misstate both directions at once: it would imply prose acquires authority on
adoption, and imply a pending requirement is merely being written. [Observed —
the distinction and its wording are RFC 0007's, which reported the gap; the
owner's decision was whether to mint the state.]

**`challenge-pending` (RFC2-13) is outside this registry too, and for a
different reason:** the three sibling surface states above *replace* a status
rendering, while `challenge-pending` *accompanies* an unchanged one — the claim
keeps its label and its tier while a submitted, not-yet-admitted challenge is
disclosed beside it. It is therefore neither a tier nor a sibling surface
state, and a reader checking this registry for it should look to RFC2-13.

## 4. Violation cases

- A status flips with no new identified evaluation; a later evaluation over an
  unchanged snapshot *improves* a claim (RFC2-3/4).
- Two runs of one evaluation disagree on a freshness state (RFC2-10; VIS-7).
- An inference overlay establishes or raises a status; an inadmissible
  challenge suspends a claim; a suspension hides its deterministic basis
  (RFC2-8/12/14).
- A contradiction resolved by precedence, or auto-scheduled (RFC2-15).
- A gap rendered resolved on a dismissal, or green on anything but gate-backed
  Observed evidence (RFC2-15/25).
- "Reconciled: 12" computed from scheduler-repair events; closed work rendered
  done without a reconciliation verdict (RFC2-17/20).
- An `unsatisfied` verdict counted or rendered as a Contradiction, or a
  `contradiction-raised` verdict opened as a gap and thereby routed into work
  without adjudication (RFC2-17/18; RFC2-15).
- A chain state computed from observation records read outside the snapshot,
  rather than from merge facts plus RFC2-1 item 10 (RFC2-2/18/20/21).
- An admitted challenge un-suspending its claim at its declared expiry instant
  with no recorded resolution act and no new snapshot (RFC2-4/13).
- Merged work rendered as anything but reconciliation-pending/Unknown at V0
  (RFC2-19; SDR-12).
- An Unknown rendered without a reason from RFC2-24, or with an invented one;
  an absent quantity rendered as zero (SDR-6).
- A rendering tier introduced without amending this RFC; any tier rendered as
  a fourth label (RFC2-25).
- A partial snapshot's aggregate rendered as full-scope coverage (RFC2-23).

## 5. Integration

**Relies on RFC 0001 (kernel/graph):** durable identity minting and continuity
for claims, gaps, and capabilities (SDR-2, SDR §5 q2–3); the relation
vocabulary realizing Aligned as a claim predicate; the kernel representation
of plan items and materialization records the reconciliation chain joins
through (SDR-7).
**Provides to RFC 0003 (`.syzygy/**` schemas):** the semantics snapshot,
evaluation, and observation-record representations must encode; RFC 0003 owns
physical form and migration.
**Provides to RFC 0004 (run envelope/adapters):** the evidence classes
execution records must satisfy; the `reduced-fidelity` tier whose labeling
schema RFC 0004 defines; the substrate-term translation duty of RFC2-17.
**Relies on RFC 0005:** consent-record representation behind reason #6;
execution profiles gating fresh verification evidence (SEC-3).
**Provides to RFC 0006 and RFCs 0007–0009 (surfaces):** the label+tier+reason
triple every surface renders verbatim; the RFC2-18 chain states Trajectory
renders; the Unknown-aggregation rule.
**Not this RFC's:** certificate semantics (post-V1 RFC); currency-bound
*values* and retention periods (quality policy); the V1 gap-computation
algorithm (V1 RFC); challenge admissibility *tooling*.

**Forward references are informative.** Where this RFC cites a sibling
*draft* by clause number (RFC3-n, RFC4-n, RFC5-n, and the surface RFCs), the
citation is **informative until that RFC is accepted**: it names where an
obligation will be discharged or where a strain was reported, never a
dependency of this contract's meaning. The temporal and epistemic contract
above is self-standing without them, and a renumbering in a sibling draft
changes nothing here. Only citations to **adopted doctrine**, to the **SDR**,
and to **RFC 0001** (this cluster's other half) are load-bearing; archived
corpus citations are marked "historical" and are informative in every case.

## 6. Alternatives considered

- **Fourth label for worker assertions.** Rejected: the three-label rule is
  exclusive by adopted doctrine; the reviewer already caught this drift
  (T-F9); tier-within-Inferred preserves honesty and the closed labels.
- **Keeping the research's seven Unknown reasons unchanged.** Rejected: three
  doctrine-named conditions (undeclared bound, challenge suspension,
  uncaptured source) would be forced into reasons with the wrong resolution
  routes, breaking the rule that makes a grey map diagnosis, not breakage. A
  fourth condition — a broken internal anchor over a captured source (#11) —
  was added post-draft on the same argument, and is flagged for owner
  confirmation (§8 q1(a)).
- **A dedicated reconciliation-record type.** Rejected: the verdict is an
  ordinary claim instance of an ordinary evaluation; a new type would
  duplicate observation-record semantics and invite a second store (`06` §5.2).
- **Auto-triggering reconciliation on merge events.** Rejected: the loop is
  human-triggered by doctrine; automatic evaluation is unattended computation
  over possibly-unconsented, possibly-stale inputs.
- **Evaluating reconciliation against current intent** as the chain's binding
  verdict (kept available as a separate *claim within the same evaluation*,
  RFC2-18). Rejected: post-merge spec drift would retroactively falsify
  finished work, conflating gap (new delta) with unsatisfied warrant (work
  never satisfied what warranted it).

## 7. Deliberately deferred

- Currency-bound and retention **values** per claim class → quality/evidence
  policy (craft-and-care).
- Certificate semantics, invalidation, expiry → post-V1 RFC (future-tagged).
- The V1 reconciliation-gap computation as navigable work-generating objects,
  and any batching of reconciliation into propagate passes → V1 RFC, after
  SDR-12's V0 rendering has run on the proving ground.
- Physical schema of snapshots, observation records, and the chain → RFC 0003;
  event envelope and adapter fidelity labeling → RFC 0004.
- Whether captured execution evidence needs a doctrine amendment as a narrow
  new evidence class (FRC-04-3 / FR-T5 lineage) — this RFC follows SDR-8
  (Execution Record = Evidence artifact) and takes no position on the
  amendment. [Unknown — owner's to rule if the tension resurfaces.]
- **Composite maturity rendering — deferred here so it is tracked, not
  merely missing.** architecture.md reserves the maturity axes *and any
  composite maturity rendering* to "the graph/status RFC". This RFC is the
  status half of that pair and **does not discharge the reservation at V0**:
  it defines no maturity axes, no composite, and no rule for collapsing
  axes — and neither does RFC 0001, which RFC7-16 records after looking.
  Until an amendment to this RFC or a named successor claims it, **no
  surface renders a composite maturity number** (RFC7-16 already binds
  Polaris to that, and the prohibition is general). Recorded as a deferral
  rather than left as an observation so the obligation exits this
  foundational phase with a home to return to. [Observed — architecture.md's
  reservation; Inferred — that this RFC is the reservation's addressee;
  Unknown — which contract eventually discharges it.]

## 8. Open questions for acceptance

1. **Reason granularity (RFC2-24).** Two sub-questions on the closure.
   **(a) Reason #11 `reference-unresolvable` is a post-draft amendment**
   added under review, driven by four independent findings (RFC 0006 §5 and
   its §8 q3, RFC 0007 §5 item 2, RFC 0008 §5 defect 5, and review 2's
   K-R18): a captured source whose declaration exists but whose cited
   internal anchor no longer resolves has no honest home among #1–#10.
   Confirm the eleventh reason, or strike it and direct that the case map to
   an existing reason. **(b)** Should #10 split observer-failure from
   source-unreachable (two resolution owners: Syzygy's observer vs the
   project's source)? One reason is proposed because both resolve through
   "repair, then new snapshot." *(Two further vocabulary strains are
   deliberately left unamended and remain open, and neither is currently
   answered by adding a reason here. **Blocked execution:** RFC5-18 renders
   it Unknown — `missing-evidence`, with the blocked execution disclosed as a
   fact of the render rather than as a reason, since the secondary-annotation
   closure stated in RFC2-24 admits no value outside this list; RFC 0005 §8
   q3 poses the alternative — a further **primary** reason
   `execution-blocked` — and should be answered together with this question,
   because a primary addition is an amendment to this closure. **A substrate
   value outside a declared derivation mapping:** RFC8-14 does **not** map it
   to `missing-declaration` — it renders the raw substrate status with the
   state-local absence value `state-undetermined`, which RFC8-14 declares is
   not an RFC2-24 reason, is never stamped with one, and is never counted
   among a project's Unknown-reason totals. RFC 0008 §8 q7 is the live
   question on that field: confirm `state-undetermined`, or direct that the
   case take an RFC2-24 reason instead — which would make a board-state field
   claim-bearing and let its counts enter this vocabulary's totals.)*

   > **ANSWERED at acceptance — A5.** The list grows to **twelve**: #12 `execution-blocked` added, #11 `reference-unresolvable` retained. This settles RFC 0005 §8 q3 (a **primary** reason, not a secondary annotation) and RFC 0008 §8 q7 (unmapped substrate status stays #1 `missing-declaration`) together, as the coupling required.
2. **Challenge expiry (RFC2-13).** The doctrine constraint first, because it
   narrows the choice: **automatic expiry-at-instant is not available.** An
   admitted challenge that un-suspended its claim the moment a declared
   expiry passed would *improve* a claim over an unchanged snapshot by pure
   passage of the as-of instant — precisely what RFC2-4 and architecture.md's
   degradation-only rule forbid (dismissal expiry is safe only because it runs
   the other way, degrading). The owner's real choice is therefore two-way:
   **expiry as eligibility**, as now drafted — an expiry-eligible challenge
   keeps suspending until a recorded human act or a pre-declared deterministic
   policy sweep resolves it as `expired`, that act entering a new snapshot —
   or **no expiry at all**, challenges living until resolved, since resolution
   is already a permitted new-snapshot input. Proposed: eligibility. It keeps
   the hygiene benefit at the price of one recorded act per lapsed challenge;
   the alternative costs nothing but leaves stale suspensions standing.

   > **ANSWERED at acceptance — B1.** Expiry stays **eligibility only**, and a **declared sweep policy is now required** wherever expiry is declared; an undeclared sweep is not a permissive default — eligible challenges continue to suspend. The sweep policy is authorization-bearing under RFC3-16(a).
3. **Reconciliation evidence class:** is gate-backed Observed (RFC2-25) too
   strict for `reconciled@E` on doc-only or governance-only work, where the
   "gate" is a deterministic diff-satisfies-clause check rather than a test
   run? Proposed reading: the check's retained output *is* the gate artifact.

   > **ANSWERED at acceptance.** Yes — a **deterministic, re-runnable diff-satisfies-clause check** is a lawful `gate-backed` route for doc-only and governance-only work, added as RFC4-13 **route 4**. Coupled to A2 as flagged. *(Rev7 rework, directive item A5 — not owner decision A5: route 4 now requires a **governed checker** — a lawfully adopted checker definition plus an execution artifact binding exact inputs and revisions, RFC4-13(b); determinism alone no longer suffices.)*
4. **Binding to the warranted intent revision** (RFC2-18) means a project can
   be simultaneously fully-reconciled and gap-ridden after an intent edit. Is
   that rendering acceptable at V1, or must Trajectory always co-render the
   current-revision claim (which RFC2-18 now places inside the *same*
   evaluation, not a second one)?

   > **ANSWERED at acceptance.** The warranted-revision binding **stands**; the two claims must render as **one paired state** naming both halves and what separates them, never as two independent aggregates. See RFC2-18.
5. **Challenge admission (RFC2-13).** The first draft named no authority for
   `submitted → admitted | rejected`. It is now a **deterministic kernel
   check of the mechanically checkable floor criteria**, recorded in the
   governed plane, with `submitted` challenges rendered on the affected claim
   but suspending nothing, and a required declared bound on admission
   latency. Two things for the owner. **(a)** Confirm this, or require
   **human admission** instead — safer against inference self-certification,
   at the price of an owner touch per challenge and a longer non-suspending
   window. **(b)** Note explicitly what "deterministic" does and does not
   mean here, since (a) asks you to confirm a *mechanism* and the two senses
   are easy to conflate. The **act** of admitting is an act recorded as a
   fact, not a computation: "specific falsifiable concern" and "individually
   resolvable" involve judgment even when checked only for presence, so two
   admitters can differ on the same challenge and **no re-computation
   adjudicates between them** — the act itself is not subject to the VIS-7
   identity test. The **state** that act produces *is* deterministic relative
   to the snapshot, because the admission record is a snapshot input (RFC2-1
   item 9): re-running an evaluation over the same snapshot reproduces the
   same admission state, and VIS-7 holds over evaluations as usual. RFC2-13
   now states both senses in the same words. Nothing downstream may assume
   that reproducing an admission state is evidence the admission was the only
   one available.

   > **ANSWERED at acceptance — B2, amending the drafted uniform-mechanical position.** Admission is **split by who minted the challenge**: an attributed human's challenge is admitted by the deterministic kernel check alone within the declared latency bound; a challenge minted by the **declared inference process** additionally requires a **recorded human admission act**. Rationale: admission checks *presence*, never merit, so a uniform mechanical rule leaves an inference process able to suspend claims at machine volume with no rate bound anywhere in the contract. See RFC2-13.

---

*End of RFC 0002. Clauses RFC2-1 … RFC2-25. The clause range is closed:
amend in place, add lettered sub-clauses, never renumber. (End marker added
2026-08-02 at the rev7 confirming review's flag — this RFC previously ended
without one; nothing normative changed.)*
