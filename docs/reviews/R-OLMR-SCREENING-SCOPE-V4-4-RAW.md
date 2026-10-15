# R-OLMR-SCREENING-SCOPE-V4-4 — public-source screening scope v4, round 4

Reviewed commit: 65edb1cbbec97384afd7b71e9c069736c89d767c
Manifest SHA-256: 0621d646f91ef3b5572d882f4bb17f5bd0785d316b30516693e48884365157ec
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh context (CC-REV-1). I was given the brief
`.syzygy/governance/contracts/candidates/public-source-screening-scope-v4/REVIEW-BRIEF.md`,
the artifact (every package file and `scripts/build_public_source_screening_scope_v4.py`),
the references the brief lists, the round-1, round-2 and round-3 raws
(`docs/reviews/R-OLMR-SCREENING-SCOPE-V4-1-RAW.md`, `-2-RAW.md`, `-3-RAW.md`),
and the package's `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`,
`ROUND-2-REPAIR.md`, `ROUND-3-DISPOSITIONS.md`, `ROUND-3-REPAIR.md` and
`ROUND-3-OWNER-DIRECTION.md`. I did not read, clone or fetch any target
repository (Redis, Butlers or other), and I opened none on disk (SEC-2). Every
target figure comes from `bd show syzygy-olmr`. I modified no repository file
and committed nothing. Every probe ran from scratch scripts under
`/tmp/claude-1000/-home-tze-GitHub-syzygy/8a9a9799-8ec6-4119-b246-f5c4638ab751/scratchpad/r4/`
(`derive.sh`, `jdiff.py`, `probe.py`, `regress.py`, `hygiene.py`).

I derived the manifest digest two ways and both give the value in the head
[Observed]: `python3 scripts/build_public_source_screening_scope_v4.py --manifest-digest`
and `sha256sum .../PUBLIC-SOURCE-SCREENING-SCOPE-V4-MANIFEST.txt`.
`git rev-parse HEAD` in the worktree printed the reviewed commit.

## Findings

**Finding 1 — the delta's "Not caught" list for key headers is narrower than what the bytes miss** (note)

SEMANTIC-DELTA.md:216-218 says: "Not caught: a header with other spacing in
the middle of a line (for example three spaces after four dashes), and a
base64 key encoded from any other offset." In this sentence's place it reads
as the complete list of escapes. Probes `r4/probe.py` C5-C14 [Observed, both
variants, `README.md`, each with a `token=` badge on line 1] found other
headers the policy also does not keep whole. In each case the key-material
line is retained.
- C5: a URL-encoded header mid-line (`-----BEGIN%20EC%20PRIVATE%20KEY-----%0A…`
  in a curl `-d`). Withheld {1, 2}; line 3 is retained.
- C6: a JSON header with ` `-escaped spaces. Line 3 is retained.
- C7: a header split by string concatenation (`"-----BEG" + "IN EC …"`, the
  form this builder uses for its own fixtures). Lines 3 and 4 are retained.
- C8: typographic en-dashes in place of `-`. Line 4 is retained.
- C11: a three-dash `--- BEGIN KEY ---` at line start. Line 4 is retained.
- C14: a lower-case `-----begin ec private key-----`. Line 4 is retained.

C9, C10, C12 and C13 are the disclosed "other spacing" case, and C2 and C3
(base64 not at offset 0, including base64 of openssl `pkcs12 -nodes` output
that begins with `Bag Attributes`) are the disclosed offset case.

