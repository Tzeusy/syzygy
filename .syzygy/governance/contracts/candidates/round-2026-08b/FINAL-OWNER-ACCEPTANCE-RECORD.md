# Final owner acceptance record — contract-closure round, 2026-08-05b

> **This file offers. It does not accept.** No act below has been performed,
> and none may be performed by an agent. Where this file and
> `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` disagree, **that
> record wins** — it owns the exact phrases and the ceremony. This file
> exists to say what you would be accepting, what is knowingly imperfect
> inside it, and what to read first.
>
> Supersedes `../round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md`, which is
> banner-marked and whose act quotes are retired.
>
> ## SUPERSEDED — 2026-08-07
>
> **This file is superseded by
> `../round-2026-08c/FINAL-OWNER-ACCEPTANCE-PACKET.md`. Read that instead.**
> The five arguments below are still current and still verify; **what is out
> of date is the defect inventory.** §3's ten rows do not include the two
> open blocking contract defects the 2026-08-07 round found, two of its rows
> describe defects since fixed, and its "Read this first" is pinned two
> rounds back.
>
> **Review RD-8 found this, and named the consequence exactly:** the owner is
> routed here by `AGENTS.md` and by `PROJECT-STATUS.md`, and the second said
> this file carries the blocking defects before the act phrases. It does not
> carry them at all. *"This is the finding that converts act 1 from a knowing
> act into a surprised one."* The routing is corrected in both files; this
> banner exists for a reader who arrives with an old link.
>
> The two defects, so this file no longer omits them:
>
> 1. **Mission safety.** RFC10-17's `reserved + spent never exceeds
>    authorized` is stated over the ledger and nothing states it over
>    consumption, while **RFC10-10** says Mission Control MUST prevent every
>    mediated act from exceeding the envelope. Both cannot be true as
>    written. Two independent reviews over identical bytes, both `REVISE`.
> 2. **Deterministic context selection.** **RFC11-4** requires the phase-rule
>    clause of every selected contract; 6 of 353 clause rows carry that kind
>    and RFC-0001…0005 have none, so a conformant selector fail-closes on all
>    nine golden fixtures.
>
> Full statements, with every act's imperfections before its phrase:
> `../round-2026-08c/FINAL-OWNER-ACCEPTANCE-PACKET.md`.

## Read this first

**One thing changed that matters more than the rest.** A confirming review
was commissioned over the exact bytes act 1 binds — closing the gap every
earlier round left open — and it returned **REVISE**, not CONFIRM.

RC-10 found three defects that this round's own corrective work had
introduced: a live escape in RFC10-18, a clause written *this round* to close
an escape; twenty-one stale derived word counts inside act 1's digest set, in
the commit whose message said it had corrected every stale derived value; and
four misdescribed seams in the report asserting those seams were closed. All
three are fixed, each with a mechanical check behind it. **Those fixes have in
turn been read by no reviewer**, and one of them edits a contract inside act
1's digest set.

That is the round's principal residual, and it is now a smaller one of the
same kind rather than a different one. Everything else below is smaller
still.

## 1. The five acts, at their current arguments

Verify before acting — `python3 scripts/check_governance.py`, checks CG-7a
through CG-7d. A CG-7 failure means **do not perform that act**.

| Act | Argument (verify, never transcribe) | Changed this round? |
|---|---|---|
| 1 — foundational contracts | `2862b2f54e39e6d477129147eb2e1d0cb4ca714c26edabd75505e2e38ff057d7` | **Yes, five times** — most recently 2026-08-06 for the rev11b correction-plane repairs; **re-quoted a sixth time on 2026-08-06** for the RD-1 blocking repairs. This row previously said "superseded by the 2026-08-06 closure round's owner acceptance packet" — **a document that did not exist** (review RD-8, finding S6). The superseding offering now exists and is named in the banner above |
| 2 — craft amendment CC-TEST-2 | `7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0` | **Yes — and this row was wrong.** It offered `3858820f…` — an argument retired on 2026-08-06 when `th-engineering` was vendored and `testing-and-verification.md` gained CC-TEST-7. The acceptance record was re-quoted then; this copy was not, and **no check examined it**: CG-7c reads the acceptance record's `CC-TEST-2@…` form, and a bare digest in a table row matched neither CG-7c, CG-7d nor CG-15. Found by review RD-6 (finding H-1) and closed by **CG-7e**, which enumerates every file carrying an act-argument copy and the acts each one carries |
| 3 — topology bundle | `7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45` | No |
| 4 — project overview | `01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1` | No |
| 5 — doctrine amendment D3 *(optional)* | `e973e8e025c93b5d1e59d16d8661b0ae1f9804304c8f8de8957950acf3d8f9c9` | **Yes** — §6 disclosure added |

**Act ordering.** Perform act 1 before act 5, and see P-24 first: act 5 may
be a *requirement* to sequence after act 1 rather than a recommendation,
depending on how you rule D4.

## 2. What act 1 now covers that it did not before

**A correction plane for Mission Control (RFC10-17…RFC10-22).** Adversarial
review RC-7 found the contract had a prevention plane and no correction
plane: thorough about stopping an agent acquiring authority it was not
granted, nearly silent about what happens after something goes wrong inside a
grant that was legitimate. Nine of its eleven blocking seams are addressed by
clause text — budget reservation at dispatch, completion adjudication by
someone other than the executing party, effect reversibility and recovery
ownership, stop guarantees over in-flight work, cross-project consent
selection, and attention-queue bounds. Seven of those nine close fully; two
close partly, and the closure report names the part each leaves open rather
than rounding it up. Details, and the two seams *not* addressed by text at
all: `MISSION-SAFETY-CLOSURE-REPORT.md`.

**A dependency graph whose two halves can no longer disagree.** `provides_to`
was removed from all 32 modules and is now derived by reversing `depends_on`,
so the asymmetry class that had sat at 20 edges under a green drift check is
unrepresentable rather than merely absent. Seven edges were added on citation
evidence; three were dropped as unsupported.

**Four of those additions were then wrong, and were reverted.** Review RC-4
showed the evidence test was too weak — it counted the boilerplate status
banner and the shape-parallel parenthetical as reliances. The reverts are
recorded in `DEPENDENCY-CLOSURE-REPORT.md` §"Correction after RC-4" rather
than quietly applied, because the mistake is the more useful record.

**One wrong value in a closed vocabulary.** `missing-declaration` was cited
as RFC2-24 #4 where #4 is `stale-beyond-currency-bound` — in a vocabulary
RFC6-14 requires emitted verbatim, and one you ruled on directly. Corrected,
and every `RFC2-24 #N` ordinal that any sweep finds inside the 32 contract
modules agrees with the table.

