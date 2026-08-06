# Is Syzygy ready to begin OpenSpec authoring?

> **Non-authoritative round record.** This file answers one question and shows
> its working. It accepts nothing, and it does not license the acts. The
> acceptance ceremony is `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`;
> what is being offered and what is wrong with it is
> `FINAL-OWNER-ACCEPTANCE-RECORD.md`. Supersedes
> `../round-2026-08/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`, which is
> banner-marked.

## The answer

**Not ready.** Two of the eight readiness criteria are unmet, and neither is
unmet for a reason more prose can fix.

This is a narrower "no" than the last round's. Six criteria are met, one of
the two failures is a *phase* boundary rather than a defect, and the corpus
now carries eleven mechanical checks that did not exist a round ago. But the
question asked for a state, not a trend, and the state is not ready.

## Criterion by criterion

| # | Criterion | State | Why |
|---|---|---|---|
| 1 | North star discoverable | **Met** | `README.md` → `intent/OVERVIEW.md` → `doctrine/vision.md`, three hops from the repository root, no founder context required. The root README routes an unfamiliar word to the one glossary at `doctrine/README.md:15` |
| 2 | Public vocabulary bounded | **Met as a boundary, unmet as a definition** | The two-tier split exists and `TERM-REGISTRY.md` draws it. But the registry is a candidate with no owner act, and **eight public terms have no adopted definition anywhere** — P-17. A reader can find out which words are public; for eight of them, finding out what they mean is not yet possible |
| 3 | Contract dependencies closed | **Met** | `provides_to` is derived by reversing `depends_on`, so the 20-edge asymmetry class is unrepresentable rather than merely absent. CG-13 examines 146 edges for dangling targets and checks the package-README-equals-module-union invariant every run |
| 4 | RFC / OpenSpec routing complete | **Met** | CG-17 examines 199 surface clauses and finds each routed exactly once across the four categories. The check catches routed-but-undeclared as well as declared-but-unrouted; it was hardened in this session after it missed the first direction |
| 5 | Context packets complete and **automatic** | **Complete as of 2026-08-06; still not automatic, and unmeetable in this phase** | The class map is now eight-for-eight (fixture 9). "Automatic" is the half that cannot be met here — see below |
| 6 | Mission-safety seams closed | **Partly** | Seven of RC-7's eleven blocking seams close fully by clause text, two partly, one is an owner ruling (P-24), one was a record correction. Three residual escapes are named in `MISSION-SAFETY-CLOSURE-REPORT.md` rather than rounded away |
| 7 | Acceptance record clone-executable | **Met** | `PUBLIC-CLONE-VERIFICATION-REPORT.md` recomputes all five act arguments inside a real clone at the offered commit, with `_bootstrap/` absent, and the clone's battery now matches the working tree's check for check. It did not one commit earlier: CG-14 answered from the local filesystem and read a `_bootstrap/`-dependent ceremony step as executable. Both the step and the check are fixed |
| 8 | The exact package passes a fresh semantic review | **Unmet** | See below |

## Criterion 5 — there is no compiler

`scripts/context_load.py` resolves a list of paths you hand it and counts
words. It does not select. Every context fixture's mandatory set was chosen by
hand and then measured, while each fixture's header says `Compiler:
context_load.py`.

This is not a gap that authoring more governance closes. A selector that maps
a task to a packet is application code, and application code is prohibited
until OpenSpec exists — which is the very thing this report is assessing
readiness *for*. So criterion 5 is unmet by construction, and it stays unmet
until the phase after this one.

What the phase *could* do was done. CG-18 recomputes each fixture's digest and
word count from its declared mandatory set, over 18 measurements across nine
fixtures; it found all eight stale on its first run, one by 1,738 words. And
the ninth fixture — the evidence-adapter class, which had none — was written
and placed on 2026-08-06, making the class map eight-for-eight without a
double-count. It records no `Compiler:` line, because there is no compiler and
the eight before it said there was.

The packets are governed, budgeted, and now loudly perishable. They are not
compiled, and one fixture more does not change that.

The honest form of this claim, with the evidence, is
`FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md`.

## Criterion 8 — the confirming review returned REVISE

RC-10 was commissioned over the exact bytes act 1 binds, with no authoring
context. Its verdict, copied: **`VERDICT: REVISE`**.

Its three most serious findings all landed on work this round had produced
while correcting other work:

1. **RFC10-18 had a live escape.** The clause was written this round to stop
   an executing party adjudicating its own success — and forbade only
   `completed`, leaving an indefinite park in `blocked` open. Verified against
   RFC10-5's `running → blocked (→ running on unblock)` edge and RFC10-19's
   "transitioning to `paused` or `blocked` discharges no obligation under this
   clause". Fixed at rev11a.
2. **Twenty-one stale derived word counts sat inside act 1's digest set** — in
   the commit whose message said it had corrected every stale derived value.
   Nineteen were module rows in package READMEs. Fixed, and CG-21 now
   recomputes all 19 rows every run.
3. **The mission-safety closure report misdescribed four of the seams it
   reported closed**, including an "owner-signed dispatch" carve-out that
   occurs zero times in RFC-0010. Fixed against the clause text.

Every one of those is now repaired with a check behind it. **The repairs
themselves have been read by no reviewer**, and one of them edits a contract
inside act 1's digest set. So criterion 8 is unmet in the same shape it was
unmet before RC-10 ran — one round smaller, and no longer hypothetical.

## What a "not ready" verdict does and does not block

It does **not** block acts 2, 3, 4 or 5. Nothing in criterion 5 or 8 touches
the craft amendment, the topology bundle, the overview, or the doctrine
amendment; those four stand on their own arguments and their own residuals,
which the offering record states.

It does **not** mean act 1 must wait. Act 1 is a decision about whether the
current text is better as adopted authority than as candidate material, and
this report has no standing to make it — VIS-4 reserves it. What this report
supplies is the input: what is wrong inside the bytes, stated where an owner
will see it before the phrase rather than after.

It **does** mean that "begin OpenSpec authoring" is not the next step. The
next steps, in the order their blockers resolve:

| Order | Step | Blocked on |
|---|---|---|
| 1 | Owner rulings on P-17, P-21, P-22, P-23, P-24 | Nothing — they are open questions awaiting an answer |
| 2 | A review over the RC-10 repairs | Nothing; it is one commission |
| 3 | The five acts, in the ceremony's order | The owner |
| 4 | OpenSpec authoring | Acts 1 and 3 |
| 5 | A real context compiler | Step 4 — it is the first thing OpenSpec should specify |

## Evidence

All read-only. Read each check's **output**, not its exit code.

```sh
python3 scripts/check_governance.py            # 32 checks, denominators printed
python3 scripts/check_governance.py --selftest # 19 fixtures, each check shown able to fail
CS=.syzygy/governance/contracts/candidates/scripts
python3 $CS/verify_final_prespec.py
python3 $CS/build_contract_index.py --check
python3 $CS/build_dependency_index.py --check
```

The raw reviews this report draws on are in `reviews/`, unedited. Where this
file and a raw review disagree about what a reviewer said, the raw review
wins; where it and a contract disagree about what a clause says, the clause
wins.
