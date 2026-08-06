# Deterministic context selection — final report

> **Non-authoritative round record.** The raw review is
> `reviews/RD-5-context-selection-RAW.md` and is never edited. Where this file
> and the raw review disagree about what the reviewer found, **the raw review
> wins**. Verdict words are copied, not summarised.

## The commission and the verdict

A reviewer with no authoring context was asked to **independently derive** each
of the nine golden context selections from the declared metadata and RFC11-4's
rules, and only then compare against what the fixtures record. The point was
not to audit the fixtures. It was to find out whether a *different* competent
human, given the same inputs, produces the same set — because that is what
"deterministic mandatory selection" has to mean before anything implements it.

**`VERDICT: REVISE`.**

**Independently reproduced: 4 of 9 — and the reviewer states that as an upper
bound.**

## The answer to the question the fixtures exist to answer

> The claim RFC11-4 makes is *"same inputs, same selection."* Two competent
> humans with the same metadata and the same rules produced different
> selections for five of nine tasks, and disagreed about **which rule to
> apply** — not about how to apply it — in every one of those five.

**Deterministic mandatory selection is not yet true, and not yet true even for
a human.** That is the finding, and it is the honest state of Workstream G.

## The reviewer's own disclosure, recorded first

RD-5 opens by disqualifying part of its own result before stating any finding,
and this belongs at the top rather than in a footnote:

> Each fixture's `**Selection rule trace (RFC11-4).**` paragraph sits in the
> file's preamble, *above* the `## Required context` heading … My extraction
> took everything above `## Required context`, so I read all nine traces before
> writing a single derivation.

So *"4 of 9"* means **at most 4 of 9**, and probably fewer blind. The
disagreements are correspondingly stronger: the reviewer differs from five
fixtures **despite having read their reasoning**.

**And the contamination is itself a finding about the fixture format:**

> A golden fixture whose question and answer cannot be separated cannot be used
> to test a selector.

**Accepted, and it is the first repair.** Each fixture must be split into a
`## Task` block — objective, warrant, risk class — with the trace and selection
strictly below a line, so a future reviewer or a future selector can be given
the question without the answer. **Not applied here:** the nine fixtures are
inside act 1's digest subject, and restructuring nine files in the pass that
froze them for review is the move this round has spent three closure reports
refusing.

## The finding that decides Workstream G

### RFC11-4's phase-rule universal has no population for five of eleven contracts

The chain, which the reviewer calls *"short and entirely mechanical"* and which
**this session verified independently**:

1. RFC11-4: *"The mandatory set always includes the **governing phase-rule
   clause of every selected contract** … no lawful packet omits the boundary
   rule of a contract it loads."*
2. `05-CONTRACT-INDEX.yaml` carries **353 clause rows**, of which **6** are
   `kind: phase-rule` — RFC-0006 through RFC-0011. **RFC-0001 through
   RFC-0005 have none**, and none exists in their text either.
3. RFC11-6: incomplete context is marked Unknown with the gap named, and **by
   default the run does not launch**.
4. **All nine golden fixtures load at least one of RFC-0001…0005.**

> The selector is not malfunctioning — it is correctly fail-closed on metadata
> that asserts a universal its population does not satisfy. But the observable
> outcome is that **the nine artifacts offered as proof that deterministic
> selection works are the nine a conformant implementation cannot produce.**

**Verified this session** by parsing every clause row of the generated index:
353 rows, 345 `normative`, 6 `phase-rule`, 2 `informative`; phase-rule
contracts `{6,7,8,9,10,11}`; contracts with none `{1,2,3,4,5}`. Two methods,
per verification rule 2 — the index parse and the reviewer's independent
`grep -F` over the contract text.

**Not repaired.** Both routes are normative edits to act 1's digest subject:
give RFC-0001…0005 a phase-rule clause each (five new clauses), or narrow
RFC11-4's universal to the contracts that have one. **This is the sharpest
single item routed to the next pass**, and it is why the Context Compiler
criterion is unmet.

### What breaks second and third

