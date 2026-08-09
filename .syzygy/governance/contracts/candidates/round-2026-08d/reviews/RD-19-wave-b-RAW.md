RD-19 — fresh-context exact-package review, round-2026-08d, **Wave B** (RFC 0007–0009, 11 modules). Date 2026-08-09. Baseline 771965c. Clone-only read. **(part 1/3)**

## 1. Manifest verification

Method: sha256 recomputed in Python from file bytes, never transcribed; manifest parsed programmatically; file set compared against a full `os.walk` of `C/rfcs/`.

**Manifest's own sha256 [Observed]:** `daa6a5dd37b7f92ac4ba4fc8a7bb491ecbffc02ba43227448f64f88dc3c3bebb` — matches the argument in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 row B and the manifest's own header line.

**Rows: 11. Recomputed digests: 11/11 MATCH [Observed].** Rows are in codepoint order (`paths == sorted(paths)` verified).

**File-set sweep with denominator [Observed].** `C/rfcs/` holds **39 files**. Files under `rfcs/RFC-0007|0008|0009`: **11**. Set difference empty in both directions. The other 28: RFC-0001..0006 = 19 (Wave A), RFC-0010 = 6, RFC-0011 = 3. **The Wave B file set is exactly the RFC 0007–0009 package — nothing extra, nothing missing.**

**Corroborating, output read not exit codes:** `build_active_manifest.py --check` → "all 7 manifests match regeneration"; `check_governance.py` → "25 OK, 15 WARN, 0 FAIL (40 checks)", CG-7a "78 entries examined, 0 findings", CG-7b "6 arguments examined, 0 findings"; `verify_final_prespec.py` → PASS, "numbered clauses defined: 341" (matches record §3).

**Independent clause sweep [Observed].** Paragraph-initial bolded clause headings extracted by regex: RFC7-1…40 defined exactly once, 1–25 / 26–40 across the two modules; RFC8-1…32 exactly once, 1–11 / 12–20 / 21–32; RFC9-1…52 exactly once, 1–23 / 24–45 / 46–52. Lettered sub-clauses land where each README says. No duplicates, no gaps, no identity in two modules. Every lookup rule reproduces.

**Retired-phrase sweep of the bound bytes [Observed].** `grep -F` over all 11 files for `ACCEPT FOUNDATIONAL RFCS`, `ACCEPT COMPACTED FOUNDATIONAL RFCS`, `ACCEPT FOUNDATIONAL WAVE`, `ACCEPT TOPOLOGY`, `ADOPT PROJECT OVERVIEW`, `CONFIRM CRAFT AMENDMENT` — **zero hits, all six sweeps**. Wave B does not carry the defect the Wave A review found.

## 2. Forward-reliance sweep — the central question for an exact-package act

Method: regex `RFC(\d{1,2})-\d+` over all 11 files, tallied per namespace; every hit outside RFC1–RFC9 printed with file:line.

**Result [Observed]: exactly one clause-level citation of a not-yet-bound artifact exists in Wave B.**

`rfcs/RFC-0009/semantic-geography.md:143`, inside **RFC9-8(a)**:
> "**This machinery is authority-bearing, and a registry that changes authorization, evaluation inputs, stable identity, layout truth, or any other project fact belongs in typed governance, never in personal presentation state** — so it lives in the typed **workspace governance store** (RFC10-15), never in the workspace manifest…"

**Zero `RFC11-n` citations anywhere in the wave.** The remaining RFC 0010/0011 mentions (RFC-0008 README:186/190, `accounting-…`:337/340, `identity-…`:310, `state-vocabulary-…`:323, RFC-0009 README:144/149) are *Provides-to* or shape-parallel lines. A citation is not a reliance; none of those imposes anything on Wave B's conformance.

