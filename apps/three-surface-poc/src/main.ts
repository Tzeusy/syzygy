import { main } from './poc-main.js';

// The unconditional entry: `node dist/main`, `node dist/main.js` and the
// package directory all run the POC, as the script did before `main` was
// extracted. Everything testable lives in `poc-main.ts`, which has no
// import-time effect.
process.exitCode = await main(process.argv.slice(2), {
  stdout: process.stdout,
  stderr: process.stderr,
  stdin: process.stdin,
  cwd: () => process.cwd(),
  now: () => new Date().toISOString(),
  onSignal: (signal, listener) => { process.on(signal, listener); },
});
