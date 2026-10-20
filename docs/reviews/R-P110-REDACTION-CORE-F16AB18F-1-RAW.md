# Preliminary implementation review — P-110 secret-redaction core
Verdict: REVISE (frozen core slice only)
Reviewed commit: `f16ab18f448ee8a443ec67b2e7cc4c6a545583f4`
Subject SHA-256: `d200ca6751ad51ce049cfc208746b57e96d5e6f65a3b578d5fb915513670d2e3` (`packages/polaris-generation-core/src/secret-redaction.ts`)

[Observed] This review is limited to the frozen core module and its tests at the commit above. Governing references: the exact installed span policy (SHA-256 `319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd`), the P-110 version-4 act already examined in the authority slice, RFC5-17, the round-4 raw and dispositions, the builder's body/whole fixtures and reference oracle, and the impact ledger's work-bound obligation. Source snapshots and their digests are enumerated in `subject-manifest.json` (SHA-256 `3fac01c3e3e1c3fa2b6360bad209a141abf99bcbd077ce71bb1bae66d7d53c3f`). Each snapshot was read with `git show <reviewed-commit>:<path>`. No mutable implementation file, observed repository body, provider or daemon was read or exercised. Repository `AGENTS.md` and requested skills were procedural context. No repository, Beads or external-review mutation was made.

[Observed] This is targeted evidence, not a full implementation, clone-battery or CI result. Consumer transport, independently revalidated Git identity, retained-corpus trust, exported/provider/render paths and the final act chain remain outside this slice. The full final review has not been released.

## Strengths and checked behavior

[Observed] The match loop tries each UTF-16 start offset with a sticky regex, so the hidden cross-line password match in the overlapping fixture is present alongside the earlier secret match. The core excludes non-redacted classes, no-rule bodies, whole-artifact detectors, anywhere header fragments and per-line header patterns before calling the every-offset scan. The explicit probe replaces `all()` with a throwing guard for those early paths and for a clean body.

[Observed] The complete builder population of 16 body fixtures and 3 whole-file fixtures matched both the builder's stated expectations and its Python reference oracle when the exact policy and frozen core were executed outside the checkout. These include the re-screen case where emptied lines create a new match, the overlapping match, multiline assignment, private-key and known-token cases, and the round-4 anywhere-header cases. A separate tab-indented six-dash header probe verified the per-line rule without relying on the anywhere fragments.

[Observed] Successful-work saturation works: `token=` repeated 4,000 times excludes whole after 9 matches totaling 215,784 matched code units over a 24,000-unit body. The match-count boundary also works: exactly 10,000 short matches remain placeable, and 10,001 excludes whole with `match-limit`.

[Observed] A literal mixed CR/LF/CRLF and Unicode fixture preserved original byte offsets `[0, 4, 9, 24, 30]` and complete-body length 34 while withholding lines 2–4. The retained line array preserved its original boundaries even where emptying lines makes terminators adjacent. Marker runs disclosed the total withheld count, kept the last run terminator (or no final terminator), and included none of the synthetic token. A further 256 deterministic generated cases checked guards at both edges, two match locations, Unicode bytes, mixed terminators, byte offsets, retained line contents and marker secrecy against independently constructed original line arrays.

[Observed] The correctness runner has 32 explicit cases, one of which contains those 256 generated cases; its 32 outcomes match expectations. Nine cache-only mutants were killed, each after its unmutated control passed: overlap skipping, removed guards, removed fragment check, removed line check, removed re-screen, removed match-count bound, removed successful-work bound, UTF-16 rather than UTF-8 byte offsets, and a wrong marker total. `redaction-mutations.json` records the subject commit, subject digest and every exact old/new fragment, so the mutants are reproducible. A separate Python audit confirmed the result denominators and enumerated the mutant IDs.

[Observed] The frozen diff adds this module and a new 156-line test file. Its declared net test delta is +24 cases: 11 direct declarations and parameterized tables of 2 and 11 rows. The existing tests cover successful-match saturation, but neither saturation fixture exercises expensive failed URL matching. This count is a source enumeration, not a report of running the repository Vitest suite.

## Important — unsuccessful URL work bypasses both scan budgets

[Observed] `secret-redaction.ts:138–165` loops over each offset and runs the declared sticky regex synchronously. Its `take()` callback charges only successful matches: line 161 adds their lengths, and line 162 limits their count or summed lengths. Failed attempts do not call `take()` and cannot trip either bound. Retained-text re-screening at line 227 uses an ordinary synchronous regex search with the same failed-search cost.

[Observed] Exact synthetic input, with N repetitions:

```javascript
"token=abcdefgh\nsafe\nsafe\nhttps://" + "a:".repeat(N) + "end\n"
```

