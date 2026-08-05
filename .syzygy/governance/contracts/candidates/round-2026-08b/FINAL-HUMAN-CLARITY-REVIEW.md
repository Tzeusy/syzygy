# Human clarity — what nine independent reviews found, and what changed

> **Non-authoritative round record.** The raw reviews in `reviews/` are the
> authority for what each reviewer said; verdict words below are **copied,
> never re-labelled**. Supersedes `../round-2026-08/FINAL-HUMAN-CLARITY-REVIEW.md`.

## The standard being tested

> A technically capable engineer unfamiliar with Syzygy can move from its
> north star to the exact contract governing one task without loading the
> whole corpus, learning thirty terms up front, resolving contradictory
> metadata, or relying on founder-local history.

Nine fresh-context sessions were commissioned, each given the artifacts and
the acceptance criteria and none given the authoring conversation.

## The verdicts, copied

| Review | Scope | Verdict |
|---|---|---|
| RC-1 | Fresh-engineer comprehension — README to one task | **EXCEPTIONS** |
| RC-2 | Vision / Polaris north star | **REVISE** |
| RC-3 | Vocabulary | **REVISE** |
| RC-4 | Contract semantics and dependency closure | **REVISE** |
| RC-5 | RFC/OpenSpec boundary | **REVISE** |
| RC-6 | Context compiler and fixtures | **REVISE** |
| RC-7 | Mission-safety adversarial | 11 blocking seams; per-attack verdicts |
| RC-8 | Evidence and security | **EXCEPTIONS** |
| RC-9 | Public clone | **EXCEPTIONS** |

**Not one CONFIRM.** That is the headline and it should not be softened: the
round asked nine independent readers whether this corpus is clear and correct,
and none of them said yes without qualification. Six said REVISE.

The corpus is materially better than it was — the section below is not short.
But "improved" and "clear" are different claims, and only the first is
established.

## What the reviews found, and what happened to it

### Closed by a change, with the check that keeps it closed

| Finding | Reviewer | What changed |
|---|---|---|
| Act 3's install step named `topology/`, a directory that has never existed — the ceremony was unexecutable, and the link checker's history allowlist was absorbing a live instruction | RC-1 | Corrected to `topology-candidates/`. **CG-14** now classifies every ceremony path by declared role and found a second instance the same day |
| Owner-approved policy adopts an engineering bar no clone can read, pinned by a *date* rather than a digest — so a fresh engineer cannot determine this project's definition of done | RC-1 | `GOVERNANCE-SUBSTRATE-LOCK.yaml` pins five substrates to public commits, trees and per-file digests. **CG-19** checks resolvability. The check also surfaced that the installed tree had drifted two commits past what D2 approved — P-26 |
| "Adopted doctrine cites a README glossary that does not exist" — asserted flatly in five tracked artifacts | RC-3 | **The finding itself was false.** The glossary exists at `doctrine/README.md:15`. All five corrected; the real, narrower defect is P-25 |
| The task-routing index publishes findings that are false, including a universal claim contradicted by a two-row counterexample | RC-1 | T-2 and T-4 retired as wrong-when-written. **CG-20** recomputes every load-map figure; eleven of eleven rows were stale |
| The adapter-author routing row is wrong in both directions and yields a packet incomplete against the package's own declared dependencies | RC-1 | Row corrected; recorded as T-5 |
| The dependency graph reported 20 asymmetric edges at every generation under a green drift check | RC-4 | `provides_to` derived from `depends_on`; asymmetry is now unrepresentable. **CG-13** checks dangling edges and the README-union invariant |
| Four dependency edges added on evidence that was not evidence — a boilerplate banner and a shape-parallel parenthetical read as reliances | RC-4 | All four reverted after independent re-verification |
| Mission Control has a prevention plane and no correction plane | RC-7 | RFC10-17…22 added; nine of eleven blocking seams closed by clause text |
| The §14 coverage review's stated digest names a value RFC-0010 has never carried | RC-7 | Independently re-verified and corrected on the review, with the wrong value left visible |
| All eight context fixtures had drifted; two caught by hand | RC-6 | **CG-18** recomputes all eight, every run |
| `missing-declaration` cited as RFC2-24 #4 where #4 is `stale-beyond-currency-bound` | RC-4 | Corrected to #1; all 13 ordinal citations swept |

### Open, and honestly so

| Finding | Reviewer | Why it is still open |
|---|---|---|
| **There is no context compiler.** `context_load.py` measures a selection you have already made; every fixture's selection is hand-authored, while each says `Compiler: context_load.py` | RC-6 | Building a selector is application code, which this phase forbids. Stated plainly rather than routed around |
| **The evidence-adapter fixture class has no fixture** — the set is seven-for-eight with one double-count | RC-6 | A ninth hand-authored fixture would inherit the same limitation |
| **D3's `vision.md` insertion settles open question D4 by stipulation** | RC-7 | Closes by an owner ruling, not by text. Disclosed at D3 §6 with the reviewer's alternative — P-24 |
| RFC9-8(a) and RFC3-10/11/21 disagree about which plane an owner-gated registry belongs to | RC-4 | Needs a ruling, not an edit — P-22 |
| Two one-way constraints are stated in one contract and enforced in neither | RC-4 | `depends_on` drives loading and neither is a load obligation — P-21 |
| Three terms are cited as glossary-defined and defined nowhere: *actuator toolchain*, *ai-bootstrap toolchain*, *actuator* | RC-2, RC-3 | Defining them is a substantive doctrine amendment with its own review |
| Six of eight reader-map role rows exceed the 20,000-token decomposition trigger | RC-6 | Row *membership* is editorial and cannot be derived until task metadata exists (T-1) |

## The one thing that did not get better

**No confirming review is bound to the bytes now offered.** The reviews above
drove the changes; the changes moved the manifest twice; so with one exception
every review predates what an owner would accept. The exception is the review
commissioned over the final bytes, whose verdict is recorded in
`FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`.

This is not a process nicety. Six clauses of the Mission contract — the ones
that answer what happens after an agent has already done something
irreversible — were written in response to a review and have not been read by
one.

## Assessment against the standard

| Clause of the standard | State |
|---|---|
| Discover the north star | **Met.** README → OVERVIEW → `vision.md`, three hops, and the root README now routes an unfamiliar word to the only glossary |
| Understand the current state | **Met.** `PROJECT-STATUS.md` carries an as-of and cites the record that owns each row |
| Navigate to the exact authority for one task | **Partly.** Routing to a *contract* works; routing to a *packet* is hand-authored, and the one routing row a reviewer actually tested was wrong in both directions until this round |
| Act correctly without reading the whole corpus | **Met at the measured tasks.** Eight fixtures land at 10.8k–22.2k words against a ~121k whole-corpus path |
| …without thirty terms up front | **Partly.** The two-tier split exists; the registry defining it is a candidate with no owner act, and eight public terms have no adopted definition anywhere (P-17) |
| …without contradictory metadata | **Met, newly.** The dependency graph's two halves can no longer disagree; three derived views now recompute under checks |
| …without founder-local history | **Met.** No live artifact directs a reader to a founder-only path; the 31 remaining mentions are enumerated in `PUBLIC-CLONE-VERIFICATION-REPORT.md`, each a record of history or evidence |

**Four met, three partly.** None of the three is met by writing more prose —
each needs an owner act (the term registry), a phase this project has not
entered (the compiler), or a review over the current bytes.
