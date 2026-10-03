#!/usr/bin/env python3
"""Measure provenance repetition and anchor resolution on two machine captures.

Read-only. Takes a captured ``GET /api/poc`` body and a captured
``GET /api/poc/polaris`` body from the same evaluation and prints the figures
the N9 amendment packages (``syzygy-u05.9``) cite:

- how many work-item and code-structure rows carry a field whose whole value
  is their block header's revision, and the bytes those fields occupy in the
  compact serialization (``,"<key>":"<value>"`` per row);
- how many anchors the machine narrative serves, whether they share one key
  set, whether each anchor's identity names its block, and whether each
  anchor's ``supports`` stay within its block's claims;
- how many anchors resolve under the amendment's predicate: the machine answer
  serves exactly one record whose own served identity equals the anchor's
  target identity. The records with a served identity today are the
  ``projectShape.sources[]`` entries (key ``identity``); every unresolved
  anchor is classed by its target identity's scheme.

    measure_machine_channel_provenance.py API_POC.json API_POC_POLARIS.json
"""

from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import sys


def row_repeats(rows: list[dict], key: str, header_value: str) -> dict:
    equal = sum(1 for row in rows if row.get(key) == header_value)
    per_row = len(json.dumps({key: header_value}, separators=(",", ":"))) - 2 + 1
    return {
        "rows": len(rows),
        "rowsCarryingHeaderValue": equal,
        "bytesPerRow": per_row,
        "bytes": equal * per_row,
    }


def measure(api_poc: pathlib.Path, api_polaris: pathlib.Path) -> dict:
    poc_bytes, polaris_bytes = api_poc.read_bytes(), api_polaris.read_bytes()
    poc, polaris = json.loads(poc_bytes), json.loads(polaris_bytes)
    work = row_repeats(poc["workItems"]["items"], "doltRevision", poc["workItems"]["doltRevision"])
    code = row_repeats(poc["codeStructure"]["files"], "revision", poc["codeStructure"]["revision"])
    repeated = work["bytes"] + code["bytes"]

    blocks = polaris["narrative"]["blocks"]
    anchors = [(block, anchor) for block in blocks for anchor in block["anchors"]]
    key_sets = collections.Counter(tuple(sorted(anchor)) for _, anchor in anchors)
    identities = collections.Counter(
        source["identity"] for source in poc["projectShape"]["sources"] if "identity" in source
    )
    resolved, unresolved = 0, collections.Counter()
    for _, anchor in anchors:
        hits = identities.get(anchor["targetId"], 0)
        if hits == 1:
            resolved += 1
        else:
            unresolved[f"{anchor['targetClass']}:{anchor['targetId'].split(':', 1)[0]}:{hits}"] += 1
    return {
        "capture": {
            "apiPoc": {"bytes": len(poc_bytes), "sha256": hashlib.sha256(poc_bytes).hexdigest()},
            "apiPocPolaris": {"bytes": len(polaris_bytes), "sha256": hashlib.sha256(polaris_bytes).hexdigest()},
        },
        "rowRepetition": {
            "workItems.doltRevision": work,
            "codeStructure.revision": code,
            "totalBytes": repeated,
            "fractionOfApiPoc": round(repeated / len(poc_bytes), 5),
        },
        "narrative": {
            "blocks": len(blocks),
            "blocksCitableFalse": sum(1 for block in blocks if block.get("citable") is False),
            "blocksWithAnchors": sum(1 for block in blocks if block["anchors"]),
            "anchorCount": len(anchors),
            "distinctAnchorIds": len({anchor["anchorId"] for _, anchor in anchors}),
            "anchorKeySets": {",".join(keys): count for keys, count in key_sets.items()},
            "anchorIdNamesItsBlock": sum(
                1 for block, anchor in anchors if anchor["anchorId"].startswith(block["blockId"] + "#")
            ),
            "anchorSupportsWithinBlockClaims": sum(
                1 for block, anchor in anchors if set(anchor["supports"]) <= set(block["claims"])
            ),
            "distinctTargetIds": len({anchor["targetId"] for _, anchor in anchors}),
        },
        "resolution": {
            "predicate": "exactly one projectShape.sources[] record whose served identity equals the anchor's targetId",
            "servedIdentities": sum(identities.values()),
            "resolved": resolved,
            "total": len(anchors),
            "unresolvedByClassSchemeAndHits": dict(sorted(unresolved.items())),
        },
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[-1].strip())
        return 2
    print(json.dumps(measure(pathlib.Path(argv[0]), pathlib.Path(argv[1])), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
