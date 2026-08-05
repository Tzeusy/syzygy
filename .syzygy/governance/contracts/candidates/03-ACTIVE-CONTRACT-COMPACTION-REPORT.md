# Active-contract compaction report (directive §3) — owner-facing

## What was done

Nine independent compaction passes (one per RFC, fresh-context workers
under `COMPACTION-CHARTER.md`), followed by owner-authorized package
splits. Three tiers enforced: Tier 1 (normative) stays active; Tier 2
(rationale, amendment history, answered questions, alternatives) moved to
`history/` with backlinks — **27,521 words extracted**; Tier 3 (index,
load map) generated as rebuildable projections. All 294 rev9 clause
identities survive unchanged — zero merged, retired, renumbered, or routed
out (04-CLAUSE-MIGRATION-MATRIX, verified by script). Two new contracts
(RFC-0010/0011) and one new sub-clause (RFC3-16(c)) were added under owner
direction.

## The numbers, stated honestly

| Measure | rev9 | rev10 |
|---|---|---|
| Normative contract text (rev9-derived) | 90,410 w | **73,685 w (−18.5%)** as compacted single files |
| + package-split scaffolding (front matter, status headers, module maps across 25 module files) | — | +7,333 w |
| + package README indexes (7) | — | +12,696 w |
| + new contracts RFC-0010/0011 | — | +5,353 w |
| **Total on disk (32 modules)** | 90,410 w | **99,067 w** |
| Tier 2 history (linked, non-normative, outside every default load) | interleaved | 27,521 w in `history/` |
| **Mandatory reading path for one governed task** | **~90,410 w (whole corpus — the only safe instruction)** | **10,900–18,300 w measured** (five fixtures; median ≈ 13,900 w ≈ 18.7k tokens) |

**The 35,000–50,000-word corpus band was not reached, and no pass could
reach it faithfully.** Every one of nine independent workers converged on
−12% to −22% with per-RFC arithmetic: the corpus is dominated by content
the charter's hard rules forbid compressing — verbatim closed vocabularies
and tables (~8,000 w across the corpus: RFC1's entity/plane/relation
tables, RFC4-19's envelope table, RFC8-13's derivation tables, RFC5/9's
closed sets), protected security reasoning ("forgeable from inside the
tree" arguments), and clauses carrying 3–5 distinct obligations each.
Reaching 40k would have required deleting roughly 3,000 words of
obligations per RFC — exactly what OD-R10-3 forbids ("do not achieve the
target by deleting constraints"). Per-RFC floor accountings:
`WORKER-REPORT-DIGEST.md` and each `matrix-rows/` preamble.

**What the owner's actual optimization target got instead.** The stated
target is "minimum complete governed context required for one decision or
work item, not minimum document count." That is delivered by structure,
not shrinkage: 7 packages ⇒ 25 normative modules averaging ~3,000 words,
each package README carrying a deterministic clause-lookup rule, and
machine metadata (`05-CONTRACT-INDEX.yaml`) for deterministic selection.
Measured result (fixtures 1–5): a typical governed task mandatory-loads
**~11–15% of the rev9 reading path**, with the one risk-class exception
disclosed rather than trimmed (fixture 2). RFC-0001 remains the single
justified oversize module (8,353 w — a dictionary with indivisible reader
groups; justification printed by the verifier and carried here).

**Total-size honesty:** the on-disk corpus *grew* 8% because packaging
costs scaffolding and two new contracts were added. No claim of a smaller
library is made; the claim — measured, re-runnable
(`scripts/context_load.py`) — is a 6–8× smaller mandatory reading path per
task, which is what context bloat actually was (finding F2).

## What moved where (Tier 2)

Per-RFC `history/RFC-000n-history.md`: every `*(History:…)*`
parenthetical verbatim; §6 alternatives wholesale (load-bearing ones keep
a one-sentence stub + pointer); 24 answered §8 questions with answers
verbatim (stubs with decision IDs remain active — numbering immutable);
review-origin and amendment narratives; superseded text (notably RFC8-25's
pre-B13 fallback, retired with reasoning). Nothing was deleted; nothing
rewritten to look cleaner.

## Semantic-preservation verification

- `scripts/verify_final_prespec.py`: **PASS** — 322 numbered clauses (294
  rev9 + 16 + 12), every package complete/disjoint, all citations
  resolve, no live History parentheticals, six phase-rule clauses
  present, matrix outcome vocabulary closed, fixtures complete.
- Each worker ran adversarial sweeps (obligation-sentence diffs,
  closed-vocabulary token checks, decision-ID censuses, epistemic-label
  counts) recorded in its `matrix-rows/` preamble; three near-losses were
  caught and restored by those sweeps before delivery (RFC2-13's VIS-7
  exemption; RFC2-18's "never as two independent aggregates"; RFC7-20's
  `dismissed-by-decision` enumeration).
- The substantive rulings a semantic-equivalence reviewer must judge are
  enumerated in `WORKER-REPORT-DIGEST.md` §"Substantive rulings" (six
  items — none silent).

## Disclosures added at review convergence

- **The one inference drawn from an owner answer's scope (q1(b)).** The
  RFC 0002 pass records decision A5's answer ("The list grows to twelve:
  #12 added, #11 retained") and infers from its closed scope that reason
  #10 was **not** split — the deduction the rev10 directive's RFC2-24
  question required. That inference is disclosed at
  `history/RFC-0002-history.md` §q1(b) and is the corpus's single
  acknowledged inference-from-answer; it is surfaced here so the owner
  reads it in the report, not only in history (equivalence-review E5).
- **`[Observed:]` source-pointer attrition.** Rev9 carried 121
  `[Observed: <source>]` citations with explicit sources; the rev10 active
  corpus carries 92 (RFC-0004 accounts for most: 30 → 13 — its per-cell
  source pointers were shortened to bare labels during envelope-table
  compaction, with the full pointers preserved in history). Epistemic
  labels themselves rose 253 → 302 and no label class was lost; but a bare
  `[Observed]` is a weaker claim than a sourced one, and RFC-0004 is the
  evidence-adapter contract where provenance traceability matters most.
  Stated rather than silent (equivalence-review E7).

## Risks accepted at this report

1. Package scaffolding duplicates *navigational* prose per module; a
   drift between a README map and module front matter is now possible —
   mitigated by the verifier's package checks (run per change).
2. The §8-stub convention keeps question numbering stable but places
   answers in history; a reader who skips the stub's decision cite reads
   less context than rev9 offered — mitigated by verbatim answers one
   link away.
3. RFC-0001's 8,353 words remain a single mandatory load for kernel
   tasks; accepted as the honest floor of a dictionary contract.
