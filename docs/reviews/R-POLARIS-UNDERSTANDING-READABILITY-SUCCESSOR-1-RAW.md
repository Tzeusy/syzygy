# R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-1 — Polaris understanding readability successor review
Verdict: REVISE
Manifest-file SHA-256: 86fce922659679537f6d8ca42d3e73e6b22f0bbeadecd96fa4d6c6275b1aec3b
Reviewed commit: a68b193797fdbf9ebe868efac040d871284e616b

Package: `.syzygy/governance/contracts/candidates/polaris-understanding-readability-successor/`
(abbreviated PKG below). Proposed files are abbreviated `proposal.md.proposed` and
`design.md.proposed`; installed files are `openspec/changes/polaris-manifesto-understanding-amendment/{proposal,design}.md`.

## Mechanical checks

- [Observed] `sha256sum PKG/SUCCESSOR-MANIFEST.txt` = `86fce922…ec3b`, identical to the
  argument in PKG/OWNER-DECISION-PACKET.md:20.
- [Observed] Manifest rows for `design.md` (`37a64e32…`) and `proposal.md` (`5077b38b…`) equal
  `sha256sum` of `design.md.proposed` and `proposal.md.proposed`. The other six rows
  (`.openspec.yaml`, `COVERAGE.md`, `GOVERNING-DEPENDENCIES.md`, `SYNTHESIS-MAP.json`,
  `specs/polaris-generation/spec.md`, `tasks.md`) equal `sha256sum` of the current files.
  SUCCESSOR.json `predecessor` digests for proposal.md (`284859db…`) and design.md (`5b06017d…`)
  equal the current files.
- [Observed] `python3 scripts/readability_successor.py --all --check` prints
  `PASS candidate-unperformed` for all three packages, "3 successor package(s) checked", rc 0.
- [Observed] Both banner links in `proposal.md.proposed:4` and `:6` use `../../../.syzygy/governance/decisions/…`;
  from `openspec/changes/polaris-manifesto-understanding-amendment/` both targets exist
  (`test -f` ok for each).

## Banner truth (proposal.md.proposed:3-9)

- [Observed] "the owner adopted this amendment on 2026-09-13, recorded in POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md":
  the act reads "Act instant: 2026-09-13T01:58:26Z" and "Scope: adopt the specification amendment at the manifest's exact bytes"
  over "its exact eight-file subject". True.
- [Observed] "the tree-form amendment later replaced REQ-polaris-generation-004": POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md
  says "On 2026-09-28 the owner adopted…" and "What it adopts: the amended REQ-polaris-generation-004 in the understanding
  amendment's spec". REQ-004 is one of the seven amended blocks named in the understanding act. True.
- [Observed] "that agreement authorized the synthesis, and the act adopted its bytes" restates old proposal.md:3-5
  ("The owner's agreement to the three design documents authorizes this synthesis") and replaces the now-false
  "it is not represented as adoption of these newly generated specification bytes" with the act's own scope. True.

## Blocking findings

### M1 — Packet misdescribes the design change: five of six design sections are byte-unchanged, not "short trees"

PKG/OWNER-DECISION-PACKET.md:32-34:
> "**`design.md`.** Its six sections — product intent, the research and editorial loop, record ownership, clarification,
> evaluation and placement — become short trees. Every decision and interface is kept."

[Observed] Comparing `design.md` with `design.md.proposed`: the only changes are (a) the head paragraph (old design.md:3-5,
new design.md.proposed:3-7) and (b) the "Placement and compatibility" bullets (old :118-125, new :120-131), which gain bold
labels and re-wrapping. "Product intent" (old :7-25 / new :9-27), "Research and editorial loop" (old :27-48 / new :29-50),
"Record ownership and interfaces" (old :50-72 / new :52-74), "Clarification and change" (old :74-92 / new :76-94) and
"Evaluation contract" (old :94-114 / new :96-116) are identical prose paragraphs and the same table; none became a tree.
The packet's sentence is false for five of the six sections it names, so the owner is told the design was restructured
when only its head and one list changed. Repair: describe the actual change (a new lead sentence, the candidate label
removed, placement bullets labelled), or actually restyle the sections.

### M2 — Proposal Impact drops a "must": interface obligation becomes a present-tense statement

Old proposal.md:77-78:
> "Prompt, validator and renderer interfaces must consume one supported understanding."

New proposal.md.proposed:96-97:
> "**Interfaces:** prompt, validator and renderer consume one supported understanding."

