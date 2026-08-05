# RFC-0007 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
the **`../rfcs/RFC-0007/` package**: `README.md` (index, scope, doctrine
grounding, package integration, alternatives, deferrals, question index),
`narrative-contract.md` (module 1, RFC7-1..RFC7-25), `rendering-and-surface.md`
(module 2, RFC7-26..RFC7-38). Full review corpus:
`_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0007-polaris-intent-surface.md`.

Every entry is keyed by the clause whose active text points here; find that
clause with the README's lookup rule (`n ≤ 25` → module 1, `n ≥ 26` → module 2).
Section numbers below are the **rev9 source's** — its §0/§1/§2/§5/§6/§7/§8 are
now carried by the package README. Extracted `*(History: …)*` parentheticals are
copied **verbatim**.

---

## §0 / §1 / §2 — reader's summary and motivation

The rev9 §0 "Reader's summary" carried a longer plain-language orientation.
Its content survives in the compacted §0 map; the sentences dropped as
duplicative of clause text were:

> - Every altitude of the narrative must be a **true coarser read** — a reader
>   who stops early has a simpler model, never a false one. Status display is
>   minimal by default but always carries label + tier + freshness; no
>   composite "maturity score" exists anywhere.
> - The acceptance test is a **cold-open comprehension walkthrough**: a fresh
>   reader must be able to say why the project exists, what it refuses to be,
>   where exactness lives, and **one thing the project doesn't know about
>   itself** — a surface passable only by confident green is fiction.
> - Everything visual is machine-readable and keyboard-reachable; a
>   distinction only pixels carry doesn't survive an endpoint response.

(These are RFC7-13, RFC7-16, RFC7-30, and RFC7-33/34 respectively, and remain
binding there.)

§2's sourcing of the "dangerous artifact" framing, dropped from the active
file because the charter bars `_bootstrap/` citations in active normative
text:

> [Observed: `05-POLARIS-BRIEF.md` §4.3; research, non-authoritative]

---

## RFC7-5 — presentation-profile requirement

Rationale removed from the active clause (the rules themselves — profile
required, Polaris drafts a default for owner sign-off, `unadopted-draft` until
signed, permanent decline permitted, no acting-as-if — all remain binding):

> Without the profile Polaris has no thesis, no reading order, and no
> progressive disclosure, and degenerates into a **disconnected specification
> browser**, which the SDR §2 charter names as a form that does not satisfy
> Polaris; RFC7-30's acceptance test, which enters at the primary narrative,
> would also have no entry point.
>
> **The requirement does not violate RFC1-7's "never presumed present", because
> nothing is presumed.** … That is the RFC2-24 reason #1 resolution route
> applied exactly as written — "first-pass drafting for owner sign-off" — and
> it keeps profile presence an **act** rather than an assumption: until the
> owner signs, the profile is declared-but-unadopted and every narrative
> element above it renders unadopted with it. A project may still decline the
> profile permanently; Polaris then renders the reduced form and says so,
> rather than pretending. What is barred is the third path — Polaris behaving
> *as if* a profile were present because one is required. [Inferred — the
> bootstrap route is the owner's decision; its grounding in reason #1 is this
> RFC's, and is what reconciles the requirement with RFC1-7 rather than
> overriding it.]

Owner decision **A4** (see §8 q5 below) is the ruling this clause implements.

## RFC7-6 — thin, never absent

Rationale removed (the rule — thin or drafted-unadopted, never absent —
remains binding):

> …and it is the narrative's *presence* that keeps RFC7-31's protection of
> honest thinness meaningful and the comprehension test runnable on v1.md's
> proving ground…

## RFC7-9 — bounding and the admissibility floor

Removed reasoning (the three binding properties (a)/(b)/(c) remain in full):

> …it fails (a) as well as (c), which is the point of defining covering as
> attribution rather than derivability.
>
> A challenger facing an unattributable block can name the claim but not the
> support they are contesting, so the challenge is unanswerable without
> re-deriving the author's intent. That each anchor resolves individually is a
> different property and does not supply per-claim attribution.

