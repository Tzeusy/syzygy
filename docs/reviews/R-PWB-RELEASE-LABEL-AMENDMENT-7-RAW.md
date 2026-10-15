# R-PWB-RELEASE-LABEL-AMENDMENT-7 — fresh-context confirmation review, round 7
Reviewed commit: decd32d8c9daa06c632d39674cdf5aa250244a4e
Manifest SHA-256: 36c8750691dfe1a5bb0126052df2c517ea33bf876f323a1d58c59b0b3f0d49b1
Verdict: REVISE

## Provenance and method

- **Commit.** A fresh `git clone git@github.com:Tzeusy/syzygy.git` to `/home/tze/.cache/claude-tmp-a3f4/r7-clone`, then `git checkout --detach decd32d8c9daa06c632d39674cdf5aa250244a4e`. The clone's HEAD is `decd32d8 governance(candidates): P-85 cycle 5 - withdraw 'never a stamp', …`. Every check below ran in that clone (rule 7).
- **Manifest digest.** `sha256sum` over `.syzygy/governance/contracts/candidates/pwb-release-label-amendment/PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` in the clean clone at that commit. It is the digest of the manifest file, not a row inside it.
- **Checks, output read (rule 4):**
  - `build_pwb_release_label_amendment.py --check`: "release-label candidate matches 11 proposed subjects (7 patched); 17 requirements, 68 scenarios; structure, regeneration, contract coverage, sibling classification and pending-patch order verify".
  - `--selftest`: "77 structure mutants, patch drift, an unclassified sibling, the pending patch population, divergent and failing application orders, a colliding companion patch, and the lost-line guard against an independent subsequence count all fail closed on their own predicates".
  - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted".
  - `--diff` read in full.
- **Census, independently.** [Observed] The signed `spec.md` has 63 `#### Scenario:` headings, and `proposed/spec.md.patch` adds 5 (`grep -c '^+#### Scenario:'`), so 68. The patch's only `-` lines are the two warrant lists (patch lines 356–357).
- **Totals, recomputed.** Capability 29 + 6 + 0 = 35. Repair delta 92 + 2 = 94 rows, 77 + 1 = 78 superseded, 60 + 1 = 61 covered, 27 Unknown, 5 + 1 = 6 not applicable, and 61 + 27 + 6 = 94. Coverage 628 + 1 = 629, with 136 + 1 = 137 covered and 245 not applicable unchanged. All match the patches.
- **My own falsifier oracle (rule 6).** `/home/tze/.cache/claude-tmp-a3f4/r7_oracle.py` is a scratch script. It implements the sweep (the twelve-digit prefix and "project name + tag"), the "zero swept occurrences outside a label unit and the excepted elements" decide-line and the identity decide-line literally. It ran over three hand-built fragments, each opening with one label unit:
  - an identity element in a sentence: **PASSES every decide-line**, yet scenario 5's THEN is false (Finding 2);
  - control, a bare twelve-digit id in a sentence: **FAILS** ("occurrence … outside unit/excepted");
  - control, an identity that is not served: **FAILS** ("identity … not served").
- **My own structure mutants (rule 6).** `/home/tze/.cache/claude-tmp-a3f4/r7_mutants.py` runs `structure_findings` over `proposed_bytes()` (baseline `[]`):
  - "running text passes these tests" → "fails" in the spec: killed by its own `REQUIRED_ONCE` phrase;
  - "(inside a sentence passes), and which tokens a served locator holds" → "(inside a sentence fails)" in `design.md`: **0 findings** (Note 3);
  - the scenario-5 WHEN widened to "outside every label unit or citation": only the `GOVERNING-DEPENDENCIES` digest finding (Note 3).
- **Reading scope.** I read:
  - `REVIEW-BRIEF.md` in full;
  - `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md` and `IMPACT-LEDGER.md` in full, and the manifest;
  - the builder's phrase tables (lines 144–336);
  - `docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-6-RAW.md` and `ROUND-6-DISPOSITIONS.md`;
  - `apps/three-surface-poc/src/polaris.ts` (lines 660–700 and grep hits for identity rendering) and `polaris-source.ts` (lines 112–142).

  Two reads fall outside the brief's file list, and I disclose them. The first is `packages/three-surface-poc-core/src/project-shape-observation.ts` lines 331–334 and 555–570, read to learn the source-identity format. The second is one grep line of `project-shape-model.test.ts`. I did not open `ROUND-1-…` to `ROUND-5-DISPOSITIONS.md`, any other raw, or any Butlers content, and I did not run the daemon.

