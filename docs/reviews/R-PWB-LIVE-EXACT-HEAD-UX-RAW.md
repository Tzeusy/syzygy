# PWB live exact-head owner UX review — raw

Date: 2026-09-05

Reviewer role: independent owner-UX / cold-open preflight

Syzygy subject: `cd6c95250772d98c199020c08e25476fbe34bb5b`

Observed Butlers revision: `a3dd1fe08a1d9a11b5e899e0ecf33f03d8eefc96`

Surfaces: `http://127.0.0.1:7478/polaris` and
`https://tzeusy.parrot-hen.ts.net/butlers-syzygy/polaris`

## Review posture

[Observed] I read the assigned baseline and the binding review criteria before
opening the surface: VIS-1/2/3/7, RFC7-30/31/34, PWB-REQ-010/011/012/016/021,
and parent POC-REQ-030/031/032/060/061. I applied the project-specific
requirements before the generic design-bar biases. I first formed the
surface-only answers below from the rendered Polaris response, then opened the
exact Butlers project-shape artifacts at the named revision to check those
answers. The selected historical prompt was
`_bootstrap/review-prompts/08_OVERVIEW_ACCESSIBILITY_AND_NARRATIVE.md`, adapted
from a static overview to the live Polaris entry.

[Observed] Review modes were desktop visual, narrow-screen visual,
plain-text/nonvisual, and keyboard-only. Google Chrome 120 was driven through a
browser driver outside the renderer for the complete live loopback DOM. This
raw review is not a kernel walkthrough execution record under RFC7-31, is not
an owner decision, and does not satisfy or simulate PWB-REQ-022. It records an
independent preflight verdict only.

## Verdict

**REVISE.**

[Inferred] The surface is admirably honest and mechanically accessible, but it
does not perform its primary job. A fresh reader can identify a visible
Unknown, yet cannot explain why Butlers exists, what it promises or refuses,
how its architecture and capability groups fit, what V1 success requires, or
where to read a verbatim requirement. Those are the acceptance questions, not
optional detail. Owner attention was not justified at this head: implementation
preflight already had enough evidence to hold the walkthrough gate.

## One-paragraph surface-only explanation

[Observed] From Polaris alone, Butlers appears to be a large software project
for which the current evaluation can list 29 design contracts, 76 modeled
baseline-spec identities, seven craft policies, and five modeled roster
identities, while many other source bodies are excluded. Polaris also drills
into a proposed WhatsApp transport identity-normalization capability and shows
revision, provenance, coverage, and evidence metadata. I cannot explain from
this surface what Butlers is for, what it promises or refuses, how its system
fits together, or what would make V1 successful, because those project-account
fields render Unknown or empty.

The later authority check gives the missing account: Butlers is a one-owner,
self-controlled personal AI system of long-running domain daemons. A
Switchboard routes triggers to specialist butlers; deterministic daemon
infrastructure spawns ephemeral LLM sessions; staffers provide shared
infrastructure; modules add tools; connectors isolate transport; and a shared
PostgreSQL instance uses per-butler schemas. Its success is reliable absorption
of recurring mental labour, not feature count. That account is present in the
exact Butlers tree (`about/README.md:3-7`,
`about/heart-and-soul/vision.md:3-29,31-53,120-137`, and
`about/heart-and-soul/architecture.md` at the reviewed revision), but Polaris
does not surface it.

## Complete RFC7-30 / PWB-REQ-021 prompt record

These are reader answers, not an owner judgment.

1. **Why does Butlers exist? — Unable from Polaris.** [Observed] `Purpose`
   renders `Unknown — missing-declaration` with no project statement. The exact
   Butlers authority says it handles recurring mental labour for one owner
   while preserving ownership of the instance, data, credentials, and agents
   (`about/heart-and-soul/vision.md:3-13`).

2. **What does it promise? — Unable from Polaris.** [Observed] `Promises`
   renders the same Unknown. The authority promises reliable scheduled and
   routed assistance, maintained life-domain context, useful proactive insight,
   and operation boring enough that the owner stops thinking about the system
   (`about/heart-and-soul/vision.md:120-137`).

3. **What does it refuse to be; can I reach one rule? — Unable from
   Polaris.** [Observed] `Refusals` is Unknown and `Non-negotiable rules` says
   no admitted source declares the class. No rule text is reachable. The exact
   authority names five non-goals, including not being SaaS, a chatbot, or a
   monolithic agent, and seven binding rules
   (`about/heart-and-soul/vision.md`, lines 31-118).

