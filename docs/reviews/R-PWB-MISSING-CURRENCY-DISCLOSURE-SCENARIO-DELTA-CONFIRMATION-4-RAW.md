# Fresh-context review - PWB missing-currency disclosure scenario (P-69 Q7a), confirmation round 4
Reviewed commit: 12abd623a63c5f6722f3519b11cf8af8e2a4bac2
Manifest SHA-256: c6ce6b4145c934ca6717f661ab8c0f542c60deeb089924996630993a30f48227
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: CC-REV-1 fresh context. No earlier raw for this package was read.
Sign-off is by version (OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md), so the manifest digest above is informational. It is the sha256sum of the manifest file at the reviewed commit and equals the digest the owner packet prints.

Summary. Every remaining item is a note. I found no defect that makes the normative text wrong or unsafe, and no blocking or revise item. The notes are a false ledger sentence about the successor chain (Finding 1), a delta block that mis-quotes the patch (Finding 2), a parity reading that rests on an [Inferred] delta sentence and not on spec text (Finding 3), builder predicates that are weaker than the mutants the brief lists (Finding 4), stale phrase wording in two package files (Finding 5), and an unstated primary-reason precedence (Finding 6).

## Classification

[Observed] Normative, concurring with the draft. The scenario changes what a compliant renderer must do. Before it, PWB-REQ-007 admitted no exception to "freshness" on every claim, so a renderer had to put one of four values on an unbounded claim. After it, that same renderer is non-compliant if it does so, and a renderer that omits freshness for the condition becomes compliant. Compliance moves in both directions, so Clarifying cannot hold. I found no argument that the ruling's "clarification scenario" label controls the class.

## Method and denominators

All commands ran against 12abd62. Mutation work was done in a `git archive` copy under the session scratchpad. The detached worktree /tmp/mc-review3 was removed afterwards.

1. `build_pwb_missing_currency_disclosure_scenario.py --check` passed: 11 subjects, 6 patched, 5 unchanged.
2. `--selftest` passed. `--diff` prints the six patches.
3. I applied all six patches with `git apply` in the archive copy, ran `sha256sum` over the 11 subject files, and diffed the result against the manifest's 11 rows. Result: identical, 11 of 11.
4. The five unpatched rows are byte-identical to base, by construction of the check "declared patched subject is unchanged". The patch population is exactly the six `.patch` files.
5. I re-ran the ledger's six published `re` predicates over `git ls-tree -r -z` at 49ef8fd.
   - Denominator: 1,772 tracked files, 4 UTF-8 decode skips. The four skips are exactly the four PNG files the ledger names.
   - PWB-REQ-007: 119 files, 530 occurrences. `git grep -F -l` agrees at 119.
   - Continuation form: 7 files, 8 occurrences. The files are the registry delta, its raw, the P2-7 mutation record, M13:1 hit, M14:1 hit, the exact-head packet, and the M13 raw with 2 hits.
   - spec.md path: 97 files, 199 occurrences.
   - GOVERNING-DEPENDENCIES path: 24 files, 41 occurrences.
   - `no-currency-bound-declared`: 65 files, 98 occurrences.
   - RFC2-10: 96 files, 391 occurrences.
   - All six rows reproduce exactly.
6. Contract gaps.
   - The repair-delta patch flips exactly RFC6-14.r1, RFC6-14.r3, RFC6-17.r1, RFC7-16.r1 and RFC7-33.r1 to `unknown-uncovered`.
   - The declared totals move from 61 covered / 16 Unknown to 56 / 21. CONTRACT-COVERAGE moves from 137 / 237 to 132 / 242. The denominator stays 622, and 248 are believed not applicable.
   - I swept the remaining 11 rows in the post-apply repair delta that still read `covered:PWB-REQ-007`. They are RFC1-19.r1/r2, RFC1-24.r1/r2, RFC2-9.r1, RFC2-24.r1, RFC2-25.r1, RFC6-14.r2, RFC6-17.r3, RFC7-16.r2 and RFC7-16.r4.
   - None of them requires a freshness value, so none is falsified by the exception.
   - RFC6-22.c4, RFC6-23.c3 and RFC1-18.r2 were already `unknown-uncovered` before this package.
   - I found no omitted consequence and no row that wrongly remains covered. Criterion 9 holds.
7. Registry act `.18` was treated as performed, not as a candidate.
   - I read the registry JSON and found 13 `currencyBounds` rows and a `currencyBoundSemantics` block.
   - No sentence in the package calls `.18` a candidate or parked.
   - No numeric bound is repeated in the package; the grep for duration numerals returned nothing.
   - The scenario is scoped to a class with no row, or a declaration lacking effective owner-act provenance. Criterion 12 holds.
8. `python3 scripts/check_governance.py` gave 31 OK, 21 WARN, 0 FAIL. `--selftest` gave 352 fixtures, 0 failing.
9. Quotations checked at definition sites.
   - PWB-REQ-007 text and falsifier.
   - RFC2-9 and RFC2-10, including "no implementation may mint, spell, or force-fit".
   - The RFC2-10 sentence "A condition genuinely outside the four is disclosed as a fact of the render".
   - The RFC2-24 row-3 route and the RFC2-24 "fact of the render - named, expandable, routed" passage.
   - CAP1-REQ-062 and the P-69 ruling row.
   - All match. The "no claim renders the disclosure route" gate wording is quoted faithfully.

