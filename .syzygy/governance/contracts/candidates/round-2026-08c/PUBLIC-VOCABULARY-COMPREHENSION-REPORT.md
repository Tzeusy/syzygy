# Public vocabulary — what a fresh reader could and could not do

> **Non-authoritative round record.** The raw review is
> `reviews/RD-3-vocabulary-RAW.md` and is never edited. Where this file and the
> raw review disagree about what the reviewer found, **the raw review wins**;
> where it and the registry disagree about what a term means, the registry's
> owning authority wins.
>
> Verdict words are copied, not summarised.

## The commission and the verdict

A reader with no project context was given the default path — `README.md` plus
`.syzygy/intent/OVERVIEW.md` before its first `<details>` drawer — and the
candidate term registry. It was asked to classify five real examples across the
five dimensions, separate five adjacent term pairs, apply the admission rule to
two admitted terms, and name every term whose meaning it could not establish.

**`VERDICT: REVISE`.**

It answered **2 of 5** classification exercises without guessing, and could not
separate **1 of 5** adjacent pairs.

## What worked, in the reviewer's own assessment

Recorded first, because a report that only lists defects misrepresents the
measurement:

> §1's five-dimension split is genuinely clarifying; the plane/label first-use
> rule and the warrant/evidence split both survived contact with a fresh
> reader; §3's admission rule is well drafted and singular; and §6, the T-16
> naming banner, and the CG-23 report-only framing are exemplary intellectual
> honesty of a kind I do not usually see. Every one of my findings is
> repairable without redesigning the registry.

Four of the five adjacent pairs separated cleanly: label vs tier, the Observed
*plane* vs an Observed *claim*, reconciliation vs converged vs aligned, and
warrant vs evidence. **The first-use rule this round added — write "the
Observed plane" or "an Observed claim", never bare "Observed" — was tested by a
reader who had not been told it existed, and it worked.**

## The one that did not separate, and it is the important one

### `Unknown` (T-31) vs `Gap` (T-20) — **could not separate**

RD-3's finding **D-1**: the two entries classify the *same* example in opposite
ways. T-20's own example treats "an adopted requirement with no verifying
evidence" as a **Gap**; T-31's cross-reference says a gap is something *known*
to be absent, and that not knowing whether it is absent is an **Unknown**.

This matters more than any other finding in the review, and for a reason the
brief on project-shape facets makes concrete: *missing declaration* and *failed
evidence* are the pair a status system most often merges, and merging them is
how a system starts lying. If the registry cannot separate them, nothing
downstream will.

**Not resolved here.** It is a question about what the corpus means, not about
how a registry is worded, and answering it inside the same pass that wrote
T-31 would be the loop this round has already been caught in twice. It is
**owner decision packet 5** and the sharpest single item in it.

## The count drift, and what caused it

RD-3 found the registry contradicting itself about its own size in four places
— eleven core terms in one sentence and twelve five lines later, thirty entries
where a script counts thirty-one, and T-31 absent from the authority-coverage
summary entirely.

**Every one of these was created by this round**, by adding T-31 and demoting
`Claim` without sweeping the registry's own self-descriptions. All are
corrected, and the correction is worth naming for what it is: **the
volatile-derived-value class, reappearing inside the artifact this round wrote
to fix that class elsewhere.** A count of one's own contents is a derived value
like any other.

Also corrected: T-16 listed *rendering tier* — its own heading — as a permitted
alias of itself (RD-3 finding **F-1**), which hid which of the two competing
names the registry had chosen.

## The bound is not a bound yet

RD-3's central structural finding: the default path is declared bounded to
eleven terms and carries **fifteen** Syzygy-specific terms with no entry and no
in-place definition. Its list:

`surface` · `kernel` · `plane` · `workspace` · `actuator` · `experience` ·
`owner act` · `gate` · `evidence bar` — and six more it enumerates.

Two sharper points inside that:

- **`experience` and `workspace` have no home anywhere.** `workspace` has
  **zero occurrences in the entire adopted doctrine tree**; `experience` heads
  a section of `README.md` and is defined nowhere. These are not advanced terms
  used early — they are words with no owner.
- **`plane` carries five or six senses**, two of them on the default path.
  It is also the word T-06 is built on.

