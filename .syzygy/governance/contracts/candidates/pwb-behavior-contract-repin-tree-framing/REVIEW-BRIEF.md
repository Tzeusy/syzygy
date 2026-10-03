# Review brief — PWB behaviour-contract re-pin (tree framing)

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries
> no verdict. No review has been run against this package.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its
governing references and the acceptance criteria.

**The artifact under review:** every file of
`.syzygy/governance/contracts/candidates/pwb-behavior-contract-repin-tree-framing/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, this brief,
`OWNER-DECISION-PACKET.md`, `PWB-EFFECT-REPIN-MANIFEST.txt`, and the two
patches under `proposed/`), plus
`scripts/build_pwb_behavior_contract_repin_tree_framing.py` and the R6
case `pins-after-tree-framing-repin-acts` in
`scripts/check_spec_reconciliation.py`.

**The subjects, at their current bytes:**
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
and
`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`.

**Governing references:**

- The two acts in force:
  `decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md` and
  `decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`,
  with their package `contracts/candidates/pwb-behavior-contract-repin/`
  and `scripts/build_pwb_behavior_contract_repin.py` (whose pure helpers
  the new builder imports).
- `decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md` and
  `contracts/candidates/pwb-tree-framing-amendment/PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt`,
  for the pinned digest and the signing tag.
- `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
  for the signing-path reasoning.
- `decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`,
  for the direction's shape and the fail-closed precedent.
- RFC3-16(a) and RFC3-16(b), read at their defining clause in
  `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`.
- PWB-REQ-005 in
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`.
- `apps/three-surface-poc/src/governance-inputs.ts` and
  `packages/three-surface-poc-core/src/body-read-authority.ts`, for the
  read-gate claims.
- `contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Is the change class right?** The delta says Normative. Is Clarifying
   the better class, and is the reason given wrong?
2. **Are the subjects untouched?** Confirm both files hash to their acts'
   `Exact digest (SHA-256)` lines, that the only proposed change is the
   two patches, and that no act record or prior manifest is edited.
3. **Does the patch change exactly what the delta says, and nothing
   else?** Exactly the `version` and `signedBy` values of
   `governingBehaviorContract`, in each file.
4. **Is the pin right?** It must equal both the `spec.md` row of the
   tree-framing manifest and the current `spec.md`, and `signedBy` must
   name the tag and record that signed those bytes. Re-derive both by
   script (rule 3).
5. **Does the package verify, and does its verification mean anything?**
   Run `python3 scripts/build_pwb_behavior_contract_repin_tree_framing.py
   --check` and `--selftest`. Is each of the selftest's mutations one the
   package would really be wrong about? Name any claim the builder makes
   that no mutant covers.
6. **Does the R6 case prove what it says?** Run
   `python3 scripts/check_spec_reconciliation.py --check` and `--selftest`.
   Confirm that `pins-after-tree-framing-repin-acts` fails when the package
   pins a wrong digest, and that the earlier `pins-after-repin-acts` case
   still holds.
7. **Is the read-gate consequence stated correctly?** From the two source
   files, confirm that an act over either subject makes that role invalid
   and the gate admit nothing. Confirm that direction C, as worded, is
   enough to restore it and no wider than needed.
8. **Is the signing-path reasoning sound?** Is the policy outside Scope A?
   Is the stated reason for keeping the registry on the digest path
   accurate, both to RFC3-16 as quoted and to the gate code, and is it
   labelled with the right epistemic label?
9. **Are the impact ledger's sweeps and rehearsal honest?** Re-run both
   sweeps at the stated base commit and confirm the counts, the
   classification and that no reader of either subject is missing. Repeat
   the rehearsal in a scratch clone and confirm each stated result.
10. **Is the at-adoption list complete?** Is any battery line, registration
    or reader that the acts break missing from the owner packet's
    "At adoption" list?
11. **Does the package avoid quoting any act argument?** No 64-hex digest
    may appear in any Markdown file of the package.
12. **Does the package claim any authority it lacks?** No file may label
    anything accepted, adopted, approved or signed off. Every banner must
    say it binds nothing.

## Out of scope

- Whether to perform either act, or to give direction C. That decision
  belongs to the owner alone.
- The three open questions in the packet. A reviewer may say an answer is
  inconsistent with the package, but does not choose one.

## Recording

Store the raw output verbatim under `docs/reviews/` as
`R-PWB-BEHAVIOR-CONTRACT-REPIN-TREE-FRAMING-RAW.md`, and copy verdict
words exactly. A later round takes the suffix `-<n>-RAW.md`.

**The raw's head is a predicate the recorder enforces.** The first four
non-blank lines must be the title and exactly:

```text
Reviewed commit: <the 40-hex commit the reviewer read>
Manifest SHA-256: <SHA-256 of the FILE PWB-EFFECT-REPIN-MANIFEST.txt>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of this package's manifest **file** at
the reviewed commit, which carries both act arguments as rows. It is not
either row. Print it with
`python3 scripts/build_pwb_behavior_contract_repin_tree_framing.py
--manifest-digest`, or with `sha256sum`. Keep the verdict line within the
first four non-blank lines, with no blank-line padding ahead of it.

Number every finding continuously as
`**Finding N — title** (blocking|revise|note)` under a `## Findings`
heading. The form is the one `scripts/record_versioned_signoff.py` parses.
A CONFIRM WITH EXCEPTIONS clears the bytes only when every finding is a
`note`. Those notes are dispositioned in a sibling
`ROUND-<n>-DISPOSITIONS.md` that names the raw on a `Reviewed record:`
line, never by editing the reviewed files. Any later edit to the package
retires the review (rule 10).
