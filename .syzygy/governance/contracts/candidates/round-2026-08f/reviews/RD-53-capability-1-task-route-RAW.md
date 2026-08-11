# RD-53 — Capability 1 task route and outline exercise (round-2026-08f, frozen commit `e2efda6`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 review 7 — the generated Capability 1 route, its generator, and the outline exercise's pass criteria |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `e2efda6` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Subject files** | `TASK-ROUTER.md`; `scripts/build_task_router.py`; `round-2026-08f/CAPABILITY-1-CONTEXT-ROUTE-REPORT.md`; `round-2026-08f/CAPABILITY-1-SPEC-OUTLINE-EXERCISE.md` |
> | **Context** | fresh — subject, governing references and acceptance criteria only |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `REVISE` — with two findings the reviewer marks **BLOCKING** |
>
> **A note on one of the reviewer's own observations.** The reviewer found
> `CAPABILITY-1-SPEC-OUTLINE-EXERCISE-RAW.md` untracked in the working tree
> during its run — the exercise was administered in the same session, after
> this review's subject was frozen. The reviewer handled it correctly: it
> used the file only as corroboration of findings it had already reached
> independently, graded nothing by it, and recorded the discrepancy. Its
> caution stands in the record.
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.

---

Repository untouched at e2efda6 (the untracked files predate or come from concurrent peer sessions; I created none). All mutation work was done in a scratchpad copy.

---

VERDICT: REVISE

---

## A. What the generator's checks actually verify

**Method.** Ran both commands at e2efda6 and read the output; then mutated a scratchpad copy (`/tmp/.../scratchpad/mut/syz/`) per-predicate and re-ran.

**Observation.** Both pass:
```
task router matches regeneration — 13 task classes validated          (--check, exit 0)
9 fixtures, 0 failing — a check that cannot fail is not a check       (--selftest, exit 0)
```

What they genuinely verify (I confirmed each by mutation):
- every routed path exists (`validate`, line 355–357);
- every cited clause ID is defined via `**<ID>` in the module the route names (line 361);
- every doctrine/craft identifier appears somewhere in its named file — a substring test, not a clause test (line 366);
- a `deferred=True` route carries the word "deferred" in some omission string (line 368);
- each `blocking_decisions` entry has a row matching `^\|\s*P-n\s*\|` **anywhere in the queue file** (line 379);
- `--check` catches any hand-edit of `TASK-ROUTER.md` (I replaced `` `RFC8-18` `` with `` `RFC8-99` `` → "task router drifted from regeneration", exit 1).

What they do **not** verify — each confirmed by a passing mutation:
1. **No deferred-wave check on the load set.** I injected two real deferred modules into the Capability 1 `modules` list — `rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md` and `rfcs/RFC-0011/deterministic-selection-and-budget.md`. `--selftest` printed **"9 fixtures, 0 failing"** and the generator wrote the file reporting **"all routes validated"**, with both deferred modules rendered into the Capability 1 **Load:** line and the computed dependency line extended to `…RFC-0009, RFC-0010`. The fixture literally named *"Capability 1 route: a deferred-wave module in the load set detected"* does not test this: it mutates `clauses`, not `modules`, mapping `RFC10-5` onto an RFC-0007 module and expecting `"not defined in"` — the identical predicate the preceding fixture already covers. **The fixture's name is false.**
2. **"Open" is never tested.** I added the four already-**Executed** rows P-6, P-7, P-13, P-26 to `blocking_decisions`. Validation passed and the file rendered: `` `P-6`, `P-7`, `P-13`, `P-26` — each verified open in the pending queue at generation time``. The check tests row *presence*, not openness; the seven `**Executed.**` rows live in the same file and match the same anchor.
3. **No completeness check** on clauses, modules, or blocking decisions — only spelling and existence of what is already hand-listed. A route omitting a needed clause is invisible.
4. **No coverage of the untested-passing direction.** Every fixture asserts a mutation *is* caught; none asserts a wrong entry *should* be rejected while currently accepted.
5. `n = 9` (line 502) is a hardcoded literal, not `len(cases)`. Adding a tenth fixture would still print "9 fixtures".

