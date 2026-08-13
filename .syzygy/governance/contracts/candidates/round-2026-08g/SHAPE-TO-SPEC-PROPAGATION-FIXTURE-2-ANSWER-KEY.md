# Shape-to-spec propagation fixture 2 — answer key

> **Do not open this file when administering the fixture.** It is separate
> from `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` so that a blind run is
> structurally blind. An administrator who has read this file has not run
> the fixture, and the record must say so.

## Golden result

**Population: 16 requirements across 5 specifications.**

### Affected — 6

| Requirement | Tied by | Changed identity |
|---|---|---|
| FAC-1 | declaration | `RFC6-19` |
| FAC-2 | declaration | `RFC6-19` |
| STA-1 | declaration | `OD-2` |
| REG-4 | declaration | `CC-PROV-5` |
| COST-1 | declaration | `CC-PROV-5` |
| COST-2 | declaration | `CC-PROV-5` |

**The several-requirements property:** one change — `CC-PROV-5` — affects
three requirements across **two** specifications (SPEC-REG and SPEC-COST).
`RFC6-19` affects two, both in SPEC-FACETS.

### Undecidable — 1

| Requirement | Why the sweep cannot settle it | What would settle it |
|---|---|---|
| FAC-3 | It declares `RFC6-18`, not the amended `RFC6-19`. But `RFC6-18`'s own text composes a fact set's facets from *"those the folding rules produce"*, so the new provenance prohibition may change what FAC-3 renders while leaving FAC-3's obligation ("render without re-deriving") verbally intact. Deciding this requires reading whether `RFC6-18`'s fact-set composition **inherits** `RFC6-19`'s constraints — a contract-reading question the sweep does not own | a ruling from the contract's owning authority on whether `RFC6-18` inherits `RFC6-19`'s folding constraints. Until then, CC-IMPACT-4: `Unknown`, never `unaffected` |

### Explicitly unaffected — 9

| Requirement | Reason | Method |
|---|---|---|
| REG-1 | declares `VIS-2`, `RFC3-5`; neither changed, and the requirement's content is the Unknown-rendering rule, which no trigger touches | declaration match **and** statement read |
| REG-2 | declares `RFC3-9`; adapter declaration is untouched by all three triggers | declaration match **and** statement read |
| REG-3 | declares `RFC1-3`, `OD-1`; `OD-1` (consent timing) is a different decision from the amended `OD-2` | declaration match **and** statement read |
| FAC-4 | declares `RFC6-13`; its obligation is **parity between two consumers**, which is invariant under any change to what is computed. Changing the folding rules changes both outputs identically and cannot break equality | statement read — declaration match alone would not settle it |
| COST-3 | declares `CC-TEST-6`; a coverage obligation over the absence branch, unchanged by `CC-PROV-5`'s new disclosure duty | declaration match **and** statement read |
| STA-2 | declares `OD-1`, `VIS-2`; the as-of instant is untouched by the reason-vocabulary rename | declaration match **and** statement read |
| STA-3 | declares `parent_requirements: SPEC-STATUS/STA-2`; its parent is itself unaffected, so no inheritance arises | parent traversal — **one level**, and it terminates because the parent is unaffected |
| ENT-1 | declares `RFC7-39` | declaration match **and** statement read |
| ENT-2 | declares `VIS-5` | declaration match **and** statement read |

**Wholly unaffected specification: SPEC-ENTRY** (both requirements).

6 + 1 + 9 = 16. ✓

## Pass criterion

A run **passes** when all three hold:

1. the derived `affected` set **contains all six** golden affected
   requirements;
2. FAC-3 is placed in `undecidable` **or** in `affected` — never in
   `explicitly unaffected`;
3. the population (16) is stated, all sixteen requirements are placed, and
   the sets sum to the population.

A run **fails** on any of: a missing golden affected requirement; FAC-3
filed as `explicitly unaffected`; a missing denominator; a requirement
placed in no set or two sets.

Divergences that are **not** failures, but must be dispositioned in the
record:

- **FAC-4 placed in `affected` or `undecidable`.** Over-inclusion here is a
  defensible reading (a sweeper may decline to reason about invariance under
  change). The golden is `explicitly unaffected`; a divergence costs nothing
  but must be recorded.
- **STA-3 placed in `undecidable`.** A sweeper who declines to traverse
  `parent_requirements` at all is being conservative, which CC-IMPACT-4
  prefers to a wrong `unaffected`.

## Divergences the fixture exists to catch

| Divergence | What it proves about the sweep |
|---|---|
| Only FAC-1 and FAC-2 are found affected | the sweep matched **contract clause IDs only**. This is RD-51 f9's warranted-but-unsweepable class made visible: `policies[]` and `decisions[]` are lawful warrants, and a sweep blind to them misses 4 of 6 affected requirements — a **67 % miss rate on this fixture** |
| STA-1 missed | owner decisions are not sweep triggers in the sweeper's model. This is the single class the pre-2026-08-13 CC-IMPACT-2 did not trigger on |
| REG-4 missed while COST-1 and COST-2 are found | the sweep ran per-specification against a topic guess ("the cost spec") rather than over the declaration population. REG-4 is a cost requirement living in the registration spec precisely to catch this |
| FAC-3 filed `explicitly unaffected`, reason "does not declare `RFC6-19`" | RD-51 f20's failure mode exactly: a **true reason** producing a **wrong answer**, carrying a denominator and full compliance. This is why CC-IMPACT-3 requires the *method*, and why CC-IMPACT-4 routes what a method cannot decide to `undecidable` |
| Affected set reported without the population | a numerator with no denominator (VIS-2; CC-KNOW-16) |

## Provenance

Built 2026-08-13 for CC-IMPACT-7, under owner charter §9.7's five required
properties. Supersedes
`../round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`, whose golden
ANSWER contradicted its own governing description (RD-51 f8) and whose
scenario exercised only contract-clause triggers.