## RFC7-10 — target-state component

Removed analogy (the recording obligation and its enumeration remain binding;
the pattern citation survives in the active §5):

> This imitates a pattern the kernel already applies everywhere else: RFC2-11
> binds a report artifact to the revision it names and renders it stale
> otherwise, and RFC2-18 pins the exact intent revision so post-merge drift
> surfaces as a *new gap* rather than a retroactive failure. Recording the
> target state creates no new authority and no new epistemic state; what it
> enables is RFC7-11(a).

## RFC7-11(a) — the drift door

Removed reasoning (the rendering obligation, the marker, the review mark, and
the "new evaluation identity alone is not drift" rule all remain binding):

> [Inferred] Drift is the third door to a second source of doctrine. RFC7-3
> closes citation and RFC7-20/21 close generation; a faithful,
> correctly-derived paragraph whose cited rule moved underneath it reaches §2's
> named dangerous artifact through **time** instead. A reader is permitted to
> stop at an early altitude with a true, coarser model (RFC7-13); that
> permission is only safe if the coarse read cannot be quietly wrong.

## RFC7-14 — the verbatim leaf under a proposed reading

Removed rationale (adjacency, distinctness, non-substitution, non-interleaving
and non-anchorability all remain binding):

> Rationale: the leaf is the one place Polaris tells a reader that the text in
> front of them *is* operative (RFC7-12). Rendering proposed requirement text
> in that position would manufacture the most quotable unadopted text in the
> system; rendering adopted text alone would make the proposed reading
> silently incomplete at its most exact altitude. Adjacency answers both.
> [Authored position, not an owner ruling — surfaced at §8 q6.]

The authored position was subsequently confirmed by owner decision **B5**
(§8 q6 below). The active clause now cites B5 rather than the open-question
marker.

## RFC7-16 — tier at rest, and composite maturity

Removed reasoning (the minimal-density fact set, including tier, remains
binding):

> …RFC6-21 already forbids the *fact set* shrinking at minimal density, but it
> says nothing about which facts the minimal *depth* must show, and Polaris is
> the surface where the omission bites hardest. … Label without tier at rest
> is that sentence.
>
> architecture.md refuses to collapse maturity's axes into one status and
> reserves any composite maturity rendering to "the graph/status RFC" — **no
> contract in this foundational set discharges that reservation**: neither
> RFC 0001 nor RFC 0002 defines composite maturity, and this contract names no
> successor. It is no longer merely unassigned, however: **RFC 0002 §7 now
> carries it as an explicit deferral**, so the obligation exits this phase
> tracked rather than lost, and its discharge is an amendment to RFC 0002 or a
> named successor.

The rev9 clause repeated "A narrative sentence doing a badge's work is judged
as a badge (RFC1-19)" as its closing line; the compaction keeps the statement
once inside the tier reasoning and once at RFC7-36, where it is load-bearing.

## RFC7-25 — materiality authority

The rev9 clause carried the authored-position marker, superseded by owner
decision **B6**:

> [Authored position — §8 q1 lists all three options, including the originally
> drafted self-declaration.]

Removed reasoning (the asymmetry rule itself remains binding, with B6's
verbatim answer retained in the active clause):

> Rationale: the drafted alternative was a self-assessment by the party with
> the incentive to avoid review, and that party is frequently an agent
> (below). VIS-4 states the general principle that classification is never
> made by the agent performing the change; narrative is non-authoritative and
> so not strictly bound by VIS-4, and this contract finds no reason for the
> principle to invert here.
>
> Without this, a narrative can rot indefinitely — every anchor resolving, no
> edit ever made — without any change becoming "material".

The RFC3-16(a) verdict-provenance argument is a security premise and stays in
the active clause in full.

## RFC7-26 — mode naming

Removed qualifier (the rule that Polaris coins no surface-local synonym
remains binding):

> …even a locally coherent one.

## RFC7-30 — the non-visual run

Removed reasoning (the per-milestone non-visual/keyboard-only run remains
binding):

