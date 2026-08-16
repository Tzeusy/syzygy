# Semantic delta 2 — the P-41/P-42 one-model amendment of 2026-08-17

> **The normative-change record for the round-2026-08i amendment** of
> `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
> (CC-SPEC) and `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`
> (CC-IMPACT), per `policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`.
> Successor to `../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`
> (the 2026-08-13 amendment against RD-51), which it does not modify.
>
> **Warrant for the amendment:** the owner's convergence-pass direction
> (2026-08-17, §9 of the pass charter): reconcile stale P-40 statements,
> close the E5 completeness gap with a bounded coverage model (§9.2), and
> close f15's two open limbs (§9.3). One consolidated repair; the repaired
> bytes then receive one combined fresh-context review. **A repair session
> cannot confirm its own repairs — nothing below is confirmed.**

## Changes to `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`

### D2-1 — CC-SPEC-1 re-grounded on the ruled SDR-37 (P-40 staleness)

**Before** (operative sentences): *"'One coherent capability' is the
granularity rule queued as **P-40**: [proposed rule text] … **P-40 is not
ruled** … This clause therefore states the rule it *proposes*, and its
force is conditional … **This clause may not be frozen before P-40 is
ruled.**"*

**After:** the clause cites the rule from `SURFACE-DECISION-RECORD.md`
**SDR-37** (ruled 2026-08-16), quoted exactly — *"one OpenSpec change
governs one coherent capability, or one coherent change to one: one
owner-readable product argument, one acceptance decision per change"* —
and the freeze conditional is removed as discharged.

**Semantic effect:** the clause's force is no longer conditional; its
warrant class moves from *proposed* to *recorded owner decision*. The
ruling confirmed the drafted rule, so no operative predicate changed —
the 2026-08-13 amendment's own condition ("if the owner rules P-40
arm (a), this clause is confirmed as written") resolved in the confirming
direction. `[Observed]` — SDR-37's text quoted from its owning record
this session.

### D2-2 — CC-SPEC-8 completed: "applicable" defined; the reviewed-N/A rule homed (RD-51 f15)

**Before:** *"…every applicable clause is covered by a requirement or
carries a reviewed N/A judgment whose home and provenance follow the
corpus's reviewed-N/A rule."* — with the parenthetical disclosure that
"applicable" was undefined and the reviewed-N/A rule's identifier
unresolved (a circular citation: this clause deferred to a rule the
routing matrix routed back to this clause).

**After:** (i) **"applicable" is defined** — a clause is applicable when
*"the capability uses the entity, behavior, authority boundary, state
vocabulary, or interface the clause governs"*, applied clause-by-clause
against the CC-SPEC-1 scope statement; (ii) **CC-SPEC-8 is declared the
reviewed-N/A rule's one home**, and every N/A judgment records five named
fields — clause, reason, scope, confirmer (never the author alone,
CC-TEST-4 pattern), provenance. The circular deferral is deleted.

**Semantic effect:** two obligations previously undischargeable for want
of a definition and an identifier become dischargeable; no obligation is
weakened. The confirmer limb (2026-08-13) is unchanged.

### D2-3 — CC-SPEC-11 minted: capability completeness (RD-51 f14; E5's "complete" limb)

**Before:** no clause tested a specification's requirement set for
completeness against its declared capability (f14, deliberately open at
the 2026-08-13 amendment for want of a directing charter).

**After:** new clause **CC-SPEC-11** — the full text is in the candidate —
requiring a coverage table whose population is the declared capability
obligations (from the CC-SPEC-1 scope statement, counted), each placed in
exactly one of `covered` / `lawfully out of scope` / `Unknown, unresolved`,
summing to the population; bounded to declared scope (no proof over an
unknowable universe); confirmed by a non-author; applied by a fresh
engineer from the scope statement alone. Distinct from CC-SPEC-8's
contract-clause coverage by construction.

**Warrant:** the owner's convergence direction §9.2 supplies the charter
authority whose absence the 2026-08-13 session recorded as its reason for
leaving f14 open.

### D2-4 — Editorial carriers of the above

- Banner: identifier range `CC-SPEC-1…10` → `CC-SPEC-1…11`; a 2026-08-17
  amendment paragraph added; the "**Not frozen** (conditional on P-40)"
  paragraph removed as discharged by D2-1.
- "Known open findings" table: f14 and f15 rows now read **repaired
  2026-08-17, unconfirmed**; f1 (sibling, P-44) stays open.

## Changes to `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`

### D2-5 — Banner only; no clause changed

A 2026-08-17 banner paragraph records that no CC-IMPACT clause moved in
this amendment (the six-class identity CC-IMPACT-1/2 consume is
unchanged), and that the CC-IMPACT-7 blind exercise has been **run and
passed** (RD-59, graded in
`../round-2026-08g/reviews/DISPOSITION-REGISTER.md`, bound to the fixture
sha256 CC-IMPACT-7 quotes in full
(`685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0`),
which still matches — verified this session).

## What this amendment deliberately does not do

- It does **not** touch CC-IMPACT-6 or create any lagging-spec exception —
  CC-REV-2 stands unmodified; the exception remains P-44's separate offer,
  and Capability 1 requires no lag.
- It does **not** define CC-IMPACT's "consumes its vocabulary"
  (`[Unknown]`, RD-51 G) — that finding stays open and disclosed in the
  impact file's own limits section.
- It does **not** edit the blind fixture or its answer key — RD-59's run
  stays bound to its digest.
- It mints no new authority: CC-SPEC-11's confirmer and the N/A record
  fields reuse the CC-TEST-4 pattern already approved in craft.

## Review posture

The repaired pair (plus the P-44 offer, per the P-41 packet's
three-subject direction) goes to **one combined fresh-context adversarial
review** under the five-part launch-blocker test, then at most one
blocker-only repair and one confirming review. Raw reviewer bytes will
land in `reviews/` beside this file, verbatim, with dispositions in a
register — never edited.
