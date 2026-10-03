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
- every population in the ``/api/poc`` body where a record in a list repeats,
  under the same key and as the same whole value, a scalar field of the
  object that holds the list (the "header repeat" sweep);
- how many anchors resolve under the amendment's predicate: the machine answer
  serves exactly one record with an ``identity`` field of its own whose whole
  value equals the anchor's target identity. Every object in the body with a
  string ``identity`` field is a candidate record; reference fields such as
  ``sourceIdentity`` are not. Every unresolved anchor is classed by its target
  identity's scheme;
- a second method for the unresolved ones: whether their target identity
  occurs as a whole string value anywhere in the ``/api/poc`` body;
- whether the capability deep-dive's ``intent.leaf.identity`` equals some
  anchor's target identity.

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


def header_repeats(body: object) -> dict[str, dict[str, int]]:
    """Records in a list that repeat, by key and whole value, a scalar of the list's holder."""
    found: dict[str, dict[str, int]] = {}

    def walk(node: object, path: str) -> None:
        if isinstance(node, dict):
            scalars = {
                key: value for key, value in node.items()
                if isinstance(value, (str, int, float)) and not isinstance(value, bool)
            }
            for key, value in node.items():
                if isinstance(value, list) and value and all(isinstance(row, dict) for row in value):
                    hits = collections.Counter(
                        field for row in value for field, item in row.items()
                        if field in scalars and scalars[field] == item
                    )
                    for field in {field for row in value for field in row if field in scalars}:
                        entry = found.setdefault(f"{path}.{key}[].{field}", {"rows": 0, "repeating": 0})
                        entry["rows"] += sum(1 for row in value if field in row)
                        entry["repeating"] += hits[field]
                walk(value, f"{path}.{key}")
        elif isinstance(node, list):
            for item in node:
                walk(item, f"{path}[]")

    walk(body, "$")
    return {path: counts for path, counts in sorted(found.items()) if counts["repeating"]}


def string_values(body: object) -> collections.Counter:
    values: collections.Counter = collections.Counter()

    def walk(node: object) -> None:
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
        elif isinstance(node, str):
            values[node] += 1

    walk(body)
    return values


def own_identities(body: object) -> collections.Counter:
    """Every string `identity` field of an object, wherever it sits."""
    found: collections.Counter = collections.Counter()

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if isinstance(node.get("identity"), str):
                found[node["identity"]] += 1
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(body)
    return found


def measure(api_poc: pathlib.Path, api_polaris: pathlib.Path) -> dict:
    poc_bytes, polaris_bytes = api_poc.read_bytes(), api_polaris.read_bytes()
    poc, polaris = json.loads(poc_bytes), json.loads(polaris_bytes)
    work = row_repeats(poc["workItems"]["items"], "doltRevision", poc["workItems"]["doltRevision"])
    code = row_repeats(poc["codeStructure"]["files"], "revision", poc["codeStructure"]["revision"])
    repeated = work["bytes"] + code["bytes"]

    blocks = polaris["narrative"]["blocks"]
    anchors = [(block, anchor) for block in blocks for anchor in block["anchors"]]
    key_sets = collections.Counter(tuple(sorted(anchor)) for _, anchor in anchors)
    identities = own_identities(poc)
    from_sources = sum(1 for source in poc["projectShape"]["sources"] if isinstance(source.get("identity"), str))
    values = string_values(poc)
    resolved, unresolved, unresolved_ids = 0, collections.Counter(), []
    for _, anchor in anchors:
        hits = identities.get(anchor["targetId"], 0)
        if hits == 1:
            resolved += 1
        else:
            unresolved[f"{anchor['targetClass']}:{anchor['targetId'].split(':', 1)[0]}:{hits}"] += 1
            unresolved_ids.append(anchor["targetId"])
    target_ids = {anchor["targetId"] for _, anchor in anchors}
    leaves = [
        dive["intent"]["leaf"]["identity"] for dive in polaris["narrative"].get("deepDives", [])
        if isinstance(dive.get("intent", {}).get("leaf", {}).get("identity"), str)
    ]
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
        "headerRepeats": header_repeats(poc),
        "resolution": {
            "predicate": "exactly one object in the /api/poc body with a string `identity` field whose whole value equals the anchor's targetId",
            "servedIdentities": sum(identities.values()),
            "servedIdentitiesInProjectShapeSources": from_sources,
            "resolved": resolved,
            "total": len(anchors),
            "unresolvedByClassSchemeAndHits": dict(sorted(unresolved.items())),
            "secondMethod": {
                "predicate": "the unresolved anchor's targetId occurs as a whole string value anywhere in the /api/poc body",
                "unresolved": len(unresolved_ids),
                "occurring": sum(1 for target in unresolved_ids if values.get(target, 0) > 0),
            },
        },
        "deepDiveLeaves": {
            "count": len(leaves),
            "equalToAnAnchorTargetId": sum(1 for leaf in leaves if leaf in target_ids),
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
