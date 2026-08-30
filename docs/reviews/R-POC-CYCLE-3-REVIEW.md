# R-POC Cycle-3 Review — Polaris, Orrery, accessibility bar, machine-consumer usability

**Commit reviewed:** `715f3b9109406edbda9b6abb32d0a9712c3671d0` (`git log -1`, HEAD of
`main` at review time) / **Reviewer:** independent fresh-context reviewer, no
prior involvement in this POC's implementation or any of the three prior
review passes (`R-POC-PRODUCT-REVIEW.md`, `R-POC-CYCLE-1-CONFIRMATION.md`,
`R-POC-CYCLE-2-CONFIRMATION.md`) / **Date:** 2026-08-30. `git status --short`
at review start showed only the pre-existing, unrelated `.gitignore`
modification — no POC file was dirty.

Scope, per the owner's improvement-cycle direction: this cycle deliberately
takes the lenses the first three passes covered least — Polaris (the
long-form white-paper surface), Orrery (the spatial code-city and its client
bundle), the accessibility bar across all four surfaces and the shared page
shell, and machine-consumer usability of `GET /api/poc`. It does not
re-review Trajectory's materialize/verify chain or the PRF/N-series findings
already confirmed in cycles 1–2. Read-only against application code; the
only file written this session is this one.

## Verdict: no BLOCKER. Four DEFECT, two NOTE findings.

None of the four findings defeats the demonstration or the truth floor —
every claim I checked still resolves to real provenance or an honest
Unknown, and the palette's contrast is, on direct computation, comfortably
above the WCAG AA floor everywhere I sampled it. The defects are concrete,
repairable readability/consumability gaps: two on Polaris's claim to be a
readable document, one accessibility markup defect, one machine-JSON
ambiguity that recurs in two unrelated fields.

## Method

- Read `polaris.ts`, `orrery.ts` (+ its inline `CLIENT_SCRIPT`),
  `trajectory.ts`, `page-shell.ts`, `design-tokens.ts`, `exact-tables.ts`,
  `materialize-action.ts`, `routes.ts`, `model.ts`,
  `worker-change-observation.ts`, `trajectory-projection.ts`,
  `orrery-projection.ts`, `test-artifact-verification.ts` in full.
- Reconstructed the actual rendered text of every Polaris claim section by
  tracing each entity's `detail` string in `model.ts` through
  `polaris.ts`'s `entitySection()` template (no live Butlers checkout was
  needed for this — the templates are pure string substitution over
  `PocModel` fields already fully visible in source).
- Computed WCAG relative-luminance contrast ratios by hand from the hex/rgb
  values in `design-tokens.ts`, `trajectory.ts`, and `materialize-action.ts`
  (formula: linearize each sRGB channel, `L = 0.2126R + 0.7152G + 0.0722B`,
  `contrast = (L1+0.05)/(L2+0.05)`), including the one alpha-blended color
  (`.epistemic-unknown`'s `#3d2f1322` background composited over its actual
  parent background).
- Ran `npx vitest run --project '@syzygy/three-surface-poc-core' --project
  '@syzygy/three-surface-poc-app'` and read the streamed output.
- Grepped for `role=`, `color:`, `tabindex`, and the composite
  `evaluation.snapshot` format across the app/core `src/` trees (excluding
  `.test.ts`) to get real denominators rather than spot checks.

## Test run

```
Test Files  20 passed | 2 skipped (22)
     Tests  114 passed | 2 skipped (116)
```

Identical to the count cycle-2 confirmed (114 passed, 2 skipped — the
env-gated `test-artifact-verification.live.test.ts` and
`work-items.live.test.ts`). No test was modified or added this session; this
is the pre-existing suite passing unmodified at this commit. [Observed]

## Lens 1 — Polaris (`apps/three-surface-poc/src/polaris.ts`)

### C3-1 (DEFECT): two of nine claim sections render a bare file path as the entire "claim", not a sentence

`entitySection()` (`polaris.ts:23-37`) renders `entity.detail` verbatim
inside a `<p>` for every Observed entity. For seven of the nine entities in
`model.ts`, `detail` is an actual sentence (e.g. `'The one configured
external proving project.'`). For exactly two, it is not — it is the raw
path constant itself:

- `packages/three-surface-poc-core/src/model.ts:381` —
  `detail: ARTIFACT_PATHS.code` → `'src/butlers/identity.py'`
