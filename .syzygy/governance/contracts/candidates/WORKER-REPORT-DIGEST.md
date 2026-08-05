# Worker-report digest (lead's working record, non-normative)

Key figures and rulings from the nine compaction-pass reports, persisted
verbatim-in-substance so the 03 report and reviewers can cite them. Full
reports were delivered in-session; matrix-rows preambles carry each pass's
sweep numbers.

## Per-RFC results

| RFC | Source → active | Outcome | Incompressibility floor |
|---|---|---|---|
| 0001 | 9,534 → 8,352 (−12.4%) | single file (above band, justified) | 1,919 w (23%) verbatim tables/enumerations (entity/plane/relation/four-sense tables); dictionary-shaped — reader groups not distinct, no split |
| 0002 | 9,323 → 7,554 (−19.0%) | package ×4 COMPLETE (1,964+2,231+2,477+2,397 + README 1,818; sliced not retyped, single deleted) | ~1,400 w tables/lists; only ~1,750 w Tier 2 existed; 112-obligation diff run, 1 precision loss caught+restored |
| 0003 | 10,193 → 8,196 (−19.6%) | package ×2 COMPLETE (4,824 + 4,275 + README 920; sweeps clean, single deleted) | 990 w verbatim blocks + ~760 w protected RFC3-16(a) + ~420 w NEW RFC3-16(c); densest RFC: 37 clause IDs |
| 0004 | 9,621 → 8,882 module total (pkg 10,558 w/ README) | package ×4 **complete, verified** (1,680/3,685/1,775/1,742 + README 1,676) | RFC4-19 envelope table 614 w; Tier 2 only ~1,850 w (19%); 31/31 byte-identical spliced |
| 0005 | 7,819 → 6,543 (−16.3%) | package ×3 COMPLETE (3,643+2,351+2,197 + README 2,005; pointer-only diffs, single deleted) | six verbatim-required blocks; §2 clauses 4,619 w; all Tier 2 already extracted |
| 0006 | 5,017 → 4,174 (−16.8%) | single file | clause text alone 2,898 w; RFC6-5 outcome table 335 w |
| 0007 | 9,843 → 8,006 (−18.7%) | package ×2 COMPLETE (5,162+3,189 + README 2,167; zero stale §-refs, single deleted) | ~500 w tables + ~450 w protected security reasoning + ~700 w closed enumerations; 4 passes, diminishing 215/230/88 |
| 0008 | 9,791 → 7,650 (−21.9%) | package ×3 COMPLETE (2,686+3,507+3,055 + README 1,921; one intended diff RFC8-27, single deleted) | RFC8-13 derivation + RFC8-4 ontology tables 976 w; 17/32 byte-identical |
| 0009 | 19,269 → 15,568 modules (−19.2%: 6,999+5,540+3,029 + README 2,029) | package ×3 COMPLETE (52 clauses uniquely homed; 20/20 History extracted; obligation deltas traced) | clause bodies 14,305 of 19,269 source words; six passes on module 1 → 6,999 floor |
| 0010 | new | 2,453 | — |
| 0011 | new | 1,880 | — |

**Projected active corpus ≈ 67–70k words** (vs rev9's 90,410 + no 0010/0011). *[Stale mid-run projection — final measured figure is 99,067 on disk (post-review fix batch) incl. package scaffolding, READMEs, and the two new contracts; the honest accounting is the 03 report's §"The numbers". Kept here unedited as the historical projection.]*
The 35–50k band is unreachable by faithful prose compaction — every
independent pass converged on −12% to −22% with arithmetic. The owner-facing
justification (OD-R10-3's escape hatch): the real context reduction is
**selective loading** — 6 packages ⇒ 19 modules, mean module ~3,200 w,
median task loads 2–4 modules (see 06-CONTEXT-LOAD-MAP).

## Substantive rulings made (for the semantic-equivalence reviewer)

1. **RFC3-16(c) added** (directive §2 repair) — two-state model; full text
   in the governance-homes module; acceptance-record rewording is the
   lead's task in the FINAL record.
2. **RFC5-3/RFC5-5 sharpened additively** (two classes exhaustive; official
   CLI/MCP/scripts/fleet workers are machine clients); **§8 q1 scope
   ruling** added (mechanism selection blocks V0 implementation, not
   specification); new violation case 2.
3. **RFC8-25's "operative limit" fallback retired as superseded by B13**
   (strictly stricter) — the one clause-text semantic resolution; verbatim
   in history.
4. **RFC2-24 "#10 not split"** written as deductive entailment of A5's
   closed-at-twelve; per-cell amendment narratives → history.
5. **RFC2-13 near-loss caught**: "the act itself is not subject to the
   VIS-7 identity test" restored before finalization (worker's own sweep).
6. RFC-0001: B20 cite moved adjacent to the spelling decision; no §2 in
   active file (rev9 §0+§1+§2 merged, §3–§8 numbering preserved).

## Cross-worker facts for RFC-0010/0011

- Work-state contract: **RFC8-12** (13 values, 3 partitions, A8) +
  **RFC8-28** chain state — two fields, never folded; RFC8-30 gates "done".
  RFC-0010 §5 updated accordingly.
- Human/machine parity: **RFC6-13** (+RFC6-14 label parity, RFC6-18 fact
  set). RFC-0010/0011 cite RFC6-13/14.
- RFC5-25 location constraint verbatim (audit trail outside `.syzygy/**`).

## Outstanding at this writing

RFC-0002 split; RFC-0003 governance module + README + deletion; RFC-0005
modules B/C + README + deletion; RFC-0008 split; RFC-0009 README + history
+ rows + report (incl. RFC9-9 follow-on item); RFC-0007 report + split
decision. All six workers resumed post-limit-reset 2026-08-03.
