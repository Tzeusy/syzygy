# Review brief — Polaris dossier local-agent mode, version 1.1

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. Stopping rule, set before round 1: at most three rounds; CONFIRM,
> or CONFIRM WITH EXCEPTIONS with notes only, clears the bytes; a third
> REVISE goes to the owner with all three raws. Round 1 returned REVISE
> over `afd789a9`; its repair and dispositions are below.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria. Run on the default model.

**Network.** Do not fetch any content of any external or target repository:
no `gh api` contents, no raw URLs, no clone, no web access. The only network
use allowed is `git fetch` of this repository. Where a criterion turns on
how a coding-agent harness behaves, judge from general knowledge and label
it `[Inferred]`.

**The artifact under review.** In
`.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-1/`:

- `proposed/spec.md.patch`, `proposed/design.md.patch`,
  `proposed/proposal.md.patch` (the subject), and
  `proposed/spec.md.n6-optional.patch` (the optional hunk, reviewed as an
  option the owner may take or leave);
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` and
  this brief.

Apply the patches to `openspec/changes/polaris-dossier-local-agent-mode/` in
a scratch worktree of the commit under review (`git worktree add --detach`
and `git apply`), and read the post-apply bytes, with and without the N6
patch. Read the v1.0 bytes beside them; `git diff` is the change.

**Governing references.**

- The sources the change carries: the v1.0 notes record
  `.syzygy/governance/contracts/candidates/POLARIS-DOSSIER-LOCAL-AGENT-MODE-REVIEW-NOTES.md`
  and the round-3 raw `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-3-RAW.md`
  (findings 1 to 9); D9's notes record
  `.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md`
  (notes N1, N2, N5, N6).
- D9 as adopted: SEC-3 in `.syzygy/governance/doctrine/security.md`, and
  `.syzygy/governance/decisions/DOCTRINE-AMENDMENT-LOG.md`, row D9 (the owner
  kept Q3 (b)).
- The v1.0 sign-off record
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.0.md`,
  and the five dossier directions in `.syzygy/governance/decisions/`
  (`POLARIS-DOSSIER-LOCAL-AGENT-*-DIRECTION.md`).
