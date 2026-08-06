# RD-4 — Contract-relation review: depends_on / constrains / cites

**Commissioned:** 2026-08-06, no authoring context.

# VERDICT
VERDICT: REVISE

**17 findings.** The three-way distinction is conceptually right and the
`cites` derivation is mechanically exact — I tried hard to break it and could
not. What fails is the application: **both declared `constrains` edges are
wrong** (one rests on non-clause prose, one is misdirected and duplicates an
already-declared `depends_on`), **two stronger clause-borne constraints are
undeclared**, and the relation is **recorded but not operative** — it appears
in no consumer, no clause, no check, and no fixture.

---

## 0. Method, and what I did not read

**Constraint honoured.** I did not open `RELATION-MODEL-DECISION.md`,
`CONTRACT-RELATION-CLOSURE-REPORT.md`, `MISSION-CONTRACT-SEMANTIC-DELTA.md`,
or any commit message. I read the 32 modules' front matter in full, the bodies
of RFC-0005, RFC-0006, RFC-0007, RFC-0008 and RFC-0011 in the regions bearing
on the claims, `build_dependency_index.py`, `build_contract_index.py`,
`06-CONTEXT-LOAD-MAP.md`, `TASK-TO-CONTRACT-INDEX.md`, all nine fixtures,
`DEPENDENCY-CLOSURE-REPORT.md`, `RC-4-contract-semantics-RAW.md`, and
`PENDING-OWNER-DECISIONS.md` row P-21.

**Sweeps.** Every load-bearing sweep in this report was written in Python `re`
against whole-file text, never `grep` with a negated class. Where a count is
stated it was produced by a script run in this session, and the scripts'
**output** is quoted, not their exit codes.

`build_dependency_index.py --check` output, this session:

```
dependency index matches regeneration — no drift
```

---

## 1. Are the two `constrains` edges correct?

### 1.1 `RFC-0006 → RFC-0005` — **not a constraint the contract states.** [Observed]

The declaring front matter is `rfcs/RFC-0006-cross-surface-selection-query-drawer.md:9`:

```
constrains: [RFC-0005]
```

The restriction text, in full, `rfcs/RFC-0006-cross-surface-selection-query-drawer.md:453-455`:

> **Provides to RFC 0005:** the resolution and query semantics its
> authentication contract wraps — client class never changes an answer's fact
> set or labels, only whether the client is admitted (SEC-1).

