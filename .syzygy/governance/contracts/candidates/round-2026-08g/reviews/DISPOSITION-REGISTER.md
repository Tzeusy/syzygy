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
