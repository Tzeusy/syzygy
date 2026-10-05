# Impact ledger — D9, SEC-3 and the owner's attended agent session

> **Candidate — binds nothing.** This is the blast radius of the amendment
> drafted in `SEMANTIC-DELTA.md` (this directory), repaired after rounds 1
> and 2. Every figure names the commit it was measured at. Re-run each one at
> the reviewed commit; never copy it.

**Commits used below.**

- `eb7be564605c98fcc7b5f2464b200382dd1bfe39` (`origin/main`, committed
  2026-10-05 23:57 +0800): the classified sweep population. It excludes this
  package's own branch commits, so the package does not count itself.
- `5863d470931625e4fbbb012f8e79ef6eabb6411a` (`origin/main` on 2026-10-06):
  the commit of the §4 application probe and of the §1 re-measurement. §1
  gives the sweep's change from `eb7be564`.
- `5126610b`, the next `origin/main` commit, is the round-2 repair's base. It
  adds four files' changes only: the owner's round-2 direction, the round-2
  raw, a `decisions/README.md` row and the `docs/README.md` campaign row. No
  doctrine, contract or policy byte differs from `5863d470` [Observed:
  `git diff --stat`].
- The reviewed commit adds this package's six files and the P-103 register
  row to the `5126610b` population [Inferred from the diff; a reviewer
  re-runs it].

## 1. The identifier sweep

**Population:** every path in `git ls-tree -r -z --name-only eb7be564`,
**2,348** paths, read as blobs at that commit. Four do not decode as UTF-8,
so **2,344** were searched.

**Predicates** (Python `re`, case-sensitive, over whole file text):

| Name | Regex | What it catches |
|---|---|---|
| exact | `(?<![A-Za-z0-9-])SEC-3(?![0-9])` | `SEC-3`, but not `CC-SEC-3` or `SEC-30` |
| ccsec | `CC-SEC-3(?![0-9])` | the craft clause that restates SEC-3 |
| range | `(?<![A-Za-z0-9-])SEC-[12]\s*(?:\.\.\.?\|…\|–\|—\|-\|through\|to)\s*(?:SEC-)?[345](?![0-9])` | continuation forms: `SEC-1…SEC-5`, `SEC-1…5`, `SEC-1–SEC-5`, `SEC-1 through SEC-5` |
| slash | `(?<![A-Za-z0-9-])SEC-(?:\d[/,] ?)+\d`, kept only when the match contains `3` | `SEC-2/3`-style runs |

The `\|` in the table is escaping; the regex alternation is a bare `|`.

**Result:** **241** files match at least one predicate: exact 202, ccsec 4,
range 58, slash 5 (a file may match several). Lanes are assigned in the order
listed, so a `reviews/` file inside a `round-*` directory counts as
historical.

| Lane | Files | Disposition |
|---|---|---|
| Historical (`round-*`, `contracts/candidates/history/`, `_bootstrap/`) | 42 | never authority |
| Retained reviews (`-RAW.md` and `reviews/` outside rounds) | 28 | raw output, stored unchanged (CC-REV-6) |
| Doctrine | 3 | §3.1 |
| Accepted contracts (`contracts/rfcs/`) | 21 | §3.2 |
| Craft-and-care | 4 | §3.3 |
| Decisions (excluding `-RAW.md`) | 4 | §3.5 |
| Specifications (`openspec/`) | 9 | §3.4 |
| Candidates (rest of `contracts/candidates/`) | 86 | §3.6 |
| Topology and intent (`.syzygy/map/`, `.syzygy/intent/`) | 5 | §3.6 |
| Evidence and pursuit records (`docs/evidence/`, `docs/pursuits/`) | 20 | records of past bytes; never edited |
| Design notes (`docs/design/`) | 8 | §3.6 |
| Code and generators (by extension) | 5 | §3.6 |
| Root pages and skills (`AGENTS.md`, `README.md`, `SECURITY.md`, `DIRECTIVE-REGISTER.md`, two `heart-and-soul/SKILL.md`) | 6 | §3.6 |

