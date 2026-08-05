# REV10 review — human digestibility and context (directive §13.2)

**Reviewer role:** technically capable newcomer, no prior exposure to this project, no authoring context, no rev9 memory.
**Verdict: EXCEPTIONS** — 4 substantive, 4 nits. None invalidate the compaction's core claim; one materially undercuts the argument that Tier-2 extraction is reader-safe, and one undercuts the claim that mandatory selection is deterministic from the index.

---

## Test 1 — cold-start navigation (entry points: `00-README.md`, `06-CONTEXT-LOAD-MAP.md`, `05-CONTRACT-INDEX.yaml` only)

All five targets found. Lookup paths and friction, verbatim:

**(a) The clause forbidding an agent widening its own budget → RFC10-8, `rfcs/RFC-0010-mission-control-autonomy.md:159`.**
Path: `06`'s reader map line 36 ("Mission Control / CLI / MCP spec author: RFC-0010 …") → `grep -i budget 05-CONTRACT-INDEX.yaml` → line 444 `tags: [autonomy, human-control, budgets, escalation, platform]` under RFC-0010 → open the single 2,453-word module → §1 summary line 44 names "the autonomy envelope and the no-self-widening rule (RFC10-7..9)" → RFC10-8. **3 steps, ~2,500 words read.** [Observed] Lowest-friction of the five: the module's own §1 acts as a clause-level table of contents, which the index does not provide.

**(b) The rule for a work item's substrate status with no mapping → RFC8-14 (+ the `state-undetermined` row of RFC8-13's absence table), `rfcs/RFC-0008/state-vocabulary-and-cost.md`.**
Path: `grep -i substrate 05-CONTRACT-INDEX.yaml` → **zero hits**. Fell back to `governs:` semantics → RFC-0008 `governs: [work, work-states, …]` → `module_ranges` → `state-vocabulary-and-cost.md` = RFC8-12..RFC8-20 → open a 3,507-word module → find RFC8-14. **4 steps, ~3,500 words.** [Observed] **Friction: the word "substrate" appears nowhere in `05-CONTRACT-INDEX.yaml`** — not in a `governs`, `tags`, or clause entry — despite being the operative noun in RFC8-12/13/14 and in fixture 2's own title. A newcomer searching the index by the term the task uses gets nothing and must already know that "substrate status" is a work-state concept. `06`'s reader map ("Adapter author: … RFC-0008 state/cost") rescues it. Not blocking; the single highest-value one-word index improvement available.

**(c) Which module governs egress consent → `rfcs/RFC-0005/consent-egress-secrets.md` (RFC5-12..RFC5-17; the choke point is RFC5-14/RFC5-15).**
Path: `grep -i egress 05-CONTRACT-INDEX.yaml` → line 191 `governs: [… consent, egress, secrets …]` under RFC-0005 → line 199 `module_ranges: {file: RFC-0005/consent-egress-secrets.md, clauses: "RFC5-12..RFC5-17"}`. **2 steps, no module read required to answer "which module."** [Observed] Cleanest path in the set — `module_ranges` plus a topic-named filename is the pattern that works.

**(d) The nine typed selection-resolution outcomes → RFC6-5 table, `rfcs/RFC-0006-cross-surface-selection-query-drawer.md:124`.**
Path: `grep -i resolution 05-CONTRACT-INDEX.yaml` → line 231 `governs: [selection-reference, url-identity, resolution-outcome, …]` under RFC-0006, single file → open 4,174 words → §0 reader map line 38 says "nine typed resolution outcomes" → §3.2 RFC6-5. **3 steps.** Table verified: nine rows (`resolved`, `resolved-absent`, `retired`, `unknown`, `not-applicable`, `excluded`, `unconsented`, `unresolvable`, `incompatible-scenario`). No friction.

