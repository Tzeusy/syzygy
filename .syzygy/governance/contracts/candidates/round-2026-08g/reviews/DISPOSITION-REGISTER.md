# Round-2026-08g — disposition register

> **The repair account, kept separate from the reviewer's bytes.** Raw review
> output lives beside this file and is never edited. Every finding is
> dispositioned `repaired` · `open` · `declined` — never "acknowledged", and
> **nothing is dismissed by omission**: if a review raised twelve findings,
> twelve rows appear below.
>
> **A repair session cannot confirm its own repairs.** Everything marked
> `repaired` here is repaired *in this session's judgement* and is not
> confirmed. Confirmation requires a fresh review of the repaired bytes.

## RD-55 — launch-gate policy semantics at v2.1

`VERDICT: REVISE` — one finding marked BLOCKING. Dispatched 2026-08-13
against frozen commit `939363f`; fresh context; same model family as the
corpus authors, so it supports repair and is not the formal launch
administration. Raw bytes: `RD-55-launch-policy-v2.1-RAW.md`.

The review's first answer was the one it was commissioned for, and it is
worth recording before the defects: over eight populations and a 25-record
differential battery against the v2.0 validator, **nothing was weakened** —
no question, verdict word, trend column or conjunct dropped, renamed or made
unreachable, and no record that fails under v2.0 and passes under v2.1.

