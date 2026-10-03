# R-PUBLIC-ADMISSION-REGISTRY-ENTRIES — fresh-context review, round 4
Reviewed commit: d08f4400cd20a9babc38e30b5fa6197b696e96e2
Manifest SHA-256: ede7266bdaf9a01fefae9dbb95993998ae63eb91e03f1f606d92c1ffca873d35
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context agent session, 2026-10-03. Read-only detached
worktree at the reviewed commit. The manifest digest above was printed by
`python3 scripts/build_public_admission_registry_entries.py --manifest-digest`
and equals `sha256sum` of the manifest file; both manifest rows equal
`sha256sum` of the two `proposed/` files. The provenance files were read as
git objects from the local clone (`git rev-parse`, `git cat-file -p`). The
egress record and the admission packet were read from
`origin/polaris/public-repo-admission` at
`8bcec86000234e7c07f90050c476619ae0fe658b`; no merged path for
`EGRESS-CONSENT-ANTHROPIC.md` exists at the reviewed commit. Every finding
below is a note; severities used: note only.

## Checks run

- `build_public_admission_registry_entries.py --check`: "public-admission
  registry entries: current", exit 0. `--selftest`: "selftest: 102 of 102
  predicates held", exit 0.
- `scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- Provenance, each pair re-derived with `git rev-parse
  3444c33f0cbf135ec0684d6394ddd59bbfdcfc0e:<path>`:
  `docs/polaris-generation/PROVIDER-EGRESS-BYTES.md` →
  `2e7d176e668417bf9842be8b11703f5fe2cc39ca`;
  `packages/polaris-generation-provider/src/request-acceptance.ts` →
  `87b30864de8d79fa8b69f2be2ca94d8c22f94a3d`;
  `packages/polaris-generation-provider/src/egress-gate.ts` →
  `3704e4036479cb5edd7f63700380e645370a3c59`. All three equal the entry's
  rows (provider json:220-233). The commit is on `agent/dossier-provider`
  (`3444c33f` follows `1e94713a` and `420c60f9`).
- Header table versus `request-acceptance.ts` at that commit
  (`headerValueProblems`, lines 71-93; `ALLOWED_HEADERS`, lines 61-66):
  12 literals, all equal byte for byte to `pinnedLiterals` (json:262-275),
  `anthropic-beta` equal to `AGENT_SDK_BETA_OFF` (line 44); 4 shapes equal
  (`x-stainless-os`, `-arch`, `-runtime-version`, `accept-encoding`, line
  83-84); `closedSet` (json:289-311) equal to `ALLOWED_HEADERS` as a set of
  21 names; `x-api-key`, `x-claude-code-session-id`, `content-length` and
  the capture-side `host` pattern agree with lines 84-91. Differences in
  Finding 3.
- Sweeps at the reviewed commit: `git grep -l -F adapter-registry -- apps
  packages` 8 files, `-- apps packages scripts` 23 files (ledger
  `IMPACT-LEDGER.md:10-11`); provider-SDK import regex
  `@anthropic-ai|claude-agent-sdk|claude_agent_sdk|import anthropic|from anthropic`
  over `apps packages scripts` 0 files.
- Criterion 10, standalone 64-hex tokens (Python `re`): the four Markdown
  files 0 each; manifest 2 (its rows); each proposed JSON 1 (copied
  `contractVersion`). Authority words outside `reviews/`: the brief's
  criterion text, both JSONs' "the adopted Butlers observer entry" (json:17),
  "the adapter is accepted only when" (provider json:124), the packet's
  "changes no adopted specification" (`OWNER-DECISION-PACKET.md:91`). None
  labels anything in this package accepted, adopted, approved or signed off.
- Builder blind spots, by in-memory mutation of `findings_for` input (no
  file written): see Finding 5.

## Round-3 findings, one by one

| R3 | Disposition at the reviewed commit |
|---|---|
| 1 (revise) | Resolved. `requestBytes.headers` (json:261-314) now carries `pinnedLiterals`, `shapes`, `valueRules` and a 21-name `closedSet`, and `unlisted` says "there is no open class of transport headers" (json:312). The `anthropic-beta` literal is the thinking-off value. The builder compares the table for exact equality with its copy (builder:60-115, 231-232) and mutants cover a changed value, an added name, the open class returning and a widened beta (builder:366-369). Residuals: Finding 3 |
| 2 (revise) | Resolved. One commit and three (path, blob) pairs, each verified above; the builder re-checks them via `git rev-parse` when the commit is present (builder:138-150) and pins the pairs as constants (builder:116-121, 233-235). The `thinking` text (json:257) matches blob `2e7d176e` lines 43-53 (`off`: body adds nothing, beta adds nothing). One sentence about the cited gate is not true of the cited blob: Finding 1 |
| 3 (note) | Resolved. `readAuthority` (json:104) now splits "[Observed in the cited measurement ...] the runtime adds ..." from "[Inferred] this entry additionally pins the model, effort, max_tokens ceiling, tools and thinking ... not observed in that form". `routeFixedByThisEntry.note` (json:259) is [Inferred] |
| 4 (note) | Resolved as an open owner choice. json:259 now says whether "fixed by the runtime" admits the pins "is a reading that a further egress record version must settle (packet O4)"; O4 (`OWNER-DECISION-PACKET.md:84`) names `model`, `tools`, `max_tokens`, effort and thinking off as fields the further egress version must admit |
| 5 (note) | (a) Resolved: O4 says the entry "carries every one of those bytes inline" and cites `PROVIDER-EGRESS-BYTES.md` "as provenance, by commit and blob" (`OWNER-DECISION-PACKET.md:77-81`). (b) Resolved: `SEMANTIC-DELTA.md:5-6` reads "Rounds 1, 2 and 3 returned REVISE ...; this is the round-4 text". The same class recurs in the packet: Finding 2 |
| 6 (note) | Resolved for the named items: header table equality, model and effort by value (builder:122, 224-226), thinking (builder:227-228), ceiling (229-230), appended acceptance text (`ACCEPTANCE_END`, 135, 236-237), provenance pairs (233-235, 238). Remaining presence-only claims: Finding 5 |

Round-1 and round-2 repairs: round 3 disposed each; the round-4 diff
(`git diff 2ffebeb3 d08f4400` over this package) touches the provider JSON,
packet, delta, brief, manifest and builder only, and reopens none of them.
The round-2 F5 plan (pin the egress record by its manifest-row digest at the
offering) stands at json:119.

## Criteria

1. Seven RFC4-2 declarations: present in both entries (identity, versions,
   inputs, outputs, per-class determinism, failure states, authority
   boundary); unchanged from round 3 in the Git entry; the provider entry's
   additions are within `requestBytes`. Holds.
2. Provider entry versus egress record: tools, telemetry, state location and
   fallback match the record's Conditions
   (`EGRESS-CONSENT-ANTHROPIC.md:117-127`); the pinned model is narrower than
   "The model is recorded per run, not fixed here" (`:21`). The
   "adds no context of its own" / "nothing else" divergence is disclosed and
   routed to O4 (see the open-choices section). Holds as disclosed.
3. Write surface: unchanged and honest under RFC4-2 item 7. Holds.
4. Fetch versus observation consent: Git entry unchanged since round 3; exact
   `FETCH_FULL` equality. Holds.
5. Determinism: nothing labels generated prose Observed (json:97). Holds.
6. `implementationVersion: null` and `unknowns`: honest; SDK import sweep 0.
   Holds, with Finding 4 on the sign-in route.
7. Failure mappings: unchanged from round 3; all in RFC2-23/RFC2-24. Holds.
8. Signing path: unchanged; Scope A not used, [Inferred]
   (`OWNER-DECISION-PACKET.md:36`). Sound.
9. Impact ledger: 8 and 23 re-derived. Honest.
10. Authority: none claimed; `--check` and `--selftest` pass; uncovered
    claims named in Finding 5.
11. Resource limits: unchanged; labelled proposals with semantics. Holds.
12. Repairs: table above; no repair introduced a blocking or revise defect.
    One stale sentence remains (Finding 2).
13. Provider entry versus `PROVIDER-EGRESS-BYTES.md` at the pinned versions:
    body fields, runtime-fixed bytes, absent-by-construction list, endpoint,
    probe, header names and the [Unknown] items match blob `2e7d176e`; the
    header values match `request-acceptance.ts` at the same commit. One
    stated fact about the cited gate is false for the cited blob (Finding 1).

## Findings

**Finding 1 — "The cited gate has a stripFingerprint option": the cited gate blob has none** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:313`
("the cited gate has a stripFingerprint option, default off"), repeated in
`OWNER-DECISION-PACKET.md:80-83` ("The cited gate can also strip the three
machine-identifying headers ... that is off by default") and in the builder's
pinned copy (`scripts/build_public_admission_registry_entries.py:113`). The
cited gate is `egress-gate.ts` blob `3704e403…` at `3444c33f`; its
`EgressGateOptions` (lines 13-18) has only `upstream` and `permitted`, and
`git grep stripFingerprint 3444c33f` returns nothing. The option arrives in
the descendant commit `abc9d411` ("optional fingerprint strip in the gate"),
where `egress-gate.ts` is a different blob. The sentence is a factual claim
about a named (commit, blob) that the bytes do not support (AGENTS.md rule
11; criterion 13, "nothing the capture did not show stated as fact"). It
changes no boundary: the headers are in `closedSet` and stated as sent, and
the strip choice is presented as the owner's with "this entry assumes no
answer", so it is graded a note, consistent with round 3's grading of the
analogous label defect (R3 Finding 3). It should still be repaired before an
offering, because once a row is signed the sentence cannot be corrected
except by a successor: either say the option exists in a later commit of
the same branch (named), or drop the clause.

**Finding 2 — The packet's review sentence is stale** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/OWNER-DECISION-PACKET.md:97`:
"Round 1 returned REVISE and round 2 REVISE; the raws are retained under
`reviews/`." Round 3 also returned REVISE
(`reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-3-RAW.md:4`) and the delta and
brief already say so (`SEMANTIC-DELTA.md:5-6`, `REVIEW-BRIEF.md:5`). The
same class as R3 Finding 5(b), now in the packet. Criterion 12.

**Finding 3 — Three header-table rows differ from the cited predicate, and one is not closed** (note)
Provider json:242, 286-287 against `request-acceptance.ts` at `3444c33f`.
(a) `connection`: "set by the transport; no value beyond an HTTP connection
token" (json:287). The cited predicate checks no `connection` value at all
(lines 71-93), and "an HTTP connection token" is a token class, not a
literal, closed shape or computed equality; it is the one header whose value
the table leaves open. Low consequence (the gate deletes `connection` before
forwarding, `egress-gate.ts:80`, and the transport sets its own), but R3
Finding 1 asked for "a pinned literal, a closed shape or a value rule" and
this rule is open. (b) `host`: the second half of the rule ("the forwarded
request names the one upstream host the gate is configured with") is from
`egress-gate.ts:78-82`, not the predicate; the builder's comment says the
table is "Copied from the cited gate's request-acceptance.ts" (builder:58-59),
which is true of every row except this clause, the `connection` rule and the
`machineFingerprint` sentence. (c) `endpoint` (json:242) is `POST
/v1/messages?beta=true`; the cited predicate also accepts `/v1/messages`
without the query (line 100). The entry is the narrower and governs; the
later implementation must narrow to it. None widens the boundary the entry
binds; RFC4-2 item 7, criterion 13.

**Finding 4 — "Signed in with the owner's account" cannot pass the header closed set** (note)
`networkAccess` (json:109) says the route is "signed in with the owner's
account or key", and `unknowns[0]` (json:141) treats a subscription login as
an open question. The `closedSet` (json:289-311) carries `x-api-key` and no
`authorization` header, and at the cited commit the adapter requires
`auth.apiKey` (`agent-sdk-provider.ts:57, 133`). [Inferred] an account
(OAuth) sign-in would carry a bearer credential outside the closed set and
fail the acceptance check, so under these bytes only the key route can pass.
It fails closed, so no effect is widened; but the entry and O3
(`OWNER-DECISION-PACKET.md:64-70`) present the account route as a live
option that these bytes already exclude. Criterion 6.

**Finding 5 — Selftest residuals (criterion 10)** (note)
In-memory mutations of the provider entry that `findings_for` returns no
finding for: appending to `requestBytes.runtimeFixed` or `generatorBuilt`;
setting `bodyFields`, `endpoint`, `probe`, `routeConditions.egressGate` or
`routeConditions.ambientContext` to any other text; `thinking` set to "off,
or adaptive when the profile asks" (builder:227 is a prefix test);
`maxTokensCeiling` set to "640000" (builder:229 is a substring test);
prepending "Any request is accepted;" to `acceptanceCheck` (only the three
substrings and the end anchor are tested, builder:215, 236). The git
re-check (builder:138-150) returns no finding when the commit is absent, as
it is in a clone without the `agent/dossier-provider` objects, so `--check`
on such a clone checks the pairs only against the hard-coded constants;
both provenance mutants (builder:376-378) are caught by those constants, and
no mutant exercises `git_provenance_findings` (it does fail on a wrong blob
when called directly, verified). These are claims the selftest covers with
no mutant, named as the criterion asks.

## Open owner choices, not counted as blocking

Each is presented by the packet as open, and no byte an act would bind
assumes an answer that enables an effect (both rows enable nothing,
json:187):

- **Route A versus Route B** (admission packet "Route", lines 319-328 at
  `8bcec860`; this packet O4 last sentence, `OWNER-DECISION-PACKET.md:84-86`):
  the entry is Route A and says Route B replaces it under RFC4-1 (json:188).
  Note.
- **O4, accepting the runtime envelope and the pinned fields**: the entry
  and the egress record contradict on "adds no context of its own" /
  "nothing else" / "a field outside the table"; the entry says accepting it
  needs a further egress record version (json:121, 259). Note.
- **stripFingerprint**: the entry assumes no answer (json:313); the choice is
  a note. The misattribution of the option to the cited blob is Finding 1.
- **max_tokens ceiling** 64000: labelled "[Inferred proposal, an owner
  choice]" (json:258). Note.
- **effort** `high`: the entry's own pin, labelled [Inferred] and "never
  observed in these values" (json:259); the measurement's default is
  `medium` (blob `2e7d176e` line 28). Note.
- O1, O2, O3 unchanged from round 3. Notes.

No finding is blocking or revise. Findings 1 and 2 are cheap prose repairs
that would retire this review if made (rule 10); Finding 1 is the one worth
making before an offering, since signed bytes cannot later be corrected.
