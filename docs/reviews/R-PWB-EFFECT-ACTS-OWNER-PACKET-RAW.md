# Fresh-context review — PWB effect-acts owner sign-off packet

Reviewer: fresh-context reviewer, no prior session history with this packet.
Scope: is the packet fit to present to the human owner as-is, against the
owner's standing directive that owner packets be plain-sentence, jargon-free,
concise and actionable, and technically-literate-non-Syzygy-readable.

Packet head: a322a60e9f2b166273a80e3fc145bc3a8193c962
Frozen subject: 48e0f5db645d1fb08e5e3a65c5e50dbcece40412

## 0. Setup facts

- `git rev-parse HEAD` at review time: `8482b0087090449ee0ba94790ee0600c1a6b8feb`
  (two commits after the named packet head — `7928f65` adds the recorder
  script, `8482b00` adds AGENTS.md notes; neither touches the packet).
  [Observed]
- Packet bytes at HEAD and at commit `a322a60e9f2b166273a80e3fc145bc3a8193c962`
  are byte-identical:
  `sha256sum .syzygy/governance/contracts/candidates/pwb-effect-acts/OWNER-SIGNOFF-PACKET.md`
  = `03d29d7a395254664ca64c8ed4fd7f0a1ea4620357c16e35ff3dca9a34e718ed`
  `git show a322a60e9f2b166273a80e3fc145bc3a8193c962:<packet path> | sha256sum`
  = `03d29d7a395254664ca64c8ed4fd7f0a1ea4620357c16e35ff3dca9a34e718ed`
  Identical digests confirm the reviewed subject is exactly the named packet
  head. [Observed]

## 1. Exactness — `[Observed]` PASS

The three phrases in "Exact owner responses" (packet lines 98, 101, 104):

```text
CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION: 5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841
```
```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61
```
```text
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7
```

Verification, each digest computed both at HEAD and at frozen subject
`48e0f5db645d1fb08e5e3a65c5e50dbcece40412` via `git show <commit>:<path> |
sha256sum`, all four values equal in each row:

