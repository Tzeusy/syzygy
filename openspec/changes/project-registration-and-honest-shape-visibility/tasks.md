# Tasks — project-registration-and-honest-shape-visibility

> **Implementation planning is deferred until the specification is
> adopted.** The owner's 2026-08-20 decision authorizes specification
> definition only. This file therefore contains **no technical backlog**:
> no build tasks, no stack tasks, no deployment tasks. The tasks below
> are the specification lifecycle itself.

## 1. Specification authoring

- [x] 1.1 Record the owner's launch decision in the decision system
- [x] 1.2 Draft proposal, spec (CAP1-REQ-001…064), and design artifacts
- [x] 1.3 Ship the coverage artifacts: `CAPABILITY-COVERAGE.md`
      (CC-SPEC-11) and `CONTRACT-COVERAGE.md` (CC-SPEC-8)
- [x] 1.4 Generate `GOVERNING-DEPENDENCIES.md` from the requirement
      warrants (CC-IMPACT-1) and wire its `--check` into the battery

## 2. Review and repair (bounded)

- [x] 2.1 Three independent fresh-context reviews (comprehension;
      behavior and testability; authority and coverage), raw output
      preserved verbatim (`round-2026-08k/reviews/`, bound at
      `round-2026-08k/REVIEW-BINDING.md`)
- [x] 2.2 One consolidated repair pass (Pass 3, 2026-08-20 — all five
      blockers and the taken non-blocking findings, one edit batch)
- [x] 2.3 One confirming review of the repaired bytes (RS-4, 2026-08-20,
      raw at `round-2026-08k/reviews/RS-4-CONFIRMING-RAW.md` — verdict
      copied exactly: **REVISE**; all five Pass 2 blockers verified
      repaired; one remaining blocker, CAP1-REQ-038's Form line, which
      the owner then disposed by authorizing one final bounded
      correction; RS-4's non-blocking observations are deferred by that
      same owner instruction)
- [x] 2.4 One fresh targeted confirmation of the final bounded
      correction only: the CAP1-REQ-038 Form relabel, all 42 form
      classifications, the exact final digests, generated-artifact
      consistency, and the final validation evidence — no broader
      review (RS-5, 2026-08-20, raw at
      `round-2026-08k/reviews/RS-5-TARGETED-CONFIRMATION-RAW.md` —
      verdict copied exactly: **CONFIRM**; all five checks PASS, no
      blockers)

## 3. Validation (rerun against the final bytes, 2026-08-20)

- [x] 3.1 `openspec validate --strict` clean — rerun after the REQ-038
      correction: "Change 'project-registration-and-honest-shape-
      visibility' is valid"
- [x] 3.2 Full governance battery green (per `PROJECT-STATUS.md` §"How to
      verify this page"), outputs and denominators read — rerun after
      the REQ-038 correction: 18/18 lines green, 33 OK / 18 WARN /
      0 FAIL on `check_governance.py`, every selftest 0 failing
- [x] 3.3 Clean-clone validation at the exact final commit — run
      2026-08-20 in a fresh clone checked out at `26e1b51`: all 18
      battery lines green, `openspec validate --strict` valid, and the
      clone's spec.md / GOVERNING-DEPENDENCIES.md sha256 digests equal
      the FINAL binding in `round-2026-08k/REVIEW-BINDING.md` exactly.
      (This checkbox lives outside that binding by design; see the
      binding's tasks.md exclusion note)

## 4. Owner adoption

- [x] 4.1 **Owner-only:** adoption of this specification at an exact
      digest (VIS-4; CC-SPEC-10). **Performed by the owner, act dated
      2026-08-20** — recorded verbatim at
      `.syzygy/governance/decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`,
      at exactly the seven digests of the FINAL binding (checkbox
      checked 2026-08-21 on the owner's explicit instruction in that
      act). The adoption authorizes **no implementation** —
      implementation requires a separate, subsequent owner
      authorization, which does not exist.
