#!/usr/bin/env python3
"""Regenerate the second Anthropic egress record (sitting row 8) from the
admission package's own template and first-version parameters.

The record is the first version's record with these differences, all derived
here and none hand-written:

  * the record version (``version`` in ``v2.json``);
  * the permitted classes gain ``project-documentation`` (RFC5-14, once the
    amendment of the rfc5-project-documentation-class package is performed);
  * the carried-content table is the one ``derive_generator_sent_text.mjs
    --table --discovery`` prints from the code at the time, so it carries the
    discovery stages and fields;
  * the record is route-neutral: it names the provider and the request and
    refers to the route only through the registered route entry. That is this
    package's own template (``templates/``, a copy of the first version's with
    the lines that name the Agent SDK route reworded) and ``fieldOverrides`` in
    ``v2.json`` (provider, retention, route context, telemetry).

Everything else (the admitted repositories, the content-class list and the
rest of the first version's parameters) is read from ``public-repo-admission/instances/egress-anthropic/params.json``
at its current bytes, so the two versions cannot drift apart silently.

  --write            regenerate the record and the manifest
  --check            fail if either differs from its regeneration
  --ready            exit 0 only when every stage in ``requiredStages`` of
                     ``v2.json`` occurs in the derived table's Stages column;
                     an empty list is NOT ready (the stage list has not been
                     delivered)
  --digests          print the record's SHA-256 (refuses while stale or not ready)
  --manifest-digest  print the SHA-256 of the manifest FILE (same refusals)
  --selftest         one mutant per predicate; each must be caught

The record is current but not ready until the discovery stage list is
delivered: ``--check`` can pass while ``--digests`` and ``--manifest-digest``
refuse, so no digest of a record that lacks the discovery stages can reach
an offering.
"""
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
PKG = CANDIDATES / "public-egress-v2"
V1 = CANDIDATES / "public-repo-admission"
MANIFEST_NAME = "PUBLIC-EGRESS-V2-MANIFEST.txt"
RECORD = "instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md"
NEW_CLASS = "project-documentation"
TEMPLATE = "EGRESS-CONSENT-TEMPLATE-V2.md"


