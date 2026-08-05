# SEMANTIC-EQUIVALENCE REVIEW — rev9 → rev10 final pre-specification package

**Reviewer role:** semantic-equivalence (directive §13.1), fresh context, no authoring input.
**Question:** does the compacted rev10 corpus preserve the full semantic force of rev9 — every clause accounted for, no founder decision or accepted fix lost, no weakened Unknown/evidence/authority rule?

**VERDICT: EXCEPTIONS** — seven, located below. **No lost obligation, no lost founder decision, and no weakened Unknown/evidence rule was found.** Every exception is an *accounting or recording* defect, not a semantic loss. E1 is the only one I would hold the owner act for.

---

## 1. Fixture results (F-EQ-1 … F-EQ-8)

| Fixture | Substance | Fixture-as-written |
|---|---|---|
| F-EQ-1 RFC2-1 eleven inputs | **PASS** | defective (see E4) |
| F-EQ-2 RFC3-16(b) nine items | **PASS** | defective (see E4) |
| F-EQ-3 `supersedes` closed-pair row | **PASS** | clean |
| F-EQ-4 RFC8-12/13 states + tables | **PASS** | clean |
| F-EQ-5 RFC6-5 nine outcomes | **PASS** | clean |
| F-EQ-6 RFC5-25 location constraint | **PASS** | clean |
| F-EQ-7 RFC8-25 deliberate resolution | **PASS** | clean |
| F-EQ-8 verifier + decision census | **PASS** (verifier) | defective (see E3) |

Evidence per fixture:

- **F-EQ-1** [Observed] Items 1–11 of RFC2-1 are byte-identical between `history/rev9-rfcs/RFC-0002-…:89–130` and `rfcs/RFC-0002/snapshot-and-evaluation-core.md:68–109`. The only deltas: item 11's `*(History: added at the rev8 final review…)*` parenthetical removed (preserved verbatim at `history/RFC-0002-history.md:18`), and an **added** stricter note — "item numbers are load-bearing and cited elsewhere — never renumber". No renumbering.
- **F-EQ-2** [Observed] Nine items, wording identical modulo re-wrapping. Item 9 retains "always, under the A1 mechanism class bound at RFC3-16(a)" and the RFC5-25 location constraint. The Bootstrap-correlation and Effect-when-the-predicate-fails paragraphs are preserved verbatim.
- **F-EQ-3** [Observed] The `supersedes` row is byte-identical (`rfcs/RFC-0001-…:493` vs `history/rev9-rfcs/RFC-0001-…:511`).
- **F-EQ-4** [Observed] All thirteen state tokens present; RFC8-13's three derivation tables are **19/19 rows byte-identical**.
- **F-EQ-5** [Observed] 11 rows each side, `diff` clean — byte-identical.
- **F-EQ-6** [Observed] Present at binding strength in both homes (`RFC-0005/admission-and-boundary.md:303`, `RFC-0003/governance-homes-and-owner-acts.md:227`).
- **F-EQ-7** [Observed] "operative limit" absent from all of `rfcs/RFC-0008/`; present at `history/rev9-rfcs/RFC-0008-…:626` and at `history/RFC-0008-history.md:248,253` with the B13-supersession reasoning. Confirmed deliberate and strictly-stricter (see §4 ruling 3).
- **F-EQ-8** [Observed] `verify_final_prespec.py` → **PASS — all checks clean** (322 clauses, 32 modules, two justified notes). Decision census: B13 5, A8 5, B19 9, A1 44, A5 15, A9 4, B9 7, D1 12, CC-TEST-2 1 — and **D2 0** (see E3).

**Independent decision-ID census beyond the fixture** [Observed]: I extracted every `[ABCD]\d{1,2}` token from rev9 and from the active corpus. **Zero IDs present in rev9 are absent from rev10.** No founder decision reference was dropped.

---

## 2. Clause-migration matrix completeness (my own enumeration, not the workers')

[Observed] Parsing `04-CLAUSE-MIGRATION-MATRIX.md` programmatically:

- **328 distinct clause-id rows.** All 294 rev9 base clauses (RFC1-1..32, RFC2-1..25, RFC3-1..32, RFC4-1..29, RFC5-1..26, RFC6-1..28, RFC7-1..38, RFC8-1..32, RFC9-1..52) have a row — **zero missing**.
- I independently extracted rev9's clause definitions from the frozen files: exactly 294 base clauses (RFC9 max = 52, no gaps) and **21 lettered sub-clauses**. All 21 have matrix rows. The extra 12 lettered entries (RFC7-2(a–c), RFC7-9(a–c), RFC8-2(a–c), RFC8-8(a–c)) are **limb rows**, consistent with rev9's own statement at `RFC-0008-…:1046` that "their parent clauses (e.g. RFC8-2(a)–(c)) are parts of those clauses". Correctly handled.
- **Outcome census:** 176 `retained unchanged`, 151 `retained with wording sharpened`, 2 `new at rev10` (RFC3-16(c), rowed twice — benign, the second row cross-references the first). **Zero merged, zero retired, zero moved-to-history, zero routed out.** The matrix's global tally is accurate.
- **Active-corpus completeness:** every one of the 294 base clauses and all 21 rev9 sub-clauses is *defined* (`**RFCn-m`) in `rfcs/`. RFC10 = 16 clauses, RFC11 = 12.

**Spot-verification, far beyond the 25 required:**

- **Target column, 214 rows** whose target cell names an explicit `.md`: **zero mismatches** — every clause is defined in the module the matrix names. (103 further rows use section refs for the single-file RFCs; those clauses were confirmed present by the completeness census.)
- **"Retained unchanged" rows, all 176 machine-diffed** against rev9 with History parentheticals stripped. Manual diffs of nine flagged candidates (RFC1-7, RFC2-11, RFC2-14, RFC2-22, RFC4-9, RFC7-28, RFC8-11, RFC8-20, RFC9-23) show: RFC1-7 **byte-identical**; the rest differ only by re-wrapping, a `---` separator, or a reference re-point (`§7` → `` `README.md` §7``; "every rule here" → "every rule in this package" — correct after the split). One phrase touch: RFC2-11 "the research's SHA-binding rule" → "the SHA-binding rule".
- **RFC3-16(a)** — the highest-stakes "retained unchanged" row — diffed in full: all four predicate limbs, the `[Inferred]` fourth-limb reading rule, the "predicate is the scope; the list is not" rule, the non-exhaustive example list, the SEC-3-extension premise, and the A1 "chosen, not open" paragraph including "owner-held key or attestation custody is not an open implementation alternative … requires a later owner decision" — **all preserved at identical strength**. Only re-wrapping and one dereferenced `§6`.

---

## 3. My own obligation hunt (all nine RFCs, not the four required)

Method: extracted every sentence containing `must|never|only|forbidden|prohibit*|may not|shall|required|refus*|cannot` from each rev9 file (**~1,150 sentences**), then fuzzy-matched each against the union of that RFC's active modules **and** its history file, flagging anything below 0.72 similarity.

Unmatched candidates: RFC1 9, RFC2 19, RFC3 15, RFC4 12, RFC5 11, RFC6 9, RFC7 15, RFC8 10, RFC9 28. **I hand-triaged every high-signal candidate.** Results:

- **Every one traced to** (a) matcher artifacts from re-wrapping, (b) §1/§2 executive-summary prose compressed while the clause itself retains the obligation verbatim, or (c) a matrix-documented Tier-2 move.
- Directly confirmed present after being flagged: RFC1-18(a) "Declared scope is a typed reference, never a string" (`RFC-0001:315`); RFC3-3's direct-write containment incl. "**inoperative** — Syzygy must not honor it" (`manifests-and-namespace.md`); RFC3-23 identity-preserving migrations; RFC2 degradation-only ("a later evaluation over the same snapshot **may only degrade**"); "only gate-backed Observed evidence may support a positive status claim"; RFC4 "the adapter must not inherit a client's drift"; RFC7-3 "Nothing cites the rendering" (`narrative-contract.md:97`); RFC9-13(a) stale-layout personal state, **verbatim**.
- **Zero unaccounted obligation losses.** The RFC-0002 pass's own published figure (23 → 22 unmatched, with two named restorations) is consistent with what I measured independently.

**Epistemic-label census** [Observed]: rev9 253 `[Observed]/[Inferred]/[Unknown]` labels → rev10 **302** across active + history. No label class lost anywhere; net increase.

---

## 4. The six substantive rulings

