# Owner decision packet — Three-Surface POC vocabulary and epistemic-record amendment

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts two questions on this version and four
> deferred-scope questions to the owner; only the owner's answer binds
> anything (VIS-4).

**Status:** drafted 2026-10-14. On your direction of that day you parked
P-84 (`../three-surface-poc-identity-amendment/`) and asked for a narrower
redraft from its 43 findings. This is that redraft, register row P-108.
*(Marked 2026-10-15: "It has had **no review yet**: round 1 is briefed in
`REVIEW-BRIEF.md`" is no longer true.)* Round 1
(docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md) was
`REVISE`, with two revise findings and seven notes. On your direction of
2026-10-15 ("One cycle", as relayed by the lead session) every finding was
**repaired once on 2026-10-15, unconfirmed pending round 2**, mapped in
`ROUND-1-DISPOSITIONS.md`. Round 2 is briefed in `REVIEW-BRIEF.md`
§"Round 2". This version is not offered for signing until a round clears
it; a `REVISE` in round 2 comes back to you with its findings open.

## What you would be signing

One amendment to the signed Three-Surface POC specification, carrying two
of the three parts P-75 (A) ruled. `SEMANTIC-DELTA.md` has the full account
and the findings census behind the narrowing.

- **POC-REQ-055 (new).** Every relationship the POC emits either carries a
  name from RFC1-25's closed table, in a role pair the table assigns it, or
  carries a flag saying it is outside that table. **None of today's nine
  relationships complies.** Seven kinds are outside the table. The eighth,
  `contains`, joins a project to a capability, a pair its row does not
  assign. The signed coverage row that mapped this to POC-REQ-052 stays as
  it is. Beside it, an added row and a disclosure say that the flag is the
  repair you ruled. Closure itself, meaning no outside kind is emitted at
  all, stays Unknown. So does whether the declared kind-to-class mapping the
  role-pair check reads through is true, because the slice that emits the
  relationships also writes that mapping.
- **POC-REQ-060 (amended).** The one-encoding rule now names all three
  labels, Observed, Inferred and Unknown. Every entity and relationship
  carries one record shape. Inferred is allowed only for an agent's
  assertion, and never counts as Observed or clears an Unknown. Nothing
  produces one today.

This started as the parked package's POC-REQ-055 unchanged, and its
POC-REQ-060 with three changes. The record shape covers entities and
relationships, not claims: the project-shape plane's claims are PWB-REQ-007's
under P-75 Q2, and the governing-intent claim on each work item, signed under
P-100, is POC-REQ-014's. *(Marked 2026-10-15: the first draft said "not
"claims", which the POC specification never defines"; P-100 made that
false, as round 1's finding 5 found.)* The Inferred recount names records by
the list and the identifier the machine answer already serves, not by the
deferred subject identity. And a tier is checked where a record carries one,
rather than "where one applies". `SEMANTIC-DELTA.md` §2 gives the reason for
each.

**What round 1 changed.** [Inferred] Rendering obligations now reach the
rendered elements that carry a relationship's or record's served `id` in a
declared marker, the form POC-REQ-020 uses, and each unmarked rendering is
an Unknown row (Question 2). The declared encoding table must give
Observed, Inferred and Unknown three different entries, which also keeps
POC-REQ-014's encoding check decidable. "Observed total" now names its
population. The coverage matrix gains three Unknown rows, one of them for
the tier meanings (`gate-backed` without a gate artifact, for example) that
the oracle does not check. The delta also now says that POC-REQ-060 keeps
Inferred records inline, not in a separate stored layer excluded from the
VIS-7 identity test as doctrine asks, and defers both to the production
constructor's act.

**What is not in it.** The subject identity requirement (POC-REQ-054), the
three-state ribbon scenario, the cross-surface link row and the join key.
Each is listed under "Deferred scope" below with a question.

**One departure from the design you adopted: role pairs, not only kinds.**
The M9 design said "Every emitted kind is either an RFC1-25 name or carries
an explicit out-of-vocabulary flag". POC-REQ-055 also checks that a named
relationship joins the kinds of thing the table allows for that name.

- **Why.** RFC1-26 forbids re-typing, so a correct name between the wrong
  kinds of thing is not compliant either. This is why `contains`, from a
  project to a capability, is flagged too. [Inferred]
- **The consequence if you sign.** Slice 8 also writes a declaration
  mapping the POC's kinds to RFC 0001's classes. Whether that mapping is
  true stays Unknown.
- **If you want the kind check alone,** answer "Revise" and say so.

**What signing does not do.**

- It starts no implementation. Under your Scope A POC extension, "Signing a
  package starts no implementation; each needs its own implementation
  authorization". Question D3 below asks which M9 slices it makes eligible.
- It does not make the Inferred arm constructible in production. Under your
  ruling (P-75 Q4) the arm stays a typed landing zone with no production
  constructor, and a production constructor needs its own act.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | The patches are applied in the sign-off change, and the specification reads 26 requirements. |
| Decline | The specification stays at 25 requirements. |
| Revise | Name what to change; a new version gets a new review round. |

**Route.** The version tag under Scope A, through
`../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`.
That record's item 1 reaches "a package that patches
`openspec/changes/three-surface-poc-experience/`", so it reaches this one.
You sign by selecting a version. No phrase or digest is needed, and the
signing change registers the package with
`scripts/record_versioned_signoff.py`, naming that direction as its
extension. [Inferred] No route question is asked, because that record
already answers it for every POC amendment.

**If unanswered,** nothing is signed and the package stays a candidate.

## Question 2 — which renderings must show the flag and the Inferred encoding?

Round 1 found that "rendered wherever the relationship is rendered" names a
population no check can list: a Polaris sentence that mentions a flagged
relationship without any marker is a rendering no sweep finds. The repair
chose one of two readings the reviewer offered.

| Option | Meaning |
|---|---|
| **Marked renderings only** (recommended; this version) | The flag and reason, and the Inferred encoding, are required in every rendered element that carries the served `id` in a declared marker. The check counts that marker population and reports it. An unmarked rendering is outside the check and is an Unknown row in the coverage matrix. |
| Every rendering, marked or not | The requirements also say every rendering of a relationship or record SHALL carry a marker. [Inferred] No sweep can find an unmarked rendering, so that limb would still have no deciding oracle. |

Signing v1.0 answers this with the recommended option. To choose the other,
answer Question 1 with "Revise" and say so.

## Deferred scope

These questions need no answer for Question 1, and none blocks signing it.
Each is about what this package leaves out.

### D1 — the subject identity requirement: when, and on what input?

The parked package's POC-REQ-054 drew 13 of the 43 findings, 7 of them
revise-level, including every revise finding of its last two rounds. The
census in `SEMANTIC-DELTA.md` traces them to one missing input. Nothing
declares which source record each rendered element belongs to, or what form
the identity takes. So every oracle wording either consulted the
implementation under test or needed judgment.

| Option | Meaning |
|---|---|
| **Evidence first** (recommended) | M9's identity slice 6 first lands, under an implementation authorization, a declared per-source identifier field and a declared attribution for seeded and many-record subjects (such as POC-REQ-051's `region:unmapped-code`). A fresh identity package then specifies POC-REQ-054 over those declarations as reviewed inputs, with an Unknown row for their truth, the precedent POC-REQ-055 set. |
| Settle the form in the specification | A fresh identity package declares the identity form and the attribution rule in the signed text itself. This needs you to choose a form RFC6-1 allows; the design's `repository:<repo>@<rev>:<path>#<objectId>` contains a path, which RFC6-1 bars as a selection identity. |
| Drop it from M9 | No cross-surface identity requirement. RFC6-1, RFC6-3 and RFC6-12 stay Part B2 beliefs. |

