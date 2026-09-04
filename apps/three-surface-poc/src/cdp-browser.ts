// A minimal Chrome DevTools Protocol driver — task 4.4 (syzygy-1z3.20).
//
// PWB-REQ-016's oracle independence asks that DOM/accessibility-tree
// enumeration and input events come from a browser driver outside the
// renderer. This module is that driver with no new dependency: it launches
// a locally installed Chrome/Chromium in headless mode, speaks the DevTools
// protocol over Node's own WebSocket, and exposes exactly what the
// accessibility checks need — navigate, evaluate, real key presses and the
// full accessibility tree. It never touches a Butlers repository and only
// ever opens the `file://` pages the caller writes.

import { spawn, spawnSync, type ChildProcess } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

export interface AxNode {
  readonly nodeId: string;
  readonly ignored: boolean;
  readonly role: string;
  readonly name: string;
  readonly backendDOMNodeId?: number;
  readonly childIds: readonly string[];
}

export type KeyName = 'Tab' | 'Enter';

export interface BrowserPage {
  navigate(url: string): Promise<void>;
  /** Evaluates `expression` in the page and returns its JSON value. */
  evaluate<T>(expression: string): Promise<T>;
  /** Dispatches a real key press (down + up) through the browser's input pipeline. */
  press(key: KeyName, modifiers?: { readonly shift?: boolean }): Promise<void>;
  axTree(): Promise<readonly AxNode[]>;
  /** Closes this page's target; the browser stays open for other pages. */
  close(): Promise<void>;
}

export interface Browser {
  readonly executable: string;
  readonly version: string;
  newPage(): Promise<BrowserPage>;
  close(): Promise<void>;
}

const CANDIDATE_EXECUTABLES = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser'] as const;

/** The browser executable to drive: `SYZYGY_POC_BROWSER` if set, else the
 * first Chrome/Chromium on PATH; `undefined` when none is installed. */
export function findBrowserExecutable(env: NodeJS.ProcessEnv = process.env): string | undefined {
  const named = env['SYZYGY_POC_BROWSER'];
  if (named !== undefined && named !== '') return named;
  for (const candidate of CANDIDATE_EXECUTABLES) {
    const probe = spawnSync('which', [candidate], { encoding: 'utf8' });
    if (probe.status === 0 && probe.stdout.trim() !== '') return probe.stdout.trim();
  }
  return undefined;
}

interface CdpMessage {
  readonly id?: number;
  readonly method?: string;
  readonly params?: unknown;
  readonly result?: unknown;
  readonly error?: { readonly message: string };
  readonly sessionId?: string;
}

const COMMAND_TIMEOUT_MS = 30_000;

class CdpConnection {
  private nextId = 1;
  private readonly pending = new Map<number, { resolve: (value: unknown) => void; reject: (error: Error) => void }>();
  private readonly listeners = new Set<(message: CdpMessage) => void>();

  private constructor(private readonly socket: WebSocket) {
    socket.addEventListener('message', (event) => {
      const message = JSON.parse(String(event.data)) as CdpMessage;
      if (message.id !== undefined) {
        const waiter = this.pending.get(message.id);
        if (waiter === undefined) return;
        this.pending.delete(message.id);
        if (message.error !== undefined) waiter.reject(new Error(`CDP: ${message.error.message}`));
        else waiter.resolve(message.result);
        return;
      }
      for (const listener of this.listeners) listener(message);
    });
  }

  static open(url: string): Promise<CdpConnection> {
    return new Promise((resolve, reject) => {
      const socket = new WebSocket(url);
      socket.addEventListener('open', () => resolve(new CdpConnection(socket)), { once: true });
      socket.addEventListener('error', () => reject(new Error(`CDP: cannot connect to ${url}`)), { once: true });
    });
  }

  send<T>(method: string, params: unknown = {}, sessionId?: string): Promise<T> {
    const id = this.nextId;
    this.nextId += 1;
    return new Promise<T>((resolve, reject) => {
      const timer = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`CDP: ${method} timed out after ${COMMAND_TIMEOUT_MS}ms`));
      }, COMMAND_TIMEOUT_MS);
      this.pending.set(id, {
        resolve: (value) => {
          clearTimeout(timer);
          resolve(value as T);
        },
        reject: (error) => {
          clearTimeout(timer);
          reject(error);
        },
      });
      this.socket.send(JSON.stringify({ id, method, params, ...(sessionId === undefined ? {} : { sessionId }) }));
    });
  }

  waitFor(method: string, sessionId: string): Promise<void> {
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        this.listeners.delete(listener);
        reject(new Error(`CDP: no ${method} event within ${COMMAND_TIMEOUT_MS}ms`));
      }, COMMAND_TIMEOUT_MS);
      const listener = (message: CdpMessage): void => {
        if (message.method === method && message.sessionId === sessionId) {
          clearTimeout(timer);
          this.listeners.delete(listener);
          resolve();
        }
      };
      this.listeners.add(listener);
    });
  }

  close(): void {
    this.socket.close();
  }
}

const KEYS: Record<KeyName, { readonly code: string; readonly keyCode: number; readonly text?: string }> = {
  Tab: { code: 'Tab', keyCode: 9 },
  Enter: { code: 'Enter', keyCode: 13, text: '\r' },
};

interface EvaluateResult {
  readonly result: { readonly value?: unknown };
  readonly exceptionDetails?: { readonly text: string; readonly exception?: { readonly description?: string } };
}

