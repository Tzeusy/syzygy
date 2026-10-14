# R-PWB-ACCESSIBLE-NAME-AMENDMENT-3 — fresh-context review, PWB accessible-name amendment (PWB-REQ-016), round 3
Reviewed commit: d6b3784f5b7f09b27ffb41f57785282b7393c4d1
Manifest SHA-256: 8dfd6d836402b81a995c44f1435354d3ce2bef735daa399692e6c4dbe9f8bae0
Verdict: CONFIRM WITH EXCEPTIONS

Package: `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/`
(manifest `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`). The head digest is
the sha256 of that file's bytes at the reviewed commit. I computed it with
`git show d6b3784f…:<path> | sha256sum` and confirmed it with a second
Python `hashlib` pass over the clean clone's working file. Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`, §"Round 3" governing. This
raw judges package C only. Findings 9 and 10 apply to both packages and are
repeated in the A raw. Prior raws: rounds 1 and 2
(`docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-2-RAW.md`, `REVISE`, at
`ae8c0740`). Repairs: `ROUND-2-DISPOSITIONS.md` §"Repairs, 2026-10-14
(cycle 2)".

## Mechanics run (fresh clone at the reviewed commit)

[Observed] I ran everything from a fresh `git clone` checked out detached at
`d6b3784f`. The engine derives `ROOT` from `__file__`, so it read the clone.
`git status --short` in the clone was empty after every run. I read each
check's output, not only its exit code.

- `build_pwb_accessible_name_amendment.py --check`: passes. Output: "11
  proposed subjects (2 patched); 17 requirements, 54 scenarios; structure,
  regeneration, contract coverage, sibling classification and
  pending-sibling composition (pairwise, and one result in every order)
  verify".
- `build_pwb_accessible_name_amendment.py --selftest`: passes. Output: "27
  structure mutants, … all fail closed on their own predicates". That is 5
  engine mutants plus 22 builder mutants, as the dispositions say.
- `build_pwb_opening_index_amendment.py --check` and `--selftest`: both
  pass. Output: 33 mutants.
- `build_pwb_class_granular_extraction_amendment.py --check`: passes.
- `build_pwb_release_label_amendment.py --check`: **fails** (exit 1). Output:
  its `GOVERNING-DEPENDENCIES.md.patch` "does not apply … :9". See finding 10.
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL;
  PASS". The R6 warning on the two behaviour-contract pins predates this
  package.
- Independent byte check. I wrote my own script, copied the change
  directory and applied both patches with plain `git apply`.
  - All 11 of 11 manifest rows hash to the proposed bytes.
  - Only `GOVERNING-DEPENDENCIES.md` and `spec.md` differ. The text before
    the requirements, the requirement population and the order are
    identical.
  - PWB-REQ-016 is the only changed block.
  - Exactly 3 signed lines are replaced or removed. They are the builder's
    3 `replaced` lines, and each opens exactly one proposed line.
  - The `warrants:` block is identical. The scenario count goes from 1 to 3.
  - Both patches target PWB paths only. The Three-Surface POC
    specification cannot be touched.
- Composition, by my own `git apply` loop. I applied the four pending spec
  patches to `spec.md` at this commit in all 24 orders. All 24 applied,
  none failed, and they gave 1 result (sha256 `fa0522173b60…`).
- Rule-6 probes through the engine's `spec_findings` over the proposed
  bytes.
  - Killed: dropping the Case limb, dropping refused pages from the page
    list, loosening the visible-label definition, and dropping the
    page-list independence line.
  - **Survived** (no finding):
    - "A link's target is its resolved `href`" → "its text";
    - "a `summary`'s controlled region is its `details` element" →
      "itself";
    - dropping the first new scenario's "**AND** no two of them with
      different targets share an accessible name";
    - narrowing that scenario's WHEN to "the same source";
    - "are measured on a fresh private-daemon capture" → "were measured on
      an old capture".

  See finding 9.
