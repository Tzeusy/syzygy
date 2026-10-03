# R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-3 — independent review of the Messages API provider route entry, round 3
Reviewed commit: 3656a1032dc7e2dc189d828f092619644e58f422
Manifest SHA-256: effc41e935e928d9d2109316672ff6ec75318d32d27728fc57950b7e9a86b466
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context independent reviewer (Claude Opus 5.5), 2026-10-03.
Read-only detached worktree at the reviewed commit; nothing tracked was
modified, no model provider was called, no external repository body was read,
and no capture was run (see "Capture" below). `ENTRY` means
`proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json` in the
package directory; line numbers are at the reviewed commit.

## What was read and run

- **Package.** Every file of the package, including both raws and both
  dispositions, and `git diff eafb02ee 3656a103` over the package and
  `scripts/build_provider_route_messages_api_entry.py` (one commit,
  `3656a103`, between round 2's reviewed commit and this one).
- **Digests (`sha256sum`).** Manifest file `effc41e9…`, equal to
  `--manifest-digest` and the head above. The proposed JSON hashes to
  `b70b16eb…`, equal to the manifest's one row.
- **Builder and governance check.**
  - `--check`: "messages-api provider route entry: current", exit 0.
  - `--selftest`: "selftest: 208 of 208 predicates held", exit 0.
  - `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- **PR #264 source at the pinned commit `e76b6929`.** `git rev-parse
  <commit>:<path>` for the three provenance files gives `fa8cdceb…`,
  `bb7f222f…`, `99d79e9d…`, equal to ENTRY 333, 337, 341. Read the guard,
  constructor and header predicate of `messages-api-provider.ts` (lines 83-115,
  212-231) and the upstream handling of `egress-gate.ts` (lines 10-15, 63-111).
  `git merge-base --is-ancestor c2305b19 e76b6929`: true.
- **PR #264 today.** `gh pr view 264`: head `209ee68d…`, OPEN. `e76b6929` is
  not an ancestor of it (`merge-base --is-ancestor` false) and is contained in
  no remote branch (`git branch -r --contains` empty); the PR timeline shows
  force-pushes at 08:44:58Z, 09:05:10Z and 10:04:05Z. GitHub still serves
  `e76b6929` by SHA (`gh api repos/…/commits/e76b6929…`). All three
  provenance blobs are identical at `209ee68d`.
- **Bead.** `bd show syzygy-yqtg`: OPEN, P1, "Egress gate/adapter: pin
  x-stainless-timeout=600, upstream https://api.anthropic.com, refuse Node
  TLS/proxy env (route B)", description items (1) timeout value, (2) upstream
  https only, (3) refuse NODE_TLS_REJECT_UNAUTHORIZED, NODE_EXTRA_CA_CERTS,
  NODE_USE_ENV_PROXY/HTTPS_PROXY/HTTP_PROXY; owned by lane-v.
- **Impact ledger.** Re-run at the reviewed commit (2,001 tracked files) and
  Sweep 2 at `b97b77ed`.
- **Package sweeps (Python `re`).** 64-hex tokens and
  accepted/adopted/approved/signed-off words over every `*.md` in the package.
- **My rule-6 run.** `r3-rule6.py` in the reviewer's scratch, importing the
  builder and calling `findings_for` on mutated copies of the entry; nothing
  tracked touched. Results under Findings 5 and 7.
- **Capture.** Not re-run. `git diff eafb02ee 3656a103` changes nothing in
  `requestBytes` except the `provenance.label` prose (ENTRY 328), so round 2's
  loopback capture (20 headers, 0 outside `closedSet`, 0 listed not captured,
  0 literal or shape mismatches) still covers the same header table and body
  description byte for byte.

## Round-2 findings re-checked against the bytes

- **F1 (blocking) — holds.** ENTRY 236 now reads "[Unknown] the connection
  header value: the cited predicate checks its name only (the
  x-stainless-timeout value is not Unknown: it is the literal 600, see
  headers.timeoutNote)". No other byte calls the timeout value Unknown: the
  only remaining value-Unknown is `valueRules.connection` (ENTRY 399), and
  `connection` is in no `pinnedLiterals` key (ENTRY 376-387). The builder
  predicate (build script 358-363) holds on the bytes and kills the round-2
  wording (my M1). It is narrower than its message claims (Finding 5).
- **N1 — holds.** ENTRY 14 names `e76b6929…`, equal to
  `provenance.commit` (ENTRY 329); predicate at build script 364-366 with a
  mutant. But the repair dropped "at drafting", and the sentence is now false
  of PR #264 (Finding 1).
- **N2/N4 — hold.** ENTRY 138 and SEMANTIC-DELTA.md now cite bead
  `syzygy-yqtg` with "[Inferred: from the bead record…]". The bead exists and
  its items (1)-(3) cover the upstream pin, the timeout value and the Node
  variables. ENTRY 177 calls the guard [Observed] at the pinned commit and
  names `c2305b19`, which is an ancestor of `e76b6929`; the source confirms
  the guard (provider.ts:86-87, called at 94 and 108). The only remaining
  [Inferred] there is "that a later implementation keeps the guard", which is
  honest. ROUND-2-DISPOSITIONS.md's corrections (a) and (b) to the round-1
  record are accurate.
- **N3 — holds.** ENTRY 328 now excepts `x-stainless-timeout: 600` and
  attributes it to the SDK source and round-1 capture. Confirmed against
  provider.ts:212-217: `LITERALS` lacks it and `OPTIONAL_SHAPES` names it.
- **N5 — holds.** OWNER-DECISION-PACKET.md names rounds 1 and 2 (REVISE) and
  points to each raw's `Verdict:` line.
- **N6 — holds.** ENTRY 206 carries "while ANTHROPIC_LOG is unset
  (retentionCondition)"; ENTRY 194, 214 and 163 agree. Predicate at build
  script 367-369 with a mutant.
- **N7 — holds.** ENTRY 250 places the ANTHROPIC_ clause in the list of causes.
- **N8 — holds.** RFC4-9 is in SEMANTIC-DELTA.md's cited IDs and in
  REVIEW-BRIEF.md's governing references.
- **N9 — holds, honestly labelled.** `nodeTransportEnvironmentInputs`
  (ENTRY 180-189) lists four rows with "must be unset" and labels both the
  behaviour and the enforcement [Inferred]. Against `e76b6929`:
  provider.ts:87 refuses only the `ANTHROPIC_` prefix and no `NODE_`/`PROXY`
  name appears in either file, so "the adapter does not refuse these at the
  pinned commit" is true. The list is not closed (Finding 3).
- **N10 — holds with residuals.** Items (a)-(e) each have predicates and
  mutants. The selftest growth 190 → 208 is exactly the 18 additions in the
  diff: mutants for timeout-Unknown (1), implementationStatus (1), retention
  (1), constructor drops authToken (1), constructor names logLevel (1), four
  Node variables dropped (4), loosened posture (1), unlabelled enforcement
  (1), three fit wordings (3), plus four pure `ctor_keys` cases (4) = 18. The
  source constructor check compares key names only (Finding 7).

## Enforcement labels against the cited code

- Upstream rule (ENTRY 138): "[Observed] the gate at the cited commit accepts
  any upstream URL including plain http". True: egress-gate.ts:87-93 takes
  `options.upstream.url` and picks `https` or `http` by its protocol, with no
  host or scheme check. Labelled as the entry's statement, pending
  `syzygy-yqtg`. Honest.
- Timeout literal (ENTRY 425): "The cited predicate treats the name as optional
  and checks no value". True: provider.ts:217, 229. Honest; the entry does not
  cite the bead here (Finding 2).
- Ambient guard (ENTRY 123, 177, 194): [Observed]. True at `e76b6929`.
- Node variables (ENTRY 188): [Inferred], not refused at the pinned commit.
  True.
- Constructor (ENTRY 176): provider.ts:115 passes `apiKey`, `authToken: null`,
  `baseURL: gate.url`, `defaultHeaders: {}`, `maxRetries: 0`, equal to the
  entry by key and value.

## Acceptance criteria

1. **Seven RFC4-2 declarations — yes.** Unchanged from round 2 apart from the
   new `nodeTransportEnvironmentInputs` block, which is an addition to item 3's
   input preconditions and item 7's boundary; no default left silent.
2. **Substitute and nothing more — yes.** `observerId` shared, new
   `implementationId`, `routeSubstitution` unchanged; the packet adds one line
   on the inherited role name and asks for exactly one entry.
3. **`requestBytes` equals what the route sends — yes.** Unchanged since
   round 2's capture (see "Capture").
4. **Egress fit honest — yes.** Three wordings in `needsReading` (ENTRY
   209-211), count word "three" in the conclusion (213), retention now
   conditional everywhere.
5. **Credential honest — yes.** ENTRY 123 labels the variable name a proposal;
   nothing in the cited source logs or persists the key.
6. **Runtime gate matches source — yes.** See "Enforcement labels".
7. **Profile pins — yes.** ENTRY 367-371, unchanged.
8. **Write surface — yes.** ENTRY 109-113, unchanged.
9. **Null version, unknowns, failure vocabularies — yes.** F1 repaired; states
   and reasons within RFC2-23/RFC2-24.
10. **Impact ledger — yes.** At the reviewed commit (2,001 files): Sweep 1
    gives 8 and 23 files (the ledger's "23 with this package's builder").
    Sweep 2 gives 2 lines, 0 lines, 1 file; the file is this package's
    builder, as in round 2. At `b97b77ed`: 0, 0, 0, as the ledger states.
11. **Round-1 repairs hold; did any introduce a defect?** Round-1 and round-2
    repairs hold as above; the round-2 repair introduced one false present
    statement (Finding 1).
12. **Provenance pair — yes.** One commit, three blobs, each re-derived;
    identical at PR #264's current head too.
13. **No authority claimed — yes.** 0 64-hex tokens in the four root `*.md`
    files and both dispositions (1 in each raw, its own head line). Authority
    words in packet, delta and ledger are all conditional or name other
    artefacts (IMPACT-LEDGER.md:36, SEMANTIC-DELTA.md:44-45, 96,
    OWNER-DECISION-PACKET.md:25, 81). Uncovered claims are in Finding 7.

## Findings

**Finding 1 — `implementationStatus` now calls `e76b6929` PR #264's head, which it was not when the repair was committed** (note)

ENTRY 14: "(PR #264, stacked on PR #258, head
e76b692926d89342e7943ce0a2d7ef669a859b47, the commit this entry pins as
provenance)". The round-2 repair removed "at drafting" (diff of ENTRY 14,
eafb02ee → 3656a103). PR #264 was force-pushed to `209ee68d` at 10:04:05Z
(18:04 +08:00); the repair commit `3656a103` is dated 19:01 +08:00. So the
present-tense "head" was false when written. `e76b6929` is now contained in no
remote branch, though GitHub still serves it by SHA, and all three pinned blobs
are byte-identical at `209ee68d`, so no `[Observed]` claim about the source is
affected. Violates AGENTS.md epistemic discipline (a stale fact stated in the
present) and, weakly, rule 11's re-checkability (a fresh clone cannot fetch
`e76b6929` from any branch; the builder's source check then silently skips,
build script 377-383). Repair while the bytes are still open: either restore
"at drafting", or re-pin `provenance.commit` and the status to `209ee68d`
(blobs unchanged; the builder's status predicate then holds). Not blocking:
the blobs bind the bytes, and the entry already calls the source
"provenance only".

**Finding 2 — the timeout-value enforcement is the one `syzygy-yqtg` item the entry does not cite** (note)

ROUND-2-DISPOSITIONS.md (Notes 2 and 4) says "The upstream pin, the
timeout-value enforcement and the Node transport variables are tracked as bead
syzygy-yqtg (lane-v), labelled [Inferred: from the bead record…]". The entry
cites the bead at ENTRY 138 (upstream) and 188 (Node), but `timeoutNote`
(ENTRY 425) says only "an implementation must enforce the literal before the
entry is usable". Not a contradiction — the bead's item (1) does cover it —
but the disposition describes the entry more fully than its bytes do.

**Finding 3 — the Node transport list is not closed, and nothing says so** (note)

[Inferred, from Node's documentation; not exercised] Further environment
inputs reach the same forwarded TLS request: `NODE_OPTIONS` (which can carry
`--use-env-proxy`, `--use-openssl-ca` — after which `SSL_CERT_FILE` /
`SSL_CERT_DIR` apply — or a `--require` preload), and the lower-case
`https_proxy` / `http_proxy` forms. ENTRY 181 does not claim completeness, so
nothing false is bound; but unlike `sdkEnvironmentInputs` (ENTRY 171, "any
other ANTHROPIC_-prefixed variable") it has no catch-all row. Candidate for
`syzygy-yqtg`'s refusal list or a closing row; it does not need to block.

**Finding 4 — REVIEW-BRIEF.md's Recording section still names the round-2 raw** (note)

REVIEW-BRIEF.md:106-108 tells the reviewer to store the raw "as
`R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-2-RAW.md` (round 1 is the `-1-RAW.md`
beside it…)" while the head (line 1, 4-7) says round 3. Followed literally it
would overwrite the round-2 raw, contrary to CC-REV-6 and the same sentence's
"never overwritten". This raw uses `-3-RAW.md` per the lead's instruction. The
brief is not act-bound.

**Finding 5 — the F1 predicate catches the round-2 wording but not equivalent reintroductions** (note)

Build script 358-363 checks only text before the first "(" of each `unknowns`
item, and requires the literal word "value". My rule-6 run (`findings_for`
over mutated copies; baseline 0 findings):
- M1, ENTRY 236 restored to the round-2 text "[Unknown] the
  x-stainless-timeout and connection values: …": **killed** ("unknowns marks
  the value of pinned header x-stainless-timeout Unknown").
- M2, "[Unknown] the connection header value (and the x-stainless-timeout
  value): …": **survived** (the split at "(" hides it).
- M3, "[Unknown] what x-stainless-timeout carries: …": **survived** (no
  "value").

The parenthesis exclusion exists so the current item's own disclaimer passes;
a predicate keyed on "[Unknown]" scope rather than on the first "(" would not
need it. The bytes under review are correct, so this is a coverage note for
CC-SPEC/rule 6, not a defect in the entry.

**Finding 6 — PR #264's adapter has moved on; the entry's `[Observed]` claims stay pinned to `e76b6929`** (note)

`209ee68d` adds commits including "ambient-env guard, version pin, stop-reason
and billing-evidence rules" and a rule-6 record "18 mutants, 16 killed, 2
survivors named". The three provenance blobs are unchanged, so nothing in the
entry is contradicted; recorded only so the offering step re-pins knowingly.

**Finding 7 — residual uncovered claims after the 208-predicate selftest** (note)

- The source constructor check (`ctor_keys`, build script 116-132, 377-383)
  compares key names only. Mutant M5 (mine): `maxRetries: 0` → `maxRetries: 2`
  and `authToken: null` → `authToken: process.env.X ?? null` in the real
  `e76b6929` source: keys unchanged, **survived**. The entry claims the values
  (ENTRY 176); round 2's P-A checked values. The entry is correct at the
  pinned commit (provider.ts:115); only the guard is weaker than the
  disposition's "constructorArguments against the adapter source".
- `NODE_ENV` (build script 139) holds `HTTPS_PROXY` only, matched by
  substring, so mutant M4 (renaming the row "HTTPS_PROXY", dropping
  `HTTP_PROXY`): **survived**.
- The source check silently skips when the pinned commit is absent locally
  (build script 377-383), which after the force-push (Finding 1) is the fresh-
  clone case.

## Verdict

CONFIRM WITH EXCEPTIONS. The round-2 blocking finding is repaired: the entry
no longer calls the `x-stainless-timeout` value Unknown, nothing else
contradicts a pinned literal, and a predicate kills the round-2 wording. Notes
1-10 of round 2 are each repaired or declared as the dispositions say, the
bead `syzygy-yqtg` exists and covers every enforcement point the entry cites
it for, every [Observed]/[Inferred]/pending label matches PR #264 at
`e76b6929`, and the selftest's 190 → 208 growth is exactly the 18 additions.
All seven findings above are notes. Finding 1 (a present-tense "head" that was
already false when the repair was committed) is the one I would fold in before
an act binds these bytes, since a bound false sentence can be corrected only
by a successor; it does not affect any byte-level claim. Any edit retires this
review (rule 10).
