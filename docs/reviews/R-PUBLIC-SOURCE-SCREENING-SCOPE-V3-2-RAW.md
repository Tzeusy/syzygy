# R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2 — public-source screening scope, version 3, review round 2
Reviewed commit: 5db1dd720338edd7963653f7e19ff727e1e99f32
Manifest SHA-256: e5328701c62fa567d9f8dcc4d11c80266638b28bc368212b264514052bcec9e3
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08. Brief:
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v3/REVIEW-BRIEF.md`
at the reviewed commit. All reads and runs used a detached scratch worktree
at that commit. Nothing was committed. Before reviewing I read the round-1
raw (`docs/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-1-RAW.md`), as the
brief's recording section requires for round 2.

`Manifest SHA-256` is the SHA-256 of the manifest **file**. I computed it two
ways and both agree [Observed]:

- `python3 scripts/build_public_source_screening_scope_v3.py --manifest-digest`;
- `sha256sum` over `PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt`.

As an independent check of the manifest's subject, I applied each patch with
GNU `patch -o` to the policy on disk, which hashes to `98a87f81…`. The output
hashes equal the two manifest rows [Observed].

## Summary

Both revise findings from round 1 are repaired in the normative bytes, and
the four notes are taken.

- The render condition now defines a page and a page sink. It sends every
  other place a body reaches to a new `egress` clause.
- `renderRule` binds every body in all three strings that carry the
  exception. The selftest has a mutant for each.

My sink sweep found no place where an exempt body, or a span of it, reaches
an HTML or SVG document without `escape` or without the CSP. It found no
other destination where a body is written without encoding for that
destination. The same sweep found no page that delivers its CSP after body
bytes.

Three notes remain:

- The Redis sitting installer, which the ledger names as the place the
  re-point set is derived, knows only versions 1 and 2. It will refuse after
  a version-3 act.
- The parser-based definition of "page" leaves XHTML and
  Markdown-rendered documents to `egress`, which does not require a CSP.
- Two attribution and wording slips.

## Round-1 findings: repairs checked against the round-1 raw

**Round-1 Finding 1 (revise): `renderCondition` did not define a sink, and read literally it withdrew the exemption at every non-HTML sink.** Repaired.

[Observed] The new `renderCondition` in both patches opens:

> "a page is a document an HTML or SVG parser reads, and a page sink is a
> place where such a body's bytes, or a span of them, are written into a
> page."

It closes:

> "Every other place such a body or a span of it reaches is not a page sink;
> egress governs it"

The new `egress` reads:

> "At every place that is not a page sink (a review packet, a provider
> request, a discovery excerpt, a stored record), an exempt body or a span of
> it counts as screening-admitted code-content … and is encoded for that
> destination's format as renderRule requires"

The round-1 repair asked for a sink definition and an `egress` rule for
other sinks, and the bytes now contain both.

The other parts of the finding are repaired as follows [Observed]:

- REQ-035. The delta (`SEMANTIC-DELTA.md:225-232`) reads "screening-admitted"
  as "one answer per body, never per sink", and `egress` says this in the
  bytes.
- The three body call sites. The ledger (`IMPACT-LEDGER.md:61-64`) names
  `repo-corpus.ts:227`, `check.ts:577` and `review.ts:188`. It also says
  that `screenBody(body)` carries no path, so the change must supply one.
- The owner packet. Its line 59 says exempt files go "in review packets for
  your sessions, and sent to a provider in provider mode". That now agrees
  with `egress`.

**Round-1 Finding 2 (revise): the bytes lifted the whole base `activeContentClassification`, `renderRule` included.** Repaired.

[Observed] The three strings now read as follows.

- `inheritedRules`:

  > "activeContentClassification (except that, for a body
  > activeContent.codeContentExemption exempts, its active-content forms are
  > not scanned for and malformedContextAction does not apply; its renderRule
  > binds every body)"

- `activeContent.rule` ends:

  > "… except the steps codeContentExemption.rule lifts for a body it
  > exempts: … and renderRule binds every body"

- `codeContentExemption.rule` ends:

  > "The exemption reaches those three steps and nothing else:
  > activeContentClassification.renderRule, and the encoding of selected text
  > for its destination, still bind such a body at every place it reaches"

`malformedContextAction` and `renderRule` are real keys of the base
`activeContentClassification`. Its keys are `inertMarkdownContexts`,
`inertContextRule`, `markdownProfile`, `excludedOutsideInertContexts`,
`unsafeUrlSchemes`, `malformedContextAction` and `renderRule` [Observed].

The selftest prints three new predicates, each `ok` [Observed]:

- "an exemption rule that drops renderRule caught";
- "inheritedRules that lift renderRule caught";
- "an active-content rule that lifts renderRule caught".

**Round-1 Finding 3 (note): three CSP readings could meet the words with an ineffective policy.** Taken.

[Observed] The condition now requires the following, which closes all three
readings:

> "an enforced Content-Security-Policy, delivered before any of the body's
> bytes, whose default-src source list is exactly 'none' and which carries no
> script-src, script-src-elem, script-src-attr or object-src directive"

The selftest has a mutant for each phrase.

**Round-1 Finding 4 (note): `non-web`'s stated reason did not separate its seven extensions.** Taken.

[Observed] The `non-web` `appliesTo` now says those seven "are the
browser-side and server-templating languages, chosen as the variant's
criterion and not as a claim that other languages carry no HTML".

**Round-1 Finding 5 (note): the delta's `[Unknown]` about REQ-012's warrants could be closed.** Taken.

[Observed] `SEMANTIC-DELTA.md:233-243` lists RFC7-13, 14, 33 and 34. I
re-derived each line cited for them:

- `narrative-contract.md:306` and `:324`;
- `rendering-and-surface.md:205` and `:241`.

Each line is the clause's own heading.

**Round-1 Finding 6 (note): install omissions.** Taken.

[Observed] The ledger now names:

- both version-2 battery lines in both places, and the replacement as one
  CG-26 triple;
- the six CG-7e failures;
- the historical pinning;
- the pre-existing app act port (`syzygy-p83h`).

[Observed] `check_governance.py` adds
`_activate_public_source_scope_v3_copy_registry`, gated on the existence of
both the version-3 act record and the manifest. This registers the manifest
at drafting time, as AGENTS.md asks. Note 1 below adds one omission.

## Criteria, applied afresh

### 1. Is the diff exactly the stated change? — yes

- [Observed] `--check`: `public-source-screening-scope-v3: patches and manifest current`.
- [Observed] `--selftest`: `33 of 33 predicates held`.
- [Observed] Second method: GNU `patch -o` over the policy on disk.
  - `all` → `c13bd56c…`;
  - `non-web` → `61f384d4…`.

  Each equals its manifest row.
- [Observed] I ran my own JSON tree diff (not the builder) of each patched
  file against the base. It changes exactly:
  - `/policyVersion`;
  - `/publicSourceScope/activeContent/{rule, consequence}`;
  - `/publicSourceScope/activeContent/codeContentExemption` (added);
  - `/publicSourceScope/inheritedRules`.

  This is the same for both variants.
- [Observed] Exemption lists, measured against
  `/publicSourceScope/contentClassification/rules/1/sourceExtensions` (25):
  - `all` exempts 25, with none extra;
  - `non-web` exempts 18 and leaves out exactly
    `.js .mjs .cjs .jsx .php .ts .tsx`.

### 2. Is the base right? — yes

- [Observed] The policy on disk hashes to `98a87f81…`, which is the version-2
  `none` row that round 1 confirmed.
- [Observed] I simulated a version-3 act by copying the patched `non-web`
  bytes over the policy in the scratch worktree. `--check` still prints
  `patches and manifest current`.
- [Observed] The selftest's "after a variant-all act" and "after a
  variant-non-web act" predicates hold. I restored the file afterwards, and
  `git status --short` printed nothing.

### 3. Is the render claim true? — yes for every sink the code has today; one wording note (Note 2)

**Re-derived citations in "Why"** [Observed, each line read at this commit]:

- `git-object-reader.ts:164` is `HTML_TAG`, the cited pattern.
- `git-object-reader.ts:191` is `scanActiveContent`.
- `screen.ts:85` and `public-source-screening.ts:138` each call
  `scanActiveContent(body)` inside `screenBody`.
- `render.ts:276` is `generationSourcesForBody(… body: blob.raw)`.
- `render.ts:350` is the quotation segment cut from `blob.raw`.
- `dossier-render.ts:129` is `page()`, emitting `DRAFT_PREVIEW_CSP_META`.
- `dossier-render.ts:261` is `<q class="verified-quote">…${escape(part.text)…}</q>`.
- `dossier-render.ts:409` is `<blockquote class="exact-source">…${escape(span.text)…}</blockquote>`.
- `dossier-render.ts:440-452` is the machine view. `quotations` carries
  page, block, source, offsets and anchor, but no text.
- `draft-preview.ts:18` is the CSP:
  `default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'`.
