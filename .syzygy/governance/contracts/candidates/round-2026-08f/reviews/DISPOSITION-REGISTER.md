# Round-2026-08f — disposition register

> **This file is the repair session's account of the reviewers' findings.
> It is not a review and it never edits one.** The raw files beside it are
> the reviewers' bytes; where this register and a raw file disagree about
> what a reviewer said, the raw file wins. Where this register says
> *repaired*, the repair is **unreviewed** — a repair session may not
> confirm its own repairs, and every row marked repaired needs a fresh
> exact-package review before it counts as more than a change.
>
> Dispositions are `repaired` · `open` · `declined (with reason)`. There is
> no "acknowledged" and no "will fix": a finding is closed by bytes or it is
> open.

## The reviews

| Review | Subject | Verdict (copied exactly) |
|---|---|---|
| RD-47 | structured launch-record schema and validator | `REVISE` |
| RD-48 | launch-policy v2.0 semantic preservation | `REVISE` |
| RD-49 | P-33 semantic installation options | `REVISE` |
| RD-50 | default-path human clarity | `CONFIRM WITH EXCEPTIONS` |
| RD-51 | specification-acceptance and shape-to-spec impact policies | `REVISE` |
| RD-52 | owner-packet one-sitting comprehension | `REVISE` |
| RD-53 | Capability 1 task route and outline exercise | `REVISE` |

All seven were dispatched against frozen bytes at commit `e2efda6`, in fresh
contexts, each given only its subject, its governing references and its
acceptance criteria. All seven are the **same model family as the corpus
authors**, so under charter §2.15 every one supports repair and **none is
the formal launch administration**.

## Repaired in this pass

| Finding | What it was | What changed |
|---|---|---|
| RD-50 f1 *(blocking)* | eight blank lines split the open-decisions table into nine fragments, so twenty of twenty-two launch-critical rows rendered as loose pipe-delimited text | the eight blank lines removed; the open table is one block of 31 rows |
| RD-49 f1 *(blocking)* | the P-33 arm space omitted the cheapest lawful arm | arm **(1g)** added with its true cost — 87 dangling in-tree path strings — and its price in confirmations, which is zero |
| RD-49 f2 *(blocking)* | "there is no arm that preserves the current confirmations" was false, unlabelled, and the packet's headline | corrected in the packet with the digest derivation re-verified, and in all three places it had propagated: the owner packet, `AGENTS.md`, and this round's readiness report |
| RD-52 f2 *(blocking)* | the owner packet said six facets and demoted Mission-ready; the linked packet says seven and requires the seventh to render its deferral | the row restated to seven, quoting rule 3, with the operational difference named |
| RD-53 f1 *(blocking)* | the Capability 1 route omitted RFC-0006 — the anti-rollup ground, the parity clauses, and RFC6-17, which three loaded modules cite and never restate | RFC-0006 added to the load set with RFC6-13/14/17/18/19/26; the RFC8-18/8-19 entry re-scoped to cost, which is what those clauses say |
| RD-53 f2 *(blocking)* | RFC3-16(a), the provenance predicate all five loaded modules defer to, had no defining module in the load set | `RFC-0003/governance-homes-and-owner-acts.md` added; `RFC3-16` named |
| RD-53 f3 | a selftest fixture named "a deferred-wave module in the load set detected" mutated `clauses` and asserted a predicate two cases above it — no deferred-leak check existed | a real predicate added (routed path, clause home, and declared module dependency), the fixture repointed at it, and a second fixture added for the clause-home direction |
| RD-53 f4 | "each verified open in the pending queue" — the check tested row presence anywhere in the file, and accepted four executed rows | openness scoped to the queue's own sections: rows under a "Resolved…" heading and rows carrying `**Executed.**` are refused, with two fixtures in the rejecting direction |
| RD-53 f5 | the blocking list omitted the wave acts and the three rulings that ride them, and carried two decisions the queue assigns to a later gate | P-1, P-21, P-22, P-28 added; P-34 and P-35 moved to a separately labelled later-gate line |
| RD-53 f6 | four counts asserted under the words "Counts computed, never asserted" | the fixture count, the routing-fixture count, the Waves A+B module count, the facet sweep and both CC clause ranges are now derived at generation |
| RD-53 f7 *(partly)* | the route named 10 of the 18 clauses the project's own two Capability 1 artifacts name | RFC1-3, RFC3-1, RFC3-5, RFC3-6, RFC3-9, RFC5-3 added, with RFC-0005 loaded. **The `--check` predicate RD-53 asks for — fail when the route diverges from `FIRST-OPENSPEC-SEQUENCE.md` — is not built; that part is open** |
| RD-53 f10 | the route told an author neither that the corpus is unaccepted nor where its own scope is stated | `FIRST-OPENSPEC-SEQUENCE.md` and `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` added to the load set; the note now states that every routed clause is candidate |
| RD-52 f7 | the P-34 packet's "verify before acting" command cannot run from the directory the packet sits in | the block now changes to the repository root first, and says why |