The first detector search finds the 14-code-unit assignment immediately. The URL suffix has many possible colon partitions but no `@`, so the URL detector fails after expensive backtracking. For N = 2,000 / 4,000 / 8,000 / 16,000, the every-offset scan took approximately 10 / 34 / 131 / 488 ms; its returned successful-match count was 1, summed successful length 14, and `limited` remained false. Full `redactBody` took approximately 17 / 62 / 255 / 1,005 ms and returned `redacted` in those runs. At N = 32,000 (64,037 UTF-8 bytes), `all()` took approximately 2,070 ms and still reported `limited:false`; an external five-second cap ended the combined scan/redaction probe during redaction. An independent direct-redaction run then completed in 4408.96 ms and returned `redacted`, withheld `[1,2]`, without a resource-limit exclusion. Initial first-match search for this input was approximately 0.25 ms. These are measurements on this host, not timing thresholds prescribed by the policy.

[Observed] The governing impact ledger, `IMPACT-LEDGER.md:80–82`, specifically identifies `credential-bearing-url` backtracking over a long delimiter-free run and requires that “the install bounds the scan within the resource limits and treats a breach as a whole-file exclusion.” The module's own comment acknowledges that individual searches retain the declared detectors' costs, but the implemented success-only budgets do not cover the failed-search path that the ledger calls out.

[Inferred] This leaves the resource-bound installation obligation incomplete and permits a small synthetic document to block the synchronous screening path for seconds without approaching either budget. The approximately fourfold time growth under doubled suffix lengths supports the ledger's quadratic-cost concern. The failure is in matching-work accounting; it is not a newly detected secret format or an objection to the disclosed unmatched-secret residual. It violates engineering-bar's behavior/failure-path criteria and test-rigor expectations 2–3 for the bounded-work acceptance condition.

[Inferred] Bound unsuccessful matching work before an individual synchronous regex operation can overrun the deterministic scan budget. An equivalent bounded matcher or a conservative preflight refusal can preserve the approved detectors and every-offset semantics; the implementation owner should choose the narrow fix. Add a behavioral regression for this failed-URL family alongside the two successful saturation fixtures, proving a resource breach excludes whole. A wall-clock-only timeout around the existing synchronous loop cannot interrupt an already running regex. No policy, detector, frozen subject, scope or contract amendment is required to complete this existing obligation.

## Evidence and preliminary assessment

[Observed] Runtime: Node `v24.6.0`. The loader strips types from the frozen module using Node's built-in type stripper; builder fixtures were evaluated by exact frozen Python builder snapshots using only standard-library dependencies. Every target body is synthetic.

- [Observed] Correctness runner: `probe-redaction-correctness.mjs`, SHA-256 `843284452c5f117b59191fed5ed00c059d1f4011e88c75e8916cee2ffefa69c0`; results: `redaction-correctness.json`, SHA-256 `7a33db8b0784598727c5092ca745f821600205803a0489a2df36e558bcca851f`.
- [Observed] Mutation runner: `probe-redaction-mutations.mjs`, SHA-256 `a3ef45accd9ac819df80693d9e687cbf217f0200d0372ac8f37d1814756707f6`; results: `redaction-mutations.json`, SHA-256 `ff0e2393bf223bd5fd60e5008f7dd5a1f97dcb3c6cf8859f9f6bb4b7c80a27c2`.
- [Observed] Failed-search reproducer: `probe-url-work.mjs`, SHA-256 `29df66e2481c2f5bf83687fb02fbe1860e404e9b7745e5ea87e57761038f8680`; captured work-series results: `failed-url-work.json`, SHA-256 `de4886f70e36fc682169eb73b96ccb14afde82931d80e6cff5a3b735c910f222`; direct-redaction command and exact output: `failed-url-direct-redaction.json`, SHA-256 `9044985d056b2d9c962f0387319ee05b4cd49bca8fa4119e3dfe3b2a6ca24593`.
- [Observed] Shared snapshot loader: `load-redaction.mjs`, SHA-256 `aa7c9cabd33c39e6369b08a80a2d16dcf4e4e36cfc8ed73aa1ce228d2320aff1`; builder fixture values: `builder-fixtures.json`, SHA-256 `b8b496e5e5132f45cedb66dc1a1a898293af87e27cdfe063fc0352dfad94a3c2`. Output and result records are copied verbatim into `R-P110-REDACTION-CORE-PROBES-F16AB18F-1-RAW.md`.

[Inferred] Preliminary frozen-core verdict: REVISE for the failed-search work bound. The enumerated correctness and mutation probes above support the checked redaction behavior; they do not establish the complete implementation. Overall implementation and merge assessment: NOT ISSUED. Hold for the final frozen head and evidence release.
