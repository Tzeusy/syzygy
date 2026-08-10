# Wave A closure report — round-2026-08e

> **Process record, never authority.** This report summarizes the Wave A
> repair-and-confirmation arc for the owner. The acceptance authority is
> `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (§1 row A owns the
> phrase and the digest; §7 owns the disclosures); the raw reviews beside
> this report are the evidence. Nothing here is an act, and this report
> decides nothing.

Closed 2026-08-10. **The Wave A package is offer-ready and confirmed; the
offer is withheld by exactly one owner ruling, P-33.**

## 1. Subject

- **Wave A**: RFC 0001–0006 — 19 modules, bound by
  `../wave-manifests/WAVE-A-MANIFEST.txt`.
- **Current argument** (manifest digest, computed by
  `scripts/build_active_manifest.py`, verified by CG-7):
  `8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a`
- **Stale predecessors**, each banner-marked where quoted, satisfying
  nothing: `6b98e0c6…` → `8af6805f…` → `c649143b…` (three script-driven
  regenerations; the history is stated in §1 row A itself).

## 2. The review-and-confirmation chain

| Review | Subject | Frozen commit | Verdict (copied exactly) |
|---|---|---|---|
| RD-26 (dimension review) | RFC 0001–0006 + launch-critical decisions | `aaff6fa` | `VERDICT: REVISE` |
| RD-31 (exact-package, first administration) | argument `c649143b…` (stale since the §15 repair batch, satisfying nothing) | `cd484b7` | `VERDICT: REVISE` |
| RD-31b (exact-package, second administration) | argument `8972d963…` | `1a23d19` | `VERDICT: CONFIRM` |

RD-31b is the round's first CONFIRM. Its operative sentence, quoted
exactly from `reviews/RD-31b-wave-a-RAW.md`:

> Yes — these bytes are offer-ready. The Wave A act may be offered on
> argument `8972d963…` once, and only once, P-33 is ruled.

A repair session may not confirm its own repaired bytes: every verdict
above was produced by an isolated fresh-context session reading only a
frozen clone, and RD-31b read the exact regenerated package with no
authoring context.

## 3. What was repaired (the RD-31 batch — delta §15, five digest-moving modules)

- **RFC3-2 ↔ RFC3-15 closure** (RD31-01, BLOCKING): the two clauses now
  state the same two admission triggers at both sites, quote trigger 2
  word-for-word across them, and cite in both directions so neither can
  be amended alone. The reproducibility dilemma RD-31 raised is answered
  by locating the sweep resolution record's irreducible content in the
  sweep's *instant* — RD-31b judged this "a genuine third branch, not a
  rhetorical one."
- **Provenance safeguard** (RD31-04, MAJOR): the sweep-resolution record
  member of `records/` carries a stated authority chain — policy gated in
  `policies/` under RFC3-16(a) → kernel verifies provenance → record
  admissible; an unbacked record is inadmissible and the suspension
  holds.
- **Sub-clause declarations** (RD31-03, MAJOR): RFC-0002's README
  declares RFC2-19(a) at all three sites; RD-31b swept all 14 Wave A
  lettered sub-clauses against all six front-matter declarations and
  found the class closed, not just the instance.
- **§7 item 18** (RD31-05, MAJOR): the Wave A act is disclosed as the
  first act freezing the `constrains:` relation while P-21(a) is open.
- **One marking convention** (RD31-06/RD31-08, MINOR): every in-clause
  drafted arm names its P-number, the awaiting-ruling state, and the
  ratify-or-revert consequence.
- **Dependency truth** (RD31-07, MINOR): `manifests-and-namespace.md`
  and the RFC-0003 package index drop the non-reliance RFC-0004 edge
  (CG-13's union rule forced the index edit — the fifth digest movement,
  recorded in delta §15 per RD-31b N-2).

## 4. What rides into the act, disclosed

Six drafted or unruled answers ride in — **all six disclosed at §7, each
cross-reference verified by RD-31b (6 of 6)**: the `declarations/`
category (item 1), RFC2-19(a)/P-31 (item 12), the `records/` widening
(item 14(a)), `unknown-terminal` (item 14(b)), the P-28 mission profile
entry (item 16), and the P-21(a) `constrains:` freeze (item 18). Each is
ratified by the act or reverted by the owner — stated in the record's own
voice, so the act is a knowing one (the RD-8 standard).

## 5. What withholds the offer

**P-33 alone** (Wave A installation shape —
`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`). §7 item 11 states, in the
record's voice: *"Until P-33 is ruled, this record offers no Wave A
act."* RD-31b: RD31-02 "was never a defect in the package, and the
register's disposition **O** was the right call." No byte repair can
settle it; it is a ceremony question owned by the owner.

## 6. Measured state (RD-31b's sweeps, denominators stated)

`[Observed]` (by RD-31b at `1a23d19`; the argument is byte-identical at
the current commit):

- 19/19 module digests recompute; the argument recomputes to
  `8972d963…`.
- Cross-wave containment: `depends_on` union over 19 modules stays inside
  {RFC-0001…0005}; **zero** edges into RFC 0006–0011.
- 63 cross-wave clause tokens across 35 lines in 9 modules — all
  classified by reading, **zero reliances**; no rule requires a deferred
  wave's text to evaluate.
- Ceremony phrases: 19 modules × 7 strings — **0 hits**.
- Self-presents-as-accepted: 3 hits, all conditional/forward — **0
  defects**.
- Candidate banner: on **8 of 19** modules, the rest covered by the
  directory-level marker CG-4a names (RD-31's original 19/19 figure was
  over-broad — corrected by RD-31b, and the corrected figure is the one
  this report carries).
- "Forward references are informative" paragraph: **6 of 19**; every
  cross-wave citation in the other modules is self-marked at the site
  (RD-31's 19/19 figure likewise corrected; no forward reference is
  unmarked).

## 7. Carried forward, deliberately not repaired here

Per rule 10 and RD-31b's own direction ("batching them now would retire
`8972d963…` … and buy nothing an owner performing the act would
notice"):

- **N-1** (MINOR): RFC3-2 ¶1/¶2's class characterization lags the
  two-trigger rule ¶3 states; trigger 1's qualifier differs from
  RFC3-15's by one word. No operative divergence (verified). Tracked as
  bd issue **syzygy-4si**; any future pass that moves Wave A bytes folds
  it in, regenerates, and re-runs the offer gate.
- N-2 and N-3 were record corrections outside the manifest — repaired
  2026-08-10 with dated markers (delta §15 and the disposition
  register's RD31-06 row).

## 8. The offer, when it opens

When the owner rules P-33, the Wave A act may be offered on argument
`8972d963…` exactly as §1 row A states it. The acceptance record owns
the phrase and the ceremony; this report is a summary of evidence, and
if it disagrees with the acceptance record, the record wins.