**The counts that used to sit in this paragraph are withdrawn, 2026-08-06.**
It read "the 13 ordinal citations inside the 32 contract modules … as do the
20 across all candidate material." Review RC-10 flagged 13 as unreproducible;
the repair kept it and attached a *narrower* scope to it, plus a second figure.
Review RC-11 then swept both populations by two methods and got 15/16 and 28;
a third sweep in the following session got 17/14 and 31/21. **No definition of
"an ordinal citation" yet proposed yields a stable number** — the count moves
with how much text may sit between `RFC2-24` and `#N`, and with whether the
round's own reports are inside the population. What is stable, and is the
claim that matters, is the property: **no ordinal disagrees with the table**,
under every sweep run so far. The count is [Unknown] and is stated as Unknown
rather than picked. A figure a reviewer has called unreproducible is not
repaired by giving it a more specific scope.

## 3. What is knowingly imperfect inside the acts

| # | Inside act | What is wrong with it |
|---|---|---|
| 1 | act 1 | **The confirming review returned REVISE, and its own repairs are unreviewed.** See "Read this first" |
| 2 | act 1 | RFC-0001 is 8,342 words against a 7,000 ceiling — justified as a dictionary-shaped kernel contract, not fixed |
| 3 | act 1 | The corpus is 100,862 words against a 35–50k target band (recompute with `verify_final_prespec.py`; the figure moves whenever a module does). Nine compaction passes each hit a floor at −12…−22%. What was optimized instead is the per-task load |
| 4 | act 1 | ~~Two one-way constraint relations (RFC-0006→RFC-0005, RFC8-9/RFC7-24)~~ — **both edges were wrong** (review **RD-4**). One rested on §5 Integration prose fifty lines past the last clause; the other was misdirected onto a pair `depends_on` already bound. Both removed; the two clause-borne edges RD-4 found undeclared are declared with a `constrains_source` anchor and a check. **Still open:** RFC11-4 does not name `constrains`, so no conformant selector reads it, and review **RD-8** (S8) shows both declared lists are **under-inclusive against their own source clause** — RFC7-3 constrains every contract and names four — **P-21** |
| 5 | act 1 | RFC9-8(a) and RFC3-10/11/21 disagree about which plane an owner-gated registry belongs to. The corpus contains both the error and RFC10-15's remedy — **P-22** |
| 6 | act 1 | ~~RFC9-32 cites `RFC 0008 §5` — a navigational section — as authority~~ **CLOSED** in the fourth re-quote; the string has zero hits in `rfcs/` and RFC9-32 now cites RFC1-22 and RFC9-31. Review **RD-8**, finding S5 |
| 7 | act 5 | The D3 `vision.md` insertion settles open question **D4** by stipulation. Now disclosed at D3 §6 with a reviewer alternative; neither is adopted — **P-24** |
| 8 | act 5 | The `architecture.md` floor as drafted omits any maximum autonomy level, moving "how autonomous may a mission be" permanently out of doctrine |
| 9 | act 1 | RFC10-20 stops runs and their descendants, but **not child missions**; RFC10-19 does not state the failed-run / completed-sibling relationship. Both are RC-10 findings left open by text, not closed |
| 10 | act 1 | ~~The RFC10-18 repair RC-10 prompted has been read by no reviewer~~ — **superseded.** Three reviews have since read those bytes: RD-1 (`REVISE`, three blocking findings, all repaired) and two independent RD-1b reviews over the repaired digest, **both `REVISE`**. The current open findings are the two in the banner above and the full list in `../round-2026-08c/MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md` |

