# Feature request M8 — Portability: the profile as a loaded, digest-bound registry input

> **Candidate — binds nothing.** Bead `syzygy-dov.8`, move M8 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`),
> written in the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and
> its six siblings. Planning only: nothing here authorizes implementation.
> Each of Q1–Q7 names the arms the owner may take; naming a lawful arm is
> not a ruling that a slice is authorized. The owner disposes.

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1 and 4) / **medium** (slices 2, 3, 6 and 7) /
**large** (slice 5).

Baseline: Syzygy `a9f671e` (main), in the worktree on branch
`agent/syzygy-dov.8`. The subject is the Three-Surface POC's observation
pipeline and renderer, not the generator package.

**Line-count convention, stated once.** Every `path:line` in this packet is
1-based over that file's bytes at `a9f671e`. Where a sentence wraps, the
cited line is the one the quoted words **begin** on, and a span that
genuinely crosses a line break is written `L–L`. Counts of "lines" are
counts of physical lines, never of sentences.

## The seven questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1 is the packet's central question — it decides
whether any slice with a rendered consequence may be scheduled at all — and
Q2, Q3 and Q5 are narrower gates inside particular slices.

| # | Question | Recommended |
|---|---|---|
| Q1 | **M8's subject — portability — is named by no approved requirement in either adopted specification. Does M8 ride the existing PWB implementation authorization as implementation of requirements already in force, or does a slice with a rendered consequence need a specification amendment naming portability first?** Swept this session with Python `re` over both adopted specification files, denominator the two files in full: the PWB specification carries **37** case-insensitive occurrences of the proving case's name (**29** of them the exact proper noun) over 1,153 lines, the Three-Surface POC specification **2** over 1,009; and the literals *second repositor*, *second project*, *portab*, *generaliz* and *locator* occur **0** times in each, case-insensitively. PWB-REQ-001's own normative sentence opens "WHEN the POC observes Butlers" (line 73). The Three-Surface POC specification's binding reader note fixes the subject: "'The configured project' is the single Butlers repository the 2026-08-29 direction bounds the POC to" (lines 23–24) [all Observed, swept and read at source this session]. | **Ride the existing act for slices 1, 3, 4, 6 and 7; hold slices 2 and 5 until this is ruled.** The five have no rendered consequence that changes what a reader is told about the project (slice 1 is a test, slice 4 is one page of the kit, slice 3 changes only where an already-bound value is read from, slice 6 is a conformance fixture, slice 7's visible change is Trajectory and Orrery going honestly Unknown instead of silently seeded — a VIS-2 repair, not a new claim). Slices 2 and 5 change what the page asserts and what the observation digest covers. **Counter-argument, and it is strong:** "no requirement names portability" is equally an argument that *none of it* may be scheduled from the product goal alone, and Q1's recommended split is a judgment about which consequences are *new* rather than a rule the specification states [Inferred]. **Second lawful arm:** hold every slice and route a portability requirement through CC-REV-2 first — slower, and it front-loads a specification amendment before any measurement exists to write it against. **Third lawful arm:** rule that the amended PWB requirement set already covers derivation-from-the-model, in which case slice 2 proceeds with slices 1, 3, 4, 6 and 7. **Default if unanswered: slices 1, 4 and 6's design work proceed to review; nothing lands.** |
| Q2 | **Slice 5 loads the observation grammar from the adapter-registry entry, which today does not carry the source grammar the code holds. Does the owner perform a third registry-entry amendment act adding those fields?** The entry at `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` is digest-bound by `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, whose Effect closes: "An edit to the artifact breaks this act's digest binding; changes travel as a new act" (lines 76–77). Its current bytes hash to the digest that act names [Observed, `sha256sum` this session compared against the record; neither value is reproduced here, per CG-15 — the record is cited by path]. Its `observationGrammar` carries six keys — `factFamilies`, `fixedCatalogKeys`, `fixedClassKeys`, `fixedProjectAccountKeys`, `precedence`, `rootSummary` — and **no** per-source extraction bindings, heading literals, root index path or tree-population rules [Observed, keys enumerated from the JSON this session]. | **Yes: one amendment act adding the missing source-grammar fields, performed before slice 5's final limb.** Slice 5's first four limbs thread a profile parameter with the current constants as the default and need no act; only the last limb — deleting the constants and loading from the entry — needs it. **Counter-argument:** enlarging what the digest binds makes every future grammar repair an owner ceremony rather than a code change, which is a real recurring cost the owner pays forever, and the proving case's grammar is still moving (three of its four known data quirks were only ruled 2026-09-07). **Second lawful arm:** keep the profile as a separate, unbound implementation-plane JSON file validated against a schema, and leave the registry entry as the checksum it is — cheaper, and it forfeits exactly the property M8 exists to buy, that a governance act rather than a rebuild changes the project. **Default if unanswered: slice 5's first four limbs are designed and none lands.** |
| Q3 | **Slice 6 runs the pipeline against the Syzygy repository itself. Which acts must exist first, and does the owner want them?** **None exists today** [Observed, swept this session]: the only observation consent is `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`, whose Subject line reads `(project:syzygy, repository:butlers-configured-poc)` (line 15); the only adapter-registry entry names `observedRepository` as `repository:butlers-configured-poc`; and `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 73 excludes, verbatim, "No second repository, no wider content class, no reading of Butlers content the secret-classification policy excludes or cannot classify." The continuation direction restates the same exclusion in the owner's own question, quoted verbatim in the record at lines 69–71: "with every original exclusion retained: no release, deployment, Butlers write, second repository, wider content class, egress, observed-code execution, mission or multi-user authority". RFC1-3 settles that the governance root is not exempt: "Every observed repository — **governance root or not** — requires a recorded **Consent record** (SEC-4). No consent means no observation, and therefore **Unknown**" (`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md` lines 130–133) [Observed, quoted at the clause]. | **Perform three acts scoped to a test-only self-observation: a consent record for the pair (`project:syzygy`, `repository:syzygy`) over a `declared-project-shape-text` content class, a second adapter-registry entry naming that pair, and an extension of the existing secret-classification policy to the observing project's own tree — then slice 6 proceeds.** This packet designs slice 6 and **does not run it**; without those acts it stays a design. **Counter-argument:** three ceremonies to obtain a *negative* result (the expectation is that most stages go honestly Unknown) is an expensive way to learn something the code comments already assert, and the owner may prefer to spend the ceremony on a real second project instead. **Second lawful arm:** rule that a conformance fixture reading Syzygy's own tracked tree at a fixed revision — bytes the daemon already reads for governance inputs, through `apps/three-surface-poc/src/governance-inputs.ts` — is not an "observed repository" within RFC1-3, because the fixture emits no rendered claim and serves no surface. This packet does **not** call that arm lawful or unlawful; RFC1-3's sentence is unqualified and the implementation act's exclusion is unqualified, and reading either narrowly is the owner's [Inferred]. **Default if unanswered: slice 6 is designed, its profile is written, and it is not run.** |
| Q4 | **The consent record already carries the approved locator. Should slice 3 read it as configuration after the authority evaluation admits it, or make it a validated consent field inside that evaluation?** `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` line 17 opens "Current locator:" and gives the path, followed on lines 17–18 by the parenthetical "(configuration, not repository identity)" — a two-line sentence [Observed, read at source]. PWB-REQ-005 fixes the size of the authority evaluation's failure population: "The closed invalid-case population SHALL contain exactly 195 independently decided cases" (line 231), and its table's consent row admits exactly three fields — "For observing project, configured repository and observation content class: missing, malformed and wrong but present. \| 9" (line 245), totalled "Every case above, no 'other invalid' bucket. \| **195**" (line 248). | **Read it as configuration after admission. The 195 stays closed and no specification amendment is needed.** The record's own parenthetical says the locator is configuration; RFC1-2 says the same in general terms — "Repository identity is a declared identity in the project declaration, never a remote URL or path — URLs and default branches change; identity must not" (`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md` lines 27–28). The bytes are already digest-verified before the parse runs, so the locator is transitively bound without being an RFC3-16(b) field. **Counter-argument:** a malformed locator line then fails at Git resolution with a resolution error rather than inside the authority evaluation with a typed refusal, which is a worse failure surface for the one input that decides *which repository is read at all* — and that is the input a security reviewer would most want inside the closed population. **Second lawful arm:** add three consent-specific cases (locator missing, malformed, wrong but present), making the population 198. That contradicts line 231's exact number over bytes an act bound, so it is a CC-REV-2 amendment and a new owner act, not an implementation choice. **Default if unanswered: the recommended arm**, because it needs no amendment and the refusal semantics are unchanged. |
| Q5 | **Slice 2 derives the page's project name from the model. Does the `h1` also change claim role from non-normative framing to an anchored project fact — and is that an implementation of PWB-REQ-014 or an amendment to it?** Today the rendered element is `<h1 data-copy-role="project-fact" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>` [Observed, verbatim from the retained capture]. The default is set in source: `DEFAULT_CLAIM_ROLE` maps `project-fact` to `non-normative-framing` (`apps/three-surface-poc/src/polaris-copy.ts` lines 260–265), with the comment "everything else is non-normative framing unless a renderer marks the unit as an anchored project fact" (lines 257–259). PWB-REQ-014 closes the role set at three: "exactly one claim role: anchored project fact, explicitly non-normative framing, or epistemically labeled claim" (lines 764–765), and every anchored claim block "SHALL have a typed, revision-bound anchor set that covers all its claims, contains no unused anchors" (lines 766–767). | **Derive the name; leave the claim role as non-normative framing in slice 2, and file the anchored-fact promotion separately.** A derived name has no anchor to carry: the project identity comes from the consent record and the registry entry, which are Syzygy governance artifacts, and REQ-014 closes anchor targets at "doctrine, contract, requirement, decision, evidence and work" (line 774) — a consent record is a decision, so the anchor exists, but minting it is a second change with its own oracle. **Counter-argument:** shipping a *derived* name that still renders as non-normative framing means the page's most prominent element is a fact the model produced and the page disclaims, which is a new kind of dishonesty rather than the old one, and the owner may prefer one change that does both. **Second lawful arm:** promote it in slice 2, with the decision anchor and the covering/minimality oracle REQ-014 requires. **Default if unanswered: the name is not derived and nothing changes.** |
| Q6 | **The lede. `shell.lede` carries the observed project's own tagline as a `scope-instruction` with no anchor. Delete it, or make it profile-supplied owner framing with an explicit disclosure?** The row is `apps/three-surface-poc/src/polaris-copy.ts` line 27 and it renders on the page immediately beneath the `h1`, with `data-copy-role="scope-instruction" data-claim-role="non-normative-framing"` [Observed, source and capture]. It is the one identity leak no proper-noun predicate can catch: the census below finds **4** of the copy table's **191** rows carrying a Butlers-domain proper noun and this row is **not** one of them, because it contains none [Observed, computed this session]. | **Delete it. Render nothing in that slot until a profile supplies an owner-declared framing line with its disclosure.** VIS-2's polarity applies: an absent framing line is honest, a borrowed one is a confident statement about a project the model never observed. **Counter-argument:** it is the page's only warm sentence, PWB-REQ-012 explicitly budgets for it ("At most one entry `scope-instruction` may state the POC bound", line 688), and deleting it costs comprehension — VIS-1's rank 2 — to buy portability, which VIS-1 does not rank at all. **Second lawful arm:** keep it, sourced from the profile, rendered with a disclosure naming it owner-supplied framing rather than observation. **Default if unanswered: it stays exactly as it is, unanchored**, and this packet records that as the outcome. |
| Q7 | **Slice 7 rewrites the shared `PocModel` type. Does that trigger the improvement-cycle ceremony the owner's direction sets — work-in-progress one, review → repair → confirm → owner report before the next cycle?** `packages/three-surface-poc-core/src/model.ts` line 113 types the project name as the **literal type** `'Butlers'`, not as `string`, and line 118 types `capabilityId` as the literal `'capability:whatsapp-transport-identity'` [Observed, read at source]. Six top-level test files and four non-test modules name `buildButlersPocModel` [Observed, enumerated this session]. All three surfaces read one instance of that model. | **Yes — treat slice 7 as one shared-model change under that direction, with WIP one, and schedule nothing else against the model while it is open.** The literal type means a second project cannot be *typed*, let alone rendered, so the change is not local to a seed constant. **Counter-argument:** the ceremony's cost is a full review-and-confirm cycle for what is, in its first limb, a pure extraction with a byte-identical `GET /api/poc` as its oracle — and that limb could land as ordinary engineering. **This is a process question the owner set the rule for, so it is put rather than decided** [Inferred — a judgment about who owns the rule, not about lawfulness]. **Second lawful arm:** rule the first limb ordinary engineering and apply the ceremony only from the second limb, where the seeds become a parameter and the empty case renders. **Default if unanswered: slice 7 does not start**, because starting it without the ceiling would consume the shared-model WIP slot the other packets also need. |

### Decided in this packet, not put to the owner

**Sequencing is a delegate decision, and it is that M8 lands last.** The
file-set intersection computed below is not zero for any sibling but M6's
documentation pair: M8's 31-file candidate surface intersects M4's cited
surface at **9** files, M2's at **7**, M3's at **6**, M5's at **5**, M1's at
**1** and M6's at **2**. No sibling *branch* touches an implementation-plane
file today — every one of the six is a documentation branch — so the
collision is between *proposed* surfaces, not landed diffs, and it resolves
by ordering rather than by negotiation. M8 is the packet that rewrites the
files the others read, so it goes after them.

**The portability predicate ships reporting-only first.** Slice 1 lands as a
test that prints its count and its file list and fails on nothing. Flipping
it to failing is gated on slices 2 and 7 landing, not on an owner ruling:
the count *is* the debt, and a predicate that fails on day one against 74
files is a predicate someone disables. That is a cost judgment a delegate
makes.

**Slice 4 is one page, not an implementation.** Converging the observer's
profile schema with the generator's admitted-input profile is a
coordination artifact circulated before either schema hardens. It proposes
no part of the LLM pipeline and writes no code.

**The dossier's prerequisite line survives, with two corrections.** The
dossier records M8's prerequisite as "none for predicate, identity, locator,
self-profile; owner act for registry-loaded profile". Two of those four are
wrong in this packet's reading. (a) **Self-profile is not prerequisite-none**:
it observes a repository for which no consent, registry or policy act exists,
and both the implementation act and RFC1-3 are quoted above — that is Q3.
(b) **Identity is not unambiguously prerequisite-none**: the `h1` is a
rendered consequence and no approved requirement names project-identity
derivation, which is Q1 and Q5. The predicate and the locator survive
unqualified: the predicate renders nothing, and the locator reads a field
an act already bound without editing it.

**The dossier's 74-of-133 figure is exact, and its corroboration method is
one file short.** Re-derived below. The note attached to L1-F11 says the two
methods "agreed on the non-test half" — which is true, 37 and 37 — but a
whole-population `ugrep -il` gives **73**, not 74, and the divergence is a
literal NUL byte in one test file that makes ugrep classify it as binary.
Recorded here because the next sweep over these trees will hit it again.

**S1-through-S6 numbering follows the dossier's own slice list; slice 7 is
added.** The dossier's M8 entry merges seven agent moves and lists six
slices. L1-M7 — separating the seeded entities from observed shape — appears
in the "What" bullet and in the merges array and in no slice
[Observed, read at source this session]. It is carried below as slice 7 with
its mapping done, so the gap is recorded rather than dropped.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `.syzygy/governance/doctrine/security.md` | VIS-1, VIS-2, VIS-4, VIS-5, VIS-7; SEC-1 (quoted in Gate 2, with what it does and does not reach), SEC-5 |
| Decisions | `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, `.syzygy/governance/decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`, `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`, `.syzygy/governance/decisions/POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` | the first two are the implementation grant and its continuation, quoted per slice in Gate 3; the last governs slice 4's plane only |
| Specification | `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` (1,153 lines, 17 requirements) and `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` (1,009 lines, 24 requirements) | both adopted; neither names portability, a second project or a locator — the Q1 sweep |
| Governed inputs | `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`, `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` | both digest-bound; slice 3 reads one, slice 5 proposes amending the other through a new act |
| Contracts | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`, `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` | RFC1-2 and RFC1-3 on repository identity and consent; RFC1-10 on opaque identifiers; RFC2-26's phase rule, run in Gate 5 |
| Policies | `.syzygy/governance/policies/craft-and-care/` and the two in-force craft policies under `.syzygy/governance/contracts/candidates/policy-candidates/` | CC-REV-2 is the amendment path Q1's second arm and Q4's second arm would need |

**No amendment overlay applies to either specification.** AGENTS.md names one
overlay composition in this estate — the Polaris *generation* requirement
lookup, which composes `openspec/changes/polaris-manifesto-generation/` with
the `polaris-manifesto-understanding-amendment/` overlay. That pairing
governs slice 4's plane and no other slice. The PWB and Three-Surface POC
specifications are amended **in place** by owner act rather than by overlay.
`.syzygy/governance/decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md` line 89
carries the PWB specification file as a signed row, and its current bytes
hash to the digest that row names; the Three-Surface POC specification's
current bytes are cited by
`.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`
[Observed, both compared by `sha256sum` this session; neither value is
reproduced here, per CG-15 — the records are cited by path]. Five `spec.md`
files exist under `openspec/changes/`, one per change directory, and the PWB
and Three-Surface POC changes have exactly one each [Observed, enumerated
this session]. So every line citation below is to the single effective file,
there is no predecessor-versus-overlay reading to do per slice, and **both
specification files are act-bound bytes that no slice proposes to edit**.

**Two bound-byte constraints this packet obeys.** (a) The adapter-registry
entry and the consent record are the only two governed artifacts any slice
touches, and **only slice 5 proposes editing one** — through a new owner act,
which is the mechanism its predecessor act's own closing sentence names.
Slice 3 *reads* the consent record and edits nothing. (b) Both specification
files still open with a candidate banner over bytes an act bound; per
AGENTS.md the act record governs and the banner is evidence of what a drafter
believed. Neither may be corrected and no slice proposes to.

## Gate 1 — Motif

**The governed artifacts already hold the per-project grammar as data, and
the code keeps hard-coded copies whose tests prove them byte-equal — so
amending the registry entry changes nothing at runtime.** The design intent
is stated in the source itself:
`packages/three-surface-poc-core/src/project-shape-observation.ts` line 21
reads "The constants below are hard-coded copies of the act-bound registry",
and `packages/three-surface-poc-core/src/project-shape-manifest.ts` line 38
reads "Byte-equal to the adopted registry entry's `discoveryVersion` and the".
The oracle comment in `apps/three-surface-poc/src/polaris-project-shape.test.ts`
line 311 is blunter still: "Oracles below are hand-typed from the registry
entry's observationGrammar." [All three Observed, read at source this
session.]

**The consequence, in five measurements taken this session.** (1) Exactly
**two** non-test modules name the registry entry's path, and both read it as
an authority *artifact* — bytes in, digest verified — never as a grammar
source. (2) The rendered project identity is literal copy: **4** of the copy
table's **191** rows carry a Butlers-domain proper noun, and the page's `h1`
is one of them. (3) The approved repository locator is one absolute
filesystem path compiled into `apps/three-surface-poc/src/git-observation.ts`
at line 6, while the consent record that an owner act digest-binds already
carries that same locator at its line 17. (4) The shared `PocModel` types the
project name as the **literal type** `'Butlers'`
(`packages/three-surface-poc-core/src/model.ts` line 113), so a second
project cannot be typed, and the seeded entities that Trajectory and Orrery
render name the proving case's own source files. (5) **74** of the **133**
top-level TypeScript modules under the two POC source trees name the proving
case, and no check, lint or conformance predicate fails when the 75th does.

**What "change the project" costs today.** Editing five core modules, the
renderer, the copy table and one app constant, then re-authoring the
conformance expectations that assert the old values — while the governance
artifacts that already declare all of it change nothing. That is the exact
shape the kit forbids. `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`
states the bar in a sentence that **wraps across lines 94 and 95** — it opens
on 94 at "it must not require" and ends on 95 at "second project render." —
and reads in full: "it must not require manually editing application code to
make the second project render" [Observed, read at source; the span is given
as a range because a citation naming only one of the two lines is a false
citation].

**Why this is weak rather than broken.** Pointed at another repository the
stack mostly fails closed and honestly — a missing root index takes every
pillar to Unknown, which is VIS-2 working. Two paths do not: the tree-only
population rules run whether or not the root index read, and the seeded
`PocModel` entities feed two surfaces with no digest to catch the mismatch.
Both are the silent-wrong class VIS-1 ranks worst.

**Success criteria, per slice.** Slice 1: the portability debt is a number a
check prints, and it only goes down. Slice 2: the page names the project the
model observed, or names none. Slice 3: binding a consented repository is a
governance act, not a rebuild. Slice 4: one profile schema exists before two
do. Slice 5: an amended registry entry changes what the observer reads.
Slice 6: the pipeline's behaviour against a second real corpus is measured
rather than argued. Slice 7: repointing the daemon cannot leave two surfaces
narrating the wrong project's work. **None of these makes anything green;
three of them make things that are silently confident today go honestly
Unknown.**

**What M8 is not.** It is not a second-repository read, not a provider
integration, not a change to the consented content class, and not a claim
that any second project has been observed. Slice 6 is designed and, absent
Q3's acts, not run.

## Measurements at `a9f671e`

Every figure below was taken this session in the worktree at `a9f671e`.
Method, predicate, denominator and raw output for each are in the evidence
record beside this packet.

### The 74-of-133 figure, re-derived with its predicate

**Predicate, stated in full.** Population: files whose name ends `.ts` and
which are **regular files at the top level** of exactly two directories,
`apps/three-surface-poc/src` and `packages/three-surface-poc-core/src` —
subdirectories excluded, no other tree. Match: a case-insensitive Python
`re.search` for the literal *butler* over the file's UTF-8 decoding, anywhere
in the file, comments included. Denominator: **133** (80 in the app tree, 53
in the core tree).

**Result: 74 match, 59 do not** — 37 of the 74 are `*.test.ts` and 37 are
not, against denominators of 64 test and 69 non-test files [Observed,
computed this session]. The dossier's L1-F11 figure reproduces exactly.

**Second method, and it disagrees by one — this is the interesting part.**
`grep -il butler` over the same 133 paths returns **73**. The missing file is
`packages/three-surface-poc-core/src/project-shape-coverage.test.ts`, which
contains a literal NUL byte at byte offset 13,811 — inside a template-string
separator on line 305, `` `${i.class}\0${i.key}` `` written as a raw control
character. ugrep classifies the file as binary, and `-l` silently omits it;
`grep -ail` lists it and `grep -aic` counts 44 matches in it [Observed, all
four invocations run this session]. Verification rule 1's class, in a new
costume: the tool did not error, it returned a smaller true answer. **Any
future sweep over these trees must pass `-a` or use Python.**

**The remainder, enumerated by two mechanical partitions.** The 59
non-matching files are **27** test files and **32** non-test, and
independently **34** app-tree and **25** core-tree; both partitions are
computed from the filename and the path, so neither is a judgment
[Observed, both computed this session; the full 59-name list is in the
evidence record]. The shape the two partitions show is that the
project-neutral remainder is the generic rendering layer and the pure core:
`apps/three-surface-poc/src/page-shell.ts`,
`apps/three-surface-poc/src/design-tokens.ts`,
`apps/three-surface-poc/src/polaris-markdown.ts`,
`apps/three-surface-poc/src/polaris-narrative.ts`,
`apps/three-surface-poc/src/verbatim-route.ts`,
`packages/three-surface-poc-core/src/git-tree.ts`,
`packages/three-surface-poc-core/src/resource-ledger.ts`,
`packages/three-surface-poc-core/src/walkthrough-readiness.ts`,
`packages/three-surface-poc-core/src/code-structure.ts` and
`packages/three-surface-poc-core/src/markdown-code-context.ts` are all in it.
**This packet offers no further classification of the 59**, because any
finer partition would be a reading rather than a measurement, and a reading
presented as a count is the defect this section exists to avoid.

**A recursive sweep changes the denominator and not the answer.** Walking
both trees recursively gives **139** `.ts` files and the same **74** matches.
The six additional files are all under
`apps/three-surface-poc/src/polaris-generation/` — `draft-preview.ts`,
`pipeline-demo.ts`, `pipeline-demo-main.ts` and three tests — and none of
them names the proving case [Observed, all three figures computed this
session, the six enumerated]. The top-level denominator is reported because
it is the one the predicate can state without ambiguity, and because the
recursive one folds in a package with its own separate act.

### What names the proving case in code a reader runs

A narrower predicate than the file-level one, because the file-level count
includes comments and fixture prose. Population: the **69** non-test
top-level modules. Method: block comments blanked to preserve line numbers,
trailing `//` comments stripped, then `re.search(r'\bButlers?\b')` over what
remains.

