import { createServer } from 'node:http';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const args = process.argv.slice(2);
const value = name => args[args.indexOf(name) + 1];
const repo = value('--repo');
const stateDir = value('--state-dir');
const port = Number(value('--port'));
if (!repo || !stateDir || !Number.isSafeInteger(port)) process.exit(2);
if (existsSync(join(repo, 'fail-next'))) process.exit(3);
mkdirSync(stateDir, { recursive: true });
const credential = join(stateDir, 'machine-credential.token');
if (!existsSync(credential)) writeFileSync(credential, 'private-fixture-credential', { mode: 0o600, flag: 'wx' });
const revision = readFileSync(join(repo, 'revision'), 'utf8');
const server = createServer((_request, response) => {
  response.writeHead(200, { 'content-type': 'text/plain' });
  response.end(revision);
});
server.listen(port, '127.0.0.1');
let closing = false;
process.on('SIGTERM', () => {
  if (closing) return;
  closing = true;
  const close = () => server.close(() => process.exit(0));
  if (existsSync(join(repo, 'hold-stop'))) {
    if (!existsSync(join(repo, 'shutdown-started'))) {
      writeFileSync(join(repo, 'shutdown-started'), 'SIGTERM received', { flag: 'wx' });
    }
    const poll = setInterval(() => {
      if (existsSync(join(repo, 'release-stop'))) {
        clearInterval(poll);
        close();
      } else if (existsSync(join(repo, 'hold-probe')) && !existsSync(join(repo, 'hold-ack'))) {
        // The acknowledgement proves the listener is still held open after
        // SIGTERM, so the test can attempt a concurrent restart without a
        // wall-clock scheduling assumption.
        writeFileSync(join(repo, 'hold-ack'), 'socket held', { flag: 'wx' });
      }
    }, 10);
  } else if (existsSync(join(repo, 'slow-stop'))) setTimeout(close, 250);
  else close();
});