- `packages/three-surface-poc-core/src/model.ts:389` —
  `detail: ARTIFACT_PATHS.test` → `'tests/core/test_identity.py'`

So the rendered Polaris section for, e.g., "Identity resolution code region"
is literally:

```html
<h2>Identity resolution code region</h2>
<p><span>src/butlers/identity.py</span> <span class="citation">(repository-file@<12-hex>, manual-mapping@<12-hex>)</span></p>
```

— a path fragment followed by a citation, with no verb, no subject, no
sentence at all. This is a concrete instance of exactly what the lens asks:
a claim that is not "genuinely readable as a document" but a data value
wearing the `<p>` tag's clothing. Every other entity in the file avoids
this because its `detail` was hand-written as a sentence; only these two
inherit their `detail` directly from a path constant reused elsewhere for a
non-prose purpose (the code/test region titles on Orrery and the exact
table). [Observed]

**Repro:** read `model.ts:378-392` (the two entity literals) against
`polaris.ts:23-30` (the template that wraps `detail` in a bare `<p><span>`
with no sentence scaffold) — no test asserts `detail` is sentence-shaped, so
nothing would catch a regression here or a new entity added the same way.

### C3-2 (NOTE): the document has no narrative connective tissue between sections

Beyond C3-1, Polaris's structure end-to-end is: one `<h2>` + one sentence +
one citation per entity (`polaris.ts:23-37`), then the same shape for the
two synthetic code-structure/work-items regions (`polaris.ts:48-76`), then
a single "How these connect" `<ul>` of one-line relationship bullets
(`polaris.ts:39-46`, `102-104`). There is no sentence anywhere that spans or
connects two claims, no framing paragraph, no ordering rationale stated to
the reader beyond the array order in `model.ts:344-428`. Structurally this
is the same information as `exact-tables.ts`'s entity/relationship tables,
reformatted from `<tr>` cells into `<h2>`/`<p>` pairs — a fresh reader gets
the same facts in the same atomized order on both surfaces, just with
different markup. This does not overstate anything and every claim still
cites resolvable provenance (confirmed by `polaris.test.ts`'s POC-REQ-030/031
coverage sweeps, which I re-read and consider sound), so I am not calling it
a DEFECT — but it means the surface does not yet deliver the "long-form
reading... paginated white paper" the page's own `lede` promises
(`polaris.ts:112`). [Observed] the structural fact; [Inferred] that this
falls short of "reads as a document" is a qualitative judgment on my part.

**Sweep run for this lens, nothing else found:** I checked every entity and
relationship `statement`/`detail` string in `model.ts` for wording that
claims more than its `epistemic.basis` supports (e.g., an "Unknown" claim
whose statement text still asserts something positive). None found — the
Unknown branches in both `entitySection()` (`polaris.ts:31-36`) and
`relationshipBullet()` (`polaris.ts:45`) never render `detail`/`statement`
at all, only the `reason`, so an Unknown claim cannot leak an overstated
positive sentence. 9/9 entities and 9/9 relationships checked.

## Lens 2 — Orrery (`apps/three-surface-poc/src/orrery.ts`)

**Determinism claim:** [Observed] holds. The client script sorts
`data.districts` by `path` before rendering (`orrery.ts:76-78`), and
`data.mappedRegions`/the unmapped block render in the server-computed,
file-list-order-derived sequence (`orrery-projection.ts:64-86`, itself a
fold over `structure.files`, whose own order comes from `git ls-tree`, a
deterministic command). `orrery.test.ts`'s "two renders of one observation
produce identical layout-relevant data (POC-REQ-050)" test (byte-identical
HTML on repeat render) and "reconciles declared mapped and unmapped counts"
test both passed in this session's run. No counterexample found.

**Unmapped-region disclosure and denominator:** [Observed] holds. The scope
paragraph states `mappedFileCount`/`totalFileCount`/`unmappedFileCount`
(`orrery.ts:136-140`), matching `model.orrery` exactly (`orrery.test.ts`'s
POC-REQ-020 parity test, passed), and the unmapped block only renders when
`unmappedFileCount > 0` (`CLIENT_SCRIPT`, `orrery.ts:103-112`), always
linking to the one declared `region:unmapped-code` entity.

