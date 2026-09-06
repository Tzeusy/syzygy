Reviewed commit: `9b28663804281f5419c41ea70b7ede52f8ff6597`

# PWB recovery gen-2 reconciliation and handoff

Date: 2026-09-06

Observed Butlers revision at review time:
`ec8b1f6cd529a976700a1360acfac1efc29f9762` (the same head the retained gen-2
repair demo observed; gen-1 observed `2891522f`).

Scope: the retained handoff for `syzygy-1z3.24.9`. One independent
fresh-context reviewer re-opened the gen-2 repairs (`syzygy-1z3.24.8`, the six
commits between `804339e` and `9b28663`) against the gen-1 reconciliation's
nine findings, the signed amended specification and a live clone-based run,
with the same single-reviewer method gen-1 used. It is not an owner judgment
under PWB-REQ-022 and changes no owner state. Between the review and this
handoff, `main` took the co-lead's docs-only commits (`e836952`, `119cebd`,
`b5651eb`, `e94172e`, `ac518d0`); none touches `apps/**` or `packages/**`, so
the reviewed code is the code this handoff sits on [Observed: `git diff --stat
9b28663 ac518d0 -- apps packages` is empty].

## Verdict

**CONFIRM WITH EXCEPTIONS.**

[Observed] PWB-RECON-01, the page half of PWB-RECON-02 and PWB-RECON-03 are
repaired. Reverting each repair's implementation hunks in the reviewer's clone
makes the new tests fail (78 of 103, 14, 5 of 18); the live human page on both
mounts renders the exact PWB-REQ-005 sentence once per authority and one
discovery state per pillar with the Unknown pillar's reason, route and
degradation state; the surface version is now a digest over both source
trees, recomputed by hand as `polaris@e64a10980701`. Sixteen of nineteen
reviewer mutants were killed. A fresh clone of `9b28663` builds, passes
1,537 tests (3 skipped) of 1,540, and its own fresh-checkout run exits 1 on
exactly `preflight-ready` with the same three Butlers-data limbs and identical
detail as the retained gen-2 record. Nothing under `openspec/**` or
`.syzygy/**` changed; the governance check reports 0 FAIL; the PWB-REQ-005
(195) and PWB-REQ-022 (84 + 2) denominators are untouched.

[Observed] The exceptions are test-rigor gaps in the new gates, not
conformance gaps: three mutants survived (a route rendered for the wrong
discovery reason; the preflight's page-wide route check removed; the core
model dropping Unknown pillars from `discovery` under the core test alone),
and the retained gen-2 mutation record stores no fragments and cites commits
no ref reaches. **Gen-3 needed: no.**

## Disposition register (PWB-RECON-01..09)

Register vocabulary: `repaired`, `open`, `owner-item`. Code evidence, gate and
the reviewer's own checks per row are in the raw review, Section A.

| ID | Disposition | Note |
|---|---|---|
| PWB-RECON-01 | repaired | sentence rendered once per authority on both mounts; equal to the machine disclosure ×3; 4 reviewer mutants killed plus the preflight-guard mutant |
| PWB-RECON-02 | repaired (page half) | cause, route and degradation state on the page; the cause itself (Spec and Spine has no index) stays owner item 3 |
| PWB-RECON-03 | repaired | surface version digests both source trees; three mutants killed; hand recomputation matches |
| PWB-RECON-04 | owner-item | unchanged; same three readiness limbs at Butlers `ec8b1f6` |
| PWB-RECON-05 | owner-item | unchanged; headroom shrank to 49,884 B direct and 44,244 B on the tailnet mount after the new lines |
| PWB-RECON-06 | repaired | the `vanish` counterexample kills the skip mutant |
| PWB-RECON-07 | repaired | tailnet mount, presentation envelope and Origin refusal probed live and gated by 19 verdict invariants; 12 of 41 fail on revert |
| PWB-RECON-08 | open | docs half done; `project-shape-discovery.live.test.ts` still pins `a3dd1fe` and is skipped in the battery |
| PWB-RECON-09 | owner-item | unchanged (wording, item 5) |

Denominator: 9 of 9 dispositioned; 5 repaired, 1 open, 3 owner-item, 0 declined.

## Exceptions (new findings)

| ID | Severity | Finding | Route |
|---|---|---|---|
| PWB-RECON-10 | Low (test rigor) | The cause-correct route for an Unknown pillar is not gated: returning the `index-unavailable` route text for `index-missing-at-revision` survives all 103 page, sweep and preflight tests. | One counterexample per reason asserting the route's distinguishing phrase; bead `syzygy-1z3.24.10` |
| PWB-RECON-11 | Low (test rigor) | The preflight limb `discovery-undisclosed`'s route check is a page-wide substring with no isolating counterexample; removing it survives 41 of 41. Same gate family as RECON-10, different instrument. | Counterexample plus scope the check to the Unknown pillar's own entry; bead `syzygy-1z3.24.10` |
| PWB-RECON-12 | Low (test rigor) | The core gate for `ProjectShape.discovery` covers only the all-discovered fixture; filtering Unknown pillars out survives the core test (0 of 29) and is caught only by the app page test. | One core assertion on an undiscovered fixture; bead `syzygy-1z3.24.10` |
| PWB-RECON-13 | Info (evidence quality) | The retained gen-2 mutation record names its twelve mutants but stores no fragments and cites pre-rebase commits (`c2d75c8`, `cff7e15`) that no ref reaches; nine in-session verdict and lifecycle mutants were not retained. Consistent, but not re-runnable from its bytes; the reviewer reconstructed equivalents. | Future rule-6 records retain fragments (guardrail added to AGENTS.md); no repair for this bead |
| PWB-RECON-05 (update) | Low (owner) | Tailnet headroom is now 2.1 % of the ceiling. | Owner item 4 stands; no new id |

