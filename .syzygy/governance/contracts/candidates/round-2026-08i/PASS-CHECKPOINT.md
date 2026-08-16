# Round 2026-08i — convergence pass checkpoint

> **In-flight coordination state for a staggered pass, not authority.**
> One lead session executes the convergence prompt
> (`syzygy_fable_convergence_to_capability1_prompt.md`) staggered over
> ~15 hours from 2026-08-17 ~02:00 (+08:00). Co-lead: check the phase table
> before editing shared artifacts; this file's "in progress" row names what
> is being edited. Updated at every phase boundary.

## Phase plan

| Phase | Workstream | State |
|---|---|---|
| 0 | Preflight — exact-state verification, baseline battery | **done** (`CONVERGENCE-PREFLIGHT.md`, this directory) |
| 1 | A — reconcile active truth path (PROJECT-STATUS, pending register, decisions/README, PROCESS-GLOSSARY, AGENTS.md, README) | **done** — plus: DECISION-HISTORY.md created; charter's stale P-34 downstream row removed and views/router regenerated; 7 view-generator fixtures re-anchored; pre-existing dry-run render drift (red at clean `9c43fc5`) regenerated clean |
| 2 | B — Wave A/B act verification, install simulation, clean clone, owner action sheet | **done** — P-33 (M) verified; ceremony §2 step 3 redrafted to (M), §1 rows A/B + §7 item 11 de-staled (commit `96b3efd`); both manifest digests verified equal to the RD-31b/RD-32c-confirmed arguments; clean-clone battery 32 OK/18 WARN/0 FAIL; (M) install simulated in the clone, 19/19 + 11/11 rows OK from the governed home; action sheet is response-only (draft in the lead session's scratchpad) |
| 3 | C1 — P-41/P-42 consolidated repair as one model + semantic delta + blind fixture | **done** — CC-SPEC-1 re-grounded on SDR-37 (P-40 staleness discharged); CC-SPEC-11 minted (f14, bounded coverage model, warrant = convergence direction §9.2); CC-SPEC-8 completed (f15: "applicable" defined, reviewed-N/A rule homed); no CC-IMPACT clause moved; delta = `SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-2.md` (this dir); blind fixture already satisfied by fixture 2 + RD-59 PASS at matching digest; both packets and all 6 active CC-SPEC-range sites reconciled (37-hit sweep, review lane frozen). Repairs unconfirmed — Phase 4 reviews them |
| 4 | C2 — freeze; one combined adversarial review (fresh context) | pending |
| 5 | C3 — blocker-only repair (if needed); one confirming review | pending |
| 6 | C4 — P-41/P-42 craft-act offerings | pending |
| 7 | D — Capability 1 charter as one source; regenerate views; outline exercise | pending |
| 8 | E + F — formal v2.4 administration packet; governance-reduction plan; readiness answer | pending |
| 9 | Final verification (battery, clean clone, hosted CI), commit, push, stop-condition summary | pending |

## Files currently being edited by this pass

- (none — between phases)

## Ground rules this pass holds itself to

- No owner act is performed; no `openspec/` content; no implementation.
- Wave A/B bytes and launch-gate v2.4 are not re-reviewed or repaired.
- P-41/P-42 gets at most the one repair→review→repair→confirm cycle.
- Commits land at phase boundaries only, with in-flight co-lead work
  excluded per the staging discipline in `PROCESS-LESSONS.md`.
