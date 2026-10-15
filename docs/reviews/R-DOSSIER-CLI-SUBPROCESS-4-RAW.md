# Review R-DOSSIER-CLI-SUBPROCESS-4
Reviewed commit: 7a6ef22cf9e619f6330d01c78dc5716a3030683b
Subject SHA-256: 5e97168892b4a8011d1b90ba13d33607cf6350a34b560186e23a72efaace5760
Verdict: REVISE

Reviewer: fresh-context reviewer, not the author. Round 4 is a confirming round over repaired bytes.
Brief: `.syzygy/governance/contracts/candidates/dossier-local-cli-subprocess-runner/REVIEW-BRIEF.md`, Round 1 section
(its stopping-rule sentence is excepted, per dispatch). Focus: the egress and trust boundary.
Companion read: `.syzygy/governance/decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`,
sha256 da3a6726e1c668ef8a57a19e8093bf9f8fe9a792d446e83df83757d1577751c7. I computed it with sha256sum and it matches
the dispatch.

## What was checked

- [Observed] `git rev-parse HEAD` returns 7a6ef22cf9e619f6330d01c78dc5716a3030683b. The `sha256sum` values of the
  subject and of the companion both equal the dispatch's values.
- [Observed] Read in full: the subject, the companion, the brief, the round-3 raw, `ROUND-3-DISPOSITIONS.md` and
  `ROUND-3-REPAIRS.md`.
- [Observed] I read `git diff` of the subject from the round-3 commit d0f776d8e584fa188674fa7f47053253027c776b to HEAD
  in full. The changed lines are :138, :140 (one added sentence), :144, :174, :178-179, :202, :218, :220, :222, :249,
  :316-317 and the Review section :358-366.
- [Observed] To look for residue I ran a fixed-string sweep of the subject for "declared credential", "pass-through",
  "one declared", "credential variable" and "authenticated through". There were 10 hits: :138, :174, :202, :218,
  :220, :222, :249, :317, :359 and :362. Each of them either states the new "no credential variable" rule or
  describes round-3 history in the Review section. None keeps the removed exception alive: the name-only record, the
  unparsed pass-through, the page disclosure, the "every value other than" digest carve-out and the Case's "declared
  credential variable" are all gone.
- [Observed] I ran `claude --help` on this host. The `--bare` text quoted at :249 ("Anthropic auth is strictly
  ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read)") and the `--restricted` and
  `--safe-mode` quotations at :247 and :250 match. I did not re-run `codex exec --help`, because no Codex row changed.
- Not read, per the dispatch: any target repository, state root or run directory. I ran no `syzygy` command and no
  npm or node script, and made no network call.

## Round-3 finding closure

| # | Class | Status | Reason |
|---|---|---|---|
| 1 | revise | closed | :138 "from an allow-list that admits no variable selecting, redirecting or authenticating a model provider, with no exception: no credential variable passes to the tool, and the tool authenticates only through its own credential file, the operator's local login". The unchecked declared input is gone instead of being guarded. Where the tool needs something else, the run fails closed: "Where the declared tool and version cannot authenticate from that file alone, Syzygy SHALL refuse the launched run, naming the failure" (:138). These lines agree with it: scenario :174 ("no credential variable is among them"), Case :218 ("a provider credential variable"), Falsifier :222 ("a provider-redirecting variable or option, or any credential variable, reaches the tool"), the `--bare` row :249 and Downstream :316-317 ("pass no credential variable"). |
| 2 | note | not closed (partly repaired) | The repair landed at :202 ("the read-only inspection of the managed settings' provider-relevant keys, whose values are never recorded or passed on"), at :220 ("excepting exactly two uses: the copy of the tool's own credential file, and the read-only inspection ...") and at :222 ("a credential read other than the two excepted uses"). These now agree with each other. The finding also asked for the same exception in paragraph 1, which was not done: :138 still reads "Syzygy SHALL read no provider credential except to copy the tool's own credential file". See new finding 2. |
| 3 | note | closed | Scenario :178 adds "or the managed layer's provider-relevant keys for the declared tool and version are not known". :179 adds "or the unknown version". Case :218 adds "presented for a tool version whose provider-relevant managed keys are not known". Falsifier :222 adds "or have provider-relevant keys not known for the declared version". The raw's [Unknown] about managed settings kept somewhere other than a file is still Unknown, and still depends on how "locations the declared tool and version documents" (:140) is read. |
| 4 | note | carried to the owner (no repair due) | :336-344 is unchanged and leaves the arm to P-111 Q2. It is restated as new finding 5. |

## New findings

