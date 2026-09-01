# Raw independent confirmation — PWB state-(1) authority boundary and security

## Review identity

- [Observed] Reviewed commit:
  `8c3b8cb3199efefd580ead08c8866877b7878799`.
- [Observed] Reviewed manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `f5088ca4de9073e55ca11aa061cec73aa6cb478808cd4be95f58ea348204a520`.
- [Observed] Baseline: `bef7f8d23fe63df5150f1ce8fac5bf5d7d3d79e7`.
- [Observed] Review class: authority boundary and security confirmation of
  repaired candidate bytes.
- [Observed] Desired verdict supplied: no.
- [Observed] The prior security review at commit `f31f8315...` and manifest
  `657197d6...` was read only as retired historical input. It did not control
  this confirmation.

## Findings

- BLOCKER: 1
- MAJOR: 0
- MINOR: 0

### 1. BLOCKER — The repaired invalid-case denominators are still not closed

[Observed] PWB-REQ-005 declares `act-record identity` and `provenance state`
to be evaluation inputs at `spec.md:218-220`, but its supposedly exhaustive
159-case table supplies only a **wrong-but-present** act-record identity case
at `spec.md:239` and only five selected state-(1)/state-(2) mechanics at
`spec.md:242`. It supplies no independently decided missing or malformed
act-record-identity cases and no missing, malformed or out-of-vocabulary
provenance-state cases. The table then says there is no other invalid bucket at
`spec.md:246`.

[Observed] RFC3-16(c) additionally defines a state-(1) record as preserving
the exact owner phrase, exact content digest, act record and recording
commit/tag (`governance-homes-and-owner-acts.md:321-330`). PWB-REQ-005's closed
population does not name missing, malformed or mismatched exact-owner-phrase
or recording-commit/tag cases. A commit/tag **alone** is correctly rejected as
a false substitute, but the inverse requirement — retaining the recording
context as part of a valid state-(1) record — is not closed by the table.
Those are record-semantics checks; requiring them would not pretend that the
same-tree record independently proves attendance.

[Observed] The RFC3-16(b) row says its 27 cases are three cases for each of
nine fields, but its one `owner attribution` wrong-but-present slot is also
said to include both another human and a non-human principal
(`spec.md:238`). Those are distinct authority failures and cannot both be
independently decided while occupying one counted case. The stated denominator
therefore does not match its own required fixtures.

[Observed] PWB-REQ-022 inherits the same allegedly exact 43-case common
population at `spec.md:881`; consequently its stated 72 present-invalid cases
inherit every omission and counting ambiguity above. Its own evaluation-input
list also names act-record identity and provenance state at `spec.md:871-873`,
while its `Every present invalid case` closure at `spec.md:885` provides no
additional cases for them.

[Inferred] An implementation could ignore a missing/malformed act-record
identity, accept an unknown or absent provenance-state encoding, omit the
state-(1) owner phrase/recording context, or skip one of the two wrong-owner
classes while satisfying every one of the enumerated 159/72 fixtures and their
required mutations. That is an authority-admission gap at both the
repository-body-read gate and the owner-judgment gate. It fails review-brief
criteria 1, 4, 7, 9 and 15 and prevents a claim that all invalid field classes
are closed.

Minimum precise repair:

- close missing, malformed and wrong/out-of-domain cases for every declared
  act-record identity and provenance-state input;
- close the RFC3-16(c) state-(1) exact-owner-phrase and recording-context
  record semantics without asserting that those tree fields prove attendance;
- count another-human and non-human owner attribution failures as independent
  cases, or define one unambiguous canonical wrong-owner case instead of
  requiring both under one count;
- recompute the PWB-REQ-005 and PWB-REQ-022 denominators and propagate them
  through the signed requirements, design, capability coverage, review brief,
  semantic delta and validation tasks before regenerating the manifest and
  obtaining fresh confirmations.

## Confirmed repaired properties

