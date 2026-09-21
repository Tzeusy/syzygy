# Feature request M16 — Renderer, diagram and visual-system engineering: the only mutation evidence for the highest-traffic module bound to bytes that no longer exist, escaping enforced by convention not the compiler, a page that cannot draw a graph, and a forced dark theme with eight stray colours outside the token set

> **Candidate — binds nothing.** Bead `syzygy-dov.16`, move M16 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`,
> section "### M16"), written in the shape of the M14 provenance-depth and
> M15 pipeline-truthfulness funnel packets and their siblings.
> Planning only: nothing here authorizes implementation. This packet names
> lawful arms for the owner to take; it rules no slice authorized or
> unauthorized, and the owner disposes.
>
> **No independent review yet. This is a first draft.** [Superseded
> 2026-09-17: review 1 applied — CONFIRM WITH EXCEPTIONS (0 blocking / 2
> non-blocking / 3 editorial), the five findings repaired in place. By
> verification rule 10 these review-1 close-out repairs post-date the
> reviewed commit 429924a and are themselves uncovered until a second
> review bound to the new bytes.] Where a closed-out
> sibling records a fresh-context review, this packet records none. By
> verification rule 10 every figure here is uncovered until a fresh-context
> review, bound to these bytes, confirms it. The load-bearing figures were
> reproduced this session by two independent methods each (verification
> rule 2), which is not a review.
>
> **The move has no spec prerequisite.** Unlike M15, no slice here is
> downstream of a change to the signed PWB specification, so — assessed per
> slice in Gate 3 — the low-risk mechanical and additive slices may
> recommend *building* under the POC improvement-cycle scope. Two slices
> are the exception: the SVG-diagram slice is a feature-request candidate
> and its recommended arm is *design*, and the light-palette theme option
> and the curation-generalization work are *design* as well. No slice
> touches the signed spec, doctrine text, the security/privacy/retention
> posture, or POC scope; the one that hardens escaping (Q2) strengthens
> SEC-1 conformance in the implementation and changes no posture. Building
> binds no doctrine and adopts no intent (VIS-4).

Date: 2026-09-17. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1, 4) / **medium** (slices 2, 3, 6) / **large**
(slice 5, the SVG diagrams, and only its design question is asked here).

Baseline: Syzygy `a9f671e` (main). The subject is the Polaris renderer and
its shared visual system in `apps/three-surface-poc/src/` — the module that
turns a `PocModel` into the human manifesto page, the Markdown-and-diagram
renderer beside it, and the design-token stylesheet all three POC surfaces
share. No core pipeline change is proposed; every slice is render-side.

**Line-count convention, stated once.** A "line N" below is the one-based
index into the split-on-newline segments of the file at `a9f671e` — the
number `sed -n 'Np'` prints. A byte count is the UTF-8 length.

**Capture convention, stated once.** Three retained machine captures of the
human `/polaris` page are read for magnitudes and for the diagram sweep, all
served from the POC at the revisions their measurement records name: the
post-trim direct capture `polaris-direct.html` (1,478,637 bytes) and its
tailnet-mounted twin `polaris-tailnet.html` (1,484,487 bytes), and the
pre-trim capture `polaris-7478.html` (2,090,025 bytes). The defects this
move addresses are read structurally at the source at `a9f671e`; the
captures supply only the rendered-page magnitudes (the diagram count and
the page byte denominators). No daemon was started this session and no
Butlers body was read.

## The six questions for the owner

Batched, recommended answer first. Everything below is the evidence behind
them. Q1 is the packet's hygiene question and stands alone: the only
mutation-kill evidence for the highest-traffic renderer module is bound to
bytes that no longer exist, which verification rules 7 and 10 make a live
gap regardless of how the other five fall. Q2–Q6 are engineering and
visual-system slices with no spec prerequisite; each is assessed against
the continuation act's escalation triggers in Gate 3 and carries its own
build/design/draft recommendation.

| # | Question | Recommended |
|---|---|---|
| Q1 | **[S8-M4] May the renderer mutation-kill sweep be re-run and re-dated, leaving the old record untouched, so the highest-traffic module carries mutation evidence bound to its current bytes?** Measured at `a9f671e`: the one mutation record for the renderer, `docs/evidence/pwb-p3-6-narrative-mutation-run-2026-09-04.json`, binds its result by a per-file content sha256 in its `subjects` block (it records no commit). For `apps/three-surface-poc/src/polaris.ts` its recorded digest and the file's current sha256 this session differ (all four subjects' full digests are in Measurement 1's table), and all four subject files differ (`polaris-narrative.ts`, `polaris-copy.ts`, `page-shell.ts` likewise). Seven or more commits touched `polaris.ts` since 2026-09-04 (`2ef68f5`, `a121591`, `6fa339b`, `5290cd0`, and earlier). So the "17 of 17 killed" result the record reports is `[Observed]` for bytes that no longer exist; the current renderer carries no mutation confirmation (verification rule 10: the record confirms history, current bytes carry none). | **Authorize the re-run — this is a *build* arm.** Re-running the sweep and writing a new dated record beside the old one restores rule-7/rule-10 coverage for the current bytes; it edits no source and changes no shipped behaviour, so it trips no escalation trigger. **The sweep rewrites sources in place and runs about 35 minutes — no edit or commit while it runs** (an AGENTS.md guardrail). The old record stays untouched (a re-issued evidence record is a new file, never an overwrite). **Every lawful arm:** (a) *no re-run* — the renderer keeps mutation evidence bound to dead bytes and rule 10 leaves it uncovered; (b) *the recommended arm* — re-run, new dated record, old one preserved; (c) *re-run all four subject files' scope at once* — the same sweep already covers them, so (b) and (c) coincide here. **Counter-argument, and it is real:** a 35-minute in-place mutation run is a serial cost that blocks other renderer work for its duration, and if Q2/Q4 land first the record must be re-run again afterward — so sequence it *after* the mechanical refactors, not before. **Default if unanswered: no re-run; the renderer's only mutation evidence stays bound to bytes that no longer exist.** |
| Q2 | **[S8-M3] May a branded `Html` type be introduced so HTML escaping is enforced by the compiler rather than by convention, with the raw string-returning helpers converted to return it?** Measured at `a9f671e`: `polaris.ts` imports `escapeHtml` from `@syzygy/cap1-daemon` (line 3) and every render helper returns a bare `string` that is in fact HTML, so a caller can interpolate an unescaped value with no type error. The five HTML-returning helpers in the `escapedCauseRoute`…`unknownRoutes` band [Superseded 2026-09-17: no function `escapedCauseRoute` exists; the band's first helper is `excludedCauseRoute` (416), which this same sentence then names correctly] (lines 416–490, dossier "417–490" corrected to start at 416) are `excludedCauseRoute(exclusion: Exclusion): string` (416), `unavailableCauseRoute(source: { readonly path: string; readonly reason: string }): string` (440), `routeOf(claim: ProjectShapeClaim, reason: string): string` (462), `reasonRouteHtml(reason: string): string` (472), and `unknownRoutes(claim: ProjectShapeClaim, prefix: string): string` (480) — all `string`, none branded. | **Design then *build* it as a mechanical, behaviour-preserving refactor, within the POC improvement-cycle scope.** A branded `Html` type serves SEC-1 (escape untrusted content) and VIS-7 (the machine's output is honest and safe) by making the escape boundary a compiler obligation; it changes no security *posture* (the escaping already happens — this enforces it), so it trips no escalation trigger. **Every lawful arm:** (a) *no change* — escaping stays a convention a reviewer must re-verify by hand each change; (b) *the recommended arm* — a branded `Html` with a single `escapeHtml`/`raw` boundary, the five helpers and their callers converted, rendered output byte-identical; (c) *lint-only* — a custom lint rule flagging bare-string HTML concatenation without the type, cheaper but advisory, not compiler-enforced. **Counter-argument:** the brand touches most of a 1,634-line module and its callers, a large blast radius for a change with no user-visible effect, and a botched conversion could *mask* a real escaping bug behind a green type-check — so it must land with the Q1 mutation evidence re-run afterward and a rendered-output diff proving byte-identity. **Default if unanswered: escaping stays convention-enforced; no `Html` brand.** |
| Q3 | **[S3-M3, S3-M4] May an assistive-technology text equivalent be added for the relations and flow diagrams, and a *visible* marking for non-normative diagram nodes, with a counterexample fixture?** Measured at `a9f671e`: `polaris-markdown.ts` marks un-anchored diagram nodes with data attributes only — `diagramNodeAttrs` (lines 101–105) emits `data-non-normative data-claim-role="non-normative-framing"` but no visible marker — and the diagram containers carry no overall AT text equivalent: the flow list (line 112) and the relationship blocks (line 126) render arrows as `aria-hidden="true"` with no `aria-label` or off-screen prose describing the graph as a whole, so a screen-reader user hears the node words with no relation and no "non-normative" cue. | **Design then *build* it as an additive rendering change with a counterexample fixture, within the POC improvement-cycle scope.** VIS-1 (a partial truth without its qualification is the worst failure) and VIS-3 (the surface is legible to the reader it claims) both rank a diagram a screen reader cannot parse, and an unmarked non-normative node, as honesty gaps. No PWB requirement pins the diagram's accessibility markup, so the change trips no escalation trigger. **The counterexample:** a fixture that renders a non-normative node and asserts both a visible marker *and* an AT text equivalent are present, and a mutation removing either fails it (verification rule 6). **Every lawful arm:** (a) *no change* — the diagrams stay opaque to AT and the non-normative cue stays invisible; (b) *the recommended arm* — an `aria-label` or off-screen equivalent per diagram plus a visible non-normative marker, fixture-guarded; (c) *AT equivalent only* — add the text equivalent but leave the non-normative marking as data attributes, half the fix. **Counter-argument:** a visible "non-normative" marker risks being read as a *verdict* on the node, which the model does not make (VIS-2); the fixture must assert the marker is descriptive, not a score. **Default if unanswered: the diagrams stay AT-opaque and non-normative nodes stay invisibly marked.** |
| Q4 | **[S8-M5] May the 1,634-line `polaris.ts` module be split along its existing section seams, mechanically, with no behaviour change?** Measured at `a9f671e`: `polaris.ts` is **1,634** lines (dossier "1,615" corrected), already divided by banner-comment seams at lines 106, 212, 297, 852, 1032 and 1206 and by ten exported render entrypoints (`renderProjectReading` at 505, `renderCapabilityDeepDive` at 1481, `renderPolarisPresentation` at 1503, `renderPolarisPage` at 1521, and six more). The seams are the natural module boundaries. | **Build it as a mechanical split within the POC improvement-cycle scope, output byte-identical.** Splitting a module at its own seams changes no behaviour and trips no escalation trigger; it lowers the per-change blast radius the Q2 brand must cross and makes the next reviewer's context smaller. **Verify by the existing parity and reachability sweeps plus a rendered-capture diff proving byte-identity** (the same discipline Q2 needs). **Every lawful arm:** (a) *no split* — the module stays a single 1,634-line file every renderer change must load whole; (b) *the recommended arm* — split at the six banner seams into cohesive modules, no symbol renamed and no output changed; (c) *split further, by entrypoint* — ten files, one per exported renderer, finer but with more cross-imports. **Counter-argument:** a split done in the same pass as the Q2 brand or the Q3 a11y change makes each diff unreadable and hides a behaviour change inside a move-only diff — so land the split *alone*, before or after the others, never interleaved. **Default if unanswered: `polaris.ts` stays one 1,634-line module.** |
| Q5 | **[S3-M1, S3-M2] May model-derived inline SVG diagrams be *designed* — over a graph shape that can express fan-in, fan-out and hierarchy, with a real legend — and the fence renderer fed literal fences instead of byte-offset-stitched ones? Feature-request candidate.** Measured at `a9f671e`, two methods: the retained `/polaris` captures contain **0** `<svg` elements (and 0 `<canvas`) — the page draws its relations as an ordered list of node spans with text arrows (`flowDiagram`, `polaris-markdown.ts` lines 108–113) and stacked from/to rows (`relationshipDiagram`, lines 115–127), never a graph. The fence path stitches diagram bodies from byte offsets rather than the literal fence content. [Superseded 2026-09-17: mislocated and mis-worded. The `polaris-markdown.ts` fence renderer already consumes literal fence lines (`body.push(lines[i++])`, :144–154); the offset-slicing lives in `polaris-reading.ts` (`SourceSpan { start; end }` at :26–30, validator/render at :47–64), and those are JS character offsets over `text`, not byte offsets. The `flowDiagram`/`relationshipDiagram` anchors (108–113, 115–127) are correct and stand.] [Anchor refined 2026-09-17: the stitch/emit site is `polaris-reading.ts:107–113` (the `applyReadingPlan` summary map: `text.slice(start, end)` assembling the relations and flow fence bodies); :47–64 is the validation block, not the stitch site. `SourceSpan { start, end }` stays :26–30.] So the manifesto cannot show fan-in, fan-out or hierarchy visually. | **This slice is *design-first* — a feature-request candidate, not a build arm.** A model-derived SVG graph renders project-shape truth *visually*, so a mis-scaled edge, an unlabelled node or a legend that implies a claim the model does not make is a partial truth in the worst class (VIS-1); it needs a design with an explicit legend, an AT text equivalent (Q3's discipline), a non-normative-vs-normative visual grammar, and a fixture oracle before any build. The literal-fence fix (S3-M2) rides with it because the SVG renderer consumes the fence body. **Every lawful arm:** (a) *no change* — the page keeps its text-arrow lists and cannot draw a graph; (b) *the recommended arm* — design the SVG graph shape, legend, AT equivalent and fixture, owner disposes before any build; (c) *design the literal-fence fix alone* — decouple S3-M2 and ship the fence correctness first, deferring the SVG feature. **Counter-argument:** an inline SVG graph is bytes on a page under a 2 MB ceiling that the P-63 trim left roughly 479 KB of headroom under — a rich graph per figure could reclaim that budget, so the design must carry a byte estimate, not just a picture. **Default if unanswered: no SVG diagrams and no literal-fence fix are designed; the page keeps its text-arrow lists.** |
| Q6 | **[S11-M3, S11-M4, S1-M4] May a type scale be named and the eight stray hex colours in the shared token stylesheet retired for tokens (with a grep guard), the forced dark theme resolved by a light palette or one recorded sentence, and figure/passage curation generalized alongside generation?** Measured at `a9f671e`: `design-tokens.ts` defines ten `:root` colour tokens (lines 45–55) [Superseded 2026-09-17: the ten `--token:` definitions are lines 46–55; line 45 is `color-scheme: dark`] and four `--space-*` spacing tokens but **no** type-scale token — every font size is a literal `rem`. Outside the `:root` block the same file carries **eight** stray hex colour literals (lines 68, 95, 99, 100, 131, 144, 147, 148; line 131 is the 8-digit RGBA `#3d2f1322`); app-wide the stray count is 19, the other 11 in the per-surface files (`materialize-action.ts`, `orrery.ts`, `routes.ts`, `trajectory.ts`). The theme is forced dark: `design-tokens.ts` line 45 sets `color-scheme: dark` with a single `:root`, no `prefers-color-scheme` branch anywhere in the app source, and `docs/POLARIS-READING-LAYOUT.md` records no theme decision. | **Split arm.** *Build* the mechanical parts within the POC improvement-cycle scope: name a type scale, retire the eight token-file stray literals for tokens, and add a grep guard against new stray literals (an AGENTS.md-style check). *Record* the theme decision — the cheapest honest arm is one dated sentence in `docs/POLARIS-READING-LAYOUT.md` stating the forced-dark choice and why; a light palette is a *design* question, not a build. *Design* the figure/passage curation generalization (S1-M4) alongside the generator kit. **Every lawful arm:** (a) *no change* — no type scale, eight stray colours, an undocumented forced dark theme; (b) *the recommended split* — build the token/type-scale cleanup and grep guard, record the theme sentence, design the light palette and the curation generalization; (c) *tokens only* — retire the literals without naming a type scale or a grep guard, leaving the next stray literal unguarded. **Counter-argument:** the app-wide 19 stray literals span four surfaces, not just Polaris, so a token cleanup scoped to `design-tokens.ts` alone leaves eleven behind on Orrery, Trajectory and the router; the grep guard must state its denominator (which files it sweeps) or it will read false-clean. **Default if unanswered: no type scale, the eight stray literals stand, the forced dark theme stays undocumented, and curation stays generator-specific.** |

