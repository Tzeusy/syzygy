# Owner direction — Three-Surface POC specification authorization

Date: 2026-08-30

Owner: Tzeusy

Baseline: `b1cdb7b` (the commit recording the 2026-08-30 redesign direction)

Recorded from direction the owner gave directly in session on 2026-08-30.
Asked whether the redesigned surfaces should be specified before they are
built, and offered the choice between POC-plane spec artifacts, a real
OpenSpec change, or direction-only, the owner chose: **a real OpenSpec
change**.

## What this authorizes

1. **Authoring of exactly one new candidate OpenSpec change**,
   `three-surface-poc-experience`, specifying the observable behavior of
   the redesigned Three-Surface POC: the Butlers code-structure and
   Beads-on-Dolt observers, the client-side rendering seam, and the
   Polaris / Trajectory / Orrery surface experiences directed on
   2026-08-30 (`THREE-SURFACE-POC-REDESIGN-DIRECTION.md`).
2. For this one change only, this direction **supersedes**:
   - the prohibition on creating any OpenSpec changeset other than the
     adopted Capability 1 change; and
   - the clause "No RFC, OpenSpec change, launch packet, questionnaire,
     acceptance ceremony, or review round is created for this direction"
     in the 2026-08-29 POC direction and its 2026-08-30 redesign
     refinement, **as it applies to an OpenSpec change alone**. No RFC,
     launch packet, questionnaire, or new review round is authorized.

## What this does not change

- Authoring authorization is never a product-behavior warrant. The change
  is a **candidate and binds nothing** until the owner signs it off;
  sign-off is a separate owner act (VIS-4). The eight-item POC cap, WIP
  one, the single bounded review cycle, and every invariant of the
  2026-08-29 direction remain in force.
- Implementation of the surface-redesign work item (`syzygy-z2b`) is
  **gated on the owner's sign-off of this specification**. Until then the
  spec change is draft material; building against it is not authorized.
- The in-force craft policies CC-SPEC-1…11 and CC-IMPACT-1…7 govern the
  authoring. Where an obligation is not yet discharged (for example the
  CC-SPEC-8 contract-coverage matrix), the change must say so explicitly
  rather than claim completeness.
- The adopted Capability 1 change and its seven adopted artifacts are
  untouched.
