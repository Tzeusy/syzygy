# Semantic delta — one identity, one vocabulary, one epistemic shape (Three-Surface POC)

> **Candidate — binds nothing.** These bytes were drafted under ruling P-75
> (arm A) of the owner's 2026-09-21 direction,
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
> That ruling directs a drafting; it is not a specification amendment act.
> Only the owner's sign-off of this package amends the signed
> three-surface-poc-experience specification (VIS-4). This candidate performs
> no act, authorizes no implementation and edits no signed byte.

**Artifact(s):** the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`, bound since 2026-09-29 by
`.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`.
Proposed bytes exist only as four unified diffs under `proposed/`. The other
two subjects, `.openspec.yaml` and `design.md`, stay byte-identical.

**Stable IDs affected:**

- **Minted:** `POC-REQ-054`, `POC-REQ-055`, and the warrant key
  `POC-DIR-2026-09-21`. The key names the ruling's record file, defined in the
  spec's reader notes beside the two existing `POC-DIR-*` keys.
- **Amended in place (CC-SPEC-3):** `POC-REQ-060`.
- **Not touched:** no other requirement, contract clause, reason, tier or
  identifier is minted, retired or renumbered.

[Observed] Over the 1,924 tracked files at `ab22492`, `POC-REQ-054` and
`POC-REQ-055` occur only in the M9 planning record set, which uses them in the
sense this package gives them (see `IMPACT-LEDGER.md`).

**Change class:** **Normative.** The POC as served today emits relation kinds
outside RFC1-25's table with no flag. Its entity and relationship records also
carry a two-member epistemic union with free-text reasons. Neither would
comply after this amendment. [Observed: the eight kinds in
`packages/three-surface-poc-core/src/poc-seeds.ts` and the `PocEpistemic` type
in `packages/three-surface-poc-core/src/model.ts` at `ab22492`. Inferred: the
compliance consequence.]

**Author:** Claude worker lane for `syzygy-dov.26`.

**Date:** 2026-10-03

## What the ruling settled, verbatim

The P-75 row of the ruling record reads, in part:

> **A** — Q1 one CC-REV-2 package against the three-surface spec only, started
> after lane B's manifest is disposed of; Q2 PWB-REQ-007 reaches only the
> project-shape plane; Q3 the seven outside kinds sit outside the closed
> table, repaired by a new requirement in slice 3's delta plus disclosure,
> never at the bound site; Q4 `Inferred` added as a typed landing zone with
> no production constructor;

and in its consequences column:

> slice 3's delta is drafted only after P-68's manifest is disposed of and
> binds nothing until sign-off; slices 4–8 after that sign-off; slice 5 never
> at catalog fan-out without re-measurement. The bound coverage-matrix row is
> edited on no arm.

[Observed] Lane B's manifest is disposed of. `scripts/check_governance.py`
line 1780 records: "Lane B was declined 2026-10-02 and never performed". The content list — POC-REQ-054, the
POC-REQ-060 amendment, POC-REQ-055 and a ribbon scenario — is the slice-3
design in `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` §"Slice 3 — One
amendment package", which the ruling adopted.

## 1. POC-REQ-054 — one subject identity across the surfaces (new)

**Current meaning.** [Observed] None of the 24 signed requirements names a
link from one surface to another or a shared subject identity. POC-REQ-060's
only scenario presumes sameness without requiring it: "**WHEN** the same
Unknown relationship appears on Polaris, Trajectory, and Orrery". The signed
matrix puts the three RFC6 identity clauses in Part B2 as author beliefs, for
example `RFC6-1 | RFC1-qualified selection-reference identity scheme … POC
builds no cross-surface selection/identity system`. Its own preamble says "A
belief is not a reviewed N/A".

**Proposed meaning.** Every subject carries one identity, held once in the
shared model, and every surface and the machine answer name it by that
identity alone. Where a source authority owns the identity (a work item's
tracker, a code region's observed revision), the model holds that identity
and mints none of its own. This keeps the requirement consistent with
RFC1-9's "the kernel **never mints an identity it does not own**" (bold in
the source), which the signed matrix already maps to POC-REQ-010 and
POC-REQ-012. A link between surfaces resolves, by that identity, to exactly one
element for the same subject. No surface-local handle crosses a boundary as
the identity.

A second paragraph carries the **ribbon**: where a surface renders one claim's
desired, execution and observed states together, each slot is filled only by
a subject joined by the identity. An unfilled slot renders Unknown with its
reason and route, never absent, scored or styled as positive, and the machine
answer carries the same three slots.

The requirement has two scenarios:

- "One subject, one identity on every surface".
- "A three-state view with nothing joined". This is the ribbon scenario the
  ruling names; it is the M9 packet's S6 and S7 joined.

**Clauses it maps, quoted at the accepted bytes** (rule 8):

- **RFC6-1**, at
  `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`
  line 108. Its first bullet (lines 112–115, partly bold in the source)
  reads: "the kernel mints nothing new for selection, and no surface-local
  handle — file path, node index, work-item row, layout coordinate, scene
  object id — is ever a selection identity". Its second bullet (lines
  116–118) reads: "every handle must resolve to a selection reference
  before it crosses a surface boundary, a URL, or an endpoint." The
  surface-handle limb is covered. Two limbs are added as Unknown rows: the
  tuple limb (a reference is RFC 0001's (entity kind, durable entity
  identity), and the POC's entity kinds are not RFC1-5's) and the
  qualifiers limb.
- **RFC6-3**, line 135: "One selection reference resolves **identically in all
  three surfaces**". Only "same entity" is covered. Two limbs are added as
  Unknown rows: same evaluation, same scenario context and same drawer fact
  set; and the skew limb ("must render the skew explicitly — naming both
  evaluation identities").
- **RFC6-12**, line 263: "Every URL-pinned selection is openable in any
  surface". The covered consequence is narrower — the same identity opens the
  subject on every surface that renders it. Two limbs are added as Unknown
  rows: the URL-hint and bookmark limb, and the clause's "subject to
  `not-applicable` per RFC6-5" limb.
- **RFC1-26**, at
  `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
  line 736: "Every rendered internal edge must resolve to its identified
  target (trust floor)". This is applied to links between surfaces.