- `draft-preview.ts:24` is `escape` over `& < > " '`.
- `draft-preview.ts:122` is `escape(source.spans[0]!.text)`.
- `pipeline.ts:265` maps spans to `{ sourceId, anchorId, text }`.
- `discovery.ts:290` builds the excerpt.
- `repo-corpus.ts:227` calls `screen?.screenBody(body)`.

**Sweep A: every screen and scan call site.** These are non-test,
non-`dist` source files under `packages/` and `apps/` [Observed,
`git grep`]:

- `screenBody(` has 6 call sites.
  - 3 screen a blob body: `repo-corpus.ts:227`, `check.ts:577` and
    `review.ts:188`.
  - 3 screen agent text for the secret result only: `render.ts:257`,
    `render.ts:360` and `close.ts:124`.
- `scanActiveContent(` has 6 sites:
  - the two screens;
  - the definition;
  - three Butlers base-scope sites: `verbatim-route.ts:124`,
    `content-classification.ts:195` and `git-object-reader.ts:368`.

  [Inferred] `inheritedRules` keeps this scope's rules out of the base scope,
  so the exemption does not reach the Butlers sites.

**Sweep B: every file writer that could carry a body.** Under `packages/`
and `apps/` there are 30 non-test source files that call `writeFile*`,
`appendFile*` or `createWriteStream` [Observed]. The 17 in `polaris-dossier`
(11) and the app's `polaris-generation/` (6) are the only ones on a
public-target path. I read each write in them:

- `render.ts:226` writes the renderer's file map. The renderer emits only
  these, by its `files.set` sites at 325, 423, 429, 432 and 440:
  - `.html` pages built by `page()`;
  - `dossier.json`, `size-report.json` and `machine.json`, which hold no span
    text.

  No standalone `.svg`, `.md` or `.xhtml` is emitted. Diagrams are inline
  SVG inside a page, with labels escaped and checked by `assertInertSvg`.
- `review.ts:260` and `session-handover.ts:251` write the review packets,
  which are JSON and therefore non-page.
- `check.ts:352/378` and `review.ts:473/474` write the frozen subject and the
  check record. The check findings carry line counts and a citation id, not
  body text.
- `brief.ts` writes the brief and schema, and `inventory.ts` and
  `session-handover.ts:192` write the inventory brief. None carries a body
  span.
- `pipeline-demo-main.ts` and `self-corpus.ts:141` call `renderDraftPreview`
  over synthetic or Syzygy-own corpora. `dossier-render-main.ts:60` writes
  the `renderDossier` file map. `dossier-main.ts:20` passes `renderDossier`
  to `runDossierTrigger`. I did not trace that trigger's writer beyond this
  point [Unknown]. It renders through the same `page()`.

**Sweep C: renderer callers.** `renderDossier(` and `renderDraftPreview(`
have 5 non-test call sites [Observed], and none is a daemon route.

**Result.** Each `page()` and `renderDraftPreview` page emits the CSP meta in
`<head>` before `<title>` and before any body content. The path-derived
`<title>` is escaped. Every body or span that reaches a page goes through
`escape` [Observed]. Round 1's interpolation-by-interpolation sweep of the
three renderer files covered 359 interpolations. I did not repeat it. I
re-read every line in those files that names `spans`, `.text` or `excerpt`
(the grep above), and each is escaped.

**Can a CSP meet the words and still run script or a plugin?** [Inferred,
general CSP3 knowledge, not tested in a browser] No, for content the page
did not mint:

- The words require an enforced policy whose `default-src` list is exactly
  `'none'`. They also forbid `script-src`, `script-src-elem`,
  `script-src-attr` and `object-src`.
- Script falls back to `default-src 'none'`, and so do plugins (`<object>`
  and `<embed>`, via `object-src`).