**Second — `depends_on` has no termination rule.** With no closure rule stated
anywhere, *"the natural implementation closes transitively and hands back
91–100% of the corpus, reproducing OD-R10-3's architecture problem inside the
contract written to abolish it."* The fixtures avoid it by an **unstated**
narrowing that exists only in the authors' judgment — and **the nine fixtures
apply at least three different versions of it**. Fixture 9's is the only one
written down, and the reviewer says it is *"ready to lift verbatim"* into
RFC11-4.

**Third — doctrine and craft selection is not derivable at all.** *"A selector
asked 'which file owns VIS-4?' gets five files from a regex mention scan and no
way to choose. Every fixture selects doctrine; no fixture's doctrine selection
is derivable."* `governance_sources` in the generated index carries no `governs`
or `applies_to`.

## What was repaired here, and it is the one that could be

### Five stale figures, and one that had leaked into the generated report — **closed**

RD-5 counted **88 measurement-shaped figures across the nine fixtures. CG-18
covers 18.** The other ~70 are transcriptions checked by nothing, and **at
least five contradict their own fixture's headline** — with the stale figure
being, in every case, *"the one the budget disposition is reasoned against."*

**One had propagated into `CONTEXT-BUDGET-REPORT.md`** — the artifact this
round built to end exactly this class. Its §2 transcribed fixture prose reading
*"RFC-0001 is indivisible (8,353 w …)"* while its own §3 table, computed by the
same script thirty lines below, said **8,342**. **Eleven words apart, in one
generated file, under a banner reading *"Do not edit by hand, and do not copy a
figure out of it."*** Verified this session at both line numbers.

**This is the second time in one round that the volatile-derived-value class
reappeared inside the artifact written to fix it** — the first was the term
registry's counts of its own contents. Twice is a pattern, and the pattern is:
*a generator that quotes prose has re-opened the door it closed.*

**Repaired at the generator.** `build_budget_report.py` now **redacts every
measurement figure out of the fixture prose it transcribes**, replacing it with
a pointer to the table that measures the files:

```python
PROSE_MEASUREMENT = re.compile(
    r"\b\d{1,2},\d{3}(?:\s*(?:w\b|words?\b|(?:est\.?|estimated)\s+tokens?\b"
    r"|tokens?\b))?")
```

Redactions are **counted and printed verbatim at the foot of §5**, so the
removal is auditable rather than a silent deletion. A stale figure in a fixture
can no longer reach the report at all.

**And the redaction density is left visible on purpose**, with the report
saying so: *"A disposition argued against an unchecked number is a disposition
argued against nothing. Reading these fields with the figures removed shows how
much of each argument was resting on one."*

**Selftest re-run after the change:** both mutation fixtures still detect
(`SELFTEST OK: measured word count mutation detected`; `SELFTEST OK: packet
digest mutation detected`), `--check` reports `fixture anchors match
regeneration`, and CG-18 reports `18 measurements examined, 0 findings`.

**Not repaired: the ~70 unchecked figures inside the fixtures themselves.**
RD-5's repair 6 — extend CG-18 past the headline to every `\d,\d{3}` in a
fixture — is right and is **routed to the next pass**, because it would fail on
nine files inside act 1's digest subject and the fix for those failures is
editing them.

## Class coverage — no class uncovered, one double-counted, one nominal

| # | Required class | Fixture | Verdict |
|---|---|---|---|
| 1 | doctrine amendment | 6 | **yes** |
| 2 | graph identity change | 7 | **yes** |
| 3 | OpenSpec capability authoring | 8 | **yes** |
| 4 | evidence-adapter change | 9 | **yes** |
| 5 | Polaris presentation change | 1 | **yes** |
| 6 | **Trajectory lifecycle change** | 2 | **nominally only** |
| 7 | Orrery lens change | 3 | **yes** |
| 8 | bounded Mission spanning capabilities/projects | 5 | **partially** |
| — | *(maps to no required class)* | 4 | extra — security / execution profile |

**Class 6 is covered by a fixture that does not exercise it.** Fixture 2 is an
*adapter* change. The two RFC-0008 modules it **omits** are exactly the work
lifecycle: `identity-authority-materialization.md` (work identity, authority,
dispatch, materialization) and `accounting-reconciliation-and-release.md`. What
it exercises is the work-state *vocabulary*.

