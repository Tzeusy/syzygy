import * as net from 'node:net';

/** The `syzygy` command inside a launched session's view (candidate REQ-polaris-generation-041). It forwards its arguments, and its
 * standard input when `--stdin` is given, to the run's broker over the session's socket, then prints what the broker returns and exits
 * with its status. It runs nothing itself. Standalone: no package imports, so the view needs only node and this file. */

async function main(): Promise<number> {
  const socket = process.env['SYZYGY_BROKER_SOCKET'];
  if (socket === undefined || socket === '') {
    process.stderr.write('syzygy: no broker socket; this command works only inside a launched session\n');
    return 2;
  }
  const argv = process.argv.slice(2);
  let stdin: string | undefined;
  if (argv.includes('--stdin')) {
    const chunks: Buffer[] = [];
    for await (const chunk of process.stdin) chunks.push(chunk as Buffer);
    stdin = Buffer.concat(chunks).toString('base64');
  }
  return new Promise<number>((resolve) => {
    const connection = net.createConnection(socket);
    let reply = '';
    connection.setEncoding('utf8');
    connection.on('connect', () => connection.write(`${JSON.stringify({ argv, ...(stdin === undefined ? {} : { stdin }) })}\n`));
    connection.on('data', (chunk: string) => { reply += chunk; });
    connection.on('error', (cause) => { process.stderr.write(`syzygy: the run's broker cannot be reached (${cause.message}); the run may have stopped\n`); resolve(2); });
    connection.on('end', () => {
      try {
        const response = JSON.parse(reply) as { stdout: string; stderr: string; exit: number };
        process.stdout.write(response.stdout);
        process.stderr.write(response.stderr);
        resolve(response.exit);
      } catch {
        process.stderr.write('syzygy: the broker sent no readable reply\n');
        resolve(2);
      }
    });
  });
}

void main().then((code) => { process.exitCode = code; });