**This is the only place in RFC-0006 where the restriction is stated.** A
Python `re` sweep for `client[- ]class` over the whole file returns exactly two
lines — `:454` above, and `:486` ("Machine-client authentication and client
classes → RFC 0005 (SEC-1)"), which is a deferral, not a restriction. A sweep
for `SEC-1` returns the same two lines. [Observed]

**And it is not in a clause.** RFC-0006's last clause opener is
`RFC6-28` at `:387`; `## 5. Integration` begins at `:437`. Line 453 is 50
lines past the final clause and inside the Integration section. RFC-0006's own
precedence rule at `:36` — *"If this map and a clause ever disagree, the clause
wins"* — is scoped to the §0 reader map, so §5 does not even carry a
disclaimer; but no clause of RFC-0006 carries this text either way. [Observed]

RC-4 §4.1 named §5 Integration prose used as a clause home as a systematic
defect class in this package. The `constrains` edge takes one instance of that
defect and promotes it to structured metadata, which makes it look more
load-bearing than the text supporting it. [Inferred]

**On the other side, RFC-0005 acknowledges nothing.** RFC-0005's four modules
cite **zero** `RFC6-n` clauses (Python `re`, all four files). Its only mentions
of RFC-0006 are contract-level pointers in prose: `RFC-0005/README.md:190`,
`admission-and-boundary.md:368`, `consent-egress-secrets.md:259`, each of the
shape "Provides to RFC 0006 and the surfaces". RFC5-3
(`admission-and-boundary.md:99-105`) grounds client classification in **SEC-1
directly**, citing no RFC-0006 clause. [Observed]

**Judgment: it is neither `constrains` nor `depends_on` as the corpus stands —
it is a sentence in an Integration section.** The *idea* (client class never
changes an answer's fact set) is a real one-way restriction and deserves to
exist. But recording it as a typed relation while its only carrier is prose
outside every clause records the relation over an artifact the package's own
convention says is navigational. The fix is a clause, not a front-matter key.

### 1.2 `RFC-0008 → RFC-0007` — **misdirected. This is a `depends_on`, and it is already declared.** [Observed]

Declared at `rfcs/RFC-0008/README.md:14` and
`rfcs/RFC-0008/identity-authority-materialization.md:12`.

The clause text, `rfcs/RFC-0008/identity-authority-materialization.md:201-204`:

> **RFC8-9.** Per SDR-18, **Trajectory owns the drafting queue and the work
> lifecycle** — **an ownership asserted against Polaris, not against the work
> scheduler**. Queue state, assignment, and progress live in this surface and
> **Polaris renders that state read-only** (RFC7-24); Polaris owns the
> contextual intent-authoring and adoption experience.

Unlike edge 1, this **is** clause-borne. But three facts, all in the text,
defeat the relation:

**(a) RFC-0007 states the same restriction itself, completely, in its own
clause.** `rfcs/RFC-0007/narrative-contract.md:432-439`:

> **RFC7-24 — The SDR-18 seam.** Trajectory owns the **drafting queue and work
> lifecycle**; Polaris owns the **contextual intent-authoring and adoption
> experience**. Queue state, assignment, and progress live in the work surface;
> Polaris renders that state read-only and hosts the acts…

That is the same rule, in the same words, in the constrained contract's own
clause body. There is no restriction here that RFC-0007 does not own. [Observed]

**(b) RFC-0007 declares itself the *provider* of the seam.**
`rfcs/RFC-0007/narrative-contract.md:559-561`:

> **Provides to RFC 0008 (Trajectory):** the SDR-18 seam obligations
> (RFC7-22/24) — the drafting queue's ownership, the read-only rendering
> contract, and where a rejection is recorded.

**(c) RFC8-9 cites RFC7-24 as its authority, and RFC-0008 already declares the
dependency.** `identity-authority-materialization.md:290-291` lists under
"Relies on": "**RFC 0007:** Polaris rendering queue state read-only
(RFC7-24)." Its front matter carries `depends_on: [… RFC-0007]`. [Observed]

**Judgment: `constrains` is the wrong relation here, and the right one is
already present.** The direction is inverted — RFC-0007 owns and states the
rule; RFC-0008 consumes and restates it under citation. What remains after the
`depends_on` is not a constraint but a **co-stated seam**: one rule written
twice, in two contracts, in two files, with a citation link in one direction
only. That is a drift risk (RC-4 finding 5, unchanged) and it is not what
`constrains` describes.

### 1.3 The index's justifying sentence is **false** for one of its two rows. [Observed]

`CONTRACT-DEPENDENCY-INDEX.md:46-48` (generated from
`build_dependency_index.py:212-214`):

> …before this relation existed they were stated in one contract, acknowledged
> by no clause in the other, and enforced by neither (owner item **P-21(a)**).

For `RFC-0008 → RFC-0007` this is contradicted by RFC7-24, quoted above — a
numbered clause of the "other" contract stating the restriction in full. RC-4,
the source the sentence relies on, says so itself at line 149 of its raw
output: *"The SDR-18 seam is stated independently and completely from Polaris's
own side at `rfcs/RFC-0007/narrative-contract.md:433`… so RFC-0007's text is
self-standing."* The index generalizes RC-4's edge-1 finding across both rows.
[Observed]

**Finding F-1** — edge `RFC-0006 → RFC-0005` is authored on §5 Integration
prose; no clause of either contract carries the restriction.
**Finding F-2** — edge `RFC-0008 → RFC-0007` is misdirected; the restriction is
owned and stated by RFC7-24, and the real relation (`depends_on`) is already
declared on the same pair, in the same direction, from the same sentence.
**Finding F-3** — the index's generated justification is false for row 2.

---

## 2. Are there `constrains` edges that were missed?

I swept the corpus twice for one-way cross-contract restrictions: once
line-based, once over whitespace-normalized whole-file text (the second pass
found hits the first missed to line wrapping — including the strongest one
below). Patterns: `no (later|other|downstream) (contract|RFC)`, `no
(contract|RFC) may`, `no surface (may|renders)`, `binds (every|all)`, `none may
weaken`, `amending this clause, not extending`, plus a cross-surface-name ×
restriction-verb sentence scan. All in Python `re`.

**Two candidates are stronger than either declared edge, and both are
undeclared.**

### 2.1 `RFC-0005 constrains RFC-0006` (and RFC-0010, RFC-0011) — **should be declared.** [Observed]

`rfcs/RFC-0005/admission-and-boundary.md:107-115`, inside RFC5-3 (clause opener
at `:99`):

> **The two classes are exhaustive, for all present and future clients**
> *(rev10 scoping, directive §2 / OD-R10-5).* There is no third client class
> and **no later contract may introduce one**: any client that is not a browser
> holding a session under RFC5-4 is machine-class, admitted **only** under
> RFC5-5 and RFC5-6. This binds the official `syzygy` CLI, agent-protocol
> adapters (e.g. an MCP server or equivalent), scripts, and fleet workers
> alike… A contract needing a further client class would be **amending this
> clause, not extending it**.

Restated at `RFC-0005/README.md` and `admission-and-boundary.md`
("…no later contract may add a third").

This is textbook `constrains`: **clause-borne**, **one-way**, and it restricts
what *other* contracts may own — explicitly naming "later contract". The
constrained population is every contract with `machine-clients` in
`applies_to`: RFC-0006, RFC-0009, RFC-0010, RFC-0011.

**The RFC-0006 case is the sharp one.** RFC-0006 declares
`applies_to: [all-surfaces, kernel, machine-clients]`, `governs:
[…machine-endpoints…]`, and `depends_on: [RFC-0001, RFC-0002]` — it does *not*
depend on RFC-0005. So nothing pulls RFC5-3 into a packet for someone editing
RFC-0006's machine-endpoint semantics, and RFC5-3 is precisely the clause that
forbids them minting a third client class. **This is the inverse of the one
edge the model does declare**: the model records RFC-0006 → RFC-0005 (prose
only) and omits RFC-0005 → RFC-0006 (clause-borne). If either direction of this
pair deserves a `constrains` edge, it is the one that was left out.

For RFC-0010 and RFC-0011 the gap is closed incidentally — both declare
`depends_on: RFC-0005` — but that is luck, not the model working.

### 2.2 `RFC-0007 constrains RFC-0001, RFC-0004, RFC-0008` — **should be declared.** [Observed]

`rfcs/RFC-0007/narrative-contract.md:96-100`:

> **RFC7-3 — Nothing cites the rendering.** No claim, gap, mapping, evidence
> link, work warrant, source anchor, or citation anywhere in Syzygy may resolve
> to a Polaris narrative, section, claim block, rendering, or editorial draft
> as its authority: a narrative artifact is never an admissible evidence
> artifact, never a snapshot input to a status claim, never a citation target.

Clause-borne, one-way, and it restricts artifacts *other* contracts own: claims
and source anchors (RFC-0001), evidence links (RFC-0004), work warrants
(RFC-0008), snapshot inputs (RFC-0002 RFC2-1). None of those contracts
`depends_on` RFC-0007 — **RFC-0001 depends on nothing at all** — so a
`depends_on`-driven selector never loads RFC7-3 for a kernel or evidence task.
This is exactly the case `constrains` exists to carry, and it is the largest
one in the corpus. **Should be declared.** [Observed for the text; Inferred for
the disposition]

### 2.3 Weaker candidates, reported for completeness

| Candidate | Text | Declare? |
|---|---|---|
| `RFC-0002 constrains RFC-0007/0008/0009` | `rfcs/RFC-0002/README.md:208-210` — "**no surface renders a composite maturity number** (RFC7-16 binds Polaris to that; the prohibition is general)" | **No, not as it stands.** Same defect as edge 1: it lives in §7 "Deliberately deferred", and RC-4 4.1(b) found a whole-corpus sweep confirming no clause carries the general prohibition. Fix the clause first. All three surfaces already `depends_on: RFC-0002`, so the load obligation is discharged anyway |
| `RFC-0005 constrains RFC-0004/0007/0008/0009` | `RFC-0005/consent-egress-secrets.md` — the content-class vocabulary "is closed at this RFC (amend to extend)" | **No.** Every named contract already declares `depends_on: RFC-0005` except RFC-0004, which does declare it. Redundant with the stronger relation |
| `RFC-0001 constrains everything` | RFC1-5 "V0-core entity vocabulary is **closed**"; RFC1-26 typed-relation closure | **No.** All ten other contracts declare `depends_on: RFC-0001` |
| `RFC-0009`'s "none may weaken a clause here (RFC9-2)" (`interaction-parity-and-release.md:339`, `visual-grammar-and-lenses.md:594`) | Binds *post-acceptance material*, not another contract | **No.** Not a contract-to-contract edge |

**Finding F-4** — `RFC-0005 constrains RFC-0006` (RFC5-3) is undeclared, is
clause-borne, and is not covered by any `depends_on`.
**Finding F-5** — `RFC-0007 constrains RFC-0001/0004/0008` (RFC7-3) is
undeclared, is clause-borne, and reaches contracts that depend on nothing.
**Finding F-6** — the two-row `constrains` table is presented without a
denominator or a stated sweep. The generator's own fallback branch
(`build_dependency_index.py:228-230`) writes "That is a claim, not an absence"
when the set is empty, but the populated branch makes no equivalent statement,
so two rows read as *the* two rather than *the two found*.

---

## 3. Is any declared `depends_on` actually a `cites`?

I ran the sharper predicate RC-4 used — *is the citation a reliance* — as a
mechanical census: for every module, for every declared `depends_on` target,
count the substantive clause citations of that target in that module's body,
excluding the identical `RFC3-16` status banner every module carries at line
~18.

### 3.1 One live instance of the exact error RC-4 refuted. [Observed]

`rfcs/RFC-0009/interaction-parity-and-release.md` declares
`depends_on: [RFC-0002, RFC-0006, RFC-0007, RFC-0008]`. Its **only** `RFC7-n`
citation in the whole file — verified with Python `re`, 1 hit — is `:299`:

> *(RFC9-52 binds the whole package, not this module alone: "RFC9-1…RFC9-51"
> spans all three modules, and the coverage matrix is produced for RFC 0009
> entire. The clause is shape-parallel with RFC6-28, RFC7-38 and RFC8-32.)*

This is the **shape-parallel parenthetical** — the construct RC-4 named as "a
note that two clauses have the same shape, which is the opposite of consuming
one", and on the strength of which four `depends_on` edges were reverted
(`DEPENDENCY-CLOSURE-REPORT.md:154-163`). The edge was added in the same pass
(Group B row `RFC-0007 → RFC-0009`, applied to this file among others) and
survives. `rfcs/RFC-0009/README.md:141` carries the identical construct as its
sole `RFC7-n` and sole `RFC8-n` citation, though the README union rule
(`depends_on` = union of siblings) independently justifies both there.

**This one should be reverted**, by the package's own precedent.

### 3.2 Eighteen module-level `depends_on` edges have no clause citation at all. [Observed]

Full list, from the census (banner excluded):

| Module | `depends_on` targets it never cites |
|---|---|
| `rfcs/RFC-0010-mission-control-autonomy.md` | RFC-0001 |
| `rfcs/RFC-0011-context-compiler.md` | RFC-0001, RFC-0002, RFC-0004 |
| `rfcs/RFC-0002/rendering-vocabularies.md` | RFC-0005 |
| `rfcs/RFC-0003/README.md` | RFC-0001, RFC-0002, RFC-0004, RFC-0005 |
| `rfcs/RFC-0005/admission-and-boundary.md` | RFC-0001 |
| `rfcs/RFC-0005/execution-profiles.md` | RFC-0001 |
| `rfcs/RFC-0008/README.md` | RFC-0003, RFC-0004, RFC-0005, RFC-0007 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | RFC-0005 |
| `rfcs/RFC-0009/README.md` | RFC-0004, RFC-0005 |

Seven of the eighteen are package READMEs and are explained by the union rule.
**The other eleven are not.** The sharpest is the contract that consumes this
metadata: `RFC-0011-context-compiler.md` cites **zero** `RFC1-n`, **zero**
`RFC2-n` and **zero** `RFC4-n` clauses (Python `re`, whole file) while
declaring load obligations on all three. Its §5 names them at contract
granularity only — `:248` "**RFC 0001/0002:** packets pin evaluations and
as-of instants…", `:255` "**RFC 0004:** evidence references enter packets by
identity" — with no clause identifier anywhere. `RFC-0010` likewise cites zero
`RFC1-n` clauses while declaring `depends_on: RFC-0001`.

I am **not** recommending these be dropped. Some are plainly real (a context
compiler does need the entity model). The finding is about the *method*: the
closure report's stated test — "the test was whether the target module actually
cites the source contract's clauses in its own body"
(`DEPENDENCY-CLOSURE-REPORT.md:45-47`) — was applied only inside the 20-edge
asymmetry window. Eleven edges outside that window fail it and were never
examined. The evidence bar is not uniform across the graph, and nothing says so.

**Finding F-7** — `rfcs/RFC-0009/interaction-parity-and-release.md` →
`RFC-0007` rests solely on the shape-parallel parenthetical; it is a `cites`,
by the package's own precedent, and should be reverted.
**Finding F-8** — eleven non-README `depends_on` edges carry zero clause
evidence, including three of the eight on RFC-0011. The citation test was
scoped to the 20 known asymmetries and never run over the rest of the graph;
that scoping is undisclosed in the index.

---

## 4. Is the derived `cites` set correct and complete?

### 4.1 The derivation reproduces exactly. **Confirmed.** [Observed]

I wrote an independent front-matter reader and clause scanner (no import from
the package script), recomputed all eleven contract rows, and diffed against
the committed table:

```
contracts: 11 modules: 32
cites table agrees with independent scan: True (11 rows)
```

All eleven rows match, including the empty ones. `--check` reports no drift.

### 4.2 The regex is complete against this corpus. **Confirmed, with the tests I ran.** [Observed]

`CLAUSE_REF = re.compile(r"\bRFC(\d+)-\d+")` (`build_dependency_index.py:54`).
I attacked it four ways:

| Attack | Method | Result |
|---|---|---|
| **Line wraps** | `RFC(\d+)-\s*\n\s*\d+` and `RFC\s*\n\s*(\d+)-\d+` over all 32 bodies | **0 hits.** No clause reference is split across a line break anywhere in the corpus |
| **Whitespace tolerance** | Recomputed every module's ref set from whitespace-normalized text with `RFC\s*(\d+)\s*-\s*(\d+)` and diffed against the script's sets | **0 modules differ.** The tolerant regex finds nothing the strict one misses |
| **Table cells** | Extracted refs from pipe-delimited rows only | Matched, and counted. Verified live: `RFC-0001-…:478` and `:480` are table rows citing RFC3-14, RFC9-4, RFC9-19(b), RFC9-20, RFC9-44, and all appear in RFC-0001's `cites` set. **The script scans body-wide, not line-wise, so table cells are not a hazard** |
| **Code fences** | Extracted ```…``` blocks and rescanned | **1 hit**, `RFC-0010-mission-control-autonomy.md`, `RFC10-20` — a self-reference, discarded by `rec["refs"].discard(cid)`. **No cross-contract citation currently sits inside a fence** |

The `RFC 0008 §5` exclusion documented at `build_dependency_index.py:51-53` is
also currently harmless: a sweep for `RFCs?\s+0*\d+\s*§\s*\d+` over all 32
bodies returns **8 hits**, all of them navigational pointers to §7 or §8
sections (owner-question and deferred-item registers) — `RFC-0011:` "RFC 0010
§8", `RFC-0002/rendering-vocabularies.md`: "RFC 0005 §8", "RFC 0008 §8" ×2,
`RFC-0009/semantic-geography.md`: "RFC 0003 §7" ×2. **RC-4's P-21(c) instance —
RFC9-32 citing "RFC 0008 §5" as authority — has been repaired**: `rfcs/RFC-0009/
visual-grammar-and-lenses.md:209` and `:238-239` now cite `RFC8-12`, `RFC8-28`
and `RFC8-13` by clause identifier. Zero section-as-authority citations remain.

### 4.3 It over-matches. Five of the twenty-two `cites` edges are artifacts. [Observed]

I ran a per-edge evidence census: for every `cites` edge, every citing line,
classified as banner boilerplate / shape-parallel parenthetical / substantive.

**(a) One edge is pure boilerplate.**

```
RFC-0006 cites RFC-0003: 1 hits, BANNER-ONLY
    RFC-0006-cross-surface-selection-query-drawer.md:19 [RFC3-16]
    effective act only after correlation (RFC3-16). Absent such a record, this
```

This is the identical status banner carried by all 32 modules, including
RFC-0001, which declares `depends_on: []`. It is the exact line RC-4 used to
refute the `RFC-0006 → RFC-0003` dependency, and on which
`DEPENDENCY-CLOSURE-REPORT.md:160` reverted it. **The derivation re-creates the
same phantom edge one relation weaker.**

**(b) Four edges are pure shape-parallel parenthetical.**

```
RFC-0010 cites RFC-0007: 1 hit  — RFC-0010-…:679  "with RFC6-28, RFC7-38, RFC8-32, RFC9-52.)"
RFC-0010 cites RFC-0009: 1 hit  — same line
RFC-0011 cites RFC-0007: 1 hit  — RFC-0011-…:224  "with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16.)"
RFC-0011 cites RFC-0009: 1 hit  — same line
```

**These are precisely the four edges the closure report reverted** — same
pairs, same evidence, same two lines. They were removed from `depends_on` for
being non-evidence and have reappeared as `cites`.

The harm is bounded, because `cites` drives no load. But the index describes
these rows as "Navigational evidence a human or an agent may follow"
(`CONTRACT-DEPENDENCY-INDEX.md:15`), and following `RFC-0011 cites RFC-0007`
leads to a parenthesis observing that two phase rules have the same shape.
That is not navigation; it is the residue of a refuted inference, re-entered
into the record by a weaker predicate. If `cites` is to mean anything to a
reader, the boilerplate banner and the shape-parallel parenthetical should be
excluded from the scan by construction — both are single, fixed, greppable
strings.

**(c) One latent over-match, no live instance.** A clause identifier appearing
inside a fenced example (a JSON packet, a YAML fragment) would be counted as a
citation. Today the only fenced reference is a self-reference. There is no
guard.

**Finding F-9** — `RFC-0006 cites RFC-0003` rests solely on the universal
status banner; the derivation reproduces a phantom the closure report removed.
**Finding F-10** — four `cites` edges (`RFC-0010`/`RFC-0011` → `RFC-0007`/
`RFC-0009`) rest solely on the shape-parallel parenthetical: the same four
edges, the same two lines, that RC-4 refuted and the closure report reverted.
**Finding F-11** — no guard excludes clause identifiers inside fenced code
blocks; latent, zero live instances.

---

## 5. Selector consequences — the nine fixtures

The index states the rule at `CONTRACT-DEPENDENCY-INDEX.md:14`: `constrains` is
"loaded **when the task class crosses the constrained seam** — editing B loads
A's constraining clauses". The metadata is **contract-granular** (`constrains:
[RFC-0005]`, not `RFC6-§5 constrains RFC5-3`), so a deterministic selector can
only implement this as: *a packet selecting any module of B also selects A*.

Measured sizes for the pulls: `rfcs/RFC-0006-…` = **4,169 w ≈ 5,628 est.
tokens**; `rfcs/RFC-0008/README.md` + `identity-authority-materialization.md` =
**4,647 w ≈ 6,273 est. tokens** (`scripts/context_load.py`, this session).

| # | Fixture | Selects RFC-0005 or RFC-0007? | Changed? |
|---|---|---|---|
| 1 | Polaris narrative | RFC-0007 README + `narrative-contract` | **YES** — pulls RFC-0008. 18,745 → ~25,000 est. tok, crossing the 20k trigger the fixture currently sits under |
| 2 | Trajectory adapter | no | no |
| 3 | Orrery lens | no | no |
| 4 | Execution profile | RFC-0005 README + `execution-profiles` | **YES** — pulls RFC-0006. 14,724 → ~20,350 est. tok, crossing the trigger |
| 5 | Cross-project mission | no | no |
| 6 | Doctrine amendment | no | no (but see below) |
| 7 | Kernel identity | no | no |
| 8 | OpenSpec authoring | RFC-0007, all three modules | **YES** — pulls RFC-0008. 30,252 → ~36,500 est. tok. This is already the largest breach in the set |
| 9 | Evidence adapter | `RFC-0005/execution-profiles` | **YES** — pulls RFC-0006 |

**Four of nine change, and every one of them changes for the worse.** [Observed
for the selections and measurements; Inferred for the judgment]

- **Fixture 4** is the clearest damage. It edits execution profiles
  (RFC5-18..23, module `execution-profiles`). The RFC-0006 restriction is about
  *client class and answer fact sets* — it bears on RFC5-3 in
  `admission-and-boundary`, a module fixture 4 explicitly and correctly omits.
  The seam is not crossed. But contract-granular metadata cannot say that, so
  the selector loads 4,169 words of selection/URL/drawer semantics into a
  security packet, and pushes it over the decomposition trigger.
- **Fixture 8** carries "the largest budget breach in the eight-fixture set"
  with a reviewed waiver. Adding RFC-0008 makes it materially worse for a
  restriction (RFC7-24) that is **already inside the fixture's own mandatory
  set** — fixture 1's prose says as much: "the adoption gate (VIS-4,
  RFC7-23/24/25) … are in the mandatory set."
- **Fixture 1** is the same story: RFC7-24 is loaded; RFC8-9 restates it; the
  model pulls in 4,647 words to deliver a rule the packet already has.

This is finding F-2 cashed out. Because edge 2 points at a contract that states
the restriction itself, the constraint pull is **pure redundancy** in every
fixture it touches.

**Where the model helps: `cites`-is-never-automatic backs one argued omission.**
Fixture 6 omits RFC-0010 and argues it in three sentences of prose ("the
amendment's *subject*, not its *authority*… moved to the **suggested** set with
provenance"). Fixture 6 selects `RFC-0003/governance-homes-and-owner-acts.md`,
which cites RFC10-9 at `:282`. Under the old single-relation model that
citation was ambiguous evidence; under the new one it is a `cites` and
therefore never automatic, and fixture 6's omission stops being an argument and
becomes a rule application. **That is a real improvement and the model earns
it.** The same rule licenses fixture 1's omission of RFC-0006 and fixture 7's
omission of the surface contracts.

**One thing the table asserts that no fixture honours.** `CONTRACT-DEPENDENCY-
INDEX.md:13` states `depends_on` behaviour as "**mandatory load**,
transitively". **Zero of the nine fixtures do this.** Fixture 1 selects
RFC-0007, whose `depends_on` is RFC-0001/0002/0003/0004/0005/0006/0009 —
transitively that is the entire corpus, against a 13,885-word packet. Fixture 2
selects RFC-0004 and RFC-0008, both of which `depends_on: RFC-0002`, and omits
RFC-0002 from mandatory entirely. The word "transitively" is new in this table
and it converts a known tension (RC-12 finding F-3, cited in fixture 2's
early-revisit conditions) into a flat contradiction between the index and every
golden selection in the package.

**Finding F-12** — the `constrains` rule as stated is contract-granular and
would inflate fixtures 4, 8 and 9 across the decomposition trigger, in every
case to deliver a rule the packet already holds or does not need.
**Finding F-13** — `CONTRACT-DEPENDENCY-INDEX.md:13` asserts transitive
mandatory loading; none of the nine fixtures implements it, and fixture 2
omits a directly-transitive dependency.

---

## 6. The seam that matters most — does `constrained_by` reach anyone?

**It does not. The relation is recorded and not operative.** [Observed]

I traced every path by which an engineer editing RFC-0005 or RFC-0007 could
learn of the constraint.

| Would it tell them? | Result |
|---|---|
| **The constrained contract's own text** | RFC-0005: no clause, no prose, cites zero `RFC6-n` (§1.1). RFC-0007: RFC7-24 states the rule — but from RFC-0007's own authority, not as an acknowledged external constraint, and it names no `RFC8-n` clause anywhere in the package (`grep -E 'RFC8-'` over all three RFC-0007 modules: **0 hits**) |
| **`05-CONTRACT-INDEX.yaml`** — the machine lookup RFC11-4 names as a selection input | **No.** `grep -c constrain` → **0**. `scripts/build_contract_index.py:118` emits `("governs", "applies_to", "depends_on", "provides_to", "tags")` — `constrains` is not in the list, and `provides_to` still is, though no module declares it any more |
| **`06-CONTEXT-LOAD-MAP.md`** | **No.** `grep -c constrain` → **0**. Its reader map lists "Security/profile work: RFC-0005 (relevant module) + RFC-0003 governance-homes + doctrine `security.md` + craft security policy" — no RFC-0006 |
| **`TASK-TO-CONTRACT-INDEX.md`** | **No.** `grep -c constrain` → **0**. Row "Security / execution-profile work" (`:48`) loads RFC-0005 + RFC-0003 + doctrine + craft. Row "Surface implementer — Polaris" (`:44`) loads RFC-0007 + RFC-0002 rendering + RFC-0006 — no RFC-0008 |
| **RFC-0011, the consuming contract** | **No.** RFC11-4 (`rfcs/RFC-0011-context-compiler.md:105-112`) enumerates the deterministic selection inputs and names "contract dependencies (`depends_on` / `provides_to`); explicit `applies_to` and clause-level metadata". `constrains` appears nowhere in the file (its one `constrain` hit, `:59`, is the phrase "silently dropped a constraint") |
| **Any of the nine fixtures** | **No.** Zero occurrences of `constrain` as a relation in any fixture |
| **Any check** | **No.** `verify_final_prespec.py`'s one hit is an unrelated fixture-section keyword. No check asserts the `constrains` set is complete, correct, or acknowledged |

**So the relation exists in exactly two files: the generated index and the
generator that writes it.** A conformant Context Compiler implemented against
RFC11-4 as written would never read it, because RFC11-4 names its inputs
exhaustively and `constrains` is not among them.

There is a second-order problem here. `CONTRACT-DEPENDENCY-INDEX.md:11-15` is a
table titled "**Context Compiler behaviour**", stating what a selector must do
with each relation — "mandatory load, transitively", "loaded when the task
class crosses the constrained seam", "never automatic". **No clause states any
of this.** It sits in a file whose own first line reads "derived, never
authority" and whose banner says "nothing here may be cited as authority
(RFC11-7 rebuildable-projection rule)". The operative half of the three-relation
model is therefore stated only in a file that disclaims the ability to state
it, and contradicted in one respect (transitivity) by every fixture. That is
the same defect shape RC-4 §4.1 catalogued — a binding rule homed in a
navigational artifact — appearing in the repair for it.

**Finding F-14** — `constrains`/`constrained_by` reaches no consumer: not
`05-CONTRACT-INDEX.yaml`, not RFC11-4's enumerated selection inputs, not the
load map, not the task index, not a fixture, not a check. The relation is
recorded, not operative.
**Finding F-15** — the "Context Compiler behaviour" column states normative
selector obligations that no clause carries, inside a file that declares itself
non-authority.

### 6.1 One structural check the generator is missing

`asymmetries()` (`build_dependency_index.py:154-162`) flags a `constrains` edge
`A → B` as `redundant` when `A in contracts[B]["depends_on"]` — B already loads
A, so the constraint adds nothing. Correct as far as it goes. **It does not
check the other direction**, `B in contracts[A]["depends_on"]`, and that is the
live case: RFC-0008 both `depends_on` RFC-0007 **and** `constrains` RFC-0007,
from the same sentence. The two are not strictly redundant (they drive loading
in opposite task classes), but a pair carrying both relations in the same
direction is exactly the signal that the constraint was derived from a
dependency and should be re-examined. The check would have fired on the one
edge that turns out to be wrong.

**Finding F-16** — the redundancy predicate is one-directional and does not fire
on `A constrains B` where `A depends_on B`; it would have caught F-2.

### 6.2 P-21(a) is still pending, and it offered two arms

`PENDING-OWNER-DECISIONS.md:81`, header "**Status: every item below is
PENDING**", as-of 2026-08-06c:

> …**One-way constraints have no home.** … so either a separate `constrains:`
> relation is introduced **or** each constrained contract gains an
> acknowledging clause.

The register frames this as a choice the owner has not made. The corpus has
taken the first arm — `constrains:` keys are now in three candidate modules'
front matter, and those modules are subjects of act 1's digest manifest — while
the second arm, the acknowledging clause, is the one that would have made the
relation operative on the constrained side (§6). [Observed for both texts;
Inferred that the arms were meant to be exclusive alternatives rather than a
sequence.] I flag this as a governance seam for the owner, not as a judgment
that the edit was unauthorized.

**Finding F-17** — P-21(a) remains PENDING and offers two alternatives; one has
been installed into candidate contract front matter and the register has not
been updated to say so.

---

## 7. Directionality — author `constrains` on which side?

**The case for authoring on the constraining contract (as built).**
The constraining contract is where the sentence lives. Metadata authored beside
the text it describes cannot silently disagree with it, and a reviewer editing
RFC5-3's exhaustiveness paragraph sees `constrains:` three lines up in the same
file. The alternative requires B to declare a fact about A's text that B does
not contain — which is how `provides_to` drifted to 20 asymmetric edges, and
the report is right that "requiring B to acknowledge it is what left the two
known cases enforced by neither". Authoring on A also means a *new* constraint
can be added by one edit to one file, by the person writing it.

**The case for authoring on the constrained contract.**
The relation's entire purpose is to reach the person editing B — and B's front
matter is what B's editor reads. An author narrowing RFC5-3's client-class
paragraph never opens RFC-0006. Authoring on B also puts the burden where the
review happens: a `constrained_by: [RFC-0006]` line in RFC-0005's front matter
is a claim RFC-0005's owner has accepted, which is the acknowledgment P-21(a)'s
second arm asks for. Under the derived-inverse rule the reader of the *index*
sees both directions either way; the asymmetry that matters is which **file**
carries the line, and only B's file is on B's editor's path.

**Recommendation: keep authoring on the constraining contract, and add a
required acknowledgment on the constrained side — but as a clause, not a
front-matter key.**

The single-authored-direction discipline is right and hard-won; do not trade it
for a second authored view. But `constrains` as built is a one-ended edge in
practice, and the fix P-21(a) already named is the one that closes it: the
constrained contract gains a short clause acknowledging the restriction and
citing it. That is what RFC7-24 already is for the RFC-0008 seam — and note
that the pair with a real acknowledging clause is exactly the pair where
`constrains` turns out to be unnecessary. That is not a coincidence; it is the
model telling you what it is for. **`constrains` is the correct home for a
restriction the constrained contract has not yet absorbed. Its right end state
for any given edge is to be replaced by a clause.** Saying so in the index —
that a `constrains` edge is a standing defect record, not a stable relation —
would make the two-row table read as a work list rather than as a design.

Two supporting recommendations:

1. **Make the edges clause-granular.** `constrains: [RFC-0005]` cannot express
   "RFC6-§5 restricts RFC5-3", so a selector must load a whole contract to
   deliver one paragraph (§5). RC-4 flagged the same contract-vs-module
   granularity mismatch for `depends_on` (its finding 8); `constrains` inherits
   it and is hurt worse, because a constraint is typically one clause where a
   dependency is typically a module.
2. **Require a clause anchor in the declaration.** A `constrains` edge whose
   source text is not inside a numbered clause of the declaring contract should
   fail a check. That single predicate rejects edge 1 (§1.1) and admits the two
   missed edges (§2.1, §2.2), which is the correct sort on all four.

---

## 8. What I confirmed

Stated so the negatives are legible as work done rather than as absence of
looking.

- **The `cites` derivation is exact.** Independently recomputed all 11 rows
  from a separate reader; 11/11 agree. `--check` prints "dependency index
  matches regeneration — no drift".
- **The clause regex is complete against this corpus.** 0 line-wrapped
  references, 0 differences against a whitespace-tolerant variant over all 32
  modules, table cells correctly captured (verified live at
  `RFC-0001-…:478/480`), 1 fenced reference and it is a self-reference.
- **`provides_to` asymmetry is genuinely unrepresentable now**, not merely
  absent. One authored direction cannot disagree with itself.
- **No dangling edges**, over 11 resolved contracts — reproduced independently.
- **P-21(c) is fixed.** Zero `RFC 000N §M`-as-authority citations remain; the
  8 surviving section references are all §7/§8 navigational pointers.
- **The `cites`-is-never-automatic rule does real work.** It converts fixture
  6's prose argument for omitting RFC-0010 into a rule application, and does
  the same for fixture 1's RFC-0006 omission and fixture 7's surface-contract
  omissions.
- **The three-way distinction itself is correct.** `depends_on`, one-way
  restriction, and navigational reference are three different predicates, a
  selector genuinely cannot act on them alike, and overloading one key was a
  real defect. Nothing below disputes the model. What I dispute is that its two
  declared instances are the right ones, and that anything downstream can see
  it.

## 9. Finding index

| # | Finding | Severity |
|---|---|---|
| F-1 | `RFC-0006 → RFC-0005` `constrains` rests on §5 Integration prose; no clause of either contract carries the restriction | **Blocking** |
| F-2 | `RFC-0008 → RFC-0007` `constrains` is misdirected; RFC7-24 owns and states the rule, and `depends_on` already binds the pair in the same direction from the same sentence | **Blocking** |
| F-3 | The index's generated justification ("acknowledged by no clause in the other") is false for row 2, on its own source's evidence | Material |
| F-4 | `RFC-0005 constrains RFC-0006` (RFC5-3, clause-borne) is undeclared and uncovered by any `depends_on` — the inverse of the one declared edge | **Blocking** |
| F-5 | `RFC-0007 constrains RFC-0001/0004/0008` (RFC7-3, clause-borne) is undeclared and reaches contracts that depend on nothing | **Blocking** |
| F-6 | The two-row `constrains` table carries no denominator and no stated sweep | Material |
| F-7 | `RFC-0009/interaction-parity-and-release.md → RFC-0007` `depends_on` rests solely on the shape-parallel parenthetical — the refuted construct, surviving | Material |
| F-8 | Eleven non-README `depends_on` edges carry zero clause evidence (incl. 3 of RFC-0011's 8); the citation test was scoped to 20 edges and the scoping is undisclosed | Material |
| F-9 | `RFC-0006 cites RFC-0003` rests solely on the universal status banner | Material |
| F-10 | Four `cites` edges rest solely on the shape-parallel parenthetical — the same four pairs the closure report reverted | Material |
| F-11 | No guard against clause identifiers inside fenced code blocks | Minor / latent |
| F-12 | Contract-granular `constrains` would push fixtures 4, 8 and 9 across the decomposition trigger to deliver rules already held | **Blocking** |
| F-13 | `CONTRACT-DEPENDENCY-INDEX.md:13` asserts transitive mandatory loading; none of the nine fixtures implements it | Material |
| F-14 | `constrains`/`constrained_by` reaches no consumer — not the YAML index, not RFC11-4, not the load map, not the task index, not a fixture, not a check | **Blocking** |
| F-15 | The "Context Compiler behaviour" column states normative selector obligations no clause carries, in a file declaring itself non-authority | Material |
| F-16 | The redundancy predicate is one-directional; it does not fire on `A constrains B` where `A depends_on B`, and would have caught F-2 | Material |
| F-17 | P-21(a) remains PENDING with two alternatives offered; one has been installed into candidate front matter and the register does not record it | Material |
