# Semantic delta — one relation vocabulary, one epistemic record shape (Three-Surface POC)

> **Candidate — binds nothing.** These bytes were drafted on 2026-10-14
> under ruling P-75 (arm A) of the owner's 2026-09-21 direction,
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
> as narrowed by the owner's direction of 2026-10-14 that parked the first
> package drafted under it (below). Neither is a specification amendment
> act. Only the owner's sign-off of this package amends the signed
> three-surface-poc-experience specification (VIS-4). This candidate
> performs no act, authorizes no implementation and edits no signed byte.
>
> **Round-1 findings repaired once on 2026-10-15, unconfirmed pending round
> 2.** Round 1 (docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md)
> was `REVISE`; on the owner's direction of 2026-10-15 ("One cycle"
> [Observed: as relayed by the lead session; not recorded under
> `decisions/`]) all nine findings, notes included, were repaired once.
> `ROUND-1-DISPOSITIONS.md` maps each finding to its repair, and round 2 is
> briefed in `REVIEW-BRIEF.md` §"Round 2".

**Artifact(s):** the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`, as they stand at
`7460aec8` with the P-97 block-provenance and P-100 governing-intent
amendments applied (each signed v1.0 on 2026-10-14). Proposed bytes exist
only as four unified diffs under `proposed/`. The other two subjects,
`.openspec.yaml` and `design.md`, stay byte-identical.

**Stable IDs affected:**

- **Minted:** `POC-REQ-055`, and the warrant key `POC-DIR-2026-09-21`, which
  names the ruling's record file and is defined in the spec's reader notes
  beside the two existing `POC-DIR-*` keys.
- **Amended in place (CC-SPEC-3):** `POC-REQ-060`.
- **Not minted:** `POC-REQ-054`. The parked package used it for the subject
  identity requirement, which is deferred (§"Deferred scope"). No proposed
  byte names it, and the builder fails if one does.
- **Not touched:** no other requirement, contract clause, reason, tier or
  identifier is minted, retired or renumbered.

**Change class:** **Normative.** [Observed at `7460aec8`] The POC emits nine
relationships over eight kinds (`packages/three-surface-poc-core/src/poc-seeds.ts`
lines 192–264), none admitted by RFC1-25's table as this package reads it
(§1), and none flagged. Its entity and relationship records carry a
two-member epistemic union (`PocEpistemic`,
`packages/three-surface-poc-core/src/model.ts` line 68) with no Inferred
arm. [Inferred] Neither would comply after this amendment; each is a target
of an M9 implementation slice, not of this package.

**Author:** Claude, fresh drafter for P-84's redraft, on the owner's
2026-10-14 direction.

**Date:** 2026-10-14; round-1 repairs 2026-10-15.

## Why this package exists: the owner's direction, verbatim as relayed

On 2026-10-14, in the lead session, the owner answered a structured question
on P-84 with: "Park, redraft narrower — Stop this package. A fresh drafter
redrafts it from the 43 findings as a smaller package, for example the
record-ownership machinery split from 055/060." [Observed: as relayed to
this drafter by the lead session; not recorded under `decisions/`.]

The parked package is
`../three-surface-poc-identity-amendment/`. Its head carries the park mark;
its history is kept unedited beneath it.

## Findings census — what kept failing, and why

The input is the 43 findings of the parked package's six fresh-context
rounds. Each round's verdict is `REVISE`, read from line 4 of each raw,
`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-1-RAW.md` through
`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-6-RAW.md`. The finding headings
were read from the raws; the levels from each raw's own label. Each finding
is placed in exactly one theme, by the requirement its body addresses; the
two findings whose bodies address both POC-REQ-054 and POC-REQ-060 form their
own row. Seven headings name no requirement, so a reader applying a
heading-only rule cannot place them; their placements are listed here: 3
and 4 in "POC-REQ-054 and POC-REQ-060 together", 6 and 35 in "POC-REQ-060",
and 7, 36 and 41 in "POC-REQ-054". [Observed: the seven headings re-read
from the round-1, round-5 and round-6 raws on 2026-10-15; placements copied
from the table below. Round 1's reviewer found that the stated heading rule
did not produce the table (finding 3 of
R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md).]

| Theme | Findings | Count | Revise-level | Last round with a finding | Last revise |
|---|---|---:|---:|---:|---:|
| POC-REQ-054: identity, ownership, attribution, links, ribbon | 1, 5, 7, 12, 15, 24, 26, 33, 34, 36, 39, 40, 41 | 13 | 7 (1, 5, 12, 26, 33, 39, 40) | 6 | 6 |
| POC-REQ-054 and POC-REQ-060 together | 3, 4 | 2 | 2 | 1 | 1 |
| POC-REQ-055: relation vocabulary | 2, 8, 13, 20, 21, 32 | 6 | 3 (2, 13, 20) | 4 | 3 |
| POC-REQ-060: record shape and Inferred | 6, 14, 16, 17, 25, 27, 28, 31, 35 | 9 | 2 (27, 28) | 5 | 4 |
| Builder phrase guards | 18, 22, 30, 37, 42 | 5 | 0 | 6 | — |
| Citations, overstatements, stale sentences | 9, 10, 11, 19, 23, 29, 38, 43 | 8 | 0 | 6 | — |
| **Total** | | **43** | **14** | | |

[Observed: counted from the table rows above; 13 + 2 + 6 + 9 + 5 + 8 = 43
and 7 + 2 + 3 + 2 = 14, which matches the 14 findings labelled `revise`
across the six raws' headings.]

**What the census shows.**

1. **The identity requirement never converged.** [Observed] POC-REQ-054
   carries 7 of the 14 revise findings and every revise finding of rounds
   5 and 6. [Inferred] Each repair defined one term and exposed the next.
   The requirement needs an oracle independent of the implementation
   (CC-SPEC-4), so round 1 (finding 4) asked for expected identities
   derived from source records. That needed a rule attributing each element
   to its subject (24, round 3). The rule needed the machine answer's
   records too (26, 33), and a test for which subjects a source "owns" (26).
   That test needed the field each source owns (36, round 5). Round 6 then
   found three things. The declaring slice is the implementation under test
   (39). "Source record" is undefined, so seeded subjects such as POC-REQ-051's
   `region:unmapped-code` falsify the new limb (40). And the decision rule
   has no Unknown outcome (41). The root is one missing input: the POC has
   no declared, reviewed mapping from rendered elements to source records,
   and no declared identity form (Departure 1 of the parked packet left the
   form to slice 6b). Without that input, every oracle wording either
   consults the implementation or needs judgment.
2. **The relation vocabulary converged.** [Observed] POC-REQ-055's last
   revise finding was 20, in round 3. Round 4 had one note on it (32), and
   rounds 5 and 6 none. [Inferred] Its one undecidable input, the
   kind-to-class correspondence, was disclosed as an Unknown row in round 3.
   Round 6 cited that disposal as the precedent POC-REQ-054 lacked (finding
   39).
3. **The record shape converged.** [Observed] POC-REQ-060's last revise
   findings were 27 and 28, in round 4. Round 5 had one note (35), and
   round 6 none. [Inferred] Its remaining dependence on POC-REQ-054 is one
   phrase, "whose two sets of Unknown records by identity must be equal".
   It reads "identity" from a requirement this package does not carry, so
   the phrase is rewritten here (§2).
4. **The guard and prose findings were second-order.** [Inferred] All 13
   were notes. Every guard finding (18, 22, 30, 37, 42) was about repair
   text added after the round before. Every stale-sentence finding (38, 43)
   was about a sentence a later cycle made false. They scale with the
   number of repair cycles, not with the content. This package starts with
   one round, so it carries no repair history, and its builder fails if any
   phrase guard lacks a mutant of its own (§"Mechanics").

**The slice this justifies.** The owner's example split, the
record-ownership machinery out, POC-REQ-055 and POC-REQ-060 in, is the
narrowest coherent slice the census supports.

- **Coherent.** Both parts are "one vocabulary" obligations on what the
  shared model emits: a closed relation vocabulary, and a closed epistemic
  vocabulary in one record shape. Neither needs a subject identity. Each
  rendering limb does need a declared attribution of a rendered element to
  a served `id`, which round 1 found missing (its finding 2); the repair
  names a declared marker for it, in POC-REQ-020's form, and lists every
  unmarked rendering as an Unknown row (§1 and §2).
- **Valuable under P-75 (A).** It delivers Q3 (the outside kinds repaired by
  a new requirement plus disclosure, the bound row unedited), Q4 (Inferred
  as a typed landing zone with no production constructor) and Q2 (the POC's
  record shape set here, not by reference to PWB-REQ-007). It is the
  specification M9 slices 4a, 4b and 8 implement.
- **Decidable, on the census.** No round after round 4 found a revise-level
  defect in either part.

Narrower slices were considered. [Inferred]

- **POC-REQ-060 alone** would leave P-75 Q3, which the ruling made the
  reason for a new requirement, unrepaired, and the closure row's
  disclosure would have nothing to point at.
- **POC-REQ-055 alone** would leave Q4's Inferred arm with no landing zone.

A wider slice was considered too. **Keeping a minimal POC-REQ-054**, one
identity value per subject with no ownership limb, is the census's failing
core. Its value-free limbs still need the element-to-subject attribution
that findings 24, 33 and 40 show is undefined.

## 1. POC-REQ-055 — every relationship is named in or flagged outside the closed vocabulary (new)

**Current meaning.** [Observed] The signed matrix's Part A carries the row
`RFC1-26 | Relations outside the closed table don't exist; no prose-widening
| covered | POC-REQ-052`. POC-REQ-052's required behavior is that Orrery
"SHALL NOT render an edge, adjacency, grouping, or emphasis encoding a
relationship the shared model does not hold". That is anti-fabrication. It
does not close the vocabulary, as P-75 Q3 ruled.

[Observed at `7460aec8`] The POC emits eight kinds over nine relationships:
`contains`, `governed-by`, `mapped-to` (×2), `materializes-as`, `changes`,
`verified-by`, `satisfies-at-runtime`, `coverage-unknown`. RFC1-25's table
has 26 data rows, at lines 596–621 of
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`.
Of the eight kinds, only `contains` names a relation in its first column.

