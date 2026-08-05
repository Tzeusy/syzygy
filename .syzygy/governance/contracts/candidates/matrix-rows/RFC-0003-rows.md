# RFC-0003 — clause migration rows (rev9 → rev10)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0003-project-workspace-manifests.md`
(frozen, 10,193 words). Target: the **`../rfcs/RFC-0003/` contract package**
and `../history/RFC-0003-history.md`.

| Target module | Clauses | Words |
|---|---|---|
| `../rfcs/RFC-0003/manifests-and-namespace.md` (**M1**) | RFC3-1…RFC3-14, RFC3-18…RFC3-32 | 4,824 |
| `../rfcs/RFC-0003/governance-homes-and-owner-acts.md` (**M2**) | RFC3-15, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-17, RFC3-17(a) | 4,275 |
| `../rfcs/RFC-0003/README.md` (index, non-normative, duplicates no clause) | — | 920 |

Compaction produced a single 8,196-word file first; the owner-authorized split
(directive §4 pattern, OD-R10-6) then divided it into the two modules above
**without moving any clause identity**. Both modules are under the ~7,000-word
module ceiling. Lookup rule: numeric part **15–17 → M2** (with every lettered
sub-clause), **everything else → M1**.

**Clause accounting.** Rev9 carried RFC3-1 … RFC3-32 plus four lettered
sub-clauses (RFC3-15(a), RFC3-16(a), RFC3-16(b), RFC3-17(a)) = 36 clause
identities. Rev10 carries the same 36 **plus one new lettered sub-clause,
RFC3-16(c)** = 37, verified present exactly once across the package union with
no clause appearing in both modules. **No clause was merged, retired,
renumbered, or dropped; the RFC3-1 … RFC3-32 range is closed with no gaps.**
Six §8 questions keep their original numbers (q1, q2 in M1; q4 in M2; q3, q5,
q6 answered and moved to history — q3 is *not* renumbered to q1, etc.).
Violation cases keep package-wide numbering 1–14, so each module's list is
non-contiguous; case 9 is the one case split by owning clause (cache/local
limbs → M1 under RFC3-20/21; challenge-admission-record limb → M2 under
RFC3-17(a)).

