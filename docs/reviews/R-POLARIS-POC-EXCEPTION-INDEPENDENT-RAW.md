Reviewed baseline `8fb6053` and candidate SHA-256 `da14c86b651e263e144975bfedcc59b800d5dc0600de7280a071403e6e07fa8a`. No Butlers file or external repository was read; no file was edited.

## 1. Problem scope — CONFIRMED

- [Observed] Signed `PWB-REQ-005` requires independently verifiable provenance for consent, policy, and registry before any body read.
- [Observed] The three gate artifacts were confirmed structurally sound at their current digests, but remain draft/unapproved/unadopted, with no RFC5-25 correlation.
- [Observed] The prior reads were correctly recorded as unauthorized and cannot be retroactively laundered.
- [Observed] A POC direction, owner consent statement, or PWB sign-off cannot override accepted RFC3-16(a), RFC4-7, or RFC5-16.
- [Observed] CC-REV-2 permits no lagging-spec or side-clause exception. The declined P-44 offer cannot be revived.

The smallest directly affected authorities are:

- `RFC3-16(a)`: normal failed-provenance effect.
- `RFC3-16(c)`: state-(1) normally cannot authorize an effect.
- `RFC4-7`: unverified registry entries admit no deterministic facts.
- `RFC5-16`: an unverified secret policy blocks ingest.
- `PWB-REQ-005`: independently verified triple is currently the only read-permitting mode.

[Inferred] RFC3-16(b) need not change if the exception remains inside RFC3-16(a)’s failure-effect semantics: state (1) still does not satisfy the predicate or become verified. It must nevertheless receive an explicit no-change disposition.

## 2. Recommendation/proportionality — QUALIFIED YES

[Inferred] A contract amendment is proportionate in principle because no lower authority can lawfully relax these gates, while implementing the full A1/RFC5-25 mechanism solely for one non-release POC capture would be disproportionate.

It is proportionate only as a single-use, exact-revision capture—not the candidate’s reusable authorization through 30 September.

The smallest form is one owner-authorized atomic transaction at Butlers revision `e27d063cdf6c6902853be48f74ada26931a00b59`, with two deterministic phases:

1. Discovery reads only the closed bootstrap seed set derivable from the signed PWB grammar and Git-tree metadata, under the pinned secret policy.
2. It fixes the full revision-bound manifest and digest, then reads only that manifest within the same transaction.

One owner act is sufficient if it authorizes both phases and pins the grammar/spec digest, revision, final authority-artifact digests, limits, and phase-A algorithm. A second act is necessary only if the owner wishes to inspect and approve the derived manifest before phase B. Success, failure, revocation, or expiry must consume the authority.

## 3. Candidate correctness/security — VERDICT: REVISE

Blocking findings against [the candidate](/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/POLARIS-POC-BOOTSTRAP-OBSERVATION-EXCEPTION-SEMANTIC-DELTA.md):

1. [Observed] Lines 153–160 judge expiry solely at evaluation `as-of`. Unless that instant is fixed from a trusted capture-start clock before any read and cannot be caller-backdated, post-expiry reads remain possible.

2. [Observed] Lines 130–160 allow repeated captures until 30 September. This is broader than the smallest necessary POC exception. Make it single-use at the exact revision and consume it on every terminal outcome.

3. [Observed] Lines 130–139 name artifact identities but do not embed the final consent, policy, registry, PWB grammar/spec, and revision digests. Those exact values should be in the accepted exception bytes, not supplied later by same-tree records.

4. [Observed] The current registry/policy model requires a revision-bound manifest before reads, while the full manifest is derived by reading pillar indexes. The amendment must define the two-phase discovery/capture transaction explicitly in RFC4-7, RFC5-16, PWB-REQ-005, and the registry/policy artifacts.

5. [Observed] Line 227 still names a failed `flag` condition after the flag was removed.

6. [Observed] Replacing only PWB-REQ-005’s normative body leaves its existing Case/Oracle/Falsifier requiring independent verification of all three provenances. The complete verification block must be replaced with exact two-mode success, failure, and zero-read oracles.

7. [Observed] The source identity boundary needs protection against locator substitution. Bind the opaque repository identity, approved locator mapping, exact revision, and permitted object database for this capture; reject alternates, worktree reads, symlinks, submodules, traversal, environment expansion, and path-selected widening.

Required safeguards otherwise correctly identified include fail-closed pre-parse secret screening, no raw-body persistence/logging/rendering, strict resource limits, no write/database/credential/environment/execution/egress authority, human/machine disclosure parity, no “verified” claim, no positive inference or release claim, immutable prior records, and no retroactivity.

## Blast radius

- [Observed] The PWB proposal, design, `PWB-REQ-005`, verification text, coverage artifacts, dependency union, matrices, tasks, and superseding digest-bound sign-off must move together.
- [Observed] RFC 0003/0004/0005 installed modules, candidate mirrors, package summaries, manifests, indexes, budget/router outputs, review, and owner acceptance must move in the same logical change.
- [Observed] Finalizing the consent changes its confirmed digest; all three final authority artifacts need fresh exact-byte security review before their acts.
- [Observed] Historical acts, reviews, and the incident remain append-only.

Other signed OpenSpec changes:

- [Inferred] `project-registration-and-honest-shape-visibility` requirement bodies can remain unchanged if the exception is explicitly outside Capability 1 evaluation. Its `CONTRACT-COVERAGE.md` RFC3-16(a) row still needs an explicit scoped disposition.
- [Observed] `three-surface-poc-experience/CONTRACT-COVERAGE.md` contains literal whole-POC claims that there is no consent record, runtime provenance check, registry, or secret policy at rows 290, 301–303, 322, and 370. Those rows require a recorded scope disposition; if they describe the evolving whole POC rather than only that signed change’s original slice, the signed coverage artifact must be amended. `POC-REQ-002` itself remains compatible because it prohibits content in the code-structure observer, while PWB introduces a separate project-shape observer.

The candidate is directionally lawful and correctly recognizes this as a foundational security-contract amendment, but it is not ready for owner review at the reviewed digest.
