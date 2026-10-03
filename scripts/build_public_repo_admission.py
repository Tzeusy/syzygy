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

A template that holds ``{{CARRIED_TABLE}}`` gets, as that field, the table
printed by ``scripts/derive_generator_sent_text.mjs --table`` (after building
``packages/polaris-generation-core``). The table is therefore GENERATED from
the code: a field with no class makes the derivation fail, and ``--check``
reports the record stale when its table differs from a fresh derivation.
"""
import functools
import hashlib
import json
import pathlib
import re
import subprocess
import sys

PKG = pathlib.Path(".syzygy/governance/contracts/candidates/public-repo-admission")
MANIFEST_NAME = "PUBLIC-REPO-ADMISSION-MANIFEST.txt"
FIELD = re.compile(r"\{\{([A-Z_]+)\}\}")
HEADER = re.compile(r"\A(# [^\n]*\n\n)(?:> [^\n]*\n)+")


REPO = pathlib.Path(__file__).resolve().parents[1]


@functools.lru_cache(maxsize=None)
def derive_table():
    """The carried-content table, derived from the generator's code."""
    build = subprocess.run(["npx", "tsc", "-b", "packages/polaris-generation-core"],
                           cwd=REPO, capture_output=True, text=True)
    if build.returncode != 0:
        raise RuntimeError("cannot build polaris-generation-core: " + build.stdout[-300:])
    done = subprocess.run(["node", "scripts/derive_generator_sent_text.mjs", "--table"],
                          cwd=REPO, capture_output=True, text=True)
    if done.returncode != 0:
        raise RuntimeError("derivation failed (a field has no class?): " + done.stderr.strip()[-400:])
    return done.stdout.strip()


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


def instances(root=None):
    root = PKG if root is None else root
    for params in sorted((root / "instances").glob("*/params.json")):
        spec = json.loads(params.read_text())
        common = spec.pop("common", {})
        for out_name, entry in spec.items():
            tpl = root / "templates" / entry["template"]
            fields = {**common, **entry["fields"]}
            if "{{CARRIED_TABLE}}" in tpl.read_text():
                fields["CARRIED_TABLE"] = derive_table()
            yield params.parent / out_name, render(tpl.read_text(), fields, entry["template"])


