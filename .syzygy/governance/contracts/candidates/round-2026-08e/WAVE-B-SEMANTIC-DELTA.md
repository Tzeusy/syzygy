# Wave B (R-B) semantic delta — round-2026-08e

> **Process bookkeeping — never authority.** This file records what the R-B
> repair batch changed in the eleven Wave B modules (RFC 0007–0009), why, and
> whether each change moves the wave's content digest. **Nothing here is
> accepted, adopted, or installed.** Every edited file remains a *candidate*;
> the owner ratifies or reverts the whole set at the Wave B act (VIS-4). No
> act was performed, no manifest was regenerated, and no acceptance record was
> touched.
>
> Written under the round-2026-08d disposition register's `repair(R-B)` rows
> and §3 cross-cutting designs X1 and X2. Finding text authority is the raw
> review beside the register; where this file and a raw review disagree, the
> raw review wins.
>
> **Subject bytes were frozen for RD-10, RD-15 and RD-19 at baseline
> `771965c`.** Editing them retires those reviews for Wave B (verification
> rule 10); the disposition register §7 already provides for that — the wave
> now owes a fresh-context exact-package review of the new bytes before it may
> be offered.

---

## 0. Scope, boundary, and what was *not* touched

**Edited — all eleven Wave B modules, and nothing else:**

| File | Words before → after |
|---|---|
| `rfcs/RFC-0007/README.md` | 2333 → 2501 |
| `rfcs/RFC-0007/narrative-contract.md` | 5172 → 5253 |
| `rfcs/RFC-0007/rendering-and-surface.md` | 3411 → 4568 |
| `rfcs/RFC-0008/README.md` | 1964 → 2037 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | 3051 → 3797 |
| `rfcs/RFC-0008/identity-authority-materialization.md` | 2684 → 2717 |
| `rfcs/RFC-0008/state-vocabulary-and-cost.md` | 3504 → 4069 |
| `rfcs/RFC-0009/README.md` | 1898 → 2142 |
| `rfcs/RFC-0009/interaction-parity-and-release.md` | 3023 → 3401 |
| `rfcs/RFC-0009/semantic-geography.md` | 7079 → 7777 |
| `rfcs/RFC-0009/visual-grammar-and-lenses.md` | 5534 → 5840 |

[Observed] Wave B total 39,653 → 44,102 words (+11.2%). Counts computed this
session by `len(text.split())` over the working-tree bytes against a
`git archive HEAD` copy; **not transcribed from any report**, and stale the
moment any module moves — the generated budget report is the owning artifact.

**Not touched, deliberately:** every manifest, the acceptance record,
RFC 0001–0006, RFC 0010/0011, `fixtures/`, `scripts/`, the routing matrix,
the routers, the dependency and contract indices, and the budget report. Four
of those need regeneration or repair because of these edits — see §9.

**Clause-identity discipline held.** No clause was renumbered, retired, or
merged. **No new numbered clause was minted** in any package (`ENDS` in
`verify_final_prespec.py` closes RFC7 at 40, RFC8 at 32, RFC9 at 52, and
`build_active_manifest`'s populations are unchanged). Two obligations that a
reviewer's repair note proposed as *new integers* were instead written as
limbs of existing clauses; both departures are stated at the finding, with
the reason (§4.3, §6.4).

---

## 1. THE HEADLINE ITEM — RFC9-8(a) no longer relies on the Mission waves

**Findings:** RD-19 **M2** (clause arm) + RD-10 **F11**. Owner charter §11.1.
**Clause:** `rfcs/RFC-0009/semantic-geography.md`, **RFC9-8(a)**.
**Digest-moving: yes.**

### 1.1 The old reliance, quoted

> "**This machinery is authority-bearing, and a registry that changes
> authorization, evaluation inputs, stable identity, layout truth, or any other
> project fact belongs in typed governance, never in personal presentation
> state** — so it lives in the typed **workspace governance store** (RFC10-15),
> never in the workspace manifest… (Staged reference: until an accepted
> RFC 0010 mints the store, no portfolio re-lay is lawful — the machinery waits
> with the store, and the manifest never substitutes.)"

RD-19's sweep established the exposure precisely: this was the **only**
clause-level citation of a not-yet-bound artifact anywhere in Wave B, and it
was a *reliance*, not a citation — the clause's operative placement obligation
named an RFC 0010 clause as the store's home, and the condition releasing the
bar ("until an accepted RFC 0010 mints the store") is itself gated on
`RFC-0010/README.md`'s **open** §8 q3. An owner performing Wave B was
accepting a permanent bar on portfolio re-lay whose release depended on a
ruling not yet made, in a contract not yet offered.

### 1.2 The new grounding, quoted

The authority-bearing sentence is **kept verbatim** — the owner's P-22 /
packet-6 ruling that the registry belongs to the governance plane is
preserved, not reversed — and the *home* is now stated in RFC 0003's terms:

> "**Where it lives, in the terms RFC 0003 already fixes.** The registry, its
> reorganisation events, and their recorded rationale are
> **authorization-bearing governance artifacts** under **RFC3-16(a)** — they fix
> the meaning of a rendered encoding rather than report a fact under it, the
> same limb that puts RFC9-18 inside the predicate. So they live in a **typed,
> owner-gated governance store**: an artifact of the governance class RFC3-15
> fixes, durable, honored **only under RFC3-16(a)**, an entry whose owner-act
> provenance does not verify treated exactly as an absent one (RFC9-18's rule,
> at portfolio scope). **Never the workspace manifest and never `local/`:** both
> are personal presentation state under VIS-6 exception (a) and are **never
> snapshot inputs** (RFC3-10, RFC3-11, RFC3-21), while the layout version and
> baseline **are** (RFC2-1 item 7; RFC9-14(a)) — so a personal-state home is
> barred by RFC 0003's own rule, not by preference. …"

and the fail-closed consequence is now derived from Wave A's own silence
rather than from RFC 0010's absence:

> "**Until such a store exists at workspace scope, no portfolio re-lay is
> lawful — and that is the operative rule.** RFC 0003 fixes governance homes at
> **project** scope (RFC3-15) and puts the workspace manifest outside every
> governed plane (RFC3-10); it establishes no home at workspace scope, and
> establishing one is an owner act of RFC3-15(a)'s recorded-widening class — the
> precedent B19 set when it minted `records/` rather than stretching a
> category's "exclusively". The consequence is fail-closed and complete on its
> own terms: the machinery waits with the store, **the manifest never
> substitutes**, and no re-lay may be performed meanwhile. Nothing here is
> conditioned on an unaccepted contract; a reader holding RFC 0001–RFC 0009 can
> evaluate every condition this clause states."

### 1.3 The staging note, quoted

> "*(**Staged successor, not a reliance.** A drafted successor already exists in
> candidate material — RFC 0010's typed workspace governance store,
> **RFC10-15** — and on acceptance it becomes this registry's home **without
> amending this clause**, since the rule above names a class and a gate rather
> than a path. It is named for orientation only: a citation, not a reliance. If
> RFC 0010 is never accepted, the rule above still stands and still
> fail-closes.)*"