| Artifact | sha256 (HEAD == frozen subject) |
|---|---|
| `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` | `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841` |
| `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` | `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61` |
| `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | `d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7` |

Each digest is 64 hex characters (`python3 len()` check on each string = 64).
Each of the three exact phrases occurs exactly once in the packet
(`grep -c -F <phrase> OWNER-SIGNOFF-PACKET.md` = 1, 1, 1 respectively). The
manifest file the packet cites at line 5
(`.syzygy/governance/contracts/candidates/pwb-effect-acts/PWB-EFFECT-ACTS-MANIFEST.txt`)
independently carries the same three rows and its own sha256
(`d259c3798b2961489d31c55af09e86c9711c0cfd4e5ec626211fdc2447a54150`) matches
the packet's citation at line 5. [Observed] PASS.

## 2. Honest trust model — `[Observed]` PASS

`grep -n -i "verified\|state (2)\|state(2)"` over the packet returns **zero
matches** — the words "verified" / "Syzygy-verified" / "state (2)" do not
appear anywhere in the packet. [Observed]

The packet states plainly, at lines 18-22:

> "Performing an act here is a **state-(1)** act: owner-trusted, uncorrelated,
> and same-tree forgeable from Syzygy's perspective. Its digest detects later
> drift; it does not prove authorship or attendance. No independent audit
> trail (A1) exists, and the act records that absence explicitly."

and again at lines 66-68 ("They are warrants, not evidence that any read,
screening or derived claim succeeded"), and at lines 93-95 ("State (1) is
selected by performing the phrase; the recorder writes the A1 audit-record
identity as absent"). This matches `ACT-SEMANTICS.md`'s per-act binding table
(item 9: "A1 audit-record identity — explicitly absent") and
`record_pwb_effect_acts.py`'s `render_act`/`render_aggregate_block`, which
both hard-code `Provenance state: owner-adopted (bootstrap, uncorrelated)` —
state (1) — and `A1 audit-record identity ... explicitly absent`, never
state (2), never "verified." [Observed] PASS.

## 3. Scope honesty — cross-checked against the three source files

For each act, the packet states what it authorizes and what it does not; body
read requires all three plus separate implementation authorization (packet
lines 16, 69, 72-73). No write/egress/execution/deployment/release (lines
59-62, 69-71). No second repository (lines 36, 71). No retroactive
authorization of the precondition-read incident (line 38). All present.
[Observed] PASS on presence.

Per-file accuracy check:

- **Consent** (packet lines 29-38) vs.
  `BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`: the packet's exclusion list
  ("PostgreSQL, credential stores, secret APIs, `.env` and credential files,
  arbitrary implementation-file bodies, working-tree traversal, code
  execution, network egress, writes to Butlers and any second repository")
  matches the source's six-item exclusion list one-for-one (source: "secret
  API or runtime-service access" — packet compresses to "secret APIs",
  dropping "runtime-service access" as a distinct clause; not a scope
  overstatement, since runtime-service access is still excluded by the
  policy's `accessBoundary` fields the packet doesn't quote). "No silent
  expiry; you may narrow or revoke by a later act" (packet line 37) matches
  the source verbatim in substance; the packet omits the source's trailing
  clause "revocation does not erase prior observation records" — an omission,
  not an overstatement. The retroactivity disclaimer (packet line 38) matches
  the source's final paragraph exactly in substance. [Observed] No
  overstatement found; one minor omission (non-blocking).

- **Policy** (packet lines 43-51) vs.
  `POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`: denied
  filenames/suffixes list matches `deniedPathBasenames` +
  `deniedPathPrefixes` + `deniedPathSuffixes` exactly (packet's `.env*`
  compresses the source's `.env`, `.env.local`, `.env.production`, and prefix
  `.env.` into one glob-like token — accurate in substance). The four
  detectors named (private-key blocks, known token formats, credential
  assignments, credential-bearing URLs) match the JSON's four `detectors`
  entries exactly in order and kind. "strict UTF-8 without NUL" matches
  `allowedTextEncodings` + the unclassifiable-exclusion trigger list.
  Retained-fields claim ("only its hash, path, policy id/version and the
  detector id or exclusion reason are retained") matches `matchAction
  .retainedFields` (`contentDigest`, `repositoryRelativePath`, `policyId`,
  `policyVersion`, `detectorId`) and `unclassifiableExclusion.retainedFields`
  (same four plus `exclusionReason`) exactly, and both set `retainBody:
  false`. **This is the criterion-3 checkpoint the task called out
  specifically** — "unclassifiable content is excluded whole" is stated
  accurately at packet line 48 ("Any match or anything unclassifiable
  excludes the whole file"), matching `unclassifiableExclusion.action:
  "exclude-whole-artifact"`. The packet never spells out the literal class
  string `unclassifiable-excluded` (nor `excluded-artifact`) — a deliberate
  jargon omission consistent with the readability directive; the *fact* (whole
  file excluded, only metadata kept) is stated correctly and completely, so
  this is not an inaccuracy, only a term the packet chooses not to import. One
  soft understatement: packet line 43 says screening happens "before anything
  is modeled," but the JSON's `scope.ingestBoundaries` names seven boundaries
  (observation, model, cache, log, human-html, machine-json,
  walkthrough-record) where the policy actually applies — the packet's "raw
  bodies are never stored, logged, rendered, returned or sent anywhere" (line
  50-51) does cover the substance of all seven boundaries, so no
  owner-relevant protection is actually missing from the packet's account,
  but "before anything is modeled" alone could read as a single ingest-time
  gate rather than a boundary enforced everywhere. [Observed] Non-blocking.

- **Registry** (packet lines 56-62) vs.
  `POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`: "phase A reads
  only the Butlers top-level README, the pillar README indexes it names and
  Git tree metadata; phase B reads only the exact Git objects in the
  resulting revision-bound manifest" matches `typedAuthority.readAuthority`
  verbatim in substance. "Empty write surface, no database access, no network
  access, no observed-code execution, no working-tree reads" matches
  `writeSurface: []`, `databaseAccess: []`, `networkAccess: []`,
  `executeObservedCode: false`, `workingTreeRead: false` exactly. "The
  implementation path it names does not exist yet; adopting the entry
  authorizes no implementation" matches `implementationStatus` verbatim in
  substance. The source's `phaseA.fixedSeedPaths` is literally
  `about/README.md`, not a repository-root `README.md`; other repo artifacts
  (`docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-RAW.md`,
  `openspec/changes/polaris-project-wide-butlers-model/design.md`) already
  refer to this same file as Butlers' "root index" / primary project
  document, so the packet's plain-English "top-level README" is a defensible
  paraphrase of an established internal term, not a misdescription of a
  literal filesystem path claim the owner would act on differently.
  [Observed] Non-blocking.

- **"What this does and does not do"** (packet lines 64-76) vs.
  `ACT-SEMANTICS.md` and `CANDIDATE-REPORT.md`: "None grants PWB
  implementation authority (task 1.8), write, egress, execution, deployment,
  release, recovery, mission, second-repository, autonomous or multi-user
  authority" (`ACT-SEMANTICS.md`) is reproduced essentially verbatim at packet
  lines 69-71. "No body read occurs until separate PWB implementation
  authorization (task 1.8) exists and an implementation evaluates the acts
  under PWB-REQ-005" (`CANDIDATE-REPORT.md`) matches packet lines 72-73.
  [Observed] PASS, no overstatement found.

Overall for criterion 3: **no sentence found that overstates authorization**
(nothing claims more access, trust or effect than the source files grant).
One soft scope-compression (policy's multi-boundary enforcement vs. "before
anything is modeled") and one omitted clause (consent's "revocation does not
erase prior records") are the only understatements found, both non-blocking
because the owner-relevant guarantee is still stated correctly elsewhere in
the same section.

## 4. Readability

Word count: 702 words (`wc -w`). Line count: 105 lines including code fences
and blank lines (`wc -l`). This is concise for three distinct authorization
grants with a trust-model disclosure, an evidence trail and literal-response
instructions; nothing reads as padding, and no owner-relevant fact looks
prunable without loss.

Findings:

- **Line 22 / 66 / 69 — "PWB" is never expanded anywhere in the packet.**
  `grep -n -i PWB` over the packet returns 8 hits (lines 5, 7, 22, 33, 66, 69,
  81, 87), all bare uses of the acronym (`PWB-EFFECT-ACTS-MANIFEST.txt`, "the
  signed PWB source population", "PWB-REQ-005", "PWB implementation") with no
  sentence saying what PWB stands for (Polaris' project-wide Butlers
  behavioral model, per AGENTS.md's own vocabulary — never stated in the
  packet). The packet's opening paragraph (lines 11-16) does explain *what is
  being asked for* in plain sentences without needing the acronym, so a
  reader can act on the packet's instructions without knowing what "PWB"
  expands to — but a careful non-Syzygy reader hitting "PWB-REQ-005" (line 22)
  or "PWB implementation (task 1.8)" (line 69) has no way to resolve the
  acronym from the packet alone. Non-blocking (the packet's action items don't
  depend on knowing the expansion) but worth a one-clause fix ("PWB — the
  project-wide Butlers behavioral model" on first use).
- **Line 69 — "task 1.8" is a bare internal backlog identifier** with no
  plain-language description beyond "PWB implementation... is a separate
  act." A reader can't tell what task 1.8 actually is, only that it's some
  other future act. Non-blocking — the sentence is actionable as written
  ("this packet does not authorize implementation; that needs a separate
  act"), the identifier is decorative context, not a fact the owner must
  parse.
- **Line 56 — the codename "polaris-butlers-project-shape"** (and elsewhere
  "Polaris" is implicit in file paths, e.g. lines 5, 26, 40, 53) is never
  defined as a term in the packet. Given the consent record the packet quotes
  verbatim at lines 29-30 is the owner's *own* statement about Butlers
  observation, and "Polaris" is a term the owner has used throughout this
  project's history (per AGENTS.md, one of the three named human surfaces),
  this is very likely already familiar vocabulary to this specific owner, and
  the sentence around it (line 56-58) is self-contained without needing to
  parse the codename. Non-blocking.
- **Line 16 in isolation** ("You may perform one, two or all three; a body
  read needs all three") could be read, on its own, as implying the three
  acts are *sufficient* for a body read. The very next section (lines 64-76)
  immediately corrects this ("They do not authorize PWB implementation (task
  1.8 is a separate act) ... Nothing reads Butlers as a result of these
  acts"), so a reader who finishes the one-page packet is not misled — but a
  reader who stops after "What you are being asked" would be. Non-blocking
  given the packet is short enough that a reader is very likely to reach the
  correcting section, but worth tightening line 16 to "a body read needs all
  three, plus a later, separate implementation authorization."
- No jargon found that blocks the owner from writing a correct response —
  every one of the three response lines (lines 98, 101, 104) is copy-pasteable
  without needing to parse any identifier's meaning, and the digest-binding
  mechanism is explained in plain sentences (lines 14-15, 93-95) without
  needing SHA-256 mechanics explained further to a "technically literate"
  reader.
- Length: no cuts identified that would lose an owner-relevant fact; the
  Evidence section (lines 78-89) is the most compressible if the owner
  already trusts the review pipeline, but removing it would remove the only
  place the packet points to independent confirmation, so it is left as is.

**No blocking readability defect found.**

## 5. Instructions — cross-checked against `record_pwb_effect_acts.py`

Packet claims, lines 74-76: "Each act is recorded in
`.syzygy/governance/decisions/` and appended to `ACCEPTANCE-ACT-RECORD.md`,
with a tag on the recording commit. Editing any of the three files afterwards
breaks its act; changes go through a new act." Read against the script:

- `record()` (lines 303-331) writes exactly two files per act:
  `act.record` — a dedicated file under `.syzygy/governance/decisions/`
  (line 42: `pathlib.Path(".syzygy/governance/decisions") / record_name`) —
  and `AGGREGATE_REL` = `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`
  (an appended block, per `expected_outputs`'s `prefix + "\n\n" +
  render_aggregate_block(...)`, lines 289-300). Matches "recorded ... and
  appended to `ACCEPTANCE-ACT-RECORD.md`" exactly. [Observed]
- `record()`'s final print (line 329-330): `"next: git add the two records,
  commit, then tag pwb-{act.act_type}-signed-{date} on that commit"` — matches
  "with a tag on the recording commit" exactly (the tag names the commit
  carrying the two just-written records). [Observed]