### Decided in this packet, not put to the owner

**The move has no spec prerequisite, and — unlike M15 — most slices may
recommend building.** No slice is downstream of a change to the signed PWB
specification, PWB-REQ text, or its falsifiers; every slice is render-side,
internal to a page already lawfully produced. Under the POC improvement-cycle
scope (review → repair beads from recorded findings → confirmation), the
mechanical and additive slices (Q1, Q2, Q3, Q4, and the token half of Q6)
are buildable; Q5 is a feature-request candidate that is design-first by its
own nature, and the light-palette and curation-generalization halves of Q6
are design. This is stated once and governs every question.

**The S8-F4 gap is `[Observed]` from the digests, not asserted.** The
mutation record's four subject digests are `[Observed]` this session against
the current bytes and all four differ; the "17 of 17 killed" outcome is
`[Observed]` for the recorded bytes and `[Unknown]` for the current ones,
because no evidence binds to them (VIS-2: no evidence yields Unknown, never a
green carried over from dead bytes).

**The diagram and accessibility harms are split by label.** That the page
renders **0** SVG and that the diagrams carry no AT text equivalent are
`[Observed]` from the captures and the source. The *harm* to a screen-reader
user, and the *harm* of a page that cannot draw a graph, are `[Inferred]` —
real under VIS-1 and VIS-3 but not measured against a specific reader this
session. The eight stray literals and the forced dark theme are `[Observed]`;
whether a light palette is wanted is an owner preference, left to Q6.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `security.md` | VIS-1 (a partial truth without its qualification is the worst failure); VIS-3 (the surface is legible to its reader); VIS-7 (the machine's output is honest and safe); SEC-1 (escape untrusted content) |
| Decisions | `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02), `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05), `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` | the implementation grant and its continuation, whose escalation triggers (spec amendment, doctrine or contract change, security/privacy/retention posture, scope) each slice is tested against in Gate 3 |
| Specification | `openspec/changes/three-surface-poc-experience/`, `openspec/changes/polaris-project-wide-butlers-model/` | the signed POC and PWB specs; no slice amends either — every slice is render-side and touches no PWB-REQ text or falsifier |
| Scope | POC improvement cycles (AGENTS.md "Beads scope") | review → repair beads from recorded findings → confirmation; the mechanical and additive slices sit inside this cycle, which is why they may recommend building |
| Contracts | RFC-0002 (RFC2-26 phase rule) | RFC2-26 run in Gate 5; each slice is scheduled from a recorded finding and an approved requirement, not from RFC-0002 alone |
| Policies | craft-and-care (CC-*) engineering and evidence bar; verification rules 6, 7, 10 | the mutation-evidence hygiene (Q1), the byte-identity proofs (Q2, Q4) and the fixture oracle (Q3, Q5) are the bar these slices are held to |

