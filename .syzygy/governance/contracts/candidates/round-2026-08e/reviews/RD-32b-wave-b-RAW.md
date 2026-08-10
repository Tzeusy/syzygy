I have everything I need. Writing the review of record.

# RD-32b — Wave B exact-package review, second administration (round-2026-08e, frozen commit b00c3dd)

## 0. Subject identification and clone state

**Clone.** `/tmp/claude-1000/.../scratchpad/clone-08e-r14`. `git rev-parse HEAD` = `b00c3dd5542250a9999a1726ccaa90b9793be6cd`; `git status --porcelain` returned **0 lines** at the start of the session. Nothing was written, created, or deleted anywhere; every command run was read-only. The live repository at `/home/tze/GitHub/syzygy` was never read. [Observed]

**Register discrepancy, stated up front.** `reviews/DELIVERY-AND-VERDICT-REGISTER.md`'s RD-32b row names frozen commit **`36c01a9` (clone-08e-r13)**; this administration ran at **`b00c3dd` (clone-08e-r14)**. The subject bytes are unaffected: `git log ad82f1d..b00c3dd -- rfcs/RFC-0007 rfcs/RFC-0008 rfcs/RFC-0009` returns **exactly one commit** (`1a23d19`), so the 11 modules and the manifest are byte-identical at `36c01a9` and at `b00c3dd`. The row wants a dated correction (finding N-8). [Observed]

**The argument, recomputed two ways this session** [Observed]:

| Method | Result |
|---|---|
| `sha256sum wave-manifests/WAVE-B-MANIFEST.txt` | `052acfb8c54bf6b7706af2b23b7bd2a84de8a34ebe3166f4cd3b078ae49bf655` |
| Python `hashlib.sha256(open(p,'rb').read())` (via `check_governance.py` CG-7b) | matches |

**Against the record.** §1 row B reads `ACCEPT FOUNDATIONAL WAVE B: 052acfb8c54bf6b7706af2b23b7bd2a84de8a34ebe3166f4cd3b078ae49bf655` — **byte-identical**, and CG-7d independently re-verifies every act digest quoted anywhere (9 quotations, 0 findings). [Observed]

**Per-module recomputation.** Manifest rows re-hashed individually from the candidates root: **11 of 11 OK, zero mismatches** (count computed from non-comment rows, not read off the header). [Observed]

**Stale predecessors, verified by git rather than by trust** — the manifest's digest at each commit that moved it [Observed]:

| Digest | Commit | Row-B account |
|---|---|---|
| `daa6a5dd37b7f92a…` | `771965c` (round-08d) | "retiring the round-08d argument `daa6a5dd…`" ✓ |
| `2041ad053127cb1f…` | `31ebc52` (wave-wide batch) | "retiring `2041ad05…`" ✓ |
| `c0fd0e27cb309deb…` | `246af62` (RD-27 batch) | "retiring `c0fd0e27…`" ✓ |
| `052acfb8c54bf6b7…` | `1a23d19` (RD-32 batch) | current ✓ |

Three regenerations in round-2026-08e, all three predecessors named and marked "**stale and satisfy nothing**" in row B. **Accurate.** [Observed] (One count inside that row is not — finding N-3.)

---

## 1. Method

Read: the acceptance record entire; `WAVE-B-SEMANTIC-DELTA.md` §§11–12; `reviews/DISPOSITION-REGISTER.md` (RD-27, RD-32 sections); `reviews/RD-32-wave-b-RAW.md`; `reviews/DELIVERY-AND-VERDICT-REGISTER.md`; `PENDING-OWNER-DECISIONS.md` (launch-scope index and rows P-1/P-21/P-22/P-33/P-38); then the subject clauses and every sweep site in the 11 modules, plus the Wave A clauses cited against them (RFC6-14, RFC6-17, RFC6-19, RFC6-22, RFC6-23).

Every sweep was run **this session** with Python `re` — never the clone's ugrep bracket classes (rule 1) — and states its denominator (rules 2, 9). Check **output** was read, never exit codes (rule 4). Every obligation quoted is anchored to a defined clause and quoted (rule 8). Cross-wave hits were classified by reading each site (rule 5). Digests are scripted (rule 3).

---

