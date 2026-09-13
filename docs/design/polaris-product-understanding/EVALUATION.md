# How we will know Polaris understands a project

Proposed evaluation design for the existing real-project proof obligation and
SPEC-DELTA.md D6. Not a performed evaluation, numeric quality score or owner verdict.

## Evaluate an account, not an API response

A successful response can contain valid JSON, fluent prose and real citations
while misunderstanding the application. The evaluation therefore asks whether
readers reach the right understanding, whether that understanding is supported,
and whether the page makes it easy to acquire at several depths.

The generator's inventory and review are product outputs under evaluation.
Independent evaluators prepare their evidence and expected answers directly from
admitted sources, before seeing the draft or its outline. They may use tools or
LLMs, but model agreement alone is not a ground truth. Disputed interpretations
remain explicit and route to source review or attributed owner clarification.

## Freeze a case before generating

Each case records its repository/snapshot, admitted classes, project boundary,
audience, supported profile, content/usage limits, permissible owner participation,
and exact engine/prompt/schema/renderer versions. Evaluators then freeze:

- material source facts, qualifications, disagreements and known unknowns;
- questions a fresh reader should answer after the introduction, main account
  and optional depth, with evidence-backed acceptable answers;
- important relationships and counterexamples to plausible wrong explanations;
- required source, terminology and component-reading paths;
- design/accessibility blocking criteria and the planned views/interactions;
- the expected outcome class: supported whole account, bounded partial account,
  owner clarification needed, or unsupported/refused scope.

The expected-answer artifact is not supplied to the authoring context. If later
source inspection changes an expected answer, retain that evaluator correction
and its reason; do not silently rewrite the oracle to fit the generated page.

When an owner clarification adds a permitted premise, independent evaluators
freeze a versioned extension from the attributed answer before evaluating revised
output. The extension records which questions, expected answers and scope changed;
it cannot use the new prose or internal review as its oracle. Affected earlier
judgments become inapplicable and remain traceable. The initial case may correctly
require clarification while the revised case has enough intent for a fuller
account. These are distinct outcomes, not a rewritten passing history.

A narrower scope accepted after a discovery limit is a new identified request.
Its useful partial result does not pass the original broader case. Corpus reports
retain both, including the reason and owner intervention required.

## A corpus that can challenge the product

| Case characteristic | What it tests | Misleading shortcut to reject |
|---|---|---|
| Rich, scattered documentation | Synthesis of distinctive intent across sources | Copying a polished README |
| Sparse intent, useful code evidence | Honest architectural explanation and targeted questions | Inferring the owner's mission from package names |
| Documentation/implementation disagreement | Desired/observed separation and material qualification | Choosing the more convenient story |
| Unconventional structure or multiple packages | Project discovery and boundary selection | Assuming one directory layout or one repository equals one thesis |
| Verbose or large admitted population | Bounded selection, omissions and explicit scope | Treating retrieved top-k chunks as the whole project |
| Irrelevant/generated bulk and misleading labels | Salience grounded in meaning and provenance | Equating file size or keyword repetition with importance |
| A factual edge with true endpoints but no relation | Relationship fidelity in prose and diagrams | Checking only node citations |
| Missing/denied source or unsupported language | Correct partial outcome and actionable explanation | Calling an unread capability absent |
| Changed purpose, qualification or relationship | Dependency-aware regeneration and stale review handling | Rewording the opening while depth tells the old story |

Several characteristics may belong to one project. Synthetic mutations make
specific predicates falsifiable; they do not replace the two real admitted
projects. A held-out case must not influence project-specific recipe tuning.
Record every attempt and bounded repair, including failures and abandoned runs,
so the final showcase is not mistaken for the full evaluated population.

## Separate the judgments

| Judgment | Independent evidence | Blocking finding |
|---|---|---|
| Scope and discovery | Admitted population plus accounted inspected/selected/unavailable material | Material in-scope omission disguised as complete coverage |
| Understanding | Source facts, premises, qualifications and disputed interpretations | Wrong purpose, erased conflict, or unsupported causal/motivational inference |
| Argument | Cold-reader answers at each stopping depth | Accurate feature list fails to explain purpose or essential relationships |
| Artifact fidelity | Every material claim/edge/term and its actual support | Supported endpoints with an invented edge; mismatched citations; stale glossary |
| Reader experience | Real page traversal, answers, screen/viewport and keyboard evidence | Dense middle, inaccessible depth, lost context, or sources replacing explanation |
| Owner effort | Actual interventions and their purpose | Owner must prewrite the inventory, argument or finished prose to obtain success |
| Regeneration | Changed source/answer and dependent artifacts/reviews | Old content or verdict remains eligible for changed meaning |
| Operational behavior | Known budgets, admissions, interrupted/uncertain effects and retained artifacts | Quality repair evades limits, repeats an uncertain effect or loses provenance |

Owner effort is recorded, not graded by an invented universal minute limit.
Separate substantive clarification of undocumented intent from manual rescue of
poor generation. A correct final page after extensive hand-authoring is not proof
that the generator produced it.

## Review the full reading

The cold reader first sees the introduction without a source briefing. They
explain why the project exists, whom it serves and its central proposition.
They then use the main reading and optional depth to explain a consequential
choice, how components relate, and a material limit or uncertainty. Record the
answers and navigation attempts, including mistakes and corrections.

Visual review captures the opening, middle, diagrams, deep dives and source paths
at narrow/wide widths and with keyboard/nonvisual navigation. A beautiful hero
cannot compensate for an incomprehensible body. A diagram's explanatory value
must survive its text equivalent. Uncertainty remains near the proposition it
qualifies, not solely behind a distant evidence drawer.

The evaluation can recommend that a qualified account is useful. It cannot
convert missing central intent into a complete manifesto or replace the owner's
separate comprehension/adoption judgment.

## Repair and compare honestly

Classify a failure at its deficient subject: discovery, understanding,
clarification, argument, prose, visual/depth artifact or rendering. Retain the
original finding, change, input/output identities and fresh review. A research
repair must invalidate the dependent plan and account; a source change must not
inherit an old review merely because the URL or artifact label is unchanged.

Compare the generated account with the repository's existing entry point and a
simple source-summary baseline under the same reader questions and permissions.
This comparison tests whether Polaris adds understanding. Winning against a weak
baseline does not waive a blocking factual, scope or design defect.

Report a matrix of cases and judgments: met, unmet, unproven, or not applicable
with a reason within the evaluation's scope. Do not collapse it to a universal
beauty/understanding score. The minimum two-project result is reported as evidence
for those profiles, not universal support. Wider product claims need additional
representative evidence.

## Evidence ladder, not completion by test count

1. Mechanical tests establish serialization, references, bounds and refusal paths.
2. Scripted runs establish stage integration and preview behavior.
3. Real bounded provider runs establish execution on actual admitted inputs.
4. Independent semantic and reader/design evaluation establishes useful output
   for the evaluated cases, after recorded repairs.
5. Held-out project and changed-source evaluation support the stated generality
   and maintenance claims; remaining unsupported profiles stay visible.

[Observed] The current implementation has evidence at the first two levels. Its
synthetic verification record at that checkpoint is not evidence of the later levels. The first convincing
product demonstration must include the real research/clarification path, an actual
manifesto and independent reader/source evaluation, not another scripted showcase.
