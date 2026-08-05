# RFC-0009 — clause migration rows (rev9 → rev10 compacted package)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0009-orrery-map-surface.md` (frozen,
19,269 words, RFC9-1..RFC9-52 plus eight lettered sub-clauses).
Target: the indexed contract package `final-prespec/rfcs/RFC-0009/`
(**owner direction OD-R10-6**). History: `final-prespec/history/RFC-0009-history.md`.

**Package outcome summary.** Every clause is **retained** — none merged, none
retired, none routed out of the active path, no renumbering, no gaps. 52 numbered
clauses + 8 lettered sub-clauses = 60 clause rows, plus 10 §8 question rows =
**70 rows**. Ranges are contiguous and disjoint: RFC9-1..23 → module 1,
RFC9-24..45 → module 2, RFC9-46..52 → module 3. Each lettered sub-clause lives
with its parent integer.

Target column names the owning **module file** inside `final-prespec/rfcs/RFC-0009/`.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC9-1 | retained with wording sharpened | `semantic-geography.md` | Section cross-refs converted to clause IDs (§3.10 → RFC9-41); rule unchanged |
| RFC9-2 | retained unchanged | `semantic-geography.md` | Semantics-only boundary; copied verbatim |
| RFC9-3 | retained with wording sharpened | `semantic-geography.md` | Drawer-invariant reasoning compressed; rejected kernel-route alternative to history §6 |
| RFC9-4 | retained unchanged | `semantic-geography.md` | Anchoring rule and spatial hierarchy copied verbatim |
| RFC9-5 | retained with wording sharpened | `semantic-geography.md` | Closed may/may-never lists copied verbatim; §3.11 → RFC9-44 |
| RFC9-6 | retained unchanged | `semantic-geography.md` | Identity-continuity rules copied verbatim |
| RFC9-7 | retained unchanged | `semantic-geography.md` | Unmapped-code rule copied verbatim (§3.11 → RFC9-44) |
| RFC9-8 | retained with wording sharpened | `semantic-geography.md` | Portfolio append-stability justification compressed; obligation unchanged |
| RFC9-8(a) | retained with wording sharpened | `semantic-geography.md` | ML-R15 problem narrative to history; workspace-scope machinery and two limits retained |
| RFC9-9 | retained with wording sharpened | `semantic-geography.md` | Two readings, measurement bar, best-effort/not-honored rule verbatim; B12(a)/B20 cites kept, narrative to history |
| RFC9-9(a) | retained with wording sharpened | `semantic-geography.md` | Four binding parts retained in full; ML-R3 finding narrative to history |
| RFC9-9(b) | retained with wording sharpened | `semantic-geography.md` | Six-facet registry entry and closed three-value domain copied; ML-R5 narrative to history |
| RFC9-10 | retained with wording sharpened | `semantic-geography.md` | Obligations (a)–(d) and owner decision B21 with its recorded cost retained; §8 q10 pointer moved to history |
| RFC9-11 | retained unchanged | `semantic-geography.md` | Masquerade boundary copied verbatim |
| RFC9-12 | retained unchanged | `semantic-geography.md` | Lens-switch invariance copied verbatim |
| RFC9-13 | retained unchanged | `semantic-geography.md` | Personal-state rule copied verbatim |
| RFC9-13(a) | retained with wording sharpened | `semantic-geography.md` | Three obligations retained verbatim; "why contract material" narrative to history |
| RFC9-14 | retained unchanged | `semantic-geography.md` | Layout input tuple copied verbatim, including the block quote |
| RFC9-14(a) | retained with wording sharpened | `semantic-geography.md` | Three input definitions and the baseline-recording obligation retained; ML-R1 narrative to history |
| RFC9-15 | retained with wording sharpened | `semantic-geography.md` | Append-stability obligation verbatim; §3.12 → RFC9-47 |
| RFC9-15(b) | retained with wording sharpened | `semantic-geography.md` | Four binding parts and the mandatory partition retained in full; ML-R1/R4/R14 narratives to history |
| RFC9-16 | retained unchanged | `semantic-geography.md` | Closed relocation-trigger set (a)–(d) copied verbatim |
| RFC9-16(d) | retained with wording sharpened | `semantic-geography.md` | Owner gate A3, the narrow carve-out and the layout-equivalence-check correction retained; ML-R2 failure case to history |
| RFC9-17 | retained unchanged | `semantic-geography.md` | Forbidden-churn list and unbounded-reservation rule copied verbatim |
| RFC9-18 | retained with wording sharpened | `semantic-geography.md` | RFC3-16(a) honoring rule verbatim; §3.4 → §4; cross-module pointer to RFC9-26 added |
| RFC9-19 | retained with wording sharpened | `semantic-geography.md` | Three placement mechanisms copied verbatim; §3.3 → §3; no-clone aside compressed |
| RFC9-20 | retained with wording sharpened | `semantic-geography.md` | Contradiction treatment and two-`placed_in` general case retained; ML-R8 narrative and §6 alternative to history |
| RFC9-21 | retained with wording sharpened | `semantic-geography.md` | Scene-scoped disclosure trigger retained verbatim; illustrative aside compressed |
| RFC9-22 | retained unchanged | `semantic-geography.md` | Repository-overlay rule copied verbatim |
| RFC9-23 | retained unchanged | `semantic-geography.md` | Authority-overlay list copied verbatim; SEC-2/3/5 premises intact |
| RFC9-24 | retained unchanged | `visual-grammar-and-lenses.md` | Reserved state palette — closed vocabulary copied verbatim |
| RFC9-25 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Saturation reservation verbatim; deferral pointer §7 dropped (now module §7) |
| RFC9-26 | retained unchanged | `visual-grammar-and-lenses.md` | Seven declared items, fail-closed rule and forged-entry security reasoning copied verbatim |
| RFC9-27 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Three-scope Unknown rule and earned-emptiness rule verbatim; §3.10/§3.12 refs normalized |
| RFC9-28 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Per-lens height rule verbatim; §6 alternative pointer added, alternative text to history |
| RFC9-29 | retained unchanged | `visual-grammar-and-lenses.md` | SEC-5 granularity bound and its shape-disclosure reasoning copied verbatim |
| RFC9-30 | retained unchanged | `visual-grammar-and-lenses.md` | Inference/challenge/consent degradation copied verbatim |
| RFC9-31 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Lens may/may-never lists and the overlay magnitude bar verbatim; closing justification compressed |
| RFC9-32 | retained with wording sharpened | `visual-grammar-and-lenses.md` | V0 lens set and both work-state fields (closed vocabularies) copied; one staging clause compressed |
| RFC9-33 | retained unchanged | `visual-grammar-and-lenses.md` | Lens staging and SEC-3 runtime gate copied verbatim |
| RFC9-34 | retained unchanged | `visual-grammar-and-lenses.md` | No-synthesis rule copied verbatim |
| RFC9-35 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Same-increment rule and the promotion predicate (B12(c)/B17) retained; §3.12 → RFC9-46; provenance parenthetical to history |
| RFC9-36 | retained unchanged | `visual-grammar-and-lenses.md` | City/Factory profile rule copied verbatim |
| RFC9-37 | retained unchanged | `visual-grammar-and-lenses.md` | Factory honesty obligations copied verbatim |
| RFC9-38 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Evaluation-naming and RFC9-41 subordination verbatim; resolved defect 3 folded in as an inline note |
| RFC9-39 | retained with wording sharpened | `visual-grammar-and-lenses.md` | `Base` context rule and absence-as-obligation retained verbatim; derivation narrative compressed |
| RFC9-40 | retained unchanged | `visual-grammar-and-lenses.md` | Proposed-scene rules copied verbatim |
| RFC9-41 | retained with wording sharpened | `visual-grammar-and-lenses.md` | D1 scope and the non-binding candidate bundle retained verbatim; rev7 rewrite parenthetical to history |
| RFC9-42 | retained unchanged | `visual-grammar-and-lenses.md` | LOD epistemic invariance copied verbatim |
| RFC9-43 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Full equivalence tuple, six tiers and three sibling states copied verbatim; second laundering example to history |
| RFC9-44 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Never-disappears rule and identity-vs-arrangement distinction verbatim; §6 alternative to history |
| RFC9-45 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Three artifacts, B12(b) default and the fail-closed `verdict-unlawful` protocol retained in full; two parentheticals to history |
| RFC9-46 | retained with wording sharpened | `interaction-parity-and-release.md` | Equivalence tuple, the two added fields and the maintenance note retained verbatim; ML-R6 attribution to history |
| RFC9-47 | retained with wording sharpened | `interaction-parity-and-release.md` | Full release-gate enumeration copied (closed checklist); ML-R9/R6 attribution compressed |
| RFC9-47(a) | retained with wording sharpened | `interaction-parity-and-release.md` | Both self-maintenance obligations verbatim; directive-item provenance to history; cross-module scope note added |
| RFC9-48 | retained unchanged | `interaction-parity-and-release.md` | Non-visual parity list copied verbatim |
| RFC9-49 | retained unchanged | `interaction-parity-and-release.md` | Declared-scope-narrowing rule and RFC6-13 divergence reasoning copied verbatim |
| RFC9-50 | retained unchanged | `interaction-parity-and-release.md` | No-ambient-motion rule copied verbatim |
| RFC9-51 | retained unchanged | `interaction-parity-and-release.md` | Illumination-as-interaction-state copied verbatim |
| RFC9-52 | retained unchanged | `interaction-parity-and-release.md` | Binding phase rule copied verbatim at identical strength; shape-parallel with RFC6-28/RFC7-38/RFC8-32 |