- RFC3-16 (`.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`),
  RFC5-12 (`.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`),
  RFC7-20 (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`),
  each read at its defining clause and quoted (verification rule 8);
  `DIRECTIVE-REGISTER.md` gives file and line. The base change's
  `openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md`.
- `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`; CC-SPEC-1 to CC-SPEC-11 and CC-IMPACT-1
  to CC-IMPACT-7 in that directory (in force under craft acts 6 and 7; the
  path still says candidate); CC-REV-1 and CC-REV-2.
- Doctrine VIS-1, VIS-2, VIS-4 and SEC-2, SEC-3, SEC-5.
- `AGENTS.md`, "Hard prohibitions" and "Verification rules".

The reviewer does not receive the drafting conversation, the drafter's
messages to the lead, or any signal of a desired verdict.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Is every item traceable to its source, and nothing more?** Each hunk
   of the three patches maps to R3-F1, F2, F3, F4, F5, F7, F8, F9, D9-N5, or
   E1 (the status-sentence correction the delta flags as not from the
   notes). A
   hunk that maps to none, or that grants read, egress, write or execution
   beyond v1.0, is blocking. Is R3-F6 rightly omitted given the owner's
   Q3 (b)?
2. **Does each item do what its finding asked, no wider and no narrower?**
   Compare each with the finding's text in the round-3 raw and the
   disposition in the notes record. In particular: does F1's keeping
   obligation match D9's condition and N2's recommended reading, and does
   the packet say it depends on N2? Does F5's agent-directed statement
   carry SEC-3's rule faithfully, quoting the head sentence exactly as
   adopted? Is F8's RFC3-16 quotation exact, and is each "not in force"
   effect in the new scenario consistent with the rest of 033?
3. **Is every quotation exact?** Re-extract by script each quotation of
   SEC-3, D9, RFC3-16, RFC5-12, `SOURCE-POLICY.md` and v1.0 text in the
   patches and in `SEMANTIC-DELTA.md` "Current meaning", and compare.
4. **Is any doctrine, contract or adopted requirement changed in effect?**
   Including whether "the choice SHALL NOT be read … as an execution
   consent" is consistent with RFC5-12, and whether the N6 hunk restricts
   the session in a way SEC-3 under D9 does not.
5. **Is every Observed claim something Syzygy can observe?** Especially the
   declaration (F2), the credential read at each step (F1), the gate-record
   reads (F8), and N6's working directory and in-scope statement.
6. **Can each new or changed scenario be falsified as written?** One
   WHEN/THEN pair, an independent oracle, a falsifier arm a wrong
   implementation would trip.
7. **Is the change class right?** The delta says Normative.
8. **Is the impact ledger reproducible?** Re-run its sweep predicate at
   `55daf6ce` and compare every row; re-compute the digests and counts;
   re-run its scratch-tree checks and compare.
9. **Is the owner packet fair and plain?** Does it state each question with
   its options and costs without steering beyond a labelled
   recommendation? Does it disclose E1, the N2 dependency, the N6 hunk's
   blind spot, and the tooling prerequisite?
10. **Does `design.md` stay design?** No implementation code in `openspec/**`;
    the skill and Codex texts never grant execution (N5).

## Round 1 disposition

Round 1 (verdict REVISE over `afd789a996952dfad9e810a66f9ad9c1b4c21a82`, 9
findings: 1 revise, 8 notes; raw retained by the lead). Every repaired
quotation re-verified by script; every digest, count and scratch-tree check
in the ledger re-run on the repaired patches.

| # | Finding | Disposition |
|---|---|---|
| 1 | Packet says the page discloses that the agent could enter the choice; the spec requires no such disclosure | Fixed in the narrower form: packet bullet says the specification tells its reader, and the page does not repeat it; delta item 4 says who the sentence is for and why no page disclosure is added |
| 2 | E1 leaves false status sentences | Fixed: E1 extended to the spec's "drafted as D9" and "the identifier it carries when adopted", and the proposal's heading, "drafted as D9", "may not be signed before D9 is adopted" and the `proposed/` sentence; `tasks.md` residues named in the delta, not edited |
| 3 | Tooling prerequisite stated three ways; reconciliation claim contradicted | Fixed: one statement (builder, recorder entry, selftests) in delta, ledger and packet; the reconciliation claim dropped; the packet and ledger say no check tells v1.0 from v1.1 bytes |
| 4 | Pre-regeneration check fails on three predicates, not two | Fixed: R3, R4, R5 named |
| 5 | Lapse scenario restates its THEN; falsifier arm unanchored; gate scenario bundles three outcomes | Fixed: lapse scenario dropped (its falsifier arm stays, and "Execution permission stays with the authoring session" asserts it); arm anchored "from a permitting brief on"; gate scenario split into three, one per outcome (231 scenarios, 232 with N6) |
| 6 | RFC5-12's D9-recorded effect change not mentioned | Fixed: delta "Not carried" names it and says v1.1 cites RFC5-12 only for what an execution consent is |
| 7 | Miscounts | Fixed: five scenarios edited, four added; packet no longer counts the round-3 notes |
| 8 | Two inexact quotations | Fixed: "Once" capitalized; E1 attributes each status phrase to the file that held it |
| 9 | N6 "SHALL carry" vs "refuses no step" | Fixed: the brief asks the agent to report both; the draft is admitted either way; the scenario's THEN says so |

## Output

A raw review stored verbatim; the lead retains it as
`docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-<n>-RAW.md`. Its first
four non-blank lines are exactly

```text
# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-<n>
Reviewed commit: <40-hex commit the reviewer read>
Manifest SHA-256: <sha256 of openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md after applying proposed/spec.md.patch alone to that commit, computed by script>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

with no blank line among them. This package has no manifest; the line
carries the v1.1 subject's digest without the N6 hunk, which the recorder
reads as information. Give the with-N6 digest in the body.

Then `## Findings`, each numbered continuously as
`**Finding N — title** (blocking|revise|note)`, with the evidence, and say
for each whether it concerns the main patches, the N6 hunk, or the package
prose. For `CONFIRM WITH EXCEPTIONS` every finding must be a `note`.