**Node-to-table route parity:** [Observed] holds, and is the one lens-2
question with direct, passing test coverage:
`orrery.test.ts`'s "every entity-backed spatial region resolves to the same
route the exact tables serve (POC-REQ-053)" test walks every
`mappedRegions[].id` and the unmapped region id from the JSON island against
the page's own anchor ids and asserts 100% resolution. I re-derived the
denominator by hand against `model.ts`'s entity list (`code:identity-
resolution` and `region:unmapped-code` are both present as real `id`
attributes via `exact-tables.ts:27`) — consistent with the test.

### C3-3 (NOTE): district block height encodes real data (total bytes) with no on-page legend, caption, or accessible-name equivalent

`CLIENT_SCRIPT` computes `var height = 3 + (district.totalBytes / maxBytes)
* 6` and sets it as the block's `--block-height` custom property
(`orrery.ts:83-84`), which `.orrery-block { min-height: var(--block-height,
4rem) }` (`orrery.ts:49`) then renders as a real, data-driven visual
variation. This is not misleading — the height is a genuine, deterministic
function of an observed field, not decoration implying evidence that
doesn't exist (the specific failure mode the lens asked me to hunt for, and
I found no instance of it: colors and border styles map 1:1 to the declared
Observed/Unknown encoding already legended via `legendHtml()`, and no
element's position or color varies without a backing data field). But
nothing on the page — no caption near `#orrery-canvas`, no entry in the
shared epistemic legend, no `aria-label` on the individual blocks — tells a
reader that height means "relative total bytes in this directory." A
sighted reader sees varying bar heights and must guess or read
`CLIENT_SCRIPT`'s source to learn what they encode; a screen-reader user
gets nothing at all for this channel, since `.block-label`'s text content is
only path + file count (`orrery.ts:85-88`), never size. The exact tables
below remain the honest, fully-labeled fallback (per `orrery.test.ts`'s
POC-REQ-022 no-script-backstop test), so no fact is actually inaccessible —
only this one supplementary visual channel is unexplained. Repair: one
caption line under the canvas heading, e.g. "Block height is proportional to
total directory size in bytes."

**Sweep run, nothing else found:** checked every `data-parity-field`
attribute Orrery emits (`orrery-scope`, `orrery-unmapped-count`,
`orrery-district`, `orrery-mapped-region`, `orrery-unmapped-region`) against
the machine JSON island (`orrery.ts:124-133`) for a field present on one
side and not the other — none found; the island is a strict subset
(`revision`, `districts`, `mappedRegions`, `mappedFileCount`,
`unmappedFileCount`, `totalFileCount`, `unmappedRegionEntityId`) of
`model.orrery`'s own fields, all present.

## Lens 3 — Accessibility bar (all four surfaces + `page-shell.ts`)

**Contrast, computed from the actual palette values (WCAG relative
luminance, not class-name inspection):**