Every repair above was made **after** its review returned, never during one:
no subject moved while a reviewer was reading it.

## Open — recorded, not repaired

Nothing here is dismissed. Each row is a finding this pass did not close,
with the reason it did not. *(One subsection — RD-50's, added later — lists
that review's findings **in full**, repaired rows included, because the
defect being corrected there was an incomplete list. Its rows carry their
own dispositions.)*

### The launch instrument (RD-48)

| Finding | Why still open |
|---|---|
| f1 *(material)* — §4's clauses name `Owner deferral decision:` and `Deferred count:`, fields no v2.0 record has, and cite `LG-*` checks that never run on a v2.0 record | §4 is byte-identical across v1.18→v2.0, and that byte-identity is a load-bearing claim of the v2.0 delta. Amending §4 is a semantic change to the instrument and needs its own version, delta and review — it cannot be slipped in beside a repair batch |
| f2 *(material)* — the computed formula has a sixth core conjunct §4 does not carry, and the report labels all six "§4 conjuncts" | same reason. The conjunct is strictly more conservative than §4 and is grounded in §3's E3 rule, so the instrument is not looser than it reads; it is differently *worded* than it computes, which is exactly what an amendment is for |
| f3 *(material)* — the gate verdict word `NOT READY` exists nowhere in §1–§8 | same. It is emitted by the tool and printed on every failing report, but the instrument that owns readiness semantics no longer defines it |
| f4 *(material)* — §7's new clause "it names no Syzygy artifact" is false of the schema, and the portable core omits both tools | same |
| f5 *(material)* — §5 delegates the normative check enumeration to a tool docstring, and that docstring's `LA-13` sentence is already wrong | the docstring half is repairable without an amendment; the delegation half is not. Both are held together so the amendment carries one coherent change |
| f6–f11 *(minor)* | batched with the amendment above, per verification rule 10: the instrument's bytes should move once, not five times |

### The validator and renderer (RD-47)

| Finding | Why still open |
|---|---|
| f1 *(material)* — LA-2/LA-3 skip themselves when the §8 parameter will not parse, so a record can declare all six waves required and a nonsense version and validate clean | a real defect with a clear fix (distinguish absent from empty; make absence an error). Not made this pass because it changes the validator's error surface and the validator's own review is only hours old — the batch belongs with f4 and f6 |
| f2 *(material)* — reviewer free text renders as raw Markdown, so a record computing NOT READY can display a forged `GATE VERDICT: READY FOR …` above the real one | same batch. The fix (fence or blockquote every free-text field, and refuse `GATE VERDICT` inside one) is small and needs its own fixtures |
| f3 *(material)* — the §6 New-findings column is bound to a CLI flag the renderer does not have, and renders "n/a (no prior record)" when a prior record is declared | this is the VIS-2 finding in the set: an affirmative claim of absence where the honest answer is Unknown |
| f4 *(material)* — `PENDING-OWNER-DECISIONS.md`, the queue of decisions *not* made, is accepted as a deferral warrant through the path branch | same batch |
| f6 *(material)* — the schema audit rejects unimplemented keywords and never requires an object schema to close, so deleting one `additionalProperties` re-opens the claimed-verdict route | same batch, and the most important of the five: it is the single guard the "a record cannot claim its verdict" property rests on |
| f5, f7–f12 *(minor)* | batched |

### The policies (RD-51)

The full finding set is in the raw file; none is repaired. The
specification-acceptance policy's bytes are meant to be frozen **after P-40
is ruled** and reviewed fresh at that point, so repairing them now would
freeze the wrong bytes. The shape-to-spec impact policy is one day old and
its first review is this one.

