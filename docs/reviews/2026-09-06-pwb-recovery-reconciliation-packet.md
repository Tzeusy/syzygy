Reviewed commit: `d92910c8a8f423414e82a25653b2857e92ebce32`

# PWB recovery gen-1 reconciliation and handoff

Date: 2026-09-06

Observed Butlers revision at review time:
`2891522f339df3a82e309d194fc41a5f7a63f8a3` (the retained 2026-09-05 fresh-clone
record observed `ff52900a341dfcc3d1018d6e5970a72526c085e3`; nineteen Butlers
commits lie between them).

Scope: the retained handoff for `syzygy-1z3.24.7`. One independent
fresh-context reviewer re-opened the whole PWB recovery (children
`syzygy-1z3.24.1`–`.24.6`) against the signed amended specification, the
2026-09-05 owner acts, the fifteen retained findings of
`2026-09-05-pwb-live-exact-head-packet.md`, and a live clone-based run. It is
not an owner judgment under PWB-REQ-022 and changes no owner state.

## Verdict

**CONFIRM WITH EXCEPTIONS.**

[Observed] Every one of PWB-LIVE-01..15 maps to exactly one repair child, to
code and to one gate the reviewer re-ran or mutated. The eleven amended
artifacts, the amended policy and the amended registry hash to their 2026-09-05
acts; nothing under `openspec/**` changed after sign-off; no digest-bound
artifact changed after its act. A fresh clone of the reviewed commit builds,
passes 1,498 tests (3 skipped), and its own fresh-checkout run exits 1 on
exactly one invariant, `preflight-ready`, with the same three limbs the
retained record shows.

[Observed] The exceptions are outside the fifteen: the human Polaris page does
not render the state-(1) trust-gap sentence PWB-REQ-005 requires on both
surfaces (the machine answer carries it); the reason the whole-shape claim is
Unknown never reaches the page; and the walkthrough binding does not change
with a core-package code change. The reviewer asks for one gen-2 implementation
pass before the owner walkthrough, and for owner decisions on the Butlers data
that keeps readiness blocked.

## Disposition register (PWB-LIVE-01..15)

Dispositions use the register vocabulary: `repaired`, `open`, `declined`.
Each row's code evidence and gate are in the raw review, Section A.

| ID | Child | Disposition | Note |
|---|---|---|---|
| PWB-LIVE-01 | syzygy-1z3.24.1 | repaired | |
| PWB-LIVE-02 | syzygy-1z3.24.2 | repaired | |
| PWB-LIVE-03 | syzygy-1z3.24.2 | repaired | |
| PWB-LIVE-04 | syzygy-1z3.24.4 (act via .24.3) | repaired | code and fixture gate complete; the live eight-versus-nine scenario is unobservable until the Butlers V1 page parses (owner item 1) |
| PWB-LIVE-05 | syzygy-1z3.24.2 | repaired | |
| PWB-LIVE-06 | syzygy-1z3.24.5 | repaired | |
| PWB-LIVE-07 | syzygy-1z3.24.4 (act via .24.3) | repaired | |
| PWB-LIVE-08 | syzygy-1z3.24.1 | repaired | |
| PWB-LIVE-09 | syzygy-1z3.24.1 | repaired | |
| PWB-LIVE-10 | syzygy-1z3.24.4 (act via .24.3) | repaired | |
| PWB-LIVE-11 | syzygy-1z3.24.5 | repaired | |
| PWB-LIVE-12 | syzygy-1z3.24.6 | repaired | |
| PWB-LIVE-13 | syzygy-1z3.24.5 | repaired | |
| PWB-LIVE-14 | syzygy-1z3.24.6 | repaired | |
| PWB-LIVE-15 | syzygy-1z3.24.2 | repaired | extraction half repaired and mutation-killed; the comprehension half is the owner's under PWB-REQ-021 by spec design |

## Exceptions (new findings)