## Round-6 findings: are they repaired?

| R6 # | Raw's finding | Status at this commit |
|---|---|---|
| F1 (revise) | "therefore never a stamp" does not follow: an embedded citation (route A) and a phrase-like locator (route B) | **Repaired in the requirement, not everywhere.** The spec sentence is gone, and both gaps are stated in the requirement in the closed-list form: "Two limits stay. Where a citation sits is not decided by this requirement: … Which tokens an anchor's served locator holds is not decided either". Scenario 5 is renamed, and an AND states the placement gap. Question 6's recommended row is reworded. But the packet's summary and one delta design choice still state the withdrawn property (Finding 1). The narrowed THEN still claims more than the oracle decides, by a route the round-6 raw did not name (Finding 2). |
| N1 (note) | Six cycle-4 wordings guarded only by the digest | **Repaired.** All six are in `REQUIRED_ONCE` (builder lines 202–207; the two decide-line wordings are merged into one phrase at 204), each with a selftest mutant (lines 905–924), and selftest reports 77 mutants. |
| N2 (note) | Design decision 13 and the delta's account not carried; "four scenarios" stale | **Repaired.** Decision 13 carries the cite-text rule, both gaps, the closed identity population and the twelve-digit scope. The delta says "Five new scenarios" with a dated note, and packet Question 1 says five. One stale census remains in the delta's residuals (Note 2). |
| N3 (note) | Swept only at twelve digits | **Repaired.** "These three are the namings the text sweep below finds, and "names the observed revision" means them: a shorter prefix of the object id is not decided by this requirement." The design says "a shorter prefix is not decided." |

## Criteria

1. **Direction content: met.** The label leads, the id sits beneath it, moved tags are disclosed, and the untagged form is honest. The departures are Q2–Q6.
2. **Specification bar: not fully met** (Finding 2). What remains decided is still a sweep with a denominator ("The count of those sites is the denominator"; "the occurrence count as this sweep's own denominator") and a falsifier list the decide-lines catch. But scenario 5's THEN is not carried by the decide-lines.
3. **Contract claims: met.** The coverage, proposal and repair-delta patches are unchanged in substance from round 6. RFC4-11.r1 rests on "it never reconstructs commit history it cannot reach", and the totals re-derive.
4. **Signed bytes: met.** Only the two warrant lines are removed, and the builder's byte-identity and lost-line checks pass.
5. **Mechanics: met.** All four checks pass in the clone, and the totals and census re-derive. One small guard gap remains (Note 3).
6. **Honest claims: not met** (Finding 1). The packet's "What you would be signing" still promises the withdrawn property.
7. **Plain language: met with Note 1.**

## Findings

**Finding 1 — The withdrawal is incomplete: the packet's signing summary and the delta's cycle-3 choice still say an id in a sentence or heading is never a stamp** (revise)

The owner's direction was: "Drop 'never a stamp', state both gaps as limits". The requirement does this. Two unmarked present-tense sentences outside it still assert the withdrawn property.

- [Observed] `OWNER-DECISION-PACKET.md` lines 138–141 sit in "What you would be signing", the summary the owner signs from: "the short id stamped in each claim's source citation … Only a citation's revision counts; an id in a sentence or heading never does (Question 6)". The requirement now says the opposite: "a citation placed inside a sentence, a heading or other running text passes these tests, though its words then name the revision outside a label unit". By the requirement's own definition, a stamp is a naming ("These three are the namings the text sweep below finds"). So an id in a sentence, inside a citation, does count.
- [Observed] `SEMANTIC-DELTA.md` lines 658–662, §"Choices the cycle-3 repair made", choice 1: "So a revision id in a sentence, a heading or the shape-identity line is never a stamp; it is a label unit, or it goes." Unlike choice 2 just above it (lines 634–637), it carries no dated withdrawal mark. Its own §"Repaired a fifth time" says only the requirement, the scenario and Question 6 changed.

The brief asks "whether the withdrawal is complete, so that no requirement text, scenario, design line or packet option still claims that a sentence, heading or identity line never names the revision through a citation". These two lines still make that claim. The first sits in what the owner reads in order to sign (criterion 6). [Inferred] A repair would reword packet line 139–141 to match Question 6's recommended row, and add a dated mark at delta line 660–662 that keeps the old words (the CG-27 lesson: mark it at the stale sentence).

**Finding 2 — Scenario 5's THEN is still not decided: an identity element placed in a sentence shows R's full object id outside a citation, and passes** (revise)

The narrowed scenario says:

> "**WHEN** a Polaris page has a sentence about the observed revision R outside every label unit **THEN** outside a citation the sentence shows neither R's full object id nor its first twelve hexadecimal digits"

The requirement excepts a second kind besides the stamp:

> "an identity, whose whole text equals the evaluation identity that the machine answer serves for that page's evaluation, or the source identity of one source record that the machine answer serves at that evaluation, and is not a revision's id alone."

Its decide-line checks only the text: "every excepted identity's whole text equal to the evaluation identity or to the source identity of one source record served at that evaluation, and not a revision's id alone". Like the citation rules, it says nothing about where the identity element sits.

- [Observed] Both excepted identities contain the full revision. `sourceIdentityOf` returns `` `${repositoryId}@${revision}:${source.path}${object}` `` (`project-shape-observation.ts` line 333). The package says so itself: the delta at lines 231–233 says "the page footer's evaluation identity and the exact-source route's source identity, both of which contain the full revision", and the packet at line 143 says "which contains the full id".
- [Observed, scratch oracle] This fragment passes every decide-line I implemented, after a leading label unit:
  ```html
  <p>Declared project shape of butlers at <code data-kind="identity">repository:butlers-configured-poc@R:about/x.md#…</code>.</p>
  ```
  The sentence is about R and lies outside every label unit. Outside any citation it shows R's full object id. The THEN is false, and the oracle passes.
- [Observed] This is not contrived. Today's exact-source footer is already a sentence that holds an identity: `` footer: `Evaluation <code>${…model.evaluation.snapshot}</code> as of <code>…</code>.` `` (`polaris-source.ts` line 141). The source identity line (line 117) is a `<p>` holding a label word and the identity.

The two stated limits are both true: placement of a *citation*, and the locator token set. But neither covers this route. The scenario's own AND says only "whether that citation sits inside the sentence is not decided". So the THEN claims more than the decide-lines decide, by a route that is not disclosed. That is the defect the brief names for revise ("where the text still claims more than its oracle decides"), and the defect the round-6 raw held at revise ("scenarios its text carries"). It is narrower than round-6 Finding 1, and it is closed by the same kind of repair.

[Inferred] Proposed repair, in the owner-chosen form:

- state the identity's placement as part of the first limit, for example "Where a citation or an excepted identity sits is not decided by this requirement";
- narrow the THEN to "outside a citation and an excepted identity", or make the AND name both.

Either keeps the decided sweep as it is. A placement rule for identities would be a content change for the owner, not a repair.

**Note 1 — Question 6's table is broken by the dated note inserted between its rows** (note)

[Observed] `OWNER-DECISION-PACKET.md` has the recommended row at line 273, then a blank line, then the dated note as a paragraph (lines 275–280), and then `| Bare ids in sentences may stay | … |` at line 281. In GFM, a pipe line after a paragraph with no header or delimiter row is not a table row. So the second option renders as a stray line of pipes, detached from the table. The owner reads this question to choose an arm (VIS-3). Move the note below the table.

**Note 2 — The delta's residual census is still at its cycle-3 figures** (note)

[Observed] `SEMANTIC-DELTA.md` lines 721–727 say "after `--apply` they read 17, 60 and 5 (the builder's `--check` prints 60)". At this commit the builder prints 68 scenarios, and PWB-REQ-001 carries 1 + 5 = 6. `IMPACT-LEDGER.md` line 43 has the current figures ("17 requirements and 68 scenarios, and PWB-REQ-001 now carries six scenarios"). Round 6 did not raise this residual, and the sign-off change reads it ("Residuals the sign-off change must carry"). Add a dated mark with 68 and 6, or cite the ledger row.

**Note 3 — Two cycle-5 wordings are guarded only by the manifest or dependency digest** (note)

[Observed, scratch mutants]
- Rewriting decision 13's "(inside a sentence passes), and which tokens a served locator holds" to "(inside a sentence fails)" gives **0** structure findings. `DESIGN_PHRASES` guards only "…Two gaps stay open and are stated in the requirement". So the design's statement of *which* gaps, and of their polarity, is unguarded.
- Widening scenario 5's WHEN to "outside every label unit or citation" gives only the `GOVERNING-DEPENDENCIES` digest finding.

Both would be caught by `--check`'s manifest comparison until the next `--write`. The delta claims only that "The six wordings the reviewer deleted … are in `REQUIRED_ONCE`", which is accurate, so this is round-6 Note 1's class at small scale, not an overclaim.

Counts: 0 blocking, 2 revise (Findings 1–2), 3 notes (1–3).