Why this is a note: none of these forms is a detector match. The delta's main
cost ("a secret no detector matches reaches the fidelity packet",
SEMANTIC-DELTA.md:297-303) and the packet's ("a second secret in that file
that no detector recognises reaches the review packet",
OWNER-DECISION-PACKET.md:69-73) already cover them. The packet's key-block
sentence (OWNER-DECISION-PACKET.md:29-32) lists exactly what the bytes catch
("`-----BEGIN ` or `---- BEGIN ` anywhere in the file, even mid-line, any line
starting with four or more dashes and then BEGIN, or the base64 start of a
header"), so it does not overclaim. [Inferred] Of these forms only C7 is
plausible in documentation. Suggested wording: "Not caught, among others: …;
any encoded, escaped or split header".

**Finding 2 — common unmatched credential shapes reach the packet that the cost list does not name individually** (note)

Probes [Observed, `r4/probe.py`, both variants, `README.md`, with a
detector match elsewhere in the body]. Each is redacted and the secret line is
retained.
- E2: Azure storage connection string `AccountKey=…`.
- E3: `Authorization: Bearer <JWT>` in a curl example.
- E4: `curl -u admin:Sup3rS3cretValue`.
- E5: a GitHub fine-grained PAT (`github_pat_…`, which
  `known-token-formats`' `gh[pousr]_` does not cover).
- E6: Stripe `sk_live_…`, OpenAI `sk-proj-…` and Google `AIza…`.
- E7: a passphrase with spaces (`password = "correct horse battery staple"`;
  no run of 8 non-space characters).
- A3 and A4: YAML block scalars `password: |` and `client_secret: >-`.
- A5: a JSON key on its own line.
- A6: a Python triple-quoted token.
- B2: a value split by concatenation.

Round 3 (Finding 3) already noted A3, A4 and the JSON shape. The general
sentence quoted under Finding 1 covers all of these, so the policy claims to
close none of them. The packet names the six round-2 shapes and the non-http
URLs as examples ("These common shapes do"), not as a closed list.
[Inferred] An owner reading the packet would still under-weight provider API
keys (`sk_live_`, `AIza`, `github_pat_`) and `Authorization` headers, which
are common in README quick-starts. Naming them in a clause would help.

**Finding 3 — the packet does not carry the delta's `https`-password-with-`/` case, and its plain words still say "a URL with a password in it"** (note)

SEMANTIC-DELTA.md:306-309 says "The URL detector, `credential-bearing-url`,
matches `http://` and `https://` only, so a password in a `postgres://` … …
reaches the packet too, as does an `https` password containing `/` (round 3,
finding 3)". OWNER-DECISION-PACKET.md:21 says "an `http` or `https` URL with
a password in it", and :79-81 names only the non-`http` schemes. Probe E9
(`https://user:pa/ssw0rd@host/`) is redacted with line 5 retained [Observed].
This is within the general cost sentence, so it is a note. Suggested
addition to packet:81: "or an `https` password containing `/` or `@`".

**Finding 4 — editorial residue in the round-3 repair of round-3 Finding 2** (note)

SEMANTIC-DELTA.md:199-205 reads: "a `.txt` file under `docs/`, `doc/` or
`licenses/` (for example a docs settings .txt file), or a root file with a
documentation stem and no suffix, is classed by its path and is redacted by
line like any other documentation (round 3, finding 2) (round 2, finding 1,
arm (b); builder whole-file fixtures …)". The round-2 citation and its
whole-file fixtures belong to the bullet's opening sentence (code-content
stays whole), but they now trail the documentation-path sentence.
"(for example a docs settings .txt file)" is also unclear. The substance is
right: paths `docs/.env.txt`, `docs/settings.py.txt`, `doc/aws-credentials.txt`,
`licenses/deploy.txt`, `docs/secrets.txt`, `docs/credential.txt`,
`Docs/Setup.TXT`, `DOCS/x.Md`, root `README`, `CHANGES` and `00-NEWS` are all
redacted by line, and so are `INSTALL.txt` and `SUPPORT.rst` under
`span-guides` [Observed, probe G]. Two small gaps: `.md`/`.rst` files under
`docs/` (for example `docs/config.yaml.md`, probe G) are also documentation
by path, and the docs-tree `docExcludedTokens` hold no `secret`, `credential`
or `env` word. Both fall under the delta's general statement that the class
is decided by path.

**Finding 5 — the impact ledger does not name the two whole-artifact header checks as install items** (note)

IMPACT-LEDGER.md:74-87 names the match offsets, "the line placement, guard,
re-screen and span test", the Python-versus-JavaScript `\s` difference, and
the requirement to run the builder's body fixtures through the TypeScript
screens. It does not name `wholeArtifactLinePattern` (a per-line regex, which
in JavaScript needs per-line application or the `m` flag) or the
anywhere-in-body `wholeArtifactFragments` comparison. [Inferred] The fixtures
requirement carries them, because six body fixtures exercise them, including
the three new mid-line fixtures. So this is a completeness note, not a gap
that would let the install ship without the checks.

No blocking or revise finding.

## Round-3 repairs checked against the round-3 raw

| R3 finding | Raw's ask | Current bytes | Result |
|---|---|---|---|
| 1 (revise): mid-line key header leaks key body | keep the line pattern, restore an anywhere `-----BEGIN ` / `---- BEGIN ` check, add a mid-line fixture and a mutant, correct ROUND-2-REPAIR.md:13 and delta:19/191 | Both proposed files hold `"wholeArtifactFragments": ["-----BEGIN ", "---- BEGIN ", "LS0tLS1CRUdJT", "LS0tLSBCRUdJT"]` beside the unchanged `^[ \t]*-{4,}[ \t]*BEGIN` (`r4/jdiff.py`). The rule text says either check excludes the body whole. Three mid-line fixtures (template literal, one-line JSON, list bullet). Predicates "a dropped anywhere header fragment caught", "a dropped anywhere RFC 4716 fragment caught" and "a mid-line fixture flip caught (anywhere check gone)" all hold. ROUND-2-REPAIR.md:13 and delta:19-22 carry dated "marked" notes that keep the false text quoted. Delta:206-218 and packet:29-32 describe both checks | **Repaired** [Observed]. `r4/regress.py` rebuilds the round-3 raw's H shapes (Python triple-quoted header, `> -----BEGIN ENCRYPTED`) and adds D1-D7 (blockquote, BOM, NBSP indent, `----- BEGIN`, PGP armour in backticks, header split across lines, CR-only line ends). All of them, under both variants, are now excluded whole. The list-bullet fixture (`- key: ---- BEGIN SSH2 …`) is excluded whole now and was redacted under **both** the round-2 and the round-3 bytes, so this round also closes a case round 2 missed |
| 2 (note): "source and configuration not affected" overclaims | narrow the wording | delta:199-205 and :311-313; packet:22-25 and :82-83 say a configuration-shaped file the path rules class as documentation is redacted like documentation | Repaired; editorial residue in Finding 4 |
| 3 (note): more shapes; URL detector is http/https only | narrow the URL wording | delta:306-310 names `http`/`https` only, five non-http schemes, and the `/` case. Packet:79-81 names non-http schemes | Repaired; the packet omits the `/` case (Finding 3) |

**No regression of round-2 or round-3 confirmed behaviour** [Observed].
`r4/regress.py` imports the round-2 builder (`git show 9caa9043:…`, the
reviewed commit of `-2-RAW.md`), the round-3 builder (`git show 05e76464:…`)
and the current builder. Each oracle runs over its own `propose()` bytes from
the same base. The population per variant is 92 bodies: the 71 probes, the
current builder's 16 body fixtures and 3 whole-file fixtures, and 2 rebuilt
round-3 shapes. That makes 184 comparisons. A regression is a body an earlier
round excluded whole that the current bytes redact, or a body whose current
withheld set is not a superset of the earlier one. Count: **0 regressions**.
The diff `05e76464..HEAD` of the builder and the two patches adds only the
two fragment strings, three fixtures and three predicates
(`git diff 05e76464 HEAD -- scripts/build_public_source_screening_scope_v4.py …/proposed`).
Class gating (`redactedClasses: ["project-documentation"]`), the every-offset
match set, the re-screen, the cited-span rule and the digest rule are
byte-unchanged.

## Per-criterion results

**1. Is the diff exactly the stated change?** Pass [Observed].
- `--check` printed "public-source-screening-scope-v4: patches and manifest
  current". `--selftest` printed "selftest: 43 of 43 predicates held".
- Base: `sha256sum` of the policy on disk equals the version-3 manifest row
  `[variant: all]`.
- Independent re-derivation (`r4/derive.sh`): copy the policy, apply each
  patch with GNU `patch`, then `sha256sum`. `span` and `span-guides` both
  equal their manifest rows.
- JSON tree walk (`r4/jdiff.py`, every key and list index, with key order
  checked). `span` changes `/policyVersion`, `/publicSourceScope/detectors`
  and `/publicSourceScope/inheritedRules`, and adds
  `/publicSourceScope/secretRedaction`. `span-guides` also changes
  `contentClassification/rules[2]/notMapped` and `rules[2]/pathRules[0]/rule`,
  and adds `rules[2]/rootGuideStems` and `rootGuideSuffixes`. No order change
  appears. This matches the delta's table (SEMANTIC-DELTA.md:95-101) row for
  row. The versions are `1.5.0-public-source-candidate.1.none.code-all.redact-span`
  and `…redact-span-guides`.

**2. Is the redaction fail-closed?** Pass, with Notes 1-4 [Observed unless
marked].
- Population: `r4/probe.py` ran 71 bodies × 2 variants = 142 oracle calls,
  and `r4/regress.py` ran 184 more comparisons (above). The builder's 16 body
  fixtures, 3 whole-file fixtures and its oracle mutants ran in the selftest.
- **No detector-matched secret reached a retained line, an admitted span, a
  marker or the provenance record** in any call.
  - Multi-line matches: F1 (`password`, blank lines, `= value`) withholds
    every touched line plus guards. A7 (`secret:` with the value on the next
    line) is one match across two lines, withheld.
  - CR-only line ends: F2 is withheld across the CR lines.
  - Line separators the splitter ignores: F5 (form feed) and F6 (U+2028)
    keep the match on one counted line, which is withheld whole, so nothing
    leaks.
  - The `g` flag's non-overlapping scan: F4 (`secret_token: …`), and the
    selftest's "hidden overlapping match" fixture with its mutant observed.
  - Re-screen: fixture "emptied lines join a new match" is excluded whole,
    with its mutant observed.
  - `credential-bearing-url`: F3 withholds the user and password.
  - Provenance records only the digest, path, policy ids, class, detector
    ids and withheld line numbers (policy `provenance` field). The marker
    carries only a count (`withheldLines`).
- **Private-key exception and the header checks:** D1-D8 and the six header
  fixtures are excluded whole, under both variants. The union of
  `wholeArtifactFragments` (anywhere, exact) and `wholeArtifactLinePattern`
  covers every literal five-dash PEM or `---- BEGIN` header in any position,
  and base64 of either at offset 0 (C1; C4 with the base64 wrapped at 64
  columns). Not covered, and all reaching the packet only as unmatched
  secrets: other spacing mid-line (disclosed), base64 from another offset
  (disclosed), and the encoded, escaped, split, typographic, three-dash and
  lower-case forms of Finding 1.
- **Unmatched secrets** (the co-location cost):
  - continuation past the guard: A1, A8 and B1, the disclosed residual,
    reproduced;
  - heredoc second secret: A2 (disclosed);
  - an ASIA id with the secret key two lines from a matched session token:
    E1 (disclosed);
  - non-http URL: E8 (disclosed);
  - https with `/`: E9 (disclosed in the delta; Finding 3);
  - other shapes: Finding 2.
  Each is within the stated cost. None is a claim the policy's own words
  make: the `consequence` field says "a secret in such a body that no
  detector matches (one beyond the guard line, or one continuing past it) is
  admitted".
- **Paths into project-documentation** (probe G, 24 paths × 2 variants):
  - Redacted by line under both variants: `docs/.env.txt`,
    `docs/settings.py.txt`, `doc/aws-credentials.txt`, `licenses/deploy.txt`,
    root `README`, `CHANGES`, `00-NEWS`, `docs/config.yaml.md`,
    `Docs/Setup.TXT`, `docs/a/b/c/d.rst`, `docs/secrets.txt`,
    `docs/credential.txt` and `DOCS/x.Md`.
  - Redacted by line under `span-guides` only (excluded whole under `span`):
    `INSTALL.txt` and `SUPPORT.rst`.
  - Excluded whole under both variants: `README.md.py`, `docs/conf.py`,
    `docs/x.yaml`, `src/README.md`, `docs/requirements-dev.txt`,
    `licenses/a/b.txt`, `.env`, `README.yaml` and `README.txt.sh`.

  No source-extension path reaches project-documentation; the suffix sets are
  disjoint (`disjointFromSourceExtensions`). Config-shaped content reaches it
  only by a documentation path, as the delta and packet now disclose
  (Finding 4 on wording).
- Guard line: called "a mitigation, not a proof" (SEMANTIC-DELTA.md:228-231).
  The continuation residual is stated in the delta (:314-315) and the packet
  (:84-85), and the co-location cost in both (delta:297-313, packet:69-83).

**3. Is the authority claim right?** Pass [Observed].
- RFC5-17 (`consent-egress-secrets.md:306`) defines "`redacted-span`
  (artifact retained, matching spans replaced by markers with a count)". The
  retention rule is at :318-319, and :322 says "Mapping the whole artifact to
  a blanket Unknown would over-degrade usable …".
- REQ-polaris-generation-025 (`polaris-manifesto-generation/…/spec.md:1400`)
  says: "redacted-span SHALL retain permitted surviving evidence at its
  otherwise-earned tier with disclosed count, making only claims dependent on
  removed spans Unknown. Redaction branches SHALL remain limited to those the
  adopted policy permits." The scenario "Partial redaction retains usable
  support" is at :1424.
- I found no clause in RFC5-14/16/17 or REQ-025/035 that requires
  whole-artifact exclusion for this scope.
- REQ-polaris-generation-035 (`polaris-dossier-local-agent-mode/…/spec.md:320`)
  says "screening-admitted only". The policy's `citedSpanRule` makes a span
  with no withheld line "screening-admitted content of the body's class" and
  re-screens it, so such a span qualifies [Inferred].

**4. Is the scope bounded?** Pass [Observed, jdiff and builder predicates].
- Only `publicSourceScope` and the shared `policyVersion` move.
  `redactedClasses` is `["project-documentation"]`.
- `appliesTo` keeps agent-written text screened whole, and `unchanged` keeps
  the active-content scan whole-body.
- `activeContent`, `accessBoundary`, `rawBodyHandling`, `sourceAdmission`,
  `prerequisite`, the detectors and every other classification rule are
  unchanged (predicates hold).
- The base scope is untouched. The Butlers gate pin effect is stated
  (ledger:23-34; packet:111-115).

**5. Variant `span-guides`.** Pass.
- The 23 stems and the 3 suffixes are byte-unchanged since round 3. The
  builder diff `05e76464..HEAD` touches neither.
- None is in `rootStems`, `FORBIDDEN_GUIDE_STEMS` or `docExcludedTokens`, and
  the suffixes are disjoint from the 25 `sourceExtensions` (predicates hold).
- `INSTALL` and `BUILD` stay unmapped (fixtures).
- The declines match their sources (SEMANTIC-DELTA.md:287-291). The delta
  (:50, :57) and the packet (:60-61) say the list recovers none of the 89
  spans. The bead's figures (140 of 233, 41 README, 89 unclassified, 10
  active content) match `bd show syzygy-olmr` lines 11-24.

