# Is Syzygy ready to author Capability 1 in OpenSpec?

## No.

Not one of the eleven conjuncts of the readiness standard is satisfied. Nine
of them require an owner act that has not been performed. The other two —
default-path hygiene and owner-packet comprehension — were `[Unknown]` when
this report was first written and are now **answered, against**: both
reviews were obtained, and both returned findings that the conjunct does not
survive. The answer is not close, and nothing in
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
| 1 | Wave A is lawfully **offerable** and **accepted** | **No.** Confirmed; the offer is withheld by P-33. *(Corrected 2026-08-11 by RD-49: this row previously said no arm preserves the confirmation. Every arm drafted before RD-49 moves an accepted byte; RD-49's arm (1g) moves none.)* | `WAVE-A-INSTALL-SHAPE-DECISION.md`; `round-2026-08f/reviews/RD-49-p33-install-shape-RAW.md` |
| 2 | Wave B is accepted **after** Wave A | **No.** Confirmed (`193e3c1e…`, RD-32c) and unoffered; it follows Wave A | delivery register |
| 3 | P-31, P-36, P-37, P-38, P-39, P-40 are ruled | **No — none is ruled.** All six prepared, in dependency order | `CAPABILITY-1-OWNER-DECISION-PACKET.md` |
| 4 | The specification-acceptance policy is **in force** | **No.** Candidate; amended this pass; needs its own craft act (P-41) | `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` |
| 5 | The shape-to-spec propagation rule is in force **and its fixture passes** | **No.** The rule was **created** this pass — before it, E6's detection step had no owner in any authority. Candidate; needs a craft act. Its fixture exists and has not been re-administered against the new rule | `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`; `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md` |
| 6 | Operating constraints are recorded | **No.** P-35 open; the packet asks eight questions and the honest answers may be `Unknown` | `PROJECT-OPERATING-CONSTRAINTS-DECISION.md` |
| 7 | Launch-gate **v2.0 is owner-approved** | **No.** Candidate, and now **not offerable for a stronger reason**: its two required reviews were obtained and both returned `REVISE` — RD-47 on the validator, RD-48 on semantic preservation. RD-48 confirmed **no readiness question, row-level verdict word, or trend column was dropped, renamed, or made unreachable** — the weakening question is answered *no*. It found the opposite of agreement on the formula: the *computed* formula carries a **sixth** core conjunct that §4 does not state, and `NOT READY` has no home in §1–§8. *(Corrected 2026-08-11: this cell previously read "the computed formula matches §4 conjunct for conjunct", which reverses RD-48 finding 2.)* §4's prose also still names deleted record fields | `LAUNCH-GATE-AUTHORITY-DECISION.md`; `reviews/RD-47…`, `reviews/RD-48…` |
| 8 | The formal structured-data administration returns **READY** | **No.** No formal administration has been run, under v2.0 or any version. The only administration on record is the 2026-08-09 pilot at v1.3: `GATE VERDICT: NOT READY`, 17 of 31 questions Not met, including **all six of section E** | `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` |
| 9 | The owner **separately authorizes** launch | **No.** Downstream of 8; not reachable today | — |
| 10 | Default-path **F4** hygiene passes | **No — reviewed.** RD-50 returned `CONFIRM WITH EXCEPTIONS`: a newcomer reached all five answers in 13 files and 1,864 lines without touching the process history, which is the standard's hardest clause — and then failed the clause "without resolving contradictory process records" three times, plus one blocking rendering defect (repaired this pass) | `reviews/RD-50-default-path-human-clarity-RAW.md` |
| 11 | Owner-packet **F3** comprehension passes | **No — reviewed.** RD-52 returned `REVISE`: four of the eleven rulings cannot be settled at all today, so the one-sitting framing is false by the packet's own contents; measured 3.5–5 hours for the seven that can be | `reviews/RD-52-owner-packet-one-sitting-RAW.md` |

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

- **P-33's recommendation was wrong twice over, and both corrections are
  measurements.** 19 of 19 Wave A and 11 of 11 Wave B modules link into
  `history/` — 68 references — so the standing recommendation (mint
  `contracts-companion/`) was the **most expensive** arm, not the cheapest,
  and the packet had never priced it. It was withdrawn for a typed arm that
  moves one module. RD-49 then found that the replacement is not cheapest
  either: arm **(1g)** moves none and retires no confirmation, and the
  packet's headline claim that no such arm exists was false.
- **E6's detection step had no owner in any authority.** The propagation
  fixture had been saying so, in its own words, for a round. It now has a
  candidate craft rule.
- **CC-SPEC-2 admitted no warrant for a requirement implementing an owner
  decision** — and Capability 1 is largely such requirements.
- **The default path lost 250 lines of process history** without losing a
  fact: `PROJECT-STATUS.md` 398 → 148, the P-34 packet 409 → 137, the
  chronology moved verbatim to a non-default lane.

---

## What eight independent readers found

**All eight fresh-context reviews the charter commissioned (§14) were
obtained.** An earlier revision of this report recorded eight `[Unknown]`s
because no reviewer could be spawned; reviewer capacity became available and
every one ran against frozen bytes at `e2efda6`. Raw output is stored
verbatim in `reviews/`, verdict words copied exactly.

```text
RD-47  structured launch-record schema and validator      REVISE
RD-48  launch-policy v2.0 semantic preservation           REVISE
RD-49  P-33 semantic installation options                 REVISE  (3 blocking)
RD-50  default-path human clarity                         CONFIRM WITH EXCEPTIONS
RD-51  spec-acceptance and shape-to-spec impact policies  REVISE
RD-52  owner-packet one-sitting comprehension             REVISE  (3 blocking)
RD-53  Capability 1 task route and outline exercise       REVISE  (2 blocking)
```

Seven documents, eight commissioned reviews: RD-51 took reviews 5 and 6
together, because CC-IMPACT-1 declares the very things CC-SPEC-2 warrants
and splitting them would have given each reviewer half the question.

**What they found that this pass could not find about itself** — the four
that changed a conclusion rather than a wording:

- **The P-33 packet's headline was false.** It said no arm preserves the
  Wave A confirmation. The act's argument is the digest of the whole wave
  manifest — four generated header lines plus nineteen module rows — so an
  arm that changes only the ceremony retires nothing **provided it leaves the
  header alone, and the header names the acceptance phrase** *(that proviso
  added 2026-08-13, RD-54 finding 2; the unqualified form stated here was
  itself false)*. RD-49 supplied that arm, **(1g)**, which the packet had
  never enumerated and which is cheaper
  than the recommendation on both of the packet's own measures. The claim
  had propagated to three documents including `AGENTS.md`.
- **The owner packet's one-sitting claim is false by its own contents.**
  Four of its eleven rulings cannot be settled at all right now — RD-52
  measured 3.5–5 hours for the seven that can. The packet had labelled the
  claim `[Inferred]` and asked for a review to settle it; the review settled
  it against.
- **The Capability 1 route omitted the half of the capability its title
  names.** RFC-0006 — one truth two consumers, label parity, aggregation
  discloses, one drawer one fact set — was in no Load path, and RFC6-17 is
  cited-never-restated by three of the modules that *were* loaded. So was
  RFC3-16(a), the provenance predicate all five loaded modules defer to.
  RD-53 and the outline exercise found this independently.
- **§4 of the launch instrument, byte-identical by design, still names
  record fields the v2.0 migration deleted.** RD-48 confirmed the migration
  weakened no readiness question and that the computed formula matches §4
  conjunct for conjunct — and then found that §4's own prose points at
  `Owner deferral decision:` and `Deferred count:`, fields no v2.0 record
  has.

**Repaired in this pass, with the review that found each:** the broken
markdown that made twenty of twenty-two open decision rows render as loose
text (RD-50 f1); arm (1g) and the false universal, corrected in all three
places it had reached (RD-49 f1/f2); the Capability 1 route's clause and
module sets, its decision list split by gate, and three of its asserted
counts made computed (RD-53 f1/f2/f4/f5/f6/f7/f10); a selftest fixture named
for a check that did not exist, now pointed at a real deferred-leak
predicate (RD-53 f3); the six-versus-seven facet contradiction (RD-52 f2);
and the P-34 verification command that could not run from where the packet
sits (RD-52 f7).

**Not repaired, and therefore open:** the launch instrument's §4/§5/§7
defects (RD-48 f1–f5), which need an instrument amendment and its own
semantic delta; the validator's five material findings (RD-47 f1–f4, f6);
the specification-acceptance and shape-to-spec findings (RD-51); and the
remainder of RD-49 and RD-52. Every one is recorded in
`reviews/DISPOSITION-REGISTER.md` with its state.

**The repaired bytes are unreviewed.** A repair session may not confirm its
own repairs; each repair above needs a fresh exact-package review before it
counts as anything but a change.

What stands beside the reviews is mechanical evidence, which is weaker and
is not offered as equivalent:

```text
check_governance.py               --selftest   125 fixtures, 0 failing
launch_gate_results.py            --selftest   329 fixtures, 0 failing
validate_launch_administration.py --selftest    75 fixtures, 0 failing
render_launch_administration.py   --selftest    12 fixtures, 0 failing
build_task_router.py              --selftest    11 fixtures, 0 failing
mutation-reverts over the new tools              31 mutants, 0 unwitnessed
```

The mutation harness found **two defects in the very bytes it was proving**:
an `lstrip("./")` that ate the leading dot of every governed path, and a
banner assertion satisfied by an empty constant. Neither was found by
reading. That is the argument for the fixtures — and RD-47 through RD-53 are
the argument against trusting them as a substitute for a reader: every one
of those selftests was green while the four findings above were true.

---

## Hosted CI and clone truth

Hosted CI is **observable and green** at this pass's final commit —
`governance-docs` run `31452287396`, conclusion `success`, head `5e8b286`.
The charter's `Unknown` fallback does not fire.

Its denominator, stated, because it moved twice in this pass: the hosted
workflow ran **four** checks when the pass began and runs **fourteen** now —
the budget report, the wave-manifest and task-router drift checks, the
router's selftest, all four checker selftests, and the worked record's
validation and regeneration — with full history, so that commit-resolving
checks are red when they fail rather than silently unrunnable. Before this
pass a green hosted run was evidence about four checks. It was still short by
three for most of this pass, including the one check that would notice a
misrouted reader, and the workflow now declares that its step list must track
the published battery.

Clean-clone evidence at the final commit — the fourteen checks verbatim, the
eighteen declared WARNs, the seven check families with no fixture, and the
hosted run as an independent second method under a different interpreter:
`FINAL-PUBLIC-CLONE-REPORT.md`.

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
7.  repair RD-47 + RD-48        → both returned REVISE; amend, then re-review
8.  approve P-34
9.  administer the gate formally → different model family, or a human
10. the owner's launch decision  → only after a READY verdict, never by one
```

Steps 1–8 are owner work with review support. Step 9 is the first point at
which the question this report answers can be answered by anything other
than a list of unperformed acts.

`openspec/` does not exist, no specification has been authored, and neither
may change before step 10.
