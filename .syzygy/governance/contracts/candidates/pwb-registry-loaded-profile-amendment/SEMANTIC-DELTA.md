# Semantic delta — the Butlers source grammar written into the registry entry

> **Candidate — binds nothing.** Agents drafted these bytes under the
> owner's 2026-09-21 ruling P-74 question 2 in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
> which authorizes **drafting only**. Effect would come from one superseding
> `adopt-registry-entry` owner act over the subject named below, and from
> nothing else. Silence, a commit, a review, a merged pull request, a
> passing check or this manifest performs no act. Nothing here authorizes
> an implementation: M8 slice 5's fifth limb, which would read these
> fields, is its own work under its own gates.

**Artifact(s):**

- `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
  — the single subject. Its current bytes are the argument of the act
  recorded at
  `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
  (2026-09-05). Those bytes are **not edited here**. The proposed bytes
  exist only as the unified diff
  `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`.
- **This diff is drafted on top of another candidate.** The `syzygy-dov.18`
  package at
  `.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/`
  edits the same subject (currency bounds and the briefing ceiling) and
  lands first. The builder applies `.18`'s diff and then this one while
  `.18` is unperformed, and this diff alone once `.18` has been applied.
  The single row of `PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt` hashes the
  result.

**Stable IDs affected:** none is amended. The fields restate the literal
extraction grammar of the PWB specification's reader definitions and
`PWB-REQ-002`/`PWB-REQ-004`, whose words do not change. `PWB-REQ-001`'s
determinism sentence is the requirement slice 5's fourth limb serves
(the profile digest as a deterministic input); this package does not
touch it.

**Change class:** **Normative.** The subject is digest-bound: any change
retires the digest the act in force names, so there is no editorial path
through it. The added fields also change what an implementation is
obliged to do once it loads them — a loader must refuse, never fall back,
when a field is missing (`missingField` below).

**Author:** agent draft, under the ruling record named above.

**Date:** 2026-09-26.

## Current meaning

