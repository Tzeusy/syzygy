# R-OLMR-SCREENING-SCOPE-V4-1 — public-source screening scope v4, round 1
Reviewed commit: 676adea9929bf4d7385e5faa4aedc7d1ca334162
Manifest SHA-256: 4667644a36edebc4f7e9dd62e325fcb489f977e3154eb32a62ff520bf9533d61
Verdict: REVISE

Reviewer: fresh context (CC-REV-1), given only the brief
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/REVIEW-BRIEF.md`,
the artifact and the references it lists. No target repository (Redis, Butlers
or other) was read, cloned or fetched; every target figure below is from
`bd show syzygy-olmr`. No repository file was modified.

Manifest digest derived two ways [Observed]:
`python3 scripts/build_public_source_screening_scope_v4.py --manifest-digest`
-> `4667644a…` and `sha256sum` of the manifest file -> the same 64 hex
characters (full value in the head above).

## Findings

**Finding 1 — `known-token-formats` is not a detector whose match "holds the secret it signals": an AWS access-key ID line releases the paired secret key two lines away** (blocking)

The delta justifies keeping only `private-key-material` whole-artifact with
(SEMANTIC-DELTA.md:143-149): "Every other detector's match holds the secret it
signals (`credential-assignment` requires eight value characters …;
`credential-bearing-url` holds the user and password; `known-token-formats` is
the token)." The policy's `known-token-formats` pattern is
`(?:AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{10,})`.
The `AKIA…` alternative matches an AWS access-key **ID**; the secret is the
separate 40-character secret access key, which no detector matches when it is
written `secret_key = "…"` or `aws_secret_access_key = …` (`credential-assignment`
needs `secret` immediately followed by `\s*[:=]`, and `api[_-]?key` needs
`api`) [Inferred, from general knowledge of AWS credentials and the pattern
text]. This is the same shape the delta gives as the reason for the private-key
exception: the match is an identifier/header and the secret sits on another
line.

Constructed body (scratch probe calling the builder's own oracle
`withheld_lines` over the re-derived `span` proposed bytes):

```text
provider "aws" {
  access_key = "AKIA<16 chars>"
  region     = "us-east-1"
  secret_key = "<40-char secret access key>"
}
```

Output [Observed]: `withheld -> {1, 2, 3} of 5 lines`. Line 4, the secret
access key, is retained, admitted as screening-admitted content and can be
cited, carried in the fidelity packet and given to an agent session. Under
version 3 the whole body was excluded because `AKIA` matched. The adjacent
form (`aws_access_key_id` / `aws_secret_access_key` on consecutive lines)
is caught only by the guard line (`{1, 2, 3} of 3 lines`), i.e. the
mitigation holds only by layout. RFC5-17: "A secret reproduced in any surface,
store, or endpoint is a trust-floor violation". Repair options: put
`known-token-formats` (or a split-out AKIA detector) in
`wholeArtifactDetectors`, or make the redaction apply only to detectors whose
match provably contains the secret, and add a body fixture of this shape; correct
the sentence at SEMANTIC-DELTA.md:146-149 and the builder comment at line 72.

**Finding 2 — the `g` flag's non-overlapping scan hides a second match that crosses lines, and the re-screen cannot see it** (revise)

The rule (proposed `secretRedaction.rule`) withholds the lines "a match"
touches, where matches come from the detectors run with their `g`/`gi` flags,
i.e. a non-overlapping left-to-right scan (the builder oracle uses
`re.finditer`, `withheld_lines` lines 290-301; a JS `matchAll` behaves the
same). `credential-assignment`'s value class `[^\s"'<>$]{8,}` can itself end
in a keyword, so a first match consumes a keyword that would have begun a
longer, line-crossing match.

Constructed bodies [Observed, same probe]:

- `"intro\nsecret: password\n\n\n: Hunter2Hunter2Real\nend\n"` -> withheld
  `{1, 2, 3}`; the pattern, searched from every start offset, matches
  `password\n\n\n: Hunter2Hunter2Real` (lines 2-5), so line 5 holds the value
  of a match the detector as written makes, and line 5 is retained.
- `"x\ntoken=placeholdersecret\n\n\n= Hunter2Hunter2Real\ny\n"` -> withheld
  `{1, 2, 3}` of 6 lines; line 5 retained.

The re-screen does not catch either: the withheld line that held the keyword is
emptied, so the retained text `"\n\n\n\n: Hunter2Hunter2Real\nend\n"` carries
no keyword (probe: no detector hit at any offset of the retained text). This is
not the residual the delta states (a matched secret continuing past the guard):
here the value is inside a detector match the scan never reported. Repair:
define the match set as every match from every start offset (or iterate
withholding to a fixpoint over overlapping matches), and add a body fixture with
a mutant. Contrived as written, but the brief asks for exactly this
construction and the policy text currently permits it.

**Finding 3 — the stated residual says unmatched secrets are "admitted under either rule"; that is false for a body that also carries a match** (revise)

SEMANTIC-DELTA.md:215-217: "A secret the detectors do not match at all is
admitted under either rule". OWNER-DECISION-PACKET.md:58-59: "Secrets the
detectors never match are admitted either way, as today." Under version 3 an
unmatched secret in a body that also has **any** detector match was excluded
with the whole body; under version 4 it is admitted unless it falls inside the
guard. Probe [Observed]: a README whose line 1 is a `token=` badge and whose
lines 3-5 are an `-----BEGIN EC PRIVATE KEY-----` block (a header the
`private-key-material` literals do not list) -> withheld `{1, 2}`; the EC key
block is retained. Finding 1's AWS pair is the same class. The second bullet
(delta:218-219, packet:60-61, "a line that is merely near a secret, beyond the
guard") gestures at it, but the first bullet tells the owner the opposite. This
co-location loss is the change's main cost and must be stated plainly in both
the delta and the packet: a body with a match is evidence that the file carries
credentials, and version 4 stops treating it so.

**Finding 4 — the redacted-span requirement is REQ-polaris-generation-025, not -024** (revise)

SEMANTIC-DELTA.md:44-49 (and REVIEW-BRIEF.md:21-22) cite
"REQ-polaris-generation-024" for "redacted-span SHALL retain permitted
surviving evidence … Redaction branches SHALL remain limited to those the
adopted policy permits" and its scenario "Partial redaction retains usable
support". In
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
the requirement text precedes its `ID:` line: `### Requirement: Owner walkthrough
and review-freeze discipline` (line 1318) is `ID: REQ-polaris-generation-024`
(line 1322); `### Requirement: Provenance-bound source policy` (line 1398),
whose text at line 1400 holds the quoted sentences, is
`ID: REQ-polaris-generation-025` (line 1402), and the scenario "Partial
redaction retains usable support" is at line 1424 under it [Observed]. Second
method: `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json:198-208`
gives REQ-024's `normativeText` as the walkthrough text and REQ-025's as the
provenance-bound text containing "redacted-span" [Observed]. The substance of
the authority claim is unaffected (criterion 3), but rule 8 requires the claim
to anchor to the defining clause; the owner would be pointed at the wrong
requirement.

**Finding 5 — the impact ledger and the packet omit that the act breaks the Butlers (base) read gate** (revise)

IMPACT-LEDGER.md:73-76: "What it does not touch: The base (Butlers) scope and
its consumers". OWNER-DECISION-PACKET.md:85-87: "signing breaks the
public-target read gate until the install re-points it". But
`apps/three-surface-poc/src/governance-inputs.ts:76-104`
(`pwbSyzygyButlersExpectations`, `configuredRepository:
'repository:butlers-configured-poc'`) pins `policyVersion:
'1.4.0-public-source-candidate.1.none.code-all'`, the act identity
`PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-APPROVAL-2026-10-08`,
its recording tag and its scope anchors [Observed]. Any act over one of this
package's rows replaces the policy digest and version, so the Butlers body-read
gate refuses until re-pinned, exactly as the version-3 ledger stated ("The
Butlers read gate pins the policy by digest and then version …, so it refuses
until re-pinned", v3 IMPACT-LEDGER.md:93-99). The v4 ledger lists
`governance-inputs.ts` only as "The read-gate pin" (line 23) without saying it
is the Butlers gate, then denies touching Butlers consumers. Also absent from
the ledger, from the 30-file policy-path sweep (below): `scripts/install_redis_sitting.py`
(the v3 ledger says the installer derives the policy step from the recorded
act), `scripts/simulate_redis_sitting.py`, `scripts/check_spec_reconciliation.py`
(whether each pins the digest: [Unknown], as v3 also left it), the app's
`checkoutPolicyActPort` (`public-source-screening.ts:85`, reading
`POLICY_ACT_FORMS[0]` only), and the provider-mode egress population
(v3 ledger's "What Syzygy transmits": span text reaches the provider via
`pipeline.ts`; version 4 widens that population to spans of retained bodies).
Repair: name the Butlers gate break in the ledger and in the packet's "Order,
as fact", and either name or explicitly disposition the other members.

**Finding 6 — the whole-body digest and the Git object id become a guessing oracle for withheld lines** (note)

`secretRedaction.withheldLines` forbids "a digest of a withheld line, or of any
part of one", with the rationale (delta:166-167) "A digest of a short secret
is a guessing oracle; the record carries the whole body's digest and line
numbers only." Once every other line of the body can be shown, the complete
body's digest (provenance) and the blob `objectId` carried on every admitted
span (`review.ts:209`) verify a guess of the withheld lines exactly as a
per-line digest would, when the withheld content is short or low-entropy (a
placeholder password, a blank guard line) [Inferred]. Mitigated in this scope
by the target being public, but the policy says "public visibility exempts
nothing", so the rationale should state the residual rather than imply the
oracle is closed.

**Finding 7 — option C's REQ-polaris-generation-035 basis is a paraphrase, not a sentence of that requirement** (note)

SEMANTIC-DELTA.md:208: "REQ-polaris-generation-035 counts every unresolved
row". No sentence of REQ-035 says that. The nearest are "The review context
SHALL write a structured verdict that … records … draft-to-source support for
every claim block" and "Syzygy SHALL validate the verdict before it counts: …
that every inventory entry and every claim block has an entry; … and that a
verdict with an unresolved blocking finding does not declare the subject
ready", plus the REQ-006 rule it keeps, "the rule that unresolved material
omissions prevent readiness" (spec.md, REQ-035 text at lines 320-328) [Observed].
The bead says unresolved rows block via the "readiness basis", which is
implementation. The decline is still sound on VIS-2 (see criterion 6); quote
the clause it rests on.

**Finding 8 — two decline/selection reasons are wider than their sources** (note)

- SEMANTIC-DELTA.md:206 and packet:73-74 say version 2's Q4 "withholds nested
  documents because they are often a vendored library's". Q4 is about nested
  **READMEs** ("A README anywhere else (for example src/README.md) is
  withheld, because a README below the root outside docs is often a vendored
  library's", v2 packet:111-116). modules/MODULES.md is withheld because no
  path rule maps a non-README document below the root outside docs/doc; the
  reason should say so.
- SEMANTIC-DELTA.md:190-192 says each guide name is "a conventional root
  guide, tutorial, how-to, overview, contribution or credit file, the kinds
  RFC5-14 lists". RFC5-14's list has no credit files (it has "contribution
  guides"); `contributors`, `credits`, `thanks`, `acknowledg(e)ments` rest on
  the general definition "accompanies the project for its readers", which is
  plausible but is not the list. `support` (a SUPPORT file may state a
  version-support policy) and `development` (a DEVELOPMENT file may prescribe
  process) are the two names closest to "governs its development"; worth one
  sentence each.

**Finding 9 — marker wording and oracle regex dialect** (note)

- The policy's marker "names the redaction and the count of withheld lines in
  the body"; IMPACT-LEDGER.md:63-64 says "a marker with the withheld-line
  count in place of each withheld run". Per-run versus per-body count: say
  which the install must render.
- The builder oracle runs the detectors with Python `re`; the screens use JS
  `RegExp`. `\s` differs (Python `str` `\s` includes U+001C-U+001F and U+0085;
  JS `\s` does not include them and includes U+FEFF) [Inferred, from the two
  engines' documented classes], so the ledger's "the builder's reference oracle
  states" the install behaviour needs the body fixtures run in both engines,
  or a caveat. No leak found from this (probe cases F, G: U+2028 and U+0085
  inside a matched line were withheld whole).

## Per-criterion results

**1. Is the diff exactly the stated change?** Pass.
- `--check` -> `public-source-screening-scope-v4: patches and manifest current`;
  `--selftest` -> `selftest: 33 of 33 predicates held` [Observed].
- Base: the policy on disk hashes to the v3 manifest row `[variant: all]`
  (`sha256sum` of the policy equals that row; same 64 hex) [Observed].
- Independent re-derivation: copied the policy to scratch, applied each patch
  with GNU `patch`, `sha256sum` -> `16f0943e…` (`span`) and `43c8d9ac…`
  (`span-guides`), equal to the two manifest rows printed by `--digests`
  [Observed].
- A JSON tree diff of my own (scratch `jdiff.py`, walking every key and list
  index) over base vs each proposed file: `span` changes exactly
  `/policyVersion`, `/publicSourceScope/detectors`,
  `/publicSourceScope/inheritedRules`, adds `/publicSourceScope/secretRedaction`;
  `span-guides` additionally changes `rules[2]/notMapped`,
  `rules[2]/pathRules[0]/rule` and adds `rootGuideStems`, `rootGuideSuffixes`.
  No key-order changes reported. Each matches the delta's table row by row
  [Observed]. Commit diff `b5a7e27a..676adea9` touches 9 files, none the policy
  itself [Observed].

**2. Is the redaction fail-closed?** Fails — Findings 1, 2, 3.
- Probes (scratch `probe.py`, `probe2.py`, calling the builder's
  `withheld_lines` over the re-derived proposed bytes; 10 constructed bodies):
  A (overlap hidden by `g`): leak, line 5 retained. B (`token = secret_key…`):
  no leak (no `[:=]` after `secret`). C (CR-only ends): withheld `{2, 3, 4}`,
  no leak; `review.ts` `linesOf` (lines 242-250) and `quote-locate.ts`
  `lineBounds` (lines 66-80) both split at LF, CRLF and CR, so the policy's
  line numbering matches the generator's [Observed]. D (tail past guard):
  `CONTINUED-2-SECRET` retained — the stated residual. E (EC key with a badge):
  EC key retained — Finding 3. F/G (U+2028, U+0085): withheld whole. H (AWS
  pair, one line between): secret key retained — Finding 1. I (AWS adjacent):
  guard catches. J (value ending in a keyword): leak — Finding 2.
- Multi-line matches: every touched line is withheld (fixture "assignment
  across lines" holds). Re-screen: catches the joined match (fixture and mutant
  hold) but not Finding 2. Private-key exception: whole-artifact on the three
  literals; sound for those, but the same reasoning applies to AKIA (Finding 1).
- Marker: carries only a count. Provenance: digest, path, policy ids, class,
  detector ids, line numbers — no withheld bytes; oracle residual in Finding 6.
- Guard line: described as "a mitigation, not a proof" (delta:153-156)
  [Observed]. Residual stated in both delta (210-219) and packet (54-61), but
  inaccurately (Finding 3).

**3. Is the authority claim right?** Substantively yes; citation wrong
(Finding 4). RFC5-17 defines `redacted-span` ("artifact retained, matching
spans replaced by markers with a count") and maps it to per-claim Unknown;
RFC5-16 "content matching the policy is excluded" is satisfied by excluding the
matching lines; REQ-polaris-generation-025 (not -024) requires redacted-span to
retain surviving evidence and limits branches "to those the adopted policy
permits", and its scenario "a policy permitting only whole-artifact exclusion
is not silently changed to partial redaction" is met by an explicit act. I
found no clause in RFC5-14/16/17 or REQ-025/035 that requires whole-artifact
exclusion for this scope. REQ-035's "screening-admitted only": the policy
itself declares a span with no withheld line "screening-admitted content of the
body's class", and its own text is re-screened, so it qualifies [Inferred].
The policy's top-level `redactionClasses.neverEmitted` still lists
`redacted-span`; the scope overrides it through the amended `inheritedRules`
exception, which is how this policy already scopes rules [Observed].

**4. Is the scope bounded?** Pass on the policy bytes; the ledger's statement
about Butlers is wrong (Finding 5). Diff touches only `publicSourceScope` and
the shared `policyVersion` [Observed, jdiff]; `appliesTo` excludes agent-written
text; `unchanged` keeps the active-content scan whole-body; no class, consent,
egress, `rawBodyHandling`, `accessBoundary`, `sourceAdmission` change (also
builder predicates). The shared `policyVersion`/digest change does reach the
Butlers read gate pins.

**5. Variant `span-guides`.** Mostly pass; notes in Finding 8. All 23 stems
are plausibly project documentation; none is governance-text by name; none in
`docExcludedTokens`, `rootStems` or `FORBIDDEN_GUIDE_STEMS` (builder predicate
held). The suffix requirement is a sound guard against a bare `INSTALL`/`BUILD`
script (fixtures `INSTALL`, `BUILD` -> not documentation) and `.md/.rst/.txt`
are disjoint from `sourceExtensions`. Declines: SECURITY matches v2 Q3 and the
v2 builder mutant (`build_public_source_screening_scope_v2.py:769`
"a security root name added is caught") and the v2 act ("Q3 to Q5 at the
packet defaults", v2 act record line 48); MANIFESTO matches v2 Q1's stated
reason and the 2026-10-07 `none` choice (act record line 50); TLS and
redis.conf reasons are the drafter's own and sound; modules/MODULES.md reason
overstated (Finding 8). The delta (25-32) and packet (47-49) say honestly
that the list recovers none of the 89 spans.

**6. Option C's decline.** Sound; anchor weak (Finding 7). VIS-2,
`.syzygy/governance/doctrine/vision.md:133-135`: "Nothing turns green, and no
project is declared aligned, converged, or genome-complete (defined in
architecture.md), without current evidence." The delta's ellipsis quote is
faithful. REQ-035 sentence it should rest on: "Syzygy SHALL validate the
verdict before it counts: … that every inventory entry and every claim block
has an entry; … and that a verdict with an unresolved blocking finding does not
declare the subject ready." Marking unread-support rows non-blocking would let
readiness stand over claims with no evidence; that this needs a specification
delta, not a policy act, agrees with the bead's note "C needs REQ-035 spec
delta".

**7. Is the install requirement complete?** Incomplete (Finding 5). Sweeps at
base `b5a7e27a`, `git grep -lF` over `packages apps scripts .github`:
version literal `1.4.0-public-source-candidate.1.none.code-all` -> 8 files
(matches the ledger's 8); policy path -> 30 files (matches the ledger's 30);
`screenBody(` outside tests/testkits -> 7 call lines in 5 files
(`repo-corpus.ts:228`, `check.ts:590`, `close.ts:124`, `render.ts:204/280/383`,
`review.ts:190`) — all named by the ledger [Observed]. Second method for
body-screening consumers: `git grep -nE "readBlobs\(|detectSecrets\("` adds
`self-corpus.ts:54` (self corpus, not a target body) and `verbatim-route.ts:120`
(base PWB route) — outside this scope [Inferred]. Of the 30 policy-path files,
the ledger does not name `install_redis_sitting.py`, `simulate_redis_sitting.py`,
`check_spec_reconciliation.py`, `walkthrough-inputs.ts` (path in
`OTHER_ACT_BOUND_ARTIFACTS`, line 103), the `build_pwb_*` builders,
`record_public_source_screening_scope_v2_act.py`, or the test files; I did not
determine which of these break on a new digest [Unknown] beyond the Butlers
gate in `governance-inputs.ts` [Observed]. Named and present: act readers
(`POLICY_ACT_FORMS`), version pins, v3 recorder battery lines, CG-7e,
`detectSecrets` offsets (it returns `first` id only, content-classification.ts
175-182 [Observed]), both screens, call sites.

**8. Owner packet plain and single-question?** Pass, subject to Finding 3's
correction. One binding ask ("Sign screening scope version 4? Pick a variant,
or decline."), three choices, words "Sign screening scope version 4, variant
span-guides" naming a manifest row by variant, a recommendation with reasons
and a "What it costs" section. Its residual bullet is inaccurate (Finding 3)
and its "Order, as fact" omits the Butlers gate (Finding 5).

**9. Authority hygiene.** Pass. `grep -n -i -E "accepted|approved|adopted|in force"`
over the 4 package `.md` files and the manifest: 3 hits — REVIEW-BRIEF.md:70
(the criterion itself), SEMANTIC-DELTA.md:48 (quoting "the adopted policy" from
the requirement), SEMANTIC-DELTA.md:202 ("its Q3, accepted", a true statement
of the v2 act) — none labels this package. 64-hex sweep with Python `re`
`[0-9a-fA-F]{64}` and a second pattern `[0-9a-fA-F]{40,}` over the 4 `.md`
files: 0 and 0 in each [Observed]; the builder's `--check` predicate agrees.
`python3 scripts/check_governance.py` -> "32 OK, 21 WARN, 0 FAIL (53 checks)"
[Observed].
