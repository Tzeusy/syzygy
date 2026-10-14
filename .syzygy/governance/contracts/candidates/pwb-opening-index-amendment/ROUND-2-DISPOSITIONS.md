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
    *(Marked 2026-10-14, later the same day: no longer true. On the owner's
    further direction that day, relayed by the lead session, every round-2
    finding, notes included, was repaired once; see "Repairs, 2026-10-14
    (cycle 2)" below.)*
  - **No round 3 is dispatched.** *(Marked 2026-10-14, later the same day:
    the same direction orders one fresh round 3 under the same stopping
    rule, briefed in `REVIEW-BRIEF.md` §"Round 3" and not yet run.)*
  - **The bytes are not cleared.** This version is not offered for sign-off.
    It goes to the owner as register row P-98, with the nine findings below
    open. This record recommends nothing on Questions 1–7.
    *(Marked 2026-10-14, later the same day: the findings below are
    repaired once, unconfirmed pending round 3, and the packet now carries
    Questions 8 and 9, which the repair added; the bytes are still not
    cleared. The dispositions below are left as written.)*
    *(Marked 2026-10-14, round 3: "not yet run" and "unconfirmed pending
    round 3" are no longer true. Round 3 returned `REVISE`; see
    `ROUND-3-DISPOSITIONS.md`.)*

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

## Repairs, 2026-10-14 (cycle 2)

**Direction.** The owner, in the lead session on 2026-10-14, directed one
more cycle for this packet: repair every round-2 finding, notes included,
once; then one fresh review under the same stopping rule; and where a
repair needs the owner's content choice, put it as a question with a
recommendation [Observed: as the lead session relayed it to the repairing
session; no decisions file records it at `814fbcc1`]. The repairing
session signs, records and dispatches nothing. The repaired bytes are
**round-2 findings repaired once on 2026-10-14, unconfirmed pending round
3** (`REVIEW-BRIEF.md` §"Round 3"). *(Marked 2026-10-14, round 3: round 3
has run and returned `REVISE`; the repaired bytes stay unconfirmed. See
`ROUND-3-DISPOSITIONS.md`.)*

**Base.** `origin/main` at `814fbcc1594cea812289bf7bc246bd9d9a38ef56`,
after the anchor-resolution sign-off (P-96) moved PWB `spec.md`. That move
left this builder's `--check` failing on a stale dependency patch, so the
spec patch was rebuilt over the current `spec.md` and the dependency patch
and manifest regenerated with `--write`. Line numbers below are of
`proposed/spec.md.patch` as repaired.

| # | Level | Repair (where) |
|---|---|---|
| 1 | revise | The first scenario's AND now reads "exactly one stopping line stands immediately after the first element of the target whose offset is largest, giving that offset and the page's word total" (patch lines 123–125), in the requirement's own terms. The phrase is pinned, with a mutant that moves it back to "follows the last indexed target" |
| 2 | revise | **Dropped, with an owner question.** The sentence "A row's accessible name names its question…" is removed, so "its question" is gone. In its place, "Each row is named by its project concept" becomes "Each row shows its declared row name" (line 23), which the table fixes and a check can read: the Oracle compares "each row's name and target" with the table (line 86), the Falsifier adds a row that "shows a name other than its declared row name" (line 102), and the first scenario's THEN says "each showing its declared row name". Distinctness from other links is left to P-99, which binds the rows like any other link if it is signed. Each new phrase is pinned with a mutant. **Packet Question 8** asks whether to keep this or declare per-row accessible names instead |
| 3 | note | The offset is now "the number of counted words that precede the target's first element in document order" (lines 35–37), defined for every rendered target, including one with no counted word. "Each row whose target is rendered SHALL show" the offset, and "A row whose target is not rendered shows no offset" (line 38); the Falsifier and the second scenario say the same. A new sub-bullet (lines 42–47) settles a tie on the largest offset, a largest-offset target inside a closed `details` (the line stands after the outermost closed `details`) and an evaluation where no target renders |
| 4 | note | The count is taken "at the one viewport width and height the oracle declares and publishes with its result" (line 50). The visibility exclusion is now per text node: "any text node whose parent element's computed `visibility` is not `visible`" (line 57), so a visible descendant of a `visibility: hidden` element counts. `display: none` stays an ancestor exclusion. Both pinned, with mutants |
| 5 | note | **Kept as drafted, with an owner question.** The term and placement are unchanged in the bytes. The packet's "one line after the last target" now says where the line stands and what it does not say, and the delta's "why" section says the line marks where the last declared target begins, not where its material ends. **Packet Question 9** puts the name and placement to the owner |
| 6 | note | `IMPACT-LEDGER.md` now plans "a word counter over the document as the browser holds it after load", not over the served HTML. The round-state sentences are marked at the sentence, dated, in the packet, the delta, this record and register row P-98 |
| 7 | note | Oracle independence now names what the recognizer's selectors may key on: "visible heading text, … claim identities the machine answer serves and … the PWB-REQ-011 exact-source route form, never on an attribute, class or identifier the renderer emits to mark an index target" (lines 93–97). Pinned, with a mutant |
| 8 | note | Both scenario phrases the raw probed are pinned: the stopping-line placement (finding 1) and "each of the other eight rows still routes to its declared target and shows that target's word offset" (lines 133–134). The old "keep their … offsets" also went, because removing the aggregate changes the other rows' offsets. The engine's prefix check is unchanged, since the engine is shared with P-85 and P-86, which are being repaired concurrently. This builder now adds a positional check: the line that follows each replaced line's signed predecessor must open with that line's signed stem. Its mutant inserts a line between them |
| 9 | note | Re-checked over the current tree: this builder's `--check` composes every pending sibling live and passes at the repair commit. The repaired P-85 and P-86 patches still need composing at sign-off time. Their own builders' `--check` fails at `814fbcc1` on a stale dependency patch, as this one did before `--write`; that is theirs to regenerate, and this repair does not touch their packages |

**Figures** [Observed, at the repair commit]. `--check`: 11 proposed
subjects (2 patched), 17 requirements, 54 scenarios. The 54 includes the
anchor-resolution scenario P-96 added. `--selftest`: 33 structure mutants
(5 engine, 28 builder), each failing on its own predicate.

**Not changed.** The table's nine rows and targets, the copy roles, the
verdict exclusion and the five `replaced` lines are unchanged. Questions
1–7 stand as written, except for the dated marks.