## §8 owner questions

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision A7; one-line stub retained so numbering never shifts |
| q2 | open — retained | `semantic-geography.md` §10 | Undeclared shared-component placement (RFC9-20); the package's only open numbered question |
| q3 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Adopted doctrine amendment D1, in part; residual candidate-bundle approval lives as live text in RFC9-41 |
| q4 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Owner decisions B12(c)/B17; the promotion predicate is clause text at RFC9-35 |
| q5 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision A6; see also the open follow-on recorded below |
| q6 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision A3, narrowed; the gate is clause text at RFC9-16(d) |
| q7 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision B12(a); consequences are RFC9-9, RFC9-9(a), RFC9-9(b), RFC9-15(b) |
| q8 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Owner decision B12(b); the three-artifact gate is clause text at RFC9-45 |
| q9 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Owner decisions B12(c)/B17, with q4 and the profile-relation limb |
| q10 | answered — moved to history | `interaction-parity-and-release.md` §8 (stub) | Owner decision B21; surviving contract text at RFC9-10(c) |

**One open item beyond the numbered set** (not a rev9 clause or question, so it
carries no row above). The rev10 RFC-0001 pass established that **owner decision
A6** closed RFC-0001 §8 q6's kernel-minting half but did not address whether
**RFC9-9's legend and edge-channel rules need a pass now that a kernel-level
declared dependency relation exists**, nor the underlying *who may add a profile
relation, and under what gate* question. No normative change was made on this
pass (owner-scoped; home is RFC1-7/RFC1-26). Carried as a visible open item in
`semantic-geography.md` §10, indexed in the package README, recorded in history
§8, and flagged to the lead for the open-question triage.

