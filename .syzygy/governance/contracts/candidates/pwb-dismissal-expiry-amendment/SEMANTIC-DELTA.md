# Semantic delta — dismissal with a live expiry (PWB-REQ-007)

> **Candidate — binds nothing.** These bytes were drafted under the owner's
> 2026-09-21 answer to row P-79, question 5, in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
> That answer is direction to draft, not a specification amendment act. Only
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
already one of RFC2-25's three closed sibling states.

**Change class:** **Normative.** Today PWB-REQ-007 says nothing about
dismissals, so a renderer that showed a dismissal as dismissal alone, or let
it lapse by reading time, is not excluded by the requirement's own text. After
this change it is. Someone who complied before may not comply after.
[Observed: current requirement text and the proposed paragraph; Inferred:
the compliance consequence.]

**Author:** Claude drafting worker for `syzygy-dov.29`.

**Date:** 2026-09-26. **Baseline:** `3ee61c7`.

## What the owner asked for

[Observed] The P-79 row answers question 5:

> Q5 dismissal is an amendment — CC-REV-2 delta plus a new act before any
> dismissal touches a tuple

and records the consequence for slice 4:

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

[Observed] VIS-6, exception (a):

> promoting a note into governance (an annotation or a dismissal)
> commits it out to the governed plane, attributed and reasoned, dismissals
> carrying an expiry (a dismissal without a reason current at the evaluation's
> as-of instant renders the gap again — expiry acts only through a new
> identified evaluation, architecture.md)

## The choice this package makes

The M12 funnel framed question 5 as widening the challenge-state vocabulary,
because a dismissal "acts on a claim's own epistemic tuple". [Observed:
`docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`, row Q5.] This
package drafts a different arm and asks the owner to choose (open question 1
in the packet).

**Drafted arm — the sibling state beside an unchanged tuple.** A dismissal is
the `dismissed-by-decision` sibling surface state. It replaces how the claim's
status is *shown* and changes no value in the claim's tuple. Reasons:

1. RFC2-25 already names `dismissed-by-decision` as a sibling state and says
   it "claims nothing about facts". Putting it inside the tuple would make it
   a claim about facts. [Observed clause; Inferred consequence]
2. RFC2-15 says the dismissal "replaces the status *rendering*, never the
   facts". An unchanged tuple is the most direct way to keep the facts.
   [Observed clause; Inferred fit]
3. RFC2-13's challenge value `resolved-dismissed` means something else: a
   challenge was rejected and "the claim's deterministic status is restored".
   Reusing the challenge slot for a decision dismissal would conflate the two.
   [Observed clause; Inferred conflict]
4. The retention direction of 2026-09-23 lets the daemon retain, per claim,
   "the claim identity, the epistemic tuple, and the challenge state… Nothing
   else", and says "No record is committed out to any governed plane". Under
   this arm a dismissal is not in any of those three fields: it is a
   governed-plane record read as an evaluation input. So this arm needs no
   change to that direction. The challenge-state arm would put a dismissal
   inside a retained field, and the owner would have to decide whether that is
   a retention change. [Observed quotations; Inferred consequence]

**Arm not drafted — widen the challenge-state vocabulary.** Available to the
owner. It needs a different patch, a reading of RFC2-13 that squares
`resolved-dismissed` with a decision dismissal, and possibly a retention
question (point 4).

**Arm not drafted — do not build.** Available to the owner. Default if
unanswered: slice 4 does not ship and PWB-REQ-007 stays as it is.

## Proposed meaning

[Observed: `proposed/spec.md.patch`] One paragraph is added after
PWB-REQ-007's SHALL paragraph. In plain terms it says:

- **What may dismiss.** Only a dismissal record: an attributed human decision
  that names the claim's semantic identity and the primary reason it
  dismisses, states a reason and an expiry instant, is committed to the
  governed plane, and is an identified input of every evaluation that reads
  it. "Nothing else dismisses a claim: not a view preference, a query
  parameter, browser or daemon state, an owner note or a model assertion."
