# Launch-gate v1.5 → v1.6 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.6 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer itself waits on a fresh-context re-review of this delta
> (**RD-34**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.5 as re-reviewed by RD-33 (subject sha256
`0522ef47757c4199a044ef10f98c78b1ff1d66adb2375d96dd08459593bdf898` at
commit `997d9bd`; raw review `reviews/RD-33-instrument-v15-RAW.md`,
`VERDICT: REVISE`, 0 BLOCKING / 5 MAJOR / 7 MINOR — and all 21 RD-24
repairs verified present, three by execution). Every delta below closes an
RD-33 finding; the dispositions are in `reviews/DISPOSITION-REGISTER.md`.
**No question's fail condition was narrowed, no verdict word was removed,
no ID renumbered.** Validator changes each carry a mutation fixture
(`scripts/launch_gate_results.py --selftest`, **34 fixtures**, including
— for the first time — fixtures for LG-7 and LG-2's digest-mismatch limb,
so the docstring's every-check-has-a-fixture claim is now true of the
bytes).

RD-33's pattern diagnosis, accepted whole: v1.5 made several checks live
for the first time, and three were defeated by the instrument's own text
or by absence — the RD24-19 absence-reads-as-success defect one level up.
Each delta below is that class closed at the level RD-33 found it.

## D-1 — Scoped-row disclosure checked, not trusted (RD33-01, MAJOR)

§4's scoped-form paragraph now states that the disclosure is the scoped
form's honesty and is checked: a record with any
`Not met (out of launch scope)` row whose deferred-wave findings line
names no defect is a validation error. New validator check **LG-9**
enforces it (RD-33's r2 — a self-contradicting record that validated
clean — is now a fixture). *Semantic change:* a requirement §4 already
stated in prose gains its check; nothing loosened.

## D-2 — Scoped findings visible to the trend log (RD33-02, MAJOR)

§6's trend table gains the **Scoped** column, with the rule stated in
place: *a scoped finding is a finding* — it registers in its own column,
rendering a defect scoped must never improve the read of any other
column, and a finding class invisible to every column would be invisible
to F1, which is answered from this log alone. The validator emits the
column, and the prior-vs-current comparison asymmetry RD-33 found in code
(`startswith("Not met")` on the prior side matching the scoped form,
`== "Not met"` on the current side) is fixed with one shared
normalization — a prior scoped row that turns plain `Not met` now counts
as a new finding (fixture, RD-33's r5). The empty
`decisions/launch-gate/TREND-LOG.md` header row is updated to the new
column set — lawful because zero administrations have bound the old
format. *Semantic change:* an instrument amendment (which is why this is
in the P-34 offer, not a post-approval patch); F1's evidence gains a
column and loses nothing.

## D-3 — Deferrals claimed only by citation (RD33-03, RD33-04, MAJOR)

§4's owner-deferral bullet now states that a deferral is claimed only by
**citation** — the record's `Owner deferral decision:` field naming the
granting owner decision; a reviewer's own evidence-cell wording is not a
deferral. A new §4 bullet states: **any deferral-carrying pass is
`READY-WITH-DEFERRALS`** — plain `READY FOR <target>` over any deferral
or nonzero `Deferred count:` is a contradiction and a validation error.
§5's template gains the `Owner deferral decision:` field and the plain
statement that the template's `(owner only)` parenthetical is a
description, never a satisfier. Validator: **LG-7 rewritten** (requires
the field for any `READY-WITH-DEFERRALS`; rejects a deferral-carrying
verdict with `Deferred count: 0`), and LG-6's plain-`READY FOR` branch
now requires F2 `Met` and zero declared deferrals — the `f2_deferral`
word-match regex (which RD-33's r4 satisfied from the reviewer's own
evidence cell) is deleted. Fixtures for r3, r4, and both new refusals;
plus a positive fixture (with-deferrals + citation validates). *Semantic
change:* the owner-only rule §4 already stated becomes enforceable; the
formula's F2-deferral limb is clarified to yield `READY-WITH-DEFERRALS`,
never plain `READY FOR` — a strengthening of the verdict-word contract,
weakening nothing.

## D-4 — The question roster bound (RD33-05, RD33-10, MAJOR + MINOR)

§5 now states the validator binds the full roster — A1–A6, B1–B5, C1–C7,
D1–D4, E1 with its five sub-rows, E2–E6, F1–F6, plus the G1 section — and
that a record missing any row is a validation error: absence of a
question is never a pass, and a delta administration's record cannot
support a gate decision (§2's full-vs-delta rule, now checked rather than
trusted). New validator check **LG-10** (RD-33's p2 — a READY record with
E5 deleted — is a fixture; the E1-rollup omission p4 that silently
disabled LG-8 is subsumed and fixtured). The reduced 11-row `GOOD`
selftest fixture is replaced by a **full §5-template-shaped record**
(RD33-08a), so template↔parser drift now breaks the selftest loudly.
*Semantic change:* the 39-row denominator becomes mechanical; no row
requirement removed.

## D-5 — Version and target agreement checked (RD33-06, MINOR)

New validator check **LG-11**: the record's `Instrument version:` must
match the committed instrument's `effective_version:` at the named
commit, and the record's `Launch target:` line must be the parameter
block's `LAUNCH_TARGET` (whitespace-normalized containment); a missing
`Launch target:` line errors regardless of git availability. RD-33's p5
(a record declaring v1.2 and "Capability 7" over correct v1.5 digests)
is now three fixtures. *Semantic change:* §5's existing verbatim-target
requirement gains its check.

## D-6 — §5's computed-vs-declared split stated honestly (RD33-09, MINOR)

§5 now states which trend figures are **computed from the rows**
(Not-met, Scoped, Unknown) and which are **declared required fields the
validator parses** (Deferred, Reopened) — declared, not computed, which
is exactly why their absence errors instead of reading zero. The
validator's per-run print says the same split instead of the blanket
"never transcribed" sentence RD-33 flagged as sitting beside two parsed
figures. *Semantic change:* presentation honesty only; both requirements
unchanged.

## D-7 — §6 project-invariant in bytes (RD33-07b, MINOR; RD24-14's secondary limb)

§6's project-specific pilot paragraph (the 2026-08-09 v1.3
administration, commit `067d8a0`, and the four reasons it does not open
the formal trend) moves verbatim-in-substance to the trend log's own
header (`decisions/launch-gate/TREND-LOG.md`), where project-specific
record-keeping lives. §6 keeps only the invariant rule: the formal trend
begins with the first administration meeting §2's integrity requirements,
and any earlier non-conforming administration is recorded in the trend
log's header, never in §6. *Semantic change:* no rule moved except its
home; §7's "everything project-specific lives in the parameter block" is
now true of §6's bytes — the claim the v1.5 delta made prematurely.

## D-8 — E4's silence rule (RD33-12, MINOR)

E4 now instructs: where the routing authority is silent on a case, the
reviewer records `routing authority silent` in the evidence, the silent
case counts as neither agreement nor disagreement, E4 is judged over the
cases the authority actually answers with the silent ones enumerated, and
silence over a case the launch target needs routed is a finding in its
own right. *Semantic change:* a defined rendering for a state the
instrument previously left to the reviewer; E4's fail conditions
unchanged.

## D-9 — P-34 packet corrections (RD33-08b, RD33-11, MINOR)

The governs-list alignment is restated as a reviewable claim by the
repair pass that the owner verifies at the act — not settled fact — with
rejection open under option (b) (RD33-08b). The mechanism's ordering now
covers option (b): amendments are applied in the working tree **before**
step 2's digest, with the changelog entry, in the one act commit
(RD33-11). The packet's version references move to v1.6 and its offer
status states the RD-34 precondition. *Semantic change:* to the decision
packet only.

## D-10 — The v1.5 delta's two false claims, corrected here (RD33-07a/b)

`LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md` is a reviewed, frozen record (RD-33
read it at `997d9bd`) and is **not edited**. Its two claims RD-33 found
untrue of the bytes are corrected here instead: (a) its D-6 said D2's
"front door", D3/F4's "default reading path", *and §4's blocking
condition 1* "all now name" `DEFAULT_ROUTE_SET` — in the v1.5 bytes only
D2 and D3 named the parameter inline; F4 and §4's condition 1 were bound
by §8's binding sentence alone (RD24-07 stayed closed because that
binding is unambiguous, but the claim overstated). (b) Its D-7 said §6
"returns to being project-invariant" — untrue at v1.5, where the pilot
paragraph remained; true only as of this delta's D-7.

## What did not change

Question IDs and texts A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1 —
unchanged except E4's silence rule recorded above (no stem or fails-when
narrowed). §1 derivation tiers, §3 order, §7 generalization path, §8's
parameters and populations, and the closed verdict vocabulary —
unchanged: the vocabulary gained no word this time, and no word was
removed. The §4 formula's conjuncts are unchanged in substance; the
F2-deferral limb's verdict-word consequence is now explicit.
