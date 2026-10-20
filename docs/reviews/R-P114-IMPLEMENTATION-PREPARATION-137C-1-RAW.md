# P-114 machine-ceiling installation — preliminary engineering-plan review

Review class: preliminary plan coverage; no final implementation was released.
Reviewed plan: `/home/tze/.cache/syzygy-59s5-implementation-2026-10-20/PREPARATION.md`
Plan SHA-256: `e6d554fd667ac10767711da32bb5fc3e1f5987a9922245ede9e97f5667231d3e`
Frozen governing/source commit: `137c327de1310cfffbec655f0cac14c542eb5aa9`
Proposal review subject: `7d7c3a3e8a68764f987aabd80d09d9c5963d7475`
Reported main baseline: `dd520e8dd2e857814d9cf5ab1ac55eb79b83da33`
Assessment: preliminary plan needs the bounded test-discovery correction below.
Overall merge verdict: WITHHELD — final frozen implementation and its gates are not the subject of this review.

[Observed] I reviewed the frozen preparation plan, the four named package prose inputs, round-2 raw, the three named owner directions, RFC3-16(b)/(c), applicable doctrine/craft policies, and the recorder/gate/history predicates the plan names. Tracked sources were read through the frozen commit, not P-110's mutable code. The retained eight-file proposal inventory compares the six original package artifacts, builder and incident JSON between the reviewed proposal commit and frozen governing commit: eight of eight SHA-256 comparisons and eight of eight Git-blob comparisons agree. That population does not include the post-review round-2 disposition as a reviewed source file.

## Finding 1 — Version-tag discovery cannot reach the planned positive authority arm (Important)

[Observed] `PREPARATION.md:95` currently describes the `governance-inputs.test.ts` change as registry act/tag/target literals and case description. The same plan requires actual resolved-tag, state-(1) admission at lines 204–211 and 273–276. The frozen test's `localTagsPresent()` at `apps/three-surface-poc/src/governance-inputs.test.ts:361–366` enumerates only:

```text
git tag --list pwb-*-signed-*
```

The approved tag is `pwb-registry-machine-ceiling-amendment-v1.0`. It does not match that selector. A disposable bare-Git fixture containing the approved ref and two ordinary signed refs reproduces the omission: the filtered listing returns only the two signed refs; an unfiltered listing and an exact `show-ref --verify` both return the approved ref. Python's independent `fnmatch.fnmatchcase` also returns false for the approved tag and frozen selector. Exact input, output and source identities are retained in `preliminary-probes.json`; the script used is `preliminary_probes.py`. No real repository refs were changed.

[Inferred] Updating the test's expected registry tag literal while retaining this helper permanently selects the untagged branch. With an otherwise valid installed/tagged transaction, the evaluator can admit while that branch still asserts `evaluation.admits === false` and `reads === 0` at lines 427–441. An untagged passing run can therefore precede a deterministic failure only when the actual approved tag is present. This prevents the plan's required tagged positive proof from being represented correctly.

Governing basis: the install direction lines 53–59 requires distinct full-authority evaluation and the named version tag on the main commit carrying the record. Scope A item 2 states, “A sign-off binds a git tag naming a `major.minor` sign-off version of the package.” The round-2 disposition note 2 requires separately exercising “full authority evaluation against the signed entry.” Canonical test-rigor rule 1 requires tests to pin observable outcomes; rule 3 makes invalid/missing-state branches first-class.

Required bounded correction: add tag discovery to this already authorized test successor, resolving the exact expected refs or enumerating without the obsolete signed-tag restriction. Prove that the approved version tag reaches the positive branch, and that an actually missing required tag still reaches the fail-closed branch. Preserve exact-record-blob validation in the production reader. Keep synthetic, untagged and actual-main-tagged evidence distinct. This is within Ask 2 item 3 and the plan's existing test file; it needs no new owner decision, tag spelling or implementation scope.

## Coverage of the other requested seams

[Inferred] The following engineering predicates are represented in the plan. This is a coverage assessment, not an assertion that unwritten code implements them or that a gate passed.

