# Review brief — public-source screening scope, version 2 (round 1)

> **Candidate — binds nothing.** Not a review; carries no verdict.

## What the reviewer is given

CC-REV-1: a fresh context holding the artifact, its governing references and
these criteria.

**Artifact:** every file of
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v2/`
and `scripts/build_public_source_screening_scope_v2.py`. Subject at its
current bytes: the policy file named in the delta, after version 1.

**References:** RFC5-12 to RFC5-17 at their defining clauses, and the RFC5-14
class text in the PR #257 amendment; the version-1 package
`public-source-screening-scope` (its builder, delta and manifest); the policy's
own `activeContentClassification`, `rawBodyHandling` and
`classificationSuccess`.

## Acceptance criteria

1. **Is the diff exactly the stated change?** Run
   `python3 scripts/build_public_source_screening_scope_v2.py --check`,
   `--selftest` and `--ready --pending-prerequisite`. Confirm the patch moves
   `policyVersion` and changes only `classesClassified`, `rules`,
   `indeterminate` and the new `prerequisite`, and that the manifest row equals
   the SHA-256 of the patched file.
2. **Is the base right?** The patch must be the same whether the policy on disk
   is the pre-version-1 bytes or the version-1 bytes (selftest). Confirm the
   version-1 manifest row is what the builder checks against.
3. **Does the rule follow RFC5-14?** Read the class text: the rule places a
   file by declared path only; it does not let a name or a file's own claim
   place it; a file it cannot place is indeterminate. Is the rule closed and
   literal? Do the three path rules overlap, and does any file match two? Is
   there a case-folding or Unicode hazard (the fixtures include dotted-capital-I
   and Kelvin-sign names that must not match)?
4. **Is the screening unchanged?** Diff every key outside `contentClassification`
   and `prerequisite` against version 1; confirm detectors and active content
   still apply to these bodies.
5. **Is the prerequisite real?** Confirm the scope carries the condition as
   data, `--ready` checks the installed RFC-0005 text and the version-1 act, and
   a consent without the class still permits no egress.
6. **Is `design/` rightly left out?** Check against RFC5-14 that design and
   specification text is `governance-text`, and that nothing here maps it.
7. **Are the claims in the owner packet true?** For each sendable and withheld
   example, run the reference reader in the builder (the fixtures).
8. **Authority.** No file may label anything accepted or approved; no 64-hex
   digest may appear in Markdown outside `reviews/`.

## Out of scope

Whether to perform the act; the read-gate re-pin (see packet Q2); the
RFC-0005 amendment itself.

## Recording

Store the raw verbatim in this package's `reviews/` directory as
`R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-1-RAW.md` (a re-issue is a further
`-RAW.md`). **The raw's head is a predicate a recorder will enforce:** the first
four non-blank lines are the title and exactly

```text
Reviewed commit: <40 hex>
Manifest SHA-256: <SHA-256 of the manifest FILE>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file**, not its row. Print
it with `python3 scripts/build_public_source_screening_scope_v2.py --manifest-digest --pending-prerequisite`.
Number findings `**Finding N — title** (blocking|revise|note)` under a
`## Findings` heading. CONFIRM WITH EXCEPTIONS clears the bytes only when every
finding is a note, dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md`.