**6. Option C's decline.** Pass [Observed].
- VIS-2, `.syzygy/governance/doctrine/vision.md:133`: "Nothing turns green,
  and no project is declared aligned, converged, or genome-complete (defined
  in architecture.md), without current evidence". The delta's ellipsis drops
  only the parenthesis.
- REQ-035: "draft-to-source support for every claim block" (spec.md:320) and
  "the rule that unresolved material omissions prevent readiness"
  (spec.md:328).

**7. Is the install requirement complete?** Pass, with Note 5 [Observed].
Sweeps at `65edb1cb` with `git grep -lF` over `packages apps scripts .github`:
- version literal `1.4.0-public-source-candidate.1.none.code-all`: 8 files,
  the population ledger:9-11 names;
- policy path: 30 files, as ledger:12 states. All 18 non-test files are named
  across ledger:18-66, as round 3 checked; this round left the ledger
  unchanged;
- `screenBody(` / `detectSecrets(` / `readBlobs(` outside
  `*.test.ts`/`*.testkit.ts`: 11 files, the same population as round 3.
  Three of them the ledger does not name, each [Inferred] outside the change:
  - `packages/polaris-dossier/src/git-object-reader.ts:93`, an interface
    declaration;
  - `apps/three-surface-poc/src/polaris-generation/self-corpus.ts:54`, which
    reads Syzygy's own repository and not a public-source target;
  - `apps/three-surface-poc/src/verbatim-route.ts:120`, the Butlers base
    scope, which is unchanged.

