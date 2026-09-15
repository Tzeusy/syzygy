
# Feature request M10 — The machine consumer gets a contract: one response identity, a route map, a schema document, and a join key that survives a revision

> **Candidate — binds nothing.** Bead `syzygy-dov.10`, move M10 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`),
> written in the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its
> eight siblings. Planning only: nothing here authorizes implementation. Each
> question below names the arms the owner may lawfully take; naming an arm is
> not a ruling that the slice behind it is authorized. The owner disposes.

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1 and 4a) / **medium** (slices 2 and 5) / **large**
(slice 3) / **gated** (slice 4b).

Baseline: Syzygy `a9f671e` (main), in the worktree on branch
`agent/syzygy-dov.10`. The subject is the two authenticated machine endpoints
and the response identity behind them, not the rendered Polaris page.

**Line-count convention, stated once.** Every "line N" citation in this packet
is a 1-based line number as `sed -n 'Np'` and `cat -n` give it. Every "the
file is N lines" figure is that file's `wc -l` count. Where a quotation spans
two source lines the packet names both, because a wrapped citation that names
one line of a two-line sentence is the error class this corpus records.

## The six questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1 is the packet's central question: three of the five
slices rest on it. Q6 is the only one that could stop slices 1, 2 and 3
together.

| # | Question | Recommended |
|---|---|---|
| Q1 | **What is the machine channel's equality key, and is minting one an implementation of POC-REQ-004 or a new contract?** Neither candidate the dossier names works. (a) A whole-body hash is *too sensitive*: the run instant `evaluation.asOf` occurs as a substring of some string value at **1,436** places in the retained `/api/poc` body, over **25** distinct structural paths, touching **6** of the payload's **19** top-level keys [Observed, computed this session; predicate and denominator in the measurements below]. Two restarts at one Butlers revision therefore differ in 1,436 places. (b) `inputsDigest` is *too insensitive*: its preimage is six named keys (`packages/three-surface-poc-core/src/model.ts` lines 381–389) and the project shape is **not** among them — a landed, passing assertion says so in terms, `packages/three-surface-poc-core/src/model.test.ts` line 343, `expect(observed.evaluation.inputsDigest).toBe(unevaluated.evaluation.inputsDigest);`, where `observed` has `projectShape.kind === 'observed'` (line 314) and `unevaluated` has `projectShape.kind === 'not-evaluated'` (line 259). An ETag keyed on `inputsDigest` would answer 304 to a client whose copy is missing the whole project-shape block. [Observed; the file's 8 tests were run this session and all pass.] | **Mint a third value — a response-identity digest over the canonically serialized body with a declared, enumerated exclusion set — and treat it as an implementation of POC-REQ-004, not a new contract.** POC-REQ-004 already names exactly this shape: "two code-structure observations of R SHALL produce identical fact content" with the oracle "structural diff excluding declared capture-instant fields" (`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` lines 188–191 and 199–200). The exclusion set is not invented here; it is the 25 measured paths. **The counter-argument, which this packet does not resolve:** POC-REQ-004's scope sentence quantifies over "all served code-structure facts across repeated runs at the same revision" (lines 189–191) — *code-structure* facts, one of seven requirement groups — whereas the proposed digest spans the whole payload including the project shape, which is the PWB plane. Reading a code-structure determinism requirement as warranting a whole-payload identity is a widening [Inferred]. **Second lawful arm:** rule it a new contract, route a requirement through CC-REV-2 and a new owner act, and hold slices 2, 3 and 4a behind it. **Third lawful arm:** scope the digest to the code-structure region alone, which POC-REQ-004 plainly covers and which is 27.05% of the body — honest, and useless as an ETag for the other 72.95%. **Default if unanswered: slice 1 lands; slices 2, 3 and 4a hold.** |
| Q2 | **Does serving `Content-Encoding: gzip` change what the declared response ceiling means — and does it therefore need a new owner act?** The registry declares the ceiling's semantics, verbatim at `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` lines 279 and 280: `"maxHumanResponseBytes": "the final encoded HTTP body for each Polaris HTML response"` and `"maxMachineResponseBytes": "the final encoded HTTP body for each authenticated Polaris machine JSON response"`. Today `boundedResponse` measures `Buffer.byteLength(body, 'utf8')` (`apps/three-surface-poc/src/routes.ts` line 138) — the UTF-8 encoding of the string, which *is* the final encoded body while no content coding is in play. Measured this session: gzip level 6 takes the retained `/api/poc` body from **5,520,314** to **851,986** bytes (15.4%) and the retained `/polaris` page from **1,478,637** to **105,850** bytes (7.2%). Under a post-compression reading the 2 MB human ceiling would stop binding at any page size this project can currently produce, and the 2026-09-13 `/polaris` breach at 2,132,656 observed bytes would have been served. | **Yes, it changes the meaning, and it needs an owner act before any compression lands.** The 2026-09-05 continuation names the trigger verbatim: stop before "a change to the constraints or envelope the 2026-09-05 registry entry declares" (`.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` lines 154–155). Compression does not merely make responses smaller; on one reading of the registry's own sentence it converts a fail-closed honest breach into a success, which is the polarity VIS-2 exists to protect. **The counter-argument:** the registry sentence can be read the other way round — "final encoded HTTP body" may mean precisely the wire bytes, in which case today's pre-compression measurement is the *loose* reading and compression tightens nothing while saving 84.6% of the machine transfer. On that reading the change is conformance, not amendment. This packet does not choose; it records that the same eleven words support both readings and that only one of them is currently implemented [Inferred]. **Second lawful arm:** implement compression while keeping `boundedResponse` measuring the uncompressed string, and record in the bead that the served `Content-Length` and the checked ceiling are then deliberately different numbers. That arm is lawful and is the cheaper one; it is also the one that leaves a false sentence standing in the registry if the owner's reading is the post-compression one, and the registry is act-bound and may not be edited to say which. **Default if unanswered: slice 4b does not ship**; slice 4a (ETag only, no content coding) is unaffected. |
| Q3 | **May the schema document be served `human-open` rather than `machine-credentialed`?** The dossier's S6-M1 slice plan says "served unauthenticated". In this daemon `human-open` is not unauthenticated in the ordinary sense: it passes `browserRequestAllowed` (`apps/three-surface-poc/src/browser-origin.ts` lines 26–38), which requires a loopback or tailnet `Host` and an `Origin` that is absent or matches. But an absent `Origin` is admitted, and a non-browser agent sends none — so a `human-open` schema route admits an agent on host alone. SEC-1 reads, verbatim at `.syzygy/governance/doctrine/security.md` lines 14–16: "**non-browser agent and CLI clients are admitted only through an explicit machine-client authentication mechanism**"; its violation list, lines 22–23, names "a machine client admitted on loopback location alone". | **Serve it `machine-credentialed`, like the two endpoints it describes.** The document's whole audience is the non-browser agent SEC-1 reserves to the credential; an agent that can reach `/api/poc` already holds the token, so credentialing the schema costs that reader nothing and costs an unauthenticated reader a document about a payload they cannot fetch. **The counter-argument is real and is the dossier's:** a schema an agent must already be admitted to read cannot be a discovery mechanism for an agent that is not yet admitted, and the schema contains no portfolio data — it is field names and types, not Butlers content, so SEC-2's egress rule is not engaged and SEC-1's concern is admission rather than confidentiality. **Second lawful arm:** serve it `human-open` and record the SEC-1 reading that makes that lawful — that a document containing no observed content is not "portfolio data" and that the origin check is the "explicit mechanism" for this class. This packet does not rule which reading SEC-1 bears [Inferred]. **Default if unanswered: slice 3 does not ship**, because the route's credential class is not a detail a delegate can pick under a doctrine rule with a violation example this close. |
| Q4 | **Do these slices trace under the improvement-cycles direction's second limb, or do they need a direction naming them?** The direction reads, verbatim at `.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lines 55–56: "Improvement-cycle work must trace to POC-REQ-001..061 or to a recorded review finding." Swept this session over the signed three-surface specification: **24** requirements and **24** scenarios; none requires an endpoint to name its siblings, none requires a schema document, none requires a cache validator, none requires a cross-revision join key [Observed; predicate `^### Requirement:` and `^#### Scenario:` over the 1,008-line file, counted this session, and each requirement's text read]. So slices 1, 3, 4a and 5 trace only through the second limb. | **They trace through the second limb, and the pursuit is the recorded review.** The direction defines a cycle's first step as "a review/audit of the runnable POC in fresh context producing evidence-cited findings" (line 34), which is exactly what the 2026-09-13 pursuit produced; S6-F1, S6-F2, S6-F4, S6-F5 and S6-F6 are those findings and every one is re-derived at source in this packet. **The counter-argument:** the same direction says repairs are "derived only from recorded findings" (line 36) and that "the agent reports each completed cycle to the owner before starting the next" (line 41) — if the owner reads the pursuit as a *new* cycle rather than a continuation, its report is owed before any slice lands. And these slices are not repairs: slice 3 adds a document that has never existed, which stretches "improvement" further than any prior cycle item. **Second lawful arm:** treat the pursuit as cycle *n*'s review, report it, and land the slices as cycle *n*'s repairs after that report. **Third lawful arm, and the cheapest affirmative one: a one-sentence direction naming M10's slices**, which moots both readings. **Default if unanswered: the slices are filed and not landed.** |
| Q5 | **May a stable cross-revision join key be derived from a source path plus a normalized statement, and is it M10's to build or M9's?** Two clauses constrain the derivation. PWB-REQ-014 reads, verbatim at `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` lines 774–776: "Anchor targets SHALL use the closed classes doctrine, contract, requirement, decision, evidence and work with durable target identity; labels, file paths and coordinates SHALL never serve as anchor identity." RFC1-10 reads, verbatim at `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md` lines 263–267: "**Identifiers are opaque; names are labels.** For every declared class (Capability, Topology entry, Declared region, Repository, Project, Proposal): renaming the thing changes its label, never its identifier. An identifier, once minted, is never reused and never renumbered; retirement is terminal." The dossier's S6-M6 proposes "a hash of source path + normalized statement" — a path-derived value. | **Build it as a sibling *join key*, never as an anchor identity, and sequence it behind M9's packet rather than duplicating it. It is not the same change as M9's, and this packet says which is which.** M9's slice 6(b) (docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md lines 920–925, read read-only in that worktree at `65de02b`) makes `repository:<repo>@<rev>:<path>#<objectId>` the canonical **cross-surface** key — one string for one artifact across Polaris, Trajectory and Orrery *at one evaluation*; it still embeds the revision. M10's slice 5 is a **cross-revision** key — the same claim across two evaluations. They are different axes and neither subsumes the other, but they mint ids in the same code path, so building both independently mints two schemes for one subject. **The counter-argument:** PWB-REQ-014's prohibition is scoped by its own sentence to *anchor* identity, and a field that is explicitly not an anchor is arguably outside it — but "arguably outside a prohibition" is the reading that should be the owner's, not a delegate's, because the thing being minted is an identity and RFC1-9 reserves minting authority by class. **Second lawful arm:** fold slice 5 into M9's slice 6 and drop it from M10 entirely, so one packet owns identity. **Third lawful arm:** derive the key from the object id the source route already carries rather than from the path, which satisfies both clauses at the cost of not joining across a content change. **Default if unanswered: slice 5 does not ship**, and the gap stays recorded here. |
| Q6 | **May the machine channel carry fields the human surfaces do not?** Slices 1, 2 and 3 each add a top-level field with no counterpart on any page. Both parity requirements are one-directional. POC-REQ-020: "Every fact a client-rendered surface presents SHALL be present, with equal value, in the machine answer for the same evaluation" (spec lines 381–382). PWB-REQ-020: "Every project-shape identity, statement, source anchor, coverage state, denominator, contradiction, body-read authority state and walkthrough-judgment state or disclosure Polaris presents SHALL be recoverable from the same evaluation in the machine answer" (PWB spec lines 906–910). Both quantify over what a *surface presents*; neither says the machine answer contains nothing more. Verified this session: the parity sweep compares named marker families as multisets and reports both denominators (**15** `compareMultisets` call sites over a 568-line file), so a new top-level machine field belongs to no family and the sweep neither guards nor breaks on it [Observed; the sweep's 43 tests were run this session and all pass]. | **Yes — the machine channel may carry more, and this packet reads the two requirements' direction as settled by their own words rather than by the sweep's silence.** A links map, a response identity and a schema document are not facts about Butlers; they are facts about the endpoint. **The counter-argument, and it is the one that makes this a question rather than a decision:** the sweep's silence is not a guarantee, it is an absence of coverage — and AGENTS.md records that PWB-REQ-020 parity is per tuple and never per id, which is a rule about not trusting a coarse invariant. A machine-only field that later acquires a human counterpart would enter no family and drift unguarded, which is the same failure shape one level up. **Second lawful arm:** rule that any new machine field must either have a human counterpart or be added to the sweep as its own family with a declared empty human denominator — which is more work and is the honest version. **Default if unanswered: slices 1, 2 and 3 hold**, because all three depend on this answer and none of them is worth landing on a reading of a requirement's direction that nobody has ruled. |

### Decided in this packet, not put to the owner

**The dossier's "prerequisite: none" survives, with two corrections and one
figure replaced.** The dossier's machine record gives M10 a `prerequisite` of
`none` and its prose says "Prerequisite. None; populate-or-prune of the
declared vocabulary (S6-M4) is a spec amendment and is listed, not scheduled."
Both halves hold. S6-M4 is not merely a spec amendment by this packet's
judgment — the specification says so in terms: PWB-REQ-014 lines 774–776
declare the six anchor classes **closed**, so pruning three of them is an edit
to signed requirement text and routes through CC-REV-2 and a new owner act. It
is listed in Gate 5 below and scheduled nowhere.

The corrections are these.

1. **The dossier's "18 top-level keys" is 19.** Counted this session on both
   retained `/api/poc` captures: 19 keys, identical sets. The likeliest
   reading of 18 is that `materializedBeadId`, whose value is `null`, was not
   counted; this packet does not know and marks it [Unknown]. Nothing in M10
   turns on the figure, but a schema document enumerates keys, so it is
   corrected where it is used.
2. **The dossier's "prerequisite: none" does not mean no owner ruling is
   needed to *land* the work.** Q1, Q2, Q3, Q5 and Q6 are genuine gates. Q4
   is the one that asks whether these slices trace at all.

**The "99.8% one class" figure reproduces exactly, on two independent
populations.** 914 of 916 anchors are `evidence`; 914/916 = 99.7817%. Both
retained presentation captures — at different Butlers revisions and different
observer commits — give byte-for-byte the same census. The dossier's figure
stands [Observed].

**S6-F6's claim label rises from Inferred to Observed.** The dossier labels
S6-F6 ("Equality identity is undocumented in-payload") `Inferred`. The
underlying facts are now measured: `asOf` is minted from the wall clock at
`apps/three-surface-poc/src/main.ts` line 134 and is embedded in two further
identity strings at lines 148 and 168; it occurs as a substring at 1,436
places in the served body over 25 distinct paths. What remains Inferred is
only the *consequence* — that a naive consumer would over-count restarts —
and that is a reading of consumer behaviour, not a measurement.

**The dossier's build_cost of 2 for M10 is not reproducible for slice 3.** The
schema document's real subject is **769** distinct structural paths and
**241** distinct field names in `/api/poc`, plus **57** paths and **48**
names in `/api/poc/polaris`, **273** names in union. Against that, the slice
plan's premise — "Enumerate PocModel and PolarisPresentationEnvelope field
docs from existing TSDoc comments" — does not hold: of `PocModel`'s 19
top-level fields, **5** carry an immediately preceding doc comment and **14**
do not, and `PolarisPresentationEnvelope`'s **7** fields carry **0**. There is
almost nothing to extract; the prose would be written, not enumerated. Slice 3
is costed **large** here, against the dossier's 2 [Observed for the counts,
Inferred for the cost class].

**S6-F3 is deliberately not a slice of this packet.** It is the dossier's own
placement — S6-M4 sits in M10's `evidence_findings` list as S6-F3's move and
is named in the What bullet as "which declared enum members are populated
(S6-M1)", which is the *disclosure*, not the pruning. This packet builds the
disclosure and schedules no pruning.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `.syzygy/governance/doctrine/security.md` | VIS-1, VIS-2, VIS-3, VIS-4, VIS-5, VIS-7; SEC-1, SEC-2 |
| Decisions | `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, `.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`, `.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`, `.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md` | the first three are the grants quoted per slice in Gate 3; the last two are the digest bindings that forbid editing either specification |
| Specification | `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` (24 requirements, 24 scenarios, 1,008 lines) and `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` (17 requirements, 31 scenarios, 1,152 lines) | POC-REQ-004, POC-REQ-020; PWB-REQ-006, PWB-REQ-014, PWB-REQ-020 |
| Registry | `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | `resourceLimits` lines 264–272 and `resourceLimitSemantics` lines 273–282; act-bound, and Q2 turns on line 280 |
| Contracts | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`, `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md` | RFC2-26's phase rule, run over every slice in Gate 5; RFC1-9, RFC1-10, RFC1-12 for slice 5; RFC1-33, the RFC-0001 twin of RFC2-26, whose own consequence list names "API answers over graph identities" |
| Policies | `.syzygy/governance/contracts/candidates/policy-candidates/` (CC-SPEC, CC-IMPACT, in force despite the directory name) | CC-REV-2 is the amendment path Q1's second arm and S6-M4 would need |

**What binds and may not be edited.** Swept this session over 605 tracked
`.md`/`.txt`/`.json`/`.yaml` files under `.syzygy/governance/decisions/`,
`.syzygy/governance/contracts/` and `docs/evidence/`, under the predicate
"contains the artifact's path in either its repository-relative or its
act-relative form" — the second form matters, because
`THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` names its signed artifacts relatively
(line 46 reads `specs/three-surface-poc-experience/spec.md`) and a
full-path-only sweep reports it as unbound, which is a false absence this
corpus has paid for before:

| Artifact | Bound by | May a slice edit it? |
|---|---|---|
| the three-surface specification | `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` (its digest table, line 46) | **No** |
| the PWB specification | `POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md`, `PWB-STATE1-AMENDMENT-ACT.md`, `PWB-TRUTH-READINESS-AMENDMENT-ACT.md` and two manifests | **No** |
| the observer registry entry | `PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`, `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, `ACCEPTANCE-ACT-RECORD.md` and two manifests | **No** |
| `apps/three-surface-poc/src/routes.ts` | no act; named by 4 evidence records | yes (implementation plane) |
| `packages/three-surface-poc-core/src/model.ts` | no act; named by 4 evidence records | yes |
| `apps/three-surface-poc/src/polaris.ts` | no act; named by 19 evidence records | yes |
| `apps/three-surface-poc/src/polaris-narrative.ts` | no act; named by 3 evidence records | yes |
| `packages/cap1-daemon/src/server.ts` | no act; named by 1 evidence record | yes |

**No slice proposes editing a bound byte.** Separately, and it is a different
claim: of the seven implementation files this packet's slices would touch, the
current sha256 of **each** is cited by **0** files across the 640 tracked
files under `docs/evidence/` and `.syzygy/governance/` [Observed, all seven
digests computed by `hashlib` this session and searched; no digest is
reproduced here, per CG-15 — the records are cited by path]. So editing them
retires no currently-bound confirmation. The evidence records above name the
**paths**, not the current bytes, so what they oblige is a re-run before a
repaired claim is made, not a prohibition.

**A pre-act banner is not the act.** Both specification files still open with
a candidate banner over bytes an act bound; AGENTS.md records the rule and
this packet follows it: the act record is read, never the package banner.

## Gate 1 — Motif

**The machine channel has no identity of its own, so it cannot say whether it
changed.** The doctrine names two first-class consumers; the owner's own
framing names "agents (machine-queryable endpoints)". What an agent holds
today is a 5.5 MB JSON body with a version label, no route map, no field
documentation, and no correct way to ask "is this the same answer you gave me
last time". The two candidate answers both fail, in opposite directions and
for reasons that are measured rather than argued: hashing the body is wrong by
1,436 embedded wall-clock substrings, and the one digest the payload already
carries is wrong by the entire project-shape block, which a landed test
asserts it excludes **on purpose**. That is the motif. Everything else in M10
is downstream of it: a links map is cheap, a schema document is large, a
cross-revision join key is gated — but none of them is worth much to a
consumer who cannot tell two answers apart.

**The specific shape, in five measurements.** (1) `/api/poc`'s handler is four
lines and does not take the request: `machineHandle` at
`apps/three-surface-poc/src/routes.ts` lines 159–162, whose body is one
`boundedResponse(..., JSON.stringify(model))`. (2) Over the two source trees
that serve every response — 104 TypeScript files under
`apps/three-surface-poc/src` and `packages/cap1-daemon/src` — there are **0**
occurrences of `ETag`, `Cache-Control`, `Content-Encoding`, `If-None-Match`,
`Accept-Encoding`, `gzip`, a `Vary` header form, `.setHeader(` or `zlib`, and
exactly **1** `.writeHead(`, at `packages/cap1-daemon/src/server.ts` line 122,
which sets one header. (3) Neither retained `/api/poc` body contains the
literal `/api/poc/polaris`, `/api/poc`, `polaris-presentation` or `/polaris`
anywhere, and neither carries a top-level field named `links`, `_links`,
`endpoints`, `routes`, `href`, `self`, `schemaUrl`, `$schema` or `version`.
(4) Of `PocModel`'s 19 top-level fields, 14 carry no doc comment at all. (5)
Three of the six declared anchor target classes have **0** construction sites
anywhere in production code or **0** rendered anchors in either capture.

**And the one honest thing about the ceiling is exactly what compression would
undo.** `boundedResponse` (`apps/three-surface-poc/src/routes.ts` lines
137–142) serves nothing on a breach — no truncation, no success-shaped model,
readiness false. AGENTS.md records what that costs: a breach "serves nothing
and logs nothing", and the 503 body is its only trace. gzip would take the
2026-09-13 `/polaris` breach from 2,132,656 observed bytes to roughly a
fifteenth of that, comfortably inside the 2,097,152 ceiling — which is either
a fix or a silent defeat of a fail-closed gate, depending on eleven words in
an act-bound registry file. That is Q2, and it is why compression is separated
from conditional GET here instead of shipped with it.

**Success criteria, per slice.** Slice 1: an agent holding one endpoint URL
can enumerate the others from the body, and adding a route without adding a
link fails a test. Slice 2: two builds at one Butlers revision with different
run instants produce the same response identity, and a single changed
project-shape byte produces a different one. Slice 3: every field an agent can
receive has a name, a type and a sentence, and a field added without a schema
entry fails a test. Slice 4a: a repeat GET with `If-None-Match` transfers no
body and the identity it keys on is slice 2's, never `inputsDigest`. Slice 5:
the same Butlers claim at two revisions carries one join key and two distinct
anchor identities, and the anchor identity is unchanged.

**What M10 is not.** It is not a change to the rendered Polaris page, not a
query interface, not pagination, not field selection, and not a change to what
any claim means. Every slice adds machine-side description or machine-side
identity; none moves a fact.

## Measurements at `a9f671e`

Every figure below was taken this session, in the worktree at `a9f671e`,
except where a figure is explicitly a property of a retained capture. Method,
predicate, denominator and raw output for each are in the evidence record
beside this packet,
`docs/evidence/polaris-m10-machine-contract-funnel-2026-09-15.json`.

### The two retained captures, and what each is evidence of

| Capture | Bytes | Butlers revision | Observer revision | What it is evidence of |
|---|---:|---|---|---|
| scratchpad/capture/api-poc.json | 5,508,208 | 7c8743f63 | f4589e26 | the population the dossier's S6 findings were computed on |
| scratchpad/capture/api-poc-polaris.json | 640,592 | 7c8743f63 | f4589e26 | the same, for the presentation envelope |
| scratchpad/m1/measure/after/api-poc.json | 5,520,314 | 2e3bac977 | 2ef68f5b | the post-lane-A machine body, the later of the two |
| scratchpad/m1/measure/after/api-polaris.json | 640,592 | 2e3bac977 | 2ef68f5b | the same, and **not** byte-identical to the first despite the equal size |
| scratchpad/m1/measure/after/polaris-direct.html | 1,478,637 | 2e3bac977 | 2ef68f5b | the human page against its 2,097,152 ceiling |
| scratchpad/m1/measure/after/polaris-tailnet.html | 1,484,487 | 2e3bac977 | 2ef68f5b | the same through the tailnet mount |

[Observed; sizes by `os.path.getsize`, revisions read from each capture's own
`project.revision` and `observerRevision` fields and from the retained daemon
logs. The two presentation envelopes have equal byte length and different
sha256 values, computed this session — a coincidence of size, not a
duplicate.] Neither directory holds a credential value and none was read.

Against the declared ceilings: the machine body uses **65.8%** of
`maxMachineResponseBytes` (8,388,608), leaving 2,868,294 bytes; the
presentation envelope uses **7.6%**; the human page uses **70.5%** direct and
**70.8%** through the mount, leaving 618,515 and 612,665 bytes. The human
figures agree with M9's packet, which computed them independently from the
same two files.

### The response handlers, quoted at `a9f671e`

The dossier cites `routes.ts` lines 159–162 at `f4589e2`. Re-located this
session at `a9f671e`: the same four lines, unchanged.

```
  const machineHandle: Route['handle'] = () => {
    const model = getModel();
    return boundedResponse(model, limits, 'maxMachineResponseBytes', 'application/json', JSON.stringify(model));
  };
```

The presentation handler is lines 163–176 and differs in one respect that
matters to slice 1: it *does* construct an envelope, with `kind`, `version`,
`presentation` and `citable` fields (lines 167–173), so the presentation
endpoint already has a small self-description and `/api/poc` has none. The
route table is lines 206–239. It returns **15** route entries over **15**
distinct paths: 9 written literally, plus 3 × 2 from the three
`humanSurfaceRoutes` spreads at lines 220, 223 and 224. **4** are
`machine-credentialed` — the two machine endpoints, each registered bare and
again under the tailnet mount prefix — and **11** are `human-open` [Observed,
counted this session: the file carries 4 `machine-credentialed` and 7
`human-open` credential literals, two of the latter inside
`humanSurfaceRoutes` and therefore emitted three times each].

### The header sweep, with its predicate and denominator

Denominator: **104** `.ts` files under `apps/three-surface-poc/src` and
`packages/cap1-daemon/src` (54 of them non-test). Predicate: a Python `re`
search per line, word-bounded where a bare substring would over-match.

| Token | Occurrences | Where |
|---|---:|---|
| `ETag` (word-bounded) | 0 | — |
| `Cache-Control` | 0 | — |
| `Content-Encoding` | 0 | — |
| `If-None-Match` | 0 | — |
| `Accept-Encoding` | 0 | — |
| `gzip` (word-bounded) | 0 | — |
| a `Vary` header form | 0 | — |
| `zlib` | 0 | — |
| `.setHeader(` | 0 | — |
| `.writeHead(` | 1 | `packages/cap1-daemon/src/server.ts` line 122 |

Second method, per verification rule 2: `git grep -F -i` over tracked files in
the same two directories agrees on every row. The word boundary is
load-bearing and is why it is stated: a case-insensitive substring search for
`etag` returns a hit in
`packages/three-surface-poc-core/src/test-artifact-verification.ts`, which is
the function name `parseTagAttrs` and not a header. That file is outside this
sweep's denominator in any case; it is named because the naive predicate would
have produced a false positive and the corrected one is what the table used.

The one header-setting site, quoted whole, is
`packages/cap1-daemon/src/server.ts` lines 121–124:

```
function respond(res: http.ServerResponse, response: RouteResponse): void {
  res.writeHead(response.status, { 'content-type': response.contentType });
  res.end(response.body);
}
```

### Discoverability: what `/api/poc` says about its siblings

Predicate A, over the 19 top-level keys of each retained `/api/poc` body: is
any key one of `links`, `_links`, `endpoints`, `routes`, `href`, `self`,
`schemaUrl`, `$schema`, `api`, `version`, `rel`, `sibling`? **0 of 19**, on
both captures. Predicate B, over the raw body text: **0** occurrences each of
`/api/poc/polaris`, `/api/poc`, `polaris-presentation`,
`presentation-artifact` and `/polaris`, on both captures. Predicate C, the
same twelve key names at **any** depth of the parsed object: **0**.

The literal `openapi` occurs exactly **1** time in each body. It is a
substring of an observed-repository test filename inside the
`codeStructure.files` list — named here without a code span, because it is a
path in the observed repository — and is not a self-description. It is
reported because a bare literal sweep for `openapi` would otherwise read as a
hit.

The presentation envelope carries **0** occurrences of `/api/poc`, `/polaris`,
`links`, `endpoints`, `href` or `openapi`. So neither endpoint names the
other, in either direction.

`/api/poc`'s only self-description is one string: `schema` =
`syzygy-three-surface-poc/v1`, declared as a literal type at
`packages/three-surface-poc-core/src/model.ts` line 99 and emitted at line
687. It is a version label; nothing is fetchable from it.

### The anchor vocabulary, re-derived two ways

The declared union is **not** in `model.ts`, which is where the drafting brief
for this packet pointed; it is at
`apps/three-surface-poc/src/polaris-narrative.ts`
lines 21 and 25, quoted verbatim:

```
export const NARRATIVE_CLAIM_ROLES = ['anchored-project-fact', 'non-normative-framing', 'epistemic-claim'] as const;
```

```
export const ANCHOR_TARGET_CLASSES = ['doctrine', 'contract', 'requirement', 'decision', 'evidence', 'work'] as const;
```

Both are spread into the served envelope at lines 185 and 186
(`roles: [...NARRATIVE_CLAIM_ROLES]` and
`anchorTargetClasses: [...ANCHOR_TARGET_CLASSES]`), which is why the payload's
`narrative.roles` and `narrative.anchorTargetClasses` are exactly these lists.

**Method 1 — population census over the served bodies.** Predicate: walk
`narrative.blocks[]`, count `role`; walk `narrative.blocks[].anchors[]`, count
`targetClass`. Denominators reported.

| Population | Blocks | Roles used | Anchors | `evidence` | `requirement` | `work` | `doctrine` | `contract` | `decision` |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| capture, Butlers 7c8743f63 | 714 | 1 of 3 | 916 | 914 | 1 | 1 | 0 | 0 | 0 |
| lane-A after, Butlers 2e3bac977 | 714 | 1 of 3 | 916 | 914 | 1 | 1 | 0 | 0 | 0 |

914/916 = **99.7817%**, which is the dossier's 99.8% [Observed]. Every anchor
id is distinct (916 of 916). Declared-but-unused: **3 of 6** classes
(`doctrine`, `contract`, `decision`) and **2 of 3** roles
(`non-normative-framing`, `epistemic-claim`).

**Method 2 — construction-site census over production code.** Denominator:
**72** non-test `.ts` files under `apps/three-surface-poc/src` and
`packages/three-surface-poc-core/src`. Predicate: a literal
`targetClass: '<class>'`, an `AnchorTargetClass` default parameter equal to
`'<class>'`, a third positional `'<class>'` to `supportAnchor` or
`artifactAnchor`, or a value of the `PROVENANCE_CLASS` map.

| Class | Construction sites | Sites |
|---|---:|---|
| `evidence` | 9 | `polaris-narrative.ts` 86, 87, 88, 90, 91, 113; `polaris.ts` 266, 407, 994 |
| `work` | 2 | `polaris-narrative.ts` 89; `polaris.ts` 287 |
| `requirement` | 1 | `polaris.ts` 1078 |
| `decision` | 1 | `polaris-narrative.ts` 92 |
| `doctrine` | **0** | — |
| `contract` | **0** | — |

The two methods agree where they overlap and each says something the other
does not. `doctrine` and `contract` are not merely unpopulated at these two
evaluations — **no production code path can construct them**. `decision` has
exactly one construction site, the `PROVENANCE_CLASS` entry mapping the
provenance kind `owner-act` (declared at
`packages/three-surface-poc-core/src/model.ts` line 56 and built by
`ownerActProvenance` at
`packages/three-surface-poc-core/src/project-shape-model.ts`
lines 668–679), and is reachable but unrendered at both evaluations. A naive
sweep would also have counted `ledger.block('contract', …)` at
`apps/three-surface-poc/src/polaris.ts` line 1088; that is a deep-dive ledger
block kind and not an anchor target class, and it is excluded by the predicate
rather than by hand.

### `inputsDigest`: what it is, where it is computed, and what it omits

Declared at `packages/three-surface-poc-core/src/model.ts` lines 108–109,
quoted whole:

```
    /** SHA-256 hex digest of the canonical observation inputs. */
    readonly inputsDigest: string;
```

Computed at lines 381–389, quoted whole:

```
  const inputDigest = sha256(
    JSON.stringify({
      repoRoot,
      repositoryRevision: input.repositoryRevision,
      observerRevision: input.observerRevision,
      artifacts: [design, proposal, requirement, code, test],
      mappingDigest,
    }),
  );
```

and emitted at lines 688–693. Its preimage is therefore exactly five named
keys plus one derived digest. The build input type
`BuildButlersPocModelInput` (lines 179–206) declares **13** members; **3** of
them (`repoRoot`, `repositoryRevision`, `observerRevision`) are in the
preimage and **10** are not, including `projectShape`, `walkthroughJudgment`,
`walkthroughReadiness`, `materializationRecord`, `testArtifactRecord`,
`runWorkItemQuery` and `evaluation` itself [Observed, counted at source this
session].

The omission is deliberate and documented in the test, not inferred. The
comment at `packages/three-surface-poc-core/src/model.test.ts` lines 341–342
reads, verbatim across both lines: "The shape does not enter the inputs digest
of the unrelated proving slice (its own identity carries manifest and
observation digests)." The assertion that follows, line 343, is:

```
    expect(observed.evaluation.inputsDigest).toBe(unevaluated.evaluation.inputsDigest);
```

with `observed.projectShape.kind === 'observed'` asserted at line 314 and
`unevaluated.projectShape.kind === 'not-evaluated'` at line 259. The file's
**8** tests were run this session and all pass. This is the counterexample
that decides Q1's option (b): `inputsDigest` is a sound identity for what it
covers and an unsound ETag for what is served.

### The wall clock in the served body

Predicate: the exact string value of `evaluation.asOf` as a substring of any
string in the parsed `/api/poc` body. Denominator: the whole body.

**1,436** occurrences over **25** distinct structural paths, touching **6** of
19 top-level keys. The five largest paths are
`projectShape.facts[].claim.evaluationId` (439),
`projectShape.items[].claim.evaluationId` (415),
`projectShape.sources[].stamp.capturedAt` (278),
`projectShape.sources[].claim.evaluationId` (278) and
`projectShape.projectAccount[].claim.evaluationId` (6); the remaining 20 paths
carry one occurrence each. Top-level keys touched: `codeStructure`,
`evaluation`, `projectShape`, `proposedWork`, `walkthroughJudgment`,
`workItems`. Untouched: the other 13.

The source is one expression, `apps/three-surface-poc/src/main.ts` line 134:

```
            const asOf = new Date().toISOString();
```

whose value is then interpolated into two further identity strings at lines
148 and 168 (`evaluation:pwb-body-read:${asOf}` and
`evaluation:pwb-walkthrough-judgment:${asOf}`). That is why 25 paths rather
than one carry it.

### The schema document's real subject

Predicate: walk the parsed body; collect every object key (**names**) and
every structural path with array indices collapsed to `[]` (**paths**).

| Endpoint | Distinct field names | Distinct structural paths |
|---|---:|---:|
| `/api/poc` | 241 | 769 |
| `/api/poc/polaris` | 48 | 57 |
| union of names | 273 | — |

Against that, the documentation already present. Predicate: a top-level
`readonly <name>:` member of the interface whose immediately preceding
non-blank line ends a block comment or starts a line comment.

| Interface | Declared at | Top-level fields | With a doc comment | Without |
|---|---|---:|---:|---:|
| `PocModel` | `packages/three-surface-poc-core/src/model.ts` lines 98–155 | 19 | 5 | 14 |
| `PolarisPresentationEnvelope` | `apps/three-surface-poc/src/routes.ts` lines 24–32 | 7 | 0 | 7 |

The five documented `PocModel` fields are `materializedBeadId`,
`projectShape`, `proposedWork`, `walkthroughJudgment` and
`walkthroughReadiness`. The fourteen undocumented are `schema`, `evaluation`,
`project`, `observerRevision`, `capabilityId`, `entities`, `relationships`,
`surfaces`, `codeStructure`, `workItems`, `workerChange`,
`testArtifactVerification`, `orrery` and `trajectory`. (The `evaluation`
member's *nested* fields carry three doc comments, at lines 101–104, 106 and
108; the member itself does not, and the predicate is about the member.)

### The ceiling, and what compression would do to it

`boundedResponse`, `apps/three-surface-poc/src/routes.ts` lines 137–142,
quoted whole:

```
export function boundedResponse(model: PocModel, limits: PwbResourceLimits, limit: ResponseLimitIdentity, contentType: string, body: string): RouteResponse {
  const observed = Buffer.byteLength(body, 'utf8');
  const declared = limits[limit];
  if (observed <= declared) return { status: 200, contentType, body };
  return { status: RESPONSE_LIMIT_STATUS, contentType: 'application/json', body: JSON.stringify(responseLimitFailure(model, limit, declared, observed)) };
}
```

The measured quantity is the UTF-8 encoding of the response *string*. Measured
this session with Python's `gzip` at level 6:

| Body | Uncompressed | gzip -6 | Ratio | Saved |
|---|---:|---:|---:|---:|
| `/api/poc` (lane-A after) | 5,520,314 | 851,986 | 15.4% | 4,668,328 |
| `/polaris` (lane-A after, direct) | 1,478,637 | 105,850 | 7.2% | 1,372,787 |

[Observed. The level is stated because the ratio depends on it; no other level
was run, and a different level would give a different ratio and the same
conclusion.] The 2026-09-13 `/polaris` breach observed 2,132,656 bytes against
a declared 2,097,152. A gzip of comparable ratio puts that body two orders of
magnitude inside the ceiling. Whether that is a fix or a defeat is Q2, and the
answer is not in the code: it is in eleven words at line 279 of the
act-bound observer registry entry,
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
— `"the final encoded HTTP body for each Polaris HTML response"`.

The resource ledger is not a second opinion here. AGENTS.md records that the
ledger is the input-side reader budget and never sees a response ceiling, and
that a ceiling breach logs nothing; this packet does not re-derive that and
does not rely on it beyond naming it as the reason Q2 cannot be answered from
a run.

### Bytes per top-level key, for costing

Method: `json.dumps(v, separators=(",", ":"))` per top-level value, against
the lane-A `/api/poc` file's own 5,520,314 bytes. The sum of the parts is
5,521,648 (100.02%), the excess being the key names and separators the parts
do not carry.

| Key | Bytes | Share |
|---|---:|---:|
| `workItems` | 2,273,467 | 41.18% |
| `projectShape` | 1,657,461 | 30.02% |
| `codeStructure` | 1,493,219 | 27.05% |
| `trajectory` | 80,130 | 1.45% |
| every other key (15 of them) | 17,371 | 0.31% |

A links map, a response identity and a schema reference together are a few
hundred bytes against 2,868,294 of machine headroom. None of M10's slices is a
byte-budget question, which is the one thing that separates it from M1 and M9.

### Line numbers re-verified at `a9f671e`

Every line number the dossier's S6 findings cite, checked at source this
session:

| Dossier citation | At `a9f671e` | Verdict |
|---|---|---|
| `routes.ts:159-162` — the handler is `JSON.stringify(model)` | lines 159–162, `machineHandle` | **confirmed** |
| `polaris-parity-sweep.test.ts:4-6` — the production comment | lines 4–6 exist and carry the comment, but the parenthetical the dossier quotes spans lines **5–7**: "(`/api/poc` is `JSON.stringify(model)` verbatim, so the machine channel here is that string parsed back)" | **confirmed with a corrected span**; the dossier's 4–6 stops one line short of the closing parenthesis, which is the wrapped-citation class this corpus records |
| `routes.ts:15-21` — the presentation route's purpose in a comment | the block comment is lines **17–20**; line 21 is the constant it documents, and lines 15–16 are `POC_HUMAN_PATH` and `POC_MACHINE_PATH` | **confirmed for the comment, 17–20**; the dossier's 15–21 is two lines wide at the top and one at the bottom |
| `server.ts:121-124` — `respond()` sets only content-type | lines 121–124 | **confirmed** |
| `main.ts:134` — `const asOf = new Date().toISOString();` | line 134 | **confirmed** |
| `api-poc.json` "18 top-level keys" | 19 | **differs**; see the corrections above |
| `routes.ts:137-142` — one `boundedResponse` for both channels | lines 137–142 (the dossier's S6 gap paragraph cites 137–142 for the ceiling and 159–162 for the handler) | **confirmed** |

## Gate 2 — Doctrine

**VIS-1 — Comprehensible truth first, and its ordering is why slice 2 outranks
slice 3.** Quoted at the clause, `.syzygy/governance/doctrine/vision.md` lines
82–87: "The full ordering, highest first: (1) truth and observation
determinism; (2) comprehension of the truth's presentation; (3) momentum
(delivery speed); (4) breadth of scope and fidelity of presentation; (5)
reproducibility of derived convenience (caches, incremental refresh,
zero-token synchronization, byte-identical inference output)." Two of M10's
slices sit at rank 1 and one sits explicitly at rank 5. A response identity
that tells two answers apart is *observation determinism* — the clause's own
rank-1 words. A schema document is *comprehension of the presentation*, rank
2. A cache validator is, in the clause's own parenthesis, "caches" — rank 5,
the lowest, "spent before higher ones". The packet's ordering follows the
clause rather than the dossier's, which lists the schema first.

**VIS-2 — No evidence means Unknown, not success.** Lines 96–106: "No surface
may declare a project aligned, converged, or genome-complete — nor turn
anything green — without current evidence… *Violation:* … a stale view
silently green." Slice 4b is where this bites. A 304 response is a statement
that the client's cached copy is still current; if the validator is wrong in
the insensitive direction — which `inputsDigest` measurably is — a 304 is a
stale view rendered silently green by the client, and Syzygy caused it. That
is why slice 4a is sequenced behind slice 2 and cannot be built on the digest
the payload already carries.

**VIS-3 — Human interpretability is a core tenet.** Lines 108–110: "Every
normative artifact — spec, doctrine, contract — must remain digestible by a
human unfamiliar with the project." A machine schema document is not a
normative artifact, so VIS-3 does not bind slice 3 directly; the doctrine this
packet reads as reaching it is VIS-1's rank-2 comprehension ordering applied
to the machine consumer the north star names as first-class [Inferred — a
reading of VIS-3's scope, stated rather than resolved; the dossier's M10 entry
tags VIS-3 without this qualification].

**VIS-4 — Humans steer the vision; agents shape within it.** Lines 122–140.
This packet drafts and adopts nothing. Q1's second arm and S6-M4 both route
through CC-REV-2 precisely because VIS-4 puts normative data contracts in the
always-human-gated class.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Lines 141–165. Every file any slice touches is in the
implementation plane — `apps/**`, `packages/**` or a root manifest. No slice
writes into `openspec/**` or `.syzygy/**`, and no slice edits a bound byte.

**VIS-7 — The observatory itself must be trustworthy.** Lines 183–193, at
the determinism sentence: "the deterministic layer of an observation record
is identical across runs of one identified evaluation (source snapshot +
as-of instant…)". Note the clause's
own parenthesis: the identified evaluation *includes* the as-of instant, so
VIS-7 does not by itself require that two runs at different instants agree —
which is exactly the gap slice 2 fills by declaring, in the payload, which
fields are the instant and which are the content.

**SEC-1 — Authenticated by default.** At
`.syzygy/governance/doctrine/security.md`
lines 10–23, quoted at the load-bearing sentence and its violation:
"**non-browser agent and CLI clients are admitted only through an explicit
machine-client authentication mechanism**; loopback location alone is never
proof of client
identity… *Violation:* … a machine client admitted on loopback location
alone." This is Q3 and nothing else in M10 engages it: slices 1, 2, 4a and 5
all add fields to routes that are already `machine-credentialed`, so their
admission posture is unchanged.

**SEC-2 — Portfolio data leaves owner-controlled infrastructure only through
explicit, scoped consent.** Lines 25–37: "Governed-project content — source
structure, specs, work history, and anything derived from them, including
prompts — is never transmitted to a store or service the owner does not
control without explicit, recorded, per-project consent. **Model providers are
such services.**" No slice in M10 transmits anything anywhere: every one adds
a field to, or a document about, a response the daemon already serves on
loopback or the tailnet mount. SEC-2 is named because Q3's second arm turns
partly on whether a schema document is "governed-project content"; this packet
reads it as not — it is field names and types of Syzygy's own model, not
Butlers content — and says so as a reading rather than a ruling [Inferred].

**RFC1-9, RFC1-10 and RFC1-12 bound slice 5.** RFC1-9 (lines 239–261) reserves
minting authority by class and requires kernel-owned identities to be
"**deterministically derived** from their defining inputs, so two runs over
the same inputs mint the same identity (VIS-7)". RFC1-10 (lines 263–267)
makes identifiers opaque and never reused. RFC1-12 (lines 278–284) says
"Judgments do not silently survive identity change" — which is the reason a
cross-revision join key must be a *join key* and never quietly become the
thing a judgment
binds to. Slice 5 is designed to satisfy all three and is still put to the
owner in Q5, because the question of whether a path may enter the derivation
is decided by PWB-REQ-014's sentence and not by these three.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Links map | `apps/three-surface-poc/src/routes.ts` (a `links` field built from the same array `pocRoutes()` returns at lines 206–239); a new sibling test | none |
| 2 Response identity | a new module under `packages/three-surface-poc-core/src/` (canonical serialization + the declared exclusion set), consumed by `apps/three-surface-poc/src/routes.ts` at lines 159–176; `packages/three-surface-poc-core/src/model.ts` if the field lands on `PocModel` rather than on the response envelope | none |
| 3 Schema document | a new emitter under `packages/three-surface-poc-core/src/` or `apps/three-surface-poc/src/`, its build step in `package.json`, and one new route in `apps/three-surface-poc/src/routes.ts` | none |
| 4a Conditional GET | `packages/cap1-daemon/src/server.ts` (the `respond` path at lines 121–124 and the admission block at lines 187–210); `apps/three-surface-poc/src/routes.ts` | none |
| 4b Compression | the same two files, plus `node:zlib` | **none edited**, but the meaning of `resourceLimitSemantics` lines 279–280 is what Q2 asks about, and that file is act-bound |
| 5 Stable join key | `apps/three-surface-poc/src/polaris-narrative.ts` (the anchor constructors at lines 102–125) and `apps/three-surface-poc/src/polaris.ts` (lines 407–409 and 1078) | none |
| 6 (carried) `evidence` block | owned by M2's packet; not designed here | not designed here |

Boundaries crossed: none. Every file above is in the implementation plane, and
`openspec/**` and `.syzygy/**` are read for authority and written by no slice.

Not touched by any slice: the credential admission path
(`packages/cap1-daemon/src/server.ts` lines 188–200), which S6's own audit
called solid and which slice 4a must read without changing; the PWB pipeline;
the renderers, except for slice 5's two anchor constructors; `boundedResponse`
itself, whose measured quantity slice 4b would change and slice 4a would not.

### The authorizing act, per slice

The grants in force are two plain owner directions and one specification
sign-off. Neither direction binds a digest, so neither adds an
acceptance-record row; both carry escalation triggers, and the triggers are
the operative text here.

`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` lines 150–156, quoted
whole: "Stop and return to the owner before proceeding if implementation would
need any of: a change to doctrine or an accepted contract; a further amendment
to the signed PWB specification beyond the 2026-09-05 package; a change to
security, privacy, or retention posture beyond the 2026-09-05 approved
secret-classification policy; a change to the constraints or envelope the
2026-09-05 registry entry declares; any observation outside the consented
content class or repository; or any scope beyond the signed change."

`THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lines 55–56, quoted whole:
"Improvement-cycle work must trace to POC-REQ-001..061 or to a recorded review
finding."

| Slice | Owner act needed | What it traces to | The trigger test |
|---|---|---|---|
| 1 Links map | **No**, per Q4's recommended reading | A recorded review finding (S6-F2). No requirement in either specification names endpoint self-description; swept this session over 24 three-surface requirements and 24 scenarios and 17 PWB requirements and 31 scenarios, **0** do | No trigger crossed: no doctrine or contract change, no specification amendment, no security-posture change, no registry-envelope change, no new observation. A field naming routes the daemon already serves |
| 2 Response identity | **No on the recommended arm of Q1; yes on its second arm** | POC-REQ-004 on the recommended reading — "two code-structure observations of R SHALL produce identical fact content", spec lines 188–189, with its oracle "structural diff excluding declared capture-instant fields" at lines 199–200. On Q1's second arm, a recorded review finding only (S6-F6) | The trigger at stake is "any scope beyond the signed change". Reading a code-structure determinism requirement as warranting a whole-payload identity is the widening Q1 names [Inferred] |
| 3 Schema document | **Yes for the route's credential class (Q3); no otherwise** | A recorded review finding (S6-F1, S6-F2). No requirement names a schema document; the literal sweep for `json-schema`, `openapi` and `schema document` over the three-surface specification returns **0** lines | If served `human-open`, the trigger is "a change to security, privacy, or retention posture" read through SEC-1. If served `machine-credentialed`, no trigger is crossed |
| 4a Conditional GET | **No**, and it is deliberately separated from 4b for this reason | A recorded review finding (S6-F4), keyed on slice 2's identity | No trigger: an `ETag`/`If-None-Match` exchange changes no declared limit, no observation, no posture. It does change what a client may believe, which is why VIS-2 puts it behind slice 2 |
| 4b Compression | **Yes — Q2** | A recorded review finding (S6-F4) | "A change to the constraints or envelope the 2026-09-05 registry entry declares", on the reading that `Content-Encoding` changes what "the final encoded HTTP body" names. This packet does not choose the reading; it records that the change is invisible to every test in the repository and visible only in the registry's sentence |
| 5 Stable join key | **Yes — Q5**, and sequenced behind M9 either way | A recorded review finding (S6-F5). PWB-REQ-014's closed-class sentence (PWB spec lines 774–776) constrains the derivation; RFC1-9's minting-authority rule constrains who may mint it | "A change to doctrine or an accepted contract" is **not** crossed by adding a sibling field — but whether a path-derived value may be an identity at all is a reading of an accepted contract, which is what Q5 puts |
| 6 (carried) | not evaluated | M2's packet owns it | not evaluated |
| S6-M4 populate-or-prune | **Yes — a specification amendment** | PWB-REQ-014 lines 774–776 declare the six classes closed | "A further amendment to the signed PWB specification" — CC-REV-2 plus a new owner act. **Listed, not scheduled** |

**What landing these slices retires.** No act binds any implementation byte a
slice touches (Gate 0's sweep). **22** files of the 624-file governance and
evidence corpus name at least one of the five implementation paths these
slices touch, and **none** of them carries the current sha256 of any of those
files [Observed, both sweeps run this session; predicates in the evidence
record]. So no confirmation currently bound to
those bytes is retired. What the implementing beads owe is a re-run of the
parity sweep and of the mutation records that name the touched paths, before
any repaired claim is made — verification rule 10 applied to an evidence
record rather than to a review.

All slices run under `syzygy-dov.10`, the pursuit bead; this packet files no
new bead.

## Gate 4 — Design sketch, per slice

### Slice 1 — The route table answers "what else is there" (small; no act per Q4)

**The field.** `/api/poc` gains one top-level object built from the array
`pocRoutes()` already returns, so it cannot drift from the real route list:

```
links: { path: string; method: 'GET'; credentialClass: 'human-open' | 'machine-credentialed'; self: boolean }[];
```

Built by mapping over the same `readonly Route[]` the function returns,
filtering nothing, so the 15 entries in the table become 15 rows. The tailnet
duplicates are kept rather than collapsed: they are real, separately
registered paths, and an agent reaching the daemon through the mount needs the
prefixed form. The presentation envelope gains the identical field, so either
endpoint answers the question.

**Where it must not be built.** Not from a hand-written list, and not from the
`*_PATH` constants at lines 15–22 — both can drift from the returned array.
The one source is the array itself.

**Oracle.** An independently written test that calls `pocRoutes()`, projects
`(path, method, credentialClass)` out of the returned array with its own code,
serves the body, parses it, and compares the two as multisets — the shape the
parity sweep already uses, and hard-coded expected counts as literals in the
test, never imported from the module under test.

**Rule-6 mutants.** (a) Add a route to `pocRoutes()` and not to the links
projection; the test must fail on a denominator mismatch. (b) Build `links`
from the `*_PATH` constants instead of the array; the tailnet forms disappear
and the test must fail. (c) Drop the `credentialClass` field; the test must
fail on the tuple, not merely on a count — which is the per-tuple discipline
AGENTS.md records for PWB-REQ-020 parity, applied here.

**Trade-offs rejected.** A hypermedia link-relation vocabulary (nothing needs
it; it invents a second encoding for a 15-row table). Collapsing the tailnet
duplicates (loses the prefix an agent behind the mount needs). Including the
human routes' *content* (that is M5's briefing, not this).

### Slice 2 — One response identity, and the payload says which field it is (medium; act per Q1)

This is the packet's central slice and the one the dossier does not have: its
S6-M5 proposes documenting the equality contract, and the measurement says the
contract as it stands cannot be documented truthfully, because neither
candidate key is correct.

**The field.**

```
responseIdentity: {
  contentKey: string;             // sha256 over the canonical body minus the exclusions
  excludes: readonly string[];    // the declared exclusion paths, as structural paths
  stableAcross: readonly string[];// e.g. ['daemon restart at one evaluation input set']
  varyingWith: readonly string[]; // e.g. ['butlers revision', 'observer revision', 'project shape']
};
```

**How `contentKey` is computed.** Canonically serialize the response body with
sorted keys, delete every value at a declared exclusion path, and sha256 the
result. The exclusion set is not invented: it is the 25 measured paths above,
declared as data in one place and quoted into the payload, so a reader can
check the claim rather than take it. A field added later that carries the run
instant and is not added to the set is a defect the oracle catches.

**Why not extend `inputsDigest`.** Because a landed test asserts its current
scope on purpose (`model.test.ts` lines 341–343, quoted in the measurements),
and that assertion is about the Capability 1 proving slice's identity, not
about the served response. Widening it would break a test that is right.
`contentKey` is a second, differently scoped value, and the payload says which
is which — which is the whole of S6-M5.

**Oracle.** Three independently written fixtures with expected outcomes as
literals: (a) two builds differing only in `evaluation.asOf` → equal
`contentKey`, unequal whole-body hash; (b) two builds differing in one
project-shape byte → unequal `contentKey`, **equal** `inputsDigest` — the
counterexample that proves the new key is doing work the old one cannot; (c) a
build with a new instant-bearing field absent from `excludes` → the identity
test fails.

**Rule-6 mutants.** (a) Remove one path from `excludes`; fixture (a) must
fail. (b) Include `evaluation.asOf` in the hashed body; fixture (a) must fail.
(c) Hash with unsorted keys; a re-serialization test must fail. (d) Point
`contentKey` at `inputsDigest`; fixture (b) must fail — and this is the
mutant that matters most, because it is the design the dossier proposes.

**Trade-offs rejected.** A per-key digest map (19 more fields, and no consumer
asked for partial invalidation). Excluding whole top-level keys rather than
paths (would exclude `projectShape` entirely, which is the error
`inputsDigest` already makes). Making `contentKey` the ETag directly in the
same slice (that is 4a, and it is separated so that a wrong validator cannot
reach a client before it is tested).

### Slice 3 — A schema document for both endpoints (large; act per Q3)

**Costed honestly first.** 769 structural paths and 241 field names in
`/api/poc`, 57 and 48 in the presentation envelope, 273 names in union; 14 of
`PocModel`'s 19 top-level fields and all 7 of the envelope's carry no doc
comment. The dossier's slice plan — enumerate existing TSDoc — describes work
that cannot be done, because the TSDoc is mostly absent. This slice is
therefore **authoring**, and it is large.

**The shape.** A static document emitted at build time from the TypeScript
types, checked into no source tree and served from a new route. Emission from
the types rather than hand-authoring is what keeps it from drifting; the
*prose* per field is hand-written and is the cost.

**What it must state, beyond types.** Per PWB-REQ-020's warrant and the S6
finding this slice answers: for each declared enum, which members are
**populated for this evaluation** and which are declared and empty — computed
from the served body at emission time, never asserted. For this evaluation
that statement reads: `anchorTargetClasses` 3 of 6 populated
(`evidence` 914, `requirement` 1, `work` 1; `doctrine`, `contract` and
`decision` 0), `roles` 1 of 3 (`anchored-project-fact` 714). It must **not**
prune: the six classes are closed by PWB-REQ-014 lines 774–776 and pruning is
an amendment.

**Where the honest line is.** The document describes; it does not promise. A
field's presence in the schema is not a claim that the field is populated, and
the populated-member statement is the mechanism that keeps those two apart.

**Oracle.** A test that walks the served body and the emitted schema and
compares path sets both ways, reporting both denominators: a body path with no
schema entry fails, and a schema entry matching no body path is reported (not
failed — a field may be legitimately absent at one evaluation, which is the
`materializedBeadId: null` case).

**Rule-6 mutants.** (a) Add a field to `PocModel` without regenerating; the
path-set test must fail. (b) Hand-edit one type in the emitted schema; a
regeneration-and-compare test must fail. (c) Change one anchor's `targetClass`
in a fixture so a fourth class becomes populated; the populated-member
statement must change, proving it is computed and not transcribed.

**Trade-offs rejected.** OpenAPI (the endpoints are two GETs with no
parameters; the format's whole apparatus is unused). Hand-writing the schema
(it drifts, which is the defect). Serving a checked-in file from the
repository (then it is not derived from the types that are compiled).

### Slice 4a — Conditional GET on slice 2's identity (small; no act)

`ETag: "<contentKey>"` on both machine routes; `If-None-Match` handled in the
daemon's admission path so a match returns 304 with no body. Credential
admission runs **first**, unchanged: a refused credential must never learn
that its cached copy is current, which is the RFC5-3 posture
`packages/cap1-daemon/src/server.ts` lines 188–200 already implements and this
slice must not weaken.

**Oracle.** A served-daemon test: GET, capture the ETag, GET again with
`If-None-Match` → 304 and zero body bytes; restart the daemon at the same
inputs → same ETag; change one project-shape byte → different ETag and a 200.
Plus one negative: `If-None-Match` with a valid ETag and **no** credential →
the same refusal as today, never a 304.

**Rule-6 mutants.** (a) Key the ETag on `inputsDigest`; the changed-shape case
must fail with a wrongly-served 304 — the failure that names the bug. (b) Key
it on the whole-body hash; the restart case must fail. (c) Move the
`If-None-Match` check before credential admission; the negative test must
fail.

**Why it is rank 5.** VIS-1 puts caches last. This slice is worth building
because 5.5 MB per poll is real, and it is sequenced last among the
non-gated slices for exactly the reason the clause gives.

### Slice 4b — Compression (gated; act per Q2)

Not designed here beyond its gate. `Accept-Encoding: gzip` honored above a
threshold, `Vary: Accept-Encoding` set. The design question this packet will
not answer is the one Q2 puts: whether `boundedResponse` then measures the
compressed bytes or keeps measuring the string. Whichever the owner rules, the
bead must record the ruling, because the two readings differ by a factor of
6.5 on the machine body and 14 on the human page and nothing in the test suite
can tell them apart.

### Slice 5 — A stable cross-revision join key (medium; act per Q5; behind M9)

**The field.** Beside the existing revision-scoped `targetId`, a sibling:

```
logicalId: string;   // opaque, revision-independent, never an anchor identity
```

**What it must satisfy.** RFC1-9's determinism ("two runs over the same inputs
mint the same identity"), RFC1-10's opacity (never a label, never reused), and
PWB-REQ-014's prohibition — which is why the field is a *sibling* and the
anchor identity is untouched. The derivation is Q5: from path plus normalized
statement (joins across a content edit, and is path-derived); or from the
object id the source route already carries (satisfies both clauses, and does
not join across a content change). This packet does not choose.

**Sequencing, stated rather than assumed.** M9's slice 6(b) mints a
cross-*surface* key at one evaluation; this mints a cross-*revision* key
across two. They are different axes, and this packet's reading is that they
are **not** the same change [Inferred — a reading of two packets' designs, not
a measurement]. But both mint identities in the same constructors
(`polaris-narrative.ts` lines 102–125), so building them independently mints
two schemes for one subject. Whichever packet is ruled first owns the
constructor; the second adds its field to what the first built.

**Oracle.** A fixture with one claim at two Butlers revisions: equal
`logicalId`, unequal `targetId`, and the `targetId` byte-identical to what it
is today.

**Rule-6 mutants.** (a) Include the revision in the `logicalId` derivation;
the two-revision fixture must fail. (b) Let the `logicalId` replace
`targetId` anywhere; the byte-identity assertion on `targetId` must fail. (c)
Use the `logicalId` as an anchor identity in one block; a PWB-REQ-014
conformance test must fail.

### Slice 6 (carried, not scheduled) — the `evidence` block

L4-M2's machine half — mirroring the revision, committed instant and capture
instant as a top-level `evidence` object on both machine endpoints — is
designed in M2's packet
(docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md, read read-only in that
worktree at `f2f37dd`), whose Gate 3 already names
`apps/three-surface-poc/src/routes.ts`. M10 carries it so the dossier's merge
list is discharged and schedules it nowhere. If both land, the `evidence`
block's instants belong in slice 2's `excludes` set; the implementing bead for
whichever lands second owes that edit.

### Design bar for the human surface

**None of M10 reaches a rendered surface.** Every slice adds a machine-side
field, a machine-side document or a machine-side header. That is stated rather
than assumed because it is what makes Q6 answerable at all: there is no human
counterpart to keep in parity because there is no human rendering.

## Gate 5 — Specification

Two signed specifications are in force over this surface: the three-surface
change (24 requirements, 24 scenarios) and the PWB change (17 requirements, 31
scenarios). Both are act-bound and neither may be edited by any slice.

### Does the machine channel's contract need a delta?

**Per slice, and the answer is not uniform.**

**Slice 1 — no delta, and no requirement either.** Swept this session over
both specifications: **0** of the 41 requirements and **0** of the 55
scenarios name endpoint self-description, a links map, a route list or
sibling-route discovery. A literal sweep for `self-link`, `sibling route` and
`endpoint list` or `endpoint map` over the three-surface file returns **2**
lines, both in POC-REQ-053 (spec lines 904 and 913), which is Orrery
entities
resolving to exact-table routes and not endpoint discovery — the remainder is
enumerated rather than waved at, per verification rule 9. So slice 1 adds a
field no requirement asks for and no requirement forbids. That is the
RFC2-26 question, run below, not a delta question.

**Slice 2 — a delta only on Q1's second arm.** On the recommended arm the
argument is a quotation, not a reading: POC-REQ-004 requires that "two
code-structure observations of R SHALL produce identical fact content" (spec
lines 188–189) and its oracle is a "structural diff excluding declared
capture-instant fields" (lines 199–200), with the falsifier "any fact field
differing between the two runs" (line 202). A response identity computed over
the canonical body minus a declared capture-instant exclusion set is that
oracle, made available to the consumer instead of only to the checker. The
residue is the scope word: POC-REQ-004's quantification is "all served
code-structure facts" (lines 190–191), and `codeStructure` is 27.05% of the
body. Whether a requirement scoped to one region warrants an identity over the
whole payload is Q1 and is not settled here.

**Slice 3 — no delta; the disclosure it carries is the thing PWB-REQ-014
already closes.** PWB-REQ-014 lines 774–776 declare the six anchor classes
closed. Stating which of the six are populated at an evaluation neither adds
nor removes a member; it is a measurement of the payload printed beside the
closed list. **Pruning** would be a delta, and that is S6-M4, listed here and
scheduled nowhere.

**Slices 4a, 4b and 5 — no delta proposed, and two of the three need an act
for a different reason.** 4b's gate is the registry's declared semantics, not
a requirement; 5's is PWB-REQ-014's prohibition read against a sibling field.
Neither proposes changing requirement text.

### The RFC2-26 test, run over all seven slice rows

RFC-0002 is an accepted design contract in force. Its phase rule, quoted
verbatim and whole at the defined clause,
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` lines
196–221, under the `###` heading at line 194:

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
> `decisions/` (RFC3-15), and the judgment is honored only through an effective
> owner act under RFC3-16(a), in state (1) or state (2), with that state rendered;
> absent or invalid acts map nothing and leave the consequence unmapped and
> Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2).
>
> **Rows are per observable consequence, not per clause.** A clause with five
> observable consequences and one mapped requirement is not covered; the matrix
> discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of the
> matrix. At surface specification a
> clause-to-requirement coverage matrix over RFC2-1..RFC2-26 is produced —
> **that matrix is review material, never authority**. This clause creates no
> OpenSpec content now (none may exist during bootstrap). This clause binds the
> whole RFC 0002 package, not this module alone. (Shape-parallel with RFC6-28,
> RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12.)

RFC-0001 carries the shape-parallel clause and it matters here more than
RFC2-26 does, because its own consequence list names this surface directly.
RFC1-33, quoted at the defined clause in
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`,
lines 750–755, at the enumerating sentence: "No implementation work for
user-observable consequences of this contract — project registration and
declaration validation flows, entity and relation rendering, lifecycle and
succession displays, proposal and materialization surfaces, **API answers over
graph identities** — may be scheduled solely from this RFC." Slice 5 mints an
identity and serves it in an API answer; it is the one slice both clauses
reach.

**The denominator is seven**: the seven rows of Gate 3's act table — slices 1,
2, 3, 4a, 4b, 5 and the carried slice 6 [Observed, counted over that table
this session]. S6-M4 is not a slice and is not a row. Every requirement and
scenario cited below was read at source this session in the signed files.

| Slice | RFC2-26 / RFC1-33 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Links map | **None enumerated.** A list of the daemon's own route paths is not an evaluation display, a claim or challenge rendering, an Unknown-reason presentation, a reconciliation or gap surface, an API answer over epistemic state, or an API answer over graph identities. It is an answer about the server, not about the project | n/a | n/a. Neither clause is engaged. Slice 1 is scheduled from a recorded review finding under the improvement-cycles direction, not from an RFC |
| 2 Response identity | **"API answers over epistemic state"** — arguably. A content key over the served body is a statement about the *evaluation*, and evaluation identity is epistemic state; but the key is a digest of bytes, not a label, tier, reason or freshness. This packet reads it as engaged and runs limb 1 rather than claiming exemption [Inferred] | **POC-REQ-004**, spec line 184, scenario **"Repeated observation at one commit"** at spec lines 204–208, quoted verbatim: "**WHEN** observation runs twice at commit R with identical inputs / **THEN** the served code-structure facts are identical apart from capture instants" | **Available, and partial.** The requirement and a scenario both exist and both say the right thing — but both are scoped to *code-structure* facts, and the slice's key spans the whole payload. Limb 1 is satisfied for 27.05% of the body by the scenario's own words and is a widening for the rest. That is Q1, and this packet calls the slice neither lawful nor unlawful on it |
| 3 Schema document | **None enumerated for the document itself** — a description of field names and types renders no claim and answers no query over epistemic state. **One enumerated for the populated-member statement**: "Unknown-reason and rendering-tier presentation" is the nearest class, and a statement that three of six declared anchor classes are empty is adjacent to it without being it [Inferred] | For the populated-member statement: **PWB-REQ-014**, PWB spec line 759, scenario **"A project claim is supported without making Polaris authority"** at PWB spec lines 799–803, quoted verbatim: "**WHEN** Polaris states one project fact / **THEN** the fact's bounded claim block identifies its exact source anchor / **AND** both human and machine forms mark the block non-citable presentation". **The scenario does not state the empty-member case**, which is the statement's actual subject [Observed: every scenario heading under PWB-REQ-014 was read this session — there is exactly **one**, at line 799 — and it does not] | **Requirement available, scenario absent for the one enumerated consequence.** The clause's bar is "an approved OpenSpec requirement **and** scenario". This packet does not rule slice 3 lawful or unlawful; it records the two repair routes the clause itself names: a scenario added through CC-REV-2, or a reviewed N/A judgment homed in `decisions/` and honored through an effective act under RFC3-16(a). This packet's view of the second's reachability: **plausible here**, because a statement computed from the payload and asserted by a test is arguably "purely structural" — unlike M6's slice 4, which the clause's "no independently testable behavior" plainly excludes. Whether it is reachable is the owner's, and saying so is the disclosure [Inferred] |
| 4a Conditional GET | **"API answers over epistemic state"** — a 304 is an assertion that the client's copy is current, and currency is VIS-2's own word | Same as slice 2: **POC-REQ-004** and the "Repeated observation at one commit" scenario, since 4a serves exactly the identity slice 2 computes and adds no new statement | **Inherited from slice 2, with slice 2's residue.** 4a maps wherever 2 maps and nowhere further |
| 4b Compression | **None enumerated by RFC-0002 or RFC-0001.** A content coding renders nothing and asserts nothing about the project | **PWB-REQ-006**, PWB spec line 340, scenario **"Resource breach is bounded and explicit"** at PWB spec lines 419–426, whose **AND** reads verbatim: "human and machine responses stay within their own declared encoded-byte ceilings and cold-open readiness is false". The requirement text at lines 378–379 reads, across both lines: "Final encoded human HTML and machine JSON SHALL each have an explicit byte ceiling." | **Available — and it is the requirement that makes 4b a gate rather than a convenience.** A requirement *and* a scenario both exist and both turn on the words "encoded" and "encoded-byte", which is precisely the ambiguity Q2 puts. Limb 1 is satisfied; the slice is still gated, because satisfying limb 1 is not the same as knowing which reading the requirement bears |
| 5 Stable join key | **RFC1-33's "API answers over graph identities"** — enumerated, explicitly, by name | **PWB-REQ-014**, PWB spec line 759 (the closed-class and durable-identity sentence at lines 774–776), scenario at lines 799–803 as above. **The scenario constrains the anchor, not a sibling join key**, which is slice 5's actual subject | **Requirement available, scenario partial.** The requirement governs what the slice must not do (make the key an anchor identity); no scenario states what it must do. Same two repair routes as slice 3, and the N/A route is **less** reachable here: a join key that resolves the same claim across two revisions is independently testable by construction, which is what the clause's N/A limb excludes [Inferred]. Q5 is where this goes |
| 6 (carried) `evidence` block | **[Unknown].** Designed in M2's packet, not here; its consequences are enumerated there | M2's packet runs its own test over it | Not run here. Naming it and not running the test is the honest form; running it over a design this packet has not made would be the dishonest one |

**What this test establishes and what it does not.** It establishes
[Observed] that slices 2 and 4a map to a named requirement-and-scenario pair
whose scope is narrower than the slice, that slice 4b maps to a
requirement-and-scenario pair squarely on its subject, that slices 3 and 5
name requirements with no scenario for their actual case, and that slice 1
enumerates no consequence of either contract. It does **not** establish that
any slice is lawful; that is Q1 through Q6, and RFC2-26's own scope sentence —
"This clause binds the whole RFC 0002 package, not this module alone" (lines
219–220) — is a reading the owner may take more or less broadly than this
packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed specification text and nothing here amends a requirement.

**S1 (slice 1).** WHEN `/api/poc` is served, THEN its `links` array has one
row per entry of the array `pocRoutes()` returns, AND a route added to that
array without a corresponding row makes the test fail on a denominator
mismatch, not on a spot check.

**S2 (slice 1).** WHEN the links projection is built from the `*_PATH`
constants instead of the returned array, THEN the test fails, AND the failure
names the missing tailnet-mounted forms.

**S3 (slice 2).** WHEN two models are built from identical inputs differing
only in `evaluation.asOf`, THEN their `responseIdentity.contentKey` values are
equal, AND a sha256 of the two whole bodies differs.

**S4 (slice 2).** WHEN two models are built differing in exactly one
project-shape byte, THEN their `contentKey` values differ, AND their
`inputsDigest` values are equal — the second clause is the assertion that
proves the new key does work the old one cannot.

**S5 (slice 2).** WHEN a field carrying the run instant is added to the model
and not added to `responseIdentity.excludes`, THEN S3 fails, AND the failure
names the path.

**S6 (slice 3).** WHEN the schema is emitted, THEN every structural path of
both served bodies has an entry, AND the check reports both denominators —
769 and 57 at this evaluation — rather than a bare pass.

**S7 (slice 3).** WHEN the schema states which enum members are populated,
THEN the statement is computed from the served body at emission time, AND
changing one anchor's class in a fixture changes the statement.

**S8 (slice 4a).** WHEN a credentialed GET is repeated with `If-None-Match`
set to the ETag the first response carried, THEN the response is 304 with zero
body bytes, AND an uncredentialed request with the same header receives the
existing refusal and never a 304.

**S9 (slice 4a).** WHEN the daemon is restarted at the same evaluation inputs,
THEN the ETag is unchanged, AND WHEN one project-shape byte changes, THEN the
ETag changes and the response is 200.

**S10 (slice 5).** WHEN one Butlers claim is evaluated at two revisions, THEN
its `logicalId` is equal across both and its `targetId` differs, AND the
`targetId` is byte-identical to what it is today.

**S11 (slice 5).** WHEN a `logicalId` is used as an anchor identity anywhere,
THEN a PWB-REQ-014 conformance test fails, AND the failure names the
closed-class sentence.

## Collision and sequencing

Nine sibling packets are in flight. **Under the branch-diff predicate the
intersection is zero everywhere; under the proposed-files predicate it is the
largest of any packet in this pursuit.** Both are reported, because they
answer different questions and only the second is about collision.

**Predicate A — what each sibling branch has actually changed.**
`git diff --name-only a9f671e <sibling HEAD>`, intersected with M10's 9-file
candidate surface (`apps/three-surface-poc/src/routes.ts`,
`apps/three-surface-poc/src/polaris.ts`,
`apps/three-surface-poc/src/polaris-narrative.ts`,
`apps/three-surface-poc/src/polaris-parity-sweep.test.ts`,
`apps/three-surface-poc/src/main.ts`,
`packages/three-surface-poc-core/src/model.ts`,
`packages/three-surface-poc-core/src/project-shape-model.ts`,
`packages/cap1-daemon/src/server.ts`, `package.json`).

**Predicate B — what each sibling packet's Gate 3 topology table proposes to
touch.** The Gate 3 section of each packet, read read-only in that packet's
own worktree, searched for each of M10's nine paths. This is the reliance
predicate: a path named in a measurement paragraph is a citation and not a
claim (verification rule 5), and the Gate 3 table is where a packet says what
it would edit.

| Sibling | PR | Register | Head read this session | Files changed on the branch | A: branch ∩ M10 | B: Gate 3 ∩ M10 | Which of M10's files |
|---|---|---|---|---:|---:|---:|---|
| lane B | #35 | P-68 | `4090f98` | 22 | **0** | **0** | — |
| M2 | #36 | P-69 | `f2f37dd` | 9 | **0** | **4** | `routes.ts`, `main.ts`, `model.ts`, `project-shape-model.ts` |
| M3 | #37 | P-70 | `6574600` | 10 | **0** | **1** | `polaris.ts` |
| M4 | #38 | P-71 | `63b8e33` | 10 | **0** | **5** | `routes.ts`, `polaris.ts`, `polaris-parity-sweep.test.ts`, `model.ts`, `project-shape-model.ts` |
| M5 | #39 | P-72 | `ba9ca61` | 7 | **0** | **3** | `routes.ts`, `polaris.ts`, `model.ts` |
| M6 | #40 | P-73 | `83c9f60` | 5 | **0** | **1** | `package.json` |
| M7 | #42 | P-76 | `f97baf4` | 5 | **0** | **2** | `routes.ts`, `package.json` |
| M8 | #43 | P-74 | `bce9039` | 5 | **0** | **5** | `routes.ts`, `polaris.ts`, `main.ts`, `model.ts`, `project-shape-model.ts` |
| M9 | #41 | P-75 | `65de02b` | 5 | **0** | **3** | `routes.ts`, `polaris.ts`, `model.ts` |

[Observed, all eighteen intersections computed this session. Predicate A's
zeros are not reassurance: every sibling branch is planning-only — each
changes only files under `docs/design/`, `docs/evidence/`, `docs/reviews/` and
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`, and lane B
additionally `scripts/`, `.github/` and its own amendment package. M6's head
has advanced since its own packet recorded `e318cbd`; the head above is the
one read this session.]

