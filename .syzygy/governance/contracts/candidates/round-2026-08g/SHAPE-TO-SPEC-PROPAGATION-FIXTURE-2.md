# Shape-to-spec propagation fixture 2 — the blind exercise

> **Non-product governance fixture.** Everything below is deliberately
> fictitious: the "specifications" are mock stubs that exist only inside
> this file, **no `openspec/` tree exists or is implied**, and no mock
> requirement describes real intended behavior. Doctrine rule IDs, contract
> clause IDs and craft clause IDs are real, so that the exercise tests a
> sweeper who knows the corpus's authority tiers; **owner decisions are
> mock** (`OD-1`, `OD-2`) because no owner product decision has been ruled,
> and writing a real pending identifier into a "was amended" scenario would
> state a falsehood inside a governance artifact.
>
> **This file contains no answer.** The golden result lives in
> `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md`, a separate file, so
> that "the reviewer derives the result without reading the answer" is
> structural rather than an honour system. *(The predecessor fixture,
> `../round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`, kept both in one
> file behind a boundary marker, and its ANSWER section contradicted its own
> governing description — RD-51 f8. This fixture supersedes it.)*
>
> **Digest discipline.** CC-IMPACT-7 names this file by path **and sha256**.
> Editing it invalidates every run bound to the old digest; supersede with
> a fixture 3 instead.

## What this fixture is for

CC-IMPACT-7 requires the propagation path to be exercised against a fixture
with a known answer, blind, **before** it is relied on. This is that
fixture. It is built so that a sweep which passes it cannot have passed by
string-matching contract clause IDs:

- one shape change affects **several** requirements, across **more than one**
  specification;
- one specification is **wholly unaffected**;
- one relationship is genuinely **undecidable** at sweep time;
- one **owner decision** changes;
- one **craft policy clause** changes.

## The mock corpus

Five mock specifications, sixteen mock requirements. Each requirement
carries the machine-readable declaration CC-SPEC-2 defines — six fields,
absent fields meaning an empty list.

### SPEC-REG — project registration

| ID | Mock requirement statement | Declaration |
|---|---|---|
| REG-1 | A registration with no evidence renders `Unknown`, never a green state | `doctrine: [VIS-2]`, `contracts: [RFC3-5]` |
| REG-2 | A registration declares its adapter set at registration time | `contracts: [RFC3-9]` |
| REG-3 | A registration requires recorded consent before any read of the target | `contracts: [RFC1-3]`, `decisions: [OD-1]` |
| REG-4 | A registration summary showing agent-run cost renders `Unknown` for runs with no recorded cost | `policies: [CC-PROV-5]` |

### SPEC-FACETS — honest shape visibility

| ID | Mock requirement statement | Declaration |
|---|---|---|
| FAC-1 | A facet view folds sibling facets according to the folding rules | `contracts: [RFC6-19]` |
| FAC-2 | A folded facet discloses the count of facets folded into it | `contracts: [RFC6-19]`, `doctrine: [VIS-1]` |
| FAC-3 | A selection yields exactly one fact set, and the view renders that fact set's facets without re-deriving them | `contracts: [RFC6-18]` |
| FAC-4 | The facet view and the facet endpoint answer from one truth | `contracts: [RFC6-13]` |

### SPEC-COST — agent run cost

| ID | Mock requirement statement | Declaration |
|---|---|---|
| COST-1 | A run summary with no token count renders `Unknown` for that run | `policies: [CC-PROV-5]` |
| COST-2 | A cost rollup over runs renders `Unknown` where any constituent run's cost is absent | `policies: [CC-PROV-5]`, `doctrine: [VIS-2]` |
| COST-3 | The cost view's absence branch is covered by a test | `policies: [CC-TEST-6]` |

### SPEC-STATUS — status rendering

| ID | Mock requirement statement | Declaration |
|---|---|---|
| STA-1 | A status that cannot be evaluated renders with a reason drawn from the approved reason vocabulary | `decisions: [OD-2]` |
| STA-2 | A status evaluation names its as-of instant | `decisions: [OD-1]`, `doctrine: [VIS-2]` |
| STA-3 | A status evaluation's as-of instant is rendered beside the status in every view | `parent_requirements: [SPEC-STATUS/STA-2]` |

### SPEC-ENTRY — human entry

| ID | Mock requirement statement | Declaration |
|---|---|---|
| ENT-1 | The human entry point is at a fixed location | `contracts: [RFC7-39]` |
| ENT-2 | No surface writes to a governed project outside the declared write boundary | `doctrine: [VIS-5]` |

## The mock authorities the corpus relies on

Enough of each to judge consumption. **Mock content, stated for the
exercise; do not read these as the real clauses.**

| Identity | What it says, for this exercise |
|---|---|
| `RFC6-19` | facet folding rules — which sibling facets may be folded into one, and how the fold is disclosed |
| `RFC6-18` | one fact set per selection — a selection resolves to exactly one fact set, whose facets are those the folding rules produce |
| `RFC6-13` | one truth, two consumers — the view and the endpoint answer from one computation |
| `RFC3-5` | closed declaration field set |
| `RFC3-9` | adapter declaration at registration |
| `RFC1-3` | consent before read |
| `RFC7-39` | fixed human entry location |
| `CC-PROV-5` | missing cost renders `Unknown`, never zero |
| `CC-TEST-6` | absence and Unknown branches are covered |
| `OD-1` | mock owner decision — consent is recorded at registration, not per read |
| `OD-2` | mock owner decision — the approved status-reason vocabulary is a closed list |
| `VIS-1`, `VIS-2`, `VIS-5` | as adopted |

## The shape change

**One logical change** amends three governing identities:

1. **`RFC6-19` (accepted contract clause)** gains one prohibition: *a fold
   may not combine facets whose fact sets differ in provenance.*
2. **`OD-2` (recorded owner decision)** is amended: one value in the closed
   status-reason vocabulary is renamed.
3. **`CC-PROV-5` (approved craft policy clause)** is amended: in addition to
   rendering `Unknown` for a run with no recorded cost, an aggregate must
   **disclose the count of constituent runs whose cost is absent.**

## Your task

Perform the CC-IMPACT-2 reverse-reference sweep over the mock corpus and
report the CC-IMPACT-3 output. Report **all four sets and the denominator**:

```text
population              every requirement examined, counted
affected                requirements a declaration or a consumption ties to
                        the change
explicitly unaffected   requirements examined and found untied — each with
                        the reason AND the method that established untiedness
undecidable             requirements whose relationship the sweep could not
                        settle, each with what would settle it
```

Rules for your answer:

- Every one of the sixteen requirements appears in exactly one set. The
  three sets sum to the population.
- For the `explicitly unaffected` set, state the **method** that established
  untiedness, not only the observation. "Does not declare the changed
  identity" is an observation; if that is your whole method, say so, and
  route what the method cannot decide to `undecidable` rather than to
  `explicitly unaffected`.
- Name which specification, if any, is **wholly** unaffected.
- State plainly anything the mock corpus does not give you.

You are being graded against a golden result you must not look for. **Do not
open `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md`**, and do not read
the disposition register, the semantic delta, or any review file — reading
any of them invalidates the run, and saying so afterwards is the honest
outcome, not a failure.
