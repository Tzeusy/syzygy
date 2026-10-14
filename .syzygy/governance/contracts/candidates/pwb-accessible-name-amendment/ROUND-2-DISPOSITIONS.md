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
    *(Marked 2026-10-14, later the same day: no longer true. On the owner's
    further direction that day, relayed by the lead session, every round-2
    finding, notes included, was repaired once; see "Repairs, 2026-10-14
    (cycle 2)" below.)*
  - **No round 3 is dispatched.** *(Marked 2026-10-14, later the same day:
    the same direction orders one fresh round 3 under the same stopping
    rule, briefed in `../pwb-opening-index-amendment/REVIEW-BRIEF.md`
    §"Round 3" and not yet run.)*
  - **The bytes are not cleared.** This version is not offered for sign-off.
    It goes to the owner as register row P-99, with the seven findings below
    open. This record recommends nothing on Questions 1–6.
    *(Marked 2026-10-14, later the same day: the findings below are
    repaired once, unconfirmed pending round 3, and the packet now carries
    Questions 7 and 8, which the repair added; the bytes are still not
    cleared. The dispositions below are left as written.)*

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

## Repairs, 2026-10-14 (cycle 2)

**Direction.** The owner, in the lead session on 2026-10-14, directed one
more cycle for this packet: repair every round-2 finding, notes included,
once; then one fresh review under the same stopping rule; and where a
repair needs the owner's content choice, put it as a question with a
recommendation [Observed: as the lead session relayed it to the repairing
session; no decisions file records it at `814fbcc1`]. The repairing
session signs, records and dispatches nothing. The repaired bytes are
**round-2 findings repaired once on 2026-10-14, unconfirmed pending round
3** (`../pwb-opening-index-amendment/REVIEW-BRIEF.md` §"Round 3").

**Base.** `origin/main` at `814fbcc1594cea812289bf7bc246bd9d9a38ef56`,
after the anchor-resolution sign-off (P-96) moved PWB `spec.md`. The spec
patch was rebuilt over the current `spec.md` and the dependency patch and
manifest regenerated with `--write`. Line numbers below are of
`proposed/spec.md.patch` as repaired. Code facts are [Observed] at
`814fbcc1`.

| # | Level | Repair (where) |
|---|---|---|
| 1 | revise | **Scoped, made checkable, and the identity half narrowed, with an owner question.** Patch lines 17–24: an element's visible label is "its text content with each whitespace run collapsed to one space and the ends trimmed". Where elements with different targets share one visible label on a page, each of their accessible names SHALL begin with that label. Where such an element's target is an exact-source route response, the words after the label SHALL include "the repository-relative path the machine answer carries for the source that route serves (PWB-REQ-011's machine recovery)". "These two rules bind no other element." The undefined "identity PWB-REQ-014 renders" is gone, and so is the round-1 sentence "told apart … by the item or source it belongs to", whose "belongs to" no oracle could resolve. The Oracle now groups by visible label and compares name prefixes and paths (line 70). Oracle independence takes the expected path from the machine answer (line 79). The Falsifier adds the failing element (line 85). The first new scenario now asserts the prefix and the path (line 100), and the second fails a shared-label name that does not begin with its label (line 112). All pinned, with mutants, including the raw's "free text" probe. Package A's rows fall under this only where another element with a different target shares a row's words. **Packet Question 7** asks whether to keep the narrowed identity half, drop it, or widen it |
| 2 | note | Patch lines 42–45: "The pages are the entry page and one exact-source route response for each source the machine answer at that evaluation lists, whether that response serves the source's body or refuses it. The list comes from the machine answer, never from the links the renderer emits." The Oracle's page count now equals "the number of pages listed from the machine answer", and the second scenario says so. Pinned, with a mutant |
| 3 | note | Patch lines 13–16 define the interactive population as the heading population is defined: every link with an `href`, button, `summary` and form control in the document after load, including those inside a closed `details`, excluding those hidden by `hidden`, `aria-hidden="true"` or `display: none`. The DOM is the population, not the accessibility tree that today's checker reads (`polaris-accessibility.ts` line 525), so a link in a closed disclosure is counted. The Oracle's per-page denominator is now "the population this requirement defines". Pinned, with a mutant |
| 4 | note | **Exemption dropped, with an owner question.** The verbatim-heading exemption is removed. Patch lines 34–35 say no heading is exempt, "including one Polaris renders from Butlers-declared text". The Falsifier's and scenario's "outside a verbatim body" went with it. The heading population now names `h1` to `h6` and `role="heading"` at its `aria-level` (line 29). The delta's reason is replaced by the code facts. The exact-source route renders each body as escaped text in a `<pre>` (`polaris-source.ts` line 123). Butlers-declared Markdown on the entry page is re-based by `polaris-markdown.ts` line 179, so Polaris already chooses those levels. **Packet Question 8** asks whether any exemption should return |
| 5 | note | The ledger's fixture line, the builder docstring and register row P-99 now say "every Polaris page served at one whole-project evaluation". The round-state sentences are marked at the sentence, dated, in the packet, the delta, this record and P-99. The packet's "Butlers' own headings are left as written" bullet is marked at the sentence |
| 6 | note | The heading exclusions and the identity half are pinned as whole sentences, each with a mutant (the raw's two probes: exclusions inverted, added words made free text). The engine's prefix check is unchanged, since the engine is shared with P-85 and P-86, which are being repaired concurrently. This builder now adds a positional check: the line after each replaced line's signed predecessor must open with that line's signed stem. Its mutant inserts a line between them |
| 7 | note | Re-checked over the current tree: this builder's `--check` composes every pending sibling live and passes at the repair commit. The repaired P-85 and P-86 patches still need composing at sign-off time. Their own builders' `--check` fails at `814fbcc1` on a stale dependency patch, as this one did before `--write`. That is theirs to regenerate, and this repair does not touch their packages |

**Figures** [Observed, at the repair commit]. `--check`: 11 proposed
subjects (2 patched), 17 requirements, 54 scenarios. `--selftest`: 27
structure mutants (5 engine, 22 builder), each failing on its own
predicate.

**Not changed.** The distinct-name rule, the target definitions, the
heading rule, the page scope and the three `replaced` lines are unchanged.
Questions 1–6 stand as written, except for the dated marks.
