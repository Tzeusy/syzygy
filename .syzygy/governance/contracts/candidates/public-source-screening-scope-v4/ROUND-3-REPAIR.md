# Round 3 repair — public-source screening scope, version 4

> **Candidate — binds nothing.** Repairs for
> `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-3-RAW.md` (verdict line 5:
> `Verdict: REVISE`), first classified in `ROUND-3-DISPOSITIONS.md`, made
> 2026-10-15 on the owner's direction (`ROUND-3-OWNER-DIRECTION.md`).

| Finding | Severity | Repair |
|---|---|---|
| 1 — the line pattern fired only at line start; a mid-line key header kept its key body | revise | `wholeArtifactFragments` again holds `-----BEGIN `, plus `---- BEGIN ` for RFC 4716, compared exactly anywhere in the body; the line pattern stays, and either check excludes the body whole. Fixtures "mid-line header in a template literal", "mid-line header in one-line JSON", "mid-line header in a list bullet"; predicates "a dropped anywhere header fragment caught", "a dropped anywhere RFC 4716 fragment caught", and a fixture-flip mutant showing the template-literal body is redacted without the anywhere check. `ROUND-2-REPAIR.md`'s "widened" claim and the delta's round-2 banner are marked false where they stand; the delta and packet now describe both checks and what neither catches |
| 2 — "Source and configuration files are not affected" overclaims | note | The delta and packet now say a configuration-shaped file the path rules class as documentation (a `.txt` under `docs/`, `doc/` or `licenses/`, a suffix-less root documentation stem) is redacted like documentation |
| 3 — more shapes reach the packet; the URL detector reads `http`/`https` only | note | The delta and packet say the URL detector matches `http://` and `https://` only and name `postgres://`, `mysql://`, `redis://`, `mongodb://` and `amqp://` connection strings, and an `https` password containing `/`, as reaching the packet from a documentation file |

Verification: builder `--write`, `--check` passes, `--selftest` holds 43 of
43 predicates.
