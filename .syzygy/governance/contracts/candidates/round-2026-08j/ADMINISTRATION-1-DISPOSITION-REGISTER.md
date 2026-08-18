# Administration 1 — repair-pass disposition register (round 2026-08j)

> **Register, never authority.** One row per Administration 1 finding
> (record:
> `../../../decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json`,
> verdict `NOT READY`, 2026-08-18), stating what this repair pass did
> with it. A "repaired" row claims only that the named defect's cited
> instances were repaired — Administration 2 owns the re-grading, and
> nothing here predicts its verdicts. Pass date: 2026-08-18.

## Verdict rows

| Q | Was | Disposition |
|---|---|---|
| A1–A5 | Met | No action needed. |
| A6 | Unknown | **Owner input queued — P-45** (`decisions/ADMINISTRATION-1-OWNER-INPUTS-DECISION.md`): the resource envelope with the named proving project, or dated re-affirmed Unknowns. |
| B1, B2 | Not met (scoped, deferred-wave-only) | **No action, by the gate's own scoping** — the C1↔C2 cycle is confined to deferred waves, met zero blocking conditions, and its repair belongs to the wave re-offer (open queue rows P-29/P-30/P-32 carry the deferred-wave repairs). |
| B3 | Met | No action needed. |
| B4 | Not met | **Structural — disclosed, not repaired.** Rejecting Wave A collapses Wave B and Capability 1 because Wave A is the foundation the sequence declares; no documentation change alters that dependency, and pretending partial survivability would be the defect. The honest state: the A→B chain was accepted knowingly (acts of 2026-08-17), and the "any single chunk rejectable" property holds only for the deferred chunks. Recorded here for Administration 2 to weigh as a property, not an oversight. |
| B5 | Unknown | **Settled by artifact — [`THESIS-RISK-ORDERING.md`](THESIS-RISK-ORDERING.md)**: six assumptions ranked, each mapped to its earliest falsifier; rankings `[Inferred]`, owner-amendable. |
| C1 | Met | No action needed. |
| C2 | Unknown | **Settled by artifact — [`C2-NORMATIVE-POPULATION-REPORT.md`](C2-NORMATIVE-POPULATION-REPORT.md)** + its sweep script: 425 files / 8,276 modal lines classified into owner classes; the five conflict-resolution rules quoted; the known residual (CG-20/21/27 → P-12) stated. |
| C3 | Not met | **Repaired at filing (commit `d9261b7`)**: README acceptance state, packet §7, contract-index regeneration. This pass added the router's stale-status repair (generator note rewritten; see D2). |
| C4–C6 | Met | No action needed. |
| C7 | Not met | **Owner-gated — already queued as P-15**; no duplicate row minted. The founder-local D1 rationale can only reach the clone by the owner supplying it. |
| D1 | Not met | **Repaired at filing** (the conflicting current-state claims were the same staleness class as C3/D4); this pass re-walked the route set after the router repair. |
| D2 | Not met | **Repaired this pass — at the generator.** `build_task_router.py` now maps every Wave A/B-manifest module to its governed home `contracts/rfcs/` (existence-guarded; deferred modules keep candidate homes), and the Capability 1 route note states the accepted post-act state. The two failing fixed tasks (evidence-adapter, seam trace) now route to accepted homes; the Mission task stays correctly deferred-routed. |
| D3 | Unknown | **Settled by artifact — [`D3-COINED-TERM-REPORT.md`](D3-COINED-TERM-REPORT.md)** + its sweep script: all 41 terms enumerated with first default-path use and definition site; 20 never surface on the default path (stated, with the re-check trigger). |
| D4 | Not met | **Repaired at filing** — root README was the one failing entry document; re-swept clean by CG-27 this pass. |
| E1–E6 | Met | No action needed. |
| F1 | Unknown | **Not settleable by a repair pass by definition** — needs Administration 2 declaring this record as prior. The stop-condition half of its settlement is queued as **P-48**. |
| F2 | Not met | **Part-repaired, part-queued.** Repaired this pass: the superseded task index moved to `history/` (49 embedded measurements off the active lane), the load map's and candidates-README's residual figures removed (CG-20: 52 findings → 0), and the sealed packet gained its correction path (§7 corrected with the seal digests untouched — the retirement-path defect instance). Queued: the reduction plan's standing is **P-47**. |
| F3 | Not met | **Repaired at filing** — the packet's false acceptance-state section corrected, dated, seal digests unmoved. |
| F4 | Not met | **Repaired at filing + this pass** — stale claims corrected at their sources, index drift regenerated, and the two generators that emitted stale text (router note) fixed so the staleness class cannot silently return there. |
| F5 | Met | No action needed. |
| F6 | Not met | **Owner input queued — P-46** (declare a ceiling, or record the case-by-case posture knowingly). |
| G1/H1 | proposal | **Carried into P-45**: the proposed H1's substance (a named proving project with a predeclared evaluation plan) is the envelope's proving-project field. Whether H1 becomes an instrument question is an owner option on the instrument (a bounded v2.5 remains "an owner option, not a gate" — P-34 record). |

## What this pass deliberately did not do

- No edit to any act-bound artifact, the instrument, the schema, or the
  validator/renderer (the five seal digests are unmoved).
- No re-administration, no self-grading: every "repaired" claim above is
  a byte-level claim about named files, checkable by diff against
  `d9261b7`, not a claim that a question now grades `Met`.
- No LICENSE/enactment or canonical recording of the 2026-08-18
  questionnaire rulings (P-14/P-16/P-24/P-44) — their own records gate
  application on an explicit owner request, which had not been given
  when this register was written.