> Without it an implementation can satisfy RFC7-33/34 on every rendered unit,
> leave every path between units pointer-only, and pass this test every time.

Also removed, as duplicative of RFC7-31's own text:

> The non-visual run's record lives where every other run's record lives
> (RFC7-31: execution records in `records/`, judgments in `decisions/`).

## RFC7-31 — verdict discipline

Verbatim amendment parenthetical extracted from the rev9 clause:

> *(History: aligned at the rev7 rework with RFC9-45's three-way split; the
> release-policy leg is shared and stated there)*

Removed gloss (the `verdict-unlawful` state, its outcome, and the shared
protocol with RFC9-45 all remain binding):

> …(a state of the judgment record, RFC9-45's term for the same protocol)…

## RFC7-34 — reachability

Removed reasoning (both limbs remain binding):

> …of which SDR-27 supplies only the semantic-equivalence half, which
> RFC7-34's first limb already carries.

## RFC7-36 — portfolio narrative

Removed framing (the carry-over lists, the badge rule, and the OQ-010 note all
remain binding):

> **Which §3.2–§3.3 obligations follow it out of `.syzygy/intent/**`.** The
> portfolio narrative sits outside the narrative model's residence rule
> (RFC7-5), so this clause states the carry-over explicitly rather than leaving
> it to inference.
>
> The four constraints above forbid a reader being unable to *tell* portfolio
> narrative from project truth; they do not by themselves forbid the
> assertion. This clause does…

**OQ-010** (portfolio authority — where a genuine cross-project fact or
Project-relationship entity would live) remains an open owner question and is
noted in the active clause.

## RFC7-37 — roll-up disclosure

Removed worked counter-example (the RFC6-17 disclosure obligation and the
"cited, never restated" rule remain binding):

> The narrow reading — labels carried through, no Unknown folded into green —
> is satisfiable by a parent narrative rendering a child's district as
> "Observed ×30" while all thirty are `reduced-fidelity` and twelve are stale,
> which on a composed narrative page reads as a settled claim about the child
> (RFC1-19).

## RFC7-38 — the binding phase rule

Verbatim amendment parenthetical extracted from the rev9 clause:

> *(History: added at the rev8 rework, directive item 7.)*

The clause text itself is retained at unchanged strength in the active
contract; nothing of RFC7-38 was compressed.

---

## §5 — integration defects, as reported at rev9

**Defect 1 — RFC 0002 (RFC2-25 sibling surface states). Discharged at
acceptance, owner decision B10.** Rev9 text:

> **~~RFC 0002 (RFC2-25 sibling surface states).~~ DISCHARGED at acceptance —
> owner decision B10.** RFC2-25's deliberately-outside list now names
> **three** sibling surface states: `dismissed-by-decision`,
> `unadopted-draft` and **`editorial-draft`**, minted on this RFC's reported
> distinction — an unadopted draft awaits an adoption gate into *authority*;
> an editorial draft awaits a human authorship act into a
> *non-authoritative* artifact and stays non-citable even after adoption.
> RFC7-20's distinct rendering is now backed by a named state rather than
> assuming one. **§8 q3 is answered and marked as such.** Downstream
> enumerations in RFC 0006 (RFC6-14, RFC6-17 equivalence tuple) are amended
> from two to three.

**Defect 3 — RFC 0001 (RFC1-7 vs RFC1-22, personal view state). Resolved;
retained for the trail.** Rev9 text:

> As reported: RFC1-7 listed "personal view state" as presentation-profile
> vocabulary, while RFC1-22 places personal presentation state **outside every
> plane** and RFC3-21 bars it from being a snapshot input, so reifying it as
> graph entities sat awkwardly against both; this RFC does not (RFC7-5). RFC1-7
> has since **qualified** the phrase rather than dropping it — the stronger of
> the two closures, since it settles the reading instead of leaving the
> vocabulary silent — and now reads that "personal view state is deliberately
> **not** reified even here — it stays outside every state plane and is never a
> snapshot input, RFC1-22" [Observed — RFC1-7 as of 2026-08-01]. RFC7-5 needs
> no change. **No RFC 0001 change is outstanding on this item.**

**Defect 2** remains live and is carried in the active §5, including its
post-draft update note:

> *[Update, post-draft: RFC 0002 added it as reason #11, citing this finding
> among its four drivers; the owner may still strike it at acceptance
> (RFC 0002 §8 q1(a)).]*

---

## §6 — Alternatives considered (moved wholesale)

Rev9 §6, verbatim:

- **The structure/prose governance split** (research FRC-1 Option C:
  structure gated as governance, prose free). Rejected by the owner — SDR-13
  rules the whole narrative one governed presentation artifact, with SDR-14's
  materiality scope doing the work the split aimed at: one artifact class
  (RFC7-7), review triggered by materiality (RFC7-25), not by which half was
  touched.
- **Per-sentence citation badges.** Rejected by SDR-16: the obligation binds
  claims, the mechanism binds blocks; sentence badges tax readability without
  adding challengeability block-level anchors lack (RFC7-9).
- **Narrative edits and editorial drafts as kernel Proposals.** Rejected: a
  narrative change is not a delta to desired state — modeling it as RFC1-27's
  Proposal would put presentation churn in the proposed plane and imply an
  adoption gate into authority that RFC7-4 forbids. Consequence recorded:
  RFC1-27's kind list needs no presentation kind.
- **Generated prose banned outright** (research FRC-2 Option A). Rejected by
  SDR-15: the proving ground is mostly undeclared [Observed: v1.md] and
  first-pass drafting is V0 work; the draft state plus non-citability is the
  floor that makes permission safe. The backlog-noise cost is mitigated by
  RFC7-22 — the queue lives in Trajectory, and rejected drafts leave the
  surface entirely.
- **A portfolio meta-project** for the owner's cross-project story. Not
  taken: SDR-29 gives the portfolio narrative a cheaper lawful home (owner
  workspace, VIS-6, exception (a)) at zero doctrine cost; a meta-project
  remains constructible later under RFC3-31 with no change here.
- **Polaris-local status vocabulary or rollups.** Rejected: the label + tier
  + reason vocabulary is the kernel's and closed (RFC2-24/25); rollups edge
  into the composite-maturity rendering doctrine reserves; SDR-17's minimal
  default needs neither.

The first and third are cited from the active §6 because they are load-bearing
for interpreting RFC7-25 and RFC1-27 respectively.

---

## §8 — answered acceptance questions (moved with their answers)

### q1 — Materiality authority (RFC7-25). Answered: owner decision B6.

Rev9 question, verbatim:

> **Materiality authority (RFC7-25).** The deterministic floor (reading
> order, section set, anchor targets, manifesto/thesis sections always
> material) is common to all three options and is not in question. What is
> in question is who classifies a **wording-only** edit. Three options:
> - **(a) Owner classifies every candidate.** Strictest; adds owner touches
>   on every recomposition.
> - **(b) Asymmetric declaration — ◀ the drafted position.** The authoring
>   party may declare a wording-only change **material**, never
>   **immaterial**; only the owner or a contest's resolution classifies a
>   change immaterial, and an undeclared edit's classification stays open
>   rather than defaulting to immaterial. Chosen because the author is
>   frequently an agent and VIS-4 states that classification is never made
>   by the agent performing the change. This is a **reviewer suggestion
>   adopted as the drafted position**, not the original draft.
> - **(c) Author self-declares** (the originally drafted rule): wording-only
>   edits are material only if author-declared or contested. Cheapest;
>   leaves the review decision with the party that has the incentive to
>   avoid review.
>
> Confirm (b), or select (a) or (c)?
>
> > **ANSWERED at acceptance — B6.** **Asymmetric.** The authoring party may
> > declare a change **material**, never **immaterial**; only the owner rules
> > something immaterial. Escalation is free and self-service; de-escalation
> > requires the owner.

### q3 — The editorial-draft surface state. Answered: owner decision B10.

> **The editorial-draft surface state (Integration defect 1).** Amend
> RFC2-25's sibling-state list with `editorial-draft`, or direct reuse of
> `unadopted-draft` with a qualifier? Proposed: the distinct state — the two
> await different acts and confer different end states, and folding them
> leaks a governance-artifact connotation onto presentation prose.
>
> > **ANSWERED at acceptance — B10.** `editorial-draft` is **minted** as a
> > third sibling surface state in RFC2-25, on this RFC's own reported
> > distinction. Downstream enumerations in RFC 0006 amended from two to three.

### q5 — Presentation-profile scope (RFC7-5/RFC7-6). Answered: owner decision A4.

> **Presentation-profile scope (RFC7-5/RFC7-6).** *Authored position, not an
> owner ruling — surfaced because it makes a profile RFC1-7 defines as
> "never presumed present" effectively mandatory wherever Polaris renders.*
> Drafted: the presentation profile is **required for any governed project
> Polaris renders**, and on an undeclared or thin project the primary
> narrative may be thin or Syzygy-drafted-unadopted but never absent. It
> follows from the SDR §2 charter (a profile-less Polaris is the
> "disconnected specification browser" the charter excludes) and from
> RFC7-30's test entering at the primary narrative. The alternative the
> owner may rule instead: **Polaris declines to render a governed project
> that does not load the profile.** Confirm the drafted scope?
>
> > **ANSWERED at acceptance — A4.** The profile is **required**, and Polaris
> > **drafts a default for owner sign-off** on first render rather than
> > presuming one — the RFC2-24 reason #1 route. RFC1-7's "never presumed
> > present" holds because nothing is presumed.

### q6 — The verbatim leaf under a proposed-scenario reading (RFC7-14). Answered: owner decision B5.

> **The verbatim leaf under a proposed-scenario reading (RFC7-14).**
> *Authored position, previously unsurfaced.* Drafted: the leaf renders the
> **adopted** requirement/scenario text as operative, with the proposed
> delta **adjacent** and visibly/queryably distinct. The two alternatives
> are proposed text at the leaf (which manufactures the most quotable
> unadopted text in the system) and adopted text alone (which makes the
> proposed reading silently incomplete at its most exact altitude). Confirm
> adjacency?
>
> > **ANSWERED at acceptance — B5.** **Adopted text is the operative leaf; the
> > proposed delta renders adjacent and visually distinct.** Rendering proposed
> > text at the leaf would make the most quotable text in the system unadopted.

### q7 — The V0 disclosure enumeration (RFC7-13/RFC7-17). Answered: owner decision B7.

> **The V0 disclosure enumeration (RFC7-13/RFC7-17).** *Authored V0 choice,
> previously taken silently.* The **obligations** are foundational — each
> altitude a self-sufficient honest read, every narrative reaching a
> verbatim leaf, each band in exactly one of three authority classes.
> Drafted as **V0 defaults, reversible without amending the obligations**:
> the five-altitude ordering (thesis → architecture → catalog → deep dive →
> verbatim leaf) and the three-band deep-dive composition. The alternative:
> freeze the enumeration as foundational, which forecloses RFC7-6's
> audience-specific narratives ordering their altitudes differently. Confirm
> the V0-default framing?
>
> > **ANSWERED at acceptance — B7.** Obligations per altitude and band are
> > binding; the five-altitude / three-band counts are the **V0 default, not a
> > frozen constraint**.

### Still open (retained in the active §8)

- **q2** — Primary-narrative cardinality (RFC7-6).
- **q4** — Rejected-draft retention (RFC7-22).

---

## Rev9 §7 wording dropped as redundant

The active §7 keeps every deferral. Two phrasings were shortened:
"Certificate rendering → post-V1 certificate RFC **(future-tagged)**" and
"Portfolio-profile detail … → portfolio profile per **RFC 0006 §7**" (now
cited as RFC 0006's portfolio-profile deferral, per the charter's rule against
citing other RFCs by section number).
