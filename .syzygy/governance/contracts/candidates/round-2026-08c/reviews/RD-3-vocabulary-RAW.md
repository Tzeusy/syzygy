# RD-3 — Public vocabulary comprehension review

**Commissioned:** 2026-08-06, fresh reader, no authoring context.

# VERDICT
VERDICT: REVISE

---

## Reading discipline actually followed

[Observed] I read, in order and once each: `README.md`; `.syzygy/intent/OVERVIEW.md`;
`.syzygy/governance/doctrine/README.md`, `vision.md`, `trust-and-evidence.md`;
`.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md` (all 1550 lines).
I read nothing under `round-2026-08c/`, `round-2026-08b/`, or `round-2026-08/`, and no commit messages.

[Observed] After the fresh-reader pass I ran mechanical verification only — term counts, occurrence
sweeps (Python `re`, not `grep`), `scripts/check_governance.py`, and a *headings-only* listing of
`architecture.md`. I did not narratively read `architecture.md`, `v1.md`, or `security.md`; where I
cite them it is a mechanical fact (a heading exists, a string occurs N times), never a definition
I absorbed. This matters: several findings below are precisely that a definition lives in a file the
reader was not routed to.

**The drawer boundary.** [Observed] `OVERVIEW.md`'s first `<details>` opens at line 143. The default
path is therefore `README.md` (all 130 lines) plus `OVERVIEW.md:1-141`.

---

## A. The default-path bound

### A.1 Every Syzygy-specific term I met on the default path

Column 3 answers: *could I understand the sentence containing it without looking the term up?*

| Term | First default-path site | Sentence understandable in place? |
|---|---|---|
| Syzygy | `README.md:1` | Yes — codename, no load |
| specification-driven **control plane** | `README.md:3` | **No.** This is the project's opening predicate and I could not tell what class of thing was being claimed |
| **desired state** | `README.md:27` | Yes — defined in place, and again at `OVERVIEW.md:41` |
| **observed state** | `README.md:28` | Yes — defined in place |
| **execution state** | `README.md:29` | Yes — defined in place |
| **evidence** | `README.md:29`, `OVERVIEW.md:42` | Yes, loosely; the *durable/identified/integrity-verifiable* load arrives only in doctrine |
| **agent fleet** | `README.md:5, 22` | Yes |
| **doctrine** (VIS-*, SEC-*) | `README.md:36` | Yes, from the authority table |
| **Unknown** (capitalised) | `README.md:38` | Yes — "never green, never zero" is the whole definition |
| **experience** ("The four experiences") | `README.md:40` | **No** — see A.3, this word appears nowhere else in the corpus |
| **surface** (intent/work/map/operator surface) | `README.md:44-47` | **No** — used as if defined; see A.3 |
| **Mission Control**, **workspace** | `README.md:47, 50` | **No** for *workspace* |
| **projection**, **kernel** | `README.md:49` | *projection* partially; **kernel: no** |
| **gap**, **contradiction** | `README.md:61` | Gist only; the load-bearing difference arrives at `OVERVIEW.md:158` inside a drawer |
| **adapter** ("typed, explicitly authorized adapters") | `README.md:61, 71` | Gist yes; *typed* and *explicitly authorized* are load-bearing and undefined |
| **candidate / adopted / accepted / recorded / owner-approved** | `README.md:79-85` | Mostly yes; *accepted* vs *adopted* vs *approved* I could not distinguish |
| **topology** | `README.md:83` | Yes ("intended placement") |
| **gate** ("exact gate state") | `README.md:12, 101` | **No** — and see A.4, the word carries two unrelated senses |
| **alignment**, **convergence**, **regeneration capability** | `README.md:118-119` | **No** for all three — see A.3 |
| **owner act**, **digest** | `OVERVIEW.md:6` | **No** for *owner act*; *digest* is ordinary engineering vocabulary |
| **reconciliation work** | `OVERVIEW.md:46, 54` | Yes — and the meaning I formed was **wrong**; see A.5 |
| **actuator** | `OVERVIEW.md:47, 55` | Gist yes (fleets are actuators); no definition |
| **warranted work** | `OVERVIEW.md:58` | **No** |
| **kernel** = "a temporal project graph plus an evaluation engine" | `OVERVIEW.md:65` | **No** — the definiens is two undefined terms |
| **evaluation engine**, **temporal project graph** | `OVERVIEW.md:65` | **No** |
| **plane** ("a co-equal plane, not an export") | `OVERVIEW.md:73` | **No** — third distinct sense; see A.4 |
| **conforming integration** | `OVERVIEW.md:74` | **No** |
| **Mission** envelope | `OVERVIEW.md:93-95` | Yes — enumerated in place |
| **evidence bar** | `README.md:81`, `OVERVIEW.md:94` | **No** |
| **escalation conditions** | `OVERVIEW.md:94` | Gist yes; no definition |
| **normative corpus / Project Genome** | `OVERVIEW.md:104-106` | Yes — defined in place |
| **north star**, **foreclosure** | `OVERVIEW.md:102-111` | Yes — defined in place |
| **V0 / V1** | `OVERVIEW.md:134` | **No** — named as a scope split, never as content |
| **project-shape** ("pre-specification project-shape normalization") | `README.md:7` | **No** |

### A.2 Checked against the registry's core set

[Observed] The registry's core table (`TERM-REGISTRY.md:34-46`) has exactly **11 rows**, verified by
script: Project (T-01), Capability (T-04), Desired state (T-07), Observed state (T-09), Execution
state (T-11), Evidence (T-14), Unknown (T-31), Gap (T-20), Contradiction (T-19), Reconciliation
(T-26), Mission (T-27).

**Finding A-1 — the registry contradicts itself about its own core set size, five lines apart.**
[Observed] `TERM-REGISTRY.md:25-26`: *"**The default public path is bounded to the twelve core terms
below.**"* `TERM-REGISTRY.md:30`: *"**Core — the eleven.**"* The table has eleven rows. This is the
same defect class the file successfully diagnoses elsewhere — *"two statements of one rule,
disagreeing about what the rule was, in one file"* (`TERM-REGISTRY.md:118-119`) — reappearing in the
paragraph that announces the bound.

**Finding A-2 — the entry count is stale in four places.** [Observed] Script count: **31** entries
(`T-01`…`T-30` plus `T-31`). The file says "30 entries" at `:11`, "30 entries above" at `:1508`,
"30 entries" at `:1545`, and "thirty terms" at `:1519` and `:1529`. `T-31 · Unknown` was added
2026-08-06 (`:50-56`) and no count was updated with it.