- **What may be dismissed.** Only a claim whose label is Unknown, and never
  one whose primary reason is `contradicted-pending-adjudication`, which RFC2-15
  routes to owner adjudication.
- **When it is in effect.** At an evaluation, only if its expiry instant has
  not passed at that evaluation's as-of instant and its reason is current.
  The reason is current only while the claim's primary reason is still the one
  the record dismissed. "The evaluation SHALL decide this from its own as-of
  instant and never from the instant a page or answer is read, so a dismissal
  lapses only through a new identified evaluation."
- **What it shows.** It "replaces the claim's status rendering and never its
  facts": label, tier, both reason kinds, resolution route, freshness,
  challenge state, claim identity and evaluation identity stay visible and
  unchanged beside the dismissal's reason, expiry instant, author and record
  identity, identically in the human and machine views.
- **What it never does.** It "SHALL not change any tuple value", render as
  positive, resolved, aligned or current, or count as resolved or favourable
  in an aggregate. Aggregates count dismissed members separately and expand to
  them.
- **Refused records.** A record missing an author, reason or expiry, naming no
  claim the evaluation carries, or naming a claim it may not dismiss,
  dismisses nothing and is disclosed as refused.

The Case, Oracle and Falsifier lines are extended to match. Two scenarios are
added after "Missing current evidence remains explicit Unknown":

- *A dismissal lapses only through a new evaluation* — one evaluation before
  the expiry and one after; re-reading the first after the expiry still shows
  it dismissed.
- *A dismissal replaces the rendering, never the facts* — human/machine parity,
  no favourable aggregate, and three refused-record cases.

Warrants gain VIS-6 (doctrine) and RFC1-20, RFC1-25, RFC2-1 and RFC2-15
(contracts).

## Same-change propagation

| Subject | Change |
|---|---|
| `spec.md` | the paragraph, three extended bullets, two scenarios, warrants |
| `proposal.md` | one new last bullet describing the dismissal |
| `CAPABILITY-COVERAGE.md` | row 32 added, covered by PWB-REQ-007; 26 covered, 6 out of scope, 32 total |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | RFC6-17.r7 becomes covered; eight rows added; totals 88 rows, 76 superseded, 67 covered, 16 Unknown uncovered, 5 believed not applicable |
| `CONTRACT-COVERAGE.md` | regenerated by its generator: 625 effective rows, 143 covered, 236 Unknown, 246 believed not applicable |
| `GOVERNING-DEPENDENCIES.md` | regenerated: 17 requirements, 99 distinct authorities (doctrine 9, contracts 70) |
| `design.md`, `.openspec.yaml`, the three matrix files | unchanged |

[Observed: builder `--check` re-derives every figure above from the proposed
bytes.] The eight new repair rows and their reasoning are in
`IMPACT-LEDGER.md`.

## Composition with the sibling packages

[Observed: builder `--check`, 15 declared outcomes, each exercised in both
orders on scratch copies.]

- **Composes cleanly:** the opening-band (`.21`) spec patch; the exact-source
  (`.30`) spec and capability patches; the machine-view (`.22`) spec patch;
  the missing-currency (`.20`) spec, capability and proposal patches. The spec
  patch uses one line of context so it still lands after `.20`'s new scenario.
- **Collides, by design:** every sibling's `GOVERNING-DEPENDENCIES.md` patch
  (generated source-digest line); lane B's spec patch (it rewrites the same
  Case, Oracle and Falsifier lines and the warrants); `.20`'s repair-delta
  totals line and its generated `CONTRACT-COVERAGE.md`.
- `.18`, the registry act, touches none of these files.

Whichever of those acts is performed first, this package must be regenerated
against the tree it leaves behind, with `--write`, and re-reviewed.

## Review findings and dispositions

None yet. No review has been dispatched. Raw output, when it exists, is kept
verbatim under `docs/reviews/` with a name ending `-RAW.md`, and every finding
is dispositioned here.