## 2. The six RD-32 repairs, verified against the actual bytes

| # | Class | Repair claimed | Verdict at the bytes |
|---|---|---|---|
| B1 | BLOCKING | RFC9-43's enumeration restored to the full RFC6-17 set | **Closed** — with one residual (N-1) |
| M2 | MAJOR | §1 row B gains the C1-shaped solo-act sentence | **Closed** |
| M1 | MAJOR | Launch-scope index verb split | **Closed** |
| m1 | MINOR | RFC7-39 / RFC9-8(a) in-place awaiting-ruling markers | **Closed** |
| m2 | MINOR (O+R) | Disclosure only; no new `constrains:` minted | **Closed** |
| m3 | MINOR | Delta addendum §12 rather than editing §7 | **Closed** |

### 2.1 B1 — the RFC9-43 ↔ RFC6-17 identity claim

Both clauses read side by side, item by item. RFC6-17 (`rfcs/RFC-0006-cross-surface-selection-query-drawer.md`, **RFC6-17 — Aggregation discloses**) and RFC9-43 (`rfcs/RFC-0009/visual-grammar-and-lenses.md`) now enumerate the **same eleven items** [Observed]:

| RFC6-17 item | In RFC9-43? |
|---|---|
| per-label counts | ✓ |
| per-tier counts | ✓ |
| per-Unknown-reason counts | ✓ |
| per-freshness-state counts | ✓ |
| sibling surface states | ✓ |
| `challenge-pending` disclosure (RFC2-13) | ✓ (RD-27 batch) |
| per-value counts of the **chain state**, RFC6-19 class 8, where members carry them | ✓ **new** |
| per-value counts of the **normalized work state**, same condition | ✓ **new** |
| the "never … disclosing nothing about reconciliation" consequence | ✓ **new** |
| **primary-reasons-only** computation, one claim instance contributes exactly one, secondaries (RFC2-24) disclosed separately and never folded | ✓ **new** |
| the RFC6-23 release-blocking rationale for that rule | ✓ **new** |
| tier counts cover all six RFC2-25 tiers, named | ✓ |
| sibling surface states are the three RFC2-25 places outside the registry | ✓ |
| "never label and Unknown reason alone" | ✓ |

The new bytes, quoted: *"and — where the aggregate's members carry them — **per-value counts of the chain state and the normalized work state of RFC6-19 class 8**, so an aggregate can never satisfy this clause in full while disclosing nothing about reconciliation (RFC9-32 carries the element-level obligation these counts aggregate); **per-Unknown-reason counts are computed over primary reasons only** — one claim instance contributes exactly one — with secondary annotations (RFC2-24) disclosed separately and never folded into the primary counts, since divergent totals over one declared scope are exactly the disagreement RFC6-23 classes release-blocking".*

**The identity claim — "RFC6-17 binds the same enumeration at the foundation layer … so the two are deliberately identical" — is now true as written.** [Observed]

Adversarial checks on the repair itself:

- **New cross-wave reliance?** The repair adds citations to RFC6-19, RFC6-23, RFC2-24 — all Wave A, all inside `visual-grammar-and-lenses.md`'s declared `depends_on` (`RFC-0001..RFC-0006`). RFC6-19 class 8 is a real defined class and does define both fields (chain state at RFC2-18; normalized work state at RFC8-12, intra-wave). **No undeclared edge, no deferred-wave edge.** [Observed]
- **New divergence?** The added parenthetical "(RFC9-32 carries the element-level obligation these counts aggregate)" is accurate: RFC9-32 binds both fields on "every element and every aggregate that carries a normalized state," and already closes by citing "RFC9-43's aggregate-composition obligation." The two clauses now cross-reference coherently. [Observed]
- **RFC9-46's carve-out** was untouched and remains sound for its own scope; RFC9-46 independently carries chain state, normalized work state and scenario context. [Observed]
- **"Full RFC6-22 equivalence tuple" label.** RFC6-22 additionally names "the same scenario context (RFC6-24)". RFC9-43 does not count scenario context — but neither does RFC6-17, and per RFC6-24 a selection carries *exactly one* scenario context, so it is not a composition facet. **Checked and cleared; the phrasing is inherited verbatim from RFC6-17, not introduced here.** [Inferred]

