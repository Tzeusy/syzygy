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
  edits the same subject (currency bounds and the briefing ceiling). The
  builder applies `.18`'s diff and then this one while `.18` is
  unperformed, and this diff alone once `.18` has been applied. That order
  is a constraint of this drafting, not an owner ruling. Asked "Landing
  order for lane B and the three spec-touching packages?", the owner
  answered "Readiness order, lane B last (Recommended)" (the 2026-09-23
  owner-values record, §6); the option it selected read `.21` → `.30` →
  `.22` → lane B, and it orders those four packages only.
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
| `rootIndex` | The root index path, the `Pillar`/`Directory` table that declares pillar roots, and the link rule. Links are read always, after the table: a link whose target (or, for a `README.md` target, its directory) ends in a pillar key also declares that pillar's root, and two different roots for one pillar — from the table, from links or from both — make that pillar Unknown. |
| `pillars` | The five pillar keys with their display labels, in order. |
| `sourcePopulation` | The index chain depth (3), the pillar index basename, the five source rules, the two tree populations with their path patterns and companions, and the eight bindings from a file to the classes it feeds. |
| `containerShapes` | Nine named shapes a class's items can take in a source — a heading section, a numbered list, a table's rows, a Git tree path, one TOML field and so on — each with one sentence saying exactly what it reads and what fails. |
| `classGrammar` | Fifteen rows. Each names one class, its source file, the heading(s) it reads under as `heading` objects (with `level` where the code fixes one; the catalog row takes its texts from `fixedCatalogKeys` by `textsFrom`), one container shape, and what becomes the item's key, how a key fails and, where the code sets one, the item's context (the catalog heading, the topology ordinal, the TOML value). |
| `sourceGrammarSemantics` | Six sentences: `scope` (the fields restate today's per-project grammar and must reproduce today's manifest and observation digests and, for every source, the items extraction reads from it; the shared rules stay in code); `headingMatch` (what a heading is — an ATX heading written at column 0, so an indented line is never one — and how a declared one matches or fails); `containerShape` (one shape per row, and any failure makes the whole source Unknown); `itemKey` (duplicate keys fail); `sharedReadingRules` (the reading rules every project shares — fences, list items, bold spans, tables, index links, tree-rule precedence — which no profile sets); and `missingField` (a loader refuses a missing field rather than using built-in values). |

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
  reads.** `--check` tests the restatement three ways. (1) Every heading
  text and catalog key is present in the specification's reader
  definitions. (2) The root path, depth, pillar keys and labels, source
  rules, bindings and tree patterns match the constants in the two
  TypeScript files; heading texts are found there as quoted literals.
  (3) The observer's own code, run under Node over files built from the
  fields alone, derives the source list the fields predict (depth, root
  index, pillars, sources) and reads the items they predict (class, key,
  text and, where the code sets one, context); 92 probes each vary one
  file and check one clause's outcome and that the sentence states it.
  The probes run for every row, and a row carrying a field its shape and
  key form do not read is refused. `--selftest` breaks the fields and the
  checks 223 ways, every one caught. What is **not** proved: a clause no
  probe exercises is checked only by its pinned wording, and no check can
  show the code has no rule the fields omit.
- The six existing grammar keys, `resourceLimits` and its semantics, the
  entry's two governance-lifecycle strings, `discoveryVersion` and every
  other field are byte-identical after the diff (checked).
- No specification, contract, policy or decision byte is touched. No act
  record is written and nothing is appended to `ACCEPTANCE-ACT-RECORD.md`.
- No implementation file is changed.

## Warrant

P-74 in the ruling record, arm A, the owner's answer ("Ruled" column):
"Q2 one registry-entry amendment act before slice 5's fifth limb only, the
first four limbs thread a profile parameter with current constants as
default" [Observed, quoted from row P-74]. The same row's "What it means"
column, which is the recorder's gloss and not the owner's words, adds
"Slice 5's fifth limb waits for the registry act" [Observed].

