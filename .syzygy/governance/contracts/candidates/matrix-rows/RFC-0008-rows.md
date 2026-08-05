# RFC-0008 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0008-trajectory-work-surface.md` (frozen,
9,791 words, RFC8-1…RFC8-32).
Active: `../rfcs/RFC-0008/` — a three-module contract package (11,169 words
including the index). History: `../history/RFC-0008-history.md`.

**Clause range after compaction:** RFC8-1..RFC8-32, contiguous. **No merges, no
retirements, no renumbering, no new clauses.** All 32 rev9 clause identifiers
survive, each in **exactly one module** (verified programmatically: 32 clause
headers, none missing, none duplicated).

| Module | File | Clauses | Words |
|---|---|---|---|
| index | `README.md` | — | 1,921 |
| 1 | `identity-authority-materialization.md` | RFC8-1..RFC8-11 | 2,686 |
| 2 | `state-vocabulary-and-cost.md` | RFC8-12..RFC8-20 | 3,507 |
| 3 | `accounting-reconciliation-and-release.md` | RFC8-21..RFC8-32 | 3,055 |

**Verified [Observed]:** 17 clauses are byte-identical to rev9 after whitespace
normalization (RFC8-1…6, 8-9, 8-11, 8-13, 8-15, 8-17, 8-20, 8-22, 8-26, 8-29,
8-30, 8-31); 15 are sharpened. RFC8-13's three derivation tables and RFC8-4's
ontology table are copied verbatim, not paraphrased. The split moved clause
text unchanged: after splitting, exactly one clause differs from the pre-split
single file — **RFC8-27**, whose stale "RFC 0004 §6" cross-reference was
repointed to `../history/RFC-0004-history.md` §6 now that RFC-0004 is itself a
package.

