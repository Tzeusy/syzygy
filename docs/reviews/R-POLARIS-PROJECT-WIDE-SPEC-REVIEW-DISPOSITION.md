# Disposition — project-wide Polaris specification review

Review subject: `f092388219867149237d586d5f18a3884ff7f3a4`

Raw review: `R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-RAW.md`

Raw review sha256: `b47fbb0eb73507d0f6a4d4cc50f72908c6330c8a82be689477ce1f59209587dc`

Review verdict: **REVISE**

This register records the author's disposition. It does not confirm repairs;
the exact repaired bytes require an independent confirmation pass.

| # | Severity | Finding | Disposition |
|---|---|---|---|
| 1 | BLOCKER | Matrix partitions clause IDs without consequence review | **Repaired, awaiting confirmation.** Three independent clause-text audits produced 613 normalized consequence rows covering all 324 accepted clauses. A repair overlay supersedes 62 rows with 68 repaired consequences. The generator now verifies identities, dispositions and warrant agreement only; it makes no semantic judgment. Effective matrix: 619 consequences, 136 covered, 235 Unknown uncovered, 248 believed not applicable. |
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

## Confirmation pass 1

Subject: `8069742258e4affcb813cfa69c545c8453c167cb`

Raw report: `R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-1-RAW.md`

Raw sha256: `b58286e3328028d64c273cae0450c5be397e0d1160537333d44eb727b59d1d29`

Verdict: **REVISE**

| Finding | Pass-1 verdict | Repair disposition |
|---|---|---|
| Original 1 — consequence matrix | NOT CONFIRMED | Repaired: split malformed RFC3-7 row, added fail-closed unparseable-row detection/mutation test, regenerated true population. |
| Original 2 — warrant overclaims | NOT CONFIRMED | Repaired: strengthened Claim identity/challenge tuple, aggregate composition, anchor target-state immutability, verbatim doctrine/non-goal comparison, personal-state separation and narrative machine type; added missing RFC7-16 metric/count-wall consequence. |
| Original 3 — capability totals | PARTIAL | Repaired: corrected 27-row totals to 21 covered + 6 lawfully out of scope. |
| Original 4 — consent/policy | CONFIRMED | No change. |
| Original 5 — closed discovery | PARTIAL | Repaired: added a closed nine-class item grammar, exact extraction syntax and path-independent item identity; arbitrary headings/links mint nothing. |
| Original 6 — input safety | CONFIRMED | No change. |
| Original 7 — plain copy | CONFIRMED | No change. |
| Original 8 — complete cold-open | CONFIRMED | No change. |
| Original 9 — authority language | CONFIRMED | No change. |
| N1 — silently dropped row | BLOCKER | Repaired as original finding 1 above. |
| N2 — triple/pair inconsistency | DEFECT | Repaired: case, observable, oracle and falsifier consistently require all three authorities. |
| N3 — judgment inside run record | DEFECT | Repaired: PWB-REQ-021 records only answers/paths/identities/mode; separate owner decision carries verdict/rationale/judging party. |

These are author dispositions. A second exact-head confirmation is required.

## Confirmation pass 2

Subject: `b4470708b7752b48acb5df81fe9a707b296fead6`

Raw report: `R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-2-RAW.md`

Raw sha256: `79c15dc57bd748872df0a7dd145bcac63b05ea00c4532387bd841bbbeed24d5f`

Verdict: **REVISE**

| Finding | Pass-2 verdict | Repair disposition |
|---|---|---|
| Original 1 / pass-1 N1 | NOT CONFIRMED | Repaired: parser now walks every data row inside every base/repair table independently of ID grammar, rejects malformed IDs/columns/dispositions, validates embedded family totals and mutation-tests each escape. RFC3-7 observation/egress row split. |
| Original 2 | NOT CONFIRMED | Repaired conservatively: six unsupported overlay rows moved to Unknown/not-applicable; exact oracles added for emission stamps, registry scope, Claim identity/challenge state, tier/sibling semantics, deletion invariance, anchor target classes/state, normative-copy absence, band classes/Base mode, personal-state exclusion, machine claim types and complete judgment fields. |
| Original 3 | CONFIRMED | No change. |
| Original 4 | CONFIRMED | No change. |
| Original 5 | PARTIAL | Repaired: item grammar now binds exact source files, heading text/levels, list/table/TOML syntax, key extraction/normalization, duplicate behavior and fail-closed malformed-source output. |
| Original 6–9 | CONFIRMED | No change. |
| Pass-1 N2/N3 | CONFIRMED | No change. |
| N4 malformed-row escape | BLOCKER | Repaired with table-structure parsing and expanded mutations. |
| N5 23 semantic overclaims | BLOCKER | Repaired as original finding 2 above; unsupported consequences remain disclosed Unknown rather than receiving broader machinery. |
| N6 parser-ambiguous item grammar | BLOCKER | Repaired as original finding 5 above. |
| N7 embedded matrix totals | DEFECT | Repaired and now mechanically checked against parsed rows. |
| N8 sibling-state applicability | DEFECT | Repaired: `unadopted-draft` aggregate composition is Unknown/applicable; unused challenge/chain/work composition is separately believed not applicable. |

These are author dispositions. A third exact-head confirmation is required.
