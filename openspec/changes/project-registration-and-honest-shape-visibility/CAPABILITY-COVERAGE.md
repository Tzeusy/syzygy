# Capability coverage — project-registration-and-honest-shape-visibility

> **CC-SPEC-11 coverage table, shipped with the specification.** The
> population is the **declared capability obligations** — each thing the
> CC-SPEC-1 scope statement (proposal.md §Scope, §What Changes) says the
> capability does, renders, records, or refuses — counted and placed in
> **exactly one** of three sets that sum to the population. A reviewer
> who believes an obligation is missing from this population raises that
> against the scope statement, not against this table.

## Population

26 declared obligations: 21 covered, 4 lawfully out of scope, 1 Unknown.
21 + 4 + 1 = 26. (Totals computed by the sweep in "Verifying this
table".)

## Covered (21)

| # | Declared obligation | Covering requirements |
|---|---|---|
| O-01 | read and validate the project declaration; register on validity | CAP1-REQ-001, CAP1-REQ-005 |
| O-02 | fail invalid or incomplete declarations by name, never partially register | CAP1-REQ-002, CAP1-REQ-003 |
| O-03 | refuse silent invention, repair, or inference of declaration content | CAP1-REQ-004 |
| O-04 | surface governance-root count violations, never repair them | CAP1-REQ-006 |
| O-05 | record and show consent and per-repository coverage as facts | CAP1-REQ-010, CAP1-REQ-011 |
| O-06 | render unconsented sources as the Unknown policy state with a route | CAP1-REQ-012 |
| O-07 | keep coverage failure states distinguishable | CAP1-REQ-013 |
| O-08 | refuse to render incomplete coverage as complete | CAP1-REQ-014 |
| O-09 | serve one coverage boundary identically to humans and admitted machines | CAP1-REQ-015 |
| O-10 | refuse observation outside granted per-pair authority | CAP1-REQ-016 |
| O-11 | serve the one fixed human entry `.syzygy/intent/OVERVIEW.md` | CAP1-REQ-020 |
| O-12 | keep the entry explanatory and routed, never authoritative | CAP1-REQ-021, CAP1-REQ-022 |
| O-13 | keep entry behavior inside the governed write plane | CAP1-REQ-023 |
| O-14 | compute and present the seven shape answers independently, vocabulary fixed here | CAP1-REQ-030, CAP1-REQ-032, CAP1-REQ-038 |
| O-15 | refuse every rollup: score, badge, colour, percentage, passing count | CAP1-REQ-031 |
| O-16 | value every answer honestly under the two-term rule, reasons visible and plural | CAP1-REQ-033, CAP1-REQ-034, CAP1-REQ-035 |
| O-17 | hold `Mission-ready` to its deferred posture and `Reconciled` to Unknown while uncomputed | CAP1-REQ-036, CAP1-REQ-037 |
| O-18 | explain every answer ("Why this answer?") with one warranted fact set | CAP1-REQ-040, CAP1-REQ-044 |
| O-19 | serve the same facts to humans and machines, stamped, parity-defect-visible | CAP1-REQ-041, CAP1-REQ-042, CAP1-REQ-043, CAP1-REQ-045, CAP1-REQ-046 |
| O-20 | report per-repository discoverability in the closed four-value vocabulary, evidence-backed | CAP1-REQ-050, CAP1-REQ-051, CAP1-REQ-052 |
| O-21 | propose (never write) the repository-entry link; keep identity stable, writes bounded, staleness and distinctions honest | CAP1-REQ-053, CAP1-REQ-060, CAP1-REQ-061, CAP1-REQ-062, CAP1-REQ-063, CAP1-REQ-064 |

## Lawfully out of scope (4)

Excluded by the specification's own non-goals (CC-SPEC-5), each with the
excluding non-goal named (proposal.md §Non-goals):

| # | Obligation a reader might expect | Excluding non-goal |
|---|---|---|
| X-01 | evaluate `Mission-ready` substantively | "does not execute or monitor Missions"; SDR-36 rule 3 defers the facet's semantics — only its honest posture is in scope (O-17) |
| X-02 | compute reconciliation / intent-to-code convergence | "does not calculate complete intent-to-code convergence" — only the honest rendering of the uncomputed state is in scope (O-17) |
| X-03 | apply the proposed repository-entry link to a root README | "does not modify source code; does not edit a repository root README" — proposing is in scope (O-21), applying is not |
| X-04 | onboard or register a real external project during authoring | "does not register or onboard a real external project during specification authoring" |

## Unknown / unresolved (1)

| # | Obligation | What would settle it |
|---|---|---|
| U-01 | the concrete evidence basis for the `Human-understandable` answer (which recorded comprehension-walkthrough artifacts count, at what currency) | acceptance of the Polaris walkthrough capability's specification, or an owner decision naming the admissible evidence classes. Until then the facet renders `Unknown` by CAP1-REQ-030's definition — the honest posture is specified; the evidence basis is not |

## Verifying this table

- Population sum: count the rows of the three tables above; they must
  sum to the stated population (21 + 4 + 1 = 26).
- Requirement reachability: every `CAP1-REQ-nnn` in the spec appears in
  at least one covered row, and every ID cited here exists in the spec —
  sweep both directions (the denominators are the spec's requirement
  count, 42, and this file's citation set).
