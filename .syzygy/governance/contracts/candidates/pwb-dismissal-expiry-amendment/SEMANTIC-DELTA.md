# Semantic delta — dismissal with a live expiry (PWB-REQ-007)

> **Candidate — binds nothing.** These bytes were drafted under the owner's
> 2026-09-21 answer to row P-79, question 5, in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
> That answer requires "CC-REV-2 delta plus a new act"; reading it as a
> direction to draft this delta is the drafter's reading [Inferred], and it
> is not a specification amendment act. Only
> a dedicated owner act naming this package's exact manifest digest may amend
> the signed PWB behavioral package. This candidate performs no act,
> authorizes no implementation and edits no signed byte.

**Artifact(s):** the eleven-artifact signed
`openspec/changes/polaris-project-wide-butlers-model/` behavior subject.
Proposed bytes exist only as six unified diffs under `proposed/`; the other
five subject rows stay byte-identical.

**Stable IDs affected:** `PWB-REQ-007`. No requirement, contract clause,
reason, tier, freshness value, challenge value or identity is minted, retired
or renumbered. The sibling surface state used, `dismissed-by-decision`, is
already one of RFC2-25's three closed sibling states. The three disclosure
classes for a record that dismisses nothing (refused, lapsed, bound to a
retired identity) are wording inside PWB-REQ-007, not new vocabulary; the
third is RFC1-12's own phrase. RFC2-24 reasons `contradicted-pending-adjudication`
and `challenge-suspended` are named, not changed.

**Change class:** **Normative.** Today PWB-REQ-007 says nothing about
dismissals, so a renderer that showed a dismissal as dismissal alone, or let
it lapse by reading time, is not excluded by the requirement's own text. After
this change it is. Someone who complied before may not comply after.
[Observed: current requirement text and the proposed paragraph; Inferred:
the compliance consequence.]

**Author:** Claude drafting worker for `syzygy-dov.29`.

**Date:** 2026-09-26; repaired 2026-09-27 after review rounds 1, 2 and 3.
**Baseline:** `3ee61c7`.

## What the owner asked for

[Observed] The P-79 row answers question 5:

> Q5 dismissal is an amendment — CC-REV-2 delta plus a new act before any
> dismissal touches a tuple

and its "What it means" column, the recorder's words rather than the
owner's answer, records the consequence for slice 4:

> slice 4 waits for the dismissal delta, its sign-off and act.

[Observed] The same row answers question 4 with "no promotion, the stage-1
unpromoted note only (VIS-6(a) personal presentation state), write act
deferred". So no write path from Syzygy into the governed plane is authorized
today, and this package does not create one.

## Current meaning

[Observed] PWB-REQ-007's operative sentence:

> Every project entity and project-fact claim SHALL have a stable semantic Claim
> identity plus an evaluation instance, be challengeable with resolvable support, and carry the
> closed label, tier, exactly one primary reason, zero or more closed secondary
> reasons, freshness, challenge state and evaluation identity that govern it.

Its Case line already sweeps "every admitted label, tier, reason, freshness,
challenge and sibling state". It never says which sibling states are admitted
or under what record, and it never mentions a dismissal, a reason or an
expiry. [Observed]

[Observed] The implementation closes the challenge vocabulary at one value,
`CHALLENGE_STATES = ['unchallenged']` in
`packages/three-surface-poc-core/src/project-shape-model.ts`, and the string
`dismissed-by-decision` appears in no file under `apps/`, `packages/` or
`scripts/` (git grep, 1,537 tracked files at the baseline).

[Observed] `CHALLENGE_STATES` being closed at `unchallenged` means no claim can
carry `challenge-suspended` today either, so the paragraph's exclusion of that
reason changes nothing the implementation does now.

## What the accepted contracts already say

Every clause below is in force. This package moves the PWB requirement toward
them; it does not change any of them.

[Observed] RFC2-15, the two exits a gap has:

> **decision
> dismissal** — a recorded, attributed human decision with reason and expiry,
> committed out to the governed plane, always rendered *dismissed by decision*,
> never green, resolved, or aligned. A dismissal whose reason or expiry is not
> current at the as-of instant renders the gap again — through a new evaluation,
> never a wall-clock flip.