**And fixtures 2 and 9 say so about each other** — fixture 9 reads *"Fixture 2
is that task; this one is its complement."* **The adapter class is
double-counted across classes 4 and 6, and no fixture exercises Trajectory
dispatch, materialization, accounting or release.**

**Class 8 is half-exercised.** Fixture 5 covers the portfolio-authority half
well and contains **no capability contract** — RFC-0001, which owns capability
identity at RFC1-14, is omitted. *"A mission spanning capabilities would need
RFC1-14."*

**So the eight classes are covered by eight fixtures, not nine, and the
redundancy the count implies is not there.** The previous round's report said
seven-for-eight with one double-count; RD-5's read is sharper and supersedes
it — the gap is not *evidence-adapter*, it is *Trajectory lifecycle*, and the
double-count is the adapter class.

## The two fixture defects that are defects, not disclosures

RD-5 is explicit that most of what it found is **disclosed** by the package
already, and says so generously:

> The package is unusually honest about its own limits. … That candour is the
> reason this review could be done at all, and it is worth saying plainly.

Three things it classifies as defects rather than disclosures:

1. **Fixture 5 states today that a 22,260-token packet is *"inside the 15–20k
   working target."*** *"A reader who loads that fixture as a worked example is
   told a false thing about the one number the fixture exists to demonstrate."*
   The repair that fixed the same fault in fixture 2 was not swept across.
2. **Fixtures 1 and 8 apply opposite readings of RFC11-4's phase-rule
   parenthetical to the same contract — and fixture 8 documents fixture 1's
   reading as the defect it was repaired for.** *"A golden set cannot contain
   both the standard and its counter-example, unlabelled."*
3. **The phase-rule universal** (above), which *"makes every fixture in the set
   unlawful under a literal reading — and two fixtures (7 and 9) assert the
   opposite in prose that a `grep -F` refutes."*

**None is repaired here**, for the reason that governs the whole round: all
nine fixtures are inside act 1's digest subject, and editing them now would
invalidate the review that found the defects. **They are named, not softened,
and they are why the golden-fixture criterion is unmet.**

## Omission registers, and the relation model's effect

**Omission registers (criterion 4):** incomplete. `craft-and-care/INSTALL-RECORD.md`
is unregistered in all nine; the doctrine registers in fixtures 1–5 are
incomplete. RFC11-6 requires every applicable-but-omitted candidate to be named
with a reason, so a silent omission is a discharge that did not happen.

**The relation model (criterion 3):** `constrains` reaching the fixtures would
change some mandatory sets — and the clause anchor is what keeps the change
cheap, since `constrains_source` names one clause rather than a contract. **But
RFC11-4 does not name `constrains` among its selection inputs**, so a
conformant selector reads none of it today. That is owner item **P-21(c)**, and
it is the same gap the contract-relation closure report leaves open.

## Disposition

**The golden context selections are complete in count and not complete as
evidence.** Nine exist, all nine reproduce their anchors under two independent
implementations, and **four of nine were reproduced by an independent human who
had already seen the answers.**

**Unmet, and named as unmet:**

- RFC11-4's phase-rule universal has no population for five contracts — **every
  fixture is unlawful under a literal reading.**
- `depends_on` has no termination rule; the fixtures apply three different
  unstated ones.
- Doctrine and craft selection is not derivable from declared metadata at all.
- Two fixtures state a false figure; two apply opposite readings of one rule.
- The fixture format cannot separate question from answer.
- ~70 fixture measurements are checked by nothing.

**Closed this pass:** the generated report no longer transcribes a measurement
figure from anything, so the one stale figure that had escaped into it is gone
and no successor can follow.

**The reviewer's own summary is the right last word:**

> The corpus is close. Repairs 1–3 above are small and local; 4–7 are
> mechanical. None requires re-authoring a contract's semantics. But the
> fixture set cannot be offered as evidence for RFC11-4's determinism claim in
> its current state.
