> # Record beside the package — not authority, binds nothing
>
> Dispositions of the third fresh-context review of the PWB opening-index
> amendment package (PWB-REQ-010, P-98, slice A). This record is not a
> package artifact: the manifest does not hash it and no builder reads it.
> It classifies each round-3 finding and repairs nothing: every finding is
> open for the owner. It offers nothing and performs no act (VIS-4).

# Round 3 dispositions — PWB opening-index amendment

Reviewed record: docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-3-RAW.md

- **Reviewed commit (raw line 2):**
  `d6b3784f5b7f09b27ffb41f57785282b7393c4d1`.
- **Manifest file digest (raw line 3):**
  `b091f9dcd646bbe25f3eaa2b8086463595ad76c8f328c4935ec8efcf5c2662e2`.
  [Observed 2026-10-14] It re-derives from the manifest file's bytes at
  the reviewed commit, and the file is unchanged on the integration
  branch.
- **Verdict (raw line 4):** `REVISE`. One revise finding (1) and nine
  notes (2–10), no blocking finding. The raw has no closing count; its
  line 119 says "The one revise finding is against criterion 3", and the
  ten were counted by script from its finding headings. Findings 9 and 10
  apply to this package and to the accessible-name package (P-99), whose
  own round 3 cleared (`../pwb-accessible-name-amendment/ROUND-3-DISPOSITIONS.md`).
- **Why the round ran.** The owner's direction of 2026-10-14 for a second
  cycle, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
  repair every finding, notes included, then one fresh review under the
  same stopping rule. The brief's §"Round 3" set that rule before the
  round.
- **Stopping rule applied.** A verdict still `REVISE` goes to the owner
  with its findings. So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the "unconfirmed pending round 3" sentences
    in the packet, the delta and `ROUND-2-DISPOSITIONS.md`, with the old
    text kept. `REVIEW-BRIEF.md` is not edited: it is shared with P-99,
    whose cleared round read it.
  - **No round 4 is dispatched** without a new owner direction.
  - **The bytes are not cleared** and this version is not offered for
    sign-off. This record recommends nothing on Q1–Q9.

## Composition at the integration branch

[Observed 2026-10-14] On the integration branch over `origin/main`
`8acb0795`, after P-85's regeneration landed, all four pending PWB
builders' `--check` pass, this one included. That is the re-run finding 10
asks for, at that commit only.

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The closed-`details` override's scope is ambiguous ("that element" after the tie sentence), and on the general reading the dispositions intend, the first scenario's AND contradicts it for a largest-offset target inside a closed disclosure. Today's claim-strength legend is itself a closed `details` (`polaris.ts:408`) | 123 | **Open for the owner.** Raw's repair: name "the target that sets the line", then qualify the scenario's AND or narrow its WHEN to a target outside any closed disclosure. |
| 2 | note | The no-target, tie and unrendered-row rules, and "the index first", lack a scenario or a falsifier limb | 173 | **Open.** Add the missing limbs; the no-target case is the nearest to a missing limb. |
| 3 | note | The packet and delta say the stopping line's text is "the two numbers only" and its name is never shown; the bytes forbid less, and Q9's recommended reason rests on the stronger property | 195 | **Open.** Add a clause ("its visible text is the two numbers and their unit") or soften the packet and delta. |
| 4 | note | The recognizer's permitted keys are named, but the expected heading text is anchored nowhere outside the renderer; the claim-identity key reads renderer attributes | 217 | **Open.** Anchor the expected strings (round 2 suggested RFC7-13's category names) and say the independence is partial. |
| 5 | note | An oracle-declared viewport makes the value the renderer must show depend on the oracle's choice | 233 | **Open.** Fix the viewport in the requirement, or say in the ledger that offsets are computed in the page after load. |
| 6 | note | "Immediately after the first element" of an inline target places the line mid-flow, invalid inside a `ul` or `tr` | 255 | **Open.** A presentation question Q9 does not mention. |
| 7 | note | "Shows its declared row name" leaves separation, exactness and case open | 265 | **Open.** One phrase, for example "the row's text begins with its declared row name, exactly". |
| 8 | note | `SEMANTIC-DELTA.md:133` names packet question 4 for slice B; slice B is question 6 (present since `ae8c0740`) | 278 | **Open.** Trivial cross-reference fix. |
| 9 | note | Two survivors change meaning ("project claims"; "any method"); `position_findings` raises a traceback instead of a finding and is duplicated in two builders (both packages) | 287 | **Open.** Pin the two phrases; return a finding; move the function into the engine at its next edit. |
| 10 | note | Composition with the release-label lane verified only for its spec patch at the reviewed commit (both packages) | 311 | **Open, with the re-run recorded above.** Re-run this builder's `--check` whenever a sibling patch changes. |

**Stale sentences outside the marked files.** `REVIEW-BRIEF.md` §"Round 3"
describes a round still to run; it is not edited, as above. Register row
P-98 and `docs/README.md`'s opening-index and accessible-name row sit
outside the package and are updated directly.
