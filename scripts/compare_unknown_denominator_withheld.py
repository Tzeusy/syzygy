#!/usr/bin/env python3
"""Compare, per source, the unknown-item-denominator set with the withheld set.

Reads one retained /api/poc capture (never a repository body). Identity is
sha256 of the repository-relative path, so the output carries no Butlers path.
Prints JSON; exit 0 when the sets are equal, 1 otherwise.
Usage: compare_unknown_denominator_withheld.py CAPTURE.json
"""
import hashlib
import json
import sys


def ident(path):
    return hashlib.sha256(path.encode("utf-8")).hexdigest()


def main(argv):
    raw = open(argv[1], "rb").read()
    shape = json.loads(raw)["projectShape"]
    unknown = {
        ident(s["path"]): s["record"].get("exclusion", {}).get("contentDigest")
        for s in shape["sources"]
        if s["itemDenominator"].get("kind") != "known"
    }
    withheld = {
        ident(e["repositoryRelativePath"]): e["contentDigest"]
        for e in shape["exclusions"]
    }
    out = {
        "measuredOn": {"capture": "api-poc.json", "sha256": hashlib.sha256(raw).hexdigest()},
        "identityScheme": "sha256 of the repository-relative path",
        "unknownDenominatorCount": len(unknown),
        "withheldCount": len(withheld),
        "onlyInUnknownDenominator": sorted(set(unknown) - set(withheld)),
        "onlyInWithheld": sorted(set(withheld) - set(unknown)),
        "contentDigestsEqualPerSource": unknown == withheld,
        "equal": set(unknown) == set(withheld),
        "members": [{"pathSha256": k, "contentDigest": withheld[k]} for k in sorted(withheld)],
    }
    json.dump(out, sys.stdout, indent=2)
    print()
    return 0 if out["equal"] and out["contentDigestsEqualPerSource"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