Rev9 `*(History: …)*` parentheticals extracted: 12 (RFC3-1, RFC3-2 ×2,
RFC3-7, RFC3-14, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-17(a),
RFC3-19, RFC3-30). All are in the history file verbatim.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC3-1 | retained with wording sharpened |  M1 (manifests-and-namespace) | YAML-dialect conformance rule kept verbatim; rev7-review-9 provenance parenthetical moved to history. |
| RFC3-2 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Four write-authority classes, the `kernel-recorded` definition and the minting-trigger rule kept in full; the [Inferred] "why the three original classes did not fit" rationale moved to history. |
| RFC3-3 | retained unchanged |  M1 (manifests-and-namespace) | Direct-write containment; no prose to compress without touching the rule. |
| RFC3-4 | retained with wording sharpened |  M1 (manifests-and-namespace) | Location-is-designation rule unchanged; the rejected field-value alternative reduced to a one-sentence in-place pointer (full text in history §6.2) because RFC3-16(a) reuses its reasoning. |
| RFC3-5 | retained unchanged |  M1 (manifests-and-namespace) | Closed field-set table copied, not paraphrased. |
| RFC3-6 | retained unchanged |  M1 (manifests-and-namespace) | Repository-entry identity and the not-observed → Unknown rule. |
| RFC3-7 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Both consent kinds and the one-record-per-(Project, provider) rule kept verbatim; owner decision **B8** now cited inline in the clause instead of in a History parenthetical; the AS-R10 amendment narrative moved to history. |
| RFC3-8 | retained unchanged |  M1 (manifests-and-namespace) | Revocation/withdrawal semantics: claim-value, rendering, and enforcement timings all preserved. |
| RFC3-9 | retained unchanged |  M1 (manifests-and-namespace) | Drafting and repair; never-auto-repair rule intact. |
| RFC3-10 | retained with wording sharpened |  M1 (manifests-and-namespace) | VIS-6 exception (a) classification and its [Inferred] justification kept; wording tightened only. |
| RFC3-11 | retained unchanged |  M1 (manifests-and-namespace) | Closed SDR-29 field list. |
| RFC3-12 | retained with wording sharpened |  M1 (manifests-and-namespace) | SDR-30 non-authority rule and derived-portfolio rule unchanged; one clause tightened. |
| RFC3-13 | retained unchanged |  M1 (manifests-and-namespace) | References-never-mints rule and Unknown rendering. |
| RFC3-14 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Asymmetric-relation bullets and the whole `depends-on` collision consequence (RFC1-25(b) elevated to a tested invariant) kept at full strength; owner decision **B20** cited inline; the "a draft had renamed it to `relies-on-project`" amendment parenthetical moved to history. |
| RFC3-15 | retained unchanged |  M2 (governance-homes) | Five-category table and the six-name validator rule copied, not paraphrased. |
| RFC3-15(a) | retained with wording sharpened |  M2 (governance-homes) + history | B19 attribution, the durability argument and the "widen explicitly, never stretch 'exclusively'" precedent kept; the pre-B19 problem statement moved to history. |
| RFC3-16 | retained with wording sharpened |  M2 (governance-homes) + history | **Directive §2 / OD-R10-5 repair.** Closed lifecycle table copied verbatim; the effective-status text now reads status *from the owner-act record* whose verification state is two-valued per RFC3-16(c); the no-record → effectively-unadopted rule and the acceptance-never-edits rule are unchanged. Rev8-rework History parenthetical moved to history. |
| RFC3-16(a) | retained unchanged |  M2 (governance-homes) + history | Predicate, four limbs, the [Inferred] fourth-limb reading rule, the non-exhaustive example list, the untrusted-tree/SEC-3-extension premise and the "mechanism class — chosen, not open" (A1) paragraph all preserved at identical strength, including "owner-held key or attestation custody is not an open implementation alternative … requires a later owner decision". Only the AS-R1 origin parenthetical moved to history. |
| RFC3-16(b) | retained unchanged |  M2 (governance-homes) + history | The nine binding items, the Bootstrap-correlation paragraph, "Effect when the predicate fails" and "One predicate, one home" all retained; the gate list compressed to bare clause IDs with its "tracks the gates; does not bound them" rule intact. Provenance parenthetical (directive item B2, **not** owner decision B2) moved to history. |
| **RFC3-16(c)** | **new at rev10 — directive §2 repair** |  M2 (governance-homes) | Names the two provenance states — *owner-adopted (bootstrap act)* vs *Syzygy-verified (effective act)* — so RFC 0003, the acceptance record and other artifacts can cite them instead of conflating them (adversarial finding F1). Lettered so the RFC3-1..RFC3-32 range stays closed. Weakens nothing: it re-states "git commits or tags alone are never sufficient" at preserved strength and defers to RFC3-16(a)'s failure effects. |
| RFC3-17 | retained unchanged |  M2 (governance-homes) | `declarations/` reservation and its owner-sign-off install gate. |
| RFC3-17(a) | retained with wording sharpened |  M2 (governance-homes) + history | Home, `kernel-recorded` authority, the no-`governance/challenges/` prohibition and every "Consequences that bind" rule kept; the long "Why `records/` and nothing else" reasoning compressed in place (each exclusion still named) with the full text in history. B19 rewrite parenthetical moved to history. |
| RFC3-18 | retained unchanged |  M1 (manifests-and-namespace) | Surface-namespace class rule. |
| RFC3-19 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | The pin-the-warranted-intent-revision schema obligation kept; the resolved RFC1-29 defect-handoff narrative (and its §5 companion paragraph) moved to history. |
| RFC3-20 | retained unchanged |  M1 (manifests-and-namespace) | `cache/` deletion-safety invariant and the observation-records-are-not-cache rule. |
| RFC3-21 | retained unchanged |  M1 (manifests-and-namespace) | `local/` presentation-state rule and the promotion-only path to authority. |
| RFC3-22 | retained unchanged |  M1 (manifests-and-namespace) | Version stamps as snapshot inputs. |
| RFC3-23 | retained unchanged |  M1 (manifests-and-namespace) | Identity-preserving migration list; semantic-change escalation. |
| RFC3-24 | retained unchanged |  M1 (manifests-and-namespace) | Explicit, reviewed, revertable migration; CC-REV-1 class 5. |
| RFC3-25 | retained unchanged |  M1 (manifests-and-namespace) | Forward/backward behavior; no silent downgrade. |
| RFC3-26 | retained unchanged |  M1 (manifests-and-namespace) | `openspec/**` outside Syzygy's migration authority. |
| RFC3-27 | retained unchanged |  M1 (manifests-and-namespace) | What Syzygy reads from `openspec/**`; adapter-vs-contract split. |
| RFC3-28 | retained unchanged |  M1 (manifests-and-namespace) | Spec anchors; degrade-never-guess; the [Unknown] identity-survival label preserved. |
| RFC3-29 | retained unchanged |  M1 (manifests-and-namespace) | One plane per repository; no directory-scoped sub-roots. |
| RFC3-30 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Per-pair role/consent rule, read-only observation of B's plane, and the whole observing-project-governs-policy paragraph (including its RFC3-16(a) dependency and the [Inferred] compromised-B argument) kept; AS-R7 parenthetical moved to history. |
| RFC3-31 | retained unchanged |  M1 (manifests-and-namespace) | Composition by declaration; derived recursion; cycle rendering. |
| RFC3-32 | retained with wording sharpened |  M1 (manifests-and-namespace) | Parent prohibitions and the RFC6-17 full-composition disclosure obligation kept whole; the laundering example tightened by one sentence. |

