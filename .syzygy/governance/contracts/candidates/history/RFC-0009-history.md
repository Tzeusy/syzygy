# RFC-0009 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is the
package at `../rfcs/RFC-0009/` (`README.md` index; modules
`semantic-geography.md` RFC9-1..23, `visual-grammar-and-lenses.md` RFC9-24..45,
`interaction-parity-and-release.md` RFC9-46..52). Full review corpus:
`_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0009-orrery-map-surface.md`.

Extracted `*(History: …)*` text is copied **verbatim**. Where a clause's
surrounding narrative was moved here rather than kept in the active module, it is
labelled *[moved narrative]*.

---

## §3 — clause-keyed amendment history

### RFC9-8(a)

*(History: added after review 8's ML-R15.)*

*[moved narrative]* The problem statement compacted out of the active clause:
"RFC9-15's terms include a **closed** relocation-trigger set (RFC9-16) whose only
reorganisation route is a layout version change, and layout versions are governed
artifacts under a *project's* `.syzygy/map/**` (RFC9-18). The portfolio is not a
project — SDR-29 and RFC3-21 put its arrangement in the **workspace manifest** —
so as written it inherited append-stability with no version registry, no
reorganisation event, no rationale record and no owner gate, and therefore **no
lawful way ever to re-lay it**. A workspace that grows to hundreds of projects one
append at a time reaches an unusable arrangement that an implementation can only
refuse to fix or fix unlawfully." Also compacted: the active clause's second limit
formerly read in full "and the portfolio's declared relations are profile
relations whose positional expression this RFC does not bind"; and the closing
attribution "[Inferred — the obligation was already binding; only its machinery
was missing, and the workspace manifest is where RFC 0003 already puts arrangement
concerns.]"

### RFC9-9

*(History: amended at acceptance by owner decision B12(a), which reversed the draft's
"proximity is inert beyond containment" position; read with **RFC9-9(a)**,
which adds a third **legend line** — residual adjacency, carries no meaning —
without adding a third reading)*

*(History: corrected after review 8's ML-N2 — this note still described the
question as surfaced and unanswered, which would route a reader who reached
§8 q7 into re-deciding a settled matter.)*

*[moved narrative]* Compacted from the active clause: the closing attribution
"the profile-relation limbs are Inferred as the legend-fidelity form of RFC1-26's
second sentence"; and, from the anti-conflation paragraph, "A portfolio view
drawing declared project intent in the same stroke as observed code coupling has
made a Desired-plane assertion look like an observation — the conflation
RFC1-25(b)'s twelve-pair invariant exists to prevent … reproduced one layer out,
at the place a reader actually sees it." Also compacted: the discharge
announcement "**The declared-dependency channel this RFC previously promised with
nothing to fill it is now backed by a real relation**; the foundation defect
reported at §5 defect 1 and the acceptance question at §8 q5 are **discharged by
A6**, and both are marked accordingly rather than left standing." The discharge
itself is retained in module 1's §Integration.

### RFC9-9(a)

*(History: added after review 8's ML-R3, which found the two-line form false as written.
The finding is recorded here rather than silently repaired, because the false
version read as the stricter and more honest one.)*

Verbatim, the mechanism correction the active clause now states compactly:

> *One correction to the finding's mechanism, which matters for RFC9-15(b) part 3.*
> The residue is not adjacency-by-**arrival order** — insertion order is never an
> input to any coordinate, and that clause stands. It is adjacency-by
> **baseline-delta**: "declared since the last full regeneration" is a shared
> property of a set of entities, computed from (declaration set, layout baseline)
> without reference to the order within it. Coarser than recency, deterministic,
> and reproducible — and still a basis for nearness that is neither of the two
> declared readings. The finding's conclusion therefore holds even though its
> mechanism is one step off, and the repair is the same.