- A second policy can only narrow.
- Directives the words leave open (`frame-src`, `child-src`, `worker-src`,
  `style-src`, `base-uri`, `form-action`) admit no script in this document.
  Each also needs a minted element, which the encoding half forbids.

### 3a. Is the reading of the affected requirements sound? — yes

- [Observed] REQ-012, at base `spec.md:636-648`, says "render untrusted source
  and provider content inertly" and "rendering executes none of that
  content". The overlay at `spec.md:362-372` carries the same opening
  sentence and scenario.
  - Nothing in the text requires withholding a body that carries
    markup-like bytes. Encoding under a no-script CSP meets "inertly"
    [Inferred].
  - "Excluded or unclassifiable content is not revealed" is not reached by
    an admitted body.
- REQ-012's warrants are `contracts: [RFC7-13, RFC7-14, RFC7-33, RFC7-34]`
  (`spec.md:682`). Round 1 read each, and none states a stricter rendering
  rule. I re-derived only their locations.
- [Observed] REQ-033's screening sentence (local-agent `spec.md:13`) says
  "every object SHALL be classified and screened … before its content is
  used in a check or rendered". Every body is still classified and every
  detector still runs, so 033 is met unchanged.
- [Observed] REQ-035 (`spec.md:320`) says "screening-admitted only". It is
  read as one answer per body, and `egress` states that in the bytes.
- A page sink that cannot meet the condition rescans "for that sink". That
  is a further screen before rendering, which is consistent with 033.

### 4. Does every detector still run? — yes

- [Observed] The tree diff changes no detector path. The top-level
  `detectors`, `publicSourceScope.detectors` and `matchAction` are untouched.
- `codeContentExemption.rule` keeps "Every detector still runs over the
  whole body".
- `inheritedRules` still lists `detectors`.
- Base `classificationOrder` step 3 ("run every detector over transient
  bytes before parsing") and step 6 ("exclude the whole artifact on any
  match") are not among the three lifted steps.
- The selftest's detector and scope-detector mutants hold.

### 5. Is the loosening bounded? — yes

- [Observed] `appliesTo` requires the code-content class and an extension
  from `exemptExtensions`, compared case-sensitively.
  - A project-documentation body, or a code-content body that is not named,
    "is scanned as before".
  - The selftest's README fixture flip is caught.
- `non-web` is a defensible cut [Inferred]. JSX and template literals are
  the common false positives, and the criterion is now stated as a choice.
  Strictly, `.cjs` and `.mjs` are Node module forms rather than
  browser-side, but that only makes the cut more conservative.
- `all` is described honestly. Packet line 59 calls it "Widest: a JavaScript
  or PHP file full of HTML strings is admitted too, protected only by the
  escaping". That understates the protection, since the CSP also applies,
  so it errs toward caution.

### 6. Is the install requirement complete? — one omission (Note 1)

[Observed] Every item the ledger names is real at the cited lines:

- `POLICY_ACT_FORMS` at `package-reader.ts:346`, `namesPolicy` at `:371` and
  `readPolicyActs` at `:394`;
- `PUBLIC_SOURCE_ACT_RECORD_PATH` at `public-source-screening.ts:51`,
  `checkoutPolicyActPort` at `:72` and the "no production caller" comment at
  `:36`;
- the shared `publicSourceContentClass` import at `screen.ts:5` and
  `public-source-screening.ts:43`.

I simulated the act with the `non-web` bytes [Observed]:

- the v2 recorder's `--selftest` raises the `ValueError` from
  `build_public_source_screening_scope_v2.py:378`, as the ledger now says;
- the builder `--check` passes.

`check_governance.py` at the unmodified head prints `32 OK, 21 WARN, 0 FAIL
(53 checks)`. I did not re-run it under the simulation, since round 1
reported the six CG-7e findings and the ledger now names them.

### 7. Authority — clean

- [Observed] I ran a Python `re` sweep for the words "accepted", "approved",
  "adopted" and "in force" (case-folded, word-bounded) over the 7 package
  files and the builder. It finds:
  - the brief's own criterion;
  - "leaves version 2 in force" (`SEMANTIC-DELTA.md:275`);
  - the base policy's own words in patch context;
  - the builder docstring's "approved 2026-10-07", about version 2.

  None labels this package's material.
- [Observed] 64-hex tokens: 2 in the manifest and 0 in every Markdown file
  of the package.

## Findings

**Finding 1 — the installer the ledger names as the derivation point knows only versions 1 and 2** (note)

`IMPACT-LEDGER.md:22-25` says the re-pointed set comes from "the recorded act
at the sitting (`scripts/install_redis_sitting.py`, step `policy`), not from
this page".

[Observed] The installer's `policy_acts` (`install_redis_sitting.py:877-897`)
reads only `SCOPE_ACT` (v1) and `V2_ACT`. It then refuses unless the policy
on disk hashes to the last of those:

> "the policy on disk does not hash to the final policy act's argument"

Its selftest predicate "a policy that is not the final act's argument is
refused" holds. Several other parts of the installer branch only on
`final.key == "v2"`:

- `gate_comment`;
- the check_governance chain edits (`policy_cg_v2_edits`);
- the battery edit.

[Inferred] After a version-3 act, the installer's `policy` step refuses
rather than deriving anything. The direction is fail-closed. Its `--check`
already refuses at this head for missing provider-route and egress records.

`scripts/simulate_redis_sitting.py:96` and `:529` also hard-code the version-2
recorder. The ledger lists `simulate_redis_sitting.py` only as "[Unknown at
drafting]".

