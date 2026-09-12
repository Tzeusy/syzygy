# Polaris generator final readiness and tooling review — 2026-09-12

CHANGES REQUESTED

[Observed] This is a bounded fresh readiness/tooling review, not adoption, effect consent, a full new nine-contract coverage audit or implementation verification. Reviewed exact files:

- `scripts/polaris_generator_approval.py` — SHA-256 `a5d5d0a66990c7cdd47eb2a7f073b005ef3d46df8691fc4b08defa3633e5613e`
- `scripts/check_governance.py` — SHA-256 `e560f93ad70028ee05c939bd068b4f7d6807602cc2c7511cb8cebd1a4f1bc4b2`
- `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json` — SHA-256 `88cc5a9bee299cfaa7b332e672e7b050e84c72853bacaf003dae94a0b001707c`
- `docs/evidence/polaris-generator-review-subject-2026-09-12.json` — SHA-256 `86a7564cfcfaa5d1be050a1e52c32e0bdbc9e6f9c94f917f5a869861d3d231b0`

## R1 — Current governing population is not closed

[Observed] `governing()` enumerates only the baseline tree, then compares the current bytes of those old paths. A new governing file is invisible. Independent synthetic reproduction: initialize a temporary Git repository containing `.syzygy/governance/doctrine/test.md`, stage it and capture its tree; evaluate `governing(root, tree)`; create and stage `.syzygy/governance/decisions/new-revocation.md`; evaluate again. Both calls succeed and return exactly equal rows. The mutation does not touch the real repository.

[Inferred] This prevents the offered `/governing` inventory from proving the claimed current governing baseline. A new act or other governing input can appear without invalidating the offer. RFC3-16(b) requires binding scope and supersession/revocation relationship, and its failure rule explicitly blocks a revoked or superseded act. Although this helper is not the eventual runtime act evaluator, its immediate pre-record baseline revalidation must detect additions as well as modifications. Compare the current governing path population with the baseline plus explicit candidate/record exceptions; test a newly added file both before and after staging. Do not generalize the exception to all new governance files.

## R2 — Recorded offer need not be the registered subject

[Observed] `--offer` accepts any filesystem path for prepare, check and record. `record()` validates only that supplied file. Meanwhile `check_governance.py` associates the transaction label with the fixed `docs/evidence/polaris-generator-approval-offer-2026-09-12.json`. The generated act does not identify a different offer location, and the helper's synthetic success test records from `offer.json`.

[Inferred] A valid digest for an alternate offer can produce three dedicated records and their aggregate copies while the registry resolves a missing or different canonical subject. Prevent recording unless the registered canonical offer exists and has the exact approved bytes, or restrict record/check to the canonical path. Scratch preparation can remain available. Add a refusal case for an alternate valid offer with absent/different canonical offer. This is an identity/integration defect under RFC3-16(b), which binds stable artifact identity and exact content, not merely any supplied JSON digest.

## Stale coverage issue and proposed scope

[Observed] The V5 matrix's 26 `subjectBindings` all match current SHA-256 bytes, including the complete 23-file frozen candidate population. Independent archive comparison found equal whitespace-token sequences for each of those 23 current files versus the retained V1 archive. V5 explicitly retains the 29 requirements, 154 scenarios, updated semantic reassessment and format-only rebinding. The prior A1 stale-binding finding is closed for this revision; this statement does not substitute for full semantic coverage review.

[Inferred] GNA-1 through GNA-3 remain precisely scoped to workspace/portfolio consequences, while individual project relationships and child composition remain required. RFC7-38 requires “Rows are per observable consequence, not per clause.” CC-SPEC-8 says that a non-consumed consequence still requires an N/A judgment and that the judgment is honored only through an effective owner act. The final offer therefore needs the exact selected conditional dispositions for computed rendering, observed-code launching and non-consumed intake/inherited work; merely passing arbitrary resolvable references does not establish semantic completeness. Selecting and independently checking those actual references is still pending because no final offer exists.

[Observed] The helper fixes project/package identity, reconstructs roles and scope, binds the complete candidate subject, checks selected JSON-pointer values and pins review bytes. It does not inspect review verdicts; selection of actual current PASS reviews remains an operator/reviewer responsibility. Its output explicitly disclaims independent authorship/review/effect/completion verification. The three distinct act bodies preserve explicit bootstrap provenance and absent A1; a recording commit/tag is still necessary for the durable state-(1) history described by RFC3-16(c).

[Inferred] The implementation effect text preserves the full Phase A/B/C goal and separately admitted real source, provider and destination effects. This is consistent with SEC-2's explicit scoped consent and SEC-3's observed-code boundary. An implementation act is not a blanket source/provider/write permission. A prepared offer must clearly present trusted-bootstrap selection to the human owner before the exact phrase is used; this review performs no such act.

## Executed checks

[Observed] `python3 scripts/polaris_generator_approval.py --selftest` passed its synthetic cases. `python3 scripts/check_governance.py --selftest` reported 234 fixtures, 0 failing; the output was inspected. The independent added-governance mutation above exposes an untested failure despite those passes. Existing-file tamper, project/package identity, exact instant, owner mismatch, missing/extra candidate file and duplicate aggregate checks are present. No real record invocation, provider call, external project read or implementation change was performed.

[Unknown] Final prepared-offer readiness remains unestablished until R1/R2 are repaired and the concrete canonical offer, pinned PASS reviews and complete selected applicability references are independently checked. No candidate byte change is requested by this review.
