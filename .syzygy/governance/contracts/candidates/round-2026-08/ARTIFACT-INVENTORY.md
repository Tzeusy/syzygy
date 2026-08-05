# Artifact inventory — post-round tracked tree

**Derived record (2026-08-05, counts scripted from
`git ls-files --cached --others --exclude-standard`, excluding the round
prompt file).** 176 files at the time of counting; the round added files afterwards, so read this as a shape record, not a live total. Lifecycle labels are the artifacts' own; this
inventory asserts none.

**No digests, deliberately (corrected 2026-08-05b).** This table quoted
truncated act digests for acts 1, 2 and 3. Two of the three had gone stale —
they named the pre-fix-batch values while the acts had moved on — and no
check could see them, because `check_governance.py` CG-7d matches only a
*full* 64-hex digest on a line that also carries the act phrase. A truncated
convenience copy was invisible to it. The digests are removed rather than
corrected: the fix for "a derived value quoted for convenience is a promise"
is to stop making the promise, not to renew it. Each row now names the
artifact that owns the digest. CG-15 now sweeps truncated digest quotes
corpus-wide, and its regression fixture is exactly this table's old text.

| Cluster | Files | Lifecycle | Notes |
|---|---:|---|---|
| Repository root (README, AGENTS, PROJECT-STATUS, CONTRIBUTING, SECURITY, CLAUDE.md, .gitignore) | 7 | procedure / presentation | Front door installed this round (P-11) |
| `.syzygy/governance/doctrine/` | 6 | **Adopted** | D1 in force; D3 proposed (act 5) |
| `.syzygy/governance/decisions/` | 5 | Recorded / pending | SDR record, two FD-037 extracts, pending queue, license packet |
| `.syzygy/governance/policies/craft-and-care/` | 10 | **Owner-approved (D2)** | Banners corrected this round; act-2 confirmation pending — digest in `INSTALL-RECORD.md` |
| `.syzygy/governance/contracts/candidates/rfcs/` | 32 | **Candidate** | RFC 0001–0011; act-1 subject is `ACTIVE-CONTRACT-MANIFEST.txt`, whose own digest is the argument |
| `candidates/` top level | 22 | Candidate / gate definition / derived / packet history | Manifest, acceptance record, D3 draft + revised packet, rev10 delivery reports, derived indexes |
| `candidates/fixtures/` | 9 | Candidate (5 accepted-set + 3 draft + 1 equivalence set) | Loads/digests re-measured this round |
| `candidates/history/` | 19 | Historical, non-normative | Rev9 corpus + Tier-2 extracts; "nothing binds" |
| `candidates/matrix-rows/` | 9 | Derived accounting | RFC-0006 rows still unreviewed (P-10 → battery vertical 4) |
| `candidates/reviews/` | 9 | Evidence, verbatim | Rev10 battery + confirming review + dispositions |
| `candidates/policy-candidates/` | 4 | Candidate | Term registry, hygiene policy, delta template, change workflow |
| `candidates/round-2026-08/` | 11+ | Round process records | This round's reports, deltas, review raws (grows until round close) |
| `candidates/scripts/` | 4 | Tooling (portable, self-rooted) | verify / index ×2 / context_load |
| `.syzygy/map/topology-candidates/` | 11 | **Candidate** | 9 members + `BUNDLE-MANIFEST.md` (act-3 subject; its digest is the argument) + tracking note |
| `.syzygy/intent/OVERVIEW.md` | 1 | Draft (act 4) | Four-layer refactor this round |
| `scripts/` + `.github/` | 2 | Tooling / CI | `check_governance.py`; documentation-only workflow |
| `.claude/` + `.codex/` skills | 3 | Navigation aids | heart-and-soul (two homes; known uncontrolled-copy pair) |
| `.beads/` | 11 | Process tracker | Hooks tracked but not installed by clone; process housekeeping only |

Founder-local (deliberately not tracked): `_bootstrap/**` — see
`HISTORICAL-ARCHIVE-INDEX.md`.