**Departure from the adopted design: the join key.** The design the ruling
adopted says POC-REQ-054 "Declares the canonical join key", and it labels
slice 6b "The key, slice 3's act" (`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md`
lines 797–798 and 920). This package does **not** declare the key. If the
owner signs it, slice 6b chooses the key's form under POC-REQ-054 with no
further act, where the design expected the form to be in the signed text.
`OWNER-DECISION-PACKET.md` puts this to the owner, and the proposed
`proposal.md` states it as an open question.

**Why the identity is not spelled out.** The M9 packet's slice 6b proposes a
concrete key. The requirement deliberately names "the identity the shared
model mints". It does not name a string form such as a repository path plus
object id, because RFC6-1 bars a file path from being a selection identity.
The form is left to slice 6, where it can be tested against that clause.
[Inferred]

## 2. POC-REQ-055 — every relation kind is named in or flagged outside the closed vocabulary (new)

**Current meaning.** [Observed] The signed matrix's Part A carries the row
`RFC1-26 | Relations outside the closed table don't exist; no prose-widening
| covered | POC-REQ-052`. POC-REQ-052's required behavior is that Orrery
"SHALL NOT render an edge, adjacency, grouping, or emphasis encoding a
relationship the shared model does not hold". That is anti-fabrication. It
does not close the vocabulary, as P-75 Q3 ruled.

[Observed at `ab22492`] The POC emits eight kinds over nine relationships:
`contains`, `governed-by`, `mapped-to` (×2), `materializes-as`, `changes`,
`verified-by`, `satisfies-at-runtime`, `coverage-unknown`. Only `contains` is
one of the thirty backticked relation tokens in the first column of RFC1-25's
table. That table has 26 data rows, at lines 596–621 of the RFC-0001 module;
the count was taken by script this session.

**Proposed meaning.** Every emitted kind is either an RFC1-25 relation name,
emitted with source and target in the roles the table assigns, or carries an
explicit outside-closed-vocabulary flag with a reason. The flag is carried in
the machine answer and rendered wherever the kind is. A flag discloses and
never widens; RFC1-26 reads "no drafter, reviewer, adapter, or profile may
widen the core vocabulary by prose", and this requirement adds no relation to
the table.

**The repair, not at the bound site.** The signed row is kept byte for byte.
The proposed matrix adds two things:

- an amendment row beneath it that maps the *disclosure* the ruling chose to
  POC-REQ-055;
- a separate Unknown amendment row for closure itself, "No relation outside
  the closed table is emitted at all". POC-REQ-055's oracle observes
  naming-or-flag, not absence, and the ruling chose disclosure rather than
  removal;
- a dated **amendment disclosure** paragraph after the Part A totals, telling
  a reader which rows to read.

The RFC1-25 amendment row likewise claims only what the oracle observes:
closed names are emitted in a role pair the table assigns them, and every
other kind is flagged. The table assigns several role pairs to some
relations, such as `contains`/`part_of`, so the requirement checks against
the set.

