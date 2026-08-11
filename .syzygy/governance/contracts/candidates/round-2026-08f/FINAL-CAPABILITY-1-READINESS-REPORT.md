# Is Syzygy ready to author Capability 1 in OpenSpec?

## No.

Not one of the eleven conjuncts of the readiness standard is satisfied. Nine
of them require an owner act that has not been performed; two require
evidence this pass could not obtain. The answer is not close, and nothing in
this pass moved it closer to *yes* — this pass moved the **launch decision
off a foundation that could not be trusted**, which is a different and
smaller thing.

> **This report is evidence, never an act.** It authorizes nothing, and no
> statement in it is an owner ruling (VIS-4).

---

## The readiness standard, conjunct by conjunct

Charter §17. Each row is the honest state, with its owning record.

| # | Conjunct | State | Owning record |
|---|---|---|---|
| 1 | Wave A is lawfully **offerable** and **accepted** | **No.** Confirmed, but the offer is withheld by P-33, and **no arm of P-33 preserves the confirmation** — whichever is ruled, the exact-package gate re-runs | `WAVE-A-INSTALL-SHAPE-DECISION.md`; `P33-SEMANTIC-INSTALL-ANALYSIS.md` |
| 2 | Wave B is accepted **after** Wave A | **No.** Confirmed (`193e3c1e…`, RD-32c) and unoffered; it follows Wave A | delivery register |
| 3 | P-31, P-36, P-37, P-38, P-39, P-40 are ruled | **No — none is ruled.** All six prepared, in dependency order | `CAPABILITY-1-OWNER-DECISION-PACKET.md` |
| 4 | The specification-acceptance policy is **in force** | **No.** Candidate; amended this pass; needs its own craft act (P-41) | `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` |
| 5 | The shape-to-spec propagation rule is in force **and its fixture passes** | **No.** The rule was **created** this pass — before it, E6's detection step had no owner in any authority. Candidate; needs a craft act. Its fixture exists and has not been re-administered against the new rule | `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`; `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md` |
| 6 | Operating constraints are recorded | **No.** P-35 open; the packet asks eight questions and the honest answers may be `Unknown` | `PROJECT-OPERATING-CONSTRAINTS-DECISION.md` |
| 7 | Launch-gate **v2.0 is owner-approved** | **No.** Candidate. P-34 is prepared but **not offerable**: its two required independent reviews were not obtained | `LAUNCH-GATE-AUTHORITY-DECISION.md` |
| 8 | The formal structured-data administration returns **READY** | **No.** No formal administration has been run, under v2.0 or any version. The only administration on record is the 2026-08-09 pilot at v1.3: `GATE VERDICT: NOT READY`, 17 of 31 questions Not met, including **all six of section E** | `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` |
| 9 | The owner **separately authorizes** launch | **No.** Downstream of 8; not reachable today | — |
| 10 | Default-path **F4** hygiene passes | **`[Unknown]`.** The default path was materially shortened this pass, and the pass cannot grade its own work. The battery is 0 FAIL, which is not the same claim | this pass; battery output |
| 11 | Owner-packet **F3** comprehension passes | **`[Unknown]`.** Two packets were rebuilt to one-sitting length; the comprehension review was not obtained | `CAPABILITY-1-OWNER-DECISION-PACKET.md` |

**P-33 is the only current obstacle to *offering* confirmed Wave A**, and
nothing in this report obscures that. It is also not the only obstacle to
*readiness*: rows 3 through 11 stand regardless of how P-33 is ruled.

---

## What this pass actually changed

**One thing, and it is structural.** The launch decision no longer depends
on parsing human Markdown as machine truth.

Between v1.3 and v1.18, the launch-gate administration record was a Markdown
file asked to be both a human report and the machine-validated source of a
launch decision. Thirteen consecutive independent re-reviews returned
`REVISE`. Each repair was correct; each minted the next. The last five
converged on one question no rule closed: *is this line the record's own
claim, or a quotation of one?* — reopened in turn by quotations, fences,
comments, list items, continuations, raw HTML, hidden DOM regions, CSS
visibility, tag populations, and disagreements between renderers.

v2.0 deletes the question. The record is JSON validated against a committed
schema; the report is generated and never parsed back; the verdict is
computed and the schema **rejects** a claimed one. §1, §3, §4 and §8 of the
instrument are byte-identical across the change — **no question's text
moved, and the formula is unchanged** — so the migration cannot have
weakened a readiness question, and that is a measurement rather than an
assurance.

