# Review — PWB opening-band aggregate scenario (PWB-REQ-010)
Reviewed commit: 59733d32acec9d6d4573a15de75177bed5a48ac3
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the package was not
read before this review, and none of the other agents active in the parallel
session (draft-opening-band or any other) was consulted, per CC-REV-1's
independence requirement. Read-only throughout; every mutation ran in a
`cp -r` scratch copy under the session scratchpad, never in the reviewed
worktree. Class: fresh-reader semantic review of a normative delta (CC-REV-4,
CC-REV-6), against `REVIEW-BRIEF.md`'s twelve criteria plus seven additional
criteria (a)–(g) named in this review's commissioning brief.

---

## What I ran

All read-only against the reviewed worktree unless stated as a scratch copy.

1. `git rev-parse HEAD` → `59733d32acec9d6d4573a15de75177bed5a48ac3`; `git
   branch --show-current` → `review/opening-band-scenario`; `git status
   --porcelain` → empty. Matches the brief.
2. `sha256sum PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` →
   `7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46`.
   Digest computed, never transcribed (rule 3). Equals the value quoted in
   `OWNER-DECISION-PACKET.md`.
3. `python3 scripts/build_pwb_opening_band_scenario.py --check` → exit 0:
   "PWB opening-band scenario manifest matches 11 proposed behavior subjects
   (2 patched, 9 unchanged); the proposed declaration equals its
   regeneration and the spec patch composes with the lane B spec patch in
   both orders."
4. `--selftest` → exit 0: "closed population, byte drift, path order,
   subject drift, patch corruption, lane B composition (both orders and a
   corrupted case), generated-declaration tampering and the
   declaration-patch collision all fail closed" — matches criterion 10's
   named predicate list exactly.
5. `--diff` → byte content matches `proposed/spec.md.patch` and
   `proposed/GOVERNING-DEPENDENCIES.md.patch` exactly (the scenario insertion
   at spec.md line 618 onward, and the single digest-line change in
   `GOVERNING-DEPENDENCIES.md`, with the requirement/authority totals — 17,
   96 — unchanged on both sides of that line).
6. Applied both `proposed/*.patch` files in a `cp -r` scratch copy
   (`review-scratch/pkg-only` and `review-scratch/orig`) with `git apply`;
   both applied cleanly, and the patched `spec.md` reads correctly: the new
   scenario sits after "WhatsApp is a drill-down, not the project account"
   and before the `warrants:` block.