**Judgement.** The checks are real and non-trivial for what they cover — path existence, clause-definition anchoring, and regeneration drift are genuinely mutation-proven. But three of the four properties the module docstring advertises for the Capability 1 route are not enforced, and one selftest fixture is named for a check that does not exist. **Inadequate as stated.**

## B. Is the clause list complete? No.

**Method and denominator.** The 30 Waves A+B modules (19 in `WAVE-A-MANIFEST.txt` + 11 in `WAVE-B-MANIFEST.txt`); I verified all 30 sha256 digests match the manifests, so the sweep is over the frozen bytes. Those modules define **344 distinct clauses** (Python `re` on `\*\*(RFC\d+-\d+)\b`). Rather than judge relevance from 344 by taste, I took the project's own two artifacts that name Capability 1's governing clauses — `FIRST-OPENSPEC-SEQUENCE.md` rev3 rows 1.1–1.6 (the scope table) and `round-2026-08e/FIRST-SPEC-TRACE-TABLE.md` (E3, which the sequence says "anchors each row's clauses at the current bytes") — and compared.

**Observation.** The two artifacts name **18 on-path clauses**. The route names **10**. The intersection is **6** (`RFC1-1`, `RFC3-4`, `RFC3-7`, `RFC7-39`, `RFC7-40`, `RFC2-24`). **The route omits 12 of 18.**

| Omitted | Defining module | In route's Load set? |
|---|---|---|
| RFC6-13, 6-14, 6-15, 6-18, 6-19, 6-26 | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | **No** |
| RFC5-3 | `rfcs/RFC-0005/admission-and-boundary.md` | **No** |
| RFC3-1, 3-5, 3-6, 3-9 | `rfcs/RFC-0003/manifests-and-namespace.md` | Yes (unnamed) |
| RFC1-3 | `rfcs/RFC-0001-…-state-planes.md` | Yes (unnamed) |

Seven of the twelve are **unreachable** — their defining modules are in Wave A but not in the route's five-module Load set.

The substitution is a category error. `FIRST-OPENSPEC-SEQUENCE.md:35` says row 1.4's authority is "RFC6-18/19 as amended", and its prerequisite table (line 66) says "the anti-rollup ground (RFC6-18/19 as amended) is Wave A's". The route instead routes anti-rollup to RFC8-18/8-19, which are cost clauses:

> **RFC8-18.** Cost renders as **independent measures, never a composite**.
> **RFC8-19.** **Absent means Unknown, never zero** … Every aggregate over partially-known measures discloses coverage ("cost known for n of m runs")

Likewise row 1.5's "identically to human and machine" is `RFC6-13`/`6-14`; the route substitutes `RFC7-33`, which is expressly scoped: "Every distinction **this package** draws".

Worse, two clauses the loaded modules themselves declare are **cited-never-restated** are undefined in the Load set:

- **RFC6-17** ("Aggregation discloses") — defined in RFC-0006. `rfcs/RFC-0002/rendering-vocabularies.md:148`: *"An aggregate satisfying this sentence alone still violates RFC6-17. The obligation is cited here, not restated, so the two cannot drift."* Also `rfcs/RFC-0003/manifests-and-namespace.md:497` and `rfcs/RFC-0007/rendering-and-surface.md:308`. Cited by **3 of the 5** loaded modules (8 citations). This is the "no rollup, no composite badge" obligation — the heart of "honest shape visibility".
- **RFC3-16(a)** (owner-act provenance predicate) — defined in `rfcs/RFC-0003/governance-homes-and-owner-acts.md:158`, a Wave A module. Cited by **5 of the 5** loaded modules (30 citations). `manifests-and-namespace.md:595` makes it load-bearing on a clause the route *does* name: "a consent record's stored attribution (**RFC3-7**) … honored only under **RFC3-16(a)**".