4. **What are the major capabilities and how do they fit? — Unable from
   Polaris.** [Observed] The surface lists many RFC/spec names and only five
   readable roster identities, but supplies no usable capability grouping or
   relationship account. `Architecture` is Unknown and `Components` is
   excluded. The exact V1 authority groups core infrastructure, three staffers,
   nine domain butlers, modules, connectors, dashboard, identity, situational
   awareness, and observability; the architecture connects them through
   trigger → classify → route → spawn → act → log
   (`about/heart-and-soul/v1.md:6-174` and
   `about/heart-and-soul/architecture.md`, `The Core Loop`).

5. **Where does exactness live; can I reach a verbatim requirement leaf? —
   Unable.** [Observed] Polaris labels design-contract and baseline-spec paths,
   but all 298 content links are same-page fragments. The selected capability's
   `Requirement and scenario text` is explicitly not rendered, so no verbatim
   requirement leaf can be read from the live surface.

6. **Name one current Unknown or contradiction with its source and how it is
   shown. — Answerable.** [Observed] `Components` is Unknown because
   `about/lay-and-land/components.md` was excluded as active content. Polaris
   shows it in amber with `? Unknown`, the reason `excluded-content`, the source
   path, and a stated route. This is the one complete cold-open answer.

7. **For one fact, how strongly does Polaris know it and what would make it
   stronger? — Unable without guessing.** [Observed] A design-contract entry is
   labeled `Observed · report-fact · fresh · unchallenged`, but only `Observed`
   is explained. The surface does not define `report-fact`, the tier ordering,
   freshness semantics, or a strengthening route. Choosing `Purpose` instead
   yields `Unknown · unstated · fresh · unchallenged` and says owner drafting
   would strengthen it, but the authority check proves the declaration already
   exists. RFC7-30 explicitly makes this vocabulary-comprehension prompt
   load-bearing.

8. **Explain the major architecture and capability groups. — Unable from
   Polaris.** [Observed] This PWB addition fails for the same concrete reason as
   prompt 4: the architecture statement, topology component body, and V1 group
   declarations are not available in the account.

9. **Explain the V1 success criteria. — Unable from Polaris.** [Observed]
   `V1 success` is Unknown and `Success criteria` says no admitted source
   declares the class. The exact authority contains eight criteria, including
   all staffers and nine domain butlers running together, >90% routing accuracy
   over the named active connector set, reliable schedules, working memory and
   dashboard visibility, seven days without manual intervention beyond key
   rotation, daily owner use across three domains, and sustainably adaptive
   proactive insight (`about/heart-and-soul/v1.md:207-232`).

[Observed] Result: one prompt is answerable, one exposes honest but
uninterpretable carrier labels, and the remaining project-comprehension prompts
are unavailable. This triggers PWB-REQ-021's explicit falsifiers: the reader
cannot explain Butlers as a whole and cannot reach exact intent.

## Findings

### PWB-UX-1 — BLOCKER — The observer omits the authority that contains the project account

[Observed] The first four project groups are present in heading order, but
their content is absent: purpose, promises, refusals, architecture, V1 scope,
and V1 success all render `Unknown — missing-declaration`; the rules, success
criteria, and declared-project catalog have zero admitted items. The page
reports 122 of 256 sources readable, 133 exclusions, six
`missing-declaration` claims, and 141 `excluded-content` claims. No
`heart-and-soul` path appears anywhere in the rendered source population.

[Observed] That absence contradicts the exact governed project. Butlers'
`about/README.md:15-21` names all five pillars and points Heart and Soul's
start link at `heart-and-soul/vision.md`; the repository contains
`about/heart-and-soul/README.md`, whose index names `vision.md`,
`architecture.md`, and `v1.md`. Those bodies contain every missing top-level
answer and have no active-content form under the implementation's own scan.

[Inferred] The direct implementation cause is the root-discovery assumption at
`packages/three-surface-poc-core/src/project-shape-manifest.ts:333-338`: a
non-README link is treated as the root itself, so the real
`heart-and-soul/vision.md` start link produces key `vision.md` and is rejected
instead of resolving the named `about/heart-and-soul/` directory. The fixture
at `project-shape-manifest.test.ts:70-99` gives Heart and Soul a separate
directory/README link that the real index does not have, so it does not falsify
this integration shape.

Supporting evidence checked:

- [Observed] Live visual and nonvisual outputs independently contain the six
  missing project statements and no Heart-and-Soul source row.
