# Review - D8 doctrine amendment packet (Inferred first-class, P-102) — round 2
Reviewed commit: 8f1fbec7723a4e60b8c00f03f260a1979e3d7738
Package digest: bf095a565049e4900a0744b2cb82a39f7bec9b5d59791307bb79f6560e091c34
Verdict: REVISE

Reviewer: a fresh-context agent that drafted none of this package (CC-REV-1).
This is round 2 under `REVIEW-BRIEF.md`, dispatched by the coordinator.
Date 2026-10-14.

## Method

- `git rev-parse HEAD` in the review worktree returned the reviewed commit.
  The worktree was clean.
- The package digest above was scripted, not transcribed. It is the brief's
  method: `git ls-files` of the package directory, sorted by bytes, each
  file hashed into a `<sha256>  <path>` line, and the concatenation
  sha256'd. It covers 5 files: IMPACT-LEDGER.md, OWNER-DECISION-PACKET.md,
  REVIEW-BRIEF.md, ROUND-1-DISPOSITIONS.md and SEMANTIC-DELTA.md. A plain
  `sha256sum` of the five files gave the same per-file hashes.
- I read the governing references the brief names, plus the round-1 raw
  (`docs/reviews/R-DOCTRINE-AMENDMENT-D8-1-RAW.md`) and
  `ROUND-1-DISPOSITIONS.md`. To check §8 at this commit I also read D7's
  packet, which is now on `main`.
- I re-ran the ledger's term sweep (Python `re`, the ledger's predicate,
  population and lane order) at `59fbf787` and again at the reviewed
  commit. The second method was a `git grep -l -i -E` count at `59fbf787`.
- I re-ran the ledger's §4 method-2 static reader sweep at `59fbf787`.
- Partial application probe: in a scratch clone at the reviewed commit, I
  applied insertion (d2) alone to `vision.md`. I then ran
  `record_polaris_understanding_adoption.py --check` (PASS before the
  insertion) and `build_directive_register.py --check`. No repository file
  was edited.
- **Process note.** This round runs outside the brief's own stopping rule
  ("One round … no round 2 is dispatched", brief lines 9–12). The brief
  names only a round-1 output path. The head line is the brief's title plus
  " — round 2", as the dispatcher instructed.

## What holds [Observed unless marked]

- **Digests.** All three doctrine sha256 values in packet §1 and
  SEMANTIC-DELTA match the bytes at the reviewed commit. Since `59fbf787`,
  doctrine changed only in `security.md` and `v1.md` (D9), which D8 does not
  touch.
- **Anchors.** Every anchor's quoted text and line range is exact at the
  reviewed commit:
  - trust-and-evidence.md 44–49, 95–96, 118–119, 134–137, 144 and 175–180;
  - vision.md 232–234;
  - architecture.md 14, 18–21, 23–25 and 210–216.
- **Other quotations.** These are exact:
  - P-75 Q4, P-71 Q3, P-71-Q5, P-74 Q3 and P-76 Q2 (rulings file lines
    58–64);
  - L3-M7's two sentences, N15's `why` and L2-F5's title (pursuit data);
  - REQ-polaris-generation-019's consent sentence (amendment `spec.md`
    line 508, heading at line 506, ID at line 510);
  - RFC1's deferral line 1005;
  - SDR-30 (`SURFACE-DECISION-RECORD.md` line 163);
  - RFC2-24 reason 8;
  - RFC2-25's tier table and the `editorial-draft` paragraph;
  - the PWB coverage-part row (line 35);
  - the M4 funnel Q3 sentence.
- **Term sweep.** It reproduces exactly at `59fbf787`: 1,554 files, 147 hit
  files and 407 occurrences. Every lane row matches the ledger table. The
  `git grep` second method also returns 147 files. That is a count match;
  the ledger and round 1 record set-equality.
- **Static reader sweep.** It reproduces at `59fbf787`: 686 files and 39
  readers. The partition 20 + 1 + 2 + 1 + 15 holds file by file.
- **Recorder gate.** The ledger's §4 claim holds at the reviewed commit.
  With (d2) applied, the recorder's `--check` fails with "review retired by
  changed input: .syzygy/governance/doctrine/vision.md". The directive
  register reports "DIRECTIVE-REGISTER.md is stale". The recorder binds
  `VISION` at line 240, and the message is at line 592.
- **Composition (§8).** D7 (now on `main`) anchors vision.md 105–107 and
  architecture.md 329–334, so no bytes overlap with D8's.
- **Round-1 repairs, checked against the current bytes:**
  - Finding 1: (f) now names `editorial-draft` in the clause, in §0, §1, §2
    and in the delta.
  - Finding 2: the §0 (d) row places the blocker in the registry entry and
    the 2026-09-02 act, and quotes P-71-Q5's route. Q4 gains the act-route
    arm. (d1) is reconciled with the Definitions entry.
  - Finding 3: "self-observed" is gone. §2 maps "subject disclosed" to
    repository identity. The `gate-backed` effect is restated without a tier
    ordering.
  - Finding 5: the battery probe, Q-A1 and §9 step 3 are present.
  - Notes 6–15: each disposition matches the bytes, and P-102 exists at
    register line 1151.
  - Finding 4: repaired in the packet, but see finding 3 below.
