# Owner sitting brief — "generate a Polaris dossier for redis/redis"

> **Candidate — binds nothing.** Drafted 2026-10-07 under bead `syzygy-qkea`.
> This page routes; it is never authority. It performs no act, quotes no
> digest and repeats no record's bytes: each decision below names the packet
> that owns it, and that packet, its review and its record win over anything
> said here. Pull-request states are as of 2026-10-07 and go stale; the pull
> request owns its state. Nothing here may be offered until a fresh-context
> review of these bytes returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes
> only. PR #370's package was cleared at `d19ec98b` by its round 3
> (CONFIRM WITH EXCEPTIONS, notes only; its `ROUND-3-DISPOSITIONS.md` carries
> the notes); this page routes to those bytes.

## What one sitting can and cannot do

The goal is that you can say "generate a Polaris dossier for redis/redis" and
your own Claude Code or Codex session writes it from a local clone while
Syzygy pins, checks and renders it, with no provider call by Syzygy (the
local-agent mode, version 1.0 signed off 2026-10-06).

One sitting can give every owner decision that run needs. It cannot make the
run work by itself:

- [Observed, 2026-10-07] Most of the `syzygy dossier` implementation is not
  written. Of the epic `syzygy-qkea`, slice S1 is closed; S2 (the reader, PR
  #367, open), S4 and S5 are in progress; S3 and S6 to S12 are open. The
  dossier gate that reads your act records is S3.
- [Observed] The post-sitting installer on `main`,
  `scripts/install_redis_sitting.py`, is written for the provider-mode
  sitting of PR #260: it refuses unless records for the psf/requests
  consent, the provider-mode Git adapter, a provider route and an egress
  consent exist (`REQUIRED_RECORDS` and `missing_records()`). A local-agent
  sitting gives none of those, so that installer refuses as it stands. A
  local-agent variant is engineering work, not an act, tracked as
  `syzygy-qkea.16`.
- [Observed, 2026-10-07] PR #370 (the local-agent acts) cleared review round
  3 over its package at `d19ec98b`, notes only, and is not yet merged; its
  rows are offered from those bytes, in its table order, consent first.

Everything provider-mode stays parked and is not asked: PR #260 rows 2a and
2b (route and API key), 3a and 3b (the fetching Git adapter, replaced by
item E below), 4 (psf/requests), 6 and 8 (egress), and 11 (standing
direction). Your agent's sends to its own provider are your act, not
Syzygy's (mode direction, item 2).

## The decisions, in the order you would be asked

| # | Decision | Owning packet | Needed for a Redis dossier? |
|---|---|---|---|
| A | Redis observation consent | PR #370 row 1 (the same record as PR #260 row 5) | Yes |
| B | Public-source screening scope, version 1, with its Q2 to Q8 | `public-source-screening-scope/OWNER-DECISION-PACKET.md`; PR #260 row 1 | Yes |
| C | RFC5-14 `project-documentation` class | `rfc5-project-documentation-class/OWNER-DECISION-PACKET.md`; PR #260 row 7 | Only for D |
| D | Screening scope version 2 (README and guides readable) | `public-source-screening-scope-v2/OWNER-DECISION-PACKET.md`; PR #260 row 12 | Strongly, see D |
| E | Source-acquisition entry, signed as package v1.0 | PR #370 row 2 | Yes |
| F | "Redis has no kernel evidence drawer", or a provider statement | PR #370 rows 3, 3a, 3b | Yes, one of them |
| G | D9 bound to exact bytes | PR #370 row 4 | Only if the agent may build and run Redis |
| H | Your RFC7-20 reading bound to exact bytes | PR #370 row 5 | Yes, or the dossier has no narrative |
| I | The non-governed narrative profile (requirement 032) | `non-governed-narrative-profile/OWNER-DECISION-PACKET.md`; PR #260 rows 9a to 9d | Yes |
| J | Rulings: altitude order, advantages, page budget | PR #260 rows 10a to 10c | No; defaults apply |
| K | Local-agent mode version 1.1, its questions 1, 3 and 4 | `polaris-dossier-local-agent-mode-v1-1/OWNER-DECISION-PACKET.md` (merged in PR #368) | No; 1.0 stays in force |
| L | D9 note N6 (version 1.1 question 2) | the same packet; `DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md` | No |
| M | `syzygy-4mbu`, the test-capture tool that runs a project's tests itself | bead `syzygy-4mbu` | No; a standing nonconformance |

Paths without a directory are under `.syzygy/governance/contracts/candidates/`.
Each act is separate and separately revocable; none implies another.

"The option at the manifest row" means a structured question whose option
names the record at its row of the package manifest; selecting it is the act
and you type no phrase or digest. The recorder writes your question opening,
option label and description verbatim, so the words given below are the
words that would be recorded.

### A. Redis observation consent

- **Signing unlocks:** Syzygy may read the Git objects of the four consented
  Redis commits, and nothing else of Redis.
- **Declining costs:** no Redis run of any kind; every Redis claim is Unknown.
- **Two things to know** (PR #370 row 1): make the clone as the record says,
  one consented commit fetched alone into an empty repository, because your
  agent reads whatever the clone holds; and the record's SEC-3 line predates
  D9 and is read as governing Syzygy's reads only (queued as `syzygy-i5qt`).
- **Recommended:** sign.
- **Your words:** option "Sign it" on the question naming the Redis
  observation consent at its manifest row.

### B. Screening scope, version 1

The policy act that decides which files of a public repository Syzygy reads
at all, and what it withholds. The local-agent mode refuses a run without it
(proposal, "Syzygy's own reads keep every gate").

- **Signing unlocks:** source code of a consented public repository becomes
  readable by Syzygy, so quotations from it can be checked.
- **Declining costs:** no public body is read; nothing after it matters.
- **Its questions** (the packet owns the text; recommendations are the
  packet's):
  - Q1, sign: yes.
  - Q2, read-gate continuation: widen it to the list the simulation
    produces. The act alone makes the Butlers read gate refuse the new
    policy; the re-pin is made in the recording commit. Declining Q2 means
    the act should not be recorded at all.
  - Q3, source extensions: accept.
  - Q4, order against PR #120: [Observed, 2026-10-07] PR #120 is open and not
    offered at this sitting, so "this one alone".
  - Q5, the narrowing: accept.
  - Q6, active content unchanged: accept.
  - Q7, exclusion reasons are whatever `GENERATION_EXCLUSION_REASONS` holds:
    confirm. [Observed] The constant is on `main` (PR #278, merged
    2026-10-03).
  - Q8, the run-profile carrier: defer. [Inferred] In the local-agent mode
    Syzygy sends no request, so the carrier is not on this run's path.
- **Your words:** option "Sign it, with Q2 to Q8 as recommended" on the
  question naming the policy at its manifest row.

### C. The RFC5-14 `project-documentation` class

A contract amendment adding a seventh content class. It matters here only
because version 2 of the screening scope (D) maps that class and is
refused while the amendment is not in force.

- **Signing unlocks:** D can be performed.
- **Declining costs:** D cannot be performed; README, guides and licence
  files stay unreadable to Syzygy.
- **Its two questions** (the packet's): the act form, where the packet
  recommends form 1, the option at the manifest row; and the bound sentence
  in the generation change's `SOURCE-POLICY.md` that lists six classes and
  turns false on adoption, where the packet does not choose. [Inferred]
  Recommended: direct a readability successor for it, because a false
  present-tense sentence on a default reading path is the failure this
  repository repairs at the sentence, not around it.
- **Recommended:** sign, in form 1.
- **Your words:** option "Sign it, at the manifest row; direct the
  SOURCE-POLICY.md readability successor".

### D. Screening scope, version 2

- **Signing unlocks:** Syzygy may read the README, changelog, contribution
  and licence files and the guides under a top-level docs folder.
  [Inferred] Requirement 032 rests a declared capability on what the
  maintainers wrote down, and Syzygy checks every quotation against objects
  it read, so without D the agent may quote the README but the quotation
  cannot be verified, and the catalog leans on code and Unknown.
- **Declining costs:** the dossier runs on code and tree only; the
  maintainers' own account of the project is unverifiable.
- **Its state** (PR #260 row 12; [Observed] at `main`): round 6 returned
  REVISE on one generated sentence; the repair (commit `e7ad7934`) is
  unreviewed, and there is no round 7 without you. The recorder records only
  a confirming review.
- **Recommended:** ask for round 7 now, before the sitting, so that D can be
  signed in it; then sign variant "none" (Q1), with Q3 to Q5 at the packet's
  defaults. Order is fact: B, then C, then D.
- **Your words now:** "Run round 7 on screening scope version 2." **At the
  sitting:** option "Sign it, variant none" on the question naming that
  variant's manifest row.

### E. The source-acquisition entry, signed as package v1.0

The registered way Syzygy reads your clone: in process, no refs, hooks or
configuration honoured, no process started, every object re-hashed.

- **Signing unlocks:** the reader becomes the one registered adapter; without
  it every read is refused before an object is opened.
- **Declining costs:** no read; a later sitting for this one act.
- **To know** (PR #370 row 2): signing extends the Scope A direction of
  2026-10-02 to a public-source entry for the first time. It also approves
  declarations (source limits, screening, failure display) that belong to the
  gate, which is not written yet. No read happens without the gate, so
  signing now is safe in that sense, but any change the gate forces into the
  entry needs a new version and a new sign-off. The install refuses until PR
  #367 merges.
- **Offered only after PR #367 merges.** Round 3 of PR #370's review (note
  4) found that the entry's implementation version names the reader "as
  merged" but is bound to no reader bytes, and the reader changed under it
  before merge. Signing before the merge would approve a version whose code
  is still moving. If PR #367 has not merged by the sitting, this row waits;
  nothing else in this brief depends on its timing except step 7 below.
- **Recommended:** sign, once PR #367 has merged.
- **Your words:** option "Extend Scope A to this entry and sign v1.0". The
  recorder refuses a label that does not contain "Extend Scope A".

### F. The drawer statement

A project counts as governed if Syzygy holds a kernel evidence drawer for it,
or its tree has any `openspec/` or `.syzygy/` path. A silent input counts as
governed, so something must be signed either way.

- **Signing unlocks:** with the statement, the brief can be issued to any
  agent without a per-provider consent, provided the pinned tree has neither
  path. With 3a or 3b, Claude Code or Codex may receive Redis content even if
  Redis counts as governed.
- **Declining costs:** no brief for Redis.
- **Recommended:** "No drawer (Recommended)" alone. It is true [Inferred],
  one record serves every agent, and it fails closed: if the tree does hold
  such a path, the run refuses and says so. [Inferred] Redis's tree has
  neither (general knowledge; nothing has been read, as no read is
  authorised).
- **Your words:** option "No drawer (Recommended)".

### G. D9 bound to exact bytes

- **Signing unlocks:** the brief may tell your attended authoring session it
  may build and run Redis, once you also record a choice for that one run.
  Signing alone runs nothing.
- **Declining costs:** every brief says not to build or run Redis outside an
  execution profile; the dossier still works, on reading alone.
- **To know** (PR #370 rows 4 and 5): it binds the whole current
  `security.md` and `v1.md`, so any later edit to either, even an unrelated
  one, unmatches the record and briefs fall back to SEC-3's rule until you
  sign a new version. Wider still (PR #370 round 3, note 1): once any act of
  that package is recorded, an edit to any file a record binds turns every
  one of its recorders' `--check` red, not only the record it touches, until
  a successor package is drafted; the failure is closed. Two readings are
  new: that your words adopted D9 and
  this act only binds it to bytes for the check, and that an act over a
  record listing digests binds the files it lists.
- **Recommended:** sign, in keeping with your choice of D9; it costs nothing
  until a run's own choice is recorded.
- **Your words:** option "Sign it" on the D9 in-force record.

### H. Your RFC7-20 reading bound to exact bytes

- **Signing unlocks:** your agent's draft is shown as an editorial draft.
- **Declining costs:** the draft layer renders Unknown; source pages and
  disclosures stay readable, so the dossier has no narrative.
- **To know:** on 2026-10-05 you chose "No extra record"; the mode's review
  (note R3-F8) later required every such ruling to rest on an owner act, so
  this asks for one record after all. It binds item 1 of the direction only,
  whole-file, at the cost described under G. The trade-off you made (a
  reviewer may call the reading a contract change) is kept, not settled.
- **Recommended:** sign.
- **Your words:** option "Sign it" on the RFC7-20 reading in-force record.

### I. The non-governed narrative profile (requirement 032)

How a dossier reads for a repository with no Syzygy declarations. The
version 1.0 proposal says "A Redis dossier needs both" (032 and the
local-agent mode). Cleared at review round 3 with notes only.

- **Signing unlocks:** a dossier-shaped page for Redis has a specification
  basis: declared capabilities from maintainer-written text, deep dives with
  an honest line for the reality band, and the maintainers' words as a
  byte-exact anchor beside an honest leaf line.
- **Declining costs:** a thin, predominantly Unknown narrative, which is the
  correct output under requirement 004 today.
- **Its questions** (the packet's, with its recommendations): O1 the leaf is
  an honest line and the maintainer span is the anchor; O2 the reality-band
  omission stands; O3 a structured option selection naming the package,
  stating whether Scope A is read to cover it; O4 the spec moves to
  `specs/` with the recount tooling as part of the act; O5 the glossary is
  deferred; O6 maintainer documentation counts as the project's own shape
  documents under RFC1-14; O7 a source object is an evidence artifact under
  RFC7-10. Two known limitations sit in the specification bytes; you may sign
  as they stand or ask for one more round. [Inferred] Sign as they stand:
  row F's statement makes the input state the absence, which is the case the
  first limitation's proposed wording names.
- **Recommended:** adopt, O1 to O7 as recommended, Scope A not read to cover
  it, the two limitations standing. [Inferred] The packet leaves the Scope A
  reading to you; "not read to cover it" keeps Scope A to what it names, and
  the profile's recorder needs no Scope A reading either way.
- **Your words:** option "Adopt as recommended" with the description "O1 to
  O7 as the packet recommends; Scope A is not read to cover it; the two known
  limitations stand." The recorder refuses a description carrying a digest.

### J. Rulings with no bytes

Plain directions; no review needed; each has a lawful default.

- **10a, altitude order.** Default: the V0 order RFC7-13 names. Recommended:
  give no ruling now.
- **10b, advantages.** Maintainer-stated only, or also external comparison
  sources. Recommended: maintainer-stated only. [Inferred] Syzygy can check a
  quotation only against objects it pinned, so an external source would
  render as the agent's unverified report.
- **10c, page budget.** Recommended: defer to the first measured run.
- **Your words:** "10a no ruling; 10b maintainer-stated only; 10c after the
  first run."

### K. Local-agent mode version 1.1 (questions 1, 3, 4)

Version 1.1 writes the 1.0 review notes and D9's dossier note into the
specification so a build that skips them no longer conforms. It adds no
permission. Review round 2 returned CONFIRM WITH EXCEPTIONS, notes only; the
notes are dispositioned in `POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-REVIEW-NOTES.md`.

**Two corrections to the packet, which is review-frozen and not edited:**

- **Question 1 says** "no check in the battery can tell 1.0's signed bytes
  from 1.1's". That stopped being true when PR #368 merged on 2026-10-06: the
  v1.0 builder's `--check`, which is in the status battery, now fails when
  the installed dossier bytes are not those of the latest recorded sign-off,
  and the v1.1 builder and the recorder's v1.1 entry exist. Your sign-off is
  no longer the only guard. [Observed at `be724397`.]
- **Question 2 quotes D9** as saying your per-run choice "names what the
  instruction covers". D9's adopted text reads "the owner has recorded a
  choice for that one run, naming what the instruction covers"
  (`security.md`, SEC-3); note 3 of the notes record carries the same
  correction. The meaning the question relies on is unchanged.

The questions:

- **Q1, sign off 1.1.** Unlocks: the credential, declaration and
  status-sentence duties become specification text. Declining: 1.0 stays in
  force and the implementation carries the same items as duties.
  Recommended: (a) sign.
- **Q3, D9 note N2: the credential condition as a standing cost.** Unlocks
  nothing new; it costs nothing until Syzygy holds an adapter credential, and
  then that credential is kept from your user account permanently. Ruling
  otherwise holds 1.1 for a redraft. Recommended: (a) accept.
- **Q4, D9 note N1: what counts as one run.** Recommended: (a) leave it to
  each feature's specification, each bounding a run by one session, a named
  scope and an end. Defining it in doctrine is new doctrine text with its own
  review.

### L. D9 note N6 (version 1.1 question 2)

D9's named scope limits what Syzygy tells the agent, not what the session
does; a session that runs more does not break SEC-3. The note asks that the
run record flag every reported command outside the named scope, so overreach
is visible rather than forbidden.

- **Taking it unlocks:** flags on commands the agent reports outside the
  clone, with no location, or out of scope. A flag blocks and hides nothing,
  and cannot catch an out-of-scope command the agent ran inside the clone and
  called in scope.
- **Leaving it out costs:** commands are still listed; nothing is flagged.
- **Recommended:** (a) take the hunk, in keeping with your choice of
  disclosure over containment. It is recorded as the recorder's `n6` option.

**Your words for K and L together** (the packet's own line): "1.1 signed off
with N6; N1 and N2 as recommended."

### M. `syzygy-4mbu`, the test-capture tool

`npm run poc:capture-test-artifact` is Syzygy code that runs Butlers' pytest
itself, with the caller's environment and no execution profile. [Inferred,
from the bead and the D9 review] That breaks SEC-3 and RFC5-18 today and
stays forbidden under D9, whose permitted case is an agent session, not
Syzygy's own process. It is not on the Redis path; it is here because the
bead waits on your direction and no code may change before it.

- **Options:** retire the tool; make it print the pytest command for you to
  run and ingest only the result file you hand it; or route it through an
  execution profile, which needs the profile contract no act has accepted.
- **Recommended:** [Inferred] print the command. It keeps the test-artifact
  evidence obtainable and matches the standing rule that separate operator
  commands, never Syzygy, run observed code.
- **Your words:** "4mbu: print the command for me to run, and ingest only the
  result."

## If you accept every recommendation

"Accept every recommendation in the Redis local-agent sitting brief: run
round 7 on screening scope version 2 now; at the sitting sign A, B with Q2 to
Q8 as recommended, C at the manifest row with the SOURCE-POLICY.md successor,
D variant none, E extending Scope A once PR #367 has merged, F no drawer, G, H, and I as recommended;
10a no ruling, 10b maintainer-stated only, 10c after the first run; 1.1
signed off with N6, N1 and N2 as recommended; 4mbu: print the command."

## After the sitting, in order

Nothing in this list is an act; each step records or applies only what you
gave. Each recorder takes `--date`, `--question-opening`,
`--selection-label`, `--selection-description` and, where the act joins a
chain, `--instant`; give instants in increasing order. Every recorder has a
`--check` with the same arguments.

1. **Version 1.1 sign-off, its own commit** (K and L). Independent of every
   other row; rehearsed on `main` both with and without `n6`.
   `scripts/record_versioned_signoff.py --record polaris-dossier-local-agent-mode --version 1.1`
   with `--option n6`, then `scripts/check_spec_reconciliation.py --regenerate`,
   then blocks 2 to 6 of `POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-SIGNOFF-ROUTE-EDITS.txt`.
2. **Preconditions, no act:** round 7 of D confirms; PR #370 merges after
   its review clears; PR #367 merges; the local-agent installer exists (see
   "What one sitting can and cannot do").
3. **Screening scope v1** (B):
   `scripts/record_public_source_screening_scope_act.py --record <row>`.
4. **RFC5-14 class** (C):
   `scripts/record_rfc5_project_documentation_act.py --record <row>`.
5. **Screening scope v2** (D):
   `scripts/record_public_source_screening_scope_v2_act.py`, at the chosen
   variant's row. Steps 3 to 5 must run in this order; the Butlers re-pin is
   made once, against the final policy bytes, by the installer.
6. **Redis observation consent** (A):
   `scripts/record_public_repo_admission_acts.py --record redis-observation <row>`.
7. **Source-acquisition entry** (E):
   `scripts/record_versioned_signoff.py --record public-git-source-acquisition-local-agent --version 1.0`.
8. **Local-agent records** (F, G, H): the recorder
   record_dossier_local_agent_acts.py, which lands with PR #370, with keys
   `redis-no-evidence-drawer`, `d9-in-force` and `rfc7-20-reading-in-force`.
   Never run that package's builder with `--write` once any of its acts is
   recorded (round 3, note 1). The recorder's printed "add the
   performed-act registration" line is stale (note 3): run
   `scripts/check_governance.py` instead.
9. **Narrative profile** (I): `scripts/record_narrative_profile_adoption.py --record`.
10. **Install, one commit with every record from steps 3 to 9:** the
    local-agent installer (to be written), doing what the existing
    installer's `registrations`, `rfc5`, `policy`, `profile` and `reconcile`
    steps do for the records a local-agent sitting produces, plus the CG-26
    lines for each new `--check`.
11. **Verify:** the battery of `PROJECT-STATUS.md` §"How to verify this page"
    and the full Vitest suite.

[Unknown] Steps 3 to 10 have not been rehearsed together, and the existing
rehearsal (`scripts/simulate_redis_sitting.py`) covers neither PR #370's
recorders nor version 1.1. Rehearse in a scratch clone before the sitting.
The order of steps 1 and 9 matters for the status page's composition figure:
the installer's profile step already handles a profile installed after a
signed dossier addition, which is why version 1.1 goes first.

## What this brief does not do

It performs no act, adopts nothing, and changes no doctrine, contract,
specification, policy or performed act. It grants no read, egress, write or
execution. It does not offer the provider-mode rows of PR #260.