- [Observed] Exact-revision Git objects contain the omitted index and answers.
- [Observed] The implementation and fixture have the path-shape mismatch above.
- [Observed] The title still claims `Butlers, as it declares itself`, and the
  capability scope says `complete catalog above`, despite omission of the
  declaration layer that owns the account and V1 groups.

Contradictory/mitigating evidence checked:

- [Observed] Polaris does not turn the missing material green or silently fill
  it. Unknown is explicit, reasoned, and consistently encoded, satisfying the
  most important VIS-2 failure posture.
- [Observed] Three unaffected catalog families remain useful: design
  contracts, readable baseline specs, and craft policies carry source anchors
  and exact revision stamps.
- [Observed] RFC7-31 permits an honestly thin read of an undeclared project,
  but this mitigation does not apply: the exact Butlers project is declared and
  its declarations are present at the evaluated revision.

Classification: **implementation fix in the current authorized outcome.** Make
root-index discovery understand the signed grammar and the real table shape;
add a real-format integration fixture; preserve the closed source boundary and
fail-closed behavior. No signed-spec, policy, or owner decision is needed to
observe already-consented declared-project-shape text. Redefining the source
grammar or accepting a cold-open without these answers would instead require a
signed-spec/owner gate.

### PWB-UX-2 — BLOCKER — “Exact source” never reaches exact requirement text

[Observed] The depth guide promises `Exact source`, but the live page contains
302 links: 298 same-page fragments and four surface routes, with no link to an
artifact body. A source citation moves focus to a ledger row carrying path,
digest, outcome, and item count; it does not open the identified artifact. In
the one capability deep dive, `Current authority` and `Requirement and scenario
text` are Unknown, and no verbatim bytes are present.

[Observed] This is not only the current excluded-body outcome. Production route
construction calls `renderPolarisPage` without a verbatim reader
(`apps/three-surface-poc/src/routes.ts:105-120,137`), and the renderer documents
that production passes none (`polaris.ts:922-929`).
`capability-detail.ts:165-170` consequently classifies an otherwise identified
leaf as outside the consented content class. Tests prove that an injected reader
can render exact bytes, but the live path never supplies one
(`polaris-capability-detail.test.ts:193-228`).

Supporting evidence checked:

- [Observed] The live deep dive contains no verbatim leaf and says the selected
  baseline spec is unavailable in the modeled subset.
- [Observed] Link enumeration found no non-surface route or external artifact
  target; every source link ends at metadata on the same 122,899-pixel page.
- [Observed] RFC7-30 requires reaching a verbatim requirement leaf, and
  PWB-REQ-011 requires exact requirement text to remain reachable.

Contradictory/mitigating evidence checked:

- [Observed] All 298 fragment activations resolve to real targets and preserve
  keyboard continuation; there are no dangling in-page paths.
- [Observed] The absence is disclosed as Unknown rather than replaced with a
  paraphrase, so the authority boundary remains honest.
- [Observed] The render-time identity check and test seam demonstrate a safe
  exact-byte mechanism exists; the defect is that the live production path
  cannot use it.

Classification: **implementation obligation, with a conditional owner gate.**
First determine whether the already-discovered baseline requirement body is
inside the performed `declared-project-shape-text` consent and can be supplied
through the existing exact-object/classification boundary. If yes, wire the
live path without storing or copying normative text. If making it reachable
would require broadening consent, weakening active-content/secret handling, or
changing the signed PWB behavior, stop at the security/spec owner gate. Do not
waive the cold-open prompt in implementation.

### PWB-UX-3 — HIGH — The hierarchy is clear, but the useful story is buried under its index

[Observed] The response is 1,069,549 bytes on loopback and 1,069,609 bytes on
tailnet. Its nonvisual text is 12,190 words over 3,513 lines. At a
1280×1923 browser viewport the document is 122,899 pixels tall, about 64
viewports. The project catalog begins at 4,000px; the capability at 21,727px;
Evidence and gaps at 26,695px; the 256-row source table then runs from 27,462px
to 111,497px before 133 expanded exclusion bullets. Only ten compact coverage
count disclosures are collapsed; the exhaustive catalog/source/exclusion
populations are open by default.

[Observed] First glance is consequently about Polaris itself, not Butlers. The
desktop fold is dominated by the hero, surface navigation, epistemic legend,
provenance notice, and four-level depth guide. The narrow-screen fold contains
only that scaffolding. The first owner-facing string is the self-referential
`Butlers, as it declares itself`; the lede narrates order (`Purpose, promises,
boundaries... first; then...`) rather than saying what Butlers is. This meets the
mechanical word-count rubric but still fails the independent comprehension
criterion that PWB-REQ-012 explicitly leaves to PWB-REQ-021.

