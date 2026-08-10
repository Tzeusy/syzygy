# RD-27 — Wave B review (round-2026-08e, frozen commit 5bb8a36)

## 1. Subject identification

**Clone:** `/tmp/claude-1000/-home-tze-GitHub-syzygy/3fa62952-e192-440e-8b1f-5b48212d8da1/scratchpad/clone-08e-r3`, `git log -1` = `5bb8a36`, working tree clean at start and at end (`git status --short` empty). No file in the clone or in the live repository was edited or created by this review.

**Manifest digest, recomputed this session** [Observed]:

```
2041ad053127cb1fc1022ed3295744e4b3a0053419f1e9945fb787537ab27f8a  wave-manifests/WAVE-B-MANIFEST.txt
```

This matches the argument quoted in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 row B byte-for-byte. **All 11 per-module digests verify**: `grep -F -v '#' wave-manifests/WAVE-B-MANIFEST.txt | sha256sum -c -` → 11 of 11 `OK`, 0 failures. `python3 scripts/build_active_manifest.py --check` → "all 7 manifests match regeneration — 7 manifest(s) over 39 module(s) in 6 wave(s)". `check_governance.py` CG-7b → "wave-act arguments match the wave manifests — 6 arguments examined, 0 findings". The Wave B argument is therefore mechanically sound and belongs to the bytes I read. [Observed]

**Subject population:** the 11 modules of RFC 0007 (3), RFC 0008 (4), RFC 0009 (4). All 11 read in full, line by line.

## 2. Method

- Read in the charter's order: `AGENTS.md`, `doctrine/vision.md`, `doctrine/security.md`, `wave-manifests/WAVE-B-MANIFEST.txt`, the acceptance record, `DEFERRED-WAVE-POSTURE.md`, the 11 modules, `decisions/PENDING-OWNER-DECISIONS.md`.
- Validation battery run at 5bb8a36, **output read, not exit code**: `check_governance.py` → 29 OK / 19 WARN / 0 FAIL (48 checks); `verify_final_prespec.py` → PASS, 341 numbered clauses over 39 modules; `build_active_manifest.py --check` clean; `build_dependency_index.py --check` clean; `build_budget_report.py --check` clean; `build_task_router.py --check` clean; **`build_contract_index.py --check` → DRIFT** (RD27-10).
- All load-bearing sweeps used Python `re` or `grep -F`, never a bracket class (rule 1).
- Cross-wave citation accuracy checked by opening each cited Wave A clause and reading its text, not by existence alone (rule 8): RFC1-7, RFC1-25(b), RFC1-25(c), RFC1-31, RFC2-1 (items 2/3/7/9), RFC2-3, RFC2-24, RFC2-25, RFC3-2, RFC3-15, RFC3-15(a), RFC3-16(a), RFC3-16(b), RFC4-13(a), RFC4-16(1)(2)(3), RFC4-17, RFC4-19, RFC4-23(2), RFC4-27, RFC5-5, RFC6-17, RFC6-22, RFC6-23, RFC6-24, RFC6-28. **Every one resolves and says what the citing Wave B text claims**, with the two divergences reported at RD27-01. Notably confirmed true: RFC3-16(a)'s example list does cite RFC8-12 by name; its encoding-meaning limb does name RFC9-26 and RFC9-18; its examples do include "an adoption/acceptance stamp" and "an approval, adjudication, or overrule Decision"; RFC1-25(b) does state "twelve ordered pairs"; RFC1-31 does omit `queued-for-materialization` (RFC8-7's reported defect is accurate).
- Manifest history recomputed from git, not transcribed: `git show <rev>:…/WAVE-B-MANIFEST.txt | sha256sum` over both revisions that touched the file.
- Clause-range distribution extracted mechanically per module and cross-checked against each README's lookup table.

## 3. Findings

---

### RD27-01 — MAJOR — RFC9-43 and RFC9-46 restate RFC6-17/RFC6-22 and drop `challenge-pending`, while RFC9-43 asserts the enumerations are identical

**Anchor (Wave B), `rfcs/RFC-0009/visual-grammar-and-lenses.md`, RFC9-43:**