1. [revise] The round-3 repair left the provider-selecting-option bar without a modal verb. SEMANTIC-DELTA.md:138
   now reads, as a sentence of its own: "Every provider-selecting option of the tool (such as a configuration
   profile, a configuration override, or a local or third-party provider switch) either absent or set by Syzygy to
   the declared provider." [Observed] In the round-3 bytes this clause was part of a sentence governed by "The
   allow-list SHALL admit nothing else ..., and every provider-selecting option ...". The repair deleted that
   governing clause, so this sentence has no SHALL and no verb. [Observed] It is the only SHALL-text carrier of the
   bar on Codex's `-p, --profile`, `-c, --config`, `--oss` and `--local-provider`. The flag table cites it as that
   authority at :255 ("Provider-selecting: absent, or set by Syzygy to the declared provider (REQ-045 first
   paragraph)"). [Inferred] These options can redirect the session to a provider or endpoint that no agent-provider
   statement covers, so this is an egress bar (brief item 1). Scenario :173 and Falsifier :222 ("a
   provider-redirecting variable or option ... reaches the tool") still state the intent. But round 3 finding 1 held
   that a scenario and a falsifier give the build no duty unless the SHALL text gives one, and the same standard
   applies here. The intent is not in doubt, and the repair is one word: "Every provider-selecting option ... SHALL
   be either absent or set by Syzygy to the declared provider."

2. [note] Paragraph 1 and paragraph 2 still conflict over the managed-settings read. Paragraph 1 (:138) reads:
   "Syzygy SHALL read no provider credential except to copy the tool's own credential file". Paragraph 2 (:140) reads:
   "Syzygy SHALL read ... only the keys that can select, redirect or authenticate a model provider, its environment
   block included" and "a key's value is used only to decide a mismatch". [Inferred] A managed environment block can
   hold a credential value, so reading it to decide a mismatch is a read of a provider credential that :138 does not
   except. The scenario (:202), the Oracle (:220) and the Falsifier (:222) now allow it, so a test would not fire on a
   conforming build. Only the SHALL texts disagree. It opens no egress. Repair: add the read-only inspection to the
   exception at :138. Alternatively, say in :140 that authenticating keys are matched by name and presence only, with
   their values left unread.

3. [note] A managed authenticating key for the *declared* provider is not refused, and :138 and :174 then overstate.
   :140 refuses only where a key "names or could select a provider, endpoint or credential route other than the
   declared provider". [Inferred] Suppose managed settings carry an API key or an API-key helper for the declared
   provider (Anthropic for `claude`). That is not a mismatch under :140 as written, so the run proceeds. The tool
   then authenticates through the administrator's key rather than "only through its own credential file, the
   operator's local login" (:138). Scenario :174 asserts the same thing ("the tool authenticates only through its own
   credential file"). [Inferred] Transmission still goes to the declared tool and provider, so it stays inside the
   statement. [Unknown] Whether the statement in force scopes the account as well as the tool and provider. The
   managed layer is already disclosed as not excluded (:140), so this is a note. Repair: either treat any managed
   authenticating key as a mismatch, since paragraph 1 admits only the credential file, or qualify :138 and :174 by
   the managed-settings disclosure.

4. [note] The new authentication refusal at :138 has no test and no timing. The sentence is "Where the declared tool
   and version cannot authenticate from that file alone, Syzygy SHALL refuse the launched run, naming the failure".
   [Observed] No scenario, Case (:218) or Falsifier (:222) clause exercises it, for example with a credential file
   that is absent or keychain-only, or a tool whose login is not file-based. [Observed] It also says neither when the
   check runs (the sibling binary refusal at :142 says "Before `init`") nor how "cannot authenticate" is decided.
   [Inferred] The arm fails closed in direction, and an unauthenticated session transmits nothing, so this is a note.
   Repair: add "before any session starts" and a Case that seeds a missing credential file, with the matching
   Falsifier clause and Unknown wording.

5. [note] The choice of arm is the owner's alone (P-111 Q2) and is unchanged. Direction :99-101 says content goes
   through a launched CLI "only where an act already in force covers that repository, that content class and that
   agent tool with its provider". The drafted arm at :146 lets unlisted classes go with a disclosure, and states that
   the trade-off rests on `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` item 2 and the one-command run's packet Q2.
   Direction :118-125 names the tension. This is not a defect of the delta.

Task 2 judgement. [Observed] The removed machinery leaves no residue, per the sweep above. [Inferred] Apart from
finding 1, every transmission stays inside an act in force on the delta's stated basis: the declared tool and
provider must have a statement in force or the run is refused (:146, :205-208), no variable may authenticate,
redirect or select a provider (:138), and managed redirection refuses (:140). The requirement stays fail-closed on
every arm it states, including the new authentication refusal. Finding 1 is a defect of form in that boundary, not
a reopened route: the intent is unambiguous from :173, :222 and :255.

Counts: 1 revise, 4 notes; round-3 closure 2 closed, 1 not closed (partly repaired, finding 2), 1 carried to the owner (finding 4).
