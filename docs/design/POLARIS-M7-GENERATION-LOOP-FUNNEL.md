# Feature request M7 — Close the generation loop: observation-typed sources, structural independence, a self-corpus proof, a route, an exit and a named egress act

> **Candidate — binds nothing.** Bead `syzygy-dov.7`, move M7 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`),
> written in the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its
> six siblings. Planning only: nothing here authorizes implementation, and this
> packet rules no slice authorized or unauthorized. A *lawful arm* below names
> an arm the owner may take, never a ruling that a slice is authorized. The
> owner disposes (VIS-4).

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slice 5) / **medium** (slices 2, 3 and 6) / **large** (slices
1 and 4).

Baseline: Syzygy `a9f671e` (main). The subject is the generation pipeline
package, its app-side demo and preview, and the one route table that would
have to carry a draft — not the rendered Polaris page.

**This packet sits on the same surface as M6 (PR #40, P-73) and does not
pretend otherwise.** Eleven of M6's cited implementation files are inside M7's
own candidate surface (Collision and sequencing, computed below). Every M7
slice names the M6 slice it sequences behind and the P-73 ruling that gates
it. No question P-73 already carries is re-asked here.

## The five questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1 is the packet's central question — it decides whether
the generator can ever satisfy the anchor clause its own specification names.
Q2 and Q3 are independent of it; Q4 and Q5 each gate exactly one slice.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Does the observer registry's `git-tree-entry` source identity satisfy RFC7-10's closed anchor classes, or does citing a project source file need a sixth class?** The effective REQ-polaris-generation-003 requires, verbatim at `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md` line 98 (REQ-003 is not one of the seven the understanding amendment touched, so the predecessor is the effective text): "Source anchors SHALL use the closed classes and durable revision/evaluation-bound identities required by RFC7-10, not labels or paths as identity." RFC7-10 (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` lines 204–213, quoted whole in Gate 5) closes the target class at **five**: a kernel entity reference; a doctrine rule or accepted-contract citation; an `openspec/**` anchor; a decision or policy identifier; or an evidence artifact identifier with integrity digest. What is **[Observed]** here is the clause and its five classes, read at source this session and enumerated: RFC7-10 names five target classes and names **no** class for a file inside an observed repository. That such a file therefore falls outside all five is **[Inferred]** — it is precisely the reading Q1 asks the owner to make, and this packet's own recommended arm is that it falls *inside* the fifth. [Superseded 2026-09-15, review 1 F6: this read "A file inside an observed project is **none of those five** [Observed, the clause read at source this session and its five classes enumerated]" — an [Observed] label on the negative standing beside a recommendation for the positive. Per AGENTS.md §Epistemic and change discipline, an LLM assertion is Inferred.] What the PWB observer actually issues is a sixth thing: the adopted registry entry declares an input class `git-tree-entry` whose `identityScheme` is `repository-id-plus-revision-plus-repository-relative-path-plus-object-id` (`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` line **54**, inside the object whose `"class": "git-tree-entry"` is on line 53; the literal `git-tree-entry` occurs **1** time across every tracked file under `.syzygy/` and `openspec/`, at line 53, **at `a9f671e`**; at this commit it occurs **3** times over the same 619 tracked files, the two additions being this packet's own P-76 register blockquote and row) [anchor corrected 2026-09-15, review 1 F10.1; it read "line 53" for the `identityScheme`. Commit anchor added 2026-09-15, review 2 G5(a): the clause read "the literal `git-tree-entry` occurs **1** time across every tracked file under `.syzygy/` and `openspec/`, at line 53)" with no commit anchor, and this packet's own register commit falsified it] [Observed, literal sweep re-run 2026-09-15 at both revisions with Python `re`, denominator the 619 tracked files under the two governed trees at each]. That entry is act-bound twice over — `PWB-OBSERVER-REGISTRY-ENTRY-ACT.md` and `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` both name it as their artifact identity — so slice 1 reads it and may never edit it. | **Rule that `git-tree-entry` is admitted as RFC7-10's fifth class — "an evidence artifact identifier with integrity digest" — for the generator's source anchors, and say so in a recorded ruling rather than leaving it to the implementation.** The object id *is* the integrity digest, the revision *is* the target state RFC7-10 demands, and the scheme is durable and path-free in exactly the sense the clause's closing sentence requires ("Anchors embed durable identifiers, never labels, paths, or coordinates"). **The counter-argument, which this packet does not resolve:** RFC7-10's fifth class reads naturally as *Syzygy's own* evidence artifacts (the class `docs/evidence/**` records belong to), and the clause says in terms "No target class exists for narrative content, renderings, or editorial drafts" — a deliberately closed list. Reading a sixth kind of target into the fifth class is a widening of an accepted contract, and RFC acceptance is VIS-4's always-human-gated shape-defining class. **Second lawful arm:** amend RFC-0007 to name the class, through the normative-change workflow and a new owner act — slower, and it re-opens an accepted contract. **Third lawful arm:** build slice 1's richer source type without claiming RFC7-10 conformance, and record the clause as unsatisfied — honest, and it leaves the specification's own anchor obligation open. **Default if unanswered: the third arm** — slice 1 ships the identity fields and records REQ-003's anchor sentence as **unsatisfied**, rather than asserting a conformance the owner has not ruled. **Review 1 named a fourth lawful arm this row does not offer — rule RFC7-10 not engaged — and observed that Q1's default is the only one of the five that ships rather than holds; both are carried unapplied in "Review 1 and repairs (2026-09-15)" below and in the P-76 register row, because adding or re-weighting an arm changes what is put to the owner and is the owner's own reading to make [clause added 2026-09-15, review 2 G16; the arm is deliberately **not** folded into this table]. |
| Q2 | **Is running the generator over Syzygy's own governed corpus a "real-project read" the implementation act reserves, or the observing project reading its own tree?** `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 42 reserves, verbatim: "Real-project reads, provider egress and destination writes remain separately admitted; no effect, production release, broad remote access or observed-project code execution is authorized by this act." `EXECUTION-PHASES.md` lines **13–14** say Phase A's operator seam "does not create or mutate live scheduler items, call a real provider, serve owner effect controls, or read **another** project" — the sentence begins on line 13 and only its second half is on 14 (emphasis this packet's, marked as added) [anchor corrected 2026-09-15, review 1 F10.2; it read "line 14"]. Syzygy is not another project; it is the observing one, and its own tree is already read by every script in the battery. But the act's reservation does not say "another project" — it says "real-project reads", and Syzygy is a real project. Measured this session **at `a9f671e`**, the corpus slice 3 would use is **105 files / 1,266,454 bytes / 1,258,724 characters** (the six doctrine files, the 71 tracked `.md` files under `.syzygy/governance/decisions/` at every level — 67 at the top level and four under `launch-gate/` — and the 28 accepted RFC modules, the `.md` files one directory below `.syzygy/governance/contracts/rfcs/`. The two accepted RFCs that are single files rather than directories, `RFC-0001-project-graph-identity-state-planes.md` and `RFC-0006-cross-surface-selection-query-drawer.md`, are **out of scope** of that predicate, and the slice's own corpus builder must say so: including them gives 107 files / 1,369,266 bytes / 1,360,678 characters / 0 over the cap / largest 63,903 [Observed, both predicates run 2026-09-15]), **0** of them over the landed per-source 100,000-character cap, the largest 55,836 characters [Observed, counted this session and re-derived 2026-09-15; predicate and denominator in the evidence record. Commit anchor added 2026-09-15, review 2 G5(b): the corpus includes `.syzygy/governance/decisions/`, so this packet's own P-76 register row moved the byte and character figures — at this commit the same predicate gives 105 files / 1,277,862 bytes / 1,270,122 characters, with the file count, the cap result and the largest source unchanged, and every future decision row will move them again [Observed, the predicate run at both revisions 2026-09-15 from `git ls-tree` blobs, denominator the 105 files at each]. Superseded 2026-09-15, review 1 F2: the parenthesis read "the 71 top-level `.md` files under `.syzygy/governance/decisions/`" — the 71 is the count at every level, and read strictly as *top-level* the predicate gives 67 and a 101-file corpus, so both halves of it were wrong. The six published figures re-derive exactly under the corrected wording]. | **Rule it the observing project reading its own tree: no new consent record, no registry entry, no act — with the ruling recorded, because the sentence above can be read the other way.** The read adds no capability the repository does not already exercise; the PWB body-read-authority gate exists to protect an *observed* repository from the observer, and Syzygy is on the other side of that gate. **Counter-argument, and it is not weak:** the generator is the thing that will one day send this material to a provider, and giving it a reader over Syzygy's own governance corpus builds the pipe before the egress act exists — the discipline the reservation protects is precisely that a read path and an egress path are admitted separately. **Second lawful arm:** require a narrow owner direction naming the self-corpus read, its file set and its no-egress condition, in the shape of `POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md`. **Default if unanswered: slice 3 does not ship.** Slices 1, 2, 5 and 6 are unaffected. |
| Q3 | **Slice 4 would add `GET /polaris/draft/<runId>` behind the machine credential. P-72's recommended category does not reach it. Extend that category, mint a second one, or serve no route?** M5's Q1 (P-72, on `agent/syzygy-dov.5` at `ba9ca61`) recommends a PWB semantic delta naming a closed category, "derived read-only machine view", defined as "composed only of fields already reachable from `/api/poc` at the same evaluation, independently oracle-verified as derivable, served under its own declared, digest-bound response ceiling", and placing `/api/poc/polaris` retroactively and `/api/poc/briefing` prospectively under it [Observed, read at source in that worktree this session]. A generation draft is **not** reachable from `/api/poc`: the two planes are disjoint, `0` references to `three-surface-poc-core`, `PocModel` or `projectShape` across the **20 tracked files** of `packages/polaris-generation-core` and `apps/three-surface-poc/src/polaris-generation` [Observed, re-run 2026-09-15 over that denominator and over the 17-file `src`-only set; **0** on both. Superseded 2026-09-15, review 1 F1: this read "across the 20 files of the generation package and the app's generation directory"]. So slice 4's route fails P-72's own membership test by construction. | **Do not open a competing question: fold slice 4 into P-72 as a second declared category in the same delta — "generated editorial draft view" — with its own `ResponseLimitIdentity` and its own registry ceiling, and rule it together with Q1 and Q2 of P-72 rather than separately.** One delta, two categories, one act; the alternative is two amendments to the same signed specification weeks apart. **Counter-argument:** P-72 is itself unruled, so folding makes slice 4 wait on a decision it cannot influence, and an owner who takes P-72's arm (c) — serve the briefing on the existing `/api/poc` with a selector — has no corresponding arm here, because a draft cannot be a selector over a body it shares no fields with. **Second lawful arm:** serve no route; keep the preview a file the operator opens, as `pipeline-demo-main.ts` writes it today, and take slice 4's owner control as a separate later move. **Default if unanswered: the second arm** — slice 4's route does not ship; the drafted-act packet limb of slice 4 is independent and is governed by Q4. |
| Q4 | **Slice 4's drafted act is an RFC7-21 per-block authorship act over Syzygy's own draft. Does it ride P-71's Q3 ruling, or is it a different subject?** M4's Q3 (P-71, on `agent/syzygy-dov.4` at `63b8e33`) asks whether Syzygy may emit a drafted owner-act packet and into whose tree, and recommends arm (a) — into Syzygy's own `.syzygy/governance/decisions/`, marked draft, under a fresh narrow direction — while recording that arm (b), a pure drafter that emits packet *data* and writes no file, needs no act [Observed, read at source in that worktree this session]. P-71's subject is a drafted act about the **observed** project's gaps. M7's is different: the effective REQ-polaris-generation-010 (base line 528, unamended) says a generated bundle "SHALL remain editorial-draft until the existing effective-owner-act predicate under RFC3-16 and RFC7-21 admits an attributed per-block authorship act for its exact subject", and RFC7-21 (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` lines 398–406) requires the adopter to attest **per claim block**. The subject is Syzygy's own narrative about a project, not a finding about Butlers. | **Take P-71's arm (b) for slice 4 — a pure drafter that returns the packet as data, writing no file — and let P-71's arm (a) govern the file-writing limb if and when the owner grants it.** Arm (b) needs no act on anyone's reading, is fully testable with no filesystem, and produces exactly the artifact RFC7-21 demands the owner sign. It also keeps one packet writer rather than two, which is what the dossier asks for. **Counter-argument:** a packet the owner must copy out of a JSON body by hand is a worse owner experience than a file, and REQ-020's "without manually assembling governance or scheduler records" is the clause slice 4 exists to serve; arm (b) satisfies the letter and strains the intent. **Second lawful arm:** wait for P-71's ruling and take whichever arm it takes, building nothing until then. **Default if unanswered: arm (b)** — the drafter is built pure and writes nothing. |
| Q5 | **Slice 6 would replace the admit port's "an already-dispatched identity MUST refuse" with reserve/complete, so a completed attempt returns its recorded artifact instead of refusing. Implementation of REQ-008, or a change to a reviewed effect-boundary safety property?** The landed contract sentence is a comment on the port declaration, `packages/polaris-generation-core/src/pipeline.ts` lines 60–64, and `packages/polaris-generation-core/src/pipeline.test.ts` lines 73–76 pin the behaviour: re-running the same request returns `admission-refused` after exactly **5** stage sends. The effective REQ-polaris-generation-008 (base line 400, unamended) asks for something narrower than the comment: "Duplicate starts for the same request identity SHALL not duplicate provider effects or spend the same allowance", and its approved scenario **"Resume valid work"** (base lines 407–411) requires that "resume reuses those stages and records which work was reused and newly dispatched". A port that refuses a completed identity cannot satisfy that scenario. | **Rule it an implementation of REQ-008, on the condition that the replay prohibition is retained unchanged for in-flight and uncertain identities.** The requirement and its scenario name the behaviour; the comment is stricter than the clause it implements, and `EXECUTION-PHASES.md` line 18 puts 008 inside Phase A's own requirement set. **Counter-argument:** the sentence is a reviewed safety property at the one boundary where a mistake spends real money and real provider effects, its stricter reading is the conservative one, and `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json` records a digest over exactly these bytes — editing them retires that record's binding (verification rule 10 applied to an evidence record). **Second lawful arm:** leave `admit` alone and implement resume as a caller-side artifact cache outside the port, which changes no reviewed sentence and leaves the port's own contract mismatched with REQ-008's scenario — a mismatch the bead would then have to record. **Default if unanswered: the second arm**, and this packet records that REQ-008's "Resume valid work" scenario stays unimplemented. |

### Decided in this packet, not put to the owner

**The dossier's "prerequisite: none for independence, typing, self-corpus
proof and the route; owner act for any egress" survives, with two
corrections.** The dossier's machine record gives M7 a `prerequisite` value of
`none; owner act for egress` [Observed, read from
`docs/pursuits/2026-09-13-vision-pursuit-data.json` this session]. It holds in
the sense the dossier meant it — no doctrine amendment, no spec amendment and
no owner act is needed to *file* any of the six slices, because every clause
they rest on is predecessor text already inside the implementation act's named
requirement set (Gate 3's act table, with the per-slice sweep). The two
corrections are: (a) **the route is not prerequisite-free** — it is a new
machine-credentialed route, which is exactly what M5's Q1 put to the owner as
a spec-delta question, so slice 4 carries a prerequisite the dossier's line
does not name (Q3); and (b) "owner act for any egress" is right but
understates — **slice 3 itself may need a ruling before any egress question
arises** (Q2), because its read is of a real project's governed corpus even
though that project is Syzygy.

**Every M7 clause is predecessor text; none is overlay-only.** This is the
respect in which M7 differs from M6. Swept this session with Python `re` over
both specification files, denominator the two files: REQ-003's anchor sentence
occurs 1× in the predecessor (line 98) and 0× in the overlay; REQ-006's
"Reviewers SHALL receive the artifact, governing references and acceptance
criteria without the authoring conversation" and "The candidate-authoring
stage SHALL NOT define or narrow its own review denominator" occur 1× in each
file (base 302, overlay 180); REQ-014's two-project and synthetic-evidence
sentences occur 1× in each (base 755, overlay 367); REQ-010's editorial-draft
sentence 1× / 0× (base 528); REQ-020's guided-start sentence 1× / 0× (base
1083); REQ-008's resume and duplicate-start sentences 1× / 0× (base 400)
[Observed, all ten sentences swept this session]. So the arm of P-73's Q6 that
gates M6's slice 4 — work scheduled solely from clauses the amendment added —
**reaches no M7 slice**. M7 inherits M6's *file* collisions, not its authority
question.

**Slice 2's "fidelity envelope built from the draft alone" is wrong and is
corrected here.** The dossier's Slices bullet says the fidelity envelope
should be "built from the draft alone". The effective
REQ-polaris-generation-006 (overlay line 180) requires the opposite in two
sentences: fidelity review "SHALL use an independently prepared, frozen
inventory … covering the entire admitted source population", and "The fidelity
reviewer SHALL verify inventory accuracy and completeness against the owning
admitted sources rather than trusting preparation output." A reviewer holding
only the draft can do neither. L3-M4's own *what* field says the right thing —
`{sources, inventory, draft, acceptanceCriteria}` — and this packet builds to
that, not to the Slices bullet.

**`readerQuestions` stay in the fidelity envelope; `plan` is removed.** This
is the one judgment inside slice 2 that could get independence wrong in either
direction, and it is decided here rather than asked, because the clause
settles it. REQ-006 names what a reviewer receives: "the artifact, governing
references and acceptance criteria without the authoring conversation". The
plan is the authoring conversation — it carries each section's self-declared
`reason` — and goes. Reader questions are acceptance criteria: the same
requirement obliges the workflow to "prepare or validate the independent
inventory and questions from admitted sources", which makes them a prepared
input to review, not an authored argument [Inferred — a reading of which side
of that sentence `readerQuestions` falls on; the measurement that they are in
the envelope today is Observed].

**Slice 3 is portability evidence, not the second project, and the packet says
so in the artifact it writes.** L3-M6 proposes publishing the self-corpus
draft "as the second project". The effective REQ-polaris-generation-014's own
scenario **"Narrow evidence offered as completion"** (overlay lines 380–384)
forecloses that: "**WHEN** only synthetic provider runs, a Butlers-specific
page or unchanged golden artifacts are available / **THEN** the completion
report marks real generation, regeneration and reader-quality requirements
unproven / **AND** no test score or successful provider response is
substituted for that missing evidence." A scripted responder is a synthetic
provider run. What slice 3 buys is real: real path shapes, a real source
count, a real contradiction population, and the budget and cap behaviour at
1.26 MB of input — the things a fixture cannot show. What it does not buy is
task 3.3. The slice's own evidence record must say that in those words.

**Slice 6's third limb — the drift band — is deferred, not dropped.** L3-M8
has three limbs: (a) stage-scoped inputs, (b) reserve/complete resume, and (c)
a rendered drift band binding each published manifesto to its `snapshotId`.
The dossier's What bullet and Slices list both carry only (a) and (b)
[Observed, read at source this session]. Limb (c) is a rendering change on a
page no generated manifesto reaches yet, and the dossier itself routes its
retained-evaluation store to M12 (L2-M6). It is carried below as deferred
slice 7 with its mapping done, so the gap is recorded rather than lost.

**Running slice 3 at the full corpus rather than a trimmed one is a stated
decision, not a question.** L3-M6's own slice plan says to "record the budget
and cap breaches honestly as findings rather than tuning the fixture until it
fits", and that is what the bead should do. The cost is one long local run and
no provider call; a delegate can make it.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `.syzygy/governance/doctrine/security.md` | VIS-1, VIS-2, VIS-4, VIS-5; SEC-2 |
| Decisions | `.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`, `POLARIS-GENERATOR-APPLICABILITY-ACT.md`, `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`, `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`, `PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`, `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` | the third is the implementation grant quoted in Q2 and Gate 3; the last two bind the registry entry Q1 reads |
| Specification | `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md` composed with `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md` | effective composition **31 requirements and 177 scenarios** per the understanding act's Scope paragraph |
| Package contracts | `SCHEMA-CONTRACT.md`, `SOURCE-POLICY.md`, `EXECUTION-PHASES.md`, `INTERFACES.md`, `tasks.md`, all under `openspec/changes/polaris-manifesto-generation/` | each is a digest row of the generator package's scope record (`docs/evidence/polaris-generator-current-scope-2026-09-12.json`, **21** rows, **all 21** under that one directory, **0** an implementation path) [Observed, enumerated this session]. The acts bind an immutable offer by its own SHA-256, not this record; the record is cited here as the enumeration of the package's governed files, never as the act's argument |
| Contracts | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`, `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` | RFC7-10's five anchor classes (Q1); RFC7-21's per-block adoption gate (Q4); RFC2-26's OpenSpec-seam phase rule, run in Gate 5 |
| Policies | `.syzygy/governance/contracts/candidates/policy-candidates/` (CC-SPEC, CC-IMPACT, in force despite the directory name) | CC-REV-2 is the amendment path Q1's second arm would need |
| Sibling packets | `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` on main; M2–M6 and lane B read-only in sibling worktrees | P-72 governs slice 4's route (Q3); P-71 governs slice 4's packet writer (Q4); P-73 sequences slices 1, 2 and 6 |

**How the specification composes.** AGENTS.md records the rule: generator
requirement lookup composes the original change with the explicit
understanding-amendment overlay. The understanding act's Scope paragraph is
the authority for which side wins: "REQ-polaris-generation-002, 004, 006, 009,
012, 014 and 019 take their full amended clauses and preserved scenarios; 030
and 031 are added. The other 22 predecessor requirements remain unchanged." Of
the six requirements this packet relies on, two (006 and 014) are in that list
and are cited at the overlay with the predecessor line given beside them; four
(003, 008, 010 and 020) are not, so the predecessor is the effective text.

**What the understanding act does not grant, and why it does not bite here.**
`POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` lines 39–41 read,
verbatim: "Revocation relationship: none. Existing implementation and
applicability acts retain their own exact scopes. This act grants no
implementation extension, source/provider/content permission, write consent,
deployment or release." That sentence is load-bearing for M6's slice 4, whose
requirement clause is text the amendment added. It reaches **no** M7 slice:
every clause below is predecessor text carried through unchanged, swept this
session over both files (the ten-sentence sweep above) [Observed for the
sweep; the consequence — that the slices are therefore covered on either
reading of the sentence — is [Inferred], the same reading P-73's Q6 declines
to settle].

**Three bound-byte constraints this packet obeys.** (a) Every file in the Gate
0 "Package contracts" row is a digest row of that scope record, and **no slice
proposes editing one**; all 21 rows are under
`openspec/changes/polaris-manifesto-generation/` and **0** are implementation
paths [Observed, enumerated this session]. (b) The observer registry entry Q1
reads is the artifact identity of two performed acts; slice 1 reads its
declared identity scheme and edits nothing. (c) All **15** paths named in
Gate 3's topology table — the ten inside the generation surface plus
`PROJECT-STATUS.md`,
`packages/three-surface-poc-core/src/project-shape-observation.ts`,
`apps/three-surface-poc/src/polaris-source.ts`,
`packages/polaris-generation-core/src/pipeline.test.ts` and
`packages/polaris-generation-core/README.md` — were swept against every
`*-MANIFEST.txt` row, every `docs/evidence/*manifest*.json`, and
`ACCEPTANCE-ACT-RECORD.md` — **0** hits for each, under a 21-file manifest
population [Observed, computed this
session; the record is cited by path and no digest is reproduced, per CG-15].
What *is* bound is an evidence record rather than an act: see "What landing
slices 1, 2 and 6 retires" in Gate 3.

**Two package banners that are false and may not be corrected.**
`docs/evidence/polaris-generator-current-scope-2026-09-12.json` carries a
governance-lifecycle status of "unadopted; awaiting final independent review
and owner acts" and an `implementedGenerator` of false over a scope three acts
adopted on 2026-09-12, and both specification files still open with a
candidate banner over bytes an act bound. Per AGENTS.md, read the act record,
never the package banner.

## Gate 1 — Motif

**The loop has no entrance from the observation plane, no exit to the owner,
and no structural independence in the middle.** Three measurements, each with
its denominator, say it exactly:

1. **No entrance.** The lawful reader — `body-read-authority` → observation →
   `git-object-reader` → classification → extraction → coverage — produces a
   `PocModel.projectShape` carrying revision identity, evaluation instant,
   classification basis, exclusion state and per-source anchor identities. The
   generator's entire notion of a source is
   `packages/polaris-generation-core/src/provider-draft.ts` line 109:
   `list(object({ sourceId: handle, text: { type: 'string', minLength: 1, maxLength: 100000 } }), 1)`.
   Across the **20** tracked files of `packages/polaris-generation-core` and
   `apps/three-surface-poc/src/polaris-generation`, the literals
   `three-surface-poc-core`, `PocModel` and `projectShape` occur **0** times
   [Observed, literal sweep re-run 2026-09-15; denominator those 20 tracked
   files, enumerated by `git ls-files` over both paths — 14 and 6]. The two
   planes have never been connected. [Superseded 2026-09-15, review 1 F1: this
   denominator read "the **20** files of
   `packages/polaris-generation-core/src` and
   `apps/three-surface-poc/src/polaris-generation`". That spelling is **17**
   tracked files (11 + 6), not 20; 20 is the whole core package plus the app
   directory. Both sweeps were re-run over both sets this session and return
   **0** on each, so the figure is unchanged and only the denominator's name
   is corrected.]

2. **No independence.** `PipelineRequest.providerRoute`
   (`packages/polaris-generation-core/src/pipeline.ts` line 19) is a single
   scalar threaded into every `AttemptInput` (line 182), so the controller
   cannot route the review stage to a different model, vendor or temperature
   even if an adapter wanted to. And the reviewer is handed the author's own
   argument. Measured this session by putting a sentinel string into one
   source and reading each stage's encoded envelope at the `generate` port:

   | Stage | Keys in the envelope's `inputs` | Sentinel occurrences |
   |---|---|---:|
   | `inventory` | `readerQuestions`, `sources` | 1 |
   | `plan` | `inventory`, `readerQuestions`, `sources` | 2 |
   | `author` | `inventory`, `plan`, `readerQuestions`, `sources` | 2 |
   | `edit` | `draft`, `inventory`, `plan`, `readerQuestions`, `sources` | 4 |
   | `fidelity` | `draft`, `inventory`, `plan`, `readerQuestions`, `sources` | 4 |

   The `inventory` stage is already structurally independent — two keys, no
   draft, no plan. The `fidelity` stage is not: it receives `plan`, whose
   `sections[].reason` is each section's self-declared justification. The
   fidelity prompt then instructs the model, at
   `packages/polaris-generation-core/src/prompts.ts` line 21, "Do not rewrite
   the draft, accept the author's self-assessment as evidence, or grant owner
   approval" — compliance by instruction where bounding by input was available
   and free. The inventory prompt shows the pattern is already known to the
   package: line 9 says "do not use a candidate draft, outline, author's
   assessment or authoring conversation as your denominator", and for that one
   stage the envelope enforces it.

3. **No exit.** `runGenerationPipeline` returns a run-lifecycle state of
   `awaiting-rendered-review` (`pipeline.ts` line 272), and that state has no
   successor anywhere in the `PipelineResult` union (lines 103–115). The
   rendered preview is produced *outside* the pipeline, by
   `apps/three-surface-poc/src/polaris-generation/pipeline-demo-main.ts` line
   16, after it has already returned. The daemon's route table registers
   **15** route entries over **15** distinct paths, **11** `human-open` and
   **4** `machine-credentialed` — the latter being two logical machine routes
   each registered twice, at its direct path and under the tailnet mount
   prefix (`apps/three-surface-poc/src/routes.ts` lines 206–239; counted this
   session by calling `pocRoutes` on the built module). In that same file the
   literals `generation` and `draft` occur **0** times, case-insensitively
   [Observed, this session, denominator the whole 240-line file]. The only way
   to see a draft is `npm run poc:generator-demo -- --out <dir>`.

**And the citation the preview does render is a position, not an identity.**
`apps/three-surface-poc/src/polaris-generation/draft-preview.ts` line 11
builds `sourceId → array index`, and line 23 emits
`<a href="#source-${index}" aria-label="Read source ${index + 1}">[${index + 1}]</a>` — so
reordering the caller's source array silently renumbers every citation on the
page. Two rows away, the PWB renderer already does this right: the
exact-source route is keyed by the source *identity* in its query
(`apps/three-surface-poc/src/polaris-source.ts` lines 31–42). The generator
re-invented the one thing Polaris is already good at, worse.

**Success criteria, per slice.** Slice 1: shuffling the source array changes
no rendered citation, and every citation resolves through a durable identity.
Slice 2: the fidelity envelope's encoded bytes contain no plan handle, and the
receipt names which route reviewed. Slice 3: the unchanged pipeline accepts
Syzygy's own 105-source corpus, and every breach it hits is recorded as a
finding rather than tuned away. Slice 4: a draft is reachable and the owner's
one action produces an RFC7-21-shaped packet nobody has performed. Slice 5: an
operator reading the kit's start path learns which act stands between them and
a provider call. Slice 6: a run killed at `fidelity` re-runs paying only
`fidelity`. None of these makes anything green.

**What M7 is not.** It is not a provider integration, not an egress request,
not a real Butlers read, not a change to the rendered Polaris page, and not a
claim that the generator works.

## Measurements at `a9f671e`

Every figure below was taken this session in the worktree at `a9f671e`.
Method, predicate, denominator and raw output for each are in the evidence
record beside this packet.

**Line-count convention, stated once.** A "line count" below is the `wc -l`
count — the number of newline characters — and is marked as such where a
figure depends on it. Under it `pipeline.ts` is 276 lines, `provider-draft.ts`
152, `routes.ts` 240, `prompts.ts` 29 and `tasks.md` 51. Where a file's
split-on-newline count is used instead (one more, for a file ending in a
newline) it is named at the site.

### What the pipeline costs, measured at the `admit` port

Method: run the shipped synthetic fixture through the unchanged
`runGenerationPipeline`, with a capturing `admit` port recording each
`AttemptInput.inputBytes`. Denominator: every stage the run admits.

| Stage | Ordinal | `inputBytes` |
|---|---:|---:|
| `inventory` | 0 | 3,422 |
| `plan` | 1 | 4,297 |
| `author` | 2 | 7,971 |
| `edit` | 3 | 8,807 |
| `fidelity` | 4 | 6,283 |
| **total** | | **30,780** |

The source corpus in that run is 439 bytes as `JSON.stringify` encodes it, so
the run charges **70.1×** the corpus against one cumulative budget [Observed].
Padding each of the three source texts and re-measuring gives the marginal
slope: 439 → 30,780, 3,439 → 65,780, 6,439 → 100,780, i.e. **11.67 bytes of
billed input per byte of source** in this fixture [Observed, three runs]. The
slope is fixture-dependent — this fixture echoes each source's text into an
inventory `statement` and again into a draft paragraph — but the structural
part is not: `sources` is a key of **all five** envelopes, so the corpus
itself is encoded once per stage, five times in a no-repair run and seven with
one repair cycle (`pipeline.ts` lines 259–269).

**A figure that differs from the dossier.** L3-F7 says the envelope "embeds a
full copy of the system prompt that is separately passed as `system` at line
219, so the prompt is billed twice per call". Half of that is confirmed and
half is not. `pipeline.ts` line 176 puts `system: prompt.system` inside the
envelope and line 219 passes `system: prompt.system` to `ports.generate`
alongside the encoded envelope, so a real adapter that fills a system message
from one and a user message from the other **transmits** the prompt twice
[Observed]. But the budget charge is `Buffer.byteLength(encoded)` (lines
177–179), the envelope alone: it is **billed once**. The five no-repair
prompts total **11,284** bytes (`inventory` 1,971, `plan` 2,371, `author`
2,459, `edit` 1,968, `fidelity` 2,515) and the six schemas **14,155** bytes,
of which `author`, `edit` and `repair` share one 3,961-byte object [Observed,
computed from the built `stageSchema` objects this session].

### What a real corpus costs, measured on Syzygy's own tree

Method: build the source array from Syzygy's own governed corpus — the six
tracked `.md` files under `.syzygy/governance/doctrine/`, the **71** tracked
`.md` files under `.syzygy/governance/decisions/` **at every directory level**
(67 at the top level and four under `launch-gate/`), and the **28** accepted
RFC modules, meaning the `.md` files **one directory below**
`.syzygy/governance/contracts/rfcs/` — and encode one real `inventory`-stage
envelope with the package's own `encodeCanonicalJson` under the limits
`pipeline.ts` line 122 constructs. Denominator: those 105 files. The two
accepted RFCs that are single files rather than directories,
`RFC-0001-project-graph-identity-state-planes.md` and
`RFC-0006-cross-surface-selection-query-drawer.md`, fall **outside** the
module predicate and so outside this corpus; taking every tracked `.md` under
`rfcs/` instead gives 107 files / 1,369,266 bytes / 1,360,678 characters /
**0** over the cap / largest 63,903 [Observed, both predicates run
2026-09-15]. [Superseded 2026-09-15, review 1 F2: this method read "the 71
top-level `.md` files under `.syzygy/governance/decisions/`, and the 28
accepted RFC modules" and named neither exclusion. Run as written the first
half is 67, not 71, and the review's own reading of it — every tracked `.md`
under `rfcs/` — is 107. The published figures re-derive exactly under the
corrected wording and under nothing else.]

| Figure | Value |
|---|---:|
| Sources | 105 |
| Raw source bytes | 1,266,454 |
| Raw source characters | 1,258,724 |
| Sources over the 100,000-character per-source cap | 0 |
| Largest single source, characters | 55,836 |
| One `inventory` envelope, encoded | **about 1.29 MB**, ± the id and question bytes (see below) |
| Smallest `maxInputBytes` that encodes it | between 1,000,000 (rejected, `byte-limit`) and 2,000,000 (accepted) |

**Which commit these figures are of.** All of them are taken at
`a9f671e`, the baseline this packet measures. The corpus includes
`.syzygy/governance/decisions/`, so this packet's own P-76 register row
moved two of them: at this commit the same predicate gives **105 files /
1,277,862 bytes / 1,270,122 characters**, with the file count, the cap
result (**0** over) and the largest source (**55,836** characters)
unchanged [Observed, the predicate run at both revisions 2026-09-15 from
`git ls-tree` blobs, denominator the 105 files at each; anchor added
2026-09-15, review 2 G5(b), which found the figures relying on a section
heading 300 lines above rather than carrying the anchor at the site].
Every future decision row will move them again.

**Why that row is approximate, and what it is approximate over.** The method
above omits two free inputs the encoded size depends on: what each source's
`sourceId` is, and what `readerQuestions` holds. **Eighteen**
reproductions — nine `sourceId` schemes × two reader-question arrays —
were run 2026-09-15 over the same 105 files, the same
`promptForStage('inventory')`, the same `stageSchema('inventory')` and
the same envelope shape `pipeline.ts` line 176 constructs, varying only
those two. With the repository-relative path as `sourceId`: 1,300,688
bytes with the demo's three reader questions, 1,300,601 with none. With
the basename: 1,297,209 / 1,297,122. With the stem: 1,296,894 /
1,296,807. With the path minus its `.syzygy/governance/` prefix:
1,298,693 / 1,298,606. With `source-N` ids: 1,294,916 / 1,294,829 one-based
and 1,294,914 / 1,294,827 zero-based. With `src-N`: 1,294,601 / 1,294,514.
With `s-N`: 1,294,391 / 1,294,304. With the bare ordinal: 1,294,181 /
1,294,094. **None equals 1,294,284**; the nearest is 20 bytes away and the
figure sits inside the band rather than on any stated scheme [Observed,
**eighteen** encodings run this session; each scheme and question array
is published in the evidence record, whose
`review1.f3_reproduction.bytes_by_scheme` carries nine schemes each with
a `demo_3` and an `empty` array. Restated 2026-09-15, review 2 G3: this
read "twelve encodings", a count that does not re-derive over the
eighteen values printed immediately above it]. So the row is restated as
approximate, which is what slice
3's own oracle already says ("an `inventory` envelope of about 1.29 MB"): rule
3's shape is that a computed figure a later reader cannot recompute is not yet
evidence. [Superseded 2026-09-15, review 1 F3: the table row read
"**1,294,284** bytes" as an exact computed figure.] What does re-derive
exactly under **every** one of the eighteen variants is the limit probe —
1,000,000 rejected with `byte-limit`, 2,000,000 accepted — and the ×5
arithmetic below ["the twelve variants" until 2026-09-15, review 2 G3].

Because `sources` is a key of all five envelopes, a no-repair run over this
corpus needs a cumulative `maxInputBytes` of at least **5 × about 1.29 MB,
i.e. about 6.5 MB** (5 × 1,294,284 = 6,471,420 on the superseded exact figure)
[the envelope figure is Observed; the ×5 follows from the stage-input
construction traced above and is [Inferred] for a run nobody has executed].
And one value must serve both roles: `dataLimits(budget.maxInputBytes)` bounds
the single canonical encoding at line 177 *and* the cumulative sum at line
179, so a budget large enough to admit five stages also permits any one
envelope to be that large.

**The two landed hard caps, and what they actually bound.** `list()`
(`provider-draft.ts` line 15) defaults `maxItems` to 200 and the source schema
at line 109 takes that default, so a corpus of more than 200 sources is
refused outright. Butlers at the retained capture reports **278** sources of
which **86** carry bodies totalling **1,120,065** bytes
(`projectShape.counts.sources` and `projectShape.resourceUse` in the retained
machine capture) [Observed, read from the capture this session]. So the honest
statement is narrower than L3-F7's: feeding Butlers' 86 **bodies** fits the
200-item cap today and feeding its 278 **sources** does not — the cap binds
the population, not the body count, and Butlers is already 78 over it on the
population. Syzygy's own 105-file corpus fits both caps.

### The two planes, and the identity each side carries

| Side | Identity it carries | Where |
|---|---|---|
| Observation | `repositoryId`, `requestedRevision`, `revision`, `capturedAt`, `sourceClaimedInstant`, `scope`, `observer`, `policy`, `manifestIdentity`, `manifestDigest`, `observationDigest`, `deterministicInputs` | `packages/three-surface-poc-core/src/project-shape-model.ts` lines 200–213 (`ProjectShapeIdentity`) |
| Observation, per source | `identity`, `stamp`, `rule`, `pillar?`, `declaredBy?`, `anchor`, `claim` | same file, lines 215–223 (`ProjectShapeSource`) |
| Observation, per claim | `claimId`, `evaluationId`, `epistemic`, `resolutionRoutes`, `challenge`, `support` (each `support` entry: `path`, `line?`, `contentDigest?`, `sourceIdentity?`) | same file, lines 107–131 |
| Generation | `sourceId`, `text` | `packages/polaris-generation-core/src/provider-draft.ts` line 109 |

Every provenance field on the left is discarded at the type level on the
right. That is the gap slice 1 closes, and the reason the fix is a richer type
rather than an adapter bolted onto this one.

### Line numbers re-verified at `a9f671e`

**The dossier's stated audit commit does not hold for this surface, and the
reconciliation is clean.** `docs/pursuits/2026-09-13-vision-pursuit-data.json`
records `"syzygy_audited_at": "f4589e2"`. Restricted to the paths this packet
cites in the implementation plane, `git diff --name-status f4589e2 a9f671e`
over `packages/polaris-generation-core`, `docs/polaris-generation`,
`apps/three-surface-poc/src/polaris-generation`, `package.json` and
`apps/three-surface-poc/src/routes.ts` returns **22** rows — **20 `A`** and
**2 `M`** — and `apps/three-surface-poc/src/routes.ts` appears in **no** row,
so its line numbers were current at `f4589e2` too. The same diff restricted to
`1932f74..a9f671e` returns **0** rows, so the whole surface is byte-identical
between the tree the L3 agent read and this packet's baseline [Observed, both
diffs run this session].

| Citation | At `a9f671e` | Dossier / finding said | Note |
|---|---|---|---|
| `pipeline.ts` `providerRoute` on `PipelineRequest` | 19 | 19 | exact |
| `pipeline.ts` `admit` port contract | comment 60–64, declaration 65 | 60–65 | the sentence is in the comment; line 65 is the declaration it annotates |
| `pipeline.ts` `PipelineResult` union | 103–115 | 103–115 | exact |
| `pipeline.ts` initial `context` | 170 | 170 | exact |
| `pipeline.ts` cumulative budget check | 176–179 | 176–179 | exact |
| `pipeline.ts` stage call sites | 259–269 | 259–263 | the dossier's range stops before the repair loop at 265–269, which is half of slice 6's subject |
| `pipeline.ts` `awaiting-rendered-review` | 272 | 272 | exact |
| `provider-draft.ts` `sourceSchema` | 109 | 109 | exact |
| `provider-draft.ts` plan pin in the draft branch | 137 | 137 | exact |
| `provider-draft.ts` `reviewVerdict` | 148–152 | 148–152 | exact |
| `draft-preview.ts` index map | 11 | 11 | exact |
| `draft-preview.ts` `#source-N` href | 23 | 23 | exact |
| `pipeline-demo.ts` hand-written source corpus | 33–37 | 33–37 | exact |
| `pipeline-demo.ts` `verifySources` | 67 | 67 | exact |
| `pipeline-demo-main.ts` preview call | 16 | 16 | exact |
| `pipeline.test.ts` duplicate-start pin | 73–76 | 74–75 | the re-run is on 75 and the **5**-send assertion that makes it load-bearing is on 76 |
| `routes.ts` "no generation route" | whole file | 21–22 | **lines 21–22 are the `POLARIS_PRESENTATION_PATH` and `POLARIS_PRESENTATION_KIND` constants**, not the route table; the finding's claim is true and its anchor is not. The route table is 206–239 and the absence is a whole-file sweep |
| generator implementation act, reservations | 42 | 42 | exact |
| base spec, RFC7-10 anchor sentence | 98 | 98 | exact; REQ-003 is unamended, so this is the effective text |
| base spec, "Reviewers SHALL receive…" | 302 | 302 | exact; REQ-006 is amended, and the sentence stands verbatim at overlay line 180 |

### Figures that differ from the dossier

Six, collected; the companion evidence record's
`figures_that_differ_from_the_dossier` array carries the same six in this
order [Observed, both counted this session].

1. **The prompt is transmitted twice and billed once**, not "billed twice per
   call" (L3-F7).
2. **The 200-item cap binds the source population, not the body count.**
   Butlers' 86 bodies fit it; its 278 sources do not. L3-F7's "a project with
   more than 200 admitted bodies is refused outright" is true of bodies and
   silent about the population figure that actually breaches.
3. **L3-F5's `routes.ts:220` and `routes.ts:21-22` anchors do not carry the
   claim.** Line 220 is the Polaris human-surface registration and 21–22 are
   the presentation-path constants; the absence is established by a whole-file
   sweep, not by those lines.
4. **The dossier's slice 2, "fidelity envelope built from the draft alone",
   contradicts the requirement it is scheduled from** and is corrected to
   `{sources, inventory, draft, acceptanceCriteria}` above.
5. **The self-corpus run cannot be "the second project"** (L3-M6): REQ-014's
   own "Narrow evidence offered as completion" scenario marks synthetic
   provider runs unproven for exactly that obligation.
6. **A defect the dossier does not name:** the `inventory` stage is *already*
   structurally independent — its envelope carries two keys and neither is a
   draft or a plan — so slice 2 is a narrowing of **four** envelopes, not six,
   and the package already contains the pattern it needs to copy. **The
   population "four" is over:** the envelopes that carry the `plan` today —
   `author`, `edit`, `fidelity` and `repair`, the last because `pipeline.ts`
   line 267 hands `repair` the same accumulated `context` [Observed, the five
   measured envelopes above plus the repair call site, read at source
   2026-09-15]. Of those four, slice 2 changes exactly two — `fidelity` and
   `repair` lose the plan, `author` and `edit` keep it — which is Gate 4's
   "**Exactly two envelopes change**". [Superseded 2026-09-15, review 1 F5:
   this item named no population for "four", leaving 2, 4 and 5 in the packet
   for one quantity with no reconciliation.]

## Gate 2 — Doctrine

**VIS-2 — No evidence means Unknown, not success.** Quoted at the clause,
`.syzygy/governance/doctrine/vision.md` lines 96–106: "No surface may declare
a project aligned, converged, or genome-complete — nor turn anything green —
without current evidence… Until a claim class declares its currency bound, its
evidence is not current and the claim renders Unknown." Slices 1 and 3 are
applications at two different seams. Slice 1: a citation that is an array
position is not evidence of anything, and a reordered input produces a
confidently wrong page — the violation clause's "a stale view silently green"
in miniature. Slice 3: the honest outcome of a self-corpus run is a list of
breaches, and the slice's own success criterion is that it records them rather
than tuning the fixture until they disappear.

**VIS-1's ordering is what puts slice 1 above slice 4.** "Truth and
observation determinism" first, "comprehension of the truth's presentation"
second (`.syzygy/governance/doctrine/vision.md` line 82 onward). A durable
citation identity is a truth change; a route that serves the draft is a
comprehension change. Both are worth doing; slice 1 is worth more, and it is
also the thing slice 4 would otherwise render.

**VIS-4 — Humans steer the vision; agents shape within it.** Lines 122–139,
quoted at the load-bearing sentence: "One class is always human-gated, gate
open or not: spec changes touching security posture, privacy or retention
obligations, or normative data contracts." Q1 exists because reading a sixth
target kind into RFC7-10's closed five is an accepted-contract question, and
RFC acceptance is named in VIS-4's first sentence as shape-defining. Q5 exists
because the `admit` port's replay prohibition is a normative data contract at
the effect boundary. This packet drafts both questions; it answers neither.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Lines 141–162. Slices 1, 2, 3, 5 and 6 write only into
`packages/**`, `apps/**`, `docs/**` and `package.json` — the implementation
plane — which is the worker action VIS-5's own sentence reserves it to:
"materialization is exclusively a worker action against scheduled work." Slice
4's **drafted-act packet is the one limb that would write into `.syzygy/**`**,
which is a lawful write root under this same rule — and that is precisely why
P-71's Q3 exists rather than being obvious: VIS-5 makes the *namespace* lawful
and says nothing about whether emitting a drafted act is an effect an act in
force covers. Q4 takes P-71's arm (b) so that this packet's recommended path
writes no file at all.

**SEC-2 — Portfolio data leaves owner-controlled infrastructure only through
explicit, scoped consent.** `.syzygy/governance/doctrine/security.md` lines
25–37, quoted at the load-bearing sentences with the source's own emphasis and
no added emphasis: "Governed-project content — source structure, specs, work
history, and anything derived from them, including prompts — is never
transmitted to a store or service the owner does not control without explicit,
recorded, per-project consent. **Model providers are such services.**
Onboarding consent must name the providers permitted for a governed project
and the content classes that may be sent". That sentence names **two** of
slice 5's five fields — the providers and the content classes — and slice 5
attributes the other three at its own site: the refusal behaviour on
withdrawal to REQ-001, and the route and the retention to this packet's own
proposal. [Superseded 2026-09-15, review 1 F9: this read "That sentence is the
whole content of slice 5: it names, field for field, what the egress act would
have to say", a contract claim wider than the clause it is anchored to.] **No
slice in M7 sends anything anywhere.** Swept over the **20 tracked files** of
`packages/polaris-generation-core` and
`apps/three-surface-poc/src/polaris-generation`, the literals `fetch(`,
`node:http`, `node:https`, `undici`, `axios` and `XMLHttpRequest` occur
**0** times [`XMLHttpRequest` added to the enumeration 2026-09-15, review
2 G13: the evidence record's predicate and this packet's own F1
disposition row both name six network primitives and this list named
five, so a reader re-running the enumerated five ran a weaker sweep than
the figure is claimed over. All six re-run over the 17-file and the
20-file sets 2026-09-15: **0** on each]; the three
matches for `https://` are all escaping fixtures inside tests, at
`packages/polaris-generation-core/src/provider-draft.test.ts` line 61 and
`apps/three-surface-poc/src/polaris-generation/draft-preview.test.ts` lines 48
and 59 [Observed, re-run 2026-09-15 over that denominator and over the 17-file
`src`-only set; identical on both. Superseded 2026-09-15, review 1 F1: the
denominator read "the 20 files of the generation package and the app's
generation directory", whose `src`-only spelling is 17 tracked files].

**RFC7-10 is a boundary slice 1 must cross deliberately, not silently.** Its
five closed target classes are quoted whole in Gate 5. Slice 1 as designed
carries the registry's `git-tree-entry` identity into the generator; whether
that satisfies REQ-003's anchor sentence is Q1, and the packet's default arm
is to ship the fields and record the clause as unsatisfied rather than to
assert conformance the owner has not ruled.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Observation-typed sources | `packages/polaris-generation-core/src/provider-draft.ts` (the source schema at line 109, `validateStage`'s source unpacking at 109–112, `references` at 90–98); `packages/polaris-generation-core/src/index.ts` (one new exported type); a new app module beside `apps/three-surface-poc/src/polaris-generation/draft-preview.ts` projecting `PocModel.projectShape` into it; `apps/three-surface-poc/src/polaris-generation/draft-preview.ts` (citations by identity, reusing `apps/three-surface-poc/src/polaris-source.ts`'s href construction); `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` (fixture shape) | **none edited.** The identity scheme is *read* from `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` line **54** (the class literal is on 53), which two acts bind [anchor corrected 2026-09-15, review 1 F10.1; it read "line 53"] |
| 2 Structural independence | `packages/polaris-generation-core/src/pipeline.ts` (`PipelineRequest.providerRoute` 19 → a per-stage map; `AttemptInput.providerRoute` 30; the validity check at 137; `AttemptInput` construction at 180–185; the stage call sites at 259–269; `StageReceipt` at 90–96 gains the route and model); `packages/polaris-generation-core/src/pipeline.test.ts` | none |
| 3 Self-corpus proof | a new operator module under `apps/three-surface-poc/src/polaris-generation/` composing slice 1's adapter over Syzygy's own tree; a new `poc:` script entry in `package.json`; a new evidence record under `docs/evidence/` | none |
| 4 Draft route and drafted act | `apps/three-surface-poc/src/routes.ts` (one new `machine-credentialed` route and one new `ResponseLimitIdentity`, both **conditional on Q3**); `packages/three-surface-poc-core/src/project-shape-observation.ts` (a fourth registry ceiling, conditional on Q3 and on P-72's Q2); `packages/polaris-generation-core/src/pipeline.ts` (`PipelineResult`'s union at 103–115 gains the states after `awaiting-rendered-review`); a new pure packet-drafter module | **conditional.** On Q3's recommended arm the registry entry `PwbResourceLimits` describes is amended by a superseding owner act, which is P-72's Q2, not a new question |
| 5 The egress act, named | `docs/polaris-generation/README.md` (one step inside "Start here", lines 37–44); `PROJECT-STATUS.md` (one sentence in the paragraph at lines 38–44) | none |
| 6 Stage-scoped inputs and resume | `packages/polaris-generation-core/src/pipeline.ts` (per-stage input construction at 259–269, shared with slice 2; the `admit` port contract at 60–65, **conditional on Q5**); `packages/polaris-generation-core/src/pipeline.test.ts` lines 73–76 | none |
| 7 (deferred) Drift band | not designed here | not designed here |

Boundaries crossed: none. Every file above is in the implementation plane,
plus `PROJECT-STATUS.md`, which is a status page and not a governed artifact.
The `openspec/**` and `.syzygy/**` trees are read for authority and written by
no slice — with the single exception of slice 4's drafted-act packet, which on
Q4's recommended arm writes nothing at all.

Not touched by any slice: the cancellation, deadline, permit, late-receipt and
uncertainty machinery of `pipeline.ts` lines 146–258, which L3 judged the
strongest part of the package and which slice 2 rearranges the *inputs* to
without changing; the canonical JSON encoder and bounded parser; the PWB
reader chain, which slice 1 consumes and does not modify.

### The authorizing act, per slice

Every M7 slice is scheduled from **predecessor text** — the ten-sentence sweep
in "Decided in this packet" — so the per-slice predecessor/overlay-only column
that P-73's Q6 turns on reads the same for all six. The column below instead
records the Phase the clause sits in, which is where M7's own act question
lives.

| Slice | Owner act needed | Effective clause (and its Phase, per `EXECUTION-PHASES.md` line 18) | Named act, the task it is filed against, and the trigger test |
|---|---|---|---|
| 1 Observation-typed sources | **No for the type; Q1 for the conformance claim** | REQ-003's anchor sentence, base line 98. **Phase A** (001–012) | Rides `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-12). Filed against unchecked task **2.2**, "Implement source understanding, project-specific argument construction and bounded asset generation (002/003/004/005), preserving Unknown and editorial-draft states" (`tasks.md` line 22). No trigger crossed: no read, no egress, no write outside the implementation plane. Q1 governs only whether the result may be *called* RFC7-10-conformant |
| 2 Structural independence | **No** | REQ-006's "Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation", base line 302, identical at overlay line 180. **Phase A** (006 is in 001–012) | Same act. Filed against unchecked task **2.4**, "Implement review invalidation, source regeneration, authored-content coexistence, per-block human acts and rejection (006/009/010/011/016)" (`tasks.md` line 24). The per-stage route map is a type change with no effect: today's single scalar is the degenerate case |
| 3 Self-corpus proof | **Q2** | REQ-014's two-project and synthetic-evidence sentences, base line 755, identical at overlay line 367. **Phase A** (014 is named) | Same act, **if** Q2 is ruled the recommended way. Filed against unchecked task **3.3**, "Run the same unmodified generator on two separately admitted, materially different real projects, and repeat after real source changes (014)" (`tasks.md` line 47) — and filed as *preparation for* it, never as its discharge. The trigger tested is the act's own "Real-project reads … remain separately admitted", which is exactly Q2 |
| 4 Draft route and drafted act | **Q3 for the route; Q4 for the packet; both are already before the owner as P-72 and P-71** | REQ-020's guided-start sentence, base line 1083 — **Phase B**, per `EXECUTION-PHASES.md` line 19: "Requirements 013, 020-024 and 026-029 remain integration obligations; their interfaces are preserved and their implementation/evidence is not claimed by Phase A." REQ-010's per-block authorship sentence, base line 528, is **Phase A** | Same act, which authorizes "the full EXECUTION-PHASES.md implementation goal", so Phase B is inside the grant and the phase ordering is a proposal rather than a gate — `EXECUTION-PHASES.md` line 4 says in terms that it "is not an owner N/A judgment, an act or permission to implement". Filed against unchecked task **2.8** (`tasks.md` line 31). Two triggers are live: Phase A's seam "does not … serve owner effect controls" (lines 13–14, the sentence beginning on 13) [anchor corrected 2026-09-15, review 1 F10.2; it read "(line 14)"], which slice 4 by design does; and the act's "destination writes", which Q4's recommended arm avoids entirely |
| 5 The egress act, named | **No** | Argued from SEC-2 directly, not from a requirement clause | Same act. The kit is not a specification obligation; the `PROJECT-STATUS.md` sentence is a status correction, which needs no act. Naming an act is not performing one, and this packet neither drafts nor performs it |
| 6 Stage-scoped inputs and resume | **No for limb (a); Q5 for limb (b)** | REQ-008's resume and duplicate-start sentences, base line 400, and its approved scenario "Resume valid work" at base lines 407–411. **Phase A** (008 is in 001–012) | Same act. Filed against unchecked task **2.3**, "Implement authoritative lifecycle integration, cancellation, duplicate/resume handling and effect uncertainty (007/008/013)" (`tasks.md` line 23) — the words "duplicate/resume handling" are the task. Limb (a), stage-scoped inputs, changes no contract sentence and needs no ruling |
| 7 (deferred) Drift band | not evaluated | REQ-009's source-drift clauses, overlay line 241 onward | not evaluated; overlaps M12 (L2-M6) |

`tasks.md` carries **24** checkbox lines under the predicate `^- \[[ xX]\] `
and **0** are checked, over a 51-line file by `wc -l` [Observed, counted this
session]. Every slice above duplicates an unchecked task and is filed against
it rather than as new scope.

### What landing slices 1, 2 and 6 retires

`docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`
records **17** source digests over exactly this surface — every non-test and
test file of `packages/polaris-generation-core/src` and
`apps/three-surface-poc/src/polaris-generation`. **All 17** equal their files'
current bytes [Observed, recomputed this session; no value is reproduced here,
per CG-15 — the record is cited by path]. Slices 1, 2, 4 and 6 rewrite
`pipeline.ts`, `provider-draft.ts`, `draft-preview.ts`, `pipeline-demo.ts` and
`pipeline.test.ts`, all of them rows. **No *act* binds those bytes** (Gate 6
item 7), so no act-bound byte is proposed for edit; but editing them retires
that record's binding to them, which is verification rule 10's shape applied
to an evidence record. The implementing bead for each slice must re-run that
verification and record the new digests before the slice is called done. M6's
slices 2, 3 and 4 incur the same obligation on an overlapping subset, so the
re-run should happen **once, after both land**, not twice.

All slices run under `syzygy-dov.7`, the pursuit bead; no new generator bead
is filed by this packet.

## Gate 4 — Design sketch, per slice

### Slice 1 — A source is an observation, and a citation is an identity (large; Q1 for the conformance claim)

**The type, in the core, with no import from the observation package.** The
generation core stays project-neutral: it defines the shape and never learns
what a `PocModel` is.

```
interface GenerationSource {
  sourceId: string;            // provider-local handle, as today
  repositoryId: string;
  revision: string;
  path: string;
  objectId: string;            // the git object id; the integrity digest
  evaluationId: string;
  classificationBasis: 'body' | 'path-only';
  exclusion: { excluded: false } | { excluded: true; reason: string };
  spans: { anchorId: string; start: number; end: number; text: string }[];
}
```

**Where the fields come from.** The registry's declared identity scheme is
`repository-id-plus-revision-plus-repository-relative-path-plus-object-id`,
and the four fields above are exactly its four parts; `evaluationId`,
`classificationBasis` and the exclusion state come from
`ProjectShapeClaim`/`ProjectShapeSource` (`project-shape-model.ts` lines
107–131 and 215–223). Nothing is invented and nothing is renamed.

**Excluded and path-only sources are admitted as first-class Unknowns.** Today
they are dropped before the generator sees them, which means the generator's
denominator is silently smaller than the project's. With
`classificationBasis: 'path-only'` and an empty `spans` array, a source is in
the corpus, countable by the inventory stage, and unquotable — which is the
truthful shape.

**One adapter, in the app.** A single module projecting
`PocModel.projectShape` into `GenerationSource[]`. This is the first arrow
between the two planes, and it lives on the app side so the core keeps its `0`
references to `three-surface-poc-core`.

**Citations.** `renderDraftPreview` stops building `sourceId → index`. Every
citation resolves through `anchorId` to the href
`apps/three-surface-poc/src/polaris-source.ts` already constructs
(`sourceRouteHref`, lines 41–43, under its doc comment at line 40), reusing
that function rather than re-deriving the URL — AGENTS.md's caution about a
second encoding for the same meaning.

**Oracle.** Independently written fixtures with the expected rendered hrefs
written as hard-coded literals in the test, never imported from the module
under test.

**Rule-6 mutants.** (a) Shuffle the source array and assert the rendered
citation set is byte-identical; then mutate the renderer back to index-based
citations and confirm that test fails — the counterexample that proves the
check is load-bearing. (b) Give a `path-only` source a non-empty `spans` array
and confirm validation refuses it. (c) Point a citation at an `anchorId` no
source carries and confirm the existing `unknown-source` error shape fires.
(d) Change one character of a source's `objectId` and confirm the citation
href changes, so the identity is genuinely revision-bound.

**Trade-offs rejected.** Keeping `{sourceId, text}` and adding a parallel
provenance map (two structures that can disagree is the defect, not the fix);
importing `three-surface-poc-core` into the generation core (it makes the core
Butlers-shaped, which is the opposite of the product goal); asserting RFC7-10
conformance without Q1 (that is the owner's ruling, not the implementation's).

### Slice 2 — Independence by construction, not by instruction (medium; no act)

**The route map.** `PipelineRequest.providerRoute: string` becomes
`routes: Record<GenerationStage, string>`; `AttemptInput.providerRoute` keeps
its scalar and receives the stage's own entry. Today's single-scalar callers
are the degenerate case — six identical entries — so no behaviour changes
until an operator supplies a different one.

**The envelopes, constructed at the call site.** `pipeline.ts` lines 259–269
stop passing the mutating `context` object and name each stage's inputs:

```
inventory : { sources, readerQuestions }                       // unchanged
plan      : { sources, readerQuestions, inventory }            // unchanged
author    : { sources, readerQuestions, inventory, plan }      // unchanged
edit      : { sources, readerQuestions, inventory, plan, draft } // unchanged
fidelity  : { sources, readerQuestions, inventory, draft, acceptanceCriteria }
repair    : { sources, readerQuestions, inventory, draft, findings }
```

Exactly two envelopes change: `fidelity` and `repair` lose `plan`. The
measurement above shows `fidelity` carries it today and `inventory` already
does not, so the package is being made consistent with itself.

**The receipt says who reviewed.** `StageReceipt` (lines 90–96) gains the
stage's route and the `model` string the adapter reported, which
`ports.record` already receives at line 253 and currently discards from the
receipt. Without this the owner cannot see whether the reviewer was a
different model at all.

**Oracle.** Assert on the **canonical encoding** of the fidelity envelope, not
on the prompt text: the encoded bytes must contain no plan section handle. The
test builds the plan with a distinctive handle so a short literal cannot be
reached by coincidence (AGENTS.md's copy-oracle caution).

**Rule-6 mutants.** (a) Re-add `plan` to the fidelity inputs and confirm the
encoding assertion fails. (b) Point two stages at the same route entry and
confirm the receipt still distinguishes them by stage. (c) Delete one stage's
entry from the route map and confirm `invalid-request` at line 137, not a
silent `undefined` on the wire.

**What this slice does not do.** It does not make the reviewer *actually*
independent — that needs two admitted provider routes, which needs egress
(slice 5). It makes independence *possible*, which it is not today, and it
costs nothing to do first.

### Slice 3 — Run the loop on Syzygy, and publish what breaks (medium; Q2)

**The responder.** A deterministic rule-based responder, not a fixture table:
it reads the envelope it is handed and emits a schema-conformant reply derived
from it (one inventory entry per source, one section per reader question, one
paragraph per cited entry). It is still a synthetic provider and the slice's
output says so in REQ-014's own words.

**The corpus.** Syzygy's own 105 governed files, measured above at
`a9f671e` (anchor added 2026-09-15, review 2 G5(b)) — the
doctrine, the decisions and the accepted RFC modules — behind an explicit
test-only profile. No new read authority is needed on Q2's recommended arm;
the files are in the worktree the process is already running in.

**The perturbation.** Change one governed file, re-run, and check that exactly
the affected blocks and citations move. With slice 1's identities this is
mechanically checkable: the citation set is a set of `anchorId`s bound to
`objectId`s, so a changed file changes exactly its own.

**What it records.** A `docs/evidence/` record naming the commit, the file
set, the per-stage `inputBytes`, every cap and budget breach, and — in the
requirement's own words — that real generation, regeneration and
reader-quality obligations remain **unproven** because the provider was
scripted.

**Oracle.** The expected breach list is written independently, from the
measurements in this packet, before the run: 105 sources at `a9f671e`
(anchor added 2026-09-15, review 2 G5(b)) under a 200-item cap
(passes), 0 sources over the 100,000-character cap (passes), an `inventory`
envelope of about 1.29 MB, and a cumulative requirement above 6.4 MB. A run
that reports no breach against a 1 MB budget has a broken check, not a cheap
corpus.

**Rule-6 mutants.** (a) Set `maxInputBytes` to 1,000,000 and confirm the run
stops with `budget-exhausted` rather than silently truncating. (b) Add a 201st
source and confirm the schema refuses the corpus. (c) Mutate the perturbation
check to compare only counts and confirm the changed-file test stops failing.

**Overlap, named.** L1-M5 — a self-profile for the **observer** — is a slice
of M8, which is being drafted in parallel and whose content is **[Unknown]**
to this session. If M8 lands a self-profile first, slice 3 should consume it
rather than build a second one; if slice 3 lands first, M8's should consume
slice 3's. This is a sequencing note, not a dependency: slice 3's reader is
the generator's input adapter, not the PWB observer.

### Slice 4 — A route, and one owner action that is a drafted act (large; Q3 and Q4)

**The route (Q3).** `GET /polaris/draft/<runId>`, `machine-credentialed`,
serving `renderDraftPreview`'s output together with the run's receipts, budget
spend and the stage that produced each block. It goes through the existing
`boundedResponse` (`routes.ts` lines 137–142), which is generic over the
identity it is handed — but its `ResponseLimitIdentity` union (line 111) is
closed at two literals and `PwbResourceLimits` is a seven-field interface, so
both widen by one. That widening happens under an owner act over the registry
entry, which is P-72's Q2, and the category question is P-72's Q1 — hence Q3's
recommendation to fold rather than to open a third framing.

**The type shows the loop's real shape.** `PipelineResult`'s union (lines
103–115) today ends at `awaiting-rendered-review`. It gains the states after
it, so a reader of the type can see that a draft is reviewed, then accepted,
rejected or repaired — rather than inferring from a status with no successor
that the loop simply stops.

**The one owner control, and what it emits (Q4).** Accept / reject /
repair-this-block. On the recommended arm the accept path calls a **pure**
drafter that returns an RFC7-21-shaped packet as data — subject digest,
per-claim-block attestation list, the phrase the owner would use, and the
manifest — and never a recorder's perform path. RFC7-21 lines 398–406 are the
bar: "The adopter attests per claim block… no draft is adopted by signature
over an unattested whole." A whole-document accept button would fail that
clause, so the packet is per block by construction.

**Never a performed act.** The drafter has no filesystem, no `bd`, no recorder
import. The packet it returns is marked draft in its own body. Nothing in this
slice can produce an artifact any surface would read as adopted.

**Oracle.** A fixture draft with three claim blocks, of which the owner
accepts two: the emitted packet carries exactly two attestations, keyed to the
two block ids, with the third absent and named as unattested. Expected values
are literals in the test.

**Rule-6 mutants.** (a) Emit a whole-document attestation and confirm the test
fails on the per-block predicate. (b) Mutate the route's ceiling identity back
to `maxMachineResponseBytes` and confirm the ceiling test stops distinguishing
a draft breach from an `/api/poc` breach. (c) Make the drafter write a file
and confirm the "writes nothing" assertion fails.

### Slice 5 — Name the act, say what it buys, say what it does not (small; no act)

**What the act would have to say**, field by field with each field attributed
to the clause that actually carries it. **Two come from SEC-2**
(`.syzygy/governance/doctrine/security.md` lines 25–37, read at source
2026-09-15), whose sentence is "Onboarding consent must name the providers
permitted for a governed project and the content classes that may be sent":
the **providers** permitted for this governed project, and the **content
classes** that may be sent. **One comes from REQ-001**, whose effective text
fixes it at base line 12: the **refusal behaviour on withdrawal** — "For
absent or withdrawn provider consent, the draft layer SHALL render Unknown
(`unconsented-source-or-provider`) as a policy state in both channels,
including when a prior draft remains retained." **Two are this packet's own
proposal and are anchored to no clause**: the **route** they are sent to and
the **retention** that applies to what is sent and to what comes back
[Inferred — a reading of what an egress act would need, not a requirement of
SEC-2 or of any requirement this packet cites]. [Superseded 2026-09-15, review
1 F9: this paragraph opened "taken field for field from SEC-2's own sentence,
which is the clause that makes it necessary" and then listed all five. SEC-2
names two of the five; asserting the other three from it is a contract claim
wider than the clause it is anchored to, which is verification rule 8's
failure.]

**What it buys.** Exactly the obligations in `tasks.md` §3 that no amount of
engineering can substitute for: 3.3's two real projects and changed-source
regeneration, 3.4's independent fidelity and cold-reader judgments over
*actual generated artifacts*, **3.4a's** application of DESIGN-ACCEPTANCE.md
to the full rendered reading "including the owner's reported failures", which
is also an actual-generated-artifact obligation, and 3.6's requirement-by-
requirement audit. **What it does not buy:** 3.1, 3.2 and 3.5 (failure seams,
rendered distinctions, fresh clone), which are reachable without it and should
land first — which is the sequencing L3-M9 argues for and this packet follows.
The partition is over the **seven** boxes `tasks.md` §3 carries — 3.1, 3.2,
3.3, 3.4, 3.4a (line 49), 3.5 and 3.6 [Observed, enumerated 2026-09-15].
[Superseded 2026-09-15, review 1 F12: the buys list named 3.3, 3.4 and 3.6 and
the complement 3.1, 3.2 and 3.5, stated as exhaustive over a §3 the packet had
read as six boxes; 3.4a was in neither half.]

**Where it goes.** One numbered step inside
`docs/polaris-generation/README.md` "Start here" (lines 37–44), between
"Inspect the synthetic example" and "Freeze the evaluation questions below
before generating" — because freezing questions is the step immediately before
a provider call, and that is where an operator is entitled to learn that the
call is not admitted. The kit's line 4 already says "This kit grants no source
access, provider egress, authorship adoption or release"; the new step says
which act would, and points at `PROJECT-STATUS.md`.

**And one sentence in `PROJECT-STATUS.md`.** Its paragraph at lines 38–44 says
"Project reads, provider egress and output writes remain separately admitted"
but does not say the thing a reader most needs: that **no model has been
called**, and that the honesty layer rather than the provider is the current
critical path. The sweep above is the evidence — 0 network primitives across
the 20 tracked files.

**This packet names the act and does not draft it.** Drafting an offer is a
separate, reviewable act-preparation task with its own ceremony
(`.syzygy/governance/decisions/README.md`) [path completed 2026-09-15, review
1 F11; it read decisions/README.md, written here without a code span because
that spelling resolves nowhere and CG-1b requires every code-span path to
resolve]; doing it inside a planning packet would put an act-shaped artifact
in a home no act covers.

**Test.** A literal assertion that the kit's start path and
`PROJECT-STATUS.md` each carry a distinctive full clause — not the word
`egress`, which is reached by coincidence (AGENTS.md's copy-oracle caution).

### Slice 6 — Pay for a stage once (medium; Q5 for limb b)

**(a) Stage-scoped inputs.** After the inventory stage, downstream stages
receive the inventory plus only the source spans their inputs cite, and the
full corpus is charged once. This shares its refactor with slice 2 — both
rewrite the same call sites at lines 259–269 — and should land in the same
change. On the self-corpus figures above, that is the difference between a
cumulative floor of about 6.4 MB and about 1.3 MB plus the cited spans.

**(b) Reserve/complete (Q5).** `admit` splits into a reservation and a
completion. A **completed** attempt identity returns its recorded artifact
instead of refusing; an **in-flight or uncertain** identity refuses exactly as
today. The replay prohibition the comment states is retained where it is
load-bearing — REQ-008's own "[a]n uncertain attempt SHALL continue to reserve
its maximum charge until trusted effect-and-usage resolution; missing receipts
or expired leases SHALL not permit redispatch" is unchanged by this slice.

**Oracle.** Kill a run at `fidelity`; re-run under the same `requestId` and
assert that the harness's send count rises by exactly **1**, not by 5. The
expected counts are literals; today's pinned value of 5 on a duplicate start
(`pipeline.test.ts` line 76) becomes the counterexample the new test must
distinguish itself from, and the old test is rewritten rather than deleted so
the change in contract is visible in the diff.

**Rule-6 mutants.** (a) Make `admit` refuse a completed identity again and
confirm the resume test fails. (b) Make it return the recorded artifact for an
**uncertain** identity and confirm a separate test fails — the mutant that
proves the retained prohibition is still guarded. (c) Remove the span-scoping
in limb (a) and confirm the per-stage `inputBytes` assertion fails.

### Slice 7 (deferred) — The drift band

Not designed here. It is L3-M8's third limb, absent from the dossier's own
What bullet and Slices list, and its mapping is done in Gate 5 so the gap is
recorded. It needs the retained-evaluation store M12 (L2-M6) proposes, and
building a second one would be the duplication AGENTS.md warns about. Re-enter
this funnel once slice 1 has landed, because a drift band's unit is "N of M
cited sources changed" and that sentence has no referent until citations are
identities.

### Design bar for the human surface

Only slices 1 and 4 reach a rendered surface. The bar: a citation must be a
link whose destination is stable under any reordering of the input, and an
excluded or path-only source must appear in the source list as a visible,
explained absence at the place its text would have been — never a missing
element, never a page-wide disclaimer. That is the treatment the PWB renderer
already gives an Unknown, and these slices copy its vocabulary rather than
inventing one.

## Gate 5 — Specification

The specification in force is the predecessor composed with the
understanding-amendment overlay, effective composition **31 requirements and
177 scenarios** (understanding act, Scope paragraph). Requirements 006 and 014
are cited at the overlay with the predecessor line beside them, and so is 009;
003, 008, 010 and 020 are not among the seven amended, so for those four the
predecessor is cited. [Superseded 2026-09-15, review 1 F4: this sentence read
"003, 008, 010, 020 and 009 are not among the seven amended, so the
predecessor is cited", which is false about 009. The understanding act's Scope
paragraph —
`.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`
lines 29–30, inside the paragraph at 28–32, read at source this session —
names "REQ-polaris-generation-002, 004, 006, 009, 012, 014 and 019". The
packet's *practice* was already right: its only REQ-009 citations are at the
overlay, the requirement heading at overlay line 241 and its text at 243, both
opened this session.]

### Does the observation source type need a spec delta? (Q1)

**No for the type; the whole question is the conformance claim.** The clause
the type serves is quoted whole,
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
line 98, at the two sentences that bind it:

> The asset bundle SHALL distinguish source claims, supported inference and
> non-normative framing and preserve captured epistemic states. Source anchors
> SHALL use the closed classes and durable revision/evaluation-bound
> identities required by RFC7-10, not labels or paths as identity.

And RFC7-10 is quoted whole at its defined identifier (`DIRECTIVE-REGISTER.md`
names it at `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`
line 204), both paragraphs, with no elision:

> **RFC7-10 — Anchor form.** A source anchor is machine-readable and typed:
> **(target class, target identifier, optional fragment, target state)**,
> target class one of: a **kernel entity reference** (selection reference per
> RFC6-1, optionally evaluation-qualified); a **doctrine rule or
> accepted-contract citation** (stable identifier `VIS-n`/`SEC-n`/RFC clause,
> rendered per RFC6-20); an **`openspec/**` anchor** (RFC3-28); a **decision
> or policy identifier**; or an **evidence artifact identifier** with
> integrity digest. No target class exists for narrative content, renderings,
> or editorial drafts (RFC7-3). Anchors embed durable identifiers, never
> labels, paths, or coordinates (RFC6-8/9).
>
> **The target-state component** records what the target said when the anchor
> was authored: for a declared or normative artifact (doctrine rule, accepted
> contract clause, `openspec/**` requirement or scenario, decision, policy,
> evidence artifact), its **revision**; for a kernel entity reference, the
> **evaluation identity** at which it was read together with the label + tier
> + reason the reference then carried (RFC6-14's vocabulary, verbatim). It is
> observed at the authoring act and **never rewritten by a later read**. It
> creates no new authority and no new epistemic state (`README.md` §5), and
> exists to enable RFC7-11(a).

**The residue, and it is a genuine owner question.** Slice 1's type carries
everything the second paragraph asks for — a revision as the target state, an
object id as the integrity digest, no label and no path as identity. What it
cannot do on its own authority is decide which of the five target classes a
file inside an observed repository belongs to. The generator's specification
requires the closed classes; the adopted registry declares a sixth identity
scheme; both are bound bytes and neither may be edited to agree. That is Q1,
and the packet does not choose for the owner.

### The RFC2-26 test, run over all seven slice rows

RFC-0002 is an accepted design contract in force. Its phase rule is quoted
verbatim at the defined clause,
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` lines
196–221, under the `###` heading "Authority boundary at the OpenSpec seam
(binding phase rule)" at line 194 — **the whole clause, both paragraphs**,
with no elision:

> **RFC2-26.** This contract schedules nothing: **it is not a specification of
> record from which implementation work may be scheduled**. No implementation
> work for user-observable consequences of this contract — evaluation and
> snapshot displays, claim and challenge rendering, Unknown-reason and
> rendering-tier presentation, reconciliation-chain and gap surfaces, API
> answers over epistemic state — may be scheduled solely from this RFC. Before
> implementation, every observable consequence either maps to an approved
> OpenSpec requirement and scenario in the governance root's `openspec/**`
> plane, or carries a reviewed N/A judgment proving it purely structural with
> no independently testable behavior. **The reviewed N/A judgment's home and
> gate.** A reviewed N/A judgment is a recorded owner judgment homed in
> `decisions/` (RFC3-15), and the judgment is honored only through an
> effective owner act under RFC3-16(a), in state (1) or state (2), with that
> state rendered; absent or invalid acts map nothing and leave the consequence
> unmapped and Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2).
>
> **Rows are per observable consequence, not per clause.** A clause with five
> observable consequences and one mapped requirement is not covered; the
> matrix discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of
> the matrix. At surface specification a clause-to-requirement coverage matrix
> over RFC2-1..RFC2-26 is produced — **that matrix is review material, never
> authority**. This clause creates no OpenSpec content now (none may exist
> during bootstrap). This clause binds the whole RFC 0002 package, not this
> module alone. (Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52,
> RFC10-16, RFC11-12.)

**The denominator is seven**: the seven slice rows of Gate 3's topology table,
slices 1 through 7 [Observed, counted this session over that table]. Every
requirement and scenario cited below was read at source this session in the
composed specification.

| Slice | RFC2-26 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Observation-typed sources | "claim and challenge rendering" (the citation is a rendered link); "Unknown-reason and rendering-tier presentation" (an excluded or path-only source renders as a visible Unknown) | **REQ-polaris-generation-003**, base line 98, scenario **"Aligned human and machine views"** at base lines 105–109, quoted verbatim: "**WHEN** a bundle is rendered for a reader and queried by a machine / **THEN** both views identify the same blocks, source anchors, captured states, reading structure and editorial-draft state / **AND** generation provenance identifies the model, version, policy and input snapshot". Also scenario **"Unsupported or surplus anchor"** at base lines 111–115, whose THEN reads "the bundle records a fidelity finding and cannot become ready for owner adoption" | **Available**, on two requirement-and-scenario pairs from the same requirement |
| 2 Structural independence | **None enumerated with confidence.** The change is to which keys a provider envelope carries and to what a receipt records. Whether a receipt naming the reviewing route is an "API answer over epistemic state" is a reading this packet does not make [Inferred] | **REQ-polaris-generation-006**, overlay line 180 (base 302), on the clauses "Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation" and "The candidate-authoring stage SHALL NOT define or narrow its own review denominator". Nearest scenarios: **"Source trade-off omitted entirely"** at overlay lines 199–203 and **"Omitted material qualification"** at 205–212. **Neither names the envelope-contents case**, which is slice 2's actual subject [Observed: all five REQ-006 scenario headings were read this session — overlay lines 187, 193, 199, 205 and 214 — and none states it]. The nearest scenario anywhere is **REQ-polaris-generation-014**'s **"Shared model blind spot"** at overlay lines 409–414, whose THEN and AND read "the external evaluation fails it using the frozen source-derived oracle" and "additional agreeing model verdicts do not override the missing support" — which is about the *external evaluation* catching the failure, not about preventing it at the envelope | **Requirement available, scenario partial.** The clause's bar is "an approved OpenSpec requirement **and** scenario". This packet calls slice 2 neither lawful nor unlawful on that; it records the two repair routes the clause itself names: a scenario added through CC-REV-2, or a reviewed N/A judgment homed in `decisions/` and honored only through an effective owner act under RFC3-16(a). This packet's view of the second: **probably reachable here**, because the change is a narrowing of an input envelope with no user-visible consequence of its own once the receipt limb is separated out — and separating it is cheap [Inferred; the clause naming the route is Observed, whether slice 2 fits it is a reading] |
| 3 Self-corpus proof | **None enumerated.** A local operator run producing an evidence record renders nothing and answers no query over epistemic state | **REQ-polaris-generation-014**, overlay line 367 (base 755), scenario **"Narrow evidence offered as completion"** at overlay lines 380–384, quoted verbatim: "**WHEN** only synthetic provider runs, a Butlers-specific page or unchanged golden artifacts are available / **THEN** the completion report marks real generation, regeneration and reader-quality requirements unproven / **AND** no test score or successful provider response is substituted for that missing evidence". Also **"Unfamiliarity without project-specific patching"** at overlay lines 392–399, whose THEN requires the evaluation to record "input/profile differences and actual reader outcomes without manually fixing generated content or adding project branches" | **Available**, and the first of the two is what *bounds* the slice's claim rather than authorizing it. The clause is not otherwise engaged |
| 4 Draft route and drafted act | "API answers over epistemic state" (a machine-credentialed route serving a draft and its receipts); "claim and challenge rendering" (the rendered preview) | **REQ-polaris-generation-020**, base line 1083, scenario **"First request needs approval"** at base lines 1089–1093, whose THEN reads "the application prepares the Proposal and bounded effect plan from admitted metadata, names missing approvals and lets the owner complete the existing gates without assembling records manually" and whose AND reads "neither a provider call nor an unconsented persistent write is used to bootstrap that approval". Also **REQ-polaris-generation-010**, base line 528, scenarios **"Valid act"** at base lines 535–539 and **"Invalid or partial act"** at 541–545, the latter's THEN reading "unattested blocks remain editorial-draft and the invalidity is visible" | **Available** on both requirements. Note that REQ-020's AND is the clause Q4's recommended arm satisfies by writing nothing at all |
| 5 The egress act, named | **None enumerated.** One documentation step and one status sentence; nothing rendered on a governed surface, nothing queried | n/a | n/a. Argued from SEC-2 directly |
| 6 Stage-scoped inputs and resume | **None enumerated.** Budget accounting and admission control are internal to the controller | **REQ-polaris-generation-008**, base line 400, scenario **"Resume valid work"** at base lines 407–411, quoted verbatim: "**WHEN** a stopped run has valid completed checkpoints and effective permissions / **THEN** resume reuses those stages and records which work was reused and newly dispatched / **AND** the remaining original budget is respected". Also **"Duplicate or ambiguous dispatch"** at base lines 413–417, whose AND reads "different run identities cannot overwrite each other's artifacts" | **Available.** The first scenario is the one the landed port contract cannot satisfy, which is Q5's whole content |
| 7 (deferred) Drift band | **[Unknown].** Not designed, so its observable consequences are not enumerated and the test cannot honestly be run over it | The mapping that *would* apply, recorded so the deferral does not lose it: **REQ-polaris-generation-009**, overlay line 243, scenario **"Changed source"** at overlay lines 250–254, whose THEN reads "Polaris identifies the affected stale presentation and offers a newly bound generation run" and whose AND reads "the old review and authorship act are not transferred to the new candidate" | Deferred, not run |

**What the test establishes and what it does not.** It establishes [Observed]
that slices 1, 3, 4 and 6 map to named requirement-and-scenario pairs in the
composed specification; that slice 2's requirement is named and no scenario
states its case; and that slices 3, 5 and 6 enumerate no consequence of
RFC-0002 at all. It does **not** establish that any slice is lawful: that is
Q1 through Q5's, and RFC2-26's own scope sentence — "This clause binds the
whole RFC 0002 package, not this module alone" (lines 219–220) — is a reading
the owner may take more or less broadly than this packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed spec text and nothing here amends a requirement.

**S1 (slice 1).** WHEN the source array handed to `renderDraftPreview` is
shuffled, THEN every rendered citation href is byte-identical to the
unshuffled render, AND a renderer that cites by array position fails this
test.

**S2 (slice 1).** WHEN a source is admitted with
`classificationBasis: 'path-only'`, THEN it appears in the corpus and in the
rendered source list as an explained absence with no quotable span, AND it is
counted in the inventory stage's denominator rather than dropped before the
stage sees it.

**S3 (slice 1).** WHEN one character of a source's `objectId` changes, THEN
that source's citation identity changes, AND no other citation on the page
moves.

**S4 (slice 2).** WHEN the `fidelity` stage's envelope is canonically encoded,
THEN it contains no plan section handle, AND the assertion is made on the
encoded bytes rather than on the prompt text.

**S5 (slice 2).** WHEN a run supplies a different route for the `fidelity`
stage than for `author`, THEN both dispatches carry their own route and the
receipts distinguish them, AND a run supplying one route for every stage
behaves exactly as today.

**S6 (slice 3).** WHEN the unchanged pipeline is run over Syzygy's own
105-file governed corpus — the file count at `a9f671e` and unchanged at
this commit, though its byte total is not (anchor added 2026-09-15,
review 2 G5(b)) — with a scripted responder, THEN the recorded evidence
names every budget and cap breach it hit, AND it states in the specification's
own words that real generation, regeneration and reader-quality obligations
remain unproven.

**S7 (slice 3).** WHEN one governed source file is changed and the run is
repeated, THEN exactly the blocks and citations bound to that source's
identity differ, AND a check that compares only counts is not sufficient.

**S8 (slice 4).** WHEN the owner accepts two of a draft's three claim blocks,
THEN the emitted packet carries exactly two per-block attestations keyed to
those block ids and names the third as unattested, AND no file is written and
no recorder perform path is called.

**S9 (slice 5).** WHEN the kit's start path or `PROJECT-STATUS.md` is read,
THEN the egress act is named with what it buys and what it does not, AND the
assertion that checks this matches a distinctive full clause rather than the
word `egress`.

**S10 (slice 6).** WHEN a run is stopped at `fidelity` and re-run under the
same request identity, THEN the send count rises by exactly one, AND an
in-flight or uncertain attempt identity still refuses.

## Collision and sequencing

**This is the one packet of the seven whose file-set intersection with a
sibling is not zero, and the number is eleven.** Method, stated once: extract
every code span from each sibling's packet file and keep those that resolve as
a real **file** in this worktree (`os.path.isfile`); intersect with M7's own
**27-file touch-set**. **The two intersection columns below are taken under
exactly that membership predicate; the two span columns are not** — they
keep the first draft's additional prefix filter (a span must also begin
`apps/`, `packages/`, `scripts/`, `docs/polaris-generation/` or be
`package.json`), and they are left under it because that is what the
published figures were measured with. The membership count is printed
beside each of them so the stated method re-derives [clarified 2026-09-15,
review 2 G8: the method paragraph and the supersession note below said the
prefix filter "is dropped in favour of membership" without saying that the
span columns were not recomputed, so a reader re-running the stated method
got different numbers in one of the six columns. Both sweeps were re-run
over all nine siblings 2026-09-15: the published 1 / 0 / 11 / 13 / 22 / 9 /
13 / 51 / 13 reproduce **only** under the prefix filter, and under membership
the counts are 4 / 9 / 25 / 28 / 39 / 20 / 30 / 74 / 37 at the heads the rows
name (M8 is 75 at its current head `bce9039`). The two intersection columns
are correct under membership: the 24-column is identical under both
predicates for all nine, and the 27-column differs at **M4** (1 rather than
2) and **M9** (2 rather than 3) under the prefix filter, because no prefix
reaches `PROJECT-STATUS.md` — which is the reason the filter was dropped for
the intersections]. That set is the 24-file candidate surface — everything
under `packages/polaris-generation-core/src` and
`apps/three-surface-poc/src/polaris-generation`, everything under
`docs/polaris-generation`, plus `apps/three-surface-poc/src/routes.ts`,
`packages/polaris-generation-core/README.md` and `package.json` — **plus the
three paths Gate 3's topology table names that the 24 excludes**:
`PROJECT-STATUS.md` (slice 5),
`packages/three-surface-poc-core/src/project-shape-observation.ts` (slice 4)
and `apps/three-surface-poc/src/polaris-source.ts` (slice 1). Every head in
the table below was read 2026-09-15 in that sibling's own worktree, read-only.
[Superseded 2026-09-15, review 1 F7: the intersection was taken over the
24-file surface only, and the span filter additionally kept only spans
beginning `apps/`, `packages/`, `scripts/`, `docs/polaris-generation/` or
`package.json` — a prefix filter that can never reach `PROJECT-STATUS.md`. The
24-file figures are kept below as the first draft's surface, because that is
what the published rows measured; the 27-file column is the packet's own
touch-set and is the one a reader should use. The prefix filter is dropped
**for the intersections only**; the two span columns are still taken under
it, as the paragraph above now states — amended 2026-09-15, review 2 G8.]

| Sibling | Head read 2026-09-15 | Prefixed spans (first draft's prefix predicate) | Resolving as files, prefix predicate (membership count in brackets) | Intersection with M7's 24 (first draft's surface) | Intersection with M7's 27-file touch-set |
|---|---|---:|---:|---:|---:|
| M1 (lane A, on main) | `a9f671e` | 3 | 1 (4) | **1** | **1** |
| lane B, PR #35, P-68 | `4090f98` | 2 | 0 (9) | **0** | **0** by code span; **1** (`PROJECT-STATUS.md`) under its stronger diff predicate — see below |
| M2, PR #36, P-69 | `f2f37dd` | 19 | 11 (25) | **1** | **1** |
| M3, PR #37, P-70 | `6574600` | 15 | 13 (28) | **0** | **0** |
| M4, PR #38, P-71 | `63b8e33` | 31 | 22 (39) | **1** | **2**, adding `PROJECT-STATUS.md` |
| M5, PR #39, P-72 | `ba9ca61` | 11 | 9 (20) | **1** | **3**, adding `apps/three-surface-poc/src/polaris-source.ts` and `packages/three-surface-poc-core/src/project-shape-observation.ts` |
| M6, PR #40, P-73 | `83c9f60` | 26 | 13 (30) | **11** (a floor — see the `pipeline.ts` row below) | **11**, the same eleven |
| M8, PR #41, P-74 | `4b2e8cb` | 61 | 51 (74) | **4** | **6**, adding the same two as M5 — see the M8/M9 paragraph below |
| M9, PR #43, P-75 | `3e764d8` | 22 | 13 (37) | **2** | **3**, adding `PROJECT-STATUS.md` |

**Lane B's row, and why its predicate differs.** Lane B's packet is a
governance amendment rather than a design funnel, so its spans were taken from
its semantic delta and its owner-decision packet, both under
pwb-scoped-attributes-amendment in the contract-candidates tree — named here
without code spans because they exist only on lane B's branch and CG-1b
requires every code-span path to resolve in this worktree. A second, stronger
predicate is available for lane B and for no other sibling, because lane B has
actually committed implementation-plane changes:
`git diff --name-only a9f671e HEAD` in its worktree names **3**
implementation-plane files — `scripts/check_governance.py` and two scripts
that exist only on its branch, named here without code spans because they do
not resolve in this worktree and CG-1b requires every code-span path to
resolve. **Under the code-span predicate the intersection with M7's surface is
0 on both the 24-file and the 27-file set.** Under the stronger diff predicate
it is **0** against the 24 and **1** against the 27: lane B's branch modifies
`PROJECT-STATUS.md`, which is M7 slice 5's second file [Observed, both
predicates recomputed 2026-09-15]. The practical risk is nil — lane B's two
hunks land at `PROJECT-STATUS.md` lines 252 and 263, and M7 slice 5's target
paragraph is at lines 38–44, both read at source this session — but the
published claim is a file-set claim and now reads as one. [Superseded
2026-09-15, review 1 F7: this read "**The intersection with M7's surface is 0
under both predicates**", true only of the narrower 24-file surface.] The
other **eight** siblings — M1, M2, M3, M4, M5, M6, M8 and M9 — have
committed **0** implementation-plane files, so for them the code-span
predicate is the only one available [Observed,
`git diff --name-only a9f671e HEAD` run 2026-09-15 in each of the eight
sibling worktrees at the head named for it; M1 is on main at `a9f671e`
and has no diff, and
M2, M3, M4, M5, M6, M8 and M9 each name only the register, their own
`docs/design` packet, their own `docs/evidence` record and their own
retained raws. Denominator eight. This read "The other six siblings"
until 2026-09-15, review 2 G7: it was counted when the collision table
had seven rows and went stale when the table grew to nine].

**The single-file intersections are all
`apps/three-surface-poc/src/routes.ts`, and three of the four are real.** M1's
packet says in terms that "The core package, the observation pipeline, the
registry ceiling and `routes.ts` are not touched" — a sentence that begins on
line 143 and ends on line 144 of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`
— so its row is a citation, not a claim. M2's Gate 3 puts `routes.ts` in slice
3's "Lives in" column; M4's Gate 3 puts it in slice 5's; M5's Gate 3 puts it
in slices 1 and 3's, slice 3 adding a new route; M8's Gate 3 puts it in slice
2's; M9's Gate 3 puts it in slices 2, 4a and 6's. **Six packets including this
one propose editing the same 240-line file** — M2, M4, M5, M7, M8 and M9 — and
M5's slice 3 and M7's slice 4 propose adding a route and a
`ResponseLimitIdentity` to the same two places [Observed, all six Gate 3
tables read at source 2026-09-15 at the heads in the table above]. [Superseded
2026-09-15, review 1 F8: this read "**Four packets including this one propose
editing the same 240-line file**" and "all four Gate 3 tables", counted before
M8 and M9 had committed.]

**The eleven-file intersection with M6, slice by slice.** These are the same
bytes, not merely the same directory, and M7 sequences behind M6 rather than
beside it.

| M7 slice | Depends on | Shared files | The P-73 ruling that gates it |
|---|---|---|---|
| 1 Observation-typed sources | **M6 slice 2** (asset disposition), which rewrites the same schema declarations and the same preview renderer | `packages/polaris-generation-core/src/provider-draft.ts`, `packages/polaris-generation-core/src/provider-draft.test.ts`, `apps/three-surface-poc/src/polaris-generation/draft-preview.ts`, `packages/polaris-generation-core/src/index.ts` | **P-73 Q1.** If the owner rules the disposition field an amendment, M6 slice 2 holds behind CC-REV-2 and M7 slice 1 should land **first** rather than wait, because its own clause is unaffected — the one ordering this packet recommends changing under that arm |
| 2 Structural independence | **M6 slice 4** (edit/repair accounting), which threads the prior draft into the same call sites at `pipeline.ts` 259–269 | `packages/polaris-generation-core/src/pipeline.ts`. **This file is invisible to the intersection predicate above** and is named here anyway: M6 cites it **10** times as the bare span `pipeline.ts` and **0** times at its full path, and the predicate keeps only spans beginning `apps/`, `packages/`, `scripts/`, `docs/polaris-generation/` or `package.json` [Observed, both counted this session]. So the published 11 is a floor, not a ceiling, and this row is the one file the sweep would have missed | **P-73 Q6.** M6 slice 4 is the one M6 slice whose clause is overlay-only and which P-73 recommends ruling explicitly. M7 slice 2 does **not** inherit that gate — its clause is predecessor text — but it inherits the merge conflict. Land whichever is ruled first; the second rebases |
| 3 Self-corpus proof | **M6 slice 1** (the onramp), because the run needs the demo chain to build from a clean install | `package.json`, `packages/polaris-generation-core/README.md` | **None.** P-73 Q5 classifies the onramp as a cost trade-off the owner may delegate, and P-73's default lands the install line |
| 4 Draft route and drafted act | nothing in M6 | none | **None from P-73.** Gated by P-72 (Q3) and P-71 (Q4) |
| 5 The egress act, named | **M6 slice 5** (the boundary restated in `AUTHORING.md` and `ARTIFACTS-AND-TOOLS.md`) — same sentence family, different files and different sites | `docs/polaris-generation/README.md`, `docs/polaris-generation/AUTHORING.md`, `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`, `docs/polaris-generation/example.json` | **None.** M6 slice 5 restates *that* egress is not granted at the two prompt-holding sites; M7 slice 5 names *which act would grant it* in the start path. Land M6 slice 5 first and make M7 slice 5's step point at it rather than repeat it |
| 6 Stage-scoped inputs and resume | **M6 slice 4** again, same call sites | `packages/polaris-generation-core/src/pipeline.ts` | **P-73 Q6**, for the same merge reason as slice 2. Limbs (a) of slice 6 and the envelope construction of slice 2 are one refactor and should be one change |

**Sequencing inside M7.** Slice 5 is independent of everything and may land
first; it is also the cheapest. Slice 1 is the change the rest rests on —
slice 3's perturbation check and slice 7's drift band both need identities
before they mean anything, and slice 4 would otherwise render positional
citations on a route. Slices 2 and 6(a) are one refactor and should be one
change. Slice 6(b) is independent of both and gated by Q5. Slice 3 follows
slice 1 and Q2. Slice 4 follows Q3 and Q4, and should follow slice 1 for the
reason above.

**The shared governance file.** All eight sibling packets add a row to
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`: P-68 (lane B), P-69
(M2), P-70 (M3), P-71 (M4), P-72 (M5), P-73 (M6), P-74 (M8) and P-75 (M9),
each present only in its own worktree's register [Observed, counted 2026-09-15
with the predicate `^| P-` over the nine worktrees' registers]. **The first
draft wrote exactly two files and no register row**, by instruction: the row
lands after review 1, batched. It landed 2026-09-15 as **P-76**, on this
branch. [Superseded 2026-09-15: this paragraph named six sibling rows, said
"this worktree's register ends at P-53, as do M8's and M9's", and said "The
next free number at the time of writing is P-74, but whoever files it should
re-derive it rather than trust this sentence, because M8 and M9 are being
drafted in parallel and may file first." They did file first — M8 took P-74
and M9 P-75, each on its own branch — so P-76 is this packet's number,
re-derived this session and not trusted from that sentence.]

**The two other P2 packets drafted in parallel have since committed, and their
intersections are measured rather than assumed.** M8 (portability — the
profile as a loaded, digest-bound registry input) is at `4b2e8cb` and M9 (one
identity, one epistemic shape, one vocabulary across the surfaces) at
`3e764d8`, both read read-only in their own worktrees 2026-09-15. **M8
intersects M7's 24 at 4** — `apps/three-surface-poc/src/routes.ts`,
`docs/polaris-generation/README.md`,
`docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` and `package.json`, two of
which are M7 slice 5's own files — and **at 6 over the 27-file touch-set**,
adding `apps/three-surface-poc/src/polaris-source.ts` and
`packages/three-surface-poc-core/src/project-shape-observation.ts`. **M9
intersects at 2** — `apps/three-surface-poc/src/routes.ts` and `package.json`
— and at **3** over the 27, adding `PROJECT-STATUS.md` [Observed, all four
figures computed 2026-09-15 at those heads under the method above]. The one
named overlap stands: M8 carries L1-M5, the observer self-profile, which slice
3 should share rather than duplicate. [Superseded 2026-09-15, review 1 F8:
this paragraph read "Both worktrees are at `a9f671e` with no commits, so no
intersection can be computed against them. They are disjoint from M7 by design
— M8's subject is the observer's profile and M9's is the rendered surfaces'
vocabulary". The first sentence was true when written and is not now; the
second was an unlabeled substantive claim and is false as a file-set claim.
The `could_not_verify` entry in the evidence record covered it honestly; the
prose did not, and a later reader reads the prose.]

**Lane B edits `scripts/check_governance.py`.** M7 does not, but M7's two
files must pass it, and lane B's branch changes it. The order that avoids a
surprise is: lane B lands, then this packet's check is re-run before merge. At
this commit the check passes in this worktree (Gate 6).

**Not verifiable this session.** [Unknown] Whether the sibling branches'
actual diffs stay inside the paths their packets cite, until they land —
**seven of the eight** have committed no implementation file at all, lane
B being the one that has [Observed, eight diffs run 2026-09-15;
denominator the eight sibling branches. This read "five of the six" until
2026-09-15, review 2 G7, having been counted when the collision table had
seven rows]. [Unknown] Which arm
the owner takes on P-72's Q1, on which slice 4's route depends entirely.
[Unknown] Whether M8 or M9 will claim any file in M7's 24. [**RESOLVED
2026-09-15**, review 2 G6: answered by the measured rows twenty lines above —
M8 claims **4** of the 24 and **6** of the 27, M9 **2** and **3**, recomputed
2026-09-15 at both the heads this packet names and the siblings' current
heads. The evidence record's twin entry was marked resolved in the same
pass and this sentence was left behind.]

## Gate 6 — Engineering bar

1. **Every count in this packet carries its predicate and its denominator**,
   and every one was taken this session in the worktree at `a9f671e`. The
   per-stage byte figures are computed by running the unchanged pipeline
   through a capturing port, not read off the source; the envelope-contents
   table is computed by parsing each encoded envelope at the `generate` port,
   not inferred from the call sites; the self-corpus envelope is a real
   `encodeCanonicalJson` call over real bytes. The literal sweeps that
   corroborate them were run with Python `re`, per verification rule 1.
2. **Two methods for the two load-bearing zeros.** "The planes are disjoint"
   is established both by the literal sweep for `three-surface-poc-core`,
   `PocModel` and `projectShape` over the 20 tracked files, and by the fact
   that `provider-draft.ts`'s source schema has no field that could carry an
   observation identity — the type census in "The two planes" table. "Nothing
   egresses" is established both by the network-primitive sweep and by
   `packages/polaris-generation-core/README.md` lines 38–39, "It has no
   default network client" (rule 2).
3. **The ×5 source re-billing was established by three methods**, not one: the
   key list of each envelope, a sentinel string counted inside each envelope,
   and a padded-corpus slope over three runs. The three agree on the
   structural part and disagree on the fixture-dependent part, which is why
   both figures are published with their scope stated.
4. **Rule-6 mutants are specified per slice and per guard branch**, above;
   each names the predicate to mutate and the fixture that must then fail. The
   two that matter most are slice 1's shuffle test — mutate the renderer back
   to index citations and the test must fail — and slice 6's
   uncertain-identity mutant, which proves the retained replay prohibition is
   still guarded.
5. **Conformance expected values are literals in the tests**, never imported
   from the module under test (AGENTS.md), and slice 5's copy oracle matches a
   distinctive full clause rather than the word `egress`, because a short
   literal is reached by coincidence.
6. **Every claim about a sibling packet was read at source this session** in
   that sibling's worktree at the head named in the intersection table, and
   every intersection figure was computed rather than carried forward. The one
   figure this packet publishes as a **floor** rather than a count — M6's
   eleven — says so at the site, with the predicate blind spot that makes it a
   floor named.
7. **No act-bound byte is proposed for edit.** All **15** paths named in Gate
   3's topology table — every file M7 would touch, including
   `PROJECT-STATUS.md` and the two outside the generation surface — were swept
   against every `*-MANIFEST.txt` row, every `docs/evidence/*manifest*.json`
   and `ACCEPTANCE-ACT-RECORD.md`, over a 21-file manifest population: **0**
   hits for each. That is a claim about *acts* only. Five slice-touched
   implementation files are digest rows of
   `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`,
   whose 17 rows all match current bytes, and landing slices 1, 2, 4 or 6
   obliges a re-run of it — stated in Gate 3.
8. **No observed-repository path is backticked anywhere in this file.** The
   approved repository locator is a hard-coded constant at
   `apps/three-surface-poc/src/git-observation.ts` line 6 and is referred to
   by that citation, never reproduced (CG-1b). No act argument and no signed
   or manifest digest is reproduced; the four digest-bearing records consulted
   are cited by path (CG-7e, CG-15).
9. **Independent review.** This packet has had **two**, each retained
   verbatim and neither overwriting the other:
   `docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md` and
   `docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md`; both
   verdict words, copied exactly, are **CONFIRM WITH EXCEPTIONS**. See
   "Review 1 and repairs (2026-09-15)" and "Review 2 and repairs
   (2026-09-15)" below for the bytes each bound, their counts and the
   disposition of every finding ["This packet has had **one**" until
   2026-09-15, later the same day]. By verification rule 10 review 1
   covers the bytes it names at `0c4b4a9` and not these, so the
   exception repairs made after it are themselves uncovered until a
   second fresh-context review reads them (which has since happened —
   review 2, 2026-09-15, retained at
   `docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md`;
   re-tensed 2026-09-15). [Superseded 2026-09-15: this item read "This
   packet has had **none**. It is a first draft… Its raw would be a file named
   R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md under docs/reviews, written here
   without a code span because the file does not yet exist and CG-1b requires
   every code-span path to resolve." The file now exists and resolves.]
10. **Rule 10 applies to this file.** Any later edit retires a review bound to
    these bytes; superseded wording is to be marked and dated in place, never
    deleted.
11. **Conventions this packet was checked against, this session.** Every
    non-fence line has an even backtick count, so no code span is broken
    across a line break. Over-width lines are counted and enumerated in
    the evidence record under the predicate the published figure is taken
    with: lines outside fenced code blocks whose first non-space
    character is not a pipe, longer than 78 columns, denominator every
    line of this file [restated 2026-09-15, review 2 G12: this read
    "outside fences, tables, block quotes and headings", under which the
    figure is **4** — lines 205, 266, 975 and 986 — rather than the
    published **10**, which also counts the H1 title at line 1 and a
    banner block-quote line at 6. Both predicates were run over this file
    2026-09-15]. Of the distinct code
    spans containing a `/`, the ones that do **not** resolve as a path in this
    worktree are enumerated there too and are each not a path. Re-derived
    after the 2026-09-15 repairs under the same predicate, and again
    after review 2's: **346** distinct spans, **82**
    slash-bearing, **19** not resolving — the same nineteen
    entries, unchanged in membership ["**298** distinct spans, **78**
    slash-bearing" until 2026-09-15, later the same day, when review
    2's repairs added spans; re-derived last over the bytes that carry
    it] — the five write-root
    globs (`.syzygy/**`, `openspec/**`, `apps/**`, `packages/**`, `docs/**`),
    the five route and URL literals (`/api/poc`, `/api/poc/polaris`,
    `/api/poc/briefing`, `/polaris/draft/<runId>`,
    `GET /polaris/draft/<runId>`), the four directory and tree references —
    the RFC2-26 quotation's own `decisions/`, plus `launch-gate/` and `rfcs/`
    from the corrected self-corpus predicate and `docs/evidence/**` — the
    quoted glob predicate `docs/evidence/*manifest*.json`, the two sibling
    branch names (`agent/syzygy-dov.4`, `agent/syzygy-dov.5`), the bare
    `https://` literal from the egress sweep, and the one HTML fragment
    quoted from `draft-preview.ts` line 23 [Observed, re-derived after every
    other edit of this pass. The first draft's figures were 264 spans and 35
    non-resolving, and review 1's F11 found one of those 35 that *was* a path
    — decisions/README.md, written without a code span here and in full at
    slice 5]. The two sibling-branch script paths in the lane-B row remain
    named without code spans for exactly this reason.
12. **The sibling packets' recommended answers are reported, never
    re-litigated.** P-71's Q3 and P-72's Q1 and Q2 are quoted from their own
    files with their own arms; where this packet recommends an arm it says
    which sibling question it is an arm *of*, so the owner rules once.

## Review 1 and repairs (2026-09-15)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the acceptance criteria) is retained
verbatim at `docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md` (33233
bytes, sha256
`93aabafeaf50933c8ff03cfe448bbd5b13a7f289bad872d75a819485f8e85943`, computed
by `wc -c` and `sha256sum` this session, never transcribed). It reviewed
commit `0c4b4a9`, at which the two reviewed files hashed as follows —
recomputed this session with `git show 0c4b4a9:<path>` piped to `wc -c` and
`sha256sum`:

| File reviewed | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` | 109383 | `9465bf5934b91f5d12bd067fc55bbc26511610fb780b97b67dbe81dfb5f12d0f` |
| `docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json` | 28824 | `f44d2f3024784ac4a511ca0576bdd97dbafe2f42c4a5baa385fb79c22632ef57` |

Its verdict word, copied exactly: **CONFIRM WITH EXCEPTIONS**. Its counts, as
the raw states them: **0 blocking, 9 non-blocking, 3 editorial** — twelve
findings, F1–F12.

**Its five-question table, in one line:** all five questions are genuine hard
gates, with Q2 called "the weakest of the five" and Q4 "weakest as a gate" and
the raw's reasons given at each; scope truthful for all five; every
recommendation found to follow from its evidence; every lawful arm named for
Q2 through Q5; **no lawful arm called unlawful anywhere**; no owner trade-off
smoothed into consensus language; every question carrying a
default-if-unanswered, four of the five defaulting to not shipping; and no
question of P-71, P-72 or P-73 re-asked [Observed, read from the retained
raw]. **Two observations in that table are not among F1–F12 and are carried
here rather than applied**, because adding or re-weighting a lawful arm
changes what is put to the owner and is the owner's own reading to make on
P-76: the raw finds a **fourth lawful arm unnamed** for Q1 — rule RFC7-10
**not engaged**, that REQ-003's "source anchors" are the bundle's anchors into
governed artifacts and a provider-side source record is not an anchor in
RFC7's sense, which this packet gestures at ("leaves the specification's own
anchor obligation open") without offering as an arm — and it notes that **Q1's
default is the only one of the five that ships rather than holds**, a
defensible trade-off that the packet does not flag as the least conservative
default it carries. Both stand open before the owner and are named in the P-76
row. **A third observation of review 1's — from its measurements
table rather than its five-question table — is carried here too**: the
sentinel figure 1/2/2/4/4 = **13** re-derives only with the sentinel in
the `mechanism` source; with it in `purpose` the counts are 1/2/2/3/3 =
**11**, because the shipped garden fixture repeats the mechanism text
twice inside the draft and the purpose text once. Both were reproduced
this session against the built package, locally and with no provider
call. The observation moves no arm — `sources` is a key of all five
envelopes either way — and the evidence record's method now names
`mechanism` [added 2026-09-15, review 2 G14, which found this observation
neither applied, carried nor mentioned].

**No recommended answer changed.** Confirmed against the raw's own
five-question table, whose "Recommendation follows from the evidence?" column
answers **Yes** for all five, and against the twelve findings: F1, F2 and F7
correct a denominator or a predicate; F3 restates one computed figure as
approximate; F4 corrects a false sentence about the amendment list; F5 names
the population an arithmetic is over; F6 relabels one claim; F8 replaces an
unlabeled claim with measured rows; F9 re-attributes five fields to their
clauses; F10, F11 and F12 correct anchors, a path and a partition. None moves
an arm, a recommendation or a default's substance. F6 is the one repair that
touches how Q1 *reads*: it splits an `[Observed]` label into the observed part
(the clause names five classes and names none for a file inside an observed
repository) and the `[Inferred]` reading built on it — sharpening the framing
of the question while leaving Q1's recommended arm, its three named arms and
its default exactly as they were [Observed, both sides read this session].

**Every exception was re-derived against source before being applied; none was
applied on the review's say-so.** Eleven of the twelve confirmed, in whole or
with a defect of the finding's own corrected rather than copied. **One did not
confirm and is not applied:** F10 item 3, which says `boundedResponse` is
declared at line 138 and closes at 143 and that the packet's "lines 137–142"
ends one line short. Read at source this session,
`apps/three-surface-poc/src/routes.ts` carries the comment on line 136, the
`export function boundedResponse(` declaration on line **137** and its closing
brace on line **142** — so the packet's citation was already exact and the
review's correction is off by one in both directions. The packet's text is
left unchanged and the reason is recorded here. Two findings carried a defect
of their own: **F2** reports the record's predicate as yielding 107 and reads
its "top-level tracked .md under decisions" as 71, but 71 is the count at
*every* directory level (67 are top-level and four are under `launch-gate/`),
so read strictly as written the predicate gives **103 files / 1,309,493
bytes / 1,301,412 characters / 0 over the cap / largest 63,903**, not
107 — both halves of the phrase were wrong and both are corrected
[restated 2026-09-15, review 2 G4: this read "the predicate gives
**101**, not 107". 101 is 6 doctrine + 67 top-level decisions + the 28
RFC *modules* — the strict reading of one half combined with the
*corrected* reading of the other, which is not what "read literally"
names; the literal reading takes every tracked `.md` under `rfcs/`, which
is 30 at `a9f671e`, and gives 103. All four compositions recomputed at
`a9f671e` from `git ls-tree` blobs 2026-09-15. The adopted 105-file
figures are unaffected]; and **F4**'s anchor names act
lines 29–32, where the sentence listing the seven amended requirements spans
lines **29–30** inside the Scope paragraph at 28–32. Superseded wording is
marked in place and dated throughout, never deleted.

| Finding | Severity | Disposition |
|---|---|---|
| F1 the "20 files" denominator names the wrong set | non-blocking | **CONFIRMED.** `git ls-files` over both spellings this session: `packages/polaris-generation-core/src` + the app directory is **17** tracked files (11 + 6); `packages/polaris-generation-core` + the app directory is **20** (14 + 6). Both sweeps were re-run over both sets: the three plane literals occur **0** times on each, the six network primitives **0** times on each, and the three `https://` hits are the same three test fixtures on each. The denominator is rewritten as "the 20 tracked files of `packages/polaris-generation-core` and `apps/three-surface-poc/src/polaris-generation`" at all seven packet sites and in both evidence fields, superseded wording kept |
| F2 the self-corpus predicate does not yield the 105 it reports | non-blocking | **CONFIRMED in substance, with the finding's own reading corrected.** Three predicates were run this session: the record's words read literally (top-level decisions + every `.md` under `rfcs/`, which is 30 at `a9f671e`) give **103** files / 1,309,493 bytes / 1,301,412 characters / **0** over the cap / largest 63,903, and the top-level-decisions-plus-RFC-**modules** variant gives **101** / 1,206,681 [restated 2026-09-15, review 2 G4: this row attributed the 101 / 1,206,681 figures to the literal reading, which is 103 / 1,309,493; both compositions recomputed at `a9f671e` from `git ls-tree` blobs 2026-09-15]; the review's reading (recursive decisions + every `.md` under `rfcs/`) gives **107** / 1,369,266; the module form (recursive decisions + the `.md` files one directory below `rfcs/`) gives **105** / 1,266,454 / 1,258,724 characters / **0** over the cap / largest 55,836 — the six published figures, exactly. The module form is now stated, at both packet sites and in the record, with the four `launch-gate/` files named and the two single-file RFCs named as out of scope and why |
| F3 the envelope figure does not re-derive from the stated method | non-blocking | **CONFIRMED**, and reproduced eighteen ways rather than four — nine `sourceId` schemes × two reader-question arrays. Over the same 105 files, the same `promptForStage('inventory')`, the same `stageSchema('inventory')` and the envelope `pipeline.ts` line 176 constructs, varying only the `sourceId` scheme and the reader-question array: 1,300,688 / 1,300,601 (repository-relative path), 1,297,209 / 1,297,122 (basename), 1,296,894 / 1,296,807 (stem), 1,298,693 / 1,298,606 (path without its `.syzygy/governance/` prefix), 1,294,916 / 1,294,829 (`source-N`, one-based), 1,294,914 / 1,294,827 (`source-N`, zero-based), 1,294,601 / 1,294,514 (`src-N`), 1,294,391 / 1,294,304 (`s-N`) and 1,294,181 / 1,294,094 (the bare ordinal). **None is 1,294,284**; the nearest is 20 bytes away. The table row is restated as "about 1.29 MB, ± the id and question bytes", the eighteen readings and both free inputs are published in the record, and the ×5 floor is restated on the approximate figure. The limit probe re-derives under all eighteen. [Restated 2026-09-15, review 2 G3: this row read "reproduced twelve ways", "the twelve readings" and "all twelve"; the data published beside the sentence is nine `sourceId` schemes each at two reader-question arrays, i.e. **18** encodings, all eighteen of which review 2 reproduced byte for byte] |
| F4 Gate 5's opening sentence is wrong about REQ-009 | non-blocking | **CONFIRMED**, with the anchor tightened. `.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` lines 29–30, inside the Scope paragraph at 28–32, read "REQ-polaris-generation-002, 004, 006, **009**, 012, 014 and 019 take their full amended clauses and preserved scenarios". "and 009" is struck from Gate 5's not-amended list and REQ-009 is placed with the overlay-cited half. The packet's REQ-009 citations already pointed at the overlay and both resolve: the requirement heading at overlay line 241 and its text at 243, opened this session |
| F5 "four envelopes, not six" reconciles with nothing else | non-blocking | **CONFIRMED.** The four are the envelopes that carry the `plan` today — `author`, `edit`, `fidelity` and `repair`, the last because `pipeline.ts` line 267 hands `repair` the accumulated `context` [read at source this session]. The population is now named at the site and reconciled with Gate 4's "exactly two envelopes change" — of the four, `fidelity` and `repair` lose the plan and `author` and `edit` keep it. Superseded wording marked |
| F6 Q1's `[Observed]` label carries the inference the owner is asked to make | non-blocking | **CONFIRMED**, and split rather than merely relabelled. The observed part is stated exactly — RFC7-10 names five target classes and names no class for a file inside an observed repository — and the conclusion that such a file falls outside all five is carried as `[Inferred]`, the reading Q1 puts to the owner. Mirrored in the P-76 register row. Per AGENTS.md §Epistemic and change discipline, an LLM assertion is Inferred |
| F7 the collision surface is narrower than the packet's own touch-set | non-blocking | **CONFIRMED**, and the whole table recomputed at each sibling's current head (lane B `4090f98`, M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`, M6 `83c9f60`; M1 on this worktree's tree at `a9f671e`). The touch-set is restated as **27** — the 24 plus `PROJECT-STATUS.md`, `packages/three-surface-poc-core/src/project-shape-observation.ts` and `apps/three-surface-poc/src/polaris-source.ts` — and the prefix filter is dropped in favour of membership **for the intersections**, because no prefix can reach `PROJECT-STATUS.md`. [Amended 2026-09-15, review 2 G8: the filter is dropped for the two intersection columns and **not** for the two span columns, which still carry the first draft's prefix-filtered figures; both predicates were re-run over all nine siblings 2026-09-15 and the membership counts are now printed beside the span column. Under the prefix filter the 24-column is unchanged for all nine and the 27-column would read M4 1 and M9 2, because no prefix reaches `PROJECT-STATUS.md`.] Over the 27: M1 1, lane B **1** under its diff predicate (`PROJECT-STATUS.md`, hunks at lines 252 and 263 against M7 slice 5's target at 38–44, both read at source) and 0 by code span, M2 1, M3 0, M4 **2**, M5 **3**, M6 11. The 24-file figures are kept as the first draft's surface |
| F8 "disjoint from M7 by design" is unlabeled and is now false | non-blocking | **CONFIRMED**, and both rows measured at heads later than the ones the review read. **M8** at `4b2e8cb` (past the `8035c8f` the review saw): **4** against M7's 24 — `apps/three-surface-poc/src/routes.ts`, `docs/polaris-generation/README.md`, `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`, `package.json` — and **6** against the 27. **M9** at `3e764d8` (past `206d775`): **2** against the 24 — `routes.ts` and `package.json` — and **3** against the 27. The sentence is replaced by the measured rows with the superseded wording kept and dated, and the claimant count for that one 240-line file is restated from four to **six** (M2, M4, M5, M7, M8, M9), each read in its own Gate 3 table this session. Mirrored in the record by same-line marking plus an appended resolved key |
| F9 slice 5's five fields are not "taken field for field from SEC-2" | non-blocking | **CONFIRMED.** `.syzygy/governance/doctrine/security.md` lines 25–37, read at source this session, name **two** of the five: the providers permitted for a governed project and the content classes that may be sent. Refusal-on-withdrawal is REQ-001's, at base line 12, which the packet already cited correctly. Route and retention are attributed to this packet's own proposal and labelled `[Inferred]`. Superseded "field for field" wording marked |
| F10 five anchor and quotation imprecisions | editorial | **FOUR CONFIRMED, ONE NOT.** (1) `identityScheme` is on registry line **54** and `"class": "git-tree-entry"` on 53 — corrected at both sites, with the literal-sweep hit left at 53 where it belongs. (2) `EXECUTION-PHASES.md`'s sentence begins on line **13** and ends on 14 — corrected at both citations. (3) **NOT CONFIRMED:** `boundedResponse` is declared on line **137** under its comment at 136 and closes at **142**, so the packet's "lines 137–142" was already exact; not applied, reason recorded above. (4) the dropped closing fragment — the bracketed ordinal and the anchor's own end tag — is restored to the `draft-preview.ts` line 23 quotation. (5) REQ-008's sentence begins with a capital "An" at base line 400 — the packet's mid-sentence lowercase is marked "[a]n" |
| F11 one code span reads as a file path and does not resolve | editorial | **CONFIRMED.** The span decisions/README.md — written here without backticks for the reason it names — resolves only as `.syzygy/governance/decisions/README.md`, which exists in this worktree; written in full at slice 5, and the record's note that "none is a file path this packet cites" is corrected rather than left standing over an entry it was false for |
| F12 slice 5's `tasks.md` §3 partition omits 3.4a | editorial | **CONFIRMED.** §3 carries **seven** boxes — 3.1, 3.2, 3.3, 3.4, **3.4a** (line 49), 3.5, 3.6 [enumerated this session]. 3.4a, "Apply DESIGN-ACCEPTANCE.md to the full rendered reading, including the owner's reported failures", is an actual-generated-artifact obligation and is named on the **buys** side, with the partition stated as over all seven |

**Registered as P-76.** The five questions are registered in
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` on this branch, as
the row the first draft said would land after review 1. P-68 (lane B), P-69
(M2), P-70 (M3), P-71 (M4), P-72 (M5), P-73 (M6), P-74 (M8) and P-75 (M9) each
live only on their own branch, and this packet sequences behind M6's P-73.

By verification rule 10, review 1 binds the bytes it names — the two digests
in the table above, at commit `0c4b4a9` — and not these. Every edit in this
section and above was made after it, so **the eleven applied exception
repairs — and the recorded decision not to apply the twelfth — are uncovered
until a second independent fresh-context review confirms them** (which
has since happened — review 2, 2026-09-15, retained at
`docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md`; re-tensed
2026-09-15); that raw will be a second `-RAW.md` file, never an overwrite
of the retained one. Subject to that, and on review 1's confirmation of
the `0c4b4a9` bytes —
CONFIRM WITH EXCEPTIONS, no blocking finding, no recommended answer moved, all
five questions found to be genuine gates and no lawful arm called unlawful —
**this packet stands at the owner gate**: P-76 is ready to be ruled, with the
two unapplied observations above open in front of it.

Over-width lines after these edits, under the predicate "lines outside fenced
code blocks whose first non-space character is not a pipe, longer than 78
columns", denominator every line of this file: **10** [Observed,
measured after all of the edits above. That figure describes the bytes
review 1's pass left, at `1803608`; this pass's repairs have since
changed them, and the current figure is measured last in the review-2
section below. Marked 2026-09-15].

## Review 2 and repairs (2026-09-15)

A second independent fresh-context review of the once-repaired packet
(read-only; only the artifact, its governing references and the acceptance
criteria) is retained verbatim at
`docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md` (42736 bytes,
sha256
`772c61f08f4d8b73dfbd040ee140d6371b3e28fc027cd482428bd228ccf29f84`,
computed by `wc -c` and `sha256sum` this session, never transcribed). It
reviewed commit `1803608`, at which the four files it names hashed as
follows — recomputed this session with `git show 1803608:<path>` piped to
`wc -c` and `sha256sum`:

| File reviewed | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` | 139264 | `c45d12c01be340321fbe6286e316cbf1eee4fb9c0129f0b32851dad5008c33bc` |
| `docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json` | 46936 | `668b14a5cd00cceb694fec35f11c3a643c8a5bec4dd5bc306058401d22754e5d` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 34761 | `4ba0e3624d8c68bb5b7200dd6166a48ebeddc743b9b98bdb672b8115ceced5eb` |
| `docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md` | 33233 | `93aabafeaf50933c8ff03cfe448bbd5b13a7f289bad872d75a819485f8e85943` |

Its verdict word, copied exactly: **CONFIRM WITH EXCEPTIONS**. Its counts, as
the raw states them: **0 blocking, 10 non-blocking, 6 editorial** — sixteen
findings, G1–G16, non-blocking G1–G10 and editorial G11–G16.

**Its verification of the review-1 dispositions, carried here as it states
them: eleven REPAIRED over twelve, and F10 item 3's non-application confirmed
correct.** Review 2 opened `apps/three-surface-poc/src/routes.ts` itself and
found the comment on line 136, the `export function boundedResponse(`
declaration on 137 and its closing brace on 142 — so this packet's "lines
137–142" was already exact, review 1's correction was off by one in both
directions, and the close-out's recorded reason matches the bytes. It also
confirms that review 1's own two defects, F2's reading of "71" and F4's
anchor, were corrected rather than copied. **Three of the eleven repairs were
incomplete rather than wrong, and all three are completed here:** **F7** was
repaired in the prose and the two intersection columns but left the two
method columns under the dropped prefix filter (**G8**) and its
evidence-record measurement block untouched (**G9**); **F8** left a resolved
`[Unknown]` standing in the prose (**G6**), left two sibling counts stale
(**G7**) and did not carry its six-packet restatement into the funnel summary
(**G1**); and **F9**'s superseded wording was reinstated unmarked in the
funnel summary (**G2**).

**Every exception was re-derived this session against source before being
applied; none was applied on the review's say-so. Sixteen of sixteen were
confirmed**, one of them with a sub-claim of the finding's own restated
rather than copied: **G8**'s "the intersections are identical under both" is
true of the 24-file column at all nine siblings and **not** of the 27-file
column, which reads M4 **1** and M9 **2** under the prefix filter against M4
**2** and M9 **3** under membership, because no prefix reaches
`PROJECT-STATUS.md` — which is the packet's own stated reason for dropping
the filter for the intersections. Everything else in that finding — the span
columns, the membership counts and all nine intersection pairs — reproduces
exactly. Superseded wording is marked in place and dated, never deleted.

| Finding | Severity | Re-derivation | Disposition |
|---|---|---|---|
| G1 the funnel summary still says four packets edit `routes.ts` | non-blocking | **CONFIRMED.** The summary's Collision line read "routes.ts shared with M2, M4 and M5 - four packets propose editing the same 240-line file", unmarked, while the body says six with the supersession marked and its neighbouring fence lines all carry one. All six re-verified at source this session in each sibling's Gate 3 "Lives in" column at its current head: M2 slice 3, M4 slice 5, M5 slices 1 and 3, M7 slice 4, M8 slice 2, M9 slices 2, 4a and 6 [Observed, all nine sibling packets opened; denominator the nine collision rows] | Applied at the summary line: restated as six, with the superseded four quoted in place and dated, as the neighbouring lines already do |
| G2 the summary reinstates the exact wording F9 superseded | non-blocking | **CONFIRMED.** `.syzygy/governance/doctrine/security.md` lines 30–32 read "Onboarding consent must name the providers permitted for a governed project and the content classes that may be sent" — two of slice 5's five fields, opened at source this session. Gate 2 and slice 5 both carry the repair with the superseded wording marked; the summary restated the superseded claim in five unmarked words | Applied with the raw's suggested phrase — "SEC-2 naming two of slice 5's five fields, the other three attributed at the site" — with the superseded five words quoted in place and dated |
| G3 "twelve reproductions" is eighteen | non-blocking | **CONFIRMED.** The record's `review1.f3_reproduction.bytes_by_scheme` carries **9** keys, each with a `demo_3` and an `empty` array — 9 × 2 = **18** — and the packet prints eighteen values beside the sentence [Observed, the record parsed this session; denominator the nine scheme keys] | Applied at all four packet sites and in the record, by a same-line append inside `review1.disposition_summary.F3` that keeps the superseded word and marks it. The record's `f3_reproduction` values are not edited |
| G4 the "101" attributed to the literal predicate is 103 | non-blocking | **CONFIRMED exactly.** Recomputed at `a9f671e` from `git ls-tree` blobs this session: 6 doctrine + **67** top-level decisions + the **30** tracked `.md` under `rfcs/` = **103 files / 1,309,493 bytes / 1,301,412 characters / 0 over the cap / largest 63,903**. The published 101 / 1,206,681 is 6 + 67 + the **28 RFC modules**, which is the strict reading of one half with the corrected reading of the other. All four compositions run in one sweep; the adopted 105-file figures are unaffected and re-derive exactly | Applied at the review-1 prose and the F2 disposition row, restated as 103 with the superseded attribution quoted and dated, and in the record by two dated sibling keys — a note that the existing key is misnamed, and a `literal_…_2026_09_15` variant carrying the true reading. The review1 key and its values are left unedited |
| G5 two self-referential measurements are falsified by this packet's own register commit | non-blocking | **CONFIRMED, both limbs.** (a) The literal `git-tree-entry` occurs **1** time over the **619** tracked files under `.syzygy/` and `openspec/` at `a9f671e` and **3** at `1803608` — registry line 53 plus the P-76 blockquote at register line 114 and the P-76 row at line 221. (b) The 105-file corpus is **1,266,454** bytes / **1,258,724** characters at `a9f671e` and **1,277,862** / **1,270,122** at `1803608`, with the file count, the cap result and the largest source unchanged [Observed, both sweeps run at both revisions this session from `git ls-tree` blobs] | Applied: Q1's clause now says "1 at `a9f671e`; 3 at this commit, the two additions being this packet's own register row", and the byte figures are anchored at the site at Q2, at the corpus table, at slice 3's corpus paragraph, at its oracle and at scenario S6. The P-76 register row repeats neither figure — the whole register was swept this session for `105`, `1,266,454`, `1,258,724` and the one-time clause, and the row carries none of them — so there was nothing there to mirror |
| G6 a resolved `[Unknown]` left standing in the "Not verifiable" block | non-blocking | **CONFIRMED.** "[Unknown] Whether M8 or M9 will claim any file in M7's 24" is answered twenty lines above it by the measured rows, and the evidence record's twin entry was marked "[RESOLVED 2026-09-15]" in the same pass while the prose sentence was not [Observed, both sites read this session] | Applied: the sentence is marked resolved in place, dated, with the measured figures restated and the rows pointed at |
| G7 two sibling counts went stale when the table grew from seven rows to nine | non-blocking | **CONFIRMED.** `git diff --name-only a9f671e HEAD` run this session in all eight sibling worktrees, heads by `git -C <wt> rev-parse --short HEAD`: M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`, M6 `83c9f60`, M8 `bce9039` and M9 `65de02b` each name only the register, their own `docs/design` packet, their own `docs/evidence` record and their own retained raws; M1 is on main at `a9f671e` and has no diff; lane B `4090f98` is the one branch that also names files under `scripts/` and `.github/`. Denominator eight | Applied at both sites — "the other **eight** siblings", naming them, and "**seven of the eight**" in the Not-verifiable block — with both superseded counts quoted and dated, and the record's first `could_not_verify` entry restated the same way |
| G8 the two method columns do not re-derive under the method the repair states | non-blocking | **CONFIRMED, with one sub-claim of the finding's own restated.** Both sweeps re-run this session over all nine siblings: the published 1 / 0 / 11 / 13 / 22 / 9 / 13 / 51 / 13 reproduce **only** under the prefix filter, and under membership the counts are 4 / 9 / 25 / 28 / 39 / 20 / 30 / **74** / 37 at the heads the rows name (M8 is **75** at its current head `bce9039`; M9 is 37 at both `3e764d8` and `65de02b`). The intersections are **not** identical under both predicates: the 24-column is, for all nine, and the 27-column differs at M4 and M9 because no prefix reaches `PROJECT-STATUS.md`. All nine intersection pairs reproduce under membership at the heads the rows name and at the current heads alike | Applied at the method paragraph, the supersession note, the table header and the F7 disposition row: the two span columns are stated to keep the first draft's prefix predicate, only the intersections use membership, the membership count is printed beside each span figure, and the two cells where the predicates disagree are named. Superseded wording kept |
| G9 the record's `file_set_intersection` block is unrepaired and unmarked | non-blocking | **CONFIRMED.** The block still carries the prefix-filtered 24-file predicate, `m7_surface_size` **24** and **seven** rows with no 27-file column and no M8 or M9 row, while `measurements.plane_disjointness` and `measurements.egress_surface` both took an inline dated correction [Observed, the record parsed this session] | Applied: `predicate` marked in place with a dated bracket and a `superseded_2026_09_15` sibling key added, both routing the reader to `review1.f7_collision_recomputed`. Nothing deleted or overwritten |
| G10 the record's `shared_governance_file` block is false in four respects and unmarked | non-blocking | **CONFIRMED in all four, and the recount reproduces exactly.** All nine sibling registers recounted this session at their own heads under the predicate `^| P-` partitioned by the `##` section: every one holds **27** rows (**22** open + **5** acceptance-act) and carries exactly one row above P-53 — P-68 `4090f98`, P-69 `f2f37dd`, P-70 `6574600`, P-71 `63b8e33`, P-72 `ba9ca61`, P-73 `83c9f60`, P-74 `bce9039`, P-75 `65de02b`, P-76 `1803608` — and main at `a9f671e` gives 21 / 5 / 26. Denominator all nine worktrees | Applied: `touched_by_M7` set **true** and `touched_by` extended to **eight**, each with a dated note key recording what it read, and the three false `disclosure` sentences marked in place and dated with the recount and the nine heads beside them |
| G11 `packet_measured.measured` asserts a currency its own sibling key denies | editorial | **CONFIRMED.** The key reads "after every other edit in this pass, so the figures are true of the bytes they describe" while every value in the block is the first draft's at `0c4b4a9`, and the disclaimer sits at the end of `slash_bearing_note`, a key about a different subject [Observed, the record parsed this session] | Applied: a `describes_commit` key set to `0c4b4a9` on the same line, and a dated clause appended inside `measured` routing the reader to `review1.post_repair_measurements` and to `review2.packet_measured_after_review2`. The values are left exactly as they are |
| G12 the over-width predicate is stated two ways and the published list satisfies one | editorial | **CONFIRMED.** Both predicates run over this file this session: under Gate 6 item 11's words ("outside fences, tables, block quotes and headings") the figure is **4** — lines 205, 266, 975 and 986 — and under the pipe-only predicate it is the published **10**, which also counts the H1 title at line 1 and a banner block-quote line at 6 | Applied: Gate 6 item 11 now names the pipe-only predicate with its denominator, the superseded wording quoted and dated, and `packet_measured.over_width_predicate` takes a dated sibling key recording that it is a third spelling describing the `0c4b4a9` figures |
| G13 the SEC-2 sweep enumerates five network literals where the record says six | editorial | **CONFIRMED.** All six re-run this session over both denominators: `fetch(`, `node:http`, `node:https`, `undici`, `axios` and `XMLHttpRequest` occur **0** times over the 17-file `src`-only set and **0** times over the 20-file package set, and `https://` occurs **3** times on each, the same three test fixtures | Applied: `XMLHttpRequest` added to the enumeration at the Gate 2 site, with the reason and both denominators stated |
| G14 a third review-1 observation is neither applied nor disclosed | editorial | **CONFIRMED, and reproduced without a provider call.** Driving the built package over the shipped garden fixture this session and counting the sentinel in each stage's encoded envelope: with the sentinel in `mechanism` the counts are 1/2/2/4/4 = **13**, and with it in `purpose` 1/2/2/3/3 = **11**, because the fixture repeats the mechanism text twice inside the draft and the purpose text once | Applied: `measurements.stage_envelopes.method` now names `mechanism` by a dated append, and the observation is carried as a **third** unapplied review-1 observation in the review-1 section above and in the record by a dated sibling key beside `review1.raw_observations_outside_f1_f12_not_applied`, which is not edited |
| G15 the register renders the raw's gate column without its two qualifiers | editorial | **CONFIRMED.** The raw's column answers Q2 "**Yes, but the weakest of the five**" and Q4 "**Weakest as a gate** … the recommended path dissolves the question. The gate is real only on the file-writing limb"; the packet carries both verbatim in its review-1 section and the register's blockquote and P-76 row said only "all five questions … genuine hard gates" [Observed, both register sites and the packet site read this session] | Applied at both register sites in the register's own shape: the two qualifiers and the dissolving arm, with the superseded phrase quoted and dated at each |
| G16 Q1's fourth lawful arm is disclosed 1,390 lines below Q1 | editorial | **CONFIRMED.** The Q1 row names three lawful arms and a default; the fourth arm review 1 identified — RFC7-10 **not engaged** — and the disclosure that Q1's default is the only one of the five that ships rather than holds appear in the review-1 section and in the P-76 row, faithfully and unsmoothed, and nowhere in the row itself | Applied: **one clause** in Q1's recommended cell pointing at the review-1 section and the register row and saying why the arm is deliberately not folded in. The arm is **not** added to the table; that decision stands and is the owner's to make on P-76 |

**Recommended answers changed after review 2: none, stated explicitly.**
Review 2's own five-question table answers "Scope truthful?" **Yes** for all
five, "Genuine hard human gate?" **Yes** for four with **Q4 qualified** for
the reason review 1 gave and this packet carries — the recommended arm "needs
no act on anyone's reading", so the gate is real only on the file-writing
limb — "Recommendation follows?" **Yes** for all five, and "Every lawful arm
named?" for all five, Q1's fourth arm being disclosed in the review-1 section
and the register row rather than in its own row. **No lawful arm is called
unlawful anywhere**, **no owner trade-off is smoothed**, every question states
a default-if-unanswered and four of the five default to not shipping, and no
P-71, P-72 or P-73 question is re-asked [Observed, read from the retained
raw]. All sixteen exceptions are presentational or evidentiary: G1, G2, G6 and
G7 are wording the repair pass reinstated or left behind; G3, G4, G8, G12 and
G13 are counts and predicates inside the repairs that did not re-derive over
the data printed beside them; G5 is two self-referential measurements this
packet's own register commit falsified; G9, G10, G11 and G14 are
evidence-record fields not carried forward with the packet; G15 and G16 move a
disclosure to where the owner meets it. **Q1 through Q5 keep the
recommendations, named arms and defaults they carried into this review, word
for word**, and no default-if-unanswered moved.

**The three review-1 observations carried unapplied, for the owner.** Each is
named here rather than acted on, because adding or re-weighting an arm changes
what P-76 puts to the owner and that reading is the owner's own. (1) Q1 has a
**fourth lawful arm this packet does not offer** — rule RFC7-10 **not
engaged**, on the reading that REQ-003's "source anchors" are the bundle's
anchors into governed artifacts and a provider-side source record is not an
anchor in RFC7's sense. (2) **Q1's default is the only one of the five that
ships rather than holds**, and the question does not flag it as the least
conservative default the packet carries. (3) The sentinel figure re-derives
**only** with the sentinel in the `mechanism` source; with it in `purpose` it
is **11** rather than **13**. Review 2 found the first two carried faithfully
and unsmoothed in both of their places and the decision not to fold them in
correctly reasoned; the third it found neither applied, carried nor mentioned,
and it is now carried in all three — here, in the review-1 section, and in the
evidence record's method.

By verification rule 10, review 2 binds the bytes it names — the four digests
in the table above, at commit `1803608` — and not these. Every edit in this
section and in the repairs above was made after it, so **the sixteen exception
repairs are uncovered until a third independent fresh-context review confirms
them**; that raw will be a third `-RAW.md` file, never an overwrite of either
retained one. Subject to that, and on review 2's confirmation of the
`1803608` bytes — CONFIRM WITH EXCEPTIONS, no blocking finding, no recommended
answer moved, and the review-1 dispositions verified as eleven REPAIRED over
twelve with F10 item 3's non-application confirmed correct and all three
incomplete repairs completed here — **this packet stands at the owner gate**:
P-76 is ready to be ruled, with the three unapplied review-1 observations open
in front of it.

Over-width lines after these edits, under the predicate "lines outside fenced
code blocks whose first non-space character is not a pipe, longer than 78
columns", denominator every line of this file: **10** [Observed, measured
after every other edit of this pass and iterated to a fixed point, so the
figure is true of the bytes that carry it].

## Funnel summary

```
## Feature Request: M7 - Close the generation loop
Size: small (slice 5) / medium (slices 2, 3, 6) / large (slices 1, 4) / deferred (slice 7)
Baseline: Syzygy a9f671e; the M7 surface is byte-identical to 1932f74; the dossier's syzygy_audited_at f4589e2 predates the whole generation package, and routes.ts is unchanged at all three
- G1 Motif: the loop has no entrance, no exit and no independence. Entrance: 0 references to three-surface-poc-core, PocModel or projectShape across the 20 tracked files of packages/polaris-generation-core and apps/three-surface-poc/src/polaris-generation (denominator corrected 2026-09-15, review 1 F1; the src-only spelling it named is 17 tracked files and the sweep returns 0 over both), whose entire notion of a source is {sourceId, text<=100000}, while the observation plane carries 12 identity fields plus per-source and per-claim identities. Independence: providerRoute is one scalar for six stages, and the fidelity envelope carries the author's plan - measured by sentinel, 5 keys including plan, against inventory's 2. Exit: awaiting-rendered-review has no successor in the PipelineResult union, and the literals generation and draft occur 0 times in a 240-line route table of 15 entries. Citations are array indices, so reordering the input renumbers the page [Observed, every figure measured this session with predicate and denominator stated]
- G2 Doctrine: VIS-2 at the citation and the self-corpus seams, VIS-1's ordering putting slice 1 above slice 4, VIS-4 for Q1 (accepted-contract reading) and Q5 (normative data contract), VIS-5 for the one slice that would write into .syzygy (slice 4, whose recommended arm writes nothing), SEC-2 naming two of slice 5's five fields, the other three attributed at the site - 0 network primitives across the same 20 tracked files [this line read "SEC-2 as the whole content of slice 5" until 2026-09-15, review 2 G2; the body was repaired the same day under review 1 F9 and this summary reinstated the superseded claim in five unmarked words]
- G3 Topology: packages/polaris-generation-core/src + apps/three-surface-poc/src/polaris-generation + routes.ts + docs/polaris-generation + package.json + PROJECT-STATUS.md; no boundary crossed; no governed artifact edited; every slice filed against an unchecked tasks.md task (24 boxes, 24 unchecked, counted this session)
- G4 Design: an observation-shaped source type whose four identity fields are the registry's own declared scheme; per-stage envelopes constructed at the call site so fidelity and repair lose the plan; a rule-based responder over Syzygy's own 105-file, 1,266,454-byte corpus that publishes its breaches; a machine-credentialed draft route folded into P-72's delta; a pure RFC7-21 per-block packet drafter that writes nothing; stage-scoped inputs and reserve/complete resume
- G5 Spec: no delta needed for the source type - the whole question is whether the registry's git-tree-entry identity is admitted as one of RFC7-10's five closed classes, which is Q1. RFC2-26 run over all seven slice rows (denominator 7): slices 1, 3, 4 and 6 map to named requirement-and-scenario pairs; slice 2's requirement is named and no scenario states the envelope case; slices 3, 5 and 6 enumerate no RFC-0002 consequence; slice 7 deferred and not run
- G6 Bar: three independent methods for the re-billing figure; two each for the two load-bearing zeros; rule-6 mutants per slice; no act-bound byte proposed for edit, with the synthetic-verification record's re-run obligation recorded once for both M6 and M7; TWO independent reviews, both verdicts copied exactly: review 1 CONFIRM WITH EXCEPTIONS (0 blocking, 9 non-blocking, 3 editorial, F1-F12), retained at docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md, and review 2 CONFIRM WITH EXCEPTIONS (0 blocking, 10 non-blocking, 6 editorial, G1-G16), retained at docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md; eleven of review 1's twelve exceptions re-derived and applied and one (F10.3) not confirmed and not applied, which review 2 verified as eleven REPAIRED with F10 item 3's non-application confirmed correct; all sixteen of review 2's exceptions re-derived and applied, and by rule 10 those sixteen repairs are uncovered until a third review [this line read "NO independent review yet - this is a first draft, and by rule 10 nothing here is covered until a fresh-context review reads these bytes" until 2026-09-15, and then "ONE independent review, verdict copied exactly: CONFIRM WITH EXCEPTIONS (0 blocking, 9 non-blocking, 3 editorial, F1-F12) ... and by rule 10 the repairs are uncovered until a second review" until later the same day]
Acts: every M7 clause is predecessor text (ten-sentence sweep over both specification files), so all six slices ride POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md (2026-09-12) on either reading of the understanding act's limiting sentence - the arm that gates M6's slice 4 reaches no M7 slice. What M7 needs instead is five rulings: Q1 an anchor-class reading, Q2 a self-corpus read, Q3 and Q4 arms of sibling questions P-72 and P-71, Q5 an effect-boundary contract sentence
Open questions: Q1-Q5 above, registered 2026-09-15 as P-76 in .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md on this branch - the row the first draft said would land after review 1 [this line read "NOT registered - this packet writes two files and no register row, by instruction; the row lands after review 1, batched" until then]. The eight siblings' rows are P-68 lane B, P-69 M2, P-70 M3, P-71 M4, P-72 M5, P-73 M6, P-74 M8 and P-75 M9, each only on its own branch
Collision: NOT zero. Eleven files shared with M6 (a floor: M6 cites pipeline.ts 10 times as a bare span the predicate misses), and routes.ts shared with M2, M4, M5, M8 and M9 - six packets including this one propose editing the same 240-line file [this line read "routes.ts shared with M2, M4 and M5 - four packets propose editing the same 240-line file" until 2026-09-15, review 2 G1; the body restated it to six the same day under review 1 F8 and the summary was left behind. All six re-verified at source 2026-09-15 in each sibling's Gate 3 table at its current head: M2 slice 3, M4 slice 5, M5 slices 1 and 3, M7 slice 4, M8 slice 2, M9 slices 2, 4a and 6]
Sign-off: pending - the owner's
Recommended handoff: land slice 5 now; then slice 1, which everything else rests on; slices 2 and 6(a) as one refactor behind M6 slice 4's ruling; slice 3 after Q2; slice 6(b) after Q5; slice 4 after P-72 and P-71; defer slice 7 behind M12
```

## Recommended handoff

**Land slice 5 first, regardless of every other answer.** It costs one step in
a kit README and one sentence in `PROJECT-STATUS.md`, it needs no act, it
crosses no trigger, and it is the only slice that makes the *shape* of the
remaining work legible to a reader who is not in this session. Sequence it
behind M6 slice 5 so the two restatements point at each other rather than
repeat.

**Then slice 1, and it is the one that matters.** Every other slice is better
after it: slice 3's perturbation check needs identities to be meaningful,
slice 4 would otherwise serve positional citations on a route, and slice 7's
drift band has no unit without them. It is also the slice that connects two
planes that have never touched, which is the single largest structural fact
this packet found.

**If Q1 is answered as recommended** — `git-tree-entry` admitted as RFC7-10's
evidence-artifact class — then slice 1 may say it satisfies REQ-003's anchor
sentence, and the bead records the ruling by its decision identifier. **If it
is answered the other way**, slice 1 still ships every field; what changes is
the claim. The bead must then record REQ-003's anchor sentence as
**unsatisfied**, and that is a coherent and honest outcome, not a failure: the
generator would carry durable identities that the accepted anchor vocabulary
does not yet have a class for, which is a gap in the vocabulary rather than in
the code. Do not let an implementation quietly assert the conformance either
way.

**If Q2 is answered as recommended**, slice 3 runs, and the thing to guard is
its *claim*, not its execution. Write the evidence record's limitation
sentence before writing the runner, in REQ-014's own words, so that no later
reader — and no later summary of this pursuit — can promote a scripted run
into task 3.3's second project. If the owner takes the narrow-direction arm
instead, slice 3 waits and slices 1, 2, 5 and 6 are unaffected.

**If Q3 is answered as recommended**, slice 4's route folds into P-72's delta
as a second declared category and is ruled once, with `/api/poc/polaris` and
`/api/poc/briefing`. If the owner takes the no-route arm, slice 4's
drafted-act limb still stands on its own: an operator can run the drafter over
a preview written to a directory, which is how the demo works today. The route
is the convenience; the packet is the substance.

**If Q4 is answered as recommended**, the drafter is pure, writes nothing, and
needs no act — and if P-71 later rules that Syzygy may write a drafted packet
into its own decisions tree, the file-writing limb is a five-line adapter over
a drafter that already exists and is already tested. Building it in that order
costs nothing and forecloses nothing.

**If Q5 is answered as recommended**, slice 6(b) lands with the replay
prohibition retained for in-flight and uncertain identities, and REQ-008's
"Resume valid work" scenario becomes implementable. If the owner takes the
second arm, land slice 6(a) alone — the stage scoping is where the money is,
on the self-corpus figures — and record in the bead's close reason that the
port contract and REQ-008's scenario remain mismatched, so the next person to
open this does not read silence as agreement.

**And one thing this packet will not do, stated plainly.** It names the egress
act and does not draft it. The reason is the sequencing L3-M9 argues for and
this packet's own measurements support: asking for egress today would buy a
real model output that the current validators cannot check and that no route
can show the owner. Slices 1 through 6 are the work that makes the first real
call also the first checkable one. That is the whole argument for doing them
first, and it is the owner's to accept or reject.
