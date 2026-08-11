# RD-51 — Specification-acceptance and shape-to-spec impact policies (round-2026-08f, frozen commit `e2efda6`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 reviews 5 and 6 — the revised specification-acceptance policy, and the shape-to-spec propagation rule and its fixture, dispatched as one review because CC-IMPACT-1 declares what CC-SPEC-2 warrants |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `e2efda6` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Subject files** | `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`; `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`; `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md` |
> | **Context** | fresh — subject, governing references and acceptance criteria only |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `REVISE` |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.

---

VERDICT: REVISE

---

## Method note

Bytes read at `e2efda6` (`git rev-parse HEAD` = `e2efda65ef029c76703904c093219cd6ce906d75`). No file was modified. Governing references read in full: `doctrine/vision.md` (VIS-1…7), `policies/craft-and-care/README.md`, `review-and-documentation.md` (CC-REV-1…7), `testing-and-verification.md` (CC-TEST-1…7), `interfaces-and-dependencies.md` (CC-DEP-2). Approved craft-clause denominator established by sweep: **46 clauses** (`grep -n "^## CC-" *.md` over the 8 cluster files → 6 SEC + 6 OBS + 7 TEST + 7 REV + 7 BAR + 6 DEP + 7 PROV). Absence claims below carry a denominator and a second method.

---

## A. CC-SPEC-2 — is the five-source warrant list complete, and are the sources distinguishable?

