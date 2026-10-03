# Impact ledger — D7, held derived computation

> **Candidate — binds nothing.** The blast-radius record for
> `SEMANTIC-DELTA.md` (this directory), drafted 2026-10-03 for
> `syzygy-u05.14`. Every figure below was computed at `origin/main`
> `66d42d09`, before this package existed; the package's own files are
> outside every population. Round 1 (`REVISE`) found three coverage gaps
> in this ledger; §1a, §1b, the two RFC2 rows in §3 and the widened §4 are
> their repairs (`ROUND-1-DISPOSITIONS.md`), unconfirmed.

## 1. The trigger sweep

**Predicate** (Python `re`, case-insensitive, occurrences counted with
`findall`):

```text
human-triggered|not autonomous|no timer|background poller|autonomously on merge|autonomous trigger|self-wake|wakes? itself|post-(?:commit|merge) hook
```

**Population:** every tracked file at `66d42d09` whose path starts
`.syzygy/`, `openspec/` or `docs/`, or is `AGENTS.md`, `README.md` or
`PROJECT-STATUS.md`, and whose name ends `.md`, `.json`, `.yaml` or `.txt`:
**1,536 files.**

**Result:** **95** files carry at least one match, **346** occurrences.
**Second method:** `git grep -l -i -E` with the same alternation (ERE
group in place of `(?:…)`) over the same pathspecs returns **95** files.

**Lanes.** Each hit file is placed by the first rule that matches its path:
a `/reviews/` segment or a `-RAW.md` suffix → raw review; a `/round-`,
`/history/` or `_bootstrap` segment → historical; then by directory —
`doctrine/`, `contracts/rfcs/` (accepted contract),
`contracts/candidates/` (candidate), `decisions/`, `openspec/` (spec),
`docs/pursuits` or `docs/evidence` (evidence); anything else → other.

| Lane | Files | Occurrences | Treatment |
|---|---:|---:|---|
| doctrine | 3 | 5 | every line read; §3 |
| accepted contract | 4 | 12 | every line read; §3 |
| decision | 5 | 7 | every line read; §3 |
| spec | 5 | 5 | every line read; §3 |
| candidate | 13 | 51 | every line read; §3 |
| other | 10 | 30 | every line read; §3 |
| evidence | 15 | 141 | not read line by line: evidence is never edited to stay current |
| raw review | 27 | 61 | not read line by line: CC-REV-6 stores raws unchanged |
| historical | 13 | 34 | not read line by line: historical lane, never edited |
| **Total** | **95** | **346** | |

The last three lanes are a stated limitation, not an absence claim: a
sentence in them that D7 makes false would stay false and is not routed.

### 1a. Wrapped matches

These pages are hard-wrapped, so a two-word literal split across a line
break escapes the predicate. **Re-run:** the same alternation with every
space replaced by `\s+`, over the same 1,536 files: **95** files, **348**
occurrences — two more than §1, both wraps of "not autonomous":
`doctrine/vision.md` lines 86–87 ("…not an outward enforcer, and not" /
"autonomous.", the section intro directly above D7's anchor; row added in
§3) and one raw review in a historical round (`round-2026-08b/reviews/`,
not edited).

### 1b. "Autonomous behavior" exclusions

