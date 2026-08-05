# RC-3 — Vocabulary review (raw reviewer output)

**Reviewer:** independent fresh-context session. No authoring history was read;
`_bootstrap/` was not opened.
**Date of review:** 2026-08-05.
**Primary subject:** `.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md`
(1,337 lines, 30 entries T-01…T-30).
**Also read in full:** `.syzygy/governance/doctrine/README.md`,
`.syzygy/governance/doctrine/vision.md`, `.syzygy/governance/doctrine/architecture.md`
(headings + §Definitions + §Vocabulary), `.syzygy/intent/OVERVIEW.md`, `README.md`.
**Swept (not read end to end):** the 32 candidate contract modules under
`contracts/candidates/rfcs/`, plus `decisions/PENDING-OWNER-DECISIONS.md`,
`round-2026-08/ROUND-DISPOSITIONS.md`, `round-2026-08/reviews/RB-1-fresh-engineer-RAW.md`.

**Method note.** `grep` on this machine is ugrep; every load-bearing sweep below
was run with Python `re` over an explicit file walk, and every "zero" claim was
confirmed a second time with `grep -F`. Counts are script-produced, not
hand-tallied.

---

## Q1 — AUTHORITY HONESTY

### 1.1 The registry's own title overstates it

`TERM-REGISTRY.md:1`

> `# Term registry — Syzygy's canonical public vocabulary`

Two lines later, `TERM-REGISTRY.md:3`:

> `> **Status: CANDIDATE. This file binds nothing.**`

The banner is exemplary. The title is not: *canonical* is precisely the word a
reader uses for "the settled one, the one you cite." A candidate artifact
cannot be canonical, and a title is what survives into link text, tab titles,
search results, and citation-by-memory — i.e. everywhere the banner does not
travel. [Observed]

### 1.2 The §2 heading contradicts the §2 body, 20 lines apart

`TERM-REGISTRY.md:72`

> `## 2. The six-plane state model (canonical)`

`TERM-REGISTRY.md:92-95`

> **Honest reading of the authority situation:** doctrine's three-state thesis
> is **adopted**; the six-plane model is **candidate**. … Until an owner act
> accepts RFC-0001, "six planes" is how we agree to speak, and `vision.md` is
> still what governs.

The body is one of the most honest paragraphs in the corpus. The heading
directly contradicts it, and headings are what a skimmer and a table-of-contents
generator carry. [Observed]

### 1.3 The public default path cites the registry as settled and complete

`.syzygy/intent/OVERVIEW.md:93-95` (Layer 2 — the five-minute argument, i.e. on
the default reading path):

> Foundational terms used so far: desired / observed / execution state,
> reconciliation work, kernel, surface, capability, Unknown, mission, owner —
> the full vocabulary lives in the term registry.

Four separate defects in one sentence, all [Observed]:

- **"the full vocabulary" is false**, and falsified by the same sentence: of the
  nine terms it names, **four have no registry entry at all** — *reconciliation
  work* (T-26 reserves unqualified "reconciliation" for something else, §Q4.3),
  *kernel*, *surface*, *owner*. Script-verified against the 30 `#### T-nn`
  headings.
- **No candidate marker.** `OVERVIEW.md:10-11` sets the file's own rule:
  "Anchors marked *candidate* cite contract clauses that bind nothing until
  owner acceptance." This line marks nothing.
- **No source anchor at all.** `OVERVIEW.md:10` also states "Source anchors sit
  at the end of each claim block." Every other Layer-2 block ends in a
  `*Sources: …*` line (`:35`, `:45`, `:77`, `:91`). This block (`:93-95`) is the
  only one that does not.
- **No link.** The reader is told where the vocabulary lives and given no path.
  The Layer-4 row (`OVERVIEW.md:187`) does mark it `Candidate` — honestly — but
  points at the *directory* `contracts/candidates/policy-candidates/`, not the
  file, so the pointer is two hops and unresolvable by click.

### 1.4 An owner-approved policy cluster calls it canonical and keys an operative rule to it

`.syzygy/governance/contracts/candidates/policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:115-126`

> `### CC-KNOW-6 — New vocabulary enters through the term registry; replacement needs a migration report`
> The canonical **term registry** — offered as a sibling candidate in this
> directory, and itself a derived record rather than an authority — is the
> admission mechanism: a term used normatively in an active artifact without a
> registry entry is an unadmitted term…

