# Round 1 dispositions — public-source screening scope, version 4

> **Candidate — binds nothing.** Raw: `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-1-RAW.md`,
> verdict line 4: `Verdict: REVISE`, over commit `676adea9`. One blocking
> finding, four revise, four notes. Each is repaired once below. Under the
> owner's stopping rule (2026-09-26) a REVISE is repaired once and reported;
> no round 2 has run, so these repaired bytes carry no confirmation and the
> packet is not offered.

| Finding | Severity | Disposition |
|---|---|---|
| 1 — `known-token-formats` matches an AWS key id, not its secret key | blocking | `known-token-formats` added to `wholeArtifactDetectors`; only `credential-assignment` and `credential-bearing-url` are redacted by line. Body fixture "AWS access-key id with its secret key" (excluded whole) and mutant "known-token-formats moved to redaction caught". Delta "Why each fail-closed choice" and the builder comment corrected |
| 2 — the non-overlapping scan hides a line-crossing match | revise | The rule now counts "every match it makes starting at any offset of the text, overlapping matches included"; the oracle scans every offset. Body fixture "hidden overlapping match" (value line withheld), predicate "a non-overlapping match set caught", and a mutant showing the plain scan leaks line 5 |
| 3 — "admitted under either rule" is false for a body with a match | revise | Delta "What it gives up" and packet "What it costs" now lead with the co-location cost. New `wholeArtifactFragments: ["-----BEGIN "]` keeps any PEM-bearing body whole, closing the reviewer's EC-key case (fixture "EC key beside a badge", predicate "a dropped PEM fragment caught"); both pages say the class is not closed |
| 4 — the requirement is REQ-polaris-generation-025 | revise | Corrected in the delta and the brief |
| 5 — the Butlers read gate break is omitted | revise | Ledger names `governance-inputs.ts` lines 76-104 as the Butlers gate and its break; packet "Order, as fact" names both gates; the four policy-path consumers and the provider egress population are listed, their breakage Unknown for the install to assess |
| 6 — whole-body digest and object id check guesses | note | The residual is now stated in `secretRedaction.withheldLines` and the delta; the digest stays because RFC5-17 requires it |
| 7 — option C's REQ-035 basis paraphrased | note | The decline row now quotes REQ-polaris-generation-035 ("draft-to-source support for every claim block") and the REQ-006 rule it keeps, and says the blocking count itself is implementation |
| 8 — two reasons wider than their sources | note | MODULES.md reason now rests on the absence of a path rule; credit names rest on RFC5-14's general definition and the `authors` precedent; `support` and `development` each get a sentence |
| 9 — marker count and regex dialect | note | Marker is one per run of withheld lines, naming the body's total count (policy and ledger agree); the ledger requires the body fixtures through the TypeScript screens because Python and JavaScript `\s` differ |

Verification after repair: the builder's `--check` passes and `--selftest`
holds 37 of 37 predicates; `scripts/check_governance.py` reports 0 FAIL.