**Is the RFC10-15 reliance staged honestly? At the clause, yes** [Observed]. The next sentence states the fail-closed consequence — "(Staged reference: until an accepted RFC 0010 mints the store, no portfolio re-lay is lawful — the machinery waits with the store, and the manifest never substitutes.)" — and the paragraph closes "Without this machinery, append-stability inherited from RFC9-15 leaves **no lawful way ever to re-lay the portfolio**." I verified the target exists and says what is claimed: `rfcs/RFC-0010/portfolio-and-cross-project-consent.md:39` defines RFC10-15 "Portfolio authority is a distinct plane," and :44 places the material "in a typed, platform-level **workspace governance store**."

**At the package and record level, no** — findings B1 and M1.

**Otherwise the package closes [Observed].** Every other cross-RFC citation lands in RFC 0001–0006 (bound at Wave B time) or inside Wave B. Setting RFC10-15 aside, **the package is independently acceptable on its citations with only Wave A bound.**

**(part 1/3 ends)**

RD-19 Wave B — **(part 2/3)** — findings, blocking → major.

## BLOCKING

### B1 — The acceptance record's own owner-attention list denies the only forward reliance in this wave

**Anchor (acceptance record, §7 item 9), quoted exactly:**
> "9. **Single-source structure, disclosed** (safety review): RFC 0001–0009 never cite RFC-0010/0011, so the no-self-widening rule has no redundant restatement inside the nine earlier contracts. Back-citations were deliberately not added (nine-contract churn for redundancy); the corpus relies on RFC10-15/RFC11-4 loading rules to carry the prohibition into every mission context."

**Contradicting bytes (Wave B, `rfcs/RFC-0009/semantic-geography.md:143`, clause RFC9-8(a)):**
> "…so it lives in the typed **workspace governance store** (RFC10-15), never in the workspace manifest…"

RFC 0009 is one of "RFC 0001–0009". It cites RFC-0010, at clause level, in a normative placement obligation. The claim is **false against the bytes Wave B binds** [Observed]. The same item then names RFC10-15 in its own next sentence, so the paragraph is internally inconsistent as well.

This is not a stale figure in a report — it sits in **§7, "Items requiring explicit owner attention at the gate"**, the list an owner reads to learn what they are choosing. An owner performing Wave B on the strength of item 9 believes the wave has no forward dependency; the wave's largest module carries one, and its unsatisfied state is a permanent bar on portfolio re-lay. This is precisely RD-8's "the finding that converts an act from a knowing act into a surprised one," relocated from a stale offering into the live record.

Corroboration that the repository's own tooling knows: `verify_final_prespec.py` prints, as its justification note for the oversize module, "the owner-ordered RFC9-8(a) amendment relocating the portfolio layout registry to the **RFC10-15 workspace governance store, with its staged reference**." The verifier states it; §7 item 9 denies it.

**Severity: blocking for Wave B.**

**Repair.** Rewrite §7 item 9 to state the actual position, e.g.: *"RFC 0001–0008 never cite RFC-0010/0011. **RFC 0009 carries exactly one such citation** — RFC9-8(a)'s staged reference to the RFC10-15 workspace governance store, whose consequence while RFC 0010 is unbound is that no portfolio re-lay is lawful. No other back-citations were added…"* Then regenerate no digest — §7 is outside every wave manifest, so the repair is digest-stable for Wave B.

---

## MAJOR

### M2 — Wave B's forward reliance is invisible to every machine-readable dependency declaration and to the act's own scope row

The RFC10-15 reliance is disclosed **only** in running prose inside a 7,079-word module. It appears in none of the places a reader or a check would look [Observed, swept]:

- `rfcs/RFC-0009/README.md` frontmatter: `depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0007, RFC-0008]` — no RFC-0010.
- `rfcs/RFC-0009/semantic-geography.md` frontmatter: `depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006]` — no RFC-0010 (and no RFC-0005, see m2).
- Acceptance record §1 row B: *"The 11 modules of RFC 0007–0009 (Polaris, Trajectory, Orrery) per `wave-manifests/WAVE-B-MANIFEST.txt`. Depends on Wave A; performed first, it binds text whose reliances point at candidate material — lawful only stated at the act."*

