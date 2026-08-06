# Term closure — what the vocabulary work settled, and what it did not

> **Non-authoritative round record.** This file accepts nothing and adopts
> nothing. It reports the state of charter §9 (vocabulary closure) as of
> 2026-08-06 and names what remains open. The vocabulary itself lives in
> `../policy-candidates/TERM-REGISTRY.md`, which is **candidate** — where this
> report and the registry disagree, the registry is right and this file is
> stale; where the registry and an owning authority disagree, the authority
> wins and both are stale.
>
> **Written late.** Charter §21 named this file as a required output of the
> round and it was not produced at the round's close. The work it reports was
> done — across the registry, `../round-2026-08/TERM-MIGRATION-REPORT.md`, and
> raw review `reviews/RC-3-vocabulary-RAW.md` — but no artifact drew it
> together or stated the residue, so "is §9 closed?" had no answer anyone
> could read. That is the gap this file closes; it is not a fresh round of
> vocabulary work.

## The answer, in one line

**Five of five §9 sub-mandates are executed; two of them are executed as far
as an agent may take them, and stop at an owner act.** Nothing in §9 is
blocked on more drafting. Three residues are named below, each already an
owner item.

## §9.1 — the false finding, retired

A published finding said adopted doctrine cites a "README glossary" that
**does not exist**. It reached five tracked artifacts before anyone checked.

The glossary exists, at `../../../doctrine/README.md:15` (`## Glossary (read
first)`). [Observed — file read this session.]

The real defect is narrower, and the original reviewer had stated it
correctly: doctrine cites the glossary from three sites (`doctrine/vision.md:16`,
`vision.md:39`, `v1.md:98`) **without saying which README**, and the root
`README.md` a reader is actually holding has none. The pointer routes them to
the wrong file and they conclude it is broken.

What was done:

| | |
|---|---|
| Correction to the register | `PENDING-OWNER-DECISIONS.md` **P-25**, which replaces the false half of P-20 and states the retired claim rather than deleting it |
| Reachability, done | the root `README.md` now links the glossary directly |
| The citation repair | drafted, **not performed**: `../policy-candidates/DOCTRINE-EDITORIAL-AMENDMENT-GLOSSARY-CITATION.md`. It amends adopted doctrine, so VIS-4 reserves it |

Three terms remain genuinely undefined anywhere reachable — *actuator toolchain*
(`vision.md:38`), *ai-bootstrap toolchain* (`v1.md:98`), and *actuator*. Those
are findings carried under P-25, not exemptions.

**The lesson this cost is recorded** (`../../../decisions/PROCESS-LESSONS.md`):
a published finding can be false, and false findings propagate. The original
reviewer's qualifier — *which* README — was lost in a summary, and the summary
is what got copied.

## §9.2 — the honest rename

The registry was titled *"Syzygy's canonical public vocabulary."* A candidate
has no canon. Renamed 2026-08-05b to **"Working term registry — candidate"**,
with the reason stated in the file: an artifact must not contradict itself in
the first line and the third.

This is now mechanical rather than a matter of care. **CG-16** examines every
mention of the registry anywhere in the corpus and fails the run if one calls
it adopted, accepted, approved, binding, authoritative, or canonical without a
negation next to the word. Current result: **32 mentions examined, 0 findings.**

## §9.3 — two tiers, and where the default path still leaks

The registry bounds the default public path to **twelve core terms**; the
other eighteen entries are advanced vocabulary — real, needed, and reachable
in one action, but never a prerequisite.

**The core twelve, against the charter's proposal.** The charter's §9.3 list
was offered as "at minimum consider", and the registry took eleven of its
twelve. One substitution:

| Charter proposed | Registry took | Why |
|---|---|---|
| Context packet (T-30) | **Claim** (T-13) | Claim is the sole carrier of positive status in the candidate kernel (RFC1-24) — a newcomer meets it in the first paragraph about state. Context packet is an agent-facing mechanism; a reader does not need it to understand what Syzygy is. T-30 is also one of the eight candidate-only terms below |

The charter's advanced list — source snapshot, evaluation, observation record,
challenge, warrant, evidence tier, autonomy envelope, attention item — maps
one-for-one onto registry entries T-21, T-22, T-23, T-18, T-17, T-16, T-28,
T-29, all in the advanced tier. [Observed — eight of eight checked by hand
against the entry headings this session.]

**The bound is now reported every run, not asserted.** **CG-23** parses the
tier split out of the registry itself (so it cannot go stale against a
hand-copied list), cuts each default-path document at its first `<details>`
drawer, and reports every advanced term appearing before that cut. Current
result: **36 term-in-file pairs examined, 2 findings** —

- `.syzygy/intent/OVERVIEW.md` — `Warrant` (T-17) 1×, as the mermaid edge
  label `warranted work` (line 58);
- `.syzygy/intent/OVERVIEW.md` — `Evaluation` (T-22) 1×, in the kernel
  sentence at line 65 ("a temporal project graph plus an evaluation …").

Both are inside act 4's digest subject, so neither was edited here. They are
smaller than the registry's own prose predicts, and one part of that prose is
wrong: it lists *evidence* among the default path's unlicensed leaners, but
Evidence is **T-14, core**. [Observed.] The registry's other named leaners —
*kernel* (3 uses), *surface* (14), *workspace* (3), *actuator* (2) — are not
registry terms at all, so CG-23 cannot see them; that half of the bound stays
prose, and it stays true.

