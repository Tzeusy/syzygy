> # Record beside the package — not authority, binds nothing
>
> Dispositions of the sixth fresh-context review of the Three-Surface POC
> identity amendment package (P-84). This record is not a package
> artifact: the manifest does not hash it and no builder reads it. It
> classifies each round-6 finding and repairs nothing: every finding is
> open for the owner. It offers nothing and performs no act (VIS-4).

# Round 6 dispositions — Three-Surface POC identity amendment

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-6-RAW.md

- **Reviewed commit (raw line 2):**
  `0ea9b4912aceb2b18fd9c080c0a660350140d3d7`, the merge of the cycle-2
  repair (#421).
- **Manifest file digest (raw line 3):**
  `a1c00c7cba872468df752427d358199101a34b62f0ffe77eabe369e23e4b9867`.
  [Observed 2026-10-14] It re-derives from the manifest file's bytes at
  the reviewed commit, and the file is unchanged on the integration
  branch.
- **Verdict (raw line 4):** `REVISE`. Two revise findings (39, 40) and
  three notes (41–43), no blocking finding (raw line 364). Finding numbers
  continue from round 5.
- **Why the round ran.** The owner's direction of 2026-10-14 for a second
  cycle, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
  repair every finding, notes included, then one fresh review under the
  same stopping rule. The brief's §"Round 6" set that rule before the
  round, and carries its warrant as "[Observed: as relayed; not yet
  recorded under `decisions/`]"; the direction record now holds it.
- **Stopping rule applied** (brief §"Round 6"; raw lines 360–362). So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the "unconfirmed pending round 6" sentences
    in the packet, the delta and `ROUND-5-DISPOSITIONS.md`, with the old
    text kept. The disposition sentence finding 42 calls untrue is not
    marked: marking it is that finding's repair, and it stays open.
    `REVIEW-BRIEF.md` is not edited.
  - **No round 7 is dispatched** without a new owner direction.
  - **The bytes are not cleared** and this version is not offered for
    sign-off. Question 1 stays open; this record recommends nothing on it.
- **What the round confirmed.** Round-5 findings 33–38 are repaired as
  asked (raw lines 106–153). `--check`, `--selftest` and the dependency
  file pass in a clone; the patches apply over the P-97-bearing signed
  tree; criteria 1, 4, 5, 6 and 7 are met (raw lines 329–358).

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 39 | revise | The per-source identifier field is declared by the implementation slice under test (slice 6), yet the RFC6-1 covered row still claims "equal to the identity that authority gives it", with no Unknown row for whether the declaration is true; the package treats POC-REQ-055's slice-written declaration the other way | 157 | **Open for the owner.** Raw's repair, by the package's own precedent: add an RFC6-1 Unknown row ("The declared per-source identifier field is the identity the source authority gives"), narrow the covered row to "as read through the declared per-source field", and say in delta §1 and Departure 1 that the declaring slice is the one under test. |
| 40 | revise | The new unattributed-carrier limb falsifies subjects the shared model holds that no source record backs (seeded entities in `poc-seeds.ts`, including POC-REQ-051's `region:unmapped-code`), and "source record" is undefined, so the attribution needs judgment for many-record and no-record subjects | 206 | **Open for the owner.** Raw's repair, any of: define "source record" to include declared or seeded subject records and say how a many-record element is attributed; narrow the limb to identity values that name no subject the model holds; or state the obligation in the required behavior and disclose today's non-compliance. The round-5 phantom path must stay closed whichever is chosen. |
| 41 | note | The decision rule has no Unknown outcome, so a run where every subject's ownership is Unknown passes on the equality limb's zeros | 274 | **Open.** One sentence: where any subject's ownership is Unknown, the equality limb's result is Unknown, never a pass. |
| 42 | note | All 11 of the reviewer's non-control probes over cycle-2 text survive the phrase guards, and `ROUND-5-DISPOSITIONS.md`'s Finding 37 row says every added sentence is guarded | 294 | **Open.** Add guards and mutants for the cycle-2 text, and mark the untrue disposition sentence. Not marked here (see the stopping rule above). |
| 43 | note | `IMPACT-LEDGER.md` lines 81–83 still say the P-97 builder's `--check` passes over the repaired bytes; it exits 1 at the reviewed commit because P-97 is signed | 315 | **Open.** Mark the sentence at the sentence. |

**Stale sentences outside the marked files.** Register row P-84 and
`docs/README.md`'s M9 row sit outside the package and are updated
directly. P-100's round 3 cleared on 2026-10-14
(`../three-surface-poc-governing-intent-amendment/ROUND-3-DISPOSITIONS.md`);
the two stay a declared mutually exclusive pair, so whichever is signed
second is regenerated over the first. P-100's round-3 raw (finding 4)
asks that, if this package is signed first, P-100's encoding arm be
re-judged against the amended POC-REQ-060.
