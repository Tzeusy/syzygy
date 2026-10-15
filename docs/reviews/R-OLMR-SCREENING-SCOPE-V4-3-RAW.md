# R-OLMR-SCREENING-SCOPE-V4-3 — public-source screening scope v4, round 3

Reviewed commit: 05e76464d63493e0a12a1ce81bc45a507d02d823
Manifest SHA-256: 1aa08522b7755d278ab4ad8cb35370513eb1844fc5c7904355f7687b4ac2a4d1
Verdict: REVISE

Reviewer: fresh context (CC-REV-1), given the brief
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/REVIEW-BRIEF.md`,
the artifact (every package file and `scripts/build_public_source_screening_scope_v4.py`),
the references it lists, the round-1 and round-2 raws
(`docs/reviews/R-OLMR-SCREENING-SCOPE-V4-1-RAW.md`, `-2-RAW.md`) and the package's
`ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md` and `ROUND-2-REPAIR.md`.
I did not read, clone or fetch any target repository (Redis, Butlers or other).
Every target figure is from `bd show syzygy-olmr`. I modified no repository
file. Every probe ran from scratch scripts under
`/tmp/claude-1000/-home-tze-GitHub-syzygy/8a9a9799-8ec6-4119-b246-f5c4638ab751/scratchpad/r3/`.

The manifest digest was derived two ways and both agree [Observed]:
`python3 scripts/build_public_source_screening_scope_v4.py --manifest-digest`
and `sha256sum PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt` print the same
value (it is in the head above).

## Findings

**Finding 1 — the round-2 repair narrowed the PEM-header check: a key header that does not start its line now leaks the key body, which round-2's bytes excluded whole, and the package calls the change "widened, fail-closed"** (revise)

At round 2 (`9caa9043`) the policy held `"wholeArtifactFragments": ["-----BEGIN "]`. The rule
excluded the body whole when that fragment appeared **anywhere** in it
("the body holds none of wholeArtifactFragments (compared exactly,
case-sensitively)"). I checked this from the round-2 span patch at
`9caa9043`, applied with GNU `patch`. Its hash equals the `9caa9043` manifest
`span` row [Observed]. The round-3 repair replaced that fragment with the base64
starts `["LS0tLS1CRUdJT", "LS0tLSBCRUdJT"]` and added
`wholeArtifactLinePattern` `^[ \t]*-{4,}[ \t]*BEGIN`. The rule applies that
pattern "to each line without its terminator". So a dashed header now keeps
the body whole only when **nothing but spaces or tabs precedes it on its
line**. The anywhere-check is gone: builder line 84 replaces it, and the diff
`9caa9043..HEAD` of the builder shows `-WHOLE_ARTIFACT_FRAGMENTS = ["-----BEGIN "]`.

Probe `r3/regress.py` imports the round-2 builder (`git show 9caa9043:…`) and
the current builder. It runs each one's oracle over its own proposed `span`
bytes, using a documentation body (`README.md`) with a `token=` badge on line
1 [Observed]:

| Body (key header not at line start) | round-2 bytes | round-3 bytes | Key body line retained |
|---|---|---|---|
| JS template literal ``const key = `-----BEGIN EC PRIVATE KEY-----`` then key lines | excluded whole | withheld {1, 2} | line 4 |
| Python `KEY = """-----BEGIN EC PRIVATE KEY-----` | excluded whole | withheld {1, 2} | line 4 |
| JSON one-line `{"key": "-----BEGIN EC PRIVATE KEY-----\n…"}` | excluded whole | withheld {1, 2} | line 3 (the whole key) |
| Markdown blockquote `> -----BEGIN ENCRYPTED PRIVATE KEY-----` | excluded whole | withheld {1, 2} | line 4 |
| control: header at line start | excluded whole | excluded whole | none |

`r3/probe.py` over both current variants adds a list bullet (`- -----BEGIN`),
an indent of no-break spaces (U+00A0) and a BOM before a line-1 header. All
three are redacted with the key body retained (H4, H6, H7 below). Each of
these bodies contains `-----BEGIN `, so the round-2 bytes excluded all of them
whole. Taken together, 7 bodies (H1-H7) moved from excluded-whole to
key-material-retained in this round.