That gloss column also says "The consent record, the registry entry and
PWB-REQ-005 are edited on no arm." Read literally that forbids this
package's subject, which the owner's Q2 answer puts under an act. Two
readings reconcile the gloss with the answer: the sentence covers the other
slices' arms only, or "edited" means changed in place outside an act, which
a superseding act is not [Inferred]. Where they differ the draft follows
the answer; packet question 3 asks the owner whether either reading
misstates it.

Doctrine: `VIS-4` reserves the act to the owner; `VIS-2` requires a source
the grammar cannot read to stay Unknown, which the `containerShape` and
`missingField` sentences state; `VIS-7` requires the result to be
deterministic, which the `scope` sentence's reproduction duty serves.

Method: `NORMATIVE-CHANGE-WORKFLOW.md` and `SEMANTIC-DELTA-TEMPLATE.md`
under `.syzygy/governance/contracts/candidates/policy-candidates/`. This
delta is at step 3: two independent review rounds each returned REVISE,
and this revision repairs the findings of both. The revision has not been
reviewed.

## Evidence or decision basis

- [Observed] The six current keys and the absence of the new ones, read
  from the subject.
- [Observed] The new fields against all three witnesses:
  `scripts/build_pwb_registry_loaded_profile_amendment.py --check`
  re-derives this on every run.
- [Observed] The diff introduces 48 key names. 15 are plain words
  (`key`, `text`, `path` and the like) that no sweep can separate. Of the
  33 distinctive ones, 24 occur in no tracked file at the baseline; the
  other nine are listed with their hits in `IMPACT-LEDGER.md`. Three of
  those nine — `rootIndex`, `pillars`, `sourcePopulation` — are already
  code identifiers; none of those reads the registry.
- [Inferred] That the fields plus the shared rules describe today's reader
  completely. The behaviour check shows the code reading the profile-built
  files as the fields say, and each probed clause holding; it does not
  prove the code has no rule the fields omit.
- [Observed] Neither `project-shape-observation.ts` nor
  `project-shape-manifest.ts` imports `project-shape-extraction.ts`. So
  [Inferred] today's manifest and observation digests depend only on
  `rootIndex`, `pillars` and `sourcePopulation`, and reproducing them says
  nothing about `classGrammar`, `containerShapes` or
  `sourceGrammarSemantics`. For those three keys the only witness today is
  the builder's behaviour check; that is why the `scope` sentence also
  requires every source's extracted items to be reproduced.
- [Unknown] Whether limb 1's regression oracle will compare the extracted
  items as well as the two digests. It is not built.
- [Observed] The overlap with M15: the ruling for P-82 Q4 puts "the
  root-independence flags" in M15's delta to `PWB-REQ-002` (`.15.1`). This
  revision adds no such flag; the one clause touching it, the last of
  `sharedReadingRules`, states today's root-blind tree enumeration. Packet
  question 9.
- [Unknown] Whether these field names match the profile schema limb 1
  will write. That schema does not exist yet (packet question 2).

## Terms introduced or retired

Introduced, in the subject's own bytes: `rootIndex`, `pillars`,
`sourcePopulation`, `containerShapes`, `classGrammar`,
`sourceGrammarSemantics`, their sub-keys (listed in `IMPACT-LEDGER.md`),
and the nine container-shape names. Retired: none.

## Downstream impact

Enumerated in `IMPACT-LEDGER.md`. In one line each:

1. **The observer-identity parity test fails until `observerVersion` moves
   in code.** `project-shape-observation.test.ts` checks
   `PWB_OBSERVER_IDENTITY` against the entry; the adoption change carries
   the version bump.
2. **Nothing reads the new fields on adoption alone.** Only slice 5's
   fifth limb reads them, and it is blocked on this act and on limbs 1–4.
3. **This builder needs `.18` applied first** (a drafting constraint, not
   an owner ruling). If `.18`'s patch changes, this package's manifest is
   regenerated with `--write`.
4. **M15's delta (`.15.1`) may later replace the last `sharedReadingRules`
   clause** with a per-population root-independence flag; that would take
   a further registry act.

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

Round 1: `docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-RAW.md`, over
commit `31305bc`. Verdict: REVISE (seven revise findings, five notes). The
packet's "Review record" table dispositions every one. This revision has
not been reviewed; `REVIEW-BRIEF.md` states what round 2 is given.
