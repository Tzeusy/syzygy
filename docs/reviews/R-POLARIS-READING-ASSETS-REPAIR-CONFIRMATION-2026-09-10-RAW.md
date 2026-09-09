# Independent reading-assets repair confirmation

Date: 2026-09-10.
Subject: runtime commit `dd289999d1b6288d0ecf0e8e022240a380b45b5a` plus
uncommitted `apps/three-surface-poc/src/polaris-reachability.test.ts`, SHA-256
`9357718370985df52084eeabdf3b9162e0d1f02fdfe3201982873b63e38bda40`.
The test file was hashed before and after the independent run.

Verdict: **PASS — RRA-1 resolved within the bounded repair scope.**

[Observed] The new `assertDecorativeArrow` helper rejects `tabindex`,
`contenteditable` and `role` attributes on the arrow and its descendants,
including boolean attribute forms. It additionally rejects nested native
interactive elements. The original positioned, aria-hidden, keyboard-focusable
counterexample is now rejected. The helper preserves the required span and
`aria-hidden="true"` checks.

[Observed] The full layout/access guard now includes a model rendered through
the admitted fixture pipeline with explicit flow content. It asserts that two
decorative arrows exist before applying the guard, eliminating a vacuous
success when the general model variants contain no arrows. The absolute/fixed
positioning exception remains restricted to decorative-arrow selectors.
Native buttons retain their required `type="button"`, and the other focus,
hiding, layout-order and keyboard-landmark checks remain intact.

[Observed] The mutation test invokes the same helper used by the full guard.
It rejects three own-attribute cases, three descendant-attribute cases, and a
nested native button; the valid rendered arrow is accepted first. These seven
counterexamples include the precise RRA-1 hidden tab-stop defect and the
boolean editability case. The diff changes test code only; runtime rendering,
source metadata, authority and response limits remain those reviewed at the
subject commit.

[Observed] Independent verification completed successfully:

```sh
npx vitest run apps/three-surface-poc/src/polaris-reachability.test.ts
```

One file and seven tests passed. The prior raw reviews remain unchanged.

[Inferred] The bounded source-record compaction and its corrected reachability
regression guard are acceptable on the evidence reviewed. The test change does
not weaken the meaningful noninteractive-only positioning boundary identified
by RRA-1.

[Unknown] This confirmation does not independently establish the coordinator's
new live-demo results, a complete governance battery, owner comprehension,
generator completion or deployment/release authorization. Those require their
own evidence. No external repository body or network destination was opened.
