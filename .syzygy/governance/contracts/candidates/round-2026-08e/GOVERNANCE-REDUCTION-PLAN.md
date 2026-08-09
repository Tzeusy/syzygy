# Governance reduction plan — bounded, for F2

> **Plan, not authority.** Launch-gate question F2 found the corpus
> disproportionate by all three of its own proxies (monotonic artifact
> count; meta outgrowing normative 2.6×; defect→report→validator loops).
> This plan is the bounded reduction the v1.4 verdict formula accepts
> ("F2 Met OR explicitly owner-deferred **with a bounded reduction
> plan**"). The owner may adopt, amend, or replace it; nothing here
> deletes institutional evidence.

## Baseline measurement (pilot administration, 2026-08-09, commit `067d8a0`)

305 tracked files: 80 normative (23 in force + 57 candidate) vs 206 meta
(reports, reviews, indexes, validators, round records). Four round
directories in nine days. The corpus never decreased at any sampled
commit. [Observed — the pilot's sweep; re-measure at the next
administration, never quote this figure as current.]

## The six lanes (every tracked artifact belongs to exactly one)

| Lane | What belongs | Growth rule |
|---|---|---|
| **Active normative** | doctrine, decisions in force, craft policies, (post-act) accepted contracts | grows only by owner act |
| **Active candidates** | candidate contracts, policy candidates, decision packets | one candidate per question — a second candidate for the same question retires the first into history |
| **Current presentation** | README, AGENTS, PROJECT-STATUS, OVERVIEW, candidates README | fixed population; edits, not additions |
| **Generated navigation** | manifests, indexes, task router, budget report, matrix | generator-owned; a generated file with no generator is a defect |
| **Historical evidence** | raw reviews, round records, superseded offerings, rev9 corpus | append-only, banner-marked, indexed from `HISTORICAL-INDEX.md`, never on a default route |
| **Scratch** | `_bootstrap/` (git-excluded) | invisible to clones by design |

## Reduction commitments

1. **Duplicate current artifacts retired (done this pass):** the
   09-readiness report (bannered historical); the round-08d first-spec
   sequence (superseded by the single current revision 3); round-08d
   packets 2/7/8/10/11 (superseded by `decisions/` packets);
   `TASK-TO-CONTRACT-INDEX.md` and the load map's reader table collapse
   into the one generated task router.
2. **Historical artifacts bannered/indexed:** every `round-2026-08*`
   directory is history except the artifacts the current lane
   explicitly lists; `HISTORICAL-INDEX.md` (candidates root) is the one
   index.
3. **Maximum new meta-artifacts next cycle: 3** (the next round's
   preflight, its delta record, and one closure report). A fourth
   requires retiring one. Reviews and their raw storage are evidence,
   not meta, and are exempt — but each review round's *reports about
   reports* are not.
4. **Stop condition for new validators:** a new FAIL-capable check may
   be added only against a recorded incident (the PROCESS-LESSONS bar)
   or a rule in force/candidate with a named owner; the CHECK_OWNERS
   inventory is the census. No incident, no check.
5. **Condition for closing the current review round:** round-2026-08e
   closes when Waves A and B carry positive exact-package reviews at
   regenerated arguments (or the owner declines), the owner packets are
   delivered, and PROJECT-STATUS states the result — **not** when every
   finding in every deferred wave is repaired. Deferred-wave repairs are
   the next round, gated on P-29/P-30.
6. **The trend must invert:** at the next formal administration, the
   meta:normative ratio and the total count are re-measured; if both
   still grew with zero retirements, F2 is `Not met` regardless of this
   plan's existence — a plan that only ever plans is the failure mode
   F2 names.

## What is deliberately not reduced

Raw reviewer output (immutable evidence), the acceptance record's
history sections (§1a, struck-through items — the record's honesty
depends on them), doctrine, and the process-lessons register.