> "**The disclosed composition is the full RFC6-22 equivalence tuple** — per-label, per-tier, per-Unknown-reason and per-freshness-state counts **and sibling surface states** … — never label and Unknown reason alone. … **RFC6-17 binds the same enumeration at the foundation layer — its own words are "the disclosed composition is the full RFC6-22 equivalence tuple" — so the two are deliberately identical, and any divergence is a defect to close rather than a surface-local variation.**"

**Anchor (Wave A), `rfcs/RFC-0006-cross-surface-selection-query-drawer.md`, RFC6-17:**

> "**The disclosed composition is the full RFC6-22 equivalence tuple**: per-label, per-tier, per-Unknown-reason and per-freshness-state counts, **the sibling surface states**, the `challenge-pending` disclosure (RFC2-13), and — where the aggregate's members carry them — per-value counts of the **chain state** and the **normalized work state** of RFC6-19 class 8…"

The verbatim quotation RFC9-43 makes is accurate; the em-dash enumeration beside it is not. RFC6-22 likewise carries "the same **`challenge-pending` disclosure** (RFC2-13)", and RFC9-46's restatement of that tuple —

> "equivalent per RFC6-22/23: same entity set, same edges, same epistemic states (label + tier + reason + freshness **and sibling surface states**), same counts, same evidence links, same scenario context, and — wherever the work/construction overlay is active — **both work-state fields**"

— omits it too, while its own maintenance note says the tuple "restates RFC6-22's cross-surface tuple and then names, item by item, the surface-local fields this surface adds" and warns that "an omission does not fail loudly anywhere."

**Sweep, with denominator** [Observed]: `grep -F 'challenge-pending'` over the corpus — **0 hits in 11 of 11 Wave B modules**; 3 Wave A modules carry it (`RFC-0002/rendering-vocabularies.md`, `RFC-0002/challenge-lifecycle.md`, `RFC-0006`). A second method (case-insensitive `grep -F 'challenge'` over RFC-0007/0008/0009) returns 10 lines, none of them the disclosure: RFC9-30's `challenge-suspended` tier, RFC7-9's admissibility floor, RFC8-18/8-25 "challengeable", and integration-list mentions.

**Failure scenario.** RFC9-47's release gate is evaluated over RFC9-46's tuple. A conforming map implementation discloses label/tier/reason/freshness/sibling-states on every aggregate and in the tabular equivalent, omits the `challenge-pending` disclosure on both, and passes every check in RFC9-47's list — while RFC6-17 and RFC6-22 require it and RFC6-23 makes the resulting scene/table silence a release-blocking disagreement that no gate on this surface looks for. The chain-state and normalized-work-state limbs RFC9-43 also drops are rescued by RFC9-32; `challenge-pending` is rescued by nothing inside Wave B. The obligation still binds through RFC6-17/RFC6-22 (both cited), so this is a false identity claim and an untested obligation, not a corpus hole — hence MAJOR, not BLOCKING. The Wave B semantic delta's own §10.2 flags the neighbouring RD-19 M4 choice as "a judgment call, not a derivation"; this is the part of that seam that came out wrong.

---

### RD27-02 — BLOCKING — the current owner-facing decision material for Wave B describes pre-repair bytes, and one substantive ruling this pass made is disclosed on no gate path

Three separable instances, one class — RD-8's "routing an owner to a stale offering … the finding that converts act 1 from a knowing act into a surprised one."

**(a) RFC7-39's "the entry *is* the primary narrative" is an owner-scoped answer disclosed nowhere the owner reads.**

Anchor, `rfcs/RFC-0007/rendering-and-surface.md`, RFC7-39:

> "**The entry is the project's primary narrative (RFC7-6), and RFC7-30 enters it.** There are not two front doors: this path is where the RFC7-6 primary narrative is published…"

The pass's own record concedes this is the owner's: `round-2026-08e/WAVE-B-SEMANTIC-DELTA.md` §10.3 — "**RFC7-39's 'the entry *is* the primary narrative' is a ruling this pass made.** … it is a substantive answer and the owner may prefer the other."

