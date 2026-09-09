/** Presentation only: callers supply already-admitted text; no source reads or links. */
const MAX_NESTING = 24;

function escapeHtml(text: string): string {
  return text.replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  })[character]!);
}

function inline(text: string, depth = 0): string {
  if (depth >= MAX_NESTING) return escapeHtml(text);
  let html = '';
  for (let i = 0; i < text.length;) {
    const rest = text.slice(i);
    const escaped = /^\\([\\`*_[\]{}()#+.!|>-])/.exec(rest);
    if (escaped) {
      html += escapeHtml(escaped[1]!);
      i += escaped[0].length;
      continue;
    }
    const ticks = /^`+/.exec(rest)?.[0];
    if (ticks) {
      const runs = /`+/g;
      runs.lastIndex = i + ticks.length;
      let end = -1;
      for (let match = runs.exec(text); match !== null; match = runs.exec(text)) {
        if (match[0].length === ticks.length) { end = match.index; break; }
      }
      if (end >= 0) {
        html += `<code>${escapeHtml(text.slice(i + ticks.length, end))}</code>`;
        i = end + ticks.length;
        continue;
      }
    }
    // Only a complete inline destination is consumed. Nested parentheses are
    // balanced, so a malicious URL cannot strand interpreted HTML in the tail.
    const link = /^!?\[([^\]\n]*)\]\(/.exec(rest);
    if (link) {
      let balance = 1;
      let end = i + link[0].length;
      for (; end < text.length && balance > 0; end++) {
        if (text[end] === '\\') end++;
        else if (text[end] === '(') balance++;
        else if (text[end] === ')') balance--;
      }
      if (balance === 0) {
        html += inline(link[1]!, depth + 1);
        i = end;
        continue;
      }
    }
    const marker = ['**', '__', '*', '_'].find((candidate) => rest.startsWith(candidate));
    if (marker && !(marker.includes('_') && /[\p{L}\p{N}]/u.test(text[i - 1] ?? ''))) {
      const end = text.indexOf(marker, i + marker.length);
      if (end > i + marker.length) {
        const tag = marker.length === 2 ? 'strong' : 'em';
        html += `<${tag}>${inline(text.slice(i + marker.length, end), depth + 1)}</${tag}>`;
        i = end + marker.length;
        continue;
      }
    }
    html += escapeHtml(text[i]!);
    i++;
  }
  return html;
}

function cells(line: string): string[] {
  const content = line.trim().replace(/^\|/, '').replace(/(?<!\\)\|$/, '');
  const cells: string[] = [];
  let cell = '';
  let codeRun = 0;
  for (let i = 0; i < content.length; i++) {
    const character = content[i]!;
    if (character === '\\' && i + 1 < content.length) { cell += character + content[++i]; continue; }
    if (character === '`') {
      const run = /^`+/.exec(content.slice(i))![0];
      if (codeRun === 0) codeRun = run.length;
      else if (codeRun === run.length) codeRun = 0;
      cell += run;
      i += run.length - 1;
    } else if (character === '|' && codeRun === 0) { cells.push(cell.trim()); cell = ''; }
    else cell += character;
  }
  cells.push(cell.trim());
  return cells;
}

function tableHeader(lines: string[], index: number): boolean {
  const first = lines[index];
  const second = lines[index + 1];
  if (!first?.includes('|') || !second) return false;
  const separators = cells(second);
  return separators.length === cells(first).length
    && separators.every((cell) => /^:?-{3,}:?$/.test(cell));
}

const listItem = /^( *)([-+*]|\d+[.)]) +(.*)$/;
const fenceStart = /^ {0,3}(`{3,}|~{3,})(.*)$/;

function diagramNodeAttrs(anchorId: string | undefined): string {
  return anchorId === undefined
    ? ' data-diagram-node data-non-normative data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable'
    : ` data-diagram-node data-anchor-id="${escapeHtml(anchorId)}"`;
}

/** Explicit flow fences contain data only; unsupported graphs stay literal. */
function flowDiagram(body: readonly string[], anchorId?: string): string | undefined {
  if (body.length !== 1) return undefined;
  const nodes = body[0]!.trim().split(/\s+-->\s+/);
  if (nodes.length < 2 || nodes.length > 12 || nodes.some((node) => !/^[\p{L}\p{N}][\p{L}\p{N} _()./&'-]{0,63}$/u.test(node))) return undefined;
  return `<ol class="source-flow" data-visual-provenance="curated" style="--flow-columns:${nodes.length}"${nodes.length > 6 ? ' data-flow-long' : ''}>${nodes.map((node, index) => `<li><span class="flow-node"${diagramNodeAttrs(anchorId)}>${escapeHtml(node)}</span>${index < nodes.length - 1 ? '<span class="flow-arrow" aria-hidden="true"> --&gt; </span>' : ''}</li>`).join('')}</ol>`;
}

function relationshipDiagram(body: readonly string[], depth: number, anchorId?: string): string | undefined {
  let rows: unknown;
  try { rows = JSON.parse(body.join('\n')); } catch { return undefined; }
  if (!Array.isArray(rows) || rows.length === 0 || rows.length > 8) return undefined;
  for (const row of rows) {
    if (row === null || typeof row !== 'object' || Array.isArray(row)
      || Object.keys(row).sort().join(',') !== 'description,from,to'
      || typeof row.from !== 'string' || !row.from.trim() || row.from.length > 128
      || typeof row.to !== 'string' || !row.to.trim() || row.to.length > 128
      || typeof row.description !== 'string' || !row.description.trim() || row.description.length > 8000) return undefined;
  }
  return `<div class="source-relationships" data-visual-provenance="curated">${rows.map((row) => `<section class="source-relationship" data-visual-provenance="curated"><div class="relationship-nodes"><strong${diagramNodeAttrs(anchorId)}>${escapeHtml(row.from)}</strong><span class="relationship-arrow" aria-hidden="true">→</span><strong${diagramNodeAttrs(anchorId)}>${escapeHtml(row.to)}</strong></div><div class="relationship-description">${blocks(row.description.split('\n'), depth + 1, anchorId)}</div></section>`).join('')}</div>`;
}

function blocks(lines: string[], depth = 0, anchorId?: string): string {
  if (depth >= MAX_NESTING) return `<pre>${escapeHtml(lines.join('\n'))}</pre>`;
  const output: string[] = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i]!;
    if (!line.trim()) { i++; continue; }
    if (/^(?: {4}|\t)/.test(line)) {
      const code: string[] = [];
      while (i < lines.length && (/^(?: {4}|\t)/.test(lines[i]!) || lines[i]!.trim() === '')) {
        code.push(lines[i++]!.replace(/^(?: {4}|\t)/, ''));
      }
      output.push(`<pre><code>${escapeHtml(code.join('\n'))}</code></pre>`);
      continue;
    }
    const fence = fenceStart.exec(line);
    if (fence) {
      const marker = fence[1]!;
      const body: string[] = [];
      i++;
      const closing = new RegExp(`^ {0,3}${marker[0]}{${marker.length},}\\s*$`);
      while (i < lines.length && !closing.test(lines[i]!)) body.push(lines[i++]!);
      if (i < lines.length) i++;
      const language = fence[2]!.trim();
      const diagram = language === 'flow' ? flowDiagram(body, anchorId) : language === 'relations' ? relationshipDiagram(body, depth, anchorId) : undefined;
      output.push(diagram ?? `<pre><code>${escapeHtml(body.join('\n'))}</code></pre>`);
      continue;
    }
    const heading = /^ {0,3}(#{1,6}) +(.+?)(?: +#+)? *$/.exec(line);
    if (heading) {
      const level = Math.min(6, heading[1]!.length + 3);
      output.push(`<h${level}>${inline(heading[2]!)}</h${level}>`);
      i++;
      continue;
    }
    if (/^ *>/.test(line)) {
      const quote: string[] = [];
      while (i < lines.length && /^ *>/.test(lines[i]!)) quote.push(lines[i++]!.replace(/^ *> ?/, ''));
      output.push(`<blockquote>${blocks(quote, depth + 1, anchorId)}</blockquote>`);
      continue;
    }
    if (tableHeader(lines, i)) {
      const header = cells(line);
      i += 2;
      const rows: string[] = [];
      while (i < lines.length && lines[i]!.includes('|') && lines[i]!.trim()) {
        rows.push(`<tr>${cells(lines[i++]!).map((cell) => `<td>${inline(cell)}</td>`).join('')}</tr>`);
      }
      output.push(`<div class="markdown-table"><table><thead><tr>${header.map((cell) => `<th scope="col">${inline(cell)}</th>`).join('')}</tr></thead><tbody>${rows.join('')}</tbody></table></div>`);
      continue;
    }
    const firstItem = listItem.exec(line);
    if (firstItem) {
      const indent = firstItem[1]!.length;
      const ordered = /^\d/.test(firstItem[2]!);
      const tag = ordered ? 'ol' : 'ul';
      const items: string[] = [];
      while (i < lines.length) {
        const item = listItem.exec(lines[i]!);
        if (!item || item[1]!.length !== indent || /^\d/.test(item[2]!) !== ordered) break;
        const content = [item[3]!];
        const contentIndent = item[0].length - item[3]!.length;
        i++;
        while (i < lines.length && lines[i]!.trim() && /^ */.exec(lines[i]!)![0].length > indent) {
          const continuation = lines[i++]!;
          const indentation = /^ */.exec(continuation)![0].length;
          content.push(continuation.slice(Math.min(contentIndent, indentation)));
        }
        // Preserve explicit numbering, including gaps in a source list.
        const value = ordered ? ` value="${Number.parseInt(item[2]!, 10)}"` : '';
        items.push(`<li${value}>${blocks(content, depth + 1, anchorId)}</li>`);
      }
      output.push(`<${tag}>${items.join('')}</${tag}>`);
      continue;
    }
    const paragraph = [line];
    i++;
    while (i < lines.length && lines[i]!.trim()
      && !fenceStart.test(lines[i]!) && !/^ {0,3}#{1,6} /.test(lines[i]!)
      && !/^ *>/.test(lines[i]!) && !listItem.test(lines[i]!) && !tableHeader(lines, i)) {
      paragraph.push(lines[i++]!);
    }
    output.push(`<p>${inline(paragraph.join('\n'))}</p>`);
  }
  return output.join('\n');
}

export function renderPolarisMarkdown(text: string, anchorId?: string): string {
  return blocks(text.replace(/\r\n?/g, '\n').split('\n'), 0, anchorId);
}