**`contains` does not comply either.** [Observed] The one `contains`
relationship runs from `project:butlers` to a capability
(`packages/three-surface-poc-core/src/poc-seeds.ts` lines 194–199). The
`contains` / `part_of` row (line 596) assigns six role pairs, none of them
Project→Capability, and its rule reads "cross-authority nesting must use a
typed relation". So none of the nine relationships emitted at drafting
complies: seven by kind, one by role pair.

**Proposed meaning.** Every emitted relationship either carries an RFC1-25
relation name with its source and target in a role pair the table assigns,
or carries an explicit outside-closed-vocabulary flag with a reason. The
flag is carried in the machine answer and rendered in every rendered element
that marks the relationship. The text was the parked package's POC-REQ-055,
unchanged, since rounds 4 to 6 of the parked package found nothing in it to
repair. Round 1 of this package then found its rendering limb
("rendered wherever the relationship is rendered") quantified over a
population no sweep enumerates (finding 2).

**Round-1 repair: the marked rendering population.** An element *marks* a
relationship when it carries the relationship's served `id` in one of the
surfaces' declared relationship markers. The sweep extracts every such
element, and the complete marker population is its denominator, which the
check counts and reports. This is POC-REQ-020's declared-parity-marker
form. A rendering that carries no marker is outside the sweep, the
requirement says so, and an RFC1-26 Unknown row carries "A flagged
relationship rendered in an element that carries no declared relationship
marker shows its flag and reason there". The covered RFC1-26 disclosure row
is narrowed to the machine answer and the marked elements. [Inferred] The
other option the reviewer named, requiring every rendering to carry a
marker, would still leave an unmarked rendering invisible to the sweep;
packet Question 2 puts the choice to the owner.