**Sweep, with denominator** [Observed]: `grep -rn -F 'primary narrative' --include='*.md'` over the whole clone, excluding `rfcs/` and the delta itself → 19 hits across 9 files; **none** is in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §7, in `decisions/PENDING-OWNER-DECISIONS.md`, or in any file under `decisions/`. The hits are round-08c briefs (superseded — `round-2026-08c/HUMAN-ENTRY-POINT-BRIEF.md:227` still reads "**missing** — no clause names `.syzygy/intent/OVERVIEW.md` as *the* entry point"), the routing matrix's RFC7-6 row, `08-OPEN-QUESTION-TRIAGE.md`'s row for the *different* question RFC7 q2 (cardinality), and history. By the charter's own test — disclosed in §7 **or** queued in `PENDING-OWNER-DECISIONS.md` — this one is neither.

**(b) The current P-38 packet states a three-value domain where the clause closes it at four.**

`decisions/HUMAN-ENTRY-DECISION.md` (headed "supersedes round-08d packet 8", queued as P-38, earliest required gate "**Wave B act**") states the question as:

> "per-repository discoverability: a kernel finding per governed repository: **yes / no / Unknown**"

and its register row P-40-neighbour reads "per-repository discoverability finding **yes/no/Unknown**". The clause the act would bind says the opposite is a violation — `rfcs/RFC-0007/rendering-and-surface.md`, RFC7-40:

> "**The answer domain is closed at four values** — **`yes` / `no` / `not-applicable` / `Unknown`** — stated once, here, and carried **verbatim** on every rendering and machine answer (RFC6-14). Closing it is what makes it checkable…"

with violation case 16 naming "the discoverability finding renders a fifth value the contract never names". Sweep [Observed]: `grep -F 'not-applicable'` outside `rfcs/` → the only occurrence connecting it to *this finding's* domain is inside `round-2026-08e/WAVE-B-SEMANTIC-DELTA.md:363`. An owner ruling option (a), "as drafted", from this packet is ratifying a domain the packet misdescribes.

**(c) Packet 6 was affirmatively re-blessed as current on 2026-08-10 while stating the superseded RFC9-8(a) placement.**

`round-2026-08d/OWNER-DECISION-PACKETS.md` header: "**Partially superseded 2026-08-10 (launch-closure pass):** packets **2, 7, 8, 10, 11** have current packets … Packets 1, 3, 4, 5, **6**, 9, 12 remain current here." `decisions/PENDING-OWNER-DECISIONS.md` repeats it: "the round-08d `OWNER-DECISION-PACKETS.md` remains current for packets 1, 3, 4, 5, **6**, 9, and 12."

Packet 6 as it stands:

> "**Question:** does the portfolio layout registry live in the **governance plane** (typed workspace governance store, **RFC10-15**)… **Costs:** (a) **portfolio re-lay waits for an accepted RFC 0010 store**"

Both statements are false against the bytes the Wave B act binds. `rfcs/RFC-0009/semantic-geography.md`, RFC9-8(a), as repaired: "they live in a **typed, owner-gated governance store**: an artifact of the governance class RFC3-15 fixes … honored **only under RFC3-16(a)**", with the bar released by "an owner act of RFC3-15(a)'s recorded-widening class" — an act wholly inside Waves A+B — and RFC10-15 demoted to "**Staged successor, not a reliance** … named for orientation only". The register's P-22 row carries the same stale text ("RFC9-8(a) is redrafted to the typed workspace governance store (RFC10-15) with a staged reference"), and its as-of header still reads 2026-08-09 although rows P-25(c) and P-34…P-40 were added to the same file on 2026-08-10.

**Failure scenario.** The owner performs Wave B from the offering apparatus the acceptance record and the register point at. They believe (i) the discoverability finding has three values, (ii) portfolio re-lay is blocked until an RFC 0010 they have deferred is accepted, and (iii) no clause identifies the fixed entry with the primary narrative. All three beliefs are wrong about the bytes they just bound, and one of them (ii) is the precise consequence the round-08e repair existed to remove. Classed BLOCKING because the charter fixes that class, and because the repair is cheap and digest-safe: every artifact named here sits **outside** the 11-module manifest, so correcting them does not move the Wave B argument.

---

