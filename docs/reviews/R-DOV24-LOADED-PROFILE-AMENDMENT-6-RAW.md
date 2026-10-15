# R-DOV24-6 — confirmation review of the dov.24 package on main
Verdict: REVISE
Reviewed commit: fa9bc47e414d96c389e815ea51d29988baeeb44f
Manifest sha256: 0bde31ebe515831005dddbdeeb774e8f2b4c89f8c760749497544eb378f33510

Fresh-context confirmation review, 2026-10-15. Subject: the candidate package
`.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`,
`scripts/build_pwb_registry_loaded_profile_amendment.py`, and the P-112 row
of `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`, at the commit
above. Work was done in two scratch clones: `r6clone`, which I only read and
ran checks in, and `r6mut`, which I used for mutants and reset after each one
(`git checkout -- .` and `git clean -fd`). My scripts are in a separate
`r6tools/` directory. I edited, committed and pushed nothing in the
repository.

The repair of every round-5 finding holds against the bytes, and the
builder's new predicates do what the packet says. The verdict is REVISE
because of one new revise finding, in the P-112 register row, which this
round is the first to review (finding 1). Every other exception is a note.

## Acceptance criteria — results

**(1) Round-5 findings against the bytes.** [Observed] Each one is checked
below, against the files and not against the disposition table
(OWNER-DECISION-PACKET.md:401–410).

- R5-1 (delta). Every sentence round 5 named now has a dated mark beside
  it, and the old text is kept: SEMANTIC-DELTA.md:20–26 (act in force and
  base), :41–47 (`.18` stacking, plus the tree-framing cost), :85–89 (the
  "changes travel as a new act" quotation attributed to the superseded
  09-05 record), :139–140 ("268" → 278), :151–152 ("after the diff" base),
  :184–186 and :282–283 (the unreviewed claims), :245–247 (downstream
  item 3), :256 (supersession), :261–262 (`--apply`). The Review section
  gains rounds 4 and 5 (:285–294). I confirmed the facts in the marks.
  `git diff --stat f5da19ff 144fa5f7` on the subject shows 2 lines changed,
  and the subject has no commit after `144fa5f7` (`git log`). The act B
  record's line 20 supersedes the 2026-09-30 act. Resolved.
- R5-2 (packet). Every sentence round 5 named is marked where it stands:
  :38–41 (review banner), :82–83 ("`.18`'s bytes exactly"), :106 (278),
  :146–149 (`--apply` and the act in force), :159–162 (two patches),
  :251–252 (the act-in-force quotation). So are the sentences the old
  page-level marker had covered: :56–57, :190–192, :287, :322. The
  page-level sentence is gone from the note (:3–29), and the round-4 entry
  is at :387–392. Resolved.
- R5-3 (the tree-framing-first cost). The note now says that this builder
  fails closed until a `PERFORMED_SUCCESSORS` entry is added, which is a
  builder edit plus a review round, and only then `--write`. It also says
  `DECLARED_SIBLINGS` only silences the composition check (:23–28). I
  re-ran the simulation in `r6mut`: `git apply` of the tree-framing
  registry patch (rc 0), then `--check` rc=1 and `--write` rc=1, both with
  the new diagnostic "the subject hashes to neither .18's row, a performed
  successor's recorded row nor this package's row, and treating .18 as
  pending fails: …". The note is accurate. Resolved.
- R5-4 (ledger). IMPACT-LEDGER.md:16–24 marks the baseline paragraph stale
  and names `b5a7e27a`, `f5da19ff` and `144fa5f7`. It labels the 48-name
  population [Inferred] and per-name counts at the new base [Unknown], and
  it explicitly retires the "current entry plus `.18`'s diff" definition
  that :40–41 still carries. Table 4 gains the performed re-pin (:158) and
  the tree-framing re-pin (:159), and the `.18` row is marked (:157).
  Resolved.
- R5-5 (brief). REVIEW-BRIEF.md:3–15 is a dated head note saying the brief
  is the round-4 brief and naming the four states. Resolved, but see
  finding 3.
- R5-6 (docstrings and diagnostic). The module docstring (builder:15–23),
  the `base_bytes` docstring (:392–399), `byte_findings` (:487) and
  `composition_findings` (:1677) are updated, and the selftest summary names
  the new predicates. The new diagnostic is observed above. Resolved.
- R5-7 (B3, B6). See criterion 2. B3 is killed. Every form of B6 inside
  the gate is killed, but one form at `apply`'s call site survives
  (finding 2).
- R5-8 (`PERFORMED_SUCCESSORS` trusted by declaration). `performed_rows`
  now keeps a row only if `path == SUBJECT.as_posix() and digest in record`
  (builder:365–366), where `record` is `ACCEPTANCE-ACT-RECORD.md`. The
  packet discloses that this is a substring test (:410). In `r6mut` I
  replaced act B's digest (its only occurrence, ACCEPTANCE-ACT-RECORD.md:1088)
  with 64 zeros. `--check` and `--apply --at-adoption` then both failed
  closed (rc=1, with the no-state diagnostic). Resolved.

