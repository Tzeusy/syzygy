# Human clarity — what ten independent reviews found, and what changed

> **Non-authoritative round record.** The raw reviews in `reviews/` are the
> authority for what each reviewer said; verdict words below are **copied,
> never re-labelled**. Supersedes `../round-2026-08/FINAL-HUMAN-CLARITY-REVIEW.md`.

## The standard being tested

> A technically capable engineer unfamiliar with Syzygy can move from its
> north star to the exact contract governing one task without loading the
> whole corpus, learning thirty terms up front, resolving contradictory
> metadata, or relying on founder-local history.

Ten fresh-context sessions were commissioned, each given the artifacts and
the acceptance criteria and none given the authoring conversation. Nine ran
against the corpus as it stood; the tenth, RC-10, was commissioned last and
given the exact bytes act 1 would bind.

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
| RC-10 | Confirming review over the final bytes | **REVISE** |

**Not one CONFIRM.** That is the headline and it should not be softened: the
round asked ten independent readers whether this corpus is clear and correct,
and none of them said yes without qualification. Seven said REVISE — including
the one commissioned specifically to confirm.

The corpus is materially better than it was — the section below is not short.
But "improved" and "clear" are different claims, and only the first is
established.

## What the reviews found, and what happened to it

### Closed by a change, with the check that keeps it closed

| Finding | Reviewer | What changed |
|---|---|---|
| Act 3's install step named `topology/`, a directory that has never existed — the ceremony was unexecutable, and the link checker's history allowlist was absorbing a live instruction | RC-1 | Corrected to `topology-candidates/`. **CG-14** now classifies every ceremony path by declared role and found a second instance the same day |
| Owner-approved policy adopts an engineering bar no clone can read, pinned by a *date* rather than a digest — so a fresh engineer cannot determine this project's definition of done | RC-1 | `GOVERNANCE-SUBSTRATE-LOCK.yaml` pins five substrates to public commits, trees and per-file digests. **CG-19** checks that every pin is complete and well-formed and that its declared drift matches what the recorded digests actually say. Its first version did far less than this row originally claimed — see the correction below. The check also surfaced that the installed tree had drifted two commits past what D2 approved — P-26 |
| "Adopted doctrine cites a README glossary that does not exist" — asserted flatly in five tracked artifacts | RC-3 | **The finding itself was false.** The glossary exists at `doctrine/README.md:15`. All five corrected; the real, narrower defect is P-25 |
| The task-routing index publishes findings that are false, including a universal claim contradicted by a two-row counterexample | RC-1 | T-2 and T-4 retired as wrong-when-written. **CG-20** recomputes every load-map figure; eleven of eleven rows were stale |
| The adapter-author routing row is wrong in both directions and yields a packet incomplete against the package's own declared dependencies | RC-1 | Row corrected; recorded as T-5 |
| The dependency graph reported 20 asymmetric edges at every generation under a green drift check | RC-4 | `provides_to` derived from `depends_on`; asymmetry is now unrepresentable. **CG-13** checks dangling edges and the README-union invariant |
| Four dependency edges added on evidence that was not evidence — a boilerplate banner and a shape-parallel parenthetical read as reliances | RC-4 | All four reverted after independent re-verification |
| Mission Control has a prevention plane and no correction plane | RC-7 | RFC10-17…22 added; nine of eleven blocking seams addressed by clause text — seven fully, two partly, each unclosed part named in `MISSION-SAFETY-CLOSURE-REPORT.md` |
| The §14 coverage review's stated digest names a value RFC-0010 has never carried | RC-7 | Independently re-verified and corrected on the review, with the wrong value left visible |
| All eight context fixtures had drifted; two caught by hand | RC-6 | **CG-18** recomputes every fixture's digest and word count from its declared mandatory set, every run — 18 measurements across nine fixtures |
| `missing-declaration` cited as RFC2-24 #4 where #4 is `stale-beyond-currency-bound` | RC-4 | Corrected to #1; all 13 ordinal citations in the 32 contract modules swept, and the 20 across all candidate material outside `history/` and `reviews/` |
| RFC10-18 forbade only `completed`, so an executing party could avoid adjudication by parking in `blocked` indefinitely | RC-10 | Fixed at rev11a: the reached state now depends on whether effects have been applied — `blocked` with no applied effects, **`failed`** with them, so RFC10-19's duties fire |
| Twenty-one derived word counts inside act 1's digest set were stale — in the commit whose message said it corrected every stale derived value | RC-10 | Nineteen module rows and two prose figures corrected. **CG-21** now recomputes every package README row |
| The mission-safety closure report misdescribed four of the nine seams it reported closed, including a carve-out that occurs zero times in RFC-0010 | RC-10 | All four rows rewritten from the clause text; two seams restated as *partly* closed with the unclosed part named |
| **The evidence-adapter class had no fixture** — the set was seven-for-eight with fixture 2 double-counted. Twelve of RFC-0004's clause rows (RFC4-18…RFC4-29) were in no packet at all | RC-6 | **Fixture 9 written and placed.** CG-18 examines it (16 → 18 measurements) and was mutation-tested against it. It measures 24,025 words — the largest in the set and outside every budget band, which the fixture states rather than trims |
| **CG-19 was near-inert while three artifacts cited it as evidence.** It ran two predicates and returned `OK, 5 pins, 0 findings` under mutations that deleted every commit, deleted every digest, set a garbage commit id, set `visibility: private`, and rewrote the host to `.invalid` — 2 of 13 defect classes caught, both defeatable | RC-10, verified by mutation sweep this session | Rewritten to eight predicate families over a parsed lock: 57 evaluations, 28 fixtures, four of them negative. **Renamed** — "publicly resolvable" was a claim about the world an offline check cannot make; it is now "complete and well-formed; drift consistent". Identifier unchanged |