### RD27-03 — MAJOR — acceptance record §1 row B discloses no regeneration and retires no prior argument; the delta's own handoff for that row is unexecuted

**Anchor,** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 row B, in full:

> "The 11 modules of RFC 0007–0009 (Polaris, Trajectory, Orrery) per `wave-manifests/WAVE-B-MANIFEST.txt`. **Depends on Wave A; performed first, it binds text whose reliances point at candidate material — lawful only stated at the act**"

Compare row A, updated in the same pass: "**Argument regenerated 2026-08-10 (RD-26 repair batch)** — seven modules repaired … the earlier `6b98e0c6…` argument is stale and satisfies nothing".

**Recomputed history** [Observed]: `git log` shows two revisions of `WAVE-B-MANIFEST.txt`; recomputing each file's own sha256 from `git show` gives `daa6a5dd37b7f92ac4ba4fc8a7bb491ecbffc02ba43227448f64f88dc3c3bebb` at `771965c` and `2041ad05…` at `31ebc52`. All eleven modules were edited (delta §0: "Edited — all eleven Wave B modules"; 39,653 → 44,102 words). Row B records none of this: no regeneration note, no retirement of `daa6a5dd…`. Acts 2, 3 and 4 all enumerate their retired arguments; row A does; row B alone does not.

The Wave B delta's §9 handoff 1 asked for exactly this and named the owner: "**X3 / the record's §7 item 9 and §1 row B.** … **Row B's disclosure should say that.** | **R-REC**". §7 item 9 *was* rewritten (it now carries the RFC3-15/RFC3-16(a) grounding and is labelled "rewritten 2026-08-10, round-2026-08e — the X3 single rewrite"). Row B was not touched.

**Failure scenario.** A reader comparing row A against row B concludes Wave B's bytes did not move in this pass — the reverse of the truth — and reads row B's surviving "its reliances point at candidate material" as still describing an RFC-0010 reliance the pass removed. Mitigating: `daa6a5dd…` survives in only 4 places corpus-wide (`grep -F 'daa6a5dd'` → `round-2026-08e/LAUNCH-CLOSURE-PREFLIGHT.md:53`, `round-2026-08d/reviews/RD-17…:236`, `RD-19…:7` and `:216`), and the preflight is correctly bannered ("The act arguments it quotes are the *pre-repair* ones and are quoted as history, never as an offer"), so no stale Wave B **offer** is live. That is why this is MAJOR rather than BLOCKING.

---

### RD27-04 — MAJOR — the routing matrix's RFC7-40 row directs a spec author to write a three-valued scenario over a four-valued closed domain

**Anchor,** `SURFACE-CLAUSE-ROUTING-MATRIX.md:1040`:

> "| RFC7-40 | OS | `spec/polaris` | The repository-front-door link to the project entry is a per-repository kernel finding — **`yes / no / Unknown`** at the producing evaluation … | A scenario must assert **the three-valued finding** renders per repository …"

against RFC7-40's "**The answer domain is closed at four values** — **`yes` / `no` / `not-applicable` / `Unknown`**".

**Failure scenario.** The matrix is the artifact `AGENTS.md` routes "May I implement X?" to and the per-clause source of spec acceptance criteria. A spec author writes the scenario the row prescribes; the resulting requirement asserts a three-value domain, and RFC7-40's `not-applicable` limb — the one that keeps a repository with no governance root from rendering `no` — has no requirement behind it, which RFC7-38's coverage matrix would then record as covered. This is the same clause and the same value RD27-02(b) finds misdescribed in the owner packet, so nothing outside RFC7-40 itself states the domain correctly.

---

### RD27-05 — MAJOR — the routing matrix's RFC9-8(a) row asserts the negation of the clause it routes to

**Anchor,** `SURFACE-CLAUSE-ROUTING-MATRIX.md:658`:

> "| RFC9-8(a) | OS | `spec/map-surface` | **The portfolio machinery lives in the workspace manifest**, not any project's `.syzygy/map/**` …"

**Anchor,** `rfcs/RFC-0009/semantic-geography.md`, RFC9-8(a):

