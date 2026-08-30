# Fresh-context review report

Review target: exact commit `f092388219867149237d586d5f18a3884ff7f3a4`

## 1. PASS

- [Observed] Both generators passed `--selftest` and `--check`; `openspec validate polaris-project-wide-butlers-model --strict` passed.
- [Observed] Independent set checks found 11 unique requirements, 11 warrant blocks, 12 capability-table rows, and a disjoint mechanical partition of 64 mapped + 25 applicable-uncovered + 235 believed-not-applicable = 324 indexed clauses.
- [Observed] The six signed `three-surface-poc-experience` artifacts still match the digests recorded at `.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md:36-49`; no signed parent artifact differs from `db5eaee`.
- [Observed] The owner direction confines itself to amendment authoring and requires a separate sign-off before implementation at `.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-POC-EVALUATION-DIRECTION.md:31-38`.
- [Observed] The candidate is explicitly non-binding at `openspec/changes/polaris-project-wide-butlers-model/proposal.md:67-72`.
- [Inferred] The candidate is structurally additive rather than directly contradictory: its project-wide source population, ordering, and evaluation criteria strengthen the parent floors while naming `POC-REQ-020`, `030`, `031`, and `032` as parent requirements. No parent bytes are silently changed.
- [Observed] Unknown, contradiction, exact-revision, shared-model, provenance, and owner-judgment failure paths are treated as first-class requirements rather than optimistic defaults.

## 2. FINDINGS

### 1. BLOCKER — The 324-clause matrix is a set partition, not a consequence-granular contract review

Evidence:

- [Observed] The generator reads only clause identifiers from the index, not authoritative clause text: `scripts/build_polaris_project_wide_contract_coverage.py:18-30`.
- [Observed] Every mapped row receives the same unsupported sentence at `scripts/build_polaris_project_wide_contract_coverage.py:130-134`.
- [Observed] Every believed-not-applicable row receives one family-wide reason selected solely from the RFC number at `scripts/build_polaris_project_wide_contract_coverage.py:60-79,163-164`.
- [Observed] The self-test proves only denominator presence, mapped/uncovered disjointness, and deterministic output at `scripts/build_polaris_project_wide_contract_coverage.py:183-210`.
- [Observed] The generated artifact repeats the same generic mapped assertion for all 64 mapped clauses at `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE.md:18-81`, and family boilerplate for all 235 Part B2 rows beginning at `CONTRACT-COVERAGE.md:121-140`.
- [Observed] CC-SPEC-8 requires rows per observable consequence, explicitly stating that one mapped requirement does not cover a clause with five consequences: `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:229-257`. RFC5-27 repeats that under-enumerated consequences make a complete-looking matrix defective: `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md:353-360`.

Why it matters:

- [Inferred] Passing `--check` establishes byte regeneration and a 324-ID partition only. It provides no evidence that any of the 324 applicability judgments is correct or that every consequence within a mapped clause has coverage.
- [Inferred] Owner sign-off based on this matrix would mistake mechanical completeness for semantic coverage—the exact failure CC-SPEC-8 prohibits.

Minimum precise fix:

- Replace each clause-level boilerplate row with an enumerated consequence record containing the authoritative clause/line pointer, the specific consequence, applicability reasoning, and exactly one disposition: mapped requirement, Unknown, or owner-recorded N/A.
- Make the generator validate exhaustive consequence identities rather than infer semantic judgments from RFC family numbers.
- Add mutation tests that remove or misclassify one consequence and prove the check fails.

### 2. BLOCKER — Material warrants are overclaimed, so the generated dependency union and mapped set are semantically unsound

Evidence:

- [Observed] PWB-REQ-001 cites all of RFC2-1 at `spec.md:37-46`, but its oracle checks only Git revision and admitted source paths at `spec.md:14-29`. RFC2-1 requires every deterministic input, including policies, parser/configuration, owner acts, prior observations, and the full minimum list at `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md:67-105`.
- [Observed] PWB-REQ-003 cites RFC5-16 and RFC5-17 at `spec.md:114-123`, but its oracle scans response bytes only at `spec.md:96-106`. RFC5-16 binds every store, surface, endpoint, policy version, and owner-act provenance at `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md:172-192,194-216`.
- [Observed] PWB-REQ-011 cites RFC7-9 at `spec.md:223-232`, while its oracle verifies route reachability, not anchor covering, minimality, or bounding. Those are RFC7-9’s distinct consequences at `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md:177-195`.
- [Observed] The dependency generator validates warrant-block syntax and qualified-parent existence, not whether a warrant’s consequences are actually exercised: `scripts/build_polaris_project_wide_spec_dependencies.py:48-72,96-127`.
- [Observed] CC-SPEC-2 requires every material warrant and forbids hiding or misrepresenting governing identities: `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:62-97`.

