<!-- Extracted under FD-037 on 2026-08-05 from _bootstrap/rfc-phase/DOCTRINE-AMENDMENT-MAP-HISTORICAL.md.
     From extraction onward, this tracked copy is the citable required source.
     Content below this header is byte-verbatim from the original. -->

# Doctrine Amendment Packet — `map/` includes historical state

> **Status:** Proposal — binds nothing until the owner adopts it. Prepared
> 2026-07-30 during the foundational-RFC phase, per the phase directive's
> lean-surface-charter instruction ("If adopting this charter would amend
> doctrine, draft a minimal doctrine amendment packet. Do not silently modify
> adopted doctrine.").

## What and why

The owner-ratified surface charter (SURFACE-DECISION-RECORD.md §2) defines
Orrery as a spatial model of "observed, intended, proposed **and historical**
project state." Adopted doctrine defines `map/` as covering "observed,
intended, and proposed system state" — historical rendering is nowhere
promised, although observation records and milestones already exist as
doctrine objects. This is the single word of doctrine text the charter
implies. Everything else in the charter is decision-layer or RFC material.

## Exact amendment (two sites in `.syzygy/governance/doctrine/architecture.md`)

1. Layout comment (line ~54–55):
   - From: `# semantic/spatial representation of observed, intended,` /
     `#   and proposed system state`
   - To: `# semantic/spatial representation of observed, intended,` /
     `#   proposed, and historical system state`
2. Definition bullet (line ~272–273):
   - From: "the semantic/spatial representation of observed, intended, and
     proposed system state, including the spatial view (UI codename Orrery)."
   - To: "the semantic/spatial representation of observed, intended,
     proposed, and historical system state, including the spatial view
     (UI codename Orrery)."

No other doctrine text changes. Historical *mechanics* (which evaluations are
renderable, retention, scenario selection) are RFC 0009 material, not
doctrine.

## Blast radius

- Consistent with the temporal model already in doctrine (immutable
  observation records; evaluation identity) — this names a rendering promise
  over records that already exist; it creates no new store and no new
  authority.
- No conflict found in the other five doctrine files (checked: vision.md
  three-state thesis; trust-and-evidence.md evidence rules; v1.md scope —
  historical rendering carries no V0/V1 scope claim by itself).

## Adoption

Owner adopts by stating clearly (no magic phrase required for amendments;
adoption authority: VIS-4). On adoption: apply the two edits, one commit
(`doctrine: amend map/ definition to include historical state`), note the
amendment in the adoption record. Amended rule text changes in place; nothing
is renumbered.
