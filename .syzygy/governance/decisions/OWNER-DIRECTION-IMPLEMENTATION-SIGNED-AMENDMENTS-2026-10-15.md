# Owner direction — implementation of the specification amendments signed 2026-10-14, and of tree framing v1.0

Date: 2026-10-15

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in
the family of `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` and
`THREE-SURFACE-POC-MODE-DIRECTION.md` (this directory). It binds no artifact
digest, adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers nothing in
`scripts/check_governance.py`. It signs nothing, and it edits no signed
byte.

## The owner's words

[Observed: the questions and selections as the lead Claude Code session
relayed them to this lane; the owner's answers themselves are in that
session, not in this repository.] All three were given on 2026-10-15 in the
lead Claude Code session, the owner acting, by structured questions.

### 1. Implementation authorization

The question:

> Authorize implementation of today's signed spec amendments under the normal implementation workflow (bounded, reviewed, no new Butlers reads or egress)? They are P-96 anchor resolution, P-97 block provenance, P-86 class-granular extraction, P-100 governing-intent Unknowns, P-99 accessible names, and P-98 opening index once its carry-over clears.

The owner selected the option "Authorize all (Recommended)", whose text
was:

> One plain implementation direction covering exactly these amendments' signed text. I unblock their beads and run them as lanes. P-86's Q8 code change is included.

### 2. Standing autonomy direction

The owner said:

> how are there so many user questions? Majority of these seem to be entirely self-drivable by you (Opus 5.5) - as long as you run the recommended option by /th-engineering and /th-projects project-shape principles and it's good there, please follow your choices

and:

> Apply all relevant choices and unblock relevant newly-unblocked beads please

### 3. Tree-form openings (added the same day, a separate item)

The question:

> Tree-form openings (73e.20): you signed tree-framing v1.0 on 2026-10-03, but no implementation authorization covers it. Authorize implementation on the same terms as today's batch: exactly the signed text, no new Butlers reads or egress, shared-model WIP one?

The owner answered "Authorize (Recommended)".

## What is authorized

Implementation, under the normal implementation workflow, of exactly the
signed text of each amendment below. "Signed" means the version named by its
tag and its sign-off record in this directory; nothing a package's notes,
open dispositions or unasked questions would add is included.

| Register row | Amendment (tag) | Sign-off record | State on 2026-10-15 | Implementation bead |
|---|---|---|---|---|
| P-96 | PWB-REQ-014 anchor resolution (`pwb-anchor-resolution-amendment-v1.0`) | `PWB-ANCHOR-RESOLUTION-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-14; covered now | `syzygy-u05.21` |
| P-97 | POC-REQ-001 / POC-REQ-010 block provenance (`three-surface-poc-block-provenance-amendment-v1.0`) | `THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-14; covered now | `syzygy-u05.19` |
| P-86 | PWB-REQ-002 class-granular extraction (`pwb-class-granular-extraction-amendment-v1.0`), **including its Q8 code change** | `PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-14; covered now | `syzygy-dov.15.2` |
| P-100 | POC-REQ-014 governing-intent Unknowns (`three-surface-poc-governing-intent-amendment-v1.0`) | `THREE-SURFACE-POC-GOVERNING-INTENT-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-14; covered now | `syzygy-u05.20` |
| P-99 | PWB-REQ-016 accessible names (`pwb-accessible-name-amendment-v1.0`) | `PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-15 (Q1 carried to the version regenerated over P-86, round-4 notes-only); landed on `main` before this record; covered now | `syzygy-u05.22` |
| P-98 | PWB-REQ-010 opening index (`pwb-opening-index-amendment-v1.0`) | `PWB-OPENING-INDEX-AMENDMENT-SIGNOFF-v1.0.md`, **not yet present** | not signed: round-3 repairs unconfirmed pending round 4 (row P-98); **covered on landing**, as the question says, "once its carry-over clears" | `syzygy-u05.23`, held by gate `syzygy-00ls` |
| — | PWB-REQ-014 tree framing (`pwb-tree-framing-amendment-v1.0`), item 3 above | `PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-03; covered now | `syzygy-73e.20` |

The question offered P-99 among "today's signed spec amendments"; its
sign-off record landed the same day. For P-98, "covered on landing" means:
when the named sign-off record lands on `main`, the version it signs is
authorized here without a further question. A version other than v1.0, or a
sign-off that answers its packet differently from the drafted text, is still
covered only as signed. Until the record lands nothing is built for it.

**P-86's Q8 code change.** The signed order names a source two rules admit
(root index `root-index`; a pillar's index `pillar-index`; a baseline spec or
roster `butler.toml` keeps its tree rule's name and class; any other file a
pillar's index names `pillar-named-file`). Where today's code differs, a
declared pillar root nested inside another, the code is changed to the
signed order. The question names it as included.

## Bounds

Every bound here holds for every row above, item 3 included.

- **Exactly the signed text.** No requirement, scenario or behaviour beyond
  it. Not authorized: the PWB-REQ-004 delta P-86 Q6 asked for (not drafted
  or signed); the later governing-intent link amendment P-100 Q1 directs
  (it authorizes nothing now); slice D of P-99 on Trajectory, Orrery and
  home (`syzygy-k0np`, a premise check for a not-yet-drafted POC
  amendment); slices B and D of P-98; the release-label package (P-85,
  unsigned); the P-95 re-pin (a separate owner act).
- **No new Butlers content class, body read or provider egress.** Butlers
  bodies are read only as the acts in force already allow: the consented
  class `declared-project-shape-text`, behind the implementation's
  PWB-REQ-005 evaluation. P-100 reads no new work-item field. A case the
  signed text names but Butlers may not exhibit (P-86's nested pillar roots)
  is tested on a synthetic fixture, never by a new read.
- **The daemon executes no observed code.** Separate operator commands run
  tests.
- **Shared-model changes WIP one.** The rows that change the shared
  Three-Surface POC model (`packages/three-surface-poc-core`, `PocModel`)
  or are computed against its machine answer run one at a time, in the
  order the beads' dependencies fix:
  P-97 (`syzygy-u05.19`) → P-100 (`syzygy-u05.20`) → P-86
  (`syzygy-dov.15.2`) → P-96 (`syzygy-u05.21`) → tree framing
  (`syzygy-73e.20`). P-99 and P-98 are render-only and sit outside the
  chain.
- **Every lane reviewed and verified per craft-and-care.** Each signed
  oracle passes as tests whose expected values are independent of the module
  under test; each falsifier limb has a rule-6 mutant that fails; the
  battery is run at a committed tree (rule 7); a Polaris size change is
  measured against the ceiling.
- **Escalation.** A lane that finds the signed text cannot be built as
  written stops and returns to the owner: an amendment travels under
  CC-REV-2 and needs its own sign-off. No release, deployment, second
  repository, write into Butlers, or act-bound byte edit.
- **Withdrawal.** A later direction may narrow or withdraw this one;
  withdrawal defeats grant.

## The standing autonomy direction, as applied

The lead session applies item 2 as follows [Inferred: the lead session's
reading, relayed to this lane]: sub-questions inside a packet and process
choices are decided by the lead, taking the recommended arm after checking
it against the `/th-engineering` and `/th-projects` project-shape bars;
final binding acts (signing a version, adopting a doctrine clause,
authorizing implementation) still go to the owner, batched. This record
adds no reading of its own and authorizes nothing by item 2.
