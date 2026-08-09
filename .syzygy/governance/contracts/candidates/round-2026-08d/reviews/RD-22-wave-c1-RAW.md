# RD-22 — Wave C1 exact-package review (part 1/3)

**Review identifier:** RD-22 · **Date:** 2026-08-09 · **Baseline commit:** 771965c
**Subject:** Wave C1 — RFC-0011 module 1 (packet identity, provenance, memory) plus the package index
**Read from:** frozen clone `…/scratchpad/clone-771965c` only. The working tree was never read or written; the clone was never written.
**Excluded per charter and not read:** `C/round-2026-08d/`, `C/history/`, every `reviews/` directory, `_bootstrap/`.
**Position in ceremony:** fifth of six. Waves A, B, D1, D2 (RFC 0001–0010) taken as bound; C2, craft, topology taken as not bound.

---

## 1. Manifest verification

**Method.** All digests recomputed in Python (`hashlib.sha256` over file bytes), never transcribed, never read from a report. Population enumerated by `rglob`, not by assumption.

### 1.1 Row-by-row recomputation — `WAVE-C1-MANIFEST.txt`

| Manifest digest | Path | Recomputed | Result |
|---|---|---|---|
| `f09821debc2ee1946530a2f3b74075bfdc5347a91c8cbf72d76834781d441fa1` | `rfcs/RFC-0011/README.md` | identical | **OK** |
| `de61d66d043e1de509fbd8c31a525f27241e3e39624e384ab3141b7267159193` | `rfcs/RFC-0011/packet-identity-provenance-and-memory.md` | identical | **OK** |

2 rows; 2 verified; 0 mismatched; 0 missing. [Observed]

### 1.2 The manifest file's own sha256

```
a5d3ba1f22ad0ff5ff66485b1829e5b2f652a8c7678dcc96699eaca4ac5b2b4d   WAVE-C1-MANIFEST.txt
```

This is byte-identical to the argument quoted in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 row C1:
`ACCEPT FOUNDATIONAL WAVE C1: a5d3ba1f22ad0ff5ff66485b1829e5b2f652a8c7678dcc96699eaca4ac5b2b4d`. [Observed]

For the seam, recomputed as well: `WAVE-C2-MANIFEST.txt` own sha256 = `acd27bb8f9b7be76725057b4280e2dc9fe23f3e9fac17c448542b9cb250d8b1a`, matching the record's C2 row; its one row (`rfcs/RFC-0011/deterministic-selection-and-budget.md` = `c5390869fc184c346220084db29c72508eca122e6ba792adb5dc7e650560962f`) verifies. [Observed]

### 1.3 Partition sweep over the RFC-0011 package — with a denominator

**Denominator: 3.** Every regular file under `C/rfcs/RFC-0011/` (recursive), enumerated mechanically:

```
rfcs/RFC-0011/README.md
rfcs/RFC-0011/deterministic-selection-and-budget.md
rfcs/RFC-0011/packet-identity-provenance-and-memory.md
```

- C1 ∩ C2 = ∅ (no file in both manifests).
- C1 ∪ C2 = the full population; **uncovered = ∅**.
- Rows naming files absent from the tree = ∅.

**The C1 and C2 manifests partition the RFC-0011 package exactly.** [Observed]

### 1.4 Second method, and the whole-corpus partition

Independent of `check_governance.py`, I counted: files under `C/rfcs/**.md` = **39**; non-comment rows in `ACTIVE-CONTRACT-MANIFEST.txt` = **39**; wave-manifest rows = 19 (A) + 11 (B) + 2 (C1) + 1 (C2) + 5 (D1) + 1 (D2) = **39**. The six waves partition the active set with no residue. [Observed]

Read-only checks run in the clone, **output read, not exit codes**:
- `check_governance.py` → `25 OK, 15 WARN, 0 FAIL (40 checks)`. Relevant lines: `OK CG-7a manifest digests valid; waves partition the set — 78 entries examined, 0 findings`; `OK CG-7b wave-act arguments match the wave manifests — 6 arguments examined, 0 findings`.
- `build_contract_index.py --check` → `index matches regeneration — no drift`.
- `build_dependency_index.py --check` → `dependency index matches regeneration — no drift`.
- `build_budget_report.py --check` → `fixture anchors match regeneration`.
- `verify_final_prespec.py` → reports 341 numbered clauses; RFC-0011 module word counts 1393 / 1370 / 1322; it also prints the standing corpus-size note (`total 110081 exceeds the 35–50k target band…`), which is a package-wide disclosure, not a C1 finding.