The entry's `observationGrammar` has six keys, in this order:
`factFamilies`, `fixedClassKeys`, `fixedCatalogKeys`,
`fixedProjectAccountKeys`, `rootSummary`, `precedence` [Observed, keys read
from the JSON]. It carries **no** root index path, no pillar labels, no
rule for which file feeds which extraction class, no heading texts for the
vision, V1 and catalog sources, and no rules for the two tree-enumerated
populations (baseline specifications and roster butlers). Every one of
those exists today only as a TypeScript constant in
`packages/three-surface-poc-core/src/project-shape-manifest.ts` and
`packages/three-surface-poc-core/src/project-shape-extraction.ts`
[Observed, read at source]. The M8 funnel records the same gap at
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md`, section "The registry
entry, and why slice 5 needs an act".

The act in force says how that gap may be closed. Its Effect closes: "An
edit to the artifact breaks this act's digest binding; changes travel as a
new act" (`PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` lines 76–77)
[Observed, quoted at the clause].

## Proposed meaning

The diff makes two changes. `--diff` prints it; `--check` proves it applies.

**1. Six keys added to `observationGrammar`, after `precedence`.** The six
existing keys are byte-for-byte unchanged.

| Key | What it says |
|---|---|
| `rootIndex` | The root index path, the `Pillar`/`Directory` table that declares pillar roots, and the link rule used when that table is absent. |
| `pillars` | The five pillar keys with their display labels, in order. |
| `sourcePopulation` | The index chain depth (3), the pillar index basename, the five source rules, the two tree populations with a `rootIndependent` flag each, and the eight bindings from a file to the classes it feeds. |
| `containerShapes` | Nine named shapes a class's items can take in a source — a heading section, a numbered list, a table's rows, a Git tree path, one TOML field and so on — each with one sentence saying exactly what it reads and what fails. |
| `classGrammar` | Fifteen rows. Each names one class, its source file, the heading(s) it reads under (with level where the code fixes one), one container shape, and what becomes the item's key. |
| `sourceGrammarSemantics` | Five sentences: the fields restate today's grammar and must reproduce today's digests; how a heading matches; what a mismatched shape does; what `rootIndependent` means; and that a loader refuses a missing field rather than using built-in values. |

**2. The version bump.** `registryVersion` and `observerVersion` both move
from `1.2.0-candidate.1` (the `.18` value) to `1.3.0-candidate.1`, a minor
bump in the entry's own convention. `discoveryVersion` is **not** bumped:
the fields restate discovery and extraction, they do not change it. Whether
that is right is open question 4 in the packet.

**Why a container-shape vocabulary is in this package.** The sitting of
2026-09-26 (§6, recorded in
`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`)
asks for a separate specification amendment, N8, letting a
project's profile declare its own container shapes, with Butlers declaring
today's. Those declarations need somewhere to live that an act binds. This
package puts Butlers' in `containerShapes` and `classGrammar`, so N8 can
point at them. Whether N8's registry need rides this act or a later one is
the packet's first open question.

## What explicitly does NOT change

- **No class, heading, source, shape or key is added to what the observer
  reads.** `--check` proves the restatement two independent ways: every
  heading text and catalog key appears in the specification's reader
  definitions, and the root path, depth, pillars, source rules, bindings,
  tree patterns and heading texts appear as the exact constant source
  lines in the two TypeScript files.
- The six existing grammar keys, `resourceLimits` and its semantics, the
  entry's two governance-lifecycle strings, `discoveryVersion` and every
  other field are byte-identical after the diff (checked).
- No specification, contract, policy or decision byte is touched. No act
  record is written and nothing is appended to `ACCEPTANCE-ACT-RECORD.md`.
- No implementation file is changed.

## Warrant

P-74 in the ruling record, arm A: "Q2 one registry-entry amendment act
before slice 5's fifth limb only, the first four limbs thread a profile
parameter with current constants as default", and in the same row: "Slice
5's fifth limb waits for the registry act" [Observed, quoted from row P-74].

The same row also says "The consent record, the registry entry and
PWB-REQ-005 are edited on no arm." Read literally that forbids this
package's subject. This package reads the sentence as describing the other
slices' arms, because Q2 in the same row rules an act over the registry
entry [Inferred]. The owner decides the reading — packet question 3.

Doctrine: `VIS-4` reserves the act to the owner; `VIS-2` requires a source
the grammar cannot read to stay Unknown, which the `containerShape` and
`missingField` sentences state; `VIS-7` requires the result to be
deterministic, which the `scope` sentence's digest-reproduction duty
serves.

Method: `NORMATIVE-CHANGE-WORKFLOW.md` and `SEMANTIC-DELTA-TEMPLATE.md`
under `.syzygy/governance/contracts/candidates/policy-candidates/`. This
delta stops at step 2: drafted, blast radius established. **No review has
been run and no self-review was performed.**

## Evidence or decision basis

- [Observed] The six current keys and the absence of the new ones, read
  from the subject.
- [Observed] Every literal in the new fields against both witnesses:
  `scripts/build_pwb_registry_loaded_profile_amendment.py --check`
  re-derives this on every run.
- [Observed] The four new key names occur in no tracked file today; see
  `IMPACT-LEDGER.md`.
- [Inferred] That the fifteen class-grammar rows describe today's reader
  completely. The check proves each literal is present in the code; it
  does not prove the code has no rule the rows omit. Limb 1's regression
  oracle (reproduce today's manifest and observation digests from the
  profile) is the proof, and it does not exist yet.
- [Unknown] Whether these field names match the profile schema limb 1
  will write. That schema does not exist yet (packet question 2).

## Terms introduced or retired

Introduced, in the subject's own bytes: `rootIndex`, `pillars`,
`sourcePopulation`, `containerShapes`, `classGrammar`,
`sourceGrammarSemantics`, and the nine container-shape names. Retired:
none.

## Downstream impact

Enumerated in `IMPACT-LEDGER.md`. In one line each:

1. **The observer-identity parity test fails until `observerVersion` moves
   in code.** `project-shape-observation.test.ts` checks
   `PWB_OBSERVER_IDENTITY` against the entry; the adoption change carries
   the version bump.
2. **Nothing reads the new fields on adoption alone.** Only slice 5's
   fifth limb reads them, and it is blocked on this act and on limbs 1–4.
3. **The `.18` package must land first.** If `.18`'s patch changes, this
   package's manifest is regenerated with `--write`.

## Migration and supersession plan

**Supersession.** One superseding `adopt-registry-entry` act, superseding
whichever registry act is then in force (the `.18` act, if performed).
The superseded record, its digest and its bytes stay unedited.

**The adoption change is indivisible.** It carries, together:
`--apply --at-adoption` (which refuses until `.18`'s bytes are in the
tree); the new dedicated recorder; the new `PWB_EFFECT_AMENDMENT_ACTS` row
in `scripts/check_governance.py`; the `observerVersion` constant; and the
act-record path in `apps/three-surface-poc/src/governance-inputs.ts`.

**Rollback.** Before the act: delete this directory and the builder.
After it: a further superseding act, never an edit.

## Review

None yet. `REVIEW-BRIEF.md` states what an independent reviewer is given.