**Judgement. Material, and it defeats the route's stated purpose.** The route names what an author must read for project *registration* reasonably well, and for *honest shape visibility* it does not: the anti-rollup ground, the aggregation-disclosure obligation, the human/machine parity clauses, and the unconsented-renders-as-policy clause are all unreachable. This is corroborated independently — the router's own sibling Polaris route handles the identical pattern correctly ("RFC-0009 is NOT omitted — it is a declared, clause-borne dependency … stated at RFC9-45, never duplicated locally"), so the generator's authors know the rule and did not apply it here.

## C. Deferred-wave leakage: none in substance.

**Method.** Built the full `depends_on` graph from front matter across all RFC modules, then computed the true transitive closure of the Capability 1 Load set — the report calls the generator's line a "transitive closure", so I checked whether it is one.

**Observation.** The dependency graph points strictly downward: `RFC-0010 → [0001-0006, 0008]` and `RFC-0011 → [0001-0006, 0008, 0010]`, and **nothing in RFC-0001…0009 depends on RFC-0010 or RFC-0011**. True transitive closure of the Capability 1 Load set = `{RFC-0001 … RFC-0009}` — entirely Waves A+B. Text sweep of the five loaded modules confirms no routing into deferred content. The route's first omission ("Every Mission and Context-selection contract — RFC-0010 and RFC-0011 — is excluded") is accurate.

Two caveats. (i) `module_deps` (line 338) is **one level deep**, not transitive; the report's word "transitive closure" is wrong, though harmless here because the true closure is no wider. (ii) The absence is an *observation*, not a *check* — per A.1, injecting RFC-0010 changed the line to include it and nothing failed.

**Judgement. Clean.** No leak, directly or through closure. But the assurance rests on the shape of the dependency graph, not on any enforcement, and the report overstates it as mechanically guaranteed.

## D. Blocking owner decisions: correct in spelling, incomplete in substance, and the validation is not real.

**Method.** Enumerated all queue rows with Python `re` (42 strict matches + `P-25(c)`, 43 total); read the queue's own **Launch-scope index** (lines 118–152); cross-read `FIRST-OPENSPEC-SEQUENCE.md`'s prerequisite table; ran the production predicate against ruled rows.

**Observation.** The queue's own index partitions the decisions by gate:

> - **Gate authoring the first spec:** P-36 …, P-39 …, P-40 …, P-41 …, **plus the two wave acts themselves.**
> - **Gate the formal launch administration, not the spec:** P-34 (instrument authority), P-35 (operating constraints).
> - **Ratified or reverted at the Wave A act …:** P-31 …, P-37 …, **P-28** …, and **P-21(a)** …
> - **Ratified or reverted at the Wave B act …:** P-38 …, **P-22** …