interface RawAxNode {
  readonly nodeId: string;
  readonly ignored: boolean;
  readonly role?: { readonly value?: unknown };
  readonly name?: { readonly value?: unknown };
  readonly backendDOMNodeId?: number;
  readonly childIds?: readonly string[];
}

class CdpPage implements BrowserPage {
  constructor(private readonly connection: CdpConnection, private readonly sessionId: string, private readonly targetId: string) {}

  async close(): Promise<void> {
    await this.connection.send('Target.closeTarget', { targetId: this.targetId });
  }

  async navigate(url: string): Promise<void> {
    const loaded = this.connection.waitFor('Page.loadEventFired', this.sessionId);
    await this.connection.send('Page.navigate', { url }, this.sessionId);
    await loaded;
  }

  async evaluate<T>(expression: string): Promise<T> {
    const outcome = await this.connection.send<EvaluateResult>('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true }, this.sessionId);
    if (outcome.exceptionDetails !== undefined) {
      throw new Error(`page script failed: ${outcome.exceptionDetails.exception?.description ?? outcome.exceptionDetails.text}`);
    }
    return outcome.result.value as T;
  }

  async press(key: KeyName, modifiers: { readonly shift?: boolean } = {}): Promise<void> {
    const spec = KEYS[key];
    const modifierBits = modifiers.shift === true ? 8 : 0;
    const base = { key, code: spec.code, windowsVirtualKeyCode: spec.keyCode, nativeVirtualKeyCode: spec.keyCode, modifiers: modifierBits };
    await this.connection.send('Input.dispatchKeyEvent', { type: spec.text === undefined ? 'rawKeyDown' : 'keyDown', ...base, ...(spec.text === undefined ? {} : { text: spec.text }) }, this.sessionId);
    await this.connection.send('Input.dispatchKeyEvent', { type: 'keyUp', ...base }, this.sessionId);
  }

  async axTree(): Promise<readonly AxNode[]> {
    const tree = await this.connection.send<{ readonly nodes: readonly RawAxNode[] }>('Accessibility.getFullAXTree', {}, this.sessionId);
    return tree.nodes.map((node) => ({
      nodeId: node.nodeId,
      ignored: node.ignored,
      role: typeof node.role?.value === 'string' ? node.role.value : '',
      name: typeof node.name?.value === 'string' ? node.name.value : '',
      ...(node.backendDOMNodeId === undefined ? {} : { backendDOMNodeId: node.backendDOMNodeId }),
      childIds: node.childIds ?? [],
    }));
  }
}

function waitForDevToolsUrl(child: ChildProcess): Promise<string> {
  return new Promise((resolve, reject) => {
    let buffered = '';
    const timer = setTimeout(() => reject(new Error(`browser did not announce a DevTools endpoint within ${COMMAND_TIMEOUT_MS}ms:\n${buffered.slice(-2000)}`)), COMMAND_TIMEOUT_MS);
    child.stderr?.on('data', (chunk: Buffer) => {
      buffered += chunk.toString('utf8');
      const match = /DevTools listening on (ws:\/\/\S+)/.exec(buffered);
      if (match !== null) {
        clearTimeout(timer);
        resolve(match[1] as string);
      }
    });
    child.once('exit', (code) => {
      clearTimeout(timer);
      reject(new Error(`browser exited with ${code ?? 'signal'} before announcing a DevTools endpoint:\n${buffered.slice(-2000)}`));
    });
  });
}

/** Launches `executable` headless with a throwaway profile and connects. */
export async function launchBrowser(executable: string): Promise<Browser> {
  const profile = mkdtempSync(join(tmpdir(), 'syzygy-poc-browser-'));
  const child = spawn(
    executable,
    [
      '--headless=new',
      '--no-sandbox',
      '--disable-gpu',
      '--no-first-run',
      '--no-default-browser-check',
      '--disable-extensions',
      '--disable-background-networking',
      `--user-data-dir=${profile}`,
      '--remote-debugging-port=0',
      '--window-size=1280,2000',
      'about:blank',
    ],
    { stdio: ['ignore', 'ignore', 'pipe'] },
  );
  let connection: CdpConnection;
  try {
    connection = await CdpConnection.open(await waitForDevToolsUrl(child));
  } catch (error) {
    child.kill('SIGKILL');
    rmSync(profile, { recursive: true, force: true });
    throw error;
  }
  const versionInfo = await connection.send<{ readonly product: string }>('Browser.getVersion');
  return {
    executable,
    version: versionInfo.product,
    async newPage(): Promise<BrowserPage> {
      const { targetId } = await connection.send<{ readonly targetId: string }>('Target.createTarget', { url: 'about:blank' });
      const { sessionId } = await connection.send<{ readonly sessionId: string }>('Target.attachToTarget', { targetId, flatten: true });
      await connection.send('Page.enable', {}, sessionId);
      await connection.send('Runtime.enable', {}, sessionId);
      await connection.send('DOM.enable', {}, sessionId);
      await connection.send('Accessibility.enable', {}, sessionId);
      // Keyboard focus must be real: without an emulated focus the page
      // never receives sequential focus navigation in headless mode.
      await connection.send('Emulation.setFocusEmulationEnabled', { enabled: true }, sessionId);
      return new CdpPage(connection, sessionId, targetId);
    },
    async close(): Promise<void> {
      try {
        await connection.send('Browser.close');
      } catch {
        // The process is killed below either way.
      }
      connection.close();
      child.kill('SIGKILL');
      await new Promise<void>((resolve) => {
        if (child.exitCode !== null) resolve();
        else child.once('exit', () => resolve());
      });
      rmSync(profile, { recursive: true, force: true });
    },
  };
}
