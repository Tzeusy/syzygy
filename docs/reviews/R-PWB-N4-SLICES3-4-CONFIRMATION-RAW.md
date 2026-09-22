# R-PWB-N4-SLICES3-4-CONFIRMATION-RAW.md

Reviewed PR: #67 (Tzeusy/syzygy), branch agent/syzygy-u05.4-slices3-4
Reviewed commit: b80f7bcbccdebbfad06860d1e14b2a16cb8663cd
Review date: 2026-09-23
Verdict: CONFIRM

Fresh-context confirmation review of the repair commit against the prior REVISE
(`a8bf4ad`, raw at
`/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/R-PWB-N4-SLICES3-4-REVIEW-RAW.md`).
Worktree built at `b80f7bc` under
`/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/pr67-confirm`
via `git worktree add` + `npm ci`; nothing committed, pushed or merged; the
worktree was removed (`git worktree remove --force`) after the review
completed, which does not touch the PR branch or main.

**Scope of the repair.** `git diff a8bf4ad..b80f7bc --stat`: exactly 3 files —
`design-tokens.ts` (+55/-24), `design-tokens.test.ts` (+81/-0),
`evaluation-footer.ts` (+6/-1, comment only). No other file in the 9-file PR
changed between the reviewed commit and this one.

## Finding 1 (F3 — `--focus` collided with `--cyan`/Observed): REPAIRED, confirmed by independent recomputation

`design-tokens.ts:63`: `--focus: #b98eff;` (was `#78e1d1`, byte-identical to
`--cyan`). The accompanying comment (lines 55-62) names the exact defect the
prior review found and states the fix's rationale and contrast numbers.

