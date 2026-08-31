---
id: RFC-0002
title: The Challenge Lifecycle — admissibility, admission, resolution, expiry
status_source: owner-act-record
module: challenge-lifecycle
clauses: RFC2-12..RFC2-14 (no gaps, no retirements, no merges)
governs: [challenge-admissibility, challenge-states, admission-authority, challenge-pending, conservative-suspension, resolution-authority, expiry-eligibility, sweep-policy]
applies_to: [kernel, all-surfaces]
depends_on: [RFC-0001, RFC-0003, RFC-0005]
tags: [foundational, epistemic, inference, challenge, fail-closed, owner-act-predicate, vis-4, sec-3]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 2 of 4 of the RFC 0002 contract package. Index, clause map,
lookup rule, package-level scope, integration, deferrals and alternatives:
`README.md`. Rationale, amendment history, and answered §8 questions:
`../../history/RFC-0002-history.md` (non-normative).

**Serves:** trust-and-evidence.md (inference-as-challenge; the admissibility floor;
conservative suspension); VIS-4 (self-certification); SEC-3 (the untrusted
actor class). Implements **owner decisions B1** (expiry stays eligibility; a
sweep policy is required) and **B2** (admission split by who minted the
challenge).

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **the whole life of a challenge**: what makes one admissible,
who may admit it, what it does to the claim while it lives, and the only four
ways it may end. Read it to answer: *may this objection suspend that claim, and
what un-suspends it?* It presupposes module 1 — a challenge binds exactly one
claim by the durable identity RFC2-5 mints, and its suspension is undone only
by the new-snapshot route RFC2-4 permits.

Three rules carry most of the weight. **Admission checks presence, never
merit** (RFC2-13) — which is precisely why owner decision B2 splits the
authority: a human's challenge passes on the deterministic kernel check alone,
while the declared inference process additionally needs a recorded human
admission act, because a uniform mechanical rule would let inference suspend
claims at machine volume. **Expiry is eligibility, never an outcome** — an
expiry-eligible challenge keeps suspending until a recorded act resolves it,
since automatic expiry would improve a claim over an unchanged snapshot.
And every declared bound or policy here — admission latency, resolution, sweep —
is **authorization-bearing under RFC3-16(a)**: the governance plane is writable
by fleet workers, so committed presence in the tree is never an owner act by
itself. Without an effective owner act, the class carries no challenges and
the suspensions stand; state (1) remains visibly uncorrelated.

---

## 3. The contract

Clauses are numbered `RFC2-n` for stable citation. Amend in place; retire
rather than renumber.

### Challenge lifecycle