**Manifest verdict for Wave C1: clean.** The argument is current, the two files are byte-exact at the digests bound, and the C1/C2 split is a true partition.

---

## 2. External reliance posture of the C1 set — the good news first

### 2.1 Declared `depends_on` edges

`README.md` and `packet-identity-provenance-and-memory.md` both declare
`depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0008, RFC-0010]` — 8 edges.
Wave A binds RFC 0001–0006; Wave B binds RFC 0007–0009; D1/D2 bind RFC-0010. **All 8 edges are satisfied at act 5.** No external forward reliance. [Observed]

### 2.2 Every outbound clause citation resolves into already-bound waves

I extracted every `RFCx-y` token from both C1 files with Python `re`, expanded the shorthand ranges written in prose (`RFC5-16/17`, `RFC5-14/15`, `RFC8-18..RFC8-20`), and checked each against the set of clause identifiers actually *defined* across `C/rfcs/**` (341 defined ids found by a bolded-clause-opener pattern).

**Denominator: 19 distinct external clause identifiers.** Every one is defined, and every one lives in a wave bound before C1:

| Cited | Defining module | Wave |
|---|---|---|
| RFC3-16 | `RFC-0003/governance-homes-and-owner-acts.md` | A |
| RFC5-6, RFC5-25 | `RFC-0005/admission-and-boundary.md` | A |
| RFC5-14, RFC5-15, RFC5-16, RFC5-17 | `RFC-0005/consent-egress-secrets.md` | A |
| RFC6-13, RFC6-14, RFC6-28 | `RFC-0006-…-query-drawer.md` | A |
| RFC7-38 | `RFC-0007/rendering-and-surface.md` | B |
| RFC8-18, RFC8-19, RFC8-20 | `RFC-0008/state-vocabulary-and-cost.md` | B |
| RFC8-32 | `RFC-0008/accounting-reconciliation-and-release.md` | B |
| RFC9-52 | `RFC-0009/interaction-parity-and-release.md` | B |
| RFC10-7, RFC10-8, RFC10-12 | `RFC-0010/prevention-envelope-and-attention.md` | D1 (module 2) |
| RFC10-16 | `RFC-0010/mission-identity-approval-and-lifecycle.md` | D1 (module 1) |

**0 dangling citations; 0 citations into Wave D2's module; 0 citations into candidate material outside the RFC corpus.** Non-RFC references are doctrine and owner-direction identifiers only (VIS-4, VIS-7, SEC-2, SEC-5, OD-R10-3, OD-R10-4) plus two path references (`README.md`, `../../CONTEXT-BUDGET-REPORT.md`). [Observed]

### 2.3 The seam, measured

This is the answer to task 3(a)'s first half, and it is favourable:

**`packet-identity-provenance-and-memory.md` contains zero citations to any Wave C2 clause.** The complete set of RFC11 identifiers appearing anywhere in that file is `RFC11-1, -2, -3, -5, -6, -7, -8, -9, -10, -12` — exactly the C1 clause set. `RFC11-4`, `RFC11-11`, `RFC11-13`, `RFC11-14`, `RFC11-15`, `RFC11-16` **do not appear in module 1 at all**. (Denominator: all 22 distinct `RFCx-y` tokens found in the file, each one enumerated with its line numbers.) [Observed]

`README.md` does cite all six C2 clauses — at lines 46 (the clause map), 89–95 (§1 summary), 176 (§8 question q1). Those are index rows and a summary, which is what an index is for.

So the C1→C2 seam is **not** carried by citations. It is carried by one undefined term, which is finding **M1** in part 2.

*(part 1/3 ends — findings follow in part 2)*

# RD-22 — Wave C1 exact-package review (part 2/3): findings

Ordered blocking → major → minor.

---

## BLOCKING

### B1 — RFC11-12's coverage-matrix range is short by four clauses, and the correction lives only in the index

