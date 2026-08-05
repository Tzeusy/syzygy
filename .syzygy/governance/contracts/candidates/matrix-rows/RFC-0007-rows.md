# RFC-0007 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0007-polaris-intent-surface.md` (frozen,
9,843 words, RFC7-1…RFC7-38 plus RFC7-11(a)).
Active target: the **`../rfcs/RFC-0007/` contract package** — `README.md` index,
`narrative-contract.md` (module 1, RFC7-1..RFC7-25), `rendering-and-surface.md`
(module 2, RFC7-26..RFC7-38). The pre-split single file
`../rfcs/RFC-0007-polaris-intent-surface.md` was deleted after the sweeps below.
History target: `../history/RFC-0007-history.md`.

No clause was merged, retired, or renumbered. All 38 numbered clauses and all
7 lettered sub-clauses survive, each in exactly one module.

## Word-count arithmetic

| Stage | Words |
|---|---|
| Frozen rev9 source | 9,843 |
| Compacted single file (pre-split) | 8,006 |
| `narrative-contract.md` | 5,167 |
| `rendering-and-surface.md` | 3,143 |
| `README.md` | 2,326 |
| Package union | 10,636 |
| **Default reading path for one task** | **7,493** (index + module 1) or **5,469** (index + module 2) |

The union exceeds the single file because the index restates the package's
scope, doctrine grounding, and integration once for both modules; no normative
clause is duplicated. Every file is under the ~7,000 ceiling. The compaction
stopped at 8,006 rather than the ~4,500 target because the residue is
charter-protected: ~500 words of copied tables, 425 of violation cases, ~450 of
security reasoning that must keep its reasoning rather than its conclusion,
~700 of closed enumerations, and RFC7-38 verbatim.

## Verification sweeps (run against the package union vs the frozen source)

1. **Clause exclusivity** — for each of RFC7-1…RFC7-38, count of `**RFC7-n —`
   headings across both modules equals exactly 1. Zero problems. RFC7-11(a)
   heading present once, in module 1.
2. **Backticked-token diff** — four tokens in source and not in the union, each
   deliberate: `05-POLARIS-BRIEF.md` (charter bars `_bootstrap/` paths in active
   normative text → history); `records/` standalone (the full path
   `.syzygy/governance/records/` is present in RFC7-31); `reduced-fidelity`
   (RFC7-37 worked example → history); and `anchored — target changed since
   authorship`, which the line-based grep misses and a newline-flattened re-grep
   confirms present in RFC7-11(a). This sweep previously caught a real defect —
   `dismissed-by-decision` had dropped out of RFC2-25's closed three-state list,
   restored in RFC7-20.
3. **Cross-RFC clause-reference diff** — every `RFCn-m` reference to another RFC
   preserved except `RFC3-31`, which appeared only in the §6 portfolio
   meta-project alternative and travelled with it to history.
4. **Doctrine-rule diff** (`VIS-*`, `SEC-*`, `SDR-*`) — zero dropped.
5. **Decision identifiers** — `A4`, `B5`, `B6`, `B7`, `B10`, `OQ-010` all
   present in the union (plus `A1` in each Status header); matches the source
   set exactly.
6. **Violation-case distribution** — 1–7, 12, 14 in module 1; 8, 9, 11 in
   module 2; 10, 13, 15 (package-spanning) in the README. All 15 accounted for,
   none renumbered, none duplicated.
7. **Stale section references** — zero `§3.x` cross-references survive in the
   modules; all were converted to clause IDs or to `README.md` §n, so no
   citation depends on a section number that moved at the split.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC7-1 | retained unchanged | narrative-contract.md | Identity clause already minimal; no prose to compress. |