Mutations run on the scenario predicate (`scenario_findings`), importing the builder and mutating the proposed spec bytes:

| Mutant | Result |
|---|---|
| Builder's own twelve selftest mutants | Each fails on its named predicate |
| `check` with 132 → 133 in the CONTRACT-COVERAGE patch | Fails on the regeneration predicate |
| Dependency digest altered | Fails on the dependency-regeneration predicate |
| Manifest byte altered | Fails on the manifest predicate |
| Manifest rows swapped | Fails on the path-order predicate |
| Spec patch context line altered | "does not apply" |
| `proposal.md.patch` deleted | Fails on patch population and on the proposal exception |
| Repair delta RFC6-17.r1 restored to covered | Fails on the gap predicate |
| Unknown→Verified in THEN | Passes (Finding 4) |
| "as-of instant" removed | Passes (Finding 4) |
| "expandable" removed | Passes (Finding 4) |
| "every other tuple obligation remains" → "may lapse" | Passes (Finding 4) |
| "never shows ... as zero" with "or may show them as zero" appended | Passes (Finding 4) |
| "together equal its membership" → "membership or less" | Passes (Finding 4) |

## Criteria results

- **Criterion 1, quotation fidelity.** The source quotes in the delta are faithful. Finding 2 concerns the delta's own proposed-text block.
- **Criterion 2, classification.** Normative, as above.
- **Criterion 3, exact missing-bound arm.** The WHEN covers both an absent declaration and one without effective owner-act provenance. The scenario keeps the RFC2-9 contradiction route beside the Declare route, which is faithful to RFC2-9. The composition is flagged [Inferred] in the delta (item 6) and reconciled openly.
- **Criterion 4, no fabricated freshness.** The scenario names all four values and forbids a fifth. It never calls the condition stale, broken or superseded. The delta quotes the RFC2-10 "fact of the render" clause as its authority.
- **Criterion 5, tuple preservation.** Tier, challenge state, semantic claim identity and evaluation identity are retained. Reason and route are stated. Freshness is the single stated exception.
- **Criterion 6, aggregate polarity.** The scenario states the aggregate rule outright: counts reconcile to membership, no value is derived from other members, the unbounded members are never zero, they appear only through the outside-slot disclosure, and no freshness value of the aggregate's own is minted. It is consistent with the PWB-REQ-010 opening aggregate, which defers to "as PWB-REQ-007 requires". The "for this condition only" clause covers that deferral. The RFC6-17 per-freshness-state count requirement is now `unknown-uncovered`, which is honest.
- **Criterion 7, PWB/RFC tension.** The tension between PWB-REQ-007 and RFC2-10 is surfaced openly, along with the Q7 origin. RFC2-9 and CAP1-REQ-062 are reconciled accurately, and the judge is described as carrying no freshness field.
- **Criterion 8, eleven-subject propagation.** Six rows change and five are exact. Proposal, capability coverage, repair delta, generated coverage, generated dependencies and spec all move together.
- **Criterion 9, contract gaps.** Verified above: 132 covered / 242 Unknown over 622.
- **Criterion 10, impact sweep.** All six predicates reproduce at the named baseline. The behaviour pins and the consumers match the ledger.
- **Criterion 11, composition.** The spec patch applies over the performed opening-band, render-mode and machine-view text without displacing it. The dependency patch regenerates from the proposed spec (the builder checks exact equality). The scenario mints no fifth freshness value, consistent with RFC2-10.
- **Criterion 12, `.18`.** Holds, as above.
- **Criterion 13, builder.** Every mutant the brief lists fails. Finding 4 is a note about wider mutants.
- **Criterion 14, governance hygiene.** One exception: Finding 1.
- **Criterion 15, authority boundary.** Nothing signs, adopts, authors a recorder or act record, selects performance order, authorizes implementation or says the route renders now. The one deviation is the successor-chain registration in Finding 1.
- **Criterion 16, owner packet.** The manifest digest is exact. Version-tag sign-off replaces the phrase. The `.18`, `.19` and implementation gates are named, and silence defaults to current behaviour. Finding 5 notes stale wording.

## Findings

**Finding 1 - The package says there is deliberately no successor-chain link, but the link is registered** (note)
`IMPACT-LEDGER.md:147-148` says "There is deliberately no `PWB_SUCCESSOR_CHAIN` link before the owner chooses performance order." `SEMANTIC-DELTA.md:238` says the chain link is added at adoption. `REVIEW-BRIEF.md:82-83` makes criterion 14 require "phrase/copy registration ... without a successor-chain assertion". But `scripts/check_governance.py:1679-1680` places `(PWB_MISSING_CURRENCY_LABEL, PWB_MISSING_CURRENCY_SUBJECT, PWB_MISSING_CURRENCY_ACT, PWB_MISSING_CURRENCY_SUBJECTS)` as the last element of `PWB_SUCCESSOR_CHAIN`, with the comment at 1677-1678 "the missing-currency scenario is the next candidate". Commit 6b66fe0 added it and 12abd62 did not change it. Verification rule 5 applies: a registration statement was not checked against the code. `check_governance.py` passes, so the link is inert while the act is unperformed, and it does not affect the normative text. Either the ledger sentence or the chain line should change. Which one is an owner or author choice; the AGENTS.md note says a candidate registers phrase and copy and gets its chain link with the act.