**Hue-collision sweep, independent of the PR's own claim.** Swept every hex,
`rgb()` and `hsl()` literal in `apps/three-surface-poc/src` and
`packages/*/src`:
`grep -rnoE '#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)' apps/three-surface-poc/src packages/*/src`.
Found 21 distinct colour sites outside `design-tokens.ts`'s own token block
and its test file (test-fixture literals `#777777`/`#767676` are WCAG
canonical-pair constants inside `polaris-accessibility.browser.test.ts`, not
page colours; `#106`, `#0000`, `#0008` are false positives — an HTML numeric
entity, a fake identity string, and a shadow alpha channel, verified by
reading each match's context). `polaris.ts` itself declares zero literal
colours (0 hex hits); it and `polaris-generation/draft-preview.ts`'s inline
SVG both style exclusively through `var(--x)` tokens (`svg path{...stroke:var(--cyan)}`
etc.), so there is nothing there to collide.

Computed CIE76 ΔE (via sRGB→XYZ→Lab, a standard formula, not the codebase's
own) from `#b98eff` to all 21 non-token colours plus all 9 declared tokens.
Lowest ΔE found: 66.41 (`--muted #8ca3a4`) — roughly 29× the ~2.3 "just
noticeable difference" threshold, and every other site scores 67–109. No hue
anywhere in the swept trees is "near-identical" to `#b98eff` by any
reasonable perceptual measure, let alone reused with a stated meaning.
`EPISTEMIC_ENCODING`'s two classes (`--cyan` ΔE=89.4, `--unknown` ΔE=105.5),
the link colour (`--cyan`, same), and `--amber`/`.notice` (ΔE=108.9) are all
far outside collision range. **F3's fix generalizes correctly, not just past
the two colours the prior review named.**

**Contrast recomputation, independent method.** Implemented WCAG relative
luminance and contrast ratio from scratch (not copied from the PR or its
tests) and checked `--focus` against every background surface a focusable
element can sit on: `--void` 7.67:1, `--panel` 7.21:1, `--panel-raised`
6.61:1, table background `#091416` 7.46:1, header-gradient lightest point
`#173238` 5.40:1, `tr:target` background `#1e383b` 4.97:1, `.notice`
background `#1b211c` 6.54:1. This reproduces the PR's cited range
**exactly** — 7.67:1 against `--void` and 5.40:1 against `#173238` are
bit-for-bit the numbers in both the code comment and the bead comment — and
every other background surface clears the same ≥3:1 WCAG 2.4.11/1.4.11
floor with margin (lowest found: 4.97:1).

**Mutation testing (rule 6), independent of the PR's own embedded mutation
test.** Ran `design-tokens.test.ts` three times, each with `--focus`
literal-patched in place and reverted after (`cp`/`sed`/`cp` back;
`git status --short` confirmed clean after each):
- old `#b98eff` → new `#78e1d1` (cyan/observed/link): 3 of 8 tests failed,
  including the CSS-derived semantic-colour sweep and the hard-coded literal
  check.
- old `#b98eff` → new `#f1b85b` (amber/notice): 4 of 8 failed, including the
  semantic-colour sweep, the amber-distinctness test, and the PR's own
  cyan-collision mutation check (which itself depends on `--focus` starting
  at its real value).
- old `#b98eff` → new `#f3c56f` (unknown): 4 of 8 failed, including the
  semantic-colour sweep and its own mutation-check test.
All three semantic collisions — Observed/cyan, Unknown, and the
notice/amber accent — are independently confirmed caught by the widened
test, not merely asserted by the PR. **Answers review question 2**: yes, the
widened test (`epistemicClassColor()` + `linkColor()`, both parsing the live
`DESIGN_TOKENS_CSS` and the live `EPISTEMIC_ENCODING` array rather than a
hard-coded exclusion list) resolves every `EPISTEMIC_ENCODING` class
(`epistemic-observed`→cyan, `epistemic-unknown`→unknown) plus the link
colour and the amber/notice accent, and a denominator assertion
(`semanticColors.size === EPISTEMIC_ENCODING.length + 2`) guards against a
future encoding entry silently going unswept (rule 9).

No blocking issue remains on F3.

## Finding 2 (F4 — `--measure-reading` dead-token overclaim): REPAIRED

`design-tokens.ts:70-85` (comment) and `design-tokens.test.ts:114`: both now
say the token "DECLARES a value" / "declares the value slice 2 wires... —
this token declares the value, it does not by itself resolve the
contradiction" — the "resolves" framing is gone from the code comment, the
widened test's own name, the PR body (its "Repair" section explicitly
restates the same correction), and the bead comment (2026-09-22 18:18,
verbatim: "Corrected wording... the token declares the canonical value for
slice 2 to wire into; it does not by itself resolve the contradiction").
`grep -rn "measure-reading" apps/three-surface-poc/src/` still finds only
the declaration and its own test — `polaris.ts` still carries the literal
66ch/74ch pair unchanged, exactly as expected since `polaris.ts` remains out
of scope for this slice. The claim now matches the code. No blocking issue
remains on F4.

## Additional checks (review's own items 3-5)

**3. The +1,024 B CSS-comment cost is real, correctly disclosed, and
reaches `/polaris`.** Extracted `DESIGN_TOKENS_CSS`'s string body from
`a8bf4ad` and `b80f7bc` via `git show <rev>:...` and a Python regex (not by
reading `git diff` insertions/deletions, which count lines, not bytes):
5,295 → 6,319 bytes, delta **exactly** 1,024 — matching the PR body's and
bead comment's number bit-for-bit. `apps/three-surface-poc/src/page-shell.ts:53`
(`<style>${DESIGN_TOKENS_CSS}${input.extraStyle ?? ''}</style>`) embeds the
full template-literal string, comments included (nothing strips CSS
comments before serving), and `polaris.ts:1620/1646` calls `pageShell(...)`,
so `/polaris` does carry this cost, not just Trajectory/Orrery. Re-ran
`page-size-delta.test.ts`: `/trajectory: before=18586B after=18968B
delta=+382B`, `/orrery: before=37781B after=38070B delta=+289B` — the
`before` baselines (which reconstruct the *pre-repair* page by substituting
the old footer literal into the *current* render) grew by exactly 1,024 B
over the prior review's own `a8bf4ad` baselines (17562→18586,
36757→37781), while the footer's own marginal cost (`delta`) is unchanged
at 382/289 — confirming the 1,024 B lands once, globally, from the token
file's comments, not from anything footer-specific. This is a real,
correctly-disclosed cost, and it is properly flagged as a genuine (if tiny)
page-weight regression rather than hidden.