Also changed, and worth naming because each was a live defect:

- **P-33's recommendation was wrong, and the measurement says so.** 19 of 19
  Wave A and 11 of 11 Wave B modules link into `history/` — 68 references.
  The standing recommendation (mint `contracts-companion/`) is the **most
  expensive** arm in the space, not the cheapest, and the packet never
  priced it. Withdrawn in favour of a typed arm that moves one module.
- **E6's detection step had no owner in any authority.** The propagation
  fixture had been saying so, in its own words, for a round. It now has a
  candidate craft rule.
- **CC-SPEC-2 admitted no warrant for a requirement implementing an owner
  decision** — and Capability 1 is largely such requirements.
- **The default path lost 250 lines of process history** without losing a
  fact: `PROJECT-STATUS.md` 398 → 148, the P-34 packet 409 → 137, the
  chronology moved verbatim to a non-default lane.

---

## What this pass could not do, and did not fake

**Eight fresh-context reviews were commissioned by the charter (§14). Zero
were obtained.** The authoring session could not spawn reviewer agents — no
pane space in the terminal it runs in — and it did not substitute its own
judgment for theirs. Every artifact this pass produced is therefore
**unreviewed by any independent reader**:

```text
1. structured launch-record schema and validator     not dispatched
2. launch-policy v2.0 semantic preservation          not dispatched
3. P-33 semantic installation options                not dispatched
4. default-path human clarity                        not dispatched
5. revised specification-acceptance policy           not dispatched
6. shape-to-spec propagation fixture                 not dispatched
7. Capability 1 task route and outline exercise      not dispatched
8. owner-packet one-sitting comprehension            not dispatched
```

**The authoring session cannot confirm itself, and did not.** This is why
row 7 above says P-34 is *not offerable* rather than *ready for approval*,
and why rows 10 and 11 read `[Unknown]` rather than *pass*.

What stands in place of those reviews is mechanical evidence, which is
weaker and is not offered as equivalent:

```text
validate_launch_administration.py --selftest    75 fixtures, 0 failing
render_launch_administration.py   --selftest    12 fixtures, 0 failing
launch_gate_results.py            --selftest   329 fixtures, 0 failing
check_governance.py               --selftest   121 fixtures, 0 failing
build_task_router.py              --selftest     9 fixtures, 0 failing
mutation-reverts over the new tools              31 mutants, 0 unwitnessed
```

The mutation harness found **two defects in the very bytes it was proving**:
an `lstrip("./")` that ate the leading dot of every governed path, and a
banner assertion satisfied by an empty constant. Neither was found by
reading. That is the argument for the fixtures and simultaneously the
argument against trusting them as a substitute for a reader.

---

## Hosted CI and clone truth

Hosted CI is **observable and green** at the commit this pass began from —
`gh run list` reports run `31433784576`, conclusion `success`, head
`4aa221b`. The charter's `Unknown` fallback does not fire.

Its denominator, stated: the hosted workflow used to run **four** checks. It
now runs **eleven**, including the budget report, all four selftests, and
the worked record's regeneration check, with full history so that
commit-resolving checks are red when they fail rather than silently
unrunnable. Before this pass, a green hosted run was evidence about four
checks; a reader who took it for the battery was over-reading it.

Clean-clone evidence at the final commit: `FINAL-PUBLIC-CLONE-REPORT.md`.

---

## The plainest answer

**Syzygy is not ready to author Capability 1 in OpenSpec, and will not be
until the owner acts.** The shortest honest path:

```text
1.  rule P-33                    → the Wave A argument regenerates,
                                   one exact-package review re-runs
2.  rule P-31 and P-37           → batched into that same regeneration
3.  the Wave A act, then Wave B
4.  rule P-36, P-38, P-39, P-40  → the authoring-side vocabulary
5.  the two craft acts           → spec acceptance and shape-to-spec impact
6.  record P-35                  → operating constraints, Unknowns allowed
7.  obtain the two v2.0 reviews  → then P-34 becomes offerable
8.  approve P-34
9.  administer the gate formally → different model family, or a human
10. the owner's launch decision  → only after a READY verdict, never by one
```

Steps 1–8 are owner work with review support. Step 9 is the first point at
which the question this report answers can be answered by anything other
than a list of unperformed acts.

`openspec/` does not exist, no specification has been authored, and neither
may change before step 10.
