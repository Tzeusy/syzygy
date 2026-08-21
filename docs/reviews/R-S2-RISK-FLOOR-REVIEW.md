<!--
RETAINED EVIDENCE — raw independent review output, stored verbatim.
Slice: S2 (consent and coverage), bead syzygy-6yi. Risk-floor class per
docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md ("credential admission and
consent enforcement … Independent review required").
Reviewer: fresh-context agent R-S2-review, 2026-08-21 (session clock
2026-08-20T17:55Z); subject was the UNCOMMITTED working tree after
S1 commit 766782b. Everything between the markers is the reviewer's
output byte-for-byte; nothing below the end marker edits it.
-->

<!-- BEGIN RAW REVIEW OUTPUT (verbatim) -->
# R-S2 — Independent risk-floor review of the S2 slice (fresh context)
Reviewed: `packages/cap1-core/src/consent.ts`, `coverage.ts`, `admission.ts`, `index.ts` (diff), `identity.ts`, `vocabulary.ts`, `declaration.ts` (validation paths); `packages/cap1-conformance/src/req-010…016.conformance.test.ts`; spec CAP1-REQ-010…016 (full SHALL/oracle/falsifier text); RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-30, RFC5-3, RFC6-26, RFC2-23 degradation table (rendering-vocabularies.md); SEC-4. Commands: `npm run typecheck` (clean), `npm test` (14 files, 80 tests, all pass).

## Findings

### Blockers (max 5)
1. **[Inferred] Conflicting per-pair consent records resolve open: an in-force record beats a withdrawn record regardless of order — observation can survive withdrawal.** `resolveConsent` (consent.ts:59-74) filters the pair's records and returns consented if *any* in-force record exists; withdrawn is checked only afterward. The governing contract fixes the record model as append-only: RFC2-23's *Consent withdrawn* row says "prior records remain (immutable) but render with the withdrawal visible." Under that model, grant-then-withdraw presents *both* an immutable in-force grant record and a withdrawal — and this layer serves the pair as consented, i.e. a withdrawn source keeps being observed. The code comment defines precedence only for "several in-force records"; the in-force-vs-withdrawn conflict is silently decided in favor of access. No input invariant rejects a conflicting per-pair record set, and no conformance test pins the case (req-011's fixture has withdrawn-XOR-in-force per pair — the suite passes against this fail-open semantics). Fix direction: fail closed on per-pair conflict (render unconsented with a distinguishable basis), or state and *enforce* a caller contract of one current-state record per pair — plus a falsifier test either way.

### Non-blocking (max 5)
1. **[Observed] The declaration's consent reference is never consulted.** RFC3-6 phrases observability as "an entry whose *consent reference* does not resolve to an in-force consent record is not observed"; `computeCoverage` ignores `entry.consent` entirely and pair-matches the whole record set. A dangling or withdrawn declared reference is never surfaced (reason #11 `reference-unresolvable` is unreachable from this layer), and consent can resolve through a record the declaration never referenced. Not an unconsented path (the resolving record is still in-force for the exact pair), but a contract divergence and a lost diagnostic.
2. **[Observed] `admitClient` admits any non-empty string, including a whitespace-only token** (admission.ts:34). The stub is disclosed and the polarity (refuse on absence; refused arm typed `served: 'nothing'` with no boundary field reachable) is right; suggest a test pinning the admissibility bar as a daemon-slice obligation so it cannot weaken silently.
3. **[Observed] Asymmetric guard in `authorizeObservation`:** it re-checks the requested *repository* against the record but takes no requested *project* id, though `record.projectId` is available to check. A caller reusing project A's resolution while serving project B is not caught at this layer. Adding `requestedProjectId` would make cross-project confusion structurally impossible here, matching the repository-side check.
4. **[Observed] REQ-011's "scope, attribution, and grant state render with the coverage boundary" is satisfied only for `observed`/`degraded-partial`:** a consented-but-`capture-failed`/`stale` repository's in-force record is not cited, and a withdrawn pair renders `basis: 'withdrawn'` without citing the withdrawal record (RFC2-23: "render with the withdrawal visible"). Passes the requirement's bounded oracle; completeness gap for the rendering slices.
5. **[Observed] Observer-failure and source-unreachable both funnel to the `'unreachable'` input → reason #10**, with degrade-to-last-good deferred to the daemon slice. The deferral is *stated* (coverage.ts:34-37; req-013 mapping note) rather than silently claimed — honest; recorded so the daemon slice's ledger picks it up alongside req-015's explicitly open dual-channel and two-location limbs.

On the review questions otherwise: default-open, cross-project bleed, and empty-credential admission each have real falsifier tests hard-coding expected spellings literally (oracle independence held — req-012 deliberately does not import the vocabulary module); every declared repository gets an explicit result with the declaration's own count as denominator; location cannot reach admission by construction (no parameter, and the arity/shape tests would trip an added one); partial never reaches `observed` by type construction.

VERDICT: REVISE
<!-- END RAW REVIEW OUTPUT -->

<!--
DISPOSITION: the blocker was repaired by a separate worker (W-S2-repair,
2026-08-21): withdrawal-defeats-grant fail-closed semantics in
resolveConsent + falsifier tests in both record orders; reviewer
non-blocking #3 (requestedProjectId re-check in authorizeObservation)
repaired in the same pass. Non-blocking #1/#2/#4/#5 filed as bead
syzygy-ydr, untouched. The same reviewer then ran the targeted
confirming pass below (R-S2b, 2026-08-21); its raw output follows
verbatim between the markers.
-->

<!-- BEGIN RAW CONFIRMING REVIEW OUTPUT (verbatim) -->
# R-S2b — Targeted confirming review of the S2 blocker repair
Reviewed: re-read `packages/cap1-core/src/consent.ts` (resolveConsent, full) and `admission.ts` (authorizeObservation, full); the new conflict describe-block in `req-011.conformance.test.ts` (lines 168–272) and the updated/new authorization tests in `req-016.conformance.test.ts`; ran `npm run typecheck` (clean) and `npm test` (14 files, 84 tests, all pass — read the output myself).

Assessment:
- **Blocker 1 is closed.** `resolveConsent` now checks withdrawal before in-force: any withdrawn record for the exact (project, repository) pair returns `consented: false, basis: 'withdrawn'` before the in-force lookup runs, so the conflict can never be decided by list order or in favor of access. The comment states the correct rationale (RFC2-23 append-only record model, no ordering in the record shape, therefore fail closed) and explicitly routes regrant-after-withdrawal onward as an unsolved supersession question rather than guessing — a fail-closed deferral, honestly stated. The new falsifier tests pin exactly the dangerous case I named: one pair holding both records, exercised in BOTH list orders, at both the resolveConsent layer (basis `'withdrawn'`) and the computeCoverage layer (`'unconsented'`, reason hard-coded as the literal `'unconsented-source-or-provider'`, no `capturedScope`, serialized entry checked to not contain the captured content). I verified the mutation claim by reasoning through the reverted logic: restoring any-in-force-wins flips all three conflict tests (both resolveConsent orders + the coverage render), so the suite genuinely catches the fail-open direction now.
- **Non-blocking #3 also repaired.** `authorizeObservation` takes `requestedProjectId` and checks it against `record.projectId` symmetrically with the repository check; mismatch refuses with `'consent-not-for-this-project'`, still rendering `'unconsented-policy-state'`. req-016's new falsifier presents a genuine project-A resolution under project B's identity and asserts refusal; disabling the comparison would fail exactly that test.
- **No new defect introduced.** The withdrawal-first change only widens refusal (strictly fail-closed); it cannot open any previously refused path. It is spec-compatible: REQ-011's SHALL is one-directional (no access without a resolvable in-force record) — refusing a pair that also holds a withdrawal record refuses more, never less, and matches RFC2-23's withdrawal-visible rendering (`basis: 'withdrawn'` survives into the coverage entry). The req-011 sweep fixture holds no conflicted pair, so its observed⇔in-force join is untouched. `admitClient` and the location-independence construction are unchanged (still a single credential parameter). computeCoverage unchanged; the conflicted pair flows through the existing unconsented arm. Typecheck clean; the only remaining working-tree diff against committed state beyond the S2 files is the index.ts re-exports, as before.
- Remaining non-blocking items from R-S2 (#1, #2, #4, #5) stand as noted — none were in scope for this repair and none were weakened by it.

VERDICT: CONFIRM
<!-- END RAW CONFIRMING REVIEW OUTPUT -->

