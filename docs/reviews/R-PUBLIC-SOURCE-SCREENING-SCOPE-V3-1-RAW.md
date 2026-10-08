# R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-1 — public-source screening scope, version 3, review round 1
Reviewed commit: 897910fcc1a186b91d436796bc6e5330836c60c1
Manifest SHA-256: 701287461d2bd90edcca48e308c976a633d5869964d0fb61bcf73ac392ec6f9b
Verdict: REVISE

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08. Brief:
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v3/REVIEW-BRIEF.md`
at the reviewed commit. Every read and run was against a detached scratch
worktree at that commit; nothing was committed. I did not read any prior
review raw of this subject or of the blockers packet.

`Manifest SHA-256` is the SHA-256 of the manifest file. I computed it two
ways: `build_public_source_screening_scope_v3.py --manifest-digest` and
`sha256sum` over
`PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt`. Both give the value in the
head.

## Summary

The diff is exactly the stated change, the base is right, every detector
still runs, and authority labelling is clean. My sweep found no HTML sink
where a target body or a span of it reaches a page unescaped or without the
CSP. The render claim holds for every page the code builds today.

Two revise findings remain, and both are in the normative bytes the owner
would sign:

- The `renderCondition` is stated per "sink" but defines only an HTML page.
  Read literally, it fails at every non-HTML sink an admitted body reaches:
  the fidelity review packet, the provider request and the discovery
  excerpt. There the consumer must scan again and exclude. That contradicts
  the packet's statement that exempt files go into review packets and to
  providers, and it leaves REQ-035's "screening-admitted" sink-relative.
- The bytes lift the whole base `activeContentClassification` for an exempt
  body, its `renderRule` included, not only the scan.

## Criteria

### 1. Is the diff exactly the stated change? — yes

- [Observed] `--check`: `public-source-screening-scope-v3: patches and manifest current`.
- [Observed] `--selftest`: 26 of 26 predicates held.
- [Observed] Second method, independent of the builder: I applied each patch
  with GNU `patch -o` to the policy on disk (sha256 `98a87f81…`). The
  outputs hash to the manifest rows: `8f70c736…` for `all` and `44b8aab8…`
  for `non-web`.
- [Observed] A JSON tree diff of each patched file against the base (my own
  script, not the builder) shows exactly these paths changed:
  - `/policyVersion`;
  - `/publicSourceScope/activeContent/{rule, consequence}`;
  - `/publicSourceScope/activeContent/codeContentExemption` (added);
  - `/publicSourceScope/inheritedRules`.

  Nothing else moves. That is the three stated values.
- [Observed] Exemption lists:
  - `all`: 25 of 25 `sourceExtensions`.
  - `non-web`: 18. The 7 not exempt are `.js .mjs .cjs .jsx .php .ts .tsx`.

### 2. Is the base right? — yes

- [Observed] The version-2 manifest row `none` is `98a87f81…`, the same as
  the policy on disk and as the `Exact digest` in
  `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md:17`.
- [Observed] I simulated a version-3 act in the scratch worktree by writing
  the `non-web` row's bytes over the policy. `--check` still printed
  `patches and manifest current`. The selftest covers both variants. I
  restored the file afterwards.

### 3. Is the render claim true? — for HTML pages, yes; see Finding 1 for non-HTML sinks

**Re-derived citations.** I checked each line against its file [Observed]:

| Citation | What is there |
|---|---|
| `git-object-reader.ts:164` | `HTML_TAG` |
| `git-object-reader.ts:191` | `scanActiveContent` |
| `screen.ts:85` | the `screenBody` definition |
| `public-source-screening.ts:138` | the `screenBody` definition |
| `polaris-dossier/src/render.ts:276` | `generationSourcesForBody` |
| `polaris-dossier/src/render.ts:350` | the quotation segment from `blob.raw` |
| `dossier-render.ts:129` | the CSP meta in `page()` |
| `dossier-render.ts:261` | `escape(part.text)` in `<q>` |
| `dossier-render.ts:409` | `escape(span.text)` in `<blockquote>` |
| `dossier-render.ts:440-452` | the machine view: offsets and anchors, no span text |
| `draft-preview.ts:18` | the CSP |
| `draft-preview.ts:24` | `escape` over `& < > " '` |
| `draft-preview.ts:122` | `escape(source.spans[0]!.text)` |

- [Observed] Python `re` with the cited pattern on `if (a<b && c>d) x();`
  returns `<b && c>`.
