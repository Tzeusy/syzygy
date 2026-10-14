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
  - *(Marked 2026-10-14: "The package is not repaired again" and "No round
    4 is dispatched" are no longer the plan. Later that day the owner
    directed one more cycle: repair every round-3 finding, notes included,
    then one fresh review under the same stopping rule. The repair is
    mapped under "Repairs, 2026-10-14 (cycle 2)" at the end of this record.
    `REVIEW-BRIEF.md` now has a Round 4 section and a dated mark under its
    round-3 heading; the round-3 text above them is unedited.
    Round-3 findings repaired once on 2026-10-14, unconfirmed pending
    round 4. This record dispatches nothing.)*
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

## Repairs, 2026-10-14 (cycle 2)

Made under the owner's direction of 2026-10-14 to run one more cycle
(relayed by the lead session): repair every round-3 finding, notes
included, then one fresh review under the same stopping rule. The repair
base is `main` at `814fbcc1`. The anchor-resolution sign-off at `7f43802f`
had moved the signed PWB `spec.md`, so this builder's `--check` failed
there on its stale derived `GOVERNING-DEPENDENCIES.md.patch`. The two
authored patches that changed (`spec.md.patch`, `design.md.patch`) were
written as diffs over the current signed bytes. The derived patches and the
manifest were regenerated with `--write`, never hand-edited.

**Round-3 findings repaired once on 2026-10-14, unconfirmed pending round
4.** The dispositions above keep their **Open** marks: they describe the
round-3 bytes. None of these repairs is accepted until round 4 reads it.

Line numbers below are in `proposed/spec.md.patch` (`spec`) and
`scripts/build_pwb_release_label_amendment.py` (`builder`) at this commit.

| # | Finding | Repair |
|---|---|---|
| 1 | Naming site counts provenance stamps and verbatim Butlers text (revise) | The raw's first repair, adopted. A naming site is now defined positively: Polaris names the revision "only in a label unit", a marked element; every Polaris page presents at least one (spec 11–16). A separate prohibition bars the revision's full or twelve-digit id, or the project name followed by a captured tag name, from visible text outside a label unit, with three marked exceptions named in the text (spec 17–32): provenance stamps, whose whole text must be a revision id and which carry no label; Butlers-declared text PWB-REQ-014 keeps verbatim or the exact-source route serves under PWB-REQ-011, which stays byte-identical, so PWB-REQ-014 wins; and the shared operability status line. "Identities are not owner-visible text" is gone; attribute values and link targets stay out. The oracle now counts label units by mark as the denominator (spec 144–146) and runs the text sweep as its own denominator (spec 147–153). Decide-lines: at least one unit per page, zero swept occurrences outside units and exceptions, stamps hold only an id, excepted text equals its source (spec 176–180). Three falsifier limbs match (spec 202–206). Design decision 12's label-unit bullet says the same. The delta, packet and ledger name the implementation consequence: `polaris.ts` lines 241, 299, 1200, 1244 become marked stamps; lines 298, 1190, 1209 and the refusal sentences wrap their id in a stamp or become a label unit. The provenance-stamp and verbatim choices are drafter choices in the delta's §"Choices the cycle-2 repair made". |
| 2 | Oracle cannot derive either not-read form (revise) | The raw's repair, adopted. As it builds each fixture the checker records the conditions it imposes: tag-set and ancestry read admission, the ref made to fail, the commit made unreadable, and any shallow or graft boundary. These "construction records" are fixture facts the checker owns, not observer inputs (spec 127–132). The oracle applies tests 1 and 3 to those records and tests 2, 4 and 5 to its own listing and commit count (spec 154–161). The untagged decide-line names "as the construction records identify it" (spec 186–187), and oracle independence includes the construction records (spec 195–197). The delta's `RFC4-11.r1` paragraph says the not-read expectation now comes from the checker's record of the shallow boundary. |
| 3 | Shared status line is a POC component inside this sweep; the ledger says otherwise (note) | The status line is excepted by name from the prohibition (spec 31–32), and no change to `page-shell.ts` is proposed. The ledger's "Not covered" bullet is marked at the sentence and re-measured at `814fbcc1`: `humanStatusLine` line 47, rendered on Polaris through `polaris.ts` lines 1870–1882. The delta's §"Scope: Polaris only" gains "One shared component reaches Polaris". Whether the Polaris status line should carry the label is an owner content choice that touches a POC-governed file, so it is **Question 5** in the packet, not decided here. |
| 4 | "Nothing presents a tag as unmoved" has no observable, decide-line or falsifier (note) | The prohibition now names its scope: no label unit, label record or other visible text holding a captured tag name says the tag is unmoved, unchanged or stable (spec 91–94). A fifth sweep searches each label unit, the label record and every other visible text node holding a captured tag name, outside the excepted Butlers text, for a closed term list (spec 171–174). It is decided by "zero stability terms found by the fifth sweep" (spec 190), with the falsifier limb "a tag presented as unmoved, unchanged or stable" (spec 214). The closed list is a named drafter choice. |
| 5 | Where the tied-name expansion lives; the machine record as a "site in a label unit" (note) | The label unit holds "the expansion of any tied names" (spec 11–14), and the tie sentence ends "expandable on the surface, inside the label unit" (spec 82). The equality decide-line covers "each label unit, its expansion included", and says that the label-unit predicates apply to page sites only and the label record is decided by that equality alone (spec 181–184). |
| 6 | Selftest predicates are shared prefixes; the lost-line guard is order-blind (note) | Each required-phrase finding now carries its full phrase, and each such mutant expects its own phrase exactly through `phrase_finding` (builder 639–642), so no mutant is satisfied by another phrase's absence. `lost_lines` is now order-aware (builder 393–412): the signed lines, less the declared replaceable ones, must be a subsequence of the new lines, and a moved line is reported as "edited, moved or removed". A new mutant, "signed line moved", swaps two signed Oracle lines of PWB-REQ-001 and fails on that predicate. Round-3 mutants were added for Findings 1, 2, 4, 5 and 6 (builder 733–767). The selftest now runs 37 structure mutants (30 before). |
| 7 | Two Observed measurements in the delta are stale (note) | Both re-measured at `814fbcc1` and marked at the sentence, old text kept. Departure 3: the grep still returns nothing, but `reevaluation.ts` (last changed `c069f5f5`) can name a superseded evaluation; the conclusion now rests on there being no captured tag set (`git-observation.ts` reads no `refs/tags`). §"Scope: Polaris only": `page-shell.ts` line 47, `orrery.ts` lines 197 and 212, `trajectory.ts` line 236, and "footer" corrected. Also re-measured, with the same marks: `git-observation.ts` lines 62, 106 and 161; the reconciliation census (17 / 52 now, 17 / 56 after apply) and the successor-chain lines (244–257); the §"Pending siblings" population (three pending, P-96 performed); and the impact ledger's census (2,683 paths, 96 files). |

**Builder, besides Finding 6.** `REQUIRED_ONCE` gains the round-3 phrases
(builder 169–197). The anchor-resolution package is removed from the
selftest's expected pending-patch population (`ORDER_POPULATION`, builder
851), since its sign-off moved it to `PERFORMED_SIBLINGS`. Requirement
count 17; scenarios 56, which is 52 signed plus the same four new ones.
The regenerated `CONTRACT-COVERAGE.md.patch` is byte-identical to round
3's, so the coverage totals are unchanged.

**Left for the owner.** One finding needed an owner content choice:
Finding 3, now Question 5. The four drafter choices in the delta's
§"Choices the cycle-2 repair made" can be changed by answering Question 1
*Revise*.
