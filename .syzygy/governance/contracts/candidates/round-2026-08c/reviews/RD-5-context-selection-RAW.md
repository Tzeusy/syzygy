# RD-5 — Independent context-selection review

**Commissioned:** 2026-08-06, no authoring context.

# VERDICT
VERDICT: REVISE

---

## 0. Method, and one disclosure that qualifies everything below

The commission asked me to read each fixture's **objective, warrant and risk
class only**, derive my own mandatory set, and *then* read the fixture's
selection and trace.

**[Observed] I did not achieve that separation cleanly, and I am saying so
before any finding.** Each fixture's `**Selection rule trace (RFC11-4).**`
paragraph sits in the file's preamble, *above* the `## Required context`
heading, interleaved with the objective and risk class. My extraction took
everything above `## Required context`, so I read all nine traces before
writing a single derivation. The traces name most of the modules the
selections contain.

What this means for the report:

- **[Inferred] My per-fixture agreement numbers (§1) are biased *toward*
  agreement.** A reviewer anchored on the trace will converge on the trace's
  answer. The honest reading of "I reproduced 4 of 9" is therefore *"at most
  4 of 9, and probably fewer under true blind conditions."* It is an upper
  bound on agreement, which makes the disagreement findings stronger, not
  weaker — I differ from five fixtures *despite* having read their reasoning.
- **[Observed] Everything in §2–§8 is independent of that contamination.**
  Those findings are mechanical sweeps over declared metadata and script
  output, not judgment calls: dependency closure, phase-rule population,
  omission-register coverage, figure recomputation. They would be identical
  had I never opened a fixture's prose.

**[Observed] A second methodological note, which is itself a finding.** The
fixture format puts the answer's reasoning in the same block as the question.
A future reviewer cannot be given "objective, warrant, risk class" without
also being given the trace, unless the files are restructured. **A golden
fixture whose question and answer cannot be separated cannot be used to test a
selector.** Recommend splitting each fixture into a `## Task` block (objective,
warrant, risk class) and everything else below a clear line.

### The derivation rule I applied, stated once

RFC11-4 names its inputs but not the function over them. I applied, uniformly:

1. Select contracts where `applies_to` intersects the surface named in the
   objective, **or** `governs` contains an entity type the objective names.
2. Within each selected contract, take the module(s) owning the affected
   clauses via `05-CONTRACT-INDEX.yaml`'s clause→module map, plus the package
   README (06's final bullet: READMEs carry the deterministic clause-lookup
   rule).
3. Add the governing phase-rule clause of every selected contract
   (RFC11-4, explicit).
4. Risk/change class → the contract owning acts of that class.
5. Doctrine files whose normative statement of an implicated rule is carried
   by no already-selected artifact.
6. Craft policy where the declared risk class names a `CC-*` rule.
7. `depends_on` — **[Unknown]**, no termination rule exists; recorded, not applied.

Rules 5 and 7 are not derivable from the declared metadata. Rule 5 is fixture
9's own formulation, which is the best statement of it anywhere in the package
(`fixtures/context-selection-9-evidence-adapter.md:157-159`) and appears in no
contract. Rule 7 is §8's finding.

---

## 1. Per-fixture agreement (acceptance criterion 1)

**[Observed] I independently reproduced 4 of 9 selections exactly: fixtures 4,
6, 8, 9.** Five differ, by 1–3 files each. None is materially different in the
sense of selecting a different contract set wholesale.

| # | Class | Recorded files | My set | Verdict |
|---|---|---:|---:|---|
| 1 | Polaris narrative | 5 | 8 | **differs by 3** |
| 2 | Trajectory adapter | 8 | 10 | **differs by 2** |
| 3 | Orrery lens | 5 | 6–7 | **differs by 1–2** |
| 4 | Execution profile | 6 | 6 | **identical** |
| 5 | Cross-project Mission | 5 | 7 | **differs by 2** |
| 6 | Doctrine amendment | 6 | 6 | **identical** |
| 7 | Kernel identity | 5 | 7 | **differs by 2** |
| 8 | OpenSpec authoring | 6 | 6 | **identical** |
| 9 | Evidence adapter | 12 | 12 | **identical** |

**[Observed] The pattern is not random.** Of the five **accepted** rev10
fixtures (1–5), I reproduce **one** (fixture 4). Of the four **draft**
fixtures (6–9), I reproduce **three**. The accepted set — the one
`06-CONTEXT-LOAD-MAP.md:47-52` and `TASK-TO-CONTRACT-INDEX.md:69-75` route
readers to — is the less reproducible half.

### Fixture 1 — differs by 3

Recorded: `RFC-0007/README.md`, `RFC-0007/narrative-contract.md`,
`RFC-0002/README.md`, `RFC-0002/rendering-vocabularies.md`,
`doctrine:vision.md`.

I would add:

- **`RFC-0007/rendering-and-surface.md`** — rule 3. The objective ends
  *"re-anchor and resubmit for adoption"*; RFC-0007 is loaded; RFC11-4 says
  *"The mandatory set always includes the **governing phase-rule clause of
  every selected contract** (the module or README text carrying it) — no
  lawful packet omits the boundary rule of a contract it loads"*
  (`rfcs/RFC-0011-context-compiler.md:115-118`). RFC7-38's clause text is in
  `rendering-and-surface.md` §3.13. The fixture instead relies on the README
  restatement (`fixtures/context-selection-1-polaris-narrative.md:47-51`).
  **This is the same disposition fixture 8 records as the defect it was
  repaired for** — see §2.1. The two fixtures apply opposite readings of the
  same parenthetical to the same contract.
- **`RFC-0003/governance-homes-and-owner-acts.md` + `RFC-0003/README.md`** —
  rule 4. *"resubmit for adoption"* is an owner act. Fixtures 4, 5 and 6 each
  pull exactly this pair for exactly this reason, and fixture 4's objective
  (*"prepare the owner-approval ceremony"*) is the same shape. Fixture 1
  disposes of RFC-0003 with *"no governed home change"*
  (`fixtures/context-selection-1-polaris-narrative.md:37-39`), which answers
  RFC3-1..14 (manifests) but not RFC3-16(a)/(b)/(c) (acts) — the module that
  is actually applicable.

