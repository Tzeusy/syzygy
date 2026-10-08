# Semantic delta — public-source screening scope, version 3

> **Candidate — binds nothing.** Drafted 2026-10-08 for `syzygy-wsev`. Effect
> comes only from an owner `approve-policy` act over the exact proposed bytes
> of one manifest row. No repository body was read to draft it, and no act is
> recorded here.

## Class

Normative, and a loosening. The version-2 scope says "This scope adds no
loosening" and "a loosening would be a later policy version and an explicit
owner question" (`publicSourceScope.activeContent`). This is that version and
that question. It adds no network route, no storage place, no class and no
detector change.

## Subject and change

Subject: the secret-classification policy of `project:syzygy` as the
version-2 act left it (the version-2 manifest row `none`).
`scripts/build_public_source_screening_scope_v3.py` takes the policy on disk
when it hashes to that row, and otherwise refuses, except after a version-3
act, when it recovers that row's bytes by reversing its own patch.

Exactly three values change; the builder fails if anything else does:

| Value | Change |
|---|---|
| `policyVersion` | next minor, the version-2 variant name kept and the version-3 variant appended: `1.4.0-public-source-candidate.1.none.code-all` or `…code-non-web` |
| `publicSourceScope.activeContent` | rule keeps every base step except the three `codeContentExemption.rule` lifts for an exempt body, and says `renderRule` binds every body; new object `codeContentExemption`; new `consequence` |
| `publicSourceScope.inheritedRules` | "activeContentClassification" becomes "activeContentClassification (except that, for a body activeContent.codeContentExemption exempts, its active-content forms are not scanned for and malformedContextAction does not apply; its renderRule binds every body)"; every other word is unchanged |

### Current text (version 2)

```text
activeContent.rule: the base activeContentClassification, inertContextRule and
the active-content condition of classificationSuccess apply unchanged to every
admitted body, Markdown or not: a body with an active-content form outside a
valid inert code context is excluded whole as active content. This scope adds
no loosening

activeContent.consequence: [Inferred] a source file that embeds markup-like
bytes outside a valid inert code context, for example an HTML string in a
script, is withheld. The first run measures how many; a loosening would be a
later policy version and an explicit owner question
```

### Proposed text (both variants)

```text
activeContent.rule: the base activeContentClassification, inertContextRule and
the active-content condition of classificationSuccess apply unchanged to every
admitted body, Markdown or not, except the steps codeContentExemption.rule
lifts for a body it exempts: a body it does not exempt with an active-content
form outside a valid inert code context is excluded whole as active content,
and renderRule binds every body

codeContentExemption.rule: such a body is admitted without the active-content
scan: neither step 4 of classificationOrder, nor the active-content condition
of classificationSuccess, nor the malformed-code-context exclusion applies to
it, because the Markdown code-context profile does not describe source code
(it reads a comparison such as a<b && c>d as an HTML tag, and an unpaired
backtick in source as a code context that never closes). Every detector still
runs over the whole body; the denied-path, strict-UTF-8, NUL and
resource-limit rules are unchanged; a project-documentation body, or a
code-content body this exemption does not name, is scanned as before. The
exemption reaches those three steps and nothing else:
activeContentClassification.renderRule, and the encoding of selected text for
its destination, still bind such a body at every place it reaches

codeContentExemption.renderCondition: a page is a document an HTML or SVG
parser reads, and a page sink is a place where such a body's bytes, or a span
of them, are written into a page. The exemption holds for a page sink only
while it writes the body or span as text: every one of the characters & < > "
' is written as a character reference, the bytes are never parsed as Markdown
or HTML and never mint a link, element, attribute, script or handler, and the
page carries an enforced Content-Security-Policy, delivered before any of the
body's bytes, whose default-src source list is exactly 'none' and which
carries no script-src, script-src-elem, script-src-attr or object-src
directive. A consumer that cannot confirm this for a page sink scans the body
as before for that sink, and excludes it whole there on a finding. Every other
place such a body or a span of it reaches is not a page sink; egress governs
it

codeContentExemption.egress: the exemption changes no egress or consent rule.
At every place that is not a page sink (a review packet, a provider request, a
discovery excerpt, a stored record), an exempt body or a span of it counts as
screening-admitted code-content, reaches an agent session or a provider only
under the rules that already govern code-content, and is encoded for that
destination's format as renderRule requires

activeContent.consequence: [Inferred] a source file whose only active-content
finding was markup-like bytes outside a Markdown code context (a comparison, a
generic type, a template literal, a string holding HTML) is admitted when its
extension is exempt; the first public-target run (2026-10-08) withheld seven C
files of its target for active content. A body a secret detector matches stays
excluded whole
```

The variants differ only in `codeContentExemption.appliesTo`,
`codeContentExemption.exemptExtensions` and the `policyVersion` suffix:

- **`all`**: `exemptExtensions` is every entry of the code-content rule's
  `sourceExtensions` (25 extensions).