| # | Ruling | Faithful? | Additive / stricter? | Honestly recorded? |
|---|---|---|---|---|
| 1 | RFC3-16(c) two-state model | yes | additive, but see **E1** | **partially — E1** |
| 2 | RFC5-3/5-5 sharpening + q1 scope ruling | yes | strictly stricter | yes |
| 3 | RFC8-25 B13-supersession | yes | strictly stricter | yes |
| 4 | RFC2-24 "#10 not split" | yes | neutral/stricter | yes (minor — **E5**) |
| 5 | RFC2-13 restoration | yes | restoration | yes |
| 6 | RFC-0001 structure | yes | neutral | yes |

**Ruling 2 — RFC5-3/5-5.** [Observed] Both rev9 clauses are preserved verbatim; the additions are new blocks explicitly labelled *(rev10 scoping, directive §2 / OD-R10-5)*. RFC5-3 closes the class set ("no later contract may introduce one"; "A contract needing a further client class would be **amending this clause, not extending it**"). RFC5-5 names CLI/MCP/scripts/fleet workers machine-class "**without exception**" and denies admission by co-location, packaging, or first-party status. Purely restrictive. The **§8 q1 scope ruling** is exemplary: it opens by stating "**this ruling does not answer the question, and the author does not select a mechanism**", leaves q1 **OPEN**, and classifies it "must close before V0 implementation; it does not block specification." No question was silently closed.

**Ruling 3 — RFC8-25.** [Observed] rev9's closing sentence "Until the bound is declared, the coverage test above is the operative limit" was a genuine internal tension with B13's fail-closed rule ("Where no threshold is declared, **no mutation inherits**"): the retired sentence implied inheritance still occurs, gated only by coverage. Retiring it is **strictly stricter**. Preserved verbatim in `history/RFC-0008-history.md:248` with the supersession reasoning. All other RFC8-25 obligations — the warrant-coverage test, "A warrant is never extended by execution-side prose", the `asserted-by-worker` tier fix — are intact.

**Ruling 4 — RFC2-24 "#10 not split".** [Observed] rev9's recorded A5 answer says only "The list grows to **twelve**: #12 added, #11 retained." It does not name the #10 split. The inference is sound (a list closed at twelve with #10 intact entails no split) and — importantly — **it is disclosed**: `history/RFC-0002-history.md:221–225` states "A5 does not name the … split explicitly … Flagged in the compaction report as the one inference drawn from an answer's scope", and the active clause at `rendering-vocabularies.md:229` points the reader to that note. Honestly recorded. (One dangling pointer — E5.)

**Ruling 5 — RFC2-13.** [Observed] "the act itself is not subject to the VIS-7 identity test" is present at `challenge-lifecycle.md:103`, with both senses (the deterministic *state* vs the judgment *act*, "two admitters can differ", "no re-computation adjudicates between them") intact. Restoration confirmed.

**Ruling 6 — RFC-0001.** [Observed] rev9 §0+§1+§2 merged into active §1; §3–§8 numbering preserved; the file has no §2 by design. B20 now sits adjacent to the spelling decision (`:508`). As described.

---

## 5. Closed vocabularies — six-plus verified, copied not paraphrased

Two independent corpus-wide sweeps rather than spot checks:

**(a) Table-row verbatim sweep, all nine RFCs.** Of 207 rev9 table rows, **14 are not byte-present** in active or history. All 14 audited:
- **RFC2-24 (6 rows)** — the twelve-reason closed vocabulary. Reason name, condition, and resolution route are **byte-identical**; only Tier-2 per-cell amendment narratives were stripped from the resolution cell (`*Renamed*…`, `*Added at acceptance by owner decision (A5).*…`). Three of four are in history verbatim; the fourth (#10-vs-#2 diagnosis) is **preserved as clause prose** at `rendering-vocabularies.md:128` and in history.
- **RFC4-19 envelope (3 rows)** — normative cells byte-identical; only `[Observed: '04' §4]`-style source pointers shortened (see E7).
- **RFC-0007 (3 rows)** — only `§3.8`→`RFC7-28`, `§3.6`→`RFC7-20`, `§3.12`→`RFC7-36`. An improvement: clause refs survive splits, section refs don't.
- **RFC-0003 (1 row)** — `schema_version`: only `§3.7`→`§2.6`, correct for the new module.
- RFC-0001 **65/65 rows**, RFC-0005 **11/11**, RFC-0006 **10/10**, RFC-0008 **26/26** byte-identical. RFC-0009 has no markdown tables in rev9.

**(b) Backticked-token sweep, all nine RFCs** (catches RFC-0009's prose-form closed sets). 448 rev9 tokens; 13 flagged; **all 13 confirmed present** on inspection — e.g. RFC7-11(a)'s `anchored — target changed since authorship` (present, broken only across a line-wrap), RFC9-45's `verdict-unlawful` (`visual-grammar-and-lenses.md:517,524`), `ACCEPT FOUNDATIONAL RFCS` (`governance-homes:87`). The rest were path spellings or source-pointer fragments.

**Verified closed sets beyond the fixtures (≥6):** RFC1-5 entity table · RFC1-25 relation/four-sense tables · RFC2-24 twelve reasons · RFC2-25 tier vocabulary · RFC3-15 five categories + install gates · RFC4-19 envelope · RFC5-7 four mechanism classes · RFC7 content-class table · RFC9-45 judgment states. **Zero closed-vocabulary value losses corpus-wide.**

---

## 6. RFC3-16(c) against RFC3-16(a)/(b) as they stood in rev9

[Observed] **No contradiction, no weakening of (a) or (b).** RFC3-16(c) closes with an explicit non-derogation bullet — "Nothing here weakens RFC3-16(a): an authorization-bearing artifact resting on a state-(1) record has not satisfied the predicate, and RFC3-16(a)'s *Effect when the predicate fails* governs its dependent effects." It re-states "A git commit or tag alone is never sufficient for **either** state" at preserved strength, and its state-(2) definition reproduces (b)'s nine-item binding and the RFC5-25 location constraint. (a) and (b) are themselves verbatim-preserved (verified above). The correlation-upgrade bullet is consistent with (b)'s Bootstrap-correlation paragraph and with RFC3-16's acts-never-edit rule.

I also checked for downstream contradiction: the three remaining "verifiable owner-act provenance" assertions in the active corpus (`RFC-0002/snapshot-and-evaluation-core.md:201`, `RFC-0002/README.md:132`, `RFC-0003/governance-homes:282`) all concern authorization-bearing artifacts and remain consistent. RFC10-9 applies the two-state model correctly.

---

## Exceptions

**E1 — `04-CLAUSE-MIGRATION-MATRIX.md:337` and `:340`: a changed authority rule is recorded as unchanged. [Observed] — the one I would hold the act for.**

Rev9 `RFC-0003-…` RFC3-16 read:

> effective status … is determined by the existence of an **independently verifiable** owner-act record …
> - An artifact with **no verifiable** owner-act record has effective status **unadopted** … it **binds nothing, anchors nothing**, and renders unadopted everywhere.

Rev10 `governance-homes-and-owner-acts.md:120,149` reads:

> effective status … is determined by an **owner-act record** … That record's own verification state is **two-valued** …
> - An artifact with **no owner-act record at all** has effective status **unadopted** …

The trigger moved from "no *verifiable* record" to "no record *at all*". Under rev9's literal text, an uncorrelated bootstrap artifact — including this repo's adopted doctrine and these RFCs — bound nothing. Under rev10 it is state (1) and governs. **That is a real relaxation.** It is owner-directed (`01-REV9-ADVERSARIAL-FINDINGS.md`: "the human may govern development by it"), it is defensible, and it is *more* honest than rev9's self-contradictory pairing. It is **not** "unchanged."

The matrix nonetheless records: "the no-record → effectively-unadopted rule … **unchanged**" (`:337`) and, for RFC3-16(c), "**Weakens nothing.**" (`:340`). For Syzygy's own claims nothing weakened — that part is true and I verified it. But the semantic-preservation matrix is precisely the artifact whose job is to state such a change plainly, and it does not. **Why it blocks:** the owner signs the act on the strength of this matrix. Fix is one row's wording, not a corpus change.

**E2 — `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:74–80`: a load-bearing normative rule lives outside the contract corpus. [Observed] Non-blocking.**

The record asserts that on a state-(1) provenance record, artifacts consumed as **constraints** "bind at full strength — refusing to apply a constraint over uncorrelated provenance would widen, not narrow" while artifacts consumed as **authorizations** do not satisfy RFC3-16(a). The reasoning is sound and conservative. But I grepped all of `rfcs/`: **the constraint half appears nowhere.** RFC3-16(c) states only the authorization half; RFC10-9 likewise. If the distinction is what makes the acceptance honest, it belongs in RFC3-16(c), not only in the ceremony document — otherwise a later reader of the accepted contract cannot derive it. Doesn't block: it is strictly conservative and stated where the owner will read it.

**E3 — `fixtures/semantic-equivalence-fixtures.md:82`: F-EQ-8 fails as written. [Observed] Non-blocking.**

The grep includes `D2` and the pass condition is "every listed decision ID appears somewhere in the active corpus". **D2 appears 0 times in `rfcs/`** — and never did in rev9 either; it is the craft-and-care approval decision, living in `craft-and-care/*.md`. A reviewer running this fixture literally reports a false loss. Fix: drop `D2` or scope the check to include the craft cluster.

**E4 — `fixtures/…:13–19` and `:24–28`: F-EQ-1 and F-EQ-2 commands don't produce what their pass conditions describe. [Observed] Non-blocking.**

F-EQ-1's `grep -A40 'RFC2-1'` matches every later `RFC2-1 item n` citation, so the diff shows unrelated §8 material, not "differences only in … item 11". F-EQ-2's `sed` range starts at the module's front-matter mention of RFC3-16(b), returning **14**, not the nine the pass condition requires. Both substantive checks pass when run precisely (I did, above), but the fixtures are supposed to be re-runnable evidence for a fresh reviewer, and as written they produce misleading output.

**E5 — `history/RFC-0002-history.md:224`: dangling cross-reference. [Observed] Non-blocking.**

Claims the q1(b) inference is "Flagged in the compaction report as the one inference drawn from an answer's scope." `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` contains no occurrence of "inference" or "q1(b)". The ruling is honestly recorded *in history*; only the pointer is broken. Given that this is the corpus's single acknowledged inference-from-owner-answer, the owner-facing report is the one place it should appear.

**E6 — `08-OPEN-QUESTION-TRIAGE.md` summary: mis-tallied. [Observed] Non-blocking; secondary lane.**

Summary states "7 may remain open before OpenSpec; 13 must close before V0; **6** must close before Mission Control V1". Machine count of the table's 28 rows: **6** may-remain-open, 13 V0, **7** Mission Control V1. Two classes are transposed; the total happens to reconcile. The substantive check in *my* lane passes: exactly **21 rev9-origin open questions** are carried, all still open, none silently closed.

**E7 — Corpus-wide source-pointer attrition on `[Observed:]` labels. [Observed] Non-blocking observation.**

Rev9 carried 121 `[Observed: <source>]` citations; rev10's active corpus carries 92. **RFC-0004 accounts for most of it: 30 → 13.** The epistemic *labels* all survive (total labels rose 253 → 302), and `COMPACTION-CHARTER.md:32–33` requires only that the label survive — so this is charter-conforming. But `[Observed]` without its source is a weaker claim than `[Observed: '04' §4]`: a reader can no longer check what was observed. Worth a sentence in the compaction report rather than silence, since RFC-0004 is the evidence-adapter contract where provenance traceability matters most.

---

## Concrete risks even where I accept

1. **RFC3-16(c) is new and unreviewed by anyone but this pass.** [Inferred] It is the load-bearing clause of the whole acceptance ceremony, written during compaction, and it is the only clause in the corpus with no rev9 antecedent to diff against. Its non-derogation bullet is good, but "additive" here rests on judgment, not on a diff.
2. **The two-state model's human/machine split is asserted in three places with three scopes** — RFC3-16(c) (authorizations), RFC10-9 (envelopes), and the acceptance record (constraints + authorizations). [Observed] Only the third is complete. [Inferred] That is the shape of a rule that drifts.
3. **RFC-0001 remains a single 8,352-word file** above the ceiling. [Observed] The justification (dictionary-shaped, 23% verbatim vocabulary) is honest and I verified all 65 of its table rows are byte-identical — but it means the corpus's densest identity contract has no selective-loading benefit.
4. **`WORKER-REPORT-DIGEST.md:24` projects "≈67–70k words"; actual is 97,861.** [Observed] The digest is explicitly non-normative and `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` states the real figure honestly, band-miss and all. But the stale projection sits in a file reviewers are pointed at.

**Bottom line:** I found no lost clause, no lost obligation, no lost founder decision, no lost closed vocabulary, no silently-closed open question, and no weakened Unknown/evidence rule. The rev10 corpus is semantically faithful to rev9. What I found instead is that the *records about* the corpus overstate their own fidelity in one consequential place (E1) and mis-describe their own contents in five minor ones. Correct E1's row wording and E3/E4's fixtures, and this becomes an ACCEPT.
