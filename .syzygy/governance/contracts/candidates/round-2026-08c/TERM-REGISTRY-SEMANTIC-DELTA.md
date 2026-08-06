# Semantic delta SD-11 — the term registry's own contradictions

> **A proposal, not an act.** The term registry is **candidate** policy: it
> binds nothing, and neither does this. Every entry in it names the artifact
> that owns its meaning, and where the registry and an owning authority
> disagree, the authority wins.

**Artifact(s):** `../policy-candidates/TERM-REGISTRY.md`
**Stable IDs affected:** T-13, T-15, T-16, T-31 (new); §"Two tiers",
§"Admitting a new public term", §1, §3
**Change class:** **Normative** for the candidate registry — the admission
rule and the tier split are the things the registry *is*. Nothing here touches
adopted doctrine or any contract clause.
**Author:** the 2026-08-06 final-closure session
**Date:** 2026-08-06

---

## The problem, stated once

A registry exists to settle what words mean. This one contained, in one file:

- **two different admission rules**, disagreeing about how many conditions
  admit a term;
- **a core-tier entry naming a term and pointing at the ID of a different
  term**;
- a core set that made a newcomer learn the kernel's status-carrier before
  they could read the thesis.

None of these is a large error. All three are the same error: **an artifact
whose job is to remove ambiguity, containing ambiguity about itself.**

---

## Change 1 — one admission rule, in one place

### Current meaning

Two rules, in two sections, 100 lines apart.

`TERM-REGISTRY.md` §"Admitting a new public term":

> A new term is admitted only when **all five** hold — any one failing is a
> rejection, not a discussion: […] 5. **It passes a fresh-reader distinction
> test**: a reader given only the two definitions places five real examples
> correctly, without coaching.

`TERM-REGISTRY.md` §3 "Term-admission rule":

> **A new durable term is admitted only when all four hold:** […]

Both are stated as *the* rule. Both use "only when all N hold". They are not
the same rule: the four-condition form has no fresh-reader test.

### Proposed meaning

**§3 states the rule. There is no other, anywhere in the file.** The
five-condition form survives, because the condition the four-condition form
omitted — the fresh-reader distinction test — is the only one that **cannot be
satisfied by the person proposing the term**. A rule whose every condition the
proposer can self-certify is not an admission rule.

Each of the retired form's four conditions maps onto one of the surviving
five; no obligation is lost, and the delta says so rather than asserting
"editorial".

The old heading remains and states nothing, with a sentence explaining what
was there and why it went. A silently deleted section is indistinguishable
from a section that was never written.

### What explicitly does NOT change

- No admitted term is re-tested against the surviving rule. Thirty entries
  were admitted under an ambiguous rule; re-adjudicating them is a separate
  piece of work and is **not** done here. **[Unknown]** how many of the thirty
  would pass condition 5 today — review RD-3 was asked to test two of them.
- Retirement discipline is unchanged: retire the term, keep the ID, never
  reuse it.

### One thing added

**Internal metadata is not public vocabulary**, stated explicitly for the
first time. `depends_on`, `constrains` and `cites` are contract-index
mechanics; *maximum park duration*, *unmediated effect surface* and *sibling
disposition on partial failure* are RFC-0010 envelope fields. Six terms
entered the corpus this round and **none of them is admitted to this
registry**. Recording that is what stops the next round admitting them by
default, on the reasoning that they are "already in use".

---

## Change 2 — `Unknown` gets its own entry, T-31

### Current meaning

The core-tier table:

> | Unknown | T-15 | no evidence — never green, never zero |

**T-15 is not `Unknown`.** T-15 is *Claim epistemic label* — the dimension
whose three values are Observed, Inferred and Unknown. The core set named a
**value** and pointed at its **dimension**.

The registry knows this: §1 lists T-15 as the label dimension, and T-15's own
entry is headed "Claim epistemic label". The core table is the only place that
says otherwise, and it is the table a newcomer reads first.

