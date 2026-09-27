# Review brief — each project's profile declares its container shapes

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries
> no verdict. No review has been run.

## What the reviewer is given, and nothing else

**The artifact** — the five files of
`.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, this
brief, `PWB-CONTAINER-SHAPE-PROFILE-MANIFEST.txt`), the three patches under
`proposed/`, and `scripts/build_pwb_container_shape_profile_amendment.py`.

**The subject** — `openspec/changes/polaris-project-wide-butlers-model/` at
its current bytes.

**Governing references** —

- §6 of `.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`.
- `VIS-2`, `VIS-4`, `VIS-7`.
- `PWB-REQ-002` and the reader definitions in the subject's `spec.md`.
- `packages/three-surface-poc-core/src/project-shape-extraction.ts`, for
  the shape sentences.
- `NORMATIVE-CHANGE-WORKFLOW.md`, `SEMANTIC-DELTA-TEMPLATE.md` and CC-REV-2.

**Withheld** — the M8 funnel under `docs/design/`, the 2026-09-22 pursuit
and the `syzygy-dov.24` package. They recommend or draft; the sitting
decides. A reviewer comparing this package with `syzygy-dov.24` is a
separate, later review.

## Acceptance criteria

1. **Does it do what §6 asks, and no more?** §6: "let a project's profile
   declare its own container shapes, instead of the shapes written into
   PWB-REQ-002's reader definitions", with Butlers' profile declaring
   "today's shapes as they are". The draft also lets the profile declare
   the file, heading and naming rule. Is that inside §6, or a widening?
   (Packet question 1.)
2. **Are the nine shape sentences exact?** Each says what is read and what
   makes a source malformed. Check each against the extraction code; a
   sentence looser or stricter than the code is a finding. Is there a shape
   the code reads that the list omits?
3. **Are the eight key forms exact and complete** for the nine Butlers class
   bullets?
4. **Is Butlers' grammar unchanged?** Only its lead-in line may differ.
5. **Does the missing-rule sentence keep `VIS-2`?** A class with no rule, or
   an unknown shape or key form, must stay counted with an Unknown item
   denominator, and no built-in rule may stand in.
6. **Is the oracle still independent and falsifiable?** In particular, can
   "for Butlers, both also apply the grammar written in these reader
   definitions" fail?
7. **Does the package verify, and does the verification mean anything?** Run
   `--check` and `--selftest` (74 mutants). Name any claim the builder makes
   that no mutant covers.
8. **Does the package quote any act argument or claim authority it lacks?**
   Nothing labelled accepted or in force; the phrase marked not offered.
9. **Are the open questions honest?** Especially 4 (per-class Unknown versus
   whole-profile refusal) and 6 (signing before any code loads a profile).

## Out of scope

Whether to perform the act; which project comes second; the registry
fields; any shape for Syzygy's own craft policies.

## Recording

Raw output under `docs/reviews/`, file name ending `-RAW.md`, verdict words
copied exactly. A digest quoted in a raw freezes those bytes.