Why this is revise, not a note:
- It weakens the private-key exception, which criterion 2 names. The delta
  gives this reason for the check: key material "no detector matches"
  follows the header (SEMANTIC-DELTA.md:191-199; builder lines 80-81). That
  reason holds wherever the header sits on its line. The three
  `private-key-material` literals still match anywhere, so the exposed
  headers are the unlisted ones: EC, ENCRYPTED, DSA, PGP, SSH2.
- The package claims the opposite. ROUND-2-REPAIR.md:13 says "Check widened,
  fail-closed". SEMANTIC-DELTA.md:19 says "The PEM check is widened to any
  dashed BEGIN header line". SEMANTIC-DELTA.md:191 says "**Any dashed BEGIN
  header line keeps the body whole.** … That covers PEM … blocks whose
  headers the private-key literals do not list". The delta names only one
  remainder: "A base64 key encoded from any other offset is not caught"
  (SEMANTIC-DELTA.md:198-199). The mid-line header is disclosed nowhere.
- The owner packet gives the owner a key-block assurance that the bytes do
  not carry: "Three cases still withhold the whole file: … any line that
  starts with four or more dashes and then BEGIN (a PEM or SSH2 key block),
  or the base64 start of one" (OWNER-DECISION-PACKET.md:24-28). The words
  "starts with" are literally accurate. But the parenthesis tells the owner
  that key blocks are covered, and the "What it costs" list (63-79) does not
  name this case.
- [Inferred] A key inside a string literal in a README's code example is an
  ordinary documentation shape (signing-library examples). After round 2 it
  is also the one class of body that the redaction now admits only because
  of this round's edit.

Repair: keep the line pattern, and also restore the anywhere-check (the
`-----BEGIN ` and `---- BEGIN ` literals compared anywhere in the body), or
search `-{4,}[ \t]*BEGIN` anywhere instead of anchoring it. Then add a builder
body fixture with a mid-line header (for example the JS template literal
above, expected `None`) and a mutant that drops the anywhere-check. Correct
ROUND-2-REPAIR.md:13 and SEMANTIC-DELTA.md:19/191 to describe what the check
actually covers.

**Finding 2 — "Source and configuration files are not affected" is wider than the class rule** (note)

SEMANTIC-DELTA.md:287 and OWNER-DECISION-PACKET.md:75-76 say "Source and
configuration files are not affected: they stay whole-file", and the packet
says at 21-22 "Source code, configuration and every other file keep today's
rule". The class gate decides by path. Under version 3's own rules (unchanged
here), configuration-shaped content on a documentation path is
project-documentation, so it is redacted. Probes [Observed, `r3/probe.py`,
the K1 AWS-credentials body with an `ASIA` id, both variants]:
`docs/examples/credentials.txt`, `doc/.env.txt`, `docs/_static/env.example.txt`,
`docs/settings.py.txt`, `licenses/deploy-credentials.txt`, root `README` (no
suffix) and `00-ReadMe.TXT` are all `doc=True` and keep the secret access
key on line 3. `INSTALL.txt` does the same under `span-guides`. The gate itself
holds: `docs/conf.py`, `docs/x.md.py`, `src/config.PY` (the extension is
case-sensitive, so the file is unclassified), `docs/requirements.txt`, `aws.ini`,
`scripts/setup.sh`, `settings.py` and `config.js` are all excluded whole. No
source-extension file can reach project-documentation, because the suffix
sets are disjoint (policy `disjointFromSourceExtensions`). [Inferred] A config
dump as a `.txt` under `docs/` is uncommon, and an owner would likely read it
as documentation. Suggested wording: "files outside the project-documentation
paths (source and most configuration) are not affected".

**Finding 3 — common shapes beyond the six still reach the packet; "a URL with a password in it" overstates the URL detector** (note)

The cost statement now names six shapes and a general sentence ("a second
secret in that file that no detector recognises reaches the review packet…",
packet:66-69). That general sentence covers everything below, so none of it
is a case the policy claims to close. Probes [Observed, `r3/probe.py`,
documentation paths, both variants, each with a detector match elsewhere in
the body and the secret line retained]:
- non-`http(s)` credential URLs: `postgres://app:S3cretPassw0rd@db…` (P1) and
  `redis://default:S3cretPassw0rd@…` (P2), the trial target's own
  connection form. An `https` URL whose password contains `/` (P3) is not
  matched either: `[^/@\s]+` stops at the slash;
