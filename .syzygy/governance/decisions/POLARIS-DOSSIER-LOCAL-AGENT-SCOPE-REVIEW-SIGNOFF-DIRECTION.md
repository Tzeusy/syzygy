# Owner direction — local-agent dossiers: repository scope, review independence, sign-off form

Date: 2026-10-05

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`

This direction follows `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md` and
`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`, given the same day. It is
a plain owner direction: it binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It signs nothing off. The
amendment it shapes binds only on the owner's later sign-off (VIS-4).

## The owner's words

On 2026-10-05, in the Claude Code CLI, the owner answered three structured
questions raised by the draft of the `polaris-dossier-local-agent-mode`
amendment (draft PR #353). The options the owner selected are reproduced
below with their descriptions as shown.

**Q1.** "Should the local-agent dossier mode be limited to observed,
non-governed repositories (e.g. redis/redis), never your own governed
projects?"

| Label | Description |
|---|---|
| "Any repo" | "Also usable on governed projects (e.g. Syzygy itself, Butlers); their content would then reach your agent's provider without a Syzygy egress record." |

The option not taken was "Observed repos only (Recommended)".

**Q2.** "How independent must the fresh-context fidelity review be?"

| Label | Description |
|---|---|
| "Separate session (Recommended)" | "A second top-level Claude Code/Codex session you start, given only the draft, cited spans and criteria; its declared session id must differ from the author's. A subagent spawned by the authoring session does not count." |

**Q3.** "How do you want to sign off the spec amendment once it's reviewed?"

| Label | Description |
|---|---|
| "Option pick, v1.0 (Recommended)" | "You select 'sign off polaris-dossier-local-agent-mode v1.0' and in the same choice extend the version-tag sign-off scope to Polaris generator spec deltas, so later deltas (incl. the narrative profile) use the same light ceremony." |

## The direction

1. **Scope.** The local-agent mode may be used on any repository the operator
   holds the required consents for, governed projects included.
   - SEC-2 is unchanged by this direction. It requires "explicit, recorded,
     per-project consent" before governed-project content reaches a model
     provider.
   - Reconciling Q1 with SEC-2 is left to the amendment and its review: for
     example, a recorded per-project statement for governed projects only.
   - Preserved trade-off: the owner chose "Any repo" over the recommended
     restriction. A reviewer who finds that this reaches doctrine should
     report it, not resolve it.
2. **Review independence.** The fresh-context fidelity review runs in a
   separate top-level session that the operator starts. That session is given
   only the draft, the cited spans and the criteria, and its declared session
   id must differ from the author's. A subagent spawned by the authoring
   session does not satisfy the review.
3. **Sign-off form.** The reviewed amendment is offered as an option
   selection naming `polaris-dossier-local-agent-mode` v1.0. The same
   selection is to state that version-tag sign-off extends to Polaris
   generator specification deltas. That extension takes effect only when the
   owner makes that selection. This record does not extend
   `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` by itself.