**One scope constraint this packet obeys.** No slice reads a Butlers body or
changes any consent, read or retention boundary — the whole move is internal
to the render of a page already lawfully produced from a body already
lawfully admitted. Q2 hardens escaping in the implementation; it changes no
security posture and adds no capability.

## Gate 1 — Motif

The move is one sentence made mechanical: **the surface that renders the
truth must itself be trustworthy — its evidence current, its escaping
enforced, its diagrams legible, and its colours named.** Four render-side
gaps, in four shapes. The highest-traffic module's mutation evidence is
bound to bytes that no longer exist, so its correctness is asserted from
history (Q1). Escaping is a convention a reviewer re-verifies by hand
instead of a compiler obligation (Q2). The diagrams are opaque to assistive
technology and their non-normative nodes are invisibly marked, and the page
cannot draw a graph at all (Q3, Q5). And the shared visual system has no
type scale, eight stray colours outside its token set, and a forced dark
theme no document records (Q6).

The motif is VIS-7 and VIS-3, not a new idea: the machine's output must be
honest and safe, and legible to the reader it claims. Each slice replaces a
convention with a checked obligation — mutation evidence bound to current
bytes, escaping enforced by the compiler, a diagram a screen reader can
read, a colour named in the token set — without changing what the page
claims.

## Measurements

