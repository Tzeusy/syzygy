# Round-2026-08g — the Capability 1 planning charter, and the views generated from it

> **Candidate account. Binds nothing.** It records what was built and what was
> measured. It adopts no doctrine, accepts no contract, approves no policy,
> rules no queue row, and creates no `openspec/`. Every clause named here is a
> **candidate** clause of a confirmed-but-unaccepted wave.

## The defect this addresses

Capability 1's shape was stated in five places that had to agree by hand: the
task router's route, the first-spec sequence's scope table, the E3 trace
table, a clause-coverage list, and a blocking-decision list. Each restated the
others. Nothing measured the agreement.

That is the same defect the owner charter §11.5 named in `AGENTS.md` — a
record restating state another record owns, going stale silently — and the
same one verification rule 3 states as a rule: *a derived value quoted outside
its owning artifact goes stale silently.* Five hand-maintained restatements of
one fact set is five chances to be wrong and no way to find out.

## What was built

**One source.** `CAPABILITY-1-CHARTER.yaml` — capability ID, title, a
one-sentence argument, the required and deferred waves, capability-level
doctrine, six behaviour rows with their clause / doctrine / decision /
policy / topology fields, the blocking and downstream decision lists,
non-goals, deferred semantics, and a `self_checks` list.

**One generator.** `scripts/build_capability_1_views.py`, stdlib only,
producing:

| View | Where it lands |
|---|---|
| the Capability 1 task-router route | consumed in-process by `build_task_router.py` |
| the first-specification sequence's behaviour rows | a marked generated block inside `FIRST-OPENSPEC-SEQUENCE.md` |
| the E3 trace-table skeleton | `CAPABILITY-1-GENERATED-VIEWS.md` |
| the initial clause-coverage population | same |
| the blocking-decision list | same |

`--check` fails on drift in any of them. The router imports the charter's
route payload directly, so a charter that does not validate makes the router
**fail**, not silently fall back to a stale route.

### The design decision that carries the most weight

**No authority home is written in the charter.** It names clause IDs and
nothing else; the builder resolves each ID to its owning module through the
generated `05-CONTRACT-INDEX.yaml`. A wrong path cannot be authored, because
no path is authored. A clause that does not exist, or is homed outside Waves
A+B, fails generation.

This is the rule *"a generator that quotes prose has re-opened the door it
closed"* applied one level up: a generator that lets its **input** carry a
transcribed path has re-opened the same door.

## The self-checks, and the mutations that prove them

The charter states six assertions about itself. Each is tested, and each test
was verified by breaking it:

| Self-check | Charter-named mutation | Result when mutated |
|---|---|---|
| every clause resolves to exactly one module in the contract index | **a missing clause** | generation fails |
| every resolved module is named by the Wave A or Wave B manifest | — | fails |
| no resolved module is named by a deferred-wave manifest | **an extra deferred module** | generation fails |
| every decision entry is an **open** row of the pending-decisions queue | **a missing decision** | generation fails |
| no decision in both blocking and downstream lists | — | fails |
| no clause in two behaviour rows | — | fails |
| *(architectural)* homes are resolved, never authored | **a wrong authority home** | **unauthorable** — there is no field to put one in |

**Two predicates had no coverage and were found by mutation, not by reading.**
Disabling the row-level `owner_decisions` check produced **0** fixture
failures, and so did disabling the `downstream_decisions` check — both were
running and neither was tested. Three fixtures were added (`row_decision`,
`blocking_executed`, `downstream_unknown`) and each of the three code paths
was re-verified to fail when disabled (1, 3 and 1 failures respectively). The
selftest now holds **18 fixtures**.

This is the same defect class RD-56 f4 found one workstream earlier: a check
that runs, is believed, and discriminates nothing. Verification rule 6 —
*mutate the input and confirm the check fails, per predicate* — is the only
thing that finds it.

### And then the fixtures did it a third way

