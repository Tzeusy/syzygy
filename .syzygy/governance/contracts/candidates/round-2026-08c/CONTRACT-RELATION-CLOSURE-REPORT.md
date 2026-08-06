# Contract relation seams — closure report

> **Non-authoritative round record.** The raw review is
> `reviews/RD-4-contract-relation-RAW.md` and is never edited. Where this file
> and the raw review disagree about what the reviewer found, **the raw review
> wins**. Verdict words are copied, not summarised.

## The commission and the verdict

A reviewer with no authoring context was given the two declared `constrains`
edges, the dependency index, the contract index, the nine fixtures and the
`depends_on` corpus, and asked whether the relation model is real: whether the
edges are clause-borne, whether the population is complete, and whether
anything downstream can see the relation at all.

**`VERDICT: REVISE`.** Seventeen findings, five of them **Blocking**.

The review's central sentence is worth quoting because it is the finding
underneath the other sixteen:

> Both declared `constrains` edges are wrong, and both correct ones are
> undeclared.

That is exactly what happened. This round authored a new relation, populated it
by reading prose, and got the direction wrong on both instances. The reviewer
found the two real edges by reading clauses instead.

## The five blocking findings

### F-1 · `RFC-0006 → RFC-0005` rests on no clause — **closed**

The declared edge cited RFC-0006's §5 Integration prose. Verified
independently: the restricting sentence sits at
`rfcs/RFC-0006-cross-surface-selection-query-drawer.md:454`, **more than fifty
lines past the last clause of the file** (RFC6-28, at line 387), inside a
section that defines nothing normative. No clause of either contract carries
the restriction.

**Edge removed.** Not softened, not re-justified — the evidence for it was
section prose, and section prose is not a clause.

### F-2 · `RFC-0008 → RFC-0007` is misdirected — **closed**

