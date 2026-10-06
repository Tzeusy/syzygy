# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-1
Reviewed commit: afd789a996952dfad9e810a66f9ad9c1b4c21a82
Manifest SHA-256: f6ee9df888a08eca72133e4fefe50a53c76fdfd32c98ee09091899266787f3f8
Verdict: REVISE

Reviewer: fresh-context reviewer (CC-REV-1), round 1 of the v1.1 amendment.
I did not draft the change or share its session. I read the brief at the
reviewed commit and followed it. Inputs: the four patches, `SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`; the v1.0
bytes of `openspec/changes/polaris-dossier-local-agent-mode/`; the round-3 raw;
the v1.0 notes record; D9's notes record; SEC-3 in `security.md`; the D9 row of
`DOCTRINE-AMENDMENT-LOG.md`; the v1.0 sign-off record; RFC3-16, RFC5-12 at
their defining clauses (located by `DIRECTIVE-REGISTER.md`); the base change's
`SOURCE-POLICY.md`; `AGENTS.md`. No external or target-repository content was
fetched. No drafting conversation was read.

Method. [Observed] Scratch worktrees (detached) at `afd789a9` (main patches;
main patches plus N6) and at `55daf6ce` (main patches, for the ledger's
scratch checks). Every patch applied cleanly with `git apply`. `git diff
--stat 55daf6ce afd789a9` over `openspec/`, `scripts/`, `PROJECT-STATUS.md`
and the reconciliation evidence directory is empty, so the v1.0 bytes and
tooling are identical at both commits. Quotations were checked by Python
substring match over whitespace-normalised text. Digests were computed by
`sha256sum` / `hashlib`, never transcribed.

Digests [Observed]:

- `spec.md`, main patch only (line 3 above): `f6ee9df888a08eca72133e4fefe50a53c76fdfd32c98ee09091899266787f3f8`
- `spec.md`, main patch plus N6 hunk: `685e398b63b83d16fb8165e8f3ec94463e25194c1af8162f39b303957d058641`
- v1.0 `spec.md` at `55daf6ce`: `b39d103263d6667e8ab5e10abec70fc0a53ed9a22fad00e4bc7532f1ce18c40e`

## Criterion results in brief

