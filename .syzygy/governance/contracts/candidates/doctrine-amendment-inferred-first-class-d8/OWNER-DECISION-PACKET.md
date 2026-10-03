# Doctrine amendment packet — D8 (proposed): Inferred as a first-class rendered state

**Status: DRAFT — not applied, not adopted; binds nothing.** Doctrine
amendment is an owner act (VIS-4). An agent session drafted this packet on
2026-10-03 for `syzygy-u05.15` (vision pursuit 2026-09-22, move N15,
"packet B"). It edits no doctrine byte, opens no gate, authorizes no
implementation and drafts no contract or specification amendment. A commit,
a merged pull request, a review, a closed bead or silence performs nothing;
only the owner's own words in the owner's own session do.

**Batched with packet A.** The bead asks for this packet to be offered
alongside D7 (held derived computation, register row P-101; its packet is
OWNER-DECISION-PACKET.md in the sibling directory
doctrine-amendment-held-derived-computation-d7, in pull request #296, not
yet on `main` when this was drafted).
The two are independent: each may be adopted, amended or declined without
the other (§8 states how their insertions compose).

**Identifier.** `D8` is provisional: the doctrine amendment log
(`../../../decisions/DOCTRINE-AMENDMENT-LOG.md`) holds D1, D5 and D6 as of
2026-10-03 [Observed]; D3 is the candidate bounded-mission packet and D4 a
ruling; D7 is packet A. If another doctrine packet is adopted first and
takes D8, this one takes the next free number on adoption.

**Companions in this directory.** `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`REVIEW-BRIEF.md`; `ROUND-1-DISPOSITIONS.md` once the review round has run.

---

## 0. The question, and the premise check's answer

The pursuit's move N15 records that Polaris renders zero Inferred claims
("S4-F3/C1-F4 confirm 0 of 729 tuples are Inferred (the word appears twice,
both in the legend)"), that "cross-surface correspondence has no claim type
to be true or false in" (L6-F2), and, in finding L2-F5, that "VIS-6(a)'s
promotion path has no destination for an observed-only project"
[Observed: quoted from `docs/pursuits/2026-09-22-vision-pursuit-data.json`,
move N15's `why` and finding L2-F5's title; the figures are the pursuit's,
not re-measured here]. It asked for one doctrine packet with six clauses
(a)–(f).

**One wording departure.** N15 describes (b) as "an AttributedAnswer
record for agent-produced answers". An agent-produced answer needs no
doctrine: it is an LLM assertion and is already Inferred
(`trust-and-evidence.md`; RFC2-25's `asserted-by-worker` tier). The gap the
pursuit's own merged move L3-M7 describes ("The attributed owner answer as
a first-class, non-derived record") and REQ-polaris-generation-031 specifies
is the *owner's* answer, so clause (b) drafts that. The owner may read N15
literally and decline (b) on that ground.

**The premise check, run before drafting, changes that framing.** Read
against doctrine and the accepted contracts, the six clauses fall into two
groups [Inferred: the drafter's reading; each row cites the clause it rests
on]:

| Clause | Does doctrine forbid it today? | What actually blocks it |
|---|---|---|
| (a) synthesis | **No.** `trust-and-evidence.md` lines 95–96: "Inferences may be woven into explanatory narrative but must never be indistinguishable from deterministic fact"; RFC7-2(c) admits a narrative claim "Inferred with its inference provenance" | PWB-REQ-012's closed set of four copy roles names no synthesis role, and whether `project-fact` may carry an Inferred composed sentence is unruled (the PWB coverage part records RFC7-2's three-way classification as "Unknown uncovered"); no inference-record format exists (RFC1 defers "inference records → inference profile / RFC 0002") |
| (b) attributed answer | **Not explicitly.** It is unnamed: `trust-and-evidence.md` names two non-evidence warrants, neither of which is an answer about intent; REQ-polaris-generation-031 (adopted) already requires attributed answers as a distinct class | Where it may live without breaking VIS-6 — for an observed-only project, nowhere (clause d) |
| (c) correspondence | **No.** RFC1-16 and RFC4-26 (accepted) already define class (ii) "inferred implementation mapping", entering "only via the inference profile, challenge authority only" | The inference profile is undefined; the POC specification excludes class (ii) (`openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md`, RFC4-26 row; POC-REQ-050, POC-REQ-052) |
| (d) observed-only project | **Yes, by omission.** `architecture.md` defines a governed project by its writable governance root; VIS-6 sends promoted content "to the governed plane"; an observed project with an empty write surface has none | Doctrine itself |
| (e) reflexive observation | **Silent.** No doctrine file names Syzygy observing itself [Observed: ledger §1]; VIS-7's trust floor assumes the observatory is not its own subject | Doctrine itself, plus P-74 Q3's three acts for the observation pipeline |
| (f) figures stage | **No.** VIS-4 lets agents draft; RFC2-25 names the `unadopted-draft` and `editorial-draft` surface states; RFC7-3/RFC7-4 make presentation non-citable | Implementation only, under the generator act |

So **three clauses (b, d, e) fill real doctrine gaps** and **three (a, c, f)
restate what doctrine and accepted contracts already permit**. The packet
still drafts all six, because the bead's acceptance asks for six and because
the owner may prefer them stated; but it recommends **no doctrine change**
for (a), (c) and (f), and routes their real blockers as owner questions
about contract and specification instruments (§7). Nothing here drafts those
instruments.

## 1. The six clauses

Each insertion below gives its anchor (exact current text, line numbers and
the file's sha256 at `origin/main` `6bb6ef26`, read 2026-10-03), the exact
bytes to insert, its change class, whether the packet recommends it, and its
no-change arm. File digests:

- `trust-and-evidence.md` sha256
  `6bf79befec771447b9f70206ee85a406eaffb16b98c8ae1c05f465cd7e486b58`
- `vision.md` sha256
  `93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d`
- `architecture.md` sha256
  `d1987f7f630b82eee359e14e89e6422ab74374a2578c218f73d47c80eefcb565`

No rule is renumbered, retired or reworded. VIS-1 through VIS-7 and SEC-1
through SEC-5 keep every current byte; the three-label rule and RFC2-25's
closed tiers are untouched.

### (a) Synthesis renders Inferred — `trust-and-evidence.md`

**Anchor** (lines 95–96):

> - Inferences may be woven into explanatory narrative but must never be
>   indistinguishable from deterministic fact.

**Insert** after line 96, as a sub-bullet of that bullet:

```markdown
  - A **synthesis** — prose a surface composes over several claims to order,
    emphasise, relate or abstract them — is an inference: it renders Inferred,
    names the exact claims it composes over, states no fact not derivable from
    them, anchors nothing, and is regenerated or withdrawn when any of them
    changes. A synthesis never fills an Unknown.
