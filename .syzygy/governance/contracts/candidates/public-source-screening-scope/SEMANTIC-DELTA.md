# Semantic delta — public-source screening scope

> **Candidate — binds nothing.** Drafted 2026-10-03 for gap 12 of
> `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md`. Effect comes only
> from an owner `approve-policy` act over the exact proposed bytes. No
> repository body was read to draft it, and no act is recorded here.

## Class

Normative. It adds a new scope with new authority (a second observed-source
class, a narrow network route, a storage place for raw bodies), changes no
existing key and does not touch the Butlers scope.

## Subject and change

Subject: the secret-classification policy of `project:syzygy`
(`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`).
The proposed bytes add one top-level object, `publicSourceScope`, directly after
`scope`, and move `policyVersion` to the next minor. The diff is generated from
the file on disk by `scripts/build_public_source_screening_scope.py`, so a
different base only needs `--write` to regenerate; it is never hand-edited.

| Part of `publicSourceScope` | What it says |
|---|---|
| Observed repositories | exactly those named by an effective observation consent for `(project:syzygy, repository:<id>)`; the policy names no repository, so a target is admitted or withdrawn without editing it |
| Authorization mode | `owner-trusted-bootstrap` only (state (1), packet Q5) |
| Source admission | all tracked blobs at the commits the consent lists; symbolic links, submodule entries and anything outside those root trees are not admitted; the base denied-path rules apply unchanged; strict UTF-8 |
| Classification | into RFC5-14 classes `code-structure`, `code-content` and `derived-composites`; never `work-history`; `code-content` by a closed list of source extensions [Inferred proposal]; every other blob, including README, guides, LICENSE and configuration, is indeterminate and refused egress |
| Instruction text | one closed rule: the text produced by exactly `promptForStage` and `stageSchema` is `code-content` of `project:syzygy`; nothing else of Syzygy's repository is classified |
| Detectors and matches | every base detector applies unchanged, including inside inert code contexts; a match excludes the whole artifact with hash-not-body provenance |
| Active content | the base rule keeps governing Markdown and other prose rendered as markup; every other admitted file is untrusted text, never interpreted as markup |
| Access boundary | the base boundary with `networkEgress` permitted for exactly two routes: the shallow by-commit fetch and the registered provider route |
| Raw bodies | storage only in a run directory outside git; logging and machine response `never`; rendering only in a local editorial draft; external egress only for content this scope classifies and under a separate egress consent |
| Self reference | a target's own policy, configuration or documentation text is never an input (RFC3-30) |

## What it does not change

The Butlers `scope`, every base key and every detector, and every act already
performed on this policy. It admits no repository, grants no read or egress by
itself, and defines no class: `project-documentation` is the subject of a
separate RFC-0005 amendment and appears nowhere in these bytes, so prose stays
indeterminate until a later policy version maps it.

## Reconciliation with PR #120

PR #120 (self-observation acts) also adds a top-level scope object to this
file and moves the minor version. The two are independent and neither
contains the other. Whichever act is performed second is regenerated against
the other's performed bytes with `--write`, then re-reviewed, before it is
offered; the generator follows the new base version on its own. If PR #120's
act lands first, the version this package proposes becomes the one after it.

## Read-gate consequence

[Observed] The Butlers read gate pins the policy's version string and its act
record (`apps/three-surface-poc/src/governance-inputs.ts`). An act over the
proposed bytes therefore makes the gate refuse the policy until the pinned
version and act record are re-pointed in the same change, as the 2026-10-02
re-pin did. The packet asks for that continuation as a question.