- Code facts the delta cites, read at this commit.
  - `polaris-source.ts:123` renders each verbatim body as escaped text in
    `<pre class="verbatim">`.
  - `polaris-markdown.ts:179` sets
    `Math.min(6, anchorHeadingLevel + 1 + heading[1]!.length - shallowestHeading)`.
  - `polaris-accessibility.ts:525` is `const tree = await page.axTree();`.
  - `grep -F -c level` over that file returns 0.
  - `project-shape-coverage.ts:189` is `readonly path: string;` inside
    `SourceCoverage`.

  All are as the delta states.

Round-2 findings, checked one by one against the bytes:

- **1 (label-in-name rule without limbs).** Repaired.
  - **Scope.** "These two rules bind no other element" (`proposed/spec.md.patch:24`),
    with the trigger "elements … whose targets differ share one visible
    label" (`:18-20`).
  - **Definition.** The visible label is text content, whitespace
    collapsed (`:17-18`).
  - **Limbs.** Oracle `:69-73`, independence `:79-80`, Falsifier `:84-86`,
    and both scenarios (`:100-102`, `:112-113`).
  - **Pinning.** All pinned. The raw's "free text" probe is now a killed
    mutant.
  - **Packet A's rows.** They fall under the rule only where another
    differently targeted element shares their text. That is correctly
    scoped.
- **2 (page enumeration).** Repaired (`:42-45`). The page list comes from
  the machine answer, served or refused, and never from the renderer's
  links. The Oracle and the second scenario carry it. The page list's
  source is outside the renderer. The residual is finding 6.
- **3 (interactive population).** Repaired (`:13-16`). It mirrors the
  heading population word for word: after load, including closed
  `details`, with the same three exclusions. It is pinned. The residual is
  finding 3.
- **4 (verbatim exemption).** Repaired by dropping it (`:34-35`). The code
  facts above support the drop. The exact-source route puts no heading
  element on the page. Entry-page Butlers headings get their levels from
  Polaris, so a gap can be closed without changing text, and the ledger
  names that consequence (`IMPACT-LEDGER.md:49-50`). Question 8 states this
  fairly, and its alternative is honestly marked not drafted.
- **5 (stale sentences).** Repaired: the ledger, the builder docstring and
  register row P-99. The round-state sentences are marked and dated. The
  residual is finding 7.
- **6 (pinning; engine prefix check).** The heading exclusions and the path
  rule are pinned as whole sentences, with mutants killed. The positional
  check is added and its mutant is killed. Residuals are in finding 9.
- **7 (sibling order).** At this commit the four pending spec patches
  compose in every order. The release-label lane is still open (finding 10).

Criterion 2 holds: only PWB-REQ-016 changes, and slice D is put to the
owner with the one-category reasoning (Question 4). Criterion 3 holds for
every new obligation: the distinct-name rule, the label prefix, the path,
the heading order, and the page and population denominators each have an
oracle limb, a falsifier limb and a scenario. Criterion 4 holds by the byte
check above. Criterion 5 holds: no capture figure is quoted, the current
figures are [Unknown], and nothing is claimed adopted. On the path question
see finding 1. Every finding below is a note.

## Findings

**Finding 1 — The machine answer does carry each listed source's repository-relative path in today's code; the clause the patch cites guarantees the identity, not the path, and the delta's [Unknown] can be closed** (note)

[Observed, static reading at `d6b3784f`] The machine route
`GET /api/poc` (`routes.ts:230-233`, `machineHandle`) serves
`JSON.stringify(model)` of the whole `PocModel` (via `servedModel()`). It
strips nothing: `withServedReadiness` (`routes.ts:183-191`) only replaces
`walkthroughReadiness`. When the shape is `observed`, `projectShape.sources`
is `readonly ProjectShapeSource[]` (`project-shape-model.ts:336`). That type
extends `SourceCoverage`, so each element carries `path`
(`project-shape-coverage.ts:189`) as well as `identity`
(`project-shape-model.ts:254`). The exact-source route resolves its
`identity` query parameter against that same array and reads `source.path`
(`polaris-source.ts:89-95`). So an oracle can follow a link to its source:
it reads the `identity` from the link's `href`, finds the
`projectShape.sources[]` element with that identity in the machine answer,
and takes that element's `path`. It never reads the rendered page to do so.

