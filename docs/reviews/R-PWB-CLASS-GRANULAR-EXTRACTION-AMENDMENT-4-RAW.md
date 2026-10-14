# Review round 4 — PWB class-granular extraction amendment (M15)
Reviewed commit: c88a621f483b8a702c15b3bcb6f894252a9b0af5
Manifest SHA-256: 4d398a75284cf1dd56d6f0e3a71af68f9daacfea6457b609ff5d319b10518be2
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: a fresh-context agent that did not draft this package. Brief:
`.syzygy/governance/contracts/candidates/pwb-class-granular-extraction-amendment/REVIEW-BRIEF.md`,
including §"Round 4". As that section directs, I read the round-3 raw
(`docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-3-RAW.md`) and
`ROUND-3-DISPOSITIONS.md` to check the repairs. I did not read the round-1
or round-2 raws or dispositions.

Manifest digest: [Observed] `git show c88a621f…:<manifest path> | sha256sum`
gives the value on line 3. `sha256sum` over the file in a fresh clone at that
commit gives the same value.

## Checks run

All checks ran in a fresh `git clone --no-hardlinks`, detached at `c88a621f`
(rule 7). [Observed] at that commit:

- `build_pwb_class_granular_extraction_amendment.py --check`: "class-granular candidate matches 11 proposed subjects (5 patched); 17 requirements, 56 scenarios; structure, regeneration, contract coverage, sibling classification and pending-patch order verify".
- `--selftest`: "51 structure mutants, a manifest row, a contract-coverage count, patch drift, an unclassified sibling, the pending patch population, and divergent and failing application orders all fail closed on their own predicates".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL; PASS". R6 is WARN, report-only: two stale pins, attributed to `syzygy-2g0d`.
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)". A grep over `^(FAIL|OK|WARN)` gives 53 lines, and none is FAIL.
- `build_pwb_release_label_amendment.py --check` **fails**: "GOVERNING-DEPENDENCIES.md.patch does not apply … GOVERNING-DEPENDENCIES.md:9". `build_pwb_opening_index_amendment.py --check` and `build_pwb_accessible_name_amendment.py --check` fail with the same finding. See Note 4.
- Signed scenario count, second method: `grep -c -F "#### Scenario:"` over the signed PWB `spec.md` gives 52. The patch adds four `#### Scenario:` headings, so the proposed spec has 56. That equals the builder's figure and the delta's corrected residual 2 (17 requirements, 56 scenarios, PWB-REQ-002 at 6 + 4 = 10).
- Quotation fidelity, my own script: every one of the 161 non-blank added lines of `proposed/spec.md.patch` occurs verbatim, whitespace-normalized, in `SEMANTIC-DELTA.md` (0 missing).
- Selftest assertions: each mutant now expects an exact finding, or a long specific prefix, through `_once` / `_lacks` (lines 655, 660). The loop matches with `startswith(expected)`, and for `_once` / `_lacks` the expected string is the whole finding. Among the seven required-phrase tuples (37 reader, 33 PWB-REQ-002, 9 design, and others), no two phrases share the 60-character prefix that `_once` truncates to. So no exact-finding assertion can be satisfied by a neighbouring phrase.
- Rule-6 probe, my own script, outside the clone. Six extra mutants over the proposed spec, each run through `structure_findings`:
  - "pillar-index precedence weakened", "root-index precedence dropped", "scenario pillar-index limb dropped", "case line dropped" and "verification case precedence dropped" each fail on their own required phrase.
  - "scenario baseline limb flipped" changes `baseline-spec-tree` to `pillar-named-file` in scenario 4's THEN. It fails only on the generic "proposed GOVERNING-DEPENDENCIES does not name the proposed spec digest" (Note 2).