RFC1-25's Domain → Range column is written in RFC 0001's classes, and the
POC's entity kinds are not those classes. The role-pair check therefore
reads through a **checked-in declaration** mapping each shared-model entity
kind to the RFC 0001 class it corresponds to, or to none. That declaration
makes a truth claim, and no stated procedure decides it. The slice that
emits the relationships (M9 slice 8) also writes it. So the requirement
decides role pairs only *as read through* the declaration, and an Unknown
amendment row carries "The declared kind-to-class correspondence matches
RFC 0001's class definitions". That row now says in its own words that the
declaring slice is the one under test, the point round 6 (finding 39) made
about the parallel declaration in POC-REQ-054. A flag discloses and never
widens: RFC1-26 reads "no drafter, reviewer, adapter, or profile may widen
the core vocabulary by prose" (lines 741–742), and this requirement adds no
relation to the table.

**The repair, not at the bound site.** The signed row is kept byte for
byte. The proposed matrix adds:

- an amendment row beneath it, mapping the *disclosure* the ruling chose to
  POC-REQ-055;
- a separate Unknown row for closure itself, "No relation outside the
  closed table is emitted at all", because the oracle observes
  naming-or-flag, not absence, and the ruling chose disclosure;
- Unknown rows for the limbs POC-REQ-055 does not decide: the
  correspondence's truth and a closed name honouring its row's semantic
  class and rule (under RFC1-25), and no re-typing (under RFC1-26);
