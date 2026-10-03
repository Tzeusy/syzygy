# Review brief — PWB opening-index and accessible-name amendments

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

Two amendment packages against the signed PWB specification,
`openspec/changes/polaris-project-wide-butlers-model/`, reviewed in one
round:

- **A, opening index** (PWB-REQ-010), in
  `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`;
- **C, accessible names** (PWB-REQ-016), in
  `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/`.

Each package has two patches under `proposed/` (the spec patch, authored,
and the `GOVERNING-DEPENDENCIES.md` patch, regenerated), a manifest,
`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md`. The
tooling under review is:

- the shared engine `scripts/pwb_requirement_amendment.py`;
- the builders `scripts/build_pwb_opening_index_amendment.py` and
  `scripts/build_pwb_accessible_name_amendment.py`;
- the pending-sibling entries added to
  `scripts/build_pwb_class_granular_extraction_amendment.py` and
  `scripts/build_pwb_release_label_amendment.py`.

To read the proposed bytes, run each builder with `--diff`, or apply the
patches in a scratch copy. Never apply them in the tree.

## Governing references (read only these)

- **The bead and its narrowing.** `bd show syzygy-u05.12` (read-only): its
  description, and the 2026-10-03 coordinator note that narrowed it to
  slices A and C and set B and D aside.
- **The pursuit finding.** `docs/pursuits/2026-09-22-vision-pursuit.md`,
  section "N12".
- **The signed subject.** The eleven artifacts each manifest names, at the
  reviewed commit. The requirements amended are PWB-REQ-010 and PWB-REQ-016;
  read PWB-REQ-012 (copy rules), PWB-REQ-020 (parity) and PWB-REQ-021 (the
  walkthrough record) for what the amendments must not cross.
- **The contract.** RFC7-30, RFC7-31 and RFC7-34 in
  `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`.
- **The parent requirement.** POC-REQ-061 in
  `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`.
- **The sign-off scope.**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **The specification bar.** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path, because craft acts 6 and 7 bound it.
- **The delta form.**
  `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md` beside it.
- **The checker C describes.** `apps/three-surface-poc/src/polaris-accessibility.ts`,
  for checking the delta's claims about today's behaviour.
- **Doctrine.** VIS-1, VIS-3 and VIS-7 in `.syzygy/governance/doctrine/vision.md`.

## Acceptance criteria

1. **No verdict, no score.** Nothing in A lets a machine decide, score or
   imply that a cold-open prompt is answered (RFC7-31; PWB-REQ-021's
   "never a verdict or proof of comprehension"). Each index target is
   declared by the specification, not chosen by a run. The offsets enter no
   epistemic tuple, parity family, walkthrough record or readiness arm.
2. **Scope.** A changes only PWB-REQ-010 and C only PWB-REQ-016. Neither
   crosses into the Three-Surface POC specification. Slices B and D are not
   drafted, and each packet puts them to the owner with clause reasoning.
3. **The specification bar.** Each amended requirement still meets CC-SPEC:
   one obligation form, scope, a sweep oracle with a denominator, an
   observable, oracle independence, a falsifier, and scenarios its text
   carries. Each new obligation has an oracle limb, a falsifier limb and a
   scenario. A's index rows obey PWB-REQ-012, and their identities match
   PWB-REQ-021's nine in order.
4. **Signed bytes.** No signed byte outside the patches changes. Every other
   requirement is byte-identical, and every signed line of the amended
   requirement survives except those each builder lists as `replaced`.
5. **Honest claims.** Each [Observed] claim is checkable at the commit it
   names. No figure is quoted from an untracked capture; current figures
   are [Unknown]. The packages claim no adoption, authorize no build or
   read, and name the packages they collide with.
6. **Mechanics.**
   - Each builder's `--check` and `--selftest` pass, and each selftest
     mutant fails on its own predicate (rule 6).
   - The dependency file equals regeneration, and contract coverage
     regenerates byte-identical over the proposed bytes.
   - The four pending PWB packages' spec patches compose in either order.
   - The class-granular and release-label builders' `--check` still pass.
7. **Plain language.** A fresh reader can restate what changes and what
   does not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7):

- `python3 scripts/build_pwb_opening_index_amendment.py --check`
- `python3 scripts/build_pwb_opening_index_amendment.py --selftest`
- `python3 scripts/build_pwb_accessible_name_amendment.py --check`
- `python3 scripts/build_pwb_accessible_name_amendment.py --selftest`
- `python3 scripts/build_pwb_class_granular_extraction_amendment.py --check`
- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/check_governance.py`
- `python3 scripts/check_spec_reconciliation.py --check`

## Output contract

One review, two raw files, one per package, because each sign-off binds one
package's review head. Write each verbatim to the path the dispatcher names;
each filename ends in `-RAW.md`. Over the first four non-blank lines of each:

- line 1 is `# ` followed by a title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of that package's manifest file
  (`PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt` or
  `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`) at that commit, computed by
  script (`git show <commit>:<path> | sha256sum`). It is never a row inside
  the manifest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Then add a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS means
every finding is a `note`. A finding about the shared engine, or about both
packages, goes in both raws.

**Stopping rule, set before this round.** One round only. For each package,
a notes-only verdict, meaning `CONFIRM` or `CONFIRM WITH EXCEPTIONS` with
every finding a note, clears the bytes it read; its notes are dispositioned
in a sibling `ROUND-1-DISPOSITIONS.md` and the package is not edited. Any
other verdict leaves that package unedited: no second round is dispatched,
and its findings go to the owner.

**Applied after the round (2026-10-03).** Both packages returned `REVISE`.
The coordinator then directed that a first-round `REVISE` on a new draft
is repaired once, with each finding and its repair recorded, and no round
2 is run; the rule above, which said the packages stay unedited, was
written for a confirmation round and was not applied. Each package's
`ROUND-1-DISPOSITIONS.md` records the repairs. The repaired bytes are
unconfirmed.
