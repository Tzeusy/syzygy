# PREPARED owner adoption act — Capability 1 specification

> **Prepared, not performed. This file adopts nothing.** Adoption is an
> owner act under VIS-4, recorded per CC-SPEC-10 ("lawful adoption …
> is recorded at the exact digest, and the record quotes what was
> adopted at which digest"). No session performs it, and this packet is
> a convenience the owner may discard. Until the owner's record exists,
> the change is a candidate binding nothing (CC-SPEC-10).

## What would be adopted

The OpenSpec change **`project-registration-and-honest-shape-visibility`**
— the Capability 1 specification (42 requirements, CAP1-REQ-001…064) —
at exactly these bytes (sha256; paths relative to
`openspec/changes/project-registration-and-honest-shape-visibility/`;
identical to the FINAL binding in `REVIEW-BINDING.md`, verified in a
clean clone at commit `26e1b51`):

```text
727fc3b35bb3eb09ccede6d08cbc829ea0044b031816d47842ec2573bff99290  .openspec.yaml
a9e170909acb672d7c46d02a6a8456511680feef4ef994ab5c297315961b735e  proposal.md
a7a90828ed51fd5e98d8cbc9f35f2aa88b5cdd75f6a53f905b816dcc11267652  design.md
2f6f4de4650b6800b968d243dd5887919ea7d4da550413db570d6928ac7646e9  CAPABILITY-COVERAGE.md
bd43e21a5930fada26549b1f6ab16be72b9d2f622a682dd07e88fccd11af7548  CONTRACT-COVERAGE.md
a00ccbf24f2e106ec3a396b8ae637097b4aaca9965548aab6d1cda0f37851c8e  GOVERNING-DEPENDENCIES.md
65b66c913cd2650881a9df8cb34a3c63b3f518041e83f45d2451980d9f1d0448  specs/project-registration-and-honest-shape-visibility/spec.md
```

`tasks.md` is the change's mutable lifecycle ledger and is outside the
adopted byte set (rationale in `REVIEW-BINDING.md` §FINAL binding).

## Evidence the act rests on (all in `round-2026-08k/`)

- RS-1 comprehension: **CONFIRM WITH EXCEPTIONS** (0 blockers)
- RS-2 behavior/testability: **REVISE** → all 3 blockers repaired (Pass 3)
- RS-3 authority/coverage: **REVISE** → both blockers repaired (Pass 3)
- RS-4 confirming: **REVISE** — five repairs verified; one residual
  (CAP1-REQ-038 Form line), disposed by the owner's final-bounded-
  correction instruction of 2026-08-20; RS-4's non-blocking
  observations deferred by that same instruction
- RS-5 targeted confirmation of the correction: **CONFIRM** (5/5 PASS)
- Validation at the final bytes: `openspec validate --strict` valid;
  18-check battery green (33 OK / 18 WARN / 0 FAIL); clean-clone run at
  `26e1b51` green with digest equality

## What adoption does — and does not do

Adoption makes the specification the accepted behavioral authority for
Capability 1, superseding the charter for required behavior (per the
charter's own header). It does **not** authorize implementation:
implementation requires the owner's **separate** authorization after
adoption (launch decision of 2026-08-20; SURFACE-CLAUSE-ROUTING-MATRIX
routing). It performs no other act — deferred waves, other capabilities,
and every open P-nn row are untouched.

## Suggested ceremony (owner's to amend or replace)

1. **Verify first** (CG-7 discipline): re-run
   `sha256sum` over the seven files and compare to the block above;
   run `python3 scripts/check_governance.py` and read the output.
2. **Declare**, in a new decisions record (suggested home:
   `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`), quoting the
   digest block above in full, with words to the effect of:

   > I adopt the Capability 1 specification
   > `project-registration-and-honest-shape-visibility` at the exact
   > digests quoted below, as the accepted behavioral authority for
   > Capability 1 under VIS-4 and CC-SPEC-10. This adoption authorizes
   > no implementation.

   Date and sign as owner.
3. **Check off** `tasks.md` item 4.1 (owner-only by its own text).
4. Follow-on pointer refreshes (`PROJECT-STATUS.md`, `AGENTS.md`,
   README, the charter's supersession banner) are session work the
   owner may direct after the act; none is part of the act itself.
