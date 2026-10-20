# Preliminary implementation review — P-110 authority encoding
Verdict: REVISE (preliminary slice only)
Reviewed commit: `f16ab18f448ee8a443ec67b2e7cc4c6a545583f4`
Subject SHA-256: `7306c43845369f7140cbb4cc24dbad178fbb993a2750827e4a2dea42371924af` (`packages/three-surface-poc-core/src/owner-act-record.ts`)

[Observed] Base: `dd520e8dd2e857814d9cf5ab1ac55eb79b83da33`. This review examines only the explicit-selection extraction change introduced in commit `997909214fbcaafa9dca9740d1fefdbcd1312719` and its evaluator consequence at the reviewed head. Full implementation review has not been released, and no overall merge verdict is issued. Repository `AGENTS.md` and the requested skill instructions were read for procedure. Live uncommitted implementation code and observed repository bodies were not inspected; providers and daemons were not exercised. No repository or tracker writes were made.

[Observed] Exact source subjects and SHA-256 digests are retained in `subject-manifest.json` (file SHA-256 `8d2f07a9f21bc9064a51ffef3e78540962bc3a4c25b02cc8e52e2fdad4e12286`). Snapshots were extracted with `git show <reviewed-commit>:<path>`; runtime execution used these snapshots outside the repository. The pre-change parser was extracted from the parent of `997909214fbcaafa9dca9740d1fefdbcd1312719` to distinguish newly accepted cases from pre-existing behavior.

## Governing interpretation

[Observed] RFC3-16(c), `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md:361–411`, defines state (1) and states at lines 369–370: “It may be performed before or after an A1 mechanism exists; after A1 exists, the act must explicitly select state (1).” It prescribes no literal parser trailer such as “explicitly selected”. RFC3-16(b), lines 303–305, says state (1) remains available after A1 “only when the human owner explicitly chooses trusted-bootstrap provenance in the act itself.” RFC3-16(a), lines 245–251, distinguishes a trusted recorded state-(1) claim from proof of attendance and prohibits a machine from reinterpreting an act.

[Inferred] In the frozen record, the paragraph labels the provenance `owner-adopted (bootstrap, uncorrelated)`, identifies it as state (1), and affirmatively says it was “explicitly given by the owner's words recorded below”. Recognizing that affirmative statement as the parser's explicit-selection claim accurately represents the recorded claim under the existing clause. It does not by itself adopt a new contract meaning. Requiring the historical literal “explicitly selected” would add a lexical requirement that RFC3-16(c) does not contain. This narrow conclusion does not independently prove the underlying human act or its complete historical chain; those remain subjects of the eventual full review. The October 20 installation direction is not treated as adopting an extra RFC3-16(c) reading.

## Strengths

[Observed] The implementation preserves the exact provenance label, A1 absence and the parser/evaluator separation. The three added parameterized cases in `owner-act-record.test.ts:97–104` cover the affirmative v4 encoding and two distinct missing-selection forms; net test delta for this change is +3 cases. The unchanged evaluator still checks provenance vocabulary, lifecycle, A1 state mechanics, phrase and digest matching, and controlled expectations.

## Important — new v4 wording is accepted inside explicit denial or quotation

[Observed] `packages/three-surface-poc-core/src/owner-act-record.ts:143` performs an unanchored substring search. In an otherwise valid synthetic state-(1) policy record, this trailer:

```text
not explicitly given by the owner's words recorded below
```

produces `explicitSelection: true`. The actual `evaluateBodyReadAuthority` then returns a valid policy state and admits the synthetic consent/policy/registry triple with `authorizationMode: owner-trusted-bootstrap`. `body-read-authority.ts:538` trusts this boolean and does not reject the negative declaration. The pre-change parser returns false for this same input, so this counterexample is introduced by the new alternative. The same newly accepted outcome occurs for `never explicitly given by the owner's words recorded below` and an explicitly rejected quoted example of the v4 wording.

[Inferred] This is a fail-closed correctness defect in the implementation, rather than a disagreement about the legitimate affirmative wording. A declaration expressly denying selection cannot supply RFC3-16(c)'s explicit-selection claim. It violates engineering-bar's fail-fast/failure-path criteria and test-rigor expectations 2–4. The three added cases do not exercise the negation or quotation boundary.

[Inferred] Constrain the supported extraction encodings to affirmative selection declarations and reject negative or quoted occurrences before projecting `explicitSelection`. Preserve the frozen affirmative v4 record and legitimate historical affirmative encodings. Add a nearest-suite parser regression and a real-evaluator regression showing that the negative policy record yields `policy:state-1-not-explicitly-selected` and `admits: false`. Do not edit the frozen act, require new owner words, or change RFC3-16(c) to fix this parser defect. The analogous negative legacy trailer already passed before this commit; the local predicate correction should preserve affirmative history while avoiding both negative paths.

## Verification and limits

[Observed] Reproduction: `node --disable-warning=ExperimentalWarning reproduce-authority.mjs` under this report's directory, Node `v24.6.0`. It strips TypeScript from exact snapshots using Node's built-in type stripper and runs the real parser, artifact-field extractor and authority evaluator. Inputs are synthetic and self-contained; recording-tag resolution is an injected fixture, not a production-tag verification.

[Observed] The probe has 12 explicitly enumerated cases: 8 match their independent expected admission outcomes and 4 expose unsafe acceptance. Three are newly accepted v4 denial/quotation cases; one identifies the pre-existing negative legacy form. Affirmative v4 and legacy fixtures admit; recorder assertion, owner wording without “explicitly”, absent selection, an occurrence after the record head, missing provenance and malformed provenance reject. The Python result audit independently counted the 12 rows and enumerated the same four remainders. Exit status 1 is the intended failing regression result. This is not a full-suite or clone/CI pass.

[Observed] Reproducer SHA-256: `148bef76f15d2f549bb8cbbfcedde7585d3e26ebd011737f3fbfc854a7d21df1`. Result JSON SHA-256: `4b0e29de35986ecff6082cca4f6b8dac09f3e6df7a5be44445a1609377aba3a8`. The command's exact stdout, stderr and exit status are retained in `R-P110-EXPLICIT-SELECTION-PROBES-F16AB18F-1-RAW.md`.

## Preliminary assessment

[Inferred] REVISE the extraction predicate and its negative-path tests. The affirmative v4 encoding itself is compatible with extraction under the existing RFC3-16(c) meaning. Overall implementation and merge assessment: NOT ISSUED. Hold pending final frozen head and evidence release.

[Observed] Re-issued as a second immutable raw solely to clarify the scope statement: procedural `AGENTS.md` was read from the repository. The first raw is preserved unchanged; substantive findings, subject bytes, evidence and preliminary verdict are unchanged.
