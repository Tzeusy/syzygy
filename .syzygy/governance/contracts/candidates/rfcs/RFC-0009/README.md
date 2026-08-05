---
id: RFC-0009
title: Orrery (Map Surface) — contract package index
status_source: owner-act-record
package: RFC-0009
modules: [semantic-geography, visual-grammar-and-lenses, interaction-parity-and-release]
clauses: RFC9-1..RFC9-52 (sub-clauses RFC9-8(a), RFC9-9(a), RFC9-9(b), RFC9-13(a), RFC9-14(a), RFC9-15(b), RFC9-16(d), RFC9-47(a); no gaps, no retired numbers, no merges)
governs: [map-surface, home-geography, analytical-planes, layout-determinism, placement, identity-counting, reserved-palette, channel-registry, lenses, scene-profiles, scenarios, aggregation, unmapped-code, non-3d-equivalence, release-gates, motion]
applies_to: [orrery, machine-clients]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008]
provides_to: [RFC-0007, RFC-0008, RFC-0010, RFC-0011]
tags: [surface, spatial, legend-fidelity, unknown, determinism, sdr-19, sdr-20, sdr-21, sdr-22, sdr-23, sdr-24, sdr-25, sdr-26, sdr-27, vis-1, vis-7, sec-2, sec-3, sec-5]
---

# RFC 0009 — Orrery (Map Surface)

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — as an owner-adopted bootstrap act
until the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Date:** 2026-07-30 (amended through 2026-08-02; compacted and split into a
package at rev10 under **owner direction OD-R10-6**, which reversed the rev9
"do not split" recommendation). **Rationale, amendment history, alternatives,
the foundation-defect trail, and answered §8 questions:**
`../../history/RFC-0009-history.md` (non-normative).

**Serves:** VIS-1, VIS-2, VIS-3, VIS-7 (trust floor: legend fidelity, link
rule); SEC-2, SEC-3, SEC-5; architecture.md (constitutional spatial requirement;
exact 2D/tabular equivalents); v1.md (3D V0 mandate, coarse granularity,
predominantly-Unknown maps); SDR §2 (Orrery charter and anti-thesis); SDR-3,
SDR-19, SDR-20, SDR-21, SDR-22, SDR-23, SDR-24, SDR-25, SDR-26, SDR-27; resolves
the map-surface portion of SDR §5 question 10. Historical state is in `map/`'s
constitutional scope by **adopted** doctrine amendment D1 (owner-ratified
2026-08-01); the concrete historical *interaction design* remains a non-binding
candidate bundle behind its own owner approval (RFC9-41).

---

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One authoritative
`RFC9-n` namespace, no duplicated normative clauses, no renumbering. Shared
concepts live in exactly one module and are cited from the others by clause ID.

| Module | File | Clauses | Words |
|---|---|---|---|
| 1 — semantic geography | `semantic-geography.md` | RFC9-1..RFC9-23, incl. RFC9-8(a), RFC9-9(a), RFC9-9(b), RFC9-13(a), RFC9-14(a), RFC9-15(b), RFC9-16(d) | 6,999 |
| 2 — visual grammar and lenses | `visual-grammar-and-lenses.md` | RFC9-24..RFC9-45 | 5,540 |
| 3 — interaction parity and release | `interaction-parity-and-release.md` | RFC9-46..RFC9-52, incl. RFC9-47(a) | 3,027 |

Counts are whole-file `wc -w` at the rev10 compaction. See **Word accounting**.

**Lookup rule (deterministic).** For any citation `RFC9-n`, read `n` as an
integer and take the row whose stated range contains it. The three ranges are
**contiguous and disjoint** and exhaustive over RFC9-1…RFC9-52, so the rule never
needs a search. A lettered sub-clause lives with its parent integer —
`RFC9-9(a)`/`RFC9-9(b)` with RFC9-9 in module 1, `RFC9-47(a)` with RFC9-47 in
module 3. Lettered *limbs* cited inside a parent clause (RFC9-10(c), RFC9-19(b))
are parts of that clause, not separate sub-clauses, and resolve the same way.
Modules are numbered for reading order only — citations name clauses, never
modules.

**Reading order for a cold reader:** module 1 → 2 → 3. Module 1 fixes the address
space every other clause encodes onto; modules 2 and 3 are independently readable
given it.

**The range is closed at RFC9-52.** A new clause anywhere in the package takes
the next free integer after 52. Amend in place, add lettered sub-clauses, never
renumber; retired numbers are never reused.

## Package reader map (non-normative)

*If this map and a clause disagree, the clause wins.*

