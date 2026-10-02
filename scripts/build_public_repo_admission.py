#!/usr/bin/env python3
"""Regenerate public-repository admission instances from their templates.

Each instance directory under the package's ``instances/`` holds a
``params.json`` naming, per output record, its template and field values
(plus a ``common`` block). The template's leading "> Template." blockquote is
replaced by an instance header; every ``{{FIELD}}`` must be filled.

  --write     regenerate every instance record
  --check     fail if any instance record differs from its regeneration
  --digests   print each instance record's SHA-256 (the act argument)
  --selftest  build one mutant per predicate; each must be caught
"""
import hashlib
import json
import pathlib
import re
import sys

PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-repo-admission")
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
        assert stale(root) == []
        path.write_text(text + "x")
        assert stale(root) == [path], "stale instance not caught"
        caught += 1
    print(f"selftest: {caught} of 5 mutants caught (banner kept, unfilled "
          "field, placeholder in value, missing banner, stale instance)")


def stale(root=PKG):
    return [p for p, text in instances(root)
            if not p.exists() or p.read_text() != text]


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--write", "--check", "--digests", "--selftest"):
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
    for path, text in instances():
        if mode == "--write":
            path.write_text(text)
        print(f"{hashlib.sha256(text.encode()).hexdigest()}  {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
