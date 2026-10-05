# Impact ledger — D9, SEC-3 and the owner's attended agent session

> **Candidate — binds nothing.** The blast radius of the amendment drafted
> in `SEMANTIC-DELTA.md` (this directory), measured 2026-10-05 at
> `origin/main` commit `b60e6cd2683f78fb0574d24f1e4146d3e6f8e58d` unless a
> row says otherwise. Every figure below was produced by the method stated
> beside it in this session. Re-run it at the reviewed commit; never copy
> it.

## 1. The identifier sweep

**Population:** every path `git ls-files -z` lists: **2,346** paths. Of
those, 4 do not decode as UTF-8 and were skipped, so **2,342** were
searched.

**Predicates** (Python `re`, case-sensitive, over whole file text):

| Name | Regex | What it catches |
|---|---|---|
| exact | `(?<![A-Za-z0-9-])SEC-3(?![0-9])` | `SEC-3`, but not `CC-SEC-3` or `SEC-30` |
| ccsec | `CC-SEC-3(?![0-9])` | the craft clause that restates SEC-3 |
| range | `(?<![A-Za-z0-9-])SEC-[12]\s*(?:\.\.\.?\|…\|–\|—\|-\|through\|to)\s*(?:SEC-)?[345](?![0-9])` | continuation forms: `SEC-1…SEC-5`, `SEC-1…5`, `SEC-1–SEC-5`, `SEC-1 through SEC-5` |
| slash | `(?<![A-Za-z0-9-])SEC-(?:\d[/,] ?)+\d`, kept only when the match contains `3` | `SEC-2/3`-style runs |

(The `\|` above is table escaping; the regex alternation is a bare `|`.)

**Result:** **240** files match at least one predicate: exact 201, ccsec
4, range 58, slash 5 (a file may match several). By authority lane:

| Lane | Files | Disposition |
|---|---|---|
| Doctrine (`.syzygy/governance/doctrine/`) | 3 | §3.1 |
| Accepted contracts (`contracts/rfcs/`) | 21 | §3.2 |
| Craft-and-care (`policies/craft-and-care/`) | 4 | §3.3 |
| Decisions (`decisions/`, excluding `-RAW.md`) | 4 | §3.5 |
| Adopted or signed specifications (`openspec/`) | 9 | §3.4 |
| Candidates (`contracts/candidates/`, excluding `round-*`, `history/` and `reviews/`) | 86 | §3.6 |
| Topology and intent (`.syzygy/map/`, `.syzygy/intent/`) | 5 | §3.6 |
| Root pages and skills (`AGENTS.md`, `README.md`, `SECURITY.md`, `DIRECTIVE-REGISTER.md`, two `heart-and-soul/SKILL.md`) | 6 | §3.6 |
| Code and generators | 5 | §3.6 |
| Design notes (`docs/design/`) | 8 | §3.6 |
| Evidence and pursuit records (`docs/evidence/`, `docs/pursuits/`) | 20 | records of past bytes; never edited |
| Retained reviews (`-RAW.md` and `reviews/` directories) | 27 | raw output, stored unchanged (CC-REV-6) |
| Historical (`round-*`, `contracts/candidates/history/`, `_bootstrap/`) | 42 | never authority |

The lanes sum to 240. The four decisions files are the three that the
2026-10-05 sweep at `eacb85d1` found, plus
`POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`, which landed on
`main` between that sweep and this one. The two sweeps differ by exactly
that file in both directions [Observed].

