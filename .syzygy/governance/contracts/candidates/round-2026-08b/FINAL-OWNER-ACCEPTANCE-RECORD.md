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

**One thing changed that matters more than the rest.** The contract corpus
moved twice on 2026-08-05b, and **no confirming review is bound to the bytes
you would be accepting.** The last CONFIRM (2026-08-03) named a manifest
digest that has since been superseded twice. Six new clauses (RFC10-17…22)
and a corrected dependency graph sit inside act 1's digest set, read by the
round's own reviewers but by no review bound to the final argument.

That is the round's principal residual. Everything else below is smaller.

## 1. The five acts, at their current arguments

Verify before acting — `python3 scripts/check_governance.py`, checks CG-7a
through CG-7d. A CG-7 failure means **do not perform that act**.

| Act | Argument (verify, never transcribe) | Changed this round? |
|---|---|---|
| 1 — foundational contracts | `718fe095192a415fe7300b039e887b4d286bbb3d06b45e0f823cfb1ce6d4724f` | **Yes, twice** |
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
grant that was legitimate. Nine of its eleven blocking seams are closed by
clause text — budget reservation at dispatch, completion adjudication by
someone other than the executing party, effect reversibility and recovery
ownership, stop guarantees over in-flight work, cross-project consent
selection, and attention-queue bounds. Details and the two seams that are
*not* closed by text: `MISSION-SAFETY-CLOSURE-REPORT.md`.

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
RFC6-14 requires emitted verbatim, and one you ruled on directly. Corrected;
all 13 ordinal citations now agree with the table.

## 3. What is knowingly imperfect inside the acts

| # | Inside act | What is wrong with it |
|---|---|---|
| 1 | act 1 | **No confirming review reaches the current bytes.** See "Read this first" |
| 2 | act 1 | RFC-0001 is 8,342 words against a 7,000 ceiling — justified as a dictionary-shaped kernel contract, not fixed |
| 3 | act 1 | The corpus is 100,673 words against a 35–50k target band. Nine compaction passes each hit a floor at −12…−22%. What was optimized instead is the per-task load |
| 4 | act 1 | Two one-way constraint relations (RFC-0006→RFC-0005, RFC8-9/RFC7-24) are stated in one contract, acknowledged by no clause in the other, enforced by neither — **P-21** |
| 5 | act 1 | RFC9-8(a) and RFC3-10/11/21 disagree about which plane an owner-gated registry belongs to. The corpus contains both the error and RFC10-15's remedy — **P-22** |
| 6 | act 1 | RFC9-32 cites `RFC 0008 §5` — a navigational section — as authority |
| 7 | act 5 | The D3 `vision.md` insertion settles open question **D4** by stipulation. Now disclosed at D3 §6 with a reviewer alternative; neither is adopted — **P-24** |
| 8 | act 5 | The `architecture.md` floor as drafted omits any maximum autonomy level, moving "how autonomous may a mission be" permanently out of doctrine |

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
first run — one by 1,738 words.

## 5. Evidence you can reproduce

```sh
python3 scripts/check_governance.py                    # 30 checks, denominators printed
python3 scripts/check_governance.py --selftest         # each check shown able to fail
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
not exist yet — its absence is the correct current state. The ceremony is
`../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §2, five steps, per
act. Nothing here is self-executing.
