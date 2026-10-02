#!/usr/bin/env python3
"""Build, check and record readability successors of signed specifications.

A readability successor restyles a signed OpenSpec change for reading while
keeping every requirement heading, scenario heading and warrant block byte
for byte. Requirement body text is not machine-guarded; its fidelity is the
review's job. Each one is a package
directory under `.syzygy/governance/contracts/candidates/` holding:

- `SUCCESSOR.json` — the act label, record paths, the signed subjects and
  their effective predecessor digests, and the review pins;
- `proposed/<subject path>.proposed` — the whole proposed bytes of each
  changed subject (the suffix keeps them out of every live-document scan:
  their relative links resolve only at the install location);
- `SUCCESSOR-MANIFEST.txt` — one `<sha256>  <path>` row per signed subject,
  generated from the proposed bytes (or the predecessor, when unchanged);
- `OWNER-DECISION-PACKET.md` — the plain offer.

The owner signs off by writing exactly `<label>: <sha256 of the manifest>`.

Modes, each over one `--package DIR` or, with `--all`, every package:

- `--check` reports `candidate-unperformed` (no record; every subject at its
  predecessor; manifest and preservation verified) or `performed-exact`
  (both records exact; every subject at its manifest row, or at a row a
  chain of later performed successors installed over it: each one's
  recorded predecessor for that path is the digest the chain has reached,
  and each one's act instant is strictly later than the step before).
  Anything in between fails.
- `--write` regenerates the manifest; `--diff` prints predecessor→proposed.
- `--record --phrase "<owner phrase>"` refuses unless the phrase is exact over
  the pinned manifest digest, the pinned review raw carries exactly one
  `Verdict:` line (CONFIRM or CONFIRM WITH EXCEPTIONS) and exactly one
  `Manifest-file SHA-256: <digest>` line, and the candidate verifies. It
  writes the dedicated act, its marked section in the acceptance record, then
  the proposed subjects.
- `--selftest` runs every refusal over a synthetic package.
"""
import argparse
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path
import posixpath
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ".syzygy/governance/contracts/candidates"
AGGREGATE = ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
CONFIG = "SUCCESSOR.json"
MANIFEST = "SUCCESSOR-MANIFEST.txt"
SUFFIX = ".proposed"
ROW = re.compile(r"^([0-9a-f]{64})  (\S[^\n]*)$", re.M)
INSTANT = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")
VERDICT = re.compile(r"^Verdict: (.*)$", re.M)
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
#: The structure a restyle may never change, per requirement-bearing file.
STRUCTURE = re.compile(
    r"^### Requirement: [^\n]*$|^#### Scenario: [^\n]*$|^```yaml\nwarrants:[\s\S]*?^```$",
    re.M)
KEYS = ("label", "marker", "act", "title", "artifact", "supersedes", "scope",
        "predecessor", "pins")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(root, rel):
    path = Path(rel)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"invalid path: {rel}")
    target = root / path
    if any(p.is_symlink() for p in [target, *target.parents] if p != root.parent):
        raise ValueError(f"symlinked path: {rel}")
    return target.read_bytes()


