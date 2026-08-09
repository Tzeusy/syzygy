RD-23 — Wave C2 exact-package review (part 1/3)

Reviewer: independent fresh-context, RD-23. Date 2026-08-09. Baseline commit 771965c, read from the frozen clone only; nothing written. Excluded per brief and not read: `round-2026-08d/`, `history/`, any `reviews/`, `_bootstrap/`. Position assumed: Wave C2 performed SIXTH and LAST, with A, B, D1, D2, C1 already bound.

## 1. Manifest verification

All digests recomputed with `sha256sum`, never transcribed.

**WAVE-C2-MANIFEST.txt own sha256:** `acd27bb8f9b7be76725057b4280e2dc9fe23f3e9fac17c448542b9cb250d8b1a` — [Observed] byte-identical to the argument in the acceptance record §1 row C2.

**Row verification (1 row, denominator 1):**
- `rfcs/RFC-0011/deterministic-selection-and-budget.md` → recomputed `c5390869fc184c346220084db29c72508eca122e6ba792adb5dc7e650560962f` = manifest row. **MATCH.**

**C1 (adjacent, for the partition claim):** `README.md` → `f09821de…1fa8` MATCH; `packet-identity-provenance-and-memory.md` → `de61d66d…9193` MATCH. C1 manifest own sha256 `a5d3ba1f22ad0ff5ff66485b1829e5b2f652a8c7678dcc96699eaca4ac5b2b4d` = record's C1 argument.

**RFC-0011 partition sweep, with denominator.** `find rfcs/RFC-0011 -type f` returns **3 files** (denominator 3). C1 holds 2, C2 holds 1, intersection empty, union = 3. [Observed] **C1+C2 partition the RFC-0011 package exactly.** Independent second method: I reconstructed all six wave manifests and `ACTIVE-CONTRACT-MANIFEST.txt` in Python — union 39 paths, active 39 paths, zero paths in two waves, zero symmetric difference, zero digest mismatches. Third method: `check_governance.py` reports `OK CG-7a manifest digests valid; waves partition the set — 78 entries examined, 0 findings` and `OK CG-7b wave-act arguments match the wave manifests — 6 arguments examined, 0 findings`. Wave row counts 19+11+2+1+5+1 = 39.

