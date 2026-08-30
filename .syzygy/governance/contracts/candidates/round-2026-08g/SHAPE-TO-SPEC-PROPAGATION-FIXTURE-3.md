# Shape-to-spec propagation fixture 3 — the blind exercise

> **Non-product governance fixture.** Everything below is deliberately
> fictitious: the "specifications" are mock stubs that exist only inside
> this file, **no `openspec/` tree exists or is implied**, and no mock
> requirement describes real intended behavior. Doctrine rule IDs and
> accepted/approved contract and craft clause IDs are real, so that the
> exercise tests a sweeper who knows the corpus's authority tiers; **owner
> decisions are mock** (`OD-11`, `OD-12`) because no owner product decision
> has been ruled, and **the topology identity is mock** (`TOPO-1`) because
> no topology identity is accepted yet (`map/topology/` does not exist —
> only `map/topology-candidates/`) — writing a real pending or candidate
> identifier into a "was amended" scenario would state a falsehood inside a
> governance artifact. These mock identifiers are private to this file and
> do not refer to, and must not be confused with, fixture 2's `OD-1`/`OD-2`.
>
> **This file contains no answer.** The golden result lives in
> `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-3-ANSWER-KEY.md`, a separate file, so
> that "the reviewer derives the result without reading the answer" is
> structural rather than an honour system.
>
> **This fixture supersedes
> `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md`.** RD-59 ran fixture 2 blind and
> passed it, and in doing so found two defects in the fixture itself, plus
> a third defect in fixture 2's answer key that the disposition register
> records honestly (`reviews/DISPOSITION-REGISTER.md`, RD-59 section):
>
> 1. Fixture 2 states the CC-SPEC-2 declaration has six fields, but **no
>    mock requirement carried a `topology[]` value** — `grep -c topology`
>    over fixture 2 returns 0. One of the six warrant classes was entirely
>    unexercised, and a sweeper blind to `topology[]` as a trigger could not
>    have been caught failing on it. Fixed here: `CAP-3` declares
>    `topology: [TOPO-1]`, and the shape change amends `TOPO-1`, so a
>    sweeper that does not treat topology as a sweep trigger **misses an
>    affected requirement**, not merely an unexercised field.
> 2. Fixture 2's task block asked for a CC-IMPACT-2 sweep and CC-IMPACT-3
>    output while stating only the four-set schema, never the clauses'
>    own text — sufficient by luck, not by design. Fixed here: the task
>    block below quotes both clauses directly.
> 3. Fixture 2's FAC-3-equivalent requirement declared a sibling clause
>    whose authority-table entry left genuine room for a two-way
>    undecidable/affected split (RD-59's own administrator resolved it
>    correctly in one hop from the fixture's own text; the answer key's
>    stated reason for calling it `undecidable` was wrong, though the pass
>    criterion's hedge absorbed the disagreement). Fixed here: `DIS-3`'s
>    authority-table entry (`RFC6-20`) states its tie to the amended clause
>    inside its own text, with no hedge and no second reading available.
>
> **Fixture 2 is not edited.** CC-IMPACT-7 names it by path **and sha256**
> in its own operative text; editing it after RD-59 bound a run to those
> bytes would make that run worth nothing (verification rule 10). Fixture 2
> carries no in-file banner for the same reason — any edit, including a
> banner, changes its digest. The supersession is recorded in
> `reviews/DISPOSITION-REGISTER.md`'s RD-59 section, which is the account
> that already anticipated this fixture before it existed, and in this
> fixture's own provenance note. **CC-IMPACT-7 continues to name fixture 2
> until a fresh, independent blind run against fixture 3 passes and is
> dispositioned — that run is explicitly out of scope for the change that
> authored this file** (`[Unknown]` until then; not run here).

## What this fixture is for

CC-IMPACT-7 requires the propagation path to be exercised against a fixture
with a known answer, blind, **before** it is relied on. This is the
successor fixture to fixture 2. It is built so that a sweep which passes it
cannot have passed by string-matching contract clause IDs, and — new in
this fixture — cannot pass by ignoring `topology[]` as a trigger class:

- one shape change affects **several** requirements, across **more than
  one** specification;
- one specification is **wholly unaffected**;
- one relationship is genuinely **undecidable** at sweep time;
- one **owner decision** changes;
- one **craft policy clause** changes;
- one **topology identity** changes, and at least one requirement's
  declaration names it.

## The mock corpus

Five mock specifications, sixteen mock requirements. Each requirement
carries the machine-readable declaration CC-SPEC-2 defines — six fields,
absent fields meaning an empty list.

### SPEC-CAPTURE — evidence capture

| ID | Mock requirement statement | Declaration |
|---|---|---|
| CAP-1 | A capture with no verifiable source renders `Unknown`, never a green state | `doctrine: [VIS-2]`, `contracts: [RFC5-6]` |
| CAP-2 | A capture records the observer identity that produced it | `contracts: [RFC5-11]` |
| CAP-3 | A capture requires an accepted topology observation boundary to be named before it may run | `topology: [TOPO-1]` |
| CAP-4 | A capture's per-run cost is disclosed | `policies: [CC-PROV-6]` |

### SPEC-DISCLOSE — honest shape disclosure

| ID | Mock requirement statement | Declaration |
|---|---|---|
| DIS-1 | A disclosure view folds sibling gaps according to the folding rules | `contracts: [RFC6-19]` |
| DIS-2 | A folded gap discloses the count of gaps folded into it | `contracts: [RFC6-19]`, `doctrine: [VIS-1]` |
| DIS-3 | A selection yields exactly one gap set, and the view renders that gap set's members without re-deriving them | `contracts: [RFC6-20]` |
| DIS-4 | The disclosure view and its machine endpoint answer from one truth | `contracts: [RFC6-13]` |

### SPEC-BUDGET — resource budget

| ID | Mock requirement statement | Declaration |
|---|---|---|
| BUD-1 | A budget summary with no recorded token count renders `Unknown` for that run | `policies: [CC-PROV-6]` |
| BUD-2 | A budget rollup renders `Unknown` where any constituent run's cost is absent | `policies: [CC-PROV-6]`, `doctrine: [VIS-2]` |
| BUD-3 | The budget view's absence branch is covered by a test | `policies: [CC-TEST-6]` |

### SPEC-STATE — evaluation state

| ID | Mock requirement statement | Declaration |
|---|---|---|
| STA-1 | An evaluation state that cannot be computed renders with a reason drawn from the approved reason vocabulary | `decisions: [OD-11]` |
| STA-2 | An evaluation state names its as-of instant | `decisions: [OD-12]`, `doctrine: [VIS-2]` |
| STA-3 | An evaluation state's as-of instant is rendered beside the state in every view | `parent_requirements: [SPEC-STATE/STA-2]` |

### SPEC-SURFACE — human entry surface

| ID | Mock requirement statement | Declaration |
|---|---|---|
| SUR-1 | The human entry point is at a fixed location | `contracts: [RFC7-39]` |
| SUR-2 | No surface writes to a governed project outside the declared write boundary | `doctrine: [VIS-5]` |

## The mock authorities the corpus relies on

Enough of each to judge consumption. **Mock content, stated for the
exercise; do not read these as the real clauses.**

| Identity | What it says, for this exercise |
|---|---|
| `RFC6-19` | gap folding rules — which sibling gaps may be folded into one, and how the fold is disclosed |
| `RFC6-20` | gap-set composition — a selection resolves to exactly one gap set for the view to render. **This clause states no independent membership rule: a gap set's members are, by this clause's own text, "exactly those the folding rules currently admit."** A change to the folding rules (`RFC6-19`) is therefore a change to what `RFC6-20` composes — that tie is stated inside `RFC6-20` itself, not inferred from outside it, and settling it needs no contract-owner ruling and no reading `RFC6-20` does not already contain |
| `RFC6-13` | one truth, two consumers — the view and the machine endpoint answer from one computation |
| `RFC5-6` | closed capture-source field set |
| `RFC5-11` | observer identity recorded at capture time |
| `RFC7-39` | fixed human entry location |
| `CC-PROV-6` | missing run cost renders `Unknown`, never zero |
| `CC-TEST-6` | absence and Unknown branches are covered |
| `OD-11` | mock owner decision — the approved status-reason vocabulary is a closed list |
| `OD-12` | mock owner decision — the as-of instant is recorded at evaluation time, not per render |
| `TOPO-1` | mock topology identity — the observation boundary a capture must run inside |
| `VIS-1`, `VIS-2`, `VIS-5` | as adopted |

## The shape change

**One logical change** amends four governing identities:

1. **`RFC6-19` (accepted contract clause)** gains one prohibition: *a fold
   may not combine gaps drawn from different observation boundaries.*
2. **`OD-11` (recorded owner decision)** is amended: one value in the
   closed status-reason vocabulary is renamed.
3. **`CC-PROV-6` (approved craft policy clause)** is amended: in addition
   to rendering `Unknown` for a run with no recorded cost, an aggregate
   must **disclose the count of constituent runs whose cost is absent.**
4. **`TOPO-1` (mock topology identity)** is amended: the observation
   boundary's definition changes to exclude any observer lacking a
   recorded credential.

## Your task

Perform the **CC-IMPACT-2** reverse-reference sweep over the mock corpus
and report the **CC-IMPACT-3** output. The clauses, quoted:

> **CC-IMPACT-2 — A shape delta performs a reverse-reference sweep, and the
> trigger set is the warrant set.**
>
> The identities that can trigger a sweep are exactly the identities that
> can warrant a requirement — CC-SPEC-2's six classes, and no others.
>
> When an adopted doctrine rule, an accepted contract clause, an approved
> craft/policy clause, a recorded owner decision, an accepted topology
> identity, or an accepted parent requirement or specification changes,
> the change carries a sweep over the specification corpus for every
> specification whose CC-IMPACT-1 declarations name the changed identity,
> or whose requirements consume its vocabulary. The sweep is part of the
> change, not a follow-up task.

> **CC-IMPACT-3 — The sweep records four sets, with its denominator and its
> method.** The sweep's output names:
>
> ```text
> population              every specification and requirement examined, counted
> affected                those a declaration or a consumption ties to the change
> explicitly unaffected   those examined and found untied — each with the reason
>                         AND the method that established untiedness
> undecidable             those whose relationship the sweep could not settle,
>                         each with what would settle it
> ```
>
> The reason and the method are two different things, and both are
> required. "Does not declare the changed identity" is an *observation*;
> if declaration-matching is the whole method, the sweep says so, and
> everything that method cannot decide routes to `undecidable` under
> CC-IMPACT-4 rather than to `explicitly unaffected`. A true reason
> producing a wrong answer, carried by a denominator and full compliance,
> is the failure mode this limb exists to prevent.

Report **all four sets and the denominator**, in this shape:

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
- For the `explicitly unaffected` set, state the **method** that
  established untiedness, not only the observation. "Does not declare the
  changed identity" is an observation; if that is your whole method, say
  so, and route what the method cannot decide to `undecidable` rather than
  to `explicitly unaffected`.
- Name which specification, if any, is **wholly** unaffected.
- State plainly anything the mock corpus does not give you.

You are being graded against a golden result you must not look for. **Do
not open `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-3-ANSWER-KEY.md`**, and do not
read the disposition register, the semantic delta, or any review file —
reading any of them invalidates the run, and saying so afterwards is the
honest outcome, not a failure.

## Provenance

Built 2026-08-30 for CC-IMPACT-7 (candidate P-42), following RD-59's
graded blind run of fixture 2 (`reviews/DISPOSITION-REGISTER.md`, RD-59
section). Supersedes
`SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md`, whose bytes are unedited and
whose digest CC-IMPACT-7 continues to name until a fresh confirming blind
run against this fixture passes and is dispositioned — that run is
separate follow-on work, not performed by the change that authored this
file.
