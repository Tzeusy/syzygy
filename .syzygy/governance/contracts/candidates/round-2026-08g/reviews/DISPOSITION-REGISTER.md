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
