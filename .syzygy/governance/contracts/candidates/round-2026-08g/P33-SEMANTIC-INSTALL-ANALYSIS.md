# P-33 — semantic installation analysis, re-derived

> **Analysis, not a decision.** P-33 is the owner's (VIS-4). Nothing here is
> applied: no module is edited, no ceremony text is changed, no arm is drafted
> into the acceptance record, and no confirmation is retired.
>
> **This supersedes `round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md`**, which
> review **RD-49** returned `REVISE` over with three findings marked BLOCKING.
> This is a re-derivation from the clauses and a fresh measurement, not a
> patch of the prior text — RD-49's finding was that patching the
> recommendation sentence by sentence is what produced the defects.
>
> Every measurement below was produced this session by a Python `re` sweep
> over the working tree at the commit this round names. Nothing is transcribed
> from the superseded analysis.

## 1. The governing clause, quoted exactly

RD-49 finding 4: the prior packet never quoted the cell, and its paraphrase —
"the home holds accepted contract content **exclusively**" — is **wider than
the cell's actual words**. Under the real words the manifests are as plainly
excluded as `history/`; under the paraphrase they read as arguably admitted.

`rfcs/RFC-0003/governance-homes-and-owner-acts.md`, the `contracts/` row:

> | `contracts/` | Accepted load-bearing contracts (RFCs), including
> normative data contracts and external service contracts | Owner acceptance:
> for the foundational set, **the digest-bound acts defined by the active
> acceptance record** … |

And the clause's own framing sentence:

> **RFC3-15.** The **five** constitutional categories of `.syzygy/governance/`
> hold, exclusively — "exclusively" bounding what each category may contain,
> and the five-category set itself being closed except by the two lawful
> widenings this RFC records … A plane validator therefore accepts exactly
> these six names and **rejects a seventh**; neither rejecting `declarations/`
> nor admitting an unreserved directory is conforming

Two things follow that the paraphrase hid:

1. **"Contracts (RFCs)" is narrow.** A wave manifest is not an RFC. Neither is
   a generated report, a history file, or a matrix-row file. **Five of the six
   companion classes are excluded by the cell's own words**, not by
   interpretation.
2. **The closure sentence is separate from the cell**, and any arm that mints
   a new directory under `governance/` amends *the closure rule*, not merely a
   row. RD-49 finding 12 — the prior analysis priced (1d) as "a row plus a
   rewrite" and missed this.

The widening precedent, quoted because two arms turn on it:

> The fifth category is an explicit widening of a structure this RFC calls
> constitutional, made by owner amendment rather than by stretching a
> category's "exclusively" — **the precedent any future widening follows.**

And the one other clause an arm relies on
(`rfcs/RFC-0003/manifests-and-namespace.md`):

> **RFC3-20.** **`.syzygy/cache/` is rebuildable projection, nothing else**
> (VIS-6). The deletion-safety invariant: deleting `cache/` in its entirety,
> at any instant, changes no truth, status, work, consent, or authoritative
> artifact … Nothing in `cache/` may be cited as evidence, serve as a snapshot
> input, hold Genome membership, or **be the only home of any fact.**

All three clauses live in **Wave A modules**. That matters in §4.

## 2. The six companion classes, typed

What the install ceremony currently copies into `contracts/`, beside the
accepted modules:

| Class | What it is | Admitted by the `contracts/` cell? |
|---|---|---|
| `rfcs/` — 39 accepted modules | Accepted contract content | **Yes.** This is what the cell names |
| `wave-manifests/` — 6 files | Integrity-bearing membership: the digest a wave act binds | **No.** Not an RFC |
| `ACTIVE-CONTRACT-MANIFEST.txt` | Package identity across all six waves | **No.** Not an RFC, and see §6 |
| `history/` | Per-module rationale — why a clause reads as it does | **No.** Non-normative |
| `matrix-rows/` | Per-module routing rows | **No.** Generated |
| Two generated reports | Context-budget and compaction measurements | **No.** Rebuildable projection |

**One of six belongs; five do not.** *(The superseded analysis said "exactly
two of six belong" while its own table sent five of six elsewhere — RD-49
finding 4's second half. The discrepancy was the manifests, and the cell's
actual words settle it: a manifest is not an RFC.)*

## 3. The measurement

