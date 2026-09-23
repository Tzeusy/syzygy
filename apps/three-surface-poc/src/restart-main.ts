import { restartOnePocListener, RestartRefusal } from './restart.js';

const args = process.argv.slice(2);
let port: number | undefined;
let timeoutMs: number | undefined;
for (let index = 0; index < args.length; index += 2) {
  if (args[index] === '--port' && args[index + 1] !== undefined) port = Number(args[index + 1]);
  else if (args[index] === '--timeout-ms' && args[index + 1] !== undefined) timeoutMs = Number(args[index + 1]);
  else { process.stderr.write('Usage: npm run poc:restart -- --port <private-poc-port> [--timeout-ms <100..30000>]\n'); process.exitCode = 2; }
}

if (process.exitCode === undefined) {
  if (port === undefined) {
    process.stderr.write('Usage: npm run poc:restart -- --port <private-poc-port> [--timeout-ms <100..30000>]\n');
    process.exitCode = 2;
  } else {
    try {
      const result = await restartOnePocListener({ port, expectedCwd: process.cwd(), ...(timeoutMs === undefined ? {} : { timeoutMs }) });
      process.stdout.write(`POC listener replaced once on 127.0.0.1:${result.port}; credential/state directory reused.\n`);
    } catch (error) {
      process.stderr.write(`POC restart refused: ${error instanceof RestartRefusal ? error.code : 'unexpected-failure'}\n`);
      process.exitCode = 1;
    }
  }
}
