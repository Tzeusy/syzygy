# Historical archive index — where history lives, and what it may be used for

**Derived index (2026-08-05).** History is retained without bound but is
never on a default reading path and never authority (hygiene principle;
doctrine VIS-3 protects active artifacts from historical accretion).

| Archive | Location | Clone-visible? | Contents | May be cited as |
|---|---|---|---|---|
| Bootstrap process record | `_bootstrap/**` (git-excluded; FD-021, made durable in versioned `.gitignore` 2026-08-04) | **No — founder-local** | Prompt pack, interviews, drafts, review transcripts, state files, superseded acceptance records (rev7–rev9), worker reports | Unavailable history only. Anything the tracked tree must *rely on* is extracted under FD-037 with a provenance header, then cited at its tracked home |
| Candidate-package history | `.syzygy/governance/contracts/candidates/history/` | Yes | Rev9 RFC corpus (9 files) + per-RFC amendment/review history (Tier-2 extracts, 27,521 words) | Non-normative rationale backlinks from the 32 active modules ("Nothing in this directory binds") |
| Candidate-package reviews | `.syzygy/governance/contracts/candidates/reviews/` | Yes | Rev10 review battery raw reports + dispositions, confirming review | Evidence about the package's review state; never edited, never authority |
| Round process records | `.syzygy/governance/contracts/candidates/round-2026-08/` | Yes | This round's preflight, matrices, semantic deltas, review raws, reports, process lessons | Round provenance; superseded by owner-act records once acts fire |
| Superseded craft install digests | `INSTALL-RECORD.md` historical block | Yes | Install-time sha256 set | Historical provenance of D2 |
| Prior front door | git history of `README.md` / `AGENTS.md` | Yes (`git log`) | One-line README; bootstrap-era AGENTS.md | History only |
| Bootstrap-phase craft copy | `_bootstrap/rfc-phase/craft-and-care/` | No | The D2-approved bytes with their historical banner | Review evidence (referenced by INSTALL-RECORD provenance) |

**Rules of use:** a fresh clone must never *need* a non-clone-visible
archive to understand any active artifact (self-containment test E of the
round charter). Active artifacts cite archives for provenance, not meaning.
When history must become load-bearing, it is extracted into a tracked home
with a provenance header (FD-037 pattern) — the archive itself stays where
it is.
