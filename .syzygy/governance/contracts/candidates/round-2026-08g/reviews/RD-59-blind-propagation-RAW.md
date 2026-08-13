# RD-59 — blind administration of shape-to-spec propagation fixture 2

> **Provenance banner, added by the recording session — everything below the
> rule is the administrator's raw output, copied verbatim and unedited.**
>
> | | |
> |---|---|
> | **Role** | the blind exercise CC-IMPACT-7 requires — *"a path that has never been run is a plan, not a process"*. **Not a review**: no artifact was judged, and no verdict word is claimed |
> | **Dispatched** | 2026-08-13 |
> | **Subject** | `../SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md`, frozen |
> | **Subject sha256** | `685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0` — the digest CC-IMPACT-7 names |
> | **Materials** | that one file, and nothing else. The administrator was forbidden the answer key, both policy candidates, the semantic delta, every review tree, the predecessor fixture, and any repository-wide search |
> | **Context** | fresh |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** |
> | **Blindness** | structural — the golden result lives in a separate file. The administrator's own confirmation section states one file was opened, and names it |
> | **Result** | **PASS** on all three of the answer key's criteria. Graded in `DISPOSITION-REGISTER.md` |
>
> **This exercise satisfies nothing by act.** CC-IMPACT-7 is a candidate
> clause and binds nothing until P-42. The run is evidence that the path can
> be walked, not that it is in force.

---

## Method

**Order of sweep.**

1. **Fixed the change set.** Three identities amended by one logical change: `RFC6-19` (accepted contract clause), `OD-2` (mock owner decision), `CC-PROV-5` (approved craft policy clause). No doctrine rule and no other clause is amended.
2. **Pass 1 — declaration match (reverse reference).** For each of the sixteen requirements, matched the changed identities against every field of its CC-SPEC-2 declaration (`doctrine`, `contracts`, `policies`, `decisions`, `parent_requirements`; absent fields = empty list). Match on exact identifier, discriminating sibling identifiers (`OD-1` vs `OD-2`; `RFC6-13`/`RFC6-18`/`RFC6-19`; `CC-PROV-5` vs `CC-TEST-6`).
3. **Pass 2 — consumption match (one hop through the mock authority table).** For each requirement *not* matched in pass 1, asked whether an identity it *does* declare is itself defined in terms of a changed identity, using the fixture's stated mock content as the whole of what those authorities say. This is the pass that string-matching clause IDs cannot do, and it is what moves `FAC-3` into `affected`.
4. **Pass 3 — inheritance.** For requirements whose only declaration is `parent_requirements`, took the disposition of the parent as the disposition of the child, then checked the child's own statement for an independent tie.
5. **Pass 4 — disposition of the residue.** For each remaining requirement, asked what *positively* establishes untiedness rather than merely the absence of a matched string. Where the only available answer was "the identifier does not appear," and the requirement's *subject matter* is nonetheless governed by a changed identity, I routed it to `undecidable` rather than to `explicitly unaffected`, per the fixture's instruction.

**What this method can decide.** Declaration ties (exactly, from the corpus). One-hop consumption ties where the fixture states the consuming authority's content. Subject-matter disjointness between a requirement's governing identity and each changed identity. Inheritance down a `parent_requirements` edge.

**What this method cannot decide.** (a) Ties that would require a second or deeper hop through authority content the fixture does not state — the mock authority table is one line per identity, so any edge not visible in that line is invisible to me. (b) Whether a tie, once established, *changes the requirement's observable behavior*; I report tie, not magnitude. (c) Anything requiring implementation structure (branch granularity, view internals), because no implementation exists in the fixture. (d) Whether the corpus's authority list is complete — I have no reverse index, only the sixteen declarations plus the eleven-row authority table.

## Population

**16.** Counted by enumerating the five mock specification tables and summing their rows: SPEC-REG 4 (`REG-1…4`) + SPEC-FACETS 4 (`FAC-1…4`) + SPEC-COST 3 (`COST-1…3`) + SPEC-STATUS 3 (`STA-1…3`) + SPEC-ENTRY 2 (`ENT-1…2`) = 16, which agrees with the fixture's stated "sixteen mock requirements." Every requirement below appears in exactly one of the three sets; 7 + 8 + 1 = 16.

## Affected