| # | Criterion | Result |
|---|---|---|
| 1 | Traceable, nothing more | Yes [Observed]. Each hunk maps: spec head = E1; 033 gate sentence = R3-F8; brief form = R3-F5; declaration = R3-F2; "not an execution consent" = R3-F7; skill sentence = D9-N5; agent-could-run sentence = R3-F4; keeping obligation, step list, list source, escalation = R3-F1; cost quoted = R3-F3; Inferred list and disclosure = R3-F2/F8/F1; scenario wording = R3-F9; three new scenarios = R3-F2 (2), R3-F8 (1); Case/Falsifier arms = F1/F2/F3/F5/F7/F8/N5; warrant RFC5-12 = F7; 034 clause = F5. design.md: banner E1; decision 8 = E1 (D9 adopted), F2, N5, F7, F4, F1, F3, F5; table row F2/F7; skill description F9. proposal.md: banner E1; "Modified in effect" F9. No hunk grants read, egress, write or execution beyond v1.0; the credential hunk restricts Syzygy. R3-F6 omission: right for its RFC5-24 half; see Finding 6 on the RFC5-12 half |
| 2 | Each item does what its finding asked | Yes for F1, F2, F3, F5, F7, F8, F9, N5. F1's keeping obligation runs "from the issue of a brief that permits execution" with no end, which is N2's recommended reading; the packet's Question 3 says it depends on N2. F5's head sentence is quoted exactly as adopted ("Syzygy runs observed-project code only inside an explicit, opt-in execution profile."). F8's RFC3-16 quotation is exact; its "not in force" effects agree with 033 (refusal for consent, registry, policy act and statement; non-permitting brief for D9; Unknown `unconsented-source-or-provider` for the RFC7-20 reading). F4: see Finding 1 |
| 3 | Quotations exact | Yes for the patches: RFC3-16, `SOURCE-POLICY.md`, SEC-3 head all found byte-exact (normalised). 15 of 15 double-quoted fragments of the delta's "Current meaning" found in v1.0 bytes or `security.md`. Two inexact quotations in package prose (Finding 8) |
| 4 | Doctrine/contract/adopted requirement changed in effect | No. The non-consent sentence is consistent with RFC5-12's definition of execution consent ("per project: the owner's approval Decision for a specific execution-profile version (RFC5-18)"). N6 only flags; it forbids nothing to the session. See Finding 6 for disclosure of RFC5-12's D9-recorded effect change |
| 5 | Every Observed claim observable | Yes. The declaration, who entered it, the agent's working directory and in-scope statement (N6) are all Inferred. The credential read is an instant OS-level read, Observed only for that instant, with gaps disclosed as Inferred. Gate records are read and disclosed as within write reach |
| 6 | Scenarios falsifiable | Yes, with notes (Finding 5) |
| 7 | Change class | Normative is right [Observed: each v1.0-conforming behaviour named in the delta's change-class paragraph fails v1.1 text] |
| 8 | Impact ledger reproducible | Every digest, count and sweep row reproduced; one scratch-check statement differs (Finding 4) |
| 9 | Owner packet fair and plain | E1, N2 dependency and N6 blind spot disclosed. One misstatement of an item's effect (Finding 1); a miscount (Finding 7); the tooling prerequisite only partly disclosed (Finding 3) |
| 10 | design.md stays design | Yes. No code; the skill and Codex texts defer to `brief.md` ("Follow the execution rule in `brief.md`. Unless it says otherwise, do not build or run the cloned project outside an explicit, opt-in execution profile") and grant nothing |

## Criterion 8: ledger reproduction

[Observed] Population at `55daf6ce` via `git ls-tree -r -z --name-only`:
2,379 paths. Byte-literal sweep rows: `SEC-3's rule` 4; `every later check and
at close` 3; `configuration holds for its typed adapters` 3; `an adopted
capability declaration` 4; `for a public repository` 2; `allow-execution` 5;
`REQ-polaris-generation-033` 8; `REQ-polaris-generation-034` 4. Every row and
every listed path matches the ledger. No hit under `apps/`, `packages/` or
`scripts/` for 033, 034 or `allow-execution`. All ten subject digests in the
ledger's table reproduce, including the regenerated
`GOVERNING-DEPENDENCIES.md` (`de399fc8…`). Patch line counts 137, 94, 44, 33
reproduce. `count_polaris_effective_scenarios.py`: 35/230 main, 35/231 with
N6. `openspec validate polaris-dossier-local-agent-mode --strict` (1.9.0):
valid in both forms. `--regenerate` changed only the contracts line
(`RFC5-12` added) and `census.json` (227 → 230, three names). After editing
`PROJECT-STATUS.md` line 51 to 230: reconciliation `--check` 7 of 7 without
FAIL; builder `--check` "the package verifies (applied)"; unions `--check`
pass; `check_governance.py` 32 OK, 21 WARN, 0 FAIL (53); recorder `--check
… --version 1.0` "regenerates exactly; applied tree verified".

## Findings

**Finding 1 — The packet tells the owner the rendered page now says the agent could enter the choice; the specification requires no such page disclosure** (revise) — package prose

`OWNER-DECISION-PACKET.md:37`: "**Who can type the choice.** The page now
says that the agent, which runs the neighbouring commands, could run
`allow-execution` itself or write its record, and that only the skill and
agent instructions forbid it." In the packet, "the page" is the rendered page:
the bullet just before it says "The page shows it as your word, not something
Syzygy saw."

[Observed] The post-apply spec puts the R3-F4 sentence in 033's requirement
text (spec:17): "Syzygy cannot observe who ran the command, or that the
operator is the owner: the authoring agent, which runs the neighbouring
commands, could run that command itself or write its record into the state
directory, and only the skill and agent texts forbid it. Who ran it, that the
operator is the owner, and the declaration rest on the operator's word, are
labelled Inferred and are disclosed". What must be disclosed is who ran it,
the operator-is-owner fact and the declaration, each Inferred. The
"could run that command itself" sentence is in no disclosure list: not in the
run-record/page disclosure paragraph (spec:27), not in the records rule's
Inferred list (spec:25), and not in any scenario or falsifier arm. The delta's
item 4 calls it "a disclosure, not a new mechanism", which holds only for
readers of the specification.

[Inferred] The owner would sign believing that every dossier reader is told
the agent can produce the choice that gates D9's permitted case. A conforming
implementation need not say so. R3-F4 asked only that the owner read it plainly,
so the specification meets the finding. The packet overstates what the
specification binds, on the safeguard D9's permitted case rests on.

Fix (either): reword the packet bullet to "The specification now says…", and
say in the delta's item 4 who the disclosure is to; or add the sentence to
033's disclosure paragraph, with a falsifier arm. The second is wider than the
finding and needs its own trace.

**Finding 2 — E1 leaves false status sentences in the bytes v1.1 would bind** (note) — main patches

E1 corrects the three banners. [Observed] A sweep of the post-apply
`spec.md`, `design.md`, `proposal.md` and `tasks.md` (Python `re`, case-insensitive:
`candidate|not adopted|draft(ed)? PR|is drafted|drafted as D9|when adopted|provisional|under review|not yet|binds nothing|D9 is adopted`
and two more patterns) finds sentences that are now false or out of date, and
v1.1 leaves them in place:

- proposal:115, "**The candidate delta is held in `proposed/`, not `specs/`,**",
  is false. The v1.0 install moved it to `specs/`, which is where these
  patches apply.
- proposal:78 "drafted as D9", and proposal:86-87 "this change may not be
  signed before D9 is adopted". proposal:85 "Otherwise it quotes SEC-3" now
  understates what F5 requires.
- spec:15, "D9, or the identifier it carries when adopted", and "drafted as
  D9". These are harmless, but they read as if D9 were still pending.
- `tasks.md` (unchanged by v1.1) still opens "Candidate — binds nothing.
  Candidate checklist", and its D9-adoption item (tasks:15-20, "drafted as
  doctrine amendment D9 (draft PR #357)") is unchecked.

E1 is optional and editorial. But AGENTS.md's lesson is to mark staleness at
the stale sentence: correcting three banners while leaving these sentences
unmarked leaves a reader with mixed signals. Either extend E1 to these
sentences, or have the delta say that E1 covers only the banners and name
these residues.

**Finding 3 — The tooling prerequisite is stated three ways, and the ledger's own observation contradicts the delta's** (note) — package prose

- SEMANTIC-DELTA.md:271-276 names two prerequisites: a builder plus its
  `real_packages()` entry, and "the reconciliation's handling of a second
  version-tagged record for an installed Polaris addition (… v1.0's
  applied-tree check reads the v1.0 bytes, which v1.1 replaces)".
- IMPACT-LEDGER.md "Tooling prerequisite" names the builder, the
  `real_packages()` entry and selftest fixtures, and not the reconciliation.
- OWNER-DECISION-PACKET.md:79 names only "a builder that applies these
  patches".

[Observed] In the `55daf6ce` scratch tree with v1.1 applied, and with no
reconciliation change, `record_versioned_signoff.py --check
polaris-dossier-local-agent-mode --version 1.0` reports "regenerates exactly;
applied tree verified". `check_spec_reconciliation.py --check` R1 and R2
pass. The ledger itself records this (IMPACT-LEDGER.md:90, "The v1.0 record
therefore survives the v1.1 bytes"). So the delta's claim that the v1.0
applied-tree check reads the v1.0 bytes is not borne out.

[Inferred] The same observation shows that no check in the battery tells the
signed v1.0 spec bytes from unsigned v1.1 bytes: after `--regenerate` and the
status-figure edit, the v1.1 bytes pass every check with no v1.1 record. The
packet should tell the owner this, because it means the version-tag sign-off
is the only guard on these bytes until the new builder exists. Align the
three statements with that observation.

**Finding 4 — The ledger says the pre-regeneration check failed on two predicates; it fails on three** (note) — package prose

IMPACT-LEDGER.md:75-78: "`scripts/check_spec_reconciliation.py --check`
failed on two predicates, both expected: `GOVERNING-DEPENDENCIES.md` differs
… and `PROJECT-STATUS.md`'s Polaris figure (35, 227) differs from the census
(35, 230)." [Observed] Same tree, same order (patches applied, before
`--regenerate`): FAIL R3, "`census.json` differs from regeneration (a name or
scenario title moved)"; FAIL R4 (GOVERNING-DEPENDENCIES); FAIL R5
(PROJECT-STATUS figure). The result is "4 of 7 predicates without FAIL". The
ledger's later steps reproduce.

**Finding 5 — Scenario and falsifier notes** (note) — main patches

- "Permitting brief carries its lapse statement" (spec:151-155): "**AND** a
  permitting brief without that statement is a failure of this requirement"
  is not an observable outcome. It restates the THEN. The lapse statement is
  also already asserted by "Execution permission stays with the authoring
  session" (spec:125-129, its AND). R3-F2 asked for a falsifier arm, which
  spec:205 now carries. The scenario adds only a duplicate.
- Falsifier (spec:205): "a credential read is skipped at a check, inventory
  check, review check, render or close after a permitting brief, or Syzygy
  holds or writes a typed-adapter credential the operator's user can read".
  The second disjunct has no time anchor. Under spec:19 the obligation starts
  "from the issue of a brief that permits execution". Before that, a readable
  credential only blocks the permitting brief. A correct implementation that
  holds a readable credential and never permits execution could trip this arm
  as written. Fix: "… or, from a permitting brief on, Syzygy holds or writes
  …".
- "Gate records established from owner acts" (spec:157-161): one WHEN over
  six input kinds, and one THEN with three different outcomes. It can be
  falsified, because the Case varies "gate records carrying a status word or
  present as a file with and without the owner-act record". But one scenario
  per outcome would give each arm its own oracle row.

**Finding 6 — RFC5-12 becomes a warrant of 033, but nothing in v1.1 says that D9 recorded an effect change on RFC5-12 in the permitted case** (note) — package prose

RFC5-12 (`RFC-0005/consent-egress-secrets.md`:95ff): "**Execution consent** —
per project: the owner's approval Decision for a specific execution-profile
version (RFC5-18). Absent: no observed code runs." The D9 log row records
"(a) for RFC5-12 (its effect change is recorded)". R3-F6 raised RFC5-12 and
RFC5-24 together. The delta drops F6 entirely ("The owner kept Q3 (b), so it
drops out"), but Q3 (b) answers only the RFC5-24 half.

[Observed] v1.1 adds RFC5-12 to 033's contract warrants and cites it for "The
choice SHALL NOT be read … as an execution consent". In the permitted case,
observed code runs with no execution consent. That is D9's recorded effect
change, and it is consistent. [Inferred] A reader of 033 who sees RFC5-12
cited, and "Absent: no observed code runs" in the clause, will not learn from
v1.1 that D9 changed this. One line in the delta's "What explicitly does NOT
change" or "Not carried" would close it: "RFC5-12's 'Absent: no observed code
runs' is changed in effect for the permitted case by D9 (Q3 (a), recorded in
the D9 log row); v1.1 cites RFC5-12 only for what an execution consent is."
This changes no requirement.

**Finding 7 — Package prose miscounts** (note) — package prose

- SEMANTIC-DELTA.md:34: "three scenarios edited". [Observed] Comparing
  scenario bodies by script between `55daf6ce` and the post-apply spec,
  five 033 scenarios change: "Governed subject without a per-project provider
  statement", "Execution rule follows SEC-3", "Execution permission stays with
  the authoring session", "Adapter credential readable", "Execution permitted
  under the amendment". Three are added and none removed (45 → 48 in this
  file). Requirement titles and IDs are unchanged.
