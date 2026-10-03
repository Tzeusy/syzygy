> # Record beside the package — not authority, binds nothing
>
> Dispositions of the third fresh-context review of the Three-Surface POC
> identity amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 3 dispositions — Three-Surface POC identity amendment

- **Reviewed commit:** `38c1c5c9be35419425a7177535c163894f51f1d4`.
- **Verdict (raw line 4):** `REVISE`. There is one revise finding (20) and
  five notes (21–25), with no blocking finding.
- **Effect:** every finding below is repaired in the package, and the repair
  retires the round-3 review (rule 10). The Part A figures were re-derived
  by `scripts/build_three_surface_poc_identity_amendment.py --check` over the
  repaired bytes: 134 rows over 78 clauses, 102 covered, 32 Unknown.
- **Stopping rule, as set in `ROUND-2-DISPOSITIONS.md` before round 3 ran:**
  this is the "repaired once more" step. If round 4 is not notes-only, no
  further round is dispatched, and its open findings go to the owner with
  the package.

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-3-RAW.md

## Dispositions

### 20 — the RFC1-26 disclosure row over-claimed through an unchecked correspondence

**Accepted, by the reviewer's second repair.**

- The RFC1-26 disclosure row now reads "by kind or by role pair as read
  through the declared kind-to-class correspondence".
- A new Unknown amendment row under RFC1-25 reads "The declared
  kind-to-class correspondence matches RFC 0001's class definitions".
- The matrix's RFC1-26 amendment disclosure says that limb has its own
  Unknown row.
- The delta drops the token-table analogy. It now says the declaration makes
  a truth claim that no procedure decides, written by the same slice that
  emits the relationships, and it names the `project`→Capability example.
- The packet's POC-REQ-055 paragraph says the mapping's truth stays Unknown.

The correspondence was not written into the requirement as literals. Doing
so would sign a mapping of today's POC kinds that slice 8 may change, and
the owner can still ask for it by answering "Revise".

### 21 — semantic class, rule and re-typing undisclosed; "fully admits" wider than the rule

**Accepted.** A new Unknown amendment row under RFC1-26 reads "A closed-name
relationship honours its row's semantic class and rule, and no relation is
re-typed". POC-REQ-055's falsifier now reads "a flag on a relationship whose
kind and mapped role pair the table assigns", the decision rule's own words.

### 22 — the builder did not guard signed prose outside the rows

**Accepted.**

- `companion_findings` now fails when any signed line of `proposal.md` is
  edited or removed. It also fails when any signed matrix line outside the
  clause and family rows is edited or removed, except the five computed
  lines named in `COMPUTED_LINES`.
- The reviewer's two mutations are now selftest mutants: "matrix banner
  edited" and "proposal heading renamed". The selftest runs 24 structure
  mutants.
- The docstring now describes POC-REQ-055 per relationship and role pair,
  and states the scope of the new guard.

### 23 — lane B's disposal cited to a code comment

**Accepted.** The delta now cites
`.syzygy/governance/decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`
line 36.

### 24 — POC-REQ-054's attribution, authority-less subjects, and "a score, a verdict"

**Accepted.**

- The oracle independence now says the checker attributes each element to
  its subject by the source record the element renders, never by the
  identity the element carries.
- A subject that no source authority owns has no independently derived
  identity. The identity-equality limb makes no claim for it, and its link
  targets and slots are still checked.
- The decision rule and falsifier now count an unfilled slot carrying a
  score or a verdict.

### 25 — POC-REQ-060's decision rule reached shape limbs only through "off-vocabulary"

**Accepted.** The decision rule now reads "zero records off the
closed-vocabulary shape (label, tier nesting, exactly one primary reason with
its route)".