**(e) Chat transcripts are not project memory → RFC11-8, `rfcs/RFC-0011-context-compiler.md:132`.**
Path: `grep -i memory 05-CONTRACT-INDEX.yaml` → line 466 `governs: [context-packets, context-selection, governed-memory, agent-profiles]` under RFC-0011, single file, 1,880 words → §3.3. **2 steps.** No friction. Also stated in the RFC's §0 reader summary, so a skimmer finds it.

**Structural friction shared by all five:** the index's `clauses:` blocks carry `{id, module, kind}` and **no clause topic**. That is sufficient to answer "which module?" but never "which clause?" — every lookup terminates in reading one whole module. That is the deliberate design (the module *is* the load unit), and with a ~3,000-word mean it is affordable. It stops being affordable at RFC-0001 (8,352 w) and RFC-0009 `semantic-geography` (6,999 w). [Inferred] A `topic:` string per clause would remove the last read step at essentially zero load cost; I record it as a recommendation, not an exception.

---

## Test 2 — package usability, clause-lookup rule determinism

**RFC-0005** (four ranges, non-monotonic — 24–26 folds back to module 1). Rule at `rfcs/RFC-0005/README.md:51-57`. Five IDs tested, predicted vs. actual definition site:

| ID | Rule predicts | Actually defined in | |
|---|---|---|---|
| RFC5-4 | admission-and-boundary | admission-and-boundary | ✓ |
| RFC5-13 | consent-egress-secrets | consent-egress-secrets | ✓ |
| RFC5-17 | consent-egress-secrets | consent-egress-secrets | ✓ |
| RFC5-19 | execution-profiles | execution-profiles | ✓ |
| RFC5-25 | admission-and-boundary | admission-and-boundary | ✓ |

**5/5.** The README additionally pre-empts the one trap in the package — "RFC 0005 has **no lettered sub-clauses**: limbs such as RFC5-18(a)–(e) are list items inside one clause body" — which is exactly the ambiguity a newcomer would otherwise burn a search on.