### 1.4 Design note — why this shape, and what it does and does not achieve

**Why a class-and-gate rather than a path.** RFC 0003 defines governance homes
at **project** scope (RFC3-15's constitutional categories) and explicitly puts
the workspace manifest *outside every governed plane* (RFC3-10). There is
therefore **no workspace-scope governance home in Wave A to point at** — and
inventing one would have been this repair pass legislating a governance
category on the owner's behalf, which VIS-4 forbids. What Wave A *does* supply
is (i) the predicate that classifies the registry (RFC3-16(a), fourth
example limb — the same limb that already reaches RFC9-18 and RFC9-26),
(ii) the class of home such an artifact takes (RFC3-15), (iii) the bar on a
personal-state home (RFC3-10/11/21 read with RFC2-1 item 7), and (iv) the
lawful route by which a new home is established (RFC3-15(a)'s recorded
widening, B19's precedent). The clause now names all four and stops.

**What the reader can now do that they could not before.** Evaluate every
condition RFC9-8(a) states with only RFC 0001–RFC 0009 in hand. The bar on
portfolio re-lay is unchanged in *effect* — it was fail-closed before and is
fail-closed now — but its *ground* moved from "an unaccepted contract has not
minted a store" to "no governance home exists at this scope yet, and creating
one is an owner act of a class RFC 0003 already defines". The owner accepting
Wave B is no longer accepting a dependency on unreviewed RFC 0010 text.

**Checked against the charter's three requirements.**
1. *Capability 1 / Wave B interpretable and acceptable with zero reliance on
   RFC-0010/0011 text* — **yes.** RFC10-15 survives as one citation inside a
   parenthetical that states, in the clause, that it is not a reliance and
   that the rule holds if RFC 0010 is never accepted. `RFC11-n` appears
   nowhere in the wave (RD-19's sweep; re-run this session, still zero).
2. *The module's `depends_on` drops RFC-0010* — **it never carried it, and
   still does not.** The corpus has **no** staged-frontmatter convention to
   mirror: a sweep for `staged_depends_on` over `candidates/` returns zero
   hits outside RD-19's own repair text, and RFC-0006 carries no staging
   marker in its front matter (its staging language is prose, as is
   RFC-0010's and RFC-0011's). So the honest declaration is the one the
   dependency index already derives: RFC 0009 **cites** RFC 0010 and does not
   **depend on** it — which is exactly what the index's own banner ("a
   citation is not a reliance") means, and is now *true* where before it was
   a mis-typing of a real reliance.
3. *The governance-plane ruling preserved, not reversed* — **yes**, verbatim.

**What this does not do.** It does not decide where the workspace-scope
governance home will be. That remains an owner act, and the clause says so.
It also does not repair the acceptance record's §7 item 9 or its §1 row B —
those are R-REC's (X3), and §9 below states what the measured position now is
so that rewrite is written against the repaired bytes and not the old ones.

---

## 2. X1 — stale numeric ranges and self-counts, removed rather than patched

The register's design: *prefer range-free formulations so the class cannot
recur*; for the seam edge count, *drop the count, do not patch it*.

### 2.1 The three phase-rule ranges (RD-10 F1, blocking; extended to RFC8-32 and RFC9-52)

| | |
|---|---|
| Clauses | **RFC7-38**, **RFC8-32**, **RFC9-52**, plus each package README's phase-boundary paragraph and the RFC-0009 README's "binds the package" note |
| Digest-moving | **yes**, in all six files |

**Old meaning.** Each clause bound "every observable consequence of
RFC7-1…RFC7-37 / RFC8-1…RFC8-31 / RFC9-1…RFC9-51".

**New meaning.** "every observable consequence of **every clause of this
contract other than this one**" — the wording **RFC6-28 already carries**, so
the four surface phase rules are now shape-parallel in fact and not only in
claim.

**Why, and the honest split between the three.**
- **RFC7-38 is a genuine semantic widening.** Round-2026-08d appended RFC7-39
  and RFC7-40 and did not move the range with them, so the two most plainly
  user-observable clauses in Polaris — the fixed entry path a human reader is
  sent to, and a per-repository rendered finding with a Proposal affordance —
  had no obligation to map to any OpenSpec requirement and no matrix row in
  which their absence would show. They are now inside it.
- **RFC8-32 and RFC9-52 name the same set they named before.** RFC8's declared
  range ends at 32 with no gaps, RFC9's at 52; "RFC8-1…RFC8-31" and
  "RFC9-1…RFC9-51" were each exactly *every clause but the phase rule*. **This
  is a reviewable "no change to today's extension" claim, not an editorial
  one**, and it is only true of *today's* clause set: going forward the new
  wording also reaches any clause appended later, which the old wording did
  not. That forward difference is the entire point of the repair, and it is a
  semantic delta the Wave B act ratifies.

Each clause also now carries one sentence saying why the range is gone, so a
later editor does not helpfully restore it.

### 2.2 The RFC-0007 seam edge count and enumeration (RD-10 F12 + RD-19 M5)

| | |
|---|---|
| Artifact | `rfcs/RFC-0007/README.md`, "Where the seam falls" |
| Digest-moving | **yes** |

**Old meaning.** "**Twelve citation edges cross it, all resolvable by the
lookup rule above:**" followed by a hand-maintained enumeration.

**New meaning.** The count and the enumeration are **deleted**. The paragraph
now states that citation edges cross in both directions, that every one
resolves by the deterministic lookup rule, and that neither the edges nor
their count is listed because both are derived measurements.

**Why.** RD-10 measured 31 edges mechanically; RD-19 measured ≈29 and found
two cross-seam citations (RFC7-28, RFC7-31) missing from the list. The figure
had already been corrected once inside a digest set (record §1a, SD-1/SD-10).
Patching it to a new number reproduces the defect; the lookup rule discharges
the navigation need without either. This is the same move the README already
makes for module sizes, and the paragraph now says so.

### 2.3 The RFC-0009 README self-counts (RD-19 m4, m5)

| | |
|---|---|
| Artifact | `rfcs/RFC-0009/README.md` |
| Digest-moving | **yes** — the register §6 records RD-19's own batching note as wrong on this point; both sit inside the Wave B manifest |

- **m4.** "**The eleven cases** keep their stable package numbering…" enumerated
  twelve items (3a is a separately-headed case). The count is **dropped**; the
  routing sentence carries the information, and one added clause states the
  eleven-integers/twelve-items fact once, where it cannot go stale by drifting
  from a number.
- **m5.** "**RFC3-16(a) gates four artifacts across two modules**" undercounted
  (RFC9-45 gates the judgment *and*, separately, the release policy) and
  counted a promotion *act* as an artifact. The count is **dropped**; the
  sentence now enumerates the gated artifacts across the package, including
  RFC9-8(a)'s portfolio registry and RFC9-52's N/A judgment, both of which the
  old sentence predated.

---

## 3. X2 — the ungated reviewed N/A judgment (RD-10 F7), three clauses

| | |
|---|---|
| Clauses | **RFC7-38, RFC8-32, RFC9-52** |
| Digest-moving | **yes**, in all three files |

**Old meaning.** Each phase rule admitted an "explicit, reviewed N/A judgment"
as an alternative to an OpenSpec requirement and said nothing about where it
lives, who may make it, or under what provenance it is honored — while every
comparable authorization-bearing artifact on these three surfaces (RFC7-21,
RFC7-25, RFC7-31, RFC8-12, RFC8-16, RFC9-18, RFC9-26, RFC9-35, RFC9-45)
invokes RFC3-16(a).

**New meaning — the exact standardized sentence, taken byte-for-byte from the
R-A batch so the two can be compared by string search:**

> **The reviewed N/A judgment's home and gate.** A reviewed N/A judgment is a
> recorded owner judgment homed in `decisions/` (RFC3-15), and it is honored
> only where its owner-act provenance is verifiable under RFC3-16(a). Where
> that provenance does not verify, the judgment maps nothing: the consequence
> remains unmapped and renders Unknown, never covered (RFC3-16(a)'s effect
> rule; VIS-2).

**Sweep, with denominator [Observed, this session].** Whitespace-normalized
string search for that sentence over **all 39 active RFC module files**:
**9 exact matches, in exactly the nine phase clauses — RFC1-33, RFC2-26,
RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32, RFC9-52 — one per
contract, zero elsewhere, and zero near-misses** (files carrying the heading
with different wording: none). The R-A and R-B halves of X2 are identical.

**Placed identically, too.** In each of the three Wave B clauses the sentence
sits between "…recording why that consequence needs no requirement." and "The
surface-specification phase must produce…", which is where RFC6-28 already
carries it.

**One Wave-B-only addition, flagged for mirroring.** RD-10 F7's secondary
limb — the binding sentence is over every observable *consequence* while the
checkable deliverable is a *per-clause* matrix, so a clause with five
consequences and one mapped requirement produces a complete-looking matrix —
is repaired in the three Wave B clauses with:

> **Rows are per observable consequence, not per clause.** A clause with five
> observable consequences and one mapped requirement is not covered; the matrix
> discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of the
> matrix.

RD-9 f11 did not raise this limb, so the six Wave A phase clauses do not carry
it. **That is a divergence between shape-parallel clauses and should be closed
by mirroring the paragraph into Wave A, not by removing it here** — the defect
is real in all nine. Routed as a handoff (§9).

---

## 4. RFC 0007 — Polaris

### 4.1 RD-10 F2 — two front doors, and the fixed one unattached to the narrative model

| | |
|---|---|
| Clause | **RFC7-39** | 
| Digest-moving | **yes** |

**Old meaning.** RFC7-39 made `.syzygy/intent/OVERVIEW.md` "the one path a
human reader is sent to first", "rendered as governed presentation under this
contract's narrative rules" — and no clause said whether that file *is* the
RFC7-6 primary narrative that RFC7-30's acceptance test enters, nor which
obligations the blanket phrase carried.

**New meaning.** Two added paragraphs state (a) that the fixed entry **is** the
project's primary narrative and RFC7-30 enters it, with the path treated as a
**publication location and never an identity** (so RFC7-6's "at most one" and
RFC7-5's opacity rule both stand, and additional named narratives are published
elsewhere); and (b) an enumeration in RFC7-36's style of the obligations that
follow the entry — **RFC7-2, RFC7-5 membership, RFC7-7, RFC7-11 and RFC7-11(a),
RFC7-33/34** including the `non-citable` / `presentation-artifact` attribute on
every exported, embedded or plain-text rendering — with RFC7-3 restated as
binding in full.

**Why this horn.** Both horns of the review's dilemma were defective; the
authors, facing the identical question one clause earlier (RFC7-36), refused
the blanket and enumerated. The identity/path distinction is what makes the
"same narrative" answer compatible with RFC7-5, and RFC7-33 itself calls the
omission of the attribute "unrecoverable at the consumer" — which is why the
enumeration names it explicitly rather than resting on the catch-all.

### 4.2 RD-10 F9 — RFC7-40's answer domain, Unknown reason, and landing document

| | |
|---|---|
| Clause | **RFC7-40** |
| Digest-moving | **yes** |

**Old meaning.** Three defects in one clause: a domain stated closed at
**`yes / no / Unknown`** and then opened to a fourth value eleven lines later;
an Unknown with no RFC2-24 reason; and a "configured landing document" input
with no lawful configuration site.

**New meaning, in three limbs.**
1. **The domain is closed at four values** — `yes` / `no` / `not-applicable` /
   `Unknown` — stated once and carried verbatim (RFC6-14), closed for the
   reason RFC6-22/23 make a spelling disagreement release-blocking. Added
   guard: `not-applicable` here is a value of **this finding's own domain** and
   **not** RFC6-5's navigation outcome of the same spelling, so RFC6-6's rule
   that outcomes are never Unknown reasons is untouched.
2. **`Unknown` carries its RFC2-24 reason verbatim**, naming the reason the
   failure actually names, and the unconsented-repository branch is **cited,
   not restated**: reason **#6 `unconsented-source-or-provider`** via **RFC3-6**
   — which the review noted was already answered upstream and only needed
   citing.
3. **"Configured landing document" is dropped** (the disposition's chosen
   route). The front door read is the repository's root README; the clause
   states why a configurable input would be unlawful (RFC3-5's closed field
   set; RFC2-2 makes an unclassified input fatal to a deterministic answer)
   and that widening it would take an RFC3-5 amendment in the same logical
   change, which this clause makes none of. **This deliberately avoids the
   cross-wave RFC3-5 arm**, per the disposition.

### 4.3 RD-10 F13 — the package's indices, scope maps and lists predate RFC7-39/40

| | |
|---|---|
| Artifacts | `rendering-and-surface.md` front matter, §0 scope map, `Serves`, §4, §5; `README.md` front matter, §4 |
| Digest-moving | **yes** |

- §0 scope map now names §3.14 and both clauses, and records that the phase
  rule precedes them in file order deliberately **and reaches them**.
- `governs` gains `fixed-human-entry-point`, `front-door-discoverability`;
  `tags` gain `entry-point`, `discoverability` (module 2 and package README).
- **`Serves` gains VIS-5**, on which RFC7-40 expressly rests, with the reason.
- Module 2 §5 and README §5 now record the reliances both clauses carry —
  RFC1-10, RFC1-27, RFC2-2, RFC2-24 (#6), RFC3-5, RFC3-6, RFC6-5/6, RFC6-14,
  RFC6-22/23 — and the RFC3-16(a) gate count in README §5 moves from **three
  clauses to four** with RFC7-38's N/A judgment named.
- **One new violation case, 16**, covering both clauses (missing `non-citable`
  attribute on the fetched entry; a second front door the test does not enter;
  a fifth finding value, a reasonless Unknown, or `no` for a repository with no
  governance root). Package numbering is stable and the distribution sentences
  in all three files were updated together.

**Deliberately not done:** F13's optional suggestion to give RFC 0007 an
RFC9-47(a)-style same-logical-change invariant. It would take a new clause
identity, and the range-free RFC7-38 wording (§2.1) removes the failure mode
F1 and F13 shared — an appended clause now falls inside the coverage
obligation automatically. Recorded here so the omission is a decision and not
an oversight.

### 4.4 RD-10 F10 — the comprehension test cannot detect an unreadable vocabulary

| | |
|---|---|
| Clause | **RFC7-30** |
| Digest-moving | **yes** |

**Old meaning.** Six prompts, none of which is failed by a reader who cannot
distinguish `asserted-by-worker` from `gate-backed` — while minimal default
density puts four technical carriers on every capability (RFC7-16).

**New meaning.** A seventh prompt: for **one rendered fact of the reader's
choosing, how strongly the surface claims to know it and what would make that
claim stronger**, with a sentence naming what the two last prompts catch that
the other does not. The review's own recommendation between its two options
("the first is cheaper and is the one the test is shaped for").

### 4.5 RD-10 F8 + RD-19 M3 — the dangling-anchor loop, closed at both ends

| | |
|---|---|
| Clauses / artifacts | **RFC7-11**; `narrative-contract.md` §5; `README.md` §5 defect 1 and §5 integration |
| Digest-moving | **yes** |

**Old meaning.** RFC7-11 named an RFC6-5 *outcome* and no RFC2-24 reason, so
the Unknown it minted had nothing to carry under RFC6-14. And README §5 defect
1 was titled "**Live**" on a premise the bound RFC 0002 bytes falsify — RFC2-24
reason **#11 `reference-unresolvable`** exists with resolution route "repair
the reference", and decision **A5** closed the list at twelve — while inviting
the owner to reconsider something A5 had foreclosed, across the act boundary.

**New meaning.** RFC7-11 now degrades the claim to Unknown **with reason #11
carried verbatim** and its resolution route visible, and states that the RFC6-5
outcome is a *navigation* fact and never the claim's reason (RFC6-6). README §5
defect 1 is relabelled "**Discharged, owner decision A5**", the false premise
removed, and "no RFC 0002 change is outstanding" stated. Module 1 §5 and README
§5 record #11's provenance and A5's ruling.

---

## 5. RFC 0008 — Trajectory

### 5.1 RD-10 F4 + RD-15 f7 — `reconciled`, orthogonality and the status leak (one design)

| | |
|---|---|
| Clause | **RFC8-12** (with an RFC8-13 row untouched, and the "orthogonal" wording corrected wherever it appeared) |
| Digest-moving | **yes** — `state-vocabulary-and-cost.md`, and the echoing sentences in `RFC-0008/README.md` §5, `state-vocabulary-and-cost.md` §0 and `RFC-0009/visual-grammar-and-lenses.md` RFC9-32 |

**Old meaning.** "**The normalized state is one of two orthogonal fields**",
with the argument for carrying both being that normalized `merged` is
compatible with three chain states; and "the normalized state is not a Claim…
carries no RFC2-25 tier and no membership in the observation record", applied
unqualified to all thirteen values.

**Both were false of one value.** `reconciled` is *defined as* `reconciled@E`
(RFC8-13), so the fields are not orthogonal there — one is a total function of
the other, and an implementer reasoning from RFC8-28's stated argument would
drop the chain state exactly where the verdict lives. And `reconciled` derives
from a **reconciliation verdict claim** (RFC2-18: "a positive status claim
requiring gate-backed Observed evidence"), so carrying it under the unqualified
non-Claim rule strips the RFC2-25 tier that is the sole licence for a positive
claim.

**New meaning, one design in three parts.**
1. **"Orthogonal" is withdrawn as an assertion.** The clause now says the two
   are **separate fields, never substituted for one another**, states that
   normalized `reconciled` is a **projection** of the chain field, and states
   that both fields are carried on every element **regardless of value** — so
   the carriage rule no longer rests on an argument that is false for one
   value. The same correction was made in the three places that echoed the
   word (RFC-0008 README §5, module 2 §0, RFC9-32), each with the reason.
2. **A field-qualification rule for machine answers.** `merged` and
   `reconciled` collide in spelling across the two vocabularies while RFC6-14
   requires both be carried verbatim; every machine answer, filter, count and
   export now **names the field each value belongs to**, and a bare value is
   not a conforming answer. Anchored on RFC1-25(b)'s twelve-pair invariant as
   the corpus's existing treatment of the same hazard.
3. **An explicit carve-out for `reconciled`.** It renders **only together with
   the verdict claim's RFC2-25 tier and its evaluation identity, read from the
   chain field**, and never on its own; where either is unavailable the field
   does not render `reconciled` (`merged` plus the chain state is the honest
   answer, which is already V0's). It remains a projection: it mints no
   two-level claim identity and no observation-record membership of its own.

*(Of RD-15 f7's two offered routes — drop `reconciled` from the vocabulary, or
carve it out — the carve-out was taken. Dropping a value from a vocabulary
owner decision **A8** closed at thirteen would reverse an owner ruling, which
a repair pass may not do.)*

### 5.2 RD-15 f5 — RFC8-28 now closes the chain vocabulary it is cited for closing

| | |
|---|---|
| Clause | **RFC8-28** |
| Digest-moving | **yes** |

**Old meaning.** RFC8-12 cited RFC8-28 as the chain state's "own closed
vocabulary"; RFC8-28 said only that the six states are "first-class Trajectory
states, queryable and filterable", and a sweep of `closed` in that module hit
`fail-closed`, "warrant classes are closed", "closed navigation-outcome set",
`closed` work item and "closure fallacy" — never the chain list. RFC2-18 states
the vocabulary as a transition expression and never uses the word.

**New meaning.** RFC8-28 now carries the closure in RFC8-12's own form —
"**Six values, closed.** … no implementation may mint, spell, or force-fit one
outside it" — with RFC8-12's reason (RFC6-14 verbatim carriage; RFC6-22/23
release-blocking disagreement) and a sentence on why this facet in particular
needed it: it carries the reconciliation truth and was the least protected of
the load-bearing facets.

### 5.3 RD-10 F3 — the colour limb, and RFC 0008's missing non-visual floor

| | |
|---|---|
| Clauses | **RFC8-28** (colour limb) and **RFC8-31** (parity limbs) |
| Digest-moving | **yes** |

**Old meaning.** RFC8-28 forbade merging `unsatisfied` and
`contradiction-raised` "into one count or one badge" — satisfied, as written,
by a distinction only colour carries; its map counterpart RFC9-32 closes the
channel explicitly ("never share a mark, a mark's color, a count, or a legend
entry"). And a case-insensitive sweep of all four RFC-0008 files for
*keyboard | accessib | screen[- ]reader | colo(u)r | non-visual* returned
**zero hits** — Polaris binds RFC7-33/34, Orrery binds RFC9-48, Trajectory
bound nothing, and no doctrine clause distinguishes surfaces.

**New meaning.**
- **RFC8-28** gains "**Never a colour-only distinction**" in RFC9-32's words,
  with the explicit statement that two differently-coloured badges do not
  discharge the clause on the surface that routes a gap to work and a
  Contradiction to owner adjudication alone.
- **RFC8-31** gains a two-limb non-visual parity floor: every normalized state,
  chain state, blocked-cause set, Unknown-provenance state and absence value
  carried **textually** on every rendering and export (RFC6-14's carriage rule
  made a rendering obligation); and the board/queue/drawer handoff and every
  traversal **operable by keyboard**, with recoverability and operability
  stated as separate obligations that both bind (RFC7-34's reasoning).
- `governs` gains `non-visual-parity` and `tags` gain `non-visual`,
  `accessibility` (module 3 and package README); module 3 §5 gains an
  **RFC 0007** entry and its front matter now declares `RFC-0007`, which the
  package README already declared.

**Departure from the review's repair note, stated.** RD-10 F3 proposed "a
non-visual parity clause to RFC 0008 (next free integer, RFC8-33)". **A new
integer is not available**: `verify_final_prespec.py` closes RFC8 at 32, and
the package README bars lettered sub-clauses ("Lettered limbs … are *parts of
that clause*"). Minting RFC8-33 would have failed the corpus's own verifier,
and changing the verifier is R-SCR's file, not this batch's. The obligation is
therefore written as a limb of RFC8-31 — the clause that already owns
cross-surface conformance and endpoint answerability — with a parenthetical in
the text saying exactly that, and noting that RFC8-32's coverage matrix reaches
it through RFC8-31. **If the owner prefers a distinct clause identity, this is
the arm to re-open**, and it takes an `ENDS` change in R-SCR's script plus a
manifest regeneration.

### 5.4 RD-15 f9 — `blocked` under multiple causes

| | |
|---|---|
| Clauses | **RFC8-17**, with **RFC8-13**'s `blocked` row and **RFC8-18**'s blocked-time measure aligned |
| Digest-moving | **yes** |

**Old meaning.** "`blocked` carries **a cause** from the closed taxonomy…
Where the substrate conflates causes and no declared derivation resolves one,
the item renders blocked with cause Unknown." The absence path covered *zero*
resolved causes; nothing covered *two*, so an implementation picks and the
owner clears the wrong blocker.

**New meaning.** `blocked` carries a **cause set** — *every* cause whose
declared derivation resolves — carried on every rendering, filter, count and
machine answer (RFC6-14), never a chosen member; **cause-Unknown is reserved
for the empty set** and is never mixed into a non-empty one. RFC8-13's row
matches, and RFC8-18's "blocked time (split by RFC8-17 cause…)" now says that
an interval with more than one resolving cause discloses that rather than being
attributed to one member. The taxonomy itself is unchanged and still closed.

### 5.5 RD-19 m3 — RFC8-7's self-contradicting attribution

| | |
|---|---|
| Clause | **RFC8-7** |
| Digest-moving | **yes** |

**Old meaning.** "…**drafted → under review → approved →
queued-for-materialization → materialized** over the RFC1-28 entity, **in
RFC1-31's own state names**" — while RFC1-31 carries no
`queued-for-materialization`, and the clause's next sentence says it is "not a
new kernel lifecycle state".

**New meaning.** "…in RFC1-31's state names, **with
`queued-for-materialization` added as a work-plane fact rather than a kernel
state** — RFC1-31 does not carry that name, and this package reports the
omission rather than diverging from it silently (§5, §8 q2)." The outstanding
foundation defect and its owner question are unchanged and still open.

### 5.6 RD-19 m2 (third item) — RFC 0005 declared with no clause anchor

| | |
|---|---|
| Artifact | `accounting-reconciliation-and-release.md` §5 |
| Digest-moving | **yes** |

**Old meaning.** The module declared `depends_on: RFC-0005` and its §5 line was
"**RFC 0005:** machine-client admission for RFC8-31's endpoint answers" — a
dependency asserted with no clause anchor, in a module containing zero `RFC5-n`
citations (verification rule 8).

**New meaning.** The line names the clause: "**RFC5-5** — machine clients are
admitted only through an explicit, revocable admission, and agent and CLI
clients are machine clients without exception". The declaration is kept because
it is now anchored and true. *(Of the review's two options — anchor it or drop
the declaration — anchoring is the smaller edit and the truer one.)*

---

## 6. RFC 0009 — Orrery

### 6.1 RD-19 M4 — RFC9-43 cited the wrong tuple

| | |
|---|---|
| Clause | **RFC9-43** |
| Digest-moving | **yes** |

**Old meaning.** "**The disclosed composition is the full RFC9-46 equivalence
tuple** — per-label, per-tier, per-Unknown-reason and per-freshness-state counts
**and sibling surface states**… RFC6-17 binds the same enumeration at the
foundation layer; the two are deliberately identical." RFC9-46 is **strictly
wider** than the list that follows: at acceptance it added the RFC9-9(b)
positional-expression state and both RFC9-15(b) part 4 backlog counts. Both
readings were bad — either every aggregate owes two fields no RFC9-47 check
tests, or the clause anchors on the wrong tuple.

**New meaning.** The citation is corrected to the **RFC6-22** equivalence tuple
— the tuple RFC6-17 itself names, in RFC6-17's own words, so "the two are
deliberately identical" is now true as written — and one added paragraph states
that **RFC9-46's surface-local additions are not aggregate-composition items**,
with the reason: they are properties of an *edge* and of the *layout*, not of
an aggregate's membership, and importing them would mint a release-blocking
obligation with no aggregate-level check, which **RFC9-47(a) part 1 forbids**.
They bind where RFC9-46 binds them — scene/table agreement over one declared
scope — and RFC9-47 already gates that.

*(Of the review's two routes, this is the first: "if aggregates carry only the
foundation tuple, change the citation to RFC6-22 and keep 'the two are
deliberately identical'." It was chosen because RFC6-17 is the aggregation
contract RFC9-43 opens by citing, and the two added fields are per-edge and
per-layout quantities that no district aggregate has a membership over.)*

### 6.2 RD-10 F5 — residual-adjacency decidability defeasible by lawful LOD, filters and narrowing

| | |
|---|---|
| Clauses | **RFC9-9(a)** part 2, with the check routed into **RFC9-47** in the same logical change (RFC9-47(a) part 1) |
| Digest-moving | **yes**, in both modules |

**Old meaning.** Part 2 promised the residue is "reader-decidable, not merely
disclaimed" — a reader can decide which of three readings applies "from what is
on the screen". Reading 1's discriminator is protected (RFC9-25 reserves the
district boundary channel); **reading 2's was protected by nothing**: RFC9-42
lets LOD reduce label density freely, RFC9-13's persistent count covers hidden
*entities* and not edges, and RFC9-49 permits narrowing a declared scope. A
lawful zoom-out, filter or narrowing therefore removed the only on-screen
evidence distinguishing reading 2 from reading 3, and part 1's third legend
line ("residual adjacency — carries no meaning") became **false about nearness
that does carry meaning** — the VIS-7 legend-fidelity failure part 2 exists to
prevent, reached without violating any clause.

**New meaning.** A limb binds the channel in **RFC9-44's words**: "no filter
default, LOD step, lens, scene profile, or RFC9-49 narrowing may drop the
`declared-dependency` edge channel or its RFC9-9(b) positional-expression state
wherever nearness is rendered". And the fallback the review offered as an
alternative is bound **as well**, for the case a lawful narrowing suppresses it
anyway: the third legend line for that region **reads "undecidable at this
fidelity"**, never the residual-adjacency line. **RFC9-47's residual-adjacency
gate now runs over filtered, zoomed-out and RFC9-49-narrowed scenes**, with the
sentence that a full-fidelity-only check passes vacuously over the case the
obligation exists for.

### 6.3 RD-10 F6 — `editorial draft` mandatory in disclosure, absent from the palette

| | |
|---|---|
| Clause | **RFC9-24** |
| Digest-moving | **yes** |

**Old meaning.** RFC9-24 reserved treatments for Contradicted, Dismissed by
decision, Proposed/speculative and Unadopted draft. A sweep of all four
RFC-0009 files for `editorial` returned **one hit** (RFC9-43). The state is
minted at RFC7-20 as the third RFC2-25 sibling surface state and is *mandatory*
in RFC9-43's disclosed composition and RFC9-46's tuple — so under RFC9-26's
fail-closed registry it either did not render (contradicting both, a
release-blocking scene/table disagreement) or rendered on an unreserved
treatment (the unlegended meaning VIS-7 forbids).

**New meaning.** **Editorial draft** joins the reserved palette with a
**distinct** reservation and the reason it may not share the unadopted-draft
treatment (an `unadopted-draft` awaits an adoption gate into *authority*; an
`editorial-draft` awaits a human authorship act into a *non-authoritative*
artifact and stays non-citable even after adoption, so a shared treatment tells
the reader the wrong thing about what act is owed). One sentence states why all
three sibling states are reserved here, closing the RFC9-43 / RFC9-26 loop
explicitly.

### 6.4 RD-10 F15 — RFC9-48 misattributed a textual-label requirement

| | |
|---|---|
| Clause | **RFC9-48** |
| Digest-moving | **yes** |

**Old meaning.** "textual epistemic labels for every state (**RFC9-27's
two-carrier rule**)" — RFC9-27 requires "at least two of {surface treatment,
plate/badge, label}", which is satisfied by two non-textual carriers. It is a
colour-independence rule, not a textual-label rule.

**New meaning.** "**textual epistemic labels for every state**, bound by this
clause (distinct from RFC9-27's two-carrier rule, which bars colour alone but
is satisfied by surface treatment plus plate/badge, neither of which is text)"
— the review's second offered form. Nothing is lost in effect: RFC9-48's own
text already bound textual labels, and RFC9-47's gate list attributes the
obligation to RFC9-48, which is now correct.

### 6.5 RD-19 m1 — the q4 stub

| | |
|---|---|
| Artifact | `visual-grammar-and-lenses.md` §8 |
| Digest-moving | **yes** |

The package README routes q4 to module 2 §8, and module 2 §8 states "answered
items keep a stub here so numbers never shift" while carrying q3, q8, q9 only.
A **q4** stub is added, in the section's own form, citing owner decisions
**B12(c)/B17** and RFC9-35's single promotion predicate. The package's stub set
is now complete at ten.

### 6.6 RD-19 m6 — RFC9-15(b) with no (a)

| | |
|---|---|
| Artifacts | `semantic-geography.md` front matter `clauses:` line and closing line |
| Digest-moving | **yes** |

Both asserted "no gaps" without explaining that `RFC9-15(b)` has no
`RFC9-15(a)` anywhere in the package and is defined after `RFC9-16(d)` in file
order. Both now state that the no-gaps claim is over the **integer** range,
that no `(a)` was ever minted and none is retired, that the definition order is
deliberate, and that sub-clause letters are minted as needed and are not a
series. Mirrors the note RFC-0007 module 2 already carries for RFC7-38's file
position. **No clause text changed.**

### 6.7 RD-19 m2 (first two items) + RD-10 F11 — the frontmatter arm

| | |
|---|---|
| Artifacts | `semantic-geography.md`, `interaction-parity-and-release.md` front matter and §Integration |
| Digest-moving | **yes** |

- `semantic-geography.md` declared `[RFC-0001, RFC-0002, RFC-0003, RFC-0004,
  RFC-0006]` while citing **RFC5-20** (RFC9-23's execution-profile boundaries).
  It now declares **RFC-0005**, and §8 names the reliance.
- `interaction-parity-and-release.md` declared `[RFC-0002, RFC-0006, RFC-0007,
  RFC-0008]` while citing **RFC1-25** in RFC9-47's relation-separation gate — a
  release-gate obligation, not an aside. It now declares **RFC-0001**, and
  **RFC-0003** for RFC9-52's `decisions/` home and RFC3-16(a) gate; §6 names
  both.

**Sweep, with denominator [Observed, this session].** Every `RFCn-m` citation in
each of the **11** Wave B modules, tallied by namespace and compared against
that module's declared `depends_on` ∪ `constrains`:

| Module | Cited-but-undeclared, after repair |
|---|---|
| RFC-0007/README.md | none |
| RFC-0007/narrative-contract.md | none |
| RFC-0007/rendering-and-surface.md | none |
| RFC-0008/README.md | `RFC9-32` |
| RFC-0008/accounting-reconciliation-and-release.md | `RFC9-32` |
| RFC-0008/identity-authority-materialization.md | none |
| RFC-0008/state-vocabulary-and-cost.md | `RFC9-32` |
| RFC-0009/README.md | none |
| RFC-0009/interaction-parity-and-release.md | none |
| RFC-0009/semantic-geography.md | `RFC10-15` |
| RFC-0009/visual-grammar-and-lenses.md | none |

**Both remainders are enumerated, not swept under.**
- **`RFC9-32` in three RFC-0008 files** is pre-existing and is a *provides-to*
  citation, not a reliance: RFC 0008 hands RFC 0009 the two-field work-state
  handoff, and the dependency index already derives it as a `cites` edge under
  its own "a citation is not a reliance" banner. Re-typing it as `constrains`
  would promote navigational prose to a semantic restriction the modules do not
  make, so it was left alone. RD-19 did not flag it.
- **`RFC10-15` in `semantic-geography.md`** is the staged successor of §1,
  deliberately retained and disclaimed **in the clause**. `semantic-geography.md`
  §8 now carries a "**No forward reliance**" paragraph saying so, and
  `RFC-0009/README.md` says it at package level without repeating the clause
  token.

**Also swept, 11-module denominator [Observed, this session]:** `RFC11-n` —
**zero hits**, matching RD-19's baseline. `RFC10-n` — **one hit, total, in the
whole wave**: `RFC10-15`, once, in RFC9-8(a)'s staged parenthetical.

**Not repaired, and why.** RD-10 F11's second limb — RFC 0007 and RFC 0009
declare `depends_on` on each other at package and module level, so loading
either pulls the other entire — was recorded by the review as an observation
with no repair. Both edges are genuine reliances (RFC7-31 and RFC9-45 state one
verdict protocol, with the shared release-policy leg *at* RFC9-45), so the
declarations are accurate; the load cost is a context-budget matter, not a
front-matter defect.

---

## 7. What was verified, and how

All read-only, run this session against the working-tree bytes.

- **`python3 scripts/verify_final_prespec.py` → PASS**, "numbered clauses
  defined: **341**". RD-19's baseline for `771965c` was PASS / 341. **No
  regression, and no clause count change** — confirming that nothing was
  minted, renumbered, or lost. Output read, not exit code (verification rule 4).
- **X2 sentence sweep** — 39-file denominator, 9 exact matches, 0 near-misses
  (§3).
- **Cross-contract citation sweep** — 11-file denominator, per-namespace tally
  against declared edges, remainders enumerated (§6.7).
- **Range/self-count sweep** — `RFC7-1…RFC7-37`, `RFC8-1…RFC8-31`,
  `RFC9-1…RFC9-51`, "twelve citation edges", "The eleven cases", "gates four
  artifacts", "configured landing document": **zero hits remaining** across the
  11 modules. "orthogonal" survives in **4 places, all four now saying the
  fields are *not* orthogonal and why** — enumerated rather than claimed absent.
- **Word counts** — computed with Python over both the working tree and a
  `git archive HEAD` copy; never transcribed (§0).

- **`python3 scripts/check_governance.py`** (repo root) — read for *which*
  checks fire, not for a green/red verdict. **HEAD baseline: 24 OK / 16 WARN /
  0 FAIL (40 checks). Working tree: 19 OK / 18 WARN / 11 FAIL (48 checks).**
  The comparison is **not** apples to apples and is not claimed to be: the
  working tree carries eight checks that do not exist at HEAD (CG-1, CG-1g,
  CG-2e, CG-2f, CG-4a, CG-4b, CG-7f, CG-7g — R-SCR's, in flight) and the
  in-progress edits of the other repair batches. Attributable to R-B:
  **CG-7a's Wave B rows** (11 of its 50 findings — every Wave B module's digest
  now differs from the manifest, which is the intended consequence of the
  repairs and is cleared by regeneration), and **one CG-17 finding that this
  batch introduced and then removed** (handoff 8). No other FAIL names a Wave B
  module; the rest name the acceptance record, the routers, the fixtures, the
  overview, the topology bundle and the launch-gate prompt — all outside this
  boundary and all already routed in the disposition register.

Two claims here are measurements this session and go stale on the next edit:
the word table and the two sweeps' remainders. The generated budget report and
the dependency index own those figures, not this file.

---

## 8. Digest-moving summary

**All eleven Wave B modules moved**, so the Wave B manifest and every digest
derived from it are stale until regenerated by
`scripts/build_active_manifest.py` — **which this batch deliberately did not
run** (the lead session owns manifest regeneration). Consequently:

- `wave-manifests/WAVE-B-MANIFEST.txt` and its own sha256 are stale;
- the acceptance record's §1 row B argument is stale;
- **RD-10, RD-15 and RD-19 are retired for Wave B** — their verdicts remain the
  verdicts for `771965c`, and the wave owes a fresh-context exact-package review
  bound to the new argument before it may be offered (register §7).

---

## 9. Handoffs — outside the R-B boundary

| # | Item | Owner |
|---|---|---|
| 1 | **X3 / the record's §7 item 9 and §1 row B.** The measured position has *changed* under this repair and the rewrite must be written against the new bytes: **RFC 0001–0008 place no reliance on RFC-0010/0011; RFC 0009 carries exactly one *citation* — RFC9-8(a)'s staged successor — and, after this repair, **no reliance**. The old draft rewrite ("RFC 0009 carries exactly one such citation … whose consequence while RFC 0010 is unbound is that no portfolio re-lay is lawful") is now only half true: the bar on re-lay stands, but it stands on RFC3-15/RFC3-16(a), not on RFC 0010. Row B's disclosure should say that. | **R-REC** |
| 2 | **Manifest + index + report regeneration.** `build_active_manifest.py` (Wave B rows and the manifest's own digest), `build_dependency_index.py` (front-matter edges changed in 4 modules — the index matched regeneration at HEAD and now drifts), `build_contract_index.py` (already drifting at HEAD, independently of this batch), `build_budget_report.py` (every Wave B word count moved). | **lead / R-SCR** |
| 3 | **`verify_final_prespec.py`'s `JUSTIFIED_OVERSIZE` note for `semantic-geography.md` is now false in two ways.** It says "at 6,996 words … before round-2026-08d" (the file is now 7,777) and attributes the overage to "relocating the portfolio layout registry to the **RFC10-15** workspace governance store, with its staged reference" — which is exactly the reliance §1 removed. The justification needs rewriting to name the RFC-0003-grounded placement and the round-2026-08e repairs. **The module remains over the ceiling and remains justified; the string is stale, not the exemption.** | **R-SCR** |
| 4 | **X2's per-consequence paragraph is Wave-B-only.** §3's last block should be mirrored into RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27 and RFC6-28 so the nine shape-parallel phase clauses stay identical. | **R-A** |
| 5 | **RD-10 F14** (topology bundle omits the RFC7-39 entry path; OVERVIEW's "four terminal answers" is a different quadruple from RFC8-28's) is `repair-record(R-REC + R-OVW)` and was not touched. RFC7-39's repaired text makes the topology silence more visible, not less. | **R-REC / R-OVW** |
| 6 | **A possible new clause identity for RFC 0008's non-visual parity** (§5.3). If the owner wants it as a clause rather than an RFC8-31 limb, it needs `ENDS` in `verify_final_prespec.py` to open RFC8 past 32 **and** the package README's no-lettered-sub-clauses rule revisited. | **owner / R-SCR** |
| 7 | **RFC 0011's own routing.** RFC9-52's range-free wording changes nothing for RFC 0010/0011, which cite RFC9-52 by identity, not by range. Recorded so the C/D batches do not re-derive it. | *(informational)* |
| 8 | **CG-17 fires on `RFC9-10(c)` and `RFC9-19(b)`** — "declared in a contract, absent from the matrix". Both tokens are **pre-existing** in `semantic-geography.md`'s closing lettered-limb note and were not added by this batch; the working tree's widened CG-17 extractor is what now sees them. The repair is two matrix rows (or an extractor exclusion for lettered *limbs*, which the note itself says are not sub-clauses), in `SURFACE-CLAUSE-ROUTING-MATRIX.md` — outside this boundary. *(Caught and self-corrected during this batch: an earlier draft of the RD-19 m6 note wrote the literal token `RFC9-15(a)` in order to say it does not exist, and CG-17 duly reported it as declared. The note now says "no lettered sibling before it" and names no phantom identity — the generator-quoting-prose failure mode, in miniature.)* | **R-REC / R-SCR** |

---

## 10. Open concerns

1. **Wave B grew 11.2%.** `semantic-geography.md` is 7,777 words against a
   7,000 ceiling it already exceeded (7,079) and is justified by path. Two
   compression passes were made on the RFC9-8(a) redraft and the RFC9-9(a)
   limb; further compression would take semantic delta to text this round has
   not reviewed. **[Inferred]** A reviewer may reasonably ask whether the
   module should now split; that is a bigger act than a repair batch, and the
   round-2026-08d wave design does not provide for it.
2. **RD-19 M4's decision was a judgment call, not a derivation.** The register
   left the choice open and the two readings have different consequences for
   implementers. §6.1 states which was taken and why; if the owner reads
   RFC9-46 as genuinely widening aggregate composition, the other arm is the
   repair and RFC9-47 needs a new aggregate-level check with it.
3. **RFC7-39's "the entry *is* the primary narrative" is a ruling this pass
   made.** RD-10 F2 required *a* statement and both horns were defective; the
   chosen horn is the one that keeps RFC7-6, RFC7-5 and RFC7-30 mutually
   consistent, but it is a substantive answer and the owner may prefer the
   other. It does **not** answer §8 q2 (primary-narrative cardinality), which
   stays open.
4. **RFC8-17's cause-set change reaches an open owner question.** §8 q3
   (blocked-time cause split) is open and now has a slightly different subject
   — an interval may carry several causes. The question text was not edited;
   flagged so the ruling is made against the repaired clause.
5. **Nothing in this batch was reviewed.** Every claim above is this session's
   own; the fresh-context Wave B review owed under register §7 is the check
   that matters, and this file is one of its inputs, never a substitute for it.

---

*End of the Wave B (R-B) semantic delta. Eleven of eleven modules edited; all
edits digest-moving; nothing accepted, nothing installed, no act performed.*

## 11. Addendum, 2026-08-10 — the RD-27 repair batch (main session)

The fresh Wave B dimension review (RD-27, frozen commit `5bb8a36`,
`VERDICT: REVISE`; raw at `reviews/RD-27-wave-b-RAW.md`, dispositions in
`reviews/DISPOSITION-REGISTER.md`) confirmed the forward-dependency posture
("Wave B is independently acceptable given Wave A") and delivered one
BLOCKING finding against the offering apparatus, five MAJOR and four MINOR.
Four repairs touch Wave B module bytes:

1. **The `challenge-pending` disclosure restored to both restated tuples**
   (RD27-01). RFC9-43's aggregate-composition enumeration and RFC9-46's
   cross-surface equivalence tuple each now carry the `challenge-pending`
   disclosure (RFC2-13) that RFC6-17/RFC6-22 — the clauses both claim
   identity with — require. Before this repair a conforming implementation
   could omit it on both surfaces and pass every RFC9-47 check while
   RFC6-23 makes the silence release-blocking.
2. **The conformance rule given a clause home** (RD27-07). The
   consume-both-fields-and-render-every-value rule moved from RFC 0008's
   README §5 into **RFC8-12** (the README now restates and points); the two
   modules citing "`README.md` §5" as its single home now cite RFC8-12.
3. **RFC 0009 README's package-name sentence corrected** (RD27-08): "no
   clause of RFC 0011 is cited anywhere in RFC 0009" — true by the recorded
   sweep — replacing the false "RFC 0011 is cited nowhere".
4. **Three bare cross-module `§` references named** (RD27-09): RFC8-6's
   §3.13 and RFC8-13's §3.14 now name
   `accounting-reconciliation-and-release.md`; RFC8-12's §6 now names the
   README's Alternatives-considered section.

**Modules touched (7 of 11):** RFC-0008/README.md,
RFC-0008/identity-authority-materialization.md,
RFC-0008/state-vocabulary-and-cost.md,
RFC-0008/accounting-reconciliation-and-release.md, RFC-0009/README.md,
plus RFC-0009/visual-grammar-and-lenses.md and
RFC-0009/interaction-parity-and-release.md — seven files. Digest-moving in
all seven; the manifest regenerates by `build_active_manifest.py` and §1
row B is rebound by script in the same change (`c0fd0e27…`;
`2041ad05…` and the round-08d `daa6a5dd…` are stale and satisfy nothing).

**Repairs outside the manifest, same batch:** the matrix's RFC7-40 row
restated to the four-value closed domain and its RFC9-8(a) row to the
typed governance store (RD27-04/05); the router's Polaris omission note
corrected and the Orrery route extended with RFC 0008's vocabulary modules,
router regenerated (RD27-06); the acceptance record row B disclosure
(RD27-03) and §7 item 15 disclosing RFC7-39's entry-identity ruling
(RD27-02(a)); `HUMAN-ENTRY-DECISION.md` corrected to RFC7-40's four-value
domain and extended with the entry-identity question (RD27-02(a)/(b));
packet 6 banner-marked stale and P-22's register row re-grounded
(RD27-02(c)); `05-CONTRACT-INDEX.yaml` regenerated (RD27-10).
RD-32, the exact-package review, binds the post-repair bytes.