**Anchor — the clause, quoted** (`packet-identity-provenance-and-memory.md` §2.5, lines 158–160):

> "At surface specification a clause-to-requirement coverage matrix over **RFC11-1..RFC11-12** is produced — **that matrix is review material, never authority**."

**Anchor — the index, quoted** (`README.md` "Phase boundary", lines 185–187):

> "…its clause-to-requirement coverage matrix must cover **RFC11-1…RFC11-16 across both modules**, not module 1 alone."

**Measurement.** I computed the defined-clause set for every RFC by scanning `C/rfcs/**` for bolded clause openers. RFC-0011: **16 clauses, RFC11-1…RFC11-16, no gaps**. The acceptance record §3 states the same range (`**RFC11-1..16**`), and `05-CONTRACT-INDEX.yaml` lists 16 clause rows. So the clause's stated matrix range under-covers the package by exactly **RFC11-13, RFC11-14, RFC11-15, RFC11-16** — the four clauses the acceptance record's wave-history note says round-2026-08d *added* ("RFC-0011 split and amended (RFC11-13..16)"). The range was not moved with the amendment; the README was. [Observed]

**Why this is not repaired by the README.** Two bound-or-binding clauses say so in terms:
- RFC11-12 itself: the matrix "is review material, never authority".
- RFC11-4 (C2), on exactly this construction: *"An index's restatement of a phase rule is never the clause: the restatement points, the defining module carries."*
Plus repository verification rule 8 and the standing prohibition on treating an index as authority. The README's `RFC11-1…RFC11-16` is a restatement that **contradicts** rather than points; the defining module carries `RFC11-1..RFC11-12`, and that is what Wave C1 would freeze.

**Scope, stated honestly.** The *phase gate* is intact: RFC11-12 forbids scheduling "implementation work for user-observable Context Compiler behavior … solely from this RFC" and requires "every observable consequence" to map to an OpenSpec requirement or a reviewed N/A — that prohibition is scoped to the contract, i.e. all 16 clauses. What is short is the **deliverable that demonstrates the gate held**. RFC11-14 (omission register contents, undecidable-fails-closed) and RFC11-15 ("the packet states that basis") plainly have observable consequences; a matrix produced faithfully to the clause would certify RFC-0011 with a denominator of 12 out of 16 while four behaviour-bearing clauses went unswept. That is the RD-8 defect shape — a coverage claim whose denominator is not the population — reproduced inside the clause that exists to prevent it, and it is why I rate it blocking rather than major.

**Failure scenario.** Wave C1 is performed. RFC11-12's bytes are frozen. At surface specification the team produces the matrix the clause names, covering RFC11-1…RFC11-12; RFC11-13…RFC11-16 receive neither a requirement mapping nor a reviewed N/A; the package is signed off as covered. Repair after the act requires `REWORK FOUNDATIONAL WAVE C1`, a regenerated manifest, and a fresh digest-bound review — where today it costs one token.

**Concrete repair.** In `packet-identity-provenance-and-memory.md` line 159, replace `RFC11-1..RFC11-12` with `RFC11-1..RFC11-16`. Then regenerate `WAVE-C1-MANIFEST.txt` and the §1 C1 argument by script, record the change as a semantic delta, and re-run this review against the new bytes (rule 10). A range-free formulation would be more durable — RFC-0008 and RFC-0009 write the deliverable as "every clause" / "for RFC 0009 **entire**", which cannot go stale under amendment.