*[moved narrative]* Also compacted: the earlier text "barred
'adjacency-by-recency' in the same breath as adjacency-by-observed-coupling. That
is not a bound this contract can keep"; and from part 2, "This is what makes the
third line honest rather than an escape hatch: a legend saying 'some proximity
means nothing and you cannot tell which' would be worse than the false two-line
legend it replaces." The attribution "[Inferred — the finding is review 8's
ML-R3; parts 1–4 are the drafter's repair …]" is retained in compacted form.

### RFC9-9(b)

*(History: added after review 8's ML-R5, which found the state asserted with no
epistemic class, no registry entry, no evidence path and no Unknown value —
i.e. rendered meaning outside the contract that governs all rendered meaning.)*

*[moved narrative]* Compacted: "[Inferred — review 8's ML-R5. The Unknown limb
and the backlog-exclusion are the parts a naive implementation gets wrong …]"

### RFC9-13(a)

*(History: added after review 8's ML-R12.)*

*[moved narrative]* The "why this is contract material" paragraph, compacted in
the active clause to one sentence: "Spatial memory is the entire stated
justification for the 3D mandate (RFC9-15), and a saved camera home is the one
artifact in this contract that **is** materialized spatial memory. The failure it
produces is RFC9-45's exact release signature — a reader stating something false
that the map supported ('Billing has collapsed', when the camera landed on Auth)
— reached through a lawful, announced, owner-gated act with nothing anywhere
marked wrong."

### RFC9-14(a)

*(History: added after review 8's ML-R1 and ML-N1; the earlier two-input form was
**false as written** — see RFC9-15(b).)*

*[moved narrative]* Compacted: "The third item is named explicitly because the
earlier wording said 'declared identity set, declared topology and placements',
which excludes edges — an implementer following it literally could never honor
RFC9-9 reading 2 at all." And: "Without it the model is over-determined and
non-reproducible: whether a `declared-dependency` edge is honored depends on
whether it was present at the last regeneration … [Inferred — the defect and this
repair are review 8's ML-R1; the owner's refresh model always implied a baseline,
and the earlier clause simply failed to name it.]"

### RFC9-15(b)

*(History: added at acceptance; owner-proposed model, superseding the layout tiebreak
that decision B12(a) would otherwise have required.)*

Part 3, verbatim:

> *(History: corrected after review 8's ML-R1. The clause previously named a **two**-input
> tuple, omitting the baseline; that form was **false**, and demonstrably so: parts 2
> and 3 are jointly non-vacuous only if a baseline input exists, since
> "regenerate some zones while others hold" is unexpressible in a function with
> nothing to hold from. The requirement was right; the input list was wrong,
> and the omission would have let two conforming renderings disagree on every
> coordinate.)*

Part 4's partition mandate: *(History: added after review 8's ML-R4.)*

The §8 q6 provenance note: *(History: rewritten after review 8's ML-R14; the earlier text
still read "nothing currently gates it," which contradicted RFC9-16(d) two
clauses above.)*

*[moved narrative]* Compacted from part 2: "reintroducing exactly the
path-dependence part 3 exists to remove". From the q6 note: "The drafted position
… was **routed to the owner and adopted** (decision A3), then narrowed after review
8's ML-R2 to the single carve-out RFC9-16(d) states."

### RFC9-16(d)

*(settled at acceptance by owner decision A3; narrowed by the same owner after review 8's
ML-R2 and ML-R7)*

The narrowness rationale, verbatim — compacted in the active clause to one
sentence:

> *Why the carve-out is this narrow.* [Inferred — review 8's ML-R2, whose failure
> case is recorded here because the earlier, looser form read as reasonable.] The
> clause previously required rendering **one** declaration set under both versions
> and comparing. But a layout version is not a claim about one declaration set; it
> is a function applied to every set the project will subsequently reach.
> Agreement on D says nothing about D ∪ {X}. A version that widens its spacing
> above eight districts agrees perfectly on a six-district project — the note is
> filed honestly, no governance act occurs — and then relocates every district on
> the ninth append, under trigger (a), with no reorganisation event, no rationale,
> and no owner act anywhere in the sequence. The narrow form closes that path at
> the cost of making most real layout changes gated, which is the correct side to
> err on for the property the whole 3D mandate rests on.

