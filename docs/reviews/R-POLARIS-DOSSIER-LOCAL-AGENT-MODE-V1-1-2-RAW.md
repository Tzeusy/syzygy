# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-2
Reviewed commit: 1110512435f34c35b0337282ba9f69e671dc8af6
Manifest SHA-256: b5564fe4f52b98716349c72307e123090952986cfd45dd7e2aab3fbf68765204
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (CC-REV-1), round 2 of the v1.1 amendment.
I did not draft the change. I read `REVIEW-BRIEF.md` at the reviewed commit
and followed it, and read the round-1 raw to test each repair. Inputs: the four
patches; `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`REVIEW-BRIEF.md`; the v1.0 bytes of
`openspec/changes/polaris-dossier-local-agent-mode/` at `55daf6ce`; D9's notes
record (N2, N5, N6); SEC-3 in `security.md`; the D9 row of
`DOCTRINE-AMENDMENT-LOG.md`; RFC3-16, RFC5-12, RFC7-20 at the lines
`DIRECTIVE-REGISTER.md` gives (RFC-0003:112, RFC-0005:95, RFC-0007:416); the
base change's `SOURCE-POLICY.md`; `AGENTS.md`. No external or
target-repository content was fetched; no drafting conversation was read.

Method [Observed]. Three detached scratch worktrees: `11105124` with the three
main patches; `11105124` with the main patches plus the N6 hunk; `55daf6ce`
with the main patches (for the ledger's scratch checks). Every patch applied
with `git apply`. `git diff --stat 55daf6ce 11105124` over `openspec/`,
`scripts/` and `PROJECT-STATUS.md` is empty, so the v1.0 bytes and tooling are
the same at both commits. `git diff --stat afd789a9 11105124` touches only the
seven package files. Quotations were checked by Python substring match over
text with whitespace collapsed and `*`, `` ` ``, `>` stripped. Digests come
from `sha256sum`.

Digests [Observed]:

- `spec.md`, main patch only (line 3): `b5564fe4f52b98716349c72307e123090952986cfd45dd7e2aab3fbf68765204`. The same at `11105124` and at `55daf6ce`.
- `spec.md`, main patch plus N6: `6414597d73572c903b0f876fd31d58f04d1b42a8c1a68361aa3a5f30feb598ee`
- `design.md` `66356a0f…4a81`, `proposal.md` `f917b750…b4da`, regenerated `GOVERNING-DEPENDENCIES.md` `de399fc8…0cf5`. The v1.0 digests `b39d1032…`, `400e4e7c…`, `abdb8ba1…`, `ae3008b3…` and `tasks.md` `6ccaa689…` all match the ledger table.

## Round-1 repairs

| R1 # | Holds? | Evidence [Observed] |
|---|---|---|
| 1 (revise) | Yes | Packet line 37ff now says "The specification now says plainly, for you as its reader, … The rendered page does not repeat that sentence". Delta item 4 says the sentence is for the specification's readers and why no page disclosure is added. This matches the spec. 033's disclosure paragraph is unchanged in that respect |
| 2 | Yes | All named residues are corrected in the post-apply spec, design and proposal. A sweep of the four files (Python `re`, case-insensitive, 15 alternatives including `candidate`, `drafted as`, `when adopted`, `PR #357`, `proposed/`, `until it is amended`) finds only `tasks.md` residues (named in delta item 10), proposal:105 "the candidate `…/polaris-non-governed-narrative-profile/`" (true: that change is a candidate), proposal:115's "was held", now in the past tense, and design:189 (Finding 2) |
| 3 | Mostly | Delta and ledger both name builder, `real_packages()` entry and selftests, and drop the reconciliation claim. Both say no check tells v1.0 from v1.1 bytes, and the packet says so too. The packet's plain-language line names the builder and recorder entry and leaves out the selftests (Finding 4) |
| 4 | Yes | Reproduced: before `--regenerate`, R3, R4 and R5 fail. "4 of 7 predicates without FAIL" |
| 5 | Yes | The lapse scenario is gone, and the AND of "Execution permission stays with the authoring session" asserts the lapse statement. The falsifier arm reads "or, from a permitting brief on, Syzygy holds or writes …". The gate scenario is split three ways: "Consent or policy record…", "D9 record…", "RFC7-20 reading record…", each with one outcome |
| 6 | Yes | Delta "Not carried" names RFC5-12's "Absent: no observed code runs", D9's recorded effect change, and the definitional-only citation |
| 7 | Yes | By script, five 033 scenarios change and four are added (45 → 49 in the file). None is removed. The names match the ledger. The packet no longer counts the round-3 notes |
| 8 | Yes | "Once Syzygy holds one, it is kept from your user account permanently" is exact in D9's notes. Each item-10 phrase is found in the file the delta attributes it to (13 of 13) |
| 9 | Yes | The N6 hunk now reads "the brief SHALL ask the agent to report … and the draft SHALL be admitted whether or not each command carries them". Its scenario THEN admits the draft. The falsifier arm adds "or a flag refuses a step or hides a command" |

