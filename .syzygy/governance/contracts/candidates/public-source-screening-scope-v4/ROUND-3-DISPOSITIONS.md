# Round 3 classification — public-source screening scope, version 4

> **Candidate — binds nothing.** Raw: `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-3-RAW.md`,
> verdict line 5: `Verdict: REVISE`, over commit `05e76464`. One revise
> finding and two notes. Under the lead's final-cycle direction (a round-3
> REVISE goes to the owner, with no round 4) **nothing is repaired**: the
> package bytes stay as round 3 read them, carry no confirmation, and P-110
> is not offered for signature. The owner decides what happens next.
> *(Marked 2026-10-15: the owner chose one more round
> (`ROUND-3-OWNER-DIRECTION.md`); the repairs are in `ROUND-3-REPAIR.md`.
> This classification is kept as written.)*

| Finding | Severity | Classification (not repaired) |
|---|---|---|
| 1 — the round-2 repair narrowed the PEM check: `wholeArtifactLinePattern` (`^[ \t]*-{4,}[ \t]*BEGIN`) fires only when the header starts its line, where round 2's `-----BEGIN ` fragment fired anywhere; seven bodies with a key header mid-line (template literal, triple-quoted string, one-line JSON, blockquote, list bullet, no-break-space indent, after a BOM) that round 2 kept whole now keep the key body; `ROUND-2-REPAIR.md`, the delta and the packet call the change a fail-closed widening | revise | **A regression this package introduced, and a false claim about it.** The repair the raw names is small: keep the line pattern and restore an anywhere check (or drop the `^` anchor), add a mid-line fixture and a mutant, and correct the repair log, the delta and the packet. It is the owner's call whether to order that repair and a round 4 |
| 2 — "Source and configuration files are not affected" is wider than the class rule: config-shaped `.txt` files under `docs/`, `doc/` or `licenses/`, and suffix-less root files with a documentation stem, are project-documentation and get redacted | note | The class gate itself holds (no source-extension path reaches project-documentation). The sentence needs narrowing to "files outside the project-documentation class" with any repair |
| 3 — common shapes beyond the six still reach the packet from a documentation file (`postgres://` and `redis://` URLs with passwords, an `https` URL whose password contains `/`, YAML block scalars, `DB_PASS`, Markdown tables, WireGuard, PuTTY and dockerconfigjson keys); "a URL with a password in it" overstates a detector that matches `http` and `https` only | note | Covered by the packet's general cost sentence; the URL wording needs narrowing with any repair |

Owner question this leaves: decline P-110 as it stands, order the finding-1
repair and one more round, or take a narrower route (for example, the
redaction only for the root README). Recovery for the trial's README is
unchanged by any of these: its spans citing neither line 1 nor line 2, a
count that stays Unknown.
