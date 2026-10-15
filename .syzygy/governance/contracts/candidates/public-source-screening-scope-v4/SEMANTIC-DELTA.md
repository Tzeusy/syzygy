# Semantic delta — public-source screening scope, version 4

> **Candidate — binds nothing.** Drafted 2026-10-15 for `syzygy-olmr`. Effect
> comes only from an owner `approve-policy` act over the exact proposed bytes
> of one manifest row. No target repository body was read to draft it; the
> Redis figures below come from the bead's own text. No act is recorded here.

## Class

Normative, and a loosening of secret screening for the public-source scope
only. The base (Butlers) scope, every detector, the active-content rule, the
content classes, the consent and egress rules and `rawBodyHandling` are
unchanged. Variant `span-guides` also widens the `project-documentation`
root-document rule by a closed list of names.

## Why

[Observed, from the bead] The Redis 8.10.2 trial
(run `run-6648312f61b5e536315215e0c22422cf`) withheld 140 of 233 cited spans
from the fidelity packet, so most claim rows stayed unresolved and readiness
blocked. The bead's three causes, and what this version does with each:

| Cause (bead) | Spans | This version |
|---|---|---|
| Whole-blob secret screening: one `credential-assignment` match on README line 1 (a badge URL carrying `token=`) withholds the whole README | 41 | **Changed** by both variants: the matched line and one guard line on each side are withheld, the rest of the body is kept |
| `SECURITY.md`, `MANIFESTO`, `TLS.md`, `redis.conf`, modules/MODULES.md (a Redis path) have no class (`unknown-extraction-class`) | 89 | **Not changed** for these five names; see "Declined" below. Variant `span-guides` adds generic root guide names, none of which is one of the five |
| Active content in `00-RELEASENOTES` and `LICENSE.txt` | 10 | **Not changed**: the active-content scan stays whole-body |

[Inferred] Under either variant the README's cited spans that include neither
line 1 nor line 2 become admissible; the bead gives no per-span line numbers,
so how many of the 41 that is stays Unknown. None of the 89 or the 10 is
recovered.

## Authority this rests on

- **RFC5-17** already defines the class this version emits: "`redacted-span`
  (artifact retained, matching spans replaced by markers with a count)", and
  says "a claim over the **surviving content** may still stand, **at the tier
  it otherwise earned**, with the redaction count disclosed on the claim; only
  a claim that **depends on a redacted span** renders Unknown
  (`excluded-content`)". It adds: "Mapping the whole artifact to a blanket
  Unknown would over-degrade usable partial evidence, which VIS-1 no more
  permits than over-claiming does."
- **REQ-polaris-generation-024** (`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`)
  already requires: "redacted-span SHALL retain permitted surviving evidence
  at its otherwise-earned tier with disclosed count, making only claims
  dependent on removed spans Unknown. Redaction branches SHALL remain limited
  to those the adopted policy permits." Its scenario "Partial redaction
  retains usable support" is the behaviour this version turns on.
- The policy today lists `redacted-span` under `redactionClasses.neverEmitted`.
  That is the policy's own choice, so a policy act is the whole authority
  needed: no contract amendment and no specification delta.
- **RFC5-14** decides what variant `span-guides` may add: `project-documentation`
  is "a project's own prose that describes, explains or accompanies the
  project for its readers and does not govern its development: README, user
  and developer guides, tutorials, how-to and overview documents, changelogs
  and release notes, contribution guides, and licence and notice files,
  ordinarily", and "A document the project's declared classification policy
  places as doctrine, spec, decision or policy text is `governance-text`".

## Subject and change