Many acts exclude "autonomous behavior", a form the §1 predicate does not
reach. **Predicate:** Python `re`, case-insensitive,
`autonomous\s+behaviou?r`. **Population:** tracked `.md` files at
`66d42d09` under `.syzygy/governance/decisions/`,
`.syzygy/governance/doctrine/`, `.syzygy/governance/contracts/rfcs/` and
`openspec/`, excluding `-RAW.md` files and `/reviews/` paths: **212
files.** **Result:** **10** files, one occurrence each — seven acts in
`decisions/` (`POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md`,
`PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md`,
`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`,
`PWB-MACHINE-VIEW-AMENDMENT-ACT.md`, `PWB-OPENING-BAND-SCENARIO-ACT.md`,
`PWB-STATE1-AMENDMENT-ACT.md`, `PWB-TRUTH-READINESS-AMENDMENT-ACT.md`) and
three specification files
(`openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md`
and `proposal.md`, `openspec/changes/three-surface-poc-experience/proposal.md`).
**Disposition:** none is made false — each excludes autonomous behaviour
from what it authorizes, and D7 authorizes nothing. But D7's heading
("delegates no decision … inside VIS-4's stated bounds") narrows what a
reader may count as "autonomous behavior" under them. The guard is that
each act confines new behaviour to its own signed scope, so no D7
behaviour ships under any of them without its own implementation
authority (packet §4). Every file in this population is act-bound or a
signed specification and is not edited on any arm.

## 2. The notification sweep

