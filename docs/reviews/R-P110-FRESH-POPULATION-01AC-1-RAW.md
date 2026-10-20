# Bounded security finding — fresh source population

Subject: `01acff07c828c1adaaf1bc9c92ba87cb4d4abf2b`. Base: `dd520e8dd2e857814d9cf5ab1ac55eb79b83da33`.
Review scope: the new public-source verifier and pipeline fresh-object handoff. This is a bounded finding, not the final implementation verdict.
Evidence metadata: `subject-evidence.json` in this packet records exact Git blob and SHA-256 identities for the reviewed implementation and governing references.

[Observed] **Important — compare and replace the complete source population returned by the fresh verifier.**

`packages/polaris-generation-core/src/pipeline.ts:252–264` compares only the request rows with `redaction`, then replaces only those rows. `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:216–218` checks repository/revision and returns the newly read and screened population. A self-consistent ordinary request row can therefore differ from that population while the run still sends it.

I reproduced this with an isolated synthetic Git repository containing one legitimately redacted documentation file and one ordinary code file. The request was serialized and parsed, and used the actual `readScreenedRepoCorpus`, `screenedRepoCorpusVerifier`, and `withConsent` adapters. Synthetic observation/egress records admitted the pinned commit and the two content classes; the consent adapter bound the request's exact population. The provider port was a local stub; no external provider, daemon, or Butlers body was used.

The unmodified control reached `awaiting-rendered-review` with 5 stub calls and no sentinel. Replacing just the ordinary source with `generationSourcesForBody` of `token=INDEPENDENT-SECRET-NOT-IN-PINNED-GIT\n`, with its correct Git blob hash but no corresponding body at the pinned path, also reached `awaiting-rendered-review` with 5 stub calls. The sentinel was present in provider input (`leakedSentinel: true`). The fresh corpus still held the original body. Original/pinned OID: `02a7c5df78723ba6e088c63d531acf0b7411c85d`; request's substituted OID: `97dc08cc43bf4685da4eb03e1677ba915fb08da0`. One other request row was a legitimate redacted projection and was successfully rehydrated through the actual adapter.

The positive test passes. The required refusal test fails at this subject: expected `source-refused` with zero sends, observed `awaiting-rendered-review` with five sends. Raw Vitest and run result JSON are retained beside this raw. The fixture's initial setup had an unmapped provider route and missing revision label; those setup errors were corrected before the retained reproduction. They are not implementation findings.

[Inferred] The new verifier's promise to re-read and screen the pinned population is bypassed for ordinary rows in a mixed request. This can carry a detector match into provider input despite the fresh screen. Bind every request row and the population membership to the fresh gated result (accounting for the existing ordinary full-body compaction and opaque excluded-row identities), then use the fresh rows for content. Add the same actual-adapter positive and mixed-population negative as regression protection.

Governing acceptance: the approved impact ledger's “Provider egress population” requires egress tests for retained-body spans, and its target-body call-site entry requires the corpus reader to carry retained bodies. RFC5-17 defines excluded provenance as “never the content itself, in any store including the audit trail.” Its final paragraph makes a secret reproduced in a surface, store, or endpoint a trust-floor violation. Parent's acceptance criterion requires comparing replay/provider input to the fresh gated population before content use; this probe exercises that exact boundary.

[Unknown] This does not establish active live-provider exploitability: the new verifier is an exported core capability and the existing generic trigger remains unwired. No overall review/merge verdict is issued here. Later corrections require separate exact-head verification.
