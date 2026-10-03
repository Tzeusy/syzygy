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
- **Stopping rule, set in `../pwb-opening-index-amendment/REVIEW-BRIEF.md`
  §"Output contract" before the round ran.** A notes-only verdict clears
  the bytes it read. Any other verdict leaves the package unedited: no
  second round is dispatched, and its findings go to the owner.
- **Applied here:**
  - Nothing in the package was edited after the review. Every finding below
    is **open**, with a proposed repair for a later version.
  - No round 2 is dispatched.
- **Status: not cleared.** Scope A offers a package only after a round that
  returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only. This version
  is not offered for sign-off. It goes to the owner as P-99. The drafter
  recommends packet question 1 *Revise*: one new version repairing all seven
  findings, then one fresh round.
- **Figures** [Observed]. Re-derived at the reviewed commit by
  `scripts/build_pwb_accessible_name_amendment.py --check`: 11 proposed
  subjects, 2 patched; 17 requirements and 53 scenarios. The manifest
  file's sha256 is the one on raw line 3, recomputed by
  `git show 0241fb83:<manifest> | sha256sum`.

Reviewed record: docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-1-RAW.md

## Dispositions

### 1 — the obligations bind every Polaris page, but the sweep covers one (revise)

**Accepted, open.** "A Polaris page" quantifies over every page, including
PWB-REQ-011's exact-source route responses, while the Case and Oracle run
over one page and report no page count.

Proposed repair, put to the owner as a new packet question: either name the
page population (the entry page and each exact-source route response at one
evaluation) and report the page count beside each per-page denominator, or
narrow the obligations to the entry page. If verbatim source bodies are in
scope, say whether their own headings are inside the heading-order
population; a Butlers body whose headings skip a level cannot be repaired
by Polaris without breaking PWB-REQ-011's verbatim rendering.

### 2 — "target" is undefined for buttons and form controls (note)

**Open.** Proposed repair: define a target for each class (a link's
resolved `href`, a `summary`'s `details`, a control's `aria-controls`), or
drop the classes Polaris does not render. State whether headings inside a
closed `details` or under `hidden` count.

### 3 — disambiguated names against the visible label and PWB-REQ-012 (note)

**Open.** Proposed repair: require the accessible name to begin with the
visible label (label-in-name), and say that the added item or source
identity is not an owner-visible string under PWB-REQ-012, or route it the
way PWB-REQ-014 routes a barred word.

### 4 — register rows P-98 and P-99 absent at the reviewed commit (note)

**Open in the package; the rows land in this change.** [Observed] The rows
were added after the review, in a later commit on the same branch. The
package is not edited.

### 5 — pair-checking and "do not overlap" overstate what was checked (note)

**Accepted, open.** As finding 6 of the opening-index round: the builder
checks three of the six pairs, and P-85 and P-86 overlap outside the spec.
The reviewer's run of all 24 orders confirms the spec composition.

### 6 — a replaced line may lose signed text (note)

**Accepted, open.** The reviewer confirmed by hand that all three replaced
lines survive as prefixes in this version. The shared-engine repair is the
one proposed for finding 7 of the opening-index round.

### 7 — index rows may collide with same-named links (note)

**Open.** The same repair as finding 8 of the opening-index round.