and, in the same clause:

> A dismissed gap's own status
> and its Unknown reason stay visible beside the dismissal **on the primary
> surface**, for the whole time the dismissal stands: the dismissal replaces the
> status *rendering*, never the facts the status rested on.

[Observed] RFC1-20:

> A dismissal without a reason current at the
> evaluation's as-of instant renders the gap again — expiry acts only through a
> new identified evaluation (VIS-6, exception (a)).

[Observed] RFC1-25's edge-authority row:

> | `dismisses` | Decision → Gap (durable identity) | Governance act | Reason + expiry mandatory; rendered *dismissed by decision*, never green |

[Observed] RFC1-18, the two-level identity that a dismissal binds:

> **RFC1-18.** **Claim and Gap identity has two levels** (SDR-2):
>
> - **Durable identity** — deterministically derived from (subject identity,
>   cited normative reference identity, declared scope); the same identity
>   across evaluations. Challenges and dismissals bind it: a dismissal recorded
>   at one evaluation still binds the same gap at a later one.

[Observed] RFC1-5's closed entity table lists Claim and Gap as separate
entities:

> | | Claim | Kernel (derived, two-level — §3.5) | The only carrier of status |
> | | Gap | Kernel (derived, two-level — §3.5) | V0 surfaces absence; V1 computes gaps |

[Observed] RFC1-12, on identity change:

> **RFC1-12.** **Judgments do not silently survive identity change.** A
> dismissal, challenge, or claim bound to a durable identity whose subject is
> split or merged is **not** transferred to successors by the kernel: the
> successor's claims and gaps are computed fresh, the predecessor's dismissal
> renders as bound-to-retired-identity, and re-dismissal is an owner act.

[Observed] RFC2-24's reason table, row 9, and RFC2-13's meaning of
`resolved-dismissed`:

> | 9 | `challenge-suspended` | An open admitted challenge conservatively suspends the claim (RFC2-8) | Challenge resolution (RFC2-13) |

> `resolved-dismissed`: the claim's deterministic
> status is restored.

[Observed] RFC2-1 item 9 lists among an evaluation's identified inputs:

> recorded
>    decisions (dismissals with reason and expiry)

[Observed] RFC2-25, on the three sibling states outside the tier registry:

> a dismissal claims
> nothing about facts, and a draft is not yet a claim source.

[Observed] RFC6-14, on machine answers:

> Sibling surface states
> (*dismissed by decision*, *unadopted draft*, *editorial draft* — the three
> RFC2-25 places deliberately outside the registry) travel with the same
> fidelity

[Observed] VIS-6, exception (a), and its violation line:

> promoting a note into governance (an annotation or a dismissal)
> commits it out to the governed plane, attributed and reasoned, dismissals
> carrying an expiry (a dismissal without a reason current at the evaluation's
> as-of instant renders the gap again — expiry acts only through a new
> identified evaluation, architecture.md)

> a dismissal taking effect without living in the governed plane.

### What the contracts do not settle: claim or gap

[Inferred] Every contract clause above dismisses a **gap**. RFC1-18 gives Claim
and Gap separate durable identities, and RFC1-5 says V0 "surfaces absence"
while V1 computes gaps. The drafted paragraph binds a record to a **claim**'s
semantic identity, reading an Unknown PWB claim as the gap it discloses. No
quoted clause states that reading. So:

- the paragraph states the whole rule for claims, and the owner may adopt it
  as written;
- the three repair rows that would credit the gap clauses (RFC1-20.r1,
  RFC1-25.r1, RFC2-15.r1) are held at `unknown-uncovered` until the owner
  answers packet question 4;
- RFC1-26 (no relation may be re-typed except by an owner amendment) is not
  engaged by the paragraph, which adds no edge and re-types none; it would be
  engaged if the owner read question 4 as retargeting `dismisses` from Gap to
  Claim. [Inferred]

## The choice this package makes

[Observed] The M12 funnel, row Q5
(`docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md:97`), names three
arms. Verbatim:

1. > **It is an amendment, and it needs a CC-REV-2 semantic delta plus a new
   > owner act — this packet does not call the dismissal lawful or unlawful,
   > only that the path to it is not conformance.** Adding a second admitted
   > challenge value changes the closed vocabulary a signed requirement's Case
   > line quantifies over.
2. > **Second lawful arm:** implement the dismissal **beside** the tuple, as
   > its own disclosed claim with its own identity, leaving every existing
   > tuple byte-identical — which needs no amendment but is exactly the "view
   > filter over a rendered list" shape L2-M8 argues would violate VIS-6(a),
   > so it trades one objection for another.
3. > **Third lawful arm:** do not build it.

The objection arm 2 carries is stated in the funnel's slice-4 section (same
file, lines 1298-1301):

> L2-M8 is right that a
> view filter over a rendered list would violate VIS-6(a) — doctrine's own
> *Violation* line names "a dismissal taking effect without living in the
> governed plane" — and right that the honest place is the claim's own
> epistemic state.

**Drafted arm — the sibling state beside an unchanged tuple.** It is closest
to arm 2, with two differences, and it is written as an amendment (the owner's
P-79 answer requires one either way):

- it is not "its own disclosed claim": RFC2-25 says a dismissal "claims
  nothing about facts", so the dismissal is the `dismissed-by-decision`
  sibling state, not a new claim with its own status;
- it is not a view filter: only a record committed to the governed plane can
  dismiss, every such record present at the snapshot is an identified input
  of the evaluation (RFC2-1 item 9), and the paragraph refuses view
  preferences, query parameters, browser or daemon state, notes and model
  assertions by name.

[Inferred] So the VIS-6(a) violation line, "a dismissal taking effect without
living in the governed plane", does not apply to the drafted text. L2-M8's
second point, that the honest place is the claim's own epistemic state, is
answered by RFC2-25 and RFC6-14, which place `dismissed-by-decision` beside
the tuple, outside the tier registry, on purpose. **The objection survives in
one case:** if the owner answers packet question 2 with no governed-plane
home for records, nothing lawful can dismiss, and an implementation that
dismissed anyway would be exactly the view filter L2-M8 describes. The
paragraph makes that case inert (no record, no dismissal) rather than
permitted.

Reasons for the sibling-state arm over arm 1:

1. RFC2-25 already names `dismissed-by-decision` as a sibling state and says
   it "claims nothing about facts". Putting it inside the tuple would make it
   a claim about facts. [Observed clause; Inferred consequence]
2. RFC2-15 says the dismissal "replaces the status *rendering*, never the
   facts". An unchanged tuple is the most direct way to keep the facts.
   [Observed clause; Inferred fit]
3. RFC2-13's challenge value `resolved-dismissed` means something else: a
   challenge was rejected and "the claim's deterministic status is restored".
   Reusing the challenge slot for a decision dismissal would conflate the two.
   For the same reason the paragraph excludes a claim whose primary reason is
   `challenge-suspended`: that claim leaves through its challenge's own
   lifecycle, which ends in `resolved-dismissed` among others, and a decision
   dismissal on top of it would blur which of the two restored the status.
   Whether to admit it is packet question 12. [Observed clauses; Inferred
   conflict]
4. The retention direction of 2026-09-23 lets the daemon retain, per claim,
   "the claim identity, the epistemic tuple, and the challenge state. [record-level
   fields omitted: the schema name, evaluation identity, both revisions and
   the two counts.] Nothing else", and says "No record is
   committed out to any governed plane". A dismissal is in none of the three
   per-claim fields. **This does not settle retention.** The first scenario
   requires a retained evaluation, read again after the expiry, to render
   the same claim state, and that state includes the dismissal's reason,
   expiry, author and record identity. That holds only if the record's bytes
   stay reachable from the retained evaluation for as long as it is kept
   (the direction keeps records without limit), or if a fourth per-claim
   field is retained. Neither is argued from a quoted clause here, and a
   retention change is an escalation trigger, so packet question 7 routes it
   to the owner. [Observed quotations; Inferred consequence]

**Arm 1 — widen the challenge-state vocabulary.** Not drafted; available to
the owner. It needs a different patch, a reading of RFC2-13 that squares
`resolved-dismissed` with a decision dismissal, and a retention answer, since
it would put a dismissal inside a retained field.

