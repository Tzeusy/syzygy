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
with the reason it did not.

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

### P-33 and the owner packet (RD-49, RD-52)

| Finding | Why still open |
|---|---|
| RD-49 f3 *(blocking)* — arms (1e) and (2b), the two recommendations, are mutually inconsistent: a closed enumeration naming `wave-manifests/` does not admit `contracts/ACTIVE-CONTRACT-MANIFEST.txt`, which (2b) installs | real, and it changes what the recommendation *is*. Reconciling it is a substantive re-recommendation, and the arm space just grew by (1g); the packet should be re-derived once, not twice |
| RD-49 f4–f13 | the same re-derivation: quote RFC3-15's cell verbatim beside the proposed replacement, price each relocating arm with and without the reference repair, carry (1f) into the table, and correct the stale §7 item 11 and the register row |
| RD-52 f1 *(blocking)* — the one-sitting claim is false by the packet's own contents | recorded in the readiness report's conjunct 11 as a fail. Splitting the page into "settleable now" and "blocked, with the unblocking action" is the right fix and is a rewrite, not an edit |
| RD-52 f3 *(blocking)* — the exclusion list omits five open queue entries, three of them unperformed acts | the task router now names P-1 among the blocking acts, which closes the router's half; the packet's exclusion list is not yet reconciled against the queue's 31 open rows plus 5 acts |
| RD-52 f4–f16 | batched with the same rewrite |

### The route and the exercise (RD-53)

| Finding | Why still open |
|---|---|
| f7 *(remainder)* — no `--check` predicate fails when the route diverges from `FIRST-OPENSPEC-SEQUENCE.md` rows 1.1–1.6 | the clause list was repaired by hand this pass, which means the defect can recur silently. This is the most valuable single check still unbuilt |
| f8 *(material)* — pass criterion 3 is unfalsifiable, criteria 2 and 4 carry no threshold, and no criterion tests clause coverage | the exercise has now been administered once against these criteria. Changing them after a run and then quoting that run's grade would be exactly the "graded to taste" failure the exercise exists to avoid; the criteria should be revised **and the exercise re-administered** |
| f9 *(minor)* — the route report is stale (ten decisions, not eleven), drops "Cost" from its RFC8-18 gloss, and calls a one-level union a transitive closure | pending the same regeneration |

## What this register does not do

It does not claim the repaired findings are fixed correctly — only that
bytes moved for a stated reason. It does not grade the reviews. And it does
not close a single readiness conjunct: the answer to *"Is Syzygy ready to
author Capability 1 in OpenSpec?"* is unchanged, and it is **No**.