> "**Never the workspace manifest and never `local/`:** both are personal presentation state under VIS-6 exception (a) and are **never snapshot inputs** (RFC3-10, RFC3-11, RFC3-21), while the layout version and baseline **are** (RFC2-1 item 7; RFC9-14(a)) — so a personal-state home is barred by RFC 0003's own rule, not by preference. The manifest carries at most a non-authoritative pointer…"

The matrix preserves the exact position P-22 was raised against and that two successive rounds repaired. Its acceptance criterion then asks a spec author to assert "a portfolio re-lay renders a reorganisation event…" — an obligation RFC9-8(a) as drafted **forbids performing at all** until a workspace-scope governance home exists ("**Until such a store exists at workspace scope, no portfolio re-lay is lawful — and that is the operative rule**"). The Wave B delta records the matrix as deliberately "Not touched"; the consequence is that a live, unbannered routing artifact contradicts the clause on the one question the Wave B act ratifies. Together with RD27-02(c), no artifact outside RFC9-8(a) itself states its placement correctly.

---

### RD27-06 — MAJOR — the generated task router's Polaris row contradicts itself and omits the module holding RFC7-31's release-policy leg

**Anchor,** `TASK-ROUTER.md`, "Specify or reason about Polaris (intent view)":

> "**Declared contract dependencies (from module front matter, computed):** RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, **RFC-0009**
> **Explicitly omitted:** **RFC-0008/0009** — sibling views own their own contracts"

The row computes RFC-0009 as a declared dependency (both `rfcs/RFC-0007/README.md` and `rfcs/RFC-0007/rendering-and-surface.md` carry `depends_on: […, RFC-0009]`) and then omits it in the next line, on a rationale that denies the edge exists. The edge is clause-borne, not decorative — `rfcs/RFC-0007/rendering-and-surface.md`, RFC7-31:

> "*(RFC9-45 states the same protocol in the same terms: defective verdict → recorded `verdict-unlawful`, test renders Unknown-never-met, gate fail-closed; **the shared release-policy leg is stated at RFC9-45**.)*"

and module 2 §5: "with the shared release-policy leg stated at RFC9-45, **never duplicated here**."

The Orrery row is the mirror case: it loads RFC-0009's three modules plus `RFC-0002/rendering-vocabularies.md` and RFC-0006, and lists **no** RFC-0008 module and no omission note, although RFC9-32 requires consuming "the declared work state … **verbatim from RFC 0008**" — the thirteen normalized values of RFC8-12/8-13 and the six chain values of RFC8-28 — and RFC9-46 puts both fields inside the release-gated equivalence tuple.

`build_task_router.py --check` reports "task router matches regeneration — 12 task classes validated", so the defect is in the route definitions the generator consumes, not in drift.

**Failure scenario.** An engineer specifying Polaris follows the single routing authority-of-navigation, never opens RFC 0009, and cannot answer whether a defective Polaris comprehension verdict blocks a release — the one thing RFC7-31 declines to state locally. An engineer specifying Orrery never opens RFC 0008 and implements the work/construction overlay against a vocabulary they have not read, which RFC9-32 says must be carried verbatim and RFC9-47 gates.

---

### RD27-07 — MINOR — RFC 0008 homes a conformance rule in a README Integration section and two modules cite it as its single home

**Anchor,** `rfcs/RFC-0008/state-vocabulary-and-cost.md` §5: "the **conformance rule binding both halves** is stated once, in `README.md` §5, and a consumer conforms only by consuming both fields." The same sentence appears in `accounting-reconciliation-and-release.md` §5. The rule itself lives at `rfcs/RFC-0008/README.md` §5: "**a consumer conforms by consuming both fields and rendering every value each field currently carries** … a value the consumer cannot render is a defect in the consumer, never a licence to fold it into a neighbour."

Verification rule 8's exact shape: section prose near a clause is not the clause, and P-21(c) already recorded this class against this package ("**`RFC 0008 §5` cited as authority** by RFC9-32"). The substance is rescued — RFC8-12 ("Every consumer, RFC9-32's work/construction overlay included, consumes **both fields**"), RFC8-28 ("**Every rendering, filter, count, endpoint answer, and cross-surface handoff that carries the normalized state carries the chain state beside it**") and RFC9-32 ("a value it cannot render is a defect here, never grounds to fold that value into a neighbouring one") each carry a limb of it — which is why this is MINOR. The repair is to fold the "renders every value each field currently carries" sentence into RFC8-12 or RFC8-28 and let the README point rather than hold.

