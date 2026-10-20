#!/usr/bin/env python3
"""Record/check the owner's paired P-114 version and Ask-2 approval.

The proposal review binds the manifest FILE digest in the raw's first four
nonblank lines. Its one ROW hashes the registry bytes, the act's argument.
Frozen proposal/support hashes below are generated from the retained sources;
the reviewed commit is provenance, not a required reachable Git ancestor.

--record constructs and validates every output before replacing the subject,
dedicated act and aggregate. A failed replacement restores their prior bytes.
It consumes only the actual paired approval in the canonical direction, never
arbitrary owner-word arguments. It creates no tag, starts no process and reads
no observed repository. --builder-selftest runs the unchanged frozen builder
in its pre-install tree after recording (its unapplied fixtures need that gate).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile

import build_pwb_registry_machine_ceiling_amendment as build
import record_versioned_signoff as vs

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = build.PKG
RECORD = pathlib.Path(build.NEXT_RECORD)
AGGREGATE = pathlib.Path('.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md')
DIRECTION = pathlib.Path('.syzygy/governance/decisions/OWNER-DIRECTION-MACHINE-CEILING-INSTALL-2026-10-20.md')
PREDECESSOR = pathlib.Path(build.ACT_B_RECORD)
RAW = pathlib.Path('docs/reviews/R-PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-2-RAW.md')
DISPOSITION = PKG / 'ROUND-2-DISPOSITIONS.md'
OWNER_DATE = '2026-10-20'
OWNER_WORDS = 'yes, approve both'
FROZEN_SUBJECT = '7d7c3a3e8a68764f987aabd80d09d9c5963d7475'
PREFIX = 'ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY'
IDENTITY = 'PWB-OBSERVER-REGISTRY-ENTRY-MACHINE-CEILING-2026-10-20'
EXPLICIT = "explicitly given by the owner's words recorded below"
EXACT = re.compile(r'^Exact digest \(SHA-256\): `([0-9a-f]{64})`$', re.M)
RECORDED = re.compile(r'^Recorded at \(UTC\): (\S+)$', re.M)
FROZEN_FILES = {'.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/IMPACT-LEDGER.md': '232a7426c1dca623f870daff111d2707627e8e0da61fe5aec4a4bd8a9e866f62',
 '.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/OWNER-DECISION-PACKET.md': '34da008095846314be05d65ce74366053b4059dafd28f3eb554d8f9de9e0652c',
 '.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-MANIFEST.txt': '5396c8912cd329ba4d4413245e69c1d6fb81536713115e7ca32506e7b1768ac1',
 '.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/REVIEW-BRIEF.md': '2b95fb2737fb6c43f410fe0e465761b99778a4ee9e6c097b30fd1ec08fb01e5a',
 '.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/ROUND-2-DISPOSITIONS.md': 'd36843908f713bb4f31228f441c1f9ab9e516fcdfc9fcf2e44ccc75132fe5ae1',
 '.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/SEMANTIC-DELTA.md': '0afa07f6de0f5a92c78ac390dcc0fe260cfa5e3211cec1bd2c468c192f78e42f',
 '.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch': '5c7c89494ab86b1514839adc9100a96e7b65f42fb4f272a2443bcc50ae673290',
 '.syzygy/governance/decisions/OWNER-DIRECTION-MACHINE-CEILING-INSTALL-2026-10-20.md': 'cd27c05dd31ee9560730ff4f0bad34589a3882de2b85e97ef1978dea643d0d67',
 '.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md': 'f8ffc7a7c1b2d9266fce1bed40538d12e1f0561a1f8b334615070503a7d8f3ce',
 'docs/evidence/syzygy-59s5-live-size-2026-10-20.json': '0431487fde447f0144d4696a9574101211fd00637972353e2d15b4331d3cd58b',
 'docs/reviews/R-PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-2-RAW.md': '25415fcdd30fc1512185936bbe1ef22e8efeee6fd554065f8b0b98f4b12c8977',
 'scripts/build_pwb_registry_machine_ceiling_amendment.py': '180008f761cc0b6a6f67ab3d07704bad4ae65161ad50ac374e630a1cde3addc2'}
BASE_DIGEST = 'ad9cd6769bffbb1a3ef94625c73226dec133fb7c9f1e0bc40186b09b15e165fa'
SELFTEST_BASE = '03178a5483c5434780fc6c3b379b9006c9ae740e'


def sha(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def frozen_files(root: pathlib.Path) -> None:
    for rel, expected in FROZEN_FILES.items():
        path = root / rel
        require(path.is_file() and sha(path.read_bytes()) == expected,
                f'frozen source differs or is missing: {rel}')


def unique(text: str, pattern: str, label: str) -> str:
    values = re.findall(pattern, text, re.M)
    require(len(values) == 1, f'{label}: expected exactly one value')
    return values[0]


def predecessor(text: str) -> None:
    require(EXACT.findall(text) == [BASE_DIGEST], 'predecessor exact digest differs')
    require(unique(text, r'^Date: (\S+)$', 'predecessor date') == '2026-10-02',
            'predecessor date differs')
    require(unique(text, r'^Act identity: `([^`]+)`$', 'predecessor identity') == build.ACT_B_IDENTITY,
            'predecessor identity differs')
    require(unique(text, r'^Act type: `([^`]+)`$', 'predecessor type') == 'adopt-registry-entry',
            'predecessor type differs')
    require(unique(text, r'^Artifact identity: `([^`]+)`$', 'predecessor artifact') == build.SUBJECT.as_posix(),
            'predecessor artifact differs')
    # Act B records a date, not a UTC instant. No timestamp is invented.


def review(raw: str, manifest_sha: str, notes: str) -> tuple[str, str]:
    head = '\n'.join(line for line in raw.splitlines() if line.strip())
    head = '\n'.join(head.splitlines()[:4])
    reviewed = unique(head, r'^Reviewed commit: ([0-9a-f]{40})$', 'review commit')
    require(reviewed == FROZEN_SUBJECT, 'review commit differs from retained review')
    require(unique(head, r'^Manifest SHA-256: ([0-9a-f]{64})$', 'review manifest') == manifest_sha,
            'review head does not bind manifest FILE digest')
    verdict = unique(head, r'^Verdict: (.+)$', 'review verdict')
    require(verdict == 'CONFIRM WITH EXCEPTIONS', 'review is not the cleared notes-only verdict')
    findings = vs.review_findings(raw)
    require(findings == {1: 'note', 2: 'note', 3: 'note'}, 'review findings are not exactly notes 1, 2, 3')
    # This retained sibling predates the generic Reviewed-record header.
    # Scope this adapter to its frozen bytes; do not weaken the generic reader.
    require(notes.count(f'`{RAW.as_posix()}`') == 1, 'disposition raw reference differs')
    require(re.findall(r'^(\d+)\. \*\*', notes, re.M) == ['1', '2', '3'],
            'disposition note population differs')
    return reviewed, verdict


def approval(text: str) -> None:
    require(unique(text, r'^Date: (\S+)$', 'approval date') == OWNER_DATE, 'approval date differs')
    require(text.count(f'> {OWNER_WORDS}\n') == 1, 'actual paired owner reply differs')
    require(f'> Sign **`{build.NEW_TAG}`** and authorize its exact Ask 2 implementation scope.' in text,
            'paired version and Ask-2 offer differs')
    require('`p114-ceiling-transaction`' in text and 'option A without' in text,
            'canonical offered selection is absent')
    section = text.split('Implementation is exactly `OWNER-DECISION-PACKET.md` Ask 2 items 1–5:', 1)
    require(len(section) == 2, 'five-item implementation scope is absent')
    scope = section[1].split('Record, patch and implement', 1)[0]
    require(re.findall(r'^(\d+)\. ', scope, re.M) == ['1', '2', '3', '4', '5'],
            'implementation item population differs')


def instant(value: str) -> dt.datetime:
    require(re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', value) is not None,
            'recording instant must be strict UTC')
    parsed = dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=dt.timezone.utc)
    require(parsed.date() >= dt.date.fromisoformat(OWNER_DATE), 'recording precedes owner answer')
    require(dt.date.fromisoformat(OWNER_DATE) > dt.date(2026, 10, 2), 'owner act does not follow predecessor date')
    return parsed


def strict_json(body: bytes):
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, f'duplicate JSON key: {key}')
            out[key] = value
        return out
    return json.loads(body, object_pairs_hook=pairs)


def validate(root: pathlib.Path, applied: bool) -> tuple[str, str, str, bytes]:
    frozen_files(root)
    predecessor((root / PREDECESSOR).read_text())
    approval((root / DIRECTION).read_text())
    manifest = (root / build.MANIFEST).read_bytes()
    rows = build.ROW_RE.findall(manifest.decode())
    require(len(rows) == 1 and rows[0][1] == build.SUBJECT.as_posix(), 'manifest row population differs')
    body = (root / build.SUBJECT).read_bytes()
    base, state = build.base_and_state(body)
    require(state == ('applied' if applied else 'unapplied'), 'subject is not in the required transaction state')
    require(sha(base) == BASE_DIGEST, 'subject is not the exact act-B base')
    proposed = build.proposed_bytes(base)
    strict_json(base)
    strict_json(proposed)
    require(build.json_findings(base, proposed) == [], 'not exactly the approved JSON leaf')
    require(sha(proposed) == rows[0][0], 'proposed bytes differ from manifest row')
    require((root / build.PATCH).read_text() == build.render_patch(base, proposed), 'patch differs from exact regeneration')
    findings, actual_state = build.check(root)
    require(not findings, 'builder: ' + '; '.join(findings))
    require(actual_state == state, 'builder state differs')
    reviewed, verdict = review((root / RAW).read_text(), sha(manifest), (root / DISPOSITION).read_text())
    return rows[0][0], reviewed, verdict, proposed


def heading() -> str:
    return f'## PWB registry machine-ceiling amendment — performed {OWNER_DATE}'


def render(argument: str, reviewed: str, verdict: str, recorded: str) -> tuple[bytes, bytes]:
    instant(recorded)
    record = f'''# Owner act — Polaris Butlers observer registry machine ceiling

Date: {OWNER_DATE}

Recorded at (UTC): {recorded}

Owner: Tzeusy

Act identity: `{IDENTITY}`

Act type: `adopt-registry-entry`

Project identity: `project:syzygy`

Artifact identity: `{build.SUBJECT.as_posix()}`

Exact digest (SHA-256): `{argument}`

Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),
{EXPLICIT}

Supersession / revocation: this act supersedes, for the `adopt-registry-entry` role only, the 2026-10-02 act recorded at `{PREDECESSOR.as_posix()}`.
That predecessor, its argument, its tag and the bytes it bound remain immutable
history. Revocation requires a later exact owner act naming this act.

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

[Observed] The attended Codex offer and paired answer are recorded at
`{DIRECTION.as_posix()}`. Its second offer named
`{build.NEW_TAG}` and the exact Ask 2 implementation scope of
`{(PKG / 'OWNER-DECISION-PACKET.md').as_posix()}`. The linked offered item
`p114-ceiling-transaction`, option A, selected that version and all five
implementation items in the same exchange. On {OWNER_DATE} the owner replied:

> {OWNER_WORDS}

The other offered action is separate and adds no scope to this act. Under
`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, this
selection binds the named version and its one manifest row. The owner did
not type the derived phrase below or its digest. This is the phrase the act
takes, derived from the row at recording:

```text
{PREFIX}: {argument}
```

The retained raw `{RAW.as_posix()}` returned `{verdict}`. Its head binds the
manifest FILE digest; the row binds the registry bytes. Reviewed commit
`{reviewed}` is provenance. The three notes are preserved in
`{DISPOSITION.as_posix()}`. The eight proposal files remain unchanged.

- recording tag: `{build.NEW_TAG}`, on the main commit carrying this
  record and the coherent applied implementation. A tag alone proves neither
human attendance nor successful behavior. This record is owner-trusted,
uncorrelated under RFC3-16(c), never independently verified.

## Effect

The registry entry `polaris-butlers-project-shape`, version
`1.2.0-candidate.1`, discovery version `pwb-discovery-v2-candidate.1`, is
adopted in `.syzygy/governance/declarations/adapter-registry` for
`project:syzygy` and `repository:butlers-configured-poc`, with `read-only`
authority and an `empty write surface`. Only
`entries[0].resourceLimits.maxMachineResponseBytes` changes, from 8,388,608
to 16,777,216. Every other byte stays the same. The paired implementation
authorization is exactly Ask 2 items 1–5 in the canonical direction.

This act adds no repository consent, source class, read, write, execution,
egress, deployment, release or live activation. The other authority roles
remain separate. It establishes no runtime result, current outage or
capacity forecast; the motivating size evidence is a historical incident.
'''
    block = f'''{heading()}

The owner selected `{build.NEW_TAG}` and its exact paired Ask 2 items 1–5
on {OWNER_DATE}, replying `{OWNER_WORDS}` in the attended Codex conversation
recorded at `{DIRECTION.as_posix()}`. The owner did not type this derived
phrase; its argument is the package manifest's single registry row:

```text
{PREFIX}: {argument}
```

| Field | Record |
|---|---|
| Subject | `{build.SUBJECT.as_posix()}` |
| Dedicated record | `{RECORD.as_posix()}` |
| Version tag | `{build.NEW_TAG}` on the main commit carrying the record |
| Review | `{RAW.as_posix()}` — `{verdict}`, notes 1–3 retained separately |
| Provenance | owner-adopted (bootstrap, uncorrelated), state (1); A1 explicitly absent; never independently verified |
| Supersession | registry role only, predecessor `{PREDECESSOR.as_posix()}` unchanged |
| Recorded at (UTC) | {recorded} |

[Observed] The bounded owner selection is recorded. Implementation, gate
admission and private response measurement require their separate evidence.
'''
    return record.encode(), block.encode()


def expected(root: pathlib.Path, recorded: str, applied: bool) -> tuple[bytes, bytes, bytes]:
    argument, reviewed, verdict, proposed = validate(root, applied)
    record, block = render(argument, reviewed, verdict, recorded)
    return proposed, record, block


def exact_record(body: bytes, argument: str) -> str:
    """The owning recorder's complete, bounded record predicate.

    Historical recovery uses this same predicate: a duplicate, malformed or
    contradictory field cannot become a different interpretation of the act.
    The timestamp is preserved, not generated again for a historical check.
    """
    recorded = unique(body.decode(), RECORDED.pattern, 'recording instant')
    expected_body, _ = render(argument, FROZEN_SUBJECT, 'CONFIRM WITH EXCEPTIONS', recorded)
    require(body == expected_body, 'dedicated record differs from exact regeneration')
    return recorded


def stage(path: pathlib.Path, body: bytes) -> pathlib.Path:
    fd, name = tempfile.mkstemp(prefix='.p114-', dir=path.parent)
    temp = pathlib.Path(name)
    try:
        with os.fdopen(fd, 'wb') as out:
            out.write(body)
        if path.exists():
            temp.chmod(path.stat().st_mode & 0o777)
        return temp
    except BaseException:
        temp.unlink(missing_ok=True)
        raise


def transaction(root: pathlib.Path, outputs: dict[pathlib.Path, bytes], *,
                before: dict[pathlib.Path, bytes | None], replace=os.replace, write_stage=stage) -> None:
    require(before.keys() == outputs.keys(), 'transaction input population differs')
    staged: dict[pathlib.Path, pathlib.Path] = {}
    changed: list[pathlib.Path] = []

    def unchanged(rel):
        actual = (root / rel).read_bytes() if (root / rel).exists() else None
        require(actual == before[rel], f'transaction input changed: {rel}')

    try:
        # These are the inputs captured before validation/output construction,
        # never a later snapshot that could adopt an intervening write.
        for rel in outputs:
            unchanged(rel)
        for rel, body in outputs.items():
            staged[rel] = write_stage(root / rel, body)
        for rel in outputs:
            unchanged(rel)
        for rel, temp in staged.items():
            unchanged(rel)
            replace(temp, root / rel)
            changed.append(rel)
    except BaseException:
        for rel in reversed(changed):
            if before[rel] is None:
                (root / rel).unlink(missing_ok=True)
            else:
                backup = stage(root / rel, before[rel])
                os.replace(backup, root / rel)
        raise
    finally:
        for temp in staged.values():
            temp.unlink(missing_ok=True)


def record(root: pathlib.Path, now: dt.datetime | None = None, **faults) -> None:
    before = {rel: (root / rel).read_bytes() if (root / rel).exists() else None
              for rel in (build.SUBJECT, RECORD, AGGREGATE)}
    require(before[RECORD] is None, 'dedicated act already exists')
    aggregate = before[AGGREGATE]
    require(aggregate is not None, 'aggregate record is missing')
    require(heading().encode() not in aggregate, 'aggregate act already exists')
    now = now or dt.datetime.now(dt.timezone.utc)
    require(now.tzinfo == dt.timezone.utc, 'recording clock is not UTC')
    recorded = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    proposed, body, block = expected(root, recorded, applied=False)
    require(before[build.SUBJECT] == build.base_and_state(proposed)[0],
            'validated subject differs from the captured input')
    transaction(root, {build.SUBJECT: proposed, RECORD: body,
                       AGGREGATE: aggregate + (b'\n' if aggregate.endswith(b'\n') else b'\n\n') + block},
                before=before, **faults)


def check(root: pathlib.Path) -> None:
    require((root / RECORD).is_file(), 'dedicated act is missing')
    actual = (root / RECORD).read_bytes()
    recorded = unique(actual.decode(), RECORDED.pattern, 'recording instant')
    proposed, body, block = expected(root, recorded, applied=True)
    exact_record(actual, sha(proposed))
    require(actual == body, 'dedicated record differs from exact regeneration')
    aggregate = (root / AGGREGATE).read_bytes()
    require(aggregate.count(heading().encode()) == 1 and aggregate.count(block) == 1,
            'aggregate does not carry exactly one complete act block')
    require((root / build.SUBJECT).read_bytes() == proposed, 'installed bytes differ')


def builder_selftest() -> int:
    import pwb_signed_selftest as helper
    frozen_files(ROOT)
    replay = helper.rerun_before_signoff(str(ROOT / 'scripts/build_pwb_registry_machine_ceiling_amendment.py'),
                                       RECORD.as_posix(), SELFTEST_BASE)
    return build.selftest() if replay is None else replay


def selftest() -> int:
    results: list[tuple[str, bool]] = []
    raw = (ROOT / RAW).read_text()
    notes = (ROOT / DISPOSITION).read_text()
    manifest_sha = sha((ROOT / build.MANIFEST).read_bytes())
    direction = (ROOT / DIRECTION).read_text()
    pred = (ROOT / PREDECESSOR).read_text()

    def rejects(name, fn, needle):
        try:
            fn()
        except (ValueError, build.Refusal, OSError) as exc:
            passed = needle in str(exc)
            if not passed:
                print(f'  {name}: unexpected refusal {exc}')
        else:
            passed = False
        results.append((name, passed))

    results.append(('notes-only review and retained note adapter accept', review(raw, manifest_sha, notes) == (FROZEN_SUBJECT, 'CONFIRM WITH EXCEPTIONS')))
    approval(direction)
    predecessor(pred)
    results.append(('actual paired selection and date-only predecessor accept', True))
    for old, new, why in [
        ('Manifest SHA-256: ' + manifest_sha, 'Manifest SHA-256: ' + BASE_DIGEST, 'manifest FILE'),
        ('Verdict: CONFIRM WITH EXCEPTIONS', 'Verdict: REVISE', 'notes-only verdict'),
        ('Reviewed commit: ' + FROZEN_SUBJECT, 'Reviewed commit: ' + '0' * 40, 'review commit differs'),
        ('**Finding 1 —', '**Finding 4 —', 'exactly notes'),
        ('**Finding 2 —', '**Issue 2 —', 'finding'),
        ('** (note)', '** (revise)', 'exactly notes'),
    ]:
        require(old in raw, f'selftest raw mutation target absent: {old}')
        rejects('review mutation: ' + why, lambda old=old, new=new: review(raw.replace(old, new, 1), manifest_sha, notes), why)
    for changed in [notes.replace(RAW.as_posix(), 'wrong-RAW.md'), notes.replace('2. **', '1. **'), notes.replace('3. **', '4. **')]:
        rejects('retained-note identity/population mutation', lambda changed=changed: review(raw, manifest_sha, changed), 'disposition')
    for changed in [direction.replace(OWNER_WORDS, 'yes'), direction.replace('Ask 2 implementation scope.', 'implementation only.'), direction.replace(build.NEW_TAG, 'other-v1.0'), direction.replace('5. This sign-off', '6. This sign-off')]:
        require(changed != direction, 'selftest approval mutation target absent')
        rejects('paired approval mutation', lambda changed=changed: approval(changed), 'differ' if '6. This sign-off' in changed else 'offer' if 'implementation only.' in changed or 'other-v1.0' in changed else 'reply')
    for changed in [pred.replace('Date: 2026-10-02', 'Date: 2026-10-03'), pred + '\nExact digest (SHA-256): `' + BASE_DIGEST + '`\n', pred.replace(build.ACT_B_IDENTITY, 'wrong')]:
        rejects('predecessor date/digest/identity mutation', lambda changed=changed: predecessor(changed), 'predecessor')
    for changed in ['2026-10-21', '2026-10-20T12:00:00+00:00', '2026-10-19T23:59:59Z']:
        rejects('recording UTC/date mutation', lambda changed=changed: instant(changed), 'recording')
    rejects('duplicate JSON key', lambda: strict_json(b'{"x":1,"x":2}'), 'duplicate JSON')

    def fixture(root):
        for rel in [*map(pathlib.Path, FROZEN_FILES), build.SUBJECT, build.CONSTANT_FILE, build.GATE_FILE, AGGREGATE]:
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, root / rel)
        base, _ = build.base_and_state((root / build.SUBJECT).read_bytes())
        (root / build.SUBJECT).write_bytes(base)
        build._set_constant(root / build.CONSTANT_FILE, build.OLD_VALUE)
        gate = (root / build.GATE_FILE).read_text()
        # Set each named object separately: current and predecessor share a path after install.
        for name, value in [('PWB_ACT_RECORDS', build.ACT_B_RECORD), ('PWB_SUPERSEDED_ACT_RECORDS', build.CURRENCY_RECORD)]:
            block = build.object_block(gate, name)
            require(block is not None, 'fixture gate block absent')
            old = build._quoted(block, 'registry')[0]
            start = gate.index('export const ' + name)
            end = gate.index('\n};', start)
            part = gate[start:end].replace(f"registry: '{old}'", f"registry: '{value}'")
            gate = gate[:start] + part + gate[end:]
        gate = gate.replace(IDENTITY, build.ACT_B_IDENTITY).replace(build.NEW_TAG, build.ACT_B_TAG)
        (root / build.GATE_FILE).write_text(gate)
        aggregate = (root / AGGREGATE).read_bytes()
        if heading().encode() in aggregate:
            aggregate = aggregate.split(heading().encode(), 1)[0].rstrip() + b'\n'
        (root / AGGREGATE).write_bytes(aggregate)

    with tempfile.TemporaryDirectory() as temp:
        clean = pathlib.Path(temp) / 'clean'
        fixture(clean)
        validate(clean, False)
        results.append(('unapplied accepting control verifies', True))
        for rel in FROZEN_FILES:
            original = (clean / rel).read_bytes()
            (clean / rel).write_bytes(original + b'\n')
            rejects('frozen-file drift: ' + rel, lambda: frozen_files(clean), 'frozen source')
            (clean / rel).write_bytes(original)
        for old, new in [(build.OLD, build.OLD + b'\n' + build.OLD), (b'"schemaVersion": 1', b'"schemaVersion": 2')]:
            original = (clean / build.SUBJECT).read_bytes()
            require(old in original, 'subject mutation target absent')
            (clean / build.SUBJECT).write_bytes(original.replace(old, new, 1))
            rejects('subject exact-base mutation', lambda: validate(clean, False), 'subject')
            (clean / build.SUBJECT).write_bytes(original)
        before = {rel: (clean / rel).read_bytes() if (clean / rel).exists() else None for rel in [build.SUBJECT, RECORD, AGGREGATE]}
        now = dt.datetime(2026, 10, 21, 0, 1, tzinfo=dt.timezone.utc)
        real_transaction = transaction
        for window in ['before transaction', 'during staging']:
            for drift_rel in before:
                foreign = ((before[drift_rel] or b'') + b'\nOwner-preserved concurrent input.\n')
                def early(root, outputs, **kwargs):
                    (root / drift_rel).write_bytes(foreign)
                    return real_transaction(root, outputs, **kwargs)
                staged_calls = [0]
                def staging(path, body):
                    temp_path = stage(path, body)
                    staged_calls[0] += 1
                    if staged_calls[0] == 3:
                        (clean / drift_rel).write_bytes(foreign)
                    return temp_path
                try:
                    if window == 'before transaction':
                        globals()['transaction'] = early
                    rejects(f'input drift {window}: {drift_rel}',
                            lambda: record(clean, now, **({'write_stage': staging} if window == 'during staging' else {})),
                            'transaction input changed')
                finally:
                    globals()['transaction'] = real_transaction
                after = {rel: (clean / rel).read_bytes() if (clean / rel).exists() else None for rel in before}
                wanted = {**before, drift_rel: foreign}
                results.append((f'input drift {window}: preserve foreign bytes and other inputs: {drift_rel}',
                                after == wanted and not list(clean.rglob('.p114-*'))))
                for rel, original in before.items():
                    if original is None:
                        (clean / rel).unlink(missing_ok=True)
                    else:
                        (clean / rel).write_bytes(original)
        replaced_calls = [0]
        foreign = before[AGGREGATE] + b'\nOwner-preserved concurrent aggregate note.\n'
        def drift_after_first_replace(source, target):
            os.replace(source, target)
            replaced_calls[0] += 1
            if replaced_calls[0] == 1:
                (clean / AGGREGATE).write_bytes(foreign)
        rejects('input drift after first replacement',
                lambda: record(clean, now, replace=drift_after_first_replace), 'transaction input changed')
        after = {rel: (clean / rel).read_bytes() if (clean / rel).exists() else None for rel in before}
        results.append(('late drift restores owned outputs and preserves foreign aggregate',
                        after == {**before, AGGREGATE: foreign} and not list(clean.rglob('.p114-*'))))
        (clean / AGGREGATE).write_bytes(before[AGGREGATE])
        for seam in ['stage', 'replace']:
            for fail_at in [1, 2, 3]:
                calls = [0]
                real = stage if seam == 'stage' else os.replace
                def failing(*args):
                    calls[0] += 1
                    if calls[0] == fail_at:
                        raise OSError('injected transaction failure')
                    return real(*args)
                rejects(f'{seam} {fail_at} refuses', lambda: record(clean, now, **{'write_stage' if seam == 'stage' else 'replace': failing}), 'injected')
                after = {rel: (clean / rel).read_bytes() if (clean / rel).exists() else None for rel in before}
                results.append((f'{seam} {fail_at} restores exact prior population/bytes', after == before and not list(clean.rglob('.p114-*'))))
        record(clean, now)
        build._set_constant(clean / build.CONSTANT_FILE, build.NEW_VALUE)
        gate = (clean / build.GATE_FILE).read_text()
        gate = gate.replace(f"registry: '{build.ACT_B_RECORD}'", f"registry: '{RECORD.as_posix()}'", 1)
        gate = gate.replace(f"registry: '{build.CURRENCY_RECORD}'", f"registry: '{build.ACT_B_RECORD}'", 1)
        gate = gate.replace(build.ACT_B_IDENTITY, IDENTITY).replace(build.ACT_B_TAG, build.NEW_TAG)
        (clean / build.GATE_FILE).write_text(gate)
        check(clean)
        results.append(('record, patch, exact regeneration and aggregate accepting control', True))
        rejects('second act refuses', lambda: record(clean, now), 'already exists')
        saved = (clean / RECORD).read_bytes()
        (clean / RECORD).write_bytes(saved.replace(EXPLICIT.encode(), b'not ' + EXPLICIT.encode()))
        rejects('changed approval provenance refuses', lambda: check(clean), 'regeneration')
        (clean / RECORD).write_bytes(saved)
        saved = (clean / AGGREGATE).read_bytes()
        (clean / AGGREGATE).write_bytes(saved + render(validate(clean, True)[0], FROZEN_SUBJECT, 'CONFIRM WITH EXCEPTIONS', now.strftime('%Y-%m-%dT%H:%M:%SZ'))[1])
        rejects('duplicate complete aggregate refuses', lambda: check(clean), 'exactly one')
        (clean / AGGREGATE).write_bytes(saved.replace(heading().encode(), b'## Other act'))
        rejects('missing aggregate block refuses', lambda: check(clean), 'exactly one')
    for name, passed in results:
        print(f'{"PASS" if passed else "FAIL"} {name}')
    failures = sum(not passed for _, passed in results)
    print(f'{len(results)} P-114 recorder fixtures, {failures} failing')
    return int(bool(failures))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    for name in ['record', 'check', 'selftest', 'builder-selftest']:
        mode.add_argument('--' + name, action='store_true')
    args = parser.parse_args()
    try:
        if args.selftest:
            return selftest()
        if args.builder_selftest:
            return builder_selftest()
        if args.record:
            record(ROOT)
            print('Recorded the paired P-114 act, exact patch and one aggregate block; no tag created. Complete approved code before serving.')
        else:
            check(ROOT)
            print('P-114 record, approved registry row, retained review/selection and one aggregate block regenerate exactly.')
    except (ValueError, build.Refusal, OSError) as exc:
        print(f'FAILED: {exc}')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