### Proposed meaning

A new entry **T-31 · Unknown**, with:

- **adopted** owning authority — VIS-2, `trust-and-evidence.md`, SDR-6 for
  never-zero. It is one of very few core terms whose definition does not
  depend on an unaccepted contract;
- the never-zero rule, the never-Inferred rule, and the closed reason
  vocabulary;
- deprecated synonyms enumerated: *N/A*, *TBD*, *pending*, `0`, `—`, an empty
  cell, a grey badge with no reason — "every one of these is a way of not
  saying Unknown, and several read as a *negative* answer rather than an
  absent one";
- and the three distinctions a reader actually confuses: Unknown vs **Gap**
  (a gap is *known* to be absent; an Unknown is not knowing), Unknown vs
  **Contradiction** (which is more information, not less), and Unknown the
  value vs T-15 the dimension.

**Why a new ID rather than a correction to the table.** Because `Unknown` does
pass the five-condition rule on its own merits: no existing term covers it
(T-15 is the dimension); the distinction is operational (an Unknown blocks,
renders grey, and is never counted as zero); its authority is **adopted** and
singular; a newcomer understands it in one sentence with no second Syzygy
term; and it separates cleanly from its nearest neighbour, `Gap`. A term that
passes the rule and is on the default path should have an entry.

**Side effect worth naming:** this closes one of P-17's eight
no-adopted-definition terms in the *other* direction. `Unknown` was never one
of the eight; but the core set's most doctrinally-grounded term had no entry
of its own, which is a related defect the eight-term list did not surface.

---

## Change 3 — `Claim` moves to advanced; the core set becomes eleven

### Current meaning

Twelve core terms, including:

> | Claim | T-13 | an assertion about state, always carrying a label |

### Proposed meaning

Eleven core terms. `Claim` moves to advanced.

**The argument.** A newcomer needs to understand *what Syzygy is for*: that
there is what should be true, what evidence says is true, what was actually
done, and that the differences between them are the work. Desired state,
observed state, execution state, evidence, Unknown, gap, contradiction and
reconciliation carry all of that.

`Claim` is the kernel's **carrier** for an assertion about state — the object
that holds a label and a tier. That is mechanism, and mechanism is what
"advanced" means here. A reader meets `Claim` the moment they work inside the
model and not before.

### The immediate consequence, which is a finding and not a success

Demoting `Claim` moved it into CG-23's advanced set, and CG-23 immediately
reported **two uses of `Claim` on `OVERVIEW.md`'s default path**. Those were
always there; the tier split is what made them visible.

**They are not edited.** `OVERVIEW.md` is act 4's digest subject, and editing
an artifact whose digest an unperformed act binds is a worse defect than the
one being corrected. They are reported, routed to the owner with the act, and
left.

### What explicitly does NOT change

- T-13's entry, its definition, and its owning authority are untouched. The
  term did not change; its **tier** did.
- Nothing in doctrine or any contract is affected. The tiering is a reading
  convention of a candidate registry.

---

## Change 4 — the default-path bound is measured, not asserted

### Current meaning

> **The bound is testable, and currently fails.** […] the default path
> additionally leans on *kernel*, *surface*, *evidence*, *workspace*, and
> *actuator* […] enforced mechanically by `check_governance.py` **CG-17** once
> the core set is owner-accepted, and reported until then.

Two defects. **CG-17 routes surface clauses and has nothing to do with
vocabulary** — the promise named the wrong check. And the list of leaks is a
frozen transcription of one sweep, which is the class this round is closing
everywhere else.

### Proposed meaning

The paragraph names **CG-23**, which is the check that actually performs the
sweep, and says to read its output rather than the sentence. The leak list is
replaced by two *classes* of leak — advanced terms CG-23 names, and terms with
no registry entry at all — with the current instances left to the check.

### And a correction to a previously published finding

**P-17 recorded that CG-23 reported two default-path leaks in `OVERVIEW.md`:
`Warrant` (T-17) and `Evaluation` (T-22). The `Warrant` finding was false.**

