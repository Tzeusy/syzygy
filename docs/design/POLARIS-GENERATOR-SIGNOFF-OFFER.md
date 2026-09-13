# Build the generalized Polaris generator

**Owner decision prepared; no act recorded.** Approval adopts the exact package
and authorizes the implementation described below. The generator is not yet
implemented, and this package makes no completion claim.

The outcome is a reusable LLM-assisted generator that turns admitted project
sources into a beautiful, coherent manifesto: a clear introduction, concise
prose, useful navigation and glossary, informative relationship diagrams, and
optional component deep dives. It must support starting a run, following its
progress, cancelling or resuming, reviewing the rendered result, and repairing
failed output.

## The decision

Approve three distinct records over one exact package:

1. **Specification:** the frozen generator behavior and output-quality criteria.
2. **Applicability:** the stated per-project scope. Workspace and portfolio
   composition are outside this operation; project relationships remain required.
   Computed rendering, observed-project code launchers and unrelated intake are
   not enabled. These dispositions do not waive obligations for future features.
3. **Implementation:** build the complete generator, protected local effect host,
   owner workflow and verification suite described by the package.

Implementation may begin with isolated generation mechanics, but completion
requires the same engine, prompts, validators and renderer to produce reviewed
manifestos for two separately admitted real projects. A real source-meaning
change must regenerate affected content and invalidate obsolete reviews.
Synthetic fixtures and the existing Butlers page cannot establish completion.

## What remains separately admitted

Actual project reads, provider/model egress and output destinations require
concrete permissions before use. This decision grants no production release,
broad remote access or execution of observed-project code. Existing permissions
are reused where they apply.

## Review materials

- [Delivery plan](POLARIS-GENERATOR-DELIVERY.md)
- [Frozen source manifest](../evidence/polaris-generator-review-subject-2026-09-12.json)
- [Output design acceptance](../../openspec/changes/polaris-manifesto-generation/DESIGN-ACCEPTANCE.md)
- [Execution phases and completion criteria](../../openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md)
- [Proposed applicability scope](../../openspec/changes/polaris-manifesto-generation/APPLICABILITY-DECISIONS.md)

## Exact approval

[Immutable offer](../evidence/polaris-generator-approval-offer-2026-09-12.json)
binds the 23 source files, current governing baseline, two passing confirmation
reviews and the exact conditional applicability selections. The recorded act
would be owner-adopted bootstrap provenance; an A1 audit identity is explicitly
absent. No independently verified authorship is asserted.

To approve this exact package, reply with:

```text
ADOPT POLARIS GENERATOR SPECIFICATION, SCOPED APPLICABILITY AND IMPLEMENTATION: 48216b0607b1b82fa21f2c5f5a3499d604541b7a0a9bf93c9fd5f7c8deab29dd
```

- [Specification and scope confirmation](../reviews/R-POLARIS-GENERATOR-SCOPE-CONFIRMATION-2026-09-12-RAW.md)
- [Recording-tool confirmation](../reviews/R-POLARIS-GENERATOR-RECORDER-CONFIRMATION-2026-09-12-RAW.md)

The repository's AGENTS.md requires an authorizing act before implementation
outside existing scope. RFC7-38 requires approved specification coverage or
recorded applicability judgments before observable Polaris implementation.
This is the remaining implementation gate; it is not a claim that the product
has been built or that source/provider permissions have been granted.
