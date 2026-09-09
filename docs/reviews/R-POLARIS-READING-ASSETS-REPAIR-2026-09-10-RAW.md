# Independent reading-assets repair review

Date: 2026-09-10.
Subject: `dd289999d1b6288d0ecf0e8e022240a380b45b5a` versus
`0c000368dea293e4c75bb5d8928e9ab2a4e6489c`.

Verdict: **CHANGES REQUESTED — one bounded regression-guard gap.**

[Observed] The source-record compaction in
`apps/three-surface-poc/src/polaris.ts:796` retains the identity, canonical
citation and anchor metadata, rule, optional pillar, outcome, source anchor
text, digest or no-body-read disclosure, denominator, claim tuple, exact-source
link and parity markers. Definition-list wrappers become explicit bold labels
with line breaks. This preserves text recoverability under PWB-REQ-016 and
provenance under PWB-REQ-014/020. No policy or response ceiling was changed.
The source-record font rule now applies to the disclosure as a whole.

[Observed] Allowing native `type="button"` controls is a legitimate correction
to the previous blanket prohibition: the expand-declaration control uses a
native button with an existing keyboard/browser test. The positioning
exception is scoped to selectors ending in `.flow-arrow`; mixed selector rules
retain the ban, as do ordinary and pseudo-element selectors. Existing hiding,
focus-outline, reordering and positive-tabindex checks remain.

## Finding RRA-1 — Positioning exemption does not establish noninteractivity

[Observed] At `polaris-reachability.test.ts:358`, the exception verifies a span,
`aria-hidden="true"`, and absence of nested native form/link controls. It does
not reject `tabindex`, `contenteditable`, or interactive roles on the span
itself. The existing global tabindex predicate accepts `tabindex="0"`.
Consequently, a positioned decorative span with `aria-hidden="true"` and
`tabindex="0"` satisfies the new tests while creating a focusable element
hidden from assistive technology. The previous positioning ban would reject
that combination. This is a meaningful PWB-REQ-016 regression-guard gap.

[Observed] A standalone counterexample ran the exact selector-stripping,
nested-control and global-tabindex predicates with that mutated span and an
absolute-positioning `.flow-arrow` rule. All predicates accepted it. No
implementation source was mutated to run the counterexample.

[Inferred] Repair by explicitly rejecting focusability/editability and
interactive roles on the decorative span, including corresponding descendant
cases, and prove the predicate rejects at least the positioned hidden tab-stop
counterexample. The production arrows currently carry none of these
attributes; this finding identifies incomplete regression protection, not an
observed current keyboard defect. It is small and belongs in this repair.

## Verification and limits

[Observed] Independently executed:

```sh
npx vitest run apps/three-surface-poc/src/polaris-reachability.test.ts apps/three-surface-poc/src/polaris-narrative.test.ts apps/three-surface-poc/src/polaris-copy.test.ts
```

Three files and 16 tests passed. Their success does not falsify RRA-1 because
the current renderer does not emit the counterexample attributes.

[Observed] The newly retained demonstration is explicitly bound to the prior
implementation commit and records failure, rather than presenting its result
as evidence for this repair. No old raw review was edited.

[Unknown] The coordinator's new live demo and the reported 15,955-byte savings
were not independently rerun in this review. Successful mounted and direct
serving at the repaired commit remain for that run to establish. This review
is not owner judgment, generator completion, deployment or release approval.
No external repository body or network destination was opened.
