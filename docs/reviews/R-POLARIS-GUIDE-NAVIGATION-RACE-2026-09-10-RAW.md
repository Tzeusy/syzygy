# Independent component-guide navigation race review

Date: 2026-09-10.
Subject: `a0cc75062734466ebb47eed858100778991e0e95`.

Verdict: **PASS within the bounded navigation-race repair scope.**

[Observed] The hosted failure log records one component guide open after the
second collapse action where none was expected. Static inspection identified
two writes for one navigation: the synchronous link click opens the guide,
and a later native hashchange reopens it. The coordinator's retained
pre-repair controlled replay fails with the same one-versus-zero result,
without keyboard focus being involved. It clicks the guide, expands and
collapses in one task, then observes the delayed native navigation event.

[Observed] `apps/three-surface-poc/src/polaris.ts:1212` now records the handled
fragment. Duplicate non-explicit handling of that fragment is ignored;
explicit link activation can always reopen it. Recording every handled hash,
including a non-guide target, preserves subsequent browser-history navigation
back to a guide. The state is private to the DOM script, does not enter the
truth model, and changes no claim, anchor, authority or source boundary.
The synchronous first opening and native fragment navigation remain intact.

[Observed] The browser regression registers a real hashchange listener before
the click and awaits that event after collapse. This exercises the delayed
writer deterministically rather than relying on a timeout or timing gap. The
same test then exercises keyboard activation of the unchanged fragment,
expand/collapse, and navigation to a non-guide fragment followed by Back.

[Observed] Independent targeted execution passed one browser test; twelve
unrelated tests were intentionally excluded by the name filter:

```sh
npx vitest run apps/three-surface-poc/src/polaris-accessibility.browser.test.ts -t 'opens a linked component guide'
```

[Observed] An additional independent browser probe extracted the exact
navigation script from the reviewed source and ran it against a minimal local
HTML fixture with two component guides. Each changed-fragment operation awaited
a pre-registered native hashchange event. Results: the delayed original event
left zero guides open after collapse; explicit same-fragment activation opened
one; leaving the fragment and using Back reopened one; collapsing then using
Forward to the non-guide fragment left zero open. This checks Back and Forward
without relying solely on the author's fixture. No external body or network
destination was opened.

Reviewed file SHA-256 values, checked again after execution:

- `polaris.ts`: `c817d5ae49fa3d203a67870e14441688d626c15391fd69e10b6eeedac379c716`.
- `polaris-accessibility.browser.test.ts`: `2b1aa0c87ef69741122e737bb4fc56d297556a24abfe080268826c647d87a955`.

[Inferred] The fix closes the demonstrated duplicate-write defect without
weakening source reachability or personal-state separation under PWB-REQ-011,
PWB-REQ-014, PWB-REQ-016 and VIS-7. No further finding was identified in this
diff. Prior raw reports remain unchanged.

[Unknown] This report does not establish the new hosted CI outcome, a complete
governance battery, an owner walkthrough verdict, generator completion or
release/deployment approval. Those require their separate evidence.