- OWNER-DECISION-PACKET.md:12: "Round 3 of its review left nine notes that
  1.0 carried as implementation duties". [Observed] Round 3 left eleven notes.
  The v1.0 notes record gives implementation obligations for F1, F2, F3, F5,
  F7, F8 and F9 (seven). F4 has a recommendation only. F6 is "No
  implementation obligation". F10 and F11 are neither.

**Finding 8 — Two quotations in the delta are not exact** (note) — package prose

- SEMANTIC-DELTA.md:115 quotes N2 as "once Syzygy holds one, it is kept from
  your user account permanently". The source
  (`DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md`, N2 row) reads "Once Syzygy holds
  one, …". The case differs.
- Item 10 (E1) says the spec's head paragraph and the two banners said
  "Candidate — binds nothing". [Observed] That literal is in v1.0 `design.md`
  and `proposal.md`, not in the spec. The spec's v1.0 head read "Candidate
  exact behavioral delta; not yet adopted, binds nothing". Likewise "is not
  adopted" is in the spec and the proposal, not in `design.md`. Attribute each
  quotation to the file that holds it.

**Finding 9 — N6 hunk: "SHALL carry" and "flag when absent" pull apart** (note) — N6 hunk

The N6 hunk (wt6 spec:21) reads "every command in the list SHALL carry the
working directory the agent reports for it and the agent's statement of
whether it falls within the scope…". In the same sentence it flags a command
"that has no reported working directory", and it adds "A flag refuses no step
and hides no command." [Inferred] One implementer will enforce "SHALL carry"
in the draft schema, so `check` refuses a draft with a command that lacks a
working directory. That refuses a step, against the hunk's own flag-not-refuse
rule. Another will accept the draft and flag the command. Say which: for
example, "the brief SHALL ask the agent to report, for every command, …; a
command reported without one is flagged". Otherwise the hunk does not restrict
the session beyond SEC-3 under D9. It forbids nothing, its working directory
and scope statement are Inferred, and the blind spot is disclosed (delta item
11; packet Question 2).

## Blocking findings

None blocking. Finding 1 is revise-level, and concerns the package prose
(the owner packet), not the patched specification bytes. Findings 2 to 9
are notes.
