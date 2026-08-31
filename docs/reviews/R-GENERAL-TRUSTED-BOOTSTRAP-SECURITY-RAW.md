REVISE

Blockers

1. The manifest-bound accepted contract set still contains the retired A1-only rule. RFC3-16(a) says valid state (1) is effective and absence of correlation alone does not block it (`RFC-0003/governance-homes-and-owner-acts.md:205-233,279-300`), yet:

   - RFC4-23 says an “unverifiable bound is no declaration” (`RFC-0004/fidelity-joins-and-mappings.md:87-96`).
   - RFC8-16 repeats that an “unverifiable” liveness bound remains ineffective (`RFC-0008/state-vocabulary-and-cost.md:239-244`).
   - RFC9’s package integration says every listed registry, judgment, release policy, and N/A artifact whose provenance “does not verify” is absent (`RFC-0009/README.md:121-136`).

   These clauses make a valid, deliberately uncorrelated state-(1) act ineffective. This fails acceptance criteria 1 and 4 and CC-REV-2’s same-logical-change requirement. Replace these consequences with effective-act checks: state (1) or state (2) succeeds; missing or invalid acts fail closed.

2. Multiple manifest-bound reader maps and violation cases still teach the old rule:

   - RFC3’s reader map says authorization requires provenance verifiable by an unforgeable mechanism (`RFC-0003/governance-homes-and-owner-acts.md:39-54`), later describes no record as the “stamped-but-unverifiable case” (`:145-149`), and treats an “unverifiable authorization” as invalid (`:435-439`).
   - RFC5’s reader map requires classification-policy and consent provenance to verify (`RFC-0005/consent-egress-secrets.md:42-50`), and its violation case rejects consent because provenance was “never verified” (`:233-238`).
   - RFC7’s reader map says an “unverifiable” human judgment has no effect (`RFC-0007/rendering-and-surface.md:52-60`).

   Although some sections are labeled non-normative, they prevent a fresh reader from correctly restating the amended contract and contradict the normative clauses they summarize. This fails VIS-3, CC-REV-4, and acceptance criterion 2.

3. The transaction’s authority/non-authority statement contradicts its own fifth act. Row 5 performs `confirm-craft-amendment` on the in-force CC-SPEC policy (`ACT-SEMANTICS.md:15-21`), while the same artifact says the transaction performs “no ... policy approval” (`:27-30`). A fresh reader cannot determine whether the policy amendment is performed. Qualify the latter as “no effect-specific authorization-policy approval” or explicitly except the CC-SPEC amendment. This affects acceptance criterion 12 and VIS-3.

Non-blocking observations

- [Observed] I resolved `ecf16fb` to `ecf16fb96450f8ecc4fd6a2fb2525f0faf1804d4` and reviewed a temporary `git archive` of that commit, not the subsequently modified shared worktree.
- [Observed] The transaction manifest SHA-256 is `9dc975399ee5859f7a585c10b8bc4e0d5184fe70887e825d83bc5f0593409f6d`. All seven direct subjects verify; all 30 nested contract rows and five PWB coverage rows verify; installed RFC 0001–0009 bytes equal their candidate mirrors. Historical Wave A/B manifests are unchanged from the baseline. The independent impact check reproduces 204 baseline files.
- The central model otherwise preserves exactly two states, reserves “independently verified” for state (2), requires explicit state-(1) selection, and prevents failed or indeterminate correlation from creating state (1) or downgrading state (2) (`RFC-0003/governance-homes-and-owner-acts.md:251-300,318-366`).
- SEC-2 through SEC-5 remain conjunctive in the normative gates: egress still requires consent, classification, and audit (`RFC-0005/consent-egress-secrets.md:153-172`); secret screening remains all-ingest and fail-closed (`:176-199`); execution retains every profile/authentication/capture limb (`RFC-0005/execution-profiles.md:80-96`); write containment and per-repository consent remain (`RFC-0003/manifests-and-namespace.md:163-171,211-231`).
- Owner acts remain warrants rather than substantive-success evidence (`RFC-0003/governance-homes-and-owner-acts.md:358-366`). RFC 0010 remains candidate and non-operative (`RFC-0010/mission-identity-approval-and-lifecycle.md:204-216`), and RFC9 expressly creates no deployment or recovery authority (`RFC-0009/visual-grammar-and-lenses.md:580-583`).

Plain-language authority restatement

After the blockers are repaired and a human owner performs the exact replacement transaction, a real digest-, scope-, act-type-, attribution-, lifecycle-, and ceremony-bound owner act may take effect in state (1) without external correlation. It must remain visibly “owner-adopted (bootstrap, uncorrelated).” Only successful independent A1 correlation permits state (2), “Syzygy-verified”; failed correlation never falls back to state (1).

That amendment would not itself observe or write a repository, approve egress or execution, adopt a registry, deploy, release, recover, start a mission, accept RFC 0010/0011, or authorize implementation. Each later effect still needs its own exact consent, policy/profile, scope, adapter, authentication, secret-screening, evidence, audit, recovery, and stop gates. The owner act authorizes the bounded attempt; separate evidence establishes what actually happened and whether it succeeded.