**Finding 2 - The delta's "Proposed meaning" block is not the patched scenario** (note)
`SEMANTIC-DELTA.md:96` says "The following scenario is inserted under PWB-REQ-007 immediately before ...". The quoted block (lines ~98-113) has WHEN, THEN and two ANDs. `proposed/spec.md.patch` inserts WHEN, THEN and four ANDs. The two bullets missing from the quote are the RFC2-9 contradiction-route bullet and the aggregate bullet. Items 6 and 7 of "What explicitly does NOT change" (`SEMANTIC-DELTA.md` around lines 148-170) describe both bullets, so the content is disclosed. But the block labelled as the inserted text is not the inserted text (criterion 1, rule 8). The delta should quote the patch bytes in full.

**Finding 3 - Machine-answer parity of the disclosure rests on an [Inferred] delta sentence, not on spec text** (note)
The scenario says the missing-bound disclosure is "a named, expandable fact of the render" (`spec.md.patch:+8`). Neither it nor PWB-REQ-020 says the machine answer must carry it. PWB-REQ-020's list reads "walkthrough-judgment state or disclosure". That phrase is ambiguous between disclosures in general and walkthrough disclosures. `SEMANTIC-DELTA.md` item 7 supplies the reading ("recoverable in the machine answer under PWB-REQ-020's parity obligation for disclosed facts"), and tags it [Inferred]. A renderer could arguably show the disclosure on the human surface only and still read as compliant, because the machine tuple has no freshness field to carry it and RFC6-14/RFC7-33 coverage is now `unknown-uncovered`. This is not a defect in the text as written, because the five coverage gaps are disclosed. It is a parity risk for the later implementation authorization. A one-clause scenario bullet, "and the same disclosure is recoverable in the machine answer", would remove it. It is not required for confirmation.

**Finding 4 - Builder scenario predicates are token-presence checks and pass semantically weaker mutants** (note)
`scripts/build_pwb_missing_currency_disclosure_scenario.py` `scenario_findings` (about lines 175-215) tests that fixed substrings exist in the scenario section. The brief's listed mutants all fail, but I ran six more. Five of them pass: "Unknown"→"Verified" in THEN, removing "as-of instant", removing "expandable", "every other tuple obligation remains"→"may lapse", appending "or may show them as zero", and "equal its membership"→"membership or less". The label `Unknown` and the "as-of instant" and "expandable" wording are not tokenized at all. The aggregate-own-value predicate matches the single phrase "its own freshness reads". The manifest digest still catches any byte edit, so adoption is safe. These are hardening gaps for a rule-6 sweep, not a failure of the brief's mutant list.

**Finding 5 - Stale phrase wording after the move to version-tagged sign-off** (note)
`OWNER-DECISION-PACKET.md:6` still says "The phrase and digest below are retained only so governance checks can detect drift", but the packet now has no phrase (line 53: "No phrase is typed"). `REVIEW-BRIEF.md:87` criterion 16 still asks whether "the one sign-off phrase is copyable". `OWNER-DECISION-PACKET.md:10` is dated 2026-09-22 while the body describes 2026-10-02 state. These are inert wording issues, with no effect on the normative text or the manifest.

**Finding 6 - The scenario fixes the primary reason without stating precedence against other applicable Unknown reasons** (note)
The THEN clause (`spec.md.patch:+4`) makes `no-currency-bound-declared` the primary reason whenever the class has no effective bound. RFC2-24 requires exactly one primary reason but defines no precedence rule. A claim in an unbounded class could also meet another reason, such as `excluded-content` or `unconsented-source-or-provider`. RFC2-9 itself says the class's claims render Unknown with this reason, so the scenario is consistent with the contract. It still hardens a precedence the contract leaves open. The rest of the PWB spec assigns no primary reasons, so there is no internal conflict (I grepped the spec for the spellings `excluded-content`, `source-uncaptured`, `unconsented-source`, `missing-declaration` and `missing-evidence` and got no hits; I did not sweep the other seven reason spellings). I record it only so a later implementation authorization decides precedence deliberately. No change to these bytes is requested.

## Owner-only decisions still open

None prevents exact final bytes. Finding 1 needs an author or owner choice between editing the ledger sentence and removing the chain link. Findings 2 to 6 are optional.

Per CC-REV-6 any edit to a reviewed byte retires this review, including a repair for Finding 1 or 2. The stopping rule from the owner's 2026-09-26 ruling applies: a notes-only round clears its bytes if the notes go in a sibling record, not by editing the reviewed files.