| Requirement | What ties it | Changed identity |
|---|---|---|
| FAC-1 | Declaration, `contracts: [RFC6-19]` — the requirement *is* "folds according to the folding rules," and the folding rules gained a prohibition | `RFC6-19` |
| FAC-2 | Declaration, `contracts: [RFC6-19]` — and the disclosed fold count is computed over a fold whose membership rule narrowed | `RFC6-19` |
| FAC-3 | **Consumption, not declaration.** Declares `RFC6-18`, whose stated content is "a selection resolves to exactly one fact set, whose facets are those *the folding rules produce*." The folding rules changed, so the fact set FAC-3 renders changes | `RFC6-19` (via `RFC6-18`) |
| REG-4 | Declaration, `policies: [CC-PROV-5]`. REG-4 is a *summary* over runs, so the new aggregate-disclosure limb plausibly bites as well as the `Unknown` limb | `CC-PROV-5` |
| COST-1 | Declaration, `policies: [CC-PROV-5]`. Tie is by declaration; note that COST-1 is single-run, so the new aggregate limb may add nothing — that is a magnitude question, not a tie question | `CC-PROV-5` |
| COST-2 | Declaration, `policies: [CC-PROV-5]`. Squarely hit: a rollup over runs must now also disclose the count of constituents whose cost is absent | `CC-PROV-5` |
| STA-1 | Declaration, `decisions: [OD-2]` — the requirement draws its reason from the closed vocabulary, and one value in that vocabulary was renamed | `OD-2` |

Affected requirements span **four** specifications (SPEC-FACETS, SPEC-COST, SPEC-REG, SPEC-STATUS).

## Explicitly unaffected

| Requirement | Reason | Method that established untiedness |
|---|---|---|
| REG-1 | `VIS-2` and `RFC3-5` are both unamended; `RFC3-5` governs the closed *declaration field set*, disjoint from folding, cost rendering and status vocabulary | Declaration match (no hit) **plus** subject-matter disjointness read off the authority table: neither declared identity's stated content mentions folding, aggregates or reason vocabulary, so no one-hop consumption edge exists |
| REG-2 | `RFC3-9` (adapter declaration at registration) is unamended and disjoint | Declaration match + one-hop consumption check against the stated content of `RFC3-9` |
| REG-3 | Declares `OD-1`, **not** `OD-2`. Only `OD-2` was amended. `RFC1-3` (consent before read) is unamended | **Sibling-identifier discrimination** — the discriminating fact is that the change set names `OD-2` alone — plus content disjointness (`OD-1` = consent at registration; `OD-2` = status-reason vocabulary; no overlap in the stated content) |
| STA-2 | Declares `OD-1` and `VIS-2`; neither amended. Its subject (the as-of instant) is disjoint from the renamed vocabulary value | Sibling-identifier discrimination + content disjointness, same as REG-3 |
| STA-3 | Its only declaration is `parent_requirements: [SPEC-STATUS/STA-2]`, and STA-2 is unaffected | **Inheritance**: disposition propagates down the parent edge; then an independent check of STA-3's own statement (rendering the as-of instant beside the status) for a tie to any changed identity — none, since the amendment to `OD-2` touches the *reason* vocabulary, not the instant |
| FAC-4 | Declares `RFC6-13` (one truth, two consumers), which is unamended | **Invariance argument**, not mere absence of a string: `RFC6-13` constrains the *agreement* between two renderings, quantifying over the relation and not over the content of the computation. The `RFC6-19` amendment changes what the one computation produces; both consumers still read that one computation, so the agreement obligation is satisfied before and after and its required observable behavior is unchanged. (If the grading convention counts any downstream-content change as a tie, FAC-4 would move to `undecidable`; I record the method so the disagreement is locatable.) |
| ENT-1 | `RFC7-39` (fixed human entry location) unamended and disjoint | Declaration match + content disjointness |
| ENT-2 | `VIS-5` unamended; **no doctrine rule is in the change set at all** | Declaration match + a set-level check: the change set contains one contract clause, one owner decision, one craft clause, and no doctrine rule — so every doctrine-only declaration is untied by construction |

## Undecidable