The RFC2-3 correction: *(History: corrected after review 8's ML-R7.)* — the active clause
retains the correction as a binding rule (a layout-equivalence check, not an
RFC2-3 identity test).

### RFC9-32

*[moved narrative]* Compacted from the chain-state bullet: "the overlay binds on
all of them regardless, so the V1 computation lands on a surface that already
renders its outcomes distinctly **rather than one being widened to accept them**."

### RFC9-35

*(History: minted as clause text at rev7 review 9, finding F9; previously stated only as §8
answer annotations to B12(c)/B17)*

### RFC9-39

*(RFC6-24's context — History: renamed from `Current` at the rev7 rework — directive
item B6, not owner decision B6)*

*[moved narrative]* Compacted: "and this scene selects no proposal set (which
would make it Proposed) and no superseded evaluation (which would make it
Historical): it compares the base graph at the selected evaluation against
declarations that are *already adopted*, i.e. against currently approved
intent"; "and a rendering that *did* move entities would by definition be an
analytical-plane or scenario switch and would have to be labelled as one";
"[Inferred — … surfaced because the scene's context was previously unstated.]"

### RFC9-41

*(History: rewritten at the rev7 rework: the original conditioned everything on a
then-pending doctrine amendment; D1 is adopted, and the two things the original
bundled — constitutional scope and concrete interaction design — are now stated
separately.)*

### RFC9-43

*[moved narrative]* Compacted: the second laundering example — "`asserted-by-worker`
is the same failure one label over: an aggregate disclosing 'Inferred ×8' without
disclosing that all eight are worker assertions with no retained artifact
(RFC2-25) has laundered the weakest tier the registry carries into an ordinary
Inferred count." And the cross-reference "RFC6-17 binds the same enumeration at
the foundation layer (§5, defect 4)". And, from the aggregate-channel paragraph,
"the composition panel honestly reports 'Unknown ×38' on expansion, and the reader
— who is reading the scene, not the panel — concludes the district is small."

### RFC9-45

*(History: separated at the rev7 rework, blocker A4: the original conflated the record of
the walkthrough, the judgment about it, and the authority that makes the judgment
gate a release.)*