Supporting evidence checked:

- [Observed] Visual screenshots at 1440px and 500px wide show no project meaning
  before the navigation/legend/depth scaffolding; the mobile fold does not reach
  the first project statement.
- [Observed] DOM geometry and the plain-text output independently establish the
  size and ordering above.
- [Inferred] An owner who follows document order must cross exhaustive inventory
  walls before reaching the capability or final gap summary; this conflicts
  with PWB-REQ-011's progressively deeper levels and the design bar's calibrated
  density bias.

Contradictory/mitigating evidence checked:

- [Observed] The H1→H2→H3 structure is coherent, headings are short, the four
  depths are explicitly indexed, and native fragment links let an informed
  reader skip directly to each target.
- [Observed] Transport is fast despite response size: three loopback requests
  completed in 15–31ms and three tailnet requests in 62–64ms. This is an
  information-friction defect, not a dead-wait defect.
- [Observed] Typography, spacing, color semantics, and visual hierarchy are
  consistent with the declared shared tokens.

Classification: **implementation UX fix.** Put a source-derived, one-sentence
project account in the hero/first reading level; keep exhaustive populations
available behind native disclosures or dedicated deeper routes; lead with the
few groups/relationships needed for comprehension; retain SSR, parity markers,
and complete keyboard reachability. No policy or signed-spec change is needed.

### PWB-UX-4 — HIGH — Resolution copy sends the owner to the wrong gate

[Observed] The six missing project statements all say `Route: First-pass
drafting for owner sign-off`. The generic route comes from
`UNKNOWN_REASON_ROUTES['missing-declaration']`
(`packages/three-surface-poc-core/src/project-shape-model.ts:79-95`), while
`projectAccountOf` falls back to that reason when no account source entered the
model (`project-shape-model.ts:400-425`). Here the exact declarations already
exist; the owner cannot repair an observer discovery defect by drafting them
again. The same surface repeats `Policy change by the owner, or accept the
exclusion` for 141 claims before distinguishing whether the immediate failure
is policy, parser, or discovery.

Supporting evidence checked:

- [Observed] Exact Butlers authority contains the purpose, refusals, rules, V1
  scope, and success criteria that Polaris labels missing.
- [Observed] Heart-and-Soul's relevant files contain no active-content form, so
  their omission is not repaired by changing the secret policy.
- [Observed] The page offers no action beyond linking the reason to the final
  two-row Unknown summary; it does not expose the upstream pillar-discovery
  failure or a repair-observer route.

Contradictory/mitigating evidence checked:

- [Observed] Every Unknown has visible reason text, and genuinely excluded
  artifacts do disclose policy identity, detector/reason, digest, and withheld
  body; for those cases, owner policy review may be a truthful option.
- [Observed] The page correctly carries `no-run-record` and
  `unknown-never-met`; it does not claim that the owner has judged or approved
  the walkthrough.
- [Observed] The reason links are keyboard-operable and resolve; the problem is
  their diagnosis and next step, not discoverability of the label.

Classification: **implementation fix.** Preserve the upstream discovery or
observer failure when it causes an empty class and route it through the existing
observer-repair vocabulary instead of converting it to a missing project
declaration. If a new closed reason or a policy change is genuinely required,
that semantic change returns to the signed-spec/policy owner gate.

## Accessibility, actions, routes, and visual language

[Observed] The strongest part of the surface is mechanical accessibility. A
real-browser sweep of the exact loopback page reached all 317 focusable elements
in forward document order and in reverse; activated all 298 fragment links;
found 16,804 non-ignored accessibility-tree nodes, including 302 named links
and 50 named headings; and found no unnamed target, focus trap, missing fragment,
or pointer-only control. It measured 7,792 rendered text samples; the minimum
contrast was 4.69:1 against a 4.5:1 threshold. The visible focus outline,
skip link, native `summary` controls, text labels, and Observed/Unknown symbols
make state recoverable without color.

[Observed] All four human route links returned HTTP 200 at both loopback and
tailnet. Normalized plain text from the two Polaris ingresses was byte-identical
(SHA-256 `4598ff1f72aca7176d1bfb880de4b0047b799c7d09b22451ef219a6406d0a5ef`),
and the tailnet hrefs retained the mount prefix. No action in this Polaris page
mutates state; repetition and destructive-recovery concerns are therefore not
applicable.