Row A, by contrast, carries an explicit closure statement — *"Every `depends_on` edge of these contracts stays inside the wave"* — so a reader is trained to read the absence of such a sentence in row B as covered by "performed first, it binds text whose reliances point at candidate material." But that caution is **conditional on ordering** (performing B before A). The RFC10-15 reliance survives the correct ceremony order A → B and is not an ordering artifact at all. A `depends_on`-based closure check would pass Wave B while the reliance stands.

A further fact the owner should have at the act, which nothing in the wave or the record states [Observed]: `rfcs/RFC-0010/README.md:194` records **"| q3 | Workspace governance store (RFC10-15) | open |"**. The condition that releases RFC9-8(a)'s bar is itself an **open owner question inside an unbound RFC**. "Until an accepted RFC 0010 mints the store" is therefore weaker than it reads — it is not merely awaiting an act, it is awaiting a ruling that has not been made.

**Severity: major.**

**Repair.** (a) Add `RFC-0010` to `semantic-geography.md`'s and `RFC-0009/README.md`'s `depends_on` with an explicit staged marker, or add a `staged_depends_on` key so the edge is machine-visible; and (b) extend §1 row B: *"Wave B's `depends_on` edges stay inside Waves A∪B, with one stated exception: RFC9-8(a) places the portfolio layout registry in the RFC10-15 workspace governance store (Waves D1). Until D1 is performed **and RFC 0010 §8 q3 is ruled**, no portfolio re-lay is lawful. Accepting Wave B accepts that bar."* Note (a) moves the digest and needs a re-offer; (b) does not.

---

### M3 — RFC-0007's package index reports a defect against already-bound RFC 0002 as **Live**, on a premise the bound bytes falsify

**Anchor (`rfcs/RFC-0007/README.md` §5, quoted exactly):**
> "1. **RFC 0002 / RFC 0006 — dangling-anchor vocabulary. Live.** RFC7-11's broken anchors land in RFC6-5's `unresolvable` outcome, but **RFC2-24 has no Unknown reason whose resolution route is "repair the reference"**; RFC 0006 already reported this, and Polaris is the most exposed surface. This package supports adding `reference-unresolvable` to RFC2-24; RFC 0002 has added it as reason #11 citing this finding, **and the owner may still strike it at acceptance**."

**Against the Wave-A bytes (`rfcs/RFC-0002/rendering-vocabularies.md`, RFC2-24) [Observed]:**
- Reason **#11 `reference-unresolvable`**, resolution route column: **"Repair the reference, owned by the governed project."** The bolded premise is false.
- Clause heading: **"RFC2-24 — Twelve reasons, closed."** and, in the clause body: *"answered at acceptance by decision **A5**: **#12 `execution-blocked`** added, **#11 retained**, #10 not split, list **closed at twelve**."* The owner **has** ruled; "may still strike it at acceptance" describes an option A5 closed.

The list's own labelling convention makes this load-bearing: items 2 and 3 in the same list are marked "**Discharged**" and "**Resolved**". Item 1's "**Live**" is a status claim, and it is wrong. At Wave B the owner has Wave A bound, so this is a live contradiction *across the act boundary* — the package index tells them an outstanding defect stands against a contract they have already accepted, and invites a reconsideration that is foreclosed.

**Severity: major.** It is index prose, not a clause, but a package index's defect register is exactly what an owner consults to learn what remains open, and this is inside the digest Wave B binds.

**Repair.** Relabel to **Discharged — owner decision A5**, and rewrite the premise: *"RFC7-11's broken anchors land in RFC6-5's `unresolvable` outcome. RFC 0002 minted `reference-unresolvable` as RFC2-24 reason #11 on this finding, and decision A5 retained it with the list closed at twelve. No RFC 0002 change is outstanding."* Digest-moving; batch with any other Wave B repair.

---

### M4 — RFC9-43 cites "the full RFC9-46 equivalence tuple" and then reproduces the narrower RFC6-22 tuple, while asserting the two are identical