- **Acceptance criterion 4.** No doctrine, contract, specification or code
  byte is edited by the package.

## Findings

### 1. Revise-level [Inferred]: clause (e) denies self-observation records to the "release verdict" while letting them evidence the floor that is the release verdict

The repaired clause says records whose subject is Syzygy's own governance
root "are never the evidence for a claim about Syzygy's own alignment,
convergence, genome-completeness or release verdict". It then says
"Evidence that the pipeline is deterministic and resolves its links may
come from any subject, this one included".

The trust floor is the release verdict. trust-and-evidence.md lines 159–161
read "a Syzygy release that breaks any of four properties is blocked", and
VIS-7 reads "Syzygy's own releases are blocked by the trust floor". So:

- Determinism or link evidence over this repository is evidence bearing on
  the release verdict. The two sentences pull against each other unless
  "release verdict" means something narrower, which the clause does not
  define.
- The permissive sentence names only floor bullets 1 and 2. A
  self-observation render shown to contain no secret material (bullet 4),
  or legend-faithful encodings (bullet 3), is left under the denial. That
  may be unintended.

Repair:

- Drop "release verdict" from the denial. Alignment, convergence and
  genome-completeness are the status-claim triggers at line 60.
- Or state that evidence for all four floor properties may come from any
  subject, and say what "release verdict" excludes.

### 2. Revise-level [Inferred]: clause (a) on Polaris collides with accepted RFC7-20, which the premise check does not name

RFC7-20 (`RFC-0007/narrative-contract.md` line 416) reads: "Generated prose
appears **only** in the explicit **editorial-draft** state … **non-citable**
… never satisfying a claim". RFC7-21 makes adoption a human act.

Clause (a) defines a synthesis as prose "a surface composes" and calls it
"an inference: it renders Inferred". §2 maps it to the Inferred label, as
a claim.

- A Polaris synthesis composed at render time by a declared inference
  process is generated prose. Under RFC7-20 it is an `editorial-draft`
  sibling state, not an Inferred narrative claim.
- RFC7-2(c)'s Inferred claims exist inside curated narrative, which only an
  authoring act produces (RFC7-2 "The check binds the authoring act").

So the §0 (a) row's "accepted contracts already permit" is incomplete. Its
blocker list (PWB-REQ-012 roles, the inference profile) omits an
accepted-contract rule that decides how such prose renders on Polaris.

The ledger's [Unknown] (a)/(f) overlap is a special case of this, not the
whole of it.

Repair: cite RFC7-20 in §0 and §1 (a), and say how (a) relates to it. Two
ways are open:

- scope (a) to surfaces outside RFC 0007, or to adopted narrative;
- route an RFC7-20 question to the owner beside Q-S1.

Recheck the "decline: doctrine already permits it" rationale for Q1 once
that is done.

### 3. Revise-level [Observed]: the ledger still quotes clause (e)'s pre-repair trigger as its current text

Round-1 finding 4 faulted the trigger phrase "observes its own repository
as an observed project". The disposition says the clause now reads
"Syzygy's observation pipeline evaluates Syzygy's own governance root as
its subject", and packet §1 (e) does read that way.

IMPACT-LEDGER.md §5 item 2 (lines 197–204) still says: "Clause (e) is
drafted to bind only observation-pipeline records ("observes its own
repository as an observed project")". It also still calls the scope "the
clause's main risk", flagged to the reviewer.

This is a quotation that differs from its source, the packet's proposed
bytes, inside the blast-radius record the owner reads. The repair of a
revise-level finding is therefore incomplete.

Repair: quote the current trigger, or mark the item as superseded by the
repair, dated, at the sentence.

### 4. Note [Observed]: review-state sentences go stale when this round lands

These sentences say no round 2 ran:

- packet line 14: "no round 2 ran";
- SEMANTIC-DELTA lines 173–176: "one round under `REVIEW-BRIEF.md`";
- register row P-102 (line 1151): "no round 2 was dispatched".

The brief's stopping rule (lines 9–12) says the same. Each becomes false
once this raw is retained. Mark each at the stale sentence, dated, per the
CG-27 lesson, and say in the dispositions under what direction round 2 ran.

### 5. Note [Observed]: §2's (f) row says `editorial-draft` "before and after the human authorship act"

- RFC7-20 and RFC7-21 say a draft "becomes curated narrative" through the
  human act. After that act it leaves the draft state and stays non-citable
  by RFC7-4 ("adopted-after-review").
- The clause's own wording ("stays non-citable after") is right. The §2
  cell and the delta's "(f)" bullet should say "`editorial-draft` before;
  presentation, non-citable (RFC7-4), after".
- RFC2-25 defines `editorial-draft` as "Narrative prose under revision".
  Applying it to a figure or passage selection extends that semantics, and
  the clause should say so [Inferred].

### 6. Note [Observed]: "observing project" is attributed to a ruling that uses it in another sense

- Packet §1 (d) says "'Observing project' is the phrase the owner's P-76 Q2
  ruling uses ('an observing project reading its own tree')". P-76 Q2's
  observing project reads **its own** tree. That is self-observation, not
  one project observing another.
- (d2) uses the phrase for a project that records consent to observe
  *another* project. That sense is the M4 funnel Q3's ("writing a
  governance artifact of the observing project *about* the observed
  project").
- Cite the M4 funnel instead, or say both senses exist.

### 7. Note [Inferred]: the P-71 Q3 statement omits which arm the owner declined

- M4 funnel Q3's recommended arm (a) put drafted packets about the observed
  project into "Syzygy's own `.syzygy/governance/decisions/`". The owner
  chose arm (b), which writes no file.
- Clause (d) recommends adopting exactly that destination class. The packet
  quotes the ruling correctly, but it should say that the owner declined
  the arm that placed content there, and why (d) does not reopen that
  choice. This keeps the owner's trade-off visible (AGENTS.md
  "Preserve the owner's trade-offs").