**Finding A-3 — `T-31` is missing from the authority-coverage summary entirely.** [Observed] The §5
table (`:1510-1513`) lists 22 + 8 = 30 term IDs; `T-31` appears in neither row. The omitted term is
the one its own entry calls *"the most firmly held term in the registry and the one with the
strongest adopted backing"* (`:833-834`). A reader who trusts §5 to say which terms are usable as
authority gets no answer for the one core term whose backing is strongest.

### A.3 Default-path terms not in the core set and not defined in place

[Observed] Verified by regex sweep of `README.md` + `OVERVIEW.md:1-141`, and by checking each name
against the 31 registry entry headings.

**Class 1 — advanced registry terms used on the default path.** CG-23 finds two:

```
WARN  CG-23  default-path vocabulary reported — 40 term-in-files examined, 2 findings
        .syzygy/intent/OVERVIEW.md — uses advanced term `Claim` (T-13) 2× on the default path
        .syzygy/intent/OVERVIEW.md — uses advanced term `Evaluation` (T-22) 1× on the default path
```

I find **two more that CG-23 structurally cannot see**: `README.md:118-119` — *"No claim of
**alignment**, **convergence**, or regeneration capability is made anywhere in this repository"*.
`Aligned` (T-24) and `Converged` (T-25) are advanced terms; CG-23 matches only the exact entry head
name at word boundaries (`scripts/check_governance.py:2839`: `re.compile(r"\b" + re.escape(name) +
r"\b", re.I)`), so the nominalisations *alignment* and *convergence* do not match. These are not
throwaway words — VIS-2 names them as the three things no surface may declare without evidence, and
README's denial sentence is the reader's first and only encounter with them.

**Class 2 — default-path terms with no registry entry at all.** The registry names four
(`:97-98`: *kernel*, *surface*, *workspace*, *actuator*) and calls them *"findings, not exemptions"*.
[Observed] I find **at least fifteen**. Verified absent from all 31 entry headings:

| Term | Default-path sites | Occurrences in adopted doctrine tree |
|---|---|---|
| `kernel` | `README.md:49`; `OVERVIEW.md:63, 65` | 7 |
| `surface` (as a noun for a UI plane) | `README.md:24, 44-47, 51`; `OVERVIEW.md:32, 72, 77-85` (14 total) | 35 |
| `workspace` | `README.md:47, 50`; `OVERVIEW.md:86` | **0** |
| `actuator` | `OVERVIEW.md:47, 55` | 5 |
| `experience` | `README.md:40` | **0** |
| `control plane` | `README.md:3` | 1 |
| `plane` (the "co-equal plane" sense) | `OVERVIEW.md:73` | 15, in other senses |
| `evidence bar` | `README.md:81`; `OVERVIEW.md:94` | **0** |
| `conforming` integration | `OVERVIEW.md:74` | **0** |
| `escalation` | `OVERVIEW.md:94` | **0** |
| `gate` (owner-acceptance sense) | `README.md:12, 101`; `OVERVIEW.md:4, 120, 124, 131` | — |
| `owner act` | `OVERVIEW.md:6, 90, 123` | — |
| `V0` / `V1` | `OVERVIEW.md:134` | many |
| `temporal project graph`, `evaluation engine` | `OVERVIEW.md:65` | — |
| `project-shape` / `shape-level` | `README.md:7, 14`; `OVERVIEW.md:116` | — |

**Finding A-4 — the check the registry tells the reader to trust cannot find the leak class the
registry says is worse.** [Observed] `TERM-REGISTRY.md:86-88` says *"`check_governance.py` **CG-23**
performs that sweep and prints its findings on every run… **Read its output rather than this
sentence**; what it finds moves."* But CG-23 builds its search set from the registry itself —
`advanced = {tid: n for tid, n in entries.items() if tid not in core}`
(`scripts/check_governance.py:2817`) — so a term with **no entry** can never be a hit. Its
denominator confirms this: "40 term-in-files examined" = 20 advanced entries × 2 files. A reader
following the registry's instruction to prefer CG-23's output over its prose will conclude the
default path leaks two terms. It leaks at least nineteen.

**Finding A-5 — `experience` is a term with no home anywhere.** [Observed] `README.md:40` heads the
Polaris/Trajectory/Orrery/Mission Control table *"## The four experiences"*. String `experience`
occurs **0 times** in the adopted doctrine tree and **0 times** in the registry. `OVERVIEW.md:77`
calls the same objects *"The three project surfaces"*. So the default path gives the reader three
competing nouns — *experience*, *surface*, *capability* — for one concept, none defined, and the two
documents disagree on the cardinality (four vs three).

**Finding A-6 — README and OVERVIEW contradict each other on whether Mission Control is a surface.**
[Observed] `README.md:47`, in a column headed *"Literal subtitle"*: `| **Mission Control** |
workspace operator surface | …`. `OVERVIEW.md:85`: *"And one thing that is **not** a surface:
**Mission Control**"*. README hedges four lines later — `README.md:50-51`, *"not a fourth project
truth surface"* — but its own table calls it an operator **surface**. On one read I could not tell
whether "surface" is a category Mission Control is in or is excluded from.

**Finding A-7 — the routed word-lookup destination does not hold most of the words.** [Observed]
`README.md:92-95`: *"**Unfamiliar word?** … holds the glossary — **the only one in this
repository**, and the one doctrine means when it says 'README glossary'. This file has none."* The
doctrine README glossary (`doctrine/README.md:15-49`) has seven bullets: Syzygy, Owner, Governed
project, the two namespaces, Polaris/Trajectory/Orrery, substrate tools, rule identifiers. It defines
none of *kernel*, *surface*, *plane*, *evidence bar*, *gate*, *owner act*, *actuator*, *capability*,
*aligned*, *converged*. [Observed] `architecture.md` carries a `### Definitions` section (line 157)
and a `## Vocabulary` section (line 285), and the registry cites `architecture.md, "Definitions"` as
owning authority for T-01, T-04, T-24 and T-25. A newcomer told there is exactly one glossary stops
at a seven-bullet list and never reaches the section that actually defines *Capability*, *Aligned*
and *Converged*. The charitable reading — "glossary" means a section literally titled Glossary — is
available, but it is not the reading a newcomer takes from *"the only one in this repository"*.

### A.4 The word `plane` carries five or six senses, two of them on the default path

[Observed] Senses I met: (1) *control plane* — `README.md:3`; (2) *co-equal plane* meaning
"consumer channel" — `OVERVIEW.md:73`; (3) *orthogonal plane* / *two-namespace plane* meaning the
governance file tree — `vision.md:51`, `doctrine/README.md:31`, `architecture.md` heading line 7;
(4) *state plane* — T-06, an enumerated six-value dimension; (5) *the governed plane* — the commit-out
destination, `trust-and-evidence.md:29`; (6) *enforcement plane* — `TERM-REGISTRY.md:1404`.

