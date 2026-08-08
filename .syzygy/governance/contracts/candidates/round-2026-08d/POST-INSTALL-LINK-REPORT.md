# Post-install link resolution — round 2026-08d simulation

**Non-authoritative round record.** Re-runs review RD-7's install
simulation against the current bytes with the round-2026-08d ceremony —
which added `CONTEXT-BUDGET-REPORT.md` and
`03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` to the first wave act's
install-time copy — and records what resolves. Valid for the working tree
it was run in (2026-08-09, this round's uncommitted state); re-run after
any module or ceremony edit.

## Method

1. Simulated the install exactly as the acceptance record §2 step 3 now
   documents, into a scratch `.syzygy/governance/contracts/`: `rfcs/`
   (39 modules with package structure), `wave-manifests/`,
   `ACTIVE-CONTRACT-MANIFEST.txt`, companions `history/` and
   `matrix-rows/`, and the two non-normative reports named above.
   `sha256sum -c wave-manifests/WAVE-A-MANIFEST.txt` verifies from the
   install root. [Observed]
2. Swept every installed module for backtick code spans that are relative
   references — the span traverses (`../…`) or names a file
   (`*.md|txt|yaml|yml|py`) — and resolved each against the file's own
   installed location. This is RD-7's population; spans holding the
   RFC-0003 reserved-directory *vocabulary* (`map/`, `cache/`,
   `decisions/`, …) are namespace names, not references, and are excluded
   by that stated filter, not silently (112 such spans in the sweep's raw
   pass). Repo-absolute `.syzygy/**` and forward `openspec/**` references
   are CG-1b/CG-1c's population, checked there against the working tree.

## Result

**87 relative references examined; 87 resolved; 0 unresolved.** [Observed]

The eight pointers RD-7 found broken by the rev10 install — six package
READMEs and one module pointing two levels up at the two package-level
reports — resolve under the amended ceremony because the reports are now
copied to exactly the level the pointers name. The remaining four of
RD-7's twelve were vocabulary spans and forward references, outside this
population by the filter above.

## Limit

A simulation proves the *documented* ceremony closes the pointer class; it
does not prove a future edit cannot reopen it. `CG-14` still validates
install routes only — a recurring post-install link check remains the
standing recommendation from RD-7, and this report is a round record, not
that check.