One residual survives the repair and is finding **N-1** below.

### 2.2 M2 — the solo-act sentence in §1 row B

Present, quoted from §1 row B: *"**Performed alone — before act 1 — this act binds eleven surface contracts whose operative predicates (11 of 11 modules' `depends_on`; 1,067 RFC 0001–0006 clause citations, RD-32's count) resolve into unaccepted Wave A candidate text: lawful only stated at the act, and the offer path is A → B** (RD32-M2; the register's P-1 row states the same ordering)."* C1-shaped, in the row the ceremony binds. **Closed.** [Observed] The embedded figure is finding N-4.

### 2.3 M1 — the launch-scope index verb split

`PENDING-OWNER-DECISIONS.md`, "Launch-scope index," now reads [Observed]:

> "**Withholds the Wave A offer:** P-33 (install shape) — §7 item 11 states in the record's own voice that no Wave A act is offered until it is ruled. **Ratified or reverted at the Wave A act (the offer, once live, stands):** P-31 …, P-37 …, **P-28** …, and P-21(a) …. *(Verbs split 2026-08-10, RD32-M1 — "gate" had carried two different forces.)*"
> "**Ratified or reverted at the Wave B act (nothing withholds this offer):** P-38 … and **P-22** …. The acts stay sequenced A → B (P-1)."

Matches §7 items 11, 15, 17. **Closed.** One omission remains (N-6).

### 2.4 m1 — the in-place markers