[Observed] The modal "must" is gone. [Inferred] In a present-tense document the new sentence reads as a statement of
current fact, and it is not one: the same section keeps "The existing intermediate wire format and linear repair runner
are not silently declared conformant to these additions", and design.md:127-129 says `pipeline.ts` and
`provider-draft.ts` "do not yet … represent this full understanding model". This is both a weakened obligation and an
invented present-fact claim (bar items 1 and 2). The same flattening applies more mildly to "Generation core needs …" →
"**Generation core:** …" and "App adapters need …" → "**App adapters:** …" (old :74-75, new :90-93), where the label form
still implies need; only the "must" line reads as a false fact. Repair: "prompt, validator and renderer must consume one
supported understanding."

## Non-blocking notes

### N1 — Dropped pre-adoption instruction is obsolete, acceptably removed

Old proposal.md:81: "Before adoption, review the amendment's exact behavioral and source-class impacts." [Observed] Not
carried forward. [Inferred] The instruction was discharged by the 2026-09-13 act; dropping it is consistent with the
present-tense direction. Likewise "this candidate claims neither …" → "This amendment claims neither …" (old :82-83,
new :100-101) and "Candidate design accompanying the formal amendment" (old design.md:3) removed — both fine.

### N2 — "Do not archive/sync" became "Never archive or sync", in bold

Old proposal.md:46 "Do not archive/sync this as an unrelated competing change." → new :56 "**Never archive or sync this as
an unrelated competing change.**" [Inferred] Marginally stronger wording of the same prohibition; not a new obligation.

### N3 — Design lead sentence is supported by the diagram

design.md.proposed:3-5 adds "Polaris builds supported understanding before it writes: it investigates, asks, argues, then
lets independent review send defects back to the step that caused them." [Observed] The unchanged mermaid has
`R -->|Research defect| U` and `R -->|Composition defect| A`; the claim is a summary, not a new one. The proposal's new
thesis line (proposal.md.proposed:11-13) likewise restates old :60-62 ("investigates first and clarifies consequential
missing intent before a confident central thesis").

### N4 — Recorder-support claim verified; its "not recorded until it lands" is process, not mechanism

PKG/OWNER-DECISION-PACKET.md:38-44. [Observed] `scripts/record_polaris_understanding_adoption.py:392` has
`require(evidence.current(path) == adopted, 'current subject drift: ' + path)` over all eight rows; today `--check`
passes (rc 0). In a scratch worktree with only `proposal.md` replaced by `proposal.md.proposed`, `--check` printed
"FAIL exact digest reconciliation unresolved: current subject drift: openspec/changes/polaris-manifesto-understanding-amendment/proposal.md",
rc 1. The packet's claim is true. [Observed] `readability_successor.py` `record()` (lines 263-285) does not consult
that recorder, so "the act is not recorded until it lands" is a commitment by whoever records, not something the tool
enforces. [Unknown] The follow-up recorder change and "its own history review" are not on this commit (a68b193 removed
it from this branch: "The recorder is under review in another lane"); I cannot verify its described predicate.

### N5 — Other readers of the amendment directory

`git grep -n polaris-manifesto-understanding-amendment -- scripts .github apps packages` returns four files.
[Observed] `packages/polaris-generation-core/src/admitted-input.ts:5`, `scripts/build_polaris_edit_repair_deletion_scenario.py:46`
and `scripts/count_polaris_effective_scenarios.py:20` reference only `specs/polaris-generation/spec.md` or the directory
name, never proposal.md/design.md (`git grep -F 'understanding-amendment/proposal'`/`'understanding-amendment/design'`
over those trees: 0 hits). The fourth is the recorder in N4. `scripts/check_governance.py` binds the adoption act through
`docs/evidence/polaris-understanding-adoption-manifest-2026-09-13.json` (line 2127), not the current files. The old
digests also appear in `docs/evidence/polaris-understanding-adoption-manifest-2026-09-13.json`,
`…-amendment-validation-2026-09-13.json`, `…-reconciliation-2026-09-28/proof.json` and
`docs/reviews/R-POLARIS-UNDERSTANDING-FORMAL-SPEC-2026-09-13-RAW.md` — historical evidence, correctly left alone.
[Inferred] The recorder in N4 is the only reader the install breaks.

### N6 — Every other proposal claim is carried

[Observed] Checked sentence by sentence: Why (unchanged), What changes (four bullets, same content with labels),
Capabilities (modified/new, both kept), Amendment relation (seven MODIFIED, 22 unchanged, two ADDED, no-archive,
bound path, SYNTHESIS-MAP routing — all kept), Scope (admission first, declared support, permissions none granted,
investigate-then-clarify, first profile not an exemption, the eleven preserved requirement families, workspace/portfolio
and computed-rendering boundaries, the no-permission list — all kept; "exact-leaf, primary-altitude, authority-band"
became "exact leaf, primary altitude, authority bands", same meaning), Impact (Trajectory "retains" → "keeps" work
ownership; wire-format/runner non-conformance kept; authority-unchanged kept). No dropped exclusion or cross-reference
found beyond N1.