- [Observed] The exact eleven-row manifest is codepoint-sorted, includes
  unchanged `.openspec.yaml`, and every row digest matches both the worktree
  bytes and `git show 8c3b8cb:<path>`; there were 0 row mismatches.
- [Observed] PWB-REQ-005 admits all eight valid state-(1)/state-(2)
  consent/policy/registry triples, preserves each exact state, and requires
  zero reads, Unknown and contradiction for every invalid case it actually
  enumerates.
- [Observed] Failed, unavailable or indeterminate state-(2) correlation never
  falls back to state (1) in PWB-REQ-005 or PWB-REQ-022.
- [Observed] State (1) carries the exact same-tree-forgeability disclosure on
  the human and machine channels and is never called independently verified.
  Both independent-oracle clauses expressly limit their state-(1) conclusion
  to record semantics and disclosure and disclaim proof of human attendance.
- [Observed] The prior undefined `export` interface has been removed from the
  amended requirements, semantic delta and tasks. PWB-REQ-020 now owns the
  bounded human/machine parity interface and requires multiplicity-preserving
  missing, duplicate, changed, collapsed and wrong-evaluation mutations.
- [Observed] The exact pair/class, observing-project policy, governance-plane
  registry, read-only/empty-write, Git-object containment, inert parsing,
  bounded-resource, secret-screening, authenticated inherited surfaces,
  no-execution and no-egress gates remain conjunctive. The repair did not
  disjoin or remove one of those gates.
- [Observed] Acts remain warrants rather than evidence that a read occurred,
  screening succeeded, admitted content is secret-free, a claim is true, a
  walkthrough happened, comprehension succeeded or a verdict is Observed.
  The walkthrough execution record and owner judgment remain separate.
- [Observed] Later A1 correlation changes only a later evaluation; earlier
  body reads and judgments retain their state-(1) provenance.
- [Observed] The candidate remains inert. It creates no consent, policy,
  registry or judgment act and grants no repository-body read,
  implementation, write, egress, execution, deployment, release, recovery or
  mission authority. A later exact-digest owner sign-off must bind all eleven
  subjects together, and separate effect-specific acts and implementation
  authorization would still be required.

## Validation evidence

- [Observed] `python3 scripts/build_pwb_state1_amendment_manifest.py --check`
  reported `11 artifacts`; its self-test passed population, determinism, byte
  mutation and path mutation.
- [Observed] The dependency generator reported 17 requirements. The coverage
  generator reported 324 accepted clauses represented, and its self-test
  passed exact IDs/dispositions, columns, family/total/repair counts, warrants
  and determinism.
- [Observed] `npx openspec validate polaris-project-wide-butlers-model
  --strict` reported the change valid.
- [Observed] The performed trusted-bootstrap transaction check reported 30
  contract paths, 5 historical PWB paths and 5 owner-act rows frozen and
  valid. Its 10 mutation cases had 0 failures.
- [Observed] `python3 scripts/check_governance.py --selftest` reported 178
  fixtures and 0 failing.
- [Observed] The ordinary governance run examined 825 tracked files and
  reported `32 OK, 19 WARN, 1 FAIL (52 checks)`. The single failure was CG-7h:
  76 predicates examined and the expected five current-PWB digest mismatches
  against the immutable 2026-09-01 historical manifest while no successor act
  exists. That is fail-closed candidate posture, not evidence that this
  amendment is effective.
- [Unknown] No implementation or runtime effect was reviewed. The validation
  scripts establish structural and transaction predicates; they do not close
  the semantic invalid-case omissions in Finding 1.

## Verdict and owner gate

**VERDICT: REVISE**

**OWNER SIGN-OFF MAY NOT BE OFFERED** for commit
`8c3b8cb3199efefd580ead08c8866877b7878799` at manifest
`f5088ca4de9073e55ca11aa061cec73aa6cb478808cd4be95f58ea348204a520`.
Repair the closed invalid populations, regenerate the eleven-row manifest and
obtain fresh independent confirmations of the new exact bytes.
