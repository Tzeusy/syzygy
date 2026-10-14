> # Record beside the package — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the PWB accessible-name
> amendment package (P-99). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 2 dispositions — PWB accessible-name amendment

- **Reviewed commit (raw line 2):**
  `ae8c074066d8e6c511d8064b505e3f89e3f2b43d`.
- **Manifest file digest (raw line 3):**
  `0509c31999aa65cee90bc2814120693f907fd530329837c0d6d8638641788d51`.
  [Observed 2026-10-14] Unchanged on the integration branch, where the
  builder's `--check` passes with the repaired P-85 and P-86 patches landed
  (the sibling-order residual of the raw's finding 7 holds at that commit).
- **Verdict (raw line 4):** `REVISE`. One revise finding (1) and six notes
  (2–7), with no blocking finding, counted from the raw's seven
  `**Finding N — …** (<class>)` headings. Findings 6 and 7 apply to this
  package and the opening-index package (P-98).
- **Why round 2 ran.** The shared brief
  (`../pwb-opening-index-amendment/REVIEW-BRIEF.md`) said one round only,
  and round 1's dispositions said no round 2. The owner's direction of
  2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`)
  ordered one fresh confirmation round per packet before the owner is asked
  the content questions. The raw is that round; the brief is not edited.
- **Stopping rule applied.** One repair and one review per packet; a packet
  still `REVISE` goes to the owner with its findings, not into another
  loop. Round 1's findings were repaired once and round 2 is the one
  review. So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the "no round 2" sentences finding 5 names
    (packet, delta and `ROUND-1-DISPOSITIONS.md`), the old text kept.
  - **No round 3 is dispatched.**
  - **The bytes are not cleared.** This version is not offered for sign-off.
    It goes to the owner as register row P-99, with the seven findings below
    open. This record recommends nothing on Questions 1–6.

Reviewed record: docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-2-RAW.md

## Dispositions

### 1 — the label-in-name and identity rule added in repair has no oracle limb, no falsifier limb and no scenario that carries it (revise)

**Open.** Raw line 80. Distinct names that do not begin with the visible
label pass every verification limb; the identity half is unpinned; the
sentence's scope is unclear where it meets P-98's rows. The raw's repair:
add oracle, falsifier and scenario limbs for the label prefix and the
identity source, scope the sentence, and pin it.

### 2 — "every Polaris page served" has no stated enumeration (note)

**Open.** Raw line 111. Naming the enumeration source, outside the
renderer, would close round-1 finding 1 fully.

### 3 — the interactive population is not defined the way the heading population now is (note)

**Open.** Raw line 125.

### 4 — the verbatim-heading exemption covers no heading today, and its stated reason does not match how Polaris renders Butlers headings (note)

**Open.** Raw line 138.

### 5 — several sentences went stale in the repair (note)

**Open for the scope half; dispositioned for the round-state half.** Raw
line 173. The ledger's fixture sentence, the builder docstring and register
row P-99's "a whole-project page" still describe the pre-repair one-page
scope: open (the register row's scope words are left as the drafter wrote
them, since changing them is the repair). The "no round 2 was dispatched"
sentences in the delta, the packet and P-99 are marked or updated, dated.

### 6 — pinning: the heading-population exclusions and the added-word identity are unpinned; the engine's prefix check accepts any line (note, both packages)

**Open.** Raw line 186.

### 7 — sibling order was checked against `main` only; the repaired P-85 and P-86 remain for sign-off time (note, both packages)

**Observed held at the integration commit; open for sign-off time.** Raw
line 197. With the repaired P-85 and P-86 patches landed, this builder's
`--check` composes them live and passes. A later change to any sibling
patch needs the check again.