The parenthetical self-qualification ("offered as a sibling candidate … itself a
derived record rather than an authority") is honest and I credit it. **"The
canonical"** is still the wrong adjective, and the operative consequence is
severe: were CC-KNOW-6 confirmed against the registry as it stands, *kernel*,
*surface*, *workspace*, *actuator*, *owner*, *owner act*, *adapter*,
*projection*, *policy*, *decision*, *work item*, *freshness state*, *chain
state* and — most of all — **`status`** would all become "unadmitted terms" used
normatively across adopted doctrine and all 32 candidate modules. The rule would
be violated at scale on the day it took force. [Inferred — from the rule text
plus the sweeps in Q2/Q4.]

### 1.5 Other sites (lower severity, all [Observed])

| Site | Text | Note |
|---|---|---|
| `decisions/PENDING-OWNER-DECISIONS.md:61` | "The term registry … **canonicalizes** the six-plane state model" | Verb overstates; the same item then honestly asks "Approve it as the working vocabulary, or amend" |
| `round-2026-08/OWNER-ROUND-CHARTER.md:665,667,673` | "Establish a **canonical** term registry" / "one **canonical** registry" / "**canonical** term" | The round direction is the origin of the title's adjective |
| `round-2026-08/ACTIVE-AUTHORITY-MAP.md:27` | `\| Vocabulary \| …TERM-REGISTRY.md \| T-nn \| Candidate \|` | **Correct.** Cited as the model for the others |
| `candidates/README.md:28` | "Candidate policy additions (term registry …) — each needs its own owner act" | **Correct** |
| `round-2026-08/PUBLIC-CLONE-AUTHORITY-MATRIX.md:25` | "Term registry (draft)" | **Correct** |

### 1.6 Proposed honest title and framing

Replace `TERM-REGISTRY.md:1`:

```
# Term registry (candidate) — a proposed public vocabulary for Syzygy
```

Replace `TERM-REGISTRY.md:72`:

```
## 2. The six-plane state model (candidate — a drafting convention, not an adopted model)
```

Add to the banner, after `:6`, one sentence that carries the §5 result up to
where a skimmer meets it:

> Eight of the thirty terms have **no adopted definition anywhere** and exist
> only in unaccepted contracts (§5). This file proposes how to speak; it settles
> nothing about what binds.

Replace `OVERVIEW.md:95`:

> …*owner* — several of these are not yet defined in any adopted artifact; the
> candidate term registry
> ([`TERM-REGISTRY.md`](../governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md))
> proposes definitions for thirty of them and binds nothing.
> *Sources: candidate: term registry §5.*

Amend `CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:117` — delete "canonical", and add a
commencement clause: CC-KNOW-6 takes force only over terms introduced *after*
the registry's own accepting act, never retroactively over incumbents.

---

## Q2 — FIVE-DIMENSION SEPARATION

**Verdict on this question: the registry does not achieve the separation it
claims, and the claim itself is false by the registry's own content.**

### 2.1 There are not five closed vocabularies. There are at least nine.

`TERM-REGISTRY.md:38-39`

> Five different questions in Syzygy are answered by five different closed
> vocabularies.

Enumerating the closed value sets the same file names — [Observed], all
citations from `TERM-REGISTRY.md` unless marked:

| # | Closed vocabulary | Values | In the §1 table? | Cite |
|---|---|---|---|---|
| 1 | State plane | desired · proposed · observed · inferred · execution · historical | yes | `:44` |
| 2 | Claim epistemic label | Observed · Inferred · Unknown | yes | `:45` |
| 3 | Evidence/rendering tier | six | yes | `:46` |
| 4 | Work lifecycle | thirteen | yes | `:47` |
| 5 | Governance lifecycle | three families | yes | `:48` |
| 6 | **Claim status** | *never enumerated anywhere* | **no** | `:551`, `:544-547`; RFC1-18 at `rfcs/RFC-0001-…:306` |
| 7 | **Freshness state** | `fresh`/`stale`/`broken`/`superseded` | **no** | `:649-650`, `:525` (RFC2-10) |
| 8 | **Challenge state** | `submitted`→`admitted`\|`rejected`; `admitted`→`resolved-upheld`\|`resolved-dismissed`\|`withdrawn`\|`expired` | **no** | `:753-754` |
| 9 | **Reconciliation chain state** | `merged`·`reconciliation-pending`·`reconciled@E`·`unsatisfied`·`contradiction-raised`·`Unknown(reason)` | half — named inside the work-lifecycle cell | `:47`, `:1068-1073`, `:1082` |
| 10 | **Sibling surface states** | `dismissed-by-decision`·`unadopted-draft`·`editorial-draft` (+`challenge-pending`) | **no** | `:679-682` |
| 11 | **Mission lifecycle** | unenumerated; `blocked` named | **no** | `:1126`, `:1200` |

So the headline "five dimensions" undercounts by six. The most consequential
omission is **#6, claim status** — see 2.3.

### 2.2 Terms belonging to two dimensions

Only **one** collision is flagged (`:61-66`, Observed/Inferred as plane vs
label). The rest are unflagged. All [Observed]:

| Word | Dimension A | Dimension B | Flagged? |
|---|---|---|---|
| `Observed` | state plane `:44` | epistemic label `:45` | **yes** `:61-66` |
| `Inferred` | state plane `:44` | epistemic label `:45` | **yes** `:61-66` |
| **`active`** | work lifecycle `:47` | governance lifecycle (decisions/consents) `:48` | **no — adjacent rows of the same table** |
| **`merged`** | work lifecycle `:47` | chain state `:47` | **no — the same table cell** |
| **`reconciled`** | work lifecycle `:47` | chain state `reconciled@E` `:47` | **no — the same table cell** |
| **`Unknown`** | epistemic label `:45` | chain state `Unknown(reason)` `:47` | **no** |
| **`superseded`** | governance lifecycle `:48` | freshness state `:525` | **no** |
| **`expired`** | governance lifecycle `:48` | challenge state `:754` | **no** |
| **`blocked`** | work lifecycle `:47` | mission lifecycle `:1200` | **no** |
| **`draft`** | governance lifecycle `:48` | surface state `unadopted-draft`/`editorial-draft` `:679-680`; rendering at `:370` | **no** |
| **`suspended`** | evidence tier (inside Unknown) `:46` | challenge effect `:755`, `:775` | partly (`:775` names both) |

`active` is the sharpest: the section that exists to stop dimension collapse
puts the same token in two of its own five rows, one line apart, and says
nothing. `merged`/`reconciled` are sharper still — they collide *inside a single
table cell* (`:47`), where the cell's own text says the chain state is carried
"**beside**" the work lifecycle without noting that two of its values are
spelled identically to two work-lifecycle values.

### 2.3 The `status` problem — the registry's rule is unenforceable and its most load-bearing word is undefined

`TERM-REGISTRY.md:52-56` (the rule):

> **Never use a generic word such as "status", "state", or "stage" where the
> dimension matters.** … A field, column, count, badge, filter, or API key named
> only `status` is a defect wherever more than one of these five could be meant.

`TERM-REGISTRY.md:118`:

> "Status" earns no term at all because it means five things (§1).

**Counts (Python `re`, `\bstatus(es)?\b`, case-insensitive) — [Observed]:**

| Corpus | Occurrences |
|---|---|
| `TERM-REGISTRY.md` | **42** on 40 lines |
| the 32 candidate contract modules under `rfcs/` | **224** |
| `README.md` | 5 |
| `OVERVIEW.md` | 8 |
| `doctrine/README.md` | 1 |

Three findings follow.

**(a) `status` is a sixth dimension, not one of the five.** RFC1-18 makes it a
first-class field *distinct from every one of the five*:

`rfcs/RFC-0001-project-graph-identity-state-planes.md:305-307`

> **Evaluation instance** — durable identity + evaluation identity, carrying
> **status**, epistemic label, rendering tier and Unknown reason where
> applicable (RFC2-24/25), supporting evidence set, freshness state, and
> challenge state.

The registry copies this verbatim at `TERM-REGISTRY.md:551`. So `status` is a
value the kernel carries, alongside — not instead of — label, tier, reason,
freshness and challenge state. **Its value set is enumerated nowhere in the
registry, nowhere in doctrine, and nowhere I could find in the contracts.** The
registry then defines its most load-bearing entry in terms of it:
`TERM-REGISTRY.md:541` — "**Plain language.** The one and only carrier of
status in Syzygy." A term is defined by an undefined word.

**(b) The corpus uses `status` in at least four incompatible senses, none
disambiguated.** [Observed]

| Sense | Dimension it really is | Evidence |
|---|---|---|
| "**status claim**", "positive status", "turns a status green" | claim status (#6 above) | `TERM-REGISTRY.md:554`, `:865`; `rfcs/RFC-0001-…:355`, `:430-434` |
| "**adoption status**", "**effective status**", "lifecycle status" | governance lifecycle | `TERM-REGISTRY.md:867`, `:873`, `:896`; `rfcs/RFC-0003/governance-homes-and-owner-acts.md:102-105`, `:126-127`, `:143-146` |
| "raw **substrate status**", "raw provider status", "a custom status" | work lifecycle | `rfcs/RFC-0008/state-vocabulary-and-cost.md:43`, `:63`, `:168-171` |
| "Genome status", "collapsed into one status" | membership / composite | `doctrine/architecture.md:155`, `:183-184` |

**Worst single offender: T-21 Source snapshot.** Within one 46-line entry,
`status` appears in three different dimensions with no qualifier:

- `TERM-REGISTRY.md:865` — "…affecting the observed graph or a **status claim**"
  (claim status)
- `TERM-REGISTRY.md:867` — "governance artifacts with **adoption status** as a
  fact" (governance lifecycle)
- `TERM-REGISTRY.md:873` and `:896` — "owner-act records establishing
  **effective status**" (governance lifecycle, a *third* phrasing)

**Runner-up: `OVERVIEW.md`**, on the public default path, uses two incompatible
senses 110 lines apart with no qualifier on either:

- `OVERVIEW.md:4` — "effective **status** lives in the owner-act record"
  (governance lifecycle — explicitly *not* computed at an evaluation)
- `OVERVIEW.md:114` — "Every **status** is computed at an identified evaluation"
  (claim status)

Read together, `:114` falsifies `:4`. [Observed]

**Runner-up: literal `Status` columns on the public surface.** `README.md:77`
and `OVERVIEW.md:169` both head a column `Status`, whose values are
Adopted/Recorded/Owner-approved/Candidate/"Does not exist yet"/"Nothing exists
yet" — i.e. governance lifecycle. The registry rule at `:55` names "column"
first in its list of defects. Two of the three most-read tables in the
repository are instances of the defect the registry defines. [Observed]

**(c) Adopted doctrine breaks the rule too, and the registry does not record
it.** `doctrine/vision.md:117` — "the failure is surfaced as status";
`doctrine/architecture.md:183-184` — "may never be collapsed into one status;
those axes … belong to the graph/status RFC". A candidate registry cannot bind
adopted doctrine, but §5's authority-coverage table is where that collision
belongs and it is absent. [Observed]

### 2.4 Summary answer to Q2

The five dimensions **bleed**. The registry's contribution — naming the
Observed/Inferred double-binding and forbidding bare `status` — is real and
valuable. But the claim of five closed vocabularies is falsified by the file's
own content (nine or more), nine of eleven cross-dimension collisions are
unflagged, and the one word the rule targets hardest is simultaneously the
kernel's most load-bearing field and the registry's only deliberate omission.

---

## Q3 — CORE VS ADVANCED

### 3.1 Count

**30 terms**, T-01…T-30, script-verified by counting `^#### T-` headings.
Matches the file's own `:5` ("its 30 entries") and `:1295` ("over the 30 entries
above"). No numbering gaps, no reuse. [Observed]

### 3.2 Proposed split

**CORE — 12 terms, the public set** (chosen so that every term is (i) needed to
state the thesis, (ii) has an adopted-doctrine anchor per §5, and (iii) is
distinguishable from its neighbour by a one-sentence test):

| # | Term | Reg. | Adopted anchor per §5 |
|---|---|---|---|
| 1 | Project | T-01 | yes |
| 2 | Capability | T-04 | yes |
| 3 | Desired state | T-07 | yes |
| 4 | Observed state | T-09 | yes |
| 5 | Execution state | T-11 | yes |
| 6 | Claim | T-13 | yes (SDR-2) |
| 7 | Evidence | T-14 | yes |
| 8 | Unknown | *split out of T-15* | yes (VIS-2, SDR-6) |
| 9 | Gap | T-20 | yes |
| 10 | Contradiction | T-19 | yes |
| 11 | Reconciliation | T-26 | yes |
| 12 | Mission | T-27 | **no — candidate only** |

Note on #12: Mission has no adopted definition (§5 lists T-27 among the eight),
yet it is unavoidable in the core because `README.md:47` puts Mission Control in
the four-experiences table and `OVERVIEW.md:22` puts bounded missions in the
30-second thesis. **A core set that must include a term with no adopted
definition is itself a finding** — it is P-17 restated as a structural fact, not
a deferral.

**ADVANCED — the provenance set, 18 remaining registry terms:** T-02 Governance
root, T-03 Project Genome, T-05 Requirement, T-06 State plane, T-08 Proposed
state, T-10 Inferred state, T-12 Historical state, T-15 Claim epistemic label
(the full three-label machinery), T-16 Evidence/rendering tier, T-17 Warrant,
T-18 Challenge, T-21 Source snapshot, T-22 Evaluation, T-23 Observation record,
T-24 Aligned, T-25 Converged, T-28 Autonomy envelope, T-29 Attention item,
T-30 Context packet. (That is 19 items because Unknown was promoted out of T-15
while T-15 itself stays advanced; total public surface = 12 core + 19 advanced
across 30 entries.)

### 3.3 The test: walk the default path

Default path taken as **`README.md` in full**, then **`OVERVIEW.md` Layers 1–2**
(banner `:1-16`, Layer 1 `:18-26`, Layer 2 `:27-95`, including the two mermaid
diagrams, which a reader cannot skip).

**Registry terms actually used on that path — 16 of 30:**

T-03, T-04, T-07, T-09, T-11, T-12, T-13, T-14, T-15(Unknown), T-17, T-19, T-20,
T-24, T-25, T-26, T-27.

**Violations of the proposed core-12 — terms used on the default path that are
outside it.** Every one [Observed]:

| # | Term | Where used | Why it is a violation |
|---|---|---|---|
| V1 | **Project Genome** (T-03) | `OVERVIEW.md:81-82` | Advanced-set term stated in bold in Layer 2; carries a three-tier inventory a Layer-2 reader cannot hold |
| V2 | **Historical state** (T-12) | `OVERVIEW.md:70-71` — "historical state included by adopted amendment D1" | Sixth-plane vocabulary; T-12 has **no adopted definition** (§5) yet is presented as settled by an adopted amendment |
| V3 | **Warrant** (T-17) | `OVERVIEW.md:56` — mermaid edge `warranted work` | Leaks in through a diagram label, which is the one place a reader cannot look up a term |
| V4 | **Aligned** (T-24), **Converged** (T-25) | `README.md:115` — "No claim of alignment, convergence, or regeneration capability" | Negated use, so mildest of the set — but a fresh reader still cannot tell what is being denied |
| V5 | **Claim** used in the plain-English sense | `README.md:115` — "No claim … is made anywhere" | Collides with T-13, which reserves Claim as the sole carrier of status |
| V6 | **Capability** used in the plain-English sense | `README.md:51-53` — "Mission Control is a workspace-level operator **capability**" | Directly collides with T-04, which restricts Capability identities to "the project's own declared artifacts". Also `README.md:115` "regeneration capability" |
| V7 | **kernel** | `README.md:49`; `OVERVIEW.md:61`, `:94` | **No registry entry** and no definition anywhere; see Q4.1 |
| V8 | **surface** | `README.md:44-47`, `:51`; `OVERVIEW.md:63`, `:66-74`, `:94` | **No registry entry**; see Q4.1 |
| V9 | **workspace** | `README.md:47`, `:50`; `OVERVIEW.md:72-73` | **No registry entry; zero occurrences in all of doctrine**; see Q4.1 |
| V10 | **actuator** | `OVERVIEW.md:43`, `:53` | **No registry entry** (0 occurrences in the registry, `grep -cF`); see Q4.1 |
| V11 | **owner act / act** | `OVERVIEW.md:1`, `:4`; `README.md:82` | **No registry entry**; the single most consequential noun in the current lifecycle stage |
| V12 | **projection** | `README.md:49`; `OVERVIEW.md:64` | **No registry entry**; carries VIS-6's whole rebuildability rule |
| V13 | **reconciliation work** | `OVERVIEW.md:43-44`; also `AGENTS.md:5` | Conflicts with T-26's hard reservation; see Q4.3 |
| V14 | **adapter** | `README.md:70` | **No registry entry**; VIS-5's entire outward mechanism |
| V15 | **agent fleet / fleet** | `README.md:4`, `:22`, `:62`; `OVERVIEW.md:29`, `:31`, `:39`, `:43`, `:84` | **No registry entry**; 9 uses on the default path |
| V16 | **owner** | `OVERVIEW.md:94` names it *foundational*; used throughout | **No registry entry**; defined only in `doctrine/README.md:22-24` |
| V17 | governance-lifecycle values *adopted / recorded / owner-approved / candidate* used as a bare `Status` column | `README.md:77-85`; `OVERVIEW.md:169-188` | The §1 rule's own named defect (`TERM-REGISTRY.md:55`) |

**Answer: no. The default path does not stay inside any core-12** — it exceeds
it by 4 advanced registry terms (V1–V4) and by **10 terms that have no registry
entry at all** (V7–V12, V14–V16). A core-12 is the right target; the current
default path needs either those 10 terms admitted, or the sentences rewritten to
avoid them. Both are cheap; neither has been done.

---

## Q4 — UNDEFINED / OVERLAPPING / CONFLICTING

### 4.1 (a) Used on the default path, defined nowhere reachable

All [Observed]. "Reachable" = findable by following links from `README.md` or
`OVERVIEW.md` without prior knowledge of the tree.

| Term | Default-path use | Registry entry | Adopted definition | Verdict |
|---|---|---|---|---|
| **workspace** | `README.md:47`, `:50`; `OVERVIEW.md:72-73` | none | **none — 0 occurrences in the entire `doctrine/` tree** (Python `re` walk: 0; `grep -rniF workspace .syzygy/governance/doctrine/` → exit 1, no output) | **Undefined.** The only definition is `TERM-REGISTRY.md:146-148`, inside T-01's *deprecated-synonyms* field, which says a workspace "is a distinct, portfolio-level concept (RFC10-15, **candidate**)" — a definition given in a negative field of a candidate file, pointing at an unaccepted contract |
| **actuator** | `OVERVIEW.md:43`, `:53` ("agent fleets are the actuators") | none (`grep -cF actuator` → 0) | none — `doctrine/README.md:42` says "workers and actuators" without defining either | **Undefined.** Confirms RB-1 F6's residual |
| **kernel** | `README.md:49`; `OVERVIEW.md:61`, `:94` | none (12 uses of "kernel" *as a modifier* inside the registry, e.g. `:141` "kernel invariant", `:280` "the kernel holds references") | `architecture.md:261` has a heading "One kernel, three surfaces" and `:263` "The kernel's shared semantics" — **usage, never a definition** | **Undefined.** A term the registry uses 12 times and never admits |
| **surface** | `README.md:44-47`, `:51`; `OVERVIEW.md:63-74`, `:94` | none | `architecture.md:269-271` enumerates three surfaces with codenames; `doctrine/README.md:36-38` repeats them — an enumeration, not a definition. "Surface" then acquires a *fourth* sense at `TERM-REGISTRY.md:679` ("sibling **surface** states") meaning a rendering slot | **Under-defined and overloaded** |
| **owner act / act** | `OVERVIEW.md:1`, `:4`; `README.md:82` | none | `grep`: "owner act" → **0 occurrences in `architecture.md`**. Defined only in RFC-0003 (candidate) | **Undefined**, and it is the noun the entire current stage turns on |
| **projection** | `README.md:49`; `OVERVIEW.md:64` | none | `architecture.md:64`, `:99`, `:277` use it; VIS-6 states the rule without naming the noun | **Under-defined** |
| **adapter** | `README.md:70` | none | VIS-5 (`vision.md:149-153`) defines "typed, explicitly authorized adapters" operationally — the best-covered of this list | **Adequately covered by doctrine; still unregistered** |
| **agent fleet** | 9 default-path uses | none | used throughout doctrine, never defined | **Undefined** |
| **owner** | `OVERVIEW.md:94` (named "foundational") | none | `doctrine/README.md:22-24` — a good definition, in the one file **neither `README.md` nor `OVERVIEW.md` links directly**; `README.md:79` links the *directory*, which renders it on GitHub but not in a local clone or editor | **Defined, weakly reachable** |
| **machine query plane** | `OVERVIEW.md:63` | none | none found | **Undefined** |
| **control plane** | `README.md:3`; `vision.md:16` | none | none found | **Undefined**, and it is the product's one-line self-description |

### 4.2 (b) Pairs a reader could not choose between

| Pair | Overlap | Cites |
|---|---|---|
| **Project Genome (T-03)** vs **Desired state (T-07)** | T-03 = "the complete normative corpus"; T-07 = "adopted governance and spec state: capabilities, requirement and scenario references, decisions, policies, topology entries…". The two enumerations are near-identical. T-07's *Related but distinct* field asserts they differ — "the corpus, not the plane" — but never says an artifact can be **both**, which it plainly is (an adopted topology entry is Genome *and* Desired-plane). A reader asked "is doctrine Genome or Desired?" gets no rule | `TERM-REGISTRY.md:200-211` vs `:346-351`; distinction claimed at `:364` and `:224` |
| **Warrant (T-17)** vs **Mission (T-27)** | T-17 = "the recorded authority that permits an act"; T-27 = "authority to *proceed inside* the gates". T-17's closed four-class warrant list includes "an explicit owner decision" — and T-27 requires an "**initiating owner act**". So a Mission either *is* a warrant or *contains* one, and neither entry says which. T-27's *Related but distinct* names Warrant with no distinguishing sentence | `:708-720` vs `:1116-1128`; non-distinction at `:733` and `:1145` |
| **Source snapshot (T-21)** vs **Context packet (T-30)** | Both are closed, digest-bound, immutable input sets that enumerate decisions, contradictions, challenges, and an evaluation. T-30 offers the one real discriminator — "inputs to an evaluation, not to a run" — but only in its *Related but distinct* field, never in either formal definition | `:862-877` vs `:1250-1268`; discriminator at `:1281` |
| **Evidence tier (T-16)** vs the three **sibling surface states** | Both are closed sets of rendering-affecting values; T-16 says the siblings "sit **outside** the registry" and *replace* a status rendering, while tiers *qualify* one. A reader choosing between `unadopted-draft` (sibling) and `declared-only` (tier) for a drafted capability with a declared mapping has no rule — and `T-07:370` renders exactly that case `unadopted-draft` while `T-16:696-698` renders it `declared-only` | `:679-682` vs `:370` vs `:696-698` |
| **Challenge (T-18)** vs **Contradiction (T-19)** | Well separated. Recorded as a **positive** finding | `:771`, `:806-809` |
| **Gap (T-20)** vs **Contradiction (T-19)** | Well separated, with the load-bearing reason stated. **Positive** | `:806-809` |
| **Aligned (T-24)** vs **Converged (T-25)** | Well separated ("Aligned is not the singular of Converged"). **Positive** | `:1010-1012` |

### 4.3 (c) Defined differently in two places

**C1 — "Reconciliation": the reservation is violated on the public default path
and in agent operating procedure.** [Observed]

`TERM-REGISTRY.md:1065-1067`:

> **Unqualified "reconciliation" means exactly one thing in Syzygy: the
> post-merge evaluation of whether a merged change satisfies the intent revision
> that warranted it.**

`OVERVIEW.md:42-44` (Layer 2, default path):

> The computed difference becomes **reconciliation work**, and agent fleets are
> the actuators that perform it.

`AGENTS.md:5`:

> the difference becomes reconciliation work

These are *incompatible*. In T-26, reconciliation is what happens **after** a
merge, to check it. In OVERVIEW/AGENTS, "reconciliation work" is the work
generated **before** any merge, from the desired-vs-observed delta — which T-20
calls a **Gap**. The registry's own hard reservation (`:1084-1090`: "the two
senses never share a field, a count, or a UI string") is broken by the project's
own public overview and its agent procedure file. "reconciliation work" occurs
**0 times** in all 32 candidate contract modules (Python `re`, confirmed), so
the presentation layer minted a sense the contracts do not carry.

**C2 — "Evidence tier" vs "rendering tier": the registry renamed a term against
its owning authority, and the corpus disagrees with the registry about which
spelling is primary.** [Observed]

- `TERM-REGISTRY.md:661` — the entry is titled **`T-16 · Evidence tier`**;
  `:689-690` demotes the other spelling: "**Permitted aliases.** *rendering
  tier* (the corpus's own term — see the migration report; both spellings are in
  use)."
- The owning authority is RFC2-25, which lives in a file literally named
  `rfcs/RFC-0002/rendering-vocabularies.md`, and `rfcs/RFC-0002/README.md:103`
  calls it "the **closed registry of rendering tiers** (six tiers)".
- Occurrence counts across the 32 modules: **`rendering tier` = 5**
  (`RFC-0001-…:306`, `RFC-0006-…:208`, `RFC-0002/README.md:103`,
  `RFC-0002/rendering-vocabularies.md:195`, `RFC-0008/state-vocabulary-and-cost.md:123`);
  **`evidence tier` = 2** (`RFC-0010-…:148`, `RFC-0005/execution-profiles.md:112`).

So the registry made the **minority** spelling primary and the owning
authority's spelling an alias. This contradicts the registry's own banner
(`:8-11`, "Owning authorities always win over this registry's restatements") and
its own §6 claim (`:1334`, "**Nothing was renamed, replaced, or migrated
anywhere in the repository**") — the rename happened inside the registry itself,
which is where it matters most.

**C3 — the same seam is simultaneously "settled by alias" and "an open owner
question."** `TERM-REGISTRY.md:689-690` treats it as resolved;
`decisions/PENDING-OWNER-DECISIONS.md:63` (P-18(c)) records it as an unresolved
contradiction that "wants an owner ruling before OpenSpec multiplies them."
Both files are current. A reader cannot tell whether the question is open.
[Observed]

**C4 — "Capability": kernel identity vs plain English, on the public front
page.** `TERM-REGISTRY.md:239-247` restricts Capability identities to the
project's own declared artifacts; `README.md:51-53` calls Mission Control "a
workspace-level operator **capability**," which is the ordinary-English sense and
is not a Capability. [Observed]

**C5 — Doctrine's frozen nouns vs the registry's set.** `architecture.md:287-289`
freezes thirteen technical nouns. `TERM-REGISTRY.md:1311-1319` reports this
honestly, including the "Claim" omission — **this is a positive finding.** But
the frozen list contains **genome-complete**, for which the registry has *no
entry* (conceded at `:1319`), so an adopted, frozen, citable noun is absent
from the artifact that claims to be the public vocabulary. [Observed]

---

## Q5 — GLOSSARY FINDING (verified, not assumed)

### 5.1 What is actually true

1. **A glossary exists.** `.syzygy/governance/doctrine/README.md:15` is
   `## Glossary (read first)`, running `:15-49`. It defines Syzygy, Owner,
   Governed project, the two namespaces, Polaris/Trajectory/Orrery, the
   substrate tools, and the rule identifiers. [Observed — read in full.]
2. **`vision.md` cites it twice, both times as "README glossary" with no path:**
   - `vision.md:16` — "Syzygy (see README glossary) is a specification-driven
     software control plane"
   - `vision.md:39` — "it assumes the public actuator toolchain (README
     glossary), never one private machine"
   - and a third site outside `vision.md`: `v1.md:98` — "the public
     ai-bootstrap toolchain (README glossary)".
3. **The repository-root `README.md` has no glossary.** Verified two ways:
   Python `re` walk for `/glossar/i` over every tracked `.md` → 0 hits in
   `README.md`; `grep -rniF glossar --include=*.md .` → 0 hits in `README.md`.
   Its headings are Why it exists / The four experiences / The core loop / What
   is authoritative here / Start here / What is not implemented / License.
   [Observed]
4. **`OVERVIEW.md` has no glossary either**, and neither `README.md` nor
   `OVERVIEW.md` links directly to `doctrine/README.md`. `README.md:79` links the
   *directory* `.syzygy/governance/doctrine/` (which GitHub renders as that
   README, but a local clone or editor does not); `OVERVIEW.md:171-175` links five
   individual doctrine files and **not** the one holding the glossary. [Observed]

### 5.2 Was the prior finding correct?

**Split — and the split matters.**

- **The original reviewer was substantially correct and appropriately careful.**
  `round-2026-08/reviews/RB-1-fresh-engineer-RAW.md:269-289` states the finding
  *and* states the resolution: at `:284-286` it writes "The intended target is
  almost certainly `.syzygy/governance/doctrine/README.md:15`, '## Glossary (read
  first)', which does define Syzygy, Owner, governed project…". RB-1 did **not**
  claim the doctrine glossary was absent. Its actual claim — that the *root*
  README has no glossary, that adopted doctrine's citation does not say which
  README, and that neither README points at the other — is **true on all three
  legs**.
- **Every downstream restatement dropped the nuance and became false as
  written.** Five tracked artifacts now assert flatly that the glossary does not
  exist:
  - `round-2026-08/ROUND-DISPOSITIONS.md:87` — "**Adopted doctrine cites a
    'README glossary' that does not exist**"
  - `round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md:119` — same phrasing
  - `round-2026-08/FINAL-HUMAN-CLARITY-REVIEW.md:49` — same
  - `round-2026-08/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md:36` — same
  - `decisions/PENDING-OWNER-DECISIONS.md:65` (P-20) — "doctrine's citation of a
    'README glossary' **that does not exist**"

  The last is the one the owner reads at decision time, and it is wrong: the
  glossary exists, at `doctrine/README.md:15`. This is the corpus's own
  documented hazard — a derived restatement going stale against its source —
  reproduced inside the round's own findings chain. [Observed]

### 5.3 The real defects, separated

These are **three** different defects needing three different fixes. Conflating
them is what produced the false restatement.

| # | Defect | Fix | Cost |
|---|---|---|---|
| **D-a** | **Ambiguous citation.** Adopted doctrine says "README glossary" at three sites without saying which README, and the root README is the one a reader is statistically holding | Doctrine amendment changing three strings to "(doctrine README glossary)" or a relative link. **Not** a missing-artifact fix | One doctrine amendment, three string edits, zero new content |
| **D-b** | **Broken reachability.** The only glossary in the repository is linked from neither `README.md` nor `OVERVIEW.md` by file path | Add one link. `README.md` "Start here" and `OVERVIEW.md:171-175` are both presentation artifacts — **no doctrine amendment needed** | One line each |
| **D-c** | **Genuinely undefined terms.** "actuator toolchain" (`vision.md:38`), "ai-bootstrap toolchain" (`v1.md:98`), "actuator" (`OVERVIEW.md:43`, `:53`) are load-bearing and defined **nowhere**, glossary included. `grep -cF actuator TERM-REGISTRY.md` → 0 | Add glossary entries (a doctrine amendment) **or** registry entries. This is the only leg that is a missing-artifact defect | New content |

P-20's one-line summary collapses D-a, D-b and D-c into "a glossary that does not
exist," which is false for D-a/D-b and understates D-c. **Recommended
correction to P-20:** replace that clause with "adopted doctrine cites the
doctrine README glossary ambiguously as 'README glossary' at three sites
(`vision.md:16`, `vision.md:39`, `v1.md:98`); the glossary exists at
`doctrine/README.md:15` but is unlinked from the public front door, and
'actuator toolchain' / 'ai-bootstrap toolchain' are defined nowhere."

---

## Q6 — TERM-ADMISSION RULE

### 6.1 What the registry states

`TERM-REGISTRY.md:101-113`:

> **A new durable term is admitted only when all four hold:**
> 1. **no existing term covers it** — check this registry first;
> 2. **its distinction matters operationally** — something is rendered, counted,
>    gated, routed, or refused differently because the distinction exists;
> 3. **its authority is clear** — exactly one artifact owns the definition, and
>    the term's entry can name it;
> 4. **a newcomer can explain it after one paragraph.**
>
> A term failing any of the four is a phrase, not vocabulary. … Terms are scarce
> on purpose: every admitted term is a thing every future reader must learn.

With a corollary at `:115-119`. **A rule exists, and it is a good one.** The
scarcity framing and the "real distinction / merely felt distinction" corollary
are the strongest paragraphs in the document.

### 6.2 Judged against the five required criteria

| Required criterion | Registry clause | Verdict |
|---|---|---|
| No existing adequate term | §3(1) `:103` | **Present but unrunnable.** §3(1) says "check this registry first," and §6 (`:1328-1329`) concedes "The corpus was not swept for terms used normatively that are absent from this registry entirely." A completeness check against an admittedly incomplete inventory returns a false negative by construction. Q4.1 gives eleven live examples |
| Operationally meaningful distinction | §3(2) `:104-106` | **Present and well drafted.** "rendered, counted, gated, routed, or refused" is a testable list. No gap |
| Identified **owner** | §3(3) `:107-108` | **Present but too weak.** "Exactly one artifact owns the definition" is satisfied by an **unaccepted candidate clause** — which is how eight of thirty terms (`:1300`) pass a rule whose whole purpose is authority clarity. The rule needs a typed threshold: adopted-owned terms are admitted; candidate-owned terms are *provisionally listed* and marked, never admitted |
| Identified **lifecycle** | **absent** | **GAP.** §3 says nothing about how a term is amended, deprecated, retired, or superseded; nothing about who performs an admission; nothing about where an admission is recorded. `:18-19` gives ID stability ("amended in place or retired; never renumbered") but no *procedure*. The only procedure in the repository sits in a *different candidate file* (`CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:115-126`, CC-KNOW-6's migration-report requirement) and §3 does not cite it |
| One-sentence plain-language explanation | **absent as a rule** | **GAP.** All 30 entries carry a **Plain language** field and `:32` says such sentences "are **reading aids** and are never the definition" — but §3 never *requires* a new term to have one. §3(4) asks for "one paragraph," not one sentence, and asks it of the *newcomer's* output rather than the *entry's* content. No field schema is stated anywhere (independently found as RB-3 F12) |
| Passes a fresh-reader **distinction** test | **absent** | **GAP, and the most serious.** §3(4) is a *comprehension* test ("a newcomer can explain it"), not a *distinction* test ("a newcomer, shown this term and its nearest neighbour, picks the right one"). Q4.2 shows exactly why the difference matters: Genome/Desired, Warrant/Mission, Snapshot/Packet, tier/sibling-state each pass comprehension individually and fail distinction pairwise. Worse, `:1332` concedes "**No newcomer comprehension test has been run** on any of the 30 entries" — so even the weaker test is unexecuted |

### 6.3 Additional gaps found

- **The rule is admittedly retroactively inert.** `:1330-1331`: "**The admission
  rule (§3) was applied to no incumbent term.** Every entry is vocabulary
  admitted by prior use." Honest, and it means all 30 entries are grandfathered.
  A rule that has never been applied to anything has no evidence of being
  applicable. [Observed]
- **No admitting authority.** §3 states conditions, never who checks them or
  whose act admits. Under VIS-4 this matters: is admitting a term a shape-level
  delta needing owner sign-off, or agent-draftable?
- **No rejection record.** Nothing says where a refused term is written down, so
  the same term can be re-proposed indefinitely. `:118` refuses "status" in one
  sentence with no record structure behind it.
- **The rule contradicts a live practice.** §3(3) demands exactly one owning
  artifact, yet the registry's own entries routinely name two (e.g. T-01 at
  `:139-141` names `architecture.md` **and** RFC1-1; T-13 at `:559-562` names
  four). The rule as written would refuse the registry's own best entries.

---

## VERDICT AND FINDINGS

**VERDICT: REVISE**

Rationale in one paragraph: this is a serious, unusually candid artifact — §5's
authority-coverage table, §6's list of what it does not establish, and §1's
Observed/Inferred double-binding note are better self-disclosure than most
adopted corpora manage. But three of its load-bearing frame claims are falsified
by its own content (the title's "canonical," §2's heading, §1's "five closed
vocabularies"), it renames a term against its owning authority in the one field
where that is most consequential, and its two public-surface consequences — the
"full vocabulary" sentence and the "reconciliation work" sense — are wrong on the
default reading path. These are cheap to fix in bytes and expensive to leave,
because they change what the document *claims*, not merely how it reads. It
should not go to an owner act in this form.

---

### Findings

**F1 — [Blocking] · The title and the §2 heading claim canonicity the file
itself disclaims.**
`TERM-REGISTRY.md:1` ("Syzygy's canonical public vocabulary") vs `:3`
("**Status: CANDIDATE. This file binds nothing.**"); `TERM-REGISTRY.md:72`
("The six-plane state model (canonical)") vs `:92-95` ("the six-plane model is
**candidate** … `vision.md` is still what governs").
*Minimal fix:* title → `# Term registry (candidate) — a proposed public
vocabulary for Syzygy`; §2 heading → `## 2. The six-plane state model (candidate
— a drafting convention, not an adopted model)`. Two lines.

**F2 — [Blocking] · "Five different closed vocabularies" is false by the
registry's own content; there are at least nine.**
`TERM-REGISTRY.md:38-39` vs the six further closed sets the same file names:
claim status (`:551`), freshness state (`:649-650`), challenge state (`:753-754`),
chain state (`:1068-1073`), sibling surface states (`:679-682`), mission
lifecycle (`:1200`).
*Minimal fix:* rewrite `:38-39` as "Five dimensions are routinely confused
because English offers one word for all of them. Four further closed
vocabularies exist and are named where they arise (§Q2 table); none of them is a
sixth dimension of *this* table," and add a one-row-each appendix listing them
with their owning clause.

**F3 — [Blocking] · Nine cross-dimension token collisions are unflagged; two sit
inside the §1 table itself.**
`active` — work lifecycle `:47` **and** governance lifecycle `:48`, adjacent
rows. `merged` and `reconciled` — work lifecycle **and** chain state, the same
cell `:47`. Also `Unknown` (`:45` vs `:47`), `superseded` (`:48` vs `:525`),
`expired` (`:48` vs `:754`), `blocked` (`:47` vs `:1200`), `draft` (`:48` vs
`:679-680`).
*Minimal fix:* extend the existing `:61-66` treatment — which is exactly right
for Observed/Inferred — to a short table covering all nine, each with its
disambiguating phrase ("the `active` work state" / "an active decision").

**F4 — [Blocking] · The `status` rule is unenforceable, and the corpus's most
load-bearing word is deliberately left undefined while the registry defines
Claim in terms of it.**
Rule at `:52-56`; refusal at `:118`; but `status` is a first-class kernel field
distinct from all five dimensions (`:551`; `rfcs/RFC-0001-…:305-307`), appears
**42×** in the registry, **224×** across the 32 candidate modules, and carries at
least four incompatible senses — claim status (`:554`), governance-lifecycle
"effective/adoption status" (`:867`, `:873`, `:896`;
`rfcs/RFC-0003/governance-homes-and-owner-acts.md:104-105`, `:126-127`),
work-lifecycle "raw substrate status"
(`rfcs/RFC-0008/state-vocabulary-and-cost.md:168-171`), and membership status
(`doctrine/architecture.md:155`). Worst single site: **T-21 uses three senses in
one entry** (`:865`, `:867`, `:873`). Worst public site: `OVERVIEW.md:4`
("effective status lives in the owner-act record") vs `OVERVIEW.md:114` ("Every
status is computed at an identified evaluation") — the second falsifies the
first. Two literal `Status` columns on the most-read tables: `README.md:77`,
`OVERVIEW.md:169`.
*Minimal fix:* add **T-31 · Claim status** with its enumerated value set from
RFC1-18 (or record `[Unknown]` if the contracts never enumerate it — which
appears to be the case, and would itself be the finding), and add to §1 a
three-row substitution table: *claim status* / *effective (governance-lifecycle)
status* / *raw substrate status*. Rename the two `Status` columns to
`Governance status`.

**F5 — [Blocking] · T-16 renames a term against its owning authority, and §6's
"nothing was renamed" is false of the registry itself.**
`TERM-REGISTRY.md:661` titles the entry *Evidence tier* and `:689-690` demotes
*rendering tier* to an alias, while the owning authority is RFC2-25 in
`rfcs/RFC-0002/rendering-vocabularies.md`, and `rfcs/RFC-0002/README.md:103`
calls it "the closed registry of **rendering tiers**." Corpus counts: `rendering
tier` = 5, `evidence tier` = 2. This violates the registry's own precedence rule
(`:8-11`) and its own §6 claim (`:1334`). It also contradicts
`decisions/PENDING-OWNER-DECISIONS.md:63` (P-18(c)), which records the same seam
as an **open** owner question.
*Minimal fix:* retitle T-16 `T-16 · Rendering tier`, list *evidence tier* as the
alias, and add one sentence recording P-18(c) as open.

**F6 — [Blocking] · `OVERVIEW.md:93-95` overstates the registry on the public
default path, and is falsified by its own sentence.**
"the full vocabulary lives in the term registry" — four of the nine terms named
in that same sentence (*reconciliation work*, *kernel*, *surface*, *owner*) have
no registry entry. No candidate marker, no `*Sources:*` anchor, no link — all
three required by the file's own banner at `:7-11`.
*Minimal fix:* the replacement sentence given in §Q1.6.

**F7 — [Blocking] · "Reconciliation work" on the default path violates T-26's
hard reservation.**
`OVERVIEW.md:43-44` and `AGENTS.md:5` use "reconciliation work" for the
*pre-merge* desired-vs-observed delta, which T-26 (`:1065-1067`, `:1084-1090`)
reserves exclusively for the *post-merge* satisfaction evaluation. The phrase
occurs **0 times** in all 32 candidate modules — the presentation layer minted
it. Under T-20 the correct word is **Gap**.
*Minimal fix:* `OVERVIEW.md:43` → "The computed difference becomes **gaps**, and
agent fleets are the actuators that close them"; same in `AGENTS.md:5`; update
the mermaid node at `OVERVIEW.md:52` (`Diff["Reconciliation work"]` →
`Diff["Gaps"]`).

**F8 — [Blocking] · Ten terms are used on the public default path with no
registry entry and no adopted definition.**
*kernel* (`README.md:49`, `OVERVIEW.md:61`), *surface* (`README.md:44-47`,
`OVERVIEW.md:63-74`), *workspace* (`README.md:47`, `:50`, `OVERVIEW.md:72-73` —
**zero occurrences in the entire doctrine tree**, verified twice), *actuator*
(`OVERVIEW.md:43`, `:53` — zero occurrences in the registry), *owner act*
(`OVERVIEW.md:1`, `:4`, `README.md:82`), *projection* (`README.md:49`),
*adapter* (`README.md:70`), *agent fleet* (9 sites), *owner*
(`OVERVIEW.md:94`), *machine query plane* (`OVERVIEW.md:63`), *control plane*
(`README.md:3`).
*Minimal fix:* admit *kernel*, *surface*, *workspace*, *owner act*, *actuator*
as T-31…T-35 (each is operationally load-bearing per §3(2)); route *owner*,
*agent fleet*, *adapter*, *projection* to the doctrine glossary and link it from
`README.md` "Start here".

**F9 — [Non-blocking] · The default path exceeds any core-12 by 14 terms.**
Full table at §Q3.3 (V1–V17). Beyond F8's ten, the registry-term overflows are
Project Genome (`OVERVIEW.md:81`), Historical state (`OVERVIEW.md:70`), Warrant
via a mermaid label (`OVERVIEW.md:56`), Aligned/Converged (`README.md:115`).
*Minimal fix:* adopt the core-12 below as a stated budget for `README.md` +
`OVERVIEW.md` Layers 1–2, then move V1–V4 to Layer 3, or gloss each in place in
one clause.

**F10 — [Non-blocking] · The propagated "README glossary does not exist" finding
is false as restated; the original review was correct and was flattened.**
The glossary **exists** at `doctrine/README.md:15`, and RB-1 said so
(`RB-1-fresh-engineer-RAW.md:284-286`). Five downstream artifacts assert it does
not: `ROUND-DISPOSITIONS.md:87`, `PUBLIC-CLONE-VERIFICATION-REPORT.md:119`,
`FINAL-HUMAN-CLARITY-REVIEW.md:49`,
`FINAL-PRE-SPECIFICATION-READINESS-REPORT.md:36`, and — the one the owner
decides from — `PENDING-OWNER-DECISIONS.md:65`. Three separate defects were
conflated into one: **D-a** ambiguous citation (`vision.md:16`, `:39`,
`v1.md:98`) → doctrine amendment; **D-b** the glossary is unlinked from
`README.md`/`OVERVIEW.md` → presentation fix, no amendment; **D-c** "actuator
toolchain" / "ai-bootstrap toolchain" / "actuator" defined nowhere → new
content. Full separation at §Q5.3.
*Minimal fix:* replace the P-20 clause with the corrected wording in §Q5.3, and
correct the four round artifacts (they are derived records, not act-bound).

**F11 — [Non-blocking] · The admission rule has four gaps against the required
bar.**
No **lifecycle** (no amend/retire/supersede procedure, no admitting authority,
no admission record); no requirement that an entry carry a **one-sentence
plain-language** explanation (and no field schema at all); §3(4) is a
*comprehension* test, not a **distinction** test — and `:1332` records that even
that test has been run on zero entries; §3(1) is unrunnable because §6
(`:1328-1329`) concedes the corpus was never swept for unregistered terms.
Additionally §3(3) is satisfiable by an unaccepted candidate clause, which is
how eight of thirty terms (`:1300`) pass an authority-clarity test, and §3(3)'s
"exactly one artifact" is contradicted by the registry's own multi-authority
entries (`:139-141`, `:559-562`).
*Minimal fix:* add a fifth condition — "a fresh reader shown this term and its
nearest registered neighbour picks the right one" — plus a short §3.1 stating
the entry field schema, the admitting act, and the retire/supersede path (or a
citation to CC-KNOW-6 for the latter); and split §3(3) into *adopted-owned →
admitted* / *candidate-owned → provisionally listed and marked*.

**F12 — [Non-blocking] · Four term pairs are not separable by a reader.**
Project Genome vs Desired state (`:200-211` vs `:346-351`, non-distinction at
`:364`); Warrant vs Mission (`:708-720` vs `:1116-1128`, non-distinction at
`:733`/`:1145`); Source snapshot vs Context packet (`:862-877` vs `:1250-1268`,
discriminator buried at `:1281`); Evidence tier vs sibling surface states, which
render the *same case* two different ways (`:370` says `unadopted-draft`,
`:696-698` says `declared-only`).
*Minimal fix:* one discriminating sentence in each formal definition — not in
the *Related but distinct* field, which readers reach after they have already
chosen. Resolve the `:370` / `:696-698` disagreement explicitly.

**F13 — [Non-blocking] · An adopted frozen noun has no registry entry.**
`architecture.md:287-289` freezes *genome-complete*; `TERM-REGISTRY.md:1319`
concedes it "has no registry entry of its own." A frozen, citable, adopted noun
is missing from the artifact that proposes to be the public vocabulary.
*Minimal fix:* add T-31 · Genome-complete, sourced verbatim from
`architecture.md:178-186`. It is one of the cheapest entries available and one
of the few with a fully adopted definition.

**F14 — [Non-blocking] · CC-KNOW-6 calls the registry "canonical" and would
mass-violate on commencement.**
`CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:117`. Under CC-KNOW-6, every unregistered
normative term becomes an "unadmitted term" — which on the evidence above
includes `status` (224 corpus uses), *kernel*, *surface*, *workspace*,
*actuator*, *owner act*, *adapter*, *projection*, and *genome-complete*.
*Minimal fix:* delete "canonical"; add a commencement clause limiting CC-KNOW-6
to terms introduced after the registry's accepting act.

---

### Proposed CORE-12 term list

1. **Project** (T-01)
2. **Capability** (T-04)
3. **Desired state** (T-07)
4. **Observed state** (T-09)
5. **Execution state** (T-11)
6. **Claim** (T-13)
7. **Evidence** (T-14)
8. **Unknown** (promoted out of T-15)
9. **Gap** (T-20)
10. **Contradiction** (T-19)
11. **Reconciliation** (T-26)
12. **Mission** (T-27 — *the only core term with no adopted definition; see
    F-note in §Q3.2*)

Everything else in the registry becomes the **ADVANCED provenance set** (19
entries): T-02, T-03, T-05, T-06, T-08, T-10, T-12, T-15, T-16, T-17, T-18,
T-21, T-22, T-23, T-24, T-25, T-28, T-29, T-30.

---

### Standing limits of this review

- I read the 32 candidate contract modules **only by targeted sweep**, per scope.
  Counts of `status`, `rendering tier`, `evidence tier`, `reconciliation work`,
  and `workspace` are complete over those files; my reading of their *meaning* is
  based on the quoted lines and the registry's restatements, not on full reads.
  [Inferred] where I characterize contract intent.
- I did **not** run a full lexical sweep for normatively-used terms absent from
  the registry — the same gap `TERM-REGISTRY.md:1328-1329` records. Q4.1's list
  of eleven is what the default-path walk surfaced, not an exhaustive inventory.
- I did not verify any digest, and performed no act-related check.
- No fresh-reader comprehension test was run on the 30 entries here either; §Q6
  judges the *rule*, not the entries' comprehensibility.