The lanes sum to 241. Round 1 measured 240 at `b60e6cd2`. The one extra file
is `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`, retained on
`main` since [Observed].

**Second method (rule 2): a term sweep with no identifier.** Predicate:
`observed[- ](?:project[- ])?code|execution[- ]profiles?|execut\w* (?:the )?observed|run(?:s|ning)? observed`,
case-insensitive, over the same 2,344 files at `eb7be564`. It matches **250**
files. Lines in the doctrine, decisions, `openspec/`, craft-and-care,
topology and root lanes, from files the identifier sweep did *not* match,
were read one by one. Each is one of three things: a grant list ("grants no
… observed-code execution"), a statement about Syzygy's pipeline, or a
profile-contract row. The ones that bear on D9 are in §3.

Round 2's version of this paragraph said that neither sweep finds
`capture-test-artifact-main.ts`. That was false: the term sweep matches it
at line 16, "executing observed", in its usage text. The round-1 read of
term hits covered only the lanes named above and skipped the code lane.
The code-lane term hits have now been read, at `5863d470`: every file with a
code extension (`.ts`, `.tsx`, `.js`, `.mjs`, `.py`, `.sh`, `.json`,
`.yaml`, `.yml`) outside `docs/evidence/` and `docs/pursuits/`. That is 17
files. Two are the capture tool, `capture-test-artifact.ts` (line 5,
"executes observed") and `capture-test-artifact-main.ts` (line 16). Two are
generators that name the `execution-profiles` module path
(`05-CONTRACT-INDEX.yaml`, `build_task_router.py`), and one is
`check_governance.py` line 2310, which names the same path. Five render or
test the phrase "observed code structure" (`evaluation-footer.ts`,
`orrery.ts`, `orrery.test.ts`, `polaris-copy.ts`, `test-model-fixture.ts`).
`worker-change-observation.ts` line 167 states that the observer never
executes observed code. The six remaining scripts either quote grants of
"no … observed-code execution" or mutate an `executeObservedCode` authority
flag in a fixture (`build_provider_route_messages_api_entry.py`,
`build_public_admission_registry_entries.py`, `build_pwb_effect_acts_packet.py`,
`polaris_generator_approval.py`, `record_pwb_behavior_amendment_acts.py`,
`record_pwb_truth_amendment.py`). Only the capture tool executes observed
code [Observed: each line read]. The round-2 review's spawn-call sweep
reached the same result by a different method.

**Re-measured at `5863d470`.** The same population rule gives **2,353**
paths, of which **2,349** decode. **244** files match the identifier
predicates (exact 205, ccsec 5, range 59, slash 5). The set at `eb7be564` is
a subset, and the three additions are two retained raws on `main` since,
`docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md` and
`docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-2-RAW.md` (retained
reviews), and `docs/README.md`, whose review-campaign table now names the D9
campaign (a docs index; unchanged by D9) [Observed]. The term sweep matches
**252** files. The lane classification above is kept at `eb7be564`.

## 2. Line-number citations of `security.md`

Arm A adds 40 lines to `security.md`: SEC-4 moves from line 72 to 112, and
SEC-5 from 85 to 125. Without the credential lines, it adds 37, and SEC-4
lands at 109. Arm W adds 37 lines (34 without the credential lines). The
arm A figures with the credential lines are [Observed] in the application
probe (§4); the rest are computed from block length.

The predicate
`` security\.md`?(?::\s*|\s+lines?\s+|\s*L)\d+|security\.md#L\d+ ``
over the §1 population at `eb7be564` finds **66** matches in **29** files:

- 5 are `DIRECTIVE-REGISTER.md` rows, which are regenerated.
- The other 61 cite lines 10 to 85.
- Only one of them cites past line 61:
  `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`, line 290,
  "(security.md:85-96)", which is SEC-5.

That raw is stored unchanged, so after application its locator names old
line numbers, as the earlier pre-D6 citations already do. (Round 1's "57" was
the count without the register at `b60e6cd2`. The total there was 62.)

## 3. Authority-lane hits, and what D9 does to their meaning

"Unchanged" means the cited text reads the same after D9 under both arms.
Where the arms differ, the row says so. "[Inferred]" marks the drafter's
judgement, which a reviewer should test.

### 3.1 Doctrine

| Site | What it says | After D9 |
|---|---|---|
| `security.md` 61 | SEC-3 | the subject |
| `security.md` 3–4, 7–8 | "treats observed code as untrusted everywhere"; Syzygy "may execute observed-project code" | unchanged |
| `v1.md` 119–120 | "executing it is opt-in, profiled, and blocked until the execution-profile RFC is accepted (SEC-3)" | optional clause (b). The line is under "Platform and audience", describes Syzygy, and stays true of Syzygy without (b) [Inferred]. (b) stops it reading as universal. The cost is that it puts a path that is not Syzygy's own execution into a list about Syzygy's platform |
| `README.md` 74–75 | rules SEC-1–SEC-5 on "executing observed code" | unchanged |

### 3.2 Accepted contracts

Each file under `contracts/rfcs/` has a byte-identical copy under
`contracts/candidates/rfcs/`. At `eb7be564`, `diff -rq` reports only
`RFC-0010` and `RFC-0011`, which exist in the candidate tree alone [Observed].
Each row therefore covers both copies.

| Site | Quoted | After D9 |
|---|---|---|
| **RFC5-12** (`RFC-0005/consent-egress-secrets.md` 108–109) | "**Execution consent** — per project: the owner's approval Decision for a specific execution-profile version (RFC5-18). Absent: no observed code runs." | **Effect changes in the permitted case, under both arms [Inferred].** The owner's recorded choice is not an execution consent, and no profile is approved. Yet observed code runs: under arm A on Syzygy's instruction, under arm W with or without it. The clause could be read as limited to consent given *to Syzygy*, but unlike RFC5-18 it has no RFC5-19-style sentence to rest on. Packet Q3 |
| **RFC5-24** (`RFC-0005/admission-and-boundary.md` 354–362) | adapter credentials are "… stored under SEC-5 discipline (never in any indexed store or surface); and" "never visible to observed-project code." | **Effect changes in the permitted case unless Q3(b) is adopted [Inferred].** The limb is not limited to profiles; the profile-only rule is the separate "injection prohibition" sentence after it. With Q3(b)'s condition, the limb stays true: Syzygy keeps its typed-adapter credentials where "neither the session nor any process it starts, directly or not, can read it at the operating-system level, for as long as any of them runs". That reaches a server or background job the session leaves running, which round 2 found the earlier wording did not (F2). An agent's own tool-permission rules do not satisfy the condition. [Inferred: a grep of `apps/` and `packages/` finds no adapter credential that Syzygy holds today. The dossier mode makes no provider call and holds no provider credential. The daemon holds a machine-client credential, which is not RFC5-24's population.] Packet Q3 |
| RFC5-18 (`execution-profiles.md`) | "Observed-project code executes only when all of" (a)–(e) | Unchanged [Inferred]. RFC5-19's last bullet ("profiles govern only code Syzygy itself launches"), RFC5-18(d)'s "launching principal" and the module diagram all scope the gate to Syzygy's launches. Under arm A, a Syzygy instruction acted on by a session the owner started is not Syzygy launching. A session Syzygy starts is excluded by the text |
| RFC5-19 | "untrusted everywhere, regardless of who owns the project"; reading outside evidence "is observation, not execution" | unchanged. Arm A's actor matches RFC5-19's "code Syzygy itself launches", extended to Syzygy's instructions. Arm W's actor-free exception list makes the CI runs RFC5-19 presupposes into doctrine violations [Inferred] |
| RFC5-20; §4 case 8 | "no ambient credential is ever inherited (SEC-3's named violation)"; "A profile inheriting the host environment 'for convenience' (SEC-3's named violation)" | unchanged. The named violation keeps every byte and still governs every profile |
| §4 case 7 (`execution-profiles.md` 263–265) | "Observed-project code executing before acceptance, or under an unapproved profile version; the owner's own repository running unprofiled 'because trust is assumed.'" | unchanged [Inferred]. The permitted case assumes no trust: the code "stays untrusted", nothing resting on it exceeds Inferred, and it runs because the owner chose a disclosed, uncontained run, not because the repository is the owner's |
| RFC5-21, RFC5-22, RFC5-23 | isolation floor, destructive-operation gates, lifecycle | unchanged. They bind profiles. The permitted case has none of their guarantees, and D9's cost bullet says so |
| RFC5-12 / RFC3 `manifests-and-namespace.md` 258–264 (consent scope "execute (SEC-3)") | the execution-consent class | the text is unchanged; the effect is as in the RFC5-12 row |
| RFC-0005 non-clause prose: `README.md` 105–107 ("no observed-project code executes until this RFC is accepted and a per-project profile exists (SEC-3)"), `README.md` 130–131 ("**No observed-project code runs without an approved execution profile** (module 3, RFC5-18) — the owner's own repositories included."), `execution-profiles.md` 30–31 ("No observed-project code executes until RFC 0005 is accepted and a per-project profile exists (SEC-3).") | three summary sentences, none a clause | **Literal tension, not resolved [Inferred].** The two README sentences sit under that README's rule "If this map and a clause disagree, the clause wins". `execution-profiles.md` 30–31 sits in the module head, *above* that module's §0, whose rule ("If this section and a clause disagree, the clause wins") is placed below it, so neither rule strictly covers it. All three are prose, not clauses, and the clause (RFC5-18 read with RFC5-19) is scoped to Syzygy. Packet Q3 arm (c) would conform them |
| RFC-0005 `README.md` 199–205 | the guarded failure mode includes "the test runner inheriting the host's SSH agent" | **D9 permits exactly that** in the permitted case, disclosed and uncontained. This is non-clause rationale. It is unchanged in text and becomes incomplete as a description: the attended case is the recorded exception it does not mention |
| RFC3-16(a) and its users: RFC2 `challenge-lifecycle.md` 162; RFC3 `governance-homes-and-owner-acts.md` 233, 478; RFC5 `consent-egress-secrets.md` 68, 200; RFC5-25; RFC7 `narrative-contract.md` 448, 531; RFC7 `rendering-and-surface.md` 361; RFC8 `accounting-reconciliation-and-release.md` 457; RFC8 `state-vocabulary-and-cost.md` 205; RFC9 `interaction-parity-and-release.md` 391; RFC4 `named-adapters.md` 229 | "SEC-3's untrusted actor class", extended to what fleet workers commit | unchanged. The attended session is in that class, and nothing it writes is trusted (see also the owner's records ruling, `POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`) |
| RFC4-12, RFC4-13 (`named-adapters.md` 150–162, 363, 501); RFC-0004 `README.md` 232, 263 | Syzygy's observers parse statically and never execute | unchanged. RFC4-13's cap ("unverifiable origin caps at `report-fact`") agrees with "never Observed" |
| RFC9-33 (`visual-grammar-and-lenses.md` 306–309, 702, 735) | the Runtime lens "is hard-gated by SEC-3 through RFC 0005's execution profiles" | unchanged. D9's claims are Inferred and open no class of captured-trace evidence |
| `Serves:` and routing lines (RFC-0001 953; RFC-0002 `README.md` 33, 214, `challenge-lifecycle.md` 26; RFC-0003 27; RFC-0004 `README.md` 31, `named-adapters.md` 25; RFC-0005 `README.md` 30, 175, 196–198, `execution-profiles.md` 3, 25, 89, 103, 135, 172, 267; RFC-0007 `README.md` 30, `narrative-contract.md` 27, `rendering-and-surface.md` 25; RFC-0008 `README.md` 32, `state-vocabulary-and-cost.md` 27; RFC-0009 `README.md` 33, `semantic-geography.md` 26, 838, `visual-grammar-and-lenses.md` 27) | citations | unchanged (rule 5: a citation is not a reliance) |

### 3.3 Craft-and-care

| Site | What it says | After D9 |
|---|---|---|
| `security-and-secrets.md` CC-SEC-3 (63–82) and its preamble (5–8) | "Observed code never executes outside an accepted profile"; "'Run the project's own test command to get better evidence' is exactly the tempting violation" | **Narrower than amended doctrine, and the dossier brief is the case it names.** The brief is a Syzygy change, which CC-SEC-3 binds ("Every change must exhibit…"). Telling an agent it may run the project to observe its behaviour is literally the "tempting violation". The file's own rules settle the conflict for now. A sentence going beyond SEC-1…SEC-5 "is a Syzygy addition and says so", and this one carries no such marker, so it is a paraphrase, and "Doctrine's text prevails over any paraphrase here" (line 21). It would still stand as a false restatement. Its digest is recorded in `policies/craft-and-care/INSTALL-RECORD.md`, so only a policy amendment changes it. Packet Q4 |
| `README.md` 24, 60, 119; `engineering-bar.md` 148–149; `review-and-documentation.md` 37 | range citations; "untrusted observed code" | unchanged |

### 3.4 Specifications

| Site | After D9 |
|---|---|
| PWB-REQ-001; PWB-REQ-006 (`primary: SEC-3`); PWB-REQ-014 | unchanged. They constrain Syzygy's own reads and renders |
| POC-REQ-002; POC-REQ-021 (`primary: SEC-3`) | unchanged |
| The POC's `CONTRACT-COVERAGE.md` RFC5-18 row ("POC never executes Butlers code, only observes it") | unchanged in text. It is contradicted today by the capture tool (§3.6), independent of D9 |
| Polaris generation: base requirements "Versioned interchange and reference integrity", "Protected audit and prospective revocation" and "Provenance-bound source policy"; overlay requirements "Versioned interchange and reference integrity" and "Accounted unfamiliar-project discovery"; `SOURCE-POLICY.md` 13–17; `APPLICABILITY-DECISIONS.md` 44–47 | unchanged. Syzygy's generator "never executes observed-project code" |
| The four `GOVERNING-DEPENDENCIES.md` unions; Capability 1 `design.md` 15 | generated or range citations; unchanged |
| **Candidate** `openspec/changes/polaris-dossier-local-agent-mode/` (PR #353, not on `main`) | **The one dependent.** Its brief's execution rule must carry the chosen arm's conditions word for word: recorded first, Inferred, every reported command disclosed, and, if Q3(b) is adopted, no adapter credential readable. Under review-1 rulings item 1, it may not be signed until D9 is adopted |

### 3.5 Decisions

| Site | After D9 |
|---|---|
| `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md` 33, 56–61 | unchanged. Line 61, "Syzygy itself still never executes observed project code (SEC-3)", stays true under both arms |
| `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md` | the direction D9 answers |
| `POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md` 216–217, 483 | unchanged (PWB-REQ-006's warrant) |
| `README.md` 84 | range citation; unchanged |
| Term-sweep hits: act records granting "no … observed-code execution"; `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-DIRECTION.md` 25; `BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` 48; `SURFACE-DECISION-RECORD.md` 244–245 | unchanged. Each limits what an act grants Syzygy, and D9 grants Syzygy no execution of its own |

### 3.6 Implementation and non-authoritative lanes

**The capture tool: a pre-existing non-conformance, disclosed, not fixed.**
`apps/three-surface-poc/src/capture-test-artifact-main.ts` runs as
`npm run poc:capture-test-artifact` (`package.json` line 18). It is
Syzygy-authored code. It spawns the real focused pytest suite on a Butlers
checkout through `spawnSync`, with no profile and the caller's environment.
`docs/THREE-SURFACE-POC.md` ("Capturing test-run evidence") calls it "a
separate, manually invoked step". Verification can then render `Verified`
from the artifact, when the commit matches, the run exits 0 and the capture
time is in range ("When verification renders `Verified`").

- [Inferred] It is non-conforming **today, independent of D9**:
  - under the current actor-free SEC-3, it is observed code outside a
    profile;
  - under RFC5-19's scoping, it is "code Syzygy itself launches", so
    RFC5-18's gate applies, and its conditions (b), (c) and (e) are unmet.
- It also contradicts the POC coverage row "POC never executes Butlers code,
  only observes it" (§3.4).
- **Arm A:** still forbidden. The tool is Syzygy launching a process, which
  is not the permitted case. The permitted case is a Syzygy *instruction* to
  an attended session; it is not Syzygy code spawning observed code.
- **Arm W:** still forbidden, by "Syzygy itself, and any process Syzygy
  launches or schedules, still runs observed code only inside a profile".
  Arm W's exception does not reach a process Syzygy spawns, even when an
  attended session invokes the tool.
- So D9 neither cures it nor makes it worse. The repair, a profile or
  retirement, is outside this package. It is tracked as bead `syzygy-4mbu`.

**`AGENTS.md` 89.** "The daemon never executes observed project code or test
suites; separate operator commands do." Round 1's row said D9 gives those
commands "a doctrine footing". That was wrong, and the correction is:

- the commands that sentence describes are typed by hand or are Syzygy's
  own capture tool, and neither is an attended agent session;
- under arm A, a hand-typed command is outside SEC-3's execution rule
  (packet Q1), and the capture tool stays forbidden, as above;
- under arm W, both are SEC-3 violations [Inferred].

**Which instructions does arm A govern?** Arm A's text now defines the
term in place: "every instruction a Syzygy feature gives an agent (a brief,
prompt, skill or work item)".

- **Shipped skills and prompt kits.** A skill Syzygy ships, such as the
  `/polaris-dossier` skill named in PR #353's design, and the prompt kit
  under `docs/polaris-generation/`, are instructions a Syzygy feature gives
  an agent, whether or not Syzygy's software emits them at run time. Arm A
  governs them: one that tells an agent to run observed code is lawful only
  as the permitted case [Inferred].
- **`AGENTS.md`.** It tells agent sessions in this repository how to run
  Butlers' tests ("Butlers' pytest needs its own `.venv/bin/python`"). It is
  the owner's procedure for their own development sessions on Syzygy, not
  an instruction a Syzygy feature gives, so arm A does not govern it
  [Inferred]. Under arm W, condition 1 reads "Syzygy never instructs …",
  which leaves the same question open. A reviewer who reads the file as a
  feature's instruction should report it to the owner.
- **A typed CI adapter.** RFC5-24 lists CI among the external authorities
  whose adapters Syzygy may hold. If Syzygy triggers a CI run of the
  observed project through such an adapter, that run is a process Syzygy
  schedules, or follows an instruction Syzygy gives, and arm A forbids it
  outside a profile. It is not the permitted case, because CI is not the
  owner's attended session [Inferred]. Reading the project's own CI
  artifacts stays observation under RFC5-19. No such adapter exists today.
  Routed (§5).

**Other lanes, which are not authority.** A hit here can go stale but
cannot change meaning:

- `contracts/candidates/public-repo-admission/`: the template and the
  `redis` and `requests` observation-consent instances exclude "executing any
  code in the repository, including build, install and test scripts
  (SEC-3)". They scope *Syzygy's* observation consent and still hold
  [Inferred], but a reader may take them to forbid the permitted case.
  Routed (§5).
- Measured fixtures `context-selection-2`, `-4`, `-6` and `-9`: their
  anchors move (§4).
- The D7 and D8 packets, the readability-restyle patches and the candidate
  RFC mirror cite SEC-3 and are unaffected.
- `SECURITY.md`, `README.md`, `.syzygy/intent/OVERVIEW.md` and the topology
  candidates are summaries saying observed code runs only in profiles.
  OVERVIEW is act 4's unperformed argument and is not edited here.

## 4. Derived artifacts: application probe

**Method.** Two scratch clones were checked out at `5863d470`. Arm A,
clauses (a) and (b), was applied to one exactly as the round-2 repair's
fenced blocks give them, with the credential lines kept, and committed. The
applied block hashes to arm A's stated sha256. The other clone was left
unapplied. The canonical battery (`PROJECT-STATUS.md` "How to verify this
page", 78 commands, unchanged since `eacb85d1`) ran in each [Observed, this
session]. The result speaks for `5863d470` only (rule 7). The round-1 repair
was probed the same way at `eb7be564`, with the same four failures.

- unapplied: **78 commands, 0 nonzero**; `check_governance.py` "32 OK, 21
  WARN, 0 FAIL";
- applied (arm A): **78 commands, 4 nonzero**, each one a regeneration:

| Command | Failure on application | What application must do |
|---|---|---|
| `scripts/check_governance.py` | "31 OK, 21 WARN, 1 FAIL": CG-18, 8 findings (fixtures 2, 4, 6 and 9 each lose their packet digest and word count) | re-anchor the four fixtures |
| `$CS/build_budget_report.py --check` | DRIFT in the same four fixtures and in `CONTEXT-BUDGET-REPORT.md` | regenerate |
| `$CS/build_contract_index.py --check` | `05-CONTRACT-INDEX.yaml` differs from regeneration | regenerate |
| `scripts/build_directive_register.py --check` | stale: on regeneration, SEC-4 72 → 112, SEC-5 85 → 125; SEC-3 stays at 61 | regenerate |

Two results matter:

- `record_polaris_understanding_adoption.py --check` and `--selftest` stay
  green, because D9 does not touch `vision.md`, which that recorder binds.
- Neither `security.md`'s digest nor `v1.md`'s occurs in any tracked file
  outside this package (`git grep -F` at `eb7be564`: 0 files each)
  [Observed]. No act manifest binds either file. The doctrine tree is
  identical at `eb7be564` and `5863d470`.

Arm W was probed at round 1 (`eacb85d1`, the round-1 bytes) with the same
four failures. Its repaired bytes differ only inside SEC-3's block, so the
same four commands are expected to fail [Inferred, not re-run]. The
no-credential variants were not probed; they move SEC-4 and SEC-5 by three
lines fewer, which changes the same four outputs.

## 5. Observations routed, not repaired

1. **Dispatched workers.** Under arm A, a work item Syzygy dispatches that
   tells a worker to run tests is "an instruction a Syzygy feature gives an
   agent". It is lawful only as the permitted case: an attended session the
   owner started, on a choice recorded for that run naming what it covers.
   By the owner's 2026-10-06 choice this needs no new doctrine act; it needs
   a per-run choice. Dispatch is deferred today. RFC5-19 treats a worker's
   retained gate artifact as produced "outside Syzygy". Whatever act opens
   dispatch must square the two. A typed CI adapter (§3.6) raises the same
   question for CI runs Syzygy triggers.
2. **Consent-record wording.** The public-repo admission template and its
   instances (§3.6) name execution as excluded "(SEC-3)". Routed to the
   consent lane.
3. **The session's reach into Syzygy.** Code the session runs can reach a
   running daemon's loopback endpoints and its machine-client credential
   file. SEC-1 still requires authentication, but a readable credential
   defeats that. Q3(b) covers only RFC5-24's adapter population. The
   machine-client credential is disclosed as a cost and is not conditioned.
   Routed to the specification lane, as an operating step if wanted.
6. **Who records the owner's choice.** Neither arm says how the record shows
   that the choice is the owner's. In PR #353's design the agent records it,
   in a state directory that the owner's records ruling treats as
   agent-editable. Routed to the dossier specification.
7. **Attendance is not observable.** Syzygy cannot see whether the owner is
   present. The limit binds Syzygy's instruction, not the session (packet
   §2). A session in an auto-approve mode with the owner away is not
   attended; in PR #353 only the interactive authoring session receives the
   execution rule.
4. **Clone integrity.** Code the session runs can rewrite the clone's object
   store (dossier review 1, finding 1). The owner's records ruling handles
   Syzygy's own records by re-deriving them.
5. **Hosts.** "The owner's own host" excludes a cloud-hosted agent session
   [Inferred]. Whether it includes a remote VM the owner rents is not settled
   (packet Q5).
