#!/usr/bin/env python3
"""Regenerate and verify the records of the local-agent dossier sitting.

Package `contracts/candidates/dossier-local-agent-acts/`. Each instance
directory under `instances/` holds a `params.json` naming, per output record,
its template and field values (plus a `common` block), as
`build_public_repo_admission.py` does. A record whose entry lists `bound`
files gets, as `{{BOUND_FILES}}`, a table of each file's whole-file SHA-256
computed from the current bytes, so a later edit to a bound file makes the
record stale here and its act's argument stale with it.

`DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt` has one row per instance record,
each the argument of one separate owner act over that record (no row binds
another), and one row for the proposed local-agent source-acquisition entry
of `public-git-source-acquisition-local-agent/`, which is no act's argument:
it is there so the one sitting review, whose head binds this manifest FILE,
also binds the entry the owner may sign off by version tag.

  --write            regenerate every instance record and the manifest
  --check            fail if a record or the manifest differs from its
                     regeneration, an instance directory holds a record
                     nothing produces, or a package Markdown file outside
                     `instances/` carries a 64-hex token
  --digests          print each manifest row (refuses while stale)
  --manifest-digest  print the SHA-256 of the manifest FILE (refuses while stale)
  --selftest         one mutant per predicate; each must be caught
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
PKG = CANDIDATES / "dossier-local-agent-acts"
MANIFEST_NAME = "DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt"
REGISTRY_ENTRY = (CANDIDATES / "public-git-source-acquisition-local-agent/proposed/"
                  "POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json")
FIELD = re.compile(r"\{\{([A-Z_]+)\}\}")
HEADER = re.compile(r"\A(# [^\n]*\n\n)(?:> [^\n]*\n)+")
HEX64 = re.compile(r"[0-9a-f]{64}")
DISPOSITIONS = re.compile(r"^ROUND-\d+-DISPOSITIONS\.md$")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bound_table(root: pathlib.Path, paths: list[str]) -> str:
    rows = []
    for rel in paths:
        file = root / rel
        if not file.is_file():
            raise ValueError(f"bound file {rel} is missing")
        rows.append(f"| `{rel}` | `{sha(file.read_bytes())}` |")
    return "| File | SHA-256 |\n|---|---|\n" + "\n".join(rows)


def render(template_text: str, fields: dict, template_name: str) -> str:
    def sub(m):
        if m.group(1) not in fields:
            raise KeyError(f"{template_name}: unfilled field {m.group(1)}")
        return fields[m.group(1)]
    head = (f"> Instance filled from `../../templates/{template_name}` by\n"
            "> `scripts/build_dossier_local_agent_acts.py`. Candidate — binds nothing\n"
            "> until the owner acts on this record's exact bytes.\n")
    text, n = HEADER.subn(lambda m: m.group(1) + head, template_text, count=1)
    if n != 1:
        raise ValueError(f"{template_name}: template header not found")
    out = FIELD.sub(sub, text)
    if "{{" in out:
        raise ValueError(f"{template_name}: placeholder left after fill")
    return out


def instances(root: pathlib.Path = ROOT):
    """(repo-relative path, text) for every record the params produce."""
    for params in sorted((root / PKG / "instances").glob("*/params.json")):
        spec = json.loads(params.read_text(encoding="utf-8"))
        common = spec.pop("common", {})
        for out_name, entry in sorted(spec.items()):
            tpl = root / PKG / "templates" / entry["template"]
            fields = {**common, **entry["fields"]}
            if "bound" in entry:
                fields["BOUND_FILES"] = bound_table(root, entry["bound"])
            rel = params.parent.relative_to(root) / out_name
            yield rel, render(tpl.read_text(encoding="utf-8"), fields, entry["template"])


def manifest_text(root: pathlib.Path = ROOT) -> str:
    rows = [(rel.as_posix(), sha(text.encode())) for rel, text in instances(root)]
    entry = root / REGISTRY_ENTRY
    if not entry.is_file():
        raise ValueError(f"{REGISTRY_ENTRY.as_posix()} is missing")
    rows.append((REGISTRY_ENTRY.as_posix(), sha(entry.read_bytes())))
    rows.sort()
    return ("# DOSSIER LOCAL-AGENT SITTING MANIFEST\n"
            "# Candidate; this file and its rows bind nothing by themselves.\n"
            f"# {len(rows)} rows sorted by codepoint path; each hashes the file's exact bytes.\n"
            "# Each row under instances/ is the argument of one separate owner act over\n"
            "# that record; no row binds another. The proposed registry-entry row is no\n"
            "# act's argument: the owner may sign that entry off by version tag, and the\n"
            "# row binds the sitting review to its bytes.\n"
            + "".join(f"{s}  {p}\n" for p, s in rows))


def stale(root: pathlib.Path = ROOT) -> list[str]:
    out = []
    try:
        produced = dict(instances(root))
        manifest = manifest_text(root)
    except (ValueError, KeyError, OSError) as exc:
        return [f"cannot regenerate: {exc}"]
    for rel, text in produced.items():
        file = root / rel
        if not file.is_file() or file.read_text(encoding="utf-8") != text:
            out.append(f"{rel.as_posix()}: differs from its regeneration")
    for md in sorted((root / PKG / "instances").glob("*/*.md")):
        if md.relative_to(root) not in produced:
            out.append(f"{md.relative_to(root).as_posix()}: produced by no params entry")
    m = root / PKG / MANIFEST_NAME
    if not m.is_file() or m.read_text(encoding="utf-8") != manifest:
        out.append(f"{MANIFEST_NAME}: stale or missing")
    for md in sorted((root / PKG).glob("*.md")):
        if not DISPOSITIONS.match(md.name) and HEX64.search(md.read_text(encoding="utf-8")):
            out.append(f"{md.name}: carries a 64-hex token")
    return out


def write(root: pathlib.Path = ROOT) -> None:
    for rel, text in instances(root):
        (root / rel).write_text(text, encoding="utf-8")
    (root / PKG / MANIFEST_NAME).write_text(manifest_text(root), encoding="utf-8")


# --- selftest ---------------------------------------------------------------

def _fixture(tmp: pathlib.Path) -> pathlib.Path:
    shutil.copytree(ROOT / PKG, tmp / PKG, ignore=shutil.ignore_patterns("reviews"))
    bound = set()
    for params in (ROOT / PKG / "instances").glob("*/params.json"):
        for name, entry in json.loads(params.read_text()).items():
            if name != "common":
                bound.update(entry.get("bound", []))
    for rel in (*sorted(bound), REGISTRY_ENTRY.as_posix()):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, tmp / rel)
    write(tmp)
    return tmp


def selftest() -> int:
    results: list[tuple[str, bool]] = []

    def caught(name, mutate, needle):
        with tempfile.TemporaryDirectory() as t:
            tmp = _fixture(pathlib.Path(t))
            mutate(tmp)
            found = stale(tmp)
            results.append((name, any(needle in f for f in found)))

    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        results.append(("a regenerated package verifies", stale(tmp) == []))
        rows = re.findall(r"^[0-9a-f]{64}  (\S+)$", manifest_text(tmp), re.MULTILINE)
        produced = sorted(p.as_posix() for p, _t in instances(tmp))
        results.append(("the manifest rows every record and the registry entry, once each",
                        rows == sorted(produced + [REGISTRY_ENTRY.as_posix()])
                        and len(rows) == len(set(rows))))
        d9 = (tmp / PKG / "instances/in-force/D9-IN-FORCE-RECORD.md").read_text()
        want = sha((tmp / ".syzygy/governance/doctrine/security.md").read_bytes())
        results.append(("the D9 record carries security.md's live digest", want in d9))

    def edit_bound(tmp):
        p = tmp / ".syzygy/governance/doctrine/v1.md"
        p.write_text(p.read_text() + "\nedit\n")
    caught("an edit to a bound doctrine file stales the D9 record", edit_bound,
           "D9-IN-FORCE-RECORD.md: differs")

    def edit_direction(tmp):
        p = tmp / ".syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md"
        p.write_text(p.read_text() + "\nedit\n")
    caught("an edit to the rulings direction stales the RFC7-20 record", edit_direction,
           "RFC7-20-READING-IN-FORCE-RECORD.md: differs")

    def edit_record(tmp):
        p = tmp / PKG / "instances/redis/NO-EVIDENCE-DRAWER-STATEMENT.md"
        p.write_text(p.read_text().replace("no kernel evidence drawer", "a drawer"))
    caught("a hand edit to a record refused", edit_record, "NO-EVIDENCE-DRAWER-STATEMENT.md: differs")

    def orphan(tmp):
        (tmp / PKG / "instances/redis/EXTRA.md").write_text("x\n")
    caught("an orphan record refused", orphan, "produced by no params entry")

    def edit_entry(tmp):
        (tmp / REGISTRY_ENTRY).write_text((tmp / REGISTRY_ENTRY).read_text() + " ")
    caught("an edit to the registry entry stales the manifest", edit_entry, "stale or missing")

    def digest_in_packet(tmp):
        (tmp / PKG / "OWNER-SITTING-PACKET.md").write_text("argument " + "a" * 64 + "\n")
    caught("a digest in a package Markdown file refused", digest_in_packet, "64-hex")

    def unfilled(tmp):
        p = tmp / PKG / "templates/AGENT-PROVIDER-STATEMENT-TEMPLATE.md"
        p.write_text(p.read_text() + "\n{{NOT_A_FIELD}}\n")
    caught("an unfilled field refused", unfilled, "unfilled field NOT_A_FIELD")

    def missing_bound(tmp):
        (tmp / ".syzygy/governance/doctrine/security.md").unlink()
    caught("a missing bound file refused", missing_bound, "bound file")
    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        (tmp / PKG / "ROUND-1-DISPOSITIONS.md").write_text("a" * 64 + "\n")
        results.append(("a disposition record may quote a digest", stale(tmp) == []))
    failed = [n for n, ok in results if not ok]
    for name, ok in results:
        print(("ok   " if ok else "FAIL ") + name)
    print(f"selftest: {len(results) - len(failed)} of {len(results)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    flags = {"--write", "--check", "--digests", "--manifest-digest", "--selftest"}
    if len(argv) != 1 or argv[0] not in flags:
        print(__doc__)
        return 2
    mode = argv[0]
    if mode == "--selftest":
        return selftest()
    if mode == "--write":
        write(ROOT)
        print(f"wrote the instance records and {MANIFEST_NAME}")
        return 0
    problems = stale(ROOT)
    if problems:
        for p in problems:
            print(f"FAIL {p}")
        return 1
    if mode == "--digests":
        print(manifest_text(ROOT).split("\n", 7)[-1], end="")
    elif mode == "--manifest-digest":
        print(sha((ROOT / PKG / MANIFEST_NAME).read_bytes()))
    else:
        print("dossier-local-agent-acts: records and manifest current")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