| Foreground | Background | Used at | Contrast | AA floor | Result |
|---|---|---|---|---|---|
| `--muted` `#8ca3a4` | `--panel` `#0c181b` | `.wi-status`, `.wi-id`, footer, legend text | 6.79:1 | 4.5:1 (small text) | Pass |
| `--muted` `#8ca3a4` | card `#091416` | `.worker-change-detail`/`-note` | 7.03:1 | 4.5:1 | Pass |
| `--cyan` `#78e1d1` (task-flagged) | card `#091416` | `.worker-change-label` (cycle-2's new class, `trajectory.ts:129`) | 11.61:1 | 4.5:1 | Pass, well clear |
| `--unknown` `#f3c56f` | `#3d2f1322` alpha-composited over card (`≈rgb(16,24,22)`) | `.epistemic-unknown` badges | 11.19:1 | 4.5:1 | Pass |
| notice text `#f6dfb5` | notice bg `#1b211c` | `.notice` (scope statements, materialize preview) | 12.60:1 | 4.5:1 | Pass |
| button text `#06171a` | `--cyan` `#78e1d1` | `.materialize-panel button` | 11.78:1 | 4.5:1 | Pass |
| `--focus`/`--amber` `#f1b85b` outline | `--void` `#071012` | `:focus-visible` ring | 10.76:1 | 3:1 (non-text) | Pass |
| `--ink` `#dfe9e7` | `--void` `#071012` | body text | very high (not tabulated) | 4.5:1 | Pass |

**Sweep, nothing found:** I computed every `color:` declaration in
`design-tokens.ts`, `polaris.ts`, `orrery.ts`, `trajectory.ts`,
`materialize-action.ts`, and `routes.ts` (18 distinct rules, confirmed by
grep) against its actual rendered background, including the one alpha-value
color and the specific `.worker-change-label`-on-card pairing the cycle-2
repair introduced. **I found zero AA contrast violations in this palette.**
This is a genuine, checked-not-assumed negative result for this sub-lens.

**Reduced motion:** [Observed] `@media (prefers-reduced-motion: reduce)`
(`design-tokens.ts:152-155`) zeroes all animation/transition durations and
disables smooth scroll; there is very little motion in this app to begin
with (no CSS animations, no JS-driven transitions in `CLIENT_SCRIPT`), so
this guard is effectively complete for what exists.

**Keyboard/focus:** [Observed] a generic `a:focus-visible, button:focus-
visible, [tabindex]:focus-visible` rule (`design-tokens.ts:73-76`) covers
every interactive element on every surface, including Orrery's JS-inserted
`<a>` elements (the rule matches by tag, not by static markup presence). A
skip link is present and functional (`skip-link`, focus-repositions
on-screen). No keyboard trap found; Orrery's non-interactive district blocks
carry no `tabindex`, so they are correctly excluded from the tab order
rather than being focusable-but-inert.

### C3-4 (DEFECT): `role="list"` wraps children that are not `role="listitem"`, on Trajectory's board

`trajectory.ts:184`:

```html
<div class="board" role="list" aria-label="Work-item board by status column">${columns}</div>
```

`columns` is built at `trajectory.ts:155` as a sequence of
`<section class="board-column" aria-label="...">` elements — no
`role="listitem"` on any of them (confirmed: `role=` appears exactly once in
the entire non-test `apps/three-surface-poc/src` tree, at this line — grep
denominator 1/1). Per the ARIA-in-HTML "required owned elements" rule, a
`role="list"` container whose immediate children carry no `listitem` role is
invalid; assistive technology that enforces this (VoiceOver and NVDA both
do, and this is exactly what `axe-core`'s `list` rule flags) either drops
the list semantics silently or announces "list, 0 items," hiding the seven
status columns from list-navigation gestures even though the visual board
renders fine and the real `<ol class="wi-list">`/`<li>` items one level
down are correctly marked up. This is a genuine, narrow, mechanically
fixable defect: either drop `role="list"` (a `<section>`-per-column layout
does not need list semantics at all) or add `role="listitem"` to each
`.board-column` section. No other surface or shared shell component uses a
non-native `role="list"`/`role="listitem"` pair, so this is an isolated,
one-line-cause defect, not a pattern.

## Lens 4 — Machine-consumer usability (`GET /api/poc` = `JSON.stringify(model)`)

### C3-5 (DEFECT): `evaluation.snapshot` is an undocumented composite string, not a structured field

`model.ts:540`:

```ts
snapshot: `${input.evaluation.snapshot}|inputs:sha256:${inputDigest}`,
```

`PocModel.evaluation` is typed only as `{ readonly snapshot: string; readonly
asOf: string }` (`model.ts:92`) — nothing in the type, a JSDoc comment, or
any response body documents that `snapshot` is actually two values joined by
a hand-rolled `|inputs:sha256:` separator. The only place this exact format
is asserted at all is a regression-test regex,
`packages/three-surface-poc-core/src/model.test.ts:165`:
`/^butlers@c1389423\|inputs:sha256:[0-9a-f]{64}$/` — a test fixture's
assertion, not a machine-readable contract. A programmatic consumer of `GET
/api/poc` who wants "the human label" or "the input digest" separately (for
example, to compare the digest against a value recorded elsewhere, per this
repo's own verification rule 3, "digests are scripted, never transcribed")
has no field to read either half from directly; they must string-split on an
undocumented literal that could change without a type error (nothing
enforces the separator's shape beyond that one test file's regex). Both
human surfaces render this same composite string verbatim in `<code>`
(`polaris.ts:115`, `routes.ts:75`), so the ambiguity is not confined to the
JSON channel. Repair: expose `inputDigest` (and, if useful, the original
un-suffixed snapshot label) as their own named fields on `PocModel`, or at
minimum document the delimiter in a comment on the `evaluation` field's
type.

### C3-6 (DEFECT): `WorkerChangeCommit.containingRef: null` means two different things depending on `state`, and the JSON gives no way to tell which

`worker-change-observation.ts:16-19` documents the field:

> `containingRef`: The ref that was found to contain this commit
> (branch/tag), when one could be identified; `null` for a commit already
> reachable from the default branch, where "the default branch" is the
> answer itself.

But this dual meaning is a documentation comment in TypeScript source, never
surfaced in the JSON. Concretely:

- When `state === 'changed-or-merged'`, `containingRef` is **hardcoded**
  `null` (`worker-change-observation.ts:210`) — the intended reading is "no
  ref lookup needed; the answer is trivially the default branch."
- When `state === 'active'`, `containingRef` comes from a real
  `findContainingRef()` lookup (`worker-change-observation.ts:229`) that
  itself can return `null` when the `for-each-ref --contains` search finds
  nothing (`worker-change-observation.ts:152`, `refs[0] ?? null`) — here the
  intended reading is "we looked, and found no containing ref."

Both cases serialize to the exact same JSON shape, `"commit": {...,
"containingRef": null}`, distinguishable only by cross-referencing the
sibling `state` field and knowing, from outside the response, that
`'changed-or-merged'` short-circuits the lookup while `'active'` performs
it. A machine consumer reading `commit.containingRef` in isolation (e.g., to
decide "was a branch identified for this change?") cannot tell "yes,
trivially — it's already on the default branch" from "no, the search came
back empty" without also branching on `state` and knowing this specific,
undocumented-in-JSON convention. `trajectory.ts:81-85` (the one renderer of
this field) sidesteps the ambiguity entirely by never rendering
`containingRef` when `state === 'changed-or-merged'` in the first place (see
the `workerChange.state === 'planned' ? ... : workerChange.commit === null ?
'' : ...` branch, which for `'changed-or-merged'` still reaches the
`containingRef === null ? '' : ...` ternary and simply omits the "on
`<ref>`" clause) — so the human page never shows a misleading value, but the
raw JSON export still carries the collision for anyone who reads it
directly rather than through this one renderer's logic.

**Sweep for this lens, nothing else found beyond C3-5/C3-6:** checked every
other optional/nullable field reachable from `PocModel` for a similar
collision — `PocProvenance.digest?` (absent, via `JSON.stringify`'s
undefined-drops-the-key behavior, only for the `git-revision` provenance
kind; this is ordinary optional-field JSON and any JSON-aware consumer
handles a missing key without special convention knowledge, so I did not
count it as ambiguous), `MaterializationEpistemic`/`materializedBeadId:
string | null` (null has exactly one meaning — "unconfirmed/none" — proven
fail-closed by cycle-2's confirmation review), `WorkerChangeResult`'s
`kind: 'observed' | 'unknown'` discriminant (clean, no collision),
`TestArtifactVerificationResult`'s `kind: 'unknown' | 'verified'`
discriminant (clean). 6 nullable/optional fields checked across the four
core observer modules; 2 collisions found (C3-5, C3-6), 4 clean.

## Bottom line

I found no BLOCKER: every positive claim I traced still resolves to real,
current provenance, no Unknown ever upgrades itself, the human/machine
channels stay in lockstep everywhere I checked, and the palette's contrast —
computed by hand from the actual hex values rather than inferred from class
names, including the one pairing this cycle's brief specifically flagged
(`.worker-change-label` cyan-on-card) — clears WCAG AA everywhere sampled.
Four DEFECT-level findings survive: two concrete Polaris readability gaps
(a literal bare-path-as-claim in two of nine sections, and a document-wide
lack of narrative connective tissue), one accessibility markup defect (an
invalid `role="list"` on Trajectory's board with no `listitem` children),
and two machine-JSON field-ambiguity defects (an undocumented composite
`evaluation.snapshot` string, and a `containingRef: null` that means two
different things depending on a sibling field). Two NOTE-level improvement
ideas round out the Orrery and Polaris lenses. All four DEFECTs are narrow
and independently repairable without touching the truth-floor machinery
this POC exists to demonstrate.

No repository edits were made beyond this review file. This file is FROZEN
as of this write — any further edit to it retires this review per AGENTS.md
verification rule 10.