`OWNER-DECISION-PACKET.md` §3 says notification has no licence anywhere.
**Predicate:** case-insensitive `notif`. **Population:** every tracked file
at `66d42d09` under `.syzygy/governance/doctrine/`,
`.syzygy/governance/contracts/rfcs/`, `.syzygy/governance/decisions/` and
`openspec/`: **229 files.** **Result:** 1 file,
`decisions/PROCESS-LESSONS.md` line 67 ("whose final message arrives via
task notification"), which is about agent tooling and licenses nothing.
**Second method:** `git grep -c -i -E notif` over the same tree paths, 1
file, the same one.

## 3. Authority-lane hits and their disposition

"Consistent" means the sentence stays true, unedited, after arm A.

| File | Line(s) | What it says | Disposition |
|---|---|---|---|
| `doctrine/vision.md` | 45; 86–87 (wrapped, §1a); 105 (2 hits) | the thesis diagram's "human-triggered work" edge; the section intro "…and not autonomous."; the "Not autonomous" bullet | 105 is D7's anchor; 45 consistent; 86–87 consistent: it summarizes the bullet below, and D7 places its class inside VIS-4's stated bounds, so "not autonomous" stays true of Syzygy — on a Q1 "inside" ruling, which section 1's text requires anyway |
| `doctrine/architecture.md` | 332 | the loop is human-triggered | D7's anchor |
| `doctrine/v1.md` | 89 | "Human-triggered propagation at full breadth" | consistent: D7 forbids unprompted dispatch |
| `contracts/rfcs/RFC-0002/reconciliation-chain.md` | 26 (sources list); 245, 247 | RFC2-19, "never autonomously on merge events" | **stays stricter, and binds every D7 trigger whose evaluation captures a merge fact**, not only the hook (packet §4, §6 item 1) |
| `contracts/rfcs/RFC-0002/reconciliation-chain.md` (no predicate match; found by round 1) | 155–157 | reconciliation-pending attaches "at the first evaluation that captures the merge fact (inside RFC2-19's deliberately triggered passes — never on a live merge event)" | **binds D7's headline example**: an unprompted evaluation capturing a merge fact contradicts it. D7's text "relaxes no contract that requires a deliberately triggered pass", so arm A leaves the clause true and the example unlawful until RFC2 is amended (packet §4) |
| `contracts/rfcs/RFC-0004/named-adapters.md` | 26, 420, 433, 435, 492, 526 | RFC4-16, "never an autonomous trigger"; observation passes are human-triggered | consistent: no clock trigger |
| `contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md` | 26 | cites the human-triggered loop as a source | consistent |
| `contracts/rfcs/RFC-0005/admission-and-boundary.md` | 323, 590 | RFC5-11 and its q6: revocation forces an evaluation | D7's precedent (packet §3) |
| `decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` | 56 (2 hits) | P-69, "No timer or background poller on any arm" | consistent; restated generally |
| `decisions/BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md` | 25 | missions are "not autonomous vision steering" | consistent; precedent for arm B |
| `decisions/DOCTRINE-AMENDMENT-D5-READABILITY.md` | 40 | names the bullet as a D3 anchor | historical record of an adopted act; consistent |
| `decisions/THREE-SURFACE-POC-MODE-DIRECTION.md` | 18, 31 | "work dispatch is human-triggered" | consistent |
| `decisions/THREE-SURFACE-POC-REDESIGN-DIRECTION.md` | 46 | the loop is human-triggered | consistent |
| `openspec/changes/polaris-manifesto-generation/` (3 files) | proposal 24; spec 1661; WORK-STATE-CONTRACT 85 | generation is human-triggered; "not an autonomous polling mandate" | consistent: D7 opens no egress and adds no polling; a rehearsal is not licensed by D7 alone (packet §6.2) |
| `openspec/changes/polaris-project-wide-butlers-model/` coverage matrix and part (2 files) | 158; 144 | RFC2-19 believed not applicable to PWB | consistent; act-bound bytes, not edited on any arm |
| `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`, `…-DRAFT.md` | 27 hits | D3 and its superseded draft | composition in packet §1.3 |
| `contracts/candidates/rfcs/` mirrors (4 files) | as the accepted copies | candidate mirrors of the rows above | same dispositions |
| `contracts/candidates/02-OWNER-DIRECTION-RECORD.md` | 23, 34 | OD-R10-2, bounded missions | consistent |
| `contracts/candidates/01-REV9-ADVERSARIAL-FINDINGS.md` | 84 | historical finding on propagation posture | consistent |
| `contracts/candidates/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md` | 314 | missions are human-triggered under existing doctrine | consistent |
| `contracts/candidates/fixtures/context-selection-6-doctrine-amendment.md` | 15, 33, 110 | a fixture over D3's draft insertions | consistent; a fixture, not edited |
| `contracts/candidates/policy-candidates/TERM-REGISTRY.md` | 1475–1476 | an open authority question about RFC-0010 and "not autonomous" | consistent; the term "held derived computation" would enter here after adoption |
| `contracts/candidates/pwb-missing-currency-disclosure-scenario/SEMANTIC-DELTA.md` | 172 | "No timer, background poller or ambient-clock transition is introduced" | consistent |
| `contracts/candidates/rfcs/RFC-0010/README.md` | 167 | approved missions satisfy the human-triggered loop | consistent |
| `.syzygy/intent/OVERVIEW.md` | 107 | "The loop stays human-triggered. Autonomy beyond doctrine's stated bounds is…" | consistent; act 4's unperformed argument, not edited on any arm |
| `.syzygy/map/topology-candidates/01-system-context.md` | 42 | owner "triggers propagate/observation passes" | consistent |
| `.syzygy/map/topology-candidates/06-intent-to-reconciliation-flow.md` | 12, 14, 34 | "nothing here runs autonomously"; RFC2-19 | consistent: D7's class is not a loop pass |
| `PROJECT-STATUS.md` | 97, 108, 250 | POC actions are human-triggered | consistent |
| `README.md` | 34, 115, 132, 240 | the loop remains human-triggered | consistent |
| `docs/THREE-SURFACE-POC.md` | 169 | a human-triggered action | consistent |
| `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` | 48 (3 hits), 1158 | Q4: "Arm (a), no timer" | consistent |
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 117, 245, 502, 666 | dispatch and the materialize action stay human-triggered | consistent; Q3's pure drafter (line 115, no match) is D7's precedent (packet §3) |
| `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md` | 336 | "not autonomous agent coordination" | consistent |
| `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md` | 8 hits | the second evaluation is human-triggered | consistent; D7 would let the second evaluation also run on an unrequesting human act, which M12 does not need |

No authority-lane sentence is made false by arm A [Inferred: from reading
every line listed]. The RFC2 rows are the reason that holds: D7 is drafted
to yield to them rather than to amend them, at the cost of its headline
example. A sentence elsewhere that confines computation to a deliberate
pass without using a §1 literal would be missed by this sweep; round 1
found one (RFC2 line 157), and the predicate is not claimed complete.

## 4. Derived artifacts that read doctrine bytes

Found by a sweep for the two doctrine digests (`git grep -F`, every tracked
file), and by a reader sweep: Python `re`
`governance/doctrine|doctrine/(vision|architecture)\.md` over every tracked
file at `66d42d09` under `apps/`, `packages/` and `scripts/` ending `.ts`,
`.py`, `.js`, `.mjs`, `.json`, `.yaml` or `.yml` — **417 files, 11
readers** — plus the generated YAML index below. Of the 11: the two
generators and the two scripts in the table; `scripts/check_governance.py`
(CG messages naming `doctrine/vision.md` as a rule's home, no bytes read);
five tests and one script using a doctrine path as a fixture path
(`apps/three-surface-poc/src/git-blob-batch.test.ts`,
`packages/cap1-conformance/src/req-023`, `req-061` and
`req-integration` conformance tests, `scripts/polaris_generator_approval.py`),
none reading today's bytes; and the self-corpus row below.

| Artifact | Reads | On application of arm A |
|---|---|---|
| `DIRECTIVE-REGISTER.md` (generated by `scripts/build_directive_register.py`) | file and line of every VIS identifier | line numbers after `vision.md` line 107 shift; regenerate with `--write`; `--check` is in the canonical battery |
| `contracts/candidates/05-CONTRACT-INDEX.yaml` (generated by `build_contract_index.py`) | a `words` count for each doctrine file | regenerate; `--check` is in the battery. Several PWB builders read this index; whether a doctrine word count reaches any of their manifests is **[Unknown]** here — the battery run after application decides it |
| `scripts/check_polaris_response_ceiling_reading.py` | quotes "No evidence means Unknown, not success" from `vision.md` | unaffected: the quoted bytes do not move |
| `scripts/record_polaris_understanding_adoption.py` | `vision.md` in its frozen-path set, read at the C1 commit | unaffected: it reads history, not today's bytes |
| `docs/evidence/polaris-understanding-reconciliation-2026-09-28/` (3 files) | the `vision.md` digest as reviewed on 2026-09-28 | unaffected: a record of the bytes reviewed then |
| `apps/three-surface-poc/src/polaris-generation/self-corpus.ts` (and its test) | doctrine Markdown as part of the self-governance corpus, read "at the pinned commit" only | unaffected: a run pinned to a later commit gets a new corpus identity digest, which is a fact of that run, not a break |

Neither doctrine digest occurs in any performed act's manifest [Observed:
the only digest citers are the three evidence files above].

## 5. Observations routed, not repaired

Outside this packet's scope; each goes to the coordinator in the worker
report. None is edited here.

1. **`syzygy-u05.2` (N2) describes the post-commit hook as a lawful trigger
   today** ("every trigger is a human act or a human-installed post-commit
   hook in the owner's own Butlers checkout"). By packet §6.1 the hook is
   not lawful on any current path, D7 or no D7. The human-triggered route
   in the same bead is unaffected.
2. **The 2026-10-03 roadmap does not carry the live fleet observability
   mandate.** `docs/plans/2026-10-03-smooth-example-roadmap.md` has 0
   case-insensitive `fleet` matches [Observed, `grep -c -i`, confirmed by
   reading its section list]. `vision.md` says "every roadmap must carry
   that as a named, sequenced item"; whether a page that calls itself "a
   plan" is a roadmap in that sense is the owner's call. Packet §5's
   entry criteria are offered for whichever roadmap the owner names.
3. **The pursuit's citation `v1.md:82`** points at "## V1 — the harness"
   since the D5/D6 restyles; the deferral row is now line 103. The pursuit
   dossier is evidence and is not edited.
4. **`.syzygy/intent/OVERVIEW.md` line 107** stays true after arm A, so no
   propagation is needed; it is act 4's unperformed argument and would need
   the act-4 digest re-minted if anyone ever chose to edit it.
