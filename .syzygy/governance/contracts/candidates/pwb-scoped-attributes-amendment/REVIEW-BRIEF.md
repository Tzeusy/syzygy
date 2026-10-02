# Review brief — PWB page-level evaluation stamp (lane B, narrowed)

Review the exact candidate commit and the manifest without authoring context.
The candidate is inert and must not be treated as an act. The proposed bytes
are the patches under `proposed/` over the current tree, printed by
`python3 scripts/build_pwb_scoped_attributes_amendment.py --diff`; nothing in
`openspec/` or the accepted contract changes on the reviewed commit. Judge the
bytes on their own; earlier broader drafts and their reviews are history under
`docs/reviews/`.

Required baseline: `VIS-1`, `VIS-2`, `VIS-4`, `VIS-7`; `CC-REV-2`, `CC-REV-4`,
`CC-REV-6`, `CC-TEST-5`, `CC-TEST-6`; `RFC7-16`, `RFC7-33` and `RFC7-34`;
`RFC6-14`; `PWB-REQ-007`, `-014`, `-016` and `-020` in the signed package; the
sibling contract package
`.syzygy/governance/contracts/candidates/rfc7-scoped-values-successor/`.

Review criteria:

1. **One value only.** No reading of the amended text lets a scope carry any
   tuple field other than the evaluation identity, a claim's identity, or the
   `non-citable` / `presentation-artifact` pair. Try to construct one.
2. **No hiding.** A claim naming a different evaluation than the stamp cannot
   render with the stamp's value; a stamp is emitted only when every claim
   under it has that value in the machine answer; the falsifier and the
   `stamp-hidden` mutant class catch the breach.
3. **Precedence.** The stamp never overrides a claim's own evaluation identity.
4. **Oracles.** PWB-REQ-007 and -020 each keep an independent oracle that
   expands the stamp with its own statement of the rule and imports no
   rendering code; both denominators are still reported.
5. **Non-visual.** The stamp's value is recoverable as text, before the claims
   it covers (PWB-REQ-016, RFC7-34), with a falsifier.
6. **Contract delta.** The RFC7-33 patch is the smallest change that makes the
   spec text lawful, applies identically to both mirrors, equals the contract
   package's patch, and leaves the non-citability sub-clause in force; the
   interactive surface is defined by delivery, and the endpoints, exports and
   copy functions carry the evaluation identity on every claim.
7. **Unchanged boundaries.** The delta's "does NOT change" list is accurate
   against the patches.
8. **Saving.** The packet's figure is labelled `[Inferred]`, shows its
   arithmetic and sources, and says plainly that the page stays over the
   1,400,000-byte target.
9. **Mechanics.** The manifest hashes exactly the post-apply bytes of the
   eleven subjects; the builder's `--check` and `--selftest` fail closed; the
   candidate binds nothing by merge.

The raw review states the exact reviewed commit, the manifest SHA-256 of the
manifest file, one exact verdict (`CONFIRM`, `CONFIRM WITH EXCEPTIONS`,
`REVISE`), and every finding with the file and line it anchors to. Number
findings continuously from 1 under a `## Findings` heading as
`**Finding N — <title>** (blocking|revise|note)`.