class Package:
    def __init__(self, root, rel):
        self.root, self.dir = root, rel.rstrip("/")
        config = json.loads(read(root, f"{self.dir}/{CONFIG}"))
        if sorted(config) != sorted(KEYS):
            raise ValueError(f"{self.dir}/{CONFIG}: keys must be exactly {', '.join(KEYS)}")
        self.__dict__.update(config)
        if sorted(self.pins) != ["manifest_sha", "review", "review_sha"]:
            raise ValueError(f"{self.dir}/{CONFIG}: pins must be manifest_sha, review, review_sha")
        self.subjects = sorted(self.predecessor)
        self.phrase = re.compile(re.escape(self.label) + r": ([0-9a-f]{64})")

    @property
    def manifest(self):
        return f"{self.dir}/{MANIFEST}"

    def proposed_path(self, rel):
        return self.root / self.dir / "proposed" / (rel + SUFFIX)

    def proposed(self):
        """Subject → proposed bytes, for every subject the package changes."""
        base = self.root / self.dir / "proposed"
        found = sorted(p.relative_to(base).as_posix()
                       for p in base.rglob("*") if p.is_file()) if base.is_dir() else []
        unsuffixed = [rel for rel in found if not rel.endswith(SUFFIX)]
        if unsuffixed:
            raise ValueError(f"proposed files must end {SUFFIX}: {', '.join(unsuffixed)}")
        found = [rel[:-len(SUFFIX)] for rel in found]
        extra = sorted(set(found) - set(self.subjects))
        if extra:
            raise ValueError(f"proposed files outside the signed subjects: {', '.join(extra)}")
        if not found:
            raise ValueError("the package proposes no change")
        return {rel: read(self.root, f"{self.dir}/proposed/{rel}{SUFFIX}") for rel in found}

    def successor(self):
        proposed = self.proposed()
        return {rel: digest(proposed[rel]) if rel in proposed else self.predecessor[rel]
                for rel in self.subjects}

    def render_manifest(self):
        rows = self.successor()
        head = (f"# {self.title} — successor manifest\n"
                f"# Signing off `{self.label}: <sha256 of this file>` installs these rows.\n")
        return head + "".join(f"{rows[rel]}  {rel}\n" for rel in self.subjects)

    def current(self):
        return {rel: digest(read(self.root, rel)) for rel in self.subjects}

    def manifest_rows(self):
        rows = {path: sha for sha, path in ROW.findall(read(self.root, self.manifest).decode())}
        if sorted(rows) != self.subjects:
            raise ValueError("manifest rows are not exactly the signed subjects")
        return rows

    def candidate_findings(self):
        """Every reason the candidate is not a faithful, current proposal."""
        findings = []
        current = self.current()
        drifted = [rel for rel in self.subjects if current[rel] != self.predecessor[rel]]
        if drifted:
            findings.append("subject differs from its predecessor digest: " + ", ".join(drifted))
        try:
            proposed = self.proposed()
        except ValueError as error:
            return findings + [str(error)]
        for rel, data in proposed.items():
            before = read(self.root, rel)
            if data == before:
                findings.append(f"proposed bytes equal the predecessor: {rel}")
            if STRUCTURE.findall(before.decode()) != STRUCTURE.findall(data.decode()):
                findings.append(f"requirement, scenario or warrant structure changed: {rel}")
        if not (self.root / self.manifest).is_file():
            findings.append(f"manifest absent: {self.manifest}")
        elif read(self.root, self.manifest).decode() != self.render_manifest():
            findings.append("manifest differs from regeneration (run --write)")
        return findings

    def validate_pins(self):
        pins = self.pins
        if None in pins.values():
            raise ValueError("unpinned: the package's pins must name the reviewed "
                             "manifest digest and its confirming raw before any act")
        current = digest(read(self.root, self.manifest))
        if current != pins["manifest_sha"]:
            raise ValueError(f"manifest digest {current} differs from the pinned "
                             f"reviewed digest {pins['manifest_sha']}")
        raw = read(self.root, pins["review"])
        if digest(raw) != pins["review_sha"]:
            raise ValueError(f"review raw {pins['review']} differs from its pinned sha256")
        text = raw.decode("utf-8")
        verdicts = VERDICT.findall(text)
        if len(verdicts) != 1 or verdicts[0].strip() not in VERDICTS:
            raise ValueError("review raw needs exactly one `Verdict:` line, CONFIRM "
                             "or CONFIRM WITH EXCEPTIONS")
        if re.findall(r"^Manifest-file SHA-256: ([0-9a-f]{64})$", text, re.M) != [current]:
            raise ValueError("review raw does not bind the manifest digest on exactly "
                             "one `Manifest-file SHA-256:` line")
        return current

    def body(self, sha, instant, rows):
        if not INSTANT.fullmatch(instant):
            raise ValueError("invalid act instant")
        datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
        table = "\n".join(f"| `{rel}` | `{self.predecessor[rel]}` | `{rows[rel]}` |"
                          for rel in self.subjects)
        return f"""# {self.title}

Owner: Tzeusy

Act instant: {instant}

Project identity: project:syzygy

Artifact identity: {self.artifact}

Act type: sign off specification successor (successor to {self.supersedes})

Provenance: owner-adopted (bootstrap, uncorrelated)

A1 audit-record identity: explicitly absent

The owner performed the act by writing exactly:

```text
{self.label}: {sha}
```

The argument is the sha256 of {self.manifest}. It was recomputed at recording,
matched the phrase, and equals the reviewed digest the package pins.

Confirming review: {self.pins['review']} (sha256 {self.pins['review_sha']})

Signed subjects, predecessor and successor digests:

| Subject | Predecessor | Successor |
|---|---|---|
{table}

Scope: {self.scope} Every requirement, scenario and warrant block is
unchanged; the successor tool verifies that structure.

Supersession relationship: each subject is bound by its successor digest
above. Earlier acts and their digests are preserved as act-time history.

Revocation relationship: none. This act widens no implementation authority
and grants no source, provider, write, deployment or release permission.

This is bootstrap owner provenance, not independent authorship verification,
runtime evidence or product readiness.
"""

    def block(self, content):
        return f"<!-- {self.marker}:BEGIN -->\n{content}<!-- {self.marker}:END -->\n"

    def check(self):
        """Return the state name; raise on any partial or drifted state.

        A performed package's subject may sit at a later successor's row
        instead of its own: see `later_rows`. Any other difference fails.
        """
        performed = self.performed_rows()
        if performed is None:
            findings = self.candidate_findings()
            if findings:
                raise ValueError("; ".join(findings))
            return "candidate-unperformed"
        instant, rows = performed
        current = self.current()
        drifted = [rel for rel in self.subjects if current[rel] != rows[rel]
                   and current[rel] not in self.later_rows(rel, rows[rel], instant)]
        if drifted:
            raise ValueError("subject differs from its successor row: " + ", ".join(drifted))
        return "performed-exact"

    def later_rows(self, rel, row, instant):
        """Every digest a chain of later performed successors installs over `row`.

        A successor extends the chain for `rel` only when its recorded
        predecessor for that path (normalized, so `./x` is `x`) equals the
        digest the chain has reached and its act instant is strictly later
        than the step before (this act's `instant` for the first step), so
        neither this package nor an earlier one ever counts. Each step must
        verify as performed (`performed_rows`); a package that is
        unperformed, partial or malformed grants nothing. The chain starts at
        `row`, so a subject at any other digest stays drift.
        """
        key, performed = posixpath.normpath(rel), []
        for config in sorted((self.root / CANDIDATES).glob(f"*/{CONFIG}")):
            try:
                other = Package(self.root, config.parent.relative_to(self.root).as_posix())
                found = other.performed_rows()
                if found is None:
                    continue
                at, rows = found
                performed.extend((at, other.predecessor[path], rows[path]) for path in other.subjects
                                 if posixpath.normpath(path) == key)
            except Exception:  # noqa: BLE001 - a failing package grants nothing
                continue
        found, seen, frontier = set(), set(), [(row, instant)]
        while frontier:
            reached, after = frontier.pop()
            for at, predecessor, successor in performed:
                if predecessor == reached and at > after and (successor, at) not in seen:
                    seen.add((successor, at))
                    found.add(successor)
                    frontier.append((successor, at))
        return found

    def performed_rows(self):
        """None when unperformed; else (act instant, manifest rows), both records exact.

        Raises on any partial record. Subjects are not compared here.
        """
        aggregate = read(self.root, AGGREGATE).decode()
        act_exists = (self.root / self.act).exists()
        if not act_exists and self.marker not in aggregate and self.label not in aggregate:
            return None
        if not act_exists:
            raise ValueError("the aggregate carries the act but the dedicated record is absent")
        sha = self.validate_pins()
        rows = self.manifest_rows()
        actual = read(self.root, self.act).decode()
        instant = re.search(r"^Act instant: (.+)$", actual, re.M)
        if not instant or actual != self.body(sha, instant.group(1), rows):
            raise ValueError("dedicated act mismatch")
        for text, where in ((actual, self.act), (aggregate, AGGREGATE)):
            lines = [line for line in text.splitlines() if self.label in line]
            if lines != [f"{self.label}: {sha}"]:
                raise ValueError(f"{where}: expected exactly one binding line")
        if (any(aggregate.count(f"<!-- {self.marker}:{s} -->") != 1 for s in ("BEGIN", "END"))
                or aggregate.count(self.block(actual)) != 1):
            raise ValueError(f"{AGGREGATE}: act section missing, changed or duplicated")
        return instant.group(1), rows

    def record(self, phrase, instant):
        m = self.phrase.fullmatch(phrase or "")
        if not m:
            raise ValueError(f"owner phrase must be exactly `{self.label}: <sha256>`, "
                             f"got {phrase!r}")
        sha = self.validate_pins()
        if m.group(1) != sha:
            raise ValueError(f"owner argument {m.group(1)} does not match manifest {sha}")
        if self.check() != "candidate-unperformed":
            raise ValueError("sign-off already recorded")
        rows, proposed = self.manifest_rows(), self.proposed()
        content = self.body(sha, instant, rows)
        with (self.root / self.act).open("x", encoding="utf-8") as stream:
            stream.write(content)
        with (self.root / AGGREGATE).open("ab") as stream:
            stream.write(("\n" + self.block(content)).encode())
        for rel, data in proposed.items():
            (self.root / rel).write_bytes(data)
        if self.check() != "performed-exact":
            raise ValueError("record did not read back")

    def diff(self):
        out = []
        for rel, data in self.proposed().items():
            out.extend(difflib.unified_diff(
                read(self.root, rel).decode().splitlines(True), data.decode().splitlines(True),
                f"a/{rel}", f"b/{rel}"))
        return "".join(out)