**Anchor (`rfcs/RFC-0009/visual-grammar-and-lenses.md`, RFC9-43), quoted exactly:**
> "**The disclosed composition is the full RFC9-46 equivalence tuple** — per-label, per-tier, per-Unknown-reason and per-freshness-state counts **and sibling surface states** … never label and Unknown reason alone. … **RFC6-17 binds the same enumeration at the foundation layer; the two are deliberately identical, and any divergence is a defect to close rather than a surface-local variation.**"

**Against RFC9-46 (module 3, same package) [Observed]:**
> "**Added to the tuple at acceptance: the positional-expression state and the backlog partitions.** The tuple additionally carries, for the same (evaluation, scenario context, lens, declared filter scope): the **RFC9-9(b) positional-expression state** … and **both RFC9-15(b) part 4 partition counts**, refresh-clearable and structurally unhonorable, separately."

And RFC6-17 (Wave A) enumerates exactly the RFC6-22 tuple — label, tier, reason, freshness, sibling surface states — with no surface-local additions.

So **"the full RFC9-46 equivalence tuple" is strictly wider than the list RFC9-43 then gives, and strictly wider than RFC6-17's**; "the two are deliberately identical" is false as written. Two readings, both bad, and an implementer must choose blind:
1. Take the citation at its word — every aggregate on the map must disclose the positional-expression state and both backlog partitions. RFC9-47's gate list has no aggregate-level check for this, so the obligation is created and tested nowhere — the exact failure RFC9-47(a) exists to prevent.
2. Take the enumeration at its word — then RFC9-43 anchors on the wrong clause, and RFC9-46's two added fields silently do not cross into aggregation.

This is the drift RFC7-37 names in the same wave: "a paraphrase is how a roll-up rule drifts from the aggregation contract it instantiates." Here the paraphrase and the citation disagree with each other.

**Severity: major** — an internal contradiction between two modules of one package, over a release-gated obligation.

**Repair.** Decide and state it. If aggregates carry only the foundation tuple, change the citation to **RFC6-22** and keep "the two are deliberately identical." If they carry the surface-local fields too, keep RFC9-46, add those two fields to RFC9-43's enumeration, delete "the two are deliberately identical", and route the aggregate-level check into RFC9-47 per RFC9-47(a) part 1's same-logical-change invariant.

---

### M5 — RFC-0007's seam self-description: the edge count is wrong and the enumeration is incomplete, in a figure already corrected once for this

**Anchor (`rfcs/RFC-0007/README.md`, "Where the seam falls"), quoted exactly:**
> "No clause spans the seam. **Twelve citation edges cross it, all resolvable by the lookup rule above:** module 1 → module 2 at RFC7-6→RFC7-30, RFC7-11/11(a)→RFC7-33, RFC7-14→RFC7-26, RFC7-17→RFC7-26/33, RFC7-20/25→RFC7-33; module 2 → module 1 at RFC7-26→RFC7-17, RFC7-27→RFC7-2, RFC7-29→RFC7-14/18/23, RFC7-30→RFC7-6, RFC7-31/32→RFC7-25, RFC7-33/34→RFC7-5/11/11(a)/13, RFC7-36→RFC7-2/3/7/11/11(a)."

