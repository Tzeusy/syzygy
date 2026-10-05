# Impact ledger — Polaris dossier local-agent mode

> **Candidate — binds nothing.** Review material for
> `SEMANTIC-DELTA.md`. Not an authority or an adopted applicability judgment.

## Method

[Observed] Sweeps ran by script over `git ls-tree -r -z --name-only` at
commit `ac35c998ec3f7b20c47adc19b22ac540f851b099` (`origin/main` when this
change was branched), so neither of this change's two directories is in the
population. Denominator (rule 9): 2,328 tracked paths, of which 4 do not
decode as UTF-8 and were skipped, so 2,324 were searched. Python `re`, never
`grep` (verification rule 1). The affected identifiers are
REQ-polaris-generation-001, 005, 006, 017, 018, 030 and 031, written `NNN`
below. The regexes, case-sensitive, with run form:

| Sweep | Regex (Python) | Notes |
|---|---|---|
| A: the identifier | `REQ-polaris-generation-NNN\b` | one pattern per identifier |
| B: continuation form | `REQ-polaris-generation-(?:\d{3}\s*(?:/\|,\|, and\| and\|\.\.\|–)\s*)+(\d{3})`; every three-digit number in the match, the first included, is tested against the seven | catches `REQ-polaris-generation-005/017` and `…-001, 030 and 031` |
| E: prose short form | `\b[Rr]equirements? ((?:\d{3}(?:,\| and\|,? and\| to)\s*)*\d{3})\b`; every number in group 1 | unqualified, so it also matches other specifications' requirement numbers (see class 8) |
| F: title form | the exact requirement titles: `Admitted project input`, `Explicit bounded generation`, `Independent review and repair`, `Registered adapter boundaries`, `Complete execution history`, `Accounted unfamiliar-project discovery`, `Consequential owner clarification` | |
| G: range form | `(?:REQ-polaris-generation-\|[Rr]equirements? )(\d{3})\s*(?:\.\.\.?\|–\|—\|-\| to \| through )\s*(?:REQ-polaris-generation-)?(\d{3})\b`, keeping an identifier `NNN` when first < NNN ≤ second | |
| I: interfaces | `INTERFACES\.md\|maxUsageUnits\|agent-selected spending` | the displaced `INTERFACES.md` text and its budget field |

Files per identifier in any of A, B, E, F or G: 001: 48; 005: 26; 006: 52;
017: 39; 018: 17; 030: 25; 031: 19. The union over all six sweeps (A to G
and I) is **135 files**: 104 from A to G, and 31 more from I alone.

## Classification of the 135 files

Classes were assigned by path rule, in the order listed (the first rule that
matches wins), then every file in classes 3, 4, 7 and 8 was read at its hit.

| Class | Rule | Files | Treatment |
|---|---|---|---|
| 1 Retained raw review | path ends `-RAW.md` | 22 | Never edited (CC-REV-6). They review the provider-mode text, which is unchanged. |
| 2 Evidence or pursuit record | under `docs/evidence/` or `docs/pursuits/` | 26 | Historical evidence of provider-mode work; not edited, still accurate for its subject. |
| 3 Adopted or act-bound governed file | the base and overlay changes, `decisions/`, the three generator readability and union successor packages | 21 | Not edited; any edit retires an act. The new requirements displace text per run mode instead. |
| 4 Sibling candidate package | other `contracts/candidates/**`, and the profile change | 31 | Not edited; see "Sibling candidates" below. |
| 5 Implementation | `packages/`, `apps/`, `scripts/` | 26 | Provider-mode code and its tests cite the requirements; unchanged. New code waits for sign-off (direction item 5). |
| 6 Design history | `docs/design/` | 5 | Historical; not edited. |
| 7 Live presentation doc | `docs/polaris-generation/` | 3 | Updated in the adoption change, not before (`README.md`, `TARGETS.md`, `REDIS-DOSSIER-GAP-ANALYSIS.md`). `REDIS-SITTING-RUNBOOK.md` does not match any sweep but describes the provider sitting and is updated at the same time. |
| 8 Other | none of the above | 1 | `openspec/changes/project-registration-and-honest-shape-visibility/specs/project-registration-and-honest-shape-visibility/spec.md`: a false positive of sweep E (its own "requirements 001", "requirement 030"), not a citer. |

22 + 26 + 21 + 31 + 26 + 5 + 3 + 1 = 135.

### Adopted files that describe the provider mode in prose (class 3)

`ADAPTER-DECLARATIONS.md`, `SCHEMA-CONTRACT.md`, `EXECUTION-PHASES.md`,
`DESIGN-ACCEPTANCE.md` and `design.md` of the base change describe the
provider adapter, stage schema and run envelope. They are design, not
requirement text, and they stay true of the provider mode. The one design
sentence this change reads differently for the operator-agent mode, the
`INTERFACES.md` Provider bullet and budget paragraph, is quoted in the
semantic delta. A reviewer who finds another design sentence that an
operator-agent run would contradict should report it as a finding.

## Sibling candidates (class 4)

- **`non-governed-narrative-profile/` and its change (REQ-032).** Composition,
  not authorship. No overlap: 032 says how a non-governed narrative is
  composed; this change says who writes it and how it is checked. Both name
  REQ-polaris-generation-001 and 030 as parents. A Redis dossier needs both.
- **`polaris-edit-repair-deletion-scenario/`.** Appends one sentence and one
  scenario to the overlay's REQ-polaris-generation-006. Every 006 fragment
  this change quotes survives its patch unchanged [Observed, by reading the
  patch]. If adopted, its block-accounting rule applies to the agent's
  resubmissions [Inferred]; `syzygy dossier check` would compute the block
  account between revisions.
- **`doctrine-amendment-inferred-first-class-d8/`.** A candidate doctrine
  amendment about the Inferred label; it cites REQ-polaris-generation-031.
  This change labels the agent's claims Inferred under today's doctrine; if
  D8 is adopted, the labelling rules of 034 are re-read against it.
- **`public-repo-admission/`, `public-egress-v2/`,
  `public-admission-registry-entries/`, `provider-route-messages-api-entry/`.**
  The provider-mode route, egress and adapter packages. Parked by direction
  item 4: not offered, not deleted, not edited. The observation-consent and
  public-source-acquisition parts that this mode still needs are named in
  `design.md` (`init`).

## Derived artifacts

`DIRECTIVE-REGISTER.md`, `PROJECT-STATUS.md`'s effective counts and the
generated dependency union regenerate after adoption, never before
(CC-KNOW-11); `tasks.md` lists them.

## Limits of this ledger

- A citation wrapped across a line break is invisible to every sweep above
  (AGENTS.md, governance prose notes); not measured here.
- Sweep E's false-positive rate outside Polaris is not measured beyond class 8.
- No target repository content was read.