- YAML block scalars `password: |` and `password: >-` with the value on the
  next line (M1, M2). The indicator character blocks `credential-assignment`,
  so the guard line has no match to sit beside;
- a comment between key and value (M5); a Markdown table row
  `| password | … |` (M6); `DB_PASS=` / `pass:` forms (M10); a JSON key on
  its own line (M4);
- key formats with no dashed header: WireGuard `PrivateKey = …` (P6), a
  PuTTY `.ppk` block (H9), a Kubernetes `.dockerconfigjson` value (P7), and a
  base64 GCP key JSON in a Secret (H12). H12 and H10 (base64 starting at
  offset 1) are the disclosed "encoding does not begin at the header's first
  dash" case.

The packet's plain words (20-21) describe the redacted match as "a URL with a
password in it". The detector matches only `http`/`https` URLs whose user and
password contain no `/` or `@`. [Inferred] Naming non-http URLs and YAML block
scalars in the cost list would help an owner deciding over a Redis trial.
The continuation residual reproduces as stated: M3 (a token wrapped onto three
lines) keeps line 6, and M9 (backslash continuation over two lines) keeps
line 5.

## Round-2 repairs checked against the round-2 raw

| R2 finding | Raw's ask | Current bytes | Result |
|---|---|---|---|
| 1 (revise) six shapes | (a) state the shapes, write `AKIA`; or (b) narrow to project-documentation | Both arms. `redactedClasses: ["project-documentation"]` in both proposed files (jdiff). The appliesTo text reads "A body of any other class, code-content included, is excluded whole". Whole-file fixtures and two mutants hold. The six shapes are named at delta:286 and packet:69-75, with `AKIA…`/`ASIA…` written out | **Repaired** [Observed]. The K1, K3 and K7 bodies on code or unclassified paths are excluded whole. On documentation paths they keep the secret line, as disclosed. K2 (`README.md`) and K8 (`docs/setup.md`) keep line 3 and line 5 (`r3/probe2.py`). Residue: Findings 2 and 3 |
| 2 (note) residuals reproduce | none | unchanged | Confirmed again (M3, M9) |
| 3 (note) four-dash key | name or catch RFC 4716 and the base64 form | line pattern plus base64 fragments; fixtures "RFC 4716 key beside a badge", "indented PEM header beside a badge", "base64 PEM in a Secret example" | Four-dash and base64-at-0 forms are caught (H8 and H11 controls are excluded whole). **But the anywhere `-----BEGIN ` check was removed**: Finding 1 |
| 4 (note) docstring | update | builder:11-22 now describes the class restriction, every-offset matches, multi-line matches, the two whole-artifact detectors, the line pattern and the base64 fragments | Repaired |
| 5 (note) ledger residue, scan cost | name the nine files; name the cost | IMPACT-LEDGER.md:53-66 names all nine as "Unknown, the install assesses each". 79-82 names the lost early stop, the sticky loop and the possible quadratic backtracking in `credential-bearing-url`, with a breach meaning whole-file exclusion | Repaired |

## Per-criterion results

**1. Is the diff exactly the stated change?** Pass [Observed].
- `--check` printed "public-source-screening-scope-v4: patches and manifest
  current". `--selftest` printed "selftest: 40 of 40 predicates held".
- Base: `sha256sum` of the policy on disk equals the v3 manifest row
  `[variant: all]` (`r3/derive.sh`). The policy file is absent from
  `git diff --stat 9caa9043 HEAD` (74 files), so it is unchanged since round 2.
- Independent re-derivation (`r3/derive.sh`): copy the policy, apply each
  patch with GNU `patch`, then `sha256sum`. Both hashes equal the manifest's
  `span` and `span-guides` rows.
- JSON tree walk (`r3/jdiff.py`, every key and list index, key order checked).
  `span` changes `/policyVersion`, `/publicSourceScope/detectors` and
  `/publicSourceScope/inheritedRules`, and adds `/publicSourceScope/secretRedaction`.
  `span-guides` also changes `rules[2]/notMapped` and `rules[2]/pathRules[0]/rule`,
  and adds `rules[2]/rootGuideStems` and `rootGuideSuffixes`. No order change.
  This matches the delta's table (delta:85-91) row for row. The versions are
  `1.5.0-public-source-candidate.1.none.code-all.redact-span` and `…redact-span-guides`.