---

### RD27-08 — MINOR — RFC 0009's README says "RFC 0011 is cited nowhere" four lines above citing it

**Anchor,** `rfcs/RFC-0009/README.md`: "It is the only mention of an unaccepted contract's clause anywhere in RFC 0009, and **RFC 0011 is cited nowhere**." Four lines later, in the same file: "**Provides to:** … **RFC 0010 / RFC 0011** — RFC9-52's phase boundary"; and above it, "both RFC 0010 and RFC 0011 cite it."

**Sweep, with denominator** [Observed]: Python `re` for `RFC10-\d+|RFC11-\d+|RFC[ -]0010|RFC[ -]0011` over all 11 Wave B modules → 18 hits; **exactly one clause token**, `RFC10-15` at `semantic-geography.md:175`, inside RFC9-8(a)'s staged-successor parenthetical. So the clause-level claim is true and the forward-dependency posture is sound (see §4); the sentence's second half is simply false as written of package names. Repair: "no clause of RFC 0011 is cited anywhere in RFC 0009."

---

### RD27-09 — MINOR — three bare cross-module `§` references in RFC 0008 name neither module nor file

**Sweep, with denominator** [Observed]: over all 11 Wave B modules, extracting every `§N[.M]` reference and testing it against the *same file's* own heading numbers (excluding refs preceded by a `.md` filename or "history"), **3 cross-module bare references remain, all in RFC 0008**:

- `identity-authority-materialization.md`, RFC8-6: "may never alter one (**§3.13**)" — §3.13 is in module 3.
- `state-vocabulary-and-cost.md`, RFC8-13 `reconciled` row: "V0: never renders (**§3.14**)" — module 3.
- `state-vocabulary-and-cost.md`, RFC8-12: "the closure fallacy needs (**§6**; RFC8-30)" — §6 is the package README's "Alternatives considered".

RFC 0009's README uses the correct convention throughout ("module 1 §10", "module 2 §8"), and RFC 0008's own lookup rule covers clause identities but is silent on section numbers, so a cold reader of module 2 has no deterministic way to resolve "§3.14".

---

### RD27-10 — MINOR — `build_contract_index.py --check` reports drift, falsifying the acceptance record §6 bullet

At 5bb8a36: `python3 …/scripts/build_contract_index.py --check` → "**DRIFT: 05-CONTRACT-INDEX.yaml differs from regeneration**". Regenerating into a scratch copy and diffing shows the drift is **two lines**, both topology word counts (`topology/BUNDLE-MANIFEST.md` 145→167, `topology/README.md` 569→602) — a consequence of the RD-25 act-3 repairs, **not** a Wave B row; all RFC 0007–0009 rows are current.

**Anchor,** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §6: "`scripts/build_contract_index.py --check` — **no drift**." That bullet is false at these bytes, and `AGENTS.md` lists this generator in the battery to run "before claiming anything is clean." The Wave B delta §9 handoff 2 predicted it ("`build_contract_index.py` (already drifting at HEAD, independently of this batch)") and it was not executed. Scoped MINOR for Wave B; it bears more on act 3.

---

## 4. Dimensions on which Wave B passes

Recorded so the verdict is not read as a wholesale rejection.