Artifact 1: *(The screen-content list was added after review 8's ML-R10: a name and a
rationale make a false pass **attributable**, not **findable** — findability
requires knowing what was rendered. Without it, "was the misleading rendering
present at test time, or introduced by the version bump since?" has no answer.)*

Artifact 3: *(History: pinned at rev7 review 9, finding F2, matching RFC2-13's
undeclared-sweep posture)*

The fail-closed paragraph: *(History: added after review 8's ML-R11, which found the
clause defining what an unlawful verdict *is not* and never saying what the
release state then *is* — exploitable precisely in the direction with teeth, since
an unattributed **fail** would otherwise be no lawful fail at all.)*

### RFC9-46

*(Review 8's ML-R6 — the B12(a) amendment added exactly the class of surface-local,
reader-actionable field the maintenance note below predicts will be lost, and did
not add it here. The RFC had run its own predicted failure.)*

### RFC9-47

**Six layout obligations added at acceptance** — *(Review 8's ML-R9 — the
B12(a)/B12(b)/A3 amendments created checkable obligations and routed none of them
to the only list that gets tested. §4 case 3a already named four of them as
violation cases, which made the omission sharper, not softer.)*

*[moved narrative]* Compacted from the closing attribution: "That sentence has now
been demonstrated twice: once by review 8's ML-R9 finding six absences, and once
by ML-R6 finding the equivalence tuple short of two fields the gate then could not
see."

### RFC9-47(a)

*(History: added at the rev7 rework — directive item B4 of
`_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`, not owner decision B4:
the list above has already been caught incomplete twice, each time by an expensive
fresh-context review; a hand-maintained enumeration whose completeness is checked
only by luck is not a release gate, it is a hope.)*

### RFC9-52

*(History: added at the rev8 rework, directive item 7.)*

---

## §5 — foundation defects reported, with their trail

All five are discharged or resolved; none is outstanding and none blocks
acceptance. Retained here verbatim in substance for the trail.

**Defect 1 — RFC1-25 had no declared placement relation from Topology entry to
Capability. DISCHARGED at acceptance — owner decision A7.** RFC1-25 now carries
**`placed_in`** (Topology entry → Capability, Desired/declared, minted by a
governance artifact), added by owner amendment rather than by extending `part_of`
— whose own rule confines it to a single authority's hierarchy and directs
cross-authority nesting to a typed relation. The district/block hierarchy
(RFC9-4), SDR-22 placement, the shared-infrastructure district (RFC9-19(b)) and
every "components of capability C" aggregate now rest on a declared edge that
exists. RFC9-20's rule is unchanged and now enforceable. **§8 q1 answered.**

**Defect 1, second half — the same table had no declared dependency relation.
DISCHARGED AT ACCEPTANCE BY A6.** *(Marked after review 8's ML-R13, which found this half
still standing in the present tense and factually false about the amended kernel,
while RFC9-9 asserted it had been marked.)* `declared-dependency`
(Capability→Capability; Topology entry→Topology entry, Desired/declared) is now in
RFC1-25, recorded at RFC1-25(a). RFC9-9 reading 2, the honored/not-honored state
(RFC9-9(b)) and the RFC9-15(b) backlog all rest on it and are all buildable.
**§8 q5 answered.**

*As reported, and retained for the trail:* RFC9-9 requires dependency edges to
render on their own explicit, resolvable edge channel, but at V0 every dependency
edge RFC1-25 then offered was observed (`depends_on` code→code,
`structurally_related`) or execution-class, and RFC1-26 says relations outside the
table do not exist at V0. This RFC accordingly declined to legend any V0
dependency edge as "declared" (that conflation is what SDR-3 forbids) and declined
to mint the relation itself, routing the gap to acceptance (§8 q5) alongside the
placement relation, since both were the same closed-vocabulary omission. **That
restraint is unchanged and still binds** — carried into the active module 1
§Integration.

**Defect 2 — RFC6-22's equivalence enumeration omitted sibling surface states and
scenario context. RESOLVED UPSTREAM 2026-08-01.** As reported: RFC6-22 tested
label + tier + reason + freshness, but *dismissed by decision* and *unadopted
draft* travel per RFC6-14 and context must travel per RFC6-25, so as literally
defined the equivalence test would not have caught a scene/table disagreement on a
dismissal or a context swap. RFC 0006 has since folded both in. [Observed —
RFC6-22 as of 2026-08-01.]

**Defect 3 — RFC6-24's context taxonomy left the observed non-default snapshot
implicit. RESOLVED UPSTREAM 2026-08-01.** As reported: a branch/PR-tree evaluation
is technically "current at that evaluation," but nothing in RFC 0006 obliged
marking it non-default, and the reader-facing distinction between "the project
now" and "this branch's truth" carries real misreading risk. RFC6-24's base-context
bullet (the context then named `Current`, renamed `Base` at the rev7 rework) now
requires **every surface to carry an explicit non-default marker naming the
revision**. RFC9-38's marker is accordingly a surface-local restatement of an
upstream obligation, not one this RFC binds alone.

**Defect 4 — RFC6-17's aggregation disclosure was narrower than RFC6-22's
equivalence tuple over the same objects. RESOLVED UPSTREAM 2026-08-01.** As
reported: it required per-label and per-Unknown-reason counts only, so tier (any
of RFC2-25's six, `asserted-by-worker` and `reduced-fidelity` most
consequentially), freshness, and sibling surface states could all be dropped at
the moment elements merge into an aggregate — label laundering at the aggregate
layer, defeating doctrine's rule that staleness stays visible on the primary
surface. RFC6-17 now binds the full RFC6-22 equivalence tuple, which is exactly
what RFC9-43 binds for this surface. (This RFC caught the same pattern in RFC6-22
at defect 2 and had reproduced it one layer down in its own RFC9-43.)

**Defect 5 — RFC2-6's observation-record contents omitted the base layout.
RESOLVED UPSTREAM 2026-08-01.** As reported: RFC9-14 asserts the
declared-identity base layout is part of the deterministic observation record, and
doctrine names it inside the identity test — but RFC2-6's enumeration did not list
it, so an implementer building the record from RFC2-6 would never persist it and
RFC9-47's "two runs, one evaluation, identical base layout" gate would have no
recorded artifact to compare against, making the layout-determinism claim
untestable after the fact. RFC2-6's enumeration now carries "**the
declared-identity base layout**", with the identity-test reason stated inline.
This was a correction rather than a new decision, since doctrine already named it.

---

## §6 — Alternatives considered (moved wholesale)

Load-bearing residues are cited from the active clauses; the full set lives here.

- **One geography with lenses only (the research brief's frame), no analytical
  planes.** Rejected by SDR-21: real analytical questions (dependency distance,
  component architecture) genuinely want positional encoding; forbidding it
  everywhere pushes those views out of the product or, worse, into home geography
  by stealth. Two regimes with a hard masquerade boundary keep both honest.
- **Minted sticky home for undeclared shared components** (research §1.3).
  Rejected in favor of RFC9-20: SDR-22 refuses the forced single district, and a
  renderer-minted home — even sticky and visible — is a placement governance
  answer produced by an algorithm; the placement-undeclared aggregation renders
  the truth (nobody decided) and routes to the deciding act. *(Load-bearing for
  RFC9-20 and for open §8 q2, which asks the owner to confirm this choice.)*
- **Freezing height to one V0 meaning** (research FRC-6 recommendation). Rejected
  by SDR-24 ⚑: per-lens height with mandatory legend; the learnability bet is
  revisitable via amendment after comprehension walkthroughs, without breaking any
  truth rule. *(Load-bearing for RFC9-28.)*
- **Factory at V0 alongside City.** Rejected by SDR-19: Factory's honest inputs
  are largely SEC-3-gated; work state rides City as an overlay; shipping Factory
  early tempts synthesized motion, the sharpest fiction risk on this surface.
- **Repository as first-class partition.** Rejected by SDR-23: it re-anchors
  geography to a storage fact and relocates the map whenever code moves
  repositories.
- **Rendering unmapped code as individual buildings by default.** Rejected by
  SDR-25: overwhelming, and it renders unstable path-derived identities as stable
  places; aggregate-with-expansion is VIS-1's endorsed pattern. *(Load-bearing for
  RFC9-44.)*
- **Historical rendering now, amendment later.** Rejected at drafting: building it
  unconditionally would have treated a then-pending doctrine amendment as adopted.
  *(Outcome: the owner ratified that amendment as D1, so the constitutional scope
  is now unconditional — but the rejection's second half stands: the concrete
  interaction design still goes through its own approval, per RFC9-41 as
  rewritten.)*
- **Encoding provenance as a new RFC6-19 drawer content class** (RFC9-3). Rejected
  in favor of a surface-local "explain this encoding" affordance. The requirement
  — an encoding a reader cannot explain from evidence is the charter's named
  failure — is satisfied either way, but the kernel route costs doctrine: RFC6-18's
  one-fact-set invariant is fixed per (selection reference, evaluation identity,
  scenario context) with no lens dimension, so an eighth content class would either
  make the shared fact set vary with personal presentation state (VIS-6, exception
  (a); RFC6-7) or hand Polaris and Trajectory drawer fields about a surface they do
  not render. The surface-local affordance is the cheapest fix that costs no
  doctrine, and it stays evidence-derived because the channel registry it reads is
  itself a governed artifact (RFC9-26/18). Recorded here rather than discarded
  silently, since the alternative is the one a later RFC 0006 revision might
  prefer. *(Load-bearing for RFC9-3.)*

---

## §7 — Deliberately deferred (rev9 text, retained)

The active modules each carry a compact module-scoped deferral list; the rev9
statement in full:

> Rendering technology, layout algorithms and tuning, and concrete visual
> treatment values → post-acceptance spec/design-contract material (none may
> weaken a clause here). Performance budget *values* and the release-gate
> operating procedure → craft-and-care / quality policy. The analytical-plane
> catalog beyond the component/architecture analytical plane → map-surface specs,
> each analytical plane entering under RFC9-10. Interaction design, including the
> **form and cost** of the return-to-home affordance (RFC9-10(c) binds only that
> return is always available and discoverable, per B21; which action it is, how
> many steps it takes, and how it is placed and labelled, is not bound here) →
> craft-and-care. Lens metric formulas and band edges → per-lens spec + quality
> policy. Factory's full scene contract → its own later spec under RFC9-36/37's
> bound invariants. Historical-scene retention and renderable-evaluation selection
> → quality/evidence policy, active only under RFC9-41. Modelled interiors below
> source/test evidence → post-V0 elaboration, no promise made. V1 gap-object
> rendering on the map → V1 RFC, over the same identities.

---

## §8 — Owner questions: full text and answers

Numbering is stable. Open items keep their full text in the owning module; the
nine answered items are here.

**q1. The placement relation (Integration defect 1).** Amend RFC 0001 to carry a
declared topology-entry→capability placement edge (extend `part_of` vs a new
`placed_in`), or rule that district membership is derived solely from
implementation mappings' capability edges (leaving component blocks unplaced when
mappings are absent)? This RFC assumes the declared edge; the map cannot render
its L4 level without an answer.

