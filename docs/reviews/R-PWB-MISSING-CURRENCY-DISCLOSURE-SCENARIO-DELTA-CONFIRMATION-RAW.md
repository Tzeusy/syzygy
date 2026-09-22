CONFIRM

Reviewed commit: `57b1d22482d26f3c028bb258bd0f6799a6f7bb3d`
Manifest SHA-256: `42dd4f91314f7aed074f21095743ba7ed175ba9518a0d8766cf38d18568209d7`

## Classification

**Normative.** The proposed scenario narrows PWB-REQ-007’s universal freshness obligation: an implementation that previously complied only by supplying freshness for every claim may cease to comply, while omission is newly admitted for the one missing-effective-bound condition. That matches the Normative definition at `SEMANTIC-DELTA-TEMPLATE.md:101-104`, notwithstanding the ruling’s “clarification scenario” wording. The rationale at `SEMANTIC-DELTA.md:19-26` is correct.

## Findings

No revise-severity or exception findings.

1. **Prior F1 — confirmed repaired**
   `IMPACT-LEDGER.md:14-58` now states a reproducible continuation predicate, the 1,376-file denominator, four exact decode skips, and all seven files/eight occurrences. Two independent methods reproduced the result:

   - Python over `git ls-tree -rz --name-only 9d741859dcee`, reading each baseline blob, UTF-8 decoding, restricting to lines containing `PWB-REQ-`, and matching `(?:,|/|\.\.|\band)\s*007\b`: **1,376 tracked files; 4 skips; 7 files; 8 occurrences**.
   - `git grep -n -E 'PWB-REQ-.*(,|/|\.\.|and)[[:space:]]*007([^0-9]|$)' 9d741859dcee --`: **7 files; 8 lines/occurrences**.

   The four skips are exactly the PNGs listed at `IMPACT-LEDGER.md:21-24`. The results include both occurrences in `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md:415-416`. Raw reviews are counted and classified as immutable review evidence, never proposed for editing, as required by `IMPACT-LEDGER.md:57-58`.

2. **Prior F2 — confirmed repaired**
   `build_pwb_missing_currency_disclosure_scenario.py:411-437` extracts the complete scenario block, removes it, and reinserts the byte-identical block after the PWB-REQ-004 heading. Independent reconstruction produced:

   - heading count: **1**
   - full scenario block preserved byte-identically: **true**
   - scenario moved across the PWB-REQ-004 boundary: **true**
   - `scenario_findings`: exactly `["disclosure scenario is not in the required PWB-REQ-007 position"]`

   Thus the placement predicate at `:166-173`, rather than heading-count failure at `:163-165`, kills the mutant.

3. **Semantic and authority review**
   The proposed scenario preserves `Unknown`, exact primary reason, exact route, tier, challenge state, semantic identity, evaluation identity, and aggregate polarity at `proposed/spec.md.patch:7-22`. It creates one explicit freshness exception and neither assigns nor implies `fresh`, `stale`, `broken`, `superseded`, or a fifth freshness value. This correctly reconciles PWB-REQ-007 with RFC2-9, RFC2-10, RFC2-24, and CAP1-REQ-062 while exposing the remaining contract tension rather than purporting to amend the RFCs.

4. **Same-change subject and contract coverage**
   Independent patch application reproduced all eleven manifest rows: **6 patched, 5 byte-identical**. The five changed coverage judgments are exactly RFC6-14.r1, RFC6-14.r3, RFC6-17.r1, RFC7-16.r1, and RFC7-33.r1. Regeneration verifies **132 covered / 242 Unknown uncovered / 248 believed not applicable = 622 total**. No additional PWB-REQ-007-covered consequence is invalidated by the narrow freshness exception.

5. **Manifest and composition**
   Independent application and hashing matched all eleven manifest rows and recomputed the manifest digest exactly as `42dd4f91314f7aed074f21095743ba7ed175ba9518a0d8766cf38d18568209d7`.

   Spec composition results:

   - exact-source: both orders apply; identical final digest
   - machine-view: both orders apply; identical final digest
   - opening-band `.21`: both orders apply; identical final digest
   - lane B first, then this package: applies
   - this package first, then lane B raw patch: fails as declared, requiring later-package regeneration
   - exact-source capability patch: both orders apply identically
   - all four sibling generated-dependency patches: collide in both orders, correctly routing to regeneration

6. **Builder and governance gates**
   Commands actually run:

   - `uv run scripts/build_pwb_missing_currency_disclosure_scenario.py --check` — exit 0; eleven subjects, six patched/five unchanged, scenario, regeneration, and sibling-order rules verified.
   - `uv run scripts/build_pwb_missing_currency_disclosure_scenario.py --selftest` — exit 0; missing/duplicate scenario, placement, fabricated freshness, aggregate absorption, stale manifest, path order, patch drift, dependency drift, contract-coverage drift, sibling orders, and generated-patch collisions all failed closed.
   - The six exact patch files were inspected directly; builder `--diff` is a direct ordered emission of those files at `build_pwb_missing_currency_disclosure_scenario.py:536-539`.
   - `python3 scripts/check_governance.py` — exit 0 over **1,389 tracked files** at the reviewed head.
   - `python3 scripts/check_governance.py --selftest` — exit 0; **263 fixtures, 0 failing**.
   - Final `git status --short` — empty.
   - Final `git rev-parse HEAD` — exact reviewed commit.

7. **Parked `.18` and authority separation**
   `.18` was treated solely as the unperformed candidate checkpoint at `4d78776`, never as effective authority. Nothing in this package merges it, selects its proposed values, treats its presence as unblocking a class, performs an act, authors a recorder, authorizes implementation, or claims the disclosure route currently renders. Candidate banners and the distinction between drafting, adoption, and implementation remain explicit.

## Sign-off readiness

The corrected exact bytes are ready for the owner sign-off stage once this raw `CONFIRM` is retained according to CC-REV-6. The current packet deliberately does not itself perform or offer the act before that retention.

Even after specification sign-off, implementation remains separately blocked on:

- lane B / `syzygy-dov.17`;
- the `.18` registry-entry amendment act;
- the `.19` continuation direction;
- fresh implementation authorization resolving the five disclosed contract-coverage gaps and naming the exact built behavior.

Silence or general approval performs nothing and leaves current signed behavior in force.