Subject: the secret-classification policy of `project:syzygy` as the
version-3 act left it (the version-3 manifest row `all`, which is the policy
on disk at this package's base). `scripts/build_public_source_screening_scope_v4.py`
takes the policy on disk when it hashes to that row and otherwise refuses,
except after a version-4 act, when it recovers that row's bytes by reversing
its own patch. The builder fails if anything outside the values below changes.

| Value | Variant | Change |
|---|---|---|
| `policyVersion` | both | next minor with the variant appended: `1.5.0-public-source-candidate.1.none.code-all.redact-span` or `…redact-span-guides` |
| `publicSourceScope.detectors` | both | appends ", except where secretRedaction retains a body as redacted-span; every detector still runs over the complete body first" |
| `publicSourceScope.secretRedaction` | both | new object, placed after `activeContent` |
| `publicSourceScope.inheritedRules` | both | "detectors, matchAction, unclassifiableExclusion, redactionClasses," becomes "detectors, matchAction and redactionClasses (except that secretRedaction retains a body of an admitted snapshot as redacted-span where its rule says so, and for such a body reads the detector condition of classificationSuccess as no detector matching its retained text), unclassifiableExclusion,"; every other word is unchanged |
| `project-documentation` rule: `root-document` text, new `rootGuideStems` and `rootGuideSuffixes`, `notMapped` text | `span-guides` only | below |

### Current text (version 3)

```text
detectors: every detector in this policy applies unchanged to every body under
this scope, including inert code contexts; public visibility exempts nothing,
and a match excludes the whole artifact with hash-not-body provenance
(matchAction, RFC5-17)
```

### Proposed `secretRedaction` (both variants)

```text
appliesTo: a body of an admitted snapshot whose path this scope admits
(code-content or project-documentation), after the denied-path, strict-UTF-8,
NUL and resource-limit rules pass. Text an agent session writes (a draft, an
inventory, a verdict, a finding) is not such a body and is screened as before

redactionClass: redacted-span
wholeArtifactDetectors: [private-key-material]
guardLines: 1

rule: every detector runs over the complete transient body exactly as before,
including inert code contexts. When at least one detector matches and none of
the matches is from a detector in wholeArtifactDetectors, the body is retained
as redacted-span (RFC5-17) instead of excluded whole. Lines are split at LF,
CRLF or CR, as the generator counts lines; a match touches every line that
holds any of its characters. A line a match touches, and guardLines lines
before and after it, is a withheld line. Every detector then runs again over
the retained text, which is the body with each withheld line replaced by an
empty line of the same terminator; a match there excludes the whole artifact
as excluded-artifact. A body with a match from a detector in
wholeArtifactDetectors, or with a match the consumer cannot place on lines, is
excluded whole as before

withheldLines: a withheld line is never stored, logged, rendered, sent,
quoted, used to verify a quotation, or given to an agent session, and no
digest of a withheld line, or of any part of one, is recorded. Wherever the
retained body is shown or carried, the withheld lines are replaced by a marker
that names the redaction and the count of withheld lines in the body

citedSpanRule: a cited span (a start line and an end line of the body) that
includes a withheld line is withheld whole, never shown in part, and every
claim that depends on it renders Unknown with reason excluded-content
(RFC5-17). A cited span that includes no withheld line is screening-admitted
content of the body's class and is carried with the body's redaction count
disclosed beside it; its own text is screened by every detector before it is
carried, and a match withholds it

provenance: the retained body's exclusion record is hash-not-body: the
content digest of the complete body, its repository-relative path, policyId,
policyVersion, the redaction class redacted-span, the id of each detector that
matched, and the numbers of the withheld lines

unchanged: the active-content scan, its malformed-code-context exclusion and
activeContent.codeContentExemption run over the complete body exactly as
before, and an active-content finding excludes the body whole; the content
classes, the consent and egress rules and rawBodyHandling are unchanged; a
withheld line changes no class
```

The `consequence` field carries the [Inferred] effect and the residual named
under "What it gives up".

### Why each fail-closed choice

- **`private-key-material` stays whole-artifact.** That detector matches the
  literal header (`-----BEGIN PRIVATE KEY-----` and two siblings), and the key
  material is on the lines after it. Withholding the header line and one guard
  would release the key. Every other detector's match holds the secret it
  signals (`credential-assignment` requires eight value characters after the
  `=` or `:`; `credential-bearing-url` holds the user and password;
  `known-token-formats` is the token).
- **A match can span lines.** `credential-assignment` allows `\s*` around its
  `:` or `=`, so `password`, a blank line and `= value` is one match; every
  line it touches is withheld (builder body fixture "assignment across lines").
- **One guard line on each side** catches the common continuation forms (a
  value wrapped onto the next line, a key on the line before its value) that
  the detectors would not match on their own. It is a mitigation, not a proof:
  see the residual below.
- **The retained text is screened again.** Emptying lines can join the text
  around them into a new match: `credential-assignment`'s `\s*` crosses blank
  lines, so a `password` two lines above a withheld run and a `= value` two
  lines below it match once the run is empty. The second pass catches that
  and excludes the body whole (builder body fixture "emptied lines join a new
  match", with a mutant showing the oracle would otherwise redact it).
- **A cited span overlapping a withheld line is withheld whole**, so a reader
  never sees half a quotation, and the claim that cites it is Unknown, which is
  exactly RFC5-17's dependent-claim rule.
- **No digest of a withheld line.** A digest of a short secret is a guessing
  oracle; the record carries the whole body's digest and line numbers only.
- **Agent-written text is unchanged.** The render, close and check paths that
  screen an agent's draft or verdict prose keep whole-text screening.

### Variant `span-guides`: the root guide names

```text
root-document rule (appended): , or, when the suffix removed is one of
rootGuideSuffixes, one of rootGuideStems

rootGuideStems: install, installing, installation, building, hacking,
development, developing, usage, tutorial, overview, getting-started,
getting_started, gettingstarted, upgrading, migrating, migration,
troubleshooting, support, contributors, credits, thanks, acknowledgments,
acknowledgements

rootGuideSuffixes: .md, .rst, .txt

notMapped: "root files named design, governance, security or code of
conduct;" becomes "root files named design, governance, security, code of
conduct, manifesto or architecture; a rootGuideStems name with no suffix;"
```

Each name is a conventional root guide, tutorial, how-to, overview,
contribution or credit file, the kinds RFC5-14 lists [Inferred, from general
convention; no target was read to choose them]. Unlike `rootStems`, a guide
name needs a suffix: a bare `INSTALL` or `BUILDING` at a repository root may be
a script, so it stays unclassified. `build` is absent because a root `BUILD` is
a Bazel build file. No name carries a `docExcludedTokens` word, none repeats a
`rootStems` name, and no suffix is a source extension (all builder-checked).

## Declined, and why

| Option | Decision | Reason |
|---|---|---|
| Root `SECURITY` as project-documentation | declined | A security policy is "policy text", which RFC5-14 puts in `governance-text`; the version-2 packet withheld it by name (its Q3, accepted), and the version-2 builder's own mutant "a security root name added is caught" guards it |
| Root `MANIFESTO` | declined | The owner chose version-2 variant `none` over variant `manifesto` on 2026-10-07; the packet's reason was that a manifesto "is also plausibly doctrine, which RFC5-14 puts in `governance-text`". The trial adds the cost, not new evidence about the file's class. The lawful route is a `governance-text` rule and a consent listing that class, a separate package |
| Root `TLS` | declined | One project's topic name; a generic list cannot grow one target at a time, and a rule admitting any root `.md` would also admit agent-instruction files (for example AGENTS.md), which govern development |
| `redis.conf` | declined | Configuration, not prose; no RFC5-14 class but `code-content` fits it, and adding `.conf` to `sourceExtensions` would class every root config file as code without a review of what config files carry |
| modules/MODULES.md (a Redis path) | declined | A document below the root outside `docs/`; the version-2 packet's Q4 withholds nested documents because they are often a vendored library's |
| Active content per line (the 10 spans) | not offered | The active-content scan is Markdown-context aware, and a code fence spans lines, so a per-line rule has no sound definition here |
| Option C: screening-withheld rows non-blocking | declined | REQ-polaris-generation-035 counts every unresolved row; marking a row whose support was never read as non-blocking would let readiness be declared over claims with no evidence, which VIS-2 forbids ("Nothing turns green ... without current evidence"). It also needs a specification delta, not a policy act |

## What it gives up

- [Inferred] A secret that a detector matches on one line and that continues
  past the guard line onto further lines is admitted in its unmatched part;
  whole-blob screening excluded the whole body in that case. A secret the
  detectors do not match at all is admitted under either rule (the existing
  residual `screen.ts` records: "the detectors match literal forms only, so an
  encoded or split secret passes them").
- A body with a match is no longer withheld whole, so a line that is merely
  near a secret, beyond the guard, reaches a page or an agent session.

## What it does not do

It names no repository, grants no consent, read, egress or provider call, and
changes no detector, class, active-content rule, consent rule or base-scope
rule. It edits no performed record and no specification. It proves nothing
about any run. Its install is separate work: until then the read gates refuse
the new digest and the screens apply no redaction (see `IMPACT-LEDGER.md`).
