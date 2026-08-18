# Pending owner decisions — register

> **Status: every item below is PENDING. This file decides nothing, adopts
> nothing, accepts nothing.** It makes the open decision queue explicit and
> clone-visible. Each row points at the record that owns the full detail;
> where this file and an owning record disagree, the record wins and this
> file is stale.
>
> **As-of: 2026-08-17** — refactored (convergence pass, round 2026-08i):
> the default sections now hold **only currently open decisions and
> unperformed acts**. Resolved rows — including the eight launch-critical
> rulings and the P-34 approval of 2026-08-16 — and the register's own
> as-of chronology live in [`DECISION-HISTORY.md`](DECISION-HISTORY.md);
> the pre-refactor row narratives are preserved verbatim in git history at
> commit `9c43fc5`.
>
> **Updated 2026-08-17 (later the same day):** four acts were performed —
> Waves A and B, then craft acts 6 and 7 (P-41/P-42, one sitting). The
> executed rows moved to `DECISION-HISTORY.md`; P-22 and P-28 resolved by
> §7 ratification at the acts; P-21 stays open (sub-question (a) unruled).

## The acceptance acts (four performed; the rest open)

Exact phrases, digests, and the ceremony live in
`../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`.
**Verify every digest before acting** — `python3 scripts/check_governance.py`
(check CG-7) compares each act argument against its subject artifact; a
CG-7 failure means "do not perform that act." The acceptance record's §7
(imperfections before the phrase) is part of each wave's knowing acceptance
— read it before any act (§2 step 0).