- Code claims, re-read at `c88a621f`. [Observed] in `project-shape-manifest.ts`:
  - `PILLAR_KEYS` is at line 47 and `SOURCE_RULES` at line 71, with the five names.
  - `addSource` keeps the first registration (line 393).
  - The comment "Rule 1 — the root index …" is at line 403, and the root index is registered at line 405, before any other source.
  - The comment "whoever names it" is at line 473. Line 478 skips a named blob only for `BASELINE_SPEC` or `ROSTER_BUTLER`, so a pillar-named roster `MANIFESTO.md` stays `pillar-named-file`.
  - Lines 500–503 register an unnamed roster `MANIFESTO.md` as `roster-tree`.
  - Pillars are processed in `PILLAR_KEYS` order, each pillar's index and then its named files. So a later pillar's index that an earlier pillar's index names is first registered as `pillar-named-file`, and its own `pillar-index` add is discarded. That is the one difference the delta names.
  - `git diff --stat 8f1fbec7 c88a621f` over both code files is empty.
  - `git grep -F pathPattern c88a621f -- packages` returns nothing, as the delta says.

## Criterion summary

1. **Ruling content.** P-82's four answers are carried. The drafter's readings are put to the owner as Q2–Q4, Q6, Q7 and the new Q8. Met.
2. **The specification bar.**
   - The order for a source more than one rule admits has its SHALL text (the reader-definition bullet at patch line 15), an oracle limb ("by the stated order …", line 164), a falsifier limb (line 179) and a scenario ("A source two rules admit carries one rule name", line 225).
   - I traced each source type the round-4 addition lists:
     - the root index: `root-index`, whatever else admits it;
     - a pillar's index file named by another index: `pillar-index`;
     - a pillar-named baseline spec: `baseline-spec-tree`;
     - a pillar-named roster `butler.toml`: `roster-tree`;
     - a pillar-named roster `MANIFESTO.md`: `pillar-named-file`;
     - an unnamed roster `MANIFESTO.md`: `roster-tree`;
     - a source two tree populations of one loaded profile admit: the first one the profile declares.
   - Each resolves to one name without judgment, because "decided in this order" makes the list a precedence.
   - Scenario coverage of the order is partial (Note 1), and one edge in the root-index text needs a reading (Note 3). Met, with notes.
3. **Category rule and exactness reach.** No regression from round 3. Met.
4. **Signed bytes.** The builder's predicates pass, and the selftest mutants fail on them. Met.
5. **Honest claims.**
   - The code claims for the order hold at the reviewed commit, and the nested-pillar exception is correctly identified and labelled [Inferred].
   - Whether Butlers has nested roots is labelled [Unknown].
   - Packet Q8 puts the code-divergent case and the loaded-profile clauses fairly. Both arms state their cost, and the recommended arm discloses that the build changes code for nested roots.
   - The stale attributions found in round 3 are marked at the sentence, with the old text kept. Met.
6. **Mechanics.** This package's `--check` and `--selftest` pass, and the totals are computed (28 + 6 + 0 = 34). The release-label `--check` cannot pass at this commit, for a reason outside this package (Note 4).
7. **Plain language.** The packet's summary and Q8 restate the change clearly. Met.

## Round-3 findings, checked against the bytes

- **Finding 1 (revise) — repaired.** The order is stated in the reader definitions, the oracle, the falsifier, the Case line and a new scenario, and in the design note. It is put to the owner as Q8. It covers the `MANIFESTO.md` and root-index cases the raw named, and it says the code's `MANIFESTO.md` behaviour already matches. The selftest has mutants for each clause, the oracle, the falsifier, the scenario heading, the `MANIFESTO.md` limb and the design sentence.
- **Finding 2 (note) — repaired.** The five mutants now assert exact findings, and the two unguarded round-3 phrases have mutants (lines 794, 798).
- **Finding 3 (note) — repaired.** Residual 4 and the ledger's §"Registry entry and policy" are marked at the sentence with the `syzygy-2g0d` / P-95 attribution. This matches R6's output at this commit.
- **Finding 4 (note) — repaired.**
  - The ledger row, the ledger's collision section and the delta's "Downstream impact" now name the three pending siblings and record that P-96 is performed.
  - `PENDING_SIBLINGS` holds exactly the three (line 128), and the comment agrees.
  - `ORDER_POPULATION` matches.
- **Finding 5 (note) — repaired.** Scenario 3's THEN carries "and the source-path population total", with a required phrase and a mutant.

The repairs introduced no regression of rounds 1–3 that I found. The new material raises only the notes below.

## Findings

**Finding 1 — Scenario 4 exercises the built-in tree-rule cases only; the clause the code violates has no scenario that sets it up** (note)