Why it matters:

- [Inferred] Because Part A is derived directly from these warrant citations, overclaiming one clause simultaneously corrupts `GOVERNING-DEPENDENCIES.md` and `CONTRACT-COVERAGE.md`.
- [Inferred] The current 64 mapped clauses cannot be confirmed as covered.

Minimum precise fix:

- Re-audit every requirement against each cited clause consequence.
- Retain a warrant only where the requirement and oracle exercise the material consequence; otherwise add the missing oracle or move that consequence to Unknown.
- Record partial limbs per consequence rather than calling the whole clause mapped.

### 3. BLOCKER — The “12 obligations” denominator omits declared refusals and is therefore incomplete

Evidence:

- [Observed] `CAPABILITY-COVERAGE.md` declares exactly 12 obligations and reports `12 covered, 0 lawfully out of scope` at `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md:3-20`.
- [Observed] The proposal separately declares refusals covering arbitrary implementation bodies, treating every file/proposal as capability truth, inferring missing capabilities, modifying Butlers, additional projects, production release, autonomy, multi-user support, and weakened security/truth floors at `proposal.md:54-65`.
- [Observed] The design adds further non-goals—LLM inference, project writes, and second-project generalization—at `design.md:26-32`.
- [Observed] CC-SPEC-11 defines the population as everything the capability “does, renders, records, or refuses” and requires every obligation in exactly one of covered, lawfully out-of-scope, or Unknown: `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:308-337`.

Why it matters:

- [Inferred] The table was derived from the chosen requirements, not independently from the full scope statement. It therefore cannot demonstrate requirement-set completeness.
- [Inferred] At least the explicitly declared refusal population is absent, and several of those refusals require security or trust-boundary verification rather than a prose non-goal.

Minimum precise fix:

- Rebuild the capability population from every positive and negative statement in proposal scope/design non-goals.
- Place each refusal in the table with its governing requirement or named excluding non-goal.
- Do not report zero lawfully-out-of-scope obligations while the proposal contains an explicit out-of-scope list.

### 4. BLOCKER — Observation consent and the concrete secret policy do not exist, so the proposed ingest cannot lawfully produce the desired model

Evidence:

- [Observed] The design says allowlisted files will be opened and classified before entering the model at `design.md:91-96`; implementation task 2.3 assumes “the observing project's secret policy” exists at `tasks.md:19-20`.
- [Observed] The candidate itself admits observation consent is applicable and uncovered at `CONTRACT-COVERAGE.md:109`.
- [Observed] An exhaustive current-tree scan found 47/47 decision files and zero `observation consent` records or Butlers-specific consent records; no `.syzygy/project.yaml` or consent artifact exists.
- [Observed] An exhaustive scan found 11/11 policy files. Only `engineering-bar.md` and `security-and-secrets.md` mention a secret-detection policy; neither defines concrete detection/classification rules.
- [Observed] RFC5-12 requires explicit per-repository observation consent; absent consent means no observation, Unknown: `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md:77-95`.
- [Observed] RFC5-16 requires the observing project’s concrete policy, its version in the snapshot, and verifiable RFC3-16(a) provenance; unverifiable policy blocks ingest: `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md:172-192`.
- [Observed] RFC3-15 assigns owner approval to security policies and recorded-owner status to consent records at `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md:83-89`.
- [Observed] CC-SEC-5/6 require fail-closed classification and hash-not-body handling but do not themselves supply the concrete classifier: `.syzygy/governance/policies/craft-and-care/security-and-secrets.md:71-99`.

Why it matters:

- [Inferred] Lawful fail-closed implementation currently has only one result: do not read/index the Butlers content, leaving the project account Unknown. Bypassing that result would violate RFC5-12, RFC5-16, SEC-5, and CC-BAR-5.
- [Inferred] Candidate sign-off alone cannot silently mint a separate consent record or concrete security policy.

Minimum precise fix:

- Mark exact per-project/per-repository observation consent and an owner-approved, digest-bound secret-classification policy as implementation-blocking prerequisites.
- Add a requirement/oracle proving both owner-act provenances are verified before any repository body is read and that absence/mismatch yields Unknown with zero read calls.
- Obtain the separate owner acts before implementation.