**Note on lettered limbs.** RFC-0008's own end-of-contract marker declares that
lettered limbs cited inside a clause (e.g. RFC8-2(a)–(c)) are *parts of that
clause — list items within one clause body — not separate sub-clauses with
their own headings*. Rows are supplied for the six that carry independently
citable content (RFC8-2(a)–(c), RFC8-8(a)–(c)) so the matrix is complete
against the charter's format; they are not separate clause identifiers, and
they resolve to their parent clause's module.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC8-1 | retained unchanged | module 1 `identity-authority-materialization.md` | Plane discipline; byte-identical. |
| RFC8-2 | retained unchanged | module 1 `identity-authority-materialization.md` | Binding anti-thesis; byte-identical. |
| RFC8-2(a) | retained unchanged | module 1 `identity-authority-materialization.md` | Second-editable-store limb; cited by RFC8-7 and violation case 2. |
| RFC8-2(b) | retained unchanged | module 1 `identity-authority-materialization.md` | Closure-renders-as-done limb; cited by RFC8-15/8-30. |
| RFC8-2(c) | retained unchanged | module 1 `identity-authority-materialization.md` | Amnesiac-board limb; past-window answerability. |
| RFC8-3 | retained unchanged | module 1 `identity-authority-materialization.md` | Rebuildable projection, synchronous-adapter mutation rule; byte-identical. |
| RFC8-4 | retained unchanged | module 1 `identity-authority-materialization.md` | Ontology binding table copied verbatim (table, not paraphrased). |
| RFC8-5 | retained unchanged | module 1 `identity-authority-materialization.md` | Deliberate non-reifications; byte-identical. |
| RFC8-6 | retained unchanged | module 1 `identity-authority-materialization.md` | Compaction record definition; byte-identical. |
| RFC8-7 | retained with wording sharpened | module 1 `identity-authority-materialization.md` | All three rules kept at strength; the three-reason justification for the annotation ban and the `[Inferred]` scoping rationale moved to history. |
| RFC8-8 | retained with wording sharpened | module 1 `identity-authority-materialization.md` | Three planes, orphaned-work Contradiction, and exclusivity rules all kept; two explanatory sentences moved to history. |
| RFC8-8(a) | retained unchanged | module 1 `identity-authority-materialization.md` | Uncovered approved normative claims; V0 absence-surfacing boundary. |
| RFC8-8(b) | retained unchanged | module 1 `identity-authority-materialization.md` | Approved-but-unmaterialized intent, queue order visible. |
| RFC8-8(c) | retained unchanged | module 1 `identity-authority-materialization.md` | Open materialized items, each checked against the materialization record. |
| RFC8-9 | retained unchanged | module 1 `identity-authority-materialization.md` | SDR-18 ownership boundary against Polaris; byte-identical. |
| RFC8-10 | retained with wording sharpened | module 1 `identity-authority-materialization.md` | Three required record components and the missing-record finding kept; one restatement of RFC8-8 compressed to a cross-reference. |
| RFC8-11 | retained unchanged | module 1 `identity-authority-materialization.md` | Divergence renders, never adjudicated; byte-identical. |
| RFC8-12 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Closed thirteen-value vocabulary, two-orthogonal-fields rule, non-Claim ruling, and the RFC3-16(a) authorization-bearing mapping with its full widening argument all kept; the genuineness essay and the spent §8 q5 routing note moved to history, replaced by an inline B14 cite. |
| RFC8-13 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | All three derivation tables (8 live + 1 terminal + 4 absence values) copied verbatim; byte-identical. |
| RFC8-14 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Rule unchanged; the spent §8 q7 routing note replaced by an inline A5/B15 cite, note moved to history. |
| RFC8-15 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | Closure is not a normalized "done"; byte-identical. |
| RFC8-16 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Obligation identical; the `_bootstrap/` audit path in the `[Observed]` citation replaced by "substrate audit" (charter bars `_bootstrap/` paths in active normative text), path preserved in history. |
| RFC8-17 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | Closed blocked-cause taxonomy; byte-identical. |
| RFC8-18 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Full measure list and the no-composite-score prohibition kept; the `declared-only`-not-`Inferred` argument condensed but its RFC2-7/SEC-2 consent premise and RFC2-8/RFC1-22 challenge-authority consequence retained (security premise may not thin). |
| RFC8-19 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Rule identical; `_bootstrap/` audit path in the `[Observed]` citation replaced by "substrate audit". |
| RFC8-20 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | Telemetry staging, V0/V1 split, deferral list; byte-identical. |
| RFC8-21 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Chain, join bases, and the thinness-must-render obligation kept; the enrichment enumeration and the `[Inferred]` derivation moved to history. |
| RFC8-22 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | Broken joins render, reconstruction forbidden; byte-identical. |
| RFC8-23 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Unknown-provenance state and its distinction from orphaned work kept; wording tightened only. |
| RFC8-24 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Full RFC2-24 reason list kept verbatim, including the maximum-inter-pass-interval obligation; the trailing "claim reasons only" paragraph folded into the clause body (same clause, no merge). |
| RFC8-25 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Sub-entry rule, B13 fail-closed threshold, warrant-coverage test, and fixed `asserted-by-worker` tier all kept; the `[Inferred]` fail-closed essay moved to history, and one rev9 paragraph ("Until the bound is declared, the coverage test above is the operative limit") dropped as superseded by B13 — see WORKER-REPORT-DIGEST.md §"Substantive rulings", ruling 3. |
| RFC8-26 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | Binding preservation set; byte-identical. |
| RFC8-27 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Every tier rule kept, including the no-upgrade rule and the `report-fact` cap; the rev7 blocker-A3 `*(History: …)*` parenthetical moved to history verbatim. |
| RFC8-28 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Four-way chain-state distinction, word reservation, and the carry-both-fields obligation kept; one restatement compressed. |
| RFC8-29 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | V0 honest-absence / V1 computation staging; byte-identical. |
| RFC8-30 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | Closure fallacy forbidden; aggregate composition disclosure; byte-identical. |
| RFC8-31 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | RFC 0006 conformance and no-surface-only-facts rule; byte-identical. |
| RFC8-32 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | **Binding phase rule.** Normative text verbatim at full strength (verified by diff); only the `*(History: added at the rev8 rework, directive item 7.)*` parenthetical moved to history. Shape-parallel with RFC6-28 / RFC7-38 / RFC9-52. |

## §8 questions

