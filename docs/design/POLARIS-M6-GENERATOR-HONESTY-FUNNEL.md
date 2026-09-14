
# Feature request M6 — The generator's honesty contract: somewhere to put Unknown, a coverage table that carries verdicts, an accounted edit, and an onramp that runs

> **Candidate — binds nothing.** Bead `syzygy-dov.6`, move M6 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`),
> written in the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its
> four siblings. Planning only: nothing here authorizes implementation, and no
> arm below is called lawful or unlawful by this packet. The owner disposes.

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1 and 5) / **medium** (slices 2, 3 and 4) / **large**
(the deferred slice 6).

Baseline: Syzygy `a9f671e` (main). The subject is the generator package and
its authoring kit, not the rendered Polaris page.

## The six questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1 is the packet's central question and the other five
are downstream of it; Q6 is the only one that could stop every slice.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Is adding a `disposition` field to the provider stage schemas an implementation of the adopted specification, or an amendment to it?** The landed schemas carry no such field — 25 distinct field names across all six stage schemas, 0 of them a disposition, 2 enums (`kind`, 9 values; `severity`, `blocking`/`advisory`), neither epistemic [Observed, computed this session from the built schema objects; method and census in the evidence record]. Three bound artifacts already name the field: the effective REQ-polaris-generation-019 requires each requested asset to resolve "to one produced, omitted or unresolved disposition" (`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md` line 453, identical in its first two sentences to the predecessor at `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md` line 1015); the effective REQ-polaris-generation-004 requires "Every requested asset SHALL have an explicit produced, reasoned-omission or unresolved disposition" (overlay line 78); and `openspec/changes/polaris-manifesto-generation/SCHEMA-CONTRACT.md` lines 33–39 already gives the three-row table with each disposition's required payload and invariant. | **It is an implementation, not an amendment; no CC-REV-2 delta is needed for the field itself.** The bound text names the field, its three values and its payloads; adding it to the executable schema conforms the code to the specification rather than changing the specification. **The counter-argument, which this packet does not resolve:** SCHEMA-CONTRACT.md's disposition vocabulary is *produced / omitted / unresolved*, REQ-004's effective vocabulary is *produced / reasoned-omission / unresolved*, and the shipped prompts say "planned, unnecessary-with-reason or unresolved" (`docs/polaris-generation/AUTHORING.md` line 102) and "produced, unnecessary-with-reason or unresolved" (`docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` line 43) — four spellings of a three-value enum across four artifacts, three of which are digest-bound and cannot be edited to agree. Whichever literal the implementation picks, it will disagree with at least one bound artifact, and that choice is the owner's [Inferred]. **Second lawful arm:** rule it an amendment and route it through CC-REV-2 before any code lands — slower, and it re-opens bytes an act bound. **Default if unanswered: slices 2, 3 and 4 do not ship**; slices 1 and 5 are unaffected. |
| Q2 | **Does the `support` discriminant — replacing every `sourceIds: string[]` with a tagged union of quoted / synthesis / inference / unresolved — go in with slice 2, or is it deferred?** This is L3-M1's other half and the largest schema change M6 could carry. Today `references()` (`packages/polaris-generation-core/src/provider-draft.ts` lines 90–98) checks only that a cited source id *exists*; nothing in the package compares a claim's text to the source text it cites [Observed, read at source this session]. The effective REQ-polaris-generation-002 requires that "Source-supported inference SHALL expose its admitted premises and inferred status" (overlay line 9; predecessor at base line 52), and base REQ-polaris-generation-003 requires the bundle to "distinguish source claims, supported inference and non-normative framing and preserve captured epistemic states" (base line 98). | **Defer it to its own funnel; do not fold it into slice 2.** Slice 2 as designed adds an *asset-level* disposition, which the bound text names field-for-field. The support discriminant additionally proposes a *mechanical entailment check* — a quoted span must be a substring of the named source — which is new machinery, changes every claim-bearing node's shape at once, and would make slice 2 unreviewable as one change. **Counter-argument, and it is strong:** without it, a paragraph's citation still means only "a source with this id exists", so slice 2 closes the asset-level hole and leaves the claim-level one open, and the owner may reasonably want both closed in one pass rather than shipping a half-honest schema twice. **Second lawful arm:** take it now as slice 2b, accepting a larger single change. **Default if unanswered: deferred**, and this packet records the claim-level hole as open. |
| Q3 | **Should the fidelity verdict become fail-closed over coverage rows, so that silence blocks readiness instead of passing it?** Today `reviewVerdict` (`packages/polaris-generation-core/src/provider-draft.ts` lines 148–152) blocks only when some finding carries `severity: 'blocking'`, and `findings` has `minItems` 0 (line 31) — so a review that enumerates every id and says nothing passes. The effective REQ-polaris-generation-006 requires the review to "record both inventory-to-draft coverage and draft-to-source support, including justified omissions; unresolved material omissions SHALL prevent readiness" (overlay line 180). | **Yes — make readiness require a positive disposition on every row of a denominator the model cannot narrow.** This is the one polarity change in M6: VIS-2's "no evidence means Unknown, not success" applied at the gate the product's honesty rests on. The existing set-equality checks (`same()` at lines 127–128) already force the whole denominator; the change is to carry a verdict on each row and to block on any row that is not positively cleared, and on any missing row. **Counter-argument:** it will make runs fail that pass today, including the shipped synthetic demo, and a run that cannot reach ready is a worse demo even when it is a more honest one. **Second lawful arm:** add the rows without changing the verdict polarity, so the coverage table is *visible* but not *binding* — honest to read, unchanged in effect. **Default if unanswered: rows are added, polarity is not changed** (the second arm), and the packet records that readiness still passes on silence. |
| Q4 | **`docs/polaris-generation/example.json` fails the landed validator 19 times out of 19 attempts. Is it regenerated from a real validation, or re-labelled?** [Observed, run this session: every combination of the six landed stages against the file's `illustrativeOutput`, `illustrativeLaterDraft` and the whole file throws `invalid-fields`; `stageSchema('understand')` throws `invalid-stage`.] The file is not a stage payload and does not claim to be: its own `exampleKind` is `synthetic-documentation-handoff`, its `schemaStatus` is `candidate-not-registered`, its `stageId` is `understand` — a stage the landed pipeline does not have — and the kit calls it "one small handoff… neither a complete manifesto nor a successful generator run" (`docs/polaris-generation/README.md` lines 41–42). | **Regenerate it from a real `validateStage` call and keep a second, clearly separated illustrative block for the not-yet-implemented understanding stage.** An operator told the example is ground truth will write to it; today what they write is rejected with `invalid-fields` and no explanation. **The counter-argument is that the dossier's framing is unfair and this packet agrees in part:** "example.json fails the landed validator" is true and was measured, but the file never asserted validator-conformance, so the defect is that the kit routes operators to it (`README.md` line 41, "Inspect the synthetic example") without saying which half is executable. **Second lawful arm:** leave the bytes and add one sentence naming the two halves — cheapest, and it fixes the routing without fixing the example. **Default if unanswered: the second arm** (one sentence), because it is reversible and needs no schema decision. |
| Q5 | **The onramp: an install line only, or an install line plus a fresh-install assertion in the battery — and is `packages/polaris-generation-core` added to `build:poc`'s explicit project list?** Measured this session at `a9f671e` in a worktree where `npm ci` had been run: the README's exact command chain **succeeds**, exit 0. With the workspace symlink `node_modules/@syzygy/polaris-generation-core` moved aside, the same chain fails with 42 TypeScript errors, 5 of them `TS2307: Cannot find module '@syzygy/polaris-generation-core'`, across 6 files; restoring the symlink restores exit 0 [Observed, both directions run this session]. `build:poc` (`package.json` line 15) names four projects and **not** `packages/polaris-generation-core`; the package builds only transitively through `apps/three-surface-poc`'s project reference. | **Install line plus a battery assertion, and add the package to `build:poc`'s explicit list.** The install line alone documents the workaround; the assertion is what stops the class recurring, and `poc:fresh-checkout-demo` already exists as the shape to extend. Adding the package to the explicit list costs nothing and removes a silent dependence on one tsconfig reference. **Counter-argument:** a fresh-install assertion means an `npm ci` in the battery, which is the slowest thing the battery could do, and the failure it catches is a developer-machine failure rather than a product one. **Second lawful arm:** install line only — one line, zero cost, no recurrence guard. **Default if unanswered: the install line lands and the assertion does not.** |
| Q6 | **Which act covers these five slices, and does RFC2-26 gate any of them?** `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 42 reads, verbatim: "Authorize the full EXECUTION-PHASES.md implementation goal, including protected effect host, complete owner experience, two-project and changed-source proof obligations. Phase A alone is not completion. Real-project reads, provider egress and destination writes remain separately admitted; no effect, production release, broad remote access or observed-project code execution is authorized by this act." All five slices sit inside Phase A, whose scope is "the source/draft contracts, immutable identities and support, bounded pure stage controller, dependency invalidation, trusted rendering and fixture adapters" and whose named requirement set is "001-012, 014-019 and 025" (`openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md` lines 10–11 and 18). None reads a real source, calls a provider or writes outside Syzygy. | **The existing implementation-authorization act covers all five; no new act is needed, and RFC2-26 gates none of them.** RFC2-26 bars scheduling implementation work for user-observable consequences **of RFC-0002** from that RFC alone; these slices are scheduled from an adopted OpenSpec specification with 31 effective requirements and 177 scenarios, and Gate 5 below runs the requirement-and-scenario test over all five slices and the deferred sixth, with its denominator stated. **Counter-argument:** slice 3 changes when a run reaches ready, which is a readiness state the owner will see, and slice 2's dispositions are rendered by `draft-preview.ts`; an owner who reads RFC2-26's consequence list broadly ("Unknown-reason and rendering-tier presentation") may want those two ruled explicitly rather than inherited. **Second lawful arm:** rule slices 2 and 3 under a fresh direction naming them. **Default if unanswered: slices 1 and 5 proceed** (documentation and build plumbing, no observable consequence enumerated); slices 2, 3 and 4 hold. |