## Criteria in brief

| # | Result |
|---|---|
| 1 | Yes [Observed]. Every hunk maps to R3-F1/F2/F3/F4/F5/F7/F8/F9, D9-N5 or E1, as in round 1. The new round-2 bytes are E1 extensions (proposal heading, "drafted as D9", "may not be signed", `proposed/` sentence; spec head) and the repairs above. No hunk grants read, egress, write or execution beyond v1.0 (see Finding 1 for an ambiguity, not a grant). R3-F6 is rightly omitted under Q3 (b), and its RFC5-12 half is now addressed in "Not carried" |
| 2 | Yes. F1's keeping obligation runs "from the issue of a brief that permits execution" with no end, which is N2's recommended reading ("Once Syzygy holds one, it is kept from your user account permanently"). Delta item 1 and packet Q3 state the dependency on N2. The D9 log row confirms that N2 remains the owner's. F5 quotes the head sentence "Syzygy runs observed-project code only inside an explicit, opt-in execution profile." exactly. F8's RFC3-16 quotation is exact, and each "not in force" outcome (refusal; no permitting brief; Unknown `unconsented-source-or-provider`) agrees with the rest of 033 |
| 3 | Yes for the patches and "Current meaning": RFC3-16, RFC5-12 ("Absent: no observed code runs"), RFC7-20 ("absent SEC-2 named-provider consent it is **not computed**"), `SOURCE-POLICY.md`, SEC-3 head and "What the permitted case costs", the D9 row ("its effect change is recorded"), and 15 of 15 "Current meaning" fragments in v1.0 or `security.md`. One inexact quotation in the packet (Finding 3) |
| 4 | No change in effect. The non-consent sentence uses RFC5-12 only for what an execution consent is ("the owner's approval Decision for a specific execution-profile version"). The N6 hunk only flags: "A flag refuses no step and hides no command" |
| 5 | Yes. The declaration, who entered it, operator-is-owner, the agent's command list, and N6's working directory and scope statement are all Inferred. The credential read is Observed only at the instant it runs, and the gaps are disclosed as Inferred. Gate-record reads are disclosed as within write reach |
| 6 | Yes, each new scenario has one WHEN/THEN and a falsifier arm; one construction note (Finding 5) |
| 7 | Normative is right: each v1.0-conforming behaviour the delta names fails v1.1 text |
| 8 | Reproduced in full; see below |
| 9 | Fair and plain. It discloses E1 ("drop it if you prefer"), the N2 dependency, N6's blind spot ("It cannot catch an out-of-scope command the agent ran inside the clone and called in scope") and the tooling prerequisite. Recommendations are labelled. Findings 3 and 4 are small |
| 10 | Yes. There is no code in `openspec/**`. The skill ("Follow the execution rule in `brief.md`. Unless it says otherwise, do not build or run the cloned project outside an explicit, opt-in execution profile.") and Codex texts defer and grant nothing |

## Criterion 8: ledger reproduction [Observed]

- Population at `55daf6ce` by `git ls-tree -r -z --name-only`: 2,379 paths.
- Byte-literal hits per phrase: `SEC-3's rule` 4; `every later check and at close` 3; `configuration holds for its typed adapters` 3; `an adopted capability declaration` 4; `for a public repository` 2; `allow-execution` 5; `REQ-polaris-generation-033` 8; `drafted as D9` 5; `the identifier it carries when adopted` 2; `The candidate delta is held in` 2; `Execution follows SEC-3 until it is amended` 1; `REQ-polaris-generation-034` 4. Every count and every listed path matches the ledger. Nothing under `apps/`, `packages/` or `scripts/` contains 033, 034 or `allow-execution`.
- Patch line counts: 141, 94, 83, 35.
- `count_polaris_effective_scenarios.py`: 35/231 (main), 35/232 (with N6). `openspec validate polaris-dossier-local-agent-mode --strict` (1.9.0) is valid in both forms.
- Before `--regenerate`: R3, R4 and R5 FAIL, "4 of 7".
- `--regenerate` adds `RFC5-12` to the contracts line and nothing else; `GOVERNING-DEPENDENCIES.md` then hashes to `de399fc8…`. `census.json` goes 227 → 231, adding the four names.
- With `PROJECT-STATUS.md` line 51 set to 231: reconciliation "7 of 7 … PASS"; builder "OK: the package verifies (applied)"; unions "3 Polaris dependency unions match their warrants"; `check_governance.py` "32 OK, 21 WARN, 0 FAIL (53 checks)"; recorder `--check … --version 1.0` "regenerates exactly; applied tree verified".