[Observed] The visual vocabulary is consistent and restrained: cyan Observed,
amber Unknown, serif narrative type, monospaced evidence mechanics, and no
decorative motion. The legend text matches the live encodings. There is no
diagram on Polaris; none is required by the signed PWB slice, so the selected
prompt's diagram checks are not applicable rather than failed. `Polaris` is
only a route/eyebrow label and the H1 names Butlers, so the metaphor is not the
primary comprehension obstacle. The obstacle is missing project meaning.

[Observed] I found no grand marketing claim or invented positive status. The
unsupported phrases are narrower but consequential: `as it declares itself`,
`complete catalog above`, and `Exact source` overstate what this particular
render makes available.

## Adapted overview-prompt coverage

- **Comprehension — fail.** Only the required Unknown example is fully
  answerable; the project account and V1 success are not.
- **Narrative — fail.** The intended why → boundaries → architecture → V1 →
  catalog → capability order exists as headings, but the first four groups have
  no project meaning and the exhaustive catalogs dominate the flow.
- **Accuracy — fail.** Unknown polarity is accurate, but the missing-declaration
  diagnosis, owner-drafting route, `complete catalog`, and `Exact source`
  framing disagree with the exact tree or live affordance.
- **Jargon — fail.** `report-fact`, `unstated`, `fresh`, `unchallenged`,
  `owner-adopted (bootstrap, uncorrelated)`, and the evaluation identifiers are
  exposed without a plain-language account of strength or progression.
- **Marketing — pass.** There is no unsupported health, alignment, completion,
  or autonomy claim; the problems are scope and affordance overstatements.
- **Diagrams — not applicable.** Polaris renders none, and the signed PWB slice
  does not require one.
- **Information density — fail.** Exhaustive inventories are present by
  default in one approximately 64-viewport response.
- **Navigation — mixed.** Every in-page link and surface route resolves and is
  keyboard-operable, but an `Exact source` target is only an internal metadata
  row and no verbatim requirement is reachable.
- **Metaphor — pass.** `Polaris` does not force the reader to learn additional
  private vocabulary before seeing the Butlers H1.
- **Accessibility — mechanical pass, comprehension fail.** Keyboard, focus,
  accessible-name, contrast, reduced-motion CSS, and legend mechanics hold;
  nonvisual access faithfully exposes the same missing account.

## Questions still unanswered from Polaris

- What recurring owner problem is Butlers meant to solve?
- What does it promise, and what is explicitly outside its identity?
- How do staffers, domain butlers, modules, connectors, the dashboard, and the
  shared data plane work together?
- Which V1 groups and success criteria are authoritative at this revision?
- What does `report-fact` mean relative to the other epistemic tiers, and what
  concrete evidence would raise a chosen claim?
- How can a reader open an exact requirement rather than its source-ledger row?
- Which Unknowns need owner policy, and which need an observer/parser repair?

## Owner-attention gate

[Inferred] **Owner attention was not justified at this head.** This is a
preflight routing conclusion, not an owner judgment. The implementation can
already falsify the requested walkthrough: mandatory project fields are empty,
the exact-requirement path has no live reader, and the claimed resolution route
misidentifies existing declarations as authoring work. The next action is an
implementation repair and fresh independent confirmation. An owner should be
asked to judge comprehension only after those blockers are absent; owner input
is needed earlier only if the repair genuinely requires changing the signed
content class, security policy, or PWB behavior.

## Concrete edits in priority order

1. Repair real-format five-pillar discovery and add an exact-shape regression
   fixture; re-observe the same Butlers revision and verify the six project
   statements, rules, V1 groups, and success criteria are populated.
2. Make one exact current requirement leaf reachable in the live production
   flow through the existing consented, digest-checked, inert-text boundary; if
   that boundary does not authorize it, stop for the explicit owner gate.
3. Replace the hero's reading-order narration with a short source-derived
   Butlers account; retain one compact scope/Unknown disclosure beneath it.
4. Collapse or route exhaustive catalog/source/exclusion populations so summary,
   catalog, detail, and exact-source are genuinely progressive rather than one
   123k-pixel document.
5. Explain the complete claim-strength tuple in ordinary language at point of
   use and state a truthful strengthening route for the chosen fact.
6. Preserve upstream observer/discovery failures in owner-facing resolution
   copy; do not route existing declarations to new drafting or every exclusion
   to policy change.
7. Re-run this same cold-open and nonvisual/keyboard preflight at the repaired
   exact head. Only then ask the owner to perform the separate judgment.

No implementation, signed specification, policy, owner-decision, Beads state,
or external project state was changed by this review.

VERDICT: REVISE
