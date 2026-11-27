// Render v2/html/*.html to v2/png at 1080x1350 and flag text under 32px or outside the frame.
import { createRequire } from 'node:module';
import { readdirSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const { chromium } = createRequire(import.meta.url)('playwright');

const here = dirname(fileURLToPath(import.meta.url));
const only = process.argv.slice(2);
const files = readdirSync(join(here, 'html')).filter(f => f.endsWith('.html') && (!only.length || only.some(o => f.includes(o)))).sort();
mkdirSync(join(here, 'png'), { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (const f of files) {
  await page.goto('file://' + join(here, 'html', f), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const issues = await page.evaluate(() => {
    const out = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const n = walker.currentNode, el = n.parentElement, txt = n.textContent.trim();
      if (!txt || el.closest('.tag,.foot,style')) continue;
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < 32) out.push(`small ${fs}px: ${txt.slice(0, 24)}`);
      const r = el.getBoundingClientRect();
      if (r.right > 1084 || r.left < -4) out.push(`off-frame: ${txt.slice(0, 24)}`);
      const foot = document.querySelector('.foot').getBoundingClientRect();
      if (r.bottom > foot.top - 4 && r.top < foot.bottom && el.children.length === 0) out.push(`hits footer: ${txt.slice(0, 24)}`);
    }
    return [...new Set(out)].slice(0, 4);
  });
  await page.screenshot({ path: join(here, 'png', f.replace('.html', '.png')) });
  console.log(f, issues.length ? 'CHECK ' + issues.join(' | ') : 'ok');
}
await browser.close();
