> # Record beside the package — not authority, binds nothing
>
> Dispositions of the third fresh-context review of the PWB release-label
> amendment package. This record is not a package artifact: the manifest does
> not hash it and no builder reads it. It offers nothing and performs no act
> (VIS-4).

# Round 3 dispositions — PWB release-label amendment

- **Reviewed commit (raw line 2):**
  `7baea99151f68ac883f27d1ed4c79e608dce08bd`, the head of
  `candidate/p85-round2-repairs` (draft PR #414).
- **Manifest file digest (raw line 3):**
  `610880fd9ce477bf094856dee7c4af90f5231d4186b4e413bdf242fc015c1dd1`.
  [Observed 2026-10-14] The manifest file hashes to the same value after the
  branch was rebased onto `main` and landed with this record, and the
  builder's `--check` passes there.
- **Verdict (raw line 4):** `REVISE`. Two revise findings (1, 2) and five
  notes (3–7), with no blocking finding (raw line 243). Criteria 2 and 3
  are not met; 1 and 4–7 are met.
- **Reading scope the reviewer disclosed.** The round-3 brief forbade
  reading the earlier dispositions and raws; the dispatcher asked for a
  repair check against this package's "Repairs, 2026-10-14" section, and
  the reviewer read that section only (raw lines 44–51).
- **Stopping rule applied.** The owner's direction of 2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`):
  one repair and one review per packet; anything still `REVISE` goes to the
  owner with its findings, not into another loop. Round 2's findings were
  repaired once and round 3 is the one review. Round 3 is not notes-only.
  So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the sentences that said round 3 was pending.
    `REVIEW-BRIEF.md` is not edited: its "Round 3 (added 2026-10-14; not
    yet dispatched)" heading and "No round 3 is dispatched" sentence are the
    brief the round ran under, and are stale only as status.
  - **No round 4 is dispatched.**
  - **The bytes are not cleared.** This version is not offered for sign-off
    under Scope A item 3. It goes to the owner as register row P-85, with
    the seven findings below open.
  - This record recommends nothing on Questions 1–4.

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md

## Round-2 repairs, as the reviewer judged them

Raw lines 53–62: findings 1, 4 and 5 repaired; 6 repaired in text and
fixtures; 2 and 3 partly repaired (their remainders are findings 2 and 1).

## Dispositions

### 1 — the naming-site definition still counts per-fact revision stamps, and now counts verbatim Butlers text (revise)

**Open.** Raw line 80. On a literal reading every provenance stamp owes a
full label unit; on a narrow reading the checker must judge which visible
hex strings are identities (CC-SPEC-4). The project-name limb can collide
with PWB-REQ-014's verbatim leaves; whether Butlers text contains such a
string is [Unknown]. The raw's repair: define a naming site positively,
with a separate prohibition over unmarked text that excludes provenance
stamps and verbatim leaves by name.

### 2 — the oracle procedure cannot derive either not-read expected form, including the fixture added for `RFC4-11.r1` (revise)

**Open.** Raw line 137. Tests 1 and 3 depend on capture conditions the
checker's own listing does not carry, so on the new fixture a checker
following the text expects *described*, and the defect r1 names would pass.
The raw's repair: make each fixture's construction conditions
checker-owned recorded inputs, and apply tests 1 and 3 to them.

### 3 — the shared status line puts a POC-governed component inside this package's sweep (note)

**Open.** Raw line 179. `page-shell.ts`'s `humanStatusLine` shows the
revision prefix on Polaris pages; the ledger lists it as not covered.

### 4 — "Nothing presents a tag as unmoved" has no observable, decide-line or falsifier limb (note)

**Open.** Raw line 190.

### 5 — where the tied-name expansion lives, and the machine record as a "site in a label unit" (note)

**Open.** Raw line 200.

### 6 — selftest predicates are shared prefixes, and the lost-line guard is order-blind (note)

**Open.** Raw line 215. The current diff moves no signed line, so
criterion 4 holds for these bytes.

### 7 — two Observed measurements in the delta are stale at the repair base (note)

**Open.** Raw line 229. Departure 3's grep and the §"Scope: Polaris only"
line citations need re-measuring at the repair base.
