# Disposition register — round 2026-08i reviews (P-41/P-42 cycle)

> Dispositions for the raw reviews stored beside this file. Raw reviewer
> bytes are never edited; every finding is dispositioned here as
> `repaired` · `open` · `declined`, with the evidence. Maintained by the
> convergence-pass lead session, 2026-08-17.

## RD-69 — combined fresh-context review of the repaired P-41/P-42 subjects

- **Raw:** `RD-69-p41-p42-combined-RAW.md` (delivered in three parts;
  provenance banner in the file).
- **Subjects at commit `be5af43`** (sha256):
  - CC-SPEC candidate —
    `c3261a8523656b38e733e230c85bf7d49390698a7fc36f1aa66cbee5de66533b`
  - CC-IMPACT candidate —
    `cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0`
  - P-44 offer —
    `beb84463d916502178eca5db2201431588efbed73bbefe58661402bcea27b2f7`
- **Verdict, copied exactly:** `VERDICT: REVISE`
- **Findings:** 1 launch blocker, 5 non-blocking (N1–N5).

| Finding | Disposition | Evidence / route |
|---|---|---|
| **BLOCKER 1** — CC-SPEC-8 opened a second, weaker home for the reviewed-N/A rule over nine contract modules, with a false absence claim | **repaired** (2026-08-17, the cycle's one blocker-only repair, reviewer's clear-path (i)) | D2-6 in `../SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-2.md`: CC-SPEC-8 reduced to a citation of RFC1-33/RFC6-28/RFC7-38/RFC8-32/RFC9-52 for home, gate, unit, effect; false sentence and five-field record deleted; "applicable" definition and production obligation kept; unit corrected to per observable consequence. **Unconfirmed until the confirming review (RD-70) returns** |
| N1 — SDR-37's "one coherent change to one" limb has no acceptance criteria in CC-SPEC | **open** — batched to the next authoring pass; surfaces to the owner in the P-41 offering as a disclosed `[Unknown]` (what settles it: a change-scoped acceptance rule, decided when the first amendment-sized change exists; for Capability 1's first spec, change and capability coincide) | five-part test: fails condition 4 (reviewer's own classification; concurred) |
| N2 — `decisions[]` warrant citation cannot distinguish ruled-but-unnumbered decisions (P-33/P-35/P-38/P-39) from pending ones; P-43 owns the settling question | **open** — already owned by open queue row **P-43**; the P-41 offering will name P-43 as the settling question | fails condition 4; no clause edit in the blocker-only repair |
| N3 — CC-SPEC-2's closed six-class "warrant" set sits beside doctrine's closed four-class work-warrant set with no slot for a confirmed finding | **open** — batched; candidate fix is one scoping sentence plus a named class or exclusion; vocabulary seams are P-18's subject | fails conditions 2 and 4 |
| N4 — P-44 offer: warrant "Owner charter §9.6" unresolvable in-tree; arm (a) yields "one carve-out"/"second carve-out" contradiction; expiry has no named detector | **open** — P-44 is not launch-critical (arm (b) verified costless); the offer must be repaired **before any arm-(a) act**, and its queue row will say so | fails condition 1 |
| N5 — dated claims (CC-SPEC-2 sweep counts; P-44 "one day old"/"not yet dispatched"; craft README tier-1 "SDR-1…33") and one claim RD-69 cannot verify (CC-IMPACT-7's RD-59 pass, barred by fresh context) | **open** — staleness batched to the next authoring pass; the CC-IMPACT-7 limb is not repairable by edit: the RD-59 record exists (`../../round-2026-08g/reviews/DISPOSITION-REGISTER.md`) but is structurally invisible to any fresh-context review — disclosed to the owner in the P-42 offering | fails conditions 3 and 4 |

**Cycle state after this register:** the one blocker-only repair is made;
the one confirming review is dispatched over the repaired bytes' new
frozen digests. If a real blocker survives it, the matter returns to the
owner with four choices (repair under new instruction / reduce scope /
defer the acts / accept the risk on the record) — never a third repair
cycle in this pass.
