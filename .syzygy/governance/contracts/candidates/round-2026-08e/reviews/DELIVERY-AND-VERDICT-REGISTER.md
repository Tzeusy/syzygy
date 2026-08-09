# Round-2026-08e review pass — delivery and verdict register

> **Process bookkeeping — never authority.** Raw reviewer output is stored
> verbatim in the `RD-*-RAW.md` files beside this register; verdict words
> below are copied exactly from those files. Every review in this pass is
> performed by an isolated fresh-context session reading only the frozen
> clone of commit `e8a4f36` (verification rule 7/10 baseline) unless its row
> states a later frozen commit. Working-tree edits after a review's frozen
> commit do not invalidate it; repairs batch into the next pass and
> dispositions are recorded before any frozen subject is edited (rule 10).
> Reviewer family: every reviewer in this pass is Claude-family (Fable 5).
> Per the owner's charter §5, none of these is — or may be presented as —
> the launch gate's family-diverse formal administration.

Register opened 2026-08-10. The charter (§5) requires nine named reviewers
before any wave offer; dispatch is deliberately staggered across the day at
the owner's direction.

## Review fleet (charter §5, nine reviewers — RD-24 … RD-32)

| Review | Charter role | Subject | Frozen commit | Parts stored | Verdict (copied exactly) | Blocking findings |
|---|---|---|---|---|---|---|
| RD-24 | Launch-gate reviewer | `launch-gate-pre-specifications.md` v1.4 — authority, scope, formula, reproducibility, administrability | `e8a4f36` | 1/1 | `VERDICT: REVISE` | RD24-01 — P-34's digest-bound approval and the same-change status edit cannot both hold; RD24-05 — §4 launch-scope rule vs formula unbridged (T1/T2: identical answers, opposite gate outcomes); RD24-09 — "F1 is not diverging" maps to no defined outcome and the named check can never fire (T3/T4) |
| RD-25 | Active-path truth reviewer | README onward — every default route | `395da99` | 1/1 | `VERDICT: REVISE` | RD25-01 — PROJECT-STATUS routes the owner to the retired 08d/P-29/P-30 plan; RD25-02 — "repairs have not begun" contradicted by four routed documents and the bytes; RD25-04 — candidate README names the superseded, unbannered D3 DRAFT as "The D3 proposal", with no digest for act 5 to fail on |
| RD-26 | Wave A reviewer | RFC 0001–0006 + launch-critical owner decisions | — | not yet dispatched | — | — |
| RD-27 | Wave B reviewer | RFC 0007–0009, the three surfaces | — | not yet dispatched | — | — |
| RD-28 | Specification-authoring reviewer | E1–E6 under the proposed authoring profile and first-spec charter | — | not yet dispatched | — | — |
| RD-29 | Human-language reviewer | README, overview, doctrine entry path, task routing | — | not yet dispatched | — | — |
| RD-30 | Owner-packet reviewer | each launch-critical decision packet, one-sitting test | — | not yet dispatched | — | — |
| RD-31 | Final Wave A exact-package reviewer | the exact regenerated Wave A argument — no authoring context | — | held until RD-24…RD-30 triage | — | — |
| RD-32 | Final Wave B exact-package reviewer | the exact regenerated Wave B argument — no authoring context | — | held until RD-24…RD-30 triage | — | — |
| RD-33 | Instrument re-reviewer (added — the nine are a minimum) | `launch-gate-pre-specifications.md` v1.5, exact bytes — the RD-24 repairs, which this session executed and may not confirm | — | held until the v1.5 repair commit | — | — |

**Ordering note.** RD-31/RD-32 are the offer gates: they bind the exact wave
arguments, so they run only after RD-24…RD-30 triage is disposed — if that
triage forces a wave-byte repair, the arguments regenerate and RD-31/RD-32
bind the fresh ones. Running them earlier would review bytes the pass might
still lawfully edit (rule 10 batches the fix, not the review).
