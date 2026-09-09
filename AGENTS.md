# Agent Instructions — Syzygy

Repository operating procedure for any agent session, in any harness. It is
**never citable as authority** and restates no digest, verdict, or act
history. What the project *is*: `README.md` and `.syzygy/intent/OVERVIEW.md`.
What state it is in: `PROJECT-STATUS.md`. Where they and this file disagree,
they win.

## Orientation

Syzygy is a specification-driven control plane: humans define what should be
true, evidence shows what is true, agents do bounded work to close the gap,
and the gap is always rendered honestly. Two planes:

- **Governed** — `.syzygy/**` (doctrine, decisions, policies, contracts) and
  `openspec/**` (specifications). Changes travel as reviewed semantic deltas
  and bind only by owner act.
- **Implementation** — `apps/**`, `packages/**`, `scripts/`, root manifests.
  Code goes here and only here.

Everything is stage-gated. Each authorization is a dated owner act or
direction under `.syzygy/governance/decisions/` (`ACCEPTANCE-ACT-RECORD.md`
owns acceptance and amendment transactions). `PROJECT-STATUS.md` says which
are in force. As of 2026-09-05: Capability 1 is implemented; a bounded,
non-release Three-Surface POC (Polaris, Trajectory, Orrery) runs against one
Butlers repository, whose PWB project-shape slice may read one consented
content class behind the P1 authority gate. Anything no act covers is
forbidden — before implementing, find the act.

## Where authority lives

| Question | Authority | Path | Status |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | Adopted, in force |
| Prior owner rulings | Decisions (SDR-1…37, acts, pending queue) | `.syzygy/governance/decisions/` | In force |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | Owner-approved |
| The specification bar (CC-SPEC-1…11, CC-IMPACT-1…7) | Craft acts 6 and 7; CC-SPEC amended 2026-09-01 | `contracts/candidates/policy-candidates/` — **not** the craft-and-care directory | **In force.** Path, filenames and head banners all still say candidate; the acts bound those bytes and none may be corrected |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/` | 0001–0009 accepted; 0010–0011 candidate in `contracts/candidates/` |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | Candidate |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Presentation, never authority |

`GOVERNANCE-SUBSTRATE-LOCK.yaml` is a record, never authority. **Cite by
identifier** (`VIS-2`, `SDR-9`, `RFC10-9`); identifiers are amended in place
or retired, never renumbered. `DIRECTIVE-REGISTER.md` (generated) says where
every identifier is defined, file and line, across all of these trees — use it
to find a clause, never to learn what one says. Candidate clauses, drafts, indexes, summaries,
and generated views are never authority.

## Task routing — context is compiled, never accumulated

Load the minimum for one correct decision; never "read everything."

| Your task | Start here |
|---|---|
| Current state, gates, next lawful step | `PROJECT-STATUS.md` |
| A doctrine question | the one doctrine file, via the `heart-and-soul` skill |
| An engineering-bar question | the one craft policy that owns it |
| A contract question | `contracts/candidates/TASK-ROUTER.md` (generated) |
| "May I implement X?" | the authorizing act in `decisions/`; plans: `docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md`, `docs/PWB-IMPLEMENTATION-PLAN.md` |
| The Capability 1 specification | `openspec/changes/project-registration-and-honest-shape-visibility/` — adopted; amend only via CC-REV-2 |
| The Three-Surface POC specification | `openspec/changes/three-surface-poc-experience/` — signed off; its `proposal.md` banner still says candidate and is bound, so cannot be corrected |
| Authoring a new spec | `contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`; only owner sign-off binds it (VIS-4) |
| Which acts exist, their phrases and ceremony | `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`; packets per `decisions/README.md` |
| Open owner questions | `decisions/PENDING-OWNER-DECISIONS.md` |
| A launch-gate administration | structured JSON (`launch-gate-administration.schema.json`); the Markdown report is generated, never parsed |
| Mission or Context-selection work | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` first |
| What a term means | `governance/doctrine/README.md` glossary, then `PROCESS-GLOSSARY.md` |
| Where a clause with a known identifier lives | `DIRECTIVE-REGISTER.md` (generated) |
| Avoiding a repeat mistake | `decisions/PROCESS-LESSONS.md` — not default context |

