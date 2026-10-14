# Doctrine amendment packet — D8 (proposed): Inferred as a first-class rendered state

**Status: DRAFT — not applied, not adopted; binds nothing.** Doctrine
amendment is an owner act (VIS-4). An agent session drafted this packet on
2026-10-03 for `syzygy-u05.15` (vision pursuit 2026-09-22, move N15,
"packet B"). It edits no doctrine byte, opens no gate, authorizes no
implementation and drafts no contract or specification amendment. A commit,
a merged pull request, a review, a closed bead or silence performs nothing;
only the owner's own words in the owner's own session do.

**Review state.** Round 1 returned `REVISE`
(docs/reviews/R-DOCTRINE-AMENDMENT-D8-1-RAW.md, line 4). Each finding was
repaired once and is recorded in `ROUND-1-DISPOSITIONS.md`; under the
stopping rule set in `REVIEW-BRIEF.md` no round 2 ran, so these bytes are
**repaired once, unconfirmed**.
*(Marked 2026-10-14: "no round 2 ran" is no longer true. On the owner's
direction of 2026-10-14
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`) a
round 2 read these bytes and returned `REVISE`, three revise findings and
nine notes (`docs/reviews/R-DOCTRINE-AMENDMENT-D8-2-RAW.md` line 4). The
bytes stay unconfirmed and go to the owner with those findings open;
`ROUND-2-DISPOSITIONS.md` beside this file classifies them.)*
*(Marked 2026-10-14, later the same day: "go to the owner with those
findings open" is no longer true. The owner directed one more cycle in the
lead session on 2026-10-14: every round-2 finding, notes included, repaired
once, then one fresh review under the same stopping rule. The twelve
round-2 findings are **repaired once on 2026-10-14, unconfirmed pending
round 3**; each repair is mapped in `ROUND-2-DISPOSITIONS.md`, "Repairs,
2026-10-14 (cycle 2)", and round 3's brief is `REVIEW-BRIEF.md` §"Round 3".)*
*(Marked 2026-10-14, round 3: "pending round 3" is no longer true. Round 3
ran and returned `REVISE` (`docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md`
line 4): one revise-level finding (under the packet's own reading of "the
governed plane", a (d2) dismissal either cannot take effect or violates
VIS-6, and the packet does not say which) and four notes, all open in
`ROUND-3-DISPOSITIONS.md`. Under the stopping rule the package is not
repaired again and the bytes stay unconfirmed; it comes to you with those
findings open.)*
*(Marked 2026-10-14, cycle 3: "the package is not repaired again" and
"comes to you with those findings open" are no longer true. On the
owner's cycle-3 direction of 2026-10-14 for P-102, given in the lead
session — "Drop dismissal from (d2)": "Dismissals of an observed-only
project's gaps can't live in the observing project's tree, so VIS-6 stays
intact. Then one more cycle." [Observed: as relayed by the lead session to
this repair lane; not yet recorded under `decisions/`] — the dismissal was
dropped from (d2) and every round-3 finding, notes included, was repaired
once; the mapping is `ROUND-3-DISPOSITIONS.md` §"Repairs, 2026-10-14
(cycle 3)".)* **Round-3 findings repaired once on 2026-10-14, unconfirmed
pending round 4.** Clauses (a), (d2) and (e) changed bytes; one arm was
added to Q5.

**Batched with packet A.** The bead asks for this packet to be offered
alongside D7 (held derived computation, register row P-101; its packet is
OWNER-DECISION-PACKET.md in the sibling directory
doctrine-amendment-held-derived-computation-d7, in pull request #296, not
yet on `main` when this was drafted).
*(Marked 2026-10-14: "not yet on `main`" is no longer true. D7's package is
on `main` at `09c7a61d`, where its packet and delta carry the `vision.md`
and `architecture.md` digests this packet cites (ledger §4). D7 was
repaired on its own branch concurrently with this repair, landing as
`7071a744`; this packet edits none of D7's bytes, and §8 states what was
re-checked.)*
The two are independent: each may be adopted, amended or declined without
the other (§8 states how their insertions compose).

**Identifier.** `D8` is provisional: the doctrine amendment log
(`../../../decisions/DOCTRINE-AMENDMENT-LOG.md`) holds D1, D5 and D6 as of
2026-10-03 [Observed]; D3 is the candidate bounded-mission packet and D4 a
ruling; D7 is packet A. If another doctrine packet is adopted first and
takes D8, this one takes the next free number on adoption.
*(Marked 2026-10-14: the log now also holds D9, adopted 2026-10-06, which
edited `security.md` and `v1.md` [Observed: log line 12]. D8 is still
free.)*

**Companions in this directory.** `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`REVIEW-BRIEF.md`, `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`,
`ROUND-3-DISPOSITIONS.md`.

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
(a)–(f). Since the pursuit, the owner's P-75 Q4 ruling reads "`Inferred`
added as a typed landing zone with no production constructor"
(`decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, P-75 row):
the state is representable in the shared model today and nothing constructs
it. This packet adds no constructor.

**One wording departure.** N15 describes (b) as "an AttributedAnswer
record for agent-produced answers". An agent-produced answer needs no
doctrine: it is an LLM assertion and is already Inferred
(`trust-and-evidence.md`; RFC2-25's `asserted-by-worker` tier). The gap the
pursuit's own merged move L3-M7 describes ("The attributed owner answer as
a first-class, non-derived record") and REQ-polaris-generation-031 specifies
is the *owner's* answer, so clause (b) drafts that. The owner may read N15
literally and decline (b) on that ground.

**Two departures from L3-M7 itself.** L3-M7 says the answer, "Rendered, it
is never Observed and never Inferred: it is attributed". That would be a
fourth label, which the three-label rule forbids; clause (b) renders it
Observed as a fact about the record (RFC2-25's `report-fact`) instead.
L3-M7 also calls the answer "the honest filler for a first-reading Unknown
whose resolution route says 'ask the owner'"; clause (b) forbids that: the
answer sits beside the Unknown, which stays Unknown, as (a) forbids a
synthesis to fill one.

**The premise check, run before drafting, changes that framing.** Read
against doctrine and the accepted contracts, the six clauses fall into three
groups [Inferred: the drafter's reading; each row cites the clause it rests
on]:

| Clause | Does doctrine forbid it today? | What actually blocks it |
|---|---|---|
| (a) synthesis | **No.** `trust-and-evidence.md` lines 95–96: "Inferences may be woven into explanatory narrative but must never be indistinguishable from deterministic fact"; RFC7-2(c) admits a narrative claim "Inferred with its inference provenance". **But on Polaris an accepted contract already decides how it renders:** RFC7-20 (`contracts/rfcs/RFC-0007/narrative-contract.md` line 416) reads "Generated prose appears **only** in the explicit **editorial-draft** state", "**non-citable**: never an anchor target (RFC7-10), never in the citation graph, never satisfying a claim, never green", and RFC7-2(c)'s Inferred claims exist only in curated narrative, which only an authoring act produces (RFC7-2, "The check binds the authoring act"). A Polaris synthesis composed by a declared inference process is generated prose, so today it is an `editorial-draft`, not an Inferred claim [Inferred: the drafter's reading; the owner's in-force RFC7-20 reading act of 2026-10-07 describes an agent draft the same way, "The agent draft renders as an editorial draft" (`decisions/DOSSIER-LOCAL-AGENT-RFC7-20-READING-IN-FORCE-ACT.md`)] | On Polaris, RFC7-20 itself: a synthesis that renders as an Inferred *claim* there needs an RFC 0007 amendment (§7 Q-C3, asked, not drafted). Everywhere, PWB-REQ-012's closed set of four copy roles names no synthesis role, and whether `project-fact` may carry an Inferred composed sentence is unruled (the PWB coverage part's RFC7-2 row, "Non-factual framing is machine-marked non-normative", is "**Unknown uncovered** — its closed roles contain no `non-normative` standing"; that row is RFC7-2(b) only, and whether `project-fact` may carry an Inferred composed sentence is this drafter's open question [Inferred]); no inference-record format exists (RFC1 defers "inference records → inference profile / RFC 0002"); and the PWB coverage part's RFC7-20 row (line 74) records "PWB explicitly excludes LLM generation/inference at observation and render time" |
| (b) attributed answer | **Not explicitly.** It is unnamed: `trust-and-evidence.md` names two non-evidence warrants, neither of which is an answer about intent; REQ-polaris-generation-031 (adopted) already requires attributed answers as a distinct class | Where it lives for a project Syzygy may not write: VIS-6 sends it "to the governed plane", and the only plane such a project has is its own (clause (d)) |
| (c) correspondence | **No.** `trust-and-evidence.md` lines 118–119: "**Inference has no authority to establish a status — only to challenge one.**", for any subject; RFC1-16 and RFC4-26 (accepted) define class (ii) "inferred implementation mapping" for capability↔code, entering "only via the inference profile, challenge authority only" | The inference profile is undefined; the POC specification excludes class (ii) (`openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md`, RFC4-26 row; POC-REQ-050, POC-REQ-052) |
| (d) observed-only project | **No, not in the abstract.** VIS-5 makes a project's own `openspec/**` and `.syzygy/**` lawful direct-write roots, and `architecture.md` (line 14; Definitions, lines 210–216) requires a designated governance root, not a writable one. What doctrine lacks is a *second* destination: VIS-6 names no home for content about a project other than that project's own plane | Not doctrine, today: the registered adapter declares `writeSurface` empty and the 2026-09-02 act bounds it (L2-F5's detail). P-71-Q5's ruling already names the act route into the observed project's own plane: "(1) a dated owner act naming the write, (2) a registry-entry amendment act taking `writeSurface` from empty to the named path". Clause (d) is an **alternative** to that route, one that never writes into the observed project |
| (e) reflexive observation | **Silent.** No doctrine file names Syzygy observing itself [Observed: ledger §1]; the trust floor does not say whether records whose subject is the observatory's own repository may certify it | Doctrine itself. P-74 Q3's three acts govern whether a test-only self-observation may run, not what its records may certify |
| (f) figures stage | **No.** VIS-4 lets agents draft; RFC2-25's `editorial-draft` state "stays non-citable even after" the human authorship act completes; RFC7-3/RFC7-4 make presentation non-citable | Implementation only, under the generator act |

So **two clauses (b, e) fill doctrine gaps**; **one (d) offers a
destination doctrine does not name, as an alternative to an act route that
already exists**; and **three (a, c, f) restate what doctrine and accepted
contracts already permit or, for (a) on Polaris, already decide**
(RFC7-20; repaired 2026-10-14 after round-2 finding 2, which found this
contract unnamed here). The packet still drafts all six, because the
bead's acceptance asks for six and because the owner may prefer them
stated; but it recommends **no doctrine change** for (a), (c) and (f), and
routes their real blockers as owner questions about contract and
specification instruments (§7). Nothing here drafts those instruments.

## 1. The six clauses

Each insertion below gives its anchor (exact current text, line numbers and
the file's sha256 at `origin/main` `6bb6ef26`, read 2026-10-03), the exact
bytes to insert, its change class, whether the packet recommends it, and its
no-change arm. The three digests are unchanged at `09c7a61d`, where the
2026-10-14 repairs re-read every anchor, including (e)'s and (d1)'s moved
ones [Observed: scripted `sha256sum`]. File digests:

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
    emphasise, relate or abstract them — is an inference: it carries its
    inference provenance, names the exact claims it composes over, states no
    fact not derivable from them, and is never itself an anchored claim. It
    renders Inferred, unless the surface admits generated prose only as a
    draft, where it is that draft and is no claim while it stays one. It is no
    fresher than its stalest input, and is withdrawn until regenerated when any
    input is broken or superseded. A synthesis never fills an Unknown.
```

*(Repaired 2026-10-14, cycle 3, round-3 note 3: "where it is that draft
and never a claim" became "where it is that draft and is no claim while it
stays one", so the bytes no longer forbid what RFC7-21's human adoption
act may later make of the draft — curated narrative, in which RFC7-2(c)
admits Inferred claims — and Q-C3's rationale no longer contradicts them.
On such a surface the freshness and withdrawal sentences bind the draft as
a rendered object, not as a claim: a stale input makes the draft render
stale, and a broken or superseded one withdraws it.)*

*(Repaired 2026-10-14, round-2 finding 2: the bytes above replace "it
renders Inferred, names the exact claims…", which on Polaris contradicted
accepted RFC7-20.)*

**Class:** Normative, narrowing — it adds obligations (name the inputs,
withdraw on a broken or superseded input) to something already
permitted. "Never itself an anchored claim" means it is not an RFC7-2(a)
claim; naming its inputs may still use RFC7-9/RFC7-10 anchor mechanics.
**Relation to RFC7-20 (accepted).** On Polaris, RFC7-20 confines generated
prose to the `editorial-draft` state, non-citable and "never satisfying a
claim", and RFC7-21 makes adoption into curated narrative a human act. The
clause's "unless the surface admits generated prose only as a draft"
sentence defers to that rule without naming a contract (doctrine cites no
RFC by number [Observed: 0 lines match `RFC ?[0-9]` in the six doctrine
files at `09c7a61d`]); so on Polaris a synthesis is an `editorial-draft` with its inference
provenance, and only on a surface no such rule governs does it render as an
Inferred claim [Inferred: the drafter's reading, for round 3 to test]. The
clause adds to RFC7-20 only the input, freshness and Unknown obligations.
Making a Polaris synthesis an Inferred *claim* instead would contradict
RFC7-20, which no doctrine clause here attempts; that route is §7 Q-C3, an
RFC 0007 question asked, not drafted. **Recommended:** decline (no change).
Rechecked after RFC7-20 (round-2 finding 2): doctrine (lines 95–96) already
permits synthesis on every surface, and on Polaris an accepted contract
already decides its rendering, so the clause would add obligations, not a
permission. What is missing is a copy role, an inference-record format and,
for PWB, lifting its own exclusion of generation at render time (the PWB
coverage part's RFC7-20 row, line 74), all below doctrine (§7 Q-S1, Q-C1,
Q-C3). The recommendation is unchanged; its reason now names RFC7-20.
**No-change arm:** synthesis stays lawful and unbuilt; on Polaris it can
only be an `editorial-draft`; its rules are written into whatever
specification amendment opens the copy role.

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
owner answers a question about intent — a purpose, a beneficiary, a priority
between two goals — the answer is attributed, dated and individually
withdrawable, and is committed out to the governed plane like any decision
(vision.md VIS-6). It renders as the owner's record: Observed as a fact about
the record, never as evidence that the project does what the answer says, and
never as adopted intent unless an applicable act adopts it (vision.md VIS-4).
It sits beside an Unknown, never in its place. Withdrawing it invalidates
exactly what was built on it.
```

**Class:** Normative — it names a class doctrine does not, and fixes how it
renders. **Not an adjudication:** an owner ruling on which of two
contradicting sources governs resolves RFC2-24 reason 8,
`contradicted-pending-adjudication` ("Owner adjudication"), and is a
recorded human decision, not this class; REQ-polaris-generation-031 keeps
"contradiction or interpretation dispositions" apart from answers too.
**Placement:** the section's opening sentence (line 14) and heading
("Evidence, and the two other warrants") enumerate warrants and stay true,
since (b) is not a warrant; but they would no longer list everything the
section holds. Retitling them is an editorial question this packet does
not draft. **Recommended:** adopt, together with (d). **Alternative not
recommended:** pursuit move L3-M7 proposed the answer as a *third VIS-6
exception*, a non-derived fact living only in Syzygy. That widens VIS-6's
closed exception list; this clause instead keeps the answer inside VIS-6 by
committing it out, which is why it needs (d), or P-71-Q5's act route, for
an observed-only project. **No-change arm:** REQ-polaris-generation-031's
attributed answers remain specified, and are consent-gated for both
persistence and use (REQ-polaris-generation-019, amendment `spec.md` line
508: "Clarification persistence and draft use SHALL require applicable input
classification, content consent and retention"). For a project Syzygy may not write, a persisted answer has no
lawful home until (d) or the act route supplies one, and use within a run
stays gated by that consent.

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

**Class:** Normative, narrowing over a wider domain — RFC1-16/RFC4-26 bound
class (ii) to capability↔code; the clause names the relation for any
cross-surface subject and adds that it is counted apart from declared
edges. Its authority limit is already doctrine for every subject (lines
118–119). **Recommended:** decline (no change); the authority limit already
binds, and the blocker is the undefined inference profile and the POC
specification's exclusion (§7 Q-C1, Q-S2). **No-change
arm:** class (ii) stays contract-defined and unbuilt.

### (d) The observed-only project — `architecture.md` and `vision.md`

**Anchor 1** (`architecture.md` lines 18–27, the definition paragraph and
the two repository bullets under it):

> A **governed project** is one or more repositories, one owner, and **exactly
> one designated governance root**: the repository holding the project's single
> `openspec/**` and `.syzygy/**` plane. The project has been explicitly brought
> under Syzygy observation.
>
> - Any other repository in the project is a declared **observed-source
>   repository**, read-only to Syzygy unless separately onboarded as a governed
>   project.
> - Onboarding is recorded, per-repository consent (security.md SEC-4).
>   **Every observed repository consents, governance root or not.**

**Insert 1** after line 27, as a new paragraph after the bullet list and
before the blank line that precedes "Syzygy governs an orthogonal" (a blank
line on each side):

```markdown
An **observed-only project** is a governed project whose governance root
Syzygy may read under the owner's consent but may not write: no act in force
names a write into it. It is still governed, and its plane is still its own;
Syzygy writes nothing there until an act names the write (vision.md VIS-6 says
where content Syzygy authors about it lives meanwhile).
```

*(Repaired 2026-10-14, round-2 note 8: the bytes above replace a sibling
bullet of the repository bullets, which defined a kind of project among
kinds of repository, and its phrase "its write surface is empty", which
brought the registry field `writeSurface` into doctrine undefined.)* **It
is a governed project.** Lines 18–21 make a project "explicitly brought
under Syzygy observation" a governed project, and an observed-only project
is one; (d1) says so, so "the governed plane" in VIS-6 and in (b) still
means the project's own plane, which Syzygy may not write, and (d2) adds a
second destination beside it [Inferred: the drafter's reading]. That
second destination takes no dismissal: a dismissal takes effect only in
the governed plane of the project whose gap it dismisses
(`trust-and-evidence.md` lines 42–43; VIS-6's violation sentence), so
repaired (d2) keeps every dismissal of an observed-only project's gap in
that project's own plane, reachable only by an act naming the write
(repaired 2026-10-14, cycle 3, round-3 finding 1, on the owner's ruling
quoted after Insert 2 below). Line 14's
"where Syzygy writes only `openspec/**` and `.syzygy/**`" bounds a write and
grants none, so a governed project Syzygy writes nothing into stays inside
it [Inferred]. The registry's empty `writeSurface` and the 2026-09-02 act
are how Butlers, the case L2-F5 names, is bound today (§0); (d1) states the effect in doctrine terms, "no
act in force names a write", and leaves the registry field to RFC material.

**Anchor 2** (`vision.md` lines 232–234, in VIS-6):

> - **Syzygy's databases and views are projections.** Content it authors is
>   committed out to the governed plane, which then becomes the authoritative
>   source.

**Insert 2** after line 234, as a sub-bullet of that bullet:

```markdown
  - **Observed-only projects** (architecture.md): content Syzygy authors about
    such a project — a promoted annotation, an attributed answer — is
    committed out to the `.syzygy/**` of the observing project, the governed
    project that records the consent to observe it. There it is Syzygy's
    attributed record about the project: it never anchors the project's
    capability map, is never presented as the project's own declaration, is
    never cited as the project's text, and never suppresses a gap of the
    project. A dismissal of such a project's gap is not committed there: it
    takes effect only in the project's own governed plane, so it waits for an
    act that names that write.
```

*(Repaired 2026-10-14, cycle 3, round-3 finding 1, on the owner's ruling
for P-102: "Drop dismissal from (d2)" — "Dismissals of an observed-only
project's gaps can't live in the observing project's tree, so VIS-6 stays
intact." [Observed: as relayed by the lead session to this repair lane;
not yet recorded under `decisions/`.] The bytes above replace "a promoted
note, a dismissal, an attributed answer" and "and is never cited as the
project's text." Three changes: "a dismissal" is dropped; "a promoted
note" becomes "a promoted annotation", because VIS-6(a) promotes a note
"as an annotation or a dismissal" and a note promoted as a dismissal is a
dismissal; and two sentences are added. "Never suppresses a gap" closes
the route by which a record that is not called a dismissal could still do
a dismissal's work. The last sentence says where such a dismissal can
lawfully live — only in the observed project's own governed plane, which
`trust-and-evidence.md` lines 42–43 ("takes effect only once committed out
to the governed plane") and VIS-6's violation sentence ("a dismissal
taking effect without living in the governed plane") already require — and
that it waits for an act naming that write, which today is P-71-Q5's route.
Without the general sentence, dropping the example alone would leave a
dismissal inside "content Syzygy authors about such a project".)*

**Class:** Normative — it names a class consistent with the Definitions
entry for **Project** (the observed-only project keeps its one designated
governance root; only no write into it is named) and gives VIS-6's
commit-out a second destination. It does **not** widen VIS-5: the
destination is `.syzygy/**`, already a direct-write root, and nothing is
written into the observed project. **"Observing project" has two senses
in the record** (repaired 2026-10-14, round-2 note 6, which found the
earlier attribution to P-76 Q2 wrong). (d2) uses the M4 funnel Q3's sense,
one project writing "a governance artifact of the observing project *about*
the observed project" (`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`, Q3).
The owner's P-76 Q2 ruling uses the phrase for self-observation, "an
observing project reading its own tree", which is clause (e)'s subject, not
(d)'s; (d2) defines its own sense in place ("the governed project that
records the consent to observe it"). **Recommended:** adopt, as the owner's trade-off between two
routes: (d) keeps every observed repository untouched but has one project
hold records about another; P-71-Q5's act route keeps each project's
content in its own plane but writes into the observed repository.
**Cross-project caution:** RFC1 defers "Cross-project relationship
semantics → portfolio profile (SDR-30)", and SDR-30 says such
relationships "come from project declarations or render
**unconfirmed/asymmetric**". A record *about* another project is not by
itself a relationship between their entities [Inferred]; if one ever links
them, SDR-30 governs its rendering. A promoted annotation, one of (d2)'s
two examples, always names an entity of the observed project, what it
annotates (round-2 note 9; the dismissal example, which named that
project's gap, was dropped 2026-10-14, cycle 3). So the question is not
whether such records stay unlinked, which they cannot, but whether naming
another project's entity is an SDR-30 relationship or only a reference;
§7 Q-C2 now asks that. **Offboarding is unstated.** `architecture.md` lines 115–117 keep committed-out annotations
and dismissals "with the repository" when a project offboards. Under (d2)
records about an observed-only project (annotations and answers, never
dismissals) live in the observing project's tree, and (d2) does not say
what happens to them when the observed project offboards; §7 Q-D1 asks,
and no arm is drafted. **What adoption does not do:** it authorizes no write. The P-71 packet found that "writing a
governance artifact of the observing project *about* the observed project
is a new effect no act in force names"
(`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`, Q3), and the owner ruled
P-71 Q3 arm (b), "a pure drafter that writes no file"
(`decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, P-71 row).
**The arm the owner declined placed content where (d) points.** The
funnel's recommended arm (a) had the drafter emit the packet "into Syzygy's
own `.syzygy/governance/decisions/`", the class of destination (d2) names,
and the funnel itself named that arm's cost: "a drafted act about the
observed project's gaps would sit in the governance tree of a project that
does not govern it". The owner chose (b) instead; the ruling records no
reason [Observed: P-71 row, rulings file line 58] (round-2 note 7). (d)
does not reopen that choice: it names in doctrine where such content *would* live, writes
nothing, and leaves P-71 Q3's "writes no file" standing. Adopting (d) does
make arm (a)'s destination doctrinally describable, so a later act naming
that write would no longer need a doctrine change first; that is the
trade-off the owner is asked to weigh, not one this packet settles. Since
the cycle-3 repair, that reaches only drafted content that suppresses no
gap: a drafted act that would dismiss one of the observed project's gaps
is not among what (d2) makes describable in the observing tree, and still
has only P-71-Q5's route into the project's own plane [Inferred]. The
first write still needs its own act, and P-71's ruling stands until one
exists.
**No-change arm:** content about Butlers has one lawful route, into its own
plane by P-71-Q5's two acts; until the owner performs them it has nowhere to
land, as L2-F5 records. On the adopt arm, a dismissal of Butlers' gap is in
the same position: (d2) gives it no second destination.

### (e) Self-observation never certifies Syzygy's own alignment — `trust-and-evidence.md`

**Anchor** (lines 57–67, "Certificate and status claims need evidence"):

> **Certificate and status claims need evidence.** A claim is one if it:
>
> - turns a badge or indicator green;
> - declares alignment, convergence, or genome-completeness;
> - affects a certificate *(certificates are post-V1; this trigger is
>   future-tagged until their RFC exists)*; or
> - says a gap is **factually resolved or absent**.
>
> No evidence means **Unknown**, not success. A claim that meets any trigger is
> a status claim **whatever its prose form**: a narrative sentence doing a green
> badge's work is judged as a badge.

**Insert** after line 67, as a new paragraph before the blank line that
precedes "**A gap leaves a surface in exactly two ways**" (a blank line on
each side):

```markdown
**Self-observation never certifies Syzygy's own alignment.** When Syzygy's
observation pipeline evaluates Syzygy's own governance root as its subject,
the observation records may surface gaps and contradictions and render with
that subject disclosed, but they are never the evidence for a claim that
declares Syzygy's own alignment, convergence or genome-completeness: such a
claim, resting only on such records, has no evidence and renders Unknown.
Evidence that any of the trust floor's four properties holds may come from
any subject, this one included, and the rule adds no property to the trust
floor.
```

*(Repaired 2026-10-14, cycle 3, round-3 note 2. Three changes to the
bytes: the citation "(vision.md VIS-7)", which tied the denial to the rule
whose body is the trust floor, is dropped, since the denial qualifies the
status-claim trigger in this same section (line 60) and needs no
cross-reference; "a claim resting only on such records" becomes "such a
claim, resting only on such records", so the Unknown sentence names only
the denied kind of claim and no longer reads as denying the floor-property
claims the next sentence admits; and the heading "Self-observation never
self-certifies" becomes "Self-observation never certifies Syzygy's own
alignment", no wider than the rule.)*

*(Repaired 2026-10-14, round-2 finding 1 and note 10. The bytes above
replace a paragraph that sat between the trust floor's last bullet and its
closing sentence (anchor lines 175–180) and denied self-observation records
to Syzygy's "release verdict" while letting them evidence the floor, which
is the release verdict (lines 159–161: "a Syzygy release that breaks any of
four properties is blocked"; VIS-7). Three changes: "release verdict" is
dropped, so the denial covers exactly the line-60 trigger, "declares
alignment, convergence, or genome-completeness"; the permissive sentence
now covers all four floor properties, not only determinism and links, so a
self-observation render shown to hold no secret material (bullet 4) or
legend-faithful encodings (bullet 3) is not under the denial; and the
paragraph moves out of the trust floor's span to the status-claim
triggers it qualifies, saying it is not a fifth floor property.)*

**Class:** Normative, narrowing — it removes authority from a class of
observation records that does not exist yet. **Scope, carried by the
inserted bytes:** the trigger is the pipeline evaluating Syzygy's own
governance root, and the bound object is "observation records", a defined
doctrine term ("the immutable result of one identified status evaluation",
line 144). Syzygy's tests, the canonical battery and a launch-gate
administration are not observation records, so the clause does not reach
them [Inferred; the round-1 reviewer reached the same reading from the
launch-gate record's keys]. Nor does it reach the release verdict: what the
floor blocks a release on is the four properties, and evidence for any of
them may come from this subject. **Release-blocking?** No, as drafted
(round-2 note 10). The rule restates, for one record class, what line 65
already does for every claim ("No evidence means **Unknown**, not
success"), so breaking it means rendering a status claim on records that
cannot carry it, a defect under the status-claim rule, not a new floor
property. If the owner wants violating (e) itself to block a release, the
route is a fifth floor bullet, which changes VIS-7's "in short" list too;
it is offered as Q5's second arm and not drafted [Inferred: the drafter's
reading]. **The other triggers, intended** (round-3 note 2, cycle 3): the
denial covers only line 60's trigger. A green badge about Syzygy itself
(line 59) or a gap of Syzygy's "factually resolved or absent" (line 63)
may still rest on self-observation records, under the ordinary
status-claim rule and on the evidence rules every subject meets; that is
how the drafter intends it, since such records are evidence of what they
observed, and a narrower clause keeps the floor-property evidence above
available [Inferred: the drafter's reading]. A reader may still call a
green badge about Syzygy, resting on Syzygy's own records,
self-certification; if the owner wants those triggers denied too, that is
Q5's third arm, not drafted.
**Recommended:** adopt as drafted, before any of P-74 Q3's three
self-observation acts is performed. The owner named Syzygy itself as the first proving project
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
    an editorial draft: it is not a claim source before a human authors it into
    a presentation artifact, and stays non-citable after.
```

**Class:** Clarifying — VIS-4 ("may draft them, never adopt them"), RFC2-25's
`editorial-draft` state (it "awaits a **human authorship act into a
non-authoritative artifact**, and **stays non-citable even after that act
completes**", as distinct from `unadopted-draft`, which binds once adopted)
and RFC7-3/RFC7-4 already say this. **One extension, disclosed** (round-2
note 5): RFC2-25 defines `editorial-draft` as "Narrative prose under
revision", so applying it to a figure or a passage selection extends that
contract state's stated semantics past prose [Inferred]. The adopted
generator specification already does so for one kind of figure,
"Generated diagrams SHALL remain editorial-draft until their applicable
authorship act" (`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
line 98), and a passage selection has no such precedent. Adopting (f)
would make that extension doctrine's for every presentation draft, which
is one more reason the packet recommends decline. **After** the human
authorship act the draft is no longer in the `editorial-draft` state: it is
presentation, non-citable by RFC7-4 ("adopted-after-review"), which is what
the clause's "stays non-citable after" says. **Recommended:** decline (no change); the figures stage (pursuit
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
| (a) synthesis | Inferred; on Polaris, not a claim: the `editorial-draft` sibling state RFC7-20 confines generated prose to, carrying its inference provenance (repaired 2026-10-14, round-2 finding 2) | none (bare label; RFC2-25: "an untier'd claim renders at its bare label"). Not `asserted-by-worker`, which is "an LLM worker's assertion of an outcome" | `fresh` only while every input is `fresh`; `stale` if any input is `stale`; any `broken` or `superseded` input withdraws it from the render until regenerated ("withdrawn" is a render action, not a fifth freshness value) | may be challenged; can challenge nothing, since it establishes nothing |
| (b) attributed answer | Observed, as a fact about the record | `report-fact` ("'X reported Y' is Observed as a fact about the report; Y itself is not thereby Observed") | of the record's evaluation | withdrawal invalidates dependents; the answered question's implementation claims keep their own labels |
| (c) correspondence | Inferred | none | of the evaluation that computed it | challenge authority only (RFC4-26 class (ii)) |
| (d) observed-only record | Observed, as a fact about Syzygy's record | `report-fact`. No (d2) record is a dismissal or suppresses a gap, so none renders `dismissed-by-decision`; a dismissal of an observed-only project's gap renders in that state only once it lives in that project's own plane (repaired 2026-10-14, cycle 3, round-3 finding 1: this cell said "a dismissal renders in the existing `dismissed-by-decision` state") | of the record | — |
| (e) self-observation | Observed, at its ordinary tier | its ordinary tier. The clause is a rule on which records a claim may cite, not a tier: such records never back a claim about Syzygy's own status, and since RFC2-25 makes `gate-backed` "The **only** tier that may support a positive status claim", no such claim is ever `gate-backed` from them | ordinary | may surface gaps and contradictions. "Subject disclosed" is the observation record's own repository identity, a provenance fact, not a tier or state |
| (f) figures | — (not a claim) | — | — | `editorial-draft` before the human authorship act (RFC2-25, RFC7-20); after it, presentation, non-citable (RFC7-4). Applying the state to a figure or passage selection extends RFC2-25's "Narrative prose" (§1 (f); repaired 2026-10-14, round-2 note 5) |

## 3. Non-expansion on the write universe

None of the six widens VIS-5 [Inferred]:

- (a), (c), (f) write nothing new; they classify rendered content.
- (b) and (d) commit out to the observing project's `.syzygy/**`, already a
  direct-write root, and never into an observed project. A first such write still needs its own
  act (§1 (d)).
- (e) removes authority; it writes nothing.

## 4. Blast radius

`IMPACT-LEDGER.md` records the sweep (predicate, population and every
authority-lane hit). Summary: no accepted contract uses any of the terms
the clauses introduce; the authority-lane hits are the anchors themselves,
REQ-polaris-generation-031's attributed answers (consistent with (b)), P-74
Q3's self-observation acts (consistent with (e), which should precede
them), and PWB-REQ-012's closed copy roles (the blocker for (a), untouched).
Applying any insertion also drifts generated artifacts the battery checks,
including the context-budget report and its fixture anchors (ledger §4).
Insertion (d2), the only `vision.md` change, also fails the Polaris
understanding adoption recorder's `--check`, which binds `vision.md` as a
frozen input of a confirmed review; that is a gate, not a rebuild (§7 Q-A1).
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
- Define the inference profile, an inference-record format or the
  portfolio profile.
- Authorize any write about an observed project (§1 (d)), or perform any of
  P-74 Q3's self-observation acts.

## 7. The owner's questions

"Recommended" is this packet's view and binds nothing. Questions Q1–Q6 are
one per clause; each has a no-change arm. Q-C and Q-S are about
instruments *below* doctrine: this packet drafts none of them and only asks
whether the owner wants them drafted. Q-A1 is about applying (d2); Q-D1,
added 2026-10-14, asks about a case (d2) leaves unstated and drafts no
bytes for it.

| # | Question | Arms | Recommended |
|---|---|---|---|
| Q1 | (a) synthesis | adopt / decline | **decline** — doctrine already permits it, and on Polaris accepted RFC7-20 already decides it renders as an `editorial-draft` (rechecked 2026-10-14 after round-2 finding 2; §1 (a)) |
| Q2 | (b) attributed answer | adopt / adopt as a third VIS-6 exception instead (L3-M7; not drafted) / decline | **adopt**, with Q4 or the act route |
| Q3 | (c) correspondence | adopt / decline | **decline** — `trust-and-evidence.md` lines 118–119 already bind its authority limit for every subject, and RFC1-16/RFC4-26 define it for capability↔code; the blockers are below doctrine (repaired 2026-10-14, round-2 note 11) |
| Q4 | (d) observed-only project | adopt / use P-71-Q5's act route into the observed project instead / decline | **adopt**; the trade-off is the owner's (§1 (d)) |
| Q5 | (e) self-observation | adopt as drafted (beside the status-claim triggers, not a floor property; denies only the alignment, convergence and genome-completeness trigger) / adopt as a fifth, release-blocking trust-floor bullet instead (not drafted; it would also change VIS-7's "in short" list in `vision.md`, tripping Q-A1's gate) / widen the denial to every status-claim trigger about Syzygy itself, a green badge and a gap "factually resolved or absent" included (not drafted; added 2026-10-14, cycle 3, round-3 note 2) / decline | **adopt as drafted**, before any P-74 Q3 act (arms repaired 2026-10-14, round-2 note 10; heading and citation repaired, cycle 3) |
| Q6 | (f) figures | adopt / decline | **decline** — VIS-4 and RFC2-25 already cover it |
| Q-C1 | Commission a draft of the inference profile (RFC1's deferred "inference records → inference profile / RFC 0002"), the record format both (a) and (c) need? | commission / defer | the owner's call; neither (a) nor (c) can be built without it |
| Q-C2 | Must the portfolio profile (RFC1's deferred "Cross-project relationship semantics → portfolio profile (SDR-30)") exist before (d) is used? A promoted annotation always names an entity of the observed project, so the records cannot stay unlinked (arms repaired 2026-10-14, round-2 note 9; "A dismissal or" dropped 2026-10-14, cycle 3, since (d2) no longer holds dismissals) | yes, before any (d) record / no: a record that names another project's entity is a reference, not an SDR-30 relationship, and only a link *between* entities of the two projects waits for the profile | the owner's call |
| Q-C3 | Should a synthesis on Polaris ever render as an Inferred narrative claim (RFC7-2(c)) rather than an `editorial-draft`? That needs an RFC 0007 amendment of RFC7-20 ("Generated prose appears **only** in the explicit **editorial-draft** state"), a contract act; nothing here drafts it (added 2026-10-14, round-2 finding 2) | no, RFC7-20 stands and a Polaris synthesis stays an `editorial-draft` / commission an RFC7-20 amendment draft | **no** — the drafter sees no gap RFC7-21's human adoption path leaves; the owner's call |
| Q-D1 | When an observed-only project offboards, what happens to records about it that (d2) placed in the observing project's tree? `architecture.md` lines 115–117 keep committed-out annotations and dismissals "with the repository", which for (d2) records is the observing project's; since the cycle-3 repair those records are annotations and answers only (added 2026-10-14, round-2 note 9) | they stay as the observing project's dated records and stop rendering for the offboarded project / they are exported to the owner and deleted with its projections / decide when (d) is first used | the owner's call; no arm is drafted into (d2) |
| Q-A1 | Applying (d2) changes `vision.md`, which retires the Polaris understanding reconciliation review for `scripts/record_polaris_understanding_adoption.py --check` (ledger §4). Resolve it by a fresh reconciliation review over the amended `vision.md`, or by a reviewed recorder change moving `vision.md` into its history set? D7's `vision.md` insertion raises the same question (D7's Q6, added in its cycle-3 repair) | reconcile / move to history / decline (d2) | the owner's call; one answer serves D7 and D8 together |
| Q-S1 | Commission a PWB specification amendment opening a synthesis copy role beside PWB-REQ-012's four? Under RFC7-20 that role's strings would be `editorial-draft`, unless Q-C3 amends it, and PWB would also lift its own exclusion of generation at render time (coverage part, RFC7-20 row, line 74) | commission / defer | after Q-C1 and Q-C3 |
| Q-S2 | Commission a POC specification amendment admitting RFC4-26 class (ii) correspondences on the surfaces? | commission / defer | after Q-C1 |

## 8. Composition with packet A (D7) and candidate D3

- D7 inserts under `vision.md`'s "Not autonomous" bullet and at the end of
  `architecture.md`'s loop paragraph; D3 edits the same two passages. D8's
  `vision.md` insertion is in VIS-6 and its `architecture.md` insertion is
  under "Governed projects", so no byte overlaps [Observed: line ranges
  compared on 2026-10-03]. Re-checked 2026-10-14 at `09c7a61d`, where D7
  is on `main`: D7 anchors `vision.md` lines 105–107 and `architecture.md`
  lines 329–334 (D7 packet lines 93 and 127); D8's repaired anchors are
  `vision.md` 232–234, `architecture.md` 18–27 and `trust-and-evidence.md`
  57–67, 95–96 and 134–137, so no bytes overlap [Observed]. D7's
  concurrent round-2 repair landed on `main` as `7071a744` while this
  repair was open; this repair was rebased onto it, and at `7071a744` D7's
  anchors are still `vision.md` lines 105–107 and `architecture.md` lines
  329–334 (now D7 packet lines 126 and 160), its commit stating "Section
  1's proposed doctrine bytes are unchanged" [Observed: anchor lines
  re-read; D7's other repairs not reviewed here]. No overlap.
- **Shared gate.** Both packets' `vision.md` insertions trip the same
  recorder gate (Q-A1; D7 asks it as its Q6 since its cycle-3 repair, and
  D7's ledger now records its own probe of the failure). Whichever packet is applied first changes
  `vision.md`'s digest, so the other's anchor digest no longer matches and
  its anchors are a changed review subject (next bullet).
- **Line numbers move.** Whichever packet lands first shifts the other's
  anchors. D8's insertion points are defined by position (after the named
  bullet), and if an anchor's bytes have moved since the sha256 above, the
  changed anchor is a changed review subject: re-anchor through a fresh
  review (rule 10), never by applying judgment at the keyboard.
- `trust-and-evidence.md` is touched by D8 only.
- **D9, adopted 2026-10-06** (added 2026-10-14, round-2 note 12). D9
  replaced SEC-3 in `security.md` and one bullet of `v1.md`
  (`../../../decisions/DOCTRINE-AMENDMENT-LOG.md` line 12). D8 touches
  neither file, so no bytes overlap, and the three digests D8 cites are
  unchanged by it [Observed]. The thirteen doctrine readers added since
  `59fbf787` read `security.md` or `v1.md` only (ledger §4).
- **The non-governed narrative profile** (REQ-polaris-generation-032,
  adopted 2026-10-07; found while repairing, not in either raw). It names a
  *non-governed* subject, one with no kernel evidence drawer and no
  `openspec/**`, adopted capability declaration or declared topology in its
  admitted inventory. That is not (d1)'s observed-only project, which keeps
  a designated governance root; the two are different classes, and (d2)
  says nothing about where content about a non-governed subject would live
  [Inferred: from REQ-032's own definition; for round 3 to test].

## 9. How adoption would be recorded

Doctrine amendments carry no magic phrase (D3, D5, D6 precedent). For each
clause the owner adopts, in the owner's own words:

1. apply its insertion as the exact bytes shown, after re-checking the
   anchor's sha256 (for (d2), only after Q-A1 is answered);
2. add one `D8` row to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md` naming
   the clauses adopted and the owner's words;
3. regenerate every derived artifact `IMPACT-LEDGER.md` §4 names,
   including the context-budget report and its fixture anchors, add the
   adopted terms to the doctrine README glossary, and run the canonical
   battery. The glossary edit is not drafted and its battery effect is
   unprobed; at least one test reads that README's live bytes (ledger §4,
   repaired 2026-10-14, cycle 3, round-3 note 4).

A declined clause is recorded in the same row as declined. Register row
P-102 (added to `PENDING-OWNER-DECISIONS.md` on this packet's branch)
closes with the outcome. No arm edits this packet.