Orrery is the **map surface**: a 3D/2D spatial rendering of the project as a
city, built for spatial memory. Its named enemy is **spectacle displacing
truth** — a green district with no evidence, a layout that quietly reshuffles,
proposed structure rendered solid. Every clause makes one of those lies a
recognizable violation rather than an aesthetic choice. The contract is
**semantics only**: no rendering engine, graphics API, layout algorithm, or stack
choice appears in it — determinism *obligations* are bound, algorithms are not.

- **Home geography is anchored to capability identity, not file paths** —
  refactoring never moves the map; projections where position encodes a metric
  are explicitly selected, legended **analytical planes** (module 1,
  RFC9-4/10/11).
- **Layout is a pure function of three inputs** — declaration set, layout
  baseline, layout version — insertion order never among them; within a version
  positions are fixed, and regeneration is full, manual, and owner-gated with
  recorded rationale (module 1, RFC9-14/15(b)/16(d)).
- **Nearness carries exactly three legend meanings** — declared containment,
  declared relatedness (best-effort, shortfall rendered *not-honored*), and
  **residual adjacency, which carries no meaning** — and a reader can tell which
  is which from what is on the screen (module 1, RFC9-9/9(a)/9(b)).
- **Unknown is a first-class colour.** A predominantly-grey map on an undeclared
  project is correct output; the unmapped district never disappears; absent a
  coverage record, "no code implements this" is Unknown, not an empty lot
  (module 2, RFC9-27/43/44).
- **Every visual channel is registered and legended** — one meaning per channel
  per lens, all legend text generated from the registry, unregistered encodings
  failing closed (module 2, RFC9-26).
- **Non-3D views are co-equal** — a table and the scene disagreeing over one
  scope is release-blocking, and truth is never purchased with frame rate
  (module 3, RFC9-46/47/49).

## Package-level integration

*Module-scoped dependency lists live in each module's own §Integration; only
genuinely package-spanning items are held here.*

**Two registries are cited by RFC3-16(a) as encoding-meaning-fixing artifacts**,
and they sit in different modules: **RFC9-18** (layout version registry, module
1) fixes which layout version a scene's positions *mean*; **RFC9-26** (channel
registry, module 2) fixes what every rendered channel *means*. For both, an entry
whose owner-act provenance does not verify is treated exactly as an absent one —
the version is not established, the channel does not render. Each module states
the rule for its own registry and names the other.

**RFC3-16(a) gates four artifacts across two modules:** those two registries, the
promotion of lenses/analytical planes/profile relations (RFC9-35), and the
walkthrough judgment and release policy (RFC9-45).

**One package-spanning maintenance obligation.** **RFC9-47(a)** (module 3)
requires that any amendment creating, removing, or changing a release-blocking
obligation on this surface update RFC9-47's gate list **in the same logical
change**. That invariant binds across module boundaries exactly as it did across
sections of the monolith: an obligation minted in module 1 or 2 is routed to
module 3's list, and the same rule binds the craft-and-care release checklist
that consumes it.

**RFC9-52 binds the package, not one module.** The phase rule names
"RFC9-1…RFC9-51", spanning all three modules, and the clause-to-requirement
coverage matrix it mandates is produced for RFC 0009 **entire**. It is
shape-parallel with RFC6-28, RFC7-38 and RFC8-32; both RFC 0010 and RFC 0011
cite it.

**Provides to:** **RFC 0007 / RFC 0008** — map-side rendering obligations behind
cross-surface highlights (same reserved palette semantics for shared states);
**RFC 0010 / RFC 0011** — RFC9-52's phase boundary; **craft-and-care** — the
release-gate list (RFC9-47) and its self-maintenance contract (RFC9-47(a)),
legend/palette registry discipline, and the interaction-cost material this
contract declines to bind (the return-to-home affordance's *form and cost*,
RFC9-10(c) binding only that return is always available and discoverable, per
**B21**); **the first map-surface spec** — every declared-value slot left open
(budget values, treatment values, band counts, analytical-plane catalog).

**Not this RFC's:** rendering engine, layout algorithms and tuning, concrete
visual treatment values, legend layout, lens metric formulas, V1 gap-object
rendering (V0 renders absence), certificate rendering (post-V1), live fleet
streaming (deferred mandate).

## Violation cases — distribution

The eleven cases keep their stable package numbering and go to the module owning
the violated clause. **No case spans modules.** Cases 1, 2, 3, 3a, 4, 5 →
module 1 §7; cases 6–10 → module 2 §5; case 11 → module 3 §5.

## Foundation defects (§5) — all discharged or resolved