| ID | Severity | Finding | Route |
|---|---|---|---|
| PWB-RECON-01 | High | Human Polaris page (both mounts) renders no state-(1) "Owner-trusted only; same-tree forgeable…" sentence for the three body-read authorities; PWB-REQ-005 requires it on both surfaces; the machine answer carries it; no human gate or parity family. Pre-existing at `cd6c952`. | Implementation, gen-2 |
| PWB-RECON-02 | Medium | Spec and Spine's declared home is a directory with no index, so the pillar is index-missing and the whole-shape claim is Unknown with an observer-repair route; neither the cause nor the degradation state reaches the human page. | Owner wording (item 3) plus implementation, gen-2 |
| PWB-RECON-03 | Medium | The evaluation identity and surface version are blind to core-package code changes (version literals unchanged since `e1617a4`; surface tree is the app source only). | Implementation, gen-2 |
| PWB-RECON-04 | Medium (owner) | Readiness is blocked by Butlers data wider than recorded: the V1 colon row, a topology table that fails the grammar, one Lay and Land page and seven of thirteen roster files withheld as active content (TOML has no inert context), one detector hit. | Owner (items 1–2) |
| PWB-RECON-05 | Low | Human byte ceiling headroom is 52,066 B direct and 46,426 B on the tailnet mount; the demo measures direct only. | Owner (item 4) |
| PWB-RECON-06 | Low | One reviewer mutant survived (an unreadable decision record skipped inside lifecycle enumeration), equivalent on the git-tree path. | Test rigor, gen-2 optional |
| PWB-RECON-07 | Low | The fresh demo and preflight never exercise the tailnet mount, the machine presentation envelope or an Origin refusal. | Demo probes, gen-2 optional |
| PWB-RECON-08 | Low (docs) | The AGENTS.md known-gap line about the excluded Lay and Land index is stale at the current Butlers head; the live discovery test pins `a3dd1fe` and is skipped in the battery. | Docs note (fixed in this handoff); re-pin the live test |
| PWB-RECON-09 | Info | The exact-source route is already a lawful PWB-REQ-021 traversal and is in the schedule; only record-guidance wording remains. | Owner wording (item 5) |

## Gen-2 need

Yes. Gen-2 must repair PWB-RECON-01, the page half of PWB-RECON-02 and
PWB-RECON-03, each with a pre-fix-failing test and rule-6 evidence, then re-run
the fresh demo and obtain an independent gen-2 reconciliation. PWB-RECON-04 and
-05 wait on the owner. Epic `syzygy-1z3.24` does not close before gen-2 or an
explicit owner acceptance of RECON-01..03 as tracked debt; the owner walkthrough
stays not ready in either case until owner item 1 or 2 lands.

## Owner decisions (collected for the 1z3.25 packet, in plain language)

1. The Butlers V1 page does not parse: one line uses a colon where the signed
   grammar requires a dash. Fix the line in Butlers, amend the grammar by act,
   or leave it Unknown. Until one of these, the walkthrough stays not ready.
2. Roster and topology files are withheld as active content or fail the table
   grammar. Repair the Butlers files, extend the policy's inert-context profile
   to TOML by a new policy act, or accept a roster denominator that stays
   Unknown.
3. Spec and Spine has no index file; its root-index cell points at a directory.
   Declare "declared without an index" by a wording amendment, add an index in
   Butlers, or keep the permanent Unknown. In every case the page should say
   why the top claim is Unknown (PWB-RECON-02).
4. The human page is within 2.2 % of its byte ceiling on the tailnet mount.
   Raise the ceiling by a registry amendment act, or direct a presentation trim.
5. Record guidance should say, in the owner's words, that the exact-source
   route is a lawful walkthrough path.
6. No decision: the state-(1) trust-gap sentence is today visible only to
   machine readers (PWB-RECON-01); gen-2 repairs it.

## Planning state

- `syzygy-1z3.24.7`: this reconciliation; closes when these records are
  committed and pushed.
- Gen-2 repair and gen-2 reconciliation children are filed under
  `syzygy-1z3.24`; the epic stays open.
- `syzygy-1z3.22`: owner walkthrough; still blocked, still Unknown.
- `syzygy-1z3.25`: cycle report; carries the six items above.

No implementation, signed artifact, policy, registry, Butlers artifact or owner
state was changed by this review. The reviewer stopped its own daemon and did
not signal the pre-existing one.

## Evidence index

- `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md`
  (`f3f6e0b689686d65ab0fa6b44fd62526eb584ac9cab94c9ed777b524b08d5fbe`)
- `docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-06.json`
  (`bbea4f375e21cb35be08ed16cf3b011ad497f8c6e7f697a548cd376a3a77f302`) — the reviewer's own clone run at `d92910c`, Butlers `2891522f`
- `docs/evidence/pwb-recon-gen1-reviewer-mutation-run-2026-09-06.json`
  (`554211c49e780e07b81d1ab66708ca316059a620e6d8bcc15e5a13c300e004ed`) — 14 reviewer mutations, 13 killed, 1 equivalent survivor
- Retained C4–C7 mutation evidence `docs/evidence/pwb-c*-2026-09-05.json`, cited by predicate in the raw review

Focused verdict: **CONFIRM WITH EXCEPTIONS**.