```

**Class:** Normative, narrowing — it adds obligations (name the inputs,
regenerate on change) to something already permitted. **Recommended:**
decline (no change). Doctrine already permits synthesis; what is missing is
a copy role and an inference-record format, both below doctrine (§7 Q-S1,
Q-C1). **No-change arm:** synthesis stays lawful and unbuilt; its rules are
written into whatever specification amendment opens the copy role.

### (b) The attributed owner answer — `trust-and-evidence.md`

**Anchor** (lines 44–49, the end of "Evidence, and the two other
warrants"):

> - **A work warrant** — creating or prioritizing work needs traceable
>   authority, not empirical evidence.
>   - Traceable authority means an approved requirement, a confirmed finding, a
>     declared policy, or an explicit owner decision.
>   - Status describes; a warrant authorizes. A claim that both declares status
>     and spawns work must pass both gates.

**Insert** after line 49, as a new paragraph (blank line before it), before
the blank line that precedes `## Status claims vs narrative claims`:

```markdown
**An attributed owner answer is neither evidence nor a warrant.** When the
owner answers a question about intent — a purpose, a beneficiary, which of two
sources governs — the answer is attributed, dated and individually
withdrawable, and is committed out to the governed plane like any decision
(vision.md VIS-6). It renders as the owner's record: Observed as a fact about
the record, never as evidence that the project does what the answer says, and
never as adopted intent unless an applicable act adopts it (vision.md VIS-4).
Withdrawing it invalidates exactly what was built on it.
```

