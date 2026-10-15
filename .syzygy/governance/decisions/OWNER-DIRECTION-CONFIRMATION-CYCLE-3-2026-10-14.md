# Owner direction — a third repair-and-review cycle, and the answers after it (2026-10-14/15)

> **A plain owner direction.** It binds no digest, adds no row to
> `ACCEPTANCE-ACT-RECORD.md`, registers nothing in
> `scripts/check_governance.py`, and performs no act. It adopts and rules
> nothing on any packet's content questions (VIS-4), except where an
> answer below is itself the owner's version-tagged sign-off, which its
> own record carries (the P-99 sign-off; see "Outcome"). It records why a
> third repair and a further review round ran, what each round returned,
> and what the owner answered after those rounds.

## The cycle-3 directions

The second cycle
([`OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`](OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md))
left five packets `REVISE` (P-84, P-85, P-98, P-101, P-102) and cleared
P-99, whose regeneration over the P-86 sign-off then moved its manifest.
Later on 2026-10-14, in the lead Claude Code session and in answer to
structured questions, the owner selected these options. [Observed: the
option labels, and the option text where given, as the lead session
relayed them to this integration; the owner's answers themselves are in
that session, not in this repository. The relay dates this group
2026-10-14.]

| Packet | Option selected | Option text, as relayed |
|---|---|---|
| P-84 | "Park, redraft narrower" | "Stop this package. A fresh drafter redrafts it from the 43 findings as a smaller package, for example the record-ownership machinery split from 055/060." (quoted in `contracts/candidates/three-surface-poc-vocabulary-epistemic-amendment/SEMANTIC-DELTA.md`) |
| P-85 | "One more cycle each" (with P-98) | Repair every round-4 finding, notes included, then one fresh review under the same stopping rule. |
| P-98 | "One more cycle each" (with P-85) | The same, for the round-3 findings. |
| P-101 (D7) | "One more cycle" | "Make Q5 consistent: state that choosing a reading of accepted text is a contract act matter (Unknown otherwise), and align §4/§6 and the ledger. Then one fresh review." |
| P-102 (D8) | "Drop dismissal from (d2)", then one more cycle | "Dismissals of an observed-only project's gaps can't live in the observing project's tree, so VIS-6 stays intact. Then one more cycle." |
| P-99 | "Carry if review clears" | Its v1.0 sign-off (Q1 "Sign v1.0", answered in cycle 2) carries to the version regenerated over P-86 if the confirmation review is notes-only and `proposed/spec.md.patch` is byte-identical to the version round 3 read. |