- a dated **amendment disclosure** paragraph after the Part A totals,
  telling a reader which rows to read.

**Departure from the adopted design: role pairs, not only kinds.** The
design's slice 3 item 3 reads "Every emitted kind is either an RFC1-25 name
or carries an explicit out-of-vocabulary flag"
(`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` lines 804–807). POC-REQ-055
also checks the role pair, which is why `contains` is flagged too. The
widening is offered because RFC1-26 forbids re-typing and the design's
slice 8 treats direction as material (lines 973–977) [Inferred]. If the owner
wants the kind check alone, the answer is "Revise".

## 2. POC-REQ-060 — one encoding, one record shape, three labels (amended in place)

**Current meaning.** [Observed] "The three surfaces SHALL draw from one
declared set of design tokens, and SHALL encode epistemic states (Observed,
Unknown, and their reasons) identically wherever they appear." It governs
encoding, not record shape, and names two of doctrine's three labels. Since
the P-100 sign-off, POC-REQ-014 decides its governing-intent encoding
against this requirement's declared table.

**Proposed meaning.** The signed sentence stays, with Inferred added to its
label list, and is extended:

- **Record shape, on entities and relationships.** Every entity and every
  relationship carries one record shape in the model and the machine
  answer. The record holds a label from the closed three, and a tier from
  RFC2-25's closed six where the record carries one, inside its parent
  label. Where Unknown, it holds exactly one primary reason from RFC2-24's
  closed twelve with its route. The sweep's denominator is the elements of
  the machine answer's entity and relationship lists, not the records that
  exist, so an element with no record, or with two, falsifies it.
- **Inferred.** It arises only from an agent's assertion, which it names.
  It never counts toward an Observed total or clears an Unknown, and it
  renders distinctly. The oracle names a procedure for each limb, and a
  fixture record injected at the model seam exercises them while no agent
  asserts anything.

The signed scenario "Unknown looks the same everywhere" is preserved
verbatim, and the builder checks this. A second scenario, "An agent
assertion stays Inferred", is added.

**Three changes from the parked package's POC-REQ-060.** Each removes a
dependence on something this package no longer carries, or on a term the
POC specification does not define. [Inferred]

1. **"Entity, relationship and claim" becomes "entity and relationship".**
   The POC specification names two kinds of claim the machine answer
   serves. The project-shape plane's claims are one, and P-75 Q2 ruled that
   "PWB-REQ-007 reaches only the project-shape plane". The other is the
   governing-intent claim the P-100 amendment signed: its RFC2-24 row reads
   "on every served item's governing-intent claim" and an RFC8-24 row reads
   "the governing-intent claim on every work item" (signed
   `CONTRACT-COVERAGE.md`). That claim sits on each work item, in the
   machine answer's `workItems`, outside the entity and relationship lists
   (`packages/three-surface-poc-core/src/model.ts` lines 185–189)
   [Observed], and POC-REQ-014 already decides its encoding against this
   requirement's declared table. Setting a record shape on either kind here
   would put a second requirement on records another requirement governs.
   (Round 1's finding 5 found that the first draft of this sentence said
   the specification defines no claim at all, which P-100 made false.) The
   Scope says "No other epistemic value the machine answer
   serves is in the record-shape population". RFC6-14's own population is
   "Every entity and claim instance", so its claim and other-value limbs are
   an Unknown row. The narrowing matches the adopted design's slice 4a,
   which replaces `PocEpistemic` on `PocEntity.epistemic` and
   `PocRelationship.epistemic` (design lines 830–831).
