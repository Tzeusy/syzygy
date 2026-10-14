# Polaris dossier local-agent mode — version-tagged sign-off v1.2

Date: 2026-10-14

Owner: Tzeusy

Package: polaris-dossier-local-agent-mode

Version: 1.2

Tag: polaris-dossier-local-agent-mode-v1.2

Kind: specification delta

Owner selection: The owner, 2026-10-14T03:32:23.826Z (2026-10-14 UTC), in a structured question in the lead session (relayed by the lead), answered the question "Sign version 1.2 of the dossier local-agent-mode spec? This is your P-107 choice ("B, reviewer may continue") written out as spec. At run start you open the three helper sessions (inventory, fidelity review, design review) once. Each waits for its packet and then runs unattended. Each may only read its own folder (inventory: also the clone) and run its one `syzygy dossier await` command. It hands in its result through that command, and Syzygy writes the file. Edit, Write, web, subagent and MCP tools are blocked, and the Claude Code tool set is limited to Read, Glob, Grep and Bash. Nothing runs Redis code. A reviewer may carry on across repair rounds, and the page says so. Three review rounds; the last was CONFIRM WITH EXCEPTIONS, notes only. Remaining limits, shown on the run page: (1) allow rules in your own ~/.claude or project settings still apply inside these sessions; a flag that could switch them off exists, and I'll evaluate it as a follow-up; (2) the v1.2 switch can be forged by anything that can write Syzygy's checkout; (3) a Codex session follows your ~/.codex config approval policy." by selecting the option "Sign version 1.2 (Recommended)". The owner selected the offered option; the words were not typed.

Review: docs/reviews/R-PR408-WAITING-SESSIONS-4-RAW.md

Reviewed commit: a3cdb3e644258561e1630eae0436905819e0ddb8

Review verdict: CONFIRM WITH EXCEPTIONS

Disposition: docs/reviews/R-PR408-WAITING-SESSIONS-4-NOTES.md

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.2 of `.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-2` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `polaris-dossier-local-agent-mode-v1.2` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