**Cross-wave note, not repairable in C1 and reported for the owner's benefit.** The identical defect stands in RFC-0010: RFC10-16 says *"clause-to-requirement coverage matrix over RFC10-1..RFC10-22 is produced"* while RFC-0010 has **24** clauses and its README says `RFC10-1…RFC10-24`. Same shape, short by RFC10-23/RFC10-24. Since no act has yet been performed, both are still cheap to fix; after Wave D1 is performed, RFC-0010's is not. I did not review Wave D1 and make no verdict on it — I report the measurement because a fix batch that repairs only C1 leaves the pattern in place. This is now the *third* recorded instance of a stale numeric range in this corpus (RD-8's `322 clauses / RFC10-1..16` correction being the first two). [Observed]

---

## MAJOR

### M1 — "mandatory context" is defined only across the seam; RFC11-5's positive duty has no bound criterion during the C1-only interval

**Anchor — the C1 clause, quoted** (module 1 §2.2, RFC11-5, lines 80–83):

> "Inference (model judgment, semantic retrieval) **may add suggested context, with provenance marking it suggested and by what**; it may **never suppress, demote, or replace** mandatory deterministic context. A packet distinguishes its mandatory core from its suggested additions."

**Anchor — the defining clause, which is C2** (`deterministic-selection-and-budget.md` §2, RFC11-4, line 42):

> "**Mandatory context is selected deterministically** — same inputs, same selection — from, at minimum: stable entity and relation identities in the objective's scope; the work/mission warrant; …"

**Measurement.** "mandator*" occurs 7 times in module 1 (lines 32, 37, 52, 82, 83, 108, 119). Of those, line 52 is RFC11-1's "the envelope is a mandatory input", lines 32/37 are the module's own scope prose, and lines 82/83/108/119 are the term used inside RFC11-5, RFC11-8 and RFC11-10. **No clause in the C1 set defines what makes context mandatory.** RFC11-6 introduces a second undefined term, "required context" ("If required context cannot be determined…"). The definitional home of both is RFC11-4, in Wave C2. [Observed]

**Direction of the exposure — stated fairly, because it bounds the severity.** Three of the four uses are *exclusionary* (RFC11-8: transcripts "are never mandatory context"; RFC11-8 and RFC11-10: an unbacked interpretation or self-asserted gate field "never enters mandatory context"). Those keep their force whatever the term's extent, and they fail closed. RFC11-1 supplies a bound floor of packet content independent of RFC11-4, and RFC11-6's default is that the run does not launch. So the C1-only interval is conservative, not permissive, on every path but one. [Inferred]

**The one path.** RFC11-5's *positive* duty — "A packet distinguishes its mandatory core from its suggested additions" — has, during the C1-only interval, no bound criterion for where that line falls. A compiler could designate an RFC11-1-sized mandatory core, omit nothing it recognised as a candidate, and render the packet **complete** under RFC11-6, because nothing "required" was undeterminable. The safeguard against exactly that — RFC11-15's *"doctrine/craft selection for it is **not claimed deterministic**, and the packet states that basis rather than implying a derivation that did not happen"* — is in Wave C2. In the C1-only interval a packet may imply a derivation that did not happen, and no bound clause forbids it. [Observed] that no C1 clause states the duty; [Inferred] the consequence.

**Mitigation that a reviewer must weigh, and I do.** RFC11-12 forbids scheduling any implementation of Context Compiler behaviour from this RFC, so during pre-specification no compiler exists and the exposure is textual rather than operational. This is why M1 is major and not blocking.

**Concrete repair — three options, cheapest first.**
1. **No byte change.** Perform C1 and C2 as one sitting, or state the condition at the act (see M3). The C1-interval then has no operational duration.
2. **Record-level.** Add to the acceptance record §1 C1 row the disclosure Wave B's row already carries in kind — see M3, which repairs M2 and M3 with the same sentence and costs no digest churn.
3. **Clause-level, if the owner wants the interval self-carrying.** Append to RFC11-5: *"A packet records the basis on which its mandatory core was derived; where that basis is not a contractually fixed derivation, the packet states so rather than implying a derivation that did not happen."* This is the RFC11-15 sentence pulled to the C1 side. It changes bytes, so it forces a manifest regeneration and a re-review.

### M2 — the C1-interval conformance posture is carried by README prose alone

**Anchor — quoted in full** (`README.md`, "The seam, and the acceptance boundary", lines 63–66):

> "References from module 1 to module 2's selection semantics are staged until module 2 is accepted; until then a conforming packet is compiled against module 1's identity and disclosure duties **with its selection basis stated**."

This is the sentence that makes Wave C1 defensible standing alone — it defines what conformance means during the interval. It is a **conformance rule**, not an index row: it tells a compiler what to do and what to disclose.

**Absence sweep, with denominator.** Denominator = all 3 files of the RFC-0011 package, searched with `grep -F` (never a bracket class) for `selection basis`, `staged`, `until module 2`, `interval`, `not claimed deterministic`. **Hits: README lines 64 and 66 only. Zero hits in `packet-identity-provenance-and-memory.md`. Zero in `deterministic-selection-and-budget.md`.** No clause anywhere in the package states the staging posture or the "selection basis stated" duty. [Observed]

**Task 3(a)'s question, answered directly: the C1-interval posture is carried only by README prose. It is not carried by any citable clause.** Under the repository's rule that an index is never authority, and under RFC11-4's own "the restatement points, the defining module carries", the sentence that licenses the C1-only interval cannot be cited to defend a packet compiled in it.

**Concrete repair.** Same three options as M1 — they are one defect seen from two sides (M1 is the term, M2 is the rule that would have contained it). Option 2 is the proportionate one: the acceptance record §1 is not bound by the C1 act's argument (the act binds the *manifest*), so stating the interval posture there costs nothing and is the form Wave B already uses.

### M3 — the acceptance record's C1 row is accurate on scope and silent on the seam

**Task 3(c), answered.** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1, row C1:

> "| C1 | `ACCEPT FOUNDATIONAL WAVE C1: a5d3ba1f…` | RFC-0011 module 1 (packet identity, provenance, memory — RFC11-1..3, 5..10, 12) plus the package index, per `wave-manifests/WAVE-C1-MANIFEST.txt`. Declares `depends_on` RFC-0010 (waves D1/D2): recommended after them |"

**What is accurate** [Observed, each verified independently this session]: the argument matches the recomputed manifest digest byte-for-byte; the clause enumeration `RFC11-1..3, 5..10, 12` matches module 1's actual 10 defined clauses exactly; "plus the package index" correctly distinguishes the README from a module; the `depends_on` RFC-0010 ordering note is correct, and I confirmed the ordering is *necessary* — module 1 cites RFC10-7, RFC10-8, RFC10-12 and RFC10-16, all in Wave D1's modules. §3's `**RFC11-1..16**` and "**0011 ×2** modules + README" are both correct. The record's §1 preamble likewise correctly lists RFC11-12 among the eleven binding phase-rule clauses.

**What is missing.** The Wave B row discloses its analogous condition explicitly:

> "Depends on Wave A; performed first, it binds text whose reliances point at candidate material — **lawful only stated at the act**."

The C1 row makes no equivalent statement, though Wave C1 binds text whose meaning is completed by Wave C2 (M1) under an interval rule that no clause carries (M2). The row discloses the *inter-package* ordering (RFC-0010) and is silent on the *intra-package* one. An owner reading only §1 would not learn that performing C1 without C2 leaves "mandatory context" undefined. Review RD-8's standard — the finding that "converts act 1 from a knowing act into a surprised one" — is the standard I am applying.

**Concrete repair.** Append to the §1 C1 row, in Wave B's own register:

> "Module 1 uses *mandatory context* as a primitive whose defining clause is RFC11-4 in Wave C2; performed alone, the packet contract binds identity, immutability, execution-record binding, the fail-closed Unknown rule, governed memory and profiles, while the criterion separating a packet's mandatory core from its suggested additions is not yet fixed — lawful only stated at the act. Performing C2 in the same sitting removes the condition."

This is a record edit, not an artifact edit: it does not touch any digest bound by any act, and it repairs M2 and M3 together.

*(part 2/3 ends — minors and verdict follow in part 3)*

# RD-22 — Wave C1 exact-package review (part 3/3): minors, the README question, and the verdict

---

## MINOR

### m1 — the index declares itself "the lookup authority", and a C1-bound module repeats it

**Anchors, quoted.** `README.md` front matter line 7:

> `clauses: "RFC11-1..RFC11-16 (no gaps, no retired numbers) — distributed non-contiguously across two modules; **the clause map below is the lookup authority**"`

`README.md` lines 39–41:

> "…clause identities are never renumbered, so the map below — not range arithmetic — **is the lookup authority**."

And in the C1-bound module itself, `packet-identity-provenance-and-memory.md` lines 179–181:

> "*End of RFC 0011 module 1. … the package README's clause map **is the lookup authority**. Nothing merged, nothing retired.*"

**Measurement.** `grep -F 'lookup authority'` across all 39 files under `C/rfcs/` returns 8 hits, in **RFC-0010 and RFC-0011 only**. RFC-0002 through RFC-0009 use "lookup **rule**" for the same table. The self-designation is a two-package novelty, and RFC-0010 (Wave D1) already carries it. [Observed]

**Why it is only minor.** The claim is about *location* — which module holds `RFC11-n` — not about normative content, and each module's own front matter carries its range independently, so the map is verifiable against the artifacts rather than trusted. It is nonetheless an index asserting authority in a repository whose standing rule is that an index never is one, and no clause in the package fixes the lookup. Under RFC11-7 the map is precisely "a rebuildable projection" — `05-CONTRACT-INDEX.yaml` regenerates it, and `build_contract_index.py --check` reported `index matches regeneration — no drift` this session, which is the honest ground for trusting it.

**Repair (optional, and it costs a digest).** Use RFC-0002…RFC-0009's word: "the clause map below is the lookup rule; each module's front matter carries its own range." If the wording is kept, keep it consistent with RFC-0010 rather than diverging.

### m2 — §1 Summary looks the package up by range arithmetic across the seam, which the clause map forbids two paragraphs earlier

**Anchor** (`README.md` §1, lines 88–90):

> "This package fixes: packet identity and immutability (RFC11-1..3); **deterministic selection semantics and the incompleteness rule (RFC11-4..7)**; governed memory boundaries (RFC11-8..9); …"

`RFC11-4..7` spans the seam: RFC11-4 is Wave C2, RFC11-5/6/7 are Wave C1. The README states at line 40 that "the map below — **not range arithmetic** — is the lookup authority", then uses range arithmetic to describe the package. The grouping is also inaccurate on substance: module 1's own §1 says *"This module does **not** claim deterministic selection is solved"*, yet the summary labels RFC11-5/6/7 as "deterministic selection semantics". **Repair:** split the item — "the mandatory/suggested distinction, the incomplete-is-Unknown rule and the no-second-truth-store rule (RFC11-5, RFC11-6, RFC11-7); deterministic selection semantics (RFC11-4)". Enumerate; do not range.

### m3 — the reader's summary asserts a property the C1 interval does not deliver

**Anchor** (`README.md` §0, lines 80–82):

> "Mandatory context is selected **deterministically** from graph and applicability rules; inference may suggest more, never silently remove."

Labelled non-normative, which is the right label. But this is the sentence a reader forms their model of the package from, and during the C1-only interval the bound corpus does not deliver it — RFC11-4 is Wave C2. **Repair:** one clause of attribution — "…selected **deterministically** (RFC11-4, module 2) from graph and applicability rules…" — so the reader can see which act makes the sentence true. Same treatment for §4 violation case 2, which turns on a selector's behaviour.

### m4 — the acceptance record's §7 item 9 states an absence that a sweep contradicts

**Anchor** (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §7 item 9):

> "**Single-source structure, disclosed** (safety review): RFC 0001–0009 **never cite RFC-0010/0011**, so the no-self-widening rule has no redundant restatement inside the nine earlier contracts."

**Measurement, with denominator.** Sweeping all 36 non-RFC-0011 module files under `C/rfcs/` for `RFC11-\d+` with Python `re`: **five files contain `RFC11-12`** — `RFC-0001-project-graph-identity-state-planes.md:744`, `RFC-0002/rendering-vocabularies.md:203`, `RFC-0003/manifests-and-namespace.md:501`, `RFC-0004/fidelity-joins-and-mappings.md:199`, `RFC-0005/admission-and-boundary.md:342`. Every one is inside a `(Shape-parallel with … RFC10-16, RFC11-12.)` phase-rule list. [Observed]

**Substance holds; wording does not.** Under this repository's fifth verification rule — *"A citation is not a reliance — the `RFC3-16` status banner and `(Shape-parallel with …)` are not dependency edges"* — those are not reliances, so item 9's *argument* is sound. The sentence as written is nonetheless literally false, in the record that teaches rule 5. **Repair:** "RFC 0001–0009 place no reliance on RFC-0010/0011 — their only occurrences are the `(Shape-parallel with …)` phase-rule lists, which rule 5 excludes from dependency edges." No digest is affected; the record is not an act argument.

### m5 — informational, no repair sought

Module 1 carries no `implementation_boundary` front-matter field; the README carries it. I confirmed against RFC11-13 that this is *correct*, not an omission — the declaration belongs "in the front matter of its index (the package README, or the file itself for a single-file contract)". All 11 contracts carry one; RFC-0011's names `RFC11-12`, which is in the C1 set, so even before C2 binds, the declaration's named clause exists. The generated `05-CONTRACT-INDEX.yaml` carries no `implementation_boundary` key for any contract (0 hits) — uniform, so no RFC-0011-specific drift.

---

## The README/index question — task 3(b), answered directly

**Does the C1 package README carry selector-consumed or obligation-bearing content that no clause states?** Yes, in three distinguishable kinds. The distinction that matters is data vs assertion, and no clause in the C1 set settles it:

| README content | Kind | Governed by a clause? |
|---|---|---|
| `implementation_boundary: {kind: requires-openspec, clause: RFC11-12}` (lines 8–10) | **Selector-consumed data.** RFC11-4: the mandatory set "always includes, for every selected contract, **what that contract's implementation-boundary declaration names (RFC11-13)**, consumed from the contract's own index"; RFC11-13: "consumed, never re-derived, inferred, or overridden by a selector" | **Only by RFC11-13 / RFC11-4 — both Wave C2.** During the C1-only interval the field is present, well-formed, and ungoverned: no bound clause requires it, defines its `none \| requires-openspec \| craft-policy` vocabulary, or attaches the consequence (packet **incomplete**) to its absence |
| The clause map + lookup rule (lines 33–51), self-designated "the lookup authority" | **Data, verifiable against the artifacts** — each module's front matter carries its own range, and `build_contract_index.py --check` regenerates the map with no drift | **No clause.** m1. Tolerable because it is checkable, not because it is authorised |
| "…until then a conforming packet is compiled against module 1's identity and disclosure duties **with its selection basis stated**" (lines 63–66); "its clause-to-requirement coverage matrix **must cover RFC11-1…RFC11-16**" (lines 185–187) | **Assertion — obligation-bearing.** These impose duties on a compiler and on the surface-specification phase | **No clause states either. Both are contradicted or unreached by the clauses that do exist** — RFC11-12 says `RFC11-1..RFC11-12`; no clause mentions a selection basis. **B1 and M2** |

**The judgement.** The first two are legitimate index content — machine-readable data, and a routing table that regenerates from the governed artifacts, which is exactly RFC11-7's category of "rebuildable projections". The third is not: it is normative text lodged in an artifact the corpus's own rules deny normative force. Wave C1 binds the README's *bytes* by digest, which is not the same as making its prose citable — RFC11-4 draws that exact line ("the restatement points, the defining module carries"), and verification rule 8 forbids a reviewer from anchoring to prose in place of a clause. So the README's coverage correction cannot cure B1, and its staging sentence cannot carry the interval.

## Package self-description accuracy — task 3(d)

| Claim | Verification | Result |
|---|---|---|
| "Every clause identity appears in exactly one module"; table "exhaustive over RFC11-1…RFC11-16 with no gaps and no duplicates" | Union of the two map rows = {1…16}; intersection = ∅; independently, `05-CONTRACT-INDEX.yaml` lists 16 rows with one module each | **Accurate** |
| Module 1 front matter `RFC11-1..RFC11-3, RFC11-5..RFC11-10, RFC11-12` | = 10 ids; matches the clause map row; matches the 10 clauses actually defined in the file | **Accurate** |
| Module 2 front matter `RFC11-4, RFC11-11, RFC11-13..RFC11-16` | = 6 ids; matches the map; 10 + 6 = 16 | **Accurate** |
| README `clauses: "RFC11-1..RFC11-16 (no gaps, no retired numbers)"` | Computed max = 16, gaps = ∅ | **Accurate** |
| **RFC11-12's coverage range `RFC11-1..RFC11-12`** | Package is RFC11-1…RFC11-16 | **INACCURATE — short by 4. B1** |
| README's phase-boundary restatement `RFC11-1…RFC11-16` | Matches the package; contradicts the clause it restates | **Accurate as a count, unauthorised as an obligation. B1** |
| "The clause text is in `packet-identity-provenance-and-memory.md` §2.5" | §2.5 is the heading at line 148; RFC11-12 at line 150 | **Accurate** |
| §8 question routing (q1 → module 2 §8; q2, q3 → module 1 §8) | Module 1 §8 holds items 2 and 3 and no item 1; module 2 §8 holds item 1 and no items 2–3; numbering does not shift across the split | **Accurate** |
| "Module sizes are deliberately not stated here" | No numeric measurement anywhere in either C1 file; `CG-21 contract prose states no measurement — 39 modules examined, 0 findings` | **Accurate** |
| §1 Summary's clause groupings | `RFC11-4..7` crosses the seam and mislabels RFC11-5/6/7 | **Loose — m2** |
| §0 reader's summary determinism claim | True only after C2 | **Premature in the C1 interval — m3** |
| §6 "this contract is new at rev10 and has no history file" | Charter forbids me `history/`; not verified | **[Unknown]** |
| "the package was split along the seam … **after** the clauses were numbered" | Provenance claim; the round record is outside my charter | **[Unknown]** — though B1's stale range is consistent with it |

Section numbering skips §3 in the README; this is the package-index convention (RFC-0010's README skips it identically, the module carrying "The contract" as its §2). Not a finding.

---

## The central question

**Is the packet contract independently acceptable during the C1-only interval, before the selection semantics bind?**

**Substantively, yes — and the split is well made.** What module 1 fixes stands on its own: RFC11-1's packet identity and its explicit refusal to be an authorization source ("whoever mints packets grants nothing"); RFC11-2's execution-record binding and no-edit-in-place rule; RFC11-3's prohibition on the read-everything dispatch; RFC11-6's fail-closed Unknown with the relaxation forced to be explicit and owner-visible; RFC11-7's no-second-truth-store; RFC11-8/9's governed memory with propose-only promotion pending q3; RFC11-10's profiles that "can never widen an envelope" and whose self-asserted gate fields "fail closed". None of that needs RFC11-4. All eight external `depends_on` edges are satisfied at act 5, all 19 outbound clause citations resolve into bound waves, and module 1's clause text cites **no** C2 clause. The README's own framing of the seam is the correct one: "a packet's honesty … is contractually fixed even while the selection policy that fills it remains under repair."

**Procedurally, not yet — for two reasons, one of which is inside the bytes.**

1. **B1 is a defect in the C1 subject itself.** RFC11-12 would be frozen mandating a coverage matrix that under-covers its own package by four clauses, with the correction sitting in an artifact the corpus denies authority. The act is what makes it expensive; today it is one token.
2. **The interval posture is uncitable (M1 + M2).** The sentence that makes C1-alone defensible is README prose, and the term it governs is defined across the seam. This is repairable at zero digest cost by stating the condition at the act, in the register Wave B's row already uses (M3) — but as the record stands, an owner performing C1 alone would not be told.

I record explicitly what I am *not* claiming: the interval is not dangerous. Every cross-seam use of the undefined term is exclusionary and fails closed, RFC11-1 supplies a bound content floor, RFC11-6 blocks by default, and RFC11-12 forbids any Context Compiler implementation from being scheduled at all — so no compiler can exist to exploit the gap during pre-specification. The defects are of record-keeping and of what a frozen clause will mandate later. That is precisely the class of defect an acceptance review exists to catch, and it is why the verdict is REVISE rather than REJECT: the package is sound, the repairs are small and named, and none of them touches the design.

**Recommended disposition.** Fix B1 (one token in module 1, line 159 — and fix RFC10-16's identical range while no act has bound it); regenerate `WAVE-C1-MANIFEST.txt` and the §1 C1 argument by script; add the M3 sentence to the §1 C1 row; take m2/m3 into the same batch since the README's digest moves anyway; treat m1 as an owner call on corpus-wide wording; correct m4 in the record. Then re-run a fresh-context review against the new bytes — this review is bound to manifest `a5d3ba1f22ad0ff5ff66485b1829e5b2f652a8c7678dcc96699eaca4ac5b2b4d` and is worth nothing once those bytes change.

VERDICT: REVISE