- `validate_artifact()` (lines 126-149) recomputes each artifact's current
  sha256 from its live bytes on every validation call and rejects a mismatch
  against both the owner's argument and the frozen-subject bytes — so an act
  performed against an edited artifact fails validation; and
  `ACT-SEMANTICS.md` states explicitly "an artifact edited after its act is
  an artifact with no act," which `render_act()`'s "Effect" section
  reproduces verbatim ("An edit to the artifact breaks this act's digest
  binding; changes travel as a new act.", lines 242-243). Matches "Editing
  any of the three files afterwards breaks its act; changes go through a new
  act" exactly. [Observed]
- The packet's "you may perform one, two or all three" (line 16) matches
  `ACTS` being three independent dict entries with independent `validate()`
  calls and independent record files — nothing in the script requires all
  three to be performed together. [Observed]
- `validate_packet()` (lines 152-176) additionally requires this very review
  file (`docs/reviews/R-PWB-EFFECT-ACTS-OWNER-PACKET-RAW.md`) to exist and
  contain the packet head, frozen subject, the owner's exact argument, and
  the literal strings `**EXACT VERDICT: CONFIRM**` and `**OWNER PACKET MAY BE
  PRESENTED TO THE OWNER: YES`, before any `--record`/`--check` call
  succeeds — i.e., this review is itself a load-bearing precondition the
  recorder fails closed without. This isn't a packet claim to verify against,
  but it is the reason this review exists and confirms the recorder's
  fail-closed design matches the "no act until reviewed" framing throughout
  the packet and companions. [Observed]

**Criterion 5: PASS**, instructions match script behavior exactly; no
discrepancy found.

## 6. Battery

```
python3 scripts/check_governance.py
```
Final summary line (read from output, not exit code):
```
33 OK, 19 WARN, 0 FAIL (52 checks) — counts derived, not asserted
```
0 FAIL. WARNs are pre-existing report-only/advisory checks (CG-19b, CG-22b,
CG-23, CG-24, CG-25 downgrades) unrelated to the PWB effect-acts packet.

```
python3 scripts/build_pwb_effect_acts_packet.py --check
```
Final (only) line:
```
CHECK OK: 3 rows verified; .syzygy/governance/contracts/candidates/pwb-effect-acts/PWB-EFFECT-ACTS-MANIFEST.txt matches regeneration
```

```
python3 scripts/record_pwb_effect_acts.py --selftest
```
Final summary line:
```
12 recording fixtures, 0 failing
```
All 12 fixtures PASS, including all three acts' "packet stage fails closed
while final review absent" fixture — true at the moment this battery ran,
since this review file did not yet exist on disk; the packet's own fail-closed
design is confirmed by this run, not undermined by it (once this review file
is written with a CONFIRM/YES verdict, that specific fixture's precondition
changes, which is the intended, designed effect of publishing this review).

**Criterion 6: PASS**, all three batteries green, 0 FAIL across all runs.

## Summary of findings (none blocking)

1. `PWB` acronym never expanded in the packet (lines 5, 7, 22, 33, 66, 69, 81,
   87) — non-blocking, doesn't block owner action.
2. "task 1.8" (line 69) is a bare internal identifier with no further
   description — non-blocking.
3. Codename "polaris-butlers-project-shape" / "Polaris" (line 56 and file
   paths at lines 5, 26, 40, 53) undefined in-packet — non-blocking, likely
   already-familiar owner vocabulary.
4. Line 16 ("a body read needs all three") could mislead a reader who stops
   before "What this does and does not do" (lines 64-76) into thinking the
   three acts alone suffice — non-blocking, corrected two sections later in a
   short, one-page packet.
5. Policy summary (line 43, "before anything is modeled") slightly compresses
   the policy's seven-boundary `ingestBoundaries` scope — non-blocking, the
   owner-relevant guarantee ("raw bodies never stored/logged/rendered/
   returned/sent") is still stated fully and correctly at lines 50-51.
6. Consent summary (lines 37) omits the source's "revocation does not erase
   prior observation records" clause — non-blocking omission, not an
   overstatement.

No finding rises to blocking: exactness (1), honest trust model (2), scope
honesty (3) and instructions (5) all fully pass; readability (4) has no
blocking defect. All three governance batteries are green.

**EXACT VERDICT: CONFIRM**
**OWNER PACKET MAY BE PRESENTED TO THE OWNER: YES**
