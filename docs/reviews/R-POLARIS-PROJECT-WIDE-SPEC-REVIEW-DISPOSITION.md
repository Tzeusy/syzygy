# Disposition — project-wide Polaris specification review

Review subject: `f092388219867149237d586d5f18a3884ff7f3a4`

Raw review: `R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-RAW.md`

Raw review sha256: `b47fbb0eb73507d0f6a4d4cc50f72908c6330c8a82be689477ce1f59209587dc`

Review verdict: **REVISE**

This register records the author's disposition. It does not confirm repairs;
the exact repaired bytes require an independent confirmation pass.

| # | Severity | Finding | Disposition |
|---|---|---|---|
| 1 | BLOCKER | Matrix partitions clause IDs without consequence review | **Repaired, awaiting confirmation.** Three independent clause-text audits produced 611 normalized consequence rows covering all 324 accepted clauses. A repair overlay supersedes 62 rows with 66 repaired consequences. The generator now verifies identities, dispositions and warrant agreement only; it makes no semantic judgment. Effective matrix: 615 consequences, 140 covered, 230 Unknown uncovered, 245 believed not applicable. |
| 2 | BLOCKER | Requirement warrants overclaim clause coverage | **Repaired, awaiting confirmation.** Warrant lists were reduced to exercised limbs, and PWB-REQ-007/014/015/016 close the essential epistemic, anchor, deep-dive and nonvisual gaps. Partial sibling consequences remain individually `unknown-uncovered`; no clause-level “covered” state exists. |
| 3 | BLOCKER | Capability denominator omits refusals | **Repaired, awaiting confirmation.** `CAPABILITY-COVERAGE.md` now derives 27 positive obligations/refusals from proposal, design and definitions: 20 covered, 7 named out of scope. |
| 4 | BLOCKER | No lawful observation consent or concrete secret policy | **Specification repaired; owner gates remain open.** PWB-REQ-005 requires both owner-provenance checks before the first body read and zero reads on every invalid case. Task 1.5 makes both separate acts dispatch blockers; sign-off mints neither. |
| 5 | BLOCKER | “Every item” has no closed identity/discovery rule | **Repaired, awaiting confirmation.** Purpose and design now define a finite source discovery procedure, stable item identity, separate source/item denominators and Unknown item counts for unavailable bodies. |
| 6 | DEFECT | Missing containment, active-content and resource controls | **Repaired, awaiting confirmation.** PWB-REQ-006 covers exact Git objects, normalized repository-relative containment, traversal/symlink/submodule rejection, inert output, unsafe URLs, declared budgets and Unknown-on-limit. |
| 7 | DEFECT | Plain-language oracle is subjective and unbounded | **Repaired, awaiting confirmation.** PWB-REQ-012 now has a closed string-role set, finite word/term/cardinality rules and an exhausted mechanical population; human comprehension remains separately owner-judged. |
| 8 | DEFECT | Cold-open omits RFC7-30 claim-strength prompt | **Repaired, awaiting confirmation.** PWB-REQ-007 exposes the full claim-strength tuple; PWB-REQ-021 preserves the complete RFC7-30 prompt set; PWB-REQ-016 requires a nonvisual/keyboard run. |
| 9 | NOTE | Proposal implies sign-off may be sufficient | **Repaired, awaiting confirmation.** Proposal now states sign-off is necessary but not sufficient; finding-derived improvement-cycle authority and security prerequisites also govern. |

## Open owner gates

1. Sign-off of the repaired candidate at its eventual exact digests.
2. A separate per-repository Butlers observation-consent record for the
   expanded project-shape content class.
3. Approval, at an exact digest, of a concrete secret-detection and content-
   classification policy suitable for project-shape Markdown and metadata.

No implementation is authorized or dispatchable while these gates remain
open.
