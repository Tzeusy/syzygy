# Semantic delta POLARIS-EDIT-REPAIR-1 — the generator's edit and repair stages must account for every dropped block

> **Candidate — binds nothing.** Drafted for bead `syzygy-dov.23`, "Gate:
> CC-REV-2 scenario for the generator edit-stage deletion (P-73 slice 4) —
> draft, sign-off," per the owner direction below. Nothing in this package
> is applied to `openspec/` or `PROJECT-STATUS.md` — the proposed changes
> live only as `.patch` files under `proposed/`, hashed post-apply in
> `POLARIS-EDIT-REPAIR-DELETION-SCENARIO-MANIFEST.txt`, and the real tree is
> touched only by `scripts/build_polaris_edit_repair_deletion_scenario.py
> --apply --at-adoption`, run inside the change that performs the owner act.

## Owner warrant, quoted verbatim

From `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
(dated 2026-09-21), the P-73 row:

> **P-73** (M6) | **A** — Q1 implementation; Q2 defer the support
> discriminant; Q3 fail closed; Q4 regenerate the example with a separated
> illustrative block; Q5 install line plus fresh-install battery assertion in
> `build:poc`; Q6 the generator implementation act covers slices 1, 2, 3, 5;
> slice 4 once its CC-REV-2 scenario for the edit-stage deletion is signed
> off. | Slices 1, 2, 3, 5 under
> `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`, implementation-plane
> files only; no schema, prompt or kit file inside a bound package is edited;
> no provider egress or new source read. **This record is the direction
> naming slice 4**: it proceeds only after that scenario is signed off
> (drafting may start at once and binds nothing). | Ready `.6.1`, `.6.2`;
> blocked `.6.3` on gate `.23`.

Bead `syzygy-dov.23` restates this directly: "The scenario may be drafted at
once; drafting binds nothing." [Observed] Bead `syzygy-dov.6.3` ("M6 slice
4: edit-stage deletion") depends on `syzygy-dov.23` and is otherwise blocked.

## What CC-REV-2 requires of this package

`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:52`,
CC-REV-2 "The same-logical-change rule":

> A change that invalidates any authoritative artifact updates **every**
> invalidated authoritative artifact in the same logical change: behavioral
> specs (`openspec/`), declared topology, accepted contracts, and the
> policies in this cluster. … The rule is a **merge invariant, not a
> property of how work is packaged**: no merge may leave mainline with an
> invalidated authoritative artifact still asserting the old truth.

This package's spec patch invalidates one descriptive, non-authoritative
sentence outside `openspec/`: `PROJECT-STATUS.md`'s scenario-count claim.
Per CC-REV-2's own scope ("behavioral specs, declared topology, accepted
contracts, and the policies in this cluster"), `PROJECT-STATUS.md` is not
itself one of the four named authoritative classes — but AGENTS.md's own
"Governance prose and docs" guardrail says a page that repeats a fact it
does not own "goes stale silently," and the same landing pass that adds a
178th scenario is the natural place to keep that repeated count honest
rather than opening a second logical change for one digit. Both files are
therefore PATCHED together in this one package, so no merge of this change
can leave either the spec or `PROJECT-STATUS.md` "still asserting the old
truth" in [Inferred] alignment with CC-REV-2's intent, even though only the
spec file is authoritative in CC-REV-2's own sense.

## Evidence basis for the requirement gap

`docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md` (candidate — binds
nothing; bead `syzygy-dov.6`, dated 2026-09-15) Gate 5 already ran this
exact RFC2-26 test for slice 4 and recorded, at its line naming the
requirement:

> **Requirement available, scenario partial** — REQ-polaris-generation-006
> (overlay line 180) is named, but neither scenario names a silent deletion
> by the edit stage, which is slice 4's actual subject [Observed: every
> scenario heading under REQ-006 was read this session — five, at overlay
> lines 187, 193, 199, 205 and 214 — and none states the edit-stage case].

[Observed, re-verified this session at the file's current lines, which have
not moved since that finding]: `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
carries `### Requirement: Independent review and repair` at line 178,
`ID: REQ-polaris-generation-006` at line 182, and exactly five
`#### Scenario:` headings under it — "Meaningful rendered review" (187),
"Revision after confirmation" (193), "Source trade-off omitted entirely"
(199), "Omitted material qualification" (205), "New evidence outside the
current budget or authority" (214) — before `Form: lifecycle transition.`
at line 222. None of the five names an edit or repair stage dropping a
prior block. This is the RFC2-26 gap this package closes: RFC2-26 requires
"every observable consequence either maps to an approved OpenSpec
requirement and scenario … or carries a reviewed N/A judgment," and the M6
funnel doc's own Q6 analysis concluded the N/A route is unlikely to be
reachable here ("an account of what an edit changed is independently
testable") — so a CC-REV-2 scenario, not an N/A judgment, is the intended
route, matching what P-73 Q6 asked for.

[Observed, re-verified this session independently of the funnel doc] The
code-level gap the scenario targets, read directly:

- `packages/polaris-generation-core/src/provider-draft.ts` line 45:
  `const schemas: Record<GenerationStage, Schema> = { inventory, plan,
  author: draft, edit: draft, repair: draft, fidelity };` — `author`,
  `edit` and `repair` share one byte-identical `draft` schema; there is no
  `changes`/`findingDispositions` field a stage could even populate.
- `validateStage`'s `else` branch (lines 143-156) covers `author`/`edit`/
  `repair` identically and never reads `context.draft` (the prior draft):
  a literal sweep of the file for `context.draft` returns exactly 2 hits,
  both inside the separate `fidelity` branch.
- `packages/polaris-generation-core/src/pipeline.ts` lines 314-320:
  `context.draft = await stage('author', context); context.draft = await
  stage('edit', context); … context.draft = await stage('repair', {
  ...context, findings: verdict.findings });` — each stage's output
  unconditionally replaces `context.draft`; nothing diffs the new value
  against the old one or records what changed.
- `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` line 66:
  `const responses = { inventory, plan, author: draft, edit: draft,
  fidelity: review, repair: draft };` — the one hit for "edit" in the app's
  `polaris-generation` directory outside test files is this demo-harness
  fixture, which reuses the identical `draft` schema for `edit` as for
  `author`; there is no separate app-level accounting logic to inspect.

None of this code is touched by this package — only the specification text
is proposed for amendment here. Implementation (giving `edit`/`repair` a
distinct schema and wiring the pipeline to diff against the prior draft) is
a separate, later-gated act under P-73's Q6 authorization, once this
scenario is signed off.

## Current meaning (verbatim, with line numbers)

`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`,
current (pre-patch) sha256 `b7c95f57ca5f67a18570b7124d20b223dff99aea2a936efef76d5940a400f93f`
(computed this session via `sha256sum`; this is the base bytes the proposed
patch applies against, distinct from the manifest's PATCHED row, which
records the *post-apply* digest `abea545df981ef1d4838146f57816135d06bdf01f8ef0fabca238bbcbcfe54ad`).

Lines 178-186 (requirement paragraph, current, unpatched):

> A draft SHALL become ready for owner review only after independent
> fidelity and rendered-design reviews confirm the frozen bundle and all
> blocking findings have dispositions verified against that same bundle.
> [… full paragraph, ending] Further acquisition SHALL use its required new
> admitted input identity and consume remaining original bounds or a
> separately authorized new run; repair SHALL NOT broaden permission, erase
> spent usage or replay an uncertain effect.
>
> ID: REQ-polaris-generation-006
> Source: VIS-3; governing warrants below.
> Scope: v1-mandatory

Lines 214-221 (last scenario before the boilerplate):

> #### Scenario: New evidence outside the current budget or authority
>
> - **WHEN** a finding requires acquisition the existing permission or
>   remaining budget cannot support
> - **THEN** the run records the unresolved dependency and affected
>   readiness
> - **AND** no repair loop expands access, erases spent usage or disguises a
>   new run as a resumed old one.
>
> Form: lifecycle transition.

`PROJECT-STATUS.md` line 34 (current): "31 requirements and 177 scenarios
in the effective composition."

## Proposed meaning

Appends one sentence to the requirement paragraph (after "…replay an
uncertain effect."):

> Every block present in an edit or repair stage's input draft SHALL appear
> in that stage's output account with an explicit kept, rewritten, split or
> removed action and a reason; an edit or repair output SHALL NOT drop a
> prior block without that account, and a repair's finding dispositions
> SHALL cover every finding it was given, including any left unrepairable.

Inserts one new scenario before `Form: lifecycle transition.`:

> #### Scenario: Edit or repair drops a prior block without account
>
> - **WHEN** an edit or repair stage returns a draft whose blocks omit one
>   or more blocks present in that stage's own input draft
> - **THEN** the output is invalid unless its change account names each
>   omitted block's id with a removed action and a reason
> - **AND** a repair that leaves every supplied finding unrepairable,
>   returning its input draft unchanged with each finding disposed as
>   unrepairable, is valid and is distinguishable in the record from a
>   repair that changed content

`PROJECT-STATUS.md` line 34, changed digit only: "31 requirements and **178**
scenarios in the effective composition."

The exact bytes are the unified diffs at `proposed/spec.md.patch` and
`proposed/PROJECT-STATUS.md.patch`; this section quotes their content, it
does not define it — the patches are authoritative for the proposed bytes,
scripted and hash-verified by `build_polaris_edit_repair_deletion_scenario.py
--check`.

**Design provenance** [Inferred, not authority]: the new sentence's
`kept`/`rewritten`/`split`/`removed` + reason vocabulary and the
"unrepairable disposition is valid and distinguishable" framing are drawn
directly from `docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md` Gate 4's
design sketch (lines ~832-880: `changes: { blockId, action:
'kept'|'rewritten'|'split'|'removed', reason, newBlockIds }[];
findingDispositions: { findingId, action: 'repaired'|'unrepairable', reason,
affectedBlockIds }[]`) and its S7/S8 proposed acceptance criteria (lines
~1076-1083). That document is a candidate planning artifact, not authority;
this package treats it only as prior design analysis to draw scenario
language from, and restates the acceptance-criteria intent as spec-scenario
prose rather than adopting its schema names as binding.

## What explicitly does NOT change

- REQ-polaris-generation-006's ID, Source or Scope block.
- Any of the five existing scenarios under REQ-006 — none is edited,
  reordered or removed.
- Any other requirement (002, 004, 009, 012, 014, 019, 030, 031, or any of
  the 22 unmodified predecessor requirements).
- The predecessor file
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
  — read-only in this package, included in the manifest only as a
  REFERENCE row so drift in the bound predecessor bytes is caught by
  `--check`.
- `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` and
  `ACCEPTANCE-ACT-RECORD.md`'s own historical "177 scenarios" sentences —
  these describe the act's scope *as adopted* on 2026-09-13 and are frozen;
  they are REFERENCE rows in the manifest (hashed to catch any future edit
  attempt) and are never proposed for a patch. Only `PROJECT-STATUS.md`'s
  live, restated count moves.
- No code: `provider-draft.ts`, `pipeline.ts` and the app's
  `pipeline-demo.ts` are cited above as evidence only; none is touched by
  any patch in this package.
- No provider egress, no new source read, no schema or prompt file inside
  a bound package.

## Downstream impact / blast-radius sweep

**Method** [Observed]: grepped every existing candidate package directory
under `.syzygy/governance/contracts/candidates/*/proposed/` for a patch
whose `+++ b/` target is either `PROJECT-STATUS.md` or this package's
amendment spec path. **Denominator**: every directory directly under
`contracts/candidates/` that itself contains a `proposed/` subdirectory
(the `build_polaris_edit_repair_deletion_scenario.py --check`
`composition_findings()` function performs this same sweep on every run,
so the finding is live, not a one-time snapshot). **Result**: 0 collisions
found as of this drafting. If a sibling package lands first and it also
patches either file, this package's manifest must be regenerated with
`--write` before this package's own act can perform — the same
landing-order rule AGENTS.md's "Governance recorders" section states for
the PWB sibling packages.

**The 177 -> 178 count** [Observed, cross-checked by two methods, see the
builder's `scenario_delta_finding()`]: (1) counting literal
`#### Scenario:` headers in the amendment spec file itself, before and
after the patch, shows a delta of exactly +1; (2) the literal integer in
`PROJECT-STATUS.md`'s "N requirements and N scenarios" sentence, before and
after its patch, also moves by exactly +1 (177 -> 178), with the
requirement count (31) unchanged in both readings. This does **not**
re-derive the full composed total of 177/178 from the composition formula
(predecessor's 22 untouched requirements plus the amendment's 9); it
trusts the existing 177 baseline as the bound act's own recorded figure
(`POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` line 32, cited, not
recomputed) and checks only that both files move together by the same +1.
An owner or reviewer who wants the full composition re-derived from
scratch would need a separate pass; that is named as an open question
below.

`COVERAGE.md` and `GOVERNING-DEPENDENCIES.md` under
`openspec/changes/polaris-manifesto-understanding-amendment/` were grepped
for `polaris-generation-006` and `Independent review and repair`: 0 hits in
either file, so neither needs regeneration as part of this change
[Observed].

## Migration / supersession plan

None needed at drafting time: this is an additive scenario and a one-clause
paragraph extension, not a supersession of prior text. At adoption, the
performing act runs
`scripts/build_polaris_edit_repair_deletion_scenario.py --apply --at-adoption`,
re-confirms `--check` against the post-apply tree, and records the
manifest's digests in the act argument per `AGENTS.md` "Governance
recorders." Slice 4's implementation (bead `syzygy-dov.6.3`) unblocks only
once the owner signs off this scenario per P-73 Q6; implementation itself
still needs its own gate, since the M6 funnel doc's Q6 finding left it
ambiguous whether the existing `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`
already covers slice 4 or a fresh act is needed — this package does not
resolve that ambiguity (see open questions).

## Open questions for the owner

1. **Sign-off scope.** Does signing off this scenario (the spec text only)
   also serve as the "CC-REV-2 scenario … signed off" condition P-73 Q6
   names for unblocking slice 4's *implementation*, or does implementation
   still need its own separate authorization act, given
   `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` was performed
   before this scenario existed and the M6 funnel doc's Q6 left this
   ambiguous ("This act grants no implementation extension")?
2. **PROJECT-STATUS.md coupling.** This package bundles the
   `PROJECT-STATUS.md` digit change into the same act as the spec
   amendment, reasoning from AGENTS.md's own "a page that restates state it
   does not own goes stale silently" guardrail rather than from CC-REV-2's
   literal four-class text (which does not name descriptive status pages).
   Is that the right home for this fix, or should the digit update instead
   be treated as ordinary maintenance, not needing CC-REV-2 packaging at
   all?
3. **Full composition re-derivation.** This package verifies only that the
   177 -> 178 delta is +1 by two methods; it does not independently
   re-derive the full 178-scenario composed total from the underlying
   predecessor + amendment formula. If the owner wants that full
   recomputation as part of sign-off (rather than trusting the bound
   act's 177 baseline), say so and it can be added as a further check.
