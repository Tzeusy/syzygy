# Review battery vertical 7 — evidence and security (RAW, verbatim)

**Reviewer:** fresh-context subagent, 2026-08-05. Given only: the review
charge, the clone-visible tree. **`_bootstrap/**` was not read** (hard
constraint honored; everything cited below is clone-visible).

## Provenance — commands run

- `git ls-files`; `git ls-files --others --exclude-standard`; `git status --porcelain`; `git log`; `git tag --list`; `git show fcb05c0:.syzygy/intent/OVERVIEW.md | sha256sum`; `git diff` (doctrine README, SURFACE-DECISION-RECORD)
- `sha256sum *.md` in `.syzygy/governance/policies/craft-and-care/`
- `sha256sum BUNDLE-MANIFEST.md` and `sha256sum -c` over the member block in `.syzygy/map/topology-candidates/`
- `sha256sum ACTIVE-CONTRACT-MANIFEST.txt` and `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` in `.syzygy/governance/contracts/candidates/` (all 32 entries OK)
- `sha256sum .syzygy/intent/OVERVIEW.md`
- `python3 scripts/check_governance.py` (full output read; result: 12 OK, 7 WARN, **1 FAIL — CG-7b**)
- Python `re` secrets scan (stdlib, script inline below in §6) over `git ls-files` ∪ `git ls-files --others --exclude-standard` — 178 files
- Full reads: doctrine `security.md`, `trust-and-evidence.md`; root `SECURITY.md`, `README.md`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`; `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`; RFC-0005 all three modules; RFC-0003 `governance-homes-and-owner-acts.md`; RFC-0004 `named-adapters.md` RFC4-13 block; craft `INSTALL-RECORD.md`, `security-and-secrets.md`, `agent-provenance-and-execution-evidence.md`; decisions extracts (`OWNER-ANSWERS-2026-08-01.md`, `DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`, `SURFACE-DECISION-RECORD.md` head); `round-2026-08/SEMANTIC-DELTAS-THIS-ROUND.md`, `ARTIFACT-INVENTORY.md`; topology `BUNDLE-MANIFEST.md`, `TRACKING-NOTE.md`; all five `.beads/hooks/*`; `scripts/check_governance.py` (entire); `candidates/scripts/build_contract_index.py` and `build_dependency_index.py` main() paths; `.github/workflows/governance-docs.yml`; `.claude/settings.json`; `.beads/config.yaml`; `.claude/skills/heart-and-soul/SKILL.md`; `.syzygy/intent/OVERVIEW.md` header.

## §1 Digest verification results (charge item 2, mechanical leg)

**INSTALL-RECORD current-digest block: VERIFIED.** All nine sha256 values in
the 2026-08-05 correction block (`INSTALL-RECORD.md:60-68`) match
`sha256sum *.md` run in the directory, byte-exact, including
`3858820f…  testing-and-verification.md` (the new act-2 argument). The
superseded install-time block is retained and labeled "historical —
superseded" (`INSTALL-RECORD.md:28`) — an honest was/now record.

**Topology bundle: VERIFIED internally.** All nine member digests in
`BUNDLE-MANIFEST.md` check OK; the manifest's own sha256 is
`89279260e4b2a74c0c32503e082802bee5811b54b42d329d265cd7df3e671ef9`. The
manifest carries its regeneration note (line 9: member digests regenerated
2026-08-05, P-6 second leg) and `TRACKING-NOTE.md` records
promoted-verbatim-then-corrected-once with the semantic delta cited (SD-2).

**Contract manifest: VERIFIED internally.** All 32 module entries in
`ACTIVE-CONTRACT-MANIFEST.txt` check OK; the manifest's own sha256 is
`5c4d6798354135bd860b3a2637c282f535c519bdd1a3cbab67d7555367af6caa`.

**Overview:** working-tree `.syzygy/intent/OVERVIEW.md` hashes
`49a1a09c2f45ac6df9be19f48f1c136e37f52e4f627cbdcd097e91a3452e61fa`; the
version at commit `fcb05c0` hashes `42de2eb1…` (matches the recorded act-4
argument). The working tree carries an uncommitted ~334-line refactor
(`git diff --stat`).

**No act performed anywhere:** `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`
does not exist; CG-6 confirms neither accepted home exists;
`PROJECT-STATUS.md:33` states this explicitly and correctly. No artifact
found claiming a performed act that did not happen. The
"artifact edited after its act has no act" rule survives verbatim at the
acceptance record §2 (line 106-108), RFC3-16(b) item 3, and
`BUNDLE-MANIFEST.md:7-8`.

## §2 Findings

### F1 — The acceptance record's §1 offers are stale for all four digest-bound acts, and two of its own invariant claims are now false — **material**

The gate-defining record
(`.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`)
still offers, at §1:

- **Act 1** (line 15): `ACCEPT COMPACTED FOUNDATIONAL RFCS: 08793ddf…` — the
  manifest now hashes `5c4d6798…` (SD-1's retired-phrase fix in RFC-0003
  regenerated it). The repo's own checker fails on exactly this:
  **CG-7b FAIL** — "the act would bind a package that no longer exists".
- **Act 2** (line 16): `CONFIRM CRAFT AMENDMENT: CC-TEST-2@aa2d6353…`,
  described as "Unchanged from rev9" — `INSTALL-RECORD.md:71-74` correctly
  declares that argument **stale and satisfying nothing**; the current
  argument is `CC-TEST-2@3858820f…`. Two clone-visible sources now define
  act 2 with different arguments; the gate-defining record holds the wrong
  one.
- **Act 3** (line 17): `ACCEPT TOPOLOGY: 0d34d1b5…` with the claim "The
  rev10 pass altered no topology file" — the bundle manifest was regenerated
  2026-08-05 and now hashes `89279260…`. The row's claim was true at rev10
  and is stale now; nothing in the record says so.
- **Act 4** (line 18): `ADOPT PROJECT OVERVIEW: 42de2eb1…`, "Unchanged from
  rev9" — the working-tree overview hashes `49a1a09c…` after this round's
  refactor.

Additionally §3 (line 124-125) asserts "**The phrase in §1 always carries
the current manifest digest**" — currently false — and §6 binds the CONFIRM
verdict to `08793ddf…` only; **no digest-binding review covers `5c4d6798…`,
`3858820f…`, `89279260…`, or the new overview bytes yet** (SD-1 states one
is "scheduled this round" — this battery is presumably it, but a vertical
review is not the exact-manifest confirming review the AGENTS/record
discipline requires).

Why material and not blocking: the §2 step-2 ceremony ("Any mismatch means
no act: regenerate, re-review, re-offer") and CG-7b make a void act
detectable before it fires, and the round's own registers (SD-1, SD-2, SD-3,
`ARTIFACT-INVENTORY.md:13-14,23`) carry the new digests honestly. But the
record cannot be executed as written, three "Unchanged from rev9" claims and
one "always carries the current digest" claim are presently false on the
authoritative gate surface, and an owner reading only the acceptance record
would copy dead phrases. **Required before any act:** refresh §1 rows 1–4
(and the row-2/3/4 "Unchanged" prose), then run the digest-binding
confirming review over the refreshed digest set.

### F2 — Act 4's regeneration chain is the only one without a was/now record — **material**

Acts 1–3's digest churn each carries an honest was/now trail: SD-1
(08793ddf → regenerated, review scheduled), INSTALL-RECORD's correction
block (aa2d6353 → 3858820f, old block retained as historical), SD-2 +
`BUNDLE-MANIFEST.md:9` + `TRACKING-NOTE.md` (0d34d1b5 → regenerated by
script). The overview's ~334-line "four-layer refactor" (git diff;
`ARTIFACT-INVENTORY.md:24`; `PROJECT-STATUS.md` gate 7) invalidates the
act-4 offer `42de2eb1…` but appears in **no semantic-delta entry**
(`SEMANTIC-DELTAS-THIS-ROUND.md` SD-1…SD-7 do not mention it), records no
new digest anywhere, and leaves the acceptance record claiming "Unchanged
from rev9". The register's scope line ("every normative or
authority-adjacent edit") arguably exempts a presentation artifact — but the
overview is a **digest-bound act subject**, which is authority-adjacent by
construction. The chain the charge asks about is honest for three acts and
absent for the fourth.

### F3 — SECURITY.md's executable-content disclosure is incomplete, and "read-only" is false for two of the four candidate scripts — **material**

`SECURITY.md:7-12` discloses `.beads/hooks/` and "read-only Python
validation scripts under `.syzygy/governance/contracts/candidates/scripts/`
and `scripts/`. Nothing else executes." Verified against the tree:

- **Correct:** the five `.beads/hooks/*` exist (all are thin
  `bd hooks run …` wrappers, no-ops without `bd` on PATH), and the claim
  "not installed by cloning — `git clone` never activates hooks" is
  accurate: they live outside `.git/hooks/` and nothing in a clone sets
  `core.hooksPath`.
- **Correct:** `scripts/check_governance.py` is read-only end to end (only
  `open(...)` reads and read-only `git` subprocesses; no write/rename/delete
  call anywhere), as is `verify_final_prespec.py` by the same inspection.
- **False for two scripts:** `candidates/scripts/build_contract_index.py:166`
  and `build_dependency_index.py:181` call `out.write_text(...)` in their
  **default** (non-`--check`) mode, rewriting `05-CONTRACT-INDEX.yaml` and
  `CONTRACT-DEPENDENCY-INDEX.md`. Scope is two derived in-tree indexes —
  benign — but "read-only" on the public security surface is a strengthened
  claim the bytes do not support. Say "read-only in `--check` mode; the two
  index builders regenerate their own derived index files otherwise".
- **Undisclosed executable content #1:**
  `.github/workflows/governance-docs.yml` runs on every push/PR in GitHub
  Actions (permissions `contents: read`, runs the three checkers — benign,
  but it executes and is not in the disclosure).
- **Undisclosed executable content #2:** `.claude/settings.json` defines
  `SessionStart` and `PreCompact` hooks executing `bd prime` — this **does**
  activate for anyone who clones and opens the repo in Claude Code with `bd`
  installed, which is precisely the class of surprise the disclosure
  paragraph exists to prevent.

### F4 — SECURITY.md's SEC-2/SEC-5 rows import candidate/craft wording into a "faithful summary" of doctrine — **minor**

Row SEC-5 (`SECURITY.md:28`): "applies at every ingest boundary" — doctrine
SEC-5 (`security.md:54-55`) says "**Observation** applies a declared
secret-detection policy"; "every ingest boundary" is RFC5-16's (candidate)
and CC-SEC-5's (craft) widening. Row SEC-2 (`SECURITY.md:25`): "the
dependent feature renders Unknown" — doctrine says "the **inferred layer**
renders Unknown" (`security.md:33-34`); "dependent feature" is CC-SEC-2's
generalization. Both drift in the strengthening direction and the "doctrine
wins" line (`SECURITY.md:19-20`) caps the damage, but a summary that claims
faithfulness to doctrine is quietly presenting unaccepted-candidate/craft
scope as adopted rule — the exact claim-class leak this vertical is charged
to catch. Fix by tracking doctrine's own nouns or marking the widened scope
as craft/candidate.

### F5 — PROJECT-STATUS.md "Known blocking defects: None known" is contradicted by its own listed verifier — **minor**

`PROJECT-STATUS.md:52` says none known at the 2026-08-05 revision, while
`PROJECT-STATUS.md:67` instructs `python3 scripts/check_governance.py`,
which at that same revision exits FAIL (CG-7b, finding F1). The stale-offer
condition blocks act performance and was known to the round (SD-1). Either
list it or scope the sentence ("no blocking defects other than the
scheduled acceptance-record digest refresh, CG-7b"). Self-limiting because
the file's own header routes disagreement to the owning record.

### F6 — Pending-decision register as-of line is one commit stale — **minor**

`PENDING-OWNER-DECISIONS.md:9` says "As-of: 2026-08-04, HEAD `adddc34`";
HEAD is `9e6f2f7` and P-6/P-7/P-8's fixes have since landed
(INSTALL-RECORD correction block, banner fixes, manifest regeneration).
CG-10 reports this by design ("never auto-verified"). Refresh with the
round-close sweep.

## §3 Charge answers not already covered

**Claim classes and provenance (charge 1) — consistent, one leak (F4).**
Observed/Inferred/Unknown definitions in `trust-and-evidence.md` are applied
faithfully downstream: RFC-0005's [Inferred] tags mark exactly the
author-derived bridging arguments (e.g. RFC5-4 lifetime rationale, RFC5-11's
RFC2-4 reconciliation); the SEC-3 committed-artifacts extension carries its
**[Inferred]** label at its single home (RFC3-16(a),
`governance-homes-and-owner-acts.md:216-218`) and is flagged for owner
ratification at the acceptance record §7 item 2 — modules that rely on it
cite the labeled clause rather than silently restating it, which is the
right shape. RFC4-13's four routes, craft CC-PROV-4's report-fact /
gate-backed rendering, and CC-TEST-2's amended scope agree with each other.
Front-door surfaces (README, PROJECT-STATUS, CONTRIBUTING, OVERVIEW header,
heart-and-soul skill) label candidate material candidate throughout; no
surface found rendering an Inferred or candidate claim as
Observed/accepted, except the F4 wording drift.

**P-8 binding (charge 3) — satisfied.** INSTALL-RECORD's Status paragraph
binds craft force to "the digest-bound acceptance act defined in the active
acceptance record (currently `ACCEPT COMPACTED FOUNDATIONAL RFCS: <manifest
digest>` …)" — the acceptance record §1 row 1 defines exactly that act, and
RFC3-15's contracts-row install gate uses the same formulation, so the
binding is satisfiable and single-sourced. The retired phrase is named as
"retired and satisfies nothing" without touching D2: the paragraph still
opens "these policies are owner-approved engineering standards", the D2
provenance sentence is unchanged in substance (citation repointed to the
FD-037 extract), and SD-4 records "Does not change: D2 approval provenance".
The only caveat is F1: until the record's §1 digest is refreshed, "the act
defined in the active acceptance record" names a phrase step 2 would refuse.

**RFC-0005 vs SEC-1..5 (charge 4) — no weakening found; spot-check of nine
clauses:** RFC5-3/RFC5-4 (SEC-1 origin/CSRF incl. loopback, absent-Origin
neutrality, DNS-rebinding defense — all present, made structural);
RFC5-5/RFC5-6 (SEC-1 machine-client mechanism — explicit, deny-by-default,
verifier-only storage); RFC5-8/RFC5-10 (SEC-1 exposure — strengthened to
refuse-to-serve fail-closed and loopback-only fresh install); RFC5-14/15
(SEC-2 — single choke point, closed content classes, highest-embedded-class,
unnamed provider requires fresh consent, absent consent → inferred layer not
computed, matching doctrine verbatim); RFC5-16/17 (SEC-5 — fail-closed both
directions, hash-not-body); RFC5-18–21 (SEC-3 — five-part gate, no ambient
credentials, no "none" isolation class, no-credential-and-no-route to
Syzygy); RFC5-22 (VIS-4 always-human classes non-standing-approvable);
RFC5-25 (audit trail outside untrusted write reach, load-bearing for
RFC3-16(a)). No candidate or presentation text found promising execution of
observed code, network exposure, or egress outside these gates —
`execution-profiles.md:31-33` states the blocking rule plainly, and
RFC4-13's authority line repeats "Syzygy reads reports; it does not run
them".

**Owner-act rule integrity (charge 2, remainder):** doctrine edits this
round were verified by diff to be the two SD-5 citation repoints only (D1
row in the doctrine README amendment log; SDR packet pointer) — no adopted
rule text touched; `doctrine-adopted-2026-07-30` tag present. The FD-037
warrant's verbatim text lives founder-local (charge notes it as classified
history); from a clone the warrant is asserted, not verifiable — consistent
with the stated two-state posture, noted here for completeness rather than
as a finding.

## §4 Secrets scan (charge 6)

Method: Python 3 stdlib `re` over the 178 files in `git ls-files` ∪
`git ls-files --others --exclude-standard` (UTF-8, errors=replace), pattern
classes: PEM private-key headers, AWS `AKIA…` key IDs, GitHub `ghp_/gho_/…`
tokens, Slack `xox…` tokens, generic `api_key/secret/password/token =
"…16+ chars"` assignments, connection strings with embedded credentials
(`postgres|mysql|mongodb|redis|amqp://user:pass@`), `Authorization: Bearer`
values, JWT triplets, `sk-…`/`sk-ant-…` model-provider keys.

Result: **0 hits — none found by this method.** This is not a claim that
none exist: the method misses novel token formats, high-entropy strings
without keyword anchors, and anything encoded or split. `.beads/config.yaml`
was additionally read by hand: it documents secret keys (linear.api_key,
github.token) but contains only commented placeholders, no values.

## §5 Verdict

Substantive, fixable defects on the digest-offer chain and the public
security surface; no false act claims, no doctrine weakening, no secrets
found, fail-safes intact.

VERDICT: EXCEPTIONS