**2. Is the redaction fail-closed?** Fails on Finding 1. The mechanism holds
for what the detectors match.
- Population: `r3/probe.py` ran 50 bodies × 2 variants = 100 oracle calls.
  `r3/probe2.py` ran 5 bodies × 2 = 10 more. `r3/regress.py` ran 5 bodies
  through the round-2 oracle and the round-3 oracle (10 calls). The builder's
  13 body fixtures, 3 whole-file fixtures and oracle mutants also ran
  (selftest). Outcomes under `span-guides`, for the 50 bodies of `probe.py`:
  10 excluded whole, 5 redacted with the secret withheld, 35 redacted with a
  secret line retained. `span` has the same split except `INSTALL.txt`, which
  is excluded whole there (11 / 5 / 34). Of the 35:
  - 7 are Finding 1's header regressions (H1-H7);
  - 8 are Finding 2's config-on-documentation-path bodies (C1-C4, C7, C9,
    C11, C13);
  - 4 carry the K1/K3/K7 shapes on documentation paths (K1-doc, K3-doc,
    K7-doc and C12 `docs/sub/README.md`); these are the disclosed six;
  - 2 are the disclosed continuation residual (M3, M9);
  - 2 are the disclosed base64-not-at-offset-0 case (H10, H12);
  - 12 are other unmatched shapes (Finding 3).
- No body put a **matched** secret's characters on a retained line, an
  admitted span, a marker or the provenance record [Observed for all calls].
  Multi-line matches: every touched line is withheld. M7 (`password`, two
  blank lines, `= value`) withholds {2..7}. CR-only line ends: M8 withholds
  {2..6}, so the match crossing CR-only lines is withheld whole. The `g`
  flag: the oracle counts matches from every offset (fixture "hidden
  overlapping match", mutant observed). Re-screen: fixture "emptied lines join
  a new match" is excluded whole, with the mutant observed.
  `credential-bearing-url` keeps user and password inside its match (P4
  control: withheld). P5 and P8 show that a partner on a matched line beyond
  the guard is withheld because it matches itself.
- Private-key exception: the three literals still exclude the body whole
  anywhere in it (`r3/probe2.py`: a `-----BEGIN PRIVATE KEY-----` mid-line
  in JSON and a `-----BEGIN RSA PRIVATE KEY-----` in a string are both
  excluded whole). Unlisted headers are caught only at line start (Finding 1).
- Class gate: no source-extension path reaches project-documentation
  (Finding 2 lists the paths tried). The case fold applies only to the
  documentation rule, and the source-extension rule is case-sensitive, so an
  upper-case `.PY` is unclassified and excluded whole, which is fail-closed.
- Guard line: the delta calls it "a mitigation, not a proof" (delta:211-212)
  [Observed]. The continuation and co-location residuals are stated in both
  the delta (278-293) and the packet (63-79) [Observed]. The mid-line header
  residual is stated in neither (Finding 1).

**3. Is the authority claim right?** Pass [Observed]. RFC5-17
(`consent-egress-secrets.md:306`) defines "`redacted-span` (artifact
retained, matching spans replaced by markers with a count)", and :318 states
the retention rule. REQ-polaris-generation-025 (spec.md:1400, ID at 1402)
carries "redacted-span SHALL retain permitted surviving evidence at its
otherwise-earned tier with disclosed count" and "Redaction branches SHALL
remain limited to those the adopted policy permits". Its scenario "Partial
redaction retains usable support" is at :1424. I found no clause in
RFC5-14/16/17 or REQ-025/035 that requires whole-artifact exclusion for this
scope. REQ-035 (local-agent-mode spec.md:320) says "screening-admitted only".
The policy's `citedSpanRule` makes a span with no withheld line
"screening-admitted content of the body's class" and re-screens it, so the
span qualifies [Inferred].