> **ANSWERED at acceptance — A7.** `placed_in` (Topology entry → Capability,
> Desired/declared) added to RFC1-25 by owner amendment rather than by extending
> `part_of`. Integration defect 1 discharged.

**q2. Undeclared shared-component placement (RFC9-20).** — **OPEN.** Full text
retained in the active module (`semantic-geography.md` §10).

**q3. Historical conditionality (RFC9-41).** Accept the dormant-clause design, or
adopt the amendment packet at the same gate so the clause activates with
acceptance? Adopting together avoids a second ruling; keeping them separate keeps
doctrine amendment visibly distinct from RFC acceptance (VIS-4).

> **ANSWERED at acceptance — D1, in part.** The doctrine amendment making `map/`
> include historical state **is adopted**, so the dormant clause's premise holds.
> The historical *design* — ghost-step opacity, milestone scenes, scrubber — is
> **held behind its own review** and does not go live on this adoption.

**q4. Analytical-plane governance (RFC9-10/18).** May an owner promote a personal
analytical-plane definition into a named, governed analytical plane under
`.syzygy/map/**` (shareable, versioned, still marker-bound), or do all
analytical-plane definitions ship product-defined at V0? Proposed: promotion
permitted — it is a governance act like any promotion (VIS-6), and the masquerade
boundary does not depend on who authored the analytical plane.

