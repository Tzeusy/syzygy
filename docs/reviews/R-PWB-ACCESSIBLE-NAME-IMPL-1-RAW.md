# R-PWB-ACCESSIBLE-NAME-IMPL-1 — code review, syzygy-u05.22
Reviewed commit: b1218a648a2d2af2ba60a3ccc363ae11c26be872
Scope: diff origin/main..b1218a648a2d2af2ba60a3ccc363ae11c26be872 against pwb-accessible-name-amendment v1.0 (PWB-REQ-016)
Verdict: CONFIRM WITH EXCEPTIONS

## Basis

- [Observed] The supplied two-dot diff (3,603 lines, 47 files) contains about 33 governance/openspec/docs files that are changes on `origin/main`, not on this branch: `origin/main` is 11 commits ahead of the merge base `72a16236`. The branch's own changes are its three commits `cb0d0a1d`, `dad36563` and `b1218a64`: 14 files, +1320/−23 (`git diff --stat 72a16236 HEAD`). I reviewed those 14 files. The rest of the diff is out of scope (Finding 8).
- [Observed] `npx vitest run apps/three-surface-poc/src/polaris-accessible-names.browser.test.ts` at the worktree HEAD reported 26 passed (26), with the browser suites running, not skipped. The 404 `unknown-route` lines in the daemon log have `pathLength` 12, which matches the browser's `/favicon.ico` probe [Inferred].
- [Observed] Scope bounds hold. No file under `packages/three-surface-poc-core/` changed. The renderer changes are in `polaris.ts`, `polaris-markdown.ts`, `surface-links.ts` and `unknown-marker.ts`. The `nameForm` parameter is opt-in and only `polaris.ts` call sites pass it. `materialize-action.ts:108` (Trajectory) and every other non-Polaris `crossSurfaceLink` caller keep the old `Read X on Y` name. `renderPolarisMarkdown` is called only from `polaris.ts`. The sweep driver (`polaris-accessible-names-main.ts`) fetches only `--base-url`, and `main.ts` does not import it. The record it writes holds counts only, plus sha256 of the source identities.
- [Observed] Mapping of the signed text to the oracle:
  - Interactive population (`a[href], area[href], button, summary, input, select, textarea`): closed `details` included; `hidden`, `aria-hidden="true"` and computed `display:none` excluded, each checked on the element and its ancestors (`polaris-accessible-names.ts:34-43`).
  - Targets: resolved `href`; the summary's parent `details`; `aria-controls`, else the element itself (`:62-84`).
  - Visible label: `textContent`, each whitespace run collapsed to one space, ends trimmed.
  - Name rules: grouping by name across targets; grouping by label limited to groups with two or more targets; `startsWith(label)`; the path searched only in `name.slice(label.length)` (`:178-213`).
  - Heading rules: `h1`–`h6` at their own level and `role="heading"` at `aria-level`, with the same exclusions; exactly one level-1 heading; a step deeper than +1 fails (`:87-96`, `:216-230`).
  - Page list: from `projectShape.sources` in the machine answer; a page not served is a violation, never a skip; coverage is checked in both directions (`:249-264`, `:313-337`).
  - Names come from CDP `Accessibility.getPartialAXTree` for each held DOM node (`cdp-browser.ts:224-241`), not from page script.
  - I found no over-reach against the signed text. The under-reach edges are Findings 3, 4 and 7.
- [Observed] Every falsifier limb has a mutant that the test run kills. The record (`docs/evidence/pwb-p99-accessible-names-mutation-run-2026-10-15.json`, commit `dad36563`, 28/28 killed, with the `old`/`new` fragment stored for each mutant) includes:
  - `shared-name-different-targets`
  - `heading-level-skipped`
  - `second-level-one-heading`
  - `page-list-from-machine-answer`
  - `every-listed-page-swept`
  - `coverage-page-not-swept`
  - `page-not-served`
  - each population exclusion
  - `names-computed-with-disclosures-open`
  - three renderer repairs
- [Observed] Commit `b1218a64` touches only evidence. Commit `dad36563` touches only the test file. The oracle source the sweep ran at `cb0d0a1d` is therefore the same as at HEAD.

## Findings