**RFC-0003** (the hardest rule in the package: module 2's clause set is deliberately non-contiguous, RFC3-15…RFC3-17 plus every lettered sub-clause). Rule at `rfcs/RFC-0003/README.md:37-50`, stated twice — once as an enumeration, once as "numeric part in 15–17 → governance-homes; otherwise → manifests-and-namespace."

| ID | Rule predicts | Actually defined in | |
|---|---|---|---|
| RFC3-2 | manifests-and-namespace | manifests-and-namespace:107 | ✓ |
| RFC3-15(a) | governance-homes | governance-homes:92 | ✓ |
| RFC3-16(b) | governance-homes | governance-homes:239 | ✓ |
| RFC3-24 | manifests-and-namespace:368 | manifests-and-namespace:368 | ✓ |
| RFC3-32 | manifests-and-namespace:464 | manifests-and-namespace:464 | ✓ |

**5/5**, and I confirmed the negative: `grep '^\*\*RFC3-1[5-7]' manifests-and-namespace.md` returns nothing, so no clause in the 15–17 run leaks into module 1.

Spot-check of RFC-0009's lettered-sub-clause carve-out: RFC9-9(b) → `semantic-geography.md:244` (module 1, with parent RFC9-9) ✓; RFC9-47(a) → `interaction-parity-and-release.md:202` (module 3, with parent RFC9-47) ✓.

[Observed] All seven package READMEs carry a lookup rule, and all seven READMEs are in `ACTIVE-CONTRACT-MANIFEST.txt`, so the rules survive installation. **This part of the design works.** It is the strongest thing in the package from a newcomer's seat: a cited `RFCn-m` genuinely resolves without search.

---

## Test 3 — RFC-0010 and RFC-0011 read cold, end to end

Both are comprehensible without rev9 history. Both open with a non-normative §0 reader's summary that states the load-bearing rule in plain language before any clause; both close with "New at rev10 — no rev9 predecessor," which is precisely the sentence a newcomer needs. RFC-0011's `2,453`/`1,880` word sizes mean a reader can hold either entirely. I found no place where the *rule* was unintelligible without outside material.

Points where comprehension reached outside the file, each judged:

| # | Where | Reaches for | Judgment |
|---|---|---|---|
| 1 | RFC-0010:18, RFC-0011:18 (Status boilerplate) | "the independent **A1** correlation mechanism" | **Acceptable citation, with a caveat.** `A1` is an owner-decision ID, defined nowhere in RFC-0010/0011. It resolves at `rfcs/RFC-0003/governance-homes-and-owner-acts.md:224` ("mechanism class at acceptance (decision A1…)") — findable, but only if you already know to look in RFC-0003. The paragraph is intelligible without it (the two-state model is stated inline), so not a defect. |
| 2 | RFC-0010:23, RFC-0011:24 | `OD-R10-1..4` at `final-prespec/02-OWNER-DIRECTION-RECORD.md` | **Defect after installation** — see E1. Inside the packet it resolves (OD-R10-1…7 are headed sections there). |
| 3 | RFC-0011:54 | finding **F7** at `01-REV9-ADVERSARIAL-FINDINGS.md` | **Acceptable citation.** This is the one place that names rev9 history, and the sentence carrying it states the gap in full ("The rev9 corpus offered no answer to 'which context did this agent receive?'"). Comprehension does not require opening F7. Post-install the path dangles (E1). |
| 4 | RFC-0011:173, :246 | the working budget figure "lives in `06-CONTEXT-LOAD-MAP.md`" | **Defect after installation** — see E1. This one is worse than the others: it is the only place a reader learns where the budget posture's actual number lives, and the clause deliberately declines to state it inline. |
| 5 | RFC-0010:61 | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` | **Defect after installation** — see E1, though softened because the same sentence states the consequence of declining ("this contract's reading … stands only as far as doctrine already permits"). |
| 6 | RFC-0010:22, RFC-0011:22 | VIS-4/5/7, SEC-1..5 | **Acceptable.** Doctrine home is given in `00-README.md:32`. Not in `05-CONTRACT-INDEX.yaml` — see E2. |
| 7 | RFC-0010:300-306 | RFC8-12 normalized work state, RFC8-28 chain state, RFC8-30 `reconciled@E`, `closed-unmerged` | **Acceptable and well-handled.** The §5 integration bullet restates the obligation at binding strength ("consume **two fields** … never folded into one"), so a Mission Control reader gets the constraint without loading RFC-0008. Fixture 5 relies on exactly this and is right to. |
| 8 | RFC-0010:264, RFC-0011:188 | "Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52" | **Acceptable.** Pure cross-reference; the phase rule is stated in full locally. All four resolve via the index. |
| 9 | RFC-0011:85 | "every resulting **Execution Record** (RFC 0008 / RFC 0002 evidence)" | **Nit.** Cited by RFC number, not clause ID, unlike every neighbouring citation. Costs a newcomer one extra module read to find RFC8-18–8-20. |

**Judgment on the pair:** both RFCs are the most reader-friendly documents in the corpus. If the rest of the package read like these two, this review would be a clean ACCEPT.

---

## Test 4 — load-map fidelity (fixtures re-measured)

I re-ran **all five**, not the required two, from the packet with `python3 scripts/context_load.py`:

| Fixture | Claimed | Measured | |
|---|---|---|---|
| 1 Polaris narrative | 13,806 w / 18,638 tok | 13,806 / 18,638 | ✓ |
| 2 Trajectory adapter | 18,175 w / 24,536 tok | 18,175 / 24,536 | ✓ |
| 3 Orrery lens | 14,134 w / 19,080 tok | 14,134 / 19,080 | ✓ |
| 4 Execution profile | 10,728 w / 14,482 tok | 10,728 / 14,482 | ✓ |
| 5 Cross-project Mission | 11,684 w / 15,773 tok | 11,684 / 15,773 | ✓ |

I also recomputed two packet digests independently (`cat <files in listed order> | sha256sum`): fixture 2 → `5117434a89aaba10…` ✓, fixture 5 → `1fb5a5eeb05306eb…` ✓. And `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` → 32/32 OK; the manifest's own digest is `b77374b8080a7082f486248c05b54e38cdd460f30a6d7da627f026b57fb0d6fb`, matching act 1's argument in the acceptance record §1. `scripts/verify_final_prespec.py` → PASS; `scripts/build_contract_index.py --check` → "no drift". **[Observed] Every measurement claim in this package that I checked reproduced exactly.** That is unusual and worth saying plainly.

**Omission arguments, judged as a newcomer:**

- **Fixture 2's exception is the strongest artifact in the set.** It states the overrun, names *why* trimming would be unlawful (RFC11-5), names the lawful alternative (shard the mapping edit from the approval ceremony), and says explicitly "this fixture shows the undivided form with the exception stated rather than hidden." A newcomer reading only this file understands the budget posture. Convincing.
- **Fixture 1's dropping of RFC-0001** ("anchor and selection semantics are restated at authoring strength inside RFC7-11/11(a)/16") is checkable and checks out — `RFC7-11(a)` appears 8× in `narrative-contract.md`. Plausible.
- **Fixture 5's mandatory/suggested split on RFC-0008** ("at approval time the mission authorizes future materialization; the work-state contract binds when work items exist … when the mission starts running, RFC-0008 becomes mandatory") is the clearest statement of *time-varying applicability* in the package. Plausible and instructive.
- **One overstatement, fixture 3:** "Performance and motion bounds (RFC9-49..51) travel in the README's package map and load on demand." [Observed] The RFC-0009 README's package map mentions RFC9-49 only ("truth is never purchased with frame rate"); RFC9-50 and RFC9-51 appear nowhere in that README except inside the range string "RFC9-1…RFC9-51". The omission is independently justified two sentences later ("the fixture's warrant does not alter frame or motion budgets"), so nothing is lost — but the supporting sentence is not accurate. Nit E8.

---

## Test 5 — module structure judgment

**Not fragmented.** 25 normative modules across 11 contracts, mean 3,409 words, median ~2,700. No module exists that a reader would have to open together with a sibling as a matter of course — I checked the seams the READMEs name (RFC-0007's "no clause spans the seam" with seven enumerated crossing citations; RFC-0003's five package-spanning items each stated once and cited from the other). I found no ceremonial multiplication: every split lands on a reader group named in `06`'s reader map, and every README's reader-group text is specific enough to act on (RFC-0008's is the best: "Adapter and endpoint authors read module 2. Board, queue, and aggregate implementers read module 3.").

**Still monolithic — two:**

- **RFC-0001, 8,352 w, single.** The justification (verifier note + 03 report §"Risks accepted" item 3): "dictionary-shaped kernel contract: 23% verbatim closed vocabularies …; reader groups not distinct, so no honest split exists; floor established by two compaction passes." **From a reader's seat: convincing, with a residual I want on the record.** Convincing because (i) the ten §3 subsections are genuinely a single dictionary — §3.6's state planes, §3.7's closed relation vocabulary and §3.5's two-level claim identity are mutually defining, and the four "load-bearing ideas" in §1 each span three subsections; (ii) the honesty is real — it is stated as a floor, not a success; (iii) **the empirical answer is the strongest argument and the report does not make it**: RFC-0001 is mandatory in *zero* of the five fixtures. Surface, adapter, security, and Mission Control work never loads it. It is an 8,352-word load for kernel tasks only, which is the one reader group that genuinely needs the whole dictionary. Residual: §3.10 "No Feature entity" (13 lines) and §3.9 "Entity lifecycle" (37 lines) are visibly separable, and a `topic:` field per clause in the index would let a non-kernel reader cite into RFC-0001 without loading it. I would not require a split.
- **RFC-0009 `semantic-geography`, 6,999 w** against a stated 7,000-word ceiling. [Observed] one word under. I make no accusation about how that number arose, but it is the second-largest mandatory load in the corpus, it carries no oversize justification because it does not trip the check, and it is mandatory for every Orrery geography task. [Inferred] A ceiling a module lands one word beneath is not doing enforcement work on that module. Recording as a friction observation, not an exception.

---

## Exceptions

### E1 — 75 references from installed modules point at material act 1 explicitly does not install *(substantive; blocks the "reader-safe Tier-2 extraction" claim, not the act)*

**Where:** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15` — act 1 accepts "The 32 active contract modules … **Nothing else — not history/, not fixtures/, not the reports**"; §2 step 3 (line 42-48) installs "the 32 modules (with their package directory structure) plus `ACTIVE-CONTRACT-MANIFEST.txt` to `.syzygy/governance/contracts/rfcs/`."

**The count, by grep over `rfcs/`:** 68 `history/` backlinks + 1 `matrix-rows/` + 6 packet-report references = **75**.

- 68 history backlinks: `../../history/RFC-0008-history.md` ×14, `RFC-0004` ×12, `RFC-0002` ×12, `RFC-0005` ×10, `RFC-0009` ×7, `RFC-0007` ×6, `RFC-0003` ×3, `../history/RFC-0006-history.md` ×2, `../history/RFC-0001-history.md` ×2.
- `rfcs/RFC-0003/README.md:120` → `../../matrix-rows/RFC-0003-rows.md`.
- `rfcs/RFC-0010-…:24` and `rfcs/RFC-0011-…:24` → `final-prespec/02-OWNER-DIRECTION-RECORD.md`; `rfcs/RFC-0010-…:61` → `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`; `rfcs/RFC-0011-…:173` and `:246` → `06-CONTEXT-LOAD-MAP.md`.

**Why it blocks the claim.** All 75 resolve correctly *inside the packet* — I verified path arithmetic for both the package form (`../../history/` from `rfcs/RFC-0002/README.md`) and the single-file form (`../history/` from `rfcs/RFC-0001-….md`). After step 3 they all dangle: `../../history/` from `.syzygy/governance/contracts/rfcs/RFC-0008/README.md` resolves to `.syzygy/governance/history/`, which nothing creates. The 03 report's stated mitigation for its own accepted risk 2 — "a reader who skips the stub's decision cite reads less context than rev9 offered — **mitigated by verbatim answers one link away**" — is the mitigation that stops existing at installation. 27,521 words of extracted rationale become unreachable from the governed tree, and `rfcs/RFC-0005/README.md:229-241` (the q1-q6 table, which routes to `history §q2`, `§q3`, `§q6` for three answered owner decisions) becomes a table of dead ends. RFC-0011's budget-figure pointer (case 4 above) is the sharpest instance: the clause declines to state the number and points at a file that will not be there.

**Does not block the act itself** — the 32 modules are self-contained normatively; the verifier's "all citations resolve" check is about clause IDs, which do resolve. This is a packaging decision, and the fix is a decision, not a rewrite: either install `history/` (and `matrix-rows/`) alongside as a declared non-normative sibling under RFC3-15 discipline, or rewrite the 75 links to a stable governed-tree location, or state in the acceptance record that Tier-2 rationale is deliberately packet-only and the links are historical. Any of the three closes it; leaving it unstated does not.

### E2 — `05-CONTRACT-INDEX.yaml` cannot reach doctrine, craft, or topology, yet every fixture's mandatory set includes doctrine *(substantive)*

**Where:** `05-CONTRACT-INDEX.yaml` (entire file — `grep -i "doctrine\|craft\|topology"` returns **zero hits**); `rfcs/RFC-0011-context-compiler.md:100-107` (RFC11-4: "Mandatory context is selected deterministically … from … explicit `applies_to` and clause-level metadata (RFC3-15's contract-index projection)"); `06-CONTEXT-LOAD-MAP.md:6-8` ("Machine lookup: `05-CONTRACT-INDEX.yaml`").

**Failure:** all five fixtures mandatorily load a doctrine file — `doctrine:vision.md` (2,156 w, fixtures 1 & 5), `doctrine:security.md` (511 w, fixtures 2 & 4), `doctrine:architecture.md` (2,350 w, fixture 3) — and fixture 4 additionally loads `craft:security-and-secrets.md`. The index describes none of them: no `governs`, no `applies_to`, no rule ID, no home. Consequently each fixture's "Selection rule trace (RFC11-4)" reaches doctrine by **prose judgment**, not by index metadata — fixture 1: "Shape-defining adoption gates are doctrine → `vision.md` (VIS-3/VIS-4)"; fixture 2: "The untrusted-actor premise is doctrine → `security.md` (SEC-3)". Those are good judgments. They are not deterministic selections, and RFC11-4's determinism claim is the load-bearing property of the whole Context Compiler design.

**Not blocking** because the doctrine corpus is small (six files, 7,774 w) and stable, and `context_load.py` already resolves `doctrine:` / `craft:` prefixes against the canonical homes — so the *measurement* half works. The *selection* half has no metadata to run on. The minimal fix is index entries for the six doctrine files and ten craft policies carrying `governs`/`applies_to`/rule IDs (VIS-n, SEC-n). Worth doing before the compiler is specified, because RFC11-7 forbids a hand-maintained sidecar and doctrine currently has no machine-readable front matter to project from.

### E3 — published module word counts are stale in four places, including the load map *(substantive-minor; these are the planning numbers)*

Actual `wc -w`, re-measured:

| Claim | Says | Actually |
|---|---|---|
| `06-CONTEXT-LOAD-MAP.md:22` — RFC-0009 README | 2,266 | **2,029** |
| `06-CONTEXT-LOAD-MAP.md:22` — RFC-0009 parity/release | 3,029 | **3,027** |
| `rfcs/RFC-0009/README.md:52` + its Word-accounting table — module 3 | 3,029 | **3,027** |
| `rfcs/RFC-0009/README.md` Word-accounting — modules total | 15,568 | **15,566** |
| `rfcs/RFC-0002/README.md:11` — reconciliation-chain | 2,462 | **2,477** |
| `rfcs/RFC-0008/README.md:11` — accounting-reconciliation-and-release | 3,057 | **3,055** |

Every one of these files asserts "Counts are `wc -w` at the rev10 compaction." The RFC-0009 README figure is the largest error (237 words) and it is in `06`, the file a newcomer is told to plan loads from. Note `06` and `rfcs/RFC-0002/README.md` **disagree with each other** on reconciliation-chain (2,477 vs 2,462); `06` is right there and wrong on RFC-0009. Cross-checks that came out *correct*: 03 report's "READMEs (7) +12,637 w" sums exactly using the true 2,029, and the verifier's total 97,861 matches — so the aggregates are sound and only the per-module tables drifted. Fix by generating these tables rather than maintaining them; the packet already has `context_load.py`, which is the generator.

### E4 — an active contract grounds an [Inferred] claim on a citation no reader of the packet can resolve *(substantive-minor)*

**Where:** `rfcs/RFC-0001-project-graph-identity-state-planes.md:81` — "[Inferred] The failure mode this contract guards against is the **silent default** … [Observed: `REVIEW-01-KERNEL.md` K-F1, K-F2]."

`REVIEW-01-KERNEL.md` is not in the packet, not in `final-prespec/reviews/` (empty), and not in `_bootstrap/rfc-phase/reviews/` (whose files are named `02-kernel-RAW.md` etc.). It exists only at `_bootstrap/drafts/surface-shaping/reviews/REVIEW-01-KERNEL.md` — bootstrap draft-phase material, git-excluded, machine-local, and never installed. Carried verbatim from rev9. A newcomer holding the packet reads an `[Observed:]` provenance tag pointing at a file they cannot obtain; a newcomer holding only the installed tree cannot even find the directory. Either drop the citation, or re-point it at `../history/RFC-0001-history.md` where the review-origin narrative was moved. This is the exact epistemic-label failure the corpus otherwise polices well.

### E5 — `00-README.md`, the designated cold-start entry point, is mostly a pre-rework snapshot *(friction)*

Lines 23–74 are the directive §0 preflight: rev9 digests, rev9 acceptance state, and at lines 45–51 a word-count table giving **RFC-0001 9,534** and **RFC-0009 19,269** with the header "Word counts [Observed, `wc -w`]". Those are the rev9 figures; the package this README fronts ships 8,352 and 15,566. The section is *labelled* "Preflight report (directive §0) — 2026-08-02" and the sentence framing is past-tense, so nothing is false. But a newcomer told "start at `00-README.md`" meets 50 lines of superseded numbers before reaching the deliverables map at line 77, and nothing on the table says "superseded — current figures in `06`." One line of cross-reference fixes it. Not blocking.

### E6 — `06-CONTEXT-LOAD-MAP.md:5-6` module arithmetic doesn't parse *(nit)*

"11 contracts → **32 modules** (7 packages + 2 single-file RFCs + RFC-0010 + RFC-0011 + 7 package READMEs)". The parenthetical enumerates 7+2+1+1+7 = 18. 32 is correct (25 normative modules + 7 READMEs — I counted the files), but "7 packages" is silently standing in for 25 files. A newcomer trying to reconcile the total against the list stalls. Also "mean normative module ~3,000 words" — the true mean over 25 normative modules is 3,409 (median ~2,700); "~3,400" or "median ~2,700" would be the honest figure.

### E7 — `07-AUTONOMY-EXTENSION-REGISTER.md`, "Environment/toolchain capsule" row is missing a cell *(nit)*

The table has four columns (Concept | Belongs to | Earliest gate | Classification); that row supplies three. Its classification text sits in the gate column and Classification renders blank — in a register whose entire purpose is "each `required before …` row names the gate that blocks V1 autonomy." Every other row of the eleven is complete.

### E8 — fixture 3's supporting sentence overstates the README *(nit)*

`fixtures/context-selection-3-orrery-lens.md`, "Why no applicable constraint was lost": "Performance and motion bounds (RFC9-49..51) travel in the README's package map and load on demand." The RFC-0009 README's package map covers RFC9-49 only. The omission itself is justified by the next clause of the same sentence; only the support is inaccurate.

---

## What I'd tell a newcomer this package gets right

Stated because a review that only lists exceptions misrepresents what I found:

1. **The clause-lookup rules work.** 10/10 on two packages including the deliberately non-contiguous one, plus 2/2 on RFC-0009's lettered carve-outs. A cited `RFCn-m` really does resolve without search, and the READMEs carrying the rules are inside the accepted manifest.
2. **Every number I re-derived reproduced.** Five fixtures, two packet digests, the 32-module manifest, the manifest's own digest against act 1's argument, `verify_final_prespec.py`, `build_contract_index.py --check`. Nothing was rounded in the package's favour, and the 03 report leads with the target it *missed* (the 35–50k band) rather than the one it hit.
3. **RFC-0010 and RFC-0011 are the model.** §0 plain-language summary → §1 clause-range roadmap → contract → numbered violation cases → integration by clause ID → explicit deferrals → open questions. A newcomer can read either in one sitting and act on it. The rest of the corpus would be more digestible written this way.
4. **The omission accounting is a genuine epistemic instrument**, not a formality — fixture 2 discloses its overrun and names the lawful alternative rather than trimming to fit, which is exactly the behaviour RFC11-11 demands of the runtime.

## Verdict

**EXCEPTIONS.** E1 and E2 should be resolved or explicitly ruled before the act, because each contradicts a claim the package makes about itself: E1 contradicts "rationale is one link away," E2 contradicts "mandatory selection is deterministic from the index." Neither requires rewriting a contract; E1 is a packaging decision and E2 is added metadata. E3 and E4 are mechanical fixes. E5–E8 are polish and need not gate anything.

I did not review semantic equivalence, acceptance-record mechanics, or clause-migration completeness — those are other reviewers' charters, and where I touched them (manifest verification, digests) it was only to establish that the artifacts I was reading are the ones under review.