> **ANSWERED at acceptance — B12(c)/B17.** One rule for lenses, analytical planes
> and profile relations alike: personal definition and use is free; **promotion**
> to a named, governed, versioned artifact is an owner governance act under
> RFC3-16(a).

**q5. The declared dependency relation (Integration defect 1, second half).**
RFC9-9 requires dependency edges to render on their own explicit, resolvable
channel, but RFC1-25 offered only *observed* and execution-class dependency edges
at V0. Amend RFC 0001 to carry a declared dependency relation between capabilities
and/or topology entries, or rule that V0 renders observed and execution dependency
edges only — legended as what they are, with no "declared" dependency channel
until the vocabulary carries one? This RFC took the second position provisionally.
**The question is intra-project only.** At project scope the portfolio profile
already supplies a declared relation (`depends-on`, RFC3-14) under RFC1-26's
second limb, and RFC9-9 legends it as a profile relation; answering this question
either way changes nothing there. RFC 0001 §8 q6 puts the adjacent and distinct
question — whether a declared dependency relation belongs in the *kernel*
vocabulary at all, or stays a profile relation — and the two should be read
together.

> **ANSWERED at acceptance — A6.** `declared-dependency` minted in RFC1-25.
> Integration defect 1's second half discharged; the declared-dependency channel
> is now backed by a relation that exists.