**Finding 1 — The live whole-surface sweep covered the entry page only; the exact-source populations and the path limb are unmeasured on Butlers** (note)

Anchors: `docs/evidence/pwb-p99-accessible-names-sweep-2026-10-15.json` (`shape: "not-admitted"`, `pagesListed: 1`, `exactSourceTargetsInSharedLabelGroups: 0`); `docs/evidence/pwb-p99-polaris-size-measurement-2026-10-15.json` (`liveEvaluation.gateFinding`, `observedShapeOnButlers`).

- [Observed] The live evaluation at Butlers `36f0e0eb` was not admitted, because the policy act's recording tag does not resolve. The machine answer therefore listed no source, and the sweep ran over 1 page: 85 interactive elements and 35 headings, with 0 violations.
- That meets acceptance criterion 1 literally: every page that evaluation served was swept, and the denominators were checked against the list from the machine answer. But no exact-source route response and no exact-source shared-label target was observed live. The signed `[Unknown]` bullet ("measured on a fresh private-daemon capture at a named commit when this is implemented") is answered only for the not-admitted shape.
- The 2 MB re-measurement (113,689 bytes direct; 113,929 bytes tailnet) is likewise for the not-admitted page. The observed-shape headroom is `[Inferred]` from a 2026-10-03 capture taken at an older Syzygy head.
- [Inferred] There is a latent risk that only an observed live shape would show. `polaris.ts:647` renders a `button.expand-declaration` with no `aria-controls`, so its target is the button itself, and its name is the shared "full account" copy. Two such buttons on one page would share a name across different targets. The fixtures render at most one.
- Repair:
  - Keep this limb open on the bead, or file a follow-up bead, until the sweep and the size measurement are re-run at an admitted, observed evaluation.
  - Say in the bead close note that acceptance criteria 1 and 4 were met at a not-admitted shape.
  - Give `expand-declaration` an `aria-controls`, or a name that includes the reading key, before that run.

**Finding 2 — The comment says the whole-surface fixture test exercises the exact-source path rule, but the test never asserts it** (note)

Anchor: `polaris-accessible-names.browser.test.ts:311-314`.

- The comment says every exact-source link in a shared-label group "carries its source path (the rule is exercised, not vacuous)". The test asserts only `sharedLabelGroups > 0` on the entry page. `exactSourceTargets` is never asserted on any rendered Polaris page.
- The path-limb mutants are killed by the pure cases and by the synthetic `omits` page (`:293-294`). So the rule's logic is tested, but nothing shows that the real renderer produces a shared-label exact-source group at all.
- Read with Finding 1, the path limb has no observed exercise on any Polaris rendering.
- Repair: assert a hand-typed literal for `report.pages[0].exactSourceTargets` (or a per-page literal list) in the observed fixture sweep, and add a mutant that drops the path suffix from the renderer's exact-source link name.

**Finding 3 — An exact-source target whose identity the machine answer does not list passes without comment** (note)

Anchors: `polaris-accessible-names.ts:205-206` and `:170`.

- `if (path === undefined) continue;` treats a shared-label link that routes to an identity outside `sourcePaths` as compliant. `exactSourceIdentity` returns `''` when the identity parameter is missing, which takes the same path.
- The signed text requires the path "the machine answer carries for the source that route serves". When the answer carries none, the honest outcome is Unknown (VIS-2: no evidence is never green), not a pass.
- `exactSourceTargets` still counts the element, so the denominator hides the skip.
- Repair: count these elements separately (for example `exactSourceTargetsWithoutMachinePath`), report the count in the evidence record, and have the driver's exit code treat a non-zero count as not passing.

**Finding 4 — The path is matched as a substring, not as words** (note)

Anchor: `polaris-accessible-names.ts:207`.

- `name.slice(label.length).includes(path)` accepts a name containing `docs/a.md` for a source whose path is `a.md`, and `x/a.md.bak` for `a.md`.
- The signed text says "the words after the label SHALL include the repository-relative path".
- Repair: match on token boundaries, so that the path is preceded by start-of-string or whitespace/punctuation that is not a path character, and followed likewise. Add a pure case where one path is a suffix of another.

**Finding 5 — Opening disclosures before the names are read is an interpretation, and the evidence record does not state it** (note)