**(2) The builder's modes, and mutation.** [Observed, output read]
- `--check` (rc 0): "manifest matches the 1 proposed subject (.18 adopted,
  then superseded by a performed act: current bytes); 6 grammar keys
  added, 15 class-grammar rows, 9 container shapes, 8 extraction bindings;
  … the observer's code reads the profile-built files as the profile says".
- `--selftest` (rc 0): "selftest: 278 predicates — base-state composition
  (.18 pending, .18 adopted and superseded by a recorded performed act, path
  and record filters, the exact --apply gate, … all fail closed". The count
  is 270 + 3 `performed_rows` predicates + 5 gate states = 278, which
  matches the diff `239c098f..fa9bc47e`.
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".

Mutants, one at a time in `r6mut` (each `str.replace` asserted to match
exactly once, and the builder restored after each):

| Mutant | old → new | `--check` | `--selftest` |
|---|---|---|---|
| B3 drop path filter | `if path == SUBJECT.as_posix() and digest in record` → `if digest in record` | rc 0 | rc 1 "a performed-successor row for another path counted" — **killed** |
| B3b drop record filter | same line → `if path == SUBJECT.as_posix()` | rc 0 | rc 1 "an unrecorded performed-successor row counted" — killed |
| B6b old prefix gate | `if state not in APPLICABLE:` → `if not state.startswith('.18 adopted'):` | rc 0 | rc 1 "misjudged the state '.18 adopted-ish: forged'" — **killed** |
| B6c PENDING applicable | `APPLICABLE = frozenset({PRIOR_ADOPTED, SUPERSEDED})` → `…, PENDING})` | rc 0 | rc 1 — killed |
| B6d gate removed in `apply_refusal` | `if state not in APPLICABLE:` → `if False:` | rc 0 | rc 1 (pending and forged states) — killed |
| B6e SUPERSEDED dropped | `APPLICABLE` → `frozenset({PRIOR_ADOPTED})` | rc 0 | rc 1 — killed |
| B1 any successor | `if sha256(body) in successors:` → `if successors:` | rc 0 | rc 1 "a performed-successor row that names other bytes passed" — killed |
| **B6a `apply` ignores the refusal** | `refusal = apply_refusal(state)\n    if refusal:` → `…\n    if False:` | rc 0 | **rc 0, survives** (finding 2) |

So a performed-successor row counts only for the subject's path and only
when the record quotes it, and `apply_refusal` is an exact membership test
over `{PRIOR_ADOPTED, SUPERSEDED}` [Observed].

Live states in `r6mut`: `--apply --at-adoption` wrote bytes hashing to
`0bde31eb…`. In that state `--check` (rc 0) reported "this package adopted:
current bytes with this patch reversed" and `--selftest` passed (278). A
second `--apply --at-adoption` refused ("the subject already carries this
package's bytes"), and `--apply` without the flag refused (rc 2).

**(3) The manifest row.** [Observed] My independent script
(`r6tools/derive.py`) copied the current subject to a temp directory and
applied the patch with `patch(1)`, not `git apply`. It returned rc 0 and
SHA-256 `0bde31ebe515831005dddbdeeb774e8f2b4c89f8c760749497544eb378f33510`,
which equals the manifest's single row. The current subject hashes to
`ad9cd6769bffbb1a3ef94625c73226dec133fb7c9f1e0bc40186b09b15e165fa`. That is
act B's argument and occurs exactly once in the acceptance record (line
1088), and the proposed digest occurs there 0 times. `difflib` opcodes
from current to proposed are `replace 2–3`, `replace 9–10` and `insert`
at 261 (new lines 262–554), 398 → 691 lines, the same three hunks round 5
found. `git diff --stat 239c098f fa9bc47e` over the subject, this
package's directory, both re-pin packages and the `.18` package lists only
this package's four Markdown files. The patch, manifest and subject are
unchanged.

**(4) Current-state prose.** No unmarked false claim remains in the four
package files from round 5's list. See finding 1 for the P-112 row and
finding 3 for one sentence this review itself made false.

**(5) VIS-4.** [Observed] `grep -cE "[0-9a-f]{64}"` returns 0 for each of
the four Markdown files. The packet says "**It is not offered here**"
(:64). The P-112 row says "**the current bytes are unconfirmed, and the act
is not offered**. No ruling is recorded". Its kind column reads "owner act
(one digest act), not offered". Nothing performs, offers or records an
act, and nothing is labelled accepted. The register recount at
PENDING-OWNER-DECISIONS.md:1209–1216 is right: 28 open, 5 acceptance-act,
33 rows, 33 distinct, one P-112 row (`r6tools/count.py`, regex
`^\| (P-[0-9]+[^ |]*)` per `##` section).

## Findings

### 1 — revise — the P-112 row miscounts the packet's questions and omits question 9

PENDING-OWNER-DECISIONS.md:1306 says: "The packet asks nine open questions:
the eight original ones (N8 fold-in; wait for slice 5 limbs 1–4,
recommended; the P-74 "edited on no arm" reading; `discoveryVersion`;
version numbers; heading literals; a continuation direction; the `.18`
merge, now moot) and, added 2026-10-15, the order against the unperformed
tree-framing re-pin (P-95), with no recommendation."

[Observed] The packet's "Open questions this package did not resolve"
section numbers **nine** questions (OWNER-DECISION-PACKET.md:219–308). The
row's eight items map to questions 1–8. Question 9 is left out: "Should
this entry say anything about root independence before M15's delta
does?" (:288). It carries a recommended arm (keep the clause, :303) and
names a later registry act if M15's arm is adopted. The ordering question
in the rebase note (:17–29) is a tenth. So the packet asks ten questions,
not nine, and the register's one-line summary of what the owner is asked
drops the M15 overlap.

This row is new in this change, so no earlier round reviewed it. It is a
false current-state claim in the owner-facing register (criterion 4).
Repair: say "ten open questions: the nine numbered ones (…, root
independence against M15, recommended keep the clause) and the ordering
question". Then recount nothing else; the row count does not change.