CG-23 counted case-insensitive **substrings**. `OVERVIEW.md`'s default path
contains "warranted work" and "the intent that warranted it" — the ordinary
verb, not the term. A word-boundary sweep of the same text finds **zero**
occurrences of `Warrant` and one of `Evaluation`. Verified by Python `re`
against the pre-drawer content:

```text
Warrant     0 hits
Evaluation  1 hit
Claim       2 hits
```

CG-23 now matches at word boundaries, and its false positives are handled the
way this battery handles every exemption: **an enumerated allowlist, printed
on every run**, keyed by (file, term). One entry exists — `README.md`'s "No
claim of alignment, convergence, or reconciliation", which is the ordinary
noun.

The cost of the change is stated in the check's own comment rather than
hidden: matching loosely reads English as jargon, matching tightly misses a
term used lowercase. The corpus's real leaks *are* lowercase running prose, so
the loose direction is the correct one, and the allowlist pays for it.

**A published finding was wrong, and this is the register that says so.** It
was published in `PENDING-OWNER-DECISIONS.md` P-17 and in the term-closure
report. Neither is corrected by this file alone; both are updated in the same
change.

---

## Change 5 — the core set stops being transcribed into the checker

### Current meaning

`check_governance.py`:

```python
CORE_TERM_IDS = ("T-01", "T-04", "T-07", "T-09", "T-11", "T-13",
                 "T-14", "T-15", "T-19", "T-20", "T-26", "T-27")
```

A hand-maintained second copy of the registry's core table, **inside the check
that polices the registry**. It went stale the moment the tier split moved,
and the check would have gone on policing the old split while reporting green.

### Proposed meaning

The core set is **parsed out of the registry's own core table** by
`_core_term_ids()`. Derived, it cannot disagree with the artifact it checks.

Two new selftest fixtures cover the failure the derivation introduces: a core
table that names an ID with no entry of its own, and a core table that does
not parse at all — which must be reported loudly rather than silently
reclassifying every term as advanced.

---

## Terms introduced / retired

**Introduced:** `Unknown` (**T-31**), owning authority **adopted**.
**Retired:** none. T-15's ID, entry and meaning are unchanged; only the core
table's mistaken use of it is corrected.
**Re-tiered:** `Claim` (T-13), core → advanced. A tier change is not a
retirement and the ID does not move.

---

## Downstream impact

Method: Python `re` sweeps, plus `check_governance.py` CG-16 (registry never
described as accepted) and CG-23 (default-path bound) run before and after.

| Artifact | Impact | Status |
|---|---|---|
| `check_governance.py` CG-23 | core set derived; matching changed to word-boundary; allowlist added | Done, 5 selftest fixtures |
| `PENDING-OWNER-DECISIONS.md` **P-17** | states a `Warrant` leak that does not exist | Corrected in the same change |
| `round-2026-08b/TERM-CLOSURE-REPORT.md` §9.3 | same false finding | Corrected in the same change |
| `README.md`, `.syzygy/intent/OVERVIEW.md` | now carry two `Claim` uses against an eleven-term core | **Reported, not edited** — `OVERVIEW.md` is act 4's digest subject |
| The registry's own §5 authority-coverage summary | gains T-31 | Updated |
| **No contract module** | the registry is candidate policy and cites contracts; it is cited by none | Verified by sweep |

**No act argument moves.** The term registry is not inside any act's digest
subject, which is why this delta could be applied in the same pass that froze
the contract bytes.

---

## Review

**Required class:** fresh-reader comprehension review — the registry's own
condition 5, applied to the registry.

**Reviewer:** commissioned as **RD-3**, a reader with no project context, given
the default path and the registry and asked to classify five real examples and
separate five adjacent pairs. It was explicitly *not* given this file.

**Verdict:** copied verbatim into
`PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md` and stored raw in `reviews/`.
