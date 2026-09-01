# Raw independent review — PWB state-(1) amendment authority boundary and security

## Review identity

- Reviewed commit: `f31f8315ecd75d83dd73ebd6739f003c241e8584`
- Reviewed manifest: `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`
- Manifest SHA-256: `657197d697abd3e502847085351741f403a8b7a9a93e10c12764fbfc72288ff5`
- Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`
- Review class: CC-REV-1 authority boundary and security
- Desired verdict supplied: no

## Findings

No findings.

- BLOCKER: 0
- MAJOR: 0
- MINOR: 0

## Authority and security review

- [Observed] The worktree HEAD was the exact reviewed commit. The manifest digest independently recomputed to the value above from both the worktree file and `git show` of the committed file. The manifest contains the closed eleven-path population in codepoint order. A second independent `git show f31f831:<path>` SHA-256 sweep verified all 11 stated subject digests with 0 mismatches.
- [Observed] PWB-REQ-005 admits the complete eight-case valid truth table for consent, policy and registry provenance: `(1,1,1)`, `(1,1,2)`, `(1,2,1)`, `(2,1,1)`, `(1,2,2)`, `(2,1,2)`, `(2,2,1)` and `(2,2,2)`. Its universal all-valid equal-or-mixed rule, state/invalid-arm sweep, hard-coded independent oracle and task 4.1 together require all eight rather than a sampled mixed case.
- [Observed] PWB-REQ-005 rejects each named invalid limb: missing, malformed, non-human, unattributed, wrong project, wrong repository, wrong class, wrong scope, wrong act type, digest mismatch, stale, expired, superseded and revoked, plus invalid state-(1) selection/audit absence and failed, unavailable or indeterminate state-(2) correlation. Any invalid limb requires zero body reads, project-model Unknown, the RFC3-16(a) contradiction and visible retention of the invalid state. A claimed state (2) never falls back to state (1).
- [Observed] Both PWB-REQ-005 and PWB-REQ-022 require an effective human owner act under RFC3-16(a), the complete RFC3-16(b) nine-field binding set, explicit state-(1) selection with A1 audit identity absent, or successful state-(2) correlation with its audit identity. A specification signature, stored attribution, file, commit, tag, machine submission, agent assertion, test, report or availability cannot substitute for the human act. The independent state-(1) oracle is expressly limited to record semantics and disclosure and does not claim to prove attendance.
- [Observed] State (1) and state (2) remain distinct. Only state (2) may be called independently verified. PWB-REQ-005 and PWB-REQ-022 use the identical required disclosure: `Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance.` Each requirement requires identical human, machine and export behavior; PWB-REQ-020 exhausts the authorization/judgment state and disclosure populations with an order-insensitive, multiplicity-preserving comparator.
- [Observed] PWB-REQ-005 preserves the security conjunction around body reads: exact observing-project/configured-repository pair and observation class, the observing project's own exact secret policy, governance-homed observer registration for the same pair, read-only authority, empty write surface, exact Git-object containment, traversal/symlink/submodule rejection, inert parsing, bounded inputs/outputs, fail-closed secret classification, authenticated inherited POC surfaces, no execution and no egress. The amendment changes only which valid RFC3-16(c) provenance states may satisfy the three owner-act gates; it does not remove or disjoin another gate.
- [Observed] The consent, policy and registry acts warrant only use of those exact artifacts. They are never evidence that a read occurred, screening succeeded, admitted content is secret-free or a derived claim is true. PWB-REQ-022 likewise keeps the kernel-recorded walkthrough execution fact separate from the owner judgment, treats the judgment as human adjudication rather than Observed evidence or a score, and says neither the act, digest, correlation nor run record proves comprehension succeeded.
- [Observed] PWB-REQ-022 accepts valid state-(1) and state-(2) judgments with exact state visible. Missing run or judgment yields Unknown-never-met without inventing a verdict. A present invalid judgment records exact `verdict-unlawful`, retains the RFC3-16(a) contradiction and remains Unknown-never-met. Failed state-(2) correlation has no state-(1) fallback.
- [Observed] Later A1 correlation affects only a later evaluation. PWB-REQ-005 and PWB-REQ-022 both prohibit rewriting the state under which an earlier read or judgment took effect, preserving the owner-trusted provenance of historical effects.
- [Observed] The proposal, design, semantic delta, capability coverage, effective contract overlay, generated dependency union and tasks consistently state that these bytes are candidate only. They create no consent, policy, registry or judgment act and authorize no body read, implementation, write, egress, execution, deployment, release, recovery or mission. The six parent Three-Surface POC artifacts remain unchanged.
- [Observed] The exact-digest amendment is indivisible: all eleven signed subjects, including unchanged `.openspec.yaml`, take effect together or none do. The transaction-validation changes keep the 2026-09-01 performed manifest immutable, reject unsigned or one-sided successor records, reject conflicting successor digests and path-population drift, and switch current-byte authority only after matching aggregate and dedicated successor acts bind the exact eleven-row manifest.

## Validation evidence

- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --check` reported `11 artifacts`; its self-test passed population, determinism, byte mutation and path mutation.
- [Observed] The dependency generator reported 17 requirements; the effective coverage generator reported 324 accepted clauses represented; its self-test passed exact IDs/dispositions, columns, family/total/repair counts, warrants and determinism.
- [Observed] `npx openspec validate polaris-project-wide-butlers-model --strict` reported the change valid.
- [Observed] The performed general trusted-bootstrap check reported 30 contract paths, 5 historical PWB paths and 5 owner-act rows frozen and valid. Its 10 mutation cases had 0 failures.
- [Observed] `python3 scripts/check_governance.py --selftest` reported `178 fixtures, 0 failing`, including unsigned-successor, one-sided-act, digest-conflict, exact 11-row successor, current-drift, row-count, duplicate, reorder and escaping-path cases.
- [Observed] The ordinary governance run reported `32 OK, 19 WARN, 1 FAIL (52 checks)`. The one failure is CG-7h's five expected current-path mismatches against the historical 2026-09-01 PWB manifest while no successor act exists. This is the intended candidate posture: the unsigned amendment cannot impersonate current authority. It is not evidence that the amendment has taken effect.
- [Unknown] No implementation or runtime effect is reviewed or proven by this specification review. Body-read behavior, secret-screening success, surface authentication, parity and walkthrough outcomes remain to be established by separately authorized implementation and retained evidence.

## Verdict and owner gate

**VERDICT: CONFIRM**

[Inferred] Within the authority-boundary and security review class, the exact eleven-artifact package may be offered for owner sign-off at manifest digest `657197d697abd3e502847085351741f403a8b7a9a93e10c12764fbfc72288ff5` once the other required independent review classes are complete. This review is not owner sign-off, does not make the candidate effective and grants none of the downstream authorities listed above.