**[Inferred] Rule applied by me and not by the fixture:** risk-and-change-class
→ act contract. The fixture's own risk class says *"no code, no security
surface"* but does not say *no owner act*, and the objective contains one.

### Fixture 2 — differs by 2

Recorded 8 files. I would add:

- **`RFC-0008/accounting-reconciliation-and-release.md`** — rule 3. RFC8-32's
  clause text lives there; the loaded `RFC-0008/README.md:239-245` is a
  restatement that says so itself (*"The clause text is in
  `accounting-reconciliation-and-release.md` §3.16"*).
- **`doctrine:trust-and-evidence.md`** — rule 5, applying fixture 9's own
  formulation. The objective says the mapping *"widens what the surface
  reports as live/dispatchable"* — that is a status claim, and VIS-2's
  normative statement (*"No evidence means Unknown, not success"*) is carried
  by no artifact in fixture 2's set. Fixture 9, for a structurally identical
  authorization-bearing adapter change, loads it. **Two adapter fixtures, one
  rule, opposite answers.**

**[Observed] A third, weaker difference I record but did not count.** 06's
"Adapter author" reader-map row was corrected at finding T-5 to add
`RFC-0002/rendering-vocabularies.md` and `RFC-0005/execution-profiles.md`
(`TASK-TO-CONTRACT-INDEX.md:117-126`), on the reasoning that a packet without
them *"was incomplete against the package's own declared dependencies, which
RFC11-6 makes Unknown and blocks launch on."* Fixture 9 carries both. Fixture 2
carries neither and is an adapter-author task. **[Inferred]** T-5's reasoning
was RFC4-13-specific (tier vocabulary, gate-backed route 1) and fixture 2 is a
work-provider adapter, so I accept the fixture's narrowing — but T-5 stated the
rule at row granularity, not clause granularity, and a selector reading T-5
would include them.

### Fixture 3 — differs by 1, arguably 2

- **`RFC-0009/interaction-parity-and-release.md`** — rule 3. RFC9-52's clause
  text. `RFC-0009/README.md:138-142` does not even paraphrase the rule; it says
  only that RFC9-52 *"binds the package, not one module"* and names its clause
  range. That is the thinnest of the three README restatements.
- **[Unknown] `RFC-0003/governance-homes-and-owner-acts.md`.** The fixture's
  own risk class says the channel registry is *"an RFC3-16(a) artifact by
  example list"* and then omits RFC-0003 because *"the proposal does not
  perform the registry's owner act"*
  (`fixtures/context-selection-3-orrery-lens.md:36-38`). Fixture 5's objective
  is also draft-only (*"no execution occurs inside this task"*) and **does**
  load RFC-0003. Two draft-only tasks producing RFC3-16(a) artifacts, opposite
  dispositions. I lean toward including it — you cannot draft a valid
  RFC3-16(a) artifact without the predicate that makes it honored — but this is
  the clearest **ambiguity**, not an error, and I count it as half a
  difference.

### Fixture 4 — identical

Recorded: `RFC-0005/README.md`, `RFC-0005/execution-profiles.md`,
`RFC-0003/README.md`, `RFC-0003/governance-homes-and-owner-acts.md`,
`doctrine:security.md`, `craft:security-and-secrets.md`. My set matches
exactly. RFC-0005 has no phase-rule clause, so rule 3 adds nothing.

**[Observed] One metadata defect this fixture surfaces without being affected
by it.** Its risk class cites **RFC5-18(c)**
(`fixtures/context-selection-4-execution-profile.md:6`), and the "no
constraint lost" section cites it again at :47. `RFC5-18(c)` appears in
`05-CONTRACT-INDEX.yaml` **zero times** — the clause list carries `RFC5-18`
only. A selector handed `RFC5-18(c)` as a warrant clause identity cannot
resolve it through the projection RFC11-4 names. The selection is unaffected
only because the parent clause's module is loaded anyway.

### Fixture 5 — differs by 2

Recorded 5 files. I would add **`RFC-0005/admission-and-boundary.md`** and
**`RFC-0006-cross-surface-selection-query-drawer.md`**.

**[Observed] Both are prescribed by 06's own reader map for this exact role.**
`TASK-TO-CONTRACT-INDEX.md:49`, transcribing 06's "Mission Control / CLI / MCP
spec author" row: *"`rfcs/RFC-0010-mission-control-autonomy.md` ·
`rfcs/RFC-0011-context-compiler.md` · `rfcs/RFC-0005/admission-and-boundary.md`
· `rfcs/RFC-0006-…` · `rfcs/RFC-0003/governance-homes-and-owner-acts.md`"*.
Fixture 5 carries three of the five. It is the only fixture that departs from a
reader-map row **without saying so** — fixture 7 makes the same kind of
departure and labels it explicitly
(`fixtures/context-selection-7-kernel-identity.md:66-74`).

**[Observed] The omission reason misses the applicable clause.** Fixture 5
dismisses RFC-0005 as *"the approving client's admission is the session's
concern, not the draft's"* (`:34-36`). That answers RFC5-4/5-5 (sessions and
machine credentials). It does not answer **RFC5-3**, which is the clause
`RFC-0005 constrains RFC-0010, RFC-0011` is anchored at, and which reads:
*"The two classes are exhaustive, for all present and future clients … no later
contract may introduce one"* (`rfcs/RFC-0005/admission-and-boundary.md`,
RFC5-3). A mission envelope that grants scope to a machine principal
(RFC10-3) is bound by that exhaustiveness. See §3.

### Fixture 6 — identical

