#!/usr/bin/env node
// Build the evidence record for one end-to-end Polaris dossier run (syzygy-qkea.13, S12), from its run directory and session
// directories, with every digest computed here (verification rule 3) and the subject and its digests named (rule 11).
//
//   node scripts/dossier_run_evidence.mjs <run directory> > docs/evidence/polaris-dossier-s12-<tool>-<date>.json
//
// It reads only the run directory, the sibling <run id>.sessions directory and this checkout's Git state. It copies no file body:
// each file appears as its path, size and sha256. What only the operator knows (that the owner attended, which launch form was
// used, what the agent tool showed) is left as an `operatorDeclared` block to fill in by hand, labelled Inferred. Not authority.
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';

const FORMAT = 'polaris-dossier-run-evidence/1';
const CHECKOUT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function fail(message) {
  process.stderr.write(`dossier_run_evidence: ${message}\n`);
  process.exit(2);
}

const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');

/** Every regular file under `root`, sorted, as { path, bytes, sha256 }; symbolic links and other entries are listed, never followed. */
function inventory(root) {
  const files = [];
  const others = [];
  const walk = (dir) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0))) {
      const full = path.join(dir, entry.name);
      const relative = path.relative(root, full);
      if (entry.isDirectory()) walk(full);
      else if (entry.isFile()) {
        const bytes = fs.readFileSync(full);
        files.push({ path: relative, bytes: bytes.length, sha256: sha256(bytes) });
      } else others.push({ path: relative, kind: entry.isSymbolicLink() ? 'symbolic link, not followed' : 'not a regular file' });
    }
  };
  walk(root);
  return { files, others };
}

function readJson(file) {
  try { return JSON.parse(fs.readFileSync(file, 'utf8')); } catch { return undefined; }
}

const git = (...args) => execFileSync('git', ['-C', CHECKOUT, ...args], { encoding: 'utf8' }).trim();

const runArg = process.argv[2];
if (runArg === undefined || process.argv.length !== 3) fail('usage: node scripts/dossier_run_evidence.mjs <run directory>');
const run = path.resolve(runArg);
if (!fs.statSync(run, { throwIfNoEntry: false })?.isDirectory()) fail(`${run} is not a directory`);
const runRecord = readJson(path.join(run, 'run.json'));
if (runRecord === undefined || typeof runRecord !== 'object' || runRecord === null) fail(`${run} holds no readable run.json`);
const sessions = `${run}.sessions`;

const brief = readJson(path.join(run, 'brief.json'));
const record = readJson(path.join(run, 'record.json'));
const sites = fs.existsSync(path.join(run, 'site')) ? fs.readdirSync(path.join(run, 'site')).filter((name) => /^(0|[1-9][0-9]*)$/u.test(name)).map(Number).sort((a, b) => a - b) : [];
const latestSite = sites.length === 0 ? null : sites[sites.length - 1];
const machine = latestSite === null ? null : path.join(run, 'site', String(latestSite), 'machine.json');
const status = git('status', '--porcelain', '--untracked-files=no');

const evidence = {
  format: FORMAT,
  record: 'One end-to-end Polaris dossier run in the operator-agent mode (syzygy-qkea.13, S12): its subject, the Syzygy commit that ran it, and the digest of every file the run left in its run and session directories. Built by scripts/dossier_run_evidence.mjs; no file body is copied. Not authority.',
  measuredOn: {
    syzygyCommit: git('rev-parse', 'HEAD'),
    syzygyTrackedTreeClean: status === '',
  },
  subject: {
    runId: path.basename(run),
    repository: runRecord.subject?.repository ?? null,
    pinnedRevision: runRecord.subject?.pinnedRevision ?? null,
    governed: runRecord.subject?.governed ?? null,
    label: 'Inferred',
    basis: 'read from the run record, which the agent sessions can write',
  },
  declared: { values: runRecord.declared ?? null, declaredBy: 'operator', label: 'Inferred' },
  executionRule: brief?.executionRule ?? { why: 'brief.json cannot be read' },
  outcome: {
    briefed: brief !== undefined,
    sites,
    latestSiteMachineSha256: machine !== null && fs.existsSync(machine) ? sha256(fs.readFileSync(machine)) : null,
    closed: record !== undefined,
    executionRecordSha256: record === undefined ? null : sha256(fs.readFileSync(path.join(run, 'record.json'))),
    agentUsage: record?.agentUsage ?? null,
    credential: record?.credential?.atClose ?? null,
  },
  runDirectory: inventory(run),
  sessionsDirectory: fs.existsSync(sessions) ? inventory(sessions) : { files: [], others: [], why: `${path.basename(sessions)} does not exist` },
  operatorDeclared: {
    label: 'Inferred',
    declaredBy: 'operator',
    fillIn: 'Enter by hand after the run; leave a field null when unknown, never guess.',
    ownerAttendedEverySession: null,
    authoringLaunch: null,
    launchForms: null,
    agentToolVersionShown: null,
    usageShownByTheTool: null,
    notes: null,
  },
};
process.stdout.write(`${JSON.stringify(evidence, null, 2)}\n`);