Question numbers are the stable package numbering and never shift. Per the
charter addendum, every answered question keeps a one-line stub in its owning
module's §8; full text and reasoning are in history.

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | answered — moved to history | history §8 q1; stub in module 2 §8 | Vocabulary closure; answered at acceptance by **A8** (thirteen values, three partitions). Ruling carried inline in RFC8-12 and by RFC8-13's derivation rows. |
| q2 | open — retained | module 1 §8 | Queue realization: work-plane fact on the approved Proposal vs a new RFC 0001 kernel lifecycle state. Paired with module 1 §5's one outstanding foundation defect. |
| q3 | open — retained | module 2 §8 | Blocked-time cause split: V1 capture obligation vs RFC4-29 enrichment-roadmap item. Blocked-time semantics remain an open default. |
| q4 | open — retained | module 3 §8 | Unknown-provenance visibility default, with its scope limit that the orphaned-work Contradiction is never filterable under any answer. |
| q5 | answered — moved to history | history §8 q5; stub in module 2 §8 | Epistemic class of the normalized state; answered by **B14** (derived rendering, not a Claim). Ruling carried inline in RFC8-12. |
| q6 | answered — moved to history | history §8 q6; stub in module 3 §8 | The "small" threshold on inherited mutations; answered by **B13** (declared per project, fails closed). Ruling carried inline in RFC8-25. |
| q7 | answered — moved to history | history §8 q7; stub in module 2 §8 | Unmapped-substrate-value rendering; answered by **A5 / B15** (no new RFC2-24 reason; `state-undetermined` stands). Ruling carried inline in RFC8-14. |

## Non-clause sections

Violation cases keep the stable package numbering and are distributed to the
module owning their clauses: 1–3 and 11 → module 1; 5–7 and 13 → module 2;
8–10 and 14 → module 3; **4 and 12 span modules and are held in the package
index** (`README.md` §4). All 14 appear exactly once across the package
(verified).

| Section | Outcome | Target | Reason |
|---|---|---|---|
| §0 Reader's summary | retained with wording sharpened | README package reader map; per-module §0 maps | Merged with §1 at compaction; no obligation lived in either. Dropped bullets recorded in history with their clause pointers. |
| §1 Summary | retained with wording sharpened | README package reader map + scope | Merged as above; the anti-thesis sentence and the semantic-contract-not-UI scope statement retained. |
| §2 Motivation | retained with wording sharpened | README §2 | Doctrine grounding, the three failure modes, and all SDR staging retained; the `_bootstrap/` audit citation path moved to history. |
| §4 Violation cases | retained unchanged | modules 1–3 §4; cases 4 and 12 in README §4 | All 14 cases retained and distributed by owning clause; four trimmed by a few words each without losing recognizability. |
| §5 Integration | retained with wording sharpened | per-module §5; package-level items in README §5 | Every relies-on citation retained and redistributed by owning clause. The **two-field RFC 0009 handoff** and its conformance rule are stated **once**, in README §5, because they cite clauses in two modules; each module's §5 points there. The one outstanding foundation defect (RFC1-28/31 queue stage) sits in module 1 §5; the four closed ones are named in README §5 with the trail in history. |
| §6 Alternatives considered | moved to rationale/history | history §6; pointer in README §6 | All seven moved wholesale; the two load-bearing ones (closure-without-merge naming; composite score) keep a one-sentence pointer in README §6 per the charter. |
| §7 Deliberately deferred | retained with wording sharpened | per-module §7; package-level items in README §7 | Every deferral retained, including the binding obligation to declare each deferred *value*. The **non-deferring column-layout obligation** is held in README §7 because it binds RFC8-12's partition across the package. |
| §3.16 phase boundary | retained unchanged | module 3 §3.16; scope note in README | RFC8-32 verbatim in module 3; README records that its clause-to-requirement coverage matrix must span RFC8-1…RFC8-31 across **all three modules**, not module 3 alone. |

> *Correction 2026-08-05 (refactor round): the RFC8-25 row's dangling 'report judgment call 1' pointer was repointed to WORKER-REPORT-DIGEST.md §"Substantive rulings", ruling 3.*