**Result: 18 modules, 51 lines** [Observed, computed this session]. The
concentration is where the dossier said it would be:
`apps/three-surface-poc/src/polaris.ts` carries 14 of the 51,
`packages/three-surface-poc-core/src/model.ts` 6,
`packages/three-surface-poc-core/src/project-shape-extraction.ts` 5,
`apps/three-surface-poc/src/polaris-copy.ts` 4 and
`packages/three-surface-poc-core/src/worker-change-observation.ts` 3; the
remaining 13 spread one or two each over
`apps/three-surface-poc/src/routes.ts`,
`apps/three-surface-poc/src/orrery.ts`,
`apps/three-surface-poc/src/trajectory.ts`,
`apps/three-surface-poc/src/main.ts`,
`apps/three-surface-poc/src/polaris-source.ts`,
`apps/three-surface-poc/src/walkthrough-preflight.ts`,
`apps/three-surface-poc/src/materialize-action.ts`,
`apps/three-surface-poc/src/polaris-reading-plan.ts`,
`apps/three-surface-poc/src/pwb-mutation-sweep.ts`,
`apps/three-surface-poc/src/fresh-checkout-demo-main.ts`,
`apps/three-surface-poc/src/capture-test-artifact-main.ts`,
`apps/three-surface-poc/src/test-project-shape-fixture.ts` and
`apps/three-surface-poc/src/test-walkthrough-judgment-fixture.ts`.

