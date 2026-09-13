# Manifesto experience — candidate review rubric

Proposed evaluation guidance for REQ-polaris-generation-006/012/014; not a
performed review, owner verdict, specification adoption or implementation grant.

[Observed] The owner identifies a beautiful, intuitive manifesto page as part of
application success. The requested reading begins with a core introduction and
uses contents and glossaries where they help. The reported failures are walls of
text, visible Markdown syntax, an oversized scrolling navigation block, and RFC
references and generic sections dominating the account of the project.

## The experience to evaluate

A newcomer opens the page and understands why this particular project exists.
The introduction leads into a coherent argument: the problem, the project's
response, its important choices, and how its capabilities serve that purpose.
The reader can choose greater depth without losing their place or having to
learn Syzygy's governance vocabulary first.

For Butlers, the owner's stated purpose is to alleviate the mental load of
day-to-day living across the domains the owner chooses to grant it. This is
direction for its project account, not a reusable slogan to insert into other
projects or a claim that the source-adoption process has been completed.

The design retains the existing shared visual language and epistemic meanings
(POC-REQ-060). Project-specific composition must not change the meaning of a
status. The argued account, progressive disclosure, exact intent and nonvisual
paths remain subject to RFC7-1, RFC7-13..16 and RFC7-33/34.

## Review the rendered page

Freeze the project-specific questions and blocking criteria before drafting in
the product evaluation, as required by REQ-polaris-generation-014. Use this
rubric to prepare that review; do not let the generator grade its own output.

| Dimension | Evidence of success | Blocking counterexample |
|---|---|---|
| Introduction | A cold reader explains the supported purpose, intended beneficiary and central thesis in their own words. | The reader must open a catalog or RFC to discover why the project exists. |
| Argument | Sections build on one another; the reader connects major capabilities to the purpose and understands material choices. | Renamed source headings, disconnected summaries or generic marketing copy substitute for an explanation. |
| Concision | Paragraphs each develop a useful point; headings expose the argument; material qualifications remain available. | Repeated summaries and undifferentiated text make the reader hunt or reread, or shortening removes a material qualification. |
| Composition | Typography, line length, spacing and supporting visuals produce a deliberate, readable composition across the full page. | A technically correct page remains visually unfinished, monotonous or hard to scan; a polished hero disguises a dense lower page. |
| Navigation | Contents appear when useful, fit the viewport, and lead to meaningful sections; readers can follow a deep link and return. | Persistent navigation obscures prose or consumes enough space to impede reading; required targets are unreachable. |
| Terminology | Unfamiliar project terms are explained in context or through a discoverable glossary where needed. | Understanding the introduction requires prior knowledge of internal abbreviations or governance vocabulary. |
| Boundaries | Supported limits and trade-offs are explained where they clarify the thesis and capability choices. | A canned “What it is not / Refusals” section dominates the opening or invents exclusions; removing it also removes material limits. |
| Rendering | Intended headings, paragraphs, lists, links and tables have usable semantics; literal source text remains literal on exact-source routes. | Markdown intended as presentation appears as raw syntax, or formatting corrupts exact normative text. |
| Depth and evidence | Supporting material and exact sources are discoverable; uncertainty and required state distinctions remain legible. | References dominate the default narrative, or polishing hides Unknowns, contradictions or source access. |
| Accessible use | The same required reading paths work on narrow and wide screens, at browser zoom, by keyboard and without visual layout cues. | Clipping, lost focus, color-only meaning or pointer-only controls prevent comprehension or navigation. |

Reviewers record aesthetic judgment explicitly, with the affected view and an
explanation. There is no invented numeric beauty score or universal paragraph
limit. A reviewer identifying a blocking composition defect leaves quality unmet
even when the functional checks pass. Passing this rubric does not manufacture
the owner's comprehension verdict or adoption act.

## Retain evidence and repeat after repair

Capture the introduction, representative middle and deepest reading, navigation
states, and narrow/wide layouts from the actual generated output. Retain reader
answers and attempted paths, reviewer findings, artifact identities, viewport and
input method, dispositions and the fresh review of repaired output. Screenshots
support visual judgment; actual interaction supplies navigation evidence.

Evaluate both separately admitted real project domains with the unchanged
generator and repeat after source changes. A hand-curated Butlers page, a fixed
template, source-only CSS inspection or a successful provider response does not
establish reusable manifesto quality. Existing records remain records of their
original bytes; they are not rewritten as passing evidence for a repaired page.
