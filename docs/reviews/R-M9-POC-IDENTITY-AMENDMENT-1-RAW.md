# R-M9-POC-IDENTITY-AMENDMENT-1 — fresh-context review of the Three-Surface POC identity amendment package
Reviewed commit: 26b0b8432667c1ac61c796b7ebebc656d75fee27
Manifest SHA-256: 679e03cf34f93b6d03ae81c7696a04b2ed9ba9656d5892176fa85350013c105b
Verdict: REVISE

Reviewer: fresh-context agent. It read only the package, its governing references as listed in `REVIEW-BRIEF.md`, and the acceptance criteria. The review ran in a clone at the commit above. No file in the repository was edited. The patches were applied only in a scratch copy outside the clone, built with `git archive HEAD openspec/changes/three-surface-poc-experience` and `patch -p1`.

## What was run, and what it printed

- [Observed] `python3 scripts/build_three_surface_poc_identity_amendment.py --check` exited 0. It printed: "manifest matches 6 proposed subjects (4 patched, 2 unchanged); 26 requirements, Part A 78 clauses over 122 rows; structure, regeneration and the preserved RFC1-26 row verify".
- [Observed] `--selftest` exited 0. It printed: "18 structure mutants, patch drift, manifest order and subject drift all fail closed on their own predicates". Each mutant was read in the source (`scripts/build_three_surface_poc_identity_amendment.py` lines 479–570). Each asserts that a finding starts with its own predicate string (line 575), not just that something fails. So rule 6 is met for the predicates the builder declares.
- [Observed] `python3 scripts/check_governance.py` printed "31 OK, 21 WARN, 0 FAIL (52 checks)". No WARN or FAIL line names the package directory (`grep -F identity-amendment` over the output found 0 lines).
- [Observed] Scratch apply: all four patches applied cleanly. The `sha256sum` of each of the six subjects equals its manifest row (manifest lines 7–12).
- [Observed] The dependency generator was run in the scratch copy: `build_three_surface_poc_spec_dependencies.py --check` printed "match regeneration — 26 requirement(s), 90 distinct authorities".
- [Observed] I counted the matrix in Python over the proposed `CONTRACT-COVERAGE.md`:
  - Part A has 122 rows over 78 clauses: 102 covered and 20 Unknown.
  - Part B1 has 28 rows over 27 clauses.
  - Part B2 has 219 clauses.
  - Per family, Part A splits RFC1 12, RFC2 8, RFC4 10, RFC5 1, RFC6 13, RFC7 12, RFC8 5, RFC9 17. Part B2 splits RFC1 23, RFC2 19, RFC3 38, RFC4 21, RFC5 11, RFC6 14, RFC7 25, RFC8 27, RFC9 41.
  - The `contracts[]` union equals the Part A clause set (78 = 78, symmetric difference empty).
  - No clause appears in both Part A and Part B2.

  All of these equal the printed figures. The signed figures recompute to 107/74/92/15 and 223.
- [Observed] The proposed spec has 26 `### Requirement:` headings and 28 `#### Scenario:` headings, matching `IMPACT-LEDGER.md:85-86`.
- [Observed] Signed bytes:
  - `diff` of signed against proposed shows that the only removed lines in `CONTRACT-COVERAGE.md` are the RFC2 and RFC6 family rows, the totals, and the four Part B2 rows (RFC2-25, RFC6-1, RFC6-3, RFC6-12).
  - The RFC1-26 row `| RFC1-26 | Relations outside the closed table don't exist; no prose-widening | covered | POC-REQ-052 |` sits byte-identical at signed line 89 and proposed line 90.
  - In `spec.md`, the only removed lines are the reader-note group and warrant sentences and the POC-REQ-060 block. `proposal.md` is purely additive.
  - The current six subjects hash to the readability successor act's successor column (`THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md:32-37`).

  Criterion 4 is met.
