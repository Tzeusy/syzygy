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
      const end = text.indexOf(ticks, i + ticks.length);
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
  return content.split(/(?<!\\)\|/).map((cell) => cell.trim());
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

function blocks(lines: string[], depth = 0): string {
  if (depth >= MAX_NESTING) return `<pre>${escapeHtml(lines.join('\n'))}</pre>`;
  const output: string[] = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i]!;
    if (!line.trim()) { i++; continue; }
    const fence = fenceStart.exec(line);
    if (fence) {
      const marker = fence[1]!;
      const body: string[] = [];
      i++;
      const closing = new RegExp(`^ {0,3}${marker[0]}{${marker.length},}\\s*$`);
      while (i < lines.length && !closing.test(lines[i]!)) body.push(lines[i++]!);
      if (i < lines.length) i++;
      output.push(`<pre><code>${escapeHtml(body.join('\n'))}</code></pre>`);
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
      output.push(`<blockquote>${blocks(quote, depth + 1)}</blockquote>`);
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
        items.push(`<li${value}>${blocks(content, depth + 1)}</li>`);
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

export function renderPolarisMarkdown(text: string): string {
  return blocks(text.replace(/\r\n?/g, '\n').split('\n'));
}