**Open follow-on recorded at the rev10 compaction.** The rev10 RFC-0001 pass
established that A6 closed the *kernel-minting* half of RFC-0001 §8 q6 but did
**not** address the part that question also raised: whether **RFC9-9's legend and
edge-channel rules need a pass now that a kernel-level declared dependency
relation exists** — whether the three-class edge taxonomy and the profile-relation
limb are still correctly divided, and beneath it *who may add a profile relation
and under what gate*. This is owner-scoped and its home is RFC1-7/RFC1-26; **no
normative change was made on the rev10 pass**. It is carried as a visible open
item in `semantic-geography.md` §10 and listed in the package README for the
open-question triage. The surface is safe under either answer meanwhile: an
unregistered profile relation fails closed under RFC9-26 and never reaches a
reader as an unlegended edge.

**q6. Is a layout-version change an owner-gated governance act (RFC9-16(d),
RFC9-18)?** The technical bounds are bound regardless: a recorded rationale naming
what the change buys and what it moves, and reservation policy unbounded in
principle so ordinary growth never forces a bump. The open question is the
**gate**. RFC3-18 binds the namespace class and confers no adoption gate, and
VIS-4's shape-level sign-off list does not name layout — so making the bump an
owner act extends that list, which is the owner's call. Drafted position:
**owner-gated**, because the bumper is Syzygy (an agent), the act relocates every
declared entity on every governed project, and append-stability — the property the
whole 3D mandate rests on — is otherwise defeasible at an agent's discretion.

> **ANSWERED at acceptance — A3, narrowed after review 8.** Owner-gated governance
> act with recorded rationale, **except** where the two versions are demonstrated
> to be the **same placement function** — agreement on every layout input tuple,
> not on one declaration set — which needs only a recorded note. The demonstration
> is a **layout-equivalence check**, not the RFC2-3 identity test (RFC2-3 is
> intra-evaluation and says nothing about comparing two layout versions; the
> earlier citation here was wrong, ML-R7). An asserted exemption is not a
> carve-out. See RFC9-16(d).

**q7. Does proximity in home geography carry any declared meaning beyond
containment (RFC9-9/RFC9-4)?** This RFC bound "proximity encodes declared
containment and nothing else; it never encodes a measurement". The alternative the
owner had not been asked about is richer: adjacency also expressing **declared
topology nesting**. SDR-21 requires home to be stable, capability-oriented,
reproducible and append-stable — it does not require proximity to be meaningless,
so the narrower rule foreclosed a family of home layouts by prose rather than by
ruling. Either answer keeps the measurement prohibition intact.

> **ANSWERED at acceptance — B12(a), reversing the drafted position.** Proximity
> carries **two** declared readings: containment (RFC9-4) and **declared
> relatedness** via `declared-dependency`. It never encodes a measurement, and
> undeclared *inputs* to placement stay barred. Reading 2 is best-effort; its
> shortfall renders **not-honored**, on a registered channel with its own Unknown
> value (RFC9-9(b)). Review 8 (ML-R3) then established that the legend needs a
> **third** line — *residual adjacency, carries no meaning* — because
> append-into-free-space produces nearness on a basis that is neither reading, and
> a two-line legend would be false for most adjacency on screen. See RFC9-9,
> RFC9-9(a), RFC9-9(b) and RFC9-15(b).

**q8. Is the comprehension test a release gate (RFC9-45)?** This RFC makes "a
reader stating something false that the map supported" a release-blocking
trust-floor incident. v1.md frames the comprehension test as an owner-judged
**success** test, re-judged at stage gates and explicitly "never rendered
Observed". Converting it into a release gate is defensible — a reader misled by
the map *is* a trust-floor breach — but it hands a release veto to a subjective
walkthrough outcome, and the escalation had not been ruled.

> **ANSWERED at acceptance — B12(b).** Yes, a release gate — **with attributed
> judgment**: every pass or fail names the judging party and records its
> rationale. The verdict is never rendered Observed. *(Rev7 rework, directive item
> A4 — not owner decision A4: the gate's structure is now three artifacts —
> kernel-recorded execution record in `records/`, attributed judgment in
> `decisions/`, and the owner-approved release policy in `policies/` that alone
> confers release authority.)*