**Arm 3 — do not build.** Available to the owner. Default if unanswered:
slice 4 does not ship and PWB-REQ-007 stays as it is.

## Proposed meaning

[Observed: `proposed/spec.md.patch`] One paragraph is added after
PWB-REQ-007's SHALL paragraph. In plain terms it says:

- **What may dismiss.** Only a dismissal record: an attributed human decision
  that names the claim's semantic identity and the primary reason it
  dismisses, states a reason and an expiry instant, and is committed to the
  governed plane. "Every dismissal record present in the governed plane at an
  evaluation's snapshot is an identified input of that evaluation", so an
  evaluation cannot leave a record out by not reading it. If the record set
  cannot be read, or no home for records is designated, the evaluation
  "dismisses no claim and SHALL disclose its dismissed count and the count of
  each record class below as Unknown, never as zero" (VIS-2: missing
  evidence never yields zero). "Nothing else
  dismisses a claim: not a view preference, a query parameter, browser or
  daemon state, an owner note or a model assertion."
- **What may be dismissed.** Only a claim whose label is Unknown, and never
  one whose primary reason is `contradicted-pending-adjudication` (owner
  adjudication only) or `challenge-suspended` (its challenge's resolution
  only).
- **When it is in effect.** "only while all three hold: the evaluation
  carries the claim identity the record names, the evaluation's as-of instant
  is earlier than the record's expiry instant, and the claim's primary reason
  is the one the record dismissed". An as-of instant equal to the expiry
  instant means lapsed. "The evaluation SHALL decide this from its own as-of
  instant and never from the instant a page or answer is read, so a dismissal
  lapses only through a new identified evaluation."
- **What it shows.** It "replaces the claim's status rendering and never its
  facts": label, tier, both reason kinds, resolution route, freshness,
  challenge state, claim identity and evaluation identity stay visible and
  unchanged beside the dismissal's reason, expiry instant, author and record
  identity, "on the same surface as the claim and without further
  disclosure", identically in the human and machine views. This carries
  RFC2-15's "on the primary surface". When more than one record is in effect
  for the same claim, each is disclosed the same way beside it and the claim
  is counted once as dismissed.
- **What it never does.** It "SHALL not change any tuple value", render as
  positive, resolved, aligned or current, or count as resolved or favourable
  in an aggregate. "Dismissed members SHALL remain in every per-label, tier,
  freshness and reason count of an aggregate, and SHALL additionally be
  counted and expandable as a sibling state", so a dismissed Unknown never
  leaves an Unknown count (VIS-2) and never leaves a freshness count
  (RFC6-17).
- **Records that dismiss nothing.** Each is disclosed in exactly one of three
  classes, distinct from each other and from a dismissal in effect. The
  classes are tested in this order and a record is disclosed in the first
  whose test it meets, so no record meets two:
  - *refused* — the record lacks an author, reason, expiry instant, claim
    identity or dismissed primary reason, or itself names, as the reason it
    dismisses, a reason that may not be dismissed; "a record is never
    refused because of the state of the claim it names";
  - *bound to a retired identity* — otherwise, RFC1-12: the evaluation
    records the claim identity it names as retired by a split or merge; it
    is never transferred to a successor, and dismissing a successor needs a
    new record;
  - *lapsed* — otherwise, a record whose expiry instant is not later than the
    as-of instant, whose claim identity the evaluation does not carry (for
    example because the declaration behind the claim was deleted or renamed),
    or whose dismissed primary reason is not the claim's (including because
    the claim is not Unknown, or its reason may not be dismissed); shown with
    the condition that lapsed it, beside the claim when the evaluation
    carries it and otherwise among the evaluation's lapsed records, so a
    complete record is never shown as refused. The condition names the test
    that failed and "never states whether the record once took effect", so a
    record whose claim or reason never matched is lapsed under the same
    condition as one whose claim or reason changed.

  Retirement and the uncarried-identity lapse are both decided on the
  evaluation's side: the evaluation either records a retirement or does not
  carry the identity. [Inferred] PWB specifies no split, merge or
  retirement record today, so until it does every record for a vanished
  claim is lapsed and the retired class is unreachable.