def packages(root):
    base = root / CANDIDATES
    return [Package(root, p.parent.relative_to(root).as_posix())
            for p in sorted(base.glob(f"*/{CONFIG}"))]


# ------------------------------------------------------------------ selftest

SPEC = """## ADDED Requirements

### Requirement: X-REQ-001 — Something holds

Syzygy SHALL do the thing, and say so.

#### Scenario: The thing

- **WHEN** asked
- **THEN** it answers

```yaml
warrants:
  primary: VIS-2
```
"""


def synthetic(base, **overrides):
    """A throwaway repository with one signed change and its successor package."""
    change = "openspec/changes/example"
    files = {f"{change}/spec.md": SPEC.encode(), f"{change}/proposal.md": b"# Why\n\nlong prose\n"}
    for rel, data in files.items():
        (base / rel).parent.mkdir(parents=True, exist_ok=True)
        (base / rel).write_bytes(data)
    (base / AGGREGATE).parent.mkdir(parents=True, exist_ok=True)
    (base / AGGREGATE).write_text("# Acceptance act record\n")
    pkg = f"{CANDIDATES}/example-readability-successor"
    (base / pkg / "proposed" / change).mkdir(parents=True)
    (base / pkg / "proposed" / change / "proposal.md.proposed").write_bytes(
        b"# Why\n\nShort prose.\n")
    config = {"label": "SIGN OFF EXAMPLE READABILITY SUCCESSOR",
              "marker": "EXAMPLE-READABILITY-SUCCESSOR",
              "act": ".syzygy/governance/decisions/EXAMPLE-ACT.md",
              "title": "Example readability successor sign-off",
              "artifact": "specification:syzygy:example:readability-successor",
              "supersedes": "EXAMPLE-SIGNOFF-ACT.md", "scope": "readability restyle.",
              "predecessor": {rel: digest(data) for rel, data in files.items()},
              "pins": {"manifest_sha": None, "review": None, "review_sha": None}}
    config.update(overrides)
    (base / pkg / CONFIG).write_text(json.dumps(config))
    package = Package(base, pkg)
    (base / package.manifest).write_text(package.render_manifest())
    return Package(base, pkg)