| Requirement | Why the sweep could not settle it | What would settle it |
|---|---|---|
| COST-3 — "The cost view's absence branch is covered by a test" | It declares `CC-TEST-6`, which is unamended — so pass 1 says untied. But its *subject* is the cost view's absence behavior, and that behavior is defined by `CC-PROV-5`, which **was** amended: an aggregate must now additionally disclose the count of absent constituents. Whether that new disclosure is part of "the absence branch" already covered, or a distinct branch that `CC-TEST-6` obliges a further test to cover, turns on branch granularity — a fact about an implementation that does not exist and about `CC-TEST-6`'s definition of a branch, neither of which the fixture states. Per the fixture's own rule, "does not declare the changed identity" is not a sufficient method here, so this goes to `undecidable`, not to `explicitly unaffected` | (a) The full text of `CC-TEST-6` — specifically whether "absence and Unknown branches" is enumerated per rendered behavior or per view; or (b) a ruling from the spec author / owner on whether the amended `CC-PROV-5` introduces a distinct absence branch in the cost view; or (c) an implementation whose branch structure could be inspected |

## Wholly unaffected specification(s)

**SPEC-ENTRY.** Both of its requirements (`ENT-1`, `ENT-2`) are in the explicitly-unaffected set, and neither has any consumption or inheritance edge to a changed identity.

No other specification is wholly unaffected: SPEC-FACETS (FAC-1/2/3), SPEC-COST (COST-1/2), SPEC-REG (REG-4) and SPEC-STATUS (STA-1) each carry at least one affected requirement. SPEC-COST additionally carries the sole undecidable requirement, so it is not clean in either direction.

## What the fixture did not give me

- **The text of `CC-IMPACT-2` and `CC-IMPACT-3`.** I was told to run the CC-IMPACT-2 sweep and report the CC-IMPACT-3 output, but the fixture states neither clause. I worked from the four-set block the fixture prints in "Your task," which I treated as the operative definition. If CC-IMPACT-3 requires fields beyond the four sets (severity, disposition, required action per requirement), those are absent here.
- **A definition of "affected."** Tie-by-declaration and change-in-required-behavior are not the same predicate. `COST-1` (single-run, declares `CC-PROV-5`, but the amended limb is about aggregates) is the case where the two predicates can diverge; I resolved on tie and flagged it.
- **The CC-SPEC-2 field list.** The fixture says "six fields" but names only five in the tables (`doctrine`, `contracts`, `policies`, `decisions`, `parent_requirements`). A sixth field exists and I do not know what it holds; if it can carry a reference, my declaration sweep is incomplete by exactly that field.
- **`CC-TEST-6`'s granularity of "branch."** This is the single missing fact that produces the undecidable case.
- **Any content for `VIS-1`, `VIS-2`, `VIS-5`** beyond "as adopted." I did not import the real doctrine text; instead I relied on the set-level observation that no doctrine rule is in the change set, which makes their content unnecessary for this sweep.
- **A forward/reverse citation index among the authorities.** I have one line of content per identity and no map of which authority cites which. All consumption edges I found (`RFC6-18` → `RFC6-19`) had to be read out of that prose. A consumption edge that exists but is not visible in the eleven-row table would be invisible to this sweep — including any edge into `RFC6-13`, which bears directly on the FAC-4 disposition.
- **Whether `OD-2`'s "rename" is a change of identifier only or of meaning.** STA-1 is affected either way, so this did not change the set assignment, but it is the difference between a mechanical string update and a semantic re-derivation of the requirement.
- **Whether REG-4's "registration summary" is an aggregate in `CC-PROV-5`'s sense.** REG-4 is affected by declaration regardless; this only affects which limb of the amendment applies.
- **No completeness guarantee on the corpus.** I have no way to establish that these sixteen requirements are all the requirements, or that these eleven identities are all the authorities they rely on. My denominator is the fixture's assertion, not a measurement I could take.

## Confirmation

I opened **exactly one file**: `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md`.

I did not open the answer key, any file under `round-2026-08g/reviews/` or `round-2026-08f/reviews/`, the semantic delta, either policy candidate, or the predecessor fixture in `round-2026-08e/`. I ran no `grep`, `rg`, `ls`, or `find` over the repository, and issued no tool call other than the single `Read` of the fixture. Repository context that appeared in my session preamble (AGENTS.md and similar) was not consulted for this exercise and contains none of the fixture's mock content; all reasoning above is derived from the fixture's own text.