| RFC7-2 | retained with wording sharpened | narrative-contract.md | Three-way taxonomy and "no fourth kind" copied verbatim; the authoring-act limb tightened without changing scope. |
| RFC7-2(a) | retained unchanged | narrative-contract.md | "Anchored" definition is part of the closed taxonomy — copied, not paraphrased. |
| RFC7-2(b) | retained unchanged | narrative-contract.md | "Explicitly non-normative" definition copied verbatim; cited by RFC7-17's argument band. |
| RFC7-2(c) | retained unchanged | narrative-contract.md | "Epistemically labeled" definition copied verbatim, including the Observed/Inferred/Unknown enumeration. |
| RFC7-3 | retained unchanged | narrative-contract.md | Load-bearing non-citation invariant and deletion invariant; wording preserved at identical strength. |
| RFC7-4 | retained unchanged | narrative-contract.md | Already one sentence of obligation. |
| RFC7-5 | retained with wording sharpened | narrative-contract.md; rationale → history | Entity table copied verbatim; the presentation-profile justification (RFC1-7 reconciliation, "disconnected specification browser") moved, all five profile rules and owner decision A4 kept. |
| RFC7-6 | retained with wording sharpened | narrative-contract.md; rationale → history | Cardinality rule and "thin, never absent" kept with the v1.md quote; the RFC7-31-meaningfulness reasoning moved. |
| RFC7-7 | retained unchanged | narrative-contract.md | SDR-13 artifact-class obligations are a closed list of four properties plus the SEC-4 rules. |
| RFC7-8 | retained unchanged | narrative-contract.md | Cache/governance boundary already minimal. |
| RFC7-9 | retained with wording sharpened | narrative-contract.md; rationale → history | Granularity rule kept; the admissibility-floor derivation compressed to its binding statement, the challenger walkthrough moved. |
| RFC7-9(a) | retained unchanged | narrative-contract.md | "Covers" definition is binding and load-bearing for (c); copied verbatim. |
| RFC7-9(b) | retained unchanged | narrative-contract.md | "Minimality" and the surplus-anchor defect rule copied verbatim. |
| RFC7-9(c) | retained with wording sharpened | narrative-contract.md | "Bounding" rule, the twenty-anchor non-conformance case, and the splitting obligation kept; the meta-commentary on why covering is defined as attribution moved to history. |
| RFC7-10 | retained with wording sharpened | narrative-contract.md; analogy → history | Anchor tuple and the closed target-class enumeration copied verbatim; the RFC2-11/RFC2-18 analogy moved (the citation survives in active §5). |
| RFC7-11 | retained unchanged | narrative-contract.md | Broken-anchor degradation semantics and the four prohibitions preserved verbatim. |
| RFC7-11(a) | retained with wording sharpened | narrative-contract.md; rationale → history | Drift rendering obligation, review mark, non-drift rule, and the "mints no RFC2-24 reason" boundary kept; the third-door reasoning moved with a backlink. |
| RFC7-12 | retained unchanged | narrative-contract.md | Restatement discipline already minimal. |
| RFC7-13 | retained with wording sharpened | narrative-contract.md | Per-altitude obligation and the V0 ordering enumeration kept verbatim; owner decision B7 now cited in place of the §8 q7 pointer. |
| RFC7-14 | retained with wording sharpened | narrative-contract.md; rationale → history | Verbatim-leaf rule and the adjacency rules kept in full; the two-alternatives rationale moved, owner decision B5 cited in place of the authored-position marker. |
| RFC7-15 | retained with wording sharpened | narrative-contract.md | Catalog honesty rules kept; connective prose tightened. |
| RFC7-16 | retained with wording sharpened | narrative-contract.md; rationale → history | Minimal-density fact set (label + tier + freshness + evaluation identity + handoff) and the composite-maturity prohibition kept; the RFC6-21/RFC1-19 derivation and the reservation narrative moved. |
| RFC7-17 | retained with wording sharpened | narrative-contract.md | Three authority classes and the full three-band composition copied verbatim as a closed enumeration; owner decision B7 cited. |
| RFC7-18 | retained unchanged | narrative-contract.md | Single-drawer and no-second-copy rules already minimal. |
| RFC7-19 | retained unchanged | narrative-contract.md | Empty-block rule already one sentence. |
| RFC7-20 | retained with wording sharpened | narrative-contract.md | Draft-state rules and the SEC-2 consent degradation kept; owner decision B10's `editorial-draft`/`unadopted-draft` distinction folded in from the discharged §5 defect so the decision stays in the active file. |
| RFC7-21 | retained unchanged | narrative-contract.md | Per-claim attestation rule and the RFC3-16(a) provenance argument are a protected security premise — reasoning kept, not just the conclusion. |
| RFC7-22 | retained unchanged | narrative-contract.md | Queue ownership and rejection rules already minimal. |
| RFC7-23 | retained unchanged | narrative-contract.md | Acts-and-gates table copied verbatim, all four rows and all gate text. |
| RFC7-24 | retained unchanged | narrative-contract.md | SDR-18 seam boundaries already minimal. |
| RFC7-25 | retained with wording sharpened | narrative-contract.md; rationale → history | Deterministic floor, asymmetric declaration with owner decision B6's verbatim answer, the RFC7-11(a) review trigger, the record home and rendering duty, and the RFC3-16(a) verdict argument all kept; the VIS-4 derivation and the rot walkthrough moved. |
| RFC7-26 | retained with wording sharpened | rendering-and-surface.md | Both mode names, the Base-includes-observed rule, and the no-synonym rule kept; the trailing qualifier moved. |
| RFC7-27 | retained unchanged | rendering-and-surface.md | No-fictitious-consensus rule already minimal. |
| RFC7-28 | retained unchanged | rendering-and-surface.md | Curated-diagram obligations are a closed list; copied. |
| RFC7-29 | retained unchanged | rendering-and-surface.md | Boundary table copied verbatim, all ten rows plus the closing rule. |
| RFC7-30 | retained with wording sharpened | rendering-and-surface.md; rationale → history | All six walkthrough prompts, the second-phase check, and the non-visual-run obligation kept verbatim; the pass-every-time reasoning compressed, the duplicated record-home gloss moved. |
| RFC7-31 | retained with wording sharpened | rendering-and-surface.md; History parenthetical → history | Two floors, two homes, the deletion-invariant argument, RFC3-16(a) honoring, and `verdict-unlawful` kept; the rev7-alignment *(History: …)* parenthetical extracted verbatim. |
| RFC7-32 | retained unchanged | rendering-and-surface.md | Trigger clause already minimal. |
| RFC7-33 | retained with wording sharpened | rendering-and-surface.md | Full distinction enumeration copied verbatim; the non-citability-travels argument is a protected security premise and keeps its reasoning; the type-name rule kept. |
| RFC7-34 | retained with wording sharpened | rendering-and-surface.md; rationale → history | Both limbs — recoverability and reachability — kept with their enumerated traversals; the SDR-27 half-coverage gloss compressed. |
| RFC7-35 | retained unchanged | rendering-and-surface.md | Workspace-manifest boundary already minimal. |
| RFC7-36 | retained with wording sharpened | rendering-and-surface.md; rationale → history | Both carry-over lists, the status-assertion prohibition, and the OQ-010 note kept in full; the framing sentences moved. |
| RFC7-37 | retained with wording sharpened | rendering-and-surface.md; example → history | Declared-relation semantics and the RFC6-17 full-composition disclosure kept verbatim, including "cited, never restated here"; the worked counter-example moved. |
| RFC7-38 | retained unchanged | rendering-and-surface.md; History parenthetical → history | Binding phase rule preserved at verbatim strength (shape-parallel with RFC6-28/RFC8-32/RFC9-52); only the *(History: added at the rev8 rework, directive item 7.)* parenthetical was extracted. |
| q1 | answered — moved to history | history §8 q1; navigational row in `README.md` §8 | Materiality authority; answered by owner decision B6, whose ruling is carried in RFC7-25. |
| q2 | open — retained | `narrative-contract.md` §8 | Primary-narrative cardinality (RFC7-6); unanswered, retained compactly. |
| q3 | answered — moved to history | history §8 q3; navigational row in `README.md` §8 | Editorial-draft surface state; answered by owner decision B10, whose ruling is carried in RFC7-20. |
| q4 | open — retained | `narrative-contract.md` §8 | Rejected-draft retention (RFC7-22); unanswered, retained compactly. |
| q5 | answered — moved to history | history §8 q5; navigational row in `README.md` §8 | Presentation-profile scope; answered by owner decision A4, whose ruling is carried in RFC7-5. |
| q6 | answered — moved to history | history §8 q6; navigational row in `README.md` §8 | Verbatim leaf under a proposed reading; answered by owner decision B5, whose ruling is carried in RFC7-14. |
| q7 | answered — moved to history | history §8 q7; navigational row in `README.md` §8 | V0 disclosure enumeration; answered by owner decision B7, whose ruling is carried in RFC7-13 and RFC7-17. |