### Open, and honestly so

| Finding | Reviewer | Why it is still open |
|---|---|---|
| **There is no context compiler.** `context_load.py` measures a selection you have already made; every fixture's selection is hand-authored, while each says `Compiler: context_load.py` | RC-6 | Building a selector is application code, which this phase forbids. Stated plainly rather than routed around |
| **D3's `vision.md` insertion settles open question D4 by stipulation** | RC-7 | Closes by an owner ruling, not by text. Disclosed at D3 §6 with the reviewer's alternative — P-24 |
| RFC9-8(a) and RFC3-10/11/21 disagree about which plane an owner-gated registry belongs to | RC-4 | Needs a ruling, not an edit — P-22 |
| Two one-way constraints are stated in one contract and enforced in neither | RC-4 | `depends_on` drives loading and neither is a load obligation — P-21 |
| Three terms are cited as glossary-defined and defined nowhere: *actuator toolchain*, *ai-bootstrap toolchain*, *actuator* | RC-2, RC-3 | Defining them is a substantive doctrine amendment with its own review |
| Six of eight reader-map role rows exceed the 20,000-token decomposition trigger | RC-6 | Row *membership* is editorial and cannot be derived until task metadata exists (T-1) |

## The one thing that did not get better

**The confirming review did not confirm.** RC-10 was commissioned over the
exact bytes act 1 binds — the one gap every earlier review left open — and
returned **REVISE**, with findings that landed on this round's own work rather
than on inherited material: a live escape in a clause written *this round* to
close an escape, twenty-one stale derived values inside act 1's digest set,
and four misdescribed seams in the report that claimed the seams were closed.

All three are fixed and each fix carries a check. But the shape of the result
is what matters: **every one of those defects was introduced by the pass that
was correcting defects.** The corpus is not converging because it is being
reviewed once more; it is converging because each finding leaves behind a
mechanical check. There are eleven of those now (CG-11…CG-21) that did not
exist a round ago.

The residual is unchanged in kind, only smaller: the fixes RC-10 prompted have
themselves been read by no reviewer, and one of them edits a contract inside
act 1's digest set.

## Assessment against the standard

| Clause of the standard | State |
|---|---|
| Discover the north star | **Met.** README → OVERVIEW → `vision.md`, three hops, and the root README now routes an unfamiliar word to the only glossary |
| Understand the current state | **Met.** `PROJECT-STATUS.md` carries an as-of and cites the record that owns each row |
| Navigate to the exact authority for one task | **Partly.** Routing to a *contract* works; routing to a *packet* is hand-authored, and the one routing row a reviewer actually tested was wrong in both directions until this round |
| Act correctly without reading the whole corpus | **Met at the measured tasks.** Eight fixtures land at 10.8k–22.2k words against a ~121k whole-corpus path |
| …without thirty terms up front | **Partly.** The two-tier split exists; the registry defining it is a candidate with no owner act, and eight public terms have no adopted definition anywhere (P-17) |
| …without contradictory metadata | **Met, newly.** The dependency graph's two halves can no longer disagree; three derived views now recompute under checks |
| …without founder-local history | **Met.** No live artifact directs a reader to a founder-only path; the 35 remaining mentions are enumerated by class in `PUBLIC-CLONE-VERIFICATION-REPORT.md` — 34 records of history or evidence, and one deliberate provenance line that is immediately followed by the public substrate pin |

**Four met, three partly.** None of the three is met by writing more prose —
each needs an owner act (the term registry), a phase this project has not
entered (the compiler), or a review over the current bytes.