Historical material (`_bootstrap/`, `contracts/candidates/history/`,
`round-*`) is never on a default path and never authority. Superseded
offerings are banner-marked; retired phrases satisfy nothing — never route
an owner to a stale offering. For the eleven `round-*` directories, read
`contracts/candidates/ROUND-ESTATE.md` before opening any of them: it says
what each round settled and where that settlement lives now, and it names
the round files that running software still reads.

## Hard prohibitions

- No implementation code inside `openspec/**` or `.syzygy/**`.
- Nothing beyond the acts in force: no deferred waves (C1/C2/D1/D2), Mission
  Control, production deployment, release, broad remote access, multi-user
  support.
- Never read a repository body without per-repository consent and the
  applicable registry and policy acts (Butlers: the consented content class
  only, after the implementation's PWB-REQ-005 evaluation).
- The daemon never executes observed project code or test suites; separate
  operator commands do.
- Syzygy never writes implementation code or adopts intent autonomously.
- Never adopt doctrine, accept contracts, approve policy, or label anything
  accepted on the owner's behalf (VIS-4); never install candidate material
  into an accepted home.
- Never edit an artifact after an act has bound its digest.
- An OpenSpec change is one coherent category overlapping no other change,
  binding nothing until owner sign-off.
- An act's escalation triggers (doctrine or contract change, spec amendment,
  security/privacy/retention posture, scope) need a new owner act.
- No unattended agent coordination.

## Epistemic and change discipline

Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. No
evidence yields Unknown — never green, never zero (VIS-2). An LLM assertion
is Inferred. Preserve the owner's trade-offs; never smooth them into
consensus language. Normative edits travel as semantic deltas
(`policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`); "editorial" is a
reviewable claim. Reviews run in fresh context with only the artifact, its
governing references, and the acceptance criteria; raw output is stored
verbatim and verdict words are copied exactly.

## Verification rules

Each paid for by an incident in `decisions/PROCESS-LESSONS.md`. Numbering
is stable; reviews cite rules by number.

1. `grep` here is ugrep; `[^]]`-style classes silently match nothing. Use
   `grep -F` or Python `re` for anything load-bearing.
2. No "zero / all / 100%" claim without running that exact sweep this
   session, confirmed by a second method. Enumerate remainders.
3. Digests are scripted, never transcribed; totals are computed.
4. Read a check's output, not its exit code, and check its denominator
   against the whole population.
5. A citation is not a reliance; a status banner is not a dependency edge.
6. Mutate the input and confirm the check fails, per predicate, before
   trusting it (`--selftest` holds the fixtures).
7. Run the battery in a clone before calling it green; the report is valid
   only for that commit.
8. Anchor a contract claim to a defined clause and quote it; nearby prose is
   not the clause.
9. A claim of absence needs a sweep with a denominator.
10. Freeze the bytes a review is bound to; any later edit retires the review.

A generator that quotes prose has re-opened the door it closed.

## Validation

`PROJECT-STATUS.md` §"How to verify this page" owns the canonical battery;
run that block, never a copy. Everyday: `python3 scripts/check_governance.py`
(`--selftest` runs the fixtures). All read-only; run before claiming clean.

## Beads scope

`bd` tracks housekeeping, the Capability 1 backlog, and POC improvement
cycles (review → repair beads from recorded findings → confirmation, reported
to the owner before the next cycle). POC shared-model changes have WIP one.
Commits land at stable gates; never commit a normative artifact while its
adoption gate is unresolved.

## Notes to self