### D2 — the ribbon: with the identity, or on its own?

The ribbon's slots fill "only from a subject joined to that claim by its
identity" (the parked text).

| Option | Meaning |
|---|---|
| **With the identity package** (recommended) | It is specified in the same package as POC-REQ-054, since it needs the join. |
| On its own | A separate package specifies the ribbon over a join it declares itself, and so makes the D1 choice for one view. |

### D3 — which M9 slices does this sign-off make eligible?

Your ruling's consequence reads "slices 4–8 after that sign-off", written
for one package. With two packages that sentence names no single sign-off.
[Inferred] Each slice below is matched to the requirement it implements,
from the design's slice list.

| Option | Meaning |
|---|---|
| **4a, 4b and 8 after this sign-off; 5, 6 and 7 after the identity package's** (recommended) | 4a and 4b implement POC-REQ-060's record shape and Inferred arm, and 8 implements POC-REQ-055. 5 is the ribbon, 6 is the identity, and 7 replaces the observed band with links into Orrery by entity id, a cross-surface link the identity package governs. |
| All of 4–8 after this sign-off | Slices 5, 6 and 7 would land with no signed requirement governing cross-surface identity. |
| Something else | Name it. |

Each slice still needs its own implementation authorization.

### D4 — the reading of P-75 Q1

Q1 ruled "one CC-REV-2 package against the three-surface spec only". Your
2026-10-14 direction replaces that one package with this one and a later
identity package. [Observed: as relayed; no decision record holds it yet.]

| Option | Meaning |
|---|---|
| **Record it** (recommended) | A plain owner direction record under `decisions/` names the 2026-10-14 park-and-redraft as narrowing P-75 Q1 to two packages, both against the three-surface spec only. It binds no digest and adds no act row. |
| Leave it as relayed | The register row and this packet carry the direction as relayed. |

**One consequence for P-85, not a question.** P-85's Q3 offers "fold into
P-84's revision" for Trajectory and Orrery release labels. P-84 is parked,
and this package takes nothing from P-85, so that arm has no live target.
Release labels on those surfaces would be a later POC amendment.
