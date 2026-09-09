# Independent reading-assets code and source-fidelity review

Review date: 2026-09-10.
Subject: implementation commit `0c000368dea293e4c75bb5d8928e9ab2a4e6489c`, compared with `79828ef`.

Verdict: **PASS within the reviewed code and source-fidelity scope.**

[Inferred] No blocking defect was found in the new sidebar, architecture
relationship/flow visuals, source-bound chapter partition, or framing copy.
This is an independent implementation review, not owner judgment, an owner
act, generator completion, deployment approval, or a complete accessibility
walkthrough verdict. No implementation files were edited.

## Governing criteria

PWB-REQ-010 requires the whole-project account before capability detail.
PWB-REQ-011 requires progressively reachable reading levels preserving a true
coarser account. PWB-REQ-012 governs copy roles and limits. PWB-REQ-014 keeps
narrative anchored, non-authoritative and personal view state outside truth.
PWB-REQ-016 requires textual and keyboard access. PWB-REQ-020 requires
human/machine fact parity. RFC7-28 requires that each named diagram element
“carries an anchor or a non-normative/proposed marking” and that curated
provenance be machine-readable, with a text equivalent. VIS-1 places truth
before comprehension; VIS-2 forbids evidence-free success; VIS-7 requires
faithful encodings and resolving internal links. The governing clauses were
read directly from the adopted specification and contract/doctrine files.
The heart-and-soul and engineering-bar skills guided this review.

## Source boundary and independent inspection

[Observed] The only project source body inspected was the previously admitted
local model identified by the coordinator-provided locator. Its entire input
was hashed before JSON parsing or source inspection:

- Input bytes: 5,396,402.
- Input SHA-256: `8e9981a77ad7ef728ae5e466edeaa3376fcb914c1ce6204e4e673c325fd8b6a6`.
- Architecture declaration SHA-256: `b6a02d08b19dbd0dee09f15076494fa6bbe4346e6009e07dff28c01fa2b5036c`.

No external repository bodies or network destinations were opened. Source
passages are deliberately absent from this report; offsets below are zero-based
half-open declaration offsets, which coincide with byte offsets for this
21,805-byte declaration.

[Observed] The ten chapter ranges form a contiguous partition from 0 through
21,805. Rejoining each extracted title, its two source newlines, and its body
reproduced the full declaration exactly. This was checked against the actual
admitted source, independently of the synthetic partition test. The guards in
`apps/three-surface-poc/src/polaris-reading.ts:60` reject gaps, duplicate IDs,
invalid heading delimiters and incomplete final coverage.

[Observed] All three relationship captions preserve their complete source
bodies: [1310,1453), [1453,1593), [1593,1721). Their concatenation exactly
reproduced all 411 bytes of [1310,1721), SHA-256
`21fd727f631d660c755ef13522d51fbd24e1ac51e959148603effcd39156b230`.
The named endpoints are exact subspans of those same bodies. Independent
semantic inspection found each plotted direction supported, including the
restriction on direct peer interaction and the qualification on future clients.
These qualifications remain in visible captions, rather than being relegated
to the complete declaration. The six-node flow at [19266,19330) preserves the
source order and directed separators. No new architectural edge is inferred.

## Rendering and trust boundary

[Observed] `polaris-markdown.ts:101` assigns every named visual element either
a canonical source-anchor reference or an explicit non-normative mark.
`polaris.ts:503` supplies the declaration anchor only when its block has exactly
one anchor. All 12 named elements in the retained-model render had anchor
references. The relationship and flow containers declare curated provenance
at `polaris-markdown.ts:112` and `polaris-markdown.ts:126`. The flow is an
ordered text list, and each relationship retains its full textual explanation;
meaning is not supplied only by arrow position or color.

[Observed] The new JSON fence is parsed strictly as data, with a closed key
set and bounded rows/strings (`polaris-markdown.ts:115`). Endpoint labels are
HTML-escaped and descriptions use the existing inert Markdown renderer.
Unsupported graphs and malformed payloads remain literal code. The existing
renderer strips active link destinations and escapes source HTML. No new
source-controlled script, URL, event handler or style interpolation is added;
flow-column interpolation uses the validated node count. Recursion retains
the existing depth bound.

[Observed] Chapter IDs sit on an outer section, outside its disclosure
(`polaris.ts:492`). The navigation script opens that section's disclosure
before or upon fragment navigation (`polaris.ts:1205`). It changes disclosure
state and `aria-current`/`aria-expanded` only. It neither writes the model nor
changes anchors, claim labels, authority or evaluation state. Rendering the
retained model preserved its serialized value exactly.

[Observed] The source digest gate at `polaris-reading.ts:35` invalidates both
the condensed summary and chapters after source drift. An independent probe
appended a new qualification to the admitted declaration: the complete text
rendered, the qualification remained present, and both chapter IDs and sidebar
chapter links disappeared. `polaris.ts:1485` derives the sidebar chapters
through the same guarded reading plan, avoiding stale navigation after drift.

[Observed] An HTMLParser sweep over the retained-model render counted 340 DOM
IDs and 680 fragment links. There were no duplicate DOM IDs or dangling
fragment targets in those populations. Independent whitespace-anchored
attribute scans confirmed both denominators. A preliminary word-boundary
regex was discarded because it incorrectly included data attributes as DOM
IDs. Repeated links to a shared target are valid and were not called duplicate
identities. Browser operation and mounted live-source routes are covered by
the coordinator's separate run, not claimed by this static capture sweep.

[Observed] The new framing lede remains explicitly non-normative,
presentation-only and non-citable in `page-shell.ts:60`; it asserts neither an
implemented capability nor acceptance. The whole-project heading order is
unchanged. The sidebar retains summary/catalog/detail/source destinations.

## Executed verification and limits

[Observed] The following targeted command completed with four passing test
files and 33 passing tests:

```sh
npx vitest run apps/three-surface-poc/src/polaris-reading.test.ts apps/three-surface-poc/src/polaris-markdown.test.ts apps/three-surface-poc/src/polaris-narrative.test.ts apps/three-surface-poc/src/polaris-copy.test.ts
```

The tests exercise partition failure cases, source drift, invalid selections,
inert payloads, diagram anchoring, narrative-state separation, and copy roles.
The actual-source partition/caption checks, fragment sweep, and model/drift
probes described above were additionally executed against the retained local
capture and the subject worktree's built renderer.

[Unknown] This review does not establish the complete project's governance
battery, release readiness, a fresh source evaluation, owner comprehension,
or completion of PWB-REQ-016's required cold-open walkthrough. Those claims
require their separate evidence and the applicable owner judgment. Source-plan
metadata remains curated and digest-specific; a future source revision
correctly loses the curated chapter/diagram presentation until independently
reviewed metadata is supplied.