### Decided in this packet, not put to the owner

**The dossier's "prerequisite: none" survives, with one correction.** The
dossier's machine record gives M6 a `prerequisite` value of
`none (confirm against generator tasks.md)`, and its prose says "these are
already-authorized
generator implementation tasks that the landed code missed, so confirm
against `openspec/changes/polaris-manifesto-generation/tasks.md` before
filing to avoid a duplicate of an unchecked task." Confirmed this session:
`tasks.md` carries **24** checkbox lines under the predicate `^- \[[ xX]\] `
and **all 24 are unchecked**, 0 checked, over a 52-line file [Observed,
counted this session]. Every M6 slice duplicates an unchecked task and is
therefore filed **against that task**, not as new scope — the per-slice task
is named in Gate 3. So "prerequisite: none" holds in the sense the dossier
meant it: no doctrine amendment, no owner act, no spec amendment is needed
*to file the work*. The correction is that it does not follow that no owner
ruling is needed to *land* it: Q1 and Q3 are genuine gates, and Q1 exists
precisely because the bound artifacts disagree with each other about the
disposition vocabulary.

**S9-F4's doctrine tag is wrong and is corrected here.** The finding cites
SEC-1 for the no-egress boundary. SEC-1 is "Authenticated by default"
(`.syzygy/governance/doctrine/security.md` line 10) and is about endpoint
authentication. The doctrine that governs sending governed-project content to
a model provider is **SEC-2**, "Portfolio data leaves owner-controlled
infrastructure only through explicit, scoped consent" (line 25), whose text
says in terms: "**Model providers are such services.**" Slice 5 is argued
from SEC-2 below.

