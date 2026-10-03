# Review brief — N9 machine-channel amendments (PWB and POC halves)

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review. It covers
> two packages in one round; the POC package's own `REVIEW-BRIEF.md` points
> here.

## What you are reviewing

Two amendment packages, each one OpenSpec change against one signed
specification:

1. **PWB half**, `.syzygy/governance/contracts/candidates/pwb-anchor-resolution-amendment/`,
   against `openspec/changes/polaris-project-wide-butlers-model/`
   (PWB-REQ-014): `proposed/*.patch`, the manifest
   `PWB-ANCHOR-RESOLUTION-AMENDMENT-MANIFEST.txt`, `SEMANTIC-DELTA.md`,
   `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`.
2. **POC half**, `.syzygy/governance/contracts/candidates/three-surface-poc-block-provenance-amendment/`,
   against `openspec/changes/three-surface-poc-experience/` (POC-REQ-001 and
   POC-REQ-010): the same five kinds of file, with the manifest
   `THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-MANIFEST.txt`.

And the tooling beside them:

- `scripts/build_pwb_anchor_resolution_amendment.py` (the checking engine and
  the PWB package) and `scripts/build_three_surface_poc_block_provenance_amendment.py`
  (the POC package, driving the same engine);
- the one-entry change to `scripts/build_pwb_class_granular_extraction_amendment.py`
  and `scripts/build_pwb_release_label_amendment.py` that lists the PWB half
  as a pending sibling;
- `scripts/measure_machine_channel_provenance.py` and the record it produced,
  `docs/evidence/n9-machine-channel-provenance-measurement-2026-10-03.json`.

To read the proposed bytes, run each builder with `--diff`, or apply the
patches in a scratch copy. Never apply them in the tree.

## Governing references (read only these)

- **The bead.** `syzygy-u05.9` in `.beads/issues.jsonl` (description,
  acceptance criteria, notes). The notes carry the coordinator's three
  drafting rulings of 2026-10-03; they are not owner acts.
- **The pursuit move.** `docs/pursuits/2026-09-22-vision-pursuit.md`, section
  "N9", and findings S6-F2, S6-F4, S4-F6 and L11-F4 in
  `docs/pursuits/2026-09-22-vision-pursuit-data.json`.
- **The signed subjects.** The two specifications above as they stand at the
  reviewed commit.
- **The contract the PWB half must not cross.** RFC7-3 and RFC7-4 in
  `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`
  (around line 111).
- **The derived-view rule.** PWB-REQ-020's "Derived read-only machine views"
  bullet in the PWB specification.
- **The sign-off scope.**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
  and register row P-84 in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`
  for the open POC route question.
- **The specification bar.** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path, because craft acts 6 and 7 bound it.
- **The delta form.**
  `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md` beside it.
- **The code the figures describe**, for checking claims about today's
  behaviour: `apps/three-surface-poc/src/polaris-narrative.ts`,
  `packages/three-surface-poc-core/src/model.ts`, `work-items.ts` and
  `code-structure.ts`.
- **Doctrine.** VIS-2, VIS-3, VIS-6 and VIS-7 in
  `.syzygy/governance/doctrine/vision.md`.

## Acceptance criteria

1. **The rulings are carried.** The PWB half keeps every narrative unit
   `non-citable`, offers a counted `anchorsResolved` pair instead, and puts
   the RFC7-3 question to the owner without drafting it. The block-to-anchor
   link is stated as already met, not invented. The POC half carries the
   per-row rule against POC-REQ-010 (and POC-REQ-001, the drafter's
   extension; judge whether it belongs). The stale dov.10.1 ordering is
   named as stale.
2. **One category per change.** Each package touches one specification and
   overlaps no other change's category.
3. **The PWB half does not cross RFC7-3 or RFC7-4.** Could any reading of the
   amended text make a narrative unit, or anything derived from the pair,
   resolve as authority?
4. **The predicates are checkable.** "Resolves", the pair, the "one shape",
   and the POC "whole value equals the revision or capture instant" rule each
   have an oracle that an independent checker can run, a denominator, and a
   falsifier limb, and the PWB pair is derivable from the machine answer's
   bytes as PWB-REQ-020 requires of a derived view.
5. **The specification bar.** Each amended requirement still meets CC-SPEC:
   one obligation form, an observable, oracle independence, a falsifier, and
   scenarios its text carries. Is adding SHALL bullets to an
   `event-response` requirement (POC-REQ-001, POC-REQ-010) still one form?
6. **Signed bytes.** No signed byte outside the patches changes; every
   requirement other than the amended ones is byte-identical; every signed
   line of an amended requirement survives except those the builders list as
   replaced.
7. **Honest claims.** Each [Observed] figure is reproducible from the evidence
   record or by the named script at the named commits; the 883 of 902 and
   772,900-byte figures in particular. [Unknown] is used where nothing was
   measured. The packages claim no adoption, authorize no build or read, and
   name what the sign-off change must carry.
8. **Mechanics.**
   - each builder's `--check` and `--selftest` pass, and each selftest mutant
     fails on its own predicate (rule 6);
   - the class-granular and release-label builders' `--check` still pass;
   - the POC identity amendment's builder `--check` still passes.
9. **Plain language.** A fresh reader can restate what changes and what does
   not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7):

- `python3 scripts/build_pwb_anchor_resolution_amendment.py --check`
- `python3 scripts/build_pwb_anchor_resolution_amendment.py --selftest`
- `python3 scripts/build_three_surface_poc_block_provenance_amendment.py --check`
- `python3 scripts/build_three_surface_poc_block_provenance_amendment.py --selftest`
- `python3 scripts/build_pwb_class_granular_extraction_amendment.py --check`
- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/build_three_surface_poc_identity_amendment.py --check`
- `python3 scripts/check_governance.py`
- `python3 scripts/check_spec_reconciliation.py --check`

## Output contract

Write your raw output verbatim to the path the dispatcher names; the filename
ends in `-RAW.md`. Over the first six non-blank lines:

- line 1 is `# ` followed by a title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `PWB manifest SHA-256: ` followed by the lowercase 64-hex sha256
  of the bytes of `PWB-ANCHOR-RESOLUTION-AMENDMENT-MANIFEST.txt` at that
  commit, computed by script (`git show <commit>:<path> | sha256sum`);
- line 4 is `POC manifest SHA-256: ` followed by the same for
  `THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-MANIFEST.txt`;
- line 5 is `PWB verdict: ` and line 6 is `POC verdict: `, each followed by
  exactly one of `CONFIRM`, `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Then add a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note) [PWB|POC|both]`. CONFIRM WITH
EXCEPTIONS means every finding against that package is a `note`.

**Stopping rule, set before this round.** One round only. A notes-only
verdict clears the bytes it read for that package. Any other verdict is
repaired once, no second round is dispatched, and the package goes to the
owner with the repaired bytes unreviewed.
