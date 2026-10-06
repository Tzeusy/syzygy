import * as dgram from 'node:dgram';
import { renderDossier } from '../../../apps/three-surface-poc/src/polaris-generation/dossier-render.js';
import { fullFixtureRun } from '../src/full-run.testkit.js';

/** The process the no-egress proof captures: `node <bundle> <clone> <commit> <state root> [canary]`. It runs one full fixture run through
 * the dossier commands and prints each step's exit status as one JSON line. With `canary`, it first sends one UDP datagram to the
 * loopback discard port, so the proof can show its capture sees a transmission when one is made. Test support only. */

const [clone, commit, stateRoot, mode] = process.argv.slice(2);
if (clone === undefined || commit === undefined || stateRoot === undefined) {
  process.stderr.write('usage: no-egress-driver <clone> <commit> <state root> [canary]\n');
  process.exit(2);
}
if (mode === 'canary') {
  const socket = dgram.createSocket('udp4');
  await new Promise<void>((resolve) => socket.send('canary', 9, '127.0.0.1', () => { socket.close(); resolve(); }));
}
const { run, steps } = await fullFixtureRun({ clone, commit, stateRoot, renderer: renderDossier, closeArgs: ['--usage-turns', '3'] });
process.stdout.write(`${JSON.stringify({ run, steps: steps.map((step) => ({ command: step.argv[0], exit: step.exit })) })}\n`);