- [Observed] The impact-ledger sweep was re-run over `git ls-tree -r -z ab22492` (1,924 paths, 4 UTF-8 decode skips). It returned exactly the table at `IMPACT-LEDGER.md:32-37`: 46/242, 2/2, 3/8, 15/43, 37/68, 21/55. The three POC-REQ-054/055 files and the three code files citing POC-REQ-060 are as listed.
- [Observed] RFC1-25's table at `RFC-0001-project-graph-identity-state-planes.md` has 26 data rows (lines 596–621) and 30 backticked first-column tokens. At `ab22492`, `poc-seeds.ts` lines 196–260 emit nine relationships over eight kinds, of which only `contains` is a table token. This matches `SEMANTIC-DELTA.md:133-138`.
- [Observed] Every quotation was checked against its source, with whitespace normalized and bold markup ignored:
  - the P-75 row and its consequences (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:63`);
  - RFC6-1 (line 108ff), RFC6-3 (135), RFC6-12 (263) and RFC1-26 (736);
  - the RFC2-25 `asserted-by-worker` authority cell (`rendering-vocabularies.md:180`);
  - `trust-and-evidence.md:25`;
  - Scope A's list;
  - POC-REQ-052's and POC-REQ-060's signed text;
  - the matrix's "A belief is not a reviewed N/A".

  All match. One line-number imprecision is in Finding 11.

## Findings

**Finding 1 — POC-REQ-054 requires the shared model to mint every subject's identity, against RFC1-9 and RFC6-1** (revise)

- **The new requirement.** [Observed] Proposed POC-REQ-054 reads: "Every subject the shared model holds SHALL carry one identity, minted once by the shared model" (`--diff` line 290).
- **What RFC1-9 says.** [Observed] RFC1-9 (`RFC-0001-…md:300-307`) reads: "the kernel **never mints an identity it does not own**: work-item identities are mirrored from the scheduler; … code-element identities come from the source adapter."
- **The signed coverage of RFC1-9.** The signed matrix maps that consequence as covered: `| RFC1-9 | Work-item identity mirrored from scheduler; kernel never mints/owns it | covered … | POC-REQ-010, POC-REQ-012 |`.
- **The omitted RFC6-1 limb.** [Observed] RFC6-1 at line 113 says "the kernel mints nothing new for selection". The delta's quotation of RFC6-1 (`SEMANTIC-DELTA.md:97-103`) begins after that limb and so omits it.
- **The conflict.** [Inferred] The POC's shared model holds `work-item` and `code-region` entities (`poc-seeds.ts:159-173`). So read literally, the amended specification would require the model to mint identities that a signed covered row says it never mints. Two requirements of the same spec would then pull against each other.
- **Not covered by the delta's reasoning.** The "Why the identity is not spelled out" reasoning (`SEMANTIC-DELTA.md:117-122`) addresses the path-form bar only, not the minting-authority bar.
- **An unlisted RFC6-1 limb.** RFC6-1's tuple limb is neither covered nor listed as Unknown: "(entity kind, durable entity identity) … exactly RFC 0001's (RFC1-5, RFC1-9/10)". Only the qualifiers limb gets an Unknown row (`--diff` line 52).
- **Repair.** Say "carry one identity, held in the shared model" (minted by the class's own authority per RFC1-9), not "minted by". Add an Unknown row for RFC6-1's RFC1-identity-tuple limb, or a covered row if the oracle is extended to check it.

**Finding 2 — The RFC1-25 amendment row and the disclosure claim a closure consequence that POC-REQ-055's oracle does not observe** (revise)

- **The vocabulary rule.** [Observed] Part A's disposition vocabulary says **covered** means "the named requirements' oracles observe the consequence" (`CONTRACT-COVERAGE.md`, Part A preamble).
- **The RFC1-25 row.** The new RFC1-25 row claims, as covered by POC-REQ-055: "Every emitted relation kind named from the closed table, with source and target in the roles the table assigns" (`--diff` line 28).
- **What the oracle accepts.** POC-REQ-055's oracle is "per-kind membership-or-flag … zero unflagged out-of-vocabulary kinds" (`--diff` line 385). It passes with seven of eight kinds outside the table, provided they are flagged. The row's own note concedes this ("the seven kinds outside the table take POC-REQ-055's flag instead"). So the consequence column states a property the oracle does not decide.
- **The disclosure.** Likewise, the disclosure (`--diff` lines 84–85) says "The closure consequence is carried by POC-REQ-055". RFC1-26's closure consequence is "Relations not in this table do not exist at V0". POC-REQ-055 discloses outside kinds; it does not make them absent.
- **What the ruling did and did not decide.** [Inferred] P-75 Q3 ruled that the seven are "repaired by a new requirement … plus disclosure". That makes the flag the owner's chosen repair. It does not make "every kind is named from the closed table" an observed consequence.
- **Repair.** Label the RFC1-25 row's consequence as what the oracle observes: each closed name is in its assigned roles, and every other kind is flagged. Then either:
  - add an Unknown row "no relation outside the closed table is emitted", with the ruling cited as the reason it stays Unknown; or
  - reword the disclosure from "carries the closure consequence" to "carries the disclosure the ruling chose as the repair; closure itself is not observed".

  Either route leaves the signed RFC1-26 row untouched.

**Finding 3 — Uncovered limbs of newly mapped clauses are not listed as Unknown** (revise)

Criterion 3 requires every uncovered limb of a newly mapped clause to be listed as Unknown. [Observed] The following limbs of the four clauses moved out of Part B2 have neither a covered row nor an Unknown row.

- **RFC2-25** (`rendering-vocabularies.md:168-200`):
  - The per-tier authority semantics are missing: `gate-backed` is "The **only** tier that may support a positive status claim"; `report-fact` "Supports claims about the report only"; `reduced-fidelity` renders "explicitly as reduced fidelity"; `declared-only` "Both halves must render"; `suspended` "the basis is never erased". POC-REQ-060's oracle validates tier *membership and nesting* only (`--diff` lines 456–458). The one covered tier row (`--diff` line 41) is honest about that, but these limbs are missing.
  - The `asserted-by-worker` authority cell is "Visible, never green, **challengeable**, never a status input". The covered row (`--diff` line 42) omits "challengeable" without an Unknown row. Its "never a status input" is wider than what the oracle observes, which is exclusion from Observed totals and not clearing an Unknown.
- **RFC6-3** (line 135): "same entity, same evaluation, same scenario context, same drawer fact set". Only "same entity" (covered) and the skew limb (Unknown) are listed. The evaluation, scenario-context and drawer-fact-set limbs are not.
- **RFC6-1:** the RFC1 identity-tuple limb (Finding 1).
- **RFC6-12:** "subject to `not-applicable` per RFC6-5". This one is minor.

The matrix's own row-method note says "a reviewer who finds an unlisted limb has found a real gap". Add the Unknown rows. The totals and family table then need recomputation; the builder already enforces that.

**Finding 4 — Several falsifier limbs have no deciding oracle, or an oracle that consults the implementation under test (CC-SPEC-4)** (revise)

- **The bar.** [Observed] CC-SPEC-4 (`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:184-214`) requires the oracle to decide "by a stated procedure", and "oracle independence: the oracle is not defined by, and does not consult, the implementation under test". It rejects an oracle "equal to 'whatever the implementation computes'".
- **POC-REQ-054.** Its oracle independence reads: "the subject identities and slot values come from the machine answer, never from a surface's renderer" (`--diff` line 325). The machine answer is the shared model's output, which is the implementation under test. Two falsifier limbs are therefore undecidable by the stated oracle:
  - "one subject named by two identity values": if the model mints two identities for one subject, both are in the machine answer's subject set, and per-element equality passes;
  - "a three-state slot … filled from a subject not joined by the identity": slot values are taken from the machine answer, so a wrong join in the model is copied into the expected value.

  [Inferred] The adopted design's own slice-5 mutant (a) needs an independent join derivation, for example the work item's external reference naming the claim (`POLARIS-M9-ONE-IDENTITY-FUNNEL.md:898-899`). The requirement does not name one.
- **POC-REQ-060.** The Observable lists three properties of an Inferred record: absence from every Observed total, leaving each Unknown Unknown, and distinct rendering (`--diff` lines 452–455). The Falsifier adds "arising from a non-agent source". But the Oracle (`--diff` lines 456–458) names only "per-encoding equality … and per-record vocabulary validation … zero off-vocabulary records decide". No stated procedure decides the total-exclusion, Unknown-clearing or agent-provenance limbs. Agent provenance also has no named observable at all.

Repair: name an independent expected value for subject identity and join membership, derived from source records rather than the model's answer. Then extend each Oracle line to the limbs its Falsifier lists.

**Finding 5 — The package departs from the adopted slice-3 design on the join key, and the owner packet does not say so** (revise)

- **The design and the package.** [Observed] The design the ruling adopted says of POC-REQ-054: "Declares the canonical join key" (`POLARIS-M9-ONE-IDENTITY-FUNNEL.md:797-798`). Slice 6b is labelled "The key, slice 3's act" (line 920). The package deliberately does not declare the key; it leaves the form to slice 6 (`SEMANTIC-DELTA.md:117-122`, labelled [Inferred]).
- **The reasoning is sound.** [Inferred] RFC6-1's path bar is real, and the slice-6b key `repository:<repo>@<rev>:<path>#<objectId>` contains a path.
- **The owner is not told.** `OWNER-DECISION-PACKET.md:13` says "One amendment … the one P-75 ruled", and it never mentions that one ruled content item is narrowed. A narrowing of what the owner adopted is the owner's call (VIS-4; CC-SPEC-6's "the spec records which open questions it believes it does not settle").
- **The consequence is left unstated.** On sign-off, slice 6b would choose the key under POC-REQ-054 with no further act, where the design expected the key to be in the signed text. The packet does not say this.