Whether "well inside the 2 MB ceiling" is *currently* true rests on stale
evidence, though: the only headroom measurement in the repo is
`docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json`, 16 days
old, which recorded 478,751 B of tailnet headroom after the P-63 trim,
against a **projected** (not yet landed, per that same file and per
AGENTS.md's "Known gaps" section) P-60/P-61 repair growth of 418–443 KB —
leaving as little as ~25 KB of margin in that file's own worst case, before
any of the 16 days of subsequent commits touching `polaris.ts`/`page-shell.ts`
are accounted for. No fresher `/polaris`-specific size measurement exists
in `docs/evidence/`. Given 1,024 B is roughly 4% of even that worst-case
25 KB remainder, and a much smaller fraction of the 478 KB headroom as
measured, this is not blocking, but the PR's "well inside the 2 MB ceiling"
line should not be read as a fresh measurement — it is a reasonable
inference from 16-day-old evidence that this PR did not update. Non-blocking;
worth a one-line caveat if the ceiling ever needs re-verifying precisely.

**4. Commands re-run in this worktree, output read (not just exit code).**
- `npm test`: flaked twice under this sandbox's load — 2 failures on the
  first run, 3 on the second, always inside
  `apps/three-surface-poc/src/polaris-copy.test.ts` (`Error: Test timed out
  in 5000ms`), a file the PR's diff does not touch. Re-ran that file alone
  with `--testTimeout=60000`: all 4 tests passed in 11.7 s (individual test
  bodies run 5.5–5.7 s — just over the 5 s default under this environment's
  load, comfortably under 60 s). This is an environment-timing flake, not a
  functional regression: confirmed by a second method (extended timeout)
  per rule 2, and the failing file is outside the diff under review. All
  other files passed consistently; the stable count (1737–1738 of 1743
  non-skipped) is consistent with the PR's claimed 1740 passed/3
  skipped/0 failed.
- `npm run build:poc`: clean, no output, exit 0.
- `python3 scripts/check_governance.py`: `32 OK, 20 WARN, 0 FAIL (52
  checks)` — matches the PR body and bead comment exactly. Read the WARN
  list (rule 4): all 20 are pre-existing governance-prose items (CG-19b
  substrate-pin population, CG-22b/CG-23 vocabulary allowlists, CG-24
  selftest-fixture coverage, CG-27 default-path claims in
  `.syzygy/governance/decisions/README.md`), none touching
  `apps/three-surface-poc/**`.

**5. PR body and bead comments: no overclaim found in the current
statements.** The bead's first comment (2026-09-22 18:02) contains the two
overclaims the prior review caught ("--focus is now distinct from
--amber" — true but silent about the cyan collision; "--measure-reading...
resolves the... contradiction" — false). Per this repo's epistemic
discipline, that comment was correctly left unedited, with a second,
explicitly-dated correction comment (18:18) appended rather than editing
history. The correction comment states both defects and both fixes
accurately, matches the code exactly (contrast range 5.4–7.7:1, matching my
own recomputation to two decimal places; the +1,024 B page-weight cost;
"well under the 2MB ceiling" — same caveat as item 3 above), and the PR body
itself carries the identical, accurate "Repair" section. No new overclaim
introduced by the repair.

## Verdict

**CONFIRM.** Both findings from the prior REVISE (`a8bf4ad`) are repaired at
`b80f7bc`: `--focus` (`#b98eff`) collides with nothing in the codebase's
declared semantic-colour set by exact value, and — independently confirmed
by a from-scratch perceptual-distance sweep, not just the PR's own claim —
with nothing close to it either; its widened distinctness test is proven by
independent mutation to actually catch a collision with every
`EPISTEMIC_ENCODING` class, the link colour and the amber/notice accent, not
merely assert distinctness against a fixed pair. The `--measure-reading`
"resolves" overclaim is corrected everywhere it appeared (code comment, test
name, PR body, bead comment) to the accurate "declares a value pending
consumption" framing. The one new, real cost this repair introduces — 1,024
bytes of CSS comment reaching every served page including `/polaris` — is
honestly disclosed with computed (not transcribed) numbers that reproduce
exactly under independent recomputation; its "well inside the ceiling"
framing rests on 16-day-old headroom evidence this PR did not refresh, which
is a non-blocking observation given the payload's size relative to even the
oldest measurement's worst case. `npm test`/`npm run build:poc`/
`check_governance.py` all reproduce the PR's claimed results exactly, modulo
an environment-only timeout flake in an out-of-scope test file, confirmed
non-functional by a second method. No further repair needed before merge.