## Non-clause material

| Rev9 section | Outcome | Target |
|---|---|---|
| §0 Reader's summary (non-normative) | moved to rationale/history | Distributed to README reader map + each module §0; rev9 thesis verbatim in history |
| §1 Summary | moved to rationale/history | Superseded by README scope + clause map |
| §2 Motivation and doctrine grounding | moved to rationale/history | [Observed] grounding retained verbatim in history; [Inferred] thesis compacted into README |
| §4 Violation cases 1, 2, 3, 3a, 4, 5 | retained unchanged | `semantic-geography.md` §7 |
| §4 Violation cases 6, 7, 8, 9, 10 | retained unchanged | `visual-grammar-and-lenses.md` §5 |
| §4 Violation case 11 | retained unchanged | `interaction-parity-and-release.md` §5 |
| §5 Integration (relies-on lists) | retained with wording sharpened | Split module-scoped; package-spanning items to README |
| §5 defect 1 (A7/A6) | retained with wording sharpened | `semantic-geography.md` §8 — owner decisions and the binding drafting restraint retained; full trail to history §5 |
| §5 defects 2, 3, 4, 5 | moved to rationale/history | All resolved upstream 2026-08-01; one-line status in the owning module, trail in history §5 |
| §6 Alternatives considered | moved to rationale/history | history §6; four load-bearing residues cited from RFC9-3, RFC9-20, RFC9-28, RFC9-44 |
| §7 Deliberately deferred | retained with wording sharpened | Split module-scoped (§9/§7/§7); rev9 text in full in history §7 |
| End-of-contract marker | retained with wording sharpened | Per-module end markers + README's closed-range statement |
