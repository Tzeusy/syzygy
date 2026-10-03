> # Record beside the package — not authority, binds nothing
>
> Dispositions of the first fresh-context review of the Three-Surface POC
> identity amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 1 dispositions — Three-Surface POC identity amendment

- **Reviewed commit:** `26b0b8432667c1ac61c796b7ebebc656d75fee27`.
- **Verdict (raw line 4):** `REVISE`. There are five revise findings (1–5)
  and six notes (6–11), with no blocking finding.
- **Effect:** every finding below is repaired in the package. The repair
  retires the round-1 review (rule 10), so round 2 reads the repaired bytes.
  A figure written here was re-derived from the repaired bytes by
  `scripts/build_three_surface_poc_identity_amendment.py --check`. None was
  copied from the raw.

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-1-RAW.md

## Dispositions

### 1 — POC-REQ-054 required the model to mint identities RFC1-9 says it never mints

**Accepted.** The requirement now reads "one identity, held once in the
shared model". It adds that where a source authority owns the identity, the
model holds that identity and mints none of its own. The delta quotes RFC1-9
and RFC6-1's "the kernel mints nothing new for selection" limb. RFC6-1's
tuple limb is a new Unknown amendment row.

### 2 — the RFC1-25 row and the disclosure claimed closure the oracle does not observe

**Accepted.** Three repairs:

- The RFC1-25 amendment row now claims what POC-REQ-055's oracle observes:
  naming in an assigned role pair, or a flag.
- The RFC1-26 amendment row and the disclosure call the flag "the disclosure
  the ruling chose as the repair".
- A new Unknown amendment row carries closure itself: "No relation outside
  the closed table is emitted at all". The builder now fails if that row is
  missing or not Unknown (mutant "closure claimed covered").

The signed RFC1-26 row is unchanged.

### 3 — uncovered limbs of newly mapped clauses not listed

**Accepted.** These are added as Unknown amendment rows:

- RFC2-25: per-tier authority semantics;
- RFC2-25: the `asserted-by-worker` claim is "challengeable and never a
  status input". The covered row is narrowed to Observed-total exclusion and
  never clearing an Unknown;
- RFC6-3: same evaluation, scenario context and drawer fact set;
- RFC6-12: the RFC6-5 `not-applicable` limb;
- RFC6-1: the tuple limb (see finding 1).

Part A is now 130 rows over 78 clauses: 102 covered, 28 Unknown. These are
the builder's computed figures.

### 4 — oracles without a deciding procedure, or consulting the implementation

**Accepted.**

- **POC-REQ-054.** The oracle independence now has the checker derive each
  subject's expected identity, and each slot's expected join, from the
  source records the model reads. It never reads the machine answer or a
  renderer for these. The Oracle line compares against those derived values.
- **POC-REQ-060.** The required behavior adds that an Inferred record names
  the agent assertion it arises from. The Oracle now names a procedure for
  each Inferred limb: provenance check, recount of Observed totals without
  the record, before/after comparison of each addressed Unknown, and encoding
  comparison. The Falsifier's "arising from a non-agent source" becomes
  "naming no agent assertion", which that procedure decides.

### 5 — departure from the adopted design on the join key not disclosed to the owner

**Accepted.** `OWNER-DECISION-PACKET.md` now has a section "One departure
from the design you adopted". It names the departure, the reason (RFC6-1's
path bar) and the consequence: slice 6b picks the form with no further act.
It also offers "Revise" for an owner who wants the form in the signed text.
The delta carries the same section with the design's line numbers. The
proposed `proposal.md` states the form as an open question.

### 6 — the RFC6-14 fold note goes stale beside the tier row

**Accepted.**

- A second amendment disclosure, for the RFC6-14 fold note, says which of
  its limbs the amendment now covers.
- The secondary-annotation limb gets Unknown amendment rows under RFC6-14
  and RFC2-24.

The signed RFC6-14 row is unchanged.

### 7 — scenarios presume conditions their requirement makes conditional

**Accepted.** Each WHEN now states its condition:

- the ribbon scenario: "a surface renders the three-state view for a
  claim…";
- the identity scenario: "one of those surfaces links to the subject on the
  other".

### 8 — singular role pair against multi-pair rows

**Accepted.** The case and oracle independence now say "the set of role
pairs the table assigns that relation".

### 9 — two citations that did not resolve at the reviewed commit

**Accepted.**

- This record now exists, so the packet's reference resolves.
- The lane-B disposal is now cited to `scripts/check_governance.py` line
  1780, a tracked record, in place of the bead note.

### 10 — the proposal overstated the Part B2 moves

**Accepted.** The proposal now reads "because a requirement now covers one
of their consequences", matching the delta.

### 11 — RFC6-1 line citation imprecise

**Accepted.** The delta now cites the first bullet at lines 112–115 and the
second at lines 116–118 of the RFC-0006 module.