**Fixtures: inside or outside?** [Observed] **Outside — entirely.** `grep -F -c fixtures` over all six wave manifests returns 0 for each; `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows) contains no `fixtures/` path. Therefore:
- What act C2 binds: **one file, 1,322 words**, at one digest.
- What act C2 does **not** bind: all ten `fixtures/context-selection-*.md`, `semantic-equivalence-fixtures.md`, `CONTEXT-BUDGET-REPORT.md`, `05-CONTRACT-INDEX.yaml`, the acceptance record itself. The record's §2 protection — *"an artifact edited after its act is, for the record, an artifact with no act (RFC3-16(b) item 3)"* — reaches none of them. After act 6 the fixtures remain freely editable with no digest breaking, which matters enormously given finding B2 below.

Mechanical battery read for output, not exit code: `check_governance.py` → **25 OK, 15 WARN, 0 FAIL (40 checks)**; `verify_final_prespec.py` → **PASS**, *"numbered clauses defined: 341"* (record §3's 341 corroborated), total corpus **110,081 words**. Working tree clean after both runs.

## 2. The central question

**The module states it is acceptable only when its selection rules reproduce the blind golden fixtures — is that acceptance test in a state an owner could knowingly bind?**

**No.** The criterion the module names does not exist; the artifacts it names are outside the act; and the ten goldens do not agree with each other on three of the module's own six clauses, so the test has no single right answer even if a derivation were run. Details as findings B1–B3.

---

# FINDINGS — blocking

## B1 [BLOCKING] The stated acceptance criterion exists nowhere. The module points at an empty place.

**Anchor** (§1 of the C2 module, immediately governing RFC11-4/11/13–16), quoted:

> "This module is acceptable only when its selection rules can reproduce the blind golden selection fixtures — the acceptance criterion is stated with the fixtures, not here, because a criterion inside its own subject cannot gate it."

The principle is right. The referent is empty.

**Sweep 1, denominator 11.** All 11 files in `fixtures/`, searched with Python `re` (not ugrep) for `acceptance|criterion|criteria|reproduce|blind`. Every `blind` hit is one of two boilerplate lines. The protocol line, verbatim and identical across all ten selection fixtures:

> "*Everything above the rule is the task. Everything below is the recorded answer: a blind derivation (the protocol review RD-5 ran) receives the Task section and the governed corpus only, derives a selection, and compares it against what follows — reading no further until its own selection is written down.*"

That states a **procedure**, not a **standard**. It never says what "reproduce" means: exact mandatory-file-set equality? set equality plus identical omission register? plus identical suggested set? plus the trace's reasoning? within what tolerance? It never says who runs it, how many derivations must agree, what a divergence obliges, or which artifact records the result. `semantic-equivalence-fixtures.md` does carry eleven explicit "Pass condition:" lines — but its entire subject is rev9→rev10 clause equivalence (F-EQ-1…F-EQ-8), not selection reproduction.

**Sweep 2, denominator 101.** Every `.md`/`.yaml`/`.txt`/`.py` under `C/` excluding the four `round-*` dirs, `history/` and `reviews/` — 101 files — searched for `golden|reproduce the blind|blind golden|acceptance criterion`. Fourteen hits total: ten are the identical fixture footer *"Selection: hand-authored golden selection"*, two are the module and README stating the condition, one is the acceptance record restating it, one is an unrelated TERM-REGISTRY line. **Zero state a pass/fail standard.**

**Sweep 3 — the mechanical checks that do exist.** Two, and neither tests selection:
- `check_governance.py` CG-18, docstring quoted: *"Each context fixture's packet digest and word count still recompute."* Output read: `OK CG-18 context fixtures recompute — 20 measurements examined, 0 findings` — 20 = 10 fixtures × 2 **measurements**. It re-measures; it cannot know whether the file list is the right file list.
- `verify_final_prespec.py` lines 267–271: comment *"Context-selection fixtures: five, each with required fields + digest"*, predicate `fail(f"context-selection fixtures: found {len(ctx)}, need ≥5")`. A **count floor** that would still pass if five of the ten fixtures were deleted.

**Sweep 4 — no derivation result is recorded.** No fixture, and no file in the 101 swept, records the outcome of a blind derivation: no "derived selection", "diverged", "agreed", or comparable field. The fixtures' own footer says why one could not have been run mechanically: *"**Selection: hand-authored golden selection. Measurement: mechanical. Compiler implementation: absent.**"*

**[Observed]** the criterion is absent. **[Inferred]** an owner performing act C2 would be attesting to a condition that cannot be checked, by them or by anyone, from the bytes the act binds. This is a defect of the **offering**, not of the fixtures — the fixtures are honest about being hand-authored; it is the module that promises a criterion lives with them.

**Repair (choose one, both digest-churning on C2):**
(a) Write the standard. One short artifact, e.g. `fixtures/SELECTION-REPRODUCTION-CRITERION.md`, defining exactly: the compared object (I recommend the ordered mandatory path list **and** the omission register at contract granularity), the tolerance (I recommend zero on the mandatory list; enumerated-and-reasoned on omissions), the number of independent derivations, where results are stored, and what a divergence obliges (REWORK, not silent re-authoring of the golden). Then run it and record the results. Then re-offer C2.
(b) Delete the conditional sentence from §1 and re-offer C2 on its own terms, moving "selection rules unvalidated against any blind derivation" to the acceptance record §7 owner-attention list as a knowing deferral.
Option (b) is honest and cheap; option (a) is what the sentence currently promises.

## B2 [BLOCKING] The condition is anchored to artifacts the act does not bind.

**Anchor:** the same §1 sentence, plus the acceptance record §1 row C2:

> "Carries its own external criterion: acceptable only when its selection rules reproduce the blind golden fixtures (`fixtures/`), a derivation the fixtures' task/answer boundary exists to allow"

**[Observed]** `fixtures/` contributes **0 of 39** rows to `ACTIVE-CONTRACT-MANIFEST.txt` and **0 rows to any of the six wave manifests** (verified by `grep -F` count = 0 per manifest, and by full reconstruction). The C2 act binds exactly one path.

The consequence is structural, not stylistic. The record's own rule is that an act binds bytes; here the module's acceptability is made conditional on bytes **no act binds**. A fixture can be edited the day after act 6 — to make it agree with a selector, or for any other reason — and nothing breaks, no digest moves, no check fails (CG-18 would simply re-measure the new bytes and report OK). Repository verification rule 10 exists for exactly this: *"Freeze the bytes a review is bound to."* The C2 offering does the opposite: it freezes the claim and leaves the subject loose.

**Repair:** if B1 is repaired by route (a), add the ten fixtures **and** the criterion file to `WAVE-C2-MANIFEST.txt` via `scripts/build_active_manifest.py` so the act binds what it depends on — noting this makes the fixtures part of the accepted, never-edited set, which is a real cost the owner should weigh. If repaired by route (b), the anchoring problem dissolves with the sentence.

(part 1/3 ends)

RD-23 — Wave C2 exact-package review (part 2/3)

## B3 [BLOCKING] The goldens contradict each other on three of the module's six clauses. The acceptance test has no single right answer.

I tested the selection rules mechanically against the corpus as bound at this position, rather than reasoning about them. Denominators stated throughout.

### B3a — RFC11-15 is applied by 4 of the 10 goldens and violated by 6.

**Anchor,** RFC11-15's final sentence, quoted:

> "Where a task class or risk class has no declared ownership metadata, doctrine/craft selection for it is **not claimed deterministic**, and the packet states that basis rather than implying a derivation that did not happen."

**[Observed], denominator 10 fixtures.** All ten select at least one doctrine file. Only four (6, 7, 8, 9) cite RFC11-15 and state a basis. Six (**1, 2, 3, 4, 5, 10**) cite RFC11-15 **zero times** while printing doctrine — and fixture 4 also a craft policy — under the heading **"## Required context (mandatory, deterministic)"**. Fixture 4's trace, verbatim: *"Doctrine floor → `security.md` (SEC-3 and the execution posture). Craft duty → `security-and-secrets.md` (secret handling in profile definitions)."* No basis statement anywhere in the file.

Since the ownership metadata does not exist (M2 below), RFC11-15's fallback limb governs 100% of doctrine/craft selection today. Six goldens therefore assert exactly the thing the clause forbids — *"implying a derivation that did not happen"* — and four do not. A blind derivation applying RFC11-15 faithfully would diverge from six of the ten answers. The goldens cannot certify a rule they themselves split on.

**Worse: two goldens describe the same metadata incompatibly.** Fixture 6: *"Doctrine ownership metadata is declared in the contract index's `governance_sources`."* Fixture 9: *"The doctrine and craft selections cannot be cross-checked that way: `governance_sources` rows carry no clause rows, no `governs`, no `applies_to`, and their `rule_ids` are a mention scan…"* Fixture 9 is correct (see M2). Fixture 6's sentence is false against the current bytes.

### B3b — RFC11-14 rule 2's enumeration duty is applied by 2 of 10, at 0–5% by the other 8.

**Anchor,** RFC11-14 item 2, quoted:

> "**Direct `depends_on`.** Add the direct `depends_on` obligations of every selected module. An edge is **satisfied by loading at least one module of the depended-on contract; where an edge is left unsatisfied, the clause identities the loaded modules cite from the depended-on contract are enumerated and disposed of individually in the omission register.**"

**Mechanical test.** I parsed each fixture's `context_load.py` mandatory block, resolved every loaded module's `depends_on` from front matter (39/39 files carry front matter; all `depends_on` targets resolve — 0 unresolved), computed unsatisfied edges, then collected every clause identity those loaded modules cite from the unsatisfied contracts and checked whether it appears anywhere in the fixture.

- **10 of 10 fixtures leave at least one direct edge unsatisfied** (44 unsatisfied edges total; range 1–7 per fixture).
- Cited-but-never-enumerated clause identities: fx1 41/43, fx2 50/51, fx3 40/41, fx4 19/19, fx5 40/42, fx6 20/20, fx7 7/7, fx8 54/54 — versus **fx9 1/13 and fx10 6/17**. **Total 278 across the ten.**

The split is bimodal, not a gradient: fixtures 9 and 10 enumerate at clause granularity (92% and 65% covered); fixtures 1–8 enumerate essentially none (0–5%), disposing of omissions at *contract* granularity instead ("RFC-0001, RFC-0006 — anchor and selection semantics are restated at authoring strength…").

Two readings of "cite" are available and neither is excluded by the text: the literal one (every `RFCn-m` token in the loaded module — 278 items outstanding) and a reliance-only one (which the repository's own verification rule 5 endorses — *"A citation is not a reliance"* — but which rule 2 does not say). The clause says **cite**. Two independent selectors, each reading honestly, produce mandatory sets and omission registers that differ by two orders of magnitude. **Answer to the operability question: no, they do not terminate on the same packet.**

### B3c — RFC11-16 is exercised by 0 of 10 goldens, and its trigger term has no representation in the corpus.

**Anchor,** RFC11-16 first sentence, quoted:

> "Where a selected clause, module, or the task's declared seam is the target of a clause-anchored `constrains` relation, the mandatory set includes the **constraining clause** — not automatically the entire constraining contract."

**[Observed], denominator 11 fixture files.** The tokens `constrains`, `RFC5-3` and `RFC7-3` appear **zero times** in any of them. Every one of the 38 `seam` hits refers to the OpenSpec seam or a domain seam; none is a `constrains` seam. RFC11-16 is applied nowhere in the acceptance test.

**[Observed], denominator 39 modules.** Exactly two carry the relation: `RFC-0005/admission-and-boundary.md` (`constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]`, `constrains_source: RFC5-3`) and `RFC-0007/narrative-contract.md` (`constrains: [RFC-0001, RFC-0002, RFC-0004, RFC-0008]`, `constrains_source: RFC7-3`). The relation is **clause-anchored on the source side and contract-targeted on the target side.** RFC11-16's trigger is phrased over *clause / module / declared seam* targets. Two readings result:
- **Contract-level targeting:** selecting any module of a listed contract triggers the rule. Tested mechanically: **8 of 10 fixtures** select a constrained contract without loading the constraining clause's home — fx2, fx3, fx5, fx7, fx9, fx10 (and fx3, fx10 doubly). All eight are then non-conforming, and none disposes of it in the omission register.
- **Strict clause-anchored targeting:** no target is a clause or a module, so the rule **never fires on this corpus**, and RFC11-16 is inert.

There is also no `seam` key in any of the 39 files' front matter and none in `05-CONTRACT-INDEX.yaml`, so *"the task's declared seam"* has no declared representation anywhere.

**Repair for B3 (all three limbs):** these are fixture and clause-precision repairs, not deletions. (1) Apply RFC11-15's basis sentence uniformly across all ten fixtures and correct fixture 6's false metadata claim to fixture 9's accurate one. (2) Pick one meaning of "cite" in RFC11-14 rule 2 — I recommend narrowing to *reliance* and saying so, consistent with the repository's own verification rule 5 — then bring all ten omission registers to that standard. (3) Either state in RFC11-16 that a `constrains` target list at contract granularity triggers the rule for any selected module of a listed contract, or define clause/module-level targeting and re-encode the two existing relations; then add at least one fixture that exercises it. (1) and (2) touch the C2 digest; all three require re-offering C2.

---

# FINDINGS — major

## M1 [MAJOR] RFC11-14 rule 3 names a marking mechanism that does not exist anywhere.

**Anchor,** RFC11-14 item 3, quoted in full:

> "3. **No silent transitivity.** Traverse beyond direct edges only where an edge is explicitly marked transitive."

**[Observed], denominator 39 modules.** The string `transitiv` occurs **5 times**: three in `RFC-0010/effects-recovery-and-stop.md` about independence and stop propagation (unrelated), and two inside rule 3 itself. `05-CONTRACT-INDEX.yaml`: **0 occurrences**. No front-matter key, no index field, no validator, no example. The corpus has no way to mark an edge transitive, and the module does not say where such a mark would live.

Today the rule is vacuously satisfiable — no edges are marked, so every conforming selector traverses zero transitive edges and they agree. But the rule is inoperable the moment anyone tries to use it, and a selector cannot verify the absence of markings it has no schema for. Contrast RFC11-16's `constrains`, which at least has a declared field with a defined companion (`constrains_source`).

**Repair:** either (a) define the marking — e.g. `depends_on_transitive: [RFC-000n]` in module front matter — and add a `check_governance.py` predicate with a `--selftest` fixture that fails on a malformed mark; or (b) restate rule 3 as an absolute V0 prohibition ("no transitive traversal at V0") and move the marking mechanism to a numbered §8 open question. (b) is the smaller change and matches the corpus's actual state.

## M2 [MAJOR] RFC11-15's required ownership metadata does not exist, in any of the three fields it requires.

**Anchor,** RFC11-15 first sentence, quoted:

> "**RFC11-15. Doctrine and craft rule ownership is declared, not judged.** Selection of doctrine rules and craft policy clauses consumes deterministic **ownership metadata**: for each rule identifier, at minimum, the owning authoritative artifact, the task classes it applies to, and the risk classes that make it mandatory."

**Measurements.**
- Denominator 16 (6 doctrine + 10 craft-and-care files): **none carries front matter at all**; `ownership metadata` — 0 occurrences; `task class` — 0; `risk class` — 1, incidental prose in `engineering-bar.md`.
- `05-CONTRACT-INDEX.yaml` `governance_sources`: **24 rows**, each exactly `{file, role, words, rule_ids}`. Inverting them gives **66 distinct rule identifiers**, of which **31 (47%) appear in more than one file** (CC-BAR-1 in 4, CC-REV-1 in 4, VIS-1 in 8, …). So field 1 — *the owning authoritative artifact* — is **not resolvable** for nearly half the rules. `task_class`: **0 occurrences** in the index. `risk_class`: **0 occurrences**. Fields 2 and 3 are absent for **all 66**.
- Denominator 56 (39 modules + TERM-REGISTRY + 6 doctrine + 10 craft): `task class` appears **twice**, both inside RFC11-15 itself. The clause introduces a term the corpus never defines. `risk class` / `change class` appear on 7 lines across the 39 modules, none of them a closed vocabulary; `RFC-0010/prevention-envelope-and-attention.md` bounds *"permitted **change classes**"* without enumerating them.

So RFC11-15's positive requirement is satisfied for **0 of 66 rule identifiers**, and its fallback limb is the entire operative content of the clause today. The module's §1 scope line advertises the clause as *"doctrine and craft ownership metadata (RFC11-15)"* without saying the metadata does not exist. That is the honesty limb doing all the work while the framing implies a mechanism. Note the module does carry the honest limb — this is a disclosure defect, not a dishonest clause.

**Repair:** add one sentence to RFC11-15 or the module's §1 stating plainly that no conforming ownership metadata exists in the corpus as of acceptance, so the fallback governs all doctrine/craft selection at V0; and open a numbered §8 question for the metadata's home and schema. Alternatively define the schema and extend `build_contract_index.py` to derive it — a much larger change, and one the acceptance record does not currently promise.

(part 2/3 ends)

RD-23 — Wave C2 exact-package review (part 3/3)

## M3 [MAJOR] The acceptance record's account of the budget evidence is stale by a factor of ~2 — and that evidence is what RFC11-11 rests on.

**Anchors.** Acceptance record §3, quoted:

> "The optimization target it served instead: measured per-task mandatory load **10,854–18,302 words** (five fixtures; median ≈ 13,900 ≈ 18.7k est. tokens ≈ 9–15% of the rev9 path), with one disclosed risk-class exception (fixture 2)."

RFC11-11, quoted:

> "a normal bounded implementation task should receive a packet well below whole-corpus size, with sharding or explicit exception (owner-visible, reasoned) when risk genuinely requires more."

**[Observed], denominator 10.** I extracted each fixture's own anchored `Measured:` figure: 14,112 / 18,377 / 14,233 / 10,917 / 21,174 / 11,528 / 16,098 / 22,904 / 24,635 / **35,667**. Range **10,917–35,667**, median **17,237.5**, n = **10**. The generated `CONTEXT-BUDGET-REPORT.md` §1 agrees exactly and adds: *"**6 of 10 fixtures are above the proposed 20,000-token trigger.**"* Corpus total is 110,081 words (verifier), so fixture 10 alone is **32% of the whole corpus**.

The record therefore tells an owner: five fixtures, top 18,302, one exception. The bytes say: ten fixtures, top 35,667 (**1.95×** the record's stated maximum), **six** breaching the proposed trigger. Neither of the record's endpoints is any fixture's figure. `verify_final_prespec.py`'s comment carries the same fossil (*"Context-selection fixtures: five…"*).

This is not a cosmetic staleness. §3 is the record's **only** statement of the evidence supporting RFC11-11 — the budget-posture clause Wave C2 binds — and it points in the opposite direction from the evidence. It is the exact class RD-8 caught twice in this same section, and the exact shape of verification rule 3: *a figure quoted outside its owning artifact goes stale silently.*

**Repair — digest-stable, no re-offer needed.** Record §3 itself states *"Only edits under `rfcs/` churn digests; fixes to this record or the reports do not."* Replace the whole clause with a pointer: "measured per-task mandatory load: see `CONTEXT-BUDGET-REPORT.md` §1, which is regenerated and states the current range, median, and the count above the proposed trigger." Do not transcribe the new numbers — that is how this one died. Also fix the stale "five" in `verify_final_prespec.py`'s comment and consider raising its `need ≥5` floor to the actual population.

## M4 [MAJOR] The acceptance record's C2 row states no dependency on C1, while the module leans on C1 ten times.

**Anchors.** Record §1 preamble: *"**Nothing adopts implicitly**: each gate below is independent, none implies another, and no artifact rides on another's gate."* Row B: *"Depends on Wave A…"*. Row C1: *"Declares `depends_on` RFC-0010 (waves D1/D2): recommended after them"*. Row C2 states **no ordering or dependency of any kind**.

**[Observed].** The C2 module references Wave C1 clauses **10 times**: RFC11-1 ×2, RFC11-5 ×1, RFC11-6 ×3, RFC11-7 ×4. Its fail-closed limbs are all C1 clauses — RFC11-4: *"a selected contract with no implementation-boundary declaration renders the packet **incomplete under RFC11-6**"*; RFC11-13: *"makes every packet selecting that contract **incomplete (RFC11-6)**"*; RFC11-14 item 8: *"the packet is incomplete (RFC11-6)"*. Further, RFC-0011's own `implementation_boundary` declaration — the thing RFC11-13 obliges a selector to consume — lives in `rfcs/RFC-0011/README.md`, a **Wave C1** file. C2's front-matter `depends_on: [RFC-0002, RFC-0010]` cannot express this, because C1 is the same contract.

C2 is the only wave row with no dependency statement, and it is the wave with the strongest intra-package reliance. Under the record's "each gate is independent" rule, an owner could lawfully perform C2 alone and bind a module whose every incompleteness consequence points at unbound text.

**Repair — digest-stable.** Amend the record's C2 row: "Depends on Wave C1 — cites RFC11-1/5/6/7, and RFC-0011's own implementation-boundary declaration (which RFC11-13 obliges selectors to consume) lives in the C1 package index. Perform after C1."

## M5 [MAJOR] RFC11-12's coverage matrix, as defined, excludes exactly the four clauses Wave C2 adds.

**Anchors.** The defined clause RFC11-12 (Wave C1 file `packet-identity-provenance-and-memory.md` §2.5), quoted: *"At surface specification a clause-to-requirement coverage matrix over **RFC11-1..RFC11-12** is produced — **that matrix is review material, never authority**."* The package index README (also C1), quoted: the matrix *"must cover **RFC11-1…RFC11-16 across both modules**, not module 1 alone."*

Per repository verification rule 8, the defined clause is the anchor and the index is not. So the **binding** coverage duty stops at RFC11-12, and RFC11-13, 14, 15, 16 — precisely the four clauses Wave C2 introduces — fall outside it. The README's sentence reads like a repair that never reached the clause.

This is a C1-file defect, but it is *about* C2's clauses and only visible from C2's side. Raise it **before** C1 is performed: after act 5 it cannot be fixed without a C1 re-quote and re-review.

**Repair:** amend RFC11-12's range to `RFC11-1..RFC11-16`, regenerate the C1 manifest, re-offer C1.

## M6 [MAJOR] RFC11-11 binds an enforcement duty to a governing policy that does not exist and whose existence is an open question.

**Anchor,** RFC11-11 first sentence, quoted: *"Packets carry a **size estimate** (words/tokens) and **the compiler enforces the governing policy's budget posture**…"*

No such policy exists. README §7 defers *"the numeric token budget (policy default, evidenced in the load map)"*, and §8 q1 asks whether it should be *"recorded as a named policy artifact at V0, or left to the OpenSpec phase."* The module then names its evidence as *"the rev10 context-load map and context-selection fixtures (**delivery-packet evidence artifacts, not part of this contract**)"* — the same unbound artifacts as B2.

The clause is careful — its `[Inferred]` label and the "What binds here" sentence are honest, and the two duties that do bind (exceeding the posture is disclosed; budget pressure never drops mandatory context; the non-shardable core) are self-contained and operable. But the owner should see plainly that accepting C2 accepts an enforcement verb pointed at Unknown. Combined with M3, the evidence the owner is shown for this clause is also wrong.

**Repair:** state in RFC11-11 or the record's C2 row that no governing budget policy exists at acceptance and that the enforcement limb is inert until §8 q1 is ruled.

---

# FINDINGS — minor

**m1.** RFC11-13's `none` and `craft-policy` limbs have **zero instances**. [Observed], denominator 11: every `implementation_boundary` declaration in the corpus is `kind: requires-openspec`, and all 11 named clauses (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12) exist as defined bolded clauses. So both alternative limbs are untested by corpus and fixtures alike, and the `craft-policy` limb would route a contract's implementation boundary into craft policy — in force at this position (owner-approved D2, clause force from act 1), so **no unbound reach**, but its own amendment CC-TEST-2 is a separate later act. Worth a sentence of disclosure; not a blocker.

**m2.** Package self-description inaccuracy. The record's C2 row says the fixtures' boundary *"exists to allow"* a derivation — true. The module says *"the acceptance criterion is stated with the fixtures"* — false (B1). The record is the more honest of the two; the module should be brought down to it.

**m3.** `verify_final_prespec.py`'s fixture check is a stale count floor (`need ≥5`, comment says "five") against a population of ten. Outside every digest set; fix opportunistically.

---

# Answers to the assigned questions

**(a) Where is the criterion written?** Nowhere. Sweeps of 11 fixture files and 101 candidate-tree files find no pass/fail standard; the only mechanical fixture predicates are a measurement-freshness check (CG-18, 20 measurements) and a count floor (≥5). A finding about the offering, not the fixtures.

**(b) Are the traversal rules individually operable — can two independent selectors terminate on the same packet?** **No.** Rule 1 (start) and rule 6 (termination — *"a module, clause, or artifact enters the mandatory set once"*) are operable and unambiguous. Rules 7–9 are operable as duties. Rule 2 is ambiguous by two orders of magnitude (B3b, 278 outstanding identities, goldens split 2-vs-8). Rule 3 references a marking mechanism with zero corpus representation (M1). Rule 4 / RFC11-16 admits two readings that differ on 8 of 10 fixtures, and its trigger term has no declared form (B3c). Rule 5 (*"Never traverse `cites` automatically"*) is operable and, notably, sits in tension with rule 2's use of the word "cite".

**(c) Outward references.** All land in bound material at position 6. The module's only outward clause reference is **RFC3-16** (Wave A ✓); its C1 references are RFC11-1/5/6/7 (act 5 ✓); doctrine VIS-7 and SEC-2 (adopted ✓); `depends_on: [RFC-0002 (A ✓), RFC-0010 (D1/D2 ✓)]`. **Zero topology mentions.** Craft is mentioned 9 times but only as the `craft-policy` limb's category (m1), with no CC-clause citation — `CC-[A-Z]+-\d+` matches zero. The undeclared-metadata reach is real but internal: RFC11-15 consumes metadata that does not exist (M2) — and the module **does** carry the honest fallback, though its §1 framing does not.

**(d) Does the acceptance record describe Wave C2 accurately?** Partly. The argument, manifest pointer, and clause set (RFC11-4, 11, 13..16) are exact and match the module's front matter and the README clause map. Two defects: the C2 row omits the C1 dependency the module relies on ten times (M4), and §3's budget-evidence paragraph — the only evidence shown for RFC11-11 — is stale by ~2× and cites a five-fixture population that no longer exists (M3). Package self-descriptions are otherwise accurate for the C2 set.

---

# Summary for the owner

Wave C2's **mechanics are clean**: one file, digest verified three ways, partition of RFC-0011 exact, battery 0 FAIL, verifier PASS. What is not clean is the thing the module itself says must be clean before it may be accepted. The module makes its own acceptability conditional on reproducing the blind golden fixtures; the criterion for "reproduce" is written nowhere, no derivation result is recorded anywhere, the fixtures are outside every manifest so the act cannot freeze them, and the ten goldens disagree with each other on three of the module's six clauses. Two of those six clauses (RFC11-14 rule 3, RFC11-15) name mechanisms with zero representation in the corpus. Act 6 cannot be a knowing act in this state.

Every repair is bounded and known. Four (M3, M4, and the record-side halves of B2/M6) are digest-stable edits to the acceptance record. The rest require re-offering C2, and M5 requires re-offering C1 — which is why M5 must be raised before act 5, not after.

Method note: all greps run through Python `re` or `grep -F`, never the system ugrep. Every absence claim above carries its swept denominator. All digests scripted. All check results read from output, never exit code.

VERDICT: REVISE
