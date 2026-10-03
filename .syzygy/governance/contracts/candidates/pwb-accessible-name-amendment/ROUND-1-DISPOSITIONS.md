> # Record beside the package — not authority, binds nothing
>
> Dispositions of the first fresh-context review of the PWB accessible-name
> amendment package. This record is not a package artifact: the manifest
> does not hash it and no builder reads it. It offers nothing and performs
> no act (VIS-4).

# Round 1 dispositions — PWB accessible-name amendment

- **Reviewed commit:** `0241fb835471af3a2ea23119959bdfa34ef14464`.
- **Verdict (raw line 4):** `REVISE`. The review has one revise finding (1)
  and six notes (2–7), with no blocking finding.
- **Stopping rule as applied.** The brief
  (`../pwb-opening-index-amendment/REVIEW-BRIEF.md`), written before the
  round, said that a non-clearing verdict leaves the package unedited. After
  the round the coordinator directed otherwise for a first-round `REVISE` on
  a new draft: repair once, record each finding and its repair here, and run
  no round 2. That direction was applied; the brief carries a dated note.
- **Status: round 1 `REVISE`, repaired once, unconfirmed; owner decides.**
  No round 2 is dispatched. The repaired bytes are not offered as cleared
  under Scope A; the owner decides between signing, a confirmation round
  and revision (register row P-99).
- **Figures** [Observed]. Re-derived after the repair by
  `scripts/build_pwb_accessible_name_amendment.py --check`: 11 proposed
  subjects, 2 patched; 17 requirements and 53 scenarios; `--selftest` 20
  structure mutants, each failing on its own predicate.

Reviewed record: docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-1-RAW.md

## Dispositions

### 1 — the obligations bind every Polaris page, but the sweep covers one (revise)

**Repaired.** The population is now "every Polaris page served at one
whole-project evaluation, including the entry page and each exact-source
route response PWB-REQ-011 serves". Each check reports the page count and,
per page, its populations. The Case, Oracle, Falsifier and the second
scenario (renamed "Name and heading checks cover every Polaris page") say
the same. On the verbatim question: headings inside a verbatim Butlers body
rendered under PWB-REQ-011 are counted and reported but are outside the
level-1 and order rules, so PWB-REQ-011 yields nothing. Packet question 6
offers the owner the narrower entry-page-only reading. New mutants: page
count dropped, exact-source pages dropped, verbatim headings ruled.

### 2 — "target" is undefined for buttons and form controls (note)

**Repaired.** A link's target is its resolved `href`; a `summary`'s
controlled region is its `details`; a button's or form control's is the
element its `aria-controls` names, or the control itself when it names
none. The heading population is every heading after load, including those
inside a closed `details`, excluding those under `hidden`,
`aria-hidden="true"` or computed `display: none`.

### 3 — disambiguated names against the visible label and PWB-REQ-012 (note)

**Repaired.** "The accessible name SHALL begin with the visible label, and
the words added to it name the item or source by the identity PWB-REQ-014
renders for it." That makes PWB-REQ-014's existing route for barred words
govern the added words. New mutant: label-in-name dropped.

### 4 — register rows P-98 and P-99 absent at the reviewed commit (note)

**Resolved outside the package.** [Observed] Both rows were added in a later
commit on this branch. No package text changed for this finding.

### 5 — pair-checking and "do not overlap" overstate what was checked (note)

**Repaired.** As finding 6 of the opening-index round: the ledger and
packet now state what was checked (each other pending package, plus all 120
orders of the five pending spec patches applied on 2026-10-03), and name the
P-85/P-86 overlap. (Corrected 2026-10-03 after PR review: first written as 24
orders, a population that omitted P-96, the N9 anchor-resolution
amendment.)

### 6 — a replaced line may lose signed text (note)

**Repaired in the shared engine.** Each `replaced` signed line must survive,
less its full stop, as a proposed line's prefix, with a mutant for it. All
three of this package's replaced lines pass.

### 7 — index rows may collide with same-named links (note)

**Repaired in the opening-index package.** Its rows' accessible names now
name their question. This package's ledger says so.