### 5. BLOCKER — “Every declared item” has no closed identity or discovery rule, and the missing-source requirement is impossible as written

Evidence:

- [Observed] PWB-REQ-002 quantifies over “every item” across all five pillars and roster identity without defining an item, traversal closure, lifecycle inclusion, or stable identity at `spec.md:48-67`.
- [Observed] The design says the manifest stores paths and extraction classes, not Butlers facts, at `design.md:44-46`.
- [Observed] PWB-REQ-003 nevertheless requires items inside a missing, unreadable, or excluded source to remain in the denominator at `spec.md:87-106`.
- [Observed] Butlers’ root index names directories and entry documents, not a closed file/item population, at `/home/tze/GitHub/butlers/about/README.md:15-21`; roster identities are dynamic under `roster/{butler}/` at `/home/tze/GitHub/butlers/about/README.md:61-66`.
- [Observed] CC-SPEC-4 requires invariants to name their quantified scope, counterexample schema, and denominator at `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:152-171`.
- [Observed] VIS-2 forbids presenting absent evidence as zero or success: `.syzygy/governance/doctrine/vision.md:96-106`.

Why it matters:

- [Inferred] If a source’s body is unavailable and the manifest deliberately holds no fact identities, the observer cannot know how many items were inside it. Comparing a pre-fault fixture denominator does not solve the real runtime case.
- [Inferred] A hand-selected allowlist can recreate the original self-selected-model failure while still passing exact equality against itself.

Minimum precise fix:

- Define a closed, revision-bound discovery procedure: root identities, allowed link/traversal forms, extraction classes, lifecycle rules, stable item IDs, and recursive termination.
- Separate the known source-path denominator from the within-source item denominator.
- When item identities cannot be known, render the item denominator Unknown rather than preserving a fabricated count; use a prior identified observation only if the temporal contract explicitly permits it and labels it stale.

### 6. DEFECT — The new untrusted-content boundary lacks path, browser-injection, and resource controls

Evidence:

- [Observed] The only content-boundary controls are allowlisting and secret classification at `design.md:91-96`.
- [Observed] PWB-REQ-001 requires sources to resolve at a revision but says nothing about normalized repository-relative paths, symlinks, submodules, repository escape, or maximum input size/count at `spec.md:14-29`.
- [Observed] No requirement prohibits raw Markdown/HTML/SVG/URL content from becoming executable browser output.
- [Observed] No requirement states limits or fail-closed behavior for extremely large files, catalogs, link graphs, nesting, or cyclic references.
- [Observed] SEC-3 treats observed-project code as untrusted and forbids execution without an accepted profile: `.syzygy/governance/doctrine/security.md:39-45`.
- [Observed] RFC5-12 scopes observation consent per repository, so following a path outside the consented repository is not authorized: `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md:81-95`.
- [Observed] SEC-5 makes any secret reproduced in a surface or endpoint a trust-floor violation: `.syzygy/governance/doctrine/security.md:54-60`.

Why it matters:

- [Inferred] A malicious governed Markdown path could read outside the repository, execute active browser content, or exhaust the local service while remaining “allowlisted” by name.
- [Inferred] Authentication does not protect the owner from stored XSS delivered through authenticated Polaris.

Minimum precise fix:

- Require reads through exact Git objects with normalized repository-relative paths; reject absolute paths, `..`, NULs, symlink following, submodule traversal, and repository escape.
- Require context-appropriate output encoding and prohibit raw active Markdown/HTML/SVG/script/event-handler or unsafe URL execution.
- Define bounded file/count/depth/byte/time budgets; limit breaches must remain visible as Unknown without shrinking known denominators.

### 7. DEFECT — The plain-language oracle is subjective and contains an unbounded escape hatch

Evidence:

- [Observed] PWB-REQ-012 uses undefined predicates—“short,” “direct,” “necessary,” “unnecessary,” and “no required rereading”—at `spec.md:234-256`.
- [Observed] Its exception permits any “necessary scope or interaction instruction” without a closed criterion at `spec.md:240-242`.
- [Observed] CC-SPEC-4 requires an effective oracle that terminates in bounded effort and independently decides success/failure: `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:152-184`.

Why it matters:

- [Inferred] Two fresh reviewers can classify the same sentence differently with no contract-defined resolution, and an author can defend almost any meta-copy as “necessary.”
- [Inferred] The injected counterexample proves one bad string can be rejected, not that the complete real copy population satisfies an independent rule.

Minimum precise fix:

- Replace the vague predicates with a finite review rubric over the exhausted owner-visible string population, including a closed exception set and a recorded disposition for every exception.
- Specify what constitutes a pass when reviewers disagree; retain the cold-open owner judgment separately from the mechanical copy sweep.

### 8. DEFECT — The project-wide cold-open requirement omits a load-bearing RFC7-30 prompt

Evidence:

- [Observed] PWB-REQ-021 lists purpose, promises/refusals, architecture/capability groups, V1 success, exact requirements, and one Unknown/contradiction at `spec.md:347-368`.
- [Observed] RFC7-30 additionally requires the reader, for a fact of their choosing, to explain how strongly Polaris claims to know it and what would make the claim stronger; it calls that prompt load-bearing at `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md:133-152`.
- [Observed] The candidate scenario merely says “every project-comprehension prompt” at `spec.md:370-375`, leaving ambiguous whether the omitted strength prompt is normative.
- [Observed] The owner walkthrough explicitly requires the RFC7-30 result at `docs/reviews/R-POC-OWNER-WALKTHROUGH-POLARIS.md:75-77`.

Why it matters:

- [Inferred] An implementation can satisfy the explicit PWB-REQ-021 list while failing the epistemic-vocabulary comprehension test that RFC7-30 says catches a distinct failure class.

Minimum precise fix:

- State that the complete RFC7-30 prompt set remains mandatory and enumerate the added project-wide prompts separately.
- Include the claim-strength/strengthening answer in the execution record and comparison oracle.

### 9. NOTE — The owner direction does not overclaim authority, but the proposal’s “until sign-off” phrasing is ambiguous about sufficiency

Evidence:

- [Observed] The direction authorizes amendment authoring only at `.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-POC-EVALUATION-DIRECTION.md:31-35`.
- [Observed] The proposal says the candidate “authorizes no implementation until the owner signs it off” at `proposal.md:67-72`.
- [Observed] The multi-change direction says a new spec never widens implementation scope by itself: `.syzygy/governance/decisions/OPENSPEC-MULTI-CHANGE-DIRECTION.md:25-36`.
- [Observed] Improvement work must still be a recorded cycle derived from findings and satisfy POC work constraints: `.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md:29-55`.

Why it matters:

- [Inferred] “Until” can be read as owner sign-off being sufficient, although the governing decisions make it only one necessary gate.

Minimum precise fix:

- State explicitly that sign-off is necessary but not independently sufficient; implementation must also proceed under the recorded POC improvement-cycle authority through an authorized, finding-traced work item.

## 3. QUESTIONS FOR OWNER

1. [Unknown] Does “all of Butlers” mean the complete recursively reachable normative corpus of all five pillars and roster identities, or only the named project-account categories in the direction? The current candidate uses both meanings.
2. [Unknown] Should the eventual sign-off packet include a separate explicit per-repository observation-consent act for Butlers governance-text ingestion, or should that consent be recorded beforehand?
3. [Unknown] Which concrete secret-detection/classification policy is the owner willing to approve for this content class? No current policy defines a classifier that implementation can lawfully execute.

## 4. VERDICT

**REVISE**

[Observed] Mechanical validity and exact-set partitioning pass.  
[Inferred] Semantic specification acceptance does not: the central denominator is undefined, the capability table is incomplete, the contract matrix does not perform consequence-level review, and the ingest path lacks the authority and controls required to execute safely.

## 5. TOP THREE DOWNSTREAM RISKS

1. [Inferred] A mechanically green but semantically false contract matrix could cause owner sign-off on manufactured completeness.
2. [Inferred] Implementing the proposed ingest without consent, a concrete policy, path containment, and active-content controls could expose owner secrets or execute governed-repository content in the browser.
3. [Inferred] An undefined/self-selected “all of Butlers” denominator could reproduce the exact product failure this change exists to repair while reporting complete coverage.

# Separate security review

## 1. Trust-boundary model

1. [Observed] Owner direction and later digest-bound sign-off are the authority boundary; the candidate itself is not authority.
2. [Observed] The external Butlers Git repository is an untrusted observed-source repository.
3. [Inferred] A source-discovery/allowlist layer selects project-shape paths at an exact revision.
4. [Inferred] A consent and secret-classification gate must precede body ingestion.
5. [Observed] Extracted facts enter one immutable shared `PocModel`, then flow to authenticated human HTML and `GET /api/poc`.
6. [Observed] Walkthrough execution records belong in `.syzygy/governance/records/`; owner judgments belong in `.syzygy/governance/decisions/`, with verified owner-act provenance under RFC7-31.
7. [Observed] Existing authentication/tailnet behavior is inherited, but the candidate matrix leaves relevant RFC5 duties Unknown.

