# Review brief — public-source screening scope

> **Candidate — binds nothing.** Not a review; carries no verdict.

## What the reviewer is given

CC-REV-1: a fresh context holding the artifact, its governing references and
these criteria.

**Artifact:** every file of
`.syzygy/governance/contracts/candidates/public-source-screening-scope/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, this brief, `OWNER-DECISION-PACKET.md`,
`PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt`, `proposed/`) and
`scripts/build_public_source_screening_scope.py`. Subject at its current bytes:
the policy file named in the delta.

**References:** RFC3-30; RFC5-12 to RFC5-17 at their defining clauses;
REQ-polaris-generation-025 in
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`;
the policy's own `scope`, `accessBoundary`, `sourceAdmission`,
`activeContentClassification`, `rawBodyHandling` and `classificationSuccess`;
`apps/three-surface-poc/src/governance-inputs.ts` and
`packages/three-surface-poc-core/src/body-read-authority.ts`; the public-repo
admission package's egress template (draft PR #215), for the instruction-text
rule it relies on; and the owner answers of 2026-10-03 (Q2, Q3, Q6, Q7).

## Acceptance criteria

1. **Is the diff exactly the stated change?** Run
   `python3 scripts/build_public_source_screening_scope.py --check` and
   `--selftest`. Confirm the patch moves `policyVersion` and adds
   `publicSourceScope` and nothing else, and that the manifest row equals the
   SHA-256 of the patched file.
2. **Does the scope contradict a base rule it says it inherits?** Check each
   inherited rule, especially `classificationOrder` and `classificationSuccess`
   which name the PWB grammar, and the active-content rule.
3. **Is each loosening stated and bounded?** Network egress, raw-body storage
   and rendering are the substantive loosenings. Does the scope permit more
   than packet Q3 and Q6 and the egress template need?
4. **Is the classification sound under RFC5-14?** The class is determined by a
   rule, not asserted by the composing step; `work-history` is never
   classified; `project-documentation` is absent; an indeterminate file fails
   closed. Is the instruction-text rule closed and sufficient for RFC5-15 part 2?
5. **Is the extension list labelled honestly?** It is an [Inferred] proposal.
6. **Does the read-gate consequence hold?** Verify from the two source files
   that a bumped version without a re-point fails closed for Butlers.
7. **Are the sweeps honest?** Re-run Sweep 1 and 2 with the stated predicates.
8. **Authority.** No file may label anything accepted or approved; no 64-hex
   digest may appear in any Markdown file of the package.

## Out of scope

Whether to perform the act; the extension list's membership beyond its
labelling; PR #120's contents.

## Recording

Store the raw verbatim in
the docs/reviews directory as `R-PUBLIC-SOURCE-SCREENING-SCOPE-RAW.md` (a re-issue is a second
`-RAW.md`). **The raw's head is a predicate the recorder enforces:** the first
four non-blank lines are the title and exactly

```text
Reviewed commit: <40 hex>
Manifest SHA-256: <SHA-256 of the manifest FILE>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file**, not its row. Print
it with `python3 scripts/build_public_source_screening_scope.py --manifest-digest`.
Number findings `**Finding N — title** (blocking|revise|note)` under a
`## Findings` heading. CONFIRM WITH EXCEPTIONS clears the bytes only when every
finding is a note, dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md`.