**Second method (rule 2), a term sweep with no identifier.** The predicate
was `observed[- ](?:project[- ])?code|execution[- ]profiles?|execut\w* (?:the )?observed|run(?:s|ning)? observed`
(case-insensitive) over the same population. It matched 248 files at
`eacb85d1`. Lines in the doctrine, decisions, `openspec/`, craft-and-care,
topology and root lanes, in files the identifier sweep did *not* match,
were read one by one. Each is a grant list ("grants no … observed-code
execution"), a Syzygy-pipeline statement, or a profile-contract row. None
reaches the attended session. The ones that bear on this amendment are in
§3 (`AGENTS.md`, `APPLICABILITY-DECISIONS.md`, `SOURCE-POLICY.md`, the
coverage matrices).

## 2. Line-number citations of `security.md`

The amendment adds 27 lines to `security.md`, so SEC-4 moves from line 72
to 99 and SEC-5 from 85 to 112 [Observed: the application probe's
regenerated register, §4]. The predicate
`` security\.md`?(?::\s*|\s+lines?\s+|\s*L)\d+|security\.md#L\d+ `` over the
§1 population finds 57 line-cited references. All except the five
`DIRECTIVE-REGISTER.md` rows (regenerated) cite lines 10–61. None cites a
line after 61 [Observed]. Most of these citations already predate D5/D6
numbering, and this amendment moves none of them.

## 3. Authority-lane hits, and whether D9 changes their meaning

"Unchanged" means the cited text reads the same after D9 as before.
"Unchanged [Inferred]" means the drafter judges so and a reviewer should
test it.

### 3.1 Doctrine

| Site | What it says | After D9 |
|---|---|---|
| `security.md` 61 | SEC-3 | the subject |
| `security.md` 3–4, 7–8 | "treats observed code as untrusted everywhere"; Syzygy "may execute observed-project code" | unchanged: the code stays untrusted, and Syzygy's own execution stays profiled |
| `v1.md` 119–120 | "executing it is opt-in, profiled, and blocked until the execution-profile RFC is accepted (SEC-3)" | **clause (b)**. It sits under "Platform and audience" and describes Syzygy's own platform, so it stays true of Syzygy [Inferred]. Read alone, though, it reads as "every execution is profiled". Clause (b) appends one sentence naming the exception and changes none of its bytes |
| `README.md` 74–75 | rules SEC-1–SEC-5 on "executing observed code" | unchanged |

### 3.2 Accepted contracts

Each file under `contracts/rfcs/` has a byte-identical copy under
`contracts/candidates/rfcs/`. At this commit, `diff -rq` reports only
`RFC-0010` and `RFC-0011`, which exist in the candidate tree alone, and no
file that differs [Observed]. Each row therefore covers both copies.

| Site | What it says | After D9 |
|---|---|---|
| RFC5-18 (`RFC-0005/execution-profiles.md`) | "Observed-project code executes only when all of" (a)–(e) | **Unchanged [Inferred], and the question a reviewer should press.** RFC5-19's last bullet scopes the gate: "profiles govern only code Syzygy itself launches". The attended session is started by the owner, not launched by Syzygy, so RFC5-18 does not reach it. Read without RFC5-19, RFC5-18's sentence names no actor, as SEC-3's did. Packet Q3 |
| RFC5-19 | "untrusted everywhere, regardless of who owns the project"; reading outside evidence "is observation, not execution" | unchanged. D9 keeps the first sentence's doctrine source verbatim. The second already treats a worker's retained gate artifact as produced "outside Syzygy" |
| RFC5-20, §4 violation cases | "no ambient credential is ever inherited (SEC-3's named violation)" | unchanged: the named violation keeps every byte and still governs every profile |
| RFC5-21, RFC5-22, RFC5-23 | isolation floor, destructive-operation gates, lifecycle | unchanged; they bind profiles. The attended session has none of their guarantees, and D9's cost bullet says so |
| RFC5-24 (`admission-and-boundary.md`) | no credential that authenticates to Syzygy may be injected into observed code | unchanged for profiles. Its premise, "no credential to Syzygy, and no route to Syzygy", is exactly what the attended session lacks. D9's cost bullet names "any Syzygy credential or endpoint on that host". §5 item 3 |
| RFC5-12 / RFC3 `manifests-and-namespace.md` 258–264 | execution consent is per project, for a profile version | unchanged. The owner's recorded choice is not an execution consent and approves no profile (delta, "What explicitly does NOT change") |
| RFC-0005 `README.md` 105–107; `execution-profiles.md` 30–31 | "no observed-project code executes until this RFC is accepted and a per-project profile exists (SEC-3)" | **Literal tension [Inferred].** Both are reader-map or preamble prose, not clauses. The map says "If this map and a clause disagree, the clause wins", and the clause (RFC5-19) is scoped to Syzygy. Packet Q3 |
| RFC3-16(a) and its users: RFC2 `challenge-lifecycle.md` 162, RFC3 `governance-homes-and-owner-acts.md` 233, 478, RFC5 `consent-egress-secrets.md` 68, 200, RFC5-25, RFC7 `narrative-contract.md` 448, 531, RFC7 `rendering-and-surface.md` 361, RFC8 `accounting-reconciliation-and-release.md` 457, `state-vocabulary-and-cost.md` 205, RFC9 `interaction-parity-and-release.md` 391, RFC4 `named-adapters.md` 229 | "SEC-3's untrusted actor class", extended to what fleet workers commit | unchanged. The attended session is in that class too, and nothing it writes is trusted |
| RFC4-12, RFC4-13 (`named-adapters.md` 150–162, 363, 501); RFC-0004 `README.md` 232, 263 | Syzygy's observers parse statically and never execute | unchanged: they are Syzygy's observers. RFC4-13's cap ("unverifiable origin caps at `report-fact`") agrees with D9's "never Observed" |
| RFC9-33 (`visual-grammar-and-lenses.md` 306–309, 702, 735) | the Runtime lens "is hard-gated by SEC-3 through RFC 0005's execution profiles" | unchanged. D9's claims are Inferred and open no captured-trace evidence class, so the Runtime lens stays gated |
| `Serves:` and routing lines (RFC-0001 953; RFC-0002 `README.md` 33, 214, `challenge-lifecycle.md` 26; RFC-0003 27; RFC-0004 `README.md` 31, `named-adapters.md` 25; RFC-0005 `README.md` 30, 175, 196–208, `execution-profiles.md` 3, 25, 89, 103, 135, 172, 267; RFC-0007 `README.md` 30, `narrative-contract.md` 27, `rendering-and-surface.md` 25; RFC-0008 `README.md` 32, `state-vocabulary-and-cost.md` 27; RFC-0009 `README.md` 33, `semantic-geography.md` 26, 838, `visual-grammar-and-lenses.md` 27) | citations | unchanged (rule 5: a citation is not a reliance) |

### 3.3 Craft-and-care

| Site | What it says | After D9 |
|---|---|---|
| `security-and-secrets.md` CC-SEC-3 (63–82) and its preamble (5–8) | "Observed code never executes outside an accepted profile"; "'Run the project's own test command to get better evidence' is exactly the tempting violation" | **Narrower than amended doctrine.** The file's own rule is "Doctrine's text prevails over any paraphrase here" (line 21), so D9 prevails where they differ. But the clause would stand as a false restatement, and its digest is recorded in `policies/craft-and-care/INSTALL-RECORD.md`, so it changes only by a policy amendment. Packet Q2 |
| `README.md` 24, 60, 119; `engineering-bar.md` 148–149; `review-and-documentation.md` 37 | range citations; "untrusted observed code" | unchanged |

### 3.4 Specifications

| Site | After D9 |
|---|---|
| PWB-REQ-001, PWB-REQ-006 (`primary: SEC-3`), PWB-REQ-014 (`polaris-project-wide-butlers-model`) | unchanged: they constrain Syzygy's own reads and renders |
| POC-REQ-002, POC-REQ-021 (`primary: SEC-3`) | unchanged |
| Polaris generation: "Versioned interchange and reference integrity", "Protected audit and prospective revocation", "Provenance-bound source policy" (base); "Versioned interchange and reference integrity", "Accounted unfamiliar-project discovery" (overlay); `SOURCE-POLICY.md` 13–17; `APPLICABILITY-DECISIONS.md` 44–47 | unchanged: Syzygy's generator "never executes observed-project code". The local-agent mode does not change that |
| The four `GOVERNING-DEPENDENCIES.md` unions; Capability 1 `design.md` 15 | generated or range citations; unchanged |
| **Candidate** `openspec/changes/polaris-dossier-local-agent-mode/` (PR #353, not on `main`) | **the one dependent.** Its brief's execution rule, `executions` list and `basis: execution` labelling are drafted to these three conditions. Under the review-1 rulings item 1, it may not be signed until D9 is adopted, and until then its brief may not tell an agent to run observed code outside a profile. Whatever D9's adopted text says, that spec must match it |

### 3.5 Decisions

| Site | After D9 |
|---|---|
| `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md` 33, 61 | unchanged. Line 61, "Syzygy itself still never executes observed project code (SEC-3)", stays true |
| `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md` | the direction D9 answers |
| `POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md` 216–217, 483 | unchanged (PWB-REQ-006's warrant) |
| `README.md` 84 | range citation; unchanged |
| Term-sweep hits: the act records that grant "no … observed-code execution"; `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-DIRECTION.md` 25; `BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` 48; `SURFACE-DECISION-RECORD.md` 244–245 | unchanged. Each limits what an act grants Syzygy, and D9 grants Syzygy nothing |

### 3.6 Non-authoritative lanes

These lanes are not authority. A hit there can go stale but cannot change
meaning. The ones a reader is likely to trip on:

- `AGENTS.md` 89: "The daemon never executes observed project code or test
  suites; separate operator commands do." It stays true, and D9 now gives
  "separate operator commands" a doctrine footing for the attended case.
- `contracts/candidates/public-repo-admission/`: the template and the
  `redis` and `requests` observation-consent instances exclude "executing
  any code in the repository, including build, install and test scripts
  (SEC-3)". They are unperformed candidates, and they scope *Syzygy's*
  observation consent. Read as written, they still hold after D9 [Inferred],
  but a reader may take them to forbid the attended session. §5 item 2.
- `fixtures/context-selection-4-execution-profile.md` and fixtures 2, 6 and
  9: measured fixtures whose anchors move (§4).
- The D7 and D8 packets, the readability-restyle patches and the candidate
  RFC mirror: they cite SEC-3 and are unaffected.
- `SECURITY.md`, `README.md`, `.syzygy/intent/OVERVIEW.md` and the topology
  candidates: summaries that say observed code runs only in profiles.
  OVERVIEW is act 4's unperformed argument and is not edited here.

## 4. Derived artifacts — application probe

**Method.** Two scratch clones were made at `eacb85d10ed7eba1d1af6d286d5a0ccd626c641a`.
Clauses (a) and (b) were applied to one exactly as the delta's fenced
blocks give them; the other was left unapplied. The canonical battery
(`PROJECT-STATUS.md` "How to verify this page", 78 commands) ran in each
[Observed, this session]. Between that commit and `b60e6cd2` the doctrine,
`contracts/rfcs/` and `policies/` trees are identical (`git diff --quiet`)
[Observed]. The probe still speaks only for `eacb85d1` (rule 7). Re-run it
at the reviewed commit.

- unapplied: **78 commands, 0 nonzero**; `check_governance.py` 32 OK, 21
  WARN, 0 FAIL;
- applied: **78 commands, 4 nonzero**, each one a regeneration:

| Command | Failure on application | What application must do |
|---|---|---|
| `scripts/check_governance.py` | CG-18 FAIL, 8 findings: fixtures 2, 4, 6 and 9 each lose their packet digest and word count | re-anchor the four fixtures |
| `$CS/build_budget_report.py --check` | DRIFT in the same four fixtures and in `CONTEXT-BUDGET-REPORT.md` | regenerate |
| `$CS/build_contract_index.py --check` | `05-CONTRACT-INDEX.yaml` differs from regeneration | regenerate |
| `scripts/build_directive_register.py --check` | stale: SEC-4 moves 72 → 99, SEC-5 85 → 112 (SEC-3 stays at 61) | regenerate |

Two results matter here:

- `record_polaris_understanding_adoption.py --check` and `--selftest`
  stayed green. Its frozen set binds `vision.md`, which D9 does not touch.
- Neither `security.md`'s nor `v1.md`'s digest occurs in any tracked file
  (`git grep -F` of each sha256 at `eacb85d1`: 0 files each) [Observed], so
  no act manifest binds either file.

## 5. Observations routed, not repaired

1. **Dispatched workers.** D9's "any process Syzygy launches or schedules"
   does not say whether a fleet worker that Syzygy *dispatches* (deferred
   today) is Syzygy's automation. RFC5-19 treats a worker's retained gate
   artifact as evidence produced "outside Syzygy". D9 neither widens nor
   narrows that. It is left for whatever act opens dispatch.
2. **Consent-record wording.** The public-repo admission template and
   instances (§3.6) name execution as excluded "(SEC-3)". Routed to the
   consent lane: if the local-agent mode is to run on those repositories,
   the record should say that the exclusion scopes Syzygy's consent, not
   the owner's attended session.
3. **The session's reach into Syzygy.** On the owner's host, observed code
   run by the session can reach whatever the owner's user can reach,
   including a running Syzygy daemon's loopback endpoints and any
   machine-client credential file. SEC-1 still requires those clients to
   authenticate, but a readable credential defeats that. D9 states the cost
   and adds no condition. The dossier specification may want an operating
   step, such as running with no Syzygy credential readable. Routed to the
   specification lane.
4. **Clone integrity.** Review 1 of the dossier amendment (finding 1) showed
   that code the session runs can rewrite the clone's object store. D9's
   cost bullet names this. Fixing it belongs to the specification.
5. **Hand-run code outside any Syzygy mode.** D9's exception is general: it
   names no feature, and its conditions bind only what Syzygy instructs and
   renders. So an owner's ordinary development session that runs tests,
   with no Syzygy involvement, is also lawful under it [Inferred]. Under the
   current text that session is arguably forbidden. The packet discloses
   this (§2) rather than drafting around it.
