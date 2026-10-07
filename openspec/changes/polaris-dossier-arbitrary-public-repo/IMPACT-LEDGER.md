# Impact ledger — Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** Review material, not an authority or an
> adopted applicability judgment.

## Method

[Observed] Sweeps ran by script over `git ls-tree -r -z --name-only HEAD` at
`origin/main` commit `3409ef5ae9f7dcbadbb248d4df1c295dc43a5b0b`, excluding
this change's own directory (absent at that commit). Denominator (rule 9):
2,569 tracked paths, of which 4 do not decode as UTF-8 and were skipped, so
2,565 were searched. Python `re`, never `grep` (verification rule 1). Row
classes by first matching rule: a path ending `-RAW.md` or containing
`/reviews/` is a raw; then `docs/evidence/`; then `.syzygy/governance/decisions/`;
then the rest of `.syzygy/`; then `openspec/`; then `apps/`, `packages/` and
`scripts/` (code); then the rest.

| Sweep | Regex (Python) | Files | Raw | Evidence | Decisions | `.syzygy` other | OpenSpec | Code | Other |
|---|---|---|---|---|---|---|---|---|---|
| A: the Redis key | `redis-redis`, case-sensitive | 37 | 6 | 1 | 2 | 9 | 0 | 19 | 0 |
| B: the consent phrase | `observation consent`, `re.I` | 181 | 33 | 10 | 24 | 54 | 10 | 40 | 10 |
| C: REQ-033 | `REQ-polaris-generation-033`, case-sensitive | 77 | 7 | 5 | 3 | 20 | 4 | 37 | 1 |
| D: ruling 10b's phrase | `maintainer-stated`, `re.I` | 19 | 1 | 0 | 3 | 4 | 2 | 7 | 2 |
| E: the drawer predicate | `kernel evidence drawer`, case-sensitive | 34 | 7 | 0 | 0 | 7 | 3 | 16 | 1 |
| F: the new identifiers | `REQ-polaris-generation-03[789]`, case-sensitive | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Second method (rule 2), for F only: `git grep -l -E "REQ-polaris-generation-03[789]" HEAD`
returns no file, equal to F. A to E carry no second method and are reported
as sweeps, not proofs of completeness. A continuation form ("REQ-033/034")
is not covered by C [Unknown]; it does not change a disposition below,
because nothing that cites REQ-033 is edited.

**Digest citers of the amendment and successor targets** [Observed: scratch
`arb_bound_check.py`, which hashes each target and searches every tracked
file for the full digest or its first 16 characters; population 2,577
tracked files on the branch, 2026-10-08]:

| Target | Citers |
|---|---|
| `doctrine/architecture.md` (A1) | The candidate D7 and D8 packages: `doctrine-amendment-held-derived-computation-d7/` and `doctrine-amendment-inferred-first-class-d8/`, each in `OWNER-DECISION-PACKET.md` and `SEMANTIC-DELTA.md` |
| `doctrine/README.md` (not amended) | none |
| `RFC-0001-…-state-planes.md` (A2) | `ACTIVE-CONTRACT-MANIFEST.txt`; `contract-readability-restyle/CONTRACT-AMENDMENT-MANIFEST.txt` |
| `RFC-0003/manifests-and-namespace.md` (A3) | the same two manifests |
| `RFC-0005/consent-egress-secrets.md` (A4) | `.github/workflows/governance-docs.yml`; `ACTIVE-CONTRACT-MANIFEST.txt`; `rfc5-project-documentation-class/CONTRACT-AMENDMENT-MANIFEST.txt`; `decisions/ACCEPTANCE-ACT-RECORD.md`; `decisions/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`; `PROJECT-STATUS.md` |
| The installed source-acquisition entry, `declarations/adapter-registry/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json` (slice 3) | `dossier-local-agent-acts/DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt`; that package's `reviews/R-DOSSIER-LOCAL-AGENT-SITTING-3-RAW.md`; `decisions/PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1.0.md` |

Every target with a citer is bound or reviewed bytes: none is edited by this
change, and each moves only through its own act or successor version.

## Disposition by class

- **Act records, decisions, evidence and raws: not edited.** They cite Redis,
  REQ-033 and the consent phrase as they stood. This change edits no file
  outside its own directory except one `openspec/README.md` row and, for the
  round 1 raw, `docs/README.md` and the partition script's campaign list.