§1's own rule (`TERM-REGISTRY.md:161-166`) says: *"**Never use a generic word such as "status",
"state", or "stage" where the dimension matters.**"* By its own logic `plane` now qualifies and the
rule does not name it. T-06 helpfully deprecates *"state used alone for the dimension"* (`:478-480`)
but nothing deprecates *plane* used alone, and *plane* used alone is what the default path does.

### A.5 The core term `Reconciliation` is used on the default path in the sense its own entry reserves against

[Observed] T-26 (`:1278-1280`): *"**Unqualified "reconciliation" means exactly one thing in Syzygy:
the post-merge evaluation of whether a merged change satisfies the intent revision that warranted
it.**"* The deprecated-synonyms block (`:1297-1301`) calls this *"a hard reservation"* and says the
two senses *"never share a field, a count, or a UI string."*

The default path uses two senses, 36 lines apart:

- `OVERVIEW.md:46-47` — *"The computed **difference** between desired and observed becomes
  **reconciliation work**, and agent fleets are the actuators that perform it."* and
  `OVERVIEW.md:54` — `Diff["Reconciliation work"]`. This is the **gap-closing** sense: the delta
  itself, *before* any merge.
- `OVERVIEW.md:82` — *"what merged **without yet being reconciled**?"* This is T-26's post-merge
  sense.

On one read I formed the first meaning, because it arrives first and is the one the narrative builds
on. T-26 then told me that meaning is wrong. [Inferred] This is the single most consequential
comprehension failure in the review, because *reconciliation* is the name of the project's central
loop and the reader forms it early.

The registry anticipates the shape of this: *"a core term used loosely is worse than an advanced term
used precisely"* (`:112-113`). Nothing checks core terms for sense-drift — CG-23 only checks advanced
terms for *presence*.

---

## B. The core set itself

| Term | Genuinely required for the thesis? | Verdict |
|---|---|---|
| **Desired state** (T-07) | Yes — one third of the thesis sentence | Keep |
| **Observed state** (T-09) | Yes | Keep |
| **Execution state** (T-11) | Yes — and it carries the second of the two rules (*"doing the work is never proof"*) | Keep |
| **Evidence** (T-14) | Yes — VIS-2 is unreadable without it | Keep |
| **Unknown** (T-31) | Yes — it *is* VIS-2 | Keep |
| **Gap** (T-20) | Yes, but see B-2 | Keep, repair |
| **Contradiction** (T-19) | Yes — "gaps and contradictions are different findings" is a default-path claim (`OVERVIEW.md:158-160`) | Keep |
| **Reconciliation** (T-26) | Yes | Keep, repair (A.5) |
| **Project** (T-01) | **Marginal.** I understood the whole thesis before meeting it. "one governance root, one owner" is an onboarding mechanic | **Demote** |
| **Capability** (T-04) | **Marginal.** It appears **zero times** on the default path outside the phrase "operator capability" (a different sense). I did not need it | **Demote** |
| **Mission** (T-27) | **Demote — with a caveat.** It is defined in place at `OVERVIEW.md:93-95`, its only authority is candidate RFC-0010, and Group F's own preamble (`:1319-1322`) records that missions *"cannot lawfully operate under unamended doctrine."* A core term whose referent cannot lawfully exist is a strange thing to make required reading | **Demote** |

[Observed] Verification of the Capability claim: the string `capabilit` occurs on the default path at
`README.md:47, 50` (*"workspace operator capability"*), `OVERVIEW.md:86` (same), `OVERVIEW.md:109`
(*"current capability claim"*), `README.md:119` (*"regeneration capability"*) — **not once** in T-04's
sense of "a named unit of declared behavior."

### B-1 — Missing from core: a term for *the difference itself*

The thesis sentence is *"Agents do work to close **the difference**"* (`OVERVIEW.md:17`). Every
default-path artifact names this concept — `README.md:31` "the difference between them",
`README.md:61` `G[Difference]`, `OVERVIEW.md:46` "the computed difference", `OVERVIEW.md:54`
`Diff[…]` — and **the registry has no entry for it**. `Gap` is not it (a gap is one instance;
`README.md:61` lists "gaps · contradictions · Unknowns" as three *kinds* of difference).
`Reconciliation` is not it (post-merge). So the noun at the centre of the thesis is the one noun with
no term. Either it earns an entry or the default path should stop treating it as a defined thing.

### B-2 — Missing from core: `surface` and `kernel`

These are not advanced-vocabulary omissions; they are the two nouns the default path uses most
(`surface` 14× on the default path, 35× in adopted doctrine). A newcomer cannot parse *"Polaris,
Trajectory, and Orrery are **projections over one shared kernel**, never independent truth stores"*
(`README.md:49-50`) without both. The registry agrees they are findings (`:96-102`) and routes a
proposed plain-language replacement to the owner. [Inferred] Given `surface` occurs 35× in **adopted**
doctrine, "the default path stops using it" is not a live option; the term needs an entry and an
owning authority.

---

## C. Five classification exercises

**Preliminary finding C-0 — §1 gives no rule for *which* dimension a statement belongs to.** Each
item below is placeable on two or three of the five simultaneously, which is correct behaviour
(§1's whole point is that they are independent) but means "which dimension does this belong to" has
no single answer. I answer on every applicable dimension.

### C.1 — "The CI gate for capability X passed at commit abc123, and the run log is retained."

- **Evidence tier = `gate-backed`.** [Observed] T-16 (`:882-884`): *"`gate-backed` (a retained,
  resolvable gate artifact bound to the exact revision — **the only tier that may support a positive
  status claim**)"*. All three predicates are satisfied verbatim: retained, gate, exact revision.
- **Claim epistemic label = `Observed`** (deterministic claim with a resolvable evidence link, T-15).
- **State plane = Observed** (T-09: *"code elements, evidence artifacts, observation records,
  verification runs"*).
- **Did I have to guess?** No. This is the registry working exactly as intended.

### C.2 — "An agent read the code and reports that capability X appears to be implemented."

- **I had to guess. This is a finding.** Two registry passages give incompatible answers:
  - T-16 (`:885-886`) — **Inferred / `asserted-by-worker`**: *"an LLM worker's assertion with no
    retained artifact — visible, never green, challengeable, never a status input."*
  - T-14's Misuse (`:767-770`) — **Observed / `report-fact`**: *"'The worker said the tests passed'
    treated as evidence that tests passed. That is Observed **as a report fact** only (SDR-9,
    adopted); `report-fact` supports claims about the report, never about the subject matter."*
- The discriminator appears to be *whether the report was durably retained* — `asserted-by-worker` is
  defined by *"no retained artifact"*. The item does not say. So the same sentence lands in **Observed**
  or in **Inferred** — different *parent labels*, not merely different tiers — depending on a fact the
  item does not state and the registry never tells you to ask for.
- My answer, forced: **Inferred / `asserted-by-worker`**, because "an agent read the code and reports"
  describes an assertion, not a retained artifact. Confidence: low.
- **State plane** is separately clear: Inferred (T-10, *challenge authority only*).

### C.3 — "Capability X is declared in the spec; nothing says whether anything implements it."

- **Evidence tier = `declared-only`.** [Observed] T-16 (`:887-889`): *"`declared-only` (the
  declaration is Observed; its satisfaction is Unknown — both halves render)"*, and T-16's own Example
  (`:909-911`) is this exact case.
