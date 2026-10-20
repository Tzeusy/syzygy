# Fresh round-3 review brief — one-command Polaris dossier run

> **Candidate — binds nothing.** One independent review of the frozen repair.
> The lead selected this bounded cycle; this is not an owner direction.

## Subject and result

Read the full six-requirement candidate and its coherent supporting prose.
The expected full commit is supplied in the review dispatch: verify it with
`git rev-parse HEAD` before reading, and record that full commit in the raw.
The subject spec SHA-256, scripted from these exact bytes, is:

`9d984c99afc4f825ee5210875f016f807b965522badf68ee116a42aa724d1267`

Compare it independently before reviewing. A later edit retires this review
binding. The subject includes `proposal.md`, `design.md`, `OWNER-PACKET.md`,
`tasks.md`, `proposed/polaris-generation/spec.md` and `ROUND-3-REPAIRS.md` in
this directory. Read the retained rounds 1 and 2 and their disposition
records for closure; the present record does not overwrite their verdicts.

Return one exact verdict, `PASS` or `REVISE`, with findings tied to exact
current text. Include the full reviewed commit and subject SHA-256, restate
the intent and constraints as a fresh reader, assess each N1–N7 and n1–n10
proposed repair separately, and identify any material new defect. Notes may
accompany `PASS`; a material unresolved defect requires `REVISE`. Preserve
uncertainty as Unknown. The author does not retain or edit the raw; the lead
stores it unchanged and records the disposition.

## Governing inputs

Use the owning text, not a summary or status banner:

- `.syzygy/governance/doctrine/vision.md`: VIS-1/2/3/4.
- `.syzygy/governance/doctrine/security.md`: SEC-2/3/5, especially SEC-3's
  "every process Syzygy launches" and "Syzygy never gives the instruction
  to a session it started" boundaries.
- `.syzygy/governance/doctrine/trust-and-evidence.md`: evidence and labels.
- `.syzygy/governance/decisions/POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`.
- `.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`.
- `.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15.md`.
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`.
- `.syzygy/governance/decisions/POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`.
- `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`:
  signed REQ-033 and 035 text, including the stored-record rule and waiting
  sessions. No predecessor bytes are edited by this candidate.
- `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:
  CC-REV-2/4/5/6/7; `engineering-bar.md`: CC-BAR-2/3/5.
- `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:
  CC-SPEC-1 through 11, whose in-force status is owned by craft act 6 and
  its amendments. Review scenarios and Form blocks as a proposed contract,
  not as evidence of implemented behaviour.

## Exact acceptance criteria

1. **N1, n8:** Every view excludes the Syzygy checkout and gate records,
   aliases and mounted ancestors included. The minimal shim supplies only
   the allowed role command protocol; those commands run in the supervisor
   outside the view and cannot return forbidden checkout content. Every
   target-derived delivery kind is screened and limited to the statement's
   classes; a blocked delivery does not silently widen consent. Author and
   inventory clone reads remain the separately disclosed operator act.
2. **N2, n4, n5:** Every launch-record field, including view digest, login,
   managed settings, exclusions and controls, is Observed only in output as
   the launching step makes the launch. A later display from stored records
   is Inferred. REQ-033's stored-record rule is not displaced; the exact
   write-reach quotation and writable `drafts/` exception are correct.
3. **N3, n1, n2, n7, n9:** Real-tool enforcement of each exclusion, fixed
   permission, execution limit and auxiliary-traffic control requires
   per-executable-digest and per-version independent evidence from an
   operator-started attended synthetic probe outside a launched run.
   Stand-ins establish invocation/refusal, not real-tool enforcement. No
   such evidence means refusal, including before login-status can open
   auxiliary connections. Unknown controls are not accepted by disclosure
   alone. Permission widening is forbidden attached or detached; both Claude
   bypass flags are named. Configuration-home variables are set only to the
   private home, not inherited; no credential variable passes. The first
   probe itself receives no new permission from this candidate.
4. **N6:** Full launch checks run before every session start, replacements
   and resumed starts included. Changed executable/version, login, managed
   settings, exclusions, limits, permissions, auxiliary controls or host
   view refuse that start and stop the run; no stored preflight substitutes.
5. **N7, n4:** A helper starts before delivery, including when an input
   already exists at resume, and obtains it through the waiting command.
   The signed "new terminal only" sentence is explicitly displaced only
   for launched runs; operator-started runs keep their signed meaning.
6. **N4, n3, n6:** REQ-040 names its own refusals. Every active design slice
   follows the required operator-provided `--clone`; no Syzygy clone/fetch
   is proposed. Proposal and owner packet disclose that this prerequisite
   costs a separate preparation command. The lead's restrictive choice is
   not represented as an owner answer or as achieving the stronger literal
   goal of no preparation command.
7. **N5, n5, n10:** Prototype limitations disclose default author tools,
   ambient MCP, each helper's general Bash under auto mode, the checkout
   mount and absent restrictions. They are historical source observations,
   not current runtime verification. The external Redis and bubblewrap
   observations remain Unknown at the claims. Supporting prose and review
   checkboxes agree with the repaired contract; completion of a review is
   not clearance.
8. **Coherence:** The six identities are retained. Scenarios and Form blocks
   make the new refusal, restart, delivery and label boundaries observable
   with independent oracles. Assess the whole candidate for contradiction,
   including broker delivery versus isolation, per-role clone reach, and
   preflight versus resume; do not rely only on the repair table.
9. **Authority and process:** No installed or bound bytes, prior disposition
   record or raw reviewer output changes. No target read, source fetch,
   provider call, real-tool probe, runtime implementation, new consent or
   owner act occurs. The bounded restart is the lead's process choice. The
   separate runner's round-5 direction is not treated as this cycle's
   authority. Confirm the stated evidence, privacy/egress, secrets and
   observed-code-execution risk floors.
10. **Mechanical evidence limits:** Inspect the author's current logs for
    authoring structure, authority sweep, unchanged protected files and the
    canonical battery run in a clean clone at the frozen commit. The generic
    `--authoring` check reports the same five inherited multiple-paragraph
    ordering errors over six IDs at baseline and candidate, as documented
    in `ROUND-3-REPAIRS.md`; judge this convention and the separate exact
    structure inspection openly rather than calling that check passing. Mechanical
    checks do not establish real-tool restrictions, product readiness,
    semantic approval or owner adoption. The existing design-bar,
    dependency-union and impact-ledger tasks remain visible as later gates.

## Review scope

Use only this repository's candidate, governing references and retained
reviews, plus the recorded mechanical evidence. Relevant prototype source
may be inspected to check the limitation statements. Do not read a target
repository or dossier state root, start a local agent CLI or daemon, call a
provider, make a real-tool probe, execute observed code, implement, adopt or
sign anything. No further reviewer or repair cycle is authorized here.