2. **The Unknown recount is named by served identifier, not by identity.**
   The parked text's "two sets of Unknown records by identity" leaned on the
   subject identity POC-REQ-054 defined. The recount now compares "the
   entity and relationship records labelled Unknown with and without it,
   whose two sets, each member named by the identifier the machine answer
   serves it under and the injected record excluded, must be equal". Every
   entity and relationship already carries an `id`
   (`packages/three-surface-poc-core/src/model.ts` lines 94 and 112)
   [Observed]. An Unknown elsewhere in the machine answer is outside that
   recount, and the RFC2-25 rows say so: the covered "never a status input"
   row is narrowed to the entity and relationship records, and a new
   Unknown row carries the rest.
3. **"Where one applies" becomes "where the record carries one".** Whether
   a tier "applies" took judgment. RFC2-25 itself says "an untier'd claim
   renders at its bare label", so the tier is optional. The oracle now
   validates a tier only where one is present.

**Round-1 repairs to POC-REQ-060.** [Inferred, each from the named finding
of R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md]

- **The Inferred rendering limb reads the marked population** (finding 2).
  An element marks a record when it carries the record's served `id` in a
  declared record marker. The Inferred encoding is compared in every
  element that marks the injected record, that marker population is the
  denominator, and an RFC2-25 Unknown row carries every unmarked rendering.
- **The three label entries are pairwise distinct, and "the legend" is
  "the declared table"** (finding 4). The required behaviour says "The
  declared token/encoding table SHALL give Observed, Inferred and Unknown
  three pairwise distinct entries", and the oracle compares them pairwise.
  The Inferred limb names "the declared table's Inferred entry". This also
  closes the latent Observed-against-Unknown gap the signed table already
  had.
- **"Observed total" has a population** (finding 7). The Scope says "An
  Observed total is every count the machine answer serves, except a count
  the machine answer declares to be of Inferred records", and each recount
  must equal the count served with the injected record present. The
  scenario says "changes no Observed total the machine answer serves".
- **The Unknown recount is keyed by list and identifier** (finding 7).
  Each member is "keyed by the list it is served in and the identifier the
  machine answer serves it under", so an `id` shared across the two lists
  cannot mask a cleared Unknown.
- **The machine answer is the shared model's observable** (finding 9). The
  obligation keeps "in the shared model and in the machine answer"; the
  Scope adds "The shared model's records are observed through the machine
  answer, which serves the shared model's fact set (POC-REQ-020); no check
  reads the shared model directly."

**Q4's landing zone.** The case says, "While no agent has asserted
anything, the Inferred limbs are exercised by a fixture record injected at
the model seam." No production constructor is required, so the requirement
is satisfiable with zero Inferred records. This follows Q4: "`Inferred`
added as a typed landing zone with no production constructor". The proposed
`proposal.md` and `OWNER-DECISION-PACKET.md` both say a production
constructor needs its own owner act. Doctrine's rule, at
`.syzygy/governance/doctrine/trust-and-evidence.md` line 25, is "An LLM
assertion is Inferred, never Observed". RFC2-25's `asserted-by-worker` row
reads "Visible, never green, challengeable, never a status input".

**A narrowing of doctrine's Inferred, stated.** Doctrine defines Inferred
more widely: "the output of a declared inference process, carrying its
inference provenance" (`trust-and-evidence.md` lines 84–85). It asks the
inferred layer to record "the model, version, and inputs that produced it"
(lines 115–116). POC-REQ-060 admits only an agent's assertion, and requires
only that the record name the assertion it arises from. This follows the
design's Q4 framing. No production constructor exists, so there is no model
or version to record yet. A constructor's own act is the place to add
doctrine's full provenance. [Inferred]