Repair: state the departure and its consequence in `OWNER-DECISION-PACKET.md`. Add a line to the spec's reader notes or to the delta saying the key's form is an open question this amendment does not settle.

**Finding 6 — The signed RFC6-14 row's fold note becomes stale beside the new tier row, with no disclosure; the secondary-annotation limb stays unlisted** (note)

- [Observed] The signed RFC6-14 row says: "Fold: full RFC2-25 tier / secondary-annotation / sibling-surface-state / challenge-pending limbs dropped — POC carries no such vocabulary" (`--diff` line 58). The new amendment row two lines below covers the tier limb (`--diff` line 59).
- RFC1-26 gets a dated disclosure telling the reader which row to trust. RFC6-14 gets none, so a reader sees two rows that disagree on whether tiers are carried.
- RFC6-14's "Secondary Unknown annotations travel with the primary" limb remains covered only by that fold. So does RFC2-24's limb "The secondary-annotation vocabulary is closed, and it is this same list" (`rendering-vocabularies.md:108`). POC-REQ-060's record shape now speaks of "exactly one primary reason" and is silent on secondaries.

Consider a one-sentence disclosure for RFC6-14, and an Unknown row for the secondary-annotation limb.

**Finding 7 — Two scenarios presume a condition their requirement makes conditional** (note)