Anchors: `polaris-accessible-names.ts:55-59` and `:271-280`.

- The approach is sound in direction.
  - [Observed] Chrome 120 reports `''` for nodes left unrendered inside a closed `details`. Under that reading, every pair of collapsed links with different targets would collide, which the signed population (closed `details` included) cannot intend.
  - The check fails closed: a page script that re-closed disclosures on toggle would produce `''` names, and those would be reported as shared names.
- Two weaknesses:
  - The DOM is mutated before the names are read. The populations (`described`, `held`) are taken before the mutation and aligned only by count, so a toggle listener that changed an `aria-label` would be measured in its post-toggle state.
  - The evidence record does not say the names were computed with every disclosure open.
- Repair: add a `method` field to the sweep record stating that names were computed with all `details` opened after enumeration. Optionally, compare each element's DOM identity before and after opening, not only the counts.

**Finding 6 — Nothing binds the swept pages to the one evaluation the page list came from** (note)

Anchors: `polaris-accessible-names.ts:313-327`; `polaris-accessible-names-main.ts:105-120`.

- The machine answer is fetched once. Each page is then probed by a separate, unauthenticated `fetch` and loaded again by the browser. Nothing checks that the pages render the same `inputsDigest` that the list came from.
- If the daemon re-evaluated mid-sweep, the record would report one evaluation over pages from another.
- Repair: re-fetch the machine answer after the sweep and require the same `evaluation.inputsDigest`, or read the evaluation identity the page carries, if it carries one.

**Finding 7 — Population edge cases the selector does not handle** (note)

Anchor: `polaris-accessible-names.ts:43` and `:68-69`.

- An SVG `<a href>` matches `a[href]`, but its `e.href` is an `SVGAnimatedString`. Every SVG link would then share one target key, `href:[object SVGAnimatedString]`.
- [Observed] Polaris renders no `<svg>` today: 0 occurrences in `polaris.ts`, `polaris-source.ts` and `polaris-markdown.ts`. So this is latent.
- Elements with `role="button"` or `role="link"`, and `tabindex` regions, are not enumerated. That follows the signed list, which names links, buttons, `summary` and form controls. [Observed] The one `tabindex="0"` element Polaris renders, the table-scroll `role="region"` at `polaris.ts:179`, is correctly outside that list.
- Repair: use `e.getAttribute('href')` resolved against `document.baseURI` for non-HTML anchors, or add `:not(svg *)` with a stated reason.

**Finding 8 — The review diff includes main-side changes, and the branch needs a rebase** (note)

Anchor: the supplied `review.diff`.

- The diff includes the reverse of about 33 files changed on `origin/main` since `72a16236`, for example the `cap1-trusted-bootstrap-consent` change, `PENDING-OWNER-DECISIONS.md` and the `docs/reviews/R-CAP1-*` raws. These are not this branch's changes and were not reviewed.
- Repair: rebase onto `origin/main` before merging, re-run the browser test and `check_governance.py` on the rebased tree, and generate future review diffs as `origin/main...HEAD` (three dots) or from the merge base.

**Finding 9 — One whole-surface expectation is derived from the fixture, not written as a literal** (note)

Anchor: `polaris-accessible-names.browser.test.ts:304`.

- The expected identity order comes from `model.projectShape.sources`. That model is the fixture, not the module under test, and the literal 17/17 at `:303` already pins the count. So this is not a vacuity, but it falls short of the hard-coded-literals rule.
- Repair: hard-code the 16 expected identities, or their sha256, as a literal list.

Renderer repairs:

- [Observed] Correct, minimal and confined to Polaris.
  - The heading clamp (`polaris-markdown.ts:183-187`) carries one `HeadingState` through nested quote, list and relations blocks in document order. Each `renderPolarisMarkdown` call starts it at the anchor level.
  - The `### C#` expectation changing from `h6` to `h5` is the signed rule applied to Butlers-declared text, which the signed text expressly does not exempt.
  - The source-remedies `summary` names (`polaris.ts:623`) begin with the visible label and add the claim id and place.
  - The label-first cross-surface name (`surface-links.ts:52`) begins with the visible label.

Findings: 0 revise, 9 note.