The builder fails if the signed row changes (`--selftest`, mutant "bound row
edited").

## 3. POC-REQ-060 — one encoding, one record shape, three labels (amended in place)

**Current meaning.** [Observed] "The three surfaces SHALL draw from one
declared set of design tokens, and SHALL encode epistemic states (Observed,
Unknown, and their reasons) identically wherever they appear." The
requirement governs encoding, not record shape, and enumerates two of
doctrine's three labels.

**Proposed meaning.** The amended requirement keeps the signed sentence and
extends it:

- **Labels:** "Observed, Inferred, Unknown".
- **Record shape:** every entity, relationship and claim carries one record
  shape in the model and the machine answer. It holds a label from the closed
  three; a tier from RFC2-25's closed six where one applies, inside its parent
  label; and, where Unknown, exactly one primary reason from RFC2-24's closed
  twelve with its route.
- **Inferred:** it arises only from an agent's assertion, which it names,
  never counts toward an Observed total or clears an Unknown, and renders
  distinctly. The oracle names a procedure for each of these limbs:
  - a check that the record names an agent assertion;
  - a recount of every Observed total without the record;
  - a before-and-after comparison of each Unknown it addresses;
  - an encoding comparison.

The signed scenario "Unknown looks the same everywhere" is preserved verbatim;
the builder checks this. A second scenario is added: "An agent assertion stays
Inferred".

**Q4's landing zone.** The case says, "While no agent has asserted anything,
the Inferred limbs are exercised by a fixture record injected at the model
seam." No production constructor is required, so the requirement is
satisfiable today with zero Inferred records. This follows Q4: "`Inferred`
added as a typed landing zone with no production constructor". Doctrine's
rule, at `.syzygy/governance/doctrine/trust-and-evidence.md` line 25, is "An
LLM assertion is Inferred, never Observed". RFC2-25's `asserted-by-worker`
row is "Visible, never green, challengeable, never a status input".

**Q2's plane boundary.** The record shape is set here and not by reference to
PWB-REQ-007, because Q2 ruled that "PWB-REQ-007 reaches only the
project-shape plane". Freshness and secondary Unknown annotations, which
PWB-REQ-007 carries, are **not** part of this shape. The matrix adds them as
Unknown rows under RFC6-14 and RFC2-24 rather than claiming them.

The same goes for the RFC2-25 limbs the oracle does not observe. Each tier's
authority — for example, only `gate-backed` supports a positive status — is
an Unknown row. So is the `asserted-by-worker` row's "challengeable" and
"never a status input" limb. The signed RFC6-14 row's fold note is preserved,
with a second disclosure saying which of its limbs the amendment now
covers.

## Coverage matrix, computed

[Observed — computed by `scripts/build_three_surface_poc_identity_amendment.py`
over the proposed bytes; the same figures are printed in the proposed file and
checked by `--check`]

| | Signed | Proposed |
|---|---:|---:|
| Part A clauses (= `contracts[]` union) | 74 | 78 |
| Part A rows: covered / Unknown | 92 / 15 | 102 / 28 |
| Part B1 clauses (rows) | 27 (28) | 27 (28) |
| Part B2 clauses | 223 | 219 |

Four Part B2 beliefs move to Part A because a requirement now covers one of
their consequences: RFC2-25, RFC6-1, RFC6-3 and RFC6-12. Every other signed
row is unchanged, and every added row carries the words "Amendment row". The
builder checks both.

The generated `GOVERNING-DEPENDENCIES.md` is regenerated over the proposed
spec. It now reads 26 requirements; the contracts class goes from 74 to 78.

## What this does not do

- It authorizes no implementation. Per the ruling, M9 slices 4–8 start only
  after this package's sign-off. Slice 5's ribbon is never at catalog fan-out
  without re-measurement.
- It does not schedule slices or spend page headroom. Q5's byte order is an
  implementation sequence, not specification text.
- It mints no N/A judgment. Every added Unknown row stays Unknown.
- It edits no performed act's record, no PWB artifact, no doctrine and no
  contract.

## Residuals the sign-off change must carry

Each item below is [Observed] at `ab22492`. It is named here so the signing
change does not discover it.

1. **The sign-off route.** The 2026-10-02 versioned sign-off direction names
   "the PWB specification deltas, the observer registry entry and the
   contract successors queued behind them". A three-surface specification
   amendment is not in that list. Signing this package by version tag
   therefore needs either the owner's word that Scope A reaches it, or the
   phrase-and-digest form with a dedicated recorder. That choice is the
   owner's; `OWNER-DECISION-PACKET.md` puts it.
2. **`scripts/check_spec_reconciliation.py`.** R3 hard-codes the POC-REQ
   census at 24, and R2 binds the six subjects to the readability successor's
   rows. Both fail after `--apply` until the signing change registers this
   package as the POC child's successor and updates `census.json`.
3. **`scripts/record_versioned_signoff.py`.** If the version-tag route is
   chosen, the package must be added to `real_packages()`, which today lists
   only PWB packages.
4. **Implementation consumers of POC-REQ-060.** Three implementation files
   cite POC-REQ-060 (`IMPACT-LEDGER.md`). They are affected only when slices
   4a/4b land, not by sign-off.