def pin(package, verdict="Verdict: CONFIRM", binding=None, extra="",
        rel="docs/reviews/R-EXAMPLE-RAW.md"):
    sha = digest(read(package.root, package.manifest))
    (package.root / rel).parent.mkdir(parents=True, exist_ok=True)
    (package.root / rel).write_text(
        f"# review\n{verdict}\nManifest-file SHA-256: {binding or sha}\n{extra}")
    package.pins = {"manifest_sha": sha, "review": rel,
                    "review_sha": digest(read(package.root, rel))}
    return f"{package.label}: {sha}"


def later(first, name, rel, data, start=None, perform=True, instant="2026-09-30T00:00:00Z"):
    """A successor over `rel` alone, after `first`, with its own review raw.

    `start` first resets the subject, so the package can name a predecessor
    `first` never installed; `perform=False` leaves it a pinned candidate.
    """
    root, upper = first.root, name.upper()
    if start is not None:
        (root / rel).write_bytes(start)
    pkg = f"{CANDIDATES}/{name}"
    (root / pkg / "proposed" / rel).parent.mkdir(parents=True)
    (root / pkg / "proposed" / (rel + SUFFIX)).write_bytes(data)
    config = {"label": "SIGN OFF " + upper.replace("-", " "), "marker": upper,
              "act": f".syzygy/governance/decisions/{upper}-ACT.md",
              "title": f"{name} sign-off", "artifact": f"specification:syzygy:{name}",
              "supersedes": first.act, "scope": "second restyle.",
              "predecessor": {rel: digest(read(root, rel))},
              "pins": {"manifest_sha": None, "review": None, "review_sha": None}}
    (root / pkg / CONFIG).write_text(json.dumps(config))
    package = Package(root, pkg)
    (root / package.manifest).write_text(package.render_manifest())
    phrase = pin(package, rel=f"docs/reviews/R-{upper}-RAW.md")
    config["pins"] = package.pins
    (root / pkg / CONFIG).write_text(json.dumps(config))
    package = Package(root, pkg)
    if perform:
        package.record(phrase, instant)
    return package


