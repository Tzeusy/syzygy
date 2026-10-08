# Review brief — public-source screening scope, version 3

> **Candidate — binds nothing.** Not a review; carries no verdict.

## What the reviewer is given

CC-REV-1: a fresh context holding the artifact, its governing references and
these criteria.

**Artifact:** every file of
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v3/`
and `scripts/build_public_source_screening_scope_v3.py`. Subject at its
current bytes: the policy file, as the version-2 act left it.

**References:** the policy's own `activeContentClassification`,
`classificationOrder`, `classificationSuccess` and `publicSourceScope`;
`packages/three-surface-poc-core/src/git-object-reader.ts` (the scanner);
`packages/polaris-dossier/src/render.ts`,
`apps/three-surface-poc/src/polaris-generation/dossier-render.ts` and
`draft-preview.ts` (the sinks); `packages/polaris-dossier/src/screen.ts` and
`apps/three-surface-poc/src/polaris-generation/public-source-screening.ts`
(the consumers); the version-2 package and act record.

## Acceptance criteria

1. **Is the diff exactly the stated change?** Run the builder's `--check` and
   `--selftest`. Confirm each patch moves only `policyVersion`,
   `publicSourceScope.activeContent` and `publicSourceScope.inheritedRules`, and
   that each manifest row equals the SHA-256 of that variant's patched file.
2. **Is the base right?** The builder takes only the version-2 row `none`, and
   survives a version-3 act (selftest).
3. **Is the render claim true?** Re-derive every file:line in the delta's "Why"
   section. Is there any sink, in any package or app, where an admitted body
   or a span of it reaches HTML without `escape`, or a page without the CSP?
   State your sweep and its denominator. If one exists, the exemption's
   `renderCondition` must fail closed for it; say whether the words do. Can
   any CSP meet `renderCondition`'s words and still run script or a plugin?
3a. **Is the reading of the affected requirements sound?** The delta's
   "Affected identifiers" section reads REQ-polaris-generation-012 as met by
   `renderCondition` for an exempt body, and REQ-polaris-generation-033 as met
   unchanged. Contradict either reading if the text supports it, and check
   REQ-012's contract warrants, which the delta did not re-read.
4. **Does every detector still run?** Confirm nothing in the patch narrows
   `detectors` or the inherited detector rules, inside code contexts included.
5. **Is the loosening bounded?** Only code-content bodies, only listed
   extensions, never project-documentation. Is `non-web`'s list a defensible
   cut, and is `all` honestly described in the owner packet?
6. **Is the install requirement complete?** The impact ledger names the read
   gate's closed `POLICY_ACT_FORMS` list (`syzygy-fxro`), the battery line,
   the two consumers, the Butlers re-pin and the version-literal pins. Is
   anything missing?
7. **Authority.** No file labels anything accepted or approved; no 64-hex
   digest appears in Markdown outside `reviews/`.

## Out of scope

Whether to perform the act; the consumer code; the recorder (written after a
confirming review).

## Recording

Store the raw verbatim under `docs/reviews/` as
`R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-<n>-RAW.md`, where `<n>` is the round
number. Round 1 is `R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-1-RAW.md` (`REVISE`),
and its findings are repaired in the delta, the ledger and the builder. A
round-2 reviewer checks those repairs against that raw and then applies
every criterion above afresh. **The raw's head is a predicate
a recorder will enforce:** the first four non-blank lines are the title and
exactly

```text
Reviewed commit: <40 hex>
Manifest SHA-256: <SHA-256 of the manifest FILE>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file**, not a row. Print it
with `python3 scripts/build_public_source_screening_scope_v3.py --manifest-digest`.
Number findings `**Finding N — title** (blocking|revise|note)` under a
`## Findings` heading. CONFIRM WITH EXCEPTIONS clears the bytes only when every
finding is a note, dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md`.