| # | Finding | Disposition |
|---|---|---|
| **1** | *BLOCKING* — §4's eligibility clause states four limbs; the tool implements three, and the fourth lives at one consumer. An invalid record deposits `READY FOR …` in the §6 trend log and the report's last line | **repaired.** Independently confirmed by RD-56 f1, which built the same attack without seeing this review. Eligibility now owns five limbs (the fifth is RD-56 f7's), is computed last so it can count errors, and the CLI's private `and not errors` is deleted. Fixtures per limb, each verified to fail without its repair |
| **2** | *MATERIAL* — §5 took back the check enumeration in the same pass that added `LA-3b`, which the enumeration does not name. `LA-3b` occurs 0 times in the instrument | **repaired.** §5 names `LA-3b` and two further predicates the list had not covered |
| **3** | *MATERIAL* — the v2.1 delta asserts preamble byte-identity, which is false, and its published script structurally cannot check it | **repaired in the v2.2 delta, not in the reviewed file.** The v2.1 delta is frozen — this review is bound to it. The correction and the preamble-inclusive script are in the v2.2 delta's corrections section |
| **4** | *MATERIAL* — the `LG-6/LG-7` half of RD-48 f1 is not repaired, and three documents say it is | **repaired.** The citation is now `(LA-12)`; the note states what v2.1 actually did. Verified: v2.1 annotated the sentence in the past tense and left the literal standing |
| **5** | *MINOR* — D-8's "equivalent-or-stronger" argument does not cover the gate-verdict half | **repaired in the v2.2 delta.** The reviewer is right that prose replaced prose there. The not-restoring decision stands; its stated reason was too broad and is narrowed |
| **6** | *MINOR* — §4's new closed-set clause is unenforced and unenforceable as written | **repaired.** Narrowed to what the schema's closure does enforce: a record carries no verdict *field*. Forbidding a reviewer from quoting a verdict word was never the rule |
| **7** | *MINOR* — §4 names `stale` as an ineligibility ground that nothing defines and nothing computes | **repaired.** Deleted; the five limbs are the list |
| **8** | *MINOR* — the fourth gate result has three spellings and no instrument definition | **repaired.** `NONE`, defined in §4, used by every surface |
| **9** | *MINOR* — the packet routes an administrator to a register with no RD-47/RD-48 rows | **repaired.** The packet's §9 now names the deltas as the repair accounts and this register for dispositions, and carries the four-review table |
| **10** | *MINOR* — D-7's "stated nowhere else" is a claim of absence the same file contradicts | **repaired in the v2.2 delta.** Scoped to "no artifact that must stay current" |

**Repaired: 10. Open: 0. Declined: 0.** All repairs are this session's
judgement and none is confirmed.

## RD-56 — launch-gate schema, validator and renderer at v2.1

`VERDICT: REVISE` — two findings marked BLOCKING. Dispatched 2026-08-13
against the same frozen commit `939363f`, **after RD-55 returned and with no
knowledge of its findings**; fresh context; same model family. Raw bytes:
`RD-56-launch-machinery-v2.1-RAW.md`.

Seven of RD-47's twelve findings were reproduced and found cleanly closed.

| # | Finding | Disposition |
|---|---|---|
| **1** | *BLOCKING* — eligibility omits §4's fourth limb; an invalid record deposits `READY FOR …` in the trend log and the report's last line | **repaired.** The same defect as RD-55 f1, found independently. See that row |
| **2** | *BLOCKING* — RD-47 f2's forgery reproduces verbatim through any of 19 unblockquoted free-text sites; the guard covered 2 of 21 | **repaired.** `_inline` at every inline site, `_quoted` at every block one; eight fixtures, one per structural shape, each failing with `_inline` reverted to identity. The v2.1 delta had described a two-field fix as a class property |
| **3** | *MATERIAL* — `--schema` is unauthenticated, so `LA-1` can be turned off wholesale; and the closure audit is vacuous on a schema declaring no `properties` | **repaired.** A non-committed schema is an `LA-1` error and therefore ineligible; a schema with no root `properties` is refused. Two fixtures |
| **4** | *MATERIAL* — the RD-47 f1 repair has no discriminating fixture, and the fixture naming it **passes against the unrepaired v2.0 validator** | **repaired.** Replaced by a fixture that mutates the *instrument* in a scratch git repository, with an expectation naming the unreadable wording rather than the bare parameter name — the mismatch branch emits that too, which is how the old one passed for the wrong reason. Verified to fail with either limb reverted |
| **5** | *MATERIAL* — three decisions-home files that record no owner ruling still grant a deferral, one of them the class §4 names explicitly; and two refusal messages state the wrong reason | **repaired mechanically; the underlying question is open.** Warrants are now classified by shape — logs and indexes, packet/draft name patterns, and any document declaring its own status unresolved — and each refusal names its actual reason. **What constitutes an owner warrant is not defined by any adopted convention**, and a repair session may not invent one: recorded as a disclosed limit and a question for the owner queue |
| **6** | *MATERIAL* — the §6 new-findings column can be laundered to `0` against a file outside the repository | **repaired.** The prior-record path must resolve inside the repository; otherwise `LA-15` errors. Fixture |
| **7** | *MATERIAL* — with git unavailable a wholly forged record validates clean, eligibility does not consider it, and the report carries no trace | **repaired in both halves.** Git-unavailability is the fifth eligibility limb, and the note is stamped into the report body. Two fixtures |
| **8** | *MINOR* — `LA-3b` is a check the tool runs that §5 does not name; and the `READY-WITH-DEFERRALS` branch never consults whether the citation resolved | **repaired in both halves.** §5 names `LA-3b`; the branch requires a resolving F2 citation, with `LA-12` saying so when it does not |
| **9** | *MINOR* — RD-47 f9 stands unrepaired verbatim, and the delta's replacement figure is stale in the commit that changed it | **repaired.** The docstring names all six prose-reading sites, beside the population it counts |
| **10** | *MINOR* — `--allow-invalid` crashes on a record with a schema error, and the v2.1 duplicate-key repair introduced a second traceback class | **repaired.** An unrenderable record gets a short report naming why, with no verdict, figures or trend row. Three fixtures |
| **11** | *MINOR* — `question_digest` in its sha256 form binds nothing | **open, deliberately.** Closing it means removing the alternative from the schema, which moves the schema digest the formal packet seals. The schema has been byte-stable across three instrument versions and the `instrument-bound` form is covered by `LA-2`. Recorded as disclosed limit 6 rather than repaired quietly |
| **12** | *MINOR* — newline-bearing scalars split the §6 row and the report's verdict line | **repaired.** Every trend cell is sanitized, not only the verdict. Fixture |
| **13** | *MINOR* — the placeholder lexicon is defeated by a zero-width space, and `counterexample` accepts whitespace | **repaired in the first half; second half open.** Invisible characters are stripped before tokenizing, with two fixtures. `counterexample: " "` remains accepted and is disclosed as limit 7 |

**Repaired: 11. Open: 2 (f11, f13's second half). Declined: 0.**
Both BLOCKING findings are repaired, **in this session's judgement and
unconfirmed**.

### The convergence, recorded as evidence

RD-55 and RD-56 were dispatched separately, in fresh context, and neither
saw the other's output. **Both found the eligibility defect, both built the
attack, and both identified the trend log and the report's last line as the
artifacts that carry it.** A defect two independent readings land on is not
a matter of taste, and the sequencing — RD-56 dispatched after RD-55
returned, against identical bytes, without its findings — is what makes the
agreement worth anything.

### The pattern both reviews name

Neither review's central complaint is that a repair was wrong. It is that
**the claim made for a repair outran the repair**: free text was fixed at two
fields and described as a class property; the schema audit was fixed against
keyword deletion and described as closure; the deferral warrant was fixed to
a three-name list and described as "a made owner decision"; eligibility was
fixed at three limbs and described as four. Every one of those descriptions
was written by the session that made the repair, in the same pass, and each
was refuted by reading the code it described.

## RD-54 — P-33 decision packet and install-shape analysis

`VERDICT: REVISE` — two findings marked BLOCKING. Dispatched 2026-08-13
against frozen commit `a47635b`; same model family as the corpus authors, so
it supports repair and is not the formal launch administration.

| # | Finding | Disposition |
|---|---|---|
| **1** | *BLOCKING* — the typed layout is **not** achieved under the recommended option, which was the packet's whole reason for departing from the owner's steer. A wave act does not retire the candidate home, so after the act `contracts/` holds `candidates/` **and** `rfcs/` | **repaired.** Verified independently — the acceptance record states retirement of the candidate home is "a separate" matter, and `contracts/` holds `candidates/` today. Both purity rows are corrected to say no option achieves purity; the packet now states that **the ceremony did not create this breach and cannot cure it**; option **(M+)** is added, with its cost honestly `[Unknown]` rather than guessed |
| **2** | *BLOCKING* — the confirmation-retirement rule is unsound in the direction the packet relied on: the manifest is not "19 rows and nothing else", and its header names the acceptance phrase | **repaired.** Verified: the argument recomputes from the whole file (`8972d963…`); stripping the comment lines yields `6ccf5380…`, which no act names. The four header lines are now quoted in both files, the rule is restated with its proviso, and **the false form was swept across the corpus** — see below |
| **3** | *MATERIAL* — Strategy T's clone-visibility row is false: `.syzygy/cache/` is gitignored, so generated reports would vanish from every clone | **repaired.** Row corrected in the analysis; the axis `C'` caveat now carries both objections — the RFC3-20 "only home of any fact" bar *and* clone absence |
| **4** | *MATERIAL* — the reference count is low by one and the method was silently scoped to backticks | **repaired.** Re-swept over raw text: **88** references (45 A / 33 B / 10 deferred), 87 in code spans, **1 bare-prose**, in a Wave A module. The method's scope is now stated in the analysis, and the finding that a code-span-scoped *rewrite* would miss the same reference is recorded — that is the sharper half of this finding |
| **5** | *MATERIAL* — the reader cannot locate the owner instruction the recommendation departs from; it exists only in an untracked root file | **open.** The instruction is an owner charter that is deliberately never committed. Recording it in a tracked governance artifact is a real fix and a real decision — what gets extracted, and under whose authority — and it is not this round's to make unilaterally. The packet's departure paragraph stands, and its unciteable premise is now this row |
| **6** | *MATERIAL* — the packet's (T) is axis E alone, but it carried a cost caveat that only the analysis's fuller T generates | **repaired.** The history-home amendment caveat is removed from the packet's (T); (T) is now stated as "(M) plus the rewrite", which is what its cost block prices |
| **7** | *MATERIAL* — measurements in the packet carry no epistemic labels, and one model reading is fused into a sweep result | **repaired.** Every figure in all three cost blocks is now labelled. The link-obligation sentence is split into `[Observed]` 9 hits across 6 of 39 modules and `[Inferred]` the reading of what they govern |
| **8** | *MATERIAL* — (M) removes the installed tree's integrity artifact and breaks ceremony step 3's verification command, and neither cost block said so | **repaired.** (M)'s block gains an "in-tree integrity artifact: none" row, and the ceremony-step consequence is stated beside it |
| **9** | *MINOR* — "up to 30 modules" understates a certainty | **repaired.** Stated as "all 30", with the measurement: 19 of 19 and 11 of 11 carry at least one such reference |
| **10** | *MINOR* — the `records/` home is not rejected with a rule, though the owner instruction names it | **open.** Correct, and cheap, but it belongs with the axis-B rewrite that finding 5's resolution will touch. Batched rather than edited twice |
| **11** | *MINOR* — only candidate contracts are swept; doctrine binds and was not checked | **repaired.** The packet now carries the `[Observed]` statement that VIS-7's link rule is scoped to rendered internal *project-entity* links and does not reach a file path in module prose |
| **12** | *MINOR* — both files elide the `contracts/` cell's third column, which is the strongest text against their typing | **open.** The elision is real. The reviewer's own reading — that it is a statement about gate authority, not residence — is the one this session would write, and a repair session restating a reviewer's argument as its own analysis is worth little. Batched with finding 5 |

**Repaired: 8. Open: 4. Declined: 0.**

None of the four open findings is blocking. Both BLOCKING findings are
repaired, **in this session's judgement and unconfirmed**.

## The correction sweep for finding 2

The false claim — *"the argument is the manifest's module rows, so a
ceremony-only change retires no confirmation"* — had propagated before RD-54
caught it. Corrected in the same pass, per the repository's own rule that
correcting a false claim means sweeping its restatements with a denominator.

```text
denominator          378 tracked .md files
method               Python re over ten phrasings of the claim
non-frozen sites     5, all corrected
frozen review lane   RD-49's quotation of the earlier false claim, left as is
```

| Site | State |
|---|---|
| `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md` | corrected — header quoted, proviso stated |
| `round-2026-08g/P33-SEMANTIC-INSTALL-ANALYSIS.md` | corrected — same |
| `PROCESS-GLOSSARY.md` | corrected — the `argument` entry |
| `decisions/PROCESS-LESSONS.md` | corrected — the lesson, plus a note that its unconditional form was written and falsified on the same day |
| `round-2026-08f/FINAL-CAPABILITY-1-READINESS-REPORT.md` | corrected — proviso added to the narrative |

**This is not a claim that no sixth site exists.** It is a claim about ten
phrasings over 378 files. A restatement using none of those ten words would
not have been found.

### Why this one is worth recording as an incident

The unconditional rule was written into `PROCESS-LESSONS.md` **on 2026-08-13**,
as a lesson learned, and was falsified the same day by a reviewer who did the
one thing nobody repeating the claim had done: **read the manifest's first
four lines.** The claim had by then been restated in five places and used to
justify a recommendation. A summary of an artifact is not the artifact.

## RD-51 — specification acceptance and shape-to-spec impact

`VERDICT: REVISE` — four findings marked **blocking**. Dispatched
2026-08-11 against frozen commit `e2efda6`; fresh context; same model family
as the corpus authors. Raw bytes are in the **previous round**:
`../../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`.

**Why the disposition is here and not there.** The round-08f register says
of this review: *"The full finding set is in the raw file; none is repaired.
The specification-acceptance policy's bytes are meant to be frozen after
P-40 is ruled and reviewed fresh at that point, so repairing them now would
freeze the wrong bytes."* That reasoning conflated **repair** with
**freeze**. Repairing a candidate does not freeze it; freezing is stopping,
and only the freeze had to wait on P-40. Owner charter §9 directed the
repair, and it is done here. The 08f register now points forward to this
section.

The repair account, clause by clause with before/after text, is
`../SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`.

| # | Finding | Disposition |
|---|---|---|
| **1** | *BLOCKING* — CC-IMPACT-6 weakens the owner-approved CC-REV-2 by side-clause, in the population CC-REV-2 names first, and its exception has no confirmer | **repaired.** The clause now creates no alternative; CC-REV-2 governs unmodified. The exception is offered instead as an amendment to CC-REV-2 itself (`policy-candidates/CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md`, queue row **P-44**), with a confirmer distinct from the change's author and a fifth element the old form lacked — the visible `contradicted`/`Unknown` interim state. **Two arms are offered, and declining is one of them** |
| **2** | *BLOCKING* — CC-SPEC-2's rationale asserts as owner rulings five decisions that are all pending, and describes a specification that does not exist | **repaired.** The sentence is withdrawn, not softened. Replaced with the true statement, plus a new operative rule: a **pending** decision is not a lawful warrant |
| **9** | *BLOCKING* — CC-IMPACT-2's sweep triggers are narrower than CC-SPEC-2's warrant sources, so a requirement can be warranted by an authority whose amendment reaches nothing | **repaired.** CC-IMPACT-2 no longer carries a second enumeration: *"the identities that can trigger a sweep are exactly the identities that can warrant a requirement."* Stated as a set identity precisely so the two cannot drift |
| **10** | *BLOCKING* — CC-IMPACT-1 declarations may diverge from CC-SPEC-2 warrants, defeating the sweep | **repaired.** The specification-level declaration is now **generated** as the union of its requirements' declarations; a narrower declaration is a defect and a hand-maintained second list is the duplicate authority CC-REV-3 forbids |
| **3** | *material* — CC-SPEC-1's operative text binds to the pending P-40 | **repaired.** The clause states the rule it proposes, quoted from P-40's packet, and states that its force is conditional and that it **may not be frozen before P-40 is ruled** |
| **4** | *material* — CC-SPEC-2's fifth warrant source names a record class that exists nowhere | **repaired.** The class is removed, per charter §9.1. The sweep was **re-run in the repairing session** rather than quoted from the review: 371 files and 784 files, two methods, hits confined to the clause's own discussion, this review, and one untracked file |
| **5** | *material* — the warrant list omits approved craft clauses and topology identities | **repaired.** Both added; the two policies now name one authority set |
| **6** | *material* — "exactly one" is ambiguous and supplies no tie-break | **repaired.** Replaced by charter §9.1's rule: all material warrants, one optionally marked primary, none hidden for being less specific |
| **7** | *material* — CC-SPEC-4 rejects prohibitions and admits unreachable conditions and tautological oracles | **repaired.** Five named forms; five obligations on every form, including the oracle's **effectiveness** and **independence**; four oracle forms rejected outright. For invariants and prohibitions the reachable case is the scope of quantification, a counterexample schema, and the sweep whose denominator bounds it |
| **8** | *material* — the fixture's golden ANSWER contradicts the fixture's own step 4 | **repaired by supersession.** Fixture 1 is banner-marked superseded and not administered; fixture 2 is new, and its answer key is a **separate file**, so blindness is structural |
| **11** | *material* — CC-IMPACT-3 mis-cites its sibling and asserts an absence without the sweep | **repaired.** The identifier is corrected, and the denominator discipline is cited to CC-KNOW-16 instead of claimed as a new home |
| **12** | *material* — CC-SPEC-10 drops VIS-4's always-human-gated class | **repaired.** Both dropped limbs are now quoted: the two conjoined preconditions, and the always-human-gated class |
| **13** | *material* — CC-IMPACT-7 has no pass criterion, no named actor, and no named fixture | **repaired in part.** Fixture named by path and sha256; administrator fresh-context per CC-REV-1; pass criterion owned by the answer key; consequence of failure stated. **Open:** the clause still does not say who *selects* the administrator |
| **15** | *material* — CC-SPEC-8's N/A judgement has no independent confirmer, and its home is circular | **repaired in part.** The confirmer is added on the CC-TEST-4 pattern. **Open:** "applicable" is undefined, and the reviewed-N/A rule's identifier is still unresolved — the routing matrix routes the deliverable back to CC-SPEC-8, so each names the other as owner |
| **20** | *material* — CC-IMPACT-3 permits a wrong "explicitly unaffected" and bounds nothing | **repaired.** The `explicitly unaffected` set now requires the **method**, not only the reason, and what a method cannot decide routes to `undecidable` rather than to `explicitly unaffected` |
| **16** | *minor* — CC-SPEC-1 mandates one capability; CC-IMPACT-1 contemplates several | **repaired.** CC-IMPACT-1 is singular |
| **17** | *minor* — CC-SPEC-9 duplicates CC-REV-4 and VIS-3 | **repaired.** Reduced to a citation, which is what CC-REV-3 requires |
| **18** | *minor* — three amendment warrants cite a document absent from the frozen bytes | **repaired.** Every amendment note in both files now cites the tracked semantic delta and an RD-51 finding number. The charter itself remains untracked and is not the citation |
| **19** | *minor* — neither candidate carries epistemic labels | **repaired in part.** The substantive claims in the amendment notes and rationale carry labels; the "why each rule is here" table does not |
| **14** | *material* | **open, and deliberately.** No clause tests a specification for **completeness against its capability**, so launch-gate E5's "complete" limb is unclosed — 0 of 10 clauses ask whether the requirement set covers the capability it claims. The fix is a new clause, and charter §9 does not direct one; minting an unrequested clause enlarges what the owner must approve at P-41. Recorded on the policy's own surface as well as here, because a candidate that hides its own open findings is the failure VIS-2 names |

**Repaired: 15. Repaired in part: 4 (f13, f15, f19, and f7's sibling
concern about undefined vocabulary consumption). Open: 1. Declined: 0.**

`[Unknown]` — **none of this is confirmed.** These repairs were made by the
session that read the verdict, which is the weakest possible evidence about
their correctness, and the same pattern has already cost this round two
rounds of `REVISE` on the launch gate. Charter §9.8 sequences one combined
fresh-context review **after P-40 is ruled**; P-40 is not ruled, so the
review has not been dispatched and **the bytes are not frozen**.

## RD-59 — the blind propagation run, graded

The exercise CC-IMPACT-7 requires has been **run**, not just specified. A
path that has never been run is a plan, not a process — the clause's own
sentence. Raw bytes: `RD-59-blind-propagation-RAW.md`. Subject:
`../SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` at sha256
`685a71f7…272ed4e0`, the digest CC-IMPACT-7 names. The administrator was
given that one file and forbidden everything else, including repository-wide
search; their confirmation section names the single file they opened.

**Result: PASS**, against the answer key's three criteria.

| Criterion | Outcome |
|---|---|
| the derived `affected` set contains all six golden affected requirements | **met** — FAC-1, FAC-2, STA-1, REG-4, COST-1, COST-2 all present |
| FAC-3 is never filed `explicitly unaffected` | **met** — filed `affected` |
| population stated, all sixteen placed, sets sum | **met** — 16 stated and derived independently; 7 + 8 + 1 = 16 |

**What the run demonstrates.** The sweep found **4 of its 6** affected
requirements through `policies[]` and `decisions[]`, not through
`contracts[]`. A sweep matching contract clause IDs — the shape of every
sweep the unrepaired CC-IMPACT-2 could have required — would have returned
FAC-1 and FAC-2 and stopped, a 67 % miss. That is RD-51 f9's
warranted-but-unsweepable class, measured rather than argued.

It also reproduced, unprompted, the two reasonings the answer key treats as
the discriminating ones: FAC-4's **invariance argument** (a parity
obligation quantifies over the relation, not over what is computed, so it
survives a change to the computation), and the routing of a case its method
could not settle to `undecidable` rather than to `explicitly unaffected`.

### Two divergences from the golden, and one is the fixture's fault

| Divergence | Judgement |
|---|---|
| **FAC-3 filed `affected`, golden `undecidable`** | **the golden's stated reason is wrong, and the run is right.** The answer key says the sweep "cannot settle it without a contract reading it does not own" — but the fixture's own authority table hands the administrator `RFC6-18`'s content, *"whose facets are those the folding rules produce"*, which settles it in one hop. The fixture supplied the fact its answer key says is unavailable. The pass criterion admits both placements, which is why the run still passes; the criterion was written that way as a hedge, and the hedge is what saved it |
| **COST-3 filed `undecidable`, golden `explicitly unaffected`** | **defensible, and unanticipated.** The administrator's argument — that `CC-TEST-6`'s coverage obligation over "the absence branch" may or may not acquire a new branch when `CC-PROV-5` gains an aggregate-disclosure limb, and that branch granularity is not a fact the fixture states — is sound. The answer key listed FAC-4 and STA-3 as tolerable divergences and did not anticipate this one |

### Two defects the run found in the fixture

`[Observed]`, both verified against the fixture's bytes after the run:

1. **The fixture says the declaration has "six fields" and no requirement
   carries `topology[]`** — `grep -c topology` over the fixture returns
   **0**. One of the six warrant classes is entirely unexercised, and the
   administrator could not even see *which* field was missing, correctly
   noting that "if it can carry a reference, my declaration sweep is
   incomplete by exactly that field."
2. **The fixture asks for a CC-IMPACT-2 sweep and CC-IMPACT-3 output
   without stating either clause.** The administrator worked from the
   four-set block printed in the task, which was sufficient, and said so.

**Neither is repaired, and repairing them is forbidden.** CC-IMPACT-7 binds
this fixture by digest and this run is bound to those bytes; editing it now
would make the run worth nothing, which is verification rule 10. The fixture
is **superseded by a fixture 3, never edited** — filed as work, not fixed
here. Until then CC-IMPACT-7 continues to name fixture 2, and this record is
what a reader needs to know its limits.

`[Inferred]` — that the path works. One passing run against one fixture
built by the session that wrote the clause it exercises is weak evidence, and
the administrator shares the corpus authors' model family. It is more than
existed before, which was nothing.

## RD-60 — the Capability 1 outline exercise, against the generated route

Owner charter §10's closing exercise, run and recorded. Raw bytes:
`RD-60-capability-1-outline-exercise-RAW.md`. **Not a review** — no artifact
was judged, no verdict word is claimed, and nothing below copies one. Subject:
`CAPABILITY-1-CHARTER.yaml` at sha256 `15e92acb…de64ad107` and the two views
generated from it. Materials withheld: every review, every register, the
status file, the README, the sequence document, and the pending-decisions
queue. Rulings available to it: **none** — every decision in its materials is
open and no spec-quality policy is in force.

**It produced a full outline** — the capability in one sentence, a shape/
behaviour split of 29 fixed items against 12 open ones with four cases argued
onto the boundary, 22 proposed requirements across the six rows each carrying
a form, a reachable case, a terminating oracle, a falsifier and a clause
citation, and a ten-row table of the decisions it ran into. It created nothing, edited nothing, and created no
`openspec/`; its confirmation section enumerates the eleven files it opened
and the line ranges it read.

### What the exercise establishes about the generated-view architecture

Two things, and only these two:

1. **It could not mis-home an authority**, because the charter names clause
   IDs only and the builder resolves each home from the generated contract
   index. Every module the exercise opened, it opened because the route named
   it. The failure mode a hand-maintained route has — a plausible wrong path
   that no check tests — was not available to it.
2. **The charter carried no decoration.** Set-difference run this session over
   the exercise's argument section (its file list excluded, since clause IDs
   appear there as range endpoints, not citations): **34 clause IDs cited, all
   25 of the charter's then-current clauses among them, 0 uncited.** A charter
   clause the exercise had no use for would have been a citation that was not
   a reliance; there were none.

### The four clauses added because of it

`[Observed]`, each verified defined and homed in a Waves A+B module before
being added; the charter's own provenance comment records the same:

| Clause | Row | Why it is a reliance, not a citation | Found by |
|---|---|---|---|
| `RFC6-22` | 1.4 | `RFC6-17` requires disclosure of *"the full RFC6-22 equivalence tuple"* inside its own body — an author cannot satisfy `RFC6-17` without it | the exercise, by citing it as authority for R1.4-C while it was absent from the route |
| `RFC1-27` | 1.6 | `RFC7-40` says the link is proposed as *"a Proposal, RFC1-27"*; row 1.6's whole obligation is that Proposal | **the exercise, explicitly** — its "what I could not do" item 6 names `RFC1-27` as cited by two clauses, outside the range the route gave it, and leaves R1.6-C's artifact undefined in consequence |
| `RFC3-3` | 1.6 | direct-write containment — the contract-level statement of what row 1.6's *"never write it"* means; VIS-5 is the doctrine half and was already carried | the exercise, by citing it in R1.6-B's authority line while it was absent from the route |
| `RFC6-23` | 1.5 | `RFC6-18` gives row 1.5 *"one fact set"* and `RFC6-22` gives the comparison tuple, but only `RFC6-23` enumerates the twelve things two equivalent renderings may not disagree about, and makes the disagreement release-blocking. That enumeration **is** the parity oracle's domain | **this disposition session, not the exercise** — the exercise cited `RFC6-23` only as the consequence in R1.5-C's falsifier line. The reliance question was asked afterwards and answered differently. Recorded as this session's reading, and the owner may disagree with the reasoning rather than only the conclusion |

**The charter has moved, and the exercise is bound to the bytes before it
moved.** The banner on the raw file says so and names the pre-addition digest.
Verification rule 10 is not violated because nothing the exercise was bound to
was *edited* — the charter was extended afterwards, on the exercise's own
evidence, and the record states which digest the run read.

### Five clause IDs the exercise cited that were deliberately **not** added

`[Observed]` — each verified this session to appear **inside the body of a
clause the charter already carries**, so the obligation is the host clause's
and adding the inner ID would import a citation that is not a reliance:

| Inner ID | Host clause already in the charter | Verified |
|---|---|---|
| `RFC1-2` | `RFC3-6` | yes |
| `RFC2-18` | `RFC6-19` | yes |
| `RFC2-25` | `RFC6-14` | yes |
| `RFC7-6` | `RFC7-39` | yes |
| `RFC8-12` | `RFC6-19` | yes |

`RFC8-12` is the sharpest of the five: `RFC6-19` class 8 (ii) marks it *"a
forward reference, informative until RFC 0008 is accepted"*, so adding it
would have imported an unaccepted dependency into a capability the charter
claims depends on Waves A+B only. The exercise saw this and said so.

### Findings left open, and why

| # | Finding | Disposition |
|---|---|---|
| f1 | **"Never partial registration" is anchored to no clause.** Row 1.1's statement asserts atomicity; `RFC3-9` gives the consequence of invalidity and `RFC3-5` the closed field set, and neither states an all-or-nothing transition. The exercise proposed R1.1-A with its authority marked incomplete rather than attribute a sentence to a clause that does not contain it | **open.** Two lawful repairs exist — amend a contract to state it, or drop the phrase from the charter row — and both are decisions this session may not make. Amending a candidate contract clause enlarges the Wave A package the owner is being asked to accept; dropping the phrase weakens a row the charter's author put there deliberately. Filed as work, routed to the owner |
| f2 | **The "named failure" vocabulary does not exist.** Row 1.1 requires an invalid declaration to be "a named failure"; no clause defines a failure-identifier vocabulary. Either the specification mints one — structurally the same question `P-37` poses for the facet names — or a contract amendment does | **open**, and deliberately not minted. It is a decision about what a specification may own, which is the subject of an open queue row, not a gap a repair session fills |
| f3 | **`RFC3-1` delegates the `project.yaml` dialect** — version, coercion rules, duplicate-key handling — *"to the first accepted spec that parses it,"* and makes it a conformance item from then on. R1.1-A/B's parse-outcome oracle therefore has an undefined boundary | **declined as a defect; recorded as a fact.** This is the contract working: it is behaviour by delegation from shape, and the delegation is explicit. The exercise correctly named it and proposed no dialect. Nothing to repair |
| f4 | **Row 1.4 could be taken least far**, because the facet names are drafted in no accepted module (the route's own generation-time sweep: **0 of the 30** Waves A+B modules). Every row-1.4 requirement the exercise wrote is a frame with an empty domain | **already recorded, not a new finding.** The charter's `deferred_semantics` carries it and routes it to `P-37`, which is exactly what the exercise concluded independently. The convergence is the useful part |
| f5 | **R1.4-B has no expected value.** The merged-but-unreconciled rendering must render Unknown, `RFC6-14` requires reasons verbatim, and `RFC2-24` closes the vocabulary at twelve — none of which the flagship V0 case is bound to | **already recorded**, `deferred_semantics` → `P-31`. Same convergence |
| f6 | **It could not say what `P-36`, or any of the nine capability-level decisions, decides** — it had identifiers and no subject matter, because the queue was withheld | **declined as a defect of the exercise's brief, not of the route.** It reported the identifiers and stopped, which is the correct behaviour; it did not guess. Worth noting that the route names blocking decisions by ID and does not summarise them: a reader following the route reaches the queue, which owns the answer |
| f7 | **No spec-quality bar was in force**, so the form/oracle/falsifier shape the exercise used is its own construction, warranted by nothing in the repository — and it said so unprompted | **correct, and it is the state `P-41` exists to end.** Recorded so no later reader mistakes the outline's shape for a policy-derived one |

`[Inferred]` — that the generated-route architecture holds. One exercise, one
capability, one model family shared with the corpus authors. What it shows is
narrower than "the route works": it shows that a fresh reader given only the
generated route reached the same open decisions the charter already names, and
found four clause gaps by trying to write requirements and running out of
authority. That last part is the only thing here that could not have been got
by reading.