The declared edge pointed the wrong way. **RFC7-24 states the SDR-18 seam from
RFC-0007's own authority**, and RFC-0008 already declares `depends_on:
RFC-0007` — so the pair was bound in that direction twice, from the same
sentence, under two relation names.

**Edge removed.** The redundancy is now a check (see F-16).

### F-4 · `RFC-0005 constrains RFC-0006` (RFC5-3) was undeclared — **closed**

The real edge, clause-borne, and the *inverse* of the one that had been
declared. Now declared on
`rfcs/RFC-0005/admission-and-boundary.md`:

```yaml
constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]
constrains_source: RFC5-3
```

### F-5 · `RFC-0007 constrains RFC-0001/0004/0008` (RFC7-3) was undeclared — **closed**

Also clause-borne, and it reaches three contracts that declare `depends_on`
nothing in RFC-0007's direction. Now declared on
`rfcs/RFC-0007/narrative-contract.md`:

```yaml
constrains: [RFC-0001, RFC-0002, RFC-0004, RFC-0008]
constrains_source: RFC7-3
```

**Both declarations sit on the module whose clause states the restriction, and
neither package README carries one.** A README defines no clauses, so an anchor
declared there cannot be verified — and an unverifiable anchor is the same
failure as F-1 wearing a metadata key. `build_contract_index.py` unions the
module values to contract level rather than accepting a transcribed one.

### F-14 · The relation reached no consumer — **partly closed, and the open part is named**

RD-4's sharpest structural finding: `constrains` appeared in the human index
and nowhere else. Not in `05-CONTRACT-INDEX.yaml`, not in RFC11-4's enumerated
selection inputs, not in the load map, not in a fixture, not in a check.

**Closed:** `05-CONTRACT-INDEX.yaml` now projects `constrains` and
`constrains_source` (`build_contract_index.py:141-144`), and the anchor is
checked (below).

**Open, and this is the honest half:** **RFC11-4 still does not name
`constrains` among the deterministic selection inputs.** A conformant compiler
built against the contract as written today would not read this relation.
Amending RFC11-4 is a normative edit to act 1's digest subject, in the pass
that froze it. It is **owner decision packet P-21(c)** and the index says so on
its face:

> Until that clause changes, a conformant compiler would not read this
> relation at all.

### F-12 · Contract-granular `constrains` would blow three fixtures' budgets — **closed by design, not by exception**

RD-4 showed that if `constrains` meant *load the whole constraining contract*,
fixtures 4, 8 and 9 cross the proposed 20,000-token decomposition trigger to
deliver rules they already hold.

The resolution is the clause anchor. `constrains_source` names **one clause**,
not a contract, so the strongest defensible selector rule is *load the anchored
clause*, at a cost of tens of tokens. That rule lives in
`RELATION-MODEL-DECISION.md` as a **proposal**, because no clause states it —
which is F-15.

## The material findings

| # | Finding | Disposition |
|---|---|---|
| F-3 | The generated justification "acknowledged by no clause in the other" was false for row 2 | **Closed.** The generalisation is removed and the specific counter-example is stated in the index text |
| F-6 | The `constrains` table carried no denominator and no stated sweep | **Closed.** The index now states the method (two Python `re` sweeps, line-based and whitespace-normalised), states that a sweep by the party that authored the edges is the weakest evidence in the repository, and records **[Unknown]** whether a third edge exists |
| F-7 | `RFC-0009/interaction-parity-and-release.md → RFC-0007` rests solely on the shape-parallel parenthetical | **Open.** Recorded. Removing a `depends_on` from a module is a normative edit to act 1's subject |
| F-8 | Eleven non-README `depends_on` edges carry zero clause evidence; the citation test was scoped to 20 edges and the scoping was undisclosed | **Open, and the disclosure is made here.** The 20-edge scoping was real and undisclosed. Eleven edges remain evidence-free, three of them RFC-0011's. **P-21(b)** |
| F-9 | `RFC-0006 cites RFC-0003` rests solely on the universal status banner | **Open.** This is verification rule 5 — *a citation is not a reliance* — firing on a derived relation. The `cites` column is explicitly not a load obligation, so the cost is a noisy row, not a wrong packet |
| F-10 | Four `cites` edges rest solely on the shape-parallel parenthetical | **Open.** Same class as F-9 |
| F-11 | No guard against clause identifiers inside fenced code blocks | **Open, latent.** No current false edge traces to it; swept this session and found none. Recorded rather than fixed, because the fix changes the derivation for every relation at once |
| F-13 | The index asserted transitive mandatory loading that none of the nine fixtures implements | **Closed.** The assertion is removed — it was part of the same non-authoritative-file-stating-normative-rules defect as F-15 |
| F-15 | The "Context Compiler behaviour" column stated selector obligations no clause carries, in a file whose banner reads *nothing here may be cited as authority* | **Closed.** Column removed. The index now says in prose that what a selector should do is deliberately not stated there, and names the defect: *the defect this package keeps re-acquiring, appearing inside the repair for it* |
| F-16 | The redundancy predicate was one-directional and would have caught F-2 | **Closed.** `coincident_edges()` now reports `A constrains B where A depends_on B` — as a **signal, not a defect**, because the coincidence is legitimate when the constraint is narrower than the dependency |
| F-17 | P-21(a) is PENDING with two alternatives offered; one has been installed into candidate front matter and the register does not record it | **Open, and it is the process finding.** Recorded in `PENDING-OWNER-DECISIONS.md`. Installing one arm of an open owner question into candidate metadata, then leaving the register describing the choice as untaken, is how a pending decision becomes a fait accompli |

## What now checks the anchor

`build_dependency_index.py`'s `asymmetries()` carries three predicates:

1. **dangling** — `depends_on` names a contract that does not exist;
2. **unanchored `constrains`** — the module declares `constrains` and its
   `constrains_source` clause is **not defined in that module**;
3. **dangling `constrains`** — the target contract does not exist.

Predicate 2 is the one that exists because of this review. It is the mechanical
form of "read the clause, not the section prose": had it existed when the two
wrong edges were authored, F-1 would have failed immediately, since RFC-0006's
§5 prose defines no clause to anchor to.

**Mutation-tested this session**, per verification rule 6: moving
`constrains_source: RFC5-3` to a clause id not defined in
`admission-and-boundary.md` makes the check report the asymmetry; restoring it
clears it.

## What this closes and what it does not

**Closed:** both wrong edges removed, both right edges declared and anchored, a
check that can tell the difference, the relation projected into the machine
index, three false or overreaching statements removed from a non-authoritative
file, and a redundancy signal that would have caught the misdirection.

**Not closed, and each is an owner item rather than an agent's call:**

- **RFC11-4 does not name `constrains`.** The relation is declared, projected
  and checked, and no clause tells a selector to read it. **P-21(c).**
- **Eleven `depends_on` edges have no clause evidence.** **P-21(b).**
- **Completeness is [Unknown].** Two edges were found by the party that
  authored the wrong ones. The population is a sweep, not a proof.
- **F-17's process defect** — an arm of a pending decision already installed.

**The relation model is now honest about what it is: two clause-anchored edges,
a check that verifies the anchor, and a stated Unknown about whether there is a
third.** It is not yet a relation any specified component reads.