- **Claim epistemic label = `Unknown`** (parent of `declared-only`).
- **State plane:** the declaration is **Desired** (T-07 lists "capabilities" as Desired-plane
  membership); the implementation claim has no plane (a Claim is a derived object, T-06: *"Derived
  objects… occupy no plane"*).
- **Did I have to guess?** No — for the tier. **Yes** for whether this is also a **Gap**; see D.1.

### C.4 — "The PR implementing X was merged three weeks ago; no one has checked it against the requirement."

- **Work lifecycle = `merged`; chain state = `reconciliation-pending`.** [Observed] T-11's Example
  (`:643-644`) is verbatim this: *"A merged work item is Execution-plane `merged`. Its chain state is
  `reconciliation-pending` until a reconciliation evaluation says otherwise."*
- **State plane = Execution** (T-11).
- **Claim epistemic label = `Unknown`**, and T-26 names the terminal `Unknown(reason)`.
- **Evidence tier: I had to guess, and I believe there is no correct answer.** The six tiers are
  closed and only two sit under `Unknown`: `declared-only` and `suspended`. `suspended` requires an
  admitted challenge (T-18) — there is none. `declared-only` describes a declaration with unknown
  satisfaction, which under-describes a merged PR. Yet T-13 (`:701-703`) makes rendering tier a field
  every claim instance carries. **[Inferred] A plain missing-evidence `Unknown` — the single commonest
  state on a fleet-built project, and the one the corpus calls "correct output" (`:1308-1310`) — has
  no lawful tier in a closed six-value set.** I could not resolve this from the registry.
- **Two further §1 defects surfaced by this item:**
  - `merged` and `reconciled` appear in **both** the thirteen work-lifecycle values **and** the chain
    state carried *"beside"* it (`:157`). I could not tell whether `merged` in one is the same fact as
    `merged` in the other.
  - The thirteen values are declared **closed**, but four of them are named only as *"four absence
    values"* (`:157`) and never enumerated. A closed vocabulary whose members are not listed cannot be
    used to classify anything.

### C.5 — "The requirements document says X must be under 200ms; the accepted architecture contract says the component is allowed 400ms."

- **This belongs to none of the five dimensions. That is a finding.** A Contradiction is not a value
  of *state plane*, *epistemic label*, *evidence tier*, *work lifecycle*, or *governance lifecycle*.
  §1 presents five closed vocabularies for the questions *"routinely confused"* — but Gap /
  Contradiction / Unknown form a sixth axis (finding type) that §1 does not name and the anti-generic
  rule does not protect. Derivatively I can answer on one dimension: **Claim epistemic label =
  `Unknown`**, because T-19 (`:1004`) says a contradiction *"renders the affected conclusion Unknown."*
- **And the classification itself is not determinate from the registry.** T-19 (`:1002-1003`): *"A set
  of authoritative claims in the same declared scope that **cannot simultaneously be satisfied**."*
  Applied literally: any realization under 200ms is also under 400ms, so the two **can** be
  simultaneously satisfied and **this is not a Contradiction**. The intuitive reading — that a 400ms
  allocation to a component on X's path makes the 200ms requirement unmeetable — is only true if the
  component is on X's path and the budget is end-to-end. That is a *scope* question, and T-19 makes
  scope load-bearing (*"in the same declared scope"*) while RFC1-18(a) (candidate, unreadable to me)
  is cited for what a scope even is (`:1252-1253`, *"declared scope is a typed reference, never a
  string"*). **I had to guess.** My answer: *not determinable without the declared scope; under the
  literal reading, not a Contradiction.*
- [Inferred] I expect most readers to answer "Contradiction" confidently and be wrong-by-the-letter.
  The plain-language gloss the registry offers — *"authorities disagree"* (`:78`) — actively produces
  that error; see G.

**Score: 2 of 5 answered without guessing (C.1, C.3). C.2 forced a guess between two parent labels.
C.4 forced a guess on tier and exposed an uncoverable case. C.5 forced a guess on scope and has no
dimension.**

---

## D. Adjacent-term distinction tests

### D.1 `Unknown` (T-31) vs `Gap` (T-20) — **COULD NOT SEPARATE**

| Item | My placement | Confidence |
|---|---|---|
| C.1 CI gate passed | Neither | High |
| C.2 agent report | Unknown | Medium |
| **C.3 declared, nothing implements it** | **The two entries give opposite answers** | — |
| C.4 merged, unchecked | Unknown(reason) | High |
| C.5 200ms/400ms | Neither — Contradiction, explicitly *"more information than Unknown, not less"* (`:848-849`) | High |

**Finding D-1 — T-20 and T-31 classify the same example in opposite ways.** [Observed]

- T-20 **Example** (`:1059-1060`): *"An adopted requirement with **no verifying evidence** at
  evaluation E **is a gap at E**."*
- T-31 **Related but distinct** (`:846-848`): *"*Gap* (T-20 — a gap is something intended and
  **known** to be absent; an Unknown is **not knowing whether it is absent**. **Rendering an Unknown
  as a gap manufactures knowledge**)."*

C.3 is "adopted/declared, no verifying evidence" — T-20's example says *gap*; T-31 says calling it a
gap *manufactures knowledge*. These cannot both be right. [Inferred] T-31's reading is the one VIS-2
requires: absence of evidence is not evidence of absence, and T-20's own formal definition
(*"Compatible desired state **not yet realized** in observed state"*, `:1037`) asserts non-realization
as a fact, which is a positive claim requiring evidence VIS-2 says you do not have.

This is the sharpest finding in the review: **the two core terms whose distinction the registry itself
calls load-bearing give contradictory answers on the commonest case in the system.** T-20's own
"Related but distinct" block escalates the stakes — it declares the *Gap/Contradiction* distinction
load-bearing (`:1019-1022`, *"No surface, count, endpoint, or UI string may merge the two"*) — while
the *Gap/Unknown* boundary, which is the one that actually fails, gets a bare cross-reference.

### D.2 `Claim epistemic label` (T-15) vs `Rendering / evidence tier` (T-16) — **SEPARABLE**

| Item | Label | Tier |
|---|---|---|
| C.1 | Observed | `gate-backed` |
| C.2 | Inferred (or Observed — see C.2) | `asserted-by-worker` (or `report-fact`) |
| C.3 | Unknown | `declared-only` |
| C.4 | Unknown | **no lawful tier** (C.4) |
| C.5 | Unknown | none — not a claim yet |

The *concepts* separate cleanly: T-16 (`:880-881`) — *"A tier qualifies how a claim renders and may
only **restrict** its parent label's authority, never extend it. **A tier never becomes a fourth
epistemic label.**"* That is one of the best-drafted sentences in the corpus. The **placements**
still failed twice, but for C.2's and C.4's reasons, not because the pair is indistinct. **Pass.**

### D.3 `Observed state` (T-09, plane) vs an `Observed` claim label — **SEPARABLE**

| Item | Plane | Label |
|---|---|---|
| C.1 | The CI artifact is an Observed-plane entity | The claim about it is Observed |
| C.2 | The code is Observed-plane; the report is Inferred-plane | Inferred |
| C.3 | The declaration is Desired-plane | Unknown |
| C.4 | The work item is Execution-plane | Unknown |
| C.5 | Two Desired-plane records | Unknown |

This is the registry's **best work**. §1's boxed **First-use rule** (`:177-184`), T-09's Misuse
(`:581-582`, *"Write 'the Observed plane' or 'an Observed claim.'"*), and T-15's cross-reference
between them are jointly sufficient. The entry is also honest that the rule is unchecked
(`:186-190`, ending *"**[Unknown]** — how many bare uses exist"*). **Pass.**

### D.4 `Reconciliation` (T-26) vs `Converged` (T-25) vs `Aligned` (T-24) — **SEPARABLE**

| Item | Placement |
|---|---|
| C.1 | **Aligned** — one subject, one cited claim, one evaluation, `gate-backed` (T-24, `:1206-1211`) |
| C.2 | None — `asserted-by-worker` is *"never a status input"* |
| C.3 | None — `declared-only` |
| C.4 | **Reconciliation** — `reconciliation-pending` on the chain |
| C.5 | None — and it blocks Converged for any scope it touches (T-25, `:1244`, *"no unresolved contradiction touches the scope"*) |

T-24's *"**Aligned is not the singular of Converged**, and Converged is not the plural of Aligned"*
(`:1223-1225`) is unusually effective. **Pass** — but note none of the three appears usably on the
default path: `Aligned`/`Converged` appear only inside README's denial sentence (A.3), and
`Reconciliation` appears in the wrong sense (A.5).

### D.5 `Warrant` (T-17) vs `Evidence` (T-14) — **SEPARABLE**

| Item | Placement |
|---|---|
| C.1 | **Evidence** — a gate artifact. Not a warrant |
| C.2 | **Neither**, on the reading I chose (an LLM assertion is Inferred; evidence must be durable and identified). Under the `report-fact` reading it becomes evidence *about the report* — the C.2 ambiguity propagates here |
| C.3 | **Neither** |
| C.4 | **Both, separately** — the requirement that authorized the PR is a work warrant (T-17's *"an approved requirement"*); the merge commit SHA is evidence (T-14 names *"a commit SHA"*) |
| C.5 | **Warrant** side — *"an approved requirement"* is one of the four closed warrant classes; neither statement is evidence |

*"**Status describes; warrant authorizes**"* (`:923`) is the single sharpest line in the registry and
it did all the work. **Pass.**

**Pairs I could not separate: one — D.1 (`Unknown` vs `Gap`).**

---

## E. The admission rule

### E.1 Where it is, and whether there is exactly one

[Observed] **Yes, one, in one place: §3, `TERM-REGISTRY.md:236-255`.** The file is explicit and
correct about this: §"Admitting a new public term" (`:115-124`) now states the rule's *history* and
deliberately states no rule — *"The five-condition form was the stronger and it survives; §3 now
states it, and this section states nothing."* [Observed] I found no third statement by sweep. This is
the registry's cleanest self-repair and it should be preserved verbatim.

The five conditions (`:239-251`), abbreviated: **(1)** no existing term adequate; **(2)** the
distinction is operationally meaningful — *"something is rendered, counted, gated, routed, or refused
differently"*; **(3)** identified owning authority **and a lifecycle** — *"the entry says what would
retire the term"*; **(4)** one-sentence plain-language explanation *"**without needing a second Syzygy
term**"*; **(5)** a fresh-reader distinction test on five real examples.

### E.2 Would `Project Genome` (T-03) pass if proposed today?

| Cond. | Verdict | Working |
|---|---|---|
| 1 | **Pass** | Nearest is *Desired state* (T-07) or "the specs"; the entry names why each is narrower (`:369-371`), and RFC1-8 makes Genome a *membership predicate over a declared inventory* rather than a plane |
| 2 | **Pass, on intent** | Membership decides what must survive deletion; the three-tier inventory (`:355-361`) is a routing rule. [Unknown] whether anything is rendered or gated differently today — nothing is implemented |
| 3 | **FAIL** | The entry names authorities (`architecture.md` "Project Genome", adopted; RFC1-8) but **states no lifecycle**. Condition 3 requires *"the entry says what would retire the term"*; T-03 says nothing about retirement |
| 4 | **Pass, strongly** | *"Everything a project would need to survive deletion of its code — and it is much more than the behavioural specs"* (`:347-348`) — zero Syzygy terms used |
| 5 | **FAIL** | Not run. §6 (`:1545-1546`): *"**No newcomer comprehension test has been run** on any of the 30 entries."* |

**Verdict: T-03 would be rejected today, on conditions 3 and 5.**

### E.3 Would `Attention item` (T-29) pass if proposed today?

| Cond. | Verdict | Working |
|---|---|---|
| 1 | **FAIL — and instructively.** | Condition 1 requires *"Name the nearest existing term and say what it cannot express."* T-29's nearest neighbour is **escalation** — the concept T-27 (`:1338`, *"it raises an escalation"*), T-28 (`:1382`, *"escalation triggers"*) and `OVERVIEW.md:94` all lean on. [Observed] `escalation` has **no registry entry** and **0 occurrences in the adopted doctrine tree**. The nearest existing term cannot be named because it is not in the registry, so condition 1 is unsatisfiable as written |
| 2 | **Pass, strongly** | Mandatory content contract; *"an expiry default must be safe"*; *"a bulk act over unenumerated items resolves nothing"* (`:1428-1435`) — all three are refusals the distinction causes |
| 3 | **FAIL** | Authority is identified (RFC10-12, RFC10-13) but **candidate only**, and again **no lifecycle stated** |
| 4 | **Pass** | *"A decision-ready packet for a human — not a notification, not an event"* (`:1420-1421`) — no Syzygy term needed |
| 5 | **FAIL** | Not run (§6) |

**Verdict: T-29 would be rejected today, on conditions 1, 3 and 5.**

### E.4 Finding E-1 — condition 3's lifecycle requirement is met by exactly one entry in thirty-one

[Observed] Script sweep for the `**Lifecycle.**` field across the registry returns **one hit**: line
832, inside `T-31 · Unknown` (*"Retired only if VIS-2 is amended, which would be a doctrine
change."*). The entry template documented at *"How to read an entry"* (`:126-142`) does not include a
Lifecycle field at all. So **30 of 31 entries fail admission condition 3** on a structural omission,
not a judgement call.

§6 (`:1543-1544`) already concedes *"The admission rule (§3) was applied to no incumbent term. Every
entry is vocabulary admitted by prior use."* That concession is honest but understates the position:
the rule cannot be applied to any incumbent without first adding a field the template does not have.

---

## F. The tier naming conflict

### F.1 Is the situation stated honestly?

[Observed] **Yes — the banner at `:867-877` is the most honest passage in the document.** It counts
both sides (*"five uses"* vs *"two uses"*), names its own prior error (*"This registry previously
carried only the minority name, which made a restatement look like a rename of the term its own
owning clause defines"*), declines to decide (*"The registry does not get to choose"*), and routes the
question to the owner.

**But the stated resolution is not carried out inside the same file.** The banner says *"the majority
name leads here, the minority name is recorded as a synonym."* [Observed] Actual usage in the
registry:

| Line | Text | Name used |
|---|---|---|
| `:65` | advanced-tier list — "rendering tier" | majority |
| `:111` | "`rendering tier` is more load-bearing…" | majority |
| **`:156`** | **§1 dimension table row: `\| **Evidence tier** \|`** | **minority** |
| **`:164`** | **§1's boxed rule: "Name the dimension: … *evidence tier* …"** | **minority** |
| `:482` | T-06 Related but distinct: "Evidence tier (T-16)" | minority |
| `:701` | T-13: "epistemic label, rendering tier, Unknown reason" | majority |
| `:760` | T-14 Related but distinct: "Evidence tier (T-16)" | minority |
| `:798` | T-15 Related but distinct: "Evidence tier (T-16…)" | minority |
| `:862` | entry heading: "Rendering tier (also called 'evidence tier')" | both |
| `:1362` | T-27 example: "the minimum evidence tier it accepts" | minority |

**Four of the five in-entry cross-references use the minority name, and so do both of §1's
statements — including the dimension table, which is the most-cited surface in the file.**

**Finding F-1 — T-16 lists its own title as a permitted alias.** [Observed] `:900`: *"**Permitted
aliases.** *rendering tier* (the corpus's own term — see the migration report; both spellings are in
use)."* The entry is titled *Rendering tier*. An entry cannot be an alias of itself. This is the
mechanical residue of the rename: the heading was changed to the majority name and the alias field,
which previously listed the majority name as an alias of an *evidence tier* head, was not.

### F.2 Which name would I pick?

**`evidence tier`** — while noting the registry's own procedural rule (owning clause + majority use)
points the other way, which is exactly why it is properly an owner question.

Reasoning, as a reader:

1. §1's own question for the dimension is *"How strongly does the **evidence** support the claim?"*
   (`:156`). The name that answers the question the table asks is *evidence tier*.
2. `rendering tier` collides with a real neighbouring concept **in the same entry**: T-16 (`:893-895`)
   introduces *"three closed **sibling surface states**… which **replace** a status **rendering**"*.
   So within eight lines, "rendering" names both the tier system and the thing the sibling states do
   to a rendering. A reader who takes "rendering tier" at face value expects it to be about
   presentation — and it is not; `gate-backed` is an evidence-strength fact that constrains what may
   render, not a rendering.
3. The whole corpus's thesis is that presentation must never carry meaning content does not have
   (VIS-1). Naming an *evidence-strength* dimension after *rendering* runs against that grain.

### F.3 Is a reader at risk of thinking these are two different things?

**Yes — and the banner under-reports the risk.** It says (`:875-877`): *"Both names denote exactly the
same six closed values; no reader is at risk of meaning-drift, only of thinking one of the two is
wrong."* [Observed] I was at risk of a third thing the banner does not list: a reader following a
cross-reference from T-14 or T-15 — *"Evidence tier (T-16)"* — scans the entry list for an entry
named *Evidence tier*, finds *T-16 · Rendering tier*, and must infer that the pointer and the target
are the same entry. The ID rescues this. **Prose that names the dimension without its ID does not
have that rescue** — `:164`'s rule tells writers to *"Name the dimension: … *evidence tier* …"*, so
compliant prose will use a name the head entry does not carry.

---

## G. Ordinary language

The registry proposes six plain phrasings (`:73-79`):

| Plain phrasing | Accurate? | What it loses |
|---|---|---|
| `what should be true` → desired state | **Mostly** | Loses **adoption**. "Should be true" also describes a *proposal* — and T-08 exists precisely because *"Proposed state… Never desired"* (`:529`). A newcomer reading "what should be true" has no way to know that an unadopted draft is excluded |
| `what evidence says is true` → observed state | **Yes — and better than the narrative's own phrasing** | Nothing. See G-1 |
| `what agents did` → execution state | **Partly** | Loses *humans*. The core table five rows above says *"what did **agents and humans** actually do?"* (`:40`). Two plain phrasings of one term in one file, disagreeing — the same defect class as A-1 |
| `something missing` → gap | **No** | Loses *known to be absent*, which is the entire T-20/T-31 boundary. "Something missing" is exactly the phrase a reader would also apply to an Unknown. **This phrasing causes the D-1 failure**, it does not merely fail to prevent it |
| `authorities disagree` → contradiction | **No** | Loses *cannot both be satisfied* and *only the owner adjudicates*. **Demonstrated in C.5**: reading "authorities disagree" I would have called 200ms-vs-400ms a Contradiction; T-19's actual definition says the literal answer is no |
| `check work against intent` → reconciliation | **Yes, and it is the best of the six** | Loses *post-merge* and *the exact intent revision that warranted it*. But it is strictly better than the default path's own "reconciliation work" (A.5) |

### Finding G-1 — the registry's plain phrasing for `observed state` is more truthful than the default path's

[Observed] `OVERVIEW.md:42`: `| **Observed state** | what is true | code, tests, CI, runtime — captured
as **evidence** |`. `README.md:28` likewise: *"**observed state** (code, tests, CI, runtime
evidence)"*. The registry says *"what **evidence says** is true"* (`:75`). Under VIS-2 the difference
is not stylistic: *"what is true"* is precisely the unqualified assertion the whole doctrine forbids,
and the evidence qualifier is what makes the row honest. A three-word repair on the default path.

### Would I have understood faster if the narrative led with the plain phrasing?

**Split.**

- **Yes, for the three state planes.** `OVERVIEW.md:39-43` already does this — the table's second
  column *is* the plain phrasing — and it is the fastest-comprehending part of the whole corpus. I
  understood the thesis in about ten seconds. The registry's *"Ordinary language first… use it and
  let the term follow in parentheses — not the other way round"* (`:70-72`) is correct and already
  working.
- **No, for `gap` and `contradiction`.** Those two plain phrasings are so loose that leading with them
  installs a *wrong* model that the formal definitions must then displace — and, in my case, did not.
  For these two the safer default-path move is the one `OVERVIEW.md:159-160` already makes inside
  Drawer 1: *"A **gap** (something missing) and a **contradiction** (two authorities disagreeing) are
  different findings with different remedies"* — the plain phrase plus the *consequence*. The
  consequence is what makes the distinction stick; the paraphrase alone does not.
- **Structural note.** That sentence is inside Drawer 1, while `Gap` and `Contradiction` are **core**
  terms, i.e. required for the default path. Two of the eleven core terms have their only
  distinguishing sentence behind a `<details>` element the reader is told is *"optional drill-down"*
  (`OVERVIEW.md:139-141`).

---

## H. The things I could not find out

Terms I met on some path whose meaning I **could not establish from the four prescribed sources**.
Ordered by where I met them. Ordinary engineering words (*digest*, *daemon*, *snapshot* in its
common sense) are excluded; so are terms defined adequately in place.

### H.1 Met on the default path — 15

| # | Term | Sites | Note |
|---|---|---|---|
| 1 | **kernel** | `README.md:49`; `OVERVIEW.md:63, 65` | Defined at `OVERVIEW.md:65` as *"a temporal project graph plus an evaluation engine"* — a definiens made of two undefined terms. No registry entry |
| 2 | **surface** | 14 default-path sites | No registry entry; 35 occurrences in adopted doctrine; README and OVERVIEW disagree on whether Mission Control is one (A-6) |
| 3 | **workspace** | `README.md:47, 50`; `OVERVIEW.md:86` | No entry; **0 occurrences in the adopted doctrine tree** (registry's claim at `:98` verified). T-01 deprecates it as a synonym for Project and asserts *"a workspace is a set of projects"* (`:296-298`) citing candidate RFC10-15 |
| 4 | **actuator** | `OVERVIEW.md:47, 55` | No entry; 5 occurrences in doctrine, all undefined |
| 5 | **plane** (the "co-equal plane" sense) | `OVERVIEW.md:73` | Five-to-six live senses (A.4); this one matches none of the defined ones |
| 6 | **control plane** | `README.md:3`; `vision.md:16` | The project's opening predicate. No entry, no definition |
| 7 | **experience** | `README.md:40` | 0 in doctrine, 0 in registry (A-5) |
| 8 | **evidence bar** | `README.md:81`; `OVERVIEW.md:94` | 0 in the adopted doctrine tree; used as a Mission-envelope field and as the name of the craft policy's remit |
| 9 | **gate** (owner-acceptance sense) | `README.md:12, 101`; `OVERVIEW.md:4, 120, 124, 131` | Collides with `gate-backed` (T-16), which is a CI gate. Two unrelated senses, no disambiguation |
| 10 | **owner act** | `OVERVIEW.md:6, 90, 123` | The mechanism the entire acceptance model rests on. No entry, no definition on the default path |
| 11 | **escalation** | `OVERVIEW.md:94`; T-27, T-28, T-29 | **0 occurrences in the adopted doctrine tree.** It is also T-29's nearest neighbour, which breaks admission condition 1 (E.3) |
| 12 | **conforming integration** | `OVERVIEW.md:74` | 0 in doctrine. Used to make a normative-sounding claim (*"Scraping a human-rendered table is never a conforming integration"*) |
| 13 | **temporal project graph** / **evaluation engine** | `OVERVIEW.md:65` | Neither defined anywhere I read |
| 14 | **V0 / V1** | `OVERVIEW.md:134`; `vision.md` ×10 | I learned they are stages, never what either contains. `vision.md:45-50` makes load-bearing claims keyed to them (*"A **witness** (V0)"*, *"harness (proof-of-concept at V0, full at V1)"*) that I could not evaluate |
| 15 | **shape** / **project-shape** / **shape-level** | `README.md:7, 14`; `OVERVIEW.md:116`; VIS-4 | VIS-4 makes *"Classification of a change as spec-level or shape-level"* a contested, human-only judgement, and defines neither side |

### H.2 Met inside the registry or doctrine bodies — 19

| # | Term | Site | Note |
|---|---|---|---|
| 16 | **district** | `TERM-REGISTRY.md:517` (*"the kernel district"*), `:548` | **0 occurrences in the adopted doctrine tree.** Used in two core-adjacent worked examples as if it were established |
| 17 | **verification oracle** / oracle coverage | T-25 (`:1243-1249, 1264-1265`) | Load-bearing: *"an oracle whose adequacy is unassessed yields Unknown"*. No entry; 5 occurrences in `architecture.md` only |
| 18 | **certificate** / **convergence certificate** | `trust-and-evidence.md:43, 104`; T-12 (`:678`) | Future-tagged but used in normative sentences. No entry |
| 19 | **execution profile** | `TERM-REGISTRY.md:67` (listed as **advanced vocabulary**); T-28 (`:1406`) | Listed in the advanced tier with **no entry**. A reader who looks it up finds nothing |
| 20 | **semantic relation class** | T-06 (`:470-471, 483`) | Named as the thing that carries an edge's whole relationship to the planes. No entry |
| 21 | **governed memory** | T-30 (`:1495`) | Named, no entry |
| 22 | **guardrail runtime** / **enforcement plane** | T-28 (`:1403-1404`) | Both named, neither defined; *enforcement plane* is a sixth sense of *plane* |
| 23 | **exclusivity group** | T-08 (`:528, 531, 549`) | Central to the Proposed plane; only ever named, never defined |
| 24 | **the four absence values** (work lifecycle) | `:157` | A **closed** thirteen-value vocabulary with four members unenumerated |
| 25 | **the twelve Unknown reasons** | T-31 (`:822`), T-15 (`:790`) | A **closed** twelve-value vocabulary; four or five leak out via examples, the list is in candidate RFC2-24 |
| 26 | **genome-complete** | VIS-2, `trust-and-evidence.md:42`, T-25 (`:1260`) | §5 confirms it (`:1532`): *"the frozen *genome-complete* has no registry entry of its own"* — although VIS-2 makes it one of three things no surface may declare |
| 27 | **materialization record** | T-26 (`:1285`), T-11 (`:624`) | *"the exact intent revision pinned in the immutable materialization record"* is the pivot of the reconciliation chain. No entry |
| 28 | **declared-identity base layout** | T-23 (`:1165`) | Named as mandatory observation-record content |
| 29 | **coverage record** | T-23 (`:1167`) | Same |
| 30 | **maximum autonomy level** | T-28 (`:1378`) | An envelope bound with no scale, no values, no definition |
| 31 | **permitted change classes** | T-28 (`:1376`) | Same |
| 32 | **handcrafted-region declaration** / marked-handcrafted carve-out | T-03 (`:357`); `vision.md:208-209` | Universally-required Genome content, undefined |
| 33 | **proving ground** | `vision.md:242` | Appears in the thesis's falsification test |
| 34 | **end-to-end propagation slice** | `vision.md:60` | Appears in a V0 escape property |

**Total: 34.** Fifteen on the default path.

**Partially inferable, excluded from the count but worth naming:** *projection* (`README.md:49`) —
gist available, mechanics not; *adapter* (`README.md:61, 71`) — gist available, but *typed* and
*explicitly authorized* are load-bearing and undefined; *accepted* vs *adopted* vs *approved*
(`README.md:79-85`) — three governance-lifecycle values used side by side in one table with no
statement of how they differ.

**A meta-observation on H.** [Inferred] The pattern is not random. Terms 1-15 are the *architectural*
vocabulary — what Syzygy **is** — and terms 16-34 are largely *mechanism* vocabulary. The registry
covers the **epistemic** vocabulary (claims, evidence, labels, tiers, planes, evaluation) thoroughly
and well; that half of the corpus is in good shape. What is uncovered is the vocabulary of the
system's own **structure and surfaces** — kernel, surface, plane, district, workspace, actuator,
control plane, experience — which is precisely the vocabulary the default path uses most.

---

## Verdict rationale

**REVISE**, not EXCEPTIONS and not REJECT.

Not **CONFIRM** or **EXCEPTIONS**: the failures are not bounded carve-outs. Two of the eleven core
terms — `Gap` and `Unknown` — give contradictory answers on the commonest case in the system (D-1),
and a third core term, `Reconciliation`, is used on the default path in the sense its own entry
reserves against (A.5). Those are defects in the core set itself, which is the artifact's central
claim. I answered 2 of 5 classification exercises without guessing.

Not **REJECT**: the structure is sound and roughly two-thirds of it works. §1's five-dimension split
is genuinely clarifying; the plane/label first-use rule (D.3) and the warrant/evidence split (D.5)
both survived contact with a fresh reader; §3's admission rule is well drafted and singular; and §6,
the T-16 naming banner, and the CG-23 report-only framing are exemplary intellectual honesty of a
kind I do not usually see. Every one of my findings is repairable without redesigning the registry.

**The three repairs that would move this to CONFIRM,** in priority order:

1. **Resolve T-20 vs T-31.** Decide whether "adopted requirement, no verifying evidence" is a Gap or
   an Unknown, and make T-20's Example, T-20's formal definition, and T-31's cross-reference all say
   the same thing. Nothing else in the registry matters as much.
2. **Fix `Reconciliation` on the default path.** `OVERVIEW.md:46, 54` uses the reserved word for the
   desired/observed delta. Either that is a second sense the corpus accepts and T-26's hard
   reservation is wrong, or the default path needs a different noun — and B-1 notes it has no term
   for that concept at all.
3. **Give `surface`, `kernel`, `plane`, `workspace`, `actuator`, `experience`, `owner act`, `gate`
   and `evidence bar` either an entry with an owning authority, or a plain-language replacement.**
   Fifteen undefined terms on a default path bounded to eleven is not a bound.

**Two smaller repairs that cost nothing:** the eleven/twelve and 30/31 count drift (A-1, A-2) and
T-31's absence from §5 (A-3); and T-16's self-alias at `:900` (F-1).

**One note on scope, offered rather than found.** Several repairs above touch `OVERVIEW.md`, which
`OVERVIEW.md:6` says is *"Adopted by its own owner act… which binds this file's exact bytes"*, and
the registry records at `:90-93` that leaks inside an unperformed act's digest subject were
deliberately not edited. [Inferred] Findings A.5, A-6 and G-1 are therefore repairs to a *pending*
offering, not corrections to a bound artifact — which, if the act has not fired, is the cheapest
moment they will ever be available.

---

## Appendix — verification performed

[Observed] All read-only. Run at working tree state of 2026-08-07, branch `main`.

- Entry count, core-table row count, `**Lifecycle.**` field sweep, number-word sweep: Python `re`
  over `TERM-REGISTRY.md`. Results: 31 entries; 11 core rows; 1 Lifecycle field.
- Default-path term occurrence sweep: Python `re`, case-insensitive, over `README.md` +
  `OVERVIEW.md[:index("<details>")]`. Drawer boundary confirmed at line 143.
- Adopted-doctrine occurrence counts: Python `re` over all six `.md` files in
  `.syzygy/governance/doctrine/`. Confirms `workspace`=0, `experience`=0, `escalation`=0,
  `district`=0, `evidence bar`=0, `conforming`=0.
- `python3 scripts/check_governance.py` — CG-23 output quoted verbatim in A.3.
  Full run: `24 OK, 13 WARN, 1 FAIL (38 checks)`. I did not investigate the FAIL; out of commission.
- CG-23 mechanism read directly at `scripts/check_governance.py:2763-2856`.
- `architecture.md` inspected **headings-only** (regex listing, no narrative read) to establish that
  `### Definitions` (line 157) and `## Vocabulary` (line 285) exist. This supports finding A-7 and
  nothing else; no definition from that file informs any answer above.
- No `grep` was used for any load-bearing claim (ugrep bracket-class hazard); all sweeps are
  Python `re`.

**Incidental observation, not a commissioned finding.** [Observed] CG-23's ordinary-English exemption
text at `scripts/check_governance.py:2798` is printed every run as a quotation —
`"No claim of alignment, convergence, or reconciliation"` — but `README.md:118-119` reads *"No claim
of alignment, convergence, or **regeneration capability**"*. The printed quote does not match the
quoted line.