The narrowing has two more limbs, which round 1 found unstated (finding 8).
Doctrine says "Deterministic facts and probabilistic inferences are
computed and stored apart" and that the inferred layer "is a separate
artifact … and is excluded from the VIS-7 identity test"
(`trust-and-evidence.md` lines 111–116). POC-REQ-060 instead places an
Inferred record inline, on the shared model's entities and relationships,
and says nothing of its storage or of the VIS-7 identity test. With a
fixture-only population and no production constructor this binds nothing
today. [Inferred] Both limbs, separate storage and exclusion from the
VIS-7 identity test (which POC-REQ-004's determinism and any
response-identity digest would read), are deferred to the production
constructor's own act, with the provenance limb.

**Q2's plane boundary.** The record shape is set here and not by reference
to PWB-REQ-007. Freshness and secondary Unknown annotations, which
PWB-REQ-007 carries, are **not** part of this shape. The matrix lists them
as Unknown rows under RFC6-14 and RFC2-24.

**RFC2-25, limb by limb.** RFC2-25 moves from Part B2 to Part A. Each tier
keeps its authority, for example only `gate-backed` supports a positive
status, and that is an Unknown row. Each word of the `asserted-by-worker`
row's Authority column has its own row:

- **"never green"** — covered, on a reading: the claim renders with the
  declared table's Inferred entry, which differs from its Observed entry, in
  every rendered element that marks it. A rendering with no declared record
  marker is a separate Unknown row.
  The row carries an `[Inferred]` tag saying that RFC2-25's `gate-backed` row
  also lists "green" among positive status claims. On the reading "never
  rendered as a positive status" this limb is the Unknown positive-status
  row.
- **"never a status input"** — split. It is covered for the two
  computations the POC performs: no Observed total, and no Unknown cleared
  among the entity and relationship records. Two Unknown rows hold the rest:
  any positive status, and clearing an Unknown outside the entity and
  relationship lists.
- **"Visible"** — Unknown. No requirement requires an Inferred record to
  appear.
- **"challengeable"** — Unknown. The POC has no challenge mechanism.

The tier's Semantics column, "An LLM worker's assertion of an outcome with
no retained artifact", has an Unknown row, because the oracle checks that a
record *names* an assertion, not that it *arose* from one. The other five
tiers' Semantics cells have one Unknown row together, "A record carries a
tier only where that tier's Semantics column holds", because the oracle
validates tier membership and nesting only: a record tagged `gate-backed`
with no gate artifact, or `suspended` with no open challenge or
contradiction, passes it. (Round 1's finding 1 found that row missing.) The
signed RFC6-14
row's fold note is preserved, with a second disclosure saying which of its
limbs the amendment now covers.

**POC-REQ-014.** [Inferred] Since P-100, POC-REQ-014's encoding arm reads
"none carries an encoding the table gives any other state". Adding the
Inferred entry to POC-REQ-060's table adds one more state that arm excludes.
That arm can pass only if the table's Unknown entry differs from every other
entry, which round 1 found unrequired (finding 4); POC-REQ-060 now requires
the three label entries to be pairwise distinct, so it is decidable.
POC-REQ-014's text and its RFC2-24, RFC8-23 and RFC8-24 rows are unchanged,
and the builder fails if its block moves. The P-100 round-3 raw (note 4)
asked that its encoding arm be re-judged against an amended POC-REQ-060, so
the review brief asks the reviewer to do that.

## Coverage matrix, computed

[Observed — computed by
`scripts/build_three_surface_poc_vocabulary_epistemic_amendment.py --check`
over the proposed bytes, and re-counted by a separate script that imports
nothing from the builder]

| | Signed | Proposed |
|---|---:|---:|
| Part A clauses (= `contracts[]` union) | 77 | 78 |
| Part A rows: covered / Unknown | 98 / 24 | 105 / 42 |
| Part B1 clauses (rows) | 28 (29) | 28 (29) |
| Part B2 clauses | 219 | 218 |

One Part B2 belief, RFC2-25, moves to Part A because a requirement now
covers one of its consequences. RFC6-1, RFC6-3 and RFC6-12, which the parked
package moved for POC-REQ-054, stay in Part B2 as signed, and the builder
fails if any other Part B2 row moves. Every other signed row is unchanged.
All 25 added rows carry the words "Amendment row (vocabulary and record
shape)", distinct from the "Amendment row" marks P-100 left. Seven are
covered and 18 Unknown; round 1's repairs added three of the Unknown rows
(the tier-Semantics row, and one unmarked-rendering row each under RFC1-26
and RFC2-25).