**Method.** Denominator built from the six wave manifests and cross-checked
against the filesystem: 39 rows, 39 files, empty set-difference both ways.
Every backtick code span extracted with Python `re` (`` `([^`]+)` `` — no
bracket class over `]`, per verification rule 1), counted per target per wave.
Markdown link syntax counted separately.

| Companion target | Wave A | Wave B | C/D | All |
|---|---|---|---|---|
| `history/` | 19 modules, 40 refs | 11 modules, 28 refs | 6 modules, 8 refs | 76 |
| `matrix-rows/` | 1, 1 | — | — | 1 |
| Context-budget report | 3, 3 | 3, 4 | 2, 2 | 9 |
| Compaction report | — | 1, 1 | — | 1 |
| **Total** | **44** | **33** | **10** | **87** |

`[Observed]`. Independently reproduced against RD-49's own table: **agrees
cell for cell.**

**Three different totals circulate and they are not interchangeable** — the
prior packet used them as if they were:

```text
68   history/ references in Waves A+B only          the "rewrite cost" figure
77   all companion references in Waves A+B          the launch-path total
87   all companion references in all 39 modules     the whole population
```

**All 87 are inert code spans. Markdown links to any companion target: 0.**
`[Observed]` — swept this session; RD-49 measured the same. Nothing renders
or resolves them; a reader follows a path string by hand. RD-49 finding 10:
calling them "links" overstates by describing broken navigation where what
exists is a string that does not point at a neighbouring file.

**The four reference kinds, kept distinct** (charter §6.3):

| Kind | Count | What breaks if the target moves |
|---|---|---|
| Clickable Markdown link | **0** | — |
| Code-span path string | **87** | A reader following it by hand lands nowhere. Resolves in any clone of *this* repository regardless |
| Semantic dependency | **0** | Nothing: no clause requires a module's prose path to resolve. Sweep in §5 |
| Historical pointer | included in the 87 | Access to the rationale is unaffected — the candidates tree keeps it |

## 4. Why the confirmations move, derived rather than asserted

The Wave A act's argument is `sha256(wave-manifests/WAVE-A-MANIFEST.txt)` =
`8972d963…`, recomputed this session. That manifest is **19 per-module digest
rows and nothing else**. Therefore:

> **The argument regenerates if and only if at least one of the 19 Wave A
> module byte-streams changes.**

The install ceremony lives in the acceptance record, which appears in no
manifest and feeds no argument. **A ceremony-only change retires nothing.**

This gives a mechanical test, and it collapses the decision:

```text
Does the arm edit a file that is a row in the Wave A or Wave B manifest?
    no  -> both confirmations survive
    yes -> that wave's confirmation retires
```

Two ways an arm can edit such a file:

1. **It amends RFC3-15 or RFC3-20.** Both clauses live in
   `RFC-0003/governance-homes-and-owner-acts.md` and
   `RFC-0003/manifests-and-namespace.md` — **rows 12 and 13 of the Wave A
   manifest.** Any amendment to either retires Wave A. `[Observed]` — both
   paths appear in `WAVE-A-MANIFEST.txt`.
2. **It rewrites the in-module path strings.** That edits up to 30 launch-path
   modules and retires **both**.

**Everything else is free.** Choosing where a *companion* installs, or
declining to install it, touches no manifest row.

## 5. Does any clause require an installed path string to resolve?

**No.** `[Observed]`, with a denominator.

Sweep: all 39 modules; every line containing `link` or `backlink`
co-occurring with `must|shall|required|resolve`, extracted with Python `re`.
**9 hits across 6 modules**, each read individually. All nine are runtime or
product clauses — RFC1-11's trust floor for retired identities, RFC6-20 (*"if
a surface renders such a citation as a link, that link must resolve"* — a
rendering clause, and none of the 87 is rendered), RFC7-3, and RFC8/RFC9
rendering rules. **None governs a governance-tree file path inside a contract
module's prose.**

`check_governance.py` likewise contains no post-install link check; CG-14
checks install *routes* only.

So the 87 dangling strings are a **quality cost, not a lawfulness cost.**
Whether an owner should mind is a values question reserved to the owner —
this analysis establishes only that no clause forbids it.

## 6. The manifest question, separated (charter §6.6)

RD-49 finding 8: the prior treatment bundled the manifest's *home* with its
*meaning*, and the typing was performed and then never converted into an arm.
The two questions are independent and the meanings are different artifacts:

| Artifact | Is | Scope | Therefore belongs |
|---|---|---|---|
| `WAVE-x-MANIFEST.txt` | **Accepted membership** — the argument an act binds | Exactly the modules that act accepts | With or inside the owner-act record. It *is* the act's argument; separating it from the act is what makes it look like an inventory |
| `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows) | **Candidate package identity** — what the package contains | All six waves, most unaccepted | The candidates tree, or a generated installed view. **Not** the accepted tree while 20 of its rows name unaccepted modules |
| An installed effective-state view | **Generated** from the owner acts performed so far | Whatever is actually accepted | Generated, never hand-written |