[Unknown] I did not serve the daemon or fetch the machine answer. That the
served JSON carries a path for every listed Butlers source at a live
evaluation is not run-verified. When the shape is not `observed`, no
sources are listed, the page list is the entry page alone, and the path
rule is vacuous.

On the specification side, the patch attributes the path to "PWB-REQ-011's
machine recovery" (`:23-24`). That limb (spec line 1167) makes
recoverable "each served route's mode, source identity and each refusal's
reason". The spec separates identity from path: line 94 says the
repository-relative path is "source-anchor state, never identity". In the
code, `identity` is a registry `git-tree-entry` identity distinct from
`path`. The clause that binds paths into the machine answer is PWB-REQ-001
instead. Its SHALL makes "human and machine readers … receive … the same
source population" over "the complete source-path population" (spec lines
282-287), and its Observable lists "source paths".

So the [Unknown] in the delta (`SEMANTIC-DELTA.md:154-156`) and in Question
7's recommended row is honest, because it says "not checked". It is also
answerable: by these code facts, and by an existing signed SHALL. Question
7 is fair. Its caveat ("if not, the machine answer needs it too") would not
fire on today's code. A future edit could cite PWB-REQ-001 beside
PWB-REQ-011.

**Finding 2 — "Visible label" is defined as text content, which is not the visible label for every element in the population** (note)

[Observed] The definition (`:17-18`) is "its text content with each
whitespace run collapsed". That is decidable, but it diverges from what a
sighted or speech-input user sees in three ways:

- text content includes descendant text hidden by `display: none`,
  `hidden` or `aria-hidden`;
- for an `input`, it is empty, because the visible label is a separate
  `label` element;
- for a `select`, it is the concatenated option text.