## 2. Threats ranked by likelihood × impact

1. **High × High:** unauthorized or unclassifiable repository-content ingest due absent observation consent and absent concrete security policy.
2. **Medium-High × High:** stored XSS/browser execution from untrusted Markdown, HTML, SVG, links, or copied project text.
3. **Medium × High:** repository escape or host-secret read through unsafe path/symlink handling.
4. **High × Medium-High:** false-completeness poisoning through a self-selected or recursively incomplete manifest.
5. **Medium × Medium-High:** secret leakage into caches, logs, machine output, or walkthrough artifacts because PWB-REQ-003 scans response bytes rather than every sink.
6. **Medium × Medium:** memory/CPU/HTML explosion from large files, graphs, catalogs, cycles, or deeply nested references.
7. **Low × Medium:** prompt injection. The no-LLM-at-observation/render-time design materially reduces this risk, provided indexed content is never later inserted into agent prompts without a separate consent/classification boundary.
8. **Unknown × High:** inherited authentication/audit defects; the candidate explicitly leaves RFC5 admission and audit obligations uncovered.

## 3. Exact contract gaps

- [Observed] Observation consent: RFC5-12 at `consent-egress-secrets.md:77-95`; candidate gap admitted at `CONTRACT-COVERAGE.md:109`.
- [Observed] Concrete classification policy and owner-act provenance: RFC5-16 at `consent-egress-secrets.md:172-192`; absent from PWB-REQ-003.
- [Observed] All-sink secret exclusion: RFC5-16/17 at `consent-egress-secrets.md:172-216`; candidate oracle scans only response bytes at `spec.md:100-102`.
- [Observed] Path/symlink/repository containment: no candidate requirement despite per-repository consent in RFC5-12.
- [Observed] Browser active-content safety: no candidate requirement despite SEC-3’s untrusted-code boundary.
- [Observed] Resource limits and fail-closed truncation: no candidate requirement.
- [Observed] Authenticated-act audit and revocation: left Unknown in `CONTRACT-COVERAGE.md:99-112`; RFC5-25/26 define the duties at `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md:300-331`.
- [Observed] Walkthrough record/judgment homes: PWB-REQ-021/022 require records but do not normatively name the RFC7-31 homes at `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md:171-190`.

## 4. Minimum architectural controls

- Verify exact per-repository observation consent and policy owner-act provenance before the first body read.
- Read exact Git objects only; normalize and contain paths; never follow working-tree symlinks or submodule paths.
- Use a closed source-discovery and extraction-class registry with explicit recursion and lifecycle rules.
- Screen every ingest and sink; keep hash-not-body exclusion provenance.
- Encode output by context; reject active Markdown/HTML/SVG/script/event handlers and unsafe URL schemes.
- Bound source count, bytes, depth, graph size, parse time, and rendered output; disclose limit-triggered Unknowns.
- Preserve the inherited authenticated route/origin controls and audit every authenticated observation act.
- Keep execution records and owner judgments in their RFC7-31 homes with separate provenance verification.

## 5. Control placement

- **Craft-and-care:** concrete secure parsing/escaping standards, path-containment patterns, resource budgets, all-sink secret tests, mutation tests, logging/audit hygiene.
- **Existing RFC obligations:** consent record semantics, owner-act provenance, snapshot inputs, secret-policy admission, audit location, authentication, walkthrough record/judgment homes. No new RFC is needed to obey these.
- **Current candidate spec:** observable refusal before consent/policy verification, Unknown behavior, complete source/item denominators, active-content prohibition, limit-triggered disclosure, and full RFC7-30 evaluation.
- **Future specs only:** multi-project generalization, broader remote access, external egress, additional providers, or production release. None is authorized here.

## 6. V0 security non-negotiables

- No repository body is read without verified observation consent.
- No content enters a model, cache, surface, endpoint, log, or record without the approved classifier.
- No observed-project content executes as browser or host code.
- No path escapes the exact consented Git revision/repository.
- No secret-bearing body appears in provenance.
- No missing, rejected, oversized, or unclassifiable input shrinks a known denominator or becomes success.
- No inherited auth/audit Unknown is represented as satisfied.
- No owner judgment is inferred from tests, page availability, or agent output.

## 7. SECURITY VERDICT

**VERDICT: REVISE**

[Inferred] The intended architecture is directionally fail-closed and suitable for a local POC after repair, but the current candidate does not yet specify enough authority or input-boundary control to be acceptable for implementation.
