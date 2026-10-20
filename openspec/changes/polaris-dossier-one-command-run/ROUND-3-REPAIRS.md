# Round 3 repair — one-command Polaris dossier run

> **Candidate — binds nothing.** One bounded source-design repair, chosen
> by the lead on 2026-10-20. It performs no owner act and grants no effect.
> Tracking bead: `syzygy-fl2g`.

[Observed] Round 2 returned `REVISE` over commit
`5f026d9cadacba639454d4e4d393d63174267810`; its output is retained unchanged
at `docs/reviews/R-POLARIS-DOSSIER-ONE-COMMAND-RUN-2-RAW.md`. The prior lane's
stop is retained unchanged in `ROUND-2-DISPOSITIONS.md`. This record is a
sibling, not a revision of that disposition or either raw review.

## Source-design decision

CC-REV-4 says, "Two failed review rounds signal upstream ambiguity — return
to the source decision, don't polish prose." The lead returned to the
source design and selected one restrictive repair plus one fresh round 3.
This is the lead's process choice within candidate drafting, not an owner
direction, an extension of the separate runner's round-5 direction, or a
sign-off. If round 3 returns `REVISE`, this bounded cycle ends with retained
raw output, dispositions and a report; no further repair is included.

[Inferred] The source directions require an explicit local CLI subprocess,
keep the provider routes parked and grant no new consent. The candidate
therefore removes unneeded checkout exposure and refuses an unobserved CLI
restriction instead of seeking a wider egress ruling. It keeps the
operator-prepared clone. These decisions narrow the proposed mechanism;
they neither implement it nor reinterpret the owner's provider ruling to
cover auxiliary traffic.

## Finding map

Each row is the drafter's proposed disposition. Closure remains for the
fresh reviewer to judge against the repaired bytes, governing sources and
`REVIEW-BRIEF-ROUND-3.md`.

| Finding | Candidate repair and observable boundary |
|---|---|
| N1 | REQ-042 removes the Syzygy checkout and gate records from every role view, including aliases and mounted ancestors. Only a minimal command shim remains; allowed role commands execute through the supervisor outside the view. The scenario and falsifier cover read, list and write attempts and content leaking through the shim or broker. |
| N2 | REQ-042 and 045 apply REQ-041's live/stored rule to view digests, login and managed-settings checks, exclusions, controls and launch metadata. Observed is limited to launching-step output as it makes the launch; later displays from records are Inferred. Proposal, design and owner packet follow. |
| N3 | REQ-045 requires tool controls that disable auxiliary telemetry, error reporting, update checks and other non-provider traffic, with independently observed real-tool evidence for the executable digest and version. Missing or unobserved controls refuse before even login-status. No auxiliary egress act is inferred or requested. |
| N4 | Design slice 4 checks the operator's `--clone` instead of fetching; slice 8 requires that clone and the real-tool evidence before an attended run. |
| N5 | The prototype limitations name the author's default general Bash, WebFetch, WebSearch and ambient MCP, the missing tool-limit flags, every helper's general Bash under auto mode, and the checkout exposure. A private configuration home is not presented as proof of exclusions. These are retained source observations, not a prototype run in this repair. |
| N6 | REQ-040, 042, 044 and 045 require fresh host-view, executable/digest/version, login, managed-settings, exclusion, tool-limit, fixed-permission and auxiliary-control checks before every session start, replacements and resume included. Stored preflight is no substitute; a failure stops the run. |
| N7 | REQ-041 starts each helper before input is delivered to it, including a fresh session on resume. Existing input may precede that launch; delivery still passes through the unchanged waiting command. |
| n1 | Fixed permissions apply attached as well as detached. The mode must deny widening beyond the role's pre-approved tools; `dontAsk` stays unobserved until evidence establishes it. `--allow-dangerously-skip-permissions` is named among forbidden flags. The REQ-043 falsifier covers widening while attached. |
| n2 | The first real-tool observation comes from an operator-started attended synthetic probe outside a launched run, with independent tool-use, settings and per-process network observations. It grants no probe or egress authority. A stand-in cannot establish real-tool enforcement; until evidence exists, runs refuse. |
| n3 | REQ-040's refusal sentence includes "of this requirement". |
| n4 | REQ-042 quotes "lie within the agent sessions' write reach" exactly, substitutes absence from the view for gate records, and excepts the author's writable `drafts/` when describing state-directory write reach. REQ-041 also names the signed "new terminal only" sentence it displaces for launched sessions. |
| n5 | The owner packet's live/stored distinction, the proposal's automatic-approval refusals, and completed review checkboxes follow the repaired spec. Review completion is not clearance. |
| n6 | The lead keeps `--clone`. Proposal and owner packet disclose that the operator must make it first and that the one command covers orchestration after this prerequisite. No Syzygy-made source fetch or new owner answer is implied. |
| n7 | Syzygy sets `HOME` and the declared tool's `CLAUDE_CONFIG_DIR` or `CODEX_HOME` only to its private configuration home. They are not inherited; no credential or provider-route variable passes. |
| n8 | The content-class and screening limits cover every target-derived input Syzygy delivers: packets, briefs, instructions, named guidance and brokered command output. An unlisted-class delivery refuses; this does not refuse the agent's own permitted clone reads. |
| n9 | REQ-044's Oracle distinguishes a stand-in's observation of the requested invocation from actual tool enforcement, which rests on the separate per-version attended-probe evidence. |
| n10 | The historical Redis figures and bubblewrap observation are marked Unknown at the claims in the proposal and owner packet. External evidence was not read. The prior raw reviews and repair records remain unchanged. |

## Amendment funnel and limits

[Observed] Baseline: `origin/main` at
`3d03f693a52328cf03804f4f5ecb15236617ce15`, containing the folded six-requirement
candidate. Syzygy uses its `.syzygy/` doctrine, decisions, contracts, map and
craft policies; no alternate `about/` authority is introduced.

[Inferred] This is a medium boundary correction to the same motif: one
operator-triggered dossier workflow with independently isolated helper
sessions. Gate 2 alignment is with VIS-1/2/3/4 and SEC-2/3/5; missing evidence
refuses and owner sign-off remains the only binding step. Gates 3–4 change
only the proposed role views, broker delivery and preflight design in
`design.md`. Gates 5–6 retain REQ-040 through 045 and add observable refusal,
resume and label cases with independent verification oracles. No new runtime
interface is implemented. The attended-view design is unchanged; its
pre-existing design-bar task remains visible in `tasks.md`.

The touched risk floors are evidence truthfulness, privacy/egress, secrets
and observed-code execution. Review must confirm that the draft preserves
them. No installed specification, owner act, source-acquisition authority or
provider route is changed. The candidate's first real-tool probe, launch,
source fetch and sign-off are not performed by this repair.

## Mechanical authoring limitation

[Observed] The generic `th-projects` checker, run with `--authoring` on an
exact-byte isolated copy, finds six requirements and six IDs but reports
five ordering errors. The baseline candidate has the same five errors: the
generic parser requires metadata after one normative paragraph, while
these requirements use the repository's multiple-paragraph normative body
followed by contiguous `ID`, `Source`, `Scope` and then scenarios. This
repair retains that readable local convention and reports the generic check
as failing, not waived or passing. A separate structural inspection checks
the complete normative bodies, metadata, scenarios, exact predecessor
quotations, unchanged warrants and identity uniqueness; it does not certify
semantic correctness or implementation. No adopted identity is renamed.