[Inferred] An element whose visible words are shared but whose text
content differs (by a hidden span) escapes the label-prefix rule. The
distinct-name rule still binds it, so screen-reader users stay protected.
The delta's speech-input rationale (`SEMANTIC-DELTA.md:142-143`) does not
fully hold for it. The term is a misnomer. One qualifier ("its rendered
text", or excluding hidden descendants) would align the term with its
purpose.

**Finding 3 — Whether "the browser computes" an accessible name for an element inside a closed `details` is not established** (note)

[Observed] The interactive population includes elements inside a closed
`details` (`:14-15`). The rule compares names "as the browser computes
them" (`:9`). [Unknown] Whether the browser's accessibility engine exposes a
computed name for a node in a closed disclosure's content, which is not
rendered on first load, or marks it ignored with no name. The delta itself
says today's accessibility-tree checker "leaves them out"
(`SEMANTIC-DELTA.md:160-162`).

The Oracle says only "group the interactive elements by computed accessible
name". It does not say whether the oracle opens the disclosure first, which
changes the first-load state that package A counts in, or uses an
independent accessible-name implementation. Two oracles could report
different groups for those elements. One sentence naming the procedure
would close it.

**Finding 4 — An element can be in the heading population twice, at two levels** (note)

[Observed] The heading population is "every `h1` to `h6` element, at its
own level, and every element with `role="heading"`, at its `aria-level`"
(`:29-30`). An `h2` with `role="heading" aria-level="3"` is in both halves,
at levels 2 and 3. An `h2` with `aria-level="3"` and no role has computed
level 3 in the browser, but level 2 by this text. An `h3` with
`role="presentation"` is no heading to a screen reader, but it counts here.

All three cases are decidable as written, but the rule's level is not the
level a nonvisual reader hears. [Inferred] Polaris emits none of these
today. "Each element once, at its computed level" would settle it.

**Finding 5 — C's hidden-element exclusions differ from A's** (note)

[Observed] C excludes `hidden`, `aria-hidden="true"` and computed
`display: none` (`:15-16`, `:31-33`). A also excludes text whose parent's
computed `visibility` is not `visible`. So a `visibility: hidden` link
counts in C's population and can fail the distinct-name rule, although no
reader can reach it. An `inert` subtree also counts. The rule is decidable,
and each package is consistent within itself. Signed together, the two
requirements would define "hidden" two ways on the same page.

**Finding 6 — The closed page list and the open "every Polaris page served" agree today, but only by today's route table** (note)

[Observed] The SHALL runs the checks "over every Polaris page served …
including the entry page and each exact-source route response" (`:36-38`).
The Falsifier fails "a check run over fewer pages … than the evaluation
serves" (`:88-89`). Meanwhile the list is closed: "the entry page and one
exact-source route response for each source the machine answer … lists"
(`:42-44`). Today `routes.ts:286-302` registers only `/polaris` and
`/polaris/source`, plus their tailnet-mount forms, as Polaris human pages,
so the two agree. A future Polaris page would be "served" and in no list.
The page-count Oracle would then pass while the Falsifier fires. The
tailnet-mount forms, which are the same pages with prefixed `href`s, are
not mentioned. One clause could say the list is the whole population, or
that a new page needs a new list.

**Finding 7 — Register row P-99's mark attributes the machine-answer page list to the wrong repair** (note)

[Observed] `PENDING-OWNER-DECISIONS.md:1193` marks the scope as "every
Polaris page served at one whole-project evaluation, the pages listed from
the machine answer, as the round-1 repair made it". Round 1 made the scope
every page. Listing the pages from the machine answer is the cycle-2
repair of round-2 finding 2 (`ROUND-2-DISPOSITIONS.md`, row 2).

**Finding 8 — Copy role of the words a name adds** (note)

[Inferred] The path words appended to a shared-label name are owner-facing
when they are announced. PWB-REQ-012 says "each interactive control may
carry one `action-label`" and that every owner-visible string carries one
role. The packet does not say whether the appended path is part of that
action label, or whether REQ-012 binds a name that is announced but not
displayed. This does not cross REQ-012 as written, but an implementer will
meet the question.

**Finding 9 — Pinning residuals and the positional check (applies to both packages)** (note)

[Observed] My survivors are listed under Mechanics. The material one is the
target definition. "A link's target is its resolved `href`" and "a
`summary`'s controlled region is its `details` element" (`:10-11`) can be
rewritten with no finding, though the distinct-name rule turns on them.
Only the button and form-control half of that sentence is pinned.

On the positional check (`position_findings`, identical in both builders):

- It fails closed. An absent predecessor is reported as "not unique": a
  misleading message, but still a finding.
- A signed replaced line that is no longer in the current block makes
  `old.index(line)` raise `ValueError`. `--check` then exits non-zero with
  a traceback, not a finding. That still fails closed, but it names
  nothing.
- The function is duplicated verbatim across two builders instead of living
  in the engine. The dispositions explain this by the concurrent P-85 and
  P-86 lanes. The next engine edit should absorb it.

**Finding 10 — Composition with the release-label lane is verified only for its spec patch as it stands at this commit (applies to both packages)** (note)

[Observed] At `d6b3784f`:

- This builder's `--check` composes all four pending spec patches, pairwise
  and in every order.
- My own loop reproduces that: 24 of 24 orders, 1 result.
- The class-granular (P-86) builder's `--check` passes.
- The release-label (P-85) builder's `--check` fails on its stale
  `GOVERNING-DEPENDENCIES.md.patch`, so its full proposed subject set,
  manifest and coverage regeneration could not be checked at this commit.

[Unknown] Whether the spec patch its lane regenerates will be
byte-identical to the one composed here. This builder's `--check` composes
whatever lands, live, and the packet's "whichever is signed second is
regenerated … and reviewed again" covers the manifest. Re-run this
builder's `--check` once P-85 lands.
