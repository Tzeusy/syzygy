#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Record/check the owner's explicit adoption of the reviewed understanding amendment."""
import argparse
from datetime import datetime
import hashlib
import posixpath
import types
import json
from pathlib import Path
import re
import tempfile
import subprocess
import sys
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
CHANGE = "openspec/changes/polaris-manifesto-understanding-amendment/"
NAMES = ".openspec.yaml COVERAGE.md GOVERNING-DEPENDENCIES.md SYNTHESIS-MAP.json design.md proposal.md specs/polaris-generation/spec.md tasks.md".split()
REVIEW = "docs/reviews/R-POLARIS-UNDERSTANDING-FORMAL-SPEC-2026-09-13-RAW.md"
REVIEW_SHA = "36c93a0b8777629c854adf126a2927449bd557589f6107647668e449fe42785a"
MANIFEST = "docs/evidence/polaris-understanding-adoption-manifest-2026-09-13.json"
ACT = ".syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md"
AGGREGATE = ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
LABEL = "ADOPT POLARIS UNDERSTANDING AMENDMENT"
MARKER = "POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION"
# The readability-successor tool decides which successors count as performed,
# so the recorder runs only the tool bytes its history review saw. A tool
# change needs a new pin here, and so a new history review.
SUCCESSOR_TOOL = "scripts/readability_successor.py"
CONTESTED = ('contested', 'contested')
SUCCESSOR_TOOL_SHA = "fdb4e483978dbe005249f60744bcdeec16ec5c4a8c71ca6bf37f018dd8afbdad"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def successor_tool(root):
    """The readability-successor tool, executed from the exact bytes that were hashed."""
    source = read(root, SUCCESSOR_TOOL)
    require(digest(source) == SUCCESSOR_TOOL_SHA,
            'successor tool differs from its reviewed digest: ' + SUCCESSOR_TOOL)
    module = types.ModuleType('readability_successor')
    module.__file__ = str(root / SUCCESSOR_TOOL)
    sys.modules['readability_successor'] = module
    try:
        exec(compile(source, module.__file__, 'exec'), module.__dict__)
    finally:
        sys.modules.pop('readability_successor', None)
    return module


def read(root, rel):
    path = Path(rel)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("invalid path")
    target = root / path
    if any(p.is_symlink() for p in [target, *target.parents] if p != root.parent):
        raise ValueError("symlinked subject")
    return target.read_bytes()