def manifest_text(root=None):
    root = PKG if root is None else root
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
        lone = root / "instances" / "nop"
        lone.mkdir()
        (lone / "REC.md").write_text("x")
        assert stale(root) == [lone / "REC.md"], "record in a directory with no params.json not caught"
        caught += 1
        (lone / "REC.md").unlink()
        lone.rmdir()
        lines = manifest_text(root).splitlines(True)
        row = next(i for i, l in enumerate(lines) if re.match(r"[0-9a-f]{64}  ", l))
        lines[row] = ("0" if lines[row][0] != "0" else "1") + lines[row][1:]
        (root / MANIFEST_NAME).write_text("".join(lines))
        assert stale(root) == [root / MANIFEST_NAME], "stale manifest not caught"
        caught += 1
        (root / MANIFEST_NAME).write_text(manifest_text(root))
        assert stale(root) == []
    # the carried-content table is generated: a different derivation is stale,
    # and a field with no class makes the derivation itself fail
    global derive_table
    real = derive_table
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "templates").mkdir()
        (root / "instances" / "x").mkdir(parents=True)
        (root / "templates" / "T.md").write_text("# T\n\n> Template. x\n\n{{CARRIED_TABLE}}\n")
        (root / "instances" / "x" / "params.json").write_text(json.dumps(
            {"R.md": {"template": "T.md", "fields": {}}}))
        try:
            derive_table = lambda: "| a |"
            [(path, text)] = list(instances(root))
            path.write_text(text)
            (root / MANIFEST_NAME).write_text(manifest_text(root))
            assert stale(root) == []
            derive_table = lambda: "| a |\n| b |"
            assert path in stale(root), "a table that differs from a fresh derivation not caught"
            caught += 1
        finally:
            derive_table = real
    mutant = REPO / "scripts" / "_derive_mutant.mjs"
    try:
        src = (REPO / "scripts" / "derive_generator_sent_text.mjs").read_text()
        assert "requestedAssets: 'run-profile'," in src
        mutant.write_text(src.replace("requestedAssets: 'run-profile',", "", 1))
        done = subprocess.run(["node", str(mutant), "--table"], cwd=REPO, capture_output=True, text=True)
        assert done.returncode == 2 and "requestedAssets" in done.stderr, "unclassified field not caught"
        caught += 1
    finally:
        mutant.unlink(missing_ok=True)
    # call-site forms the derivation must refuse, never drop (round-7 note 1)
    real = (REPO / "packages/polaris-generation-core/src/pipeline.ts").read_text()
    plan_call = next(l for l in real.splitlines() if "stage('plan'," in l)
    author_call = next(l for l in real.splitlines() if "stage('author'," in l)
    mutants = {
        "a stage called through a variable": real.replace(
            plan_call, "    const planInputs = { sources: sourcePopulation, operatorNote: frozen.requestId };\n"
            "    context.plan = await stage('plan', planInputs);", 1),
        "a stage named by a template string": real.replace("stage('plan',", "stage(`plan`,", 1)
            .replace("await stage(`plan`, {", "await stage(`plan`, { ...context,", 1),
        "a double-quoted stage with a new key": real.replace(
            author_call, author_call.replace("stage('author', {", 'stage("author", { projectId: frozen.projectId,', 1), 1),
    }
    with tempfile.TemporaryDirectory() as d:
        for name, text in mutants.items():
            assert text != real, f"mutant {name} did not change the source"
            copy = pathlib.Path(d) / "pipeline.ts"
            copy.write_text(text)
            done = subprocess.run(["node", "scripts/derive_generator_sent_text.mjs", "--table", "--pipeline", str(copy)],
                                  cwd=REPO, capture_output=True, text=True)
            assert done.returncode == 2 and done.stdout == "", f"{name}: derivation did not refuse (exit {done.returncode})"
            caught += 1
    # refusals while stale: both digest modes exit 1 and print nothing on stdout
    global PKG
    saved = PKG
    with tempfile.TemporaryDirectory() as d:
        PKG = pathlib.Path(d)
        (PKG / "templates").mkdir()
        (PKG / "instances" / "x").mkdir(parents=True)
        (PKG / "templates" / "T.md").write_text(tpl)
        (PKG / "instances" / "x" / "params.json").write_text(json.dumps(
            {"R.md": {"template": "T.md", "fields": {"A": "1", "B": "2"}}}))
        try:
            import contextlib, io
            for mode in ("--digests", "--manifest-digest"):
                out = io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                    rc = main(["x", mode])
                assert rc == 1 and out.getvalue() == "", f"{mode} did not refuse silently on stdout while stale"
                caught += 1
            assert main(["x", "--bogus"]) == 2, "unknown mode not refused"
            caught += 1
        finally:
            PKG = saved
    print(f"selftest: {caught} of 16 checks held: one positive render check "
          "(banner replaced) and fifteen mutants: unfilled field, placeholder in value, "
          "missing banner, stale instance, orphan record, record in a "
          "directory with no params.json, stale manifest, refusals of "
          "--digests and --manifest-digest while stale, unknown mode, a carried-content"
          " table that differs from a fresh derivation, a field with no class, and three call-site forms the"
          " derivation refuses: a variable, a template string, a double-quoted stage with a new key")


def stale(root=None):
    """Records that differ from their regeneration, plus orphan records: a
    ``.md`` file in an instance directory that no ``params.json`` produces."""
    root = PKG if root is None else root
    produced = dict(instances(root))
    bad = [p for p, text in produced.items()
           if not p.exists() or p.read_text() != text]
    for d in sorted({p.parent for p in produced}
                    | {d for d in (root / "instances").glob("*") if d.is_dir()}):
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
