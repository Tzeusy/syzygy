# Raw review — Polaris SVG graph diagrams feature candidate

Reviewed commit: `6e2c183744cecb3dcc1072f7a0a633a6ddc0aa83`

Reviewed artifact SHA-256:
`ecabd87459a317ab9ad24fe88fe60281775194388571d7f1958bd1add0fb07da`

Verdict: REVISE

## Review scope and commands

- Exact reviewed head was clean on branch `agent/syzygy-dov.16.5`.
- The reviewed change added one file only:
  `docs/design/POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE.md`.
- `git diff --check
  44c51b54054b7181e63f71917380faaa302a2df2..6e2c183744cecb3dcc1072f7a0a633a6ddc0aa83`
  passed.
- `python3 scripts/check_governance.py` passed with
  `32 OK, 20 WARN, 0 FAIL (52 checks)`.

## Findings

### F1 — Blocking: typed-relation identity is conflated with relationship-instance identity

Candidate lines 88 and 122–134 conflate `RFC1-25(d)` typed-relation identity
(relation name plus ordered endpoint-domain pair) with edge-instance identity.
That causes lawful chain, fan-in, and fan-out instances of the same typed
relation to collide or be refused.

Distinguish all three concepts:

1. model relationship-instance identity, which owns graph membership and the
   rendered edge key;
2. typed-relation class, which is the relation name plus ordered endpoint-domain
   pair under `RFC1-25(d)`; and
3. presentation label, which is never identity.

Add a fixture with at least two edge instances of the same typed relation and
require both to survive SVG rendering, text rendering, and parity comparison.

### F2 — Blocking: hierarchy has two unreconciled truth carriers

The node's `parentIdentity` and the edge's `hierarchy: true` are independent
truth carriers for the same relationship. Choose one authority and derive the
other, or require exact bidirectional equality. Add mutations for disagreement,
a missing parent, and a node incorrectly treated as a root.

### F3 — Medium: additive diagram budgets cannot bound always-complete text

The 24 KiB per-figure and 96 KiB aggregate hard limits cannot bound the text
rendering while also requiring that text to remain always complete. Split:

1. the additive SVG-and-legend byte budget;
2. the always-complete text population, which density limits may never
   truncate; and
3. the authoritative whole-response ceiling, whose breach serves nothing.

The density fixture must measure each population before and after SVG fallback.

## Confirmed strengths

- OWNER HOLD and non-binding scope are explicit.
- Identity and layout are separated.
- Cycles, self-loops, parallel edges, provenance, and role fixtures are named.
- The SVG is inert, `aria-hidden`, and link-free, with complete semantic HTML.
- Keyboard, no-JS, reflow, contrast, and motion constraints are present.
- The literal-fence boundary is distinguished from the future offset-stitch
  replacement.
- The reviewed change added one design file only; it changed no code,
  specification, or governed bytes.
- Governance validation was green at the reviewed commit.

## Verdict basis

The feature boundary, accessibility posture, and owner hold are sound, but the
two identity defects can reject lawful graphs or let hierarchy disagree with
itself. The budget defect makes the stated fail-closed behavior internally
inconsistent. Those issues require semantic repair before confirmation.