- **Forward dependencies — clean, and this is the pass's real achievement.** The `RFC10-*`/`RFC11-*` sweep above (denominator: 11 of 11 modules) finds one clause token, and it is a citation under verification rule 5, stated as such in-clause: "*(**Staged successor, not a reliance.** … It is named for orientation only: a citation, not a reliance. If RFC 0010 is never accepted, the rule above still stands and still fail-closes.)*" I read RFC9-8(a) in full and confirm the operative rule stands on RFC3-15, RFC3-15(a) and RFC3-16(a) — all Wave A — and fail-closes independently. Every `depends_on` edge declared by the 11 modules lands inside Waves A+B (RFC-0001…RFC-0009); none reaches RFC-0010 or RFC-0011. `DEFERRED-WAVE-POSTURE.md`'s claim that "Wave B's former clause-level reliance (RFC9-8(a) → RFC10-15) is redrafted … to a Wave-A-grounded governance store" is accurate against these bytes. **Wave B is independently acceptable given Wave A.**
- **Cross-wave citation accuracy.** 25 Wave A clauses opened and read against the citing Wave B text; all resolve and all say what is claimed of them, with the RD27-01 divergences the only exceptions. The reason numbers (#1, #5, #6, #8, #11), the twelve-reason and six-tier closures, the three sibling surface states, RFC6-24's exactly-three contexts, RFC1-25(b)'s twelve ordered pairs, RFC1-25(c)'s non-functional `placed_in`, RFC2-1's item numbering, and RFC3-16(a)'s named examples all check out verbatim.
- **Clause hygiene.** Mechanical extraction confirms RFC7 1–25 / 26–40, RFC8 1–11 / 12–20 / 21–32, RFC9 1–23 / 24–45 / 46–52, no identity in two modules, no gaps; violation-case distribution matches every README's routing sentence (RFC 0007: 16 cases, RFC 0008: 14, RFC 0009: 12 items under 11 integers, all as the READMEs state); every §8 question's state matches between README index and owning module. `verify_final_prespec.py` PASS.
- **Human entry and accessibility.** I found no term used before a reader could resolve it: each package carries a reader map, a deterministic lookup rule, and a per-module scope statement, and the surfaces' purposes, obligations and prohibitions are each stated in a clause a cold reader reaches. RFC7-34's reachability limb, RFC8-31's two-limb parity statement, and RFC9-48's keyboard/screen-reader obligations are mutually consistent and each names why encoding and operability are separate obligations. RD27-09 is the only navigational friction I could reproduce.
- **Routing rows that are correct.** `TASK-ROUTER.md` carries one route per surface, each naming the right package and a correct directly-governing clause; the deferred-wave routes are singular and explicitly labelled, as `DEFERRED-WAVE-POSTURE.md` requires. CG-17 reports 210 clauses routed exactly once, 0 findings — the round-08e handoff on `RFC9-10(c)`/`RFC9-19(b)` has landed. RD27-04/05/06 are defects in specific rows, not in the routing structure.

## 5. Overall assessment

The Wave B bytes themselves are in good shape: the argument is scripted and verifies, the eleven modules are internally coherent, the clause ranges and violation-case distributions are exactly what the package indices claim, twenty-five spot-checked cross-wave citations all say what the citing text claims of them, and the pass's headline achievement is real — after the RFC9-8(a) redraft, a Python `re` sweep over 11 of 11 modules finds exactly one token of an unaccepted contract's clause, and it is a stated citation over a rule that fail-closes on RFC 0003's own terms, so Wave B is genuinely acceptable alone once Wave A is bound. What is not in good shape is everything around the bytes. The one substantive ruling this pass made inside a clause — that the fixed entry *is* the RFC7-6 primary narrative — is recorded only in a process-bookkeeping delta that no gate path reaches; the two owner packets whose "earliest required gate" is the Wave B act both describe the pre-repair corpus, one of them affirmatively re-blessed as current on the same date the repair landed and still telling the owner that portfolio re-lay waits on an RFC 0010 they have deferred; the acceptance record's own row B neither discloses that all eleven modules moved nor retires the argument they superseded, leaving the delta's handoff half-executed; and two hand-maintained routing rows now state, respectively, a three-value domain against a clause that closes it at four and the exact workspace-manifest placement the clause forbids in bold. Add RFC9-43's assertion that its aggregate enumeration is "deliberately identical" to RFC6-17's when it drops the `challenge-pending` disclosure that appears in 0 of 11 Wave B modules, and the pattern is consistent: the contract text was repaired carefully and the apparatus that tells an owner what they are accepting was not brought with it. Every finding here is repairable **outside** the eleven-module manifest, so none of them requires regenerating the Wave B argument — but until they are repaired, performing Wave B on the current offering would be a surprised act, which is the precise thing the wave structure exists to prevent.

VERDICT: REVISE
