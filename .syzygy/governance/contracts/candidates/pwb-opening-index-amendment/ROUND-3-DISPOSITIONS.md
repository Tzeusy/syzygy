> # Record beside the package — not authority, binds nothing
>
> Dispositions of the third fresh-context review of the PWB opening-index
> amendment package (PWB-REQ-010, P-98, slice A). This record is not a
> package artifact: the manifest does not hash it and no builder reads it.
> It classifies each round-3 finding and repairs nothing: every finding is
> open for the owner. It offers nothing and performs no act (VIS-4).
> *(Marked 2026-10-14, cycle 3: "repairs nothing" and "every finding is
> open" are no longer true. On the owner's direction that day, every
> finding was repaired once; see §"Repairs, 2026-10-14 (cycle 3)" below.
> The classification table is left as written.)*

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
  *(Marked 2026-10-14, cycle 3: the first two bullets are no longer true.
  The owner directed "One more cycle each" for P-85 and P-98 in the lead
  session that day: every round-3 finding repaired once, then one fresh
  round 4 under the same stopping rule, briefed in `REVIEW-BRIEF.md`
  §"Round 4" and not yet run. The bytes are still not cleared.)*

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
*(Marked 2026-10-14, cycle 3: `REVIEW-BRIEF.md` is now edited, by adding
a §"Round 4" after §"Round 3". The text above it, which rounds 1–3 read,
is left unchanged. The P-99 clearance it protected no longer binds,
because P-99 was regenerated over P-86 and awaits its own round 4.)*

## Repairs, 2026-10-14 (cycle 3)

**Direction.** The owner, in the lead session on 2026-10-14, directed "One
more cycle each" for P-85 and P-98: repair every round-3 finding, notes
included, once; then one fresh review under the same stopping rule; and
where a repair needs the owner's content choice, put it as a question with
a recommendation [Observed: as the lead session relayed it to the
repairing session; no decisions file records it at `7460aec8`]. The
repairing session signs, records and dispatches nothing. The repaired
bytes are **round-3 findings repaired once on 2026-10-14, unconfirmed
pending round 4** (`REVIEW-BRIEF.md` §"Round 4").

**Base.** `origin/main` at `7460aec80196e40cc2889eb46f8bdce8bcb77614`,
after the class-granular sign-off (P-86) moved PWB `spec.md`. That move
left this builder's `--check` failing on a stale dependency patch. The spec
patch was rebuilt over the current `spec.md` (the signed lines it carries
are unchanged), and the dependency patch and manifest regenerated with
`--write`. Line numbers below are of `proposed/spec.md.patch` as repaired.