**One naming mismatch, recorded not fixed.** The core table lists `Unknown` at
ID **T-15**, but T-15's entry is titled *Claim epistemic label*, and Unknown is
one of its three values rather than an entry of its own — there is no
`#### T-… · Unknown` heading anywhere in the registry. [Observed — grep count
0, confirmed by reading T-15 in full.] Not a contradiction; the definition a
reader needs is in T-15 and is correct. It is a promise the table makes and
the entry list does not keep, and it belongs to the registry's owner act.

**Also corrected:** the registry stated that its core bound would be "enforced
mechanically by `check_governance.py` CG-17 once the core set is
owner-accepted." CG-17 routes surface clauses and has nothing to do with
vocabulary. The promise now names CG-23, which exists.

## §9.4 — five dimensions, mechanically separated

The registry's §1 names five closed vocabularies that English collapses into
one word, each with its owning authority: **state plane** (RFC1-22, candidate),
**claim epistemic label** (`trust-and-evidence.md`, adopted), **evidence tier**
(RFC2-25, candidate), **work lifecycle** (RFC8-12/8-28, candidate),
**governance lifecycle** (RFC3-16 candidate; adoption authority VIS-4,
adopted).

The charter's operative clause was not the table but the prohibition: *disallow
an unqualified field or prose term `status` where the dimension is ambiguous.*
That was documented and unenforced. It is now **CG-22**.

CG-22 sweeps the active lane — 135 tracked markdown files, excluding frozen
history, verbatim reviewer output, and the superseded round, which are
evidence and are never edited to satisfy a checker. It catches three shapes
(bare `` `status` ``, code-span field `` `status:` ``, indented `status:`) and
exempts a use whose whitespace-normalized ±2-line window names one of the five
dimensions, or marks the mention as retired.

**It found one real defect on its first run, and it was in this round's own
work.** `GOVERNANCE-SUBSTRATE-LOCK.yaml` recorded the `th_engineering` drift
under a key named `status:` — while CG-19's own header called that value a
*disposition*. Renamed to `disposition:`; CG-19 now reads the new key and
**reports a legacy `status:` key as a finding** rather than silently accepting
it, with fixture `F8g` holding that behavior. `SUBSTRATE-REPRODUCIBILITY-REPORT.md`
updated to match.

Current result: **135 files examined, 0 findings**, with **2 files
allowlisted** and printed —

- the registry itself, which states the rule (the bare form is the thing being
  forbidden);
- `craft-and-care/interfaces-and-dependencies.md`, which quotes a violating
  API's own field name as the rule's worked counter-example. That is adopted
  craft text, not a Syzygy field, and amending it would be a normative edit
  requiring a semantic delta — allowlisting the checker is the correct move,
  not editing the artifact.

Seven `--selftest` fixtures hold CG-22, including two negatives: a qualifier
that lands across a line wrap must exempt, and a retirement marker **outside**
the window must not. The second exists because the exemption is otherwise a
back door — any file mentioning a rename anywhere would pass.

## §9.5 — the admission rule, and the limit of what it governs

The registry's §3 admits a new durable term only when all conditions hold: no
existing term covers it; the distinction matters operationally (something is
rendered, counted, gated, routed, or refused differently); exactly one artifact
owns the definition; and a newcomer can explain it after one paragraph.

**The rule was applied to no incumbent term.** The registry says so itself, and
the sentence is worth repeating rather than burying: all thirty entries are
vocabulary admitted by prior use. The rule governs what comes next — which
matters, because what comes next is OpenSpec authoring, and requirement
authoring is where field names multiply.

## What is closed, and what an owner still owns

**Closed by this round.** The false glossary finding (retired with rationale,
not deleted). The dishonest title. The two-tier split, with the core set
bounded and the bound reported every run. The five dimensions — state plane,
epistemic label, evidence tier, work lifecycle, governance lifecycle — with
the unqualified-field prohibition made executable and one live defect found
and fixed by it. The admission rule, written and scoped.

**Open, and only the owner can dispose** — each already carries an item:

| Item | What is unsettled |
|---|---|
| **P-16** | Approve the registry as the working vocabulary, or amend. Until then the six-plane model is how we agree to speak and doctrine's adopted three-state thesis is what governs |
| **P-17** | **Eight of the thirty public terms have no adopted definition anywhere** — State plane, Proposed state, Historical state, Evidence tier, Mission, Autonomy envelope, Attention item, Context packet. They are usable vocabulary and unusable authority. Acts 1 and 5 close this. A reader can find out which words are public; for eight of them, finding out what they *mean* is not yet possible |
| **P-18** | Three doctrine/contract vocabulary seams: four constitutional `governance/` categories versus five-plus-a-reserved-sixth; **Claim** absent from doctrine's frozen-noun list while candidate RFC1-24 makes it the sole carrier of positive status; `evidence tier` and `rendering tier` naming one dimension twice |
| **P-25** | The glossary citation amendment — drafted, not performed — plus three terms undefined anywhere reachable |

**What this report does not establish.** The corpus was never swept for terms
used normatively that are absent from the registry entirely — the larger unrun
half of a lexical audit, which the migration report also names under its own
finding. No newcomer comprehension test has been run on any of the thirty
entries; VIS-3's fresh-reader review is a separate act. Nothing was renamed or
migrated anywhere in the repository beyond the one lock key named above.

## Evidence

All read-only. Read each check's **output**, not its exit code.

```sh
python3 scripts/check_governance.py            # CG-16, CG-22, CG-22b, CG-23
python3 scripts/check_governance.py --selftest # each check shown able to fail
```

Figures in this report were produced by those two commands in the session that
wrote it and are re-derivable from them. Where a figure here disagrees with a
current run, the run is right and this file is stale.