**M6's slice list is one slice short of its own "What" bullet.** The
dossier's What bullet names six moves (L3-M1, S9-M2, L3-M2, L3-M3, S9-M1,
S9-M4, S9-M3) and its Slices list gives five. S9-M3 — the diagram, deep-dive
and glossary promise-to-schema gap — appears in the What and in
`evidence_findings` as S9-F3, and in no slice [Observed, read at source this
session]. It is carried below as a deferred slice 6 with its mapping done, so
the gap is recorded rather than dropped. L3-M1's support discriminant is the
other unplaced half and is Q2.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `security.md` | VIS-1, VIS-2, VIS-3, VIS-4, VIS-5; SEC-2 |
| Decisions | `.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`, `POLARIS-GENERATOR-APPLICABILITY-ACT.md`, `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`, `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` | all four dated 2026-09-12 or 2026-09-13; the third is the implementation grant quoted in Q6 |
| Specification | `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md` composed with `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md` | effective composition **31 requirements and 177 scenarios** per the understanding act, Scope paragraph |
| Package contracts | `SCHEMA-CONTRACT.md`, `ASSET-CONTRACT.md`, `SOURCE-POLICY.md`, `EXECUTION-PHASES.md`, `tasks.md`, all under `openspec/changes/polaris-manifesto-generation/` | all are rows of the adopted offer's file set (`docs/evidence/polaris-generator-current-scope-2026-09-12.json`, 21 rows) and are therefore digest-bound |
| Contracts | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` | RFC2-24's closed twelve reasons; RFC2-26's OpenSpec-seam phase rule, run in Gate 5 |
| Policies | `.syzygy/governance/contracts/candidates/policy-candidates/` (CC-SPEC, CC-IMPACT, in force despite the directory name) | CC-REV-2 is the amendment path Q1 would need on its second arm |

**How the specification composes.** AGENTS.md records the rule: generator
requirement lookup composes the original change with the explicit
understanding-amendment overlay. The understanding act's Scope paragraph is
the authority for which side wins: "REQ-polaris-generation-002, 004, 006,
009, 012, 014 and 019 take their full amended clauses and preserved
scenarios; 030 and 031 are added. The other 22 predecessor requirements
remain unchanged." Every requirement this packet relies on is therefore cited
at the overlay when it is one of those seven, and at the predecessor
otherwise, with both line numbers given where the dossier cited the
predecessor.

**Three bound-byte constraints this packet obeys.** (a) Every file named in
the Gate 0 "Package contracts" row is a row of the adopted offer's file set,
so **no slice proposes editing one** — Q1's first arm conforms code to those
bytes rather than changing them. (b) `SCHEMA-CONTRACT.md`'s current sha256
equals the value recorded for it in
`docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json`, so the
lines quoted here are the bound bytes and not a later edit [Observed,
`sha256sum` this session, compared against that record; neither value is
reproduced here, per CG-15 — cite the record by path]. (c)
`docs/evidence/polaris-generator-current-scope-2026-09-12.json` carries
`"status": "unadopted; awaiting final independent review and owner acts"`
and `"implementedGenerator": false`. That is a **pre-act** snapshot: the
three acts were performed on 2026-09-12 and the record's own status line was
never rewritten. Per AGENTS.md, read the act record, never the package
banner; the same shape governs the two specification files, both of which
still open "Candidate specification — binds nothing until the required owner
adoption" over bytes an act bound.

## Gate 1 — Motif

**The kit's flagship honesty claim does not exist in the code the kit points
to.** `docs/polaris-generation/README.md` line 70 states the product
promise — "Missing evidence is Unknown; unsupported assets are unresolved
with a reason" — and `packages/polaris-generation-core/src/prompts.ts` line 6
instructs every one of the six stages to "Follow the supplied schema's
unresolved/failure representation when support or capability is missing".
The supplied schema has no such representation. A model with no evidence
therefore has exactly two schema-conformant moves: omit, which is invisible,
or invent, which is indistinguishable from support. That is VIS-2 inverted at
the one seam the product's stated goal runs through.

**The specific shape, in four measurements.** (1) Across all six landed stage
schemas there are **25** distinct field names and **2** enums; **0** fields
and **0** enum values can hold a disposition, an unresolved state or an
epistemic class. (2) **5** prompt instructions direct the model to use a
named schema representation for missing or unsupported material, in stages
`common`, `plan`, `edit`, `fidelity` and `repair`. (3) The fidelity stage's
coverage declaration is two bare id lists — `inventoryIds` and `blockIds`,
each forced by `same()` to equal its whole population, which is genuinely
good denominator discipline — with **no per-entry verdict**, so its entire
mechanical content is "I enumerated all of them", and `findings` may be
empty. (4) `author`, `edit` and `repair` share one schema object, byte-equal
under `JSON.stringify` [Observed, compared this session], so an edit that
deletes half the author's paragraphs validates, and the next fidelity call's
`blockIds` denominator is recomputed from the shrunken draft — the deletion
is not merely unreported, it is unreportable.

**And the onramp is conditional on a state the kit never names.** The
README's one runnable command works from a checkout whose `node_modules` is
current and fails with five `TS2307`s from one whose workspace symlink is
absent, with no diagnostic pointing at the cause. The kit states no setup
step at all.

**Success criteria, per slice.** Slice 1: the README's exact command chain
runs from a state the README describes, and a battery check fails if it stops
doing so. Slice 2: a provider that lacks support for a requested asset has a
schema-conformant way to say so, and the shipped example demonstrates it.
Slice 3: the reviewer's coverage claim carries a verdict per row, and a
missing row is an invalid output rather than a pass. Slice 4: every block id
of an edit's or repair's input appears in its output's account, with an
action. Slice 5: the egress boundary is restated where an operator would act
on it. None of these makes anything green; three of them make things that are
silently green today go honestly Unknown.

**What M6 is not.** It is not a change to the rendered Polaris page, not a
provider integration, not a real-source read, and not a claim that the
generator works. Every slice runs against the scripted synthetic adapters the
demo already uses.

## Measurements at `a9f671e`

Every figure below was taken this session in the worktree at `a9f671e`.
Method, predicate, denominator and raw output for each are in the evidence
record beside this packet.

### The demo command chain, run this session

The README's command is at `packages/polaris-generation-core/README.md`
line 55, under the sentence at line 53, "Run the controlled end-to-end
example from the repository root:". It is the only occurrence of
`poc:generator-demo` in either README [Observed, literal sweep over the two
files]. Run from the worktree root with `--out` under this session's scratch
directory:

| Run | Condition | Exit | Output |
|---|---|---|---|
| 1 | as-is, after `npm ci` | 0 | `Created three synthetic pipeline previews and their stage records. No real provider or project was used.` |
| 2 | `node_modules/@syzygy/polaris-generation-core` moved aside; `dist/` of both projects removed | 2 | 42 `error TS` lines, of which **5** are `TS2307: Cannot find module '@syzygy/polaris-generation-core' or its corresponding type declarations`, across **6** files, all under `apps/three-surface-poc/src/polaris-generation/` |
| 3 | symlink restored, rebuilt, rerun | 0 | same success line as run 1 |

Run 1 produced 7 files — three `.html`, three `.json` and a `report.json`,
41,940 bytes in total. The remaining 37 errors in run 2 are downstream
`TS7006`/`TS2339` consequences of the five unresolved imports, in the same
six files.

**So the dossier's S9-F1 reproduces as a mechanism and not as a verdict.**
The finding's own evidence names the cause — "this checkout's `node_modules`
predates the package by three days and was never reinstalled" — and the
counterexample above confirms it: the break is the missing workspace symlink,
present or absent, and nothing else. The finding's headline, "fails on the
exact documented command chain… from a fresh checkout", is therefore
**overstated for a genuinely fresh checkout** (clone, `npm ci`, run: exit 0)
and **exact for the state the finding actually observed** (a checkout whose
install predates the package). What survives, and is the thing slice 1
repairs, is the second half of the finding's own title: *the kit states no
setup step*. The literal `npm ci` occurs 0 times in the core README and
0 times in the four kit files [Observed, literal sweep, denominator 5 files].


**One further defect this session found and the dossier did not.**
`build:poc` (`package.json` line 15) is `tsc -b --force` over four projects,
and `packages/polaris-generation-core` is **not one of them**. The package is
built only because `apps/three-surface-poc/tsconfig.json` declares a project
reference to it. That is a single point of silent failure for the same class
of break, and Q5's third limb proposes adding it to the explicit list.

### Schema field census, computed from the built schema objects

Method: import `stageSchema` from the package's own `dist/provider-draft.js`,
walk each of the six stage schemas recursively, collect every `properties`
key and every `enum`. Denominator: all six stages.

| Stage | Schema version | Field count | Fields |
|---|---:|---:|---|
| `inventory` | `polaris-provider-inventory-v1` | 5 | `entries`, `id`, `kind`, `sourceIds`, `statement` |
| `plan` | `polaris-provider-plan-v1` | 5 | `id`, `reason`, `sections`, `sourceIds`, `title` |
| `author` | `polaris-provider-author-v1` | 15 | `deepDives`, `diagrams`, `edges`, `from`, `id`, `introduction`, `label`, `nodes`, `paragraphs`, `sectionId`, `sections`, `sourceIds`, `text`, `title`, `to` |
| `edit` | `polaris-provider-edit-v1` | 15 | identical to `author` |
| `repair` | `polaris-provider-repair-v1` | 15 | identical to `author` |
| `fidelity` | `polaris-provider-fidelity-v1` | 6 | `blockIds`, `findings`, `inventoryIds`, `message`, `severity`, `target` |

**Distinct across all six: 25.** The two enums are
`inventory.entries[].kind` (`purpose`, `beneficiary`, `thesis`,
`capability`, `choice`, `term`, `qualification`, `conflict`, `other` — 9
values) and `fidelity.findings[].severity` (`blocking`, `advisory` — 2
values).

**The zero, with its predicate.** Predicate: a field whose name or whose enum
admits a per-asset or per-claim disposition, an unresolved state, an omitted
state, or an epistemic class (quoted versus inferred versus synthesised).
Over the 25 names and the 11 enum values, **0** qualify. The nearest
candidate is `plan.sections[].reason`, which is the free-text justification
for a section's presence, not a disposition on a requested asset; and
`fidelity.findings[].severity`, whose two values are a triage level, not a
disposition. This is the same zero L3-F2 and S9-F2 report by a different
method — a literal grep for `disposition|unresolved|unnecessary` over
`provider-draft.ts` and `pipeline.ts` — and the two methods agree
(verification rule 2).

**`author`, `edit` and `repair` are one object.** `stageSchema` returns three
different `version` strings over a schema that is byte-equal under
`JSON.stringify` for all three [Observed, compared this session]. The
declaration is at `packages/polaris-generation-core/src/provider-draft.ts`
line 33:

```
const schemas: Record<GenerationStage, Schema> = { inventory, plan, author: draft, edit: draft, repair: draft, fidelity };
```

### Prompt instructions naming a schema representation that does not exist

Predicate: a sentence in `packages/polaris-generation-core/src/prompts.ts`
that directs the model to express missing, unsupported or changed material
**using a named schema** ("the supplied schema", "the schema's", "the trusted
schema"). Denominator: the whole file, 30 lines, 7,517 bytes. Count: **5**.

| Line | Stage | Instruction, verbatim |
|---:|---|---|
| 6 | common | "Follow the supplied schema's unresolved/failure representation when support or capability is missing" |
| 13 | `plan` | "Account for every requested asset with the schema's disposition and a reason; unsupported required assets remain unresolved." |
| 18 | `edit` | "Preserve source support and report changed content and affected references using the supplied schema." |
| 21 | `fidelity` | "Return findings tied to supplied handles, severity and unresolved reasons using the trusted schema." |
| 22 | `repair` | "Return the schema's affected content and finding-to-change dispositions; retain explicit unresolved findings when a valid repair is unsupported." |

The broader literal sweep, same file, same denominator, case-insensitive:
`unresolved` **6** (lines 6 ×2, 10, 13, 21, 22 — the line-10 occurrence is
"unresolved questions", a property of source content rather than a schema
representation, which is why the directive count is 5 and not 6);
`disposition` **5** (lines 10, 13, 16, 21, 22); `omission` **2** (10, 20);
`unsupported` **5**; `omitted` **0**. The only `unknown` in the file is the
error string `'unknown-generation-stage'` at line 27.

### The fidelity coverage shape

Quoted from `packages/polaris-generation-core/src/provider-draft.ts`
lines 30–32, the whole declaration:

```
const fidelity = object({ inventoryIds: { ...list(handle, 1), uniqueItems: true }, blockIds: { ...list(handle, 1, 5000), uniqueItems: true },
  findings: list(object({ severity: { ...text, enum: ['blocking', 'advisory'] }, message: text, target: handle }), 0, 1000),
});
```

Per-entry fields on each coverage direction: **0** on `inventoryIds`, **0**
on `blockIds` — both are `handle` arrays, and a `handle` is a string matching
`^[A-Za-z0-9][A-Za-z0-9_.:-]*$` (line 14). Per-entry fields on a finding:
**3** (`severity`, `message`, `target`), and `findings`' `minItems` is **0**
(line 31), so a review with complete enumeration and no findings is valid and
`reviewVerdict` returns `blocking: false` (lines 148–152). The denominator
discipline that makes the enumeration whole is at lines 127–128:
`same(data.inventoryIds, unique(inv.entries.map((entry) => entry.id)));` and
`same(data.blockIds, handles.blocks);`, with `same()` at lines 86–89 throwing
`incomplete-coverage` on any inequality. That discipline is the best idea in
the package and every slice below preserves it.

### What edit and repair return, and which validator compares output to input

`pipeline.ts` line 262 is `context.draft = await stage('edit', context);`
and line 267 assigns `context.draft` from a `repair` stage call carrying the
verdict's findings. Both overwrite the prior draft in place.

The package exports exactly two validators over provider payloads:
`validateStage` (`provider-draft.ts` line 107) and `reviewVerdict` (line
148); the other four exports are `encodeCanonicalJson`,
`digestCanonicalJson`, `parseBoundedJson` and `stageSchema` [Observed,
enumerated by a literal sweep for lines beginning `export` followed by
`function`, `async function`, `const`, `interface` or `type`, over the four
non-test sources].

**Absence claim, with its sweep.** `validateStage`'s `else` branch — the
branch that runs for `author`, `edit` and `repair`, lines 131–144 — reads
`context.plan` at lines 133, 134 and 137 and **never reads `context.draft`**.
A literal sweep of `provider-draft.ts` for `context.draft` returns exactly
two lines, 124 and 126, both inside the `fidelity` branch; a sweep for
`priorDraft` returns 0 [Observed, denominator: the whole file, 152 lines].
So no validator in the package compares a stage's output to its input, and an
`edit` output that drops arbitrarily many prior blocks validates, provided it
still covers the plan's section ids (line 137).

### The kit's promises against the landed schema

| Promise, quoted | Where | Schema field |
|---|---|---|
| "For each visual supply its reader question, named nodes, typed edges, edge meaning, source support, necessary qualifications, text equivalent and proposed placement." | `docs/polaris-generation/AUTHORING.md` lines 45–46 | of the eight, the diagram schema (`provider-draft.ts` lines 24–27) carries **2**: named nodes (`nodes[].label`) and source support (`sourceIds`). No reader question, no edge meaning distinct from `label`, no qualifications, no text equivalent, no placement, no legend. |
| "one meaningful trade-off, and links back to the parent and to its evidence" | `AUTHORING.md` line 62 | `deepDives` (line 28) carries `id`, `title`, `sectionId`, `paragraphs`. **0** of the three. |
| "add a glossary when it helps further reading" | `AUTHORING.md` line 26 | **absent**: the literal `glossar` occurs 0 times in `provider-draft.ts` and `pipeline.ts`, and once in `prompts.ts` (line 13, as prose) [Observed, case-insensitive sweep over the four non-test sources]. |
| "Glossary entries are shared by inline definitions and glossary routes" | `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` line 40 | same absence. |
| "Every requested asset has a produced, unnecessary-with-reason or unresolved disposition" | `ARTIFACTS-AND-TOOLS.md` line 43 | **absent**, per the field census above. |
| "Give every requested asset a planned, unnecessary-with-reason or unresolved disposition." | `AUTHORING.md` line 102, inside a copy-pasteable Plan prompt block | **absent**. |

S9-F3 cited `AUTHORING.md:45-49`, `:60-63`, `:26` and
`ARTIFACTS-AND-TOOLS.md:40-41`, `:43`. Re-verified at `a9f671e`: the diagram
sentence spans lines 45–46 (not 45–49, which includes two further sentences),
the trade-off clause is on line 62 (inside 58–71), and the other three are
exact.

### The no-egress boundary across the kit's four files

Predicate and denominator: the literal `egress`, case-sensitive, over
`docs/polaris-generation/README.md` (102 lines), `AUTHORING.md` (144),
`ARTIFACTS-AND-TOOLS.md` (108) and `example.json` (119) — 473 lines.
Count: **1**, at `README.md` line 4: "This kit grants no source access,
provider egress, authorship adoption or release."

A second predicate, the literal `grants no`, returns **2**: the same line,
and `ARTIFACTS-AND-TOOLS.md` line 15, "verified outside the LLM; putting a
grant-shaped string in JSON grants nothing" — which is about the invalidity
of a self-asserted grant, not about whether the document itself grants
anything. `AUTHORING.md`, the file that carries the six copy-pasteable stage
prompt blocks under its "Stage prompts" heading (line 72), contains **0**
occurrences of either literal.

### The landed validator over `docs/polaris-generation/example.json`

Method: parse the file, build the validator context from its own
`sourceBundle.sources` (one source, `s1`), and call `validateStage` for each
of the six landed stages against each of three payloads — the file's
`illustrativeOutput`, its `illustrativeLaterDraft`, and the whole file.
Denominator: 18 calls, plus one call to `stageSchema` for the stage the file
names.

| Call | Result |
|---|---|
| `stageSchema('understand')` | throws `invalid-stage` |
| all 18 `validateStage` calls | each throws `invalid-fields` |

The cause is structural rather than incidental: `check()` at
`provider-draft.ts` lines 61–63 requires the payload's key set to equal the
schema's `required` exactly, so any object with a field the schema does not
name is rejected before its contents are examined. The file's
`illustrativeOutput` carries `editorialState`, `claims`, `unresolved`,
`assetDispositions` and `coverage` — five keys, none of which appears in the
25-name census.

### Line numbers re-verified at `a9f671e`

**The dossier's stated audit commit does not hold for these two surfaces.**
`docs/pursuits/2026-09-13-vision-pursuit-data.json` records
`"syzygy_audited_at": "f4589e2"`. At `f4589e2` the generation package **did
not exist**: `git diff --numstat f4589e2 a9f671e` over
`packages/polaris-generation-core`, `docs/polaris-generation`, `package.json`
and `apps/three-surface-poc/src/polaris-generation` shows all 22 files added
with 0 deletions, including every file L3 and S9 cite [Observed, this
session]. S9-F1's own evidence names the tree it read — "main @ `1932f74`" —
and `f4589e2` is an ancestor of `1932f74`. The reconciliation is clean: the
same diff restricted to `1932f74..a9f671e` returns **no rows**, so the entire
M6 surface is byte-identical between the commit S9 actually read and this
packet's baseline, and every line citation below is current.

| Citation | At `a9f671e` | Dossier / finding said | Note |
|---|---|---|---|
| `provider-draft.ts` `paragraph` | 18 | 18 | exact |
| `provider-draft.ts` `fidelity` schema | 30–32 | 30 | line 30 is the first of three |
| `provider-draft.ts` shared draft schema | 33 | 33 | exact |
| `provider-draft.ts` `sourceSchema` | 109 | 109 | exact |
| `provider-draft.ts` `else` branch + `reviewVerdict` | 131–152 | 131–152 | exact |
| `prompts.ts` common instruction | 6 | 6 | exact |
| `prompts.ts` `edit` instruction | 18 | 18 | exact |
| `prompts.ts` `repair` instruction | 22 | 22 | exact |
| base spec, "Source-supported inference SHALL expose…" | 52 | 52 | exact; **superseded in force** by overlay line 9 |
| base spec, "The asset bundle SHALL distinguish…" | 98 | 98 | exact; REQ-003 is not amended, so this is the effective text |
| base spec, "record both inventory-to-draft coverage…" | 302 | 302 | exact; **superseded in force** by overlay line 180 |
| base spec, "resolving to one produced, omitted or unresolved disposition" | 1015 | 1015 | exact; **superseded in force** by overlay line 453, whose first two sentences are identical |
| `packages/polaris-generation-core/README.md` demo command | 55 | 55 (prompt), 44–48 (S9-F1) | the command is line 55; S9-F1's 44–48 is the preceding paragraph |
| `AUTHORING.md` diagram promise | 45–46 | 45–49 | the sentence ends at 46 |
| `AUTHORING.md` deep-dive trade-off | 62 | 60–63 | the clause is on 62 |
| `ARTIFACTS-AND-TOOLS.md` glossary sentence | 40 | 40–41 | begins at 40 |

**Four figures that differ from the dossier**, collected: (1) the demo
command succeeds at `a9f671e` after `npm ci`, where the dossier says it
"fails with TS2307 from a fresh checkout"; (2) `syzygy_audited_at` is
`f4589e2`, where the audited tree for L3 and S9 was `1932f74`; (3) S9-F4's
doctrine tag is SEC-1 where the governing rule is SEC-2; (4) M6's Slices list
carries five entries where its What bullet names six moves.

## Gate 2 — Doctrine

**VIS-2 — No evidence means Unknown, not success.** Quoted at the clause,
`.syzygy/governance/doctrine/vision.md` lines 96–106: "No surface may declare
a project aligned, converged, or genome-complete — nor turn anything green —
without current evidence… Until a claim class declares its currency bound,
its evidence is not current and the claim renders Unknown." Slices 2, 3 and 4
are each an application of this rule at a different seam: slice 2 gives a
model with no evidence a way to say so; slice 3 makes the absence of a
verdict block rather than pass; slice 4 makes a deletion reportable. The
violation clause names "a stale view silently green", which is the shape of a
fidelity review that enumerates a denominator and returns no findings.

**VIS-1's ordering is what puts slice 3 above slice 5.** Truth and
observation determinism first, comprehension of the presentation second. A
coverage table that carries verdicts is a truth change; restating the egress
sentence is a comprehension change; both are worth doing and slice 3 is worth
more.

**VIS-3 — Human interpretability is a core tenet.** Lines 108–121: "Every
normative artifact — spec, doctrine, contract — must remain digestible by a
human unfamiliar with the project." The kit is authoring guidance rather than
a normative artifact, so VIS-3 does not bind it directly; the doctrine this
packet reads as reaching the onramp is VIS-1's second-place comprehension
ordering, applied to the product's own operator surface [Inferred — a
reading of VIS-3's scope, stated rather than resolved; the dossier's M6 entry
tags VIS-3 for slice 1 without this qualification].

**VIS-4 — Humans steer the vision; agents shape within it.** Lines 122–140.
This packet drafts; it adopts nothing. Q1's second arm, an amendment through
CC-REV-2, is named precisely because VIS-4's last paragraph puts
"normative data contracts" in the class that "is always human-gated, gate
open or not".

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Lines 141–160. Every slice writes into `packages/**`,
`apps/**`, `docs/**` or `package.json` — the implementation plane. That is a
**worker action against scheduled work**, which is exactly what VIS-5's own
sentence reserves it to: "materialization is exclusively a worker action
against scheduled work." No slice writes into `openspec/**` or `.syzygy/**`,
and no slice edits a bound byte.

**SEC-2 — Portfolio data leaves owner-controlled infrastructure only through
explicit, scoped consent.** `.syzygy/governance/doctrine/security.md` lines
25–37, quoted at the load-bearing sentence: "Governed-project content —
source structure, specs, work history, and anything derived from them,
**including prompts** — is never transmitted to a store or service the owner
does not control without explicit, recorded, per-project consent. **Model
providers are such services.**" Slice 5 restates that boundary at the two
places an operator holds a prompt in their hand. No slice in M6 sends
anything anywhere: the demo's adapters are scripted and synthetic, and
`packages/polaris-generation-core/README.md` lines 38–39 record that the
controller "has no default network client."

**RFC2-24's closed twelve.** If slice 2's `unresolved` disposition ever
surfaces as an Unknown on a rendered page, its reason must be one of
RFC2-24's twelve values verbatim
(`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
line 92: "Every Unknown claim instance carries exactly one primary reason
from this list"). Slice 2 as designed keeps the disposition inside the
provider interchange and does not render it on Polaris, so the constraint is
recorded as a boundary the slice must not cross rather than as a requirement
it must satisfy.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Onramp | `packages/polaris-generation-core/README.md` (one line before line 55); `docs/polaris-generation/README.md` (the "Executable development slice" section, lines 27–33); `package.json` line 15 (`build:poc`'s project list); a new battery assertion beside `poc:fresh-checkout-demo` | none |
| 2 Asset disposition | `packages/polaris-generation-core/src/provider-draft.ts` (the `inventory`, `plan` and `draft` schema declarations, lines 19–29; `validateStage`, 107–146); `packages/polaris-generation-core/src/provider-draft.test.ts`; `apps/three-surface-poc/src/polaris-generation/draft-preview.ts` (render the three dispositions distinctly); `docs/polaris-generation/example.json` (regenerated, per Q4) | **none edited.** The vocabulary is read from `SCHEMA-CONTRACT.md` lines 33–39 and the two effective requirements; Q1 decides whether reading it is conformance or amendment |
| 3 Coverage rows | `provider-draft.ts` (the `fidelity` schema, lines 30–32; `same()` at 86–89 preserved; `reviewVerdict` at 148–152 rewritten, per Q3); `pipeline.ts` line 264's `ports.fidelity(review)` call site, unchanged in shape | none |
| 4 Edit/repair accounting | `provider-draft.ts` line 33 (split `edit` and `repair` out of the shared `draft` entry) and `validateStage`'s `else` branch (131–144, which gains the prior draft); `pipeline.ts` lines 262 and 267 (thread the prior draft into the stage context) | none |
| 5 Boundary restatement | `docs/polaris-generation/AUTHORING.md` (one line above the "Stage prompts" heading, line 72); `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md` (one line above "Per-stage envelope", line 8) | none |
| 6 (deferred) Diagram, deep-dive, glossary | not designed here | not designed here |

Boundaries crossed: none. Every file above is in the implementation plane.
The `openspec/**` and `.syzygy/**` trees are read for authority and written by
no slice.

Not touched by any slice: the six-stage controller's cancellation, deadline,
permit and receipt machinery (`pipeline.ts` lines 1–258), which L3 judged the
strongest part of the package; the canonical JSON encoder and the bounded
parser; the source-admission path, which does not exist yet and is Phase B.

### The authorizing act, per slice

| Slice | Owner act needed | Named act, the task it is filed against, and the trigger test |
|---|---|---|
| 1 Onramp | **No** | Rides `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-12). Filed against unchecked task **3.5**, "Run repository-required checks in a fresh clone of the final implementation, inspect denominators and counterexamples, and report residuals explicitly" (`tasks.md` line 50). No trigger crossed: the act's own reservations name "real-project reads, provider egress and destination writes" and "no effect, production release, broad remote access or observed-project code execution" (line 42); a documentation line, a `tsc -b` project list and a battery assertion are none of those |
| 2 Asset disposition | **No for the field; yes if Q1 is ruled the second way** | Same act. Filed against unchecked task **2.2**, "Implement source understanding, project-specific argument construction and bounded asset generation (002/003/004/005), preserving Unknown and editorial-draft states" (`tasks.md` line 22) — the words "preserving Unknown" are the task this slice performs. On Q1's amendment arm the trigger is a specification amendment, which needs CC-REV-2 and a new owner act |
| 3 Coverage rows | **No**, with one disclosure | Same act. Filed against unchecked task **2.4**, "Implement review invalidation, source regeneration, authored-content coexistence, per-block human acts and rejection (006/009/010/011/016)" (`tasks.md` line 24). The disclosure is Q3: changing the verdict polarity changes when a run reaches `awaiting-rendered-review`, an owner-visible readiness state, so the owner should rule it rather than inherit it |
| 4 Edit/repair accounting | **No** | Same act. Filed against task **2.4** as well, on the clause "The original finding, repair, dispositions and input/output identities SHALL remain traceable" (overlay REQ-006, line 180) |
| 5 Boundary restatement | **No** | Same act. Filed against unchecked task **1.4** only loosely; more exactly it is kit guidance rather than a specification obligation, and it is proposed on SEC-2's authority rather than on a task's |
| 6 (deferred) | not evaluated | not evaluated |

All six slices run under `syzygy-dov.6`, the pursuit bead; no new generator
bead is filed by this packet.

## Gate 4 — Design sketch, per slice

### Slice 1 — The onramp says what to run first, and a check says when it stops working (small; no act)

Three edits and one new assertion.

**The install line.** Immediately above
`packages/polaris-generation-core/README.md` line 55, one sentence naming the
prerequisite state the command needs — a current workspace install at the
repository root — and, in the same breath, the symptom it prevents, so an
operator who hits `TS2307` can recognise it. The same line goes into
`docs/polaris-generation/README.md`'s "Executable development slice" section,
which routes operators to the core README (line 29) without repeating its
command.

**The explicit project list.** `package.json` line 15's `build:poc` gains
`packages/polaris-generation-core` in its `tsc -b --force` list. This changes
no build output today — the package is already built transitively — and
removes the dependence on a single `references` entry in
`apps/three-surface-poc/tsconfig.json`.

**Test.** A battery assertion in the shape of `poc:fresh-checkout-demo`,
which already exists and already exits by a verdict over recorded invariants:
run the README's exact command string from a clean install into a temporary
directory, assert exit 0 and assert the seven expected output files. The
assertion must read the command out of the README rather than restating it,
or the check and the documentation can drift apart — which is exactly the
failure slice 1 exists to prevent.

**Rule-6 mutants.** (a) Move the workspace symlink aside and confirm the new
assertion fails with a message naming the install step, not a bare `TS2307`.
(b) Change the README's command string and confirm the assertion fails
because it no longer matches what it ran. (c) Remove
`packages/polaris-generation-core` from `build:poc` again and confirm the
assertion still passes — it should, since the transitive reference still
works, which records honestly that limb (c) is defence in depth and not a
tested guard.

### Slice 2 — Somewhere to put "I could not support this" (medium; act per Q1)

**The field.** Each of `inventory`, `plan` and `draft` gains a required
per-requested-asset disposition. Sketch:

```
type Disposition =
  | { kind: 'produced'; assetIds: string[] }      // references resolve in the same bundle
  | { kind: 'omitted'; reason: string }           // optional assets only
  | { kind: 'unresolved'; reason: string };       // no output id or digest invented
```

The three arms and their payloads are read from `SCHEMA-CONTRACT.md`
lines 35–39, whose table gives each disposition a "Required payload" and an
"Invariant" column: Produced — "References to one or more validated output
assets", invariant "Every reference resolves in the same bundle; produced
does not mean reviewed, adopted or acceptable"; Omitted — "Reviewable reason
and supporting disposition reference", invariant "Only optional assets whose
omission preserves every reading obligation; not a substitute for
unavailable capability"; Unresolved — "Missing support, permission,
capability or failed-validation reason, with the relevant references",
invariant "No output digest or asset is invented; the affected readiness
obligation stays unmet".

**Where it attaches.** On `plan`, one disposition per requested asset,
keyed by the request's own identity. On `draft`, one per `diagrams[]` and
`deepDives[]` entry, plus a draft-level `unresolved: { question, reason }[]`
for material the plan asked for and the sources could not support. On
`inventory`, the "relevance or justified omission disposition" the inventory
prompt already asks for at `prompts.ts` line 10.

**Validation.** `validateStage` gains one check per stage: the set of
disposition keys must equal the set of requested-asset ids in the context,
using the same `same()` function the fidelity stage already uses — so the
denominator is the request's, not the model's. A `produced` disposition whose
`assetIds` do not all resolve in the returned draft is `unknown-asset`, in
the shape of the existing `unknown-source` and `unknown-node` errors.

**Rendering.** The draft preview renderer,
`apps/three-surface-poc/src/polaris-generation/draft-preview.ts`,
already refuses an unresolved section, node or source rather than omitting
it, and already draws "No relationship supplied" over an unconnected node.
The three dispositions render in that vocabulary rather than an invented one:
an `unresolved` asset appears as a visible absence with its reason, never as
a missing element.

**Oracle.** Independently written fixtures: one plan requesting three assets
of which the sources support one, with the expected disposition set written
by hand in the test and never imported from the module under test (AGENTS.md:
"Conformance expected values are hard-coded literals").

**Rule-6 mutants.** (a) Drop one disposition row from a valid fixture and
confirm validation throws; mutate the `same()` call to a subset check and
confirm the test fails. (b) Give an `unresolved` disposition an `assetIds`
array and confirm the schema rejects it on the key-set check at lines 61–63.
(c) Point a `produced` disposition at an id no asset carries and confirm
`unknown-asset`. (d) Regenerate `example.json` from a real `validateStage`
call, then mutate one byte of it and confirm the new "the shipped example
validates" test fails.

**Trade-offs rejected.** Making the disposition optional with a default of
`produced` (that is silence-means-success, the exact polarity VIS-2 forbids);
putting it on the output asset rather than the request (SCHEMA-CONTRACT.md
lines 26–31 keep requested and output assets as different records, and
"Requiredness cannot be downgraded by provider output"); inventing a fourth
value for "not applicable" (the bound table is three rows and closed).

### Slice 3 — A coverage table that carries verdicts, and a verdict that is a function of the denominator (medium; no act; Q3 rules the polarity)

**The shape.** Both `inventoryIds` and `blockIds` stop being bare handle
arrays and become rows:

```
inventoryCoverage: {
  entryId: handle;
  disposition: 'represented' | 'justified-omission' | 'unsupported' | 'unresolved';
  blockIds: handle[];        // empty only for the two non-represented arms
  reason: string;            // required when disposition is not 'represented'
}[];
blockSupport: {
  blockId: handle;
  verdict: 'supported' | 'anchor-does-not-support' | 'unresolved';
  sourceIds: handle[];
  reason: string;
}[];
```

**The denominator is preserved exactly as it is today.** `same()` still runs,
now over the row keys: `inventoryCoverage[].entryId` must equal the
inventory's entry id set, and `blockSupport[].blockId` must equal
`draftHandles(context.draft).blocks`. A missing row is `incomplete-coverage`,
the error that exists today — so the change adds verdicts without weakening
the one mechanical honesty the package already has.

**The verdict (Q3).** On the recommended arm, `reviewVerdict` blocks when any
`inventoryCoverage` row is not `represented` or `justified-omission`, when
any `blockSupport` row is not `supported`, or when any row is absent — and
the severity-only path is deleted. On Q3's second arm the rows are added and
`reviewVerdict` is left as it is; the packet's disclosure in that case is
that readiness still passes on silence.

**What this gives the spec's own named scenario a field to live in.** The
effective REQ-polaris-generation-006 carries a scenario, quoted verbatim from
`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
lines 199–203, the whole scenario:

> #### Scenario: Source trade-off omitted entirely
>
> - **WHEN** all generated claims have anchors but an independently
>   inventoried material trade-off is absent from the account
> - **THEN** source-to-draft coverage records the omission as a blocking
>   finding
> - **AND** an author-generated outline or claim list cannot replace the
>   independent source inventory

Today the only way to record that omission is a free-text finding with
`target: 'entry-7'`, and `findings` may be empty. After slice 3 the entry's
own row carries `unsupported` with a reason, and on the recommended arm that
row blocks.

**Oracle.** Three independently written fixtures: a review with every row
present and all positive (passes); a review with every row present and one
`unsupported` (blocks); a review missing one row (invalid output, not a
pass). The expected outcomes are literals in the test.

**Rule-6 mutants.** Mutate each of the three predicates separately — the row
completeness check, the inventory-disposition test and the block-verdict
test — and confirm the corresponding fixture fails; mutate `same()` to a
subset check and confirm the missing-row fixture stops failing, which is the
counterexample that proves the check is load-bearing.

### Slice 4 — An edit that cannot delete in silence (medium; no act)

**The split.** `provider-draft.ts` line 33 stops mapping `edit` and `repair`
to the shared `draft` object. `edit` returns a draft **plus** a changed-block
account; `repair` returns a draft plus a changed-block account **plus** a
finding-to-change disposition:

```
changes: { blockId: handle; action: 'kept' | 'rewritten' | 'split' | 'removed';
           reason: string; newBlockIds: handle[] }[];
findingDispositions: { findingId: handle; action: 'repaired' | 'unrepairable';
                       reason: string; affectedBlockIds: handle[] }[];
```

**The prior draft enters validation.** `pipeline.ts` lines 262 and 267 pass
the prior draft into the stage context, and `validateStage`'s `else` branch
gains, for these two stages only, a `same()` over `changes[].blockId` against
`draftHandles(priorDraft).blocks` — total coverage of the input's blocks,
the same discipline the fidelity stage already applies to its own two
populations. For `repair`, a second `same()` over the `findingId` of every
`findingDispositions` row, against the findings the pipeline supplied at
line 267.

**Why total coverage and not a diff.** A diff would be computed by the
trusted side and would tell the model nothing; the point is that the model
must *account* for each block, because the account is what a reviewer reads.
A `kept` action costs one row and is the honest default.

**The prompts already ask for exactly these fields**, which is the argument
that this is conformance rather than invention: `prompts.ts` line 18, "report
changed content and affected references using the supplied schema", and line
22, "Return the schema's affected content and finding-to-change
dispositions". The kit's own run contract names them too: "Concise, coherent
revision plus change list" and "Bounded replacement artifacts"
(`docs/polaris-generation/README.md` lines 65 and 67).

**One design question this slice does not settle.** L3-M3 proposes
additionally relaxing the plan pin at `provider-draft.ts` line 137 so a
repair may emit a plan revision and re-enter the plan stage. That is a
control-flow change to the six-stage pipeline rather than a schema change,
and this packet leaves it out of slice 4 rather than smuggling it in
[Inferred — a scoping judgment, not a lawfulness claim].

**Oracle and rule-6 mutants.** A fixture edit output that omits one prior
block id must be `invalid-output`; mutate the coverage check to a subset test
and confirm that fixture stops failing. A repair that returns its input
unchanged with every finding marked `unrepairable` must validate and must be
visibly distinguishable in the receipts from one that repaired — which is the
honest outcome, not a failure.

### Slice 5 — The boundary restated where an operator acts on it (small; no act)

Two lines. One directly above `docs/polaris-generation/AUTHORING.md`'s "Stage
prompts" heading (line 72), the section that holds six copy-pasteable prompt
blocks; one directly above `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`'s
"Per-stage envelope" heading (line 8), the section describing how to build
the request that would accompany a provider call. Each restates
`README.md` line 4's sentence and names SEC-2 as its source, so a reader can
follow it rather than take it on the kit's word.

**Test.** A literal assertion that the sentence occurs in all three kit
prose files, in the shape of the existing copy oracles — with the caution
AGENTS.md records about those: a very short label is "reached" by
coincidence, so the assertion matches a distinctive full clause, not the word
`egress`.

### Slice 6 (deferred) — The diagram, deep-dive and glossary promise gap

Not designed here. It is named in M6's What bullet, absent from M6's Slices
list, and its mapping is done in Gate 5 so the gap is recorded. It needs a
decision this packet has not made: whether to extend the schema to the fields
`AUTHORING.md` promises, or to trim the prose to what the schema carries.
S9-M3 recommends extending, on the pursuit posture's waiver of backward
compatibility inside the POC surface; that waiver does not reach
`ASSET-CONTRACT.md`, which is bound and defines the Glossary kind's fields at
line 37. Re-enter this funnel once slice 2 has landed, because the
disposition field is the thing every new asset kind would need first.

### Design bar for the human surface

Only slice 2 reaches a rendered surface, through
`apps/three-surface-poc/src/polaris-generation/draft-preview.ts`. The bar
there: an `unresolved` asset must read as a visible, explained absence at the
place the asset would have been — never a footnote, never a missing element,
never a page-wide disclaimer. That is the same treatment the PWB renderer
already gives an Unknown, and the slice copies its vocabulary rather than
inventing one (AGENTS.md's own caution about a second encoding for the same
meaning).

## Gate 5 — Specification

The specification in force is the predecessor composed with the
understanding-amendment overlay, effective composition **31 requirements and
177 scenarios** (understanding act, Scope paragraph). Requirements 002, 004,
006, 009, 012, 014 and 019 are cited at the overlay; all others at the
predecessor.

### Does `disposition` need a spec delta? (Q1)

**No, on the recommended arm, and the argument is a quotation rather than a
reading.** Three bound artifacts name the field:

`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
line 453, the requirement text of REQ-polaris-generation-019 — the cited line
is the requirement's normative paragraph, which begins after that
requirement's own heading at line 451 — quoted at its second sentence:

> Each requested asset SHALL have its own identity, kind, requiredness and
> purpose, resolving to one produced, omitted or unresolved disposition;
> produced SHALL reference actual matching assets while unresolved SHALL NOT
> fabricate output identities or digests.

The same sentence stands verbatim in the predecessor at base line 1015; the
overlay's amendment to REQ-019 adds a scenario ("Research projection cannot
mint authority", overlay lines 501–505) and leaves this sentence untouched
[Observed, the two paragraphs compared this session; they diverge only later
in the paragraph].

The same overlay, line 78, the requirement text of
REQ-polaris-generation-004, quoted at the relevant sentence and the two that
bound it:

> Every requested asset SHALL have an explicit produced, reasoned-omission or
> unresolved disposition. An asset required by the request, reading
> obligation or frozen acceptance criteria SHALL remain unmet when support,
> permission or renderer capability is unavailable. Optional omission SHALL
> NOT excuse an unmet reading-depth obligation; silent omission, decorative
> approximation or an unapproved textual substitute SHALL NOT discharge a
> required asset.

And `openspec/changes/polaris-manifesto-generation/SCHEMA-CONTRACT.md` lines
33–39, which is the table quoted field-for-field in slice 2 above, under the
heading "Requested assets and output assets are different records" (line 26).

**The residue, and it is a genuine owner question.** Those three sources give
the enum three *different* spellings — `omitted` (REQ-019 and
SCHEMA-CONTRACT.md), `reasoned-omission` (REQ-004), and the kit's
`unnecessary-with-reason` (AUTHORING.md line 102, ARTIFACTS-AND-TOOLS.md
line 43) — plus the plan prompt's `planned` where the others say `produced`
(`AUTHORING.md` line 102). The first three are bound bytes and none may be
edited to agree. Whichever literal lands in the executable schema will
disagree with at least one bound artifact, and this packet does not choose
for the owner. It notes only that the kit files are *not* bound and can be
brought into line with whatever is chosen.

### The RFC2-26 test, run over all six slice rows

RFC-0002 is an accepted design contract in force. Its phase rule is quoted
verbatim at the defined clause,
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 196–221, under the `###` heading "Authority boundary at the OpenSpec
seam (binding phase rule)" at line 194 — **the whole clause, both
paragraphs**, with no elision:

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
> state rendered;
> absent or invalid acts map nothing and leave the consequence unmapped and
> Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2).
>
> **Rows are per observable consequence, not per clause.** A clause with
> five
> observable consequences and one mapped requirement is not covered; the
> matrix
> discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of
> the
> matrix. At surface specification a clause-to-requirement coverage matrix
> over RFC2-1..RFC2-26 is produced — **that matrix is review material, never
> authority**. This clause creates no OpenSpec content now (none may exist
> during bootstrap). This clause binds the whole RFC 0002 package, not this
> module alone. (Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52,
> RFC10-16, RFC11-12.)

**The denominator is six**: the six slice rows of Gate 3's "The authorizing
act, per slice" table, slices 1 through 6 [Observed, counted this session
over that table]. The test is run over all six. Every requirement and
scenario cited below was read at source this session, in the composed
specification.

| Slice | RFC2-26 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Onramp | **None enumerated.** A documentation line, a `tsc -b` project list and a battery assertion render nothing and answer no query over epistemic state; no class in the clause's list fits | n/a | n/a. The clause is not engaged. Slice 1 is filed against unchecked task 3.5 and schedules from the generator's own adopted specification, not from RFC-0002 |
| 2 Asset disposition | "Unknown-reason and rendering-tier presentation" (the disposition is rendered by `draft-preview.ts`); "API answers over epistemic state" (the disposition is a field of the interchange) | **REQ-polaris-generation-019**, overlay line 453, scenario **"Two requested diagrams have different obligations"** at overlay lines 465–469, quoted verbatim: "**WHEN** one required computed diagram and one optional editorial diagram are requested and only the editorial diagram is produced / **THEN** separate request identities retain their own dispositions and the required computed request stays unresolved without a fabricated output digest / **AND** duplicate kind labels or produced optional content cannot discharge that required request". Also **REQ-polaris-generation-004**, overlay line 78, scenario **"Required visual unavailable"** at overlay lines 103–107; and **REQ-polaris-generation-003**, base line 98, scenario **"Computed output has no enabled production renderer"** at base lines 159–163, whose THEN reads "its disposition is unresolved with the unsupported renderer identified, and required computed output keeps readiness unmet" | **Available**, on three independent requirement-and-scenario pairs |
| 3 Coverage rows | "claim and challenge rendering"; "API answers over epistemic state" | **REQ-polaris-generation-006**, overlay line 180, scenario **"Source trade-off omitted entirely"** at overlay lines 199–203, quoted in full in slice 3 above. The requirement text is the closer match still: "It SHALL record both inventory-to-draft coverage and draft-to-source support, including justified omissions; unresolved material omissions SHALL prevent readiness" | **Available.** The scenario's THEN names a *blocking finding*, which is what Q3's recommended arm makes mechanically achievable and Q3's second arm leaves to model goodwill — a difference the owner should see when ruling Q3 |
| 4 Edit/repair accounting | **None enumerated with confidence.** The change lists are interchange fields; whether they are "API answers over epistemic state" depends on whether an account of what an editor changed is an epistemic state, which this packet does not decide [Inferred] | **REQ-polaris-generation-006**, overlay line 180, on the clause "The original finding, repair, dispositions and input/output identities SHALL remain traceable"; nearest scenarios **"Omitted material qualification"** at overlay lines 205–212 and **"New evidence outside the current budget or authority"** at 214–220. **Neither scenario names a silent deletion by the edit stage**, which is slice 4's actual subject [Observed: every scenario heading under REQ-006 was read this session — five, at overlay lines 187, 193, 199, 205 and 214 — and none states the edit-stage case] | **Requirement available, scenario partial.** The clause's bar is "an approved OpenSpec requirement **and** scenario". This packet does not call slice 4 lawful or unlawful on that; it puts the reading to the owner in Q6, and records that the honest repair route if the owner reads the bar strictly is a scenario added through CC-REV-2 |
| 5 Boundary restatement | **None enumerated.** Two sentences in two unbound kit files; nothing rendered, nothing queried | n/a | n/a. Argued from SEC-2 directly |
| 6 (deferred) Diagram, deep-dive, glossary | **[Unknown].** Not designed, so its observable consequences are not enumerated and the test cannot honestly be run over it | The mapping that *would* apply, recorded so the deferral does not lose it: **REQ-polaris-generation-003**, base line 98 ("The versioned bundle SHALL distinguish narrative sections, contents, glossary, comparison tables, curated relationship diagrams and computed visual references"), scenario **"Editorial relationship diagram"** at base lines 117–121, whose THEN requires "the supported relationships, per-element anchors or non-normative/proposed markings, faithful legend and editorial-draft provenance"; and **REQ-polaris-generation-004**, overlay line 78 ("Glossaries SHALL explain concepts where needed for comprehension"), scenario **"No supported optional asset"** at overlay lines 91–95 | Deferred, not run |

**What the test establishes and what it does not.** It establishes
[Observed] that slices 2 and 3 map to named requirement-and-scenario pairs in
the adopted specification, that slice 4's requirement is named and its
scenario is not, and that slices 1 and 5 enumerate no consequence of
RFC-0002 at all. It does not establish that any slice is lawful: that is
Q6's, and RFC2-26's own scope sentence — "This clause binds the whole RFC
0002 package, not this module alone" (line 221) — is a reading the owner may
take more or less broadly than this packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed spec text and nothing here amends a requirement.

**S1 (slice 1).** WHEN the README's exact command chain is run from a clean
workspace install at the repository root, THEN it exits 0 and writes the
seven expected files, AND the assertion that checks this reads the command
string out of the README rather than restating it.

**S2 (slice 1).** WHEN the workspace symlink for the generation package is
absent, THEN the battery assertion fails with a message naming the install
step, AND a bare `TS2307` alone is not an acceptable failure message.

**S3 (slice 2).** WHEN a plan requests three assets and the admitted sources
support one, THEN the plan's disposition set has exactly three rows keyed to
the three request ids, one `produced` and two carrying a reason, AND a plan
returning two rows is `incomplete-coverage`, not a pass.

**S4 (slice 2).** WHEN a disposition is `unresolved`, THEN the draft preview
renders a visible absence with its reason at the asset's place, AND no output
identity or digest is present on that row.

**S5 (slice 3).** WHEN a fidelity review returns a row for every inventory
entry and every draft block, all positive, THEN the run proceeds, AND WHEN
one inventory row reads `unsupported`, THEN readiness is blocked (Q3's
recommended arm) or the row is recorded and readiness is unchanged (Q3's
second arm), and which of the two applies is stated in the bead.

**S6 (slice 3).** WHEN a fidelity review omits one row of either population,
THEN the output is invalid, AND it is not treated as a pass with a smaller
denominator.

**S7 (slice 4).** WHEN an edit returns a draft, THEN its change account
covers every block id of the prior draft exactly once, AND an account missing
one id is `invalid-output`.

**S8 (slice 4).** WHEN a repair is given three findings, THEN it returns a
disposition for each, AND a repair that returns its input unchanged with
three `unrepairable` dispositions is valid and is distinguishable in the
receipts from one that repaired.

**S9 (slice 5).** WHEN either authoring file is read from its prompt or
envelope section, THEN the egress boundary sentence is present in that
section, AND the assertion that checks this matches a distinctive full clause
rather than a single word.

## Collision and sequencing

**The file-set intersection with every sibling packet is zero.** Method:
extract every code span from each sibling packet, keep those that are
implementation-plane paths (`apps/`, `packages/`, `scripts/`,
`docs/polaris-generation/`, or `package.json`) and that resolve as a real
file in this worktree; intersect with M6's own 23-file candidate surface
(everything under `packages/polaris-generation-core/src`,
`apps/three-surface-poc/src/polaris-generation`, `docs/polaris-generation`,
plus `packages/polaris-generation-core/README.md` and `package.json`).

| Sibling | Their resolving implementation paths | Intersection with M6's 23 |
|---|---:|---:|
| M1 (lane A, on main) | 3 | **0** |
| M2, PR #36, P-69 | 17 | **0** |
| M3, PR #37, P-70 | 15 | **0** |
| M4, PR #38, P-71 | 26 | **0** |
| M5, PR #39, P-72 | 11 | **0** |
| lane B, PR #35, P-68 | 3 | **0** |

**Two near-misses, named rather than hidden.** M4 cites
`apps/three-surface-poc/src/polaris-generation/` and M5 cites
`packages/polaris-generation-core/` — both as code spans, both inside a
*baseline-provenance* paragraph establishing what changed between `f4589e2`
and `a9f671e`, and neither proposes touching a file inside them (M5's says in
terms "none of the files this packet cites") [Observed, both paragraphs read
at source this session]. So the directories are named by two siblings and the
files are claimed by none.

**The shared files are governance, not code.** All four sibling packets add a
row to `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. **This
packet writes no register row** — it writes exactly two files — so its six
owner questions are, as of this commit, unregistered. That is a disclosure,
not a design: an owner reading the pending queue will not find Q1–Q6 there,
and whoever lands this packet should file them.

**Lane B edits `scripts/check_governance.py`.** M6 does not, but M6's two
files must pass it, and lane B's branch changes it. The order that avoids a
surprise is: lane B lands, then this packet's check is re-run before merge.
At this commit the check passes in this worktree (Gate 6).

**Sequencing inside M6.** Slice 1 and slice 5 are independent of everything
and of each other; either may land first. Slice 2 must precede slice 6, since
every new asset kind needs the disposition field first. Slice 3 is
independent of slice 2 but reads better after it, because a coverage row
whose subject has a disposition is easier to reason about than one whose
subject does not. Slice 4 is independent of both. Q1 gates slices 2 and 4's
schema work on its second arm; Q3 gates only slice 3's polarity, not its
rows.

**Not verifiable this session.** [Unknown] Whether the sibling branches'
actual diffs stay inside the paths their packets cite, until they land.
[Unknown] Which arm the owner takes on Q1, and therefore whether slices 2, 3
and 4 are one change or a change plus an amendment. [Unknown] Whether the
disposition literal the owner chooses will be `omitted`, `reasoned-omission`
or something else; all three bound spellings are in force simultaneously.

## Gate 6 — Engineering bar

1. **Every count in this packet carries its predicate and its denominator**,
   and every one was taken this session in the worktree at `a9f671e`. The
   field census is computed from the built schema objects rather than read
   off the source, and the literal sweeps that corroborate it were run with
   Python `re` rather than `grep`, per verification rule 1.
2. **Two methods for the load-bearing zero.** "No field can hold a
   disposition" is established both by the computed 25-name census and by the
   literal sweep for `disposition|unresolved|unnecessary` over
   `provider-draft.ts` and `pipeline.ts`; the two agree (rule 2).
3. **The demo's failure mode was established by counterexample, both
   directions**, not by observing one failure: symlink absent → 42 errors;
   symlink restored → exit 0; and the restoration was verified (rule 6).
4. **Rule-6 mutants are specified per slice and per guard branch**, above;
   each names the predicate to mutate and the fixture that must then fail.
5. **Conformance expected values are literals in the tests**, never imported
   from the module under test (AGENTS.md).
6. **The copy oracle caution is applied**: slice 5's assertion matches a
   distinctive full clause, because a short literal is reached by coincidence.
7. **`npm run poc:generator-demo` writes only under the scratch directory**
   in every run this session, never the README's own suggested output path
   under the system temporary directory. In the worktree, `git status` with
   `--short` is clean of everything but this packet's two files.
8. **No bound byte is proposed for edit.** Every file in Gate 0's package-
   contracts row is a row of the adopted offer's 21-file set, and no slice
   touches one.
9. **Independent review.** This packet has had none. It is a first draft and
   should be reviewed in fresh context against the artifact, its governing
   references and the acceptance criteria, with the raw retained under
   docs/reviews/ as R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-RAW.md — named
   without a code span, because CG-1b requires every code-span path to
   resolve and this one does not exist yet.
10. **Rule 10 applies to this file.** Any later edit retires a review bound
    to these bytes; superseded wording is marked and dated in place, never
    deleted.
11. **Conventions this packet was checked against, this session.** Every
    non-fence line has an even backtick count, so no code span is broken
    across a line break (0 of 1,073 non-fence lines). Two lines exceed
    78 columns outside fences, tables and headings, and each is a single
    unbreakable code-span path. Of 261 distinct code spans, 10 contain a `/`
    and do not
    resolve as a path in this worktree; each is enumerated and is not a
    path: five write-root globs (`.syzygy/**`, `openspec/**`, `apps/**`,
    `packages/**`, `docs/**`), two TypeScript error-message literals, the
    RFC2-26 quotation's own bare `decisions/`, two build-output references
    under the generation package (`dist/` and `dist/provider-draft.js`). The
    not-yet-written path of this packet's first review is deliberately not a
    code span, so CG-1b does not see it. No observed-
    repository path is backticked anywhere in this file, and no act argument
    or signed digest is reproduced — the two digest records consulted are
    cited by path, per CG-7e and CG-15.

## Funnel summary

```
## Feature Request: M6 - Generator honesty contract and kit onramp
Size: small (slices 1, 5) / medium (slices 2, 3, 4) / large (deferred slice 6)
Baseline: Syzygy a9f671e; M6 surface byte-identical to 1932f74; the dossier's syzygy_audited_at f4589e2 predates the whole generation package
- G1 Motif: the kit's flagship honesty claim does not exist in the code it points to - 25 distinct schema field names across six stage schemas, 0 able to hold a disposition or an unresolved state, 2 enums neither of them epistemic, against 5 prompt instructions directing the model to use a schema representation that is absent; the fidelity coverage declaration is two whole-population id lists with 0 per-entry verdicts and findings minItems 0, so silence passes; author/edit/repair share one byte-equal schema object so an edit can delete a supported claim and the next review's denominator is recomputed from the shrunken draft; the kit's example.json fails the landed validator 19 times out of 19 [Observed, all measured this session with predicates and denominators stated]
- G2 Doctrine: VIS-2 at three seams (disposition, verdict polarity, edit accounting), VIS-1's ordering putting slice 3 above slice 5, VIS-4 (this packet drafts and adopts nothing), VIS-5 (implementation plane only, worker action), SEC-2 for slice 5 - NOT SEC-1, which is the finding's tag and is about endpoint authentication
- G3 Topology: packages/polaris-generation-core + apps/three-surface-poc/src/polaris-generation + docs/polaris-generation + package.json; no boundary crossed; no governed artifact touched; every slice filed against an unchecked tasks.md task (24 boxes, 24 unchecked, counted this session)
- G4 Design: a three-value asset disposition read field-for-field out of SCHEMA-CONTRACT.md lines 33-39; fidelity coverage as rows carrying verdicts with the existing set-equality denominator preserved; edit and repair split out of the shared draft schema with total prior-block coverage; an install line plus a battery assertion that reads the command out of the README; the egress sentence restated at the two acting points
- G5 Spec: no delta needed for the disposition field on the recommended arm - three bound artifacts already name it - but the three bound artifacts spell the enum three different ways and none may be edited to agree, which is Q1. RFC2-26 run over all six slice rows (denominator 6): slices 2 and 3 map to named requirement-and-scenario pairs; slice 4's requirement is named and no scenario states its case; slices 1 and 5 enumerate no RFC-0002 consequence; slice 6 deferred and not run
- G6 Bar: computed census plus corroborating literal sweep for the load-bearing zero; the demo failure established by counterexample in both directions; rule-6 mutants per slice; no bound byte proposed for edit; NO independent review yet - this is a first draft
Acts: all five slices ride POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md (2026-09-12), whose grant is quoted in Q6 and covers the full EXECUTION-PHASES.md goal; all five sit in Phase A; no new act needed on the recommended arms; Q1's second arm would need CC-REV-2 and a new act
Open questions: Q1-Q6 above. NOT registered in PENDING-OWNER-DECISIONS.md - this packet writes two files and no register row, unlike its four siblings (P-68 lane B, P-69 M2, P-70 M3, P-71 M4, P-72 M5)
Sign-off: pending - the owner's
Recommended handoff: land slices 1 and 5 now (no gate, no schema); rule Q1; then slice 2, then slice 3 with Q3's polarity ruled, then slice 4; defer slice 6 behind slice 2
```

## Recommended handoff

**If Q1 is answered as recommended:** file no new bead. Build slices 1 and 5
first, under `syzygy-dov.6` — neither needs a schema decision, neither
enumerates an RFC-0002 consequence, and together they cost a few lines and
one battery assertion. Then slice 2, which is the change the rest of M6 rests
on: it is the one that gives a model with no evidence a schema-conformant way
to say so, and the one whose absence makes the kit's central promise false in
the code the kit points to.

**If Q1 is answered the other way** — that adding the field is an amendment —
then slices 2, 3 and 4 hold behind a CC-REV-2 delta and a new owner act, and
slices 1 and 5 proceed regardless. That is a coherent outcome and should be
written down as one: the reason it is coherent is the enum-spelling residue,
which means *any* implementation of the field will contradict a bound
artifact, and an owner may prefer to settle that in the specification rather
than in code.

**If Q3 is answered as recommended:** slice 3 lands the rows *and* the
polarity change together, and the bead records that runs which pass today
will stop passing — including the shipped synthetic demo, which should be
re-run and its output inspected before the slice is called done. If the owner
takes the second arm, land the rows alone and record, in the bead's close
reason, that readiness still passes on silence — so the next person to open
this does not mistake a visible table for a binding one.

**If Q2 is answered as recommended:** the support discriminant is deferred
and this packet's record of the open hole stands: a paragraph's `[1]` marker
means only that a source with that id exists, and nothing in the package
compares a claim's text to the source it cites. That is the largest remaining
honesty gap in the generator after M6, and it deserves its own funnel rather
than a corner of slice 2.

**If Q4 is answered as recommended:** regenerate `example.json` from a real
`validateStage` call and add the test that asserts it validates, keeping a
clearly separated illustrative block for the understanding stage the pipeline
does not yet have. If the owner takes the one-sentence arm instead, the
sentence must say which half of the file is executable and which is
illustration — the defect is the kit's routing, not the file's honesty.

**If Q5 is answered as recommended:** the install line, the explicit
`build:poc` entry and the battery assertion land as one change. If the owner
declines the assertion, land the other two and record that the recurrence
guard is absent — this class of break is silent, and the only thing that
caught it last time was an auditing agent reading the package cold.

**If Q6 is answered the other way** — that slices 2 and 3 need a fresh
direction naming them, because they change what an owner sees at the
readiness gate — then hold those two and land 1, 4 and 5. Slice 4 is the one
that carries no rendered consequence at all and the one whose requirement is
named in the effective REQ-polaris-generation-006; it is the least gated of
the three schema slices, and it closes the hole that makes a deletion
unreportable rather than merely unreported.