- Scenario 4's WHEN is "a pillar's index names a baseline spec, a roster `butler.toml` and that roster directory's `MANIFESTO.md`".
- Its last AND, "each pillar's index file `pillar-index`, whichever index also names them", asserts the nested-pillar clause. But nothing in the WHEN makes any index name another pillar's index file, so the assertion holds without that case being exercised.
- That clause is exactly the one case where [Observed] today's code differs from the text (delta §3, packet Q8). The Verification Case line (patch line 142–144) also omits it.
- The loaded-profile clauses (a profile tree population over a pillar-named file, and two populations of one profile) also have no scenario.
- The oracle limb ("by the stated order") and the falsifier limb do reach every clause, so the obligation stays decidable and falsifiable. But a test author working from the scenarios would not build the divergent fixture.
- Read literally, the WHEN also has one index naming both an `openspec/specs/…` file and a `roster/…` file. Under the signed within-root restriction, that needs a pillar root that encloses both top-level directories. The delta's own account uses two pillars, one at `openspec/` and one at `roster/`.
- Suggested:
  - Say "pillar indexes name" in the WHEN.
  - Add a nested-root fixture to the WHEN, or as its own scenario, so that the `pillar-index` AND is exercised.

**Finding 2 — The structure predicate does not guard scenario 4's THEN outcomes** (note)

- [Observed] My mutant "scenario baseline limb flipped" rewrites "the baseline spec is named `baseline-spec-tree`" to name `pillar-named-file`. That inverts the precedence the scenario asserts.
- It yields only the generic GOVERNING-digest finding that every spec byte change trips. No required phrase covers that THEN line or the `butler.toml` `roster-tree` half.
- `--check` would still fail on such an edit through manifest regeneration, so no drift can land silently.
- But the selftest's own-predicate claim does not extend to this limb. The `MANIFESTO.md` limb and the last AND are guarded, which makes the omission look accidental.
- Suggested: add the THEN line to `REQ_REQUIRED_ONCE`, with a mutant.

**Finding 3 — "leaves that pillar's index and named files unadmitted" reads absolute against the new precedence for nested roots** (note)

- The reader definitions say: "a pillar root it does not name unambiguously leaves that pillar's index and named files unadmitted". The new order says: "any other file a pillar's index names … is `pillar-named-file`".
- Take nested roots where the inner pillar is `not-named-in-root-index` or `named-root-ambiguous`, and the outer pillar's index names the inner `README.md`. One sentence says that file is unadmitted, and the other says it is admitted under rule 2.
- [Observed] The code admits it as `pillar-named-file` (the loop at lines 470–487 adds every named path not owned by rules 3 and 4, `rule: 'pillar-named-file'` at line 481).
- The natural reading, "unadmitted *as that pillar's*", agrees with the code and with the order's clause 2. That clause applies only to the index of a pillar root the root index names. So an assessor can decide it.
- The case needs the same nested roots Q8 already puts to the owner. Suggested: scope the sentence ("leaves … unadmitted by the first and second rules for that pillar"), or name the case in Q8.

**Finding 4 — The release-label `--check` (criterion 6) fails at this commit for a sibling-lane reason; composition is verified only for the spec patches** (note)

- [Observed] `build_pwb_release_label_amendment.py --check` fails because its own `GOVERNING-DEPENDENCIES.md.patch` no longer applies to the signed bytes that the P-96 sign-off (`7f43802f`) moved. The P-98 and P-99 builders fail identically.
- This package's own dependency patch was regenerated over those bytes and applies. The failure is in the siblings' lanes, not this package.
- Composition I could verify: this builder's all-orders check applies its spec patch and the three pending siblings' spec patches in every order, and gets one result.
- Composition I could not verify at this commit:
  - that the sibling builders still pass with this package listed;
  - the combined `GOVERNING-DEPENDENCIES.md`;
  - the design-decision-12 and capability-row-34 collision with P-85, which packet Q5 already routes to regeneration and re-review.
- The criterion 6 bullet "`build_pwb_release_label_amendment.py --check` still passes" therefore stays unmet until P-85's lane regenerates. Re-run it then.

Counts: 0 blocking, 0 revise-level findings, 4 notes (Findings 1–4).