> **Superseded 2026-08-13 — this paragraph was wrong, and the twenty
> findings are now dispositioned.** The reasoning above conflated **repair**
> with **freeze**: repairing a candidate does not freeze it, and only the
> freeze had to wait on P-40. Written as a reason not to act, it left four
> blocking findings — including one clause weakening an owner-approved rule
> — carried for two days as "not repaired, by design."
>
> All twenty findings are dispositioned in
> `../../round-2026-08g/reviews/DISPOSITION-REGISTER.md` (15 repaired, 4
> repaired in part, 1 open and deliberately so). The repair account is
> `../../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`. The
> freeze and the combined review still wait on P-40, which is the only part
> of the paragraph above that was correct.

### P-33 and the owner packet (RD-49, RD-52)

| Finding | Why still open |
|---|---|
| RD-49 f3 *(blocking)* — arms (1e) and (2b), the two recommendations, are mutually inconsistent: a closed enumeration naming `wave-manifests/` does not admit `contracts/ACTIVE-CONTRACT-MANIFEST.txt`, which (2b) installs | real, and it changes what the recommendation *is*. Reconciling it is a substantive re-recommendation, and the arm space just grew by (1g); the packet should be re-derived once, not twice |
| RD-49 f4–f13 | the same re-derivation: quote RFC3-15's cell verbatim beside the proposed replacement, price each relocating arm with and without the reference repair, carry (1f) into the table, and correct the stale §7 item 11 and the register row |
| RD-52 f1 *(blocking)* — the one-sitting claim is false by the packet's own contents | recorded in the readiness report's conjunct 11 as a fail. Splitting the page into "settleable now" and "blocked, with the unblocking action" is the right fix and is a rewrite, not an edit |
| RD-52 f3 *(blocking)* — the exclusion list omits five open queue entries, three of them unperformed acts | the task router now names P-1 among the blocking acts, which closes the router's half; the packet's exclusion list is not yet reconciled against the queue's 31 open rows plus 5 acts |
| RD-52 f4–f16 | batched with the same rewrite |

### The default path (RD-50)

*Added 2026-08-11. **This section was missing**, and its absence was the
register's own worst finding: RD-50 raised eleven findings, exactly one
(f1) appeared in the repaired table above, and the other ten appeared
nowhere — while this file's header says "Nothing here is dismissed". Ten
findings were dismissed by omission. They are dispositioned below.*

