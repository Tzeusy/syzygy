# Review brief — Polaris dossier local-agent mode

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. Round 1 returned REVISE over `f1bd0b5c` and round 2 REVISE over
> `af97611d`; both repairs and dispositions are below. Round 3 is the
> confirming round, dispatched by the lead after D9's text is fixed by its
> own review. Stopping rule, set before round 3: CONFIRM, or CONFIRM WITH
> EXCEPTIONS with notes only, clears the bytes; a third REVISE goes to the
> owner with all three raws.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria.

**The artifact under review.**

- `openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md`
  (the subject), and in the same change `proposal.md`, `design.md`,
  `tasks.md` and `GOVERNING-DEPENDENCIES.md`.
- In `.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode/`:
  `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` and this
  brief.

**Governing references.**

- The warrants:
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`,
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`,
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`,
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`
  and
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`.
- The dependency: doctrine amendment D9, draft PR #357, whose package
  directory under `contracts/candidates/` is named
  doctrine-amendment-sec3-attended-agent-session-d9 (not on `main` when
  this brief was written). Read its `SEMANTIC-DELTA.md`, "Proposed meaning",
  at the commit the lead names when dispatching (its text as fixed by its
  own review). 033 and 034 must carry its conditions; the drafter aligned
  them to arm A as frozen after D9's round-2 repair at `62c29093`, including
  the optional credential condition (D9's Q3(b)) as conditional on adoption,
  and closed in 033 three points D9 leaves to the spec: who records the
  per-run choice, which session may receive the permission, and how the
  credential condition is checked.
- `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`; CC-SPEC-1 to CC-SPEC-11 in
  `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` and CC-IMPACT-1 to
  CC-IMPACT-7 in `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` (craft acts 6 and
  7 put these in force; the path still says candidate); CC-REV-1 and CC-REV-2.
- RFC2-24 (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`),
  RFC3-16, RFC4-2, RFC4-19, and RFC7-2, RFC7-9, RFC7-10, RFC7-13, RFC7-19,
  RFC7-20 and RFC7-25 in `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`,
  each read at its defining clause and quoted (verification rule 8);
  `DIRECTIVE-REGISTER.md` gives file and line.
- The effective requirements 001, 002, 003, 004, 005, 006, 012, 017, 018,
  019, 020, 021, 022, 025, 030 and 031: the base spec
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
  the overlay `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`,
  `decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`, and the base change's
  `INTERFACES.md`, `SECURITY-CONTRACT.md`, `OWNER-FLOW.md`,
  `EFFECT-HOST-DESIGN.md` and `SCHEMA-CONTRACT.md`; RFC4-19's table in
  `.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`.
- Doctrine VIS-1 to VIS-4 and SEC-1, SEC-2, SEC-3, SEC-5 (`.syzygy/governance/doctrine/`).
- The two earlier raws, `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`
  and `-2-RAW.md`, to check whether each repair holds.
- The sibling candidate `openspec/changes/polaris-non-governed-narrative-profile/`,
  for overlap only.
- `AGENTS.md`, "Hard prohibitions" and "Verification rules".

The reviewer does not receive the drafting conversation, the drafter's
messages to the lead, or any signal of a desired verdict.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Does the change do what the direction authorizes, and no more?** Compare
   with direction items 1 to 5 and "What this direction does not do". Any
   grant of read, egress, write or execution, any withdrawal of the provider
   mode, or any adoption language is a blocking finding.
2. **Is every quotation of current text exact?** Re-extract each block under
   "Current meaning" from its file by script and compare. Is each displaced
   fragment named in the spec present verbatim in the effective file?
