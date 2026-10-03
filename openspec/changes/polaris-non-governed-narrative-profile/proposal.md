# Polaris non-governed narrative profile

> **Candidate — binds nothing.** Drafted 2026-10-03 for the owner's review. It
> is not adopted, performs no act, and grants no read, egress or write. Effect
> comes only from an owner act over the exact reviewed bytes.

**Polaris can write an honest account of an open-source repository that has
no Syzygy declarations, without pretending that it does.** This change adds
one requirement to the `polaris-generation` capability so that the narrative
obligations written for governed projects have a defined reading for a
non-governed, observed repository.

## Why

The adopted narrative obligations assume a governed subject. Catalog
membership comes from "declared capabilities", capability deep dives carry
argument, contract and reality bands, and the exact-source terminus is
verbatim text from `openspec/**`. [Inferred: from the repository's public
description; no body was read in drafting] An observed public repository such
as `redis/redis` has none of these. Applied literally, the catalog would be
nearly all Unknown, each deep dive would carry empty bands, and the
terminus would have nothing to quote. RFC7-6 and RFC7-15 define the first as
correct, thin output, so each result is honest by the current text; the
proposal is that all three are also useless for a proving-ground dossier. The proving-ground work in `docs/polaris-generation/TARGETS.md`
needs a defined reading, not a silent reinterpretation by the generator.

## What changes

- **Added:** requirement 032, "Non-governed narrative profile", with twelve
  scenarios. It defines (a) what a declared capability is for such a
  repository, (b) how deep-dive bands report absence, and (c) what the leaf
  altitude and the exact-source terminus are when no specification exists.
- **Modified:** no requirement's bytes. For a non-governed subject the profile
  displaces the text of requirement 004 that the requirement lists (and the
  delta quotes), so 004's effective meaning changes for that class of subject; requirements 001 to 031 keep their bytes,
  meaning and scenarios for governed projects.
- **Not decided here:** the altitude order for a dossier, the reading of
  "advantages", and the reader-facing page budget. Those are owner rulings
  (see the owner packet) and need no amendment to be put.

## Capabilities

- **Modified:** `polaris-generation`, by one added requirement.
- **New:** none. It is the same capability, extended in the way requirements
  030 and 031 extended it.

## Amendment relation

- It amends the composition of `openspec/changes/polaris-manifesto-generation/`
  and `openspec/changes/polaris-manifesto-understanding-amendment/`, as
  amended by the tree-form adoption. No byte of either is edited.
- **The candidate delta is held in `proposed/`, not `specs/`.** A third file
  under `specs/polaris-generation/` would fail the effective-scenario
  recount's rule of exactly one base and one overlay
  (`scripts/count_polaris_effective_scenarios.py`). Placing it in `specs/`
  is a step of adoption, taken in the same change as that script's
  generalization (task list).
- Never archive or sync this as an unrelated competing change.

## Scope and preserved boundaries

- **Admission comes first.** The profile is chosen from the admitted project
  input and the source classes discovery exposes; the generator never reads a
  repository to decide how to compose it (requirements 001, 020, 025, 030).
- **Declared means the maintainers said so.** A declaration is the
  maintainers' statement, not verified behavior, not adopted Syzygy intent,
  and not an endorsement.
- **The governed readings stay.** A governed subject composed under this
  profile fails.
- **Existing requirements stay applicable:** editorial-draft state, no
  invented motive, source-integrity, retention and per-project consent.
