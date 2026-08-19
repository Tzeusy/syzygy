# Tasks — project-registration-and-honest-shape-visibility

> **Implementation planning is deferred until the specification is
> adopted.** The owner's 2026-08-20 decision authorizes specification
> definition only. This file therefore contains **no technical backlog**:
> no build tasks, no stack tasks, no deployment tasks. The tasks below
> are the specification lifecycle itself.

## 1. Specification authoring

- [x] 1.1 Record the owner's launch decision in the decision system
- [x] 1.2 Draft proposal, spec (CAP1-REQ-001…064), and design artifacts
- [ ] 1.3 Ship the coverage artifacts: `CAPABILITY-COVERAGE.md`
      (CC-SPEC-11) and `CONTRACT-COVERAGE.md` (CC-SPEC-8)
- [ ] 1.4 Generate `GOVERNING-DEPENDENCIES.md` from the requirement
      warrants (CC-IMPACT-1) and wire its `--check` into the battery

## 2. Review and repair (bounded)

- [ ] 2.1 Three independent fresh-context reviews (comprehension;
      behavior and testability; authority and coverage), raw output
      preserved verbatim
- [ ] 2.2 One consolidated repair pass
- [ ] 2.3 One confirming review of the repaired bytes

## 3. Validation

- [ ] 3.1 `openspec validate --strict` clean
- [ ] 3.2 Full governance battery green (per `PROJECT-STATUS.md` §"How to
      verify this page"), outputs and denominators read
- [ ] 3.3 Clean-clone validation at the exact reviewed commit

## 4. Owner adoption — not performed by this change

- [ ] 4.1 **Owner-only:** adoption of this specification at an exact
      digest (VIS-4; CC-SPEC-10). This task belongs to the owner; no
      session may check it off. Until it is done, this change binds
      nothing and authorizes no implementation.
