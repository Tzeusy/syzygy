// `npm run poc:keyboard-sweep -- --base-url <private daemon>` — the
// keyboard sweep of the served Polaris page (syzygy-1z3.30; PWB-REQ-016,
// a prerequisite of the task 4.6 cold-open walkthrough).
//
// `poc:accessibility-check` sweeps fixture variants; this sweeps the page
// a reader is actually served. It fetches `/polaris` from a running private
// daemon twice — directly, and with the tailnet Host header `tailscale
// serve` forwards (the mount form) — retains both bodies in a private
// temporary directory, runs `checkPolarisAccessibility` over each in a real
// headless browser, and writes a dated evidence record: per mount the
// served digest, the focusable population and how much of it Tab reached,
// the fragment activations, and the violations by kind. `--file` sweeps a
// retained capture instead of a live daemon.
//
// It reads no Butlers repository itself; the daemon (`main.ts`) never
// imports it. Exits 0 only when every swept page has zero violations.
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import * as http from 'node:http';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { TAILNET_HOST } from './browser-origin.js';
import { findBrowserExecutable, launchBrowser } from './cdp-browser.js';
import { defaultRunGit } from './governance-inputs.js';
import { checkPolarisAccessibility, type AccessibilityReport } from './polaris-accessibility.js';
import { POLARIS_HUMAN_PATH } from './polaris.js';
import { pwbSurfaceVersion } from './walkthrough-inputs.js';

const USAGE = 'usage: npm run poc:keyboard-sweep -- (--base-url http://127.0.0.1:<port> | --file <capture.html> [--file …]) [--date YYYY-MM-DD[-suffix]] [--out <record.json>]\n';

function argument(name: string): string | undefined {
  const index = process.argv.indexOf(name);
  return index === -1 ? undefined : process.argv[index + 1];
}

function argumentsNamed(name: string): string[] {
  return process.argv.flatMap((value, index) => (value === name && process.argv[index + 1] !== undefined ? [process.argv[index + 1] as string] : []));
}

/** GET with an explicit Host header — the Fetch API drops a set Host. */
function get(baseUrl: string, path: string, host?: string): Promise<{ readonly status: number; readonly body: Buffer }> {
  return new Promise((resolvePromise, reject) => {
    const url = new URL(path, baseUrl);
    const request = http.get(url, { headers: host === undefined ? {} : { Host: host } }, (response) => {
      const chunks: Buffer[] = [];
      response.on('data', (chunk: Buffer) => chunks.push(chunk));
      response.on('end', () => resolvePromise({ status: response.statusCode ?? 0, body: Buffer.concat(chunks) }));
      response.on('error', reject);
    });
    request.on('error', reject);
  });
}

interface Sweep {
  readonly mount: string;
  readonly source: Readonly<Record<string, unknown>>;
  readonly bytes: number;
  readonly sha256: string;
  readonly report: AccessibilityReport;
}

function violationsByKind(report: AccessibilityReport): Record<string, number> {
  const kinds: Record<string, number> = {};
  for (const violation of report.violations) kinds[violation.kind] = (kinds[violation.kind] ?? 0) + 1;
  return kinds;
}

async function main(): Promise<number> {
  const baseUrl = argument('--base-url');
  const files = argumentsNamed('--file');
  if ((baseUrl === undefined) === (files.length === 0)) {
    process.stderr.write(USAGE);
    return 2;
  }
  const executable = findBrowserExecutable();
  if (executable === undefined) {
    process.stderr.write('No Chrome/Chromium found on PATH and SYZYGY_POC_BROWSER is unset; nothing measured.\n');
    return 2;
  }
  const date = argument('--date') ?? new Date().toISOString().slice(0, 10);
  const output = argument('--out') ?? join('docs', 'evidence', `polaris-keyboard-sweep-${date}.json`);
  const repoRoot = resolve('.');
  const head = execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();

  const pages = mkdtempSync(join(tmpdir(), 'syzygy-poc-keyboard-sweep-'));
  const targets: { readonly mount: string; readonly source: Readonly<Record<string, unknown>>; readonly body: Buffer }[] = [];
  try {
    if (baseUrl !== undefined) {
      for (const [mount, host] of [['direct', undefined], ['tailnet', TAILNET_HOST]] as const) {
        const response = await get(baseUrl, POLARIS_HUMAN_PATH, host);
        if (response.status !== 200) {
          process.stderr.write(`${mount} ${POLARIS_HUMAN_PATH} answered ${response.status}; nothing swept.\n`);
          return 1;
        }
        targets.push({ mount, source: { path: POLARIS_HUMAN_PATH, host: host ?? new URL(baseUrl).host, status: response.status }, body: response.body });
      }
    } else {
      for (const file of files) targets.push({ mount: `file:${file}`, source: { file }, body: readFileSync(file) });
    }

    const browser = await launchBrowser(executable);
    const sweeps: Sweep[] = [];
    try {
      for (const [index, target] of targets.entries()) {
        const file = join(pages, `polaris-${index}.html`);
        writeFileSync(file, target.body);
        const page = await browser.newPage();
        try {
          const report = await checkPolarisAccessibility(page, pathToFileURL(file).href, target.mount);
          sweeps.push({ mount: target.mount, source: target.source, bytes: target.body.byteLength, sha256: createHash('sha256').update(target.body).digest('hex'), report });
          process.stdout.write(`${target.mount}: focusables ${report.focusTrace.reached}/${report.focusTrace.population}, activations ${report.activations.length}, violations ${report.violations.length} ${JSON.stringify(violationsByKind(report))}\n`);
        } finally {
          await page.close();
        }
      }
    } finally {
      await browser.close();
    }

    const violations = sweeps.reduce((sum, sweep) => sum + sweep.report.violations.length, 0);
    const evidence = {
      task: 'syzygy-1z3.30 (PWB task 4.6 prerequisite: the keyboard sweep of the served Polaris page)',
      requirement: ['PWB-REQ-016'],
      capturedAt: new Date().toISOString(),
      syzygyHead: head,
      surfaceVersion: pwbSurfaceVersion(defaultRunGit, repoRoot, head),
      browser: { executable: browser.executable, version: browser.version },
      method: 'checkPolarisAccessibility over each served body, retained in a private temporary directory and opened as a file URL; fragment activations stay in-document, so the served bytes are the whole input',
      mounts: sweeps.map((sweep) => ({
        mount: sweep.mount,
        source: sweep.source,
        bytes: sweep.bytes,
        sha256: sweep.sha256,
        population: sweep.report.focusTrace.population,
        reached: sweep.report.focusTrace.reached,
        activations: sweep.report.activations.length,
        disclosures: sweep.report.disclosures,
        contrastMeasured: sweep.report.contrast.measured,
        violations: sweep.report.violations.length,
        violationsByKind: violationsByKind(sweep.report),
        firstViolations: sweep.report.violations.slice(0, 5),
      })),
      totals: { mounts: sweeps.length, violations },
    };
    mkdirSync(join('docs', 'evidence'), { recursive: true });
    writeFileSync(output, `${JSON.stringify(evidence, null, 2)}\n`);
    process.stdout.write(`wrote ${output}: ${violations} violations across ${sweeps.length} mounts\n`);
    return violations === 0 ? 0 : 1;
  } finally {
    rmSync(pages, { recursive: true, force: true });
  }
}

main().then(
  (code) => process.exit(code),
  (error: unknown) => {
    process.stderr.write(`${error instanceof Error ? error.stack ?? error.message : String(error)}\n`);
    process.exit(1);
  },
);
