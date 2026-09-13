# Polaris: understanding a project well enough to explain it

Working product proposal — not an adopted doctrine amendment, specification
amendment, implementation extension or source/provider permission.

[Observed] The existing generator specification was adopted on 2026-09-12; its
bound source banners remain unchanged. The owning records are the
[specification act](../../../.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md)
and [implementation act](../../../.syzygy/governance/decisions/POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md).
This proposal starts at implementation commit `cb0614a`. It strengthens the
existing `polaris-generation` capability rather than creating a parallel product
specification or changing the approved files in place.

Read [the product vision](VISION.md) first. [The proposed behavior delta](SPEC-DELTA.md)
makes its decisions testable and identifies the existing requirements affected.
[The evaluation design](EVALUATION.md) describes evidence that could establish
understanding, useful writing and portability, and evidence that cannot.

## The gap this proposal addresses

[Observed] The current executable slice accepts already prepared sources and
uses scripted responses in its demonstration. It connects stages, validates
intermediate records and renders a preview. It neither discovers an unfamiliar
repository nor establishes that an LLM understands it.

[Inferred] The central product problem is therefore upstream of prose generation:
build a defensible account of what a project is for, what its parts mean, and what
remains unsettled, then turn that account into a compelling reading experience.
The adopted spec already requires supported argument, independent review and real
project proof. Those are unfinished obligations, not missing ideas. The proposed
additions make discovery, owner clarification and semantic coverage more concrete.

## Decisions proposed for discussion

- Investigate first; ask the owner only questions whose answers materially change
  the account and cannot be recovered from permitted evidence. A missing central
  purpose blocks a confident thesis, not all useful partial exploration.
- Treat code as evidence about structure and implementation. Code alone cannot
  establish the owner's purpose, motives, normative promises or product direction.
- Make one project understanding record feed prose, diagrams, glossary and depth;
  do not author those as independent summaries with conflicting meanings.
- Judge useful understanding and visual comprehension independently of schema
  validity, citation counts and the generator's own reviewer verdict.
- Admit supported repository profiles explicitly. “Any codebase” is a direction
  for generalization, not a claim of universal language, scale or access support.

These are proposed design choices. In particular, the clarify-before-confident-thesis default
remains an owner preference to confirm; the alternative is a deliberately
qualified account followed by questions. Neither permits invented intent.

## Remaining product choices

The first supported profile is still to be selected: documentation-led projects
with interpretable structure, or code-first projects needing more owner intent.
That choice sets the initial discovery/evaluation promise; it does not remove
sparse-intent and held-out challenge cases or imply permission to read code.
Interview timing is the current owner question. A later profile decision should
name languages, source classes, project boundary and scale together.

## Funnel and change boundaries

| Gate | Finding |
|---|---|
| Baseline | Doctrine, accepted contracts and craft policies exist; the adopted generator spec owns this capability. Placement is described by its delivery design; topology candidates do not acquire authority here. |
| Problem and user | The owner needs a project-specific account without first writing a dossier or hand-designing the page. A fresh reader must understand its purpose and important relationships. |
| Doctrine | Proposed alignment with VIS-1/2/3: simplify presentation, preserve truth and uncertainty, evaluate human understanding. VIS-4 continues to reserve intent adoption to the owner. |
| Placement | Acquisition and permission adapters at the app boundary; understanding/argument contracts and validators in generation core; authoring and challenge prompts as versioned recipes; owner clarification and previews in Polaris, work lifecycle in Trajectory. |
| Design | Discovery → understanding → clarification where necessary → argument → composition → independent review; repairs can revisit understanding rather than only rewrite prose. See VISION.md. |
| Spec | Proposed additive amendments in SPEC-DELTA.md, retaining existing IDs and scenarios; new source-class and clarification effects need explicit impact review before adoption. |
| Quality | EVALUATION.md supplies independent denominators, challenge cases, actual reader/visual evidence and limits on generality claims. |

No new read class is enabled here. Existing Butlers consent does not become code,
history, issues or arbitrary repository access. The source, authority, retention,
privacy and authoring consequences of discovery and owner answers must be reviewed
before this proposal can become an exact amendment offer. This packet is ready
for product discussion, not presented as an approval transaction.