| # | Level | Repair (where) |
|---|---|---|
| 1 | revise | The placement rule now names its subject. "Exactly one stopping line SHALL stand at the place the next item fixes" (line 41). The next item defines "the target that sets the line": the rendered target with the largest offset, the later in document order on a tie (line 45). The line then stands "immediately after the outermost element that contains the first element of the target that sets the line, that first element itself included", where that element is a closed `details` or one of the elements in finding 6 (lines 47–53). So the closed-`details` rule applies in every case, not only on a tie. The first scenario's AND now carries both places: "immediately after that target's first element, or after the outermost closed `details`, `p`, heading, `ul`, `ol`, `dl` or `table` element containing it" (lines 144–149). A new scenario, "A last-beginning target inside a closed disclosure moves the line after it" (line 168), covers the case the raw observed in today's legend. The phrases are pinned. Two mutants are killed: one keys the rule back to "that element", one lets the scenario's line stay inside the disclosure. The rule's place for a closed disclosure is also put to the owner (Question 11) |
| 2 | note | Each rule the raw named now has its limbs. **No target rendered:** a Case limb, the Oracle's "or, where no indexed target renders, only the recomputed total" (line 105), the Falsifier's "where no indexed target renders, the stopping line gives anything but the word total" (line 126), and a scenario (line 178). **Tie:** a Case limb and a scenario (line 160). **Unrendered row "SHALL say so":** the Falsifier now reads "an unrendered target's row does not say that its target is not rendered, routes anywhere or shows an offset" (line 122). **Index first:** an Observable limb, "the first reading level begins with the index" (line 94), and a Falsifier limb, "the index is present but does not begin the first reading level" (line 119). Each is pinned, with a mutant for each falsifier limb and for the tie scenario |
| 3 | note | **Bytes made to match the packet.** "The stopping line's visible text is its numbers and their unit, and nothing else" and "'Stopping line' is this specification's name for it and is never shown on the page" (lines 55–57), plus the Falsifier limb "the stopping line shows any text beyond its numbers and their unit" (line 127). Question 9's reason now rests on a pinned clause. A dated mark under Question 9 says so. Both sentences are pinned, with mutants |
| 4 | note | **Partly repaired; the rest disclosed, with an owner question.** The recognizer's selectors "and every heading string they match" are now "published with the oracle before it runs" (line 110), so a run cannot fit its strings to the page it sees. The raw's suggested anchor does not exist. [Observed] RFC7-13 names altitudes, not these targets' headings (`narrative-contract.md:306-317`). So the delta now says the independence is partial: heading strings share the renderer's vocabulary, and claim identities are read through attributes the renderer emits for every claim. **Packet Question 12** offers tying each heading to its row name instead. Pinned, with a mutant |
| 5 | note | **Viewport fixed to the page's own, with an owner question.** Words are counted "at the viewport width and height the page has when it loads", and "The offsets and total a page shows SHALL be those of that viewport; an oracle declares the viewport it ran at and publishes it with its result" (lines 60–63). The renderer's numbers are now defined independently of any oracle's choice. `IMPACT-LEDGER.md` now says the renderer's counter runs in the page after load, and that an oracle enumerates the document after its scripts run. **Packet Question 10** offers one fixed size instead. Both sentences pinned, with mutants |
| 6 | note | **Drafted, with an owner question.** The placement rule in finding 1 also steps out of a `p`, heading (`h1` to `h6`), `ul`, `ol`, `dl` or `table` containing the target's first element (lines 47–53). A line after the `exact-requirement` link therefore never stands mid-sentence or inside a list or table. **Packet Question 11** puts this, and stepping out of closed disclosures only, to the owner |
| 7 | note | "Each row's visible text begins with its declared row name, exactly as the table spells it, character for character and in the same case, and the row's offset, or its statement that its target is not rendered, follows the name" (lines 23–26). The Falsifier now reads "its text does not begin with its declared row name exactly" (line 120), and the first scenario "each beginning with its declared row name". Pinned, with two mutants (match loosened; falsifier dropped) |
| 8 | note | `SEMANTIC-DELTA.md` now names packet question 6 for slice B, with a dated note that it said 4 |
| 9 | note | **Pinning.** All six of the raw's surviving probes are now pinned and killed by a mutant each: "are presentation measurements" → "are project claims"; "one declared method" → "any method"; the Case's absent-aggregate evaluation dropped; the Observable's index limb dropped; the first scenario's WHEN widened; and the capture sentence replaced by "estimated". **Positional check.** `position_findings` now returns a named finding on every path: a replaced line not once in the signed block, a predecessor absent, a predecessor repeated, and a predecessor with no line after it. No path raises. `--selftest` runs four fixtures over synthetic signed blocks for the paths a proposed-spec mutant cannot reach, and each fails closed with its own message. [Observed] Replacing `copies == 0` with `copies == -1` in a scratch copy of the builder makes `--selftest` exit non-zero. **Not moved into the engine.** The engine is not edited in this cycle, because the accessible-name builder (P-99) carries the same function and its cleared bytes are only being regenerated, not repaired. The duplicate in that builder keeps its traceback path, and the engine's next edit should absorb both |
| 10 | note | Re-run on this branch over `7460aec8`: this builder's `--check` composes the two still-pending spec patches, P-99 and P-85, live, pairwise and in every order, and passes. The accessible-name builder's `--check` passes. [Observed] The release-label builder's `--check` fails on its own `CAPABILITY-COVERAGE.md.patch` after the P-86 sign-off. That is the concurrent P-85 lane's to regenerate, and this repair does not touch its package. Its spec patch still composes here |

**Owner questions added.** Question 10 (which viewport the numbers
describe), Question 11 (where the line goes when the last target starts
mid-text or inside a closed disclosure) and Question 12 (disclose the
recognizer's partial independence, or tie each heading to its row name).
Each recommends the version drafted.

**Figures** [Observed, at the repair commit]. `--check`: 11 proposed
subjects (2 patched), 17 requirements, 61 scenarios (PWB-REQ-010 goes from
2 to 7). `--selftest`: 4 position fixtures, and 50 structure mutants (5
engine, 45 builder), each failing on its own predicate.

**Not changed.** The table's nine rows and targets, the copy roles, the
verdict exclusion, the count's exclusions and the five `replaced` lines.
Questions 1–9 stand as written, except for the dated marks.
