# Final pre-specification readiness — twelve criteria

> **Non-authoritative round record.** It decides nothing and accepts nothing.
> Every criterion cites the artifact that owns its evidence; where this file
> and that artifact disagree, the artifact wins and this file is stale.
>
> **As-of: 2026-08-07.** Supersedes
> `round-2026-08b/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`.

## The answer

> **Is Syzygy ready for OpenSpec authoring?**

**No — and it is closer, in a specific and stateable way.**

**Nine of twelve criteria are met. Three are not**, and each unmet one is named
with the exact finding that blocks it, by a reviewer who did not write the
thing they blocked.

**The three unmet criteria do not block the five acceptance acts.** They are
candidate-corpus defects an act would bind **knowingly**, and the acceptance
packet states them before the act phrases — which is the difference between a
knowing acceptance and a surprised one.

## Method, and what this report will not do

**Eight independent reviews ran this round. Every verdict was `REVISE`.** Raw
output is at `reviews/`, never edited, verdict words copied. No verdict is
restated as "pass with findings"; no blocking finding is reclassified; no
acceptance waiver is offered over any of them.

**A criterion is met only if an artifact outside this file carries the
evidence.** "Met" here never means "we believe it"; it means a named document
holds a measurement, and where that measurement is a sweep, its denominator.

## The twelve

| # | Criterion | Status |
|---|---|---|
| 1 | North star discoverable | **Met** |
| 2 | Default narrative understandable without advanced terminology | **Met, with the bound stated** |
| 3 | Project-shape facets defined independently and source-backed | **Met** |
| 4 | Fixed human entry point defined for every governed project | **Met** |
| 5 | Typed authority and contract relations closed | **Met — or owner-ruled** |
| 6 | Public vocabulary bounded and internally consistent | **Bounded, not internally consistent** |
| 7 | RFC/OpenSpec routing complete | **Met** |
| 8 | Context-selection contract and metadata complete | **NOT MET** |
| 9 | Golden selections complete, current, independently reviewed, and budgeted | **NOT MET** |
| 10 | Mission safety contract semantically closed | **NOT MET** |
| 11 | Acceptance ceremony executable from a clean clone | *(pending RD-7)* |
| 12 | Exact final package passes a fresh semantic review | *(pending RD-8)* |

---

### 1 · North star discoverable — **Met**

A fresh reader with no project context answered **six of six** entry questions
about this repository and **gave up on nothing** (review RD-2). *What is this
project* took **one hop** from `README.md`.

**The honest edge:** *"which artifact owns the answer"* was one hop at the
shape level and **five** to reach a governing clause. Five hops is the
measurement, and it is recorded rather than rounded down.

Evidence: `HUMAN-CLARITY-CLOSURE-REPORT.md`; `reviews/RD-2-human-clarity-RAW.md`.

### 2 · Default narrative understandable without advanced terminology — **Met, with the bound stated**