**Class:** Normative — it names a class doctrine does not, and fixes how it
renders. **Recommended:** adopt, together with (d). **Alternative not
recommended:** pursuit move L3-M7 proposed the answer as a *third VIS-6
exception*, a non-derived fact living only in Syzygy. That widens VIS-6's
closed exception list; this clause instead keeps the answer inside VIS-6 by
committing it out, which is why it needs (d) for an observed-only project.
**No-change arm:** REQ-polaris-generation-031's attributed answers remain
specified, but for an observed-only project a persisted answer has no
lawful home, so the generator may ask and use an answer within one run and
must not retain it ("Missing input/persistence consent SHALL preserve the
limitation without silently retaining or using the answer").

### (c) The correspondence claim — `trust-and-evidence.md`

**Anchor** (lines 134–137):

> - **Rendering may blend the layers**, provided provenance is available where
>   the claim is consumed (hover, query, API field) and inferred structure stays
>   visually distinct from observed structure.
>   - A speculated future component must never look like an existing one.

**Insert** after line 137, as a second sub-bullet of that bullet:

```markdown
  - A **correspondence** — an inferred link from a claim on one surface to its
    subject on another, where no declared mapping exists — is an inferred
    relationship: it renders Inferred beside declared edges and is counted
    apart from them, carries challenge authority only, and never moves a claim
    off Unknown or counts as a declared mapping.
```

**Class:** Clarifying — RFC1-16/RFC4-26 already define class (ii) with
"challenge authority only"; the clause restates it at doctrine level and
extends the word from capability↔code to any cross-surface subject.
**Recommended:** decline (no change); the blocker is the undefined inference
profile and the POC specification's exclusion (§7 Q-C1, Q-S2). **No-change
arm:** class (ii) stays contract-defined and unbuilt.

### (d) The observed-only project — `architecture.md` and `vision.md`

**Anchor 1** (`architecture.md` lines 23–25):

> - Any other repository in the project is a declared **observed-source
>   repository**, read-only to Syzygy unless separately onboarded as a governed
>   project.

**Insert 1** after line 25, as a sibling bullet:

```markdown
- An **observed-only project** is one the owner has consented to observe but
  has not brought under Syzygy's write plane: Syzygy reads it under that
  consent and writes nothing into it (vision.md VIS-6 says where content about
  it lives).
```

**Anchor 2** (`vision.md` lines 232–234, in VIS-6):

> - **Syzygy's databases and views are projections.** Content it authors is
>   committed out to the governed plane, which then becomes the authoritative
>   source.

**Insert 2** after line 234, as a sub-bullet of that bullet:

```markdown
  - **Observed-only projects** (architecture.md): content Syzygy authors about
    such a project — a promoted note, a dismissal, an attributed answer — is
    committed out to the `.syzygy/**` of the governance root the owner runs
    Syzygy from. There it is Syzygy's attributed record about the project: it
    never anchors the project's capability map, is never presented as the
    project's own declaration, and is never cited as the project's text.
```

**Class:** Normative — it names a class and gives VIS-6's commit-out a
destination it does not have today. It does **not** widen VIS-5: the
destination is `.syzygy/**`, already a direct-write root, and nothing is
written into the observed project. **Recommended:** adopt. **What adoption
does not do:** it authorizes no write. The P-71 packet found that "writing a
governance artifact of the observing project *about* the observed project
is a new effect no act in force names"
(`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`, Q3), and the owner ruled
P-71 Q3 arm (b), "a pure drafter that writes no file"
(`decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, P-71 row).
Clause (d) names where such content *would* live; the first write still
needs its own act, and P-71's ruling stands until one exists. **No-change arm:** promotion,
dismissal and persisted answers about Butlers stay dead-ended, as L2-F5
records.

### (e) Self-observation never self-certifies — `trust-and-evidence.md`

**Anchor** (lines 175–180, the end of the trust floor):

> - every visual encoding means exactly what its legend says;
> - no credential or secret material appears in any surface, store, or endpoint
>   (security.md SEC-5).
>
> A change to Syzygy that breaks this floor, or presents inference as fact, may
> be rejected however well it otherwise works.

**Insert** after line 177, as a new paragraph between the floor's last
bullet and the sentence beginning "A change to Syzygy" (a blank line on
each side):

```markdown
**Self-observation never self-certifies.** When Syzygy observes its own
repository as an observed project, those observation records may raise
challenges and gaps and render as self-observed, but they never satisfy this
floor, Syzygy's release gate (vision.md VIS-7), or any claim that Syzygy is
aligned, converged or genome-complete.
```

**Class:** Normative, narrowing — it removes authority from a class of
observation records that does not exist yet. **Scope, stated because it is
the clause's main risk:** it binds observation records that Syzygy's
*observation pipeline* makes of its own repository. It does not touch
Syzygy's own tests, the canonical battery or the launch-gate
administration, which are gate artifacts produced by tooling, not records
of Syzygy observing itself as a project [Inferred: the drafter's reading of
the launch-gate record shape; the reviewer is asked to test it].
**Recommended:** adopt, before any of P-74 Q3's three self-observation acts
is performed. The owner named Syzygy itself as the first proving project
(`decisions/A6-RESOURCE-ENVELOPE-DECISION.md` line 25: "The syzygy
repository itself; second: butlers"), and P-76 Q2 already ruled that "an
observing project reading its own tree, recorded here, needs no consent
record, registry entry or act" for the generator's corpus. **No-change
arm:** self-observation stays possible under P-74 Q3's acts with no
doctrine rule against its records certifying the observatory.

### (f) Machine-drafted presentation stays a draft — `trust-and-evidence.md`

**Anchor:** the same bullet as (c), lines 134–137.

**Insert** after (c)'s sub-bullet if (c) is adopted, otherwise after line
137, as a sub-bullet of that bullet:

```markdown
  - A machine-drafted figure, passage selection or other presentation draft is
    an unadopted draft until a human adopts it, and once adopted is
    presentation only, never a claim source.
```

**Class:** Clarifying — VIS-4 ("may draft them, never adopt them"), RFC2-25's
`unadopted-draft` and `editorial-draft` states, and RFC7-3/RFC7-4 already
say this. **Recommended:** decline (no change); the figures stage (pursuit
move S3-M4) is implementation under the generator act and enters the
feature-request funnel on its own. **No-change arm:** nothing changes.

## 2. Each clause in the current tuple vocabulary

The tuple is label (three, closed), tier (RFC2-25, six, closed; a claim may
be untiered), Unknown reason (RFC2-24, twelve, closed), freshness (RFC2-10,
four, closed) and challenge state, plus RFC2-25's three sibling surface
states. **No clause needs a new label, tier, reason, freshness value or
surface state** [Inferred: mapping by the drafter].

| Clause | Label | Tier | Freshness | Challenge / surface state |
|---|---|---|---|---|
| (a) synthesis | Inferred | none (bare label; RFC2-25: "an untier'd claim renders at its bare label"). Not `asserted-by-worker`, which is "an LLM worker's assertion of an outcome" | derived from its inputs: any non-`fresh` input makes the synthesis stale or withdrawn (the regeneration rule) | may be challenged; can challenge nothing, since it establishes nothing |
| (b) attributed answer | Observed, as a fact about the record | `report-fact` ("'X reported Y' is Observed as a fact about the report; Y itself is not thereby Observed") | of the record's evaluation | withdrawal invalidates dependents; the answered question's implementation claims keep their own labels |
| (c) correspondence | Inferred | none | of the evaluation that computed it | challenge authority only (RFC4-26 class (ii)) |
| (d) observed-only record | Observed, as a fact about Syzygy's record | `report-fact`; a dismissal renders in the existing `dismissed-by-decision` state | of the record | — |
| (e) self-observation | Observed, at its ordinary tier | any tier, but a claim *about Syzygy itself* is restricted below `gate-backed` — RFC2-25 lets a tier "only *restrict* its parent label's authority" | ordinary | may raise challenges and gaps |
| (f) figures | — (not a claim) | — | — | `unadopted-draft`, then presentation (RFC7-4) |

## 3. Non-expansion on the write universe

None of the six widens VIS-5 [Inferred]:

- (a), (c), (f) write nothing new; they classify rendered content.
- (b) and (d) commit out to `.syzygy/**`, already a direct-write root, and
  never into an observed project. A first such write still needs its own
  act (§1 (d)).
- (e) removes authority; it writes nothing.

## 4. Blast radius

`IMPACT-LEDGER.md` records the sweep (predicate, population and every
authority-lane hit). Summary: no accepted contract uses any of the terms
the clauses introduce; the authority-lane hits are the anchors themselves,
REQ-polaris-generation-031's attributed answers (consistent with (b)), P-74
Q3's self-observation acts (consistent with (e), which should precede
them), and PWB-REQ-012's closed copy roles (the blocker for (a), untouched).
No authority-lane sentence is made false by adopting (b), (d) and (e)
[Inferred].

## 5. Why this is not self-licensing under VIS-4

No clause delegates a decision. (a), (c) and (f) restrict how inference and
drafts render; (b) requires an act before an answer becomes intent; (d)
names a destination and authorizes no write; (e) removes authority. None
touches the spec-adoption gate or any always-human class, so a doctrine
amendment (this packet, an owner act) is the whole mechanism [Inferred;
the owner may overrule].

## 6. What adoption would not do

- Build anything: every clause enters the feature-request funnel only after
  adoption (pursuit slice 3).
- Amend PWB-REQ-012, the POC specification's class (ii) exclusion, or
  REQ-polaris-generation-031.
- Define the inference profile or an inference-record format.
- Authorize any write about an observed project (§1 (d)), or perform any of
  P-74 Q3's self-observation acts.

## 7. The owner's questions

"Recommended" is this packet's view and binds nothing. Questions Q1–Q6 are
one per clause; each has a no-change arm. Q-C and Q-S are about
instruments *below* doctrine: this packet drafts none of them and only asks
whether the owner wants them drafted.

| # | Question | Arms | Recommended |
|---|---|---|---|
| Q1 | (a) synthesis | adopt / decline | **decline** — doctrine already permits it |
| Q2 | (b) attributed answer | adopt / adopt as a third VIS-6 exception instead (L3-M7; not drafted) / decline | **adopt**, with Q4 |
| Q3 | (c) correspondence | adopt / decline | **decline** — RFC1-16/RFC4-26 already define it |
| Q4 | (d) observed-only project | adopt / decline | **adopt** |
| Q5 | (e) self-observation | adopt / decline | **adopt**, before any P-74 Q3 act |
| Q6 | (f) figures | adopt / decline | **decline** — VIS-4 and RFC2-25 already cover it |
| Q-C1 | Commission a draft of the inference profile (RFC1's deferred "inference records → inference profile / RFC 0002"), the record format both (a) and (c) need? | commission / defer | the owner's call; neither (a) nor (c) can be built without it |
| Q-S1 | Commission a PWB specification amendment opening a synthesis copy role beside PWB-REQ-012's four? | commission / defer | after Q-C1 |
| Q-S2 | Commission a POC specification amendment admitting RFC4-26 class (ii) correspondences on the surfaces? | commission / defer | after Q-C1 |

## 8. Composition with packet A (D7) and candidate D3

- D7 inserts under `vision.md`'s "Not autonomous" bullet and at the end of
  `architecture.md`'s loop paragraph; D3 edits the same two passages. D8's
  `vision.md` insertion is in VIS-6 and its `architecture.md` insertion is
  under "Governed projects", so no byte overlaps [Observed: line ranges
  compared on 2026-10-03].
- **Line numbers move.** Whichever packet lands first shifts the other's
  anchors. D8's insertion points are defined by position (after the named
  bullet), and if an anchor's bytes have moved since the sha256 above, the
  changed anchor is a changed review subject: re-anchor through a fresh
  review (rule 10), never by applying judgment at the keyboard.
- `trust-and-evidence.md` is touched by D8 only.

## 9. How adoption would be recorded

Doctrine amendments carry no magic phrase (D3, D5, D6 precedent). For each
clause the owner adopts, in the owner's own words:

1. apply its insertion as the exact bytes shown, after re-checking the
   anchor's sha256;
2. add one `D8` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md` naming
   the clauses adopted and the owner's words;
3. regenerate the derived indexes `IMPACT-LEDGER.md` §4 names, add the
   adopted terms to the doctrine README glossary, and run the canonical
   battery.

A declined clause is recorded in the same row as declined. Register row
P-102 closes with the outcome. No arm edits this packet.