**The stopping rule** is the one stated with the cycle-2 direction: one
repair of every finding, notes included, and one fresh review per packet.
A round with no revise-severity or blocking finding clears the exact bytes
it read under the owner's 2026-09-26 ruling
(`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), its notes going in a
sibling record and the package not edited. A round still `REVISE` comes
back to the owner with its findings open. A verdict is never re-labelled,
and a clearance is not a sign-off. P-84 was not repaired: it is parked,
and its narrower redraft is a new package, P-108, which had its own
round 1.

This record is the `decisions/` record that the D7 round-4 raw's note 5,
the D8 round-4 raw's note 6 and the P-85 round-5 raw's note 6 say was
missing.

## The repairs

Each was one pull request, rebase-merged to `main` on 2026-10-14.

| Packet | Package | PR | Merged commit |
|---|---|---|---|
| P-84 parked; P-108 drafted | `three-surface-poc-identity-amendment` (parked); `three-surface-poc-vocabulary-epistemic-amendment` (new) | #433 | `6d3923f365bca6e4458200ac0f75381655ef5bb6` |
| P-101, P-102 | `doctrine-amendment-held-derived-computation-d7`, `doctrine-amendment-inferred-first-class-d8` | #432 | `79f51fdfa5350feb747162af91137758dc3b38ed` |
| P-85 | `pwb-release-label-amendment` (also regenerated over P-86) | #431 | `83b29c96775d9c2215292fa41e1599080f0b802c` |
| P-98; P-99 regenerated | `pwb-opening-index-amendment`, `pwb-accessible-name-amendment` | #430 | `65f84c71d5a08a735fb28eed57ba73e303b5b7db` |

[Observed 2026-10-15: each PR number and merge commit from `gh pr list
--state merged`; each commit is an ancestor of this record's branch.]

## What each round returned

Every verdict word below is copied from the raw file at the line cited,
and each head digest is the one on the raw's own line 3. Every raw is
retained verbatim under `docs/reviews/` (CC-REV-6); there are six.

| Packet | Round | Raw | Reviewed commit | Head digest (raw line) | Verdict (raw line) | Revise / notes |
|---|---|---|---|---|---|---|
| P-85 | 5 | `R-PWB-RELEASE-LABEL-AMENDMENT-5-RAW.md` | `83b29c96775d9c2215292fa41e1599080f0b802c` | Manifest SHA-256 `d7220b77fdc1b61f05a3a15f43e157ff279a179dc3bc84ca152b5e9832f1b1ad` (3) | `REVISE` (4) | 1 / 7 |
| P-98 | 4 | `R-PWB-OPENING-INDEX-AMENDMENT-4-RAW.md` | `83b29c96775d9c2215292fa41e1599080f0b802c` | Manifest SHA-256 `fe0791ef8699083ad88871b2ed0a2a183fd5a8f469e99ae1306f45f9ed441867` (3) | `CONFIRM WITH EXCEPTIONS` (4) | 0 / 7 |
| P-99 | 4 | `R-PWB-ACCESSIBLE-NAME-AMENDMENT-4-RAW.md` | `83b29c96775d9c2215292fa41e1599080f0b802c` | Manifest SHA-256 `f794d73536f55b916fa09bff8504cecf7b9b67d225c0cc0916211184cbb95490` (3) | `CONFIRM WITH EXCEPTIONS` (4) | 0 / 3 |
| P-101 | 4 | `R-DOCTRINE-AMENDMENT-D7-4-RAW.md` | `79f51fdfa5350feb747162af91137758dc3b38ed` | Package digest `b237bc50abf8bf53384a8591830db75d05dcd520b6081c127ec67c9f7cba36e7` (3) | `REVISE` (4) | 1 / 4 |
| P-102 | 4 | `R-DOCTRINE-AMENDMENT-D8-4-RAW.md` | `79f51fdfa5350feb747162af91137758dc3b38ed` | Package digest `21198cac259b3ef68462632d774c83ed6dcba00361cf3dad643fa58db21bd8c3` (3) | `CONFIRM WITH EXCEPTIONS` (4) | 0 / 6 |
| P-108 | 1 | `R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md` | `6d3923f365bca6e4458200ac0f75381655ef5bb6` | Manifest SHA-256 `03069d521ae3280f2abf8525950d74e3a128cec1db140218efa3372791a75cba` (3) | `REVISE` (4) | 2 / 7 |

[Observed 2026-10-15] Every revise and note count above was re-derived by
script from each raw's finding headings and their severity words. It
agrees with each raw's own closing count where it has one (P-85 raw line
152, P-101 line 293, P-102 lines 248–249, P-108 line 297). The P-98 and
P-99 raws have none; each says "Every finding below is a note." (P-98 line
164, P-99 line 116). No round raised a blocking finding. The P-85 raw
numbers its revise finding and its notes separately (Finding 1, Notes
1–7).

[Observed 2026-10-15] Each head digest was recomputed from the bytes at
the reviewed commit, and each matches: for the four manifest-bound
packages, the manifest file's sha256; for P-101 and P-102, each brief's
directory method over the seven files the reviewed commit tracked there.

## The owner's answers after those rounds

On 2026-10-14/15, in the lead session and by structured questions, the
owner answered. [Observed: as relayed to this integration, with the same
caveat as above; the relay does not date each answer separately.]

- **P-85: "One more cycle"** — a round 6: one more repair of the round-5
  findings, notes included, then one fresh review under the same rule.
- **P-101 (D7): "Park until RFC2 decided"** — park D7, and commission an
  RFC2-18/19 contract clarification draft fixing which reading binds
  (the narrow, the wide, or the broadest built from RFC4
  `named-adapters.md` lines 420–421 and 492); then redraft D7 against it.
  Filed as `syzygy-a4ry` (the commissioned clarification draft, related to
  the earlier `syzygy-nosn`) and `syzygy-xhh2` (the D7 redraft, blocked by
  `syzygy-a4ry`), both related to `syzygy-u05.14`. The inference-profile
  draft D8's Q-C1 commissioned is `syzygy-3p62`, filed by the D8 change.
- **P-108: "One cycle"** — one repair of the round-1 findings, notes
  included, then one fresh review.
- **P-98**, answered on the cleared version:

  | Question | Option selected, as relayed | The packet option it selects (`OWNER-DECISION-PACKET.md`) |
  |---|---|---|
  | Q1 | "Sign v1.0" | "Sign v1.0" — "The patch is applied in the sign-off change by version tag (Scope A covers PWB specification deltas)." |
  | Q2 | "Walkthrough identities" | "The nine walkthrough identities of PWB-REQ-021" — "The rows are the questions the cold-open walkthrough asks, in its order." |
  | Q3 | "Words visible on arrival" | "Words in the flow on arrival" — collapsed disclosure text left out until opened, its visible toggle label counted. |
  | Q4 | "Human surface only" | "No, human surface only" — the offsets stay out of the machine answer and the PWB-REQ-020 parity sweep. |
  | Q5 | "Existing roles" (confirming both readings) | The existing copy roles: row names are action labels, the offsets and the stopping line scope instructions, an unrendered row's text an epistemic disclosure, with PWB-REQ-012's one-entry-scope-instruction limit read as the packet reads it. |
  | Q6 | "Leave for now" | "Leave it for now" — slice B is not drafted. |
  | Q7 | "Covered by syzygy-k0np" | Slice D is the POC-REQ-061 bead already filed under P-99's Q4, `syzygy-k0np`; no second bead. |
  | Q8 | "Names from the table" | "Row names from the table; no separate accessible-name rule". |
  | Q9 | "Keep name and place" | "Keep the name and place". |
  | Q10 | "The opening window" | "The window the page opens in". |
  | Q11 | "Step outward" | "Step outward" — the line goes just after the outermost collapsed disclosure, paragraph, heading, list or table that holds the target's start. |
  | Q12 | "Disclose it, as now" | "Disclose it, as now". |

  And **"Carry if review clears"**, the P-99 rule, applying after P-98 is
  regenerated over the signed P-99: its Q1 "Sign v1.0" carries to that
  version only if its confirmation review is notes-only and its
  `proposed/spec.md.patch` is byte-identical to the version round 4 read.
- **P-99** keeps its cycle-2 answers, Q1 "Sign v1.0", Q2 "All focusable",
  Q3 "One h1, no skips", Q4 "File a POC-REQ-061 bead" (filed:
  `syzygy-k0np`), Q5 "First ready lands first", Q6 "Every Polaris page",
  Q7 "Label + source path" and Q8 "No exemption", under the cycle-3
  "Carry if review clears" rule above.

The D8 (P-102) answers on the cleared packet are applied by a separate
change and are not recorded here.

## Outcome

- **P-98, P-99 and P-102 clear.** Each returned notes only, which clears
  the exact bytes it read at the digest above. The notes are
  dispositioned, open, in a sibling record beside each package, and no
  other file in those packages is edited:
  - P-98: `pwb-opening-index-amendment/ROUND-4-DISPOSITIONS.md`;
  - P-99: `pwb-accessible-name-amendment/ROUND-4-DISPOSITIONS.md`;
  - P-102: `doctrine-amendment-inferred-first-class-d8/ROUND-4-DISPOSITIONS.md`.

  Their stale "pending round N" and "not yet recorded under `decisions/`"
  sentences are corrected in those records, not in the packages.
- **P-99 is signed v1.0** under its carry-over rule, whose three
  conditions were each verified on the sign-off branch: the round-4 raw is
  notes-only (three notes, each `(note)`); its head manifest digest equals
  the manifest file at `main`; and `proposed/spec.md.patch` is the same
  blob at `d6b3784f`, the commit round 3 read, and at `main`. The sign-off
  record is
  [`PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md`](PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md),
  tag `pwb-accessible-name-amendment-v1.0`. It authorizes no
  implementation.
- **P-98 is answered and not signed.** The P-99 sign-off moves PWB
  `spec.md`, so under the carry-over rule P-98 is regenerated over it and
  reviewed again first, by another change.
- **P-85, P-101 and P-108 are `REVISE`.** Each has a dispositions record
  beside its package: P-85 `ROUND-5-DISPOSITIONS.md` and P-101
  `ROUND-4-DISPOSITIONS.md` classify their findings and repair nothing.
  P-108's `ROUND-1-DISPOSITIONS.md` was written by the separate repair
  lane (PR #445, `b5a7e27a`), which repaired the round-1 findings once on
  2026-10-15, notes included; the repair is unconfirmed until round 2, which
  is briefed and not yet run. This change only adds a section to that
  file, naming the raw that now lands. Under the owner's answers, P-85 gets
  one more repair and one fresh round, made by a separate change.
  P-101 is **parked** (a dated banner heads its packet) until the
  commissioned RFC2-18/19 clarification exists and D7 is redrafted
  against it.
- Register rows P-85, P-98, P-101 and P-108 say this, with one dated
  header note and a recount; P-99 moves to `DECISION-HISTORY.md`.

## Integration facts

[Observed 2026-10-15 on branch `governance/cycle-3-records` over
`origin/main` `60995b23`. Re-checked after rebasing onto `b5a7e27a`:
`git diff 83b29c96 b5a7e27a` over the paths below is empty.]

- **The cleared packages are unchanged since their reviewed commits.**
  `git diff --stat 83b29c96` over the P-99 package directory, its builder,
  the shared engine `scripts/pwb_requirement_amendment.py` and the PWB
  change directory is empty, and the P-98 and P-99 manifest files hash to
  their raws' head digests. The D8 directory method over its seven tracked
  files gives the raw's head digest.
- **Composition before the sign-off.** The three pending PWB builders'
  `--check` pass here: accessible-name, opening-index and release-label.
- **Status marks.** In the P-85 and P-101 packages, the stale
  "unconfirmed pending round N" and "not yet recorded under `decisions/`"
  sentences in the packet, delta, ledger and latest dispositions record
  are marked at the sentence, dated 2026-10-15, with the old text kept.
  Raws and review briefs are not edited. In the P-108 package this change
  edits only `ROUND-1-DISPOSITIONS.md`, which the repair lane wrote: it
  marks that file's "not recorded under `decisions/`" sentence at the
  sentence and appends a section naming the raw. The packet, delta and
  brief belong to that lane.
- **Package digests that move.** The P-101 directory digest covers every
  tracked file in its package, so the new record and the marks move it
  away from the head digest above; it is not cleared, so no clearance is
  retired. The P-102 directory now also holds its sibling
  `ROUND-4-DISPOSITIONS.md`; the cleared digest stays the one over the
  seven files the round read.
