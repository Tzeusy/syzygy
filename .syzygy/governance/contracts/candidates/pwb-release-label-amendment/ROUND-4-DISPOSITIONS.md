> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fourth fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-4 finding and repairs nothing: every finding is open for the owner.
> It offers nothing and performs no act (VIS-4).

# Round 4 dispositions — PWB release-label amendment

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md

- **Reviewed commit (raw line 2):**
  `8acb0795562c548201e24eb6a20d8eddc66f04d1`, the merge of the cycle-2
  repair (#424).
- **Manifest file digest (raw line 3):**
  `73cca446620b99bc6626adcc2530817fb4ef2c55d6a428d20f16150077fbca61`.
  [Observed 2026-10-14] It re-derives from the manifest file's bytes at
  the reviewed commit, and the file is unchanged on the integration
  branch.
- **Verdict (raw line 4):** `REVISE`. One revise finding (1) and seven
  notes (2–8), no blocking finding (raw line 206).
- **Why the round ran.** The owner's direction of 2026-10-14 for a second
  cycle, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
  repair every finding, notes included, then one fresh review under the
  same stopping rule. The brief's §"Round 4" set that rule before the
  round: "Any other verdict sends the package to the owner with its
  findings open. No round 5 is dispatched without a new owner
  instruction."
- **Stopping rule applied.** So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the "unconfirmed pending round 4" sentences
    in the packet, the delta and `ROUND-3-DISPOSITIONS.md`, with the old
    text kept. `REVIEW-BRIEF.md` is not edited; its heading "Round 4
    (added 2026-10-14, cycle 2; not yet dispatched)" is no longer true,
    and this record carries the correction.
  - **No round 5 is dispatched** without a new owner direction.
  - **The bytes are not cleared** and this version is not offered for
    sign-off. This record recommends nothing on Q1–Q5.
- **What the round confirmed.** Round-3 finding 2 and notes 3–7 are
  repaired; round-3 finding 1 is partly repaired (raw lines 59–67). Every
  check passes in a clone, the sibling builders pass, and criteria 3, 4, 5
  and 7 are met (raw lines 69–77).

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The provenance-stamp exception is decided by the implementation's own mark and a bare-id text shape, so a page that marks every naming of the revision as a stamp passes every decide-line; "lead with" has no observable; the falsifier has no limb for a naming presented as a stamp. The ledger itself prescribes wrapping prose namings (`polaris.ts` lines 1190, 1209) in stamps | 81 | **Open for the owner.** Raw's repair: make the stamp structural (only the revision element of a citation attached to an anchored claim, source, leaf or refusal, verified from the anchor records); a revision id in prose, a heading or the shape-identity section is never a stamp; the first naming on each page is a label unit with the label before the full id; add the falsifier limb. Or, if the owner prefers bare stamps in prose, a named choice, with the "cannot hide a naming" claim withdrawn. |
| 2 | note | The footer's evaluation identity (`polaris.ts` line 1881) shows the full observed revision on every page, matches no exception, and is missing from the ledger's inventory | 133 | **Open.** Name it in the inventory and say which treatment the text intends. |
| 3 | note | The status-line exception's warrant ("which the POC specification governs") is unanchored, since no POC requirement names the line; whether `data-human-status` is the mark is unstated | 146 | **Open.** Anchor or withdraw the warrant; say which mark. |
| 4 | note | The stability sweep is narrower than its falsifier limb and is blind to split text nodes | 151 | **Open.** Align the limb to the list or name the gap there; define the sweep over an element's whole text. |
| 5 | note | Construction records name test-3 conditions no fixture builds (unadmitted ancestry read, unreadable commit in a full clone, grafted object database) | 160 | **Open.** Add the fixtures or narrow test 3's observed population. |
| 6 | note | "Every Polaris page" has no stated population; the draft view carries no project-shape identity under PWB-REQ-020 | 177 | **Open.** Name the population, for example the human HTML routes under `/polaris`, excluding the PWB-REQ-020 machine and draft views. |
| 7 | note | Three load-bearing wordings are guarded only by the dependency digest; `lost_lines` can match a signed line to a later identical twin | 187 | **Open.** Add the three wordings to `REQUIRED_ONCE`; make `lost_lines` duplicate-safe. |
| 8 | note | The order check covers `spec.md` only; `design.md` (two decisions numbered 12) and `CAPABILITY-COVERAGE.md` (row 34 in both) collide with class-granular | 197 | **Open.** Already disclosed and routed to P-86's Q5 (whichever is signed second is regenerated and reviewed again). P-86's round 4 has since cleared, which does not resolve the collision. |

**Stale sentences outside the marked files.** Register row P-85 and
`docs/README.md`'s release-label row sit outside the package and are
updated directly.
