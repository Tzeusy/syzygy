# Polaris editorial repair

Status: implementation working record, not an owner walkthrough judgment.
Issue: syzygy-xy1. The prior cold-open remains incomplete after prompt 4.

[Observed] The owner reported walls of text, excessive RFC references,
obstructing depth navigation, unrendered Markdown and a presentation far from
a polished manifesto. At the capabilities-and-fit prompt the owner said it
was hard to tell, and requested several polishing passes producing concise
long-form summaries. The owner subsequently authorized all relevant necessary
improvements and clarified the desired result: a coherent, concise manifesto
beginning with a core introduction, with glossaries and contents where useful.
Beauty and intuitive reading are explicit owner success criteria.

[Observed] This direction is recorded as design intent and repair scope. It
does not record a performed specification amendment or owner judgment.

## Acceptance for this repair

- The first viewport introduces the application before its evidence machinery.
- The account explains purpose, promises, limits, architecture and scope in a
  coherent reading order. Source terms and capability groups aid comprehension.
- Markdown becomes readable semantic HTML without executing source HTML,
  links, images or code. Exact-requirement routes retain their verbatim contract.
- Contents stay in document flow. Expanding them cannot create a scrolling
  overlay; native keyboard navigation and small-screen reading remain usable.
- Shortening is explicitly extractive: complete selected passages retain
  their source identity, and the complete declaration is reachable alongside.
  No generated summary becomes an Observed kernel fact.
- Unknowns, qualifiers, all declared populations, provenance and source routes
  survive. A reviewer checks the rendered account against the admitted source
  model, including whether selected passages mislead by omission.
- Independent design review inspects actual desktop/mobile captures for
  composition, readability, navigation and comprehension. Mechanical checks
  alone cannot satisfy the owner's design success criteria.

## Scope and verification

[Observed] The repair uses the existing PWB implementation authorization and
PWB-REQ-010, 011, 012, 014, 016 and 020. It changes the presentation of the
shared model, with no Butlers writes, new content class, runtime LLM egress,
new truth store or edit to signed artifacts. Captured content stays local.

The quality sequence is source/structure review, implementation, independent
fidelity and visual review, repair, then exact-head confirmation. Run focused
Markdown/reading tests, the existing narrative/parity/reachability checks,
real-browser checks, the full suite and the canonical clone governance battery.
Retain before/after local captures and repository metadata-only evidence.

[Unknown] Owner comprehension and satisfaction with the repaired page remain
unjudged until the owner reads it. The previous readiness reviews remain
historical records and are not evidence that the owner accepted the design.

## Initial passage binding (superseded for the first reading)

The rejected lexical omission rule has been removed. The architecture uses
reviewed complete passages only when the extracted declaration matches its
exact SHA-256. Any changed or unreviewed declaration renders completely.
The plan stores offsets, not source bodies, and has no runtime input channel.

- Plan: apps/three-surface-poc/src/polaris-reading-plan.ts
- Plan file SHA-256: 755d1155d4dd6d61e00695051e2240099909249d0db35fb549c734927c16cdf4
- Extracted declaration SHA-256: b6a02d08b19dbd0dee09f15076494fa6bbe4346e6009e07dff28c01fa2b5036c
- Independent selection review: docs/reviews/R-POLARIS-EDITORIAL-PASSAGES-RAW.md

This binding identifies the retained selection review; changing offsets retires
that review until the new selection has its own independent confirmation.

## Reading hierarchy revision

Independent design review required a shorter core architecture, practical
capabilities before engineering detail, early contents/terminology routes and
compact Unknown disclosure. The V1 project scope is part of the manifesto;
the full capability catalog remains after the architecture, preserving
RFC7-13's primary altitude order.

The primary architecture now uses the separately confirmed core selection.
The V1 account retains its complete deferrals alongside every declared
capability context and complete example member statements. The complete
scope and architecture remain available. New selection metadata and exact
review bindings are in docs/evidence/polaris-editorial-reading-plans-2026-09-09.json.
The current implementation plan file SHA-256 is 7effb17f7f19ddb7d003313d57cba2865fb8558450c8614d2ae2a6da8b046d58.
The original 1,685-word selection confirmation remains historical.
