# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-2 — screening scope v2 review, round 2
Reviewed commit: a1564e1f26e07ff7625bcbfe5604cbb1adc5acd4
Manifest SHA-256: acc7494af578bf55a4ebc7d5089957b3bc0b707b73ea088890525cb9320be51b
Verdict: REVISE

Reviewer: fresh-context governance reviewer (Claude Opus 5.5). I worked in a detached worktree at the reviewed commit. I called no model provider and read no external repository body. Probe scripts ran in a scratch directory outside the worktree. Every rule-6 mutant was restored, and `git status --porcelain` was empty afterwards.

## Checks run (this session, at the reviewed commit)

- [Observed] `gh pr view 326` headRefOid = a1564e1f26e07ff7625bcbfe5604cbb1adc5acd4.
- [Observed] `--check`: "current", exit 0.
- [Observed] `--selftest`: "70 of 70 predicates held", exit 0.
- [Observed] `--ready`: exit 1, with two FINDINGs: the class is not defined in the installed RFC-0005 text, and the version-1 act is not recorded.
- [Observed] `--ready --pending-prerequisite`: exit 0, with the same two lines as NOTE.
- [Observed] `--manifest-digest --pending-prerequisite` printed acc7494a…; `sha256sum` of the manifest file gives the same value, which equals the expected digest.
- [Observed] `python3 scripts/check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] `gh pr checks 326`: `checks` pass, `node` pass.
- [Observed] Rule 6, all against `--check`, each restored afterwards. Every one exits 1 with STALE:
  - (a) In the architecture patch, the `docExcludedSegments` literal `"governance"` was changed to `"governanc"`. Result: "architecture: patch differs from its regeneration".
  - (b) The architecture patch was copied over the manifesto patch, so a variant carried another variant's rule. Result: "manifesto: patch differs".
  - (c) The `[variant: manifesto]` and `[variant: architecture]` labels were swapped in the manifest. Result: "manifest differs from its regeneration".
  - (d) `"manifesto"` was added to the rootStems of the none patch. Result: "none: patch differs".
- [Observed] B-4: I applied the #257 package's `proposed/RFC-0005/consent-egress-secrets.md.patch` to a copy of the real installed module. I placed the copy at `RFC5_INSTALLED` in a scratch root with a v1 act file present. `readiness()` returned `[]`. With the unpatched real module it named the missing class. The selftest readiness predicates (met, class missing, act missing, file absent, real path exists) all hold.
- [Observed] B-3: the reference reader returns False for `٠١-README.md`, `١٢-LICENSE`, `０１-README.md` (fullwidth) and `1２-README.md` (mixed), and True for `01-README.md`. The selftest's `str.isdigit` mutant is caught.
- [Observed] N-5: fixture `LICENſE` is False under the ASCII fold and True under `casefold`. Fixture `docs/ſpecs/x.md` is True under the ASCII fold and False under `casefold`. Fixture `docs/CMAKELISTS.txt` (Kelvin sign) is True under the ASCII fold and False under both `lower` and `casefold`. All three swap mutants are caught in the selftest.
- [Observed] B-1/B-2 depth and case: these are all False: `docs/a/b/ADR/x.md`, `DOCS/X/Y/GOVERNANCE/z.md`, `docs/a/Policies/b.md`, `docs/a/SECURITY/b.md`, `docs/a/b/c/RFCS/x.rst`, `docs/x/REQUIREMENTS-dev.TXT`, `doc/Robots.TXT`, `docs/a/CMakeLists.TXT`. Root `SECURITY.md`, `DESIGN.md`, `GOVERNANCE.txt` and `CODE_OF_CONDUCT.md` are False in every variant.
- [Observed] Variants: diffing the none patch against each of the other three shows only the hunk-header line counts and the added `rootStems` entries. The four manifest rows are distinct. With rootStems as the only difference, `MANIFESTO` and `00-ARCHITECTURE.md` are True exactly in their own variants and in `both`.
- [Observed] Consumer: `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:95` runs `detectSecrets` and then `scanActiveContent` on every body. It does not read `contentClassification`, and the PR changes no file under `apps/` or `packages/`. `semantic_findings` (builder 430-432) fails any change to detectors, activeContent, accessBoundary, rawBodyHandling, inheritedRules or selfReferenceRule. No screen is weakened against v1.
- [Observed] VIS-4: a sweep of the added lines for accepted, approved, adopted and "in force" finds only "approved requirement" in the unchanged v1 `inheritedRules`, prerequisite conditions ("while … is not in force") and brief or review text. None is a label.

## Findings

**Finding 1 — name-based withholding is root-only, and the policy bytes and the packet still claim more than the rule does** (blocking)
The docs-tree rule excludes only exact directory segments (builder 102-103, 149). A governance-shaped file name, or a near-synonym directory, under `docs/` is mapped in every variant. Probes through `classify_documentation` with the none rule all return True:
- governance-shaped file names: `docs/spec.md`, `docs/design.md` (both are asserted True by fixtures at builder 179), `docs/SECURITY.md`, `docs/GOVERNANCE.md`, `docs/CODE_OF_CONDUCT.md`, `docs/policy.md`, `docs/adr.md`, `doc/security.txt`;
- near-synonym directories: `docs/specifications/x.md`, `docs/decision/x.md`, `docs/adr-records/x.md`, `docs/architecture-decisions/x.md`, `docs/rfc-0001/x.md`;
- the opt-in names: `docs/MANIFESTO.md`, `docs/ARCHITECTURE.md`, `docs/architecture/overview.md`.

Against those results:
- The policy bytes contradict their own fixtures. The `indeterminate` text says "specification, design, decision and policy documents (this policy leaves them unmapped)" (builder 252-255; none patch line 107, and the same in all four patches).
- The generated withheld block says "Specification, decision, policy and report text, and any other prose" stays withheld (OWNER-DECISION-PACKET.md:34; builder 507). That is the round-1 Finding 1 defect again, in a block now asserted to be "generated from the rule's own constants". The line is a hand-written literal, not derived from them.
- SEMANTIC-DELTA.md:172-173 says that "security and conduct policies below the root" stay indeterminate. That is false for `docs/SECURITY.md` and `docs/CODE_OF_CONDUCT.md`.
- Packet Q3 (lines 81-85) justifies withholding DESIGN, GOVERNANCE, SECURITY and CODE_OF_CONDUCT "by their ordinary content". The same content is mapped one directory down. This is the root/directory inconsistency that round-1 Finding 2 named, now inverted.
- Q1 (lines 62, 67-75) says the none variant maps "neither" and frames MANIFESTO as possibly doctrine. Yet `docs/MANIFESTO.md` and `docs/architecture/**` are sendable in every variant, so declining does not withhold what the question implies.

Repair: do one of the following.
- Make the rule match the claims. Add a docs-tree file-stem exclusion for the governance names. Keep the opt-in stems out of the docs tree unless the variant enables them. Decide on the near-synonyms.
- Or make every claim exact, saying "by exact directory segment only; a governance-named file under docs is mapped". Then put Q1 and Q3 to the owner with that scope stated.

Either way, add fixtures for the probes above and derive the withheld line from the constants.

**Finding 2 — stale cross-references after the repair** (note)
- SEMANTIC-DELTA.md:192 says "See packet Q4". The policy and governance question is Q3, and Q4 is nested READMEs.
- Builder docstring line 23 still says "the one-row manifest". `--write` (line 773) prints only the default patch path.

**Finding 3 — "exactly one variant" is enforced only in prose** (note)
Nothing in the package stops a second approve-policy act over another row. The four variants share one `policyVersion` string (each patch, line 6), so the version does not tell which variant is in force; only the digest does. The packet (44-47, 76) and the delta (194-199) state the rule. The recorder, which is "written after the review", should refuse a second variant act unless it is a declared superseding version. Say so in the packet or the ledger.

**Finding 4 — Kelvin-sign denylist bypass is literal by design** (note)
`docs/CMAKELISTS.txt` is mapped, because the Kelvin sign is not folded. This is consistent with the declared literal rule, and the detectors and the active-content screen still apply. Recording it so that a TypeScript consumer reproduces it rather than "fixing" it.

Criteria summary:
1. Round-1 repairs: B-3, B-4 and N-5 hold. B-1 and B-2 hold at the root and for the exact segments, but fail on the claims (Finding 1). N-6, N-7 and N-8 hold.
2. Variant design: the variants are distinct, differ only in rootStems, and `--check` catches cross-variant mutants. Picking one row needs no regeneration. The Q1 framing is misleading per Finding 1, and exclusivity is prose-only per Finding 3.
3. Class fidelity: ARCHITECTURE and MANIFESTO are fairly presented as opt-ins with default none, citing the RFC5-14 "policy decides" and doctrine risk. Mapped paths under docs/ include governance-named files (Finding 1).
4. No weakening against v1: holds. Supersession is specified in the delta, and the performed-v2 state is covered by the selftest.
5. Builder and checks: all green as listed above.
