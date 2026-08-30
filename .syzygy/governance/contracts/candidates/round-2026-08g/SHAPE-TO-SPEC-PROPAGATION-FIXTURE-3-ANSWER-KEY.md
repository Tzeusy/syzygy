# Shape-to-spec propagation fixture 3 — answer key

> **Do not open this file when administering the fixture.** It is separate
> from `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-3.md` so that a blind run is
> structurally blind. An administrator who has read this file has not run
> the fixture, and the record must say so.

## Golden result

**Population: 16 requirements across 5 specifications.**

### Affected — 8

| Requirement | Tied by | Changed identity |
|---|---|---|
| DIS-1 | declaration | `RFC6-19` |
| DIS-2 | declaration | `RFC6-19` |
| DIS-3 | consumption — `RFC6-20`'s own text composes its membership from `RFC6-19`'s folding rules | `RFC6-19`, via `RFC6-20` |
| STA-1 | declaration | `OD-11` |
| CAP-3 | declaration | `TOPO-1` |
| CAP-4 | declaration | `CC-PROV-6` |
| BUD-1 | declaration | `CC-PROV-6` |
| BUD-2 | declaration | `CC-PROV-6` |

**The several-requirements property:** one change — `CC-PROV-6` — affects
three requirements across **two** specifications (SPEC-CAPTURE and
SPEC-BUDGET). `RFC6-19` affects three requirements, all in SPEC-DISCLOSE,
one of them (`DIS-3`) only through `RFC6-20`'s consumption of it.

**The topology property:** `TOPO-1` affects exactly one requirement,
`CAP-3`, which declares no other warrant. A sweep whose trigger set omits
topology entirely misses `CAP-3` with no other route to catching it —
unlike the CC-PROV-6 case, there is no second declaration to fall back on.

### Undecidable — 1

| Requirement | Why the sweep cannot settle it | What would settle it |
|---|---|---|
| BUD-3 | It declares `CC-TEST-6`, a coverage obligation over "the absence branch." `CC-PROV-6`'s new aggregate-disclosure duty may be a new branch the absence-coverage obligation must now also cover, or it may be a refinement of the branch already covered — the fixture states neither, because "the absence branch"'s granularity is not defined anywhere the corpus gives the sweep | a ruling, or a corpus artifact, stating whether `CC-PROV-6`'s disclosure duty is a distinct branch from the one `CC-TEST-6` already requires coverage of. Until then, CC-IMPACT-4: `Unknown`, never `unaffected` |

### Explicitly unaffected — 7

| Requirement | Reason | Method |
|---|---|---|
| CAP-1 | declares `VIS-2`, `RFC5-6`; neither changed, and the requirement's content is the Unknown-rendering rule, which no trigger touches | declaration match **and** statement read |
| CAP-2 | declares `RFC5-11`; observer-identity recording is untouched by all four triggers | declaration match **and** statement read |
| DIS-4 | declares `RFC6-13`; its obligation is **parity between two consumers**, which is invariant under any change to what is computed. Changing the folding rules changes both outputs identically and cannot break equality | statement read — declaration match alone would not settle it |
| STA-2 | declares `OD-12`, `VIS-2`; `OD-12` (as-of instant timing) is a different decision from the amended `OD-11` | declaration match **and** statement read |
| STA-3 | declares `parent_requirements: SPEC-STATE/STA-2`; its parent is itself unaffected, so no inheritance arises | parent traversal — **one level**, and it terminates because the parent is unaffected |
| SUR-1 | declares `RFC7-39` | declaration match **and** statement read |
| SUR-2 | declares `VIS-5` | declaration match **and** statement read |

**Wholly unaffected specification: SPEC-SURFACE** (both requirements).

8 + 1 + 7 = 16. ✓

## Pass criterion

A run **passes** when all four hold:

1. the derived `affected` set **contains all eight** golden affected
   requirements — including `CAP-3` (the topology-triggered requirement)
   and `DIS-3` (the consumption-only requirement);