def canonical(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def current_subject(root):
    raw = read(root, REVIEW)
    if digest(raw) != REVIEW_SHA:
        raise ValueError("review changed")
    bindings = re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`$", raw.decode(), re.M)
    if len(bindings) != 12 or len(dict(bindings)) != 12:
        raise ValueError("review binding population")
    for path, expected in bindings:
        if digest(read(root, path)) != expected:
            raise ValueError("reviewed bytes changed: " + path)
    population = sorted(CHANGE + name for name in NAMES)
    actual = sorted(p.relative_to(root).as_posix() for p in (root / CHANGE).rglob("*") if p.is_file())
    if population != actual or not set(population) <= dict(bindings).keys():
        raise ValueError("amendment population changed")
    return {"version": 1, "project": "project:syzygy",
            "artifact": "specification:syzygy:polaris-generation:understanding-amendment",
            "artifacts": [{"path": path, "sha256": digest(read(root, path)),
                           "role": "behavior-specification" if path.endswith("/spec.md") else "amendment-support"} for path in population],
            "review": {"path": REVIEW, "sha256": REVIEW_SHA},
            "reviewed_context": [{"path": path, "sha256": sha} for path, sha in bindings if path not in population],
            "modified_requirements": ["REQ-polaris-generation-" + n for n in ["002", "004", "006", "009", "012", "014", "019"]],
            "added_requirements": ["REQ-polaris-generation-030", "REQ-polaris-generation-031"],
            "scope": "Specification amendment adoption only; no implementation extension or new source, provider, write, deployment or release permission."}


def validate(root):
    expected = canonical(current_subject(root))
    if read(root, MANIFEST) != expected:
        raise ValueError("adoption manifest mismatch")
    return digest(expected)


def body(sha, instant):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", instant):
        raise ValueError("invalid act instant")
    datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
    return f"""# Polaris understanding specification amendment adoption

Owner: Tzeusy

Act instant: {instant}

Project identity: project:syzygy

Artifact identity: specification:syzygy:polaris-generation:understanding-amendment

Act type: adopt specification amendment

Provenance: owner-adopted (bootstrap, uncorrelated)

A1 audit-record identity: explicitly absent

Owner instruction, recorded verbatim: “Adopt it”

The instruction refers to the reviewed formal amendment offered immediately
before it. The manifest below binds its exact eight-file subject and retained
review/context hashes. This recorder-generated binding is not presented as a
longer phrase typed by the owner:

{LABEL}: {sha}

Manifest: {MANIFEST}

Scope: adopt the specification amendment at the manifest's exact bytes.
REQ-polaris-generation-002, 004, 006, 009, 012, 014 and 019 take their full
amended clauses and preserved scenarios; 030 and 031 are added. The other 22
predecessor requirements remain unchanged. Effective composition is 31
requirements and 177 scenarios, not an implementation completion verdict.

Supersession relationship: partial specification amendment to the subject of
POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md. Only the seven named requirement
blocks are superseded by their extended blocks; the predecessor remains in force
for its unchanged requirements and is preserved byte-for-byte.

Revocation relationship: none. Existing implementation and applicability acts
retain their own exact scopes. This act grants no implementation extension,
source/provider/content permission, write consent, deployment or release.

Adoption leaves the reviewed files and their candidate-era banners unchanged.
The act record determines effective status. This is bootstrap owner provenance,
not independent authorship verification, runtime evidence or product readiness.
"""


def block(content):
    return f"<!-- {MARKER}:BEGIN -->\n{content}<!-- {MARKER}:END -->\n"


def check_original(root):
    sha = validate(root)
    actual = read(root, ACT).decode()
    match = re.search(r"^Act instant: (.+)$", actual, re.M)
    if not match or actual != body(sha, match.group(1)):
        raise ValueError("dedicated act mismatch")
    aggregate = read(root, AGGREGATE).decode()
    if any(aggregate.count(f"<!-- {MARKER}:{suffix} -->") != 1 for suffix in ["BEGIN", "END"]) or aggregate.count(block(actual)) != 1:
        raise ValueError("aggregate act missing, changed or duplicated")


def record(root, instruction, instant):
    if instruction != "Adopt it":
        raise ValueError("unexpected owner instruction")
    sha = validate(root)
    content = body(sha, instant)
    aggregate = read(root, AGGREGATE)
    if (root / ACT).exists() or MARKER.encode() in aggregate:
        raise ValueError("adoption already recorded or partial")
    validate(root)
    with (root / ACT).open("x") as stream:
        stream.write(content)
    with (root / AGGREGATE).open("ab") as stream:
        stream.write(("\n" + block(content)).encode())
    check_original(root)


def selftest():
    bindings = re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`$", read(ROOT, REVIEW).decode(), re.M)
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for rel in [REVIEW, *[p for p, _ in bindings]]:
            target = root / rel; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(git_blob(ROOT, HISTORICAL, rel))
        (root / MANIFEST).parent.mkdir(parents=True, exist_ok=True)
        (root / MANIFEST).write_bytes(canonical(current_subject(root)))
        (root / AGGREGATE).parent.mkdir(parents=True, exist_ok=True)
        (root / AGGREGATE).write_text("# Synthetic aggregate\n")
        def refuses(fn):
            try: fn()
            except ValueError: return
            raise AssertionError("mutation accepted")
        target = root / (CHANGE + "design.md"); saved = target.read_bytes()
        target.write_bytes(saved + b"changed"); refuses(lambda: validate(root)); target.write_bytes(saved)
        extra = root / (CHANGE + "extra.md"); extra.write_text("extra")
        refuses(lambda: validate(root)); extra.unlink()
        refuses(lambda: record(root, "continue", "2026-09-13T00:00:00Z"))
        refuses(lambda: record(root, "Adopt it", "2026-02-30T00:00:00Z"))
        record(root, "Adopt it", "2026-09-13T00:00:00Z")
        refuses(lambda: record(root, "Adopt it", "2026-09-13T00:00:00Z"))
        with (root / AGGREGATE).open("a") as stream: stream.write("\nLater unrelated record.\n")
        check_original(root)
        with (root / AGGREGATE).open("a") as stream: stream.write(block(read(root, ACT).decode()))
        refuses(lambda: check_original(root))
    print("PASS subject drift, extra file, wrong instruction, invalid instant, duplicate act, non-tail readback and duplicated aggregate")


# The later record is technical evidence of the owner's existing act. It cannot
# perform adoption, change an old act, or admit any other changed subject.
HISTORICAL = '3c915991fbb0eebc38f8daaaea4d05679914b6b8'
ADOPTION = '077089d6268323c86fab9f6a5c32217e4955c006'
BASELINE = 'f7d80ca6b0f89b4005c52de6b01958d75f71cec5'
SPEC = CHANGE + 'specs/polaris-generation/spec.md'
PREDECESSOR = 'openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md'
DIRECTION = '.syzygy/governance/decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md'
PACKET = '.syzygy/governance/decisions/POLARIS-TREE-FORM-AMENDMENT.md'
OLD_SHA = 'b7c95f57ca5f67a18570b7124d20b223dff99aea2a936efef76d5940a400f93f'
NEW_SHA = '6841e63cda0ccdb81966a6fabbdfaf3721910df8ea04959711eb59843859ba58'
MANIFEST_SHA = '3f4b96956b85a268532521ee5d0b1212d28537af7fddf09f89c877bd54bbc40d'
EVIDENCE = 'docs/evidence/polaris-understanding-reconciliation-2026-09-28/'
PROOF = EVIDENCE + 'proof.json'
TEMPLATE = EVIDENCE + 'technical-record-template.json'
INPUTS = EVIDENCE + 'review-inputs.json'
DOC_PATCH = EVIDENCE + 'final-documentation.patch'
DOC_IMAGES = EVIDENCE + 'documentation-images.json'
RAW = EVIDENCE + 'REVIEW-RAW.md'
SUPPLEMENT = EVIDENCE + 'technical-record.json'
PLACEHOLDER = '__C2_RAW_REVIEW_SHA256__'
SCRIPT = 'scripts/record_polaris_understanding_adoption.py'
CHECK_GOV = 'scripts/check_governance.py'
POLICY = '.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md'
VISION = '.syzygy/governance/doctrine/vision.md'
DOC_PATHS = ('PROJECT-STATUS.md', '.syzygy/governance/decisions/README.md',
             '.github/workflows/governance-docs.yml')
FROZEN_PATHS = (EVIDENCE + 'README.md', PROOF, TEMPLATE, DOC_PATCH, DOC_IMAGES, SCRIPT,
                CHECK_GOV, POLICY, VISION, *DOC_PATHS)
# Read at C1, never at today's bytes: the status pages and the governance
# checker move on, CC-SPEC takes owner-adopted successors, and this recorder
# took its history reading after C3. CC-SPEC must still be a digest some
# performed act confirmed; this recorder's current bytes are bound by the
# latest history review instead (HISTORY-READING.md in the evidence package).
HISTORY_PATHS = (*DOC_PATHS, CHECK_GOV, POLICY, SCRIPT)
HISTORY_REVIEW = re.compile(r'HISTORY-REVIEW-([1-9][0-9]*)-RAW\.md')
# A basename is a history-review name, and so must be strictly HISTORY_REVIEW, when
# it matches this pattern (re.IGNORECASE, re.search): the word history, any run of
# characters other than ASCII letters and digits (including none), the word review.
HISTORY_REVIEW_LIKE = re.compile(r'history[^a-z0-9]*review', re.IGNORECASE)
POLICY_ACT = re.compile(r'^CONFIRM CRAFT AMENDMENT: CC-SPEC@([0-9a-f]{64})$', re.M)
TREE_REVIEWS = tuple('.syzygy/governance/decisions/POLARIS-TREE-FORM-AMENDMENT-REVIEW-'
                     + str(n) + '-RAW.md' for n in range(1, 5))


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def git_output(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True)
    require(result.returncode == 0, 'Git evidence unavailable: ' + ' '.join(args))
    return result.stdout


def git_blob(root, commit, path):
    require(bool(re.fullmatch('[0-9a-f]{40}', commit)), 'invalid evidence commit')
    require(git_output(root, 'cat-file', '-t', commit + ':' + path).strip() == b'blob',
            'evidence object is not a blob: ' + path)
    return git_output(root, 'show', commit + ':' + path)


def chain(pairs):
    """Compose one path's (predecessor, successor) pairs into one pair, or CONTESTED.

    A pair that changes the bytes is a step. The steps must form a single
    unbranched chain: exactly one first digest that no step reaches, and
    every step visited from it once, so a repeated step, two steps from one
    digest, a cycle or a second chain is contested. A pair that keeps the bytes says
    the path was unchanged; its digest must lie on the chain, or be the only
    such digest when there is no step.
    """
    steps = [(a, b) for a, b in pairs if a != b]
    kept = {a for a, b in pairs if a == b}
    if not steps:
        return (min(kept), min(kept)) if len(kept) == 1 else CONTESTED
    following = dict(steps)
    first = set(following) - set(following.values())
    if len(first) != 1:
        return CONTESTED
    nodes = list(first)
    while nodes[-1] in following and len(nodes) <= len(steps):
        nodes.append(following[nodes[-1]])
    if len(nodes) != len(steps) + 1 or not kept <= set(nodes):
        return CONTESTED
    return (nodes[0], nodes[-1])


class Evidence:
    """Read-only evidence seams; selftests replace these reads in memory."""
    def __init__(self, root):
        self.root = root

    def current(self, path):
        try:
            return read(self.root, path)
        except FileNotFoundError as exc:
            raise ValueError('missing evidence: ' + path) from exc

    def blob(self, commit, path):
        return git_blob(self.root, commit, path)

    def successor_rows(self):
        """{path: (predecessor, successor)} over every performed readability successor.

        Only a package that checks as performed-exact contributes; a package
        that fails to load or check contributes nothing and blocks no other.
        Paths are normalized. The pairs every package records for one path,
        whatever their order or spelling, compose into one pair (`chain`):
        a later successor whose predecessor is an earlier one's row extends
        that chain. A path whose pairs do not form one chain maps to
        CONTESTED and is refused when checked. The tool must be the reviewed
        bytes, and runs from the bytes that were hashed.
        """
        if getattr(self, '_successors', None) is not None:
            return self._successors
        claims = {}
        if (self.root / SUCCESSOR_TOOL).is_file():
            module = successor_tool(self.root)
            for config in sorted((self.root / module.CANDIDATES).glob('*/' + module.CONFIG)):
                try:
                    package = module.Package(self.root, config.parent.relative_to(self.root).as_posix())
                    if package.check() != 'performed-exact':
                        continue
                    installed = package.manifest_rows()
                    pairs = [(path, package.predecessor[path], installed[path]) for path in package.subjects]
                except Exception:  # noqa: BLE001 - any failing package grants nothing
                    continue
                for path, predecessor, successor in pairs:
                    # Keyed by normalized path, so './x' and 'x' are one path.
                    claims.setdefault(posixpath.normpath(path), []).append((predecessor, successor))
        rows = {key: chain(pairs) for key, pairs in claims.items()}
        self._successors = rows
        return rows

    def ancestor(self, earlier, later):
        git_output(self.root, 'merge-base', '--is-ancestor', earlier, later)

    def history_population(self):
        """Evidence paths ever added on HEAD's history, and those on disk."""
        # Every commit and every parent, merges included: a raw renamed away,
        # dropped by a merge, or added by the merge itself still counts, and
        # one path added on two branches appears twice.
        log = git_output(self.root, 'log', '--no-renames', '--full-history',
                         '--diff-merges=combined', '--diff-filter=A', '--name-only', '-z',
                         '--format=', 'HEAD', '--', EVIDENCE).decode(
                             'utf-8', 'replace').split('\0')
        # -z: paths arrive unquoted (core.quotePath cannot hide a non-ASCII name)
        # and newline-safe; NUL-splitting leaves only empty separators to drop.
        log = [p for p in log if p]
        base = self.root / EVIDENCE
        return log, [EVIDENCE + p.relative_to(base).as_posix()
                     for p in base.rglob('*') if p.is_file()]

    def introduction(self, path):
        commits = git_output(self.root, 'log', '--diff-filter=A', '--format=%H',
                             'HEAD', '--', path).decode().splitlines()
        require(len(commits) <= 1, 'reintroduced evidence: ' + path)
        return commits[0] if commits else None


def aggregate_block(data):
    begin = f'<!-- {MARKER}:BEGIN -->\n'.encode()
    end = f'<!-- {MARKER}:END -->\n'.encode()
    require(data.count(begin) == data.count(end) == 1, 'aggregate block population')
    start = data.index(begin)
    stop = data.index(end) + len(end)
    require(stop > start, 'aggregate block order')
    return data[start:stop]


def req004_parts(data):
    headings = list(re.finditer(rb'(?m)^### Requirement: [^\n]+\n', data))
    matches = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(data)
        if re.search(rb'(?m)^ID: REQ-polaris-generation-004$', data[heading.start():end]):
            matches.append((heading.start(), end))
    require(len(matches) == 1, 'REQ-004 identity ambiguous')
    start, end = matches[0]
    return data[:start], data[start:end], data[end:]


def composition(base, overlay):
    """Recount this pinned base/overlay using independent regex and line scans.

    This is deliberately the fixed two-source proof, not the evolving generic
    counter. The immutable manifest identifies the seven replacements and two
    additions; no removal or rename is admitted by this reconciliation.
    """
    def regex_counts(data):
        headings = list(re.finditer(rb'(?m)^### Requirement: [^\n]+$', data))
        result = {}
        for index, heading in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(data)
            block_data = data[heading.start():end]
            ids = re.findall(rb'^ID: (REQ-polaris-generation-[0-9]{3})$', block_data, re.M)
            require(len(ids) == 1 and ids[0] not in result, 'composition requirement identity')
            result[ids[0]] = len(re.findall(rb'^#### Scenario:', block_data, re.M))
        return result

    def line_counts(data):
        result = {}
        current = None
        headings = 0
        for line in data.splitlines():
            if line.startswith(b'### Requirement: '):
                headings += 1
                current = None
            elif line.startswith(b'ID: REQ-polaris-generation-'):
                current = line.removeprefix(b'ID: ')
                require(current not in result, 'composition duplicate identity')
                result[current] = 0
            elif line.startswith(b'#### Scenario:'):
                require(current is not None, 'composition scenario without identity')
                result[current] += 1
        require(headings == len(result), 'composition heading population')
        return result

    results = []
    for parse in (regex_counts, line_counts):
        original, amended = parse(base), parse(overlay)
        expected_modified = {('REQ-polaris-generation-' + n).encode()
                             for n in ('002', '004', '006', '009', '012', '014', '019')}
        expected_added = {b'REQ-polaris-generation-030', b'REQ-polaris-generation-031'}
        require(set(amended) & set(original) == expected_modified, 'composition replacement population')
        require(set(amended) - set(original) == expected_added, 'composition addition population')
        results.append(original | amended)
    require(results[0] == results[1], 'composition parsers disagree')
    return {'requirements': len(results[0]), 'scenarios': sum(results[0].values())}


def baseline_proof(evidence):
    """Validate both source links without claiming the supplement exists."""
    old_manifest = evidence.blob(HISTORICAL, MANIFEST)
    require(digest(old_manifest) == MANIFEST_SHA, 'historical manifest identity')
    require(evidence.current(MANIFEST) == old_manifest, 'historical manifest changed')
    manifest = json.loads(old_manifest)
    population = sorted(CHANGE + name for name in NAMES)
    require([row['path'] for row in manifest['artifacts']] == population,
            'historical subject population')
    historical_review = evidence.blob(HISTORICAL, REVIEW)
    require(digest(historical_review) == REVIEW_SHA, 'historical review identity')
    require(evidence.current(REVIEW) == historical_review, 'historical review changed')
    bindings = re.findall(r'^- `([^`]+)`: `([0-9a-f]{64})`$', historical_review.decode(), re.M)
    require(len(bindings) == len(dict(bindings)) == 12, 'historical review population')
    for path, sha in bindings:
        require(digest(evidence.blob(HISTORICAL, path)) == sha,
                'historical reviewed blob mismatch: ' + path)
    rows = []
    for row in manifest['artifacts']:
        path = row['path']
        old = evidence.blob(HISTORICAL, path)
        adopted = evidence.blob(ADOPTION, path)
        require(digest(old) == row['sha256'], 'historical subject hash: ' + path)
        expected = NEW_SHA if path == SPEC else row['sha256']
        require(digest(adopted) == expected, 'adoption blob mismatch: ' + path)
        current = evidence.current(path)
        if current != adopted:
            # A performed readability successor may replace adopted bytes, but
            # only one whose recorded predecessor is exactly these bytes.
            row = evidence.successor_rows().get(path)
            require(row != CONTESTED, 'two performed successors claim ' + path)
            require(row == (digest(adopted), digest(current)), 'current subject drift: ' + path)
        rows.append({'path': path, 'historical_sha256': digest(old),
                     'adopted_sha256': digest(adopted), 'changed': old != adopted})
    actual = sorted(p.relative_to(evidence.root).as_posix()
                    for p in (evidence.root / CHANGE).rglob('*') if p.is_file())
    require(actual == population, 'current subject population')
    old_act = evidence.blob(HISTORICAL, ACT)
    match = re.search(r'^Act instant: (.+)$', old_act.decode(), re.M)
    require(match is not None and old_act.decode() == body(MANIFEST_SHA, match.group(1)),
            'historical act identity')
    require(evidence.current(ACT) == old_act, 'historical act changed')
    old_block = aggregate_block(evidence.blob(HISTORICAL, AGGREGATE))
    require(old_block == block(old_act.decode()).encode(), 'historical aggregate mismatch')
    require(aggregate_block(evidence.current(AGGREGATE)) == old_block, 'aggregate act changed')
    preserved = []
    for path in (DIRECTION, PACKET, *TREE_REVIEWS):
        adopted = evidence.blob(ADOPTION, path)
        require(evidence.current(path) == adopted, 'owner evidence changed: ' + path)
        preserved.append({'path': path, 'sha256': digest(adopted)})
    direction = evidence.blob(ADOPTION, DIRECTION).decode()
    # Exact full-file preservation above is the source binding. These assertions
    # make the subject correspondence visible and reject an ambiguous source.
    for phrase in ('"1. Adopt and implement the Polaris tree-form amendment", 2. Permitted, 3.\n  Adopt now"',
                   'amended REQ-polaris-generation-004', 'as merged with this record.',
                   '31 requirements and 182 scenarios.'):
        require(direction.count(phrase) == 1, 'owner-to-subject correspondence')
    old_spec = evidence.blob(HISTORICAL, SPEC)
    new_spec = evidence.blob(ADOPTION, SPEC)
    require(digest(old_spec) == OLD_SHA, 'old spec identity')
    before, old_req, after = req004_parts(old_spec)
    new_before, new_req, new_after = req004_parts(new_spec)
    require((before, after) == (new_before, new_after), 'change outside REQ-004')
    old_scenarios = re.findall(rb'^#### Scenario: (.+)$', old_req, re.M)
    new_scenarios = re.findall(rb'^#### Scenario: (.+)$', new_req, re.M)
    added = [s.decode() for s in new_scenarios if s not in old_scenarios]
    require(len(added) == 5 and all(s in new_scenarios for s in old_scenarios), 'scenario delta')
    base = evidence.blob(HISTORICAL, PREDECESSOR)
    require(evidence.current(PREDECESSOR) == base, 'predecessor drift')
    totals = [composition(base, spec) for spec in (old_spec, new_spec)]
    require(totals == [{'requirements': 31, 'scenarios': 177},
                       {'requirements': 31, 'scenarios': 182}], 'effective composition')
    evidence.ancestor(HISTORICAL, ADOPTION)
    return {'version': 1, 'historical_commit': HISTORICAL, 'owner_adoption_commit': ADOPTION,
            'integration_base': BASELINE, 'manifest_sha256': digest(old_manifest),
            'historical_act_sha256': digest(old_act), 'aggregate_block_sha256': digest(old_block),
            'subjects': rows, 'preserved_owner_evidence': preserved,
            'composition_before': totals[0], 'composition_after': totals[1],
            'added_scenarios': added, 'changed_requirements': ['REQ-polaris-generation-004']}


def candidate_check(evidence):
    proof = baseline_proof(evidence)
    require(evidence.current(PROOF) == canonical(proof), 'candidate proof mismatch')
    inputs = json.loads(evidence.current(INPUTS))
    require(set(inputs) == {'version', 'files'} and inputs['version'] == 1,
            'review input schema')
    require([r['path'] for r in inputs['files']] == sorted(FROZEN_PATHS), 'review input population')
    for row in inputs['files']:
        require(set(row) == {'path', 'sha256'}, 'review input row schema')
        require(digest(evidence.current(row['path'])) == row['sha256'],
                'candidate input drift: ' + row['path'])
    template = evidence.current(TEMPLATE)
    require(template.count(PLACEHOLDER.encode()) == 1, 'template placeholder population')
    require(json.loads(template)['proof_sha256'] == digest(evidence.current(PROOF)), 'template proof binding')
    after = documentation_after_images(evidence)
    expected_images = {path: {'before_sha256': digest(evidence.current(path)),
                             'after_sha256': digest(after[path])} for path in DOC_PATHS}
    require(evidence.current(DOC_IMAGES) == canonical(expected_images), 'documentation image mismatch')
    return proof


def reviewed_template(evidence):
    raw = evidence.current(RAW)
    text = raw.decode()
    verdicts = re.findall(r'^Verdict:([^\n]*)$', text, re.M)
    require(verdicts == [' PASS'], 'independent review not confirming: expected exactly one PASS verdict header')
    commits = re.findall(r'^Reviewed commit:([^\n]*)$', text, re.M)
    require(len(commits) == 1, 'C1 review commit population')
    require(re.fullmatch(r' [0-9a-f]{40}', commits[0]) is not None, 'invalid C1 review commit')
    c1 = commits[0][1:]
    evidence.ancestor(BASELINE, c1)
    evidence.ancestor(c1, 'HEAD')
    c2 = evidence.introduction(RAW)
    require(c2 is not None and c2 != c1, 'C2 raw review must be retained after C1')
    evidence.ancestor(c1, c2)
    require(evidence.blob(c2, RAW) == raw, 'retained C2 review changed')
    bindings = re.findall(r'^- `([^`]+)`: `([0-9a-f]{64})`$', text, re.M)
    require(len(bindings) == len(set(p for p, _ in bindings)), 'duplicate C1 review input')
    require(set(p for p, _ in bindings) == set(FROZEN_PATHS) | {INPUTS}, 'C1 review input population')
    for path, sha in bindings:
        require(digest(evidence.blob(c1, path)) == sha, 'C1 review blob mismatch: ' + path)
        if path not in HISTORY_PATHS:
            require(digest(evidence.current(path)) == sha, 'review retired by changed input: ' + path)
    performed = set(POLICY_ACT.findall(evidence.current(AGGREGATE).decode()))
    require(digest(evidence.blob(c1, POLICY)) in performed, 'C1 CC-SPEC bytes are no performed CC-SPEC digest')
    history_review(evidence)
    # Validate the complete original freeze using its own immutable doc before-images.
    class Frozen(Evidence):
        def current(self, path):
            return evidence.blob(c1, path) if path in HISTORY_PATHS else evidence.current(path)
        def blob(self, commit, path):
            return evidence.blob(commit, path)
        def ancestor(self, earlier, later):
            return evidence.ancestor(earlier, later)
        def successor_rows(self):
            return evidence.successor_rows()
    candidate_check(Frozen(evidence.root))
    template = evidence.current(TEMPLATE)
    return template.replace(PLACEHOLDER.encode(), digest(raw).encode()), c1


def history_reviews(evidence):
    """Every history review, numbered 1..n, none deleted after it was committed."""
    population = evidence.history_population()
    malformed = sorted({p for paths in population for p in paths
                        if p.startswith(EVIDENCE)
                        and HISTORY_REVIEW_LIKE.search(p.rsplit('/', 1)[-1])
                        and not HISTORY_REVIEW.fullmatch(p[len(EVIDENCE):])})
    require(not malformed, 'malformed history review name: ' + ', '.join(malformed))
    twice = sorted({p for p in population[0] if population[0].count(p) > 1
                    and p.startswith(EVIDENCE) and HISTORY_REVIEW.fullmatch(p[len(EVIDENCE):])})
    require(not twice, 'history review added more than once: ' + ', '.join(twice))
    def named(paths):
        return {p for p in paths if p.startswith(EVIDENCE)
                and HISTORY_REVIEW.fullmatch(p[len(EVIDENCE):])}
    added, listed = map(named, population)
    def number(path):
        return int(HISTORY_REVIEW.fullmatch(path[len(EVIDENCE):]).group(1))
    reviews = sorted(set(added) | set(listed), key=number)
    require([number(p) for p in reviews] == list(range(1, len(reviews) + 1)),
            'history review numbering is not 1..n')
    deleted = sorted(set(added) - set(listed))
    require(not deleted, 'history review deleted: ' + ', '.join(deleted))
    return reviews


def history_review(evidence):
    """The latest retained history review must confirm this recorder's current bytes."""
    reviews = history_reviews(evidence)
    require(reviews, 'no history review binds the current recorder')
    for path in reviews:
        intro = evidence.introduction(path)
        require(intro is not None, 'history review not retained: ' + path)
        require(evidence.blob(intro, path) == evidence.current(path), 'retained history review changed: ' + path)
    text = evidence.current(reviews[-1]).decode()
    verdicts = re.findall(r'^Verdict:([^\n]*)$', text, re.M)
    require(verdicts in ([' CONFIRM'], [' CONFIRM WITH EXCEPTIONS']),
            'latest history review not confirming: ' + reviews[-1])
    bindings = re.findall(r'^- `' + re.escape(SCRIPT) + r'`: `([0-9a-f]{64})`$', text, re.M)
    require(bindings == [digest(evidence.current(SCRIPT))],
            'latest history review does not bind the current recorder: ' + reviews[-1])


def check_evidence(evidence):
    baseline_proof(evidence)
    expected, c1 = reviewed_template(evidence)
    require(evidence.current(SUPPLEMENT) == expected, 'technical record differs from reviewed template')
    images = json.loads(evidence.current(DOC_IMAGES))
    require(set(images) == set(DOC_PATHS), 'documentation population')
    c3 = evidence.introduction(SUPPLEMENT)
    if c3 is not None:
        c2 = evidence.introduction(RAW)
        require(c3 != c2, 'C3 technical record must follow C2 review')
        evidence.ancestor(c2, c3)
        require(evidence.blob(c3, SUPPLEMENT) == expected, 'retained C3 technical record changed')
    governance_source = evidence.blob(c3, CHECK_GOV) if c3 else evidence.current(CHECK_GOV)
    require(governance_source == evidence.blob(c1, CHECK_GOV), 'governance registration source changed before C3')
    for path, pair in images.items():
        require(set(pair) == {'before_sha256', 'after_sha256'}, 'documentation image schema')
        require(digest(evidence.blob(c1, path)) == pair['before_sha256'], 'documentation before-image: ' + path)
        # Freeze the final documentation at C3, not every future status-page edit.
        after = evidence.blob(c3, path) if c3 else evidence.current(path)
        require(digest(after) == pair['after_sha256'], 'documentation after-image: ' + path)
    return c1


def check(root):
    return check_evidence(Evidence(root))


def documentation_after_images(evidence):
    """Apply the frozen patch to its frozen before-images in a scratch directory."""
    patch = evidence.current(DOC_PATCH)
    paths = re.findall(rb'^\+\+\+ b/(.+)$', patch, re.M)
    require(sorted(p.decode() for p in paths) == sorted(DOC_PATHS), 'documentation patch population')
    with tempfile.TemporaryDirectory() as directory:
        scratch = Path(directory)
        for path in DOC_PATHS:
            target = scratch / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(evidence.current(path))
        result = subprocess.run(['git', 'apply', '--unidiff-zero', '--check', '-'], cwd=scratch,
                                input=patch, capture_output=True)
        require(result.returncode == 0, 'documentation patch does not apply')
        result = subprocess.run(['git', 'apply', '--unidiff-zero', '-'], cwd=scratch,
                                input=patch, capture_output=True)
        require(result.returncode == 0, 'documentation patch application failed')
        return {path: (scratch / path).read_bytes() for path in DOC_PATHS}


def reconciliation_selftest():
    """Exercise the checker through memory reads; never mutate the real corpus."""
    class Cached(Evidence):
        def __init__(self, root):
            super().__init__(root)
            self.cache = {}
        def blob(self, commit, path):
            key = (commit, path)
            if key not in self.cache:
                self.cache[key] = super().blob(commit, path)
            return self.cache[key]
    source = Cached(ROOT)
    c1 = 'f' * 40
    c2 = 'e' * 40
    c3 = 'd' * 40
    before = {path: source.current(path) for path in (*FROZEN_PATHS, INPUTS)}
    # Selftests also run after C3. Recover the reviewed C1 docs when available.
    if (ROOT / RAW).exists():
        match = re.search(r'^Reviewed commit: ([0-9a-f]{40})$', source.current(RAW).decode(), re.M)
        require(match is not None, 'selftest C1 identity')
        for path in HISTORY_PATHS:
            before[path] = source.blob(match.group(1), path)
    history_paths = [EVIDENCE + 'HISTORY-REVIEW-' + str(n) + '-RAW.md' for n in range(1, 11)]
    history_path = history_paths[-1]
    decoy_path = EVIDENCE + 'HISTORY-REVIEW-011-RAW.md'
    history_commit = 'c' * 40

    class Fixture(Evidence):
        def __init__(self):
            super().__init__(ROOT)
            self.files = dict(before)
            self.blobs = {}
            self.introductions = {RAW: c2, SUPPLEMENT: None, decoy_path: history_commit,
                                  **{path: history_commit for path in history_paths}}
            self.added = list(history_paths)
            self.recorded = {}
            # Today's performed successors, so the fixture tracks installed restyles.
            self.successors = dict(source.successor_rows())
        def successor_rows(self):
            return self.successors
        def current(self, path):
            if path in self.files:
                require(self.files[path] is not None, 'missing evidence: ' + path)
                return self.files[path]
            return source.current(path)
        def blob(self, commit, path):
            if (commit, path) in self.blobs:
                return self.blobs[(commit, path)]
            if commit == c1:
                return before[path]
            if commit == c2 and path == RAW:
                return raw
            if commit == history_commit and path in self.introductions:
                return self.files[path]
            if commit == c3:
                return self.recorded[path]
            return source.blob(commit, path)
        def ancestor(self, earlier, later):
            if set((earlier, later)) & {c1, c2, c3}:
                return
            return source.ancestor(earlier, later)
        def introduction(self, path):
            return self.introductions.get(path)
        def history_population(self):
            listed = [p for p, data in self.files.items()
                      if p.startswith(EVIDENCE) and data is not None]
            return list(self.added), listed

    fixture = Fixture()
    raw = ('Verdict: PASS\nReviewed commit: ' + c1 + '\n' + ''.join(
        '- `' + path + '`: `' + digest(data) + '`\n' for path, data in sorted(before.items()))).encode()
    fixture.files[RAW] = raw
    # Nine superseded REVISE raws and the confirming tenth: numeric order puts
    # it last; text order would not.
    for path in history_paths[:-1]:
        fixture.files[path] = ('Verdict: REVISE\n- `' + SCRIPT + '`: `' + '0' * 64 + '`\n').encode()
    fixture.files[history_path] = ('Verdict: CONFIRM\n- `' + SCRIPT + '`: `'
                                   + digest(source.current(SCRIPT)) + '`\n').encode()
    fixture.files[SCRIPT] = source.current(SCRIPT)
    fixture.files[SUPPLEMENT] = before[TEMPLATE].replace(PLACEHOLDER.encode(), digest(raw).encode())
    fixture.files.update(documentation_after_images(fixture))
    check_evidence(fixture)
    witnesses = []
    commit = git_output(ROOT, 'rev-parse', 'HEAD').decode().strip()

    def mutate(path, reason, *, historical=None, old=b'', new=b'\nmutated\n', missing=False):
        key = (historical, path) if historical else path
        mapping = fixture.blobs if historical else fixture.files
        existed = key in mapping
        saved = mapping.get(key)
        original = fixture.blob(historical, path) if historical else fixture.current(path)
        if not old:
            length = min(32, len(original))
            old = original[-length:]
            while original.count(old) != 1:
                length = min(length * 2, len(original))
                old = original[-length:]
            new = old + new
        require(original.count(old) == 1, 'selftest mutation fragment not unique: ' + path)
        mapping[key] = None if missing else original.replace(old, new, 1)
        if path == RAW and not historical:
            fixture.blobs[(c2, RAW)] = mapping[key]
        try:
            check_evidence(fixture)
        except ValueError as exc:
            require(reason in str(exc), 'wrong refusal: ' + str(exc) + '; wanted ' + reason)
            witnesses.append({'commit': commit, 'path': path, 'git_commit': historical,
                              'operation': 'remove' if missing else 'replace-once',
                              'old': old.decode(), 'new': None if missing else new.decode(),
                              'refusal': str(exc)})
        else:
            raise AssertionError('mutation accepted: ' + path)
        finally:
            if existed: mapping[key] = saved
            else: mapping.pop(key, None)
            if path == RAW and not historical:
                fixture.blobs.pop((c2, RAW), None)

    mutate(MANIFEST, 'historical manifest changed')
    mutate(MANIFEST, 'historical manifest identity', historical=HISTORICAL)
    mutate(ACT, 'historical act changed')
    mutate(AGGREGATE, 'aggregate act changed', old=block(source.current(ACT).decode()).encode(),
           new=block(source.current(ACT).decode().replace('Owner: Tzeusy', 'Owner: Mutant')).encode())
    mutate(SPEC, 'historical reviewed blob mismatch', historical=HISTORICAL)
    mutate(SPEC, 'adoption blob mismatch', historical=ADOPTION)
    mutate(SPEC, 'current subject drift')
    mutate(CHANGE + 'tasks.md', 'current subject drift')
    # A performed readability successor replaces a subject only from its
    # exact adopted predecessor.
    proposal = CHANGE + 'proposal.md'
    installed = dict(fixture.successors)
    today = fixture.current(proposal)
    adopted_proposal = fixture.blob(ADOPTION, proposal)
    restyled = adopted_proposal + b'\nrestyled\n'
    fixture.files[proposal] = restyled
    fixture.successors = {**installed, proposal: (digest(adopted_proposal), digest(restyled))}
    check_evidence(fixture)
    fixture.successors = {**installed, proposal: ('0' * 64, digest(restyled))}
    try:
        check_evidence(fixture)
    except ValueError as exc:
        require('current subject drift' in str(exc), 'wrong successor refusal: ' + str(exc))
        witnesses.append({'commit': commit, 'path': proposal, 'operation': 'successor-wrong-predecessor',
                          'old': None, 'new': None, 'refusal': str(exc)})
    else:
        raise AssertionError('successor from a foreign predecessor accepted')
    fixture.successors = {**installed, proposal: (digest(adopted_proposal), '1' * 64)}
    try:
        check_evidence(fixture)
    except ValueError as exc:
        require('current subject drift' in str(exc), 'wrong successor refusal: ' + str(exc))
        witnesses.append({'commit': commit, 'path': proposal, 'operation': 'successor-row-mismatch',
                          'old': None, 'new': None, 'refusal': str(exc)})
    else:
        raise AssertionError('bytes other than the successor row accepted')
    fixture.successors = {**installed, proposal: CONTESTED}
    try:
        check_evidence(fixture)
    except ValueError as exc:
        require('two performed successors claim' in str(exc), 'contested refusal: ' + str(exc))
        witnesses.append({'commit': commit, 'path': proposal, 'operation': 'successor-contested',
                          'old': None, 'new': None, 'refusal': str(exc)})
    else:
        raise AssertionError('contested successor accepted')
    fixture.files[proposal] = today
    fixture.successors = installed
    mutate(DIRECTION, 'owner evidence changed')
    mutate(DIRECTION, 'missing evidence', missing=True)
    mutate(DIRECTION, 'owner evidence changed', historical=ADOPTION)
    mutate(SUPPLEMENT, 'missing evidence', missing=True)
    mutate(SUPPLEMENT, 'technical record differs', old=fixture.current(SUPPLEMENT), new=b'{}\n')
    mutate(RAW, 'retained C2 review changed', historical=c2)
    mutate(SUPPLEMENT, 'technical record differs', old=NEW_SHA.encode(), new=b'0' * 64)
    mutate(SUPPLEMENT, 'technical record differs', old=SPEC.encode(), new=b'wrong/path')
    mutate(SUPPLEMENT, 'technical record differs', old=b'"version": 1', new=b'"version": 1, "extra_subject": "unreviewed"')
    mutate(RAW, 'independent review not confirming', old=b'Verdict: PASS', new=b'Verdict: REVISE')
    mutate(RAW, 'independent review not confirming', old=b'Verdict: PASS', new=b'Verdict: REVISE\nVerdict: PASS')
    mutate(RAW, 'independent review not confirming', old=b'Verdict: PASS', new=b'Verdict: PASS\nVerdict: PASS')
    mutate(RAW, 'C1 review commit population', old=('Reviewed commit: ' + c1).encode(),
           new=('Reviewed commit: wrong\nReviewed commit: ' + c1).encode())
    mutate(RAW, 'C1 review commit population', old=('Reviewed commit: ' + c1).encode(),
           new=('Reviewed commit: ' + c1 + '\nReviewed commit: ' + 'a' * 40).encode())
    mutate(RAW, 'invalid C1 review commit', old=c1.encode(), new=b'bad-commit')
    mutate(RAW, 'C1 review input population', old=('- `' + TEMPLATE + '`:').encode(), new=b'- `wrong/template`:')
    mutate(TEMPLATE, 'review retired by changed input')
    mutate(INPUTS, 'review retired by changed input')
    mutate(SCRIPT, 'latest history review does not bind the current recorder')
    mutate(history_path, 'latest history review not confirming', old=b'Verdict: CONFIRM', new=b'Verdict: REVISE')
    mutate(history_path, 'history review deleted', missing=True)
    mutate(history_paths[4], 'history review deleted', missing=True)
    # A leading zero or a suffix is refused, never skipped: a REVISE raw so
    # named would otherwise leave an earlier CONFIRM standing.
    for malformed in (decoy_path, EVIDENCE + 'HISTORY-REVIEW-3-RAW-ADDENDUM.md',
                      EVIDENCE + 'history-review-11-raw.md', EVIDENCE + 'sub/HISTORY-REVIEW-11-RAW.md',
                      EVIDENCE + 'HISTORY_REVIEW-11-RAW.md', EVIDENCE + 'History Review 11 RAW.md'):
        fixture.added.append(malformed)
        fixture.files[malformed] = ('Verdict: REVISE\n- `' + SCRIPT + '`: `' + '0' * 64 + '`\n').encode()
        try:
            check_evidence(fixture)
        except ValueError as exc:
            require('malformed history review name' in str(exc), 'wrong malformed-name refusal: ' + str(exc))
            witnesses.append({'commit': commit, 'path': malformed, 'operation': 'add-malformed-name',
                              'old': None, 'new': None, 'refusal': str(exc)})
        else:
            raise AssertionError('malformed history review name accepted')
        finally:
            fixture.added.pop()
            del fixture.files[malformed]
    mutate(history_path, 'latest history review not confirming', old=b'Verdict: CONFIRM\n',
           new=b'Verdict: CONFIRM\nVerdict: REVISE\n')
    mutate(history_path, 'does not bind the current recorder', old=b'`\n',
           new=b'`\n- `' + SCRIPT.encode() + b'`: `' + b'1' * 64 + b'`\n')
    mutate(AGGREGATE, 'no performed CC-SPEC digest',
           old=b'\nCONFIRM CRAFT AMENDMENT: CC-SPEC@' + digest(before[POLICY]).encode(),
           new=b'\n> CONFIRM CRAFT AMENDMENT: CC-SPEC@' + digest(before[POLICY]).encode())
    mutate(history_path, 'retained history review changed', historical=history_commit)
    mutate(AGGREGATE, 'no performed CC-SPEC digest', old=b'CC-SPEC@' + digest(before[POLICY]).encode(), new=b'CC-SPEC@' + b'0' * 64)
    mutate(POLICY, 'C1 review blob mismatch', historical=c1)
    mutate(PROOF, 'review retired by changed input')
    mutate(DOC_PATHS[0], 'documentation after-image')
    mutate(CHECK_GOV, 'governance registration source changed before C3')
    # A raw on disk that no commit added is refused, never ignored.
    uncommitted = EVIDENCE + 'HISTORY-REVIEW-11-RAW.md'
    fixture.files[uncommitted] = fixture.files[history_path]
    try:
        check_evidence(fixture)
    except ValueError as exc:
        require('history review not retained' in str(exc), 'wrong uncommitted refusal: ' + str(exc))
        witnesses.append({'commit': commit, 'path': uncommitted, 'operation': 'add-uncommitted',
                          'old': None, 'new': None, 'refusal': str(exc)})
    else:
        raise AssertionError('uncommitted history review accepted')
    finally:
        del fixture.files[uncommitted]
    # A numbering gap and an empty population, each removed from Git history
    # and disk alike, so the deletion guard cannot be what refuses them.
    for removed, reason in ((history_paths[4:5], 'history review numbering is not 1..n'),
                            (history_paths, 'no history review binds')):
        saved_added, saved_files = list(fixture.added), {p: fixture.files[p] for p in removed}
        fixture.added = [p for p in fixture.added if p not in removed]
        for path in removed:
            fixture.files[path] = None
        try:
            check_evidence(fixture)
        except ValueError as exc:
            require(reason in str(exc), 'wrong population refusal: ' + str(exc))
            witnesses.append({'commit': commit, 'path': EVIDENCE, 'operation': 'remove-history-reviews',
                              'old': sorted(removed), 'new': None, 'refusal': str(exc)})
        else:
            raise AssertionError('history review population mutation accepted')
        finally:
            fixture.added = saved_added
            fixture.files.update(saved_files)
    # C3 has a different source for documentation: its immutable commit, not
    # today's status page. Exercise that path as well as the pre-commit gate.
    fixture.introductions[SUPPLEMENT] = c3
    fixture.recorded = {path: fixture.current(path) for path in (SUPPLEMENT, CHECK_GOV, *DOC_PATHS)}
    check_evidence(fixture)
    mutate(SUPPLEMENT, 'retained C3 technical record changed', historical=c3)
    mutate(DOC_PATHS[0], 'documentation after-image', historical=c3)
    mutate(CHECK_GOV, 'governance registration source changed before C3', historical=c3)
    fixture.files[DOC_PATHS[0]] += b'\nUnrelated later status-page update.\n'
    check_evidence(fixture)
    fixture.files[DOC_PATHS[0]] = fixture.recorded[DOC_PATHS[0]]
    for path, replacement, reason in ((RAW, None, 'C2 raw review must be retained'),
                                       (SUPPLEMENT, c2, 'C3 technical record must follow C2'),
                                       (history_path, None, 'history review not retained')):
        saved = fixture.introductions[path]
        fixture.introductions[path] = replacement
        try:
            check_evidence(fixture)
        except ValueError as exc:
            require(reason in str(exc), 'wrong introduction refusal: ' + str(exc))
            witnesses.append({'commit': commit, 'path': path, 'operation': 'replace-introduction-seam',
                              'old': saved, 'new': replacement, 'refusal': str(exc)})
        else:
            raise AssertionError('introduction mutation accepted')
        finally:
            fixture.introductions[path] = saved
    print('PASS reconciliation selftest: 3 valid states (before C3, committed C3, later docs); ' + str(len(witnesses)) + ' trust-boundary mutations refused; owner direction and technical proof remain distinct.')
    print('RULE6-WITNESSES ' + json.dumps(witnesses, sort_keys=True))


def history_population_selftest():
    """Run the real Git population query over a scratch repository."""
    def git(root, *args):
        subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
    def raw(root, name, text):
        target = root / EVIDENCE / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
    cases = []
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        git(root, 'init', '-q', '-b', 'main')
        git(root, 'config', 'user.email', 'selftest@example.invalid')
        git(root, 'config', 'user.name', 'selftest')
        raw(root, 'HISTORY-REVIEW-1-RAW.md', 'Verdict: CONFIRM\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'raw 1')
        # Renamed into place, then deleted.
        raw(root, 'draft.md', 'Verdict: REVISE\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'draft')
        git(root, 'mv', EVIDENCE + 'draft.md', EVIDENCE + 'HISTORY-REVIEW-2-RAW.md')
        git(root, 'commit', '-qm', 'rename')
        git(root, 'rm', '-q', EVIDENCE + 'HISTORY-REVIEW-2-RAW.md')
        git(root, 'commit', '-qm', 'delete')
        added, _listed = Evidence(root).history_population()
        cases.append(('renamed then deleted raw counts as added',
                      EVIDENCE + 'HISTORY-REVIEW-2-RAW.md' in added))
        # Added on a side branch, dropped by an ours-merge.
        git(root, 'checkout', '-q', '-b', 'side')
        raw(root, 'HISTORY-REVIEW-3-RAW.md', 'Verdict: REVISE\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'raw 3')
        git(root, 'checkout', '-q', 'main')
        git(root, 'merge', '-q', '-s', 'ours', '--no-edit', 'side')
        added, listed = Evidence(root).history_population()
        cases.append(('raw dropped by a merge counts as added',
                      EVIDENCE + 'HISTORY-REVIEW-3-RAW.md' in added
                      and EVIDENCE + 'HISTORY-REVIEW-3-RAW.md' not in listed))
        # Two branches add the same raw; the merge keeps the side's CONFIRM.
        raw(root, 'HISTORY-REVIEW-4-RAW.md', 'Verdict: REVISE\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'raw 4 on main')
        git(root, 'checkout', '-q', '-b', 'side4', 'HEAD~1')
        raw(root, 'HISTORY-REVIEW-4-RAW.md', 'Verdict: CONFIRM\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'raw 4 on side')
        git(root, 'checkout', '-q', 'main')
        subprocess.run(['git', '-C', str(root), 'merge', '-q', '--no-edit', 'side4'],
                       capture_output=True)
        (root / EVIDENCE / 'HISTORY-REVIEW-4-RAW.md').write_text('Verdict: CONFIRM\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'merge keeps side')
        try:
            history_reviews(Evidence(root))
        except ValueError as exc:
            cases.append(('one raw added on two branches refused',
                          'added more than once' in str(exc)))
        else:
            cases.append(('one raw added on two branches refused', False))
        # A raw added by a merge commit itself, then deleted.
        git(root, 'checkout', '-q', '-b', 'side5')
        raw(root, 'unrelated.md', 'x\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'side 5')
        git(root, 'checkout', '-q', 'main')
        git(root, 'merge', '-q', '--no-commit', '--no-ff', 'side5')
        raw(root, 'HISTORY-REVIEW-5-RAW.md', 'Verdict: REVISE\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'merge adds raw 5')
        git(root, 'rm', '-q', EVIDENCE + 'HISTORY-REVIEW-5-RAW.md')
        git(root, 'commit', '-qm', 'delete raw 5')
        added, _listed = Evidence(root).history_population()
        cases.append(('raw added by a merge commit counts as added',
                      EVIDENCE + 'HISTORY-REVIEW-5-RAW.md' in added))
        # A raw on disk that no commit added.
        raw(root, 'HISTORY-REVIEW-6-RAW.md', 'Verdict: CONFIRM\n')
        added, listed = Evidence(root).history_population()
        cases.append(('uncommitted raw is listed from disk',
                      EVIDENCE + 'HISTORY-REVIEW-6-RAW.md' in listed
                      and EVIDENCE + 'HISTORY-REVIEW-6-RAW.md' not in added))
    # Committed then deleted names that core.quotePath or a line split would
    # hide, and near-miss spellings; each is refused, never skipped, while a
    # strictly named raw beside them still passes.
    for label, name in (('non-ASCII name', 'HISTORY-REVIEW-2-RAW-\u00e9.md'),
                        ('newline in name', 'history-review-2\nx.md'),
                        ('dot-separated near-miss', 'history.review-2-RAW.md'),
                        ('prefixed near-miss', 'old-history-review-2.md'),
                        ('newline-joined near-miss', 'history\nreview.md'),
                        ('underscore near-miss', 'HISTORY_REVIEW-2-RAW.md'),
                        ('space near-miss', 'History Review 2 RAW.md'),
                        ('run-together near-miss', 'HistoryReview-2-RAW.md')):
        for deleted in (False, True):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                git(root, 'init', '-q', '-b', 'main')
                git(root, 'config', 'user.email', 'selftest@example.invalid')
                git(root, 'config', 'user.name', 'selftest')
                raw(root, 'HISTORY-REVIEW-1-RAW.md', 'Verdict: CONFIRM\n')
                raw(root, name, 'Verdict: REVISE\n')
                git(root, 'add', '-A'); git(root, 'commit', '-qm', 'strict raw and near miss')
                if deleted:
                    git(root, 'rm', '-q', '-f', EVIDENCE + name); git(root, 'commit', '-qm', 'delete')
                try:
                    history_reviews(Evidence(root))
                    ok = False
                except ValueError as exc:
                    ok = 'malformed history review name' in str(exc)
                cases.append((label + (' deleted' if deleted else ' on disk') + ' refused', ok))
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        git(root, 'init', '-q', '-b', 'main')
        git(root, 'config', 'user.email', 'selftest@example.invalid')
        git(root, 'config', 'user.name', 'selftest')
        for n in (1, 2):
            raw(root, 'HISTORY-REVIEW-' + str(n) + '-RAW.md', 'Verdict: CONFIRM\n')
        raw(root, 'HISTORY-READING.md', 'x\n'); raw(root, 'history-reading-rule6.json', '{}\n')
        git(root, 'add', '-A'); git(root, 'commit', '-qm', 'legitimate names')
        cases.append(('strict names and unrelated history files pass',
                      history_reviews(Evidence(root)) == [EVIDENCE + 'HISTORY-REVIEW-' + str(n)
                                                          + '-RAW.md' for n in (1, 2)]))
    for label, ok in cases:
        require(ok, 'history population selftest: ' + label)
    print('PASS history population selftest: ' + str(len(cases)) + ' real-Git cases')


def render_reconciliation(root):
    evidence = Evidence(root)
    expected, _ = reviewed_template(evidence)
    record = json.loads(expected)
    today = datetime.now(ZoneInfo(record['recording_timezone'])).date().isoformat()
    require(record['recording_date'] == today, 'recording date moved; re-freeze and re-review')
    # Exclusive append of a new technical record; no owner act or aggregate write.
    with (root / SUPPLEMENT).open('xb') as stream:
        stream.write(expected)
    require(read(root, SUPPLEMENT) == expected, 'technical record readback')


def successor_rows_selftest():
    """Only a performed, exact readability successor grants rows; drift withdraws them."""
    import shutil
    import tempfile
    module = successor_tool(ROOT)
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        require(Evidence(root).successor_rows() == {}, 'successor rows without the successor tool')
        (root / 'scripts').mkdir()
        shutil.copy(ROOT / 'scripts/readability_successor.py', root / 'scripts')
        package = module.synthetic(root)
        require(Evidence(root).successor_rows() == {}, 'unperformed successor granted rows')
        phrase = module.pin(package)
        config_path = root / package.dir / 'SUCCESSOR.json'
        config = json.loads(config_path.read_text())
        config['pins'] = package.pins
        config_path.write_text(json.dumps(config))
        module.Package(root, package.dir).record(phrase, '2026-09-29T00:00:00Z')
        proposal = 'openspec/changes/example/proposal.md'
        rows = Evidence(root).successor_rows()
        require(set(rows) == set(package.subjects), 'performed successor rows population')
        require(rows[proposal] == (package.predecessor[proposal], digest(read(root, proposal))),
                'performed successor row')
        # A malformed sibling package grants nothing and blocks nothing.
        broken = root / module.CANDIDATES / 'broken-readability-successor' / module.CONFIG
        broken.parent.mkdir(parents=True)
        broken.write_text('{')
        require(Evidence(root).successor_rows() == rows, 'malformed sibling package changed the rows')
        broken.write_text('[' * 100000)
        require(Evidence(root).successor_rows() == rows, 'deeply nested sibling package changed the rows')
        # A full sibling copy whose pins are a list fails inside the tool's check.
        shutil.copytree(root / package.dir, broken.parent, dirs_exist_ok=True)
        wrong = json.loads((root / package.dir / module.CONFIG).read_text())
        wrong['pins'] = ['manifest_sha', 'review', 'review_sha']
        broken.write_text(json.dumps(wrong))
        require(Evidence(root).successor_rows() == rows, 'sibling with listed pins changed the rows')
        for field in ('label', 'predecessor', 'pins'):
            wrong = json.loads((root / package.dir / module.CONFIG).read_text())
            wrong[field] = 5 if field != 'pins' else []
            broken.write_text(json.dumps(wrong))
            require(Evidence(root).successor_rows() == rows, 'wrongly typed sibling ' + field + ' changed the rows')
        shutil.rmtree(broken.parent)
        tool = root / SUCCESSOR_TOOL
        reviewed = tool.read_bytes()
        tool.write_bytes(reviewed + b'\n# edited\n')
        try:
            Evidence(root).successor_rows()
        except ValueError as exc:
            require('successor tool differs' in str(exc), 'edited tool refusal: ' + str(exc))
        else:
            raise AssertionError('unreviewed successor tool accepted')
        tool.write_bytes(reviewed)
        # A second performed package over the same path chains or is refused, never ranked.
        second = module.CANDIDATES + '/example-second-readability-successor'
        shutil.copytree(root / package.dir, root / second)
        config = json.loads((root / second / module.CONFIG).read_text())
        config.update(label='SIGN OFF EXAMPLE SECOND READABILITY SUCCESSOR',
                      marker='EXAMPLE-SECOND-READABILITY-SUCCESSOR',
                      act='.syzygy/governance/decisions/EXAMPLE-SECOND-ACT.md',
                      pins={'manifest_sha': None, 'review': None, 'review_sha': None})
        # It shares the proposal, unchanged, and restyles a file of its own.
        other = 'openspec/changes/example/design.md'
        (root / other).write_bytes(b'# Design\n\nlong prose\n')
        # It spells the shared path differently; normalization still sees the claim.
        config['predecessor'] = {'openspec/changes/example/./proposal.md': digest(read(root, proposal)),
                                 other: digest(read(root, other))}
        (root / second / module.CONFIG).write_text(json.dumps(config))
        shutil.rmtree(root / second / 'proposed')
        (root / second / 'proposed' / other).parent.mkdir(parents=True)
        (root / second / 'proposed' / (other + '.proposed')).write_bytes(b'# Design\n\nShort.\n')
        again = module.Package(root, second)
        (root / again.manifest).write_text(again.render_manifest())
        # Its own review raw, so the first package keeps checking exact.
        first_raw = read(root, package.pins['review'])
        phrase = module.pin(again)
        own_raw = 'docs/reviews/R-EXAMPLE-SECOND-RAW.md'
        shutil.move(root / again.pins['review'], root / own_raw)
        (root / package.pins['review']).write_bytes(first_raw)
        again.pins['review'] = own_raw
        config['pins'] = again.pins
        (root / second / module.CONFIG).write_text(json.dumps(config))
        module.Package(root, second).record(phrase, '2026-09-29T00:00:01Z')
        require([p.check() for p in module.packages(root)] == ['performed-exact'] * 2,
                'both successors perform exactly')
        restyled = digest(read(root, proposal))
        composed = Evidence(root).successor_rows()
        require(composed.get(proposal) == (package.predecessor[proposal], restyled),
                'an unchanged later claim did not compose onto the chain')
        require(composed.get(other) == (config['predecessor'][other], digest(read(root, other))),
                'a later package lost its own row')
        # A later successor whose predecessor is the restyle extends the chain.
        third = module.later(package, 'example-third', proposal, b'# Why\n\nShortest.\n')
        require([p.check() for p in module.packages(root)] == ['performed-exact'] * 3,
                'every chained successor performs exactly')
        require(Evidence(root).successor_rows().get(proposal)
                == (package.predecessor[proposal], digest(read(root, proposal))),
                'a chain of successors did not compose from the first predecessor')
        # A fork from the first predecessor makes the path contested, not ranked.
        adopted_bytes = b'# Why\n\nlong prose\n'
        require(digest(adopted_bytes) == package.predecessor[proposal], 'fixture predecessor bytes')
        module.later(package, 'example-fork', proposal, read(root, proposal), start=adopted_bytes)
        require([p.check() for p in module.packages(root)] == ['performed-exact'] * 4,
                'the fork and the chain both perform exactly')
        contested = Evidence(root).successor_rows()
        require(contested.get(proposal) == CONTESTED, 'a forked successor chain accepted')
        require(contested.get(other) == (config['predecessor'][other], digest(read(root, other))),
                'a contested path blocked an uncontested one')
        shutil.rmtree(root / module.CANDIDATES / 'example-fork')
        require(Evidence(root).successor_rows().get(proposal)
                == (package.predecessor[proposal], digest(read(root, third.dir + '/proposed/' + proposal + module.SUFFIX))),
                'removing the fork did not restore the chain')
        (root / proposal).write_bytes(b'drifted\n')
        require(Evidence(root).successor_rows() == {}, 'drifted successor granted rows')
    a, b, c, d = ('a' * 64, 'b' * 64, 'c' * 64, 'd' * 64)
    for pairs, expected, label in (
            ([(a, b)], (a, b), 'one step'),
            ([(b, c), (a, b)], (a, c), 'two steps in any order'),
            ([(a, b), (b, b)], (a, b), 'an unchanged claim on the chain'),
            ([(a, a), (a, b)], (a, b), 'an unchanged claim of the first digest'),
            ([(a, a), (a, a)], (a, a), 'two unchanged claims of one digest'),
            ([(a, a), (b, b)], CONTESTED, 'two unchanged claims of different digests'),
            ([(a, b), (c, c)], CONTESTED, 'an unchanged claim off the chain'),
            ([(a, b), (a, b)], CONTESTED, 'one step claimed twice'),
            ([(a, b), (a, c)], CONTESTED, 'two steps from one digest'),
            ([(a, b), (c, d)], CONTESTED, 'two separate chains'),
            ([(a, b), (b, a)], CONTESTED, 'a cycle with no first digest'),
            ([(a, b), (b, c), (c, b)], (a, b), 'a step back to an earlier digest'),
            ([(a, b), (c, d), (d, c)], CONTESTED, 'a chain beside a cycle')):
        require(chain(pairs) == expected, 'chain composition: ' + label)
    print('PASS successor rows selftest: absent tool, unperformed, performed, malformed, deeply nested and wrongly typed siblings, edited tool, chained, forked and drifted packages; 13 composition cases')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    for action in ['prepare', 'record', 'check', 'selftest', 'candidate-check', 'render-reconciliation']:
        mode.add_argument('--' + action, action='store_true')
    parser.add_argument('--owner-instruction'); parser.add_argument('--instant')
    args = parser.parse_args()
    try:
        if args.selftest:
            selftest()
            reconciliation_selftest()
            history_population_selftest()
            successor_rows_selftest()
        elif args.candidate_check:
            candidate_check(Evidence(ROOT))
            print('PASS owner direction observed; 8 historical rows, 7 unchanged, 1 reconciled candidate; 31/177 -> 31/182. Exact digest reconciliation remains unresolved pending independent review and technical record.')
        elif args.prepare:
            with (ROOT / MANIFEST).open('xb') as stream: stream.write(canonical(current_subject(ROOT)))
            print('Prepared exact reviewed amendment manifest; no act recorded')
        elif args.record:
            record(ROOT, args.owner_instruction, args.instant)
            print('Recorded explicit owner adoption; bootstrap provenance; A1 absent')
        elif args.render_reconciliation:
            render_reconciliation(ROOT)
            print('Rendered reviewed technical supplement only; apply reviewed documentation patch before --check')
        else:
            c1 = check(ROOT)
            print('PASS owner direction observed; exact digest reconciled: 8 historical rows, 7 unchanged, REQ-004 adoption/current bytes; 31 requirements/182 scenarios; C1 ' + c1 + '. Technical evidence does not perform adoption or grant permission.')
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print('FAIL exact digest reconciliation unresolved: ' + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
