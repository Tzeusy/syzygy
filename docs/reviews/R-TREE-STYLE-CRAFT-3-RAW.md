Title: Craft-and-care tree-style restyle — confirmation review 3
Verdict: REVISE
Reviewed: REPAIR-DIFF.txt and NEW-*.md vs OLD-*.md in review-craft3/, against REVIEW-2-RAW.md
Reviewer: independent fresh-context agent

**Scope and method**

- I read REVIEW-2-RAW.md and REPAIR-DIFF.txt. For each hunk I read the section in NEW and the matching rule body in OLD. I edited nothing.
- The diff has four hunks and no filenames. I found each one by exact-string search:
  - NEW-performance-and-visual-discipline.md, L15–17 (`## Performance` opening) and L64–67 (`## Visual discipline` opening).
  - NEW-review-and-documentation.md, L163–165 (CC-REV-6 opening).
  - NEW-testing-and-verification.md, L138–140 (CC-TEST-5 opening).

## A. Review 2 items

| Item | Status | Current NEW text | OLD rule it must match |
|---|---|---|---|
| N1 | RESOLVED | perf L15–17: "Performance spends only declared scope, treats caches as sacrificial, and backs every performance claim with a retained measurement artifact and its conditions, or labels it [Unknown]." | OLD CC-PERF-3: "Any claim that a change improves or regresses performance follows the evidence bar: a retained measurement artifact with its conditions, or the claim is labeled [Unknown]." |
| N7 | RESOLVED (note R2) | perf L64–67: "Every encoding declares its source, units/scale, legend, Unknown behavior and freshness; decoration never silently misstates truth; Unknowns stay visible, including inside aggregates; non-3D views tell the same truth as the 3D scene; and layout is reproducible." | OLD CC-VIZ-1: "declares: the data source it renders, its units/scale, a legend stating exactly what it means, how Unknown values render, and the freshness of the underlying evaluation." OLD CC-VIZ-3: "Aggregation anywhere discloses **membership count, the full aggregation-composition tuple, and expansion to members**" |
| N9 | PARTIAL (see R1) | review L163–165: "every revise-severity finding is fixed or explicitly overruled, with recorded rationale, by the accountable authority." | OLD CC-REV-6: "Every revise-severity finding is either fixed or explicitly overruled with recorded rationale by the accountable authority (the owner, for owner-gated artifacts)." |
| N10 | RESOLVED | testing L138–140: "Suites that feed alignment/convergence claims declare their scope and coverage, and a test becomes normative only by explicit, recorded designation." | OLD CC-TEST-5: "Any suite whose results feed alignment/convergence claims declares its scope and coverage so the claim can render 'converged **under this oracle**' honestly" |

**N1 detail**

- The repair restores both the [Unknown] alternative and the conditions requirement. It also narrows "every claim" to "performance claims".
- "Every performance claim" is still slightly broader than OLD's "claim that a change improves or regresses performance".
- That wording is the fix Review 2 gave, and it matches the rule's own OLD title, "Performance claims carry measurement evidence". I do not count it as drift.

## B. New drift in the changed lines

**Material**

**R1. CC-REV-6 opening (review L163–165): the added commas widen who the agent is.**

- NEW: "is fixed or explicitly overruled**, with recorded rationale,** by the accountable authority."
- The NEW body bullet (L168–170) keeps OLD's form, with no commas: "either fixed or explicitly overruled with recorded rationale by the accountable authority".
- In OLD, "with recorded rationale by the accountable authority" attaches to "overruled". The repair sets it off with commas, so the natural reading applies "by the accountable authority" to both verbs.
- The opening therefore now reads as requiring the accountable authority (the owner, for owner-gated artifacts) to make or justify fixes as well as overrulings. That states the rule more broadly than its body.
- A reader who stops at the opening gets a different answer to "may the author simply fix a revise-severity finding?"
- Fix: "every revise-severity finding is either fixed or explicitly overruled with recorded rationale by the accountable authority." This drops the two commas and restores "either", matching the body.

**Notes**

**R2. `## Visual discipline` opening (perf L64–67).**

- The five declarations now match CC-VIZ-1.
- The repair replaced "declares what it means" with a bare "legend". The opening no longer carries CC-VIZ-1's fidelity clause: "a legend stating exactly what it means" / "An encoding means exactly what its legend says".
- "Unknowns stay visible, including inside aggregates" is narrower than CC-VIZ-3's disclosure duty. That duty applies to every aggregate, not only to Unknowns, and requires count, composition tuple and expansion.
- Both are coarsening rather than a changed answer. The fidelity clause is stated in full one level down (L73–74), and "decoration never silently misstates truth" partly covers it.
- Optional wording: "…legend (which it means exactly), Unknown behavior and freshness; … aggregates disclose their count, composition and members".

**No drift**

- N1 hunk: none beyond the note under A.
- N10 hunk: none. "Explicit, recorded designation" was not changed by this repair.

## Summary

- N1, N7 and N10 are resolved. N9 is partial.
- R1 is new and material: the repair's commas make the CC-REV-6 opening apply "by the accountable authority" to fixes as well as overrulings, which is broader than the body.
- R2 is a note.
- The verdict is REVISE on R1 alone. Its fix is a two-comma deletion, given above.
