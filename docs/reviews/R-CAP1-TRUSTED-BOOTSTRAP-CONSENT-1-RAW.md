Independent semantic verdict: **REVISE**  
Fresh-reader verdict: **PASS**

[Inferred] The intent is understandable: propose scoped CAP1 observation consent using an explicitly human-chosen, uncorrelated bootstrap act; retain correlated consent; refuse invalid acts before content reads; preserve captured provenance across human/machine answers. Drafting and review confer neither adoption nor implementation authority.

Findings requiring disposition:

1. **REVISE — Candidate acceptance coverage is deferred rather than demonstrated.** `APPLYING.md:13–18,35–40` defers the consequence-level coverage disposition and generated dependency union until a future offering. The reviewed cluster also lacks the counted capability-obligation partition required by CC-SPEC-11. CC-SPEC-8 requires that “the specification ships with its coverage matrix”; CC-SPEC-11 requires a coverage table whose population is the declared capability obligations. The handoff truthfully acknowledges incomplete adoption preparation, but it cannot establish specification acceptance under these criteria. Provide candidate coverage/dependency artifacts and independently confirm the obligation partition before presenting an accepted specification review.

2. **REVISE — The human-attendance negative case lacks a producible, independent decision oracle.** `specs/project-registration-and-honest-shape-visibility/spec.md:40–43` requires refusal for a tree file or machine submission without an actual human act. Its generic additional oracle at `:75` states that expected tuples “are specified” without supplying how the checker produces or distinguishes an absent human act when the recorded bytes are otherwise identical. `design.md:35–40` correctly admits undetectable forgery and narrows operational refusal to recognized non-human acts. These are materially different test boundaries. CC-SPEC-4 requires a reachable case using named means and a bounded independent oracle. State separately the controllable recognized-non-human rejection predicate and the normative unauthorized-forgery limitation; identify which evidence the controlled scenario supplies. This finding does **not** demand independent attendance verification for bootstrap.

[Observed] Both full predecessor excerpts match the adopted requirement bodies exactly. All 13 protected-file digests match BASELINE.json. The stable-ID checker incompatibility is disclosed and is not grounds to renumber adopted CAP1 identities.

[Inferred] Review classes include authority boundaries, deterministic observation, security, and public interfaces. The candidate correctly preserves the operational hold, avoids state-(2) fallback, and distinguishes permission, provenance, and execution. Exact serialization and authority-source acquisition remain explicitly gated; this review establishes no implementation readiness.

Frozen SHA-256 hashes, computed during review; paths relative to `openspec/changes/cap1-trusted-bootstrap-consent/`:

```text
99f4cb4cc789c6d4e665b552c7fc401530b10f538c6cf87d334842e868590303  .openspec.yaml
e659eebdc64d40e49f008c6dedd911798005e1b4a934e64d1826bab848d24fad  APPLYING.md
5e6315d084bbe2af8a13258b5405306261f19bb4f48ce644b8c55cd0a6b00c40  BASELINE.json
14b383b1f0aad7ae625a85a8ad5478dcce9c5cd054731e3df7575a4c8e87bb65  PREDECESSOR-REQUIREMENTS.md
63162739b5679b91bed62c6a0a7bae7bf48c4be6264c26bafc22bce3230e830f  README.md
48eab94d7c33793700912001211a9e23186add7a163b7dadb8ecdf2ae9dddbbb  VALIDATION.md
ac9ea7d46f2ac03efcfc8a255798795c6f07115f8017e500f50f819dc05df5c0  design.md
5ab0200aa8609a4b1e91393edf1d8ee13aab1c6b997e65fe255e8cec4898c33d  proposal.md
10b050698d2a849bbf625cb256d85092df3b75849228eb9dd86c4a8ce7545ba7  specs/project-registration-and-honest-shape-visibility/spec.md
e5b8d0ec2701f738e66d77a4d1faee41a0427d67b5aef73d360c76053ce29193  tasks.md
```

Read-only review; no fixes authored. Preserve this raw output unchanged under CC-REV-6.