- [Observed] POC-REQ-054's ribbon paragraph is conditional: "Where a surface renders one claim's standing in the desired, execution and observed states together …" (`--diff` line 299). Scenario "A three-state view with nothing joined" (`--diff` lines 341–348) has a WHEN that does not state that any surface renders the view. Its THEN asserts that slots render.
- Likewise, scenario "One subject, one identity on every surface" asserts that "a link from one surface to the other resolves" (`--diff` line 336). The requirement only constrains links that exist.
- [Inferred] Both scenarios are stronger than the requirement text that carries them, against criterion 2's "scenarios that the requirement text actually carries". Add the condition to each WHEN.

**Finding 8 — POC-REQ-055's "an expected role pair for that relation" is singular, but RFC1-25 rows carry several endpoint pairs** (note)

[Observed] Several rows carry more than one endpoint pair:

- `contains` / `part_of` has six (`RFC-0001…md:596`);
- `implements`, `verifies`, `depends_on` and `cites` each carry more than one.

The case text (`--diff` line 379) and the Oracle's "zero reversed roles" read most naturally as one pair per relation. Say "the set of role pairs the table assigns".

**Finding 9 — Two citations that do not resolve at the reviewed commit** (note)

- [Observed] `OWNER-DECISION-PACKET.md:8-9` says the review of record is "recorded in this package's `ROUND-1-DISPOSITIONS.md`". No such file exists at `26b0b84`. It is a forward reference with no marker saying so.
- [Observed] `SEMANTIC-DELTA.md:60-61` grounds "Lane B's manifest is disposed of" in "the bead's 2026-10-03 audit note". No bead export is present in the clone. The fact is corroborated by tracked files: `scripts/check_governance.py:1780` ("Lane B was declined 2026-10-02 and never performed") and `pwb-missing-currency-disclosure-scenario/SEMANTIC-DELTA.md:242`. Cite a tracked record.

**Finding 10 — The proposal's amendment section overstates the Part B2 moves** (note)

- [Observed] The proposed `proposal.md` says "four Part B2 beliefs move to Part A because a requirement now covers them" (`--diff` lines 241–242).
- The delta states it correctly: "because a requirement now covers one of their consequences" (`SEMANTIC-DELTA.md:211-212`).
- Each of RFC2-25, RFC6-1, RFC6-3 and RFC6-12 keeps at least one Unknown row. Align the proposal with the delta. A signed-surface sentence should not say "covers them".

**Finding 11 — RFC6-1 line citation imprecise** (note)

[Observed] `SEMANTIC-DELTA.md:98-103` places both quoted RFC6-1 sentences at "lines 113–115". The second ("every handle must resolve … an endpoint.") is at lines 116–118 of `RFC-0006-cross-surface-selection-query-drawer.md`.

## Criteria summary

1. **Ruling content:** largely met.
   - All six content items are present: POC-REQ-054, the POC-REQ-060 amendment, POC-REQ-055, the ribbon scenario, Q3's new requirement plus disclosure with the signed row unedited, and Q4's fixture-only Inferred limb.
   - Nothing beyond the ruling was found.
   - The join-key narrowing is undisclosed to the owner (Finding 5).
2. **Specification bar:** not met. See Findings 4, 7 and 1.
3. **Contract claims:** not met.
   - Every quotation matches its source.
   - Coverage honesty fails: see Findings 2, 3 and 6.
4. **Signed bytes:** met. The RFC1-26 row is byte-identical, and only the four named Part B2 rows moved.
5. **Mechanics:** met. `--check`, `--selftest` and the regeneration all pass, and the totals equal computation.
6. **Honest claims:** met for adoption and implementation scheduling.
   - The three residuals are named (`SEMANTIC-DELTA.md:235-251`).
   - `check_spec_reconciliation.py:214` pins `"POC": (24, 24)`.
   - `real_packages()` lists only PWB packages (`record_versioned_signoff.py:117-130`).
   - Scope A's list is quoted correctly.
   - Exceptions: Findings 5 and 9.
7. **Plain language:** met. A fresh reader can restate what changes from `OWNER-DECISION-PACKET.md` and the delta, subject to Finding 10.