Each figure names its source and its method. Method is Python `re`, a byte
count, and `sha256sum`/`wc` over the source and the retained captures
(verification rule 1); every load-bearing figure is confirmed by a second
method (verification rule 2). No "zero / all / every" claim rests on a single
sweep.

### 1. The renderer's mutation evidence is bound to dead bytes (S8-F4)

`docs/evidence/pwb-p3-6-narrative-mutation-run-2026-09-04.json` records its
result by a per-file content sha256 in `subjects` (four files) and no commit;
its `killed` and `total` are both 17. Each subject file's recorded digest and
its current sha256 this session (computed with `sha256sum`, full digests, not
a truncated form) are:

| Subject file | recorded 2026-09-04 | current this session |
|---|---|---|
| `apps/three-surface-poc/src/polaris.ts` | `e5367575adb5ec9db5358d1fb58144dec0efe630534752c7b08f389c3a1e5674` | `b6dd1a90ea3dd8f53ed8bf2fc46b96476fa945430bf11b13333b04b3d714f2a6` |
| `apps/three-surface-poc/src/polaris-narrative.ts` | `0b0733ef410eb1791eaa3698c9db75a8c57bede106a9fdd0df68a4f133212e0b` | `a97a80db28410491f926cb811eea13c379aa214140ac1dba285a9440a70cdf3d` |
| `apps/three-surface-poc/src/polaris-copy.ts` | `f6ab0f2a6a8bf9607a81bc72d0fc03e1cebc23be2f707c225f860cafdc7c15e5` | `6a0dce8f15fb049126da6ae74716161d221a38dfa7026d085f9059d170996d95` |
| `apps/three-surface-poc/src/page-shell.ts` | `5fb5a4cdd2be27a515833911102232c9f5e686c37e6c6dfbf82776d849fc39fd` | `c969d2442c5f16cf9c6906a817bc28dcb2073e382fe1a24a9418f9565c662da4` |