The Case, Oracle and Falsifier lines are extended to match. Three scenarios
are added after "Missing current evidence remains explicit Unknown":

- *A dismissal lapses only through a new evaluation* — one evaluation before
  the expiry and one exactly at it; the second shows the record lapsed; each
  evaluation carries the tuple values its own snapshot and as-of instant give,
  none changed by the dismissal; re-reading the first after the expiry still
  shows it dismissed (see point 4 above on retention).
- *A dismissal replaces the rendering, never the facts* — human/machine parity
  on the claim's own surface, aggregate counts kept (freshness included), no
  favourable aggregate, and the refused-record cases, where a record is
  refused for the reason it itself dismisses, never for the claim's current
  reason.
- *A record that no longer applies is lapsed or retired, never refused* —
  reason drift gives lapsed, even when the claim's new reason may not be
  dismissed; an identity the evaluation records as retired gives bound to a
  retired identity; an identity the evaluation does not carry gives lapsed;
  no record is shown as refused.

Warrants gain VIS-6 (doctrine) and RFC1-12, RFC1-20, RFC1-25, RFC2-1 and
RFC2-15 (contracts).

## Same-change propagation

| Subject | Change |
|---|---|
| `spec.md` | the paragraph, three extended bullets, three scenarios, warrants |
| `proposal.md` | one new last bullet describing the dismissal |
| `CAPABILITY-COVERAGE.md` | row 32 added, covered by PWB-REQ-007; 26 covered, 6 out of scope, 32 total |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | RFC6-17.r7 becomes covered; twelve rows added; totals 92 rows, 77 superseded, 65 covered, 22 Unknown uncovered, 5 believed not applicable |
| `CONTRACT-COVERAGE.md` | regenerated by its generator: 628 effective rows, 141 covered, 242 Unknown, 245 believed not applicable |
| `GOVERNING-DEPENDENCIES.md` | regenerated: 17 requirements, 100 distinct authorities (doctrine 9, contracts 71) |
| `design.md`, `.openspec.yaml`, the three matrix files | unchanged |

[Observed: builder `--check` re-derives every figure above from the proposed
bytes.] The twelve new repair rows and their reasoning are in
`IMPACT-LEDGER.md`.

## Composition with the sibling packages

[Observed: builder `--check`, 15 declared outcomes, each exercised in both
orders on scratch copies, plus one sequential run that applies every
composing sibling in table order (`.21`, `.30`, `.22`, `.20`) and then this
package, and re-checks the requirement's text.]

- **Composes cleanly:** the opening-band (`.21`) spec patch; the exact-source
  (`.30`) spec and capability patches; the machine-view (`.22`) spec patch;
  the missing-currency (`.20`) spec, capability and proposal patches. The spec
  patch uses one line of context so it still lands after `.20`'s new scenario.
- **Collides, by design:** every sibling's `GOVERNING-DEPENDENCIES.md` patch
  (generated source-digest line); lane B's spec patch (it rewrites the same
  Case, Oracle and Falsifier lines and the warrants); `.20`'s repair-delta
  totals line and its generated `CONTRACT-COVERAGE.md`.
- `.18`, the registry act, touches none of these files.

Whichever of this package and lane B lands second must be regenerated first
with `--write` against the tree the other leaves behind, and re-reviewed; the
same holds for `.20` and for every sibling whose dependencies patch collides.

## Review findings and dispositions

Round 1 (fresh context, over `9b18409`) returned **REVISE**: eleven revise
findings and seven notes. The raw is kept verbatim at
`docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-RAW.md`, and every finding is
dispositioned in the review record at the end of `OWNER-DECISION-PACKET.md`.
Round 2 (fresh context, over `82cc6c4`) returned **REVISE**: two revise
findings (N1, N2) and nine notes. The raw is kept verbatim at
`docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-2-RAW.md` and each finding is
dispositioned in the packet's review record. Round 3 (fresh context, over
`8307180`) returned **REVISE**: one revise finding (R1) and seven notes. The
raw is kept verbatim at `docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-3-RAW.md`
and each finding is dispositioned in the packet's review record. Every repair
retires the round before it (rule 10); a confirmation round must bind the
new manifest digest.