3. **Is the displacement complete and bounded?** Is there an adopted
   sentence that an operator-agent run would still violate and that the
   change neither displaces nor reads (check 001, 002, 003, 004, 012, 018,
   019, 020, 022, 025, 030 and the base change's design files)? Is anything
   displaced for the provider mode?
4. **Is any contract or doctrine changed in effect?** RFC2-24's closed
   Unknown reasons, RFC7-10's anchor form, SEC-2 and SEC-3: a spec that
   contradicts an accepted clause is blocking. RFC7-20 is different: the
   owner ruled a reading of it (rulings direction, item 1), knowing a
   reviewer may call that reading a contract change. Say whether you find it
   one, with the clause quoted. Report it as a finding for the owner; do not
   treat the ruling as settling it, and do not treat your finding as
   overruling it. Separately, check that 033 applies the ruling's three
   conditions exactly and no wider.
   The same holds for scope: the owner chose "Any repo" with SEC-2
   unchanged, and after round 1 kept it, with disclosure (review-1 rulings,
   item 2). Check that 033 states plainly that the per-project statement is
   a consent record and that neither its content classes nor SEC-5
   screening bind the agent's own reads and sends, and that its governed
   predicate matches 032's four conditions. Whether a consent whose class
   limit nothing enforces is SEC-2's "scoped" consent is the owner's; report,
   do not resolve.
   SEC-3: the owner chose to permit host execution by amending SEC-3
   (review-1 rulings, item 1). Check that nothing in the change, the design
   or the harness texts tells an agent to run observed code outside an
   execution profile while that amendment is not in force, and that the
   spec and the packet say sign-off waits for its adoption.
4a. **Is review independence as the owner ruled?** A separate top-level
   session the operator starts, a declared session id different from the
   author's, no subagent. The fidelity packet also carries the frozen
   inventory, read as part of "the criteria"; say whether that reading is
   faithful to the owner's option text.
5. **Is every Observed claim something Syzygy can observe?** Check each
   requirement's Observed / Inferred / operator-declared split against what a
   local process can actually see, given that the agent can write the
   clone's `.git` directory and, on a single-user host, Syzygy's state
   directory. An unobservable fact labelled Observed is blocking. The
   reading of 018's work home and 022's trail location for this mode is put
   to the owner (packet, R1); say whether the packet states it fairly.
6. **Can each scenario be falsified as written?** CC-SPEC: one WHEN/THEN pair,
   an independent oracle, a falsifier that a wrong implementation would
   trip.
7. **Is the change class right?** The delta says Normative.
8. **Is the impact ledger reproducible?** Re-run its published regexes at its
   commit and compare the counts, the 135-file classification, the 14-file
   extension and the 2-file extension for 021 (151 in all).
9. **Are the owner's rulings applied exactly?** Compare the packet's table
   and the specification with the three rulings records. Is any ruling
   widened, narrowed or restated as the drafter's choice, and is any
   decision taken that belongs to the owner? The packet's open items should
   be only the adoption of D9 and the v1.0 sign-off, with the findings it
   carries to the sign-off named (round 1: 6 to 8; round 2: 4, 5, 7 and 8).
   Is R1 applied exactly, with no qualifier the ruling lacks? Do 033 and 034
   carry every condition D9's text sets?
10. **Does `design.md` stay design?** No implementation code in `openspec/**`;
    the skill and Codex texts are prose, and no command it names claims
    behavior the requirements do not require.

## Round 1 disposition

Round 1 (raw held by the lead, verdict REVISE over
`f1bd0b5ccb09056905e85270037eb8cd92efa918`, 21 findings, 1 to 5 blocking).
The repair re-verified every quotation by script against its source.

| # | Finding | Disposition |
|---|---|---|
| 1 | Bytes read by identifier are not bound to the consented revision | Fixed: 033 reads honour no replacement objects, grafts, repository-local configuration, hooks or alternates, and recompute every commit, tree and blob identifier from the bytes read; scenario "Object store altered after pinning"; falsifier arms |
| 2 | Syzygy's records within the agent's write reach | Fixed in the honest form: 033 holds records in the state directory, rests nothing Observed on a stored record, re-derives quotations, checks and packet bindings at each check and render, labels the rest Inferred, issues no credential; 018, 020 and 022 read for this mode; scenario "Stored record altered within the agent's reach"; owner question R1 |
| 3 | 030's start-gate and read-coverage sentences retained unread | Fixed: 036 reads both, binding Syzygy's reads; the agent's reads are the operator's own act; scenario "Syzygy's reads wait for its start gates" |
| 4 | 006's inventory-verification sentences vs the ruled packet | Fixed: 035 reads both; accuracy verified against packet spans, completeness and preparation self-reported, Inferred; verdict records entry accuracy |
| 5 | 005 "actual inputs" and 002's producer understanding | Fixed: 033 reads the 005 scenario; 034 requires a self-reported `understanding` record reading 002; 002 and 003 added |
| 6 | RFC7-20 reading changes the clause's effect | For the owner: preserved in the delta and the packet, carried with the sign-off (review-1 rulings, item 3) |
| 7 | SEC-2 and "Any repo" | For the owner, applied as ruled (item 2): (a) and (b) stated plainly in 033; (c) the egress-consent-class option removed, the statement is a consent record; (d) 032's four conditions adopted |
| 8 | SEC-3 and agent execution | For the owner, applied as ruled (item 1): execution rule gated on an adopted SEC-3 amendment in 033 and 034; sign-off waits for it (spec head, packet, tasks) |
| 9 | Headless and `!`-prefixed launch forms | Fixed as the lead ruled on the updated finding: the headless form is dropped; a new terminal (default) and a `!` launch count as operator-started, stated in 035; 035 records the launch form as operator-declared and refuses any other; skill and Codex texts aligned |
| 10 | Limit rules contradict at zero | Fixed: deadline and budgets positive; repair and question limits nonnegative integers, 0 allowed |
| 11 | Independence readings | Fixed: inventory session-id refusal and scenario arm; extensions marked the drafter's choice (delta, packet O4); verdict schema noted as format |
| 12 | Model identity missing | Fixed: model identity and version operator-declared, no provider-reported version stated; 003 relied on |
| 13 | RFC7-10 target class unnamed | Fixed: evidence artifact identifier with integrity digest, the recomputed blob id serving as both |
| 14 | Citation duty by block kind | Fixed: Inferred cites, Unknown may cite none, non-normative cites nothing |
| 15 | Execution basis visible only when marked | Fixed: check and scenario apply to marked claims; the page says the marking is self-reported |
| 16 | Disclosure scenario incomplete | Fixed: commands and Syzygy's verification added, with the new disclosures |
| 17 | Work home and 020 left to planning | Fixed: 033 reads 020's gates and names the state directory as the Execution Record's home; with R1 |
| 18 | Packet should carry findings 6 to 8 | Fixed: the packet's sign-off section carries them |
| 19 | Ledger populations omit 002, 003, 020, 022 | Fixed: extension sweep, 14 more files, 149 in all |
| 20 | Duplicate open question in `design.md` | Fixed: merged |
| 21 | Warrant `decisions` empty | Fixed: the four direction identifiers listed; dependency union regenerated |

## Round 2 disposition

Round 2 (verdict REVISE over `af97611ddfc5b42f0893837c726a82a9e7a3bb9b`, 17
findings, 1 to 4 blocking; raw retained by the lead). Dispositions as the lead
directed. Every quotation was re-verified by script after the repair.

| # | Finding | Disposition |
|---|---|---|
| 1 | Pinned revision is a stored record, never re-bound | Fixed: 033 re-checks the recorded revision against the in-force consent at every check, review check and render; brief, draft, inventory and packets name it, a mismatch refuses; which revision was used is disclosed Inferred; scenario "Recorded revision altered"; falsifier arms |
| 2 | "Packet's exact contents" labelled Observed | Fixed: 035 Observes only the packet Syzygy built, its digest and the verdict's naming of it; the reviewer reading it unaltered is Inferred; the packet carries its own digest; design decision 5 corrected |
| 3 | R1 narrowed and uncited | Fixed: qualifier dropped ("a record it stored"); the Inferred list is open and longer; R1 cited in 033 and its warrants and 034's; R1 marked answered in packet, brief, delta, proposal, design and tasks |
| 4 | `!` launch form not shown to the owner | Fixed as directed: packet O4 row and plain-terms summary, proposal and delta state that admitting `!` is the lead's reading of the owner's words, with the reviewer's facts; the sign-off covers it; no new question |
| 5 | R1 does not cover the 020 reading; option A's costs understated | For the owner: not recorded as ruled by R1; the 020 reading and the costs (agent-editable 022 audit evidence, stored pinned revision and packets) carried with the sign-off offering |
| 6 | Second discovery population drawn from a stored read log | Fixed: the Observed population is the objects the render itself reads and verifies; earlier-step membership, where shown, is Inferred; falsifier arm |
| 7 | RFC7-20 reading | For the owner: preserved with round 1's finding 6, including that the reading now does work only for non-governed subjects |
| 8 | SEC-2 "scoped"; governed predicate input | First part for the owner: the packet names 033's consent-record sentence as the point the sign-off decides. Second part fixed: every `.syzygy/` path counts, adopted or not, never less strict than 032; recorded as an overlap the second adoption reconciles; proposal's "overlaps it nowhere" corrected |
| 9 | Which spans the fidelity packet carries | Fixed: spans cited by the draft and by the frozen inventory, screening-admitted only |
| 10 | Hash algorithm source; design route 1 | Fixed: the algorithm is the consented identifier's; a clone that does not hash under it refuses. Route 1 dropped; the design names an in-process reader that reads no repository configuration |
| 11 | 021, SEC-1 and 022's principal | Fixed: 033 says the commands serve no route, hold no Syzygy credential and are outside 021's inventory; the audit principal is the operator, credential identity Unknown; SEC-1's bullet read [Inferred]; 021 swept (2 more files, 151) |
| 12 | RFC4-19 work-item identity | Fixed: absent with its reason; the run renders as unattributed execution, never dropped |
| 13 | Project-scoped agent configuration in the clone | Fixed: skill and Codex texts never start a session in the clone and treat its text as data; session directories exclude the clone; 034's brief states the data rule |
| 14 | Design review binds pages the final render changes | Fixed: subject excludes one named review-status region; any other change is a revision; scenario "Design review survives its status region" |
| 15 | Design consistency | Fixed: session id session-declared, launch form operator-declared through `launch-form`, both Inferred; sessions start in role directories without the draft; `--out` removed; `preflight` reads no tree; "strict form" removed |
| 16 | Scenario bundling | Fixed: zero limits, statement withdrawal, non-governed subject and provider-mode draft are their own scenarios |
| 17 | Delta header; SEC-3 timing | Fixed: header names `OWNER-FLOW.md`, `SECURITY-CONTRACT.md`, 021 and SEC-1; 033 and 034 cite D9 and carry its four draft conditions (owner-started, attended, own host; choice recorded first; Inferred; commands disclosed with their claims); round 3 waits for D9's text |

## Output

A raw review stored verbatim; the lead retains it as
`docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-<n>-RAW.md`. From round 3 its
head takes the form `scripts/record_versioned_signoff.py` reads: the first
four non-blank lines are exactly

```text
# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-<n>
Reviewed commit: <40-hex commit the reviewer read>
Manifest SHA-256: <sha256 of proposed/polaris-generation/spec.md at that commit, computed by script>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

with no blank line inside them that would push `Verdict:` out of the first
four non-blank lines. The recorder reads `Manifest SHA-256:` as information,
never as an argument; this package has no manifest, so the line carries the
subject's digest, the same value rounds 1 and 2 put on their
`Subject SHA-256:` line. It accepts only `CONFIRM` or `CONFIRM WITH
EXCEPTIONS`.

Then `## Findings`, each numbered continuously as
`**Finding N — title** (blocking|revise|note)`, with the evidence. For
`CONFIRM WITH EXCEPTIONS` every finding must be a `note`, and the lead writes
a sibling `ROUND-3-DISPOSITIONS.md` in this package that names the raw on a
`Reviewed record:` line and disposes of exactly the raw's findings. The
recorder also needs this package's builder, which is post-sign-off work
(`tasks.md`).