Durable lessons only; status and narrative belong in git log, `bd`, or
`PROJECT-STATUS.md`. Capability 1 status, the FROZEN-files rule, and the
tailscale `--set-path` finding live in `bd memories` — do not re-add them.
Last compacted 2026-09-05; C5 seams, recorder notes and the docs-estate
lessons added the same day; the second through fifth docs-pass lessons
added 2026-09-06; the ceiling, locator, extractor and regex lessons
added 2026-09-07.

### Architecture

- `packages/cap1-core/`: pure domain modules; one conformance file per
  CAP1-REQ in `packages/cap1-conformance/`. One `FactModel` feeds both
  channels; an independent oracle compares their outputs.
- Three-Surface POC: `packages/three-surface-poc-core/` (one shared
  `PocModel`) and `apps/three-surface-poc/` read the same instance — never
  split surface truth stores. `build:poc` keeps `tsc -b --force`: ignored
  incremental outputs are executable inputs.
- PWB pipeline (pure, injectable, in order): `body-read-authority` gates
  every Butlers read → observation → `git-object-reader` → classification
  (excluded content yields hash-not-body records) → extraction (literal
  grammar) → coverage (precedence only via a Butlers-declared
  `PrecedenceRule`, never "newest wins") → `PocModel.projectShape`.
  Since the 2026-09-05 amendment the precedence input is the root index's
  own seven-row `Precedence Order When Layers Disagree` table, admitted
  only when every row matches the registry literal grammar; a row decides
  a disagreement only when exactly one declaration lies under its home.
- Two render-time seams sit beside the shape, both pure and injectable:
  `walkthrough-readiness.ts` (core; PWB-REQ-021 nine answer identities,
  ten arms, never a verdict or score, never touches the PWB-REQ-022
  evaluator) and `verbatim-route.ts` (app; PWB-REQ-011 exact-requirement
  route, derived per render from the model, caches nothing). Phase B
  classifies baseline specs path-only, so the route runs the unchanged
  secret detectors and active-content scan on the transient body itself.

### Guardrails (keep even when old)

- Contract amendment tooling reads both installed `contracts/rfcs/` and mirrored `contracts/candidates/rfcs/` bytes. Probe both locations in isolation: current indexes and budget fixtures derive from the candidate copies, while performed manifests remain immutable. Regenerating the active manifest does not establish successor authority.

- Polaris reading selections are metadata-only offsets bound to the exact
  extracted declaration digest and an independent fidelity review. Source
  drift must render the full declaration; keyword-based omission can drop
  qualifications. Scope sticky styling to `.site-nav`, never all `nav` tags.
- Phase-A pillar indexes follow roots declared by the screened root index,
  not directory basenames. Reuse the screened root derivation in the
  manifest; repeating it is another registry-budgeted parse pass.
- Manifest tree rules supply only blobs. When a named source yields to a
  tree rule, keep missing/non-blob targets counted, and update literal
  mutation targets whenever the guarded source fragment changes.
- Fresh `git worktree`: run `npm ci` inside it first, or `NodeNext` silently
  resolves `@syzygy/*` to the main checkout's `node_modules`.
- `git ls-tree` needs `-z`, or quoted paths break the parser.
- `npm run poc:pwb-*-mutation-*` rewrites sources in place (~35 min): never
  edit or commit while it runs.
- CDP headless: enable `Emulation.setFocusEmulationEnabled` or focus never
  moves; re-navigate before Tab/Enter when the fragment already matches the
  hash; `<summary>` needs its own `:focus-visible` rule.
- Never put a fragment target (an `id` some `href="#…"` names) inside a
  `<details>`: after navigating to it Chrome restarts Tab at the details'
  first focusable, stranding keyboard readers. Collapse populations, route
  the targets.
- A Python block matcher written `(?:- .*\n)+` under `re.S` swallows every
  following block (`.` eats the newline); use `[^\n]*` and no DOTALL, and
  assert the match ends where the next heading begins.
- The Write tool has emitted mixed NFC/NFD bytes; use Unicode escapes in
  fixtures when exact matching matters.
- A mutation that throws at describe time reports zero tests and scores as
  survived — build fixtures in `beforeAll`.
