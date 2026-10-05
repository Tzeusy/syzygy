# Owner direction — local-agent dossiers: rulings on the first amendment review

Date: 2026-10-05

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`

This direction follows the three `POLARIS-DOSSIER-LOCAL-AGENT-*` directions
given the same day. It answers the three findings that the first
fresh-context review of draft PR #353 reported for the owner (findings 6, 7
and 8; verdict REVISE, reviewed commit `dc85c278`).

It is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It does not amend
doctrine: item 1 directs that a doctrine amendment be drafted, and only the
owner's adoption act binds one (VIS-4).

## Correction disclosed to the owner

The earlier question on code execution
(`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`, Q2) stated "SEC-3 only
binds Syzygy's own execution". That was the lead's reading, not the
doctrine's text. Before asking again, the lead told the owner so and quoted
SEC-3: "Observed code is untrusted, everywhere. Observed-project code runs
only inside an explicit, opt-in execution profile."

## The owner's words

On 2026-10-05, in the Claude Code CLI, the owner answered three structured
questions. For each, the selected option is reproduced with its description
as shown.

**Q1.** "SEC-3 (doctrine): 'Observed code is untrusted, everywhere … runs
only inside an explicit, opt-in execution profile.' Should the dossier brief
let your agent build/run the target project?"

| Label | Description |
|---|---|
| "Allow on host, amend SEC-3" | "Keep your earlier choice; it then needs a doctrine amendment to SEC-3 (a separate owner adoption act), drafted and reviewed before the dossier mode can be signed." |

Options not taken: "Only in a sandbox (Recommended)" and "Forbid, disclose".

**Q2.** "For your own governed projects (Syzygy, Butlers), the reviewer
notes: the per-project provider statement can't actually limit what the
agent reads or sends (it reads freely), secrets SEC-5 would withhold could
reach the provider, and that statement is arguably a Syzygy egress record
after all. How should governed projects be handled?"

| Label | Description |
|---|---|
| "Keep any repo, disclose" | "Governed projects allowed with the per-project statement; the spec states plainly that class limits and secret screening don't bind the agent's own sends, and that the statement is a consent record. Reviewer will likely re-raise SEC-2 'scoped' and SEC-5." |

Option not taken: "Public repos for now (Recommended)".

**Q3.** "RFC7-20 ('absent SEC-2 named-provider consent [a draft] is not
computed'): the reviewer finds your 'only Syzygy-computed drafts' reading
changes the clause's effect, but offers a cleaner basis — for non-governed
repos SEC-2 doesn't apply, so the condition never bites; for governed repos
the per-project statement IS the consent. Which basis should the spec rest
on?"

| Label | Description |
|---|---|
| "Keep my ruling" | "Spec keeps resting on 'RFC7-20 governs drafts Syzygy computes', with the reviewer's finding that this changes the clause's effect recorded for you." |

Option not taken: "Reviewer's basis (Recommended)".

## The direction

1. **SEC-3.** The owner keeps "Allow, disclose" for the operator's agent
   session, on the host, and directs that an amendment to SEC-3 be drafted
   and reviewed to permit it.
   - The local-agent amendment may not be signed until that doctrine
     amendment has been adopted by the owner's act.
   - Until then, nothing in the dossier mode may tell an agent to run
     observed code outside an execution profile.
2. **Governed projects.** The mode stays usable on any repository. For
   governed projects the per-project provider statement is required, and the
   specification states plainly that:
   - class limits and secret screening (SEC-5) do not bind the agent's own
     reads and sends;
   - the statement is a consent record.

   The owner chose this over limiting the mode to public repositories,
   expecting the SEC-2 "scoped" and SEC-5 questions to be raised again.
3. **RFC7-20.** The specification keeps resting on the owner's reading in
   `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md` item 1. The review's
   finding that the reading changes the clause's effect is recorded for the
   owner and preserved, not resolved.
