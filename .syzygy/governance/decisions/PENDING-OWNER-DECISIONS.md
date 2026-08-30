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
>
> **Updated 2026-08-19:** four rulings from the owner's 2026-08-18
> questionnaire sitting applied on explicit request — P-14 (MIT), P-16
> (term registry as drafting vocabulary), P-24 (D4: inside VIS-4's
> bounds), P-44 (CC-REV-2 exception declined). Rows moved to
> `DECISION-HISTORY.md`; each has its own decision record in this
> directory. P-45…P-48 were added 2026-08-18 by the Administration-1
> repair pass.
>
> **Updated 2026-08-19 (later the same day):** the Administration-1
> owner inputs **P-45…P-48 were all ruled** in one adversarially-reviewed
> questionnaire sitting and applied on explicit request — the A6
> envelope stated with syzygy named the first proving project (P-45), no
> governance ceiling declared with case-by-case recorded knowingly
> (P-46), the governance-reduction plan adopted as directed work (P-47),
> and the launch-repair cycle bounded at two further administrations
> (P-48). Rows moved to `DECISION-HISTORY.md`; each has its own decision
> record in this directory.

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
| P-5 | **Optional act 5** — adopt, amend, or decline the D3 bounded-mission doctrine amendment. **P-24 (D4) was ruled 2026-08-18: inside VIS-4's bounds, with the reviewer's §1.2 wording designated for act 5** (`D4-RULING-DECISION.md`) — a D3 rev2 carrying that wording, plus the VIS-3 fresh-reader review D3 §5 requires, precede the act | `../contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1); `D4-RULING-DECISION.md` |

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
  P-29, P-30, P-32, and the D3 adoption question (D4 itself was ruled
  2026-08-18 — `D4-RULING-DECISION.md`; act 5 stays open as P-5) — see
  `DEFERRED-WAVE-POSTURE.md`.
- **Open but not launch-gating:** everything else below; each row states
  its own earliest gate where one exists.

Where this index and a row disagree, the row wins and this index is stale.

## Open, and only the owner can dispose

| # | Decision | Type | Blocks / earliest gate | Owning record |
|---|---|---|---|---|
| P-10 | Commission a confirming review of `SURFACE-CLAUSE-ROUTING-MATRIX.md`'s final bytes (all 199 routes) and the six newest RFC-0010 clauses, or knowingly defer | review posture | none — not launch-gating | the matrix; `round-2026-08/reviews/` |
| P-12 | Knowledge-hygiene craft policy — pick the 22-rule original or the ten-rule compaction; own `CONFIRM CRAFT AMENDMENT` act. Would also give CG-20/21/27 an authoritative home | craft act | not launch-gating | `KNOWLEDGE-HYGIENE-DECISION.md`; `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` + `…-COMPACT.md` |
| P-15 | Whether a compact FD register follows the two extracted warrants into this directory, while the founder decision log stays founder-local | decision | none | queue entry only; FD-037 |
| P-17 | Eight foundational public terms have no adopted definition anywhere; the wave acts close this. Accepting the surface before then is a knowing deferral | knowing deferral | the wave acts / act 4 | term registry §authority coverage; `round-2026-08b/TERM-CLOSURE-REPORT.md` §9.3 |
| P-18 | Three doctrine/contract vocabulary seams (C-1…C-6): governance-category counts, "Claim" outside doctrine's frozen nouns, `evidence tier` vs `rendering tier` | ruling | before OpenSpec multiplies them (advisory) | `round-2026-08/TERM-MIGRATION-REPORT.md` |
| P-19 | Mission-envelope residuals — the RFC-0010 correction plane (RFC10-17…22) closes them only if the D-wave acts are performed | deferred with waves | D1/D2 offer | `DEFERRED-WAVE-POSTURE.md`; `round-2026-08b/reviews/RC-7-mission-safety-RAW.md` |
| P-20 | The fixture-set acceptance posture — the residue P-29 owns; coverage itself is closed (ten fixtures) | deferred | with P-29 | `round-2026-08/ROUND-DISPOSITIONS.md`; `round-2026-08b/FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md` |
| P-21 | Is `constrains:` the right relation for one-way constraints (arm a)? The declaration's **presence** was ratified when the Wave A and B acts were performed 2026-08-17 (§7 item 18: "the acts ratify its presence" while (a) rides in **unruled**) — the sub-question itself remains open; its consumer clause sits in deferred Wave C2 | ruling | before Wave C2 is offered, or at the first consumer of the relation | `round-2026-08c/CONTRACT-RELATION-CLOSURE-REPORT.md`; acceptance record §7 item 18 |
| P-23 | Mission-safety stage placement — hold the correction plane for V1 (propose-only V0), or ship it with V0; the ceiling and the plane move together | deferred with waves | D1/D2 offer | `round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`; `round-2026-08b/reviews/RC-7-mission-safety-RAW.md` |
| P-25 | Editorial doctrine amendment qualifying the three "README glossary" citations (drafted, not performed); three terms remain undefined anywhere reachable | doctrine amendment — only the owner applies | none | `policy-candidates/DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md` |
| P-25(c) | The `actuator` definition — a minimal doctrine amendment with the exact glossary insertion, one inferred sentence flagged for the owner | doctrine amendment — only the owner applies | none | `policy-candidates/DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md` |
| P-27 | RFC10-18's correction-plane routing defects (RC-11) and RC-10's undisclosed residue — all inside deferred D-wave modules | deferred with waves | D1/D2 offer | `round-2026-08b/DISPOSITIONS-RC-11-RC-12.md` |
| P-29 | The Wave C2 acceptance criterion — write the blind-fixture reproduction standard into the manifest (arm a), or delete the conditional sentence and defer knowingly (arm b) | deferred with waves | Wave C2 re-offer | `round-2026-08d/reviews/RD-23-wave-c2-RAW.md` B1/B2 |
| P-30 | Form of the stop/containment repair — D1-side floor limbs (i), move RFC10-20 to D1 (ii), or merge the D acts (iii) | deferred with waves | D1/D2 re-offer | `round-2026-08d/reviews/RD-20…RD-21…RD-13…RD-14` raw reviews |
| P-32 | RFC11-15 ownership metadata at V0 — author the schema, or rule the honest-fallback limb permanent and say so plainly | deferred with waves | Wave C2 re-offer | `round-2026-08d/reviews/RD-23-wave-c2-RAW.md` M2 |
| P-43 | What marks a file as recording a **made** owner decision — `SDR-n` only, an `**Executed.**` marker, a front-matter field? LA-11's shape classification is defensible and unruled | convention ruling | before any administration rests on a deferral | this row; `round-2026-08g/reviews/RD-56-launch-machinery-v2.1-RAW.md` f5 |
| P-49 | The accepted RFC-0007 module `narrative-contract.md` claims sub-clauses `RFC7-2(a)–(c)` and `RFC7-9(a)–(c)` in its frontmatter and closing summary, but **defines none of them in the module body** — the family count reads 41 by definition-header sweep, 47 by the module's own claim (accepted population 324 vs 330). Amend the module's count claims, or define the sub-clauses, or rule the frontmatter non-authoritative on counts | module amendment ruling — an accepted module's bytes; only the owner amends | before any artifact's clause-population claim must survive an adversarial count | `round-2026-08k/reviews/RS-3-AUTHORITY-RAW.md` observation 2; `contracts/rfcs/RFC-0007/narrative-contract.md` |
| P-50 | Capability 1 charter row 1.1's phrase **"never partial registration"** (atomicity of the registration transition) is anchored to no clause. `RFC3-9` fixes only the *consequence* of an invalid declaration (every dependent claim renders Unknown; no auto-repair) and `RFC3-5` fixes only the closed top-level field set — neither states an all-or-nothing registration transition, and verification rule 8 bars justifying a clause-level claim from adjacent prose. Two lawful repairs, both owner-only: **(a)** amend an accepted Wave A/B module (`RFC3-5` or `RFC3-9`) to state the atomic transition — enlarges what the owner already accepted, since RFC 0003 is bound; or **(b)** drop the atomicity phrase from `CAPABILITY-1-CHARTER.yaml` row 1.1 — weakens a row the owner deliberately authored. Recommend (b): a charter-row edit is the smaller, more reversible change against a module the owner has already accepted, but the owner may prefer (a) if atomic registration is intended production behavior. **Default if unanswered: neither repair is made — row 1.1 keeps the unanchored phrase, and no spec built on row 1.1 may cite atomicity as clause-backed until this rules** | contract amendment or charter ruling — only the owner disposes | before any spec cites row 1.1's atomicity as clause-backed | `round-2026-08g/reviews/RD-60-capability-1-outline-exercise-RAW.md` R1.1-A / observation B3; `contracts/rfcs/RFC-0003/manifests-and-namespace.md` (RFC3-5, RFC3-9); `contracts/candidates/CAPABILITY-1-CHARTER.yaml` row 1.1 |

**Nothing in this register is self-executing.** Acts happen only by the exact
ceremonies their owning records define, performed by the owner.