**None of this is repaired here**, and the reason is worth stating rather than
apologising for. Nine of RD-3's fifteen appear in `OVERVIEW.md`, which is act
4's digest subject. Editing an artifact whose digest an unperformed act binds
is a worse defect than the one being corrected — but RD-3 makes the
counter-argument better than the round can:

> Findings A.5, A-6 and G-1 are repairs to a *pending* offering, not
> corrections to a bound artifact — which, if the act has not fired, is the
> cheapest moment they will ever be available.

That is right, and it is an owner call rather than an agent's. It is **decision
packet 5**, option (c).

## Three findings the round is carrying rather than closing

| # | Finding | Why it is open |
|---|---|---|
| **D-1** | `Unknown` and `Gap` classify the same example oppositely | A question about corpus meaning; **packet 5** |
| **A.5** | `Reconciliation` is used on the default path in the sense T-26's entry explicitly reserves against | `OVERVIEW.md:46,54` — inside act 4's digest subject. Either the reservation is wrong or the narrative needs a different noun, and RD-3's **B-1** notes the corpus has **no term at all** for "the difference between desired and observed", which is the concept the narrative is reaching for |
| **A-6** | `README.md` and `OVERVIEW.md` contradict each other on whether Mission Control is a surface | Both are default-path artifacts; one is inside act 4's digest subject |

## What the check learned

RD-3's finding **A-4** — the check the registry tells a reader to trust cannot
see the leak class that matters — is closed, and closing it changed the check
twice in opposite directions:

1. **Matching was tightened** to word boundaries, which removed a false
   `Warrant` finding that had been published in **P-17** and in the
   term-closure report. `warranted work` is not the term `Warrant`.
2. **Then it was loosened back to case-insensitive**, because the corpus's real
   leaks are lowercase running prose — "computed at an identified evaluation",
   "the intent that warranted it" — and a case-sensitive matcher found none of
   them.

The cost of matching loosely is ordinary English read as jargon. That is paid
for the way this battery pays for every exemption: **an enumerated allowlist,
printed on every run**, keyed by (file, term), currently holding one entry.

And the core set is no longer transcribed into the checker. It was a
hard-coded tuple; it is now parsed from the registry's own core table, so the
check and the artifact cannot disagree about what "core" means. Two selftest
fixtures cover the failure that derivation introduces.

RD-3 also caught, incidentally, that the allowlist's own quotation of the line
it exempts **did not match that line**. Corrected.

## Vocabulary simplification — what was done, and what is proposed

**Done, inside candidate policy:**

- The core set is **eleven**, not twelve. `Claim` moved to advanced: a newcomer
  does not need the kernel's positive-status carrier to understand the thesis.
- `Unknown` has its own entry, **T-31**, with an **adopted** owning authority.
  It was previously listed in core under T-15's ID, which is the *dimension*,
  not the value.
- The core table now leads with the **plain question** each term answers, and
  the registry carries the ordinary-language mapping (*what should be true*,
  *what evidence says is true*, *what agents did*, *something missing*,
  *authorities disagree*, *check work against intent*) as the preferred
  default-path phrasing, with the term in parentheses.
- One admission rule, in one place, with five conditions.

**Proposed, not applied** — every one touches an artifact inside an unperformed
act's digest subject:

| Avoid on the default path | Prefer |
|---|---|
| kernel | shared project model |
| surface | view |
| workspace | portfolio workspace, defined inline |
| actuator | agent workers, or work-execution tools |
| warrant | approval, or authority — unless the precise term is needed |
| evaluation engine | the rules that compare declared intent and evidence |

Poetic codenames keep literal subtitles. `Project Genome`'s first use in any
document reads **"Project Genome — the project's complete normative
definition"**.

## Is the public vocabulary bounded?

**As a boundary: yes.** The two tiers exist, the registry draws them, and a
check reports the bound every run against a core set it reads from the registry
rather than a copy.

**As a definition: no, and by a wider margin than the last round recorded.**
Eight of thirty-one terms still have no adopted definition anywhere (**P-17**),
fifteen default-path terms have no entry at all, and two entries classify the
same example in opposite ways.

A reader can find out which words are public. For a meaningful fraction of
them, finding out what they mean is still not possible.