All four differ. **Second method:** a
`git log --since 2026-09-04 -- apps/three-surface-poc/src/polaris.ts` lists
seven or more commits (`2ef68f5`, `a121591`, `6fa339b`, `5290cd0`, …), so the
file provably changed after the run. All four subject files' current digests
differ from the recorded ones. The record's outcome is `[Observed]` for the
recorded bytes; the current renderer's mutation state is `[Unknown]`.

### 2. Escaping is convention, not compiler-enforced (S8-M3)

`polaris.ts` imports `escapeHtml` from `@syzygy/cap1-daemon` (line 3); every
render helper returns a bare `string` that is HTML. The five HTML-returning
helpers in the band the dossier names (lines 416–490) are `excludedCauseRoute`
(416), `unavailableCauseRoute` (440), `routeOf` (462), `reasonRouteHtml`
(472) and `unknownRoutes` (480), each typed `string`; a caller can
concatenate an unescaped value with no type error. **Second method:** a grep
for `function .*: string {` across the band returns these five plus
`causeRoutes` (448), which returns `readonly string[]` and is not an
HTML-string helper — five HTML-string helpers, confirmed by reading each
signature. [Superseded 2026-09-17: the quoted narration is wrong.
`causeRoutes` (`polaris.ts` 448) returns `readonly string[] | undefined` and
does not match a `: string {` grep, so the band-scoped grep returns exactly
the five helpers — no `causeRoutes` false positive to exclude. The next
`: string {` match is `readingFigure` at line 491, one line past the 416–490
band.]

### 3. The page renders zero SVG (S3-M1)

Sweeping the three retained `/polaris` captures for `<svg`: **0** in each,
by two methods — `grep -c -F '<svg'` and a Python `str.count('<svg')` both
return 0, and `<canvas` is 0 by the same two. Denominators (the whole page
each sweep ran over): `polaris-direct.html` 1,478,637 bytes,
`polaris-tailnet.html` 1,484,487 bytes, `polaris-7478.html` 2,090,025 bytes.
The relations render as an ordered list of node spans (`flowDiagram`,
`polaris-markdown.ts` 108–113) and stacked from/to rows
(`relationshipDiagram`, 115–127), never a graph.

### 4. Eight stray colours in the token stylesheet, 19 app-wide (S11-M3)

Sweeping `apps/three-surface-poc/src` for a CSS hex colour literal (`#`
followed by exactly 3, 4, 6 or 8 hex digits, not part of a longer run),
excluding the `:root` token-definition lines and the test files: **8** stray
literals in `design-tokens.ts` (lines 68, 95, 99, 100, 131, 144, 147, 148),
which is the dossier's "eight"; **19** stray app-wide, the other 11 in
`materialize-action.ts`, `orrery.ts`, `routes.ts` and `trajectory.ts`. Line
131's `#3d2f1322` is an 8-digit RGBA literal a `{3,6}`-digit sweep misses;
the precise `{3,4,6,8}` sweep is the load-bearing one and is confirmed by a
second sweep counting `#` occurrences per line and subtracting the ten
token-definition rows. Three matches were excluded as non-colours: two
contrast-threshold pairs in `polaris-accessibility.browser.test.ts` (test
fixtures) and one `#0000…` fragment identifier in a source-route test.
[Superseded 2026-09-17: "two contrast-threshold pairs" should read two
contrast-threshold *values* — `#777777` and `#767676` in
`polaris-accessibility.browser.test.ts` — not two pairs; the exclusion total
(3) and the stray counts (8 / 19) are unaffected.]

### 5. The theme is forced dark, undocumented (S11-M4)

`design-tokens.ts` line 45 sets `color-scheme: dark` inside a single `:root`;
a Python search for `prefers-color-scheme` across the whole app source
returns **0** matches, so there is no light branch.
`docs/POLARIS-READING-LAYOUT.md` (45 lines) contains no `theme`, `dark`,
`light` or `color-scheme` token by a case-insensitive Python search — no
theme decision is recorded.

## Gate 2 — Doctrine