**No package-wide manifest may sit in the accepted tree implying that
unaccepted waves are accepted.** Under the current deferred posture that is
not a temporary condition: C1/C2/D1/D2 are off the offer path, so a 39-row
manifest installed at the first act would carry **9 permanently unaccepted
rows** — the mirror consequence of deferring the install, which the prior
packet stated for one option and not the other (RD-49 finding 8).

**The cross-product defect.** RD-49 finding 3: the prior recommendations (1e)
and (2b) were mutually inconsistent — (1e)'s closed enumeration admitted
`wave-manifests/`, while (2b) installed `ACTIVE-CONTRACT-MANIFEST.txt` at
`contracts/` root, which a *closed* enumeration excludes. **Ruling both would
have adopted a cell forbidding a file the same ruling installs.** The
separation above removes the conflict at its source: the two manifests are
different artifacts with different scopes and different homes.

## 7. The option space on independent axes

The charter's seven axes are not seven choices. **Axes F and G are
consequences, not decisions:**

```text
A. where accepted RFC modules install          chosen
B. where integrity-bearing manifests live      chosen
C. where generated reports live                chosen
D. where historical rationale lives            chosen
E. whether in-module path strings are rewritten  chosen  <- the only costly one
F. whether accepted module bytes move          FOLLOWS from E and from
                                               whether A-D need an amendment
G. whether confirmations retire                FOLLOWS from F
```

Stating this plainly is most of the analysis. The owner chooses A–E; F and G
are computed by the rule in §4.

### The lawful settings of each axis

| Axis | Setting | Lawful? | Amends a Wave A module? |
|---|---|---|---|
| **A** | `contracts/rfcs/` | **Yes** — this is what the cell names | no |
| **B** | inside the owner-act record (quoted or attached) | **Yes** for the quoted form; *open reading* for an attached `.txt` — the `decisions/` cell neither admits nor excludes one | no |
| **B'** | `contracts/wave-manifests/` | Only by amending the cell | **yes** |
| **C** | leave in the candidates tree | Yes | no |
| **C'** | `.syzygy/cache/` | **Lawful but contestable** — they are rebuildable, but RFC3-20 bars cache from being "the only home of any fact", and the budget report is cited *as* the home of every volatile measurement. Route the citations first or the arm creates the defect it tidies | no |
| **C''** | `contracts/` | Only by amending the cell | **yes** |
| **D** | leave in the candidates tree | Yes | no |
| **D'** | `governance/history/` | Only by amending **the closure sentence** — a seventh name | **yes** |
| **D''** | outside `.syzygy/governance/` | Yes — RFC3-15's scope stops at `governance/` | no |
| **E** | leave the 87 strings | Yes | no |
| **E'** | rewrite them | Yes | **yes — up to 30 modules** |

**Rejected settings, each with its stated rule** (charter §6.2 — reject only
with a rule):

- **Rewrite references during the copy so installed links resolve.** Rejected:
  the ceremony's own invariant is "Installation, bytes unchanged", verified by
  `sha256sum -c`. An installed byte differing from the accepted byte makes the
  digest verification meaningless.
- **Install companions as symlinks.** Rejected as strictly worse: no clause
  addresses symlinks, so whether a symlink is "held" by the category is a new
  open question. It buys nothing over leaving the companions where they are.
- **Copy the companions in a separate operation after the act.** Rejected as
  unlawful: "exclusively" bounds *what the category may contain*, not when it
  came to contain it. Timing does not cure containment.
- **Widen the `contracts/` cell to admit companions.** Not rejected — lawful,
  and priced below. But the RFC3-15(a) precedent cuts against it, and that
  objection applies **equally to a closed re-typing of the cell**, which the
  superseded analysis asserted it did not (RD-49 finding 5). Re-typing a cell
  from one occupant class to three is widening with a fence around it; whether
  the fence changes the character of the move is exactly the question, and
  this analysis does not answer it by assertion. `[Inferred]`, and contested.

