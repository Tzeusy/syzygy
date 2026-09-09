import { describe, expect, it } from 'vitest';
import { renderPolarisMarkdown } from './polaris-markdown.js';

describe('Polaris admitted-text Markdown presentation', () => {
  it('formats headings and paragraphs without adding fragment identities', () => {
    expect(renderPolarisMarkdown('# Context\n\nOnly **observed** evidence\nmay count.\n\n### C#'))
      .toBe('<h4>Context</h4>\n<p>Only <strong>observed</strong> evidence\nmay count.</p>\n<h6>C#</h6>');
  });

  it('preserves qualifiers, literal code and unsupported syntax', () => {
    expect(renderPolarisMarkdown('*not* __accepted__; `**literal** <x>`\n\n~~unknown~~ and source_name_value'))
      .toBe('<p><em>not</em> <strong>accepted</strong>; <code>**literal** &lt;x&gt;</code></p>\n<p>~~unknown~~ and source_name_value</p>');
  });

  it('escapes active HTML, event handlers and entity-shaped source text', () => {
    const html = renderPolarisMarkdown('<script>alert(1)</script>\n<img src=x onerror="alert(2)"> &lt;iframe&gt;');
    expect(html).toBe('<p>&lt;script&gt;alert(1)&lt;/script&gt;\n&lt;img src=x onerror=&quot;alert(2)&quot;&gt; &amp;lt;iframe&amp;gt;</p>');
    expect(html).not.toMatch(/<(script|img|iframe)\b/i);
  });

  it('renders links and image labels inert, including unsafe nested destinations', () => {
    const html = renderPolarisMarkdown('[Visible](javascript:alert(1)) ![diagram <x>](https://x.invalid/a.png) [normal](https://example.test)');
    expect(html).toBe('<p>Visible diagram &lt;x&gt; normal</p>');
    expect(html).not.toMatch(/<(a|img)\b|href=|src=/);
  });

  it('keeps malformed links and reference syntax visible and inert', () => {
    expect(renderPolarisMarkdown('[missing](javascript:alert(1) [reference][id]\n\n[id]: javascript:alert(1)'))
      .toBe('<p>[missing](javascript:alert(1) [reference][id]</p>\n<p>[id]: javascript:alert(1)</p>');
  });

  it('renders fenced code literally and closes an unterminated fence safely', () => {
    expect(renderPolarisMarkdown('```html\n<script>**literal**</script>\n```\n\n~~~\n<x>'))
      .toBe('<pre><code>&lt;script&gt;**literal**&lt;/script&gt;</code></pre>\n<pre><code>&lt;x&gt;</code></pre>');
  });

  it('requires the closing fence to match the opening character and length', () => {
    expect(renderPolarisMarkdown('````\n```\n~~~\n````\nafter'))
      .toBe('<pre><code>```\n~~~</code></pre>\n<p>after</p>');
  });

  it('renders nested lists and preserves explicit ordered numbers and continuation text', () => {
    expect(renderPolarisMarkdown('3. Parent\n   qualifier\n   - Child\n     - Deeper\n7. Next\n\nOutside'))
      .toBe('<ol><li value="3"><p>Parent\nqualifier</p>\n<ul><li><p>Child</p>\n<ul><li><p>Deeper</p></li></ul></li></ul></li><li value="7"><p>Next</p></li></ol>\n<p>Outside</p>');
  });

  it('renders blockquotes with semantic nested content', () => {
    expect(renderPolarisMarkdown('> **Unknown**\n>\n> - Not measured'))
      .toBe('<blockquote><p><strong>Unknown</strong></p>\n<ul><li><p>Not measured</p></li></ul></blockquote>');
  });

  it('renders tables without dropping extra cells and escapes their contents', () => {
    expect(renderPolarisMarkdown('| Claim | State |\n| --- | :---: |\n| <img> | **Unknown** | qualifier |'))
      .toBe('<div class="markdown-table"><table><thead><tr><th scope="col">Claim</th><th scope="col">State</th></tr></thead><tbody><tr><td>&lt;img&gt;</td><td><strong>Unknown</strong></td><td>qualifier</td></tr></tbody></table></div>');
  });

  it('leaves a malformed table delimiter visible', () => {
    expect(renderPolarisMarkdown('| Claim | State |\n| -- | ??? |'))
      .toBe('<p>| Claim | State |\n| -- | ??? |</p>');
  });

  it('bounds nesting while retaining deeply nested content', () => {
    const html = renderPolarisMarkdown(`${'> '.repeat(1000)}<script>qualifier</script>`);
    expect(html).toContain('&lt;script&gt;qualifier&lt;/script&gt;');
    expect(html).not.toContain('<script>');
    expect(html.match(/<blockquote>/g)).toHaveLength(24);
  });
});


describe('literal code boundaries', () => {
  it('retains indented code without interpreting links or emphasis', () => {
    expect(renderPolarisMarkdown('    [literal](must-retain) **literal**')).toBe('<pre><code>[literal](must-retain) **literal**</code></pre>');
  });
  it('closes inline code only with an equal-length delimiter run', () => {
    expect(renderPolarisMarkdown('`a``[literal](must-retain)`')).toBe('<p><code>a``[literal](must-retain)</code></p>');
  });
  it('keeps pipes within a code span in their table cell', () => {
    const html = renderPolarisMarkdown('| Key | Meaning |\n| --- | --- |\n| `a|b` | Literal |');
    expect(html).toContain('<td><code>a|b</code></td><td>Literal</td>');
  });
});
