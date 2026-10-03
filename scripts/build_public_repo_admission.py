#!/usr/bin/env python3
"""Regenerate public-repository admission instances from their templates.

Each instance directory under the package's ``instances/`` holds a
``params.json`` naming, per output record, its template and field values
(plus a ``common`` block). The template's leading "> Template." blockquote is
replaced by an instance header; every ``{{FIELD}}`` must be filled.

  --write     regenerate every instance record
  --check     fail if any instance record differs from its regeneration,
              or an instance directory holds a record nothing produces
  --digests   print each instance record's SHA-256 (refuses while stale)
  --manifest-digest
              print the SHA-256 of the manifest FILE (refuses while stale)

``--write`` also writes ``PUBLIC-REPO-ADMISSION-MANIFEST.txt``: one row per
instance record, ``<sha256>  <repo-relative path>``, sorted by path. Each row
is the argument of one separate owner act over that record (Q5); no row binds
another. ``--check`` also fails when the manifest differs from its
regeneration.
  --selftest  build one mutant per predicate; each must be caught
"""
import hashlib
import json
import pathlib
import re
import sys

PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-repo-admission")
MANIFEST_NAME = "PUBLIC-REPO-ADMISSION-MANIFEST.txt"
FIELD = re.compile(r"\{\{([A-Z_]+)\}\}")
HEADER = re.compile(r"\A(# [^\n]*\n\n)(?:> [^\n]*\n)+")


def render(template_text, fields, template_name):
    def sub(m):
        if m.group(1) not in fields:
            raise KeyError(f"{template_name}: unfilled field {m.group(1)}")
        return fields[m.group(1)]
    head = (f"> Instance filled from `../../templates/{template_name}` by\n"
            "> `scripts/build_public_repo_admission.py`. Candidate — binds nothing\n"
            "> until the owner acts on this record's exact bytes.\n")
    text, n = HEADER.subn(lambda m: m.group(1) + head, template_text, count=1)
    if n != 1:
        raise ValueError(f"{template_name}: template header not found")
    out = FIELD.sub(sub, text)
    if "{{" in out:
        raise ValueError(f"{template_name}: placeholder left after fill")
    return out


def instances(root=PKG):
    for params in sorted((root / "instances").glob("*/params.json")):
        spec = json.loads(params.read_text())
        common = spec.pop("common", {})
        for out_name, entry in spec.items():
            tpl = root / "templates" / entry["template"]
            fields = {**common, **entry["fields"]}
            yield params.parent / out_name, render(tpl.read_text(), fields, entry["template"])


def manifest_text(root=PKG):
    rows = sorted((path.as_posix(), hashlib.sha256(text.encode()).hexdigest())
                  for path, text in instances(root))
    return ("# PUBLIC REPOSITORY ADMISSION MANIFEST\n"
            "# Candidate; this file and its rows bind nothing by themselves.\n"
            f"# {len(rows)} records; rows sorted by codepoint path; each row hashes the\n"
            "# record's exact bytes and is the argument of one separate owner act over\n"
            "# that record. Each row requires its own act; no row binds another.\n"
            + "".join(f"{sha}  {path}\n" for path, sha in rows))


def selftest():
    """Each predicate is shown to fire on a mutant built for it."""
    import tempfile
    tpl = "# T {{A}}\n\n> Template. x\n> y\n\nv {{B}}\n"
    good = render(tpl, {"A": "1", "B": "2"}, "t")
    caught = 0
    # banner replaced: the template's own banner must not survive
    assert "> Template." not in good and "> Instance filled" in good
    caught += 1
    # unfilled field
    try:
        render(tpl, {"A": "1"}, "t")
        raise AssertionError("unfilled field not caught")
    except KeyError:
        caught += 1
    # placeholder smuggled in through a field value
    try:
        render(tpl, {"A": "1", "B": "{{C}}"}, "t")
        raise AssertionError("placeholder left after fill not caught")
    except ValueError:
        caught += 1
    # missing banner
    try:
        render("# T\n\nno header\n", {}, "t")
        raise AssertionError("missing header not caught")
    except ValueError:
        caught += 1
    # staleness: a one-byte edit to a regenerated instance must be reported
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "templates").mkdir()
        (root / "instances" / "x").mkdir(parents=True)
        (root / "templates" / "T.md").write_text(tpl)
        (root / "instances" / "x" / "params.json").write_text(json.dumps(
            {"R.md": {"template": "T.md", "fields": {"A": "1", "B": "2"}}}))
        [(path, text)] = list(instances(root))
        path.write_text(text)
        (root / MANIFEST_NAME).write_text(manifest_text(root))
        assert stale(root) == []
        path.write_text(text + "x")
        assert stale(root) == [path], "stale instance not caught"
        caught += 1
        path.write_text(text)
        orphan = path.parent / "ORPHAN.md"
        orphan.write_text("x")
        assert stale(root) == [orphan], "orphan record not caught"
        caught += 1
        orphan.unlink()
        (root / MANIFEST_NAME).write_text(manifest_text(root).replace("1", "2", 1))
        assert stale(root) == [root / MANIFEST_NAME], "stale manifest not caught"
        caught += 1
        (root / MANIFEST_NAME).write_text(manifest_text(root))
        assert stale(root) == []
    print(f"selftest: {caught} of 7 mutants caught (banner kept, unfilled "
          "field, placeholder in value, missing banner, stale instance, "
          "orphan record, stale manifest)")


def stale(root=PKG):
    """Records that differ from their regeneration, plus orphan records: a
    ``.md`` file in an instance directory that no ``params.json`` produces."""
    produced = dict(instances(root))
    bad = [p for p, text in produced.items()
           if not p.exists() or p.read_text() != text]
    for d in {p.parent for p in produced}:
        bad += sorted(p for p in d.glob("*.md") if p not in produced)
    manifest = root / MANIFEST_NAME
    if not manifest.exists() or manifest.read_text() != manifest_text(root):
        bad.append(manifest)
    return bad


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--write", "--check", "--digests", "--manifest-digest",
                    "--selftest"):
        print(f"unknown mode {mode}", file=sys.stderr)
        return 2
    if mode == "--selftest":
        selftest()
        return 0
    if mode == "--check":
        bad = stale()
        for path in bad:
            print(f"STALE {path}")
        print("public-repo admission instances:", "STALE" if bad else "current")
        return 1 if bad else 0
    if mode == "--manifest-digest":
        if stale():
            print("refusing: instances or manifest are stale; run --check",
                  file=sys.stderr)
            return 1
        print(hashlib.sha256((PKG / MANIFEST_NAME).read_bytes()).hexdigest())
        return 0
    if mode == "--digests" and stale():
        print("refusing: instances are stale; run --check", file=sys.stderr)
        return 1
    for path, text in instances():
        if mode == "--write":
            path.write_text(text)
        print(f"{hashlib.sha256(text.encode()).hexdigest()}  {path}")
    if mode == "--write":
        (PKG / MANIFEST_NAME).write_text(manifest_text())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
