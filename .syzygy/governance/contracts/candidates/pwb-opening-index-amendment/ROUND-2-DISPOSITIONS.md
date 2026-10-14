> # Record beside the package — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the PWB opening-index
> amendment package (P-98). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 2 dispositions — PWB opening-index amendment

- **Reviewed commit (raw line 2):**
  `ae8c074066d8e6c511d8064b505e3f89e3f2b43d`.
- **Manifest file digest (raw line 3):**
  `4cee1b0c8120448bdda6bba1047d7ad06f51b1a7a18fec12c0cb4cd07475e518`.
  [Observed 2026-10-14] Unchanged on the integration branch, where the
  builder's `--check` passes with the repaired P-85 and P-86 patches landed
  (the sibling-order residual of the raw's finding 9 holds at that commit).
- **Verdict (raw line 4):** `REVISE`. Two revise findings (1, 2) and seven
  notes (3–9), with no blocking finding, counted from the raw's nine
  `**Finding N — …** (<class>)` headings. Findings 8 and 9 apply to this
  package and the accessible-name package (P-99).
- **Why round 2 ran.** The brief's stopping rule said one round only, and
  round 1's dispositions said no round 2. The owner's direction of
  2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`)
  ordered one fresh confirmation round per packet before the owner is asked
  the content questions. The raw is that round; the shared brief is not
  edited.
- **Stopping rule applied.** One repair and one review per packet; a packet
  still `REVISE` goes to the owner with its findings, not into another
  loop. Round 1's findings were repaired once and round 2 is the one
  review. So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the "no round 2" sentences finding 6 names
    (packet, delta and `ROUND-1-DISPOSITIONS.md`), the old text kept.
  - **No round 3 is dispatched.**
  - **The bytes are not cleared.** This version is not offered for sign-off.
    It goes to the owner as register row P-98, with the nine findings below
    open. This record recommends nothing on Questions 1–7.

Reviewed record: docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-2-RAW.md

## Dispositions

### 1 — the new scenario still places the stopping line "after the last indexed target", contradicting the repaired requirement (revise)

**Open.** Raw line 92. The requirement says "immediately after the first
element of the target whose offset is largest"; the scenario was not
repaired and its wording is unpinned. The raw's repair: restate the
scenario in the requirement's terms, and pin the phrase.

### 2 — the row accessible-name sentence added in repair has no oracle limb, no falsifier limb and no scenario (revise)

**Open.** Raw line 115. "Its question" is also undefined, and the "so it
shares no name" consequence holds only if P-99 is signed too. The raw's
repair: declare each row's name or a rule deriving it, with oracle,
falsifier and scenario limbs, or drop the sentence and leave distinctness
to P-99.

### 3 — an offset is undefined when the target has no counted word; "each row SHALL show" has no exception for an unrendered row (note)

**Open.** Raw line 142.

### 4 — the computed-style exclusions depend on a browser state the method does not fix (note)

**Open.** Raw line 156. Latent today: the `@media` blocks hide nothing.

### 5 — the stopping line sits at the start of the last target's material, and its name invites a reader to stop there (note)

**Open.** Raw line 170. The raw says the owner may want this named.

### 6 — two sentences went stale in the repair (note)

**Open for the ledger half; dispositioned for the round-state half.** Raw
line 184. `IMPACT-LEDGER.md` lines 43–44 still plan a counter over the
served HTML: open. The "no round 2 was dispatched" sentences in the delta,
the packet and register row P-98 are marked or updated, dated.

### 7 — the recognizer is "published with the oracle", but nothing says it is independent of the renderer's markup (note)

**Open.** Raw line 197.

### 8 — pinning: the scenario phrases most at risk are unpinned; the engine's prefix check accepts any line (note, both packages)

**Open.** Raw line 208. The current bytes pass on the correct lines; a later
`--write` could pass on the wrong one.

### 9 — sibling order was checked against `main` only; the repaired P-85 and P-86 remain for sign-off time (note, both packages)

**Observed held at the integration commit; open for sign-off time.** Raw
line 220. With the repaired P-85 and P-86 patches landed, this builder's
`--check` composes them live and passes. A later change to any sibling
patch needs the check again.
