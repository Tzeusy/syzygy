> **Candidate — binds nothing.** The review instruction for a drafted
> contract successor. It performs no act and authorizes no implementation.

# Review brief — RFC-0007 scoped-values amendment

Review the exact candidate commit and manifest without authoring context. The
proposed bytes are `proposed/RFC-0007/rendering-and-surface.md.patch` over the
current module; nothing under `contracts/rfcs/` changes on the reviewed commit.
Verify by running, this session: `python3 scripts/build_rfc7_scoped_values_successor.py --check`
and `--selftest`, `python3 scripts/record_rfc7_scoped_values_successor.py --selftest`,
and `python3 scripts/check_governance.py` (0 FAIL).

Required baseline: `VIS-1`, `VIS-2`, `VIS-4`, `VIS-7`; `CC-REV-2`, `CC-REV-4`,
`CC-REV-6`; `RFC7-33`, `RFC7-34`, `RFC7-16` in
`.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`;
`RFC6-13`, `RFC6-14`; the lane B package
`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`
(its `SEMANTIC-DELTA.md` and contract patch), whose step 1 this is.

Criteria:

1. **Interactive surface only.** The interactive surface is defined by
   delivery. No reading lets a scope replace a unit's own attribute on the
   machine-queryable endpoints, on any plain-text or exported rendering, or
   in any copy, share or export function the surface offers.
2. **Non-citability stands, and the builder knows it.** `non-citable` /
   `presentation-artifact` cannot be carried by a scope; the sub-clause below
   the new paragraph is intact; the builder's exclusion predicate fails when
   either is removed.
3. **One value only.** A scope carries the evaluation identity and nothing
   else, is valid only when every claim under it would carry that identity,
   never overrides a claim's own, states its content as text on its own
   element, and is expanded before parity comparison. Try to construct a
   reading that hides a distinction from a reader or an agent.
4. **Nothing else moves.** The diff changes exactly the one parenthetical and
   the one paragraph; clause leads, front matter and headings are unchanged;
   both mirrors take identical bytes; the manifest row hashes the patched bytes.
5. **Agreement with lane B.** The package patch and the lane B contract patch
   compose to identical module bytes, and the lane B behavior delta relies on
   no permission this paragraph does not give.
6. **No act, no authority.** The packet offers nothing, the recorder is
   unpinned, no chain link is registered, and no implementation is authorized.

## Raw review head contract

Write the raw to `docs/reviews/` with a basename ending `-RAW.md`. Its first
four non-blank lines, with no blank line after the title, are:

```
# Review — <title>
Reviewed commit: <full 40-character sha>
Manifest SHA-256: <sha256 of CONTRACT-AMENDMENT-MANIFEST.txt, the file>
Verdict: <exactly CONFIRM, CONFIRM WITH EXCEPTIONS or REVISE>
```

The `Manifest SHA-256` line carries the act argument itself: the digest of the
manifest *file*, not of its row. Number findings continuously from 1 under a
`## Findings` heading as `**Finding N — <title>** (blocking|revise|note)`.