- [Observed] Of the delta's spec citations:
  - base `spec.md:641` and overlay `spec.md:366` are each the
    `ID: REQ-polaris-generation-012` line;
  - base `spec.md:682` is the `contracts:` warrant line;
  - local-agent `spec.md:31` is REQ-033's ID line;
  - local-agent `spec.md:320` lies inside REQ-035, whose ID line is 328.

**Sweep 1: every HTML emitter.** The population is the non-test `.ts`
files under `packages/` and `apps/` (no `dist/`) that contain a closing tag
of `p, div, li, span, a, section, q, blockquote, pre, code, td, h1-h6,
main, body, svg, text, title`. There are 24 [Observed].

- 5 are under `apps/three-surface-poc/src/polaris-generation/`:
  `diagram-layout.ts`, `dossier-render-local.ts`, `dossier-render.ts`,
  `draft-preview.ts` and `svg-inert.ts`.
- The other 19 contain none of the strings `polaris-generation`,
  `GenerationSource`, `public-source`, `publicSource`, `repo-corpus` or
  `polaris-dossier` [Observed]. They are the Butlers POC surfaces and the
  Capability 1 daemon. [Inferred] No public-target body reaches them. I
  checked direct references only and did not trace transitive data flow.
- [Observed] No source file uses `innerHTML`, `outerHTML`,
  `insertAdjacentHTML`, `document.write` or `dangerouslySetInnerHTML`
  except `orrery.ts:82` (`canvas.innerHTML = ''`).
- [Observed] No package manifest depends on a Markdown or HTML renderer
  (`marked`, `markdown-it`, `remark*`, `rehype*`, `micromark`, `showdown`,
  `commonmark`, `mermaid`, `jsdom`, `dompurify`, `sanitize-html`).
- [Observed] No daemon route serves a dossier or draft. `routes.ts` has one
  `text/html` responder, for `PocModel` pages, and nothing in `routes*.ts`,
  `server*.ts`, `main*.ts` or `cap1-daemon/src/` names a draft, dossier or
  run directory. Dossier pages exist only as static files in `site/<n>/`,
  where the meta CSP still applies.

**Sweep 2: every interpolation in the three renderer files.** I extracted
every `${…}` with balanced braces [Observed]:

| File | Interpolations | Led by `escape(` | Not led by `escape(` |
|---|---|---|---|
| `draft-preview.ts` | 79 | 29 | 50 |
| `dossier-render-local.ts` | 25 | 13 | 12 |
| `dossier-render.ts` | 255 | 98 | 157 |

I read every one of the 219 not led by `escape(`. Each is one of:

- a number or byte offset;
- a SHA-256 slice;
- a constant (`DRAFT_PREVIEW_CSP_META`, CSS, `MARKING_LABEL[m]`);
- an internal tag or attribute string;
- composed markup whose text leaves were escaped where they were built;
- an id or href that the enclosing call wraps in `escape(`. For example,
  `dossier-render.ts:367` writes `escape(href(…, \`section-${parent.id}\`))`.

`diagram-layout.ts` escapes every label at 177, 183 and 191. Its attribute
values are numbers, a path built by the layout, or ids and classes built by
the module (its comment at 160 says so, and the code agrees). `svg-inert.ts`
is a validator.

[Observed] The sweep found no HTML sink where a body or a span reaches
markup without `escape`, and none where a page lacks the CSP. Both page
builders (`page()` and `renderDraftPreview`) emit `DRAFT_PREVIEW_CSP_META`
in `<head>`, before any body content.

**Sweep 3: every call site that screens a read blob body.** `screenBody(`
appears at 6 non-test call sites [Observed]:

- 3 screen a blob body:
  - `repo-corpus.ts:227`;
  - `polaris-dossier/src/check.ts:577`;
  - `polaris-dossier/src/review.ts:188`.
- 3 screen agent text for the secret result only:
  - `render.ts:257`;
  - `render.ts:360`;
  - `close.ts:124`.

The sinks downstream of the three body sites are:

- HTML: the dossier pages and the draft preview, which meet the condition.
- The fidelity review packet, written as JSON to a session the operator
  starts. Span text is carried raw at `review.ts:197-226`.
- The design review packet, which carries the rendered pages, CSP included.
- Provider mode: the author request (`pipeline.ts:265`) and the discovery
  excerpt (`discovery.ts:290`).

**Can a CSP meet the words and still run script or a plugin?** [Inferred,
from general knowledge of CSP Level 3, not tested here] Not for the page
itself, when "default-src is 'none'" is read as the exact source list
`'none'`:

