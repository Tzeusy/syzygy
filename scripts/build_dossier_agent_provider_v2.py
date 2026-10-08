#!/usr/bin/env python3
"""Regenerate and verify the agent-provider statement successor package.

Package `contracts/candidates/dossier-agent-provider-v2/`. Version 1 of each
agent-provider statement lives in `dossier-local-agent-acts/` and was drafted
before RFC5-14 had the class `project-documentation`, so it does not list it.
This package holds version 2 of the one statement an act binds today (Redis,
Claude Code with Anthropic): the same record, the same Record ID, with
`project-documentation` added to its classes, a new draft date and version, and
a supersession of version 1. Nothing else may differ, and `--check` proves it
by deriving the expected bytes from the version-1 file on disk.

It lives in its own package because the version-1 recorder freezes every file
of `dossier-local-agent-acts/` (`record_dossier_local_agent_acts.py`), so a new
file there would break the recorder of an act already performed. The manifest
has one row, the argument of one new owner act over this record.

  --write            regenerate the instance record and the manifest
  --check            fail if the record or the manifest differs from its
                     regeneration, the record differs from its predecessor
                     beyond the declared lines, an instance directory holds a
                     record nothing produces, or a package Markdown file at
                     any depth outside `instances/` and `reviews/` (round
                     dispositions excepted) carries a 64-hex token
  --digests          print the manifest row (refuses while stale)
  --manifest-digest  print the SHA-256 of the manifest FILE (refuses while stale)
  --selftest         one mutant per predicate; each must be caught

Review-head contract for a recorder written after the review: the raw's first
four non-blank lines carry `Reviewed commit: <40 hex>`, `Manifest SHA-256:
<SHA-256 of the manifest FILE>` and a `Verdict:` line.
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
PKG = CANDIDATES / "dossier-agent-provider-v2"
MANIFEST_NAME = "DOSSIER-AGENT-PROVIDER-V2-MANIFEST.txt"
FIELD = re.compile(r"\{\{([A-Z_]+)\}\}")
HEADER = re.compile(r"\A(# [^\n]*\n\n)(?:> [^\n]*\n)+")
HEX64 = re.compile(r"[0-9a-f]{64}")
DISPOSITIONS = re.compile(r"^ROUND-\d+-DISPOSITIONS\.md$")
ADDED_CLASS = "project-documentation"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def header(template_name: str) -> str:
    return (f"> Instance filled from `../../templates/{template_name}` by\n"
            "> `scripts/build_dossier_agent_provider_v2.py`. Candidate — binds nothing\n"
            "> until the owner acts on this record's exact bytes.\n")


def render(template_text: str, fields: dict, template_name: str) -> str:
    def sub(m):
        if m.group(1) not in fields:
            raise KeyError(f"{template_name}: unfilled field {m.group(1)}")
        return fields[m.group(1)]
    text, n = HEADER.subn(lambda m: m.group(1) + header(template_name), template_text, count=1)
    if n != 1:
        raise ValueError(f"{template_name}: template header not found")
    out = FIELD.sub(sub, text)
    if "{{" in out:
        raise ValueError(f"{template_name}: placeholder left after fill")
    return out


def specs(root: pathlib.Path = ROOT):
    """(repo-relative path, template name, fields, predecessor path) for every record the params declare."""
    for params in sorted((root / PKG / "instances").glob("*/params.json")):
        spec = json.loads(params.read_text(encoding="utf-8"))
        common = spec.pop("common", {})
        for out_name, entry in sorted(spec.items()):
            yield (params.parent.relative_to(root) / out_name, entry["template"], {**common, **entry["fields"]},
                   entry["predecessor"])


def instances(root: pathlib.Path = ROOT):
    for rel, template, fields, _pred in specs(root):
        tpl = root / PKG / "templates" / template
        yield rel, render(tpl.read_text(encoding="utf-8"), fields, template)


def expected_from_predecessor(pred_text: str, fields: dict, template: str) -> str:
    """The version-1 bytes with exactly the declared lines changed: the instance header, the draft date, the
    version, one class appended after the last listed class, and the supersession."""
    out = pred_text
    swaps = [
        (re.compile(r"(?m)^> Instance filled from[^\n]*\n> [^\n]*\n> [^\n]*\n"), header(template)),
        (re.compile(r"(?m)^Date: \d{4}-\d{2}-\d{2} \(drafted\)"), f"Date: {fields['DRAFT_DATE']} (drafted)"),
        (re.compile(r"(?m)^Record version: `[^`\n]+`$"), f"Record version: `{fields['VERSION']}`"),
        (re.compile(r"(?m)^(Content classes the provider may receive[^\n]*\n\n(?:- `[a-z-]+`\n)+)"),
         lambda m: m.group(1) + f"- `{ADDED_CLASS}`\n"),
        (re.compile(r"(?m)^Proposed revocation state: active; supersedes no earlier statement$"),
         f"Proposed revocation state: active; {fields['SUPERSESSION']}"),
    ]
    for pattern, repl in swaps:
        out, n = pattern.subn(repl, out, count=1)
        if n != 1:
            raise ValueError(f"predecessor line not found exactly once: {pattern.pattern[:60]}")
    return out


def manifest_text(root: pathlib.Path = ROOT) -> str:
    rows = sorted((rel.as_posix(), sha(text.encode())) for rel, text in instances(root))
    return ("# DOSSIER AGENT-PROVIDER STATEMENT VERSION 2 MANIFEST\n"
            "# Candidate; this file and its rows bind nothing by themselves.\n"
            f"# {len(rows)} row(s) sorted by codepoint path; each hashes the record's exact bytes\n"
            "# and is the argument of one separate owner act over that record.\n"
            + "".join(f"{s}  {p}\n" for p, s in rows))


def stale(root: pathlib.Path = ROOT) -> list[str]:
    out = []
    try:
        produced = dict(instances(root))
        manifest = manifest_text(root)
        declared = list(specs(root))
    except (ValueError, KeyError, OSError) as exc:
        return [f"cannot regenerate: {exc}"]
    for rel, text in produced.items():
        file = root / rel
        if not file.is_file() or file.read_text(encoding="utf-8") != text:
            out.append(f"{rel.as_posix()}: differs from its regeneration")
    for rel, template, fields, pred in declared:
        try:
            want = expected_from_predecessor((root / pred).read_text(encoding="utf-8"), fields, template)
        except (ValueError, OSError) as exc:
            out.append(f"{rel.as_posix()}: predecessor unreadable: {exc}")
            continue
        if produced[rel] != want:
            out.append(f"{rel.as_posix()}: differs from its predecessor beyond the declared lines")
        if f"`{ADDED_CLASS}`" in (root / pred).read_text(encoding="utf-8"):
            out.append(f"{rel.as_posix()}: the predecessor already lists {ADDED_CLASS}")
    for md in sorted((root / PKG / "instances").glob("*/*.md")):
        if md.relative_to(root) not in produced:
            out.append(f"{md.relative_to(root).as_posix()}: produced by no params entry")
    m = root / PKG / MANIFEST_NAME
    if not m.is_file() or m.read_text(encoding="utf-8") != manifest:
        out.append(f"{MANIFEST_NAME}: stale or missing")
    for md in sorted((root / PKG).rglob("*.md")):
        rel = md.relative_to(root / PKG)
        if rel.parts[0] in ("instances", "reviews") or DISPOSITIONS.match(md.name):
            continue
        if HEX64.search(md.read_text(encoding="utf-8")):
            out.append(f"{rel.as_posix()}: carries a 64-hex token")
    return out


def write(root: pathlib.Path = ROOT) -> None:
    for rel, text in instances(root):
        (root / rel).write_text(text, encoding="utf-8")
    (root / PKG / MANIFEST_NAME).write_text(manifest_text(root), encoding="utf-8")


# --- selftest ---------------------------------------------------------------

def _fixture(tmp: pathlib.Path) -> pathlib.Path:
    shutil.copytree(ROOT / PKG, tmp / PKG, ignore=shutil.ignore_patterns("reviews"))
    for _rel, _t, _f, pred in specs(ROOT):
        (tmp / pred).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / pred, tmp / pred)
    write(tmp)
    return tmp


def selftest() -> int:
    results: list[tuple[str, bool]] = []
    record = PKG / "instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md"

    def caught(name, mutate, needle):
        with tempfile.TemporaryDirectory() as t:
            tmp = _fixture(pathlib.Path(t))
            mutate(tmp)
            found = stale(tmp)
            results.append((name, any(needle in f for f in found)))

    with tempfile.TemporaryDirectory() as t:
        tmp = _fixture(pathlib.Path(t))
        results.append(("a regenerated package verifies", stale(tmp) == []))
        text = (tmp / record).read_text()
        results.append(("the record lists the added class once", text.count(f"- `{ADDED_CLASS}`") == 1))
        results.append(("the record keeps the version-1 Record ID", "Record ID: `AGENT-PROVIDER-redis-redis-anthropic`" in text))

    def hand_edit(tmp):
        p = tmp / record
        p.write_text(p.read_text().replace("- `evidence-content`\n", ""))
    caught("a hand edit to the record refused", hand_edit, "differs from its regeneration")

    def drift_params(tmp):
        p = tmp / PKG / "instances/redis/params.json"
        p.write_text(p.read_text().replace("- `evidence-content`\\n", ""))
        write(tmp)
    caught("a class dropped through params refused against the predecessor", drift_params, "beyond the declared lines")

    def drift_template(tmp):
        p = tmp / PKG / "templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md"
        p.write_text(p.read_text().replace("It is not an egress record", "It is an egress record"))
        write(tmp)
    caught("a template prose change refused against the predecessor", drift_template, "beyond the declared lines")

    def drift_predecessor(tmp):
        pred = next(specs(tmp))[3]
        p = tmp / pred
        p.write_text(p.read_text().replace("- `derived-composites`\n", f"- `derived-composites`\n- `{ADDED_CLASS}`\n"))
    caught("a predecessor that already lists the class refused", drift_predecessor, "already lists")

    def orphan(tmp):
        (tmp / PKG / "instances/redis/EXTRA.md").write_text("x\n")
    caught("an orphan record refused", orphan, "produced by no params entry")

    def edit_manifest(tmp):
        p = tmp / PKG / MANIFEST_NAME
        p.write_text(p.read_text() + "# extra\n")
    caught("an edited manifest refused", edit_manifest, "stale or missing")

    def digest_in_md(tmp):
        (tmp / PKG / "SEMANTIC-DELTA.md").write_text("argument " + "a" * 64 + "\n")
    caught("a digest in a package Markdown file refused", digest_in_md, "64-hex")

    def digest_in_template_header(tmp):
        # The renderer replaces the template's header blockquote, so only the Markdown sweep can see this token.
        p = tmp / PKG / "templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md"
        p.write_text(re.sub(r"^> ", "> " + "b" * 64 + " ", p.read_text(), count=1, flags=re.M))
    caught("a digest in a template's header refused", digest_in_template_header, "templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md: carries a 64-hex token")

    def unfilled(tmp):
        p = tmp / PKG / "templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md"
        p.write_text(p.read_text() + "\n{{NOT_A_FIELD}}\n")
    caught("an unfilled field refused", unfilled, "unfilled field NOT_A_FIELD")

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
        print(f"wrote the instance record and {MANIFEST_NAME}")
        return 0
    problems = stale(ROOT)
    if problems:
        for p in problems:
            print(f"FAIL {p}")
        return 1
    if mode == "--digests":
        print("".join(line + "\n" for line in manifest_text(ROOT).splitlines() if not line.startswith("#")), end="")
    elif mode == "--manifest-digest":
        print(sha((ROOT / PKG / MANIFEST_NAME).read_bytes()))
    else:
        print("dossier-agent-provider-v2: record and manifest current")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