**Method.** Quoted the clause verbatim; enumerated the authority classes the repository actually recognises (doctrine's typed-authority table via `AGENTS.md`'s "Where authority lives", the craft cluster's own precedence list in `policies/craft-and-care/README.md` L36–43, and the four declaration classes the *sibling candidate* CC-IMPACT-1 defines); tested each recognised class against the five admitted sources; then swept for the fifth source's defining record.

The clause (`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` L18–27):

> **CC-SPEC-2 — Every requirement names its lawful higher-level warrant.**
> A requirement traces upward to exactly one of these, **and names which**:
> ```
> adopted doctrine                 by rule ID
> accepted contract                by clause ID
> recorded owner product decision  by decision identifier or path
> accepted parent specification    by specification and requirement ID
> lawfully admitted user need      by the record that admitted it
> ```

**Observation — the list is not complete. Two constructions fit none of the five.**

*(1) A requirement warranted only by an approved craft clause.* The craft cluster is a distinct authority tier — `policies/craft-and-care/README.md` L36–43 lists it as tier 2, separate from tier 1 (doctrine + SDRs), and separate again from contracts. Concrete requirement an author legitimately wants: *"When a run summary carries no token count, the cost rollup renders `Unknown` for that run and the aggregate discloses the count of runs with absent cost."* Its warrant is **CC-PROV-5** ("Missing cost renders Unknown, never zero") and **CC-TEST-6**. CC-PROV-5 is not a doctrine rule ID, not a contract clause ID, not a decision identifier, not a parent-spec requirement ID, and not a user-need record. Under CC-SPEC-2 as written this requirement "is a finding against the spec, not a bonus" (L29–30). The class is not exotic: CC-OBS-3 (labelled degradation), CC-TEST-6 (Unknown/absence branches) and CC-PROV-5 all generate directly user-observable behaviour.

*(2) A requirement warranted by an accepted topology identity.* The sibling candidate offered in the same pass, `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` L19–28, requires every specification to declare `topology identities — the placements it assumes`, and CC-IMPACT-2 (L35–37) makes a change to *"an accepted doctrine rule, contract clause, or topology identity"* trigger the sweep. So topology is a shape authority a spec may rely on and be invalidated by — yet no requirement may lawfully name it as warrant. The two candidates disagree about the authority set.

**Observation — source 5 is vacuous.** `lawfully admitted user need — by the record that admitted it` (L26): sweep of `.syzygy/**` (`*.md`/`*.yaml`/`*.json`, **353 files**, Python `re` `user\s+need` case-insensitive) → **1 hit, the clause itself**. Second method, repo-wide over `.md/.py/.json/.yaml/.yml/.txt` (**764 files**) → **2 hits**: the clause, and the untracked authoring charter at repo root (`git ls-files | grep -F syzygy_fable` → empty; the charter is **not in the frozen commit**). No record class, no admission act, no register for "admitted user need" exists anywhere in the governed corpus. An author may therefore satisfy CC-SPEC-2 by pointing at any document they choose to call "the record that admitted it" — which is precisely the "no constraint at all" the clause's own rationale (L36–37) says naming-which prevents.

**A requirement fitting two, and whether the clause resolves it.** *"When a repository's evidence set has no declared currency bound, the status endpoint renders `Unknown` with reason `no-currency-bound`, never a green state."* This traces to **VIS-2** (doctrine: "Until a claim class declares its currency bound, its evidence is not current and the claim renders Unknown"), **and** to the reason-vocabulary contract clause RFC2-24, **and** to owner decision P-36 (Unknown vs Gap). Three of the five sources, genuinely. CC-SPEC-2 says the requirement "traces upward to **exactly one** of these, **and names which**". On the literal words, "exactly one" is a property of the requirement, so a three-warranted requirement is *unlawful*, not merely under-named. On the charitable reading ("name exactly one"), the clause supplies **no tie-break** — no "most specific wins", no "nearest binding authority", no "name all applicable". Compare the corpus's own habit of stating precedence explicitly (`craft-and-care/README.md` L36–43). The clause does not tell the author which to name.

**Judgement.** Incomplete (two demonstrated gaps), one source vacuous, ambiguity between "exactly one warrant" and "name exactly one" unresolved. **Not acceptable as written.**

---

## B. CC-SPEC-4 — is the four-part test sufficient?

**Method.** Quoted the clause; constructed a passing-but-untestable instance against each of the four named parts; then constructed a requirement class the corpus demonstrably needs and tested it against the four parts.

The clause (L43–53, L55–56):

> **CC-SPEC-4 — Observable requirements name success *and* falsification.**
> A testable observable requirement names four things:
> ```
> initiating condition      what happens, or is done, to trigger it
> observable result         what is then visible, and where …
> positive success oracle   how one decides the result IS the expected one,
>                           without judgment
> falsifying evidence       what would show it failed or is absent
> ```
> A requirement whose satisfaction no evidence could ever contradict is not a requirement.

**A requirement satisfying all four and still untestable:**

> **REQ-X.** *Initiating condition:* a status evaluation is requested for a repository whose evidence set has been continuously current for one year. *Observable result:* the `aligned` field appears in the machine endpoint's response body. *Positive success oracle:* `aligned` is `true` exactly when the specification corpus and the implementation are semantically equivalent. *Falsifying evidence:* a response where `aligned` is `true` and they are not equivalent.

All four parts are named, and the oracle is stated as an equality rather than an opinion, so it survives "without judgment" on the clause's words. It is untestable twice over: the **initiating condition is unreachable** (nothing can produce a one-year currency history on demand), and the **oracle is not effective** (semantic equivalence of a corpus and a codebase is not decidable by any procedure the requirement names). CC-SPEC-4 requires the oracle to be judgment-free; it does **not** require it to be *decidable in bounded effort*, nor the initiating condition to be *producible*. A second variant needs no exotic predicate at all: *"the oracle is: the flag equals what the reconciliation engine computes."* That is tautological — the oracle is defined by the implementation under test. The canonical `test-rigor` bar's no-tautologies rule is adopted by reference (`craft-and-care/README.md` L12–18) but governs *tests*; a spec's oracle is not a test, so nothing in the 46 approved clauses or in CC-SPEC-1…10 forbids it.

**A genuinely good requirement the four-part test would wrongly reject:** a **prohibition**, which is the dominant requirement shape this doctrine generates.

> **REQ-Y.** No surface renders a green status from evidence whose currency bound is undeclared.

This is VIS-2's own shape, and it is exactly the requirement Capability 1 most needs. It has **no initiating condition** — it is universally quantified over all renders, not triggered by an event. It has **no positive success oracle**: the expected observable result is *nothing happening*, and one cannot positively decide "this render is the expected non-violation" except by exhausting the render space. It has excellent falsifying evidence (one counterexample). So the four-part test rejects it while the clause's own closing sentence — "a requirement whose satisfaction no evidence could ever contradict is not a requirement" — *admits* it. The clause contradicts itself across L47–52 and L55–56.

The hedge "**Observable** requirements name…" does not rescue this. Either prohibitions are observable requirements (then CC-SPEC-4 wrongly rejects them), or they are not (then **no clause in CC-SPEC-1…10 states any testability bar for them at all**, and the largest requirement class in the corpus escapes E5 entirely). Both horns are findings.

**Judgement.** The four-part test is **not sufficient** and is over-inclusive at one end and under-inclusive at the other. It needs (a) a reachability constraint on the initiating condition, (b) an effectiveness/non-tautology constraint on the oracle, and (c) an explicit alternative form for prohibitions and invariants.

---

## C. CC-SPEC-10 vs VIS-4 — word by word

**CC-SPEC-10** (L89–95, operative text in a blockquote at L91–92):

> **CC-SPEC-10 — Lawful adoption is recorded at the exact digest.**
> > Lawful adoption under VIS-4 is recorded at the exact digest. Under the current doctrine state, this means owner adoption.
> Until that record exists the spec is a candidate like everything else, and the record quotes what was adopted at which digest.

**VIS-4** (`doctrine/vision.md` L127–139), the spec-relevant limbs:

> Behavioral specs (`openspec/`) sit below that line: LLM adoption of spec changes is permitted in principle, but opening that gate is a **doctrine amendment event** — it requires both an accepted adjudication RFC (defining what makes adversarial judgment independent, how the ambiguity determination is recorded, and how each adopted change stays individually revertable) *and* the owner's explicit doctrine amendment recording that the gate opens; RFC acceptance alone never opens it. One class is always human-gated, gate open or not: spec changes touching security posture, privacy or retention obligations, or normative data contracts. Classification of a change as spec-level or shape-level is contested by default and is never made by the agent performing the change…

**Word-by-word.**

| CC-SPEC-10 words | VIS-4 counterpart | Relation |
|---|---|---|
| "recorded at the exact digest" | *no digest concept in VIS-4* | **Adds** — a lawful strengthening, and the clause's real contribution |
| "the record quotes what was adopted at which digest" | none | **Adds** — lawful |
| "Under the current doctrine state, this means owner adoption" | "opening that gate is a doctrine amendment event … RFC acceptance alone never opens it" | **Correct paraphrase of today's state.** The gate is not open (no accepted adjudication RFC exists; `contracts/rfcs/` does not exist), so owner adoption is the current reading. Accurate. |
| *silent* | "**One class is always human-gated, gate open or not**: spec changes touching security posture, privacy or retention obligations, or normative data contracts" | **Subtracts — materially.** |
| "VIS-4 governs delegation and may define a future gate that is not the owner personally" (L98) | "it requires **both** an accepted adjudication RFC … **and** the owner's explicit doctrine amendment" | **Subtracts** the two conjoined preconditions; reads as though VIS-4 alone could move the gate |

**Judgement.** It **adds** (digest binding — the clause's genuine value), **paraphrases correctly** for the present state, and **subtracts** the one limb whose whole purpose is to survive the change the amendment was written to anticipate. The amendment note (L95–101) says the restatement exists so the clause is "the right thing later"; the omitted sentence is precisely the *later* rule. A reader in a gate-open future reading CC-SPEC-10 alone would conclude the entire spec corpus is LLM-adoptable at a digest. Fix: append the always-human-gated class by quotation, or replace the second sentence with a bare pointer that adds nothing beyond the digest rule.

---

## D. Conflicts, dead overlaps, gaps across the 17 clauses

**Method and denominator.** 10 CC-SPEC + 7 CC-IMPACT = **17 clauses**, **136 unordered pairs** (17×16/2). I read all 17 clause bodies in full and classified each pair by whether the two clauses share a subject (same artifact, same actor, or same obligation). **13 pairs share a subject**; the remaining **123** do not, by the clause texts as read. The 13:

| # | Pair | Relation | Severity |
|---|---|---|---|
| 1 | CC-SPEC-1 ↔ CC-IMPACT-1 | **Conflict.** CC-SPEC-1: "The specification names **one** coherent capability". CC-IMPACT-1: "`capability identities — which capability (or capabilities) it specifies`". One mandates singular; the other's declaration schema contemplates plural. | material |
| 2 | CC-SPEC-2 ↔ CC-IMPACT-1 | **Gap.** CC-SPEC-2 binds warrants at *requirement* level; CC-IMPACT-1 binds declarations at *specification* level. **Nothing requires the declaration to be the union of the requirement warrants.** A spec whose REQ-3 names RFC6-19 as its contract warrant while its CC-IMPACT-1 declaration lists only RFC6-18 satisfies both clauses and is **invisible to CC-IMPACT-2's sweep** — the exact FAC-1 failure the fixture exists to catch. | **blocking** |
| 3 | CC-SPEC-2 ↔ CC-IMPACT-2 | **Gap.** CC-SPEC-2 admits `recorded owner product decision` as a warrant class; CC-IMPACT-2 triggers a sweep only for "an accepted doctrine rule, contract clause, or topology identity". **A change to an owner decision triggers no sweep and is declared nowhere.** Warrantable-but-unsweepable is a silent-staleness generator, and it applies to two of the five sources (decisions, user-need records). | **blocking** |
| 4 | CC-SPEC-2 ↔ CC-IMPACT-1 (topology) | **Inconsistency.** Topology is declarable and sweepable but not warrantable (see A). | material |
| 5 | CC-SPEC-8 ↔ CC-IMPACT-1 | **Overlap / two homes.** The clause-to-requirement coverage matrix (CC-SPEC-8) and the declared contract-clause IDs (CC-IMPACT-1) hold the same fact — which clauses a spec touches — with no derivation rule between them. CC-REV-3: "discovering the same question answered in two homes is a contradiction to surface". | material |
| 6 | CC-SPEC-8 ↔ CC-IMPACT-2 | **Overlap.** The coverage matrix *is* the reverse index the sweep needs; CC-IMPACT-2 ignores it and invents declarations instead. | minor |
| 7 | CC-SPEC-10 ↔ CC-IMPACT-6 | **Gap.** CC-SPEC-10 binds adoption to an exact digest. CC-IMPACT-6 permits a spec to lag its shape change. **No clause says whether the lagging spec's later amendment requires a fresh CC-SPEC-10 adoption record**, so an owner-adopted digest can silently cease to describe the adopted content. | material |
| 8 | CC-SPEC-6 ↔ CC-SPEC-2 | **Tension.** CC-SPEC-6 blocks a spec whose requirement "would settle an open owner question"; CC-SPEC-2 admits owner decisions as warrants. Whether a *pending* decision may be cited is unstated — and CC-SPEC-1 itself cites the pending P-40 (finding 3 below). | material |
| 9 | CC-SPEC-9 ↔ CC-SPEC-1 | **Overlap.** CC-SPEC-1: "A reader can say what the capability is in one sentence"; CC-SPEC-9: a fresh reader "can restate the capability and its acceptance conditions". Same judgement, two clauses, no distinct actor or threshold. | minor |
| 10 | CC-IMPACT-5 ↔ CC-IMPACT-6 | **Near-dead.** CC-IMPACT-6's exception limb already requires "the owning actor". In the default (same-change) case CC-IMPACT-5's actor is trivially the author. CC-IMPACT-5 does independent work only where CC-IMPACT-6 already names the actor. | minor |
| 11 | CC-IMPACT-3 ↔ CC-IMPACT-4 | **Gap between them.** CC-IMPACT-3's `explicitly unaffected` set requires only "the reason"; CC-IMPACT-4 only catches specs the sweep "could not settle". A sweep that *decides* wrongly (declaration-match says untied) lands in `explicitly unaffected` with a true-but-irrelevant reason and never reaches CC-IMPACT-4. No clause bounds the `undecidable` set either — a sweep placing all specs in `undecidable` satisfies CC-IMPACT-3. | **blocking** |
| 12 | CC-SPEC-5 ↔ CC-IMPACT-4 | Benign overlap: both apply VIS-2's Unknown rule to specs, at different triggers (authoring vs propagation). | none |
| 13 | CC-SPEC-3 ↔ CC-IMPACT-1 | Complementary: stable requirement identities are what make declarations resolvable over time. | none |

**The largest gap is not a pair — it is an absence across all 17.** Launch-gate E5 (`launch-gate-pre-specifications.md` L404–406) asks: *"Do acceptance criteria exist for a spec itself — how one will be judged **complete**, testable, and faithful to the shape above it?"* Sweep of all ten CC-SPEC clause bodies for a completeness obligation **with respect to the capability**: CC-SPEC-8 is completeness with respect to *contract clauses*; CC-SPEC-5 requires non-goals but never requires the in-scope surface to be covered; CC-SPEC-1 requires scope to be *stated*, not *covered*. **0 of 10 clauses ask whether the requirement set covers the capability it claims.** E5's "complete" limb is unclosed.

---

## E. Restatement of what doctrine or approved craft policy already owns

**Method.** Each of the 17 clause bodies compared against the 46 approved craft clauses (enumerated by sweep) and the 12 doctrine rules.

| Candidate clause | Already owned by | Verdict |
|---|---|---|
| **CC-SPEC-9** | **CC-REV-4** — "Every normative artifact passes fresh-reader review at adoption and on material amendment (VIS-3): a reader with no authoring context restates intent and constraints correctly, and failures are recorded on the artifact's surface." Plus **VIS-3** itself. A specification is a normative artifact. CC-SPEC-9 adds only "not the reader", which VIS-3's "failure is recorded on the artifact's surface" already implies. | **Duplicate.** Replace with a citation. |
| **CC-SPEC-5** (Unknown half) | **VIS-2**, and **CC-REV-5** ("missing evidence renders Unknown, never Inferred"). The clause openly says "(VIS-2 applied to the spec itself)". The non-goals half is new. | Partial duplicate; keep the non-goals half. |
| **CC-SPEC-3** | **CC-REV-7** ("amend text in place; retire rather than renumber… A retired identifier's entry remains, marked retired") and **CC-DEP-2**. CC-SPEC-3 lawfully *extends* to a new population (requirement IDs, not in CC-REV-7's enumeration) but **drops the retirement limb** — it says "never renumbered or reused" and supplies no mechanism for a withdrawn requirement. | Extension with a subtraction. |
| **CC-SPEC-10** | **VIS-4** — see C. Deliberate deference; the digest binding is new. | Lawful, but subtracts (C). |
| **CC-IMPACT-4** | **VIS-2**. "Silence is not an answer, and 'not listed as affected' is never evidence of being unaffected" is VIS-2's "No evidence means Unknown, not success" applied. | Restates rather than cites — contrary to the file's own preamble. |
| **CC-IMPACT-3** | **CC-KNOW-16** (candidate, P-12, `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` L245–252): "'All,' 'none,' 'zero,' '100%' may be written only if the exact sweep described was run… A sweep that returns nothing supports a universal claim only when a second method agrees." | **Duplicate-in-waiting**, and the clause's justification is false — see finding 11. |

**CC-IMPACT-6 against CC-REV-2 — checked specifically.**

CC-IMPACT-6's factual claim about CC-REV-2 is **correct**. CC-REV-2 reads: *"The one structural carve-out: **doctrine** is amended only through the owner gate (VIS-4)."* There is no other exception limb. CC-IMPACT-6 states this accurately (L71–72).

But what CC-IMPACT-6 then does is the problem. CC-REV-2 (`review-and-documentation.md` L57–65) says:

> A change that invalidates any authoritative artifact updates **every** invalidated authoritative artifact in the same logical change: **behavioral specs (`openspec/`)**, declared topology, accepted contracts, and the policies in this cluster. "We'll sync the spec later" is a violation, not a plan… The rule is a **merge invariant, not a property of how work is packaged**: no merge may leave mainline with an invalidated authoritative artifact still asserting the old truth. Splitting one logical change across sequenced merges that pass through such a state *is* the violation — an open follow-up PR is "syncing later" by another name.

CC-IMPACT-6 (L69–79):

> This rule therefore **adds exactly one lawful alternative**… an affected specification may **lag** its shape change **only** under a recorded exception that names the specification, the reason, the owning actor, and the condition that ends it…

Behavioral specs are **the first item in CC-REV-2's enumerated list**. CC-IMPACT-6 therefore **weakens an owner-approved clause**, in the population that clause names first, by writing a new clause beside it rather than amending it. Three independent problems:

1. **It is a weakening, and the cluster's own precedence forbids only cross-tier weakening** (`craft-and-care/README.md` L44–45: "A lower layer can strengthen a higher one; it can never weaken it"). CC-IMPACT-6 sits in the *same* tier, so precedence supplies **no** rule to settle the contradiction. Two clauses of one approved cluster would give opposite answers to "may this merge land?" with nothing to arbitrate.
2. **It creates a second home for the merge invariant**, which CC-REV-3 forbids: "documentation **cites** authoritative artifacts, it does not restate them normatively — a restated rule drifts and becomes a shadow authority."
3. **The exception has no confirmer.** Compare the two approved exception mechanisms in this cluster: CC-TEST-1 — exceptions "recorded in the change record with the reason and the compensating verification performed"; CC-TEST-4 — the classification "is **never made by the implementing agent alone** — … confirmed by the change's reviewer (or the owner where no reviewer exists)." CC-IMPACT-6 requires four fields and **no second party**. The author of the shape change writes their own exception to CC-REV-2 and merges. That is the CC-REV-2 violation with a form attached.

There is a fourth fact worth recording. The fixture (`round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md` L36–41) states of exactly this limb:

> *(An earlier form of this step invented an "explicit exception with reason and expiry" alternative; no craft clause contains it, and it is **withdrawn**.)*

CC-IMPACT-6 reinstates that same limb — reason, owning actor, and "the condition that ends it" (an expiry by another name) — as a candidate clause. Creating a rule by act is lawful; creating one that overrides a *different* approved clause without amending it is not.

**The preamble's claim is false on its own file's face.** L11–14 says: *"Steps 3 and 4 already have owners — VIS-2 and CC-REV-2 — and this policy does not restate them, it cites them."* CC-IMPACT-4 restates step 3 normatively; CC-IMPACT-6 restates step 4 normatively **and amends it**.

---

## F. Unenforceable clauses — no actor, no observable trigger, or an unassigned judgement

**Method.** Each of the 17 clauses tested for three things: a named actor, an observable trigger, and an assigned judge for every judgement word it contains. **Denominator 17.**

| Clause | Actor | Trigger | Unassigned judgement |
|---|---|---|---|
| CC-SPEC-1 | none | acceptance | **"coherent"; "A reader can say… in one sentence" — which reader?** |
| CC-SPEC-2 | none | acceptance | which warrant, when several apply (A) |
| CC-SPEC-3 | none | acceptance | — |
| CC-SPEC-4 | none | acceptance | "without judgment" is asserted, not verified by anyone |
| CC-SPEC-5 | none | acceptance | what counts as "not yet known" |
| **CC-SPEC-6** | **none** | none — the trigger is "*would* settle an open owner question", a counterfactual | **Who decides that a requirement would settle an open question?** VIS-4 answers the analogous question ("Classification … is contested by default and is never made by the agent performing the change"); CC-SPEC-6 inherits none of it, so the spec's own author is both the only party positioned to notice and the party least able to. |
| CC-SPEC-7 | none | acceptance | "genuinely about it" |
| **CC-SPEC-8** | **none** | acceptance | **"every *applicable* clause" — applicability is undefined and the N/A judgment's reviewer is unnamed.** This is the single largest laundering channel in the ten (see G). |
| CC-SPEC-9 | CC-REV-4's reviewer, by reference | adoption | — (the one clause that borrows an actor) |
| CC-SPEC-10 | owner | adoption | — |
| CC-IMPACT-1 | none | acceptance | "**a fixed and machine-readable place**" — no authority defines one, and P-39 (OpenSpec form and version), the decision that would, is **pending** |
| **CC-IMPACT-2** | **none — "the change carries a sweep" is passive** | shape delta lands | **who performs the sweep, who judges it adequate** |
| **CC-IMPACT-3** | none | with the sweep | **no bound on `undecidable`; no adequacy threshold** |
| CC-IMPACT-4 | none | after the sweep | who "renders", and on what surface — no renderer exists |
| CC-IMPACT-5 | the clause's whole subject **is** the actor rule — enforceable | before the change lands | — |
| **CC-IMPACT-6** | exception author only | merge | **nobody confirms the exception (E, item 3)** |
| **CC-IMPACT-7** | "the reviewer" — unnamed, unselected | "before the first real shape amendment after specifications exist" — observable | **no pass criterion.** The clause requires only that "the comparison is recorded". A blind run that misses every impacted spec, recorded honestly, satisfies CC-IMPACT-7 in full. |

**Judgement.** **6 of 17 clauses are unenforceable as written** (CC-SPEC-6, CC-SPEC-8, CC-IMPACT-2, CC-IMPACT-3, CC-IMPACT-6, CC-IMPACT-7); CC-SPEC-1 is enforceable only as an opinion. The CC-SPEC family's lack of a named actor is defensible — it is a rubric applied at the CC-SPEC-10 acceptance act — but the CC-IMPACT family's is not, because CC-IMPACT-2's actor is *the specific thing the fixture said was missing*.

---

## G. Does CC-IMPACT-1…7 close the fixture's step-2 hole?

**The hole, quoted** (fixture L23–31):

> 2. **Affected-spec enumeration** — a blast-radius sweep over the spec corpus for every requirement citing the amended clause or consuming its vocabulary, with its denominator recorded. **This step has no owner in any authority today**… Detection is the open half of E6.

**Walking the fixture's scenario against the new clauses.** Amendment: RFC6-19 gains a facet-folding prohibition; RFC2-24's reason vocabulary gains one owner-approved reason. Corpus: 12 mock requirements across 4 mock specs. Golden answer: impacted = FAC-2, FAC-3, **FAC-1**, **QRY-1**.

| Step | Clause | Result |
|---|---|---|
| Is a sweep required at all? | CC-IMPACT-2 | **Closed.** "The sweep is part of the change, not a follow-up task." This is the real gain. |
| Who runs it? | — | **Still open.** CC-IMPACT-2 is passive voice; CC-IMPACT-5 assigns an actor to *amendments*, not to detection. The fixture's words were "this step has no owner"; after CC-IMPACT-1…7, detection has a *requirement* and still has **no owner**. |
| FAC-2, FAC-3 (direct citation) | CC-IMPACT-1 + 2 | **Found.** Declarations name RFC6-19 and RFC2-24. |
| FAC-1 (impacted at one remove, through RFC6-18's fact-set contract) | CC-IMPACT-2's "or whose requirements consume its vocabulary" | **Stalls.** FAC-1 declares RFC6-18, not RFC6-19. "Consumes its vocabulary" is **undefined**, and no clause establishes transitive closure over contract-clause dependencies. Best case CC-IMPACT-4 renders it `undecidable → Unknown`, which is honest. Worst case — and the clause permits it — the sweeper decides "no declaration, no literal citation" and files FAC-1 under `explicitly unaffected` with the reason "does not declare RFC6-19". That reason is **true** and the answer is **wrong**. |
| QRY-1 (the new prohibition changes what a lawful rendered answer is) | CC-IMPACT-1…4 | **Stalls harder.** QRY-1 declares RFC6-13. There is no declaration tie and no vocabulary tie of any kind — the impact is a *semantic consequence* two steps out. Under CC-IMPACT-3 it lands in `explicitly unaffected`, with a defensible reason, and CC-IMPACT-4 never fires because the sweep did not find it undecidable. |
| The blind exercise | CC-IMPACT-7 | **Cannot grade.** No pass criterion (F), and the fixture it would run against is internally contradictory (finding 8): the fixture's governing step 4 says CC-REV-2 "admits **no exception limb**… withdrawn", while its own ANSWER L89–92 grades the correct response as "the same logical change, **or a recorded exception** naming FAC-1's one-remove impact". A reviewer who answers correctly per step 4 is marked divergent by the ANSWER. |

**So: the hole is roughly half closed.** CC-IMPACT-1…7 converts detection from "nobody's job, no shape" into "a required deliverable with a defined output shape and an anti-silence rule". That is real progress against E6's *interim disagreement* limb. It does **not** close E6's *detection* limb: the sweep has no owner, "vocabulary consumption" is undefined, and the fixture's own headline lesson — "a sweep matching only literal clause citations misses it, which is why the enumeration must follow declared vocabulary consumption, not string match alone" — is restated as a requirement without a method. Worse, the policy **upgrades the failure mode**: before, a missed spec was silence; after, a missed spec is a *documented, reasoned, denominator-carrying claim of "unaffected"* that a reader has every reason to trust. VIS-2's own violation example is "a stale view silently green"; CC-IMPACT-3 as written can produce a stale view **confidently** green.

**Would these policies, in force, have prevented a specification accepted on a vibe? Worked example of an acceptance that passes every clause and is still wrong.**

*Spec: "Capability 1 — repository registration."* Five requirements, REG-1…REG-5.

- **CC-SPEC-1** ✓ one capability, in/out stated, one-sentence summary.
- **CC-SPEC-2** ✓ REG-1 names VIS-2; REG-2 names RFC3-5; REG-3 names RFC7-40; REG-4 names decision path `decisions/HUMAN-ENTRY-DECISION.md`; REG-5 names VIS-5.
- **CC-SPEC-3** ✓ identifiers minted once.
- **CC-SPEC-4** ✓ all five carry four parts. REG-1's oracle: "the rendered value equals the value the registration store returns for that key" — judgment-free, and tautological; nothing forbids it.
- **CC-SPEC-5** ✓ non-goals listed; two Unknowns rendered with reasons.
- **CC-SPEC-6** ✓ — the author judged that no requirement settles an open question. Nobody checks (F).
- **CC-SPEC-7** ✓ no stack named.
- **CC-SPEC-8** ✓ coverage matrix produced. **RFC1-3 (consent) is marked reviewed N/A** — "consent is not user-observable at registration" — by the same author, since no confirmer is assigned.
- **CC-SPEC-9** ✓ a fresh reader restates the capability correctly. She restates *what is there*.
- **CC-SPEC-10** ✓ owner adopts at digest `a1b2…`.
- **CC-IMPACT-1** ✓ declarations present: capability `CAP-1`, rules VIS-2/VIS-5, clauses RFC3-5/RFC7-40, topology `intent/`.

Every one of the seventeen clauses is satisfied. The spec is still wrong: **the consent flow is absent**, because "applicable" (CC-SPEC-8) is an unassigned judgement and no clause asks whether the requirement set *covers* the capability (D). CC-SPEC-9's fresh reader restates the spec faithfully and has no way to notice a requirement that was never written — CC-REV-4's test is comprehensibility, not completeness. And because REG-3's warrant is P-38 territory, which is **pending**, the spec has quietly selected an arm of an open owner question — the exact CC-SPEC-6 violation, invisible because CC-SPEC-6 assigns no one to look.

**Judgement on the vibe question.** The policies do not eliminate the vibe check; they **relocate and shard** it. One unstructured judgement becomes seventeen structured ones, of which at least four remain pure unassigned judgement (coherence, applicability, would-settle, restatement). That is a genuine improvement — a sharded judgement is auditable and a vibe is not — but E5's failure condition is stated as "spec acceptance would be a vibe check **by whoever reviews it**", and after CC-SPEC-1…10 the applicability judgement in CC-SPEC-8 is still a vibe check by whoever reviews it, with no independent confirmer, in a corpus whose own approved clauses (CC-TEST-4, CC-REV-1) name a confirmer for every comparable judgement.

---

# Findings

### 1 — CC-IMPACT-6 weakens the owner-approved CC-REV-2 by side-clause, and its exception has no confirmer — **blocking**
**File:** `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L69–79**
**Evidence:** CC-REV-2 (`policies/craft-and-care/review-and-documentation.md` L57–65) enumerates "**behavioral specs (`openspec/`)**" first among the artifacts that must move in the same logical change, and states "no merge may leave mainline with an invalidated authoritative artifact still asserting the old truth." CC-IMPACT-6 "adds exactly one lawful alternative" permitting exactly that state. Both would sit in cluster tier 2, where `craft-and-care/README.md` L44–45 supplies no arbitration ("a *lower* layer … can never weaken it" addresses cross-tier only). No second party confirms the exception, unlike CC-TEST-1 and CC-TEST-4 ("never made by the implementing agent alone … confirmed by the change's reviewer"). The fixture at L36–41 records this same limb as previously **invented and withdrawn**.
**Fix:** Do not create the limb here. Either (a) strike CC-IMPACT-6's exception and let CC-REV-2 stand, or (b) if the owner wants the limb, carry it as a **semantic delta amending CC-REV-2 in place** through the craft-amendment route, and require a confirmer distinct from the change's author on the CC-TEST-4 pattern.

### 2 — CC-SPEC-2's rationale asserts as owner rulings five decisions that are all pending — **blocking**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L33–35**
**Evidence:** The text: *"a requirement implementing a **recorded owner decision** had no lawful warrant to cite, and the first specification is full of them: P-31, P-36, P-37, P-38 and P-40 are all owner rulings that Capability 1 must implement."* `decisions/PENDING-OWNER-DECISIONS.md` L3: *"**Status: every item below is PENDING. This file decides nothing, adopts nothing, accepts nothing.**"* Each named packet opens identically — `SPECIFICATION-GRANULARITY-DECISION.md` L3, `PROJECT-SHAPE-FACETS-DECISION.md` L3, `HUMAN-ENTRY-DECISION.md` L3, `UNKNOWNS-AND-GAPS-DECISION.md` L4: "**This file decides nothing.**" None of the five is a ruling. The sentence "the first specification is full of them" describes a specification that does not exist.
**Fix:** Replace with the true statement — these are *queued* decisions whose rulings, once made, would become citable under source 3 — and state explicitly that a **pending** decision is not a lawful warrant (which is what CC-SPEC-6 requires anyway). Label the forward-looking claim `[Inferred]` or delete it.

### 3 — CC-SPEC-1's operative text binds to a pending decision — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L13–14**
**Evidence:** *"The specification names one coherent capability (per the granularity rule, **P-40**)"*. P-40 is an open queue row; its packet decides nothing. If the owner rules differently (or declines), CC-SPEC-1's meaning changes with no amendment — and a bound clause silently re-pointing is what CC-REV-7's discipline exists to prevent. It also puts CC-SPEC-1 in the posture CC-SPEC-6 forbids: content that presumes an open question's answer.
**Fix:** Either inline the granularity rule's text as the clause's own words (making P-40's ruling a confirmation rather than a dependency), or state the clause as conditional and add P-40 to CC-SPEC-1's stated prerequisites. Note that the register already sequences P-41 after P-40 for this reason — the clause should say so.

### 4 — CC-SPEC-2's fifth warrant source names a record class that exists nowhere — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L26**
**Evidence:** `lawfully admitted user need — by the record that admitted it`. Sweep 1: Python `re` `user\s+need` (case-insensitive) over `.syzygy/**` `*.md|*.yaml|*.json`, **353 files → 1 hit**, the clause itself. Sweep 2 (second method, repo-wide, `.md|.py|.json|.yaml|.yml|.txt`, **764 files → 2 hits**): the clause, plus the untracked authoring charter at repo root (`git ls-files | grep -F syzygy_fable` → empty; not in the frozen commit). No admission act, register, or record class is defined by any authority.
**Fix:** Either define the admitting record (which authority admits a user need, in which file, by what act), or strike source 5 until such a record exists. As written it is an unbounded escape hatch in the clause whose stated purpose is to close one.

### 5 — The warrant list omits approved craft clauses and topology identities — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L22–26**
**Evidence:** `craft-and-care/README.md` L36–43 lists the craft cluster as its own authority tier, distinct from doctrine and contracts; 46 approved clauses exist, several of which (CC-PROV-5, CC-OBS-3, CC-TEST-6) directly mandate user-observable behaviour. Separately, `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` L27 makes `topology identities` a declarable reliance and L36 makes them sweep triggers, while CC-SPEC-2 admits neither.
**Fix:** Add two sources — `approved craft policy clause — by clause ID` and `accepted topology identity — by identity` — and reconcile the source set with CC-IMPACT-1's declaration classes so the two policies name one authority set.

### 6 — CC-SPEC-2's "exactly one" is ambiguous and supplies no tie-break — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L19**
**Evidence:** "A requirement traces upward to **exactly one** of these, **and names which**". Worked case in A: a currency-bound Unknown requirement traces genuinely to VIS-2, RFC2-24 and P-36. On the literal reading the requirement is unlawful; on the charitable reading the author must name one and the clause never says which.
**Fix:** Restate as "names **at least one**, and names **every** authority it relies on that CC-IMPACT-1 must declare", plus an explicit precedence sentence if a single primary warrant is wanted.

### 7 — CC-SPEC-4 rejects prohibitions and admits unreachable conditions and tautological oracles — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L43–56**
**Evidence:** See B. REQ-Y ("No surface renders a green status from evidence whose currency bound is undeclared") has no initiating condition and no positive success oracle, yet is falsifiable — so L47–52 rejects it while L55–56 admits it. REQ-X satisfies all four parts with an unreachable initiating condition and an undecidable oracle. The no-tautologies bar adopted by reference governs tests, not spec oracles.
**Fix:** Add (a) "the initiating condition is producible by a party performing the check"; (b) "the oracle is decidable in bounded effort and is not defined by the implementation under test"; (c) an explicit second form for prohibitions and invariants: *scope of quantification, a counterexample schema, and the sweep whose denominator bounds it.*

### 8 — The fixture's golden ANSWER contradicts the fixture's own step 4 — **material**
**File:** `.syzygy/governance/contracts/candidates/round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md` **L36–41 vs L89–92**
**Evidence:** L38–41: *"CC-REV-2 admits **no exception limb** … (An earlier form of this step invented an 'explicit exception with reason and expiry' alternative; no craft clause contains it, and it is withdrawn.)"* L89–92: *"**Responsibility:** the shape amendment's author, in the same logical change, **or a recorded exception** naming FAC-1's one-remove impact explicitly."* A reviewer administering blind, answering step 4(d) correctly from the governing description, is graded divergent by the ANSWER. CC-IMPACT-7 would make this fixture the gate on the first real propagation.
**Fix:** Reconcile in one direction. If CC-IMPACT-6's limb survives finding 1, update step 4 and mark the ANSWER as depending on CC-IMPACT-6; if it does not, strike "or a recorded exception" from the ANSWER. Do not leave both.

### 9 — CC-IMPACT-2's sweep triggers are narrower than CC-SPEC-2's warrant sources — **blocking**
**File:** `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L35–37**
**Evidence:** Triggers are "an accepted doctrine rule, contract clause, or topology identity". CC-SPEC-2 admits owner decisions and user-need records as warrants; CC-IMPACT-1 permits declaring neither. A requirement lawfully warranted by `decisions/HUMAN-ENTRY-DECISION.md` is invisible when that decision is amended — a warranted-but-unsweepable class, which is silent staleness by construction.
**Fix:** Make the two clause sets one set: whatever may warrant a requirement must be declarable under CC-IMPACT-1 and must trigger a sweep under CC-IMPACT-2.

### 10 — CC-IMPACT-1 declarations may diverge from CC-SPEC-2 warrants, defeating the sweep — **blocking**
**File:** `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L19–33**
**Evidence:** Nothing requires the spec-level declaration to be the union of its requirements' CC-SPEC-2 warrants. A spec whose REQ-3 names RFC6-19 while its declaration lists only RFC6-18 satisfies both clauses and is missed by CC-IMPACT-2 — the fixture's FAC-1 case reproduced *inside* the policy meant to catch it.
**Fix:** Add to CC-IMPACT-1: "the contract-clause and doctrine-rule declarations are the union of the warrants named under CC-SPEC-2, plus any further reliance; a declaration narrower than that union is a defect."

### 11 — CC-IMPACT-3 mis-cites its sibling and asserts an absence without the sweep — **material**
**File:** `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L53–56**
**Evidence:** (a) *"…which is the defect **CC-IMPACT-2** exists to fix"* — but the defect described (a rule living only in non-citable operating procedure) is what **CC-IMPACT-3** itself fixes; the file's own table at L106 says CC-IMPACT-2's defect is "detection deferred to a follow-up nobody files". (b) The claim *"the denominator discipline is this repository's verification rule 9, restated here because a rule that lives only in operating procedure is not citable authority"* is a claim of absence made with no sweep: **CC-KNOW-16** in the sibling candidate `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` L245–252 already carries it ("A sweep that returns nothing supports a universal claim only when a second method agrees"), is queued as P-12, and lives in the same directory. If both acts pass, two craft clauses own the denominator rule — CC-REV-3's duplicate authority.
**Fix:** Correct the identifier to CC-IMPACT-3; and either cite CC-KNOW-16 (making CC-IMPACT-3 the spec-corpus *application* of it) or state explicitly why a second home is wanted and how the two are ordered.

### 12 — CC-SPEC-10 drops VIS-4's always-human-gated class — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L89–101**
**Evidence:** See C. VIS-4: *"One class is always human-gated, gate open or not: spec changes touching security posture, privacy or retention obligations, or normative data contracts."* The restatement's stated purpose is future-proofing; the omitted sentence is the limb that binds in exactly that future.
**Fix:** Quote the always-human-gated class in CC-SPEC-10, or reduce the clause to the digest rule plus a bare "adoption is governed by VIS-4" with no gloss on VIS-4's content.

### 13 — CC-IMPACT-7 has no pass criterion, no named actor, and no named fixture — **material**
**File:** `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L81–86**
**Evidence:** "…the reviewer derives the affected, unaffected and undecidable sets without reading the answer, **and the comparison is recorded**." A run that misses FAC-1 and QRY-1 entirely, recorded honestly, satisfies the clause. The clause names no fixture (the only one in the corpus is defective — finding 8), no selector for the reviewer, and no consequence of divergence.
**Fix:** Name the fixture by path and digest; require the reviewer to be fresh-context per CC-REV-1; state the pass criterion (e.g. "the derived affected set equals the golden set, or every divergence carries a recorded disposition per CC-REV-6") and the consequence of failure ("the path is not relied on until a passing run exists").

### 14 — No clause tests a specification for completeness against its capability; E5's "complete" limb is unclosed — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`, whole file (CC-SPEC-1…10, **L13–101**)
**Evidence:** E5 (`launch-gate-pre-specifications.md` L404–406) asks for criteria judging a spec "**complete**, testable, and faithful". Sweep of all ten clause bodies: CC-SPEC-8 is completeness w.r.t. contract clauses; CC-SPEC-5 requires non-goals but not in-scope coverage; CC-SPEC-1 requires scope stated, not covered. **0 of 10.** The G worked example turns on exactly this.
**Fix:** Add a clause requiring that every in-scope behaviour named by CC-SPEC-1 map to at least one requirement, and that the mapping be produced with the spec — the same shape as CC-SPEC-8, over the capability instead of the clause set.

### 15 — CC-SPEC-8's N/A judgement has no independent confirmer, and its home is circular — **material**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L78–82**
**Evidence:** "every applicable clause is covered by a requirement or carries a **reviewed N/A judgment** whose home and provenance follow **the corpus's reviewed-N/A rule**." No identifier is given; the rule is not defined in the approved cluster (0 of 46 clauses). The nearest statement lives in `contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md` L265, which routes the deliverable *back to CC-SPEC-8*: "the coverage-matrix deliverable's named candidate home is the specification-acceptance policy, CC-SPEC-8." Each names the other as owner — no single home (CC-REV-3). And "applicable" is undefined, with no confirmer, contrary to CC-TEST-4's pattern for comparable judgements.
**Fix:** Name the clause (RFC3-15 / RFC3-16(a) if that is the intent) and quote it; define "applicable"; require the N/A judgement to be confirmed by a party other than the spec's author.

### 16 — CC-SPEC-1 mandates one capability; CC-IMPACT-1 contemplates several — **minor**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L13** vs `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L24**
**Evidence:** "names **one** coherent capability" vs "`capability identities — which capability (**or capabilities**) it specifies`".
**Fix:** Make CC-IMPACT-1 singular, or state the exception CC-SPEC-1 permits.

### 17 — CC-SPEC-9 duplicates CC-REV-4 and VIS-3 — **minor**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L84–87**
**Evidence:** CC-REV-4 already binds "every normative artifact" to fresh-reader review at adoption and material amendment, with failures recorded on the artifact's surface; VIS-3 states the same test. CC-SPEC-9 adds "not the reader", which VIS-3 implies. CC-REV-3: documentation "cites … it does not restate them normatively".
**Fix:** Reduce to a citation, or state the one thing it adds that CC-REV-4 does not (if any).

### 18 — Three amendment warrants cite a document absent from the frozen bytes — **minor**
**File:** `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` **L31, L56, L96** ("owner charter §9")
**Evidence:** `git ls-files | grep -F syzygy_fable` → empty; `git log -- syzygy_fable_structured_launch_gate_capability1_prompt.md` → no commits. The warrant for all three amendments is unreadable from a clone. The register's own header (`PENDING-OWNER-DECISIONS.md` L57–60) records this class of defect as previously repaired: "routed most owning records to the git-excluded `_bootstrap/` tree that a clone cannot read."
**Fix:** Cite a tracked artifact (a semantic delta or a decision packet in `decisions/`) that carries the owner's instruction, or commit the charter.

### 19 — Neither candidate carries epistemic labels — **minor**
**Files:** both candidates, whole files
**Evidence:** `craft-and-care/README.md` L64–66: "Substantive claims inside policies are labeled [Observed] (with source), [Inferred], or [Unknown]." Sweep (`grep -c -F` for the three labels): SPEC candidate **0**, IMPACT candidate **0**; installed cluster files carry 1–4 each in README, review-and-documentation and performance files. Finding 2's false claim is precisely what a label would have caught.
**Fix:** Label the substantive claims in the rationale notes and the "why each rule is here" table before the act.

### 20 — CC-IMPACT-3 permits a wrong "explicitly unaffected" and bounds nothing — **material**
**File:** `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` **L42–50**
**Evidence:** `explicitly unaffected — specs examined and found untied, each with the reason` accepts "does not declare the changed identity" as a reason. Against the fixture, that reason files FAC-1 and QRY-1 — 2 of the 4 golden impacted requirements — as unaffected, with a denominator, a reason, and full compliance. Nothing bounds the `undecidable` set either.
**Fix:** Require the unaffected reason to state the *method* that established untiedness and to survive the transitive-consumption test the fixture's expected divergence names; and require any sweep whose method cannot follow consumption to declare that limitation and route the residue to `undecidable` under CC-IMPACT-4 rather than to `explicitly unaffected`.

---

# What I could not test and why

1. **Whether the amendments do what the owner asked.** The warrant, "owner charter §9", is not in the frozen commit (finding 18). I deliberately did not read the untracked charter's §9 beyond confirming its existence and its one `user need` occurrence, to avoid taking the authoring session's intent as a review input. I therefore judged the clauses on their own words only.
2. **Behaviour against a real specification corpus.** No specification exists (`openspec/` absent, and forbidden). Every claim about how CC-SPEC-1…10 and CC-IMPACT-1…7 behave in use is derived from the mock corpus in the fixture plus constructed counterexamples — `[Inferred]`, not `[Observed]`.
3. **Whether CC-IMPACT-2's sweep is mechanisable.** The policy explicitly declines to define implementation (L89–94). I could not test whether "consumes its vocabulary" is decidable, because it is not defined; I could only show it is undefined and show two cases where the undefinedness decides the answer.
4. **The reviewed-N/A rule's actual content.** CC-SPEC-8 points at "the corpus's reviewed-N/A rule" without an identifier. The candidates RFC3-15 / RFC3-16(a) are named only in a routing-matrix cell, and I did not read the RFC modules to confirm those clause texts — anchoring a finding to an unquoted clause would violate verification rule 8. Finding 15 is therefore scoped to the citation's unresolvability, not to the content of whatever it points at.
5. **Digest and validator conformance.** I ran no repository check script (`check_governance.py`, `verify_final_prespec.py`). Nothing in this review depends on a digest, and I quoted no digest.
6. **Coverage of the remaining 123 clause pairs in D.** I classified all 136 pairs by shared subject from the clause texts as read, and report the 13 that share one. The claim that the other 123 are independent is a reading, not a scripted sweep — there is no machine-checkable predicate for "shares a subject", so treat it as `[Inferred]`.
agentId: a3a74f4356350748b (use SendMessage with to: 'a3a74f4356350748b', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 122022
tool_uses: 30
duration_ms: 622897</usage>
