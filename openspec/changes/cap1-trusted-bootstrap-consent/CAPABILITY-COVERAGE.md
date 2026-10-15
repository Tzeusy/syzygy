# Candidate capability coverage

Non-effective CC-SPEC-11 table for this one coherent amendment. [Inferred]
Population is extracted from proposal.md What Changes/Impact/Non-goals, expanded
by its two full requirement replacements; it is not the implementation's successes.
A reviewer independently checks omitted scope obligations against those texts.

## Amendment partition

[Observed] Scripted table construction yields 15 rows:
10 covered by proposed requirements, 5 excluded by explicit
non-goals, and 0 unresolved amendment behavior rows. Coverage means specified,
not implemented or adopted. Exact encoding/authority-source acquisition are
separate implementation-gate questions, not implicitly chosen here.

| ID | Declared amendment obligation | Covering scenario or constraint |
|---|---|---|
| A-01 | Explicit state-(1) consent admits only exact scope without A1 | CAP1-REQ-011: Explicit bootstrap consent without an audit provider |
| A-02 | Correlated state-(2) consent remains a distinct admission | CAP1-REQ-011: Correlated consent |
| A-03 | Invalid binding variants refuse content reads with Unknown and owner routing | CAP1-REQ-011: Invalid binding refuses observation |
| A-04 | Failed correlation never downgrades to bootstrap | CAP1-REQ-011: Failed correlation does not downgrade |
| A-05 | Observable missing/non-human act evidence is refused without a forged-attendance detection claim | CAP1-REQ-011: Observable machine-only submission is refused; Bootstrap oracle boundary |
| A-06 | Grant/withdrawal conflicts and unresolved withdrawal do not revive authority | CAP1-REQ-011: Withdrawal and unresolved withdrawal remain fail closed |
| A-07 | Capture binds immutable decisions to inputs and explicit as-of | CAP1-REQ-011: Captured decision is immutable |
| A-08 | Human/machine consent provenance agrees and does not imply effect success | CAP1-REQ-046: Bootstrap disclosure agrees across channels |
| A-09 | Invalid consent explanations preserve primary/specific reasons and keyboard access | CAP1-REQ-046: Invalid consent has an accessible explanation |
| A-10 | Later correlation changes a new evaluation without rewriting old evidence | CAP1-REQ-046: New correlation cannot rewrite old evidence |

## Lawfully out of scope for this proposal

| ID | Excluded outcome | Excluding non-goal |
|---|---|---|
| X-01 | Implementation and automatic legacy-record upgrade | proposal.md Non-goals: no implementation; no automatic conversion |
| X-02 | Audit/ceremony provider, owner-held keys, credentials or new retention infrastructure | proposal.md Non-goals: no provider/ceremony service, keys, credentials or retention system |
| X-03 | Real-project reads, egress, runtime operation, deployment or release | proposal.md Non-goals: no observation/egress/runtime/deployment/release |
| X-04 | General authority-input system and policy adoption | proposal.md Non-goals: no general authority-input system or policy adoption |
| X-05 | Walkthrough, generator, launch-gate, terminal review or deferred Mission/Context changes | proposal.md Non-goals: named unrelated lanes excluded |

## Predecessor composition

[Observed] The unchanged predecessor CAPABILITY-COVERAGE.md contains 26
unique O/X/U obligation rows. This amendment supplements its O-05/O-10/O-19
consent/provenance limbs; it does not delete or reclassify the other obligations.
The predecessor's U-01 remains Unknown. Its table and all predecessor requirements
except the two explicit replacements remain part of the composition; no blanket
claim that the whole capability is now covered is made. Re-derive predecessor rows
from lines matching the O/X/U ID column; independently compare the row IDs as a set.

Independent confirmation is pending the corrected candidate review. A sign-off
requires that confirmation, not this author's table count alone.
[Marked 2026-10-15: the first sentence was true when written. Review 2 confirmed
the partition on 2026-09-14 (docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2-RAW.md:3);
the 2026-10-15 rebase retired that confirmation for the changed bytes, and the
confirmation of record is the one REVIEW-DISPOSITION.md names for the rebased
bytes.]