## 4. What this round did *not* do, and cannot

**There is no mechanical task → context-packet compiler, and this phase
cannot build one.** `scripts/context_load.py` resolves a *given* list of
paths and counts words. It does not select. Every context fixture's selection
was authored by hand and then measured; the selection trace in each fixture
is a record of reasoning, not of a computation. Building the selector would
be application code, which this phase forbids. So the packets are governed
and budgeted but not yet *compiled*, and the honest form of that claim is in
`FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md`.

The fixtures now at least go stale loudly: CG-18 recomputes each one's digest
and word count from its declared mandatory set. It found all eight stale on
first run — one by 1,738 words. A ninth was added on 2026-08-06 for the
evidence-adapter class, which had none; it is outside act 1's digest set, so it
changes no act argument.

## 5. Evidence you can reproduce

```sh
python3 scripts/check_governance.py                    # denominators printed per check
python3 scripts/check_governance.py --selftest         # fixture results; CG-24 prints the coverage
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py
python3 .syzygy/governance/contracts/candidates/scripts/build_contract_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_dependency_index.py --check
```

Read a check's **output**, not its exit code. `--selftest` exists because
this repository has shipped a validator that could not fail: the dependency
index reported 20 asymmetric edges at every generation while its drift check
reported clean, because regenerating a knowingly-broken graph reproduces the
same knowingly-broken file.

## 6. After the acts

Act 1 installs the 32 modules to `.syzygy/governance/contracts/rfcs/` and
creates `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`, which does
not exist yet — its absence is the correct current state. Whether the acts
*should* be performed now is answered, with its reasoning, in
`FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`; the short form is that act 1 is
the one whose residual is live, and the other four are not waiting on it. The ceremony is
`../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §2, five steps, per
act. Nothing here is self-executing.