Adding `RFC6-23` to row 1.5 turned one of the eighteen fixtures red. The cause
was not the new clause: the `duplicate_clause` fixture mutated the literal
`governing_clauses: [RFC7-40]`, row 1.6 had earlier gained two clauses, the
`.replace` matched nothing, and **the fixture had been passing while testing
nothing.** It reported green until an unrelated edit happened to make its
assertion fail.

That is the same shape as the `LA-11` fixture that broke the same day, when a
commit from another session untracked `.beads/issues.jsonl` and left a
launch-gate fixture bound to a path that no longer existed. **A mutation that
silently stops mutating is a check that silently stops checking**, and neither
instance was found by design — both surfaced because something else failed.

Repaired here for the eight mutation fixtures in this builder: each now
asserts its mutation applied, and each guard was verified by breaking its
literal and confirming the dependent fixtures fail (1, 3 and 2 failures for
the three literals). Measured across the battery, the exposure elsewhere is
real and larger — 216 unguarded mutation sites in `launch_gate_results.py`,
4 in `check_governance.py`, 3 in `validate_launch_administration.py`, 1 in
`render_launch_administration.py`, and 0 in `build_task_router.py`, which uses
none. Filed as work rather than fixed here, because the general repair is one
raising helper applied at every site and that churns a 329-fixture suite this
pass is not otherwise touching.

## What the fresh-agent outline exercise returned

Charter §10's closing exercise was run and is recorded in full at
`reviews/RD-60-capability-1-outline-exercise-RAW.md`, dispositioned in
`reviews/DISPOSITION-REGISTER.md`. It was given the generated route, the
charter, the generated views, and the contract modules those name — and
withheld every review, register, status file, sequence document and the
decision queue. **No ruling was available to it**, because none has been made,
and no spec-quality policy is in force.

Two results are worth carrying out of that record:

1. **It found four clause gaps by trying to write requirements and running out
   of authority.** `RFC6-22`, `RFC1-27` and `RFC3-3` were added to the charter
   on its evidence; `RFC6-23` was added by the dispositioning session on a
   reliance argument the exercise did not make. That is evidence a reading
   pass would not have produced.
2. **The charter carried no decoration.** Sweep run this session over the
   exercise's argument: **34 clause IDs cited, all 25 of the charter's
   then-current clauses among them, 0 uncited.**

And two limits, stated because they bound what the exercise proves:

- Its shape/behaviour split is **its own construction**. No specification
  quality bar is in force — `P-41` is exactly the decision that would end that
  — so nothing in the repository warrants the form/oracle/falsifier shape it
  used, and it said so unprompted.
- It converged with the charter's own `deferred_semantics` on the two rows the
  charter already flags (`P-37`'s facet vocabulary, `P-31`'s
  merged-but-unreconciled reason). Convergence between a fresh reader and the
  record is worth something; it is not independent confirmation, since both
  read the same clauses.

## What this does not claim

- **It does not claim Capability 1 is ready to author.** Nine capability-level
  queue rows block authoring before any row-level question is reached, and the
  generator refuses to build a route that names a resolved or executed one.
- **It does not claim the six behaviour rows are the right six.** They were
  hand-authored into the charter from the prior sequence document; the
  generator checks their *consistency*, never their *sufficiency*. Nothing
  here tests whether a seventh row is missing, and the outline exercise
  proposed none — which is one reader's silence, not a measurement.
- **It does not claim the clause set is complete.** It is now demonstrably
  more complete than it was, by four clauses, found by one exercise. A second
  exercise would be the way to find out whether that number is converging.
- **It resolves no `P-nn` row and performs no act.**

## Battery

Two checks were added to the published battery, which is now sixteen:

```sh
python3 $CS/build_capability_1_views.py --check      # charter → five views, drift
python3 $CS/build_capability_1_views.py --selftest   # 18 fixtures
```

`PROJECT-STATUS.md` owns the canonical list and states its count; CG-26
asserts the published battery equals the hosted one, and reports 16 / 16 / 16.
