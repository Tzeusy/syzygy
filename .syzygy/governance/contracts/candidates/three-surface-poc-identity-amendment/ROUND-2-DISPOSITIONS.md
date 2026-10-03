> # Record beside the package — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the Three-Surface POC
> identity amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 2 dispositions — Three-Surface POC identity amendment

- **Reviewed commit:** `25f4e891f8a9e0f19c2f8d0f4a3444e39c3e603a`.
- **Verdict (raw line 4):** `REVISE`. There are two revise findings (12 and
  13) and six notes (14–19), with no blocking finding.
- **Effect:** every finding below is repaired in the package, and the repair
  retires the round-2 review (rule 10). The Part A figures were re-derived
  by `scripts/build_three_surface_poc_identity_amendment.py --check` over the
  repaired bytes: 132 rows over 78 clauses, 102 covered, 30 Unknown.
- **Stopping rule for round 3, set before it runs:**
  - A notes-only round clears the bytes it read. Its notes are dispositioned
    in a sibling record, and the package is not edited.
  - Any revise finding is repaired once more. If the round after that is
    also not notes-only, no further round is dispatched, and the open
    findings go to the owner with the package.

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-2-RAW.md

## Dispositions

### 12 — POC-REQ-054's decision rule left limbs undecided

**Accepted, limb by limb.**

- **Surface-local handle.** The sentence and its falsifier limb are
  removed from the requirement. No stated procedure classifies a value as a
  handle. The RFC6-1 covered row is narrowed to "equal to the identity its
  owning source authority gives it", which per-element equality with the
  independently derived identity decides. The handle limb is a new Unknown
  amendment row.
- **"Exactly one".** The requirement now speaks of "exactly one link target
  on that surface", carrying the same identity. The oracle counts link
  targets defined more than once. A subject may still render more than once
  on a surface; only the link target must be unique.
- **The reasoned Unknown slot.** The decision rule now counts unfilled slots
  lacking the Unknown label, a reason, a route or the declared Unknown
  encoding, and slot differences between surface and machine answer. The
  falsifier names each limb.
- **RFC6-12.** The covered row is narrowed to "every link between surfaces
  that exists". A new Unknown row covers "every subject rendered on more
  than one surface is openable by its identity on each of them".

### 13 — POC-REQ-055's role-pair check had no declared correspondence, and `contains` fails undisclosed

**Accepted.**

- **The requirement.** It is now per relationship, not per kind. The
  role-pair check reads through a checked-in declaration mapping each
  shared-model entity kind to its RFC 0001 class, or to none, and the oracle
  independence names that declaration.
- **The decision rule.** It now counts all four falsifier limbs:
  - unflagged outside kinds;
  - unflagged unassigned role pairs, reversed roles included;
  - flags on fully admitted relationships;
  - flagged relationships missing their reason.
- **The account of `contains`.** The delta, the owner packet and the
  matrix's disclosure now state that none of the nine relationships emitted
  at drafting complies. Seven fail by kind and `contains` fails by role pair
  (Project→Capability, which its row does not assign).

### 14 — the Inferred scenario asserted a tier the requirement does not require

**Accepted.** The THEN no longer names `asserted-by-worker`. It requires the
label Inferred and the named agent assertion, which the requirement text
carries.

### 15 — "a code region's [identity] by its observed revision"

**Accepted.** It now reads "a code region's source adapter", per RFC 0001's
identity table.

### 16 — Q4's "no production constructor" limb not carried where a signer reads it

**Accepted.**

- The proposed `proposal.md`, the delta and `OWNER-DECISION-PACKET.md`'s
  "What signing does not do" now say that signing does not make the
  Inferred arm constructible in production, and that a constructor needs
  its own act.
- The proposal reconciles the non-goal: no Inferred record, an inferred
  edge included, is produced until that act. The non-goal therefore stands.

### 17 — POC-REQ-060 narrows doctrine's Inferred definition

**Accepted.** The delta has a new paragraph, "A narrowing of doctrine's
Inferred, stated". It quotes `trust-and-evidence.md` lines 84–85 and
115–116, names the two narrowings, and says why the provenance limb is
lighter today and where doctrine's full provenance would be added.

### 18 — the builder overstated its rule-6 coverage, and the RFC6-14 disclosure was unguarded

**Accepted.**

- The docstring now says what the selftest covers: a sample of the required
  phrases, not each one.
- A predicate and a mutant now guard the RFC6-14 disclosure.
- Two predicates that had no mutant gained one each: the ruling-key warrant
  and the Purpose check.

The selftest now runs 22 structure mutants. The two subject-change
predicates in `check()` stay outside the selftest. That is stated, not
claimed.

### 19 — "adds two things" before three bullets

**Accepted.** It now reads "adds three things".
