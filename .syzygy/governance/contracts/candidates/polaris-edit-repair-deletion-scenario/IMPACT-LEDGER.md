# Impact ledger — Polaris edit/repair deletion-account scenario

> Candidate — binds nothing. Bead `syzygy-dov.23`.

## Discovery method

- Read `docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md` (candidate
  planning doc, bead `syzygy-dov.6`) Gate 5, which already ran an
  RFC2-26-shaped test against REQ-polaris-generation-006 for slice 4 and
  recorded "requirement available, scenario partial."
- Independently re-read
  `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
  lines 178-222 this session and confirmed, by literal line-anchored count,
  exactly 5 `#### Scenario:` headings under REQ-006 (at lines 187, 193,
  199, 205, 214), none naming an edit/repair-stage deletion.
- Grepped the generator code for the "edit" stage in both named
  directories from the task brief:
  - `packages/polaris-generation-core`: `provider-draft.ts` line 45 (shared
    `draft` schema for `author`/`edit`/`repair`) and its `validateStage`
    `else` branch, lines 143-156 (never reads `context.draft`, the prior
    draft — 2 hits total for the literal `context.draft` in the file, both
    in the separate `fidelity` branch); `pipeline.ts` lines 314-320
    (`context.draft` unconditionally reassigned per stage, no diff kept).
  - `apps/three-surface-poc/src/polaris-generation`: exactly 1 hit for
    `edit` outside test files, `pipeline-demo.ts:66`, a demo-harness fixture
    mapping stage names to canned responses, reusing the same `draft`
    schema for `edit` as for `author`. No app-level accounting logic
    exists to inspect; the gap is entirely in the core package.

## Classes

| Class | Count | What it means for this package |
|---|---|---|
| PATCHED (proposed, not applied) | 2 | `PROJECT-STATUS.md`, the amendment `spec.md` |
| REFERENCE (read, hashed, never patched) | 4 | predecessor `spec.md`, `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`, `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, `review-and-documentation.md` (CC-REV-2's home) |
| Code cited as evidence, not touched | 3 files | `provider-draft.ts`, `pipeline.ts`, `pipeline-demo.ts` |
| Planning artifact cited, not authority | 1 | `docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md` |

## The two artifacts that move (post-adoption)

| File | Current sha256 | Proposed (post-apply) sha256 |
|---|---|---|
| `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md` | `b7c95f57ca5f67a18570b7124d20b223dff99aea2a936efef76d5940a400f93f` | `abea545df981ef1d4838146f57816135d06bdf01f8ef0fabca238bbcbcfe54ad` |
| `PROJECT-STATUS.md` | `e78865bb2ed0c4ee4098b81ff66a66dad813f39f46023ccee152e6d7e69324b8` | `819197d6994d668e315f32f4f119a727c1a851953098746f100bc195930e7fc7` |

Both digests are computed by
`scripts/build_polaris_edit_repair_deletion_scenario.py`'s `render_manifest()`
(via `git apply` in a scratch tempdir, never the real tree) and recorded in
`POLARIS-EDIT-REPAIR-DELETION-SCENARIO-MANIFEST.txt`; they are not
transcribed by hand into this ledger from anywhere but that generated
manifest (verification rule 3).

## Files NOT in scope, and why

- `openspec/changes/polaris-manifesto-understanding-amendment/COVERAGE.md`
  and `GOVERNING-DEPENDENCIES.md` — grepped for `polaris-generation-006`
  and `Independent review and repair`: 0 hits in either file this session,
  so neither tracks REQ-006's scenario content and neither needs
  regeneration.
- `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
  (the predecessor's own copy of REQ-006, lines 300-344 there) — superseded
  in force by the amendment overlay for this requirement ID per the
  composition rule in AGENTS.md Architecture; read-only REFERENCE row here,
  never a patch target.
- `.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`
  line 32 and `ACCEPTANCE-ACT-RECORD.md` line 506 — both carry the same
  historical "177 scenarios" phrase describing the *act's own scope as
  adopted* on 2026-09-13. These are frozen, bound-act bytes and are never
  proposed for a patch; they are REFERENCE rows only, so `--check` still
  catches an accidental future edit to them, but this package does not and
  cannot correct their now-superseded-in-context wording (matching the
  documented "bound file's own banner can be permanently wrong" guardrail
  pattern for a similar case elsewhere in this repository).
- No code file is patched.

## Merge and landing-order boundary

**Method** [Observed, live-computed, not a one-time snapshot]: every
`--check` run of `scripts/build_polaris_edit_repair_deletion_scenario.py`
calls `composition_findings()`, which lists every directory directly under
`.syzygy/governance/contracts/candidates/` (excluding this package) that
itself has a `proposed/` subdirectory, reads every `*.patch` file's
`+++ b/<path>` target line, and compares it against this package's two
PATCHED paths (`PROJECT-STATUS.md`, the amendment `spec.md`).

**Denominator**: every sibling candidate-package directory under
`contracts/candidates/` with a `proposed/` subdirectory, as of the commit
`--check` is run at. Re-swept this session with `for d in
.syzygy/governance/contracts/candidates/*/; do [ -d "${d}proposed" ] &&
echo "$d"; done`: **6** siblings as of this drafting
(`pwb-exact-source-render-mode-scenario`, `pwb-machine-view-amendment`,
`pwb-missing-currency-disclosure-scenario`, `pwb-opening-band-scenario`,
`pwb-registry-currency-briefing-amendment`, `pwb-scoped-attributes-amendment`).
An earlier draft of this ledger listed 10 directories from a stale mental
list that included packages with no `proposed/` subdirectory
(`pwb-effect-acts`, `pwb-state1-amendment`, `pwb-truth-policy-amendment`,
`pwb-walkthrough` — these exist as directories but carry no patches, so a
directory-name sweep alone overcounts); corrected here to the actual
`proposed/`-bearing population per verification rule 9 (an absence claim
needs a sweep with a denominator, and the denominator itself has to be
re-derived, not recalled).

**Result**: 0 collisions found. No sibling package's `proposed/*.patch`
targets either `PROJECT-STATUS.md` or the amendment `spec.md`.

**If this changes before adoption**: whichever act — this one or a
colliding sibling's — lands second must regenerate its manifest with
`--write` before it can be performed, per AGENTS.md's "Governance
recorders" note ("Sibling packages patching the same CG-7h-bound tree …
each hash post-apply bytes against the *current* tree: whichever act lands
second must be regenerated with `--write` first"). `--check`'s
`composition_findings()` call will surface a future collision as a hard
`FAIL` on this package's own `--check`, not merely a warning, since no
sibling collision is documented or expected today.

## Scenario-count cross-check (177 -> 178)

Performed by `scenario_delta_finding()` in the builder, using two
independent methods over the same two files, both scripted (verification
rule 2, "confirmed by a second method"):

1. **Amendment file's own scenario-header count**: literal occurrences of
   `#### Scenario:` in the amendment `spec.md`, before the patch versus
   after. Delta: **+1**.
2. **`PROJECT-STATUS.md`'s stated total**: the literal integers in "N
   requirements and N scenarios in the effective composition," before the
   patch versus after. Requirements: unchanged at 31 in both readings.
   Scenarios: **177 -> 178**, delta **+1**.

Both deltas agree at +1. This is a consistency check on the *delta*, not a
full re-derivation of the composed 177/178 total from the underlying
predecessor-plus-amendment composition formula (see SEMANTIC-DELTA.md open
question 3) — the 177 baseline is trusted as the bound act's own recorded
figure, cited by path and line, not recomputed from the two spec files'
full requirement sets.