- `script-src-elem` and `script-src-attr` fall back to `script-src`, then to
  `default-src`.
- `worker-src` falls back through `child-src` and `script-src`.
- `object-src` covers `<object>` and `<embed>`.
- `style-src 'unsafe-inline'` runs no script in current browsers.

Three edge readings are in Finding 3.

### 3a. Is the reading of the affected requirements sound? — yes, with one consequence unaddressed

- [Observed] REQ-012's words, at base `spec.md:636-648`, are "Generated
  pages SHALL render untrusted source and provider content inertly" and the
  scenario "rendering executes none of that content and the workflow obtains
  no new authority from it". They are about how content renders, not
  whether markup-bearing bytes are admitted. Entity encoding with no
  element minting, under a CSP that admits no script, meets "inertly"
  [Inferred]. I cannot find text that requires withholding a body which
  carries markup-like bytes. The third line, "excluded or unclassifiable
  content is not revealed", is not reached by an admitted body. The
  delta's reading stands.
- [Observed] The four contract warrants, in RFC-0007, are:
  - RFC7-13, progressive disclosure (`narrative-contract.md:306`);
  - RFC7-14, the verbatim leaf (`:324`);
  - RFC7-33, machine-readable distinctions (`rendering-and-surface.md:205`);
  - RFC7-34, non-visual recoverability (`:241`).

  None states a rendering-safety rule stricter than REQ-012. The delta's
  `[Unknown]` can be closed as "none stricter" (Finding 5).
- [Observed] SEC-3 ("Observed code is untrusted, everywhere") binds running
  observed code. Rendering source as encoded text under a no-script CSP
  runs nothing [Inferred]. The delta's "No SEC- clause is amended" holds.
- REQ-033's reading holds. Every body is still classified, and every
  detector still runs before use. REQ-035 is the one the delta does not
  address. It requires the fidelity packet's "cited spans SHALL be those
  cited by the draft and by the frozen inventory, screening-admitted only"
  (`spec.md:320`). Under the per-sink condition, "screening-admitted"
  becomes sink-relative. See Finding 1.

### 4. Does every detector still run? — yes

- [Observed] The top-level `detectors`, `publicSourceScope.detectors`
  ("including inert code contexts") and `matchAction` are byte-identical
  across both variants (tree diff above).
- [Observed] `codeContentExemption.rule` keeps "Every detector still runs
  over the whole body".
- [Observed] `inheritedRules` still lists `detectors`. The base
  `markdownProfile.precedence` says the mask "never [applies] to secret
  detectors". With no scan, no mask is computed, so detectors see the whole
  body.
- [Observed] The selftest mutants for detector, scope detector and
  dropped-detector-sentence changes each fire.

### 5. Is the loosening bounded? — by class and extension yes; by rule, no (Finding 2); `non-web` is a defensible cut with an indefensible stated reason (Finding 4)

- [Observed] Both variants bound the loosening:
  - `appliesTo` requires the code-content class and an exempt extension,
    compared as `sourceExtensions` are;
  - fixtures pin `README.md` and `docs/guide.md` as not exempt, and
    `src/server.C` as not exempt (case);
  - project-documentation bodies are "scanned as before".
- [Observed] The owner packet's option A
  (`DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md:59`) states the widest
  cost plainly: "a JavaScript or PHP file full of HTML strings is admitted
  too, protected only by the escaping". "Only by the escaping" understates
  the protection, since the CSP also applies, but it errs toward caution.
  It is honest about `all`.
- The same cell says every newly admitted file can be "put in review packets
  for your sessions, and sent to a provider in provider mode". That depends
  on the reading Finding 1 says the bytes do not support.

### 6. Is the install requirement complete? — mostly; omissions in Finding 6

[Observed] Each item the ledger names is real and correctly located:

- `POLICY_ACT_FORMS` at `package-reader.ts:346`, `namesPolicy` at `:371`
  and `readPolicyActs` at `:394`;
- the v2 recorder lines in `PROJECT-STATUS.md:403-404` and
  `governance-docs.yml:222-226`;
- the two consumers;
- the Butlers pins.

I re-ran the version-literal sweep with `git grep -nF` and got the same 6
tracked non-governance files the ledger names. Omissions found by simulating
the act are in Finding 6.

### 7. Authority — clean

