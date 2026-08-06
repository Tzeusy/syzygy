# Public-clone authority matrix — human-clarity refactor round

**As-of round start:** HEAD `9e6f2f7`, 2026-08-05. "Founder machine" =
exists under git-excluded `_bootstrap/**` (or machine-local config);
"Public clone resolves it?" = a fresh `git clone` can read the artifact and
resolve its essential citations. **Required action** is this round's plan
under the owner's §7 dispositions; nothing in this file is itself an
adoption or acceptance.

| Artifact | Founder machine | Git tracked | Public clone resolves it? | Lifecycle | Authority | Required action |
|---|---:|---:|---:|---|---|---|
| Doctrine cluster (6 files + D1) | mirror | ✔ | ✔ | adopted | authoritative (why) | none (adoption-status lines per-file: reviewer item, fix in round) |
| Owner surface decisions SDR-1..33 | mirror | ✔ | partially (some `_bootstrap` warrant pointers) | recorded | authoritative (decisions) | FD-037 repoints |
| Founder decision log FD-1..37 | ✔ | ✘ | ✘ | recorded | owning record for FD citations | P-15: promote compact decision register to `decisions/` |
| Pending-decision register P-1..16 | — | ✔ | reads queue, cannot resolve `_bootstrap` owning records | pending (stale as-of `adddc34`) | pointer only | regenerate at round end from owning records, with tracked pointers |
| Compacted contract modules (32, RFC 0001–0011) | ✔ | ✘ | ✘ | candidate (CONFIRM-bound rev10) | none until act 1 | track under `contracts/candidates/rfcs/`; fix P-6; regenerate manifest |
| `ACTIVE-CONTRACT-MANIFEST.txt` | ✔ | ✘ | ✘ | derived (act-1 argument) | derived, not authority | track with package; regenerate after P-6 fix |
| Final acceptance record (rev10 → this round) | ✔ | ✘ | ✘ | gate definition | gate procedure once owner acts | supersede with round record, tracked |
| Confirming + §20/§13 reviews (raw) | ✔ | ✘ | ✘ | evidence | evidence, never authority | track package reviews under `candidates/`; keep raw interviews/transcripts local |
| Portable verification scripts (3) | ✔ | ✘ | ✘ | tooling | derived checks | track under `candidates/scripts/`; add repo-level checks + CI |
| Topology bundle (10 files) | ✔ | ✘ | ✘ | candidate (act 3 offered) | none until act 3 | track under `.syzygy/map/topology-candidates/`; fix retired-phrase leg; regenerate bundle digest |
| Mission Control contract (RFC-0010) | ✔ | ✘ | ✘ | candidate | none until act 1 | tracked with package; §14 review |
| Context Compiler contract (RFC-0011) + fixtures (5+3) | ✔ | ✘ | ✘ | candidate | none until act 1 | tracked with package; fix fixture defects (§15) |
| Doctrine amendment D3 (bounded missions) | ✔ | ✘ | ✘ | proposed | none until owner act 5 | track packet under `candidates/`; minimal packet per §14 |
| Term registry (draft) | ✔ | ✘ | ✘ | draft | none | finalize per §10 → `candidates/policy-candidates/TERM-REGISTRY.md` |
| Knowledge-hygiene policy draft (CC-KNOW/CC-BUDGET) | ✔ | ✘ | ✘ | draft | none until craft act | finalize per §12 → `candidates/policy-candidates/`; own craft amendment act |
| Clause migration map (04-CLAUSE-MIGRATION-MATRIX) | ✔ | ✘ | ✘ | derived accounting | derived | track with package; apply D2 accounting fixes |
| RFC/OpenSpec routing matrix (matrix-rows, 28 RFC-0006 rows) | ✔ | ✘ | ✘ | derived, partially unreviewed | derived | track; P-10 review |
| Owner-decision ledger extractions (D1 packet, OWNER-ANSWERS) | ✔ | ✘ | ✘ | recorded warrants | warrant sources | FD-037 step 1 extraction → `decisions/` |
| Front-door drafts (README/AGENTS/STATUS/CONTRIBUTING/SECURITY) | ✔ | ✘ | ✘ | draft with known defects | none | rewrite per §8 (+ delta-index fixes), fresh-reader review, install per P-11 |
| License packet | ✔ | ✘ | ✘ | decision aid | owner/legal decision (P-14) | track `decisions/LICENSE-DECISION-PACKET.md`; README carries status line |
| Craft-and-care cluster (9 files + INSTALL-RECORD) | mirror | ✔ | ✔ (banners lie) | approved (D2), CC-TEST-2 confirmation pending | authoritative (engineering bar) | P-7 banner fix, P-8 binding fix, regenerate digests, re-offer act 2 |
| Overview (`intent/OVERVIEW.md`) | mirror | ✔ | ✔ (stale gate prose) | draft offered (act 4) | presentation only, never citable as authority | §9 progressive-disclosure refactor; new digest; re-offer |
| Installed `AGENTS.md` / one-line `README.md` | — | ✔ | misleads (stale lifecycle, `about/` row, retired phrases) | stale | repo procedure | replace per §8 |
| th-engineering tier-3 baseline | mirror (optional; no longer required) | ✔ | ✔ | vendored (owner override, 2026-08-06 — supersedes this row's original "do not import") | external, pinned (`../../policies/GOVERNANCE-SUBSTRATE-LOCK.yaml`) | none — vendored at `.claude/skills/th-engineering/` + `.codex/skills/th-engineering/`, digest-pinned; P-26 executed |
| Beads DB + hooks | local DB; hooks tracked | partial | hooks visible, uninstalled; no `refs/dolt/data` on remote | process | work lifecycle only | disclose posture in AGENTS/CONTRIBUTING; no product beads |

**Principle applied (round prompt §6):** active authority and active
candidates required for current review become clone-visible; raw research,
interviews, transcripts, and detailed review history stay founder-local or
separately archived. `_bootstrap/**` remains excluded (FD-021), with
extraction-and-repoint (FD-037) as the only repair direction.