- **`non-web`**: the same list less `.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`,
  `.tsx` and `.php` (18 extensions). `appliesTo` says those seven are
  scanned as before, and gives the criterion: they are the browser-side and
  server-templating languages. It says this is a choice, not a claim that
  other languages carry no HTML. Round 1 (finding 4) noted that Python, Go,
  Ruby and others also embed HTML, so the earlier reason, "commonly carry
  HTML", did not separate the seven.

The full proposed bytes are the two diffs under `proposed/`.

## Why [Observed] / [Inferred]

- [Observed] The scanner is the Markdown active-content scan,
  `scanActiveContent` (`packages/three-surface-poc-core/src/git-object-reader.ts:191`),
  whose tag pattern is `HTML_TAG` at line 164:
  `<\/?([A-Za-z][A-Za-z0-9-]*)(?:\s[^<>]*)?\/?>`. In `a<b && c>d` it matches
  `<b && c>`, a "tag" named `b`.
- [Observed] Both consumers of this scope apply it to every admitted body:
  `packages/polaris-dossier/src/screen.ts:85` and
  `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:138`.
- [Observed, as reported by the lead from run `run-e8b77d72780cc48f4dd032267d963d93`]
  the run withheld seven C files of its target for active content. This
  package did not read the run directory.
- [Observed] The renderer encodes every rendered byte of a target body. The
  dossier command `packages/polaris-dossier/src/render.ts` does no HTML itself:
  it hands the located bytes to an injected renderer (quotation segments at
  `render.ts:350`, whole-blob sources at `render.ts:276`). That renderer,
  `apps/three-surface-poc/src/polaris-generation/dossier-render.ts`, writes a
  quotation as `<q class="verified-quote">` around `escape(part.text)` (line
  261) and a source page as `<blockquote class="exact-source">` around
  `escape(span.text)` (line 409); the provider-mode preview,
  `draft-preview.ts:122`, writes `escape(source.spans[0]!.text)` inside a
  `<div class="exact-source">`. `escape` is `draft-preview.ts:24`, which
  replaces each of `& < > " '` with a character reference. Every page carries
  `DRAFT_PREVIEW_CSP_META` (`draft-preview.ts:18`, used at
  `dossier-render.ts:129`): `default-src 'none'; style-src 'unsafe-inline';
  base-uri 'none'; form-action 'none'`. It carries none of the four
  directives `renderCondition` forbids. Those four are named because a later
  directive overrides `default-src` for its own fetch type, so
  `default-src 'none'` alone would be met by a policy that also carried
  `script-src 'unsafe-inline'` (round-1 review of PR #404, finding 3). Since
  the package's own round 1 (finding 3), the condition also requires an
  *enforced* policy, which a `Report-Only` header is not. The policy must be
  delivered before any of the body's bytes, because a `<meta>` policy governs
  only what is parsed after it. Its default-src list must be *exactly*
  `'none'`, because browsers ignore `'none'` beside other source
  expressions. Both page builders (`page()` and `renderDraftPreview`) emit
  the meta first in `<head>` [Observed by that review]. The machine view
  (`dossier-render.ts:440-452`) carries quotation offsets and anchors, not
  their text.
- [Observed by the package's round-1 review, re-derived at this commit]
  **Page sinks and other sinks.** Three non-test call sites screen a blob body:
  `apps/three-surface-poc/src/polaris-generation/repo-corpus.ts:227`,
  `packages/polaris-dossier/src/check.ts:577` and
  `packages/polaris-dossier/src/review.ts:188`. Downstream of them, the
  dossier pages and the draft preview are page sinks. The others are not:
  - the fidelity review packet, which `review.ts` writes as JSON for a
    session the operator starts;
  - the provider author request
    (`packages/polaris-generation-core/src/pipeline.ts:265`);
  - the discovery excerpt (`packages/polaris-generation-core/src/discovery.ts:290`).

  Round 1 found that `renderCondition`, as then worded, failed at every one of
  these non-page sinks, which would have withdrawn the exemption from exactly
  the review packets that judge a quoted C file's claims. The condition now
  defines a page sink as a document an HTML or SVG parser reads, and routes
  every other place to `egress`. There the body counts as screening-admitted
  code-content and is encoded for that destination's format under the base
  `renderRule`.
- **The lead's wording is not quite true, and the delta does not use it.** The
  proposal said a code-content body "is only ever rendered context-encoded
  inside code blocks". It is rendered context-encoded, but inside an inline
  quotation (`<q>`) and a block quotation (`<blockquote>`), not a code block.
  The narrowest true statement is the one `renderCondition` makes: on a page,
  entity-encoded text under an enforced CSP whose `default-src` list is
  exactly `'none'` and which carries no script-bearing directive. The
  package's round-1 reviewer swept every non-test `.ts` file under
  `packages/` and `apps/` that emits a closing HTML tag (24 files), and every
  interpolation in the three renderer files: 359 in all, with each of the 219
  not led by `escape(` read individually. No other page
  sink for a public-target body was found [Observed by that review]. The
  condition is still stated per page sink and fails closed, for a page sink
  added later.
- [Inferred] The scan protects HTML sinks. A body that reaches no HTML sink
  unencoded gains nothing from it, while the scan's Markdown grammar misreads
  ordinary source. Secret detectors are the screen that guards egress, and they
  stay.

## Affected identifiers, and the reading the exemption relies on

- **REQ-polaris-generation-012**, "Safe accessible presentation", opens:
  "Generated pages SHALL render untrusted source and provider content
  inertly". Its scenario "Malicious source or output" reads: "**WHEN** an input
  contains executable markup, unsafe links or instructions to broaden tool
  access **THEN** rendering executes none of that content and the workflow
  obtains no new authority from it". It is defined at
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md:641`
  and restated with the same opening sentence and scenario in the
  understanding overlay,
  `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md:366`.
  **The reading this delta relies on:** for an exempt body, REQ-012's "render
  … inertly" and "rendering executes none of that content" are met by
  `renderCondition` (every character that could open markup is written as a
  character reference, and the page's CSP admits no script or plugin), not by
  withholding the body. Under version 2, the active-content scan was a second
  way of meeting them for these bodies; under version 3 it is not used for
  them. A reviewer who reads REQ-012 as requiring a body that carries markup-like
  bytes to be withheld, however it is rendered, contradicts this reading, and
  then the exemption needs a specification amendment as well as this act.
  REQ-012's third line, "excluded or unclassifiable content is not revealed in
  assets or diagnostics", is not reached: an exempt body is admitted, not
  excluded.
- **REQ-polaris-generation-033**, the operator-agent mode
  (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:31`),
  requires that "every object SHALL be classified and screened under the
  observing project's effective policies (REQ-polaris-generation-025) before
  its content is used in a check or rendered" (`screen.ts:8-9` quotes it).
  The exemption changes what the effective policy's screen contains, not
  whether screening happens. Every body is still classified, and every detector
  still runs over it, so this delta reads 033 as met unchanged. REQ-025 is
  reached only through that sentence. The delta changes none of its words.
- **REQ-polaris-generation-035**
  (`…/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:320`)
  requires that the fidelity packet's "cited spans SHALL be those cited by the
  draft and by the frozen inventory, screening-admitted only". This delta
  reads "screening-admitted" as one answer per body, never per sink. An exempt
  body is screening-admitted everywhere, and `egress` says so in the bytes.
  `renderCondition` withdraws the exemption only at a page sink that cannot
  meet it, and only for that page.
- No `SEC-`, `VIS-` or `RFC` clause is amended. REQ-012's contract warrants
  are `RFC7-13, RFC7-14, RFC7-33, RFC7-34` (base `spec.md:682`). Each was
  read in `contracts/candidates/rfcs/RFC-0007/`:
  - RFC7-13, progressive disclosure (`narrative-contract.md:306`);
  - RFC7-14, the verbatim leaf (`:324`);
  - RFC7-33, machine-readable distinctions (`rendering-and-surface.md:205`);
  - RFC7-34, non-visual recoverability (`:241`).

  [Observed] None states a rendering-safety rule stricter than REQ-012.
  RFC7-33's "a copy-paste into an agent prompt" concerns distinctions that
  survive a copy, not executable content. This closes the earlier [Unknown].

## What it does not change

Every detector, including inside code contexts; the base `renderRule`
("admitted Markdown is never rendered as HTML; selected text is encoded for
its destination and code-context bytes never mint a link, element,
attribute, script or handler"), which still binds an exempt body: the
exemption lifts only the active-content scan, its success condition and the
malformed-context exclusion. Also unchanged: denied paths; strict UTF-8 and
NUL; resource limits; the classes and their rules; `project-documentation`
bodies (still scanned); the access boundary; raw-body handling; every
consent; every act already performed. A version of this delta before
round 1 of the package's review lifted the whole base
`activeContentClassification` for an exempt body, `renderRule` included
(finding 2). The builder now fails if any of the three strings that carry
the exception stops keeping `renderRule`.

## Supersession and the state after the act

The act supersedes the version-2 act for the `approve-policy` role from its own
instant, as version 2 superseded version 1. After it, the policy on disk is the
chosen row's bytes; this builder's `--check` still passes (selftest). The
version-2 recorder's `--check` fails by design, and so does its `--selftest`
(the version-2 builder refuses a policy that is neither its base nor its row).
Both battery lines go at install, in `PROJECT-STATUS.md` and the workflow,
and the version-3 recorder's lines replace them (`IMPACT-LEDGER.md`). The recorder is written after a
confirming review and must refuse a second variant act over this manifest.

## One variant act, or none

The manifest has two rows. The owner picks at most one; declining leaves
version 2 in force and the C files withheld.
