"""syzygy-bpyt.4.2, acceptance criterion 1: what `npm run build` emits, before and after, file by file.

`python3 compare_emit.py <base root> <base commit> <head root> <head commit>` prints one JSON record over every `.js` file under
each tree's `apps/*/dist` and `packages/*/dist`. Each root is a checkout built with `npm run build` from nothing (every dist
removed first); the commits are labels the caller vouches for. The record counts each tree's files and tests (`*.test.js`), lists
every file on one side only and every common file whose bytes differ, and digests each tree (path and bytes of every file)."""
import hashlib, json, os, sys

base, base_commit, head, head_commit = sys.argv[1:5]


def emitted(root):
    out = {}
    for parent in ("packages", "apps"):
        for name in sorted(os.listdir(os.path.join(root, parent))):
            for directory, _, files in os.walk(os.path.join(root, parent, name, "dist")):
                for file in files:
                    if file.endswith(".js"):
                        path = os.path.join(directory, file)
                        out[os.path.relpath(path, root)] = open(path, "rb").read()
    return out


def tree(files, commit):
    return {"commit": commit, "files": len(files), "tests": sum(path.endswith(".test.js") for path in files),
            "sha256": hashlib.sha256(b"".join(p.encode() + b"\0" + files[p] for p in sorted(files))).hexdigest()}


a, b = emitted(base), emitted(head)
common = sorted(set(a) & set(b))
print(json.dumps({
    "subject": "the JavaScript `npm run build` emits under apps/*/dist and packages/*/dist",
    "base": tree(a, base_commit), "head": tree(b, head_commit), "common": len(common),
    "byteIdentical": sum(a[p] == b[p] for p in common), "differ": [p for p in common if a[p] != b[p]],
    "onlyInBaseTests": sum(p.endswith(".test.js") for p in set(a) - set(b)),
    "onlyInBaseOther": sorted(p for p in set(a) - set(b) if not p.endswith(".test.js")),
    "onlyInHead": sorted(set(b) - set(a)),
}, indent=1))