### 8. Note [Inferred]: (d1)'s terms and placement

- "Its write surface is empty" brings the registry field `writeSurface`
  into doctrine without defining it.
- architecture.md lines 18–21 make a project "explicitly brought under
  Syzygy observation" a governed project. (d1) does not say whether an
  observed-only project is a governed project. That decides what "the
  governed plane" means for it in VIS-6 and in (b).
- (d1) is inserted as a sibling of a bullet that lists repositories *within*
  a governed project, but it defines a kind of project.

### 9. Note [Inferred]: (d2)'s dismissals and Q-C2

- A dismissal or promoted annotation about the observed project necessarily
  names one of that project's gaps or entities. Q-C2's "no, while records
  stay unlinked to the observed project's entities" arm therefore cannot
  hold for two of (d2)'s three named examples.
- architecture.md lines 115–117 keep committed-out dismissals "with the
  repository" on offboarding. Under (d2), dismissals about an observed-only
  project stay in the observing project's tree, and nothing says what
  happens to them when that project offboards.

### 10. Note [Inferred]: (e) sits inside the normative trust floor without saying whether it is release-blocking

The insertion goes between the floor's bullets and its closing sentence, in
a section that opens "a Syzygy release that breaks any of four properties
is blocked". The delta lists "The trust floor's four bullets and its closing
sentence" as unchanged, but does not say whether violating (e) blocks a
release.

### 11. Note [Observed]: Q3's rationale lags the reclassification of (c)

- The §7 table gives Q3 as "decline — RFC1-16/RFC4-26 already define it".
- After the round-1 repair, §1 (c) says the clause widens past their
  capability↔code domain, and rests the decline on trust-and-evidence.md
  lines 118–119.
- The table cell should match.
- Related, minor: the delta's (a) row says "regenerate on change". The
  clause says stale when an input is stale, and withdrawn until regenerated
  only on a broken or superseded input.

### 12. Note [Observed]: figures and absence claims are pinned to `59fbf787`; several moved by the reviewed commit

This is lawful, since the ledger states rule-7 scope. At
`8f1fbec7`, with the package excluded:

- **Term sweep:** the same predicate gives 1,864 files, 149 hit files and
  427 occurrences. The authority-lane file sets are unchanged. The new
  decision occurrences are D8's own register lines 1147 and 1151.
- **Digest absence:** the statement that architecture.md's digest "occurs
  in no tracked file", and that vision.md's occurs only in three evidence
  files, is false at this commit. D7's `OWNER-DECISION-PACKET.md` (lines
  87, 121) and `SEMANTIC-DELTA.md` (lines 12, 14) now carry both digests.
- **D9:** adopted 2026-10-06, editing `security.md` and `v1.md`. It has no
  byte overlap with D8, and §8 does not mention it.
- **The battery:** it has grown since `59fbf787` (60 script files
  changed), so the 80-command probe is valid only at its commit. My partial
  probe confirms the recorder and register rows at this commit. I did not
  re-run the full battery.

## Summary

- Revise-level findings: 3 (findings 1–3).
- Notes: 9 (findings 4–12).
- All anchors, digests and quotations I checked are exact, and both sweeps
  reproduce at their pinned commit.
- Round-1 findings 1, 2, 3 and 5, and notes 6–15, are repaired in the
  bytes. Finding 4 is repaired in the packet but left a stale quotation in
  the ledger (finding 3).
- New in this round:
  - an internal tension in repaired (e) (finding 1);
  - an unnamed accepted-contract blocker for (a), RFC7-20 (finding 2).