## 8. The two finalist strategies (charter §6.4)

### Strategy M — minimum byte churn

```text
A  contracts/rfcs/                    accepted modules only
B  inside the owner-act record        quoted inline
C  candidates tree                    unchanged
D  candidates tree                    unchanged
E  leave the 87 strings
```

| | |
|---|---|
| Accepted bytes moved | **0** |
| Wave A confirmation | **survives** |
| Wave B confirmation | **survives** |
| RFC3-15 amendment | **none** — the cell is satisfied literally |
| Path strings affected | 87 (44 A, 33 B, 10 C/D) |
| Rendered links affected | **0** |
| Manual-follow paths broken | **87**, inside the installed tree only |
| Post-install navigation | A reader in the accepted tree who follows a rationale pointer by hand lands nowhere. The same string resolves in any clone of this repository |
| Contract-category purity | **Full.** `contracts/` holds `rfcs/` and nothing else |
| Clone visibility | Every companion remains present and readable in the candidates tree |
| Future maintenance | Lowest. Nothing to keep in sync |

### Strategy T — clean typed layout

```text
A  contracts/rfcs/                    accepted modules only
B  the owner-act record               membership, exactly scoped to each act
C  .syzygy/cache/                     rebuildable generated reports
D  a named history home               non-authoritative rationale and evidence
E  rewrite the strings                so the installed tree is self-contained
```

| | |
|---|---|
| Accepted bytes moved | **up to 30 modules** (19 A + 11 B) |
| Wave A confirmation | **retires** |
| Wave B confirmation | **retires** |
| RFC3-15 amendment | **the closure sentence**, if the history home is a seventh name under `governance/`; **none** if it sits outside `governance/` |
| Path strings affected | 87, all rewritten |
| Rendered links affected | 0 |
| Manual-follow paths broken | **0** |
| Post-install navigation | Self-contained: every pointer resolves from where the reader is standing |
| Contract-category purity | **Full**, and each companion class sits in a home that names its type |
| Clone visibility | Same content, typed homes |
| Future maintenance | Highest: two trees to keep in step, and the rewrite recurs whenever a companion moves |
| Re-review cost | **One full exact-package review of each wave**, on regenerated arguments |

### The finding that changes the shape of this decision

**Strategy T's typing is available without paying for it.** `[Inferred]` from
the axis table above, and it is the load-bearing new claim here.

Axes A, B, C and D can all be set to their typed values **without amending any
clause and without moving any accepted byte** — accepted modules to
`contracts/rfcs/`, membership into the act record, generated reports left
where they are (or moved to `cache/` once their citations are routed),
rationale left in the candidates tree. The clean type boundary the charter
argues for is achieved by *declining to install the companions*, not by
finding new homes inside `governance/` for them.

**So the two strategies do not differ on typing. They differ on axis E alone.**
The real question is one question:

> **Must a path string inside an installed module resolve from inside the
> installed tree?**

```text
No   -> both confirmations survive, the typed layout is achieved,
        and the cost is 87 code-span strings that resolve in the
        source repository and nowhere else.

Yes  -> up to 30 accepted modules are edited, both confirmations
        retire, and each wave needs one fresh exact-package review.
```

Every other framing of P-33 that has been written — six arms, seven arms,
"the cheapest lawful arm" — is a way of not saying this.

## 9. What this analysis does not establish

- **Whether the owner should mind 87 dangling strings.** That is the actual
  trade and it is reserved (VIS-4). Established here: no *clause* forbids
  them, with a denominator; not established: whether they are acceptable.
- **Whether `decisions/` may hold an attached manifest `.txt`.** The cell
  neither admits nor excludes one. A genuinely open reading, flagged rather
  than resolved. Strategy M is safe under the inline-quotation form regardless.
- **Whether the generated reports may live in `cache/`.** They are rebuildable,
  which is the invariant; but RFC3-20 also bars cache from being the only home
  of a fact, and CG-20 routes every volatile measurement to the budget report
  *as its home*. Lawful only after those citations are routed. Contestable
  today, and marked so above rather than counted as a free win.
- **Whether a re-review would return `CONFIRM` again.** Only a re-administration
  answers that. What is established is that under Strategy M no re-review is
  needed, because no argument regenerates.
- **Any prior review's disposition.** RD-49 is read here; RD-18, RD-26 and
  RD-30 are not re-litigated.