- [Observed] `grep -inE "accepted|approved|adopted|in force"` over the
  package and the builder finds only:
  - the brief's own criterion;
  - "leaves version 2 in force" at `SEMANTIC-DELTA.md:205`, which is true
    of a performed act;
  - the base policy's own words, inside the patch context;
  - the builder docstring's "approved 2026-10-07", about version 2.

  None labels this package's material.
- [Observed] 64-hex tokens in the package: 2, both in the manifest. None
  are in Markdown. The builder's own Markdown predicate agrees.
- [Observed] `check_governance.py` at the reviewed commit: `32 OK, 21 WARN,
  0 FAIL (53 checks)`.

## Findings

**Finding 1 — `renderCondition` does not say what a "sink" is, and read literally it withdraws the exemption from every non-HTML sink an admitted body reaches** (revise)

The condition reads "the exemption holds for a sink only while that sink
renders such a body, or any span of it, as text". It then names character
references, no Markdown or HTML parsing, and "the page carries a
Content-Security-Policy…". Its fallback is: "A consumer that cannot confirm
this for a sink scans the body as before for that sink, and excludes it
whole on a finding".

[Observed, Sweep 3] An admitted public body reaches three sinks that are not
pages:

- the fidelity review packet, written as JSON and given to an agent session
  (`review.ts:188` screens the body; `review.ts:197-226` writes span text
  raw into `packet.json`);
- the provider author request (`pipeline.ts:265`);
- the discovery excerpt (`discovery.ts:290`).

None writes `<` as a character reference, and none has a page or a CSP. On
the words, each must re-scan and exclude. Then:

- [Inferred] A quotation from an exempt C file would render on the page,
  where `check.ts:577` admits it, but be absent from the fidelity packet.
  The reviewer could not judge the block, so it renders Unknown. The C
  files would stay out of exactly the reviews that make their claims
  Inferred.
- REQ-035's "screening-admitted only" becomes sink-relative, which no text
  addresses.
- The packet (`DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md:59`) and the
  ledger ("What Syzygy transmits") say exempt files go into review packets
  and to providers. The `egress` clause presumes the same. The bytes say
  the opposite.
- The ledger's install instruction ("skip the scan only for a code-content
  body whose extension it lists") makes no per-sink decision. It names the
  two `screenBody` definitions but not the three body call sites, whose
  signature (`screenBody(body)`) carries no path or sink.

The direction is fail-closed, so this is not a hazard. But the owner would
sign bytes whose effect at three of the five downstream sinks is
undetermined, and two documents in the same package describe the opposite
effect.

Repair: define the sink in the bytes. For example, "a sink is a place where
the body's bytes, or a span of them, are written into a document an HTML or
SVG parser reads". Then say what governs every other sink: the `egress`
clause, with the body encoded for its destination's format. Alternatively,
keep the literal reading and correct the packet, the ledger and REQ-035's
reading to match. Either way, name the three body call sites in the ledger.

**Finding 2 — the bytes lift the whole base `activeContentClassification` for an exempt body, not just the scan** (revise)

The delta calls the change admission "without the active-content scan", and
`codeContentExemption.rule` lists three things that do not apply: step 4,
the active-content condition of `classificationSuccess`, and the
malformed-code-context exclusion. Two other strings in the same patch are
wider:

- `activeContent.rule` applies "the base activeContentClassification,
  inertContextRule and the active-content condition … to every admitted body
  that codeContentExemption does not exempt";
- `inheritedRules` applies "activeContentClassification (except where
  activeContent.codeContentExemption exempts a body)".

[Observed] The base `activeContentClassification` also holds `renderRule`:
"admitted Markdown is never rendered as HTML; selected text is encoded for
its destination and code-context bytes never mint a link, element,
attribute, script or handler". For an exempt body, these two strings lift
that rule too. `renderCondition` restates the HTML half, and more strictly,
but only as a condition on the exemption. "Selected text is encoded for its
destination" is gone for every non-HTML destination. The delta's "What it
does not change" list does not mention this, and the selftest has no
predicate for it.

Repair: scope both exceptions to the steps `codeContentExemption.rule` names.
For example: "activeContentClassification (except that, for a body
activeContent.codeContentExemption exempts, its active-content forms are not
scanned for and malformedContextAction does not apply)". Leave `renderRule`
binding, and add a selftest mutant that drops it.

**Finding 3 — three CSP readings can satisfy the words of `renderCondition` with an ineffective policy** (note)

[Inferred, general knowledge of CSP3 and browser behaviour; not tested
here] None of the three lets a body run script while the encoding half of
the condition also holds. Each is only a gap in the CSP half's wording:

- "whose default-src is 'none'" does not say "exactly". CSP3 browsers
  ignore `'none'` when other source expressions sit beside it (Chromium
  warns and drops it). So `default-src 'none' 'unsafe-inline'` would admit
  inline script through the fallback while arguably "being 'none'".
- `Content-Security-Policy-Report-Only` enforces nothing, and "carries a
  Content-Security-Policy" does not exclude it.
- A `<meta>` policy governs only content parsed after it. A sink that
  emitted the meta after the quoted text would "carry" a CSP that does not
  cover it.

Today's builders emit the exact list, enforced, first in `<head>`
[Observed]. Suggested words: "an enforced Content-Security-Policy, delivered
before any of the body's bytes, whose default-src source list is exactly
'none'".

**Finding 4 — `non-web`'s stated reason does not distinguish its seven extensions** (note)

The `non-web` `appliesTo` writes into the policy that `.js .mjs .cjs .jsx .ts
.tsx .php` are kept "because those languages commonly carry HTML in their
source". [Inferred] So do the exempt ones: Python (template strings,
Django/Jinja), Ruby, Go (`html/template` strings), Java, C# and shell
heredocs.

The cut is defensible on a different ground: those seven are the
browser-side and templating languages, where JSX and template literals are
the common false positives. That is also how the packet's option B
describes it. As written, the reason is an unlabelled empirical claim in
normative bytes, and it does not justify the cut it makes.

Replace it with the actual criterion, or label it [Inferred]. This does not
affect `all`.

**Finding 5 — the delta's `[Unknown]` about REQ-012's contract warrants can be closed** (note)

[Observed] RFC7-13, RFC7-14, RFC7-33 and RFC7-34 bind, in turn:

- progressive disclosure;
- the verbatim leaf;
- machine-readable distinctions;
- non-visual recoverability.

None states a rendering-safety rule stricter than REQ-012. RFC7-33's
"copy-paste into an agent prompt" concerns distinctions that survive a
copy, not executable content. The delta can replace "[Unknown] whether any
of them states a stricter rendering rule" with this result.

**Finding 6 — install omissions surfaced by simulating the act** (note)

I simulated the act in the scratch worktree with the `non-web` row's bytes,
then restored the file [Observed]:

- `record_public_source_screening_scope_v2_act.py --selftest` crashes. It
  raises `ValueError: the policy on disk carries publicSourceScope but is
  neither the version-1 bytes nor this package's proposed bytes …` from
  `build_public_source_screening_scope_v2.py:378`. The ledger says the v2
  recorder's `--check` "fails by design" and that "its battery line" is
  replaced. There are two lines, `--check` and `--selftest`, in each of
  `PROJECT-STATUS.md` and the workflow, and both break.
- `check_governance.py` fails `CG-7e` with 6 findings:
  - the v2 manifest, the v2 act record (including its bare `Exact digest`
    at line 17) and `ACCEPTANCE-ACT-RECORD.md` each "does not contain its
    current argument";
  - the v3 manifest "is not in either act-copy registry".

  The ledger leaves `check_governance.py` at "[Unknown at drafting]". The
  v2 package has an existence-gated `_activate_public_source_scope_v2_copy_registry`;
  the v3 package registers nothing. AGENTS.md's recorder notes ask for that
  registration at drafting time. The v2 copies will also need historical
  pinning. A v3 recorder would resolve some of these findings, but not the
  historical pinning.
- Pre-existing, not created by this package: the app consumer's act reader,
  `checkoutPolicyActPort` in `public-source-screening.ts`, reads only the
  version-1 record (`PUBLIC_SOURCE_ACT_RECORD_PATH`). It requires the policy
  to hash to that record's single `Exact digest`, `d42defca…`. The policy has
  hashed to `98a87f81…` since the version-2 act, so `loadPublicSourceScreen`
  already refuses on the real checkout [Inferred from the code and the two
  records; not run]. The ledger lists this file as a consumer that must
  read `exemptExtensions`, but not that its act reader must move to the
  chain first. The file's own comment says it has "no production caller".

## Not done

- No `npm` test, browser test or full `PROJECT-STATUS.md` battery was run.
  The runs were the builder `--check`, `--selftest` and `--manifest-digest`,
  `check_governance.py` before and after the simulated act, the v2
  recorder `--selftest` after it, GNU `patch` and my own scripts.
- No target-repository content and no run directory were read.
- Whether the seven Redis C files would pass the secret detectors is not
  known here.