def selftest():
    results = []

    def expect(label, fn, needle):
        try:
            fn()
        except ValueError as error:
            results.append((label, needle in str(error), str(error)))
        else:
            results.append((label, False, "accepted"))

    def fresh(**overrides):
        directory = tempfile.mkdtemp()
        return synthetic(Path(directory), **overrides)

    def states(*chosen):
        """Each package's state, or its refusal, so a failing fixture names itself."""
        found = []
        for package in chosen:
            try:
                found.append(package.check())
            except ValueError as error:
                found.append(str(error))
        return found

    instant = "2026-09-29T00:00:00Z"
    p = fresh()
    results.append(("candidate state", p.check() == "candidate-unperformed", ""))
    phrase = f"{p.label}: {digest(read(p.root, p.manifest))}"
    expect("unpinned refused", lambda: p.record(phrase, instant), "unpinned")
    phrase = pin(p)
    expect("wrong label refused", lambda: p.record("SIGN OFF OTHER: " + "0" * 64, instant),
           "owner phrase")
    expect("wrong argument refused", lambda: p.record(f"{p.label}: {'0' * 64}", instant),
           "does not match manifest")
    for label, kwargs, needle in (
            ("REVISE verdict refused", {"verdict": "Verdict: REVISE"}, "exactly one `Verdict:`"),
            ("CONFIRMED is not CONFIRM", {"verdict": "Verdict: CONFIRMED"},
             "exactly one `Verdict:`"),
            ("two verdicts refused", {"extra": "Verdict: REVISE\n"}, "exactly one `Verdict:`"),
            ("other manifest refused", {"binding": "3" * 64}, "does not bind"),
            ("two bindings refused", {"extra": f"Manifest-file SHA-256: {'4' * 64}\n"},
             "does not bind")):
        q = fresh()
        ph = pin(q, **kwargs)
        expect(label, lambda q=q, ph=ph: q.record(ph, instant), needle)
    q = fresh()
    ph = pin(q)
    q.pins["review_sha"] = "2" * 64
    expect("raw sha mismatch refused", lambda: q.record(ph, instant), "pinned sha256")
    q = fresh()
    ph = pin(q)
    q.pins["manifest_sha"] = "1" * 64
    expect("stale pinned digest refused", lambda: q.record(ph, instant), "differs from the pinned")
    expect("bad instant refused", lambda: p.record(phrase, "2026-09-29"), "invalid act instant")
    # Candidate predicates.
    q = fresh()
    spec = "openspec/changes/example/spec.md"
    (q.root / spec).write_text(SPEC + "\n")
    expect("drifted predecessor refused", q.check, "differs from its predecessor")
    q = fresh()
    target = q.proposed_path("openspec/changes/example/spec.md")
    target.write_text(SPEC.replace("X-REQ-001 — Something holds", "X-REQ-001 — Something"))
    (q.root / q.manifest).write_text(q.render_manifest())
    expect("renamed requirement refused", q.check, "structure changed")
    target.write_text(SPEC.replace("primary: VIS-2", "primary: VIS-3"))
    (q.root / q.manifest).write_text(q.render_manifest())
    expect("changed warrant refused", q.check, "structure changed")
    target.write_text(SPEC.replace("#### Scenario: The thing", "#### Scenario: A thing"))
    (q.root / q.manifest).write_text(q.render_manifest())
    expect("renamed scenario refused", q.check, "structure changed")
    target.write_text(SPEC)
    (q.root / q.manifest).write_text(q.render_manifest())
    expect("no-op proposal refused", q.check, "equal the predecessor")
    q = fresh()
    stray = q.proposed_path("openspec/changes/example/tasks.md")
    stray.write_text("x")
    expect("proposed file outside subjects refused", q.check, "outside the signed subjects")
    q = fresh()
    q.proposed_path("openspec/changes/example/spec.md").with_suffix("").write_text(SPEC)
    expect("unsuffixed proposed file refused", q.check, "must end .proposed")
    q = fresh()
    (q.root / q.manifest).write_text(q.render_manifest() + "\n")
    expect("stale manifest refused", q.check, "differs from regeneration")
    # Record, then every partial or drifted performed state.
    p.record(phrase, instant)
    results.append(("records and installs, performed-exact", p.check() == "performed-exact"
                    and read(p.root, "openspec/changes/example/proposal.md")
                    == b"# Why\n\nShort prose.\n", ""))
    expect("second record refused", lambda: p.record(phrase, instant), "already recorded")
    for label, rel, mutate, needle in (
            ("subject drift after act", "openspec/changes/example/proposal.md",
             lambda b: b + b"\n", "successor row"),
            ("act edited", p.act, lambda b: b.replace(b"Owner: Tzeusy", b"Owner: Other"),
             "dedicated act mismatch"),
            ("aggregate section duplicated", AGGREGATE,
             lambda b: b + b"\n" + p.block(read(p.root, p.act).decode()).encode(),
             "exactly one binding line"),
            ("aggregate marker duplicated", AGGREGATE,
             lambda b: b + f"<!-- {p.marker}:BEGIN -->\n".encode(), "duplicated"),
            ("aggregate section content edited", AGGREGATE,
             lambda b: b.replace(b"Owner: Tzeusy", b"Owner: Other", 1), "act section")):
        original = read(p.root, rel)
        (p.root / rel).write_bytes(mutate(original))
        expect(label, p.check, needle)
        (p.root / rel).write_bytes(original)
    (p.root / p.act).unlink()
    expect("aggregate without dedicated record", p.check, "dedicated record is absent")
    q = fresh()
    (q.root / "openspec/changes/example/proposal.md").write_bytes(b"# Why\n\nShort prose.\n")
    expect("installed without an act", q.check, "differs from its predecessor")
    # Chained successors: a later performed package whose predecessor for a
    # subject is this package's row supersedes that row; nothing else does.
    proposal = "openspec/changes/example/proposal.md"
    q = fresh()
    q.record(pin(q), instant)
    two = later(q, "example-chain-two", proposal, b"# Why\n\nShorter.\n")
    broken = q.root / CANDIDATES / "example-broken" / CONFIG
    broken.parent.mkdir(parents=True)
    broken.write_text("{")
    found = states(q, two)
    results.append(("superseded by a later successor, performed-exact",
                    found == ["performed-exact"] * 2, "; ".join(found)))
    three = later(q, "example-chain-three", proposal, b"# Why\n\nShortest.\n",
                  instant="2026-10-01T00:00:00Z")
    found = states(q, two, three)
    results.append(("superseded through a chain of two, performed-exact",
                    found == ["performed-exact"] * 3, "; ".join(found)))
    (q.root / proposal).write_bytes(b"# Why\n\nOther.\n")
    expect("superseded subject at no successor's row refused", q.check, "successor row")
    # A step back to earlier bytes: only later acts extend a chain, so the
    # intermediate digest, restored by hand, is drift for the latest act.
    q = fresh()
    q.record(pin(q), instant)
    restyled = read(q.root, proposal)
    two = later(q, "example-forward", proposal, b"# Why\n\nShorter.\n")
    back = later(q, "example-back", proposal, restyled, instant="2026-10-01T00:00:00Z")
    found = states(q, two, back)
    results.append(("a step back keeps every act performed-exact",
                    found == ["performed-exact"] * 3, "; ".join(found)))
    (q.root / proposal).write_bytes(b"# Why\n\nShorter.\n")
    expect("an earlier act's bytes restored by hand refused", back.check, "successor row")
    # One act naming a file twice cannot supersede its own row.
    q = fresh()
    config = json.loads(read(q.root, f"{q.dir}/{CONFIG}"))
    config["predecessor"]["openspec/changes/example/./proposal.md"] = config["predecessor"][proposal]
    (q.root / q.dir / CONFIG).write_text(json.dumps(config))
    q = Package(q.root, q.dir)
    (q.root / q.manifest).write_text(q.render_manifest())
    ph = pin(q)
    config["pins"] = q.pins  # on disk, so the package reloads as performed
    (q.root / q.dir / CONFIG).write_text(json.dumps(config))
    q = Package(q.root, q.dir)
    expect("an act's own row never supersedes its other row", lambda: q.record(ph, instant),
           "successor row")
    q = fresh()
    q.record(pin(q), instant)
    foreign = later(q, "example-foreign", proposal, b"# Why\n\nShorter.\n",
                    start=b"# Why\n\nforeign\n")
    found = states(foreign)
    results.append(("foreign-predecessor successor performs", found == ["performed-exact"], found[0]))
    expect("successor from a foreign predecessor supersedes nothing", q.check, "successor row")
    q = fresh()
    q.record(pin(q), instant)
    pending = later(q, "example-pending", proposal, b"# Why\n\nShorter.\n", perform=False)
    (q.root / proposal).write_bytes(read(q.root, f"{pending.dir}/proposed/{proposal}{SUFFIX}"))
    expect("unperformed successor supersedes nothing", q.check, "successor row")
    q = fresh()
    q.record(pin(q), instant)
    partial = later(q, "example-partial", proposal, b"# Why\n\nShorter.\n")
    (q.root / partial.act).unlink()
    expect("partially recorded successor supersedes nothing", q.check, "successor row")
    expect("config with an unknown key refused",
           lambda: fresh(extra="x"), "keys must be exactly")
    failed = [(label, detail) for label, ok, detail in results if not ok]
    for label, detail in failed:
        print(f"FAIL {label}: {detail}")
    print(f"{len(results)} fixtures, {len(failed)} failing")
    return 1 if failed else 0


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--package", help="package directory, relative to the repository")
    target.add_argument("--all", action="store_true", help="every successor package")
    mode = parser.add_mutually_exclusive_group(required=True)
    for flag in ("--check", "--write", "--diff", "--record", "--selftest"):
        mode.add_argument(flag, action="store_true")
    parser.add_argument("--phrase", help="the owner's phrase, verbatim")
    parser.add_argument("--instant", help="UTC act instant (default: now)")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        chosen = packages(ROOT) if args.all else [Package(ROOT, args.package)]
    except (ValueError, OSError, TypeError) as error:
        print(f"FAIL {error}")
        return 1
    if args.record or args.write or args.diff:
        if len(chosen) != 1:
            print("FAIL choose one --package")
            return 1
    status = 0
    for package in chosen:
        try:
            if args.write:
                (ROOT / package.manifest).write_text(package.render_manifest())
                print(f"wrote {package.manifest}")
            elif args.diff:
                print(package.diff(), end="")
            elif args.record:
                instant = args.instant or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                package.record(args.phrase, instant)
                print(f"Recorded the owner's sign-off for {package.dir}; subjects installed.")
            else:
                print(f"PASS {package.check()}: {package.dir}")
        except (ValueError, OSError) as error:
            print(f"FAIL {package.dir}: {error}")
            status = 1
    if args.check and args.all:
        print(f"{len(chosen)} successor package(s) checked")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