- A rule-6 evidence record must store each mutant's `old`/`new` fragment and
  the commit it ran at; ids and outcomes alone are not re-runnable, and a
  rebase-merge leaves the recorded commit reachable from no ref.
- A retained raw review's filename must end in `-RAW.md`: `check_governance`
  exempts only that suffix from CG-1b and CG-15, so a raw named
  `…-RAW-ADDENDUM.md` fails on the Butlers paths and truncated digests it
  quotes verbatim. A re-issued raw is a second `-RAW.md` file, never an
  overwrite of the digest-cited first.
- Fail-closed polarity: withdrawal defeats grant; future-dated evidence is
  stale; no evidence → Unknown.
- Conformance expected values are hard-coded literals, never imported from
  the module under test.
- Root Vitest `test.projects` must alias both `@syzygy/cap1-core` and
  `@syzygy/cap1-daemon` to source; verify with every `dist/` absent.
- Butlers' pytest needs its own `.venv/bin/python`.
- Never wire `WORKER_CHANGE_SEAM` test-artifact evidence into the unrelated
  identity-resolution entities in `model.ts` — false "Verified" (reverted
  once already).
- Never quote a performed act's argument or a truncated signed digest in a
  new artifact unless it is in `ACT_DIGEST_COPY_FILES` (CG-7e/CG-15); cite
  the record by path. Never backtick a Butlers path in a packet (CG-1b).
- `authorizeWrite` uses raw `startsWith` for containment; callers must
  normalize paths first (tracked, unfixed).
- App typecheck (`tsc --noEmit -p apps/three-surface-poc`) resolves core
  through `dist` declarations: run `tsc -b packages/three-surface-poc-core`
  first after a core type change, or the app reports phantom errors.
- Ledger semantics: a refused read is not a counted pass; phase-B breaches
  are typed findings and do not set the degradation state; catalog
  extraction keys off the basename `v1.md`. The tailnet mount is detected
  by `Host`, never by path.
- Copy-oracle tests match by substring: a very short label (`None`) is
  "reached" by coincidence and proves nothing — give every label a
  distinctive string or drop it.
- A counterexample isolates a *scoping* change only if the same signal is
  genuinely elsewhere on the page: the preflight fixture (`TEXTS` in
  `walkthrough-preflight.test.ts`) already renders craft-and-care as
  `index-unavailable` with its route, so a page-wide substring check
  survives any case using a different reason (the phrase check catches
  it first). Give the mutated pillar the reason already on the page.
