# Launch-gate v1.4 → v1.5 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.5 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34).

Baseline: v1.4 as reviewed by RD-24 (subject sha256
`1e28271ddde68729aa63e59d65dedf2f288899aa4ebcf5e44bd0353a545dd899` at
commit `e8a4f36`; raw review
`reviews/RD-24-launch-gate-RAW.md`, `VERDICT: REVISE`, 3 BLOCKING /
11 MAJOR / 7 MINOR). Every delta below closes an RD-24 finding; the
dispositions are in `reviews/DISPOSITION-REGISTER.md`. **No question's
fail condition was narrowed, no verdict word was removed, no ID
renumbered.** Validator changes each carry a mutation fixture
(`scripts/launch_gate_results.py --selftest`, 22 fixtures).

## D-1 — Verdict formula restated as predicates (RD24-09, BLOCKING)

The §4 conjunct "F1 is not diverging" — a word outside the closed
vocabulary, which RD-24 proved unenforceable (its T3/T4 records passed
READY over a self-declared diverging F1) — is now "F1 is `Met` or
`Unknown` — a `Not met` F1 blocks, whichever of its two limbs failed."
The validator enforces it (`F1 is Not met` refusal; fixture). A closing
sentence states that every formula term is a predicate over the closed
vocabulary. *Semantic change:* the conjunct becomes enforceable; a
`Not met` F1 that previously slipped through now blocks — a
strengthening. The stop-condition limb of F1 now also blocks (previously
ambiguous), deliberately.

## D-2 — The scoped row form (RD24-05, BLOCKING)

`Not met (out of launch scope)` joins the closed vocabulary, lawful only
in A–D for a defect confined to a deferred wave that meets none of §4's
five blocking conditions. §4 now states that the scoped form is the
*only* honest rendering of such a defect (a bare `Met` is a false row; a
bare `Not met` blocks what §4 says must not block). The validator accepts
it in A–D, rejects it elsewhere, counts it separately, and READY is
consistent with it (fixtures for RD-24's T1/T2 pair). *Semantic change:*
the rendering choice RD-24 showed could flip the gate outcome is closed;
neither prior rendering was lawful for this case, so no question weakened.

## D-3 — Owner-act mechanism reordered (RD24-01, BLOCKING; RD24-04)

P-34's mechanism now edits the `status:` header — a governance-lifecycle
state — **first** and binds the approval to the digest of the resulting
bytes, in one commit — the
approval and the in-force instrument can never disagree, and every later
administration verifies that same digest (LG-2). The garbled step-3
sentence is repaired. *Semantic change:* to the decision packet only; the
instrument's text is unchanged by this delta item.

## D-4 — §5 record template hardened (RD24-02, RD24-10, RD24-19, RD24-21)

The template gains: a required non-authority banner as its first body
line; the literal `GATE VERDICT:` token (the previous
"Gate verdict per §4:" phrasing did not match the validator's parser —
RD-24 showed a template-verbatim record being rejected); a `## G1` section
slot with the rule that G1 is never a verdict row (row form now errors);
required `Deferred count:` / `Reopened count:` fields whose **absence is a
validation error, never an implicit zero** (RD-24 showed the trend row
printing `0 | 0` from missing fields — VIS-2 applied to the gate's own
record); and the five E1 sub-verdict rows (`E1-form`, `E1-home`,
`E1-granularity`, `E1-acceptance-authority`, `E1-change-process`), which
the parser now accepts and LG-8 cross-checks against the E1 rollup.
*Semantic change:* records become mechanically checkable in exactly the
places RD-24 proved they silently were not; requirements added, none
removed.

## D-5 — §2 withhold/read-access reconciliation (RD24-15)

Prior-review and administration trees are in scope as **objects** of the
F2/F4/C3 sweeps but never **read for content**; a reviewer who has read
them for content records a materials deviation. *Semantic change:* the
collision RD-24 identified (under-counting sweeps vs. contamination) now
has one stated resolution.

## D-6 — Populations closed (RD24-18, RD24-20, RD24-07, RD24-13, RD24-16, RD24-06)

New parameter-block bindings, each referenced from the question that
quantifies over it: `CHUNK_UNIT` (B-section "chunk" = the six wave acts);
`C2_POPULATION`, `C5_POPULATION`, `C7_POPULATION`, `D3_POPULATION`,
`D4_POPULATION` (denominator rules for the five open universals);
`DEFAULT_ROUTE_SET` (the enumerated default reading/task routes — §4's
blocking condition 1, D2's "front door", and D3/F4's "default reading
path" all now name it); `FIRST_SPEC_CANDIDATE` fixed to
`contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md` (revision 3, the
self-declared single current document) with the absent-case rule (E2
`Not met`, never `Unknown`); `E4_ROUTING_AUTHORITY` (the routing matrix,
with the two-valued classification stated); `LAUNCH_TARGET` now cites
Capability 1's defining artifact (`DEFERRED-WAVE-POSTURE.md`) with its
owner-directed sentence quoted. *Semantic change:* questions become
administrable identically by two administrators; no fail condition moved.

## D-7 — Pilot recurrence check relocated and made executable (RD24-14)

§6's instruction to the next administrator — which referenced a pilot
finding §2 withholds — moves to §8 as `PILOT_RECURRENCE_CHECK`, with the
defect described in place (a retired ceremony phrase standing as the live
acceptance gate in two digest-carrying owner documents) and the sweep
named. *Semantic change:* §6 returns to being project-invariant (§7's own
rule); the instruction becomes executable from the instrument alone.

## D-8 — Small statements (RD24-03, RD24-08, RD24-11, RD24-12, RD24-17)

`governs:` gains "the launch-scope parameters (§8)", matching P-34's list
(the conservative direction — §8 re-parameterization is owner-gated once
in force; flagged in P-34). A5 is declared answered repository-wide,
wave-blind. An `Unknown` F2 is deferrable on the same owner-deferral terms
as a `Not met` F2. F5/F6's non-conjunct status at Administration 1 is
stated as deliberate, with promotion of F5 flagged as a prepared owner
option in P-34. §6 names the trend-log path, and the canonical result home
now exists with a README stating what may live there (a home, not a
decision).

## What did not change

Question IDs and texts A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1 —
unchanged except the population/route pointers recorded above (C2, C5, C7,
D3, D4, D2, E4 gained *Population:*/routing pointers; no stem or fails-when
narrowed). §1 derivation tiers, §3 order, §6 trend-log columns, §7
generalization path unchanged. The verdict vocabulary gained the scoped
form and lost nothing.