Recorded: four doctrine files + `RFC-0003/README.md` +
`RFC-0003/governance-homes-and-owner-acts.md`. My set matches. I had flagged
RFC-0010 as arguable (D3's subject is bounded missions); the fixture moves it
to **suggested with provenance**, which is precisely what RFC11-5 licenses, and
states the reasoning (`:46-52`). I agree with the disposition.

### Fixture 7 — differs by 2

I would add **`RFC-0003/governance-homes-and-owner-acts.md` +
`RFC-0003/README.md`**, on two independent grounds:

1. 06's "Kernel implementer" row names `RFC-0003 governance-homes`.
2. **[Observed] `rfcs/RFC-0002/snapshot-and-evaluation-core.md` declares
   `depends_on: [RFC-0001, RFC-0003, RFC-0005]` in its own front matter.** The
   fixture loads that module and neither RFC-0003 nor RFC-0005. That is the
   exact shape T-5 named as *"incomplete against the package's own declared
   dependencies, which RFC11-6 makes Unknown and blocks launch on."*

**[Observed] The fixture handles this in the right form even though I
disagree with the answer** — it names the departure, gives the rule it applied
(fixture 3's "the adoption ceremony is a different packet"), and moves the
material to suggested (`:66-74`). This is the single best-formed disagreement
in the set: it is *visible*, so a reader can overrule it. Fixture 5's identical
departure is invisible.

**[Observed] Two claims in this fixture are false.** At `:109-112`: *"RFC-0001
and RFC-0002 each travel with their governing phase rule (RFC11-4's
mandatory-inclusion rule): RFC-0001 is a single file carrying its own, and the
selected RFC-0002 README carries the package's — no loaded contract's boundary
rule is missing."* Verified by `grep -F`: the string `schedules` occurs **0
times** in `rfcs/RFC-0001-project-graph-identity-state-planes.md`; the string
`phase` occurs **0 times** in that file and **0 times** in
`rfcs/RFC-0002/README.md`. Neither contract has a phase rule. See §2.2.

### Fixture 8 — identical

Recorded: `RFC-0001`, all three `RFC-0007` modules, `doctrine:vision.md`,
`craft:testing-and-verification.md`. My set matches exactly, including the
forcing of `rendering-and-surface.md` by the `kind: phase-rule` index row —
which the fixture states as its reasoning at `:132-137` and which is the
correct application of RFC11-4.

### Fixture 9 — identical

Recorded 12 files. My set matches exactly. This is the strongest fixture in the
set by a wide margin: it declares its own dependency-closure rule (`:207-214`),
enumerates the twelve unclosed clause citations individually with dispositions
(`:217-224`), names three concrete triggers that would promote RFC-0001 to
mandatory, measures five decomposition alternatives, states the limits of the
index cross-check for doctrine and craft (`:235-240`), and leaves the checklist
item *"Selection produced deterministically"* **unchecked, marked "false by
construction"** (`:312-314`). It is the only fixture that does not imply a
determinism it cannot demonstrate.

I add one omission finding against it: **`craft-and-care/INSTALL-RECORD.md` is
neither loaded nor in the omission register**, despite the fixture stating at
`:201-202` that CC-TEST-2 is act 2's subject and *"the amendment's digest lives
in `craft-and-care/INSTALL-RECORD.md`"*. The index lists that file as a
governance source carrying `rule_ids: [..., CC-TEST-2, ...]`
(`05-CONTRACT-INDEX.yaml:497`). It is applicable by the fixture's own reasoning
and disposed of nowhere. See §4.

---

## 2. Is the selection derivable at all? (acceptance criterion 2)

**[Observed] No. Three of the differences above are ambiguity in the rules;
three are insufficiency in the metadata; two are errors.** Taken together the
"deterministic" claim in RFC11-4 is not yet true for a human, let alone a
machine.

### 2.1 Ambiguity — "the module or README text carrying it"

RFC11-4's parenthetical `(the module or README text carrying it)` admits two
readings, and **the fixture set contains both, applied to the same contract**:

| | Reading | Applied by | On |
|---|---|---|---|
| A | A README restatement satisfies the rule | **fixture 1** (`:47-51`) | RFC-0007 |
| B | Only the clause text satisfies the rule | **fixture 8** (`:124-126`) | RFC-0007 |

Fixture 8 does not merely disagree — it records reading A as **the defect it
was repaired for**: *"its pre-repair draft loaded a README whose phase-rule
text is a restatement pointing elsewhere, and no mechanical check caught it"*
(`fixtures/context-selection-8-openspec-authoring.md:206-209`).

**[Observed] The READMEs settle it against reading A on the facts.**
`rfcs/RFC-0007/README.md:272-279` says *"The clause text is in
`rendering-and-surface.md` §3.13"*; `rfcs/RFC-0008/README.md:239-246` says
*"The clause text is in `accounting-reconciliation-and-release.md` §3.16"*.
Each README states, in the restatement itself, that it is not the clause.

**Fixtures 1, 2 and 3 all take reading A. Fixture 8 takes reading B and calls
A a defect. Nothing in the corpus rules between them.**

### 2.2 Insufficiency — the phase-rule universal has no population for 5 of 11 contracts

RFC11-4 says *"every selected contract"*. `05-CONTRACT-INDEX.yaml` carries
`kind: phase-rule` on **6 clauses** (RFC6-28, RFC7-38, RFC8-32, RFC9-52,
RFC10-16, RFC11-12) out of **353 clause rows**. **RFC-0001, RFC-0002, RFC-0003,
RFC-0004 and RFC-0005 have no phase-rule clause at all** — verified two ways:
no `kind: phase-rule` row in the index, and a Python `re` sweep of all 32
module files for `schedules nothing|not a specification of record|phase.rule|
Phase boundary|OpenSpec seam` returns zero structural hits in those five
contracts. The §7 sections fixture 9 points at
(`fixtures/context-selection-9-evidence-adapter.md:196-198`, *"RFC-0004's phase
and deferral rules are in its README §7"*) are titled **"Deliberately
deferred — package-level"** in RFC-0002, RFC-0004 and RFC-0005 alike. A
deferral list is not a boundary rule.

**[Observed] All nine fixtures load at least one of those five contracts.**
F1 → RFC-0002; F2 → RFC-0003, RFC-0004; F3 → RFC-0002; F4 → RFC-0003,
RFC-0005; F5 → RFC-0003; F6 → RFC-0003; F7 → RFC-0001, RFC-0002;
F8 → RFC-0001; F9 → RFC-0002, RFC-0003, RFC-0004, RFC-0005.
Denominator: 9 of 9.

So the rule *"no lawful packet omits the boundary rule of a contract it
loads"* is **unsatisfiable by every fixture in the set**. This is not the
fixtures' error — it is a defect in RFC11-4's universal quantifier, or a gap
in five contracts. Either way it is the finding a selector implementation hits
first. See §8.

### 2.3 Insufficiency — `depends_on` has no termination rule

RFC11-4 names *"contract dependencies (`depends_on` / `provides_to`)"* as a
deterministic selection input and states no closure rule. Fixture 9 is the only
fixture that notices, and declares its own (`:207-211`):

> *first-order edges of every loaded module, satisfied by loading at least one
> module of the depended-on contract; where an edge is not satisfied, the cited
> clauses are enumerated and disposed of individually.*

**[Observed] Applying that rule mechanically to all nine fixtures — module
front matter, not the index — every one leaves at least one edge unsatisfied:**

| Fixture | Loaded contracts | Unsatisfied first-order `depends_on` |
|---|---|---|
| 1 | 0002, 0007 | 0001, 0003, 0004, 0005, 0006, 0009 (6) |
| 2 | 0003, 0004, 0008 | 0001, 0002, 0005, 0006, 0007 (5) |
| 3 | 0002, 0009 | 0001, 0003, 0004, 0005, 0006, 0007, 0008 (7) |
| 4 | 0003, 0005 | 0001, 0002, 0004 (3) |
| 5 | 0003, 0010, 0011 | 0001, 0002, 0004, 0005, 0006, 0008 (6) |
| 6 | 0003 | 0001, 0002, 0004, 0005 (4) |
| 7 | 0001, 0002 | 0003, 0004, 0005 (3) |
| 8 | 0001, 0007 | 0002, 0003, 0004, 0005, 0006, 0009 (6) |
| 9 | 0002, 0003, 0004, 0005 | **0001 (1)** |

Denominator: 9 fixtures, 32 modules, edges read from each module's own front
matter. **Only fixture 9 discloses its open edge as an edge.** The other eight
dispose of contracts by topic (*"not cited by the warrant's clause set"*),
which is a different and unstated rule.

**[Observed] Transitive closure is not a viable alternative.** Computing the
full `depends_on` closure from each fixture's seed contracts:

| Fixture seeds | Closure | Modules | Words | Est. tokens |
|---|---:|---:|---:|---:|
| F1 / F8 (RFC-0007) | 9/11 | 30/32 | 93,610 | **126,374** |
| F2 | 9/11 | 30/32 | 93,610 | **126,374** |
| F3 | 9/11 | 30/32 | 93,610 | **126,374** |
| F5 | **11/11** | **32/32** | 102,623 | **138,541** |
| F4 / F6 / F7 / F9 | 5/11 | 18/32 | 50,157 | **67,712** |

The whole corpus is 32 modules / 102,623 words / 138,541 est. tokens. **Closing
the edges yields 91–100% of the corpus for five fixtures and 56% for the other
four — the minimum being 3.4× the decomposition trigger.** RFC-0002..RFC-0005
form a mutual `depends_on` clique, so loading any one of them transitively
pulls the whole kernel; RFC-0005's `depends_on` reaches back into RFC-0004,
which reaches RFC-0003, and so on.

**This is exactly the rev9 failure RFC-0011 exists to abolish** — *"whole-corpus
loading was the only safe instruction, which OD-R10-3 rules an architecture
problem"* (`rfcs/RFC-0011-context-compiler.md:55-56`). The contract names a
selection input which, under the only closure rule anyone could derive from the
text, reproduces the failure. **The narrowing that gets from 138,541 tokens to
the fixtures' 14,724–32,759 is unstated, and it is doing all of the work.**

### 2.4 Insufficiency — doctrine and craft selection is not derivable at all

`05-CONTRACT-INDEX.yaml`'s `governance_sources` block (lines 490–517) carries
`file`, `role`, `words`, and `rule_ids`. It carries **no `governs`, no
`applies_to`, no `depends_on`, no clause rows**. And `rule_ids` is a plain
mention scan — `scripts/build_contract_index.py:36` defines
`RULE_ID = re.compile(r"\b(VIS-\d+|SEC-\d+|CC-[A-Z]+-\d+)\b")` and line 166
applies it to whole-file text. So VIS-4 "resolves" to `doctrine/v1.md`,
`doctrine/vision.md`, `craft/engineering-bar.md`, `craft/review-and-documentation.md`
and `craft/security-and-secrets.md` with **no ownership signal distinguishing
them**.

Every one of the nine fixtures selects at least one doctrine file, and four
select craft policies. **None of those selections is derivable from RFC11-4's
declared inputs.** Fixture 9 states this limitation precisely (`:235-240`);
fixtures 6 and 7 state a weaker version (*"The doctrine and craft selections
above were additionally verified against the files directly"*). "Verified by
reading the files" is the honest description — and it is not determinism.

### 2.5 Insufficiency — the clause projection is not faithful

RFC11-4 requires the compiler to *"verify the projection regenerates faithfully
from the governed artifacts"* before selecting from it (RFC11-7). Two defects:

- **[Observed] Six sub-clause identifiers are declared to exist and appear in
  no clause row.** `05-CONTRACT-INDEX.yaml:273` declares
  `"RFC7-1..RFC7-25 (sub-clauses RFC7-2(a)-(c), RFC7-9(a)-(c), RFC7-11(a); …)"`.
  The clause list for RFC-0007 carries `RFC7-11(a)` and **not** RFC7-2(a),(b),(c)
  or RFC7-9(a),(b),(c). The same six are declared in
  `rfcs/RFC-0007/narrative-contract.md:6`, `:591`, `rfcs/RFC-0007/README.md:7`,
  `:41`, `:53-54` and `:284` — and appear as clause text **nowhere in the
  package** (verified by `re` sweep of all three RFC-0007 modules: the only
  hits are those front-matter and summary restatements). Either they do not
  exist and six statements inside act 1's digest set are wrong, or they exist
  unlabelled and the projection cannot resolve them.
- **[Observed] `RFC5-18(c)` and `RFC5-18(e)` are cited at binding strength in
  `rfcs/RFC-0005/execution-profiles.md:200,207,214,224,231` and in fixture 4's
  declared risk class, and appear in the index zero times.**

`build_contract_index.py --check` passes because the generator and the checker
share the same extraction rule. **[Inferred] A projection that regenerates
consistently is not the same fact as a projection that regenerates faithfully**;
RFC11-7 asks for the second and only the first is tested.

### 2.6 Errors (not ambiguity)

- **Fixture 7 `:109-112`** — claims RFC-0001 and RFC-0002 each carry a phase
  rule. Both false; see §2.2.
- **Fixture 9 `:196-198`** — *"Each loaded contract travels with its own
  boundary rule: RFC-0004's phase and deferral rules are in its README §7,
  RFC-0002's and RFC-0005's in their loaded modules and package README."* All
  three §7s are "Deliberately deferred". None of the four loaded contracts has
  a boundary rule.
- **Fixture 5 `:23-24`** — *"16,489 words ≈ 22,260 estimated tokens — inside
  the 15–20k working target."* 22,260 is above the 15–20k target and above the
  20,000 trigger. See §6.

---

## 3. The relation model's effect (acceptance criterion 3)

The two authored edges: `RFC-0005 constrains RFC-0006, RFC-0009, RFC-0010,
RFC-0011` (anchor RFC5-3) and `RFC-0007 constrains RFC-0001, RFC-0002,
RFC-0004, RFC-0008` (anchor RFC7-3).

**[Observed] First, the governing fact: no clause tells a selector to read
this relation.** `CONTRACT-DEPENDENCY-INDEX.md:26-30`: *"Its home if adopted is
**RFC11-4**, which enumerates the deterministic selection inputs today and
names `depends_on` / `provides_to` and clause-level metadata — and does **not**
name `constrains`. Until that clause changes, a conformant compiler would not
read this relation at all."* I confirm this by reading RFC11-4 directly: the
string `constrains` does not appear in `rfcs/RFC-0011-context-compiler.md`.

Under the reading "loading B also pulls A's anchor clause":

| Fixture | Loaded | `constrains` edge triggered | Would add | Improvement? |
|---|---|---|---|---|
| 1 | 0002, 0007 | 0002 ←0007 | nothing (0007 loaded) | **no change** |
| 2 | 0003, 0004, 0008 | 0004 ←0007, 0008 ←0007 | **RFC7-3** | marginal |
| 3 | 0002, 0009 | 0002 ←0007, 0009 ←0005 | **RFC7-3, RFC5-3** | marginal |
| 4 | 0003, 0005 | none | nothing | **no change** |
| 5 | 0003, 0010, 0011 | 0010 ←0005, 0011 ←0005 | **RFC5-3** | **yes — clear** |
| 6 | 0003 | none | nothing | **no change** |
| 7 | 0001, 0002 | both ←0007 | **RFC7-3** | **no — worse** |
| 8 | 0001, 0007 | 0001 ←0007 | nothing (0007 loaded) | **no change** |
| 9 | 0002, 0004 (+0003, 0005) | both ←0007 | **RFC7-3** | marginal |

**[Observed] Honouring `constrains` changes five of nine fixtures: 2, 3, 5, 7,
9.** Four are unaffected.

**[Inferred] Only fixture 5's change is an unambiguous improvement.** RFC5-3
reads *"The two classes are exhaustive, for all present and future clients …
There is no third client class and **no later contract may introduce one**"*.
A cross-project Mission envelope granting scope to a machine principal
(RFC10-3) is directly bound by that. It is also what 06's reader map already
prescribes for the Mission Control role, and — crucially — **it is the clause
fixture 5's omission reason does not address** (§1, fixture 5). Two independent
mechanisms both point at the same missing module. That is the strongest
evidence in this review that the relation carries real information.

**[Inferred] Fixture 7's change is a regression.** RFC7-3 reads *"Nothing cites
the rendering … a narrative artifact is never an admissible evidence artifact"*.
It is a prohibition on treating Polaris output as authority. A kernel identity
author has no way to violate it — the clause binds what may *cite* a narrative,
and identity minting cites nothing. Adding the 5,172-word `narrative-contract.md`
to a packet already 6.8% over the trigger, for a clause the task cannot reach,
is the opposite of what RFC11-11 asks.

**[Inferred] Fixture 9's change is arguable and expensive.** RFC7-3's *"never
an admissible evidence artifact"* is genuinely a constraint an evidence-adapter
author should know. But the packet is already the set's largest at 32,759
tokens; +6,982 tokens for one clause takes it near 40,000. **This is the case
that argues the relation should pull the *anchor clause*, not the contract** —
and no artifact in the package says which.

**[Observed] The dependency index already marks three of the four RFC-0005
edges `(load-covered)`** (`CONTRACT-DEPENDENCY-INDEX.md:89`) because the
constrained contract declares `depends_on` RFC-0005 anyway. Fixture 5 is the
proof that "load-covered" is a statement about the *declared graph*, not about
what gets loaded: RFC-0010 and RFC-0011 both declare `depends_on: RFC-0005`,
the edge is marked load-covered, and fixture 5 **loads neither**. **A relation
discharged by a dependency nobody honours is not discharged.**

---

## 4. Omission records (acceptance criterion 4)

RFC11-6 requires incomplete context to be *"marked incomplete/Unknown with the
gap named"*. Sweep over the full candidate population — 11 contracts, 6
doctrine files, 10 craft-and-care files, topology, history — checking whether
each appears in the mandatory set or the omission register.

**[Observed] Contract coverage: complete in all nine.** Every one of the 11
contracts is either loaded or named in every fixture's register (accounting for
the compressed `RFC-0003/0004/0005/…` form).

**[Observed] Doctrine coverage: five silent omissions in the accepted set, zero
in the draft set.** Denominator 6 doctrine files per fixture:

| Fixture | Loaded | Named in register | **Silent** |
|---|---:|---:|---:|
| 1 | 1 (vision) | 1 (security) | **4** — architecture, trust-and-evidence, v1, README |
| 2 | 1 (security) | 0 | **5** |
| 3 | 1 (architecture) | 1 (security) | **4** |
| 4 | 1 (security) | 0 | **5** |
| 5 | 1 (vision) | 0 | **5** |
| 6 | 4 | 2 | **0** |
| 7 | 1 | 5 | **0** |
| 8 | 1 | 5 | **0** |
| 9 | 2 | 4 | **0** |

Fixtures 7, 8 and 9 each assert this explicitly — *"Every doctrine file is
either loaded or listed here; none is unexplained"*
(`fixtures/context-selection-8-openspec-authoring.md:102-103`) — and the
assertion checks out. **Fixtures 1–5, the accepted set, name between 0 and 1
doctrine files each and leave 4–5 silent.**

**[Observed] Craft coverage: worse.** Denominator 10 craft-and-care files:

- **Fixture 4 names no craft policy at all** — not individually, not
  collectively. It loads `security-and-secrets.md` and the register (`:31-42`)
  contains no craft mention of any kind. **9 silent omissions**, in a fixture
  whose declared risk class is *"security surface, authorization-bearing"*.
- Fixtures 1, 2, 3, 5, 6 dispose of craft collectively (*"all craft policies —
  no governed home change"*, *"craft — not cited by the warrant's clause set"*,
  *"Craft policies — no code, no tests"*). One reason for ten files. **[Inferred]
  A collective dismissal is a reason, but it is not "each with its reason"
  (RFC11-1) and it cannot be checked per file.**
- Fixtures 7 and 8 name the remainder by *topic* rather than filename
  (*"the remaining policies bind observability, performance, provenance,
  review, secrets, and testing duties"*) — resolvable, but not mechanically.
- Fixture 9 names 9 of 10 individually.
- **`craft-and-care/INSTALL-RECORD.md` is silent in all nine**, including
  fixture 9, which cites it by name outside the register (`:201-202`) as the
  home of act 2's digest for a clause in its own mandatory set.

**[Observed] The topology bundle and the historical lane are named in
fixtures 6, 7, 8, 9 and in none of 1–5.**

**Conclusion on criterion 4: the omission registers do not discharge RFC11-6 in
the accepted fixture set.** The four draft fixtures do discharge it, for
doctrine and contracts; craft remains partial everywhere and `INSTALL-RECORD.md`
is universally silent. The quality gradient runs the wrong way — the five
fixtures the load map routes readers to are the five with the weakest registers.

---

## 5. Reproducibility (acceptance criterion 5)

### 5.1 The anchors do recompute

**[Observed] `python3 .syzygy/governance/contracts/candidates/scripts/build_budget_report.py --check`** prints, in full:

```
fixture anchors match regeneration
```

**[Observed] `python3 scripts/check_governance.py`** prints, at CG-18:

```
OK    CG-18  context fixtures recompute — 18 measurements examined, 0 findings
```

and closes with `26 OK, 13 WARN, 0 FAIL (39 checks) — counts derived, not
asserted`. I read the output, not the exit code.

**Denominator for CG-18: 18 = 9 fixtures × 2 measurements.** Confirmed by
reading `cg18_fixture_freshness` in `scripts/check_governance.py`: it recomputes
(a) a sha256 over the files named in the ` ```scripts/context_load.py … ``` `
block, compared against the first hex quotation after `## Packet digest`, and
(b) the first `Measured: **N words` figure. **That is all it recomputes.**

### 5.2 Measurements that nothing recomputes — and five that are wrong

**[Observed] The nine fixtures contain 88 measurement-shaped figures. CG-18
covers 18.** The remaining ~70 — every `≈ N estimated tokens` figure outside
the headline, every waiver-table figure, every decomposition-alternative
measurement, every suggested-addition word count — are transcriptions checked
by nothing.

**[Observed] Five of the nine fixtures carry a token figure that contradicts
their own headline.** All headlines are `words × 1.35` and all are correct;
the secondary figures are stale:

| Fixture | Headline | Secondary figure (waiver / checklist) | Implied word count | Matches |
|---|---:|---:|---:|---|
| 2 | 18,362 w | **"8 files, 18,282 words"** (`:47`) | 18,282 | nothing — not the current figure, not the recorded previous (18,315) |
| 6 | 15,556 tok | **15,574** (`:153`) | 11,536 | the footer's "Previous: 11,537 words" |
| 7 | 21,361 tok | **21,285** (`:43`, `:171`) | 15,767 | the footer's "Previous: 15,767 words" |
| 8 | 30,262 tok | **30,048** (`:49`, `:197`) | 22,258 | the footer's "Previous: 22,258 words" |
| 9 | 32,759 tok | **32,433** (`:86`, `:299`) | 24,024 | **nothing** — and this fixture's footer says *"No previous figures exist: this fixture is new."* |

**[Observed] The stale figure is in every case the one the budget disposition is
reasoned against.** Fixture 7's justification argues about *"21,285 estimated
tokens exceeds the 20,000-token line"*; the true figure is 21,361. Fixture 8's
waiver is written against 30,048; the true figure is 30,262. The headline the
check verifies and the number the argument uses are different numbers.

**[Observed] One stale figure has propagated into the generated report.**
`CONTEXT-BUDGET-REPORT.md:74` and `:83` both state *"RFC-0001 is indivisible
(8,353 w …)"*, copied verbatim out of fixtures 7 and 8. `CONTEXT-BUDGET-REPORT.md:107`
— thirty lines later, in the same generated file, in the table the generator
computes — states `| rfcs/RFC-0001-project-graph-identity-state-planes.md | 8,342 |`.
Fixture 9 says 8,342 (`:250`). **The generated report contradicts itself by 11
words because §2 transcribes fixture prose and §3 measures the file**, under a
banner reading *"Do not edit by hand, and do not copy a figure out of it"*
(`:3-4`).

**Answer to criterion 5:** the anchors recompute, verified twice by independent
code. **Roughly 70 of 88 fixture measurements are recomputed by nothing, at
least five of them are demonstrably stale today, and one has leaked into the
generated report.** The fix is mechanical and mirrors T-2's: make the
token/word figures references to the budget report rather than transcriptions,
or extend CG-18 to every `\d,\d{3}` in a fixture.

---

## 6. Budget dispositions (acceptance criterion 6)

**[Observed] The count is five, not four.** `CONTEXT-BUDGET-REPORT.md:45`:
*"**5 of 9 fixtures are above the proposed 20,000-token trigger.**"* Fixtures
2 (+23.9%), 5 (+11.3%), 7 (+6.8%), 8 (+51.3%), 9 (+63.8%). The commission's
brief says four; the generated report is right and the brief is one behind.

**[Observed] Honesty about the threshold: excellent, uniformly.** The report's
banner (`:9-16`) states that `CC-BUDGET-1` *"is **installed nowhere**"*, that
*"A waiver against a rule that does not bind is a different object from a
waiver against one that does"*, and that every row says `candidate budget
exception`, never `waiver`. Fixtures 6, 7 and 8 each carry the same disclosure
in their own words. Fixture 9 cites `CC-BUDGET-1` by identifier **and**
immediately marks it *"candidate material, binding nothing"* (`:87-89`). I
find no dishonesty about the non-installed threshold anywhere in the set.

**[Observed] Fixture 2, 7, 8, 9 dispositions are checkable.** Each has a named
reviewer (RC-12, dated, with the reviewer's own verdict `EXCEPTIONS` disclosed
rather than laundered), a scope with explicit exclusions, and an expiry with an
"earlier of (a)/(b)" structure. The scopes are specific enough to falsify:

- Fixture 7's *"where CC-BAR-5 floor 7 is the declared classifier"* and its
  early-revisit *"any change that makes RFC-0001 divisible"* are both testable
  facts.
- Fixture 9's *"where the warrant spans the retention × cause coupling — i.e.
  where a `reduced-fidelity` cause depends on a retention-horizon fact"* is the
  sharpest scope in the set: it names a coupling, not a topic, and it names the
  out-of-scope case (*"A warrant touching labels only … takes the smaller shard
  instead"*).
- Fixture 2's early-revisit condition (iii), *"If a budget rule is installed
  whose number is not 20,000"*, is the correct handling of the non-installed
  threshold.

**[Observed] One disposition is unfalsifiable because it is empty, and one
fixture is worse than unfalsifiable — it is false.**

`CONTEXT-BUDGET-REPORT.md:62-69`, fixture 5's row, in full:

```
- **Measured:** 16,489 words ≈ 22,260 estimated tokens — 11.3% above the proposed trigger.
- **Reason:** [Unknown] — not declared in the fixture
- **Scope:** [Unknown] — not declared in the fixture
- **Reviewer:** [Unknown] — not declared in the fixture
- **Expiry / revisit trigger:** [Unknown] — not declared in the fixture
- **Decomposition reviewed:** [Unknown] — not declared in the fixture
```

The generator is doing exactly the right thing — *"A missing field renders
`[Unknown]`, never blank and never `none`"* (`:50-51`). **The fixture is not.**
`fixtures/context-selection-5-cross-project-mission.md:23-24` still reads:

> Measured: **16,489 words ≈ 22,260 estimated tokens** — inside the
> 15–20k working target.

**This is a live false statement in an accepted-set fixture.** 22,260 is neither
inside 15–20k nor under the 20,000 trigger. The fixture has **no exception
section at all** — the only breaching fixture without one. And fixture 2
received a documented repair for a *weaker* version of this exact fault:

> **Correction, 2026-08-06 (RC-12 finding F-1).** The sentence above previously
> named only the 15–20k *working target* and never the 20,000-token
> *decomposition trigger* it actually crossed. A reader checking this fixture
> against §11.4 found no acknowledgment that §11.4 had been crossed at all
> (`fixtures/context-selection-2-trajectory-adapter.md:35-41`)

Fixture 2 at least named the working target it exceeded. **Fixture 5 claims to
be inside it.** RC-12's F-1 repair was applied to one fixture and not swept
across the set. Three fixtures (7, 8, 9) grew past the trigger and gained
justification sections; fixture 5 grew past it — from a recorded 12,843 words
to 16,489, per its own footer — and its prose was never revisited.

**[Observed] Decomposition reviews are declared inconsistently.** The report
marks *"Decomposition reviewed: [Unknown] — not declared in the fixture"* for
fixtures 2, 8 and 9. Fixtures 8 and 9 **do** contain decomposition tables
(three splits and five respectively, with measurements) — the generator's field
extractor does not find them because they sit outside the disposition table.
**[Inferred]** That is a generator gap producing a false `[Unknown]`, which is
the safe direction but still a wrong fact in a generated artifact: it under-credits
the two fixtures that did the most decomposition work.

---

## 7. Class coverage (acceptance criterion 7)

| # | Required class | Fixture | Exercised? |
|---|---|---|---|
| 1 | doctrine amendment | 6 | **yes** — both amendment sites mandatory |
| 2 | graph identity change | 7 | **yes** — RFC1-11 minting/continuity |
| 3 | OpenSpec capability authoring | 8 | **yes** — RFC1-14/15 + RFC7-38 |
| 4 | evidence-adapter change | 9 | **yes** — RFC4-13 routes, RFC4-24/25 |
| 5 | Polaris presentation change | 1 | **yes** — RFC7-11(a) target-changed anchors |
| 6 | Trajectory lifecycle change | 2 | **nominally only** — see below |
| 7 | Orrery lens change | 3 | **yes** — RFC9-24..35 channel + lens contract |
| 8 | bounded Mission spanning capabilities/projects | 5 | **partially** — see below |
| — | *(unmapped)* | **4** | security / execution-profile change |

**[Observed] No class is uncovered. One fixture (4) maps to no required
class.** That is fine as an extra, and fixture 4 is the one selection I
reproduced exactly among the accepted set — but it means the eight classes are
covered by eight fixtures, not nine, and the redundancy the count implies is not
there.

**[Observed] Class 6 is covered by a fixture that does not exercise it.**
Fixture 2's objective is *"amend the substrate-to-normalized work-state
derivation mapping for a work-provider adapter"* — an **adapter** change. Its
selection is 3 RFC-0004 modules and 2 RFC-0008 modules, and the two RFC-0008
modules it **omits** are `identity-authority-materialization.md` (RFC8-1..11 —
work identity, authority, dispatch, materialization) and
`accounting-reconciliation-and-release.md` (RFC8-21..32 — accounting,
reconciliation chain state, release). **Work lifecycle is precisely what is
omitted**; what is exercised is the work-state *vocabulary* (RFC8-12/13).

Worse, fixtures 2 and 9 are both adapter fixtures and say so about each other:
fixture 9 at `:148-150` — *"Fixture 2 is that task; this one is its
complement"*. **The adapter class is double-counted across classes 4 and 6, and
no fixture exercises Trajectory dispatch, materialization, accounting or
release.**

**[Inferred] Class 8 is partially exercised.** Fixture 5 is a two-*project*
mission and covers the portfolio-authority half well (RFC10-15, RFC10-9). The
class as commissioned says *"spanning capabilities/projects"*; fixture 5's
selection contains no capability contract — RFC-0001 (which owns capability
identity, RFC1-14) is omitted with the reason *"no kernel-entity … change in the
drafting task"*. A mission spanning **capabilities** would need RFC1-14. The
capability half of the class is untested.

**Recommendation:** either re-scope fixture 2 to a genuine Trajectory lifecycle
task (dispatch or materialization, pulling `identity-authority-materialization.md`),
or add a tenth fixture for it and re-label fixture 2 as a second adapter case.

---

## 8. What would break first (acceptance criterion 8)

**[Inferred] The first thing a selector built tomorrow against RFC11-4 and this
metadata gets wrong is the phase-rule universal — and the way it gets it wrong
is that it refuses to compile anything touching the kernel.**

The chain is short and entirely mechanical:

1. RFC11-4: *"The mandatory set always includes the **governing phase-rule
   clause of every selected contract** … no lawful packet omits the boundary
   rule of a contract it loads"* (`rfcs/RFC-0011-context-compiler.md:115-118`).
2. The projection RFC11-4 names carries `kind: phase-rule` on 6 of 353 clause
   rows, covering RFC-0006 … RFC-0011. **RFC-0001 through RFC-0005 have none**,
   and none exists in their text either (§2.2).
3. RFC11-6: *"If required context cannot be determined … the packet is marked
   **incomplete/Unknown with the gap named**, and **by default the run does not
   launch**"*.
4. **All nine golden fixtures load at least one of RFC-0001..0005.** A
   conformant selector therefore blocks on all nine.

The selector is not malfunctioning — it is correctly fail-closed on metadata
that asserts a universal its population does not satisfy. But the observable
outcome is that **the nine artifacts offered as proof that deterministic
selection works are the nine a conformant implementation cannot produce.**

The second thing it gets wrong, immediately after someone patches around the
first, is `depends_on` termination (§2.3): with no closure rule, the natural
implementation closes transitively and hands back 91–100% of the corpus,
reproducing OD-R10-3's architecture problem inside the contract written to
abolish it. The fixtures avoid this by an unstated narrowing that exists only in
the authors' judgment, and the nine fixtures apply at least three different
versions of it (fixture 9's declared first-order rule; fixtures 1–5's topical
"not cited by the warrant's clause set"; fixture 7's reader-map departure rule).

Third, and cheapest to fix: doctrine and craft (§2.4). A selector asked "which
file owns VIS-4?" gets five files from a regex mention scan and no way to
choose. Every fixture selects doctrine; no fixture's doctrine selection is
derivable.

### The minimum set of repairs that would make a selector possible

1. **Give RFC-0001..0005 a phase-rule clause, or narrow RFC11-4's universal to
   the contracts that have one.** Until then RFC11-4 is unsatisfiable.
2. **State the `depends_on` termination rule in RFC11-4.** Fixture 9's
   formulation is ready to lift verbatim and is the only one anyone wrote down.
3. **Resolve the "module or README text carrying it" parenthetical** — fixtures
   1 and 8 currently disagree about the same clause of the same contract, and
   fixture 8 records fixture 1's reading as a defect.
4. **Add `governs` / `applies_to` to `governance_sources`**, or state that
   doctrine and craft selection is judgment and not claimed to be deterministic.
5. **Repair fixture 5's budget prose and give it an exception row**, or shard it.
6. **Extend CG-18 past the headline** to every measurement figure in a fixture.
7. **Register `craft-and-care/INSTALL-RECORD.md`** in all nine omission
   registers; complete the doctrine registers in fixtures 1–5.

---

## 9. Why REVISE and not EXCEPTIONS

**[Observed] The package is unusually honest about its own limits.** The
dependency index says a conformant compiler would not read `constrains`. The
budget report says 5 of 9 breach, renders fixture 5's fields `[Unknown]`, and
states the threshold binds nothing. Fixture 9 leaves *"Selection produced
deterministically"* unchecked and writes *"false by construction."* Every
fixture carries *"Selection: hand-authored … Compiler implementation: absent."*
That candour is the reason this review could be done at all, and it is worth
saying plainly.

**But three findings are defects requiring repair, not disclosures:**

1. **Fixture 5 states, today, that a 22,260-token packet is "inside the 15–20k
   working target."** A reader who loads that fixture as a worked example is
   told a false thing about the one number the fixture exists to demonstrate.
   The repair that fixed the same fault in fixture 2 was not swept.
2. **Fixtures 1 and 8 apply opposite readings of RFC11-4's phase-rule
   parenthetical to the same contract, and fixture 8 documents fixture 1's
   reading as the defect it was repaired for.** A golden set cannot contain both
   the standard and its counter-example, unlabelled.
3. **RFC11-4's phase-rule universal has no population for 5 of 11 contracts**,
   which makes every fixture in the set unlawful under a literal reading — and
   two fixtures (7 and 9) assert the opposite in prose that a `grep -F` refutes.

And the headline: **I independently reproduced 4 of 9, having been anchored by
reading every trace first.** Under blind conditions the number would be lower.
The claim RFC11-4 makes is *"same inputs, same selection."* Two competent humans
with the same metadata and the same rules produced different selections for five
of nine tasks, and disagreed about *which rule to apply* — not about how to
apply it — in every one of those five. **That is what "deterministic mandatory
selection is not yet true even for a human" looks like, stated as evidence
rather than as opinion.**

The corpus is close. Repairs 1–3 above are small and local; 4–7 are mechanical.
None requires re-authoring a contract's semantics. But the fixture set cannot
be offered as evidence for RFC11-4's determinism claim in its current state.

---

*End of RD-5 raw output. Verdict word: REVISE. Independently reproduced: 4 of 9
(upper bound — see §0). All script output read as output, not exit code:
`build_budget_report.py --check` → "fixture anchors match regeneration";
`check_governance.py` → "26 OK, 13 WARN, 0 FAIL (39 checks)", CG-18 "18
measurements examined, 0 findings". All load-bearing pattern matching done with
Python `re` or `grep -F`, never a bracket class.*