7. **Rule 6, my own mutation (not the selftest's internal fixture).** In a
   `cp -r` scratch copy (`review-scratch/orig`, never the worktree), flipped
   one hex character of the manifest's `spec.md` row digest
   (`9a44…` → `0a44…`). Re-ran `--check`: it failed —
   "PWB opening-band scenario manifest does not verify: manifest differs
   from exact regeneration over the proposed bytes", exit 1. Restored the
   row from a backup and confirmed `--check` passed again with the original
   output. The checker fails closed on a tampered digest, independent of the
   selftest's self-report.
8. **Composability (criterion (d)), independent of the builder.** In two
   fresh scratch copies of the unpatched `spec.md`, applied lane B's
   `proposed/spec.md.patch` then this package's (order AB), and this
   package's then lane B's (order BA), with plain `patch -p6`. Both orders
   applied cleanly with no `.rej` files (only line-offset hunks, no fuzz).
   `diff` between the two resulting files: **empty** — byte-identical
   regardless of order. This reproduces the builder's own composability
   claim by a second method (rule 2).
9. **Impact ledger reproduction (criterion 9, additional (e)).** Re-derived
   all five swept figures over the 1,334-file baseline population
   (`git ls-tree -r --name-only a4a3451 | wc -l` = 1,334, confirmed) using an
   independent Python `re` script, matching `PWB-REQ-010` (36 files/110
   occurrences), the continuation-form pattern (0/0), the patched spec path
   (51/113), the patched dependencies path (9/13) and the current digest
   (13/13) — all five reproduce exactly. Also independently confirmed the
   class-3 finding: both named declarations
   (`POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
   `POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`) carry the
   current digest in a `governingBehaviorContract.version` field beside a
   `signedBy` value naming a pending registry act, exactly as claimed.
10. **Decode-failure sweep, independent (rule 2).** Re-ran the "paths that
    fail to decode are skipped" method over the same 1,334-file baseline
    (`review-scratch/baseline`, `git archive a4a3451`). Found **4** files
    that fail UTF-8 decode:
    `docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`,
    `…-repaired-wide-2026-09-09.png`,
    `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png`,
    `…-wide-2026-09-09.png` — see finding 1.
11. **Owner ruling record**, read in full (102 lines):
    `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
    Verified byte-exact: the P-71 warrant quote (arm A, "…Q7 slices 3–5
    routed through one CC-REV-2 scenario for the opening-band aggregate"),
    the "What it means" cell quote, the P-71-Q5 "no write" ruling ("Reading
    B: the return path's write into Butlers is foreclosed by the
    2026-09-02 act; slice 6 does not run"), the cross-cutting note "P-69
    Q2(a) … and P-72 Q2 … are prepared as one superseding registry-entry
    amendment act (gate bead `syzygy-dov.18`)", and the "edited on no arm"
    closing sentences in both the P-74 and P-78 rows' "What it means" cells
    — see finding 3 for a caveat on the last of these.
12. **OQ-1, additional criterion (a).** Read `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`
    Gate 5 in full (lines 1031–1454), including the eight-row RFC2-26 test
    table. Row 3 (opening band, slice 3): "**None found**" over a stated
    denominator of 41 approved requirements and 55 scenarios (including a
    sixth candidate requirement added per review 7). Row 4
    (`model.surfaces`, slice 4) and row 5 (home route, slice 5): both
    "**None**". Independently swept this specification and the three-surface
    specification for `home` and `surfaces`/`model.surfaces`: consistent
    with the funnel's own zero/near-zero counts, none in a requirement
    naming those consequences.
13. **OQ-3, criterion (c).** Read `apps/three-surface-poc/src/polaris.ts`
    lines 920–931 directly:
    ```
    function gapReasonCounts(claims: readonly ProjectShapeClaim[]): ReadonlyMap<string, number> {
      const counts = new Map<string, number>();
      for (const claim of claims) {
        if ('reasons' in claim.epistemic) {
          const reason = claim.epistemic.reasons.primary;
          counts.set(reason, (counts.get(reason) ?? 0) + 1);
        }
      }
      return counts;
    }
    ```
    Confirmed: only `reasons.primary` is read, into one count map; no
    secondary-reason handling exists. This falsifies the inherited
    PWB-REQ-007 tuple against the design's own reused projection, exactly as
    OQ-3 claims.
14. **Lane B hunk coverage, OQ-2.** `grep -n "^@@"` on lane B's
    `proposed/spec.md.patch` → hunks at `@@ -450,22` (covers 450–471) and
    `@@ -473,11` (covers 473–483), plus a third at `@@ -907,23`. Confirmed
    PWB-REQ-007's only scenario heading
    (`#### Scenario: Missing current evidence remains explicit Unknown`)
    sits at line 470 — inside lane B's first hunk — and confirmed by
    heading sweep (`### Requirement` / `#### Scenario`) that PWB-REQ-007
    carries exactly one scenario before the next requirement at line 487.
15. **Registration anchors, criterion (g).** `OWNER-DECISION-PACKET.md`'s
    "Registration at merge" section names no line numbers — it describes
    anchors qualitatively ("constants beside the existing PWB package
    constants", `_act_subjects()`, `ACT_DIGEST_COPY_FILES`, an
    existence-gated activation function, a fourth PWB successor-chain link).
    Grepped `scripts/check_governance.py` for the lane B pattern this
    package claims to mirror: confirmed real, present anchors —
    `PWB_SCOPED_AMENDMENT_LABEL`/`_DIR`/`_MANIFEST`/`_ACT` constants at
    lines 1518–1523, `_act_subjects()` at line 1976, `ACT_DIGEST_COPY_FILES`
    at line 2173, and an existence-gated activation comment referencing
    `PWB-SCOPED-ATTRIBUTES-AMENDMENT-ACT.md` at line 2300. The pattern this
    package says it will mirror genuinely exists at this commit.
16. Quotation-fidelity spot checks (criterion 1), all confirmed byte-exact
    at the cited line ranges: PWB-REQ-010 (spec.md:596–630), PWB-REQ-007's
    aggregate sentence and Observable (444–458), PWB-REQ-020 (906–910),
    RFC2-26's defined clause
    (`contracts/rfcs/RFC-0002/rendering-vocabularies.md`:196, cross-checked
    against `DIRECTIVE-REGISTER.md`:260), the M4 funnel's Q7 cell (line 119)
    and slice 3/4/5 design text (820–918), the M2 funnel's currency-probe
    text (441–480), the M3 funnel's slice-3 design text (903–935), and
    POC-REQ-032 (three-surface spec.md:578).

---

## Findings

**Finding 1 — note.** `IMPACT-LEDGER.md`'s Discovery Method states "paths
that fail to decode are skipped and **none did**" (line 27). Re-run
independently (item 10 above), 4 files fail UTF-8 decode:
`docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`,
`orrery-height-repaired-wide-2026-09-09.png`,
`polaris-existing-orrery-narrow-2026-09-09.png`,
`polaris-existing-orrery-wide-2026-09-09.png` — all binary images, none of
which could carry any of the five swept patterns. The claim is false but
inconsequential: all five reported figures reproduce exactly regardless.
This is exactly the "absence claim needs a sweep with a denominator" shape
rule 9 warns about (a mini absence-claim, "none did", asserted rather than
enumerated) inside an artifact whose whole purpose is re-derivability.
**Repair:** replace "and none did" with the actual count and the four
paths, or drop the sub-claim and state only that the population figure is
unaffected by any skip.

**Finding 2 — note.** Criterion 7 / RFC2-26 for slice 3 rests on OQ-2, which
the delta itself surfaces honestly and does not resolve: hosting the
scenario under PWB-REQ-010 supplies the *position-and-uniqueness* half of
the opening-band consequence, but the *aggregate-tuple* half is PWB-REQ-007's
subject, and PWB-REQ-007's own scenario (line 470, confirmed singular, item
14 above) is the unmodified per-claim case, not an aggregate case. So it is
not settled, on these bytes alone, that RFC2-26's "requirement **and**
scenario" bar is cleared even for slice 3 — only that this package does not
overclaim it (the delta never asserts RFC2-26 is satisfied; it says the
scenario is placed so as to clear it "for slice 3 only" while leaving OQ-2
open). This is not a defect the delta missed — it is the delta working as
designed under rule 6 — but it is a real, load-bearing gap and I flag it so
it is not casually rounded off in owner review: whoever performs the amendment
act should treat OQ-2 as a precondition of any later claim that slice 3's
RFC2-26 limb 1 is fully supplied, not merely as a placement preference.

**Finding 3 — note.** `IMPACT-LEDGER.md` and `SEMANTIC-DELTA.md` both write
"the owner ruled … in P-74 Q4 and P-78 Q4 that the adapter-registry entry
'is edited on no arm' of those moves." In the ruling record, that exact
sentence closes each row's "What it means" cell as a summary of the whole
row (which answers Q1–Q7 for P-74 and Q1–Q5 for P-78), not a sentence
explicitly scoped to "Q4" within the cell's prose. The substance is correct
— the owner did rule the registry entry is edited on no arm of either move —
but the "Q4" attribution is this package's own reasonable inference (Q4 in
both rows is the nearest registry/configuration-adjacent sub-question), not
a labelled quotation. Low severity: the claim is true and appropriately
[Observed]-labelled for the ruling itself; only the per-question tag is
slightly tighter than the source supports.

No blocking findings. Criteria 2, 3, 4, 5, 8, 10, 11 and 12 all confirm
clean with no exception:

- **Criterion 2 (change class):** Normative is correctly argued from added
  obligation ("today a renderer may place two independent aggregates… may
  give an opening aggregate no tuple… may hoist a member's Unknown out of
  its own claim" — each becomes a falsifier after adoption), not diff size.
- **Criterion 3 (scenario form):** WHEN/THEN/AND, correctly placed, every
  clause is an inspectable behaviour (count, non-displacement, tuple
  completeness, population/count equality, reachability, machine parity) —
  none states a bare value.
- **Criterion 4 (no overlap):** confirmed against all three named gates —
  no hunk touches PWB-REQ-007's or PWB-REQ-020's regions, no hunk touches
  the three-surface specification, and composability with lane B is proven
  by a second method (item 8).
- **Criterion 5 (reconciliation performed):** all three parties quoted from
  their own packets (items 12–13, and the M2/M3 quotes independently
  verified byte-exact), and each of R-1/R-2/R-3 traces to a specific bullet
  of the proposed scenario.
- **Criterion 8 (does not change):** all 8 items verified true — the patch
  is purely additive to spec.md (no `-` hunks removing existing text), the
  `GOVERNING-DEPENDENCIES.md` patch changes only the digest line (17
  requirements / 96 authorities unchanged on both sides), and the scenario
  text contains no write verb into any repository.
- **Criterion 10 (manifest/builder):** 11 rows verified, 2 patched rows
  hash post-apply bytes (spec.md row's new digest matches the
  `GOVERNING-DEPENDENCIES.md.patch`'s new digest line exactly), selftest
  names every predicate the brief lists, and an external (reviewer-driven,
  not selftest-internal) mutation confirms `--check` fails closed (item 7).
- **Criterion 11 (hygiene):** the only occurrence of the current performed
  digest (`42d073c…`) anywhere in the package is as a diff's removed line
  inside `proposed/GOVERNING-DEPENDENCIES.md.patch` — a mechanical diff
  artifact, not a prose quotation, so CG-7e/CG-15 are not implicated. No
  Butlers-repository path appears anywhere (only Syzygy-internal
  `openspec/changes/…` paths). No "accepted/adopted/signed off" language
  found by sweep. Every prose file (`SEMANTIC-DELTA.md`,
  `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`) opens
  with a candidate/inert banner naming the warrant and gate bead. No signed
  directory byte is edited in place — proposed bytes exist only as the two
  `proposed/*.patch` files.
- **Criterion 12 (scope of authority):** the delta's own banner and warrant
  section state plainly that drafting is warranted and adoption is not; the
  scenario's WHEN clause is conditional ("if one is rendered"), so a
  conforming implementation that renders no opening aggregate at all
  vacuously satisfies it — confirmed by the scenario's own text at line
  141 of `SEMANTIC-DELTA.md` ("does not require an opening aggregate to
  exist").

---

## Verdict rationale

CONFIRM WITH EXCEPTIONS. Every criterion the brief and the commissioning
message named was checked against the bytes, largely by independent,
second-method reproduction rather than by reading the package's own claims
(rule 2): quotation fidelity, the reconciliation's three parties, the
manifest/builder's fail-closed behaviour under an externally-authored
mutation, the impact ledger's five figures, and lane B composability in
both orders were each re-derived, not re-read. Nothing found rises to
REVISE: finding 1 is a factual slip that changes no conclusion, finding 2
restates and reinforces a gap the delta already surfaces rather than
missing, and finding 3 is a loose but true attribution. The package does
not perform or imply any act, schedules no implementation, and correctly
leaves five genuine, unresolved questions to the owner rather than settling
any of them in its own favor.
