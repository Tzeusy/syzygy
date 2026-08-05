# Rev10 review dispositions (lead synthesis; raw reports stored unchanged alongside)

Discipline: every finding fixed or explicitly owner-overruled; raw report
stored verbatim before synthesis; only fixes touching `rfcs/` invalidate
the act-1 manifest digest, and all such fixes are batched so the digest is
regenerated once, before the confirming review.

## 1. rev10-transaction (acceptance-transaction, directive §13.5) — EXCEPTIONS, 5 findings

| # | Finding | Disposition |
|---|---|---|
| E1 | RFC3-16(b) (render honestly) vs RFC3-16(c) final bullet (effect rule blocks) prescribe different implementer behavior for state-(1) artifacts; record §2 states only the human-governance half | **FIX (two halves).** Record §2: machine-side complement added (constraints bind at full strength; authorizations-for-effect fail the predicate until correlation, per RFC10-9's concrete treatment) — APPLIED. RFC3-16(b): one reconciling sentence stating the constraint/authorization split — **QUEUED for the rfcs/ fix batch** (invalidates manifest digest; lands before the confirming review). The reviewer's [Inferred] two-audience reading is confirmed as authoring intent; resolution is conservative (authorizations fail closed). The [Unknown] — whether the owner intends the effect rule to reach the foundational corpus itself at V0 — is answered by the split: corpus-as-constraint binds, corpus-derived authorizations wait for correlation; flagged in record §2 so acceptance is knowing |
| E2 | Act 3's bound artifact (topology bundle) absent from packet; step-2 not runnable from packet | **FIXED.** Bundle copied into packet at `topology/` (10 files; BUNDLE-MANIFEST digest re-verified `0d34d1b5…` after copy); §1 act-3 row updated to say so |
| E3 | Step 3 lands the manifest at `…/contracts/rfcs/`, breaking its own `rfcs/…`-prefixed entries — mandated post-copy `sha256sum -c` would fail on a correct install | **FIXED.** Step 3 rewritten: modules → `…/contracts/rfcs/`, manifest → `…/contracts/` (one level above), `-c` run from `…/contracts/` |
| E4 | Rev9 `ACCEPT FOUNDATIONAL RFCS` gate still live and executable (phrase carries no digest argument; rev9 record has no forward supersession marker) — both RFC gates concurrently offerable | **FIXED.** Retirement notice written into the rev9 record header (dated, unconditional at rev10 delivery, acts 2–4 preserved, decision-content authority retained); rev10 record §1 supersession paragraph rewritten to match; 00-README updated. Lead action on reviewer finding — retires an un-executed phrase, adopts nothing; surfaced to owner in the exit report |
| E5 | Act 3's `.syzygy/map/` home creation unstated (every other home-minting step is explicit) | **FIXED.** Step 3 now states act 3 creates `.syzygy/map/` (RFC3-18 surface-namespace home) at that step |

Non-exception risks acted on: §3 now distinguishes rfcs/-touching fixes
(digest churns) from record/report fixes (digest stable); §7 item 1 now
quotes RFC3-15's six-name closed validator so the q4 default's weight is
visible. RFC10-9-consistency and §6-provisional observations: no action
needed (by design, disclosed).

### Queued rfcs/ batch (apply after all six reviews are in; then regenerate manifest + §1 digest; then confirming review)

- **E1-RFC**: in `rfcs/RFC-0003/governance-homes-and-owner-acts.md`,
  RFC3-16(b) "Bootstrap correlation" paragraph, after "…not as verified.":
  add — "Rendering is the only effect this paragraph adds; what a
  state-(1) record *suffices for* splits by role (RFC3-16(c)): an artifact
  consumed as a **constraint** binds at full strength — refusing to apply
  a constraint over uncorrelated provenance would widen, not narrow —
  while an artifact consumed as an **authorization for an effect** (a
  consent, an autonomy envelope, a write-expanding policy) has not
  satisfied the RFC3-16(a) predicate on a state-(1) record alone, and
  *Effect when the predicate fails* governs that effect until the
  correlation act (RFC10-9 is the worked example)."

## 2. rev10-digestibility (human digestibility/context, directive §13.2) — EXCEPTIONS, 4 substantive + 4 nits

| # | Finding | Disposition |
|---|---|---|
| E1 | 75 refs from installed modules point at material act 1 doesn't install (68 history backlinks + 1 matrix-rows + 6 packet-report refs) | **FIX (three parts).** (a) Record step 3 now installs `history/` + `matrix-rows/` as declared **non-normative companion material** at `.syzygy/governance/contracts/` — backlink path arithmetic resolves post-install; explicitly outside the accepted digest set — APPLIED. (b) The 6 packet-report references in RFC-0010/0011 are reworded as bootstrap-provenance descriptions — **QUEUED (rfcs/ batch)**. (c) RFC-0003 README matrix-rows link survives via (a) |
| E2 | 05-CONTRACT-INDEX cannot reach doctrine/craft/topology; fixture doctrine selection was prose-judgment, not metadata | **FIXED.** `build_contract_index.py` now emits a deterministic `governance_sources` section (doctrine/craft/topology packet files with role, words, extracted VIS/SEC/CC rule IDs); regenerated, no drift, cross-process determinism verified (fixed a set-order tie bug in the process) |
| E3 | Stale word counts (06 map ×2, RFC-0009/0002/0008 READMEs) under "wc -w" claims | **QUEUED (post-batch regeneration).** All README count tables + the 06 module table are refreshed by script AFTER the rfcs/ batch lands (counts change again with the batch); refresh is scripted, never hand-transcribed |
| E4 | RFC-0001:81 [Observed] cite → REVIEW-01-KERNEL.md, unreachable from packet | **QUEUED (rfcs/ batch).** Re-point to `../history/RFC-0001-history.md` (verified: its line 38 carries the K-F1/K-F2 narrative) |
| E5 | 00-README preflight = stale rev9 snapshot without a marker | **FIXED** — "Historical snapshot" callout added pointing to current figures |
| E6 | 06 module arithmetic doesn't parse; mean overstated | **QUEUED (post-batch regeneration)** — enumeration rewritten as 21 package modules + 7 READMEs + 2 singles + 0010 + 0011; mean/median from final bytes |
| E7 | Autonomy register row missing a cell | **FIXED** — Environment/toolchain capsule row now has all four cells |
| E8 | Fixture 3 support sentence overstates README | **FIXED** — reworded to the accurate support |
| rec | `topic:` per clause in index | **RECORDED, not implemented** — deferred to the committed conformance tooling (09 report §tooling); zero exceptions rest on it |
| rec | "substrate" absent from index | **QUEUED (rfcs/ batch)** — add to RFC-0008 README front-matter tags |

## 3. rev10-boundary (RFC/OpenSpec boundary, directive §13.4) — EXCEPTIONS, 9

| # | Finding | Disposition |
|---|---|---|
| E1 | Phase rule can be absent from a lawful packet (fixture 1: no phase-rule text; RFC-0007 README lacks the restatement; index couldn't force it) | **FIX (three parts).** (a) "## Phase boundary" section for RFC-0007 README mirroring RFC-0008's — **QUEUED (rfcs/ batch)**. (b) Index now marks the six clauses `kind: phase-rule` — APPLIED; RFC11-4 gains "the mandatory set always includes the governing phase-rule clause of every selected contract" — **QUEUED (rfcs/ batch)**. (c) Fixture 1's why-nothing-lost updated after (a) lands — QUEUED |
| E2 | Tallies line garbled (rev9 per-RFC DI counts re-labelled as DI/OS/CR aggregate; 6× OS overstatement) | **FIXED** — replaced with a machine-recounted per-contract table; "no pure IR" reading restored |
| E3 | Rule section says "four RFCs"; routing sentence says 0007–0009 only | **FIXED** — six clauses named; scope re-stated as 0007–0011 |
| E4 | RFC10-16/RFC11-12 omit four rev9 limbs (incl. "matrix is review material, never authority"); "shape-parallel" overstated | **QUEUED (rfcs/ batch)** — restore (a)–(d) verbatim, keep the stricter N/A limb |
| E5 | RFC10-4/5/12 classed pure OS with unnamed retained DI limbs (10-12's is a safety invariant) | **FIXED** — all three now DI + OS with retained limbs named in the rationale |
| E6 | `DI + OS` undefined; skeleton "OS rows" pointer excluded 10 routed carried rows | **FIXED** — five-class table; 10 carried rows relabelled DI + OS (no substance change); skeleton sourcing now names every row explicitly |
| E7 | Non-exemption sentence covered DI but not CR | **FIXED** — "a DI or CR class never exempts" |
| E8 | MCP named without OD-R10-1's "(or equivalent)" hedge at RFC-0010:93/:259 | **QUEUED (rfcs/ batch)** |
| E9 | Open-question class counts transposed (6/7 not 7/6; V0 off by one) in triage/09/record | **FIXED** in all three files, with the enumeration written into the triage summary so it can't silently drift again |
| rec | Advisory disclaimer on 09 sequence; phase-rule line in record | **BOTH APPLIED** |
| rec | Residue paragraph refresh re RFC10-16 | **APPLIED** |

## 4. rev10-portability (directive §13.6) — EXCEPTIONS (2 must-fix, 6 non-blocking); core portability answered YES

| # | Finding | Disposition |
|---|---|---|
| 1 | F-EQ-8 D2 census fails its own pass condition (D2 in craft headers only, never in rfcs/) | **FIXED** — D2 dropped from the grep with an explanatory sentence (craft-cluster decision, honored in craft-and-care/ + record) |
| 2 | Two stale 06 cells (2,266→2,029; 3,029→3,027) | **QUEUED (post-batch regeneration)** — same fix stream as digestibility E3 |
| 3 | F-EQ-2 sed range unanchored (prints 14, states 9) | **FIXED** — anchored at the clause heading |
| 4 | F-EQ-1 annotation imprecise | **FIXED** — expectation reworded to the actual output shape |
| 5 | Prefix resolution silently prefers ancestor .syzygy over packet copies | **FIXED** — `context_load.py` now prints `[source] spec -> path (canonical home|packet copy)` to stderr |
| 6 | `scripts/__pycache__/` shipped | **FIXED** — removed (and re-removed after each script run) |
| 7 | bash/zsh + GNU-grep assumptions unstated | **FIXED** — stated in the fixture header |
| 8 | Packet mutated mid-review (topology/, one review file) | **No action** — deliberate lead additions (transaction E2 fix; raw-report storage); confirming review binds the final tree |

## Consolidated rfcs/ fix batch (single application after all six reviews; then scripted count refresh → manifest + index regeneration → confirming review)

**STATUS 2026-08-03: ALL SEVEN ITEMS APPLIED**, followed by the scripted
refresh (fixtures 1–5 re-measured, 06 map regenerated, README count tables
fixed, `05-CONTRACT-INDEX.yaml` regenerated with `--check` clean,
`ACTIVE-CONTRACT-MANIFEST.txt` regenerated — new package digest
`08793ddf70f3c2a30b5dcec51cac9266a81d03e9db48aa8b7071953f7687c936` —
record §1/§3 updated, `verify_final_prespec.py` PASS). Queued items below
are retained as the plan of record; none remains open.

1. RFC-0003 governance-homes: RFC3-16(b) constraint/authorization reconciling sentence (transaction E1)
2. RFC-0010: OD-R10 cite reworded as bootstrap provenance (:24); D3 draft pointer reworded (:61); MCP hedges (:93, :259); RFC10-16 four limbs restored (digestibility E1b, boundary E4/E8)
3. RFC-0011: OD-R10 cite (:24); F7 cite labelled bootstrap record (:54); budget-figure pointer reworded to name the artifact class, not the packet filename (:173, :246); RFC11-4 phase-rule-inclusion sentence; RFC11-12 four limbs restored (digestibility E1b, boundary E1b/E4)
4. RFC-0001: REVIEW-01-KERNEL cite → ../history/RFC-0001-history.md (digestibility E4)
5. RFC-0007 README: add "## Phase boundary" section (boundary E1a)
6. RFC-0008 README: front-matter tags += substrate (digestibility rec)
7. RFC-0002/0008/0009 READMEs: count tables regenerated from final bytes (digestibility E3)
Then: fixture 1 note update; 06 regeneration; ACTIVE-CONTRACT-MANIFEST + 05 index regeneration; record §1/§3 digest update.

## 5. rev10-safety (mission/autonomy safety, directive §13.3) — EXCEPTIONS, 14 (6 blocking)

All six blocking findings are clause-text repairs in the conservative direction; none
requires reopening an owner decision, but S1/S3 pin consequences the owner should see
(added to record §7). Rulings:

| # | Finding | Disposition (all clause edits in the rfcs/ batch) |
|---|---|---|
| S1 (A1) | RFC10-9 pre-A1 mission authorization undecided: "no mission until correlation" vs "forgeable bootstrap record suffices" | **FIX — strict reading stated operatively.** A mission-approval act is a *runtime* act performed after Syzygy exists, so it must be an A1-mechanism act (owner-attended, Syzygy-mediated, correlated to the external audit trail) — never a bootstrap-shaped tree record. An approval resting on a state-(1) record does not satisfy the RFC3-16(a) predicate and the mission never leaves `awaiting-approval`. "Renders as owner-adopted" applies to the *foundational corpus a mission cites*, never to the mission's own authorization. Consequence pinned (record §7): **Mission Control V0 ships the approval ceremony + external audit trail as a hard precondition** — consistent with RFC5-15/5-18(c), which already impose the same pre-A1 block on egress/execution |
| S2 (A2) | Sibling children over-subscribe parent budget (no reservation concept) | **FIX.** Child grants are reservations debited from the parent at grant time; invariant Σ(outstanding child grants) + parent's own spend ≤ parent budget, enforced at mint |
| S3 (A3) | RFC10-4 (every mission binds an initiating owner act) vs RFC10-8 (child limb implies agents may mint children) | **FIX — narrow-reading completion.** Decomposition is off by default: an agent may mint a child mission only when the parent envelope **explicitly grants decomposition** (an owner-approved envelope field); the child's authorizing provenance *is* the parent's act plus a recorded derivation, its envelope a reserved subset. Absent the grant, no children. Flagged in record §7 |
| S4 (A4) | RFC11-6 incomplete-context blocking is opt-in — inverts the corpus fail-closed posture | **FIX.** Default flipped: incomplete mandatory context blocks launch; proceeding on disclosed-incomplete context requires an explicit, owner-visible envelope relaxation |
| S5 (A5) | RFC10-10 "MUST prevent" unscoped — a guarantee the architecture cannot deliver (nominal control believed real) | **FIX.** MUST scoped to acts mediated by Syzygy's choke points; honest residual stated: effects reached through externally-held toolchain credentials are bounded by the adapter/credential authorization, not by the guardrail runtime (VIS-1 honesty; doctrine's outward non-enforcement) |
| S6 (A6) | RFC11-10 profile facts (independence, permissions, risk classes) satisfy envelope gates as self-assertions | **FIX.** Gate-satisfying profile fields are authorization-bearing under RFC3-16(a): they satisfy an envelope-required gate only with owner-act provenance or identified evidence; a self-asserted field fails closed for gate satisfaction |
| 7–9 (D1/D2/D5+D4) | D3 draft: gate-list weakening; narrow envelope enumeration; operational dependence unstated; VIS-4 self-licensing question | **FIXED (draft edits, applied)** — "every gate that would otherwise apply" + proceed-inside-gates sentence; enumeration marked non-exhaustive incl. write scope/gates; operative consequence of declining stated; the VIS-4 position stated explicitly with the owner's overrule path. D4 remains an owner ruling — record §7 |
| 10 (A12) | Propose-only interim floor only in the non-normative triage | **FIX (batch).** Moved into RFC10-7 clause text |
| 11 (A13) | `blocked → running` has no actor constraint | **FIX (batch).** Exit from a block arising under RFC10-8/10-11 is a human resolution act |
| 12 (A10) | Attention batch-resolution launders floods into consent | **FIX (batch).** One authorizing act resolves one item, or explicitly enumerates each resolved item's identity and chosen option; volume/SLA policy stays deferred but the per-item floor is clause text |
| 13 (A15/A16/A17) | Mission act-record home unstated; store writ overlaps its own prohibition; store deferral understated | **FIX (batch).** RFC10-14: approval act record lives at `.syzygy/governance/decisions/` binding the envelope digest — in-tree envelope + stamp is never the approval. RFC10-15: prohibition wins; pause = Syzygy refuses to schedule, never mutates project state; store home requires an RFC3-15-style recorded owner widening |
| 14 (A7/A8/A9/A20) | RFC11-4 dangling cite; projection-faithfulness unverified; no non-shardable core; packet not declared non-authorizing; memory promotion weaker than RFC3-16(a) | **FIX (batch).** Cite corrected to RFC11-7's projection; compiler must verify the projection regenerates faithfully before selecting; non-shardable core named (envelope in full + prohibited/always-human surfaces + applicable doctrine rules + the governing phase rule); packet reports/never grants; propose-only default into RFC11-8 + envelope-interpreting memory is authorization-bearing |
| A14/A18/A19 (worth-the-eye) | Scope legibility; completion evidence tier; ambiguity rule citation | **FIX (batch).** RFC10-3: holding a mission-affecting scope permits *submitting* an act for owner attendance, nothing more. RFC10-6: completion predicate declares a minimum RFC2-25 tier; render discloses tier achieved. RFC10-7: stated-but-ambiguous bounds resolve narrow and are escalation triggers (making RFC10-8's cite true) |

Structural observation (RFC 0001–0009 never cite RFC10/11 — no redundancy for
no-self-widening): recorded for the owner in record §7; adding back-citations to
accepted-clause text was NOT done (it would touch nine contracts for redundancy
alone; the single-source risk is disclosed instead).

## 6. rev10-equivalence (semantic equivalence, directive §13.1) — EXCEPTIONS, 7 (E1 act-holding)

Bottom line verified independently: zero lost clauses/obligations/decisions/closed
vocabularies; zero silently-closed questions; no weakened Unknown/evidence rule;
294+21 rev9 clause rows complete; 176 retained-unchanged rows machine-diffed clean.

| # | Finding | Disposition |
|---|---|---|
| E1 | Matrix records the unadopted-trigger change ("no verifiable record" → "no record at all") as "unchanged"/"weakens nothing" — a real owner-directed relaxation stated nowhere in the matrix | **FIXED** — RFC3-16 row now states the relaxation plainly (rev9 trigger vs rev10 trigger, what it licenses, what still fails the predicate); RFC3-16(c) row qualified to "weakens nothing *for Syzygy's own claims*" with a pointer to the relaxation row |
| E2 | Constraint-half of the two-audience split lives only in the acceptance record, not the contract | **FIX (batch)** — the RFC3-16(b) reconciling sentence (already queued from transaction E1) carries the constraint half into the contract corpus; a cross-reference bullet added in (c) |
| E3 | F-EQ-8 D2 census fails as written | **Already FIXED** (portability finding 1) |
| E4 | F-EQ-1/2 commands don't produce their stated outputs | **Already FIXED** (portability findings 3/4) |
| E5 | history q1(b) note points at a compaction-report flag that didn't exist | **FIXED** — the q1(b) inference disclosure now in the 03 report (§Disclosures) |
| E6 | Triage summary transposed | **Already FIXED** (boundary E9) |
| E7 | [Observed:] source-pointer attrition (121→92; RFC-0004 30→13) undisclosed | **FIXED** — disclosed in the 03 report §Disclosures |
| risks | RFC3-16(c) single-pass review; three-scope drift risk; RFC-0001 no selective benefit; digest stale projection | Confirming review re-binds RFC3-16(c) post-batch; drift risk mitigated by E2's fix (one complete statement in the contract); RFC-0001 disclosed; digest projection annotated as stale — DONE |

## 7. rev10 final confirming review (2026-08-03) — **CONFIRM** at `08793ddf70f3c2a30b5dcec51cac9266a81d03e9db48aa8b7071953f7687c936`

Raw report verbatim at `rev10-confirming-review.md` (stored before this
synthesis). All six numbered checks PASS; every claim re-reproduced. Three
residuals, dispositioned:

| # | Finding | Disposition |
|---|---|---|
| R1 | `rfcs/RFC-0007/README.md:46` self-count 2,268 (+ derived unions 10,578/7,435/5,411) stale by the 58-word Phase-boundary section added in the fix batch; actual 2,326 | **NOT FIXED — deliberately surfaced instead** (fixing churns the act-1 digest and forces another confirming cycle for a navigation figure that binds nothing). Recorded as record §7 item 10, a knowing-acceptance choice the owner makes at the gate, exactly per the reviewer's recommendation |
| R2 | Record §6 softened two reviewer verdicts (Boundary "8" vs actual 9 findings; Portability "PASS" vs actual EXCEPTIONS-all-fixed) | **FIXED (digest-stable)** — both labels corrected in §6; §6 now also discloses that it was corrected post-confirmation on the reviewer's R2 instruction. Lead error class: verdict-smoothing in a summary, the exact thing raw-report storage exists to catch |
| R3 | Two 3-cell rows under the register's 4-column header (Durable-state capsule, Convergence/regeneration certification) — classification value sitting in the gate column | **FIXED (digest-stable)** — gate cells added ("When missions outlive single sessions routinely"; "No gate scheduled") |

Standing risks the reviewer carried forward (single-source structure,
fixture-2 over-target load, `context_load.py` ancestor-preference logging,
R1's understated reading-path cost) are all already disclosed in record
§7/§3, the fixtures, and the script header — no further action.