## Findings

**Finding 1 — The N5 sentence defers every session to "the run's `brief.md`", which is the authoring brief; read literally, it hands a role session the authoring permission** (note) — main patches

Post-apply spec:19: "The `/polaris-dossier` skill and the Codex instructions
SHALL NOT grant execution themselves: they SHALL only defer to the execution
rule in the run's `brief.md`, and absent that brief SHALL state that the
observed project is not to be built or run outside an explicit, opt-in
execution profile." [Observed] The same skill serves the inventory and review
sessions. Design:389-398 has an "Always:" list that includes "Follow the
execution rule in `brief.md`", and design:447 adds "With a role…". By the time
those sessions start, the run's `brief.md` exists, and when execution was
permitted it carries the permission. spec:17 says "Only the authoring
session's brief may carry the permission: the inventory brief, every review
packet and every session prompt … SHALL carry SEC-3's rule". [Inferred] An
implementer who follows the N5 sentence literally would ship a skill that
points a role session to a permitting `brief.md`. The "absent that brief"
branch would never fire for role sessions, because the run's brief always
exists by then. The controlling rule in spec:17 and SEC-3's "every
instruction a Syzygy feature gives an agent (a brief, prompt, skill …)" still
govern. The design's role paragraph sends the inventory session to
`inventory-brief.md`. So a careful reader resolves this, and I do not rate it
a grant. Suggested wording for a later version, or now if the drafter
re-opens the bytes for another reason: "defer to the execution rule in the
brief or packet the session was given (the run's `brief.md` for the authoring
session)".

**Finding 2 — design.md keeps v1.0's "its configuration holds" where F1 changed the spec to "Syzygy holds"** (note) — main patches

Post-apply design:188-189: "Syzygy's own read attempt, as the operator's
user, finds no adapter credential its configuration holds readable." The
spec changed "every credential that Syzygy's configuration holds for its
typed adapters" to "every credential that Syzygy holds for its typed
adapters". The design hunk edits the next sentences of the same paragraph
and leaves this one. [Observed] The ledger's sweep phrase
(`configuration holds for its typed adapters`) does not match the design
wording, so the sweep could not catch it. The requirements are controlling
(design head), so nothing binds differently. It is a residue a reader will
notice.

**Finding 3 — The packet quotes D9 inexactly** (note) — package prose

`OWNER-DECISION-PACKET.md`:92: "D9 says your per-run choice "names what the
instruction covers"." [Observed] SEC-3 as adopted (`security.md`:78-79)
reads "the owner has recorded a choice for that one run, naming what the
instruction covers". The literal "names what the instruction covers" occurs
in v1.0 033, not in D9. Either quote "naming what the instruction covers" or
attribute the phrase to the dossier specification.

**Finding 4 — The packet's prerequisite line omits the selftests the delta and ledger name** (note) — package prose

The round-1 disposition, item 3, says "one statement (builder, recorder
entry, selftests) in delta, ledger and packet". [Observed] Packet Q1 says "a
builder that applies these patches, and its entry in the sign-off recorder".
The delta and ledger each add "a selftest fixture per predicate". For an owner
this is immaterial; it is noted only because the disposition claims parity.

**Finding 5 — "Consent or policy record without its owner act" asserts a page disclosure the WHEN does not cause** (note) — main patches

Its AND reads "every page discloses that the records Syzygy read for its gates
lie within the agent sessions' write reach". [Observed] The THEN refuses the
step, and the disclosure is owed on every page whatever the gate outcome
(spec:29). The pair's oracle is still clear: the refusal and its reason. But
the AND is a standing property rather than a response to this WHEN. "Mode
disclosed on every page" is the natural home for it. Optional tidy-up; the
scenario is falsifiable as written.

## Blocking findings

None. All five findings are notes. Findings 1, 2 and 5 concern the main
patches. Findings 3 and 4 concern the package prose. None concerns the N6
hunk, whose round-1 note is repaired.
