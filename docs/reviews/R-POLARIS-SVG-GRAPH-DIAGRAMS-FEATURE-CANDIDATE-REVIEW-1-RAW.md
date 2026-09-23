REVISE

Tested commit: `6e2c183744cecb3dcc1072f7a0a633a6ddc0aa83`

## Findings

### Finding 1 — Blocking: typed-relation identity is conflated with edge-instance identity

`docs/design/POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE.md:88,122-134` says each edge’s `identity` is the RFC1-25(d) typed-relation identity, derives `edgeKey` from only `graphKey` plus that identity, and rejects duplicate relation identities.

RFC1-25(d), at `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md:584-630`, defines a typed-relation identity for each `(relation name, ordered endpoint-domain pair)`—the relation type, not each graph-edge instance. Multiple edge instances may lawfully reference the same typed relation. The current model separately supplies an edge-instance `PocRelationship.id`, `kind`, `from`, and `to` at `packages/three-surface-poc-core/src/model.ts:76-84`.

As written, a valid chain, fan-in, or fan-out containing multiple instances of one typed relation either collides on `edgeKey` or is refused as a duplicate. This contradicts the feature’s central graph population and makes the `chain` and `diamond` fixtures insufficiently specified.

Repair by distinguishing:

- the existing model relationship-instance identity used for membership, uniqueness, and `edgeKey`;
- the RFC1-25(d) typed-relation identifier/class referenced by that instance; and
- the presentation label.

Add a fixture with at least two different edge instances of the same typed relation and require both to survive independently in SVG, text, and parity output.

### Finding 2 — Blocking: hierarchy has two un-reconciled truth carriers

The node contract carries `parentIdentity` at candidate lines `98-112`, while the edge contract independently marks a relation `hierarchy: true` at `118-130`. Roots are said to derive from “the parent relation” at `82-90`, but the document never declares which representation owns parenthood or requires the two representations to agree.

The validator at `132-134` rejects two parents but does not reject:

- a node’s `parentIdentity` disagreeing with its hierarchy edge;
- a parent named in only one representation; or
- roots derived differently from the two representations.

The deterministic-layout pipeline at `157-166` therefore has no unique hierarchy input. The oracle’s separate parent-map and edge-set comparisons at `363-370` do not define the missing coherence rule.

Use one authoritative input representation and derive the other, or require exact bidirectional equality and add mismatch/missing-parent mutations. Until then, hierarchy and layout determinism are ambiguous under VIS-1 and RFC6-22.

### Finding 3 — Medium: byte “hard limits” cannot enforce their stated populations

The 24 KiB figure limit at candidate lines `329-330` explicitly includes “SVG, legend, and complete text,” but its failure behavior is “Figure renders text only.” The complete text can itself exceed 24 KiB because provenance/anchor populations are not byte-bounded. The 96 KiB aggregate row has the same problem: replacing later SVGs with complete text does not ensure the aggregate encoded diagram bytes fall below 96 KiB.

This makes the limits non-falsifiable as hard output ceilings and conflicts with review criterion 6 at `464`. Separate:

- an additive SVG/legend byte budget that decides whether SVG is emitted;
- the always-complete text population; and
- the existing whole-response ceiling, which remains authoritative.

The density-boundary fixture should independently exercise each population and record measured bytes before and after fallback.

## Confirmed aspects

- `OWNER HOLD` and non-binding design-only posture are explicit at lines `3-10`, with no implementation warrant.
- P-83 Q5 authorizes design only; the candidate preserves the feature-request re-entry boundary.
- Layout coordinates remain presentation state and do not enter identity.
- Directed cycles, self-loops, parallel relations, node non-duplication, roles, epistemic tuples, and provenance are otherwise carried into explicit fixtures and an independent oracle.
- The SVG is inert, `aria-hidden`, has zero focusable descendants, contains no links or URLs, and is paired with an always-visible complete semantic HTML rendering.
- Keyboard, visible focus, no-JS behavior, 200% resizing, 400% zoom/320 px reflow, contrast measurement, reduced motion, and non-interactive fallback are expressly required.
- The literal-fence section accurately distinguishes the current literal fence parser from the character-offset stitch in `polaris-reading.ts:107-113`.
- No implementation, OpenSpec, doctrine, registry, act, or other governed artifact changed; the commit adds only this design candidate.

## Commands and results

- Bootstrap: clean `agent/syzygy-dov.16.5`, exact HEAD `6e2c183744cecb3dcc1072f7a0a633a6ddc0aa83`, common directory `/home/tze/GitHub/syzygy/.git`.
- `git diff-tree --no-commit-id --name-status -r HEAD`: one added design document only.
- `git diff HEAD^ HEAD --check`: exit 0.
- `python3 scripts/check_governance.py`: 1,402 tracked files examined; `32 OK, 20 WARN, 0 FAIL`. Warnings are disclosed repository-wide/advisory checks, not candidate failures.
- Final worktree status remained clean at the tested commit.

## PR readiness

Not ready. Repair all three findings and obtain fresh independent design/accessibility review of the exact corrected head. The candidate remains an inert owner-held design document; no implementation or specification work is authorized.
