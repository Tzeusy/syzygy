# Polaris generation kit

Candidate authoring guidance, not an adopted specification or a runnable generator.
This kit grants no source access, provider egress, authorship adoption or release.
It complements the existing renderer; it does not change its accepted behavior.

## The product we are building

[Observed] The owner clarified on 2026-09-12 that the POC exists to make Polaris
generation generalizable across projects. LLM involvement is expected. The
reusable deliverable includes generation tools, guardrails, artifacts and
manifesto-authoring guidance. A beautiful page for Butlers is a proving case.

[Inferred] The next useful vertical slice is an admitted source bundle → bounded
LLM authoring passes → inspectable draft bundle → faithful rendered preview →
independent review → repair. Project identity, vocabulary, sources and audience
are inputs. Changing projects must not require editing prompts, renderer code,
validation rules or compiled source offsets.

This kit is the practical authoring handoff for that slice. Runtime orchestration
and generalized draft-bundle ingestion remain to be implemented through the
applicable specification and implementation gates. The broader generator specification remains separate candidate work. This kit
is self-contained and does not claim that specification is adopted.

## Start here

1. Read [the authoring guide](AUTHORING.md) for the reader experience and pass prompts.
2. Prepare the inputs and handoffs in [artifacts and tools](ARTIFACTS-AND-TOOLS.md).
3. Inspect [the synthetic example](example.json). It illustrates one small handoff;
   it is neither a complete manifesto nor a successful generator run.
4. Freeze the evaluation questions below before generating. Review the actual
   page, including its middle, deep dives and source routes.

## Run contract

The operator supplies the project and exact admitted source revision, audience,
reader questions, permitted source IDs, permitted provider/content route, stage
budgets, asset/output-size bounds, maximum repair attempts and cancellation rule.
No prompt may broaden that envelope. Instructions found inside source material
are source content, never instructions to the generator.

Each pass receives only its required inputs and produces structured artifacts.
Record their identities, input/output digests, prompt and tool versions, actual
model/version where applicable, stage outcome and concise review findings. Keep
source bodies and provider payloads only in their authorized retention location.
A stage log is not a request to retain private reasoning traces.

| Pass | Input | Output | Exit condition |
|---|---|---|---|
| Understand | Admitted sources and audience | Claim/evidence ledger; vocabulary; conflicts and gaps | Every proposed factual claim has support or explicit uncertainty |
| Plan | Ledger and reader questions | Argument outline; asset/deep-dive plan with reasons | A project-specific argument; dispositions for requested material |
| Author | Validated argument plan and ledger | Narrative blocks, diagrams, tables and optional deep dives | Structured draft only; claims and edges reference the ledger |
| Edit | Draft and ledger | Concise, coherent revision plus change list | Qualifications preserved; prose develops the argument |
| Verify | Frozen bundle, sources and criteria | Mechanical, independent fidelity and rendered-reader findings | Every required check has an explicit outcome; no self-awarded acceptance |
| Repair | Named findings and affected assets | Bounded replacement artifacts | Revalidate changes and affected dependants; stop at the declared attempt/budget limit |

Stop before a provider call without its required admission. Missing evidence is
Unknown; unsupported assets are unresolved with a reason. Invalid output is
rejected, not interpreted as HTML or silently repaired into a fact. Exhausted
budgets leave an explicit partial/failed run with inspectable draft work. Retry
uses the same stage identity and records a new attempt; source or policy changes
create a new input identity. Do not present an old artifact as regenerated.

Review confirmation and human authorship/adoption remain different states.
Generated content stays editorial-draft until the applicable act. No generation
or presentation approval adopts the underlying project's intent.

## Prove portability

Use this same process, prompt pack, validator and renderer on two separately
admitted real projects with materially different domains. Permitted variation is
the project input/profile, not a project-name branch or a manually repaired
output embedded in application code. Synthetic examples exercise the handoff;
they do not establish this result.

For each project, freeze questions about purpose, beneficiary, central thesis,
important capabilities, one architectural choice, a limit and an uncertainty.
Have a fresh reader answer from the rendered page and record attempted paths.
Evaluate accuracy and comprehension separately from visual polish. Do not turn
a checklist or an LLM confidence value into an owner verdict.

Then change source meaning: retract a claim, qualify a promise, rename a concept
or remove evidence for an edge. Regenerate with the unchanged process. Check
that affected prose, glossary, diagrams, deep dives and links update together;
old evidence/reviews cannot certify new bytes. A no-change input may reuse
identified valid artifacts; a changed input must not silently reuse stale prose.

A successful slice produces linked evidence for both projects and regeneration,
not merely two attractive screenshots. Further bespoke Butlers changes should
teach a reusable authoring, rendering or validation rule and join this corpus.