### The copy-table proper-noun census

**Predicate.** Population: every object literal in the `POLARIS_COPY` array
of `apps/three-surface-poc/src/polaris-copy.ts` matching the row shape
`{ id, role, kind, text }`, with `text` in either quote style. Denominator
**191**, confirmed against a raw count of the literal `{ id: '` in the file,
which is also 191 [Observed, both this session]. The first attempt parsed
**189** because two rows use double quotes for an apostrophe
(`capability.scope` and `evidence.relationships`); the corrected regex
recovers both, and neither carries a proper noun. Match: a proper-noun set
drawn from the observed project's own vocabulary.

**Result: 4 of 191 rows carry a Butlers-domain proper noun** — line 26
(`shell.heading`, role `project-fact`, text is the bare project name), line
60 (`group.overview`), line 62 (`group.architecture`) and line 235
(`source.not-authority`, the notice naming the owning artifact's home)
[Observed]. Role distribution over the 191: 83 `epistemic-disclosure`, 77
`project-fact`, 19 `scope-instruction`, 12 `action-label` — a partition, 83 +
77 + 19 + 12 = 191 [Observed, counted this session].

**And the census misses the leak that matters most.** `shell.lede` at line
27 carries the observed project's own tagline and contains **no** proper
noun, so no proper-noun predicate reaches it, and its claim role is
`non-normative-framing` with no anchor — so no anchoring rule, parity sweep
or claim tuple reaches it either [Observed; the row is read at source and
the rendered element is read from the retained capture]. That is Q6, and it
is also the honest bound on slice 1: **a proper-noun predicate measures the
portability debt it can see, never the whole of it.**

### The rendered page, from the retained capture

The retained capture `polaris-7478.html` was served by the owner's loopback
daemon at Butlers `66ed58f` / observer `a121591`, as-of 2026-09-10 — an
earlier tree than this packet's baseline. It is cited for **what the
renderer emits**, and every source row it is cited against was re-read at
`a9f671e` and is unchanged [Observed].

- The exact proper noun occurs **96** times in the capture [Observed,
  Python `re` over the file this session; the dossier's figure reproduces].
- The page's first heading is, verbatim:
  `<h1 data-copy-role="project-fact" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>Butlers</h1>`
  and the element immediately following it is the lede paragraph carrying
  the tagline with `data-copy-role="scope-instruction"` and the same
  `non-normative-framing` claim role [Observed, read from the capture].

### The registry entry, and why slice 5 needs an act

The entry at
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
is 14,604 bytes and carries exactly **one** entry. Its current bytes hash to
the digest named by
`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
(2026-09-05), which supersedes
`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`
(2026-09-02) for the `adopt-registry-entry` role only [Observed, `sha256sum`
this session compared against the record; the digest is not reproduced here,
per CG-15]. It is a row of two transaction manifests and of
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` [Observed, swept
this session over every `*-MANIFEST.txt` and every
`docs/evidence/*manifest*.json` in the repository, denominator 22 files].

**So any edit to it is a new owner act, by the act's own words.** The
amendment act's Effect closes: "An edit to the artifact breaks this act's
digest binding; changes travel as a new act" (lines 76–77), and its "What
this act does not authorize" section adds "It grants no write, egress,
execution, deployment, release, recovery, mission, second-repository,
autonomous or multi-user authority, widens no consent, edits no signed
artifact" (lines 88–90) [both Observed, quoted at the clause].

**What the entry does and does not already carry.** Its `observationGrammar`
has six keys: `factFamilies`, `fixedCatalogKeys` (the nine catalog keys),
`fixedClassKeys`, `fixedProjectAccountKeys`, `precedence` (the closed
seven-row table with its `cellSyntax` and `factFamilyRows`) and
`rootSummary` (heading, leading label, cardinal form, emitted facts). It
carries **no** root index path, **no** per-basename extraction bindings,
**no** heading literals for the vision, V1 or catalog sources and **no**
tree-population rules — every one of which exists as a TypeScript constant
[Observed, keys enumerated from the JSON and the constants read at source
this session]. That gap is exactly what Q2 asks the owner to close.

**And the locator it does not carry.** The entry's `inputClasses` names
`repository-locator-mapping` with `identityScheme`
`opaque-repository-id-plus-normalized-approved-locator`, and its `subject`
names `observedRepository` as `repository:butlers-configured-poc` — but the
entry gives no locator value. The value lives in the consent record, at line
17, with the parenthetical "(configuration, not repository identity)"
running onto line 18 [Observed, both read at source this session]. **That is
why slice 3 needs no act and slice 5 does**: slice 3 reads a field an act
already bound, slice 5 adds fields to the artifact an act binds.

### Where the registry entry is actually read

**Two** non-test modules name the entry's path —
`apps/three-surface-poc/src/governance-inputs.ts` and
`apps/three-surface-poc/src/walkthrough-inputs.ts` — against **three** test
files [Observed, swept over both source trees this session]. The loader
reads it as an `ArtifactInput` of raw bytes for digest comparison and parses
no field of it: `loadBodyReadAuthorityInputs` resolves the artifact, the act
record, the lifecycle and the recording tag and returns them
(`apps/three-surface-poc/src/governance-inputs.ts`, the `load` closure at
lines 314–331) [Observed, read at source]. The consent record travels the
same path, so **slice 3's locator parse runs over bytes that the authority
evaluation has already digest-verified** — the locator becomes transitively
act-bound without becoming an RFC3-16(b) field, which is Q4's recommended
arm.

### The shared model's literal types

`packages/three-surface-poc-core/src/model.ts` line 113 declares
`readonly name: 'Butlers';` — a **literal type**, not `string` — inside
`PocModel`'s `project` field, and line 118 declares
`readonly capabilityId: 'capability:whatsapp-transport-identity';` the same
way. The builder is `buildButlersPocModel` (line 369) and it sets the value
at line 694 [all Observed, read at source]. **Four** non-test modules and
**six** top-level test files name that builder [Observed, enumerated this
session]. The dossier's L1-F10 cites the value-level seeds; the literal type
is the stronger fact and is not in the dossier: a second project cannot be
typed at all, so slice 7 is a type change before it is a data change.

### The tests that assert the current identity

Measured because it is slice 2's and slice 7's real cost, and because a
packet that omits it understates. Over the **64** top-level test files:
**1** asserts the heading by regex (`apps/three-surface-poc/src/polaris-first-reading.test.ts`
line 62, `/<h1[^>]*>Butlers<\/h1>/`); **3** assert a remediation sentence
naming the observed repository verbatim (`polaris-first-reading.test.ts`,
`apps/three-surface-poc/src/polaris-project-shape.test.ts`,
`apps/three-surface-poc/src/walkthrough-preflight.test.ts`); **1** asserts
the two section headings (`apps/three-surface-poc/src/polaris-copy.test.ts`
line 267); **1** names the locator constant
(`apps/three-surface-poc/src/git-observation.test.ts`); **6** name the model
builder [all Observed, swept this session].

### A rule-6 record that slice 2 must not silently retire

`docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json` records a
mutation over `apps/three-surface-poc/src/polaris.ts` at commit
`4e8d918da0b7afe9d31199f57925fd9eec419738`, with `old` the fragment
`renderPolarisMarkdown(example.statement as string)`, `new` the fragment
`escapeHtml(example.key)`, `exitCode` 1 and `restored` true. That record
carries **no** sha256 field, so it binds no bytes — it is a mutation run,
valid for the commit it names (verification rule 7), not a digest binding
[Observed, the record's five scalar fields read this session]. The guarded
fragment is still present in the current file, exactly once [Observed]. Slice
2 edits that file. **If a slice's edit moves or rewrites that fragment, the
mutation target must be updated in the same change**, per the AGENTS.md
guardrail; if it does not touch the fragment, the record survives the edit as
evidence for its own commit and nothing more.

### Differences from the dossier, re-verified at `a9f671e`

Every `file:line` in the M8 dossier entry and in the seven L1 moves and six
L1 findings it merges was opened at `a9f671e` this session. **Eight**
differences, all recorded and none silently absorbed. Line citations not
listed here verified exactly.

| # | Dossier | At `a9f671e` |
|---|---|---|
| 1 | L1-M1 cites `packages/three-surface-poc-core/src/project-shape-coverage.ts` line 85 | Line 85 is blank. `CLASS_ROWS` is declared at line **86** and `FACT_FAMILIES` at line **78** |
| 2 | L1-F3 and L1-M3 cite `apps/three-surface-poc/src/polaris.ts` lines 420, 424 and 428 as remediation sentences | All three are off by one or more: 420 is a closing brace, 424 is `case 'active-content':` and 428 is `case 'denied-path':`. The remediation sentences are at **419, 423, 425, 427, 432 and 441**, and the pillar routes at **671, 673, 675, 677, 679, 681 and 683** |
| 3 | L1-M5 cites `apps/three-surface-poc/src/governance-inputs.ts` line 113 | Line 113 declares the `LoadGovernanceInputsOptions` interface. The authority loader's `load` closure is at lines **314–331** |
| 4 | L1-F11's note says the two methods agree | They agree on the non-test half (37 and 37) and disagree on the whole: Python gives **74**, `ugrep -il` gives **73**, over a NUL byte. The headline figure, 74 of 133, is exact |
| 5 | L1-F10 cites the seeded values in `packages/three-surface-poc-core/src/model.ts` | Those verify, and they understate: line **113** types the project name as the literal **type** `'Butlers'`, so a second project cannot be typed at all |
| 6 | The dossier's `prerequisite` reads "none for … self-profile" | The self-profile observes a repository no consent, registry or policy act names, and the implementation act excludes a second repository. That is Q3 |
| 7 | The dossier's L1-M2 tags SEC-1 for the locator | SEC-1 is endpoint authentication. No SEC clause names a repository locator; RFC1-2 and RFC1-3 do. Gate 2 states this |
| 8 | The dossier's M8 entry lists six slices and merges seven moves | L1-M7 appears in the "What" bullet and in `merges` and in no slice. It is carried here as slice 7 |

The dossier's `syzygy_audited_at` value is `f4589e2`. This packet's baseline
is `a9f671e`, and **the eight rows above are the complete set of differences
the re-verification found** over the dossier's M8 entry and the thirteen L1
records it merges [Observed, every citation opened this session; the
denominator is the citation list in those records, enumerated in the
evidence record].

## Gate 2 — Doctrine

**VIS-1 — Comprehensible truth first; never comprehensible fiction.** Quoted
at the clause, `.syzygy/governance/doctrine/vision.md` lines 82–95: "The full
ordering, highest first: (1) truth and observation determinism; (2)
comprehension of the truth's presentation; (3) momentum (delivery speed); (4)
breadth of scope and fidelity of presentation; (5) reproducibility of derived
convenience… Comprehension is achieved by simplifying *presentation*, never
*content*: an honest view may aggregate, defer, or progressively disclose
Unknowns, but may never substitute a confident state for an Unknown one."
Slices 2 and 7 are rank-1 repairs: each removes a place where the surfaces
would substitute a confident statement about the wrong project for an
Unknown. Q6's deletion of the lede spends rank 2 to buy rank 1, which is the
direction VIS-1's ordering permits; the reverse would not be.

**VIS-2 — No evidence means Unknown, not success.** Lines 96–106: "No
surface may declare a project aligned, converged, or genome-complete — nor
turn anything green — without current evidence… *Violation:* … a stale view
silently green." Slice 7's empty case is this rule applied at the seam where
the seeds sit: a profile that supplies no seeds must take Trajectory and
Orrery to an explicitly Unknown, denominator-bearing empty graph, never to a
default. Slice 6 is the same rule applied to the packet's own claims: until
the pipeline has been run against a second corpus, "the pipeline is portable"
is Unknown, and this packet does not assert it.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Lines 141–166. Every slice but 5 writes only into `apps/`,
`packages/` or `docs/` — the implementation plane, reached as "a worker
action against scheduled work", which is the sentence VIS-5 reserves it to.
Slice 5's *governance* limb writes into `.syzygy/**`, which is one of the two
permitted direct-write namespaces — but writing a **digest-bound** artifact
there is gated by the act that bound it, not by VIS-5, which is Q2.

**VIS-7 — The observatory itself must be trustworthy.** Lines 183–193:
"every rendered internal project-entity link resolves to its identified
target… every encoding means what its legend says." Slice 2 is the case where
the *label* stops meaning what its legend says: an element marked
`data-copy-role="project-fact"` naming a project the model never observed is
an encoding that misreports, whatever its claim-role attribute says
alongside.

**SEC-1 — Authenticated by default, quoted because the dossier tags it for
the locator, and it does not reach it.** `.syzygy/governance/doctrine/security.md`
lines 10–23, verbatim at the load-bearing sentences: "Syzygy's endpoints and
UI are reachable without authentication only on the loopback interface, and
client classes are distinguished even there: **browser requests must pass
origin/CSRF protections, including on loopback**…; **non-browser agent and
CLI clients are admitted only through an explicit machine-client
authentication mechanism**; loopback location alone is never proof of client
identity." SEC-1 governs **who may ask**, not **which repository is
answered about**. The dossier's L1-M2 tags SEC-1 for the locator; this packet
reads that tag as wrong and says so rather than inheriting it [Inferred — a
reading of SEC-1's scope, stated rather than resolved; SEC-2 is about egress,
SEC-3 about executing observed code, SEC-4 about writes and SEC-5 about
secrets, and **no SEC clause names a repository locator**, which is itself
the finding].

**What does govern the locator, at its defined clause.** **RFC1-2**:
"Repository identity is a declared identity in the project declaration, never
a remote URL or path — URLs and default branches change; identity must not"
(`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
lines 27–28). The implementation already honours the *identity* half: the
registry's identity scheme is
`opaque-repository-id-plus-normalized-approved-locator` and the subject is an
opaque repository id. What it does not honour is where the *configuration*
half comes from. There is a structural echo of SEC-1's "loopback location
alone is never proof of client identity" in "a filesystem path alone is never
proof of repository identity" — but that is an analogy this packet draws, not
a clause either document states [Inferred].

**RFC1-3 governs slice 6, and it is unqualified.** Same file, lines 130–133:
"Observed-source repositories are read-only to Syzygy unless separately
onboarded. Every observed repository — governance root or not — requires a
recorded **Consent record** (SEC-4). No consent means no observation, and
therefore **Unknown** — never an empty graph read as absence." The phrase
"governance root or not" is the reason Q3 exists rather than being decided
here.

**RFC1-10 governs slice 7's rename.** Lines 263–266: "Identifiers are opaque;
names are labels. For every declared class (Capability, Topology entry,
Declared region, Repository, Project, Proposal): renaming the thing changes
its label, never its identifier." Slice 7 must therefore change the *label*
carried in `PocModel.project.name` and leave any minted identifier alone, and
must not re-key existing entities by the new label.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Portability predicate | a new test module beside `apps/three-surface-poc/src/polaris-copy.test.ts`, sweeping both source trees | none |
| 2 Identity from the model | `apps/three-surface-poc/src/polaris-copy.ts`, `apps/three-surface-poc/src/polaris.ts`, `apps/three-surface-poc/src/polaris-source.ts`, `apps/three-surface-poc/src/walkthrough-preflight.ts`, `apps/three-surface-poc/src/routes.ts`, `apps/three-surface-poc/src/orrery.ts`, `apps/three-surface-poc/src/trajectory.ts`, `apps/three-surface-poc/src/polaris-reading-plan.ts` and four test files | none |
| 3 Locator from consent | `apps/three-surface-poc/src/git-observation.ts`, `apps/three-surface-poc/src/governance-inputs.ts`, `packages/three-surface-poc-core/src/body-read-authority.ts` and two test files | **read, never edited**: `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` line 17 |
| 4 One profile schema | `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`, `docs/polaris-generation/README.md` | none |
| 5 Registry-loaded profile | a new `packages/three-surface-poc-core/src/` profile module plus `project-shape-observation.ts`, `project-shape-manifest.ts`, `project-shape-extraction.ts`, `project-shape-coverage.ts`, `project-shape-model.ts` in that tree, and `apps/three-surface-poc/src/governance-inputs.ts` | **edited, under a new act**: `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` — Q2 |
| 6 Self-profile proof | a new conformance module in `packages/three-surface-poc-core/src/`, plus a Syzygy profile fixture | **none edited**; it *reads* this repository's own tracked tree, which is what Q3 gates |
| 7 Seeded entities out of the model | `packages/three-surface-poc-core/src/model.ts`, a new seed module beside it, `apps/three-surface-poc/src/main.ts`, `apps/three-surface-poc/src/walkthrough-inputs.ts`, `apps/three-surface-poc/src/test-model-fixture.ts`, `apps/three-surface-poc/src/trajectory.ts`, `apps/three-surface-poc/src/orrery.ts` and their tests | none |

Boundaries crossed: **one**, deliberately. Slice 5's last limb writes into
`.syzygy/**`, which is a permitted direct-write namespace under VIS-5 but a
digest-bound artifact under the act that bound it — so it travels as an owner
act, never as an implementation change. Every other slice writes only in the
implementation plane.

Not touched by any slice: the body-read authority *evaluation* itself
(`packages/three-surface-poc-core/src/body-read-authority.ts`'s 195-case
population and its RFC3-16 field checks), which slice 3 extends beside rather
than inside; the nine walkthrough answer identities in
`packages/three-surface-poc-core/src/walkthrough-readiness.ts`, which are
already project-neutral; the resource ledger; the secret detectors and the
active-content scan.

### The authorizing act, per slice

The **Named clause** column records, per slice, the requirement clause the
slice's observable consequence is scheduled from — or states that none is
named, which is Q1's subject. Neither specification has an amendment overlay
(Gate 0), so there is no predecessor-versus-overlay reading; the column
instead records whether the clause is one the slice *implements* or one it
*contradicts*.

| Slice | Owner act needed | Named clause | Named act and the trigger test |
|---|---|---|---|
| 1 Predicate | **No** | **None named.** A test that renders nothing enumerates no observable consequence | Rides `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02) as continued 2026-09-05. Its point 3 authorizes "Code in the ordinary implementation plane only — `apps/**`, `packages/**`, tooling, root manifests" (lines 59–61). No escalation trigger crossed: the act's triggers are doctrine or contract change, specification amendment, security/privacy/retention posture, registry envelope, observation outside the consented class or repository, or scope beyond the signed change (lines 88–94); a reporting-only sweep is none of them |
| 2 Identity | **Ruled by Q1; and Q5 if the claim role changes** | **None names project-identity derivation.** PWB-REQ-012 (line 683) governs the copy table's *roles*, word limits and prohibited terms and says nothing about where a string comes from; PWB-REQ-014 (lines 764–765) closes the *claim roles* and is what Q5 engages | Same act on Q1's recommended reading, which holds this slice. The trigger at issue is "any scope beyond the signed change" (line 94): a page that names the project it observed is arguably within PWB-REQ-001's "Every emitted project-shape fact SHALL carry its source identity" (line 78), and arguably a new consequence. This packet does not rule it |
| 3 Locator | **No**, on Q4's recommended arm | **PWB-REQ-005**, line 245's consent-specific field row and line 231's "exactly 195 independently decided cases". The slice is designed **not** to change either | Same act. No trigger crossed *on the recommended arm*: the artifact is read, not edited; the content class is unchanged; the repository is unchanged; the 195 is unchanged. On Q4's second arm the trigger is "an amendment to the signed PWB specification" (lines 89–90), which needs CC-REV-2 and a new act |
| 4 One profile schema | **No** | **None named.** One page of authoring guidance, argued from the kit's own stated bar at `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` lines 94–95 | Rides `.syzygy/governance/decisions/POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-12), whose line 42 authorizes "the full EXECUTION-PHASES.md implementation goal, including protected effect host, complete owner experience, **two-project** and changed-source proof obligations", with the reservation "Real-project reads, provider egress and destination writes remain separately admitted". A coordination page is none of the reserved three |
| 5 Registry profile | **Yes — a third registry-entry amendment act (Q2)**, for its last limb only | **None names a loaded profile.** The clause the slice must not break is PWB-REQ-001's determinism sentence, lines 74–76: the observation "SHALL bind the consent record, secret-policy version, source-discovery version and observer/parser version as deterministic evaluation inputs" — so the loaded profile's digest must join that set | Same PWB act for limbs 1–4. Limb 5 crosses the trigger "a change to the constraints or envelope the registry entry declares" (lines 92–93) explicitly, which is what the 2026-09-05 continuation direction exists to show the shape of: the owner continued authorization *after* the registry amendment, not before it |
| 6 Self-profile proof | **Yes — a consent record, a registry entry and a policy extension for this repository (Q3)** | **PWB-REQ-005** line 206, the prohibition itself, and **RFC1-3** lines 130–133. Both are quoted in Q3 | No existing act covers it. `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 73 excludes "No second repository" and the continuation restates it. **This packet does not rule whether Syzygy observing its own tracked tree is a "second repository"; it states that no act names the pair and that RFC1-3's sentence is unqualified** |
| 7 Seeded entities | **No for the code; Q7 for the ceremony** | **POC-REQ-050** (line 777) requires Orrery's regions to "derive from the directory structure and declared capability-to-path mappings", with the falsifier "a rendered region backed by no observed directory or declared mapping" (lines 791–793). Seeded entities from the wrong project are that falsifier | Same PWB act; the change is implementation-plane only and repairs a requirement rather than extending one. Q7 is about the owner's improvement-cycle ceremony, not about authority |

**What landing slices 2 and 5 retires.**
`docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json` records a
rule-6 mutation over `apps/three-surface-poc/src/polaris.ts` at a named
commit, and slice 2 edits that file. The record binds no digest (it has no
sha256 field), so **no act-bound and no digest-bound byte is retired** — but
the evidence is valid only for the commit it names (verification rule 7), and
the implementing bead must re-run it and record the new commit before the
slice is called done. Slice 5 rewrites five core modules whose conformance
expectations currently assert the constants byte-equal to the registry entry;
those expectations become schema-conformance and profile-fixture assertions,
and each must keep its expected values as hard-coded literals rather than
importing them from the module under test.

All seven slices run under `syzygy-dov.8`, the pursuit bead; no new bead is
filed by this packet, and no register row is added here — the owner questions
are registered after review 1, batched with the siblings'.

## Gate 4 — Design sketch, per slice

### Slice 1 — The portability debt becomes a number a check prints (small; no act)

**What.** One new test module beside
`apps/three-surface-poc/src/polaris-copy.test.ts` that sweeps the two POC
source trees for the active profile's proper nouns and reports the count, the
file list and the denominator. It ships **reporting-only**: it fails on
nothing until slices 2 and 7 land.

**The predicate, and its stated blind spot.** The sweep matches the proper
nouns the profile declares, over the same 133-file top-level population this
packet measured, reading files as bytes with an explicit UTF-8 decode so a
NUL byte cannot silently shrink the denominator. Its failure message states
the denominator, the count and the allowlist — because a bare "1 violation"
is a message someone deletes. **It cannot see the lede**: a tagline carrying
no proper noun passes the sweep while being the most confident wrong
statement on the page, and the test's own docstring must say so, or the next
reader will mistake a passing sweep for portability.

**Files touched.** One new test module; no source file.

**The oracle.** The count and the file list, compared against a hard-coded
expected baseline literal in the test — never imported from the module under
test. The baseline at landing is 74 over 133, with the 74 enumerated.

**Rule-6 mutants.** (a) Add the proper noun to one allowlisted profile
module and confirm the sweep still passes — it should, and recording that
makes the allowlist's scope visible rather than assumed. (b) Add it to one
file *outside* the allowlist, in a distinctive string that cannot be reached
by coincidence (the short-label lesson: a bare project name would be
"reached" by any file that mentions it in a comment), and confirm the sweep
reports 75 with that file named. (c) Insert a NUL byte into a file that does
name the proper noun and confirm the count does **not** drop — the
counterexample for the ugrep class this packet measured. Each mutant's `old`
and `new` fragments and the commit are recorded.

**Maps to.** No approved requirement; enumerates no RFC-0002 consequence.
Filed as ordinary engineering under the implementation act.

### Slice 2 — The page names the project the model observed (medium; Q1, Q5)

**What.** Add `projectDisplayName` to the profile, surface it on the shape
identity, and convert the copy table's four proper-noun rows into templated
slots filled from it — a bare `{project}` for the heading, and the
templated forms of the two group headings and the not-authority notice. Do
the same for the fourteen
renderer-built sentences in `apps/three-surface-poc/src/polaris.ts` and the
one in `apps/three-surface-poc/src/walkthrough-preflight.ts`, and for the
four page eyebrows in `polaris-source.ts`, `routes.ts`, `orrery.ts` and
`trajectory.ts`.

**What it does not do.** It does not promote the heading from
`non-normative-framing` to an anchored project fact — that is Q5's second
arm, and it needs REQ-014's covering-and-minimal anchor set, which is a
second oracle. It does not touch the lede, which is Q6.

**Files touched.** Eight source modules and four test files, enumerated in
Gate 3.

**The oracle.** The copy oracle in
`apps/three-surface-poc/src/polaris-copy.test.ts`, extended with a predicate
that fails when any rendered sentence contains a proper noun absent from the
active profile. Every label it matches must be a distinctive full clause: a
bare project name is reached by coincidence in a page that legitimately
quotes the project's own source text, which is exactly what the source route
does. The independent expected values come from a fixture profile whose
display name is a string that occurs nowhere else in the repository.

**Rule-6 mutants.** (a) Reinsert the literal proper noun into one copy row
and confirm the oracle fails naming that row's id. (b) Change the fixture
profile's display name and confirm the rendered heading follows it — the
positive direction, which a negative-only mutant would not establish. (c)
Leave one of the fourteen remediation sentences untemplated and confirm the
sweep names it; this is the mutant that matters, because the remediation
routes are the easiest to miss and the most damaging to get wrong — they tell
a reader which repository to go and repair.

**Maps to.** PWB-REQ-012 for the role invariant it must not break; **no
approved requirement for the derivation itself** — Q1. Rendered consequence:
yes, the page's first heading.

### Slice 3 — The locator comes from the consent record (medium; no act)

**What.** Delete `PWB_APPROVED_REPOSITORY_LOCATOR` from
`apps/three-surface-poc/src/git-observation.ts` and pass the approved locator
in from `governance-inputs.ts`, parsed out of the consent artifact's already
digest-verified bytes.
`resolvePwbRepositoryBinding` already takes `approvedLocator` as an option
and already normalizes through `realpath` plus a Git common-directory check,
so the refusal semantics do not change — only where the approved value comes
from.

**The parse, and its grammar.** The consent record's line 17 opens with the
literal label *Current locator:* and carries the path in a code span, with a
parenthetical that runs onto line 18. The parse is a literal grammar over
that one line: the exact label, a single complete inline code span, and
nothing else before the parenthetical. **A grammar failure is a refusal, not
a fallback** — the observer refuses with a typed reason and performs zero
reads, which is the fail-closed polarity the rest of the pipeline already
has. This is where the
AGENTS.md extractor lesson applies in reverse: a grammar this narrow will
reject a record whose author reflows the line, so the failure message must
name the expected shape.

**Where the parse runs, and why that is Q4's recommended arm.** It runs
**after** `evaluateBodyReadAuthority` has admitted the triple, over the same
bytes the digest check passed. The locator is therefore transitively bound by
the consent act without becoming one of PWB-REQ-005's 195 cases, and line
231's exact number is untouched. A new refusal reason `locator-unconsented`
covers a repository the consent record does not name; it is distinct from
`locator-mismatched`, which stays for a repository that is named and resolves
elsewhere.

**Files touched.** `git-observation.ts`, `governance-inputs.ts`,
`body-read-authority.ts` (the consent artifact's parsed shape only, not its
validator), and two test files.

**The oracle.** The current binding resolves byte-identically: same
`gitCommonDirectory`, same snapshot identity, same observation digest as
before the change. That equality is the regression oracle and it is exact —
if any of the three moves, the slice is wrong.

**Rule-6 mutants.** (a) Point the run at a repository the consent record does
not name and confirm zero Git calls occur before the refusal, with reason
`locator-unconsented`. (b) Reflow the consent record's line 17 in a scratch
copy and confirm the parse refuses rather than falling back to any default.
(c) Delete the locator line entirely and confirm the same. (d) Leave the
constant in place as a test-only default and confirm no production path
reads it — the guard against the change being cosmetic.

**Maps to.** PWB-REQ-005 as the requirement the slice must not perturb, with
its scenario "Missing observation consent blocks content reads" (lines
296–300, "WHEN no effective Butlers observation-consent act exists / THEN the
project-shape observer performs zero body reads / AND the project model
reports Unknown with the consent reason") as the shape the new refusal must
match. No rendered consequence beyond the refusal reason, which already
renders.

### Slice 4 — One profile schema, before two exist (small; no act)

**What.** One page naming the fields the observer's `ProjectShapeProfile` and
the generator's admitted-input profile share, which stage owns each, and one
digest that names both. Added to
`docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`, whose "Prepare sources"
row already says "admitted snapshot and project adapter" without defining
either, and routed from `docs/polaris-generation/README.md`.

**Why it is worth its own slice.** The generator package is in Phase A and
its own bound scope document states, at
`openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md` lines
5–6, "The full owner-facing generator, two real projects and changed-source
proof remain mandatory completion criteria", while Phase A "does not create
or mutate live scheduler items, call a real provider, serve owner effect
controls, **or read another project**" (lines 13–14) [Observed, quoted at
source]. Two efforts arriving at two profile schemas is the expensive
outcome, and it is cheap to prevent now.

**Files touched.** Two kit files, neither of which is act-bound or
digest-bound [Observed, both swept against the 22-file corpus this session].

**The oracle.** A field-by-field table in the page, checked against the
landed schema when either lands; no executable oracle, because the artifact
is a coordination page and pretending otherwise would be the "ordinary
engineering dressed as a gate" defect in reverse.

**Rule-6 mutants.** None applicable; there is no predicate to mutate. Stating
that is more honest than inventing one.

**Maps to.** No requirement; no RFC-0002 consequence.

### Slice 5 — The profile is a loaded, digest-bound registry input (large; Q2)

**What.** A new `ProjectShapeProfile` value defining the root index path, the
layer and pillar vocabulary with labels, the per-source extraction bindings,
the tree-population rules with a root-independence flag, the precedence row
vocabulary, the catalog keys and the project-account keys. Loaded from the
registry entry's `observationGrammar` (extended per Q2) plus the policy's
source admission, validated against a JSON schema, and threaded as a
parameter through manifest derivation, phase-A seed admission, extraction,
coverage and model construction.

**Five limbs, in order, only the last of which needs the act.**

1. Write the type and its JSON schema; derive the current profile from the
   existing constants and prove it byte-reproduces today's manifest digest
   and observation digest at the captured revision. **The existing digests
   are the regression oracle** — this limb changes no behaviour and must
   prove it.
2. Thread the profile through `project-shape-manifest.ts` and phase-A
   admission, with the constants as the default argument. Still no behaviour
   moves.
3. Thread it through `project-shape-extraction.ts` and
   `project-shape-coverage.ts` — the precedence rows, the class-to-layer
   table, the catalog and project-account key sets.
4. Add the profile digest to the deterministic inputs and to the machine
   surface. PWB-REQ-001 lines 74–76 require the consent record, secret-policy
   version, source-discovery version and observer version to be deterministic
   inputs; a loaded grammar that is not one would let the observation digest
   stay equal across a grammar change, which is the determinism failure the
   requirement exists to prevent.
5. Delete the constants and load from the registry entry. **This limb needs
   the amendment act (Q2) and nothing before it does.**

**Files touched.** A new core module plus the five `project-shape-*` modules
and `governance-inputs.ts`, with their conformance files.

**The oracle.** Two, and they answer different questions. (i) The
manifest and observation digests at the captured revision, unchanged across
limbs 1–3 — an equality oracle over values computed before the change. (ii)
After limb 4, a **change-detection** oracle: mutate one profile field at a
time and confirm the observation digest changes, and that it does not change
when nothing does. The second is the one that proves the profile is really an
input rather than decoration.

**Rule-6 mutants.** One per profile field, per limb 4's oracle: for each
field, a mutant that changes it and a confirmation that the digest moves;
plus a no-op mutant confirming the digest does not move on a formatting
change. Also (a) a schema-invalid profile must refuse the load rather than
fall back to the constants, and (b) a registry entry whose
`observationGrammar` lacks a field the schema requires must refuse, not
default — both fail-closed.

**Maps to.** PWB-REQ-001's determinism sentence, which limb 4 exists to keep
satisfied. **No approved requirement names a loaded profile**, which is Q1.
Rendered consequence: the deterministic-input set the page and the machine
answer both expose grows by one entry, so yes.

### Slice 6 — The pipeline is measured against a second real corpus (medium; Q3)

**What.** Author a Syzygy profile — a root index under this repository's own
governance tree, its own layer vocabulary, its own heading literals — and run
the complete phase-A and phase-B pipeline against Syzygy's own tracked tree
at an exact revision, as a conformance fixture. Record, per stage, whether
the outcome is a crash, an honest Unknown, or a claim. Then render the
resulting shape to HTML in the test and run the existing parity and copy
oracles over it.

**Why it is the cheapest real portability evidence.** The alternative —
observing a second external project — needs a second consent, a second
registry entry and a policy extension for a repository nobody has chosen. The
self-profile needs the same three acts for a repository the owner already
governs, and it exercises the failure the dossier flags as most likely:
Syzygy's doctrine directory holds files with the same basenames the
extraction grammar binds to, carrying a different ontology
(`packages/three-surface-poc-core/src/project-shape-extraction.ts` line 369
reads `if (base === 'vision.md') {`, dispatching on the basename alone, and
`.syzygy/governance/doctrine/` holds `vision.md`, `architecture.md` and
`v1.md` under a wholly different ontology) [Observed, both read at source
this session].

**What this packet does with it: designs it, does not run it.** No consent
record, registry entry or policy names the pair (`project:syzygy`,
`repository:syzygy`); the implementation act excludes a second repository;
RFC1-3's requirement is unqualified for the governance root. Slice 6 is a
design and a request, and Q3 is the request.

**Files touched.** A new conformance module and a profile fixture. No
existing source module changes.

**The oracle, in three stages.** (i) Stage outcomes only — crash, Unknown or
claim — with **no expected values**, so the first run measures rather than
asserts. (ii) Every emitted claim classified: derivable from this
repository's own bytes, or leaked from the proving case's copy path. Each
leak is a bead against slice 2 or slice 7, and the leaks are the proof those
slices are load-bearing. (iii) Render and sweep; the heading and the
remediation routes are the **expected** first failures before slice 2 lands.
Expected values are hard-coded literals in the test, never imported from the
module under test.

**Rule-6 mutants.** Deferred until the slice may run: a mutation plan for a
fixture that has never executed is a plan against imagined output, and
writing one would be the "ordinary engineering dressed as evidence" defect.
The one mutant that can be specified now is (a) point the fixture at a
revision where the Syzygy root index is absent and confirm every pillar goes
Unknown with its reason rather than empty.

**Maps to.** PWB-REQ-005 and RFC1-3 as the gates, not as coverage. No
approved requirement names a self-observation. No rendered consequence — the
render happens inside the test.

### Slice 7 — Seeded entities leave the shared model (medium; Q7 for the ceremony)

**What.** Move `WORKER_CHANGE_SEAM`, `ARTIFACT_PATHS`, `INTENT_MARKERS` and
the seeded entity graph out of `packages/three-surface-poc-core/src/model.ts`
into a profile-supplied seed module; widen the literal type at line 113 from
`'Butlers'` to the profile's display-name type; rename
`buildButlersPocModel` to `buildPocModel` taking the profile. **Where a
profile supplies no seeds, Trajectory and Orrery render an explicitly Unknown
graph with its denominator, never a default.**

**Three limbs.**

1. Extract the seed constants to a seed module; prove `GET /api/poc` is
   byte-identical. Pure refactor, equality oracle.
2. Take the seeds as a parameter; render the empty case on all three
   surfaces and confirm nothing reads green (VIS-2) and every empty region
   carries its denominator (POC-REQ-051).
3. Key the snapshot identity by repository id rather than by the literal
   prefix at `apps/three-surface-poc/src/main.ts` line 102.

**The trap, named because it has been sprung once already.** Do **not** wire
`WORKER_CHANGE_SEAM` test-artifact evidence into the identity-resolution
entities while moving them. That produced a false "Verified" once and was
reverted; it is the single most likely way this slice goes wrong, because the
two constant groups sit adjacent in the file and move together.

**Files touched.** `model.ts`, a new seed module, `main.ts`,
`walkthrough-inputs.ts`, `test-model-fixture.ts`, `trajectory.ts`,
`orrery.ts` and their tests — six test files name the builder.

**The oracle.** Limb 1: `GET /api/poc` byte-identical, compared against a
capture taken before the change. Limb 2: an independent expected table of
which regions and columns appear in the empty case, hand-written from
POC-REQ-050's and POC-REQ-051's text rather than from the projection module.

**Rule-6 mutants.** (a) Supply a profile with no seeds and confirm Orrery
renders an Unknown region with a denominator rather than zero regions — the
VIS-2 case. (b) Supply a profile whose display name differs and confirm no
entity id changes (RFC1-10: renaming changes the label, never the
identifier). (c) Reintroduce one seeded path and confirm the parity sweep
reports it as a region backed by no observed directory — POC-REQ-050's own
falsifier, used as the mutant.

**Maps to.** POC-REQ-050 (line 777, with its falsifier at lines 791–793) and
POC-REQ-051. Rendered consequence: yes — Trajectory and Orrery change what
they show in the empty case, from a confident seeded graph to an Unknown one.

## Gate 5 — Specification

Two adopted specifications are in force, both digest-bound (Gate 0), neither
carrying an amendment overlay. Requirement citations below are to the single
effective file in each case, and every requirement and scenario cited was
read at source this session.

### Does M8 need a specification delta? (Q1)

**The measurement first, because it is the whole argument.** Swept this
session with Python `re` over both specification files in full — denominator
the two files, 1,153 and 1,009 lines — the literals *second repositor*,
*second project*, *portab*, *generaliz* and *locator* occur **0** times in
each, case-insensitively. The word *profile* occurs **once** in the PWB
specification, at line 357, where it means a UTF-8 line-oriented text profile
for code contexts and nothing to do with a project adapter [Observed, the hit
read at source].

**What the specifications say instead.** PWB-REQ-001's normative sentence
begins "WHEN the POC observes Butlers" (line 73). The Three-Surface POC
specification's reader notes, which are marked "binding on how this file is
read" (line 18), fix the subject at lines 23–24: "'The configured project' is
the single Butlers repository the 2026-08-29 direction bounds the POC to."

**So M8's subject is named nowhere and its slices are individually another
matter.** That distinction is the packet's central claim and it is a reading,
not a measurement [Inferred]. A slice that changes *where a value is read
from* without changing any rendered claim (slices 1, 3, 4, 6) implements the
requirements already in force; a slice that changes *what the page asserts*
or *what the observation digest covers* (slices 2, 5) proposes a consequence
no approved requirement names. Slice 7 sits between: its change is to make
two surfaces honest in a case that never occurs while exactly one project is
configured, which is a repair of POC-REQ-050's own falsifier rather than a
new consequence — **but it is a rendered change in that case**, and a strict
reader would put it with 2 and 5. Q1 is where the owner rules it.

**The bytes are bound, so the second arm is expensive and should be priced.**
Both specification files hash to digests named in owner-act records (Gate 0).
A portability requirement is therefore a CC-REV-2 semantic delta, an
independent review in fresh context and a new owner act — not a paragraph
added to a file. That is the honest cost of Q1's second arm, and it is a
reason to prefer it only if the owner wants portability *specified* rather
than *proved first*.

### The RFC2-26 test, run over all seven slice rows

RFC-0002 is an accepted design contract in force. Its phase rule is quoted
verbatim at the defined clause,
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` lines
196–221, under the `###` heading "Authority boundary at the OpenSpec seam
(binding phase rule)" at line 194 — **the whole clause, both paragraphs, with
no elision**:

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

**The denominator is seven**: the seven slice rows of Gate 3's "The
authorizing act, per slice" table [Observed, counted this session over that
table]. The test is run over all seven.

| Slice | RFC2-26 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Predicate | **None enumerated.** A test module renders nothing, answers no query and reaches no surface; no class in the clause's list fits | n/a | n/a. The clause is not engaged |
| 2 Identity | "claim and challenge rendering" (the page's first heading is a claim about which project the reader is looking at); "API answers over epistemic state" (the project name is a field of the machine answer) | **Requirement partial, scenario absent.** **PWB-REQ-012**, line 683, governs the copy table but constrains only role, word count and prohibited terms; its scenario "Section headings name project concepts" (lines 705–710) reads "**WHEN** Polaris renders the project-level entry / **THEN** its headings name concepts such as purpose, boundaries, architecture, V1 scope, capabilities, evidence or gaps / **AND** no heading describes a document movement or reading stage" — which the current literal heading already satisfies and would continue to satisfy if it named the wrong project. **PWB-REQ-001** line 78 requires "Every emitted project-shape fact SHALL carry its source identity, scope, capture instant and observer identity/version", which reaches the *facts* and not the page's own heading. **No scenario in either adopted specification states the case of a rendered project name that the model did not observe.** Denominator: **55** scenarios — 31 in the PWB specification and 24 in the Three-Surface POC specification — each swept over its heading and its WHEN/THEN bullets, bounded at the `yaml` fence, for *project name*, *display name*, *project identity*, *names the project*, *which project* or *heading names*; **0** match [Observed, Python `re` this session, the denominator counted from the same pass] | **Not available.** This packet does **not** call slice 2 lawful or unlawful. It records the two repair routes the clause itself allows: a requirement-and-scenario pair added through CC-REV-2 and a new owner act, or the reviewed N/A judgment the clause names — "a recorded owner judgment homed in `decisions/` (RFC3-15)", honored only through an effective owner act under RFC3-16(a). This packet's view of the second: **not reachable here**, because the clause admits an N/A judgment only for a consequence "purely structural with no independently testable behavior", and a heading that names a project is independently testable by reading it [Inferred — the routes are Observed in the clause; whether slice 2 fits the second is a reading] |
| 3 Locator | **None enumerated on the recommended arm.** The one rendered change is a new refusal reason, and refusal reasons already render under PWB-REQ-005's disclosure requirement (lines 220–222) | **PWB-REQ-005**, line 206, with scenario **"Missing observation consent blocks content reads"** at lines 296–300, quoted verbatim: "**WHEN** no effective Butlers observation-consent act exists / **THEN** the project-shape observer performs zero body reads / **AND** the project model reports Unknown with the consent reason" | **Available.** The new refusal is the same shape the scenario already requires: zero reads, Unknown, reason rendered |
| 4 One profile schema | **None enumerated.** Two sentences in two unbound kit files; nothing rendered, nothing queried | n/a | n/a. Argued from the kit's own bar |
| 5 Registry profile | "API answers over epistemic state" — the deterministic-input set the machine answer exposes gains the profile digest; **and** "evaluation and snapshot displays", since the human surface exposes the same identities | **Requirement available, scenario partial.** **PWB-REQ-001**, line 73, whose normative text requires the observation to "bind the consent record, secret-policy version, source-discovery version and observer/parser version as deterministic evaluation inputs" (lines 74–76) and that "Human and machine readers SHALL receive those identities" (lines 76–77). Its scenario **"Source population is complete at one revision"** (lines 98–102) reads "**WHEN** Butlers is observed at revision R / **THEN** every admitted project-shape source resolves at R / **AND** the human and machine views expose the same complete source set" — which is about the *source set*, not about the input identity set. **No scenario states the case of a deterministic input being added.** PWB-REQ-001 carries exactly **one** scenario, the one quoted [Observed, counted this session over the 31 scenarios in that file]; the phrase "deterministic input" occurs at lines 76, 85 and 95, all inside the requirement's own prose and its falsifier, never inside a scenario | **Requirement available, scenario not.** Same two routes as slice 2, same reading on the second. The requirement's own sentence enumerates four deterministic inputs by name and a loaded profile is a fifth, so a strict reader may hold that adding one **contradicts** a closed list rather than implementing an open one — that reading is not this packet's to take, and it is the sharpest form of Q1 |
| 6 Self-profile proof | **None enumerated.** The render happens inside a test and reaches no surface | **PWB-REQ-005** line 206 and **RFC1-3** lines 130–133 are gates on whether the slice may run, not coverage of a consequence. No approved requirement names a self-observation [Observed, the 0-occurrence sweep above] | n/a for RFC2-26; **blocked by Q3**, which is the stronger gate |
| 7 Seeded entities | "evaluation and snapshot displays" — in the no-seeds case Trajectory and Orrery change what they show | **Available.** **POC-REQ-050**, line 777, "WHEN Orrery is read, it SHALL render a spatial projection of the observed code structure in which regions derive from the directory structure and declared capability-to-path mappings", with falsifier "a rendered region backed by no observed directory or declared mapping" (lines 791–793); scenario **"Stable city over one observation"** at lines 795–799, verbatim: "**WHEN** Orrery renders the same code-structure observation twice / **THEN** every region's position and extent is identical, and every region resolves to an observed path or declared mapping". Also **POC-REQ-051** — "Unmapped code is a visible Unknown region with a denominator" (line 812) — for the empty case | **Available.** The scenario's THEN, "every region resolves to an observed path or declared mapping", is exactly what a seeded region from the wrong project fails. Slice 7 implements a requirement the current code does not satisfy in the case the requirement covers |

**What the test establishes and what it does not.** It establishes
[Observed] that slices 3 and 7 map to named requirement-and-scenario pairs;
that slice 5's requirement is named and its scenario is not; that slice 2's
requirement is partial and its scenario absent; and that slices 1, 4 and 6
enumerate no RFC-0002 consequence at all. It does **not** establish that any
slice is lawful — that is Q1's, and RFC2-26's own scope sentence, "This
clause binds the whole RFC 0002 package, not this module alone" (lines
219–220), is a reading the owner may take more or less broadly than this
packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed specification text and nothing here amends a requirement.

**S1 (slice 1).** WHEN the portability sweep runs over the two POC source
trees, THEN it reports a count, the matching file list and the denominator,
AND the denominator is the number of files it actually decoded, not the
number it attempted.

**S2 (slice 1).** WHEN a file in the swept population contains a NUL byte,
THEN it is still decoded and still counted, AND a sweep that silently omits
it fails its own self-test.

**S3 (slice 2).** WHEN the active profile declares a display name, THEN the
page's first heading, both group headings, the not-authority notice, the four
page eyebrows and all fifteen remediation sentences carry that name, AND no
rendered sentence contains a proper noun absent from the profile.

**S4 (slice 2).** WHEN the profile's display name is changed, THEN every one
of those elements changes with it in one render, AND a test that only checks
the negative direction is not sufficient evidence for this scenario.

**S5 (slice 3).** WHEN the consent record names an approved locator and the
configured locator resolves to it, THEN the binding is `bound` with the same
`gitCommonDirectory` and the same snapshot identity as before this slice, AND
the observation digest is unchanged.

**S6 (slice 3).** WHEN the configured repository is not the one the consent
record names, THEN zero Git calls occur before the refusal and the reason is
`locator-unconsented`, AND a malformed or missing locator line refuses
identically rather than falling back to any compiled default.

**S7 (slice 5).** WHEN one field of the loaded profile changes, THEN the
observation digest changes, AND WHEN nothing but formatting changes, THEN it
does not.

**S8 (slice 5).** WHEN the registry entry's `observationGrammar` lacks a
field the profile schema requires, THEN the load refuses and the observation
reports Unknown with that reason, AND it does not fall back to a compiled
constant.

**S9 (slice 6).** WHEN the pipeline runs against a Syzygy profile at a fixed
revision, THEN each stage records crash, Unknown or claim with no expected
values asserted on the first run, AND every emitted claim is classified as
derivable from this repository's bytes or as leaked from the proving case's
copy path.

**S10 (slice 7).** WHEN a profile supplies no seeds, THEN Trajectory and
Orrery render an explicitly Unknown graph carrying its denominator, AND no
region, column or entity is rendered that resolves to no observed path or
declared mapping.

**S11 (slice 7).** WHEN the profile's display name changes, THEN no entity
identifier changes, AND the snapshot identity is keyed by repository id
rather than by a literal name prefix.

## Collision and sequencing

**Method.** Extract every code span from each sibling packet; keep those that
are implementation-plane paths (`apps/`, `packages/`, `scripts/`,
`docs/polaris-generation/`, or `package.json`); resolve each against this
worktree at `a9f671e` under two predicates — **resolves to anything**
(`os.path.exists`, so a directory span counts) and **resolves to a file**
(`os.path.isfile`); intersect the file-resolving set with M8's own **31-file**
candidate surface, which is every existing file named in Gate 3's topology
table [Observed, all counts computed this session; every one of the 31
resolves].

| Sibling | Head read this session | Resolving spans (any path) | Resolving spans (files only) | Intersection with M8's 31 |
|---|---|---:|---:|---:|
| M1 (lane A, on main) | `a9f671e` (the packet is on main; this worktree's copy is the same bytes) | 3 | 1 | **1** |
| M2, PR #36, P-69 | `f2f37dd` | 17 | 11 | **7** |
| M3, PR #37, P-70 | `6574600` | 15 | 13 | **6** |
| M4, PR #38, P-71 | `63b8e33` | 26 | 22 | **9** |
| M5, PR #39, P-72 | `ba9ca61` | 11 | 9 | **5** |
| M6, PR #40, P-73 | `83c9f60` | 24 | 13 | **2** |
| lane B, PR #35, P-68 | `4090f98` | not computed — see below | | |

**M8 is the collision-heavy packet in this set, and that is the finding.**
Where M6 reported zero against every sibling, M8 intersects five of the six.
The overlapping files, with the M8 slice that claims each: M4 at
`apps/three-surface-poc/src/governance-inputs.ts` (S3, S5),
`apps/three-surface-poc/src/orrery.ts` (S2, S7),
`apps/three-surface-poc/src/polaris-copy.ts` (S2),
`apps/three-surface-poc/src/polaris-copy.test.ts` (S1, S2),
`apps/three-surface-poc/src/polaris.ts` (S2),
`apps/three-surface-poc/src/routes.ts` (S2),
`apps/three-surface-poc/src/trajectory.ts` (S2, S7),
`packages/three-surface-poc-core/src/model.ts` (S7) and
`packages/three-surface-poc-core/src/project-shape-model.ts` (S5, S6). M2 at
`apps/three-surface-poc/src/git-observation.ts` (S3),
`apps/three-surface-poc/src/main.ts` (S7),
`apps/three-surface-poc/src/polaris-copy.ts`,
`apps/three-surface-poc/src/routes.ts`,
`apps/three-surface-poc/src/walkthrough-preflight.ts` (all S2),
`packages/three-surface-poc-core/src/model.ts` (S7) and
`project-shape-model.ts` (S5, S6). M3 at
`apps/three-surface-poc/src/polaris-copy.ts`,
`apps/three-surface-poc/src/polaris-first-reading.test.ts`,
`apps/three-surface-poc/src/polaris.ts`,
`apps/three-surface-poc/src/walkthrough-preflight.ts` (S2),
`apps/three-surface-poc/src/polaris-project-shape.test.ts` (S2) and
`project-shape-model.ts` (S5, S6). M5 at
`apps/three-surface-poc/src/polaris-source.ts`,
`apps/three-surface-poc/src/polaris.ts`,
`apps/three-surface-poc/src/routes.ts` (S2),
`packages/three-surface-poc-core/src/model.ts` (S7) and
`packages/three-surface-poc-core/src/project-shape-observation.ts` (S5). M1
at `apps/three-surface-poc/src/routes.ts` (S2). M6 at
`docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` and
`docs/polaris-generation/README.md` (S4) [all Observed, computed this
session].

**The intersection is between *proposed* surfaces, not landed diffs.** Every
one of the six sibling branches is a documentation branch: a name-only diff
against `a9f671e` in each worktree names only files under `docs/design/`,
`docs/evidence/`, `docs/reviews/` and
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — **no sibling
branch touches an implementation-plane file today** [Observed, run in all six
worktrees this session]. So the collision resolves by ordering, not by
negotiation, and the ordering is that M8 lands last.

**Lane B's row is not computed and is stated as such.** Lane B's cited
implementation-plane spans include two scripts that exist only on its branch
and do not resolve in this worktree, so the two-predicate method above gives
a figure that means something different for it than for the other five. What
can be said without computing it: **M8's 31-file surface contains no file
under `scripts/`**, and lane B's cited surface is governance plus `scripts/`,
so the intersection is 0 by construction of M8's surface [Observed, the
31-file list carries no `scripts/` path]. Lane B also edits
`scripts/check_governance.py`, which M8 does not touch but whose output M8's
two files must pass — so the order is: lane B lands, then this packet's check
is re-run before merge.

**The two other P2 packets drafted in parallel — M7 and M9.** Their content
is **[Unknown]** to this session; neither was read, and neither worktree was
opened. They are described as disjoint by design in files. That description
is **not** what the dossier's own evidence lists say, and the discrepancy is
recorded rather than smoothed: M9's dossier entry cites
`apps/three-surface-poc/src/polaris.ts`,
`packages/three-surface-poc-core/src/model.ts`,
`apps/three-surface-poc/src/trajectory.ts` and
`apps/three-surface-poc/src/orrery.ts` — four files that are all in M8's
31-file surface — and M9's own subject, one identity and one vocabulary
across the surfaces, is adjacent to slice 2's [Observed, the M9 dossier entry
read at source this session; **whether M9's packet actually claims those
files is Unknown**]. M7's dossier entry cites the generator package and
`apps/three-surface-poc/src/routes.ts`; the first is disjoint from every M8
slice but 4, and `routes.ts` is in slice 2's surface [Observed, same source,
same Unknown]. **The owner should expect M8 and M9 to need explicit
sequencing**, and this packet does not propose one for a packet it has not
read.

**Sequencing inside M8.** Slice 1 and slice 4 are independent of everything
and of each other; either may land first. Slice 3 is independent of all
others and is the smallest real change — it should land first among the code
slices. Slice 2 must precede slice 6's render-and-sweep limb, since the
heading and the remediation routes are slice 6's expected first failures.
Slice 5's limbs 1–4 may proceed before Q2 is answered; limb 5 may not. Slice
7 holds the shared-model WIP slot while it is open, so it must not overlap
slice 2's edits to `trajectory.ts` and `orrery.ts` — the two slices touch the
same two files and slice 7 goes second.

**Not verifiable this session.** [Unknown] Whether the sibling branches'
actual diffs stay inside the paths their packets cite, until they land.
[Unknown] What M7 and M9 propose to touch. [Unknown] Which arm the owner
takes on Q1, and therefore whether slices 2 and 5 are implementation or an
amendment. [Unknown] Whether the self-profile of slice 6 would produce mostly
honest Unknowns or a crash, because it has not been run and this packet did
not run it.

## Gate 6 — Engineering bar

1. **Every count in this packet carries its predicate and its denominator**,
   and every one was taken this session in the worktree at `a9f671e`. The
   file-level sweeps were run with Python `re` rather than `grep`, per
   verification rule 1, and the two places where a `grep` corroboration was
   attempted are reported with their disagreement rather than with the
   agreeing half alone.
2. **Two methods for the load-bearing count, and they disagreed.** 74 by
   Python over 133 files; 73 by `ugrep -il` over the same 133. The single
   divergent file, its NUL byte, its offset and the four invocations that
   establish it are recorded (rule 2). The dossier's figure is confirmed and
   its corroboration sentence is narrowed rather than repeated.
3. **The copy-table denominator was checked against a second count.** 191
   parsed rows against 191 raw occurrences of the row-opening literal; the
   first attempt gave 189 and the two missing rows were found and named
   rather than rounded away (rule 4).
4. **Rule-6 mutants are specified per slice and per guard branch**, above;
   each names the predicate to mutate and the fixture that must then fail,
   and slice 6's are explicitly deferred rather than invented for a fixture
   that has never run.
5. **Conformance expected values are literals in the tests**, never imported
   from the module under test (AGENTS.md), and slice 5's regression oracle is
   the existing digests, computed before the change.
6. **The copy-oracle caution is applied**: slice 2's predicate matches
   distinctive full clauses and the fixture profile's display name is a
   string occurring nowhere else, because a bare project name is reached by
   coincidence on a page that legitimately quotes the project's own text.
7. **No act-bound byte is proposed for edit except one, by an act.** Of the
   31 files in M8's surface plus the two governed artifacts it names — 33 in
   all — **4** appear anywhere in the digest-binding corpus, swept this
   session over every `*-MANIFEST.txt` and every
   `docs/evidence/*manifest*.json` in the repository plus
   `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`, denominator 22
   corpus files against 33 named paths. Two are
   the registry entry and the consent record, both genuinely act-bound; slice
   3 reads one and slice 5 edits the other **through a new owner act, which
   is the mechanism the binding act's own closing sentence names**. The other
   two, `apps/three-surface-poc/src/polaris.ts` and
   `apps/three-surface-poc/src/polaris-first-reading.test.ts`, appear in a
   mutation-run record that carries no sha256 field and therefore binds no
   bytes; the obligation there is to re-run, not to refrain.
8. **No observed-repository path is backticked anywhere in this file**, and
   no act argument, manifest digest or truncated signed digest is reproduced
   — the four digest comparisons this packet ran are reported as
   match/no-match with the record cited by path, per CG-7e and CG-15.
9. **Independent review.** This packet has had **none**. It is a first draft.
   Verification rule 10: every figure and every quotation above is bound to
   these bytes and to `a9f671e`, and any later edit retires a review bound to
   them.
10. **Conventions this packet was checked against, this session, over the
    bytes these figures now sit in.** Every non-fence line has an even
    backtick count — 0 of **1344** — so no code span is broken across a line
    break; four were, in the first draft, and each was rewritten rather than
    left. **6** lines exceed 78 columns outside fences, tables, block quotes
    and headings, and every one is a single unbreakable code span: four
    repository paths, one quoted HTML element and one path inside a sentence.
    Of **250** distinct code spans, **11** contain a `/` and do not resolve as
    a path here; each is enumerated in the evidence record and none is a
    path: five write-root and glob patterns, one regular expression, one HTML
    element, one HTTP route, one branch name, one bare `decisions/` inside
    the RFC2-26 quotation, and one change-directory name given without its
    parent — 5 + 1 + 1 + 1 + 1 + 1 + 1 = 11. **No observed-repository path is
    backticked anywhere in this file.**
11. **What this packet does not claim.** It does not claim the pipeline is
    portable; it claims the portability debt is measurable and measures it.
    It does not claim any slice is lawful. It does not claim the self-profile
    would pass, or fail, because it was not run.

## Funnel summary

```
## Feature Request: M8 - Portability: the profile as a loaded, digest-bound registry input
Size: small (slices 1, 4) / medium (slices 2, 3, 6, 7) / large (slice 5)
Baseline: Syzygy a9f671e; the dossier's syzygy_audited_at is f4589e2 and every line it cites was re-verified at a9f671e, with the eight differences tabulated in this packet and recorded in the evidence record
- G1 Motif: the governed artifacts already hold the per-project grammar as data and the code keeps hard-coded copies whose tests prove them byte-equal, so amending the registry entry changes nothing at runtime - 2 non-test modules name the registry entry and both read it as bytes for a digest, never as a grammar; 4 of the copy table's 191 rows carry a proper noun and the page's h1 is one; the approved locator is one absolute path compiled into the app while the digest-bound consent record already carries it; PocModel types the project name as the literal type 'Butlers' so a second project cannot be typed; 74 of 133 top-level modules name the proving case and nothing stops the 75th [Observed, every figure measured this session with its predicate and denominator]
- G2 Doctrine: VIS-1's rank-1/rank-2 ordering (slices 2 and 7 are rank-1 repairs; Q6 spends rank 2 to buy rank 1), VIS-2 (slice 7's empty case, slice 6's own Unknown), VIS-5 (implementation plane, plus one deliberate .syzygy write under an act), VIS-7 (an encoding that misreports). SEC-1 is quoted and read as NOT reaching the locator - no SEC clause names one; RFC1-2 and RFC1-3 do
- G3 Topology: apps/three-surface-poc/src + packages/three-surface-poc-core/src + docs/polaris-generation; one boundary crossed, deliberately, by slice 5's last limb into the act-bound registry entry; every other slice implementation-plane only
- G4 Design: a reporting-only portability predicate with its blind spot named; a model-derived project identity leaving the claim role alone; the locator parsed out of already-digest-verified consent bytes after admission, so PWB-REQ-005's closed 195 is untouched; one coordination page; a five-limb profile where only the last needs an act; a self-profile designed and not run; the seeds out of the shared model with an Unknown empty case
- G5 Spec: 0 occurrences of second repositor / second project / portab / generaliz / locator in either adopted specification, denominator both files in full; both files are act-bound bytes so a portability requirement is a CC-REV-2 delta and a new act. RFC2-26 run over all seven slice rows (denominator 7): slices 3 and 7 map to named requirement-and-scenario pairs; slice 5's requirement is named and its scenario is not; slice 2's requirement is partial and its scenario absent; slices 1, 4 and 6 enumerate no RFC-0002 consequence
- G6 Bar: two methods for the load-bearing count and they disagreed by one file over a NUL byte, reported with the divergence; the copy denominator checked twice and the first attempt's two missing rows named; rule-6 mutants per slice, deferred honestly for slice 6; 4 of 33 named files appear in the digest-binding corpus and only one is proposed for edit, through the act its binding act names; NO independent review yet - this is a first draft
Acts: slices 1, 3, 4, 6 and 7 are argued to ride PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md (2026-09-02) as continued 2026-09-05, whose grant and exclusions are quoted in Q1 and Q3; slice 4 rides POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md (2026-09-12) instead; slice 5's last limb needs a third registry-entry amendment act (Q2); slice 6 needs a consent record, a registry entry and a policy extension naming this repository, none of which exists (Q3); slices 2 and 5 are held pending Q1
Open questions: Q1-Q7 above. NOT registered in PENDING-OWNER-DECISIONS.md - the register row lands after review 1, batched with the siblings'; the five siblings' existing rows are P-68 lane B, P-69 M2, P-70 M3, P-71 M4, P-72 M5 and P-73 M6, each only on its own branch
Sign-off: pending - the owner's
Recommended handoff: land slice 3 first (smallest, no act, no rendered claim), then slice 1 reporting-only and slice 4; rule Q1; then slice 7 under Q7's ceremony; slice 2 after Q1 and Q5; slice 5's limbs 1-4 any time and limb 5 after Q2; slice 6 only after Q3
```

## Recommended handoff

**If Q1 is answered as recommended:** file no new bead. Build slice 3 first,
under `syzygy-dov.8`. It is the smallest change with the largest unblock: it
removes the one machine-specific literal that makes the POC unbuildable as-is
on any other checkout, it makes a consented second repository a governance
act rather than a rebuild, and its oracle is exact — the current binding must
resolve byte-identically. Then slice 1 reporting-only and slice 4, neither of
which changes behaviour. Then slice 7, under Q7's answer.

**If Q1 is answered the other way** — that a portability requirement must
exist first — then slices 2 and 5 hold behind a CC-REV-2 delta and a new
owner act, and slices 1, 3, 4 and 7 proceed. That is a coherent outcome and
should be written down as one: the reason it is coherent is that the adopted
specification's subject really is one named repository, stated in its own
binding reader note, and a specification that says so is not wrong — it is
narrow. Widening it deliberately is better governance than reading it
loosely, and it costs one amendment cycle.

**If Q2 is answered as recommended:** slice 5 runs limbs 1–4 immediately and
the amendment packet is prepared in parallel, so limb 5 lands the day the act
is performed. If the owner declines and prefers an unbound profile file, land
limbs 1–4 anyway — the threading is worth having on its own — and record in
the bead's close reason that the registry entry remains a checksum, so the
next person does not mistake a threaded parameter for a governed input.

**If Q3 is answered as recommended:** the three acts are prepared as one
packet and slice 6 runs against this repository at a fixed revision. If the
owner declines, slice 6 stays a design and **the portability claim stays
Unknown** — which is the honest outcome, and the packet says so rather than
substituting the predicate's count for evidence the pipeline works. A
count of 0 proper nouns is not a proof of portability; it is the absence of
one kind of counter-evidence.

**If Q4 is answered as recommended:** slice 3 lands as designed. If the owner
takes the second arm, the slice holds behind a CC-REV-2 delta that moves
PWB-REQ-005's closed population from 195 to 198, and the bead records that
the locator became an RFC3-16(b)-adjacent field with three new invalid cases
and their mutation proofs.

**If Q5 is answered as recommended:** slice 2 derives the name and leaves the
claim role alone, and a follow-up bead carries the anchored-fact promotion
with REQ-014's covering-and-minimal oracle. If the owner takes the second
arm, the two land together and the anchor target is the consent record, which
is a `decision` in REQ-014's closed class.

**If Q6 is answered as recommended:** the lede is deleted and the slot renders
nothing until a profile supplies an owner-declared line. If the owner keeps
it, it must carry a disclosure naming it owner-supplied framing — and the
bead should record that the portability predicate cannot see it, so its
passing count never covers this row.

**If Q7 is answered as recommended:** slice 7 opens the shared-model WIP slot
and nothing else touches the model while it is open, which means slice 2's
edits to `trajectory.ts` and `orrery.ts` wait. If the owner rules limb 1
ordinary engineering, limb 1 lands with slice 3 and the ceremony starts at
limb 2 — which is the faster path and the one this packet would take if the
rule were its own to make.