## Gen-3 need

No. The three required repairs are confirmed by revert, mutation and live
observation; the fresh demo exits only on Butlers-data limbs; nothing
regressed. PWB-RECON-10..12 are test-rigor debts on the new gates (the live
route is cause-correct today) and close by an ordinary bead with its own
rule-6 evidence. The owner walkthrough remains not ready for the reasons the
owner already holds (PWB-RECON-04), not for any Syzygy-side gap.

## PWB-UX crosswalk (bounded addendum)

The co-lead's [Inferred] crosswalk in
`2026-09-05-pwb-live-finding-traceability.md` maps the UX reviewer's own
identifiers PWB-UX-1..4 to PWB-LIVE-02, -06, -13 and -13. The gen-2 reviewer
was asked to check it after its charge was issued and had frozen before the
request reached its report, so the raw review records no mapping. This
handoff's own reading of the two raw texts agrees with all four rows
[Inferred: the same overlapping sentences the crosswalk quotes, re-read at
`R-PWB-LIVE-EXACT-HEAD-UX-RAW.md` lines 153-154, 202, 248 and 297]. The
review reached no different answer, so the crosswalk stands as written.

## Owner decisions (accumulated for the 1z3.25 packet, in plain language)

Gen-2 adds one item; the gen-1 items stand unchanged.

1. The Butlers V1 page does not parse: one line uses a colon where the signed
   grammar requires a dash. Fix the line in Butlers, amend the grammar by act,
   or leave it Unknown. Until one of these, the walkthrough stays not ready.
2. Roster and topology files are withheld as active content or fail the table
   grammar. Repair the Butlers files, extend the policy's inert-context profile
   to TOML by a new policy act, or accept a roster denominator that stays
   Unknown.
3. Spec and Spine has no index file; its root-index cell points at a directory.
   The page now says so and names the missing index path. Add the index in
   Butlers, amend the discovery rule by act, or keep the permanent Unknown.
4. The human page is within 2.1 % of its byte ceiling on the tailnet mount.
   Raise the ceiling by a registry amendment act, or direct a presentation trim.
5. Record guidance should say, in the owner's words, that the exact-source
   route is a lawful walkthrough path.
6. Repaired, no decision: the state-(1) trust-gap sentence is now on both
   surfaces (PWB-RECON-01 closed by gen-2).
7. New: close epic `syzygy-1z3.24` now with PWB-RECON-08 and -10..13 carried
   as ordinary beads, or hold it until those test-rigor gaps close with
   evidence. The reviewer recommends closing now: none of them changes what
   the page says today.

## Planning state

- `syzygy-1z3.24.9`: this reconciliation; closes when these records are
  committed and pushed.
- `syzygy-1z3.24.10`: test-rigor repairs for PWB-RECON-10..12 (new bead).
- `syzygy-1z3.24.11`: re-pin the live discovery test (PWB-RECON-08, new bead).
- `syzygy-1z3.22`: owner walkthrough; still blocked, still Unknown.
- `syzygy-1z3.25`: cycle report; carries the seven items above.

No implementation, signed artifact, policy, registry, Butlers artifact or owner
state was changed by this review. The reviewer stopped its own daemon (stderr
empty) and signalled no other process.

## Evidence index

- `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN2-RAW.md`
  (`5cbc10e3a7cc812424d7218a48fad1ed4391f9f5fb7dc686b48df3a25e090d68`)
- `docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-06-gen2-reviewer.json`
  (`3fd46719ec7d02aea23e1e6be850717b9fa28864cee77d23c71325482658683a`) — the reviewer's own clone run at `9b28663`, Butlers `ec8b1f6`
- `docs/evidence/pwb-recon-gen2-reviewer-mutation-run-2026-09-06.json`
  (`c3aab77494720633fec0fa471b94009eff323e8ec9739d6b8b5ef217fa70abf8`) — 19 reviewer mutants with fragments, 16 killed, 3 survived
- Retained gen-2 repair evidence `docs/evidence/pwb-recon-gen2-repair-mutation-run-2026-09-06.json`, `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-06-parity-markers.json`, `docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-06-gen2.json`, checked by predicate in the raw review, Section C and E

Focused verdict: **CONFIRM WITH EXCEPTIONS**.