Five were reported; **none is outstanding and none blocks acceptance.** Defect 1
(RFC1-25 carrying neither a declared placement relation nor a declared dependency
relation) was **discharged at acceptance by owner decisions A7 and A6**; the
drafting restraint that produced them still binds and is carried in module 1's
§Integration. Defects 2 (RFC6-22's equivalence enumeration), 3 (RFC6-24's context
taxonomy), 4 (RFC6-17's aggregation disclosure) and 5 (RFC2-6's omission of the
base layout) were all **resolved upstream on 2026-08-01**. Full trail: history §5.

## Owner questions — package index

Stable numbering; each question keeps a stub in the module owning its subject,
with full text, answers and decision cites in history §8.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | The placement relation (§5 defect 1) | **answered — A7** | module 1 §10 |
| q2 | Undeclared shared-component placement (RFC9-20) | **OPEN** | module 1 §10 |
| q3 | Historical conditionality (RFC9-41) | **answered — D1, in part** | module 2 §8 |
| q4 | Analytical-plane governance (RFC9-10, RFC9-18) | **answered — B12(c)/B17** | module 2 §8 |
| q5 | The declared dependency relation (§5 defect 1) | **answered — A6** | module 1 §10 |
| q6 | Layout-version change as owner-gated act (RFC9-16(d)) | **answered — A3**, narrowed | module 1 §10 |
| q7 | Proximity's declared meaning (RFC9-9, RFC9-4) | **answered — B12(a)** | module 1 §10 |
| q8 | Comprehension test as release gate (RFC9-45) | **answered — B12(b)** | module 2 §8 |
| q9 | Who may adopt a lens (RFC9-32, RFC9-35) | **answered — B12(c)/B17** | module 2 §8 |
| q10 | Return-to-home bound (RFC9-10(c); SDR-21) | **answered — B21** | module 3 §8 |

**One open item beyond the numbered set.** The rev10 RFC-0001 pass flagged that
**owner decision A6** closed the kernel-minting question but did **not** address
the adjacent part RFC-0001 §8 q6 also raised: whether **RFC9-9's legend and
edge-channel rules need a pass now that a kernel-level declared dependency
relation exists**, and beneath it *who may add a profile relation and under what
gate*. No normative change was made on this pass — the question is owner-scoped
and its home is RFC1-7/RFC1-26, not this surface. Carried as a visible open item
in **module 1 §10**; recorded in history §8. The surface is safe under either
answer meanwhile: an unregistered profile relation fails closed under RFC9-26 and
never reaches a reader as an unlegended edge.

## Word accounting (rev10 compaction)

| | Words |
|---|---|
| rev9 monolith (frozen source) | 19,269 |
| module 1 | 6,999 |
| module 2 | 5,540 |
| module 3 | 3,027 |
| **modules total (active contract)** | **15,566** |
| package index (this file, navigational) | 2,029 |

The package is **above the ~9,500 target**. Per the charter's word-target rule
and lead ruling 5, this pass stopped at the smallest faithful size rather than
reaching the number by deleting constraints.

Where the −3,703 words went: roughly **4,500 words of rev9 material moved to
Tier 2** (all 20 `*(History: …)*` parentheticals, §6 alternatives, §7's full
text, §0/§1/§2, and the answered §8 question text), offset by roughly **+1,580
words of new per-module scaffolding** the monolith never carried (three sets of
front matter, status blocks, package pointers, reader maps and end markers).
Net **−19.2%** against the monolith. Prose compression *within* retained clause
text is deliberately small — the clause bodies are 14,305 of the source's 19,269
words and are near-continuous obligation: closed vocabularies copied not
paraphrased, multi-part binding rules, and nine owner decisions.

**Module 1 sits at 6,999 against the ~7,000 ceiling — that is its floor, not a
coincidence.** Its range is 7,184 source words; everything remaining is a rule, a
closed vocabulary, an owner decision, or a load-bearing distinction. Further
headroom requires splitting the range (a natural seam exists at RFC9-1..13 /
RFC9-14..23), not deleting rules — an owner/lead call, not this pass's.

**Selective loading is the point of the split.** "May this move?" loads module 1
alone (6,999); "what does this colour mean?" module 2 alone (5,540); "what does
release check?" module 3 alone (3,027) — against 19,269 for any question before
the split.

---

*End of RFC 0009 package index. Clauses RFC9-1 … RFC9-52, with sub-clauses
RFC9-8(a), RFC9-9(a), RFC9-9(b), RFC9-13(a), RFC9-14(a), RFC9-15(b), RFC9-16(d)
and RFC9-47(a), distributed across three modules. The three ranges are contiguous
and disjoint; no retired numbers, no merged numbers, no gaps, and no clause
identity in more than one module.*