Sweep for `\bP-\d+\b` over the 11 modules: **exactly 2 hits**, both new, both inside the clause they mark (verified by walking each file's clause headers): `rendering-and-surface.md:382` sits under **RFC7-39** (defined at line 369); `semantic-geography.md:143` sits under **RFC9-8(a)** (defined at line 135). [Observed]

Both name the question, the round, the ratify-or-revert consequence, the revert alternative, and the §7 item. Corpus-wide the convention now stands at **four in-place markers across Waves A+B** — P-28 (RFC-0001), P-31 (RFC-0002), P-38 (RFC-0007), P-22 (RFC-0009) — one idiom. **Closed.** [Observed]

### 2.5 m2 — disclosure, not a new front-matter edge

- `git diff ad82f1d b00c3dd` over the 11 modules touches **no front matter**; `build_dependency_index.py --check` reports **8 `constrains` edges**, matching regeneration. **No new edge was minted.** [Observed]
- §7 item 18 now reads: *"The same open ruling covers a declared-nowhere instance inside Wave B: RFC8-12 and RFC9-32 restrict each other in-clause with no `depends_on` or `constrains` edge either way (RD32-m2; intra-wave, no containment escape, and no new front matter is minted while (a) is open)."* [Observed]
- P-21's register row carries the same disclosure and adds *"RFC-0007's twin rides the Wave B act the same way."* [Observed]

**Closed** as disposed (O+R).

### 2.6 m3 — the delta addendum

Delta §7's reviewed text is **unedited**; addendum §12 carries the correction and states the true figure. My own sweep: `configured landing document`, **1 hit over 11 modules**, `rfcs/RFC-0007/rendering-and-surface.md:447`, inside RFC7-40's repair heading. **Closed, and the corrected figure is correct.** [Observed]

*(The same batch appended a dated stale-marking clause to §11's closing parenthetical. That is an annotation of a retired digest, not an edit to reviewed findings text; checked and cleared.)*

---

## 3. Mechanical battery — all run this session, output read

| Check | Output |
|---|---|
| `sha256sum -c` per manifest row | **11/11 OK**, 0 mismatches |
| `check_governance.py` | **29 OK / 19 WARN / 0 FAIL over 48 checks** |
| CG-7a | 78 entries, 0 findings; active manifest `5a426d26…` |
| CG-7b | **6 wave arguments match their manifests**, 0 findings |
| CG-7d / CG-7f / CG-7g / CG-7c / CG-7e | 0 findings each |
| CG-2a | 348 files, **2 retired phrases declared, 0 presented as current, 0 unmarked** |
| CG-4a / CG-4b | banners present; **105 files claim no acceptance** |
| CG-13 | **185 dependency edges resolve**, 0 findings |
| CG-14 | 12 install paths, 0 findings |
| CG-17 | **210 clauses routed exactly once**, 0 findings |
| CG-21 | **39 modules, contract prose states no measurement**, 0 findings |
| `verify_final_prespec.py` | **PASS**, 341 numbered clauses, 39 modules, 11 phase-rule clauses; two oversize notes, both `JUSTIFIED` |
| `build_active_manifest.py --check` | "all 7 manifests match regeneration — 7 manifests over 39 modules in 6 waves" |
| `build_contract_index.py --check` | no drift, 367 clauses |
| `build_dependency_index.py --check` | no drift, 176 `depends_on`, 8 `constrains` |
| `build_budget_report.py --check` | fixture anchors and report match regeneration |
| `build_task_router.py --check` | 12 task classes validated |

**Correction to RD-32, carried for the closure report** (finding N-7): RD-32 wrote "**No WARN names a Wave B module**." That is false. **CG-8** (WARN, report-only, 43 artifacts, 15 findings) names **six** Wave B modules as §11.4 decomposition-review triggers: `RFC-0007/narrative-contract.md` (5,253 w), `RFC-0007/rendering-and-surface.md` (4,609 w), `RFC-0008/state-vocabulary-and-cost.md` (4,135 w), `RFC-0009/semantic-geography.md` (7,818 w), `RFC-0009/visual-grammar-and-lenses.md` (5,934 w) — plus `RFC-0006` on the Wave A side. These are **review prompts, not failures**, and none is a defect; the false statement is the denominator error. CG-20's 52 findings are in `06-CONTEXT-LOAD-MAP.md`, `TASK-TO-CONTRACT-INDEX.md` and `candidates/README.md` — **no module README**, confirmed by extracting the paths from the check's own output. [Observed]

`semantic-geography.md` moved 7,777 → **7,818 words** (the 41-word P-22 marker); the verifier's justification remains `JUSTIFIED` and its text is still true of the current bytes. [Observed]

---

## 4. Sweeps, with denominators — all run this session

**Denominator throughout: the 11 modules of `WAVE-B-MANIFEST.txt`** (count computed from non-comment rows).

**4.1 Wave containment — front matter.** `depends_on` extracted from all 11: **zero edges into RFC-0010 or RFC-0011**, 11 of 11. Every out-of-package edge names RFC 0001–0006 or an intra-wave sibling. [Observed]

**4.2 Cross-wave clause tokens.** Regex `RFC(\d{1,2})-(\d+)` over all 11, every family tallied:

| Family | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tokens | 161 | 177 | 158 | 94 | 8 | 160 | 373 | 252 | 427 | **1** | **0** |

**`RFC11-n`: zero hits.** **`RFC10-n`: exactly one hit in the entire wave** — `RFC10-15`, `semantic-geography.md:178`. Read at the site: it sits inside RFC9-8(a)'s parenthetical, which states in-clause *"It is named for orientation only: **a citation, not a reliance**. If RFC 0010 is never accepted, the rule above still stands and still fail-closes."* The operative rule above it stands on RFC3-15/RFC3-16(a)/RFC3-15(a) and the clause states *"a reader holding RFC 0001–RFC 0009 can evaluate every condition this clause states."* **Classified: citation, not reliance (rule 5).** [Observed]

**4.3 Package-name tokens** `RFC[ -]00(10|11)`: **17 hits, every one read.** Four in RFC-0008 ("**To RFC 0010:**", "**To RFC 0011:**") — outbound provides-to. Seven in the RFC-0009 README — outbound provides-to, the verified-true "both RFC 0010 and RFC 0011 cite it," the "no clause of RFC 0011 is cited anywhere in RFC 0009" statement (confirmed: `RFC11-\d+` = 0 hits), and the phase-boundary sibling list. Six in `semantic-geography.md` — the staged-successor parenthetical and the §8 "**No forward reliance**" paragraph. **Zero reliances on deferred-wave text.** [Observed]

**4.4 The Wave A seam.** **758** RFC 0001–0006 clause tokens across the wave (`RFC[1-6]-\d+`, second method: 755 at `ad82f1d`, +3 from the RD-32 batch — all three inside RFC9-43's new text: RFC6-19, RFC2-24, RFC6-23). The seam is **reliance by design, wholesale**, and is disclosed in three places in the record's own voice: §1 row B's solo-act sentence ("resolve into unaccepted Wave A candidate text: lawful only stated at the act, and the offer path is A → B"), the launch-scope index, and `DEFERRED-WAVE-POSTURE.md`. **The three citations the batch added are each inside a declared `depends_on` and each anchors to a defined clause I read.** [Observed]

**4.5 Cited-but-undeclared remainders**, tallied per namespace against each module's declared `depends_on ∪ constrains ∪ self`: exactly two classes — **`RFC9-n` in three RFC-0008 modules** (README ×1, `accounting-reconciliation-and-release.md` ×3, `state-vocabulary-and-cost.md` ×2 — the m2 instance, now disclosed at §7 item 18 and P-21's row) and **`RFC10-15` in `semantic-geography.md`** (classified above). **This reproduces RD-32's remainder set exactly, by independent computation.** [Observed]

**4.6 Ceremony phrases.** Eight literal patterns (`re.escape`) × 11 modules = **88 cells, 0 hits**: `ACCEPT FOUNDATIONAL RFCS`, `ACCEPT COMPACTED FOUNDATIONAL RFCS`, `ACCEPT FOUNDATIONAL WAVE`, `CONFIRM CRAFT AMENDMENT`, `ACCEPT TOPOLOGY`, `ADOPT PROJECT OVERVIEW`, `REWORK FOUNDATIONAL WAVE`, `REJECT FOUNDATIONAL WAVE`. Neither retired phrase nor any current one is inside the digest subject. Corroborated independently by CG-2a over its own 348-file population. [Observed]

**4.7 Self-presents-as-accepted.** Three regex families over 11 modules: **0 hits.** No 64-hex digest string appears inside any module (0 hits) — no module quotes its own act argument. **11 of 11** carry all three candidate-banner strings ("Proposed foundational contract", "Absent such a record, this contract binds nothing", the RFC3-16 pointer). [Observed]

**4.8 Drafted-arm disclosure — enumerated population.** Every drafted or unruled answer riding into the Wave B act, and its §7 cross-reference:

| Arm | Site | Disclosed at | Verified |
|---|---|---|---|
| RFC7-39 entry-identity ("there are not two front doors") | `rendering-and-surface.md` RFC7-39 | §7 item 15; P-38 row; in-place marker | ✓ |
| RFC9-8(a) typed governance-store placement | `semantic-geography.md` RFC9-8(a) | §7 item 17; P-22 row; in-place marker | ✓ |
| RFC7-40's four-value answer domain | `rendering-and-surface.md` | §7 item 15 via P-38's packet | ✓ |
| RFC8-12 ↔ RFC9-32 undeclared reciprocal restriction | 3 RFC-0008 modules + RFC9-32 | §7 item 18; P-21 row | ✓ |
| Package §8 open questions (RFC7 q2/q4; RFC-0008 §8 q2 foundation defect) | package indexes | §5 (27 open §8 questions, triaged) | ✓ |
| **OQ-010** (portfolio authority) | RFC-0007 README; RFC7-36 | *not in §5's population, not in §7* | see below |

**OQ-010 checked and cleared, not raised as a finding:** RFC7-36 states in-clause *"This clause binds the portfolio narrative's **discipline** and settles nothing about where cross-project truth lives; it is compatible with every option OQ-010 leaves open."* No drafted answer rides in; nothing contested is ratified. [Observed]

**4.9 Collateral — attribution of every Wave B digest movement since `ad82f1d`.** Six commits landed in that range. `git log --oneline ad82f1d..b00c3dd -- rfcs/RFC-0007 rfcs/RFC-0008 rfcs/RFC-0009` returns **exactly one**: `1a23d19`, the RD-32 batch, touching **three modules, +19/−3 lines**. The RD-31 (Wave A) batch `d577823`, the RD-34 storage `0af54dc`, the v1.7 batch `eb53c3e`, the RD-31b delivery `36c01a9`, and the **v1.8 validator batch `b00c3dd`** each moved **zero** Wave B module bytes. The full diff is exactly the three repairs claimed in delta §12 and nothing else. **Every Wave B digest movement since `ad82f1d` is attributable to the RD-32 batch.** [Observed]

---

## 5. New findings

### N-1 (MAJOR) — the B1 repair imported a stated release-blocking obligation into RFC9-43 and routed no check for it, in the amendment RFC9-47(a) part 1 governs

**RFC9-47(a) — The registry maintains itself or it is wrong**, part 1, quoted (`rfcs/RFC-0009/interaction-parity-and-release.md`):

> "**The same-logical-change invariant.** Any amendment to this RFC — or to a contract this RFC consumes — that **creates, removes, or changes a release-blocking obligation on this surface** must update this clause's list **in the same logical change** … An amendment that creates a checkable obligation and does not route it here is an incomplete amendment; **the review that accepts it must treat the omission as a defect of the amendment, not a later housekeeping task.**"

And RFC9-47's own closing note: *"**This list is what craft-and-care consumes, so an obligation absent from it is tested nowhere** — demonstrated twice, once by a review finding six absences and once by a review finding the equivalence tuple short of two fields the gate then could not see."*

The RD-32 batch amended RFC9-43 — a clause of this RFC — and added text that names its own release-blocking consequence in-clause: *"since divergent totals over one declared scope are exactly the disagreement **RFC6-23 classes release-blocking**."* [Observed]

**RFC9-47's list was not touched.** `git diff ad82f1d b00c3dd` shows `interaction-parity-and-release.md` — the module RFC9-47 lives in — **unchanged by the batch**. [Observed]

I read RFC9-47's entire list (lines 106–207) against the two imported items:

| Imported item | Routed in RFC9-47? |
|---|---|
| per-value counts of chain state / normalized work state at aggregate level | **Yes, substantially** — the "work-state two-field consumption (RFC9-32)" entry names "**every element and every aggregate that carries a normalized work state carries its RFC2-18 chain state beside it** — no rendering, filter, **count**, legend entry, or tabular row shows one in place of the other," run against a fixture carrying every chain outcome |
| **primary-reasons-only Unknown-count rule** | **No entry reaches it** |

Every candidate entry was checked and excluded by reading it: "Unknown coverage (… every reason **rendered** …)" is a rendering rule, not a count-attribution rule; "no double-counting (**RFC9-21**)" is identity counting across aggregates ("Aggregates count each identity once per query subject … a shared component counts once in each district") — a different subject; the equivalence gate (RFC9-46/RFC6-22/23) compares two surfaces of *one* implementation, which share a counting convention by construction, so it **passes vacuously** over the exact failure RFC6-17 states the rule exists to prevent ("two conforming surfaces could produce different Unknown-reason totals over one declared scope while both satisfying this clause"). [Observed for the text; Inferred for the vacuity, from the clause's own stated failure mode.]

**Corroborating sweep, denominator 11:** `secondary` — **1 hit**; `primary reasons only` — **1 hit**. Both are the new RFC9-43 text. The rule exists in exactly one place in the wave and is named by no gate. [Observed]

**The package's own precedent points the same way.** When RFC9-46's tuple last gained two fields, RFC9-47's list gained matching entries in the same change — "Not-honored rendering (part 1, RFC9-9(b))" and "Backlog partitioning (part 4) … on both surfaces (RFC9-46)". That is the established practice this batch departed from. [Observed]

**The counter-reading, stated fairly.** RFC6-17 already bound the rule on this surface (RFC-0009 declares `depends_on: RFC-0006`), so it can be argued the amendment *restated* rather than *created* an obligation, leaving the routing gap pre-existing — one RD-32 itself noted in passing ("RFC9-47's gate list has no aggregate-level check for the gap") without making routing part of B1's repair direction on the branch the batch chose. [Inferred] I do not find that reading sufficient: part 1 explicitly reaches amendments "to a contract this RFC consumes," which shows the routing duty is meant to follow the obligation onto the surface wherever it becomes live; the amendment is the last clear moment; and part 1's final sentence is addressed to me by name — the accepting review may not defer it as housekeeping.

**Rule-10 disposition — does this warrant retiring the argument now, or batching?** **Retiring now.** The repair is one entry in RFC9-47's list, in `interaction-parity-and-release.md` — a bound module byte, so the manifest regenerates and this review retires with it. I judge it non-deferrable for three reasons: (i) the clause that governs the omission forbids treating it as later housekeeping, and I am the review it addresses; (ii) the alternative is binding, at an owner act, a stated release-blocking obligation that the package's own gate registry cannot see — the exact harm RFC9-47's closing note records twice; (iii) the offer is withheld regardless until P-33 is ruled (§7 item 11, and Wave A's offer precedes B), so the schedule cost of repairing now is close to zero, while the cost of binding it is permanent under RFC3-16(b) item 3.

### N-2 (MINOR) — a fourth restatement of RFC6-17's composition survives in RFC7-37, two repair batches behind

`rfcs/RFC-0007/rendering-and-surface.md`, **RFC7-37 — Subprojects render as declared relations**, quoted:

> "**Any roll-up over a child's facts additionally discloses RFC6-17's full composition** — the RFC6-22 equivalence tuple, per-label, per-tier, per-Unknown-reason and per-freshness-state counts and sibling surface states, expandable to members — **cited, never restated here**, because a paraphrase is how a roll-up rule drifts from the aggregation contract it instantiates."

The gloss is short of RFC6-17 by **four** items: `challenge-pending` (added to RFC9-43/RFC9-46 by the RD-27 batch), chain state, normalized work state, and the primary-reasons-only rule (added to RFC9-43 by the RD-32 batch). Neither batch reached it. The sentence declares "cited, never restated here" and names paraphrase-drift as the danger, while itself paraphrasing. [Observed]

**Not narrowing, and therefore MINOR:** under rule 8 the operative term is the citation, "RFC6-17's full composition," which is correct as written; a conforming implementation is bound to the full set. The defect is a misleading gloss, not a narrower obligation. **Disposition: batch into the N-1 repair** — the cleanest fix is deleting the gloss, which the clause's own words already justify.

**Consequence for the delta:** §12's claim that the drift class was "closed at the full set rather than item-by-item" is true of RFC9-43 and **false of the wave** — a fourth site stands. [Observed]

### N-3 (MINOR, record — not digest-moving) — §1 row B undercounts the RD-27 batch and contradicts the delta it cites

Row B: "for the RD-27 batch (**four modules**; delta §11)". `git diff --name-only 31ebc52 246af62` over the wave returns **seven** modules (RFC-0008 README, `accounting-reconciliation-and-release.md`, `identity-authority-materialization.md`, `state-vocabulary-and-cost.md`; RFC-0009 README, `interaction-parity-and-release.md`, `visual-grammar-and-lenses.md`). Delta §11, cited in the same parenthesis, says: "**Modules touched (7 of 11)** … seven files. Digest-moving in all seven." The batch had **four repairs** across **seven modules**; the record says four modules. [Observed]

### N-4 (MINOR, record — not digest-moving) — the "1,067" figure in §1 row B does not reproduce

Row B quotes "**1,067 RFC 0001–0006 clause citations, RD-32's count**." My count at `b00c3dd`: **758** (`RFC[1-6]-\d+`, 11 modules); at `ad82f1d`, the bytes RD-32 read: **755**. I tried six plausible variant readings (all clause tokens 1,811; tokens + package names 926; tokens + VIS/SEC 900; lines containing a token 621; distinct ids per module summed 304) — **none yields 1,067**. RD-32's own sentence routes the reader to "per-module counts in §4 below"; **RD-32 §4 contains no per-module citation table.** [Observed]

This is rule 3's exact shape: a derived value transcribed out of its owning artifact into the ceremony row the owner reads at the act. The qualitative claim the sentence makes is independently true (11 of 11 `depends_on`), so the repair is to drop or recompute the figure, not to weaken the disclosure.

### N-5 (MINOR, record — not digest-moving) — three statements of review state went stale when RD-31b returned CONFIRM

At `b00c3dd`, `RD-31b-wave-a-RAW.md` is stored and the delivery register copies its verdict as `VERDICT: CONFIRM`, bound to Wave A argument `8972d963…`. Three routed statements still say otherwise [Observed]:

| Artifact | Text | Status |
|---|---|---|
| Acceptance record §1 row A | "the current argument **awaits its fresh exact-package review (RD-31b)** before any offer" | stale |
| Acceptance record §6 | "**No CONFIRM verdict is bound to the current argument.**" | false for Wave A |
| `PENDING-OWNER-DECISIONS.md` P-1 row | "**No confirming review is yet bound to any wave argument**" | false |

P-1 is the row the launch-scope index defers to under its own precedence rule ("the row wins"). This is the RD-8 class arriving from the currency direction rather than the supersession direction. None of it touches the Wave B package; all three are record repairs.

### N-6 (MINOR, register — not digest-moving) — the repaired launch-scope index's Wave B bullet omits P-21(a)

The Wave B bullet lists P-38 and P-22 only. But §7 item 18 closes "Rule P-21(a), or perform **the acts** knowing the relation rides in unruled," and P-21's own row states "**RFC-0007's twin rides the Wave B act the same way.**" P-21(a) appears in the index's Wave A bullet only. [Observed] Small harm — Wave A precedes B, so the owner sees the item before either act — but it is the same completeness defect M1's repair set out to fix, in the bullet that repair rewrote.

### N-7 (denominator correction, carried) — RD-32's "no WARN names a Wave B module"

False; CG-8 names six. Detail and denominators in §3. No defect in the bytes; the correction travels to the closure report, as RD-31b's two did.

### N-8 (record) — the delivery register's RD-32b row names the wrong frozen commit

Row says `36c01a9` (clone-08e-r13); this administration ran at `b00c3dd` (clone-08e-r14). The subject bytes are identical at both commits (§0), so nothing is invalidated; the row wants a dated correction when this review is stored. [Observed]

---

## 6. What passes — stated plainly

The package's mechanics are **impeccable**, and containment is again the strongest part of it. The argument reproduces two ways and matches §1 row B byte for byte; 11 of 11 module digests verify from the ceremony's documented working directory; the manifests are the generator's current output and still partition the 39-module package; the repo-wide battery is **0 FAIL**; clause continuity, index, dependency index, budget report and task router all check clean; every module carries its candidate banner; no module claims acceptance or quotes an act digest; **88 phrase-module cells, zero ceremony phrases**; **zero declared or textual dependencies on the deferred waves** apart from one clause token disclaimed in-clause and fail-closed on Wave A ground; the remainder set reproduces RD-32's exactly by independent computation; and **all six RD-32 repairs are present, correctly placed, and closed** — B1's identity claim, which had failed three times, is now true item for item against RFC6-17's bytes.

The offer-ceremony disclosures are also, for the first time, complete in the record's own voice: row B states what a solo Wave B act binds and that the path is A → B; §7 items 15, 17 and 18 name every drafted arm; the launch-scope index no longer tells the owner the offer is gated when the record says it is ratified.

---

## 7. Answer to the commission question

**The package question and the offer question, separated.**

*Is the offer open?* **No, and that is correct and disclosed.** The offer path is A → B; Wave A's offer is withheld in the record's own voice until P-33 is ruled (§7 item 11), P-33 is open with undrafted arms, and RD-31b — the round's first CONFIRM — says the same. Nothing in this review changes that, and it is not what my verdict is about.

*Are these bytes offer-ready?* **No.** One defect requires a byte repair inside the manifest: **N-1**, the primary-reasons-only Unknown-count rule imported into RFC9-43 by the very batch under review, stated release-blocking in its own text, and routed into RFC9-47's gate list nowhere — which RFC9-47(a) part 1 calls an incomplete amendment and directs the accepting review to treat as a defect of the amendment, "not a later housekeeping task." **N-2**, the fourth short restatement of RFC6-17's composition surviving in RFC7-37, batches into the same repair. Both are small — one list entry and one deleted gloss — and neither reopens the substance the RD-32 batch settled.

The remaining findings (**N-3** through **N-8**) are record, register and delta corrections outside the manifest; they do not move a digest and should land in the same change.

Because the repair moves a bound module byte, the argument **`052acfb8…` retires with it** (rule 10), the manifest regenerates by `build_active_manifest.py`, §1 row B is rebound by script, and the offer gate re-runs as a fresh exact-package review of the new argument.

**Answer: no — the Wave B act may not be offered on argument `052acfb8c54bf6b7706af2b23b7bd2a84de8a34ebe3166f4cd3b078ae49bf655`.**

VERDICT: REVISE