- **Redis.** Its observation consent, Anthropic statement, D9, the RFC7-20
  reading and the screening scope stay exactly as recorded, and the standing
  route never reaches it. **REQ-038 does reach Redis's runs** (packet Q5):
  its motivations and trade-offs may be reconstructed, narrowing how ruling
  10b and REQ-034's "maintainer-stated advantages and trade-offs" topic
  apply to Redis. No Redis record is edited for that; the ruling's record
  stays as it is, and REQ-038 states the narrowing.
- **Code keyed on Redis (A, 19 files).** Three are source:
  `packages/polaris-dossier/src/gate-sources.ts` (`DRAWER_FORMS`,
  `STATEMENT_FORMS`) and the recorders `scripts/record_dossier_local_agent_acts.py`
  and `scripts/record_public_repo_admission_acts.py`; the other 16 are tests.
  They change in slices 2 and 4 of `design.md`, after sign-off.
- **Code implementing the governed predicate (E, 16 files).**
  `packages/polaris-dossier/src/governed.ts` keeps its tree predicate
  unchanged; its drawer input gains the standing record as a source, and its
  disclosure gains the fold's residual (slice 4).
- **Code using "maintainer-stated" (D, 7 files).** The provider-mode prompt
  and evaluation files under `packages/polaris-generation-core/` belong to the
  parked provider mode, which this change does not touch. The local-agent
  brief test (`packages/polaris-dossier/src/brief.test.ts`) changes with the
  brief's reader topics (slice 8).
- **OpenSpec (B 10, C 4, D 2, E 3).** The adopted changes are bound and not
  edited. REQ-037 and REQ-038 name the exact predecessor sentences they read.

## Edits required (CC-IMPACT-5, 6)

| Artifact | Why it moves | Actor |
|---|---|---|
| `openspec/README.md` | `scripts/check_spec_reconciliation.py` R5 wants one row per tracked change directory; the row says candidate, binds nothing. Its SHA-256 appears in no tracked file, so it is not act-bound [Observed: the sweep above] | This candidate (existence-time) |
| `docs/reviews/R-ARBITRARY-PUBLIC-REPO-1-RAW.md`, `docs/README.md`, `scripts/check_docs_review_campaign_partition.py` | Round 1 raw retained verbatim, with its campaign pattern and row | This candidate (done) |
| `doctrine/architecture.md`, `DOCTRINE-AMENDMENT-LOG.md` | A1 | Owner's doctrine amendment act, after its own review |
| RFC-0001, RFC-0003, RFC-0005 modules; `ACTIVE-CONTRACT-MANIFEST.txt`; the workflow's pinned RFC-0005 digest; `ACCEPTANCE-ACT-RECORD.md` | A2 to A4 | Owner's contract amendment act(s), in the RFC5-14 act's form |
| The D7 and D8 candidate packages | Their cited `architecture.md` digest goes stale when A1 lands first (or A1's when they do) | Whichever package lands second |
| A new standing consent record in `decisions/` | A5 | Owner's consent act |
| The source-acquisition entry, candidate (`public-git-source-acquisition-local-agent/proposed/…json`) and installed (`declarations/adapter-registry/…json`) copies | Subject must admit a standing-admitted pair; the gate reads the installed copy (`packages/polaris-generation-consent/src/package-reader.ts:773`) | A new version and its version-tagged sign-off (slice 3) |
| The candidate spec in `proposed/` | Moves to `specs/polaris-generation/spec.md` | Installing change |
| `GOVERNING-DEPENDENCIES.md` | Regenerated by `--write-additions` on install | Installing change |
| `PROJECT-STATUS.md` | Requirement and scenario figures rise by 3 and 32 (18 + 10 + 4 scenario headings), or by 2 and 28 without REQ-039 [Observed: 32 `#### Scenario:` headings in the proposed spec, counted by `grep` and by a Python count] | Installing change |
| `DIRECTIVE-REGISTER.md` | Generated; gains 037 to 039 | Installing change |
| `docs/polaris-generation/TARGETS.md`, the `/polaris-dossier` skill | Candidate guidance naming per-repository consents | Optional, slice 8 |

## Undecidable impact (CC-IMPACT-4)

- [Unknown] Whether the owner takes the amendment route at all (packet Q0),
  and whether D7 or D8 lands before A1.
- [Unknown] Whether history is admitted (Q2): if not, REQ-037's history
  paragraph and its scenario stay as a disabled option or are struck before
  sign-off.
- [Unknown] Whether REQ-038 reaches Redis (Q5) and whether REQ-039 survives
  (Q6); each changes the scenario figures above.