def _v1_builder():
    spec = importlib.util.spec_from_file_location(
        "build_public_repo_admission", REPO / "scripts" / "build_public_repo_admission.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def derive_table(root=None):
    """The carried-content table with the discovery rows (``--table
    --discovery``), derived from the code at REPO. Refuses while the
    generator's code has no ``--discovery`` mode: the record is not
    producible, and so not ready, until it is on main."""
    import subprocess
    root = PKG if root is None else root
    args = settings(root).get("tableArgs", ["--table", "--discovery"])
    build = subprocess.run(["npx", "tsc", "-b", "packages/polaris-generation-core"],
                           cwd=REPO, capture_output=True, text=True)
    if build.returncode != 0:
        raise RuntimeError("cannot build polaris-generation-core: " + build.stdout[-300:])
    done = subprocess.run(["node", "scripts/derive_generator_sent_text.mjs", *args],
                          cwd=REPO, capture_output=True, text=True)
    if done.returncode != 0:
        raise RuntimeError("derivation failed (a field has no class, or the code has no "
                           "--discovery mode yet?): " + done.stderr.strip()[-400:])
    return done.stdout.strip()


def v1_fields(v1=None):
    """The first version's field values for its egress record."""
    v1 = V1 if v1 is None else v1
    spec = json.loads((v1 / "instances/egress-anthropic/params.json").read_text())
    common = spec.pop("common", {})
    [(_, entry)] = [(k, e) for k, e in spec.items() if e["template"] == "EGRESS-CONSENT-TEMPLATE.md"]
    return {**common, **entry["fields"]}, entry["template"]


def template_delta(root=None, v1=None):
    """(hunks, removed lines, added lines) of this package's template against
    the first version's. ``v2.json`` pins these counts, so an edit to the
    template that the record's description does not cover is reported by
    ``--check`` and not left to a review to notice."""
    import difflib
    root = PKG if root is None else root
    v1 = V1 if v1 is None else v1
    _, name = v1_fields(v1)
    a = (v1 / "templates" / name).read_text().splitlines()
    b = (root / "templates" / TEMPLATE).read_text().splitlines()
    hunks = removed = added = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            hunks += 1
            removed += i2 - i1
            added += j2 - j1
    return hunks, removed, added


def settings(root=None):
    root = PKG if root is None else root
    return json.loads((root / "v2.json").read_text())


def fields(root=None, v1=None, table_fn=None):
    root = PKG if root is None else root
    base, _ = v1_fields(v1)
    cfg = settings(root)
    if cfg["version"] == base["VERSION"]:
        raise ValueError("v2 version equals the first version's")
    if NEW_CLASS in base["CONTENT_CLASSES"]:
        raise ValueError("the first version already lists the class; v2 would add nothing")
    out = dict(base)
    for key, value in cfg.get("fieldOverrides", {}).items():
        if key not in base:
            raise ValueError(f"fieldOverrides names {key}, which the first version does not fill")
        out[key] = value
    out["VERSION"] = cfg["version"]
    out["CONTENT_CLASSES"] = base["CONTENT_CLASSES"] + f"\n- `{NEW_CLASS}`"
    out["SUPERSEDES"] = (f"supersedes version {base['VERSION']} of this record, if an act over that "
                         "version is in force, from the effective instant of the act on this "
                         "version (prospective, RFC5-13); with none in force it supersedes nothing")
    out["CARRIED_TABLE"] = (table_fn or derive_table)()
    return out


def record_text(root=None, v1=None, table_fn=None):
    b = _v1_builder()
    root = PKG if root is None else root
    tpl_name = TEMPLATE
    text = b.render((root / "templates" / tpl_name).read_text(), fields(root, v1, table_fn), tpl_name)
    if f"`../../templates/{tpl_name}`" not in text:
        raise ValueError("instance header does not name the template as expected")
    return text.replace("`scripts/build_public_repo_admission.py`", "`scripts/build_public_egress_v2.py`", 1)


def stages_in(table):
    """Stage names named by the table's Stages column; ``all`` is not a name."""
    found = set()
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in ("Where", "---"):
            found.update(t.strip() for t in cells[2].split(",") if t.strip() != "all")
    return found


def readiness(root=None, table=None):
    """(ready, reasons): the delivered stage list must all occur in the table."""
    root = PKG if root is None else root
    req = settings(root).get("requiredStages", [])
    if not req:
        return False, ["requiredStages is empty: the discovery stage list has not been delivered"]
    have = stages_in(table if table is not None else derive_table())
    missing = [s for s in req if s not in have]
    return (not missing), [f"stage {s!r} does not occur in the derived table" for s in missing]


def manifest_text(root=None, v1=None, table_fn=None):
    root = PKG if root is None else root
    sha = hashlib.sha256(record_text(root, v1, table_fn).encode()).hexdigest()
    path = (root / RECORD).as_posix()
    return ("# PUBLIC EGRESS V2 MANIFEST\n"
            "# Candidate; this file and its row bind nothing by themselves.\n"
            "# 1 record; the row hashes the record's exact bytes and is the argument of one\n"
            "# owner act over that record (sitting row 8). It depends on row 7.\n"
            f"{sha}  {path}\n")


def stale(root=None, v1=None, table_fn=None):
    root = PKG if root is None else root
    bad = []
    rec = root / RECORD
    if not rec.exists() or rec.read_text() != record_text(root, v1, table_fn):
        bad.append(rec)
    for extra in sorted((root / "instances").rglob("*.md")):
        if extra != rec:
            bad.append(extra)
    pinned = settings(root).get("templateDelta")
    tpl = root / "templates" / TEMPLATE
    if pinned is None or [pinned["hunks"], pinned["removedLines"], pinned["addedLines"]] != list(template_delta(root, v1)):
        bad.append(tpl)
    man = root / MANIFEST_NAME
    if not man.exists() or man.read_text() != manifest_text(root, v1, table_fn):
        bad.append(man)
    return bad


def selftest():
    import contextlib
    import io
    import subprocess
    import tempfile
    caught = 0
    table = ("| Where | Field | Stages | Class |\n|---|---|---|---|\n"
             "| envelope | `system` | all | instruction-text |\n"
             "| inputs | `sources` | inventory, author | target-content |\n"
             "| inputs | `map` | map, reduce | composite |")
    assert stages_in(table) == {"inventory", "author", "map", "reduce"}
    with tempfile.TemporaryDirectory() as d:
        base = pathlib.Path(d)
        v1 = base / "v1"
        (v1 / "templates").mkdir(parents=True)
        (v1 / "instances/egress-anthropic").mkdir(parents=True)
        (v1 / "instances/egress-anthropic/params.json").write_text(json.dumps({
            "E.md": {"template": "EGRESS-CONSENT-TEMPLATE.md", "fields": {
                "PROVIDER": "P", "CONTENT_CLASSES": "- `code-content`", "SUPERSEDES": "none"}},
            "common": {"VERSION": "0.1.0-candidate.7"}}))
        root = base / "v2"
        (root / "instances/egress-anthropic").mkdir(parents=True)
        (root / "templates").mkdir()
        base_tpl = "# E {{PROVIDER}}\n\n> Template. x\n\nv `{{VERSION}}`\n{{CONTENT_CLASSES}}\n{{SUPERSEDES}}\n{{CARRIED_TABLE}}\n"
        (v1 / "templates").mkdir(exist_ok=True)
        (v1 / "templates/EGRESS-CONSENT-TEMPLATE.md").write_text(base_tpl)
        (root / "templates" / TEMPLATE).write_text(base_tpl + "extra line\n")
        assert template_delta(root, v1) == (1, 0, 1)

        def setup(cfg):
            cfg = {**cfg, "templateDelta": {"hunks": 1, "removedLines": 0, "addedLines": 1}}
            (root / "v2.json").write_text(json.dumps(cfg))
            (root / RECORD).write_text(record_text(root, v1, lambda: table))
            (root / MANIFEST_NAME).write_text(manifest_text(root, v1, lambda: table))

        def expect(exc, fn, why):
            try:
                fn()
            except exc:
                return 1
            raise AssertionError(why)

        setup({"version": "0.2.0-candidate.1", "requiredStages": ["map", "reduce"]})
        text = (root / RECORD).read_text()
        assert stale(root, v1, lambda: table) == []
        assert "`code-content`" in text and f"`{NEW_CLASS}`" in text and "0.2.0-candidate.1" in text
        assert "0.1.0-candidate.7 of this record" in text and f"`../../templates/{TEMPLATE}`" in text
        caught += 1  # positive render: class appended, version set, supersession names v1
        (root / RECORD).write_text(text + "x")
        assert stale(root, v1, lambda: table) == [root / RECORD], "stale record not caught"
        caught += 1
        (root / RECORD).write_text(text)
        assert stale(root, v1, lambda: table + "\n| inputs | `y` | map | composite |") == [root / RECORD, root / MANIFEST_NAME], \
            "a table that differs from a fresh derivation not caught"
        caught += 1
        (root / MANIFEST_NAME).write_text(manifest_text(root, v1, lambda: table).replace("1 record", "2 records"))
        assert stale(root, v1, lambda: table) == [root / MANIFEST_NAME], "stale manifest not caught"
        caught += 1
        (root / MANIFEST_NAME).write_text(manifest_text(root, v1, lambda: table))
        orphan = root / "instances/egress-anthropic/ORPHAN.md"
        orphan.write_text("x")
        assert orphan in stale(root, v1, lambda: table), "orphan record not caught"
        orphan.unlink()
        caught += 1
        assert readiness(root, table) == (True, [])
        caught += 1
        # not ready: empty list, and a stage the table lacks, and a substring that is not a stage
        for cfg, why in (({"version": "0.2.0-candidate.1", "requiredStages": []}, "empty stage list"),
                         ({"version": "0.2.0-candidate.1", "requiredStages": ["map", "rank"]}, "absent stage"),
                         ({"version": "0.2.0-candidate.1", "requiredStages": ["inv"]}, "substring of a stage")):
            (root / "v2.json").write_text(json.dumps(cfg))
            ok, reasons = readiness(root, table)
            assert not ok and reasons, f"{why} counted as ready"
            caught += 1
        (root / "v2.json").write_text(json.dumps({"version": "0.2.0-candidate.1", "requiredStages": ["all"]}))
        assert not readiness(root, table)[0], "'all' counted as a stage name"
        caught += 1
        # refusals: same version as v1; class already present in v1; placeholder left
        caught += expect(ValueError, lambda: fields(
            root=_with(root, {"version": "0.1.0-candidate.7", "requiredStages": ["map"]}), v1=v1, table_fn=lambda: table),
            "same version not refused")
        params = v1 / "instances/egress-anthropic/params.json"
        saved = params.read_text()
        params.write_text(saved.replace("- `code-content`", f"- `code-content`\\n- `{NEW_CLASS}`"))
        caught += expect(ValueError, lambda: fields(
            root=_with(root, {"version": "0.2.0-candidate.1", "requiredStages": ["map"]}), v1=v1, table_fn=lambda: table),
            "class already in v1 not refused")
        params.write_text(saved)
        caught += expect(ValueError, lambda: record_text(
            _with(root, {"version": "0.2.0-candidate.1", "requiredStages": ["map"]}), v1, lambda: "{{LEFT}}"),
            "placeholder left after fill not caught")
        text0 = record_text(root, v1, lambda: table)
        over = _with(root, {"version": "0.2.0-candidate.1", "requiredStages": ["map"],
                            "fieldOverrides": {"PROVIDER": "Q-route-neutral"}})
        assert "Q-route-neutral" in record_text(over, v1, lambda: table) and "Q-route-neutral" not in text0
        caught += 1  # an override reaches the record
        caught += expect(ValueError, lambda: fields(
            root=_with(root, {"version": "0.2.0-candidate.1", "requiredStages": ["map"],
                              "fieldOverrides": {"NOT_A_FIELD": "x"}}), v1=v1, table_fn=lambda: table),
            "an override of a field the first version does not fill not refused")
        # the template's delta against the first version's is pinned
        setup({"version": "0.2.0-candidate.1", "requiredStages": ["map", "reduce"]})
        assert stale(root, v1, lambda: table) == []
        saved_tpl = (root / "templates" / TEMPLATE).read_text()
        (root / "templates" / TEMPLATE).write_text(saved_tpl + "second extra line\n")
        assert (root / "templates" / TEMPLATE) in stale(root, v1, lambda: table), "template drift not caught"
        (root / "templates" / TEMPLATE).write_text(saved_tpl)
        pinned_cfg = json.loads((root / "v2.json").read_text())
        (root / "v2.json").write_text(json.dumps({k: v for k, v in pinned_cfg.items() if k != "templateDelta"}))
        assert (root / "templates" / TEMPLATE) in stale(root, v1, lambda: table), "unpinned template delta not caught"
        (root / "v2.json").write_text(json.dumps(pinned_cfg))
        caught += 2
        # the derivation refuses a reader-question leaf it has no class for
        mutant = REPO / "scripts" / "_derive_mutant_v2.mjs"
        try:
            src = (REPO / "scripts" / "derive_generator_sent_text.mjs").read_text()
            frag = "const READER_QUESTION_LEAVES = ['id', 'topics', 'text'];"
            assert frag in src
            mutant.write_text(src.replace(frag, "const READER_QUESTION_LEAVES = ['id', 'topics'];", 1))
            done = subprocess.run(["node", str(mutant), "--table"], cwd=REPO, capture_output=True, text=True)
            assert done.returncode == 2 and "readerQuestions[] leaf text" in done.stderr, "reader-question leaf not refused"
            caught += 1
        finally:
            mutant.unlink(missing_ok=True)
        # digest modes refuse while not ready, silently on stdout
        global PKG, V1
        saved_pkg, saved_v1 = PKG, V1
        PKG, V1 = root, v1
        real_table = derive_table
        globals()["derive_table"] = lambda: table
        try:
            (root / "v2.json").write_text(json.dumps({"version": "0.2.0-candidate.1", "requiredStages": [], "templateDelta": {"hunks": 1, "removedLines": 0, "addedLines": 1}}))
            (root / RECORD).write_text(record_text(root, v1, lambda: table))
            (root / MANIFEST_NAME).write_text(manifest_text(root, v1, lambda: table))
            for mode in ("--digests", "--manifest-digest"):
                out = io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                    rc = main(["x", mode])
                assert rc == 1 and out.getvalue() == "", f"{mode} did not refuse while not ready"
                caught += 1
            (root / "v2.json").write_text(json.dumps({"version": "0.2.0-candidate.1", "requiredStages": ["map"], "templateDelta": {"hunks": 1, "removedLines": 0, "addedLines": 1}}))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                assert main(["x", "--manifest-digest"]) == 0 and re.fullmatch(r"[0-9a-f]{64}\n", out.getvalue())
            caught += 1
            assert main(["x", "--bogus"]) == 2
            caught += 1
        finally:
            PKG, V1 = saved_pkg, saved_v1
            globals()["derive_table"] = real_table
    print(f"selftest: {caught} checks held")


def _with(root, cfg):
    """A sibling root whose v2.json is cfg (only v2.json is read by fields())."""
    alt = root.parent / ("alt-" + hashlib.sha256(json.dumps(cfg).encode()).hexdigest()[:8])
    alt.mkdir(exist_ok=True)
    (alt / "v2.json").write_text(json.dumps(cfg))
    if not (alt / "templates").exists():
        (alt / "templates").symlink_to(root / "templates")
    return alt


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--write", "--check", "--ready", "--digests", "--manifest-digest", "--selftest"):
        print(f"unknown mode {mode}", file=sys.stderr)
        return 2
    if mode == "--selftest":
        selftest()
        return 0
    table = derive_table()
    if mode == "--ready":
        ok, reasons = readiness(table=table)
        for r in reasons:
            print("NOT READY:", r)
        print("public egress v2:", "ready" if ok else "not ready")
        return 0 if ok else 1
    if mode == "--write":
        (PKG / RECORD).write_text(record_text(table_fn=lambda: table))
        (PKG / MANIFEST_NAME).write_text(manifest_text(table_fn=lambda: table))
        return 0
    bad = stale(table_fn=lambda: table)
    if mode == "--check":
        for path in bad:
            print(f"STALE {path}")
        print("public egress v2:", "STALE" if bad else "current")
        return 1 if bad else 0
    ok, reasons = readiness(table=table)
    if bad or not ok:
        print("refusing: " + ("stale; run --check" if bad else "; ".join(reasons)), file=sys.stderr)
        return 1
    if mode == "--manifest-digest":
        print(hashlib.sha256((PKG / MANIFEST_NAME).read_bytes()).hexdigest())
    else:
        print(hashlib.sha256((PKG / RECORD).read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