| Focus | Plan coverage | Frozen basis / final proof obligation |
|---|---|---|
| Actual paired approval | Lines 34–36, 143–155, 179 and 182 preserve the actual question/reply, canonical direction, exact package/version and both asks. | Install direction lines 16–29 and 41–51 records the attended Codex reply `yes, approve both`. Derive the machine phrase while preserving those exact owner words; do not copy the v4 renderer's Claude/variant ceremony. RFC3-16(c) preserves the human act and exact scope; the owner answer proves no code result. |
| Exact row and one leaf | Lines 72–81, 92, 174–177 and 220–226 require frozen files, exact manifest-row population/path, independent byte/JSON proof, exact predecessor and duplicate-key/sibling negatives. | Package delta lines 60–62: exactly one literal/line and parsed leaf changes. RFC3-16(b) item 3: “approving a path never approves future content at that path.” The eight-file frozen comparison is retained; no installed-successor claim follows from it. |
| Frozen note adapter | Lines 164–178 preserve the exact round-2 disposition, its raw reference and note IDs 1–3 separately from the eight reviewed files. | Frozen `record_versioned_signoff.py:981–997` requires a literal `Reviewed record:` line absent from the retained numbered disposition. A bounded adapter is necessary; weakening the generic validator or editing the reviewed source is not. |
| Predecessor and single act | Lines 157–162 and 176–184 require the exact act-B argument, identity/date, one record/block, unapplied state, UTC recording instant and deterministic regeneration. | RFC3-16(b) items 2–8. Act B is a dated historical predecessor. See compatibility note 1 below; do not fabricate a predecessor instant. |
| Atomic failure | Lines 157–162, 183 and 194–202 require preflight construction plus validation/write-stage fault injection and before/after hashes. | Frozen v4 `do_record():502–525` is a structural precedent with separate writes, not proof of atomic failure handling. The P-114 requirement must be verified by injected write failures at the transaction seam; code and rollback behavior remain Unknown. |
| Four named historical successors | Lines 99–102, 119–139, 185 and 227–231 require only this performed row/record/patch, strict negatives and separate policy coverage. | Frozen currency `act_bytes():144–150` already delegates to re-pin `base_bytes()`. Re-pin `subject_at_act():257–277` recovers later subjects before `base_bytes():280–296` reverses its own patch. The currency recorder uses `act_bytes()`; the re-pin recorder's applied `validate_artifact():201–207` currently uses the live subject and must recover its exact historical subject. Keep one interpretation of the chain. |
| Static scanner versus runtime | Lines 224–245 distinguish frozen builder checks from evaluated TypeScript parity, exact recorder validation and real authority. | Round-2 raw finding 2 gives the arithmetic-expression, empty-record/identity and wrong-target counterexamples. The plan explicitly carries those counterexamples to the appropriate executing gates rather than editing the frozen scanner or adding a TypeScript parser. |
| Fail-closed tag/digest/target | Lines 182, 185, 204–211 and 273–276 require exact record/identity/type/tag/anchors, absent A1, registry-only supersession and actual tag-record agreement. | Authority evaluator lines 438–444 rejects wrong digest; 480–494 rejects missing/wrong supersession; 536–540 requires explicit state (1)/absent A1; 565–571 rejects an unresolved recording tag. Finding 1 corrects the test's discovery of the approved tag. |
| Shared WIP and final evidence | Lines 62–71, 227–231 and 264–283 hold execution for lead release, preserve P-110 policy fields, refresh the canonical battery and require a committed clean-clone run with actual denominators. | Install direction lines 64–67 serializes the installs and confines P-114 to registry authority. Retained warnings, skips, test delta and risk-floor declaration must accompany the eventual exact-head report under CC-BAR-2 and CC-TEST-2; this preliminary review establishes none of those gate outcomes. |

## Compatibility notes for implementation, not findings on unwritten code

1. [Observed] The frozen act-B predecessor is 101 lines and carries `Date: 2026-10-02`, with no `Recorded at (UTC):` field. Both an anchored regex and a literal line-prefix enumeration over those 101 lines agree. By contrast the frozen v4 recorder's `validate():256–258` requires a predecessor UTC instant. [Inferred] Apply the plan's “after predecessor” rule using the actual date precision available in act B; do not copy a mandatory nonexistent timestamp or manufacture one. The new record's own recording instant can still be strict UTC and on its actual recording date, separately preserving the owner-answer date.
2. [Observed] The frozen authority test's `EVALUATION_INSTANT` is `2026-10-08T00:00:00Z` at line 35. Authority evaluation rejects an act dated after the evaluation date at `body-read-authority.ts:454–460`. [Inferred] Reconcile this test instant with the post-P-110 final base and actual P-114 act date. P-110 may already repair it; do not independently overwrite that lane's change. This is a final exact-head check, not a reason to amend the approved package or ask the owner again.
3. [Observed] The frozen parser recognizes the phrase `explicitly selected` in the provenance trailer, while the v4 renderer writes `explicitly given`. The parent reports P-110's affirmative-grammar correction is in progress; that mutable code was not inspected. [Inferred] P-114 should reuse the released, tested affirmative grammar, preserve the actual free-form owner reply, and verify the rendered record through the real parser/evaluator. Negated or quoted selection text must not become authority. No ceremony change or generic parser expansion is proposed by this review.

## Retained scope and disposition

[Observed] This review wrote only outside-repository cache artifacts, performed frozen-source reads and a disposable bare-Git selector fixture. It ran no builder/recorder/install, Vitest suite, canonical battery, daemon or provider request, read no Butlers body, changed no repository file, and made no Beads, main/tag or external application mutation. The source plan snapshot is `PREPARATION-SUBJECT-RAW.md`; the probe result is `preliminary-probes.json`; the exact probe script is `preliminary_probes.py`.

[Inferred] Finding 1 is an in-scope engineering-plan correction. The remaining inspected focus areas have explicit planned acceptance predicates. No additional owner question follows from this review. Risk floors touched by the proposed transaction include sign-off, evidence, security and truth; the eventual implementation record and independent review must confirm their treatment under CC-BAR-2/5.

[Unknown] Final post-P-110 base/head, actual recorder code, emitted act bytes and recording instant, tag target, transaction fault-injection outcomes, runtime parity/authority, clean-clone battery/CI and private size measurements are not established here. Overall merge verdict remains WITHHELD. This reviewer holds for a separately released final frozen head.
