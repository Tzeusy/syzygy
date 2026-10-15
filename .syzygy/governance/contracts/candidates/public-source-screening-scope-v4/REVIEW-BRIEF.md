# Review brief — public-source screening scope, version 4

> **Candidate — binds nothing.** Not a review; carries no verdict.

## What the reviewer is given

CC-REV-1: a fresh context holding the artifact, its governing references and
these criteria. **Do not read, clone or fetch any target repository (Redis,
Butlers or any other); SEC-2.** Every figure about a target comes from bead
`syzygy-olmr` (`bd show syzygy-olmr`) and from Syzygy's own code and records.

**Artifact:** every file of
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/`
and `scripts/build_public_source_screening_scope_v4.py`. Subject at its
current bytes: the policy file
`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`,
as the version-3 act left it.

**References:** RFC5-14, RFC5-16 and RFC5-17 in
`.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`;
REQ-polaris-generation-025 in
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
and REQ-polaris-generation-035 in
`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`;
VIS-1 and VIS-2 in `.syzygy/governance/doctrine/vision.md`; the policy's own
`detectors`, `matchAction`, `redactionClasses`, `classificationSuccess` and
`publicSourceScope`; `packages/polaris-dossier/src/screen.ts` and
`review.ts`; `packages/three-surface-poc-core/src/content-classification.ts`
(`detectSecrets`); the version-2 owner packet
(`public-source-screening-scope-v2/OWNER-DECISION-PACKET.md`) and the
version-3 act record
(`decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md`).

## Acceptance criteria

1. **Is the diff exactly the stated change?** Run the builder's `--check` and
   `--selftest`. Confirm each patch moves only the values the delta's table
   names, and that each manifest row equals the SHA-256 of that variant's
   patched file (re-derive it yourself).
2. **Is the redaction fail-closed?** Using the four detectors as written in
   the policy, try to construct a body where a secret the detectors match
   reaches a retained line, an admitted span, a marker or the provenance
   record. Consider multi-line matches, the `g` flag's non-overlapping scan,
   CR-only line ends, the re-screen, and the private-key exception. Is one
   guard line honestly described as a mitigation, and is the residual stated
   in both the delta and the packet?
3. **Is the authority claim right?** The delta says RFC5-17 and
   REQ-polaris-generation-025 already permit `redacted-span`, so a policy act
   suffices and no contract amendment or specification delta is needed.
   Contradict this if any clause or requirement requires whole-artifact
   exclusion for this scope. Does REQ-polaris-generation-035's
   "screening-admitted only" accept a span of a retained body?
4. **Is the scope bounded?** Base (Butlers) scope untouched; agent-written
   text still screened whole; active content still whole-body; no class,
   consent or egress rule moved.
5. **Variant `span-guides`.** Is every name on the list plausibly
   project-documentation under RFC5-14's wording, and none governance-text?
   Is the required suffix a sound guard? Are the declined names (SECURITY,
   MANIFESTO, TLS, redis.conf, modules/MODULES.md) declined for the reasons
   their sources state, and is the recommendation honest that the list
   recovers none of the trial's 89 spans?
6. **Is option C's decline sound?** Quote the VIS-2 text and the
   REQ-polaris-generation-035 sentence it rests on.
7. **Is the install requirement complete?** The impact ledger names the act
   readers, the version-literal pins, the recorder battery lines, CG-7e, the
   match-offset need in `detectSecrets`, the two screens and the call sites.
   Is anything missing? State your sweep and denominator.
8. **Is the owner packet plain and single-question?** One binding ask, words
   that name a manifest row, a stated recommendation and its cost.
9. **Authority hygiene.** No file labels anything accepted or approved; no
   64-hex digest appears in the package Markdown.

## Out of scope

Whether to perform the act; the install code; the recorder (written after a
confirming review).

## Recording

Store the raw verbatim under `docs/reviews/` as
`R-OLMR-SCREENING-SCOPE-V4-<n>-RAW.md`. **The raw's head is a predicate a
recorder will enforce:** the first four non-blank lines are the title and
exactly

```text
Reviewed commit: <40 hex>
Manifest SHA-256: <SHA-256 of the manifest FILE>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file**, not a row. Print it
with `python3 scripts/build_public_source_screening_scope_v4.py --manifest-digest`.
Number findings `**Finding N — title** (blocking|revise|note)` under a
`## Findings` heading. Stopping rule (owner, 2026-09-26): a round whose
findings are all notes clears these bytes, with the notes dispositioned in a
sibling `ROUND-<n>-DISPOSITIONS.md`; a REVISE is repaired once and then
reported to the owner before any further round.