2. `DIS-3` is filed in `affected` — **and only there.** Unlike fixture 2's
   FAC-3, no hedge applies: `RFC6-20`'s authority-table text settles the
   tie in one hop, so `undecidable` or `explicitly unaffected` are both
   fails here, not defensible divergences;
3. `CAP-3` is filed in `affected` — a miss here means the sweep's trigger
   set silently excludes topology, the exact defect fixture 2 could not
   detect;
4. the population (16) is stated, all sixteen requirements are placed, and
   the sets sum to the population.

A run **fails** on any of: a missing golden affected requirement; `DIS-3`
filed anywhere but `affected`; `CAP-3` filed anywhere but `affected`; a
missing denominator; a requirement placed in no set or two sets.

Divergences that are **not** failures, but must be dispositioned in the
record:

- **`DIS-4` placed in `affected` or `undecidable`.** Over-inclusion here is
  a defensible reading (a sweeper may decline to reason about invariance
  under change). The golden is `explicitly unaffected`; a divergence costs
  nothing but must be recorded.
- **`STA-3` placed in `undecidable`.** A sweeper who declines to traverse
  `parent_requirements` at all is being conservative, which CC-IMPACT-4
  prefers to a wrong `unaffected`.
- **`BUD-3` placed in `affected`.** A sweeper who reasons that any new
  disclosure duty necessarily creates a new branch is over-inclusive but
  not unreasonable; the golden is `undecidable` because the fixture states
  no branch-granularity fact either way, and a defensible `affected`
  reading costs nothing but must be recorded.

## Divergences the fixture exists to catch

| Divergence | What it proves about the sweep |
|---|---|
| `CAP-3` missed while `CC-PROV-6`-triggered requirements are found | the sweep's trigger set omits `topology[]` — CC-SPEC-2's sixth warrant class was never exercisable against fixture 2, and this is the miss fixture 2 could not produce. There is no second declaration on `CAP-3` to catch this by accident |
| Only `DIS-1` and `DIS-2` are found affected in SPEC-DISCLOSE | the sweep matched **declared clause IDs only** and did not read `RFC6-20`'s authority text, missing `DIS-3`. Because `RFC6-20`'s tie to `RFC6-19` is stated in one hop with no hedge, this is now a plain miss, not a defensible reading |
| `DIS-3` filed `explicitly unaffected`, reason "does not declare `RFC6-19`" | the RD-51 f20 / fixture-2-answer-key failure mode exactly: a **true reason** producing a **wrong answer**, carrying a denominator and full compliance. `RFC6-20`'s text removes the excuse fixture 2's answer key itself relied on |
| `STA-1` missed | owner decisions are not sweep triggers in the sweeper's model |
| `CAP-4` missed while `BUD-1`/`BUD-2` are found (or the reverse) | the sweep ran per-specification against a topic guess rather than over the declaration population — `CAP-4` is a budget-shaped requirement living in the capture spec precisely to catch this, mirroring fixture 2's REG-4 |
| Affected set reported without the population | a numerator with no denominator (VIS-2; CC-KNOW-16) |

## Provenance

Built 2026-08-30, superseding
`SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md`. Fixture 2's own run
(RD-59, `reviews/DISPOSITION-REGISTER.md`) found the three defects this
fixture and this key repair: no `topology[]` warrant exercised, the task
block stating the four-set schema without quoting CC-IMPACT-2/CC-IMPACT-3,
and a FAC-3-equivalent authority-table entry that left a genuine
undecidable/affected split rather than settling in one hop. `DIS-3`
replaces the FAC-3 role with a deterministic tie; `BUD-3` supplies this
fixture's own genuinely undecidable case, built the same way RD-59's
COST-3 divergence was — a real gap in what the corpus states, not an
authoring accident. A fresh, independent blind run against this fixture,
graded by an administrator who has not read this file, is required before
CC-IMPACT-7 may name it in place of fixture 2; that run is separate
follow-on work.