| Finding | Disposition |
|---|---|
| f1 *(blocking)* — the decisions register renders as broken Markdown for 20 of 22 open rows | **repaired** — see the table above |
| f2 *(material)* — `candidates/README.md` and `FIRST-OPENSPEC-SEQUENCE.md` say the waves await fresh exact-package reviews, contradicting `PROJECT-STATUS.md`, and carry no precedence banner | **repaired 2026-08-11** — both now carry the "the owning record wins and this page is stale" banner and a dated state line; the two stale sentences are corrected in place, each naming RD-50 f2 and what it replaced |
| f11 *(minor)* — the sealed packet binds a commit behind HEAD, so a reviewer verifying at HEAD finds a mismatch and must decide for themselves that it does not matter | **repaired 2026-08-11** — the packet's §2 now says the commit is expected to advance, that the four digests are what bind, and what a real mismatch looks like |
| f3 *(material)* — the P-34 queue row asks the owner to approve **v1.18**, a version that no longer exists | **open** — the fix RD-50 prescribes (cite the instrument's header rather than writing a version number into the row) is one line, but it sits inside the same table cell f6 says must be rewritten. Editing that cell twice is how a 1,283-word cell got built; it moves once, with f6 |
| f6 *(material)* — the P-34 cell is ~1,283 words of v1.4→v1.18 litigation in a single table cell; the register makes the reader read the history it exists to spare them | **open** — this is charter §6.2's bounded P-34 packet, which was not written. It is a rewrite of one cell into a packet file plus a three-column row, with the chronology moving to `decisions/launch-gate/HISTORY.md`, and it carries f3 with it |
| f5 *(material)* — `doctrine/v1.md`, the only file that says what the software would do, is not linked from README's "Start here" | **open** — a one-line addition to a doctrine-adjacent routing list, and the front door is exactly where an unreviewed "small" edit is expensive. Batched with f7/f9/f10 as one front-door pass with its own review |
| f4 *(material)* — the 48-check battery reports 0 FAIL and catches none of f1–f3; a reader told "the battery is clean" over-reads it | **open** — the prescribed currency check (any file asserting a wave/gate state must match `PROJECT-STATUS.md` or carry the precedence banner) is a new check family with its own fixtures. It is the most valuable item in this section, because f2 recurring silently is the default outcome without it |
| f7 *(minor)* — `decisions/` has no `README.md`, though README links the directory as a destination | **open** — front-door pass |
| f8 *(minor)* — terms used before definition: `act`, `argument`, `wave`, `offer`, `P-nn`, `RD-nn`, `E1…E6` have no glossary anywhere on the routed path | **open** — process vocabulary has no home; the candidate `TERM-REGISTRY.md` covers product terms only. Naming its home is a decision, not an edit |
| f9 *(minor)* — `OVERVIEW.md` sets a riddle ("Doctrine has a name for that corpus") 131 lines from the answer | **open** — front-door pass; `OVERVIEW.md` is a candidate awaiting its own owner act, so its bytes should move once |
| f10 *(minor)* — a 2,059-line process instrument and the launch packet sit in the repository root, unmentioned by README | **open** — moving either changes paths that other artifacts and the sealed packet cite by name. Naming them in README's authority table is the cheap half and belongs to the front-door pass |
| f12 | not a defect — RD-50 recorded zero marketing language across the front door as a positive finding. Nothing to dispose |

### The route and the exercise (RD-53)

| Finding | Why still open |
|---|---|
| f7 *(remainder)* — no `--check` predicate fails when the route diverges from `FIRST-OPENSPEC-SEQUENCE.md` rows 1.1–1.6 | the clause list was repaired by hand this pass, which means the defect can recur silently. This is the most valuable single check still unbuilt |
| f8 *(material)* — pass criterion 3 is unfalsifiable, criteria 2 and 4 carry no threshold, and no criterion tests clause coverage | the exercise has now been administered once against these criteria. Changing them after a run and then quoting that run's grade would be exactly the "graded to taste" failure the exercise exists to avoid; the criteria should be revised **and the exercise re-administered** |
| f9 *(minor)* — the route report is stale (ten decisions, not eleven), drops "Cost" from its RFC8-18 gloss, and calls a one-level union a transitive closure | pending the same regeneration |

## Not a reviewer's finding — three sites the reviews' own arrival made false

*Added 2026-08-11, from a sweep run when the charter was audited section by
section. No reviewer raised these; obtaining RD-47 and RD-48 is what made
them false, and the pass that obtained them did not sweep for their
consequences. Recorded here because this is where a reader looks for what
moved after the reviews.*

| Site | What it said | What changed |
|---|---|---|
| `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` — the **P-34 owner packet** | *"Two reviews are required … and neither has been obtained … Status 2026-08-11: not dispatched"*, with two `[Unknown]` verdict rows, and option (a) recommended *"only after the two reviews return"* | both verdicts recorded as `REVISE` with their raw paths, dates and frozen commit; a one-line summary of what each found; option (a)'s condition shown as met in letter and failed in substance; option (c) *amend first* now carries the recommendation and the reviews' own change list. **This was the worst of the three** — the owner-facing packet for P-34 told the owner nobody had looked |
| `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` §9 | *"The two v2.0 reviews. They have not been obtained"* | replaced with what they returned and why it matters to an administrator, kept inside §5's withholding rule so the disclosure does not become a channel for the reviewers' judgments |
| `round-2026-08f/FINAL-CAPABILITY-1-READINESS-REPORT.md` conjunct 7 and step 7 | the conjunct said RD-48 confirmed *"the computed formula matches §4 conjunct for conjunct"* — **the reverse of RD-48 finding 2**, which measured a sixth computed conjunct §4 does not carry. The step list still said *"obtain the two v2.0 reviews"* | both corrected, the conjunct naming what RD-48 actually confirmed (no question, verdict word or trend column weakened) beside what it actually found |

**Denominator.** Swept every tracked `.md` outside the frozen review lane
for *"not been obtained"*, *"not yet been obtained"*, *"two required
reviews"* and *"two v2.0 reviews"*; four hits in three files, all above,
all resolved. `[Observed]` for the sweep; a sweep over phrasings is only as
good as its phrase list, so this is not a claim that no fourth site exists.

## What this register does not do

It does not claim the repaired findings are fixed correctly — only that
bytes moved for a stated reason. It does not grade the reviews. And it does
not close a single readiness conjunct: the answer to *"Is Syzygy ready to
author Capability 1 in OpenSpec?"* is unchanged, and it is **No**.
