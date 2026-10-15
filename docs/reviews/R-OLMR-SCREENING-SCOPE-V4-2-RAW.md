# R-OLMR-SCREENING-SCOPE-V4-2 — public-source screening scope v4, round 2

Reviewed commit: 9caa9043dc1eb32ff756c2ee288e826263220924
Manifest SHA-256: f95efebfeb07b654800cefa46e5310223ef059d6b3aaa3060118029f24181c7f
Verdict: REVISE

Reviewer: fresh context (CC-REV-1), given the brief
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/REVIEW-BRIEF.md`,
the artifact, the references it lists, the round-1 raw
`docs/reviews/R-OLMR-SCREENING-SCOPE-V4-1-RAW.md` and `ROUND-1-DISPOSITIONS.md`.
No target repository (Redis, Butlers or other) was read, cloned or fetched;
every target figure below is from `bd show syzygy-olmr`. No repository file was
modified; all probes ran from a scratch directory.

Manifest digest derived two ways [Observed]:
`python3 scripts/build_public_source_screening_scope_v4.py --manifest-digest`
and `sha256sum` of `PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt` print the
same 64 hex characters (full value in the head above).

## Findings

**Finding 1 — the owner packet's cost statement reads as a long tail, but the secrets it admits include the commonest credential syntaxes in the file types this scope admits, including an AWS secret key beside an STS key id** (revise)

The packet's main-cost bullet (OWNER-DECISION-PACKET.md:60-66): "Under
version 4 a second secret in that file that no detector recognises reaches the
review packet, an agent session and the draft page, unless it sits on a
withheld line [Inferred]. The review found two such cases (an AWS secret key,
an EC private key) and both now keep the whole file withheld; the general risk
remains." Its plain-words section (packet:21-24) says the whole file is still
withheld for "a known token format such as an AWS key id (its secret key sits
on another line that no detector catches)". The delta's matching bullet
(SEMANTIC-DELTA.md:252-258) says the two closures "close the two cases the
review constructed; they do not close the class."

That statement is true but tells the owner nothing about how big the class is,
and naming "an AWS secret key" as closed invites a wider reading than the
closure has. The four detectors (policy `detectors`, unchanged) do not match
several of the commonest ways credentials are written in the extensions
`code-content` admits (`.py`, `.js`, `.ts`, `.go`, `.rb`, `.php`, `.sh`, …) and
in Markdown docs [Observed, from the patterns]:

- `credential-assignment` needs the keyword *directly* followed by
  `\s*[:=]`, so a quoted key (`"password": "…"` in JSON or JS, `'PASSWORD': '…'`
  in a Python dict) never matches, and neither does a keyword followed by `_` or a
  letter (`SECRET_KEY`, `STRIPE_SECRET_KEY`, `aws_secret_access_key`,
  `secretAccessKey`);
- `known-token-formats` matches only `AKIA` key ids, not `ASIA` (STS
  temporary) key ids, while the paired `aws_session_token = …` line *is* a
  `credential-assignment` match, so the body goes to line redaction instead of
  whole exclusion;
- the `-----BEGIN ` fragment is literal, so a base64-encoded PEM (a
  Kubernetes Secret's `tls.key: LS0tLS1CRUdJTi…`) does not hold it.

Probes [Observed]: scratch `r2/probe.py` imports the builder and calls its
oracle `withheld_lines` over both proposed files, re-derived by GNU `patch`
from the policy on disk (hashes equal the two manifest rows). "v3" is the
version-3 result (any detector match excludes the whole body):

| Probe | v3 | v4 (both variants) | Retained secret line |
|---|---|---|---|
| K1 AWS credentials file: `aws_access_key_id = ASIA…`, `aws_secret_access_key = wJalr…` on line 3, region, output, `aws_session_token = …` on line 6 | excluded whole (`credential-assignment`) | withheld {5, 6} of 6 | line 3, the secret access key |
| K2 JS: `secretAccessKey: 'wJalr…'` on line 3, a `password: 'hunter2hunter2'` object four lines below | excluded whole | withheld {7, 8, 9} of 9 | line 3 |
| K3 Django settings: `SECRET_KEY = 'django-insecure-…'` on line 2, `EMAIL_HOST_PASSWORD = '…'` on line 6 | excluded whole | withheld {5, 6} of 6 | line 2 |
| K4 Markdown k8s Secret example: `password: MWYy…` on line 5, `tls.key: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0t…` on line 8 | excluded whole | withheld {4, 5, 6} of 9 | line 8, a base64 private key |
| K7 JS object: `"url": "https://deploy:abc12345@db…"` on line 2, `"password": "OtherS3cretValue"` on line 5 | excluded whole (`credential-bearing-url`) | withheld {1, 2, 3} of 6 | line 5, a line that literally reads `"password": "…"` |
| K8 heredoc `.env`: `DB_PASSWORD=…` on line 2, `STRIPE_SECRET_KEY=sk_live_…` on line 5 | excluded whole | withheld {1, 2, 3} of 6 | line 5 |
| K10 control: round-1 AKIA Terraform pair | excluded whole | excluded whole | none |
| K11 control: EC PEM key beside a badge | excluded whole | excluded whole | none |

The re-screen and the cited-span screen do not catch any of K1-K8, because
neither detector pass matches the retained secret line (that is why it was
unmatched in the first place).

Judgement against the stated residual. The package does disclose the class
(packet:60-66, delta:252-258, policy `consequence`), so this is not a case the
policy's own words claim to close: the rule text and `consequence` are
accurate. It is revise rather than note on the brief's second test, a shape
common enough that the cost statement misleads:
(a) these are not exotic encodings but the default syntax of settings files,
SDK client configs and `.env` heredocs. A `.py`, `.js` or `.ts` file whose one
`credential-assignment` hit is a placeholder password is the typical case
where v3's whole-file exclusion was doing the work. And the delta's own reason
for the change says the match is the evidence: "A body with a detector match
is evidence that the file carries credentials" (delta:252-253);
(b) "The review found two such cases (an AWS secret key, …) and both now keep
the whole file withheld" will be read as "AWS secret keys are handled". K1
shows that holds only for `AKIA` ids, and the round-1 shape (finding 1) recurs
unchanged with an `ASIA` id;
(c) the owner is asked to trade this against the 41 README spans, and the
packet gives no example of what the trade admits beyond the two closed cases.

Repair (one of): state plainly in the packet's "What it costs" and in the
delta's "What it gives up" that the detectors do not recognise quoted keys
(`"password":`), `…SECRET_KEY` / `secretAccessKey` forms, STS (`ASIA`) key ids or
base64-encoded keys, so in a file with any line-redacted match those secrets
are admitted, with K1 as the AWS example and the word "AKIA" in place of "an
AWS key id"; or narrow the redaction's `appliesTo` (for example, to
`project-documentation` bodies only, which is where the trial's 41 spans are,
leaving `code-content` whole-artifact), which would make the cost statement
true as written. The second is a policy choice and the owner's to make; the
first is the minimum.

**Finding 2 — the disclosed residuals reproduce as stated** (note)

Probes [Observed, same script]:
- K5 (YAML plain scalar `token: abcdefgh12345678` wrapped over two more
  lines): withheld {1, 2, 3} of 5; line 4 `CONTINUED2PART` retained.
- K12 (JS string concatenation `const token = 'abcdefgh' +` then three
  `'…' +` lines): withheld {1, 2} of 4; lines 3-4 retained.
- K6 (`.netrc` block `password Hunter2Hunter2Real`, with no `:` or `=`, five
  lines below a `token=` badge): withheld {1, 2} of 7; line 6 retained.

K5 and K12 are the residual "a secret that a detector matches on one line and
that continues past the guard line onto further lines is admitted in its
unmatched part" (delta:259-260; packet:67-68). K6 is Finding 1's co-location
class. Concatenation (K12) is a common way to wrap a long literal in code, and
it shows that "one guard line" is a mitigation and nothing more, as the delta
says (delta:183-186). No further repair is needed beyond Finding 1.

**Finding 3 — "Any PEM header" is wider than the literal fragment** (note)

SEMANTIC-DELTA.md:170: "**Any PEM header keeps the body whole.**" The
fragment is `-----BEGIN ` exactly, five dashes and a space. An RFC 4716 /
SSH.com private key (`---- BEGIN SSH2 ENCRYPTED PRIVATE KEY ----`, four dashes)
does not hold it. Probe K9 (that block three lines below a badge): v3 excluded
whole; v4 withheld {1, 2} of 6, key body on line 5 retained [Observed]. RFC
4716 is not PEM, so the heading is literally true, but the reason given (a key
"whose header the private-key literals do not list") covers this format too.
Say "a `-----BEGIN ` header" and name the four-dash format, together with the
base64-encoded form (Finding 1), as admitted.

**Finding 4 — the builder's module docstring still describes the round-0 rule** (note)

`scripts/build_public_source_screening_scope_v4.py:11-17`: "Version 4 retains a
body a single-line detector matches as RFC5-17's `redacted-span` … A
`private-key-material` match still excludes the body whole". After the round-1
repair, `known-token-formats` and the `-----BEGIN ` fragment also keep the body
whole, the match set counts every offset, and `credential-assignment` matches
can span lines (fixture "assignment across lines"). The comment at line 72-77
was corrected; the docstring was not.

**Finding 5 — ledger completeness residue; the every-offset scan is install work the ledger names only by offsets** (note)

- The 30-file policy-path sweep (re-run below) has members that the ledger
  neither names nor dispositions: `walkthrough-inputs.ts` (line 103, path only
  in `OTHER_ACT_BOUND_ARTIFACTS`), `test-walkthrough-judgment-fixture.ts:215`,
  `build_public_source_screening_scope.py`, `build_pwb_behavior_contract_repin.py`,
  `build_pwb_behavior_contract_repin_tree_framing.py`,
  `build_pwb_effect_acts_packet.py`, `build_pwb_truth_policy_amendment.py`,
  `record_public_source_screening_scope_v2_act.py`, and
  `packages/polaris-generation-consent/README.md`. Round 1 asked to "either
  name or explicitly disposition the other members". The four named are
  dispositioned "Unknown; the install assesses each" (IMPACT-LEDGER.md:45-52).
  One sentence putting the rest in that bucket, or saying why they do not
  break, would close it. [Inferred] Most are prior-package builders that read
  the path for their own superseded `--check`.
- The screens compile each detector with its policy flags and call
  `expression.test(text)` after resetting `lastIndex`
  (`content-classification.ts:159-164`), and `detectSecrets` keeps only the
  first matching id (175-182) [Observed]. "Every match from every offset"
  needs a sticky per-offset loop and gives up v3's early stop at the first hit.
  The ledger names the offsets (IMPACT-LEDGER.md:60-68). It does not name the
  cost: `credential-bearing-url`'s `[^/@\s]+:[^/@\s]+@` backtracks
  quadratically over a long run without `/`, `@` or whitespace, now at every
  `http` offset of every matched body [Inferred]. Worth one line for the
  install's resource limits.

## Round-1 repairs checked against the round-1 raw

| R1 finding | Raw's ask | Current bytes | Result |
|---|---|---|---|
| 1 (blocking) AKIA | `known-token-formats` whole-artifact, fixture, correct delta:146-149 and builder comment | `wholeArtifactDetectors: ["private-key-material", "known-token-formats"]` in both proposed files (jdiff probe); fixture "AWS access-key id with its secret key" → None; mutant "known-token-formats moved to redaction caught" holds; delta:161-169 rewritten; builder line 72-74 rewritten | Repaired; K10 control excluded whole. Docstring residue: Finding 4. Same shape with `ASIA`: Finding 1 |
| 2 (revise) `g` scan | every-offset match set, fixture, mutant | rule text "every match it makes starting at any offset of the text, overlapping matches included"; oracle `all_offsets` (lines 317-329); fixture "hidden overlapping match" → {1..6}; mutant "a non-overlapping scan leaks the hidden match's value line" holds | Repaired. [Inferred] For these four patterns Python's greedy match at a fixed offset reaches the furthest line any match from that offset can reach (each `\s*`/`{n,}` is forced to be maximal), so one match per offset suffices |
| 3 (revise) co-location | state plainly in delta and packet | delta:252-258 and packet:60-66 lead with it; `-----BEGIN ` fragment added; fixture "EC key beside a badge" → None | Repaired as asked; Finding 1 says the statement is still not enough for the owner |
| 4 (revise) REQ-025 | correct the citation | delta:49, brief:21 say REQ-polaris-generation-025; spec.md:1400 holds the quoted sentences, `ID: REQ-polaris-generation-025` at 1402, scenario at 1424 [Observed] | Repaired |
| 5 (revise) Butlers gate | name the break in ledger and packet; name or disposition the others | ledger:23-34 names `governance-inputs.ts` 76-104 (verified: lines 76, 83, 100, 104); packet:94-98 "breaks both read gates, the public-target gate and the Butlers gate"; ledger:45-56 names 4 consumers plus egress | Repaired; residue in Finding 5 |
| 6 (note) digest oracle | state the residual | `withheldLines` ends "so a guess at short withheld lines can be checked against them; the target being public does not lift this residual"; delta:196-200 | Repaired |
| 7 (note) REQ-035 paraphrase | quote the clause | delta:248 quotes "draft-to-source support for every claim block" (spec.md:320 [Observed]) and "rule that unresolved material omissions prevent readiness" (spec.md:328 [Observed]) | Repaired |
| 8 (note) wide reasons | MODULES reason; credit names; support/development | delta:246 "no path rule maps it"; delta:225-232 credit names on the general definition and `authors`; one sentence each for SUPPORT and DEVELOPMENT | Repaired |
| 9 (note) marker / dialect | per-run vs per-body; both engines | policy "each run of consecutive withheld lines is replaced by one marker that names … the total count of withheld lines in the body"; ledger:84-86 agrees; ledger:66-68 requires the fixtures through the TS screens | Repaired |

## Per-criterion results

**1. Is the diff exactly the stated change?** Pass [Observed].
- `--check` → `public-source-screening-scope-v4: patches and manifest current`;
  `--selftest` → `selftest: 37 of 37 predicates held`.
- Base: `sha256sum` of the policy on disk equals the v3 manifest row
  `[variant: all]`. The policy file is unchanged between `676adea9` and
  `9caa9043` (absent from `git diff --stat 676adea9 9caa9043`, 98 files).
- Independent re-derivation (`r2/derive.sh`: copy the policy, apply each patch
  with GNU `patch`, `sha256sum`): both hashes equal the manifest's `span` and
  `span-guides` rows.
- JSON tree walk (`r2/jdiff.py`, every key and list index, key order checked):
  `span` changes `/policyVersion`, `/publicSourceScope/detectors` and
  `/publicSourceScope/inheritedRules`, and adds `/publicSourceScope/secretRedaction`.
  `span-guides` also changes `rules[2]/notMapped` and
  `rules[2]/pathRules[0]/rule`, and adds `rules[2]/rootGuideStems` and
  `rootGuideSuffixes`. No key-order change. This is the delta's table
  (delta:75-81) row for row. Versions are `1.5.0-public-source-candidate.1.none.code-all.redact-span`
  and `…redact-span-guides`, as stated.

**2. Is the redaction fail-closed?** Fails on Finding 1's honesty test; the
mechanism itself holds for what the detectors match.
- Population: 12 constructed bodies (K1-K12) × 2 variants = 24 oracle calls,
  plus the builder's 10 body fixtures and its 3 oracle mutants (selftest).
  Of the 12: 2 controls excluded whole (K10, K11); 10 redacted with a secret
  line retained. Of those 10, 3 are the stated continuation or co-location
  residual (K5, K6, K12; Finding 2), 6 are common unmatched syntaxes
  (K1-K4, K7, K8; Finding 1) and 1 is the four-dash key format (K9; Finding 3).
  All 10 were excluded whole under v3.
- No body put a *matched* secret's characters on a retained line, an admitted
  span, a marker or the provenance record [Observed for the 24 calls and the
  fixtures]. Multi-line matches: every touched line is withheld (fixture
  "assignment across lines"). `g` flag: repaired (above). CR-only ends:
  round-1 probe C held; the oracle splits at LF/CRLF/CR, as the generator
  does. Re-screen: fixture and mutant hold. Private-key exception: now three
  literals, plus the AKIA detector, plus the `-----BEGIN ` fragment.
  Marker: a count only. Provenance: digest, path, policy ids, class, detector
  ids, line numbers. The guessing-oracle residual is stated.
- Guard line: called "a mitigation, not a proof" (delta:183-186)
  [Observed]. Residual stated in both the delta (252-264) and the packet
  (60-69) [Observed], but understated for the owner (Finding 1).

**3. Is the authority claim right?** Pass. RFC5-17
(`consent-egress-secrets.md:306-307`) defines "`redacted-span` (artifact
retained, matching spans replaced by markers with a count)", and 318-321 gives
the surviving-content rule. RFC5-16 (270-271): "content matching the policy is
excluded" is met by withholding the matching lines. RFC5-16 also says "The act
warrants use of the policy; it is never evidence that screening succeeded or
that admitted content is secret-free", which fits a disclosed residual.
REQ-polaris-generation-025 (spec.md:1400, ID at 1402) carries both quoted
sentences, and its scenario at 1424 is satisfied by an explicit act. I found no
clause in RFC5-14/16/17 or REQ-025/035 that requires whole-artifact exclusion
for this scope. REQ-035 (spec.md:320) "screening-admitted only": the policy's
`citedSpanRule` declares a span with no withheld line "screening-admitted
content of the body's class" and re-screens it, so it qualifies [Inferred]. The
RFC5-17 trust-floor sentence ("A secret reproduced in any surface … is a
trust-floor violation") is the reason Finding 1 matters, not a bar to the act.

**4. Is the scope bounded?** Pass on the bytes [Observed, jdiff and builder
predicates]. Only `publicSourceScope` and the shared `policyVersion` move.
`appliesTo` excludes agent-written text, and `unchanged` keeps the
active-content scan whole-body. No class, consent, egress, `rawBodyHandling`,
`accessBoundary`, `sourceAdmission` or `prerequisite` change. The shared
version and digest reach the Butlers gate pin, which is now stated
(ledger:23-34; packet:94-98).

**5. Variant `span-guides`.** Pass. 23 stems. None is in `rootStems`,
`FORBIDDEN_GUIDE_STEMS` or `docExcludedTokens` (builder predicates hold), and
all are plausibly RFC5-14 project documentation; the credit names and
SUPPORT/DEVELOPMENT are argued (delta:223-232). The suffix requirement is a
sound guard: fixtures `INSTALL` and `BUILD` are not documentation; `.md`,
`.rst` and `.txt` are disjoint from the 25 `sourceExtensions` [Observed]. The
declines match their sources as round 1 checked, with MODULES.md now on the
path-rule reason. The delta (34-37) and packet (51-53) say honestly that the
list recovers none of the 89 spans.

**6. Option C's decline.** Pass. VIS-2 at
`.syzygy/governance/doctrine/vision.md:133-135`: "Nothing turns green, and no
project is declared aligned, converged, or genome-complete (defined in
architecture.md), without current evidence." The delta's ellipsis drops only
the parenthesis. REQ-035 sentences: "draft-to-source support for every claim
block" (spec.md:320) and "the rule that unresolved material omissions prevent
readiness" (spec.md:328). The delta says the blocking count itself is
implementation, which agrees with the bead ("readiness basis").

**7. Is the install requirement complete?** Pass with notes (Finding 5).
Sweeps at `9caa9043`, `git grep -lF` over `packages apps scripts .github`:
version literal → 8 files (the ledger's 8; all 8 named or covered);
policy path → 30 files (the ledger's 30); `screenBody(`/`detectSecrets(`/`readBlobs(`
outside `*.test.ts`/`*.testkit.ts` → 20 lines in 11 files (counted from the output). The ledger names
every target-body and agent-text call site (`repo-corpus.ts:228`,
`check.ts:590`, `review.ts:190`, `render.ts:204/280/383`, `close.ts:124`) and
both screens (`screen.ts`, `public-source-screening.ts`, including their path
screens at 86/157, which the redaction does not touch). `self-corpus.ts:54` and
`verbatim-route.ts:120` are outside this scope [Inferred]. Act readers, version
pins, the v3 recorder battery lines, CG-7e, `detectSecrets` offsets and the
Butlers gate are present. Missing: the residue in Finding 5.

**8. Is the owner packet plain and single-question?** One binding ask ("Sign
screening scope version 4? Pick a variant, or decline."), three choices, words
that name a manifest row by variant ("Sign screening scope version 4, variant
span-guides"), a recommendation with reasons and a "What it costs" section:
pass on form. The cost statement fails on substance (Finding 1).

**9. Authority hygiene.** Pass. `grep -n -i -E "accepted|approved|adopted|in force"`
over the 5 package `.md` files and the manifest gives 3 hits:
REVIEW-BRIEF.md:70 (the criterion itself), SEMANTIC-DELTA.md:53 (quoting "the
adopted policy" from REQ-025) and SEMANTIC-DELTA.md:242 ("its Q3, accepted", a
statement of the v2 act). None labels this package. 64-hex sweep with Python
`re` (`(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])`) and a second pattern
`[0-9a-fA-F]{40,}` over the 5 `.md` files: 0 and 0 in each [Observed], and
the builder's `--check` predicate agrees. `python3 scripts/check_governance.py`
→ "32 OK, 21 WARN, 0 FAIL (53 checks)" [Observed].
