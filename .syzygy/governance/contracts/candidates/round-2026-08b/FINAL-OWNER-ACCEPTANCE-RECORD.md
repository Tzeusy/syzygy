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
| 1 — foundational contracts | `2922de1c21354ad3a804acebcfdf665d9a8986d4fa8b3df42c62169f207ed98d` | **Yes, three times** — most recently 2026-08-06, for RC-11's nine stale word counts in `RFC-0009/README.md` |
| 2 — craft amendment CC-TEST-2 | `3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d` | No |
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
| 4 | act 1 | Two one-way constraint relations (RFC-0006→RFC-0005, RFC8-9/RFC7-24) are stated in one contract, acknowledged by no clause in the other, enforced by neither — **P-21** |
| 5 | act 1 | RFC9-8(a) and RFC3-10/11/21 disagree about which plane an owner-gated registry belongs to. The corpus contains both the error and RFC10-15's remedy — **P-22** |
| 6 | act 1 | RFC9-32 cites `RFC 0008 §5` — a navigational section — as authority |
| 7 | act 5 | The D3 `vision.md` insertion settles open question **D4** by stipulation. Now disclosed at D3 §6 with a reviewer alternative; neither is adopted — **P-24** |
| 8 | act 5 | The `architecture.md` floor as drafted omits any maximum autonomy level, moving "how autonomous may a mission be" permanently out of doctrine |
| 9 | act 1 | RFC10-20 stops runs and their descendants, but **not child missions**; RFC10-19 does not state the failed-run / completed-sibling relationship. Both are RC-10 findings left open by text, not closed |
| 10 | act 1 | The RFC10-18 repair RC-10 prompted is inside act 1's digest set and **has been read by no reviewer** |

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
