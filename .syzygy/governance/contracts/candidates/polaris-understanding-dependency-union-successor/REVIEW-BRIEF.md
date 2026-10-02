# Review brief — Polaris understanding dependency-union successor

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries
> no verdict. No review has been run against this package.

## What the reviewer is given, and nothing else

**The artifact under review:** every file of
`.syzygy/governance/contracts/candidates/polaris-understanding-dependency-union-successor/`
(`SUCCESSOR.json`, `SUCCESSOR-MANIFEST.txt`, the one proposed file under
`proposed/`, `OWNER-DECISION-PACKET.md` and this brief), plus
`scripts/build_polaris_dependency_unions.py` and the R7 case
`union-after-successor-act` in `scripts/check_spec_reconciliation.py`.

**The subject, at its current bytes:**
`openspec/changes/polaris-manifesto-understanding-amendment/GOVERNING-DEPENDENCIES.md`.

**Its source:**
`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`.
For comparison, the base change's `spec.md` and `GOVERNING-DEPENDENCIES.md`
under `openspec/changes/polaris-manifesto-generation/`.

**Governing references:**

- `decisions/POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md` (the act
  that binds the subject today) and its package
  `contracts/candidates/polaris-understanding-readability-successor/`.
- `scripts/readability_successor.py` (the recorder) and
  `scripts/record_polaris_understanding_adoption.py`, for the
  recording-prerequisite claims.
- `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, for
  the signing-path claim.
- `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`
  (change classes).

## Acceptance criteria

1. **Is the regeneration exact?** Recompute the union of every warrants
   block in the amendment's `spec.md` by your own method. Does the
   proposed file carry exactly that union, in the signed file's format
   (section order, sort order, separator, empty-class sentence, trailing
   blank line)?
2. **Does the proposal change only what it says?** Exactly one line,
   `CC-REV-8` added to policies. Check with `--diff`.
3. **Is the package internally consistent?** Run `python3
   scripts/readability_successor.py --all --check`. The package must read
   `candidate-unperformed`, the predecessor must equal the subject's
   current digest and the act-in-force row, and the manifest must be its
   regeneration.
4. **Does the builder verify, and does its verification mean anything?**
   Run `python3 scripts/build_polaris_dependency_unions.py --check` and
   `--selftest`. Are the two renderer-fidelity fixtures real evidence of
   format fidelity? Is each mutation one the builder would really be wrong
   about? Name any claim no mutant covers.
5. **Does the R7 case prove what it says?** Run
   `python3 scripts/check_spec_reconciliation.py --selftest`. Confirm that
   `union-after-successor-act` fails if the proposed union omits
   `CC-REV-8`, and that requiring R2 (and only R2) to fail matches R2's
   stated design.
6. **Is the change class right?** The packet claims Editorial. Test the
   claim.
7. **Are the recording prerequisites stated correctly and completely?**
   Would recording without them turn the battery red as described? Is
   anything missing?
8. **Is the signing path right?** Is a Polaris generation amendment file
   outside Scope A?
9. **Does the packet's quoted phrase carry the current manifest digest,
   and does any file claim authority it lacks?**

## Out of scope

Whether to sign off. That decision belongs to the owner alone.

## Recording

Store the raw output verbatim under `docs/reviews/` as
`R-POLARIS-UNDERSTANDING-DEPENDENCY-UNION-SUCCESSOR-1-RAW.md`, and copy
verdict words exactly. A later round increments the number.

**The raw's head is a predicate the recorder enforces**
(`readability_successor.py`, `validate_pins`). In the whole raw there must
be exactly one line `Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>`
and exactly one line `Manifest-file SHA-256: <digest>`. Write no second
line beginning `Verdict:` or `Manifest-file SHA-256:` anywhere, including
in quoted material. The digest is the sha256 of `SUCCESSOR-MANIFEST.txt`
at the reviewed commit; the packet's phrase quotes the same value. Put
those two lines and `Reviewed commit: <40 hex>` directly under the title,
in the form of
`docs/reviews/R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-2-RAW.md`.
Only CONFIRM or CONFIRM WITH EXCEPTIONS can be recorded.

Number findings as `**Finding N — title** (blocking|revise|note)` under
`## Findings`. A CONFIRM WITH EXCEPTIONS clears the bytes only when every
finding is a `note`. Notes are answered in a sibling record
(`REVIEW-NOTES.md`, as the readability package did), never by editing the
reviewed files. A later edit to the proposed file or the manifest retires
the review (rule 10).
