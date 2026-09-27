# Review brief — each project's profile declares its container shapes

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries
> no verdict. Round 1 returned REVISE
> (`docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-RAW.md`); this brief is for
> round 2, over the repaired bytes.

## What the reviewer is given, and nothing else

**The artifact** — the five files of
`.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, this
brief, `PWB-CONTAINER-SHAPE-PROFILE-MANIFEST.txt`), the three patches under
`proposed/`, `scripts/build_pwb_container_shape_profile_amendment.py`, and
the round-1 raw with the packet's review record.

**The subject** — `openspec/changes/polaris-project-wide-butlers-model/` at
its current bytes.

**Governing references** —

- §6 of `.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`.
- P-74 (line 64) and P-82 (line 70) of
  `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, and §6 of
  `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` (landing order),
  all under `.syzygy/governance/decisions/`.
- `VIS-2`, `VIS-4`, `VIS-7`.
- `PWB-REQ-002` and the reader definitions in the subject's `spec.md`.
- `packages/three-surface-poc-core/src/project-shape-extraction.ts`, for
  the shape sentences.
- `NORMATIVE-CHANGE-WORKFLOW.md`, `SEMANTIC-DELTA-TEMPLATE.md` and CC-REV-2.

**Shared text** — `SHAPES` and `ITEM_KEY_SENTENCES` in
the loaded-profile amendment's builder under `scripts/` on branch
`agent/tier4-dov24` (PR #123; not yet on `main`), which this package copies
word for word. Read
those two constants only, to check the copy; the rest of that package is
withheld.

**Withheld** — the M8 funnel under `docs/design/` and the 2026-09-22
pursuit. They recommend; the sitting decides.

## Acceptance criteria

1. **Is every round-1 finding closed as the review record says?** R1–R5
   and N1–N9, each against the bytes, not the disposition's words.
2. **Does it do what §6 asks, and no more?** §6: "let a project's profile
   declare its own container shapes, instead of the shapes written into
   PWB-REQ-002's reader definitions", with Butlers' profile declaring
   "today's shapes as they are". The draft also lets the profile declare
   the file, heading and key form. Is that inside §6, or a widening?
   (Packet question 1.)
3. **Are the shape and key-form sentences exact?** Check each against the
   extraction code and against the shared constants; a sentence looser or
   stricter than the code, or a copy that differs, is a finding. Can the
   grammar rows express every one of Butlers' nine class bullets?
4. **Is Butlers' grammar unchanged?** Only its opening line may differ; the
   exactness paragraph moves word for word into its own bullet.
5. **Do the loaded-profile and interim-default sentences keep `VIS-2` and
   agree with P-74 Q2?** A class with no row, or an invalid row, must make
   the class and its category Unknown with every source counted; no
   built-in rule may stand in once a profile is loaded; today's code, with
   no profile loaded, must conform.
6. **Are this package and M15 (P-82) kept apart?** Does anything here decide
   how much of a source fails, which P-82 leaves to M15? Packet question 8.
7. **Is the oracle still independent and falsifiable?** In particular, can
   "for Butlers read through its loaded profile, both also apply the grammar
   written in these reader definitions" fail?
8. **Does the package verify, and does the verification mean anything?** Run
   `--check` and `--selftest` (106 mutants). Name any claim the builder makes
   that no mutant covers.
9. **Does the package quote any act argument or claim authority it lacks?**
   Nothing labelled accepted or in force; the phrase marked not offered; no
   landing order attributed to the owner beyond the ruled four.
10. **Are the open questions honest, and not already ruled?** Especially 4,
    6, 7 and 8.

## Out of scope

Whether to perform the act; which project comes second; the registry
fields; any shape for Syzygy's own craft policies.

## Recording

Raw output under `docs/reviews/`, file name ending `-RAW.md`, verdict words
copied exactly. A digest quoted in a raw freezes those bytes.
