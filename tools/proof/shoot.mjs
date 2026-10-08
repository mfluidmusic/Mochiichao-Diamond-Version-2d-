// Headless Chromium screenshots of the proof harness (proof/harness).
// Usage: PW_CORE=/path/to/playwright-core node tools/proof/shoot.mjs <prefix> [baseUrl]
// Also logs every request to an external sprite host so "before" vs "after" network use is provable.
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_CORE || 'playwright-core');
const prefix = process.argv[2] || 'shot';
const base = process.argv[3] || 'http://localhost:3100';
const outDir = new URL('../../proof/', import.meta.url).pathname;
const shots = [
  ['battle_mochii_vs_razorgater', 'view=battle&party=001&enemy=004'],
  ['battle_kittember_vs_oblivirex', 'view=battle&party=010&enemy=009'],
  ['battle_sproutle_vs_reaperdile', 'view=battle&party=038&enemy=006'],
  ['battle_tiidebiite_vs_chromedile', 'view=battle&party=002&enemy=005'],
  ['roster_party', 'view=roster&party=001,004,007,010,038,003'],
  ['roster_party2', 'view=roster&party=002,005,008,039,006,009'],
  ['world_wild_battle', 'view=world&party=007'],
];
if (process.env.DEX) shots.push(['dex_all', 'view=dex']);
const browser = await chromium.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox'] });
const ext = new Set();
for (const [name, q] of shots) {
  const page = await browser.newPage({ viewport: { width: 1024, height: q.includes('dex') ? 1400 : 840 } });
  page.on('request', r => { const u = r.url(); if (!u.startsWith(base) && !u.startsWith('data:')) ext.add(u); });
  if (q.includes('view=world')) await page.addInitScript(() => { Math.random = () => 0.01; });
  await page.goto(`${base}/proof/harness/index.html?${q}`, { waitUntil: 'networkidle' });
  if (q.includes('view=world')) {
    await page.waitForTimeout(800);
    for (let i = 0; i < 4; i++) { await page.keyboard.press('ArrowRight'); await page.waitForTimeout(350); }
    await page.waitForTimeout(1500);
  } else await page.waitForTimeout(1500);
  await page.screenshot({ path: `${outDir}${prefix}_${name}.png`, fullPage: q.includes('dex') });
  console.log('saved', `${prefix}_${name}.png`);
  await page.close();
}
await browser.close();
fs.writeFileSync(`${outDir}${prefix}_external_requests.txt`, [...ext].join('\n') + (ext.size ? '\n' : ''));
console.log('external requests:', ext.size);
