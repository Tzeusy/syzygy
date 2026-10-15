# R-DOV24-5 — confirmation review of PR #123
Verdict: REVISE
Reviewed commit: 239c098f9f612dbcf8dc1c361be5bba73ff85cdf
Manifest sha256: 0bde31ebe515831005dddbdeeb774e8f2b4c89f8c760749497544eb378f33510

Fresh-context confirmation review, 2026-10-15. Subject: the candidate package
`.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`
(SEMANTIC-DELTA.md, OWNER-DECISION-PACKET.md, IMPACT-LEDGER.md,
REVIEW-BRIEF.md, PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt, one patch under
`proposed/`) and `scripts/build_pwb_registry_loaded_profile_amendment.py`, at
the commit above. I worked in two scratch clones: `r5clone-dov24`, which I
only read and checked, and `r5mut`, which I used for mutants and reset after
each one. I edited, committed and pushed nothing in the repository.

The builder's mechanics are correct and fail closed (criteria 1–4 and 6 hold).
The verdict is REVISE because criterion 5 fails. Three of the four prose
files make false current-state claims that nothing marks. The rebase note
itself misstates what happens if the tree-framing act goes first.

## Acceptance criteria — results

**(1) The performed-successor state fails closed.** [Observed] `base_bytes`
(builder:381–383) returns the current bytes as the base only when
`sha256(body)` is in `performed_rows()`. That function (builder:341–349)
collects the rows for the subject path in each `PERFORMED_SUCCESSORS`
manifest. Today's subject hashes to `ad9cd676…` (sha256 computed by
script). That digest is the subject row of
`pwb-behavior-contract-repin/PWB-EFFECT-REPIN-MANIFEST.txt`. It is also the
argument recorded for act B at `decisions/ACCEPTANCE-ACT-RECORD.md:1088` and
`decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md:15,36`, and
it is not `.18`'s row (`2356b9ed…`). The tree-framing package's subject row,
`f9441339…`, appears nowhere under `decisions/`, so that act is unperformed.
I ran these mutants in `r5mut`, using `--check` for the S-group and
`--check`/`--selftest` for the B-group:

| Mutant | Result |
|---|---|
| S1 subject drift outside every hunk (`maxSources` 512→513) | `--check` rc=1 |
| S2 one hex character of the re-pin manifest's subject row flipped | `--check` rc=1 |
| S3 re-pin manifest deleted | `--check` rc=1 |
| S4 re-pin row's path renamed | `--check` rc=1 |
| S5 tree-framing patch applied to the subject first | `--check` rc=1 |
| S6 tree-framing removed from `DECLARED_SIBLINGS` | `--check` rc=1, "undeclared sibling patches the same subject" |
| B1 `if sha256(body) in successors` → `if successors` | `--check` passes, `--selftest` rc=1: "a performed-successor row that names other bytes passed" |
| B2 successor branch disabled | both rc=1 |
| B4 `PERFORMED_SUCCESSORS` emptied | both rc=1 |
| B5 own-row branch disabled | `--selftest` rc=1 (crash) |
| B3 subject-path filter in `performed_rows` dropped | **survives** both (finding 7) |
| B6 `apply`'s `.18 adopted` gate removed | **survives** `--selftest` (finding 7) |