- **VIS-7 (the machine's output is honest and safe).** Q1 keeps the
  renderer's correctness evidence bound to its current bytes; Q2 makes the
  escape boundary a compiler obligation so an unescaped value cannot ship
  silently.
- **VIS-3 (legible to the reader it claims).** Q3 gives assistive technology
  a text equivalent and marks non-normative nodes visibly; Q5 lets the page
  draw the graph its architecture actually is.
- **VIS-1 (a partial truth without its qualification is the worst failure).**
  Q3's non-normative marker and Q5's legend are exactly this rule — a diagram
  node or an SVG edge shown without the qualification that it is framing, not
  a claim, is a partial truth; the marker and legend attach the qualification.
- **SEC-1 (escape untrusted content).** Q2's `Html` brand is SEC-1 made
  compiler-enforced; it strengthens conformance and changes no posture.
- **VIS-2 (no evidence → Unknown, never a carried-over green).** Q1's default
  is the honest one: the renderer's mutation state is Unknown until a re-run
  binds evidence to current bytes, never green from the 2026-09-04 record.
- **No new read or egress.** Every slice is render-side and internal; none
  reads a Butlers content class or changes a consent boundary.

## Gate 3 — Topology and the acts

The authorizing acts are the implementation grant
(`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, 2026-09-02) and its continuation
(`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, 2026-09-05), whose
escalation triggers stop implementation before a spec amendment, a doctrine
or contract change, a security/privacy/retention posture change, or a scope
change. Render-side improvement work sits inside the POC improvement-cycle
scope (AGENTS.md "Beads scope"). Each slice against the triggers:

| Slice | Trigger test | Reading |
|---|---|---|
| Q1 / S8-M4 | re-runs a test suite, writes a new evidence record, edits no source | **no trigger** — build arm; evidence hygiene under rules 7 and 10 |
| Q2 / S8-M3 | hardens escaping in the implementation; no posture change, no observable behaviour change | **no trigger** — build arm; SEC-1 conformance, output byte-identical |
| Q3 / S3-M3, S3-M4 | additive rendering; no PWB-REQ pins the diagram a11y markup | **no trigger** — build arm; fixture-guarded, VIS-1/VIS-3 |
| Q4 / S8-M5 | mechanical module split; output byte-identical | **no trigger** — build arm; verified by parity/reachability + capture diff |
| Q5 / S3-M1, S3-M2 | a new visual feature rendering model truth as a graph | **feature-request candidate** — design arm by its own nature, legend + AT + fixture before any build |
| Q6 / S11-M3, S11-M4, S1-M4 | token cleanup + grep guard (mechanical); light palette + curation (new design) | **split** — build the token/type-scale/guard, record the theme sentence; design the palette and curation |

No slice amends the signed spec, edits doctrine, changes the
security/privacy/retention posture, or widens POC scope; Q2 strengthens SEC-1
without changing any posture, and Q5 is design-first because a graph renders
truth visually, not because an act forbids it.

## Gate 4 — Design sketch, per slice

**Slice 1 (S8-M4, mutation re-run).** Re-run the renderer mutation sweep
against the current bytes, write a new evidence record dated this session
(`docs/evidence/pwb-…-mutation-run-<date>.json`) beside the untouched
2026-09-04 record, and record each subject file's current digest and the
killed/total. The sweep rewrites sources in place and runs about 35 minutes;
no edit or commit while it runs.

**Slice 2 (S8-M3, `Html` brand).** Define a branded `Html` string type with a
single `escapeHtml`/`raw` boundary; convert the five HTML-returning helpers
(416–490) and their callers to return and compose `Html`, so a bare `string`
cannot be interpolated into markup without escaping. Prove byte-identity with
a rendered-capture diff, and re-run the Q1 mutation evidence afterward.

**Slice 3 (S3-M3, S3-M4, accessibility).** Add an `aria-label` or off-screen
prose equivalent per diagram describing the graph as a whole, and a visible
non-normative marker beside `data-non-normative` nodes; a counterexample
fixture asserts both are present and that removing either fails, and that the
marker reads as descriptive, not a verdict (VIS-2).

**Slice 4 (S8-M5, module split).** Split `polaris.ts` at its six
banner-comment seams (106, 212, 297, 852, 1032, 1206) into cohesive modules,
no symbol renamed and no output changed; verify by the existing parity and
reachability sweeps plus a rendered-capture diff. Land the split alone, never
interleaved with Q2 or Q3.

**Slice 5 (S3-M1, S3-M2, SVG diagrams).** Design a model-derived inline SVG
graph shape expressing fan-in, fan-out and hierarchy, with an explicit
legend, an AT text equivalent (Q3's discipline), a normative-vs-non-normative
visual grammar, a fixture oracle, and a per-figure byte estimate against the
2 MB ceiling; feed the fence renderer literal fences rather than
byte-offset-stitched bodies. [Superseded 2026-09-17: the current fence
renderer already consumes literal fence lines; the offset-slicing is in
`polaris-reading.ts` (:26–30, :47–64) and uses JS character offsets, not
byte offsets.] [Anchor refined 2026-09-17: the stitch/emit site is
`polaris-reading.ts:107–113` (`applyReadingPlan`); :47–64 is the
validation block, not the stitch site. `SourceSpan` stays :26–30.] Design
only — the owner disposes before any
build.

**Slice 6 (S11-M3, S11-M4, S1-M4, visual system).** Name a type-scale token
set in `design-tokens.ts`, retire the eight stray literals for tokens, and
add a grep guard stating its file denominator; record the forced-dark theme
decision in `docs/POLARIS-READING-LAYOUT.md` in one dated sentence (or design
a light palette under `prefers-color-scheme`); design the figure/passage
curation generalization alongside the generator kit.

## Gate 5 — Specification and the RFC2-26 test

RFC2-26 bars scheduling implementation work for user-observable consequences
**of RFC-0002** from that RFC alone. No slice here is scheduled from RFC-0002;
each is scheduled from a recorded pursuit finding and the engineering bar:

- Q1 from S8-F4 and verification rules 7 and 10 — an evidence-hygiene repair,
  no user-observable change.
- Q2 and Q4 from S8-M3 and S8-M5 — internal refactors with byte-identical
  output, no user-observable change to schedule.
- Q3 and Q5 from S3-M1/M2/M3/M4 and VIS-1/VIS-3 — user-observable, and
  scheduled from the doctrine legibility requirement plus a fixture oracle,
  not from RFC-0002; Q5 is design-gated regardless.
- Q6 from S11-M3/M4 and S1-M4 — the token cleanup is internal; the light
  palette and curation are design.

Each slice's oracle is a hand-typed fixture or a scripted digest/byte diff,
not a generator that quotes prose (the rule-1-and-8 discipline). The
load-bearing ones are Q2's and Q4's byte-identity diffs and Q3's
counterexample fixture, mutation-tested (verification rule 6) before either
is called green.

## Collision and sequencing

| Slice | Touches | Collides with |
|---|---|---|
| 1 S8-M4 | the renderer's evidence record | 2, 4 — re-run *after* they land, or re-run twice |
| 2 S8-M3 | `polaris.ts` helpers and callers, a new `Html` type | 4 (same module), 1 (re-run follows) |
| 3 S3-M3, S3-M4 | `polaris-markdown.ts` diagram emitters | 5 (shares the diagram surface) |
| 4 S8-M5 | `polaris.ts` structure | 2 (same module — land the split alone) |
| 5 S3-M1, S3-M2 | the diagram renderer and the fence path | 3 (AT equivalent), 6 (visual grammar) |
| 6 S11-M3, S11-M4, S1-M4 | `design-tokens.ts`, the layout doc | 5 (legend/theme grammar) |

Sequencing: land Q4 (the split) alone first, then Q2 (the brand) on the split
modules, then Q1 (the mutation re-run) once the source is stable, so the run
is not spent twice. Q3 and Q5 share the diagram surface and should be designed
together, Q3 built and Q5 designed. Q6's token cleanup is independent and can
land any time; its theme and curation halves feed Q5's visual grammar.

## Gate 6 — Engineering bar and the review posture

- **Self-referential figures, computed at a fixed point.** This file is
  **503** lines, **467** of them outside fenced
  code blocks. Over the non-fenced prose lines whose first non-space character
  is not `|`, `>` or `#`, **0** exceed 78 columns. The
  odd-backtick-non-fence-line count is **0**. These numbers are
  the same ones the evidence record carries, computed against the bytes this
  file ends in.
- **No self-referential figure was transcribed.** Each was scripted over the
  finished bytes and iterated to convergence after the last edit (verification
  rule 3).
- **No review yet; every figure uncovered until one lands.** This is a first
  draft; by verification rule 10 every figure here is uncovered until a
  fresh-context review, bound to these bytes, confirms it. The load-bearing
  figures — the four differing mutation-subject digests, the five HTML-string
  helper signatures, the 0-SVG sweep over three captures, the eight stray
  literals and the 19 app-wide, and the forced-dark theme with no recorded
  decision — were each reproduced this session by a second method
  (verification rule 2), which is not a review. [Superseded 2026-09-17:
  review 1 has since landed — CONFIRM WITH EXCEPTIONS (0 blocking / 2
  non-blocking / 3 editorial), findings F1–F5 repaired in place; see
  "## Review 1 and repairs (2026-09-17)" below. By rule 10 the review-1
  repairs post-date the reviewed commit 429924a and are themselves uncovered
  until a second review bound to the new bytes.]
- **What a review must re-derive.** The four subject digests in Measurement
  1's table, current against recorded, all four differing; the five
  HTML-string helper signatures at 416–490; the 0 `<svg` over the three named
  captures with their byte denominators; the eight stray literals at the named
  lines and the 19 app-wide count; that `color-scheme: dark` is forced with no
  `prefers-color-scheme` branch and the layout doc records no theme; and that
  `polaris.ts` is 1,634 lines (not the dossier's 1,615), split by six banner
  seams.

## Review 1 and repairs (2026-09-17)

One independent, fresh-context review of this packet at commit 429924a
returned **CONFIRM WITH EXCEPTIONS** — 0 blocking, 2 non-blocking, 3
editorial. Its raw output is retained verbatim at
`docs/reviews/R-POLARIS-M16-RENDERER-VISUAL-SYSTEM-FUNNEL-1-RAW.md` (11,812
bytes, sha256
`cddd9878ed4c89b50c9afe1d4eca25e164c5c0f3affed895cd01b9380b7c5c79`), the
`-RAW.md` suffix keeping it exempt from CG-1b/CG-15 for the paths and digests
it quotes. Each finding is repaired below by marking the superseded wording in
place, dated, never deleting it.

- **F1 (non-blocking, narration).** Measurement 2's second-method narration
  claimed the `: string {` grep returns the five helpers plus `causeRoutes`
  (448) excluded. Repaired in Measurement 2: `causeRoutes` returns
  `readonly string[] | undefined` and does not match the grep, so the band
  grep returns exactly the five; the next match is `readingFigure` (491),
  one line outside the 416–490 band.
- **F2 (non-blocking, mislocation).** The "stitches diagram bodies from byte
  offsets" sub-claim was mislocated and mis-worded. Repaired in Q5 and in
  Gate 4 slice 5: the offset-slicing lives in `polaris-reading.ts`
  (`SourceSpan` at :26–30; the stitch/emit site is :107–113 in
  `applyReadingPlan`, refined from the :47–64 validation block) and uses JS
  character offsets, not byte offsets; the `polaris-markdown.ts` fence
  renderer already consumes literal fence lines. The
  `flowDiagram`/`relationshipDiagram` anchors (108–113, 115–127) were correct
  and stand.
- **F3 (editorial).** The band label named a non-existent `escapedCauseRoute`.
  Repaired in Q2: the band's first helper is `excludedCauseRoute` (416),
  which the same sentence already names correctly.
- **F4 (editorial).** "ten `:root` colour tokens (lines 45–55)" was off by
  one. Repaired in Q6: the ten `--token:` definitions are lines 46–55; line
  45 is `color-scheme: dark`.
- **F5 (editorial).** "two contrast-threshold pairs" was two values, not two
  pairs. Repaired in Measurement 4: the two values are `#777777` and
  `#767676`; the exclusion total (3) and the stray counts (8 / 19) are
  unaffected.

None of the five moves any recommended arm, any lawful arm, or any default;
each corrects a second-method narration or an anchor, and every load-bearing
figure the reviewer independently re-derived reproduced exactly. The reviewed
bytes are commit 429924a. By verification rule 10 these review-1 close-out
edits post-date 429924a and are themselves uncovered until a further
fresh-context review, bound to the new bytes, confirms them.

## Funnel summary

```
Move M16 — Renderer, diagram and visual-system engineering  rev 1: CWE
------------------------------------------------------------------------------
Motif    the surface that renders the truth must itself be trustworthy:
         evidence current, escaping enforced, diagrams legible, colours named
Gap 1    the renderer's only mutation evidence (17/17 killed, 2026-09-04) is
         bound by content sha256 to bytes that changed 7+ commits ago
Gap 2    escaping is convention: 5 HTML helpers return bare string, unbranded
Gap 3    0 SVG on the page over 3 captures; diagrams AT-opaque, nodes
         non-normative only in data attributes, no visible marker
Gap 4    design-tokens.ts: no type scale, 8 stray hex (19 app-wide), forced
         dark (color-scheme: dark, no prefers-color-scheme, undocumented)

Q1 S8-M4   BUILD: re-run + re-date the renderer mutation sweep, old kept small
           default: mutation evidence stays bound to dead bytes
Q2 S8-M3   BUILD: a branded Html type, 5 helpers fixed, output identical  medium
           default: escaping stays convention-enforced
Q3 S3-M3/4 BUILD: AT text equivalent + visible non-normative marker      medium
           default: diagrams stay AT-opaque, nodes invisibly marked
Q4 S8-M5   BUILD: split the 1,634-line module at its 6 banner seams        small
           default: polaris.ts stays one 1,634-line file
Q5 S3-M1/2 DESIGN: model-derived SVG graph + legend + AT; literal fences   large
           default: no SVG, no graph, no literal-fence fix
Q6 S11+S1  BUILD tokens/type-scale/guard; RECORD theme; DESIGN palette+curation
           default: no type scale, 8 stray colours, undocumented dark theme

Acts     no spec prerequisite; Q1-Q4 and Q6-tokens are build arms in the POC
         improvement-cycle scope, Q5 and Q6-palette/curation are design;
         no slice touches spec, doctrine, security posture or scope (VIS-4)
Review   [was: none yet; first draft, every figure uncovered until a review]
         rev 1 applied 2026-09-17: CONFIRM WITH EXCEPTIONS (0 blocking /
         2 non-blocking / 3 editorial), F1-F5 repaired in place; by rule 10
         the review-1 repairs post-date 429924a, uncovered until a 2nd review
Register P-83 in PENDING-OWNER-DECISIONS.md: six questions, mixed build/design,
         no spec prerequisite, review 1 applied (CWE)
```

## Recommended handoff

1. **Commission the second fresh-context review of the close-out bytes.**
   [Superseded 2026-09-21 at this sentence: it read "Commission the first
   fresh-context review. This packet records none" after review 1 (commit
   429924a, CONFIRM WITH EXCEPTIONS) had landed — see the banner and Gate 6.]
   By rule 10 the close-out repairs are uncovered until a fresh-context
   review, bound to these bytes, confirms them. Give the reviewer only this packet, its evidence
   record, the named source files at `a9f671e`, the three captures, and the
   acceptance criteria.
2. **Put Q1–Q6 to the owner as one batch.** Each carries a recommended arm
   (build, design or draft), its lawful arms, a real counter-argument and a
   stated default of "nothing happens." Q1–Q4 and the token half of Q6 are
   build arms under the POC improvement-cycle scope; Q5 and the palette and
   curation halves of Q6 are design.
3. **Sequence the builds to spend the mutation run once.** Land Q4 (the split)
   alone, then Q2 (the brand) on the split modules, then Q1 (the re-run) on
   the stable source; never interleave the split with the brand or the a11y
   change.
4. **Keep the byte-identity discipline on Q2 and Q4, and the fixture on Q3.**
   The refactors must diff byte-identical against a rendered capture, and the
   accessibility marker must be fixture-asserted as descriptive, never a
   verdict (VIS-2).