- PWB-REQ-020 parity is per tuple, never per id: a claim may render more
  than once (the current-authority citation repeats the baseline-spec
  item's tuple), so `tuples === distinct ids` is a false invariant; check
  every rendered tuple against its machine claim by id and both id sets.
- `poc:fresh-checkout-demo` names its evidence file by `--date` and
  overwrites silently: pass a suffixed `--date` (`2026-09-06-gen2`) when a
  same-day file exists. Rebase-merge re-hashes the recorded head; the
  surface version (sha256 over both `src` trees) is the stable anchor.
- **A response-ceiling breach serves nothing and logs nothing.** `routes.ts`'s
  `boundedResponse` answers HTTP 503 with a JSON body (`served: 'nothing'`,
  readiness false); no ledger, stderr line or status record sees it — the 503
  body of the breaching request is the only trace. The resource ledger is
  the input-side reader budget and never sees a response ceiling. Two
  governance records said "degrades honestly" / "the ledger reports the
  breach" for a day; both marked 2026-09-07. `/polaris` sat 44 KB under
  the 2 MB ceiling; the P-63 trim (`syzygy-1z3.27`) cut 434,960 bytes on
  both forms (`docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json`),
  leaving ~479 KB for the P-60/P-61 repairs' 418–443 KB.
- **Measuring `/polaris` needs a committed, clean tree.** The observer
  refuses uncommitted inputs, so commit first, then serve a private daemon
  (`--port 0 --state-dir <scratch>`) from the worktree root and curl the
  page twice: direct, and with `Host: tzeusy.parrot-hen.ts.net` (the mount
  prefix adds 15 bytes per internal link, 5,640 bytes at 376 links). Never
  measure through the loopback daemon on 7478.
- **Where a trimmed byte may not come from.** The parity sweep finds class
  tables by the literal `<tbody>` and the reachability test wants a region
  inner starting with `<table>`; an attribute hoisted onto either tag drops
  the family to a human count of 0 rather than failing loudly. Hoist roles
  onto the `tableRegion` div (its `attrs` parameter). A cite span needs only
  `data-anchor-id`; every other anchor field lives once in the frozen
  narrative JSON, and the source-route `href` is the single carrier of the
  exact-source identity (`sourceRouteIdentities(html)` reads it back).
- The daemon serves only the registered locator (`git-observation.ts`
  refuses any other `--repo`), so a repaired Butlers page cannot be measured
  on a private daemon from a scratch clone: measure per-item marginal cost
  on the retained capture instead, or wait for a real Butlers commit.
- The extractor stops at the first grammar failure, so a finding that names
  "one line" understates: re-run on a scratch copy after each fix until it
  parses (v1.md had five colon forms and four duplicate labels behind "one
  row uses a colon").
- The fresh-checkout demo exits by `fresh-checkout-verdict.ts` over every
  invariant it records (daemon stderr must be empty); the walkthrough
  preflight (`walkthrough-preflight.ts`) is mechanical readiness and
  never an owner verdict — keep readiness, execution record, owner
  judgment and act validity as four states.

### Governance prose and docs

- **A page-level "may be stale" banner discharges CG-27 while a false
  sentence stands.** Three default-path pages carried inverted act claims for
  nineteen days behind such banners. Mark staleness **at the stale sentence**,
  keeping the superseded text quoted and dated; never rely on a page banner to
  cover a specific false claim.
- CG-27's historical exemption is **paragraph-scoped, and a Markdown table is
  one paragraph** — an incidental `superseded`/`historical` token anywhere in
  a table (a filename counts) exempts every current-state claim in it.
  Verified by mutating the block. Tracked as a check-quality bug.
- A page that restates state it does not own goes stale silently. Cite
  `PROJECT-STATUS.md` or the act record instead of repeating the row.
- **"Historical" never means "safe to relocate."** Sweep for citers first:
  `round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json` is a live CI input of
  `.github/workflows/governance-docs.yml`, and rounds `h`–`k` are cited as
  evidence by acts in force.
- `docs/superpowers/**` is **path-pinned**:
  `scripts/build_general_trusted_bootstrap_impact_ledger.py` hard-codes the
  prefix to classify those paths as spent evidence, so moving a file out
  silently re-classifies it on the next regeneration. Do not move or rename.
- A prepared act package may still carry the pre-act "candidate, binds
  nothing" banner it was drafted with. **Read the act record, never the
  package banner.**
- **`bd search` reaches neither bead descriptions nor `close_reason`.**
  `bd search PWB-LIVE` returns "No issues found" while five beads name those
  identifiers in their descriptions, and `RTF-1` appears in exactly one place
  in the tracker — `syzygy-zal.9`'s close reason (1 hit over all 165 beads).
  Sweep the `.beads/issues.jsonl` export instead: one line per bead, every
  field, and its line count is the denominator.
- Identifiers in this corpus are written in **continuation form** — "Repair
  PWB-LIVE-02, 03, 05 and 15", `PWB-LIVE-02/03/05/15`, `PWB-LIVE-01..15`. A
  sweep matching the full identifier misses every continuation and produces a
  false absence (it produced one, on a page written the day before). An
  absence claim's denominator must cover the *forms* an identifier occurs in,
  not only the records searched (rule 9).
- The two in-force craft policies inside `policy-candidates/` are in the
  authority table above; the trap that is not is CC-IMPACT-7, which mandates a
  blind run against `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` by path *and*
  digest — a fixture that fixture 3 superseded on 2026-08-30 because it left
  `topology[]` unexercised. Neither the clause nor fixture 2 may be edited to
  say so.
- A clause is found by identifier, not by directory. `DIRECTIVE-REGISTER.md`
  is generated from all five trees and carries file and line for every one; a
  scan of a directory you *expect* to own a family will miss the two above.
- A round directory's index date is its **first-commit** date and does not
  bound its contents: `round-2026-08g` took two files seventeen days after it
  closed. Many round file heads carry no status word at all — read the
  `round-*` path itself as the banner. Counts for that estate live in one
  place, `contracts/candidates/ROUND-ESTATE.md`, which derives them: four
  different figures for the same directories were in circulation, each right
  about a different population, and one of them was stale on publication
  because the page quoting it had itself become the missing citer.
  **Measuring last is not enough.** That page's own uncited count was exact
  when published and wrong three commits later, falsified by prose in the
  same pass that named two of the files it counted. An absence figure over a
  population the current pass is still editing has to be re-derived, never
  read — and it needs its citer predicate stated, because "cited by no other
  tracked file" and "cited by nothing outside its own round" differ by
  nineteen files over the same 237.
- **A word set published as "X, Y or similar" is not a predicate, and the
  figure resting on it cannot be re-derived.** The round estate's 96
  unbannered heads were published with four status words "or similar"; the
  four alone give 118, and the figure only comes back at 96 when
  *non-authoritative* and *not authority* are added — recovered by search,
  not from the page. Enumerate every literal, the window, and the case
  folding, or the number is a claim no reader can check. Test the denominator
  separately: that same figure is 96 over the round work files, over every
  `.md` under the eleven directories, and over the population as it stood
  before the READMEs landed, so naming one of the three was never load-bearing
  and only went stale.
- Where a file *sits* and whether its work is *finished* are different
  questions. The general trusted-bootstrap impact ledger classifies everything
  under `docs/superpowers/` as spent evidence, but
  `plans/2026-08-24-cap1-runtime-hardening-followups.md` is the open P1 epic
  `syzygy-u2a`'s approved implementation guidance. Check the `bd` issue.
- Before editing any governance prose, hash the file and grep the manifests —
  a file listed in a performed act's manifest is bound (`ACCEPTANCE-ACT-RECORD.md`
  names the argument). `openspec/changes/polaris-project-wide-butlers-model/`
  is bound this way: it cannot take a status banner at all.
- **A bound file's own banner can be permanently wrong, and correcting it is
  forbidden.** Both adopted specifications still open "Candidate
  specification… until that act, this change binds nothing" —
  `project-registration-and-honest-shape-visibility/proposal.md` (bound by
  `CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`) and
  `three-surface-poc-experience/proposal.md` (bound by
  `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`). The act bound the bytes that say
  it, so the sentence is now false and uncorrectable, in both directions:
  the same shape as CC-SPEC/CC-IMPACT living under `policy-candidates/`.
  Trust the act record and the routing table above; a package banner is
  evidence of what a drafter believed, never of what binds.
- **A package's own manifest is part of the digest-binding corpus.** A sweep
  that excludes the directory under audit will call its files unbound when the
  sibling `*-MANIFEST.txt` carries them as rows (rule 4). This is how
  `general-trusted-bootstrap-authorization/ACT-SEMANTICS.md` and its
  `IMPACT-LEDGER.md` read as free: both are rows of `TRANSACTION-MANIFEST.txt`
  in the same directory, so ACT-SEMANTICS.md permanently opens "Candidate —
  binds nothing" about a transaction performed 2026-09-01. The eight unbound
  prose files in the three PWB packages took dated **PERFORMED** heads instead
  (2026-09-06, `syzygy-bba`); the pre-act banner stays beneath, unedited.
  Membership in the package directory is neither necessary nor sufficient,
  so read the rows: of the 8 files in that one, 5 are digest-cited and 3
  (`CANDIDATE-TRANSACTION-REPORT.md`, `OWNER-SIGNOFF-PACKET.md`,
  `REVIEW-BRIEF.md`) are not.
- **An act's *preservation* language edit-locks files whose digest appears
  nowhere.** Both Capability 1 acts name `round-2026-08k` as their evidence
  chain and say it is preserved. In `decisions/`,
  `CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md` lines 7-9 name
  `REVIEW-BINDING.md`, reviews RS-1…RS-5 and the adoption PREPARED packet as
  "preserved unchanged"; `CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`
  lines 6-8 name the implementation PREPARED packet "banner-marked performed,
  preserved". All 9 tracked files under that directory return **0** digest
  citers across every tracked file under `.syzygy/`, `openspec/`, `docs/` and
  `scripts/`, and the acceptance record never names the path — so the manifest
  grep, the digest grep and the record grep all read them as free. The lock is
  the act's own sentence. Route around the language; there is no hash to
  mismatch.
- **Zero digest citers does not mean never bound.** A raw review that quotes a
  digest freezes those *bytes*, not the path, so a file edited after its
  confirmation looks identical to one no review ever touched.
  `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md`, in
  `contracts/candidates/`, has 0 citers for its current hash while
  `docs/reviews/R-GENERAL-TRUSTED-BOOTSTRAP-SEMANTIC-DELTA-6-RAW.md:3`
  confirms a digest the file stopped hashing to two commits later, before the
  diff that added RFC4-23, RFC8-16 and CC-SPEC-8 to its affected-ID set. That
  is rule 10 working: the review confirms history and the current bytes carry
  no confirmation. Before calling a governed file unreviewed, grep the raws
  for *any* digest cited against its path, not only its current one — and do
  not copy the stale prefix into your finding, which is CG-15's whole point.
- **An *unperformed* act's prepared argument is just as untouchable, and
  nothing in the file says so.** `.syzygy/intent/OVERVIEW.md` is the argument
  of act 4, `ADOPT PROJECT OVERVIEW`, which has never been performed — so its
  hash appears in no performed act's manifest and the manifest grep above
  returns clean, yet editing one word regenerates the argument and retires any
  confirmation bound to it. Grep
  `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` for
  the path too. Its false "Nothing is implemented" sentence is queued as P-59
  for exactly this reason; do not repair it.
- Every `round-*` directory now carries a `README.md` naming what the round
  settled, where that settlement lives now, and its live-input cautions;
  `contracts/candidates/ROUND-ESTATE.md` is the route across all eleven. The
  96 unbannered *file* heads inside them are unchanged — but **only 19 of the
  96 could ever be banner-marked**, and the other 77 are not an owner's to
  authorize: 74 are raw reviewer output under a round's `reviews/`
  subdirectory (CC-REV-6 stores raw output unchanged, which is not a question
  of authority), two are digest-bound, and one is regenerated and
  byte-compared by CI. A count of unbannered heads measures what a reader may
  open, never how much work is available; check what protects each file before
  costing a pass over a population.
- `docs/README.md`'s review-campaign table is ten rows over every file in
  `docs/reviews/`, each row carrying its last verdict of record and where the
  findings landed. It is re-derived, not maintained: the count moved 88 → 90
  within a day of being written, and again the same day, so rerun the
  partition rather than trusting a row.
- **An index that routes by short name makes the files it routes read as
  orphans.** `contracts/candidates/reviews/DISPOSITIONS.md` sections are
  titled "rev10-boundary", "rev10-safety" — never the filename — so a sweep
  for a report by its own basename finds no citer and reports it unread
  (rule 9's false-absence class again, this time in the *citer's* form rather
  than the identifier's). It cannot be repaired at the site: the general
  trusted-bootstrap `IMPACT-LEDGER.md` classifies that file as raw-review
  evidence "never rewritten to current semantics", and the ledger is a row of
  its own package's transaction manifest, so the classification binds. Route
  from the nearest *unbound* index instead — the map from filename to verdict
  to disposition section now lives in `candidates/README.md`.
- **A citation wrapped across a line break is invisible to every basename
  sweep, so every absence figure in this corpus carries an unmeasured error
  term.** These pages are hard-wrapped at 78 columns, and a wrapper that
  breaks inside a code span leaves half a filename on each line:
  `docs/PWB-IMPLEMENTATION-PLAN.md` cited a mutation-run record as
  `…-2026-09-05.` + `json`, which is why one evidence file read as uncited by
  a full-basename sweep and as cited by a stem sweep — both were right. To
  measure it, take each non-fence line with an odd backtick count, join its
  tail to the next line's head, and test the join against the tracked
  basenames; a hit that neither half carries alone is a wrapped citation.
  Repaired 2026-09-06 in three places over 165,027 non-fence lines; the one
  remainder is in `round-2026-08/ROUND-DISPOSITIONS.md`, which is historical
  and not edited. Never let a reflow break a code span.
- **A home's README describing what it will hold goes false the moment it
  holds something, and a stored review may make the false sentence
  undeletable.** `decisions/launch-gate/README.md` said "Empty today,
  correctly: no formal administration has been run" for nineteen days after
  Administration 1 landed beside it, stated a filename convention
  (`ADMINISTRATION-<n>-<date>.md`) that the one record never followed, and
  named neither the canonical JSON nor the two other file classes present.
  `round-2026-08e/reviews/RD-28-spec-authoring-RAW.md` quotes that exact
  sentence verbatim as evidence of the project's epistemic discipline, so it
  was marked and dated in place, not removed — a review's referent may not be
  edited out from under it. Retain a validation transcript beside every future
  administration record: rule 7 makes a transcript valid only for the commit
  it names, and a JSON record with none is a record no later reader can
  confirm was checked.

### Known gaps

- syzygy-ydr: non-blocking S2/S5 review findings outstanding.
- Butlers data quirks (as of `13d269b`): `v1.md` is whole-source Unknown
  (five colon forms and four duplicate labels outside the signed dash
  grammar); Spec and Spine's home `openspec/` has no index, so the
  whole-shape claim is Unknown; `components.md` fails the table grammar
  (seven code-span first cells); `frontend.md` and 7 of 13 `butler.toml`
  are withheld as active content (TOML has no inert context). Repairs for
  the first three were ruled 2026-09-07 (P-60/P-61/P-62) and sit on
  Butlers PR #4066, cleared to merge once the P-63 trim is on main. Do not
  relax the grammar or policy without an owner gate.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
### Governance recorders (digest-bound acts)

- Each digest-bound owner act has a dedicated recorder script that
  hard-codes the frozen subject and packet head, validates the owner's
  phrase against current bytes, writes a new dedicated record and appends
  one aggregate section to `ACCEPTANCE-ACT-RECORD.md`; `--check` must
  count exactly one copy of its block, never assume it is the file tail.
  A superseding act gets a new record; the superseded record is never
  edited, and its recorder fails `--check` by design.
- Register a new act phrase in `check_governance.py`'s `_act_subjects()`
  and its packet copies in `ACT_DIGEST_COPY_FILES` before the packet
  exists, or CG-7d cannot see them go stale; files that appear only after
  an act are registered from an existence-gated activation function.
- Plain owner directions (implementation authorization, continuation)
  bind no digest, add no acceptance-record row and register nothing.

## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Session Completion

**MANDATORY — work is NOT complete until `git push` succeeds:**

1. **File issues** for remaining work; close finished issues, update
   in-progress ones
2. **Run quality gates** (if code changed)
3. **Push**: `git pull --rebase && git push`; `git status` must show
   "up to date with origin"
4. **Clean up** (stashes, stale branches) and **hand off** context for the
   next session

NEVER stop before pushing — that strands work locally. If push fails,
resolve and retry until it succeeds.
<!-- END BEADS INTEGRATION -->