I also ran `--apply --at-adoption` in `r5mut`. It wrote bytes hashing to
`0bde31eb…`. In that state `--check` passed ("this package adopted: current
bytes with this patch reversed"), `--selftest` passed (270), and a second
`--apply --at-adoption` refused ("the subject already carries this package's
bytes").

**(2) The manifest row.** [Observed] I wrote an independent script that
applies the patch with `patch(1)`, not `git apply`, to the current subject in
a temp directory. The result hashes to
`0bde31ebe515831005dddbdeeb774e8f2b4c89f8c760749497544eb378f33510`, which
equals the one row of the manifest. The patch is byte-unchanged since
`1d5966c`: `git diff --stat 1d5966c 239c098f` lists only the packet, the
manifest and the builder.

**(3) Bytes outside the hunks.** [Observed] `difflib` opcodes from the
current subject (398 lines) to the proposed bytes (691 lines) are exactly
`replace 3`, `replace 10` (`1.2.0-candidate.1` → `1.3.0-candidate.1`) and
`insert` at new lines 262–554. Neither file contains a `\u` escape, and an
`object_pairs_hook` finds no duplicate keys. Parsed, only `registryVersion`,
`observerVersion` and `observationGrammar` differ. No existing grammar key
changed, `governingBehaviorContract` (act B's re-pin) is equal, and
`discoveryVersion` is unchanged.

**(4) The builder's own modes.** [Observed, output read]
- `--check`: "manifest matches the 1 proposed subject (.18 adopted, then
  superseded by a performed act: current bytes); 6 grammar keys added, 15
  class-grammar rows, 9 container shapes, 8 extraction bindings; …".
- `--selftest`: "selftest: 270 predicates — … all fail closed".
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_docs_review_campaign_partition.py`: "total=418 assigned=418 …
  unmatched=0 overlaps=0".

Node v24.6.0. No `npm ci` was needed.

**(5) Rebase note and current-state prose.** Fails. See findings 1–4.

**(6) VIS-4.** [Observed] No 64-hex string appears in any of the package's
four Markdown files (`grep -E "[0-9a-f]{64}"`, 0 hits). No act phrase is
followed by an argument, and nothing is labelled accepted. The words
"in force" appear only in references to the registry act (see findings 1
and 2). Nothing performs, offers or records an act.

## Findings

### 1 — revise — SEMANTIC-DELTA.md has no rebase note and states a superseded act as the act in force

[Observed] The delta got no 2026-10-15 marker, and these sentences are now
false:

- SEMANTIC-DELTA.md:16–20 says the subject's "current bytes are the argument
  of the act recorded at `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
  (2026-09-05)". They are not. The current bytes `ad9cd676…` are act B's
  argument (`PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md:15`).
  Act B superseded the 2026-09-30 `.18` act, which had superseded the
  09-05 act (ACCEPTANCE-ACT-RECORD.md, act B's supersession row).
- SEMANTIC-DELTA.md:70–73: "The act in force says … 'changes travel as a new
  act' (`PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` lines 76–77)". That
  clause is found only in the 09-05 record, not in the act in force: a
  `grep -F "changes travel as a"` over the three registry act records hits
  only `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md:76`.
- SEMANTIC-DELTA.md:23–28 and 223–225 call `.18` unperformed or say
  "`.18` applied first" is needed. :232–233 reads "the `.18` act, if
  performed", which is now performed and superseded.
- SEMANTIC-DELTA.md:79–81 and 130–134 say "byte-for-byte unchanged". The
  claim holds against the current bytes, but the delta never says the base
  is the re-pinned entry rather than `.18`'s.
- SEMANTIC-DELTA.md:123 says "268 ways". The selftest now reports 270.
- SEMANTIC-DELTA.md:164–166 and 256–258 say "three independent review rounds
  each returned REVISE … The revision has not been reviewed;
  `REVIEW-BRIEF.md` states what round 4 is given". Round 4 ran, returning
  CONFIRM WITH EXCEPTIONS over `1d5966c`
  (`docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-4-RAW.md:2`). The Review
  section names rounds 1–3 only.

The delta is the normative artifact an owner act would rest on. It now names
the wrong act in force and the wrong base. Repair: add a dated marker at
each stale sentence, keeping the old text quoted (the lesson against
page-level banners in AGENTS.md).

### 2 — revise — OWNER-DECISION-PACKET.md: the rebase note marks only ".18 as pending", and several false claims fall outside even that

[Observed] The note at OWNER-DECISION-PACKET.md:14 says "Text below that
treats `.18` as pending is historical". That is one page-level marker over a
long page, the pattern AGENTS.md ("A page-level 'may be stale' banner
discharges CG-27 while a false sentence stands") says not to rely on. These
sentences are false now, and most of them do not treat `.18` as pending at
all:

- :26–29 says "**Reviewed three times, verdict REVISE each time;** … this
  revision, which has not yet been reviewed. The review record is at the end
  of this file." Four rounds ran, and the Review record (:296–357) has no
  round-4 entry. The note's own line 12 ("Round 4 cleared the bytes at
  `1d5966c`") contradicts the banner instead of marking it.
- :67–69 says "outside the two version lines and the one inserted block, the
  file is `.18`'s bytes exactly". The base is no longer `.18`'s bytes.
  `git diff f5da19ff 144fa5f7` on the subject shows act B changed
  `governingBehaviorContract.version` and `.signedBy`. The proposed file
  equals the *re-pinned* bytes outside the hunks (criterion 3), not `.18`'s.
- :129–131 says "`--apply --at-adoption` refuses unless `.18`'s bytes are
  already in place". It does not: it accepts the re-pinned bytes, because
  the performed-successor state string begins `.18 adopted` (builder:383,
  2200). I applied it successfully in `r5mut`.
- :135–140 ("Not yet offered: the argument") says "Those bytes exist only as
  the result of applying the two patches … It changes whenever `.18`'s patch
  or this one changes." The builder now applies one patch to the current
  bytes. `.18`'s patch is spent, and the row now moves when the subject's
  bytes move (the tree-framing act, for example) or when this patch changes.
  The instruction "Run `--check`, then read the row" is still correct.
- :225–226 says "the act in force draws the same line ('changes travel as a
  new act')". That quoted line is in the 09-05 record only (see finding 1).
- :90 says "268 ways". The selftest reports 270.
- :41–44, :164–173, :258–260 and :292–294 are `.18`-pending text, which the
  note does cover as "historical".

Repair: mark each sentence where it stands, and add a round-4 row to the
review record.

### 3 — revise — the rebase note's "whichever lands second is regenerated with `--write`" is false for this package

[Observed] OWNER-DECISION-PACKET.md:17–19 says that if the tree-framing
re-pin lands first, this package is "regenerated with `--write` before it is
offered". I simulated that in `r5mut`: `git apply` of
`pwb-behavior-contract-repin-tree-framing/proposed/….patch`, then `--write`.
The builder raised a traceback: "….json.patch (.18) does not apply to …".

The cause is in the builder. `PERFORMED_SUCCESSORS` (builder:76–78) lists
only the performed re-pin manifest, so the post-tree-framing subject matches
no recognised state and falls through to the `.18`-pending branch. This
patch itself still applies (`git apply --check` clean), so landing second
needs a **builder edit** (a new `PERFORMED_SUCCESSORS` entry), then
`--write`. A builder edit retires any confirmation (rule 10) and needs a
review round. Regenerating alone will not do it.

This failure is closed, so it is safe. But it bears directly on the new
owner ordering question: the note understates what tree-framing-first costs
this package. The note also says `DECLARED_SIBLINGS` makes `--check` read the
sibling "as declared, not as decided" (:19–20). That is true for
`composition_findings` only (S6). Nothing in the base-state logic handles the
tree-framing state.

### 4 — revise — IMPACT-LEDGER.md has no rebase note; its baseline and sibling table are stale

[Observed]
- IMPACT-LEDGER.md:6–14 says "The branch now sits on `96ee305`; the subject,
  the `.18` package, … are byte-identical between `08d4d02` and `96ee305`".
  The branch now sits on `b5a7e27a`. The subject changed twice after the
  baseline (`f5da19ff`, `144fa5f7`). No sentence says the name sweep was not
  re-run over the new base.
- :30–31 defines the swept population against "base bytes (current entry
  plus `.18`'s diff)". The base is now the current entry alone. The 48-name
  population is probably unchanged, because the patch is unchanged and act B
  added no key names [Inferred]. The per-name file counts were not
  re-derived at the new base [Unknown].
- Table 4 (:143–150) lists `.18`, `.25`, N8 and M15. It omits both packages
  the builder now declares in `DECLARED_SIBLINGS`: the performed re-pin,
  which is this package's base, and the unperformed tree-framing re-pin,
  which raises the new open ordering question. :147 still calls `.18` a
  pending drafting constraint.

### 5 — note — REVIEW-BRIEF.md still briefs round 4

[Observed] REVIEW-BRIEF.md:5 says "**Round 4.** Rounds 1, 2 and 3 each
returned REVISE". Criterion 4 (:72–75) says "differ from `.18`'s bytes …
diff the `.18`-applied file". Criterion 5 (:76–79) names three states and
omits the performed-successor state. This round was briefed out of band, but
the retained brief no longer describes the subject.

### 6 — note — stale builder docstrings, and a misleading diagnostic

[Observed]
- The module docstring (builder:9–19) and the `base_bytes` docstring
  (:369–372) list three states.
- `byte_findings`' docstring (:454) says "the bytes are `.18`'s".
- `composition_findings`' docstring (:1644) says "No candidate other than
  `.18` and this one".
- The selftest summary line does not name the two new predicates.

When the subject matches no recognised state (S1–S5, B2, B4), the only
diagnostic is "….patch (.18) does not apply". It fails closed, but it points
at `.18` rather than at "subject matches neither `.18`'s row nor a performed
successor's row".

### 7 — note — two builder mutants survive `--selftest`

[Observed]
- B3: drop the `path == SUBJECT.as_posix()` filter in `performed_rows`
  (builder:347–348). It is harmless today: the re-pin manifest's other row
  is the policy file's digest (`66cd41ee…`), which no registry entry can hash
  to. But the predicate has no fixture.
- B6: remove `apply`'s `if not state.startswith(".18 adopted")` gate
  (builder:2200). No selftest predicate exercises `apply`'s refusals, and the
  gate now relies on the new state string sharing that prefix. `apply` is
  unchanged since `1d5966c` [Observed, diff], so the gap is not new. The
  rebase made it load-bearing.

### 8 — note — `PERFORMED_SUCCESSORS` is trusted by declaration

[Observed] The builder treats any manifest listed in `PERFORMED_SUCCESSORS`
as performed. It never checks that the row is the argument of a recorded act.
I checked that independently (criterion 1), and it holds today. A future
edit that listed an unperformed manifest, such as the tree-framing one,
would be accepted silently; only review of the builder's diff would catch
it. One option is to cross-check `ACCEPTANCE-ACT-RECORD.md` for
`<PHRASE>: <row>`.

## Not findings

- The rebase note's facts check out [Observed]. `.18` was adopted at
  `f5da19ff`. Act B (`adopt-registry-entry`, 2026-10-02) re-pinned
  `governingBehaviorContract`. The patch applies unchanged. The row was
  re-minted. Round 4 cleared `1d5966c` (its dispositions page). The
  tree-framing package is unperformed and carries bead `syzygy-2g0d`
  (its OWNER-DECISION-PACKET.md:13).
- Round-4 notes N-A to N-F are routed to `syzygy-dov.32` and were not
  re-reviewed here.
