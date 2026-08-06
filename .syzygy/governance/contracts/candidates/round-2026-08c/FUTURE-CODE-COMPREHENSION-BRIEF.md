# Future code comprehension — craft-and-spec routing brief

> **Candidate routing brief. Binds nothing, and describes nothing that
> exists.** There is no application code. This brief says what evidence would
> have to exist before anyone may claim a Syzygy codebase is comprehensible,
> and where each obligation would be homed. It creates no code, chooses no
> language, and names no framework.

## The claim this brief exists to prevent

> *"The contracts are clear, therefore the code will be clear."*

They are not the same claim and the second has no evidence.

**Codebase understandability is `[Unknown]` and will remain `[Unknown]` until
code exists and a fresh engineer is measured against it.** Not *pending*, not
*expected to be good*, not *green by inheritance from the governance layer*.
VIS-2's rule — no evidence yields Unknown, never green, never zero — applies to
Syzygy's own codebase exactly as it applies to a governed project's, and this
is the first place a project of this shape starts lying to itself.

The contracts constrain what the code must *do*. Whether a stranger can *find*
it is a separate measurement with a separate instrument, and the instrument is
below.

## 1. The measurement — six tasks, one fresh engineer

The comprehension bar is not a document review. It is a timed, recorded
exercise performed by an engineer who did not write the code and has not read
its design discussions. They are given the repository and one capability name,
and asked to do six things in order:

```text
fresh engineer locates one capability
identifies its owning package
finds its public interface
traces it to requirement and tests
explains its dependency boundary
identifies its data and failure contracts
```

**Each step is scored independently and none is inferred from another.** An
engineer who found the package but could not find its public interface scores
1 of 6, not "mostly succeeded". The step-level result is the evidence; a
composite score is exactly the badge the project-shape facet model rejects, and
it is rejected here for the same reason.

**What is recorded per step:** the artifact reached, the number of hops, the
elapsed time, and — where the step failed — the point at which the engineer
stopped and what they were missing. *A failure with a named cause is a better
result than a success with an unrecorded path*, because only the first one
tells the next author what to fix.

**Who may run it:** not the authoring session, and not an agent that
participated in the change. This is CC-REV-4's fresh-reader review applied to
code rather than to normative prose, and CC-REV-2's same-logical-change rule
forbids the author from being the reviewer of their own work. The governing
loop rule this repository has already paid for twice applies unchanged: **a
repair pass and the review of that pass cannot be the same pass.**

## 2. The six steps, and what each one requires to be answerable

| # | Step | What must exist for it to be answerable | Craft home |
|---|---|---|---|
| 1 | **Locate one capability** | A capability identifier that appears in `openspec/**`, in the code tree, and in the work plane as the *same* string. Not three names for one thing | **CC-DEP-2** — stable identities anchor everything |
| 2 | **Identify its owning package** | Exactly one package owns each capability, and the mapping is declared rather than inferred from imports. Two owners is the same defect as none | **CC-DEP-6** — one kernel; surfaces never fork semantics |
| 3 | **Find its public interface** | The package states what is public and what is not. "Public by absence of an underscore" is not a statement | **CC-DEP-5** — public interfaces are contracts with a compatibility story |
| 4 | **Trace it to requirement and tests** | A resolvable path from code → the OpenSpec requirement it satisfies → the tests that verify it, traversable in both directions | **CC-TEST-5** — verification scope is declared |
| 5 | **Explain its dependency boundary** | What the package may depend on, and what may depend on it, declared and enforced — not discovered by reading the import graph | **CC-DEP-1**, **CC-DEP-5** |
| 6 | **Identify its data and failure contracts** | The shapes it accepts and emits, *and* what it does when an input is absent, stale, or unreadable — the Unknown path, named | **CC-TEST-6** — Unknown and absence paths are first-class test targets |

**Step 6 is the one that will be skipped, and it is the one that matters
most.** A data contract that describes only the success shape has not described
the system; it has described the demo. CC-TEST-6 already makes absence a
first-class test target, and this brief adds only that the *documentation* of
the contract must name the absence path too, because an engineer tracing a
failure reads the contract before the tests.

## 3. Literal technical names — the rule and its exact boundary

> **Package names, module names, type names, API paths, schema names, CLI
> commands, and configuration keys use literal technical names.**
>
> **Polaris, Trajectory, Orrery and Mission Control are product codenames.
> They may appear in user-facing presentation, documentation and marketing.
> They may not be the primary identifier of a package, type, endpoint, schema
> or command.**

The reason is not aesthetic. A codename is a word whose meaning must be
learned before any reasoning can start, and a codebase that requires four such
lookups before an engineer can read a route table has spent its comprehension
budget on vocabulary. The governing standard for this whole round says a
capable engineer must reach the contract governing one task *without learning
Syzygy's entire internal vocabulary*; that standard does not stop at the
`.syzygy/` boundary.

