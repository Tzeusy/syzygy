# Review brief — public-source screening scope (round 3)

> **Candidate — binds nothing.** Not a review; carries no verdict. Rounds 1
> and 2 returned REVISE; this is the round-3 brief.

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
   digest may appear in any Markdown file of the package outside `reviews/`
   (retained raws carry the manifest digest in their head, by contract).

9. **Does each round-1 repair hold, and did one introduce a defect?** The raw
   is `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-1-RAW.md` (REVISE: findings 1,
   3 to 6 revise; 2, 7 to 9 notes). Re-derive each count, line and quote from
   the bytes. Specifically: the pin table of the ledger against a fresh sweep
   (is it complete?); the version label distinct from PR #120's; the
   asymmetric ordering; one reading of indeterminate; active content
   unchanged; the Q2/Q7 narrowing disclosed.

10. **Does each round-2 repair hold, and did one introduce a defect?** The raw
    is `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-2-RAW.md` (REVISE: findings 1
    and 2 revise; 3 to 8 notes). Specifically: run
    `python3 scripts/simulate_public_source_screening_scope_act.py --tests`
    yourself and compare its failing checks and literal hits with the ledger
    tables (F1); check that `targetMetadataRule` admits exactly what the
    confirmed admission egress record's generated table sends for sources and
    nothing the pipeline does not send (F2); the stale docstring and comment,
    the version-literal sentence and the one-way sibling clause (F3 to F5);
    the run-profile carrier as an open question (F6); Q6 naming `.jsx`/`.tsx`
    and the unclosed-backtick exclusion (F7); this criterion's scoping (F8).
    Population: findings 1 to 8; revise 1 and 2; notes 3 to 8.

## Out of scope

Whether to perform the act; the extension list's membership beyond its
labelling; PR #120's contents.

## Recording

Store the raw verbatim in this package's `reviews/` directory as
`R-PUBLIC-SOURCE-SCREENING-SCOPE-3-RAW.md` (a re-issue is a further
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

11. **Is the exclusion-reason set structural?** `targetMetadataRule` lists no
    reason and names `GENERATION_EXCLUSION_REASONS` in `generation-source.ts`.
    That constant is [Inferred] not yet in code: run
    `python3 scripts/build_public_source_screening_scope.py --check` and
    confirm it reports the package current and then "not ready for an act"
    (exit 1); `--pending-symbol` downgrades that to a note so the manifest
    digest can be printed. Confirm the symbol must exist before the act, that
    the reader fails closed on an absent, unexported, computed, empty or
    repeating set (selftest), and that packet Q7 now asks only to confirm the
    set.

12. **Does each round-3 repair hold, and did one introduce a defect?** The raw
    is `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-3-RAW.md` (REVISE: findings 1
    and 2 revise; 3 to 7 notes) and the repairs are in
    `ROUND-3-DISPOSITIONS.md`. Specifically: the reader sets comments and
    strings aside before matching (F1; the selftest fixtures and mutants in
    `exclusion_reasons`' battery); `reasonRule` no longer says the set cannot
    differ from what the generator emits (F2, patch); Q7 names reasons that
    originate outside generation-source.ts (F3); the redundant pre-check now
    has its own messages and fixtures (F4); the ledger's record figure carries
    its predicate and own-package count (F5); the delta's rule count (F6); the
    opaque `sourceId` sentence in the rule (F7). Re-derive the record count
    and the manifest digest yourself.