## Non-clause material

| Item | Outcome | Target | Reason |
|---|---|---|---|
| §0 Reader's summary | retained with wording sharpened | `README.md` package reader map + each module's §0; dropped bullets → history | Charter allows a short reader map; bullets that restated RFC7-13/16/30/33 verbatim moved. |
| §1 Summary | retained with wording sharpened | `README.md` Scope | SDR §2 charter quote preserved verbatim; the clause-list sentence dropped as duplicative of §0's structure line. |
| §2 Motivation | retained with wording sharpened | `README.md` §2; brief citation → history | Doctrine quotes and the SDR-13…18 ruling list retained; the `_bootstrap/` brief citation moved (charter bars `_bootstrap/` paths in active normative text). |
| §4 Violation cases | retained unchanged | distributed: modules §4, spanning cases 10, 13 and 15 in `README.md` §4 | All 15 cases retained; Tier 1 explicitly keeps violation cases. |
| §5 Integration | retained with wording sharpened | two-layer: `README.md` §5 package edges; each module §5 module-local; defects 1 and 3 narratives → history | All reliance citations kept and RFC 0003/0004/0005 added where the body actually depends on them; the discharged (B10) and resolved defect narratives moved with backlinks, decision IDs kept in the active file. |
| §6 Alternatives considered | moved to rationale/history | history §6; load-bearing pointer in `README.md` §6 | Charter moves §6 wholesale; the two alternatives load-bearing for RFC7-25 and RFC1-27 keep a one-sentence pointer in the active §6. |
| §7 Deliberately deferred | retained with wording sharpened | `README.md` §7 (package-level) | Tier 1 keeps explicit deferrals; composite-maturity deferral folded in from RFC7-16, RFC 0006 §7 re-cited as a named deferral rather than a section number. |
| End-of-contract marker | retained with wording sharpened | `README.md` end marker + per-module end markers | Restated to enumerate the full sub-clause set and assert the range is contiguous with no gaps. |
| Clause map and lookup rule | new at the split | `README.md` | Deterministic `n ≤ 25` → module 1, `n ≥ 26` → module 2; sub-clauses live with their parent; ranges contiguous and exhaustive so no search is needed. |
| Seam documentation | new at the split | `README.md` | Names the reader-group seam and enumerates the twelve cross-module citation edges, all resolvable by the lookup rule. |

> *Correction 2026-08-05 (refactor round): the four RFC-0007 word figures above were refreshed to the recounted values (2,268→2,326; 10,578→10,636; 7,435→7,493; 5,411→5,469), matching rfcs/RFC-0007/README.md and the 04 change log.*