**Illustrative only — no name here is chosen, and choosing one would be a
technology decision this lifecycle stage forbids:**

| Not this | This shape |
|---|---|
| a package named for a constellation | a package named for what it does — intent surface, work surface, map surface |
| `/api/polaris/...` | a path naming the resource — capabilities, requirements, work items |
| a type named after a codename | a type named after the thing it models |
| a CLI verb that is a codename | a CLI verb that is a verb |

**Where the codename stays.** A surface's rendered title, its documentation
heading, its narrative prose. `Project Genome` keeps its literal subtitle on
first use in any document — *"Project Genome — the project's complete normative
definition"* — the same rule the term registry applies to poetic codenames
generally.

**How this is checked.** `[Unknown]`, and deliberately so: there is no code to
check and inventing a linter for a language that has not been chosen would be
the technology decision this stage forbids. What is recorded is that **the
check is owed** — an identifier sweep over package, type, endpoint, schema and
command names, with an enumerated allowlist for deliberate codename use, in the
style every other exemption in this repository is carried. It is listed in §6
as an obligation with no owner yet.

## 4. What must exist *before* the first line of code, not after

Comprehension evidence is not retrofittable — an engineer's first read of a
codebase happens once, and a repository that acquires its capability map in
month four has already lost the measurement for months one to three. Four
things must exist before implementation, and all four route to OpenSpec rather
than to this brief:

1. **The capability identifier scheme** — one string per capability, used
   identically in `openspec/**`, the code tree and the work plane (step 1).
2. **The capability → package ownership declaration** — machine-readable,
   single-owner, checkable (step 2).
3. **The requirement ↔ code ↔ test traversal**, in both directions (step 4).
4. **The dependency boundary declaration** per package (step 5).

**None of these is code.** Each is a declaration that code must then conform
to, which is the only ordering under which a comprehension claim can ever be
`[Observed]` rather than asserted.

## 5. What this brief refuses to claim

Stated plainly, because a brief that only lists requirements reads as though
meeting them were already underway:

- **It does not claim the contracts prove future code clarity.** They do not.
  The relationship between a clear specification and a clear implementation is
  `[Unknown]` and this project has no instance of it to reason from.
- **It does not claim the six-step exercise is validated.** It has never been
  run, on anything. `[Inferred]` that it measures what it intends to; the first
  run is also the first test of the instrument, and its result should be read
  with that doubled uncertainty.
- **It does not set a passing threshold.** How many of six steps must succeed,
  and how fast, is an engineering-bar question owned by craft policy and not
  settled here. Setting it here would install a number into a brief that binds
  nothing, which is exactly the volatile-value defect this round spent a
  workstream removing.
- **It does not survive contact with a real codebase unamended.** `[Inferred]`,
  and stated so that the first amendment is expected rather than treated as a
  failure of the brief.

## 6. Routing

| Obligation | Home | Status |
|---|---|---|
| Comprehensible truth as a merge constraint | **CC-BAR-3** (owner-approved) | **Exists.** Covers normative artifacts explicitly; whether it reaches *code* comprehension is the gap this brief names |
| Public interface is a contract | **CC-DEP-5** (owner-approved) | Exists |
| Stable identities | **CC-DEP-2** (owner-approved) | Exists |
| Absence paths are test targets | **CC-TEST-6** (owner-approved) | Exists |
| Fresh-reader review, and author ≠ reviewer | **CC-REV-4**, **CC-REV-2** (owner-approved) | Exists for normative artifacts |
| **The six-step comprehension exercise as a required evidence class** | **missing** — smallest home is **CC-REV-1**, which already enumerates mandatory independent review classes and would gain one | Craft amendment, owner act. **Not proposed here** — a second craft amendment in flight alongside CC-TEST-2 would put two unaccepted amendments in one gate |
| **The literal-technical-names rule** | **missing** — smallest home is **CC-DEP-2**, which already owns identifiers | Craft amendment, owner act. Same deferral |
| **The identifier-name check** | **missing, and unownable today** — no language chosen | Recorded as owed |
| Capability identifier scheme; capability→package ownership; requirement↔code↔test traversal; dependency boundary declaration | **OpenSpec** — all four are observable behaviour | Routed to `FIRST-OPENSPEC-SEQUENCE.md`, Capability 1 and Capability 2 |

**Two craft amendments are named and neither is proposed.** Both are one-clause
additions to rules that already exist, and both would be normative edits landed
in the same pass that is asking the owner to accept an unrelated craft
amendment. They are recorded for the pass after the acts, which is the same
disposition every other deferred normative edit in this round received.
