// Render html/post-NN.html to png/post-NN.png at 1080x1350. Usage: node render.mjs [NN ...]
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { readdirSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const only = args.filter(a => /^\d+$/.test(a)).map(n => `post-${String(n).padStart(2, '0')}.html`);
const prefixes = args.filter(a => !/^\d+$/.test(a));
const files = readdirSync(join(here, 'html')).filter(f => f.endsWith('.html') && (!args.length || only.includes(f) || prefixes.some(p => f.startsWith(p)))).sort();
mkdirSync(join(here, 'png'), { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (const f of files) {
  await page.goto('file://' + join(here, 'html', f), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // flag anything that spills outside the 1080x1350 frame or overlaps the footer
  const issues = await page.evaluate(() => {
    const out = [], foot = document.querySelector('.foot').getBoundingClientRect();
    for (const el of document.querySelectorAll('.wrap *')) {
      const r = el.getBoundingClientRect();
      if (!r.width || getComputedStyle(el).position === 'absolute' && el.closest('svg')) continue;
      if (r.right > 1084 || r.left < -4 || r.bottom > 1354) out.push('off-frame: ' + el.textContent.trim().slice(0, 30));
      else if (r.bottom > foot.top - 6 && el.children.length === 0 && el.textContent.trim()) out.push('hits footer: ' + el.textContent.trim().slice(0, 30));
    }
    const h1 = document.querySelector('h1').getBoundingClientRect(), vis = document.querySelector('.vis').getBoundingClientRect();
    if (vis.height < 300) out.push('visual squeezed: ' + Math.round(vis.height) + 'px');
    return [...new Set(out)].slice(0, 4);
  });
  await page.screenshot({ path: join(here, 'png', f.replace('.html', '.png')) });
  console.log(f, issues.length ? 'CHECK ' + issues.join(' | ') : 'ok');
}
await browser.close();