Against that partition the route's list of 11 is:
- **Correctly named (9):** P-33, P-31, P-37, P-38, P-36, P-39, P-40, P-41, P-42 (P-42 postdates the index; its own row says "Earliest gate: before the first spec is authored", and the index's closing line says the row wins).
- **Omitted, on the index's own reading (4):** **P-1** — the two wave acts, which the authoring bullet names explicitly; **P-28** and **P-21(a)** (ride the Wave A act); **P-22** (rides the Wave B act, and is a *project registry placement* question — the core of "project registration").
- **Over-included (2):** **P-34, P-35**, which the index assigns to a different gate. `FIRST-OPENSPEC-SEQUENCE.md:73` on P-35: "**the spec itself does not consume it**".

The P-1 omission is not defensible as "acts are not decisions", because **P-41 and P-42 are themselves craft acts and are in the list**. The route's note "Every blocking owner decision is named below" is therefore inaccurate under its own inclusion rule.

On validation: it is **spelling only**. Confirmed by execution — the four `**Executed.**` rows P-6/P-7/P-13/P-26 validate and render under "each verified open". Two further hazards: the strict pattern misses suffixed IDs like `P-25(c)`; and eight blank lines inside the open table mean a human reader sees P-21…P-42 as literal pipe-delimited paragraphs while the line-anchored regex sees rows — machine and reader disagree.

**Judgement. Material.** The named 11 are each real and each genuinely open today, so the route is not misleading in what it says; but it is incomplete in what it omits, over-inclusive by two, and the emitted words "verified open" claim more than the check performs.

## E. Honesty of the omissions, and transcription.

**Method.** Compared every measurement-shaped string in the generated file against its source; compared the report against the router it reports on.

**Observation.** The omissions section is genuinely good in character — it names the deferred waves, refuses to list candidate craft under "Craft", and refuses to route the facet vocabulary to a plausible clause. That last refusal is the right call and rare.

But the file's closing line asserts **"Counts computed, never asserted"**, and four of its five counts are asserted:

| String | Computed? | True today? |
|---|---|---|
| "13 task classes" | Yes (`len(tasks)`) | yes |
| "**Three** routes are permanent routing regression fixtures" (line 399) | No — literal | yes (3) |
| "zero of the **30** Waves A+B modules" (line 312) | No — literal | see below |
| "CC-SPEC-1…10", "CC-IMPACT-1…7" (lines 306–307) | No — literal | yes (10 and 7) |
| "9 fixtures" (line 502) | No — literal | yes |

On the "zero" claim: sweeping all 30 modules for `facet` (case-insensitive) returns **3 occurrences in 2 modules** — RFC-0006 lines 401 and 564, RFC-0008/accounting line 236. All three are generic English ("a facet outside this tuple", "the least-protected load-bearing facet"), so the *substantive* claim — the shape-facet vocabulary is in no contract byte — holds, and matches E3 row 5. But the sentence as written is a measurement the generator never performs and would never re-check; if P-37 were ruled and the vocabulary drafted into RFC-0006, the router would keep asserting zero and `--check` would still pass. This is exactly the failure mode the repo's own rule names: *"A generator that quotes prose has re-opened the door it closed."*

The report is worse, because it is hand-written and already stale against the file it reports on:
- Report line 62 and line 92, and exercise line 66, all say **ten** owner decisions and list them **without P-42**. `TASK-ROUTER.md:119` names **eleven**, including P-42. A transcribed list already drifted.
- Report line 26 glosses RFC8-18 as "independent measures, never a composite", **dropping the word "Cost"** — an elision that converts a cost clause into a general anti-rollup clause and thereby conceals finding B.
- Report lines 44–47 transcribe the computed dependency line into a fenced block (correct today, will go stale silently).
- Report line 79 says the three new fixtures "each was run and observed to fail the check when applied" and then quotes the fixture *names*. The mutation each applies does fail; but the third name misdescribes what it tests (see A.1), so the reader is told a deferred-leak guard exists when it does not.

**Judgement.** The omissions are the *right* omissions and honestly framed in character. The file is not honest about its own computedness, and the report's transcriptions have already drifted.

## F. The six pass criteria.

**Method.** Judged the criteria as written against the materials the exercise actually hands the agent. I then found that the exercise **has been administered** since e2efda6 (untracked `CAPABILITY-1-SPEC-OUTLINE-EXERCISE-RAW.md`, administered 2026-08-11), which serves as an empirical test of my reading.

**Observation.** Criteria 5 and 6 are falsifiable and well-drawn; 6 has an explicit bright line. Criterion 2 is correctly identified as the sharp one and is the right thing to test. Problems:

- **Criterion 3 ("distinguishes shape from behavior") is unfalsifiable as written.** Neither "shape" nor "behavior" is defined for the agent or the grader, and no material given to the agent defines the distinction. It is graded to taste — the exact thing the file's own preamble says fixing criteria in advance prevents.
- **Criteria 2 and 4 carry no threshold.** "Identifies unresolved decisions" is satisfied by naming one. The bright line ("at least three … P-37, P-36, P-38") lives in the prose, not the criterion.
- **Criterion 5 measures citation form, never citation sufficiency**, and the materials list restricts the agent to "exactly the clauses and modules that route names". So an agent can only cite the route's 10 IDs, and passing criterion 5 is nearly automatic while the outline omits RFC6-13/14/15/18/19 entirely.
- **No criterion tests clause coverage.** Nothing in the six can detect the defect in section B.

**Could a bad outline pass all six? Yes — and one did.** The administered run graded **six of six pass**, and the route defect surfaced only because the agent *volunteered* it outside the rubric. The raw file records the agent's own words: *"RFC-0006 is in the route's computed dependency list but in none of its five Load paths … **This is the gap I would most want closed before authoring**"*, and separately that it "anchored its own heading H2 to a clause it had not read" (RFC3-16(a)). Both are the findings of section B, reached independently. The rubric scored the run a clean pass anyway.

**Could a good outline fail one?** Yes. An outline that correctly refuses to invent testable scenarios because no scope document was supplied fails criterion 4. An outline that names RFC6-18 as the authority it *needs* risks failing criterion 5 as citing an authority it was not given. And criterion 6's "any mention of a concrete stack … fails it outright, regardless of hedging" would literally fail an outline that says "this spec must not name a storage engine".

**Judgement.** Fixing criteria in advance was right, and criteria 2/5/6 are sound. But the set has a designed-in blind spot — it cannot detect an incomplete route — and the administered run demonstrates that blind spot empirically rather than hypothetically.

## G. What I would still be missing if handed this route and told to author.

Concretely:

1. **The capability's own scope.** The route's Load set is five RFC modules. It contains **no document that says what Capability 1 must do** — `FIRST-OPENSPEC-SEQUENCE.md` and its six behaviour rows are not routed, and the exercise's four materials do not include it either. I would be inferring rows 1.1–1.6 from a title.
2. **RFC-0006** — RFC6-13/14/15 (one truth two consumers; label parity; evaluation stamping), RFC6-17 (aggregation discloses), RFC6-18/19 (one fact set; drawer content classes), RFC6-26 (unconsented renders as policy). Three of my five loaded modules tell me the aggregation obligation is RFC6-17's and is deliberately not restated locally.
3. **`rfcs/RFC-0003/governance-homes-and-owner-acts.md`** for RFC3-16(a)/(b)/(c) — cited by all five loaded modules, and the honoring predicate for RFC3-7, which the route *does* name as directly governing.
4. **RFC3-1/3-5/3-9** — the semantic-contract framing, the closed field set, and the invalid-declaration-renders-Unknown rule. Row 1.1 is unspecifiable without them; the module is loaded but the route does not point at them.
5. **How to author at all** — `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`, `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1…10). The route mentions them in an omission string but does not route them; the *sibling* "Author or judge a specification" route loads all three.
6. **What "Waves A+B are unaccepted" means for every clause I cite.** Every module carries "Absent such a record, this contract binds nothing." The route says authoring is forbidden and names decisions, but never says the entire clause corpus is candidate, or that P-33 retires the Wave A confirmation under every arm.
7. **That P-28, P-21(a) and P-22 will be ratified or reverted inside the Wave A/B bytes I am citing** — my citations may not survive the acts.
8. **A resolution for `Unknown` vs `Gap`** (P-36) and **the facet vocabulary** (P-37) — these the route names correctly and honestly.

---

## Findings

**1. [BLOCKING] The Capability 1 route omits RFC-0006 entirely; the "honest shape visibility" half of the capability is unreachable.**
`TASK-ROUTER.md:115-117`; generator `build_task_router.py:271-295`.
Evidence: `FIRST-OPENSPEC-SEQUENCE.md:35-36` assigns rows 1.4/1.5 to `RFC6-18/19` and `RFC6-13/14/15`; `FIRST-SPEC-TRACE-TABLE.md:19-20` independently confirms. The route names none of them and does not load the module. `rfcs/RFC-0002/rendering-vocabularies.md:148`: *"An aggregate satisfying this sentence alone still violates RFC6-17. The obligation is cited here, not restated, so the two cannot drift."* RFC6-17 is cited by 3 of the 5 loaded modules and defined only in RFC-0006. The substitutes are cost-scoped: *"**RFC8-18.** Cost renders as independent measures, never a composite."*
Fix: add `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` to `modules`, and add `RFC6-13`, `RFC6-14`, `RFC6-17`, `RFC6-18`, `RFC6-19`, `RFC6-26` to `clauses`. Re-scope the RFC8-18/8-19 entry to cost, or drop it. Apply the reasoning the sibling Polaris route already states at `TASK-ROUTER.md:64`.

**2. [BLOCKING] RFC3-16(a) is the honoring predicate for a clause the route names, and its defining module is not loaded.**
`TASK-ROUTER.md:116`. RFC3-16(a) is defined at `rfcs/RFC-0003/governance-homes-and-owner-acts.md:158` (Wave A) and cited by **5 of 5** loaded modules, 30 citations. `rfcs/RFC-0003/manifests-and-namespace.md:595`: *"**RFC3-16(a)**, under which a consent record's stored attribution (RFC3-7) … are honored."* The route names RFC3-7 as directly governing while its predicate is undefined in the load set. Independently reported by the administered exercise.
Fix: add `rfcs/RFC-0003/governance-homes-and-owner-acts.md` to `modules` and `RFC3-16` to `clauses`.

**3. [MATERIAL] The selftest fixture "a deferred-wave module in the load set detected" tests nothing of the kind; no deferred-leak check exists.**
`build_task_router.py:497-501`. The case mutates `clauses`, expecting `"not defined in"` — the same predicate as the preceding case. Proven: injecting real RFC-0010/RFC-0011 modules into the Capability 1 `modules` list yields "9 fixtures, 0 failing" and "all routes validated", with the deferred modules rendered into the Load line.
Fix: add a real predicate in `validate()` — for any non-deferred route, error if a routed path matches `/rfcs/RFC-001[01]/` or if `module_deps` returns RFC-0010/RFC-0011 — and repoint the fixture at it.

**4. [MATERIAL] "each verified open in the pending queue" is false; the check tests row presence, not openness.**
`build_task_router.py:377-381` (check) and `428-432` (emitted claim) → `TASK-ROUTER.md:119`. Proven: P-6, P-7, P-13, P-26 — all `**Executed.**` — validate and render as "verified open".
Fix: scope the search to the "Open, and only the owner can dispose" section, or reject rows containing `**Executed.**`; add a fixture in the rejecting direction. Failing that, change the emitted words to "each has a row in the pending queue at generation time".

**5. [MATERIAL] The blocking-decision list omits P-1 (the two wave acts), P-28, P-21(a) and P-22, and over-includes P-34/P-35.**
`build_task_router.py:299-300` → `TASK-ROUTER.md:119`. `PENDING-OWNER-DECISIONS.md:140-146` assigns "plus the two wave acts themselves" to the authoring gate and P-34/P-35 to "the formal launch administration, **not the spec**"; lines 125-137 put P-28/P-21(a) on the Wave A act and P-22 on the Wave B act. The "acts are not decisions" defence fails because P-41 and P-42 are craft acts and are listed.
Fix: add P-1, P-28, P-21(a), P-22; move P-34/P-35 to a separately labelled downstream-gate line; correct the note "Every blocking owner decision is named below".

**6. [MATERIAL] The generated file asserts four counts while claiming "Counts computed, never asserted".**
`TASK-ROUTER.md:132` vs lines 13, 121, 122; generator lines 306-307, 312, 399, 502. "Three", "30", "zero", "CC-SPEC-1…10", "CC-IMPACT-1…7", and selftest `n = 9` are literals. All are true today; none is re-derived, so all drift silently. The `facet` sweep over the 30 modules returns 3 hits (RFC-0006:401, RFC-0006:564, RFC-0008/accounting:236) — all generic English, so the substance holds but the sentence is unverified.
Fix: compute the fixture count, the wave-module count, the CC ranges and the facet occurrence count in the generator; or move them to the budget report the banner says owns every measurement.

**7. [MATERIAL] The route names 12 of 18 fewer clauses than the project's own two Capability 1 artifacts.**
Beyond findings 1 and 2: RFC3-1, RFC3-5, RFC3-6, RFC3-9 and RFC1-3 sit in loaded modules but are not named, and RFC5-3's module is not loaded at all. Row 1.1 ("an invalid declaration is a named failure, never partial registration") maps to `rfcs/RFC-0003/manifests-and-namespace.md:250` — *"An unparseable or invalid `project.yaml` renders every dependent claim Unknown"* — which the route does not name.
Fix: reconcile `clauses` against `FIRST-OPENSPEC-SEQUENCE.md` rows 1.1–1.6 and E3, and add a `--check` predicate that fails when they diverge.

**8. [MATERIAL] Pass criterion 3 is unfalsifiable and no criterion tests clause coverage.**
`CAPABILITY-1-SPEC-OUTLINE-EXERCISE.md:57-64`. "Distinguishes shape from behavior" defines neither term for agent or grader. No criterion can detect findings 1, 2 or 7 — demonstrated by the administered run grading six of six while the agent separately flagged both defects outside the rubric.
Fix: define shape/behavior in the criterion; add a seventh criterion on clause sufficiency ("names any authority it needed and could not reach"); set thresholds on criteria 2 and 4.

**9. [MINOR] The report is stale and misquotes RFC8-18.**
`CAPABILITY-1-CONTEXT-ROUTE-REPORT.md:62, 92` and `CAPABILITY-1-SPEC-OUTLINE-EXERCISE.md:66` say **ten** decisions and omit P-42; the router names eleven. Report line 26 renders RFC8-18 as "independent measures, never a composite", dropping "Cost". Report line 49 calls a one-level `depends_on` union a "transitive closure".
Fix: regenerate the report's transcribed values or replace them with pointers; restore "Cost"; call the line what it is.

**10. [MINOR] The route does not tell an author the corpus is unaccepted, or route them to the authoring guide.**
`TASK-ROUTER.md:113-122`. The sibling route at line 94 loads `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`, `FIRST-OPENSPEC-SEQUENCE.md` and the CC-SPEC candidate; the Capability 1 route loads none of them, including the only document defining its own scope.
Fix: add those three to `modules`, and state in the note that every routed clause is candidate and binds nothing.

---

## What I could not test, and why

- **Whether the omitted clauses are the *only* ones missing.** My denominator for "needed" is the project's own two artifacts (18 clauses), not an independent derivation from all 344. A clause needed by Capability 1 that neither artifact names would not appear in my sweep. I state 12-of-18 as a measurement against those artifacts, not as a claim of exhaustiveness over 344.
- **Whether P-34/P-35 truly do not block authoring.** I relied on the queue's launch-scope index and `FIRST-OPENSPEC-SEQUENCE.md:71,73`. The index self-describes as "a reading aid, never authority", and authoring is arguably chain-blocked through the launch decision. I graded this as over-inclusion by the project's own partition, not as an error of fact.
- **The doctrine identifiers.** `validate` tests only that `VIS-2`/`VIS-4`/`VIS-5` appear as substrings in `vision.md`; I did not audit whether those three are the right doctrine rules for this capability, nor whether SEC-4 (consent) should be routed given rows 1.2's consent obligations. `RFC1-3` names SEC-4 explicitly, which suggests it should — I flag this as untested rather than as a finding.
- **The administered exercise result.** `CAPABILITY-1-SPEC-OUTLINE-EXERCISE-RAW.md` is **untracked and not part of the frozen subject at e2efda6**; at that commit the report's "has not been run / `[Unknown]`" is accurate. I used it only as corroboration of findings I had already reached independently, and I did not grade it. The caller should note the working tree now contradicts the frozen subject's status claim.
- **Concurrent writes.** Several untracked files appeared during my session from peer sessions. I verified `git status` and `git diff` show the two generator/router subject files unmodified at e2efda6; all mutation was done in a scratchpad copy.