Separately, and not caused by this package: the installer's `--selftest`
prints `74 of 77 predicates held` at the unmodified head, with three
"chain edits" predicates failing. I got the same 74 of 77 with the
simulated act.

Repair: name `install_redis_sitting.py` (`policy_acts`, `gate_comment`,
`policy_cg_v2_edits`) and `simulate_redis_sitting.py` as code that must learn
version 3. Alternatively, say that the version-3 install is a hand-written
change that does not run through that installer.

**Finding 2 — "page" is defined by parser, so an XHTML or Markdown-rendered destination falls to `egress`, which requires no CSP** (note)

`renderCondition` defines a page as "a document an HTML or SVG parser reads".
[Inferred] Two kinds of document fall outside that definition while still
being able to run markup:

- a document served as `application/xhtml+xml`, which is read by the XML
  parser;
- a Markdown file that a viewer later renders to HTML.

Each falls to `egress`. There the body must be "encoded for that
destination's format as renderRule requires", but no CSP is required.
`renderRule` still forbids minting an element or a handler, so encoding still
protects the body. But the defence-in-depth that `renderCondition` demands
for a page is absent there.

[Observed, Sweep B] No such sink exists today: the site holds `.html` and
`.json` files only.

Suggested words: "a document an HTML, XHTML or SVG parser reads, or any
document a consumer renders to one".

**Finding 3 — two attribution and wording slips in the package prose** (note)

- `IMPACT-LEDGER.md:11` ("round-1 review finding 7") and `:119` ("round-1
  review, finding 5") refer to the PR #404 round-1 raw. That raw's Finding 7
  is the version pin and its Finding 5 is the egress population [Observed].
  The package's own round 1 has six findings, and its Finding 5 is the RFC7
  warrants. The delta qualifies "round-1 review of PR #404" once (line 144)
  and uses a bare "round 1" for the package's own review elsewhere. Qualify
  both ledger citations.
- `SEMANTIC-DELTA.md:150-151` says both page builders "emit the meta first in
  `<head>`". [Observed] It is the third element, after `<meta charset>` and
  the viewport meta (`dossier-render.ts:129`, `draft-preview.ts:124`). The
  property the condition needs, "before any of the body's bytes", holds.
  "First" is not true. Say "in `<head>`, before `<title>` and any body
  bytes".

## Not done

- I did not run `npm ci`, `npm` tests, browser tests or the full
  `PROJECT-STATUS.md` battery. Every run was Python:
  - the builder's `--check`, `--selftest` and `--manifest-digest`;
  - `check_governance.py`;
  - the v2 recorder's `--selftest` and the installer's `--selftest` and
    `--check`, both before and after the simulated act;
  - GNU `patch`;
  - my own tree-diff and authority-sweep scripts.
- I did not re-read every interpolation in the three renderer files, which
  round 1 did (359). My HTML sweep re-derived the cited lines, every
  body-text line, every file writer and every renderer caller.
- I read no target-repository content and no run directory.