## §8 question rows

| Question | Outcome | Target | Note |
|---|---|---|---|
| q1 (monorepo subprojects, RFC3-29) | open — retained | M1 §7 | Foreclosure of many governed projects in one repository still needs the owner's word; unaffected by compaction or the split. |
| q2 (workspace manifest classification, RFC3-10) | open — retained | M1 §7 | VIS-6 exception (a) rebuildability trade still open. |
| q3 (egress consent granularity, RFC3-7) | answered — moved to history | history §8 | B8: one record per (project, provider); ruling carried inline in RFC3-7 (M1). |
| q4 (`declarations/` category, RFC3-17) | open — retained | M2 §5 | B19 settled only the challenge half; drafted default (reservation outside the constitutional five) stands, reversible by amendment. |
| q5 (owner-act provenance predicate, RFC3-16(a)) | answered — moved to history | history §8 | A1/A9: ceremony + independent audit trail; the A9 interim posture is what RFC3-16(c) now names as state (1). |
| q6 (governance home for challenges, RFC3-17(a)) | answered — moved to history | history §8 | B19: `records/` + `kernel-recorded`; carried in RFC3-15/15(a)/17(a) (M2). |

## Preservation checks run

All sweeps below were executed against the **package union** (M1 + M2
concatenated), re-run after the split; the pre-split single file was deleted
only once they passed.

- **Clause identities.** 37 clause openers found in the union — RFC3-1…RFC3-32
  plus RFC3-15(a), RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-17(a) — with the
  intersection of the two modules' clause sets **empty**: no clause appears
  twice, none is missing, none renumbered.
- **Owner decisions and identifiers — swept, not assumed.** All 23 decision
  and provenance tokens appearing anywhere in the rev9 source (A1, A9, B2 —
  the directive item, not the owner decision —, B8, B19, B20, AS-R1, AS-R7,
  AS-R8, AS-R10, S6, CC-REV-1, FD-034, OQ-010, T15, SDR-4, SDR-7, SDR-8,
  SDR-10, SDR-28, SDR-29, SDR-30, SDR-32) were enumerated from the frozen
  source and each confirmed present in the package, README, or history.
  **Zero missing.** Separately, all 16 tokens carried by the pre-split single
  file were confirmed present in the package union alone — **the split lost
  none**. (D1/D2 and CT-* never appear in RFC 0003.)
- **Cross-RFC citations — swept twice.** 90 unique `RFCn-m` citations in rev9;
  89 survive in the active contract. The two that left — `RFC5-6` and
  `RFC4-16(2)`, both occurring only inside §6.3 and the answered §8 q5 — are
  preserved verbatim in history. The only citation with no rev9 counterpart is
  `RFC3-16(c)` itself. Across the split: single file 89 unique, package union
  89 unique, **zero lost and zero added**.
- **Security premises.** The untrusted-tree premise, the **[Inferred] SEC-3
  extension to workers' *commits*** (a standing owner-attention item), VIS-7's
  trust floor, the RFC5-25 outside-the-tree location constraint and the
  compromised-B nearest-plane argument all retain their reasoning, not only
  their conclusions. The first three live in M2 (RFC3-16(a)); the last in M1
  (RFC3-30), which cites RFC3-16(a) rather than restating it.
- **Epistemic labels.** rev9, the pre-split single file, and the package union
  each carry 12 `[Inferred]`, 4 `[Observed]`, 1 `[Unknown]` — identical across
  the split. Versus rev9 the composition differs by exactly two entries:
  RFC3-2's `[Inferred]` class-fit rationale moved to history, and RFC3-16(c)
  added its own label line. No retained claim lost its label.
- **No `_bootstrap/` paths remain in active normative text** (checked); the
  two rev9 occurrences (RFC3-16(b)'s directive reference and §3.9's seed-file
  citation) are in history or reduced to an unpathed `[Observed]`.
- **Verbatim blocks — located after the split.** RFC3-5's field table in M1;
  RFC3-15's category table, RFC3-16's lifecycle table, RFC3-16(b)'s nine items
  and RFC3-16(a)'s example list in M2. Copied, not paraphrased (990 words in
  total).
- **Violation cases.** All 13 rev9 cases retained; one new case (14) added for
  RFC3-16(c). Across the union the numbers 1–14 each appear once, except **9,
  which appears in both modules by design** — its limbs were divided by owning
  clause and each module states where the other limbs live.
