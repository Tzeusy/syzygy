# Disposition — project-wide Polaris specification review

Review subject: `f092388219867149237d586d5f18a3884ff7f3a4`

Raw review: `R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-RAW.md`

Raw review sha256: `b47fbb0eb73507d0f6a4d4cc50f72908c6330c8a82be689477ce1f59209587dc`

Review verdict: **REVISE**

This register records the author's disposition. It does not confirm repairs;
the exact repaired bytes require an independent confirmation pass.

| # | Severity | Finding | Disposition |
|---|---|---|---|
| 1 | BLOCKER | Matrix partitions clause IDs without consequence review | **Repaired, awaiting confirmation.** Three independent clause-text audits produced 613 normalized consequence rows covering all 324 accepted clauses. A repair overlay supersedes 62 rows with 71 repaired consequences. The generator now verifies identities, dispositions and warrant agreement only; it makes no semantic judgment. Effective matrix: 622 consequences, 132 covered, 242 Unknown uncovered, 248 believed not applicable. |
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

## Confirmation pass 3

Subject: `a89956847ecbc26b1529f205d115146e7b21723c`

Raw report: `R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-3-RAW.md`

Raw sha256: `c24fb7b7c345cb2dac79c316db3642216fd2ef08c11716bfe41dc62002091068`

Verdict: **REVISE**

| Finding | Pass-3 verdict | Repair disposition |
|---|---|---|
| Original 1 / pass N1/N4 | NOT CONFIRMED | Repaired: table parser now enforces canonical clause-derived base/repair IDs, exact covered syntax, every family row and bold Total row, declared repair row/supersession/disposition totals, and mutations for wrong-prefix IDs, junk/separator dispositions, missing/corrupt totals and deleted repairs. |
| Original 2 / N5 | NOT CONFIRMED | Repaired conservatively: four disputed identity/freshness/anchor rows and two release-only rows moved to Unknown/not-applicable; remaining exact oracles strengthened for emission stamps, registry scope, challenge/sibling semantics, deletion invariance, anchor target state/type, normative-copy absence, band classes/Base mode, personal-state exclusion and judgment fields. |
| Original 3–4, 6–9, pass-1 N2/N3 | CONFIRMED | No change. |
| Original 5 / N6 | NOT CONFIRMED | Repaired: qualifying topology H2 establishes ordinal context but mints no item; only first-column table labels mint topology identities. |
| N7 embedded totals | PARTIAL | Repaired: all embedded family and bold Total rows are now parsed, recomputed and mutation-tested. |
| N8 sibling applicability | NOT CONFIRMED | Repaired: used `unadopted-draft` and challenge aggregate composition are separately applicable/Unknown; only reconciliation-chain/work composition remains believed not applicable. |
| N9 exact identity/disposition validation | BLOCKER | Repaired as the first row above. |
| N10 four unsupported rows | BLOCKER | Repaired as the second row above. |
| N11 topology ambiguity | BLOCKER | Repaired as original finding 5 above. |
| N12 challenge applicability | BLOCKER | Repaired as N8 above. |

These are author dispositions. A fourth exact-head confirmation is required.

## Confirmation pass 4

Subject: `f441517e5c036608ff9af1f2b76b8fd9828c2c84`

Raw report: `R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-4-RAW.md`

Raw sha256: `56965025354f87872dea486bb572dbee372f6726b0b6dc8d06a50e48b8a9366d`

Verdict: **REVISE**

| Finding | Pass-4 verdict | Repair disposition |
|---|---|---|
| Original 1 / N1/N4/N9 | NOT CONFIRMED | All matrix/checker attacks now confirmed closed; remaining semantic closure repaired by adding the two omitted sibling-state consequences as separate Unknown rows. |
| Original 2 / N5/N10 | CONFIRMED | No change. |
| Original 3–4, 6–9, N2/N3/N7/N10–N12 | CONFIRMED | No change. |
| Original 5 / N6 | NOT CONFIRMED | Repaired: the reader-definition catalog set now includes Core Infrastructure exactly like the literal grammar. |
| N8 sibling applicability | NOT CONFIRMED | Repaired: `unadopted-draft`, `dismissed-by-decision`, `editorial-draft` and challenge aggregation each have their own applicable Unknown rows; only unused reconciliation/work composition remains believed not applicable. |
| N13 catalog heading conflict | BLOCKER | Repaired as original finding 5 above. |
| N14 missing sibling states | BLOCKER | Repaired as N8 above. |
| N15 two-versus-three authority summaries | DEFECT | Repaired: proposal, design, capability table, requirement and tasks all name consent + secret policy + observer registry. |

These are author dispositions. Confirmation pass 5 is the sixth and final
reconciliation pass permitted by the convergence ceiling.

## Sixth and final reconciliation pass

Subject: `4b16f0c9127ac1d91268b7ec22a9b55c02cd12e7`

Raw report: `R-POLARIS-PROJECT-WIDE-SPEC-CONFIRMATION-FINAL-RAW.md`

Raw sha256: `3f98fbc8bdbb39bbae5e27b4f6b0222d2f80d8db8a656090b742fcd8023326e5`

Verdict: **REVISE**

Twenty-four findings are **CONFIRMED**. One remains:

- **N15 — NOT CONFIRMED (DEFECT, security-significant).** Proposal, design
  decision §5, capability coverage, PWB-REQ-005 and task 1.5 all require the
  consent + secret policy + observer registration triple. The numbered data
  flow in `design.md` still says only “Verify observation consent and
  secret-policy owner provenance” before discovery and body reads, omitting
  observer registration. The flow can therefore be read as a two-gate
  implementation sequence in conflict with the three-gate requirement.

No repair was made after this verdict. The six-pass convergence ceiling is
exhausted. The candidate remains unconverged and cannot be offered for sign-off
or implementation without a new owner direction.

Recommended owner action: authorize exactly one bounded post-ceiling correction
to add observer-registry owner provenance to the numbered data-flow gate, then
one fresh confirmation of that correction only. This recommendation is not
authorization.

## Authorized post-ceiling correction

Authorization record:
`.syzygy/governance/decisions/POLARIS-POST-CEILING-CORRECTION-AUTHORIZATION.md`

Corrected subject: `5c52c0d0ff49bb123fc9fd0efb11397dcc90a595`

Raw targeted confirmation:
`R-POLARIS-PROJECT-WIDE-POST-CEILING-CONFIRMATION-RAW.md`

Raw sha256: `0f8402366f9c763991d91a1ac3afb902435d56bc1a681c25b521eb61b2f22d5a`

Verdict: **CONFIRMED**

N15 is closed. The proposal, design decision, numbered data flow, capability
coverage, PWB-REQ-005 and task 1.5 all require observation consent + secret
policy + observer registration before discovery or body reads. The exact
base-to-subject candidate diff is the one authorized design line; no other
candidate artifact changed.

All findings in the review chain are now confirmed. This confirmation is not
candidate sign-off, does not mint any security-authority artifact and does not
authorize implementation.
