#!/usr/bin/env python3
"""Regenerate public-repository admission instances from their templates.

Each instance directory under the package's ``instances/`` holds a
``params.json`` naming, per output record, its template and field values
(plus a ``common`` block). The template's leading "> Template." blockquote is
replaced by an instance header; every ``{{FIELD}}`` must be filled.

  --write     regenerate every instance record
  --check     fail if any instance record differs from its regeneration
  --digests   print each instance record's SHA-256 (the act argument)
  --selftest  mutate a field and an unfilled placeholder; both must be caught
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
    tpl = "# T {{A}}\n\n> Template. x\n> y\n\nv {{B}}\n"
    assert render(tpl, {"A": "1", "B": "2"}, "t").endswith("v 2\n")
    for bad in ({"A": "1"},):
        try:
            render(tpl, bad, "t")
        except KeyError:
            continue
        raise AssertionError("unfilled field not caught")
    try:
        render("# T\n\nno header\n", {}, "t")
    except ValueError:
        pass
    else:
        raise AssertionError("missing header not caught")
    print("selftest: fill case passes; 2 of 2 mutants caught (unfilled field, missing header)")


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        selftest()
        return 0
    bad = 0
    for path, text in instances():
        if mode == "--write":
            path.write_text(text)
        elif mode == "--check":
            if not path.exists() or path.read_text() != text:
                print(f"STALE {path}")
                bad += 1
        if mode in ("--write", "--digests"):
            print(f"{hashlib.sha256(text.encode()).hexdigest()}  {path}")
    if mode == "--check":
        print("public-repo admission instances:", "STALE" if bad else "current")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
