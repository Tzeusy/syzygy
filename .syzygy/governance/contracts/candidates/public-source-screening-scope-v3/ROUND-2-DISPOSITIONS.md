# Round-2 dispositions — public-source screening scope, version 3

> **Candidate — binds nothing.** This record dispositions review notes. It
> performs no act, approves nothing and changes no reviewed byte.

Review: `docs/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2-RAW.md`, verdict
`CONFIRM WITH EXCEPTIONS` (raw line 4), over commit `5db1dd72`. The raw's
head names the manifest file it read; cite it from there. All round-1
findings are repaired. Round 2 has three findings, each marked `note`, and
none marked revise. Under the owner's notes-only rule
(`decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), that round
clears the package at its manifest. The notes are recorded here, and the
package prose (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`) is left as reviewed.
Where a note corrects a sentence, read the sentence as this record says.

Reviewed record: docs/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-2-RAW.md

*(Added 2026-10-08 at install: the line above and the numbered headings
below are the form `scripts/record_public_source_screening_scope_v3_act.py`
reads, through `record_versioned_signoff.validate_disposition`; no
disposition changed. Each heading kept its words after the number. The
install outcome of each note is in "Install notes" at the end.)*

## 1 — Install requirement — the Redis sitting installer must learn version 3 (note 1)

**This is an install-time requirement, and the owner should read it beside
the act.** The installer that would carry out the install refuses after a
version-3 act. It fails closed, so the gate stays where version 2 left it,
but nothing re-points until the code below changes.

[Observed, re-derived 2026-10-08 at this branch's head]
`scripts/install_redis_sitting.py` knows only versions 1 and 2:

- `policy_acts` (`:877`) reads only the version-1 act (`SCOPE_ACT`, `:118`,
  read at `:880`) and the version-2 act (`V2_ACT`, `:121`, read at `:883`).
  It then refuses unless the policy on disk hashes to the final act's
  argument. After a version-3 act, the policy hashes to version 3's row, so
  this step refuses.
- `gate_comment` (`:918`) knows only `final.key == "v2"` (`:920`) and
  otherwise writes version 1's comment.
- `step_policy` applies `policy_cg_v2_edits` (`:715`) only when
  `final.key == "v2"` (`:941`). That function writes the version-2
  `check_governance` chain link and nothing for a third version.
- The battery edit (`battery_lines`, `:743`; `edit_battery`, `:760`) takes
  its recorder script from those two acts only.

`scripts/simulate_redis_sitting.py` hard-codes the version-2 recorder
(`V2_RECORDER` at `:96`, and the row-12 call at `:529`). The ledger lists
that script only as "[Unknown at drafting]".

**Read `IMPACT-LEDGER.md` lines 22–25 as follows.** The ledger says the
installer "derives" the re-pointed set from the recorded act at the sitting.
That holds only after the installer learns version 3. The version-3 install
needs one of two things:

- `policy_acts`, `gate_comment`, `policy_cg_v2_edits`, the battery edit and
  the simulator taught version 3, in the install commit or before it; or
- a hand-written install change that does not run through that installer.

The install also needs the rest of the ledger's list: the third
`POLICY_ACT_FORMS` form (`syzygy-fxro`), the two consumers, the battery
lines and the CG-7e historical pinning.

Separately, and not caused by this package, the installer's `--selftest`
holds 74 of 77 predicates today [Observed: run 2026-10-08 in a fresh clone
of `5db1dd72`]. The three that fail are "chain edits: one version-2 row, one
offering, the version-1 manifest gated, one exemption", "chain edits: the
argument quoted is version 1's", and "chain edits: version 2 without version
1 is refused". Repair them before the installer is extended.

## 2 — Note 2 — "page" is defined by parser (residual)

`renderCondition` defines a page as "a document an HTML or SVG parser
reads". Two kinds of document fall outside that definition while still being
able to run markup [Inferred by the reviewer]:

- a document served as `application/xhtml+xml`, which an XML parser reads;
- a Markdown file a viewer later renders to HTML.

Either would fall to `egress`. There `renderRule` still forbids minting an
element or handler, but no CSP is required. No such destination exists
today: the reviewer's file-writer sweep found the site emits `.html` pages
and `.json` files only.

**Disposition.** This is a stated residual of the reviewed bytes. Any
consumer change that adds an XHTML-served or rendered-Markdown destination
for an exempt body should be reviewed against it. A successor policy should
carry the reviewer's wording: "a document an HTML, XHTML or SVG parser
reads, or any document a consumer renders to one".

## 3 — Note 3 — attribution and wording slips

- `IMPACT-LEDGER.md` line 11 ("round-1 review finding 7") and line 119
  ("round-1 review, finding 5") cite the decision packet's round-1 review.
  **Read as:** findings 7 and 5 of
  `docs/reviews/R-PR404-DOSSIER-BLOCKERS-1-RAW.md`, not of this package's own
  round 1 (`R-PUBLIC-SOURCE-SCREENING-SCOPE-V3-1-RAW.md`).
- `SEMANTIC-DELTA.md` lines 150–151 say both page builders "emit the meta
  first in `<head>`". It is the third element, after the charset and
  viewport metas. **Read as:** "in `<head>`, before `<title>` and any body
  bytes", which is the property `renderCondition` needs.

## Install notes

*(Added at install, in the commit that records the version-3 act. The
notes above are unchanged; this says what the install did with each.)*

- **Note 1, taken.** `scripts/install_redis_sitting.py` now reads version 3:
  - `policy_acts` reads version 3 after version 2. It refuses version 3
    without version 2, a version 3 recorded at or before version 2's
    instant, version 3 carrying version 2's argument, a version-3 record
    that does not name version 2, and a policy not at version 3's bytes.
  - `gate_comment` names version 3 and version 2's date.
  - `policy_cg_v3_edits` writes the `check_governance` chain link:
    - version 2's chosen row becomes history;
    - the amendment registries learn a `variant-row` offering shape, since
      every version-2 manifest row ends in its `[variant: …]` tag;
    - the version-2 manifest's current registration is gated off;
    - the version-3 record's manifest heading becomes a checked exemption.
  - The battery edit replaces whichever earlier scope recorder's two lines
    it finds. Its `--check` line carries version 3's packet words.
  - A new `--only` flag runs named steps without the original sitting's
    full record set. That record set was never all performed on this
    tree, so the install ran `--only policy,reconcile`. The local-agent
    sitting's installer composes the same steps.

  `scripts/simulate_redis_sitting.py` records version 3 after version 2
  (`--v3-variant`, default `all`).

  The three failing chain-edit predicates failed only because the live
  `check_governance.py` already carries the version-1 and version-2 links,
  so the edits had nothing to add. They now run on a pre-install fixture
  (`PRE_INSTALL_CG`). The version-3 edit is also run on the live file.

  The rest of the ledger's list is in the same commit:
  - the third `POLICY_ACT_FORMS` form (`syzygy-fxro`);
  - both screens, through the shared `codeContentExempt`;
  - the render condition. The dossier's `render.ts` scans an exempt body as
    before when the pages cannot be confirmed. The app's page sinks are held
    to it by `page-sink.test.ts`.
- **Note 2, residual stands.** The install adds no page destination. The
  sinks are still the dossier renderer and the draft preview, both `.html`
  pages under the policy's CSP.
- **Note 3, unchanged.** Read the two sentences as stated above.