**Swept [Observed], regex `RFC7-(\d+)` over each module:**
- Module 1 cites module-2 clauses **{26, 28, 30, 31, 33}**. The enumeration names only {26, 30, 33}. **RFC7-28 and RFC7-31 are cited across the seam and are not in the list:**
  - `narrative-contract.md:125` (RFC7-5's entity table): "| **Curated diagram** | A hand-composed visual with anchored or marked elements (**RFC7-28**) | The composition |"
  - `narrative-contract.md:155` (RFC7-6's body): "a predominantly-Unknown catalog under an honestly thin narrative is correct output (RFC7-15, **RFC7-31**)"
  - also `:60` and `:568` (module scope and Integration).
- Module 2 → module 1: the enumeration is complete (the only extra hit, `RFC7-1`, is the range endpoint in RFC7-38's "RFC7-1…RFC7-37", not a citation).
- The count: the twelve items are **rows**, not edges. Expanded to (source clause, target clause) pairs the list itself describes ≈29 edges (8 forward, 21 back). "Twelve citation edges" is true of neither the rows-as-edges reading nor the actual edge population.

This figure has already failed once inside a digest set: acceptance record §1a records the prior re-quote as *"RFC-0007 README self-counts **and edge count** corrected (SD-1, SD-10)."* Verification rule 3 — a derived value quoted outside its owning artifact goes stale silently — is being paid a second time in the same file.

**Severity: major** (repeat defect in a self-description inside the bound digest; not itself an authority claim).

**Repair.** Either drop the count and the enumeration entirely — the lookup rule is deterministic and needs neither, and this is the same move the package already made for module sizes ("deliberately **not stated here**… a measurement copied into contract prose goes stale the moment any module moves") — or generate the enumeration mechanically and stop hand-maintaining it. Do not simply patch "twelve" to a new number; that reproduces the defect.

**(part 2/3 ends — minor findings, clean results, and verdict in part 3/3)**

RD-19 Wave B — **(part 3/3)** — minor findings, what verified clean, verdict.

## MINOR

### m1 — RFC-0009's owner-question index routes q4 to a stub that does not exist

**Anchor (`rfcs/RFC-0009/README.md:188`):** "| q4 | Analytical-plane governance (RFC9-10, RFC9-18) | **answered — B12(c)/B17** | module 2 §8 |"

**Anchor (`visual-grammar-and-lenses.md` §8):** "Numbering is the stable package numbering; **answered items keep a stub here so numbers never shift.**" — the section then carries **q3, q8, q9 only**.

Swept [Observed]: `**q<n>` stubs across the package are q1,q2,q5,q6,q7 (module 1 §10), q3,q8,q9 (module 2 §8), q10 (module 3 §8) = **9 of 10**. `q4` appears in exactly two places: the README row above, and `visual-grammar-and-lenses.md:271` inside RFC9-35's parenthetical "*(Owner decisions B12(c)/B17, answering §8 q4 and q9 with one rule.)*". A reader following the index lands in a section whose stated invariant it violates.

**Repair.** Add a q4 stub to module 2 §8 alongside q9: *"**q4** — analytical-plane governance (RFC9-10, RFC9-18)? **Answered — owner decisions B12(c)/B17**, the single promotion predicate stated in RFC9-35. See history §8."*

### m2 — Module frontmatter `depends_on` is inaccurate in three places

Swept [Observed] by comparing each module's declared `depends_on` against every `RFCn-m` citation in its body:
- `RFC-0009/semantic-geography.md`: declares `[RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006]`; cites **RFC5-20** at :677 ("execution-profile boundaries [Observed: SEC-3; RFC5-20]") and **RFC10-15** at :143. Two undeclared namespaces.
- `RFC-0009/interaction-parity-and-release.md`: declares `[RFC-0002, RFC-0006, RFC-0007, RFC-0008]`; cites **RFC1-25** at :135 ("RFC1-25's anti-conflation rule run as a rendering check") — a release-gate obligation, not an aside.
- `RFC-0008/accounting-reconciliation-and-release.md`: declares `RFC-0005`, but the module contains **zero `RFC5-n` citations**; its §5 line is "**RFC 0005:** machine-client admission for RFC8-31's endpoint answers" — a dependency asserted with no clause anchor (verification rule 8).

**Repair.** Correct the three frontmatter lists; give the RFC 0005 line in RFC-0008 module 3 its clause, or drop the declaration. Digest-moving.

### m3 — RFC8-7 says `queued-for-materialization` is "in RFC1-31's own state names"; it is not one of them

**Anchor (`identity-authority-materialization.md`, RFC8-7):** "Trajectory renders the approved-Proposal lifecycle **drafted → under review → approved → queued-for-materialization → materialized** over the RFC1-28 entity, **in RFC1-31's own state names**."

**Against Wave-A-bound RFC1-31 [Observed]:** "**Proposals**: drafted → under review → approved (kind (e): then `approved` → `materialized`, RFC1-28/29) / adopted … / rejected / abandoned / superseded." No `queued-for-materialization`.

The same clause then says it is "**not** a new kernel lifecycle state," so the clause contradicts its own attribution sentence. This is **honestly staged elsewhere** — the module's §5 reports it as the package's one outstanding foundation defect and §8 q2 asks the owner to confirm or direct RFC 0001 to add the state — so I do not treat it as concealed. The sentence is still literally false for one of five names it attributes.

**Repair.** "…in RFC1-31's state names, **with `queued-for-materialization` added as a work-plane fact rather than a kernel state (§5, §8 q2)**."

### m4 — RFC-0009 README: "The eleven cases" enumerating twelve items

**Anchor:** "**The eleven cases** keep their stable package numbering… Cases **1, 2, 3, 3a, 4, 5** → module 1 §7; cases 6–10 → module 2 §5; case 11 → module 3 §5." That is 6 + 5 + 1 = **12 enumerated items**; module 1 §7 does carry 3a as a separately-headed case [Observed]. Either say "twelve" or drop the count (the routing sentence carries the information alone).

### m5 — RFC-0009 README: "RFC3-16(a) gates four artifacts across two modules"

**Anchor:** "**RFC3-16(a) gates four artifacts across two modules:** those two registries, the promotion of lenses/analytical planes/profile relations (RFC9-35), and the walkthrough judgment and release policy (RFC9-45)." [Inferred] The last item names **two** separately RFC3-16(a)-gated artifacts — RFC9-45 gates the judgment ("honored **only under RFC3-16(a)**") and, separately, the release policy ("under `.syzygy/governance/policies/` (honored only under RFC3-16(a))"). Counting artifacts gives five; the promotion predicate is an act, not an artifact. Low confidence on intent, but the sentence does not survive a careful count either way.

### m6 — Lettered-sub-clause hygiene in `semantic-geography.md`

[Observed] `RFC9-15(b)` exists with **no `RFC9-15(a)` anywhere in the package** (`grep -F` → 0 hits in all four files), and definition order in the file runs RFC9-14 → RFC9-14(a) → RFC9-15 → RFC9-16 → RFC9-16(d) → **RFC9-15(b)** → RFC9-17. RFC-0007's module 2 carries an explicit note where it does the same thing ("RFC7-38, the phase rule, is defined before RFC7-39/40 in file order — **deliberate**"); this module's frontmatter and closing line assert "no gaps" without one. Not a defect in the clauses; a reader-facing inconsistency worth one sentence.

---

## Verified clean — stated with denominators

- **Manifest**: 11/11 digests recomputed and matching; manifest self-digest matches §1 row B; file set exactly RFC 0007–0009 against a 39-file `rfcs/` denominator.
- **Retired phrases**: zero hits across six `grep -F` sweeps of all 11 files. §1 row B's phrase is live and correct; the two retired phrases (`ACCEPT FOUNDATIONAL RFCS`, `ACCEPT COMPACTED FOUNDATIONAL RFCS`) are declared retired in the record and appear nowhere in the wave.
- **Acceptance record §1 row B scope**: "The 11 modules of RFC 0007–0009 (Polaris, Trajectory, Orrery)" — right count, right files, right digest source (`wave-manifests/WAVE-B-MANIFEST.txt`). Accurate, subject to M2's omission.
- **Wave-history note is live and honest**: "**no confirming review is yet bound to any wave argument above** — the round's fresh-context review pass is owed before any wave act is performed." True for Wave B; this review is bound to the digests in part 1.
- **Clause continuity**: RFC7-1…40 (+7 lettered), RFC8-1…32 (no lettered), RFC9-1…52 (+8 lettered) — each defined exactly once, in the module its README's lookup rule assigns. Every README clause range, module list, and lookup rule reproduces. Acceptance record §3's "+7 / +8" lettered counts verified against the bytes.
- **Violation-case distribution**: RFC 0007 (1–7,12,14 module 1; 8,9,11 module 2; 10,13,15 README) = 15, complete and non-overlapping. RFC 0008 (1,2,3,11 / 5,6,7,13 / 8,9,10,14 / 4,12 README) = 14, complete and non-overlapping. Both READMEs' distribution statements are exactly right.
- **Owner-question routing**: RFC 0007 (open q2, q4, both in module 1) and RFC 0008 (open q2 module 1, q3 module 2, q4 module 3) verified stub-by-stub against the READMEs — accurate. RFC 0009 accurate except m1.
- **Cross-RFC citation accuracy, spot-checked against Wave-A bytes**: RFC2-24 "closed at twelve" (RFC9-45's phrasing is correct); reason **#1 `missing-declaration`**, **#5 `mapping-coverage-absent`**, **#8 `contradicted-pending-adjudication`** all match RFC9-20/9-9(b)/9-27/8-8/8-14/8-24's usages; RFC2-25's **six tiers** and **three sibling surface states** (`dismissed-by-decision`, `unadopted-draft`, `editorial-draft`) match RFC9-43, RFC7-20, RFC8-12; RFC6-5's outcome set contains `unresolvable`, `retired`, `incompatible-scenario` as cited; RFC6-14 and RFC6-17 match RFC7-33 and RFC9-43's foundation-layer claims.
- **RFC9-10(c)'s claim "CC-VIZ-5 is amended to match"**: verified true [Observed] — `policies/craft-and-care/performance-and-visual-discipline.md:108ff` carries "return to home is always available and discoverable (SDR-21 as relaxed by the owner at RFC acceptance — the earlier 'one action back to home' wording is superseded; RFC9-10(c) governs)."
- **RFC-0008's outstanding foundation defect is real, not stale**: RFC1-28 and RFC1-31 in bound RFC 0001 contain no `queued-for-materialization`. Reported honestly.
- **RFC 0011**: zero clause citations anywhere in Wave B.
- **Machine checks, output read**: `verify_final_prespec.py` PASS / 341 clauses; `build_active_manifest.py --check` "all 7 manifests match regeneration"; `check_governance.py` 25 OK / 15 WARN / **0 FAIL**, CG-7a–7e all clean.

## Judgment on the four questions asked

**(a) Independently acceptable with only Wave A bound?** On its citations, yes but for one item: **RFC9-8(a)'s RFC10-15 reliance**, which is staged honestly *in the clause* (fail-closed, consequence named, target verified accurate) and **silently at the package and record level** (absent from every `depends_on`, absent from §1 row B, and actively **denied** by §7 item 9). Nothing else in the wave reaches forward. RFC 0011 is untouched.

**(b) Does the record describe Wave B accurately?** Files, count, and digest source: yes. Phrase: live and correct, no retired phrase reachable. **§7 item 9: no** — B1.

**(c) Package self-descriptions accurate?** Clause ranges, module lists, lookup rules, violation-case distribution, and owner-question routing: accurate, except RFC 0009 q4 (m1). Counts and cross-module claims: **three wrong** — M5 (edge count and enumeration), m4 ("eleven cases"), m5 ("four artifacts") — and **one cross-module citation claim contradicts its own target** (M4).

**(d) Anything that would make the owner's act a surprised one?** Yes: **B1**, compounded by **M2**, and independently **M3**.

B1 is not repairable by explanation at the act — the record's own owner-attention list has to say the true thing before the phrase is written. M3 puts a false status claim about already-bound RFC 0002 inside the digest Wave B binds. M4 is an unresolved contradiction between two modules over a release-gated obligation.

Note on batching: B1, M2(b), m4, m5 and the §7 wording are all outside the wave manifest and are **digest-stable**. M3, M4, M5, m1, m2, m3, m6 move the digest and must go in one pass, per verification rule 10 — this review is bound to `daa6a5dd…`, and any edit to the modules retires it.

VERDICT: REVISE