**RFC2-12 — Admissibility (doctrine floor, made operational).** A challenge is
admissible only if it: identifies exactly one claim (by durable identity,
RFC2-5); states a specific falsifiable concern; carries its inference
provenance (or, if human-authored, attribution); and is individually
resolvable. Mere model uncertainty, batch objections, and unfalsifiable unease
are inadmissible: recorded as rejected, never suspending anything. [Observed
floor — trust-and-evidence.md; the operational tests are this RFC's.]

**RFC2-13 — States, admission, resolution, expiry.**
`submitted → admitted | rejected`;
`admitted → resolved-upheld | resolved-dismissed | withdrawn | expired`.
Only `admitted` suspends (RFC2-8).

**Admission** is a **deterministic kernel check of the mechanically checkable
parts** of the RFC2-12 floor: the challenge binds **exactly one** claim by
durable identity, and inference provenance — or, for a human-authored
challenge, attribution — is present. Those are the whole of the mechanical
set: admission **never adds a criterion the RFC2-12 floor does not carry**,
since a stricter check would reject challenges doctrine admits. The
judgment-bearing parts (that the concern is *specific and falsifiable*, that it
is *individually resolvable*) are checked as **presence, not merit** — whether
a falsifiable concern is stated, never whether it is a good one. Merit belongs
to resolution. The admission or rejection record is a **kernel fact written to
the governed plane** (home `.syzygy/governance/records/`, RFC3-15's fifth
category; write authority `kernel-recorded`, RFC3-2; see RFC3-17(a)), and it is
the artifact RFC2-1 item 9 identifies as a snapshot input — so admission state
is rebuildable (VIS-6) rather than ambient.

**Two senses of "deterministic", never conflated.** The *state* is
deterministic **relative to the snapshot**: because the admission record is a
snapshot input, re-running an evaluation over the same snapshot reproduces the
same admission state and VIS-7 holds as for any other deterministic conclusion.
The *act* is not: presence is still a judgment, **two admitters can differ on
the same challenge**, and **no re-computation adjudicates between them** —
admitting is an act recorded as a fact, not a computation, and the act itself
is not subject to the VIS-7 identity test. Nothing downstream may assume the
first sense implies the second; that an evaluation reproduces an admission
state is never evidence that the admission was the only one available.

**The pre-admission window, named `challenge-pending`.** A `submitted`
challenge **suspends nothing**, but is **rendered visibly on the affected
claim**: the claim holds its deterministic status with the pending challenge
disclosed, never hidden. The disclosure is a rendered state with a value, not
an unnamed decoration: RFC6-13 makes anything a surface renders queryable,
RFC6-14 requires every machine answer to carry rendered state **verbatim**, and
RFC6-22/23 make two renderings disagreeing over one declared scope
release-blocking — none of which a nameless disclosure can satisfy. Naming what
it is not is the whole of its semantics: **not the `suspended` tier** (RFC2-25
reserves that for admitted challenges and contradictions; this state suspends
nothing); **not an RFC2-24 Unknown reason** (the claim is not Unknown — it
holds its deterministic label and tier unchanged); **not a sibling surface
state** in RFC2-25's sense, because *dismissed by decision*, *unadopted draft*
and *editorial draft* **replace** a status rendering, whereas
`challenge-pending` **accompanies** one that is unchanged. It therefore never
displaces the claim's label, tier, reason, or freshness on any surface or
answer — it travels beside them. It ends when the kernel records admission or
rejection: `admitted` moves the claim to Unknown (`challenge-suspended`,
`suspended` tier); `rejected` clears the disclosure with the rejection record
standing. [Inferred — the name and its categorisation are this RFC's; the
rendering obligation is the clause's original text.]

**Declared bounds and policies are authorization-bearing.** A **declared policy
bound on admission latency** is required before a claim class may carry
challenges; the bound's *value* is quality-policy material (craft-and-care),
the obligation to declare it is this clause's. That latency bound, the
**resolution policy** and the **sweep policy** below are each an
**authorization-bearing governance artifact under RFC3-16(a)**, honored only
under the owner-act provenance predicate, because each unblocks or widens a
claim class in the predicate's exact sense — and the governance plane is
writable by fleet workers (SEC-3's untrusted actor class, extended to committed
artifacts by the premise RFC3-16(a) states), so committed presence in the tree
is forgeable from inside the tree and is not provenance. Concretely: a
worker-minted latency bound widens the window in which a claim renders its
deterministic status while a challenge against it sits unadmitted — disclosed
but not yet biting; a worker-minted resolution or sweep policy would un-suspend
wholesale, without any human act, every claim an admitted challenge
conservatively suspended to Unknown. Without an effective owner act, the claim
class **does not carry challenges at all** rather than carrying them under an
invalid bound, and an invalid resolution or sweep policy resolves nothing —
the suspensions stand (RFC3-16(a)'s effect rule). State-(1) and state-(2) acts
are both effective; kernel-recorded admission, rejection and deterministic
sweep-resolution facts remain facts, never owner acts, and carry the policy's
act provenance.

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
check, each suspending its claim to Unknown — a denial-of-truth path with no
rate bound anywhere in this contract, and the same self-certification VIS-4
forbids in its own domain (an inference process certifying its own output as
admissible). Human challenges are rare, costly to author, and individually
attributable, so the mechanical path carries no comparable exposure; this keeps
challenges cheap to raise for the party that actually needs them cheap.

**Resolution authority:** a human, or a deterministic policy declared in
`.syzygy/governance/policies/` before the challenge was admitted. Such a policy
is a resolution authority **co-equal with a human**, so it is honored **only
under RFC3-16(a)** — pre-declaration establishes *when* it was written, never
*who* wrote it. `resolved-upheld`: the concern was substantiated and the
challenged claim is revised. `resolved-dismissed`: the claim's deterministic
status is restored. `withdrawn`: challenger retraction. Each takes effect only
via a new snapshot carrying the resolution as an authoritative input, and a new
evaluation.

**Provider revocation is not a resolution.** Where consent for the model
provider whose inference overlay produced a challenge is revoked (SEC-2/SEC-4;
RFC5-13), that provider's overlays are not recomputed and admit no **new**
challenges — but challenges **already admitted** persist through the lifecycle
unchanged and leave it only by one of the four resolutions named here.
Revocation ending a suspension would improve a claim by a consent-record change
rather than a resolution act, against RFC2-4; conservative suspension protects
truth and does not lapse with the provider. RFC5-13 states the revocation-side
consequences and cites this rule; the lifecycle is this clause's. [Inferred —
this RFC's ruling.]

**Expiry is eligibility, never an outcome.** An expiry declared in the
admitting record makes the challenge *eligible* to be resolved as `expired` at
and after that instant; it does **not** end the suspension. An expiry-eligible
challenge **continues to suspend** the claim until a recorded resolution act —
a human, or the pre-declared deterministic policy sweep — resolves it as
`expired`; that act is an authoritative input of a **new snapshot**, and the
un-suspension takes effect only at an evaluation over that new snapshot.
**Automatic expiry at the instant is not available**: it would improve a claim
over an unchanged snapshot by pure passage of the as-of instant — the exact
violation RFC2-4 and architecture.md's degradation-only rule forbid. Dismissal
expiry (RFC2-15) may look like a counter-example but runs the other way: it
*degrades*, making a suppressed gap visible again, which the temporal rule
permits. [Inferred — this RFC's design within doctrine's constraints.]

**A sweep policy is required wherever expiry is declared** *(added at
acceptance by owner decision B1).* A claim class whose challenges may carry an
expiry **must** have a declared sweep policy naming what resolves an
expiry-eligible challenge — the resolving party or the deterministic rule, and
the cadence at which it runs. **An undeclared sweep is not a permissive
default**: where none is declared, expiry-eligible challenges continue to
suspend indefinitely, and the class renders that fact rather than implying that
eligibility means anything. Without this requirement `expired` is a status word
nobody acts on. [Inferred — the requirement and its fail-closed direction are
the owner's decision; the RFC3-16(a) binding follows from the predicate's
existing limbs.]

**RFC2-14 — Suspension is not erasure.** A suspended claim's deterministic
basis stays visible for the entire lifecycle; resolving the challenge is the
only path that restores or revises the status; an inference never silently
overrides deterministic evidence. [Observed — trust-and-evidence.md.]

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.*

10. *(RFC2-4/13)* An admitted challenge un-suspends its claim at its declared
    expiry instant with no recorded resolution act and no new snapshot.

Cases 3 and 11 span this module and module 1 and are held at the package level
(`README.md` §4).

---

## 5. Integration (module-local)

**Relies on RFC 0001:** the durable claim identity (RFC1-18) a challenge binds
exactly one of, and the declared inference process (RFC1-5) whose challenges
take the second admission branch. **Relies on RFC 0003:** RFC3-15's fifth
governed-artifact category and RFC3-2's `kernel-recorded` write authority
(see RFC3-17(a)) for the admission record; RFC3-16(a) for the latency bound,
resolution policy and sweep policy. **Relies on RFC 0005:** RFC5-13's consent
revocation, whose revocation-side consequences cite this module's rule that
revocation is not a resolution.

**Provides to RFC 0003:** the admission-record semantics it must physically
encode as a governed-plane kernel fact. **Provides to RFC 0006 and the surface
RFCs:** `challenge-pending` as a named rendered state — queryable under
RFC6-13, carried verbatim in machine answers under RFC6-14, and parity-checkable
under RFC6-22/23. **Provides to the rest of this package:** the admitted-challenge
condition behind Unknown reason #9 and the `suspended` tier (module 4), and the
open-challenge test in the no-gap definition (module 3, RFC2-21).

## 8. Owner questions (stubs; full text and reasoning in history)

- **q2 — Challenge expiry (RFC2-13).** Answered at acceptance — **owner
  decision B1**. See `../../history/RFC-0002-history.md` §8.
- **q5 — Challenge admission (RFC2-13).** Answered at acceptance — **owner
  decision B2**, amending the drafted uniform-mechanical position. See
  `../../history/RFC-0002-history.md` §8.

Question numbers are RFC-level and immutable; the package index is in
`README.md` §8.
