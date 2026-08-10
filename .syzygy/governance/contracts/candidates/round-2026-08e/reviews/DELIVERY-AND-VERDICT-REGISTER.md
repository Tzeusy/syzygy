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
| RD-26 | Wave A reviewer | RFC 0001–0006 + launch-critical owner decisions | `aaff6fa` | 1/1 | `VERDICT: REVISE` | RD26-01 — the Wave A install breaches RFC3-15's "exclusively", P-33 unruled and its packet says the wave cannot be re-offered until ruled; RD26-02 — P-31/P-33/P-37 each name the Wave A act as their earliest gate and none appears in the acceptance record (the RD-8 surprised-act class, three instances) |
| RD-27 | Wave B reviewer | RFC 0007–0009, the three surfaces | `5bb8a36` | 1/1 | `VERDICT: REVISE` | RD27-02 — the owner-facing offering apparatus describes pre-repair bytes: RFC7-39's entry-is-primary-narrative ruling disclosed on no gate path, the P-38 packet states a three-value domain where RFC7-40 closes it at four, and packet 6 was re-blessed as current while stating the superseded RFC9-8(a) placement |
| RD-28 | Specification-authoring reviewer | E1–E6 under the proposed authoring profile and first-spec charter | `246af62` | 1/1 | `VERDICT: REVISE` | none — seven MAJOR (E4 routing authority silent on 11 of the first spec's 20 clauses with a self-refuting rationale; `spec/polaris` unminted; clause-vs-consequence unit mismatch; E6's invented CC-REV-2 exception limb and unowned detection step; the spec-acceptance craft act gateless; E1 rows unlabeled; fixture 8's unlabeled Wave C2 derivation), three MINOR |
| RD-29 | Human-language reviewer | README, overview, doctrine entry path, task routing | `eb7e486` | 1/1 | `VERDICT: REVISE` | RD29-01 — the owner's decision register routes act 2 to the superseded 2026-08-05 digest block (the RD-8 shape verbatim); RD29-02 — the status page's gate table and launch path omit P-41, the blocking spec-acceptance prerequisite |
| RD-30 | Owner-packet reviewer | each launch-critical decision packet, one-sitting test | `4599701` | 1/1 | `VERDICT: REVISE` | RD30-01 — P-37's "as drafted" seven-facet vocabulary appears in zero of the 30 Waves A+B modules (swept), yet three launch-path documents claim the Wave A act ratifies it — an owner ruling (a) would believe the act settles something it does not touch |
| RD-31 | Final Wave A exact-package reviewer | the exact regenerated Wave A argument `c649143b…` — no authoring context | `cd484b7` | 1/1 | `VERDICT: REVISE` | RD31-01 — the RD26-04 `records/` widening (RFC3-15) contradicts RFC3-2's own closure sentence ("only on an actor's submission"), which it cites as its authority — two conforming implementations disagree on the very record the repair exists to admit; RD31-02 — §7 item 11 states in the record's voice that no Wave A act is offered until P-33 is ruled, and P-33 is unruled with undrafted arms (a gate, not a byte defect — dispositive of the offer regardless of package quality). Mechanics impeccable: 19/19 digests recompute, zero reliance escapes over 113 classified cross-wave references, all five drafted arms disclosed. The argument `c649143b…` may not be offered; repairs batch, the argument regenerates, and the offer gate requires a fresh exact-package review of the new argument |
| RD-32 | Final Wave B exact-package reviewer | the exact regenerated Wave B argument — no authoring context | — | held until RD-24…RD-30 triage | — | — |
| RD-33 | Instrument re-reviewer (added — the nine are a minimum) | `launch-gate-pre-specifications.md` v1.5, exact bytes (sha256 `0522ef47…`, unchanged since the repair commit `395da99`) — the RD-24 repairs, which this session executed and may not confirm | `997d9bd` | 1/1 | `VERDICT: REVISE` | none BLOCKING — all 21 RD-24 repairs verified present (19 closed, 3 BLOCKING confirmed by execution); five MAJOR in the absence-reads-as-success class one level up: RD33-01 scoped row's disclosure requirement unenforced (self-contradicting record validates clean); RD33-02 scoped findings invisible in every trend-log column F1 is answered from, plus a `startswith`/`==` asymmetry; RD33-03 LG-7 satisfied by the template's own "(owner only)" label, no fixture; RD33-04 reviewer-self-authorized F2 deferral passes under plain `READY FOR`; RD33-05 question roster unchecked — a deleted E-row validates READY. Two (RD33-01/02) need instrument amendments → v1.6, so the offer requires a further re-review (RD-34) of the v1.6 delta by a session that did not author it |

| RD-34 | Instrument delta re-reviewer (added — same rule that added RD-33) | `LAUNCH-GATE-v1.6-SEMANTIC-DELTA.md` + the v1.6 instrument (sha256 `9d68fa3b…`) and validator bytes — the RD-33 repairs, which this session executed and may not confirm | `0bdd37d` | dispatched 2026-08-10, in flight (subject disjoint from wave bytes, same basis as RD-33's parallel run) | — | — |

**Ordering note.** RD-31/RD-32 are the offer gates: they bind the exact wave
arguments, so they run only after RD-24…RD-30 triage is disposed — if that
triage forces a wave-byte repair, the arguments regenerate and RD-31/RD-32
bind the fresh ones. Running them earlier would review bytes the pass might
still lawfully edit (rule 10 batches the fix, not the review).
