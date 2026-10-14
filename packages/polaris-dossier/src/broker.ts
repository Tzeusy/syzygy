import * as fs from 'node:fs';
import * as net from 'node:net';
import * as path from 'node:path';

/** The command broker of a launched run (candidate REQ-polaris-generation-041, 042).
 *
 * A launched session cannot reach the run directory, so the Syzygy commands it is allowed run outside its view, in the supervisor. Each
 * session has its own Unix socket, bound into its view; the `syzygy` shim inside the view sends its argument list (and standard input, when
 * `--stdin` is given) over that socket, and the broker runs the command only when the session's own allow rule admits it. Identity comes
 * from the socket, never from what the session says. One request per connection: a length-free JSON line in, a JSON line out. */

export interface BrokerRequest { readonly argv: readonly string[]; readonly stdin?: string }
export interface BrokerResponse { readonly stdout: string; readonly stderr: string; readonly exit: number }

/** Run one admitted command, as `runDossierCli` would, with the standard input bytes given. */
export type BrokerRunner = (argv: readonly string[], stdin: Uint8Array | null) => Promise<BrokerResponse>;

/** Whether this session may run this argument list; the refusal text otherwise. */
export type BrokerRule = (argv: readonly string[]) => string | null;

const MAX_REQUEST = 32 * 1024 * 1024;

/** The rule of a helper session: only `syzygy dossier await <its own directory>/ ...`. */
export const awaitRule = (sessionDir: string): BrokerRule => (argv) => {
  const [family, command, target] = argv;
  if (family !== 'dossier' || command !== 'await') return 'this session may run only `syzygy dossier await` on its own directory';
  if (target === undefined || path.resolve(target) !== path.resolve(sessionDir)) return `this session may run await only on ${sessionDir}/`;
  return null;
};

/** The rule of the authoring session: `check` and `status` on its own run, and `help`. */
export const authorRule = (runDir: string): BrokerRule => (argv) => {
  const [family, command, target] = argv.filter((arg) => arg !== '--json');
  if (family !== 'dossier') return 'only `syzygy dossier` commands are available here';
  if (command === 'help') return null;
  if (command !== 'check' && command !== 'status') return 'the authoring session of a launched run may run only `syzygy dossier check` and `status` on its run; Syzygy runs every other step';
  if (target === undefined || path.resolve(target) !== path.resolve(runDir)) return `this session may run ${command} only on its run, ${runDir}`;
  return null;
};

export interface Broker { readonly socket: string; close(): void }

export function startBroker(socket: string, rule: BrokerRule, run: BrokerRunner, log: (line: string) => void): Broker {
  try { fs.unlinkSync(socket); } catch { /* absent */ }
  const server = net.createServer((connection) => {
    let buffer = '';
    connection.setEncoding('utf8');
    connection.on('data', (chunk: string) => {
      buffer += chunk;
      if (buffer.length > MAX_REQUEST) { connection.end(`${JSON.stringify({ stdout: '', stderr: 'request too large\n', exit: 2 })}\n`); return; }
      const newline = buffer.indexOf('\n');
      if (newline < 0) return;
      const line = buffer.slice(0, newline);
      buffer = '';
      void (async () => {
        let response: BrokerResponse;
        try {
          const request = JSON.parse(line) as BrokerRequest;
          const argv = Array.isArray(request.argv) ? request.argv.map(String) : [];
          const refusal = rule(argv);
          if (refusal !== null) {
            log(`refused: syzygy ${argv.join(' ')} — ${refusal}`);
            response = { stdout: '', stderr: `syzygy (launched run): ${refusal}\n`, exit: 1 };
          } else {
            log(`run: syzygy ${argv.join(' ')}`);
            response = await run(argv, typeof request.stdin === 'string' ? new Uint8Array(Buffer.from(request.stdin, 'base64')) : null);
          }
        } catch (cause) {
          response = { stdout: '', stderr: `syzygy (launched run): broker error ${(cause as Error).message}\n`, exit: 2 };
        }
        connection.end(`${JSON.stringify(response)}\n`);
      })();
    });
    connection.on('error', () => { /* the session went away */ });
  });
  server.listen(socket);
  fs.chmodSync(path.dirname(socket), 0o700);
  return { socket, close: () => { server.close(); try { fs.unlinkSync(socket); } catch { /* gone */ } } };
}