Some signed lines move because they print figures computed from the rows:
the RFC2 and Total family-table rows, and the five lines the builder lists
in `COMPUTED_LINES`. The builder recomputes each replacement and checks it.

The generated `GOVERNING-DEPENDENCIES.md` is regenerated over the proposed
spec. It reads 26 requirements, and its contracts class goes from 77 to 78.

## Deferred scope

Each item below is something P-75 (A) or its adopted design named and this
package leaves out. Each carries an owner question in
`OWNER-DECISION-PACKET.md` §"Deferred scope".

1. **POC-REQ-054, one subject identity across the surfaces.** This covers
   the identity, the ownership and attribution rules, the link-resolution
   limb, and the RFC6-1, RFC6-3 and RFC6-12 consequences that would move out
   of Part B2. The census says why: it needs a declared element-to-source
   attribution and a declared identity form that the specification does not
   yet have (packet question D1).
2. **The ribbon scenario**, the per-claim view of the desired, execution
   and observed states. Its slots fill "only from a subject joined to that
   claim by its identity", so it cannot be specified before the identity
   (packet question D2).
3. **The RFC1-26 cross-surface link row**, "A link between surfaces
   resolves to the identified subject on the target surface". It was
   POC-REQ-054's.
4. **The join key.** The design's slice 6b key, and the parked packet's
   Departure 1, go with item 1.

## What this does not do

- It authorizes no implementation. Signing a POC amendment starts none
  (`OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`, "Bounds"), and
  which M9 slices it makes eligible is packet question D3.
- It mints no N/A judgment. Every added Unknown row stays Unknown.
- It edits no performed act's record, no PWB artifact, no doctrine and no
  contract. It edits nothing in the parked package except that package's
  head status mark.

## Residuals the sign-off change must carry

Each item below is [Observed] at `7460aec8`. It is named so that the signing
change does not have to discover it.

1. **The sign-off route.** Version tag under Scope A, through the POC
   extension: "A Three-Surface POC specification amendment, a package that
   patches `openspec/changes/three-surface-poc-experience/`, may be signed
   by version tag under Scope A"
   (`.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`,
   direction item 1). That record names P-84 and P-100 as covered, not this
   package by name. Its item 1 reaches this package by its definition.
2. **`scripts/record_versioned_signoff.py`.** The package must be added to
   `real_packages()` with that record as its `extension`, as P-97's entry
   is.
3. **`scripts/check_spec_reconciliation.py`.** Its R3 census pins the POC
   family at 25 requirements and 26 scenarios (`EXPECTED_TOTALS`), and its
   R2 chain composes the POC child's versioned successors. After `--apply`
   the spec reads 26 requirements and 28 scenarios, so both need this
   package as the next link after P-100's, with `census.json` regenerated. [Inferred: from the P-97 and
   P-100 signing changes; the chain entry is the signing change's to write.]
4. **The parked package.** Its four patches touch the same lines this
   package's do (the reader notes, the POC-REQ-060 block, and the RFC1-25,
   RFC1-26, RFC2-24, RFC2-25 and RFC6-14 rows). It is parked, so no
   composition order is declared. Any later identity package must be drafted
   over whatever this one leaves in the tree.
5. **Implementation consumers of POC-REQ-060.** Six implementation files
   cite it (`IMPACT-LEDGER.md`). They are affected only when slices 4a and 4b
   land, not by sign-off.