### 2 — note — B6's call-site form survives: `apply` itself is never exercised

builder:2264–2266 (`refusal = apply_refusal(state)` / `if refusal:` /
`print(refusal); return 1`).

[Observed] With `if refusal:` replaced by `if False:`, `--check` and
`--selftest` both pass (278 predicates). The new predicates test
`apply_refusal` directly (builder:1810–1814), so the gate is exact, but no
predicate shows that `apply` consults it. Round 5's B6 removed the gate at
exactly this site. The repaired code moved the test into a helper, and
the helper's mutants are killed (B6b–B6e). The disposition's "Both mutants
were re-run against the new selftest and are killed" (OWNER-DECISION-PACKET.md:409)
is therefore true of the gate's logic but not of `apply`'s use of it
[Inferred: the original mutant text no longer exists, so the disposition
could only re-run an analogue]. I verified the real path live: `apply`
refused in the adopted state and in the unrecorded state. The residual is
only that a future edit dropping the call would not be caught. Optional
repair: a selftest predicate that runs `apply(True)` against a temp root in
a non-applicable state and asserts rc 1 and an unchanged subject.

### 3 — note — "no round 6 is dispatched" is false now that this round runs

OWNER-DECISION-PACKET.md:15 and :412–413; SEMANTIC-DELTA.md:293–294;
REVIEW-BRIEF.md:13; PENDING-OWNER-DECISIONS.md:1306 ("Under the stopping
rule no round 6 was dispatched").

[Observed] This is round 6, briefed out of band over `fa9bc47e`. The
sentences were true when written and could not have been marked in
advance. They are not a repair defect. The round-6 disposition should
mark each one where it stands, keeping the text quoted and dated, and say
what this round found. The same applies to REVIEW-BRIEF.md:3–15, which
still briefs round 4's criteria for a fifth time.

### 4 — note — the entry's behaviour-contract pin trails the specification, and the packet does not say so

[Observed] The subject's `governingBehaviorContract.version` (subject:20)
is `sha256:0d50f8f4…`, act B's pin to the readability-successor sign-off.
The PWB specification has since taken four version-tagged sign-offs
(`4b2c75bd`, `7f43802f`, `235b71eb`, `029947a1`). The tree-framing
builder's own `--check` reports the current spec as `sha256:c3ea81d9…`
and calls its package stale. This package keeps the pin unchanged, which
is correct for a restatement. But performing this act first would
re-adopt a pin four sign-offs behind the current specification. The
rebase note's ordering question (:17–29) names the tree-framing re-pin
only as "itself stale and to be redrafted", not the pin lag that is the
reason the order matters [Inferred]. The builder's specification witness
does read the current spec and passes, so no heading literal is affected.
Optional: one sentence in the ordering question.

## Not findings

- The rebase-note facts re-check [Observed]. Act B's record line 20
  supersedes the 2026-09-30 `.18` act. The 09-05 record alone carries
  "changes travel as a new act". Act B moved only two lines.
- Question 7's "`.18` needs one (`syzygy-dov.19`)" is still true:
  `OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md:100` keeps
  the currency and briefing fields gated on `syzygy-dov.19` [Observed].
- The other main-line changes between `239c098f` and `fa9bc47e`, including
  93 changed lines in the PWB spec and 18 lines in the acceptance record,
  do not break the builder. `--check`'s specification witness passes at
  the reviewed commit [Observed].
- Round-4 notes N-A to N-F remain routed to `syzygy-dov.32` and were not
  re-reviewed.