**The load-bearing number is `routes.ts`: six of the nine sibling packets
propose to edit it.** M2, M4, M5, M7, M8 and M9 all name it in Gate 3, and so
does M10 in four of its seven slices. The core model file
`packages/three-surface-poc-core/src/model.ts`
is named by five (M2, M4, M5, M8, M9) plus M10;
`packages/three-surface-poc-core/src/project-shape-model.ts` by three (M2, M4,
M8) plus M10; `apps/three-surface-poc/src/polaris.ts` by five (M3, M4, M5, M8,
M9) plus M10. **No file in this pursuit is uncontended.** That is a scheduling
fact the owner should see before ruling any of the nine, and it is the reason
this packet's handoff recommends landing order rather than parallel execution.

**The three specific collisions the pursuit names, resolved.**

1. **M5 (P-72, PR #39) owns the machine channel's task-scoped route and
   dispatch packet.** M5's slice 3 is `GET /api/poc/briefing?for=<selector>` —
   a *new route with a query parameter*, which is the query interface M10
   explicitly does not build. M10's slice 1 is a links map over the routes
   that exist; if M5's briefing route lands, it appears in that map for free,
   because the map is projected from the route array. The two are
   complementary and the ordering is free. **No duplication.**
2. **M2 (P-69, PR #36) owns the `evidence` block this move's L4-M2 slice would
   carry.** M10 carries it as slice 6 and schedules it nowhere; M2's packet
   designs it. The one coupling is stated in Gate 4: if both land, the
   `evidence` block's instants belong in slice 2's exclusion set, and
   whichever lands second owes that edit.
3. **M9 (P-75, PR #41) proposes a stable cross-revision identity — and it does
   not.** This is the collision the pursuit asks to be resolved, and the
   resolution is that the two are **different changes**. M9's slice 6(b)
   (packet lines 920–925) makes the artifact identity the source route
   already mints the canonical **cross-surface** join key — one string for
   one artifact across
   Polaris, Trajectory and Orrery *at one evaluation*, with the revision still
   embedded. M10's slice 5 is a **cross-revision** key: the same claim at two
   revisions. Neither subsumes the other. But both mint identities in the same
   constructors, so **M10's slice 5 sequences behind M9's packet** and adds
   its field to whatever M9's slice 6 builds, rather than minting a second
   scheme.
   If the owner prefers one packet to own identity entirely, Q5's second arm
   folds slice 5 into M9 and drops it here [Inferred — a reading of two
   packets' designs; the packets' own words are quoted above and in Gate 4].

**M4 (P-71, PR #38) and M3 (P-70, PR #37) touch `polaris.ts`.** So does M10's
slice 5, at lines 407–409 and 1078 — the two anchor-constructor call sites.
M3's Gate 3 names `polaris.ts` for the encoding work and M4's for the owner
loop; neither names those two lines [Observed, both Gate 3 sections read this
session]. The collision is the file, not the region, and a rebase resolves it;
the ordering constraint that is real is slice 5 behind M9, not behind M3 or
M4.

**Sequencing inside M10.** Slice 1 is independent of everything and is the
cheapest thing here. Slice 2 must precede slice 4a — an ETag on the wrong
validator is worse than no ETag, which is the VIS-2 argument in Gate 2. Slice
3 is independent of 1 and 2 but reads better after both, because a schema
describing a `links` field and a `responseIdentity` field is a schema of the
contract M10 is actually proposing. Slice 4b is behind Q2 and behind nothing
else. Slice 5 is behind Q5 and behind M9.

**The register.** This packet's six questions are **not** registered in
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`; the register row
lands after review 1, batched with the other repairs, and the next free number
is **P-77** (P-68 through P-76 are held by the nine siblings, each only on its
own branch; verified this session with the predicate `^| P-` over all ten
worktree registers and main's).

**Not verifiable this session.** [Unknown] Whether any sibling branch's
eventual diff stays inside the paths its packet's Gate 3 names — none has an
implementation commit yet. [Unknown] Which arm the owner takes on Q1, and
therefore whether slice 2 is an implementation or an amendment. [Unknown]
Whether the registry's "final encoded HTTP body" bears the pre- or
post-compression reading; both are grammatical and the file may not be edited
to say which.

## Gate 6 — Engineering bar

1. **Every count in this packet carries its predicate and its denominator**,
   and every one was taken this session in the worktree at `a9f671e` or on a
   named retained capture. Where a figure is a property of a capture rather
   than of the code, the capture and its Butlers revision are named in the
   table at the top of the measurements.
2. **Two methods for the two load-bearing zeros.** "No caching or negotiation
   header exists" is established by a word-bounded Python `re` sweep over 104
   files and by `git grep -F -i` over the same two directories; the two agree,
   and the naive substring predicate that would have produced a false positive
   is named. "Three anchor classes are empty" is established by a population
   census over two independently captured bodies and by a construction-site
   census over 72 production modules; the two agree and each adds something
   the other cannot see.
3. **The central claim is established by a counterexample, not by reading.**
   That `inputsDigest` is unsound as an ETag is not an inference from its
   preimage: it is a landed, passing assertion at
   `packages/three-surface-poc-core/src/model.test.ts` line 343, run this
   session as part of that file's 8 passing tests, that a model with an
   observed project shape and a model with none have the same value.
4. **Rule-6 mutants are specified per slice and per guard branch**, above;
   each names the predicate to mutate and the fixture that must then fail. The
   mutant that matters most is slice 2's (d) — point `contentKey` at
   `inputsDigest` and watch fixture (b) fail — because that is the design the
   dossier proposes and the one this packet declines.
5. **Conformance expected values are literals in the tests**, never imported
   from the module under test (AGENTS.md).
6. **The copy-oracle caution is applied** where it bites: slice 1's oracle
   compares tuples, not counts, and slice 3's path-set comparison reports both
   denominators, because a substring or a count is reached by coincidence.
7. **The baseline is green and was run, not assumed.** In this worktree at
   `a9f671e`: `packages/three-surface-poc-core/src/model.test.ts` 8 passing;
   `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` 43 passing;
   `apps/three-surface-poc/src/response-limits.test.ts` 12 passing;
   `apps/three-surface-poc/src/polaris-presentation-route.test.ts` 2 passing —
   57 tests over 3 files in the second run, 8 in the first. A short git
   status in the worktree names only this packet's two files.
8. **No act-bound byte is proposed for edit**, and that is a claim about
   *acts* specifically. The two specifications and the observer registry entry
   are act-bound and no slice touches them. The implementation files are not
   act-bound; 22 governance and evidence files name them by path and none
   carries their current digests, so editing them retires no bound
   confirmation — but the implementing beads owe a re-run of the records that
   name the paths.
9. **A false-absence trap was hit and corrected in this pass.** The first
   digest-binding sweep looked for repository-relative paths only and reported
   the three-surface specification as bound by nothing. It is bound by
   `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`, which names its artifacts
   *act-relatively*: line 46 reads
   `specs/three-surface-poc-experience/spec.md`.
   The sweep in Gate 0 runs both forms. This is the "index that routes by
   short
   name" class AGENTS.md records, and it is reported rather than silently
   fixed because the corrected predicate is what the reader should check.
10. **Independent review.** This packet has had **none**. It is a first draft,
    and every figure in it is uncovered until a fresh-context review confirms
    it. Verification rule 10: any later edit to these bytes retires a review
    bound to them, so superseded wording will be marked and dated in place,
    never deleted.
11. **Conventions this packet was checked against, this session.** Every
    non-fence line has an even backtick count, so no code span is broken
    across a line break (0 of **1,328** non-fence lines). **Two** lines
    exceed 78 columns outside fences, tables, headings and block quotes, and
    each is a single unbreakable code-span path: the observer registry entry
    and the RFC-0001 filename. Of **273** distinct code spans, **57** contain
    a `/` and **13** of those do not resolve as a path in this worktree; each
    is enumerated here and none is a path in it. They are: four write-root
    globs (`.syzygy/**`, `openspec/**`, `apps/**`, `packages/**`); four
    served route forms (`/api/poc`, `/api/poc/polaris`, `/polaris`, and M5's
    proposed `GET /api/poc/briefing?for=<selector>`, which is a route plus a
    query and not a file); RFC2-26's own bare `decisions/`; the model's
    version label `syzygy-three-surface-poc/v1`; this worktree's branch name
    `agent/syzygy-dov.10`; the act-relative form
    `specs/three-surface-poc-experience/spec.md`, quoted because the
    false-absence trap in item 9 turns on exactly that spelling; and the
    command `python3 scripts/check_governance.py`, whose script half does
    resolve while the command as written is not a path. The six
    retained-capture paths and the two sibling packets' paths are named
    **without** code spans, because they resolve in the session scratch
    directory and on other branches rather than in this worktree. No
    observed-repository path is backticked anywhere in this file; no act
    argument, manifest digest or signed digest is reproduced, and every
    digest record consulted is cited by path, per CG-7e and CG-15; and no
    revision short form is written with a trailing ellipsis, which CG-15
    reads as a truncated digest quote. `python3 scripts/check_governance.py`
    was run in this worktree after the final edit and its last line reads
    **32 OK, 20 WARN, 0 FAIL (52 checks)**. Every figure here was re-derived
    over these bytes rather than carried forward from an earlier draft; the
    first draft's figures, before the code-span and ellipsis repairs, were
    1,312 non-fence lines, 278 distinct spans and 20 non-resolving
    slash-bearing spans, and two checks then failed.

## Funnel summary

```
## Feature Request: M10 - The machine consumer gets a contract
Size: small (slices 1, 4a) / medium (slices 2, 5) / large (slice 3) / gated (slice 4b)
Baseline: Syzygy a9f671e; the dossier audited at f4589e2, and every line number it cites is re-verified above
- G1 Motif: the machine channel has no identity of its own. Hashing the body is wrong by 1,436 embedded wall-clock substrings over 25 structural paths touching 6 of 19 top-level keys; the one digest the payload carries, inputsDigest, is wrong by the entire project-shape block, which a landed passing test asserts it excludes on purpose (model.test.ts:343). 0 caching or negotiation headers exist across 104 files, 1 writeHead. Neither endpoint names the other: 0 occurrences of either route path in either body. 3 of 6 declared anchor classes have 0 construction sites or 0 rendered anchors; doctrine and contract have 0 construction sites at all [Observed, every figure measured this session with its predicate and denominator]
- G2 Doctrine: VIS-1's ordering puts the response identity (rank 1, observation determinism) above the schema (rank 2, comprehension) above the cache (rank 5, named in the clause's own parenthesis); VIS-2 is why an ETag may not be built on inputsDigest; SEC-1 is Q3 and reaches only the schema route's credential class; RFC1-9/10/12 bound slice 5's derivation
- G3 Topology: routes.ts + a new core module + server.ts + polaris-narrative.ts + polaris.ts + package.json; no boundary crossed; no governed artifact edited; the two specifications and the registry entry are act-bound and untouched
- G4 Design: a links map projected from the route array so it cannot drift; a contentKey over the canonical body minus a declared 25-path exclusion set, with the excludes quoted into the payload; a schema emitted from the types stating which enum members are populated without pruning the closed six; conditional GET keyed on that contentKey and nothing else; a sibling logicalId that is never an anchor identity
- G5 Spec: no delta proposed by any slice. RFC2-26 and RFC1-33 run over 7 slice rows (denominator 7): slice 4b maps to PWB-REQ-006 and a scenario squarely on its subject; slices 2 and 4a map to POC-REQ-004 and its scenario at a narrower scope than the slice; slices 3 and 5 name PWB-REQ-014 with no scenario for their case; slice 1 enumerates no consequence of either contract; slice 6 is carried and not run. S6-M4 populate-or-prune is a spec amendment (PWB-REQ-014 closes the six classes) and is listed, never scheduled
- G6 Bar: two methods per load-bearing zero; the central claim proved by a landed counterexample rather than a reading; rule-6 mutants per slice; 65 tests run green at this baseline; a false-absence trap in the digest sweep found and reported; NO independent review yet - this is a first draft
Acts: slices 1 and 4a ride the improvement-cycles direction's second limb ("Improvement-cycle work must trace to POC-REQ-001..061 or to a recorded review finding", lines 55-56) on Q4's recommended reading; slice 2 rides POC-REQ-004 on Q1's recommended arm and needs CC-REV-2 plus an act on its second; slice 3 needs a ruling on its credential class (Q3, SEC-1); slice 4b needs an act because the 2026-09-05 continuation stops at "a change to the constraints or envelope the 2026-09-05 registry entry declares" (lines 154-155); slice 5 needs Q5
Open questions: Q1-Q6 above, NOT yet registered - the register row lands after review 1 and the next free number is P-77 (P-68..P-76 are held by the nine siblings, each only on its own branch)
Collisions: 0 under the branch-diff predicate (every sibling branch is planning-only); under the Gate-3 proposed-files predicate, routes.ts is claimed by 6 of 9 siblings, model.ts by 5, polaris.ts by 5, project-shape-model.ts by 3. No file in this pursuit is uncontended
Sign-off: pending - the owner's
Recommended handoff: land slice 1 now (no gate, no schema, a few hundred bytes); rule Q1 and build slice 2; then slice 4a on slice 2's key; rule Q3 before slice 3; hold slice 4b behind Q2 and slice 5 behind Q5 and behind M9
```

## Recommended handoff

**If Q4 is answered as recommended:** file no new bead. Build slice 1 first
under `syzygy-dov.10` — it needs no gate, no schema decision and no new
concept, it costs a few hundred bytes against 2.8 MB of machine headroom, and
it closes the discoverability half of S6-F2 on its own. It is also the only
slice whose oracle is trivial to write correctly.

**If Q1 is answered as recommended:** slice 2 is the change the rest of M10
rests on and should be built second. Its value is not the field; it is that
the payload will then contain a true sentence about its own identity, where
today it contains none and the two available candidates are both false in
opposite directions. Build slice 4a immediately after, on that key and on no
other — and if the owner takes Q1's second arm instead, hold 2 and 4a
together behind the CC-REV-2 delta and land slice 1 alone. Holding 4a while
landing 2 is also coherent; landing 4a without 2 is not, and the bead should
say so.

**If Q1 is answered the third way** — scope the digest to the code-structure
region, which POC-REQ-004 plainly covers — then say so in the bead's close
reason in terms: the resulting key is honest about 27.05% of the body and
useless as a cache validator for the other 72.95%, and slice 4a does not
follow from it. That is a coherent outcome and should be written down as one
rather than quietly becoming a partial ETag.

**If Q3 is answered as recommended:** slice 3 is served
`machine-credentialed` and is a large piece of authoring — 273 field names
across the two endpoints, of which the existing TSDoc documents 5 top-level
fields and nothing else. Budget it as authoring, not extraction. If the owner
takes the `human-open` arm, the bead must record the SEC-1 reading that makes
it lawful, because SEC-1's violation list names a machine client admitted on
loopback location alone and a reader coming to this later deserves to see
which reading was taken.

**If Q2 is answered as recommended:** slice 4b waits for its act, and the
bead records what is at stake — that under the post-compression reading the
2 MB human ceiling would stop binding at any page size this project can
currently produce, and the 2026-09-13 breach would have been served. If the
owner takes the second arm instead (compress, keep measuring the string), the
bead must record that the served `Content-Length` and the checked ceiling are
then deliberately different numbers, so the next person to read
`boundedResponse` does not treat the divergence as a bug.

**If Q5 is answered as recommended:** slice 5 sequences behind M9's packet and
adds its field to whatever M9's slice 6 builds. If the owner prefers one
packet to own identity, fold it into M9 and drop it here — that is Q5's second
arm and it is the cleaner outcome; this packet recommends against it only
because the two keys are on different axes and M9's packet is already at its
gate with eight slices.

**If Q6 is answered the other way** — that a machine-only field must either
have a human counterpart or be added to the parity sweep as its own family
with a declared empty human denominator — then slices 1, 2 and 3 each grow one
sweep family, which is more work and is the honest version. It does not stop
any of them; it changes what "done" means, and the beads should be written
against that definition from the start rather than have it added at review.