| # | Decision | Owning record |
|---|---|---|
| P-1 | **The six foundational wave acts — the two launch-path acts are PERFORMED.** **Wave A and Wave B were both accepted 2026-08-17** (A then B), each over its confirmed argument (RD-31b / RD-32c), the 30 modules installed at `contracts/rfcs/` (shape (M)); record in `ACCEPTANCE-ACT-RECORD.md` (this directory). What remains open under this row: Waves C1/C2 (RFC-0011) and D1/D2 (RFC-0010), which carry no confirming review and stay deferred per `../contracts/candidates/DEFERRED-WAVE-POSTURE.md` | acceptance record §1; `ACCEPTANCE-ACT-RECORD.md`; digests `contracts/candidates/wave-manifests/WAVE-*-MANIFEST.txt` |
| P-2 | **Act 2** — confirm craft amendment CC-TEST-2 | acceptance record §1 row 2; digest block in `../policies/craft-and-care/INSTALL-RECORD.md` (**2026-08-06 correction** block holds the current argument) |
| P-3 | **Act 3** — accept the topology bundle | acceptance record §1 row 3; `../../map/topology-candidates/BUNDLE-MANIFEST.md` |
| P-4 | **Act 4** — adopt the project overview | acceptance record §1 row 4; `../../intent/OVERVIEW.md` |
| P-5 | **Optional act 5** — adopt, amend, or decline the D3 bounded-mission doctrine amendment. Rule **P-24 (D4)** first — adopting D3 as written settles D4 by stipulation | `../contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1) |

**Act ordering:** A → B (P-1). Under the current deferred-wave posture no
C/D act is offered; perform the wave acts before act 5 so bounded-mission
terms do not become adopted doctrine with definitions only in unaccepted
contracts (acceptance record §7 item 8).

## Launch-scope index (a reading aid, never authority)

The launch target is **Capability 1**
(`../contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md`); its prerequisite
acts are **Waves A and B only** (`DEFERRED-WAVE-POSTURE.md`). Read the open
table through this lens:

- **Ratified at the Wave A act (2026-08-17):** P-28 (mission extension
  profile, §7 item 16) — resolved, see `DECISION-HISTORY.md`. P-21(a)'s
  presence also rode in, **unruled** (§7 item 18) — its row stays open below.
- **Ratified at the Wave B act (2026-08-17):** P-22 (the RFC9-8(a) registry
  placement, §7 item 17) — resolved, see `DECISION-HISTORY.md`.
- **Gate authoring the first spec:** satisfied 2026-08-17 — the two wave
  acts and craft acts 6 + 7 (P-41 + P-42) are all performed
  (`ACCEPTANCE-ACT-RECORD.md`). What still gates authoring is the launch
  gate, not any queue row here: Administration 1 (2026-08-18) returned
  `NOT READY` (`launch-gate/TREND-LOG.md`), and the owner's launch
  decision is separate.
- **Gate a deferral-bearing administration:** P-43.
- **Deferred with their waves (no C/D act is offered):** P-19, P-23, P-27,
  P-29, P-30, P-32, and the D3/D4 doctrine questions — see
  `DEFERRED-WAVE-POSTURE.md`.
- **Open but not launch-gating:** everything else below; each row states
  its own earliest gate where one exists.

Where this index and a row disagree, the row wins and this index is stale.

## Open, and only the owner can dispose

| # | Decision | Type | Blocks / earliest gate | Owning record |
|---|---|---|---|---|
| P-10 | Commission a confirming review of `SURFACE-CLAUSE-ROUTING-MATRIX.md`'s final bytes (all 199 routes) and the six newest RFC-0010 clauses, or knowingly defer | review posture | none — not launch-gating | the matrix; `round-2026-08/reviews/` |
| P-12 | Knowledge-hygiene craft policy — pick the 22-rule original or the ten-rule compaction; own `CONFIRM CRAFT AMENDMENT` act. Would also give CG-20/21/27 an authoritative home | craft act | not launch-gating | `KNOWLEDGE-HYGIENE-DECISION.md`; `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` + `…-COMPACT.md` |
| P-14 | License choice — four candidates, three `[Unknown]`s incl. copyleft reach; wants qualified legal review, never chosen autonomously | owner/legal decision | none stated | `LICENSE-DECISION-PACKET.md` (this directory) |
| P-15 | Whether a compact FD register follows the two extracted warrants into this directory, while the founder decision log stays founder-local | decision | none | queue entry only; FD-037 |
| P-16 | Approve the term registry (31 terms, T-01…T-31, six-plane state model) as working vocabulary, or amend. Doctrine's three-state thesis stays governing either way | decision | none — the registry stays candidate | `policy-candidates/TERM-REGISTRY.md` |
| P-17 | Eight foundational public terms have no adopted definition anywhere; the wave acts close this. Accepting the surface before then is a knowing deferral | knowing deferral | the wave acts / act 4 | term registry §authority coverage; `round-2026-08b/TERM-CLOSURE-REPORT.md` §9.3 |
| P-18 | Three doctrine/contract vocabulary seams (C-1…C-6): governance-category counts, "Claim" outside doctrine's frozen nouns, `evidence tier` vs `rendering tier` | ruling | before OpenSpec multiplies them (advisory) | `round-2026-08/TERM-MIGRATION-REPORT.md` |
| P-19 | Mission-envelope residuals — the RFC-0010 correction plane (RFC10-17…22) closes them only if the D-wave acts are performed | deferred with waves | D1/D2 offer | `DEFERRED-WAVE-POSTURE.md`; `round-2026-08b/reviews/RC-7-mission-safety-RAW.md` |
| P-20 | The fixture-set acceptance posture — the residue P-29 owns; coverage itself is closed (ten fixtures) | deferred | with P-29 | `round-2026-08/ROUND-DISPOSITIONS.md`; `round-2026-08b/FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md` |
| P-21 | Is `constrains:` the right relation for one-way constraints (arm a)? The declaration's **presence** was ratified when the Wave A and B acts were performed 2026-08-17 (§7 item 18: "the acts ratify its presence" while (a) rides in **unruled**) — the sub-question itself remains open; its consumer clause sits in deferred Wave C2 | ruling | before Wave C2 is offered, or at the first consumer of the relation | `round-2026-08c/CONTRACT-RELATION-CLOSURE-REPORT.md`; acceptance record §7 item 18 |
| P-23 | Mission-safety stage placement — hold the correction plane for V1 (propose-only V0), or ship it with V0; the ceiling and the plane move together | deferred with waves | D1/D2 offer | `round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`; `round-2026-08b/reviews/RC-7-mission-safety-RAW.md` |
| P-24 | Rule doctrine question **D4** before act 5 — D3's `vision.md` insertion otherwise settles D4 by stipulation; the reviewer's alternative text is carried in the packet | doctrine ruling | act 5 | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` §6; RC-7 F10 |
| P-25 | Editorial doctrine amendment qualifying the three "README glossary" citations (drafted, not performed); three terms remain undefined anywhere reachable | doctrine amendment — only the owner applies | none | `policy-candidates/DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md` |
| P-25(c) | The `actuator` definition — a minimal doctrine amendment with the exact glossary insertion, one inferred sentence flagged for the owner | doctrine amendment — only the owner applies | none | `policy-candidates/DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md` |
| P-27 | RFC10-18's correction-plane routing defects (RC-11) and RC-10's undisclosed residue — all inside deferred D-wave modules | deferred with waves | D1/D2 offer | `round-2026-08b/DISPOSITIONS-RC-11-RC-12.md` |
| P-29 | The Wave C2 acceptance criterion — write the blind-fixture reproduction standard into the manifest (arm a), or delete the conditional sentence and defer knowingly (arm b) | deferred with waves | Wave C2 re-offer | `round-2026-08d/reviews/RD-23-wave-c2-RAW.md` B1/B2 |
| P-30 | Form of the stop/containment repair — D1-side floor limbs (i), move RFC10-20 to D1 (ii), or merge the D acts (iii) | deferred with waves | D1/D2 re-offer | `round-2026-08d/reviews/RD-20…RD-21…RD-13…RD-14` raw reviews |
| P-32 | RFC11-15 ownership metadata at V0 — author the schema, or rule the honest-fallback limb permanent and say so plainly | deferred with waves | Wave C2 re-offer | `round-2026-08d/reviews/RD-23-wave-c2-RAW.md` M2 |
| P-43 | What marks a file as recording a **made** owner decision — `SDR-n` only, an `**Executed.**` marker, a front-matter field? LA-11's shape classification is defensible and unruled | convention ruling | before any administration rests on a deferral | this row; `round-2026-08g/reviews/RD-56-launch-machinery-v2.1-RAW.md` f5 |
| P-44 | A lagging-specification exception to CC-REV-2 — amend in place (arm a) or decline (arm b); declining costs nothing while no specification exists. **Reviewed in the P-41/P-42 cycle (RD-69): the offer itself needs repair before any arm-(a) act** — its "Owner charter §9.6" warrant resolves nowhere in-tree, and arm (a)'s appended text contradicts the "one structural carve-out" sentence it follows (RD-69 N4); arm (b) is verified costless and needs no repair | policy amendment offer | not launch-critical | `policy-candidates/CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md`; RD-69 register (`../contracts/candidates/round-2026-08i/reviews/`) |

**Nothing in this register is self-executing.** Acts happen only by the exact
ceremonies their owning records define, performed by the owner.
