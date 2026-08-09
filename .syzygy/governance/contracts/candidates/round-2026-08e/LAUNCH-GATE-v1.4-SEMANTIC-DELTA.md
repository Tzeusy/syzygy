# Launch-gate v1.3 → v1.4 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority; this delta records every change of meaning so
> "no question was weakened" is a reviewable claim rather than an assertion.
> Owner approval of v1.4 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md`.

Baseline: v1.3 as administered 2026-08-09 (sha256
`5b5e76535ebab73ec06351eb16094882f79d01b8eb786883b1411f4f0ebc49ad`,
tracked at HEAD `e69c923`). Every delta below is additive or clarifying;
**no existing question's fail condition was narrowed, no verdict word was
opened, no ID renumbered.**

## D-1 — Typed authority header (new)

A `status:` YAML block (a governance-lifecycle state, per the term registry's five-dimension rule) now declares the instrument's governance-lifecycle state, owner, effective version,
governs / does-not-govern, amendment process, and the canonical result home
(`.syzygy/governance/decisions/launch-gate/`). A three-artifact-class
lifecycle model (definition / administration record / owner launch
decision) is stated in the preamble, closing the pilot-era ambiguity in
which the instrument, its results, and the launch decision shared one file
class. *Semantic change:* an administration verdict is now explicitly never
an owner act (previously implied by "the owner reads the verdicts and
decides"; now stated).

## D-2 — §2 administration integrity requirements (new)

A formal administration must: run against a **committed** instrument; quote
the instrument sha256 and the §8 parameter-block sha256; be full, not
delta; disclose reviewer model family, and disclose when family diversity
was not achieved; and never be administered by the session that repaired
the bytes under judgment. *Motivation:* all four are the pilot's recorded
defects (§6 pilot note). *Semantic change:* a record missing these cannot
support a gate decision — a strengthening.

## D-3 — Launch scope (§4 + §8) (new)

The gate is administered against a named `LAUNCH_TARGET` with
`REQUIRED_WAVES` / `DEFERRED_WAVES` / `DEFERRED_WAVE_POSTURE` fixed in the
parameter block. A–D remain answered repository-wide; a defect living only
in a deferred wave's candidate semantics blocks only under the five stated
conditions (default route / required-wave meaning / launch-target
dependency / current-truth misstatement / owner comprehension). *Semantic
change:* the verdict becomes `READY FOR <LAUNCH_TARGET>`; the previous
unscoped reading (every wave's semantics implicitly required) is retired.
This is a scoping, not a weakening: source-of-truth and hygiene questions
are explicitly never scoped away, and out-of-scope defects stay recorded
findings.

## D-4 — Verdict formula strengthened (§4)

v1.3: every E Met ∧ no Not-met in A–D ∧ F1 not diverging.
v1.4 adds three conjuncts: **F3 Met** (owner packet without archaeology),
**F4 Met** (default path safe to abandon), **F2 Met or explicitly
owner-deferred with a bounded reduction plan**. *Semantic change:* strictly
harder to pass.

## D-5 — A5 population fixed (amended in place)

A5's population is the closed `MAJOR_SHAPE_COMMITMENTS` list (11 entries,
§8) with a required two-way table (commitment → named consumer need;
consumer → ≥1 commitment) as evidence, never new authority. *Motivation:*
the pilot returned Unknown solely because A5's universal had no defined
population — a meaningless 341-clause table was the only literal reading.
*Semantic change:* the question became administrable; its fail condition is
unchanged.

## D-6 — E4 cases fixed (amended in place + §8 `E4_CASES`)

Six candidate statements are fixed in the parameter block, written in
ordinary language (no clause IDs — §1's derivation rule is honored), one
per boundary class: graph identity, registration behavior, visual Unknown,
review obligation, machine endpoint, propagation rule. The project's
routing disagreeing **with itself** over parallel cases is now an explicit
fail limb (the pilot's actual E4 failure mode). *Semantic change:*
comparability across administrations; a fail limb added, none removed.

## D-7 — D2 tasks promoted from suggested to fixed (§8)

The three routing tasks are unchanged in text; "suggested" became "fixed".
The pilot already used them as fixed.

## D-8 — New questions C7, F5, F6 (appended)

From the pilot's G1, three of its four proposals, each universal,
falsifiable, and administrable in-session:

- **C7** successor recoverability (clone-only continuation, rationale for
  irreversible decisions distributable);
- **F5** assurance independence (substantive, not procedural — with
  instrument capture folded into its second limb: amendment history
  separable from corpus failures, §6's amended-question flag);
- **F6** governance effort per delivered increment (bounded, declining,
  declared ceiling).

**Declined: a standalone G2 ("instrument capture").** Reason: its first
limb (administering party's interests differ from the authors') is F5's
substantive-independence test applied to the gate itself, and its second
limb (amendment-history separability) is now F5's parenthetical plus §6's
existing "a trend across amended questions is not a trend" rule. A separate
question would double-count one failure into two Not-mets. Recorded here so
the proposal is answered, not lost.

## D-9 — Results record format (§5)

Gains: instrument version + sha256, parameter-block sha256, launch target,
same-family disclosure line, and a "deferred-wave findings recorded outside
launch scope" line. Names `scripts/launch_gate_results.py` as the record
validator (13 mutation fixtures, all failing when they should; the
instrument, not the tool, owns readiness semantics).

## D-10 — §6 pilot note (new)

The 2026-08-09 v1.3 administration is bound as **pilot steering evidence,
not the formal trend baseline**, with the four reasons recorded, its
findings preserved, and the standing instruction that its documented
corpus-level recurrence (the retired-phrase defect) belongs in the Reopened
column of the first formal administration if still present.

## What did not change

Question IDs A1–A6, B1–B5, C1–C6, D1–D4, E1–E6, F1–F4, G1 — text unchanged
except A5/E4 as recorded above. Verdict vocabulary unchanged. §1 derivation
tiers, §3 order, §6 trend-log columns, §7 generalization path unchanged.
The retired reading "Ready to begin specifications" (unscoped) survives
only inside the v1.3 pilot record, which is historical.