The core public set is **eleven** terms, each leading with the plain question
it answers, with the ordinary-language mapping as the preferred default-path
phrasing. A reader who had not been told the first-use rule existed (*"the
Observed plane"* / *"an Observed claim"*, never bare *Observed*) **applied it
correctly** — the rule was tested rather than assumed.

**The bound is declared and not yet held:** the default path carries **fifteen**
Syzygy-specific terms with no registry entry. Two have no owner anywhere —
`workspace` has **zero occurrences in the entire adopted doctrine tree**
(verified this session over six files), and `experience` heads a section of
`README.md` and is defined nowhere.

Criterion 2 is met because a reader can read the default path without the
advanced tier. It is **not** a claim that every word on it is defined.

Evidence: `PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md`.

### 3 · Project-shape facets defined independently and source-backed — **Met**

Seven facets, ten rules, no composite, Unknown first-class with a reason. A
reviewer who tried to break the model — constructing two facets that must
disagree, a facet unanswerable without another, and an unfalsifiable facet —
produced repairable defects in the *evidence* and **none in the seven-facet
decision**. Their words: *"The model is right … I would not weaken any of it."*

**Source-backed** is the half that failed and was repaired: three Unknown
reasons minted outside RFC2-24's closed twelve, a fabricated contract gap, and
a fabricated quotation. All three closed at the source, and the vocabulary
sweep across three files reports **zero** non-vocabulary reasons remaining.

**The repaired documents have been read by no independent reviewer** — the
repairs came after RD-2 returned, and a repair pass may not be its own
confirming reviewer. Recorded, not papered over.

Evidence: `PROJECT-SHAPE-FACETS-BRIEF.md`, `PROJECT-SHAPE-FACETS-ROUTING.md`,
`HUMAN-CLARITY-CLOSURE-REPORT.md`.

### 4 · Fixed human entry point defined for every governed project — **Met**

One path, chosen, with the alternative rejected in writing:
**`.syzygy/intent/OVERVIEW.md`**. Eight content obligations, presentation never
authority, and the root-README discoverability finding rendered **per declared
repository entry** and **never written**.

**The cost is now listed rather than discovered:** RFC3-29 allows one
`.syzygy/` plane per repository and RFC3-30 makes every other repository
read-only, so **N−1 of a project's N repositories can never have an entry
point.** The per-repository finding renders the hole; nothing in this design
closes it, and the brief says so.

**Two one-line contract gaps remain and neither is filled** — no clause names
the fixed path (smallest home RFC7-6), and none defines the discoverability
finding (smallest home RFC3-6).

Evidence: `HUMAN-ENTRY-POINT-BRIEF.md`.

### 5 · Typed authority and contract relations closed — **Met, or owner-ruled**

Three relations with one authored direction each and every inverse derived.
Both originally-declared `constrains` edges were **wrong**, both real ones were
**undeclared**, and a reviewer found all four by reading clauses. Corrected,
anchored to a defining clause, projected into the machine index, and checked —
the anchor predicate is **mutation-tested in an isolated clone**.

**Owner-ruled, not agent-closed:** **RFC11-4 does not name `constrains`**, so a
conformant compiler reads none of it. **P-21(c).** Eleven `depends_on` edges
carry zero clause evidence — **P-21(b)**. Completeness is **`[Unknown]`**: the
population came from a sweep by the party that authored the wrong edges.

Evidence: `CONTRACT-RELATION-CLOSURE-REPORT.md`, `RELATION-MODEL-DECISION.md`.

### 6 · Public vocabulary bounded and internally consistent — **Bounded, not internally consistent**

**Bounded: yes.** Two tiers exist, the registry draws them, and a check reports
the bound every run **against a core set it parses from the registry rather
than a copy**.

**Internally consistent: no**, and by one specific failure. **`Unknown` (T-31)
and `Gap` (T-20) classify the same example in opposite ways** — T-20's own
example treats *"an adopted requirement with no verifying evidence"* as a Gap;
T-31 says a gap is something *known* absent. It was the one adjacent pair a
fresh reader could not separate.

**That is the missing-declaration-versus-failed-evidence distinction the entire
facet model turns on.** It is **owner packet 5(a)** and is not resolved by an
agent, because it is a question about what the corpus means.

Also open: eight of thirty-one terms have no adopted definition anywhere
(**P-17**).

Evidence: `PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md`,
`TERM-REGISTRY-SEMANTIC-DELTA.md`.

### 7 · RFC/OpenSpec routing complete — **Met**

`SURFACE-CLAUSE-ROUTING-MATRIX.md` routes all **202** clause identities, one
route each — verified by CG-17 this session (`202 clauses examined, 0
findings`). Every gap this round found is routed: to a named clause, to a named
owner packet, or to a named OpenSpec capability, and
`FIRST-OPENSPEC-SEQUENCE.md` states the dependency graph among the four.

**One routing question is left open rather than guessed:** whether the
per-item inclusion reason for non-declarative ordering is a contract gap or an
OpenSpec obligation is `[Unknown]`, and this round could not decide it.

Evidence: `SURFACE-CLAUSE-ROUTING-MATRIX.md`, `FIRST-OPENSPEC-SEQUENCE.md`,
`UNIVERSAL-VISIBILITY-REVIEW.md`.

### 8 · Context-selection contract and metadata complete — **NOT MET**

**RFC11-4 requires the phase-rule clause of every selected contract. Six of
353 clause rows carry that kind. RFC-0001 through RFC-0005 have none, and none
exists in their text. All nine golden fixtures load at least one of them.**

Under RFC11-6 a conformant selector marks the packet incomplete and **does not
launch** — on all nine. In the reviewer's words:

> the nine artifacts offered as proof that deterministic selection works are
> the nine a conformant implementation cannot produce.

Verified this session by two methods: parsing every clause row of the generated
index (353 rows; 345 normative, 6 phase-rule, 2 informative; phase-rule
contracts `{6,7,8,9,10,11}`), and the reviewer's independent `grep -F` over the
contract text.

Two more, each independently sufficient to fail this criterion:

- **`depends_on` has no termination rule.** The natural implementation closes
  transitively and returns 91–100% of the corpus. The fixtures avoid it by an
  **unstated** narrowing, and **the nine apply at least three different
  versions of it**.
- **Doctrine and craft selection is not derivable at all.** `governance_sources`
  carries no `governs` or `applies_to`; *"a selector asked 'which file owns
  VIS-4?' gets five files from a regex mention scan and no way to choose."*

Evidence: `FINAL-CONTEXT-SELECTION-REPORT.md`;
`reviews/RD-5-context-selection-RAW.md`.

### 9 · Golden selections complete, current, independently reviewed, and budgeted — **NOT MET**

**Complete in count** — nine exist, and **all nine reproduce their anchors
under two independent implementations** (`build_budget_report.py --check`;
CG-18, `18 measurements examined, 0 findings`).

**Independently reviewed: yes, and that is what failed them.** A reviewer
derived all nine from the declared metadata and **reproduced four — stated as
an upper bound**, because the fixture format put each answer's reasoning above
its question. *"A golden fixture whose question and answer cannot be separated
cannot be used to test a selector."*

The claim RFC11-4 makes is *same inputs, same selection*. Two competent humans
produced different selections for **five of nine**, and disagreed about **which
rule to apply** — not how to apply it — in every one.

**Not current, in a specific way:** ~70 of 88 fixture measurements are checked
by nothing, and **at least five contradict their own fixture's headline** — the
stale figure being, in every case, the one the budget disposition argues
against.

**Budgeted: honestly, and the threshold is not installed.** `CC-BUDGET-1`
resolves to no governed artifact; four fixtures exceed a *proposed* 20,000
tokens. Fixture 5 states today that a 22,260-token packet is *"inside the
15–20k working target."*

**Class coverage is eight classes over eight fixtures, not nine.** The adapter
class is double-counted; **Trajectory lifecycle is covered by a fixture that
omits work identity, dispatch, materialization, accounting and release.** The
previous round's *eight-for-eight* claim is withdrawn.

**One thing this round did close:** the generated budget report had itself
contradicted its own computed table by eleven words, because it transcribed a
figure from fixture prose under a banner reading *do not copy a figure out of
it*. The generator now redacts every measurement out of what it transcribes and
prints the redactions. Selftest re-run: both mutation fixtures still detect.

Evidence: `FINAL-CONTEXT-SELECTION-REPORT.md`, `CONTEXT-BUDGET-REPORT.md`.

### 10 · Mission safety contract semantically closed — **NOT MET**

Asked whether a bounded, autonomous Mission can cause an unrecoverable or
unauthorized outcome without an owner act, an independent reviewer answered:

> **Yes.** … by at least three independent routes.

**Two RD-1b reviews read the identical bytes at `7f823aa3…` without reading
each other and converged on the same structural defect from opposite
directions.** That convergence is the strongest evidence this round produced
about anything.

The three routes: the budget reservation is **stated over the ledger and not
over consumption**, while RFC10-10 says Mission Control MUST prevent — both
cannot be true as written; **`reversible` is an effect class with no
definition, no named action, no funding and no duty**, and it defeats
RFC10-19's strongest sentence because no attempt is owed so nothing can fail;
and **provider egress breaks the contract whichever way the effects-applied
predicate answers.**

**The three RD-1 blocking findings were closed and the closing created two
more** — the park escape reappeared **one state earlier**, at the parent/child
grant seam.

**Nothing further is repaired, and that is a decision rather than an
omission.** A fourth repair-and-review cycle inside one round is the recursion
the charter says to stop, and the contract sits at **6,749 of 7,000 words**
with its amendment log and 21 violation cases already moved to Tier 2. *There
is no room left to repair in* — which is a structural signal that the package
needs splitting first.

**RFC-0010 is frozen** at `7f823aa3773c7bf47fed2f7634aa696c454b3ca62dea691c656a3f58a191f825`,
including the one-token `depends_on` fix both reviewers found. Two reviews are
bound to those bytes.

Evidence: `MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md`;
`reviews/RD-1-…`, `RD-1b-…`, `RD-1b-…-confirming-RAW.md`.

### 11 · Acceptance ceremony executable from a clean clone

*Pending review RD-7 — a clone taken from HEAD, with the full battery run
inside it and each of the five acts attempted from what git tracks. Recorded
here as `[Unknown]` until that review returns; a criterion answered by the
machine that has the founder's working tree is the one failure mode this
repository keeps re-acquiring.*

### 12 · Exact final package passes a fresh semantic review

*Pending review RD-8 — an independent semantic confirmation over the exact
bytes of all five act subjects, answering whether an owner performing the acts
would be surprised by anything they had bound. Recorded here as `[Unknown]`
until it returns.*

---

## What "not ready" means, precisely

**It does not mean stop.** Three criteria are unmet and each has a named,
bounded repair list written by someone who did not author the defect:

- **Criterion 8** — five phase-rule clauses (or one narrowing of RFC11-4), one
  termination rule, and `governs`/`applies_to` on `governance_sources`.
- **Criterion 9** — split each fixture's question from its answer, extend CG-18
  past the headline, repair two fixtures' figures, re-scope or add one fixture
  for Trajectory lifecycle.
- **Criterion 10** — split the RFC-0010 package, then B1 through B6, then a
  fresh review over the new bytes by someone who wrote none of it.

**None of the three requires re-authoring a contract's semantics**, in the
reviewers' own assessments. All three are edits to act 1's digest subject, and
that is the single reason none was made: **repairing them now would invalidate
the reviews that found them.**

**The order that follows from this report:** perform the acts, or decline them,
with the imperfections stated. Then repair. Then review the repairs, with a
reviewer who did not make them.

## What is ready

Recorded because a readiness report that lists only what is missing
misrepresents the state:

- A fresh reader answers **six of six** entry questions and gives up on
  nothing.
- **202** surface clause identities, one route each, checked.
- **40** governance checks, **26 OK / 14 WARN / 0 FAIL**, every denominator
  computed and every allowlist printed.
- **16 of 24** check families have a mutation fixture, and the figure is
  computed by CG-24 rather than claimed.
- A relation model with a clause anchor and a check that verifies it.
- Every volatile measurement in one generated home that now copies nothing.
- Eight independent reviews on the record, none edited, none softened.

**The project can say what it does not know.** That was the thing at stake, and
on the evidence of this round it is the thing that works.
