# Current-format coverage reconciliation

[Observed] The accompanying [binding bridge](../evidence/polaris-generator-non7-current-binding-bridge-2026-09-12.json) reconciles the preserved RFC1–4 V2 and RFC5/6/8/9 V2 coverage records with the current frozen review subject. It does not replace their semantic assessments or grant applicability decisions.

All 23 archived subjects retain the same whitespace-normalized word sequences. Only the specification has changed bytes. Its 29 complete requirement word sequences and 154 scenario bodies remain equal; current requirement and scenario locations were independently extracted and the scenario tuples agree with RFC7 V5. A separate line-based count confirms the requirement and scenario populations.

The reconciliation checks the 136 retained RFC1–4 clause bodies and their 904 locator quotes, and current source hashes and 565 locator quotes for RFC5/6/8/9. It re-extracts the locations of 3,449 retained mapped scenario references. These are reference occurrences, not distinct tests or independently discharged consequences.

The JSON retains the two `ownerScopeSubjects` values exactly, under their existing keys. They remain proposed conditional scope; GNA-1 through GNA-3 also remain proposed in the frozen applicability document. RFC1–4 V2 remains a repair confirmation for R14-1/R14-2, and RFC5/6/8/9 retains its stated inventory limits. This binding check adds no adoption, exhaustive semantic coverage, runtime or output-quality claim.