The act readers, version pins, recorder battery lines, CG-7e, match offsets
with their cost, the two screens, class gating and the call sites
(`review.ts`, `check.ts`, `repo-corpus.ts`, `render.ts:204/280/383`,
`close.ts:124`) are all present.

**8. Is the owner packet plain and single-question?** Pass [Observed].
- There is one binding ask: "Sign screening scope version 4? Pick a variant,
  or decline." (:41).
- Three choices, and words that name a manifest row by variant: "Sign
  screening scope version 4, variant span-guides" (:49-51).
- A recommendation with reasons (:53-65), and a cost section (:67-86) that
  names the six shapes, `AKIA…`/`ASIA…`, non-http connection strings, and
  config-shaped documentation-path files.
- The key-block assurance (:29-32) matches the bytes.
- Notes: Findings 2 and 3.

**9. Authority hygiene.** Pass [Observed].
- `r4/hygiene.py` swept the 10 package `.md` files with Python `re` for
  `\b(accepted|approved|adopted|in force|ratified|signed)\b`,
  case-insensitive. It found 4 hits: REVIEW-BRIEF.md:70 ×2 (the criterion
  itself), SEMANTIC-DELTA.md:73 (quoting "the adopted policy" from REQ-025)
  and SEMANTIC-DELTA.md:287 ("its Q3, accepted", which states the version-2
  act). None labels this package.
  `ROUND-3-OWNER-DIRECTION.md` says it "approves no policy and signs nothing".
- 64-hex: Python `(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])` and
  `[0-9a-fA-F]{40,}` give 0 and 0 in each of the 10 files. A second method,
  `grep -rcE "[0-9a-fA-F]{64}" --include=*.md`, gives 0 in each of the 10.
  The builder's `--check` predicate agrees.
- `python3 scripts/check_governance.py` reported "32 OK, 21 WARN, 0 FAIL (53
  checks)".