**4. Is the scope bounded?** Pass [Observed, jdiff and builder predicates].
Only `publicSourceScope` and the shared `policyVersion` move. Redaction is now
narrower than at round 2 (`redactedClasses: ["project-documentation"]`).
`appliesTo` keeps agent-written text whole-screened, and `unchanged` keeps the
active-content scan whole-body. No class, consent, egress, `rawBodyHandling`,
`accessBoundary`, `sourceAdmission` or `prerequisite` change. The Butlers gate
pin effect is stated (ledger:23-34; packet:104-108).

**5. Variant `span-guides`.** Pass. The 23 stems are byte-identical to round
2's (builder diff `9caa9043..HEAD` touches no stem). None is in `rootStems`,
`FORBIDDEN_GUIDE_STEMS` or `docExcludedTokens` (predicates hold). The suffix
guard holds: `INSTALL` and `BUILD` are fixtures that stay unmapped, and
`.md`/`.rst`/`.txt` are disjoint from the 25 `sourceExtensions`. The declines
match their sources: SECURITY, MANIFESTO, TLS and redis.conf for the reasons
round 1 checked, and MODULES.md on the path-rule reason. The delta (40, 47)
and packet (56-58) say honestly that the list recovers none of the 89 spans.
Recovery of the 41 README spans stays Unknown (delta:43-47), consistent with
the bead.

**6. Option C's decline.** Pass [Observed]. VIS-2 at
`.syzygy/governance/doctrine/vision.md:133`: "Nothing turns green, and no
project is declared aligned, converged, or genome-complete (defined in
architecture.md), without current evidence." The delta's ellipsis drops only
the parenthesis. The REQ-035 sentences are "draft-to-source support for every
claim block" (spec.md:320) and "the rule that unresolved material omissions
prevent readiness" (spec.md:328).

**7. Is the install requirement complete?** Pass [Observed]. Sweeps at
`05e76464` used `git grep -lF` over `packages apps scripts .github`:
- version literal: 8 files, all 8 named (ledger:23-38);
- policy path: 30 files. All 18 non-test files are named across ledger:18-66.
  The 12 test or testkit files are covered by the ledger's "the tests pin it
  too" and the screen-test population (88-91) [Inferred];
- `screenBody(`/`detectSecrets(`/`readBlobs(` outside `*.test.ts`/`*.testkit.ts`:
  20 lines in 11 files, the same population as round 2.

Every target-body and agent-text call site is named (`repo-corpus.ts:228`,
`check.ts:590`, `review.ts:190`, `render.ts:204/280/383`, `close.ts:124`), as
are both screens. Class gating is a new install item (ledger:92-95), and
`screen.ts:88-90` already exposes `contentClass` [Observed]. Act readers,
version pins, recorder battery lines, CG-7e, the match offsets with their
cost, and the Butlers gate are present. [Inferred] Finding 1's repair adds a
fixture that the ledger's "builder's body fixtures through the TypeScript
screens" already carries.

**8. Is the owner packet plain and single-question?** On form, pass. There is
one binding ask ("Sign screening scope version 4? Pick a variant, or
decline."), three choices, words that name a manifest row by variant ("Sign
screening scope version 4, variant span-guides"), a recommendation with
reasons, and a cost section that now names the six shapes with `AKIA…` and
`ASIA…` written out. On substance, the key-block assurance at 24-28 is wider
than the bytes (Finding 1). Notes: Findings 2 and 3.

**9. Authority hygiene.** Pass [Observed]. `r3/hygiene.py` swept the 7
package `.md` files with Python `re` for
`\b(accepted|approved|adopted|in force|ratified|signed)\b`, case-insensitive.
It found 4 hits:
- REVIEW-BRIEF.md:70 ×2 (the criterion itself);
- SEMANTIC-DELTA.md:63 (quoting "the adopted policy" from REQ-025);
- SEMANTIC-DELTA.md:268 ("its Q3, accepted", a statement of the v2 act).

None labels this package. The builder docstring's "approved 2026-10-08" states
the v3 act. 64-hex sweep: Python `re`
`(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])` and `[0-9a-fA-F]{40,}` give 0
and 0 in each of the 7 files. `grep -rcE "[0-9a-fA-F]{64}"` gives 0 per file.
The builder's `--check` predicate agrees. `python3 scripts/check_governance.py`
reported "32 OK, 21 WARN, 0 FAIL (53 checks)".
