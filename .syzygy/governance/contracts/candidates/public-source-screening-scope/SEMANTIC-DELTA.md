# Semantic delta — public-source screening scope

> **Candidate — binds nothing.** Drafted 2026-10-03 for gap 12 of
> `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md`. Effect comes only
> from an owner `approve-policy` act over the exact proposed bytes. No
> repository body was read to draft it, and no act is recorded here. Rounds 1
> and 2 returned REVISE (raws retained verbatim under `reviews/`); this is the
> round-3 text.

## Class

Normative. It adds a new scope with new authority (a second observed-source
class, a narrow network route, a storage place for raw bodies), changes no
existing key and does not touch the Butlers scope.

## Subject and change

Subject: the secret-classification policy of `project:syzygy`
(`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`).
The proposed bytes add one top-level object, `publicSourceScope`, directly after
`scope`, and move `policyVersion` to the next minor with its own label,
`public-source-candidate.1`, because PR #120 proposes `1.2.0-candidate.1` for
different bytes. The diff is generated from
the file on disk by `scripts/build_public_source_screening_scope.py`, so a
different base only needs `--write` to regenerate; it is never hand-edited.

| Part of `publicSourceScope` | What it says |
|---|---|
| Observed repositories | exactly those named by an effective observation consent for `(project:syzygy, repository:<id>)`; the policy names no repository, so a target is admitted or withdrawn without editing it |
| Authorization mode | `owner-trusted-bootstrap` only (state (1), packet Q5) |
| Source admission | all tracked blobs at the commits the consent lists; symbolic links, submodule entries and anything outside those root trees are not admitted; the base denied-path rules apply unchanged; strict UTF-8 |
| Classification | into RFC5-14 classes `code-structure`, `code-content` and `derived-composites`; never `work-history`; `code-content` by a closed list of source extensions, compared case-sensitively on the final path segment [Inferred proposal], so configuration written in a listed extension is `code-content`; no extractor runs and the body is admitted as whole-blob spans. Every other blob is indeterminate, with one reading: unclassifiable, excluded from reading and from egress (fail closed), hash-not-body, never stored or rendered, its path and size still `code-structure` |
| Instruction text | one closed rule: the text produced by exactly `promptForStage` and `stageSchema` is `code-content` of `project:syzygy`; nothing else of Syzygy's repository is classified |
| Classification basis | a class is decided at the runtime check from the origin of the content, never from a field name; the field-level table in a public-target egress record gates which fields may be carried and confers no class (carried from the admission package's round-7 notes 2 and 4) |
| Run profile | classified only as the values of the code-declared `DOSSIER_READER_QUESTIONS` and `DOSSIER_REQUESTED_ASSETS` in `dossier-profile.ts` (PR #259), selected by a profile id a request carries (the id and its carrier are an open owner question); any other origin is unclassified and not carried. [Observed] the base pipeline types `readerQuestions` as unknown and validates only `requestedAssets`; the typed validation is not in code and is not assumed |
| Target metadata | `code-structure`, exactly the fields of the pipeline's `sourcePopulation` entry (source id, classification basis, exclusion flag and, for an excluded source only, a reason that is a member of the closed set held by the exported constant `GENERATION_EXCLUSION_REASONS`, which the rule names and does not list), which the confirmed admission egress record's generated table sends as `target-metadata`. The field list is read from `pipeline.ts` and the reason set from that constant by the builder, not typed, and the builder fails closed while the constant is absent; no body, content digest or policy detail, and no path of an excluded source; an excluded source's `sourceId` is an opaque identifier not derived from its path or body ([Inferred]: enforced only by the reader implementation, which the generator's lane is asked to write that way, not by these bytes) |
| Detectors and matches | every base detector applies unchanged, including inside inert code contexts; a match excludes the whole artifact with hash-not-body provenance |
| Active content | no loosening: the base rule and the active-content condition of `classificationSuccess` apply unchanged to every admitted body. [Inferred] A source file embedding markup-like bytes outside a valid inert code context is withheld; the first run measures how many |
| Access boundary | the base boundary; the `networkEgress` boolean stays false as the base reads it, and exactly two routes (the shallow by-commit fetch and the registered provider route) are carried beside it |
| Raw bodies | storage only in a run directory outside git; logging and machine response `never`; rendering only in a local editorial draft; external egress only for content this scope classifies and under a separate egress consent |
| Self reference | a target's own policy, configuration or documentation text is never an input (RFC3-30) |

## What it does not change

The Butlers `scope`, every base key and every detector, and every act already
performed on this policy. It admits no repository, grants no read or egress by
itself, and defines no class: `project-documentation` is the subject of a
separate RFC-0005 amendment and appears nowhere in these bytes, so prose stays
indeterminate until a later policy version maps it.

## The egress template's phrase, resolved

The admission package's egress template relies on "the generator-authored
request-text rule of the public-source screening scope". No rule is named that
here; the rules are `instructionTextRule`, `runProfileRule` and
`targetMetadataRule`: three rules for the four populations the generated
carried-content table names, because the envelope-control labels (prompt and
response-schema versions) are produced by the two `instructionTextRule`
symbols. `classificationBasis` says the table gates fields and confers no class.

## Narrowing of the owner's answers (Q2, Q7)

The owner answered Q2 "all but work-history" and Q7 "T1 (requests) runs on code
and specs only". This scope narrows both. No closed rule here maps
specification and design documents to `governance-text` or committed reports to
`evidence-content`, and guessing one from a path or an extension would be an
unreviewed class assignment. So `governanceTextPaths` and `evidenceContentPaths`
stay empty, those documents are indeterminate (excluded from reading and
egress), and for T1 "specs" reduces to what sits in a listed source extension.
The packet asks the owner about this as Q5; it does not assume consent.

## Reconciliation with PR #120

PR #120 (self-observation acts) also adds a top-level scope object to this
file and moves the minor version. The two are independent and neither contains
the other, and `inheritedRules` now says that a sibling scope's own rules do
not govern this scope. The ordering is **asymmetric**:

- **PR #120 first.** This package needs only `--write` against the performed
  bytes (simulated by the round-1 reviewer): the version label follows from the
  new base, and the package is re-reviewed before it is offered.
- **This package first.** PR #120's builder hard-codes its current and proposed
  versions (`1.1.0-candidate.1` and `1.2.0-candidate.1`), and its digest-bound
  consent prose names `1.2.0-candidate.1`. It then needs code edits and a
  changed consent record before its own `--write` can work, and a fresh review.

The packet recommends PR #120 first when both are signed in one sitting, and
this package alone otherwise, with PR #120 regenerated later.

## Read-gate consequence

[Observed] The Butlers read gate refuses on any byte change, before it looks at
the version: `exact-digest-wrong` (`body-read-authority.ts:444`) compares the
act's bound digest with the artifact as read, and `policy-version-wrong` (:641)
is reached only after. So leaving the version unchanged would not avoid the
refusal; it would only mislabel it. An act over the proposed bytes therefore
makes the gate refuse the policy until every pin below is re-pointed in the same
change, as the 2026-10-02 re-pin did without a version bump. The impact ledger
enumerates them. The packet asks for that continuation as a question.

## The instruction-text rule

[Observed] `promptForStage` (`prompts.ts:29`) takes no target input and
imports nothing, and `provider-draft.ts` imports only `node:util` and a type, so
the two named symbols yield only Syzygy-authored text and the rule is closed and
sufficient for RFC5-15 part 2 at these bytes. It binds symbols and code-declared
version labels, not a digest: whatever those symbols later embed would be
`code-content` by this rule. Recorded for the next policy version.