**q9. Who may adopt a lens (RFC9-32/35)?** RFC9-35 calls adding a lens "a contract
act" without naming whose act it is, and q4 asks only about governed analytical
planes. Lenses bind **height** — the channel SDR-24 deliberately left unfrozen —
so lens adoption authority determines who may change what height means.
Product-defined only at V0; owner-promotable like analytical planes; or a distinct
authority? **Answer this for extension profiles generally, not for lenses alone.**
The same authority question arises three times in this RFC — lens adoption here,
analytical-plane promotion at q4, and **who may add a profile *relation***
(RFC9-9's profile-relation rule; RFC1-7, RFC1-26's second limb). All three add
vocabulary that changes what a rendered encoding *means*, which is the third limb
of RFC3-16(a)'s predicate. Answering two of the three and leaving the third to be
settled by whoever first needs it is the asymmetry this section exists to avoid.
*(The surface is safe under either answer meanwhile: an unregistered profile
relation fails closed under RFC9-26. The home of the general rule is
RFC1-7/RFC1-26, not this clause.)*

> **ANSWERED at acceptance — B12(c)/B17**, with q4 and the profile-relation limb.
> Same single rule.

**q10. Does the return-to-home bound stay "one action" (RFC9-10(c); SDR-21)?**
SDR-21's ratified wording is that analytical planes are "always legended, visibly
temporary, **one action back to home**". A draft of RFC9-10(c) had restated this
as "always available and discoverable"; the restatement was reverted, because a
contract clause may not narrow ratified text by prose. **For relaxing:** the
truth-bearing obligation really is that the reader is never stranded outside home,
and interaction cost really is craft-and-care material — this RFC defers every
other interaction cost, and "one action" reaches into affordance design in a way
no other clause here does. **Against:** SDR-21 is ratified text, and "one action"
is a **testable bound** — a release check can count actions — where "available and
discoverable" is a judgement no gate can run, so the relaxation converts a
checkable obligation into an unfalsifiable one on the surface whose whole contract
is checkability.

> **ANSWERED at acceptance — B21, granting the relaxation.** The obligation is
> that the reader is never stranded outside home; the return affordance is "always
> available and discoverable" rather than a counted action bound. CC-VIZ-5 has
> been amended to match, so no artifact is left carrying the stricter form. The
> owner accepted the stated cost: a checkable bound becomes a judged one on the
> surface whose contract is checkability, and no release gate can count actions
> any more. See RFC9-10(c) and CC-VIZ-5.

---

## Compaction note (rev10)

The rev9 monolith carried a §0 "Reader's summary" and a §2 "Motivation and
doctrine grounding". Both were non-normative; their substance is distributed to
the package README's reader map and to each module's §0, and the doctrine
grounding's [Inferred] thesis is carried in compacted form in the README's reader
map; its verbatim rev9 text is preserved here:

> The failure this contract guards against is **spectacle displacing truth**:
> spatial rendering is the product's most seductive surface and its cheapest place
> to lie — a synthesized flow, a green district with no evidence, a layout that
> quietly reshuffles, a proposed structure rendered solid. Every clause below
> makes one of those lies a recognizable violation rather than an aesthetic
> choice.

The rev9 §2 [Observed] grounding, retained here in full: the constitutional
requirement is a spatial comprehension surface anchored to **capability
identities, not file paths** — refactoring must not randomly relocate the map,
layout must be reproducible from the same snapshot, exact 2D/tabular equivalents
always available [Observed: architecture.md, "One kernel, three surfaces"]. V0
realizes it in 3D at coarse granularity, capability identities from the project's
own declared artifacts, and **a predominantly-Unknown map on an undeclared
project is the correct output, not a defect** [Observed: v1.md]. The trust floor
makes every visual encoding mean exactly what its legend says and every rendered
map entity resolve to its identified target [Observed: trust-and-evidence.md,
floor]. The charter's anti-thesis names the recognizable failures: a decorative 3D
file tree, a single-metric software city, an unstable layout, a scene whose
encodings cannot be explained from evidence [Observed: SDR §2].
